---
name: feature-miner
description: Extract reusable product/app feature patterns from harvested trend data into structured development notes (capabilities, UX patterns, monetization hints, integration points).
---

# Feature Miner

Use this skill after raw trend data is collected.

## Goal

Convert noisy feed entries into development-ready feature signals.

## Input

- `/root/.openclaw/workspace/data/harvest/latest.json`

## Output

- `/root/.openclaw/workspace/data/harvest/feature_patterns.json`

## Extraction schema

Each pattern should include:

- `name`: concise feature name
- `sourceTitle`: original item title
- `sourceUrl`: canonical URL
- `coreValue`: solved user problem
- `uxPattern`: interaction model
- `techHint`: stack/integration clue
- `monetizationHint`: likely pricing or GTM angle
- `priority`: P0/P1/P2

## Workflow

1. Read latest harvest file.
2. Keep only dev-relevant records (tools, APIs, automation, agent workflows).
3. Deduplicate by product and feature intent.
4. Write normalized JSON output.

## Rule

No speculative hype text. Keep concise, builder-oriented language.
