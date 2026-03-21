#!/usr/bin/env python3
import json, time, os, re
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from xml.etree import ElementTree as ET

OUT_DIR = '/root/.openclaw/workspace/data/harvest'
os.makedirs(OUT_DIR, exist_ok=True)

SOURCES = [
    ('github_trending_python', 'https://github.com/trending/python?since=daily'),
    ('github_trending_global', 'https://github.com/trending?since=daily'),
    ('hackernews_newest', 'https://hnrss.org/newest'),
    ('producthunt_feed', 'https://www.producthunt.com/feed'),
    ('techcrunch_feed', 'https://techcrunch.com/feed/'),
]


def fetch(url, timeout=20):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 OpenClaw-Harvester'})
    with urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='ignore')


def parse_rss(text):
    items = []
    try:
        root = ET.fromstring(text)
    except Exception:
        return items
    for item in root.findall('.//item')[:50]:
        title = (item.findtext('title') or '').strip()
        link = (item.findtext('link') or '').strip()
        pub = (item.findtext('pubDate') or item.findtext('published') or '').strip()
        if title and link:
            items.append({'title': title, 'url': link, 'published': pub})
    for item in root.findall('.//{http://www.w3.org/2005/Atom}entry')[:50]:
        title = (item.findtext('{http://www.w3.org/2005/Atom}title') or '').strip()
        link_el = item.find('{http://www.w3.org/2005/Atom}link')
        link = (link_el.get('href') if link_el is not None else '') or ''
        pub = (item.findtext('{http://www.w3.org/2005/Atom}updated') or '').strip()
        if title and link:
            items.append({'title': title, 'url': link, 'published': pub})
    return items


def parse_github_trending(html):
    items = []
    for m in re.finditer(r'<h2 class="h3 lh-condensed">\s*<a href="([^"]+)"', html):
        href = m.group(1)
        repo = href.strip('/').replace('/', ' / ')
        url = 'https://github.com' + href
        items.append({'title': repo, 'url': url, 'published': ''})
    return items[:50]


def run_once():
    ts = datetime.now(timezone.utc).isoformat()
    all_rows = []
    for name, url in SOURCES:
        try:
            raw = fetch(url)
            if 'github.com/trending' in url:
                items = parse_github_trending(raw)
            else:
                items = parse_rss(raw)
            for it in items:
                all_rows.append({
                    'source': name,
                    'fetchedAt': ts,
                    **it
                })
        except Exception as e:
            all_rows.append({'source': name, 'fetchedAt': ts, 'error': str(e)})

    # de-dup by url
    uniq = {}
    for r in all_rows:
        u = r.get('url')
        if u:
            uniq[u] = r
    rows = list(uniq.values())

    with open(os.path.join(OUT_DIR, 'latest.json'), 'w', encoding='utf-8') as f:
        json.dump({'fetchedAt': ts, 'count': len(rows), 'items': rows[:200]}, f, ensure_ascii=False, indent=2)

    with open(os.path.join(OUT_DIR, 'stream.jsonl'), 'a', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

    with open(os.path.join(OUT_DIR, 'heartbeat.txt'), 'w', encoding='utf-8') as f:
        f.write(f'{ts}\ncount={len(rows)}\n')


if __name__ == '__main__':
    run_once()
