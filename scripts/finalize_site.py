#!/usr/bin/env python3
"""Set the canonical origin in MyST static metadata and add Pages support files."""
from pathlib import Path
import re
SITE = Path(__file__).resolve().parents[1] / '_build/html'
ORIGIN = 'https://flview.org'
for path in SITE.rglob('*'):
    if path.suffix not in ('.html', '.json', '.xml', '.txt', '.xsl'):
        continue
    text = re.sub(r'http://localhost:\d+', ORIGIN, path.read_text())
    if path.suffix == '.html':
        route = '/' + str(path.relative_to(SITE)).removesuffix('index.html')
        text = re.sub(r'<link[^>]+rel="canonical"[^>]*>', '', text)
        text = text.replace('</head>', f'<link rel="canonical" href="{ORIGIN}{route}"/></head>')
    path.write_text(text)
(SITE / '.nojekyll').touch()
(SITE / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n')
print('PASS: canonical production URLs, sitemap, robots.txt, and .nojekyll prepared')
