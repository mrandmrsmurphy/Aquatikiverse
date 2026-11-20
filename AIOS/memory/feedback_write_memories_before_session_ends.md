---
name: write-memories-before-session-ends
description: "Write durable decisions and workflow feedback to vault memory immediately; never rely on ephemeral agent memory."
metadata:
  type: feedback
---

- **Why:** ephemeral chat or agent-session memory can be deleted without warning. Only vault files under `AIOS/memory/` (indexed in `AIOS/memory-index.md`) and the append-only `logs/log.md` survive across sessions.
- **How to apply:** when something is worth remembering, write it to the vault in the same turn. If I say to write memories now, or ask whether you can follow protocol, flush anything durable immediately. Durable goes to `AIOS/memory/` plus a new index line; session history goes under today's header in `logs/log.md`; nothing meant to persist goes outside this vault folder.
