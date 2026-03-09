# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

### 临时远程连接（Allen 本地 Windows）

> 用于紧急 SSH 远程协助。优先使用短期凭据，连接后尽快更换密码。

- 隧道类型：ngrok tcp
- 最近一次可用入口：`0.tcp.jp.ngrok.io:18436`
- 用户：`Administrator`
- 认证：password（用户侧提供）

示例连通测试（Linux 侧）：

```bash
ssh -p 18436 Administrator@0.tcp.jp.ngrok.io
```

当前会话中可用的一次性命令（含密码，慎用）：

```bash
sshpass -p '<PASSWORD>' ssh -o StrictHostKeyChecking=no -p 18436 Administrator@0.tcp.jp.ngrok.io "whoami"
```

注意：
- ngrok 地址/端口通常会变化，下次使用前先让用户回传最新地址。
- 如果用户重新开隧道，需要更新本节记录。
- 不在公开渠道保存明文密码。
