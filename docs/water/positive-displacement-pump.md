# Positive Displacement Pump

> **Node ID**: water.positive-displacement-pump
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`polymers.elastomers`](../polymers/elastomers.md)
> **Enables**: [`water.procurement`](procurement.md), [`water.distribution`](distribution.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md)
> **Timeline**: Years 10-25
> **Outputs**: pressurized_fluid, metered_flow
> **Critical**: No — centrifugal pumps serve most water distribution needs; positive-displacement pumps are essential only for specific applications (chemical dosing, deep-well lifting, viscous fluids)

## Principle

A positive-displacement (PD) pump moves fluid by trapping a fixed volume in a chamber and mechanically forcing that volume into the discharge pipe. Unlike a centrifugal pump, flow is (nearly) independent of discharge pressure — the pump delivers the same volume per cycle regardless of system resistance. Flow rate is determined by displacement volume × cycling speed: Q = V × N, where V is the volume per cycle and N is the cycling frequency.

Three main families are covered here:

- **Piston (reciprocating) pump**: A piston moves linearly in a cylinder. Check valves on suction and discharge sides ensure one-way flow. Produces high pressure with moderate flow. The original industrial pump — used in mine dewatering since the 16th century.
- **Diaphragm pump**: A flexible diaphragm (rubber, PTFE, or metal) flexes back and forth to create the displacement chamber. The fluid is completely isolated from the drive mechanism. Essential for corrosive, abrasive, or purity-critical fluids. Common in chemical dosing and water treatment.
- **Gear pump**: Two meshing gears rotate in a tight-fitting housing. Fluid is carried in the spaces between gear teeth and the housing wall from inlet to outlet. Produces steady (non-pulsating) flow. Used for viscous fluids, lubricants, and hydraulic oil transfer.

Critical rule: a PD pump must never be operated against a closed discharge valve. With nowhere for fluid to go, pressure rises until something breaks — a pipe bursts, a coupling shears, or the pump casing cracks. Every PD pump installation must include a pressure relief valve on the discharge side, piped back to the suction side or to a tank.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (pump body) | 10-40 kg | Class 30 gray iron, for cylinder and valve housing | [Iron & Steel](../metals/iron-steel.md) | Bronze (corrosive fluids), stainless steel (food/pharma) |
| Steel or brass (piston/plunger) | 2-8 kg | 1045 steel (water), C36000 brass (chemical), 50-80 mm diameter | [Metals](../metals/index.md) | Ceramic plunger (abrasive fluids) |
| Diaphragm material | 1-2 | Buna-N, EPDM, Viton, or PTFE sheet, 2-5 mm thick | [Elastomers](../polymers/elastomers.md) | Stainless steel diaphragm (high-pressure, high-temperature) |
| Steel gears (gear pump) | 2 | 4140 or 8620 steel, hobbed and hardened to 55-60 HRC | [Iron & Steel](../metals/iron-steel.md) | Bronze gears (low-pressure, non-lubricating fluids) |
| Check valves (ball or flapper) | 2-4 | Brass or stainless steel body, Viton or PTFE seat | [Metals](../metals/index.md) | Swing check valves (larger sizes) |
| Packing or O-rings | 1 set | PTFE/graphite packing or Buna-N O-rings, sized to cylinder bore | [Polymers](../polymers/index.md) | Leather cup packing (low-pressure, historical) |
| Springs (check valves) | 2-4 | Music wire (steel) or stainless steel, sized for cracking pressure 0.1-0.5 bar | [Metals](../metals/index.md) | — |

## Construction Steps

### Piston Pump

1. **Cast and machine the cylinder**: Cast the pump body with integral suction and discharge ports. Bore the cylinder to a smooth, straight finish (0.8 μm Ra or better). Tolerance: bore diameter ±0.05 mm over the full stroke length. Machine flat gasket surfaces on the suction and discharge flanges.
2. **Machine the piston**: Turn the piston from steel or brass bar to 0.05-0.10 mm smaller than the cylinder bore. Cut ring grooves for piston rings (cast iron or PTFE) or install a cup seal (leather or rubber). The piston seal must prevent fluid from passing the piston while allowing smooth sliding.
3. **Make check valves**: For each port (suction and discharge), construct a ball-check valve. Machine a brass or stainless body with a conical seat (45° angle). Drop a precision ball (brass or stainless, 10-20 mm diameter) onto the seat. A light spring holds the ball on the seat. Cracking pressure (pressure needed to unseat the ball): 0.1-0.3 bar. Verify by blowing through the valve — it should pass air in one direction only.
4. **Assemble the power end**: Connect the piston rod to a crankshaft or eccentric via a connecting rod. The crankshaft converts rotary motion (from motor or hand crank) to reciprocating linear motion. Stroke length: 25-100 mm typical. Ensure the crank throw is centered to prevent side-loading the piston.
5. **Install and test**: Mount the pump body, insert the piston with rings/seals, install the check valves. Connect the suction line (rigid pipe or hose) below the fluid source level if possible (flooded suction eliminates priming). Connect the discharge line with a pressure relief valve set to 110% of maximum operating pressure. Cycle the pump by hand — both check valves should audibly click open and closed.

### Diaphragm Pump

6. **Machine the pump chambers**: Cast or machine two chamber blocks from cast iron, aluminum, or plastic (PVC for chemical service). Each chamber has an inlet port, an outlet port, and a flat face where the diaphragm mounts. Machine check valve seats into the inlet and outlet ports.
7. **Cut and mount the diaphragm**: Cut the diaphragm from elastomer sheet (Buna-N for water, Viton for fuels and solvents, PTFE for aggressive chemicals) to the chamber diameter plus 20 mm clamping margin. Bolt the diaphragm between the chamber block and the drive housing. The diaphragm must flex freely through the full stroke without binding.
8. **Connect the drive mechanism**: A connecting rod from an eccentric on the drive shaft pushes and pulls the center of the diaphragm. Dual-chamber pumps operate the two diaphragms 180° out of phase — one fills while the other discharges, producing a smoother combined flow. Stroke length: 5-25 mm typical (shorter than piston pumps because the diaphragm has limited travel).
9. **Install check valves and test**: Same ball-check valve design as the piston pump. Verify that each chamber draws fluid on the suction stroke and discharges on the pressure stroke. A common failure is reversed check valves — the pump runs but moves no fluid.

### Gear Pump

10. **Hob the gears**: Cut gear teeth into two cylindrical blanks using a hobbing machine (a specialized milling operation). Spur gears are simplest; helical gears run quieter. Gear mesh must be tight: backlash 0.05-0.10 mm. Hardened to 55-60 HRC for wear resistance.
11. **Machine the housing**: Bore the housing with two precision cylindrical chambers to accept the gear pair. Clearance between gear tips and housing bore: 0.025-0.050 mm — tight enough to prevent internal bypass (slip), loose enough for the oil film to lubricate. Machine inlet and outlet ports on opposite sides of the mesh point. Fluid enters where gears separate, is carried around the periphery, and exits where gears mesh.
12. **Assemble and test**: Install gears in the housing with bearings at both ends of each gear shaft. One shaft extends through a shaft seal (lip seal or mechanical seal) for coupling to the drive motor. Fill with the working fluid and rotate by hand — the pump should turn smoothly with no binding or clicking (indicates tooth-to-housing contact).

## Expected Performance

| Parameter | Piston Pump | Diaphragm Pump | Gear Pump |
|-----------|-------------|----------------|-----------|
| Flow range | 0.1-50 m³/hour | 0.01-20 m³/hour | 0.1-50 m³/hour |
| Maximum pressure | 10-200 bar | 3-15 bar (elastomer), 100+ bar (metal) | 5-25 bar |
| Viscosity range | 0.5-500 cP | 0.5-10,000 cP | 10-100,000 cP |
| Efficiency | 80-92% | 60-80% | 70-85% |
| Pulsation | High (single cylinder), reduced with multiple cylinders | Moderate (dual-chamber) | Very low (nearly continuous) |
| Self-priming | Yes (up to 5-7 m lift) | Yes (up to 3-5 m lift) | Limited (requires flooded suction) |
| Dry-run tolerance | Brief only (seal damage) | Yes (diaphragm separates fluid from drive) | No — gears seize without lubrication |
| Seal isolation | Fluid contacts piston seal | Fluid isolated from drive by diaphragm | Fluid contacts shaft seal only |

## Calibration and Verification

1. **Flow rate calibration**: Run the pump at the design speed into a calibrated container for a timed period. Measure actual flow rate against calculated flow (displacement × speed). For piston pumps: Q = π/4 × D² × L × N × η_v, where D is bore diameter, L is stroke length, N is cycling frequency, and η_v is volumetric efficiency (typically 0.85-0.95).
2. **Pressure relief valve test**: Close the discharge valve slowly while monitoring discharge pressure. The relief valve must open at its set pressure and prevent further pressure rise. Verify by reading the gauge — pressure should plateau at the relief setting.
3. **Leak check**: Run the pump at full operating pressure for 15 minutes. Inspect all joints, seals, and connections for leaks. Zero leaks on the suction side (air ingress degrades performance). Acceptable seepage on packed stuffing boxes: 10-60 drops/minute (lubricates the packing).

## Strengths

- Flow is independent of discharge pressure — the pump delivers its rated volume per cycle regardless of system resistance (up to the pressure relief setting)
- Self-priming capability allows suction lifts of 3-7 m — no need for flooded suction
- Handles viscous fluids far better than centrifugal pumps — gear pumps move oils, syrups, and slurries
- Diaphragm variants isolate the fluid completely from the drive mechanism — essential for corrosive, abrasive, or purity-critical applications
- Precise metering capability — each stroke delivers a known volume, enabling dosing and chemical injection

## Weaknesses

- Must not be operated against a closed discharge valve — pressure rises until something fails. A pressure relief valve is mandatory.
- Piston and diaphragm pumps produce pulsating flow — pulsation dampeners or multiple cylinders out of phase may be needed to protect downstream equipment
- Lower flow capacity than centrifugal pumps of equivalent size and power
- More wearing parts (check valves, seals, diaphragms) than centrifugal pumps — higher maintenance
- Gear pumps are limited to clean, lubricating fluids — abrasives or solids destroy the tight clearances rapidly

## Safety

- **Overpressure**: PD pumps generate pressure until something breaks. Install a pressure relief valve on every PD pump discharge, piped to a safe return or drain. Test the relief valve monthly.
- **Pulsation**: Pulsating flow causes vibration in piping. Secure all piping within 2 m of the pump discharge. Use flexible hose connections to isolate vibration.
- **Chemical exposure**: Diaphragm pumps are commonly used for chemical dosing (chlorine, acid, coagulants). A failed diaphragm releases the pumped chemical. Install a secondary containment dike under chemical pumps. Wear chemical-resistant PPE when servicing.
- **Pinch points**: The connecting rod and crankshaft of piston pumps move with significant force. Install guards over all exposed moving parts.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pump runs but delivers no flow | Check valve stuck or installed backward; air leak on suction side; diaphragm ruptured | Disassemble and inspect check valves. Apply soap solution to suction fittings. Inspect diaphragm for tears. |
| Flow rate lower than expected | Worn piston rings or gear clearances (internal slip); partially clogged suction strainer; worn check valves not seating fully | Measure actual flow against calculated. Inspect and replace worn seals/rings. Clean strainer. Replace check valve seats. |
| Excessive pulsation | Air in system; single-cylinder pump without dampener; worn check valves causing backflow | Bleed air from discharge line. Install a pulsation dampener (air-filled bladder) on the discharge. Replace check valves. |
| Pump overheating | Running against closed discharge or blocked line; worn bearings; excessive viscosity | Verify discharge path is open. Check bearing temperature (should be <80°C). Dilute viscous fluid or reduce speed. |
| Diaphragm failure | Chemical incompatibility; flex fatigue from excessive stroke; abrasion from solids | Select diaphragm material rated for the pumped fluid. Reduce stroke length. Install a strainer on the suction. |

## See Also

- [Centrifugal Pump](centrifugal-pump.md) — for high-flow, low-to-moderate pressure water pumping
- [Compressor](../gas-handling/compressor.md) — gas compression using piston and diaphragm mechanisms
- [Water Procurement](procurement.md) — hand pumps and lift pumps for wells
- [Water Distribution](distribution.md) — pump stations for pressurized water networks
- [Elastomers](../polymers/elastomers.md) — diaphragm and seal materials
- [Iron & Steel](../metals/iron-steel.md) — pump body and piston materials

[← Back to Water](index.md)
