---
type: "encyclopedia"
aliases:
  - "Redox"
  - "Biological energy"
  - "Metabolism and redox"
tags:
  - "aquatikiverse"
  - "encyclopedia"
  - "chemistry"
  - "biology"
status: "draft"
---

# Redox Chemistry

## Summary

All life runs on **redox reactions**: an electron donor hands electrons to an electron acceptor, and the drop in free energy pays for living. Every biosphere in the vault is built from a set of such reactions, the **forward set** that releases energy, and a **regeneration set** that undoes them by lifting the products back up to donor and acceptor. The forward half is easy to write. The regeneration half is the real constraint, because it costs at least as much energy as the forward half released, and that energy has to come from outside: starlight, geothermal heat, radioactive decay, or burial of carbon. Analysing a biosphere means checking that these two halves exist, balance atom for atom, and are powered by something the world actually has. Inventing one means choosing a couple, a solvent and a driver that fit together.

## Donors, acceptors and half-reactions

A redox reaction splits into two half-reactions. Each couple (oxidized form / reduced form) has a **reduction potential** E°′, measured in volts at a stated pH (biochemists use pH 7). A couple with a low (negative) E°′ is a good electron donor in its reduced form; one with a high E°′ is a good acceptor in its oxidized form. Stacking couples in order gives the **electron tower**:

| Couple (oxidized / reduced) | Electrons (n) | E°′ at pH 7 (V) |
| --- | --- | --- |
| CO₂ / CH₂O (carbohydrate) | 4 | −0.425 |
| H⁺ / H₂ | 2 | −0.414 |
| CO₂ / CH₄ | 8 | −0.245 |
| SO₄²⁻ / HS⁻ | 8 | −0.217 |
| Fe(OH)₃ / Fe(OH)₂ | 1 | −0.133 |
| NO₂⁻ / NH₄⁺ | 6 | +0.340 |
| NO₃⁻ / NO₂⁻ | 2 | +0.431 |
| NO₃⁻ / N₂ | 10 | +0.747 |
| Fe³⁺ / Fe²⁺ (dissolved, acidic) | 1 | +0.769 |
| O₂ / H₂O | 4 | +0.815 |
| H₂O₂ / H₂O | 2 | +1.348 |

Electrons flow downhill, from a reduced species high in the table to an oxidized species lower down, and the voltage gap sets the energy: **ΔG = −n F ΔE**, with F = 96.485 kJ per volt per mole of electrons. Hydrogen with oxygen has a gap of 0.815 − (−0.414) = 1.23 V across 4 electrons, which is 474 kJ per mole of O₂. Methane with sulfate has a gap of only 0.028 V across 8 electrons: ΔG° ≈ −17 kJ per mole of methane, which is why sulfate-driven methane oxidation is a life on the edge. Two of the entries are fragile in this scale: dissolved Fe³⁺ exists only in acid (at neutral or alkaline pH iron precipitates as Fe(OH)₃, whose potential is 0.9 V lower), and H₂O₂ is so oxidizing that it attacks most organic molecules and decomposes by itself.

## The energy ledger

For a reaction written out and balanced, the standard free-energy change is the sum of the formation energies of the products minus those of the reactants, and the real value shifts with concentration: **ΔG = ΔG° + RT ln Q**, where Q is the product-over-reactant activity ratio. Hydrogen ions count too, so a reaction that consumes H⁺ is more favourable in acid and one that releases H⁺ is more favourable in base (at pH 7 each H⁺ consumed adds 39.9 kJ to ΔG relative to pH 0).

Three benchmarks keep numbers in proportion:

- **ATP** costs roughly 50–70 kJ per mole to make inside a cell, so a reaction yielding −100 kJ pays for 1–2 ATP.
- **Minimum quantum:** a cell can only conserve energy from a reaction that yields about −15 to −20 kJ or more (about a third of an ATP, because the cell's proton pump moves ions in whole units). Below that, no organism can profit, whatever the chemistry says on paper.
- **Kinetics:** a large negative ΔG says a reaction is allowed, not that it happens. Most strongly favoured reactions (methane with oxygen, hydrogen with sulfur) are slow without a catalyst, and the catalyst is the enzyme or mineral surface. Biospheres exploit this: they live where a reaction is thermodynamically open but kinetically held shut.

## Closing the loop

A forward reaction turns donor + acceptor into waste products and releases free energy. If a biosphere only ran this, it would run out of donor and acceptor and stop. To last for billions of years it needs a **regeneration set** that turns the products back into donor and acceptor. By the second law, regeneration costs at least as much free energy as the forward set released, and in practice more. So a lasting biosphere is **materially cycling but energetically open**: atoms circulate, energy flows through from a source to heat.

The source is one of only a few types:

- **Light.** Photons lift electrons uphill. Oxygenic photosynthesis (CO₂ + H₂O → CH₂O + O₂, ΔG° = +479 kJ) rebuilds both carbohydrate and the oxygen that burns it. A photon of 1.3 eV carries 125 kJ per mole, so the +479 kJ of oxygenic photosynthesis needs at least 4 such photons even at perfect efficiency; real organisms use more (the standard figure is 8–10 photons, with bigger photons of about 1.8 eV), and the less energy per photon, the more photons each step needs.
- **Geothermal and geological disequilibrium.** Hot rock and water react to make H₂, H₂S, Fe²⁺ and CH₄ (reduced donors) at some places and leave oxidized crust at others. The biosphere's energy supply is the continuing separation of the two.
- **Radiolysis.** Ionizing radiation from decaying uranium, thorium and potassium splits water into H₂ and oxidants such as H₂O₂ (2 H₂O → H₂ + H₂O₂, +340 kJ per mole, paid by the radiation, not the organism).
- **Burial.** If part of the organic carbon (or silicon, in the silicon biosphere) is buried before it can react back, the unreacted oxidant accumulates as free O₂. Net oxygen production equals the burial rate, not the photosynthesis rate.
- **Escape.** If a world loses hydrogen to space, the planet is oxidized by the loss (the crust is left with fewer electrons to give). This slow oxidation recharges the acceptors of an iron-based biosphere.
- **Heat gradients.** A hot–cold contrast can drive redox cycling through a heat engine (convection carrying material between a reducing zone and an oxidizing zone), but a gradient is an energy source only while something maintains it.

Whichever source is chosen, the numbers must fit: the energy budget (watts, from light flux, tidal and radiogenic heat, or the redox inventory itself) divided by the cost per mole fixes how many moles of carbon per year the biosphere can process. That is the biosphere's productivity limit.

## Method: building a reaction set

A set of reactions for a speculative biosphere can be built and tested in nine steps. Each step is a question the numbers must answer.

1. **Fix the solvent and conditions.** The solvent (water, ammonia–water, liquid SO₂, a dry siloxane lattice) decides which species stay dissolved, which are stable, and what the pH or acidity scale means. A reaction set only works if neither partner reacts with the solvent: strongly oxidizing H₂O₂ or ClO₄⁻ is stable in water for a time but oxidizes SO₂-based or organic solvents.
2. **List the available elements and their oxidation states.** Which elements are common on the world and have two or more stable oxidation states that are close together in energy (C, H, N, O, S, Fe, Mn, As, I, U, Ce, Si)? These make the donors and acceptors.
3. **Pick a couple pair.** Choose one reduced couple as donor and one oxidized couple as acceptor with a large enough potential gap. Check the two E°′ values give at least −20 kJ per electron-pair, with margin for concentrations.
4. **Balance the reaction.** Atoms and charge must balance, with H₂O, H⁺ and OH⁻ added as the solvent allows. An unbalanced equation is the most common error in a draft and hides missing products.
5. **Compute ΔG at the environment's conditions.** Use the pH, temperature and concentrations of the actual niche, not the standard state. Check the product accumulation: a reaction that yields −17 kJ in a standard state may give zero at the concentrations the products reach.
6. **Write the reverse path.** List the reactions that turn each product back into donor and acceptor. Check that every waste is consumed by someone, or removed by a physical process (burial, outgassing, precipitation, escape).
7. **Name the driver.** The regeneration must be coupled to an energy source: photon, thermal gradient, radiolysis, burial or a geological supply. Compute the minimum photons (ΔG ÷ photon energy ÷ efficiency) or watts it needs.
8. **Check the throughput.** The energy source in watts per square metre and the cost per mole set the biosphere's mass of fixed carbon, which in turn must be consistent with the biomass and gas inventory the world page claims.
9. **Look for leaks.** What is lost permanently (hydrogen escape, burial of carbon, sequestered oxidant)? Is the loss replaced by something external over the life of the biosphere?

## Worked examples

All reaction energies below are computed from standard formation energies for the reactions as written on the vault pages (298 K, solutes at 1 M, gases at 1 atm). "pH 7" differs from the standard state by the effect of the hydrogen ions each reaction consumes or releases.

### Forward reactions

| Reaction (as written on the page) | ΔG° (kJ) | ΔG at pH 7 (kJ) | World |
| --- | --- | --- | --- |
| 2 H₂ + O₂ → 2 H₂O | −474 | −474 | Earth reference |
| 4 H₂ + CO₂ → CH₄ + 2 H₂O | −131 | −131 | [[Life on Azotia]], [[Life on Neonova]] |
| 4 H₂ + SO₄²⁻ + H⁺ → HS⁻ + 4 H₂O | −192 | −152 | [[Life on Ferruva]] |
| CH₄ + SO₄²⁻ → HCO₃⁻ + HS⁻ + H₂O | −17 | −17 | [[Life on Ferruva]] |
| NH₄⁺ + NO₂⁻ → N₂ + 2 H₂O | −358 | −358 | [[Life on Nibbles]] |
| 5 CH₄ + 8 NO₃⁻ + 8 H⁺ → 5 CO₂ + 4 N₂ + 14 H₂O | −4,148 (−830 per CH₄) | −3,828 (−766 per CH₄) | [[Life on Nibbles]] |
| CH₄ + NO₃⁻ + 2 H⁺ → CO₂ + NH₄⁺ + H₂O | −549 | −469 | [[Life on Azotia]] |
| NO₃⁻ + 4 H₂ + 2 H⁺ → NH₄⁺ + 3 H₂O | −679 | −600 | [[Life on Ferruva]] |
| CH₄ + 8 Fe³⁺ + 2 H₂O → CO₂ + 8 Fe²⁺ + 8 H⁺ | −463 | (acid only) | [[Life on Neonova]] |
| CH₄ + 8 Fe(OH)₃ → CO₂ + 8 Fe(OH)₂ + 6 H₂O | −86 | −86 | [[Life on Aphrod]] |
| H₂ + H₂O₂ → 2 H₂O | −340 | −340 | [[Life on Oxhydra]] |
| CH₄ + 4 H₂O₂ → CO₂ + 6 H₂O | −1,230 | −1,230 | [[Life on Oxhydra]] |
| HS⁻ + 4 H₂O₂ → SO₄²⁻ + 4 H₂O + H⁺ | −1,169 | −1,209 | [[Life on Oxhydra]] |
| SiH₄ + 2 O₂ → SiO₂ + 2 H₂O | −1,387 | −1,387 | [[Life on Middle Path]] |

Reading the table is itself the analysis. The sulfate–methane reaction yields only −17 kJ, right at the minimum quantum, so a biosphere built on it can only be slow and thin. The iron–methane reaction on [[Aphrod]] yields −86 kJ because solid iron hydroxides are strongly bound, which is what limits its yield (about 1 ATP). The peroxide reactions of [[Oxhydra]] yield −340 to −1,230 kJ, far above the minimum, so peroxide organisms can afford to be sluggish and cold; the cost is that H₂O₂ itself takes +340 kJ per mole to make from water and H₂. Nitrate-driven methane oxidation on [[Nibbles (habitable moon)|Nibbles]] yields about −766 kJ per methane at pH 7, comparable with methane burning in oxygen (−818 kJ per CH₄ to CO₂ gas), so a nitrate-rich world can host a respiration as productive as oxygen's.

### Regeneration reactions

| Reaction | ΔG (kJ) | Driver |
| --- | --- | --- |
| CO₂ + H₂O → CH₂O + O₂ | +479 | Light |
| CO₂ + 4 Fe(OH)₂ + 3 H₂O → CH₂O + 4 Fe(OH)₃ | +113 | Light (4 photons of 1.3 eV, about 22% efficient) |
| 2 H₂O → 2 H₂ + O₂ | +474 | Electrical work ([[Life on Skemer]]) |
| 2 H₂O → H₂ + H₂O₂ | +340 | Radiolysis ([[Life on Ferruva]]) |

Photoferrotrophy is the regeneration half of Aphrod's loop: the iron–methane reaction oxidizes methane with Fe(OH)₃ and releases about 86 kJ, and photoferrotrophs run the reverse accounting by using starlight to oxidize Fe(OH)₂ back to Fe(OH)₃ while making carbohydrate. Per carbon fixed it needs +113 kJ, which four 1.3 eV photons (502 kJ per mole) pay with about 22% efficiency. The oxygen-making half of Earth's loop is the same kind of reaction at higher cost (+479 kJ), and the silicon biosphere of [[Middle Path]] uses a similar budget: oxidizing silane to silica consumes oxygen and releases 7.2 eV of free energy (7.9 eV of enthalpy) per O₂, so reducing silicon back from SiO₂ and water costs at least that much per O₂ freed, about 12 near-infrared photons at 50% efficiency, and burying the reduced silicon material is what leaves the free oxygen behind.

### Where the vault's reaction sets stand

Nine biospheres write out both halves ([[Life on Oxhydra]], [[Life on Nibbles]], [[Life on Dysmorph]], [[Life on Stygium]], [[Life on Aphrod]], [[Life on Azotia]], [[Life on Neonova]], [[Life on Thionis]], [[Life on Ferruva]]). A loop's quality comes from what powers it:

- **Light-driven, with a written reverse:** [[Life on Stygium]] (arsenite and arsenate in liquid SO₂), [[Life on Thionis]] (H₂S and sulfur), [[Life on Azotia]] (NH₃ split to H₂ by photons).
- **Radiation-driven:** [[Life on Nibbles]] makes nitrate from N₂ with Jerry-belt particles; [[Life on Dysmorph]] cycles uranium and cerium with a radiogenic pump; [[Life on Ferruva]] uses radiolysis.
- **Stored but not made:** [[Life on Oxhydra]] regenerates its peroxide carrier (Mg(OH)₂ + H₂O₂ → MgO₂ + 2 H₂O), which stores oxidant but creates none; the energy gain depends on a supply of H₂O₂ from radiation or geology.
- **Partly specified:** [[Life on Neonova]], [[Life on Skemer]], [[Life on Crying Eye]] and [[Life on Middle Path]] name the regeneration route and its driver in words or as a single half-reaction, but not as a balanced equation.

A loop is only as strong as its least specified step; the checks of the method above can be run on any of these pages.

## In the Aquatikiverse

The vault treats a biosphere's reaction set as the thing that connects a world's physics to its life. Climate fixes the temperature and solvent, the star fixes the photon supply, and the planet's geology fixes the donors, acceptors and radiogenic heat. The redox set is where those three meet, so most reconciliations in the vault were driven by it. For [[Aphrod]], changing the planetary ocean to 15–25% ammonia by weight and adopting photoferrotrophic recharge plus hydrogen escape made the iron–methane loop close. For the silicon biosphere of [[Middle Path]], the oxygen budget (the silicon biosphere as the O₂ source) came from asking which reaction regenerates the oxidant that the volcanoes consume. For [[Oxhydra]], the question "what makes the peroxide?" remains open, which is exactly the kind of gap the method is built to expose.

## References

- Thauer, Jungermann & Decker 1977, "Energy conservation in chemotrophic anaerobic bacteria", *Bacteriological Reviews* 41, 100–180: the standard table of E°′ values and free energies for microbial couples (cited from memory; not yet checked against the source).
- Schink 1997, "Energetics of syntrophic cooperation in methanogenic degradation", *Microbiology and Molecular Biology Reviews* 61, 262–280: the minimum energy quantum of about −20 kJ per reaction (cited from memory; not yet checked against the source).
- Stumm & Morgan, *Aquatic Chemistry* (3rd ed., 1996) and the NBS/CODATA thermodynamic tables: standard formation energies and pH-dependent redox calculations (textbook results; the values used here were entered from memory and not yet checked against the tables).
