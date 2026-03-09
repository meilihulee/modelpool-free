#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB = Path('/root/.openclaw/workspace/ops-stack/data/kuma/kuma.db')

MONITORS = [
    ('leehub-home', 'https://leehub.xyz/'),
    ('leehub-api', 'https://api.leehub.xyz/api/resources'),
]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute('SELECT id, username FROM user ORDER BY id LIMIT 1')
    row = cur.fetchone()
    if not row:
        raise SystemExit('No Kuma user found. Complete Kuma setup first.')
    user_id = row[0]

    for name, url in MONITORS:
        cur.execute('SELECT id FROM monitor WHERE name = ?', (name,))
        if cur.fetchone():
            print(f'exists: {name}')
            continue

        cur.execute(
            '''INSERT INTO monitor
            (name,active,user_id,interval,url,type,weight,maxretries,ignore_tls,upside_down,maxredirects,accepted_statuscodes_json,retry_interval,method,resend_interval,timeout)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
            (name, 1, user_id, 60, url, 'http', 2000, 3, 0, 0, 10, '["200-299"]', 60, 'GET', 0, 48),
        )
        print(f'inserted: {name}')

    con.commit()
    cur.execute('SELECT id,name,url,interval,maxretries FROM monitor ORDER BY id')
    print('\nmonitors:')
    for r in cur.fetchall():
        print(r)


if __name__ == '__main__':
    main()
