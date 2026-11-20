"""One-off frontmatter corrections found while building List of Planets. Run from vault root with python3 -I."""
import math, re
G = 6.67430e-11; ME = 5.9722e24; RE = 6371.0
def derived(m, r):
    mk = m * ME; rm = r * RE * 1000
    f = lambda x: float(f"{x:.6g}")
    return {"density_gcc": f(mk / (4 / 3 * math.pi * rm ** 3) / 1000), "gravity_ms2": f(G * mk / rm ** 2),
            "escape_kms": f(math.sqrt(2 * G * mk / rm) / 1000), "area_km2": f(4 * math.pi * (r * RE) ** 2),
            "volume_km3": f(4 / 3 * math.pi * (r * RE) ** 3), "circumference_km": f(2 * math.pi * r * RE)}
def fmt(v):
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, float) and v == int(v) and abs(v) < 1e15: return str(int(v))
    if isinstance(v, (int, float)): return repr(v)
    return '"' + v + '"'
def rewrite(path, drop, new):
    s = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", s, re.S)
    lines = m.group(1).split("\n"); out = []; skip = False
    for l in lines:
        k = re.match(r"^([A-Za-z_][\w]*):", l)
        if k:
            skip = k.group(1) in drop or k.group(1) in new
        if not skip: out.append(l)
    # insert new fields before cover
    ins = [f"{k}: {fmt(v)}" for k, v in new.items()]
    if out and out[-1].startswith("cover:"): out = out[:-1] + ins + [out[-1]]
    else: out += ins
    open(path, "w", encoding="utf-8").write("---\n" + "\n".join(out) + "\n---\n" + s[m.end():])

T = "Tom and Jerry and Nibbles/"
rewrite(T + "Jerry (gas giant).md", {"type", "mass_sun", "radius_sun", "spectral_type", "rotation_period_days", "binary_separation_au", "binary_inclination_deg"},
        {"mass_earth": 3814.0, "radius_earth": 12.34, "semimajor_au": 50, "period_days": 57.75, "rotation_period_hours": 8, "flux_earth": 0.8, "albedo_bond": 0.6, **derived(3814.0, 12.34)})
# put type first
p = T + "Jerry (gas giant).md"; s = open(p, encoding="utf-8").read(); open(p, "w", encoding="utf-8").write(s.replace("---\n", '---\ntype: "planet"\n', 1))
rewrite(T + "Nibbles (habitable moon).md", {"type", "mass_sun", "radius_sun", "spectral_type", "binary_period_days", "moons_count"},
        {"mass_earth": 0.4, "radius_earth": 0.7, "semimajor_km": 1000000, "period_days": 1.865, "flux_earth": 0.8, "albedo_bond": 0.3, "moons_count": 0, **derived(0.4, 0.7)})
p = T + "Nibbles (habitable moon).md"; s = open(p, encoding="utf-8").read(); open(p, "w", encoding="utf-8").write(s.replace("---\n", '---\ntype: "moon"\n', 1))
rewrite("Lytherin System/Zucchero.md", set(), {"radius_earth": 6.8, "density_gcc": 0.056, "circumference_km": float(f"{2*math.pi*6.8*RE:.6g}")})
rewrite("Chiaroscuro System/Euryphessa.md", set(), {"radius_earth": 13.45, "circumference_km": float(f"{2*math.pi*13.45*RE:.6g}")})
rewrite("Gammal System/Dold-Pärla.md", {"system", "star"}, {"system": "[[Gammal System]]", "star": "[[Gammal]]", "host": "[[Storebror]]"})
rewrite("Ghulheim–Ferruva system/Ferruva.md", set(), {"host": "[[Ghulheim]]", "semimajor_au": 0.05, "period_days": 16.96})
rewrite("Ɬiʔa System/Shield Couple.md", set(), {"semimajor_au": 1.5})
rewrite("Aethonix System/Lunara.md", set(), {"host": "[[Noctilux]]"})
# Mot is an ice giant, not a star
rewrite("Thrírlitir System/Mot.md", {"type", "mass_sun", "radius_sun", "teff_k", "rotation_period_days", "binary_separation_au", "binary_eccentricity", "binary_period_days", "binary_inclination_deg"},
        {"mass_earth": 30, "radius_earth": 5.34, "semimajor_au": 117, "eccentricity": 0.09, "inclination_deg": 1.6, "period_days": 289278, "rotation_period_hours": 11.2, **derived(30, 5.34)})
p = "Thrírlitir System/Mot.md"; s = open(p, encoding="utf-8").read(); open(p, "w", encoding="utf-8").write(s.replace("---\n", '---\ntype: "planet"\n', 1))
# Gigafusc is a brown dwarf orbiting Stellula
rewrite("Stellula System/Gigafusc.md", {"type", "binary_separation_au", "binary_eccentricity", "binary_period_days", "binary_inclination_deg", "rotation_period_days"},
        {"semimajor_au": 0.1, "eccentricity": 0.0, "period_days": 37.8, "inclination_deg": 0, "rotation_period_hours": 4})
p = "Stellula System/Gigafusc.md"; s = open(p, encoding="utf-8").read(); open(p, "w", encoding="utf-8").write(s.replace("---\n", '---\ntype: "brown-dwarf"\n', 1))
print("done")
