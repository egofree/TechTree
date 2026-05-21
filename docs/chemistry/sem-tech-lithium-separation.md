# SEM Tech Lithium Separation: Selective Ion Recovery

> **Node ID**: chemistry.lithium-separation
> **Domain**: Chemistry
> **Timeline**: Years 25-40
> **Outputs**: lithium_compounds
> **Tags**: materials=[chemicals, polymers], era=industrial

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech](sem-tech.md)) enable selective lithium ion separation as a downstream application of the membrane platform. The SEM Tech patent describes a microporous ion-selective separator configured for lithium separation — blocking larger sodium ions while allowing lithium passage (patent line 107). Electrodialysis (see [SEM Tech Electrodialysis](sem-tech-electrodialysis.md)) is the primary mechanism by which this selective transport is achieved at scale.

## Overview

Lithium is a critical material for batteries, electric vehicles, and grid-scale energy storage. Demand has grown sharply as lithium-ion batteries become the dominant energy storage technology. Conventional lithium extraction relies on brine evaporation ponds (months to years of solar concentration) or hard-rock mining of spodumene ores (energy-intensive roasting and acid leaching). Both methods have significant environmental footprints and slow throughput.

SEM Tech membranes offer a potential path to electrochemical lithium recovery using selective ion transport. The patent's claim of a microporous ion-selective separator tuned for lithium separation suggests that membranes with pore sizes and functional groups preferential to Li⁺ can be manufactured from the same off-the-shelf resin beads and PVC/CPVC binder used in chlor-alkali cells. This would enable continuous lithium extraction from brines or recycling streams, bypassing the months-long evaporation process.

**Speculative status**: Lithium-specific separation with SEM Tech membranes is claimed in the patent but has not been demonstrated experimentally. The membrane platform is at TRL 5 for chlor-alkali applications; lithium-selective membranes remain untested.

## Lithium Demand

Lithium consumption has shifted from historical uses (ceramics, glass, lubricants) to dominance by battery production:

- **Electric vehicles**: Each EV battery pack contains 10-60 kg of lithium carbonate equivalent (LCE)
- **Grid-scale energy storage**: Stationary battery installations for load leveling and renewable integration
- **Consumer electronics**: Lithium-ion batteries for phones, laptops, and tools
- **Industrial applications**: Grease, ceramics, glass, and aluminum smelting flux

Meeting projected demand requires new extraction capacity and recovery from secondary sources including battery recycling streams.

## SEM Tech Membrane in Lithium Separation

The SEM Tech patent (line 107) specifically mentions a "microporous ion selective separator" configured "for lithium separation to block out larger sodium ions." This indicates that the membrane's pore structure and ion exchange functional groups can be tuned to discriminate between lithium and sodium — a technically challenging separation because Li⁺ (ionic radius 0.76 Å) and Na⁺ (ionic radius 1.02 Å) have similar charge but different hydrated radii.

**Key mechanism**: The microporous separator exploits differences in hydrated ionic radius. While bare Li⁺ is smaller than Na⁺, the hydrated lithium ion (Li⁺·nH₂O) is actually larger due to its higher charge density attracting a stronger hydration shell. A membrane with appropriately sized pores and selective functional groups can preferentially transport Li⁺ while blocking Na⁺, K⁺, and Mg²⁺.

**Membrane manufacturing**: The standard SEM Tech process applies — pulverize specialized ion exchange resin beads, mix with PVC/CPVC binder in solvent, cast, dry. Resin selection and loading would be tuned for lithium selectivity rather than general cation transport. The patent's embodiment list (line 104-107) includes coatings on electrodes and microporous ion-selective separators alongside rare-earth and platinum group metal resins, placing lithium separation within the same tunable membrane framework.

**Relationship to electrodialysis**: The selective membrane alone does not perform separation — it requires an electric field to drive ion transport. Electrodialysis (see [SEM Tech Electrodialysis](sem-tech-electrodialysis.md)) provides this framework, using stacked membrane pairs between electrodes to continuously move target ions from a feed stream into a concentrate stream.

## Selective Ion Transport

The core challenge in lithium extraction from natural brines is separating Li⁺ from chemically similar ions present at much higher concentrations:

- **Sodium (Na⁺)**: Typically 10-100x the lithium concentration in brines
- **Potassium (K⁺)**: Often comparable to or greater than lithium concentration
- **Magnesium (Mg²⁺)**: Particularly problematic in South American brines (Li:Mg ratios can reach 1:10)
- **Calcium (Ca²⁺)**: Present in most brine sources

Conventional processing uses sequential precipitation — raising pH to precipitate Mg and Ca as hydroxides, then concentrating the remaining Li. This is chemical-intensive and produces large volumes of waste. The Mg/Li ratio is a key metric: ratios above 6:1 make conventional processing very difficult, and several major brine deposits have ratios exceeding 10:1.

A lithium-selective SEM Tech membrane could perform this separation electrochemically via electrodialysis, using stacked membrane pairs where only Li⁺ passes through the selective membrane. The result is a lithium-enriched concentrate stream and a lithium-depleted waste stream, with no chemical addition required. The selectivity challenge is fundamentally about pore size and functional group tuning — the same approach SEM Tech uses for specialized ion resins targeting rare earths and platinum group metals (patent line 105).

## Process Design

A lithium recovery system using SEM Tech membranes would combine elements from the chlor-alkali cell architecture and the electrodialysis stack:

**Feed preparation**: Raw brine (from salt flats, geothermal fluids, or battery recycling leachate) is pre-filtered to remove suspended solids. pH adjustment may be needed to prevent scaling.

**Electrodialysis stack**: Lithium-selective cation exchange membranes alternate with standard anion exchange membranes. Under applied voltage, Li⁺ migrates through the selective membrane into the concentrate channel while Na⁺, K⁺, Mg²⁺, and Ca²⁺ are rejected.

**Concentration**: Multiple ED stages increase lithium concentration progressively. The final concentrate is processed to lithium carbonate (Li₂CO₃) or lithium hydroxide (LiOH) by carbonation or precipitation.

**Closed-loop operation**: Following the SEM Tech design philosophy, depleted brine recirculates or is returned to the source. No continuous chemical discharge.

**Expected operating parameters** (estimated from conventional ED practice, not yet verified with SEM Tech membranes):
- Feed lithium concentration: 100-15,000 mg/L (brine-dependent)
- Lithium recovery per pass: 30-60% (multiple stages for higher recovery)
- Energy consumption: 2-8 kWh per kg LCE (estimated, feed-dependent)
- Operating temperature: ambient (20-40°C)
- Membrane replacement cycle: months to ~1 year (consistent with SEM Tech chlor-alkali experience)

## Applications

**Brine extraction**: Salt flat brines (Salar de Atacama, Salar de Uyuni) contain 0.1-1.5% Li. Electrodialysis with selective membranes could replace months-long evaporation pond processing with continuous extraction in days.

**Geothermal brines**: Geothermal fluids in the Salton Sea (California) and Rhine Valley (Germany) contain commercially interesting lithium concentrations (100-400 mg/L) alongside high total dissolved solids. ED can extract lithium while the geothermal plant generates power.

**Battery recycling**: Spent lithium-ion batteries are shredded and leached to produce a mixed metal solution (Li, Co, Ni, Mn). Lithium-selective membranes recover lithium from this complex stream — a growing application as battery waste volumes increase.

**Seawater**: Seawater contains only 0.17 mg/L Li, making recovery uneconomical with current technology. Selective membranes at very low cost might make marginal extraction feasible, though this remains speculative.

**Produced water**: Oil and gas extraction generates large volumes of saline produced water, some of which contains lithium at 50-200 mg/L. Co-locating lithium recovery with existing produced water treatment could improve economics while reducing waste disposal volumes.

## Safety

- **Lithium compound handling**: LiOH is corrosive and causes severe skin and eye burns. Li₂CO₃ is less hazardous but still an irritant. Standard chemical PPE (goggles, gloves, aprons) required for all lithium product handling.
- **Brine handling**: Natural brines contain high concentrations of salts, heavy metals, and arsenic in some deposits. Avoid skin contact and inhalation of dried brine dust.
- **Electrical safety**: ED stacks for lithium separation operate at high DC voltages. Proper grounding, insulation, and lockout/tagout procedures are mandatory — see [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) for electrical safety details.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode requires ventilation in enclosed installations.
- **Pressure**: ED systems operate at low pressure (1-5 bar), presenting lower mechanical hazard than reverse osmosis systems (40-80 bar), but leaks in pressurized brine systems still require secondary containment.

## Limitations

**Unproven selectivity**: The patent claims lithium-selective membrane capability, but no experimental data on Li⁺/Na⁺ selectivity ratios, Li⁺/Mg²⁺ rejection rates, or long-term membrane performance in brine has been published. The claimed selectivity is plausible based on ion exchange resin chemistry but unverified.

**TRL gap**: SEM Tech membranes are at TRL 5 for chlor-alkali electrolysis. Lithium-specific configurations have not been built or tested. Significant development would be needed to reach pilot-scale operation.

**Brine complexity**: Natural brines vary enormously in composition. A membrane optimized for one brine source may perform poorly on another due to different ion ratios, organic content, or scaling tendency.

**Competition with established methods**: Solar evaporation is extremely slow but essentially free in suitable climates. SEM Tech ED would need to demonstrate both performance and cost advantages over evaporation to displace existing operations.

## See Also

- [SEM Tech](sem-tech.md) -- core membrane technology and manufacturing process
- [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) -- ED principles and membrane stack design
- [Electrolysis](electrolysis.md) -- parent article on industrial electrochemical processes

---

*Part of the [Bootciv Tech Tree](../) | [Chemistry](./) | [All Domains](../)*
