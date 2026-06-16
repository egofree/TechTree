# Mars ISRU

> **Node ID**: `space-resources.mars-isru`
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md),
> [`gas-handling`](../gas-handling/index.md),
> [`mining`](../mining/index.md),
> [`energy.electricity`](../energy/electricity.md)
> **Enables**: None
> **Timeline**: Years 80+
> **Outputs**: mars_propellant
> **Critical**: No

Mars In-Situ Resource Utilization (ISRU) manufactures rocket propellant — methane and liquid oxygen — from the Martian atmosphere and mined water ice, so that a return vehicle need not carry its ascent propellant from Earth. This single capability cuts the launched-from-Earth mass of a Mars sample-return or crewed-return mission by roughly an order of magnitude: instead of landing a 30+ metric ton fueled ascent vehicle, the mission lands an empty (~3 ton) tank and a ~2 ton ISRU plant, then fills the tank over 14–26 months using only Martian resources. The concept was validated at miniature scale by the **MOXIE** instrument on the Perseverance rover (2021), which produced ~10 grams of oxygen per hour from atmospheric CO₂.

## Mars Atmosphere Composition

The Martian atmosphere is thin (surface pressure 6–10 mbar, less than 1% of Earth's) but remarkably uniform in composition, making it an accessible feedstock that requires no mining — only pumping and compression.

| Component | Volume % | Notes |
|-----------|----------|-------|
| **CO₂** | **95.3%** | Primary ISRU feedstock |
| N₂ | 2.7% | Inert; potential buffer gas for life support |
| Ar | 1.6% | Inert |
| O₂ | 0.13% | Trace; not directly harvestable |
| CO | 0.08% | Trace |
| H₂O | 0.03% (variable) | Seasonal; not a viable water source |
| Dust | variable | Global dust storms (every 5–6 years) foul intakes |

The 95.3% CO₂ content means the atmosphere is almost pure carbon dioxide — but at only 6–10 mbar, a liter of Martian "air" contains only ~10–20 milligrams of CO₂. Any ISRU process must therefore begin by **compressing the atmosphere by roughly 100×** (to ~1 bar) before chemical processing is practical.

## Atmosphere Collection and Compression

### Sorption Pumps

The baseline Mars atmosphere collection approach uses **temperature-swing sorption pumps**: beds of zeolite (13X) or amorphous silica adsorbent that capture CO₂ from the passing atmosphere at night (cold, ~-70°C overnight), then release it when heated during the day (warm, ~+20°C). Because adsorption is exothermic and the Martian night is cold, the bed fills passively; daytime heating (by solar or waste heat) drives off concentrated CO₂ at near-atmospheric pressure, which a mechanical compressor then pressurizes to the 1–30 bar required by downstream reactors.

### Mechanical Compression

Sorption pump output is boosted to reactor pressure by a **multi-stage compressor**: typically a diaphragm or scroll compressor (oil-free, to avoid contaminating catalysts) taking 10–100 mbar inlet and delivering 1–30 bar outlet. Dust filtration is mandatory — global dust storms suspend sub-micron dust that would destroy compressor bearings and poison catalysts. Filters are back-flushed with CO₂ during off-cycle periods.

## MOXIE and Solid-Oxide Electrolysis

The **Mars Oxygen In-Situ Resource Utilization Experiment (MOXIE)**, flown on the Perseverance rover, demonstrated the core oxygen-production reaction: **solid oxide electrolysis of CO₂**.

### The SOXE Reaction

> 2CO₂ → 2CO + O₂    (electrolysis at 800°C)

In the solid oxide electrolysis cell (SOXE), CO₂ at ~800°C passes over a yttria-stabilized zirconia (YSZ) ceramic electrolyte. Under an applied voltage (~1.0–1.5 V per cell), oxide ions (O²⁻) migrate through the electrolyte and combine at the anode to form O₂ gas. At the cathode, CO₂ is reduced to CO, releasing the oxide ion.

### MOXIE Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| O₂ production rate | ~10 g/hr | Demo scale; ~122 g total over 16 runs |
| O₂ purity | > 98% | Separated from CO byproduct |
| Operating temperature | 800°C | SOXE stack |
| Electrolyte | Scandia-stabilized zirconia (ScSZ) | Higher conductivity than YSZ |
| Cell voltage | 0.8–1.2 V | ~80% thermoneutral efficiency |
| Power input | ~300 W | For ~10 g/hr O₂ |
| Mass | 17.1 kg | Including compressor and controls |

MOXIE's ~10 g/hr rate is a demonstration scale. A full crewed ascent mission needs ~25–30 metric tons of O₂ — requiring a plant ~2,500× larger than MOXIE, or roughly 25–30 kW of continuous SOXE power. The technology scales linearly by stacking cells; the engineering challenge is lifetime (the ceramic cells degrade via chromium poisoning and thermal cycling).

### CO Byproduct

Solid-oxide electrolysis co-produces **carbon monoxide (CO)** at a 2:1 molar ratio to O₂. The CO is a waste stream in pure oxygen production but a feedstock for Sabatier methanation (combined with hydrogen) or for metal reduction. A full ISRU plant captures the CO rather than venting it.

## Sabatier Methanation

The **Sabatier reaction** converts CO₂ and hydrogen into methane and water, producing the fuel half of the propellant pair:

> CO₂ + 4H₂ → CH₄ + 2H₂O    (ΔH = -165 kJ/mol, exothermic, 300–400°C)

### Reactor Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Catalyst | Ruthenium on alumina (Ru/Al₂O₃) | Ni also works but Ru is more active |
| Temperature | 300–400°C | Higher T shifts equilibrium to reactants |
| Pressure | 1–30 bar | Higher pressure favors products (4 → 3 moles gas) |
| H₂:CO₂ feed ratio | 5:1 | Stoichiometric is 4:1; excess H₂ prevents coking |
| Per-pass CO₂ conversion | > 98% | Near-equilibrium at 300°C |
| Methane selectivity | > 99% | Minor CO byproduct from reverse water-gas shift |

The reaction is **exothermic** — it releases heat — so the reactor is self-sustaining once started and must be cooled, not heated, during steady operation. A small electric heater is needed only for cold-start.

### The 5:1 Hydrogen Requirement

The Sabatier reaction consumes **4 moles of H₂ per mole of CO₂** (stoichiometric), but practical reactors run at a **5:1 H₂:CO₂ ratio** to suppress carbon formation (coking) on the catalyst and to drive conversion. The excess hydrogen is recovered from the product stream (via membrane separation or cryogenic condensation of methane) and recycled. The net hydrogen consumption is set by the stoichiometry: producing 1 metric ton of CH₄ requires ~0.50 ton of H₂ (or ~4.5 tons of H₂O, after electrolysis).

### Water Electrolysis — Closing the Loop

The Sabatier water byproduct is electrolyzed back into hydrogen and oxygen:

> 2H₂O → 2H₂ + O₂    (electrolysis)
>
> Net (Sabatier + electrolysis): CO₂ + (recycled H₂) → CH₄ + 2O₂

This means **half the oxygen produced comes "for free"** from the water electrolysis that recycles the Sabatier hydrogen. The hydrogen is not consumed — it acts as a chemical carrier — but make-up hydrogen (from mined water ice) is required to offset losses.

## Propellant Production — The ISPP Plant

The integrated **In-Situ Propellant Production (ISPP)** plant combines atmosphere collection, electrolysis, Sabatier methanation, and cryogenic liquefaction into a single propellant factory.

### Mass Balance

To produce 1 metric ton of methane requires:

| Input | Quantity | Source |
|-------|----------|--------|
| CO₂ | 2.75 metric tons | Martian atmosphere (compressed) |
| H₂O | 2.25 metric tons | Mined water ice (electrolyzed to H₂ + O₂) |
| H₂ (make-up) | ~0.25 metric tons | From water electrolysis |

The canonical scaling figure — **1 metric ton of CH₄ per 17.7 metric tons of H₂O and atmospheric CO₂** — reflects the total mass of feedstock required when accounting for all stoichiometry, recovery inefficiencies, and the co-produced oxygen.

### Per-Sol Production Target

A crewed Mars ascent vehicle needs roughly **7 metric tons of CH₄ and 5.5 metric tons of O₂** as a minimum (a larger, fully fueled vehicle may need 7 t CH₄ + 22–25 t O₂ for a methane-LOX ascent stage; the 5.5 t O₂ figure corresponds to a smaller demonstration or the oxygen produced as a byproduct of the Sabatier water loop). The ISPP plant must produce this over the ~500-Sol (Mars days) window between arrival and departure:

| Product | Target Mass | Production Rate (over 500 Sols) |
|---------|-------------|--------------------------------|
| CH₄ | 7 metric tons | ~14 kg/Sol (1 Sol = 24 h 39 min) |
| O₂ (net, after loop closure) | 5.5 metric tons | ~11 kg/Sol |
| Power required | — | 25–40 kWe continuous |

### ISPP Plant Architecture

A full ISPP plant consists of:

1. **Atmosphere intake** — dust-filtered CO₂ compressed to 1–30 bar by sorption pump + scroll compressor.
2. **SOXE electrolyzer** — converts part of the CO₂ to O₂ (product) and CO (recycled to Sabatier via reverse water-gas shift, or vented).
3. **Water ice miner** — extracts water from regolith (subsurface ice at 30–60°N/S, or polar), melts and purifies it.
4. **Water electrolyzer** — splits mined H₂O into H₂ (for Sabatier) and O₂ (product).
5. **Sabatier reactor** — converts CO₂ + H₂ → CH₄ + H₂O; water returned to electrolyzer.
6. **Cryocooler / liquefier** — liquefies CH₄ (-162°C) and O₂ (-183°C) for storage in the ascent vehicle tanks.
7. **Storage and transfer** — cryogenic dewars and transfer lines to the ascent vehicle.

## Mars Water Ice Resources

Unlike the Moon, where accessible water is confined to polar PSRs, Mars has widespread subsurface water ice across much of the mid- and high-latitudes. The **Phoenix lander** (2008) directly confirmed water ice a few centimeters below the surface at 68°N. Radar sounding (MARSIS, SHARAD) has mapped extensive ice deposits.

| Region | Ice Depth | Ice Content | Accessibility |
|--------|-----------|-------------|---------------|
| Mid-latitude (30–50°N/S) | 0.1–1 m | 20–60% by mass | Drill or scrape |
| Phoenix site (68°N) | < 10 cm | Near-pure ice | Direct excavation |
| Polar layered deposits | Surface | > 90% ice | High latitude, cold |

Water mining is a [mining](../mining/index.md) and [gas-handling](../gas-handling/index.md) problem: excavate icy regolith, warm it in a sealed reactor to sublime/melt the ice, capture the vapor, condense and purify the water, then feed it to the electrolyzer.

## Power for the ISPP Plant

The ISPP plant is the single largest continuous power consumer in a Mars surface campaign. A 25–40 kWe continuous load, sustained for 500+ Sols, dominates the surface power architecture.

### Power Options

| Source | Scale | Mars Constraint |
|--------|-------|-----------------|
| Solar (photovoltaic) | 5 kWe per ~100 m² array | Dust accumulation degrades output ~0.5%/Sol; global storms cut >90% |
| Fission surface power | 10 kWe–1 MWe | Operates independent of dust and season; baseline for crewed ISPP |
| Battery / electrolyzer storage | 10–100 kWh | Bridges day-night (12.3-hour) and short dust events; cannot bridge global storms |

A dust-tolerant solar array must be oversized by roughly 2–3× and fitted with automated dust-removal (electrostatic clearing or wiper). Even so, a global dust storm lasting weeks would halt a solar-only plant — making **fission surface power the reference baseline** for crewed-mission ISPP. The NASA Kilopower / Fission Surface Power (FSP) project targets 10–40 kWe scalable units that fit this role.

### Energy Cost of Propellant

Producing 7 metric tons of CH₄ + 5.5 tons of O₂ over 500 Sols consumes roughly 250,000–400,000 kWh total (the SOXE stack is the dominant draw at ~20–25 kWh/kg O₂, plus electrolysis at 55 kWh/kg H₂, plus cryocoolers). This is comparable to the energy needed to produce the same propellant on Earth — but delivered to the Martian surface, where every watt of power generation equipment itself had to be launched from Earth.

## Production Scale and Campaign Timing

A crewed Mars mission exploits the ~26-month Earth-Mars transfer window. The ISPP plant is delivered robotic-only on a preceding transfer window and has ~20 months (roughly 740 Sols) to fill the ascent vehicle tanks before the crew arrives. This pre-positioning is what makes ISRU feasible: the plant operates uncrewed for over a Martian year, then the crew lands near the already-fueled ascent vehicle.

### Campaign Timeline

| Phase | Duration | Activity |
|-------|----------|----------|
| Pre-positioning | Transfer + landing | ISPP plant, empty ascent vehicle delivered |
| Autonomous production | ~500–740 Sols | ISPP fills CH₄ + LOX tanks uncrewed |
| Crew arrival | Landing | Crew verifies tank fill, performs checkout |
| Surface operations | ~500 Sols | Continued top-off; ISPP supports surface mobility fuel |
| Ascent | Launch day | Crew launches in fully fueled vehicle |

If the ISPP plant fails after the crew arrives but before ascent, the crew has no return — making ISPP reliability a crew-survival requirement. This drives the plant toward **redundancy**: two or more parallel trains, either of which can fill the tanks within the available window.

## Comparison with Lunar ISRU

| Dimension | Lunar ISRU | Mars ISRU |
|-----------|-----------|-----------|
| Primary feedstock | Regolith (solid) | Atmosphere (CO₂ gas) + water ice |
| Headline product | Oxygen (O₂) | Methane + oxygen (CH₄/LOX) |
| Key reaction | Molten electrolysis, ilmenite reduction | Sabatier, solid-oxide electrolysis |
| Reactor temperature | 1000–1600°C | 300–800°C |
| Water source | PSR ice (-240°C) | Subsurface ice (-50 to -20°C) |
| Night duration | 354 hours (non-polar) | 12.3 hours (continuous cycle) |
| Dust hazard | Abrasive, electrostatic | Fine, global storms |
| Power source | Polar solar or fission | Fission baseline (storm-tolerant) |

## Integration Points

| Stage | Contribution |
|-------|-------------|
| Chemistry | Sabatier catalysis, electrolysis, gas separation — the chemical heart of ISPP |
| Gas Handling | CO₂ compression, H₂ storage, cryogenic liquefaction — all gas-processing heritage |
| Mining | Water ice excavation, regolith handling, drill-and-scrape architectures |
| Energy (electricity) | 25–40 kWe continuous for SOXE, electrolysis, and cryocoolers |

## Safety

- **CO toxicity**: Carbon monoxide is the major byproduct of solid-oxide CO₂ electrolysis. CO is odorless and lethal at 400 ppm over 1 hour. All SOXE reactors must be vented to the Martian atmosphere (not the habitat) and monitored with electrochemical CO sensors.
- **Hydrogen flammability**: H₂ leaks in the Sabatier loop are flammable over 4–75% in air. The ISPP plant operates in a sealed module with H₂ leak detectors and inert-purge capability.
- **Cryogenic hazards**: LOX at -183°C and liquid CH₄ at -162°C cause cryogenic burns and, on mixing, form a detonable gel. Storage tanks are double-walled vacuum vessels with pressure relief.
- **Dust storms**: Global dust storms (occurring every ~5 Mars years) reduce solar power by >90% for weeks. A solar-only ISPP plant must be oversized or backed by nuclear power to ride out a storm season.

## Key Deliverables

- Sorption pump + scroll compressor delivering 1–30 bar CO₂ at kg/hr scale
- Solid-oxide electrolyzer stack producing >25 kg O₂/hr (full scale) at 800°C
- Sabatier reactor converting CO₂ + H₂ to CH₄ at >98% per pass over Ru/Al₂O₃
- Water electrolyzer closing the hydrogen loop (PEM or alkaline, 50–65 kWh/kg H₂)
- Cryogenic liquefier producing liquid CH₄ (-162°C) and LOX (-183°C)
- 25–40 kWe continuous power source (fission surface power or large solar + storage)
- Water ice miner extracting and purifying >2 metric tons of H₂O per campaign

## Limitations

- **Atmosphere is thin**: 6–10 mbar means 100× compression just to reach 1 bar — a significant energy and mechanical cost before any chemistry begins.
- **Hydrogen scarcity**: All methane production ultimately depends on mined water ice for hydrogen. A water-poor landing site cripples the ISRU plant.
- **SOXE lifetime**: Solid-oxide cells degrade via chromium vapor transport and thermal cycling; >10,000-hour lifetime at 800°C is not yet demonstrated at scale.
- **Dust storm power loss**: Solar-powered ISPP plants lose >90% output during global storms, halting production for weeks.
- **Cryogenic boil-off**: Stored LOX and CH₄ boil off at 0.1–1.0%/day on Mars (warmer than lunar night). The ISPP plant must over-produce to fill tanks before launch, accounting for losses.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| SOXE O₂ output dropping | Cell degradation (Cr poisoning) or cracked electrolyte | Increase cell voltage to maintain current; if ineffective, isolate and bypass failed cells; replace stack |
| Sabatier CO₂ conversion < 90% | Catalyst coking or excess CO₂ in feed (H₂:CO₂ < 5:1) | Increase H₂ feed ratio to 5:1; regenerate catalyst by H₂ purge at 400°C; check for cold spots |
| Compressor CO₂ flow reduced | Dust filter fouled or sorption bed saturated | Back-flush dust filter with CO₂; regenerate sorption bed by heating to +80°C |
| Water electrolyzer degraded | Mineral deposits on electrodes (impure feed water) | Run feed water through de-ionizer; acid-wash electrodes; replace if resistance remains high |
| Cryocooler can't reach -183°C | Condenser fouled or refrigerant leak | Inspect condenser for CO₂ frost; check refrigerant charge; verify vacuum jacket integrity |

## See Also

- [Chemistry](../chemistry/index.md) — catalysis, electrolysis, and gas-phase reaction fundamentals
- [Gas Handling](../gas-handling/index.md) — compression, storage, and cryogenic liquefaction heritage
- [Mining](../mining/index.md) — water ice excavation and regolith handling
- [Electricity Generation & Distribution](../energy/electricity.md) — continuous power for the ISPP plant
- [Atmosphere Collection](mars-isru.atmosphere-collection.md) — CO₂ sorption and MOXIE-class electrolysis
- [Sabatier Methanation](mars-isru.sabatier-methanation.md) — CO₂ + H₂ → CH₄ over Ru catalyst
- [Propellant Production (Mars)](mars-isru.propellant-production-mars.md) — integrated ISPP plant
- [Lunar ISRU](lunar-isru.md) — regolith and PSR water ice utilization
- [Propellant Production](../launch-vehicles/propellant-production.md) — terrestrial/cryogenic propellant heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Resources](./index.md) • [Mars ISRU](mars-isru.md)*
