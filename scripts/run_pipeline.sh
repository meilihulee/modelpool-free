#!/usr/bin/env bash
set -euo pipefail

BASE="/root/.openclaw/workspace"

python3 "$BASE/scripts/harvest_trends.py"
python3 "$BASE/scripts/mine_features.py"
python3 "$BASE/scripts/rank_ideas.py"

echo "DONE"
echo "- $BASE/data/harvest/latest.json"
echo "- $BASE/data/harvest/feature_patterns.json"
echo "- $BASE/data/harvest/skills_ideas.json"
echo "- $BASE/data/harvest/apps_ideas.json"
