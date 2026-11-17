# Ajustes

Cambios de configuración que no son apps. Salvo las animaciones y la zona horaria, se hicieron editando `settings.db` con [`tools/ajuste.py`](../tools/ajuste.py). En 2.3 no existe el comando `settings`, y `content insert` no anda desde el shell.

| Ajuste | Tabla / nombre | Antes | Después | Por qué |
|---|---|---|---|---|
| Pantalla encendida mientras carga | `system / stay_on_while_plugged_in` | 3 (siempre, con USB o cargador) | 0 | Gastaba pantalla y calentaba el teléfono cada vez que estaba enchufado. |
| Wi-Fi con la pantalla apagada | `system / wifi_sleep_policy` | 2 (nunca se apaga) | 1 (nunca mientras carga) | A batería se apaga 15 min después de apagar la pantalla y vuelve solo al prenderla. |
| Vibración al tocar | `system / haptic_feedback_enabled` | 1 | 0 | Ahorro y pedido del usuario. |
| Vibración de llamadas | `system / vibrate_on` | 6 | 5 ("Vibrar: Siempre") | Al borrar "Modo de timbre" se dejó la vibración al máximo. |
| Animaciones | `service call window 42` | 1.0 / 1.0 | 0 / 0 | Más rápido. Ver [paso-a-paso.md](paso-a-paso.md#4-pantalla-de-inicio-y-animaciones). |
| Zona horaria | `persist.sys.timezone` | (GMT) | `America/Argentina/Buenos_Aires` | El reloj mostraba la hora de Londres. `su -c 'setprop persist.sys.timezone America/Argentina/Buenos_Aires'` y reiniciar. |
| Datos móviles | `secure / mobile_data` | 0 | 0 | Ya estaban apagados; se dejaron así. |

Lo que se revisó y **no hacía falta tocar**:
- **Brillo automático**: anda (sensor TSL2550) y queda bajo.
- **Procesador**: modo `ondemand` (480–800 MHz).
- **GPS y Bluetooth**: apagados.
- **Wake locks**: después de los cambios no queda ninguno, y nada despierta al teléfono salvo el reloj del sistema.

El teclado de AOSP 2.3 trae la vibración apagada por defecto (`vibrate_on` en sus preferencias), así que no hubo que cambiar nada ahí.

## Cómo cambiar uno a mano

```
adb -s SERIAL shell su -c stop          # apaga la interfaz de Android
adb -s SERIAL shell "su -c 'cat /data/data/com.android.providers.settings/databases/settings.db > /data/local/tmp/s.db; chmod 644 /data/local/tmp/s.db'"
adb -s SERIAL pull /data/local/tmp/s.db
sqlite3 s.db "update system set value='0' where name='stay_on_while_plugged_in'"
adb -s SERIAL push s.db /data/local/tmp/s.db
adb -s SERIAL shell "su -c 'cat /data/local/tmp/s.db > /data/data/com.android.providers.settings/databases/settings.db'"
adb -s SERIAL shell su -c start         # vuelve a arrancar la interfaz
```

Se usa `cat >` en vez de `cp` o `mv`, para que el archivo conserve su dueño (`system`) y sus permisos.
