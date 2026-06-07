# Thermostats & Temperature Control Devices

> **Node ID**: measurement.thermostat
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`metals`](../metals/copper-bronze.md), [`measurement.temperature-pressure`](./temperature-pressure.md)
> **Enables**: [`energy.cooling`](../energy/cooling.md), [`silicon.crystal-growth.cz-pulling`](../silicon/cz-pulling.md)
> **Critical**: No — thermostats provide automated temperature control but manual temperature monitoring is a functional alternative
> **Timeline**: Years 5-60+
> **Outputs**: on_off_control, proportional_control, pid_control, temperature_regulation


Temperature control is what separates haphazard craft from repeatable manufacturing. A kiln that overshoots by 50°C cracks its pottery. A furnace running too cold wastes fuel and produces inconsistent metal. A chemical reactor that drifts 10°C produces different reaction products than intended. And semiconductor manufacturing? Crystal growth furnaces need ±0.5°C stability at 1400°C. Diffusion furnaces demand ±0.1°C. Without thermostats, every thermal process is a gamble controlled by human attention span and guesswork.

A civilization that cannot regulate temperature cannot produce consistent steel, cannot run chemical processes reliably, and certainly cannot grow silicon crystals or fabricate integrated circuits. Thermostats close the feedback loop: sense temperature, compare it to a setpoint, and actuate a heater or cooler to drive the process toward the target. This topic covers 22 thermostat types across five categories, progressing from the simplest mechanical expansion rod (buildable with basic metalworking) through pneumatic and electronic systems to infrared pyrometer feedback loops suitable for semiconductor furnaces.


## Articles in this Topic

- [Mechanical Thermostats](./thermostat-mechanical.md) — Expansion rod, rod-and-tube, bimetallic strip, and snap-action disc types. No external power required. Buildable with basic metalworking. ±2-20°C accuracy.
- [Fluid & Gas Thermostats](./thermostat-fluid.md) — Mercury tilt, mercury contact thermometer, liquid expansion, vapor pressure, gas expansion, wax pellet, thermostatic radiator valve, and pneumatic types. Remote sensing, proportional control, no electronics needed. ±0.5-3°C accuracy.
- [Electrical Thermostats](./thermostat-electrical.md) — Thermocouple, RTD (resistance thermometer), and reed switch types. Self-generating sensors and precision bridge circuits. ±0.1-5°C accuracy over -200 to 1800°C.
- [Electronic Thermostats](./thermostat-electronic.md) — Thermistor, silicon junction, IC sensor, and digital PID microcontroller types. Active circuitry for precise control. ±0.01-1°C accuracy with PID.
- [Advanced & Specialty Thermostats](./thermostat-advanced.md) — Shape memory alloy actuators, quartz crystal sensors, and infrared pyrometers. Non-contact sensing, calibration-grade precision. ±0.01°C to ±2% of reading.


## Selection Guide

| Type | Range (°C) | Accuracy | Power Required | Remote Sensing | Best Use |
|------|-----------|----------|---------------|----------------|----------|
| 1. Single-metal rod | 100-800 | ±10-20°C | None | No | Crude furnace draft control |
| 2. Rod-and-tube | 50-800 | ±5-10°C | None | No | Simple oven, kiln control |
| 3. Bimetallic strip | -50 to 500 | ±2-5°C | None | No | General-purpose switching |
| 4. Snap-action disc | 30-300 | ±2-3°C | None | No | Appliance safety cutoff |
| 5. Mercury tilt | -10 to 300 | ±0.5-1°C | None | No | Room thermostat (heating) |
| 6. Mercury contact | -30 to 300 | ±0.1-0.5°C | None | No | Lab temperature regulation |
| 7. Liquid expansion | -50 to 400 | ±1-3°C | None | Yes | Remote oven/tank sensing |
| 8. Vapor pressure | -50 to 300 | ±1-2°C | None | Yes | Refrigeration TXV |
| 9. Gas expansion | -200 to 800 | ±0.5-1°C | None | Yes | Industrial furnace |
| 10. Wax pellet | 30-95 | ±2-3°C | None | No | Engine cooling thermostat |
| 11. TRV | 5-30 | ±1-2°C | None | No | Radiator zone control |
| 12. Pneumatic | 10-35 | ±0.5-1°C | Compressed air | No | Building HVAC |
| 13. Thermocouple | -200 to 1800 | ±1-5°C | Sensor: none | Yes | High-temp furnace control |
| 14. RTD | -200 to 850 | ±0.1-1°C | Electronics | Yes | Precision furnace control |
| 15. Reed switch | -40 to 120 | ±1-2°C | None | No | Spark-free switching |
| 16. Thermistor | -50 to 300 | ±0.1-1°C | Electronics | Yes | General electronic thermostat |
| 17. Silicon junction | -55 to 150 | ±1-3°C | Electronics | No | Embedded sensor in circuits |
| 18. IC sensor | -55 to 150 | ±0.5°C | Electronics | No | Smart thermostat projects |
| 19. PID/microcontroller | Sensor-dependent | ±0.01°C possible | Electronics | Yes | Precision process control |
| 20. SMA actuator | -100 to 100 | ±1-2°C | Optional | No | Compact thermal actuator |
| 21. Quartz crystal | -50 to 250 | ±0.01-0.05°C | Electronics | No | Calibration-grade sensing |
| 22. IR pyrometer | 0 to 3000+ | ±0.5-2% | Electronics | Yes (non-contact) | High-temp, non-contact |

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundational metalworking | Expansion rod, rod-and-tube, bimetallic strip thermostats for furnace and kiln control |
| Glass & Chemistry | Mercury tilt, mercury contact, liquid/vapor/gas thermostats (glassworking, hermetic sealing, fluid handling) |
| Energy & Steam | Pneumatic thermostats for building HVAC, thermocouple-based boiler control, wax pellet engine cooling |
| Chemistry & Processes | Vapor pressure thermostats for refrigeration, RTD thermostats for reaction temperature control |
| Electronics | Thermistor, silicon junction, and IC sensor thermostats; PID control with microcontroller |
| Silicon & Semiconductors | PID-controlled furnaces with RTD or thermocouple sensors (±0.1-0.5°C), IR pyrometers for wafer temperature |
| Quality Control | Calibration-grade quartz crystal sensors (±0.01°C), temperature cycling tests |

## Key Deliverables

- **Tier 1** (Years 5-15): Bimetallic strip and snap-action disc thermostats for basic furnace and kiln control. These require only metalworking and are sufficient for steel production, pottery firing, and basic chemical processing.
- **Tier 2** (Years 15-25): Mercury tilt thermostat for precise room and oven control. Liquid expansion and vapor pressure thermostats for remote sensing in industrial processes. Wax pellet thermostats for engine cooling once internal combustion is developed.
- **Tier 3** (Years 25-40): Thermocouple thermostats for high-temperature furnace control (steel, glass, ceramics). RTD thermostats for precision applications. These are essential for the chemistry and early semiconductor stages.
- **Tier 4** (Years 40-60+): Digital PID thermostats with thermistor, RTD, or IC sensors for semiconductor furnace control (±0.1°C or better). IR pyrometer feedback for crystal growth and rapid thermal processing. Quartz crystal sensors for calibration-grade temperature measurement.

## Safety & Hazards

- **Mercury toxicity**: Types 5 and 6 use elemental mercury. Mercury vapor from spills, broken ampoules, and filling operations causes cumulative neurological damage. IDLH: 10 mg/m³. Vapor pressure at 20°C is 0.0012 mm Hg, enough to exceed safe limits in unventilated rooms after a spill. Fill and calibrate mercury thermostats in fume hoods or under local exhaust ventilation. Clean spills with zinc dust or commercial mercury absorbent. Never vacuum mercury spills (vaporizes mercury and disperses it). Store mercury in sealed glass containers under water or mineral oil. Use mercury-free alternatives (bimetallic strip, thermocouple, thermistor) wherever possible.
- **Pressure hazards**: Types 7-9 (sealed fluid and gas systems) contain pressurized fluids. A gas expansion thermostat at 800°C may contain nitrogen at 25+ bar. Sudden rupture of the bulb or capillary causes explosive release of hot fluid. Proof-test all sealed systems at 1.5× maximum operating pressure behind a polycarbonate blast shield. Never point the capillary end toward anyone during pressure testing. Replace any unit that shows bulging, cracking, or corrosion.
- **High-temperature burn risks**: Thermostat calibration involves placing sensors in hot baths, ovens, and furnaces. Temperatures of 200-1000°C cause instant deep burns on contact. Use heat-resistant gloves, tongs, and face shields. Allow equipment to cool before handling.
- **Electrical hazards**: Types 13-19 involve mains-voltage switching (120-240V AC) through relays and triacs. Incorrect wiring causes electrocution, fire, or equipment damage. Use insulated tools, work with power disconnected, and verify with a voltmeter before touching any circuit. Enclose all mains-voltage wiring in grounded metal or insulated enclosures.
- **Fire risk from heater runaway**: The most dangerous failure mode for any thermostat is stuck-on (heater remains powered indefinitely). A 2 kW oven element stuck on in an insulated enclosure can reach 800°C, igniting surrounding materials. Always include an independent high-limit cutoff (bimetallic disc, Type 4) wired in series with the heater, set 20-50°C above the normal operating range. This backup device must be mechanically independent of the primary thermostat.

## Limitations

- **Mechanical wear**: Contact-type thermostats (Types 1-6, 15) rely on physical contacts that erode with each switching cycle. A relay switching 10A at 240V AC has a rated life of 100,000-1,000,000 cycles. At 6 cycles per hour (typical heating system), this is 2-20 years. Arcing accelerates wear; snap-action mechanisms (Types 4, 5) reduce arcing by switching fast.
- **Deadband and hysteresis**: On/off thermostats cannot hold temperature exactly at the setpoint. They cycle between an upper and lower limit (the deadband). Mechanical thermostats have deadbands of 1-15°C. Even electronic on/off thermostats have 0.5-2°C deadband (set by software hysteresis). Only PID control (Type 19) eliminates deadband by modulating heater power proportionally.
- **Thermal lag**: The sensor temperature always lags behind the process temperature. A bimetallic strip in still air takes 30-60 seconds to reach equilibrium. A thermocouple in a thermowell takes 5-20 seconds. This lag causes overshoot (heater is still on when the process is already above setpoint because the sensor has not caught up). PID control compensates for lag with the derivative term, but it cannot eliminate it entirely.
- **Sensor range limits**: No single sensor covers the full range from cryogenic to 3000°C. Thermocouples cover the widest range but sacrifice low-temperature accuracy. RTDs are best from -200 to 850°C. Thermistors are best from -50 to 300°C. IR pyrometers struggle below 0°C (weak radiation signal). Any bootstrap civilization needs multiple sensor types for different applications.
- **Calibration drift**: All temperature sensors drift with time and thermal cycling. Thermocouples drift 1-5°C per 1000 hours at high temperature. RTDs drift 0.1-0.5°C per year. Thermistors drift 0.1-0.2°C per year. Regular calibration against fixed-point references (ice point, steam point, metal freezing points) is essential. A thermostat that was accurate when installed will be inaccurate after a year of service without recalibration.
- **Electromagnetic interference**: Electronic thermostats (Types 16-19) are susceptible to EMI from motor drives, welders, and radio transmitters. A thermocouple wire run alongside a motor power cable can pick up several millivolts of noise, causing temperature errors of 10-50°C. Use twisted-pair wiring, shielded cables, and signal conditioning filters to reject interference.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Single-metal expansion rod thermostat trips at wrong temperature (±10-20°C error) | Mounting bracket flexure mistaken for thermal expansion; set screw drifted from vibration; rod end not filed perpendicular | Bolt bracket rigidly to 10 mm cast iron base plate; add locknut to set screw; file rod ends flat and perpendicular — tilted contact introduces angular error; recalibrate at 2-3°C/minute heating rate against reference thermometer |
| Rod-and-tube differential thermostat binding at high temperature | Sliding fit between iron rod (7.5 mm) and copper tube (8 mm ID) too tight; differential expansion causes the rod to seize | Maintain 0.5 mm clearance (7.5 mm rod in 8.0 mm bore); use spacer ring (copper wire, 0.5 mm) at free end for centering; lubricate with graphite powder; if binding persists, increase clearance to 0.7 mm |
| Bimetallic strip contacts arcing and burning (reduced contact life) | Plain strip without snap-action bending gradually; contacts separate slowly, drawing arc each cycle | Add snap-action by overbending strip 2-3 mm past flat (initial camber toward brass side); snap-action causes instantaneous separation eliminating arcing; braze silver or tungsten contact tips (2-3 mm diameter) to free end for arc resistance |
| Mercury tilt thermostat setpoint shifts depending on mounting orientation | Static imbalance of moving assembly (coil + arm + ampoule) on pivot; gravity biases mercury position | Balance the entire moving mass on the pivot bearing; add counterweight to the arm opposite the ampoule; mount thermostat in intended orientation during calibration — gravity determines which way mercury flows; recheck after installation |
| Thermocouple thermostat reading offset by 20-25°C at room temperature | Cold junction compensation not functioning; instrument assumes 0°C reference while terminals are at 20-25°C | Verify cold junction compensation circuit (thermistor or RTD at terminal block); for galvanometer relay, check bimetallic strip on coil is shifting zero point correctly; for electronic method, verify compensation voltage is added — Type K thermocouple produces ~40 μV/°C at cold junction |
| RTD Wheatstone bridge not balancing at 0°C (expected 100.0 Ω) | Lead wire resistance (0.6 Ω per 3 m of 0.5 mm copper wire) adding to RTD reading; bridge resistor tolerance too loose | Switch to four-wire (Kelvin) connection to eliminate lead resistance; use manganin wire resistors (±0.01% tolerance, near-zero temperature coefficient of ~20 ppm/°C); trim bridge arms at 0°C in ice-water bath |
| Wax pellet thermostat piston stroke insufficient (below 8-12 mm) | Wrong wax blend with narrow melting range; wax filled to above 85% of bore volume (no room for expansion); piston binding in tapered bore | Select wax with sharp melting transition (2-3°C range); fill to 85% of bore volume only — the air gap allows initial expansion; verify bore is uniform within 0.02 mm along entire length (taper causes piston binding); total stroke should be 8-12 mm for 25 mm deep pellet |
| Pneumatic thermostat output pressure jumping in steps instead of changing smoothly | Nozzle contaminated or partially blocked; restrictor orifice (0.15 mm) clogged with dirt in air supply | Clean nozzle orifice (0.8 mm) with solvent and compressed air; install air line filter (5 μm) upstream of restrictor; verify restrictor orifice (0.15 mm) is clear — this tiny hole is easily blocked; use only clean, dry compressed air (18-20 psi supply) |
| Thermistor thermostat relay chattering when temperature nears setpoint | Insufficient hysteresis in comparator feedback; electrical noise on thermistor voltage divider output | Increase feedback resistor from comparator output to non-inverting input (try 1-10 MΩ range — higher resistance = wider hysteresis); add 100 nF bypass capacitor across thermistor to filter noise; target 0.5-2°C hysteresis to prevent rapid cycling |
| PID-controlled furnace oscillating ±5-10°C around setpoint instead of settling | PID tuning constants wrong: proportional gain (Kp) too high causing overshoot; integral time (Ki) too aggressive; derivative amplifying noise | Reduce Kp until oscillation amplitude halves; then reduce Ki (integral) to eliminate steady-state offset without causing oscillation; set Kd (derivative) low initially — derivative amplifies measurement noise; typical starting values for a 2 kW furnace: Kp=5, Ki=0.5/min, Kd=30 sec; tune empirically |

## Bootstrap Progression

The 22 thermostat types form a natural dependency chain that tracks the civilization's technological capability:

**Stage 1 — Basic Metalworking (Years 5-15)**: Expansion rod and bimetallic strip thermostats require only metalworking — no glass, no electronics, no precision machining. An expansion rod thermostat (Type 1) is a brass or iron rod that protrudes through a furnace wall and pushes a damper lever as it heats and elongates. Accuracy is ±10-20°C, but this is enough to prevent kiln overshoot and regulate draft. Bimetallic strips (Types 3-4) improve accuracy to ±2-5°C and enable snap-action switching for appliance safety cutoffs. These are sufficient for steel production, pottery firing, and basic chemical heating.

**Stage 2 — Glassworking & Fluid Handling (Years 15-25)**: Mercury tilt thermostats (Type 5) require glassblowing to seal mercury in a glass ampoule with electrical contacts. Liquid expansion and vapor pressure thermostats (Types 7-9) require capillary tubing and sealed bulb construction. These enable remote temperature sensing (sensor at the process, switch at a distance) and improved accuracy to ±0.5-3°C. Essential for chemical process control, refrigeration, and industrial oven regulation.

**Stage 3 — Electrical Measurement (Years 25-40)**: Thermocouple and RTD thermostats (Types 13-14) require wire drawing for thermocouple alloys (Type K: chromel/alumel) or fine platinum wire for RTDs, plus basic electronic circuits (Wheatstone bridge, galvanometer relay). Accuracy improves to ±0.1-5°C over ranges from -200 to 1800°C. These are essential for steel heat treatment, glass melting, and early semiconductor processing where ±5°C is not adequate.

**Stage 4 — Electronics & Semiconductors (Years 40-60+)**: Thermistor, IC sensor, and PID thermostats (Types 16-19) require semiconductor manufacturing capability — the very capability they help enable. This circular dependency is resolved by using thermocouple/RTD thermostats for the first generation of semiconductor furnaces, then transitioning to thermistor/PID control once basic semiconductor devices become available. Quartz crystal sensors (Type 21) and IR pyrometers (Type 22) represent the precision ceiling, enabling calibration-grade measurement (±0.01°C) and non-contact sensing at extreme temperatures.

## Scaling Notes

Thermostat production scales with the precision of the underlying technology:

- **Workshop scale** (1-50 units/day): Hand-formed bimetallic strips, hand-blown mercury ampoules, point-to-point wired electronic circuits. Each unit individually calibrated against reference thermometer. Adequate for equipping a single factory or laboratory.

- **Factory scale** (500-5,000 units/day): Stamped bimetallic elements, automated glass sealing for mercury bulbs, PCB-assembled electronic controllers with automated test and calibration. Statistical process control on trip temperature. This scale supplies an industrial economy's HVAC, appliance, and process control thermostat needs.

- **Precision scale** (specialized, low volume): Hand-assembled and individually calibrated RTD and thermistor probes for laboratory and semiconductor furnace use. Each probe certified against NIST-traceable standards. Production rate: 10-100 units/day. Quality and consistency matter more than volume.

**Critical bottleneck**: Calibration infrastructure. Every thermostat is only as accurate as its calibration reference. A civilization needs at minimum: ice point (0.0°C), steam point (100.0°C at 1 atm), and several metal freezing points (Sn 231.9°C, Zn 419.5°C, Ag 961.8°C, Au 1064.2°C) to establish a reliable temperature scale. Without calibration standards, even perfectly constructed thermostats give inaccurate readings.

## Quality Control

| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Trip temperature accuracy | Calibrated reference thermometer in stirred bath | ±2°C for mechanical, ±0.5°C for electronic, ±0.1°C for precision grades |
| Deadband (on-off differential) | Measure temperature at make and break points | Within manufacturer specification (typically 0.5-5°C depending on type) |
| Contact resistance (mechanical) | 4-wire milliohmmeter on closed contacts | <50 mΩ for silver contacts, <100 mΩ for tungsten |
| Cycle life | Automated cycling at rated load | 100,000 cycles minimum for appliance grade |
| Sensor resistance (RTD) | Precision ohmmeter at 0°C ice point | 100.0 Ω ±0.1% for Pt100 RTD |
| Sensor output (thermocouple) | Millivolt meter at known reference temperature | Within ±1% of NIST standard tables for the thermocouple type |
| PID controller tuning | Step response test on thermal load | Settles to ±0.5°C within 5 minutes with <10% overshoot |

## See Also

- [Temperature & Pressure Measurement](./temperature-pressure.md): thermocouples, RTDs, pyrometers, pressure gauges
- [Precision Metrology](./precision-metrology.md): calibration infrastructure, measurement uncertainty
- [Electrical Instruments](./electrical-instruments.md): multimeters, oscilloscopes, frequency counters
- [Metals](../metals/iron-steel.md): metal forming, thermocouple materials, spring steel
- [Glass](../glass/glassblowing.md): glassworking for mercury thermostats, ampoules
- [Chemistry](../chemistry/semiconductor-chemicals.md): mercury production, metal oxides for thermistors
- [Silicon](../silicon/basic-devices.md): semiconductor sensors, IC temperature sensors
- [Energy](../energy/cooling.md): steam systems, HVAC, engine cooling

## Variations and Alternatives

| Control Strategy | Accuracy | Cost | Complexity | Best Application |
|-----------------|----------|------|-----------|-----------------|
| On/off (mechanical) | ±2-20°C | Very low | Very low | Furnace draft, appliance safety cutoff |
| On/off (electronic) | ±0.5-2°C | Low | Low | Oven control, incubator, HVAC |
| Proportional (P) | ±0.5-1°C | Medium | Medium | Process heating with moderate stability needs |
| Proportional-Integral (PI) | ±0.1-0.5°C | Medium | Medium | Most industrial process control |
| Full PID | ±0.01-0.1°C | High | High | Semiconductor furnaces, crystal growth, calibration baths |
| Cascade (dual-loop) | ±0.05°C | High | Very high | Ultra-precision furnaces, multi-zone ovens |
| Fuzzy logic | ±0.5-2°C | Medium | Medium (software) | Nonlinear systems, HVAC comfort control |

**On/off vs. proportional**: The simplest thermostats operate in on/off mode — the heater is either fully on or fully off. This creates temperature oscillation within the deadband. For a kiln with 20°C deadband, the temperature cycles between (setpoint - 10°C) and (setpoint + 10°C). Proportional control modulates heater power as a percentage of full power, proportional to the error (difference between measured and setpoint temperature). A proportional controller at 50% power when the temperature is halfway to setpoint produces much smoother control. PID adds integral action (eliminates steady-state offset) and derivative action (anticipates temperature trends to reduce overshoot).

**Calibration reference points**: Any civilization developing thermostats needs reliable temperature fixed points for calibration:

| Fixed Point | Temperature | Material | Achievable Accuracy |
|------------|------------|----------|-------------------|
| Ice point | 0.00°C | Ice/water equilibrium | ±0.002°C |
| Steam point | 100.00°C | Boiling water at 1 atm | ±0.05°C (pressure-dependent) |
| Tin freeze | 231.93°C | Sn solidification | ±0.1°C |
| Zinc freeze | 419.53°C | Zn solidification | ±0.1°C |
| Silver freeze | 961.78°C | Ag solidification | ±0.5°C |
| Gold freeze | 1064.18°C | Au solidification | ±0.5°C |

These fixed points are reproducible because phase transitions (melting/freezing) occur at precisely defined temperatures. A calibrated thermometer chain — from ice point through metal freeze points — establishes the temperature scale against which all thermostats are verified. Without this calibration chain, thermostat accuracy claims are unverifiable.

**Redundancy best practice**: For any critical temperature-controlled process, use two independent thermostats: a primary controller (electronic or PID) and an independent mechanical high-limit cutoff (bimetallic snap disc) set 20-50°C above the normal operating range. The high-limit device is wired in series with the heater and requires manual reset. This prevents catastrophic runaway if the primary controller fails in the "heater on" state.

## Integration with Semiconductor Manufacturing

Thermostats are embedded throughout the semiconductor fabrication process chain:

| Process | Temperature Range | Required Stability | Thermostat Type |
|---------|-------------------|--------------------|----------------|
| Photoresist spin/bake | 90-120°C | ±1°C | Thermistor PID |
| Oxidation furnace | 800-1200°C | ±0.5°C | Thermocouple PID (Type S or R) |
| Diffusion furnace | 900-1200°C | ±0.1°C | Thermocouple PID with zone control |
| LPCVD deposition | 300-800°C | ±1°C | Thermocouple PID |
| PECVD deposition | 200-400°C | ±2°C | Thermocouple PID |
| Metal sputtering (substrate) | 20-400°C | ±2°C | Thermocouple PID |
| Rapid thermal anneal | 600-1100°C | ±5°C (ramp 50-200°C/s) | IR pyrometer PID |
| Crystal growth (Czochralski) | 1414°C (Si melting) | ±0.5°C | IR pyrometer + thermocouple cascade |
| Wafer chuck (CMP, litho) | 20-80°C | ±0.1°C | RTD or thermistor PID |
| Wet bench processes | 20-180°C | ±1°C | RTD PID |

The most demanding thermostat application in semiconductor manufacturing is the Czochralski silicon crystal pull. The melt temperature must be held within ±0.5°C of the 1414°C silicon melting point while a 200-300 mm crystal is pulled over 24-72 hours. This requires a cascade control loop: an IR pyrometer measures the melt surface temperature as the primary sensor, with a Type S (Pt-10%Rh/Pt) thermocouple embedded in the crucible susceptor as the secondary sensor. The PID controller modulates RF induction heater power with 0.1% resolution. Any temperature excursion beyond ±1°C during the pull creates dislocations in the crystal lattice, potentially scrapping the entire ingot (value: $5,000-50,000 depending on size and grade).

---

*Part of the [Bootciv Tech Tree](../index.md) • [Measurement](./index.md) • [All Domains](../index.md)*
