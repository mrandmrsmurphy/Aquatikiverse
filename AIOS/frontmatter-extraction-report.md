# Frontmatter extraction report (dry run)

Private review report from `AIOS/scripts/2026-11-14_frontmatter_extract.py`. **No page has been changed.** The proposed frontmatter for every page is in `AIOS/scripts/2026-11-14_frontmatter_extract.json`.

- Content pages scanned: **152**; pages with at least one extracted property: **146**.
- Class guesses: planet 76, star 20, biosphere 19, system 17, species 6, moon 4, encyclopedia 4, black-hole 2, mineral 1, hub 1, civilization 1, none 1.
- Pages with unparsed or unmapped table rows: **142** (**527** rows).
- Pages where a computed bulk value disagrees with the page's own table: **1** (**1** values).
- Multi-column property tables not extracted (multi-body pages): **7**.

## Mismatches between the page's table and the value computed from its mass and radius

Tolerances: 4% for density, gravity, escape speed and area; 6% volume; 2% circumference. The frontmatter would carry the computed value.

| Page | Field | Page says | Computed | Difference |
| --- | --- | --- | --- | --- |
| Nimvion System/Rheomede | gravity_ms2 | 5.1 | 5.56251 | 9.1% |

## Additional property tables skipped (only the first full table per page is used)

- Altmania System/Nasia: 2 more table(s), first columns: Property, Value
- Altmania System/Thionis: 2 more table(s), first columns: Property, Value, Notes
- Gammal System/Dold-Pärla: 1 more table(s), first columns: Property, Adopted working value
- Nimvion System/Aurion and Argyra: 2 more table(s), first columns: Property, Value
- Nimvion System/Rheomede: 1 more table(s), first columns: Property, Value
- Thrírlitir System/Thrírlitir: 2 more table(s), first columns: Property, Value
- Tom and Jerry and Nibbles/Tom (black hole): 1 more table(s), first columns: Property, Working value or interpretation
- Ɬiʔa System/Middle Path: 1 more table(s), first columns: Property, Adopted value
- Ɬiʔa System/Two-Face: 2 more table(s), first columns: Quantity, Value

## Multi-column tables not extracted

- Aethonix System/Aethonix: columns Property, Aethonix A (Primary), Aethonix B (Secondary)
- Altmania System/Altmania: columns Property, Altmania A, Altmania B
- Boreads System/Calais and Zetes: columns Property, Calais (WD-A), Zetes (WD-B)
- Boreads System/Calais and Zetes: columns Property, Calais, Zetes
- Chiaroscuro System/Chiaroscuro: columns Property, Chiaroscuro A, Chiaroscuro B
- Lytherin System/Lytherin: columns Property, Lytherin A, Lytherin B
- Orpheus and Eurydice System/Orpheus and Eurydice: columns Property, Orpheus, Eurydice

## Labels deliberately ignored (not properties)

notes (18), extrasolarplanet (13), apsis (13), classification (9), epoch (8), discovery ref (8), planets (8), location (6), heliopause (3), star mass (3), star radius (3), star luminosity (3), outermost planet (3), protoplanetary disc (3), kuiper cliff (3), dwarf planets (3), variable (3), frost line (3), pronounced (3), discovery reference (2), coordinates (2), radial velocity (2), interior (2), galactocentric radius (2), observer inclination (2), stellar rv amplitude (2), q factor (2)

## Unmapped labels (count of rows)

apastron (4), astropause (3), a (3), home (3), mass (m☉) (2), radius (r☉) (2), luminosity (l☉) (2), surface temperature (k) (2), absolute magnitude (v) (2), apparent magnitude (v) (2), rotation period (days) (2), estimated main sequence lifetime (2), progenitor label (2), white-dwarf mass (2), present radius, interpolated model (2), present effective temperature (2), present luminosity (2), cooling age at biological zero (2), effective temperature at biological zero (2), spectral atmosphere (2), magnetic activity (2), spherical reference area (2), discovery (2), magnetic field (2), origin (2), present state (2), present reference age (2), approximate main-sequence lifetimes (2), outermost semi-major axis (2), metazoan (2), morphology (2), sapience (2), locomotion (2), communication (2), variability (2), comets (2), mean solar day (2), estimated stellar lifespan (2), habitable zone (2), spin period (2), residual magnetic field (2), tidal response (2), water inventory (2), pronunciation (2), reference temperature (2), dayside (2), rings (2), area (2), gray equilibrium (2), nearest physical stellar neighbor (2), secondary (1), total mass/luminosity (1), relative binary orbit (1), metallicity/current age (1), approximate main-sequence lifetime scale (1), classical hz reference (1), observed outer structured debris (1), gravitational/hill scale (1), disk frost-line reference (1), planets/dwarfs (1), satellites/minor bodies (1), mutual orbital period (1), category (1), formula (1), molweight (1), symmetry (1), color (1), habit (1), fracture (1), luster (1), streak (1), diaphaneity (1), mohs (1), opticalprop (1), fluorescence (1), other (1), surface water (1), spectral types (1), confirmed planets (1), a mass (1)

## Rows that could not be parsed, by page

**Aethonix System/Aethonix System**
- `Secondary` = `0.7 M☉, 0.70 R☉, 4600 K, ~0.198 L☉, K4V` — unmapped label
- `Total mass/luminosity` = `1.8 M☉ /1.7 L☉` — unmapped label
- `Relative binary orbit` = `0.15 AU, e=0.01, period15.816days` — unmapped label
- `Metallicity/current age` = `[Fe/H]=+0.15; ~4 Gyr` — unmapped label
- `Approximate main-sequence lifetime scale` = `~7.5–8 Gyr, model-dependent` — unmapped label
- `Classical HZ reference` = `~1.24–2.18 AU; spectrum/climate-model dependent, not a sharp habitatio` — unmapped label
- `Observed outer structured debris` = `~15–30 AU; no confirmed trans-belt cloud` — unmapped label
- `Gravitational/Hill scale` = `~1.5light-years illustrative; depends on Galactic environment, not hel` — unmapped label
- `Disk frost-line reference` = `~3.5 AU historical formation scale; not a present rigid boundary` — unmapped label
- `Planets/dwarfs` = `Eight planets; at least Korelva, Vastur, Eyaquon` — unmapped label
- `Satellites/minor bodies` = `Hundreds of catalogued satellites, thousands of minor bodies, cometary` — unmapped label

**Aethonix System/Aethonix**
- `Mutual orbital period` = `15.8 days` — unmapped label
- `Inclination` = `Coplanar with planetary plane` — no unit match

**Aethonix System/Aska**
- `inclination` = `Coplanar with stellar binary` — no unit match
- `temperature` = `1200–1300 °C` — NOTE: from Celsius

**Aethonix System/Cryodon**

**Aethonix System/Glaciumite**
- `category` = `Rare-earth isotope silicate` — unmapped label
- `formula` = `Y₃(NdF₆)·Si₃O₉` — unmapped label
- `molweight` = `~753.20 g/mol (nominal ideal formula; isotope/site substitutions modif` — unmapped label
- `symmetry` = `P1̅` — unmapped label
- `color` = `Violet-blue (electroluminescent)` — unmapped label
- `habit` = `Prismatic veins, granular crusts` — unmapped label
- `fracture` = `Subconchoidal` — unmapped label
- `luster` = `Submetallic to vitreous` — unmapped label
- `streak` = `Pale blue` — unmapped label
- `diaphaneity` = `Translucent to opaque` — unmapped label
- `mohs` = `6.5–7.2` — unmapped label
- `opticalprop` = `Anisotropic` — unmapped label
- `fluorescence` = `UV-excited fluorescence; separate field-driven emission` — unmapped label
- `other` = `Electromagnetically responsive; Nd-isotope/site-ordering signature` — unmapped label

**Aethonix System/Goku**
- `surface water` = `~84%` — unmapped label

**Aethonix System/Life on Goku**

**Aethonix System/Life on Lunara**

**Aethonix System/Lunara**

**Aethonix System/Noctilux**

**Aethonix System/Rimeas**
- `single temperature` = `~5 °C (mean surface)` — NOTE: from Celsius

**Aethonix System/Thalor**

**Aethonix System/Tsurai**

**Aethonix System/Velora**

**Altmania System/Altmania System**
- `Spectral types` = `A: K6V; B: K4V` — unmapped label
- `Confirmed planets` = `Six; three around each star` — unmapped label
- `A mass / radius / luminosity [a mass]` = `0.60 M☉` — unmapped label
- `B mass / radius / luminosity [b mass]` = `0.70 M☉` — unmapped label
- `Binary periastron / apastron [binary periastron]` = `14.4` — unmapped label
- `Binary periastron / apastron [apastron]` = `15.6 AU` — unmapped label

**Altmania System/Altmania**
- `Apastron` = `~15.6 AU` — unmapped label
- `Mass (M☉) (a)` = `0.60` — unmapped label
- `Radius (R☉) (a)` = `0.62` — unmapped label
- `Luminosity (L☉) (a)` = `0.10` — unmapped label
- `Surface Temperature (K) (a)` = `4120` — unmapped label
- `Absolute Magnitude (V) (a)` = `Requires a spectral bolometric correction` — unmapped label
- `Apparent Magnitude (V) (a)` = `Mᵥ + 3.406 at 48 pc, before extinction` — unmapped label
- `Distance (pc) (a)` = `48` — no unit match
- `Rotation Period (days) (a)` = `30–40` — unmapped label
- `Estimated Main Sequence Lifetime (a)` = `30–40 Gyr` — unmapped label
- `Mass (M☉) (b)` = `0.70` — unmapped label
- `Radius (R☉) (b)` = `0.74` — unmapped label
- `Luminosity (L☉) (b)` = `0.20` — unmapped label
- `Surface Temperature (K) (b)` = `4490` — unmapped label
- … and 5 more

**Altmania System/Azotia**

**Altmania System/Dunamas**
- `Satellites` = `Two moons (0.8 and 0.3 lunar masses)` — NOTE: count from words; check

**Altmania System/Iodulon**
- `Eccentricity` = `Approximately zero` — no number
- `Rotation` = `Synchronous / tidally locked; supplied under inclination` — no unit match
- `Orbital inclination` = `Not specified` — no unit match
- `Terminator temperature` = `230–240 K in exposed living belt; warmer habitats pressurized; 270–330` — unmapped label
- `Albedo` = `Unknown` — no number
- `Terminator atmospheric pressure` = `Approximately 1.2 atm` — unmapped label

**Altmania System/Life on Azotia**

**Altmania System/Life on Iodulon**

**Altmania System/Life on Neonova**

**Altmania System/Life on Thionis**

**Altmania System/Nasia**
- `Discovery year` = `2094` — unmapped label
- `Moons` = `Natia, Stephanie, Kathy` — moon count is descriptive

**Altmania System/Neonova**
- `Orbital inclination` = `Not specified; source field says “tidally locked,” a spin state` — no unit match

**Altmania System/Thionis**

**BD−08°2823 System/BD−08°2823 System**
- `Stellar mass` = `0.74 M☉` — unmapped label
- `Stellar radius` = `Approximately 0.70 R☉` — unmapped label
- `Reference luminosity` = `0.225 L☉ adopted model value; 0.237 L☉ reported catalog value; 0.20–0.` — unmapped label
- `Stellar rotation` = `Approximately 26–27 days` — unmapped label
- `Planets in the setting` = `Seven: b, Oxhydra, c, Prithvi, Ṭanḍī, Varuna, Juṛvā` — unmapped label
- `Real discovery context` = `b and c detected by radial velocity; setting c orbit deliberately refi` — unmapped label
- `Named natural satellites` = `Nine; additional unnamed minor moons and irregulars exist` — unmapped label
- `Outermost listed major orbit` = `Juṛvā, 18 AU; no outer minor-body boundary specified` — unmapped label
- `Historical nearest-neighbor fields` = `LHS 292 and HD 92788 were listed in the supplied source; their nearest` — unmapped label

**BD−08°2823 System/BD−08°2823 b**
- `Discovery-fit time of periastron (BJD)` = `2,454,637.7 ± 1.6` — unmapped label
- `Discovery-fit argument of periastron (degrees)` = `30 ± 100` — unmapped label
- `RV semi-amplitude (m/s)` = `6.5 ± 1.0` — unmapped label

**BD−08°2823 System/BD−08°2823 c**

**BD−08°2823 System/BD−08°2823**
- `Visual magnitude` = `V = 9.86` — unmapped label
- `Parallax` = `24.1641 ±0.0397 mas` — unmapped label
- `Proper motion in RA` = `−375.517 ±0.066 mas/year` — unmapped label
- `Proper motion in declination` = `+25.460 ±0.060 mas/year` — unmapped label
- `Metallicity [Fe/H]` = `−0.04 ±0.06 dex` — unmapped label
- `Projected rotation speed` = `1.4 km/s` — unmapped label

**BD−08°2823 System/Juṛvā**

**BD−08°2823 System/Life on Oxhydra**

**BD−08°2823 System/Oxhydra**
- `Inclination` = `Unknown` — no unit match

**BD−08°2823 System/Prithvi**
- `Discovery context` = `Fictional follow-up exploration of the HARPS b/c system; discoverer un` — unmapped label
- `Discovery and settlement` = `In-setting exploration; colonized through the Mohan Initiative` — unmapped label
- `Land water ratio` = `65% land / 35% water` — unmapped label
- `Albedo` = `Moderate; seasonally variable` — no number

**BD−08°2823 System/Pumper Beetles**
- `Home planet` = `[[Oxhydra]]` — unmapped label
- `Clade` = `Continuant Peroxidovores` — unmapped label
- `First appearance` = `Siloxyl Revolution (post–Aqueous Meteor Sequence)` — unmapped label
- `Environment` = `Subsurface siloxyl soils; brine fractures; oxidant fronts` — unmapped label
- `Average length` = `12–60 mm` — unmapped label
- `Metabolic basis` = `Hydrogen peroxide respiration; methane oxidation` — unmapped label
- `Primary senses` = `Chemoreception; gradient mapping; plasmonic field detection` — unmapped label
- `Social structure` = `Kin clusters; cooperative tunneling groups` — unmapped label

**BD−08°2823 System/Varuna**

**BD−08°2823 System/Ṭanḍī**

**Boreads System/Boreads System**
- `Combined mass` = `1.20 M☉` — unmapped label
- `Present binary relative semimajor axis` = `0.006 AU` — unmapped label
- `Present binary period` = `~3.72 hours` — unmapped label
- `Working binary eccentricity and planetary plane` = `Circular, approximately coplanar screening reference; physical history` — unmapped label
- `Planetary axis and Kepler year` = `0.030 AU; ~41.58 hours` — unmapped label
- `Mean spin` = `Near-synchronous 1:1 working model; does not freeze both stellar posit` — unmapped label
- `Biological age` = `~3.5 Gyr since panspermia into wet habitats` — unmapped label
- `Current epoch` = `Diaspora; retreating natural biosphere, sanctuary/refugia persist` — unmapped label
- `Reference time since last common envelope` = `~4.3 Gyr` — unmapped label
- `Current reference component cooling ages` = `Calais ~5.3 Gyr; Zetes ~4.3 Gyr` — unmapped label
- `Present illustrative component temperatures` = `~5,314 K; ~5,137 K` — unmapped label
- `Present illustrative combined luminosity` = `~2.07×10⁻⁴ L☉` — unmapped label
- `Present barycentric point-source flux` = `~312 W/m² / 0.23 S⊕` — unmapped label
- `Total stellar-system age` = `Includes progenitor evolution; not yet fixed by a binary-evolution mod` — unmapped label
- … and 1 more

**Boreads System/Calais and Zetes**
- `Binary relative semimajor axis` = `0.006 AU` — unmapped label
- `Planetary orbit` = `0.030 AU; ~41.58 hours Kepler reference` — unmapped label
- `Coplanarity` = `Approximately coplanar working model` — unmapped label
- `Combined present luminosity` = `~2.07×10⁻⁴ L☉` — unmapped label
- `Present barycentric flux at Chronmismer` = `~312 W/m² / 0.23 Earth flux before phase variation` — unmapped label
- `Current component reference cooling ages` = `Calais ~5.3 Gyr; Zetes ~4.3 Gyr` — unmapped label
- `Total system age` = `Older than the white-dwarf cooling ages; initial stellar evolution not` — unmapped label
- `Progenitor label (calais)` = `Approximately 2.0 M☉ A-type star; pre-transfer reference` — unmapped label
- `White-dwarf mass (calais)` = `0.65 M☉` — unmapped label
- `Present radius, interpolated model (calais)` = `~0.01179 R☉` — unmapped label
- `Present effective temperature (calais)` = `~5,314 K` — unmapped label
- `Present luminosity (calais)` = `~9.99×10⁻⁵ L☉` — unmapped label
- `Cooling age at biological zero (calais)` = `~1.8 Gyr` — unmapped label
- `Effective temperature at biological zero (calais)` = `~7,022 K` — unmapped label
- … and 11 more

**Boreads System/Chronmismer**
- `Kepler orbital period` = `~41.58 hours` — unmapped label
- `Spin` = `Near-synchronous mean 1:1 reference` — no unit match
- `Obliquity` = `Low working reference` — no unit match
- `Near-side geography` = `Substellar scar, formerly humid plains and estuaries` — unmapped label
- `Nightside` = `Cold provinces, aquifers, geothermal and subglacial refugia` — unmapped label
- `Biosphere age/current state` = `~3.5 Gyr / retreating and surviving in refugia` — unmapped label

**Boreads System/Life on Chronmismer**

**Chiaroscuro System/Chiaroscuro System**
- `Outermost listed orbit` = `26 AU` — unmapped label
- `Major companions` = `Six planets and the brown dwarf [[Umbryl]], described below` — unmapped label
- `Stellar spectra and luminosities` = `F1V (≈5.5 L☉), K1V (≈0.4 L☉)` — unmapped label

**Chiaroscuro System/Chiaroscuro**

**Chiaroscuro System/Eirda**
- `Inclination` = `Nearly coplanar reference orbit. Exact eclipse geometry remains to be ` — no unit match

**Chiaroscuro System/Ereba**

**Chiaroscuro System/Euryphessa**
- `Reference radius` = `1.2 R_J (≈85,800 km using Jupiter’s equatorial reference radius)` — unmapped label
- `Albedo` = `Visible geometric ≈0.9. Working Bond ≈0.66, with a non-Lambertian phas` — NOTE: Bond value taken

**Chiaroscuro System/Kharon**
- `Inclination` = `Approximately coplanar with the low-inclination planetary reference mo` — no unit match
- `Albedo` = `Working Bond albedo ≈0.001 and visible geometric albedo of the same or` — NOTE: Bond value taken

**Chiaroscuro System/Phothinos**
- `Eccentricity` = `Near-circular reference orbit, with binary-forced variations` — no number
- `Density` = `6270 kg/m^3` — no unit match
- `Surface gravity` = `14.54 m/s^2` — no unit match
- `Albedo` = `Working Bond albedo ≈0.80, visible geometric albedo ≈0.85` — NOTE: Bond value taken

**Chiaroscuro System/Skotos**
- `Albedo` = `Visible geometric ≈0.02. Working Bond ≈0.03.` — NOTE: Bond value taken

**Chiaroscuro System/Umbryl**
- `Inclination` = `Near the planetary reference plane` — no unit match

**Gammal System/Dold-Pärla**
- `Mean surface temperature` = `Reference near **288 K**, with described long-term states about **288–` — NOTE: from Celsius
- `Native biosphere age` = `Approximately **4 Gyr**; separate from the 9.5-Gyr star and human chro` — unmapped label
- `Local recognition` = `Antiquity, by direct local observation` — unmapped label
- `Earth/instrument recognition` = `Fictional circa-2439-CE system discovery context, not the date of loca` — unmapped label

**Gammal System/Gammal System**
- `Stellar age / mass [stellar age]` = `9.5 Gyr` — unmapped label
- `Sky position` = `J2000 **17h46m00s, −29°05′00″**, Sagittarius` — unmapped label
- `Major inhabited satellite` = `**Dold-Pärla**, 480,000 km from Storebror` — unmapped label
- `Satellite census` = `Eleven Storebror moons; six named, five incompletely specified` — unmapped label
- `Galactic orbit inclination` = `Source ≈2° reference to Galactic plane; orbit not reconstructed` — unmapped label
- `Circumstellar periods` = `Gycklare **41.6 d**; Storebror **174.3 d**` — unmapped label
- `Planetary orbital speeds` = `About **57.5 / 35.7 km/s**, respectively` — unmapped label
- `Native biological history` = `**About 4 Gyr** on Dold-Pärla` — unmapped label
- `Human history` = `Abrupt arrival about **100,000 years before the Archive reference**; l` — unmapped label
- `Disk / formation snow line [disk]` = `Protoplanetary disk dissipated` — unmapped label
- `Disk / formation snow line [formation snow line]` = `inherited snow-line reference ≈2.3 AU at unspecified epoch` — unmapped label
- `Astropause` = `Inherited ≈55-AU estimate, wind/environment dependent` — unmapped label
- `Minor bodies` = `Ring/shepherd debris and possible resonant bodies; full census unmodel` — unmapped label

**Gammal System/Gammal**
- `Activity` = `Low; not an intrinsically large-amplitude variable` — unmapped label
- `Line-of-sight extinction` = `Illustrative Av≈1.5–3.0 mag` — unmapped label
- `Astropause` = `Source estimate about 55 AU, conditional on wind/interstellar pressure` — unmapped label
- `Formation-disk snow line` = `Source reference about 2.3 AU at an unspecified disk epoch` — unmapped label

**Gammal System/Gycklare**
- `Spherical reference area / volume [spherical reference area]` = `2.94×10⁹ km²` — unmapped label
- `Gravity at reference radius` = `**10.74 m/s²**` — unmapped label
- `Periastron / apastron [periastron]` = `About 0.2189` — apsis not parsed
- `Periastron / apastron [apastron]` = `0.2211 AU` — unmapped label
- `Rotation` = `Assumed approximately synchronous; tidal evolution not reconstructed` — no unit match
- `Full-redistribution equilibrium temperature` = `About **414 K**` — unmapped label
- `Discovery` = `Automated remote photometric array, circa **2439 CE**, transit/RV in t` — unmapped label

**Gammal System/Storebror**
- `Spherical reference area / volume [spherical reference area]` = `7.77×10¹⁰ km²` — unmapped label
- `Periastron / apastron [periastron]` = `About 0.5691` — apsis not parsed
- `Periastron / apastron [apastron]` = `0.5749 AU` — unmapped label
- `Earth observer inclination` = `**89.8°**, distinct from spin obliquity and satellite inclinations` — unmapped label
- `Spin obliquity` = `**5°** to the circumstellar orbital normal; working eclipse-geometry c` — unmapped label
- `Quadrupole` = `Illustrative **J₂≈0.008**, requiring an interior model` — unmapped label
- `Globe Bond / geometric albedo [globe bond]` = `0.35` — unmapped label
- `Stellar input` = `About **1414 W/m²**, normal incidence` — unmapped label
- `Discovery` = `Remote photometric array, circa **2439 CE**, transit and radial veloci` — unmapped label

**Ghulheim–Ferruva system/Ferruva**
- `Axis about Ghulheim` = `**0.05 AU**, measured center to center` — unmapped label
- `Period and synchronous rotation` = `About **16.96 Earth days**` — unmapped label
- `Obliquity` = `Small, approximately zero in the working reference` — no unit match
- `Temperature` = `Cold exposed exterior; warmer insulated brine compartments` — no unit match
- `Discovery metadata` = `Fictional setting object; no real discovery claimed` — unmapped label

**Ghulheim–Ferruva system/Ghulheim and Ferruva**
- `Formal designation` = `GXN-1` — unmapped label
- `Components` = `Ghulheim, brown dwarf; Ferruva, rocky life-bearing satellite` — unmapped label
- `Stellar context` = `No current local hydrogen-burning host; formerly part of a K-star syst` — unmapped label
- `Earth-sky constellation` = `**Sagittarius**, near the Galactic Center` — unmapped label
- `Earth-sky direction` = `Near J2000 17h45m40s, −29°00′28″; Sgr A* reference direction, not an e` — unmapped label
- `Galactic location` = `Nuclear Star Cluster, about **0.05 pc / 10,300 AU** from Sgr A* in the` — unmapped label
- `Outer orbit` = `**0.05 pc** semimajor axis; eccentricity **0.05** adopted for an illus` — unmapped label
- `Outer pericenter / apocenter [outer pericenter]` = `About 0.0475` — unmapped label
- `Outer pericenter / apocenter [apocenter]` = `0.0525 pc in that layout` — unmapped label
- `Outer Kepler period` = `About **505 Earth years** around a rounded 4.3 ×10⁶-M☉ point mass` — unmapped label
- `Body age` = `About **7 Gyr**` — unmapped label
- `Present nuclear-orbit residence` = `Unspecified; not equated to either age` — unmapped label
- `Primary reference` = `**0.058 M☉**, about **0.79 R♃**, **1050 K**, **7.2 ×10⁻⁶ L☉**` — unmapped label
- `Satellite reference` = `**0.8 M⊕**, **0.95 R⊕**, axis **0.05 AU**, period **16.96 days**` — unmapped label

**Ghulheim–Ferruva system/Ghulheim**
- `Magnetic field` = `Kilogauss scale; setting assumption, not a measured value` — unmapped label
- `Spectral description` = `Peculiar, cool, high-gravity brown dwarf; precise subtype unspecified` — unmapped label
- `Satellites` = `One major companion, Ferruva; formerly additional minor moons` — NOTE: count from words; check
- `Ferruva’s axis and period` = `0.05 AU; about **16.96 days**` — unmapped label
- `Orbit about Sagittarius A*` = `About 0.05 pc; about 505 years in a point-mass reference` — unmapped label

**Ghulheim–Ferruva system/Life on Ferruva**
- `Origin` = `Abiogenesis during a K-star-illuminated ocean epoch; later transition ` — unmapped label
- `Main energy capture` = `Hydrothermal redox chemistry and radiolytic chemical products; supplem` — unmapped label
- `Element chemistry` = `Carbon-based; speculative halogenated biochemistry and tightly contain` — unmapped label
- `Redox systems` = `Fe(III)/Fe(II), Mn(IV)/Mn(II), sulfate/sulfide and thiosulfate transfo` — unmapped label
- `Membranes` = `Halogenated lipid analogs with selective ion transport; energetic coup` — unmapped label
- `Light capture` = `Ancestral visible-light photosynthesis; residual near-IR photochemistr` — unmapped label
- `External atmosphere` = `No substantial atmosphere; possible transient exosphere` — unmapped label
- `Internal gases` = `O₂, CH₄, SO₂ and NH₃ in compatible dissolved or compartmentalized chem` — unmapped label
- `Coverage` = `Regional connected brine basins, fractures and basal pores beneath a c` — unmapped label
- `Main life` = `Radiotrophic/radiation-responsive mats, biofoam colonies, PFC-carrying` — unmapped label
- `Domains` = `Lid, Zone, Ground` — unmapped label
- `Intelligence / civilization` = `None` — combined row: label/value counts differ
- `Present state` = `Persistent but energy-limited setting ecology; productivity and longev` — unmapped label

**Lytherin System/Frey**

**Lytherin System/Freya**

**Lytherin System/Jaspis**

**Lytherin System/Jötunn**

**Lytherin System/Life on Jaspis**

**Lytherin System/Lytherin System**
- `A / B masses [a]` = `1.70` — unmapped label
- `A / B masses [b masses]` = `1.60 M☉` — unmapped label
- `A / B radii [a]` = `1.70` — unmapped label
- `A / B radii [b radii]` = `1.60 R☉` — unmapped label
- `A / B luminosities` = `6.0 / 5.0 L☉; total 11 L☉` — combined row: label/value counts differ
- `A / B temperatures [a]` = `~6930` — unmapped label
- `A / B temperatures [b temperatures]` = `~6820 K, early-F dwarfs` — unmapped label
- `Present reference age` = `~1 Gyr; not the full stellar lifetime` — unmapped label
- `Approximate main-sequence lifetimes` = `~2.5–3.5 Gyr, model-dependent` — unmapped label
- `Binary relative orbit` = `0.100 AU, eccentricity 0.001, period 6.358 days` — unmapped label

**Lytherin System/Lytherin**
- `Binary separation` = `0.1 AU` — unmapped label
- `Approximate main-sequence lifetimes` = `~2.5–3.5 billion years; model-dependent` — unmapped label
- `Present reference age` = `~1 billion years` — unmapped label

**Lytherin System/Pele**
- `Surface thermal regime` = `Engineered ~3000 K reference; local magma/fountain temperatures ~2800–` — unmapped label
- `Natural irradiation-only equilibrium` = `~781 K globally; ~1104 K substellar comparison` — unmapped label

**Lytherin System/Zucchero**
- `Optical/haze radius` = `43,323 km (~6.8 R⊕)` — unmapped label
- `Nominal 1-bar radius` = `~36,952 km (5.8 R⊕); structural reference, not independently fitted` — unmapped label
- `Density convention` = `Apparent ~0.056 g/cm³ at optical radius; ~0.0904 g/cm³ using nominal 1` — unmapped label

**Methuselan System/Life on Magnum**

**Methuselan System/Magnum**
- `Inclination` = `Near-equatorial (regular satellite)` — no unit match

**Methuselan System/Melchior**
- `Intrinsic heat` = `negligible (~12 K intrinsic temperature, ~0.001 W/m²)` — unmapped label

**Methuselan System/Methuselah**
- `Catalog coordinate reference` = `J2000 (historical)` — unmapped label
- `Catalog distance from Sol` = `100 pc (approximately 326 ly)` — unmapped label

**Methuselan System/Methuselan System**
- `Outermost semi-major axis` = `0.25 AU` — unmapped label
- `Round satellites` = `4 (Clavelin, Magnum, Jéréboam, Piccolo)` — unmapped label
- `Galactic orbital speed` = `~210 km/s` — unmapped label
- `Galactic orbital period` = `~230 million years` — unmapped label
- `Spectral evolution` = `M6V → K7V-like (late-stage *blue dwarf*)` — unmapped label

**Nimvion System/Aurion and Argyra**
- `Libration amplitude (angular separation)` = `≈60° ± 30°` — unmapped label

**Nimvion System/Francesca**
- `Albedo` = `High due to fog and haze` — no number

**Nimvion System/Life on Stygium**

**Nimvion System/Morphfiends**
- `Alternate name(s)` = `Morphfiends (informal exonym)` — unmapped label
- `Home` = `[[Stygium]]` — unmapped label
- `Metazoan` = `Arsenic-based multicellular analog` — unmapped label
- `Morphology` = `Variable, polyplastic, field-guided` — unmapped label
- `Sapience` = `Yes` — unmapped label
- `Development` = `Functional castes, influenced by environment and learning` — unmapped label
- `Reproduction` = `Asexual budding or fission, with occasional physical fusion and geneti` — unmapped label
- `Locomotion` = `Terrestrial crawling, buoyant floating, and aerodynamic gliding with f` — unmapped label
- `Communication` = `Electromagnetic template transmission` — unmapped label

**Nimvion System/Nimvion 3421**
- `Variability` = `None known` — unmapped label
- `Photospheric temperature` = `~5400 K` — unmapped label
- `Surface gravity` = `log g ≈4.39 (cgs, from the stated mass and radius)` — no unit match

**Nimvion System/Nimvion System**
- `Protoplanetarydisc` = `≈25 AU (estimated)` — unmapped label
- `Dwarfplanets` = `1 (Cryosthene)` — unmapped label
- `Minorplanets` = `Inner and outer belt populations` — unmapped label
- `Comets` = `Periodic from Mirrorband reservoir` — unmapped label
- `Spectral` = `G9/K0 V` — unmapped label
- `Frostline` = `≈2.1 AU` — unmapped label

**Nimvion System/Nivalis**

**Nimvion System/Rheomede**
- `Satellites` = `Inner ring-shepherd moonlets (unnamed)` — moon count is descriptive
- `Albedo` = `Bond ≈0.28; geometric ≈0.17` — NOTE: Bond value taken

**Nimvion System/Stygium**
- `Tidal quality factor` = `85` — unmapped label

**Orpheus and Eurydice System/Alchemis**
- `Tidal Q factor` = `80` — unmapped label
- `Mean solar day` = `~265.5 hours (~11.06 Earth days)` — unmapped label
- `Surface temperatures` = `~321 K (day), ~214 K (night)` — unmapped label

**Orpheus and Eurydice System/Dysmorph**
- `Hill radius` = `Not specified` — hill_radius_km: no unit match
- `Roche limit` = `Not specified` — no unit match
- `Sidereal day` = `Not specified` — no unit match
- `Axial tilt` = `Not specified` — no unit match
- `Rot velocity` = `Not specified` — no unit match
- `Moment of inertia factor` = `Not specified` — no number

**Orpheus and Eurydice System/Formoquens**
- `Home` = `[[Alchemis]]` — unmapped label
- `Metazoan` = `None (inorganic automaton)` — unmapped label
- `Morphology` = `Modular crystalline forms (quadrupeds common)` — unmapped label
- `Sapience` = `Yes` — unmapped label
- `Gender` = `None` — unmapped label
- `Locomotion` = `Terrestrial (quadrupedal, modular); limited flight (specialized forms)` — unmapped label
- `Communication` = `Structured photonic emission; local electromagnetic field modulation` — unmapped label

**Orpheus and Eurydice System/Laputa**

**Orpheus and Eurydice System/Life on Alchemis**

**Orpheus and Eurydice System/Life on Dysmorph**

**Orpheus and Eurydice System/Life on Laputa**

**Orpheus and Eurydice System/Orpheus and Eurydice System**
- `Age` = `Old; several Gyr (proposed post-supernova fallback system)` — no unit match
- `Listed semi-major axis` = `1.6 AU` — unmapped label
- `Primary spectral type` = `K0V` — unmapped label
- `Variability` = `None known` — unmapped label

**Orpheus and Eurydice System/Orpheus and Eurydice**
- `Companion distance` = `~20–40 AU from Orpheus` — unmapped label
- `Estimated stellar lifespan (orpheus)` = `~25 Gyr` — unmapped label
- `Habitable zone (orpheus)` = `~0.62–1.07 AU` — unmapped label
- `Spin period (orpheus)` = `Not specified` — unmapped label
- `Residual magnetic field (orpheus)` = `Not specified` — unmapped label
- `Luminosity (eurydice)` = `Not specified` — no unit match
- `Effective temperature (eurydice)` = `Not specified` — no unit match
- `Estimated stellar lifespan (eurydice)` = `Not specified` — unmapped label
- `Habitable zone (eurydice)` = `Not specified` — unmapped label
- `Spin period (eurydice)` = `>20 ms` — unmapped label
- `Residual magnetic field (eurydice)` = `~10⁸ G` — unmapped label

**Skemer/Life on Skemer**
- `Biosphere age` = `Several hundred million years (native life); ~150 years (posthuman int` — no unit match

**Skemer/Skemer-mense**
- `Home / place of differentiation [home]` = `[[Skemer]]` — unmapped label
- `Home / place of differentiation [place of differentiation]` = `Earth-human ancestry` — unmapped label
- `Intelligent` = `Yes` — unmapped label
- `Spacefaring` = `Limited; heritage technology only` — unmapped label
- `Kingdom` = `Animalia` — unmapped label
- `Phylum` = `Chordata` — unmapped label
- `Class` = `Mammalia` — unmapped label
- `Order` = `Primates` — unmapped label
- `Family` = `Hominidae` — unmapped label
- `Genus` = `Homo` — unmapped label
- `Species` = `H. skemerensis / Homo skemerensis` — unmapped label
- `Adult stature` = `Typically 1.1–1.3 m` — unmapped label
- `Engineering interval` = `Six generations / approximately 150 years` — unmapped label
- `Reproductive isolation` = `Dated to the fourth post-arrival generation` — unmapped label
- … and 1 more

**Skemer/Skemer**
- `Satellites` = `One, Maan` — NOTE: count from words; check
- `Tidal response` = `Illustrative constant time lag 100 s, k₂=0.3; frequency-dependent Q` — unmapped label
- `Stellar flux` = `Zero direct host-star illumination` — no unit match
- `Sky location` = `Hydra, assuming J2000 coordinates RA 10h04m, Dec −24°30′` — unmapped label
- `Total heat flux` = `Approximately 0.312 W/m² present reference; concentrated locally in ac` — unmapped label
- `Typical global temperature` = `Approximately 255–265 K; warmer active belts` — unmapped label

**Sol System/Ceres**
- `Obliquity` = `—` — no unit match

**Sol System/Earth**

**Sol System/Eris**
- `Obliquity` = `—` — no unit match

**Sol System/Haumea**
- `Obliquity` = `—` — no unit match

**Sol System/Jupiter**

**Sol System/Makemake**
- `Obliquity` = `—` — no unit match

**Sol System/Mars**

**Sol System/Mercury**

**Sol System/Neptune**

**Sol System/Pluto**

**Sol System/Saturn**

**Sol System/Sun**
- `Volumetric mean radius` = `695,700 km (1 R☉; 109 R⊕)` — unmapped label
- `Photosphere temperature` = `~4,400 K (top) to ~6,600 K (bottom)` — unmapped label
- `Central temperature` = `~1.57×10⁷ K (model value)` — unmapped label
- `Obliquity to the ecliptic` = `7.25°` — unmapped label
- `Composition (photosphere, by number)` = `H 90.97%, He 8.89%; heavier elements ~0.14% (O, C, Ne, N, Fe, Mg, Si, ` — unmapped label

**Sol System/Uranus**

**Sol System/Venus**

**Stellula System/Gigafusc**
- `Surface pressure` = `n/a (no solid surface)` — no unit match

**Stellula System/Harth**
- `Tidal heat flux` = `~0.1–1 W/m² (adopted premise; see Tidal heating)` — unmapped label

**Stellula System/Stellula System**
- `Outermost semi-major axis` = `0.1000 AU (Stellula–Gigafusc relative orbit)` — unmapped label
- `Outermost companion` = `Gigafusc` — unmapped label
- `Satellites` = `around Gigafusc and Virans` — moon count is descriptive
- `Comets` = `None detected` — unmapped label
- `Orbital speeds` = `~87.9 km/s (Tito) to ~28.8 km/s (Gigafusc relative to Stellula)` — unmapped label
- `Orbital periods` = `1.1366–37.80 days` — unmapped label
- `Stellar binary stability screen` = `~0.041 AU around Stellula for circular, coplanar test-particle orbits` — unmapped label

**Stellula System/Stellula**
- `Catalogue name` = `AQV Stellula` — unmapped label
- `Surface gravity` = `log g ≈ 5.3 (cgs), ~8 times solar` — no unit match
- `Metallicity` = `Assumed near solar` — no number
- `Adopted system age` = `~2 billion years` — unmapped label
- `Estimated main-sequence lifetime` = `On the order of 5 trillion years` — unmapped label

**Stellula System/Tito**
- `Water inventory` = `tens of percent of the mass; global ocean ~100–200 km deep over high-p` — unmapped label

**Stellula System/Virans**
- `Gravity at 1 bar` = `8.66 m/s² (0.88 g at 1 bar level)` — unmapped label

**Thrírlitir System/Aialon**
- `Pronunciation` = `/ˈaɪ.ə.lɒn/` — unmapped label

**Thrírlitir System/Aphrod**
- `Oceans` = `~85% surface coverage; ammonia–water with 15–25 wt% NH₃ in the bulk` — unmapped label
- `Rotation` = `Slow, non-synchronous` — no unit match

**Thrírlitir System/Barzél**
- `Reference temperature` = `1,080 K for a uniformly redistributed A = 0 body (988 K at A = 0.3)` — unmapped label
- `Dayside` = `mean ≈ 1,280 K; substellar point ≈ 1,530 K (A = 0)` — unmapped label

**Thrírlitir System/Ceraun**
- `Cloud-top gravity` = `~9.7 m/s²` — unmapped label
- `Axial / magnetic tilt (source field) [axial]` = `Tidally locked` — unmapped label
- `Axial / magnetic tilt (source field) [magnetic tilt (source field)]` = `magnetic tilt ~70°` — unmapped label
- `Rotation` = `Synchronous` — no unit match
- `Global equilibrium temperature` = `~1080 K (Bond albedo 0.1; uniform redistribution)` — unmapped label
- `Reference pressure` = `High, but not well-defined (gas giant)` — unmapped label
- `Albedo` = `Bond albedo ~0.1 (absorptive upper layers)` — NOTE: Bond value taken
- `Roche lobe radius` = `~485,000 km (6.2 planetary radii; the planet fills 16% of it)` — unmapped label
- `Atmospheric escape` = `~8.7×10⁶ kg/s (≈0.046 M⊕/Gyr, 0.03% of the planet's mass per Gyr)` — unmapped label
- `Pronunciation` = `/ˈsɛr.ɔːn/` — unmapped label

**Thrírlitir System/Life on Aphrod**

**Thrírlitir System/Mot**
- `Satellites` = `Mot I plus at least 11 minor moons` — moon count is descriptive
- `Gravity (1-bar level)` = `~10.3 m/s²` — unmapped label
- `Temperature range` = `~24 K (polar-night upper troposphere) to ~95 K (deepest storm-cleared ` — unmapped label

**Thrírlitir System/Pekhám**
- `Reference temperature` = `558 K (flux from C alone), 606 K (C+B), for a uniformly redistributed ` — unmapped label
- `Dayside` = `mean ≈ 720 K; substellar point ≈ 860 K (C+B, A = 0)` — unmapped label

**Thrírlitir System/Thrírlitir System**
- `Stellar types` = `F8 V primary; G8 V + M1 V binary` — unmapped label
- `Outer extent` = `~1.5 ly (comet-cloud and debris extent; the Galactic tidal radius is ~` — unmapped label

**Thrírlitir System/Thrírlitir**
- `Metallicity` = `~solar` — no number

**Thrírlitir System/Valen**
- `Sidereal day / mean solar day [mean solar day]` = `23.09 hours` — unmapped label
- `Ocean fraction` = `~79%` — unmapped label

**Tom and Jerry and Nibbles/Jerry (gas giant)**
- `Orbit period` = `~57.75 days / 1,386 hours (around Tom; Newtonian reference)` — unmapped label
- `Internal luminosity` = `2.2×10¹⁸ W working value; intrinsic effective temperature ~149 K` — unmapped label
- `Satellites` = `Nibbles plus other surviving moons; inherited ≥10-major-moon census is` — moon count is descriptive

**Tom and Jerry and Nibbles/Life on Nibbles**

**Tom and Jerry and Nibbles/Nibbles (habitable moon)**
- `Rotation` = `Synchronous with Jerry` — no unit match

**Tom and Jerry and Nibbles/Tom (black hole)**
- `Galactocentric location` = `~19,500 ly (6 kpc) from its host galaxy’s center; not an Earth distanc` — unmapped label
- `Listed sky direction` = `Pavo; inherited working coordinates, parent galaxy and Earth distance ` — unmapped label
- `Companions` = `[[Jerry (gas giant)\|Jerry]] (warm super-Jupiter), [[Nibbles (habitabl` — unmapped label

**Tom and Jerry and Nibbles/Tom and Jerry and Nibbles**
- `System age` = `Approximately 10 Gyr; capture epoch unspecified` — unmapped label
- `Parent galaxy / Earth distance [parent galaxy]` = `Unspecified` — unmapped label
- `Parent galaxy / Earth distance [earth distance]` = `the galactocentric distance is not an Earth distance` — no unit match
- `Central mass` = `Tom, ~5×10⁶ M☉` — unmapped label
- `Tom luminosity` = `~2,000 L☉ / 7.66×10²⁹ W, bolometric target` — unmapped label
- `Eddington luminosity ratio` = `~1.2×10⁻⁸` — unmapped label
- `Jerry orbit` = `~50 AU, low-eccentricity working model` — unmapped label
- `Jerry orbital period / speed` = `~57.75 days / 1,386 hours; ~0.0314c, Newtonian reference` — combined row: label/value counts differ
- `Jerry spin` = `~8 hours; not synchronous with Tom` — unmapped label
- `Jerry internal luminosity` = `2.2×10¹⁸ W working value; ~149 K intrinsic effective temperature` — unmapped label
- `Jerry cloud-top field` = `~3,000 μT equatorial reference; topology unmodeled` — unmapped label
- `Nibbles mass / radius [nibbles mass]` = `0.4 M⊕` — unmapped label
- `Nibbles orbit` = `~1,000,000 km from Jerry’s center; prograde, near-equatorial reference` — unmapped label
- `Nibbles orbital and synchronous spin period` = `~44.76 hours` — unmapped label
- … and 3 more

**Trigeminal System/Trigemina**

**Trigeminal System/Trigeminal System**
- `A–C orbit` = `10.2 AU, e = 0.20, 17.2 yr` — unmapped label
- `B orbit` = `220 AU, e = 0.30, ~1,388 yr, inclined ~10°` — unmapped label
- `Close-binary periods` = `A 4.0 d, B 5.0 d, C 4.5 d` — unmapped label
- `Candidate habitable zones` = `A 1.53–2.21 AU, B 1.84–2.66 AU, C 1.47–2.12 AU` — unmapped label

**Ɬiʔa System/Belted King**
- `Area / volume [area]` = `2.040×10¹⁵ m²` — unmapped label
- `Period ratio with Epilepticus` = `Pf/Pe = 3/2 target; resonant libration untested` — unmapped label
- `Satellites` = `Five named-by-number reference moons` — NOTE: count from words; check

**Ɬiʔa System/Corpse**
- `Stellar orbital inclination` = `Approximately 90° to reference plane, provisional; full secular dynami` — unmapped label
- `Area / volume [area]` = `Approximately 1.474×10⁹ km²` — unmapped label
- `Gray global equilibrium` = `Approximately 103 K; not a solved surface mean` — unmapped label
- `Atmosphere / intrinsic magnetism [intrinsic magnetism]` = `no sustained intrinsic dynamo adopted` — unmapped label
- `Satellites` = `g1 and g2; historical gl/gll spellings are aliases` — moon count is descriptive

**Ɬiʔa System/Crying Eye**
- `Orbital period / synchronous rotation` = `Approximately 26.09 Earth days` — combined row: label/value counts differ
- `Ratio with c` = `Target Pd/Pc = 3/2; actual libration remains untested` — unmapped label
- `Eccentricity / inclination [eccentricity]` = `Nearly circular, eccentricity not finally fitted` — no number
- `Reference stellar irradiation` = `Approximately 0.582 Earth flux, or 793 W/m²` — unmapped label
- `Gray global equilibrium / substellar reference` = `Approximately 222 / 315 K; not actual global mean or a solved surface ` — combined row: label/value counts differ
- `Ice coverage` = `Approximately 90% design target; Furnace/open-water fraction requires ` — unmapped label
- `Upper ice lid` = `Approximately 20-km regional reference, not a globally uniform equilib` — unmapped label
- `Deep ecological pressure` = `Principal provinces target ~1–3 GPa, with shallower/deeper specialized` — unmapped label
- `Deep interior` = `Rock-rich interior with high-pressure water/ice overburden; ~100–300 G` — unmapped label
- `Fluid Roche example` = `Approximately 34,600 km from center for a 1000-kg/m³ satellite; densit` — unmapped label

**Ɬiʔa System/Epilepticus**
- `Reference flux` = `0.3392 S⊕` — unmapped label
- `Eccentricity / orbital inclination` = `0.04 / 3° to system reference plane; node unspecified` — combined row: label/value counts differ
- `Bulk rotation` = `Near-synchronous reference, approximately 39.14 days; shell libration/` — unmapped label
- `Gray equilibrium` = `Approximately 169–187 K across that albedo range; actual surface map u` — unmapped label
- `Rings / moons` = `None specified` — combined row: label/value counts differ

**Ɬiʔa System/Life on Crying Eye**
- `Origin` = `Native abiogenesis, approximately 2.7 Gyr ago` — unmapped label
- `Principal deep pressure range` = `Order 1–3 GPa; locally shallower/deeper niches, not a universal fixed ` — unmapped label
- `Fundamental chemistry` = `Independently evolved carbon-bearing organic–mineral/ionic/polymeric c` — unmapped label
- `Solvent and media` = `Pressure-dependent water-rich NH₃/CH₃OH/salt brines, interfacial fluid` — unmapped label
- `Boundaries` = `Sessile mineral/ice/brine interfaces; evolved portable composite bound` — unmapped label
- `Primary energy` = `Genuine geological/biological fission; radiolysis-fed chemistry; geoth` — unmapped label
- `Chemical redox inventories` = `H₂ and locally available oxidants, Fe(II)/Fe(III), U(VI)/U(IV), nitrog` — unmapped label
- `Thorium and lead` = `Important mineral/resource/waste constituents in some provinces, not a` — unmapped label
- `Photosynthesis` = `No photosynthetic primary-production guild is established in this acco` — unmapped label
- `Atmosphere / surface [surface]` = `~90%-glaciated outer surface is a climate design target` — unmapped label
- `Dominant guilds` = `Magnetrobes, Corions, Ammoniaphages, Magnetotrophs, Magnetomycota, Ign` — unmapped label
- `Main biomes` = `Exchange/flux provinces, polar vent basins, Furnace upwellings, high-p` — unmapped label
- `Sapient natives` = `**Carbon Suits**; detailed body plan and cultural account not specifie` — unmapped label
- `Technological descriptor` = `“Cro-Magnon-equivalent” denotes substantial human-comparable cognition` — unmapped label
- … and 1 more

**Ɬiʔa System/Life on Middle Path**
- `Backbone chemistry` = `Dual: silicon-based and carbon-based` — unmapped label
- `Silicon photosynthesis band` = `≈850–1000 nm (near-infrared); silicon-gap photovoltaic limit ≈19%` — unmapped label
- `Main ecosystems` = `Dry eye, eyewall and Hot Zone (silicon); terminator belt and nightside` — unmapped label
- `Current state` = `Stable, spatially constrained co-habitation; the silicon biosphere is ` — unmapped label

**Ɬiʔa System/Middle Path**
- `Core` = `0.294 M⊕ (mass fraction 0.28); radius ≈3,434 km; Fe–Ni with ≈15 wt% li` — unmapped label
- `Hill radius / star–planet L1 [star–planet l1]` = `198,680 km from the center` — unmapped label
- `Bond albedo / absorbed mean flux [absorbed mean flux]` = `≈209 W/m² (the dome keeps 76.7% of the starlight)` — unmapped label
- `Water inventory` = `20% of Earth's (2.8×10²⁰ kg, a 523 m global layer)` — unmapped label
- `Surface heat flow` = `≈0.6–0.75 W/m² (7–8 times Earth's)` — unmapped label
- `Magnetic field` = `Dipole along the star direction, ≈144 μT at the equator (≈288 μT at th` — unmapped label
- `Satellites` = `One artificial dome, the Tethered Moon` — NOTE: count from words; check
- `Biospheres` = `Native silicon (~3 Gyr); transplanted carbon (<10,000 yr)` — unmapped label

**Ɬiʔa System/Mirar's Veil**
- `Identity` = `Fictional star; AQ-MV-01; Mirar's Veil` — unmapped label
- `J2000 reference right ascension` = `17h 23m 00s` — unmapped label
- `J2000 reference declination` = `−21° 00′ 00″` — unmapped label
- `Reference parallax` = `65.36 mas; derived from the nominal distance, not an independent preci` — unmapped label
- `Proper motion` = `Total 0.21 arcsec yr⁻¹; position angle not specified` — unmapped label
- `Present mass` = `0.20 M☉` — unmapped label
- `Present radius` = `0.25 R☉` — unmapped label
- `Rotation` = `Nominal two days; physical latitude/activity variations not independen` — no unit match
- `Equatorial rotation speed` = `Approximately 6.32 km s⁻¹` — no unit match
- `Mean unsigned surface magnetic field` = `Nominal 4 kG` — unmapped label
- `Strong surface magnetic regions` = `Approximately 6–8 kG` — unmapped label
- `Large-scale dipole polar strength` = `Nominal 2 kG, distinct from the unsigned surface average` — unmapped label
- `Magnetic geometry` = `Dominant dipole with multipolar active regions; nominal 20° dipole til` — unmapped label
- `X-ray activity reference` = `Lx/Lbol of order 10⁻³; declared design target, not derived from the su` — unmapped label
- … and 3 more

**Ɬiʔa System/Shield Couple**
- `Stellar barycentric axis / period [stellar barycentric axis]` = `1.5 AU` — unmapped label
- `Stellar eccentricity / inclination [stellar eccentricity]` = `0.02` — unmapped label
- `Stellar eccentricity / inclination [inclination]` = `approximately coplanar with system reference plane` — no unit match
- `Mutual center-to-center separation` = `150,000 km, near-circular reference` — unmapped label
- `Mutual inclination` = `Approximately 90° to the stellar orbital plane` — unmapped label
- `Mutual period / component spins [mutual period]` = `Approximately 2.116 days` — unmapped label
- `Mutual period / component spins [component spins]` = `mutually synchronous reference` — unmapped label
- `Each component mass / radius [each component mass]` = `5 M⊕` — unmapped label
- `Each reference density / gravity / escape speed [each reference density]` = `2.266 g/cm³` — unmapped label
- `Each area / volume [each area]` = `Approximately 2.698×10¹⁵ m²` — unmapped label
- `Albedo references` = `Sapphire 0.3; Rust 0.4` — unmapped label
- `Gray equilibrium` = `Approximately 58 K / 55 K, respectively` — unmapped label
- `Shared circular Hill scale` = `Approximately 8.27 million km` — unmapped label
- `Small moons` = `Four shared circumbinary satellites, each <100 km diameter` — unmapped label

**Ɬiʔa System/Two-Face**
- `Designations` = `Two-Face; Mirar's Veil b; AQ-MV-01 b` — unmapped label
- `Orbital eccentricity / inclination` = `Nominal 0.01 / 1° to the inner reference plane; complete resonant elem` — combined row: label/value counts differ
- `Period ratio with c` = `Target Pb/Pc = 2/3; resonance libration not yet demonstrated` — unmapped label
- `Core mass fraction` = `Approximately 75% target; a detailed equation-of-state fit remains nec` — unmapped label
- `Stellar irradiation` = `Approximately 1.717 Earth flux, or 2337 W/m² at the reference distance` — unmapped label
- `Dry molecular backbone` = `55% N₂, 44.9% CO₂, 0.1% CO; minor plume and upper-atmosphere species v` — unmapped label
- `Temperature targets` = `Hot illuminated terrain 400–450 K; night 160–190 K; small exceptional ` — unmapped label
- `Temperate frontier` = `Approximately 270–300 K locally, slightly onto the illuminated side; n` — unmapped label
- `Example molecular scale heights` = `Approximately 6.0 km at 430 K and 2.5 km at 180 K for the reference mi` — unmapped label
- `Intrinsic magnetic field` = `Nominal 60 μT equatorial dipole reference, with multipolar/local anoma` — unmapped label
- `Magnetic-axis inclination` = `Nominal ~85° to the spin axis; does not define a continuous terminator` — unmapped label
- `Roche reference` = `Fluid aggregate at 3000 kg/m³: approximately 24,400 km from the center` — unmapped label
- `Tidal response` = `Q = 80 is a model input, not a measurement; k₂ and internal response r` — unmapped label
- `Moons / rings [rings]` = `the luminous girdle is atmospheric/plasma emission, not a particulate ` — unmapped label

**Ɬiʔa System/Ɬiʔa System**
- `Present stellar mass` = `0.20 M☉` — unmapped label
- `Listed star plus planetary masses` = `Approximately 0.20007 M☉; excludes an unquantified minor-body/moon cor` — unmapped label
- `J2000 reference direction` = `RA 17h23m00s, Dec −21°00′00″` — unmapped label
- `Distance / nominal parallax [nominal parallax]` = `65.36 mas` — unmapped label
- `Galactic direction` = `l ≈ 3.95°, b ≈ +8.59°` — unmapped label
- `Earth-frame Galactic XYZ` = `Approximately (15.09, 1.04, 2.28) pc` — unmapped label
- `Present stars` = `One; no current bound stellar companion is specified` — unmapped label
- `Satellite inventory` = `Five at Belted King, two at The Corpse, four shared by Shield Couple, ` — unmapped label
- `Nearest physical stellar neighbor` = `Unassigned; angular proximity to HD 156026 is not a nearest-neighbor d` — unmapped label
- `Outer planetary barycenter` = `1.5 AU` — unmapped label
- `Outer debris population` = `Described over 3–10 AU` — unmapped label
- `30-AU Kuiper cliff` = `Not established` — unmapped label
- `Present irradiation snow-line estimate` = `Approximately 0.2075 AU; not the primordial disk snow line` — unmapped label
- `Astropause / wind boundary [astropause]` = `Not calculated` — unmapped label
- … and 6 more

## Sample proposed frontmatter

### Ɬiʔa System/Middle Path

```yaml
---
type: "planet"
system: "[[Ɬiʔa System]]"
star: "[[Mirar's Veil]]"
mass_earth: 1.05
radius_earth: 1.0247
semimajor_au: 0.07684
orbital_speed_kms: 48.05
hill_radius_km: 199845.0
eccentricity: 0.01
obliquity_deg: 0.0
period_days: 17.396
rotation_period_hours: 417.504
tidally_locked: True
albedo_bond: 0.2
temperature_mean_k: 288.0
pressure_surface_bar: 1.6212
moons_count: 1
density_gcc: 5.38049
gravity_ms2: 9.82021
escape_kms: 11.3234
area_km2: 535573000.0
volume_km3: 1165470000000.0
circumference_km: 41018.9
---
```

### Aethonix System/Aethonix

```yaml
---
type: "star"
system: "[[Aethonix System]]"
system_luminosity_sun: 1.7
metallicity_feh: 0.15
age_gyr: 4.0
distance_ly: 42.0
ra_hours: 9.3333
dec_deg: -50.0
constellation: "Vela"
a_mass_sun: 1.1
a_radius_sun: 1.161
a_luminosity_sun: 1.502
a_teff_k: 5930.0
a_spectral_type: "G0V"
a_rotation_period_days: 26.0
b_mass_sun: 0.7
b_radius_sun: 0.7
b_luminosity_sun: 0.198
b_teff_k: 4600.0
b_spectral_type: "K4V"
b_rotation_period_days: 41.0
components: 
  - "a"
  - "b"
binary_separation_au: 0.15
binary_eccentricity: 0.01
---
```

### Gammal System/Dold-Pärla

```yaml
---
type: "moon"
system: "Gammal"
star: "Storebror"
mass_earth: 0.9
radius_earth: 0.95
albedo_bond: 0.32
temperature_mean_k: 290.15
temperature_mean_k_min: 288.15
temperature_mean_k_max: 292.15
pressure_surface_bar: 1.0
surface_coverage: "77% liquid water, mainly saline oceans; 23% land"
density_gcc: 5.78755
gravity_ms2: 9.7931
escape_kms: 10.8878
area_km2: 460333000.0
volume_km3: 928715000000.0
circumference_km: 38028.7
---
```

### Aethonix System/Life on Lunara

```yaml
---
type: "biosphere"
system: "[[Aethonix System]]"
planet: "[[Lunara (moon)]]"
solvent: "Water–Ammonia brine"
backbone: "Carbon-based"
primary_metabolism: "Geochemical and radiolysis-fed chemosynthesis; supplemental speculative direct radiotrophy"
redox_couples: 
  - "H₂/SO₄²⁻"
  - "CH₄/CO₂"
  - "Fe²⁺/Fe³⁺"
  - "Radiolytic OH•/organics"
membrane_chemistry: "Mixed lipids and cryostable ether derivatives"
photosynthesis_band_nm: "No photosynthetic primary-production pathway specified; optical signaling/sensing is separate"
biosphere_age_gyr: 1.0
seeding_origin: "Panspermia (cometary extremophiles)"
dominant_lifeforms: 
  - "Towers"
  - "Scorchers"
  - "Zeppeliforms"
  - "Janusthropes"
ecosystems: 
  - "Chemovents"
  - "Radiogenic bloom fields"
  - "Brine caverns"
  - "Floating colonies"
biosphere_state: "Stable with episodic expansions"
intelligent_species: 
  - "Janusthropes: intelligent social/tool-using animals"
  - "no demonstrated sapient civilization"
civilization_level: "None"
surface_coverage: "Cryobrine seas, ammonia lakes, tholin plains, geothermal basins"
---
```

### Sol System/Earth

```yaml
---
type: "planet"
system: "[[Sol System]]"
star: "[[Sun]]"
mass_earth: 1.0
radius_earth: 1.0
semimajor_au: 1.0
eccentricity: 0.017
inclination_deg: 0.0
obliquity_deg: 23.4
period_days: 365.25
rotation_period_hours: 23.9352
flux_earth: 1.0
moons_count: 1
density_gcc: 5.51344
gravity_ms2: 9.8203
escape_kms: 11.1862
area_km2: 510064000.0
volume_km3: 1083210000000.0
circumference_km: 40030.2
---
```

### Thrírlitir System/Valen

```yaml
---
type: "planet"
system: "[[Thrírlitir System]]"
star: "[[Thrírlitir#Binary Pair B+C]]"
mass_earth: 1.33
radius_earth: 1.1
semimajor_au: 0.8
hill_radius_km: 1220000.0
roche_limit_km: 18000.0
eccentricity: 0.06
inclination_deg: 1.0
obliquity_deg: 20.0
period_days: 233.8
rotation_period_hours: 23.0
flux_earth: 1.15
flux_earth_min: 0.82
flux_earth_max: 1.48
albedo_bond: 0.37
temperature_mean_k: 290.0
pressure_surface_bar: 0.95
moons_count: 2
named_after: "Old Aialonic root related to \"vale\" / \"valley\""
adjectives: 
  - "Valenic"
density_gcc: 5.5093
gravity_ms2: 10.7942
escape_kms: 12.3002
area_km2: 617178000.0
volume_km3: 1441750000000.0
circumference_km: 44033.2
---
```

