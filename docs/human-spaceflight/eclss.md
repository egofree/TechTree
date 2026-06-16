# Environmental Control & Life Support

> **Node ID**: human-spaceflight.eclss
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `chemistry`, `gas-handling`, `water`, `energy.fuel-cell`, `ehs.radiation-safety`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eclss_systems, water_recovery_systems
> **Critical**: Yes

The Environmental Control and Life Support System (ECLSS) is the aggregate subsystem that keeps a crew alive inside a pressurised spacecraft. It is the difference between a tin can in vacuum and a shirtsleeve habitat. Every breath of oxygen, every sip of water, every watt of metabolic heat that is not removed, every trace of CO2 that accumulates above 0.7 kPa, is ultimately the ECLSS's responsibility. In a sealed spacecraft the crew and the cabin form a closed thermodynamic system: mass in must equal mass out, energy in must equal energy rejected, or the crew dies.

This article covers ECLSS across five process areas: [atmosphere management](./eclss.atmosphere-management.md) (pressure, O2, CO2, trace contaminants), [thermal and humidity control](./eclss.thermal-humidity-control.md) (cabin temperature, condensate removal), [water recovery](./eclss.water-recovery.md) (urine and condensate to potable water), [waste management](./eclss.waste-management.md) (fecal collection, stabilisation, containment), and [fire detection and suppression](./eclss.fire-detection-suppression.md) (smoke detection, CO2/water-mist extinguishers). Together they recreate, in a few cubic metres of pressure vessel, the ecosystem services that on Earth are provided free by an entire planet.

## Overview

The fundamental design reference for ECLSS is the human metabolic load. A crew member at rest consumes roughly 0.84 kg of oxygen per day and produces about 1.0 kg of CO2, 1.5 kg of water vapour (through respiration and perspiration), 0.11-0.15 kg of feces, and 1.0-1.5 kg of urine. Metabolic heat output averages 80-120 W per person. These are the inputs the ECLSS must continuously absorb, transform, and reject for the duration of the mission.

### Per-Crew Daily Mass Balance

| Substance | Consumed (kg/day) | Produced (kg/day) | Notes |
|-----------|-------------------|-------------------|-------|
| O2 | 0.84 | — | Inspired; metabolic oxidation |
| CO2 | — | 1.00 | Exhaled; ~28% recovered via Sabatier |
| Water (potable) | 2.2-3.0 | — | Drinking + food rehydration |
| Water (urine) | — | 1.0-1.5 | Reclaimable at ~85-93% |
| Water (condensate) | — | 1.2-2.0 | From humidity control |
| Feces | — | 0.11-0.15 | Dried, stored, or processed |
| Food (dry) | 0.5-0.7 | — | Respiration O2 source |
| Metabolic heat | — | 80-120 W | Removed by coolant loops |

For a 6-crew, 180-day mission this aggregates to roughly 900 kg of O2, 1,080 kg of CO2 to remove, and 2,400-3,200 kg of water to recover. Carrying all consumables open-loop — as Mercury, Gemini, and Apollo did — is feasible for short missions but prohibitive for long-duration spaceflight. The ISS targets approximately 85% overall mass loop closure, with the Water Recovery System alone achieving 93% closure and reclaiming about 6,000 kg of water per year.

### Mass Balance Diagram

```
              Oxygen  ──►  Crew  ──►  CO2  ──►  CDRA  ──►  Sabatier  ──►  H2O
               ▲                                       │                  │
               │                                       │                  │
              OGS ◄───────────────────────────────────┘                  │
               │                                                          │
              H2O ◄──────────────────────────────────────────────────────┘
               ▲
               │
   Water Recovery  ◄──  Urine + Condensate + Hygiene
```

## Cabin Atmosphere Specification

The reference habitat atmosphere is modelled on sea-level air but slightly relaxed to reduce structural pressure loads and leak rates.

| Parameter | Sea-level reference | ISS operating range | Hazard threshold |
|-----------|--------------------|--------------------|------------------|
| Total pressure | 101.3 kPa | 97.9-102.7 kPa | < 70 kPa hypoxia |
| O2 partial pressure (pO2) | 21.0 kPa | 19.5-23.1 kPa | < 16 kPa / > 32 kPa |
| CO2 partial pressure (pCO2) | 0.04 kPa | < 0.7 kPa (daily mean) | > 2.0 kPa toxic |
| N2 partial pressure | 79.1 kPa | balance | — |
| Temperature | 22°C | 18-27°C | > 32°C / < 16°C |
| Relative humidity | 50% | 25-75% | < 20% / > 80% |
| Ventilation velocity | — | 0.05-0.5 m/s | stagnant zones > 5 min |

The 19.5-23.1 kPa oxygen band is the fire-safety and hypoxia envelope: below 16 kPa the crew suffers altitude sickness, and above 32 kPa materials become dangerously flammable. CO2 is the most tightly constrained metabolic product — symptoms of hypercapnia (headache, lethargy, impaired judgement) appear above 2 kPa, and the ISS nominal target of 0.4-0.7 kPa reflects a hard operational ceiling.

## Atmosphere Management

### Cabin Pressure Control

Total cabin pressure is maintained by a Pressure Control Assembly (PCA) that meters gaseous nitrogen from high-pressure tanks (typically 20-30 MPa storage, 0.6 m³ internal volume) into the cabin to offset leaks and O2 consumption. The leak rate on a large space station is 0.1-0.5 kg/day total — small in absolute terms but requiring continuous makeup. N2 is chosen as the ballast gas because it is inert, suppresses flammability, and dilutes O2 to a fire-safe partial pressure.

Oxygen is metered separately by the Oxygen Partial Pressure Controller, which tops up the cabin whenever pO2 falls below 20.7 kPa. On the ISS, O2 is supplied either from compressed gas tanks delivered by resupply vehicles, or generated in-situ by the OGS electrolyser — both routes feed a common distribution manifold at 0.7-1.0 MPa.

### Oxygen Generation

The ISS Oxygen Generation System (OGS) electrolyses water to produce O2, consuming roughly 0.84 kg of water per kg O2 generated. For a nominal 6-crew load the OGS must produce up to 5.4 kg of O2 per day (0.84 kg × 6 crew + 10% margin), drawing 3-5 kW of electrical power.

The electrochemical reaction is:

```
2 H2O  →  2 H2 + O2  (electrolysis, ΔG = +237 kJ/mol)
```

The hydrogen byproduct is vented overboard or, in the Sabatier reactor, reacted with waste CO2 to recover water and methane:

```
CO2 + 4 H2  →  CH4 + 2 H2O  (Sabatier, 300-400°C, Ni/Ru catalyst)
```

This Sabatier step recovers roughly 50% of the hydrogen mass as water, which is then re-electrolysed. Full closure is impossible with Sabatier alone because methane exits the loop carrying four hydrogen atoms; a plasma pyrolysis or Bosch reactor would be needed for true 100% carbon closure.

### Carbon Dioxide Removal

CO2 removal has evolved through three technological generations:

| Technology | Mechanism | Capacity | Regenerable | Used on |
|-----------|-----------|----------|-------------|---------|
| LiOH canister | 2 LiOH + CO2 → Li2CO3 + H2O | 0.92 kg CO2 / kg LiOH | No | Mercury, Gemini, Apollo, Shuttle |
| 4-Bed Molecular Sieve (4BMS) | Zeolite adsorption/desorption | 0.12 kg CO2/hr per bed | Yes (vacuum desorb) | ISS (early) |
| CDRA | Twin 4BMS + air save | 0.18 kg CO2/hr | Yes | ISS (current) |

A single LiOH canister on the Space Shuttle scrubbed roughly 2.0 kg of CO2 over a 12-hour shift for a 7-crew cabin. LiOH is non-regenerable: every kilogram of CO2 removed permanently consumes 1.1 kg of LiOH, which must be launched and stowed as trash. For long missions this becomes the dominant logistics mass.

The CDRA (Carbon Dioxide Removal Assembly) on the ISS uses paired zeolite beds that cycle between adsorption (cabin air at 101 kPa) and desorption (vacuum of space at < 0.1 kPa). Each cycle removes approximately 0.18 kg CO2 per hour at a power cost of 200-400 W, with no consumable mass — only electricity. The trade is mass-on-orbit versus power and complexity.

### Trace Contaminant Control

Cabin air accumulates 200-400 trace contaminants from offgassing polymers, crew metabolism, cleaning agents, and experiment payloads. Activated charcoal beds (typically 5-15 kg of Barnebey-Sutcliffe type) adsorb volatile organics; ambient-temperature catalytic oxidisers (ATCO) convert carbon monoxide and light hydrocarbons to CO2 and H2O. A typical trace contaminant control assembly processes 5-15 m³/h of cabin air with a 1-2 year charcoal bed lifetime.

#### Example Trace Contaminant Limits (SMAC, 7-day)

| Contaminant | Source | 7-day SMAC (mg/m³) | Removal method |
|-------------|--------|---------------------|----------------|
| Carbon monoxide | Pyrolysis, smoking | 17 | Catalytic oxidiser |
| Ammonia | Metabolic, cleaning | 30 | Acid-impregnated charcoal |
| Formaldehyde | Polymer offgassing | 0.4 | Activated charcoal |
| Methanol | Wipes, experiments | 19 | Activated charcoal |
| Freon-11 | Refrigerant leak | 100 | None (monitor) |
| Acetone | Cleaning, biology | 18 | Activated charcoal |

SMAC (Spacecraft Maximum Allowable Concentration) values are published by NASA for 1-hour, 24-hour, 7-day, 30-day, and 180-day exposure windows; longer exposures permit progressively lower concentrations because of cumulative toxicity.

## Thermal & Humidity Control

Cabin heat and humidity are removed by a condensing heat exchanger that cools cabin air below its dew point, condensing water vapour onto hydrophilic coatings. The condensate is wicked into a water separator and routed to the Water Recovery System. Cabin air enters the heat exchanger at 22-27°C and leaves at 10-14°C; sensible and latent heat removal together total 150-350 W per crew member plus equipment dissipation.

The internal coolant loop is water (freezing-point inhibited by additives to -5°C), which transfers heat through an interface heat exchanger to the spacecraft's external ammonia loop, and thence to radiators that reject heat to deep space. Each crew member's Liquid Cooling and Ventilation Garment (LCVG) can remove up to 750 W of metabolic heat during exercise by circulating 80-100 kg/h of chilled water through capillary tubes woven into the suit undergarment.

### Humidity Control Operating Points

| Parameter | Nominal | Tolerance | Action if exceeded |
|-----------|---------|-----------|-------------------|
| Cabin dew point | 9-12°C | ±2°C | Increase coolant flow |
| Relative humidity | 45% | 25-75% | Adjust CHX bypass |
| Condensate rate | 1.5-3.0 kg/day per crew | — | Verify separator |
| Coolant inlet temp | 4-7°C | ±1°C | Modulate three-way valve |
| Cabin air flow at CHX | 100-150 m³/h | — | Verify fan speed |

When relative humidity exceeds 75% for more than 30 minutes, condensation forms on cold electronic surfaces and creates electrical short-circuit hazards. When RH drops below 25%, crew report dry eyes, static-electricity shocks, and dust irritation.

## Water Recovery

The ISS Water Recovery System (WRS) is the centrepiece of closed-loop ECLSS. It processes two waste streams: urine and humidity condensate.

| Stream | Source | Volume (kg/day, 6 crew) | Reclamation rate |
|--------|--------|------------------------|------------------|
| Urine | Waste Management Facility | 6-9 | ~85% (15% brine purge) |
| Condensate | Cabin heat exchanger | 7-12 | ~99% |
| Total | Both | 13-21 | 93% loop closure |
| Annual | — | ~6,000 kg/year | — |

The WRS process train is:

1. **Waste Water Tank** — collect urine, flush water, condensate
2. **Particulate Filter** — 0.5 µm nominal, removes hair, fibre, precipitate
3. **Multifiltration Beds** — ion-exchange resins and activated carbon remove organics, ammonia, heavy metals
4. **Volatile Removal Assembly** — catalytic oxidiser at 130°C oxidises low-molecular-weight organics
5. **Ion Exchange Bed** — final polish to potable mineral content
6. **Microbial Check Valve** — iodine dosing at 0.5-2.0 mg/L residual

Product water meets EPA and WHO potable standards, with total organic carbon below 0.5 mg/L and microbial counts below 1 CFU/100 mL. The WRS achieves roughly 6,000 kg of water reclaimed per year, eliminating the need for 6 Progress resupply flights that would otherwise be required for water logistics alone.

### Multifiltration Bed Media

Each multifiltration (MF) bed is a sequential column of media tailored to specific contaminant classes:

| Layer | Media | Target contaminant | Capacity (kg contaminant/kg media) |
|-------|-------|--------------------|------------------------------------|
| 1 | 5-µm prefilter | Particulate | — |
| 2 | Activated carbon (coconut) | Non-polar organics | 0.05-0.20 |
| 3 | Weak-acid cation resin | Divalent cations (Ca, Mg) | 0.10-0.15 |
| 4 | Strong-base anion resin | Anions (Cl, SO4, NO3) | 0.08-0.12 |
| 5 | Phosphoric-acid carbon | Polar organics, ammonia | 0.03-0.08 |
| 6 | Mixed-bed polish | Final ionic polish | 0.02-0.04 |

Bed replacement is on a fixed schedule (typically 30-90 days) or on a conductivity breakthrough alarm from the product-water sensor. Spent beds are returned to Earth for regeneration analysis.

### Closed-Loop vs Open-Loop

| Architecture | Water closure | O2 closure | Resupply mass (180-day, 6-crew) | Used on |
|--------------|---------------|-----------|--------------------------------|---------|
| Open-loop (stored) | 0% | 0% | 5,400 kg | Mercury, Gemini |
| Partial closure (LiOH + WRS) | 93% | 0% | 2,400 kg | Shuttle (WRS on ISS only) |
| Partial closure (OGS + CDRA + WRS) | 93% | ~85% | 800 kg | ISS (current) |
| Full closure (Bosch + advanced WRS) | ~98% | ~98% | 150 kg | Design target, not flown |

The ISS targets approximately 85% overall mass closure with current hardware. Closing the last 15% requires the Bosch reaction (CO2 + 2 H2 → C + 2 H2O, depositing solid carbon) and brine-drying hardware to recover the 15% water currently lost as urine brine — neither has been flown at operational scale.

## Waste Management

Each crew member produces 0.11-0.15 kg of feces and 1.0-1.5 kg of urine per day. The Waste Management Facility (WMF) on ISS uses a vacuum toilet that air-entrains waste into a storage bag, with urine separated by a centrifugal fan separator and routed to the WRS. Fecal waste is vacuum-dried, bagged, and stored in a containment canister for eventual disposal — historically loaded into a cargo vehicle (Cygnus, Progress) and burnt up on atmospheric reentry.

Trash — food packaging, used clothing, experiment waste — accumulates at roughly 1.0-1.5 kg per crew-day. Compaction reduces volume by a factor of 3-5; some trash is loaded into the cargo vehicle for destructive reentry, while a portion is returned to Earth for analysis. Long-duration missions beyond LEO will require in-situ waste processing (incineration, pyrolysis, or bio-stabilisation) because the trash cannot be simply de-orbited.

### Waste Output Breakdown (per crew-day)

| Stream | Mass (kg) | Volume (L) | Disposition |
|--------|-----------|------------|-------------|
| Urine | 1.0-1.5 | 1.0-1.5 | WRS processing |
| Feces | 0.11-0.15 | 0.10-0.15 | Dried, bagged, stored |
| Food packaging | 0.4-0.8 | 4-8 | Compacted, stored |
| Used clothing | 0.2-0.4 (variable) | 1-3 | Stored or reentered |
| Hygiene wipes | 0.1-0.2 | 0.5-1.0 | Stored, returned |
| Experiment waste | variable | variable | Returned or reentered |

## Fire Detection & Suppression

A spacecraft fire in microgravity behaves fundamentally differently from a terrestrial fire. Without buoyant convection, flames are spherical, spread slower along solid surfaces (1-10 mm/s versus 10-100 mm/s on Earth), but produce more soot and CO. Oxygen diffuses to the flame only by molecular diffusion and the cabin ventilation system — if ventilation is off, the flame self-extinguishes within seconds in its own combustion products.

| Element | Type | Detection / agent | Coverage |
|---------|------|-------------------|----------|
| Smoke detector | Photoelectric + ionisation | 0.003-0.3 µm smoke particulate | Cabin + racks |
| Portable extinguisher | CO2 (2.7 kg) | Smothering + cooling | Handheld, 1 per module |
| Fixed extinguisher | Water mist (H2O fog) | 5-10 µm droplets in N2 | Behind racks |
| Post-fire cleanup | Contaminant cleanup kit | Replacement LiOH + charcoal | Atmosphere scrub |

The ISS carries portable CO2 extinguishers in each module, plus a water-mist system behind equipment racks where smouldering fires are most likely. After any fire event, the cabin atmosphere is scrubbed through fresh LiOH and charcoal beds and particulate filters are replaced.

### Microgravity Flame Behaviour

- **Shape**: Spherical (no upward buoyancy → no teardrop flame)
- **Spread rate along solid fuel**: 1-10 mm/s (Earth: 10-100 mm/s)
- **Soot production**: 2-3× higher than 1g flames (longer residence time)
- **Self-extinguishment**: Yes, in stagnant air within 10-30 seconds
- **Ventilation effect**: Critical — forced flow > 5 cm/s sustains flame; < 1 cm/s extinguishes

This is why spacecraft smoke detectors are placed in the ventilation return ducts (where smoke is transported) rather than at the ceiling (where smoke never accumulates, because there is no buoyancy to lift it).

## Mass and Power Budget

A complete ECLSS for a 6-crew, 90-day mission has a typical dry mass and steady-state power envelope as follows:

| Subsystem | Dry mass (kg) | Power (W) | Consumable mass (kg/90 d) |
|-----------|---------------|-----------|---------------------------|
| Atmosphere (OGS + CDRA + charcoal) | 1,500 | 4,000 | 50 (charcoal, LiOH margin) |
| Thermal & humidity | 800 | 600 | 0 |
| Water recovery | 1,200 | 800 | 100 (filter beds) |
| Waste management | 350 | 200 | 200 (bags, liners) |
| Fire detection & suppression | 120 | 50 | 30 (extinguisher charge) |
| **Total** | **3,970** | **5,650** | **380** |

For a Mars-class mission (180-day transit, 500-day surface, 180-day return, 6 crew), open-loop water and oxygen alone would require 30+ tonnes of consumables — closing the loop with ECLSS reduces that to under 1 tonne of filter beds and spare parts, at the cost of ~4 tonnes of ECLSS hardware.

## Troubleshooting

| Symptom | Likely cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| pCO2 rising | CDRA bed saturated or heater failed | Check cycle temps; CO2 breakthrough curve | Swap to redundant CDRA |
| pO2 dropping | OGS cell-stack voltage drift | Inspect current/voltage curve | Replace deioniser bed |
| Cabin humidity high | CHX coolant bypass stuck open | Verify valve position, coolant temp | Manual valve override |
| Product water TOC spike | MF bed breakthrough | Sample at VRA inlet | Replace MF bed early |
| Smoke detector false trips | Dust or fibre in optics | Inspect detector chamber | Clean or replace unit |
| Urine separator low flow | Inline filter clogged | Pressure differential | Replace prefilter |

## Glossary

- **ECLSS**: Environmental Control and Life Support System — the aggregate subsystem maintaining a habitable cabin environment
- **OGS**: Oxygen Generation System — water electrolysis unit producing O2 for cabin makeup
- **CDRA**: Carbon Dioxide Removal Assembly — regenerable zeolite-bed CO2 scrubber on the ISS
- **4BMS**: Four-Bed Molecular Sieve — zeolite adsorption/desorption CO2 removal technology
- **Sabatier**: CO2 + 4 H2 → CH4 + 2 H2O — catalytic reaction recovering water from waste CO2 and H2
- **Bosch**: CO2 + 2 H2 → C + 2 H2O — full-closure alternative to Sabatier, deposits solid carbon
- **WRS**: Water Recovery System — ISS subsystem reclaiming potable water from urine and condensate
- **PCA**: Pressure Control Assembly — meters N2 to maintain total cabin pressure
- **CHX**: Condensing Heat Exchanger — removes sensible and latent heat from cabin air
- **LCVG**: Liquid Cooling and Ventilation Garment — undergarment removing metabolic heat from a crew member
- **MF bed**: Multifiltration bed — layered ion-exchange and activated-carbon column polishing recovered water
- **VRA**: Volatile Removal Assembly — catalytic oxidiser polishing trace organics from recovered water
- **WMF**: Waste Management Facility — toilet and waste collection assembly
- **SMAC**: Spacecraft Maximum Allowable Concentration — NASA-published contaminant exposure limits
