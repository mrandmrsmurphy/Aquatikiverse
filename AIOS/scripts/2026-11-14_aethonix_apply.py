"""Staged edit for the Aethonix records (dry run by default; --apply writes)."""
import sys, os, re
DRY = "--apply" not in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse/Aethonix System")
def load(p): return open(p, encoding="utf-8").read()
OUT = {}
def sub(p, a, b):
    s = OUT.get(p) or load(p)
    assert s.count(a) == 1, (p, a[:70], s.count(a))
    OUT[p] = s.replace(a, b)

REC = "[[Aethonix adopted reconciliation and calculations]]"
MARK = "## Reference and model limits"
def tail(p, new):
    s = OUT.get(p) or load(p)
    assert s.count(MARK) == 1, p
    sect = s[s.index(MARK):]
    assert REC in sect and len(sect) < 500, (p, len(sect))
    OUT[p] = s[:s.index(MARK)].rstrip("\n") + "\n\n" + new.strip("\n") + "\n"

# ---------------------------------------------------------------- inline satellite-table sentence on seven host pages
OLD_SAT = "Masses/radii absent from the original account are declared model inputs in [[Aethonix adopted reconciliation and calculations]], not discoveries silently attributed to the source."
NEW_SAT = "Masses and radii not otherwise specified are declared model inputs, described under Physical basis on [[Aethonix System]]."
for pg in ("Velora", "Goku", "Thalor", "Rimeas", "Noctilux", "Cryodon", "Tsurai"):
    sub(pg + ".md", OLD_SAT, NEW_SAT)

# ---------------------------------------------------------------- wording
sub("Life on Goku.md", "Source display width: 300 px. This fuller biosphere article governs detailed biology; earlier planetary and system accounts remain supplemental.", "This fuller biosphere article governs detailed biology; the planetary and system accounts are supplemental.")
sub("Tsurai.md", "Their listed kilometre sizes are radii; the ambiguous0.1–0.5 AU-equivalent phrase is retired:", "Their listed kilometre sizes are radii, and literal 0.1–0.5 AU-equivalent axes would partly exceed the ~0.289 AU Hill scale:")
sub("Rimeas.md", "and the revised e=0.02 support", "and the e = 0.02 support")
sub("Noctilux.md", "take precedence over old 0.95-atm or patchy-gas wording.", "govern its atmosphere.")
sub("Noctilux.md", "The image’s original outer-moon caption remains illustrative;", "The image’s outer-moon caption is illustrative;")
sub("Lunara.md", "as a target of the revised hydrogen-bearing greenhouse", "as a target of the hydrogen-bearing greenhouse")
sub("Lunara.md", "## Revised atmosphere and warmth requirement", "## Atmosphere and warmth requirement")
sub("Life on Lunara.md", "Planetwide0.05 atm freeO₂is retired;", "A planetwide 0.05 atm of free O₂ is not assumed;")
sub("Glaciumite.md", "; the conflicting512.4 g/mol entry is retired.", ".")
sub("Glaciumite.md", "overburden is~39–90 MPa; the former>500 MPa value is not kept at those same shallow depths.", "overburden is~39–90 MPa, so a >500 MPa confinement would not fit those shallow depths.")
sub("Aethonix System.md", "with Rimeas f correcting its former duplication of Thalor e.", "with Rimeas f.")

# ---------------------------------------------------------------- Aethonix (star)
tail("Aethonix.md", """
## Physical basis

**Stars.** The primary's radius of about 1.161 R☉ preserves its 5930 K temperature and the 1.70 L☉ total luminosity; a 1.05 R☉ radius at that temperature would give only about 1.426 L☉. The tuple satisfies Stefan–Boltzmann arithmetic (about 1.502 and 0.198 L☉ for the two stars) but is not a fitted stellar-evolution or metallicity track. The 26- and 41-day stellar spins are reference values, not proof of weak tidal or magnetic evolution, and the 7.5–8 Gyr lifetime scale is distinct from the present 4-Gyr age. The binary's relative orbit is 0.150 AU with e = 0.01 and a period of 15.816 days.

**Location.** The shared J2000 position (RA 09h20m, Dec −50°) and 12.9-pc distance are used in the documented Galactic frame. Demonyms for human communities are not evidence of independent native sapient species on these worlds. Surface climate targets, crystal performance and long-term orbital evolution are distinguished from computed arithmetic and short gravitational screens.
""")

# ---------------------------------------------------------------- hub
tail("Aethonix System.md", """
## Physical basis

This section separates adopted setting inputs from calculated arithmetic, declared model choices and unverified long-term physics: a climate target is not a radiative-transfer result, and a short surviving orbit is not a four-billion-year proof. No manufactured-system premise, collector swarm or exotic nuclear power source applies here.

**Planets.**

| Body | Axis (AU) | e | Period (Earth days) | Flux (Earth) |
| --- | --- | --- | --- | --- |
| Aska | 0.600 | 0.02 | 126.53 | 4.722 |
| Velora | 1.200 | 0.00 | 357.87 | 1.181 |
| Goku | 1.345 | 0.03 | 424.66 | 0.940 |
| Thalor | 1.530 | 0.02 | 515.22 | 0.726 |
| Rimeas | 1.728 | 0.02 | 618.40 | 0.569 |
| Noctilux | 4.000 | 0.00 | 2177.93 | 0.1063 |
| Cryodon | 6.000 | 0.00 | 4001.11 | 0.0472 |
| Tsurai | 12.000 | 0.00 | 11316.86 | 0.01181 |

NX-4b, Aethonix Target 77 and TPN-12.8 are catalog aliases, not physical orbital specifications. Eccentricities of 0.06 for Thalor and 0.10 for Rimeas would make their radial envelopes overlap; at 0.02 the axes stay, seasonal forcing weakens and clearance improves. The adopted layout survived two 5000-year explicit-binary screens and a 2000-year half-step check, with minimum sampled interplanet distances of about 0.097–0.100 AU; no exact 6:5 chain or libration is asserted. The classical habitable zone, 1.24–2.18 AU, is a model-dependent descriptor: Velora can be a near-inner-edge climate target, Rimeas lies inside the interval, and the main belt partially overlaps its outer portion.

**Dry atmosphere references.** These are dry reference mixtures, and water vapor, local outgassing and vertical chemistry need normalization of wet fractions. They are climate-model inputs, not validated mean temperatures or human exposure guarantees.

| World | Pressure | N₂ | O₂ | Other reference constituents |
| --- | --- | --- | --- | --- |
| Velora | 0.91 atm | 75.96% | 23% | Ar 1%, CO₂ 0.04% |
| Goku | 1.3 atm | 74.9% | 24% | Ar 1.029%, CO₂ 0.07%, Kr/other 0.001% |
| Thalor | 1.7 atm | 86.5% | 12.4% | Ar 1%, CO₂ 0.1%; volcanic gases regional |
| Rimeas | 4 atm | 90.299999% | 5.2% | Ar 4.2%, CO₂ 0.2%, CH₄ 0.1%, SF₆ 0.000001% (10 ppb) |
| Lunara | 20 bar | 64.9499% | not a global bulk constituent | H₂ 30%, CO₂ 5%, CH₄ 0.05%, NH₃/other 0.0001% |

Goku's pO₂ of about 0.312 atm keeps its fire and physiology significance, while Rimeas (about 0.208 atm) and Thalor (about 0.211 atm) do not by themselves certify breathable conditions; pressure scattering, methane haze, fluorinated-gas lifetime and CO₂ physiology remain model requirements.

**Satellites.** All named moons remain. The masses, radii and axes below are declared modeling choices, not measurements, and the multi-moon screens required wider spacing for Goku, Noctilux and Thalor.

- Velora: the unnamed 1.1-lunar-mass moon at 300,000 km, radius unspecified.
- Goku: Gohan (0.7 lunar masses) at 180,000 km and Goten (0.4 lunar masses) at about 374,415 km; the name-to-mass assignment is an adoption choice, and the period ratio is near 3:1 with no libration claim.
- Thalor: Caelis, Tamar and Nerith near 3:1 and 3:1, with Nerith's 20-local-day (18.33 Earth-day) orbit preserved; Caelis's radius is chosen for an apparent diameter of about 1°, and Velka stays outer, smallest in volume and inclined and eccentric, though not automatically the largest instantaneous eccentricity under perturbations.
- Rimeas: Jacob (0.2 lunar masses) at 140,000 km and Esau (1 lunar mass) at 300,000 km.
- Noctilux: Narela at 180,000 km, Lunara at 400,000 km, Thyxis at 1,200,000 km and Boril at 3,000,000 km. Narela (0.03 M⊕) and Lunara (0.086 M⊕) have source masses, and Thyxis (0.003 M⊕) and Boril (0.001 M⊕) have nominal masses with radii unspecified.
- Cryodon: the listed major sizes are radii, with model mean densities of 1.8–2.5 g/cm³: Evara 350,000 km, Halix 700,000 km, Vesca 1.3 million km, Zhenya 2.3 million km, Myrrh 4 million km and the eccentric retrograde Roqan 7 million km.
- Tsurai: the listed major sizes are radii, with model mean densities of 1.5–2.5 g/cm³: Aurenne 0.5 million km, Halego 0.8 million km, Mizari 1.3 million km, Keltra 2.2 million km, Iphrix 3.8 million km at about 30° and the eccentric retrograde Droven 8 million km. A literal 0.1–0.5 AU-equivalent axis would partly exceed the roughly 0.289 AU Hill scale.

The unusual total moon masses call for a natural formation history with impacts, captures and modified disks; the system is not manufactured. Small main-planet inclinations are not Earth-view inclinations, and neither magnetic fields, the number of moons nor a reservoir of orbital angular momentum stabilizes every spin and orbit.

**Screens.** The planetary reference uses the explicit binary and eight-planet low-eccentricity screens (5000 years each), which omit satellites. The satellite screen integrates each host with all its declared major moons and a 1.8-M☉ stellar point source, with finite moon masses, nominal eccentricities and inclinations and an initial barycentric reflex adjustment; it omits the binary quadrupole, other planets and hosts, minor moons and rings, J₂, tides, spin, dissipation and climate. It is not a full combined-system integration and does not validate source inclination histories or resonance libration. All seven host models have 1000-year seed-0 runs, and Noctilux, Thalor, Cryodon and Tsurai have second-phase and smaller-step checks, as does Goku's wider pair. A total energy dominated by the host and stars means surviving a trial is not a convergence proof.

A Noctilux layout with Thyxis and Boril at 800,000 and 1,200,000 km failed in the first full four-moon start, and 1,000,000 and 2,000,000 km survived a coarse trial but showed a near-escape in the smaller-step test; the 1,200,000 and 3,000,000-km layout is tested independently. A compact Goku 3:2 hypothesis also failed, which does not exclude every phase-protected resonance. Some surviving models develop appreciable eccentricity excursions, which are tidal and thermal concerns even without escape, so no perpetual low-eccentricity stability is promised, and secular robustness, true resonance angles, coupled all-host perturbations, stellar tides and 4-Gyr survival remain unproved.

**Belts.** The Dawn Lanterns are candidate Rimeas exterior 3:2 families near 2.264 AU, not 60° trojans without a host, and the roughly 3.3-AU groups are associated with Noctilux's interior 4:3 near 3.302 AU. Tsuraid exterior 3:2 and 2:1 groups lie near 15.72 and 19.05 AU. These are plausible locations, not a test-particle occupancy simulation. Ordinary 15–30 AU equilibrium temperatures are about 82–58 K before albedo, and Tsurai can scatter objects inward as well as remove them.
""")

# ---------------------------------------------------------------- Aska
tail("Aska.md", """
## Physical basis

Aska's 800-atm, 1200–1300 °C target is not cooled merely because the irradiation equilibrium is about 388 K. A nominal pressure-supported volatile inventory is of order 7.44×10²¹ kg (about 0.050% of the planet's mass), with composition and radiation chemistry still to be solved. Volatile-rich runaway-greenhouse calculations reach surface temperatures above 1500 K, a precedent for the target that does not validate Aska's exact state ([Kasting 1988, runaway and moist greenhouse atmospheres](https://www.pku-atmos-acm.org/static/pdfs/Runaway%20and%20moist%20greenhouse%20atmospheres%20and%20the%20evolution%20of%20Earth%20and%20Venus.pdf)). Acid rain falls in compatible cooler layers and evaporates or reacts before the hottest surface. The 84.35-day rotation is 3:2 in spin frequency, not in rotation period, and long-term capture is unmodeled. The orbital screens are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Velora
tail("Velora.md", """
## Physical basis

At Velora's 80° obliquity the polar annual-mean heating can exceed the equatorial, so forests, rain belts and winter refugia follow seasonal topography and ocean circulation, not an imposed Earth-like latitude rule; high-obliquity dynamic-ocean models give a comparison, not a Velora simulation ([Ferreira et al., climate at high obliquity](https://pog.mit.edu/src/ferreira_climate_high_obliquity_2014.pdf)). The 1.1-lunar-mass moon at 300,000 km gives, with an illustrative J₂ = 0.0013 and C = 0.33, a precession scale of tens of thousands of years, with no proven obliquity stabilization. The orbital screens and atmosphere reference are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Goku
tail("Goku.md", """
## Physical basis

Goku's two moons, Gohan (0.7 lunar masses, 180,000 km) and Goten (0.4 lunar masses, about 374,415 km), have a period ratio near 3:1 with no libration claim, and a compact source-sized 3:2 hypothesis was unstable in the screens. The 1.3-atm reference has a pO₂ of about 0.312 atm. The atmosphere table and screens are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Thalor
tail("Thalor.md", """
## Physical basis

Thalor's moons Caelis, Tamar and Nerith lie near 3:1 and 3:1, with Nerith's 20-local-day (18.33 Earth-day) orbit preserved and Caelis's radius chosen for an apparent diameter of about 1°; Velka is the outer, smallest-volume moon on an inclined, eccentric orbit. The 278-K temperate target compares with an irradiation equilibrium of about 239 K, and pressure, haze cooling and gas warming belong to one energy balance. The atmosphere reference (1.7 atm, pO₂ about 0.211 atm) and the screens are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Rimeas
tail("Rimeas.md", """
## Physical basis

Rimeas's moons are Jacob (0.2 lunar masses, 140,000 km) and Esau (1 lunar mass, 300,000 km). A near-Earth oxygen partial pressure (about 0.208 atm) does not remove the 4-atm total pressure, nitrogen and CO₂ loading, dust or local chemical hazards, so the field systems and sealed vehicles are fictional infrastructure design, not an exposure or decompression protocol. The 2–7 °C target is a greenhouse target under about 0.569 Earth flux. The atmosphere table and screens are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Noctilux
tail("Noctilux.md", """
## Physical basis

Noctilux's four moons (Narela 180,000 km, Lunara 400,000 km, Thyxis 1,200,000 km, Boril 3,000,000 km) were tested together, and tighter Thyxis and Boril layouts produced a failure or near-escape; the adopted spacing is a working reference, not a stability proof. The irradiation-only equilibrium comparison is about 143 K at a Bond albedo of 0.35. The screens and rejected layouts are described on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Cryodon / Tsurai
tail("Cryodon.md", """
## Physical basis

Cryodon's listed major moon sizes are radii, with model mean densities of 1.8–2.5 g/cm³: Evara 350,000 km, Halix 700,000 km, Vesca 1.3 million km, Zhenya 2.3 million km, Myrrh 4 million km and the eccentric retrograde Roqan 7 million km. The atmosphere, ocean and phase claims for the moons need thermal, escape and phase models. The screens are on [[Aethonix System]] under Physical basis.
""")
tail("Tsurai.md", """
## Physical basis

Tsurai's listed major moon sizes are radii, with model mean densities of 1.5–2.5 g/cm³: Aurenne 0.5 million km, Halego 0.8 million km, Mizari 1.3 million km, Keltra 2.2 million km, Iphrix 3.8 million km at about 30° and the eccentric retrograde Droven 8 million km. Literal 0.1–0.5 AU-equivalent axes would partly exceed the roughly 0.289 AU Hill scale, so the table keeps the planet-dominating vistas without impossible axes. The screens are on [[Aethonix System]] under Physical basis.
""")

# ---------------------------------------------------------------- Lunara
tail("Lunara.md", """
## Physical basis

At the source radius of 3200 km, mass 0.086 M⊕, axis 400,000 km and e = 0.1, Lunara's two-body period is 9.175 days. Global absorbed starlight is about 26 W/m² at a Bond albedo of 0.28, and the standard synchronous-tide sensitivity for k₂/Q = 0.003 gives about 0.38 W/m². Surface blackbody emission at 278 K is about 339 W/m², but the roughly 313 W/m² difference is not automatically an internal heat requirement: atmospheric insulation must bring actual top-of-atmosphere loss into balance. A grey Eddington optical-depth diagnostic gives the opacity scale required, not a computed molecular absorption, and it is not a solved climate. Hydrogen collision-induced absorption is a physical greenhouse mechanism outside a classical CO₂ habitable zone ([Pierrehumbert & Gaidos](https://arxiv.org/abs/1105.0021); [Ramirez & Kaltenegger](https://arxiv.org/abs/1702.08618)), but neither those models nor this arithmetic establish that this low-gravity moon and mixture give 278 K, and radiative transfer, cloud chemistry and H₂ escape and replenishment remain unverified; no artificial heating system is assumed. Laboratory radiation-associated fungal growth ([Dadachova et al. 2007](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0000457)) does not demonstrate a self-sufficient megafaunal radiation ecosystem, and radiolytic hydrogen has an independent microbial-energy basis ([measured radiolytic H₂ yield](https://www.sciencedirect.com/science/article/pii/S0016703704006271)).
""")

# ---------------------------------------------------------------- Glaciumite
tail("Glaciumite.md", """
## Physical basis

The idealized formula Y₃(NdF₆)·Si₃O₉ has a molar mass of 753.20 g/mol. Natural ⁸⁹Y is the only stable yttrium isotope ([NIST yttrium isotopic composition](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ascii=ascii&ele=Y)). Rare-earth-crystal quantum storage is a broad scientific analogue for the memory role, not a validation of this exact compound or its performance claims ([rare-earth-crystal optical quantum storage](https://www.nature.com/articles/s41534-022-00541-3)). The 20-hour extraction deadline protects metastable electronic and crystal ordering, and ordinary thermal cycling is not nuclear transmutation; weak background radiation comes from separately identified K-40- and Rb-87-bearing inclusions, and stabilization, argon containment and field treatment do not change half-lives. Electroluminescence, UV fluorescence, static corona, crack-related emission and acoustic release are separate effects, and the 3–5 m interference range is a fictional reference, not a universal cutoff.
""")

# ---------------------------------------------------------------- Life pages
tail("Life on Goku.md", """
## Physical basis

The planetary figures, atmosphere reference and satellite screens are on [[Goku]] and [[Aethonix System]] under Physical basis. The biology is a speculative scenario with no native sapient civilization.
""")
tail("Life on Lunara.md", """
## Physical basis

The energy accounting, atmosphere and warmth requirement for the biosphere are on [[Lunara]] under Physical basis. Radiolysis and rock reactions create separated reactants, with useful oxidants held in fluids, mineral interfaces or biological stores; direct melanin-like radiotrophy is supplementary and speculative. Total radionuclide inventories, usable yields, dose damage, repair and transport must support the ecological productivity. The Janusthropes are intelligent animals without a demonstrated sapient civilization.
""")

hist = re.compile(r"author|retire|former|formerly|\bold\b|older|supersed|original|reconcil|replaced|source’s|source's|revised", re.I)
for p in sorted(OUT):
    print("=== history-like words in", p)
    for n, line in enumerate(OUT[p].split("\n"), 1):
        if hist.search(line) and n > 18 and not line.startswith("|"): print(f"{n}: {line[:140]}")
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
