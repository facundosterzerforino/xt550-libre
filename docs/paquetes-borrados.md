# Paquetes borrados

Lista completa de lo que se sacó del teléfono, por etapa.
- **Ruta original**: dónde estaba el archivo.
- **SHA256 original**: la huella del archivo de fábrica (del respaldo previo al root). Antes de borrar cada archivo se verificó que coincidiera con la copia en la PC.
- Las que dicen *instalada por nosotros* o *la instaló la herramienta de root* no venían de fábrica.

En total: 87 paquetes de fábrica + 6 instalados después y borrados. Quedan 35 (ver [paquetes-finales.md](paquetes-finales.md)).

## 1. Apps viejas que ya no funcionan

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.facebook.katana` | Facebook 1.8 (ya no conecta) | `/flex/app/FBAndroid-1.8.3-preload.apk` | `d3c0caaa244c45473e6af5f326a9f92270eba54e249a5de23c7b952feaf77e38` |
| `com.twitter.android` | Twitter 3.1 (ya no conecta) | `/flex/app/Twitter-3.1.1-release.apk` | `1fab9a66a1045ec5dbdeaf019c4cb4b18847e046390d5fed9cf7690bd32bc556` |
| `com.google.android.apps.blogger` | Blogger | `/flex/app/blogger.apk` | `d0605a53ff517072d81ec8d86757881079bd700c28b79ce960048bd61e618988` |
| `com.google.android.apps.plus` | Google+ (servicio cerrado) | `/flex/app/PlusOne.apk` | `b7450e00aa0fe9671314025248b706f87150a418e86767d642b31ef5052a3f16` |
| `com.google.android.talk` | Google Talk (servicio cerrado) | `/flex/app/Talk.apk` | `7016f25330100766d48af28ece336d2a8581aa2a7f9ec7c02f3df904b51c723d` |
| `com.google.android.street` | Street View | `/flex/app/Street.apk` | `c1b1463b24f7d1bce782bb50eb7cbfa0863c5568e9fb56c7bf2e66b673e45cf0` |
| `com.google.android.youtube` | YouTube viejo (ya no reproduce) | `/flex/app/YouTube.apk` | `f7102875a932bab773f9bfe0069723ed2d33923ddf9b983f75de38958949a8ce` |
| `com.mgyapp.android` | Tienda de apps china que instaló la herramienta de root | *la instaló la herramienta de root* | |

## 2. Lanzador 3D, clima, correo y Motorola

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.motorola.mmsp.threed.motohome` | Lanzador 3D de Motorola (pesado); reemplazado por ADW | `/flex/app/MotoHome3D_argonspin_mdpi.apk` | `583715b6dad24125e4add54beebfe0070a70d918f685f8fc96ca811f8dbf1654` |
| `com.android.email` | Correo | `/system/app/Email.apk` | `3d85f81f134c7b3454cc0b3c56077e61aa9392b9d4bdb3fa04ac5944b6f723ef` |
| `com.google.android.gm` | Gmail | `/flex/app/Gmail.apk` | `88e08e31aa3fc9a8bb13ad566e70846ad0198372ae697935c4d160a9e34dc7ff` |
| `com.android.arcsoft.ArcSoftDMS` | DLNA: compartir fotos/música con TV por Wi-Fi | `/flex/app/MediaSerGlobal.apk` | `35016a35bb43ad62970375c21a94864983fe5a9c5af3907b7eb29a27fcbb38d2` |
| `com.arcsoft.mediasee` | Visor DLNA | `/flex/app/MediaSeeGlobal.apk` | `ea063eb9a3539e482b94851fde207abb0569a4b0c6859dea535e64deae23fbf8` |
| `com.google.android.apps.genie.geniewidget` | Widget Noticias y tiempo | `/flex/app/GenieWidget.apk` | `993bc8af4e03ac901fc1ada844c6220f6e44f73322590a6b75eb5fa86d3f5496` |
| `com.google.android.voicesearch` | Búsqueda por voz | `/flex/app/VoiceSearch.apk` | `7542b2e2ed28120d4a87f9ddf8e47edd2ac71f69ec0f518291ba51f0cc942c7f` |
| `com.nuance.android.vsuite.vsuiteapp` | Comandos de voz Nuance | `/flex/app/VSuiteApp.apk` | `795075b6a75d6de78ca4eef7826814a40f47e02b1747cc4a94a6de819d7f597b` |
| `com.motorola.container.movistargeneric` | Contenido de Movistar | `/flex/app/MotorolaContainerMovistarGeneric_1.1.21.apk` | `c7a1809e1871da36fff4c2ed84084e3bcd9e77af0189d99eac00c063a893f96d` |
| `com.motorola.mmsp.accuweather.app` | Clima AccuWeather | `/flex/app/MotoAccuWeather2_App_argonspin_mdpi.apk` | `5ebc760c76060e14206c36ab7b90ff7ba8ddb7796a865813c15079fba4c1d9cd` |
| `com.motorola.mmsp.accuweather.service` | Servicio de clima AccuWeather | `/flex/app/MotoAccuWeather2_Service.apk` | `0d31df13c612f52eeb5a6872bb4f6050bcc9555ca238dc8f3d74faba606b1ffd` |
| `com.motorola.mmsp.locationwidget.small` | Widget de ubicación | `/flex/app/MotoLocationWidget_Simplified_small_argonspin_mdpi.apk` | `59e7255fe69267e6d150a7681bc3796fcce151d3baa861198bd6878510d641ab` |
| `com.motorola.mmsp.weatheranimationres` | Animaciones del clima | `/flex/app/MotoWeatherPictureRes_argonspin_mdpi.apk` | `8f92a8ced10c2c78bcfdf2a1c97c14748bc1265a82ebfc37881c363a7a91bd55` |
| `com.motorola.mmsp.weatherlivewallpaper` | Fondo animado del clima | `/flex/app/MotoWeatherLiveWallpaper_argonspin_mdpi.apk` | `b367e2b74dfe7ccbcd940a4d85d4d56650a8782b9dd0139e4867f50c601df60c` |

## 3. Google y Play

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.android.vending` | Play Store / Market | `/flex/app/Phonesky.apk` | `7da9ec5f140868573047f0a269e2635b586106e9ad3cab16b940e43cc183b7e3` |
| `com.android.vending.updater` | Actualizador del Market | `/flex/app/MarketUpdater.apk` | `04a512b1d38b24bc62ff21301fa16e282a2ef0302fd659569e37f713f74ebcfd` |
| `com.google.android.gsf` | Servicios de Google | `/system/app/GoogleServicesFramework.apk` | `f18e42ebd4f2c69972342437b1f13fafbe785a0f3894b7e17bb975c7263be3f3` |
| `com.google.android.location` | Ubicación por red de Google | `/flex/app/NetworkLocation.apk` | `1f657d4eb0d04013cfe7b60817a000a3e9b86a57e762673819fc62066e996ff5` |
| `com.google.android.apps.maps` | Google Maps | `/flex/app/Maps.apk` | `18c85988b761217866319e3fe29370f1889ea228155e7674e619cd725703f2d0` |
| `com.google.android.apps.uploader` | Subida de fotos a Picasa | `/flex/app/MediaUploader.apk` | `3f6b5e57f1feff8e3e15e4cc410eab6e5918007be3425b541a15d80b654d8552` |
| `com.google.android.feedback` | Reportes a Google | `/flex/app/GoogleFeedback.apk` | `70a5b8245d739daf8604b307083b4f8ba92c34fe2a15420bce2facfe61a383a3` |
| `com.google.android.googlequicksearchbox` | Búsqueda de Google | `/flex/app/GoogleQuickSearchBox.apk` | `1fdb02944a69eecf50847eb478b0170da81c08a7e30638f8ec9dc01b9a043603` |
| `com.google.android.latinimetutorial` | Tutorial del teclado | `/flex/app/LatinImeTutorial.apk` | `05d691848220f2d64e13c2a495292c233900371f9fd8e963d9340673b032b2be` |
| `com.google.android.partnersetup` | Configuración de socios de Google | `/flex/app/GooglePartnerSetup.apk` | `1bb059373cc8e96d1bd8cae777aa14d4420368ae9ee0a91ddb50f06297d9c5c5` |
| `com.google.android.syncadapters.calendar` | Sincronización de calendario con Google | `/flex/app/GoogleCalendarSyncAdapter.apk` | `3a1f05a695af3ef40dd2311609f30a340fadd2710500f59344f2f2c696dc4552` |
| `com.google.android.syncadapters.contacts` | Sincronización de contactos con Google | `/flex/app/GoogleContactsSyncAdapter.apk` | `e775c2362d0cbf1665119cf9f987fc5f15ea829bddec136ca04e501492cd20ad` |
| `com.android.setupwizard` | Asistente de primera configuración | `/system/app/SetupWizard.apk` | `3691be8976cadeccef4d5ecbcc5583cabf67091ca5a4dc8eb20b96a0e6385078` |
| `com.tunewiki.smp.moto` | TuneWiki (letras de canciones online) | `/flex/app/SMPM_3_3_4_367_Signed_2012-06-25_09-09-57.apk` | `da1ff1037d9b71b057e02fee7e5286ba3d7b2d6f35c24f55fafe0dc2682082ef` |

## 4. Música de Motorola

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.motorola.mmsp.musicdashboard` | Panel de música de Motorola; reemplazado por Música Simple | `/flex/app/MusicDashboardGlobal_argonspin_mdpi.apk` | `0618a19ff8ddce7ca677b1a9cf53de4a79a38c2aeb939c802cb9dffede4cee94` |
| `com.android.music` | Música de Motorola; reemplazada por Música Simple | `/flex/app/MusicGlobal_argonspin_mdpi.apk` | `428a7b9406cfa74ca845689e79fc769c399c6c4b98f6f4d6571b6cc266b663de` |
| `com.motorola.mmsp.musicnowglobal` | Widget "Música ahora" (recomendaciones online) | `/flex/app/MusicNowGlobal_SMP_argonspin_mdpi.apk` | `cb23c6c12e146b45b61e08dc4aa312e1e6d45a5a92dfca597c4e2098d8383a7f` |
| `com.cellon` | Números de servicio (SDN) | `/flex/app/Sdn.apk` | `784dc85518915ef3e7412da7b2f9d7b1ccd7585e870b2dac262038a1cb971550` |
| `org.kreed.vanilla` | Vanilla Music (la instalamos para probar) | *instalada por nosotros* | |
| `com.martinmimigames.littlemusicplayer` | Little Music Player (lo instalamos para probar) | *instalada por nosotros* | |

## 5. Servicios de Motorola y extras

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.motorola.blur.service.blur` | Servicios de Motorola (cuentas Motoblur) | `/system/app/blur-services.apk` | `ac739f9a91eb96ec1ca4285edfe005515f76bad384d0fd3cf93dbbd3cc83e03c` |
| `com.motorola.blur.updater` | Actualizador de Motoblur | `/system/app/BlurUpdater.apk` | `0f79b48cc1d0d765366c309362aaabd639292b8398b1435278f7637fb6ead4a1` |
| `com.motorola.Upgrader` | Actualizador del sistema | `/system/app/Upgrader.apk` | `f1133a225f881659fa84def0f6d19a78ec92ffd6084942623e29bb7678aeef4f` |
| `com.motorola.botasettings` | Ajustes de actualización por aire | `/system/app/BotaSettings.apk` | `db3a4000af248678279070ab74fb3b9a88ce4b1b740e431ef5a3ce58e52b67d0` |
| `com.cellon.oma` | Gestión remota del operador (vDM) | `/system/app/vdmc.apk` | `81e102b833e238b1f97dc05df5313ca1b5b5b2e0ddc27e66159cd7fea82408ed` |
| `com.cellon.register` | Registro del teléfono | `/system/app/RegistrationMoto.apk` | `10843623ead924f736e6b1e512308e545910df06ea6bdefcbc136a8be713290f` |
| `com.qualcomm.wiper` | Ubicación por Wi-Fi de Qualcomm | `/system/app/Wiper.apk` | `e1ba5a7e877e3e36adaa431a50d33b1df941a9080ceee61c38d8e1e2ece04257` |
| `com.cellon.mat` | Herramienta de fábrica | `/system/app/mat.apk` | `582b4a59fb544453e9ed3083859ff3710b3448973cdd392ed74fe3985f0d2c64` |
| `com.cellon.mat.version` | Versión de la herramienta de fábrica | `/system/app/internalVersion.apk` | `4196891468e0866b1d8bf47076b0a14f9956af0db0d1554ecaff2a004a340b1c` |
| `com.android.protips` | Widget de consejos | `/system/app/Protips.apk` | `a316f1213c9f137d7dbda4d80416cf4909132914f7635dac1486ad540053d2fa` |
| `com.android.wallpaper` | Fondos animados | `/system/app/LiveWallpapers.apk` | `5a50d232f21b94ea5c68ac5eba4e2a94395bee0706aaa3fa750c0f3079d18c80` |
| `com.android.wallpaper.livepicker` | Selector de fondos animados | `/system/app/LiveWallpapersPicker.apk` | `8452c96246e9f83c18bf77569c725a507f261501ec693264bfea1152a7848e9f` |
| `com.motorola.widgetapp.worldclock` | Widget de reloj mundial | `/flex/app/WorldClock.apk` | `b53dcbd0816b169ebb5eca009aebb6a8c2e82aeee8a61e7144ff159c3751fcaa` |
| `com.motorola.togglewidgets` | Widgets de encendido/apagado | `/flex/app/ToggleWidgetsGlobal_argonspin_mdpi.apk` | `c725e815401029c56d9eaf73034281dd480dfaddc3fad4a07812598098e898c8` |
| `com.monotype.android.font.bauhaus` | Fuente Bauhaus | `/flex/app/Bauhaus.apk` | `677f87f1f513a9c0087366e572bb1156eceffd78884d6c619e57638430cd90a0` |
| `com.motorola.mmsp.activitygraph` | Red social de Motorola | `/flex/app/ActivityGraph_argonspin_mdpi.apk` | `d423df628338fa373e11f47fe9c76853d4192a7e3ed60454b014e952844e1e28` |
| `com.motorola.mmsp.socialGraphCallService` | Red social de Motorola (llamadas) | `/flex/app/SocialGraphCallService.apk` | `0841299e7dc73c44303492c3a88bcacbcbe15f0fcdc532cfcd0f0f2c9b4177e2` |
| `com.motorola.mmsp.socialGraphService` | Red social de Motorola (servicio) | `/flex/app/SocialGraphService.apk` | `bfd6f201119a2aa7a4a379a213f98bcab528246a7ecd2fa9d7cfde23788fd3b1` |
| `com.motorola.mmsp.socialGraphWidget` | Red social de Motorola (widget) | `/flex/app/SocialGraphWidget_argonspin_mdpi.apk` | `327ea78f6054026f5613811709cc7384108e8246473518dc585de33c8263f991` |
| `com.motorola.settings.tos` | Términos de servicio | `/system/app/LegalReader.apk` | `8dffc929a314bb09a2a672c00b9fe4561bd99526ab897cc569daa26d5a424702` |
| `com.motorola.setup.tos` | Términos de servicio (configuración) | `/system/app/SetupLite.apk` | `4e6695b7f60e27f3dbc3662f1e34144008e04f38b119eb363323af66f52feacf` |
| `com.android.server.vpn` | VPN | `/system/app/VpnServices.apk` | `8efe8034aef86922d185e5fac36ec9c472852d59fb31ace926da7976a290df58` |
| `com.android.certinstaller` | Instalar certificados desde la tarjeta | `/system/app/CertInstaller.apk` | `7aef1afb6020808708d873e461e5ab7515277078cf242147d101355aa92c6d9a` |

## 6. Teclados y archivos

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.swype.android.inputmethod` | Teclado Swype; reemplazado por Teclado Libre | `/flex/app/Swype.apk` | `74ddd7b5de737196e65bd22b62b7bdb60f886ba588fd699ad7f376ce58ba1a0e` |
| `com.motorola.FileManager` | Administrador de archivos de Motorola | `/flex/app/FileManager.apk` | `161b473ab21860cd036957d4e5b36d9274507a85c8681b8f889be1bf07498cc5` |
| `org.openintents.filemanager` | OI File Manager (lo instalamos para probar) | *instalada por nosotros* | |
| `com.android.inputmethod.latin` | Teclado de Android sin diccionario; reemplazado por Teclado Libre | `/system/app/LatinIME.apk` | `b50bfaae4d041c8e6dfb9aa7859ea7f95f7f5bd4e60831e9a199195441f24e8c` |

## 7. Voz, brújula y extras de Cellon

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `android.tts` | Texto a voz | `/system/app/TtsService.apk` | `ee1985224de69054634a6bb7e954e0bb3db1e4bbd128d89528c2a01e611883fc` |
| `com.svox.pico` | Voz Pico | `/system/app/PicoTts.apk` | `ed8ffefaf0de4a79ac22ef1b7bfe431781843441d79102ff208621e502a8933e` |
| `com.cellon.compass` | Brújula | `/system/app/Compasses.apk` | `46081948374d00d24c3bd9b4843f6ffb1cf00613fb2448f0b35962e60773b6b5` |
| `com.cellon.qfuse` | Código secreto de fábrica | `/system/app/Qfuse.apk` | `0a0818dd50570c7fc4563c7cf7c844bb0002882037d08ce71497176a9a1390e3` |
| `com.cellon.quicksms` | Respuestas rápidas al rechazar llamada | `/system/app/QuickSms.apk` | `d7271a240c3ddf9c2a8deb6f8d886205b81f7336c7a1286447b07f71cb1ddfaf` |
| `com.cellon.startupnotice` | Aviso al encender | `/system/app/StartupNotice.apk` | `c61aaa86f7447d12fda90b21592f9dc09922389e2a654f398866555994e2b8ae` |

## 8. Apps reemplazadas o sin uso

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.android.browser` | Navegador viejo (sin HTTPS moderno); reemplazado por Navegador | `/system/app/Browser.apk` | `ec12f2a4825d596e64638b9556159dc914d9a310638bf86bf75a9e041927f87b` |
| `com.android.calculator2` | Calculadora; reemplazada por la recompilada | `/system/app/Calculator.apk` | `674910d201797a2a6fc06a58a28246cf77ca928e7446b2b9250a08d168409726` |
| `com.android.calendar` | Calendario | `/system/app/Calendar.apk` | `982dce10229964cecf5df00cfe16a001000063c1fd68eac6af49e0a22fb6877e` |
| `com.android.providers.downloads.ui` | Lista de descargas (se ve dentro del Navegador) | `/system/app/DownloadProviderUi.apk` | `b8d7a9733663d7bec2bae17bce8f50c106a587c7b37dd8a7e5bf17ffe58d6822` |
| `com.android.soundrecorder` | Grabadora | `/system/app/SoundRecorder.apk` | `dddf326618c3a9070de6f9774ae2eb4ddb4b72fd89d7dbeaf4dfc2133926646c` |
| `com.broadcom.bt.app.fm` | Radio FM | `/system/app/FmRadio.apk` | `51b2838380f4d5c33381a5c78376758d32000802147949202ad0d624f558a93f` |
| `com.broadcom.app` | Servicio de la radio FM | `/system/app/FmRadioListener.apk` | `aba2adfae0f003d9e3e07ab190629a7d5a881a8cb508aefccd598d9aaf8cdfc0` |
| `com.motorola.batterymanager` | Administrador de batería de Motorola | `/flex/app/EnhancedBatteryManager_noApp_mdpi.apk` | `f1ffeec5296240fb58807b3d1268c4069c86a66f1b94c9b5384d7ac0180be5d6` |
| `com.motorola.sdcardbackuprestore` | Copia de seguridad a la tarjeta | `/flex/app/PimBackup.apk` | `5df548a1e4ae33f6736ccdcb67661e6e4824a015bb456e975cad818b93772659` |

## 9. Gestor de root chino

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.mgyun.shua.su` | ROOT大师 (MGYun): gestor de root con push de Tencent; reemplazado por su + Superuser libres | *la instaló la herramienta de root* | |

## 10. Reloj, galería, DRM y tareas

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.android.deskclock` | Reloj de Motorola; reemplazado por Reloj recompilado | `/system/app/DeskClock.apk` | `84aec6fc9e509ada51d9445e4bb83438f611824cbc376606a48c9b89054a925d` |
| `com.cooliris.media` | Galería 3D; reemplazada por Galería recompilada | `/system/app/Gallery3D.apk` | `28d56d40c5674e49696c035aa56c421cf5cb00654a6842e7b50a168ae9b4fbe7` |
| `com.discretix.drm.api` | App de DRM Discretix (las librerías DRM del sistema se conservan) | `/system/app/DxDrmApplication.apk` | `cf6306ae21d069dad8052e895dd48bb50d2ceeb46911bbffcbbea342572dea5e` |
| `com.android.dxdrmplugin` | Plugin DRM del navegador | `/system/app/DxDrmPlugin.apk` | `891be3e686bbe373f9b1d0d2afe3d5f34f05dec4058ce1106d19bf689459e306` |
| `com.motorola.mmsp.taskmanager` | Administrador de tareas | `/flex/app/TaskManager_mdpi.apk` | `016af565da3d28c9451f4bd56fbd6a2611e54deb019744801f8675309086150f` |

## 11. Últimos

| Paquete | Qué era | Ruta original | SHA256 original |
|---|---|---|---|
| `com.cellon.factorydatareset` | Pantalla de reset de fábrica de Cellon (Ajustes tiene la suya) | `/system/app/FactroyDataReset.apk` | `8c69d27847f9b50dbd81af11a820d58657c5b8bc6ee24a51dfa29ebb6b34aaf9` |
| `com.cellon.ringmodeprofile` | Modo de timbre / perfiles de sonido | `/system/app/RingModeProfile.apk` | `248e8557ac1d30e2d6f2c995ef26baa6369f427b742fed373fd83323ca062c06` |
| `com.darshancomputing.BatteryIndicator` | BatteryBot; reemplazado por el % en el ícono del sistema | *instalada por nosotros* | |

## Otros archivos

- `/system/tts/nuance/` (17 archivos de voz, 5,5 MB): restos de los comandos de voz Nuance.
- `/system/lib/plugins/com.android.dxdrmplugin/libcom.android.dxdrmplugin.so`: plugin DRM del navegador viejo.
- `/system/bin/.suv`, `/system/usr/.suv` y `/data/local/tmp/.romaster_script`: copias ocultas de `su` que dejó la herramienta de root.
- 35 archivos huérfanos de `/data/dalvik-cache` y 39 carpetas de `/data/data` de paquetes ya borrados.
- Se **conservaron** a propósito `libjni_latinime.so` (la usa Teclado Libre), `libDxDrm*.so` y `DxDrmServerIpc` (los usan MediaPlayer, MediaScanner, webkit y MMS de Motorola), y `DownloadProvider`/`CalendarProvider` (proveedores de datos).
