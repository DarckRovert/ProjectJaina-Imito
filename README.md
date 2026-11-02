![ProjectJaina-Imito Banner](assets/project-jaina-imito-banner.jpg)

# ProjectJaina-Imito

**Tu Azeroth. Tu personaje. Ahora en tu móvil o tableta Android junto a jugadores de PC.**

**ProjectJaina-Imito** es el cliente oficial y soberano de **World of Warcraft 3.3.5a** para dispositivos móviles Android (ARM64, Android 12+), concebido para integrarse a la perfección con el clúster y los reinos de **JainaCore**:
* **Reino 1 — JainaCore** (Era Vanilla Cap 60 / Host Darck Perú)
* **Reino 3 — WanitosGYM** (Era WotLK ICC Cap 80 / Host Fran España)
* **Túnel Remoto Global Playit** (Conexión mundial en 1 clic sin lag ni apertura de puertos)

---

## ⚡ Características Principales

* 📱 **Experiencia de PC en Móvil:** Juega con tu mismo personaje, tu misma hermandad y en los mismos reinos que tus compañeros en ordenador.
* 🎮 **Soporte Dual de Controles:**
  * **Touch UI:** Interfaz táctil ergonómica con joystick virtual y botones de acceso rápido.
  * **ConsolePortLK:** Soporte nativo para mandos Bluetooth/USB (Xbox, PlayStation DualSense, Razer Kishi, GameSir, AYN Odin 2).
* 🔋 **Modo ECO (40 FPS Cap):** Optimización inteligente para sesiones largas de juego que reduce el calentamiento y duplica la vida útil de la batería.
* 🚀 **Pila de Emulación de Alto Rendimiento:**
  * Motor de traducción binaria **Box64 v0.4.5** con Dynarec optimizado.
  * Capa de compatibilidad **Wine 10.10** con parches dedicados de estabilidad de buffers.
  * Drivers gráficos **Mesa Turnip 26.1.0** (Snapdragon Adreno) y **Vortek 2.1 / VirGL** (MediaTek Mali / Dimensity).
* 🛡️ **Empaquetado y Seguridad L9:** Binario alineado a 4 bytes (`zipalign`) y firmado con certificado criptográfico oficial bajo el esquema **Android Signature Scheme v3**.

---

## 📥 Descarga Oficial y Verificación

| Archivo | Versión | Tamaño | Suma de Verificación SHA-256 |
| :--- | :---: | :---: | :--- |
| **`ProjectJaina-Imito-v1.0.apk`** | **v1.0** | **430.76 MB** | `A3BC068BC2FDBAB8AEDBC198E01AB4F55D83414A27CEE03EE8618FF59C875F00` |

> Los instaladores se encuentran publicados en el directorio local:
> 👉 [`releases/ProjectJaina-Imito-v1.0.apk`](releases/ProjectJaina-Imito-v1.0.apk)

---

## 🚀 Inicio Rápido (3 Pasos)

1. **Instala la APK:**  
   Instala `ProjectJaina-Imito-v1.0.apk` en tu dispositivo y concede el permiso **"Acceso a todos los archivos"** en los ajustes de Android.
2. **Copia los archivos del juego:**  
   Copia la carpeta de tu cliente WoW de PC (`Data/`, `Interface/`, `Wow.exe`) a la ruta:
   ```text
   Almacenamiento interno / WoW-Imito / Client /
   ```
3. **Elige tu reino y juega:**  
   Abre la aplicación, ve a **Settings > Set realm** e ingresa la dirección de juego:
   * **Conexión Global (Cero VPN):** `ambulance-ergonomic.tun.ply.gg`
   * **WiFi en Casa (Misma red):** `192.168.1.80`
   * **Reino 3 WanitosGYM (España):** `100.98.162.75:8087`
   Pulsa **PLAY** ¡y bienvenido a Azeroth!

---

## 📚 Documentación Técnica Detallada

* 📖 [**Guía de Instalación Paso a Paso**](docs/GUIA_INSTALACION_ANDROID.md) — Requisitos, transferencia por USB-C y primeros pasos.
* 🎮 [**Configuración de Mandos y Controles**](docs/CONFIGURACION_MANDOS.md) — Asistente de calibración de mandos Xbox/PS5/Odin 2 y modo táctil.
* ⚙️ [**Arquitectura Técnica del Runtime**](docs/ARQUITECTURA_TECNICA.md) — Detalle de emulación ARM64, drivers Turnip/Vortek y resiliencia de sockets.
* ⚖️ [**Modelo de Gobernanza**](GOVERNANCE.md) — Normas de desarrollo, licencias y preservación arquitectónica.

---

## ⚖️ Licencia y Créditos

* **Licencia:** Distribuido bajo la licencia [GNU Lesser General Public License v2.1](LICENSE) (LGPL-2.1), respetando los términos de Winlator y WoW-Imito.
* **Proyecto Upstream:** Basado en la tecnología de emulación desarrollada por **Mr Anonymz** ([WoW-Imito](https://github.com/MrAnonymz/WoW-Imito)).
* **Ecosistema JainaCore:** Arte oficial de Lady Jaina Proudmoore y perfiles de conexión mantenidos por el equipo de ingeniería de **Project Jaina**.
