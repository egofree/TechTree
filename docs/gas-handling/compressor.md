# Gas Compressor

> **Node ID**: gas-handling.compressor
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`gas-handling.cylinder-filling`](cylinder-filling.md), [`chemistry.air-separation`](../chemistry/air-separation.md), [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md)
> **Timeline**: Years 15-30
> **Outputs**: compressed_gas
> **Critical**: Yes — gas compression is the enabling step for gas storage, transport, air separation, and virtually all gas-phase industrial chemistry

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

## Calibration and Verification

1. **Leak test**: Pressurize the compressor discharge to 50% of rated pressure with the compressor off (using an external air source). Soap-test all joints, valve covers, and shaft seals. Zero leaks on gas joints. Acceptable oil seepage at shaft seal: 10-30 drops/hour.
2. **Capacity test**: Run the compressor at rated speed into a known-volume receiver tank. Measure the time to pressurize from atmospheric to a target pressure. Calculate free air delivery (FAD): the volume of atmospheric air the compressor would need to draw in to produce the observed pressure rise. Compare to rated FAD.
3. **Discharge temperature check**: Run at full load for 30 minutes. Measure discharge temperature at each stage. First-stage discharge: should be below 180°C. After intercooler: within 15°C of cooling water. Second-stage discharge: below 180°C. Higher temperatures indicate inadequate intercooling, worn valves, or excessive pressure ratio.
4. **Vibration check**: Measure vibration at the crankcase, cylinder head, and discharge flange. Acceptable: below 4.5 mm/s RMS velocity. Higher vibration indicates misalignment, imbalance, or bearing wear.

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

## See Also

- [Basic Gas Handling](basic.md) — compressor types overview, gas cylinder safety
- [Cylinder Filling](cylinder-filling.md) — high-pressure compressors for gas cylinder filling
- [Gas Purification](gas-purification.md) — gas drying and scrubbing before or after compression
- [Piping Systems](piping-systems.md) — high-pressure gas piping design
- [Lubricants](../chemistry/lubricants.md) — compressor oil selection and maintenance
- [Iron & Steel](../metals/iron-steel.md) — materials for pressure-containing components

[← Back to Gas Handling](index.md)
