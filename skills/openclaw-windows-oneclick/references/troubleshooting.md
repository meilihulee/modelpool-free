# Windows Troubleshooting

## 1) `openclaw` not recognized
- Close and reopen PowerShell.
- Run `npm prefix -g` and ensure that path is in User PATH.
- Re-run `install_openclaw_windows.ps1`.

## 2) npm permission or EACCES style errors
- Use elevated PowerShell (Run as Administrator).
- Run `repair_openclaw_windows.ps1`.

## 3) `openclaw doctor` fails due to network
- Check proxy/firewall.
- Retry after confirming access to npm registry and model provider endpoints.

## 4) Telegram or channel auth issues
- Validate token in OpenClaw config.
- Run `openclaw doctor --non-interactive` again.

## Exit code convention
- `selfcheck_openclaw_windows.ps1`
  - `0`: healthy
  - `1`: one or more checks failed
