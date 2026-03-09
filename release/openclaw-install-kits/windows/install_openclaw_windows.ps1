$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$Work = Join-Path $env:TEMP 'openclaw-install'
New-Item -ItemType Directory -Path $Work -Force | Out-Null
$Log = Join-Path $Work 'install.log'

function Write-Log([string]$msg) {
  $line = "[$(Get-Date -Format s)] $msg"
  Write-Host $line
  Add-Content -Path $Log -Value $line
}

function Test-Cmd([string]$name) {
  return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

function Ensure-Node {
  if (Test-Cmd 'node') {
    Write-Log "Node exists: $(node -v)"
    return
  }

  if (Test-Cmd 'winget') {
    Write-Log 'Installing Node.js LTS via winget...'
    winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements --silent
  } elseif (Test-Cmd 'choco') {
    Write-Log 'Installing Node.js LTS via choco...'
    choco install nodejs-lts -y
  } else {
    throw 'Node.js not found and neither winget nor choco is available. Install Node.js LTS manually from https://nodejs.org/'
  }
}

function Ensure-NpmPath {
  $npmGlobal = npm prefix -g
  if (-not $npmGlobal) { return }
  $npmBin = Join-Path $npmGlobal ''
  if ($env:Path -notlike "*$npmBin*") {
    $newPath = "$env:Path;$npmBin"
    [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
    $env:Path = $newPath
    Write-Log "Updated user PATH with $npmBin"
  }
}

Write-Log 'Starting OpenClaw Windows install...'
Ensure-Node
Write-Log "Node version: $(node -v)"
Write-Log "npm version: $(npm -v)"

Write-Log 'Installing OpenClaw globally...'
npm install -g @openclaw/openclaw
Ensure-NpmPath

Write-Log 'Running OpenClaw doctor...'
openclaw doctor --non-interactive | Tee-Object -FilePath (Join-Path $Work 'doctor_after_install.log')

Write-Log 'Install finished.'
exit 0
