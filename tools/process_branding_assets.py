"""
process_branding_assets.py - Pipeline de Generación de Activos Gráficos Oficiales
ProjectJaina-Imito (Android ARM64 Client)
L9 Staff Software Engineer - Claude Mythos 5
"""

import os
import json
from PIL import Image, ImageFilter, ImageOps, ImageDraw

BASE_DIR = r"E:\ProjectJaina_Lab\ProjectJaina-Imito"
LOGO_DIR = r"E:\Logo_ProjectJaina"
DIST_LOGO = r"E:\ProjectJaina_Distribucion_Publica\01_Cliente_ProjectJaina_Publico\logo.png"

CREST_SRC = os.path.join(LOGO_DIR, "project_jaina_crest_logo.jpg")
HERO_SRC = os.path.join(LOGO_DIR, "project_jaina_hero_banner.jpg")
LORE_SRC = os.path.join(LOGO_DIR, "project_jaina_living_lore.jpg")

BRANDING_OUT = os.path.join(BASE_DIR, "assets", "branding")
WALLPAPERS_OUT = os.path.join(BASE_DIR, "assets", "wallpapers")


def create_adaptive_icon():
    print("[1/4] Generando Icono Adaptativo Android (1254x1254 px)...")
    target_size = (1254, 1254)
    canvas = Image.new("RGBA", target_size, (10, 17, 40, 255))  # Deep Arcane Navy #0a1128

    # Radial vignette gradient
    vignette = Image.new("RGBA", target_size, (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    cx, cy = target_size[0] // 2, target_size[1] // 2
    max_r = target_size[0] // 2
    for r in range(max_r, 0, -8):
        alpha = int(220 * (r / max_r) ** 1.8)
        # Outer dark ring
        vdraw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(5, 8, 20, 255 - alpha))

    canvas.paste(vignette, (0, 0), vignette)

    # Load Crest Logo
    crest = Image.open(CREST_SRC).convert("RGBA")
    
    # Safe zone for Android adaptive icon is inner 66% (~820px)
    crest_size = 850
    crest_resized = crest.resize((crest_size, crest_size), Image.Resampling.LANCZOS)

    # Optional circular mask with soft feathering
    mask = Image.new("L", (crest_size, crest_size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.ellipse([10, 10, crest_size - 10, crest_size - 10], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(8))

    # Center crest on canvas
    offset_x = (target_size[0] - crest_size) // 2
    offset_y = (target_size[1] - crest_size) // 2
    canvas.paste(crest_resized, (offset_x, offset_y), mask)

    # Save to branding and apk resources
    out_path = os.path.join(BRANDING_OUT, "imito_icon_adaptive.png")
    canvas.save(out_path, "PNG", optimize=True)
    print(f"      -> Guardado: {out_path} ({os.path.getsize(out_path)} bytes)")


def create_wallpapers():
    print("[2/4] Generando Fondos de Pantalla para Launcher Móvil (512x512 px)...")
    
    # Wallpaper 1: Arcane Crest
    wp1_dir = os.path.join(WALLPAPERS_OUT, "wallpaper-1")
    os.makedirs(wp1_dir, exist_ok=True)
    crest = Image.open(CREST_SRC).convert("RGB")
    wp1_img = ImageOps.fit(crest, (512, 512), Image.Resampling.LANCZOS)
    wp1_img = wp1_img.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
    wp1_path = os.path.join(wp1_dir, "image.png")
    wp1_img.save(wp1_path, "PNG", optimize=True)
    with open(os.path.join(wp1_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump({
            "primaryColor": "#01579b",
            "secondaryColor": "#0277bd",
            "orientation": "horizontal"
        }, f, indent=4)
    print("      -> Wallpaper 1 generado (Crest Arcana JainaCore).")

    # Wallpaper 2: Theramore Living Lore
    wp2_dir = os.path.join(WALLPAPERS_OUT, "wallpaper-2")
    os.makedirs(wp2_dir, exist_ok=True)
    lore = Image.open(LORE_SRC).convert("RGB")
    wp2_img = ImageOps.fit(lore, (512, 512), Image.Resampling.LANCZOS)
    wp2_path = os.path.join(wp2_dir, "image.png")
    wp2_img.save(wp2_path, "PNG", optimize=True)
    with open(os.path.join(wp2_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump({
            "primaryColor": "#0d1b2a",
            "secondaryColor": "#1b263b",
            "orientation": "vertical",
            "scale": 0.675
        }, f, indent=4)
    print("      -> Wallpaper 2 generado (Theramore Living Lore).")

    # Wallpaper 3: Icecrown Frostmourne WanitosGYM (Cap 80)
    wp3_dir = os.path.join(WALLPAPERS_OUT, "wallpaper-3")
    os.makedirs(wp3_dir, exist_ok=True)
    hero = Image.open(HERO_SRC).convert("RGB")
    wp3_img = ImageOps.fit(hero, (512, 512), Image.Resampling.LANCZOS)
    wp3_path = os.path.join(wp3_dir, "image.png")
    wp3_img.save(wp3_path, "PNG", optimize=True)
    with open(os.path.join(wp3_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump({
            "primaryColor": "#00acc1",
            "secondaryColor": "#1565c0",
            "orientation": "horizontal"
        }, f, indent=4)
    print("      -> Wallpaper 3 generado (Hero Arcana/Escarcha WanitosGYM).")


def create_repo_banner():
    print("[3/4] Generando Banner Panorámico del Repositorio...")
    hero = Image.open(HERO_SRC).convert("RGB")
    banner = ImageOps.fit(hero, (1920, 1080), Image.Resampling.LANCZOS)
    banner_path = os.path.join(BASE_DIR, "assets", "project-jaina-imito-banner.jpg")
    banner.save(banner_path, "JPEG", quality=92, optimize=True)
    print(f"      -> Guardado: {banner_path} ({os.path.getsize(banner_path)} bytes)")


def create_standard_icons():
    print("[4/4] Generando Iconos de Densidad Mipmap Android...")
    crest = Image.open(CREST_SRC).convert("RGBA")
    densities = {
        "mdpi": (48, 48),
        "hdpi": (72, 72),
        "xhdpi": (96, 96),
        "xxhdpi": (144, 144),
        "xxxhdpi": (192, 192),
        "playstore": (512, 512)
    }
    for name, size in densities.items():
        icon = crest.resize(size, Image.Resampling.LANCZOS)
        icon_path = os.path.join(BRANDING_OUT, f"ic_launcher_{name}.png")
        icon.save(icon_path, "PNG", optimize=True)
    print("      -> Iconos mipmap (48, 72, 96, 144, 192, 512 px) generados exitosamente.")


if __name__ == "__main__":
    print("=== Pipeline de Generación Gráfica ProjectJaina-Imito ===")
    create_adaptive_icon()
    create_wallpapers()
    create_repo_banner()
    create_standard_icons()
    print("=== Generación Gráfica Completada al 100% ===")
