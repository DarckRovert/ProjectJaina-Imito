# Guía Oficial de Instalación — ProjectJaina-Imito (Android ARM64)

Bienvenido a **ProjectJaina-Imito**, la edición móvil oficial de World of Warcraft 3.3.5a para dispositivos Android (teléfonos, tabletas y consolas portátiles como AYN Odin 2, Retroid Pocket 4 Pro y Razer Edge) integrada con el clúster soberano **Project Jaina**.

---

## 1. Requisitos de Sistema y Almacenamiento

| Componente | Requisito Mínimo | Recomendado |
| :--- | :--- | :--- |
| **Sistema Operativo** | Android 12 | Android 13, 14 o 15 |
| **Arquitectura CPU** | ARM64 (64 bits) | Snapdragon 870 / 888 / 8 Gen 1 / Gen 2 / Gen 3 o Dimensity 8000+ |
| **Memoria RAM** | 6 GB RAM | 8 GB RAM o superior |
| **Almacenamiento Libre** | 25 GB libres | 35 GB+ en almacenamiento interno rápido (UFS 3.1 / 4.0) |
| **Cliente de Juego** | Cualquier cliente WoW 3.3.5a completo | Cliente Project Jaina FHD Remasterizado |

> [!IMPORTANT]
> Se requiere un procesador ARM64 de 64 bits con Android 12 o posterior. Dispositivos de 32 bits no son compatibles.

---

## 2. Paso a Paso de Instalación

### Paso 1: Instalar la APK Oficial
1. Transfiere o descarga el archivo [`ProjectJaina-Imito-v1.0.apk`](file:///E:/ProjectJaina_Lab/ProjectJaina-Imito/releases/ProjectJaina-Imito-v1.0.apk) en tu teléfono o tableta.
2. Abre tu administrador de archivos y toca el instalador `.apk`.
3. Si el sistema te lo solicita, activa **"Permitir desde esta fuente"**.
4. Completa la instalación. **No abras el juego aún** hasta transferir los archivos de juego.

### Paso 2: Conceder el Permiso de Almacenamiento Completo
Android 12+ requiere permiso de gestión de archivos externa para que Wine y Box64 puedan leer los archivos `.MPQ`:
1. Ve a **Ajustes de Android > Aplicaciones > ProjectJaina-Imito > Permisos**.
2. Selecciona **Archivos y contenido multimedia** (o Acceso a todos los archivos).
3. Marca **"Permitir administrar todos los archivos"**.

### Paso 3: Transferir la Carpeta del Cliente WoW desde tu PC
Conecta tu teléfono a tu ordenador mediante un cable USB tipo C (Modo Transferencia de Archivos / MTP):

1. En el almacenamiento interno de tu teléfono, navega a la carpeta:
   ```
   Almacenamiento interno / WoW-Imito / Client /
   ```
   *(Si la carpeta no existe, créala manualmente respetando mayúsculas y minúsculas).*
2. Copia dentro de `Client` el contenido de tu cliente WoW de PC:
   * La carpeta **`Data/`** (con sus archivos `.MPQ` y la subcarpeta `esES` o `enUS`).
   * La carpeta **`Interface/`** (con tus AddOns preferidos).
   * El ejecutable **`Wow.exe`** de 3.3.5a.

> [!TIP]
> **Transferencia Ultrarrápida:** Para evitar demoras transfiriendo miles de archivos pequeños, se recomienda comprimir la carpeta en un único archivo `.zip` en la PC, transferirlo al teléfono y descomprimirlo directamente allí con ZArchiver o la app de Archivos de tu móvil.

---

## 3. Conexión a los Reinos de Project Jaina

Al abrir **ProjectJaina-Imito**, la aplicación detectará automáticamente tu cliente dentro de `Client/`.

### Configuración del Servidor (Realmlist):
1. En la pantalla principal de la aplicación, toca el icono de engranaje (**Ajustes**) o toca sobre el nombre del cliente reconocido.
2. Selecciona **Set realm** (Configurar reino).
3. Introduce la dirección de acuerdo a tu modo de juego:

* **Opción A — Conexión Global Oficial (Cero VPN / Sin puertos abiertos):**
  ```text
  ambulance-ergonomic.tun.ply.gg
  ```
  *(Recomendado para jugar fuera de casa con datos móviles 4G/5G o WiFi remota).*

* **Opción B — Conexión WiFi en Casa (Mismo Router que el PC Servidor):**
  ```text
  192.168.1.80
  ```
  *(Latencia de 1 ms en tu red local).*

* **Opción C — Conexión mediante Tailscale VPN P2P:**
  * Para **Reino 1 JainaCore** (Host Darck Perú): `100.81.210.121`
  * Para **Reino 3 WanitosGYM** (Host Fran España): `100.98.162.75:8087`

4. Toca en **Save** (Guardar).
5. Pulsa el botón grande **PLAY** y ¡bienvenido a Azeroth!

---

## 4. Opciones de Rendimiento y Batería (Modo ECO)

* **Modo ECO (40 FPS Cap):**  
  Altamente recomendado para sesiones prolongadas de juego. Limita el renderizado a 40 cuadros por segundo estables, reduciendo la temperatura del procesador en hasta un 35% y duplicando la duración de la batería. Se activa en **Settings > ECO Mode**.
* **Driver Gráfico Recomendado:**
  * **Procesadores Snapdragon (Adreno):** Usa el driver **Turnip 26.1.0** (máxima fluidez y estabilidad gráfica).
  * **Procesadores MediaTek Dimensity / Mali:** Usa el driver **Vortek 2.1** o **VirGL**.
