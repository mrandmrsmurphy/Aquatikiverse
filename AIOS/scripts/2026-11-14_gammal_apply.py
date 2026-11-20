"""Staged edit for the Gammal records (dry run by default; --apply writes)."""
import sys, os, re
DRY = "--apply" not in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse/Gammal System")
def load(p): return open(p, encoding="utf-8").read()
OUT = {}
def sub(p, a, b):
    s = OUT.get(p) or load(p)
    assert s.count(a) == 1, (p, a[:70], s.count(a))
    OUT[p] = s.replace(a, b)
def before(p, marker, new):
    s = OUT.get(p) or load(p)
    assert s.count(marker) == 1, (p, marker)
    OUT[p] = s.replace(marker, new.strip("\n") + "\n\n" + marker)

HUB, GM, DP, GY, SB = "Gammal System.md", "Gammal.md", "Dold-Pärla.md", "Gycklare.md", "Storebror.md"
LINK = "- [[Gammal calculation and reconciliation notes]]\n"

# ------------------------------------------------------------------ hub wording
sub(HUB, "numerical labels should follow the reconciled values below.", "numerical labels should follow the values below.")
sub(HUB, "The author approved correction of the planetary arithmetic, retention of the huge planetary sky and short lunar cycle, predominantly refractory rings, a less exposed outer-satellite layout, and a strong but physically qualified magnetic umbrella.", "The system keeps the huge planetary sky and short lunar cycle, predominantly refractory rings, a less exposed outer-satellite layout, and a strong but physically qualified magnetic umbrella.")
sub(HUB, "The current moon eccentricity is **0.003**, a modest reduction from 0.005.", "The current moon eccentricity is **0.003**.")
sub(HUB, "| **Approximately 5.3 kpc**, replacing the source’s 3 kpc |", "| **Approximately 5.3 kpc** |")
sub(HUB, "The original `noknown_stars=yes` template flag is superseded by the explicit one-star inventory.", "The system has one known star.")
sub(HUB, "The small temperature revision brings radius and luminosity into agreement. The inherited absolute/apparent magnitudes and extinction are arithmetically consistent;", "The radius, temperature and luminosity agree. The absolute and apparent magnitudes and extinction are arithmetically consistent;")
sub(HUB, "the source’s 670-K or >900-K values can only be modeled layer temperatures, not unqualified equilibrium values.", "layer temperatures of 670 K or above 900 K are possible in a model but are not unqualified equilibrium values.")
sub(HUB, "Revised density is **2.05 g/cm³**", "The density is **2.05 g/cm³**")
sub(HUB, "The updated **89.8°** observer inclination allows the intended transit, whereas the old 88° geometry did not.", "The **89.8°** observer inclination allows the intended transit; 88° would not.")
sub(HUB, "Full setup, results, analytic branch and limitations are in [[Gammal calculation and reconciliation notes]].", "The setup and results are under Physical basis.")
sub(HUB, "The author’s sequence ends in **evacuation after the human era**.", "The sequence ends in **evacuation after the human era**.")
sub(HUB, "The supplied article records the inhabited-world era; the current text does not imply", "The article records the inhabited-world era; it does not imply")
sub(HUB, "## Remaining homework", "## Open modeling tasks")
sub(HUB, "All supplied material is transferred or explicitly superseded. The remaining work is quantitative modeling or unspecified narrative detail, rather than missing arithmetic:", "The open work is quantitative modeling or unspecified narrative detail:")
sub(HUB, "define the old map coordinate basis", "define the map coordinate basis")
sub(HUB, "Existing illustrations are retained, but their diagrams", "Existing illustrations are conceptual, and their diagrams")
sub(HUB, "; update any old labels to the adopted values if present.", ".")
sub(HUB, LINK, "")
sub(HUB, "- [[Gammal reconciliation review|Historical evaluation]]\n", "")

before(HUB, "## See also", """
## Physical basis

The calculations support arithmetic consistency and expose physical requirements. They do not prove a four-billion-year habitable system or explain the unexplained human arrival and later evacuation. The two major planets are separated by about 9.3 mutual Hill radii in a near-circular coplanar reference, which is a screen, not a long-term stability proof. The stellar, giant, moon and climate calculations are on [[Gammal]], [[Storebror]], [[Dold-Pärla]] and [[Gycklare]] under Physical basis.

**Four-body screen.** A separate Newtonian screen includes Gammal, Gycklare, Storebror and Dold-Pärla, in units of AU, Julian years and solar masses (G = 4π²), with masses of 0.82, 6.3×3.0034896×10⁻⁶, 2.2×0.0009545942 and 0.9×3.0034896×10⁻⁶ M☉ (these rounded conversions differ slightly from the SI constants and do not change the narrative precision). The initial axes and eccentricities are Gycklare 0.22 AU / 0.005, the giant–moon barycenter 0.572 AU / 0.005 and the moon 480,000 km / 0.003; the planets are coplanar, the moon is inclined 5° and the giant has no modeled spin quadrupole. The seeds j = 0, 1, 2 use planetary mean anomalies of 0.4 + 0.734j and 1.7 + 0.411j radians and a lunar mean anomaly of 2.3999632297j radians, with the giant–moon subsystem initialized about its barycenter and the whole system shifted to zero barycentric position and velocity. The integration uses direct pair gravity with a fourth-order symmetric velocity-Verlet composition (w₁ = 1/(2 − 2^(1/3)), w₀ = −2^(1/3)/(2 − 2^(1/3))) at a main step h = 10⁻⁵ yr, sampling radius and eccentricity every 25 steps and the total-energy error every 2,500 steps. The run stops if the moon–planet separation falls below 250,000 km or rises above 900,000 km, a conservative local screen, not the actual Roche or Hill boundary.

| Seed / interval | Sampled moon separation (km) | Maximum osculating e | Maximum relative total-energy error |
| --- | --- | --- | --- |
| 0 / 100 yr | 478,377–481,686 | 0.003579 | 6.5×10⁻¹³ |
| 1 / 100 yr | 478,375–481,511 | 0.003398 | 7.5×10⁻¹³ |
| 2 / 100 yr | 478,519–481,472 | 0.003205 | 6.2×10⁻¹³ |
| 0 / 25 yr, original step | 478,384.740–481,678.020 | 0.003564830 | 5.6×10⁻¹³ |
| 0 / 25 yr, half step | 478,384.598–481,678.321 | 0.003564823 | 9.8×10⁻¹³ |

No termination threshold was crossed. The step comparison gives consistent short-interval radius and eccentricity scales, but it is not a formal long-term convergence result, and the osculating eccentricity includes forced variations, so it should not be inserted directly into an averaged heat formula. The screen excludes all other moons, ring gravity and collisions, J₂ and spin, tides, migration, stellar evolution, Galactic encounters, radiation and climate. It supports only the selected geometry; it does not certify Trasp, eleven-moon stability, four Gyr of orbital survival or a four-Gyr biosphere.
""")

# ------------------------------------------------------------------ Gammal (star)
sub(GM, "The small change from 4900 to approximately 4960 K makes L/R/T mutually consistent to the intended precision. The source’s K2V label remains approximate,", "A temperature of approximately 4960 K makes L, R and T mutually consistent to the intended precision. The K2V label is approximate,")
sub(GM, "The old 3-kpc Galactocentric value is superseded. ", "")
sub(GM, "The main index’s old Earth-frame tuple (3000,260,0) is an archival map annotation with undefined axes/units, not a competing measured position. The source’s 2° inclination is retained as an approximate **Galactic orbit-plane** setting parameter,", "The main index's Earth-frame tuple (3000,260,0) is a map annotation with undefined axes and units, not a measured position. A 2° inclination is an approximate **Galactic orbit-plane** setting parameter,")
sub(GM, "; the original 0.45–0.75-AU band is not retained as a calculated conservative boundary.", ".")
sub(GM, LINK, "")
before(GM, "## Further reading", """
## Physical basis

**Constants.** The calculations use G = 6.67430×10⁻¹¹ SI, M☉ = 1.98847×10³⁰ kg, M♃ = 1.89813×10²⁷ kg, M⊕ = 5.9722×10²⁴ kg, R☉ = 695,700 km, R♃ = 71,492 km, R⊕ = 6,371 km, AU = 149,597,870.7 km, L☉ = 3.828×10²⁶ W, σ = 5.670374419×10⁻⁸ SI and a 365.25-day year; rounded narrative values are not precise measurements. Bulk quantities follow ρ = 3M/(4πR³), g = GM/R², v_esc = √(2GM/R), a spherical area 4πR² and a volume 4πR³/3.

**Star.** The Stefan–Boltzmann relation T = 5772 K × (0.34/0.79²)^¼ gives about 4,959 K. Photometry m = M + 5 log₁₀(d/10 pc) + Av gives 20.10–21.60 for Mv = 6.21, d = 3,000 pc and Av = 1.5–3.0. For a sightline near the Galactic Center, an Earth distance of about 3 kpc and a solar Galactocentric radius of about 8.3 kpc imply roughly 5.3 kpc from the center.

**Orbits and transits.** For near-circular motion P = 2π√[a³/G(M+m)] and v = √[G(M+m)/a], and the stellar radial-velocity semi-amplitude is √(G/a) m sin i / √(M+m), with a negligible eccentricity correction at e = 0.005. A transit requires |a cos i| ≲ R★ + R_body in the circular reference: Storebror needs approximately i > 89.58°, so 88° would not work, and the adopted 89.8° also permits Gycklare's transit. The stellar inclination, giant spin obliquity, moon-equatorial inclination and Galactic orbit inclination are distinct.

**Habitable-zone context.** A roughly 0.58–1.05 AU terrestrial habitable-zone polynomial at this stellar temperature is context only, not a climate result.
""")

# ------------------------------------------------------------------ Storebror
sub(SB, "| Property | Reconciled reference |", "| Property | Reference |")
sub(SB, "The source’s 1.1-g/cm³ density, 26.4-m/s² gravity, 60-km/s escape speed and 25-m/s RV amplitude are superseded. “Saturn-like”", "“Saturn-like”")
sub(SB, "With the fast spin, the original flattening 0.025 is too small in a simple positive-J₂ hydrostatic estimate;", "With the fast spin, a flattening of 0.025 would be too small in a simple positive-J₂ hydrostatic estimate;")
sub(SB, "This dials back the source’s unspecified factor of fifteen but preserves a substantial difference from Earth:", "This preserves a substantial difference from Earth:")
sub(SB, "The original assertion that ancient exposed ice is automatically replenished by an unusually violent Galactic environment is retired.", "Ancient exposed ice is not assumed to be automatically replenished by an unusually violent Galactic environment.")
sub(SB, "The source’s nearly polar Trasp at 5.2 million km and e=0.41 is retired as a long-lived working orbit. Its later fuller appearance as a distant irregular is preserved with a more compact, lower-eccentricity retrograde candidate.", "Trasp is a distant irregular on a compact, lower-eccentricity retrograde candidate orbit; a nearly polar orbit at 5.2 million km with e = 0.41 would not be long-lived.")
sub(SB, "The source moon’s eccentricity is reduced modestly from 0.005 to **0.003**, rather than to the review’s 0.0003–0.001 proposal. Its associated heat, damping and possible recent excitation are discussed on [[Dold-Pärla]] and [[Gammal calculation and reconciliation notes]].", "The moon's eccentricity is **0.003**. Its associated heat, damping and possible recent excitation are discussed on [[Dold-Pärla]] and under Physical basis below.")
sub(SB, LINK, "")
before(SB, "## See also", """
## Physical basis

**Oblateness.** For Storebror's fast spin, q = Ω²R³/(GM) ≈ 0.0565 using its mean-radius reference. The first-order hydrostatic relation f ≈ q/2 + 3J₂/2 would need a negative J₂ for f = 0.025, so f ≈ 0.04 and J₂ ≈ 0.008 are approximate positive-J₂ targets. This does not solve a self-consistent rotating figure, and using the equatorial radius shifts it slightly.

**Sky from the moon.** A 5° giant obliquity, a nearly equatorial satellite and a small forced Laplace-plane adjustment preserve an equatorial orbit together with a several-degree mutual tilt to the star's plane. Storebror's angular diameter, 2 asin(R_planet/a_moon), is about 18.86°, in a nearly fixed direction for a synchronous moon. The prograde stellar cycle, 1/(1/P_moon − 1/P_planet), is about 1.4598 days against an orbital period of 1.4477 days. A central point-source eclipse, 2 asin(R_planet/a_moon)/(n_moon − n_planet), lasts about 1.835 hours, roughly 5.24% of the stellar cycle; off-center crossings, the finite stellar disk and moon, and observer latitude change the partial and total contact durations, so the roughly 1.6-hour substantial eclipse is not identical at every site. The rings are nearly edge-on from the moon's near-equatorial vantage; surface parallax, warp and small orbital inclination let a narrow presentation vary, but a wide open ring ellipse is not a permanent naked-eye view. Reflected planetshine changes with phase even though the planet's position is fixed.

**Tidal branch.** The requirement is about 4 Gyr of native biological persistence, not 9.5 Gyr at one exact axis. For a primary spinning faster than the satellite, a simple constant-Q approximation is da/a = 3(k₂p/Qp)(M_m/M_p)(R_p/a)⁵ n dt; with fixed primary spin and radius n ∝ a^(−3/2), so da/dt ∝ a^(−11/2) and a(t_lookback) = a_now [1 − (13/2) t_lookback/τ_a,now]^(2/13). Adopting Qp/k₂p = 3×10⁷, a_now = 480,000 km and the adopted masses and radius gives a local timescale of about 41.5 Gyr, and a four-Gyr lookback gives approximately 412,600 km. This response is unusually weak compared with the giant-planet values inferred at some observed satellite frequencies, so it is a requirement to justify a frequency-dependent interior model, not a value inferred from the star, the strong field or the wish for four-Gyr survival. Fixed spin and radius, omitted stellar torques and other moons, and a simplified Q prescription all limit the branch, which does not solve initial capture or formation, pre-biological history, giant evolution or a changing climate; frequency-dependent tides can differ strongly, but that does not validate the selected weak response.

The moon's synchronous eccentricity-tide reference is P_tidal = (21/2)(k₂m/Qm) G Mp² Rm⁵ n e² / a⁶. For e = 0.003 and k₂m/Qm = 3×10⁻⁴ the surface-mean heat is 2.39 W/m², and varying the lunar response from 10⁻⁴ to 10⁻³ gives about 0.8–8 W/m², a response sensitivity, not a measured Q. The corresponding eccentricity-damping scale, (2/21)(Qm/k₂m)(Mm/Mp)(a/Rm)⁵/n, is about 0.81 Myr, so the present excitation need not have persisted unchanged through four Gyr; recent forcing could coexist with the Archive anomalies, but no causal event is assigned. The giant and the moon have different response parameters: a large magnetic field does not establish weak tidal loss, and lunar heat can be significant while the giant's response is weak, but maintaining that heat for long intervals needs an eccentricity and energy source. Neither a recent massive orbital relocation nor its unaccounted energy deposition is assumed. Context: [Barnes & O’Brien (2002)](https://arxiv.org/abs/astro-ph/0205035), [Fuller et al. (2016)](https://academic.oup.com/mnras/article/458/4/3867/2613868) and [Lainey et al. (2009)](https://www.nature.com/articles/nature08108) motivate caution, and none validates Storebror's adopted response.

**Magnetic umbrella.** The giant's equatorial field of 3 mT gives a pure-dipole field of about 13.2 μT at 480,000 km, and a reference magnetopause at 30 R_p corresponds to an external magnetic-equivalent pressure B_s²/(30⁶·2μ₀) ≈ 4.9 nPa. These are pressure and dipole scales, not a magnetodisk, current or transport model. The moon's own 30-μT surface reference and one-bar atmosphere add shielding, its low surface dose is an adopted observational premise to be reproduced, and trapped belts and high-energy photons and particles need separate modeling ([Heller & Zuluaga](https://arxiv.org/abs/1309.0811)). The relative prograde magnetic-pattern period, 1/(1/9.7 h − 1/34.744 h) ≈ 13.46 h, differs from the stellar cycle, and field geometry, current coupling and particle access determine whether it produces a strong biological signal.
""")

# ------------------------------------------------------------------ Dold-Pärla
sub(DP, "| Antiquity, by direct local observation; the source’s “indigenous observation” metadata |", "| Antiquity, by direct local observation |")
sub(DP, "The mass/radius imply the revised gravity and escape speed; they supersede the source’s 9.3-m/s² and 10.6-km/s values.", "The mass and radius imply the gravity and escape speed.")
sub(DP, "The newer equatorial-orbit description is preserved without losing the earlier small inclination to the **star’s** plane: those are different reference planes.", "The moon's orbit is nearly equatorial for Storebror while having a small inclination to the **star’s** plane: those are different reference planes.")
sub(DP, "The source’s 1.28-day period does not match the retained 480,000-km axis and corrected primary mass.", "A 1.28-day period would not match the 480,000-km axis and the primary's mass.")
sub(DP, "the short numerical screen in [[Gammal calculation and reconciliation notes]] does not include every moon.", "the short numerical screen on [[Gammal System]] under Physical basis does not include every moon.")
sub(DP, "The author’s sequence is **native biosphere", "The sequence is **native biosphere")
sub(DP, "The supplied fuller article describes the inhabited era; the evacuation is a later author-specified event.", "The article describes the inhabited era; the evacuation is a later event.")
sub(DP, LINK, "")
before(DP, "## See also", """
## Physical basis

At 0.572 AU the stellar flux is F = L/(4πa²) ≈ 1414.5 W/m². For Dold-Pärla's Bond albedo of 0.32 and the central eclipse reference, the global-mean illustration is:

| Contribution | Global-mean illustration |
| --- | --- |
| Absorbed direct star | about 227.9 W/m² |
| Storebror thermal emission | about 1.54 W/m² |
| Absorbed reflected planetshine | about 0.61 W/m² |
| Lunar eccentricity tides | about 2.39 W/m² (response specified on [[Storebror]]) |
| Other interior heat | 0.08 W/m², an illustrative background, not a solved interior flux |
| Total | about 232.5 W/m² |

The planet's thermal input uses a uniform 252-K equilibrium globe and disk dilution, divided by four for the lunar area. Reflection uses an illustrative Lambertian globe with a geometric albedo of 0.35/1.5 ≈ 0.233, a full-phase scale A_g F (R_p/a)², a mean phase factor of 4/π², a lunar area factor of 1/4 and a lunar absorption of 0.68. Rings, thermal bandpass absorption, real cloud anisotropy and partial shadowing are omitted. For the Lambertian reference the phase integral is 1.5, so a geometric albedo of 0.233 is paired with a Bond albedo of 0.35 to conserve reflected and absorbed power; the real cloud phase function can differ.

The effective emission temperature is about 253 K, and an approximately 35-K greenhouse would connect it to the 288-K surface reference. This is a target budget, not a radiative-convective or circulation solution: the tilted geometry changes the eclipse duty, and ocean and cloud feedbacks could alter the result substantially ([Heller & Barnes 2013](https://arxiv.org/abs/1209.5323)).
""")

# ------------------------------------------------------------------ Gycklare
sub(GY, "The derived bulk quantities replace the incompatible source density, area, volume and escape speed. A heavy-element-dominated interior with a smaller H/He mass fraction is the starting model, rather than the source’s unsupported claim of ≤40% core and ≥60% envelope.", "The bulk quantities are derived from the mass and radius. A heavy-element-dominated interior with a smaller H/He mass fraction is the starting model; a core of ≤40% with a ≥60% envelope is not supported.")
sub(GY, "The earlier assertion of efficient redistribution and a fixed >900-K/<300-K contrast is replaced by a **pressure-dependent circulation model to be determined**.", "Heat redistribution and the day–night contrast need a **pressure-dependent circulation model, still to be determined**; efficient redistribution and a fixed >900-K/<300-K contrast are not assumed.")
sub(GY, "The original **7×10¹³ kg/year** is now an **uncertain high-state estimate**, not an established continuous loss rate across 9.5 Gyr. The overview’s earlier 10¹²-kg/year value is likewise not adopted without an XUV model.", "A loss of **7×10¹³ kg/year** is an **uncertain high-state estimate**, not an established continuous loss rate across 9.5 Gyr, and a 10¹²-kg/year value likewise needs an XUV model.")
sub(GY, "the source’s spectral detail is an in-setting interpretation", "the spectral detail is an in-setting interpretation")
sub(GY, LINK, "")
sub(GY, "The source’s habitable-zone category is retained in provenance but superseded in physical classification. The original reference-list template was empty; external interior models are illustrative rather than evidence for fictional detections.", "")
before(GY, "## See also", """
## Physical basis

The 414-K full-redistribution equilibrium uses a Bond albedo of 0.3 and is a reference, not a surface temperature: the weather and spectrum are a pressure-dependent problem, and the high escape rate needs an XUV history and cannot be derived from optical brightness alone. External interior models are illustrative rather than evidence for fictional detections.
""")

hist = re.compile(r"author|retire|former|formerly|\bold\b|older|supersed|source’s|source's|original|reconcil|homework|replaced", re.I)
for p in sorted(OUT):
    print("=== history-like words in", p)
    for n, line in enumerate(OUT[p].split("\n"), 1):
        if hist.search(line) and n > 17 and not line.startswith("|"): print(f"{n}: {line[:150]}")
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
