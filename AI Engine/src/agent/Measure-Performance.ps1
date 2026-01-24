<#
.SYNOPSIS
    Measures current system performance metrics.
    
.DESCRIPTION
    Captures baseline metrics to quantify optimization impact.
    Currently measures: CPU Load, RAM Usage. 
    (Future: Frametime/FPS integration via external tools/overlays if scope allows).

.OUTPUTS
    JSON String containing performance metrics.
#>

$ErrorActionPreference = "Stop"

function Measure-Performance {
    param (
        [int]$DurationSeconds = 3
    )

    try {
        # CPU Load (Snapshot)
        # Using WMI to be language agnostic (Get-Counter depends on localized strings)
        $cpuInfo = Get-CimInstance Win32_Processor | Select-Object -ExpandProperty LoadPercentage
        $avgCpu = $cpuInfo

        # Memory Available
        $osInfo = Get-CimInstance Win32_OperatingSystem
        $availMem = [math]::Round($osInfo.FreePhysicalMemory / 1KB, 0) # FreePhysicalMemory is in KB already? No, it's in KB. 1MB = 1024KB.
        # Win32_OperatingSystem.FreePhysicalMemory is in Kilobytes.
        $availMemMB = [math]::Round($osInfo.FreePhysicalMemory / 1024, 0)

        # Mockup for Latency (DPC Latency requires kernel drivers, simulating or using basic ping for network latency as placeholder if needed, 
        # but for now we stick to resource usage as primary proxy for 'load')
        
        $metrics = [PSCustomObject]@{
            Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
            Metrics   = @{
                AvgCpuLoad_Percent = [math]::Round($avgCpu, 2)
                AvailableMemory_MB = $availMemMB
            }
        }

        return $metrics | ConvertTo-Json
    }
    catch {
        Write-Error "Failed to measure performance: $_"
        exit 1
    }
}

Measure-Performance
