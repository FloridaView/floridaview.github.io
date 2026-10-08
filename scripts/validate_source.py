#!/usr/bin/env python3
"""Validate the complete published source inventory, not just Markdown links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
import hashlib
import json
import re
import sys
import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []

def require(ok, message):
    if not ok:
        ERRORS.append(message)

def frontmatter(path):
    text = path.read_text()
    return yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---\n') else {}

def toc_files(entries):
    for entry in entries:
        if 'file' in entry:
            yield entry['file']
        yield from toc_files(entry.get('children', []))

def urls(text):
    # The supported source forms: Markdown links/images, autolinks, and card links.
    yield from re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
    yield from re.findall(r'<(https?://[^>\s]+)>', text)
    yield from re.findall(r'^:link:\s*(\S+)', text, re.M)
    yield from re.findall(r'^:::\{image\}\s+(\S+)', text, re.M)

def image_references(text):
    yield from re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
    for url, options in re.findall(r'^:::\{image\}\s+(\S+)\n(.*?)^:::\s*$', text, re.M | re.S):
        alt = re.search(r'^:alt:\s*(.+)$', options, re.M)
        yield (alt.group(1) if alt else '', url)

def main():
    config = yaml.safe_load((ROOT / 'myst.yml').read_text())
    files = list(toc_files(config['project']['toc']))
    require(len(files) == 20 and len(set(files)) == 20, 'Expected 20 distinct published pages')
    labs = [f'pages/lidar-labs/lab-{i:02}.md' for i in range(1, 11)]
    require(set(labs) <= set(files), 'All ten labs must be in the navigation')
    images, external, inventory = set(), set(), []
    for name in files + ['footer.md', 'sidebar-footer.md']:
        p = ROOT / name
        require(p.is_file(), f'Missing source: {name}')
        if not p.is_file():
            continue
        text = p.read_text()
        require(not re.search(r'^::\{', text, re.M), f'{name}: invalid two-colon directive')
        require(not re.search(r'\n\?\?\s*\n', text), f'{name}: unresolved conversion placeholder')
        for url in urls(text):
            parsed = urlsplit(url)
            if parsed.scheme in ('http', 'https'):
                external.add(url)
                continue
            if parsed.scheme or not parsed.path:
                continue
            target = (ROOT / parsed.path.lstrip('/')) if parsed.path.startswith('/') else p.parent / unquote(parsed.path)
            require(target.is_file(), f'{name}: missing link/image/card target {url}')
        for alt, url in image_references(text):
            require(bool(alt.strip()) and 'Description automatically generated' not in alt,
                    f'{name}: non-descriptive image alternative: {alt}')
            q = (p.parent / url).resolve()
            images.add(q)
        if name in labs:
            fm = frontmatter(p)
            stem = p.stem
            require(len(fm.get('exports', [])) == 1, f'{name}: expected one PDF export')
            export = fm['exports'][0]
            require(export['format'] == 'typst' and export['output'] == f'exports/lidar/{stem}.pdf', f'{name}: invalid PDF export')
            require(export['id'] == stem + '-pdf', f'{name}: inconsistent PDF export ID')
            require((p.parent / export['template'] / 'template.yml').is_file(), f'{name}: missing PDF template')
            downloads = fm.get('downloads', [])
            require(any(d.get('id') == export['id'] for d in downloads), f'{name}: missing PDF download')
            for d in downloads:
                if 'file' in d:
                    require((p.parent / d['file']).is_file(), f'{name}: missing download {d["file"]}')
            require('Teaching data: not yet published' in text, f'{name}: dataset availability must be explicit')
            inventory.append({'lab': stem, 'image_uses': len(list(image_references(text))), 'source_sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    lab_images = set((ROOT / 'assets/labs/lidar').glob('**/*.png'))
    require(len(lab_images) == 112, f'Expected 112 instructional images, including recovered Lab 9 Figure 2; found {len(lab_images)}')
    require(lab_images <= images, 'Unreferenced instructional images: ' + ', '.join(str(p.relative_to(ROOT)) for p in lab_images - images))
    for p in (ROOT / 'assets').glob('**/*'):
        if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.ico'):
            try:
                with Image.open(p) as im:
                    im.verify()
            except Exception as exc:
                ERRORS.append(f'{p}: unreadable image: {exc}')
    templates = list((ROOT / 'downloads/submission-templates').glob('lab-*.docx'))
    require(len(templates) == 10, 'Expected ten original submission templates')
    for p in (ROOT / 'downloads').glob('**/*.docx'):
        with ZipFile(p) as archive:
            require(archive.testzip() is None and 'word/document.xml' in archive.namelist(), f'{p}: invalid DOCX')
    report = {'pages': len(files), 'labs': inventory, 'instructional_images': len(lab_images), 'submission_templates': len(templates), 'external_urls': sorted(external), 'errors': ERRORS}
    out = ROOT / '_build/verification'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'source.json').write_text(json.dumps(report, indent=2) + '\n')
    if ERRORS:
        print('\n'.join(ERRORS))
        return 1
    print(f'PASS: {len(files)} pages, 10 labs, {len(lab_images)} referenced instructional images, 10 DOCX templates; source links and image alternatives valid')
    return 0

if __name__ == '__main__':
    sys.exit(main())
