# FloridaView maintainer guide

## Ownership and source authority

The official repository is https://github.com/FloridaView/floridaview.github.io. Prof. Caiyun Zhang remains the institutional steward; contributors work in review branches. Preserve history, organization ownership, and domain registration. Do not force-push `main` or replace the repository.

The approved final ZIP dated 2026-10-07 is the implementation baseline. Older Word documents are reference material for migration fidelity and recovery of demonstrated omissions. They do not supersede approved current content.

## One edit produces web and PDF

Edit `pages/lidar-labs/lab-NN.md`. Its Typst `exports` entry writes `pages/lidar-labs/exports/lidar/lab-NN.pdf`; its matching download ID exposes that PDF in the web page. The HTML build fingerprints the published PDF filename. Link to the lab page for a durable public URL rather than copying a generated hash URL.

Use normal Markdown for prose and tables, MyST directives for callouts/cards, and descriptive image alternatives. For small toolbar icons, use an `{image}` directive with an explicit width. Put screenshots in the lab's assets directory. Do not edit generated PDFs, HTML, or cached theme files.

## Build and review

Follow the pinned installation commands in `README.md`, then run:

```bash
npm run build
python3 scripts/check_external_links.py
npm start
```

The shared release script performs source inventory/link checks; strict PDF export; an exact ten-PDF gate; strict static HTML export; production canonical metadata; and validation of built HTML links, anchors, assets, PDF text, image counts, and byte-identical downloads. Reports and logs are in `_build/verification/`.

The book theme is pinned in `scripts/prepare_theme.py`. The PDF template is vendored under `templates/plain_typst_book/` with upstream commit and license. MyST is locked by `package-lock.json`; Python requirements and CI action revisions are pinned. Update dependencies in a separate PR and repeat the full review. Native Typst can fetch versioned packages such as `tablex` on first use; a build requires network access to those official sources.

Automated checks do not certify layout, keyboard interaction, screen-reader usability, or the scientific results of GIS exercises. Review all 20 pages in light mode, all ten PDFs, menu/search/download behavior, narrow viewports (including 375px), zoom/reflow, and keyboard focus. The named datasets are absent, so end-to-end ArcGIS/FUSION exercise execution cannot be claimed.

## Review branch to production

1. Create a branch from current `main`, make changes, run the local build, and commit.
2. Push to the FloridaView repository and open a pull request targeting `main`.
3. Require **Validate FloridaView / build** to succeed for the latest PR commit. Download its `floridaview-review-build` artifact and complete the browser/PDF review. Get PI review for curriculum changes.
4. Merge only after all gates are green. `Deploy FloridaView` rebuilds from the merged commit; its deploy job depends on a successful build. PR workflows cannot deploy to Pages.
5. Confirm the Pages deployment succeeded for that merged commit. Verify the public site and all ten PDF downloads, then record the commit and Actions run URLs in the handoff. Tag a release only after production verification.

Branch protection requiring the validation check is recommended but must be configured by a repository administrator. A YAML file alone does not enforce merge restrictions. Keep Prof. Zhang as organization owner and grant contributors only the access needed for their role.

## GitHub Pages and Namecheap

After review and CI pass, in repository **Settings → Pages** select **GitHub Actions** as the build source. Set the custom domain to `flview.org` before directing DNS to GitHub. Actions-based Pages deployments use this setting; an old starter `CNAME` file must not be reintroduced.

Inspect the current Namecheap nameservers and records first. If Namecheap BasicDNS/PremiumDNS is authoritative, edit **Domain List → Manage → Advanced DNS**. If another DNS provider is authoritative, edit records there instead. Use these records with automatic TTL:

| Type | Host | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `FloridaView.github.io` |

Replace only conflicting website/parking/URL-redirect records for `@` and `www`. Preserve MX, email-related TXT, verification TXT, and unrelated records. Do not add a wildcard. IPv6 is optional: if using it, GitHub's apex AAAA values are `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, and `2606:50c0:8003::153`. Remove stale conflicting website AAAA records if not configuring IPv6.

If GitHub requests domain ownership verification, add the exact TXT challenge displayed for the FloridaView organization; do not invent the value. After DNS validates and GitHub issues the certificate, enable **Enforce HTTPS**. Provisioning can take time. Verify apex HTTPS, HTTP-to-HTTPS redirect, and `www` redirect to `https://flview.org`, including a nested lab URL.

Official references:
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://www.namecheap.com/support/knowledgebase/article.aspx/319/2237/how-can-i-set-up-an-a-address-record-for-my-domain/

## Production acceptance and rollback

Check Home, Mission, PI, Data, Tutorials, all ten labs, Software & Access, Accessibility, Contact, and resource navigation. Download every PDF and submission template from the live site; compare PDF hashes with that deployment's output report. Check all instructional images, desktop/mobile light-mode rendering, keyboard navigation, and HTTPS redirects.

Revert a faulty merge through a PR and allow the deployment workflow to publish the last good source. Do not rewrite history or change ownership to roll back. Keep any temporary Vercel preview until the official site and domain have passed acceptance; its deletion is optional and separate from this build.

## Data and content limitations

Retain unavailable-data notices until each course dataset has a working gateway URL, provenance, rights, coordinate reference system, and checksum. Do not substitute arbitrary public datasets for the named teaching inputs. The current screenshots reflect their original application versions. Lab 4's original submission worksheet and lesson allocate points differently; the PI must determine the grading rubric. `LICENSE-CONTENT` records the existing third-party rights qualification.
