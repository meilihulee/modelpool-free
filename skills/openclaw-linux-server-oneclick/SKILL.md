---
name: openclaw-linux-server-oneclick
description: One-click OpenClaw install and recovery for Linux cloud servers (Ubuntu/Debian/CentOS/RHEL/Alma/Rocky). Use when users need fast and stable server deployment with prerequisite checks, automatic install, health self-check, and repair flow.
---

# OpenClaw Linux Server One-Click

Use this skill for beginner-friendly cloud server deployment.

## Workflow

1. Detect distro and package manager automatically.
2. Install prerequisites (curl, ca-certificates, Node.js LTS) safely.
3. Install OpenClaw globally via npm.
4. Run `openclaw doctor --non-interactive` and `openclaw health --json`.
5. If unhealthy, run repair script and verify again.
6. Return status:
   - healthy
   - healthy-with-warning
   - needs-manual-help

## Commands

```bash
chmod +x ./install_openclaw_linux_server.sh ./selfcheck_openclaw_linux_server.sh ./repair_openclaw_linux_server.sh
./install_openclaw_linux_server.sh
./selfcheck_openclaw_linux_server.sh
```

If broken:

```bash
./repair_openclaw_linux_server.sh
./selfcheck_openclaw_linux_server.sh
```

## References

- Read `references/troubleshooting.md` for standard failure and fix matrix.
