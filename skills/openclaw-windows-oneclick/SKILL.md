---
name: openclaw-windows-oneclick
description: One-click beginner-friendly OpenClaw setup and recovery on Windows. Use when users want fast/stable OpenClaw installation on Windows 10/11, with automatic prerequisite checks, install, doctor self-check, and repair/reinstall flow.
---

# OpenClaw Windows One-Click

Use this skill to deliver a copy-paste, low-friction setup for beginners on Windows.

## Workflow

1. Confirm user is on Windows 10/11 and has admin PowerShell.
2. Run `scripts/install_openclaw_windows.ps1` in elevated PowerShell.
3. Run `scripts/selfcheck_openclaw_windows.ps1`.
4. If check fails, run `scripts/repair_openclaw_windows.ps1` and re-run self-check.
5. Return a short final status with next action:
   - healthy
   - healthy-with-warning
   - needs-manual-help

## Commands to provide users

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
powershell -ExecutionPolicy Bypass -File .\install_openclaw_windows.ps1
powershell -ExecutionPolicy Bypass -File .\selfcheck_openclaw_windows.ps1
```

If broken:

```powershell
powershell -ExecutionPolicy Bypass -File .\repair_openclaw_windows.ps1
powershell -ExecutionPolicy Bypass -File .\selfcheck_openclaw_windows.ps1
```

## What to read when needed

- For common failure patterns and exact fixes, read `references/troubleshooting.md`.
- For output interpretation, use script exit codes and json artifacts in `%TEMP%\openclaw-install`.
