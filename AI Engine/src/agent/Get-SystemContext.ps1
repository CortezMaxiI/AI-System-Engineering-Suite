<#
.SYNOPSIS
    Retrieves system context for the Optimax AI Engine.
    
.DESCRIPTION
    This script collects hardware and software information such as CPU, GPU, RAM, 
    Windows Version, Power Plan, and active processes.
    It outputs a JSON object to be consumed by the AI Engine.

.OUTPUTS
    JSON String containing system context.

.EXAMPLE
    .\Get-SystemContext.ps1
#>

$ErrorActionPreference = "Stop"

# Verify Administrator Privileges
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "This script requires Administrator privileges to access system telemetry."
    exit 1
}


function Get-SystemContext {
    try {
        # CPU Info
        $cpu = Get-CimInstance Win32_Processor | Select-Object -First 1 Name, NumberOfCores, MaxClockSpeed

        # RAM Info
        $osInfo = Get-CimInstance Win32_OperatingSystem
        $totalRamGB = [math]::Round($osInfo.TotalVisibleMemorySize / 1MB, 2)
        $freeRamGB = [math]::Round($osInfo.FreePhysicalMemory / 1MB, 2)

        # GPU Info (Taking the first one, usually discrete if present or integrated)
        $gpu = Get-CimInstance Win32_VideoController | Select-Object -First 1 Name, DriverVersion

        # Power Plan
        $powerPlan = "Unknown"
        try {
            $planObj = Get-CimInstance -Namespace root\cimv2\power -ClassName Win32_PowerPlan -Filter "IsActive=TRUE" -ErrorAction Stop
            $powerPlan = $planObj.ElementName
        }
        catch {
            Write-Warning "Could not retrieve Power Plan (Access Denied?). Using 'powercfg' fallback."
            try {
                $output = powercfg /getactivescheme 2>&1
                if ($output -match "\((.*)\)") {
                    $powerPlan = $Matches[1]
                }
            }
            catch {
                $powerPlan = "Unknown (Error)"
            }
        }

        # Windows Version
        $osVersion = $osInfo.Caption + " (" + $osInfo.Version + ")"

        # Active Heavy Processes (Top 5 by CPU)
        $processes = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, CPU, Id

        $context = [PSCustomObject]@{
            Timestamp    = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
            Hardware     = @{
                CPU              = $cpu.Name
                Cores            = $cpu.NumberOfCores
                MaxClockSpeedMHz = $cpu.MaxClockSpeed
                TotalRAM_GB      = $totalRamGB
                FreeRAM_GB       = $freeRamGB
                GPU              = $gpu.Name
            }
            Software     = @{
                OS        = $osVersion.Trim()
                PowerPlan = $powerPlan
            }
            TopProcesses = $processes
        }

        return $context | ConvertTo-Json -Depth 3
    }
    catch {
        Write-Error "Failed to gather system context: $_"
        exit 1
    }
}

Get-SystemContext
