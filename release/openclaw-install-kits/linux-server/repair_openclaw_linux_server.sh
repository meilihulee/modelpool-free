#!/usr/bin/env bash
set -euo pipefail

WORK="/tmp/openclaw-install"
mkdir -p "$WORK"
LOG="$WORK/repair.log"

log() { printf '[%s] %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$1" | tee -a "$LOG"; }
has() { command -v "$1" >/dev/null 2>&1; }

if [[ ${EUID:-$(id -u)} -ne 0 ]]; then
  if has sudo; then SUDO='sudo'; else echo 'Run as root or install sudo.' >&2; exit 1; fi
else
  SUDO=''
fi

log 'Starting OpenClaw repair...'
log 'Cleaning npm cache...'
npm cache clean --force || true

log 'Reinstalling OpenClaw...'
$SUDO npm uninstall -g @openclaw/openclaw || true
$SUDO npm install -g @openclaw/openclaw

log 'Trying gateway restart (best effort)...'
openclaw gateway restart || true

log 'Re-running doctor and health...'
openclaw doctor --non-interactive | tee "$WORK/doctor_after_repair.log"
openclaw health --json | tee "$WORK/health_after_repair.json"

log 'Repair complete.'
