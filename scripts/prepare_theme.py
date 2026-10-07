#!/usr/bin/env python3
"""Fetch the approved book theme at an immutable commit, retaining its lockfile."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / '.cache/book-theme'
COMMIT = '23f2df5493e23dfb1d9433c8aa64c87beb4232a3'
URL = 'https://github.com/myst-templates/book-theme.git'

def git(*args):
    return subprocess.check_output(['git', '-C', str(THEME), *args], text=True).strip()

fresh_clone = not THEME.exists()
if fresh_clone:
    THEME.parent.mkdir(exist_ok=True)
    subprocess.run(['git', 'clone', '--no-checkout', URL, str(THEME)], check=True)
if git('remote', 'get-url', 'origin') != URL:
    raise SystemExit('Unexpected cached theme origin; inspect .cache/book-theme')
if not fresh_clone and git('status', '--porcelain', '--untracked-files=no'):
    raise SystemExit('Cached theme has modified tracked files; refusing to overwrite them')
if git('rev-parse', 'HEAD') != COMMIT:
    git('fetch', 'origin', COMMIT)
git('checkout', '--detach', COMMIT)
print(f'PASS: pinned book theme {COMMIT}')
