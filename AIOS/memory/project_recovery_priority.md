---
name: recovery-priority
description: "AIOS and logging support recovery from AI mistakes and catastrophe; a manual zip backup exists, and the vault is a git repo (2026-11-20) pushed to a public GitHub repo."
metadata:
  type: project
---

A central purpose of this persistent-memory and logging setup is to roll back damaging AI actions and recover lost work after a catastrophe, or at least preserve enough description to understand what was lost. All durable support files must live inside this vault; tool-specific or chat memory is not an acceptable durable store.

An append-only descriptive log is not a complete backup and cannot guarantee restoration of prior bytes. This setup does not initialize git, establish automatic backups, configure remote replication, or choose a snapshot/versioning policy. Those recovery mechanisms remain a separate user decision. Do not describe AIOS as catastrophe-proof.

**Why:** The user explicitly prioritizes recovery from AI mistakes and loss, rather than merely avoiding repeated conversation.

**How to apply:** Log meaningful changes and corrections promptly, preserving enough detail for reconstruction; retain provenance and avoid destructive cleanup without authorization. Keep archives frozen and rotate only when asked. Do not put a duplicate session history in another memory or audit file. If exact rollback or off-device recovery is required, discuss and implement an explicitly chosen backup/versioning mechanism as a separate task. Related: [[reference_session_logging]], [[feedback_write_memories_before_session_ends]].

**Backup status:** A manual zip backup of the whole vault exists in the parent folder (`Documents/Aquatikiverse 20261113.zip`, taken 2026-11-13). The vault has been a git repo since 2026-11-20, remote `origin` = public `github.com/mrandmrsmurphy/Aquatikiverse`; images not yet pushed.
