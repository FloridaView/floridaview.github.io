# FloridaView PI maintenance guide

Prof. Caiyun Zhang retains institutional stewardship through the FloridaView organization. A technical contributor maintains the implementation without taking ownership of the organization, repository, or domain.

## Update a lab once

1. Open https://github.com/FloridaView/floridaview.github.io and select `main`.
2. Open `pages/lidar-labs/lab-NN.md` and click **Edit**. Change the lesson in this Markdown file. Keep its `exports` and `downloads` metadata.
3. Choose **Create a new branch for this commit and start a pull request**. Give the branch a descriptive name, such as `update-lab-04-2027`. Do not commit directly to `main`.
4. If figures changed, upload replacements under `assets/labs/lidar/lab-NN/` on the same branch. Keep descriptive alt text and stable names when practical.
5. Open the pull request. Wait for **Validate FloridaView / build** to turn green for the latest commit. Review the changed web page and its generated PDF with the technical contributor. The workflow artifact is named `floridaview-review-build`; it contains the site, PDFs, and validation reports. A ZIP download of the site needs a local web server for browser review.
6. Approve curriculum changes and merge only after the required checks and visual review pass.
7. Wait for **Deploy FloridaView** on `main` to succeed. Open https://flview.org, visit the changed lab, and use **Downloads → Download this lab as PDF**. Confirm the new text appears in both versions.

GitHub Actions regenerates both outputs automatically. There is no separate PDF manuscript to maintain. Word submission templates remain separate student worksheets; edit those only when the assignment form itself changes.

## Common changes

| Change | Source |
|---|---|
| PI biography | `pages/pi.md` |
| Mission | `pages/mission.md` |
| Data availability and gateway links | `pages/data.md` and `DATA_SOURCES.md` |
| Tutorials landing page | `pages/tutorials/index.md` |
| Software and access | `pages/software.md` |
| Accessibility or contact information | `pages/accessibility.md`, `pages/contact.md` |
| Screenshots | `assets/labs/lidar/lab-NN/` |
| Submission worksheet | `downloads/submission-templates/lab-NN-submission-template.docx` |

Keep large datasets outside the website repository. A new data download must have a real, tested URL and clear provenance. Until then, retain the availability notice in each affected lab.

If a check fails, ask the technical contributor to fix the branch. Do not bypass a failing check. To undo a published change, use GitHub's **Revert** on the merged pull request, then review and merge the revert through the same checks.
