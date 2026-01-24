<#
.SYNOPSIS
    Base Idempotency Script for Lumi: Architect.
    Demonstrates the "Discovery Phase" to avoid redundant operations.
#>

function Test-SoftwareInstalled {
    param([string]$Command)
    try {
        $null = Invoke-Expression "$Command" -ErrorAction SilentlyContinue
        return ($LASTEXITCODE -eq 0)
    } catch {
        return $false
    }
}

function Install-Software {
    param(
        [string]$Name,
        [string]$CheckCmd,
        [string]$InstallCmd
    )

    Write-Host "--- Checking $Name ---" -ForegroundColor Cyan
    
    # 1. Discovery Phase
    if (Test-SoftwareInstalled -Command $CheckCmd) {
        Write-Host "[SKIP] $Name is already installed. No action needed." -ForegroundColor Yellow
        return
    }

    # 2. Execution Phase
    Write-Host "[FORGE] $Name not found. Starting installation..." -ForegroundColor Blue
    Write-Host "Running: $InstallCmd" -ForegroundColor Gray
    
    # Simulation of installation
    # Invoke-Expression $InstallCmd
    
    Write-Host "[SUCCESS] $Name installed successfully." -ForegroundColor Green
}

# Example Usage
Install-Software -Name "Git" -CheckCmd "git --version" -InstallCmd "winget install --id Git.Git -e --silent"
Install-Software -Name "Node.js" -CheckCmd "node --version" -InstallCmd "winget install --id OpenJS.NodeJS -e --silent"
