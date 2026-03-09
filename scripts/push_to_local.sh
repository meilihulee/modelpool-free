#!/usr/bin/env bash
set -euo pipefail

# Usage:
# LOCAL_HOST=0.tcp.jp.ngrok.io LOCAL_PORT=18436 LOCAL_USER=Administrator LOCAL_PASS='xxx' \
#   ./scripts/push_to_local.sh /path/to/file [remote_subdir]

SRC="${1:-}"
SUBDIR="${2:-incoming_from_cloud}"

: "${LOCAL_HOST:?LOCAL_HOST required}"
: "${LOCAL_PORT:?LOCAL_PORT required}"
: "${LOCAL_USER:?LOCAL_USER required}"
: "${LOCAL_PASS:?LOCAL_PASS required}"

if [[ -z "$SRC" || ! -e "$SRC" ]]; then
  echo "source file missing: $SRC" >&2
  exit 1
fi

sshpass -p "$LOCAL_PASS" ssh -o StrictHostKeyChecking=no -p "$LOCAL_PORT" "$LOCAL_USER@$LOCAL_HOST" \
  "powershell -NoProfile -Command \"New-Item -ItemType Directory -Force -Path \$env:USERPROFILE\\$SUBDIR | Out-Null\""

sshpass -p "$LOCAL_PASS" scp -P "$LOCAL_PORT" -o StrictHostKeyChecking=no "$SRC" "$LOCAL_USER@$LOCAL_HOST:$SUBDIR/"

echo "uploaded: $SRC -> $LOCAL_USER@$LOCAL_HOST:$SUBDIR/"
