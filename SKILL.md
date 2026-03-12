---
name: modelpool
description: Free AI model manager for OpenClaw. Auto-discovers free models from OpenRouter, configures multi-key rotation for doubled free quota, builds smart fallback chains, and includes one-click repair for model issues.
license: MIT
---

# ModelPool — Free AI Model Manager for OpenClaw

Automatically discover, configure, and maintain free AI models with multi-key rotation and smart fallback.

## Commands

- `modelpool setup` — Interactive setup: enter your OpenRouter keys, auto-discover best free models, configure rotation
- `modelpool auto` — Auto-discover and configure the best free models (non-interactive, uses existing keys)
- `modelpool list` — List all available free models from OpenRouter with quality scores
- `modelpool switch <model>` — Manually switch primary model
- `modelpool status` — Show current model config, key status, and fallback chain
- `modelpool repair` — Diagnose and fix model issues (dead API, stuck sessions, broken config)
- `modelpool keys add <key>` — Add a new OpenRouter key for rotation
- `modelpool keys list` — Show all configured keys and their status
- `modelpool refresh` — Force refresh model cache from OpenRouter API

## Setup

```bash
# First time: interactive setup
modelpool setup

# That's it. ModelPool will:
# 1. Ask for your OpenRouter key(s)
# 2. Auto-discover all free models
# 3. Score and rank them by quality
# 4. Configure multi-key rotation
# 5. Build smart fallback chain
# 6. Restart OpenClaw
```

## How It Works

### Multi-Key Rotation
Each OpenRouter key has independent rate limits. ModelPool distributes models across keys:
- Key1: Model A, Model C, Model E
- Key2: Model B, Model D, Model F

When Key1 hits rate limit → auto-switch to Key2's models → back to Key1 when cooldown ends.
**Result: 2x free quota with 2 keys, 3x with 3 keys.**

### Smart Fallback Chain
Models are ranked by quality score (based on context window, reasoning capability, and community ratings). The fallback chain is:
1. Best free model (Key1)
2. Best free model (Key2)
3. Second best (Key1)
4. Second best (Key2)
5. ... and so on

### Auto-Repair
`modelpool repair` runs 7-step diagnostics:
1. Check Gateway process
2. Validate config file
3. Test each model API connectivity
4. Fix config with `openclaw doctor`
5. Clean stuck sessions
6. Rebuild fallback chain (skip dead models)
7. Full restart

## Getting OpenRouter Keys

1. Go to [openrouter.ai](https://openrouter.ai)
2. Click "Sign Up" (free, no credit card needed)
3. Go to Keys page → Create Key
4. Copy the key starting with `sk-or-v1-...`

For more keys: use different email addresses. Each account gets independent free quota.

## File Structure

```
modelpool/
├── SKILL.md          # This file
├── scripts/
│   ├── freeswitch.py # Main CLI tool
│   └── repair.py     # Repair module
├── docs/
│   └── openrouter-guide.md
├── README.md
└── LICENSE
```
