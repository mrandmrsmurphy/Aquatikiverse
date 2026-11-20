---
name: yaml-frontmatter-goals
description: User's goals for the YAML/frontmatter rewrite (2026-11-14): infobox tables become comparable numeric properties in common units; all wiki-import YAML is junk and goes.
metadata:
  type: project
---

The user has BIG goals for frontmatter. Most of the tables that were templates on the MediaWiki (radius, density, mass, surface area, volume, gravity, flux, period, and so on) should become frontmatter PROPERTIES, in the SAME UNITS across every page so bodies are directly comparable. All the source YAML (source, wiki_assessment, source_categories, source_exhausted, source_disposition, source_content_sha256, reconciliation stage fields, date stamps, retired aliases) is 'importation junk' and goes. This supersedes the earlier lighter 'rich schema' idea ([[vault-cleanup-plan]] interview answer 10: aliases, tags, type, system, status, linked star and planet, cover image, no dates), which still applies as the non-physical part.

**Why:** the vault's point is integrated physics, chemistry and biology practice across many invented worlds; comparable numeric properties make worlds sortable and checkable against each other (and against the Sol System pages, which already use sourced tables).
**How to apply:** design the schema FIRST with the user (units per quantity, field names, numeric-only values, body classes: star, planet, moon, dwarf/minor body, system, biosphere, species), then script the extraction from the existing infobox tables, check each value against the page text, and only then rewrite frontmatter, with a confirmed fresh zip first. Numbers in frontmatter must be plain numbers (no units or ranges in the value; units live in the field name), so Obsidian Bases/Dataview can sort and compare. Keep the body tables for readers unless the user says otherwise. Related: [[reconciliation-files-removal]].

**Design decisions (user, 2026-11-14; all four were the recommended options):** (1) UNITS: Earth units for planets, moons and dwarfs (mass_earth, radius_earth, flux_earth, semimajor_au), solar units for stars (mass_sun, radius_sun, luminosity_sun, teff_k), with area, volume, density and gravity in km², km³, g/cm³ and m/s²; field names carry the unit and values are plain numbers. (2) DERIVED values (density, gravity, escape speed, surface area, volume, circumference): COMPUTE from mass and radius with one fixed constants set (the Encyclopedia/scripts set) and FLAG pages whose own table disagrees, for the user's review before anything is written. (3) QUALIFIED values: store one plain representative number (drop '~', '≈', 'Approximately'), with paired `_min`/`_max` fields for ranges; per-star or per-epoch variants stay in the body. (4) SCOPE: ALL fields become frontmatter: physical numbers, plus biosphere fields (solvent, backbone, metabolism, redox couples, membrane, age, civilization level) and identity fields (system, star, planet, constellation, spectral type, named after).
**Process agreed:** schema first (show the user), then a dry-run extraction report in AIOS listing per-page values, unparsed rows and mismatches, then a confirmed fresh zip, then the rewrite. Survey facts (2026-11-14): 142 pages have a Property/Quantity table with 688 distinct row labels; most-used labels are Mass (84), Eccentricity (64), Mean radius (57), Surface gravity (53), Inclination (50), Semimajor axis (48), Escape velocity (48), Density (46); the Earth symbol appears as both ⊕ and 🜨; giants use M♃ or M_J.

**Draft schema written 2026-11-14:** `AIOS/frontmatter-schema.md` (rules, constants, field lists for stars, planets/moons/dwarfs, biospheres; species fields still to survey). A test mapping of the 2,568 property-table rows onto it covered 68% directly; the rest are discovery fields, combined rows ('gravity / escape speed'), and rarer quantities. NEXT: the user reviews the draft schema, then a dry-run extraction report (AIOS), then zip, then rewrite.

**Schema approved by the user (2026-11-14):** 'definitely looks right'; distance for stars is in LIGHT-YEARS (`distance_ly`), as drafted. Dry-run extraction script: `AIOS/scripts/2026-11-14_frontmatter_extract.py` (writes `AIOS/frontmatter-extraction-report.md` and `AIOS/scripts/2026-11-14_frontmatter_extract.json`; changes no page).

## Decisions after the dry run (2026-11-14)
- Two-world pair pages (Aurion and Argyra, Shield Couple): frontmatter describes the first-named world only (type `planet`); the other stays in the body. Eventually every world gets its own page, with no pairs.
- "Single temperature" rows count as mean surface (`temperature_mean_k`).
- Body volume typos fixed (Harth, Aialon, Valen).
- Body tables stay as written for now; an embedded view of the frontmatter is a later question.
- Apply-script overrides needed: Aurion and Argyra take values from the Aurion table (the extractor read the shared orbit table); Shield Couple mass_earth 5 (each component); Life on Crying Eye is type biosphere.

## Applied (2026-11-14)
- `AIOS/scripts/2026-11-14_frontmatter_apply.py` rewrote the YAML of all 152 content pages from the extractor JSON (type, aliases, tags, links, physical and biosphere properties, cover). All `source_*`, `wiki_*`, `reconciliation_stage` fields and the retired alias "Gliese 1237 c" are gone; bodies untouched; every block parses as YAML.
- Not yet done: species and civilization fields, `status` values beyond the 21 existing, body tables unchanged, 142 pages with unparsed table rows (527) — candidates for later fields. Extractor and apply scripts are one-shot; rerunning the extractor now would read the new frontmatter-era pages, so do not re-apply.

## Follow-ups found 2026-11-14 (List of Planets)
- Keep `List of Planets.md` generated from frontmatter (`AIOS/scripts/2026-11-14_list_of_planets.py`); never copy numbers from the old wiki table. The user wants every world to have its own page eventually (no pair pages).
- A Type column (terrestrial, ice giant, habitable...) is not built: tags are inconsistent. Candidate: a `kind` frontmatter property chosen per page, then a column.
- Star frontmatter needs an audit: BD−08°2823 mass_sun 0.02, Stellula 0.08, Trigemina/Aethonix/Lytherin/Chiaroscuro/Calais and Zetes hubs without star fields.
