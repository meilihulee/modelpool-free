---
name: trend-harvester
description: Continuous low-token trend collection from GitHub Trending, Hacker News, Product Hunt, and RSS sources into local JSON/JSONL files. Use when the user wants always-on discovery with minimal model usage.
---

# Trend Harvester

Use this skill for long-running, low-token data collection.

## What it does

- Pulls trend/news feeds from public sources
- Stores normalized records to local files
- Runs in loop mode (e.g., every 30 minutes)
- Avoids LLM-heavy summarization by default

## Run once

```bash
python3 /root/.openclaw/workspace/scripts/harvest_trends.py
```

## Run continuously

```bash
nohup bash -lc 'while true; do python3 /root/.openclaw/workspace/scripts/harvest_trends.py >> /root/.openclaw/workspace/logs/harvest.log 2>&1; sleep 1800; done' >/root/.openclaw/workspace/logs/harvest.nohup.out 2>&1 &
```

## Output files

- `/root/.openclaw/workspace/data/harvest/latest.json`
- `/root/.openclaw/workspace/data/harvest/stream.jsonl`
- `/root/.openclaw/workspace/data/harvest/heartbeat.txt`
- `/root/.openclaw/workspace/logs/harvest.log`

## Operator rules

- Prefer bandwidth over token usage
- Keep raw data first, summarize later on demand
- Validate JSON before downstream usage
