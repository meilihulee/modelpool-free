#!/usr/bin/env bash
set -euo pipefail

WORK="/tmp/openclaw-install"
mkdir -p "$WORK"
LOG="$WORK/install.log"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$1" | tee -a "$LOG"
}

has() { command -v "$1" >/dev/null 2>&1; }

ensure_node() {
  if has node; then
    log "Node exists: $(node -v)"
    return
  fi

  if has brew; then
    log 'Installing node via Homebrew...'
    brew install node
  else
    log 'Homebrew not found. Installing Homebrew...'
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv || /usr/local/bin/brew shellenv)"
    brew install node
  fi
}

ensure_user_npm_prefix() {
  local npm_prefix
  npm_prefix="$(npm config get prefix 2>/dev/null || true)"
  if [[ "$npm_prefix" == "/usr/local" || "$npm_prefix" == "/opt/homebrew" ]]; then
    mkdir -p "$HOME/.npm-global"
    npm config set prefix "$HOME/.npm-global"
  fi

  if [[ ":$PATH:" != *":$HOME/.npm-global/bin:"* ]]; then
    export PATH="$HOME/.npm-global/bin:$PATH"
    if [[ -f "$HOME/.zshrc" ]]; then
      grep -q 'npm-global/bin' "$HOME/.zshrc" || echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> "$HOME/.zshrc"
    fi
    if [[ -f "$HOME/.bashrc" ]]; then
      grep -q 'npm-global/bin' "$HOME/.bashrc" || echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> "$HOME/.bashrc"
    fi
  fi
}

log 'Starting OpenClaw macOS install...'
ensure_node
ensure_user_npm_prefix

log "Node version: $(node -v)"
log "npm version: $(npm -v)"

log 'Installing OpenClaw globally...'
npm install -g @openclaw/openclaw

log 'Running OpenClaw doctor...'
openclaw doctor --non-interactive | tee "$WORK/doctor_after_install.log"

log 'Install finished.'
