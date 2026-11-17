# Lecciones de Android 2.3

Cosas que nos hicieron perder tiempo. Valen para casi cualquier teléfono con Gingerbread rooteado.

## Shell y comandos

- El `sh` de 2.3 (toolbox) **no tiene** `[`, `cp`, `mkdir -p`, `printf`, `head`, `touch` ni las expansiones `${v%%x}`.
  - Usá un BusyBox (`/data/local/tmp/busybox [ ... ]`).
  - Si el comando es largo, subí un script y ejecutalo; los `su -c '...'` complicados fallan sin avisar.
- `ps` devuelve líneas con `\r` al final. Hacé `tr -d '\r'` antes de `awk`, o el PID sale vacío (y `kill` sin PID falla sin que te des cuenta).
- `ps <nombre>` no filtra bien. Traé la lista completa y filtrá en la PC.
- No existen `pm list packages -s/-3`: usá `pm list packages -f` y mirá la ruta.
- No existen `settings`, `input tap`, `am force-stop` ni `sqlite3`.
  - Para tocar la pantalla se usa `sendevent` sobre el nodo táctil.
  - `input keyevent 26` no prende la pantalla: en el XT550, `sendevent /dev/input/event6 1 116 1` y luego `... 0`.
- `adb shell cat` de un binario lo corrompe (convierte saltos de línea). Usá `adb pull`.

## Root y su

- Algunos `su` devuelven 0 aunque el comando falle. Leé el código **dentro** del su: `su -c 'comando; echo __RC:$?'`.
- Cuando una app lee la salida de `su`, la primera línea puede venir vacía.
- El cuadro de permiso de Superuser 3.x recuerda la última elección de "Recordar". Fijate que esté tildado.
- Para que Superuser no muestre un aviso cada vez que una app usa root: `apps.notifications=0` en su `su.db`, con Superuser cerrado.
- Después de `rm` en `/system`, el `remount,ro` puede fallar con "busy". Reintentá a los segundos y verificá con `mount`.

## Archivos del sistema

- Un archivo que el sistema tiene abierto, como `framework-res.apk`, no se sobrescribe. Se copia a `.new`, se renombra con `mv` y se reinicia.
- En Android 2.x, para apps del sistema, solo se verifica la firma de `AndroidManifest.xml` (`PARSE_IS_SYSTEM` en `PackageParser`). Se pueden cambiar recursos sin re-firmar. En versiones nuevas esto ya no es así.
- La herramienta de root puede dejar copias del mismo APK en `/system/app` **y** en `/data/app`. Si borrás una, Android levanta la otra.

## Datos de apps

- `settings.db` y otras bases solo se editan con la app (o Android) detenida. Si usan WAL, hay que traer `.db`, `-wal` y `-shm` juntos y dejar `journal_mode=DELETE` al guardar.
- Al restaurar `/data/data/<paquete>` con `tar` como root, la carpeta queda a nombre de root. Android lo marca como `mismatched_uid` y le cambia la ruta de librerías en `packages.xml`. Para arreglarlo:
  1. `chown <uid>.<uid>` y `chmod 751` a la carpeta;
  2. `lib` con dueño `1000:1000` y permisos 755;
  3. `pm install -r` del mismo APK.

## Compilar para 2.3

- Apps de AOSP 2.3 fuera del árbol: aapt rechaza `@+android:id`; hay que cambiarlo por `@+id` y declarar el id. Algunas usan métodos que solo están en el `android.jar` de la API 10.
- Paquete renombrado: usá `aapt --rename-manifest-package`. Cambiar `package=` rompe los namespaces de atributos propios.
- Los diccionarios del teclado de AOSP 4.1+ son de otro formato y el código nativo de 2.3 no los lee.
- El NDK r10e de Windows no trae `ndk-build`: llamá a gcc directo.
- `/dev/random` en el kernel 2.6.38 puede tardar minutos; usá `/dev/urandom`.
- El kernel 2.6.38 no tiene `getrandom()`, ni Bionic de API 9 tiene `statvfs`, `utimensat` o `syncfs` (importa al compilar BusyBox).

## Medios y DRM (Motorola)

- El MediaPlayer de Motorola intenta DRM (Discretix) cuando recibe una **ruta**. Con un **descriptor** (`setDataSource(FileDescriptor)`) reproduce sin problemas.
- No borres las librerías DRM ni `DxDrmServerIpc`: MediaPlayer, MediaScanner, webkit y MMS de Motorola las llaman. Sin ellas no suena ni la alarma.

## Hora

- Sin chip, Android 2.3 nunca pone la hora sola.
- El `date -s` de toolbox pasa por `/dev/alarm`, así que fija también el reloj de hardware y avisa al sistema. El `date -s` de BusyBox solo cambia la hora del kernel, y después de reiniciar vuelve la vieja.
- Con la fecha mal, ningún sitio HTTPS abre: todos los certificados parecen vencidos o "todavía no válidos".
