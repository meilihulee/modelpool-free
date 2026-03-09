OpenClaw macOS One-Click Kit (Beginner)

1) Open Terminal
2) cd into this folder
3) Run:

chmod +x ./install_openclaw_macos.sh ./selfcheck_openclaw_macos.sh ./repair_openclaw_macos.sh
./install_openclaw_macos.sh
./selfcheck_openclaw_macos.sh

If check fails:

./repair_openclaw_macos.sh
./selfcheck_openclaw_macos.sh

Expected:
- selfcheck exit code 0 = healthy
- selfcheck exit code 1 = still has issues
