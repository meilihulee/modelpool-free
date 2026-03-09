#!/usr/bin/env python3
import json
import os
import time
import urllib.request
import urllib.error
from datetime import datetime

RESOURCES = "/root/.openclaw/workspace/new-site/backend/src/data/resources.json"
OUT_DIR = "/var/www/leehub/maintenance"

os.makedirs(OUT_DIR, exist_ok=True)


def check_url(url: str, timeout: int = 8):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "leehub-maintainer/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, None
    except Exception:
        # Some sites block HEAD; fallback to GET.
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "leehub-maintainer/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, None
        except urllib.error.HTTPError as e:
            return e.code, str(e)
        except Exception as e:
            return None, str(e)


def main():
    with open(RESOURCES, "r", encoding="utf-8") as f:
        resources = json.load(f)

    total = len(resources)
    ok = 0
    bad = []

    for item in resources:
        title = item.get("title", "")
        url = item.get("url", "")
        if not url.startswith("http"):
            bad.append((title, url, "invalid url"))
            continue

        code, err = check_url(url)
        if code and 200 <= code < 400:
            ok += 1
        else:
            bad.append((title, url, f"code={code} err={err}"))
        time.sleep(0.15)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = [
        f"LeeHub maintenance report",
        f"time: {ts}",
        f"total: {total}",
        f"ok: {ok}",
        f"bad: {len(bad)}",
        "",
    ]
    for t, u, e in bad:
        report.append(f"- {t} | {u} | {e}")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_path = os.path.join(OUT_DIR, f"report-{stamp}.txt")
    latest_path = os.path.join(OUT_DIR, "latest.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")
    with open(latest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
