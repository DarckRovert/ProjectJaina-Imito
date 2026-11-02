# ProjectJaina-Imito — Modelo de Gobernanza y Normas de Ingeniería L9

## 1. Misión y Filosofía Soberana
**ProjectJaina-Imito** es el cliente oficial de World of Warcraft 3.3.5a para dispositivos Android (ARM64, Android 12+) perteneciente al ecosistema **Project Jaina / JainaCore**.

El objetivo primordial del proyecto es garantizar una experiencia de juego de escritorio en movilidad con paridad total de características respecto al cliente de PC, asegurando:
1. Conexión soberana y fluida a los reinos del clúster:
   - **Reino 1 — JainaCore** (Vanilla Cap 60 / Host Darck Perú).
   - **Reino 3 — WanitosGYM** (WotLK ICC Cap 80 / Host Fran España).
   - **Túnel de Red Remoto Playit / WAN** (conectividad sin NAT ni retrasos).
2. Estabilidad técnica de grado de producción (60 FPS estables o 40 FPS en Modo ECO de larga duración).
3. Gobernanza transparente, respeto estricto a las licencias de software libre (LGPL-2.1 de Winlator / WoW-Imito y MIT de Box64/Mesa) y preservación de la identidad visual de Lady Jaina Proudmoore.

---

## 2. Invariantes de Arquitectura de Red y Multi-Reino
- **Prioridad de Autenticación:** El servidor de autenticación central (`authserver` en puerto 3724) reside en el Nodo 1 Maestro (Perú - Darck). Todos los clientes móviles apuntan a esta autoridad para inicio de sesión unificado.
- **Conmutación de Reino:** La era del reino se determina dinámicamente en el servidor. El cliente móvil soporta tanto contenido nivel 60 (Reino 1) como nivel 80 (Reino 3) sin alterar archivos locales.
- **Preservación de Ajustes de Cliente:** El lanzador no mutará jamás las configuraciones de interfaz del jugador al alternar servidores.

---

## 3. Estándar de Contribución (Claude Mythos 5 — L9 Staff Engineer)
- **Cero Suposiciones:** Toda modificación en emulación, drivers gráficos (Turnip, Vortek, VirGL) o capas de compatibilidad debe probarse empíricamente con mediciones de rendimiento y compatibilidad de GPU.
- **Empaquetado Seguro:** Los paquetes APK distribuidos deben estar siempre firmados con claves criptográficas válidas bajo los esquemas Android v2 y v3, verificadas con `apksigner`.
