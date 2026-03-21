---
name: idea-ranker
description: Rank and convert mined feature signals into executable Skill ideas and App ideas with priority, effort, moat, and MVP scope.
---

# Idea Ranker

Use this skill to create build queues from mined signals.

## Inputs

- `/root/.openclaw/workspace/data/harvest/feature_patterns.json`

## Outputs

- `/root/.openclaw/workspace/data/harvest/skills_ideas.json`
- `/root/.openclaw/workspace/data/harvest/apps_ideas.json`

## Ranking dimensions

- `impact` (1-5)
- `effort` (1-5)
- `speedToMVP` (hours/days)
- `moat` (Low/Medium/High)
- `priority` (P0/P1/P2)

## Required fields per idea

- `title`
- `type` (skill/app)
- `oneLiner`
- `targetUser`
- `coreFeatures` (3-5)
- `integration` (APIs/tools)
- `mvpPlan` (step list)
- `rankReason`

## Rule

Default output should include at least:

- 10 skill ideas
- 10 app ideas

If data is thin, output fewer but with explicit confidence notes.
