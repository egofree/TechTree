# Space Recycling & Closed-Loop Logistics

> **Node ID**: space-resources.space-recycling
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: `human-spaceflight.eclss`, `chemistry`, `polymers`, `metals`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 80-200+
> **Outputs**: recycled_materials
> **Critical**: No

The Earth is, from a crewed-spacecraft perspective, a closed-loop recycling system of staggering throughput. The atmosphere, the oceans, the soil, and the biosphere together recover nearly 100% of all metabolic and geological waste and return it as breathable oxygen, potable water, and edible biomass — powered by 1,361 W/m² of free solar energy and maintained by an ecosystem that took three billion years to debug. A spacecraft must reproduce this service inside a few hundred cubic metres of pressure vessel, with no landfill, no ocean to dump into, no atmosphere to vent to without loss, and a resupply cadence measured in months. Space recycling is the discipline of closing those loops.

This article covers closed-loop logistics across three process areas: [life support loop closure](./space-recycling.life-support-loop-closure.md) (biological and physical-chemical hybrid regeneration of air, water, and food), [material reprocessing](./space-recycling.material-reprocessing.md) (metal and polymer scrap recovery, solar melting, and cargo vehicle disposal), and [propellant recycling](./space-recycling.propellant-recycling.md) (venting capture, boil-off recovery, and residual gas reclamation). Together they define the mass budget that determines whether a crewed mission to Mars — or a permanent orbital settlement — is launch-feasible at all.

## Overview

The governing constraint of long-duration spaceflight is the mass balance. Every kilogram of consumables launched to low Earth orbit costs roughly $2,000-$54,000 per kg depending on the launcher, and orders of magnitude more to lunar or Martian orbit. A six-person crew on a 1,000-day Mars mission would, on a fully open loop (no recycling), require roughly:

| Consumable | Per crew per day | 6 crew × 1,000 days | Open-loop mass |
|------------|------------------|---------------------|----------------|
| Oxygen | 0.84 kg | 5,040 kg | 5,040 kg |
| Potable water | 2.5 kg | 15,000 kg | 15,000 kg |
| Food (dry) | 0.62 kg | 3,720 kg | 3,720 kg |
| Total metabolic | — | — | ~23,760 kg |

Add redundancy margins, packaging, and tankage and the open-loop consumable mass approaches 30-40 tonnes — before any hardware, propellant, or structure. This is why recycling is not an environmental nicety in space; it is the enabling technology. The ISS, with approximately 85% overall water loop closure and 93% recovery in the Water Recovery System, already saves roughly 6,000 kg of launched water per year. The ESA MELiSSA project targets 99% total loop closure — the threshold at which a Mars mission becomes mass-feasible with near-Earth resupply cadences.

### The Loop Closure Spectrum

| Recovery rate | Annual resupply (6 crew) | Mission enabled |
|--------------|--------------------------|-----------------|
| 0% (open loop) | ~24,000 kg consumables | LEO sortie, < 30 days |
| 50% (ISS early) | ~12,000 kg | ISS-class, continuous resupply |
| 85% (ISS current) | ~3,600 kg | LEO station, 6-month crew rotation |
| 93% (water only) | ~1,700 kg water | Lunar sortie feasibility |
| 99% (MELiSSA goal) | ~240 kg make-up | Mars transit, 1,000 days |

The asymptotic cost of closing the last 1% — from 99% to 100% — is generally considered prohibitive, because it requires recovering trace contaminants, refractory compounds, and unavoidable losses (atmospheric leak, adsorbed water, abrasion). The design target is therefore 99% closure with a small make-up mass launched annually, not perfect closure.

## Life Support Loop Closure

### The MELiSSA Architecture

The European Space Agency's Micro-Ecological Life Support System Alternative (MELiSSA) is the most developed bioregenerative loop closure concept. It is structured as an engineered ecosystem of five compartments, each performing a specific trophic function, modelled on a terrestrial lake ecosystem:

| Compartment | Function | Key Organisms | Input | Output |
|-------------|----------|---------------|-------|--------|
| C1: Waste | Anaerobic degradation | Thermophilic bacteria (e.g. *Clostridium*) | Fecal waste, inedible biomass | Volatile fatty acids, NH4+, CO2, H2 |
| C2: Nitrifying | Ammonia to nitrate | *Nitrosomonas*, *Nitrobacter* | NH4+ from C1 | NO3- (nitrate) |
| C3a: Photosynthetic (bacteria) | CO2 + H2 fixation | *Rhodospirillum rubrum* | CO2, fatty acids, NO3- | Biomass, O2 |
| C3b: Photosynthetic (algae) | O2 generation | *Chlorella*, *Arthrospira (Spirulina)* | CO2, light, NO3- | O2, edible biomass |
| C4: Consumer | Crew + higher plants | Humans, wheat, soy, rice | O2, food, water | CO2, waste, water vapour |

The loop is designed so that the output of C1 feeds C2, C2 feeds C3, C3 produces O2 and food for C4, and C4's waste returns to C1 — closing the carbon, nitrogen, and water cycles. The photosynthetic compartments (C3a, C3b) are driven by light, which in space is abundant and free: solar constant is 1,361 W/m² at 1 AU, of which photosynthetically active radiation (PAR, 400-700 nm) is roughly 45%.

### Algae Bioreactors

Algae are the workhorse of biological atmosphere revitalisation because their photosynthetic efficiency (3-6% of incident PAR) far exceeds higher plants (1-2%). The two principal species studied for space life support are *Chlorella vulgaris* and *Arthrospira platensis* (Spirulina):

| Parameter | *Chlorella vulgaris* | *Arthrospira platensis* |
|-----------|----------------------|-------------------------|
| O2 productivity | 500-600 g O2/m²/day | 400-800 g O2/m²/day |
| Protein content | 50-55% dry mass | 60-70% dry mass |
| Growth temperature | 25-35°C | 30-38°C |
| pH tolerance | 6.5-8.0 | 8.5-11.0 |
| Doubling time | 6-24 hours | 8-12 hours |

A single square metre of high-density algal bioreactor (50-100 g dry mass per litre culture density) can produce enough oxygen for roughly 0.5-0.7 crew members. For a six-person crew, 9-12 m² of illuminated algal surface area is sufficient to close the oxygen loop — compact enough to fit inside a single habitat module rack when configured as a flat-panel airlift reactor. The trade-off is that the system must be continuously illuminated and mixed, drawing 1-2 kW of parasitic power for pumps and lighting during eclipse periods.

### Higher Plant Chambers

Algae close the atmosphere loop but not the food loop — humans cannot subsist on Spirulina alone. Higher plants provide calorie density, dietary variety, and psychological benefit. The reference crops for bioregenerative life support are:

| Crop | Growing area (m²/person) | Yield | Photoperiod | Edible biomass |
|------|--------------------------|-------|-------------|----------------|
| Wheat | 5.5 | 1.5-2.5 kg/m²/cycle | 20 h light / 4 h dark | 40-50% of total |
| Soybean | 8-12 | 0.8-1.2 kg/m²/cycle | 12-16 h light | 35-40% |
| Rice | 6-10 | 1.0-1.8 kg/m²/cycle | 12 h light | 40-45% |
| Lettuce | 1-2 | 0.3-0.5 kg/m²/cycle | 16-18 h light | 80-90% |
| Potato | 8-12 | 2-4 kg/m²/cycle | 16-18 h light | 70-80% |

Wheat at 5.5 m² per person is the calorie benchmark: a wheat chamber for six crew needs roughly 33 m² of growing area, producing 50-80 kg of grain per 70-80 day cycle — enough for roughly 60% of caloric needs. Full diet closure (2,500-3,000 kcal/person/day) requires 40-60 m² per person of mixed crops, which is the dominant volume and power driver of a bioregenerative habitat. Total power for crop lighting at 200-400 µmol/m²/s PAR is 50-100 W/m² — meaning a 200 m² farm draws 10-20 kW just for illumination, supplemented by natural sunlight where possible.

### Water Recovery

The ISS Water Recovery System (WRS), inherited from the ECLSS domain, achieves 93% water loop closure by processing urine, humidity condensate, and hygiene water through multifiltration beds and a catalytic reactor. Closing the remaining 7% requires recovering water from:

1. **Brine** — the concentrated reject from the urine processor (30-50% of input water remains trapped in brine)
2. **Fecal water** — 0.11-0.15 kg/person/day of feces contains 75% water that is currently dried and stored
3. **Trace humidity** — condensate adsorbed into cabin materials and clothing

Advanced brine dryers using membrane distillation or ionomer-membrane drying can push water recovery to 98-99%, leaving a dry solid residue for stabilisation and storage or — in a fully biological loop — feedstock for the MELiSSA C1 degrading compartment.

## Material Reprocessing

Beyond metabolic waste, a space station generates a steady stream of structural and packaging scrap: decommissioned solar arrays, expended propellant tanks, cargo transfer bags, food packaging, failed electronics, and replaced subsystem hardware. On the ISS this mass is loaded into expendable cargo vehicles (Cygnus, HTV, Progress) and destructively deorbited — the waste burns up on reentry. As launch costs fall and mission duration grows, this linear waste stream becomes unacceptable.

### Solar Concentrator Melting

In space, sunlight is available continuously (orbit permitting) at 1,361 W/m² with no atmosphere to attenuate it. A parabolic concentrator mirror of 2-3 m diameter can focus sunlight to achieve spot temperatures of 1,500-2,500°C — sufficient to melt aluminum (660°C), steel (1,400-1,500°C), and titanium (1,668°C). The melting concept:

| Stage | Operation | Temperature | Output |
|-------|-----------|-------------|--------|
| 1. Sorting | Magnetic + density separation | Ambient | Separated metal/polymer streams |
| 2. Compaction | Hydraulic press | Ambient | Dense briquettes |
| 3. Solar melting | Concentrated solar flux | 700-1,700°C | Molten metal pool |
| 4. Casting | Chill mould or additive feed | Solidification | Ingot or wire feedstock |
| 5. Polymer extrusion | Heated extruder (waste heat) | 180-260°C | Filament spool |

The advantage of solar melting over electric arc furnaces (used terrestrially) is that it consumes no scarce electrical power — the energy is free. The challenge is managing the melt in microgravity, where surface tension dominates and molten metal forms floating spheres rather than a flat pool. Solutions include electromagnetic confinement (for conductive metals) and capillary-channel crucibles that wick the melt into a defined geometry.

### In-Space Manufacturing Feedstock

The output of material reprocessing is feedstock for in-space additive manufacturing:

- **Reclaimed polymer filament** — chopped cargo bags and packaging (ULD, Kevlar, Nomex, polyethylene) cleaned, shredded, and re-extruded into 1.75 mm filament for fused-deposition manufacturing of tools, brackets, and replacement parts.
- **Reclaimed metal wire** — aluminum and titanium scrap redrawn or cast into wire for wire-fed electron-beam or arc additive manufacturing of structural trusses and pressure-vessel repair stock.

A single ISS increment generates roughly 1,000-1,500 kg of trash. At 60-70% recoverable metal and polymer content, that is 600-1,000 kg of usable feedstock per crew rotation — enough to manufacture replacement parts on orbit rather than launching them.

### Cargo Vehicle Disposal

Unrecoverable waste — contaminated materials, hazardous compounds, and end-of-life hardware with no recycling value — is compacted, sealed, and loaded into an expendable cargo vehicle. The cargo vehicle is then deorbited on a trajectory that ensures complete destructive reentry over an uninhabited ocean. The reentry burn-up is not "recycling" in the mass-recovery sense, but it is the controlled disposal path that prevents orbital debris accumulation and closes the logistics loop by removing waste mass from the orbital regime.

| Disposal path | Mass fraction (est.) | Fate |
|---------------|----------------------|------|
| Recovered to feedstock | 60-70% | Re-enter manufacturing loop |
| Stabilised and stored | 10-15% | Surface storage or future recovery |
| Cargo vehicle burn-up | 15-25% | Destructive reentry over ocean |

## Propellant Recycling

### Boil-Off Recovery

Cryogenic propellants — liquid oxygen (LOX, 90 K) and liquid hydrogen (LH2, 20 K) — continuously boil off in storage because no thermal insulation is perfect. A passive LOX tank with multilayer insulation loses 0.05-0.5% of its mass per day; an LH2 tank loses 0.1-1.0% per day. Over a Mars transit (1,000 days), unmanaged boil-off would evaporate the entire propellant load.

Zero-boil-off (ZBO) systems use active cryocoolers to recondense the vented vapour back into the tank. The propellant recycling contribution goes further: the boil-off vapour is captured, recondensed, and returned to the tank rather than vented to space, and the cryocooler waste heat is routed to habitat thermal control or a Stirling generator for partial electricity recovery.

| Propellant | Boil-off rate (passive) | Recovery method | Energy cost |
|------------|--------------------------|-----------------|-------------|
| LOX (90 K) | 0.05-0.5%/day | Cryocooler recondensation | 5-15 W per kg/day |
| LH2 (20 K) | 0.1-1.0%/day | Cryocooler + para-ortho conversion | 30-100 W per kg/day |
| Residual N2/H2O | Vent gas | Membrane separation + compression | 10-30 W per kg/day |

### Residual Propellant Recovery

After a spacecraft engine shuts down, propellant remains trapped in feed lines, manifolds, and tank ullage — typically 1-3% of the loaded propellant mass. Rather than venting this residual to space (standard practice today), it can be recovered by:

1. **Positive-expulsion bladder** — a flexible bladder squeezes the tank to push residual propellant to a common sump
2. **Inert gas purge** — pressurised helium pushes residual propellant to a recovery tank
3. **Vapour capture** — a cold trap or zeolite adsorption bed captures vented propellant vapour before it exits the vehicle

### Vent Gas Reclamation

Beyond propellants, a station vents a steady stream of gases: cabin atmosphere leakage (N2, O2), experiment venting, and ullage gas from tank transfers. A gas reclamation system captures these vent streams through:

- **Selective membrane separation** — separating O2 from N2 and CO2 by differential permeation through polymer membranes
- **Cryogenic distillation** — condensing each gas fraction at its boiling point (O2 at 90 K, N2 at 77 K, CO2 at 195 K sublimation)
- **Sabatier reprocessing** — recovered CO2 reacts with recovered H2 over a ruthenium catalyst to produce methane and water, closing both the carbon and hydrogen loops

```
  CO2 + 4 H2  ──►  CH4 + 2 H2O    (Sabatier, 300-400°C, Ru catalyst)
     │                  │
     │                  ├──► H2O ──► electrolysis ──► H2 + O2  (loop closed)
     │                  │
     └──► CH4 ──► pyrolysis ──► C (solid) + 2 H2  (hydrogen recovered)
```

The carbon produced by methane pyrolysis is a solid that can be stored, used as a structural filler, or — in a fully closed system — fed to the MELiSSA waste compartment as a carbon source.

### Trace Contaminant Control

As a station approaches 99% closure, the remaining unrecovered mass is dominated by trace contaminants — the hundreds of volatile organic compounds (VOCs), metabolic byproducts, and off-gassed materials that accumulate in a sealed atmosphere. A closed loop does not just recover bulk mass; it must scrub these traces or they reach toxic concentration:

| Contaminant class | Source | Concentration ceiling | Removal method |
|-------------------|--------|----------------------|----------------|
| VOCs (formaldehyde, benzene) | Adhesives, paints, polymers | < 0.1 mg/m³ | Activated carbon + photocatalytic oxidation |
| Ethylene (C2H4) | Plant chambers (ripening hormone) | < 50 ppb | Potassium permanganate scrubber |
| Methane (CH4) | Flatulence, Sabatier leaks | < 1.0% (LEL 5%) | Catalytic oxidiser (Pt/Pd, 250°C) |
| Carbon monoxide (CO) | Pyrolysis, equipment overheating | < 11 ppm | Hopcalite catalyst (CuO/MnO2) |
| Ammonia (NH3) | Urine, cleaning agents | < 30 ppm | Phosphoric-acid-impregnated charcoal |
| Microbial volatile compounds | Biofilms, fungal growth | trace | HEPA + biocidal coating |

A full trace contaminant control subassembly (TCCS) draws 5-15 m³/hour of cabin air through a packed bed of activated charcoal and a high-temperature catalytic oxidiser, and is essential to closing the final 1-2% of the atmosphere loop. The spent charcoal cannot be regenerated in place; it becomes part of the cargo-vehicle disposal stream or — in a biological architecture — feedstock for the MELiSSA C1 degrading compartment.

## Mass Balance: The Closed Station

Combining all three recycling processes, a closed-loop orbital station for six crew approaches the following steady-state mass budget:

| Loop | Recovery rate | Make-up mass (kg/year) | Source |
|------|---------------|------------------------|--------|
| Water | 98% | ~800 kg | Brine dryer + fecal drying |
| Atmosphere (O2/CO2) | 95% | ~250 kg | Algae bioreactor + Sabatier |
| Food | 50-60% | ~1,500 kg | Higher plant chambers |
| Propellant | 90% | ~200 kg | Boil-off + residual recovery |
| Hardware/materials | 65% | ~1,000 kg | Solar melting + polymer filament |
| **Total** | **~85%** | **~3,750 kg/year** | Resupplied or ISRU-derived |

Reaching 99% overall closure requires closing the food loop to 80-90% (large plant chambers) and the materials loop to 90%+ (full scrap recovery). At that point, the annual make-up mass drops below 1,000 kg/year — low enough that a single cargo launch can supply a station for years, or that ISRU-produced water and CO2 from a planetary surface can fully close the deficit.

## Power and Energy Budget

Closing loops is energetically expensive — recycling always consumes more energy than the open-loop alternative of launching fresh mass. The dominant power consumers in a closed-loop station are biological lighting, cryogenic recondensation, and thermal rejection. The energy budget constrains the achievable closure rate as much as the mass budget does:

| Subsystem | Power draw (6-crew station) | Purpose | Energy source |
|-----------|----------------------------|---------|---------------|
| Crop lighting | 10-20 kW | Higher-plant photosynthesis (40-60 m²) | Solar + battery (eclipse) |
| Algae bioreactor | 1-3 kW | Pumps, mixing, illumination (9-12 m²) | Solar + LED |
| Water recovery (advanced) | 0.5-1.5 kW | Brine dryer, catalytic reactor | Electrical |
| Cryocoolers (ZBO propellant) | 2-8 kW | LOX/LH2 recondensation | Electrical |
| Sabatier + electrolysis | 3-6 kW | CO2 methanation, water splitting | Electrical |
| Thermal rejection | 5-15 kW | Radiators to reject metabolic + recycle heat | Passive radiators |
| **Total recycle load** | **~22-53 kW** | Continuous | Solar arrays + storage |

For context, the ISS generates 75-90 kW from its solar arrays, of which roughly 30 kW is available for science and growth after baseline subsystems. A closed-loop station needs 2-3x the ISS power budget — which is why space recycling and abundant space power (large solar arrays or nuclear electric) are co-dependent capabilities.

## Bootstrapping Sequence

The recycling capability is built incrementally, each stage reducing resupply mass:

1. **Stage 1 — Physical-chemical ECLSS** (Years 50-60): The ISS baseline. 85% water recovery, 93% in the WRS. Open atmosphere (CO2 vented or partially Sabatier-recovered). No material recycling.
2. **Stage 2 — Advanced physical-chemical** (Years 60-75): Brine drying pushes water to 95-98%. Full Sabatier loop closes the carbon loop. Residual propellant recovery begins.
3. **Stage 3 — Hybrid bio/physical** (Years 75-90): Algae bioreactors (MELiSSA C3) close the O2 loop biologically. Solar melting begins for metal scrap. Polymer filament extrusion comes online.
4. **Stage 4 — Bioregenerative + closed materials** (Years 90+): Higher-plant chambers provide 50-80% of food. Full material reprocessing. Cargo vehicle disposal reserved only for truly unrecoverable mass. 99% loop closure achieved.

## Failure Modes and Redundancy

A closed loop is a single point of failure: if the recycling system stops, the crew suffocates, dehydrates, or starves within hours to days. Redundancy philosophy shifts from "launch spares" (the ISS model) to "buffer storage + divergent pathways":

| Failure mode | Buffer duration | Redundant pathway |
|--------------|-----------------|-------------------|
| Water recovery outage | 30-day potable reserve | Stored water + contingency rationing |
| Algae bioreactor crash | 14-day O2 reserve | Physical-chemical OGS electrolyser backup |
| Crop failure (disease, radiation) | 90-day food reserve | Stored dehydrated rations + cargo resupply |
| Sabatier reactor poisoning | CO2 beds (CDRA) fallback | Absorbent beds accept degraded throughput |
| Solar melting failure | Deferred scrap processing | Increased cargo-vehicle disposal temporarily |

The biological compartments are the most fragile: a single contamination event (phage infection of the algae culture, fungal blight in the wheat chamber) can collapse the loop. Crews must maintain pure seed cultures in cryogenic archive, sterilise the reactor between cycles, and monitor for microbial drift — the same disciplines terrestrial agriculture uses, but with no fallback ecosystem to absorb a failure.

## Dependencies

This capability sits at the convergence of life support, chemistry, and materials science:

- **[human-spaceflight.eclss](../human-spaceflight/eclss.md)** — provides the baseline atmosphere, water, and waste-management subsystems that space recycling extends toward full closure
- **[chemistry](../chemistry/index.md)** — catalytic oxidation, Sabatier methanation, membrane separation, and acid-base chemistry for waste degradation and gas reclamation
- **[polymers](../polymers/index.md)** — reclaimed polymer feedstock for in-space additive manufacturing filament
- **[metals](../metals/index.md)** — reclaimed metal scrap for solar melting and structural feedstock

## Further Reading

- [Life Support Loop Closure](./space-recycling.life-support-loop-closure.md) — MELiSSA, algae bioreactors, higher-plant chambers
- [Material Reprocessing](./space-recycling.material-reprocessing.md) — solar melting, waste compaction, cargo vehicle disposal
- [Propellant Recycling](./space-recycling.propellant-recycling.md) — boil-off recovery, residual propellant, vent gas reclamation
- [ECLSS — Environmental Control & Life Support](../human-spaceflight/eclss.md) — the baseline subsystem this capability extends

[↑ Back to Space Resources](./index.md)
