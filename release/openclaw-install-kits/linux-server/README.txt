OpenClaw Linux Server One-Click Kit (Beginner)

Supports: Ubuntu/Debian/CentOS/RHEL/Alma/Rocky

1) SSH into server
2) cd into this folder
3) Run:

chmod +x ./install_openclaw_linux_server.sh ./selfcheck_openclaw_linux_server.sh ./repair_openclaw_linux_server.sh
./install_openclaw_linux_server.sh
./selfcheck_openclaw_linux_server.sh

If check fails:

./repair_openclaw_linux_server.sh
./selfcheck_openclaw_linux_server.sh

Expected:
- selfcheck exit code 0 = healthy
- selfcheck exit code 1 = still has issues
