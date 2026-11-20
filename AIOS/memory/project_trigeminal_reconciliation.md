---
name: trigeminal-reconciliation
description: Trigeminal (Trigemina) system: findings, decisions (separations kept, 4–5 d binaries, V 8.9, empty candidate zones), files and plan.
metadata:
  type: project
---

Trigemina: six stars in three F+K binaries (A1 F5V 1.21 M☉ 2.52 L☉; A2 K7V 0.59/0.07; B1 F3V 1.31/3.62; B2 K5V 0.65/0.12; C1 F4V 1.19/2.31; C2 K7V 0.58/0.07), A–C at 10.2 AU (e 0.2, i≈3°), B around A+C at 220 AU (e 0.3, i≈10°); only page was `Trigemina.md` (star article), hub `Trigeminal System` unwritten, no planets, placeholders for RA/Dec; constellation 'Jinina'. Files: `Trigeminal System/Research/trigemina_reference.py` (+JSON), `trigemina_nbody_screen.cpp` (six stars + a planet per binary; Yoshida; usage in header).

**Checks that pass:** masses total A 1.80, B 1.96, C 1.77 (A+C 3.57, total 5.53 M☉); L from R and T within the listed ± (A1 2.67 vs 2.52, C1 2.63 vs 2.31); HZ centres √L = 1.61/1.93/1.54 AU; Mardling–Aarseth needs a_out/a_in 3.9 (actual 21.6); conservative HZ 1.53–2.21 (A), 1.84–2.66 (B), 1.47–2.12 (C).

**Findings:** Kepler periods for the quoted separations are 17.2 yr (A–C) and 1,388 yr (B), not 9.1 and 1,523 yr (those need 6.66 and 234 AU, and then the S-type limit around A/C is ~1.4 AU, inside the HZ); HW S-type limits are 2.14 AU (A), 2.11 (C), 31.9 AU (B) (page said 3.4 and >70); P-type limit about A–C binary 30 AU, S-type limit about A+C from B 46 AU, so circumquadruple dwarfs only in 30–46 AU; V at 200 pc for 8.71 L☉ is 8.9 (page 10.5; 10.5 needs ~420 pc); C seen from an A planet is 0.016–0.036 F⊕ (≈2,000–4,600 lux at night); B-star MS lifetime (M/L) 3.6 Gyr caps the age at ~2–3 Gyr; page gave no inner-binary periods.

**Decisions (2026-11-14):** (1) KEEP SEPARATIONS 10.2 AU and 220 AU → periods 17.2 yr and 1,388 yr. (2) Inner binaries ~4–5 d: A 4.0 d, B 5.0 d, C 4.5 d (a 0.060, 0.072, 0.065 AU; P-type limits 0.146, 0.175, 0.157 AU). (3) KEEP 200 pc, set V ≈ 8.9. (4) EMPTY CANDIDATE ZONES (no planets); planets can be designed later. Plan: create `Trigeminal System/Trigeminal System.md` hub, rewrite `Trigemina.md`, add a stage page `Trigeminal adopted reconciliation and calculations.md`.

**Completion (2026-11-14):** hub created, `Trigemina.md` rewritten (copy in Sources), stage page added. N-body (10⁵ yr): HZ-centre planets stable with e ≤0.09 (A, C), B planet e ≈0; A 2.1/C 2.2 AU stable with e ≤0.16/0.21; the 'keep periods' alternative (6.66 AU/234 AU) was also stable but with e ≤0.27 (CORRECTION: I had said it would be unstable). TRIGEMINAL RECONCILIATION COMPLETE; this was the last unreconciled system. Lore questions later: planets for each binary, system age and names, coordinates.

**Update (2026-11-14):** the stage record was folded into a `Physical basis` section on `Trigemina.md` and deleted; see [[reconciliation-files-removal]]. Noted for the user: the F stars live 3.6–5.2 Gyr against an adopted age of 2–3 Gyr, B1 shortest.
