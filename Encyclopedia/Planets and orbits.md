---
type: "encyclopedia"
aliases:
  - "Orbits"
  - "Planetary orbits"
tags:
  - "aquatikiverse"
  - "encyclopedia"
  - "physics"
status: "draft"
---

# Planets and orbits

## Summary

A planet's orbit decides how much starlight it gets, how long its year is, and whether it can stay in place for billions of years. Three ideas do most of the work: **Kepler's third law** (farther means slower), the **inverse-square law** (farther means dimmer) and **gravitational stability** (some orbits are shaken apart by neighbours). The [[Sol System]] is the worked example throughout.

## Year and distance

Kepler's third law links an orbit's period P in years to its semimajor axis a in AU and the star's mass M in solar masses: **P² = a³ / M**. Earth (1 AU, 1 M☉) has P = 1 year; Mercury (0.387 AU) has P = 0.241 years; Neptune (30.07 AU) has P = 164.9 years. A star twice as massive gives a year 1/√2 as long at the same distance. This is how the vault fixes every planet's year from its orbit and star: for example [[Valen]] (0.80 AU around the 1.25 M☉ B+C pair) has a year of 0.80^1.5 / √1.25 = 0.640 years, and [[Mot]] (117 AU around 2.55 M☉) has 792.5 years.

## Starlight and temperature

**Flux.** Starlight spreads over the surface of a sphere, so flux falls as 1/d². In Earth units, a star of luminosity L (in L☉) delivers **S = L / a²** F⊕ at distance a AU, where 1 F⊕ ≈ 1,361 W/m². Mars receives 0.43 F⊕ and Neptune 0.0011 F⊕.

**Equilibrium temperature.** A planet absorbs sunlight over its cross-section and radiates from its whole surface, so its equilibrium temperature is **T = 278.3 K × S^¼ × (1 − A)^¼**, where A is the Bond albedo (the fraction of light reflected) and the formula assumes heat is spread evenly. Earth with A = 0.306 has T ≈ 254 K, which is 34 K below its actual 288 K mean: the difference is the greenhouse effect. Venus is the opposite extreme, with 737 K at the surface against about 230 K at equilibrium.

**Not every point is the same.** Spread over only the sunlit side, the temperature is a factor 2^¼ = 1.19 higher; directly under the star it is 2^½ = 1.41 times higher. A planet with no atmosphere and a locked spin has very different hot and cold sides, which is why the dwarf planets [[Pekhám]] and [[Barzél]] are described as two-faced worlds rather than by a single temperature.

**Eccentric orbits** change the flux over the year by a factor ((1+e)/(1−e))²; Mars varies between 0.36 and 0.52 F⊕, and Mercury (e = 0.206) between 4.6 and 10.6 F⊕.

## Spin and tides

A planet's day, tilt and spin history are set by tides. Tides from the star (or a moon) slow a planet's rotation until it **locks** in a resonance: Mercury turns three times per two orbits, while planets close to their stars usually lock 1:1, always showing one face to the star. Locking times grow steeply with distance (as a⁶): about 10⁴ years for bodies at 0.05 AU, such as Barzél and Pekhám, and many gigayears at 1 AU for a planet like Earth. A large moon stabilises a planet's tilt: Earth's 23.4° is steady, while Mars's wanders because Phobos and Deimos are too small.

## Stability

**Hill sphere.** A planet controls space out to about r_H = a (m / 3M)^(1/3). Moons are stable out to about half that distance if they orbit in the planet's direction and out to roughly 0.7 of it if they orbit the other way. [[Mot]], at 30 Earth masses and 117 AU, has a Hill radius of 2.7 AU, so a moon at 580,000 km is far inside it.

**Roche limit.** A body held together by its own gravity is torn apart by tides when it gets closer than about 2.44 R (ρ_planet / ρ_body)^(1/3). Rings form from material inside this limit.

**Resonances and neighbours.** Orbits whose periods are simple ratios (such as 3:2 for Pluto and Neptune) can protect or destabilise bodies. Planets also stir each other: Jupiter shapes the asteroid belt, and Neptune's resonance protects Pluto. Systems are tested by integrating the orbits numerically for long periods.

**Planets in binary stars.** A planet circling one star of a close binary (an *S-type* orbit) is stable only inside a critical radius of roughly a third to a half of the binary separation, and a planet around both stars (a *P-type* or circumbinary orbit) only outside a critical radius of about 2–4 times the separation. The Holman–Wiegert formulae give these limits as a function of the mass ratio and eccentricity.

## In the Aquatikiverse

The vault uses these tools to check its own worlds. In [[Thrírlitir System]], Valen was moved from 0.779 to 0.80 AU because the circumbinary 4:1 resonance with the B–C binary at 0.757 AU destabilised it (an N-body screen of 10⁶ years, 4 of 4 runs stable at 0.80 AU). [[Aialon]] sits at 83% of its critical radius around A, and the close-in dwarf planets [[Pekhám]] (limit 0.061 AU, at 0.05) and [[Barzél]] (limit 0.101 AU, at 0.05) are stable because they sit inside the S-type limits. [[Mot]]'s year, [[Aphrod]]'s 7:5 near-resonance with [[Valen]] and [[Ceraun]]'s tidal locking all follow from the formulae above.

## References

- [JPL Planetary Physical Parameters](https://ssd.jpl.nasa.gov/planets/phys_par.html) and [NASA Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html): the Solar System values used above.
- [Holman & Wiegert 1999, "Long-term stability of planets in binary systems"](https://arxiv.org/abs/astro-ph/9809315): the critical-radius formulae.
- Kopp & Lean 2011, *Geophysical Research Letters* 38, L01706, the solar constant of 1,361 W/m² (cited from memory; not yet checked against the source).
- The Kepler, Hill, Roche and equilibrium-temperature formulae are standard textbook results.
