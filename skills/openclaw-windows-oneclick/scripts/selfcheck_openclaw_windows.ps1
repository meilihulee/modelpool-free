$ErrorActionPreference = 'Stop'
$Work = Join-Path $env:TEMP 'openclaw-install'
New-Item -ItemType Directory -Path $Work -Force | Out-Null
$Out = Join-Path $Work 'selfcheck.json'

function Check([string]$name, [scriptblock]$test) {
  try {
    $ok = & $test
    return @{ name = $name; ok = [bool]$ok; error = $null }
  } catch {
    return @{ name = $name; ok = $false; error = $_.Exception.Message }
  }
}

$checks = @()
$checks += Check 'node' { Get-Command node -ErrorAction Stop | Out-Null; $true }
$checks += Check 'npm' { Get-Command npm -ErrorAction Stop | Out-Null; $true }
$checks += Check 'openclaw' { Get-Command openclaw -ErrorAction Stop | Out-Null; $true }
$checks += Check 'openclaw-status' { openclaw status | Out-Null; $true }
$checks += Check 'openclaw-doctor' { openclaw doctor --non-interactive | Out-Null; $true }

$failed = @($checks | Where-Object { -not $_.ok })
$result = @{
  timestamp = (Get-Date).ToString('s')
  checks = $checks
  healthy = ($failed.Count -eq 0)
}

$result | ConvertTo-Json -Depth 5 | Set-Content -Path $Out -Encoding UTF8
Write-Host ($result | ConvertTo-Json -Depth 5)

if ($failed.Count -eq 0) { exit 0 } else { exit 1 }
