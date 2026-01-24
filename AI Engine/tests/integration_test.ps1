<#
.SYNOPSIS
    Integration test for Optimax AI Engine.
    
.DESCRIPTION
    Simulates the full pipeline:
    1. Measure Baseline Performance
    2. Gather System Context
    3. Request AI Decision
    4. Execute Plan
    5. Measure Post-Optimization Performance
    6. Generate Comparison Report
#>

param(
    [switch]$Demo
)

$ErrorActionPreference = "Stop"
$Root = "$PSScriptRoot\.."
$Src = "$Root\src"
$ContextFile = "$Src\data\context_test.json"
$ReportFile = "$Src\data\metrics\last_report.json"

Write-Host "--- [OPTIMAX] Starting Full Optimization Cycle ---" -ForegroundColor Cyan

# 0. Check Privileges
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "[-] ERROR: Administrator privileges required." -ForegroundColor Red
    exit 1
}

# 1. Measure Baseline
Write-Host "[1/6] Measuring Baseline Performance..." -ForegroundColor Yellow
$baselineRaw = & "$Src\agent\Measure-Performance.ps1"
$baseline = $baselineRaw | ConvertFrom-Json
Write-Host "    -> CPU: $($baseline.Metrics.AvgCpuLoad_Percent)% | RAM Available: $($baseline.Metrics.AvailableMemory_MB) MB"

# 2. Gather Context
Write-Host "[2/6] Gathering System Context..." -ForegroundColor Yellow
$contextJson = & "$Src\agent\Get-SystemContext.ps1"
$contextJson | Out-File -FilePath $ContextFile -Encoding utf8

# 3. Call AI Engine (main.py at root)
Write-Host "[3/6] Requesting AI Decision..." -ForegroundColor Yellow
$engineArgs = @("--context", $ContextFile, "--json")
if ($PSBoundParameters.ContainsKey('Demo')) { $engineArgs += "--demo" }

$engineOutput = python "$Root\main.py" @engineArgs
if (-not $engineOutput) { Write-Error "Engine returned no output."; exit 1 }

$plan = $engineOutput | ConvertFrom-Json

Write-Host "    -> Strategy: $($plan.strategy)" -ForegroundColor Cyan
Write-Host "    -> Reasoning: $($plan.reasoning)" -ForegroundColor Gray

# 4. Execute Plan
Write-Host "[4/6] Executing Plan..." -ForegroundColor Yellow
$decisionId = $plan.meta.decision_id

foreach ($action in $plan.plan) {
    Write-Host "    -> Running: $($action.id) ($($action.description))" -ForegroundColor Magenta
    $invokeArgs = @{
        ScriptBlockContent = $action.content
        ActionId           = $action.id
        DecisionId         = $decisionId
    }
    if ($plan.meta.demo_mode) { $invokeArgs["DemoMode"] = $true }
    & "$Src\agent\Invoke-Optimization.ps1" @invokeArgs
}

# 5. Measure Post-Optimization
Write-Host "[5/6] Measuring Post-Optimization Performance..." -ForegroundColor Yellow
Start-Sleep -Seconds 2 # Allow system to settle
$postRaw = & "$Src\agent\Measure-Performance.ps1"
$post = $postRaw | ConvertFrom-Json
Write-Host "    -> CPU: $($post.Metrics.AvgCpuLoad_Percent)% | RAM Available: $($post.Metrics.AvailableMemory_MB) MB"

# 6. Generate Comparison Report
Write-Host "[6/6] Generating Comparison Report..." -ForegroundColor Yellow
$report = [PSCustomObject]@{
    Timestamp  = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    DecisionId = $decisionId
    Before     = $baseline.Metrics
    After      = $post.Metrics
    Diff       = @{
        CpuUsageDelta           = $post.Metrics.AvgCpuLoad_Percent - $baseline.Metrics.AvgCpuLoad_Percent
        MemoryAvailableDelta_MB = $post.Metrics.AvailableMemory_MB - $baseline.Metrics.AvailableMemory_MB
    }
    Strategy   = $plan.strategy
}

$report | ConvertTo-Json | Out-File -FilePath $ReportFile -Encoding utf8
Write-Host "[+] SUCCESS: Report generated at $ReportFile" -ForegroundColor Green
Write-Host "--- [OPTIMAX] Cycle Completed ---" -ForegroundColor Cyan
