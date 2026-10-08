# FloridaView production candidate verification

Review date: 2026-10-07. **This is a locally validated candidate, not a completed production deployment.** No claim of green GitHub CI, merge, domain activation, or browser acceptance is made here.

## Verified locally

| Gate | Evidence and result |
|---|---|
| Authoritative package and repository comparison | Final October 7 ZIP inspected before changes; official repository contained the initial MyST starter at `926fa8e8c45166c469d46147c7d53793db2cdc42`. History retained. |
| Published source | 20 pages, ten lab Markdown sources and matching export/download IDs. |
| Instructional images | 112 PNG files, 113 uses; all decode and are referenced. Includes recovered Lab 9 Figure 2; repeated Lab 4 Explore icon accounts for the extra use. |
| Source downloads | Ten submission DOCX files plus three source documents retained byte-for-byte from the approved ZIP and ZIP integrity checked. |
| PDF generation | All ten PDFs compile; 118 pages total; required text and all 113 instructional image uses verified. |
| HTML generation | Strict MyST build produces all 20 pages after PDF export. |
| Bundled downloads | All ten PDF and ten worksheet download entries resolve to actual files with matching hashes. |
| Internal links | Built-page links, anchors, images, styles, and static assets checked; no missing targets found. |
| Accessibility basics | Published images have alternatives; source alternatives checked; each HTML page has English language, responsive viewport and one H1. Focus styling, hover contrast and reduced-motion support repaired. This is not WCAG certification. |
| External resources | 66 URLs tested: 65 reachable, no confirmed 404/410 failures, one inconclusive HTTP 403 from the FAU GIS Center. HTTP reachability is not content or licensing verification. |
| PDF visual review | All pages rendered and reviewed as contact sheets, with detailed checks of recovered figures and icon sizing. Original Word render used only for documented migration defects. |
| Clean theme retrieval | Theme fetched from a fresh cache at pinned commit; full local build succeeds. |
| Configuration syntax | Shell syntax, YAML parsing, action input spelling, pinned action references, and `git diff --check` reviewed. Actual Actions execution remains pending. |

PDF page counts: Lab 1: 5; Lab 2: 7; Lab 3: 11; Lab 4: 47; Lab 5: 5; Lab 6: 9; Lab 7: 10; Lab 8: 8; Lab 9: 8; Lab 10: 8.

Machine-readable build evidence is generated in `_build/verification/source.json` and `output.json`, with PDF hashes, counts, and build logs. External results are in `external-links.json` when its separate checker is run. CI uploads these reports as artifacts.

## Environment limits and outstanding gates

Local PDF compilation used the Typst 0.15.0 Python binding through a local CLI adapter because the native binary was unavailable. CI is configured for the official native Typst 0.15.0 CLI, but it has not run. Local HTML building needed a workspace-only Node network-interface shim because this sandbox rejects interface enumeration; the repository and CI do not depend on that shim.

The managed browser preview service failed with `bwrap: Can't mount proc on /newroot/proc: Operation not permitted`. Browser navigation, responsive layout, light-mode visual acceptance, keyboard behavior, and actual download-menu interaction have **not** been verified. Static HTML checks do not replace those gates.

The connected GitHub account reports pull access without push/admin access. Pages settings show a sign-in wall. Remote branch publication, PR creation, green CI, merge, Pages settings, Namecheap records, HTTPS, apex/www redirects, and live-site acceptance remain pending. No DNS record or Vercel project has been changed.

## Known content limitations

Named course datasets were not supplied and remain explicitly unavailable for public download. GIS exercises cannot be completed or scientifically validated end-to-end without those inputs and the required software/licenses. Screenshots retain their original software versions. Lab 4's supplied worksheet and lesson use different point allocations; the PI must establish the course rubric. The existing third-party content-license qualification remains in `LICENSE-CONTENT`. PDFs have not been certified as PDF/UA or audited with assistive technology.
