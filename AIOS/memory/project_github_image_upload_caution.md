---
name: project-github-image-upload-caution
description: When the vault becomes a GitHub repo, do not push all images at once; stage uploads in batches.
metadata:
  type: project
---

Never upload all the vault images to GitHub at once; be careful not to upload all the images at once.

**Why:** The user flagged this in advance; the vault holds many shared images, and a bulk push risks size limits or failure.

**How to apply:** At repo setup, add images in small batches (or use `.gitignore` / Git LFS as discussed with the user), and check total image size first. Make the initial commit text-only, then add images incrementally. Ask the user which approach they prefer before the first push. Related: [[project-recovery-priority]].

**Status (2026-11-20):** Repo created as public `mrandmrsmurphy/Aquatikiverse`; text-only commit pushed. The user chose plain git in batches (~20-30 MB per commit/push) for `images/`; not yet done. If a push fails with HTTP 400, retry with `-c http.postBuffer=524288000`.

**Update (2026-11-20):** All images were pushed at once by mistake and the user accepted this; nothing further to batch. Git is now handled by the Obsidian Git plugin ([[feedback-git-handled-by-obsidian]]).
