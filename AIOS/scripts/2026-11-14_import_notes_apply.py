"""Staged edit for the 12 pages that still carry Import/Reconciliation notes.
Dry run by default; --apply writes; --drop-category-column also removes the old-wiki
Category column from the root hub table (separate user decision)."""
import sys, os, re
DRY = "--apply" not in sys.argv
DROP_CAT = "--drop-category-column" in sys.argv
os.chdir("/Users/robertmarshallmurphy/Documents/Aquatikiverse")
def load(p): return open(p, encoding="utf-8").read()
OUT = {}
NOTES = re.compile(r"^## (Import notes|Reconciliation notes)\s*$", re.M)

def tail_from_notes(p, new, stop_at=None):
    """replace from the first notes heading to EOF (or to `stop_at` heading) with `new` (may be empty)"""
    s = OUT.get(p) or load(p)
    m = NOTES.search(s)
    assert m, p
    start = m.start()
    end = len(s) if stop_at is None else s.index(stop_at, start)
    head = s[:start].rstrip("\n")
    body = (head + "\n\n" + new.strip("\n") + "\n") if new.strip() else head + "\n"
    if stop_at is not None:
        body += "\n" + s[end:]
    OUT[p] = body

OE = "Orpheus and Eurydice System/"
# -------------------------------------------------------------- Orpheus and Eurydice hub
tail_from_notes(OE + "Orpheus and Eurydice System.md", """
## Model status

The current stellar population is two. The formation history is an explicitly uncertain fallback-origin hypothesis, and the detailed planet and biosphere pages govern all planetary figures.
""")
# -------------------------------------------------------------- Orpheus and Eurydice (star)
tail_from_notes(OE + "Orpheus and Eurydice.md", """
## Physical basis

The adopted 0.79 M☉, 5250 K and 0.40 L☉ agree with a radius of about 0.765 R☉ (L = R²(T/5772 K)⁴). Formation and recycling histories are explicitly uncertain. The system has two current stellar objects and three planets, and the 20–40 AU companion distance is an observational estimate, not a specified periastron or apastron range.
""")
# -------------------------------------------------------------- Alchemis
tail_from_notes(OE + "Alchemis.md", """
## Physical basis

Alchemis began with a 24-hour rotation and now has a prograde sidereal day of **240 hours**; at the ~104-day year this gives a **mean solar day of ~265.5 hours**, not 240. A flattening of 0.0034 belongs to the early rotation, and the present flattening is unspecified. The orbital period is ~104 days, life is established and the native intelligent species is Formoquens. The mass, radius, gravity and density agree within their approximate precision, and surface redox cycling includes native inorganic metabolism.

The representative day and night temperatures, the phosphor energy storage over long nights and the ~4.5-km atmospheric scale height are approximate environmental assumptions, not independent high-precision predictions. The scale height refers to the warmer atmospheric layers (~350 K for an oxygen-dominated mixture), not the cold nighttime surface. The exotic photonic biosphere is a speculative premise.
""")
# -------------------------------------------------------------- Laputa
tail_from_notes(OE + "Laputa.md", """
## Physical basis

**Orbit and atmosphere.** An orbit of 0.63 AU, a period of ~205 days and ~1.01 Earth flux are mutually consistent with Orpheus's 0.79 M☉ and 0.40 L☉. The dry atmosphere sums to 100%: 49% Ne, 21% O₂, 24.9% N₂, 5% Ar, 0.04% CO₂ and 0.06% other trace gases, which gives an oxygen partial pressure of 0.189 atm at 0.90 atm total pressure. Clean-air breathability is distinct from particulate exposure; [NASA's atmospheric environment guidance](https://www.nasa.gov/reference/6-0-natural-and-induced-environments-vol-2/) separates oxygen supply from contaminant control.

**The Harmonids.** The moons have masses of 0.020 and 0.015 Earth masses, mean radii of 2,500 and 2,200 km and a 110,000-km barycentric orbit about Laputa. Their bulk densities are ~1.83 and ~2.01 g/cm³: enriched crusts and small metallic cores sit within lower-density, volatile-bearing interiors, so the moons are not entirely metallic. Their orbits are nearly circular, coplanar and prograde with mutually synchronous spins. [Eggleton's volume-equivalent Roche-lobe approximation](https://articles.adsabs.harvard.edu/pdf/1983ApJ...268..368E) gives a limiting center separation of ~6,210 km for the stated volume radii, so the adopted **7,000 km** is a modest margin above that first-order limit (a 5,000-km separation would lie inside it). At 7,000 km the volume-equivalent Roche lobes are ~2,828 and ~2,480 km, exceeding the mean radii; tidal shapes are expected, and perfectly spherical surfaces are not assumed. The mutual period is **8.65 hours** and the pair's orbital period around Laputa is **3.10 Earth days**. The mutual Hill scale at 110,000 km is ~20,510 km and the adopted separation is ~0.34 of that, within the ~0.5-Hill scale often used for prograde binary survival ([three-body Hill-stability research](https://academic.oup.com/mnras/article/466/1/276/2617724)). These are consistency checks for a plausible working configuration, not a full tidal or N-body proof of gigayear survival or an exact mathematical minimum; the setting adopts the configuration as sufficiently stable for its present narrative.

**Geochemistry and climate.** Uranium oxidation consumes oxygen; it does not release it. Salt exposure hazards are compound-dependent. The surface temperature is a climate-model assumption, not an airless equilibrium temperature, and the ~9-km atmospheric scale height is representative and varies with composition and temperature.

**Speculative physics.** The >1-tesla field, quasicrystalline magnetic materials and levitating mountains are speculative premises, not claimed to follow quantitatively from ordinary neodymium magnetism alone. Low-field habitation corridors reduce engineering constraints but do not guarantee universal equipment compatibility or complete radiation protection. "Null" is one of five cultural navigation categories, not a fifth spatial axis. The rounded planetary figure is an adopted structural model, not derived solely from rotation.
""")
# -------------------------------------------------------------- Formoquens
tail_from_notes(OE + "Formoquens.md", """
## Model status

Assemblers repair and reconfigure existing individuals, queens fabricate new independent individuals, and ongoing abiogenesis can produce rogues independently of queens; recurring battles over newly evolving forms are an explicit part of clade society. The Formoquens are native to Alchemis and are not post-biological descendants of an organic species. Caste changes require substantial reconstruction. Clades coordinate through local optical networks and traveling emissaries, not instantaneous nation-wide consensus, and rare individual transfers are compatible with long operational lifespans. Contact with human-inhabited Laputa occurs after human settlement began in the 24th century; an exact first-contact year is not specified. Spacefaring bodies require carried reactants and stored energy, and detailed propulsion performance is not asserted. The inorganic photonic machinery is a speculative premise.
""")
# -------------------------------------------------------------- Dysmorph
tail_from_notes(OE + "Dysmorph.md", """
## Physical basis

Blank infobox fields are unspecified; they are not needed for the present narrative. Dysmorph lies outside Orpheus's quoted circumstellar zone even though it supports exotic life. The bulk shape is nearly spherical with a distorted geoid, the flattening is ~0.0025 from the stated radii and the orbital period is ~832 days. Local gravity runs from ~0.7 g to more than 3 g in the detailed planet account; these extreme anomalies are a speculative setting premise, not a result established from density contrasts alone.

**Energy accounting.** Globally averaged absorbed starlight is ~37 W/m², against ~0.3–0.5 W/m² of internal heat. Radiogenic energy powers local geochemistry and hot spots, while greenhouse warming and starlight control the broader climate. Radioactive regeneration is the nonaqueous proposal in [[Life on Dysmorph#Proposed Nonaqueous Regeneration]]; its detailed chemistry remains explicitly unresolved, an accepted limitation of the model.
""")
# -------------------------------------------------------------- Life on Alchemis
tail_from_notes(OE + "Life on Alchemis.md", """
## Model status

The detailed biosphere and species accounts govern the system summary: Formoquens are native to Alchemis, with ~1.2–1.5 Gyr of biospheric development. The present sidereal day is 240 hours (mean solar day ~265.5 hours) and rotation is prograde. New independent clade members are fabricated by queens, assemblers repair and reconfigure existing members, and independent abiogenesis continues outside that process, so recurrent struggles over new rogue forms remain central to ecology and society. Independent origins coexist with inherited structural lineages. "Non-biological" means outside terrestrial cellular biology, not an absence of metabolism or evolution. Nightside input lacks direct starlight but includes phosphorescence and transported stored energy. The 400–950 nm range is the adopted photonic exchange band, and UV-sensitive receptors also exist. Clades are locally coordinated, with travel and direct encounters connecting distant groups. The photonic-mineral machinery is an explicit speculative premise whose microscopic energy storage and processing remain open for future development.
""")
# -------------------------------------------------------------- Life on Laputa
tail_from_notes(OE + "Life on Laputa.md", """
## Model status

The selenium endpoint is Se⁰, matching the detailed metabolic description. Selenobiontes are a small chemoheterotrophic decomposer community, compatible with the absence of macroscopic grazing or predation. The atmospheric composition follows [[Laputa]] and totals 100% on a dry reference basis. The <10% liquid surface coverage is distinct from a water inventory ~10% of Earth's, and neither is substituted for the other. The stellar spectral reference (~550 nm) is distinct from the phototroph absorption peak (~610 nm). The ongoing oxidation transition refers to remaining crustal sinks and regional redox fronts despite a high atmospheric oxygen baseline. The biosphere is ~1.2 Gyr old, and human agriculture is a later introduced ecosystem.
""")
# -------------------------------------------------------------- Life on Dysmorph (keep the references section)
tail_from_notes(OE + "Life on Dysmorph.md", """
## Model status

The biosphere and Teuthis radiomancia are established setting facts. The inorganic halide biosphere, extreme gravity niches and radiomancy are setting premises, and nonaqueous abiotic regeneration is a proposed mechanism: neither a quantitative chemical yield nor detailed ionizing-radiation optics is claimed to be established. The reactions, limitations and scientific references are on this page. Squiddies is the human colloquial name; it has no standalone article.
""", stop_at="## Scientific references for the regeneration model")
# -------------------------------------------------------------- Nimvion 3421
tail_from_notes("Nimvion System/Nimvion 3421.md", """
## Physical basis

The adopted mass, radius, temperature and luminosity agree at the quoted precision.
""")
# -------------------------------------------------------------- Chiaroscuro
tail_from_notes("Chiaroscuro System/Chiaroscuro.md", """
## Physical basis

The stellar components are F1V and K1V, totaling 2.2 M☉ and approximately 5.9 L☉, rounded to 6 L☉ in illumination estimates, at an adopted distance of 100 pc. The binary eccentricity of 0.02 is a working assumption for stability and illumination calculations. In a central mutual eclipse the K star can obscure about 28% of the F star's projected area, roughly a 27% reduction in total bolometric light with the quoted luminosities; the actual wavelength-dependent eclipse depth depends on stellar surface brightness and limb darkening.
""")
# -------------------------------------------------------------- root hub
tail_from_notes("Aquatikiverse.md", "")

if DROP_CAT:
    s = OUT["Aquatikiverse.md"]
    lines = s.split("\n")
    out, n = [], 0
    for ln in lines:
        if ln.startswith("|"):
            cells = re.split(r"(?<!\\)\|", ln)
            # cells[0] == '' and cells[-1] == '' around the outer pipes
            inner = cells[1:-1]
            if len(inner) == 7:
                inner = inner[:-1]
                ln = "|" + "|".join(inner) + "|"
                n += 1
        out.append(ln)
    OUT["Aquatikiverse.md"] = "\n".join(out)
    print("hub table rows rewritten (Category dropped):", n)

hist = re.compile(r"retire|former|formerly|\bold\b|supersed|original|reconcil|imported|exhausted|wiki|resolved|author", re.I)
for p in sorted(OUT):
    new = OUT[p]
    i = max(new.rfind("\n## Physical basis"), new.rfind("\n## Model status"))
    seg = new[i:] if i >= 0 else ""
    hits = [l for l in seg.split("\n") if hist.search(l)]
    print(f"{p}: new section {len(seg)} chars; history-like lines in it: {len(hits)}")
    for h in hits[:3]: print("   ", h[:150])
tbl = [l for l in OUT["Aquatikiverse.md"].split("\n") if l.startswith("|")]
print("hub table cell counts:", sorted({len(re.split(r'(?<!\\)\|', l)) - 2 for l in tbl}))
for p in sorted(OUT): print(("DRY " if DRY else "WROTE ") + p)
if not DRY:
    for p, t in OUT.items(): open(p, "w", encoding="utf-8").write(t)
    print("applied")
