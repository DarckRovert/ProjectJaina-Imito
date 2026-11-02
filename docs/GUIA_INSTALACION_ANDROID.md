# Guía Oficial de Instalación — ProjectJaina-Imito (Android ARM64)

Bienvenido a **ProjectJaina-Imito**, la edición móvil oficial de World of Warcraft 3.3.5a para dispositivos Android (teléfonos, tabletas y consolas portátiles como AYN Odin 2, Retroid Pocket 4 Pro y Razer Edge) integrada con el clúster soberano **Project Jaina**.

---

## 1. Requisitos de Sistema y Almacenamiento

| Componente | Requisito Mínimo | Recomendado |
| :--- | :--- | :--- |
| **Sistema Operativo** | Android 12 | Android 13, 14 o 15 |
| **Arquitectura CPU** | ARM64 (64 bits) | Snapdragon 870 / 888 / 8 Gen 1 / Gen 2 / Gen 3 o Dimensity 8000+ |
| **Memoria RAM** | 6 GB RAM | 8 GB RAM o superior |
| **Almacenamiento Libre** | 18 GB libres (Modo Óptimo) | 38 GB libres (Modo HD) en almacenamiento interno (UFS 3.1 / 4.0) |
| **Cliente de Juego** | Cualquier cliente WoW 3.3.5a con `Data/` | Cliente Oficial Project Jaina |

> [!IMPORTANT]
> Se requiere un procesador ARM64 de 64 bits con Android 12 o posterior. Dispositivos de 32 bits no son compatibles.

---

## 2. Método Recomendado: Asistente Automatizado USB 1-Clic (Windows)

El método más rápido, seguro y libre de errores. No requiere comandos manuales ni navegar por los menús de ajustes del teléfono.

1. **Activar Depuración USB en tu Android:**
   * Ve a **Ajustes > Información del Teléfono** y pulsa 7 veces consecutivas sobre **"Número de compilación"**.
   * Ve a **Ajustes > Opciones de desarrollador** y activa **"Depuración USB"**.
2. **Conectar por USB al PC:**
   * Conecta tu teléfono mediante cable USB a tu PC Windows.
   * Si aparece en la pantalla del móvil el mensaje *¿Permitir depuración por USB desde este equipo?*, marca **"Permitir siempre"** y pulsa **Aceptar**.
3. **Ejecutar el Asistente:**
   * Haz doble clic en [`Instalador_ProjectJaina_Android.bat`](file:///E:/ProjectJaina_Lab/ProjectJaina-Imito/Instalador_ProjectJaina_Android.bat) (o descomprime `ProjectJaina-Imito-Asistente-USB.zip`).
   * El asistente:
     * Validará tu dispositivo y memoria disponible.
     * Instalará la APK oficial con firma criptográfica v3.
     * Concederá de forma desatendida el permiso de almacenamiento.
     * Te permitirá elegir entre el **Modo Móvil Óptimo (~16 GB)** (60 FPS sin cierres de RAM) o **Modo HD**.
     * Transferirá los archivos mediante ADB por bloques a alta velocidad.
     * Inyectará el `realmlist.wtf` del servidor seleccionado y el `Config.wtf` calibrado con cursor táctil de software (`gxCursor "0"`).
4. **¡Listo!** Desconecta el cable y abre la app en tu móvil.

---

## 3. Método Alternativo: Instalación Manual

Si no deseas utilizar el asistente de PC, puedes realizar la instalación de forma manual:

### Paso 1: Instalar la APK Oficial
1. Transfiere o descarga el archivo [`ProjectJaina-Imito-v1.0.apk`](file:///E:/ProjectJaina_Lab/ProjectJaina-Imito/releases/ProjectJaina-Imito-v1.0.apk) en tu dispositivo.
2. Abre tu administrador de archivos y toca el instalador `.apk`.
3. Concede el permiso **"Permitir desde esta fuente"** y completa la instalación.

### Paso 2: Conceder el Permiso de Almacenamiento Completo
Android 12+ requiere permiso de gestión de archivos externa:
1. Ve a **Ajustes de Android > Aplicaciones > ProjectJaina-Imito > Permisos**.
2. Selecciona **Acceso a todos los archivos** y marca **"Permitir administrar todos los archivos"**.

### Paso 3: Crear Carpetas y Transferir Archivos
1. En el almacenamiento interno de tu dispositivo, crea la ruta exacta:
   ```text
   Almacenamiento interno / WoW-Imito / Client /
   ```
2. Copia dentro tu carpeta `Data/` (con `esES` o `enUS`) y tu archivo `Wow.exe`.
3. En `Client/WTF/Config.wtf`, asegúrate de incluir:
   ```text
   SET gxCursor "0"
   SET gxWindow "1"
   SET gxMaximize "1"
   SET Sound_OutputDriverName "System Default"
   SET readTOS "1"
   SET readEULA "1"
   ```

---

## 4. Configuración de Conexión a los Reinos

| Servidor / Entorno | Realmlist (`realmlist.wtf`) | Descripción |
| :--- | :--- | :--- |
| **Reino 1: Global Anycast** | `set realmlist ambulance-ergonomic.tun.ply.gg` | **Recomendado fuera de casa:** Juega con 4G/5G sin VPN. |
| **Reino 1: WiFi Local Casa** | `set realmlist 192.168.1.80` | **En el hogar:** Máxima velocidad y latencia ultrabaja (1 ms). |
| **Reino 3: WanitosGYM** | `set realmlist 100.98.162.75:8087` | **Nodo España:** Cap 80 ICC / WotLK progresivo. |

---

## 5. Solución de Problemas Frecuentes

* **La app se cierra en la pantalla de carga:**  
  *Causa:* Falta de memoria RAM en el dispositivo por haber copiado parches HD de PC (`patch-A` a `patch-G`).  
  *Solución:* Elimina los parches HD opcionales en `/sdcard/WoW-Imito/Client/Data/` dejando solo los archivos canónicos (`common.MPQ`, `common-2.MPQ`, `expansion.MPQ`, `lichking.MPQ`, `patch.MPQ`, `patch-2.MPQ`, `patch-3.MPQ`).
* **El cursor táctil no responde o parpadea:**  
  *Solución:* Abre `WTF/Config.wtf` y verifica que esté configurado `SET gxCursor "0"`.
* **Error de permisos al iniciar:**  
  *Solución:* Concede manualmente el permiso "Acceso a todos los archivos" en los Ajustes de Android para la aplicación.
