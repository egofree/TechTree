# SEM Tech Water Treatment: Membrane Desalination and Purification

> **Node ID**: water.sem-tech-water-treatment
> **Domain**: [Water](./index.md)
> **Dependencies**: [`chemistry.sem-tech`](../chemistry/sem-tech.md), [`water.basic-treatment`](basic-treatment.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 20-35
> **Outputs**: fresh_water, brine
> **Critical**: No — advanced capability for brackish water desalination, not required for basic water supply

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

## Process Description

The SEM Tech electrodialysis (ED) desalination process uses alternating cation and anion exchange membranes — both manufactured from the same low-cost resin-bead process described in [SEM Tech](../chemistry/sem-tech.md) — arranged in a multi-cell stack between two electrodes. The complete treatment train proceeds as follows: **intake → pre-treatment → ED stack → post-treatment → distribution**.

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

## Post-Treatment

ED removes dissolved ions but does not eliminate microorganisms, organic contaminants, or suspended solids. Product water from the ED stack requires post-treatment before it is safe for human consumption. Additionally, very low-TDS product water (<50 mg/L) is corrosive to metal pipes and has a flat taste — remineralization improves both palatability and distribution system compatibility.

### Disinfection

**Chlorination** is the most practical disinfection method for SEM Tech installations. Sodium hypochlorite (NaOCl) is available as a byproduct of [SEM Tech chlor-alkali electrolysis](../chemistry/sem-tech.md), or calcium hypochlorite granules (HTH, 65-70% available chlorine) can be purchased commercially.

1. **Dose**: 2-5 mg/L of sodium hypochlorite solution (or equivalent calcium hypochlorite dose) into the product water storage tank. Actual dose depends on feed water organic content and chlorine demand.
2. **Contact time**: Minimum 30 minutes at pH <8.0. The CT value (concentration × time) should exceed 15 mg·min/L for effective bacterial and viral inactivation.
3. **Residual target**: 0.5-1.0 mg/L free chlorine residual after 30 minutes contact. For distribution systems with long residence times, maintain 0.2-0.5 mg/L residual at the point of use.
4. **Testing**: Use DPD (N,N-diethyl-p-phenylenediamine) colorimetric test kit to verify free chlorine residual. Test daily at the storage tank outlet and weekly at the farthest distribution point.

**Alternative: UV disinfection** — A low-pressure mercury vapor UV lamp (254 nm wavelength) at a dose of 40 mJ/cm² provides effective disinfection without chemical addition. Requires a clear (low-turbidity) water stream and reliable electrical power. No residual protection in distribution — best suited for point-of-use systems or when chlorination chemicals are unavailable.

**Alternative: Solar disinfection (SODIS)** — For household-level emergency use, filling clear PET bottles with ED product water and exposing to full sun for 6 hours achieves bacterial inactivation. Not suitable as a primary community-scale disinfection method.

### Remineralization

ED product water at <100 mg/L TDS is aggressive (corrosive) toward metal pipes, concrete, and some plastics. Remineralization adds dissolved minerals back to the water for:

- **Corrosion control**: Maintaining a positive Langelier Saturation Index (LSI ≥0) prevents dissolution of metal pipe materials.
- **Taste improvement**: Water below 50 mg/L TDS tastes flat and unsatisfying. Target 150-300 mg/L TDS for palatability.
- **Health**: Minimum calcium and magnesium levels are beneficial. WHO suggests at least 30 mg/L combined Ca²⁺ + Mg²⁺.

**Methods**:

- **Lime dosing**: Add calcium hydroxide (Ca(OH)₂, hydrated lime) at 30-80 mg/L to raise calcium content and alkalinity. Lime is inexpensive and widely available. Dissolve lime in a small mixing tank before dosing into the product water stream. Target pH: 7.5-8.2.
- **Calcite (limestone) contactor**: Pass product water through a bed of crushed calcium carbonate (CaCO₃, 1-3 mm particle size). The slightly acidic ED product water slowly dissolves calcite, adding calcium and alkalinity. Simple, passive, no dosing equipment. Bed replacement every 6-12 months depending on flow.
- **Blending**: Mix a controlled fraction (5-15%) of filtered raw (feed) water back into the product water. Requires the feed water to be microbiologically safe after filtration. Simplest method but limits final water quality.

### pH Adjustment

ED product water pH may drift outside the desirable range (6.5-8.5) depending on feed chemistry and operating conditions:

- **Low pH (<6.5)**: Dose with hydrated lime (Ca(OH)₂) or sodium hydroxide (NaOH, from [SEM Tech chlor-alkali](../chemistry/sem-tech.md)). Lime is preferred for cost and safety.
- **High pH (>8.5)**: Dose with carbon dioxide (CO₂) gas or dilute hydrochloric acid (HCl). CO₂ injection is safer and self-regulating — excess CO₂ off-gasses.

Verify pH with a calibrated pH meter after adjustment. Target pH: 7.0-8.0 for drinking water distribution.

### Final Filtration

After disinfection and remineralization, a final 1-micron cartridge filter removes any particulates introduced during post-treatment (lime particles, sand fines, rust from piping). This filter protects distribution system fixtures and provides a final barrier against large microorganisms (Giardia cysts, helminth eggs).

## Water Quality Testing

Regular testing ensures product water meets drinking water standards and detects process upsets early. The following schedule is based on WHO Guidelines for Drinking-water Quality.

### WHO Drinking Water Parameters

| Parameter | WHO Guideline | Action Threshold |
|-----------|--------------|-----------------|
| **TDS** | <1,000 mg/L (health), <600 mg/L (taste) | >500 mg/L — investigate stack performance |
| **pH** | 6.5-8.5 | <6.0 or >9.0 — stop distribution, adjust post-treatment |
| **Turbidity** | <4 NTU (health), <1 NTU (aesthetic) | >5 NTU — check pre-treatment filters |
| **Free chlorine residual** | 0.2-5.0 mg/L | <0.2 mg/L — re-dose chlorination |
| **Total coliform bacteria** | 0 per 100 mL | Any detection — shock-chlorinate system |
| **E. coli** | 0 per 100 mL | Any detection — stop distribution, investigate source contamination |
| **Sodium (Na⁺)** | 200 mg/L | >150 mg/L — check membrane integrity |
| **Chloride (Cl⁻)** | 250 mg/L (taste) | >200 mg/L — check stack leakage |
| **Total hardness** | No guideline (structural) | <30 mg/L as CaCO₃ — remineralize |
| **Fluoride** | 1.5 mg/L | >1.0 mg/L — check feed water source |

### Testing Schedule

**Continuous monitoring** (instrumentation):
- Product water conductivity (TDS proxy) — conductivity meter with data logging
- Product water pH — pH probe at storage tank inlet
- Stack voltage and current — DC power supply readout
- Flow rates (diluate and concentrate) — inline flow meters

**Daily tests** (operator, 5-10 minutes):
- Free chlorine residual at storage tank outlet (DPD test kit)
- Visual inspection of product water (clarity, color, odor)
- Record stack voltage, current, conductivity, flow rates in logbook

**Weekly tests** (operator, 15-20 minutes):
- Feed water TDS and pH
- Brine TDS
- Turbidity of product water (nephelometric turbidity tube or meter)
- Total hardness of product water (EDTA titration kit)

**Monthly tests** (laboratory or field kit):
- Total coliform bacteria (membrane filtration or presence/absence test)
- E. coli (membrane filtration with selective media)
- Sodium concentration (flame photometry or ion-selective electrode)
- Chloride concentration (silver nitrate titration or ion-selective electrode)

**Quarterly tests** (contracted laboratory):
- Full chemical panel: heavy metals (Pb, As, Cd, Cr, Hg), nitrate, nitrite, sulfate, fluoride, boron
- Pesticide scan (if agricultural runoff is a concern)
- Radionuclides (if in a known radon/uranium area)

### Record-Keeping

Maintain a bound logbook or simple spreadsheet recording:
- Daily: chlorine residual, conductivity reading, voltage, current, flow rates, feed tank level, brine tank level, any observations
- Weekly: pH, turbidity, hardness, TDS
- Monthly: bacterial results, chemical parameters
- Corrective actions taken (cleaning cycles, membrane replacements, chemical adjustments)

Retain records for a minimum of 2 years. Records demonstrate water safety to regulators and community members, and provide diagnostic history for troubleshooting.

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

## Brine Management

Every liter of fresh water produced by ED generates a corresponding volume of concentrated brine. The brine volume equals (1 - recovery rate) × feed volume. At 80% water recovery, a 25 m³/day system produces approximately 6.25 m³/day of brine at 16,000-25,000 mg/L TDS (from a 4,000 mg/L feed). Brine management is often the most logistically challenging aspect of inland ED deployment.

### Brine Characteristics

ED concentrate brine differs from RO reject in several important ways:

- **Lower pressure**: ED operates at 0.5-3 bar, so brine exits the stack at low pressure. No pressure recovery equipment is needed.
- **Matched ionic composition**: ED removes all ion types proportionally. The brine mirrors the feed water chemistry at higher concentration. If the feed is predominantly NaCl, the brine is predominantly NaCl.
- **Temperature**: ED brine is at ambient feed temperature (no significant heating during processing).
- **Non-ionic contaminants**: Dissolved organics, silica, and suspended solids remain in the diluate (product) stream, not in the brine. Brine is primarily dissolved salts.

### Disposal and Recovery Options

**Evaporation ponds (arid and semi-arid climates)**:

The simplest brine management approach. Brine flows by gravity or low-pressure pump to a shallow, lined pond where solar evaporation concentrates it to dryness.

- **Sizing**: Pond area = brine volume ÷ net evaporation rate. Net evaporation rate = pan evaporation rate × 0.7 − rainfall. In an arid climate with 2,500 mm/year pan evaporation and 200 mm/year rainfall: net evaporation ≈ 1,550 mm/year = 4.25 mm/day. For 6.25 m³/day brine: pond area ≈ 6.25 ÷ 0.00425 ≈ 1,470 m² (approximately 38 m × 38 m). Size at 1.5× calculated area to accommodate irregular evaporation and storm events.
- **Lining**: 1.0-1.5 mm HDPE geomembrane liner prevents soil and groundwater contamination. Liner cost: $2-5/m² installed. A 2,200 m² pond (1.5× oversize): $4,400-11,000.
- **Construction**: Earthen berms 0.5-1.0 m high, compacted subgrade, smooth HDPE liner, anchor trench at perimeter. Inlet pipe from brine tank. Overflow spillway for storm events.
- **Salt harvesting**: Crystallized salt accumulates over months to years. In regions with seasonal evaporation, annual salt harvesting is practical. Harvested salt can be used for industrial purposes, chlor-alkali feedstock (NaCl), or disposed of in landfill if contaminants are present.
- **Monitoring**: Monthly inspection of liner integrity. Quarterly groundwater monitoring wells upgradient and downgradient if required by local regulations.

**Deep well injection (geologically suitable sites)**:

Brine is pumped into a deep, confined geological formation below freshwater aquifers. Suitable formations include depleted oil/gas reservoirs, deep saline aquifers, or impermeable shale formations.

- **Depth**: Typically 300-2,000 m below surface, below all potable aquifers.
- **Geological requirements**: Confining layer (impermeable shale or clay) above the injection zone; porous, permeable injection zone (sandstone, limestone); no faults connecting to freshwater.
- **Well construction**: Steel casing cemented to surface, injection tubing with packer, corrosion-resistant materials. Cost: $50,000-500,000 per well depending on depth.
- **Pumping**: Injection pressure must not exceed formation fracture pressure. Low-pressure ED brine may require a booster pump.
- **Regulatory**: Requires geological survey, permitting, and often environmental impact assessment. Not available in all jurisdictions.

**Dilution discharge (coastal installations only)**:

For installations near the ocean, brine can be diluted with seawater and discharged through a properly designed outfall.

- **Dilution ratio**: Mix brine with 10-20 volumes of seawater before discharge to bring salinity within 1-2 ppt of ambient seawater (~35 ppt).
- **Outfall design**: Diffuser nozzle or multi-port outfall extending beyond the surf zone ensures rapid mixing. Discharge velocity >3 m/s promotes initial dilution.
- **Environmental assessment**: Required before construction. Sensitive marine ecosystems (coral reefs, seagrass beds) may require higher dilution ratios or alternative discharge locations.
- **Regulatory**: Coastal discharge permits required in most jurisdictions.

**Salt recovery (industrial co-product)**:

When brine concentration exceeds approximately 100,000 mg/L TDS (achievable by operating at lower water recovery or multi-stage concentration), salt can be crystallized and recovered as a commercial product.

- **Solar crystallization**: Extended evaporation in shallow ponds. NaCl crystallizes first; other salts (CaSO₄, MgSO₄) crystallize at higher concentrations. Sequential crystallization produces relatively pure NaCl.
- **Thermal crystallization**: Forced evaporation using waste heat or solar thermal collectors. More compact than pond systems but requires energy input.
- **Product quality**: Recovered salt is suitable for industrial chlor-alkali feedstock (requires >97% NaCl purity), road de-icing, or water softener regeneration. Food-grade salt requires additional washing and drying.
- **Economic value**: Industrial salt at $30-80/ton provides modest revenue that partially offsets brine management costs. At 6.25 m³/day of brine from 4,000 mg/L feed, salt production is approximately 25 kg/day (9 tons/year) — too small for industrial salt market but sufficient for local use (chlor-alkali cell feed, water softener regeneration).

**Zero liquid discharge (ZLD) — sensitive environments**:

In locations where no brine discharge is permitted (closed-basin lakes, protected watersheds, arid regions with no suitable injection geology), a ZLD system recovers all water from the brine, producing only solid salt as waste.

- **Process**: Feed ED brine to a secondary concentration stage (higher-voltage ED or thermal evaporation) to produce saturated brine, then crystallize to dryness. Recovered condensate returns to the product water stream.
- **Energy cost**: Thermal evaporation consumes 25-40 kWh/m³ of brine — an order of magnitude more than the ED desalination itself. ZLD is only practical when energy is very cheap or when no alternatives exist.
- **Applicability**: Rarely necessary for inland brackish water ED. Reserve for sites with extreme environmental constraints or for recovering high-value salts from industrial waste streams.

### Inland Deployment Strategy

For most inland SEM Tech ED installations, the recommended brine management approach is:

1. **Primary**: Evaporation pond — lowest cost, lowest complexity, passive operation.
2. **Backup/overflow**: Second pond cell or emergency storage tank for storm events.
3. **Salt reuse**: Harvest crystallized salt for local chlor-alkali cell feed or water softener regeneration.
4. **Monitoring**: Quarterly inspection of pond liner and (if applicable) groundwater quality.

Total brine management capital cost for the 25 m³/day community system: $5,000-15,000 (dominated by evaporation pond construction and HDPE liner), or approximately 30-50% of total system capital cost. This is a significant but unavoidable expense for inland installations.

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

## Troubleshooting

### Rising Product Water TDS

**Symptom**: Product water conductivity increases despite normal operation.

**Causes and remedies**:
- **Membrane damage**: Pinholes or tears allow concentrate to leak into the diluate stream. Inspect membranes by holding to light (pinholes appear as bright spots). Replace damaged membranes.
- **Internal leakage**: Uneven stack compression or degraded spacer gaskets allow cross-flow between channels. Retorque tie rods in cross-pattern. Replace hardened or cracked gaskets.
- **Insufficient voltage/current**: Current density below threshold for effective ion transport. Verify power supply output with a multimeter. Increase voltage while staying below 1.5V per cell pair.
- **Channeling**: Flow distribution is uneven, allowing some water to pass through the stack without adequate ion removal. Check spacer mesh for blockage or compaction. Verify flow rates are within specification (5-15 cm/s velocity).

### Increasing Stack Resistance

**Symptom**: Stack voltage rises at constant current, or current drops at constant voltage. Energy consumption increases.

**Causes and remedies**:
- **Scaling**: Calcium carbonate or calcium sulfate precipitation on membrane surfaces. Perform acid cleaning (2% HCl, 30-60 minutes circulation). If recurrent, implement electrodialysis reversal (EDR) or add pre-treatment for hardness removal.
- **Organic fouling**: Natural organic matter (humic substances) coating membranes. Perform alkaline cleaning (1% NaOH, 30-60 minutes circulation). Add activated carbon pre-treatment if organic load is high.
- **Electrode degradation**: Graphite electrodes erode over time, increasing contact resistance. Inspect electrodes during scheduled maintenance. Replace when visibly eroded or pitted.
- **Air entrainment**: Air bubbles trapped in channels create high-resistance zones. Purge the system by running circulation pumps at maximum flow with the stack unpowered. Check for air leaks on the suction side of pumps.
- **Membrane compaction**: Long-term compression reduces channel height and increases flow resistance. Disassemble stack, inspect spacer thickness, replace compressed spacers.

### Low Water Recovery

**Symptom**: Brine volume is higher than expected; product water volume is lower than design.

**Causes and remedies**:
- **Excessive brine flow**: Concentrate stream flow rate set too high relative to diluate flow. Reduce concentrate pump flow. Target concentrate flow within 80-120% of diluate flow.
- **Membrane deformation**: Pressure imbalance between diluate and concentrate channels bows membranes, reducing effective channel area. Balance hydraulic pressures in both loops.
- **High feed TDS**: Feed water salt content is higher than design point, requiring more current and longer residence time for equivalent removal. If persistent, consider adding a second stage or operating in batch recirculation mode.

### Product Water pH Outside Range

**Symptom**: Product water pH <6.5 or >8.5.

**Causes and remedies**:
- **Water splitting at electrodes**: At very high current density (>50 mA/cm²), water electrolysis at the electrode boundary membranes produces acid (anode side) and base (cathode side) that can contaminate adjacent channels. Reduce current density. Ensure electrode rinse flow is adequate.
- **Feed water pH shift**: Source water chemistry changes seasonally (e.g., spring snowmelt, agricultural runoff). Monitor feed pH daily and adjust post-treatment dosing accordingly.
- **Bicarbonate stripping**: At low TDS, bicarbonate equilibrium shifts, releasing CO₂ and lowering pH. Remineralization with lime (Ca(OH)₂) restores pH and alkalinity simultaneously.

### Uneven Flow Distribution

**Symptom**: Product water quality varies between cells; some cells produce good water while others do not.

**Causes and remedies**:
- **Manifold blockage**: Debris or scale in inlet/outlet manifolds restricts flow to some cells. Flush manifolds with acid solution. Improve pre-treatment filtration.
- **Spacer compaction**: Repeated compression cycles permanently deform spacers in high-pressure zones. Replace compressed spacers. Use consistent torque during reassembly.
- **Air locks**: Air trapped in specific channels prevents flow. Purge system at high flow rate. Install air release valves at high points in the manifold.

### Electrode Corrosion

**Symptom**: Graphite electrodes visibly eroded, pitted, or friable. Electrode rinse water discolored.

**Causes and remedies**:
- **Normal wear**: Graphite slowly oxidizes in the electrode compartments. Expected lifetime: 1-2 years in ED service. Schedule replacement during annual maintenance.
- **Excessive current density**: Current density above 50 mA/cm² accelerates electrode erosion. Reduce operating current density.
- **Poor electrode rinse flow**: Stagnant water in electrode compartments accelerates corrosion. Verify electrode rinse flow rate meets specification (typically 5-10% of feed flow).

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
