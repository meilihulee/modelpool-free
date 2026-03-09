# Linux Server Troubleshooting

## 1) Node installation failed
- Check outbound network access to `deb.nodesource.com` or `rpm.nodesource.com`.
- On apt systems, run: `apt-get update` then retry install.

## 2) npm global permission denied
- Run scripts as root or with sudo available.
- Retry repair script.

## 3) openclaw gateway restart failed under non-systemd environment
- Use `openclaw gateway` manual mode or `gateway restart` RPC if configured.
- Verify with `openclaw health --json`.

## 4) doctor fails on model/channel credentials
- Set valid provider keys and channel tokens.
- Re-run doctor and selfcheck.

## Exit code convention
- `selfcheck_openclaw_linux_server.sh`
  - `0`: healthy
  - `1`: one or more checks failed
