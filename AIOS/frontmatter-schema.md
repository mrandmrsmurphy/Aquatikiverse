# Frontmatter schema (draft for review)

Private working specification for the YAML rewrite. Decisions behind it are in `AIOS/memory/project_yaml_frontmatter_goals.md`. Nothing here has been applied to any page yet.

## Rules

1. **Plain numbers only.** Every numeric field holds one number (`5.97`, `1.2e-4`), never text, units or `~`. The unit is part of the field name (`radius_earth`, `density_gcc`).
2. **One unit per quantity, everywhere.** Earth units for planets, moons and dwarf planets; solar units for stars and brown dwarfs; the fixed units below for everything else. No page may use another unit.
3. **Ranges** become paired `_min` and `_max` fields; the unsuffixed field is the representative value. Per-star, per-epoch or per-hemisphere variants stay in the body.
4. **Derived values are computed**, not copied: density, surface gravity, escape speed, surface area, volume and circumference come from mass and radius with the constants below. A page whose own table disagrees is listed in the review report.
5. **No provenance or dates.** No `source*`, `wiki_*`, hash, disposition, reconciliation or date-stamp fields. In-universe years (a discovery in 2294) are fine as numbers.
6. **Links** are quoted wikilinks (`"[[Ɬiʔa System]]"`); several links are a YAML list. Text properties are short strings or lists of strings.
7. Absent means unknown or unspecified: omit the field rather than write `null` or `unknown`.

## Constants (the set used for every derived value)

G = 6.67430×10⁻¹¹ m³ kg⁻¹ s⁻²; M⊕ = 5.9722×10²⁴ kg; R⊕ = 6371 km (mean); M☉ = 1.98847×10³⁰ kg; R☉ = 695,700 km; L☉ = 3.828×10²⁶ W; AU = 149,597,870.7 km; 1 yr = 365.25 d; 1 atm = 1.01325 bar; σ = 5.670374419×10⁻⁸ W m⁻² K⁻⁴; S⊕ = 1361 W/m².

## Fields shared by every page

| Field | Type | Meaning |
| --- | --- | --- |
| `type` | text | one of `system`, `star`, `brown-dwarf`, `planet`, `moon`, `dwarf-planet`, `minor-body`, `ring-belt`, `biosphere`, `species`, `civilization`, `encyclopedia`, `hub` |
| `aliases` | list | alternate names only (current names; no retired catalogue names) |
| `tags` | list | `aquatikiverse` plus topical tags |
| `system` | link | the system page |
| `status` | text | `draft` or `complete` |
| `cover` | text | image filename in `images/` |

## Stars and brown dwarfs (`type: star` or `brown-dwarf`)

| Field | Unit | Notes |
| --- | --- | --- |
| `spectral_type` | text | e.g. `K4V` |
| `mass_sun`, `radius_sun`, `luminosity_sun` | M☉, R☉, L☉ | |
| `teff_k` | K | effective temperature |
| `metallicity_feh` | dex | |
| `age_gyr` | Gyr | |
| `rotation_period_days` | d | |
| `distance_ly` | ly | from Earth |
| `ra_hours`, `dec_deg` | h, ° | J2000 |
| `constellation` | text | |
| `absolute_magnitude_v`, `apparent_magnitude_v` | mag | where given |
| `component_of` | link | for stars in a binary or triple |

## Planets, moons and dwarf planets

**Bulk** (independent: `mass_earth`, `radius_earth`; derived, computed: `density_gcc`, `gravity_ms2`, `escape_kms`, `area_km2`, `volume_km3`, `circumference_km`). Optional measured extras: `radius_polar_earth`, `flattening`, `moment_of_inertia_factor`.

**Orbit:** `semimajor_au` (about a star) or `semimajor_km` (about a host planet), `eccentricity`, `inclination_deg`, `period_days`, `periastron_au`/`apoastron_au` (or `_km`), `hill_radius_km`, `orbital_speed_kms`. Moons also carry `host` (link).

**Rotation:** `rotation_period_hours`, `obliquity_deg`, `tidally_locked` (true/false).

**Climate and atmosphere:** `flux_earth` (F⊕ at the semimajor axis), `albedo_bond`, `temperature_eq_k` (gray equilibrium), `temperature_mean_k` (adopted mean surface), with `_min`/`_max` for stated ranges, `pressure_surface_bar` (with `_min`/`_max`), `scale_height_km`. Atmosphere composition stays in the body table.

**Counts and identity:** `moons_count`, `star` (link, or list for circumbinary), `named_after`, `adjectives` (list), `discoverer`, `discovery_method`, `discovery_site`, `discovery_year`.

## Biospheres (`type: biosphere`)

`planet` (link), `solvent` (text), `backbone` (text: base-element chemistry), `primary_metabolism` (text), `redox_couples` (list), `membrane_chemistry` (text), `photosynthesis_band_nm` (text range allowed here), `biosphere_age_gyr`, `seeding_origin` (text), `dominant_lifeforms` (list of links or text), `ecosystems` (list), `intelligent_species` (list of links), `civilization_level` (text), `surface_coverage` (text).

## Species and civilizations

To be surveyed after the physical pages: expected fields are `homeworld` (link), `body_plan`, `energy_source`, `lifespan_years`, `population`.

## Open points for the review report

- `Single temperature` rows are ambiguous (equilibrium or mean surface); each page is assigned from its own text and listed for confirmation.
- Combined rows ("gravity / escape speed", "surface area / volume", "mass / radius") are split into their fields.
- Multi-body pages (a hub describing several worlds) keep their per-world numbers in the body and are listed, not guessed.
- Whether the body tables stay as written or later become an embedded view of the frontmatter (one source of truth) is a separate decision.
