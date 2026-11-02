$tokens = $null
$errors = $null
$ast = [System.Management.Automation.Language.Parser]::ParseFile("E:\ProjectJaina_Lab\ProjectJaina-Imito\tools\scripts\Install-ProjectJaina-Android.ps1", [ref]$tokens, [ref]$errors)

if ($errors.Count -gt 0) {
    Write-Host "SE ENCONTRARON $($errors.Count) ERRORES DE SINTAXIS:" -ForegroundColor Red
    foreach ($err in $errors) {
        Write-Host "Línea $($err.Extent.StartLineNumber): $($err.Message)" -ForegroundColor Yellow
    }
    exit 1
} else {
    Write-Host "SINTAXIS 100% VALIDA Y COMPILADA SIN ERRORES" -ForegroundColor Green
    exit 0
}
