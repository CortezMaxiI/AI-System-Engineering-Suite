@echo off
TITLE SENTINEL-IIOT BOOTLOADER
:: Ejecuta el script de PowerShell saltándose la política de ejecución local
powershell -ExecutionPolicy Bypass -File "%~dp0Sentinel-Launcher.ps1"
pause
