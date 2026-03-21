#!/usr/bin/env python3
import argparse, json, os, time
from urllib import request, error

OUT_DIR = '/root/.openclaw/workspace/data/model-collector'
GEN_DIR = os.path.join(OUT_DIR, 'generated')
os.makedirs(GEN_DIR, exist_ok=True)


def http_json(method, url, headers=None, payload=None, timeout=20):
    headers = headers or {}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    req = request.Request(url, data=data, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode('utf-8', errors='ignore')
            return r.status, body
    except error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        return e.code, body
    except Exception as e:
        return 0, str(e)


def norm_base(base_url):
    b = (base_url or '').rstrip('/')
    if b.endswith('/v1'):
        return b
    if b.endswith('/api'):
        return b + '/v1'
    return b + '/v1'


def probe_openai(base, key, model):
    headers = {'Authorization': f'Bearer {key}'} if key else {}
    s1, b1 = http_json('GET', f'{base}/models', headers=headers)
    s2, b2 = http_json('POST', f'{base}/chat/completions', headers=headers, payload={
        'model': model or 'gpt-4o-mini',
        'messages': [{'role': 'user', 'content': 'ping'}],
        'max_tokens': 8
    })
    return {
        'models_status': s1,
        'chat_status': s2,
        'models_ok': 200 <= s1 < 300,
        'chat_ok': 200 <= s2 < 300,
        'models_preview': b1[:240],
        'chat_preview': b2[:240]
    }


def probe_anthropic(base_raw, key, model):
    base = base_raw.rstrip('/')
    headers = {
        'x-api-key': key or '',
        'anthropic-version': '2023-06-01'
    }
    s, b = http_json('POST', f'{base}/v1/messages', headers=headers, payload={
        'model': model or 'claude-3-5-sonnet-latest',
        'max_tokens': 16,
        'messages': [{'role': 'user', 'content': 'ping'}]
    })
    return {
        'messages_status': s,
        'messages_ok': 200 <= s < 300,
        'messages_preview': b[:240]
    }


def classify(openai_probe, anth_probe):
    if openai_probe['chat_ok'] or openai_probe['models_ok']:
        return 'openai-compatible'
    if anth_probe['messages_ok']:
        return 'anthropic'
    return 'unknown'


def build_configs(results):
    openclaw = {'providers': []}
    opencode = {'providers': []}
    for r in results:
        if r['protocol'] == 'unknown':
            continue
        entry = {
            'name': r['name'],
            'base_url': r['base_url'],
            'api_key_env': r['env_key']
        }
        openclaw['providers'].append(entry)
        opencode['providers'].append(entry)
    return openclaw, opencode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    args = ap.parse_args()

    src = json.load(open(args.input, 'r', encoding='utf-8'))
    sources = src.get('sources', [])

    results = []
    for s in sources:
        name = s.get('name', 'unknown')
        base_raw = s.get('base_url', '')
        base = norm_base(base_raw)
        key = s.get('api_key', '')
        env_key = s.get('api_key_env', f'{name.upper()}_API_KEY')
        model = (s.get('preferred_models') or [''])[0]

        o = probe_openai(base, key, model)
        a = probe_anthropic(base_raw, key, model)
        protocol = classify(o, a)

        ok = protocol != 'unknown'
        suggestion = '检查 base_url 是否包含正确网关路径与版本；确认 key 权限含模型推理。'
        if protocol == 'openai-compatible':
            suggestion = '可按 OpenAI 兼容协议接入，优先用 /v1/chat/completions 测试。'
        elif protocol == 'anthropic':
            suggestion = '按 Anthropic 协议接入，需 x-api-key + anthropic-version。'

        results.append({
            'name': name,
            'base_url': base_raw,
            'normalized_base': base,
            'env_key': env_key,
            'preferred_model': model,
            'protocol': protocol,
            'ok': ok,
            'openai_probe': o,
            'anthropic_probe': a,
            'suggestion': suggestion,
            'timestamp': int(time.time())
        })

    openclaw_cfg, opencode_cfg = build_configs(results)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, 'results.json'), 'w', encoding='utf-8') as f:
        json.dump({'count': len(results), 'items': results}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(GEN_DIR, 'openclaw.providers.json'), 'w', encoding='utf-8') as f:
        json.dump(openclaw_cfg, f, ensure_ascii=False, indent=2)
    with open(os.path.join(GEN_DIR, 'opencode.providers.json'), 'w', encoding='utf-8') as f:
        json.dump(opencode_cfg, f, ensure_ascii=False, indent=2)

    md = ['# Model Collector Adapter Results', '']
    for r in results:
        md.append(f"## {r['name']}")
        md.append(f"- protocol: **{r['protocol']}** | ok: **{r['ok']}**")
        md.append(f"- base: `{r['base_url']}`")
        md.append(f"- suggestion: {r['suggestion']}")
        md.append('')
    with open(os.path.join(OUT_DIR, 'results.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print('done:', os.path.join(OUT_DIR, 'results.json'))


if __name__ == '__main__':
    main()
