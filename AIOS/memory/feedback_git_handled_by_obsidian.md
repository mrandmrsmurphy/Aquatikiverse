---
name: feedback-git-handled-by-obsidian
description: The user's Obsidian Git plugin auto-commits and pushes the vault; Claude should not run git commit/push.
metadata:
  type: feedback
---

The user installed the Obsidian Git plugin (2026-11-20), which automatically commits and pushes the vault to the public GitHub repo `mrandmrsmurphy/Aquatikiverse`. Claude never needs to commit, push, or manage git for the vault.

**Why:** The user wants git to be invisible background infrastructure. An earlier `git add -A` by Claude pushed all images in one go, which is exactly what the user wanted to avoid (see [[project-github-image-upload-caution]]); the images (~158 MB) are already in the repo and the user accepted that.

**How to apply:** Do not run `git add`, `commit`, or `push` in this vault unless the user asks. Just edit files; the plugin handles versioning. Never use `git add -A` here. The batching script `AIOS/scripts/2026-11-20_push_images_in_batches.py` is unneeded.
