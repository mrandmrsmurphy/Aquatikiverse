---
name: session-logging
description: "One append-only live log; same-day sessions share a date section; rotation occurs only on request."
metadata:
  type: reference
---

- Session-by-session history lives in exactly one place: `logs/log.md`.
- Format: one dated header (`## YYYY-MM-DD`) per date, bullets underneath, newest at the bottom. Multiple sessions on the same day share that section, as explicitly clarified by the user. One bullet per notable thing created, changed, or decided.
- Append-only, forever. Never edit or delete a past entry. If a past entry turns out to be wrong, add a new entry noting the correction; never rewrite history.
- Terse is the ideal, not a hard limit. Sessions doing real design or research work may produce detailed entries; losing real information is worse than length.
- Content/log separation: content pages document current state only (no dates, no correction narratives); history goes in the log; `AIOS/` is exempt. This concerns editorial date stamps, not meaningful in-universe dates or scientific epochs.
- Rotation, ONLY when I ask (never roll unprompted):
  1. `cp logs/log.md logs/archive/log-NNN.md`, verbatim, zero-padded, next sequential number (first is `log-001.md`). The archive file is frozen forever.
  2. Replace `logs/log.md` with just the header plus a pointer to the archive and `logs/index.md`.
  3. Add an entry to `logs/index.md` (create it on the first rotation): one prose paragraph per archived file, oldest first, summarizing the major threads by date-section so the right archive can be found without opening each.
  4. Update `AIOS/site-map.md` if it lists the log files.
  5. Update this memory file with anything learned from the roll.

Related: [[project_article_and_history_separation]], [[project_recovery_priority]], [[feedback_write_memories_before_session_ends]].
