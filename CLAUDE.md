# Aquatikiverse Instructions

This file and `AGENTS.md` are duplicates — always keep them byte-identical; edit both (or edit one and copy it over the other) whenever instructions change.

Aquatikiverse is a personal recreational workspace for practicing and integrating physics, chemistry, and biology through fictional stars, worlds, biospheres, and civilizations. Its primary audience is the user, with occasional sharing with students; future work will add explanations, encyclopedic reference articles, and current exoplanetary research links. The vault uses a main Aquatikiverse hub, system/topic folders, linked subject articles, shared images, and reconciliation records that document each system's calculated results. Preserve the user's important fictional identities while explaining scientific tradeoffs and distinguishing chosen speculation from calculated results.

## Memory system (read first)

- Read `AIOS/memory-index.md` first, every session, before touching anything. It points to every durable memory (project identity, standing decisions, workflow feedback from past sessions). Do not skip it and re-derive things from scratch.
- Durability warning: never write anything meant to persist to `~/.claude/projects/.../memory/` or anywhere outside this vault folder. Everything meant to survive across sessions goes in `AIOS/memory/`, indexed in `AIOS/memory-index.md`. Session-by-session history of what was created/changed/decided goes in `logs/log.md` (append-only).
- See `AIOS/site-map.md` for the current page hierarchy and status of each section.
- Scripts and calculation outputs (Python, C++, JSON, run logs) never live in system folders or `Research/` folders. Any script written from now on goes in `AIOS/scripts/` with a date prefix (`YYYY-MM-DD_name.py`); the results that matter go on the content or stage page as readable tables.
- When something is worth remembering (a standing decision, a correction, a workflow preference, a fact that would otherwise be re-derived), write it to the vault in the same turn. Do not wait for a later wrap-up. If I say "write memories now," flush everything durable immediately.

## Content pages vs. log — the rule that matters most

- Content pages (everything outside `AIOS/` and `logs/`) document **current state only**. No date stamps, no "decided by the user on X," no correction narratives. If a decision changes, update the page's fact in place, written as if it had been right from the start.
- All history — what was decided when, what got corrected, who caught what — belongs exclusively in `logs/log.md` (append-only, never edit past entries). If you catch yourself writing history on a content page, move it to today's log entry instead.
- Citation-confidence / evidentiary-weight flags (for example "plausible extension, not directly attested") are facts about the claim itself and are fine on content pages — terse and undated, no session references or names.
- `AIOS/site-map.md` and everything in `AIOS/memory/` are exempt from this rule — tracking what changed and when is their actual job. Dates and "New (date)" markers belong there.

## End-of-session checklist

Before finishing any session that changed anything:

1. Append today's entry to `logs/log.md` (new `## YYYY-MM-DD` header if none exists for today; otherwise add bullets under today's header).
2. Update `AIOS/site-map.md` for any page added, removed, or whose scope or status changed.
3. Write or update any durable memory (decision, correction, workflow preference) in `AIOS/memory/` and add its line to `AIOS/memory-index.md`.
4. If this file changed, copy it over its twin so `CLAUDE.md` and `AGENTS.md` stay byte-identical.
