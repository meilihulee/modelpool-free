#!/usr/bin/env bash
set -euo pipefail

WORK="/tmp/openclaw-install"
mkdir -p "$WORK"
OUT="$WORK/selfcheck.json"

check() {
  local name="$1"; shift
  if "$@" >/dev/null 2>&1; then
    printf '{"name":"%s","ok":true,"error":null}' "$name"
  else
    printf '{"name":"%s","ok":false,"error":"check_failed"}' "$name"
  fi
}

c1=$(check node command -v node)
c2=$(check npm command -v npm)
c3=$(check openclaw command -v openclaw)
c4=$(check openclaw-status openclaw status)
c5=$(check openclaw-doctor openclaw doctor --non-interactive)
c6=$(check openclaw-health openclaw health --json)

json="[$c1,$c2,$c3,$c4,$c5,$c6]"
if echo "$json" | grep -q '"ok":false'; then
  healthy=false
  code=1
else
  healthy=true
  code=0
fi

printf '{"timestamp":"%s","healthy":%s,"checks":%s}\n' "$(date '+%Y-%m-%dT%H:%M:%S')" "$healthy" "$json" | tee "$OUT"
exit "$code"
