# Model Collector Adapter Results

## openrouter
- protocol: **openai-compatible** | ok: **True**
- base: `https://openrouter.ai/api`
- suggestion: 可按 OpenAI 兼容协议接入，优先用 /v1/chat/completions 测试。

## anthropic
- protocol: **unknown** | ok: **False**
- base: `https://api.anthropic.com`
- suggestion: 检查 base_url 是否包含正确网关路径与版本；确认 key 权限含模型推理。
