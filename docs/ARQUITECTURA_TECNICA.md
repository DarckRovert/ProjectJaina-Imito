# Arquitectura Técnica — ProjectJaina-Imito (Android ARM64)

> **Autor:** 'Claude Mythos 5' — Staff Software Engineer (L9)  
> **Ecosistema:** Project Jaina / JainaCore 3.3.5a  
> **Pila de Tecnologías:** Box64 + Wine 10.10 + Mesa Turnip / Vortek + Winlator Runtime + Android NDK

---

## 1. Visión General de la Pila de Emulación

```
┌─────────────────────────────────────────────────────────────┐
│             World of Warcraft 3.3.5a (x86_32)               │
│               + Interface / AddOns (Lua 5.1)                │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│           Capa de Traducción de API Win32 (Wine 10.10)      │
│  - wined3d-null-buffer-map.patch (Evita fallos de VBO)      │
│  - wined3d-shader-alpha-test.patch (Corrección de shaders)  │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│       Traducción Binaria Dinámica x86 a ARM64 (Box64 0.4.5) │
│  - Dynarec JIT con compilación BigBlock (Nivel 2/3)         │
│  - Emulación rápida de redondeo x87 y NaNs (FASTNAN/ROUND)  │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│             Capa Gráfica de Usuario / Drivers Vulkan        │
│  - Snapdragon (Adreno): Mesa Turnip 26.1.0 + KGSL Driver    │
│  - Dimensity / Mali: Vortek 2.1 / VirGL 23.1.9             │
│  - DXVK 1.10.3 / 2.4.1 o WineD3D Nativo                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│       Kernel Linux de Android + Hardware Móvil ARM64        │
│  - Android 12+ (API 31-35), SELinux Permissive en Chroot    │
│  - Servicios Foreground: WrathRTGameSessionService          │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Componentes Críticos del Runtime

### 2.1. Traductor Binario Box64 v0.4.5
Box64 intercepta las instrucciones x86 de 32 bits de `Wow.exe` y las compila al vuelo en código máquina nativo ARM64 (AArch64):
* **`BOX64_DYNAREC_BIGBLOCK = 2`**: Genera bloques de compilación continuos en la memoria ELF, reduciendo la penalización de saltos condicionales en el bucle principal de renderizado del cliente WoW.
* **`BOX64_DYNAREC_FASTNAN = 1`**: Optimiza las comparaciones de punto flotante en cálculos de trayectoria de proyectiles y colisiones de terreno.
* **`BOX64_DYNAREC_CALLRET = 1`**: Acelera las llamadas de retorno de funciones en la pila Win32.

### 2.2. Pila de Gráficos y Renderizado
* **Mesa Turnip 26.1.0:** Driver Vulkan de código abierto optimizado para las GPUs Qualcomm Adreno serie 600, 700 y 800. Se comunica directamente con el driver del kernel `kgsl` sin sobrecarga de capas intermedias del sistema operativo.
* **Vortek 2.1 / Zink 22.2.5:** Capas de traducción OpenGL sobre Vulkan para chipsets sin soporte nativo de Turnip (como MediaTek Dimensity o procesadores Exynos con GPU Xclipse).
* **Parches Quirúrgicos de WineD3D:**
  * `wined3d-null-buffer-map.patch`: Resuelve excepciones de puntero nulo al mapear buffers de vértices dinámicos durante cargas masivas de texturas en Dalaran o mazmorras de 25 jugadores.
  * `wined3d-shader-alpha-test.patch`: Corrige artefactos visuales en el canal alfa de partículas mágicas y auras de personajes.

### 2.3. Resiliencia de Red en Android (Servicio Foreground `specialUse`)
A diferencia de los juegos de consola normales, un MMORPG requiere mantener el socket TCP (`authserver` en 3724 y `worldserver` en 8085) vivo incluso si el usuario cambia temporalmente a Discord o atiende una notificación.

ProjectJaina-Imito incorpora:
* **`WrathRTGameSessionService`**: Servicio foreground declarado con subtipo `specialUse` en `AndroidManifest.xml`.
* Evita que el sistema operativo mate el proceso de Box64/Wine por optimización agresiva de batería (Doze Mode) mientras el jugador permanece en el mundo de juego.

---

## 3. Seguridad y Firma Criptográfica de la APK

Para garantizar la instalación limpia sin advertencias de seguridad en Android 12, 13, 14 y 15:
1. **Alineación de Recursos (4-Byte Boundary):**
   * Todas las librerías nativas `.so` sin comprimir están alineadas a límites de 4 bytes (`zipalign -p -f 4`) para permitir la carga mediante `mmap()` directo en memoria sin duplicar el consumo de RAM.
2. **Esquema de Firma APK v2 y v3:**
   * Firmado digitalmente con una clave RSA de 2048 bits (`jaina_release.keystore`) mediante `apksigner`.
   * El esquema v3 protege contra manipulaciones del archivo `.apk` y valida la integridad de cada bloque binario contra el hash SHA-256 oficial.
