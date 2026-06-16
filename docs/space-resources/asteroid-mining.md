# Asteroid Mining

> **Node ID**: space-resources.asteroid-mining
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: mining, automation
> **Enables**: 
> **Timeline**: Years 80+
> **Outputs**: asteroid_materials, asteroid_water
> **Critical**: NO — Asteroid mining multiplies the mass budget of industrial civilization by accessing the ~10^11 tonnes of resources in near-Earth objects, but no single asteroid-derived material is on the critical path to bootstrapping; it is an expansion and sustainability capability, not a bottleneck

Asteroid mining is the prospecting, extraction, and processing of resources from minor planets — predominantly near-Earth objects (NEOs) and main-belt asteroids. Where terrestrial mining fights gravity, oxidation, and biosphere regulation, asteroid mining fights vacuum, distance, and the absence of any pre-existing industrial base. The payoff is enormous: a single M-type asteroid such as 16 Psyche contains roughly 10^19 kg of iron-nickel, and a modest 1 km C-type (carbonaceous) body holds more water than has ever been launched from Earth. This article covers the integrated capability across three process areas: [prospecting](./asteroid-mining.prospecting.md), [extraction methods](./asteroid-mining.extraction-methods.md), and [water extraction](./asteroid-mining.water-extraction-asteroid.md).

## Overview

The asteroid resource base divides cleanly into three spectral classes, each mined for a different purpose. **C-type** (carbonaceous, chondrite) asteroids are the priority targets for early operations because they contain 5-20% structural water bound in hydrated phyllosilicate minerals, plus organic compounds and carbon. Water is the highest-value early product: it splits into hydrogen and oxygen propellant, provides radiation shielding, and supports life support. **S-type** (silicaceous) asteroids are rocky, dominated by pyroxene, olivine, and iron sulfide, with small fractions of free metal. **M-type** (metallic) asteroids are the long-term prize: nearly pure iron-nickel bodies, likely the exposed cores of differentiated parent bodies that were shattered in ancient collisions.

The bootstrapping sequence is deliberate. Early operations target water-rich C-type NEOs because water has the highest specific value-per-kilogram in cislunar space (propellant sells itself). Metal extraction follows once the propellant infrastructure makes round-trips economical. The whole enterprise depends on two upstream capabilities: [mining](../mining/) (the terrestrial discipline of prospecting, drilling, comminution, and beneficiation, translated to a regolith context) and [automation](../automation/) (because lightspeed delay, radiation, and the sheer distance make telerobotic and fully autonomous operation mandatory).

### Asteroid Class Comparison

| Class | Composition | Water Content | Key Resources | Example | Priority |
|-------|-------------|---------------|---------------|---------|----------|
| C-type (CI/CM chondrite) | Phyllosilicates, organics, carbon | 5-20% | Water, organics, PGMs | Bennu (B-type) | 1 (early propellant) |
| S-type | Pyroxene, olivine, FeS | 0.1-1% | Silicates, Fe, Ni | Itokawa | 2 (structural metals) |
| M-type | Fe-Ni metal, PGMs | trace | Iron, nickel, cobalt | 16 Psyche | 3 (bulk metal) |
| D/P-type | Organics, ices | up to 25% (outer) | Volatiles, organics | Outer belt | 4 (far-term) |

## Notable Asteroids and Mission Heritage

The case for asteroid mining rests on ground-truth from sample-return missions and spectral surveys. These are the reference points every design study benchmarks against:

Three missions — Hayabusa, Hayabusa2, and OSIRIS-REx — have now returned pristine asteroid material to Earth, transforming asteroid composition from inference into measured fact. The Psyche orbiter (en route to 16 Psyche, arrival 2029) will extend this ground truth to the M-type class.

| Asteroid | Class | Mission | Sample Mass | Year | Key Finding |
|----------|-------|---------|-------------|------|-------------|
| 25143 Itokawa | S-type | Hayabusa (JAXA) | ~1 g | 2010 | Rubble-pile, mm grains, LL-chondrite composition |
| 162173 Ryugu | Cb-type | Hayabusa2 (JAXA) | 5.4 g | 2020 | CI-like, hydrated, NH3 and organics detected |
| 101955 Bennu | B-type (C-subclass) | OSIRIS-REx (NASA) | 250 g | 2023 | Hydrated phyllosilicates, magnetite, carbonates |
| 16 Psyche | M-type | Psyche (NASA, en route) | — | 2029 (arrival) | 226 km diameter, ~10^19 kg metal-rich |
| 433 Eros | S-type | NEAR-Shoemaker | — | 2001 | Orbital + landing, Mg/Si/Fe abundance maps |

The OSIRIS-REx mission to Bennu is the defining modern data point. It returned 250 grams of regolith in September 2023 — roughly 4x the original mission requirement of 60 g — confirming that Bennu is a hydrated carbonaceous chondrite analog rich in phyllosilicates, magnetite, carbonates, and organic molecules. Spectral analysis showed a 2.7 micron absorption feature diagnostic of O-H stretching in hydrated minerals, the direct signature of structurally bound water. The Touch-And-Go Sample Acquisition Mechanism (TAGSAM) used pressurized nitrogen gas to fluidize regolith into a collector head on a brief contact lasting under 6 seconds — a proof of concept for non-contact, low-reaction-force sampling in microgravity.

Hayabusa2's Ryugu sample was even more revealing: laboratory analysis of the 5.4 g returned in December 2020 identified CI-group chondrite affinity, amino acids (including proteinogenic types), nucleobases, and ammonium salts — evidence that carbonaceous asteroids delivered prebiotic organics and volatile nitrogen to the early inner solar system.

## Spectral Prospecting

Before any extraction, asteroids must be characterized remotely. See [prospecting](./asteroid-mining.prospecting.md) for the full process. The workhorse technique is **near-infrared reflectance spectroscopy** in the 1-2.5 micron range, where diagnostic absorption bands reveal mineralogy:

- **2.7-2.9 micron**: O-H stretch in hydrated phyllosilicates — the primary water indicator. Strong in CI/CM chondrites; absent in anhydrous S-types
- **1.4 micron**: O-H first overtone — secondary hydration indicator
- **1.9 micron**: H2O combination band — adsorbed/interlayer water
- **1.0 and 2.0 micron**: Fe2+ absorption in pyroxene and olivine — S-type discriminator
- **0.5-0.7 micron**: Charge-transfer features revealing Ni-Fe metal content — M-type signature
- **3.0-3.8 micron**: C-H stretch organics and carbonates

| Spectral Feature | Wavelength | Diagnostic Of | Class Marker |
|------------------|-----------|---------------|--------------|
| O-H stretch | 2.7 micron | Hydrated phyllosilicates | C-type (water) |
| Fe2+ band I | 1.0 micron | Pyroxene, olivine | S-type |
| Fe2+ band II | 2.0 micron | Pyroxene | S-type |
| Ni-Fe slope | 0.5-0.7 micron | Free metal | M-type |
| Organics | 3.4 micron | Aliphatic C-H | C/D-type |
| Carbonate | 3.9-4.0 micron | Ca-Mg carbonates | CI/CM |

Survey is conducted by space-based telescopes (the NEO Surveyor mission, launching ~2027, will discover and characterize the NEO population in the thermal infrared at 4-5 micron and 6-10 micron) supplemented by rendezvous spacecraft that measure density (via gravitational perturbation), thermal inertia (via infrared radiometry), and surface roughness (via radar). Thermal inertia distinguishes bare rock (~500-2500 J m^-2 K^-1 s^-1/2) from fine regolith/dust (~30-100), which in turn predicts whether the surface is coherent (drillable) or unconsolidated (scoopable).

## Water Extraction

Water is the keystone early product. See [water extraction](./asteroid-mining.water-extraction-asteroid.md) for the full process. Carbonaceous chondrites of the CI and CM groups contain 5-20% water by mass, locked in three reservoirs:

1. **Adsorbed water** (released 100-150 C): physically adsorbed on grain surfaces
2. **Interlayer water** (released 150-300 C): bound between phyllosilicate sheets
3. **Structural OH** (released 300-800 C): chemically bound in the mineral lattice, requires dehydroxylation

The extraction process heats crushed regolith in a sealed, solar-concentrator-heated retort. Released water vapor is captured on a cold finger, purified, and stored as ice or electrolyzed immediately into H2 and O2 propellant. The energy budget is substantial: heating 1 tonne of CI-chondrite regolith (specific heat ~800 J/kg/K) to 800 C requires roughly 600 MJ of thermal energy, or ~1.7 hours of direct solar concentration at 100 kW.

| Heating Phase | Temperature | Water Released | Energy (per tonne) |
|---------------|-------------|----------------|--------------------|
| Drying | 100-150 C | Adsorbed H2O | ~80 MJ |
| Interlayer | 150-300 C | Bound H2O | ~180 MJ |
| Dehydroxylation | 300-800 C | Structural OH | ~600 MJ (total to 800 C) |
| **Total** | **to 800 C** | **5-20% by mass** | **~600 MJ** |

For a 1 km C-type asteroid containing even 10% water, the accessible resource is ~10^11 kg of water — enough to refuel every launch ever conducted from Earth, thousands of times over. The electrolysis step (H2O -> H2 + 1/2 O2) consumes ~237 kJ of electrical energy per mole of water (the Gibbs free energy), or ~13 MJ per kg of water, plus overpotential losses raising the practical figure to ~50 MJ/kg.

## Metal Extraction Methods

See [extraction methods](./asteroid-mining.extraction-methods.md) for the full process. Three complementary techniques recover metals from asteroid regolith:

### Thermal Volatilization

Heating regolith to high temperature (1200-2000 C) under vacuum vaporizes volatile metals and sulfur, which recondense on a cold trap. This is energy-intensive but mechanically simple, requiring only solar concentrators and a condenser array. The sequence of volatilization tracks vapor pressure: sulfur and zinc first, then sodium and potassium, then iron at the highest temperatures. Fractional condensation on a temperature-graded cold trap separates the elements spatially, yielding distinct metal deposits without chemical processing.

### Magnetic Separation

M-type asteroids and the metal fractions of other classes contain free metal grains (kamacite, taenite — Fe-Ni alloys). After comminution (crushing/grinding), a rotating magnetic drum or superconducting separator pulls the ferromagnetic fraction away from silicate gangue. This is the lowest-energy beneficiation step and recovers the highest-grade metal concentrate. The meteorite analog (iron meteorites such as Canyon Diablo) shows coarse Widmanstatten intergrowth of kamacite and taenite, with grain sizes of millimetres to centimetres — easily liberated by moderate crushing. The Ni content of kamacite (~5-7%) and taenite (~30-60%) means the separated metal is already a stainless-grade alloy, requiring no terrestrial-style smelting to remove oxygen (there is none in vacuum-recovered metal).

### Chemical Leaching

For elements dispersed in the silicate matrix (platinum-group metals at ppm levels, rare earths), aqueous or acid leaching dissolves the target element, which is then electrochemically plated out. This requires imported reagents (sulfuric acid, hydrochloric acid) or in-situ-generated leachant, and is far more complex — typically reserved for high-value PGM recovery. PGM concentrations in iron meteorites reach 10-100 ppm, modest by terrestrial mine grades but significant given the sheer mass of an M-type body.

### Comminution in Microgravity

Crushing and grinding (comminution) is the universal first step in beneficiation, liberating mineral grains from their host matrix. Terrestrial ball mills and SAG mills rely on gravity to cascade the grinding media; in microgravity, the media float free and impart no impact energy. Microgravity comminution substitutes centrifugal mills (spinning the charge against the mill wall) or vibratory mills that drive media by inertia rather than weight. The energy input per tonne is comparable to terrestrial practice (10-30 kWh/tonne), but the equipment must be fully enclosed to contain ejecta.

| Method | Target | Energy | Complexity | Yield |
|--------|--------|--------|------------|-------|
| Magnetic separation | Fe-Ni metal grains | Low | Low | High (free metal) |
| Thermal volatilization | Volatile metals, S | High | Low | Medium |
| Chemical leaching | PGMs, REEs | Medium | High | Low (ppm feed) |

### 16 Psyche: The Metal Endowment

The archetype M-type asteroid, 16 Psyche, illustrates the scale of the metal resource. With a mean diameter of 226 km and an estimated bulk density of ~4000 kg/m^3, Psyche's mass is roughly 2.4 x 10^19 kg. Even if only 10% of that mass is accessible Fe-Ni metal, the recoverable iron (~2 x 10^18 kg) exceeds Earth's entire proven iron-ore reserves (~10^14 kg of contained Fe) by a factor of 10,000. Psyche is the target of NASA's Psyche orbiter mission, arriving in 2029, which will map the body's composition and gravity field to test whether it is indeed an exposed planetary core.

## The Microgravity Operating Environment

Asteroid operations occur in a regime that is neither terrestrial nor lunar. Key characteristics:

- **Microgravity (10^-4 to 10^-6 g)**: Excavation cannot rely on weight for reaction force. Anchoring harpoons, cold-gas thrusters, or clamp-foot mechanisms grip the surface to provide reaction mass. Drilling requires the spacecraft to "push" against the asteroid, not just spin the bit
- **Vacuum**: No atmosphere means no convective cooling, no oxidation, no dust transport by wind. Waste heat must be radiated. Dust produced by mining does not settle — it follows ballistic trajectories and contaminates optics and mechanisms
- **Temperature extremes**: Surface temperatures swing from -100 C to +100 C across the day-night cycle at 1 AU, inducing thermal stress in equipment and causing outgassing from hydrated minerals when sunlit
- **Rubble-pile structure**: Most NEOs above ~200 m are not solid monoliths but gravitationally aggregated rubble piles (bulk porosity 30-50%), as confirmed by Hayabusa at Itokawa and OSIRIS-REx at Bennu. This means regolith is already pulverized (no drilling needed) but the body has no structural strength for anchoring
- **Rotation**: Many NEOs rotate with periods of 2-12 hours; some spin near the breakup limit. Operations must contend with a moving, centrifugally variable gravity field
- **Radiation**: Outside Earth's magnetosphere, galactic cosmic rays and solar particle events expose electronics to total ionizing dose and single-event upsets. Mining avionics require radiation-hardened or radiation-tolerant design, mirroring [spacecraft systems](../spacecraft-systems/) practice

### Anchoring and Reaction Force

The reaction-force problem is the defining mechanical challenge. On Earth, a drill pushes down using its own weight; on an asteroid, applying torque or thrust without an anchor simply pushes the spacecraft away. Four anchoring strategies are in development:

1. **Harpoon/pylons**: Fired into the regolith by compressed gas or explosive charge. Effective on cohesive surfaces; risk of ejecta on rubble piles. The Philae lander on comet 67P demonstrated both the promise (it anchored) and the peril (the anchor failed to deploy, and it bounced)
2. **Cold-gas thrusters**: Downward-facing thrusters hold the craft against the surface. Reliable but consumes propellant continuously during contact
3. **Clamp/grip feet**: Mechanical claws grip surface protrusions. The OSIRIS-REx TAGSAM avoided this entirely by using a touch-and-go sampling stroke under 6 seconds with minimal reaction force
4. **Microspine arrays**: Biomimetic arrays of tiny hooks that engage asperities in rough rock, borrowed from [automation](../automation/) climbing-robot technology. Effective on coherent rock but less so on smooth or dusty surfaces

## Mining and Automation Dependencies

Asteroid mining is an extreme expression of two mature terrestrial capabilities:

- **[Mining](../mining/)**: The core mining disciplines — prospecting (geophysical survey), comminution (crushing and grinding), beneficiation (separating ore from gangue), and material handling — all translate directly. What changes is the reaction-force problem (no gravity to push against), the dust mitigation problem (vacuum ballistics, no air drag to stop fines), and the energy source (solar photovoltaic and solar-thermal concentration replace diesel and grid power). The [mining](../mining/) domain's hard-won knowledge of cut-off grades, reserve estimation, and throughput scaling provides the engineering framework
- **[Automation](../automation/)**: Round-trip light time to a typical NEO is 2-20 minutes each way. Telerobotic control at those latencies is impractical for manipulation tasks (human reaction time is ~200 ms). Operations must be autonomous at the level of individual mining unit actions: approach, anchor, excavate, process, and store, all supervised by onboard software with only high-level goals uplinked from Earth. This demands the full stack of [automation](../automation/) capability: sensor fusion, path planning, fault detection and recovery, and autonomous decision-making under uncertainty

## Energy Requirements

Every extraction step is gated by energy. In deep space, the only practical sources are solar photovoltaic (degrading with the inverse square of distance from the sun) and nuclear (radioisotope thermoelectric generators for low power, fission for high power). The choice between them is the single largest driver of mission architecture: solar limits operations to the inner solar system and imposes large deployed array areas; nuclear enables main-belt operations and continuous power through asteroid night, but requires enriched fuel and a licensed launch approval process.

Solar concentrators (parabolic reflectors or Fresnel lenses focusing sunlight onto a retort) are uniquely suited to thermal extraction because they convert sunlight directly to process heat without the electrical conversion losses (~30% for PV) that would otherwise multiply the energy cost. A 100 kW-thermal concentrator delivering ~600 MJ to a retort in under two hours is far more mass-efficient than an equivalent electric heater powered by PV.

| Operation | Energy per tonne regolith | Source |
|-----------|---------------------------|--------|
| Excavation (cutting/breaking) | 1-10 kWh | Electric actuators |
| Comminution (grinding) | 10-30 kWh | Electric mills |
| Water extraction (to 800 C) | ~170 kWh (600 MJ) | Solar concentrator |
| Magnetic separation | 1-5 kWh | Electromagnets |
| Electrolysis (H2O -> H2 + O2) | ~50 kWh per tonne water | PV electric |
| Thermal volatilization (to 1500 C) | ~400 kWh | Solar concentrator |

At 1 AU, a 100 kW solar array (roughly 500 m^2 at 20% efficiency) delivers ~600 kWh per 6-hour mining shift. This is enough to process roughly 3 tonnes of regolith per day through the water-extraction pathway — a meaningful but not transformative rate. Scaling to industrial output (1000s of tonnes/day) requires either very large solar arrays or space-deployed fission reactors.

Solar power falls off with the inverse square of heliocentric distance. At 2 AU (main belt), irradiance drops to ~340 W/m^2, a quarter of the 1 AU value, quadrupling the array area needed for the same power. This is why C-type NEOs (perihelia near or inside 1 AU) are prioritized over main-belt targets for early operations — not because the belt lacks resources, but because the power penalty is prohibitive until nuclear fission is available.

| Distance | Irradiance | Relative Power | Array Area for 100 kW |
|----------|-----------|----------------|------------------------|
| 0.8 AU | 2127 W/m^2 | 1.56x | ~240 m^2 |
| 1.0 AU | 1361 W/m^2 | 1.0x | ~370 m^2 |
| 1.5 AU | 605 W/m^2 | 0.44x | ~830 m^2 |
| 2.0 AU | 340 W/m^2 | 0.25x | ~1470 m^2 |
| 2.7 AU (belt) | 187 W/m^2 | 0.14x | ~2670 m^2 |

## Economics and the Propellant Value Chain

The economic case for asteroid mining rests on the cost of launching mass from Earth versus retrieving it from space. Launch to low Earth orbit costs roughly $1,500/kg (Falcon 9, reusable) and to GEO or lunar orbit 3-10x more. Water delivered to a cislunar refueling depot from a C-type asteroid, even after the mining and transport overhead, can in principle undercut Earth-launched water by an order of magnitude once the mining infrastructure is amortized.

The key insight is that water is not consumed at the asteroid — it is converted to propellant and used to move other things. A single 100 m C-type asteroid (water content ~10%) yields roughly 10^7 kg of water, producing ~10^6 kg of hydrogen and ~10^7 kg of oxygen — enough propellant to deliver ~3000 tonnes of payload from LEO to lunar orbit, or to refuel hundreds of upper stages. Platinum-group metals are the oft-cited alternative revenue source, but their terrestrial market is small (~200 tonnes/year of platinum) and would be saturated by returning even a modest asteroid fraction; the value lies instead in using them in space rather than importing them to a saturated Earth market.

The bootstrapping logic reverses the usual terrestrial sequence: rather than mining metal first and using it to build infrastructure, asteroid mining extracts propellant first (water), uses that propellant to cheaply move large masses, and only then mines metal in volume once transport is no longer the binding cost. This is why water-rich C-type targets, not metal-rich M-types, anchor the early capability.

## Target Selection

Not all NEOs are worth mining. The economic target is a water-rich C-type on a low-delta-v trajectory relative to Earth — one that a chemical spacecraft can reach, loiter at, and return from with propellant to spare. The **accessibility metric** is the total delta-v from low Earth orbit to the asteroid surface and back to a cislunar depot; values below ~5 km/s are competitive with lunar-sourced propellant.

- **Delta-v budget**: LEO departure (~3.2 km/s) + rendezvous + landing + ascent + return. The lowest-energy targets require ~4.5-6 km/s total; these are rare (a few dozen known) but new surveys continuously expand the catalogue
- **Stay time**: Mining campaigns of 1-3 years require the target's orbital phasing to permit long residence without enormous station-keeping cost. Some NEOs are only briefly accessible every few years
- **Size**: Targets below ~50 m diameter hold insufficient total resource to amortize mission cost; targets above ~1 km are structurally complex and risk-prone. The sweet spot is 100-500 m water-rich bodies
- **Spin state**: Slow rotators (period > 4 hours) are preferred because they present long, predictable work windows. Fast rotators (period < 2 hours) are dynamically stressful and may be monolithic rather than rubble piles

## Mission Architecture

A mining campaign to a single NEO is not a single spacecraft but a sequence of purpose-built vehicles, each optimized for one phase. The reference architecture for a C-type water-mining mission:

1. **Prospector** (~500 kg): A small rendezvous spacecraft carrying multispectral imagers, a near-infrared spectrometer (1-2.5 micron), a thermal-infrared radiometer, and a gravimeter. Spends 6-12 months characterizing the target, producing a high-resolution shape model, density estimate, hydration map, and hazard catalogue (boulders, slopes, jet activity)
2. **Transporter-miner** (~5000 kg): Launched on a heavy-lift vehicle to a halo orbit around the target. Carries the excavation and processing hardware: solar concentrator (~100 kW thermal), retort, condenser, electrolysis unit, and cryocooler for propellant storage. Operates autonomously for the 1-3 year mining campaign
3. **Propellant tanker**: Cycles between the asteroid and a cislunar depot (typically a near-rectilinear halo orbit around the Moon or an Earth-Moon L2 gateway), ferrying cryogenic hydrogen and oxygen in insulated tanks. Each tanker carries ~10-50 tonnes of propellant per trip
4. **Depot**: A crewed or autonomous station in cislunar space that receives, stores, and dispenses asteroid-derived propellant to customer spacecraft. Long-duration cryogenic storage (zero-boiloff) is the depot's core technical challenge — passive insulation alone cannot stop boiloff over months, so active cryocoolers (Stirling or pulse-tube) intercept the heat leak. The depot also performs propellant transfer: either pump cryogens through a docking coupling (hard, because cryogenic pumps cavitate) or settle the liquids with small thruster impulses and drain by pressure (simpler, but wasteful of pressurant gas).

| Element | Mass Class | Power | Mission Duration | Key Tech |
|---------|-----------|-------|------------------|----------|
| Prospector | 500 kg | 1 kW | 6-12 months | NIR spectrometer, autonomy |
| Transporter-miner | 5000 kg | 100 kW | 1-3 years | Solar concentrator, retort |
| Tanker | 2000 kg dry | 5 kW | 1-2 years per cycle | Cryo storage, transfer |
| Depot | 10000+ kg | 50 kW | Permanent | Zero-boiloff cryocooling |

The total campaign from prospector launch to first propellant delivery typically spans 5-8 years, dominated by interplanetary transit (months to a year each way for NEO-class targets) and the slow accumulation of mined product. This long horizon is why the [automation](../automation/) dependency is non-negotiable: no single spacecraft can be babysat from Earth for that duration.

### Dust Mitigation

Mining ejects fine regolith at low velocity. In vacuum, these grains follow ballistic trajectories and do not settle — they coat optical surfaces, abrade mechanisms, and short electrical contacts. Mitigation strategies include: shrouding excavation points with deployable curtains; electrostatic grids that charge and deflect dust; and designing all moving interfaces for dust tolerance ( labyrinth seals rather than contact seals). The [mining](../mining/) domain's terrestrial dust-control practice (water sprays, baghouses) is inapplicable because water cannot be sprayed into vacuum. Instead, the [automation](../automation/) discipline contributes the sealed, sensor-monitored handling systems that keep dust contained within processing enclosures.

## Key Parameters Summary

| Parameter | Value | Notes |
|-----------|-------|-------|
| C-type water content | 5-20% | CI/CM chondrite class |
| Water extraction temperature | 150-800 C | Stepwise heating |
| Energy to extract water | ~600 MJ/tonne | To 800 C |
| Bennu sample returned | 250 g | OSIRIS-REx, 2023 |
| Ryugu sample returned | 5.4 g | Hayabusa2, 2020 |
| 16 Psyche mass | ~2.4 x 10^19 kg | M-type, mostly Fe-Ni |
| 16 Psyche Fe content | ~10^18 kg (est.) | 10,000x Earth reserves |
| NEO round-trip light time | 2-20 min | Drives autonomy requirement |
| Surface gravity | 10^-4 to 10^-6 g | Rubble-pile NEOs |
| Solar irradiance at 1 AU | 1361 W/m^2 | PV + concentrator input |
| Typical NEO rotation | 2-12 hours | Some near breakup limit |
| Bulk porosity (rubble piles) | 30-50% | Bennu, Ryugu measured |
| PGM grade (iron meteorites) | 10-100 ppm | Modest but bulk-metallic |
| Accessible C-type NEOs | ~10-50 known (delta-v < 5 km/s) | Grows with survey |

## Operating Modes

| Mode | Activity | Autonomy Level | Duration |
|------|----------|----------------|----------|
| Approach | Rendezvous and match orbit | Fully autonomous | Days-weeks |
| Survey | Mapping, spectral sampling | Autonomous + uplink goals | Weeks-months |
| Anchor | Harpoon/clamp to surface | Autonomous | Hours |
| Excavate | Cut/scoop regolith | Autonomous, supervised | Continuous |
| Process | Heat, separate, store | Autonomous | Continuous |
| Depart | Release, transfer to depot | Autonomous | Days-months |

Each transition between modes is guarded by automated health checks: the spacecraft will not commit to excavation until anchoring telemetry confirms a stable grip, and will not begin thermal processing until the retort seal is verified. If any check fails, the system falls back to a safe hold and awaits ground review — a pattern inherited from [spacecraft systems](../spacecraft-systems/) fault-protection practice.

## See Also

- [Asteroid Prospecting](./asteroid-mining.prospecting.md) — spectral survey and NIR characterization
- [Extraction Methods](./asteroid-mining.extraction-methods.md) — thermal, magnetic, chemical recovery
- [Water Extraction](./asteroid-mining.water-extraction-asteroid.md) — hydration recovery from carbonaceous chondrites
- [Microgravity Manufacturing](./microgravity-manufacturing.md) — orbital production using extracted materials
- [Mining](../mining/) — terrestrial mining discipline (tool dependency)
- [Automation](../automation/) — autonomous robotic operations (tool dependency)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md)*
