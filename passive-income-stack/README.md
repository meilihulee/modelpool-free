# Passive Income Stack (RapidAPI + Apify starter)

## Services
- extract-api: GET /extract?url=...
- screenshot-api: GET /shot?url=...&fullPage=true&width=1280&height=720

## Quick start

```bash
cd /root/.openclaw/workspace/passive-income-stack/extract-api
npm install

cd /root/.openclaw/workspace/passive-income-stack/screenshot-api
npm install
npx playwright install chromium

npm i -g pm2
pm2 start /root/.openclaw/workspace/passive-income-stack/deploy/ecosystem.config.cjs
pm2 save
```

## Health checks

```bash
curl http://127.0.0.1:3001/health
curl http://127.0.0.1:3002/health
```

## RapidAPI listing fields

### 1) Article Extractor API
- Base URL: `https://YOUR_DOMAIN/extract`
- Endpoint: `GET /extract?url=https://example.com/post`
- Header: `x-api-key: <key>` (if self-host auth enabled)

### 2) Website Screenshot API
- Base URL: `https://YOUR_DOMAIN/screenshot`
- Endpoint: `GET /shot?url=https://example.com&fullPage=true&width=1280&height=720`
- Header: `x-api-key: <key>`

## Suggested pricing (start)
- Free: low quota
- Basic: $5-$7/month
- Pro: $15-$19/month

## Apify actor idea
- Name: webpage-change-monitor
- Input: URL + CSS selector + keyword + webhook
- Output: changed/no-change + diff summary
