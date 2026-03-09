# Website Ops Maintenance (n8n + Kuma + Metabase)

## Current automation (already enabled)

- Script: `scripts/ops_watchdog.sh`
- Schedule: every 5 minutes via crontab
- Targets:
  - `https://leehub.xyz/`
  - `https://api.leehub.xyz/api/resources`
- Behavior:
  1. Check both URLs (HTTP 200 expected)
  2. If either fails, restart `n8n metabase uptime-kuma`
  3. Re-check and write result to `ops-stack/logs/watchdog.log`

## n8n workflow template

- File: `ops-stack/workflows/website-maintenance-n8n.json`
- Purpose: import into n8n UI as a visual workflow (schedule + checks + restart)
- Note: CLI import may fail on some sqlite schema variants. Use n8n UI import when needed.

## Kuma baseline monitors (manual in UI)

Add 2 HTTP monitors in Kuma:

1. Name: `leehub-home`
   - URL: `https://leehub.xyz/`
   - Interval: 60s
   - Retries: 3
2. Name: `leehub-api`
   - URL: `https://api.leehub.xyz/api/resources`
   - Interval: 60s
   - Retries: 3

## Metabase baseline dashboard

Recommended cards:
- Uptime rate (24h / 7d)
- Avg response time
- Incident count
- Recovery duration

Data source can be watchdog logs (later ETL) or Kuma exports.
