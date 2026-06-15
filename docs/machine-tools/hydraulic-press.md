# Hydraulic Press

> **Node ID**: machine-tools.hydraulic-press
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`machine-tools.joining`](joining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 15-25
> **Outputs**: formed_parts, stamped_parts, compressed_assemblies
> **Critical**: No — mechanical screw presses and fly presses can substitute for many operations, but the hydraulic press is the only practical route for high-force, slow-speed forming

## Overview

A hydraulic press multiplies a small input force into a large output force using Pascal's law — pressure applied to a confined fluid transmits equally in all directions. A small-diameter pump cylinder pressurizes hydraulic oil, which acts on a large-diameter ram cylinder. The force multiplication equals the ratio of ram area to pump area: F_out = F_in × (A_ram / A_pump). A shop press with a 150 mm diameter ram and a 20 mm diameter pump cylinder multiplies force 56×. At 20 MPa system pressure, the 150 mm ram produces 350 kN (35 tonnes) of force.

The hydraulic press occupies a specific niche in the machine shop: high force at low speed with controllable pressure. Hammers deliver impact energy; mechanical presses deliver force at a specific crank angle; hydraulic presses deliver steady, adjustable force at any point in the stroke. This makes them ideal for pressing bearings, bending thick bracketry, stamping small parts, straightening shafts, and laminating materials. For [metal forming](forming.md) operations requiring controlled deformation rather than impact, the hydraulic press is the standard tool.

Downstream, the hydraulic press enables [deep drawing](forming.md) of sheet metal into cup-shaped parts, [compression molding](compression-press.md) of thermoset polymers and rubber, and bearing installation in every machine tool built after the foundry stage.

The hydraulic press is one of the simplest high-force machines to build. A hand pump, a cylinder, a ram, and a frame are sufficient for a functional 10-35 tonne press. No gears, no flywheel, no precision bearings beyond the cylinder bore. The trade-off is speed — hydraulic presses move slowly (5-20 mm/s approach, 1-5 mm/s at force). For high-speed stamping operations, a mechanical press is better; for controlled-force applications, the hydraulic press has no equal.

Pascal's law governs the force multiplication: pressure applied to a confined fluid transmits equally in all directions. The force on the ram equals the system pressure times the ram bore area. A 20 MPa pump acting on a 150 mm diameter ram produces 353 kN (35 tonnes). The same pump acting on a 250 mm ram produces 982 kN (100 tonnes). The pump, not the cylinder, is the limiting component — a 20 MPa hand pump produces the same maximum force regardless of how fast the operator pumps.

## Prerequisites

- [Steel plate](../metals/iron-steel.md) — for frame, bed, and ram (minimum 10 mm thick for structural members)
- [Seamless steel tubing](forming.md) — for hydraulic cylinder bore (or bored solid bar)
- [Hydraulic seals](../polymers/rubber.md) — O-rings, U-cup seals (nitrile or polyurethane)
- [Hydraulic oil](../chemistry/lubricants.md) — ISO VG 32 or 46 (or filtered vegetable oil as substitute)
- [Pressure gauge](../measurement/index.md) — 0-30 MPa range
- [Hand pump or powered pump](../energy/index.md) — rated to 20+ MPa
- [Machining capability](machining.md) — for boring cylinder, machining ram, and facing mating surfaces
- [Welding capability](joining.md) — for frame fabrication

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame) | 100-200 kg | A36 or equivalent, 12-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, no welding needed) |
| Steel bar (ram) | 20-50 kg | 1045 or 4140, 80-150 mm diameter, hardened to 45-50 HRC | [Iron & Steel](../metals/iron-steel.md) | Ground and polished mild steel (shorter life) |
| Seamless tubing (cylinder) | 5-15 kg | Honed ID, 80-150 mm bore, 10 mm wall | [Forming](forming.md) | Bored solid bar (more machining) |
| Hydraulic seals | 1 set | U-cup or O-ring, matched to bore diameter | [Elastomers](../polymers/rubber.md) | Leather cup packing (lower pressure limit, ~7 MPa) |
| Hydraulic oil | 10-30 L | ISO VG 32 or 46, filtered to 25 μm | [Lubricants](../chemistry/lubricants.md) | Filtered vegetable oil (degrades faster) |
| Pressure gauge | 1 | 0-30 MPa, Bourdon tube type | [Measurement](../measurement/index.md) | None — pressure indication is safety-critical |
| Bolts and nuts | 2-5 kg | Grade 8.8 or higher, M12-M20 | [Fasteners](../metals/iron-steel.md) | Riveted joints (non-adjustable) |
| Welding consumables | 5-10 kg | E7018 electrodes or equivalent | [Joining](joining.md) | Bolted flanges (heavier) |

## Process Description

### Frame Construction

1. **Cut frame plates**: Cut two side plates (500 × 800 mm, 15 mm thick) and a bed plate (400 × 500 mm, 25 mm thick) from steel plate using a torch or saw. A C-frame design uses a single side with a deep throat; an H-frame uses two side plates with tie rods.
2. **Machine mating surfaces**: Mill the top and bottom faces of the side plates flat and parallel to 0.05 mm. The ram guide bore (if integrated into the frame) must be bored perpendicular to the bed within 0.02 mm per 100 mm.
3. **Weld or bolt frame**: For an H-frame press, weld the side plates to the bed plate with full-penetration fillet welds (E7018, 3.2 mm electrode). Alternatively, use bolted flanges with Grade 8.8 bolts for disassembly. Reinforce corners with gusset plates (10 mm, triangular, 100 mm legs).
4. **Install tie rods** (H-frame): Thread four tie rods (M20, 500-600 mm long) through the side plates. Tighten nuts alternately and evenly to 300 N·m. The tie rods preload the frame to resist the working force without joint separation.

**Calibration**: Place a precision straightedge across the bed. Check flatness with feeler gauges — maximum deviation 0.05 mm per 100 mm. Check that the ram guide bore is perpendicular to the bed with a machinist's square and dial indicator.

**Expected performance**: Frame deflection at rated load: <0.5 mm (H-frame), <1.0 mm (C-frame). Bed flatness: ±0.05 mm.

### Cylinder and Ram

5. **Prepare cylinder bore**: If using seamless tubing, hone the bore to a 0.8 μm Ra finish or better. If boring from solid bar, bore to diameter, then hone. The bore must be round within 0.02 mm and straight within 0.05 mm over the full stroke length.
6. **Machine ram**: Turn the ram from 1045 or 4140 steel bar. Diameter is 0.05-0.10 mm smaller than the cylinder bore (clearance fit for the seal). Surface finish: 0.4 μm Ra or better (polished). Harden to 45-50 HRC for wear resistance.
7. **Install seals**: Fit U-cup seals into the cylinder head (gland nut). Seal orientation: cup faces the pressure side. Install O-ring in the gland nut for static seal between cylinder head and cylinder body. Coat all seals with hydraulic oil before assembly.
8. **Assemble cylinder**: Insert ram into cylinder bore through the gland nut. Thread gland nut into cylinder body (or bolt on). The ram should slide smoothly under hand pressure with no binding.

**Calibration**: Pressurize the cylinder to 5 MPa with no load. Hold for 10 minutes. Inspect all seals and connections for leaks. Zero leaks acceptable. Measure ram-to-bore concentricity with a dial indicator: runout <0.05 mm.

**Expected performance**: Ram force: F = P × A, where P = system pressure and A = ram bore area. At 20 MPa with 150 mm bore: F = 20 × π/4 × 150² = 353 kN (35 tonnes). Seal life: 6-12 months continuous use.

**Materials specifications**: Seamless steel tubing or 4140 solid bar (80-150 mm bore × stroke length + 100 mm), U-cup seals (nitrile, matched to bore), O-rings (nitrile), gland nut (1045 steel).

### Hydraulic System

9. **Mount cylinder**: Bolt the cylinder to the top of the frame (H-frame) or the upper cross-member (C-frame). Align the ram axis perpendicular to the bed within 0.1 mm per 100 mm using a machinist's square.
10. **Connect pump**: Connect the hand pump (or power unit) to the cylinder via hydraulic hose rated to at least 1.5× the maximum working pressure. Install a pressure gauge in the line between pump and cylinder.
11. **Fill and bleed**: Fill the reservoir with filtered hydraulic oil. Cycle the pump 10-20 times with the ram unloaded to purge air from the system. Air in the system causes spongy feel and erratic force.
12. **Install pressure relief valve**: Set to 110% of the rated maximum pressure. This prevents overloading the frame or bursting the cylinder. Verify by pumping to relief pressure and confirming the gauge reading.
13. **Add stroke limiter**: Install adjustable mechanical stops to prevent the ram from over-traveling. This protects the bed and workpiece from damage.

**Calibration**: Place a calibrated load cell between the ram and bed. Pump to the relief valve set pressure. Record the gauge reading and the measured force. Verify the force matches the design calculation within ±5%. Check parallelism: place a straightedge across the bed, lower the ram until it contacts the straightedge at two points. Measure gap between ram face and straightedge at four corners — maximum deviation 0.05 mm per 100 mm.

**Expected performance**: Ram approach speed: 5-20 mm/s (hand pump), 2-8 mm/s (powered at full force). Cycle time (150 mm stroke): 15-30 s (hand pump), 20-50 s (powered).

**Materials specifications**: Hand pump or power unit rated to 20+ MPa, hydraulic hose (rated to 30 MPa minimum), 0-30 MPa Bourdon tube pressure gauge, pressure relief valve (pilot-operated).

## Quantitative Parameters

### Force vs. Pressure Reference

| System Pressure (MPa) | 80 mm ram | 100 mm ram | 150 mm ram | 200 mm ram |
|------------------------|-----------|------------|------------|------------|
| 10 | 50 kN (5 t) | 79 kN (8 t) | 177 kN (18 t) | 314 kN (32 t) |
| 15 | 75 kN (8 t) | 118 kN (12 t) | 265 kN (27 t) | 471 kN (48 t) |
| 20 | 100 kN (10 t) | 157 kN (16 t) | 353 kN (36 t) | 628 kN (64 t) |
| 25 | 126 kN (13 t) | 196 kN (20 t) | 442 kN (45 t) | 785 kN (80 t) |

### Operating Parameters by Pump Type

| Parameter | Hand Pump | Powered (5 L/min) | Powered (20 L/min) |
|-----------|-----------|-------------------|---------------------|
| Ram force (150 mm bore, 20 MPa) | 350 kN (35 t) | 350 kN (35 t) | 350 kN (35 t) |
| Ram approach speed | 5-20 mm/s | 0.5-2 mm/s at force | 2-8 mm/s at force |
| Ram return speed | 10-30 mm/s | 2-5 mm/s | 5-15 mm/s |
| Cycle time (150 mm stroke) | 15-30 s | 60-120 s | 20-50 s |
| Pump effort | 100-200 N per stroke | N/A | N/A |
| Oil volume per stroke (150 mm bore, 100 mm travel) | 0.18 L | — | — |

### Common Press Sizes and Applications

| Ram Bore (mm) | Force at 20 MPa (tonnes) | Typical Application |
|----------------|--------------------------|---------------------|
| 80 | 10 | Light-duty: pin insertion, small bracket bending, staking |
| 100 | 16 | General shop: bearing pressing, bracket forming, bushing installation |
| 150 | 35 | Medium-duty: shaft straightening, die set pressing, structural bending |
| 200 | 64 | Heavy-duty: large bearing pressing, heavy stamping, laminating |
| 250 | 125 | Production: deep drawing, large part stamping, plate bending |

### Hydraulic System Parameters

| Parameter | Value |
|-----------|-------|
| System pressure range | 10-25 MPa (typical: 20 MPa) |
| Ram bore sizes | 80, 100, 150, 200, 250 mm (standard) |
| Stroke length | 100-300 mm (design-dependent) |
| Frame deflection at rated load | <0.5 mm (H-frame), <1.0 mm (C-frame) |
| Bed flatness | ±0.05 mm |
| Seal life | 6-12 months continuous use; inspect monthly |
| Duty cycle | Intermittent — 10 min on, 5 min off (thermal limit on pump) |
| Recommended reservoir volume | 3× pump flow rate per minute |

### Common Press Operations and Force Requirements

| Operation | Material | Required Force (kN) | Notes |
|-----------|----------|---------------------|-------|
| Bearing installation (30 mm OD) | Steel/bronze | 10-30 kN | Press fit: 0.02-0.05 mm interference |
| Bushing installation (50 mm OD) | Bronze | 20-50 kN | Press fit: 0.03-0.07 mm interference |
| Shaft straightening (25 mm dia.) | Steel | 30-80 kN | Requires V-blocks and dial indicator |
| Small bracket bending (3 mm × 50 mm) | Mild steel | 20-40 kN | V-die width: 3× material thickness |
| Punching holes (6 mm dia. × 3 mm plate) | Mild steel | 50-80 kN | Clearance: 10-15% of material thickness |
| Pressing shaft into gear (35 mm bore) | Steel | 50-100 kN | Shrink fit: heat gear to 200°C or press at room temperature |

## Scaling Notes

- A 35-tonne H-frame press (150 mm ram at 20 MPa) handles most shop work: bearing pressing, bracket bending, small stamping dies, and punching plate up to 6 mm thick.
- Scale to 100+ tonnes by increasing ram bore to 250 mm or raising system pressure to 28 MPa. A 250 mm ram at 20 MPa produces 1,227 kN (125 tonnes). Frame steel thickness must increase proportionally — a 125-tonne frame requires 25-40 mm plate.
- Deep-draw stamping demands 500-5000 tonnes. These presses use multiple-cylinder arrangements and forged steel frames. Build only after establishing a machine shop capable of boring 300+ mm cylinders and machining 100+ mm tie rods.
- The minimum economic press for general workshop use produces 10-20 tonnes (80 mm ram at 20 MPa). Below this, a fly press or arbor press suffices.
- Hydraulic press frames are typically 3-5× heavier than the rated force in tonnes. A 35-tonne press frame weighs 200-400 kg. Account for foundation loads — a 100-tonne press transmits 100 tonnes through the floor.
- Seal material selection: Nitrile (Buna-N) for oil service to 100°C; polyurethane for higher pressure and longer life; Viton for temperatures above 100°C. Leather cup seals work up to ~7 MPa at low cost but require frequent replacement.
- Oil reservoir sizing: 3× the pump flow rate per minute is the minimum. A larger reservoir (5×) runs cooler and allows contaminants to settle. Install a magnetic drain plug and a return-line filter (25 μm) in the reservoir.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Ram drifts down under load | Cylinder seal leaking past piston; check valve not holding | Replace U-cup seals; lap check valve seat; verify gland nut torque |
| Spongy feel, inconsistent force | Air trapped in hydraulic system | Bleed system: cycle ram 10-20 times at full stroke with bleeder open; top off reservoir |
| Ram scores in cylinder | Dirt or metal particles in oil; damaged seal | Drain oil, flush cylinder with solvent; replace seal; filter oil to 25 μm before refilling |
| Pump won't build pressure | Relief valve set too low; pump worn; low oil level | Verify relief valve setting with gauge; check pump output flow; fill reservoir to mark |
| Frame spreading under load | Tie rod preload insufficient; weld crack | Re-torque tie rods to specification; inspect all welds with dye penetrant; add gusset reinforcement |
| Ram stalls under load (powered) | Pump flow insufficient for cylinder volume at required speed | Install larger pump or add accumulator; reduce expected approach speed; check for hose restriction |
| Oil overheating (>70°C) | Relief valve dumping excess flow; undersized reservoir | Install oil cooler; increase reservoir volume to 3× pump flow per minute; check that relief valve is not cracked open |
| Slow return stroke | Return line restricted; rod-side cavity too small | Check return hose for kinks; verify tank vent is not blocked; install larger return hose |
| Ram tilts under off-center load | Ram guide worn; uneven tie rod preload | Replace ram guide bushings; re-torque tie rods in alternating pattern; avoid off-center loads exceeding 50% of rated force |
| Oil discoloration (milky) | Water contamination from condensation or cooler leak | Drain and replace oil; repair cooler leak; install desiccant breather on reservoir; check for condensation in humid environments |

## Safety

- **Pinch points**: The ram-to-bed gap is the primary hazard. Never place hands in the working zone. Use tongs, pliers, or jigs to position workpieces. A 35-tonne press exerts 343 kN — any body part caught between ram and bed is crushed beyond surgical repair.
- **Hydraulic injection**: Hydraulic oil at 20+ MPa can penetrate skin through a pinhole leak. Injection injuries appear as a small puncture wound but spread oil through tissue planes, requiring immediate surgical debridement (wide excision of contaminated tissue). Never use hands to search for leaks — use cardboard or paper to detect spray patterns.
- **Frame failure**: An overloaded frame can fail catastrophically. Never exceed rated force. Verify pressure relief valve function monthly. A cracked weld on a loaded frame releases stored energy in a violent fracture.
- **Oil fire hazard**: Hydraulic oil (ISO VG 32) has an auto-ignition point of 300-400°C if atomized. A leaking fitting that sprays onto a hot surface ignites. Keep ignition sources away from hydraulic systems. Keep a Class B fire extinguisher within 10 m.
- **Stored energy**: A pressurized hydraulic system at 20 MPa stores energy in the compressed fluid and the frame elastic deformation. Before maintenance, relieve all system pressure by opening the relief valve and cycling the ram to bottom. Lock out the pump.

## Quality Control

1. **Dimensional check on pressed parts**: Measure formed parts with calipers at three positions. Flatness of pressed plates: check with straightedge and feeler gauges — maximum gap 0.1 mm per 100 mm of bend length.
2. **Springback verification**: After bending steel plate, the part springs back 2-5° from the bend angle. Over-bend by the springback amount. Verify by checking the finished angle with a protractor (±0.5° for structural work).
3. **Bearing seating test**: After pressing a bearing into a housing, verify the fit by checking that the bearing outer race is flush with the housing face within 0.02 mm. A bearing not fully seated will walk under load.
4. **Oil cleanliness**: Hydraulic oil must be filtered to 25 μm or better. Contaminated oil scores cylinder bores and destroys seals within weeks. Check oil clarity monthly — cloudy oil indicates water contamination (drain and replace).
5. **Cylinder bore inspection**: Annually, remove the ram and inspect the cylinder bore with a bore gauge. Score marks indicate contamination or seal failure. Honing removes minor scores; major scoring requires reboring and a new oversized ram.
6. **Tie rod tension check**: For H-frame presses, verify tie rod preload annually using a torque wrench or ultrasonic bolt gauge. Preload loss causes frame spreading and joint separation under load. Re-torque to specification if preload has dropped more than 10%.

## Variations and Alternatives

- **H-frame vs. C-frame**: H-frame presses have two side plates connected by tie rods, providing symmetric force distribution and minimal frame deflection. C-frame presses have a single side with a deep throat for accessing the work area from three sides. C-frames deflect more under load — limit to 50% of H-frame rated force for the same frame weight.
- **Hand pump vs. powered pump**: Hand pumps (lever or pedal operated) provide full force at low speed, suitable for intermittent operations like bearing pressing and small-part stamping. Powered pumps (electric motor + hydraulic pump) cycle faster and suit production work. A 5 L/min gear pump at 20 MPa produces 1.7 kW hydraulic power — adequate for a 35-tonne press cycling at 2-3 strokes per minute.
- **Arbor press (mechanical alternative)**: A rack-and-pinion arbor press produces 1-5 tonnes of force with no hydraulics. Suitable for light-duty work: pin insertion, small bearing pressing, staking. Build an arbor press for tasks under 5 tonnes; reserve the hydraulic press for heavier work.
- **Hydraulic jack press**: A bottle jack (common automotive tool) mounted in a steel frame makes a functional 10-20 tonne press. The jack provides pump, cylinder, and relief valve in one unit. Limitations: short stroke (100-150 mm), slow return, no return stroke force. Adequate for bootstrapping before building a dedicated cylinder.
- **Mechanical screw press**: A large threaded shaft driven by a flywheel produces high force with no hydraulics. Force is less controllable than hydraulic but the design avoids seals, oil, and hoses. Suitable for coining, stamping, and pressing operations where force control is not critical.
- Seal replacement interval: U-cup seals last 6-12 months in continuous service. Keep spare seal sets in stock. Replace seals proactively at scheduled intervals rather than waiting for leakage — a seal failure during a critical pressing operation causes downtime and potential part damage.
- Frame stress calculation: For a simple H-frame with four tie rods in tension, each rod sees F/4 of the working force. M20 Grade 8.8 bolts have a proof load of 145 kN each (4 × 145 = 580 kN total). Working at 350 kN gives a 1.66× safety factor. For higher-force presses (100+ tonnes), increase to M30 or M36 tie rods.
- C-frame deflection: A C-frame press deflects laterally under load because the force is applied off-center from the frame backbone. The deflection is approximately F × L³ / (3 × E × I), where L is the throat depth, E is the Young's modulus of the frame steel (200 GPa), and I is the moment of inertia of the frame cross-section. This deflection causes the ram and bed to become non-parallel under load, producing tapered workpieces.

## References

- Pascal's law: pressure in a confined fluid transmits equally in all directions. F₁/A₁ = F₂/A₂. The basis of all hydraulic force multiplication.
- [Iterative Machine Bootstrap](iterative-bootstrap.md) — the bootstrap sequence that produces machine tools
- [Machining](machining.md) — cutting operations for cylinder and ram components
- [Forming](forming.md) — metal forming operations that use presses
- [Joining](joining.md) — welding and bolted joint design for the frame
- [Compression Press](compression-press.md) — heated-platen variant for polymer processing
- [Iron & Steel](../metals/iron-steel.md) — material properties for frame and ram steel
- Hydraulic oil viscosity: ISO VG 32 (32 cSt at 40°C) for ambient temperature; ISO VG 46 for warmer climates. Viscosity affects seal life and pump efficiency.
- Seal materials: Nitrile (Buna-N) for oil service to 100°C; polyurethane for higher pressure and longer life; Viton for temperatures above 100°C.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
