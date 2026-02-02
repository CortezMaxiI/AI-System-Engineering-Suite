# ══════════════════════════════════════════════════════════════════════════════
# SENTINEL-IIOT: Predictive Lumi Engine Launcher
# Industrial Automation Startup Script
# ══════════════════════════════════════════════════════════════════════════════

Clear-Host

# Setup Lumi Branding Color (Violet-ish)
$LumiViolet = "#A16EFF"

Write-Host "
   ____  _____ _   _ _____ ___ _   _ _____ _     
  / ___|| ____| \ | |_   _|_ _| \ | | ____| |    
  \___ \|  _| |  \| | | |  | ||  \| |  _| | |    
   ___) | |___| |\  | | |  | || |\  | |___| |___ 
  |____/|_____|_| \_| |_| |___|_| \_|_____|_____|
   ___ ___ ___ _____ 
  |_ _|_ _/ _ \_   _|
   | | | | | | || |  
   | | | | |_| || |  
  |___|___\___/ |_|  
" -ForegroundColor Magenta

Write-Host ">>> Iniciando enlace neuronal... Ready for monitoring." -ForegroundColor Gray
Write-Host "────────────────────────────────────────────────────────" -ForegroundColor DarkGray

# 1. Verification of Environment
Write-Host "[CHECK] Verificando dependencias..." -NoNewline
if ((Get-Command dotnet -ErrorAction SilentlyContinue) -and (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host " OK" -ForegroundColor Green
} else {
    Write-Host " FAILED" -ForegroundColor Red
    Write-Host "Error: Se requiere .NET 8 SDK y Python 3.11+ instalados en el PATH."
    Exit
}

# 2. Orquestación de Módulos

# Módulo 1: THE MUSCLE (C#)
Write-Host "[LAUNCH] Desplegando THE MUSCLE (Telemetry Core)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Sentinel-Muscle-CS; `$Host.UI.RawUI.WindowTitle = 'SENTINEL | THE MUSCLE'; dotnet run"

# Delay para asegurar que el socket PUB de ZeroMQ esté listo
Write-Host "[WAIT] Estabilizando sockets de ZeroMQ (5s)..." -ForegroundColor DarkGray
Start-Sleep -Seconds 5

# Módulo 2: THE BRAIN (Python)
Write-Host "[LAUNCH] Desplegando THE BRAIN (AI Engine)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Sentinel-Brain-PY; `$Host.UI.RawUI.WindowTitle = 'SENTINEL | THE BRAIN'; python main.py"

Start-Sleep -Seconds 2

# Módulo 3: THE HUD (UI)
Write-Host "[LAUNCH] Desplegando THE HUD (Lumi View)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd Sentinel-UI-WPF; `$Host.UI.RawUI.WindowTitle = 'SENTINEL | THE HUD'; dotnet run"

Write-Host "────────────────────────────────────────────────────────" -ForegroundColor DarkGray
Write-Host "SISTEMA SENTINEL TOTALMENTE OPERATIVO." -ForegroundColor Green
Start-Sleep -Seconds 3
