"""Apply proposed frontmatter from 2026-11-14_frontmatter_extract.json to every page.
Replaces each page's YAML block; the body is never touched. Run from the vault root with python3 -I."""
import json, math, os, re, sys

ROOT = os.getcwd()
DATA = json.load(open("AIOS/scripts/2026-11-14_frontmatter_extract.json", encoding="utf-8"))["pages"]
G = 6.67430e-11; ME = 5.9722e24; RE = 6371.0
RETIRED_ALIASES = {"Gliese 1237 c"}
KEEP_TEXT = {"status"}


def derived(m, r):
    mk = m * ME; rm = r * RE * 1000
    return {
        "density_gcc": mk / (4 / 3 * math.pi * rm ** 3) / 1000,
        "gravity_ms2": G * mk / rm ** 2,
        "escape_kms": math.sqrt(2 * G * mk / rm) / 1000,
        "area_km2": 4 * math.pi * (r * RE) ** 2,
        "volume_km3": 4 / 3 * math.pi * (r * RE) ** 3,
        "circumference_km": 2 * math.pi * r * RE,
    }


def sig(x, n=6):
    return float(f"{x:.{n}g}")


OVERRIDES = {
    "Nimvion System/Aurion and Argyra.md": dict(
        mass_earth=200, radius_earth=10.6, rotation_period_hours=11, flux_earth=0.048,
        temperature_eq_k=120, albedo_bond=0.28, _derive=True),
    "Ɬiʔa System/Shield Couple.md": dict(mass_earth=5, _derive=True),
    "Ɬiʔa System/Life on Crying Eye.md": dict(type="biosphere"),
}


def fmt(v):
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, int): return str(v)
    if isinstance(v, float):
        return str(int(v)) if v == int(v) and abs(v) < 1e15 else repr(v)
    return json.dumps(v, ensure_ascii=False)


def emit(key, v):
    if isinstance(v, list):
        if not v: return []
        return [f"{key}:"] + [f"  - {fmt(x)}" for x in v]
    return [f"{key}: {fmt(v)}"]


def parse_existing(yaml):
    """Return dict of existing top-level scalar/link/list values we may carry over."""
    out = {}; cur = None
    for line in yaml.split("\n"):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            cur = m.group(1); val = m.group(2).strip()
            out[cur] = [] if val == "" else val.strip('"')
        elif cur and line.strip().startswith("- "):
            if not isinstance(out[cur], list): out[cur] = [out[cur]]
            out[cur].append(line.strip()[2:].strip().strip('"'))
    return out


changed = 0
for rel, info in DATA.items():
    path = os.path.join(ROOT, rel)
    s = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", s, re.S)
    if not m: print("no frontmatter:", rel); continue
    body = s[m.end():]
    ex = parse_existing(m.group(1))
    fm = dict(info["proposed"])
    ov = OVERRIDES.get(rel, {})
    derive = ov.pop("_derive", False) if ov else False
    fm.update(ov)
    if derive:
        fm.update({k: sig(v) for k, v in derived(fm["mass_earth"], fm["radius_earth"]).items()})
    # carry over identity links the extractor could not read
    for src, dst in (("system", "system"), ("star", "star"), ("stars", "star"), ("planet", "planet"),
                     ("home", "homeworld"), ("homeworld", "homeworld"), ("satellite_of", "host"),
                     ("parent_body", "host"), ("status", "status")):
        if src in ex and dst not in fm and isinstance(ex[src], str): fm[dst] = ex[src]
    if "adjective" in ex and "adjectives" not in fm: fm["adjectives"] = [ex["adjective"]]
    aliases = []
    for a in list(ex.get("aliases", [])) + list(fm.pop("alt_names", []) if isinstance(fm.get("alt_names"), list) else []):
        if a and a not in RETIRED_ALIASES and a not in aliases: aliases.append(a)
    if isinstance(fm.get("alt_names"), str): fm.pop("alt_names")
    tags = ex.get("tags", [])
    if isinstance(tags, str): tags = [tags]
    cover = fm.pop("cover", None) or info.get("cover_candidate")
    typ = fm.pop("type", None)
    lines = ["---"]
    if typ: lines += emit("type", typ)
    lines += emit("aliases", aliases) + emit("tags", tags)
    for k, v in fm.items(): lines += emit(k, v)
    if cover: lines += emit("cover", cover)
    lines.append("---\n")
    new = "\n".join(lines) + body
    if new != s:
        open(path, "w", encoding="utf-8").write(new); changed += 1
print("pages rewritten:", changed)
