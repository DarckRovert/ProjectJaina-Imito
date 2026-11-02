"""
build_jaina_imito.py - Pipeline Maestro de Empaquetado, Branding y Firma
ProjectJaina-Imito (Cliente Oficial Android ARM64 para JainaCore)
Persona: 'Claude Mythos 5' — Staff Software Engineer (L9)
"""

import os
import sys
import shutil
import hashlib
import subprocess
import re

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================================
# RUTAS DE ENTORNO Y HERRAMIENTAS VERIFICADAS
# ==============================================================================
BASE_DIR = r"E:\ProjectJaina_Lab\ProjectJaina-Imito"
LAB_DIR = r"E:\ProjectJaina_Lab"
UPSTREAM_APK = os.path.join(LAB_DIR, "WoW-Imito-Upstream", "WoW-Imito-Public.apk")
DECODED_DIR = os.path.join(LAB_DIR, "apktool_test")
APKTOOL_JAR = os.path.join(LAB_DIR, "apktool.jar")

JAVA_HOME = r"C:\Program Files\Android\Android Studio\jbr"
JAVA_EXE = os.path.join(JAVA_HOME, "bin", "java.exe")
BUILD_TOOLS = r"C:\Users\darck\AppData\Local\Android\Sdk\build-tools\36.0.0"
ZIPALIGN_EXE = os.path.join(BUILD_TOOLS, "zipalign.exe")
APKSIGNER_BAT = os.path.join(BUILD_TOOLS, "apksigner.bat")

KEYSTORE_PATH = os.path.join(BASE_DIR, "tools", "keystore", "jaina_release.keystore")
KEY_ALIAS = "jaina_key"
KEY_PASS = "jainacore2026"

OUT_RELEASES_DIR = os.path.join(BASE_DIR, "releases")
FINAL_APK_NAME = "ProjectJaina-Imito-v1.0.apk"
FINAL_APK_PATH = os.path.join(OUT_RELEASES_DIR, FINAL_APK_NAME)


def check_prerequisites():
    print("[1/6] Verificando herramientas y requisitos del sistema...")
    for path, name in [
        (JAVA_EXE, "OpenJDK 25 Runtime"),
        (ZIPALIGN_EXE, "Android SDK zipalign"),
        (APKSIGNER_BAT, "Android SDK apksigner"),
        (APKTOOL_JAR, "Apktool 2.10.0"),
        (DECODED_DIR, "Árbol decodificado APK base")
    ]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Falta componente crítico: {name} en {path}")
        print(f"  [OK] {name} disponible.")

    # Asegurar keystore en tools/keystore
    os.makedirs(os.path.dirname(KEYSTORE_PATH), exist_ok=True)
    src_ks = os.path.join(LAB_DIR, "jaina_release.keystore")
    if os.path.exists(src_ks) and not os.path.exists(KEYSTORE_PATH):
        shutil.copy2(src_ks, KEYSTORE_PATH)
        print(f"  [OK] Keystore copiado a {KEYSTORE_PATH}")
    elif os.path.exists(KEYSTORE_PATH):
        print(f"  [OK] Keystore verificado en {KEYSTORE_PATH}")
    else:
        raise FileNotFoundError(f"No se encontró el keystore en {src_ks} ni en {KEYSTORE_PATH}")


def inject_branding_and_strings():
    print("\n[2/6] Inyectando Identidad Visual y Branding JainaCore...")

    # 1. Icono Adaptativo de Lanzador (1254x1254)
    adaptive_icon_src = os.path.join(BASE_DIR, "assets", "branding", "imito_icon_adaptive.png")
    adaptive_icon_dst = os.path.join(DECODED_DIR, "res", "drawable-nodpi", "imito_icon_adaptive.png")
    shutil.copy2(adaptive_icon_src, adaptive_icon_dst)
    print("  [OK] Icono adaptativo reemplazado en res/drawable-nodpi/imito_icon_adaptive.png")

    # 2. Wallpapers del Launcher Móvil
    for wp in ["wallpaper-1", "wallpaper-2", "wallpaper-3"]:
        src_wp = os.path.join(BASE_DIR, "assets", "wallpapers", wp)
        dst_wp = os.path.join(DECODED_DIR, "assets", "wallpapers", wp)
        if os.path.exists(src_wp) and os.path.exists(dst_wp):
            shutil.copy2(os.path.join(src_wp, "image.png"), os.path.join(dst_wp, "image.png"))
            shutil.copy2(os.path.join(src_wp, "config.json"), os.path.join(dst_wp, "config.json"))
            print(f"  [OK] Fondos y metadatos actualizados en assets/wallpapers/{wp}")

    # 3. Textos y Nombres Oficiales en strings.xml
    strings_xml_path = os.path.join(DECODED_DIR, "res", "values", "strings.xml")
    with open(strings_xml_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Reemplazos quirúrgicos
    replacements = {
        r'<string name="app_name">[^<]+</string>': '<string name="app_name">ProjectJaina-Imito</string>',
        r'<string name="wrathrt_wordmark">[^<]+</string>': '<string name="wrathrt_wordmark">ProjectJaina-Imito</string>',
        r'<string name="wrathrt_launching">[^<]+</string>': '<string name="wrathrt_launching">Iniciando ProjectJaina-Imito...</string>',
        r'<string name="imito_distribution_short">"[^"]+"</string>': '<string name="imito_distribution_short">"ProjectJaina-Imito\\nEdición Oficial JainaCore"</string>',
        r'<string name="wow_help_title">[^<]+</string>': '<string name="wow_help_title">Controles y Mandos ProjectJaina-Imito</string>',
    }

    for pattern, repl in replacements.items():
        content, count = re.subn(pattern, repl, content)
        print(f"  [OK] Patrón '{pattern[:30]}...' sustituido ({count} ocurrencias).")

    with open(strings_xml_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  [OK] res/values/strings.xml actualizado y guardado.")


def build_apk():
    print("\n[3/6] Reconstruyendo paquete APK con Apktool 2.10.0...")
    raw_apk = os.path.join(LAB_DIR, "jaina_raw_build.apk")
    if os.path.exists(raw_apk):
        os.remove(raw_apk)

    cmd = [
        JAVA_EXE,
        "-jar", APKTOOL_JAR,
        "b", DECODED_DIR,
        "-o", raw_apk
    ]
    env = os.environ.copy()
    env["JAVA_HOME"] = JAVA_HOME

    print(f"  Ejecutando: {' '.join(cmd)}")
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print("ERROR en Apktool Build:\n", res.stderr)
        raise RuntimeError("Fallo en reconstrucción con Apktool.")

    size_mb = os.path.getsize(raw_apk) / (1024 * 1024)
    print(f"  [OK] APK sin alinear ensamblada exitosamente: {size_mb:.2f} MB")
    return raw_apk


def align_apk(raw_apk):
    print("\n[4/6] Optimizando y alineando archivo con zipalign (4-byte alignment)...")
    aligned_apk = os.path.join(LAB_DIR, "jaina_aligned.apk")
    if os.path.exists(aligned_apk):
        os.remove(aligned_apk)

    cmd = [ZIPALIGN_EXE, "-p", "-f", "4", raw_apk, aligned_apk]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("ERROR en zipalign:\n", res.stderr)
        raise RuntimeError("Fallo en alineación con zipalign.")

    print("  [OK] APK alineada correctamente.")
    return aligned_apk


def sign_and_verify_apk(aligned_apk):
    print("\n[5/6] Firmando criptográficamente con apksigner (Esquemas v2 y v3)...")
    os.makedirs(OUT_RELEASES_DIR, exist_ok=True)
    if os.path.exists(FINAL_APK_PATH):
        os.remove(FINAL_APK_PATH)

    cmd = [
        APKSIGNER_BAT,
        "sign",
        "--v1-signing-enabled", "true",
        "--v2-signing-enabled", "true",
        "--v3-signing-enabled", "true",
        "--ks", KEYSTORE_PATH,
        "--ks-key-alias", KEY_ALIAS,
        "--ks-pass", f"pass:{KEY_PASS}",
        "--key-pass", f"pass:{KEY_PASS}",
        "--out", FINAL_APK_PATH,
        aligned_apk
    ]

    env = os.environ.copy()
    env["JAVA_HOME"] = JAVA_HOME
    env["PATH"] = f"{os.path.join(JAVA_HOME, 'bin')};{env.get('PATH', '')}"

    res = subprocess.run(cmd, env=env, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print("ERROR en apksigner sign:\n", res.stderr)
        raise RuntimeError("Fallo en firma de APK.")

    print(f"  [OK] APK firmada y emitida: {FINAL_APK_PATH}")

    # Verificación estricta
    print("  Verificando firma digital con apksigner verify...")
    verify_cmd = [APKSIGNER_BAT, "verify", "--verbose", FINAL_APK_PATH]
    vres = subprocess.run(verify_cmd, env=env, shell=True, capture_output=True, text=True)
    print("  --- Resultado de Verificación ---")
    for line in vres.stdout.splitlines():
        if "Verified" in line or "Verifies" in line or "Number of signers" in line:
            print(f"    {line.strip()}")

    if "Verifies" not in vres.stdout and vres.returncode != 0:
        raise RuntimeError("La verificación de firma falló.")


def generate_checksums():
    print("\n[6/6] Calculando suma de verificación SHA-256 del binario final...")
    sha256 = hashlib.sha256()
    with open(FINAL_APK_PATH, "rb") as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    digest = sha256.hexdigest().upper()
    size_bytes = os.path.getsize(FINAL_APK_PATH)
    size_mb = size_bytes / (1024 * 1024)

    sha_file = os.path.join(OUT_RELEASES_DIR, "SHA256SUMS.txt")
    with open(sha_file, "w", encoding="utf-8") as f:
        f.write(f"{digest}  {FINAL_APK_NAME}\n")

    print(f"  Archivo: {FINAL_APK_NAME}")
    print(f"  Tamaño:  {size_mb:.2f} MB ({size_bytes} bytes)")
    print(f"  SHA-256: {digest}")
    print(f"  Checksum guardado en: {sha_file}")


def cleanup_intermediates():
    for f in ["jaina_raw_build.apk", "jaina_aligned.apk"]:
        p = os.path.join(LAB_DIR, f)
        if os.path.exists(p):
            os.remove(p)


if __name__ == "__main__":
    print("=================================================================")
    print("🚀 PIPELINE DE ENSAMBLADO PROJECTJAINA-IMITO (L9 STAFF ENGINEER)")
    print("=================================================================")
    try:
        check_prerequisites()
        inject_branding_and_strings()
        raw = build_apk()
        aligned = align_apk(raw)
        sign_and_verify_apk(aligned)
        generate_checksums()
        cleanup_intermediates()
        print("\n=================================================================")
        print("✅ COMPILACIÓN Y FIRMA DE PROJECTJAINA-IMITO FINALIZADA CON ÉXITO")
        print("=================================================================")
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO EN EL PIPELINE: {e}")
        sys.exit(1)
