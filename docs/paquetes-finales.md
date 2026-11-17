# Lo que quedó instalado (35 paquetes)

Estado al 16/11/2026. Antes había 112.

## Libre

| Paquete | Qué es | Archivo |
|---|---|---|
| `acr.browser.barebones` | Navegador (Lightning) con HTTPS moderno. | `/data/app/acr.browser.barebones-1.apk` |
| `com.noshufou.android.su` | Superuser (permisos de root; oculta del cajón). | `/data/app/com.noshufou.android.su-2.apk` |
| `net.sourceforge.solitaire_cg` | SolitaireCG (solitario). | `/data/app/net.sourceforge.solitaire_cg-1.apk` |
| `org.adw.launcher` | ADW.Launcher 1.3.6 (pantalla de inicio). | `/data/app/org.adw.launcher-2.apk` |
| `org.librecalculadora` | Calculadora. | `/data/app/org.librecalculadora-1.apk` |
| `org.libregaleria` | Galería. | `/data/app/org.libregaleria-1.apk` |
| `org.librehora` | Hora por Internet. | `/data/app/org.librehora-2.apk` |
| `org.libremusic.simple` | Música Simple. | `/data/app/org.libremusic.simple-2.apk` |
| `org.librereloj` | Reloj y alarmas. | `/data/app/org.librereloj-2.apk` |
| `org.libreteclado.latin` | Teclado Libre (español con sugerencias). | `/data/app/org.libreteclado.latin-2.apk` |

## Teléfono

| Paquete | Qué es | Archivo |
|---|---|---|
| `com.android.contacts` | Contactos y marcador (Teléfono). | `/system/app/Contacts.apk` |
| `com.android.mms` | Mensajes (SMS/MMS). | `/system/app/Mms.apk` |
| `com.android.phone` | Llamadas y radio celular. | `/system/app/Phone.apk` |
| `com.android.stk` | Menú de la tarjeta SIM. | `/system/app/Stk.apk` |
| `com.cellon.fastdormancy` | Ahorro de batería en datos 3G (con datos apagados no hace nada). | `/system/app/CellonFastDormancy.apk` |

## Multimedia

| Paquete | Qué es | Archivo |
|---|---|---|
| `com.android.camera` | Cámara de Motorola (sin tocar). | `/system/app/Camera.apk` |

## Sistema

| Paquete | Qué es | Archivo |
|---|---|---|
| `android` | Recursos de Android (framework-res). **Modificado**: batería con porcentaje (ver [xt550-battery-percent](https://github.com/facundosterzerforino/xt550-battery-percent)). | `/system/framework/framework-res.apk` |
| `com.android.bluetooth` | Bluetooth. | `/system/app/Bluetooth.apk` |
| `com.android.defcontainer` | Ayudante del instalador. | `/system/app/DefaultContainerService.apk` |
| `com.android.htmlviewer` | Visor de HTML (licencias, etc.). | `/system/app/HTMLViewer.apk` |
| `com.android.packageinstaller` | Instalador de apps. | `/system/app/PackageInstaller.apk` |
| `com.android.settings` | Ajustes. | `/system/app/Settings.apk` |
| `com.android.systemui` | Barra de estado. | `/system/app/SystemUI.apk` |
| `com.qualcomm.alerter` | Alertas de emergencia por difusión celular (Qualcomm). | `/system/app/Alerter.apk` |
| `com.qualcomm.privinit` | Ajusta caché/hilos de red al arrancar (Qualcomm); inofensivo. | `/system/app/PrivInit.apk` |

## Datos

| Paquete | Qué es | Archivo |
|---|---|---|
| `com.android.providers.applications` | Búsqueda de apps. | `/system/app/ApplicationsProvider.apk` |
| `com.android.providers.calendar` | Base de calendario (otros componentes la consultan). | `/system/app/CalendarProvider.apk` |
| `com.android.providers.contacts` | Base de contactos y registro de llamadas. | `/system/app/ContactsProvider.apk` |
| `com.android.providers.downloads` | Motor de descargas (lo usa el Navegador). | `/system/app/DownloadProvider.apk` |
| `com.android.providers.drm` | Proveedor DRM (lo usa el sistema de medios de Motorola). | `/system/app/DrmProvider.apk` |
| `com.android.providers.media` | Índice de música y fotos. | `/system/app/MediaProvider.apk` |
| `com.android.providers.settings` | Base de ajustes. | `/system/app/SettingsProvider.apk` |
| `com.android.providers.subscribedfeeds` | Cuentas y sincronización (Ajustes). | `/system/app/AccountAndSyncSettings.apk` |
| `com.android.providers.telephony` | Base de SMS/MMS y APN. | `/system/app/TelephonyProvider.apk` |
| `com.android.providers.userdictionary` | Palabras del usuario del teclado. | `/system/app/UserDictionaryProvider.apk` |

Fuera de los paquetes también se cambiaron:

- `/system/bin/su`: `su` 3.2 libre (ver [su-binary](https://github.com/facundosterzerforino/su-binary)).
- `/data/local/tmp/busybox`: BusyBox 1.38.0 compilado (ver [busybox](https://github.com/facundosterzerforino/busybox)). Solo lo usa la PC por USB.
