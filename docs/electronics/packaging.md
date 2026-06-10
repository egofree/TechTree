# IC Packaging & Interconnect

> **Node ID**: electronics.packaging
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`Electronics Assembly`](assembly.md)
> **Enables**: Various downstream capabilities
> **Timeline**: Years 30-50
> **Outputs**: packaged_ics, wire_bonds, leadframes, bga_substrates
> **Critical**: No

## Overview

Integrated circuit packaging and interconnect: die singulation from wafers, die attach to substrates, wire bonding and flip-chip interconnection, encapsulation in epoxy molding compounds, and advanced packaging (BGA, QFP, chip-scale). Packaging bridges bare silicon die and functional electronic assemblies, protecting the die while providing electrical, thermal, and mechanical interfaces.

IC packaging is the process of encapsulating a bare silicon die in a protective package that provides electrical connections to the outside world, mechanical support, thermal management, and environmental protection. The package is the interface between the fragile microscopic circuitry on the die and the macroscopic world of circuit boards, connectors, and systems. Without packaging, a bare die cannot be handled, connected, or used in any practical circuit.

Package types have evolved from the early dual in-line package (DIP) with through-hole leads, through surface-mount packages (QFP, SOIC), to modern area-array packages (BGA, CSP) that place connections under the die rather than around its perimeter. Each generation increases the number of available connections per unit of board area while decreasing the package footprint. The ball grid array (BGA) package, with its array of solder balls on the package bottom, is the current mainstream for complex ICs, offering hundreds to thousands of connections in a compact form factor.

Primary outputs: `packaged_ics`, `wire_bonds`, `leadframes`, `bga_substrates`.

The packaging process must protect the die from moisture, ionic contamination, mechanical shock, and thermal cycling stress while maintaining reliable electrical connections for the device's rated lifetime (typically 10-20 years in the field). Package-related failures, including wire bond lift-off, die attach delamination, and moisture-induced corrosion, account for a significant fraction of field returns.

The transition from through-hole packaging (DIP) to surface-mount packaging (QFP, SOIC) in the 1980s enabled dramatically higher component density on printed circuit boards. Surface-mount packages have leads that solder directly to pads on the board surface rather than passing through holes, allowing components on both sides of the board and eliminating the board real area consumed by through-holes. The subsequent transition to area-array packages (BGA) moved the connections underneath the package body, further increasing I/O density and reducing electrical parasitics (shorter signal paths with lower inductance).

## Prerequisites

### Materials

- Eutectic solder (63Sn/37Pb) or lead-free solder (SAC305: 96.5Sn/3.0Ag/0.5Cu) for die attach
- Silver-filled epoxy (conductive die attach adhesive) for applications requiring lower processing temperature
- Gold bonding wire (25 μm diameter, 99.99% purity) or aluminum wire (25-50 μm, for power devices)
- Epoxy molding compound (EMC): silica-filled cresol novolac epoxy with catalyst, flame retardant, and stress relief additives
- Copper alloy leadframes (C194 or C7025) or organic/BGA substrates (BT laminate with copper traces)
- Solder balls (Sn-Ag-Cu) for BGA assembly, 0.2-0.8 mm diameter

### Equipment

- [Electronics Assembly](assembly.md) — tool dependency
- Wafer probe tester for pre-packaging die sort (known-good-die selection)
- Back grinding (backlap) equipment for wafer thinning (from 725 μm to 100-200 μm)
- Dicing saw with diamond blade for wafer singulation
- Die attach machine (epoxy dispenser or eutectic scrub head) with vacuum pick-up
- Wire bonder: thermosonic ball bonder (for Au wire) or ultrasonic wedge bonder (for Al wire)
- Transfer molding press for epoxy encapsulation
- Trim and form press for leadframe singulation and lead forming
- Marking system (laser or ink) for device identification
- Package test system (handler + ATE) for final test and burn-in

### Knowledge

- Wire bonding parameters: bond force (20-120 grams), ultrasonic power (0.1-1.0 W), bond time (10-50 ms), and stage temperature (150-250°C for thermosonic Au ball bonding). These four parameters must be optimized for each pad metallization and wire diameter combination.
- Molding compound rheology: transfer mold pressure (50-150 kg/cm²), mold temperature (170-180°C), and cure time (60-120 seconds). The compound must fill the mold cavity without trapping voids and without sweeping wire bonds out of position.
- Die attach material selection: matching the coefficient of thermal expansion (CTE) between die, attach material, and substrate to minimize thermal cycling stress. Eutectic solder provides the best thermal conductivity but requires 250°C processing. Silver epoxy cures at 150-180°C but has lower thermal conductivity.
- Solder bump formation for flip-chip: electroplating or screen printing of solder onto die bond pads, followed by reflow to form spherical bumps

### Infrastructure

- Cleanroom (Class 1,000 or better) for die attach and wire bonding operations
- ESD-controlled workstations with grounded wrist straps, conductive flooring, and ionized air for all IC handling
- Oven for die attach epoxy cure (150-180°C, 30-60 minutes) or eutectic die attach reflow (250°C peak)
- Transfer molding press with preheated cavities and post-mold cure oven (175°C, 4-8 hours)
- Burn-in oven for accelerated stress testing (125°C, 24-168 hours under electrical bias)
- Laser marking system with device-specific font and code libraries

## Process Description

### Step-by-Step Procedure

1. **Wafer probe test**: Probe each die on the wafer with a probe card that contacts the bond pads. Apply test patterns to identify functional die. Ink or map the failed die locations. Only known-good die proceed to packaging, saving the cost of packaging defective devices.
2. **Back grinding (backlap)**: Grind the wafer backside from its original 725 μm thickness to 100-200 μm (or thinner for mobile applications, down to 50 μm). Use coarse grinding followed by fine grinding to control subsurface damage. Clean the thinned wafer in a spin rinser.
3. **Wafer dicing**: Mount the wafer on a dicing tape (UV-curable adhesive on a stainless steel ring frame). Cut the wafer into individual die using a diamond-impregnated blade rotating at 20,000-40,000 RPM with water coolant. Blade kerf is 20-40 μm. Die sizes range from 1×1 mm to 20×20 mm.
4. **Die attach**: Pick the die from the dicing tape with a vacuum collet. Place onto the leadframe die pad or substrate with die attach material. For epoxy attach: dispense a controlled pattern of silver-filled epoxy, place the die, and cure in an oven. For eutectic attach: scrub the die against the Au-plated die pad at 250°C to form the Au-Si eutectic bond. The attach must be void-free; trapped air pockets create hot spots.
5. **Wire bonding**: Connect each die bond pad to its corresponding leadframe or substrate pad with fine wire. For Au ball bonding: spark-melt the wire tail into a ball (0.5-0.8× wire diameter), press the ball onto the die pad with force and ultrasonics (first bond), loop the wire to the lead, and press a stitch bond onto the lead (second bond), then cut the wire. A complex IC may have 500-5,000 wire bonds per device.
6. **Encapsulation**: Load the wired leadframe strips into a transfer mold cavity. Preheat the molding compound pellets to 80-90°C for softening, then inject at high pressure (50-150 kg/cm²) into the mold at 170-180°C. The liquid epoxy fills around the die and wires. Cure for 60-120 seconds in the mold, then post-cure in an oven for 4-8 hours to complete cross-linking.
7. **Trim and form**: Singulate the leadframe strips into individual packages by punching or cutting. Form the leads to the required shape (gull-wing for surface mount, straight for through-hole). Deburr the cut edges.
8. **Mark and test**: Laser mark the device with part number, lot code, date code, and pin 1 indicator. Test each device on automated test equipment (ATE) for DC parametrics, functional performance, and speed binning. Burn-in at elevated temperature under bias screens out early-life failures.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Au wire diameter | 18-33 μm | Thinner wire for fine-pitch, thicker for power |
| Ball bond force | 20-120 grams | Optimized per pad metallization |
| Ultrasonic power (bonding) | 0.1-1.0 W | Too little = non-stick; too much = pad damage |
| Stage temperature (bonding) | 150-250°C | Higher for harder pad metallizations |
| Mold transfer pressure | 50-150 kg/cm² | Must fill without wire sweep |
| Mold temperature | 170-180°C | Must cure without thermal damage to die |
| Post-mold cure | 175°C, 4-8 hours | Completes epoxy cross-linking for reliability |

## Safety Considerations

- **Lead exposure**: Lead-based solders (63Sn/37Pb) contain toxic lead. Handle with nitrile gloves. Wash hands before eating. Even lead-free solders contain tin and silver with their own exposure limits. Local exhaust ventilation at soldering stations captures fumes.
- **Epoxy sensitization**: Molding compounds and die attach epoxies contain resin systems that cause allergic skin sensitization with repeated exposure. Once sensitized, even trace exposure triggers dermatitis. Wear nitrile gloves and avoid skin contact with uncured epoxy.
- **Wire bonder ultrasonics**: The ultrasonic transducer on a wire bonder operates at 60-120 kHz. Direct contact with the vibrating capillary during bonding causes hand-arm vibration exposure. Operators must not contact the bonding tool during operation.
- **Leadframe sharp edges**: Stamped and etched leadframes have sharp metal edges that cause lacerations. Wear cut-resistant gloves when handling leadframe strips.
- **Dicing blade hazard**: The diamond dicing blade rotates at 20,000-40,000 RPM. Blade contact causes severe injury. The dicing saw is fully enclosed with interlocked safety doors.

### Personal Protective Equipment

- Nitrile gloves when handling lead-based solder, uncured epoxy, or molding compound pellets
- Cut-resistant gloves (Kevlar or steel mesh) when handling leadframe strips before encapsulation
- Safety glasses with side shields in the dicing and trim/form areas (flying debris hazard)
- ESD wrist strap grounded to the workstation at all die attach and wire bonding stations
- Hearing protection near the trim/form press (punch press operation exceeds 90 dBA)

### Emergency Procedures

- Lead solder ingestion: Seek medical attention. Do not induce vomiting. Inform medical staff of lead exposure.
- Epoxy skin contact: Wash immediately with soap and water. Remove contaminated clothing. If sensitization reaction occurs (rash, itching), seek medical evaluation and reassign to non-epoxy tasks permanently.
- Dicing blade injury: Apply direct pressure to control bleeding. The diamond blade can cause deep lacerations. Seek medical attention immediately.
- Molding press entrapment: The transfer mold press has two-hand safety controls and light curtains. Never defeat these interlocks. If a hand is caught, hit the emergency stop and reverse the press hydraulics.

## Quality Control

### Acceptance Criteria

- **Wire bonds**: Destructive wire pull test strength above 3× wire minimum breaking force (per MIL-STD-883). Ball shear strength above 30 grams (for 25 μm Au wire on Al pad). No non-stick-on-die (NSOD) defects visible under 100× optical inspection.
- **Die attach**: X-ray inspection showing void area below 10% of total die attach area. Die shear strength above 2.5 kg for a 5×5 mm die.
- **Package marking**: Legible at 5× magnification. Correct part number, lot code, and date code. Pin 1 indicator visible.
- **Encapsulation**: No visible cracks, voids, or incomplete fill. Package dimensions within ±0.1 mm of specification.

### Testing Methods

- Wire pull test: hook under the wire loop, pull perpendicular to the die surface at controlled rate. Record breaking force and failure mode (wire break = acceptable, ball lift or pad lift = reject). Test 5-10 wires per lot destructively.
- Ball shear test: shear the ball bond off the pad with a calibrated tool. Record shear force. Low shear force indicates contamination or insufficient bonding energy.
- X-ray inspection of die attach: detects voids trapped under the die that would cause hot spots during operation. Void area calculated by image analysis software.
- Visual inspection under 40-100× microscope: check for wire bond placement accuracy, wire loop height and shape, foreign material on the die surface, and encapsulation defects.
- Burn-in test: operate the device at 125°C under electrical bias for 24-168 hours to screen out early-life failures (infant mortality). Devices that pass burn-in have significantly lower field failure rates.

### Sampling Protocol

- 100% optical inspection of wire bonds on every device (automated vision system or manual microscope)
- Destructive wire pull test: 5 wires per device on 3 devices per lot (or per MIL-STD-883 sample plan)
- X-ray die attach void inspection on 5 devices per lot; reject the lot if any device exceeds 10% void area
- Package dimensions checked on 10 devices per lot with optical comparator or CMM
- Burn-in test 100% of devices for critical applications; sample burn-in for consumer-grade parts
- Track wire bond pull strength data on SPC charts; investigate any trend below the control limit

## Scaling Notes

IC packaging scales from manual laboratory operations (hand-placing die with tweezers under a microscope, hand-bonding wires one at a time) to fully automated production lines processing thousands of units per hour. A modern wire bonder completes 10-20 bonds per second, with automated pattern recognition aligning to bond pads with ±2 μm accuracy. A single wire bonder processes 500-1,000 devices per hour.

The capital cost of a packaging production line is dominated by the wire bonders (each costing $200,000-500,000) and the molding presses. Throughput is typically limited by wire bonding, as complex devices require 500-5,000 bonds each. Multiple bonders run in parallel to match the throughput of the upstream die attach and downstream molding operations.

Flip-chip bonding is an alternative to wire bonding where solder bumps are formed directly on the die's bond pads by electroplating or screen printing, then reflowed to form spherical bumps (80-200 μm diameter). The die is flipped upside-down onto the substrate, and the bumps are reflowed to create electrical connections. Flip-chip provides shorter interconnections (lower inductance, higher speed), higher connection density, and connections anywhere on the die surface, not just at the periphery. The tradeoff is underfill dispensing (epoxy between die and substrate to compensate for CTE mismatch) and the inability to visually inspect hidden solder joints.

The thermal management challenge in IC packaging increases with each chip generation. Modern high-performance processors generate heat fluxes exceeding 100 W/cm². The package must provide a low-thermal-resistance path from the die to the external heat sink through thermally conductive die attach material, metal heat spreader lids (copper or aluminum), and thermal interface material (TIM) between the package and the heat sink.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Non-stick on die (NSOD) | Contaminated bond pad (organic film >5 nm thick), insufficient ultrasonic power, or wrong stage temperature (<150°C for thermosonic Au bonding) | Clean bond pads with UV ozone (15-30 min exposure) or oxygen plasma (100 W, 5 min, 0.5 Torr O₂) before bonding; increase ultrasonic power in 0.05 W steps from minimum until bond forms; raise stage temperature to 200-250°C for hard pad metallizations |
| Wire sweep during molding | Excessive mold transfer pressure (>150 kg/cm²), high-viscosity molding compound, or wire loop height too tall (>300 μm) | Reduce transfer pressure to 50-100 kg/cm²; preheat molding compound pellets to 80-90°C for 2-3 min to lower viscosity; use lower-viscosity compound grade (melt viscosity <100 Poise at 175°C); optimize wire loop height to 200-250 μm for 25 μm wire |
| Die attach voids | Trapped air from improper epoxy dispensing pattern, or outgassing during cure (moisture in epoxy >0.5%) | Optimize epoxy dispense pattern (X-pattern for dies <5×5 mm, spiral for larger dies, ensuring full coverage with no air pockets); use vacuum-assisted epoxy dispense (vacuum to 10 Torr for 30 seconds after dispense); add a vacuum bake step at 80°C, 10 Torr for 15 minutes before cure |
| Package delamination | Poor adhesion between molding compound and die pad (surface contamination, moisture absorption in compound >0.3%) | Clean leadframes before die attach (ultrasonic clean in isopropyl alcohol 5 min, dry at 120°C for 30 min); apply adhesion promoter (silane coupling agent, 0.5-2% by weight in compound formulation); verify molding compound stored in sealed containers with desiccant at <5°C (shelf life 6-12 months at 5°C, 3 months at 25°C) |
| Cracked die during wire bonding | Excessive bond force (>120 grams) on a thinned die (below 150 μm thickness), or uneven die attach (void area >10%) | Reduce bond force to 20-60 grams for dies below 150 μm; verify die attach uniformity with X-ray (voids <10% total area); consider film-over-wire (FOW) molding for very thin die (<100 μm) to protect during molding |
| Lead coplanarity failure | Bent leads from trim/form tooling wear (punch clearance >0.02 mm), or improper handling (vacuum pickup force >5 N) | Replace trim/form punch and die set (tool life: 500,000-2,000,000 strokes); verify leadframe alignment during forming (±0.05 mm positional accuracy); handle packages with vacuum pickup (0.5-2.0 N force, not mechanical grippers); coplanarity specification: <0.1 mm for surface-mount packages |
| Open wire bonds after burn-in | Kirkendall voiding at the Au-Al bond interface (purple plague) from excessive temperature-time exposure (>300°C equivalent for >100 hours) | Lower burn-in temperature to 125°C max for Au-Al bonds; use Au-Au wire bonding (requires Au-plated bond pads, adds cost); limit Au-Al exposure to below 200°C for <168 hours; inspect bonds after burn-in with wire pull test (minimum 3 grams for 25 μm Au wire) |
| Solder balling on BGA rework | Oxidized solder balls or insufficient flux activity during reballing | Use fresh solder balls (bright, no dull surface); apply tacky flux (no-clean type, 1-2% solids content); verify reflow profile peaks at 235-250°C for SAC305 (time above liquidus 60-90 seconds) |

## Variations and Alternatives

- **Flip-chip (C4)**: Solder bumps on die pads, die flipped onto substrate, reflowed to connect. Higher I/O density, better electrical performance (shorter connections), but requires underfill and hidden-joint inspection. Dominant for high-performance processors and ASICs.
- **Chip-scale packaging (CSP)**: Package footprint no larger than 1.2× the die area. Achieved by using the die itself as part of the package structure. Used in mobile devices where board space is limited.
- **Wafer-level packaging (WLP)**: Packaging steps performed at wafer level before dicing. Redistribution layer (RDL) reroutes bond pads to a bump array, then the wafer is molded and diced. Eliminates traditional die attach and wire bonding. Lowest cost per unit for high-volume production.
- **System-in-package (SiP)**: Multiple dies (processor, memory, RF, sensors) integrated in a single package. Connected by wire bonds, flip-chip, or embedded die technology. Enables complex system integration without advanced monolithic integration.

Wafer-level packaging, SiP, and 2.5D/3D packaging using through-silicon vias (TSVs) represent the current frontier. These technologies enable continued system performance improvement even as transistor scaling slows, by integrating multiple functions in a single package rather than relying solely on smaller transistors.

Package reliability testing subjects the packaged device to accelerated stress conditions to predict field failure rates. Temperature cycling (-65°C to +150°C, 500-1000 cycles), thermal shock, moisture resistance (85°C/85% RH, 168 hours), and mechanical shock/vibration are standard JEDEC test procedures. Each test targets specific failure mechanisms: die attach delamination, wire bond fatigue, solder joint cracking, or moisture-induced corrosion.

The underfill process in flip-chip packages dispenses an epoxy material between the die and substrate that fills the gap around the solder bumps. Underfill compensates for the thermal expansion mismatch between the silicon die and organic substrate, preventing solder bump fatigue failure during temperature cycling. The underfill material must have the right viscosity for capillary flow, the right coefficient of thermal expansion, and good adhesion to both the die passivation and the substrate.

Bare silicon dies are extremely fragile and must be handled with vacuum pickup tools in a cleanroom environment. Even microscopic contamination on a bond pad prevents reliable wire bonding. Packaged ICs are more robust but still sensitive to electrostatic discharge (ESD): a static electricity spark that is imperceptible to humans can destroy the input protection circuitry of a MOSFET device. All IC handling, testing, and assembly must occur at ESD-controlled workstations with grounded wrist straps, conductive flooring, and ionized air.

The trend toward smaller, thinner packages with higher I/O counts drives continuous innovation in packaging technology. Wafer-level packaging (WLP) performs the packaging steps at the wafer level before dicing, eliminating the traditional die-attach and wire-bond steps. System-in-package (SiP) integrates multiple dies (processor, memory, RF, sensors) in a single package. 2.5D and 3D packaging stack multiple dies vertically using through-silicon vias (TSVs) for inter-die connections. These advanced packaging technologies enable continued system performance improvement even as transistor scaling slows.

Copper wire bonding has partially replaced gold wire bonding in cost-sensitive applications. Copper wire offers higher thermal and electrical conductivity than gold at lower material cost, but copper oxidizes readily and is harder than gold, requiring more careful control of bonding parameters (higher ultrasonic power, protective gas atmosphere during ball formation). Copper wire bonds also require different pad metallization or a palladium-coated copper wire to prevent intermetallic growth at the bond interface.

Plasma cleaning of bond pads before wire bonding removes organic contamination that causes NSOD (non-stick on die) defects. Oxygen or argon plasma sputters away thin organic films without damaging the underlying aluminum pad metallization. This step has become standard practice for fine-pitch wire bonding below 50 μm pad pitch, where even nanometer-scale contamination layers prevent reliable thermosonic bonding. Without plasma cleaning, NSOD defect rates can exceed 1% on fine-pitch devices, which is unacceptable for high-reliability applications.

Mold compound selection is driven by three competing requirements: low viscosity for filling without wire sweep, high glass transition temperature (Tg) for reliability during solder reflow, and low moisture absorption to prevent popcorning during board-level assembly. Halogen-free molding compounds have largely replaced brominated flame retardants in response to environmental regulations, requiring reformulation of the resin system to maintain flame retardancy without halogen compounds.

## References

- [Electronics](index.md) — parent capability
- [Electronics Domain](./index.md) — domain overview and related capabilities
- [Electronics Assembly](assembly.md) — upstream dependency (tool)

### Material Handling

- Handle bare die only with vacuum pickup tools in a cleanroom environment. Even microscopic contamination on a bond pad prevents reliable wire bonding.
- Protect packaged ICs from electrostatic discharge (ESD) at all handling stages: conductive trays, grounded workstations, ESD bags for shipping. A static spark imperceptible to humans can destroy MOSFET input protection circuitry.
- Store molding compound pellets in sealed containers with desiccant. Moisture absorption causes voids and reduces adhesion during molding.
- Keep gold bonding wire on sealed spools in a dry nitrogen cabinet. Wire contamination from airborne organics causes NSOD defects.
- Inspect solder balls for oxidation before BGA assembly; oxidized balls do not reflow properly and cause open connections.
- Handle dicing tape and UV-release frames carefully: wrinkles in the tape cause die to fly off during dicing, destroying die and damaging the blade.

---
*Part of the [Bootciv Tech Tree](../../index.md) · [Electronics](./index.md) · [All Domains](../../index.md)*
