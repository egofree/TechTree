# Electronic Thermostats

> **Node ID**: measurement.thermostat-electronic
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`measurement.thermostat-electrical`](./thermostat-electrical.md), [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md), [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md)
> **Enables**: [`silicon.crystal-growth`](../silicon/cz-pulling.md), [`measurement.thermostat-advanced`](./thermostat-advanced.md)
> **Critical**: No — analog electronic control is not the only path to precise temperature regulation
> **Timeline**: Years 30-60
> **Outputs**: pid_control, proportional_control, digital_temperature_regulation


Electronic thermostats use semiconductor sensors (thermistors, silicon junctions, IC temperature sensors) and active circuitry (comparators, microcontrollers) to achieve precise temperature control. They culminate in the digital PID thermostat, which eliminates the steady-state offset, overshoot, and oscillation that plague all mechanical and simple on/off electronic designs. With a good sensor and well-tuned PID algorithm, temperature stability of ±0.01°C is achievable.


## Thermistor-Based Electronic Thermostat

**Principle**: A thermistor is a sintered metal-oxide ceramic (typically manganese, nickel, or cobalt oxides) whose electrical resistance changes dramatically with temperature. NTC (negative temperature coefficient) thermistors decrease in resistance by 3-6% per °C, roughly 10× the sensitivity of an RTD. A 10 kΩ NTC thermistor at 25°C drops to about 3.6 kΩ at 60°C. This large resistance change simplifies the electronics: a simple voltage divider (thermistor + fixed resistor) produces a voltage that changes significantly with temperature, directly compatible with a comparator input. No bridge circuit needed.

**Prerequisites**:
- [Metal oxide powder processing](../ceramics/electronic-ceramics.md) (MnO₂, NiO, Co₃O₄)
- [High-temperature sintering](../ceramics/kilns.md) (1200-1400°C kiln)
- [Comparator circuit](../electronics/semiconductor-devices.md) (op-amp, resistors, potentiometer)
- [Relay](../electronics/passive-components.md) or [triac](../electronics/power-electronics.md) for heater switching
- [Basic PCB assembly](../electronics/pcb-fabrication.md)

**Materials**:
- [Thermistor](../ceramics/electronic-ceramics.md): NTC disc or bead type, 10 kΩ at 25°C, ±1% tolerance (or hand-made, see below)
- [Fixed resistor](../electronics/passive-components.md): 10 kΩ, 1% metal film (for voltage divider)
- [Comparator](../electronics/semiconductor-devices.md): LM311 or LM393 (dual comparator)
- [Potentiometer](../electronics/passive-components.md): 10 kΩ linear taper (for setpoint adjustment)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts, or [triac](../electronics/power-electronics.md) (BT136 for AC loads)
- [Power supply](../electronics/electrical-systems.md): 5V or 12V DC regulated
- Thermistor fabrication materials (if not using commercial part):
  - [Manganese dioxide (MnO₂) powder](../chemistry/coatings.md)
  - [Nickel oxide (NiO) powder](../chemistry/coatings.md)
  - [Cobalt oxide (Co₃O₄) powder](../chemistry/coatings.md)
  - [Binder: polyvinyl alcohol (PVA) solution](../polymers/synthetic.md)
  - [Silver paste](../metals/precious-metals.md) (for electrodes)
  - [Kiln](../ceramics/kilns.md) capable of 1300°C

**Construction**:

1. **Fabricate the thermistor** (if commercial parts are unavailable): Mix MnO₂, NiO, and Co₃O₄ powders in the desired ratio (a common composition is 60% MnO₂, 30% NiO, 10% Co₃O₄ for a 10 kΩ NTC thermistor). Add PVA binder and press into discs (5 mm diameter, 2 mm thick) at 10 tons pressure. Dry at 120°C for 2 hours. Sinter at 1300°C for 4 hours in air, then cool at 5°C/minute. The sintering process fuses the oxide particles into a dense ceramic with semiconducting properties. Apply silver paste to both faces and fire at 800°C for 10 minutes to create electrical contacts. Solder lead wires to the silver electrodes. The resulting thermistor will have a nominal resistance that depends on the exact composition and sintering conditions. Measure and sort.

2. **Build the voltage divider**: Connect the thermistor in series with the fixed resistor between Vcc and ground. The junction between thermistor and resistor is the output. At 25°C, with a 10 kΩ thermistor and 10 kΩ fixed resistor, the output is Vcc/2 (2.5V with 5V supply). As temperature rises, the NTC thermistor resistance drops, and the output voltage rises (if thermistor is the lower element) or drops (if thermistor is the upper element). Choose the configuration that gives increasing voltage with increasing temperature for a heating thermostat.

3. **Build the comparator circuit**: Connect the voltage divider output to the non-inverting input of the comparator (LM311). Connect a potentiometer (voltage divider from Vcc to ground) to the inverting input. The potentiometer sets the threshold voltage (setpoint). When the thermistor voltage exceeds the setpoint, the comparator output goes high, driving the relay through a transistor driver.

4. **Add hysteresis**: Connect a high-value resistor (1-10 MΩ) from the comparator output back to the non-inverting input. This provides positive feedback that creates a small voltage hysteresis (0.5-2°C equivalent), preventing rapid on/off cycling when the temperature is near the setpoint. Without hysteresis, electrical noise or tiny temperature fluctuations cause the relay to chatter, which destroys relay contacts quickly.

5. **Wire the relay**: Connect the comparator output through a current-limiting resistor to the base of a switching transistor (2N2222 or similar). The transistor drives the relay coil. Add a flyback diode (1N4007) across the relay coil to protect the transistor from inductive voltage spikes when the relay opens.

**Calibration**:

1. Immerse the thermistor in a temperature bath with a [reference thermometer](./temperature-pressure.md).
2. Measure the voltage divider output at several temperatures. Record voltage vs. temperature.
3. Set the potentiometer to the voltage corresponding to the desired setpoint. Use the recorded data as a lookup.
4. Verify the trip point by heating through the setpoint and checking that the relay switches at the correct temperature.
5. Adjust hysteresis: if the relay cycles rapidly, increase the feedback resistor. If the deadband is too wide (temperature swings too large), decrease it.

**Expected accuracy**: ±0.1-1°C over -50 to 300°C range. The high sensitivity of NTC thermistors makes them easy to use with simple circuits. Long-term stability is ±0.1-0.2°C per year for glass-encapsulated beads, worse for epoxy-coated discs.

**Applications**: 3D printer hotend control, battery pack thermal management, home brewing temperature control, HVAC systems, medical thermometer circuits, refrigerator temperature control. The thermistor thermostat is the most common electronic thermostat in consumer products. It is cheap, sensitive, and simple to interface with both analog and digital circuits.

**Strengths**:
- Very high sensitivity (3-6% per °C) simplifies circuit design
- Simple voltage divider interface; no bridge circuit needed
- Small size allows fast response and easy placement
- Cheap to produce in quantity
- Compatible with both analog and digital circuits

**Weaknesses**:
- Non-linear resistance-temperature response complicates wide-range use
- Limited temperature range (-50 to 300°C) compared to thermocouples
- Self-heating errors if excitation current is too high
- Long-term drift of ±0.1-0.2°C per year requires periodic recalibration
- Not interchangeable without selection or software compensation


## Silicon Junction (Diode/Transistor) Thermostat

**Principle**: The forward voltage drop of a silicon pn junction decreases by approximately -2.0 to -2.2 mV per °C, nearly linearly over a wide temperature range. This property is inherent to silicon semiconductor physics: the bandgap voltage decreases with temperature, and the forward voltage tracks it. A diode (1N4148, 1N4001) or the base-emitter junction of a transistor (2N2222) driven by a constant current source produces a temperature-dependent voltage that can be measured with a simple op-amp circuit.

**Prerequisites**:
- [Semiconductor diode or transistor manufacturing](../silicon/basic-devices.md)
- [Constant current source circuit](../electronics/semiconductor-devices.md)
- [Operational amplifier](../electronics/semiconductor-devices.md)
- [Basic electronics assembly](../electronics/assembly.md)

**Materials**:
- [Silicon diode](../silicon/basic-devices.md) (1N4148 or 1N4001) or [NPN transistor](../silicon/basic-devices.md) (2N2222, connected as diode: base and collector shorted)
- [Constant current source](../electronics/semiconductor-devices.md): LM334 adjustable current source or discrete circuit (op-amp + transistor + resistor)
- [Operational amplifier](../electronics/semiconductor-devices.md): LM358 or TL072
- [Precision resistors](../electronics/passive-components.md) (1% metal film)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts
- [Flyback diode](../electronics/semiconductor-devices.md) (1N4007)
- [5V or 12V regulated power supply](../electronics/electrical-systems.md)

**Construction**:

1. **Configure the temperature sensor**: Connect a transistor as a diode (short base to collector, use the base-emitter junction as the sensing element). Drive it with a constant current of 100 μA (set by the LM334 with a 680 Ω programming resistor). At 25°C, the forward voltage is about 650 mV. At 100°C, it drops to about 485 mV. The sensitivity is about -2.1 mV/°C.

2. **Build the measurement circuit**: Amplify the diode voltage with an op-amp. Since the diode voltage decreases with temperature (for a heating thermostat, you want the output to *increase* with temperature), use an inverting amplifier configuration. Gain of 50 converts the -2.1 mV/°C slope to -105 mV/°C, which is -0.105 V/°C. Over a 100°C range, this gives a 10.5 V swing (use a ±12V supply or reduce the gain).

3. **Add the setpoint comparator**: Feed the amplified sensor voltage to one input of a comparator (LM311). Connect a potentiometer (voltage divider from Vcc to ground) to the other input as the setpoint. Add hysteresis by connecting a feedback resistor (1-10 MΩ) from the comparator output back to the sensor input.

4. **Calibration compensation**: Silicon diodes from different batches have varying nominal forward voltages (600-700 mV at 25°C). The sensor must be individually calibrated. Add an offset adjustment potentiometer to null out the part-to-part variation.

**Calibration**:

1. Immerse the sensor in an ice-water bath (0°C). Measure the output voltage. Adjust the offset pot to a convenient reference (e.g., 0V at 0°C).
2. Transfer to boiling water (100°C). The output should change by approximately 10.5V (with gain of 50). Adjust the gain resistor if needed.
3. Set the comparator trip point using the calibrated output voltage.
4. The linearity is excellent: the diode forward voltage is within ±0.5°C of linear over -55 to 150°C.

**Expected accuracy**: ±1-3°C over -55 to 150°C range. Accuracy is limited by the initial calibration and the current source stability. With careful calibration, ±0.5°C is achievable.

**Applications**: CPU temperature monitoring and throttle control, battery charger temperature cutoff, power supply overtemperature protection, simple electronic thermostat where a thermistor is not available. The silicon junction sensor is very cheap (a single diode) but has a limited temperature range compared to thermistors or RTDs. Most useful as an embedded sensor in electronic systems where a silicon diode or transistor is already present.

**Strengths**:
- Sensor is extremely cheap (a single diode or transistor)
- Nearly linear response over the operating range
- Easy to integrate into existing electronic circuits
- Small size and fast thermal response
- Well-understood semiconductor physics

**Weaknesses**:
- Limited temperature range (-55 to 150°C); unusable for high-temperature applications
- Significant part-to-part variation in forward voltage requires individual calibration
- Requires a stable constant current source for accurate readings
- Not as accurate as RTDs or thermistors without careful calibration
- Accuracy degrades if current source drifts with temperature or supply voltage


## IC Temperature Sensor Thermostat

**Principle**: A dedicated integrated circuit combines a bandgap temperature sensor with signal conditioning, analog-to-digital conversion, and (in digital types) a serial interface. The bandgap sensor exploits the difference between the thermal voltage (PTAT: proportional to absolute temperature) and the bandgap voltage (constant with temperature) to produce a calibrated output. Analog types (LM35, TMP36) output a voltage directly proportional to temperature (10 mV/°C for LM35). Digital types (DS18B20) output temperature as a digital number over a 1-wire serial interface, eliminating analog noise issues.

**Prerequisites**:
- [IC fabrication capability](../silicon/basic-devices.md)
- [PCB assembly](../electronics/assembly.md) (soldering)
- [Microcontroller](../computing/embedded-systems.md) for digital types (reading serial data)
- [Regulated power supply](../electronics/electrical-systems.md)

**Materials**:
- IC temperature sensor:
  - Analog: [LM35](../silicon/basic-devices.md) (10 mV/°C, 0-150°C), TMP36 (500 mV offset + 10 mV/°C, -40 to 125°C)
  - Digital: [DS18B20](../silicon/basic-devices.md) (12-bit resolution, -55 to 125°C, 1-wire interface), LM75 (I2C interface)
- [Comparator](../electronics/semiconductor-devices.md) (for analog types): LM311
- [Microcontroller](../computing/embedded-systems.md) (for digital types): ATmega328 or similar
- [Relay driver](../electronics/semiconductor-devices.md): switching transistor (2N2222) with [flyback diode](../electronics/semiconductor-devices.md) (1N4007)
- [Relay](../electronics/passive-components.md): 12V DC coil, 10A contacts, or [SSR](../electronics/power-electronics.md)
- [PCB](../electronics/pcb-fabrication.md), solder, hookup wire
- [Bypass capacitors](../electronics/passive-components.md) (100 nF ceramic, 10 μF electrolytic)

**Construction (Analog Type - LM35)**:

1. **Power the sensor**: Connect Vcc (4-30V) and ground to the LM35. Add a 100 nF bypass capacitor between Vcc and ground, placed within 10 mm of the IC. The LM35 draws only 60 μA, so self-heating is negligible (<0.1°C in still air).

2. **Read the output**: The LM35 output pin produces a voltage of 10 mV/°C. At 25°C, the output is 250 mV. At 100°C, it is 1.000V. This low-level signal is susceptible to noise pickup on long wires. Keep the sensor close to the comparator, or use shielded cable.

3. **Build the comparator**: Feed the LM35 output to the non-inverting input of an LM311 comparator. Feed the setpoint (from a potentiometer voltage divider) to the inverting input. The setpoint voltage for a desired temperature T is: V_setpoint = T × 0.01V. For 50°C: V_setpoint = 0.500V.

4. **Add hysteresis and relay driver**: Connect a high-value resistor (1-10 MΩ) from the comparator output back to the non-inverting input for hysteresis. Connect the comparator output through a current-limiting resistor to the base of a switching transistor (2N2222). The transistor drives the relay coil. Add a flyback diode (1N4007) across the relay coil.

**Construction (Digital Type - DS18B20)**:

1. **Wire the 1-wire bus**: Connect the DS18B20 data pin to a microcontroller GPIO pin through a 4.7 kΩ pullup resistor to Vcc. The 1-wire bus can connect multiple sensors on the same wire (each DS18B20 has a unique 64-bit serial number).

2. **Write the firmware**: Initialize the 1-wire bus, send a temperature conversion command, wait 750 ms (for 12-bit resolution), read the result. The DS18B20 returns temperature as a 16-bit signed integer in units of 0.0625°C. For thermostat operation, compare the reading to a setpoint stored in the microcontroller's EEPROM. Drive a relay based on the comparison.

3. **Add a display** (optional): Connect a 16×2 LCD or 7-segment display to show current temperature and setpoint. Add up/down buttons for setpoint adjustment. Store the setpoint in EEPROM so it survives power cycles.

**Calibration**:

1. For the LM35: verify at two temperatures (ice water and body temperature or boiling water). The LM35 is factory-calibrated to ±0.5°C at 25°C. If the reading is off by a constant offset, add a correction in the comparator setpoint. If the slope is wrong (reading drifts with temperature), the IC is defective.
2. For the DS18B20: the digital output is factory-calibrated to ±0.5°C from -10 to 85°C. Verify by immersion in a known-temperature bath. Apply a software offset correction if needed.

**Expected accuracy**: ±0.5°C typical (factory-calibrated). The DS18B20's 12-bit resolution gives 0.0625°C granularity, though absolute accuracy is ±0.5°C. The LM35 is ±0.25°C at room temperature, ±0.75°C over full range.

**Applications**: Precision temperature monitoring and control where IC packaging is acceptable, data logging temperature with microcontroller, multi-zone temperature monitoring (multiple DS18B20 on one 1-wire bus), smart thermostat projects, laboratory equipment with digital readout. The IC temperature sensor is the modern default for electronic thermostat projects: easy to interface, factory-calibrated, and available in convenient packages.

**Strengths**:
- Factory calibrated; no sensor-level calibration needed
- Easy interface (voltage output for analog, serial bus for digital)
- Digital types eliminate analog noise and long-wire signal degradation
- Multiple sensors on a single bus (DS18B20 1-wire)
- Compact IC packages with minimal external components

**Weaknesses**:
- Requires full IC fabrication infrastructure to manufacture
- Limited temperature range (-55 to 150°C) by silicon semiconductor physics
- Packaged ICs not suitable for harsh environments (corrosive, high-pressure, cryogenic)
- Self-heating in small packages affects accuracy at low airflow
- Dependent on a single supplier or complex supply chain for specific IC types


## Digital/Microcontroller PID Thermostat

**Principle**: Any electronic temperature sensor (thermocouple, RTD, thermistor, IC sensor) feeds its reading to a microcontroller running a Proportional-Integral-Derivative (PID) control algorithm. The PID algorithm computes three terms from the error (difference between measured temperature and setpoint): P = proportional to current error, I = integral of error over time (eliminates steady-state offset), D = derivative of error (anticipates future error, reduces overshoot). The combined PID output drives a solid-state relay (SSR), triac, or PWM-controlled heater. The result is smooth, precise temperature regulation without the oscillation inherent in on/off control.

The PID algorithm in discrete form: output(n) = Kp × e(n) + Ki × Σe(i) × Δt + Kd × (e(n) - e(n-1)) / Δt, where e(n) = setpoint - measurement, Kp/Ki/Kd are tuning constants, and Δt is the sample interval.

**Prerequisites**:
- [Microcontroller](../computing/embedded-systems.md) (Arduino ATmega328, ESP32, STM32, or similar)
- [Firmware development capability](../computing/embedded-systems.md) (C/C++ programming)
- [Electronic temperature sensor](./temperature-pressure.md) (thermistor, RTD, thermocouple with amplifier, or IC sensor)
- [Solid-state relay (SSR)](../electronics/power-electronics.md) or [triac](../electronics/power-electronics.md) for heater switching
- [PCB assembly](../electronics/pcb-fabrication.md) and [power supply](../electronics/electrical-systems.md)

**Materials**:
- [Microcontroller board](../computing/embedded-systems.md) (Arduino Nano, ATmega328P, or equivalent)
- Temperature sensor (choose one):
  - [Thermistor](../ceramics/electronic-ceramics.md) (10 kΩ NTC) with voltage divider
  - [RTD (Pt100)](../metals/precious-metals.md) with Wheatstone bridge and amplifier
  - [Thermocouple](./temperature-pressure.md) with MAX6675 or MAX31855 converter IC
  - [IC sensor (DS18B20 or LM35)](../silicon/basic-devices.md)
- [SSR](../electronics/power-electronics.md): DC-controlled AC solid-state relay (Fotek SSR-25DA or equivalent, rated for heater current)
- [Enclosure](../polymers/thermoplastics.md) and connectors
- [Display (optional)](../electronics/semiconductor-devices.md): 16×2 LCD or OLED
- [Keypad or rotary encoder](../electronics/passive-components.md) (for setpoint entry)
- [Power supply](../electronics/electrical-systems.md): 5V DC for microcontroller, 12V DC for SSR control

**Construction**:

1. **Build the sensor interface**: Connect the temperature sensor to the microcontroller's ADC input (for analog sensors) or digital I/O (for DS18B20 or other digital sensors). For thermocouple input, use a MAX6675 or MAX31855 thermocouple-to-digital converter IC, which handles cold junction compensation and outputs temperature directly over SPI.

2. **Wire the SSR control**: Connect a microcontroller PWM output pin to the SSR control input through a current-limiting resistor (220 Ω for most SSRs). The SSR switches the AC heater power. The microcontroller varies the duty cycle of the PWM signal to control average heater power. A 10-second PWM period with 1-second resolution gives 10% power steps, sufficient for most applications. Faster PWM (1-2 second period) gives smoother control.

3. **Write the PID firmware**:
   ```
   // Pseudocode for PID thermostat
   setpoint = desired_temperature
   Kp = 10.0   // Proportional gain (tuning parameter)
   Ki = 0.5    // Integral gain
   Kd = 50.0   // Derivative gain
   integral = 0
   prev_error = 0
   
   loop every 500ms:
     measurement = read_sensor()
     error = setpoint - measurement
     integral = integral + error * dt
     integral = clamp(integral, -max, max)  // Anti-windup
     derivative = (error - prev_error) / dt
     output = Kp * error + Ki * integral + Kd * derivative
     output = clamp(output, 0, 100)  // 0-100% heater power
     set_pwm_duty(output)
     prev_error = error
   ```

4. **Tune the PID constants**: Start with Kp only (Ki=0, Kd=0). Increase Kp until the system oscillates, then halve it. Add Ki to eliminate steady-state offset (start small, 0.1-0.5). Add Kd to reduce overshoot (start with Kd ≈ Kp × 0.1). The Ziegler-Nichols tuning method provides a systematic approach.

5. **Add safety features**:
   - **Watchdog timer**: If the microcontroller crashes, the watchdog resets it within 250 ms, ensuring the heater doesn't stay on indefinitely.
   - **High-limit cutoff**: Independent hardware thermostat (bimetallic strip, Type 3) wired in series with the heater as a backup. If the software fails, the hardware cutoff prevents runaway heating.
   - **Sensor break detection**: If the sensor reading goes out of range (open circuit, short circuit), shut off the heater and sound an alarm.

**Calibration**:

1. Calibrate the sensor separately by comparing it to a [reference thermometer](./temperature-pressure.md) at known temperature points. For a thermistor, record resistance vs. temperature. For a thermocouple, verify voltage output at ice point and boiling point. For an IC sensor, check against factory calibration at two temperatures.
2. The PID algorithm itself needs no calibration, only tuning. Tuning depends on the thermal characteristics of the system (heater power, thermal mass, insulation, heat loss rate). A well-insulated kiln with 2 kW heater and 50 kg of thermal mass will need different PID constants than a small oven with 200 W heater and 2 kg thermal mass.
3. Typical tuning for a small oven: Kp = 5-20, Ki = 0.1-1.0, Kd = 10-100. Start conservative (low gains) and increase until response is satisfactory.
4. Verify by running the system through a full setpoint range (e.g., from room temperature to setpoint and back). Watch for overshoot (should be <5°C), settling time (should be <10 minutes for small systems), and steady-state error (should be <0.5°C with integral term active).

**Expected accuracy**: Determined entirely by the sensor. With a thermistor: ±0.1-0.5°C. With an RTD: ±0.05-0.2°C. With a thermocouple: ±1-3°C. The PID algorithm itself contributes negligible error if properly tuned. Temperature stability of ±0.01°C is achievable with a good RTD sensor and well-tuned PID.

**Applications**: Precision furnace control for semiconductor manufacturing (crystal growth, diffusion, oxidation), laboratory oven regulation, reflow soldering, espresso machine temperature control, sous-vide cooking, 3D printer hotend and heated bed control, incubator temperature regulation. The digital PID thermostat is the standard for any application requiring precise, stable temperature control. It supersedes all purely mechanical thermostats for new designs.

**Strengths**:
- Best possible temperature control: eliminates steady-state offset (integral term), reduces overshoot (derivative term)
- Compatible with any electronic temperature sensor
- Tunable for different thermal systems by adjusting PID constants
- Supports data logging, remote monitoring, and complex control profiles
- Proportional output eliminates on/off cycling and extends heater life

**Weaknesses**:
- Requires firmware development skill (C/C++ programming)
- Software bugs can cause heater runaway if watchdog timer is not implemented
- Needs a reliable power supply; power loss disables all control
- PID tuning requires experimentation for each new thermal system
- More expensive and complex than mechanical or simple electronic alternatives


---

*Part of [Thermostats & Temperature Control](./thermostat.md) • [Measurement](./index.md) • [All Domains](../index.md)*
