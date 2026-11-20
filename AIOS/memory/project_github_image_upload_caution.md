---
name: project-github-image-upload-caution
description: When the vault becomes a GitHub repo, do not push all images at once; stage uploads in batches.
metadata:
  type: project
---

The vault is not yet a git or GitHub repo (as of 2026-11-20). When it is made one, be careful not to upload all the images at once.

**Why:** The user flagged this in advance; the vault holds many shared images, and a bulk push risks size limits or failure.

**How to apply:** At repo setup, add images in small batches (or use `.gitignore` / Git LFS as discussed with the user), and check total image size first. Make the initial commit text-only, then add images incrementally. Ask the user which approach they prefer before the first push. Related: [[project-recovery-priority]].
