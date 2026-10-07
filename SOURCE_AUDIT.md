# FloridaView Source Migration Audit

Source package: `Lab_WORD(1).zip` supplied for FloridaView curriculum migration.

## Migrated source assets

- 10 LiDAR laboratory tutorial DOCX files.
- 10 laboratory submission-template DOCX files.
- Original software-requirements document.
- Original FAU Apporto instructions.
- Original GitHub structure specification dated 2026-08-14.
- 111 media files extracted from the ten tutorial DOCX files and normalized into predictable per-lab asset folders.
- 4 source EMF graphics converted to PNG for browser/PDF compatibility (Labs 2, 5, and 7).

The earlier planning inventory listed 115 embedded figures/screenshots. Pandoc extraction from the supplied package produced 111 distinct media files; some source documents repeat or reference media objects in ways that do not map one-to-one to unique extracted files. The deployed browser/PDF review remains the final reconciliation gate for repeated or reused figures.

## Source cleanup applied

- Removed local `H:\MyCourses\...` course-drive paths from public tutorials.
- Removed temporary `/mnt/data/...` conversion paths.
- Replaced empty image alternatives with source-derived or procedural descriptions.
- Normalized image filenames by lab and sequence.
- Preserved original lab procedure content while adding consistent MyST metadata, learning objectives, software prerequisites, and FAU submission guidance.
- Kept the ten original submission templates as direct downloads.

No lab dataset ZIPs were present in the supplied source package. Dataset publication is intentionally marked **in preparation** rather than fabricated.

## 2026-10-07 production audit and demonstrated recoveries

The preceding section describes the supplied migration package. For this release, `FloridaView_V1_Final_20261007(1).zip` is authoritative for the current implementation. The original Word ZIP was consulted only after visual review demonstrated missing/cropped figures; no older prose replaced approved content wholesale.

The approved package contained 111 PNG instructional assets. All were retained, with one source-faithful replacement and one recovered composite added, yielding 112 image files and 113 uses across the ten labs.

| Defect | Evidence | Repair |
|---|---|---|
| Lab 7 Figure 2 lost labels and most of its diagram | Approved PNG was cropped; original Word page 3 rendered the complete first/last-return schematic and sample raster. Inkscape conversion reproduced the crop. | Rendered the original Word with LibreOffice, then extracted the complete figure region from PDF page 3 into the existing `fig-07-02.png`. No elements were redrawn or invented. |
| Lab 9 Figure 2 missing | Word `document.xml` includes a grouped figure with PNG panels `image4.png` / `image5.png` and TIFF fallback representations. Approved Markdown omitted this group. | Recovered the pair as one composite from original Word PDF page 3, saved as `fig-09-03.png`, and restored Figure 2 at its referenced procedure. Existing Figure 1 and Figure 3 files retain their names. |
| Lab 8 second image unused | `fig-08-02.png` was already in the approved ZIP and matches the terrain DSM procedure. | Added the existing image to the relevant procedure. |
| Two Lab 3 icons expanded to page width | The PNGs are 16 × 16 toolbar icons; default PDF block-image sizing enlarged them. | Added explicit 24px MyST image widths in the same lab Markdown source. |

Original Word renders for the other EMF-bearing labs (2 and 5), and Lab 7 Figure 3, were compared with the supplied converted assets. No additional replacement was warranted. Counts in the original Word package total 115 media files because the omitted Lab 9 group includes two TIFF fallback versions as well as its two PNG panels; media-file count is not the same as unique published figures.

All ten original submission templates and three source downloads in the final ZIP remain byte-for-byte unchanged. The newly recovered figures and source Word document hashes are recorded in the review evidence. Dataset files were neither manufactured nor substituted.

Targeted instructional repairs were grounded in surrounding steps or official software documentation: LAS symbology tables, TIN output location, inconsistent output names, the missing selected-contour export step, and ArcGIS TIFF support. Lab 10's original 0.61 m exercise is now explicitly described as its historical teaching scenario. Curriculum execution with real data remains unverified.
