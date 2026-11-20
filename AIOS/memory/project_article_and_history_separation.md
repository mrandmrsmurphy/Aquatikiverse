---
name: article-and-history-separation
description: "Presentable current-state articles are the goal; migrate existing audit history into logs in a later task."
metadata:
  type: project
---

The main body of the vault should become presentable, polished current-state articles. AIOS and logs are under-the-hood support. All editorial/session history, audit narratives, corrections and who-decided-what accounts belong in `logs/log.md`; dates and changes in scope/status can also be tracked in `AIOS/site-map.md` and memories.

Existing audit/reconciliation history is legacy material awaiting eventual migration into the logs. The user rejected leaving it permanently embedded in the main body. The AIOS setup itself must not modify, rename, move, or delete existing content pages; perform the migration as a subsequent task. Do not treat the old format as a standing precedent for new articles, and do not reconstruct old session history unless requested.

Scientific assumptions, source citations, confidence qualifiers, evidentiary weight and model limitations remain current-state reference facts. In-universe chronology and scientific epochs remain article content. Distinguish these from editorial narratives when migrating audit material; preserve scientific substance and provenance rather than discarding them.

**Why:** The user wants clean articles while retaining a recoverable account of AI changes and mistakes under the hood.

**How to apply:** Update current facts in place when content editing is authorized, and append the change/decision history to the live log. Record scope/status changes in the site map. When audit migration is undertaken, transfer historical material without losing unique lore, calculations, source attribution or model limits. See [[reference_session_logging]] and [[project_recovery_priority]].
