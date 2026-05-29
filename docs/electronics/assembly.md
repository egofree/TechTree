# Electronics Assembly

> **Node ID**: electronics.assembly
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`glass.fibers`](../glass/fibers.md), [`polymers.thermosets`](../polymers/thermosets.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Enables**: [`computing.electronic`](../computing/electronic.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 30-50
> **Outputs**: pcb_assemblies, soldered_joints, packaged_components
> **Critical**: Yes — electronics assembly bridges semiconductor device fabrication and functional electronic systems, without which no transistor or IC becomes a usable circuit

## 1. Overview

Electronics assembly encompasses PCB fabrication, component placement, soldering (through-hole and surface mount), conformal coating, and testing. It bridges semiconductor device fabrication and functional electronic systems — from discrete transistor circuits to multi-chip modules and early integrated circuit packaging.

## 2. Prerequisites

### Materials
- **Copper-clad laminate**: FR-4 substrate (woven [fiberglass](../glass/fibers.md) + [epoxy resin](../polymers/thermosets.md)), copper foil 17.5-35 μm thickness
- **Solder alloys**: Sn63/Pb37 eutectic (melts 183°C), SAC305 lead-free (melts 217-220°C), from [metals processing](../metals/iron-steel.md)
- **Solder paste**: Flux + solder powder (20-45 μm particles, Type 3), stored at 2-10°C
- **Flux**: Rosin-core (colophony, abietic acid), no-clean, or water-soluble types
- **Conformal coating**: Acrylic, epoxy, urethane, silicone, or parylene from [polymers](../polymers/thermosets.md)
- **Electronic components**: [Semiconductor devices](../silicon/basic-devices.md), [passive components](passive-components.md), connectors
- **Photoresist**: Dry film (25-50 μm) or liquid, for PCB patterning
- **Etchant chemicals**: Ferric chloride (FeCl₃) or ammonium persulfate from [chemical supply](../chemistry/acids.md)

### Tools
- Soldering iron (25-80W, tip temperature 320-420°C) or reflow oven
- Pick-and-place machine (10,000-100,000+ components/hour) or manual placement tools
- [Wire drawing dies](../machine-tools/machining.md) for consistent wire diameters
- Wave soldering machine for through-hole assembly
- Stencil printer for solder paste application (stainless steel stencil, 100-150 μm)
- [Oscilloscope](../measurement/electrical-instruments.md) and multimeter for testing

### Knowledge
- Soldering metallurgy: wetting, intermetallic formation, surface tension
- Reflow profile optimization: preheat → soak → reflow → cool
- ESD (electrostatic discharge) control procedures
- IPC-A-610 workmanship standards for solder joint acceptability

## 3. Bill of Materials

| Material | Quantity (per 100 boards, 100 × 100 mm, mixed SMT/TH) | Source | Alternatives |
|----------|-------------------------------------------------------|--------|-------------|
| FR-4 copper-clad laminate (1.6 mm, 1 oz Cu) | 1.0 m² | [Glass Fibers](../glass/fibers.md) + [Thermosets](../polymers/thermosets.md) | Paper/phenolic (FR-2, lower cost/performance) |
| Solder paste (SAC305, Type 3) | 200-500 g | [Metals](../metals/index.md) | Sn/Pb 63/37 (lower melting, toxic lead) |
| Solder wire (Sn/Pb 63/37, 0.8 mm) | 50-200 g | [Metals](../metals/index.md) | Lead-free wire (higher melting temperature) |
| Flux (rosin-core or no-clean) | 50-100 mL | [Chemical supply](../chemistry/acids.md) | — |
| Conformal coating (acrylic) | 100-200 mL | [Polymers](../polymers/thermosets.md) | Urethane, silicone, epoxy (longer cure) |
| Components (resistors, capacitors, ICs) | Per BOM | [Passive Components](passive-components.md), [Semiconductors](semiconductor-devices.md) | — |
| Ferric chloride etchant (42° Baumé) | 2-4 L | [Chemical supply](../chemistry/acids.md) | Ammonium persulfate (slower, cleaner) |
| Photoresist (dry film, 38 μm) | 1-2 sheets | Photochemical supply | Liquid photoresist (screen-printed) |

## 4. Process Description

### 4.1 PCB Fabrication (Single-Sided)

Printed circuit boards (PCBs) provide the interconnection substrate for all electronic assemblies. The most basic PCB is a single-sided copper-clad laminate with etched traces.

**Substrate materials**:
- FR-4: Woven fiberglass cloth impregnated with epoxy resin. Dielectric constant εᵣ = 4.2-4.8 at 1 MHz. Dissipation factor tan δ = 0.01-0.02. Glass transition temperature Tg = 130-140°C (standard) or 170-180°C (high-Tg). Thickness: 0.2-3.2 mm. The workhorse substrate for 95%+ of PCBs. See [Glass Fibers](../glass/fibers.md) for fiberglass production.
- Copper foil: Electrodeposited (ED) or rolled copper, 17.5 μm (0.5 oz/ft²) or 35 μm (1 oz/ft²) thickness. Bonded to substrate with heat and pressure. Adhesion: >1.0 N/mm peel strength.

**Single-sided PCB process**:
1. Cut copper-clad laminate to panel size (typically 300 × 300 mm or 450 × 600 mm).
2. Drill holes with carbide bits (0.3-3.0 mm diameter) at 50,000-100,000 RPM. Hit rate: 100-200/minute. Entry/exit material (aluminum or phenolic) prevents burrs. Holes per panel: 100-5,000.
3. Clean surface: pumice scrub or chemical microetch (Na₂S₂O₈ or H₂O₂/H₂SO₄). Surface roughness: 0.3-0.5 μm Ra.
4. Apply photoresist: dry film (25-50 μm) laminated at 100-110°C, 2-3 bar. Or liquid (screen-printed, 10-20 μm).
5. Expose: UV light (365 nm, 100-300 mJ/cm²) through photomask for 10-30 seconds.
6. Develop: 1% Na₂CO₃ at 30°C for negative resist, 30-60 seconds spray.
7. Etch copper: FeCl₃ (30-42° Baumé, 45-55°C) or ammonium persulfate (20-25%, 40-50°C). Etch rate: 15-30 μm/min for FeCl₃. Minimum trace: 0.1-0.2 mm.
8. Strip resist: 3-5% NaOH at 50-60°C.
9. Solder mask: screen-printed or photoimageable epoxy (green/blue/red/black). Cure at 150°C for 30-60 min. Thickness: 10-30 μm.
10. Silkscreen legend: white epoxy ink, component designators. Cure at 150°C for 15-20 min.
11. Surface finish: HASL (dip in molten Sn/Pb at 235-260°C, hot air level, 1-30 μm). Or ENIG (3-5 μm Ni + 0.03-0.08 μm Au). Or immersion Ag (0.1-0.3 μm).
12. Electrical test: flying probe or bed-of-nails. Continuity <10 Ω, isolation >10 MΩ.

**Double-sided PCB**: Same process plus plated through-holes (PTH). After drilling: catalytic activation (Pd-Sn colloid), electroless Cu (0.5-2.0 μm), electrolytic Cu (20-25 μm at 15-30 mA/cm²). PTH resistance: <5 mΩ per hole.

**Multi-layer PCB**: Inner cores (etched both sides) stacked with prepreg and outer Cu foils. Laminated at 170-180°C, 200-400 psi, 60-90 min. Drill all layers, plate holes. Layer count: 2-32+. Via types: through-hole, blind (outer-to-inner), buried (inner-to-inner).

## Soldering

**Solder alloys**: Sn63/Pb37 eutectic melts at 183°C (traditional). Lead-free: SAC305 (Sn96.5/Ag3.0/Cu0.5, melts 217-220°C), Sn99.3/Cu0.7 (melts 227°C). High-temperature: Sn95/Ag5 (221-240°C), Au80/Sn20 (280°C, for die attach).

**Through-hole soldering**:
- Hand soldering: 25-80W iron, tip at 320-380°C (Sn/Pb) or 350-420°C (lead-free). Contact: 2-5 seconds/joint. Rosin-core flux wire. Wetting angle <90° = good joint.
- Wave soldering: spray flux → preheat (80-120°C) → wave of molten solder (250-270°C) at 1-3 m/min. Contact time: 2-5 sec. Defect target: <500 ppm.

**Surface mount soldering**:
- Solder paste: flux + solder powder (20-45 μm particles, Type 3). Viscosity: 150-250 Pa·s. Store at 2-10°C, shelf life 3-6 months.
- Stencil printing: stainless steel stencil (100-150 μm) with laser-cut apertures. Squeegee at 50-150 mm/s, 3-8 kg pressure. Print accuracy: ±25 μm at 3σ.
- Pick-and-place: 10,000-100,000+ components/hour. Accuracy: ±50-100 μm (standard), ±10-25 μm (high-precision). Range: 0201 (0.5 × 0.25 mm) to 40 × 40 mm QFP/BGA.
- Reflow oven: preheat (25-150°C at 1-3°C/s) → soak (150-200°C, 60-120s) → reflow (peak 220-250°C for lead-free, 45-90s above liquidus) → cool (2-4°C/s). Total: 3-6 min. Uniformity: ±5°C. N₂ atmosphere (O₂ <1000 ppm) for lead-free.

## Conformal Coating

Protective coating on assembled PCBs against moisture, dust, chemicals, and fungus. Applied by spray, dip, or selective dispensing at 0.025-0.075 mm dry thickness.

**Types**: Acrylic (easy rework, solvent-removable). Epoxy (chemical-resistant, hard to remove). Urethane (flexible, abrasion-resistant). Silicone (200°C rated, flexible). Parylene (vapor-deposited, 0.01-0.05 mm, highest performance — see [Chemical Vapor Deposition](../chemistry/cvd.md)).

Cure: air dry (24-48 hours acrylic), thermal (60-80°C, 30-60 min epoxy), UV (10-30 seconds). Mask connectors, test points, and adjustable components before application. Inspect under UV light (fluorescent tracer in coating shows coverage gaps).

## Wire and Cable Assembly

**Hookup wire**: Stranded tinned copper (7-65 strands, 0.08-0.32 mm) with PVC or PTFE insulation, 22-16 AWG (0.3-1.3 mm²). Rated 300-600V. Temperature: -20 to 80°C (PVC), -60 to 200°C (PTFE). Strip 5-8 mm with wire strippers (not knife — nicks cause breakage).

**Crimp terminals**: Ring, spade, pin terminals applied with calibrated crimp tool. Pull test: >15 N for 22 AWG, >50 N for 16 AWG. Insulation displacement connectors (IDC) for ribbon cable: punch at 50-100 N force.

**Wire harness rules**: Color code (red: +V, black: ground, blue: signal). Cable ties every 200-300 mm. Service loops (50-100 mm slack) at connectors for strain relief. Label both ends. Insulation resistance: >100 MΩ at 500V DC between adjacent conductors.

## Testing and Quality Control

**In-circuit test (ICT)**: Bed-of-nails fixture probes every net. Measures component values (R, C, L, diode Vf). Test time: 10-60 seconds. Fault coverage: 85-95%. Detects wrong values, missing components, shorts, opens.

**Functional test**: Apply power (3.3V, 5V, ±12V DC) and input signals. Verify output. Test firmware if applicable. Time: 1-10 minutes. Coverage: 70-90%.

**Automated optical inspection (AOI)**: Camera inspects solder joints and component placement. Detects: missing/misaligned components, tombstoning, solder bridges, insufficient solder. Rate: 10-50 cm²/s. Coverage: >95% visible defects, 0% hidden joints (BGA underside).

**X-ray inspection**: For BGA and QFN hidden joints. 2D X-ray at 20-160 kV, 10-100 μm resolution. Detects: voids (target <25% area), bridging, insufficient solder. Essential for BGA — AOI cannot see underside.

**Burn-in**: Power boards at 55-85°C for 24-168 hours. Precipitates early-life failures (infant mortality). Failure rate during burn-in: 1-5%. Boards surviving burn-in have 10-50× lower first-year field failure rate.

## Electrostatic Discharge (ESD) Control

Semiconductor devices damaged by ESD at 100V (MOSFET gate oxide) to 2000V (bipolar junctions). Human body model: 100 pF through 1.5 kΩ — walking on carpet generates 10,000-25,000V.

**Control measures**: Grounded wrist straps (<1 MΩ to ground). ESD-safe mats (10⁶-10⁹ Ω/sq). Ionizing air blowers. Humidity 40-60% RH. Antistatic bags for storage. ESD-safe smocks (conductive fibers). Conductive floor tiles (<10⁹ Ω to ground).

**Sensitive device handling**: MOSFETs, CMOS, and JFETs most vulnerable. Keep in antistatic packaging until placement. Touch grounded surface before handling. Use ESD-safe vacuum pickup, not plastic tweezers (triboelectric charge generation).

## IC Packaging

Semiconductor die must be packaged for handling, electrical connection, and environmental protection.

**Die attach**: Eutectic (Au-Si at 363°C, 2-5 seconds on gold-plated lead frame) or epoxy (silver-filled, cure at 150-180°C for 1-2 hours, 1.5-5.0 W/m·K thermal conductivity). Die thickness: 150-500 μm. Void target: <10% die area.

**Wire bonding**: 25 μm gold wire (ball bonding) or 25-50 μm aluminum wire (wedge bonding). Thermosonic: 200-250°C, 100-200 mN, ultrasonic 30-100 mW. Placement accuracy: ±5 μm. Pull strength: >40 mN (25 μm Au). Rate: 8-15 bonds/second. Typical IC: 8-500 bonds.

**Molding**: Transfer mold epoxy compound (80-90% silica filler by weight, 0.8-1.5 W/m·K thermal conductivity) at 170-180°C, 70-100 bar, 60-120 seconds. Post-mold cure: 175°C for 4-8 hours. Mold thickness over die: 0.5-1.5 mm.

**Package types**:
- DIP: dual in-line, 8-48 pins, 2.54 mm pitch
- SOP/SOIC: small outline, 8-28 pins, 1.27 mm pitch
- QFP: quad flat pack, 44-240 pins, 0.5 mm pitch
- QFN: quad flat no-lead, 16-72 pins, 0.5 mm pitch, exposed thermal pad
- BGA: ball grid array, 48-2000+ balls, 0.5-1.27 mm pitch, solder balls on bottom
- CSP: chip scale package, ≤1.2× die size

**Hermetic packaging** (military, aerospace, high-reliability): Ceramic (alumina) or metal (Kovar alloy). Seal by brazing (Cu-Ag at 780°C) or laser weld in N₂. Leak rate: <1×10⁻⁸ atm·cm³/s He. Moisture: <5000 ppm (Karl Fischer at 125°C for 24 hours). See [Ceramics](../materials/ceramics.md).

## Reliability and Failure Modes

**Solder joint fatigue**: Thermal cycling (-40 to +125°C, 1000-5000 cycles) causes cracking from CTE mismatch. Component ceramic: 6-7 ppm/°C, PCB FR-4: 14-17 ppm/°C. SAC305 (lead-free) stiffer than Sn/Pb — transfers more stress. Life: 5-20 years depending on severity.

**PCB failures**: Delamination from moisture vaporizing during reflow (FR-4 absorbs 0.1-0.3% water — bake at 125°C for 4-24 hours before assembly). PTH barrel cracking (Z-axis CTE mismatch). CAF (conductive anodic filament) growth — Cu migration along glass-epoxy interface under DC bias in humidity, causing shorts over months to years.

**Component failures**: Electrolytic capacitor drying (ESR increases, capacitance drops 20%/1000 hours at 85°C, rated life 2000-10,000 hours). Ceramic capacitor flex cracking from board bending. MOSFET gate oxide rupture (ESD/overvoltage). IC bond wire lift-off (thermal cycling). Mold compound popcorning (moisture in package vaporizes during reflow — bake components at 125°C/24h before assembly if stored in humidity >60% RH).

**Design for reliability**: Use components rated 25°C above maximum operating temperature. Derate voltage to 50-80% of rated maximum. Derate current to 50-70% of rated. Provide thermal relief pads for high-power components (4-8 thermal spokes connecting pad to copper pour). Maintain minimum 0.5 mm clearance between traces and board edge. Avoid 90° trace corners (use 45° miters or curved traces to reduce EMI reflections).

## PCB Design Rules

**Trace width by current**: Standard 1 oz (35 μm) copper at 10°C temperature rise:
- 0.25 mm trace: 1.0 A (external), 0.5 A (internal)
- 0.50 mm trace: 2.0 A (external), 1.0 A (internal)
- 1.00 mm trace: 3.5 A (external), 1.8 A (internal)
- 2.00 mm trace: 5.5 A (external), 3.0 A (internal)
- For higher currents, use copper pours or bus bars

**Impedance control**: For high-speed signals (clocks, USB, HDMI, Ethernet), trace impedance must match the system impedance (typically 50 Ω single-ended, 100 Ω differential). Microstrip impedance: Z₀ ≈ (87/√(εᵣ+1.41)) × ln(5.98h/(0.8w+t)), where h = dielectric thickness, w = trace width, t = copper thickness. For FR-4 (εᵣ = 4.5), 50 Ω requires approximately 0.18 mm trace over 0.2 mm dielectric.

**Via specifications**: Standard through-hole via: 0.3 mm finished hole diameter, 0.6 mm capture pad. Via resistance: 0.5-5 mΩ depending on plating thickness. Via inductance: ~1 nH per mm of board thickness. Current through via: derate to 50% of equivalent trace width. For high-current paths, use multiple vias in parallel (via stitching).

**Clearance and creepage**: Electrical safety requires minimum distances between conductors at different potentials:
- 30V: 0.1 mm clearance, 0.1 mm creepage
- 150V: 0.5 mm clearance, 0.5 mm creepage
- 300V: 1.5 mm clearance, 1.5 mm creepage
- 500V: 3.0 mm clearance, 3.0 mm creepage
- Values are for pollution degree 2, material group III. Derate at altitude (>2000m: multiply by altitude correction factor per IEC 60664).

## Solder Defect Analysis

**Common defects and causes**:

| Defect | Cause | Prevention |
|--------|-------|-------------|
| Cold solder joint | Insufficient temperature or time | Increase iron temperature; ensure 2-5 sec contact |
| Solder bridge | Excess solder or paste | Reduce paste volume; check stencil aperture |
| Tombstone | Uneven heating of chip component ends | Optimize reflow profile; ensure symmetrical pad design |
| Insufficient solder | Low paste volume or poor wetting | Increase stencil thickness; check flux activity |
| Solder balls | Paste slumping or moisture | Reduce paste slump; bake boards before printing |
| Voiding in BGA | Outgassing during reflow | Use longer soak profile; vacuum reflow for critical assemblies |
| Lifted pad | Excessive heat or mechanical stress | Reduce soldering temperature/time; avoid flexing board |
| Component shift | Surface tension imbalance during reflow | Symmetrical pad design; adequate paste volume |

### PCB Design Rules

**Trace width by current**: Standard 1 oz (35 μm) copper at 10°C temperature rise:
- 0.25 mm trace: 1.0 A (external), 0.5 A (internal)
- 0.50 mm trace: 2.0 A (external), 1.0 A (internal)
- 1.00 mm trace: 3.5 A (external), 1.8 A (internal)
- 2.00 mm trace: 5.5 A (external), 3.0 A (internal)

**Impedance control**: For high-speed signals (clocks, USB, HDMI, Ethernet), trace impedance must match the system impedance (typically 50 Ω single-ended, 100 Ω differential). Microstrip impedance: Z₀ ≈ (87/√(εᵣ+1.41)) × ln(5.98h/(0.8w+t)). For FR-4 (εᵣ = 4.5), 50 Ω requires approximately 0.18 mm trace over 0.2 mm dielectric.

**Via specifications**: Standard through-hole via: 0.3 mm finished hole diameter, 0.6 mm capture pad. Via resistance: 0.5-5 mΩ. Via inductance: ~1 nH per mm of board thickness.

**Clearance and creepage**: Electrical safety requires minimum distances between conductors at different potentials:
- 30V: 0.1 mm clearance, 0.1 mm creepage
- 150V: 0.5 mm clearance, 0.5 mm creepage
- 300V: 1.5 mm clearance, 1.5 mm creepage
- 500V: 3.0 mm clearance, 3.0 mm creepage

### Assembly Process Flow

Typical surface mount assembly sequence for a mixed-technology board (SMT + through-hole):

1. **Solder paste printing**: Apply paste to SMT pads via stencil printer (cycle time 15-30 seconds per panel)
2. **SMT inspection**: SPI (solder paste inspection) — 3D laser scanning checks paste volume and height (cycle time 10-20 seconds)
3. **SMT placement**: Pick-and-place machine positions all SMT components (cycle time 30-120 seconds)
4. **Pre-reflow AOI**: Optional inspection for placement accuracy before soldering
5. **Reflow soldering**: 3-6 minute conveyor oven profile
6. **Post-reflow AOI**: Inspect solder joints for defects (cycle time 15-30 seconds)
7. **Through-hole insertion**: Manual or automated insertion of through-hole components
8. **Wave soldering or selective soldering**: Solder through-hole joints
9. **ICT**: In-circuit test verifies component values and connectivity (10-60 seconds)
10. **Functional test**: Apply power and verify operation (1-10 minutes)
11. **Conformal coating**: Apply protective coating if required
12. **Final inspection and packaging**: Visual inspection, burn-in (optional), and ship

Typical first-pass yield for a well-controlled SMT line: 98-99.5%. Defects per million opportunities (DPMO) target: <500 for mature products. Process capability index Cpk >1.33 for all critical parameters (stencil printing volume, reflow peak temperature, placement accuracy).

### Reliability and Failure Modes

**Solder joint fatigue**: Thermal cycling (-40 to +125°C, 1000-5000 cycles) causes cracking from CTE mismatch. Component ceramic: 6-7 ppm/°C, PCB FR-4: 14-17 ppm/°C. SAC305 (lead-free) stiffer than Sn/Pb — transfers more stress. Life: 5-20 years depending on severity.

**PCB failures**: Delamination from moisture vaporizing during reflow (FR-4 absorbs 0.1-0.3% water — bake at 125°C for 4-24 hours before assembly). PTH barrel cracking (Z-axis CTE mismatch). CAF (conductive anodic filament) growth — Cu migration along glass-epoxy interface under DC bias in humidity, causing shorts over months to years.

**Component failures**: Electrolytic capacitor drying (ESR increases, capacitance drops 20%/1000 hours at 85°C, rated life 2000-10,000 hours). Ceramic capacitor flex cracking from board bending. MOSFET gate oxide rupture (ESD/overvoltage). IC bond wire lift-off (thermal cycling). Mold compound popcorning (moisture in package vaporizes during reflow — bake components at 125°C/24h before assembly if stored in humidity >60% RH).

### Moisture Sensitivity Levels

IC packages absorb moisture through the mold compound. During reflow, this moisture vaporizes rapidly, causing internal delamination or cracking (popcorning). MSL ratings define maximum floor life before baking is required:
- MSL 1: Unlimited floor life at ≤30°C/85% RH
- MSL 2: 1 year at ≤30°C/60% RH
- MSL 3: 168 hours (1 week) at ≤30°C/60% RH
- MSL 4: 72 hours at ≤30°C/60% RH
- MSL 5: 48 hours at ≤30°C/60% RH
- MSL 6: Must bake before use (mandatory bake at 125°C for 5-48 hours depending on package thickness)

Components stored in dry cabinets (<5% RH) have indefinite floor life. Dry pack bags (moisture barrier bag + desiccant + humidity indicator card) provide 12+ months shelf life.

## 6. Scaling Notes

- **Bench scale (prototyping)**: Hand soldering + toner transfer PCBs. Output: 1-10 boards per day. Single-sided, no plated holes. Suitable for prototype circuits and one-off designs.
- **Workshop scale**: Reflow oven + pick-and-place machine + UV exposure PCB. Output: 10-100 boards per day. Double-sided with through-hole plating. Sufficient for small-batch production.
- **Production scale**: Fully automated SMT line (stencil printer, pick-and-place, reflow, AOI, ICT). Output: 1000-10,000+ boards per day. Mixed SMT/through-hole. BGA capability with X-ray inspection.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cold solder joints | Iron temperature too low or contact time <2 sec | Increase tip temperature to 350°C (Sn/Pb) or 380°C (lead-free); ensure 2-5 sec contact |
| Solder bridges between fine-pitch leads | Excess paste volume or paste slump | Reduce stencil thickness; use Type 4 paste (20-25 μm particles) for 0.5 mm pitch |
| Tombstoning of chip components | Uneven pad thermal mass or reflow profile | Equalize pad sizes; extend soak zone to 120s; verify reflow zone uniformity ±5°C |
| BGA voids >25% area | Outgassing from moisture or flux | Bake boards at 125°C/24h; use longer soak profile; vacuum reflow for Class 3 assemblies |
| Component misalignment after reflow | Paste volume uneven or pad design asymmetry | Check stencil aperture blockage; verify pad symmetry per IPC-7351 |
| Delamination during reflow | Moisture in FR-4 substrate (>0.1%) | Bake bare boards at 125°C for 4-24h before assembly; control storage humidity <30% RH |
| ICT false failures | Fixture pin contact resistance, fixture contamination | Clean probe tips; verify pin spring force (>0.5 N); recalibrate fixture |
| Electrolytic capacitor venting | Reverse polarity installation or excessive ripple current | Verify polarity marking on BOM and board; derate ripple current to <70% of rated |

## 8. Safety

Electronics assembly involves hot solder, chemical exposures, electrical testing, and mechanical operations — each requiring specific protective measures.

**Soldering hazards**:
- **Lead exposure (Sn63/Pb37 solder)**: Lead is a cumulative neurotoxin. The primary exposure route during soldering is inhalation of lead oxide fumes from molten solder (solder melts at 183°C but significant lead fume generation begins above 500°C — well above normal tip temperatures of 320-380°C). The greater risk is hand-to-mouth contamination from handling solder wire and flux residues. Wash hands thoroughly before eating or drinking. Do not eat, drink, or apply cosmetics in soldering areas. Lead-free solders (SAC305, Sn/Cu) eliminate this risk but have higher melting points (217-227°C), requiring higher iron temperatures.
- **Solder fumes**: The visible "smoke" from soldering is primarily flux vapor, not metal fume. Rosin-core flux (colophony, abietic acid) produces formaldehyde, toluene, and phenol vapors when heated. These are respiratory sensitizers — prolonged exposure causes occupational asthma ("colophony asthma"). Use local exhaust ventilation (fume extractors with activated carbon and HEPA filters) positioned 5-15 cm from the solder joint. Minimum capture velocity: 0.3-0.5 m/s at the work point. In confined spaces or high-volume soldering stations, supplemental room ventilation should maintain <0.05 mg/m³ rosin flux particulate (OSHA PEL).
- **Thermal burns**: Soldering iron tips reach 320-420°C. Contact causes immediate second-degree burns. Iron rests must be stable and positioned to prevent accidental contact. Wave soldering machines contain 50-200 kg of molten solder at 250-270°C — splashes from wave soldering cause severe burns. Full-length heat-resistant gloves, face shield, and long-sleeved protective clothing required for wave soldering operation and maintenance.
- **Solder paste**: Contains fine metal powder (20-45 μm solder particles in flux vehicle). Lead-containing paste is a skin absorption and ingestion hazard. Wear nitrile gloves during stencil printing and paste handling. Solder paste misprints must be cleaned immediately using appropriate solvent and wipes (disposed as hazardous waste if lead-containing). Do not blow off excess paste with compressed air — creates airborne metal particles.

**Chemical hazards (PCB fabrication)**:
- **Ferric chloride (FeCl₃) etchant**: Corrosive (pH <1), causes skin and eye irritation. Stains clothing and skin brown (the iron hydrolyzes to Fe(OH)₃ on contact with skin). Splash goggles and nitrile gloves required. Spills: neutralize with sodium bicarbonate, then absorb with inert material.
- **Sodium hydroxide (NaOH) for resist stripping**: Concentrated (3-5%) at 50-60°C causes chemical burns. The hot alkali is particularly hazardous to eyes. Chemical splash goggles required (not just safety glasses).
- **PCB drilling**: Fiberglass dust from FR-4 substrate is a mechanical irritant (glass fibers embed in skin and respiratory tract). Use dust extraction at the drill head. Carbide drill bits (0.3-3.0 mm) rotate at 50,000-100,000 RPM — bit breakage sends high-velocity fragments outward. Safety glasses mandatory.

**Electrical testing**:
- In-circuit test (ICT) and functional test apply power (3.3V, 5V, ±12V DC) to assemblies. While these voltages are generally safe, high-current power supplies and energy storage in large capacitors pose hazards. Verify power is disconnected before probing live circuits. Capacitor discharge: large electrolytic capacitors (>1000 μF) can deliver significant current even after power removal — discharge through a bleeder resistor before handling.
- X-ray inspection equipment (20-160 kV) produces ionizing radiation. Modern X-ray systems are fully enclosed with interlocked shields that disable the X-ray tube when the enclosure is opened. Never bypass interlocks. Operators should wear dosimeter badges for cumulative exposure monitoring.

**ESD Control**: Semiconductor devices damaged by ESD at 100V (MOSFET gate oxide) to 2000V (bipolar junctions). Human body model: 100 pF through 1.5 kΩ — walking on carpet generates 10,000-25,000V. Control measures: grounded wrist straps (<1 MΩ to ground), ESD-safe mats (10⁶-10⁹ Ω/sq), ionizing air blowers, humidity 40-60% RH, antistatic bags for storage.

**General PPE and workstation requirements**:
- Safety glasses with side shields at all times in assembly areas
- Nitrile gloves for chemical handling and solder paste work
- Heat-resistant gloves for wave soldering and hot plate operations
- ESD wrist strap (grounded through <1 MΩ resistor) when handling components and assemblies
- No food or drink in assembly areas (lead contamination risk from Sn/Pb solder)
- First aid kit and eyewash station accessible within 10 seconds travel from all chemical and soldering workstations
- Fire extinguisher (CO₂ for electrical fires, dry chemical for general) at each soldering station

## 9. Quality Control

### Design for Reliability
- Use components rated 25°C above maximum operating temperature
- Derate voltage to 50-80% of rated maximum
- Derate current to 50-70% of rated
- Provide thermal relief pads for high-power components (4-8 thermal spokes connecting pad to copper pour)
- Maintain minimum 0.5 mm clearance between traces and board edge
- Avoid 90° trace corners (use 45° miters or curved traces to reduce EMI reflections)

### X-ray Void Measurement
For BGA solder joints, void area measured by 2D X-ray imaging. IPC-7095 standard: Class 1 (consumer) allows up to 30% void area; Class 2 (industrial) allows 25%; Class 3 (military/medical) allows 15% maximum. Large voids (>25% area) under the die shadow area are most critical — they cause hot spots and reduce thermal transfer to the PCB.

### Solder Paste Management
Refrigerated storage at 2-10°C. Allow 4-8 hours to equilibrate to room temperature before opening (condensation from opening cold paste ruins it). Stir before use (1-2 minutes with plastic spatula — do not use metal, which generates solder particles). Working life on stencil: 4-8 hours. Discard paste that has been on stencil >8 hours or shows viscosity changes.

## 10. Variations and Alternatives

| Assembly Method | Best For | Trade-off |
|----------------|----------|-----------|
| Hand soldering | Prototyping, field repair, low-volume (<50 units) | Slowest, lowest consistency; requires no automation equipment |
| Wave soldering | Through-hole boards, high-volume (>500 units) | Fast for TH; requires flux and preheat; incompatible with SMT on bottom side |
| Reflow soldering | SMT boards, all volumes | Highest throughput for SMT; requires stencil printer and oven; BGA inspection needs X-ray |
| Selective soldering | Mixed SMT/TH boards | Eliminates wave soldering mask step; slower than wave (point-by-point); robot cost $50K-$200K |
| Conformal coating (spray) | General environmental protection | Fast application; uneven thickness; requires masking |
| Conformal coating (selective dispense) | High-volume, precision coating | Consistent thickness; no masking needed; robot cost $30K-$100K |

## 11. References

- **[Basic Semiconductor Devices](../silicon/basic-devices.md)**: the devices being assembled into circuits
- **[Electrical Systems](electrical-systems.md)**: power distribution and wiring infrastructure
- **[Glass Fibers](../glass/fibers.md)**: fiberglass cloth for PCB substrate (FR-4)
- **[Electrolysis](../chemistry/electrolysis.md)**: copper production for PCB traces and wire
- **[Wafer Production](../silicon/wafering.md)**: silicon wafers that become IC die
- **[Passive Components](passive-components.md)**: resistors, capacitors, inductors mounted on PCBs
- **[Power Electronics](power-electronics.md)**: converters assembled using these techniques
- **[Polymers](../polymers/thermosets.md)**: epoxy resin for laminate and conformal coating

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md) • [All Domains](../index.md)*
