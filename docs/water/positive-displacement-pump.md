# Positive Displacement Pump

> **Node ID**: water.positive-displacement-pump
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`polymers.rubber`](../polymers/rubber.md)
> **Enables**: [`water.procurement`](procurement.md), [`water.distribution`](distribution.md), [`chemistry.electrolysis`](../chemistry/electrolysis.md)
> **Timeline**: Years 10-25
> **Outputs**: pressurized_fluid, metered_flow
> **Critical**: No — centrifugal pumps serve most water distribution needs; positive-displacement pumps are essential only for specific applications (chemical dosing, deep-well lifting, viscous fluids)

## Overview

![Lantern Slide - Tangyes Ltd, "Special" Steam Operated Positive Displacement Pump Advertisement, circa 1910](../images/water/water_positive-displacement-pump.jpg)

> *Image: Unknown authorUnknown author, Public domain*

A positive-displacement (PD) pump moves fluid by trapping a fixed volume in a chamber and mechanically forcing that volume into the discharge pipe. Unlike a [centrifugal pump](centrifugal-pump.md), flow is (nearly) independent of discharge pressure — the pump delivers the same volume per cycle regardless of system resistance. PD pumps are essential for specific applications: chemical dosing, deep-well lifting, viscous fluids, high-pressure low-flow metering, and any situation where the pump must self-prime.

PD pumps complement centrifugal pumps in a water infrastructure system. Centrifugal pumps move large volumes at low-to-moderate pressure. PD pumps move smaller volumes at high pressure, handle viscous or abrasive fluids, and deliver precisely metered flow. A complete water system uses both types.

**Principle**: Flow rate is determined by displacement volume × cycling speed: Q = V × N, where V is the volume per cycle and N is the cycling frequency. Three main families are covered here:

- **Piston (reciprocating) pump**: A piston moves linearly in a cylinder. Check valves on suction and discharge sides ensure one-way flow. Produces high pressure with moderate flow. The original industrial pump — used in mine dewatering since the 16th century.
- **Diaphragm pump**: A flexible diaphragm ([rubber](../polymers/rubber.md), PTFE, or metal) flexes back and forth to create the displacement chamber. The fluid is completely isolated from the drive mechanism. Essential for corrosive, abrasive, or purity-critical fluids. Common in chemical dosing and water treatment.
- **Gear pump**: Two meshing gears rotate in a tight-fitting housing. Fluid is carried in the spaces between gear teeth and the housing wall from inlet to outlet. Produces steady (non-pulsating) flow. Used for viscous fluids, lubricants, and hydraulic oil transfer.

**Critical rule**: a PD pump must never be operated against a closed discharge valve. With nowhere for fluid to go, pressure rises until something breaks — a pipe bursts, a coupling shears, or the pump casing cracks. Every PD pump installation must include a pressure relief valve on the discharge side, piped back to the suction side or to a tank.

## Prerequisites

- [Iron and steel](../metals/iron-steel.md) for cylinder bodies, gears, and pistons
- [Machine tools](../machine-tools/machining.md) — lathe for cylinder boring, hobbing machine for gears
- [Rubber and polymers](../polymers/rubber.md) — diaphragm materials, O-rings, packing
- [Precision balls](../metals/index.md) for check valves (brass or stainless steel, 10-20 mm diameter)
- [Spring wire](../metals/index.md) for check valve springs

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (pump body) | 10-40 kg | Class 30 gray iron, for cylinder and valve housing | [Iron & Steel](../metals/iron-steel.md) | Bronze (corrosive fluids), stainless steel (food/pharma) |
| Steel or brass (piston/plunger) | 2-8 kg | 1045 steel (water), C36000 brass (chemical), 50-80 mm diameter | [Metals](../metals/index.md) | Ceramic plunger (abrasive fluids) |
| Diaphragm material | 1-2 | Buna-N, EPDM, Viton, or PTFE sheet, 2-5 mm thick | [Rubber](../polymers/rubber.md) | Stainless steel diaphragm (high-pressure, high-temperature) |
| Steel gears (gear pump) | 2 | 4140 or 8620 steel, hobbed and hardened to 55-60 HRC | [Iron & Steel](../metals/iron-steel.md) | Bronze gears (low-pressure, non-lubricating fluids) |
| Check valves (ball or flapper) | 2-4 | Brass or stainless steel body, Viton or PTFE seat | [Metals](../metals/index.md) | Swing check valves (larger sizes) |
| Packing or O-rings | 1 set | PTFE/graphite packing or Buna-N O-rings, sized to cylinder bore | [Polymers](../polymers/index.md) | Leather cup packing (low-pressure, historical) |
| Springs (check valves) | 2-4 | Music wire (steel) or stainless steel, sized for cracking pressure 0.1-0.5 bar | [Metals](../metals/index.md) | — |

## Process Description

### Piston Pump

**Principle**: A piston reciprocates in a cylinder. On the suction stroke, the piston withdraws, creating a partial vacuum that draws fluid through the inlet check valve. On the discharge stroke, the piston advances, pressurizing the fluid and forcing it through the outlet check valve. Each complete cycle displaces a volume equal to the cylinder bore area × stroke length. Flow rate Q = (π/4) × D² × L × N × η_v, where D is bore diameter, L is stroke length, N is cycling frequency, and η_v is volumetric efficiency (0.85-0.95).

**Prerequisites**: [Cast iron or bronze](../metals/iron-steel.md) for cylinder, [machining capability](../machine-tools/machining.md) for precision bore, [check valves](../metals/index.md), [piston seal materials](../polymers/index.md).

**Materials**: Cast iron cylinder body (10-30 kg), steel piston (2-5 kg), 2 check valve assemblies, piston rings or cup seal, connecting rod, crankshaft.

**Construction**:

1. **Cast and machine the cylinder**: Cast the pump body with integral suction and discharge ports. Bore the cylinder to a smooth, straight finish (0.8 μm Ra or better). Tolerance: bore diameter ±0.05 mm over the full stroke length. Machine flat gasket surfaces on the suction and discharge flanges.
2. **Machine the piston**: Turn the piston from steel or brass bar to 0.05-0.10 mm smaller than the cylinder bore. Cut ring grooves for piston rings (cast iron or PTFE) or install a cup seal (leather or rubber). The piston seal must prevent fluid from passing the piston while allowing smooth sliding.
3. **Make check valves**: For each port (suction and discharge), construct a ball-check valve. Machine a brass or stainless body with a conical seat (45° angle). Drop a precision ball (brass or stainless, 10-20 mm diameter) onto the seat. A light spring holds the ball on the seat. Cracking pressure (pressure needed to unseat the ball): 0.1-0.3 bar. Verify by blowing through the valve — it should pass air in one direction only.
4. **Assemble the power end**: Connect the piston rod to a crankshaft or eccentric via a connecting rod. The crankshaft converts rotary motion (from motor or hand crank) to reciprocating linear motion. Stroke length: 25-100 mm typical. Ensure the crank throw is centered to prevent side-loading the piston.
5. **Install and test**: Mount the pump body, insert the piston with rings/seals, install the check valves. Connect the suction line (rigid pipe or hose) below the fluid source level if possible (flooded suction eliminates priming). Connect the discharge line with a pressure relief valve set to 110% of maximum operating pressure. Cycle the pump by hand — both check valves should audibly click open and closed.

**Calibration**: Run the pump at design speed into a calibrated container for a timed period. Measure actual flow against calculated: Q = (π/4) × D² × L × N × η_v. Volumetric efficiency should be 0.85-0.95. If significantly lower, check for internal leakage past the piston seal or leaking check valves.

**Expected performance**: Flow: 0.1-50 m³/hour. Maximum pressure: 10-200 bar (triplex plunger pumps reach 200 bar). Efficiency: 80-92%. Self-priming to 5-7 m lift. Pulsation: high for single-cylinder, reduced with multiple cylinders (duplex = 2 cylinders, triplex = 3 cylinders phased 120° apart).

**Strengths**:
- Highest pressure capability of any pump type — triplex plunger pumps reach 200+ bar
- Self-priming from dry suction (5-7 m lift)
- Flow rate is predictable and independent of discharge pressure
- Handles abrasives with proper plunger and seal selection

**Weaknesses**:
- Pulsating flow — requires pulsation dampener or multiple cylinders to smooth output
- More wearing parts than centrifugal pumps (piston rings, check valves, packing)
- Cannot run against closed discharge — overpressure relief valve is mandatory
- Lower maximum flow than centrifugal pumps of equivalent power

### Diaphragm Pump

**Principle**: A flexible diaphragm (elastomer or PTFE) flexes back and forth to alternately expand and compress a chamber. Check valves on inlet and outlet ports ensure one-way flow. The fluid contacts only the inside of the chamber and the diaphragm — the drive mechanism (connecting rod, crankshaft) is isolated on the other side of the diaphragm. This complete separation makes diaphragm pumps the standard for corrosive, abrasive, and purity-critical applications.

**Prerequisites**: [Elastomer diaphragm material](../polymers/rubber.md), [cast iron or aluminum housing](../metals/iron-steel.md), [check valves](../metals/index.md), [machining capability](../machine-tools/machining.md).

**Materials**: Two chamber blocks (cast iron or aluminum, 5-20 kg each), two diaphragms (Buna-N, EPDM, Viton, or PTFE, 2-5 mm thick), 4 check valves, connecting rod, eccentric drive shaft.

**Construction**:

6. **Machine the pump chambers**: Cast or machine two chamber blocks from cast iron, aluminum, or plastic (PVC for chemical service). Each chamber has an inlet port, an outlet port, and a flat face where the diaphragm mounts. Machine check valve seats into the inlet and outlet ports.
7. **Cut and mount the diaphragm**: Cut the diaphragm from elastomer sheet (Buna-N for water, Viton for fuels and solvents, PTFE for aggressive chemicals) to the chamber diameter plus 20 mm clamping margin. Bolt the diaphragm between the chamber block and the drive housing. The diaphragm must flex freely through the full stroke without binding.
8. **Connect the drive mechanism**: A connecting rod from an eccentric on the drive shaft pushes and pulls the center of the diaphragm. Dual-chamber pumps operate the two diaphragms 180° out of phase — one fills while the other discharges, producing a smoother combined flow. Stroke length: 5-25 mm typical (shorter than piston pumps because the diaphragm has limited travel).
9. **Install check valves and test**: Same ball-check valve design as the piston pump. Verify that each chamber draws fluid on the suction stroke and discharges on the pressure stroke. A common failure is reversed check valves — the pump runs but moves no fluid.

**Calibration**: Time a measured discharge volume at the design stroke setting. Diaphragm pumps typically achieve volumetric efficiency of 0.75-0.90. Lower efficiency compared to piston pumps results from diaphragm flexibility absorbing some stroke volume.

**Expected performance**: Flow: 0.01-20 m³/hour. Maximum pressure: 3-15 bar (elastomer diaphragm), up to 100+ bar (metal diaphragm). Efficiency: 60-80%. Self-priming to 3-5 m lift. Can run dry without damage (unlike most pump types).

**Strengths**:
- Fluid completely isolated from drive mechanism — handles corrosive and abrasive fluids
- Can run dry without damage (no metal-on-metal sliding contact in the fluid path)
- Self-priming to 3-5 m lift
- Seal-free fluid path — no packing or mechanical seal to leak

**Weaknesses**:
- Diaphragm is a wearing part — fatigue failure after 2,000-10,000 hours depending on stroke and chemistry
- Limited pressure capability with elastomer diaphragms (3-15 bar)
- Lower volumetric efficiency than piston pumps
- Diaphragm failure releases pumped fluid into the drive housing — install leak detection for hazardous chemicals

### Gear Pump

**Principle**: Two meshing gears rotate in a close-fitting housing. Fluid fills the spaces between gear teeth and the housing wall on the inlet side (where gears separate). As the gears rotate, the trapped fluid is carried around the periphery to the outlet side (where gears mesh), where it is displaced by the meshing teeth. Flow is continuous and nearly pulse-free because the gear teeth engage smoothly. Internal clearance between gear tips and housing bore (0.025-0.050 mm) determines the amount of internal slip (backflow from high to low pressure side).

**Prerequisites**: [Hardened steel gears](../metals/iron-steel.md), [precision boring capability](../machine-tools/machining.md) for housing, [hobbing machine](../machine-tools/machining.md) for gear cutting.

**Materials**: Two gear blanks (4140 or 8620 steel, 1-5 kg each), housing (cast iron or steel, 5-20 kg), bearings (4 units), shaft seal.

**Construction**:

10. **Hob the gears**: Cut gear teeth into two cylindrical blanks using a hobbing machine (a specialized milling operation). Spur gears are simplest; helical gears run quieter. Gear mesh must be tight: backlash 0.05-0.10 mm. Hardened to 55-60 HRC for wear resistance.
11. **Machine the housing**: Bore the housing with two precision cylindrical chambers to accept the gear pair. Clearance between gear tips and housing bore: 0.025-0.050 mm — tight enough to prevent internal bypass (slip), loose enough for the oil film to lubricate. Machine inlet and outlet ports on opposite sides of the mesh point. Fluid enters where gears separate, is carried around the periphery, and exits where gears mesh.
12. **Assemble and test**: Install gears in the housing with bearings at both ends of each gear shaft. One shaft extends through a shaft seal (lip seal or mechanical seal) for coupling to the drive motor. Fill with the working fluid and rotate by hand — the pump should turn smoothly with no binding or clicking (indicates tooth-to-housing contact).

**Calibration**: Measure flow at rated speed with a calibrated container. Gear pump volumetric efficiency is 0.90-0.98 with clean fluid. Efficiency drops with low-viscosity fluids (water: 0.85-0.92) because thin fluids slip more through the tight clearances.

**Expected performance**: Flow: 0.1-50 m³/hour. Maximum pressure: 5-25 bar (external gear), up to 250 bar (internal gear with pressure-loaded wear plates). Efficiency: 70-85%. Not self-priming — requires flooded suction or pre-priming. Flow is nearly pulse-free.

**Strengths**:
- Nearly pulse-free flow — no pulsation dampener needed
- Handles viscous fluids (10-100,000 cP) that centrifugal pumps cannot move
- Compact and simple — few wearing parts (gears, bearings, shaft seal)
- Reversible — change rotation direction to reverse flow

**Weaknesses**:
- Cannot run dry — gears seize without lubrication from the pumped fluid
- Limited to clean fluids — solids and abrasives destroy the tight clearances in minutes
- Not self-priming — requires flooded suction
- Lower pressure capability than piston pumps

## Quantitative Parameters

| Parameter | Piston Pump | Diaphragm Pump | Gear Pump |
|-----------|-------------|----------------|-----------|
| Flow range | 0.1-50 m³/hour | 0.01-20 m³/hour | 0.1-50 m³/hour |
| Maximum pressure | 10-200 bar | 3-15 bar (elastomer), 100+ bar (metal) | 5-25 bar |
| Viscosity range | 0.5-500 cP | 0.5-10,000 cP | 10-100,000 cP |
| Efficiency | 80-92% | 60-80% | 70-85% |
| Pulsation | High (single), reduced (multi-cylinder) | Moderate (dual-chamber) | Very low (nearly continuous) |
| Self-priming | Yes (up to 5-7 m lift) | Yes (up to 3-5 m lift) | Limited (requires flooded suction) |
| Dry-run tolerance | Brief only (seal damage) | Yes (diaphragm separates fluid from drive) | No — gears seize without lubrication |
| Seal isolation | Fluid contacts piston seal | Fluid isolated from drive by diaphragm | Fluid contacts shaft seal only |
| Typical bearing life | 15,000-30,000 hours | 10,000-20,000 hours | 20,000-40,000 hours |
| Typical seal life | 1-3 years (packing), 2-5 years (mechanical) | 2,000-10,000 hours (diaphragm) | 1-3 years (shaft seal) |

### Pressure Rating by Pump Configuration

| Configuration | Max Pressure | Typical Application | Power Range |
|--------------|-------------|--------------------|-------------|
| Single-cylinder piston, brass body | 10-20 bar | Hand pump, well lifting | 0.1-0.5 kW (manual) |
| Duplex piston, cast iron | 20-50 bar | Boiler feed, hydrostatic test | 1-15 kW |
| Triplex plunger, hardened steel | 50-200 bar | Water jetting, RO feed, mine dewatering | 5-150 kW |
| Quintuplex plunger | 100-350 bar | High-pressure water jetting | 50-500 kW |
| Single diaphragm, elastomer | 3-7 bar | Chemical dosing, drum emptying | 0.1-2 kW |
| Dual diaphragm, elastomer | 3-15 bar | Slurry transfer, filter press feed | 0.5-10 kW |
| Metal diaphragm | 50-200 bar | Toxic/corrosive high-pressure dosing | 1-30 kW |
| External gear, cast iron housing | 5-15 bar | Lubricating oil, hydraulic fluid | 0.5-15 kW |
| External gear, steel with wear plates | 15-25 bar | Fuel oil, polymer transfer | 1-30 kW |
| Internal gear, pressure-loaded | 25-250 bar | Hydraulic power units | 5-100 kW |

## Scaling Notes

- **Chemical dosing** (0.01-5 L/hour): Small diaphragm metering pumps (0.01-5 L/hour stroke volume) for chlorine, coagulant, or pH adjustment chemical injection. Adjustable stroke length provides 10-100% flow turndown. Accuracy: ±1-3% of set flow. One pump per chemical, sized to the maximum dose rate.
- **Well lifting** (1-20 m³/hour): Piston pumps or progressive cavity pumps for lifting water from wells 10-100 m deep. Hand-operated piston pumps for small flows (see [Water Procurement](procurement.md)). Motor-driven piston pumps for village-scale supply.
- **Industrial transfer** (5-100 m³/hour): Gear pumps for lubricating oils and hydraulic fluids. Diaphragm pumps for corrosive chemicals and slurries. Piston pumps for high-pressure washing and hydrostatic testing.
- **High-pressure service** (50-200 bar): Multicylinder piston pumps (triplex or quintuplex) for water jetting, hydrostatic testing, and reverse osmosis. These are the highest-pressure pumps available for water service — a triplex plunger pump at 200 bar is a compact unit weighing 50-200 kg.
- **Viscous fluids**: Gear pumps are the standard for fluids above 100 cP viscosity — lubricating oil, syrup, molasses, paint, and resin. Centrifugal pumps cannot move these fluids effectively. Size the gear pump for the viscosity at operating temperature, not at ambient temperature.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Pump runs but delivers no flow | Check valve stuck or installed backward; air leak on suction side; diaphragm ruptured | Disassemble and inspect check valves. Apply soap solution to suction fittings. Inspect diaphragm for tears. |
| Flow rate lower than expected | Worn piston rings or gear clearances (internal slip); partially clogged suction strainer; worn check valves not seating fully | Measure actual flow against calculated. Inspect and replace worn seals/rings. Clean strainer. Replace check valve seats. |
| Excessive pulsation | Air in system; single-cylinder pump without dampener; worn check valves causing backflow | Bleed air from discharge line. Install a pulsation dampener (air-filled bladder) on the discharge. Replace check valves. |
| Pump overheating | Running against closed discharge or blocked line; worn bearings; excessive viscosity | Verify discharge path is open. Check bearing temperature (should be <80°C). Dilute viscous fluid or reduce speed. |
| Diaphragm failure | Chemical incompatibility; flex fatigue from excessive stroke; abrasion from solids | Select diaphragm material rated for the pumped fluid. Reduce stroke length. Install a strainer on the suction. |
| Gear pump noisy (whine or grind) | Cavitation from insufficient suction pressure; worn bearings; gear tooth damage | Increase suction pipe diameter. Check fluid level in supply tank. Inspect gears for pitting or scoring. |
| Pressure relief valve opening during normal operation | Discharge blockage; system pressure higher than expected; relief valve set too low | Check for closed valves or blockages downstream. Verify relief valve setting matches system requirements (typically 110% of max operating pressure). |

## Safety

- **Overpressure**: PD pumps generate pressure until something breaks. Install a pressure relief valve on every PD pump discharge, piped to a safe return or drain. Test the relief valve monthly. A failed relief valve on a PD pump is a catastrophic hazard — the pump will continue to build pressure until the casing, pipe, or coupling fails.
- **Pulsation**: Pulsating flow causes vibration in piping. Secure all piping within 2 m of the pump discharge with clamps or U-bolts. Use flexible hose connections to isolate vibration from rigid pipework. Install a pulsation dampener (gas-charged bladder or air chamber) on triplex and larger pumps.
- **Chemical exposure**: Diaphragm pumps are commonly used for chemical dosing (chlorine, acid, coagulants). A failed diaphragm releases the pumped chemical. Install a secondary containment dike under chemical pumps. Wear chemical-resistant PPE (nitrile gloves, face shield, chemical apron) when servicing chemical pump systems.
- **Pinch points**: The connecting rod and crankshaft of piston pumps move with significant force. Install guards over all exposed moving parts. Never reach into the crankcase while the pump is operating.
- **High-pressure discharge**: Triplex plunger pumps operating above 50 bar can inject fluid through skin (hydraulic injection injury). Never inspect a leak with bare hands — the fluid jet is often invisible. Depressurize the system before tightening fittings or replacing components.

## Quality Control

- **Flow rate verification**: Calibrate each pump against a calibrated container and stopwatch. For metering pumps, verify the delivered volume per stroke at three stroke settings (25%, 50%, 100%). Record the calibration curve. Recheck monthly for chemical dosing applications.
- **Pressure relief test**: Verify the relief valve opens at its set pressure and prevents further pressure rise. Close the discharge valve slowly while monitoring pressure. The relief valve should open within ±10% of its set point. A failed relief valve is a catastrophic hazard — it must work every time.
- **Check valve integrity**: Test each check valve by pressurizing the discharge side and verifying zero backflow through the valve. A leaking check valve reduces pump output and can cause reverse flow when the pump stops.
- **Diaphragm integrity**: For diaphragm pumps handling hazardous chemicals, install a leak detection probe in the space between the double diaphragms. Any fluid detected indicates a diaphragm breach — shut down and replace before the chemical reaches the drive mechanism.
- **Noise and vibration baseline**: Record the pump sound level and vibration during initial commissioning. A change in sound (clicking, knocking, grinding) or an increase in vibration amplitude indicates developing wear in check valves, bearings, or gears.

## Variations and Alternatives

### Progressive Cavity Pump

A single-helix rotor turning inside a double-helix stator creates a series of sealed cavities that progress from inlet to outlet as the rotor turns. The stator is an elastomer ([rubber](../polymers/rubber.md)) mold; the rotor is hardened steel. Produces smooth, non-pulsating flow with self-priming capability and excellent solids handling.

**Prerequisites**: [Steel rotor machining](../machine-tools/machining.md), [rubber stator molding](../polymers/rubber.md).

**Expected performance**: Flow: 0.1-100 m³/hour. Pressure: 5-25 bar (higher with multiple stages). The standard pump for wastewater sludge handling.

**Strengths**:
- Handles highly abrasive and viscous fluids that destroy gear and centrifugal pumps
- Non-pulsating flow — no pulsation dampener needed
- Self-priming to 5-8 m suction lift
- Reversible — can pump in either direction

**Weaknesses**:
- The rubber stator is a wearing part — replacement every 1-3 years depending on abrasiveness
- Cannot run dry — the pumped fluid lubricates the rotor-stator interface. Running dry destroys the stator in minutes.
- Higher cost than centrifugal for equivalent water-only flow

### Peristaltic Pump

A flexible tube is progressively squeezed by rollers mounted on a rotating arm, pushing fluid through the tube. The fluid contacts only the tube interior — complete isolation from the pump mechanism. No check valves, no seals, no diaphragms.

**Prerequisites**: Flexible tubing (PVC, silicone, Viton, or PTFE-lined), roller mechanism.

**Expected performance**: Flow: 0.001-5 m³/hour. Pressure: 1-5 bar (limited by tube burst strength). Efficiency: 20-50%.

**Strengths**:
- Fluid contacts only the tubing — the purest fluid isolation of any pump type
- No seals, no valves, no diaphragms — extremely simple maintenance (replace the tube)
- Self-priming and can run dry without damage

**Weaknesses**:
- Tubing is a wearing part — replacement every 100-2000 hours depending on chemistry and compression
- Pulsating flow (one pulse per roller passage)
- Limited pressure capability (tube burst strength)
- Low efficiency (20-50%) — energy is wasted compressing the tube

### Metering (Dosing) Pump

A precision diaphragm or piston pump designed for accurate, repeatable delivery of a fixed volume per stroke. Stroke length and/or frequency are adjustable. Used for chemical dosing in water treatment: chlorine (0.5-5 mg/L), coagulant (5-50 mg/L), pH adjustment (acid or base).

**Prerequisites**: [Diaphragm materials](../polymers/rubber.md), precision machining for stroke adjustment mechanism, chemical-resistant wetted parts.

**Expected performance**: Flow per stroke: 0.01-5 mL (micro-dosing) to 1-10 L (industrial). Accuracy: ±1% of rated capacity.

**Strengths**:
- Precise, repeatable delivery — the defining feature for chemical dosing
- Adjustable stroke provides 10-100% turndown without loss of accuracy
- Diaphragm versions isolate the chemical from the drive mechanism

**Weaknesses**:
- Limited flow capacity — not suitable for bulk water transfer
- Requires calibration for each chemical (viscosity affects delivery)
- Check valves are the primary wearing part — must be serviced or replaced annually

## References

- [Centrifugal Pump](centrifugal-pump.md) — for high-flow, low-to-moderate pressure water pumping
- [Compressor](../gas-handling/compressor.md) — gas compression using piston and diaphragm mechanisms
- [Water Procurement](procurement.md) — hand pumps and lift pumps for wells
- [Water Distribution](distribution.md) — pump stations for pressurized water networks
- [Water Valves](water-valves.md) — check valves and pressure relief valves for pump installations
- [Rubber](../polymers/rubber.md) — diaphragm and seal materials
- [Iron & Steel](../metals/iron-steel.md) — pump body and piston materials

---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
