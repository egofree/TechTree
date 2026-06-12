# Electrical Thermostats

> **Node ID**: measurement.thermostat-electrical
> **Domain**: [Measurement](./index.md)
> **Dependencies**: `electronics`, [`measurement.electrical-instruments`](./electrical-instruments.md),
> [`measurement.temperature-pressure`](./temperature-pressure.md)
> **Enables**: [`measurement.thermostat-electronic`](./thermostat-electronic.md)
> **Critical**: No — thermocouple-based thermostats are self-generating but not the only option
> **Timeline**: Years 15-40
> **Outputs**: high_temperature_sensing, self_generating_sensor, precision_resistance_sensing

Electrical thermostats use electrical properties of materials (thermoelectric voltage, resistance change, magnetic actuation) to sense temperature. Unlike the mechanical and fluid types, these require some form of electrical measurement circuitry but gain much wider temperature ranges and better accuracy in return. The thermocouple is self-generating (needs no power at the sensor), the RTD provides the highest accuracy and stability of any contact sensor, and the reed switch offers sealed contactless switching.

## Thermocouple-Based Thermostat

**Principle**: Two dissimilar metals joined at a measurement junction generate a small voltage (Seebeck effect) proportional to the temperature difference between the measurement (hot) junction and the reference (cold) junction. This voltage, typically in the millivolt range, drives a galvanometer relay or electronic comparator. When the voltage exceeds the setpoint threshold (corresponding to the target temperature), the relay trips, shutting off the heater. The thermocouple is self-generating: it needs no external power to produce its temperature signal. This makes it the simplest possible high-temperature thermostat.

**Prerequisites**:
- [Thermocouple wire](./temperature-pressure.md) (chromel, alumel, or other dissimilar metal pairs)
- [Millivoltmeter or galvanometer relay](./electrical-instruments.md), or [electronic comparator circuit](../electronics/semiconductor-devices.md)
- [Relay](../electronics/passive-components.md) for switching the heater (if not using a galvanometer relay directly)
- [Cold-junction temperature measurement](./temperature-pressure.md) (for compensation)

**Materials**:
- [Thermocouple wire](./temperature-pressure.md) (Type K: chromel + alumel, 0.5-1.0 mm diameter, 1-3 m length, depending on application)
- [Thermocouple plug/jack](../metals/alloys.md) (compatible alloy terminals, to avoid introducing third-metal errors)
- [Galvanometer relay](./electrical-instruments.md) (moving-coil meter with contacts) or [electronic comparator](../electronics/semiconductor-devices.md) (op-amp + reference voltage + relay driver)
- [Relay](../electronics/passive-components.md): mechanical (10-20 A contacts) or [solid-state relay](../electronics/power-electronics.md) (SSR, 20-40 A)
- [Reference temperature sensor](./temperature-pressure.md) (thermistor or RTD at the cold junction) if using electronic compensation
- [Ice bath](../water/procurement.md) or isothermal block for cold junction (if using manual compensation)

**Construction**:

1. **Make the thermocouple junction**: Strip 10 mm of insulation from both thermocouple wires. Twist the bare ends together tightly (6-8 turns). Weld the junction using a capacitance-discharge welder (preferred for consistent junctions) or gas torch with borax flux. The junction must be a clean weld, not just a twist. A twisted junction adds contact resistance that drifts with corrosion and mechanical vibration. Test: the resistance of the junction should be within 10% of the calculated resistance of the wire lengths.

2. **Insulate the wires**: Slide ceramic insulator beads (2 mm bore, 4 mm long) over each wire from the junction to the terminals. Alternatively, use mineral-insulated (MgO) sheathed thermocouple cable for harsh environments. The two wires must not short together anywhere except at the measurement junction.

3. **Connect to the measuring circuit**:
   - **Galvanometer relay method** (simplest, no electronics): Connect the thermocouple wires directly to a galvanometer relay. This is a sensitive moving-coil meter (like a millivoltmeter) with adjustable contact points. The meter needle deflects proportionally to the thermocouple voltage. When the needle reaches the setpoint contact, the circuit closes, driving a power relay. Cold junction compensation is done mechanically: a bimetallic strip on the galvanometer coil shifts the zero point to compensate for ambient temperature changes.
   - **Electronic comparator method** (more precise): Connect the thermocouple to an instrumentation amplifier (gain 100-1000×). The amplified voltage is compared to a reference voltage (set by a potentiometer, the setpoint dial) using a comparator IC (LM311 or similar). When the thermocouple voltage exceeds the setpoint, the comparator output drives a relay or SSR. Cold junction compensation is done electronically: a thermistor or RTD at the terminal block measures the local temperature, and a compensation circuit adds or subtracts the appropriate offset voltage.

4. **Set up cold junction compensation**: The thermocouple voltage represents the *difference* between the hot junction and the cold junction (terminal block) temperatures. To measure absolute temperature, you must know the cold junction temperature. Three methods:
   - **Ice bath** (most accurate): immerse the terminal block in an ice-water slurry (0°C). The thermocouple voltage now reads directly in °C (0°C reference). Not practical for permanent installations but used for calibration.
   - **Electronic compensation**: measure the terminal block temperature with a thermistor or RTD and add the corresponding compensation voltage. This is standard in all commercial thermocouple instruments.
   - **Isothermal block**: mount the terminal block on a large aluminum block with slow thermal response. The block temperature is measured once and assumed constant during short measurements.

5. **Wire the output**: Connect the relay output to the heater circuit. For simple on/off control, wire the relay contacts in series with the heater power. For a basic proportional control, use a time-proportioning relay (cycling the heater on and off with variable duty cycle).

**Calibration**:

1. Calibrate the thermocouple at two reference points: ice-water (0°C) and boiling water (100°C at 1 atm). Record the output voltage at each point. For Type K, the expected values are 0.000 mV at 0°C and 4.096 mV at 100°C (with cold junction at 0°C).
2. Check linearity at intermediate points. Type K is not perfectly linear (sensitivity varies from ~39 μV/°C at 0°C to ~42 μV/°C at 1000°C), but it is close enough for ±2-3°C accuracy using linear interpolation.
3. Verify cold junction compensation: with the thermocouple at a known temperature (e.g., immersed in boiling water at 100°C), check that the instrument reads correctly with the terminal block at room temperature (typically 20-25°C). If the reading is off by about the room temperature value, the cold junction compensation is not working.
4. For the galvanometer relay, adjust the contact position to set the trip point. For the electronic comparator, adjust the reference potentiometer.

**Expected accuracy**: ±1-5°C over -200 to 1800°C (depending on thermocouple type and calibration effort). Self-generating, no power required for the sensor itself. Type K covers -200 to 1260°C. Type S covers 0 to 1600°C with lower sensitivity but better stability.

**Applications**: Furnace temperature control, kiln firing, gas appliance safety (thermocouple holds gas valve open while pilot flame heats the junction), automotive exhaust gas temperature, any application requiring high-temperature sensing with minimal infrastructure. The thermocouple thermostat is the workhorse of industrial temperature control. If you can make two different metal wires and weld their ends together, you can regulate furnace temperature.

**Strengths**:
- Self-generating sensor; no power needed at the measurement point
- Widest temperature range of any contact sensor (-200 to 1800°C depending on type)
- Extremely simple to construct: two wires welded together
- Rugged and resistant to vibration, shock, and high temperature
- Fast response, especially with bare or grounded junctions

**Weaknesses**:
- Very low output signal (millivolts) susceptible to electrical noise
- Cold junction compensation required for accurate readings
- Non-linear voltage-temperature relationship varies by thermocouple type
- Calibration drift of 1-5°C per 1000 hours at high temperature
- Lower accuracy than RTDs or thermistors without careful calibration

## Resistance Thermometer (RTD) Thermostat

**Principle**: A fine platinum wire (or thin-film platinum element) increases in electrical resistance predictably with temperature. The Pt100 standard specifies 100.0 Ω at 0°C with a temperature coefficient of +0.385 Ω/°C. At 100°C, the resistance is 138.5 Ω. The resistance is measured using a Wheatstone bridge circuit: three fixed resistors and the RTD form the bridge, and a galvanometer or amplifier detects the imbalance voltage when the RTD resistance deviates from the setpoint value. The bridge output drives a relay or control circuit.

**Prerequisites**:
- [Fine wire drawing capability](../metals/precious-metals.md) (platinum wire, 0.025-0.05 mm diameter) or thin-film deposition
- [Wheatstone bridge circuit construction](../electronics/passive-components.md) (precision resistors, galvanometer or amplifier)
- [Platinum sourcing](../metals/precious-metals.md) (rare but needed for accuracy and stability)
- [Four-wire measurement technique](../electronics/passive-components.md) for lead resistance elimination

**Materials**:
- [Platinum wire](../metals/precious-metals.md) (0.05 mm diameter, 2 m length) or commercial Pt100 element
- [Manganin wire](../metals/alloys.md) (for precision bridge resistors): 0.1 mm diameter, low temperature coefficient (~20 ppm/°C)
- Wheatstone bridge: two fixed arms (100.0 Ω each, ±0.01%), one variable arm (decade resistance box or potentiometer for setpoint), and the RTD
- [Galvanometer or zero-center millivoltmeter](./electrical-instruments.md) (±50 mV range)
- [Relay driver circuit](../electronics/power-electronics.md): amplifier + relay or [SSR](../electronics/power-electronics.md)
- [Ceramic bobbin for winding RTD element](../ceramics/electronic-ceramics.md) (alumina, 5 mm diameter, 30 mm long)

**Construction**:

1. **Wind the RTD element** (if not using a commercial element): Wind platinum wire (0.05 mm diameter) in a bifilar pattern (folded back on itself to cancel inductance) onto the ceramic bobbin. The bifilar winding is essential for AC bridge measurements. Calculate the wire length needed: Pt100 at 0°C requires resistance of exactly 100.0 Ω. Platinum wire at 0.05 mm diameter has resistance of approximately 3.8 Ω/m, so you need about 26 m of wire. Wind this onto the bobbin, taking care not to kink or stretch the wire (platinum work-hardens and its resistance changes with strain). The wire must be wound loosely enough that it can expand and contract freely with temperature, without binding on the bobbin.

2. **Trim to exact value**: Measure the resistance at 0°C (ice bath). Carefully unwind wire until the resistance is exactly 100.0 Ω. This is fussy work with 0.05 mm wire. Each cm of wire removed changes the resistance by about 0.04 Ω (0.1°C). Patience pays off.

3. **Seal the element**: Coat the wound bobbin with a thin layer of alumina cement or enclose it in a stainless steel sheath (6 mm OD, 50-100 mm long) packed with alumina powder for thermal contact and electrical insulation. The sheath protects the delicate platinum wire from mechanical damage and contamination.

4. **Build the Wheatstone bridge**: Construct three bridge arms using manganin wire resistors. Manganin (84% Cu, 12% Mn, 4% Ni) has a near-zero temperature coefficient, so the bridge resistors do not drift with ambient temperature changes. Wind the resistors bifilar on ceramic bobbins. Two arms should be exactly 100.0 Ω. The third arm is the setpoint: a decade resistance box or a calibrated potentiometer that allows the operator to dial in the desired resistance (and thus the desired temperature).

5. **Wire the bridge**: Connect the RTD to the bridge using a four-wire (Kelvin) connection. In a four-wire setup, two wires carry the excitation current and two wires sense the voltage across the RTD. This eliminates the resistance of the lead wires from the measurement. With 3 m of copper lead wire (0.5 mm diameter), the lead resistance is about 0.6 Ω, which would cause a 1.5°C error in a two-wire measurement. Four-wire eliminates this error entirely.

6. **Add the detector and relay**: Connect a galvanometer or instrumentation amplifier across the bridge output (the two midpoints). When the RTD resistance matches the setpoint resistance, the bridge is balanced and the output is zero. When temperature deviates, the bridge output is proportional to the temperature error. Amplify this signal and drive a relay or SSR.

**Calibration**:

1. Immerse the RTD in an ice-water bath (0°C). Adjust the bridge setpoint to 100.0 Ω. The bridge should balance (zero output). If not, trim the bridge resistors.
2. Transfer to a steam bath (100°C). The RTD should read 138.5 Ω. Set the bridge setpoint to 138.5 Ω and verify that the bridge balances at 100°C.
3. Check at intermediate points (37°C body temperature = 114.2 Ω). Linearity should be excellent: the Callendar-Van Dusen equation for platinum deviates less than 0.1°C from linearity over 0-200°C.
4. For thermostat operation, set the bridge setpoint to the resistance corresponding to the desired trip temperature. Use the formula: R(T) = 100 × (1 + 0.00385 × T), where T is in °C. For example, 200°C corresponds to 177.0 Ω.

**Expected accuracy**: ±0.1-1°C over -200 to 850°C. RTDs are among the most stable and accurate temperature sensors available. Platinum is chemically inert and the resistance-temperature relationship is extremely stable over time and thermal cycling.

**Applications**: Precision furnace control, semiconductor processing (crystal growth, diffusion, oxidation furnaces), calibration laboratory temperature standards, food processing temperature monitoring, pharmaceutical process temperature validation. The RTD thermostat is the choice when you need better than ±1°C accuracy and have electronic measurement capability.

**Strengths**:
- Highest accuracy and long-term stability of any contact temperature sensor
- Nearly linear resistance-temperature relationship simplifies circuit design
- Wide range (-200 to 850°C) with excellent interchangeability (Pt100 standard)
- Platinum is chemically inert; no contamination or drift from oxidation
- Well-characterized physics; Callendar-Van Dusen equation gives precise modeling

**Weaknesses**:
- Requires electronic measurement circuitry (bridge, amplifier)
- Platinum is expensive and rare
- Fragile fine wire (0.05 mm) requires careful handling during winding
- Slow response when sheathed for protection
- Lead resistance errors require four-wire measurement for accuracy

## Reed Switch Thermostat

**Principle**: A permanent magnet is mounted on a bimetallic element. As temperature changes, the bimetallic element bends, moving the magnet relative to a sealed glass reed switch. The reed switch contains two ferromagnetic reed blades hermetically sealed in an inert gas atmosphere. When the magnet approaches, the magnetic field magnetizes the reed blades, causing them to attract each other and snap together, closing the circuit. When the magnet moves away, the field weakens and the reeds spring apart. The reed switch provides contactless switching: the magnet never touches the switch, and the contacts are sealed inside a glass envelope, immune to dust, oxidation, and corrosion.

**Prerequisites**:
- [Rolling mill](../machine-tools/forming.md) for producing thin bimetallic strips
- Two metals with different expansion coefficients ([brass](../metals/bronze.md) + [steel](../metals/iron-steel.md))
- [Bonding method](../machine-tools/joining.md) for bimetallic strip (riveting, brazing)
- [Spring tempering](../metals/iron-steel.md) capability
- [Permanent magnet](../metals/non-ferrous.md) (ferrite or alnico)
- Sealed reed switch (glass envelope, normally open contacts)

**Materials**:
- [Bimetallic strip](../metals/alloys.md) (steel/brass, 0.3 mm thick, 8 mm wide, 60 mm long)
- [Permanent magnet](../metals/non-ferrous.md): ferrite bar (5 × 5 × 10 mm) or [alnico disc](../metals/alloys.md) (6 mm diameter, 3 mm thick)
- [Reed switch](../electronics/passive-components.md): glass envelope (45 mm long, 5 mm diameter), normally open contacts rated for 0.5-1 A
- [Mounting bracket](../metals/iron-steel.md) (aluminum or plastic)
- [Adjustment screw](../machine-tools/machining.md) (M3) with locknut

**Construction**:

1. **Mount the magnet on the bimetallic strip**: Epoxy or braze the permanent magnet to the free end of the bimetallic strip. The magnet's orientation matters: the magnetic field must be parallel to the reed switch axis (longitudinal to the reed blades) for maximum sensitivity. A magnet oriented perpendicular to the reeds requires closer approach to actuate.

2. **Mount the reed switch**: Fix the reed switch in a stationary position on the mounting bracket, parallel to the bimetallic strip, with the reed blade gap positioned at the point where the magnet will pass. The gap between the magnet and the reed switch at the actuation temperature should be about 2-5 mm, depending on magnet strength.

3. **Calculate the geometry**: The bimetallic strip deflects approximately D = K × (L²/t) × ΔT. For a 60 mm long, 0.6 mm thick steel-brass strip, K ≈ 14 × 10⁻⁶/°C. At ΔT = 20°C, deflection D ≈ 14 × 10⁻⁶ × (60²/0.6) × 20 = 1.7 mm. The magnet must move about 2-3 mm relative to the reed switch to transition from "on" to "off." This requires a strip long enough to produce that deflection over the desired temperature range.

4. **Set the trip point**: Mount an adjustment screw that moves the reed switch position relative to the strip. Turning the screw shifts the switch closer to or farther from the magnet, changing the temperature at which the magnetic field is strong enough to close the reeds.

5. **Wire the circuit**: Connect the reed switch leads in series with the heater circuit (through a relay if the heater draws more than the reed switch's rated current, typically 0.5-1 A). The reed switch carries only the relay coil current, not the full heater load.

**Calibration**:

1. Place in a temperature-controlled environment with a [reference thermometer](./temperature-pressure.md). Adjust the screw until the reed switch just closes at the desired trip temperature (detect with ohmmeter).
2. Heat and cool through the trip point 5-10 times to verify consistency. The reed switch should trip at the same temperature within ±1°C each cycle.
3. Check the deadband: the temperature difference between switch closing (on heating) and switch opening (on cooling). Reed switches with magnets have a hysteresis of about 1-2°C due to the magnetic latching effect (the reeds close at a certain field strength but don't release until the field drops below a lower threshold).

**Expected accuracy**: ±1-2°C over -40 to 120°C range. Limited by the bimetallic element and the magnet-reed hysteresis.

**Applications**: Low-voltage thermostat switching (battery-powered systems), intrinsically safe circuits (no spark outside the sealed glass envelope), protective thermostat for electronics, electric blanket control, refrigerator thermostat replacement. The reed switch thermostat is ideal for environments where contact sparking is a concern (flammable gas atmospheres, though not explosion-proof rated).

**Strengths**:
- Sealed glass envelope protects contacts from dust, oxidation, and corrosion
- No electrical power required at the sensor
- Contactless actuation via magnet; no mechanical wear on the switch
- Spark-free switching suitable for hazardous atmospheres
- Simple construction with few components

**Weaknesses**:
- Very limited current rating (0.5-1 A); must drive a relay for larger loads
- Magnetic hysteresis adds 1-2°C deadband
- Sensitive to external magnetic fields that can cause false triggering
- Limited temperature range (-40 to 120°C) set by magnet and bimetallic properties
- Not proportional; on/off switching only

## Scaling Notes

Electrical thermostat technologies scale from individual sensor fabrication to automated production:

- **Thermocouple production**: Wire drawing of thermocouple alloys (Chromel, Alumel, Constantan, Iron) from cast ingots. Junction welding by capacitance-discharge or TIG. Sheathing in stainless steel or Inconel tubes with MgO insulation. Pilot scale: 10-50 junctions/day by hand. Production scale: 500-2000/day with automated welding and sheathing.

- **RTD production**: Platinum wire winding (0.05 mm) onto ceramic or glass mandrels. Requires clean-room conditions for precision grades. Hand-wound RTDs achieve ±0.1°C at calibration points. Machine-wound production RTDs achieve ±0.3°C. The platinum wire cost dominates — a Pt100 element uses 0.05 mm wire worth ~$2-5 in raw platinum.

- **Reed switch production**: Glass-encapsulated magnetic reed switches require glass-to-metal sealing in inert gas atmosphere. The ferromagnetic reed contacts must be plated with rhodium or ruthenium for reliable switching. Production scale: 10,000+ switches/day with automated sealing equipment.

## Quality Control

1. **Thermocouple verification**: Check each junction by immersing in ice-water slurry (0.0°C reference) and boiling water (100.0°C at sea level). Output must be within ±1.0°C of standard tables for the thermocouple type. Verify that both wires are the correct alloy by measuring the magnetic response (Alumel is magnetic, Chromel is not for Type K).

2. **RTD calibration**: Measure resistance at 0°C (100.00 Ω for Pt100, 1000.0 Ω for Pt1000) and 100°C (138.51 Ω for Pt100). The ratio R(100)/R(0) must equal 1.3851 ± 0.001 for Class B, ± 0.0003 for Class A. Any deviation indicates platinum purity problems or wire strain.

3. **Reed switch testing**: Verify pull-in temperature by slowly heating in a controlled bath. Contact resistance must be below 100 mΩ when closed. Open-circuit resistance must exceed 10 MΩ when open. Cycle the switch 1000 times and verify trip temperature has not drifted more than ±1°C.

## Variations and Alternatives

| Thermostat Type | Temp Range | Accuracy | Response Time | Best For |
|----------------|-----------|----------|---------------|----------|
| Type K thermocouple | -200 to +1300°C | ±1-2°C | 0.1-1 second | General industrial, furnaces, engines |
| Type J thermocouple | -40 to +750°C | ±1-2°C | 0.1-1 second | Lower cost, reducing atmospheres |
| Type T thermocouple | -200 to +350°C | ±0.5-1°C | 0.1-1 second | Cryogenic, food processing |
| Pt100 RTD (Class A) | -200 to +650°C | ±0.15-0.35°C | 1-10 seconds | Precision industrial, pharmaceuticals |
| Pt1000 RTD | -200 to +650°C | ±0.3-0.6°C | 1-10 seconds | HVAC, 2-wire applications (higher base resistance) |
| Reed switch thermostat | -40 to +150°C | ±1-3°C | 0.5-2 seconds | Simple on/off, HVAC, appliances |
| Bimetallic strip | -50 to +400°C | ±2-5°C | 5-30 seconds | Safety cutoffs, simple control |

## See Also

- **[Thermostats Overview](thermostat.md)**: Parent overview of all thermostat types
- **[Mechanical Thermostats](thermostat-mechanical.md)**: Bimetallic and rod-and-tube types
- **[Electronic Thermostats](thermostat-electronic.md)**: Thermistor and IC based
- **[Advanced Thermostats](thermostat-advanced.md)**: SMA, quartz, and IR types

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Thermocouple reads incorrectly at room temperature | Cold junction compensation not working | Check that the cold junction sensor (thermistor or RTD) is securely mounted at the terminal block; verify compensation circuit adds the correct offset voltage; test by shorting the thermocouple terminals (meter should read ambient temperature) |
| Thermocouple reading drifts at high temperature | Junction degradation or wire contamination | Inspect the junction weld for cracks or oxidation; Type K thermocouples suffer "green rot" above 800°C in reducing atmospheres (chromel oxidizes selectively); replace with Type S (platinum-rhodium) for high-temperature or reducing environments |
| RTD bridge won't balance at 0°C | Bridge resistor tolerance too loose or lead resistance uncompensated | Verify all bridge resistors are within ±0.01% of 100.0 Ω; switch to four-wire (Kelvin) connection to eliminate lead resistance (3 m of 0.5 mm copper wire adds 0.6 Ω, causing 1.5°C error in two-wire mode) |
| RTD reading jumps or is noisy | Loose connection or electromagnetic interference | Check all solder joints and terminal screws; route RTD leads in twisted pairs away from power cables; add a 0.1 μF capacitor across the bridge output to filter high-frequency noise |
| Reed switch chatters (rapid on/off cycling) | Hysteresis too narrow or vibration in the mechanism | Increase the gap between magnet and reed switch by 0.5-1 mm to widen the deadband; add a dashpot (silicone oil damper) to the bimetallic strip to damp oscillations; verify the reed switch is rigidly mounted (not vibrating on its leads) |
| Reed switch does not actuate at setpoint | Magnet too far from reed or bimetallic strip fatigued | Reduce the magnet-to-switch gap to 2-3 mm; verify the magnet is oriented with its field parallel to the reed blade axis; check that the bimetallic strip hasn't work-hardened and lost its deflection range (replace strips after ~100,000 cycles) |
| Thermocouple output signal too low | Wire gauge too thin or junction resistance too high | Use thicker thermocouple wire (0.8-1.0 mm instead of 0.3-0.5 mm) for runs longer than 3 m; check for corrosion at terminal blocks (green patina on chromel indicates oxidation — clean with abrasive paper) |
| Galvanometer relay sticks at trip point | Contact pitting or mechanical friction | Clean relay contacts with contact cleaner and a burnishing tool; check the pivots for dried lubricant and clean with solvent; verify the return spring provides adequate restoring force |
| RTD resistance reads incorrectly | Wire strain from bending or kinking during installation | Platinum wire in RTDs work-hardens when deformed; any kink permanently changes resistance. Handle RTD probes gently; never bend the sheath sharper than 5× its diameter. Replace damaged probes |

## Safety & Hazards

- **Thermocouple wire fumes**: Heating thermocouple wires during welding or brazing can produce metal oxide fumes. Chromel (nickel-chromium alloy) produces chromium VI compounds when heated above 600°C in oxidizing atmospheres. Chromium VI is a confirmed carcinogen. Weld thermocouple junctions in a well-ventilated area or under local exhaust. Use a capacitance-discharge welder (brief spark, minimal fume) rather than a gas torch when possible.
- **RTD platinum wire hazard**: The 0.05 mm platinum wire used in hand-wound RTD elements is thin enough to cut skin and can cause eye injury if it snaps during winding. Wear safety glasses during RTD construction. The fine wire is also a strangulation hazard if long lengths are used loosely on the bench.
- **Electrical hazards**: Electronic comparator circuits operate from mains-derived power supplies. All thermostat circuits that switch mains-powered heaters must include proper fusing, grounding, and isolation. A relay contact failure (welded contacts) leaves the heater permanently on, which can cause fires. Always include an independent high-limit cutoff (bimetallic strip thermostat wired in series with the heater) as a backup.
- **Mercury in thermometers**: Calibration using mercury-in-glass thermometers carries mercury exposure risk if the thermometer breaks. Mercury vapor at 20°C exceeds safe workplace limits in unventilated spaces after a spill. Clean any mercury spill with zinc dust or a commercial mercury absorbent. Never vacuum mercury.
- **RFI/EMI from relay switching**: Relay contacts switching inductive loads (heater coils, solenoid valves) produce electromagnetic interference that can disrupt nearby electronic equipment. Add snubber circuits (RC network: 0.1 μF + 100 Ω in series) across relay contacts driving inductive loads. Use solid-state relays (SSRs) for zero-crossing switching when interference is a concern.

---

*Part of [Thermostats & Temperature Control](./thermostat.md) • [Measurement](./index.md) • [All Domains](../../index.md)*
