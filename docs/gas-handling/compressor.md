# Gas Compressor

> **Node ID**: gas-handling.compressor
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`gas-handling.cylinder-filling`](cylinder-filling.md), [`chemistry.air-separation`](../chemistry/air-separation.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md)
> **Timeline**: Years 15-30
> **Outputs**: compressed_gas
> **Critical**: Yes — gas compression is the enabling step for gas storage, transport, air separation, and virtually all gas-phase industrial chemistry

## Prerequisites

- [Iron & Steel](../metals/iron-steel.md) — cast iron for cylinder blocks, forged steel for crankshafts and connecting rods
- [Machining](../machine-tools/machining.md) — precision boring of cylinders, grinding of journals, milling of rotor profiles
- [Electricity](../energy/electricity.md) — motor drive power (5-500 kW depending on compressor size)
- [Lubricants](../chemistry/lubricants.md) — compressor oil for sealing, cooling, and lubrication

## Principle

A gas compressor raises gas pressure by mechanically reducing its volume. Unlike liquids (essentially incompressible), gases follow the ideal gas law PV = nRT (or more accurately, PV = ZnRT where Z is the compressibility factor). Compression work heats the gas — adiabatic compression of air from 1 to 10 bar raises temperature from 20°C to approximately 250°C. Multi-stage compressors with intercoolers between stages approach isothermal (constant-temperature) compression, which requires the least work. The theoretical minimum work for isothermal compression from P₁ to P₂ is W = nRT × ln(P₂/P₁).

Three main compressor families:

- **Reciprocating (piston) compressor**: A piston compresses gas in a cylinder, with suction and discharge valves controlling flow direction. Pressure ratio per stage: 3-5. For discharge pressures above 5 bar, multi-stage compression with intercoolers is mandatory to keep discharge temperature below 150-180°C (oil ignition limit) and to reduce total work.
- **Rotary screw compressor**: Two helical rotors mesh to trap and compress gas continuously. No suction/discharge valves. Oil-flooded versions inject oil for sealing, cooling, and lubrication. Pressure ratio 3-15 in a single stage. Oil-free (dry) versions use PTFE-coated rotors but consume 15-25% more power.
- **Diaphragm compressor**: A metal diaphragm flexed by hydraulic oil isolates the gas from the drive mechanism. Zero contamination — the only compressor type suitable for ultra-pure and toxic gases. Pressure ratio 3-10 per stage. Lower flow rates but capable of very high discharge pressures (up to 1000+ bar in multi-stage configurations).

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Cast iron (cylinder block) | 50-200 kg | Class 30 or 40 gray iron, for cylinder bores and valve decks | [Iron & Steel](../metals/iron-steel.md) | Nodular iron (higher strength) |
| Forged steel (pistons, connecting rods) | 20-80 kg | 1045 or 4140, heat-treated to 28-32 HRC | [Iron & Steel](../metals/iron-steel.md) | Cast iron pistons (smaller compressors) |
| Steel or nodular iron (screw rotors) | 10-40 kg | Precision-machined helical rotors, 3-5 μm tolerance on rotor profile | [Iron & Steel](../metals/iron-steel.md) | — |
| Stainless steel (diaphragm) | 1-2 | 301 or 316 full-hard, 0.5-1.5 mm thick | [Metals](../metals/index.md) | Inconel (high-temperature service) |
| Valve plates (suction/discharge) | 1 set | Spring steel or stainless, 1-2 mm thick, with sealing gaskets | [Iron & Steel](../metals/iron-steel.md) | Ring valves (higher speed) |
| Piston rings | 1 set | Cast iron or PTFE-filled, sized to cylinder bore | [Machine Tools](../machine-tools/index.md) | — |
| Bearings | 4-8 | Roller and ball bearings rated for combined radial and axial loads at operating speed | [Bearings](../machine-tools/bearings-abrasives.md) | — |
| Compressor oil | 5-30 L | ISO VG 100-150, mineral or synthetic, rated for discharge temperature | [Lubricants](../chemistry/lubricants.md) | Synthetic ester oil (longer life, higher temperature) |
| Intercooler tubes | 5-20 kg | Copper or steel finned tubing, surface area sized for heat rejection | [Metals](../metals/index.md) | Shell-and-tube heat exchanger |
| Gaskets and O-rings | 1 set | Viton or PTFE for gas sealing at elevated temperature | [Polymers](../polymers/index.md) | Copper gaskets (high-pressure joints) |

## Construction Steps

### Reciprocating Piston Compressor (2-Stage)

1. **Cast the cylinder block**: Use a sand mold to cast the two-stage cylinder block with integral cooling jackets (water passages around the cylinder bores). First-stage bore: 100-150 mm diameter. Second-stage bore: 50-80 mm (smaller because gas volume is reduced after first-stage compression and intercooling). Bore both cylinders to 0.05 mm tolerance with 0.8 μm Ra finish.
2. **Machine valve decks**: On the top of each cylinder, machine flat surfaces for the suction and discharge valve plates. Each valve plate seats on a gasket and is held by a valve cage (spring-loaded). The suction valve opens when cylinder pressure drops below inlet pressure; the discharge valve opens when cylinder pressure exceeds discharge line pressure. Machine valve pockets with 0.02 mm flatness on the sealing surface.
3. **Make the crankshaft**: Forge or machine a crankshaft from 4140 steel with two crank throws (one for each stage) offset by 180° for balanced operation. Hardened to 28-32 HRC. Journal surfaces ground to 0.4 μm Ra. Install main bearings in the crankcase.
4. **Machine pistons and connecting rods**: Turn pistons from cast iron bar to 0.10-0.15 mm smaller than cylinder bore. Cut piston ring grooves (2-3 rings per piston: 2 compression rings, 1 oil control ring). Forge connecting rods from 1045 steel with big-end bearing bore and small-end wrist pin bore. Wrist pin: case-hardened steel, 20-30 mm diameter.
5. **Build the intercooler**: Construct a finned-tube heat exchanger between the first and second stages. First-stage discharge gas passes through the tubes while cooling water (or ambient air) flows over the fins. Target: reduce gas temperature from ~150°C discharge to within 10-15°C of cooling water inlet temperature. Intercooler effectiveness directly determines second-stage efficiency and total power consumption.
6. **Assemble the running gear**: Install crankshaft in crankcase with main bearings. Attach connecting rods to crank throws. Install pistons in cylinder bores with rings compressed by a ring compressor tool. Verify piston-to-valve clearance at top dead center: minimum 1.5 mm. Insufficient clearance causes piston-to-valve contact at high temperature (thermal expansion of the piston rod).
7. **Install valve plates and cylinder head**: Mount suction and discharge valve plates on the valve decks with gaskets. Bolt the cylinder head over the valve assembly. The cylinder head contains the gas passages connecting suction/discharge ports to the valves.
8. **Install shaft seal**: Mount a lip seal or mechanical seal on the crankshaft where it exits the crankcase. This prevents oil from leaking out and gas from leaking in (or vice versa). For oil-free compressors, a multi-lip labyrinth seal is used instead.
9. **Couple to motor**: Align the compressor flywheel to the motor sheave (if belt-driven) or couple directly. Belt drive allows speed reduction (compressors typically run at 300-1200 RPM, while motors run at 1450-2900 RPM). V-belts rated for the transmitted power (typically 5-50 kW for industrial units).

### Oil-Flooded Rotary Screw Compressor

10. **Machine the rotor pair**: Cut male (4 lobes) and female (6 flutes) rotor profiles on a CNC milling machine using a form cutter. Profile tolerance: 3-5 μm. The rotors mesh with a controlled clearance of 0.025-0.050 mm. Coat rotors with PTFE for oil-free service, or leave bare for oil-flooded service (oil film provides the seal).
11. **Bore the rotor housing**: Precision-bore two intersecting cylindrical chambers in the cast iron housing to accept the rotor pair. The housing includes inlet and outlet ports positioned to trap gas as rotor lobes separate (inlet) and compress as lobes mesh (outlet).
12. **Assemble with timing gears**: Install the rotor pair with timing gears that maintain the correct phase relationship (rotors do not touch each other — the timing gears transmit torque). Install bearings at both ends of each rotor shaft.
13. **Install oil system**: For oil-flooded units, connect an oil injection port near the discharge end. An oil separator (centrifugal or coalescing filter) on the discharge line removes oil from the compressed gas. Oil is cooled by an oil cooler and returned to the injection port via a pump or pressure differential.

### Diaphragm Compressor

14. **Machine the compression head**: Bore a shallow cavity (5-15 mm deep, 100-300 mm diameter) in a forged steel block. The cavity profile is contoured to allow the diaphragm to fully deflect against the head surface. Machine the cavity surface to 0.4 μm Ra finish — any surface defect creates a stress concentration that initiates diaphragm fatigue cracks. Drill suction and discharge ports with valve seats.
15. **Prepare the diaphragm**: Cut a disc of full-hard 301 or 316 stainless steel, 0.5-1.5 mm thick, to cover the cavity with 10-20 mm clamping margin. Inspect edges for burrs or nicks — these are crack initiation sites. The diaphragm must be absolutely flat; any waviness creates uneven stress during flexing.
16. **Assemble the hydraulic system**: The diaphragm is driven by hydraulic oil pressure from a plunger pump. The plunger pump is driven by the same crankshaft as the compression head. Oil pressure cycles the diaphragm between the cavity floor (suction stroke) and the head surface (discharge stroke). A hydraulic relief valve limits maximum oil pressure to prevent diaphragm overstress.
17. **Clamp the diaphragm**: Sandwich the diaphragm between the compression head and the oil-side backing plate using high-strength bolts in a bolt circle. Bolt torque must be precisely controlled (typically 50-100 N·m depending on bolt size) to seal the diaphragm perimeter without crushing it. Uneven bolt torque causes edge leaks and premature diaphragm failure.
18. **Install contour plate (oil side)**: The oil-side plate has a contoured surface matching the compression head cavity. This ensures the diaphragm is supported on both sides throughout its deflection range, preventing excessive bending stress at the center. The contour profile is critical — incorrect contour causes rapid diaphragm failure (100-1000 hours instead of 2000-5000 hours).
19. **Set the hydraulic overload relief**: Adjust the hydraulic relief valve to limit maximum oil pressure to 110-120% of design discharge pressure. This protects the diaphragm from overpressure. Test by deadheading the discharge (blocked outlet) and verifying the relief valve opens before the diaphragm ruptures. The relief valve must be rated for the full hydraulic system pressure.
20. **Install the discharge check valve**: A spring-loaded check valve on the discharge port prevents backflow of high-pressure gas into the compression head during the suction stroke. The check valve must open at <0.1 bar differential to minimize throttling losses. Seat material: PTFE or stainless depending on gas compatibility.

## Valve Types and Selection

Compressor valves control gas flow into and out of the cylinder. Valve design affects efficiency, reliability, and maximum operating speed.

**Plate valves**: Flat spring-steel plates (1-2 mm thick) lift off their seats by suction or discharge pressure differential. Maximum lift: 2-4 mm. Used on most industrial reciprocating compressors. Life expectancy: 10,000-20,000 hours. Failure modes: fatigue cracking at the plate center, erosion from liquid or particle ingestion, spring breakage.

**Ring valves**: Concentric rings (2-5 rings per valve) replace the single plate. Each ring lifts independently, providing more flow area and lower pressure drop than plate valves. Used on high-speed compressors (600-1200 RPM). More expensive to manufacture but longer life at high speed.

**Poppet valves**: Individual mushroom-shaped poppets (6-30 per valve) with coil springs. Low pressure drop, quiet operation, good for gas compressors with varying molecular weights. Used on natural gas and process gas compressors.

**Valve selection criteria**: Plate valves for general-purpose air compressors below 600 RPM. Ring valves for high-speed air compressors (600-1200 RPM). Poppet valves for process gas compressors with variable gas composition. All valves must be compatible with the gas being compressed — corrosive gases (HCl, Cl₂, H₂S) require stainless steel valve components.

## Maintenance Schedule

Preventive maintenance is essential for compressor reliability. A typical schedule for a reciprocating compressor in continuous service:

| Interval | Task | Component |
|---|---|---|
| Daily | Check oil level, discharge temperature, discharge pressure, unusual noise or vibration | Crankcase, instruments |
| Weekly | Drain moisture from receiver tank, check belt tension (if belt-driven) | Receiver, belts |
| Monthly | Inspect air filter (clean or replace if ΔP > 250 Pa), check all bolt torques | Air intake, foundation |
| Quarterly | Test pressure relief valves (must open at set pressure), sample compressor oil for analysis (viscosity, acidity, particulate count) | Relief valves, oil |
| Semi-annually | Clean intercooler and aftercooler tubes, inspect and clean suction/discharge valves | Heat exchangers, valves |
| Annually | Replace suction/discharge valve plates and springs (preventive), change compressor oil and oil filter, check bearing clearances with dial indicator | Valves, oil, bearings |
| Every 3-5 years | Full overhaul: replace piston rings, bearings, shaft seal, gaskets; re-machine valve decks if worn; check cylinder bore for taper and ovality | Complete rotating assembly |

Oil analysis is the most cost-effective condition monitoring technique. Track viscosity (should be within ±10% of rated grade), total acid number (TAN >2.0 indicates oxidation — change oil immediately), and particulate count (>50 ppm iron indicates abnormal wear). Trend these values over time to predict failures weeks before they occur.

## Calibration and Verification

1. **Leak test**: Pressurize the compressor discharge to 50% of rated pressure with the compressor off (using an external air source). Soap-test all joints, valve covers, and shaft seals. Zero leaks on gas joints. Acceptable oil seepage at shaft seal: 10-30 drops/hour.
2. **Capacity test**: Run the compressor at rated speed into a known-volume receiver tank. Measure the time to pressurize from atmospheric to a target pressure. Calculate free air delivery (FAD): the volume of atmospheric air the compressor would need to draw in to produce the observed pressure rise. Compare to rated FAD.
3. **Discharge temperature check**: Run at full load for 30 minutes. Measure discharge temperature at each stage. First-stage discharge: should be below 180°C. After intercooler: within 15°C of cooling water. Second-stage discharge: below 180°C. Higher temperatures indicate inadequate intercooling, worn valves, or excessive pressure ratio.
4. **Vibration check**: Measure vibration at the crankcase, cylinder head, and discharge flange. Acceptable: below 4.5 mm/s RMS velocity. Higher vibration indicates misalignment, imbalance, or bearing wear.

## Aftercooler and Moisture Separation

Compressed gas leaving the final stage is hot (80-180°C) and saturated with moisture. Before storage or use, the gas must be cooled and dried.

**Aftercooler**: A heat exchanger (air-cooled finned tube or water-cooled shell-and-tube) mounted on the compressor discharge. Cools the gas from 80-180°C to within 10-20°C of ambient. As the gas cools, its moisture-holding capacity drops sharply — water condenses out.

**Moisture separator**: A centrifugal or cyclone separator installed downstream of the aftercooler. The cooled gas enters a cylindrical vessel tangentially, creating a vortex. Liquid water droplets (and oil mist from lubricated compressors) are flung to the vessel wall by centrifugal force, drain to the bottom, and are discharged through an automatic drain valve. Separation efficiency: 95-99% for droplets >10 μm.

**Refrigerated dryer** (for instrument-quality air): Further cools the gas to 2-5°C using a small vapor-compression refrigeration unit, condensing remaining moisture. A dew point of 2°C at line pressure corresponds to approximately -22°C at atmospheric pressure — dry enough for most pneumatic tools and instrument air. For semiconductor-grade gas, additional desiccant drying (molecular sieve to -70°C dew point) is required.

**Desiccant dryer types**:
- **Regenerative (twin-tower)**: Two beds of activated alumina or molecular sieve alternate — one drying the gas stream while the other is regenerated by a purge of dry gas or heated air. Achieves dew points of -40 to -70°C. Standard for industrial instrument air.
- **Disposable cartridge**: Small, simple, used for low-flow applications. Desiccant is discarded and replaced when saturated. Common for laboratory gas lines.

## Multi-Stage Sizing

The number of compression stages determines both efficiency and discharge temperature. Each stage should operate with a pressure ratio of 3-5 to keep discharge temperature below 150-180°C.

**Optimal stage pressure ratios**: For N stages with equal pressure ratios, the ratio per stage is (P_discharge / P_inlet)^(1/N). Examples:
- 1 to 10 bar: 1 stage (ratio 10:1 is at the upper limit — discharge temperature ~250°C). Add a second stage if temperature must stay below 180°C.
- 1 to 30 bar: 2 stages, ratio √30 ≈ 5.5 per stage. Intercooler required.
- 1 to 100 bar: 3 stages, ratio ∛100 ≈ 4.6 per stage.
- 1 to 350 bar: 4 stages, ratio ∜350 ≈ 4.3 per stage.

**Intercooler effectiveness**: An intercooler that brings the gas to within 5°C of cooling water temperature gives the best second-stage efficiency. Each 10°C of imperfect cooling increases total power consumption by 2-3%. Size the intercooler generously — it is the cheapest way to improve compressor efficiency.

**Receiver tank sizing**: A receiver tank on the discharge line dampens pulsations from reciprocating compressors and provides stored volume for intermittent demand. Minimum size: 10-20% of the compressor's free air delivery per minute. Example: a 10 m³/min compressor needs a 1-2 m³ receiver. The tank also allows moisture to settle out before the gas reaches downstream equipment.

## Drive Systems and Control

**Motor selection**: Compressor motors are sized based on shaft power requirements with a 10-15% service factor. A 10 bar reciprocating compressor with 5 m³/min FAD requires approximately 30 kW shaft power. Motor: 37 kW (50 HP) TEFC (totally enclosed fan-cooled) induction motor, 3-phase, 1450 or 2900 RPM. For hazardous-area gas compression (flammable or toxic gases), use an explosion-proof (Ex d) motor enclosure.

**Belt drive vs. direct coupling**:
- **Belt drive (V-belts)**: Allows speed reduction from motor to compressor. Typical ratio: 2:1 to 4:1. V-belts absorb shock loads and provide some protection against jamming (belts slip rather than stalling the motor). Tension: deflect belt 16 mm per meter of span center with moderate finger pressure. Replace belts in matched sets.
- **Direct coupling (flexible coupling)**: Used when motor and compressor run at the same speed, or when a gear reducer is integrated. More efficient (no belt slip losses, typically 2-3%). Requires precise shaft alignment (angular <0.05 mm/100 mm, parallel <0.05 mm). Misalignment causes premature bearing failure.

**Capacity control methods**:
- **Start/stop**: The simplest control — compressor runs until receiver pressure reaches upper setpoint, then shuts off. Restarts when pressure drops to lower setpoint. Suitable for intermittent duty. Motor starting current is 5-8× rated current; limit starts to 4-8 per hour to prevent motor overheating.
- **Load/unload**: Compressor runs continuously but unloads (opens suction valve or bypasses discharge to suction) when receiver pressure is at upper setpoint. Loads again when pressure drops. Used for compressors that cannot be started frequently. Unloaded power: 15-30% of loaded power.
- **Modulating (throttling)**: A suction throttle valve reduces intake volume, matching output to demand. Efficient at 60-100% load. Inefficient below 60% (throttling losses). Used on screw and centrifugal compressors.
- **Variable speed drive (VSD)**: Electronic motor speed control matches compressor output to demand across 30-100% range. Most efficient method at partial loads. Premium cost ($2,000-10,000 for the drive). Payback: 1-3 years for compressors with variable demand profiles.

**Lubrication system**: Reciprocating compressors use splash lubrication (crankshaft dips into oil sump) for small units, or pressurized lubrication (gear pump delivers oil to bearings, cylinder walls, and piston pins) for units above 30 kW. Oil pressure: 1-3 bar above crankcase pressure. Oil filter: full-flow, 25 μm nominal. Oil temperature: 60-80°C operating range. Oil change interval: 2,000-4,000 operating hours for mineral oil, 4,000-8,000 hours for synthetic.

## Expected Performance

| Parameter | Reciprocating (2-stage) | Rotary Screw (oil-flooded) | Diaphragm |
|-----------|------------------------|---------------------------|-----------|
| Discharge pressure | 10-350 bar (multi-stage) | 5-15 bar (single stage) | 10-1000+ bar (multi-stage) |
| Flow range (FAD) | 1-500 m³/hour | 5-3000 m³/hour | 0.1-50 m³/hour |
| Power consumption | 5-200 kW | 5-500 kW | 2-50 kW |
| Isothermal efficiency | 60-75% | 65-80% (oil-flooded) | 50-65% |
| Discharge temperature (per stage) | 120-180°C | 80-110°C (oil-cooled) | 100-150°C |
| Oil carryover in discharge gas | 5-50 ppm (lubricated) | 2-10 ppm (with separator) | Zero (gas isolated from oil) |
| Duty cycle | Intermittent to continuous | Continuous | Intermittent to continuous |
| Service life (before overhaul) | 15,000-30,000 hours | 30,000-60,000 hours | 10,000-20,000 hours |

## Strengths

- Reciprocating compressors achieve the highest discharge pressures (up to 350+ bar in multi-stage) — essential for cylinder filling and high-pressure gas processes
- Oil-flooded screw compressors run continuously with low vibration — ideal for plant air and process gas supply
- Diaphragm compressors provide zero gas contamination — the only option for ultra-pure gases (semiconductor-grade H₂, O₂, Ar)
- Multi-stage compression with intercooling approaches isothermal efficiency, minimizing power consumption

## Weaknesses

- Reciprocating compressors are heavy, noisy, and produce pulsating flow — pulsation dampeners or receiver tanks needed on the discharge
- Oil-flooded screw compressors contaminate the gas with oil — not acceptable for breathing air, food processing, or semiconductor applications without extensive downstream filtration
- Diaphragm compressors have low flow rates relative to their physical size and cost — the diaphragm is a wear item with limited fatigue life
- All compressors generate significant heat — intercoolers, aftercoolers, and oil coolers add complexity and cost

## Safety

- **Overpressure**: Compressors generate increasing pressure until something fails. Install a pressure relief valve on every stage discharge, set to 110% of maximum allowable working pressure (MAWP). Test relief valves quarterly.
- **Oil fire**: Compressor oil in contact with hot discharge gas (above auto-ignition temperature ~250°C for mineral oil) can ignite. This is a catastrophic event inside the compressor. Monitor discharge temperature and shut down above 180°C. Use synthetic oil with higher auto-ignition temperature for high-pressure service.
- **Toxic gas handling**: Compressing toxic gases (CO, H₂S, Cl₂) requires leak-tight construction (diaphragm or oil-free reciprocating), gas detection in the compressor room, and emergency ventilation rated for the specific gas.
- **Noise**: Compressors produce 85-110 dB noise levels. Hearing protection required for all personnel in the compressor room. Enclose the compressor in a sound-attenuating housing for continuous operation near occupied areas.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Discharge pressure below rated | Worn suction/discharge valves (not seating); worn piston rings (blowby); leaking gaskets | Remove and inspect valve plates — look for carbon deposits, broken springs, eroded seats. Replace piston rings if cylinder compression test shows blowby. |
| Excessive discharge temperature | Intercooler fouled or water flow insufficient; excessive pressure ratio per stage; suction temperature too high | Clean intercooler tubes. Verify cooling water flow rate and inlet temperature. Check first-stage discharge pressure — if above 5 bar, the intercooler is undersized. |
| Oil in discharge gas | Worn oil separator element; excessive oil injection rate; failed oil scraper ring | Replace coalescing separator element. Reduce oil injection rate. Inspect and replace scraper rings on the piston rod. |
| Vibration increasing | Loose foundation bolts; worn bearings; crankshaft imbalance; valve breakage | Tighten foundation bolts in cross-pattern. Check bearing clearances with dial indicator. Rebalance if crankshaft was repaired. Replace broken valve plates. |
| Compressor won't start (motor trips) | Liquid in cylinder (hydraulic lock); seized piston; motor undersized | Turn compressor over by hand — if locked, remove cylinder head and check for liquid. Never start a compressor with liquid in the cylinder — the incompressible liquid will bend the connecting rod or crack the cylinder. |
| Gas leakage at shaft seal | Worn lip seal; scored shaft surface; excessive pressure in crankcase | Replace lip seal. Check shaft surface for scoring — polish or replace shaft. Install a crankcase vent to prevent pressure buildup. |
| Interstage pressure imbalance (first stage >6 bar discharge) | Intercooler restricted or second-stage suction valve stuck closed | Clean intercooler tubes and verify water flow. Inspect second-stage suction valve for stuck or broken spring. High interstage pressure overloads first-stage cylinder. |
| Diaphragm failure (gas in hydraulic oil) | Diaphragm fatigue crack from overpressure or excessive deflection cycles | Replace diaphragm. Check hydraulic relief valve setting — should limit oil pressure to 110% of discharge. Verify contour plate profile matches head cavity. Expected diaphragm life: 2000-5000 hours. |
| Screw compressor surge (hunting load/unload) | Discharge pressure set too close to maximum; control valve hysteresis | Increase unload pressure differential (at least 1 bar between load and unload setpoints). Check modulation valve response. Verify receiver tank is adequately sized. |
| Moisture carryover in discharge after aftercooler | Aftercooler fouled or undersized; automatic drain valve stuck closed | Clean aftercooler tubes. Verify drain valve operates (should discharge water every 5-15 minutes). If ambient humidity is high, add a refrigerated dryer downstream. |

## See Also

- [Basic Gas Handling](basic.md) — compressor types overview, gas cylinder safety
- [Cylinder Filling](cylinder-filling.md) — high-pressure compressors for gas cylinder filling
- [Gas Purification](gas-purification.md) — gas drying and scrubbing before or after compression
- [Piping Systems](piping-systems.md) — high-pressure gas piping design
- [Lubricants](../chemistry/lubricants.md) — compressor oil selection and maintenance
- [Iron & Steel](../metals/iron-steel.md) — materials for pressure-containing components

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Gas Handling](./index.md) • [All Domains](../../index.md)*
