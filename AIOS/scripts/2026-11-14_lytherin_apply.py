"""Staged edit for the Lytherin records (dry run by default; --apply writes)."""
import sys, os, re
DRY = "--apply" not in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse/Lytherin System")
def load(p): return open(p, encoding="utf-8").read()
OUT = {}
def sub(p, a, b):
    s = OUT.get(p) or load(p)
    assert s.count(a) == 1, (p, a[:70], s.count(a))
    OUT[p] = s.replace(a, b)

POINTER = "## Reference and model limits\n\nShared adopted values, manufacture premise, calculations and the limits of the orbital and climate models are recorded in [[Lytherin adopted reconciliation and calculations]].\n"
def replace_pointer(p, new):
    """replace the pointer section; if text follows it, move Physical basis to the end of the page"""
    s = OUT.get(p) or load(p)
    assert s.count(POINTER) == 1, p
    rest_after = s[s.index(POINTER) + len(POINTER):].strip("\n")
    head = s[:s.index(POINTER)].rstrip("\n")
    body = head + ("\n\n" + rest_after if rest_after else "") + "\n\n" + new.strip("\n") + "\n"
    OUT[p] = body

# ---------------------------------------------------------------- wording
sub("Lytherin System.md", "Its revised 3-M⊕/1.5-R⊕ reference gives", "Its 3-M⊕/1.5-R⊕ reference gives")
sub("Lytherin System.md", "Pure acetylene lakes and benzene rivers are replaced by phase-compatible mixed heavy-organic basins and tar channels.", "Cool basins hold phase-compatible mixed heavy-organic fluids and tar channels, not pure acetylene lakes or benzene rivers.")
sub("Lytherin System.md", "The 150–170-K thermal description replaces the original 50–70-K total-temperature claim. A 50-K", "The thermal reference is 150–170 K. A 50-K")
sub("Lytherin System.md", "The original capture/inner-system-or-rogue origin is compatible with assembly requiring an energy-loss or multi-body mechanism, but not a simple isolated flyby.", "Capture from the inner system or as a rogue body requires an energy-loss or multi-body mechanism, not a simple isolated flyby.")
sub("Lytherin System.md", "The revised orbital layout targets adjacent **5:2 period commensurabilities**, replacing the unstable unphased compact 3:2 starting layouts in the short screens.", "The orbital layout targets adjacent **5:2 period commensurabilities**; compact unphased 3:2 starting layouts were unstable in the short screens.")
sub("Pele.md", "The reference deliberately retains the original 3000-K global magma-world concept while putting its extreme heat on a quantified energy supply.", "The reference is a 3000-K global magma world whose extreme heat rests on a quantified energy supply.")
sub("Jötunn.md", "The fuller supplied planetary account follows. The 7.4-AU / approximately 4.4-R⊕ and 150–170-K references take precedence over the opening overview’s coarser values, while unresolved arithmetic and thermal conventions remain explicit for later reconciliation.", "The fuller planetary account follows. The 7.4-AU / approximately 4.4-R⊕ and 150–170-K references take precedence over the opening overview’s coarser values.")
sub("Lytherin Empire.md", "The Four Freya Moons and Five Frey Moons retain their identities.", "The Four Freya Moons and Five Frey Moons have distinct identities.")

# ---------------------------------------------------------------- Lytherin (star page)
replace_pointer("Lytherin.md", """
## Physical basis

**Stars.** The adopted tuple is stellar A 1.70 M☉, 1.70 R☉, 6.0 L☉, about 6929 K (approximately F1–F2 V) and stellar B 1.60 M☉, 1.60 R☉, 5.0 L☉, about 6824 K (approximately F2 V), for a combined 3.30 M☉ and 11.0 L☉, in a 0.100-AU, e = 0.001, 6.358-day relative orbit. The total luminosity is allocated 6 + 5 L☉, and radii of 1.7 and 1.6 R☉ keep the Stefan–Boltzmann temperatures early-F; smaller radii with these luminosities would imply cooler F5/F6 stars. These are a consistent setting tuple, not a stellar-evolution or metallicity fit, and the spectral subclasses are approximate. The present age (~1 Gyr) is separate from the main-sequence lifetime scale (~2.5–3.5 Gyr, model-dependent), from Sunder's impact 500 Myr after ignition, from Jaspis's ~400-Myr biosphere and from the Empire's centuries-long history; the manufacture epoch is unspecified.

**Photometry and location.** Illustrative V magnitudes use M_bol,☉ = 4.74, a −0.05-mag early-F bolometric correction and negligible extinction: A has Mv ≈ 2.85 (mv ≈ 4.28) and B Mv ≈ 3.05 (mv ≈ 4.48). These are reference estimates, not separately observed photometry ([Pecaut & Mamajek](https://www.pas.rochester.edu/~mpecaut/tmp/pecaut_mamajek_2013.pdf) give the spectral calibration). The system lies 19.3 pc (about 63 light-years) away at J2000 RA 19h44m00s, Dec +36°15′00″ in Cygnus, which gives Galactic Cartesian coordinates of about (6.3, 18.1, 2.1) pc with +X toward the Galactic center.

**Limits.** Flux values use the semimajor-axis reference with central-mass Kepler periods, and the stellar tuple is not a stellar-evolution calculation.
""")

# ---------------------------------------------------------------- hub
replace_pointer("Lytherin System.md", """
## Physical basis

**Manufactured architecture.** Lytherin is a manufactured system intended to maximize habitable worlds by exploiting resonance. All nine inhabited moons remain, with wider target commensurabilities; this is a high-multiplicity design, not a proof that nine is the largest physically possible number, and the screens do not require removing one.

**Planets.** Kepler periods are barycentric central-mass approximations; perturbations and giant–moon barycentric motion mean real conjunctions and osculating elements vary.

| Body | Axis (AU) | Period | Mass / radius | Flux (Earth) |
| --- | --- | --- | --- | --- |
| Pele | 0.400 | 50.87 days | 4 M⊕ / 1.4 R⊕ | 68.750 |
| Jaspis | 2.000 | 1.557 yr | 3 M⊕ / 1.5 R⊕ | 2.750 |
| Freya | 3.015 | 2.8819 yr (1052.6 days) | 300 M⊕ / 10 R⊕ | 1.210 |
| Frey | 4.205 | 4.7467 yr (1733.7 days) | 320 M⊕ / 10 R⊕ | 0.622 |
| Jötunn | 7.400 | 11.081 yr | ~17 M⊕ / ~4.4 R⊕ | 0.201 |
| Zucchero | 9.800 | 16.888 yr | 3.2 M⊕ / 6.8 R⊕ optical | 0.115 |

Freya's e = 0.004 gives apsides of 3.00294 and 3.02706 AU, and Frey's e = 0.005 gives 4.183975 and 4.226025 AU. Their mutual separation is about 5.75 mutual Hill radii in the central-mass approximation, a screening measure, not a stability theorem for the whole system. The circular circumbinary test-particle critical radius is about 0.24 AU, inside Pele's 0.4 AU, but the empirical boundary does not guarantee stability for massive interacting planets ([Holman & Wiegert](https://arxiv.org/abs/astro-ph/9809315)). The formulae are P² = a³/M, S/S⊕ = L/a², ρ = 3m/(4πR³), g = Gm/R² and escape speed √(2Gm/R).

**Numerical screens.** The satellite screen covers one giant, its four or five finite-mass moons and a 3.3-M☉ stellar point source, using a fourth-order symplectic composition. The adopted layout puts the inner moons at 800,000 and 700,000 km, which reduces tidal heating and increases inner-system clearance, and those wider isolated layouts survived 1000-year trials. The full-binary screen includes both stars, six intact planets, all nine massive inhabited moons and Callinora, with a barycentric reflex adjustment for the three satellite-host systems; the debris populations and Jiwe are omitted. Planet and inhabited-moon orbits start coplanar in this screen despite the articles' small illustrative system-plane inclinations, and Callinora is inclined 35° under an aligned-equator assumption, so it is an idealized architecture screen, not an element fit to every inclination.

- Full binary, seed 0, 1000 years: survived; maximum sampled relative total-energy error about 3.5×10⁻⁹.
- Full binary, seed 1, 1000 years: survived; error about 3.0×10⁻⁹.
- Full binary, half step, 500 years: survived; error about 2.2×10⁻¹⁰.

The main timestep is 0.0001 yr (about 52.6 minutes) and the half step 0.00005 yr (about 26.3 minutes). The diagnostics sample osculating semimajor axes and eccentricities; the total energy is dominated by the binary and does not alone certify every satellite's orbital accuracy. In these runs the inner Freya moon reached e ≈ 0.033, the inner Frey moon about 0.0235, the outer inhabited moons about 0.06–0.11 and Callinora about 0.30. Surviving a trial means no tested escape or host-impact condition occurred, not that every long-term hazard was excluded. No tides, spin, oblateness, atmosphere loss, radiation forces, machinery or climate is integrated, and the simulations are roughly a million times shorter than the system's age, so long-term stability, resonance-angle libration, secular inclination robustness and tidal migration remain explicit limits. Compact unphased 3:2 starts produced strong encounters in the tested conditions, which does not prove every phase-protected 3:2 chain impossible; wider 2:1 starts also failed in the chosen trials, while 3:1 starts survived with larger eccentricities than the selected 5:2 layout.

**Resonance.** A genuine resonance needs librating critical angles, not just a ratio of periods, and these screens did not show that the 5:2 angles librate. The architecture is therefore described as engineered target commensurabilities with resonance management, not a proven passive billion-year chain; resonant chains can themselves destabilize ([Pichierri & Morbidelli](https://arxiv.org/abs/2004.07789)).

**Tides.** The low-eccentricity synchronous equilibrium-tide sensitivity is P_tide = (21/2)(k₂/Q) G^(3/2) M_p^(5/2) R_s⁵ e² / a^(15/2). For k₂/Q = 0.003 and e = 0.02 the inner Freya moon receives about 1.66 W/m² and the inner Frey moon about 5.30 W/m², and the heating scales as e² at higher sampled eccentricities. This is a sensitivity, not a coupled thermal–orbital solution; dissipation, eccentricity evolution and heat transport need longer modeling ([Heller & Barnes](https://pmc.ncbi.nlm.nih.gov/articles/PMC3549631/) discuss illumination and tidal coupling for exomoon habitability).

**Sunder and the ice field.** Sunder is a dwarf-sized precursor of order 0.01 M⊕ disrupted 500 Myr after stellar ignition by an illustrative ~800-km embryo at 25–35 km/s, an order-of-magnitude impact and binding-energy comparison. Coupling, reaccretion, the present belt mass and the collisional lifetime are not simulated.

**Limits.** The calculations are screening arithmetic and short numerical trials; they do not validate the system for 1 Gyr.
""")

# ---------------------------------------------------------------- Pele
replace_pointer("Pele.md", """
## Physical basis

At 0.4 AU direct starlight supplies only about 2.1×10¹⁹ W after a nominal Bond albedo of 0.1, while a 1.4-R⊕ blackbody at 3000 K emits about 4.59×10²¹ W, so the additional absorbed power is 4.57×10²¹ W. An 80%-efficient collection and delivery budget needs about 6.1×10¹⁶ m² of effective collecting area at that orbital distance, equivalent to a 279,000-km disc and about 1.36×10⁻⁶ of the binary luminosity: an enormous distributed swarm, not a single rigid mirror or an ordinary internal dynamo. The stellar supply is adequate in this arithmetic sense. Collector orbits, angular-source concentration limits, optical materials, waste heat, radiation pressure, aiming, collisions, delivered spectrum and atmospheric energy exchange are unsolved engineering, and the blackbody figure is a budget scale, not an atmosphere model. Plasma excitation can have a different temperature from the molten surface. Lava-world comparisons are physical context only, not evidence for an observed manufactured planet ([Kite et al., atmosphere–interior exchange](https://doi.org/10.3847/0004-637X/828/2/80); [two-phase magma oceans](https://arxiv.org/abs/2205.02864)). No claim of billion-year survival under this evaporative regime is made, and the deep-core temperatures and phases are hypotheses, not derived layers.
""")

# ---------------------------------------------------------------- Jaspis
replace_pointer("Jaspis.md", """
## Physical basis

A 3-M⊕ world at 1.5 R⊕ has a density of about 4.90 g/cm³, a gravity of 1.33 g and an escape speed of about 15.82 km/s; a 1.1-R⊕ radius would imply about 12.43 g/cm³, too dense for a carbon-rich bulk composition. Carbon-rich differentiated interiors are plausible model families, not a unique solution ([SiC equation-of-state and interior models](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018JE005582)). At a Bond albedo of 0.05 the simple irradiation comparison is about 354 K, so the nominal 450-K mean is a greenhouse target without a radiative-convective calculation, and volcanic provinces reach about 900 K or hotter locally. The normalized 7-bar gas table closes. Benzene's critical temperature is about 562 K, so pressure cannot produce an ordinary pure-liquid benzene sea at 900 K ([NIST phase data](https://webbook.nist.gov/cgi/formula?ID=C71432&Type=TC)); cool sheltered basins and subsurface pools may instead hold mixed heavy-aromatic and nitrile fluids, with anthracene and phenanthrene as candidate components, not a complete mixture phase diagram.
""")

# ---------------------------------------------------------------- Life on Jaspis
replace_pointer("Life on Jaspis.md", """
## Physical basis

Photons, redox work and maintained hot–cold gradients supply the planimals' energy, and springs store it; recycled carbon is material, not a perpetual energy source. Templates carry heritable information and selectable variation without DNA or RNA. This is speculative solid-state biology: no experimental validation or numerical material-fatigue model is supplied, and the planet's physical reference is on [[Jaspis]] under Physical basis.
""")

# ---------------------------------------------------------------- Freya / Frey
replace_pointer("Freya.md", """
## Physical basis

Freya orbits at 3.015 AU with a period of 2.8819 yr (1052.6 days), a mass of 300 M⊕ and a radius of 10 R⊕, and receives 1.210 Earth flux; e = 0.004 gives apsides of 3.00294 and 3.02706 AU. Each adjacent pair of its four moons targets a 5:2 period ratio, and the outermost moon at 5,000,000 km lies at about 0.246 of the cluster's roughly 20.35-million-km Hill radius, a less crowded layout that keeps all four inhabited worlds. Nominal initial eccentricities in the screens are 0.003 and are not claimed to stay constant. With k₂/Q = 0.003 and e = 0.02 the inner moon receives about 1.66 W/m² of tidal heat, which scales as e². The system-wide screens, resonance limits and tidal sensitivity are under Physical basis on [[Lytherin System]].
""")
replace_pointer("Frey.md", """
## Physical basis

Frey orbits at 4.205 AU with a period of 4.7467 yr (1733.7 days), a mass of 320 M⊕ and a radius of 10 R⊕, and receives 0.622 Earth flux; e = 0.005 gives apsides of 4.183975 and 4.226025 AU. Each adjacent pair of its five moons targets a 5:2 period ratio, and the outermost moon at 8,058,819 km lies at about 0.278 of the cluster's roughly 29.01-million-km Hill radius, a less crowded layout that keeps all five inhabited worlds. Nominal initial eccentricities in the screens are 0.003 and are not claimed to stay constant. With k₂/Q = 0.003 and e = 0.02 the inner moon receives about 5.30 W/m² of tidal heat, which scales as e²; the wider 700,000-km inner moon eases this compared with a closer candidate. The system-wide screens, resonance limits and tidal sensitivity are under Physical basis on [[Lytherin System]].
""")

# ---------------------------------------------------------------- Empire
replace_pointer("Lytherin Empire.md", """
## Physical basis

The giant-axis reference gives a mean synodic period of 7.3354299 Earth years; actual dates vary under perturbations. The 7.335-year Great Cycle governs Conjunction and Ascension, migration festivals and alternating capital relocation, and a Civil Year is 365.25 Earth days, distinct from a Great Cycle. The orbital and tidal calculations behind the moon layout are under Physical basis on [[Lytherin System]].
""")

# ---------------------------------------------------------------- Jötunn
replace_pointer("Jötunn.md", """
## Physical basis

Jötunn keeps 17 M⊕, about 4.4 R⊕, a 7.4-AU orbit, 18 moons, a 14-hour spin, an obliquity of 13° and a magnetic tilt of 45°. Its density is about 1.10 g/cm³ and its circular orbital speed about 19.89 km/s. The irradiation comparison gives about 164 K; adding an illustrative 50-K intrinsic component by fourth powers gives a total effective temperature near 164.4 K. High-pressure water and ammonia phases and an ionic dynamo remain hypotheses; it is a Neptune-class ice giant, not a near-brown-dwarf mass.
""")

# ---------------------------------------------------------------- Zucchero
replace_pointer("Zucchero.md", """
## Physical basis

Zucchero keeps 3.2 M⊕, a 9.8-AU orbit and a roughly 0.8-M⊕ core. The 6.8-R⊕ optical radius is separate from a nominal **5.8-R⊕ 1-bar radius**, which gives about 0.095 g and about 0.0904 g/cm³ at the pressure reference. An isothermal 140-K, μ = 2.3-g/mol hydrostatic comparison gives a pressure ratio of about 4.4×10⁻⁵ between the optical and 1-bar radii, a geometrical plausibility check, not a haze or structure model; a smaller 4-R⊕ pressure radius would put the optical outline implausibly many scale heights above 1 bar in that comparison. An apparent haze-inflated radius is an established proposal for some superpuffs ([Wang & Dai](https://arxiv.org/abs/1902.04188)), but applying it here is an inference, and radius, envelope entropy, age, cooling, escape, haze support and any continuing manufactured maintenance still need a joint model. A 140-K effective reference (about 143 K from the irradiation comparison) does not fix the temperature of every layer. The deep H₂/He/CH₄/other composition is normalized to 86.5/12/1/0.5%, and upper abundances can change through condensation and chemistry. Quiet clouds alone do not prove a missing internal dynamo.

Callinora's finite-mass relative period is about 121.2 days and its barycentre lies about 216,000 km from Zucchero's center; the roughly 15.6% mass ratio means the coupling is substantial. At these distances the illustrative k₂/Q = 0.003 tidal heat is only of order 10⁻⁵ W/m², so radiogenic and geothermal subsurface refugia are emphasized, and the nominal 200-K CO₂/N₂ climate is a greenhouse target, not a demonstrated result.
""")

hist = re.compile(r"author|retire|former|formerly|\bold\b|older|supersed|original|reconcil|replaced|revised|source’s|source's", re.I)
for p in sorted(OUT):
    print("=== history-like words in", p)
    for n, line in enumerate(OUT[p].split("\n"), 1):
        if hist.search(line) and n > 18 and not line.startswith("|"): print(f"{n}: {line[:140]}")
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
