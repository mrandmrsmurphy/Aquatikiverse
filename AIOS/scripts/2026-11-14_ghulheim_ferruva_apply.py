"""Staged edit for the Ghulheim–Ferruva records (dry run by default; --apply writes).
Folds the calculation notes into Physical basis sections, scrubs history wording,
relinks, and leaves the two record pages for deletion by hand."""
import sys, os, re
DRY = "--apply" not in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse/Ghulheim–Ferruva system")
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

HUB, GH, FE, LF = "Ghulheim and Ferruva.md", "Ghulheim.md", "Ferruva.md", "Life on Ferruva.md"

# ------------------------------------------------------------------ hub wording
sub(HUB, "The later, fuller planet and biosphere accounts govern this reconciliation. The author approved a cool brown dwarf, a geothermal foundation for the liquid habitat, geological hemispheric contrast, PFC-bearing carrier fluids with unresolved biosynthesis, separate historical clocks, and corrected metabolic accounting. The result is an adopted speculative working model with explicit quantitative homework, not a demonstrated habitable nuclear-cluster system.",
    "The later, fuller planet and biosphere accounts govern the details. The model rests on a cool brown dwarf, a geothermal foundation for the liquid habitat, geological hemispheric contrast, PFC-bearing carrier fluids with unresolved biosynthesis, separate historical clocks and consistent metabolic accounting. It is an adopted speculative working model with explicit open modeling tasks, not a demonstrated habitable nuclear-cluster system.")
sub(HUB, "The source’s Monoceros coordinates, 2,000-pc Earth distance and 15,000-year outer period are superseded. ", "")
sub(HUB, "The old **10⁵ stars/pc³** density is retained only as an **unverified source-order environmental parameter**,", "A density of **10⁵ stars/pc³** is an **unverified order-of-magnitude environmental parameter**,")
sub(HUB, "The source’s **0.17 W/m² ambient cluster IR** figure remains an unverified illustrative background", "An **ambient cluster IR flux of 0.17 W/m²** is an unverified illustrative background")
sub(HUB, "visible shadows from ordinary Sgr A* flares are retired pending a calibrated visible spectrum.", "visible shadows from ordinary Sgr A* flares need a calibrated visible spectrum.")
sub(HUB, " preserving its approximately **1050-K** infrared identity while revising the mass and radius.", " giving it an approximately **1050-K** infrared identity.")
sub(HUB, "The old **L9pec δ** designation is retired; the precise subtype is unspecified and δ is not a high-gravity suffix.", "The precise spectral subtype is unspecified, and δ is not a high-gravity suffix.")
sub(HUB, "An encounter disrupts the original host-star architecture", "An encounter disrupts the ancestral host-star architecture")
sub(HUB, "modulate conditions; the old permanent hemisphere shielding is retired.", "modulate conditions, and no permanent hemisphere shielding is assumed.")
sub(HUB, "## Remaining research homework", "## Open modeling tasks")
sub(HUB, "No equation-balancing work is required from the author. Chemical accounting has been repaired; the substantive remaining tasks are:", "The written reactions conserve atoms and charge; the substantive open tasks are:")
sub(HUB, "construct the original K-star/dwarf/moon architecture", "construct the ancestral K-star/dwarf/moon architecture")
sub(HUB, "verify or replace the source’s 10⁵-stars/pc³ and 0.17-W/m² background figures", "verify or replace the 10⁵-stars/pc³ and 0.17-W/m² background figures")
sub(HUB, "- [[Ghulheim–Ferruva calculation notes]]\n", "")
sub(HUB, "- [[Ghulheim–Ferruva reconciliation review|Historical reconciliation review]]\n", "")

before(HUB, "## See also", """
## Physical basis

**Constants.** The calculations use G = 6.67430×10⁻¹¹ SI, M☉ = 1.98847×10³⁰ kg, M♃ = 1.89813×10²⁷ kg, M⊕ = 5.9722×10²⁴ kg, R☉ = 695,700 km, R♃ = 71,492 km, R⊕ = 6,371 km, AU = 149,597,870.7 km, pc ≈ 206,264.806 AU, L☉ = 3.828×10²⁶ W, σ = 5.670374419×10⁻⁸ SI and a 365.25-day year. Rounded adopted references do not imply that their input constants or physical models are exact.

**Orbit and illumination.**

- The two-body period P = 2π√(a³/[G(M+m)]) is about 16.956 days for Ferruva's a = 0.05 AU and Ghulheim's 0.058 M☉, with the small satellite mass included.
- Ghulheim's angular diameter, 2 asin(R/a), is about 0.861°; its direction is nearly fixed for synchronous Ferruva, while its bands rotate.
- The satellite sits at a/R ≈ 133.1 dwarf radii, beyond a hypothetical magnetopause at tens of radii; intermittent tail connectivity is possible, not demonstrated.
- The relative prograde magnetic-pattern period, 1/|1/P_spin − 1/P_orbit|, is about 5.062 hours for a 5-hour spin, assuming aligned prograde motion and nonaxisymmetric structure; the arithmetic does not establish the field geometry or any biological forcing.
- The normal incident flux F = L/(4πa²) is about 3.922 W/m², the spherical mean before reflection F/4 is about 0.980 W/m², and a zero-albedo uniform-emission reference, (F/[4σ])^¼, is about 64.5 K, which is not a local surface or brine temperature.
- At 0.05 pc, isotropic luminosities of 10²⁹ W bolometric and 10²⁶ W X-ray from Sgr A* imply 0.00334 W/m² and 3.34 μW/m². These are different bands and power references: actual high-energy dose needs spectra and transport, and the local stellar and dust field is not included.

**Galactic orbit and survival.** Kepler scaling for a = 0.05 pc around about 4.3×10⁶ M☉ gives a period of 505 years; for the adopted outer eccentricity of 0.05 the pericenter is 0.0475 pc. This neglects extended stellar mass, encounters, relativistic corrections and evolving orbit elements. A Hill screening, r_H ≈ r_peri [M_dwarf/(3 M_BH)]^(1/3), gives about 16.2 AU at pericenter, or 17.0 AU for the circular 0.05-pc reference, so Ferruva's 0.05 AU is about 0.0031 of the pericenter scale. This is a screen, not an integration or a proof of 7-Gyr survival. Eccentric orbits change the flux with distance, and exact directions, occultations and time-dependent spectra are not supplied by these mean calculations. The real black-hole mass and distance and the observing sources are on [[Sagittarius A*]].

**Limits.** These are reproducible analytic references, not an orbital simulation, an atmospheric retrieval or a coupled habitat model.
""")

# ------------------------------------------------------------------ Ghulheim
sub(GH, "This replaces the original 0.075-M☉ reference, which was problematic for a cool, old, metal-rich brown dwarf near the metallicity-dependent hydrogen-burning boundary.", "A 0.075-M☉ mass would sit at the metallicity-dependent hydrogen-burning boundary and risk being a very-low-mass star, so a lower mass suits a cool, old, metal-rich brown dwarf.")
sub(GH, "The original **L9pec δ** designation is retired. The δ gravity suffix belongs", "A δ designation would be wrong: the δ gravity suffix belongs")
sub(GH, "approximately **0.86°**, rather than the original 6°. It remains", "approximately **0.86°**. It remains")
sub(GH, "The supplied **Ghulheim spectral energy diagram.png**, captioned “Synthetic spectral energy distribution diagram,” is unavailable locally. A future diagram should use the reconciled reference and clearly identify any schematic spectrum.",
    "A spectral energy distribution diagram is not yet available; a future diagram should use this reference and clearly identify any schematic spectrum.")
sub(GH, "Published rows and the interpolation are documented in [[Ghulheim–Ferruva calculation notes]]. This is a reference cooling trajectory, not a fit to an observed object or a reconstruction of its encounters and accretion events.",
    "The reference uses selected **+0.5 metallicity, solar-C/O, 0.058-M☉** rows of the Sonora Bobcat tables ([Marley et al. 2021](https://arxiv.org/abs/2107.07434)), read from the plain-text SEDA mirror with columns M/M☉, age, log L/L☉, Teff, log g and R/R☉. Values at 3.5, 5, 6.5 and 7 Gyr use independent linear-in-age interpolation of the tabulated log luminosity, temperature, log gravity and radius, with no extrapolation, so the interpolated columns need not obey every nonlinear relation exactly. At 7 Gyr this gives a mass of 0.058 M☉ ≈ 60.76 M♃, Teff = 1052.5 K, R = 0.0808 R☉ ≈ 0.7863 R♃, log g = 5.3855, log L/L☉ = −5.1425 and L ≈ 7.203×10⁻⁶ L☉, which the page rounds to about 1050 K, 0.79 R♃ and 7.2×10⁻⁶ L☉. The cloudless, isolated-model assumptions and rounding limit the precision. This is a reference cooling trajectory, not a cloud spectrum, a fit to an observed object or a reconstruction of its encounters and accretion events, and no separate L9 or low-gravity spectral assignment is made.")

# ------------------------------------------------------------------ Ferruva
sub(FE, "| About 7 Gyr; narrows the original 5–9 Gyr range |", "| About 7 Gyr |")
sub(FE, "the original 0.17-W/m² IR figure remains an unverified illustrative background", "an ambient 0.17-W/m² IR figure is an unverified illustrative background")
sub(FE, "some original ocean water remains buried.", "some of the ocean water remains buried.")
sub(FE, "- [[Ghulheim–Ferruva calculation notes]]\n", "")
sub(FE, "The overview’s [[Ghulheim and Ferruva#Remaining research homework|research homework]] lists the quantitative models still needed. Balanced reaction examples are on [[Life on Ferruva]]; none require the author to supply missing stoichiometry.",
    "The overview's [[Ghulheim and Ferruva#Open modeling tasks|open modeling tasks]] list the quantitative models still needed, and balanced reaction examples are on [[Life on Ferruva]].")
before(FE, "## See also", """
## Physical basis

**Bulk.** For 0.8 M⊕ and 0.95 R⊕ the density is 5.144 g/cm³, the gravity 8.705 m/s² (0.886 g) and the area 460.3 million km², so fifty equal-area plates would average 9.21 million km² (actual plate sizes and speeds are setting assumptions). The geothermal reference of 0.08 W/m² corresponds to about 3.68×10¹³ W in total; it is a design input that needs an old-planet heat model, not something inferred from density or core enrichment.

**Ice column.** For a one-dimensional, steady, conductive, pure-ice comparison with k(T) = 651/T W/(m K) (an illustrative approximation, from the ice-shell discussion in [Hand 2007](https://cchyba.scholar.princeton.edu/sites/g/files/toruqf3881/files/documents/Kevin%20Hand%20thesis_2007.pdf)), integrating q = k(T) dT/dz gives d = (651/q) ln(T_interface/T_surface). With T_interface = 260 K, T_surface = 70 K and q = 0.08 W/m², d ≈ 10.68 km. This interface temperature is separate from the proposed 275–300 K hydrothermal liquid compartments: pressure and salinity melting behavior must justify the real boundary, since pure ice cannot remain solid against arbitrarily hot liquid. A constant k = 2 W/(m K) gives d ≈ 4.75 km for the same temperatures and flux, which shows the conductivity sensitivity; neither comparison fixes a unique shell thickness, and minerals, porosity, convection, cracks, advection and varying heating can change it. A nominal 10-km, 920-kg/m³ ice column gives ρgh ≈ 80.1 MPa before denser cap minerals, topography and pore-pressure structure, and overburden pressure is not automatically fluid pressure in every compartment. The biology–mineral cap is tens to hundreds of meters thick, but the Lid as a complete roof includes kilometer-scale insulation and supports, and a pressure, heat and support model must also account for the water inventory and persistent circulation. A cold exterior is compatible with a warm insulated interior; there is no global warm exposed sea.

**Tides.** For a nearly synchronous low-eccentricity satellite, P_tidal = (21/2)(k₂/Q) G M_dwarf² R_moon⁵ n e² / a⁶. With e = 0.001 and k₂/Q = 10⁻³ this gives about 4.0×10⁻⁶ W/m² at the present reference, assuming a simplified equilibrium response and omitting obliquity, frequency dependence, primary tides, perturbed motion and thermal feedback; the assigned eccentricity is not evidence of rapid circularization. The small-e damping timescale, (2/21)(Q/k₂)(m/M)(a/R)⁵/n, is of order 84 Gyr, while a constant-response spin-down estimate (moment coefficient 0.33, initial 24-hour spin) is much shorter, of order a million years. Synchronization and circularization cannot be equated, and a satellite formed or captured closer in, or one that retained low excitation, needs a complete evolution model to connect to the present orbit.
""")

# ------------------------------------------------------------------ Life on Ferruva
sub(LF, " Its original “sealed thermodynamic system” and energy-amplifying IR relay explanations are replaced: the ecosystem is **energetically open**, exchanging heat, radiation and interior chemistry.", " The ecosystem is **energetically open**, exchanging heat, radiation and interior chemistry.")
sub(LF, "| Property | Reconciled description |", "| Property | Description |")
sub(LF, "The original equation converting uranyl to bare U⁶⁺ plus an electron is retired: uranyl already contains uranium(VI), and that expression lost oxygen and charge. An atom/charge-consistent **schematic sensitizer sequence** is:", "Uranyl already contains uranium(VI), so it is not an oxidation-state pair with a bare U⁶⁺ ion. An atom- and charge-consistent **schematic sensitizer sequence** is:")
sub(LF, "Thermal IR can affect reaction kinetics, but the former “H₂O + IR → PCET activation” expression is removed as an energy source.", "Thermal IR can affect reaction kinetics but is not an energy source by itself.")
sub(LF, "[[Ghulheim and Ferruva#Remaining research homework|the system overview]]", "[[Ghulheim and Ferruva#Open modeling tasks|the system overview]]")
sub(LF, "- [[Ghulheim–Ferruva calculation notes]]\n", "")
sub(LF, "The source’s methane “dehydrogenase” expression is replaced by balanced **reforming accounting**:", "Methane reforming is shown as balanced **reforming accounting**:")
before(LF, "## See also", """
## Physical basis

The 17 chemical expressions on this page were checked as species with elemental inventories and formal charges, and the left and right counts agree for the three uranyl sensitizer steps, uranyl reduction, semiquinone/quinol, thiosulfate disproportionation, methane–sulfate oxidation, reforming, alcohol/NAD redox, the net radiolytic-product illustration, pyrite reduction, Fe(III) and Mn(IV) reductions, H₂–sulfate, H₂–nitrate and carbon reduction. The unchanged generic groups D, A, Q and R are treated consistently on both sides, NAD⁺ and NADH use matching formal protonation states (biological conditions can change the ionic notation), and photons and deposited energy carry energy, not atoms or charge. The three separate nuclear steps conserve nucleon number and electric charge, with electron antineutrinos shown in the beta-decay account.

This establishes **stoichiometry only**. It does not establish ΔG under Ferruvan conditions, reaction rates, catalysts, radiation yields, photocycle efficiency, primary production or the feasibility of multi-meter macrofauna. The uranyl electron-transfer sequence, the halogenated pumps and natural PFC production remain speculative; the missing physical and biochemical models are listed in the system overview.
""")

# ------------------------------------------------------------------ report
hist = re.compile(r"author|retire|former|formerly|\bold\b|supersed|original|reconcil|homework|replaced", re.I)
for p in sorted(OUT):
    print("=== history-like words in", p)
    for n, line in enumerate(OUT[p].split("\n"), 1):
        if hist.search(line) and n > 18 and not line.startswith("|"): print(f"{n}: {line[:160]}")
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
