# FloridaView V1 release candidate notes

This candidate preserves the approved October 7 implementation and repairs defects discovered during release validation. Production acceptance is pending; see `QUALITY_REPORT.md` for verified results and outstanding gates.

The website contains the approved Home, Mission, PI, Data, Tutorials, Software & Access, Accessibility, and Contact pages, the tutorial resources page, and the ten-lab LiDAR sequence. Each lab remains one MyST Markdown source that publishes to the web and exports a Typst PDF. Original student worksheets are unchanged.

Repairs include valid lab cards and icon tables, targeted procedure/name corrections, descriptive image alternatives, restored Lab 8 media, complete Lab 7 Figure 2, recovered Lab 9 Figure 2, readable PDF icon sizes, useful section pagination, absolute PDF links, and production canonical metadata. Missing teaching datasets remain clearly labeled.

Builds now use locked dependencies and a pinned theme, a vendored PDF template, shared PR/production validation, exact PDF counts, and complete artifact/download checks. Maintenance documentation uses a branch/PR workflow and distinguishes local validation from GitHub CI and live verification. Starter license attribution and repository ancestry are retained.

Institutional ownership and domain registration are unchanged. Large datasets stay outside this repository. No Vercel cleanup is included before the official deployment passes acceptance.
