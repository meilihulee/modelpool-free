---
name: model-collector-adapter
description: Collect model API endpoints and automatically probe protocol compatibility (OpenAI/Anthropic/Responses) for different agents and coding tools, then generate normalized adapter configs and test reports.
---

# Model Collector Adapter

用于把“模型 API + URL”自动整理成可用配置，并输出协议匹配结果与测试报告。

## 适用场景

- 你有多家模型供应商的 API 地址与密钥
- 你希望自动识别协议（OpenAI 兼容 / Anthropic / Responses）
- 你希望按不同 Agent / 编程工具输出可直接接入的配置片段

## 输入

创建输入文件：

`/root/.openclaw/workspace/data/model-collector/sources.json`

示例结构：

```json
{
  "sources": [
    {
      "name": "openrouter",
      "base_url": "https://openrouter.ai/api",
      "api_key": "sk-...",
      "preferred_models": ["openai/gpt-4o-mini"]
    }
  ]
}
```

## 执行

```bash
python3 /root/.openclaw/workspace/skills/model-collector-adapter/scripts/collector.py \
  --input /root/.openclaw/workspace/data/model-collector/sources.json
```

## 产出

- `data/model-collector/results.json`：探测结果与兼容性矩阵
- `data/model-collector/results.md`：可读汇总
- `data/model-collector/generated/openclaw.providers.json`：OpenClaw provider 配置片段
- `data/model-collector/generated/opencode.providers.json`：OpenCode provider 配置片段

## 规则

- 先探测，再生成配置；不要盲猜协议
- 每个源至少做 1 次 endpoint 连通性测试
- 若失败，写明最短修复建议（URL/Key/Path/Header）
