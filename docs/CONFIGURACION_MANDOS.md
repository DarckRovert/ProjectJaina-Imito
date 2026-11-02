# Configuración de Mandos y Controles — ProjectJaina-Imito

**ProjectJaina-Imito** incorpora soporte nativo para dos modalidades de control de primer nivel: **Controles Táctiles (Touch UI)** para jugar directamente con la pantalla de tu móvil o tableta, y **Mandos Físicos (ConsolePortLK)** para una experiencia de consola de sobremesa portátil.

---

## 1. Modos de Control Disponibles

> [!IMPORTANT]
> El modo **Touch UI** y el modo **ConsolePort** son mutuamente excluyentes. En la pantalla de selección de personajes, toca el botón **AddOns** y activa el que corresponda a tu estilo de juego actual:
> - Para jugar **con la pantalla táctil**: Activa `WoW Imito Touch UI` / `ImitoTouchUI`.
> - Para jugar **con mando físico**: Activa `ConsolePort` y `ConsolePortBar` (y desactiva `ImitoTouchUI`).

---

## 2. Compatibilidad con Mandos Físicos

El cliente reconoce de forma automática los mandos conectados por Bluetooth o cable USB-C a tu dispositivo Android:

| Dispositivo | Tipo de Conexión | Compatibilidad | Notas |
| :--- | :--- | :---: | :--- |
| **Xbox Wireless Controller (Series X/S / One)** | Bluetooth / USB OTG | 100% Nativo | Mapeo oficial ABXY estándar. |
| **PlayStation DualSense (PS5) / DualShock 4** | Bluetooth / USB OTG | 100% Nativo | Soporte de touchpad y botones Cruz/Círculo. |
| **Mandos Telescópicos (Razer Kishi, GameSir G8)** | USB-C Directo | 100% Nativo | Cero latencia por conexión directa por bus. |
| **Consolas Portátiles (AYN Odin 2, Retroid, RG556)** | Integrado | 100% Nativo | Mapeo analógico y gatillos analógicos L2/R2. |

---

## 3. Asistente Inicial de ConsolePortLK

Al iniciar sesión por primera vez con el AddOn **ConsolePort** activo:
1. Aparecerá en el centro de la pantalla el **Asistente de Calibración de Mando**.
2. Presiona los botones que el asistente te indique:
   * **Gatillo Izquierdo (LT / L2)** y **Gatillo Derecho (RT / R2)**.
   * **Cruceta Direccional (D-Pad)**: Arriba, Abajo, Izquierda, Derecha.
   * **Botones de Acción**: A/Cruz, B/Círculo, X/Cuadrado, Y/Triángulo.
3. Elige tu distribución de botones preferida (Xbox Style o PlayStation Style).
4. Guarda la configuración. Tus combinaciones de hechizos quedarán asignadas a los botones principales combinados con los gatillos modificadores (`LT + A`, `RT + X`, etc.), permitiéndote acceder a más de 40 habilidades sin soltar los joysticks.

---

## 4. Modo Táctil (WoW Imito Touch UI)

Si juegas sin mando, el modo táctil proyecta una interfaz ergonómica en pantalla:
* **Joystick Izquierdo Virtual:** Movimiento continuo del personaje y giro de cámara.
* **Zona Derecha:** Toques rápidos para lanzar hechizos, saltar y seleccionar objetivos más cercanos.
* **Pellizco (Pinch to Zoom):** Alejar o acercar la cámara del personaje como en un juego nativo de móvil.
* **Barra de Acceso Rápido:** Bolsas, mapa, panel de personaje y libro de hechizos situados en las esquinas superiores para evitar pulsaciones accidentales en combate.

---

## 5. Addon de Batería y Rendimiento (Titan Panel Móvil)

En la parte superior de la pantalla verás la barra **Titan Panel**:
* Muestra el porcentaje de batería real de tu teléfono Android en tiempo real.
* Muestra el estado de la conexión de red (Ping / Latencia hacia el servidor).
* Muestra los fotogramas por segundo (FPS) en tiempo real para verificar la fluidez del juego.
