---
name: openclaw-macos-oneclick
description: One-click beginner-friendly OpenClaw setup and recovery on macOS. Use when users want fast/stable OpenClaw installation on macOS (Intel/Apple Silicon), with automatic prerequisite checks, install, doctor self-check, and repair flow.
---

# OpenClaw macOS One-Click

Use this skill to provide copy-paste setup for new users on macOS.

## Workflow

1. Confirm user is on macOS and can run Terminal commands.
2. Run `scripts/install_openclaw_macos.sh`.
3. Run `scripts/selfcheck_openclaw_macos.sh`.
4. If check fails, run `scripts/repair_openclaw_macos.sh` and re-run self-check.
5. Return final status as:
   - healthy
   - healthy-with-warning
   - needs-manual-help

## Commands to provide users

```bash
chmod +x ./install_openclaw_macos.sh ./selfcheck_openclaw_macos.sh ./repair_openclaw_macos.sh
./install_openclaw_macos.sh
./selfcheck_openclaw_macos.sh
```

If broken:

```bash
./repair_openclaw_macos.sh
./selfcheck_openclaw_macos.sh
```

## What to read when needed

- For common failure patterns and exact fixes, read `references/troubleshooting.md`.
- Self-check json output is written to `/tmp/openclaw-install/selfcheck.json`.
