# ==============================================================================
# PROJECT JAINA: GENERADOR DE ACTIVO PUBLICITARIO WEB (EDICIÓN ANDROID)
# ==============================================================================
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

WIDTH = 1920
HEIGHT = 1080

def create_showcase():
    print("[1/5] Creando lienzo base de 1920x1080...")
    # Fondo base oscuro
    canvas = Image.new("RGBA", (WIDTH, HEIGHT), (10, 10, 20, 255))

    # Cargar fondo épico si existe
    bg_candidates = [
        r"E:\Logo_ProjectJaina\project_jaina_hero_banner.jpg",
        r"E:\Logo_ProjectJaina\project_jaina_living_lore.jpg",
        r"E:\ProjectJaina_Web\images\jaina_hero_banner.jpg"
    ]
    bg_img = None
    for cand in bg_candidates:
        if os.path.exists(cand):
            bg_img = Image.open(cand).convert("RGBA")
            break

    if bg_img:
        # Escalar manteniendo proporción cubriendo el lienzo
        bg_ratio = max(WIDTH / bg_img.width, HEIGHT / bg_img.height)
        new_w = int(bg_img.width * bg_ratio)
        new_h = int(bg_img.height * bg_ratio)
        bg_scaled = bg_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        # Recorte centrado
        left = (new_w - WIDTH) // 2
        top = (new_h - HEIGHT) // 2
        bg_cropped = bg_scaled.crop((left, top, left + WIDTH, top + HEIGHT))

        # Oscurecer y teñir de violeta arcano
        tint = Image.new("RGBA", (WIDTH, HEIGHT), (12, 8, 28, 190))
        bg_final = Image.alpha_composite(bg_cropped, tint)
        canvas.paste(bg_final, (0, 0))

    # Añadir gradiente de viñeta radial/horizontal
    vignette = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    for i in range(150):
        alpha = int((i / 150) * 180)
        v_draw.rectangle([0, HEIGHT - 150 + i, WIDTH, HEIGHT], fill=(5, 5, 12, alpha))
        v_draw.rectangle([0, 0, WIDTH, 150 - i], fill=(5, 5, 12, alpha))
    canvas = Image.alpha_composite(canvas, vignette)

    print("[2/5] Renderizando maqueta de smartphone horizontal...")
    # Dimensiones del teléfono
    phone_w = 920
    phone_h = 510
    phone_x = 930
    phone_y = 280
    corner_r = 36

    # Glow exterior del smartphone
    glow_box = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_box)
    g_draw.rounded_rectangle(
        [phone_x - 20, phone_y - 20, phone_x + phone_w + 20, phone_y + phone_h + 20],
        radius=corner_r + 15,
        fill=(139, 92, 246, 120)  # Púrpura Kirin Tor resplandeciente
    )
    g_draw.rounded_rectangle(
        [phone_x - 10, phone_y - 10, phone_x + phone_w + 10, phone_y + phone_h + 10],
        radius=corner_r + 8,
        fill=(56, 189, 248, 140)  # Cyan arcano brillante
    )
    glow_box = glow_box.filter(ImageFilter.GaussianBlur(28))
    canvas = Image.alpha_composite(canvas, glow_box)

    # Chasis del teléfono (Gris titanio oscuro con borde fino)
    phone_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(phone_layer)
    # Borde exterior plateado
    p_draw.rounded_rectangle(
        [phone_x, phone_y, phone_x + phone_w, phone_y + phone_h],
        radius=corner_r,
        fill=(22, 22, 30, 255),
        outline=(160, 160, 185, 230),
        width=3
    )

    # Pantalla interior
    screen_border = 14
    screen_x1 = phone_x + screen_border
    screen_y1 = phone_y + screen_border
    screen_x2 = phone_x + phone_w - screen_border
    screen_y2 = phone_y + phone_h - screen_border
    screen_w = screen_x2 - screen_x1
    screen_h = screen_y2 - screen_y1

    # Cargar contenido de la pantalla (Living Lore o Wallpapers)
    screen_content_cand = [
        r"E:\ProjectJaina_Lab\ProjectJaina-Imito\assets\wallpapers\wallpaper-2\image.png",
        r"E:\Logo_ProjectJaina\project_jaina_living_lore.jpg",
        r"E:\Logo_ProjectJaina\project_jaina_crest_logo.jpg"
    ]
    screen_img = None
    for cand in screen_content_cand:
        if os.path.exists(cand):
            screen_img = Image.open(cand).convert("RGBA")
            break

    if screen_img:
        s_ratio = max(screen_w / screen_img.width, screen_h / screen_img.height)
        sw = int(screen_img.width * s_ratio)
        sh = int(screen_img.height * s_ratio)
        s_scaled = screen_img.resize((sw, sh), Image.Resampling.LANCZOS)
        s_left = (sw - screen_w) // 2
        s_top = (sh - screen_h) // 2
        s_crop = s_scaled.crop((s_left, s_top, s_left + screen_w, s_top + screen_h))

        # Mascara con esquinas redondeadas para la pantalla
        mask = Image.new("L", (screen_w, screen_h), 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.rounded_rectangle([0, 0, screen_w, screen_h], radius=corner_r - 8, fill=255)

        phone_layer.paste(s_crop, (screen_x1, screen_y1), mask)

    # Superponer HUD virtual móvil (ConsolePort y botones táctiles)
    hud = Image.new("RGBA", (screen_w, screen_h), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(hud)

    # D-Pad táctil en la esquina inferior izquierda
    dpad_cx, dpad_cy = 90, screen_h - 90
    h_draw.ellipse([dpad_cx - 45, dpad_cy - 45, dpad_cx + 45, dpad_cy + 45], fill=(20, 20, 35, 140), outline=(56, 189, 248, 180), width=2)
    h_draw.polygon([(dpad_cx, dpad_cy - 35), (dpad_cx - 15, dpad_cy - 12), (dpad_cx + 15, dpad_cy - 12)], fill=(255, 255, 255, 200))
    h_draw.polygon([(dpad_cx, dpad_cy + 35), (dpad_cx - 15, dpad_cy + 12), (dpad_cx + 15, dpad_cy + 12)], fill=(255, 255, 255, 200))
    h_draw.polygon([(dpad_cx - 35, dpad_cy), (dpad_cx - 12, dpad_cy - 15), (dpad_cx - 12, dpad_cy + 15)], fill=(255, 255, 255, 200))
    h_draw.polygon([(dpad_cx + 35, dpad_cy), (dpad_cx + 12, dpad_cy - 15), (dpad_cx + 12, dpad_cy + 15)], fill=(255, 255, 255, 200))

    # Botones de acción táctiles en la esquina inferior derecha (ABXY ConsolePort)
    btn_cx, btn_cy = screen_w - 95, screen_h - 90
    btn_r = 18
    h_draw.ellipse([btn_cx - btn_r, btn_cy - 40 - btn_r, btn_cx + btn_r, btn_cy - 40 + btn_r], fill=(245, 158, 11, 160), outline=(255, 255, 255, 200), width=2) # Y
    h_draw.ellipse([btn_cx - btn_r, btn_cy + 40 - btn_r, btn_cx + btn_r, btn_cy + 40 + btn_r], fill=(34, 197, 94, 160), outline=(255, 255, 255, 200), width=2)  # A
    h_draw.ellipse([btn_cx - 40 - btn_r, btn_cy - btn_r, btn_cx - 40 + btn_r, btn_cy + btn_r], fill=(59, 130, 246, 160), outline=(255, 255, 255, 200), width=2) # X
    h_draw.ellipse([btn_cx + 40 - btn_r, btn_cy - btn_r, btn_cx + 40 + btn_r, btn_cy + btn_r], fill=(239, 68, 68, 160), outline=(255, 255, 255, 200), width=2)  # B

    # Barra de acción central inferior estilizada
    bar_w = 420
    bar_h = 38
    bar_x = (screen_w - bar_w) // 2
    bar_y = screen_h - 50
    h_draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=8, fill=(10, 10, 20, 170), outline=(139, 92, 246, 180), width=1)
    for b in range(10):
        bx = bar_x + 6 + (b * 41)
        h_draw.rounded_rectangle([bx, bar_y + 4, bx + 34, bar_y + 34], radius=4, fill=(40, 30, 60, 200), outline=(200, 200, 240, 120), width=1)

    # Indicador de 60 FPS en esquina superior derecha
    h_draw.rounded_rectangle([screen_w - 110, 15, screen_w - 20, 42], radius=6, fill=(15, 23, 42, 210), outline=(34, 197, 94, 200), width=1)
    
    # Notch / Cámara frontal en el marco izquierdo
    p_draw.ellipse([phone_x + 6, phone_y + (phone_h // 2) - 6, phone_x + 18, phone_y + (phone_h // 2) + 6], fill=(10, 10, 15, 255))

    phone_layer.paste(hud, (screen_x1, screen_y1), hud)
    canvas = Image.alpha_composite(canvas, phone_layer)

    print("[3/5] Integrando escudo soberano de Lady Jaina y tipografía oficial...")
    # Cargar logo del escudo
    crest_cand = [
        r"E:\ProjectJaina_Lab\ProjectJaina-Imito\assets\branding\imito_icon_adaptive.png",
        r"E:\Logo_ProjectJaina\project_jaina_crest_logo.jpg",
        r"E:\ProjectJaina_Web\images\jaina_crest_logo.jpg"
    ]
    crest_img = None
    for cand in crest_cand:
        if os.path.exists(cand):
            crest_img = Image.open(cand).convert("RGBA")
            break

    text_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(text_layer)

    # Fuentes
    font_path_bold = r"C:\Windows\Fonts\segoeuib.ttf"
    font_path_regular = r"C:\Windows\Fonts\arialbd.ttf"
    title_font = ImageFont.truetype(font_path_bold, 54)
    subtitle_font = ImageFont.truetype(font_path_bold, 30)
    badge_font = ImageFont.truetype(font_path_bold, 20)
    small_font = ImageFont.truetype(font_path_bold, 17)

    # Dibujar Escudo en la izquierda
    if crest_img:
        crest_scaled = crest_img.resize((150, 150), Image.Resampling.LANCZOS)
        # Resplandor dorado para el escudo
        c_glow = Image.new("RGBA", (190, 190), (0, 0, 0, 0))
        cg_draw = ImageDraw.Draw(c_glow)
        cg_draw.ellipse([10, 10, 180, 180], fill=(245, 158, 11, 130))
        c_glow = c_glow.filter(ImageFilter.GaussianBlur(15))
        text_layer.paste(c_glow, (85, 145), c_glow)
        text_layer.paste(crest_scaled, (105, 165), crest_scaled)

    # Textos del panel izquierdo
    t_draw.text((280, 165), "PROJECT JAINA", font=subtitle_font, fill=(167, 139, 250, 255)) # Púrpura claro
    t_draw.text((280, 205), "EDICIÓN ANDROID ARM64", font=title_font, fill=(255, 255, 255, 255))
    t_draw.text((280, 275), "World of Warcraft 3.3.5a en tu Smartphone o Tablet", font=subtitle_font, fill=(56, 189, 248, 255))

    # Badge de cabecera
    badge_x, badge_y = 105, 345
    t_draw.rounded_rectangle([badge_x, badge_y, badge_x + 380, badge_y + 36], radius=8, fill=(124, 58, 237, 220), outline=(192, 132, 252, 255), width=1)
    t_draw.text((badge_x + 18, badge_y + 8), "🚀 CROSS-PLAY TOTAL PC ⇄ ANDROID", font=small_font, fill=(255, 255, 255, 255))

    # Lista de 4 características destacadas con tarjetas
    features = [
        ("📱", "MOTOR ARM64 NATIVO", "Box64 v0.4.5 + Wine 10.10 + Turnip Mesa 26.1 Vulkan"),
        ("🎮", "CONTROLES TÁCTILES & MANDOS", "Touch UI ergonómico + soporte Bluetooth (Xbox, PS5, Razer)"),
        ("🌐", "CONEXIÓN ANYCAST SIN VPN", "Acceso directo a Reino 1 Vanilla 60 y Reino 3 WanitosGYM 80"),
        ("🔋", "MODO ECO TÉRMICO (40/60 FPS)", "Ahorro de batería y mínima temperatura en largas sesiones")
    ]

    card_y = 410
    card_w = 780
    card_h = 75
    for icon, title, desc in features:
        # Fondo de la tarjeta
        t_draw.rounded_rectangle(
            [105, card_y, 105 + card_w, card_y + card_h],
            radius=12,
            fill=(18, 16, 36, 210),
            outline=(76, 29, 149, 160),
            width=1
        )
        # Círculo icono
        t_draw.ellipse([125, card_y + 16, 168, card_y + 59], fill=(109, 40, 217, 180), outline=(167, 139, 250, 200), width=1)
        t_draw.text((134, card_y + 24), icon, font=badge_font, fill=(255, 255, 255, 255))

        # Texto tarjeta
        t_draw.text((185, card_y + 14), title, font=badge_font, fill=(253, 224, 71, 255)) # Amarillo dorado
        t_draw.text((185, card_y + 42), desc, font=small_font, fill=(203, 213, 225, 255)) # Gris claro

        card_y += 90

    # Pastilla de Requisitos Mínimos en la parte inferior
    t_draw.rounded_rectangle([105, 785, 105 + card_w, 835], radius=8, fill=(15, 23, 42, 230), outline=(56, 189, 248, 180), width=1)
    t_draw.text((120, 796), "⚙️ Requisitos Mínimos: Android 12+ · Procesador ARM64 de 64 bits · 6 GB RAM · 16 GB Almacenamiento", font=small_font, fill=(147, 197, 253, 255))

    canvas = Image.alpha_composite(canvas, text_layer)

    print("[4/5] Guardando imágenes renderizadas...")
    # Convertir a RGB para JPEG
    final_rgb = canvas.convert("RGB")
    out_web = r"E:\ProjectJaina_Web\images\project_jaina_mobile_showcase.jpg"
    out_lab = r"E:\ProjectJaina_Lab\ProjectJaina-Imito\assets\project_jaina_mobile_showcase.jpg"

    final_rgb.save(out_web, "JPEG", quality=95, optimize=True)
    final_rgb.save(out_lab, "JPEG", quality=95, optimize=True)

    print(f"[OK] Showcase guardado exitosamente en:\n    {out_web}\n    {out_lab}")

if __name__ == "__main__":
    create_showcase()
