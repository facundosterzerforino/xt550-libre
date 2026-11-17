# Lo que queda de fábrica

Análisis de los paquetes que no son nuestros. Se contaron las clases de cada ODEX con `dexdump`: cuántas son de Android (AOSP) y cuántas del fabricante (Motorola, Cellon, Qualcomm).

| Pieza | Clases | Del fabricante | ¿Se puede reemplazar? |
|---|---|---|---|
| Mensajes (`com.android.mms`) | 525 | 57: pantallas de Cellon y un "firewall" de SMS de Motorola | **Sí**: el Mensajes de AOSP 2.3.6 recompilado. Pendiente: los SMS no se pueden probar sin chip. |
| Ajustes (`com.android.settings`) | 549 | 49: accesos rápidos de Motorola | No: corre como `system` y necesita la firma de Motorola. |
| Contactos y marcador (`com.android.contacts`) | 343 | 6: servicio de ubicación de números | Posible, pero gana poco y arriesga las llamadas, incluidas las de emergencia. |
| Teléfono (`com.android.phone`) | 451 | 6 | No: corre como `radio` y necesita la firma. |
| Cámara (`com.android.camera`) | 172 | 0 | Posible (es AOSP puro). Sin microSD no se puede probar que guarde fotos. |
| Barra de estado, Bluetooth, SIM, instalador, visor HTML | — | 0 | Ya son AOSP; sin la firma no se pueden cambiar. |
| Proveedores (contactos, SMS, medios, descargas, ajustes...) | — | 0 | Ídem. |
| Alerter (`com.qualcomm.alerter`) | 15 | 15 (cerrado) | Alertas de emergencia por difusión celular. Se deja a propósito. |
| `framework-res.apk` | — | — | Modificado por nosotros (batería con %). |

Además siguen siendo de fábrica:
- el kernel 2.6.38;
- los drivers (cámara, Wi-Fi, módem, gráficos);
- el DRM de Discretix (`libDxDrm*`, `DxDrmServerIpc`): el framework de Motorola lo llama desde MediaPlayer, MediaScanner, webkit y MMS;
- los binarios de `/system/bin`.

No existe ninguna ROM libre (CyanogenMod, etc.) para el XT550, y no se encontró la forma de entrar a su modo de carga de firmware.
