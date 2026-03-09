# macOS Troubleshooting

## 1) `openclaw: command not found`
- Reopen terminal.
- Run: `echo $PATH` and ensure `$HOME/.npm-global/bin` is present.
- Re-run `install_openclaw_macos.sh`.

## 2) npm permission errors
- Avoid sudo global npm if possible.
- Use user prefix (`~/.npm-global`) as set by install script.
- Re-run `repair_openclaw_macos.sh`.

## 3) Homebrew install failure
- Install Xcode Command Line Tools: `xcode-select --install`.
- Re-run install script.

## 4) `openclaw doctor` network failure
- Verify access to npm and your model provider endpoints.
- Retry after network/proxy fix.

## Exit code convention
- `selfcheck_openclaw_macos.sh`
  - `0`: healthy
  - `1`: one or more checks failed
