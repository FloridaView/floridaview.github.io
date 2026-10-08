#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="$PWD/node_modules/.bin:$PATH"
for cmd in python3 myst typst; do
  command -v "$cmd" >/dev/null || { echo "FAIL: missing $cmd (see README.md)"; exit 1; }
done
myst --version
typst --version
python3 scripts/prepare_theme.py
# Delete only reproducible outputs belonging to this project.
rm -rf _build pages/lidar-labs/exports
mkdir -p _build/verification
python3 scripts/validate_source.py
echo "Building PDFs before HTML..."
myst build --typst --strict --ci 2>&1 | tee _build/verification/pdf-build.log
test "$(find pages/lidar-labs/exports/lidar -name 'lab-*.pdf' -type f | wc -l | tr -d ' ')" = 10
myst build --html --strict --ci 2>&1 | tee _build/verification/html-build.log
python3 scripts/finalize_site.py
python3 scripts/validate_output.py
echo "PASS: FloridaView build and artifact gates complete"
echo "Browser review, CI status, and production DNS/HTTPS are separate release gates."
