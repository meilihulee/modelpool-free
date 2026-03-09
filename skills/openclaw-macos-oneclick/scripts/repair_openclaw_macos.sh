#!/usr/bin/env bash
set -euo pipefail

WORK="/tmp/openclaw-install"
mkdir -p "$WORK"
LOG="$WORK/repair.log"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$1" | tee -a "$LOG"
}

log 'Starting OpenClaw repair...'
log 'Cleaning npm cache...'
npm cache clean --force || true

log 'Reinstalling OpenClaw...'
npm uninstall -g @openclaw/openclaw || true
npm install -g @openclaw/openclaw

log 'Trying gateway restart (best effort)...'
openclaw gateway restart || true

log 'Re-running doctor...'
openclaw doctor --non-interactive | tee "$WORK/doctor_after_repair.log"

log 'Repair complete.'
