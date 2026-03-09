#!/usr/bin/env bash
set -euo pipefail

LOG="/var/log/oc-watchdog.log"
ts(){ date '+%F %T'; }

# OpenClaw gateway probe
if ! curl -fsS --max-time 3 http://127.0.0.1:18789/ >/dev/null 2>&1; then
  echo "$(ts) gateway unhealthy -> restart" >> "$LOG"
  openclaw gateway restart >> "$LOG" 2>&1 || true
fi

# nginx
if ! systemctl is-active --quiet nginx; then
  echo "$(ts) nginx inactive -> restart" >> "$LOG"
  systemctl restart nginx >> "$LOG" 2>&1 || true
fi

# sing-box
if ! systemctl is-active --quiet sing-box; then
  echo "$(ts) sing-box inactive -> restart" >> "$LOG"
  systemctl restart sing-box >> "$LOG" 2>&1 || true
fi
