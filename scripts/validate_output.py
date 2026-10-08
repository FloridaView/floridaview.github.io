#!/usr/bin/env python3
"""Check the actual deploy artifact, every lab download, and PDF contents."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import hashlib
import json
import re
import sys
from pypdf import PdfReader
from validate_source import image_references

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_build/html'
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids, self.images = path, [], set(), []
        self.lang = self.viewport = False
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'html':
            self.lang = a.get('lang') == 'en'
        if tag == 'meta' and a.get('name') == 'viewport':
            self.viewport = 'width=device-width' in a.get('content', '')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img':
            self.images.append(a)
            if 'alt' not in a:
                errors.append(f'{self.path}: image lacks alt attribute')
        for key in ('href', 'src'):
            if a.get(key):
                self.links.append(a[key])

def find_file(url):
    p = SITE / unquote(urlsplit(url).path).lstrip('/')
    for q in (p, p / 'index.html', p.with_suffix('.html')):
        if q.is_file():
            return q
    return None

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

pages = {}
for path in sorted(SITE.rglob('*.html')):
    page = Page(str(path.relative_to(SITE)))
    page.feed(path.read_text())
    pages[path] = page
    if not (page.lang and page.viewport and page.h1 == 1):
        errors.append(f'{page.path}: language, responsive viewport, or single H1 check failed (H1={page.h1})')
if len(pages) != 20:
    errors.append(f'Expected 20 HTML pages; found {len(pages)}')
for path, page in pages.items():
    base = '/' + str(path.relative_to(SITE))
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        resolved = urljoin(base, link)
        target = find_file(resolved)
        if target is None:
            errors.append(f'{page.path}: missing built target {link}')
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{page.path}: missing anchor {link}')

labs = []
for i in range(1, 11):
    stem = f'lab-{i:02}'
    source = ROOT / f'pages/lidar-labs/{stem}.md'
    pdf = ROOT / f'pages/lidar-labs/exports/lidar/{stem}.pdf'
    data = json.loads((SITE / f'pages.lidar-labs.{stem}.json').read_text())
    downloads = data['frontmatter']['downloads']
    pdf_item = next((d for d in downloads if d.get('filename') == stem + '.pdf'), None)
    docx_item = next((d for d in downloads if d.get('filename') == stem + '-submission-template.docx'), None)
    if not pdf_item or not docx_item:
        errors.append(f'{stem}: PDF or submission template missing from download menu')
        continue
    for item, original in [(pdf_item, pdf), (docx_item, ROOT / f'downloads/submission-templates/{stem}-submission-template.docx')]:
        deployed = find_file(item['url'])
        if deployed is None or digest(deployed) != digest(original):
            errors.append(f'{stem}: missing or stale bundled download {item["filename"]}')
    reader = PdfReader(pdf, strict=True)
    expected_images = len(list(image_references(source.read_text())))
    actual_images = sum(len(p.images) for p in reader.pages)
    if actual_images != expected_images:
        errors.append(f'{stem}: {actual_images} PDF image uses versus {expected_images} source image uses')
    text = '\n'.join(p.extract_text() for p in reader.pages)
    for required in (f'Lab {i}', 'Caiyun Zhang', 'Overview', 'Teaching data'):
        if required not in text:
            errors.append(f'{stem}: PDF missing required content {required}')
    for page in reader.pages:
        for annotation in page.get('/Annots', []):
            uri = annotation.get_object().get('/A', {}).get('/URI', '')
            if uri and uri.startswith('/'):
                errors.append(f'{stem}: relative PDF hyperlink {uri}')
    labs.append({'lab': stem, 'pdf_pages': len(reader.pages), 'pdf_image_uses': actual_images, 'pdf_sha256': digest(pdf), 'download_url': pdf_item['url']})
# Static source assets and original downloads must survive the build byte-for-byte.
for folder in ('assets', 'downloads'):
    for p in (ROOT / folder).rglob('*'):
        if p.is_file():
            q = SITE / p.relative_to(ROOT)
            if not q.is_file() or digest(p) != digest(q):
                errors.append(f'Static asset missing or changed: {p.relative_to(ROOT)}')
report = {'html_pages': len(pages), 'labs': labs, 'errors': sorted(set(errors))}
out = ROOT / '_build/verification'
out.mkdir(exist_ok=True)
(out / 'output.json').write_text(json.dumps(report, indent=2) + '\n')
if errors:
    print('\n'.join(report['errors']))
    sys.exit(1)
print(f'PASS: 20 built pages, internal links/anchors/assets, 10 downloadable PDFs and DOCX templates, PDF text and all {sum(lab["pdf_image_uses"] for lab in labs)} instructional image uses')
