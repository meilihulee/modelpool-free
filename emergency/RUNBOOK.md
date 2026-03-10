# OpenClaw 应急手册（小船长）

更新时间：2026-03-10 14:42

## 1) 一键体检
```bash
openclaw health --json
```

## 2) 网关异常先重启
```bash
openclaw gateway restart
openclaw health --json
```

## 3) 模型应急切换（从免费切到稳定）
当前策略：免费优先 + 回退
- primary: openrouter/stepfun/step-3.5-flash:free
- fallbacks: haiku -> sf-flash -> gpt-5.3-codex

如需强制切到稳定主模型（codex）可执行：
```bash
openclaw config set agents.defaults.model.primary bobdong-codex/gpt-5.3-codex
openclaw gateway restart
```

## 4) Telegram 通道异常排查（最短路径）
```bash
openclaw health --json
# 看 channels.telegram.running 是否 true
```
若为 false：
```bash
openclaw doctor --non-interactive
openclaw gateway restart
openclaw health --json
```

## 5) 配置回滚
备份文件：
- /root/.openclaw/workspace/emergency/openclaw.json.backup-20260310-1442

回滚命令：
```bash
cp /root/.openclaw/workspace/emergency/openclaw.json.backup-20260310-1442 /root/.openclaw/openclaw.json
openclaw gateway restart
```

## 6) 关键目标
- 不断联（先保 Telegram 通道）
- 可用优先（必要时切 codex 主模型）
- 先恢复服务，再做优化
