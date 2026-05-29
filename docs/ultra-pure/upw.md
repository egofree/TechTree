# Ultra-Pure Water (UPW) Production

> **Node ID**: ultra-pure.upw
> **Domain**: [Ultra-Pure Materials](./index.md)
> **Dependencies**: [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md), [Polymers](../polymers/index.md), [Energy](../energy/index.md)
> **Enables**: [High-Purity Chemicals](high-purity-chemicals.md), [Analytical Verification](analytical-verification.md)
> **Timeline**: Years 40-70
> **Outputs**: ultra_pure_water
> **Tags**: materials=[water, chemicals], era=semiconductor

## Overview

Ultra-pure water (UPW) is the single most consumed material in semiconductor fabrication — a typical wafer fab uses 5-10 million liters per day. UPW must achieve **18.2 MΩ·cm resistivity** at 25°C (theoretical maximum for pure water), with total organic carbon (TOC) below 1 ppb, dissolved oxygen below 5 ppb, particles smaller than 0.05 μm removed, and metallic impurities at sub-ppt concentrations. A single 0.1 μm particle on a wafer can destroy an entire die at advanced nodes.

Standard water treatment (see [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md)) produces drinking water at <500 mg/L TDS — roughly 3-4 orders of magnitude above semiconductor requirements. UPW production is a multi-stage process chain where each stage targets specific contamination classes: suspended solids → dissolved ions → organic molecules → dissolved gases → bacteria and particles → trace metals.

## Purity Requirements

### Semiconductor UPW Specifications (SEMI F63)

| Parameter | Specification | Measurement Method |
|-----------|--------------|-------------------|
| **Resistivity** | 18.2 MΩ·cm at 25°C | Inline conductivity cell |
| **TOC** | <1 ppb (μg/L) | UV oxidation + conductivity |
| **Dissolved oxygen** | <5 ppb | Membrane electrode |
| **Particles (≥0.05 μm)** | <100 per mL | Laser particle counter |
| **Particles (≥0.1 μm)** | <10 per mL | Laser particle counter |
| **Silica (dissolved)** | <0.5 ppb | Colorimetric (molybdate blue) |
| **Bacteria** | <1 CFU/100 mL | Membrane filtration + culture |
| **Bacterial endotoxins** | <0.03 EU/mL | LAL (Limulus amebocyte lysate) |
| **Total metals** | <1 ppt (each) | ICP-MS |
| **Anions (Cl⁻, SO₄²⁻)** | <0.1 ppb each | Ion chromatography |
| **Cations (Na⁺, K⁺, Ca²⁺)** | <0.1 ppb each | Ion chromatography |

### Why Each Parameter Matters

**Resistivity 18.2 MΩ·cm**: The theoretical maximum resistivity of pure water at 25°C is 18.18 MΩ·cm. Any dissolved ionic species — even at ppb levels — lowers resistivity below this threshold. Achieving 18.2 MΩ·cm proves total ionic purity.

**TOC <1 ppb**: Dissolved organic carbon leaves carbonaceous residues on wafer surfaces during rinsing. These residues act as dopants, create nucleation sites for defects, and interfere with photoresist adhesion. A single ppb of TOC corresponds to roughly 10¹³ organic molecules per liter.

**Dissolved oxygen <5 ppb**: Dissolved oxygen forms native oxide on bare silicon surfaces. In gate oxide growth (<10 nm), uncontrolled oxide thickness variation of even 0.1 nm shifts transistor threshold voltage. DO control is critical for thermal oxidation uniformity.

**Particles <0.05 μm**: At 28 nm node and below, a 0.05 μm particle can bridge adjacent lines causing a short circuit, or block an etch creating an open circuit. Particles are the leading cause of yield loss in semiconductor manufacturing.

**Silica <0.5 ppb**: Dissolved silica deposits as SiO₂ on wafer surfaces during drying. These deposits create unwanted insulation layers and interfere with subsequent process steps.

## Process Flow

A complete UPW system consists of five functional blocks: **pretreatment → primary purification → polishing → distribution → reclamation**.

### Block 1: Pretreatment

Pretreatment removes the bulk of contaminants from the feed water, protecting downstream purification equipment from fouling and overload. Feed water is typically municipal water or well water at 100-500 mg/L TDS.

**Media filtration**: Multi-layer depth filter (anthracite + sand + garnet) removes suspended solids >10 μm. Automatic backwash every 24-48 hours. Removes turbidity to <0.1 NTU.

**Activated carbon**: Granular activated carbon (GAC) bed removes free chlorine (which would irreversibly damage downstream RO membranes) and organic compounds. Chlorine removal to <0.1 ppm by GAC adsorption plus sodium bisulfite (NaHSO₃) injection as backup. Empty bed contact time (EBCT): 10-15 minutes.

**Water softening**: Strong acid cation exchange resin in sodium form removes hardness (Ca²⁺, Mg²⁺) to prevent RO membrane scaling. Regeneration with NaCl brine. Reduces hardness to <1 mg/L as CaCO₃.

**Cartridge filtration**: 5-10 μm polypropylene depth filter as final pretreatment barrier. Protects high-pressure RO pump from any remaining particles.

### Block 2: Primary Purification

Primary purification removes >99% of dissolved ions, organics, and particles through membrane-based separation.

**Strengths**:
- RO removes 95-99% of dissolved ions and 99% of organics >200 Da in a single pass
- EDI provides continuous ion removal without chemical regeneration downtime
- Membrane processes scale linearly — add more membrane modules for higher capacity

**Weaknesses**:
- RO requires 10-15 bar operating pressure — significant energy consumption for high-pressure pumping
- Membranes foul over time and require periodic cleaning or replacement (3-5 year life)
- EDI cannot achieve 18.2 MΩ·cm alone — requires downstream mixed-bed polishing

**Reverse osmosis (RO) — first pass**: Polyamide thin-film composite (TFC) membrane at 10-15 bar operating pressure. Rejects 95-99% of dissolved ions, 99% of organics >200 Da, and 99% of particles >0.01 μm. Permeate quality: 0.5-5 mg/L TDS, TOC <50 ppb. Recovery: 75-85%.

**RO — second pass (optional)**: A second RO pass on the first-pass permeate further reduces TDS to <0.1 mg/L and TOC to <10 ppb. Used when feed water is high in dissolved silica or boron.

**Electrodeionization (EDI)**: Continuous electrodeionization combines ion exchange resin with an electric field. The resin provides rapid ion transport pathways while the electric field continuously regenerates the resin in place — eliminating chemical regeneration. Product quality: 15-17 MΩ·cm, TOC <10 ppb. EDI produces consistent water quality without the regeneration downtime of conventional ion exchange.

**Degasification**: Membrane contactor degasification removes dissolved CO₂ (which forms carbonic acid and lowers resistivity) and dissolved oxygen. Hollow-fiber hydrophobic membrane with vacuum or nitrogen sweep on the shell side. Reduces DO to <50 ppb, CO₂ to <1 ppm.

### Block 3: Polishing

Polishing removes the last traces of contaminants to reach semiconductor-grade purity. Each polishing stage targets a specific contaminant class.

**Strengths**:
- Mixed-bed ion exchange achieves 18.0-18.2 MΩ·cm resistivity — the final ion barrier
- UV oxidation reduces TOC by 50-90% and provides continuous bacterial control
- Ultrafiltration at 10 nm pore size removes bacteria, endotoxins, and colloidal silica

**Weaknesses**:
- Mixed-bed resin exhausts in months and must be regenerated or replaced off-site
- UV lamps degrade over 6-12 months — 185 nm output diminishes affecting TOC removal
- UF membranes require automatic backwash every 15-30 minutes, consuming product water

**Mixed-bed ion exchange**: Strong acid cation + strong base anion exchange resins in a single vessel. Removes the final traces of dissolved ions that pass through EDI. Product resistivity: 18.0-18.2 MΩ·cm. The mixed-bed is the final ion barrier — when its effluent resistivity drops below 18.0 MΩ·cm, the resin is exhausted and must be replaced or regenerated off-site.

**UV oxidation (185 nm + 254 nm)**: Low-pressure mercury vapor UV lamps produce simultaneous 185 nm (oxidizing) and 254 nm (bactericidal) wavelengths. The 185 nm radiation produces hydroxyl radicals (·OH) from water, which oxidize trace organic compounds to CO₂ and H₂O. The 254 nm radiation kills bacteria and viruses. TOC reduction: typically 50-90% of remaining TOC. UV dose: >180 mJ/cm² at 254 nm for bacterial kill.

**Sub-micron filtration (ultrafiltration)**: Hollow-fiber ultrafiltration membrane with 0.01 μm (10 nm) nominal pore size removes:
- Bacteria and bacterial fragments (prevents biofilm in distribution)
- Colloidal silica particles
- Any resin fines or particulates from upstream ion exchange
- Endotoxins and pyrogens (bacterial cell wall fragments)

Typical configuration: Two UF units in parallel (one online, one in backwash/standby). Automatic backwash every 15-30 minutes with UPW product water.

**Final polish — TOC reduction**: For systems requiring TOC <0.5 ppb, a final 185 nm UV-TOC reduction unit provides the last organic removal step. This stage also provides continuous bacterial control at the point of distribution.

### Block 4: Distribution

The distribution system must deliver UPW from the polishing loop to point-of-use (POU) without contaminating it. This is arguably the hardest engineering challenge in UPW — maintaining purity during transport.

**Loop design**: Continuous recirculating loop with no dead legs. Water velocity 1.5-3.0 m/s (turbulent flow prevents biofilm). No low-flow or stagnant zones. All connections use orbital-welded joints or sanitary clamp fittings.

**Piping materials**: PFA (perfluoroalkoxy) or PVDF (polyvinylidene fluoride) — both ultra-low extractable fluoropolymers. PVC, CPVC, and polypropylene leach organic extractables at ppb levels and are NOT acceptable for UPW distribution. All wetted surfaces must be electropolished to Ra <0.4 μm.

**Storage tanks**: Vertical cylindrical HDPE or PVDF-lined tanks with nitrogen blanket (prevents CO₂ and O₂ absorption). Tank design: conical bottom for complete drainability, spray ball for CIP (clean-in-place). No headspace — nitrogen pad maintains positive pressure and excludes atmosphere.

**Point-of-use (POU) filters**: 0.05 μm membrane capsule filters at each tool connection. PES (polyethersulfone) or nylon membrane. Replaced on differential pressure (>0.3 bar) or time (3-6 months).

**Temperature control**: UPW is distributed at 22-25°C for most applications. For advanced photoresist processing, heated UPW at 60-80°C may be required — this needs dedicated heated loops with PFA piping.

### Block 5: Reclamation

Modern fabs reclaim 60-80% of used UPW. Reclaimed water is treated and recycled, reducing both water consumption and wastewater discharge.

**Collection**: Used rinse water from wafer processing tools is segregated by contamination type. HF-containing streams are separated (fluoride must be removed before recycling). Other streams are combined for reclamation treatment.

**Treatment**: Reclaimed water passes through activated carbon (organic removal) → UV oxidation (TOC) → mixed-bed ion exchange (ions) → sub-micron filtration (particles) → returned to UPW pretreatment feed.

**Zero liquid discharge (ZLD)**: In water-scarce regions, reverse osmosis concentrate and other waste streams are evaporated and crystallized to eliminate liquid discharge. Energy-intensive (25-40 kWh/m³ of concentrate) but eliminates wastewater.

## System Sizing

### Small Fab (1,000 wafers/month, 200mm)

- UPW demand: ~200,000 L/day
- Pretreatment: 2 × 10 m³/hr media filters + 2 × 10 m³/hr GAC beds
- RO: 2 × 10 m³/hr TFC membrane skids (1 duty + 1 standby)
- EDI: 2 × 10 m³/hr modules
- Polishing: 2 × mixed-bed vessels + 2 × UV units + 2 × UF units
- Distribution loop: 500 m of 25 mm PFA piping
- Capital cost: $500,000-$1,500,000

### Large Fab (50,000 wafers/month, 300mm)

- UPW demand: ~5,000,000 L/day
- Full multi-stage system with dual-train redundancy
- RO concentrate recovery to achieve 95%+ water reclamation
- Capital cost: $10,000,000-$30,000,000

## Materials of Construction

Every material that contacts UPW must be evaluated for extractables and leachables at ppb/ppt levels.

| Component | Acceptable Material | Unacceptable Material |
|-----------|-------------------|----------------------|
| Piping | PFA, PVDF, electropolished 316L SS | PVC, CPVC, PP, carbon steel |
| Tanks | PVDF-lined, HDPE (lined), 316L SS (electropolished) | Unlined steel, concrete |
| Pumps | PFA-lined, ceramic, PTFE | Cast iron, bronze |
| Valves | PFA/PTFE diaphragm valves | Ball valves (dead legs), gate valves |
| Gaskets | PTFE, Kalrez (FFKM) | EPDM, Viton (leach organics) |
| Filter housings | 316L SS (electropolished), PFA | Polypropylene (extractables) |
| Membranes | Polyamide (RO), PES (UF), PVDF (MF) | Cellulose acetate (bacterial food) |
| UV sleeves | High-purity fused silica | Borosilicate glass (extractables) |

## Monitoring and Control

Continuous inline monitoring is essential for UPW quality assurance. The system must detect and alarm on any excursion within minutes.

| Parameter | Instrument | Alarm Threshold | Location |
|-----------|-----------|-----------------|----------|
| Resistivity | Toroidal conductivity cell | <18.0 MΩ·cm | After mixed-bed, distribution loop |
| TOC | UV-persulfate oxidation + conductivity | >1 ppb | After UV-TOC, distribution loop |
| Particles | Laser light scattering (0.05-0.2 μm) | >100/mL (0.05 μm) | Distribution loop, POU |
| Flow | Magnetic flow meter | ±10% of setpoint | Distribution loop |
| Pressure | Sanitary pressure transmitter | <1.0 bar (low flow alarm) | Distribution loop |
| Temperature | RTD or thermocouple | Outside 22-25°C | Distribution loop |
| DO | Membrane electrode | >5 ppb | After degas, distribution loop |
| pH | Glass electrode (sanitary) | Outside 6.5-7.5 | After mixed-bed |

## Troubleshooting

### Resistivity Below 18.2 MΩ·cm

**Causes**: Mixed-bed ion exchange exhaustion. RO membrane degradation (salt passage increase). CO₂ absorption through tank headspace. Piping leak introducing atmospheric CO₂.

**Resolution**: Replace mixed-bed resin. Check RO rejection rate (should be >98%). Verify nitrogen blanket on storage tanks. Pressure-test distribution loop for leaks.

### TOC Excursion (>1 ppb)

**Causes**: UV lamp failure (185 nm output degrades over 6-12 months). New piping component releasing organics (insufficient flushing). Bacterial bloom in stagnant zone. Activated carbon exhaustion in pretreatment.

**Resolution**: Replace UV lamps (schedule annually). Flush new components for 24-48 hours before commissioning. Check loop flow velocity (must maintain >1.5 m/s). Replace GAC if chlorine breakthrough detected.

### High Particle Counts

**Causes**: UF membrane breach. Distribution pipe corrosion. Pump seal wear generating particles. Construction debris in new piping. Bacterial growth (biofilm sloughing).

**Resolution**: Integrity-test UF membranes (bubble point test). Inspect pump seals. Flush and sanitize loop. Verify no dead legs in piping. Sanitize with hot water (80°C) or hydrogen peroxide (3%).

### Bacterial Contamination

**Causes**: Insufficient UV dose. Stagnant water in dead legs. Biofilm establishment in low-flow zones. Contaminated replacement filters or resin.

**Resolution**: Sanitize entire loop with hot UPW (80°C for 2 hours) or ozone (0.5-1.0 ppm for 30 minutes). Eliminate dead legs. Verify UV lamp output with radiometer. Use only pre-sterilized replacement components.

## Cross-Domain Dependencies

- **[Water Treatment](../water/sem-tech-water-treatment.md)**: Provides pretreated feed water (RO permeate or deionized water at <10 mg/L TDS) as UPW system input.
- **[Chemistry / Electrolysis](../chemistry/electrolysis.md)**: Chlorine for pretreatment disinfection (or alternative). Sodium bisulfite for dechlorination.
- **[Polymers](../polymers/index.md)**: PFA, PVDF, PTFE piping and seals. Polyamide RO membranes. PES UF membranes.
- **[Cleanrooms](../photolithography/cleanrooms.md)**: UPW system must be housed in or adjacent to the cleanroom to minimize distribution length and contamination risk.
- **[Energy](../energy/index.md)**: UPW production consumes 2-5 kWh/m³. A large fab UPW system draws 500-1500 kW continuous power.
- **[Measurement](../measurement/index.md)**: Inline resistivity, TOC, particle, and DO instruments for continuous quality monitoring.

## Limitations

- **Energy intensive**: UPW production consumes 2-5 kWh/m³. RO alone requires 2-4 kWh/m³ for high-pressure pumping. A large fab's UPW system is a major electricity consumer.
- **Membrane replacement**: RO membranes last 3-5 years. UF membranes last 1-3 years. Mixed-bed resin is exhausted in months and must be regenerated off-site or replaced. Annual membrane and resin replacement cost: 10-20% of system capital cost.
- **No margin for error**: A single excursion in any parameter can contaminate wafers in process. The system requires 100% uptime — redundant trains on all critical components.
- **Water consumption**: Even with 70-80% reclamation, a large fab still consumes 1-2 million liters per day of fresh feed water. In water-scarce regions, this is a significant operational constraint.
- **Microbial control**: Bacteria grow even in 18.2 MΩ·cm water (oligotrophic organisms). Continuous UV, ozone, or hot water sanitization is mandatory. Biofilm removal once established requires aggressive chemical cleaning.

## See Also

- [High-Purity Chemicals](high-purity-chemicals.md) — 9N+ chemical purification for semiconductor processing
- [Analytical Verification](analytical-verification.md) — PPT-level analysis and contamination detection
- [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md) — ED desalination for brackish water
- [Cleanrooms](../photolithography/cleanrooms.md) — Contamination-controlled environments for wafer processing
- [Solvents](../chemistry/solvents.md) — Industrial solvent production (predecessor to electronic-grade)

---

*Part of the [Bootciv Tech Tree](../index.md) | [Ultra-Pure Materials](./index.md) | [All Domains](../index.md)*
