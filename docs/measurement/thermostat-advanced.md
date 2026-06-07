# Advanced & Specialty Thermostats

> **Node ID**: measurement.thermostat-advanced
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`measurement.thermostat-electronic`](./thermostat-electronic.md), [`silicon.basic-devices`](../silicon/basic-devices.md), [`optics.inspection`](../optics/inspection.md)
> **Enables**: Semiconductor process monitoring, calibration-grade temperature measurement
> **Critical**: No — these are refinements for specialized applications
> **Timeline**: Years 40-60+
> **Outputs**: non_contact_temperature_sensing, calibration_grade_measurement, shape_memory_actuation


Advanced thermostats cover three specialized niches: shape memory alloy actuators for compact, high-force thermal switching; quartz crystal sensors for calibration-grade precision; and infrared pyrometers for non-contact temperature measurement at extreme temperatures. These types are not needed for general-purpose temperature control but become essential at the frontier of semiconductor manufacturing and high-temperature process control.


## Shape Memory Alloy (SMA) Thermostat

**Principle**: Certain alloys, most notably nickel-titanium (NiTi, also called Nitinol), undergo a reversible crystal-structure phase transition at a specific temperature. Below the transition, the alloy is in a martensitic phase (soft, easily deformed). Above the transition, it transforms to an austenitic phase (stiff, returns to a "trained" shape). If the alloy is deformed while cold and then heated through the transition temperature, it snaps back to its trained shape with substantial force (up to 500 MPa stress recovery). This provides a compact, powerful thermal actuator with no springs, no bellows, no fluid.

**Prerequisites**:
- [Nickel and titanium smelting](../metals/non-ferrous.md)
- [Precision alloy heat-treatment](../metals/alloys.md) (training the shape memory)
- [Arc melting or induction melting](../metals/refractory-metals.md) for alloy production

**Materials**:
- [NiTi wire](../metals/alloys.md) (55.8-56.0 wt% Ni, balance Ti): 0.5-1.0 mm diameter, 50-100 mm length
- Alternatively, [NiTi sheet](../metals/alloys.md) (0.2-0.5 mm thick) stamped into spring shapes
- [Bias spring](../metals/iron-steel.md) (steel, to deform the SMA when cold)
- [Electrical connections](../electronics/assembly.md) for resistive heating (if self-heated)

**Construction**:

1. **Obtain the alloy**: Melt nickel and titanium together in an arc furnace under argon atmosphere (titanium oxidizes rapidly in air at melting temperature). The composition must be controlled to within ±0.1 wt% nickel. A 56.0 wt% Ni alloy has an austenite finish temperature (Af) of about 60°C. Increasing nickel content by 0.1% lowers Af by about 10°C. This sensitivity makes precise composition control essential.

2. **Train the shape memory**: Heat the NiTi wire to 500°C (in the austenitic phase) and hold for 5 minutes. While hot, form it into the desired hot-state shape (typically straight, or a tightly coiled spring). Cool to room temperature. The wire "remembers" this shape. Now deform it to the cold-state shape (bend it, stretch it, compress it) using the bias spring. When heated above the transition temperature, it will recover the trained shape.

3. **Assemble the actuator**: Connect the NiTi wire in tension between a fixed anchor and a moving element (valve stem, switch lever). Install a steel bias spring that pulls the wire into the deformed (cold) state. When heated (either by ambient temperature or by passing electrical current through the wire), the wire contracts with force, overcoming the bias spring and moving the actuator. When cooled, the bias spring stretches the wire back to the cold position.

4. **Wire for self-heating (optional)**: If the SMA actuator is to be electrically heated (rather than responding to ambient temperature), connect electrical leads to both ends of the wire. Current through the wire causes resistive heating (NiTi resistivity is about 80 μΩ·cm). For a 100 mm length of 0.5 mm diameter wire, resistance is about 4 Ω. At 2V, this draws 0.5A (1W), sufficient to heat the wire above its transition temperature in a few seconds.

**Calibration**:

1. The transition temperature is fixed by the alloy composition. You cannot adjust it after manufacture (unlike a bimetallic strip where you can change the setpoint screw). Calibrate by immersion in a temperature bath with a [reference thermometer](./temperature-pressure.md) and measuring the actuation temperature.
2. The actuator has hysteresis: the martensite-to-austenite transition occurs at a higher temperature than the reverse. Typical hysteresis is 20-40°C. This means the actuator might snap to its hot shape at 60°C but not return to cold shape until it cools to 30-40°C. This limits the thermostat to applications where wide hysteresis is acceptable.
3. For resistive heating, calibrate the current needed to reach the transition temperature. Apply increasing current until the actuator snaps. Record the current value. This is the drive current.

**Expected accuracy**: ±1-2°C at a fixed transition temperature (determined by alloy composition). Range: -100 to 100°C, adjustable by alloy composition (NiTi transition temperature can be tuned from about -50°C to 110°C by adjusting Ni/Ti ratio and adding ternary elements like copper).

**Applications**: Automatic greenhouse vent openers, fire sprinkler actuators, automotive transmission thermal valves, medical devices (stents that deploy at body temperature), micro-actuators for robotics. SMA thermostats are niche but valuable where compact, high-force thermal actuation is needed without any external power (ambient-temperature-actuated types).

**Strengths**:
- Extremely compact actuator for the force it produces (up to 500 MPa)
- No springs, bellows, or fluids needed; the alloy itself is the actuator
- Ambient-heated versions require no external power at all
- Silent operation; no mechanical clicking or switching noise
- Can be electrically heated for active control when desired

**Weaknesses**:
- Transition temperature is fixed by alloy composition; not adjustable after manufacture
- Very wide hysteresis (20-40°C) limits precision and applicability
- Fatigue and drift after many thousands of thermal cycles
- Expensive alloy requiring precise composition control during melting
- Slow response compared to electronic switching (seconds to actuate)


## Quartz Crystal Temperature Sensor Thermostat

**Principle**: A quartz crystal cut at a specific orientation (typically Y-cut or LC-cut) has a resonant frequency that changes linearly with temperature, at about 1000 ppm/°C (1 kHz per MHz of resonant frequency per °C). A 10 MHz crystal shifts by 10 kHz per °C. A frequency counter measures the resonant frequency with high precision (1 Hz resolution is routine), giving a temperature resolution of 0.001°C for a 10 MHz crystal. The frequency-temperature relationship is exceptionally stable and reproducible, limited only by the crystal's aging rate (a few ppm per year).

**Prerequisites**:
- [Quartz crystal oscillator manufacturing](../silicon/basic-devices.md) (crystal cutting, electrode deposition)
- [Frequency counter electronics](./electrical-instruments.md) (or microcontroller with counter input)
- [Temperature-stable oscillator reference](../electronics/semiconductor-devices.md)
- [Digital electronics](../computing/digital-logic.md) for frequency-to-temperature conversion

**Materials**:
- [Temperature-sensing quartz crystal](../silicon/basic-devices.md): Y-cut, 10 MHz nominal frequency
- [Oscillator circuit](../electronics/semiconductor-devices.md): Pierce or Colpitts oscillator built around the crystal
- [Frequency counter](./electrical-instruments.md): microcontroller counter input or dedicated counter IC
- [Reference oscillator](../silicon/basic-devices.md): standard AT-cut quartz crystal (temperature-stable, ±10 ppm over 0-60°C) for the frequency counter clock
- [Microcontroller](../computing/embedded-systems.md) for frequency-to-temperature conversion and thermostat logic
- [SSR](../electronics/power-electronics.md) for heater control

**Construction**:

1. **Select the crystal**: A Y-cut quartz crystal has a nearly linear frequency-temperature coefficient of about +90 ppm/°C. An LC-cut (linear coefficient) crystal is specifically designed for temperature measurement and provides better linearity (frequency deviates less than ±0.1°C from linear over -50 to 150°C). The crystal is packaged in a metal can (HC-49 or similar) with two pins.

2. **Build the oscillator**: Construct a Pierce oscillator circuit around the temperature-sensing crystal. The circuit consists of the crystal, two capacitors (15-33 pF), a feedback resistor (1-10 MΩ), and an inverting amplifier (74HC04 hex inverter, one section). The oscillator produces a square wave at the crystal's resonant frequency. Keep component values stable: use NPO/COG ceramic capacitors (temperature coefficient ±30 ppm/°C) or silver mica capacitors.

3. **Count the frequency**: Feed the oscillator output to a microcontroller counter input. Count the number of oscillations in a 1-second gate time (gated by the reference oscillator). A 10 MHz crystal at 25°C might produce 10,000,000 Hz. At 26°C, it produces 10,000,000 × (1 + 90 × 10⁻⁶) = 10,000,900 Hz. The 900 Hz difference is easily measured with a 1-second gate time. Longer gate times (10 seconds) give 10× better resolution.

4. **Convert frequency to temperature**: The microcontroller computes temperature from frequency using a calibration formula. For an LC-cut crystal with linear coefficient: T = (f_measured - f_0) / (f_0 × k), where f_0 is the frequency at 0°C and k is the temperature coefficient (about 90 × 10⁻⁶/°C). For better accuracy, use a 3rd-order polynomial fit from calibration data.

5. **Implement thermostat logic**: Compare the computed temperature to the setpoint. Drive the SSR with proportional control: compute the temperature error (setpoint minus measurement), multiply by a gain factor to get heater power percentage, and set the SSR PWM duty cycle accordingly. For tighter control, implement a full PID algorithm: compute proportional (current error), integral (accumulated error over time), and derivative (rate of error change) terms, combine them with tuning constants, and output the result as heater power percentage. The microcontroller updates the output every 500 ms to 1 second, adjusting the PWM duty cycle sent to the SSR.

**Calibration**:

1. Immerse the crystal sensor in a temperature-stable bath (ice-water, body temperature, boiling water) with a [reference thermometer](./temperature-pressure.md). Measure the frequency at each point.
2. Fit a polynomial: f(T) = f₀ × (1 + k₁T + k₂T² + k₃T³). The coefficients k₁, k₂, k₃ are determined by the crystal cut and are stable over the crystal's lifetime. For an LC-cut crystal, k₁ ≈ 35 × 10⁻⁶/°C, k₂ is small, k₃ is negligible.
3. Store the calibration coefficients in the microcontroller's EEPROM.
4. Verify at intermediate temperatures. Residual error should be less than ±0.05°C over the calibrated range.

**Expected accuracy**: ±0.01-0.05°C over -50 to 250°C range. Resolution limited only by frequency counter gate time and reference oscillator stability. With a 10-second gate time and a stable reference oscillator, resolution of 0.001°C is achievable.

**Applications**: High-precision temperature measurement and control, calibration of other temperature sensors, meteorological reference instruments, semiconductor process monitoring where ultra-stable temperature measurement is needed. The quartz crystal thermostat is overkill for most applications but provides the best combination of accuracy, stability, and resolution available in a reasonably simple electronic sensor.

**Strengths**:
- Best resolution of any practical temperature sensor (0.001°C achievable)
- Exceptional long-term stability (a few ppm per year aging)
- Digital output (frequency) inherently immune to analog noise
- Frequency-temperature relationship is stable and reproducible
- Suitable for calibration of other temperature sensors

**Weaknesses**:
- Complex electronics required (oscillator, frequency counter, microcontroller)
- Expensive specialized crystal (Y-cut or LC-cut, not the common AT-cut)
- Limited range compared to thermocouples (-50 to 250°C)
- Slow thermal response due to metal can packaging
- Overkill for most applications; hard to justify the cost and complexity


## Infrared/Radiation Pyrometer Thermostat

**Principle**: Every object above absolute zero emits thermal radiation described by Planck's law. The total radiated power and its spectral distribution depend on the object's temperature and emissivity. An infrared pyrometer collects this radiation (through optics: lens, mirror, or fiber optic), focuses it onto a detector (thermopile, pyroelectric sensor, or photodiode), and converts the detector signal to a temperature reading. Because the sensor measures radiation without physical contact, it can regulate the temperature of moving objects, molten metals, semiconductor wafers in vacuum, and any target that cannot be touched by a probe.

**Prerequisites**:
- [Optical components](../optics/inspection.md) (lenses, mirrors, windows transparent to IR radiation)
- [IR detector fabrication](../electronics/semiconductor-devices.md) (thermopile, pyroelectric, or photon detector)
- [Amplifier and signal conditioning electronics](../electronics/semiconductor-devices.md)
- [Calibration](./precision-metrology.md) against known-temperature blackbody sources
- [Microcontroller](../computing/embedded-systems.md) for temperature computation and PID control

**Materials**:
- IR optics: [germanium lens](../optics/inspection.md) (for 2-14 μm band), [calcium fluoride window](../optics/inspection.md), or [gold-coated mirror](../optics/optical-coatings.md)
- Detector:
  - [Thermopile](../electronics/semiconductor-devices.md) (multiple thermocouple junctions on a silicon chip, output ~50 μV/°C of target temperature)
  - [Pyroelectric sensor](../ceramics/advanced-ceramics.md) (lithium tantalate crystal, generates charge proportional to rate of temperature change)
  - [InGaAs photodiode](../silicon/basic-devices.md) (for 1-2.5 μm band, high-temperature targets)
- [Amplifier](../electronics/semiconductor-devices.md): low-noise op-amp (OP27, AD745) with gain 1000-10000
- [Microcontroller](../computing/embedded-systems.md) with ADC
- [Emissivity adjustment](../electronics/passive-components.md): potentiometer or software setting

**Construction**:

1. **Build the optics**: For a single-wavelength (spectral) pyrometer, use a germanium lens (25 mm diameter, 50 mm focal length, AR-coated for 8-14 μm) to focus IR radiation from the target onto the detector. The lens must be made of a material transparent at the measurement wavelength (glass is opaque in the thermal IR). Germanium, zinc selenide, and calcium fluoride are common IR lens materials. For a simpler design, use a reflective objective (gold-coated concave mirror) which avoids chromatic aberration and works over any wavelength.

2. **Mount the detector**: Position the detector element at the focal point of the optics. For a thermopile detector, the active area is typically 1-2 mm diameter. The detector must see only the target (no stray radiation from the housing). Use a baffled tube (inner surface painted matte black) between the lens and detector to block stray light.

3. **Build the amplifier**: The thermopile output is tiny (50-500 μV for typical temperature ranges). Amplify with a precision instrumentation amplifier (gain 1000-10000, input offset < 1 μV). Use a low-pass filter (0.1-1 Hz cutoff) to reject 50/60 Hz power-line interference and high-frequency noise. Shield the amplifier and detector connections in a metal enclosure to reduce electromagnetic pickup.

4. **Add the reference junction**: The thermopile measures the difference between the target temperature and the detector temperature. You must measure the detector's own temperature independently (with a thermistor or RTD mounted on the thermopile package) and add it to the differential reading to get absolute target temperature.

5. **Compute temperature from radiation**: The total radiated power per unit area is given by the Stefan-Boltzmann law: P = ε × σ × T⁴, where ε is emissivity (0-1), σ is the Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²/K⁴), and T is absolute temperature. The detector voltage is proportional to the received power, which is proportional to the target's T⁴ (minus the detector's T⁴). The microcontroller computes: T_target = ((V_detector / (ε × k)) + T_detector⁴)^(1/4), where k is a calibration constant.

6. **Handle emissivity**: The emissivity ε varies with material and surface condition. Polished metals have ε = 0.05-0.2 (poor emitters, difficult to measure with IR). Oxidized metals and most non-metals have ε = 0.8-0.95 (good emitters). The operator must set the correct emissivity value in the pyrometer. Error from wrong emissivity setting: a 10% error in ε causes about 2.5% error in measured temperature (at typical process temperatures, this is 10-30°C). A two-color (ratio) pyrometer avoids this problem by measuring the ratio of radiation at two wavelengths; the ratio is emissivity-independent.

7. **Implement PID control**: Feed the computed temperature to a PID algorithm running on the microcontroller. Compute the proportional term (gain times current error), the integral term (accumulated error over time), and the derivative term (rate of error change). Combine all three with tuning constants to produce a heater power output from 0 to 100%. Drive the SSR with PWM at the computed duty cycle. Update the control loop every 500 ms to 1 second, reading the detector, computing temperature, and adjusting heater power.

**Calibration**:

1. **Blackbody calibration**: Point the pyrometer at a blackbody calibration source (a cavity with ε ≈ 0.999, heated to a known temperature by a calibrated RTD). Measure the pyrometer output at 5-6 temperatures across the range.
2. Fit a calibration curve: plot detector voltage vs. T⁴ (Stefan-Boltzmann). The relationship should be linear for a thermopile detector. The slope gives the calibration constant k; the intercept gives the detector self-radiation offset.
3. **Emissivity verification**: Measure a known-temperature object with known emissivity (e.g., a painted steel plate at 200°C, ε ≈ 0.95) to verify that the emissivity compensation works correctly.
4. For a two-color pyrometer: calibrate at two or more temperatures using the blackbody source. The ratio of the two detector channels should be independent of emissivity.

**Expected accuracy**: ±0.5-2% of reading (in Kelvin) over 0 to 3000°C+. A 2% error at 1000°C (1273 K) is about 25°C. At 200°C (473 K), it is about 9°C. Better accuracy requires careful calibration and correct emissivity setting. Two-color pyrometers achieve ±0.5% with emissivity independence.

**Applications**: Steel and glass melting furnace control, semiconductor wafer temperature measurement during rapid thermal processing, kiln and furnace regulation where contact sensors cannot survive, moving web temperature monitoring (paper, plastic film, steel strip), engine turbine blade temperature measurement. The IR pyrometer thermostat is essential for any application where the target cannot be contacted, is moving, is too hot for contact sensors, or is in a vacuum chamber where a probe would contaminate the process.

**Strengths**:
- Non-contact sensing; measures temperature without touching the target
- Very high temperature capability (0 to 3000°C+)
- Can measure moving objects, molten metals, and targets in vacuum chambers
- Fast response limited only by detector and electronics speed
- No probe contamination or degradation in harsh environments

**Weaknesses**:
- Accuracy depends heavily on correct emissivity setting
- Expensive IR-transparent optics (germanium, zinc selenide)
- Requires clear line of sight to the target
- Struggles with polished metals (low emissivity, weak signal)
- Needs blackbody calibration source for reliable accuracy


## Scaling Notes

Advanced thermostat technologies scale with the underlying materials science capability:

- **SMA thermostats**: NiTi (Nitinol) requires melting nickel and titanium together at 1300°C in an inert atmosphere. Titanium powder is pyrophoric. Nickel is a skin sensitizer and suspected carcinogen. SMA thermostats are best suited for niche applications where their unique properties (silent operation, high force output) justify the material cost and processing complexity.

- **Quartz crystal thermostats**: Require synthetic quartz crystal production (hydrothermal growth at 350-400°C, 100-200 MPa in NaOH solution). This is a significant industrial capability. Once crystal production is established, frequency-based temperature sensing offers exceptional resolution (0.001°C) and long-term stability.

- **IR pyrometers**: Optical components (germanium lenses, zinc selenide windows) require specialized optical material production. Calibration requires blackbody sources traceable to fixed-point temperature standards (zinc freezing point 419.527°C, gold freezing point 1064.18°C).

## Quality Control

Each advanced thermostat type requires specific calibration and verification:

1. **SMA thermostat calibration**: Cycle the SMA element through its transformation temperature 50-100 times to stabilize the hysteresis loop. Verify trip temperature with a calibrated thermocouple (±0.5°C). SMA elements drift by 1-2°C during the first 100 cycles, then stabilize.

2. **Quartz crystal verification**: Measure frequency vs. temperature against a calibrated reference. The frequency-temperature curve must match the theoretical AT-cut characteristic within ±5 ppm. Verify that the oscillator starts reliably at all temperatures in the operating range.

3. **IR pyrometer calibration**: Verify against a blackbody source at 3-5 temperatures spanning the operating range. Check emissivity setting accuracy by measuring a known-temperature target (e.g., boiling water at 100°C with emissivity set to 0.97 for water). Recheck calibration annually.

## Variations and Alternatives

| Thermostat Type | Temp Range | Accuracy | Response Time | Best For |
|----------------|-----------|----------|---------------|----------|
| SMA (Nitinol) | -20 to +110°C | ±2-5°C | 1-10 seconds | Silent switching, medical devices, compact actuators |
| Quartz crystal | -50 to +250°C | ±0.001-0.01°C | 0.1-1 second | Precision temperature measurement, laboratory standards |
| IR pyrometer | 0 to +3000°C | ±0.5-2% of reading | 1-100 ms | Non-contact measurement, hot metals, glass, kilns |
| Thermocouple (K type) | -200 to +1300°C | ±1-2°C | 0.1-1 second | General-purpose industrial temperature sensing |
| RTD (Pt100) | -200 to +850°C | ±0.1-0.5°C | 1-10 seconds | Precision industrial temperature measurement |
| Thermistor (NTC) | -50 to +300°C | ±0.1-0.2°C | 0.1-1 second | Medical, HVAC, consumer electronics |
| Bimetallic strip | -50 to +400°C | ±2-5°C | 5-30 seconds | Simple on/off control, safety cutoffs |

## See Also

- **[Thermostats Overview](thermostat.md)**: Parent overview of all thermostat types
- **[Mechanical Thermostats](thermostat-mechanical.md)**: Bimetallic and rod-and-tube types
- **[Electrical Thermostats](thermostat-electrical.md)**: Thermocouple and RTD based
- **[Electronic Thermostats](thermostat-electronic.md)**: Thermistor and IC based

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| SMA actuator does not return when cooled | Hysteresis too wide (20-40°C gap between heating and cooling transitions) or bias spring too weak | Increase the bias spring force to overcome the hysteresis and fully deform the cold-phase martensite. If the spring cannot provide enough force, use a shorter SMA wire (less force recovery) or a design with two antagonistic SMA actuators (one heats while the other cools) |
| SMA actuator drifts after hundreds of cycles | Fatigue — repeated phase transitions accumulate slip at grain boundaries, degrading the shape memory effect | Limit cycle life to the manufacturer's rated value (typically 10,000-100,000 cycles depending on strain amplitude). Reduce the imposed strain (how far the wire is stretched in the cold state) to below 4% for maximum cycle life. Replace the wire element when drift exceeds acceptable limits |
| Quartz crystal frequency reading unstable | Reference oscillator drifting or crystal not properly thermally coupled to the target | Verify the reference oscillator (AT-cut crystal) is stable to ±10 ppm over the operating temperature range. Ensure the sensing crystal (Y-cut or LC-cut) is in direct thermal contact with the measured medium — an air gap adds thermal lag. Shield the crystal from vibration (mechanical stress shifts the resonant frequency) |
| IR pyrometer reads too low on shiny metal | Wrong emissivity setting — polished metals have ε = 0.05-0.2, not the default 0.95 | Set the emissivity correctly for the target material and surface condition. Polished aluminum: ε ≈ 0.05. Oxidized aluminum: ε ≈ 0.2-0.4. Painted surface: ε ≈ 0.9-0.95. If the emissivity is unknown or variable, use a two-color (ratio) pyrometer which is emissivity-independent, or apply a small patch of high-emissivity paint (ε ≈ 0.95) to the target |
| IR pyrometer reading drifts with ambient temperature | Detector self-heating or reference junction not at the measured temperature | The thermopile detector measures the difference between target and detector temperatures. If the detector temperature drifts (from electronics heat or sunlight), the reading shifts. Ensure the detector housing is temperature-stabilized. Use the built-in reference sensor (thermistor or RTD on the detector package) and verify it reads the detector temperature correctly |
| Quartz crystal sensor reads temperature shifts when none occurred | Crystal aging or stress from mounting | New crystals age faster (frequency shifts of 5-10 ppm/year in the first year, declining to 1-3 ppm/year after). Pre-age crystals by baking at 125°C for 48 hours before use. Verify the crystal mounting does not apply stress — use compliant leads (not rigid solder joints directly to the crystal pins) |
| IR pyrometer sees reflections from hot objects nearby | Stray radiation from furnaces, lamps, or heaters entering the optics | Install a sighting tube (baffled, matte-black interior) between the pyrometer lens and the target to restrict the field of view. Verify the pyrometer sees only the target by checking its field of view diameter at the working distance (typically 1/30 to 1/50 of the distance) |

## Safety & Hazards

- **Laser safety (interferometer and pyrometer sources)**: HeNe lasers used in interferometer calibration and some IR pyrometer light sources are typically Class II (< 1 mW visible) or Class IIIa (< 5 mW). Direct beam exposure can cause retinal damage. Never look into the laser aperture. Use beam stops and enclose beam paths where possible. Label the work area with appropriate laser warning signs.
- **High-temperature targets**: IR pyrometers are often aimed at targets above 500°C. Surrounding equipment and fixtures near the target may also be hot enough to cause burns. Use thermal barriers and maintain safe distances. A blackbody calibration source at 1000°C radiates enough heat to ignite paper at 1 m distance.
- **IR-transparent optics hazards**: Germanium lenses and zinc selenide windows used in IR pyrometers are brittle and can shatter if dropped. Germanium is also a heavy metal with toxicity concerns if ingested or inhaled as dust. Handle optics with care, wear gloves, and do not grind or machine germanium without respiratory protection.
- **NiTi (Nitinol) alloy processing**: Melting nickel and titanium together requires temperatures above 1300°C in an inert atmosphere. Titanium powder is pyrophoric (ignites spontaneously in air). Nickel and its compounds are skin sensitizers and suspected carcinogens. Melt NiTi in sealed, argon-purged furnaces only. Do not grind or machine NiTi without dust collection and respiratory protection.
- **Blackbody calibration sources**: Operating at temperatures up to 1200°C, these sources present severe burn and fire hazards. Enclose the hot cavity in a heat-shielded housing. Allow adequate cooling time (2-4 hours for a 1200°C source) before opening or handling. Use infrared viewers or cameras, never direct visual observation, to check cavity conditions at high temperature.


---

*Part of [Thermostats & Temperature Control](./thermostat.md) • [Measurement](./index.md) • [All Domains](../index.md)*
