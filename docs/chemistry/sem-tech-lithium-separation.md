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

## Membrane Specifications for Lithium Selectivity

The lithium-selective SEM Tech membrane requires specialized resin selection and formulation beyond the standard cation exchange membrane used in chlor-alkali cells. The membrane exploits the difference in hydration energy between Li⁺ (520 kJ/mol hydration enthalpy) and Na⁺ (405 kJ/mol hydration enthalpy) to achieve preferential Li⁺ transport through appropriately sized nanopores (0.6-0.8 nm effective pore diameter).

**Resin selection**: Chelating resins with crown ether functional groups (12-crown-4 for Li⁺ selectivity) or iminodiacetic acid groups provide selectivity over Na⁺ by factors of 5-20:1 in laboratory column tests. These specialized resins are commercially available from major ion exchange resin manufacturers (Dowex, Lewatit, Purolite product lines) at $50-200 per cubic foot — more expensive than standard water softener resin ($5-20 per cubic foot) but still far cheaper than Nafion membrane.

**Membrane fabrication**: The standard SEM Tech process applies: pulverize the lithium-selective resin beads to below 200 microns, disperse at 30-50% loading by volume in PVC/CPVC binder dissolved in THF or cyclohexanone, cast at 150-400 microns thickness, dry at ambient temperature. Membrane cost: estimated $2-5 per square foot due to the higher resin cost, still 20-80x cheaper than conventional selective membranes.

**Projected performance**: Selectivity ratio Li⁺/Na⁺ of 5-20:1 at current densities of 5-20 mA/cm². Area resistance: 15-40 Ω·cm² (higher than standard SEM Tech cation membrane at 5-15 Ω·cm² due to the specialized resin). Expected Li⁺ flux: 0.5-2.0 mol/m²/h at 10 mA/cm².

## System Design Parameters

A pilot-scale lithium recovery plant using SEM Tech electrodialysis would be configured as follows:

**ED stack configuration**: 100-300 cell pairs per stack, each cell pair consisting of one lithium-selective cation membrane and one standard anion membrane. Active membrane area per cell: 0.5-2.0 m². Total membrane area per stack: 100-1,200 m². At SEM Tech pricing of $2-5/ft², total membrane cost per stack is $2,200-65,000 — compared to $500,000-5,000,000 for conventional selective membranes at equivalent area.

**Operating conditions**: Stack voltage 50-300V DC (0.5-1.5V per cell pair), current density 5-20 mA/cm², feed flow velocity 3-8 cm/s through 0.5-1.0 mm spacer channels. Operating temperature 20-40°C (ambient). System pressure 1-3 bar. No heating or cooling required.

**Throughput**: At 10 mA/cm² current density and 40% Li⁺ recovery per pass, a single stack with 200 cell pairs of 1.0 m² membrane area processes approximately 2.0 m³/h of brine containing 1,000 mg/L Li⁺, producing 0.8 kg/h of Li⁺ in the concentrate stream (equivalent to 42 kg/day of Li₂CO₃ or 15 tonnes/year). A 10-stack array produces 150 tonnes/year of LCE.

**Multi-stage enrichment**: A single ED pass typically achieves 3-5x concentration of Li⁺. For feed brines at 1,000 mg/L Li⁺, the first-stage concentrate reaches 3,000-5,000 mg/L. A second ED stage further concentrates to 10,000-25,000 mg/L — sufficient for efficient Li₂CO₃ precipitation. Each stage operates at progressively lower feed volume but higher ionic concentration, requiring adjustment of current density (higher stages operate at 3-10 mA/cm² to manage concentration polarization). Total membrane area for a two-stage system producing 500 tonnes LCE/year: approximately 5,000-10,000 m², costing $50,000-500,000 at SEM Tech membrane pricing.

**Brine pretreatment requirements**: Raw brine from salt flats or geothermal sources contains suspended solids (10-500 mg/L TSS), dissolved organic matter (5-50 mg/L DOC), and silica (50-500 mg/L SiO₂) that can foul membranes. Pretreatment sequence: (1) sand filtration to 10-50 μm, (2) cartridge filtration to 1-5 μm, (3) activated carbon for organics removal, (4) pH adjustment to 6.5-7.5 with HCl or NaOH to prevent CaCO₃ and Mg(OH)₂ scaling on membrane surfaces. Pretreatment capital cost: $20,000-50,000 for a 500 t/year plant. Operating cost: $0.05-0.20/m³ of brine processed.


**Energy consumption**: At 1.0V per cell pair and 10 mA/cm², each stack consumes approximately 2.0 kW of electrical power. Pumping power at 2 m³/h through 1 mm spacers: approximately 0.2 kW. Total system power: 2.2 kW per stack. Energy per kg LCE: approximately 3.8 kWh. At $0.06/kWh, electricity cost is $0.23/kg LCE — less than 0.1% of the current LCE market price of $15-30/kg.

## Comparison with Conventional Extraction Methods

| Parameter | Solar Evaporation | Hard Rock Mining | SEM Tech ED (Projected) |
|-----------|------------------|------------------|------------------------|
| **Processing time** | 12-24 months | 2-5 days | Hours to days |
| **Water consumption** | 500-800 m³/t LCE | 100-250 m³/t LCE | 50-100 m³/t LCE (recycled) |
| **Energy** | Solar (free) | 15-25 kWh/kg LCE | 2-8 kWh/kg LCE |
| **Land use** | 5-20 km² per 10,000 t/yr | Mine footprint | <0.01 km² per 10,000 t/yr |
| **Li recovery** | 40-60% | 70-85% | 80-95% (projected) |
| **Capital cost** | Low (ponds) | High (mine + plant) | Moderate (ED stacks) |
| **Operating cost** | $2,000-4,000/t LCE | $4,000-8,000/t LCE | $1,000-3,000/t LCE (projected) |
| **Mg/Li tolerance** | Poor (>6:1 difficult) | N/A (ore feed) | Good (selective membrane) |
| **Environmental impact** | High (water depletion) | High (mine waste) | Low (closed loop) |

The SEM Tech ED approach is most competitive for brines with high Mg/Li ratios (where evaporation struggles) and for distributed small-scale production (where building evaporation ponds is impractical).

## Applications

**Brine extraction**: Salt flat brines (Salar de Atacama, Salar de Uyuni) contain 0.1-1.5% Li. Electrodialysis with selective membranes could replace months-long evaporation pond processing with continuous extraction in days.

**Geothermal brines**: Geothermal fluids in the Salton Sea (California) and Rhine Valley (Germany) contain commercially interesting lithium concentrations (100-400 mg/L) alongside high total dissolved solids. ED can extract lithium while the geothermal plant generates power.

**Battery recycling**: Spent lithium-ion batteries are shredded and leached to produce a mixed metal solution (Li, Co, Ni, Mn). Lithium-selective membranes recover lithium from this complex stream — a growing application as battery waste volumes increase.

**Seawater**: Seawater contains only 0.17 mg/L Li, making recovery uneconomical with current technology. Selective membranes at very low cost might make marginal extraction feasible, though this remains speculative.

**Produced water**: Oil and gas extraction generates large volumes of saline produced water, some of which contains lithium at 50-200 mg/L. Co-locating lithium recovery with existing produced water treatment could improve economics while reducing waste disposal volumes.

## Scaling Considerations

**Pilot scale (10-100 tonnes LCE/year)**: 1-5 ED stacks, each with 100-200 cell pairs of 0.5-1.0 m² membranes. Total membrane area: 50-500 m². Membrane cost at SEM Tech pricing: $1,000-25,000. Power consumption: 5-25 kW. Suitable for testing at geothermal sites or brine pilot projects.

**Demonstration scale (100-1,000 tonnes LCE/year)**: 10-50 stacks, total membrane area 500-5,000 m². Membrane cost: $10,000-250,000. Power: 50-250 kW. Requires automated control system, continuous feed pretreatment (sand filtration + 10-micron cartridge filter + activated carbon), and product crystallization circuit.

**Commercial scale (1,000-10,000 tonnes LCE/year)**: 50-500 stacks in parallel trains, total membrane area 5,000-50,000 m². Membrane cost: $100,000-2,500,000 (still 10-100x cheaper than conventional selective membranes). Power: 0.5-2.5 MW. Requires dedicated pretreatment plant, product purification (carbonation to Li₂CO₃ or causticization to LiOH), and brine management infrastructure.


## Concentration and Product Finishing

The lithium-rich concentrate stream from the ED stack contains 5,000-30,000 mg/L Li⁺ (enriched 5-30x from the original brine feed). This concentrate requires further processing to produce commercially saleable lithium products.

**Lithium carbonate (Li₂CO₃) production**: The standard battery-grade product. Sodium carbonate (Na₂CO₃, soda ash) is added to the lithium concentrate at 85-95°C, precipitating Li₂CO₃ (solubility 1.3 g/100 mL at 20°C, decreasing with temperature). At a Li⁺ concentration of 15,000 mg/L in the concentrate, adding 82 g/L of Na₂CO₃ precipitates approximately 80% of the lithium as Li₂CO₃ crystals over 2-4 hours of stirring. The crystals are filtered, washed with deionized water at 90°C (to minimize solubility losses), and dried at 120°C. Product purity: 99.0-99.5% after one precipitation; 99.9%+ after re-dissolution in pure water and re-precipitation.

**Lithium hydroxide (LiOH) production**: Required for lithium iron phosphate (LFP) and nickel manganese cobalt (NMC) cathode precursors. Li₂CO₃ is dissolved in water and reacted with Ca(OH)₂ (slaked lime) at 90-95°C: Li₂CO₃ + Ca(OH)₂ → 2LiOH + CaCO₃. The insoluble CaCO₃ is filtered off. The LiOH solution is evaporated to crystallize LiOH·H₂O monohydrate at 50-60°C. Battery-grade LiOH·H₂O requires 99.5%+ purity with Na and Ca below 50 ppm each.

**Energy and reagent costs per tonne of LCE**: Approximately 200-400 kg of Na₂CO₃ at $200/tonne ($40-80), 2-5 MWh of thermal energy for heating and evaporation ($120-300 at $60/MWh), and 50-100 m³ of process water. Total finishing cost: approximately $200-500 per tonne of LCE, dominated by thermal energy.

## Cost Analysis

**Capital cost estimate** for a demonstration-scale plant (500 tonnes LCE/year):

| Component | Estimated Cost | Notes |
|-----------|---------------|-------|
| ED stacks (25 units, 200 cell pairs each) | $150,000-500,000 | SEM Tech membranes at $2-5/ft² |
| Power supply (250 kW DC rectifier) | $25,000-50,000 | Thyristor rectifier, 95%+ efficiency |
| Pumps and piping | $15,000-30,000 | Corrosion-resistant (HDPE, PVC, titanium) |
| Feed pretreatment system | $20,000-40,000 | Filters, activated carbon, pH adjustment |
| Product finishing circuit | $30,000-60,000 | Reactor, filter, dryer, crystallizer |
| Control and instrumentation | $10,000-25,000 | PLC, sensors, SCADA |
| **Total** | **$250,000-705,000** | **$500-1,400 per annual tonne LCE** |

For comparison, a conventional evaporation pond operation of similar capacity costs $2,000-5,000 per annual tonne of LCE capacity (mostly land, earthworks, and pond liners). A hard-rock mining and processing plant costs $5,000-15,000 per annual tonne. SEM Tech ED offers 2-10x lower capital intensity if the membrane selectivity claims are validated.

**Operating cost estimate**: Electricity at 5 kWh/kg LCE × 500,000 kg/year = 2,500,000 kWh/year at $0.06/kWh = $150,000. Membrane replacement (12-month lifetime, $25,000 replacement cost): $25,000/year. Reagents (Na₂CO₃ for precipitation): $30,000/year. Labor (2 operators): $100,000/year. Maintenance: $20,000/year. **Total: approximately $325,000/year or $650/tonne LCE.** Current LCE market price: $15,000-30,000/tonne, providing ample margin even with conservative performance assumptions.

## Safety

- **Lithium compound handling**: LiOH is corrosive and causes severe skin and eye burns. Li₂CO₃ is less hazardous but still an irritant. Standard chemical PPE (goggles, gloves, aprons) required for all lithium product handling.
- **Brine handling**: Natural brines contain high concentrations of salts, heavy metals, and arsenic in some deposits. Avoid skin contact and inhalation of dried brine dust.
- **Electrical safety**: ED stacks for lithium separation operate at high DC voltages. Proper grounding, insulation, and lockout/tagout procedures are mandatory — see [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) for electrical safety details.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode requires ventilation in enclosed installations.
- **Pressure**: ED systems operate at low pressure (1-5 bar), presenting lower mechanical hazard than reverse osmosis systems (40-80 bar), but leaks in pressurized brine systems still require secondary containment.


## Cross-Domain Dependencies

The lithium separation system depends on several upstream capabilities. The PVC/CPVC binder resin requires [chlor-alkali electrolysis](electrolysis.md) for chlorine production and the [petrochemical industry](./index.md) for ethylene. The lithium-selective chelating resin beads require sulfonated polystyrene chemistry (from styrene monomer derived from benzene and ethylene). The power supply requires [rectifier-grade electrical infrastructure](../energy/electricity.md) delivering 50-300V DC at current densities of 50-200 A per stack. The sodium carbonate reagent for lithium precipitation is produced via the [Solvay process](alkalis.md) or mined as trona ore. Product finishing requires thermal energy (85-120°C) from a [boiler or heat exchanger](../energy/index.md) capable of delivering 100-300 kW of heat to the precipitation and drying stages.

## Limitations

**Unproven selectivity**: The patent claims lithium-selective membrane capability, but no experimental data on Li⁺/Na⁺ selectivity ratios, Li⁺/Mg²⁺ rejection rates, or long-term membrane performance in brine has been published. The claimed selectivity is plausible based on ion exchange resin chemistry but unverified.

**TRL gap**: SEM Tech membranes are at TRL 5 for chlor-alkali electrolysis. Lithium-specific configurations have not been built or tested. Significant development would be needed to reach pilot-scale operation.

**Brine complexity**: Natural brines vary enormously in composition. A membrane optimized for one brine source may perform poorly on another due to different ion ratios, organic content, or scaling tendency.

**Membrane lifetime in high-salinity brine**: SEM Tech membranes have been tested at pH 0 and ORP >1.5V in chlor-alkali conditions, but continuous exposure to concentrated NaCl-MgCl₂-CaCl₂ brines at 20-40°C presents different fouling and degradation mechanisms. Silica scaling (SiO₂ precipitation at pH >8) and calcium sulfate (CaSO₄) crystallization on membrane surfaces are common failure modes in brine ED. Electrodialysis reversal (EDR) — periodic polarity switching every 15-30 minutes — can mitigate scaling but has not been tested with SEM Tech membrane stacks.

**Competing ED technologies**: Several companies (Lilac Solutions, EnergyX, Summit Nanotech) are developing lithium-selective membranes and ED processes at TRL 6-8 with significant venture capital investment ($50-200M cumulative). SEM Tech offers a cost advantage but would enter a competitive market with established players.

**Competition with established methods**: Solar evaporation is extremely slow but essentially free in suitable climates. SEM Tech ED would need to demonstrate both performance and cost advantages over evaporation to displace existing operations.

## See Also

- [SEM Tech](sem-tech.md) -- core membrane technology and manufacturing process
- [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) -- ED principles and membrane stack design
- [Electrolysis](electrolysis.md) -- parent article on industrial electrochemical processes

---


*Part of the [Bootciv Tech Tree](../index.md) | [Chemistry](./index.md) | [All Domains](../index.md)*
