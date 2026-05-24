# SEM Tech Water Treatment: Membrane Desalination and Purification

> **Node ID**: water.desalination
> **Domain**: Water
> **Timeline**: Years 20-35
> **Outputs**: fresh_water, brine
> **Tags**: materials=[polymers], era=industrial

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech Membranes](../chemistry/sem-tech.md)) make electrodialysis (ED) desalination practical at a fraction of the cost of conventional membrane processes. While reverse osmosis dominates large-scale seawater desalination today, ED excels at brackish water treatment (1,000–10,000 mg/L TDS) where it consumes significantly less energy. The SEM Tech membrane — manufactured from pulverized water softener resin beads in a PVC/CPVC binder at under $1 per square foot — removes the single largest cost barrier to deploying ED in bootstrap and small-scale water treatment scenarios.

For the underlying electrodialysis principles and membrane science, see [SEM Tech Electrodialysis](../chemistry/sem-tech-electrodialysis.md).

## Overview

Water desalination and purification are essential capabilities for any settlement, regardless of scale. Brackish groundwater — containing 1,000–10,000 mg/L of total dissolved solids (TDS) — is the most common impaired water source worldwide. Conventional approaches (reverse osmosis, multi-stage flash distillation) require either high-pressure pumping systems or large thermal energy inputs, both of which demand industrial infrastructure.

Electrodialysis using SEM Tech membranes offers an alternative path: moderate-voltage DC power drives ion transport through inexpensive membranes, producing fresh water without high-pressure equipment or exotic materials. The process is modular, scales linearly, and can be powered directly from solar panels or wind turbines without inverters (DC operation).

**Speculative status**: SEM Tech ED desalination has not yet been demonstrated. The membranes have been validated for chlor-alkali electrolysis at TRL 5, but complete ED desalination stacks using SEM Tech membranes remain untested. Performance estimates below are drawn from conventional ED practice and projected SEM Tech membrane properties.

## Membrane Water Treatment Technologies

Several membrane-based water treatment technologies exist, each suited to different feed conditions:

**Electrodialysis (ED)**: Ions are transported through ion exchange membranes under an applied electric field. Removes dissolved salts and charged contaminants. Best suited for brackish water (1,000–10,000 mg/L TDS). Operates at low pressure with moderate DC voltage.

**Reverse osmosis (RO)**: High pressure (15–80 bar) forces water through a semipermeable membrane that blocks dissolved salts. Effective across all salinity ranges, including seawater (35,000+ mg/L TDS). Requires high-pressure pumps, energy recovery devices, and robust membrane housings.

**Nanofiltration (NF)**: A membrane process intermediate between RO and ultrafiltration. Removes divalent ions (Ca²⁺, Mg²⁺, SO₄²⁻) and organic molecules while passing monovalent ions. Used for water softening and organic removal.

**Ultrafiltration/Microfiltration (UF/MF)**: Removes suspended solids, bacteria, and large molecules. Does not remove dissolved salts. Used as pre-treatment for ED or RO.

For bootstrap scenarios, ED with SEM Tech membranes is the most accessible option because it avoids the high-pressure infrastructure of RO and the specialized membrane chemistry of NF.

## SEM Tech ED Desalination

The SEM Tech ED desalination process uses alternating cation and anion exchange membranes — both manufactured from the same low-cost resin-bead process described in [SEM Tech](../chemistry/sem-tech.md) — arranged in a multi-cell stack between two electrodes:

1. **Feed water** (brackish water) enters the diluate channels
2. **DC voltage** is applied across the electrode pair
3. **Cations** (Na⁺, Ca²⁺, Mg²⁺) migrate through cation exchange membranes toward the cathode
4. **Anions** (Cl⁻, SO₄²⁻, HCO₃⁻) migrate through anion exchange membranes toward the anode
5. **Diluate channels** progressively lose ions → fresh water product
6. **Concentrate channels** accumulate ions → brine waste stream

The process produces two output streams: fresh water (typically <500 mg/L TDS) and concentrated brine (20,000–80,000 mg/L TDS depending on recovery rate and feed concentration).

**Key advantage**: No high-pressure pumps are required. The driving force is electrical, not hydraulic. A simple DC power supply or direct solar panel connection suffices. Stack pressure is limited to the hydraulic pressure needed to circulate water through the thin channels (typically 0.5–3 bar).

## Comparison with Reverse Osmosis

| Parameter | ED (SEM Tech) | Reverse Osmosis |
|-----------|--------------|-----------------|
| **Optimal feed TDS** | 1,000–10,000 mg/L | 1,000–45,000+ mg/L |
| **Energy (brackish)** | 0.5–3.0 kWh/m³ | 1.5–4.0 kWh/m³ |
| **Energy (seawater)** | Not economical | 3.0–5.0 kWh/m³ |
| **Operating pressure** | 0.5–3 bar (flow only) | 15–80 bar |
| **Membrane cost** | <$1/sq ft (SEM Tech) | $30–100/sq ft |
| **Water recovery** | 75–90% | 50–85% |
| **Removes non-ionic?** | No | Yes |
| **Pre-treatment needed** | Suspended solids removal | Extensive (scaling control) |
| **Power type** | DC (direct solar possible) | AC (high-pressure pumps) |
| **Scaling sensitivity** | Moderate (EDR mitigates) | High (membrane fouling) |

ED wins decisively for brackish water (1,000–10,000 mg/L TDS): lower energy, lower pressure, lower membrane cost, higher water recovery. RO wins for seawater (>35,000 mg/L TDS) where resistive losses in ED stacks become prohibitive.

## Multi-Stage ED Configuration

For high-purity product water (<100 mg/L TDS from brackish feed), a multi-stage ED system is used:

**Stage 1 — Roughing**: Removes 60–80% of feed TDS. Large cell pairs (1.0–1.5mm spacers), moderate current density (20–40 mA/cm²). Handles the bulk of ion removal efficiently.

**Stage 2 — Polishing**: Further reduces TDS to target levels. Tighter spacers (0.5–0.75mm), lower current density (10–20 mA/cm²) to manage concentration polarization at low ionic strength. May use monovalent-selective membranes if hardness removal is critical.

**Stage 3 (optional) — Trimming**: Final ion removal for high-purity applications (industrial process water). Very low current density, long residence time.

Between stages, the partially desalted water may be recirculated to achieve target quality. A single-pass multi-stage system processes water continuously; a batch recirculation system processes a fixed volume until target TDS is reached.

**Electrodialysis Reversal (EDR)**: Periodically reversing electrode polarity (every 15–30 minutes) flips diluate and concentrate channels, which:
- Dissolves scale deposits on membrane surfaces
- Extends membrane lifetime without chemical cleaning
- Simplifies pre-treatment requirements
- Adds control system complexity but reduces operating cost

## Operating Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Feed TDS range** | 1,000–10,000 mg/L | Brackish water sweet spot |
| **Voltage per cell pair** | 0.5–1.5V | Below water splitting threshold |
| **[Current density](../glossary/current-density.md)** | 10–50 mA/cm² | Higher for concentrated feeds |
| **Stack voltage** | 50–600V DC | Depends on cell pair count |
| **[Energy consumption](../glossary/energy-consumption.md)** | 0.5–3.0 kWh/m³ | Brackish water range |
| **Water recovery** | 75–90% | Balance recovery vs. brine concentration |
| **Cell pair count** | 50–600 | More pairs = higher single-pass removal |
| **Flow velocity** | 5–15 cm/s | Through spacer channels |
| **[Operating temperature](../glossary/operating-temperature.md)** | 15–45°C | Higher temperature lowers resistance |
| **Membrane lifetime** | 1–5 years | Projected for SEM Tech in ED service |
| **Product TDS** | <500 mg/L | Drinking water standard: <1,000 mg/L |

Energy consumption scales roughly linearly with the amount of salt removed. Desalting from 5,000 to 500 mg/L TDS requires approximately 1.0–2.0 kWh/m³ with conventional ED membranes. SEM Tech membrane resistance in ED configuration is uncharacterized but expected to be comparable to conventional heterogeneous membranes based on similar composition.

## Materials

Building a SEM Tech ED desalination stack requires the following materials, organized by subsystem:

**Membrane materials** (see [SEM Tech](../chemistry/sem-tech.md) for manufacturing details):
- Strong acid cation exchange resin beads (sulfonic acid type, as used in water softeners)
- Strong base anion exchange resin beads (quaternary ammonium type)
- PVC or CPVC resin (powder or pellets) for binder matrix
- Organic solvent: THF (tetrahydrofuran), MEK (methyl ethyl ketone), or cyclohexanone
- Optional: fiberglass mesh, fumed silica, or fine sand for membrane reinforcement

**Stack hardware materials**:
- PVC or CPVC sheet (3–6 mm thick) for spacer gaskets and cell frames
- PVC cement (solvent welding adhesive) for sealing joints
- Graphite plates (5–10 mm thick) for electrodes — or coated titanium mesh for longer life
- Polypropylene or polyethylene mesh screen (0.5–1.5 mm thick) for flow spacers
- threaded steel tie rods (8–12 mm diameter) with nuts and washers for stack compression
- Thick PVC or steel plate (15–25 mm) for end plates
- Rubber or neoprene gasket material for electrode seals

**Plumbing and tanks**:
- PVC pipe and fittings (for feed, product, and brine manifolds)
- HDPE or PVC tanks for feed water storage, product water collection, and brine holding
- PVC ball valves for flow control
- Flexible PVC or silicone tubing for recirculation loops

**Pre-treatment materials**:
- Sand (graded silica sand, 0.5–2 mm particle size) for sand filter bed
- Polypropylene cartridge filter elements (5–10 micron nominal rating)
- Optional: activated carbon for organic contaminant removal

**Post-treatment materials**:
- Sodium hypochlorite solution (from [chlor-alkali electrolysis](../chemistry/sem-tech.md)) or calcium hypochlorite granules for disinfection
- Optional: lime (calcium hydroxide) for pH adjustment and remineralization

**Electrical materials**:
- DC power supply (variable, 0–600V, 0–20A) or solar panel array with charge controller
- Electrical cable (rated for DC, appropriate gauge for current)
- Terminal lugs and connectors
- Fuses or circuit breakers (DC-rated)

## Equipment

**Membrane fabrication tools** (see [SEM Tech](../chemistry/sem-tech.md)):
- Blender, ball mill, or grinder — for pulverizing resin beads to <200 µm particle size
- Drying oven or desiccator — for drying pulverized resin if wet-milled
- Mixing containers and stir sticks — glass or HDPE, solvent-resistant
- Flat casting surface — glass sheet, polished metal, or HDPE sheet
- Drawdown bar, spatula, or spray gun — for applying membrane film to controlled thickness
- Calipers or micrometer — for measuring membrane thickness

**Stack fabrication tools**:
- Drill press or hand drill — for cutting manifold holes in PVC spacer frames
- Jigsaw or band saw — for cutting PVC sheet to frame dimensions
- Hole saw — for cutting electrode openings in end plates
- Torque wrench — for even compression of tie rods (0.5–2.0 MPa)
- PVC cement applicator — brush or dauber for solvent welding

**Operational equipment**:
- Circulation pumps (2 units) — low-pressure, chemically resistant (magnetic-drive or diaphragm pumps rated for 0.5–3 bar), one for diluate loop and one for concentrate loop
- DC power supply — variable voltage/current, or solar charge controller with battery bank
- Conductivity meter — for monitoring product water TDS in real time
- Flow meters (2 units) — for balancing diluate and concentrate flow rates
- pH meter — for monitoring feed and product water pH

**Pre-treatment equipment**:
- Sand filter vessel (gravity or pressure-fed, 0.5–1.0 m³ sand bed)
- Cartridge filter housing (standard 10-inch or 20-inch housing)

**Maintenance equipment**:
- Cleaning-in-place (CIP) circulation system — tank, pump, and hoses for chemical cleaning
- Spare membrane material and spacer gaskets
- Multimeter — for checking stack resistance and electrode continuity

## Steps

### Step 1: Fabricate membranes

Manufacture cation exchange membranes (CEM) and anion exchange membranes (AEM) following the SEM Tech process described in [SEM Tech](../chemistry/sem-tech.md):

1. **Pulverize cation resin** to <200 µm powder using a blender or ball mill. Dry thoroughly.
2. **Prepare PVC binder solution**: dissolve PVC resin in THF or MEK at approximately 3:7 polymer-to-solvent ratio by weight.
3. **Mix cation resin powder** into the binder solution at ~50% volume loading. Stir until homogeneous.
4. **Cast onto flat surface** using a drawdown bar set to 0.5–1.0 mm wet thickness. Allow to dry at ambient temperature (24–48 hours depending on solvent and conditions).
5. **Peel the dried CEM film** from the casting surface. Trim to stack frame dimensions.
6. **Repeat steps 1–5** with anion exchange resin beads to produce AEM film.
7. **Test membrane integrity**: hold each membrane up to light — pinholes appear as bright spots. Discard or patch defective areas. Measure thickness (target: 0.2–0.8 mm dry).

### Step 2: Fabricate stack components

1. **Cut spacer gaskets** from PVC sheet: rectangular frames with a central open window (the flow channel area) and drilled manifold ports (inlet and outlet holes at opposite corners). Make enough for all cell pairs (each pair needs one diluate spacer and one concentrate spacer).
2. **Insert flow spacers**: place polypropylene mesh screen inside each spacer frame window. This mesh promotes turbulent flow and prevents membrane contact.
3. **Prepare electrodes**: cut graphite plates to match end plate dimensions. Drill or cut ports for electrode rinse water flow if using sealed electrode compartments.
4. **Cut gaskets** for electrode compartments from rubber or neoprene sheet.

### Step 3: Assemble the ED stack

1. **Lay one end plate** flat on a work surface. Place a rubber gasket, then the anode graphite plate.
2. **Apply PVC cement** to the first spacer gasket and press it onto the end plate assembly. Allow cement to set per manufacturer instructions.
3. **Begin alternating layers**:
   - Place CEM membrane on the spacer
   - Place diluate spacer gasket (with mesh) on the CEM — PVC cement the gasket edges
   - Place AEM membrane on the diluate spacer
   - Place concentrate spacer gasket (with mesh) on the AEM — PVC cement the gasket edges
4. **Repeat step 3** for all cell pairs. Keep track of which channels are diluate and which are concentrate — they must alternate consistently.
5. **Place cathode graphite plate** and rubber gasket on the final membrane.
6. **Install the second end plate** on top.
7. **Insert tie rods** through the corner holes in end plates and spacer frames. Hand-tighten nuts.
8. **Torque the tie rods** evenly in a cross-pattern, incrementally tightening to the target compression (0.5–2.0 MPa). Even compression prevents internal leakage between channels.
9. **Connect manifold plumbing**: attach PVC piping to the diluate inlet/outlet ports and concentrate inlet/outlet ports. Use PVC cement for all joints.
10. **Connect electrode rinse lines** to the anode and cathode compartments.

### Step 4: Set up pre-treatment

1. **Fill sand filter vessel** with graded silica sand (coarse at bottom, fine at top). Backwash to remove fines.
2. **Install cartridge filter** downstream of the sand filter. Use a 10-micron polypropylene element.
3. **Connect feed water source** (well pump or tank) to the sand filter inlet.
4. **Verify pre-treatment output**: feed water should have <5 mg/L total suspended solids (TSS) before entering the ED stack. Test with a turbidity meter or visual inspection (water should be clear).

### Step 5: Commission the system

1. **Fill both diluate and concentrate loops** with feed water. Purge all air from the system by running circulation pumps with the stack unpowered.
2. **Check for leaks** at all manifold connections and end plate seals. Tighten tie rods if seepage is observed.
3. **Measure initial conductivity** of feed water in both loops (should be identical).
4. **Apply DC voltage**: start at low voltage (10–20V) and gradually increase while monitoring current. Voltage per cell pair should not exceed 1.5V to avoid water splitting.
5. **Monitor product water conductivity**: the diluate stream conductivity should decrease steadily. The concentrate stream conductivity should increase.
6. **Adjust flow rates**: balance diluate and concentrate flows to maintain similar hydraulic pressure in both channels. Unequal pressures can deform membranes.
7. **Continue operation** until product water TDS reaches the target (<500 mg/L for drinking water).
8. **Sample product water**: test for TDS, pH, and — for drinking water applications — microbial contamination. Apply post-treatment (chlorination to 1–3 mg/L residual Cl₂) before distribution.

### Step 6: Routine operation and maintenance

1. **Monitor daily**: product water conductivity, flow rates, stack voltage and current, feed and brine tank levels.
2. **Clean membranes** when product water quality degrades or stack resistance increases >20% from baseline: circulate 2% HCl solution (for scale removal) followed by 1% NaOH solution (for organic fouling) through both loops for 30–60 minutes each. Rinse thoroughly with feed water before resuming operation.
3. **Replace cartridge filters** monthly or when pressure drop exceeds the manufacturer's recommended change-out differential.
4. **Inspect and replace membranes** when cleaning no longer restores performance. Membrane lifetime is projected at 1–5 years for SEM Tech membranes in ED service. Disassemble the stack, remove old membranes, clean spacer frames, and reassemble with fresh membranes.
5. **For EDR operation**: if using electrodialysis reversal, the control system automatically swaps polarity every 15–30 minutes. Verify that diluate and concentrate valves switch correctly and that product water conductivity remains stable across polarity reversals.

## System Design for Community Water Supply

A practical SEM Tech ED system for a small community (500 people at 50 L/person/day = 25 m³/day product water) treating brackish groundwater at 4,000 mg/L TDS:

**ED stack**: 200 cell pairs, 500 cm² active area per cell, operating at 20 mA/cm². Total membrane area: 100 m² (50 m² CEM + 50 m² AEM). Membrane cost at SEM Tech pricing: $50-100. Stack voltage at 1.0V per cell pair: 200V DC. Current at 20 mA/cm² × 500 cm² = 10A. Power consumption: 2.0 kW.

**Operating schedule**: Continuous operation for 12.5 hours/day to produce 25 m³ of fresh water. Daily energy consumption: 25 kWh. At $0.10/kWh: $2.50/day or $912/year for electricity.

**Pre-treatment**: Sand filter (1 m³ sand bed, $100-200) followed by 10-micron cartridge filter ($20-50, replaced monthly). Removes suspended solids to below 5 mg/L TSS.

**Product water quality**: <500 mg/L TDS (from 4,000 mg/L feed, 87.5% salt removal). Meets WHO drinking water standards. Post-treatment with chlorination (1-3 mg/L residual Cl₂) for disinfection adds $0.02-0.05/m³.

**Brine management**: 3 m³/day of concentrated brine at 20,000-30,000 mg/L TDS. For inland installations: evaporation pond (100-200 m² surface area in arid climate) or deep well injection. For coastal installations: dilution and ocean discharge.

**Total system capital cost**: Membranes $50-100, stack hardware $200-500, DC power supply $200-400, pre-treatment $150-300, piping and tanks $100-300, post-treatment chlorination $50-100. **Total: approximately $750-1,700.** For comparison, an RO system of equivalent capacity costs $5,000-15,000.

## Solar-Powered Deployment

The DC power requirement of ED stacks matches directly with solar photovoltaic output without AC-DC conversion. A 500W solar panel array (approximately 3 m², $200-400 at current panel prices) produces 2.0-2.5 kWh/day at 4-5 peak sun hours, sufficient to power the 25 m³/day community ED system described above during daylight hours.

**Off-grid configuration**: 500W solar panels ($200-400) + 40A solar charge controller ($50-100) + 12V, 200Ah deep-cycle battery ($150-250, provides 2.4 kWh storage for 1 day of operation without sun). Total off-grid power system cost: $400-750, comparable to 4-8 months of water purchases from tanker trucks at $5-10/m³ in water-scarce regions.

**Power matching**: The ED stack draws constant power during operation. Solar output varies throughout the day. A maximum power point tracking (MPPT) charge controller between the solar panels and the ED stack optimizes energy harvest. The battery buffer allows the ED system to operate during peak solar hours and store energy for evening operation, matching water production to demand patterns.


## Cost Analysis

**Capital cost comparison** for a 100 m³/day brackish water desalination system (4,000 mg/L TDS feed):

| Component | SEM Tech ED | Reverse Osmosis |
|-----------|------------|-----------------|
| Membranes | $100-200 (SEM Tech, <$1/ft²) | $3,000-8,000 (RO elements) |
| Stack/vessel hardware | $500-1,500 (PVC/CPVC) | $2,000-5,000 (stainless/FRP) |
| High-pressure pump | Not required | $1,500-4,000 (80 bar rated) |
| DC power supply | $300-600 (200V, 20A) | Not applicable |
| Pre-treatment | $200-500 (sand + cartridge) | $1,000-3,000 (extensive) |
| Post-treatment | $100-200 (chlorination) | $200-500 (remineralization + UV) |
| Piping and tanks | $200-500 | $500-1,500 |
| **Total** | **$1,400-3,500** | **$8,200-22,000** |

SEM Tech ED offers 3-6x lower capital cost than RO for equivalent brackish water capacity, primarily by eliminating high-pressure pumps and expensive RO membrane elements. The cost advantage grows at smaller scales where RO fixed costs (pumps, controls) are harder to amortize.

**Operating cost per cubic meter** (100 m³/day, brackish water 4,000 mg/L TDS):

- **Electricity**: 1.5 kWh/m³ × $0.10/kWh = $0.15/m³
- **Membrane replacement** (2-year lifetime, $200 replacement): $0.003/m³
- **Pre-treatment consumables** (cartridge filters): $0.01-0.03/m³
- **Cleaning chemicals** (quarterly CIP): $0.005-0.01/m³
- **Post-treatment (chlorination)**: $0.02-0.05/m³
- **Maintenance labor**: $0.05-0.10/m³
- **Total**: approximately $0.24-0.34/m³

For comparison, RO operating cost for equivalent feed: $0.40-0.80/m³. Tanker truck water in water-scarce regions: $5-10/m³. The SEM Tech ED system pays for itself in water cost savings within 2-6 weeks of operation.

## Scaling and Deployment

**Household system (0.5-2.0 m³/day)**: 5-20 cell pairs, 50-100 cm² active area, operating at 5-15 mA/cm². Powered by a single 50-100W solar panel. Produces enough drinking water for a family of 4-6 at 50 L/person/day. Membrane cost: $0.50-2.00. Total system cost: $50-150. Suitable for remote homesteads and off-grid communities.

**Community system (10-100 m³/day)**: 50-200 cell pairs, 200-1,000 cm² per cell, operating at 15-30 mA/cm². Requires 200-500W solar array or small wind turbine. Serves 50-500 people. Membrane cost: $10-100. Total system cost: $500-3,500. Most cost-effective scale for community water supply in developing regions.

**Municipal system (1,000-10,000 m³/day)**: Multiple parallel stacks with 100-400 cell pairs each. Requires 20-200 kW electrical supply. Serves 5,000-50,000 people. Membrane cost: $1,000-10,000 at SEM Tech pricing. Total system cost: $50,000-200,000 — compared to $300,000-1,500,000 for an RO plant of equivalent capacity.

## Cross-Domain Dependencies

The SEM Tech water treatment system depends on upstream capabilities from several domains. Membrane fabrication requires PVC/CPVC resin from the [chlor-alkali and petrochemical industry](../chemistry/electrolysis.md) and ion exchange resin beads (sulfonated polystyrene). The DC power supply requires [electrical infrastructure](../energy/electricity.md) — either grid power with a rectifier or direct solar panel output. Pre-treatment requires sand (quarry product) and cartridge filters (polypropylene nonwoven fabric from [textiles/petrochemicals](../chemistry/index.md)). Post-treatment chlorination requires sodium hypochlorite (from [chlor-alkali electrolysis](../chemistry/sem-tech.md) or calcium hypochlorite). Brine evaporation ponds require HDPE liner material (from [polyethylene production](../chemistry/index.md)) and earthworks capability. The PVC/CPVC stack hardware and solvent-welded joints require [PVC cement](../chemistry/index.md) (PVC resin dissolved in THF or MEK solvent).

## Applications

**Drinking water**: Primary application. Brackish groundwater (the most common impaired source) is ideal for ED. Product water meets WHO drinking water standards (<1,000 mg/L TDS, typically <500 mg/L). Modular units can serve communities from 100 to 100,000 people.

**Industrial process water**: Many industrial processes require low-TDS water (boiler feed, cooling tower makeup, chemical processing). ED provides this from brackish sources without RO infrastructure.

**Agricultural irrigation**: Moderately saline water (up to 3,000 mg/L TDS) is acceptable for many crops. ED can partially desalinate highly brackish water to irrigation-suitable levels, consuming less energy than full drinking water treatment. See [SEM Tech Hydroponics](../agriculture/sem-tech-hydroponics.md) for water reuse in controlled growing environments.

**Brine management**: The concentrate stream from ED is a managed brine that must be disposed of responsibly. Options include: evaporation ponds (arid climates), deep well injection (geologically suitable sites), further concentration for salt recovery, or dilution with wastewater effluent.

**Mine water treatment**: Acid mine drainage and process water from mining operations contain dissolved metals and salts. SEM Tech ED can recover fresh water while concentrating the contaminants for treatment. This synergizes with SEM Tech mineral extraction capabilities (see [SEM Tech](../chemistry/sem-tech.md)).

## Safety

- **Brine handling**: Concentrated brine (up to 80,000 mg/L TDS) is corrosive and harmful to vegetation and aquatic life. Containment structures must be chemically resistant (HDPE, PVC). Never discharge untreated brine to surface water or groundwater.
- **Electrical safety**: ED stacks operate at 50–600V DC. Proper grounding, insulation, and lockout/tagout procedures are mandatory during maintenance. Current leakage through failed seals can cause localized electrolysis and gas generation.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode during operation. Ensure ventilation in enclosed installations. Hydrogen accumulation above 4% concentration in air is explosive.
- **Chemical exposure**: Cleaning solutions (acid for scale removal, alkali for organic fouling) require standard chemical handling PPE — goggles, gloves, aprons.
- **Product water quality**: ED removes only dissolved ions. Suspended solids, microorganisms, and organic contaminants pass through unaffected. Post-treatment (disinfection, filtration) is required for drinking water applications.

## Limitations

**Not demonstrated**: SEM Tech ED desalination is speculative. Membranes are validated for chlor-alkali electrolysis (TRL 5) but have not been tested in multi-cell ED stacks for water treatment. Key unknowns: membrane resistance in thin-channel ED geometry, matched cation-anion pair performance, fouling behavior with natural water matrices, and long-term durability in continuous desalination service.

**Not suitable for seawater**: ED becomes uneconomical above approximately 10,000 mg/L TDS due to increasing resistive losses. Seawater desalination (35,000+ mg/L) requires reverse osmosis or thermal processes.

**No non-ionic contaminant removal**: ED transports only charged species. Dissolved organics, silica, microorganisms, and suspended solids are not removed. Pre-treatment (filtration) and post-treatment (disinfection) are essential for potable water.

**Brine disposal**: Every cubic meter of fresh water produced generates 0.1–0.25 m³ of concentrated brine. Inland brine disposal is a significant logistical challenge. Evaporation ponds require large land areas; deep well injection requires suitable geology.

**Divalent ion scaling**: Calcium and magnesium can precipitate as carbonates or hydroxides on membrane surfaces, reducing performance. Electrodialysis reversal (EDR) mitigates this but adds complexity. Pre-treatment to remove hardness may be necessary for high-hardness feeds.

## See Also

- [SEM Tech](../chemistry/sem-tech.md) — ion exchange membrane manufacturing
- [SEM Tech Electrodialysis](../chemistry/sem-tech-electrodialysis.md) — ED principles and process variants
- [SEM Tech Hydroponics](../agriculture/sem-tech-hydroponics.md) — water reuse in controlled growing systems

---

*Part of the [Bootciv Tech Tree](../index.md) | [Water](./index.md) | [All Domains](../index.md)*
