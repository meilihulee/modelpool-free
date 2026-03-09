#!/usr/bin/env bash
set -euo pipefail

URL1="https://leehub.xyz/"
URL2="https://api.leehub.xyz/api/resources"
ROOT="/root/.openclaw/workspace/ops-stack"
LOG_DIR="$ROOT/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/watchdog.log"

check_url() {
  local url="$1"
  local code
  code=$(curl -m 12 -s -o /dev/null -w '%{http_code}' "$url" || echo 000)
  [[ "$code" == "200" ]]
}

now() { date '+%Y-%m-%d %H:%M:%S'; }

echo "[$(now)] watchdog tick" >> "$LOG"
ok1=0; ok2=0
if check_url "$URL1"; then ok1=1; fi
if check_url "$URL2"; then ok2=1; fi

echo "[$(now)] status leehub=$ok1 api=$ok2" >> "$LOG"

if [[ $ok1 -eq 1 && $ok2 -eq 1 ]]; then
  exit 0
fi

echo "[$(now)] unhealthy -> restarting stack" >> "$LOG"
cd "$ROOT"
docker compose restart n8n metabase uptime-kuma >> "$LOG" 2>&1 || true
sleep 8

ok1=0; ok2=0
if check_url "$URL1"; then ok1=1; fi
if check_url "$URL2"; then ok2=1; fi
echo "[$(now)] post-restart leehub=$ok1 api=$ok2" >> "$LOG"

exit 0
