---
name: feedback-verify-before-asserting
description: Check specialized astrophysics claims against primary sources before stating them as findings; retract plainly when wrong.
metadata:
  type: feedback
---

On 2026-11-14 I told the user a 0.15 M☉ star would still be a red dwarf at 3 Tyr and that blue dwarfs only shrink; this came from memory and was wrong (the primary source, Laughlin–Bodenheimer–Adams 1997, shows radius growth to a maximum then shrinkage, and a 0.15 M☉ lifetime of ~2–3 Tyr). The user interrupted my question dialog and pasted contrary research.

**Why:** the vault's reconciliation work is only useful if its stated checks are right; asserting an unverified claim as a 'finding' wastes the user's decisions.
**How to apply:** for stellar evolution, interior or atmosphere models and other literature-dependent claims, fetch the primary source (web-fetch agent) before presenting a finding; label memory-based numbers as such; when the user supplies contrary research, read it and the primary source, say plainly what holds and what does not, and drop the withdrawn point.
