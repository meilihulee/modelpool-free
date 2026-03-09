#!/usr/bin/env bash
set -euo pipefail

TS="$(date +%Y%m%d-%H%M%S)"
OUT_DIR="/root/.openclaw/backups/${TS}"
mkdir -p "$OUT_DIR"

cp -a /root/.openclaw/openclaw.json "$OUT_DIR/openclaw.json"
cp -a /etc/nginx/sites-available "$OUT_DIR/nginx-sites-available"
cp -a /etc/nginx/sites-enabled "$OUT_DIR/nginx-sites-enabled"
cp -a /etc/sing-box "$OUT_DIR/sing-box"
cp -a /var/www/leehub "$OUT_DIR/leehub-www"

echo "$OUT_DIR" > /root/.openclaw/backups/latest
printf 'backup saved: %s\n' "$OUT_DIR"
