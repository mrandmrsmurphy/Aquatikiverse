"""Redox reference calculations for Encyclopedia/Redox Chemistry.md.

Standard Gibbs energies of formation (298 K, kJ/mol): solutes at 1 M, gases at 1 atm,
solids pure. Values are standard textbook (NBS/CODATA-type) numbers entered from memory
and NOT yet checked against the tables; each reaction below is atom- and charge-balanced
by the script. Run with: python3 -I redox_reference.py
"""
import json, re, math, os

F = 96.485      # kJ per V per mol e-
R = 8.314e-3    # kJ/mol/K
T = 298.15
RT = R * T
LN10 = math.log(10)
EV = 96.485     # kJ/mol per eV

# name: (formula, charge, dGf)
S = {
 "H2": ("H2", 0, 0.0), "O2": ("O2", 0, 0.0), "N2": ("N2", 0, 0.0),
 "H2O": ("H2O", 0, -237.1), "H+": ("H", 1, 0.0),
 "CO2": ("CO2", 0, -394.4), "CH4": ("CH4", 0, -50.7),
 "HCO3-": ("HCO3", -1, -586.8),
 "NH4+": ("NH4", 1, -79.4), "NO2-": ("NO2", -1, -37.2), "NO3-": ("NO3", -1, -111.3),
 "SO4--": ("SO4", -2, -744.5), "HS-": ("HS", -1, 12.1),
 "H2O2": ("H2O2", 0, -134.1),
 "Fe++": ("Fe", 2, -78.9), "Fe+++": ("Fe", 3, -4.7),
 "Fe(OH)2": ("FeO2H2", 0, -486.5), "Fe(OH)3": ("FeO3H3", 0, -696.5),
 "CH2O": ("CH2O", 0, -152.9),   # one sixth of glucose (carbohydrate level)
 "SiH4": ("SiH4", 0, 56.9), "SiO2": ("SiO2", 0, -856.3),
}
DHF = {"SiH4": 34.3, "SiO2": -910.7, "H2O": -285.8, "O2": 0.0}  # kJ/mol (enthalpies)

def comp(f):
    d = {}
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", f):
        d[el] = d.get(el, 0) + (int(n) if n else 1)
    return d

def balance(left, right):
    def tot(side):
        atoms, ch = {}, 0
        for n, sp in side:
            f, c, _ = S[sp]
            for el, k in comp(f).items():
                atoms[el] = atoms.get(el, 0) + n * k
            ch += n * c
        return atoms, ch
    a, ca = tot(left); b, cb = tot(right)
    return a == b and ca == cb

def dG0(left, right):
    return sum(n * S[s][2] for n, s in right) - sum(n * S[s][2] for n, s in left)

def dG_pH(left, right, pH):
    """dG at given pH, all other activities 1 (solutes 1 M, gases 1 atm)."""
    nH = sum(n for n, s in right if s == "H+") - sum(n for n, s in left if s == "H+")
    return dG0(left, right) + nH * RT * LN10 * pH * (-1) * (-1) * 0 + nH * RT * math.log(10 ** (-pH))

def rx(text):
    def side(t):
        out = []
        for term in t.split(" + "):
            term = term.strip()
            m = re.match(r"(\d+)\s+(.*)", term)
            out.append((int(m.group(1)), m.group(2)) if m else (1, term))
        return out
    l, r = text.split(" -> ")
    return side(l), side(r)

RXNS = [
 # label, reaction, vault pages, role
 ("Knallgas (per O2)", "2 H2 + 1 O2 -> 2 H2O", "Earth reference", "forward"),
 ("Methanogenesis", "4 H2 + CO2 -> CH4 + 2 H2O", "Life on Azotia; Life on Neonova", "forward"),
 ("Sulfate reduction by H2", "4 H2 + SO4-- + H+ -> HS- + 4 H2O", "Life on Ferruva", "forward"),
 ("Sulfate-driven methane oxidation", "CH4 + SO4-- -> HCO3- + HS- + H2O", "Life on Ferruva", "forward"),
 ("Nitrate-driven methane oxidation", "5 CH4 + 8 NO3- + 8 H+ -> 5 CO2 + 4 N2 + 14 H2O", "Life on Nibbles", "forward"),
 ("Anammox", "NH4+ + NO2- -> N2 + 2 H2O", "Life on Nibbles", "forward"),
 ("Methane + nitrate to ammonium", "CH4 + NO3- + 2 H+ -> CO2 + NH4+ + H2O", "Life on Azotia", "forward"),
 ("Nitrate ammonification by H2", "NO3- + 4 H2 + 2 H+ -> NH4+ + 3 H2O", "Life on Ferruva", "forward"),
 ("Peroxide + hydrogen", "H2 + H2O2 -> 2 H2O", "Life on Oxhydra", "forward"),
 ("Peroxide + methane", "CH4 + 4 H2O2 -> CO2 + 6 H2O", "Life on Oxhydra", "forward"),
 ("Peroxide + sulfide", "HS- + 4 H2O2 -> SO4-- + 4 H2O + H+", "Life on Oxhydra", "forward"),
 ("Methane + ferric ion", "CH4 + 8 Fe+++ + 2 H2O -> CO2 + 8 Fe++ + 8 H+", "Life on Neonova", "forward"),
 ("Methane + ferric hydroxide", "CH4 + 8 Fe(OH)3 -> CO2 + 8 Fe(OH)2 + 6 H2O", "Life on Aphrod", "forward"),
 ("Photoferrotrophy (carbohydrate level)", "CO2 + 4 Fe(OH)2 + 3 H2O -> CH2O + 4 Fe(OH)3", "Life on Aphrod", "regeneration"),
 ("Water splitting (per O2)", "2 H2O -> 2 H2 + 1 O2", "Life on Skemer", "regeneration"),
 ("Peroxide from water and H2", "2 H2O -> H2 + H2O2", "Life on Ferruva (radiolysis)", "regeneration"),
 ("Oxygenic photosynthesis (carbohydrate level)", "CO2 + H2O -> CH2O + O2", "Earth reference", "regeneration"),
 ("Silane oxidation (per SiH4)", "SiH4 + 2 O2 -> SiO2 + 2 H2O", "Life on Middle Path", "forward"),
]

def main():
    out = {"constants": {"F_kJ_per_V": F, "RT_kJ": RT}, "reactions": []}
    for label, text, page, role in RXNS:
        L, Rr = rx(text)
        assert balance(L, Rr), "unbalanced: " + text
        g0 = dG0(L, Rr)
        # electrons transferred: use oxidation states is overkill; give per-reaction values only
        g7 = dG_pH(L, Rr, 7.0)
        out["reactions"].append({"label": label, "reaction": text, "pages": page, "role": role,
                                 "dG0_kJ": round(g0, 1), "dG_pH7_kJ": round(g7, 1)})
    # specific per-unit quantities
    ph = next(r for r in out["reactions"] if r["label"].startswith("Photoferrotrophy"))
    e_ph = 1.3 * EV
    out["photoferrotrophy"] = {"dG_kJ_per_C": ph["dG0_kJ"], "photons_per_C": 4,
        "photon_energy_eV": 1.3, "absorbed_kJ_per_mol_C": round(4 * e_ph, 1),
        "efficiency": round(ph["dG0_kJ"] / (4 * e_ph), 3)}
    dh = DHF["SiO2"] + 2 * DHF["H2O"] - DHF["SiH4"]
    dg = dG0(*rx("SiH4 + 2 O2 -> SiO2 + 2 H2O"))
    out["silane"] = {"dH_per_O2_kJ": round(dh / 2, 1), "dH_per_O2_eV": round(-dh / 2 / EV, 2),
                     "dG_per_O2_kJ": round(dg / 2, 1), "dG_per_O2_eV": round(-dg / 2 / EV, 2)}
    out["atp_context"] = {"ATP_synthesis_kJ_per_mol_cell": "about 50-70",
                          "minimum_quantum_kJ_per_reaction": "about 15-20 (about one third ATP)"}
    # Half-reaction table at pH 7 (E0', V): ox + n e- + m H+ -> red + k H2O
    halves = [
      ("O2 / H2O", "1 O2 + 4 H+ -> 2 H2O", 4),
      ("NO3- / N2", "2 NO3- + 12 H+ -> 1 N2 + 6 H2O", 10),
      ("NO3- / NO2-", "NO3- + 2 H+ -> NO2- + H2O", 2),
      ("NO2- / NH4+", "NO2- + 8 H+ -> NH4+ + 2 H2O", 6),
      ("H2O2 / H2O", "H2O2 + 2 H+ -> 2 H2O", 2),
      ("CO2 / CH2O", "CO2 + 4 H+ -> CH2O + H2O", 4),
      ("SO4-- / HS-", "SO4-- + 9 H+ -> HS- + 4 H2O", 8),
      ("CO2 / CH4", "CO2 + 8 H+ -> CH4 + 2 H2O", 8),
      ("H+ / H2", "2 H+ -> 1 H2", 2),
      ("Fe+++ / Fe++", "Fe+++ -> Fe++", 1),
      ("Fe(OH)3 / Fe(OH)2", "Fe(OH)3 + H+ -> Fe(OH)2 + H2O", 1),
    ]
    out["half_reactions_pH7"] = []
    for name, text, n in halves:
        # add n electrons conceptually: compute dG with e- at zero formation energy; charge balance
        # check by hand: left charge + (-n) == right charge
        l, r = text.split(" -> ")
        def side(t):
            o = []
            for term in t.split(" + "):
                m = re.match(r"(\d+)\s+(.*)", term.strip())
                o.append((int(m.group(1)), m.group(2)) if m else (1, term.strip()))
            return o
        L, Rr = side(l), side(r)
        ch = lambda s: sum(k * S[sp][1] for k, sp in s)
        assert ch(L) - n == ch(Rr), "charge: " + text
        g0 = dG0(L, Rr)
        nH = sum(k for k, sp in L if sp == "H+") - sum(k for k, sp in Rr if sp == "H+")
        gp = g0 + nH * RT * LN10 * 7.0   # consumed H+ at 1e-7 raises dG
        E = -gp / (n * F)
        out["half_reactions_pH7"].append({"couple": name, "half_reaction": text.replace("->", "+ %d e- ->" % n) if False else l + " + %d e- -> %s" % (n, r), "n": n, "E0prime_V": round(E, 3)})
    out["half_reactions_pH7"].sort(key=lambda d: d["E0prime_V"])
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "2026-11-14_redox_reference.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    for r in out["reactions"]:
        print(f"{r['label']:48s} dG0 {r['dG0_kJ']:9.1f}  pH7 {r['dG_pH7_kJ']:9.1f}")
    print(out["photoferrotrophy"]); print(out["silane"])
    for h in out["half_reactions_pH7"]:
        print(f"{h['couple']:22s} n={h['n']:2d}  E0' {h['E0prime_V']:+.3f} V")

main()
