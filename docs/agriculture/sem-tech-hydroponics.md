# SEM Tech Hydroponics: Electromembrane Nutrient and pH Control

> **Node ID**: agriculture.hydroponic-ph-control
> **Domain**: [Agriculture](./index.md)
> **Dependencies**: [`chemistry.sem-tech`](../chemistry/sem-tech.md), [`chemistry.sem-tech-electrodialysis`](../chemistry/sem-tech-electrodialysis.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 25-40
> **Outputs**: balanced_nutrient_solution
> **Critical**: No — this is an advanced optimization of hydroponic nutrient management; conventional hydroponics with manual pH adjustment is a functional alternative


The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech](../chemistry/sem-tech.md)) enable precise nutrient ion management in hydroponic growing systems. While SEM Tech's primary application is chlor-alkali electrolysis, the same membrane platform — pulverized pre-functionalized resin beads in a PVC/CPVC binder — can be applied to electrodialysis for controlled-environment agriculture.

Hydroponics grows plants in nutrient-enriched water without soil. Plants absorb macronutrients (nitrogen as NO₃⁻ or NH₄⁺, phosphorus as H₂PO₄⁻, potassium as K⁺) and micronutrients (Fe²⁺, Mn²⁺, Zn²⁺, Cu²⁺, B(OH)₄⁻, MoO₄²⁻) dissolved in water. Maintaining the correct ionic balance and pH (typically 5.5-6.5) is critical for plant health.

Conventional hydroponic systems manage nutrients and pH through manual addition of acid (phosphoric or nitric acid) or base (potassium hydroxide) to correct drift. This approach is imprecise, risks overcorrection, and generates waste when solution must be discarded due to accumulated imbalances. SEM Tech membranes, combined with a small electrodialysis (ED) unit (see [SEM Tech Electrodialysis](../chemistry/sem-tech-electrodialysis.md)), offer a continuous, electrochemical approach: selectively removing or adjusting ion concentrations without adding corrective chemicals.

Position in the dependency chain: SEM Tech hydroponics requires [SEM Tech membrane manufacturing](../chemistry/sem-tech.md), [electrodialysis system design](../chemistry/sem-tech-electrodialysis.md), and [electrical infrastructure](../energy/electricity.md). It represents a more advanced approach than [Aquaponics](aquaponics.md), which achieves similar results using biological processes (fish, bacteria) at much lower technological requirements.

**This article describes a speculative application.** No SEM-Tech-specific hydroponic data exists. The following describes a plausible application based on established electrodialysis principles and SEM Tech membrane capabilities.

## Prerequisites

**Materials**:
- Ion exchange resin beads: strong acid cation resin (sulfonic acid, R-SO₃H) and strong base anion resin (quaternary ammonium, R-N⁺(CH₃)₃)
- PVC or CPVC resin (binder for membranes)
- Organic solvent (THF, cyclohexanone, or MEK) for membrane casting
- PVC or CPVC sheet (3-6 mm) for stack spacer gaskets
- Graphite plates (5-10 mm) for electrodes
- Polyethylene mesh (0.5-2 mm) for spacers

**Tools and equipment**:
- Blender or ball mill for resin pulverization (particle size below 200 microns)
- Flat casting surface (glass, metal, or acrylic, 30×30 cm minimum)
- Blade or drawdown bar for membrane spreading
- [DC power supply](../energy/electricity.md) (0-30V, 1-5A adjustable)
- pH probe and EC (conductivity) sensor
- Microcontroller or comparator circuit for automated control

**Knowledge**:
- Electrodialysis principles (ion migration under DC voltage through ion-selective membranes)
- Hydroponic nutrient solution chemistry (Hoagland solution composition, EC targets, pH management)
- Membrane casting technique (resin-binder mixing, solvent evaporation)
- Stack assembly and compression (gasket sealing, manifold routing)

**Infrastructure**:
- Functioning hydroponic system with recirculating nutrient reservoir (200-2,000 L)
- [Electrical supply](../energy/electricity.md) producing at least 50W DC continuous
- Workshop space for membrane fabrication and stack assembly
- [SEM Tech membrane manufacturing capability](../chemistry/sem-tech.md)

## Bill of Materials

## Membrane Materials (10 cell pairs, 200 cm² active area)

| Material | Quantity | Source | Notes |
|----------|----------|--------|-------|
| Strong acid cation exchange resin beads | 100-200 g | Water treatment suppliers | Pre-functionalized sulfonic acid (R-SO₃H) type |
| Strong base anion exchange resin beads | 100-200 g | Water treatment suppliers | Pre-functionalized quaternary ammonium (R-N⁺(CH₃)₃) type |
| PVC or CPVC resin (pellets or powder) | 50-100 g | Plumbing supply, [Chemistry](../chemistry/index.md) | Binder matrix for membranes |
| Organic solvent (THF, cyclohexanone, or MEK) | 200-500 mL | [Chemistry → Solvents](../chemistry/solvents.md) | For dissolving PVC/CPVC binder |

## Stack Hardware Materials

| Material | Quantity | Source | Notes |
|----------|----------|--------|-------|
| PVC or CPVC sheet (3-6 mm thick) | 0.5-1.0 m² | Plumbing supply | Spacer gaskets and stack frames |
| PVC cement (solvent weld) | 1 small can | Plumbing supply | Sealing stack joints |
| Graphite plates (5-10 mm thick) | 2 pieces, ~200 cm² each | [Materials](../metals/index.md) or industrial supply | Anode and cathode electrodes |
| Polyethylene mesh or netting (0.5-2 mm) | 0.5 m² | Hardware store | Spacer material between membranes |
| Tie rods with nuts and washers (stainless steel) | 4-8 sets, 200-300 mm length | [Metals](../metals/index.md) or hardware | Stack compression |
| Thick PVC or steel end plates (15-25 mm) | 2 pieces | [Metals](../metals/index.md) or hardware | Stack end compression plates |

## Plumbing and Integration Materials

| Material | Quantity | Source | Notes |
|----------|----------|--------|-------|
| PVC tubing or hose (6-12 mm ID) | 2-5 m | Hardware store | Side-stream plumbing |
| Small submersible or inline pump (5-20 L/min) | 1 unit | [Electronics](../electronics/index.md) or commercial | Side-stream circulation |
| Food-grade HDPE tanks (5-20 L) | 2-3 units | General supply | Concentrate and reservoir tanks |
| Hose barbs, connectors, valves | Assorted | Hardware store | Plumbing connections |
| Sediment filter (50-100 micron) | 1 unit | Water filter supply | Downstream particulate capture |

## Process Description

## 4.1 Membrane Fabrication

Follow the SEM Tech membrane manufacturing process (see [SEM Tech](../chemistry/sem-tech.md) for full details).

1. **Pulverize resin beads**: Reduce cation exchange resin beads to fine powder (below 200 microns) using a blender or ball mill. If wet pulverizing is used, dry the powder thoroughly before proceeding. Repeat with anion exchange resin beads in a separate batch.
2. **Prepare binder solution**: Dissolve PVC or CPVC resin in THF, cyclohexanone, or MEK at approximately 3:7 polymer-to-solvent ratio by weight. Stir until fully dissolved and homogeneous.
3. **Cast cation exchange membrane (CEM)**: Mix pulverized cation resin powder into the binder solution at approximately 50% loading by volume. Stir until homogeneous. Spread onto the flat casting surface using a blade or drawdown bar to achieve 100-300 micron wet thickness. Allow to dry at ambient temperature until solvent has fully evaporated (2-24 hours depending on solvent and conditions). Peel the finished CEM from the surface.
4. **Cast anion exchange membrane (AEM)**: Repeat Step 3 using pulverized anion exchange resin powder. The process is identical — only the resin feedstock changes.
5. **Cut membranes**: Cut each membrane to the active area required for the ED stack (approximately 200 cm² per membrane for a medium-scale system). Cut 10 CEM pieces and 10 AEM pieces for a 10-cell-pair stack.

**Strengths**:
- Membrane casting uses ambient-temperature drying — no thermal curing or specialized equipment
- Cost per membrane pair: approximately $0.22 at SEM Tech pricing (<$1 per square foot)
- Both CEM and AEM use the same PVC/CPVC binder — only the resin powder changes between types

**Weaknesses**:
- Resin must be pulverized to below 200 microns — requires a blender or ball mill (1-2 hours of processing)
- Organic solvents (THF, MEK, cyclohexanone) are required — these may not be available until [organic chemical synthesis](../chemistry/index.md) is established
- Membrane quality depends on uniform resin-binder mixing — poor mixing produces areas of variable ion transport

## 4.2 ED Stack Assembly

1. **Prepare spacer gaskets**: Cut PVC or CPVC sheet into rectangular frames that define the flow channels. Each frame has an open center (the active membrane area) and holes at opposite ends for inlet/outlet manifolds. Prepare two types: diluate spacers and concentrate spacers, differing only in manifold hole placement.
2. **Assemble the stack**: On a flat surface, build up the stack in this repeating sequence from anode to cathode:
   1. Place anode (graphite plate)
   2. CEM
   3. Diluate spacer gasket
   4. AEM
   5. Concentrate spacer gasket
   6. Repeat steps 2-5 for each cell pair (10 times total)
   7. Place final CEM
   8. Place cathode (graphite plate)
3. **Compress and seal**: Place thick end plates on both sides. Thread tie rods through corner holes and tighten nuts evenly in a cross-pattern. Apply PVC cement to the frame joints as you assemble to create leak-tight solvent-welded seals. Do not overtighten — aim for firm, even compression across the entire membrane area.
4. **Connect plumbing**: Attach inlet and outlet manifolds to the diluate and concentrate ports using PVC cement. Connect the side-stream pump to draw nutrient solution from the main reservoir through the diluate channels, and return it. Connect the concentrate loop to a small HDPE collection tank.
5. **Connect power and sensors**: Wire the DC power supply to the anode and cathode. Install the pH probe and EC sensor in the main hydroponic reservoir. Connect sensors to the microcontroller, and wire the output to control the DC power supply.

**Strengths**:
- Stack assembly uses standard plumbing materials and PVC cement — no specialized manufacturing equipment
- 10-cell-pair stack with 200 cm² membranes costs approximately $30-73 total (dominated by power supply and sensors, not membranes)
- Stack housing (PVC frame, end plates) is reusable across multiple membrane replacements

**Weaknesses**:
- Stack assembly requires precise alignment of spacer gaskets and membranes — misalignment causes internal leakage between diluate and concentrate channels
- PVC cement fumes are toxic — assembly must be done in a well-ventilated area
- Compression must be even across the entire stack — overtightening tears membranes, undertightening causes leaks

## 4.3 System Operation

1. **Calibrate sensors**: Calibrate pH probe using standard buffer solutions (pH 4.0, 7.0, 10.0). Calibrate EC sensor using standard KCl solution. Set target thresholds: pH 5.8-6.2 (or crop-specific range), EC 1.5-3.0 mS/cm (or crop-specific target).
2. **Start the side-stream pump**: Begin circulating nutrient solution through the ED stack at 5-20 L/min. Check all connections for leaks. Verify flow through both diluate and concentrate channels.
3. **Activate ED when correction is needed**: When pH or EC drifts outside the target range, the microcontroller activates the DC power supply. Set initial voltage to 10V and current limit to 2A. Monitor pH and EC during correction — a typical correction cycle takes 20-60 minutes for a 1,000 L reservoir with moderate drift.
4. **Monitor concentrate tank**: As the ED removes excess ions, they accumulate in the concentrate tank. When concentrated (EC > 5.0 mS/cm), it can be stored for later re-dosing when specific nutrients are depleted.
5. **Perform routine maintenance**: Every 14-30 days, clean the ED stack in place:
   - Flush with 0.1M NaOH solution (4 g/L) at 2-3 L/min for 15-30 minutes to remove organic deposits.
   - If inorganic scaling is present, precede with 0.05M HCl (1.8 g/L) for 15 minutes.
   - Rinse with deionized water for 10 minutes.
   - Return to service.
6. **Replace membranes as needed**: At projected 6-12 month intervals in organic-rich hydroponic service, disassemble the stack, peel old membranes, cast new membranes from fresh resin-binder mixture, and reassemble. Total membrane replacement cost: $2-5. Reuse the PVC stack housing and plumbing.

**Strengths**:
- Automated operation requires no daily human intervention — microcontroller triggers ED based on sensor thresholds
- Energy cost per correction cycle: approximately $0.001-0.003 in electricity — effectively negligible
- Extended nutrient solution life (months vs. weekly replacement) reduces water and mineral salt waste by 80-95%

**Weaknesses**:
- Requires continuous sensor calibration — pH probes drift and need recalibration every 2-4 weeks
- Organic fouling from root exudates increases membrane resistance 10-40% over 30-60 days, requiring regular CIP cleaning
- Membrane replacement every 6-12 months — each replacement requires 2-4 hours of disassembly, casting, and reassembly

## 4.4 pH Stabilization

pH drift in hydroponics results from differential ion uptake. Plants absorbing more cations than anions release H⁺, lowering pH. Conversely, excess anion uptake releases HCO₃⁻/OH⁻, raising pH.

Electrochemical pH stabilization uses proton-selective membranes (a specialized SEM Tech membrane variant using cation resin tuned for H⁺ selectivity) to remove excess H⁺ or OH⁻ ions:
- **pH too low** (excess H⁺): ED transports protons out of the nutrient solution into a waste or concentrate stream.
- **pH too high** (excess OH⁻): ED transports hydroxide out, or equivalently, transports H⁺ into the solution from a separate acid reservoir.

This replaces conventional pH correction (manual addition of phosphoric acid or potassium hydroxide) with a continuous process that does not introduce additional ions. Electrochemical pH control can hold pH within ±0.1 units, compared to ±0.5 units typical of manual dosing.

**Strengths**:
- pH precision of ±0.1 units — 5× more precise than manual dosing at ±0.5 units
- No corrective chemicals added to nutrient solution — avoids unwanted ion introduction (e.g., phosphorus from phosphoric acid)
- Automated pH maintenance eliminates daily manual measurement and dosing labor

**Weaknesses**:
- Requires proton-selective membrane variant — standard CEM may not achieve sufficient H⁺/Na⁺ selectivity
- pH sensor accuracy limits system precision — sensor drift of ±0.1 pH units equals the entire control band
- Power outage during pH correction allows drift to continue uncontrolled until power returns

## 4.5 Nutrient Ion Management

In a recirculating hydroponic system, plants selectively absorb ions at different rates. Nitrogen is consumed rapidly; calcium and sulfate accumulate. Over time, the solution drifts from its target composition. Electromembrane-based management addresses this by:
- **Selective ion removal**: An ED stack can extract excess ions (accumulated Ca²⁺, SO₄²⁻, Na⁺) from the nutrient solution, restoring balance without full replacement.
- **Nutrient recovery**: Concentrated ions removed from the main loop can be stored and re-dosed when depletion occurs, closing the nutrient loop.
- **Crop transitions**: When switching crops in the same system (e.g., lettuce to tomato), the ED module selectively adjusts the full ion profile over 2-4 hours for a 1,000 L system, eliminating the need to dump and mix a completely new solution.

**Strengths**:
- Eliminates nutrient solution replacement — continuous ion adjustment keeps the same solution in service for months
- Crop transitions (lettuce → tomato) take 2-4 hours instead of requiring a full solution dump — saves 800-1,000 L of water per transition
- Concentrated ion stream can be stored and re-dosed, recovering 80-95% of mineral nutrients that would otherwise be wasted

**Weaknesses**:
- Non-selective ED co-removes micronutrients (iron, manganese, zinc, copper at 0.5-5 mg/L) along with target ions — may require staged operation or selective membranes
- Does not remove pathogens — separate UV, ozone, or biological treatment is required for disease management
- Ion transport rate at 10 mA/cm² across 200 cm²: 26.8 meq/min — adequate for gradual correction but too slow for rapid emergency adjustments

## Quantitative Parameters

## Membrane Specifications for Hydroponic ED

| Parameter | CEM (Cation) | AEM (Anion) |
|-----------|-------------|-------------|
| Functional group | Sulfonic acid (R-SO₃H) | Quaternary ammonium (R-N⁺(CH₃)₃) |
| Resin ion exchange capacity | 1.8-2.2 meq/mL | 1.0-1.4 meq/mL |
| Membrane thickness | 100-300 microns | 100-300 microns |
| Target ion transport | K⁺, Ca²⁺, Mg²⁺, NH₄⁺, Fe²⁺, Mn²⁺ | NO₃⁻, H₂PO₄⁻, SO₄²⁻, Cl⁻, HCO₃⁻ |
| Cost per 200 cm² membrane | ~$0.11 | ~$0.11 |
| Estimated area resistance | 20-50 Ω·cm² | 20-50 Ω·cm² |

## ED System Operating Parameters

| Parameter | Small (50-200 L) | Medium (200-2,000 L) | Large (2,000-20,000 L) |
|-----------|------------------|----------------------|------------------------|
| Cell pairs | 5 | 10-20 | 20-50 |
| Active area per membrane | 100 cm² | 200-500 cm² | 500-2,000 cm² |
| Current density | 5-10 mA/cm² | 10-20 mA/cm² | 15-30 mA/cm² |
| Total current | 0.5-1.0 A | 2-10 A | 7-60 A |
| Stack voltage | 2.5-7.5 V | 5-30 V | 10-60 V |
| Side-stream flow | 1-2 L/min | 5-20 L/min | 20-100 L/min |
| Correction cycle time | 30-90 min | 20-60 min | 20-60 min |
| Total membrane cost | $1-3 | $5-15 | $15-50 |

## Nutrient Solution Ion Transport Rates

| Ion | Concentration in Hoagland Solution | Transport Rate at 2A (10 cell pairs) | Time to Reduce 50 mg/L Ca²⁺ in 500 L |
|-----|------------------------------------|---------------------------------------|--------------------------------------|
| K⁺ | 234 mg/L (6 mM) | 1.07 g/min | — |
| Ca²⁺ | 160 mg/L (4 mM) | 0.54 g/min | 46 minutes |
| NO₃⁻ | 1,000 mg/L (16 mM) | 1.08 g/min | — |
| SO₄²⁻ | 192 mg/L (2 mM) | 0.97 g/min | — |

## Cost Analysis

| Component | Cost |
|-----------|------|
| SEM Tech membranes (20 pieces) | $2-5 |
| PVC/CPVC stack housing | $3-8 |
| DC power supply (0-30V, 5A) | $10-25 |
| pH probe + EC sensor | $8-15 |
| Microcontroller or comparator | $2-5 |
| Tubing, fittings, small pump | $3-10 |
| Concentrate tank (10L HDPE) | $2-5 |
| **Total capital cost** | **$30-73** |

| Operating Parameter | Manual Acid/Base Dosing | SEM Tech ED Management |
|---------------------|------------------------|------------------------|
| Annual chemical cost | $20/year (acid + base) | $0 (electricity only) |
| Annual water waste | 13,000 L (biweekly replacement) | 2,000 L (semi-annual replacement) |
| Annual nutrient waste | $45 (dumped with solution) | $25 (reduced waste) |
| Annual membrane replacement | — | $2.20 |
| Annual CIP chemicals | — | $5-10 |
| **Total annual operating cost** | **~$130/year** | **~$43/year** |

## Scaling Notes

**Small-scale (50-200 L reservoir)**: Single ED module with 5 cell pairs, 100 cm² active area per membrane. Suitable for hobby greenhouses and research growth chambers. Processes 1-2 L/min of side-stream flow. Full correction cycle: 30-90 minutes.

**Medium-scale (200-2,000 L reservoir)**: 10-20 cell pairs, 200-500 cm² active area per membrane. Suitable for commercial greenhouses and multi-rack vertical farms. Correction cycle: 20-60 minutes. Total membrane cost: $5-15 per stack.

**Large-scale (2,000-20,000 L reservoir)**: 20-50 cell pairs, 500-2,000 cm² active area. Requires proportionally larger power supply (30-60V, 10-60A). Membrane cost below $50 per stack. Suitable for hectare-scale greenhouse operations.

**Integration with solar power**: A 50W solar panel ($30-50) produces sufficient power for 8-20 correction cycles per day. A 12V, 20Ah lead-acid battery ($25-40) stores 2-3 days of backup power. Total off-grid power system: $80-130.

**Key bottleneck**: Organic solvent availability. Membrane fabrication requires THF, MEK, or cyclohexanone. These solvents require [organic chemical synthesis](../chemistry/index.md) capability that may not be available in early bootstrap scenarios.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| ED stack not correcting pH | Membrane fouling, electrode degradation, or sensor miscalibration | Clean stack (NaOH flush); check electrode connections; recalibrate pH probe with buffer solutions |
| Declining ion transport rate | Organic fouling increasing membrane resistance | Run CIP cleaning (0.1M NaOH for 15-30 min); increase cleaning frequency |
| Internal leakage between diluate and concentrate | Damaged spacer gasket or uneven compression | Disassemble stack; inspect gaskets; replace damaged components; recompress evenly |
| Excessive voltage required | Scaling (CaCO₃, CaSO₄) on membrane surfaces | Precede NaOH cleaning with 0.05M HCl flush for 15 min; check feed water hardness |
| Micronutrient depletion in nutrient solution | Non-selective ED co-removes micronutrients along with target ions | Add staged ED operation with selective membrane formulation; supplement micronutrients separately |
| Membrane tearing during assembly | Overtightening tie rods or uneven gasket surface | Hand-tighten nuts in cross-pattern; use torque-limiting technique; inspect membranes for defects before installation |

## Safety

- **Solvent handling during membrane fabrication**: THF, MEK, and cyclohexanone are flammable organic solvents with TLV-TWA values of 200-590 ppm. Use in well-ventilated areas away from ignition sources. THF forms explosive peroxides on prolonged storage — use fresh solvent or test for peroxides before use. Wear nitrile gloves and safety goggles when handling solvents.
- **Electrical safety near water**: The ED module operates at low DC voltage (5-30V) which presents minimal shock hazard, but all electrical connections must be waterproofed. Ground-fault circuit interrupters (GFCIs) are mandatory on the power supply. The ED module housing must be sealed and drip-proof.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode of the ED stack. At the small scale proposed (1-5A current), gas production is negligible (milliliters per hour) but adequate ventilation should be maintained in enclosed growing spaces. Hydrogen accumulates above 4% concentration in air (explosive range: 4-75%).
- **Concentrated nutrient solutions**: ED concentrate streams contain high levels of dissolved ions. Standard chemical handling practices apply: gloves, eye protection, and clearly labeled containers. Concentrated potassium hydroxide (used in some hydroponic formulations) is caustic and requires the same precautions as any strong base (pH >13 in concentrated form; causes chemical burns on skin contact).
- **Membrane integrity**: Degraded membranes could release resin particles into the nutrient solution. A sediment filter (50-100 micron) downstream of the ED module catches any particulate matter. Inspect filter monthly and replace when clogged.

## Quality Control

## ED Stack Performance Verification

| Parameter | Target | Test Method |
|-----------|--------|-------------|
| Diluate conductivity reduction per pass | 5-15% (at 10V, 2A) | Measure EC at inlet and outlet of diluate channel |
| pH correction rate | 0.1-0.3 pH units per 10 minutes | Time pH change from 6.5 to 6.0 with continuous ED operation |
| Concentrate EC increase | >1.0 mS/cm per correction cycle | Measure EC in concentrate tank before and after cycle |
| Stack pressure drop | <50 kPa at design flow rate | Pressure gauge at inlet and outlet |
| Membrane resistance increase | <20% per month (after CIP cleaning) | Measure stack voltage at constant current; compare to baseline |

## Nutrient Solution Quality Targets

| Parameter | Target Range | Out-of-Range Action |
|-----------|-------------|-------------------|
| pH | 5.5-6.5 | Activate ED pH correction |
| EC | 1.5-3.0 mS/cm (crop-dependent) | Activate ED ion removal or add nutrients |
| Calcium | 80-200 mg/L | Adjust via concentrate re-dosing |
| Nitrate-N | 100-200 mg/L | Supplement if depleted; remove excess via ED |
| Iron | 2-5 mg/L | Add chelated iron supplement (ED cannot selectively add iron) |

## Variations and Alternatives

## Nutrient Management Method Comparison

| Method | pH Precision | Annual Cost | Complexity | Water Waste |
|--------|-------------|------------|-----------|------------|
| Manual acid/base dosing | ±0.3-0.5 units | ~$130/year | Low | High (biweekly dump) |
| Automated dosing pumps | ±0.2-0.3 units | ~$200/year (equipment + chemicals) | Medium | High (biweekly dump) |
| SEM Tech ED control | ±0.1 units | ~$43/year | High | Low (semi-annual replacement) |
| [Aquaponics](aquaponics.md) (biological) | ±0.3-0.5 units | ~$50/year (fish food) | Medium (living system) | Very low (continuous recirculation) |

## Crop-Specific Nutrient Profiles

| Crop | EC Target (mS/cm) | pH Target | Key Nutrient Emphasis | Notes |
|------|-------------------|-----------|----------------------|-------|
| Lettuce | 1.0-2.0 | 5.5-6.5 | Moderate nitrogen | Low EC; sensitive to high salts |
| Tomato | 2.5-4.5 | 5.8-6.5 | Elevated potassium during fruiting | K⁺ at 8-12 mM during fruiting |
| Strawberry | 1.0-1.5 | 5.5-6.5 | Strict calcium management | Ca²⁺ at 4-6 mM to prevent tip burn |
| Cucumber | 2.0-3.0 | 5.5-6.0 | Balanced N-P-K | Fast growth; frequent correction needed |
| Herbs (basil, mint) | 1.0-2.0 | 5.5-6.5 | Moderate nitrogen | Continuous harvest; steady demand |

## See Also

- [SEM Tech Ion Exchange Membrane](../chemistry/sem-tech.md) — parent article on SEM Tech membrane manufacturing and properties
- [Electrodialysis](../chemistry/sem-tech-electrodialysis.md) — electrochemical ion separation using SEM Tech membranes
- [SEM Tech Water Treatment](../water/sem-tech-water-treatment.md) — desalination and water purification applications
- [Aquaponics](aquaponics.md) — lower-technology biological approach to nutrient and pH management
- [Chemistry → Solvents](../chemistry/solvents.md) — organic solvents required for membrane fabrication
- [Energy → Electricity](../energy/electricity.md) — electrical supply for ED stack operation
- [Electronics](../electronics/index.md) — pH probes, EC sensors, and microcontroller circuits



[← Back to Agriculture](index.md)
