---
name: scripts-in-aios
description: User's rule (2026-11-14) that all Research/ folders are deleted and any future script goes in AIOS/scripts/ with a date prefix.
metadata:
  type: feedback
---

The user chose to DELETE every `Research/` folder (all scripts, JSON, CSV, run outputs, READMEs; 148 files) rather than keep tools or an offline zip. Scripts written from now on are time-stamped parts of AIOS: `AIOS/scripts/YYYY-MM-DD_name.py` (or `.cpp`), private and unpublished.

**Why:** the user wants system folders to contain only readable pages; results belong on pages as tables, not in code folders, and the recipe is cheap to rebuild when a number changes.
**How to apply:** never create a `Research/` folder again; put new scripts and their outputs in `AIOS/scripts/` with the date prefix; put the numbers that matter on the content or stage page. If a calculation needs redoing, rebuild it from the page's tables and method text. Related: [[sources-research-inventory]], [[vault-cleanup-plan]]. Today's redox script lives at `AIOS/scripts/2026-11-14_redox_reference.py`.
