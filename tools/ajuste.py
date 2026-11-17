#!/usr/bin/env python
"""Change a setting in Android 2.3's settings database (settings.db).

Android 2.3 has no `settings` command and does not accept `content insert`
from the shell. The only reliable way is to stop Android, edit the database
and start it again:

1. `su -c stop` (stops the Android interface; the phone shows black);
2. copies settings.db to the PC and saves a "before" copy in --respaldo;
3. changes (or creates) the value with sqlite3 on the PC and checks the
   database;
4. puts it back in place (overwriting the content, which keeps the owner and
   permissions) and runs `su -c start`.

Example (screen does not stay on while charging):
  python ajuste.py --serial SERIAL --respaldo respaldo/ system stay_on_while_plugged_in 0

Settings used on the XT550 (see docs/ajustes.md):
  system stay_on_while_plugged_in 0   screen does not stay on while charging
  system wifi_sleep_policy 1          Wi-Fi always on only while charging
  system haptic_feedback_enabled 0    no vibration when touching
  system vibrate_on 5                 "Vibrar: Siempre"
"""
import argparse, pathlib, re, shutil, sqlite3, subprocess, sys, time

DB = '/data/data/com.android.providers.settings/databases/settings.db'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--serial', required=True)
    ap.add_argument('--respaldo', required=True, type=pathlib.Path)
    ap.add_argument('--adb', default='adb')
    ap.add_argument('tabla', choices=['system', 'secure'])
    ap.add_argument('nombre')
    ap.add_argument('valor')
    a = ap.parse_args()
    adb = [a.adb, '-s', a.serial]

    def root(cmd):
        out = subprocess.run(adb + ['shell', "su -c '%s; echo __RC:$?'" % cmd],
                             capture_output=True, text=True).stdout.replace('\r', '')
        m = re.search(r'__RC:(\d+)\s*$', out)
        if not m or m.group(1) != '0':
            sys.exit('Falló como root: %s\n%s' % (cmd, out))
        return out[:m.start()]

    a.respaldo.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime('%Y%m%d-%H%M%S')
    before, after = a.respaldo / ('settings-%s-antes.db' % stamp), a.respaldo / ('settings-%s-despues.db' % stamp)

    root('stop')
    try:
        time.sleep(3)
        root('cat %s > /data/local/tmp/s.db && chmod 644 /data/local/tmp/s.db' % DB)
        subprocess.run(adb + ['pull', '/data/local/tmp/s.db', str(before)], check=True, capture_output=True)
        shutil.copy(before, after)
        c = sqlite3.connect(after)
        old = c.execute('select value from %s where name=?' % a.tabla, (a.nombre,)).fetchone()
        if old is None:
            c.execute('insert into %s (name, value) values (?, ?)' % a.tabla, (a.nombre, a.valor))
        else:
            c.execute('update %s set value=? where name=?' % a.tabla, (a.valor, a.nombre))
        c.commit()
        assert c.execute('pragma integrity_check').fetchone()[0] == 'ok'
        c.close()
        print('%s.%s: %s -> %s' % (a.tabla, a.nombre, old[0] if old else '(no existía)', a.valor))
        subprocess.run(adb + ['push', str(after), '/data/local/tmp/s.db'], check=True, capture_output=True)
        root('cat /data/local/tmp/s.db > %s && rm /data/local/tmp/s.db' % DB)
    finally:
        root('start')
    print('Listo. Copia de antes: %s' % before)


if __name__ == '__main__':
    main()
