# Volver atrás

Todo se puede deshacer. Necesitás el respaldo de fábrica (paso 1) y root.

## Reinstalar una app de fábrica borrada

1. Buscá su archivo en [paquetes-borrados.md](paquetes-borrados.md), que tiene la ruta original y el SHA256.
2. Verificá que tu copia tenga ese hash.
3. Subila a su carpeta:

```
adb -s SERIAL push respaldo/flex-app/App.apk /data/local/tmp/App.apk
adb -s SERIAL shell su -c 'mount -o remount,rw -t yaffs2 /dev/block/mtdblock14 /flex'
adb -s SERIAL shell su -c '/data/local/tmp/busybox cp /data/local/tmp/App.apk /flex/app/App.apk'
adb -s SERIAL shell su -c 'chmod 644 /flex/app/App.apk; mount -o remount,ro -t yaffs2 /dev/block/mtdblock14 /flex'
adb -s SERIAL reboot
```

- Para `/system` es igual, con `/dev/block/mtdblock11 /system`.
- Si tenía `.odex`, subilo también.
- Si la app sigue desactivada después de reiniciar: `su -c 'pm enable <paquete>'`.

Los datos de la app (si los tenía) están en la copia que se hizo al borrarla. Se restauran con `tar`. Después hay que devolverle el dueño a la carpeta: ver [lecciones.md](lecciones.md#datos-de-apps).

## Ícono de batería original

En el teléfono quedó una copia del archivo de fábrica y un script que lo pone de nuevo:

```
adb -s SERIAL shell su -c 'sh /data/local/tmp/restore-fr.sh'
adb -s SERIAL reboot
```

El script verifica el SHA256 de la copia (`670bd9f0…9ead9b`) antes de usarla. Esto funciona aunque Android no termine de arrancar: `adb` y `su` andan desde el arranque, y el `su` le da root a la conexión USB sin preguntarle a la app Superuser.

## Un ajuste

[`tools/ajuste.py`](../tools/ajuste.py) guarda una copia de `settings.db` antes y después de cada cambio. Para volver atrás, poné de nuevo el valor anterior (ver [ajustes.md](ajustes.md)). También podés subir la copia "antes" con el mismo procedimiento.

## El root

- Para sacar el root: borrá `/system/bin/su` y desinstalá Superuser (`pm uninstall com.noshufou.android.su`).
- Las apps de Google, Motorola y del gestor chino no se reinstalan solas.

## Todo el teléfono

El firmware original del XT550 (`ARGONS_LATAM_Retail.sbf`) se puede grabar con RSD Lite en modo flash. **No lo probamos.** En este teléfono no encontramos la combinación de teclas que entra a modo flash: el modo existe en el firmware, pero no la confirmamos. Por eso todo se hizo con respaldo y verificación paso a paso, sin flashear nada.
