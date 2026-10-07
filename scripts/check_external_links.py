#!/usr/bin/env python3
"""Report definitive broken links separately from inconclusive network/bot blocks."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from urllib.parse import urldefrag
import json
import sys
from validate_source import ROOT, urls

targets = set()
for p in [ROOT / 'index.md', ROOT / 'footer.md', ROOT / 'sidebar-footer.md', *sorted((ROOT / 'pages').rglob('*.md'))]:
    targets.update(urldefrag(u)[0] for u in urls(p.read_text()) if u.startswith(('https://', 'http://')))

def check(url):
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (FloridaView link validation)'}), timeout=12) as r:
            return {'url': url, 'status': r.status, 'final_url': r.url, 'result': 'reachable'}
    except HTTPError as e:
        return {'url': url, 'status': e.code, 'result': 'broken' if e.code in (404, 410) else 'unverified', 'reason': str(e)}
    except Exception as e:
        return {'url': url, 'result': 'unverified', 'reason': str(e)}

results = list(ThreadPoolExecutor(max_workers=8).map(check, sorted(targets)))
out = ROOT / '_build/verification'
out.mkdir(parents=True, exist_ok=True)
(out / 'external-links.json').write_text(json.dumps(results, indent=2) + '\n')
counts = {key: sum(r['result'] == key for r in results) for key in ('reachable', 'broken', 'unverified')}
print(json.dumps(counts))
for r in results:
    if r['result'] != 'reachable':
        print(r['result'].upper(), r['url'], r.get('reason'))
sys.exit(1 if counts['broken'] else 0)
