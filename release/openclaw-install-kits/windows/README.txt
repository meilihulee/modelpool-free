OpenClaw Windows One-Click Kit (Beginner)

1) Right click PowerShell -> Run as Administrator
2) cd into this folder
3) Run:

Set-ExecutionPolicy -Scope Process Bypass -Force
powershell -ExecutionPolicy Bypass -File .\install_openclaw_windows.ps1
powershell -ExecutionPolicy Bypass -File .\selfcheck_openclaw_windows.ps1

If check fails:

powershell -ExecutionPolicy Bypass -File .\repair_openclaw_windows.ps1
powershell -ExecutionPolicy Bypass -File .\selfcheck_openclaw_windows.ps1

Expected:
- selfcheck exit code 0 = healthy
- selfcheck exit code 1 = still has issues
