#!/usr/bin/env python3
import json, os

IN_FILE='/root/.openclaw/workspace/data/harvest/feature_patterns.json'
OUT_SK='/root/.openclaw/workspace/data/harvest/skills_ideas.json'
OUT_APP='/root/.openclaw/workspace/data/harvest/apps_ideas.json'
os.makedirs('/root/.openclaw/workspace/data/harvest', exist_ok=True)

with open(IN_FILE,'r',encoding='utf-8') as f:
    pats=json.load(f).get('items',[])


def mk_skill(i,p):
    title=p['name']
    return {
      'title': f"{title} 自动化技能",
      'type':'skill',
      'oneLiner':'把趋势能力封装成可复用 Agent 技能，减少重复手工操作',
      'targetUser':'独立开发者/自动化团队',
      'coreFeatures':['一键执行','参数化输入','结构化输出','失败重试'],
      'integration':['OpenClaw','Webhook/API','JSON存储'],
      'mvpPlan':['定义输入输出','实现脚本','接入任务流','添加验收用例'],
      'impact':4,'effort':2,'speedToMVP':'1-2天','moat':'Medium',
      'priority': p.get('priority','P1'),
      'rankReason': p.get('coreValue','')
    }


def mk_app(i,p):
    title=p['name']
    return {
      'title': f"{title} 轻量应用",
      'type':'app',
      'oneLiner':'围绕高频需求做垂直小应用，优先闭环与可变现',
      'targetUser':'内容运营/增长/开发团队',
      'coreFeatures':['数据采集','任务执行','结果看板','通知回传'],
      'integration':['OAuth/API','任务队列','SQLite/Postgres'],
      'mvpPlan':['做最小可用页面','接一条核心API','实现结果回显','部署上线'],
      'impact':4,'effort':3,'speedToMVP':'2-4天','moat':'Low',
      'priority': p.get('priority','P1'),
      'rankReason': p.get('techHint','')
    }

skills=[mk_skill(i,p) for i,p in enumerate(pats[:10],1)]
apps=[mk_app(i,p) for i,p in enumerate(pats[:10],1)]

with open(OUT_SK,'w',encoding='utf-8') as f:
    json.dump({'count':len(skills),'items':skills},f,ensure_ascii=False,indent=2)
with open(OUT_APP,'w',encoding='utf-8') as f:
    json.dump({'count':len(apps),'items':apps},f,ensure_ascii=False,indent=2)

print('Wrote',OUT_SK,len(skills))
print('Wrote',OUT_APP,len(apps))
