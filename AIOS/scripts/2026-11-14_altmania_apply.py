"""Staged edit for the Altmania records (dry run by default; --apply writes)."""
import sys, os, re
DRY = "--apply" not in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse/Altmania System")
def load(p): return open(p, encoding="utf-8").read()
OUT = {}
def sub(p, a, b):
    s = OUT.get(p) or load(p)
    assert s.count(a) == 1, (p, a[:70], s.count(a))
    OUT[p] = s.replace(a, b)

MARK = "## Reconciliation and research"
def tail(p, new):
    s = OUT.get(p) or load(p)
    assert s.count(MARK) == 1, p
    sect = s[s.index(MARK):]
    assert "Adopted design, calculation assumptions" in sect and len(sect) < 500, (p, len(sect))
    OUT[p] = s[:s.index(MARK)] + new.strip("\n") + "\n"

PAGES = ["Altmania", "Altmania System", "Azotia", "Iodulon", "Dunamas", "Thionis", "Neonova", "Nasia", "Dichlorans", "Life on Azotia", "Life on Iodulon", "Life on Neonova", "Life on Thionis"]
for pg in PAGES:
    sub(pg + ".md", "reconciled: 2026-11-12\n", "")

# ------------------------------------------------------------------ wording
sub("Altmania System.md", "| Age | 3 Gyr working common age (formerly 2–5 Gyr range) |", "| Age | 3 Gyr working common age |")
sub("Altmania System.md", "The two human colony worlds are Nasia and Dunamas; an earlier 0.85-AU site is a retired draft location, not an extra planet.", "The two human colony worlds are Nasia and Dunamas.")
sub("Altmania System.md", "A short Newtonian reference screen is documented in [[Altmania adopted reconciliation and calculations]]; no multi-gigayear integration is claimed.", "A short Newtonian reference screen is described under Physical basis; no multi-gigayear integration is claimed.")
sub("Altmania.md", "The original visual magnitude pairs were internally consistent with the distance modulus, but are not maintained as calibrated K-dwarf photometry without bolometric corrections.", "The visual magnitude pairs are internally consistent with the distance modulus, but are not calibrated K-dwarf photometry without bolometric corrections.")
sub("Azotia.md", "| 260 K (approximately −13 °C), revised warmer climate reference |", "| 260 K (approximately −13 °C) |")
sub("Azotia.md", "Thus warming removes the severe pure-fluid pressure mismatch of the old 205-K reference, while the actual", "The pure-fluid comparison is therefore compatible with the chosen mixture at this temperature, while the actual")
sub("Azotia.md", "neither the original 201-K equilibrium nor a mere four-kelvin greenhouse increment is retained. The change is a canon climate revision, not an invented recent warming event or human terraforming history.", "a 201-K equilibrium with a mere four-kelvin greenhouse increment would not reach it. The 260-K climate is not the result of a recent warming event or human terraforming history.")
sub("Azotia.md", "The revised global working mean is **260 K**", "The global working mean is **260 K**")
sub("Azotia.md", "Some Slushcrawler habitats retain the original approximately 200–230-K regional conditions.", "Some Slushcrawler habitats keep approximately 200–230-K regional conditions.")
sub("Azotia.md", "subject to the revised mixture/vapor-equilibrium model.", "subject to the mixture and vapor-equilibrium model.")
sub("Dunamas.md", "The original 340,000/160,000-km axes and unscreened 300,000/140,000-km prograde candidate are superseded. Opposite orbital directions and greater margin against stellar forcing preserve", "Opposite orbital directions and greater margin against stellar forcing preserve")
sub("Dunamas.md", " Periods and phase-specific short-screen results are in [[Altmania adopted reconciliation and calculations]].", " Wider prograde layouts produced escapes or large excursions in the screens. Periods and the short-screen results are under Physical basis below and on [[Altmania System]].")
sub("Dunamas.md", "The source's one-third-sized inner-moon appearance is retired. ", "")
sub("Dichlorans.md", "; the old universal 100× factor is retired.", ".")
sub("Nasia.md", "specified differing phases/nodes in the calculation artifact. The original mass/size/shape and prograde/retrograde characters remain; Kathy's refined tilt lies within the original >140° range. These revised axes supersede the unscreened 90,000/220,000/400,000-km candidates. Moon periods and short-screen outcomes are documented in [[Altmania adopted reconciliation and calculations]].",
    "differing phases and nodes in the screens. Each moon has a distinct mass, size, shape and orbital sense, and Kathy's tilt is above 140°, retrograde. A wider unscreened layout (90,000/220,000/400,000 km) produced escapes or large excursions. Moon periods and short-screen outcomes are under Physical basis below and on [[Altmania System]].")
sub("Life on Azotia.md", "The revised principal open-sea habitats", "The principal open-sea habitats")
sub("Life on Azotia.md", "atom-balanced kinetic network; the former unbalanced elementary expression is retired.`", "atom-balanced kinetic network.`")
sub("Life on Azotia.md", "## Revised habitat and redox reference", "## Habitat and redox reference")
sub("Life on Azotia.md", "The author approved warming to preserve ammonia-based life. The adopted mean is **260 K**, retaining NH₃-rich 3-atm air and extensive ammonia–water seas rather than imposing N₂ dominance at 205 K.", "The mean is **260 K**, with NH₃-rich 3-atm air and extensive ammonia–water seas.")
sub("Life on Azotia.md", "the 1.5–2.0-Gyr history is not replaced by a newly invented warming event.", "the 1.5–2.0-Gyr history includes no recent warming event.")
sub("Life on Iodulon.md", "access in corrosion-resistant craft; the earlier near-space description belongs to an earlier stage.", "access in corrosion-resistant craft.")
sub("Altmania System.md", "The adopted warmer reference is **260 K**", "The adopted reference is **260 K**")
sub("Iodulon.md", "Water is scarce and variable; the earlier 0.003–0.012-atm global-water prescription is retired.", "Water is scarce and variable.")

# ------------------------------------------------------------------ Physical basis
tail("Altmania.md", """
## Physical basis

**Location.** From the supplied J2000 position (RA 02h12m, Dec −11°) and 48-pc distance, an approximate standard heliocentric Galactic transformation gives l ≈ 176.398° and b ≈ −65.124°, hence X ≈ −20.15, Y ≈ 1.27 and Z ≈ −43.55 pc, with +X toward the Galactic center and +Z north. This is a rounded matrix calculation, not an Astropy execution; the frame is defined by [Astropy's Galactic frame](https://raw.githubusercontent.com/astropy/astropy/main/astropy/coordinates/builtin_frames/galactic.py) and [transform implementation](https://raw.githubusercontent.com/astropy/astropy/main/astropy/coordinates/builtin_frames/galactic_transforms.py).

**Stars.** The stellar lifetimes are rough, model-dependent estimates of tens of Gyr. The temperatures follow from the adopted radii and luminosities, and the visual magnitudes would need spectral bolometric corrections; matching a distance modulus is not an absolute-flux validation. Velora is a fictional sky designation, not an IAU constellation.

**Water zone.** A conservative one-Earth-mass water-zone comparison is about 0.324–0.610 AU for A and 0.453–0.839 AU for B ([Kopparapu et al.](https://arxiv.org/html/1404.5292v1)). A habitable-zone label is not an observed climate; the actual climate states are on the planet pages.
""")

tail("Altmania System.md", """
## Physical basis

**Moon layouts.** The selected layouts come from numerical screening:

| Host | Satellite | Mass | Axis | Inclination to planetary orbital plane | Initial e | Approximate Kepler period |
| --- | --- | --- | --- | --- | --- | --- |
| Iodulon | Unnamed small moon | 10⁻⁵ M⊕ | 80,000 km | 3°, prograde | 0.003 | 2.82 d |
| Nasia | Stephanie | 2.6×10⁻⁴ M⊕ | 50,000 km | 20°, prograde | 0.003 | 1.263 d |
| Nasia | Natia | 0.015 M⊕ | 150,000 km | 5°, prograde | 0.003 | 6.515 d |
| Nasia | Kathy | 1.5×10⁻⁵ M⊕ | 330,000 km | 175°, retrograde | 0.003 | 21.412 d |
| Dunamas | Minor moon | 0.3 lunar masses | 120,000 km | 175°, retrograde | 0.003 | 4.665 d |
| Dunamas | Major moon | 0.8 lunar masses | 260,000 km | 1°, prograde | 0.003 | 14.833 d |

A both-prograde Dunamian layout and a wider Nasian outer layout produced escapes, close approaches or large excursions in the screens, which is why the tighter, counter-orbiting arrangements are used; they are working references, not stability proofs. Iodulon's small moon has a working 160-km radius (density about 3.48 g/cm³), a newly specified parameter, not a measured object; its observatory and foundry need confined life support, managed volatile stocks and cold storage, and tidal stress modulation is distinct from an uncalculated dominant vent heat source. Dunamas's working moon radii at lunar density are 1613 and 1163 km, subtending about 0.71° (major) and 1.11° (minor); eclipse opportunities follow real conjunctions, planes and local visibility, and all six moon periods are sidereal Kepler comparisons, with stellar forcing producing osculating variations. The 14,000–20,000-km ring (2.09–2.98 planetary radii, young, ice-poor and rocky) keeps an inclined ringed appearance in a near-equatorial reference plane with latitude-dependent surface visibility; optical depth, particle size, mass, strength, spreading and drag, and outer moonlet accretion are unsolved, and no perpetual ring lifetime is assumed. The present 25-hour Nasia and Dunamas spins and the 20-hour Thionis spin rest on weak-dissipation working histories (k₂ ≈ 0.3 and an effective Q of order 10,000 are illustrative, not measured); retrograde tidal decay, stellar spin torques, moon migration and obliquity resonances need a full coupled evolution, and nothing in a short point-mass screen certifies a 3-Gyr moon system.

**Numerical screens.** The screens use Newtonian point masses in AU, year and solar-mass units with a fourth-order Yoshida composition of velocity-Verlet steps. They start from the supplied planetary masses, axes, eccentricities and reference inclinations, with planet and moon phases and nodes varied by integer seed, and conserve momentum through barycentric initialization while monitoring total energy and host-relative osculating elements.

- The eight-body binary-plus-six-planets screen survives 10,000 years in two phase cases (steps of 0.001 and 0.0005 yr); adjacent planets stay radially separated, and osculating eccentricity reaches about 0.095 for Iodulon, 0.069 for Nasia and 0.104 for Dunamas, so the supplied near-circular elements are epoch references, not fixed circular orbits.
- The star–planet–moon screens survive 3000 years in two phase cases for each Nasian and Dunamian layout. Nasia's outer moon Kathy is the most sensitive orbit, with a maximum sampled osculating e of about 0.307 (seed 0) and 0.444 (seed 1) and significant axis excursions; Dunamas's major moon reaches e of about 0.120–0.143 and its inner retrograde moon stays at e ≤ 0.013.
- The Iodulonian small-moon screen covers 300 years in two phase and step cases, and half-step 500-year runs for Nasia and Dunamas and the planetary screen keep the same qualitative survival and comparable orbital envelopes. Total relative-energy errors are about 10⁻¹⁰–10⁻¹², but energy is dominated by stellar binding, so that number does not replace checking the moon elements.

The eccentricities that vary in these runs belong in the eventual tidal and thermal evolution, not the frozen initial e = 0.003. The moon runs omit the binary companion, other planets, oblateness, tides, thermal and rheological feedback, collisions, relativity and external encounters, and the planetary runs omit moons and dissipation, so none of this extrapolates to 3 Gyr. Spin obliquities are not dynamical bodies in the screens. The empirical stability boundaries come from [Holman & Wiegert](https://arxiv.org/abs/astro-ph/9809315) and the satellite boundaries from [Domingos et al.](https://doi.org/10.1111/j.1365-2966.2006.11104.x).
""")

tail("Nasia.md", """
## Physical basis

Nasia's three moons are Stephanie (2.6×10⁻⁴ M⊕, 50,000 km, 20° prograde, 1.263 d), Natia (0.015 M⊕, 150,000 km, 5° prograde, 6.515 d) and Kathy (1.5×10⁻⁵ M⊕, 330,000 km, 175° retrograde, 21.412 d), each starting at e = 0.003. In the 3000-year star–planet–moon screens Kathy is the most sensitive orbit, reaching a maximum sampled osculating e of about 0.307 or 0.444 with significant axis excursions, so it is not a quiet circular or proven long-lived orbit. The present 25-hour spin rests on a weak-dissipation working history (illustrative k₂ ≈ 0.3 and Q of order 10,000), and Natia influences spin-axis precession without being assumed to fix the obliquity for billions of years. The screens are described on [[Altmania System]] under Physical basis, and a short screen does not certify a 3-Gyr moon system.
""")

tail("Dunamas.md", """
## Physical basis

Dunamas's major moon (0.8 lunar masses, 260,000 km, prograde, 14.833 d) and minor moon (0.3 lunar masses, 120,000 km, retrograde at 175°, 4.665 d) have working radii of 1613 and 1163 km at lunar density, subtending about 0.71° and 1.11°. The major moon's eccentricity reaches about 0.120–0.143 in the 3000-year screens while the inner retrograde moon stays at e ≤ 0.013, and these varying eccentricities belong in the eventual tidal and thermal evolution. The 14,000–20,000-km young, ice-poor rocky ring (2.09–2.98 planetary radii) has unsolved optical depth, mass, spreading and moonlet accretion. The present 25-hour spin rests on a weak-dissipation working history (illustrative k₂ ≈ 0.3 and Q of order 10,000). The screens and their limits are described on [[Altmania System]] under Physical basis.
""")

tail("Iodulon.md", """
## Physical basis

The 1.2-atm reference atmosphere is normalized to 30% HCl, 18% Cl₂, 9% HF, 26% SO₂, 16.48% N₂, 0.5% CO₂, 0.019% halocarbons and other gases and 0.001% H₂O; free F₂ is compartmentalized and transient, not 2% of the bulk air. At 240 K the specified SO₂ partial pressure is about 0.316 bar, close to the pure-fluid saturation comparison ([NIST SO₂](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7446095&Mask=4)). Cold nightward 230–240 K living belts, pressurized warmer caverns and vapor-retaining cells keep complete coral and hexapod life cycles possible, while warmer 270–330 K open terrain is largely inhospitable. Global cold trapping, chemistry and mixture activities are uncomputed, and fluorine chemistry has its own hazards ([NOAA fluorine chemistry](https://cameochemicals.noaa.gov/report?key=CH764)). The small moon has a working 160-km radius at a density of about 3.48 g/cm³, a newly specified parameter. The orbital screens are on [[Altmania System]] under Physical basis.
""")

tail("Thionis.md", """
## Physical basis

The 4-atm dry reference is 90% CO₂, 8% SO₂, 1.5% H₂S, 0.3% H₂ and 0.2% CH₄, and the SO₂ partial pressure of about 0.324 bar is close to the 240-K pure-fluid comparison ([NIST SO₂](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7446095&Mask=4)). Locally hydrated phases and gel media take the place of a bulk H₂SO₃-hydrate solvent, and acidity is solvent-specific, with aqueous pH comparisons restricted to aqueous compartments. Thiolipid assembly, thioester inheritance and disulfide strand control remain hypothetical. The spin and moon-system limits are on [[Altmania System]] under Physical basis.
""")

tail("Neonova.md", """
## Physical basis

Neonova is 4 M⊕ and 1.5 R⊕ with a 17-atm atmosphere. The seven gas fractions are a local hot and wet reference, not a globally uniform 4% water. H₂-rich pressure-balanced lift sacs provide the main lift; noble gases serve damping and control roles, with Ne giving modest lift at equal temperature and Ar negative lift in the listed mixture. A 23–26-day recirculating jet and vertical trajectory supports full life cycles. Geothermal H₂ and a speculative illuminated anoxygenic Fe(II)-to-Fe(III) regeneration guild power the net redox renewal, and the yields, water, carbon and iron transport and oxygen exclusion are unmodeled. The 5-S⊕ climate requires reflecting clouds and haze and an outgoing-energy model; 17 atm is not itself a cooling mechanism.
""")

tail("Azotia.md", """
## Physical basis

The normalized local atmospheric reference is NH₃ 57.5%, N₂ 39%, CH₄ 2.5%, H₂ 0.9%, H₂S 0.05%, water vapor 0.03%, CO₂ 0.005% and other minor gases 0.015%, with nitrates mainly dissolved or particulate and only trace gas-phase NOₓ; water, CO₂ and ammonia vary with condensation, reactions and vent input. The NIST Antoine coefficients for 239.6–371.5 K ([NIST NH₃](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7664417&Mask=4); [NIST N₂](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7727379&Mask=4)) give a pure-NH₃ saturation pressure of 2.546 bar at 260 K, and 57.5% of 3 atm is 1.748 bar, which requires an effective liquid ammonia activity near 0.687 in a simple vapor and fugacity comparison. This does not establish an ocean concentration: a nonideal NH₃–H₂O/salt model must supply the activity and a stable liquid domain, with the reduced water partial pressure needing the same validation ([experimental ammonia–water phase work](https://ntrs.nasa.gov/api/citations/19940031629/downloads/19940031629.pdf)). No pure N₂ fog is claimed; NH₃/H₂O droplets and ice are carried in the gas. At a mean flux of 0.38775 S⊕ and e = 0.10, a radiative-convective cloud, haze and greenhouse model must yield the 260-K target, and trace-gas opacity, scattering, NH₃ photolysis and ammonia and CO₂ salts remain physical model requirements.
""")

tail("Dichlorans.md", """
## Physical basis

No ordinary image-forming vision is required of the Dichlorans, but photochemical sensing and instrument optics are retained, and chemical and pigment language and symbolic archives are explicit. Durable glyphs have volatile-retaining hosts; TiCl₄ is a controlled precursor, not a warm solid blade. Ceramic firing needs heat separately from chlorine treatment, and controlled metal recovery supplies electrodes. Carried nonoxygen oxidants permit chemical ascent, and cold elemental-halogen expulsion is not automatically energetic monopropulsion; electric propulsion takes appropriate orbital roles. Exact rocket materials, fuels, thrust and exhaust performance remain engineering hypotheses. The planet and orbital figures are on [[Iodulon]] and [[Altmania System]].
""")

tail("Life on Iodulon.md", """
## Physical basis

All eight volisomes, the PS/PS₂ genetics, the sulfur–phosphonate scaffolds, the mineral and gel materials and the adaptive hexapod structures are speculative molecular architecture. The formate/ferric and methyl-halide/perchlorate balances are balanced equations, not feasibility proofs. The atmosphere and moon figures are on [[Iodulon]] under Physical basis.
""")

tail("Life on Thionis.md", """
## Physical basis

Thiolipid assembly, thioester inheritance and disulfide strand control are hypothetical. Formal repeat-unit digestion and schematic fermentation are kept separate from demonstrated respiration or energy yields. The solvent and atmosphere figures are on [[Thionis]] under Physical basis.
""")

tail("Life on Neonova.md", """
## Physical basis

Geothermal H₂ and a speculative illuminated anoxygenic Fe(II)-to-Fe(III) regeneration guild power the net redox renewal, and the actual yields, water, carbon and iron transport and oxygen exclusion remain to be modeled. The Great Methane Event stabilization reflects a powered source–sink network, not consumption of an infinite initial iron reservoir. The planetary figures are on [[Neonova]] under Physical basis.
""")

tail("Life on Azotia.md", """
## Physical basis

Balanced nitrate ammonification is CH₄ + NO₃⁻ + H⁺ → CO₂ + NH₃ + H₂O, with the ammonium convention CH₄ + NO₃⁻ + 2 H⁺ → CO₂ + NH₄⁺ + H₂O kept separate. Nitrogen fixation requires electron donors and work, photons do not replace escaped hydrogen atoms, and serpentinization, hydrothermal supply and finite volatile and mineral inventories enter the source–sink budget. The molecular equations are reference balances, not validated cold-ammonia enzymes. The atmosphere and vapor comparison are on [[Azotia]] under Physical basis.
""")

hist = re.compile(r"author|retire|former|formerly|\bold\b|older|supersed|original|reconcil|replaced|source's|source’s|revised", re.I)
for p in sorted(OUT):
    print("=== history-like words in", p)
    new = OUT[p]
    for n, line in enumerate(new.split("\n"), 1):
        if hist.search(line) and n > 18 and not line.startswith("|"): print(f"{n}: {line[:140]}")
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
