# SEM Tech Acid Regeneration: Bipolar Membrane Electrodialysis for Acid Recovery

> **Node ID**: chemistry.sem-tech-acid-regeneration
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.sem-tech`](sem-tech.md), [`chemistry.sem-tech-electrodialysis`](sem-tech-electrodialysis.md)
> **Enables**: [`chemistry.chemical-recovery`](chemical-recovery.md), [`metals.finishing`](../metals/finishing.md)
> **Timeline**: Years 20-35
> **Outputs**: regenerated_acid, recovered_base
> **Critical**: No — acid regeneration reduces chemical waste and cost but does not enable new capabilities

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech](sem-tech.md)) enable acid recovery and regeneration via bipolar membrane electrodialysis (BMED), a process variant of [SEM Tech Electrodialysis](sem-tech-electrodialysis.md). Where conventional electrodialysis separates ions from water, BMED goes further: it splits water into protons and hydroxide ions at a membrane junction, producing concentrated acid and base from waste salt solutions without electrode-driven electrolysis.

## Overview

Industrial processes that use strong acids — steel pickling, mining leaching, chemical synthesis, metal surface treatment — generate enormous volumes of spent acid contaminated with dissolved metals, salts, and organic residues. Disposing of this waste is expensive, environmentally damaging, and represents a loss of valuable chemical feedstock. Acid regeneration recovers the acid from these waste streams for reuse, closing the material loop.

Bipolar membrane electrodialysis achieves this by combining two technologies: the ion-transporting membranes of conventional electrodialysis with bipolar membranes that split water into H⁺ and OH⁻ ions. The result is a purely electrochemical process that converts salt solutions back into their parent acid and base:

- NaCl + H₂O → HCl + NaOH
- Na₂SO₄ + 2H₂O → H₂SO₄ + 2NaOH
- FeCl₂ + 2H₂O → 2HCl + Fe(OH)₂

The Rowow LLC Technical Volume (lines 337-339) describes electrodialysis applied to acid/base separation, confirming that the SEM Tech membrane platform is designed to support this application alongside its primary chlor-alkali function.

## Acid Recovery Challenge

Acid waste is one of the largest-volume industrial waste streams worldwide. Major sources include:

**Steel pickling**: Hot-rolled steel is descaled by immersion in hydrochloric or sulfuric acid (15-20% concentration). The spent pickling liquor contains 2-5% free acid, 10-20% dissolved iron (as FeCl₂ or FeSO₄), and trace metals. A single mid-size steel plant generates 5,000-15,000 cubic meters of spent pickling liquor per year.

**Mining leachate**: Acid leaching of ores (particularly copper, uranium, and rare earth elements) produces spent leach solutions containing target metals at low concentration, residual acid, and high dissolved salt loads. These solutions are typically neutralized with lime, producing vast quantities of gypsum sludge for landfill disposal.

**Chemical process waste**: Organic synthesis, pharmaceutical manufacturing, and electroplating generate acid waste streams with mixed contaminants. Neutralization destroys the acid value and produces salt waste.

Current regeneration methods — thermal distillation, solvent extraction, ion exchange resin regeneration — each have drawbacks: high energy consumption, secondary waste generation, or limited recovery efficiency. BMED offers a direct electrochemical route that recovers both the acid and a useful base co-product.

## Bipolar Membrane Electrodialysis

BMED differs from conventional electrodialysis (see [SEM Tech Electrodialysis](sem-tech-electrodialysis.md)) by introducing bipolar membranes into the cell stack. A bipolar membrane consists of a cation exchange layer laminated to an anion exchange layer. Under applied voltage, water molecules at the internal junction dissociate into H⁺ and OH⁻ ions:

- **H₂O → H⁺ + OH⁻** (at bipolar membrane junction, driven by electric field)

This water-splitting reaction requires approximately 0.83V at the bipolar junction — far less than the 1.23V needed for electrode-driven water electrolysis. The H⁺ ions migrate toward the cathode through the cation exchange layer, and OH⁻ ions migrate toward the anode through the anion exchange layer.

**[Three-compartment BMED cell](../glossary/three-compartment-bmed-cell.md)** (one repeating unit):
1. **Acid compartment**: Receives H⁺ from the bipolar membrane. Salt anions (Cl⁻, SO₄²⁻) enter through the adjacent anion exchange membrane. Result: acid concentration increases.
2. **Base compartment**: Receives OH⁻ from the bipolar membrane. Salt cations (Na⁺, Fe²⁺) enter through the adjacent cation exchange membrane. Result: base concentration increases.
3. **Salt compartment**: Feed solution loses cations (to the base compartment) and anions (to the acid compartment). Result: salt is depleted.

A BMED stack contains many such repeating units between two electrodes. The electrodes serve only to apply the driving voltage; no electrochemical reaction occurs at the electrodes beyond minor water splitting.

**Strengths**: BMED regenerates both acid AND base from waste salt — dual product recovery; water splitting at bipolar junction requires only 0.83V (vs 1.23V for electrode electrolysis — 33% less energy); no electrode consumption or chlorine gas generation; SEM Tech membranes make BMED economically viable at <$1/ft² membrane cost; closes the material loop for steel pickling and metal finishing acids.

**Weaknesses**: Bipolar membrane fabrication is more complex than single-layer membranes (requires lamination of cation + anion layers); feed stream must be pre-filtered to prevent membrane fouling; iron and multivalent cations can precipitate as hydroxides in the base compartment (scaling); current efficiency decreases at higher acid/base concentrations (back-diffusion); membrane lifetime under BMED conditions not yet characterized for SEM Tech membranes.

## SEM Tech Membrane Application

The SEM Tech membrane manufacturing process (see [SEM Tech](sem-tech.md)) produces all three membrane types required for BMED:

**Cation exchange membranes**: Strong acid cation resin (sulfonic acid functional groups) in PVC/CPVC binder. Transports Na⁺, K⁺, and other cations from the salt compartment to the base compartment.

**Anion exchange membranes**: Strong base anion resin (quaternary ammonium functional groups) in PVC/CPVC binder. Transports Cl⁻, SO₄²⁻, and other anions from the salt compartment to the acid compartment.

**Bipolar membranes**: The critical component. A SEM Tech bipolar membrane would be fabricated by laminating a cation exchange layer to an anion exchange layer with an intermediate catalyst zone. The SEM Tech approach — pulverizing pre-functionalized resin beads in a polymer binder — lends itself to this layered construction: one layer cast with cation resin, one with anion resin, bonded while the binder is still soft from solvent evaporation.

The cost advantage is decisive. Conventional BMED stacks use bipolar membranes costing $200-500 per square meter. SEM Tech membranes at less than $1 per square foot ($10 per square meter) would reduce membrane capital cost by 20-50x, making BMED economically viable for applications that are marginal with conventional membranes.

**Speculative status**: SEM Tech BMED stacks have not been demonstrated. The bipolar membrane laminated construction is a logical extension of the SEM Tech manufacturing process but requires experimental validation. Water-splitting efficiency, long-term junction stability, and acid/base product purity using SEM Tech bipolar membranes all remain uncharacterized.

## Process Description

A BMED acid regeneration system converts spent acid waste into reusable acid and base co-products through a complete treatment train: **spent acid intake → pre-treatment → BMED stack → product handling → recycled acid/base**.

### Process Flow

1. **Spent acid intake**: Waste acid is collected from the industrial process (pickling line, leaching circuit, plating bath) in a holding tank. The composition is characterized for free acid content, dissolved metal concentration, and total dissolved solids.

2. **Pre-treatment**: Spent acid feed is filtered to remove suspended solids (cartridge filter, 5-10 micron) and optionally treated with activated carbon to reduce organic fouling potential. Dissolved metals that would interfere with membrane performance may be partially removed by pH-adjusted precipitation or ion exchange before entering the BMED stack. Iron-rich feeds benefit from pre-oxidation to convert Fe²⁺ to Fe³⁺, which precipitates more readily.

3. **BMED stack processing**: The pre-treated feed enters the salt compartments of the BMED stack. DC voltage is applied across the electrodes. In each cell triple:
   - Salt anions (Cl⁻, SO₄²⁻) migrate through the anion exchange membrane into the acid compartment
   - Salt cations (Na⁺, Fe²⁺) migrate through the cation exchange membrane into the base compartment
   - The bipolar membrane splits water, sending H⁺ to the acid compartment and OH⁻ to the base compartment
   - The salt compartment is progressively depleted of ions

4. **Product handling**:
   - **Regenerated acid**: 1-4 mol/L concentration (5-15% HCl or 5-20% H₂SO₄), collected in an acid-resistant storage tank (HDPE or glass-lined steel). Suitable for direct reuse in pickling, leaching, or chemical synthesis. If higher concentration is needed, blend with fresh acid or apply vacuum distillation.
   - **Recovered base**: 1-4 mol/L NaOH or KOH solution, collected in a separate tank. Usable for pH adjustment, metal precipitation, cleaning-in-place, or sale as industrial chemical.
   - **Depleted salt stream**: Low-concentration salt solution from the salt compartment, dischargeable to wastewater treatment or recyclable to the process.

5. **Recirculation**: For batch operation, the salt solution is recirculated through the stack until the target salt depletion is reached (typically 80-95% salt removal). Acid and base compartments are also recirculated to build concentration. For continuous operation, multiple stacks in series achieve the target conversion in a single pass.

### BMED Stack Configuration

**Typical configuration**:
- 50-200 cell triples (each triple = salt + acid + base compartment)
- Operating voltage: 1.0-3.0V per cell triple
- Current density: 10-50 mA/cm²
- Stack voltage: 100-600V DC depending on number of cell triples
- Membrane area: 10-100 m² depending on throughput

**Membrane arrangement per cell triple** (from anode to cathode):
1. Anion exchange membrane (AEM)
2. Acid compartment (with spacer)
3. Bipolar membrane (BPM)
4. Base compartment (with spacer)
5. Cation exchange membrane (CEM)
6. Salt compartment (with spacer, feed enters here)

This repeating unit is stacked 50-200 times between the anode and cathode electrodes. Electrode rinse water circulates through the electrode compartments to remove gas bubbles and heat.

### Comparison with Alternatives

| Method | Energy | Recovery Rate | Secondary Waste | Complexity |
|--------|--------|--------------|-----------------|------------|
| **BMED (SEM Tech)** | 1.5-3.0 kWh/kg acid | 80-92% | Minimal (depleted salt) | Moderate |
| **Thermal distillation** | 8-15 kWh/kg acid | 90-98% | Scale, residue | High |
| **Solvent extraction** | 2-5 kWh/kg acid | 85-95% | Spent solvent | High |
| **Neutralization + disposal** | Minimal | 0% | Gypsum sludge, salt water | Low |
| **Ion exchange resin** | 1-3 kWh/kg acid | 70-85% | Spent regenerant chemicals | Moderate |

BMED with SEM Tech membranes offers the best combination of energy efficiency, recovery rate, and low secondary waste generation at the lowest capital cost. The key advantage over neutralization is that the acid is *recovered for reuse* rather than destroyed.

## Bipolar Membrane Fabrication Details

The SEM Tech bipolar membrane is fabricated by a two-layer casting process that exploits the room-temperature solvent evaporation characteristic of the membrane platform. Unlike conventional bipolar membranes that require thermal lamination at 120-180°C under pressure, SEM Tech bipolar membranes can be assembled at ambient temperature.

**Layer 1 — Cation exchange layer**: Pulverized strong acid cation resin (sulfonated polystyrene, particle size below 200 microns) at 40-50% loading by volume in PVC/CPVC binder (dissolved in THF). Cast on a glass plate at 150-250 microns wet thickness. Allow partial drying (30-60 seconds) until the surface is tacky but not liquid.

**Layer 2 — Anion exchange layer**: Pulverized strong base anion resin (quaternary ammonium polystyrene, same particle size) at 40-50% loading in PVC/CPVC binder. Cast directly on top of the partially dried cation layer at matching thickness. The solvent in layer 2 softens the surface of layer 1, creating a molecular bond at the interface without additional adhesive.

**Catalyst zone**: An optional intermediate layer containing 0.1-1.0 mg/cm² of a water-splitting catalyst (FeCl₃, CrCl₃, or TiO₂ nanoparticles) dispersed in the PVC/CPVC binder solution, applied as a thin spray or brush coat between the two layers before the second layer is cast. The catalyst reduces the water-splitting overpotential from approximately 0.83V to 0.4-0.6V at the bipolar junction, improving energy efficiency by 25-50%.

**Total bipolar membrane cost**: At SEM Tech material pricing, a 1 m² bipolar membrane requires approximately 100 g of cation resin ($0.30), 100 g of anion resin ($0.40), 20 g of PVC/CPVC ($0.05), 200 mL of THF ($0.80), and catalyst ($0.05-0.50). **Total materials cost: approximately $1.60-2.05 per m²** — compared to $200-500/m² for commercial bipolar membranes from Fumatech or Astom Corporation.

## System Design Parameters

**Steel pickling acid recovery — detailed design**:

For a mid-size steel plant generating 10,000 m³/year of spent HCl pickling liquor (composition: 3% free HCl, 15% FeCl₂, 0.5% trace metals):

- **Feed rate**: 1.25 m³/h (assuming 8,000 operating hours/year)
- **BMED stack configuration**: 100 cell triples, each with 0.5 m² active membrane area. Total membrane area: 150 m² (50 m² each of cation, anion, and bipolar membranes).
- **Membrane cost**: At $10/m² for monopolar and $15/m² for bipolar SEM Tech membranes, total membrane cost: approximately $2,000. Conventional BMED membrane cost at equivalent area: $30,000-75,000.
- **Operating voltage**: 1.5-2.5V per cell triple, total stack voltage 150-250V DC
- **Current density**: 20-40 mA/cm² (2-4 kA/m²)
- **Power consumption**: 75-150 kW, yielding approximately 1.5-3.0 kWh/kg HCl recovered
- **Product streams**: Regenerated HCl at 2.0-3.5 mol/L (7-13%); NaOH at 2.0-3.0 mol/L (8-12%); depleted FeCl₂ solution at 1-3% for iron recovery or disposal
- **Acid recovery rate**: 80-92% of free HCl in the feed
- **Annual HCl recovered**: approximately 300-345 tonnes (from 375 tonnes in feed), valued at $45,000-70,000 at bulk HCl pricing of $150-200/tonne

## Operating Conditions and Performance

| Parameter | HCl Recovery | H₂SO₄ Recovery | Mixed Acid |
|-----------|-------------|----------------|------------|
| **Feed acid concentration** | 2-5% free HCl | 3-8% free H₂SO₄ | Variable |
| **Feed dissolved metals** | 10-20% FeCl₂ | 5-15% FeSO₄ | 1-10% mixed |
| **Product acid concentration** | 5-15% HCl | 10-20% H₂SO₄ | Variable |
| **Product base concentration** | 8-12% NaOH | 8-12% NaOH | 5-10% NaOH |
| **Acid recovery rate** | 80-92% | 75-88% | 60-80% |
| **Current efficiency** | 65-85% | 60-80% | 50-70% |
| **Energy consumption** | 1.5-3.0 kWh/kg acid | 2.0-4.0 kWh/kg acid | 2.0-5.0 kWh/kg acid |
| **Operating temperature** | 25-40°C | 25-45°C | 25-40°C |
| **Membrane lifetime** | 6-18 months (projected) | 6-18 months (projected) | 3-12 months (projected) |

Current efficiency is reduced from 100% because some H⁺ and OH⁻ ions leak back through the membranes (co-ion transport) rather than contributing to product acid/base. Higher product concentrations increase back-diffusion losses, which is why BMED product concentrations are limited to approximately 4 mol/L.

## Materials

Building a SEM Tech BMED acid regeneration system requires the following materials, organized by subsystem:

**Membrane materials** (see [SEM Tech](sem-tech.md) for manufacturing details):
- Strong acid cation exchange resin beads (sulfonic acid type)
- Strong base anion exchange resin beads (quaternary ammonium type)
- PVC or CPVC resin (powder or pellets) for binder matrix
- Organic solvent: THF, MEK, or cyclohexanone
- Water-splitting catalyst for bipolar membrane junction: FeCl₃, CrCl₃, or TiO₂ nanoparticles (optional but recommended — improves energy efficiency by 25-50%)
- Optional: fiberglass mesh or fumed silica for membrane mechanical reinforcement

**Stack hardware materials**:
- PVC or CPVC sheet (3-6 mm thick) for spacer gaskets and cell frames
- PVC cement (solvent welding adhesive) for sealing joints
- Graphite plates (5-10 mm thick) for electrodes, or coated titanium mesh for longer service life
- Polypropylene or polyethylene mesh screen (0.5-1.5 mm thick) for flow spacers in acid, base, and salt compartments
- Threaded steel tie rods (8-12 mm diameter) with nuts and washers for stack compression
- Thick PVC or steel plate (15-25 mm) for end plates
- Rubber or neoprene gasket material for electrode compartment seals

**Plumbing and tanks** (all acid/base contact surfaces must be corrosion-resistant):
- HDPE pipe and fittings for acid and base product lines (HDPE resists HCl and NaOH up to 4 mol/L)
- PVC pipe and fittings for salt feed and depleted salt lines
- HDPE tanks for acid product, base product, salt feed, and depleted salt storage
- PTFE (Teflon) or PVDF gaskets and seals for high-acid-concentration connections
- PVC ball valves or PTFE-lined valves for flow control

**Pre-treatment materials**:
- Polypropylene cartridge filter elements (5-10 micron nominal rating) for solids removal
- Granular activated carbon (GAC) for organic contaminant reduction
- Optional: hydrogen peroxide (H₂O₂) or sodium hypochlorite for Fe²⁺ oxidation before precipitation
- Optional: lime (Ca(OH)₂) or NaOH for pH-adjusted metal precipitation from feed

**Chemical handling materials**:
- Sodium hydroxide (NaOH) or potassium hydroxide (KOH) for initial base compartment fill solution
- Hydrochloric acid (HCl) or sulfuric acid (H₂SO₄) for initial acid compartment fill solution (matching the acid being regenerated)
- Sodium chloride (NaCl) or process salt for initial salt compartment fill (if needed)
- Cleaning chemicals: 2-4% HCl solution for scale removal; 1-2% NaOH solution for organic fouling

**Electrical materials**:
- DC power supply (variable, 0-600V, 0-500A) — thyristor rectifier or IGBT-based supply
- Electrical cable (rated for DC, appropriately sized for current — consult ampacity tables for 200-500A service)
- Terminal lugs and connectors (corrosion-resistant, tinned copper)
- DC-rated fuses or circuit breakers
- Grounding cable and ground rod

## Equipment

**Membrane fabrication tools** (see [SEM Tech](sem-tech.md)):
- Blender, ball mill, or grinder — for pulverizing resin beads to <200 µm particle size
- Drying oven or desiccator — for drying pulverized resin
- Glass or HDPE mixing containers — solvent-resistant, with stir sticks
- Flat casting surface — glass sheet or polished HDPE
- Drawdown bar, spatula, or spray gun — for applying membrane film to controlled thickness
- Calipers or micrometer — for measuring membrane thickness
- Fine spray bottle or brush — for applying catalyst layer between bipolar membrane layers

**Stack fabrication tools**:
- Drill press or hand drill — for cutting manifold holes in PVC spacer frames
- Jigsaw or band saw — for cutting PVC sheet to frame dimensions
- Hole saw — for cutting electrode openings in end plates
- Torque wrench — for even compression of tie rods (target: 0.5-2.0 MPa)
- PVC cement applicator — brush or dauber for solvent welding

**Operational equipment**:
- Circulation pumps (3 units, corrosion-resistant) — magnetic-drive or diaphragm pumps with HDPE or PTFE wetted parts for acid, base, and salt loops. Flow rate matched to stack hydraulic requirements (typically 5-15 cm/s channel velocity).
- DC power supply — variable voltage/current rectifier (100-600V, 50-500A), with current limiting and voltage ramp capability
- Conductivity meters (3 units) — for monitoring acid, base, and salt stream concentrations in real time
- pH meters (2 units) — for acid and base product verification
- Flow meters (3 units) — for balancing acid, base, and salt loop flow rates
- Pressure gauges (3 units) — for monitoring hydraulic pressure in each loop (sudden changes indicate membrane failure)

**Pre-treatment equipment**:
- Cartridge filter housing — standard 10-inch or 20-inch, polypropylene or 316SS construction
- Activated carbon vessel — for organic removal from feed (optional)
- Feed pump — for transferring spent acid from holding tank to pre-treatment

**Maintenance equipment**:
- Cleaning-in-place (CIP) circulation system — acid-resistant tank, pump, and hoses for chemical cleaning of the stack
- Spare membrane material and spacer gaskets
- Multimeter — for checking stack resistance and electrode continuity
- Portable conductivity meter — for spot-checking product quality

## Steps

### Step 1: Fabricate monopolar membranes

Manufacture cation exchange membranes (CEM) and anion exchange membranes (AEM) following the SEM Tech process described in [SEM Tech](sem-tech.md):

1. **Pulverize cation resin** to <200 µm powder. Dry thoroughly.
2. **Prepare PVC binder solution**: dissolve PVC resin in THF or MEK at approximately 3:7 polymer-to-solvent ratio by weight.
3. **Mix cation resin powder** into the binder at ~50% volume loading. Stir until homogeneous.
4. **Cast onto flat surface** using a drawdown bar at 0.5-1.0 mm wet thickness. Dry at ambient temperature (24-48 hours).
5. **Peel dried CEM film**. Trim to stack frame dimensions.
6. **Repeat steps 1-5** with anion exchange resin beads to produce AEM film.
7. **Test membrane integrity**: hold each membrane to light — pinholes appear as bright spots. Discard or patch defective areas. Target dry thickness: 0.2-0.8 mm.

### Step 2: Fabricate bipolar membranes

Manufacture bipolar membranes (BPM) using the two-layer casting process described in [Bipolar Membrane Fabrication Details](#bipolar-membrane-fabrication-details):

1. **Cast the cation exchange layer**: Apply cation resin/PVC mixture to a glass plate at 150-250 µm wet thickness. Allow partial drying (30-60 seconds) until surface is tacky but not liquid.
2. **Apply catalyst** (optional but recommended): Spray or brush-coat a thin layer of FeCl₃ or TiO₂ nanoparticles dispersed in PVC/THF solution onto the tacky cation layer surface. Target: 0.1-1.0 mg/cm² catalyst loading.
3. **Cast the anion exchange layer** directly on top of the partially dried cation layer at matching thickness. The solvent in the second layer softens the first layer surface, creating a molecular bond.
4. **Dry completely** at ambient temperature (24-48 hours).
5. **Peel the completed bipolar membrane** from the casting surface. Trim to stack frame dimensions.
6. **Test integrity**: Check for delamination by flexing the membrane gently — the two layers should not separate. Check for pinholes as with monopolar membranes.

### Step 3: Fabricate stack components

1. **Cut spacer gaskets** from PVC sheet: rectangular frames with a central open window and drilled manifold ports (inlet and outlet at opposite corners). Each cell triple needs three spacers: acid, base, and salt compartments.
2. **Insert flow spacers**: Place polypropylene mesh screen inside each spacer frame window to promote turbulent flow and prevent membrane contact.
3. **Prepare electrodes**: Cut graphite plates to match end plate dimensions. Drill ports for electrode rinse water flow.
4. **Cut gaskets** for electrode compartments from rubber or neoprene sheet.

### Step 4: Assemble the BMED stack

1. **Lay one end plate** flat. Place rubber gasket, then anode graphite plate.
2. **Begin stacking cell triples** (repeat for each unit):
   - Place AEM membrane on the spacer
   - Place acid compartment spacer gasket (with mesh) — PVC cement edges
   - Place BPM membrane
   - Place base compartment spacer gasket (with mesh) — PVC cement edges
   - Place CEM membrane
   - Place salt compartment spacer gasket (with mesh) — PVC cement edges
3. **Repeat** for all cell triples. Keep track of acid, base, and salt channels — they must alternate consistently in the correct order.
4. **Place cathode graphite plate** and rubber gasket on the final membrane.
5. **Install the second end plate**. Insert tie rods through corner holes.
6. **Torque tie rods** evenly in cross-pattern to 0.5-2.0 MPa compression. Even compression prevents internal leakage between acid, base, and salt channels.
7. **Connect manifold plumbing**: Attach separate PVC/HDPE piping to the acid inlet/outlet, base inlet/outlet, salt inlet/outlet, and electrode rinse ports.

### Step 5: Prepare solutions and pre-treatment

1. **Fill acid compartment loop** with dilute acid solution matching the target product (e.g., 0.5 mol/L HCl for HCl recovery). This provides initial conductivity for current flow.
2. **Fill base compartment loop** with dilute NaOH solution (e.g., 0.5 mol/L). Same purpose.
3. **Fill salt compartment** with pre-treated spent acid feed. Verify feed is filtered to <5 mg/L TSS.
4. **Fill electrode rinse loop** with NaCl or Na₂SO₄ solution (1-3% concentration).
5. **Purge all air** by running circulation pumps at maximum flow with the stack unpowered.

### Step 6: Commission the system

1. **Check for leaks** at all manifold connections and end plate seals. Tighten tie rods if seepage is observed.
2. **Measure initial conductivity** of acid, base, and salt loops. Record as baseline.
3. **Apply DC voltage**: Start at low voltage (20-50V) and gradually increase while monitoring current. Voltage per cell triple should remain below 3.0V.
4. **Monitor product streams**: Acid compartment conductivity should increase (acid concentrating). Base compartment conductivity should increase (base concentrating). Salt compartment conductivity should decrease (salt depleting).
5. **Adjust flow rates**: Balance all three loops to maintain similar hydraulic pressure. Unequal pressures deform membranes and cause cross-contamination.
6. **Continue operation** until target acid concentration is reached (typically 1-4 mol/L) or salt depletion exceeds 80%.
7. **Sample product streams**: Verify acid concentration by titration, base concentration by titration, and check for cross-contamination (salt ions in product streams).

### Step 7: Routine operation and maintenance

1. **Monitor daily**: Acid and base product concentration (conductivity meters), salt feed depletion, stack voltage and current, flow rates, pressures in all loops.
2. **Clean membranes** when current efficiency drops below 60% or stack resistance increases >20% from baseline:
   - Circulate 2-4% HCl solution through all loops for 30-60 minutes (removes metal hydroxide scale)
   - Rinse with fresh water
   - Circulate 1-2% NaOH solution through salt and base loops for 30-60 minutes (removes organic fouling)
   - Rinse thoroughly with feed solution before resuming operation
3. **Replace membranes** when cleaning no longer restores performance. Projected SEM Tech membrane lifetime in BMED: 6-18 months depending on feed chemistry and operating conditions. Disassemble stack, remove old membranes, clean spacer frames, reassemble with fresh membranes.
4. **Inspect electrodes** during scheduled maintenance. Replace graphite electrodes when visibly eroded (projected: 1-2 years in BMED service).
5. **Check bipolar membrane integrity**: If acid and base product concentrations diverge from expected values, or if product stream pH shifts unexpectedly, a bipolar membrane may have delaminated. Shut down and inspect.

## Cost Analysis

**Capital cost estimate** for a steel pickling acid recovery system (10,000 m³/year throughput):

| Component | Estimated Cost | Notes |
|-----------|---------------|-------|
| SEM Tech membranes (150 m² total) | $2,000-3,000 | $10-15/m² including bipolar |
| Stack hardware (PVC/CPVC frames, spacers) | $5,000-10,000 | Solvent-welded construction |
| DC power supply (200V, 500A rectifier) | $15,000-25,000 | Thyristor rectifier |
| Pumps and piping (HDPE, PVC) | $5,000-10,000 | Corrosion-resistant materials |
| Pre-treatment (filters, carbon) | $3,000-8,000 | Sand filter + cartridge + activated carbon |
| Instrumentation and controls | $5,000-10,000 | Conductivity, pH, pressure, PLC |
| **Total** | **$35,000-66,000** | **Conventional BMED: $150,000-400,000** |

**Operating cost comparison** for steel pickling acid recovery (10,000 m³/year of spent liquor):

- **Without regeneration**: Fresh HCl (30%) at $200/tonne, consumption 500 tonnes/year = $100,000. Neutralization with Ca(OH)₂ at $120/tonne, consumption 1,200 tonnes/year = $144,000. Sludge disposal at $50/tonne, 2,400 tonnes/year = $120,000. **Total: approximately $364,000/year.**

- **With SEM Tech BMED**: Electricity at 2.0 kWh/kg × 300,000 kg HCl/year = 600,000 kWh at $0.08/kWh = $48,000. Membrane replacement (12-month lifetime): $3,000/year. NaOH co-product credit: 240 tonnes/year at $400/tonne = -$96,000 (credit). Reduced neutralization cost: -$80,000. Reduced sludge disposal: -$60,000. **Net operating cost: approximately $195,000/year, saving $169,000/year.**

Payback period on the $35,000-66,000 capital investment: approximately 2.5-5 months. Even with doubled membrane cost and halved membrane lifetime, payback remains under 12 months.

## Scaling Considerations

**Small-scale BMED (100-1,000 m³/year)**: Single stack with 20-50 cell triples, 0.1-0.5 m² membrane area per cell. Total membrane area 6-75 m², costing $90-1,125 at SEM Tech pricing. Power supply: 50-150V, 50-200A. Suitable for job-shop metal finishing, small electroplating operations, and pilot demonstrations.

**Medium-scale BMED (1,000-10,000 m³/year)**: 1-3 stacks with 50-150 cell triples each, 0.5-2.0 m² per cell. Total membrane area 75-900 m², costing $1,125-13,500. Power supply: 100-400V, 200-1,000A. Suitable for mid-size steel plants, mining operations, and chemical manufacturing.

**Large-scale BMED (10,000-100,000 m³/year)**: Multiple parallel stack trains with 100-200 cell triples each. Total membrane area 1,000-10,000 m², costing $15,000-150,000 at SEM Tech pricing (compared to $2,000,000-5,000,000 for conventional BMED membranes at equivalent area). Power: 0.5-3.0 MW. Requires automated feed switching, continuous product quality monitoring, and redundant stack capacity for online maintenance.

At the projected SEM Tech membrane cost of $10-15/m² (including bipolar membranes), BMED becomes economically attractive for acid recovery at throughputs as low as 100 m³/year — a threshold currently served only by neutralization and disposal. The combination of low membrane cost and simple room-temperature fabrication opens acid regeneration to small and medium enterprises that cannot justify conventional BMED systems.

## Applications

**Steel pickling acid recovery**: The primary commercial application. Spent HCl pickling liquor is fed to BMED, producing regenerated HCl for the pickling line and NaOH for rinse water treatment or waste neutralization. Recovery rates of 80-95% free acid are achievable.

**Mining leachate treatment**: Spent sulfuric acid leach solutions from copper or uranium mining are processed to recover H₂SO₄ for leach circuit reuse. The co-produced base can precipitate remaining metals from the depleted salt stream.

**Chemical process waste**: Mixed acid waste from organic synthesis or electroplating is regenerated. BMED handles mixed acid matrices better than thermal methods, which can decompose sensitive organic contaminants into hazardous byproducts.

**Electroplating bath maintenance**: Acid recovery from spent plating baths and rinse water. The recovered acid maintains bath chemistry; the base can adjust pH in wastewater treatment.

## Safety

- **Concentrated acid and base**: BMED produces acid and base streams simultaneously. HCl, H₂SO₄, and NaOH at 1-4 mol/L concentrations cause severe chemical burns. Full PPE (acid-resistant gloves, face shield, chemical apron) is mandatory when handling product streams.
- **High voltage DC**: BMED stacks operate at 100-600V DC. Proper electrical insulation, grounding, and lockout/tagout procedures are essential. Arc flash hazard exists at these voltages.
- **Cross-contamination risk**: Membrane failure can allow acid and base to mix, producing vigorous exothermic neutralization. Pressure and conductivity monitoring on product streams detects membrane leaks early.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode requires ventilation in enclosed installations.
- **Chemical burns from membrane handling**: Fresh membranes may retain solvent residues. Used membranes contain absorbed acid or base. Handle with appropriate PPE.

## Troubleshooting

### Low Current Efficiency

**Symptom**: Acid and base production rates are lower than expected for the applied current. Stack current is normal but product concentrations increase slowly.

**Causes and remedies**:
- **Membrane co-ion transport**: H⁺ and OH⁻ ions leaking back through monopolar membranes reduce net product formation. This increases with product concentration. Reduce target concentration to 2-3 mol/L if efficiency drops below 60%. Use thicker monopolar membranes for improved selectivity.
- **Bipolar membrane delamination**: The cation/anion layers separate at the junction, allowing bulk solution mixing. Check for sudden changes in product pH. Replace delaminated bipolar membranes.
- **Excessive current density**: Above 50 mA/cm², water splitting at monopolar membrane surfaces (not just the bipolar junction) wastes current. Reduce current density to 20-40 mA/cm².

### Product Stream Cross-Contamination

**Symptom**: Acid product contains Na⁺ or base product contains Cl⁻/SO₄²⁻. Product purity is below specification.

**Causes and remedies**:
- **Membrane selectivity failure**: Worn or fouled monopolar membranes lose their ability to block counter-ions. Clean membranes (acid wash followed by alkali wash). If persistent, replace affected membranes.
- **Internal leakage**: Uneven stack compression or degraded spacer gaskets allow hydraulic cross-flow between channels. Retorque tie rods in cross-pattern. Replace hardened or cracked gaskets.
- **Pressure imbalance**: Higher hydraulic pressure in one loop forces solution through membranes into adjacent loops. Balance flow rates to equalize pressure across all three compartments.

### Rising Stack Resistance

**Symptom**: Stack voltage increases at constant current, or current drops at constant voltage. Energy consumption increases.

**Causes and remedies**:
- **Metal hydroxide scaling**: Iron, calcium, or magnesium hydroxides precipitate on membrane surfaces, blocking ion transport. Common with iron-rich pickling liquors when the base compartment pH exceeds iron precipitation thresholds. Perform acid cleaning (2-4% HCl, 30-60 minutes). If recurrent, improve feed pre-treatment to reduce iron loading.
- **Organic fouling**: Oil, grease, or dissolved organics from the industrial process coat membrane surfaces. Perform alkali cleaning (1-2% NaOH, 30-60 minutes). Add activated carbon pre-treatment to the feed.
- **Air entrainment**: Air bubbles trapped in channels create high-resistance zones. Purge system at high flow rate. Check for air leaks on pump suction sides.
- **Electrode degradation**: Graphite electrodes erode, increasing contact resistance. Inspect electrodes during maintenance. Replace when visibly pitted.

### Bipolar Membrane Failure

**Symptom**: Product acid and base concentrations plateau below target. Salt compartment shows unexpected pH shift. Asymmetric performance between acid and base loops.

**Causes and remedies**:
- **Junction delamination**: The cation/anion layer bond at the bipolar junction fails, typically due to thermal cycling, mechanical stress, or osmotic pressure differences. The membrane no longer splits water effectively. Replace the failed bipolar membrane. Ensure even stack compression during reassembly.
- **Catalyst poisoning**: Heavy metal ions or organic contaminants poison the water-splitting catalyst at the bipolar junction. Pre-treat feed to remove heavy metals. Use fresh catalyst loading in replacement membranes.
- **Chemical degradation**: Prolonged exposure to high acid or base concentration at the membrane surface degrades the functional groups. Limit product concentrations to 4 mol/L maximum. Ensure adequate flow velocity to prevent stagnant concentration boundary layers.

### Acid Product Concentration Too Low

**Symptom**: Acid loop conductivity plateaus well below target concentration despite normal salt feed and current.

**Causes and remedies**:
- **Insufficient salt feed concentration**: Not enough salt anions entering the acid compartment. Check salt feed TDS. If feed is diluted, increase flow rate or concentration.
- **Current density too low**: Ion transport rate is insufficient for the desired production rate. Increase current while monitoring voltage per cell triple (do not exceed 3.0V).
- **Back-diffusion**: At higher product acid concentrations, H⁺ diffuses back through the AEM into the salt compartment, limiting net acid accumulation. This is a fundamental BMED limitation. Accept 1-3 mol/L product or add a second concentration stage.

## Limitations

**Speculative technology**: SEM Tech BMED stacks have not been built or tested. All performance estimates are extrapolated from conventional BMED practice. The laminated bipolar membrane construction is theoretically sound but unvalidated.

**Product concentration ceiling**: BMED produces acid at 1-4 mol/L — lower than fresh concentrated acid (12 mol/L HCl, 18 mol/L H₂SO₄). For applications requiring concentrated acid, supplemental distillation or blending with fresh acid is necessary.

**Membrane fouling**: Dissolved metals and organic contaminants in spent acid foul membranes over time. Pretreatment requirements add complexity and cost. Iron-rich pickling liquors are particularly challenging — iron hydroxide precipitation on membrane surfaces reduces efficiency.

**Energy vs. fresh production**: At high electricity costs, BMED regeneration may be more expensive than producing fresh acid from salt and sulfur (contact process + chlor-alkali). The economic case depends on waste disposal costs avoided and the value of the co-produced base.

**Scale limitation**: Current SEM Tech membrane manufacturing is laboratory-scale. Industrial BMED requires hundreds of square meters of membrane per installation, requiring scale-up of membrane production capacity.

## See Also

- [SEM Tech](sem-tech.md) -- parent article on low-cost ion exchange membrane technology
- [SEM Tech Electrodialysis](sem-tech-electrodialysis.md) -- general electrodialysis using SEM Tech membranes
- [Electrolysis](electrolysis.md) -- industrial electrolysis processes
- [Alkali Production](alkalis.md) -- NaOH production and uses

---

*Part of the [Bootciv Tech Tree](../index.md) | [Chemistry](./index.md) | [All Domains](../index.md)*
