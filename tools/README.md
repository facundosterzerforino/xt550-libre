# Herramientas

Scripts para teléfonos con **Android 2.3 rooteado**. Se usaron con el Motorola XT550 y se probaron contra él:
- `borrar_app_sistema.py`: en modo verificación (frena si falta la copia, y si está, guarda los datos);
- `ajuste.py`: cambiando un valor real.

Necesitan Python 3, `adb` y, en el teléfono, `su` y un BusyBox (ver [busybox](https://github.com/facundosterzerforino/busybox)).

## borrar_app_sistema.py

Borra apps de sistema solo si tenés una copia idéntica en la PC. Por defecto **solo verifica**.

```
adb -s SERIAL pull /system/app respaldo/system-app      # una vez, ANTES de tocar nada
adb -s SERIAL pull /flex/app   respaldo/flex-app        # (solo Motorola: /flex)

python borrar_app_sistema.py --serial SERIAL --respaldo respaldo com.ejemplo.app
python borrar_app_sistema.py --serial SERIAL --respaldo respaldo --aplicar com.ejemplo.app
adb -s SERIAL reboot
```

## ajuste.py

Cambia un valor de `settings.db` (tablas `system` o `secure`) y guarda una copia antes y después.

```
python ajuste.py --serial SERIAL --respaldo respaldo-ajustes system stay_on_while_plugged_in 0
```

La interfaz de Android se apaga unos segundos (`stop` / `start`) mientras cambia el valor.
