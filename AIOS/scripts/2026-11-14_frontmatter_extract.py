"""Dry-run extraction of infobox tables into proposed frontmatter (changes NO page).

Reads every content page, parses its Property/Quantity tables, converts values to the
canonical units in AIOS/frontmatter-schema.md, computes derived bulk values from mass and
radius, compares them with the page's stated values, and writes:
  AIOS/scripts/2026-11-14_frontmatter_extract.json   (proposed frontmatter per page; input for the apply step)
  AIOS/frontmatter-extraction-report.md              (human review report)
Run with: python3 -I AIOS/scripts/2026-11-14_frontmatter_extract.py
"""
import os, re, json, math, collections
ROOT = "/Users/robertmarshallmurphy/Documents/Aquatikiverse"
os.chdir(ROOT)

# ---------------------------------------------------------------- constants (schema)
G = 6.67430e-11; MEARTH = 5.9722e24; REARTH = 6371.0; MSUN = 1.98847e30; RSUN = 695700.0
LSUN = 3.828e26; AU = 149597870.7; YEAR = 365.25; ATM = 1.01325; SEARTH = 1361.0
MJUP = 1.89813e27; RJUP = 71492.0; MLUNAR = 7.342e22; PC_LY = 3.26156

SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
def sci(t):
    """normalise scientific notation and unicode to plain ASCII exponents"""
    t = t.replace("−", "-").replace("–", "–")
    t = re.sub(r"\s*[×x·]\s*10\s*\^?\s*([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda m: "e" + m.group(1).translate(SUP), t)
    t = re.sub(r"\s*[×x·]\s*10\s*\^\s*\{?([-+]?\d+)\}?", lambda m: "e" + m.group(1), t)
    t = re.sub(r"\s*[×x·]\s*10([-+]?\d+)\b", lambda m: "e" + m.group(1), t)
    return t

def clean(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = t.replace("\\|", "|")
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"\*\*|`", "", t)
    return sci(t).strip()

NUM = r"[-+]?\d[\d,]*(?:\.\d+)?(?:e[-+]?\d+)?"
def tonum(s):
    s = s.replace(",", "")
    try: return float(s)
    except ValueError: return None

def unit_match(text, units):
    """find first 'number [– number] unit'; returns (value, vmin, vmax, factor_key) or None. units: list of (regex, factor)"""
    for rx, fac in units:
        m = re.search(r"(" + NUM + r")\s*[–—]\s*(" + NUM + r")\s*(?:" + rx + r")", text)
        if m:
            a, b = tonum(m.group(1)), tonum(m.group(2))
            if a is not None and b is not None:
                lo, hi = sorted((a * fac, b * fac)); return (lo + hi) / 2, lo, hi
        m = re.search(r"(" + NUM + r")\s*(?:" + rx + r")", text)
        if m:
            a = tonum(m.group(1))
            if a is not None: return a * fac, None, None
    return None

EARTH = r"(?:M|R|F|S|g)(?:⊕|🜨|_?(?:Earth|E\b))|Earth\s+(?:masses|mass|radii|radius|flux)"
UNITS = {
 "mass_kg": [(r"M(?:⊕|🜨|_?Earth)|Earth masses|Earth mass", MEARTH), (r"M(?:☉|_?Sun)|solar masses", MSUN), (r"M(?:♃|_J|_Jup\w*)|Jupiter masses", MJUP), (r"lunar masses?|M(?:☾|_Moon)", MLUNAR), (r"kg", 1.0)],
 "radius_km": [(r"R(?:⊕|🜨|_?Earth)|Earth radii|Earth radius", REARTH), (r"R(?:☉|_?Sun)|solar radii", RSUN), (r"R(?:♃|_J|_Jup\w*)", RJUP), (r"km", 1.0)],
 "density_gcc": [(r"g\s*/\s*cm³|g\s*cm⁻³|g/cc|g cm-3", 1.0), (r"kg\s*/\s*m³|kg m⁻³", 0.001)],
 "gravity_ms2": [(r"m\s*/\s*s²|m s⁻²|m/s2", 1.0), (r"g(?:⊕|🜨)?\b", 9.80665)],
 "escape_kms": [(r"km\s*/\s*s", 1.0), (r"m\s*/\s*s\b", 0.001)],
 "semimajor": [(r"AU", ("au", 1.0)), (r"million\s+km", ("km", 1e6)), (r"km", ("km", 1.0))],
 "period_days": [(r"Earth days|days|d\b", 1.0), (r"Earth years|years|yr|y\b", YEAR), (r"hours?|h\b", 1 / 24)],
 "rotation_hours": [(r"hours?|h\b", 1.0), (r"Earth days|days|d\b", 24.0)],
 "flux_earth": [(r"F(?:⊕|🜨)|S(?:⊕|🜨)|Earth flux|Earth insolation", 1.0), (r"W\s*/\s*m²|W m⁻²", 1 / SEARTH)],
 "temperature_k": [(r"K\b", 1.0)],
 "pressure_bar": [(r"atm", ATM), (r"bar", 1.0), (r"mbar", 0.001), (r"Pa\b", 1e-5)],
 "area_km2": [(r"million\s+km²", 1e6), (r"km²|km\^2", 1.0), (r"m²|m\^2", 1e-6)],
 "volume_km3": [(r"km³|km\^3", 1.0), (r"m³|m\^3", 1e-9)],
 "circumference_km": [(r"km", 1.0)],
 "luminosity_lsun": [(r"L(?:☉|_?Sun)|solar luminosities", 1.0), (r"W\b", 1 / LSUN)],
 "age_gyr": [(r"Gyr|Ga\b|billion years", 1.0), (r"Myr|million years", 1e-3), (r"Tyr|trillion years", 1e3)],
 "distance_ly": [(r"light[- ]?years?|ly\b", 1.0), (r"pc\b|parsecs?", PC_LY)],
 "angle_deg": [(r"°|º|deg(?:rees)?", 1.0)],
}

# label regex -> (field key, kind). kind: q=quantity via UNITS[key]; n=plain number; t=text; l=list; k=link text; c=combined
LABELS = [
 (r"^name$", "name", "t"), (r"^(system|star system)$", "system", "k"), (r"^planet$", "planet", "k"), (r"^(star|stars|host.*|primary)$", "star", "k"),
 (r"^type$", "type_text", "t"), (r"^named after$", "named_after", "t"), (r"^(adjectives?|demonym.*)$", "adjectives", "l"), (r"^constellation$", "constellation", "t"),
 (r"^right ascension$", "ra_hours", "ra"), (r"^declination$", "dec_deg", "dec"), (r"^(distance.*|earth distance)$", "distance_ly", "q:distance_ly"),
 (r"^(spectral type|spectral classification|luminosity class)$", "spectral_type", "t"), (r"^(effective temperature)$", "teff_k", "q:temperature_k"),
 (r"^(luminosity|bolometric luminosity|star luminosity)$", "luminosity_sun", "q:luminosity_lsun"), (r"^metallicity$", "metallicity_feh", "n"),
 (r"^(age|formation age)$", "age_gyr", "q:age_gyr"),
 (r"^(absolute (visual )?magnitude)$", "absolute_magnitude_v", "n"), (r"^(apparent (visual )?magnitude)$", "apparent_magnitude_v", "n"),
 (r"^(system mass|total stellar mass|total mass)$", "system_mass_sun", "q:mass_kg"), (r"^(combined luminosity|total luminosity)$", "system_luminosity_sun", "q:luminosity_lsun"),
 (r"^roche limit$", "roche_limit_km", "q:circumference_km"), (r"^(equatorial rotation speed|rot velocity|rotation velocity)$", "rotation_speed_kms", "q:escape_kms"),
 (r"^geometric albedo$", "albedo_geometric", "n"), (r"^moment of inertia factor$", "moment_of_inertia_factor", "n"), (r"^satellite of$", "host", "k"),
 (r"^mass$", "mass", "q:mass_kg"), (r"^(mean radius|radius|equatorial radius|star radius)$", "radius", "q:radius_km"),
 (r"^polar radius$", "radius_polar", "q:radius_km"),
 (r"^(density|bulk density|mean density)$", "density_gcc", "q:density_gcc"), (r"^(surface gravity|surface grav.*|gravity)$", "gravity_ms2", "q:gravity_ms2"),
 (r"^escape.*", "escape_kms", "q:escape_kms"), (r"^surface area$", "area_km2", "q:area_km2"), (r"^volume$", "volume_km3", "q:volume_km3"),
 (r"^circumference$", "circumference_km", "q:circumference_km"), (r"^flattening$", "flattening", "n"),
 (r"^(semimajor.*|semi-major.*|orbital separation|axis|binary semimajor axis|orbital semi-major axis)$", "semimajor", "q:semimajor"), (r"^(orbital period|period|binary period)$", "period_days", "q:period_days"),
 (r"^(eccentricity|orbital eccentricity|binary eccentricity)$", "eccentricity", "n"), (r"^(inclination|orbital inclination)$", "inclination_deg", "q:angle_deg"),
 (r"^(apoastron|periastron|aphelion|perihelion)$", "apsides", "x"), (r"^(axial tilt|obliquity)$", "obliquity_deg", "q:angle_deg"),
 (r"^(sidereal day|sidereal rotation|rotation|rotation period|spin)$", "rotation_period_hours", "q:rotation_hours"),
 (r"^(stellar flux|flux.*|insolation.*|irradiat.*)$", "flux_earth", "q:flux_earth"), (r"^(albedo|bond albedo.*)$", "albedo_bond", "albedo"),
 (r"^(equilibrium temp.*)$", "temperature_eq_k", "q:temperature_k"), (r"^(temperature|single temperature|mean surface temperature|surface temperature|mean temp.*)$", "temperature_mean_k", "q:temperature_k"),
 (r"^(surface pressure|pressure|atmospheric pressure)$", "pressure_surface_bar", "q:pressure_bar"), (r"^(atmosphere|atmosphere composition|atmospheric composition)$", "atmosphere_text", "skip"),
 (r"^(satellites|known moons|moons.*)$", "moons_count", "count"), (r"^(scale height|atmospheric scale height)$", "scale_height_km", "q:circumference_km"),
 (r"^hill (radius|scale)$", "hill_radius_km", "q:semimajor"), (r"^(average orbital speed|avg speed|orbital velocity|orbital speed)$", "orbital_speed_kms", "q:escape_kms"),
 (r"^discoverer$", "discoverer", "t"), (r"^discovery method$", "discovery_method", "t"), (r"^discovery site$", "discovery_site", "t"), (r"^(discovered|reported discovery date|discovery date)$", "discovery_year", "year"),
 (r"^(alt names|alternate name|alt name)$", "alt_names", "l"),
 (r"^solvent$", "solvent", "t"), (r"^base element chemistry$", "backbone", "t"), (r"^primary metabolism$", "primary_metabolism", "t"), (r"^dominant redox couples$", "redox_couples", "l"),
 (r"^membrane chemistry$", "membrane_chemistry", "t"), (r"^photosynthesis wavelength$", "photosynthesis_band_nm", "t"), (r"^(biosphere age|age of biosphere)$", "biosphere_age_gyr", "q:age_gyr"),
 (r"^seeding origin$", "seeding_origin", "t"), (r"^dominant lifeforms$", "dominant_lifeforms", "l"), (r"^primary ecosystem types$", "ecosystems", "l"),
 (r"^current biosphere state$", "biosphere_state", "t"), (r"^intelligent species$", "intelligent_species", "l"), (r"^civilization level$", "civilization_level", "t"), (r"^surface coverage$", "surface_coverage", "t"),
]
COMBINED = [  # combined rows, split on ' / ' in order
 (r"^mass / radius$", ["mass", "radius"]), (r"^(surface area / volume|spherical reference area / volume)$", ["area_km2", "volume_km3"]), (r"^axis / eccentricity$", ["semimajor", "eccentricity"]),
 (r"^gravity / escape speed$", ["gravity_ms2", "escape_kms"]), (r"^density / gravity / escape speed$", ["density_gcc", "gravity_ms2", "escape_kms"]),
]
KEYBYFIELD = {f: k for _, f, k in LABELS}

IGNORE = {"apsis", "notes", "extrasolarplanet", "epoch", "discovery ref", "discovery reference", "classification", "location", "interior", "variable", "pronounced", "coordinates", "planets", "dwarf planets", "outermost planet", "protoplanetary disc", "kuiper cliff", "heliopause", "frost line", "galactocentric radius", "star mass", "star radius", "star luminosity", "radial velocity", "stellar rv amplitude", "observer inclination", "q factor", "periastron / apastron"}
def label_match(lab):
    if lab in IGNORE: return "ignored", "ignore"
    for rx, f, k in LABELS:
        if re.search(rx, lab): return f, k
    return None, None

def parse_ra(t):
    m = re.search(r"(\d+)\s*h\s*(?:(\d+)\s*m)?\s*(?:(\d+(?:\.\d+)?)\s*s)?", t)
    if not m: return None
    return round(int(m.group(1)) + int(m.group(2) or 0) / 60 + float(m.group(3) or 0) / 3600, 4)
def parse_dec(t):
    t = t.replace("−", "-").replace("–", "-")
    m = re.search(r"([-+]?)\s*(\d+)\s*°\s*(?:(\d+)\s*[′']\s*)?(?:(\d+(?:\.\d+)?)\s*[″\"]\s*)?", t)
    if not m: return None
    v = int(m.group(2)) + int(m.group(3) or 0) / 60 + float(m.group(4) or 0) / 3600
    return round(-v if m.group(1) == "-" else v, 4)

def parse_cell(field, kind, text):
    """returns (value, extras dict, note). value None => unparsed"""
    raw = text
    t = clean(text)
    if kind == "t": return (t or None), {}, ""
    if kind == "k": return (re.sub(r"\s+", " ", text.replace("\\|", "|").strip()) or None), {}, ""
    if kind == "l":
        parts = [p.strip() for p in re.split(r";|,(?![^()]*\))", t) if p.strip()]
        return (parts or None), {}, ""
    if kind == "ra":
        v = parse_ra(t); return v, {}, "" if v is not None else "RA not parsed"
    if kind == "dec":
        v = parse_dec(t); return v, {}, "" if v is not None else "Dec not parsed"
    if kind == "skip": return None, {}, "kept in body"
    if kind.startswith("q:temperature") :
        m = re.search(r"(" + NUM + r")\s*[–-]\s*(" + NUM + r")\s*°\s*C", t)
        if m:
            a, b = tonum(m.group(1)) + 273.15, tonum(m.group(2)) + 273.15
            return (a + b) / 2, {"min": min(a, b), "max": max(a, b)}, "from Celsius"
        m = re.search(r"(" + NUM + r")\s*°\s*C", t)
        if m and not re.search(r"\bK\b", t): return tonum(m.group(1)) + 273.15, {}, "from Celsius"
    if kind == "year":
        m = re.search(r"\b(1[5-9]\d\d|2\d\d\d)\b", t); return (int(m.group(1)) if m else None), {}, ""
    if kind == "count":
        if re.search(r"\b(none|no known|no moons|no satellites)\b", t, re.I): return 0, {}, ""
        words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
        m = re.match(r"^\s*(?:~|≈)?(\d+)\b", t)
        if m: return int(m.group(1)), {}, ""
        m = re.match(r"^\s*(one|two|three|four|five|six|seven|eight|nine|ten)\b", t, re.I)
        if m: return words[m.group(1).lower()], {}, "count from words; check"
        return None, {}, "moon count is descriptive"
    if kind in ("n", "albedo"):
        if kind == "albedo":
            m = re.search(r"Bond[^0-9]*(" + NUM + ")", t)
            if m: return tonum(m.group(1)), {}, "Bond value taken"
        m = re.search(NUM, t)
        if not m: return None, {}, "no number"
        a = tonum(m.group(0)); return a, {}, ""
    if kind == "x":  # apsides: handled as a pair of fields by caller
        return None, {}, "apsis"
    if kind.startswith("q:"):
        ukey = kind[2:]
        r = unit_match(t, UNITS[ukey])
        if r is None:
            if ukey == "angle_deg":
                m = re.search(r"(" + NUM + r")\s*[–-]\s*(" + NUM + ")", t)
                if m: a, b = tonum(m.group(1)), tonum(m.group(2)); return (a + b) / 2, {"min": min(a, b), "max": max(a, b)}, ""
                m = re.search(NUM, t)
                if m and not re.search(r"unknown|coplanar|aligned", t, re.I): return tonum(m.group(0)), {}, "no degree sign"
            return None, {}, "no unit match"
        v, lo, hi = r
        extras = {}
        if lo is not None: extras = {"min": lo, "max": hi}
        return v, extras, ""
    return None, {}, "unhandled"

def semimajor_fields(v, t):
    """semimajor returns km or au: re-run to know which unit"""
    for rx, (u, fac) in UNITS["semimajor"]:
        m = re.search(r"(" + NUM + r")\s*(?:" + rx + r")", t)
        if m: return u, tonum(m.group(1)) * fac
    return None, None

# ---------------------------------------------------------------- page scan
def read_pages():
    pages = []
    for r, d, f in os.walk("."):
        if r.startswith(("./AIOS", "./logs", "./.obsidian", "./images", "./.git")): continue
        for x in f:
            if x.endswith(".md"): pages.append(os.path.join(r, x)[2:])
    return sorted(pages)

HEADPROP = re.compile(r"^\|\s*(?:\*\*)?(Property|Quantity|Parameter|Attribute|Name)(?:\*\*)?\s*\|", re.I)
def tables_in(body):
    out = []
    lines = body.split("\n"); i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"): j += 1
            out.append((lines[i], lines[i + 2:j])); i = j
        else: i += 1
    return out

def split_row(ln): return [c.strip() for c in re.split(r"(?<!\\)\|", ln)[1:-1]]

def front(t):
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return (m.group(1), t[m.end():]) if m else ("", t)

def old_list(fm, key):
    m = re.search(r"^" + key + r":\n((?:\s+- .*\n?)+)", fm + "\n", re.M)
    if not m: return []
    return [re.sub(r'^["\']|["\']$', "", l.strip()[2:].strip()) for l in m.group(1).splitlines()]
def old_val(fm, key):
    m = re.search(r"^" + key + r':\s*(.+)$', fm, re.M)
    return re.sub(r'^["\']|["\']$', "", m.group(1).strip()) if m else None

def guess_class(fields, tags, rel, semi_unit):
    f = set(fields)
    tg = " ".join(tags).lower()
    if "solvent" in f or "primary_metabolism" in f: return "biosphere"
    if "spectral_type" in f or "teff_k" in f or "luminosity_sun" in f: return "star"
    if "mass" in f or "radius" in f or "semimajor" in f:
        if semi_unit == "km" or "moon" in tg: return "moon"
        return "planet"
    return None


SKIP_PAGES = {"AGENTS.md", "CLAUDE.md"}
EXPLICIT = {
 "Orpheus and Eurydice System/Formoquens": "species", "Nimvion System/Morphfiends": "species", "Tom and Jerry and Nibbles/Pedonpods": "species",
 "BD−08°2823 System/Pumper Beetles": "species", "Skemer/Skemer-mense": "species", "Altmania System/Dichlorans": "species",
 "Lytherin System/Lytherin Empire": "civilization", "Aethonix System/Glaciumite": "mineral",
 "Milky Way/Sagittarius A*": "black-hole", "Tom and Jerry and Nibbles/Tom (black hole)": "black-hole",
 "Aquatikiverse": "hub", "Ghulheim–Ferruva system/Ghulheim and Ferruva": "system", "Tom and Jerry and Nibbles/Tom and Jerry and Nibbles": "system",
 "Aethonix System/Aethonix": "star", "Altmania System/Altmania": "star", "Lytherin System/Lytherin": "star", "Chiaroscuro System/Chiaroscuro": "star",
 "Orpheus and Eurydice System/Orpheus and Eurydice": "star", "Boreads System/Calais and Zetes": "star", "Trigeminal System/Trigemina": "star",
 "Nimvion System/Aurion and Argyra": "planet", "Ɬiʔa System/Shield Couple": "planet",
}
def link_of(v):
    return re.sub(r"\s+", " ", v.replace("\\|", "|").strip()) if v else None
def sanitize(v):
    if isinstance(v, str):
        v = v.strip()
        while v.endswith(")") and v.count(")") > v.count("("): v = v[:-1].rstrip()
        while v.startswith("(") and v.count("(") > v.count(")"): v = v[1:].lstrip()
    return v
def slug_of(h):
    h = re.sub(r"\([^)]*\)", "", clean(h)).strip()
    toks = h.split()
    if toks and len(toks[-1]) == 1: return toks[-1].lower()
    return re.sub(r"[^a-z0-9]+", "_", (toks[0] if toks else h).lower().replace("ɬ", "l")).strip("_") or "c"

def handle(lab, val, store, unp, srcname):
    """parse one table row into `store` (dict field -> (value, extras))"""
    if lab in ("orbital and rotation period", "orbital / rotation period"):
        v, ex, note = parse_cell("period_days", "q:period_days", val)
        if v is not None:
            store.setdefault("period_days", (v, ex)); store.setdefault("rotation_period_hours", (v * 24, {})); store.setdefault("tidally_locked", (True, {}))
        else: unp.append((srcname, val[:70], "orbital and rotation period: " + note))
        return
    # generic combined row: several labels separated by ' / ' with values separated by ' / ' or ';'
    if " / " in lab:
        lparts = [x.strip() for x in lab.split(" / ")]
        vparts = [x.strip() for x in re.split(r"\s+/\s+|;\s*", val.replace("**", "")) if x.strip()]
        if len(lparts) == len(vparts):
            for lp, vp in zip(lparts, vparts): handle(lp, vp, store, unp, srcname + " [" + lp + "]")
            return
        fld, kind = label_match(lab)
        if fld is None:
            unp.append((srcname, val[:70], "combined row: label/value counts differ")); return
    fld, kind = label_match(lab)
    if kind == "ignore": ignored[lab] += 1; return
    if fld is None:
        notable[lab] += 1; unp.append((srcname, val[:70], "unmapped label")); return
    if kind == "x":
        key = {"apoastron": "apoastron", "aphelion": "apoastron", "periastron": "periastron", "perihelion": "periastron"}.get(lab)
        u, v = semimajor_fields(0, clean(val))
        if key and v is not None: store.setdefault(key + ("_au" if u == "au" else "_km"), (v, {}))
        else: unp.append((srcname, val[:70], "apsis not parsed"))
        return
    if fld in ("semimajor", "hill_radius_km"):
        u, v = semimajor_fields(0, clean(val))
        if v is None: unp.append((srcname, val[:70], fld + ": no unit match")); return
        if fld == "semimajor": store.setdefault("semimajor_" + u, (v, {}))
        else: store.setdefault("hill_radius_km", (v if u == "km" else v * AU, {}))
        return
    v, ex, note = parse_cell(fld, kind, val)
    if v is None:
        if kind != "skip": unp.append((srcname, val[:70], note))
        return
    if note: unp.append((srcname, val[:70], "NOTE: " + note))
    store.setdefault(fld, (v, ex))

pages = read_pages()
results = {}; unparsed = collections.defaultdict(list); mism = collections.defaultdict(list)
multicol = []; notable = collections.Counter(); ignored = collections.Counter(); extra_tables = collections.defaultdict(list)

def finalise(raw, cls, p, fmout):
    """canonical fields from a raw field dict; returns nothing, writes into fmout"""
    stellar = cls == "star"
    def put(k, v, ex=None):
        if v is None: return
        if isinstance(v, float): v = float("%.6g" % v)
        fmout[k] = sanitize(v) if isinstance(v, str) else v
        if ex and "min" in ex:
            fmout[k + "_min"] = float("%.6g" % ex["min"]); fmout[k + "_max"] = float("%.6g" % ex["max"])
    if "mass" in raw: put("mass_sun" if stellar else "mass_earth", raw["mass"][0] / (MSUN if stellar else MEARTH))
    if "radius" in raw: put("radius_sun" if stellar else "radius_earth", raw["radius"][0] / (RSUN if stellar else REARTH))
    if "radius_polar" in raw: put("radius_polar_earth", raw["radius_polar"][0] / REARTH)
    if "system_mass_sun" in raw: put("system_mass_sun", raw["system_mass_sun"][0] / MSUN)
    for k in ("luminosity_sun", "system_luminosity_sun", "teff_k", "metallicity_feh", "age_gyr", "distance_ly", "ra_hours", "dec_deg", "absolute_magnitude_v", "apparent_magnitude_v"):
        if k in raw: put(k, raw[k][0], raw[k][1])
    for k in raw:
        if k.startswith(("semimajor_", "periastron_", "apoastron_", "hill_radius", "orbital_speed", "roche_limit", "rotation_speed")): put(k, raw[k][0])
    for k in ("eccentricity", "inclination_deg", "obliquity_deg", "period_days", "rotation_period_hours" if not stellar else "_skip", "tidally_locked", "flux_earth", "albedo_bond", "albedo_geometric",
              "temperature_eq_k", "temperature_mean_k", "pressure_surface_bar", "scale_height_km", "moons_count", "flattening", "moment_of_inertia_factor"):
        if k in raw: put(k, raw[k][0], raw[k][1])
    for k in ("spectral_type", "constellation", "named_after", "discoverer", "discovery_method", "discovery_site", "discovery_year", "adjectives", "alt_names",
              "solvent", "backbone", "primary_metabolism", "redox_couples", "membrane_chemistry", "photosynthesis_band_nm", "biosphere_age_gyr", "seeding_origin",
              "dominant_lifeforms", "ecosystems", "biosphere_state", "intelligent_species", "civilization_level", "surface_coverage"):
        if k in raw: put(k, raw[k][0])
    if stellar and "rotation_period_hours" in raw: put("rotation_period_days", raw["rotation_period_hours"][0] / 24)
    if cls == "biosphere" and "age_gyr" in fmout and "biosphere_age_gyr" not in fmout:
        fmout["biosphere_age_gyr"] = fmout.pop("age_gyr")
    if not stellar and "mass_earth" in fmout and "radius_earth" in fmout:
        M = fmout["mass_earth"] * MEARTH; Rm = fmout["radius_earth"] * REARTH * 1000
        calc = {"density_gcc": M / (4 / 3 * math.pi * Rm ** 3) / 1000, "gravity_ms2": G * M / Rm ** 2, "escape_kms": math.sqrt(2 * G * M / Rm) / 1000,
                "area_km2": 4 * math.pi * (Rm / 1000) ** 2, "volume_km3": 4 / 3 * math.pi * (Rm / 1000) ** 3, "circumference_km": 2 * math.pi * Rm / 1000}
        tol = {"density_gcc": .04, "gravity_ms2": .04, "escape_kms": .04, "area_km2": .04, "volume_km3": .06, "circumference_km": .02}
        for k, cv in calc.items():
            if k in raw:
                sv = raw[k][0]
                if sv and abs(cv - sv) / sv > tol[k]: mism[p].append((k, sv, cv, abs(cv - sv) / sv))
            fmout[k] = float("%.6g" % cv)
    elif not stellar:
        for k in ("density_gcc", "gravity_ms2", "escape_kms", "area_km2", "volume_km3", "circumference_km"):
            if k in raw: fmout[k] = float("%.6g" % raw[k][0])

for p in pages:
    if p in SKIP_PAGES: continue
    rel = p[:-3]
    t = open(p, encoding="utf-8").read()
    fm, body = front(t)
    tags = old_list(fm, "tags"); aliases = old_list(fm, "aliases")
    raw = collections.OrderedDict(); comps = collections.OrderedDict()
    semi_unit = None; tables_used = 0; primary_done = False
    for head, rows in tables_in(body):
        hc = split_row(head)
        if not hc or not re.match(r"^(\*\*)?(property|quantity|parameter|attribute)(\*\*)?$", hc[0].strip(), re.I): continue
        if len(hc) > 2 and not re.search(r"value|reference|adopted|description|status|stage|current|working|notes", hc[1].lower()):
            # multi-component table: columns are bodies
            multicol.append((p, hc))
            for ci in range(1, len(hc)):
                sg = slug_of(hc[ci]); store = comps.setdefault(sg, collections.OrderedDict())
                for ln in rows:
                    c = split_row(ln)
                    if len(c) <= ci: continue
                    handle(clean(c[0]).lower().strip(" :"), c[ci], store, unparsed[p], c[0] + " (" + sg + ")")
            continue
        if primary_done: extra_tables[p].append(hc); continue
        tables_used += 1; before = len(raw)
        for ln in rows:
            c = split_row(ln)
            if len(c) < 2: continue
            handle(clean(c[0]).lower().strip(" :"), c[1], raw, unparsed[p], c[0])
        if len(raw) - before >= 3: primary_done = True
    for k in list(raw):
        if k.startswith("semimajor_"): semi_unit = k.split("_")[1]
    cls = EXPLICIT.get(rel)
    if cls is None and rel.startswith("Encyclopedia/"): cls = "encyclopedia"
    if cls is None and rel.endswith(" System") : cls = "system"
    if cls is None: cls = guess_class(raw.keys(), tags, p, semi_unit)
    fmout = collections.OrderedDict()
    if cls: fmout["type"] = cls
    # identity: existing YAML first, table second
    for key, ykeys in (("system", ["system"]), ("star", ["star", "stars"]), ("planet", ["planet"]), ("host", [])):
        val = None
        for yk in ykeys:
            val = old_val(fm, yk)
            if val: break
        if not val and key in raw: val = link_of(raw[key][0])
        if val: fmout[key] = val
    if cls == "star" and comps:
        finalise(raw, cls, p, fmout)
        for sg, st in comps.items():
            sub_out = collections.OrderedDict(); finalise(st, "star", p, sub_out)
            for k, v in sub_out.items():
                if k != "type": fmout[sg + "_" + k] = v
        fmout["components"] = list(comps.keys())
    else:
        finalise(raw, cls, p, fmout)
        if comps:
            for sg, st in comps.items():
                sub_out = collections.OrderedDict(); finalise(st, cls or "planet", p, sub_out)
                for k, v in sub_out.items():
                    if k != "type": fmout[sg + "_" + k] = v
            fmout["components"] = list(comps.keys())
    if "system" not in fmout and cls not in ("encyclopedia", "hub", None):
        folder = rel.split("/")[0] if "/" in rel else None
        fb = {"Ghulheim–Ferruva system": "[[Ghulheim and Ferruva]]", "Tom and Jerry and Nibbles": "[[Tom and Jerry and Nibbles]]", "Skemer": "[[Skemer]]", "Milky Way": None}
        if folder in fb: sysl = fb[folder]
        else: sysl = "[[" + folder + "]]" if folder else None
        if sysl and not (cls == "system" and sysl.strip("[]") == rel.split("/")[-1]): fmout["system"] = sysl
    if cls == "star":
        for old, new_ in (("semimajor_au", "binary_separation_au"), ("eccentricity", "binary_eccentricity"), ("period_days", "binary_period_days"), ("inclination_deg", "binary_inclination_deg")):
            if old in fmout: fmout[new_] = fmout.pop(old)
    cover = re.search(r"!\[\[images/([^\]|]+)", body)
    results[p] = {"existing_aliases": aliases, "existing_tags": tags, "class": cls, "proposed": fmout,
                  "cover_candidate": cover.group(1) if cover else None, "tables_used": tables_used}

# ---------------------------------------------------------------- outputs
with open("AIOS/scripts/2026-11-14_frontmatter_extract.json", "w", encoding="utf-8") as f:
    json.dump({"constants": {"G": G, "MEARTH": MEARTH, "REARTH": REARTH, "MSUN": MSUN, "RSUN": RSUN, "LSUN": LSUN, "AU": AU},
               "pages": results}, f, ensure_ascii=False, indent=1)

pages = [p for p in pages if p in results]
n_pages = len(pages); with_props = [p for p in pages if results[p]["proposed"] and len(results[p]["proposed"]) > 1]
cls_ct = collections.Counter(results[p]["class"] for p in pages)
R = []
R.append("# Frontmatter extraction report (dry run)\n")
R.append("Private review report from `AIOS/scripts/2026-11-14_frontmatter_extract.py`. **No page has been changed.** The proposed frontmatter for every page is in `AIOS/scripts/2026-11-14_frontmatter_extract.json`.\n")
R.append(f"- Content pages scanned: **{n_pages}**; pages with at least one extracted property: **{len(with_props)}**.")
R.append("- Class guesses: " + ", ".join(f"{k or 'none'} {v}" for k, v in cls_ct.most_common()) + ".")
R.append(f"- Pages with unparsed or unmapped table rows: **{len(unparsed)}** (**{sum(len(v) for v in unparsed.values())}** rows).")
R.append(f"- Pages where a computed bulk value disagrees with the page's own table: **{len(mism)}** (**{sum(len(v) for v in mism.values())}** values).")
R.append(f"- Multi-column property tables not extracted (multi-body pages): **{len(multicol)}**.\n")
R.append("## Mismatches between the page's table and the value computed from its mass and radius\n")
R.append("Tolerances: 4% for density, gravity, escape speed and area; 6% volume; 2% circumference. The frontmatter would carry the computed value.\n")
R.append("| Page | Field | Page says | Computed | Difference |"); R.append("| --- | --- | --- | --- | --- |")
for p in sorted(mism):
    for k, sv, cv, rel in mism[p]:
        R.append(f"| {p[:-3]} | {k} | {sv:.6g} | {cv:.6g} | {100*rel:.1f}% |")
R.append("\n## Additional property tables skipped (only the first full table per page is used)\n")
for p_, hcs in sorted(extra_tables.items()): R.append(f"- {p_[:-3]}: {len(hcs)} more table(s), first columns: {', '.join(hcs[0])}")
R.append("\n## Multi-column tables not extracted\n")
for p, hc in multicol: R.append(f"- {p[:-3]}: columns {', '.join(h for h in hc)}")
R.append("\n## Labels deliberately ignored (not properties)\n")
R.append(", ".join(f"{l} ({n})" for l, n in ignored.most_common()))
R.append("\n## Unmapped labels (count of rows)\n")
R.append(", ".join(f"{l} ({c})" for l, c in notable.most_common(80)))
R.append("\n## Rows that could not be parsed, by page\n")
for p in sorted(unparsed):
    R.append(f"**{p[:-3]}**")
    for lab, val, note in unparsed[p][:14]: R.append(f"- `{clean(lab)}` = `{val}` — {note}")
    if len(unparsed[p]) > 14: R.append(f"- … and {len(unparsed[p]) - 14} more")
    R.append("")
R.append("## Sample proposed frontmatter\n")
SAMPLES = ["Ɬiʔa System/Middle Path.md", "Aethonix System/Aethonix.md", "Gammal System/Dold-Pärla.md", "Aethonix System/Life on Lunara.md", "Sol System/Earth.md", "Thrírlitir System/Valen.md"]
def yv(v):
    if isinstance(v, list): return "\n" + "\n".join("  - " + json.dumps(x, ensure_ascii=False) for x in v)
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    return str(v)
for s in SAMPLES:
    if s in results:
        R.append(f"### {s[:-3]}\n\n```yaml\n---")
        for k, v in results[s]["proposed"].items(): R.append(f"{k}: {yv(v)}")
        R.append("---\n```\n")
open("AIOS/frontmatter-extraction-report.md", "w", encoding="utf-8").write("\n".join(R) + "\n")
print("pages", n_pages, "| with properties", len(with_props), "| classes", dict(cls_ct))
print("unparsed pages", len(unparsed), "rows", sum(len(v) for v in unparsed.values()), "| mismatch pages", len(mism), "values", sum(len(v) for v in mism.values()), "| multicol", len(multicol))
