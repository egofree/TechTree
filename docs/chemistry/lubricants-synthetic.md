# Synthetic Lubricants & Specialty Fluids

> **Node ID**: chemistry.lubricants-synthetic
> **Domain**: [Chemistry](./index.md)
> **Parent**: [Lubricants, Oils & Fluid Mechanics](lubricants.md)
> **Dependencies**: [`chemistry.lubricants-mineral`](./lubricants-mineral.md),
> [`chemistry.petroleum-alternatives`](./petroleum-alternatives.md)
> **Enables**: None
> **Timeline**: Years 50-200+
> **Outputs**: synthetic_oil, vacuum_oil, pfpe_grease
> **Critical**: No — synthetic lubricants enable demanding applications but are not prerequisites for core capabilities

Synthetic lubricants are engineered molecules with uniform structure, produced by chemical synthesis rather than petroleum distillation. They extend the temperature range, oxidation stability, and consistency of lubrication beyond what mineral oils can achieve. Specialty fluids — vacuum oils, cleanroom-compatible lubricants, and perfluoropolyether (PFPE) greases — serve niche applications in aerospace, vacuum technology, and semiconductor manufacturing where mineral oil lubricants fail.

The key advantage of synthetic lubricants over mineral oils is molecular uniformity. Mineral oil contains a distribution of hydrocarbon chain lengths and branching patterns, giving it a mix of light fractions (volatile, thin) and heavy fractions (sludgy, viscous). Synthetic lubricants are built from identical or near-identical molecules, eliminating these extremes. The result is a lubricant with predictable viscosity across a wider temperature range, better resistance to oxidation (no reactive impurities), and lower volatility (no light fractions to evaporate). This predictability matters in jet engines (where oil must flow at -40°C and survive at 200°C), vacuum systems (where even tiny vapor pressures contaminate the process), and semiconductor manufacturing (where outgassing from lubricants deposits on wafers and causes defects).

## Synthetic Lubricants

**Composition**: Engineered hydrocarbon or non-hydrocarbon molecules with uniform structure, produced by chemical synthesis rather than petroleum distillation. The uniform molecular weight distribution (no light or heavy fractions) gives synthetics advantages in temperature range, oxidation stability, and consistency.

**Prerequisites**:
- Advanced chemical synthesis capability
- Specific precursor chemicals (varies by type)
- Controlled reaction conditions (temperature, pressure, catalysts)

**Materials**:
- Varies by synthetic type (see below)

**Types and Manufacture**:

**Polyalphaolefin (PAO)**: Hydrocarbon synthetic made by oligomerizing α-olefins (primarily decene, C₁₀) with BF₃ catalyst, then hydrogenating. Uniform molecular weight distribution gives: better low-temperature fluidity (pour point -50 to -65°C vs -15°C for mineral oil), higher viscosity index (130-150 vs 95-105), and better oxidation stability (2-3x longer oil life). Used in jet engine oils, Arctic machinery, and long-drain automotive oils.

**Ester oils**: Diesters and polyol esters, synthesized from organic acids and alcohols. Excellent lubricity (polar ester groups adsorb strongly to metal surfaces), good thermal stability (200-250°C continuous), and biodegradable. Used in jet engine oils (MIL-PRF-23699), compressor oils, biodegradable hydraulic fluids (forestry, marine), and two-stroke engine oils.

**Silicone oils**: Polydimethylsiloxane (PDMS), made from silicon + methyl chloride chemistry. Extremely wide temperature range (-70 to +250°C), chemically inert, and excellent dielectric properties. Poor lubricity for metal-on-metal (low load-carrying capacity). Used where temperature stability or chemical inertness matters more than extreme pressure performance: diffusion pump fluids, dashpot dampers, electrical insulation, mold release, and medical devices.

**Perfluoropolyether (PFPE)**: Fluorinated synthetic, the most chemically resistant lubricant. Inert to oxygen, fuels, solvents, acids, and bases. Temperature range: -80 to +300°C. Ultra-low vapor pressure, meaning no outgassing in vacuum. Used in spacecraft mechanisms, semiconductor manufacturing equipment, oxygen compressors (mineral oil + high-pressure O₂ = explosion risk), and chemical processing valves.

**Properties**: PAO: pour point -50 to -65°C, VI 130-150, 2-3x mineral oil oxidation life. Ester: 200-250°C thermal stability, biodegradable. Silicone: -70 to +250°C, chemically inert, poor metal-on-metal lubricity. PFPE: -80 to +300°C, chemically inert, ultra-low vapor pressure.

**Synthetic lubricant properties comparison**:

| Type | Viscosity Range (cSt at 40°C) | Pour Point (°C) | Flash Point (°C) | VI | Thermal Stability (°C) | Vapor Pressure at 25°C | Relative Cost vs Mineral |
|------|-------------------------------|-----------------|-------------------|-----|----------------------|------------------------|--------------------------|
| PAO | 4-100 | -50 to -65 | 220-280 | 130-150 | 150-180 | <10⁻⁶ Pa | 3-5x |
| Diester | 5-25 | -60 to -70 | 220-250 | 140-160 | 200-220 | ~10⁻⁴ Pa | 4-6x |
| Polyol ester | 15-100 | -40 to -55 | 250-310 | 130-150 | 220-250 | ~10⁻⁵ Pa | 5-8x |
| Silicone (PDMS) | 10-100,000 | -70 to -50 | 300-350 | 200-400 | 250-280 | ~10⁻⁶ Pa | 8-15x |
| PFPE | 10-500 | -80 to -50 | Non-flammable | 100-150 | 280-300 | <10⁻¹⁰ Pa | 50-100x |
| Mineral oil (ref) | 10-460 | -10 to -30 | 180-240 | 95-105 | 120-150 | ~10⁻² Pa | 1x |

**Safety & Handling**:

> **Safety warning**: PFPE decomposes above 300°C, releasing toxic fluorinated compounds. Silicone oils are not readily biodegradable. PAO and ester oils have good fire safety profiles (high flash points). Handle all synthetic lubricants according to the manufacturer's safety data, which varies significantly by chemistry.

**Specific hazards**:
- **PFPE thermal decomposition**: Above 300°C, PFPE breaks down into hydrogen fluoride (HF), carbonyl fluoride (COF₂), and perfluoroisobutylene (PFIB). HF causes severe chemical burns to skin, eyes, and lungs (IDLH 30 ppm). COF₂ hydrolyzes to HF in moist tissue. PFIB is one of the most toxic fluorocarbons known (LC₅₀ in rats ~ 0.5 ppm for 4-hour exposure). Use PFPE only where operating temperature remains below 250°C. If a PFPE-lubricated bearing overheats, evacuate the area and ventilate before approaching.
- **Ester oil hydrolysis**: Ester lubricants react with water at elevated temperatures, hydrolyzing back into acids and alcohols. The resulting organic acids (acetic, butyric) corrode bearings and seals. Keep ester oil systems dry (water content <200 ppm). Install desiccant breathers on reservoirs. If oil pH drops below 5.0, drain and replace.
- **Silicone oil seal incompatibility**: Silicone oil swells nitrile rubber (NBR) seals by 20-40%, causing leakage. Use fluorocarbon (FKM/Viton) or PTFE seals with silicone oils. Before converting a system from mineral oil to silicone, replace all elastomeric seals with compatible materials.
- **PAO seal shrinkage**: PAO has lower solvency than mineral oil and can shrink some elastomers, causing leaks. Use fluorocarbon or polyurethane seals. Alternatively, blend PAO with 10-20% ester oil to restore seal compatibility.

## Prerequisites

- Advanced chemical synthesis capability (olefin polymerization, esterification, fluorination)
- Specific precursor chemicals: α-olefins (for PAO), organic acids and alcohols (for esters), chlorosilanes (for silicones), fluorinated monomers (for PFPE)
- Controlled reaction conditions (temperature ±5°C, pressure 1-50 bar, catalyst systems)
- Distillation and purification equipment for precursor production
- Quality testing: viscosity measurement (capillary viscometer), flash point (Pensky-Martens closed cup), pour point (ASTM D97)

## Bill of Materials

| Material | Quantity per 100 L synthetic lubricant | Source | Alternatives |
|----------|---------------------------------------|--------|-------------|
| α-Olefins (primarily decene, C₁₀) | 80-95 kg | [Petrochemicals](petroleum-alternatives.md) — ethylene oligomerization | Higher olefins (C₁₂-C₁₄) for higher viscosity grades |
| BF₃ catalyst (for PAO) | 0.5-2 kg | [Fluorine chemistry](acids.md) — boron trifluoride | TiCl₄/Ziegler-Natta catalysts |
| Organic acids (for esters) | 40-70 kg | [Chemistry](index.md) — carboxylic acid synthesis | Natural fatty acids (lower purity, less consistent) |
| Polyhydric alcohols (for esters) | 20-40 kg | [Chemistry](index.md) — pentaerythritol, trimethylolpropane | Ethylene glycol (diesters only) |
| Chlorosilanes (for silicones) | 50-80 kg | [Silicon](../silicon/index.md) — methyl chloride + silicon | Imported silicone intermediates |
| Fluorinated monomers (for PFPE) | 70-90 kg | [Fluorine chemistry](acids.md) — perfluoroolefin polymerization | No practical alternative for PFPE |
| Hydrogen gas (for hydrogenation) | 1-5 kg | [Chemistry](ammonia.md) — water electrolysis or SMR | None (hydrogenation is essential) |
| Additives (antioxidants, anti-wear) | 0.5-5 kg | [Chemistry](index.md) | Proprietary additive packages |

## Vacuum Oils

Vacuum technology demands lubricants with extremely low vapor pressure — the oil must not evaporate into the vacuum chamber and contaminate the process. Three classes of vacuum oil serve different pressure ranges.

**Mineral vacuum oil** (for roughing pumps): Highly refined, solvent-extracted mineral oil with vapor pressure ~10⁻² Pa at 25°C. Used in rotary vane and piston roughing pumps. These oils are distilled from selected crude fractions and treated to remove volatile components. Service life: 3-6 months in continuous operation, limited by oxidation and contamination with process gases. Cost: moderate. Suitable for rough vacuum (760-10⁻³ Torr).

**Silicone vacuum oil** (for diffusion pumps): Polydimethylsiloxane (PDMS) with specific viscosity grade (DC-704, DC-705 are common). Vapor pressure ~10⁻⁶ to 10⁻⁸ Pa at 25°C. The extremely low vapor pressure and thermal stability (operates at 150-200°C in the diffusion pump boiler) make silicone oil the standard diffusion pump fluid. Limitation: silicone oil contamination of vacuum chambers is extremely persistent — silicone films adhere to surfaces and cannot be removed by standard solvent cleaning. If silicone backstreaming occurs, chamber surfaces must be cleaned with potassium hydroxide solution or abrasive methods. Used for high vacuum (10⁻³ to 10⁻⁷ Torr).

**PAO vacuum oil** (for turbomolecular and scroll pumps): Synthetic hydrocarbon with vapor pressure ~10⁻⁶ Pa. Provides better lubrication than silicone oil for mechanical pump bearings and is easier to clean up if spilled. Increasingly used in dry (oil-free) pump backing applications and as a cleaner alternative to mineral oil in roughing pumps. Used for high and ultra-high vacuum backing (10⁻³ to 10⁻⁹ Torr).

**Vacuum oil properties comparison**:

| Oil Type | Vapor Pressure at 25°C | Max Operating Temp | Application | Pump Type | Typical Life |
|----------|------------------------|-------------------|-------------|-----------|-------------|
| Mineral vacuum | ~10⁻² Pa | 120°C | Rough vacuum | Rotary vane, piston | 3-6 months |
| Silicone (DC-704) | ~10⁻⁶ Pa | 200°C | High vacuum | Diffusion pump | 6-12 months |
| Silicone (DC-705) | ~10⁻⁸ Pa | 200°C | UHV | Diffusion pump (UHV) | 6-12 months |
| PAO synthetic | ~10⁻⁶ Pa | 175°C | HV/UHV backing | Turbo, scroll | 12-24 months |
| PFPE (Fomblin) | <10⁻¹⁰ Pa | 300°C | UHV, semiconductor | Dry pumps, bearings | 12-36 months |

## Scaling Notes

Synthetic lubricant production scales differently from mineral oil refining:

- **PAO**: Oligomerization is a batch or continuous process in a stirred reactor. A 1 m³ reactor produces ~500 kg of PAO per batch (8-12 hour cycle including catalyst removal and hydrogenation). Scaling is straightforward: larger reactors, more reactors in parallel. Minimum economic scale: ~100 tonnes/year (serves a regional market for specialty lubricants).

- **Ester oils**: Esterification is a straightforward acid-alcohol reaction with water as byproduct. Removal of water drives the reaction to completion. Batch production in glass-lined or stainless steel reactors at 150-250°C. Scale similar to batch chemical production.

- **Silicone oils**: Silicone production requires chlorosilane chemistry (methyl chloride + silicon at 300°C in a fluidized bed to produce dimethyldichlorosilane, then hydrolysis to form the polymer). This is a significant chemical infrastructure investment. Minimum practical scale: 1,000 tonnes/year for the silane intermediate production.

- **PFPE**: Fluorination chemistry is the most demanding. Perfluoroolefin photo-oxidation or anionic polymerization produces PFPE. The handling of toxic fluorinated intermediates (perfluoroisobutylene, hydrogen fluoride) requires specialized equipment and safety infrastructure. Production is concentrated in a few facilities worldwide. Not practical at small scale.

## Quality Control

Synthetic lubricant quality is verified by a battery of tests, most of which are standardized (ASTM, DIN, ISO):

1. **Kinematic viscosity** (ASTM D445): Capillary viscometer at 40°C and 100°C. Must fall within ±10% of the ISO VG grade specification.
2. **Viscosity index** (ASTM D2270): Calculated from 40°C and 100°C viscosities. PAO should show VI 130-150, confirming uniform molecular structure. Values below 120 suggest contamination with mineral oil.
3. **Flash point** (ASTM D92, Cleveland Open Cup): PAO 220-280°C, esters 220-310°C. Low flash point indicates volatile contaminants.
4. **Pour point** (ASTM D97): PAO -50 to -65°C. Higher pour point than specified indicates incomplete hydrogenation or contamination.
5. **Total acid number** (ASTM D974): Must be below 0.05 mg KOH/g for fresh synthetic oil. Higher values indicate oxidation or residual catalyst.
6. **Evaporation loss** (ASTM D972, Noack test): Weight loss after 1 hour at 250°C with air flow. PAO: <5%, ester: <10%. Higher losses indicate volatile fractions.
7. **Oxidation stability** (ASTM D943): Time to reach acid number 2.0 mg KOH/g at 95°C with oxygen and catalyst. PAO: 3000-4000+ hours vs. 1000-1500 for mineral oil. This test directly predicts service life.

**Quick field test**: Place a drop of oil on a clean glass plate and heat on a hot plate at 200°C for 30 minutes. Synthetic oil (PAO, ester) leaves minimal residue. Mineral oil leaves a dark, gummy deposit. Silicone oil leaves a white, powdery residue (silica from oxidation).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| PAO oil leaks from seals that held mineral oil | PAO causes shrinkage of nitrile (NBR) and neoprene seals | Replace seals with fluorocarbon (FKM/Viton) or polyurethane; blend PAO with 15-20% ester oil to restore seal swell |
| Silicone-lubricated bearing shows excessive wear | Silicone has poor metal-on-metal load-carrying capacity (low polar adsorption) | Switch to PAO or ester oil for loaded bearings; reserve silicone for light-load, wide-temperature-range applications (dashpots, electrical insulation) |
| PFPE grease dries out and fails in vacuum chamber | Grease thickener evaporated or PFPE migrated away from bearing surface | Use PFPE grease with PTFE thickener (not lithium soap, which outgasses); reapply every 6-12 months in continuous vacuum service; check for excessive bearing temperature (>250°C decomposes PFPE) |
| Ester hydraulic fluid turns acidic (pH <5) | Hydrolysis from water contamination at elevated temperature | Install desiccant breathers on reservoir; keep water content <200 ppm; drain, flush system, and refill; add hydrolysis stabilizer if available |
| Vacuum pump oil fails to reach target pressure | Oil vapor pressure too high for the vacuum level, or oil contaminated with process gases | Switch to lower vapor pressure oil (silicone for diffusion pumps, PAO for mechanical); degas oil by heating under vacuum before use; install foreline trap to prevent backstreaming |
| Diffusion pump silicone oil darkens and pumps lose speed | Oil cracked by thermal cycling or contaminated with reactive process gases | Replace silicone oil (typical life 6-12 months continuous); install cold trap above pump to catch backstreaming; avoid pumping aggressive solvents without trap |
| Synthetic cutting fluid leaves residue on machined parts | Ester-based fluid polymerizing at high cutting temperatures, or additive dropout | Reduce cutting temperature with higher coolant flow; switch to PAO-based cutting fluid for high-temperature operations; clean residue with isopropyl alcohol |
| Vacuum pump makes knocking noise with PAO oil | PAO viscosity too low for the pump at cold startup temperature | Use higher viscosity PAO grade (VG 46 or 68 instead of 32); install oil heater to warm reservoir to 30°C before startup; check pump clearances |


## Safety

Synthetic base stocks (PAO, ester, PAG) have low acute toxicity but prolonged skin contact causes defatting dermatitis — wear nitrile gloves. Additive packages contain anti-wear agents (zinc dialkyldithiophosphate — ZDDP), which hydrolyzes to hydrogen sulfide in contact with acids; H2S is lethal at 100 ppm. Synthetic ester fires burn at 400-600°C with dense smoke — store away from ignition sources. Polyalkylene glycol (PAG) spills create extremely slippery surfaces. Dispose of used lubricants through approved recycling channels.

## See Also

- **[Lubricants Overview](lubricants.md)**: Theory, selection guide, and cross-cutting topics
- **[Natural Lubricants](lubricants-natural.md)**: Animal fats and vegetable oils
- **[Mineral Oil Lubricants](lubricants-mineral.md)**: Petroleum-derived lubricants and fluids
- **[Grease & Solid Lubricants](lubricants-grease-solid.md)**: Grease production and solid lubricant coatings

## Variations and Alternatives

| Lubricant Type | Temp Range (°C) | Vapor Pressure | Cost vs Mineral | Best Application |
|---------------|----------------|----------------|----------------|-----------------|
| PAO | -65 to +180 | <10⁻⁶ Pa | 3-5× | Jet engines, Arctic machinery, long-drain automotive |
| Diester | -70 to +220 | ~10⁻⁴ Pa | 4-6× | Compressors, biodegradable hydraulics, two-stroke oils |
| Polyol ester | -55 to +250 | ~10⁻⁵ Pa | 5-8× | Jet engines (MIL-PRF-23699), high-temp industrial |
| Silicone (PDMS) | -70 to +280 | ~10⁻⁶ Pa | 8-15× | Diffusion pumps, dashpots, electrical insulation |
| PFPE | -80 to +300 | <10⁻¹⁰ Pa | 50-100× | Spacecraft, semiconductor mfg, oxygen service |
| Mineral oil (ref) | -30 to +150 | ~10⁻² Pa | 1× | General purpose, automotive, industrial gearboxes |

**When to choose synthetic over mineral**: Synthetic lubricants are justified when any of these conditions apply: (1) operating temperature exceeds 150°C or drops below -30°C; (2) extended oil drain intervals are needed (synthetic lasts 2-4× longer); (3) vacuum or cleanroom compatibility requires ultra-low vapor pressure; (4) the lubricated component is inaccessible for maintenance (sealed bearings, spacecraft mechanisms). For all other applications, mineral oil is adequate and 3-50× cheaper.

## Historical Context

Synthetic lubricants emerged from military and aerospace needs in the mid-20th century:

- **WWII era**: Diester lubricants developed for German jet engines (Me 262) because mineral oils degraded at the turbine temperatures encountered. This was the first large-scale use of synthetic lubricants.
- **1950s-1960s**: PAO development driven by US military needs for Arctic-grade lubricants (pour point below -50°C for operations in Alaska and Greenland). MIL-L-7808 and MIL-L-23699 specifications defined jet engine oil requirements.
- **1960s-1970s**: Silicone diffusion pump oils enabled the semiconductor industry's vacuum needs. DC-704 and DC-705 became standard fluids for high-vacuum deposition systems.
- **1970s-1980s**: PFPE development driven by space program needs (lubricants for spacecraft mechanisms that operate in vacuum for years without maintenance) and oxygen compressor safety (mineral oil + high-pressure oxygen = explosion).
- **1980s-present**: PAO became cost-competitive for automotive use, driving the consumer synthetic motor oil market. Ester-based biodegradable hydraulic fluids adopted for forestry and marine applications.

For a bootstrapping civilization, synthetic lubricants appear very late in the technology chain — they require petrochemical infrastructure (for PAO precursors), fluorine chemistry (for PFPE), or silicon metal production (for silicones). Natural and mineral lubricants serve 95% of lubrication needs. Synthetic lubricants become necessary only for jet engines, space hardware, ultra-high vacuum systems, and semiconductor manufacturing equipment.

## Integration Points

| Technology Domain | Synthetic Lubricant Used | Why Synthetic is Required |
|-------------------|------------------------|--------------------------|
| Aerospace (jet engines) | PAO + ester blends | -50°C cold start to 200°C cruise temperature range |
| Vacuum technology | Silicone (diffusion pumps), PFPE (UHV) | Vapor pressure below 10⁻⁶ Pa; mineral oil outgasses excessively |
| Semiconductor manufacturing | PFPE grease, PAO vacuum oil | Ultra-low outgassing prevents wafer contamination |
| Oxygen compressors | PFPE only | Mineral oil + high-pressure O₂ detonates; PFPE is inert |
| Space mechanisms | PFPE | 10+ year life in vacuum without maintenance |
| Arctic operations | PAO | Pour point below -50°C; mineral oil solidifies |
| Cleanroom bearings | Ester or PAO | Low volatility, defined outgassing spec |

**Bootstrap ordering**: Natural lubricants (animal fats, vegetable oils) are available from Year 1 and serve 90% of lubrication needs through the entire bootstrap. Mineral oils become available once petroleum refining is established (Year 15-25). Synthetic lubricants are needed only when the civilization reaches jet engines, vacuum technology, or semiconductor manufacturing (Year 50+). The progression is: natural → mineral → synthetic, with each stage justified by specific performance demands that the previous stage cannot meet.

**Key takeaway**: A bootstrapping civilization should not invest in synthetic lubricant production until it has exhausted the capabilities of natural and mineral lubricants. The performance gap between mineral oil and PAO is meaningful only in extreme-temperature or extreme-vacuum applications. For bearings, gears, and hydraulic systems operating below 120°C and above atmospheric pressure, mineral oil is entirely adequate. Reserve synthetic lubricant development for the specific applications that demand it: jet engines, diffusion pumps, spacecraft, and semiconductor cleanrooms.

**Cost-benefit threshold**: Synthetic lubricants cost 3-100× more than mineral oil per liter. This premium is justified only when the cost of lubricant failure (equipment damage, process contamination, maintenance downtime) exceeds the lubricant cost by a wide margin. A jet engine that seizes at 40,000 feet destroys a $100M aircraft — the $500 difference between mineral and synthetic engine oil is trivial. A vacuum chamber contaminated with silicone backstreaming requires days of cleaning and delays $50,000 worth of wafer production — PFPE grease at $500/tube is cheap insurance. For a lathe in a workshop, mineral oil at $5/liter works perfectly well.

**Mixing caution**: Never mix synthetic and mineral lubricants without verifying compatibility. PAO and mineral oil are miscible (they mix physically) but the blend has intermediate properties — the synthetic advantage is diluted. Silicone oil is NOT miscible with mineral oil or PAO; attempting to mix them produces a cloudy, unstable emulsion that separates over time. PFPE is not miscible with any hydrocarbon lubricant. Before switching a system from one lubricant type to another, drain completely, flush with a compatible solvent, and refill with the new lubricant. Residual old lubricant (even 1-2% contamination) can cause seal incompatibility, additive precipitation, or foaming.

**Environmental considerations**: PAO and ester lubricants are biodegradable (ester > PAO), making them suitable for forestry and marine applications where spills could contaminate water. Silicone oils are not biodegradable but are chemically inert and non-toxic to aquatic life. PFPE is not biodegradable and extremely persistent in the environment — the same chemical inertness that makes it valuable as a lubricant means it does not break down. Disposal of PFPE requires incineration at >1200°C; landfill disposal is not recommended due to extreme persistence. Mineral oil spills are the most common industrial lubricant contamination event — a single hydraulic line failure can release 50-200 liters into soil or waterways. Containment berming around lubricant storage and dispensing areas is standard industrial practice, with 110% containment capacity (a 200 L drum requires a berm holding 220 L).

*For a bootstrapping civilization, synthetic lubricants represent the final tier of lubrication technology — powerful but unnecessary until extreme applications demand them.*

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [Lubricants](lubricants.md)*
