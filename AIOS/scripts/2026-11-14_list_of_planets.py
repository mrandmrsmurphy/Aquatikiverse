"""Build List of Planets.md from page frontmatter. Run from the vault root with python3 -I.
Re-run after frontmatter changes; the output file is overwritten."""
import os, re

SYSTEM_ORDER = ["Ɬiʔa System", "Aethonix System", "Lytherin System", "Altmania System", "Skemer", "Gammal System",
                "Ghulheim–Ferruva system", "Boreads System", "Tom and Jerry and Nibbles", "BD−08°2823 System",
                "Chiaroscuro System", "Nimvion System", "Methuselan System", "Stellula System", "Thrírlitir System",
                "Orpheus and Eurydice System"]
HUB = {"Ghulheim–Ferruva system": "Ghulheim and Ferruva"}


def fm(path):
    s = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", s, re.S)
    d = {}
    for l in m.group(1).split("\n"):
        k = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", l)
        if k: d[k.group(1)] = k.group(2).strip().strip('"')
    return d


def num(d, k):
    try: return float(d[k])
    except Exception: return None


def f(x, sig=3):
    if x is None: return "—"
    if x == 0: return "0"
    if abs(x) >= 1000 and abs(x) < 1e7: return f"{int(float(f'{x:.3g}')):,}"
    if abs(x) >= 1e7 or abs(x) < 1e-3:
        m, e = f"{x:.3g}e0".replace("e+", "e").split("e")[:2] if "e" in f"{x:.3g}" else (f"{x:.3g}", "0")
        return f"{m}×10^{int(e)}^" if False else f"{x:.2e}".replace("e+0", "e+").replace("e-0", "e-")
    return f"{x:.{sig}g}"


COLS = ["World", "Mass (M⊕)", "Radius (R⊕)", "Density (g/cm³)", "Gravity (m/s²)", "Semimajor axis (AU)", "Period (d)", "Flux (F⊕)", "Mean temp. (K)"]


def row(name, d):
    link = f"[[{name}]]"
    if d.get("type") == "moon" and d.get("host"):
        link += f" (moon of {d['host']})"
    elif name == "Aurion and Argyra" or name == "Shield Couple":
        link += " (pair)"
    return "| " + " | ".join([link, f(num(d, "mass_earth")), f(num(d, "radius_earth")), f(num(d, "density_gcc")),
                              f(num(d, "gravity_ms2")), f(num(d, "semimajor_au")), f(num(d, "period_days")),
                              f(num(d, "flux_earth")), f(num(d, "temperature_mean_k"), 4)]) + " |"


def collect(folder):
    out = []
    for fn in os.listdir(folder):
        if not fn.endswith(".md"): continue
        d = fm(os.path.join(folder, fn))
        if d.get("type") in ("planet", "moon", "dwarf-planet") and "mass_earth" in d:
            if "brown-dwarfs" in open(os.path.join(folder, fn), encoding="utf-8").read().split("\n---")[0]: continue
            out.append((fn[:-3], d))
    # order: planets by semimajor axis, moons after their planets as they sort (no axis -> end)
    out.sort(key=lambda x: (num(x[1], "semimajor_au") is None, num(x[1], "semimajor_au") or 0, x[0]))
    return out


lines = ["---", 'type: "hub"', "tags:", '  - "aquatikiverse"', '  - "home"', '  - "reference"', 'status: "complete"', "---", "",
         "# List of Planets", "",
         "Every planet and moon in the Aquatikiverse with its bulk and orbital properties, grouped by system. The values are the properties at the top of each world's page, in the units listed in [[Glossary]]; a dash means the page does not state that quantity. Within a system, worlds run outward by semimajor axis, and moons and rogue worlds follow.", "",
         "Flux is the stellar flux at the world's orbit. Mean temperature is the adopted mean surface temperature. For the pair pages ([[Aurion and Argyra]], [[Shield Couple]]) the row gives the first-named world's properties. Brown dwarfs have their own table below, and the real [[Sol System]] is listed last as a yardstick.", ""]
total = 0
for folder in SYSTEM_ORDER:
    rows = collect(folder)
    if not rows: continue
    total += len(rows)
    hub = HUB.get(folder, folder)
    lines += [f"## [[{hub}]]", "", "| " + " | ".join(COLS) + " |", "| " + " | ".join(["---"] * len(COLS)) + " |"]
    lines += [row(n, d) for n, d in rows]
    lines.append("")
# brown dwarfs
bd = []
for fp in ["Ghulheim–Ferruva system/Ghulheim.md", "Chiaroscuro System/Umbryl.md", "Stellula System/Gigafusc.md"]:
    d = fm(fp); n = os.path.basename(fp)[:-3]
    m_sun = num(d, "mass_sun")
    if m_sun is None and num(d, "mass_earth"): m_sun = num(d, "mass_earth") * 5.9722e24 / 1.98847e30
    r_sun = num(d, "radius_sun")
    if r_sun is None and num(d, "radius_earth"): r_sun = num(d, "radius_earth") * 6371 / 695700
    bd.append((n, d, m_sun, r_sun))
lines += ["## Brown dwarfs", "", "Substellar objects in solar units.", "",
          "| Object | Mass (M☉) | Radius (R☉) | Semimajor axis (AU) | Period (d) |", "| --- | --- | --- | --- | --- |"]
for n, d, m, r in bd:
    lines.append(f"| [[{n}]] | {f(m)} | {f(r)} | {f(num(d,'semimajor_au'))} | {f(num(d,'period_days'))} |")
lines.append("")
sol = collect("Sol System")
sol.sort(key=lambda x: num(x[1], "semimajor_au") or 0)
lines += ["## [[Sol System]]", "", "| " + " | ".join(COLS) + " |", "| " + " | ".join(["---"] * len(COLS)) + " |"] + [row(n, d) for n, d in sol] + [""]
open("List of Planets.md", "w", encoding="utf-8").write("\n".join(lines))
print("worlds in systems:", total, "| sol:", len(sol), "| brown dwarfs:", len(bd))
