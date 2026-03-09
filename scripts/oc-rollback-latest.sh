#!/usr/bin/env bash
set -euo pipefail

LATEST_FILE="/root/.openclaw/backups/latest"
if [[ ! -f "$LATEST_FILE" ]]; then
  echo "no backup marker found: $LATEST_FILE"
  exit 1
fi

SRC="$(cat "$LATEST_FILE")"
if [[ ! -d "$SRC" ]]; then
  echo "backup path not found: $SRC"
  exit 1
fi

cp -a "$SRC/openclaw.json" /root/.openclaw/openclaw.json
cp -a "$SRC/nginx-sites-available"/* /etc/nginx/sites-available/
cp -a "$SRC/nginx-sites-enabled"/* /etc/nginx/sites-enabled/
rm -rf /etc/sing-box
cp -a "$SRC/sing-box" /etc/sing-box
rm -rf /var/www/leehub
cp -a "$SRC/leehub-www" /var/www/leehub

/usr/sbin/nginx -t
systemctl restart nginx
systemctl restart sing-box || true
openclaw gateway restart

echo "rollback done from: $SRC"
