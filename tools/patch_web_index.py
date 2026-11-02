# ==============================================================================
# PROJECT JAINA: INYECTOR QUIRÚRGICO DE SHOWCASE MÓVIL EN PORTAL WEB
# ==============================================================================
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

INDEX_PATH = r"E:\ProjectJaina_Web\index.html"

def patch_index():
    print(f"Leyendo: {INDEX_PATH}")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Modificar Hero Actions si no tiene ya el botón de Android
    hero_target = '            <a href="downloads/ProjectJaina_Launcher.exe" download="ProjectJaina_Launcher.exe" class="btn-primary" style="font-size: 1.05rem; padding: 0.85rem 2rem; background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0c4a6e 100%); border-color: #38bdf8; box-shadow: 0 0 25px rgba(56, 189, 248, 0.4); letter-spacing: 0.5px; color: #ffffff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.75);" title="Descarga directa del Lanzador Oficial v2.1 (~20 MB) ejecutable en 1 Clic">⚡ Descargar Lanzador Oficial v2.1 (~20 MB)</a>'
    hero_replacement = (
        hero_target + "\n" +
        '            <a href="#juego-movil" class="btn-primary" style="font-size: 1.05rem; padding: 0.85rem 1.8rem; background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 50%, #4c1d95 100%); border-color: #a78bfa; box-shadow: 0 0 25px rgba(167, 139, 250, 0.45); letter-spacing: 0.5px; color: #ffffff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.75);" title="Juega a World of Warcraft 3.3.5a en smartphones y tablets Android ARM64">📱 ¡Juega en Android! (ARM64)</a>'
    )

    if '#juego-movil" class="btn-primary"' not in content:
        if hero_target in content:
            content = content.replace(hero_target, hero_replacement, 1)
            print("[OK] Botón de Android inyectado en el Hero.")
        else:
            print("[AVISO] No se encontró hero_target exacto; intentando búsqueda flexible.")
    else:
        print("[SKIP] El botón de Android ya estaba presente en el Hero.")

    # 2. Inyectar la Sección Interactiva #juego-movil antes de #como-jugar
    section_marker = '    <!-- GUÍA DE CONEXIÓN RÁPIDA (ZERO-VPN ANYCAST 1-CLIC) -->'
    
    mobile_section_html = '''    <!-- SECCIÓN INTERACTIVA: EDICIÓN MÓVIL PROJECTJAINA-IMITO (ANDROID ARM64) -->
    <section id="juego-movil" style="padding: 5rem 1.5rem; background: radial-gradient(circle at 50% 20%, rgba(124, 58, 237, 0.12) 0%, rgba(10, 10, 18, 0.98) 75%); border-top: 1px solid rgba(139, 92, 246, 0.25); border-bottom: 1px solid rgba(139, 92, 246, 0.25); position: relative; overflow: hidden;">
        <div style="text-align: center; max-width: 900px; margin: 0 auto;">
            <div class="hero-badge" style="background: rgba(124, 58, 237, 0.2); border-color: rgba(167, 139, 250, 0.5); color: #c084fc; box-shadow: 0 0 20px rgba(167, 139, 250, 0.3);">
                📱 REVOLUCIÓN MÓVIL · CROSS-PLAY TOTAL PC ⇄ ANDROID
            </div>
            <h2 class="section-title" style="background: linear-gradient(135deg, #ffffff 0%, #e9d5ff 50%, #c084fc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Azeroth en tu Bolsillo: ProjectJaina-Imito
            </h2>
            <p class="section-subtitle" style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.6;">
                Juega con tu mismo personaje, en los mismos reinos y junto a tus compañeros de PC desde tu smartphone, tableta o consola portátil Android. Cero emuladores pesados en PC, sin cuotas y con rendimiento optimizado.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; align-items: center; max-width: 1250px; margin: 3rem auto 0;">
            <!-- Mockup Showcase Visual -->
            <div style="position: relative; text-align: center;">
                <div style="position: relative; border-radius: 16px; overflow: hidden; border: 1px solid rgba(167, 139, 250, 0.4); box-shadow: 0 0 35px rgba(124, 58, 237, 0.35);">
                    <img src="images/project_jaina_mobile_showcase.jpg" alt="Project Jaina Edición Android ARM64" style="width: 100%; height: auto; display: block; object-fit: cover;">
                </div>
                <div style="display: flex; gap: 0.6rem; justify-content: center; flex-wrap: wrap; margin-top: 1rem;">
                    <span style="font-size: 0.72rem; background: rgba(124, 58, 237, 0.25); border: 1px solid rgba(167, 139, 250, 0.4); color: #e9d5ff; padding: 4px 10px; border-radius: 9999px; font-weight: 700;">🎮 Touch UI & Mandos</span>
                    <span style="font-size: 0.72rem; background: rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.4); color: #7dd3fc; padding: 4px 10px; border-radius: 9999px; font-weight: 700;">⚡ Box64 + Turnip Mesa 26.1</span>
                    <span style="font-size: 0.72rem; background: rgba(34, 197, 94, 0.2); border: 1px solid rgba(34, 197, 94, 0.4); color: #86efac; padding: 4px 10px; border-radius: 9999px; font-weight: 700;">🌐 Cero VPN Anycast</span>
                </div>
            </div>

            <!-- Grid de Pilares Tecnológicos y Descargas -->
            <div>
                <div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin-bottom: 2rem;">
                    <!-- Pilar 1 -->
                    <div style="background: rgba(20, 16, 36, 0.75); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 1rem 1.2rem; display: flex; gap: 1rem; align-items: flex-start;">
                        <span style="font-size: 1.8rem; line-height: 1;">🎮</span>
                        <div>
                            <h4 style="margin: 0 0 0.25rem 0; font-size: 0.95rem; color: #fde047; font-weight: 700;">Controles Táctiles Adaptativos + Soporte Mando</h4>
                            <p style="margin: 0; font-size: 0.82rem; color: #cbd5e1; line-height: 1.45;">
                                Juega cómodamente con botones virtuales ergonómicos en pantalla o empareja por Bluetooth mandos de Xbox, PS5, Switch Pro, Razer Kishi o consolas AYN Odin.
                            </p>
                        </div>
                    </div>

                    <!-- Pilar 2 -->
                    <div style="background: rgba(20, 16, 36, 0.75); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 1rem 1.2rem; display: flex; gap: 1rem; align-items: flex-start;">
                        <span style="font-size: 1.8rem; line-height: 1;">🔋</span>
                        <div>
                            <h4 style="margin: 0 0 0.25rem 0; font-size: 0.95rem; color: #4ade80; font-weight: 700;">Modo ECO Térmico (40 / 60 FPS)</h4>
                            <p style="margin: 0; font-size: 0.82rem; color: #cbd5e1; line-height: 1.45;">
                                Hasta un 35% de ahorro de batería y menor calentamiento. Raidea en Rasganorte o sube nivel en Vanilla durante horas sin degradar tu dispositivo.
                            </p>
                        </div>
                    </div>

                    <!-- Pilar 3 -->
                    <div style="background: rgba(20, 16, 36, 0.75); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 1rem 1.2rem; display: flex; gap: 1rem; align-items: flex-start;">
                        <span style="font-size: 1.8rem; line-height: 1;">⚡</span>
                        <div>
                            <h4 style="margin: 0 0 0.25rem 0; font-size: 0.95rem; color: #38bdf8; font-weight: 700;">Arquitectura ARM64 Nativa</h4>
                            <p style="margin: 0; font-size: 0.82rem; color: #cbd5e1; line-height: 1.45;">
                                Emulación Box64 v0.4.5 + Wine 10.10 + drivers Mesa Turnip Vulkan de última generación. Máxima tasa de fotogramas sin capas innecesarias.
                            </p>
                        </div>
                    </div>

                    <!-- Pilar 4 -->
                    <div style="background: rgba(20, 16, 36, 0.75); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 1rem 1.2rem; display: flex; gap: 1rem; align-items: flex-start;">
                        <span style="font-size: 1.8rem; line-height: 1;">🌐</span>
                        <div>
                            <h4 style="margin: 0 0 0.25rem 0; font-size: 0.95rem; color: #c084fc; font-weight: 700;">Multi-Reino Anycast sin VPN</h4>
                            <p style="margin: 0; font-size: 0.82rem; color: #cbd5e1; line-height: 1.45;">
                                Conéctate directamente con tus datos móviles (4G/5G) o WiFi a Reino 1 (Vanilla Cap 60) y Reino 3 (WanitosGYM ICC Cap 80).
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Botonera de Descargas Directas -->
                <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
                    <a href="https://github.com/DarckRovert/ProjectJaina-Imito/releases/download/v1.0/ProjectJaina-Imito-v1.0.apk" class="btn-primary" style="flex: 1.3; text-align: center; padding: 0.85rem 1.2rem; font-size: 0.92rem; background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 50%, #4c1d95 100%); border-color: #a78bfa; box-shadow: 0 0 20px rgba(124, 58, 237, 0.4); color: #ffffff !important; text-shadow: 0 1px 3px rgba(0,0,0,0.75);" title="Descargar APK oficial firmada (~430 MB)">
                        📲 Descargar APK Oficial v1.0 (430 MB)
                    </a>
                    <a href="https://github.com/DarckRovert/ProjectJaina-Imito/releases/download/v1.0/ProjectJaina-Imito-Asistente-USB.zip" class="btn-secondary" style="flex: 1; text-align: center; padding: 0.85rem 1rem; font-size: 0.88rem; border-color: rgba(167, 139, 250, 0.5); color: #e9d5ff;" title="Descargar asistente para transferir e instalar por cable USB en 1 clic">
                        ⚡ Asistente USB PC (1 Clic)
                    </a>
                    <a href="https://github.com/DarckRovert/ProjectJaina-Imito" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="padding: 0.85rem 1rem; font-size: 0.88rem; border-color: rgba(255, 255, 255, 0.2); color: #cbd5e1;" title="Ver repositorio oficial en GitHub">
                        📖 Guía GitHub ➔
                    </a>
                </div>
                <div style="margin-top: 0.8rem; font-size: 0.74rem; color: var(--text-muted); text-align: center;">
                    ⚙️ Requisitos: Android 12+ · Procesador ARM64 de 64 bits · 6 GB RAM · 16 GB libres
                </div>
            </div>
        </div>
    </section>

'''

    if 'id="juego-movil"' not in content:
        if section_marker in content:
            content = content.replace(section_marker, mobile_section_html + section_marker, 1)
            print("[OK] Sección interactiva #juego-movil inyectada exitosamente.")
        else:
            print("[ERROR] No se encontró el marcador section_marker para #como-jugar.")
    else:
        print("[SKIP] La sección #juego-movil ya existe en el archivo.")

    # 3. Inyectar Opción 3 en el Paso 2 de Descargas en #como-jugar
    opcion3_marker = '                <!-- Opción C: Espejo de Respaldo Nube (Discreto / Contingencia) -->'
    opcion3_html = '''                <!-- Opción 3: Edición Móvil Android (ARM64) -->
                <div style="background: rgba(147, 51, 234, 0.08); border: 1px solid rgba(168, 85, 247, 0.35); border-radius: 10px; padding: 0.9rem; margin-bottom: 0.8rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
                        <span style="font-size: 0.75rem; font-weight: 800; color: #c084fc; text-transform: uppercase; letter-spacing: 0.5px;">📱 Opción 3 (Móviles & Tablets)</span>
                        <span style="font-size: 0.68rem; background: rgba(168, 85, 247, 0.25); color: #e9d5ff; padding: 1px 6px; border-radius: 4px; font-weight: 700;">Android 12+</span>
                    </div>
                    <div style="font-size: 0.82rem; color: #ffffff; font-weight: 600; margin-bottom: 0.2rem;">¿Quieres jugar en tu smartphone o tablet?</div>
                    <p style="font-size: 0.74rem; color: var(--text-muted); line-height: 1.35; margin-bottom: 0.6rem;">
                        Cliente oficial ProjectJaina-Imito con emulación ARM64, soporte para mandos Bluetooth (Xbox/PS5) y controles táctiles ergonómicos.
                    </p>
                    <div style="display: flex; gap: 0.4rem;">
                        <a href="https://github.com/DarckRovert/ProjectJaina-Imito/releases/download/v1.0/ProjectJaina-Imito-v1.0.apk" class="btn-primary" style="flex: 1.2; text-align: center; padding: 0.55rem 0.4rem; font-size: 0.76rem; background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%); border-color: #a78bfa; font-weight: 700; color: #ffffff !important;" title="Descarga directa del APK Oficial v1.0 para Android">
                            📲 Descargar APK (v1.0)
                        </a>
                        <a href="#juego-movil" class="btn-secondary" style="flex: 1; text-align: center; padding: 0.55rem 0.4rem; font-size: 0.76rem; border-color: rgba(168, 85, 247, 0.5); color: #c084fc; font-weight: 700;" title="Ver guía completa y asistente de instalación USB">
                            ⚡ Asistente USB ➔
                        </a>
                    </div>
                </div>

'''
    if 'Opción 3 (Móviles & Tablets)' not in content:
        if opcion3_marker in content:
            content = content.replace(opcion3_marker, opcion3_html + opcion3_marker, 1)
            print("[OK] Opción 3 de descarga inyectada en #como-jugar.")
        else:
            print("[AVISO] No se encontró opcion3_marker en el archivo.")
    else:
        print("[SKIP] La Opción 3 ya estaba presente en #como-jugar.")

    # 4. Inyectar rutina de detección de Android al final
    js_marker = '</body>'
    mobile_detection_js = '''    <!-- DETECCIÓN PROACTIVA DE VISITANTE ANDROID -->
    <script>
    (function() {
        if (/Android/i.test(navigator.userAgent)) {
            var banner = document.createElement('div');
            banner.id = 'androidVisitorBanner';
            banner.style.cssText = 'position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, #1e1035 0%, #0d0a1a 100%); border: 1px solid #a855f7; box-shadow: 0 4px 25px rgba(168, 85, 247, 0.5); border-radius: 30px; padding: 10px 18px; z-index: 99999; display: flex; align-items: center; gap: 12px; color: #ffffff; font-family: inherit; font-size: 0.85rem; max-width: 90vw; animation: fadeIn 0.4s ease;';
            banner.innerHTML = '<span>📱 <strong>¿Estás en Android?</strong> Juega a Project Jaina en este dispositivo.</span>' +
                '<a href="https://github.com/DarckRovert/ProjectJaina-Imito/releases/download/v1.0/ProjectJaina-Imito-v1.0.apk" style="background: #7c3aed; color: #ffffff; text-decoration: none; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 0.78rem;">Descargar APK</a>' +
                '<button onclick="this.parentElement.remove()" style="background: transparent; border: none; color: #a1a1aa; cursor: pointer; font-size: 1rem; padding: 0 4px;">✕</button>';
            document.body.appendChild(banner);
        }
    })();
    </script>
'''
    if 'androidVisitorBanner' not in content:
        content = content.replace(js_marker, mobile_detection_js + js_marker, 1)
        print("[OK] Script de detección proactiva Android inyectado.")
    else:
        print("[SKIP] Script de detección Android ya estaba presente.")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("[SUCCESS] Archivo index.html modificado y guardado con éxito.")

if __name__ == "__main__":
    patch_index()
