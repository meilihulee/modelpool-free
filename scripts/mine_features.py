#!/usr/bin/env python3
import json, re, os
from collections import OrderedDict

IN_FILE = '/root/.openclaw/workspace/data/harvest/latest.json'
OUT_FILE = '/root/.openclaw/workspace/data/harvest/feature_patterns.json'
os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

KEYWORDS = [
    'ai','agent','llm','gpt','copilot','cursor','sdk','api','workflow','automation',
    'model','open source','github','deployment','rag','inference','tool'
]


def priority_from_text(t: str) -> str:
    t=t.lower()
    if any(k in t for k in ['release','2.0','agent','copilot','cursor','studio']):
        return 'P0'
    if any(k in t for k in ['api','sdk','workflow','automation','model']):
        return 'P1'
    return 'P2'


def core_value(title: str) -> str:
    t=title.lower()
    if 'agent' in t: return '把重复决策与执行流程自动化，提升交付速度'
    if 'api' in t or 'sdk' in t: return '降低集成成本，缩短功能上线周期'
    if 'copilot' in t or 'cursor' in t: return '提升编码效率与代码质量一致性'
    if 'model' in t or 'llm' in t: return '提升模型能力接入与推理效率'
    return '帮助开发者更快构建并迭代工具型产品'


def ux_pattern(title: str) -> str:
    t=title.lower()
    if 'agent' in t: return '任务输入 -> 代理执行 -> 结果回传与继续迭代'
    if 'studio' in t: return '可视化配置 -> 预览测试 -> 一键部署'
    if 'api' in t or 'sdk' in t: return '统一接口层 + 模块化调用 + 可观察日志'
    return '搜索/配置/执行三段式流程'


def tech_hint(url: str, title: str) -> str:
    u=url.lower(); t=title.lower()
    if 'github.com' in u: return '优先看开源实现，抽取核心模块与CLI封装'
    if 'producthunt' in u: return '先做MVP功能切片，再补自动化与增长环节'
    if any(k in t for k in ['api','sdk']): return 'Node/Python SDK + REST/Webhook + 队列任务'
    return '前端控制台 + 后端任务编排 + 数据缓存层'


def monetization_hint(title: str) -> str:
    t=title.lower()
    if 'agent' in t: return '按执行次数/席位订阅，附加高级自动化套餐'
    if 'api' in t or 'sdk' in t: return '按调用量计费 + 企业版SLA'
    if 'copilot' in t or 'cursor' in t: return '个人订阅 + 团队协作包'
    return '免费试用 + 专业版订阅'


with open(IN_FILE,'r',encoding='utf-8') as f:
    data=json.load(f)
items=data.get('items',[])

patterns=[]
seen=OrderedDict()
for it in items:
    title=(it.get('title') or '').strip()
    url=(it.get('url') or '').strip()
    if not title or not url:
        continue
    t=title.lower()
    score=sum(1 for k in KEYWORDS if k in t)
    if score==0:
        continue
    key=re.sub(r'\s+',' ',title.lower())
    if key in seen:
        continue
    rec={
        'name': title[:80],
        'sourceTitle': title,
        'sourceUrl': url,
        'coreValue': core_value(title),
        'uxPattern': ux_pattern(title),
        'techHint': tech_hint(url,title),
        'monetizationHint': monetization_hint(title),
        'priority': priority_from_text(title)
    }
    seen[key]=1
    patterns.append(rec)

# sort priority P0>P1>P2
rank={'P0':0,'P1':1,'P2':2}
patterns.sort(key=lambda x:(rank.get(x['priority'],9), x['name']))

with open(OUT_FILE,'w',encoding='utf-8') as f:
    json.dump({'count':len(patterns),'items':patterns[:80]},f,ensure_ascii=False,indent=2)

print(f'Wrote {OUT_FILE}:',len(patterns[:80]))
