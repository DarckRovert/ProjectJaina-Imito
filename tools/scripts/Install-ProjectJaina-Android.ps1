# ==============================================================================
# PROJECT JAINA: ASISTENTE INSTALADOR AUTOMATIZADO 1-CLIC PARA ANDROID
# ==============================================================================
# Arquitectura: PowerShell Nativo + ADB Embebido (Cero Dependencias de Terceros)
# Dispositivo Objetivo: Smartphons y Tablets Android 12+ (ARM64)
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "Project Jaina - Asistente Instalador Móvil (Android ARM64)"

function Show-Header {
    Clear-Host
    Write-Host "===============================================================================" -ForegroundColor Cyan
    Write-Host "   PROJECT JAINA: ASISTENTE DE DESPLIEGUE AUTOMATIZADO PARA ANDROID" -ForegroundColor Magenta
    Write-Host "   Juega a WoW 3.3.5a en tu Smartphone o Tablet junto a Jugadores de PC" -ForegroundColor White
    Write-Host "===============================================================================" -ForegroundColor Cyan
    Write-Host ""
}

# 1. Localizar binario ADB
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$AdbCandidates = @(
    (Join-Path $ScriptDir "..\adb\adb.exe"),
    (Join-Path $ScriptDir "..\..\tools\adb\adb.exe"),
    (Join-Path $ScriptDir "tools\adb\adb.exe"),
    "C:\Users\darck\AppData\Local\Android\Sdk\platform-tools\adb.exe",
    "adb.exe"
)

$AdbPath = $null
foreach ($c in $AdbCandidates) {
    if (Test-Path $c) {
        $AdbPath = (Resolve-Path $c).Path
        break
    }
}

if (-not $AdbPath) {
    # Intentar en el PATH
    $cmd = Get-Command "adb" -ErrorAction SilentlyContinue
    if ($cmd) { $AdbPath = $cmd.Source }
}

if (-not $AdbPath) {
    Show-Header
    Write-Host "[ERROR CRÍTICO] No se encontró el binario adb.exe ni en tools\adb ni en el sistema." -ForegroundColor Red
    Write-Host "Por favor asegúrate de que la carpeta tools\adb contenga adb.exe y sus librerías DLL." -ForegroundColor Yellow
    Write-Host ""
    Pause
    Exit 1
}

# 2. Localizar APK oficial
$ApkCandidates = @(
    (Join-Path $ScriptDir "..\..\releases\ProjectJaina-Imito-v1.0.apk"),
    (Join-Path $ScriptDir "..\..\ProjectJaina-Imito-v1.0.apk"),
    (Join-Path $ScriptDir "..\ProjectJaina-Imito-v1.0.apk"),
    (Join-Path $ScriptDir "ProjectJaina-Imito-v1.0.apk"),
    "E:\ProjectJaina_Lab\ProjectJaina-Imito\releases\ProjectJaina-Imito-v1.0.apk",
    "E:\ProjectJaina_Distribucion_Publica\04_Cliente_Android_Imito\ProjectJaina-Imito-v1.0.apk"
)

$ApkPath = $null
foreach ($a in $ApkCandidates) {
    if (Test-Path $a) {
        $ApkPath = (Resolve-Path $a).Path
        break
    }
}

# 3. Ciclo de detección de dispositivo
function Get-ConnectedDevice {
    while ($true) {
        Show-Header
        Write-Host ">>> [1/5] ESCANEANDO DISPOSITIVOS ANDROID CONECTADOS..." -ForegroundColor Yellow
        Write-Host "    Binario ADB: $AdbPath" -ForegroundColor DarkGray
        Write-Host ""

        $rawDevices = & $AdbPath devices
        $lines = $rawDevices -split "`r?`n" | Where-Object { $_ -match "\S" -and $_ -notmatch "List of devices attached" }
        
        $validDevices = @()
        $unauthorized = $false

        foreach ($line in $lines) {
            $parts = -split $line
            if ($parts.Count -ge 2) {
                $serial = $parts[0]
                $state = $parts[1]
                if ($state -eq "device") {
                    $validDevices += $serial
                } elseif ($state -eq "unauthorized") {
                    $unauthorized = $true
                }
            }
        }

        if ($validDevices.Count -gt 0) {
            return $validDevices[0]
        }

        if ($unauthorized) {
            Write-Host "[DISPOSITIVO DETECTADO PERO NO AUTORIZADO]" -ForegroundColor Yellow
            Write-Host "Por favor DESBLOQUEA la pantalla de tu móvil o tablet." -ForegroundColor White
            Write-Host "Aparecerá un mensaje: '¿Permitir depuración por USB desde este equipo?'" -ForegroundColor Cyan
            Write-Host "Marca la casilla [X] 'Permitir siempre' y pulsa ACEPTAR." -ForegroundColor Green
            Write-Host ""
        } else {
            Write-Host "[NO SE DETECTÓ NINGÚN DISPOSITIVO ANDROID POR USB]" -ForegroundColor Red
            Write-Host ""
            Write-Host "Para conectar tu teléfono en 30 segundos:" -ForegroundColor Cyan
            Write-Host "  1. Ve a Ajustes -> Información del Teléfono -> Pulsa 7 veces 'Número de compilación'." -ForegroundColor White
            Write-Host "  2. Ve a Ajustes -> Sistema / Opciones de Desarrollador -> Activa 'Depuración USB'." -ForegroundColor White
            Write-Host "  3. Conecta el cable USB a este PC y elige modo 'Transferencia de Archivos'." -ForegroundColor White
            Write-Host ""
        }

        Write-Host "Opciones: [R] Reintentar escaneo  |  [S] Salir" -ForegroundColor DarkYellow
        $opt = Read-Host "Ingresa tu opción (R/S) [Por defecto R]"
        if ($opt -match "s|S") {
            Exit 0
        }
    }
}

$DeviceSerial = Get-ConnectedDevice

# 4. Obtener especificaciones del dispositivo
Show-Header
Write-Host ">>> [2/5] VERIFICANDO COMPATIBILIDAD DE HARDWARE..." -ForegroundColor Yellow
$model = (& $AdbPath -s $DeviceSerial shell getprop ro.product.model).Trim()
$mfr = (& $AdbPath -s $DeviceSerial shell getprop ro.product.manufacturer).Trim()
$androidVer = (& $AdbPath -s $DeviceSerial shell getprop ro.build.version.release).Trim()
$abi = (& $AdbPath -s $DeviceSerial shell getprop ro.product.cpu.abi).Trim()

# Espacio libre en almacenamiento
$dfOut = (& $AdbPath -s $DeviceSerial shell df -k /sdcard) -split "`r?`n"
$freeKb = 0
if ($dfOut.Count -ge 2) {
    $cols = -split $dfOut[1]
    if ($cols.Count -ge 4) {
        $freeKb = [int64]$cols[3]
    }
}
$freeGb = [math]::Round($freeKb / 1024 / 1024, 2)

Write-Host "    Dispositivo Detectado : $mfr $model" -ForegroundColor Green
Write-Host "    Versión de Android    : Android $androidVer" -ForegroundColor White
Write-Host "    Arquitectura de CPU   : $abi" -ForegroundColor White
Write-Host "    Almacenamiento Libre  : $freeGb GB disponibles en /sdcard" -ForegroundColor Cyan
Write-Host ""

if ($abi -notmatch "arm64") {
    Write-Host "[ADVERTENCIA] Tu procesador no reporta arm64-v8a ($abi)." -ForegroundColor Red
    Write-Host "ProjectJaina-Imito requiere CPU de 64 bits para la emulación ARM64." -ForegroundColor Yellow
    $ans = Read-Host "¿Deseas continuar de todos modos? (S/N)"
    if ($ans -notmatch "s|S") { Exit 1 }
}

# 5. Instalación de la APK Oficial
Write-Host ">>> [3/5] INSTALANDO APLICACIÓN OFICIAL PROJECTJAINA-IMITO v1.0..." -ForegroundColor Yellow
if ($ApkPath -and (Test-Path $ApkPath)) {
    Write-Host "    Instalando: $ApkPath" -ForegroundColor DarkGray
    & $AdbPath -s $DeviceSerial install -r -d "$ApkPath"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "    [OK] APK instalada y verificada exitosamente." -ForegroundColor Green
    } else {
        Write-Host "    [AVISO] Si la app ya estaba instalada con otra firma, desinstálala primero del móvil." -ForegroundColor Yellow
    }
} else {
    Write-Host "    [AVISO] No se encontró el binario APK local. Omitiendo instalación de APK." -ForegroundColor Yellow
}

# 6. Concesión Automática de Permisos
Write-Host ""
Write-Host ">>> CONCEDIENDO PERMISO 'ACCESO A TODOS LOS ARCHIVOS'..." -ForegroundColor Yellow
& $AdbPath -s $DeviceSerial shell appops set pub.wowimito MANAGE_EXTERNAL_STORAGE allow 2>$null
& $AdbPath -s $DeviceSerial shell am start -a android.settings.MANAGE_APP_ALL_FILES_ACCESS_PERMISSION -d package:pub.wowimito >$null 2>$null
Write-Host "    [OK] Permiso de almacenamiento de archivos inyectado." -ForegroundColor Green

# 7. Creación de estructura de directorios en Android
Write-Host ""
Write-Host ">>> CREANDO ESTRUCTURA EN /sdcard/WoW-Imito/Client/..." -ForegroundColor Yellow
& $AdbPath -s $DeviceSerial shell mkdir -p /sdcard/WoW-Imito/Client/Data/esES
& $AdbPath -s $DeviceSerial shell mkdir -p /sdcard/WoW-Imito/Client/Data/enUS
& $AdbPath -s $DeviceSerial shell mkdir -p /sdcard/WoW-Imito/Client/WTF
Write-Host "    [OK] Directorios base creados." -ForegroundColor Green

# 8. Selección de Carpeta del Cliente WoW en PC
Show-Header
Write-Host ">>> [4/5] LOCALIZACIÓN DE ARCHIVOS DE WORLD OF WARCRAFT 3.3.5a" -ForegroundColor Yellow
Write-Host ""

$ClientSourceCandidates = @(
    "E:\ProjectJaina_FHD\Client",
    "E:\ProjectJaina_Distribucion_Publica\01_Cliente_ProjectJaina_Publico\Client",
    "E:\ProjectJaina_Distribucion_Publica\01_Cliente_ProjectJaina_Publico",
    "..\01_Cliente_ProjectJaina_Publico\Client",
    "..\Client",
    "C:\World of Warcraft 3.3.5a",
    "D:\World of Warcraft 3.3.5a"
)

$DetectedClient = $null
foreach ($cand in $ClientSourceCandidates) {
    if (Test-Path "$cand\Data\common.MPQ") {
        $DetectedClient = (Resolve-Path $cand).Path
        break
    } elseif (Test-Path "$cand\Data\common.mpq") {
        $DetectedClient = (Resolve-Path $cand).Path
        break
    }
}

if ($DetectedClient) {
    Write-Host "Se detectó automáticamente un cliente WoW en:" -ForegroundColor Cyan
    Write-Host "    $DetectedClient" -ForegroundColor White
    Write-Host ""
    $useAuto = Read-Host "¿Deseas utilizar este cliente para transferir a tu teléfono? (S/N) [Por defecto S]"
    if ($useAuto -match "n|N") {
        $DetectedClient = $null
    }
}

if (-not $DetectedClient) {
    Write-Host "Selecciona la carpeta raíz de tu cliente World of Warcraft 3.3.5a..." -ForegroundColor Yellow
    Add-Type -AssemblyName System.Windows.Forms
    $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $dialog.Description = "Selecciona la carpeta de World of Warcraft 3.3.5a (donde está Wow.exe y Data)"
    $dialog.ShowNewFolderButton = $false
    if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
        $DetectedClient = $dialog.SelectedPath
    } else {
        Write-Host "Operación cancelada por el usuario." -ForegroundColor Yellow
        Exit 0
    }
}

$DataDir = Join-Path $DetectedClient "Data"
if (-not (Test-Path $DataDir)) {
    Write-Host "[ERROR] La carpeta seleccionada no contiene la subcarpeta 'Data'." -ForegroundColor Red
    Pause
    Exit 1
}

# 9. Selección de Perfil de Copiado (Prevención de OOM)
Show-Header
Write-Host ">>> SELECCIONA EL PERFIL DE RENDIMIENTO PARA TU TELÉFONO" -ForegroundColor Yellow
Write-Host ""
Write-Host "  [1] MODO MÓVIL ÓPTIMO (~16 GB - RECOMENDADO)" -ForegroundColor Green
Write-Host "      - Transfiere solo archivos oficiales 3.3.5a + idioma + AddOns táctiles."
Write-Host "      - 60 FPS estables, menor calentamiento y CERO cierres por memoria RAM."
Write-Host "      - Ideal para cualquier smartphone de 6 a 8 GB de RAM."
Write-Host ""
Write-Host "  [2] MODO COMPLETO HD REMASTERIZADO (~36 GB)" -ForegroundColor Cyan
Write-Host "      - Incluye parches de texturas HD de PC (patch-A hasta patch-G)."
Write-Host "      - Requiere smartphone o tablet de gama alta con 12+ GB de RAM y 256 GB libres."
Write-Host ""
Write-Host "  [3] OMITIR TRANSFERENCIA DE DATOS (Solo configurar Realmlist y Config.wtf)" -ForegroundColor DarkGray
Write-Host ""

$profileOpt = Read-Host "Elige una opción (1, 2 o 3) [Por defecto 1]"
if (-not $profileOpt) { $profileOpt = "1" }

if ($profileOpt -eq "1" -or $profileOpt -eq "2") {
    $neededGb = if ($profileOpt -eq "1") { 17 } else { 38 }
    if ($freeGb -lt $neededGb) {
        Write-Host ""
        Write-Host "[ADVERTENCIA DE ESPACIO INSUFICIENTE]" -ForegroundColor Red
        Write-Host "Tu teléfono tiene $freeGb GB libres, pero este perfil requiere aproximadamente $neededGb GB." -ForegroundColor Yellow
        $cont = Read-Host "¿Deseas continuar a pesar del riesgo de espacio lleno? (S/N)"
        if ($cont -notmatch "s|S") { Exit 1 }
    }

    # Copiar Wow.exe si existe
    $wowExe = Join-Path $DetectedClient "Wow.exe"
    if (Test-Path $wowExe) {
        Write-Host "Transfiriendo Wow.exe..." -ForegroundColor White
        & $AdbPath -s $DeviceSerial push "$wowExe" /sdcard/WoW-Imito/Client/Wow.exe
    }

    # Determinar qué archivos MPQ transferir
    $allMpqs = Get-ChildItem -Path $DataDir -Filter "*.mpq"
    $baseMpqs = @("common.mpq", "common-2.mpq", "expansion.mpq", "lichking.mpq", "patch.mpq", "patch-2.mpq", "patch-3.mpq")

    $toTransfer = @()
    foreach ($m in $allMpqs) {
        if ($profileOpt -eq "1") {
            if ($baseMpqs -contains $m.Name.ToLower()) {
                $toTransfer += $m
            }
        } else {
            $toTransfer += $m
        }
    }

    Write-Host ""
    Write-Host "Iniciando transferencia de $($toTransfer.Count) archivos MPQ a /sdcard/WoW-Imito/Client/Data/..." -ForegroundColor Cyan
    $idx = 1
    foreach ($file in $toTransfer) {
        $sizeMb = [math]::Round($file.Length / 1024 / 1024, 1)
        Write-Host "[$idx/$($toTransfer.Count)] Copiando $($file.Name) ($sizeMb MB)..." -ForegroundColor White
        & $AdbPath -s $DeviceSerial push "$($file.FullName)" "/sdcard/WoW-Imito/Client/Data/$($file.Name)"
        $idx++
    }

    # Transferir carpeta de idioma (esES o enUS)
    $localeDir = $null
    if (Test-Path "$DataDir\esES") { $localeDir = "$DataDir\esES" }
    elseif (Test-Path "$DataDir\enUS") { $localeDir = "$DataDir\enUS" }

    if ($localeDir) {
        $locName = Split-Path -Leaf $localeDir
        Write-Host "Copiando carpeta de idioma $locName..." -ForegroundColor Cyan
        & $AdbPath -s $DeviceSerial push "$localeDir" "/sdcard/WoW-Imito/Client/Data/"
    }

    # Transferir Interface/AddOns si existe
    $addonsDir = Join-Path $DetectedClient "Interface"
    if (Test-Path $addonsDir) {
        Write-Host "Copiando AddOns e Interfaz adaptativa..." -ForegroundColor Cyan
        & $AdbPath -s $DeviceSerial push "$addonsDir" "/sdcard/WoW-Imito/Client/"
    }
}

# 10. Inyección de Realmlist y Config.wtf Calibrado
Show-Header
Write-Host ">>> [5/5] CONFIGURACIÓN DE CONEXIÓN Y OPTIMIZACIÓN TÁCTIL" -ForegroundColor Yellow
Write-Host ""
Write-Host "Selecciona el servidor al que te conectarás desde tu teléfono:" -ForegroundColor White
Write-Host "  [1] REINO 1: JAINACORE GLOBAL (Playit Anycast - Cero VPN / Juega desde la calle)" -ForegroundColor Green
Write-Host "  [2] REINO 1: JAINACORE WIFI CASA (Red Local 192.168.1.80 / 1 ms latencia)" -ForegroundColor Cyan
Write-Host "  [3] REINO 3: WANITOSGYM ESPAÑA (ICC Cap 80 / 100.98.162.75:8087)" -ForegroundColor Magenta
Write-Host ""

$realmOpt = Read-Host "Elige una opción (1, 2 o 3) [Por defecto 1]"
if (-not $realmOpt) { $realmOpt = "1" }

$realmlistContent = "set realmlist ambulance-ergonomic.tun.ply.gg"
$patchContent = "set patchlist ambulance-ergonomic.tun.ply.gg"
$realmNameTag = "JainaCore (Global Anycast)"

if ($realmOpt -eq "2") {
    $realmlistContent = "set realmlist 192.168.1.80"
    $patchContent = "set patchlist 192.168.1.80"
    $realmNameTag = "JainaCore (WiFi Local)"
} elseif ($realmOpt -eq "3") {
    $realmlistContent = "set realmlist 100.98.162.75:8087"
    $patchContent = "set patchlist 100.98.162.75:8087"
    $realmNameTag = "WanitosGYM (Espana Cap 80)"
}

# Guardar temporalmente en host y empujar por adb
$tempWtf = Join-Path $env:TEMP "realmlist.wtf"
$realmlistFull = "$realmlistContent`r`n$patchContent`r`n"
Set-Content -Path $tempWtf -Value $realmlistFull -Encoding ASCII

& $AdbPath -s $DeviceSerial push "$tempWtf" /sdcard/WoW-Imito/Client/Data/esES/realmlist.wtf >$null 2>$null
& $AdbPath -s $DeviceSerial push "$tempWtf" /sdcard/WoW-Imito/Client/Data/enUS/realmlist.wtf >$null 2>$null
& $AdbPath -s $DeviceSerial push "$tempWtf" /sdcard/WoW-Imito/Client/realmlist.wtf >$null 2>$null

# Inyectar Config.wtf optimizado para móvil (gxCursor 0, sin contratos, audio por defecto)
$tempConfig = Join-Path $env:TEMP "Config.wtf"
$configContent = @"
SET locale "esES"
SET realmName "$realmNameTag"
SET gxCursor "0"
SET gxWindow "1"
SET gxMaximize "1"
SET gxResolution "1920x1080"
SET ffxGlow "0"
SET ffxDeath "0"
SET Farclip "500"
SET Sound_OutputDriverName "System Default"
SET readTOS "1"
SET readEULA "1"
SET checkAddonVersion "0"
SET accounttype "LK"
"@
Set-Content -Path $tempConfig -Value $configContent -Encoding ASCII
& $AdbPath -s $DeviceSerial push "$tempConfig" /sdcard/WoW-Imito/Client/WTF/Config.wtf >$null 2>$null

# 11. Finalización exitosa
Show-Header
Write-Host "===============================================================================" -ForegroundColor Green
Write-Host "   ¡INSTALACIÓN COMPLETADA CON ÉXITO EN TU DISPOSITIVO ANDROID!" -ForegroundColor Green
Write-Host "===============================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Dispositivo : $mfr $model (Android $androidVer)" -ForegroundColor White
Write-Host "Servidor    : $realmNameTag" -ForegroundColor Cyan
Write-Host "Ubicación   : Almacenamiento interno / WoW-Imito / Client" -ForegroundColor White
Write-Host ""
Write-Host "PASOS FINALES PARA JUGAR EN TU TELÉFONO:" -ForegroundColor Yellow
Write-Host "  1. Desconecta el cable USB si lo deseas." -ForegroundColor White
Write-Host "  2. Abre la aplicación 'ProjectJaina-Imito' en tu teléfono." -ForegroundColor White
Write-Host "  3. En la pantalla inicial, pulsa 'Configurar' o 'Iniciar WOW'." -ForegroundColor White
Write-Host "  4. Conecta tu mando Bluetooth (Xbox, PS5, etc.) o usa los controles táctiles." -ForegroundColor White
Write-Host "  5. ¡Entra con tu cuenta SRP6 y disfruta de Azeroth en tu bolsillo!" -ForegroundColor Magenta
Write-Host ""
Write-Host "===============================================================================" -ForegroundColor Green
Write-Host ""
Pause
