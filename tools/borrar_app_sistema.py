#!/usr/bin/env python
"""Delete system apps from a rooted Android 2.3 phone, with a backup first.

By default it only CHECKS and prints the plan; nothing is changed. With
--aplicar it deletes.

For each package it:
1. finds its APK (and ODEX) with `pm list packages -f`;
2. computes the SHA256 on the phone and compares it with the copy in the PC
   backup folder (--respaldo: a copy of /system/app and /flex/app made
   BEFORE touching anything, for example with `adb pull /system/app`). If the
   copy is missing or different, it stops. That way every deleted file can be
   put back;
3. saves the app's data (/data/data/<package>, without lib) to
   <respaldo>/datos/<package>.tgz;
4. with --aplicar: `pm disable`, mounts /system (and /flex if present) as
   writable, deletes the files, ALWAYS mounts them read-only again, and
   cleans up the dalvik-cache and the data.

Then restart the phone.

Requirements: adb, root (`su` that accepts `su -c` from the shell) and a
busybox with sha256sum and tar on the phone (--busybox).

Example:
  python borrar_app_sistema.py --serial SERIAL --respaldo respaldo/ com.example.app
  python borrar_app_sistema.py --serial SERIAL --respaldo respaldo/ --aplicar com.example.app
"""
import argparse, hashlib, pathlib, re, subprocess, sys, time


class Phone:
    def __init__(self, adb, serial):
        self.base = [adb, '-s', serial]

    def sh(self, cmd):
        r = subprocess.run(self.base + ['shell', cmd], capture_output=True, text=True)
        return r.stdout.replace('\r', '')

    def root(self, cmd):
        """Runs as root. Returns (code, output); the code is read INSIDE su, because some su return 0 anyway."""
        out = self.sh("su -c '%s; echo __RC:$?'" % cmd.replace("'", "'\\''"))
        m = re.search(r'__RC:(\d+)\s*$', out)
        return (int(m.group(1)) if m else -1), out[:m.start()] if m else out

    def pull(self, remote, local):
        subprocess.run(self.base + ['pull', remote, str(local)], check=True, capture_output=True)


def sha256(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--serial', required=True)
    ap.add_argument('--respaldo', required=True, type=pathlib.Path)
    ap.add_argument('--adb', default='adb')
    ap.add_argument('--busybox', default='/data/local/tmp/busybox')
    ap.add_argument('--aplicar', action='store_true', help='delete for real (without this it only checks)')
    ap.add_argument('paquetes', nargs='+')
    a = ap.parse_args()
    ph, bb = Phone(a.adb, a.serial), a.busybox

    paths = {}
    for line in ph.sh('pm list packages -f').splitlines():
        if line.startswith('package:'):
            path, name = line[8:].strip().rsplit('=', 1)
            paths[name] = path
    local = {p.name: p for p in a.respaldo.rglob('*') if p.is_file()}

    plan = []
    for pkg in a.paquetes:
        if pkg not in paths:
            sys.exit('%s: no está instalado' % pkg)
        files = [paths[pkg]]
        odex = paths[pkg][:-4] + '.odex'
        if ph.root('ls %s' % odex)[0] == 0:
            files.append(odex)
        for f in files:
            code, out = ph.root('%s sha256sum %s' % (bb, f))
            phone_hash = out.split()[0] if code == 0 and out.strip() else None
            name = pathlib.PurePosixPath(f).name
            pc_hash = sha256(local[name]) if name in local else None
            ok = phone_hash is not None and phone_hash == pc_hash
            print('%-4s %s  tel=%s  pc=%s' % ('OK' if ok else 'MAL', f, (phone_hash or '-')[:16], (pc_hash or 'sin copia')[:16]))
            if not ok:
                sys.exit('Frenado: %s no tiene una copia idéntica en %s' % (f, a.respaldo))
            plan.append((pkg, f))

    datos = a.respaldo / 'datos'
    datos.mkdir(parents=True, exist_ok=True)
    for pkg in a.paquetes:
        if ph.root('ls /data/data/%s' % pkg)[0] != 0:
            continue
        tmp = '/data/local/tmp/%s.tgz' % pkg
        code, out = ph.root('%s tar czf %s -C /data/data --exclude=%s/lib %s && chmod 644 %s' % (bb, tmp, pkg, pkg, tmp))
        if code != 0:
            sys.exit('No se pudo respaldar los datos de %s: %s' % (pkg, out))
        ph.pull(tmp, datos / (pkg + '.tgz'))
        ph.root('rm %s' % tmp)
        print('datos de %s -> %s' % (pkg, datos / (pkg + '.tgz')))

    if not a.aplicar:
        print('\nSolo verificación. Para borrar de verdad, repetí con --aplicar.')
        return

    mounts = {}
    for line in ph.sh('mount').splitlines():
        f = line.split()
        if len(f) >= 3 and f[1] in ('/system', '/flex'):
            mounts[f[1]] = (f[0], f[2])
    for pkg in a.paquetes:
        print(ph.root('pm disable %s' % pkg)[1].strip())
    try:
        for mp, (dev, fs) in mounts.items():
            ph.root('mount -o remount,rw -t %s %s %s' % (fs, dev, mp))
        for pkg, f in plan:
            code, out = ph.root('rm %s' % f)
            print('borrado' if code == 0 else 'ERROR', f, out.strip())
    finally:
        for mp, (dev, fs) in mounts.items():
            for _ in range(6):  # right after rm it can say "busy": retry
                ph.root('sync; mount -o remount,ro -t %s %s %s' % (fs, dev, mp))
                if any(l.split()[1:2] == [mp] and ' ro,' in l for l in ph.sh('mount').splitlines()):
                    break
                time.sleep(3)
    for pkg, f in plan:
        if f.endswith('.apk'):
            ph.root('rm /data/dalvik-cache/%s@classes.dex' % f.strip('/').replace('/', '@'))
    for pkg in a.paquetes:
        ph.root('rm -r /data/data/%s' % pkg)
    print('\nListo. Reiniciá el teléfono (adb reboot) y verificá con: adb shell pm list packages')
    print([l for l in ph.sh('mount').splitlines() if ' /system ' in l or ' /flex ' in l])


if __name__ == '__main__':
    main()
