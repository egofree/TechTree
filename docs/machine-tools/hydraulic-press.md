# Hydraulic Press

> **Node ID**: machine-tools.hydraulic-press
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`machine-tools.joining`](joining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 15-25
> **Outputs**: formed_parts, stamped_parts, compressed_assemblies
> **Critical**: No — mechanical screw presses and fly presses can substitute for many operations, but the hydraulic press is the only practical route for high-force, slow-speed forming

## Principle

A hydraulic press uses Pascal's law — pressure applied to a confined fluid transmits equally in all directions — to multiply a small input force into a large output force. A small-diameter pump cylinder pressurizes hydraulic oil, which acts on a large-diameter ram cylinder. The force multiplication equals the ratio of ram area to pump area: F_out = F_in × (A_ram / A_pump). A typical shop press with a 150 mm diameter ram and a 20 mm diameter pump cylinder multiplies force 56×. At 20 MPa system pressure, the 150 mm ram produces 350 kN (35 tonnes) of force. The press produces controllable force at low speed, making it ideal for forming, pressing bearings, stamping, and laminating.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame) | 100-200 kg | A36 or equivalent, 12-25 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, no welding needed) |
| Steel bar (ram) | 20-50 kg | 1045 or 4140, 80-150 mm diameter, hardened to 45-50 HRC | [Iron & Steel](../metals/iron-steel.md) | Ground and polished mild steel (shorter life) |
| Seamless tubing (cylinder) | 5-15 kg | Honed ID, 80-150 mm bore, 10 mm wall | [Forming](forming.md) | Bored solid bar (more machining) |
| Hydraulic seals | 1 set | U-cup or O-ring, matched to bore diameter | [Elastomers](../polymers/elastomers.md) | Leather cup packing (lower pressure limit, ~7 MPa) |
| Hydraulic oil | 10-30 L | ISO VG 32 or 46, filtered to 25 μm | [Lubricants](../chemistry/lubricants.md) | Filtered vegetable oil (degrades faster) |
| Pressure gauge | 1 | 0-30 MPa, Bourdon tube type | [Measurement](../measurement/index.md) | None — pressure indication is safety-critical |
| Bolts and nuts | 2-5 kg | Grade 8.8 or higher, M12-M20 | [Fasteners](../metals/iron-steel.md) | Riveted joints (non-adjustable) |
| Welding consumables | 5-10 kg | E7018 electrodes or equivalent | [Joining](joining.md) | Bolted flanges (heavier) |

## Prerequisites

- [Steel plate](../metals/iron-steel.md) — for frame, bed, and ram (minimum 10 mm thick for structural members)
- [Seamless steel tubing](forming.md) — for hydraulic cylinder bore (or bored solid bar)
- [Hydraulic seals](../polymers/elastomers.md) — O-rings, U-cup seals (nitrile or polyurethane)
- [Hydraulic oil](../chemistry/lubricants.md) — ISO VG 32 or 46 (or filtered vegetable oil as substitute)
- [Pressure gauge](../measurement/index.md) — 0-30 MPa range
- [Hand pump or powered pump](../energy/hydraulics.md) — rated to 20+ MPa
- [Machining capability](machining.md) — for boring cylinder, machining ram, and facing mating surfaces

## Construction Steps

### Frame

1. **Cut frame plates**: Cut two side plates (500 × 800 mm, 15 mm thick) and a bed plate (400 × 500 mm, 25 mm thick) from steel plate using a torch or saw. A C-frame design uses a single side with a deep throat; an H-frame uses two side plates with tie rods.
2. **Machine mating surfaces**: Mill the top and bottom faces of the side plates flat and parallel to 0.05 mm. The ram guide bore (if integrated into the frame) must be bored perpendicular to the bed within 0.02 mm per 100 mm.
3. **Weld or bolt frame**: For an H-frame press, weld the side plates to the bed plate with full-penetration fillet welds (E7018, 3.2 mm electrode). Alternatively, use bolted flanges with Grade 8.8 bolts for disassembly. Reinforce corners with gusset plates (10 mm, triangular, 100 mm legs).
4. **Install tie rods** (H-frame): Thread four tie rods (M20, 500-600 mm long) through the side plates. Tighten nuts alternately and evenly to 300 N·m. The tie rods preload the frame to resist the working force without joint separation.

### Cylinder and Ram

5. **Prepare cylinder bore**: If using seamless tubing, hone the bore to a 0.8 μm Ra finish or better. If boring from solid bar, bore to diameter, then hone. The bore must be round within 0.02 mm and straight within 0.05 mm over the full stroke length.
6. **Machine ram**: Turn the ram from 1045 or 4140 steel bar. Diameter is 0.05-0.10 mm smaller than the cylinder bore (clearance fit for the seal). Surface finish: 0.4 μm Ra or better (polished). Harden to 45-50 HRC for wear resistance.
7. **Install seals**: Fit U-cup seals into the cylinder head (gland nut). Seal orientation: cup faces the pressure side. Install O-ring in the gland nut for static seal between cylinder head and cylinder body. Coat all seals with hydraulic oil before assembly.
8. **Assemble cylinder**: Insert ram into cylinder bore through the gland nut. Thread gland nut into cylinder body (or bolt on). The ram should slide smoothly under hand pressure with no binding.

### Hydraulic System

9. **Mount cylinder**: Bolt the cylinder to the top of the frame (H-frame) or the upper cross-member (C-frame). Align the ram axis perpendicular to the bed within 0.1 mm per 100 mm using a machinist's square.
10. **Connect pump**: Connect the hand pump (or power unit) to the cylinder via hydraulic hose rated to at least 1.5× the maximum working pressure. Install a pressure gauge in the line between pump and cylinder.
11. **Fill and bleed**: Fill the reservoir with filtered hydraulic oil. Cycle the pump 10-20 times with the ram unloaded to purge air from the system. Air in the system causes spongy feel and erratic force.

### Safety Features

12. **Install pressure relief valve**: Set to 110% of the rated maximum pressure. This prevents overloading the frame or bursting the cylinder. Verify by pumping to relief pressure and confirming the gauge reading.
13. **Add stroke limiter**: Install adjustable mechanical stops to prevent the ram from over-traveling. This protects the bed and workpiece from damage.

## Calibration and Verification

1. **Force calibration**: Place a calibrated load cell (or a known-weight test) between the ram and bed. Pump to the relief valve set pressure. Record the gauge reading and the measured force. Calculate the effective ram area: F = P × A. Verify the force matches the design calculation within ±5%.
2. **Parallelism check**: Place a precision straightedge across the bed. Lower the ram until it contacts the straightedge at two points. Measure gap between ram face and straightedge at four corners. Maximum deviation: 0.05 mm per 100 mm of ram face width. Adjust frame or shim as needed.
3. **Pressure test**: Pump to 1.25× the rated working pressure with no load. Hold for 10 minutes. Inspect all connections, seals, and welds for leaks. Zero leaks acceptable.
4. **Stroke test**: Cycle the ram through full stroke 20 times unloaded, then 10 times at 50% rated force. Verify smooth operation with no jerking, binding, or pressure drift.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Maximum force (20 MPa, 150 mm ram) | 350 kN (35 tonnes) |
| Maximum force (20 MPa, 100 mm ram) | 155 kN (16 tonnes) |
| Stroke length | 150-300 mm (design-dependent) |
| Ram speed (hand pump) | 5-20 mm/sec |
| Ram speed (powered pump, 5 L/min) | 0.5-2 mm/sec at full force |
| Frame deflection at rated load | <0.5 mm (H-frame), <1.0 mm (C-frame) |
| Bed flatness | ±0.05 mm |
| Hydraulic system pressure | 10-20 MPa (typical) |
| Duty cycle | Intermittent — 10 min on, 5 min off (thermal limit on pump) |
| Seal life | 6-12 months continuous use; inspect monthly |

## Strengths

- Enormous force in a compact frame — 35 tonnes from a 150 mm ram at 20 MPa
- Force is controllable and repeatable via pressure gauge — unlike a hammer or fly press
- Slow, steady motion avoids shock loading — suitable for delicate operations (bearing pressing, laminating)
- Simple hydraulic circuit — hand pump, cylinder, relief valve. No complex electronics required

## Weaknesses

- Slow operating speed — hydraulic presses are for high-force, low-speed work, not high-throughput stamping
- Hydraulic oil leaks are inevitable over time — seals wear, hoses age. Oil on the floor is a slip hazard
- Frame must be massively overbuilt — a 35-tonne press frame experiences 35 tonnes of force trying to spread it apart
- Not suitable for impact forming — the slow ram speed means workpieces strain-rate harden rather than flow

## Safety

- **Pinch points**: The ram-to-bed gap is the primary hazard. Never place hands in the working zone. Use tongs, pliers, or jigs to position workpieces.
- **Hydraulic injection**: Hydraulic oil at 20+ MPa can penetrate skin through a pinhole leak. Injection injuries require immediate surgical debridement. Never use hands to search for leaks; use cardboard or paper.
- **Frame failure**: An overloaded frame can fail catastrophically. Never exceed rated force. Verify pressure relief valve function monthly.
- **Oil fire hazard**: Hydraulic oil ignites at 300-400°C if atomized. Keep ignition sources away from hydraulic systems.

## See Also

- [Iterative Machine Bootstrap](iterative-bootstrap.md) — the bootstrap sequence that produces machine tools
- [Machining](machining.md) — cutting operations for cylinder and ram components
- [Forming](forming.md) — metal forming operations that use presses
- [Joining](joining.md) — welding and bolted joint design for the frame

[← Back to Machine Tools](index.md)
