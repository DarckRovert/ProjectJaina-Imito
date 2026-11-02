@echo off
setlocal
title Project Jaina - Instalador Automatizado para Android (ARM64)
color 0B

echo ===============================================================================
echo   PROJECT JAINA: ASISTENTE DE INSTALACION EN SMARTPHONES Y TABLETS ANDROID
echo ===============================================================================
echo.
echo Iniciando el asistente con soporte nativo PowerShell y ADB embebido...
echo.

set "SCRIPT_DIR=%~dp0"
set "PS_SCRIPT=%SCRIPT_DIR%tools\scripts\Install-ProjectJaina-Android.ps1"

if not exist "%PS_SCRIPT%" (
    echo [ERROR] No se encontro el script de instalacion en:
    echo %PS_SCRIPT%
    echo.
    pause
    exit /b 1
)

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%PS_SCRIPT%"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [AVISO] El instalador finalizo con codigo: %ERRORLEVEL%
    pause
)

exit /b %ERRORLEVEL%
