$ErrorActionPreference = 'Continue'
$Work = Join-Path $env:TEMP 'openclaw-install'
New-Item -ItemType Directory -Path $Work -Force | Out-Null
$Log = Join-Path $Work 'repair.log'

function Log([string]$m) {
  $line = "[$(Get-Date -Format s)] $m"
  Write-Host $line
  Add-Content -Path $Log -Value $line
}

Log 'Starting OpenClaw repair...'

Log 'Cleaning npm cache...'
npm cache clean --force

Log 'Removing and reinstalling OpenClaw package...'
npm uninstall -g @openclaw/openclaw | Out-Null
npm install -g @openclaw/openclaw

Log 'Trying gateway restart (best effort)...'
openclaw gateway restart | Out-Null

Log 'Re-running doctor...'
openclaw doctor --non-interactive | Tee-Object -FilePath (Join-Path $Work 'doctor_after_repair.log')

Log 'Repair complete.'
exit 0
