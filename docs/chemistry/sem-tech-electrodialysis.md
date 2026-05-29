# SEM Tech Electrodialysis: Electrochemical Ion Separation

> **Node ID**: chemistry.sem-tech-electrodialysis
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.sem-tech`](sem-tech.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`chemistry.chemical-recovery`](chemical-recovery.md), [`chemistry.sem-tech-acid-regeneration`](sem-tech-acid-regeneration.md), [`chemistry.sem-tech-lithium-separation`](sem-tech-lithium-separation.md)
> **Timeline**: Years 20-35
> **Outputs**: separated_ions, desalted_water, concentrated_brine
> **Critical**: No — electrodialysis enables efficient ion separation but requires SEM Tech membranes and electricity

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech](sem-tech.md)) enable electrodialysis (ED) as a practical separation technology well before conventional fluoropolymer membranes become available. While SEM Tech's primary application is chlor-alkali electrolysis, the same membrane manufacturing process — pulverizing pre-functionalized resin beads in a PVC/CPVC binder — produces membranes suitable for electrodialysis at less than $1 per square foot.

## Overview

Electrodialysis is an electrochemical separation process that uses ion exchange membranes and an electric field to transport ions from one solution to another. Unlike electrolysis, which drives redox reactions at electrodes to produce new chemical species, electrodialysis performs purely physical ion transport — no chemical reaction occurs at the electrodes beyond minor water splitting at the boundary membranes. The goal is separation, not synthesis.

The Rowow LLC Technical Volume (lines 82-84) describes the discovery of related electro-separation approaches, including electrodialysis and a multi-cell configuration that enables single-stage elemental separation. Combined with the SEM Tech patent's specialized ion resins for selectivity (patent line 105), this positions electrodialysis as a key downstream technology enabled by the SEM Tech membrane platform.

## Electrodialysis Principles

Electrodialysis works by applying a direct current across a stack of alternating cation and anion exchange membranes placed between two electrodes:

- **[Anode](../glossary/anodes.md)** (positively charged electrode): attracts anions (negatively charged ions)
- **[Cathode](../glossary/cathode.md)** (negatively charged electrode): attracts cations (positively charged ions)
- **Cation exchange membranes (CEM)**: permit passage of cations, block anions
- **Anion exchange membranes (AEM)**: permit passage of anions, block cations

When an electric field is applied, cations migrate toward the cathode and anions toward the anode. The alternating membrane stack creates two types of channels: **diluate** channels (where ions are removed, producing purified water) and **concentrate** channels (where ions accumulate, producing brine). Critically, no electrolysis of the feed solution occurs — the ions simply move through the membranes under electrical force.

The only electrode reactions are minor water splitting at the boundary membranes, which produces small amounts of hydrogen and oxygen gas. This means energy consumption is dominated by ion transport, not by electrochemical conversion, making ED inherently more energy-efficient than electrolysis for separation tasks.

## Multi-Cell Configuration

A practical electrodialysis stack consists of many membrane pairs arranged in series between two electrodes:

**Cell pair components** (one repeating unit):
1. Cation exchange membrane (CEM)
2. Diluate channel (feed solution losing ions)
3. Anion exchange membrane (AEM)
4. Concentrate channel (receiving ions)

A commercial stack may contain 100-600 cell pairs. The voltage drop across each pair is small (0.5-1.5V), so the total stack voltage scales linearly with the number of pairs. Current density typically ranges from 10-50 mA/cm² depending on feed concentration and membrane properties.

**Strengths**: No electrochemical reactions at electrodes (only ion transport) — inherently more energy-efficient than electrolysis for separation; SEM Tech membranes at <$1/ft² make ED economically viable before fluoropolymer chemistry; 100-600 cell pairs per stack provide massive throughput in compact footprint; purely physical separation — no chemical addition to feed stream; simultaneous diluate (purified water) and concentrate (brine) production.

**Weaknesses**: Membrane fouling by organics, scale, and colloids requires periodic cleaning; multivalent cations (Ca²⁺, Mg²⁺) can precipitate in concentrate channels; spacer gaskets (0.5-2 mm) are flow restrictions that create pressure drop; current efficiency decreases at very low or very high feed concentrations; requires stable DC power supply and careful voltage control to avoid water splitting.

**Flow configuration**: Diluate and concentrate solutions flow through their respective channels in parallel, typically in a tortuous-path or sheet-flow spacer design. Solutions are recirculated until the desired level of ion removal or concentration is achieved.

**Spacer gaskets**: Thin polymeric mesh spacers (0.5-2mm thick) separate the membranes and create flow channels. These spacers also promote turbulent mixing at the membrane surface, reducing concentration polarization — the buildup of depleted or enriched ion layers that impede transport.

## SEM Tech Membrane in ED

The SEM Tech membrane manufacturing process (see [SEM Tech](sem-tech.md)) produces both membrane types needed for electrodialysis:

**Cation exchange membranes**: Manufactured from strong acid cation resin (sulfonic acid functional groups, R-SO₃H). These are the same resin beads used in SEM Tech chlor-alkali cells. The membrane selectively transports cations (Na⁺, K⁺, Ca²⁺, Mg²⁺, etc.) while blocking anion passage.

**Anion exchange membranes**: Manufactured from strong base anion resin (quaternary ammonium functional groups, R-N⁺(CH₃)₃). The same SEM Tech manufacturing process — pulverize, mix with PVC/CPVC binder, cast, dry — works with anion resin beads to produce anion-selective membranes.

**Specialized selectivity**: The SEM Tech patent describes specialized ion resins that can be tuned for selectivity toward specific ions (patent line 105). For electrodialysis, this enables membranes with preferential transport of target ions — for example, monovalent-selective membranes that pass Na⁺ while blocking Ca²⁺ and Mg²⁺, or proton-selective membranes for acid recovery.

**Speculative status**: While SEM Tech cation membranes have been demonstrated in chlor-alkali cells at TRL 5, complete electrodialysis stacks with matched cation-anion membrane pairs have not yet been built or tested. The theoretical performance is well-established from conventional ED practice, but SEM Tech membrane properties in multi-cell ED configurations (resistance per cell pair, ion selectivity in stacked geometry, long-term fouling behavior) remain to be characterized experimentally.

## Process Variants

### Conventional Electrodialysis (ED)

Standard ED for desalination and ion concentration. Feed solution passes through diluate channels; ions migrate to concentrate channels under applied voltage. Produces desalted water and concentrated brine simultaneously. See [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md) for desalination applications.

Typical performance:
- Salt removal: 50-95% per pass (multiple passes for higher removal)
- Water recovery: 75-90%
- Energy consumption: 0.5-3.0 kWh per cubic meter of product water (feed dependent)

### Reverse Electrodialysis (RED)

Reverse ED generates electricity from the mixing of fresh and salt water — the inverse of conventional ED. Concentrated brine and fresh water flow through alternate channels; the salinity gradient drives ion transport through the membranes, generating electrical current. This is salinity-gradient power, also called **[blue energy](../energy/sem-tech-blue-energy.md)**. See [SEM Tech Blue Energy](../energy/sem-tech-blue-energy.md).

RED viability depends critically on membrane cost, since large membrane areas are needed for modest power output. SEM Tech membranes at less than $1/sq ft could make RED economically feasible for the first time.

### Bipolar Membrane Electrodialysis (BMED)

Bipolar membranes consist of a cation exchange layer bonded to an anion exchange layer. Under applied voltage, water splits at the junction into H⁺ and OH⁻ ions. In a BMED stack, this produces acid and base from their corresponding salts without electrolysis:

- NaCl + H₂O → HCl + NaOH
- Na₂SO₄ + 2H₂O → H₂SO₄ + 2NaOH

This is directly relevant to [SEM Tech Acid Regeneration](sem-tech-acid-regeneration.md), where spent acid streams are reconcentrated for reuse. BMED eliminates the need for electrode-driven electrolysis in acid-base production.

## Operating Parameters

| Parameter | Conventional ED | RED | BMED |
|-----------|----------------|-----|------|
| **Voltage per cell pair** | 0.5-1.5V | N/A (generates voltage) | 1.0-3.0V |
| **Current density** | 10-50 mA/cm² | 1-10 mA/cm² | 10-50 mA/cm² |
| **Feed TDS** | 1,000-10,000 mg/L | Seawater + fresh | Salt solutions |
| **[Temperature](../glossary/temperature.md)** | 20-40°C | 15-30°C | 25-45°C |
| **Flow velocity** | 5-15 cm/s | 1-5 cm/s | 5-10 cm/s |
| **Recovery rate** | 75-90% | N/A | 80-95% |
| **Energy (ED)** | 0.5-3.0 kWh/m³ | Generates 0.5-2.0 W/m² | 1.0-5.0 kWh/kg acid |

**Key operating considerations**:
- **Concentration polarization**: At high current densities, ion depletion at the membrane surface limits transport. Spacer design and flow velocity manage this effect.
- **Scaling**: Divalent ions (Ca²⁺, Mg²⁺) can precipitate as carbonates or hydroxides on membrane surfaces. Pre-treatment or periodic polarity reversal (electrodialysis reversal, EDR) mitigates scaling.
- **Membrane fouling**: Organic matter and colloids foul membranes over time. Cleaning-in-place (CIP) with acid and alkali solutions restores performance.

## Membrane Stack Construction

A SEM Tech electrodialysis stack is constructed from readily available materials using simple fabrication techniques consistent with the SEM Tech design philosophy.

**Stack frames**: PVC or CPVC sheets (3-6 mm thick) cut to form the spacer gaskets that define flow channels. Holes drilled for inlet and outlet manifolds. Frame dimensions typically 200-500 mm × 400-1,000 mm for practical stacks. The frames are assembled with PVC cement (solvent welding) — the same technique used in plumbing — to create leak-tight seals between membranes and frames.

**Electrodes**: Graphite plates (5-10 mm thick) or coated titanium mesh at each end of the stack serve as anode and cathode. Graphite is inexpensive ($5-20 per kg) but slowly erodes; coated titanium (DSA) costs $200-500 per kg but lasts 5-8 years. For ED, where electrode reactions are minimal, graphite is acceptable with replacement every 1-2 years.

**End plates**: Thick PVC or steel plates (15-25 mm) clamp the stack together with tie rods. Compression force: 0.5-2.0 MPa distributed evenly across the membrane area to prevent internal leakage between diluate and concentrate channels.

**Assembly sequence**: (1) Place anode electrode on end plate. (2) Stack alternating CEM, diluate spacer, AEM, concentrate spacer until desired cell pair count is reached. (3) Place cathode electrode. (4) Install end plate with tie rods. (5) Torque tie rods evenly to specified compression. (6) Connect manifolds, power supply, and recirculation pumps. A 100-cell-pair stack with 0.1 m² active area per cell can be assembled by one person in 2-4 hours.

## Step-by-Step Procedure

### Phase 1: Fabricate Ion Exchange Membranes

1. **Source cation exchange resin**: Strong acid cation resin beads (sulfonated polystyrene, gel or macroporous, IEC 1.8-2.2 meq/g). If pre-functionalized beads are unavailable, chloromethylate polystyrene beads and sulfonate with concentrated H₂SO₄ at 80-100°C for 4-8 hours. Wash until effluent pH >5.
2. **Source anion exchange resin**: Strong base anion resin beads (quaternary ammonium functional groups, IEC 1.2-1.8 meq/g). Type I (trimethylamine) or Type II (dimethylethanolamine). Same SEM Tech manufacturing process applies.
3. **Pulverize resin**: Ball-mill each resin type separately to <200 μm particle size. Use ceramic or plastic media — metal media contamination degrades ion exchange performance. Sieve to remove particles >250 μm. Target: 80% of particles between 50-150 μm.
4. **Prepare binder solution**: Dissolve PVC or CPVC resin (K-value 55-65) in THF at 15-20% w/v concentration. Stir until fully dissolved (2-4 hours). CPVC preferred for higher temperature tolerance.
5. **Mix membrane slurry (CEM)**: Combine cation resin powder (40-60% by volume) with PVC binder solution. Mix on a planetary mixer for 30-60 minutes to achieve uniform dispersion. Degas under vacuum to remove entrapped air bubbles.
6. **Mix membrane slurry (AEM)**: Repeat step 5 with anion resin powder. Keep CEM and AEM slurries in clearly labeled separate containers — cross-contamination destroys selectivity.
7. **Cast membranes**: Using a drawdown bar or adjustable film applicator, cast each slurry onto a clean glass plate at 200-400 μm wet thickness. Target dry thickness: 100-200 μm. For thicker membranes (higher mechanical strength, higher resistance), cast at 400-600 μm wet.
8. **Dry and cure**: Air-dry for 2-4 hours until solvent evaporates. Peel membrane from glass plate. Post-condition in 1M NaCl solution for 12-24 hours to hydrate the resin phase and activate ion exchange sites. Rinse with deionized water. Store moist until use.

### Phase 2: Fabricate Stack Components

9. **Cut spacer gaskets**: Cut PVC or CPVC sheets (0.5-2.0 mm thick) to frame dimensions (e.g., 250 mm × 500 mm outer, 200 mm × 400 mm inner window). Drill manifold holes (inlet/outlet, 6-10 mm diameter) at corresponding positions on each frame. Diluate and concentrate frames have manifold holes on opposite sides to route flows through correct channels.
10. **Prepare electrodes**: Cut graphite plates to match frame dimensions (200 mm × 400 mm active area). Drill or machine tab connections for power supply attachment. Clean surfaces with isopropanol. For longer life, coat anode with mixed metal oxide (RuO₂/IrO₂ on Ti expanded mesh) — but graphite is acceptable for ED where electrode reactions are minimal.
11. **Cut end plates**: Prepare two thick PVC or steel plates (15-25 mm) with bolt holes matching the stack bolt pattern. Machine a recess for the electrode and a gasket groove for sealing.

### Phase 3: Assemble the ED Stack

12. **Layout and alignment**: Place bottom end plate on a flat surface. Position anode electrode in the recess. Place a rubber or PVC gasket around the electrode perimeter.
13. **Stack cell pairs**: For each cell pair, place in order: (a) CEM membrane, (b) diluate spacer frame (manifold on diluate side), (c) AEM membrane, (d) concentrate spacer frame (manifold on concentrate side). Align manifold holes precisely — misaligned holes block flow.
14. **Install cathode**: After the last cell pair, place the cathode electrode with a gasket.
15. **Clamp**: Place top end plate. Insert tie rods through bolt holes. Hand-tighten all nuts in a star (cross) pattern. Then torque to 0.5-2.0 MPa in 3-4 incremental passes, maintaining even compression. Uneven compression causes internal leakage between diluate and concentrate channels.
16. **Pressure test**: Connect a water supply to the diluate inlet. Flow deionized water at low pressure (0.1-0.3 bar). Check all seams and manifold connections for leaks. Tighten as needed. Repeat for concentrate channel.

### Phase 4: Connect Systems and Commission

17. **Connect plumbing**: Install two separate recirculation loops — one for diluate and one for concentrate. Each loop: feed tank → circulation pump (mag-drive or diaphragm, 5-50 L/min) → stack inlet manifold → stack outlet → back to tank. Install flow meters, pressure gauges, and sampling ports on both loops.
18. **Connect power supply**: Connect a DC power supply (0-100V, 0-50A for bench-scale) to the electrodes. Positive terminal to anode, negative to cathode. Verify polarity with a multimeter before energizing — reversed polarity damages membranes.
19. **Prepare feed solutions**: Fill diluate tank with the solution to be treated (e.g., brackish water at 3,000-5,000 mg/L TDS). Fill concentrate tank with a starting solution at similar concentration (or deionized water for initial operation). Volume: 10-50 liters per tank for bench-scale.
20. **Start recirculation**: Turn on both circulation pumps. Verify flow through both channels — no flow indicates blocked manifolds. Adjust flow to 5-15 cm/s channel velocity (typical: 1-5 L/min for bench-scale stack). Verify no cross-leakage by checking conductivity in both tanks with pumps running but power OFF.
21. **Apply voltage**: Set power supply to constant current mode. Start at 5 mA/cm² (low). Gradually increase to target current density (10-30 mA/cm²). Monitor stack voltage — expect 0.5-1.5V per cell pair. A 20-cell-pair stack at 1.0V/pair = 20V total.
22. **Monitor performance**: Track diluate conductivity (should decrease over time) and concentrate conductivity (should increase). Measure product quality every 15-30 minutes. Typical batch desalination run: 30-120 minutes depending on starting TDS and target purity.
23. **Shutdown**: When target conductivity is reached, turn off power supply, then turn off pumps. Drain and rinse both circuits with deionized water. Store membranes moist (do not let dry out — dried membranes crack and lose performance).

### Phase 5: Maintenance and Cleaning

24. **Routine cleaning (weekly)**: Circulate 0.1M HCl through both channels for 30 minutes to dissolve carbonate and hydroxide scale. Rinse with deionized water. Then circulate 0.1M NaOH for 30 minutes to remove organic fouling. Rinse thoroughly.
25. **Polarity reversal (EDR mode)**: For scaling-prone feeds, reverse electrode polarity every 15-30 minutes. This reverses ion transport direction, dissolving nascent scale deposits before they harden. Requires a reversible DC power supply and double-throw valve arrangement to swap diluate and concentrate streams.
26. **Membrane replacement**: SEM Tech membranes are inexpensive enough to replace semi-annually or annually. Disassemble stack, remove old membranes (recycle by grinding into filler), clean frames, install fresh membranes, reassemble. Total time: 2-4 hours for a bench-scale stack.

## Cost Comparison with Conventional ED

| Component | Conventional ED Stack | SEM Tech ED Stack |
|-----------|----------------------|-------------------|
| Cation membrane (per m²) | $100-300 (Neosepta CMX) | $10 (SEM Tech) |
| Anion membrane (per m²) | $100-300 (Neosepta AMX) | $10 (SEM Tech) |
| Bipolar membrane (per m²) | $200-500 (Fumasep FBM) | $15 (SEM Tech, projected) |
| 100-cell-pair stack, 0.5 m²/cell | $20,000-60,000 membranes | $1,000 membranes |
| Stack hardware (PVC frames, electrodes) | $5,000-10,000 | $2,000-5,000 |
| **Total stack cost** | **$25,000-70,000** | **$3,000-6,000** |
| Membrane replacement (100 m², annual) | $10,000-30,000 | $1,000 |
| Stack lifetime (membranes) | 2-5 years | 0.5-1 year (projected) |
| Annualized membrane cost | $4,000-15,000 | $1,000 |

Despite shorter projected lifetime, SEM Tech membranes deliver 4-10x lower annualized membrane cost. The key trade-off is more frequent replacement (semi-annually or annually versus every 2-5 years), offset by the trivial cost of new membranes.

## Applications

**Desalination**: Brackish water desalination is the largest commercial ED application. ED excels at moderate salinity (1,000-10,000 mg/L TDS) where reverse osmosis becomes energy-intensive. See [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md).

**Acid and base production**: BMED converts salt solutions into their constituent acids and bases. Useful for regenerating spent pickling acids, producing organic acids, and generating NaOH without chlor-alkali electrolysis. See [SEM Tech Acid Regeneration](sem-tech-acid-regeneration.md).

**Metal recovery**: ED concentrates metal ions from dilute waste streams (electroplating rinse water, mining leachate) for recovery by electrowinning or precipitation. Selective membranes enable separation of mixed metal streams.

**Food processing**: Demineralization of whey, deacidification of fruit juices, salt removal from soy sauce. ED preserves flavor compounds that thermal processes would destroy.

**Blue energy**: Reverse ED generates electricity from river-sea water mixing at estuaries. Global theoretical potential exceeds 2 TW. See [SEM Tech Blue Energy](../energy/sem-tech-blue-energy.md).


## Energy Consumption Analysis

The energy consumption of electrodialysis is determined by the number of ions transported and the electrical resistance of each cell pair. The theoretical minimum energy to remove salt from water is the Gibbs free energy of mixing. For desalting from 5,000 to 500 mg/L TDS (NaCl), the theoretical minimum is approximately 0.11 kWh/m³. Practical ED systems consume 0.5-2.0 kWh/m³, achieving 5-18% thermodynamic efficiency — the remaining energy is dissipated as resistive heating (I²R losses) in the solution and membranes.

**Resistance breakdown per cell pair** (typical 0.5 mm spacer, 5,000 mg/L NaCl feed at 25°C):
- Diluate channel solution resistance: 3-8 Ω·cm²
- Concentrate channel solution resistance: 2-5 Ω·cm²
- Cation membrane resistance: 1-5 Ω·cm² (SEM Tech estimated: 3-15 Ω·cm²)
- Anion membrane resistance: 1-5 Ω·cm² (SEM Tech estimated: 3-15 Ω·cm²)
- **Total per cell pair**: 7-23 Ω·cm² (conventional), 11-43 Ω·cm² (SEM Tech estimated)

At a current density of 20 mA/cm² (200 A/m²), a conventional cell pair at 15 Ω·cm² drops 0.3V, while a SEM Tech cell pair at 27 Ω·cm² drops 0.54V. For a 200-cell-pair stack, total voltage is 60V (conventional) versus 108V (SEM Tech). At 20 mA/cm² across 0.5 m² active area, total current is 100A. Power consumption: 6.0 kW (conventional) versus 10.8 kW (SEM Tech) — approximately 80% higher for SEM Tech, translating to 0.9 kWh/m³ additional energy cost. At $0.08/kWh, this adds $0.07/m³ to the water treatment cost — acceptable for most applications.

## Cross-Domain Dependencies

Electrodialysis using SEM Tech membranes requires upstream capabilities from multiple domains. The membranes themselves require PVC or CPVC resin from the [chlor-alkali and petrochemical industry](electrolysis.md), ion exchange resin beads (sulfonated polystyrene from [organic synthesis](./index.md)), and organic solvents (THF, MEK, cyclohexanone). The stack hardware requires [PVC plumbing components](../chemistry/index.md) and [graphite or titanium electrodes](../metals/index.md). The DC power supply requires [rectifier-grade electrical infrastructure](../energy/electricity.md) converting AC to DC at 50-600V. For water treatment applications, pre-treatment requires [sand filtration](../water/index.md) and possibly [activated carbon](../chemistry/index.md) for organic removal. For BMED applications, the acid and base products require [chemical-resistant storage vessels](../chemistry/index.md) and standard industrial chemical handling infrastructure.


## Scaling Considerations

**Bench-scale ED (0.1-1.0 m² membrane area)**: 5-20 cell pairs, operating at 5-20 mA/cm², 5-30V total stack voltage. Processes 0.5-5 L/h of feed solution. Suitable for laboratory research, water quality testing, and small-scale demonstration. Total membrane cost at SEM Tech pricing: $0.10-1.00.

**Pilot-scale ED (1-50 m² membrane area)**: 20-100 cell pairs, operating at 10-30 mA/cm², 20-150V. Processes 50-500 L/h. Suitable for field trials, small community water treatment (serving 50-500 people at 50 L/person/day), and industrial process water for small facilities. Total membrane cost: $1-50.

**Industrial-scale ED (50-1,000 m² membrane area)**: 100-600 cell pairs in one or more stacks, operating at 20-50 mA/cm², 50-600V. Processes 5-100 m³/h. Suitable for municipal brackish water desalination, industrial wastewater treatment, and mining process water. Total membrane cost: $50-1,000 — compared to $50,000-300,000 for conventional membranes at equivalent area.

**Large municipal ED (1,000-10,000 m² membrane area)**: Multiple parallel stack trains with common manifolds and power supply. Processes 100-1,000 m³/h (serving 20,000-200,000 people). Requires automated cleaning-in-place (CIP) systems, redundant stacks for continuous operation during maintenance, and sophisticated process control. Total membrane cost at SEM Tech pricing: $1,000-10,000 — a transformative reduction from the $500,000-3,000,000 cost of conventional membrane installations.

At each scale, the SEM Tech membrane cost is so low relative to other system components (power supply, pumps, piping, controls) that membrane replacement becomes a routine maintenance item rather than a capital decision — fundamentally changing the economics of ED deployment.
## Safety

- **Electrical safety**: ED stacks operate at high DC voltages (50-600V depending on cell pairs). Proper grounding, insulation, and lockout/tagout procedures are mandatory. Current leakage through improperly sealed cells can cause electrolysis and gas generation.
- **Chemical handling**: Concentrate streams may contain high concentrations of acids, bases, or salts. Standard chemical handling PPE (goggles, gloves, aprons) required when handling concentrate solutions.
- **Acid/base exposure**: BMED produces concentrated acid and base streams simultaneously. Cross-contamination from leaking membranes can cause vigorous neutralization reactions with heat generation. Pressure monitoring on product streams detects membrane failures.
- **Hydrogen gas**: Minor hydrogen evolution occurs at the cathode. Ensure adequate ventilation in enclosed stack installations to prevent flammable gas accumulation.
- **Membrane degradation**: Degraded membranes can release resin particles or binder material into product streams. Monitor product water quality with conductivity sensors.

## Limitations

**Speculative technology status**: SEM Tech membranes have been validated for chlor-alkali electrolysis (TRL 5), but full electrodialysis stacks using SEM Tech membranes have not been demonstrated. Key unknowns: membrane resistance in thin multi-cell stacks, long-term ion selectivity under continuous ED operation, fouling and cleaning behavior, and matched performance between cation and anion SEM Tech membranes.

**Not suitable for high-TDS feeds**: Conventional ED becomes uneconomical for seawater desalination (>35,000 mg/L TDS) because resistive losses increase with concentration. Reverse osmosis is preferred for seawater; ED excels at brackish water.

**Membrane replacement cost**: Although SEM Tech membranes are inexpensive, large ED stacks require hundreds of square meters. Membrane lifetime in ED service (months to years) determines operating cost.

**Divalent ion limitations**: Standard ion exchange membranes do not distinguish well between monovalent and divalent ions. Selective membranes (monovalent-selective) add complexity and cost, though SEM Tech's tunable resin approach may address this.

**No non-ionic contaminant removal**: ED removes only charged species. Suspended solids, organic molecules, and microorganisms pass through the channels unchanged. Pre-treatment (filtration, activated carbon) is needed for complete water purification.

## See Also

- [SEM Tech Ion Exchange Membrane](sem-tech.md) — parent article on SEM Tech membrane manufacturing and properties
- [Water Treatment](../water/sem-tech-water-treatment.md) — desalination and water purification applications
- [Acid Regeneration](sem-tech-acid-regeneration.md) — acid-base recovery via bipolar membrane electrodialysis
- [Blue Energy](../energy/sem-tech-blue-energy.md) — reverse electrodialysis for salinity-gradient power generation

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
