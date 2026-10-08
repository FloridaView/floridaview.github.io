# FloridaView release checklist

Status recorded 2026-10-07. Checked items have local evidence; unchecked items block the requested production acceptance.

- [x] Inspect final authoritative ZIP and compare official repository.
- [x] Preserve Git history, approved branding, current content direction, and original worksheets.
- [x] Validate 20 sources, ten labs, 112 instructional images, and internal source links.
- [x] Generate ten PDFs before HTML; verify all download files and PDF image uses.
- [x] Build all 20 HTML pages with strict MyST checks.
- [x] Validate built internal links, anchors, assets, and basic document semantics.
- [x] Render and review all ten PDFs; recover documented missing/cropped source figures.
- [x] Test practical external links; document the inconclusive FAU 403.
- [x] Test theme setup from a fresh cache and rebuild.
- [ ] Review every production page and lab in a browser in light mode.
- [ ] Verify mobile layout, zoom/reflow, keyboard navigation, search, and downloads.
- [ ] Publish review branch and open pull request to `main`.
- [ ] Verify native Typst and all gates in GitHub Actions on the latest PR commit.
- [ ] Merge only after the preceding gates pass.
- [ ] Configure Pages source as GitHub Actions; verify production deploy succeeds.
- [ ] Set Pages custom domain and inspect/configure authoritative Namecheap DNS.
- [ ] Verify HTTPS certificate, apex, HTTP redirect, and www redirect.
- [ ] Verify all public pages, images, PDF downloads and worksheet downloads.
- [ ] Record live URL, merge SHA, CI/deployment URLs, PDF hashes and browser evidence in the handoff.
- [ ] Tag a release after production acceptance; optionally retire Vercel afterward.

`npm run build` covers build/artifact gates, not all items above. See `QUALITY_REPORT.md` for environment and access blockers; `MAINTAINER_GUIDE.md` contains the continuation workflow and exact DNS records.
