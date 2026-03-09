#!/usr/bin/env bash
set -euo pipefail

WORK="/tmp/openclaw-install"
mkdir -p "$WORK"
LOG="$WORK/install.log"

log() { printf '[%s] %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$1" | tee -a "$LOG"; }
has() { command -v "$1" >/dev/null 2>&1; }

need_root() {
  if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
    if has sudo; then
      SUDO='sudo'
    else
      echo 'Run as root or install sudo.' >&2
      exit 1
    fi
  else
    SUDO=''
  fi
}

install_base_tools() {
  if has apt-get; then
    $SUDO apt-get update -y
    $SUDO apt-get install -y curl ca-certificates gnupg
  elif has dnf; then
    $SUDO dnf install -y curl ca-certificates
  elif has yum; then
    $SUDO yum install -y curl ca-certificates
  else
    echo 'Unsupported package manager. Require apt/dnf/yum.' >&2
    exit 1
  fi
}

install_node() {
  if has node; then
    log "Node exists: $(node -v)"
    return
  fi

  if has apt-get; then
    log 'Installing Node.js LTS via NodeSource...'
    curl -fsSL https://deb.nodesource.com/setup_lts.x | $SUDO bash -
    $SUDO apt-get install -y nodejs
  elif has dnf; then
    log 'Installing Node.js LTS via NodeSource...'
    curl -fsSL https://rpm.nodesource.com/setup_lts.x | $SUDO bash -
    $SUDO dnf install -y nodejs
  elif has yum; then
    log 'Installing Node.js LTS via NodeSource...'
    curl -fsSL https://rpm.nodesource.com/setup_lts.x | $SUDO bash -
    $SUDO yum install -y nodejs
  fi
}

log 'Starting OpenClaw Linux server install...'
need_root
install_base_tools
install_node

log "Node version: $(node -v)"
log "npm version: $(npm -v)"

log 'Installing OpenClaw globally...'
$SUDO npm install -g @openclaw/openclaw

log 'Running OpenClaw doctor...'
openclaw doctor --non-interactive | tee "$WORK/doctor_after_install.log"

log 'Install finished.'
