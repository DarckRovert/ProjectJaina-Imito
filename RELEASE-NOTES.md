# Notas de la Versión — ProjectJaina-Imito v1.0 (Oficial)

## 🌟 Resumen de la Versión 1.0 (2026-11-02)

**ProjectJaina-Imito v1.0** es el lanzamiento oficial del cliente World of Warcraft 3.3.5a para dispositivos Android (ARM64, Android 12+) adaptado soberanamente para la comunidad y jugadores de **Project Jaina / JainaCore**.

Permite disfrutar de una experiencia de juego de PC completa directamente en smartphones, tabletas y consolas portátiles (AYN Odin 2, Retroid Pocket 4 Pro, Razer Edge), con soporte total para juego cruzado (cross-play) con los usuarios de ordenador en nuestros dos reinos:
- **Reino 1 — JainaCore** (Vanilla Cap 60 / Host Darck Perú)
- **Reino 3 — WanitosGYM** (WotLK ICC Cap 80 / Host Fran España)

---

## 🚀 Novedades y Características Principales

### 1. Pila de Emulación y Rendimiento ARM64
- **Traductor Binario Box64 v0.4.5:** Compilación Dinámica (Dynarec) optimizada con bloques grandes de ejecución (`BIGBLOCK=2`), aceleración de operaciones de retorno (`CALLRET=1`) y operaciones de punto flotante de alta velocidad (`FASTNAN=1`).
- **Capa Win32 Wine 10.10 con Parches de Estabilidad:**
  - Parche `wined3d-null-buffer-map.patch`: Erradica excepciones de puntero nulo al volcar buffers de vértices en zonas concurridas (Dalaran, Orgrimmar, ventormenta).
  - Parche `wined3d-shader-alpha-test.patch`: Corrige mezclas de canal alfa en auras mágicas y partículas.
- **Drivers Gráficos Oficiales:**
  - **Mesa Turnip 26.1.0:** Driver Vulkan nativo para Qualcomm Adreno (Snapdragon 870, 888, 8 Gen 1/2/3).
  - **Vortek 2.1 / VirGL 23.1.9:** Drivers para GPUs Mali (MediaTek Dimensity) y PowerVR.
- **Modo ECO (40 FPS Cap):** Limitador de fotogramas de alta eficiencia que reduce la carga térmica hasta un 35% y duplica la autonomía de la batería en sesiones largas.

### 2. Identidad Visual y Branding JainaCore
- **Icono Adaptativo Android 12-15:** Nuevo icono oficial de 1254 × 1254 px derivado del escudo soberano de Lady Jaina con zona segura contra recortes circulares y squircles.
- **Fondos de Pantalla Móviles:**
  - `wallpaper-1`: Escudo oficial de Lady Jaina Proudmoore.
  - `wallpaper-2`: Ilustración de Theramore Living Lore.
  - `wallpaper-3`: Emblema Escarcha de Icecrown Citadel para WanitosGYM Cap 80.
- **Textos y Diálogos:** Localización al español neutro en avisos de carga y créditos.

### 3. Conectividad Multi-Reino Simplificada
- Incorporación de perfiles listos para usar en `client_patches/`:
  - `ambulance-ergonomic.tun.ply.gg` (Túnel Anycast global Playit sin necesidad de abrir puertos).
  - `192.168.1.80` (WiFi local de alta velocidad).
  - `100.81.210.121` y `26.140.157.205` (VPNs P2P para Reino 1 Perú).
  - `100.98.162.75:8087` y `26.202.12.241:8087` (VPNs P2P para Reino 3 España).

### 4. Soporte Ergonómico para Mandos y Pantalla Táctil
- **Touch UI:** Mapeo táctil en pantalla con joysticks virtuales, pellizco de cámara (pinch-to-zoom) y accesos directos.
- **ConsolePortLK:** Soporte nativo para mandos Xbox, PlayStation DualSense, Razer Kishi y GameSir con asistente de calibración en primer arranque.
- **Titan Panel Móvil:** Barra superior con porcentaje de batería real del dispositivo Android y telemetría de latencia en milisegundos.

---

## 🛡️ Seguridad y Verificación del Paquete

- **Firma Digital:** Certificado oficial con Android Signature Scheme v3 (`apksigner`).
- **Alineación de Memoria:** 4-byte boundary validado (`zipalign -p -f 4`).
- **Suma de Verificación SHA-256:**
  ```text
  A3BC068BC2FDBAB8AEDBC198E01AB4F55D83414A27CEE03EE8618FF59C875F00  ProjectJaina-Imito-v1.0.apk
  ```
