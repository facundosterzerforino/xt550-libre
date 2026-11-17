# Paso a paso

Cómo se hizo todo, en el orden en que se hizo. Los comandos son para un Motorola XT550 con Android 2.3.6 (build `ARGONS_4_07.1B.16RPS`). En otro teléfono, los nombres de particiones, nodos y paquetes pueden cambiar.

> En todos los comandos, `SERIAL` es el número de serie que muestra `adb devices`.

## 0. Preparación

- PC con Windows, `adb` (platform-tools de Google) y los drivers de Motorola.
- En el teléfono: *Ajustes → Aplicaciones → Desarrollo → Depuración USB*.
- Herramientas para compilar (las mismas para todas las apps):
  - JDK 17 (Temurin);
  - Android build-tools 30.0.3 (`aapt`, `d8`, `zipalign`, `apksigner`);
  - `android.jar` de la API 10 (2.3.3);
  - NDK r10e para el código C.

  No usamos Gradle: cada repo tiene un `build.py` que llama a esas herramientas directamente. La clave de firma vive fuera de los repos.

## 1. Respaldo de fábrica

Antes de cualquier cambio:

```
adb -s SERIAL pull /system/app respaldo/system-app
adb -s SERIAL pull /flex/app   respaldo/flex-app
```

Salieron 170 archivos (APK y ODEX, 94 MB). Calculamos el SHA256 de cada uno. Ese respaldo es lo que permite volver atrás cualquier borrado ([recuperar.md](recuperar.md)).

En el XT550 las apps de fábrica están en dos particiones:
- `/system` (`/dev/block/mtdblock11`);
- `/flex` (`/dev/block/mtdblock14`, apps de Motorola y del operador).

## 2. Root

- **zergRush** (exploit libre clásico de 2.3) **falló** en este firmware.
- La guía del XT550 en XDA usa **Romaster** (MGYun). Recuperamos el instalador original de 2015 de Internet Archive (firma Authenticode de MGYun válida) y lo extrajimos sin instalar.
- Usamos solo el módulo `root.exe`, con un solo teléfono conectado. Funcionó al primer intento: `su -c id` → `uid=0(root)`.

Romaster dejó tres cosas que **no queríamos**:
- el gestor `com.mgyun.shua.su` ("ROOT大师"): leía SMS y contactos, tenía internet y el push de Tencent (XGService);
- una tienda de apps (`com.mgyapp.android`);
- copias ocultas de `su` en `/system/bin/.suv` y `/system/usr/.suv`, más un script que las recreaba.

En el paso 9 se reemplazó todo.

## 3. Limpieza

Cada tanda siguió el mismo procedimiento, que quedó en [`tools/borrar_app_sistema.py`](../tools/borrar_app_sistema.py):

1. Ubicar el APK y el ODEX con `pm list packages -f`.
2. Calcular el SHA256 en el teléfono y compararlo con el respaldo. Si no coincide, no se borra.
3. Guardar `/data/data/<paquete>` en la PC.
4. Correr `pm disable`, montar `/system` y `/flex` como escritura, borrar los archivos y **siempre** volver a solo lectura. Justo después de borrar, el sistema a veces dice "busy": hay que reintentar a los segundos.
5. Borrar su `dalvik-cache` y sus datos.
6. Reiniciar y verificar:
   - que desaparecieron exactamente esos paquetes y ningún otro;
   - que hay root;
   - que `/system` y `/flex` quedaron en solo lectura;
   - que Teléfono, Contactos, Mensajes, Cámara y el resto abren.

Al principio movíamos las apps a una carpeta de cuarentena. Después se borraron, porque la copia en la PC alcanza.

**Antes de borrar algo dudoso** buscamos quién lo usa. `dexdump` sobre los ODEX de Teléfono, Mensajes, Contactos, Ajustes y `framework.odex` muestra si alguien llama a ese paquete y qué pasa si no está. Ejemplos:
- **Respuestas rápidas al rechazar una llamada** (`com.cellon.quicksms`): Teléfono la llama sin `try/catch`, solo cuando se elige "Rechazar con mensaje". Se aceptó ese riesgo.
- **DRM de Discretix**: el framework de Motorola lo llama desde MediaPlayer, MediaScanner, webkit y MMS. Se borró la app, pero se dejaron las librerías y el servicio. Sin ellos no sonaría ni la alarma.
- **Teclado de Android de fábrica**: se borró la app, pero `libjni_latinime.so` queda, porque la usa Teclado Libre.

Las 12 tandas, con cada paquete, están en [paquetes-borrados.md](paquetes-borrados.md).

## 4. Pantalla de inicio y animaciones

- Se instaló **ADW.Launcher 1.3.6** (al principio el de F-Droid, después compilado por nosotros) y se borró MotoHome 3D.
- **Animaciones**: Android 2.3 no tiene un comando para cambiarlas. Leyendo `framework.odex` encontramos el número de la llamada `setAnimationScale` (42) de `IWindowManager` en este firmware. Con eso:

  ```
  su -c 'service call window 42 i32 0 i32 0'   # animación de ventanas
  su -c 'service call window 42 i32 1 i32 0'   # transiciones
  ```

  Los números cambian según el firmware: no los copies a otro teléfono sin verificar.
- **Cajón**: ADW permite grupos. El grupo "Apps" lista solo lo que se usa. Está en `shared_prefs/APP_CATALOG_1.xml` de ADW, y las apps nuevas se agregan ahí a mano. Las flechas para cambiar de grupo se ocultaron (`drawer_navigate_catalogs=false`).

## 5. Google afuera

Se sacaron:
- Play Store y su actualizador;
- los servicios de Google (`gsf`) y la ubicación por red;
- Maps, Búsqueda, la búsqueda por voz y la sincronización de contactos y calendario;
- Gmail, el asistente de configuración y TuneWiki.

El teléfono no tenía cuenta de Google. **Ojo:** `Mms.apk` declara como *requerida* la librería `com.google.android.browser`. Las librerías y sus XML no se tocaron, para no romper los SMS.

## 6. Música y teclado

- **Música Simple**: app propia de 17 KB, sin internet.
  - Reproduce desde la memoria interna o la tarjeta, abriendo el archivo con `FileInputStream` y pasando el descriptor a `MediaPlayer`. Si le pasa la ruta, el MediaPlayer de Motorola intenta DRM y falla.
  - El botón físico de música del XT550 manda el broadcast `com.motorola.mmsp.ACTION_MUSIC`. Música Simple lo recibe y pausa o reanuda sin abrir nada.
  - Reemplazó a Música y al Panel de música de Motorola.
- **Teclado Libre**: el teclado de Motorola tenía un diccionario de 34 bytes, o sea ninguna sugerencia.
  - Tomamos el teclado de AOSP 2.3.6 y le agregamos el diccionario español de AOSP (60.000 palabras), convertido al formato que entiende 2.3. Los diccionarios de 4.1 en adelante no sirven.
  - Usa la librería nativa que ya trae el teléfono.
  - Reemplazó a Swype y al teclado de Motorola.

## 7. Regla: todo desde el código

Desde acá, ningún APK precompilado. Para cada app:
1. Fork en GitHub del proyecto original.
2. Revisar el código: permisos, uso de red, `exec`, rastreadores.
3. Sacar del repo los `.jar` y `.apk` incluidos y compilarlos desde su fuente. Por ejemplo:
   - `arity` para la Calculadora;
   - `support-v4` para Superuser, desde AOSP;
   - dos APK de prueba que había en el repo de Lightning.
4. Compilar con `build.py`, instalar y probar en el teléfono.
5. Publicar una rama `xt550-libre` y un release con el APK y `SHA256SUMS.txt`.
6. Bajar el release sin sesión de GitHub y comparar tres hashes: el bajado, el compilado y el instalado (`pm path` + `adb pull`).

## 8. Apps de AOSP recompiladas

- Reloj, Galería y Calculadora son las de Android 2.3.6 (`android-2.3.6_r1`).
  - Como apps de sistema usan APIs ocultas y permisos de sistema. Las adaptamos para compilar con el SDK público.
  - Les pusimos paquete propio (`org.librereloj`, `org.libregaleria`, `org.librecalculadora`) para que convivan con el sistema.
- **Reloj**: hubo que empaquetar la fuente `Clockopia.ttf`; sin ella se cierra.
- **Galería**: responde a `com.cooliris.media.action.REVIEW`, que usa la Cámara de Motorola para mostrar la última foto.
- **ADW y Solitario**: se compilaron con el mismo paquete que tenían, y sus datos se pasaron a la versión nueva.
  - Ojo: al restaurar datos con `tar`, la carpeta de la app queda a nombre de root. Android lo detecta (`/mismatched_uid` en `packages.xml`). Hay que devolverle el dueño y reinstalar el mismo APK con `pm install -r`.
- **Solitario**: forzaba la pantalla horizontal en Android viejo. Ahora se juega en vertical con cartas que ocupan el ancho.

## 9. Root libre

- `su` 3.2 y Superuser 3.3 de ChainsDD, compilados:
  - `su`, estático con el NDK, instalado en `/system/bin/su` con permisos 6755;
  - Superuser, como app normal.
- Cambios al `su`:
  - lee el formato de permisos de Superuser 3.3;
  - llama a `am` sin shell;
  - para root y para la conexión USB, no avisa a Superuser en cada comando.
- Después se borraron el gestor chino (estaba en `/system/app` **y** en `/data/app`), su tienda y las copias ocultas `.suv`.
- Quedaron con setuid solo `run-as`, `ping`, `netcfg` y `fusermount` (de fábrica) más nuestro `su`.

## 10. Navegador con HTTPS moderno

El navegador de Android 2.3 usa OpenSSL 1.0.0a: hasta TLS 1.0, que casi ningún sitio acepta hoy. Ni Wikipedia ni DuckDuckGo abrían.

- **Base**: Lightning Browser 3.0.5, una versión vieja que todavía funciona en 2.3. Le agregamos descargas propias y lo pasamos al español.
- **Cómo usa nuestro TLS**: el WebView de 2.3 hace HTTPS con `android.net.http.HttpsConnection`, que tiene un campo estático `mSslSocketFactory`. Por reflexión, el Navegador pone ahí su propia fábrica de sockets.
- **La capa TLS** es **mbedTLS 3.6.7** en C, compilada con el NDK r10e (sin `ndk-build`: un `build_native.py` llama a gcc directo). Ocupa 464 KB.
  - Usa TLS 1.2/1.3, verifica la cadena y el nombre del sitio, y trae las 110 raíces de Mozilla.
  - Reanuda sesiones para que la segunda conexión sea rápida.
- **Certificados**: el WebView igual dice "certificado no confiable", porque compara contra las raíces viejas del sistema. El Navegador acepta ese aviso **solo** si mbedTLS acaba de verificar ese mismo certificado. Cualquier otro error se le pregunta al usuario. De paso arreglamos un error del original, que aceptaba algunos errores sin avisar.
- **Problemas resueltos**:
  - `/dev/random` en el kernel 2.6.38 tardaba hasta 235 s en dar 64 bytes: se usa `/dev/urandom`, igual que el resto de Android;
  - con TLS 1.3, después de un `NewSessionTicket`, mbedTLS dice "esperando datos" aunque la respuesta ya está en el buffer: hay que seguir leyendo;
  - conexiones sin timeout: ahora 30 s.
- **Pruebas en badssl.com**: los certificados vencidos, de otro sitio o de una raíz desconocida se rechazan.
- **Fecha**: si la fecha del teléfono es anterior al día de compilación, avisa "La fecha del teléfono está mal".

## 11. BusyBox

El `busybox` que dejó Romaster era un binario de origen desconocido. Lo compilamos desde git.busybox.net (1.38.0) **en Windows, sin make**:
- Kconfiglib en Python para la configuración;
- los generadores de BusyBox portados a Python;
- gcc del NDK.

Quedó estático, de 304 KB, con 67 comandos. Solo se usa por USB para mantenimiento.

## 12. Ajustes

Ver [ajustes.md](ajustes.md):
- batería;
- vibración;
- zona horaria;
- datos móviles.

## 13. Hora por Internet

Android 2.3 pone la hora automática solo con la red del celular (NITZ). Sin chip, nunca se corrige: estaba 18 s adelantado. Si se queda sin batería, puede volver a 2012, y entonces ningún sitio HTTPS abre.

**Hora por Internet** es una app propia que:
- pide la hora a `pool.ntp.org`, `time.cloudflare.com` y `time.google.com` (SNTP) cuando hay conexión, como mucho cada 12 h;
- si la diferencia es de 1 s o más, ejecuta `date -s` como root.

El `date` del sistema pasa por `/dev/alarm`, así que también fija el reloj de hardware. Superuser recuerda el permiso; se le apagó la notificación.

## 14. Porcentaje en el ícono de batería

`framework-res.apk` traía 21 dibujos de batería, uno cada 5 %, y tres "recetas" (*level-lists*):
- normal;
- cargando;
- cargando por USB.

Cambiamos:
- 10 de esos dibujos por los dígitos 0–9;
- las 3 recetas por 101 niveles: cuerpo de la batería (o la animación de carga) con los dígitos encima.

Las recetas se compilaron con `aapt` contra el propio `framework-res.apk`. Probamos los 303 íconos con el código de dibujo del teléfono antes de instalar.

**Por qué el teléfono acepta el archivo**: en Android 2.x, para apps del sistema, `PackageParser` solo verifica la firma de `AndroidManifest.xml`. Ese archivo, la firma y `resources.arsc` quedaron idénticos.

La instalación se hace copiando a `.new` y renombrando (nunca sobrescribiendo: todos los procesos tienen el archivo abierto), y después se reinicia. Con esto se borró BatteryBot.

Herramientas y detalle: [xt550-battery-percent](https://github.com/facundosterzerforino/xt550-battery-percent).

## 15. Últimas piezas cerradas

- **Teclado Libre es2.** El motor del diccionario (`native/` de AOSP 2.3.6, sin cambios) se compila con el NDK r10e y va dentro del APK como `lib/armeabi-v7a/libjni_latinime.so` (13 KB). Android carga primero la copia de la app. Lo verificamos de dos formas:
  - en `/proc/<pid>/maps` aparece la librería de la app;
  - escribiendo `cancion` → `canción`.

  Después se borró la copia de Motorola en `/system/lib`.
- **PrivInit** (Qualcomm, cerrado): solo ejecutaba `setprop` al encender y quedaba en memoria. Leyendo `framework.odex` vimos qué hace Android si esos valores faltan: usa los suyos (`net.http.threads` 4, caché de webkit 8 MB, `idle_cache` 8). Se borró.
- **CellonFastDormancy** (cerrado): solo actúa con datos 3G, que están apagados. Se borró.

Se hizo con [`tools/borrar_app_sistema.py`](../tools/borrar_app_sistema.py): 35 → 33 paquetes. Después de reiniciar, root, teclado, Navegador y las 12 apps principales siguieron funcionando.
