# Changelog

## 2026-10-07 — FloridaView V1 production candidate

- Finalized FloridaView navigation, mission, PI, data, tutorials, software/accessibility, and contact pages.
- Migrated all ten LiDAR tutorials to maintainable MyST Markdown with 111 normalized instructional media assets.
- Added all ten original submission templates as stable downloads.
- Switched lab PDF generation to the `plain_typst_book` Typst template proven in local testing.
- Replaced PDF-hostile raw HTML tables and repaired Word-to-Markdown formatting artifacts.
- Added custom FloridaView footer/sidebar identity and refined white-first institutional styling.
- Added automated source gates, Typst PDF builds, static HTML deployment, and monthly external-link checks.
- Corrected CI artifact paths and added an explicit ten-PDF deployment gate.
- Updated PI/contact details and external resource links against current official sources.
- Large teaching-data packages remain intentionally marked in preparation until provenance, rights, checksums, and durable hosting are confirmed.

## 2026-09-26 — FloridaView V1 release candidate

- Established FloridaView-owned GitHub/MyST publishing architecture.
- Replaced template placeholder structure with FloridaView navigation.
- Added Mission, PI, Data, Tutorials, Software, Accessibility, and Contact pages.
- Migrated all ten LiDAR lab tutorials from the provided Word source package to Markdown.

## 2026-10-07 — Audited production candidate repair

- Reconstructed the approved source on a branch descending from the official repository's initial commit.
- Corrected malformed lab cards, Lab 3 icon tables/sizing, selected procedural typos and output names, and the obsolete TIFF restriction in Lab 7.
- Restored Lab 8's already-supplied DSM image, recovered cropped Lab 7 Figure 2 and omitted Lab 9 Figure 2 from the original Word render, and retained all other approved media.
- Pinned MyST, the web theme, Python dependencies, native CI Typst, and action revisions; vendored the PDF template with its license.
- Fixed PDF pagination and relative links, production canonicals, workflow ordering, and clean-checkout theme setup.
- Added source/output validation and honest external-link reporting. All local build/artifact gates pass; browser, GitHub CI and production/domain gates remain pending.
- Replaced stale deployment commands with an exact review-branch maintenance workflow.
