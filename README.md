# FloridaView

Source for the FloridaView website and ten LiDAR laboratories. The production address is **https://flview.org**; see [QUALITY_REPORT.md](QUALITY_REPORT.md) for the actual release status. A successful local build is not evidence of a live deployment.

The repository remains in the **FloridaView** GitHub organization under Prof. Caiyun Zhang's institutional stewardship. Raghupathi Chepyala is the technical contributor. No ownership transfer is part of this release.

## Publishing architecture

Each `pages/lidar-labs/lab-NN.md` is the single source for its website page and downloadable PDF. GitHub Actions builds all ten Typst PDFs **before** building MyST HTML, validates the complete artifact, then deploys `_build/html` through GitHub Pages. Generated files are not committed. Namecheap provides DNS for the custom domain.

The [data gateway](pages/data.md) links to authoritative data providers. Course datasets that have not been published are explicitly labeled unavailable. Large datasets belong in Zenodo, ArcGIS Online where appropriate, or their authoritative repository.

## Reproduce the build

Install Node **24.19.0**, Python **3.12.14**, and the official Typst CLI **0.15.0**. Use a virtual environment for Python dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-build.txt
npm ci --ignore-scripts
npm run build
```

`npm run build` runs `scripts/release_gate.sh`: it retrieves the pinned book theme, cleans generated outputs, validates sources, generates ten PDFs, builds strict HTML, sets production metadata, and validates every bundled download and internal link. Internet access is required for the locked npm dependencies, pinned theme, and versioned Typst packages on first build.

For local browser review, run `npm start` after the build and open the URL printed by MyST. Check both desktop and mobile widths, light mode, keyboard navigation, and every lab download. Preview does not publish anything.

```bash
python3 scripts/check_external_links.py
```

The external-link report separates confirmed 404/410 failures from inconclusive timeouts or access restrictions. Review both; an exit code of zero does not mean every vendor link was verified.

## Maintenance and release

- [PI quick guide](PI_QUICK_GUIDE.md): edit one lab and publish both outputs.
- [Maintainer guide](MAINTAINER_GUIDE.md): exact review, CI, domain, and rollback workflow.
- [Release checklist](IMPLEMENTATION_CHECKLIST.md): outstanding gates.
- [Source audit](SOURCE_AUDIT.md): authority and targeted migration repairs.

Software licensing is in `LICENSE`; educational-content and third-party terms are in `LICENSE-CONTENT`. Original starter attribution is retained in `vendor/STARTER_LICENSE`.
