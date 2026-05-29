# Electrical Instruments

> **Node ID**: measurement.electrical-instruments
> **Domain**: [Measurement](./index.md)
> **Dependencies**: [`energy.electricity`](../energy/electricity.md), [`measurement`](./index.md)
> **Enables**: [`computing.electromechanical`](../computing/electromechanical.md), [`telecom.radio`](../telecom/radio.md)
> **Timeline**: Years 20-35
> **Outputs**: voltmeter, ammeter, ohmmeter, oscilloscope, multimeter, insulation_tester, frequency_counter
> **Critical**: No — measurement improves quality but civilization can function without precision instruments

## Problem

Electrical systems cannot be built or maintained without measurement. You need to know voltage (is the generator producing what it should?), current (is the load drawing too much?), resistance (is the insulation intact?), frequency (is the alternator spinning at the right speed?), and waveform (is the AC output clean or distorted?). This page covers the instruments that answer these questions, from the fundamental galvanometer movement through digital multimeters, oscilloscopes, and specialized testers.

### Prerequisites

- [Electricity](../energy/electricity.md) — power generation, voltage, current, and circuit fundamentals
- [Measurement fundamentals](./index.md) — calibration philosophy and traceability
- [Copper wire](../metals/copper.md) — fine wire for galvanometer coils and instrument windings
- [Magnets](../metals/magnetism.md) — permanent magnets for meter movements
- [Glass](../glass/index.md) — CRT envelopes for oscilloscopes

## Galvanometer (D'Arsonval Movement)

The D'Arsonval movement is the foundation of analog electrical measurement. A lightweight coil of fine wire (typically 40-50 gauge, 0.08-0.08 mm diameter) is suspended in the field of a permanent magnet. Current through the coil generates a torque proportional to the current: T = N × B × I × A, where N is the number of turns, B is the magnetic field strength, I is the current, and A is the coil area. A hairspring (phosphor bronze spiral) provides a restoring torque proportional to the deflection angle. The pointer reaches equilibrium when these torques balance, giving a deflection proportional to current.

Sensitivity is specified as the current for full-scale deflection (FSD). Common movements: 50 μA FSD (high sensitivity, used in voltmeters), 1 mA FSD (rugged, used in panel meters). Internal resistance: 50-5000 Ω depending on coil wire gauge and turns. A 50 μA movement typically has 1000-5000 Ω internal resistance. The taut-band suspension (replacing pivots and jewel bearings with a twisted metal band) eliminates friction, improving repeatability and eliminating the need for leveling.

The galvanometer is inherently a current-measuring device. Every other analog instrument (ammeter, voltmeter, ohmmeter) is a galvanometer with external circuitry that converts the measured quantity to a proportional current.

## Ammeter

Measures current by passing it through (or a known fraction of it through) the meter movement. A bare 50 μA movement measures only up to 50 μA. To measure higher currents, a shunt resistor is placed in parallel with the meter. The shunt carries most of the current; a precise fraction passes through the meter movement.

Shunt resistance: R_shunt = (I_meter × R_meter) / (I_range - I_meter). Example: a 50 μA, 2000 Ω movement converted to measure 0-1 A requires R_shunt = (0.00005 × 2000) / (1.0 - 0.00005) = 0.1000 Ω. The shunt is a precisely calibrated manganin or constantan strip (low temperature coefficient of resistance, <20 ppm/°C, to prevent drift with self-heating). At 1 A, the shunt dissipates I²R = 0.1 W, raising its temperature slightly. Manganin's near-zero temperature coefficient keeps the resistance stable.

Multi-range ammeters use switchable shunts. Ranges typically span 1 mA to 10 A in decade steps. The burden voltage (voltage drop across the ammeter) is I × (R_shunt ∥ R_meter), typically 50-200 mV at full scale. This voltage drop affects the circuit being measured; lower burden voltage is better. An ammeter is always connected in series with the load, never in parallel (a parallel ammeter shorts the supply, destroying the meter and possibly the supply).

## Voltmeter

Measures voltage by passing a small, known current through the meter movement. A series resistor (multiplier) is added: R_multiplier = (V_range / I_meter) - R_meter. Example: a 50 μA, 2000 Ω movement for a 0-10 V range needs R_multiplier = (10 / 0.00005) - 2000 = 198,000 Ω. Total meter resistance is 200 kΩ, giving a sensitivity of 20,000 Ω/V. This sensitivity figure matters because the voltmeter draws current from the circuit under test, loading it and changing the voltage being measured. Higher Ω/V means less loading.

Multi-range voltmeters switch different multiplier resistors. Common ranges: 1 V, 10 V, 100 V, 1000 V. High-voltage multipliers (for the 1000 V range) dissipate significant power: P = V²/R = 1000² / 20,000,000 ≈ 0.05 W. Standard 1/4 W resistors suffice, but for sustained high-voltage measurement, 1 W resistors are safer.

A voltmeter is always connected in parallel with the component or circuit being measured. A 1000 V range on a 20,000 Ω/V meter draws 50 μA, negligible in power circuits but significant in high-impedance electronics (where a 1 MΩ source resistance would see its voltage drop by 5% from meter loading alone).

## Ohmmeter

Measures resistance by applying a known voltage from an internal battery and measuring the resulting current. The series-type ohmmeter uses an internal battery (typically 1.5 V for low ranges, 9 V or 15 V for high ranges), the meter movement, a zero-adjust resistor, and the unknown resistance all in series.

The scale is nonlinear and reads right-to-left: zero resistance gives full-scale deflection (maximum current), infinite resistance gives zero deflection (no current). The midpoint of the scale represents R_mid = V_battery / I_FSD. A 1.5 V battery with a 50 μA movement gives R_mid = 30 kΩ. Measurements are most accurate near the midpoint of the scale (the nonlinear compression at both ends degrades resolution).

Zero adjustment: short the test leads and adjust the zero potentiometer until the meter reads exactly zero ohms (full-scale current). This compensates for battery voltage decline over time. As the battery drops from 1.5 V to 1.2 V (end of life), the zero adjustment adds series resistance to maintain full-scale current, but the R_mid point shifts, reducing accuracy on the high-resistance end.

For precision resistance measurement, the Wheatstone bridge (below) is preferred over the ohmmeter.

## Wheatstone Bridge

Four resistors arranged in a diamond, with a galvanometer (null detector) across the middle and a battery across the top and bottom. At balance (galvanometer reads zero), the ratio of resistances is equal: R1/R2 = R3/R4. If three resistors are known, the fourth is calculated: R_unknown = R_known × (R_ratio1 / R_ratio2).

The bridge's power comes from null measurement: at balance, no current flows through the galvanometer, so the meter's internal resistance and the meter accuracy do not affect the result. Only the resistor values matter. With precision resistors (0.01% tolerance, available as wire-wound standards), the bridge measures resistance to 0.01 Ω resolution.

Practical construction: ratio arms (R1, R2) are switched in decade steps (1:1, 1:10, 10:1, 1:100, 100:1). The known arm (R3) is a calibrated decade resistance box (0.1 Ω to 1 MΩ in steps). The galvanometer detects the null; its sensitivity determines the smallest detectable imbalance. A 50 μA movement can detect a 1 μA unbalance current, giving a resolution of about 0.01% of the unknown resistance.

The Kelvin double bridge extends the Wheatstone to very low resistances (<1 Ω) by eliminating lead and contact resistance errors. Used for measuring bus bar resistance, motor winding resistance, and shunt calibration.

## Oscilloscope

The oscilloscope displays voltage waveforms as a graph of voltage (vertical axis) versus time (horizontal axis). It reveals signal characteristics invisible to a meter: waveform shape, frequency, amplitude, distortion, noise, and timing relationships between multiple signals.

### CRT-Based Oscilloscope

A cathode ray tube (CRT) fires a focused electron beam at a phosphor-coated screen. Vertical deflection plates move the beam up and down proportional to the input voltage. Horizontal deflection plates sweep the beam across the screen at a controlled rate (time base). The phosphor (P31 green, P22 white) emits light where the beam strikes, creating a visible trace that persists briefly (persistence: 1-100 ms depending on phosphor type).

**Vertical system**: Input attenuator and amplifier scale the signal to fit the CRT's deflection range. Sensitivity: 1 mV/division to 20 V/division in a 1-2-5 sequence. Bandwidth: DC to 100 MHz (typical general-purpose). The bandwidth defines the highest frequency the vertical amplifier can reproduce with less than 3 dB attenuation. A 100 MHz scope can display a 100 MHz sine wave at 70% of its true amplitude; square waves and pulses require 5-10× the fundamental frequency in bandwidth for accurate edge display.

**Time base**: A ramp generator produces a linear voltage sweep for horizontal deflection. Sweep speed: 0.1 μs/division to 0.5 s/division. A 10-division screen at 1 μs/division shows a 10 μs time window, enough for 10 cycles of a 1 MHz signal.

**Trigger**: The trigger circuit starts the sweep at a consistent point on the waveform, producing a stable display instead of a random jumble. Trigger source: the input channel itself, an external trigger input, or the line frequency. Trigger level: the voltage threshold that initiates the sweep. Without triggering, repetitive waveforms appear to drift randomly across the screen.

**Dual-trace**: Two input channels share the CRT, displayed either by alternating sweeps (ALT mode, for fast sweeps) or chopping between channels at a high rate (CHOP mode, for slow sweeps). Allows comparing timing between two signals.

## Multimeter

### Analog Multimeter (VOM)

Combines voltmeter, ammeter, and ohmmeter in one instrument using a single galvanometer movement with switchable range circuits. The classic Simpson 260 (1940s design still in use) has a 50 μA movement, 20,000 Ω/V sensitivity on DC voltage ranges, 5,000 Ω/V on AC (rectifier losses reduce sensitivity). AC measurement uses a copper-oxide or germanium diode rectifier to convert AC to DC for the movement. The rectifier introduces nonlinearity and a minimum voltage threshold (~0.3 V), so AC voltage ranges are less accurate than DC (typically ±3% vs ±1.5%).

Ohms ranges use an internal 1.5 V battery (R × 1, R × 10, R × 100) and a 15 V or 22.5 V battery (R × 10K) for higher resistance ranges. The analog ohms scale's nonlinearity limits accuracy to ±5% at best (near midscale).

### Digital Multimeter (DMM)

Uses a dual-slope integrating analog-to-digital converter (ADC). The input voltage charges an integrator capacitor for a fixed time (signal integrate), then a reference voltage of opposite polarity discharges it (de-integrate). The ratio of discharge time to integrate time equals the ratio of input voltage to reference voltage. This technique rejects 50/60 Hz power line noise (the integration period is chosen as a multiple of the line period) and provides stable readings.

Resolution: 3.5 digits (1999 counts), 4.5 digits (19999 counts), or 6.5 digits (1999999 counts) for bench instruments. Accuracy: ±0.5% for a 3.5-digit DMM on DC voltage, ±1.0% on AC voltage. Auto-ranging selects the optimal range automatically. Input impedance: typically 10 MΩ on DC voltage ranges (vs. 20 kΩ/V for a 50 μA analog meter on the 1 V range), minimizing circuit loading.

Current measurement uses internal shunt resistors. The burden voltage is displayed during current measurement: 0.1 V at 2 A on the 10 A range. For AC measurement, the DMM uses either average-responding (calibrated for sine waves, reads low on non-sinusoidal waveforms) or true-RMS conversion (computes the actual root-mean-square value, accurate for any waveform). True-RMS meters cost more but are essential for measuring distorted waveforms, variable-frequency drives, and switched-mode power supplies.

## Wattmeter (Dynamometer Type)

Measures real electrical power (watts) directly. The dynamometer movement has two coils: a fixed current coil (low resistance, connected in series with the load) and a movable voltage coil (high resistance, connected in parallel with the load). The torque on the moving coil is proportional to the product of the two currents: T ∝ I_load × V_load / R_voltage_coil ∝ P. The pointer deflection is proportional to instantaneous power, and the mechanical inertia of the movement averages the reading.

For AC circuits, the dynamometer inherently measures real power because the instantaneous torque follows the product of instantaneous voltage and current, which averages to the real power (the reactive component averages to zero over a cycle). Range: 0-5 W to 0-10 kW depending on coil ratings. Accuracy: ±0.5-1.0% of full scale.

Three-wattmeter method for three-phase power: one wattmeter per phase, total power is the sum. Two-wattmeter method (Blondel's theorem): two wattmeters measure total three-phase power without a neutral connection, but the individual readings have no physical meaning.

## Insulation Tester (Megger)

Measures the insulation resistance of cables, motor windings, transformers, and switchgear. Insulation resistance should be high (>1 MΩ for most equipment, >100 MΩ for high-voltage insulation). An ordinary ohmmeter (1.5 V battery) cannot measure these high resistances accurately because the test voltage is too low to reveal insulation defects that appear only at operating voltage.

The megger generates a high DC test voltage (500 V, 1000 V, 2500 V, or 5000 V) using a hand-cranked DC generator or electronic inverter. The generated voltage is applied across the insulation under test. A ratio-meter movement (two coils on a common shaft, one carrying the test current, one carrying a reference current proportional to the generator voltage) indicates resistance directly. The ratio measurement compensates for generator speed variations: cranking faster generates more voltage but also proportionally more reference current, so the reading is independent of cranking speed.

Test procedure: disconnect the equipment from all power sources. Connect one lead to the conductor and the other to ground (or the other conductor). Crank steadily (120 RPM for hand-crank models) or press the test button (electronic models). Read resistance after 60 seconds (the one-minute reading). Compare to the one-minute reading divided by the 30-second reading (polarization index): a healthy insulation has a PI >2.0. A PI <1.5 indicates moisture or contamination.

## Frequency Counter

Measures the frequency of a periodic signal by counting cycles over a precisely timed gate interval. A crystal oscillator (typically 10 MHz, temperature-compensated or oven-controlled for stability ±0.01% or better) generates the timebase. The gate time is derived from this crystal: a 1-second gate counts cycles directly in Hz (1 count = 1 Hz resolution), a 0.1-second gate gives 10 Hz resolution, a 10-second gate gives 0.1 Hz resolution.

The input signal is amplified, squared (converted to a clean digital waveform by a comparator with hysteresis), and fed to a counter chain. At the start of the gate, the counter begins counting input cycles. At the end of the gate, the count is latched and displayed. Resolution = 1 / gate_time. For a 10 MHz signal measured with a 1-second gate: reading is 10,000,000 Hz ±1 count. Accuracy is limited by the timebase crystal stability: ±0.01% for a TCXO (temperature-compensated crystal oscillator), ±0.0001% for an OCXO (oven-controlled).

Reciprocal counting: instead of gating the input signal, the counter gates by the input signal period and counts timebase clocks. This gives fixed resolution regardless of input frequency. A 10 MHz timebase counting over one cycle of a 1 kHz input gives 10,000 counts (0.01% resolution), far better than conventional counting (which would count 1 cycle in a 1 ms gate, giving 1 kHz ±1 Hz, or 0.1% resolution).

## Construction Notes

### Galvanometer Movement

Wind the moving coil on an aluminum former (the former also acts as an eddy-current damper, slowing the pointer to prevent overshoot). Wire gauge and turns are chosen for the desired sensitivity: a 50 μA movement uses ~200 turns of 50 AWG wire on a 15 × 20 mm former. The coil assembly must be lightweight (50-200 mg) for responsive deflection. The permanent magnet is alnico (see **Magnetic Materials** (alnico or ferrite)) or ferrite, shaped with pole pieces to create a uniform radial field in the air gap where the coil rotates. The return springs are phosphor bronze, 0.01-0.02 mm thick, providing 5-20 μN·cm/degree of restoring torque.

### Shunt Resistor Construction

Cut a strip of manganin sheet (84% Cu, 12% Mn, 4% Ni, temperature coefficient <20 ppm/°C) to the calculated width and length for the desired resistance. Mill or file trimming notches to fine-tune resistance to ±0.1%. Mount between heavy copper terminal blocks with silver-soldered joints. The terminal blocks carry the high current and provide a low-resistance path to the shunt strip. For a 100 A shunt at 75 mV output: R = 0.075/100 = 0.00075 Ω. The manganin strip might be 20 mm wide, 0.5 mm thick, and 50 mm long between terminals, adjusted during calibration.

### Multiplier Resistor Selection

Voltmeter multiplier resistors must be stable and accurate. Wire-wound resistors (manganin or Evanohm wire on a ceramic former) provide the best stability (±0.01% per year drift) but have inductance that affects AC measurements. For DC voltmeters, wire-wound is ideal. For AC-capable meters, carbon film or metal film resistors with low inductance are preferred, though their accuracy (±1%) is worse than wire-wound. Calculate the required power dissipation for each range: the 1000 V range on a 20,000 Ω/V meter draws 50 μA, dissipating 0.05 W in the multiplier. Use resistors rated for at least twice the calculated dissipation for long-term stability. High-voltage multipliers (>500 V) should be potted in epoxy or mounted on standoffs to maintain creepage and clearance distances.

### Decade Resistance Box

A precision variable resistor used as the known arm of the Wheatstone bridge. Four or five decade dials, each with ten position switches selecting one of ten precision resistors (0.1, 1, 10, 100, 1000, 10,000 Ω). Total range: 0-99,999.9 Ω. Each resistor is calibrated to ±0.05% or better. Switch contacts are silver-plated to minimize contact resistance (each switch adds 1-5 mΩ). The box is shielded to prevent stray pickup. Used not only for bridge measurements but for any application requiring a precisely known variable resistance: circuit trimming, sensor simulation, calibration reference.

## Integration Points

| Phase | Instruments | Application |
|-------|------------|-------------|
| Power generation | Voltmeter, ammeter, frequency counter | Monitor generator output voltage, load current, and frequency |
| Power distribution | Megger, wattmeter, current transformer | Test cable insulation, measure power consumption, meter billing |
| Motor and drive systems | Ammeter, oscilloscope, insulation tester | Motor starting current, drive waveform quality, winding insulation |
| Electronics production | DMM, oscilloscope, frequency counter | Circuit testing, signal analysis, oscillator calibration |
| Semiconductor fab | Precision DMM, electrometer, LC meter | Wafer probing (μV-level measurements), leakage currents, process control |

### Measurement of Non-Electrical Quantities

Electrical instruments serve as the foundation for measuring many non-electrical quantities through transducers. A thermocouple converts temperature to millivolts (see [Temperature & Pressure](../measurement/temperature-pressure.md)). A strain gauge converts mechanical strain to resistance change, measured with a Wheatstone bridge. A photodiode converts light intensity to current, measured with a picoammeter. A pH electrode generates a voltage proportional to hydrogen ion concentration (59.16 mV per pH unit at 25°C), measured with a high-impedance voltmeter (input impedance >10¹² Ω to avoid loading the electrode).

In each case, the electrical measurement technique (null methods for precision, direct-reading methods for speed) determines the achievable accuracy. The Wheatstone bridge principle extends to AC measurements with capacitance and inductance: the Maxwell bridge measures inductance, the Schering bridge measures capacitance and loss tangent, the Wien bridge measures frequency. These AC bridges use a headphone or oscilloscope as the null detector instead of a DC galvanometer.

## Calibration

All measurement instruments drift over time. Resistors change value with aging and moisture absorption. Meter movements lose calibration spring tension. Crystal oscillators age (frequency drifts a few ppm per year). A calibration program maintains traceability: compare each instrument against a more accurate reference at regular intervals.

Voltage calibration uses a standard cell (Weston cadmium cell: 1.01864 V at 20°C, stable to ±0.001% per year) as the primary reference, or a modern voltage reference IC (bandgap or buried zener, ±0.01% initial accuracy, ±5 ppm/°C temperature coefficient). Resistance calibration uses standard resistors (wire-wound manganin or Evanohm, 0.001-0.01% tolerance, aged for stability). Frequency calibration uses a crystal oscillator referenced to a standard (WWVB radio, GPS-disciplined oscillator, or rubidium frequency standard with ±10⁻¹¹ accuracy).

Calibration intervals depend on instrument stability and usage severity. Field multimeters: 6-12 months. Bench DMMs: 12 months. Standard resistors: 12-24 months. Oscilloscopes: 12 months (vertical calibration, time base calibration). Document all calibrations with before/after readings and uncertainty statements.

### CRT Oscilloscope Construction Notes

Building a CRT oscilloscope from scratch requires mastering several precision technologies. The CRT itself is a glassblowing challenge: the electron gun assembly (cathode, control grid, accelerating anodes, focus anode) must be aligned to within 0.1 mm inside the neck of the tube. The phosphor screen is deposited by settling a slurry of phosphor powder (P1 zinc silicate for green, P2 zinc sulfide-cadmium sulfide for long persistence) onto the faceplate, then drying and baking. The tube is evacuated to <10⁻⁶ mbar and sealed with a getter (barium flash getter to absorb residual gas).

The vertical amplifier must be linear from DC to the rated bandwidth with constant gain. A differential amplifier (long-tailed pair with current source) provides the required bandwidth and common-mode rejection. The time base ramp generator uses a constant current source charging a capacitor: V = (I/C)×t, producing a linear ramp. Linearity better than 1% across the screen is needed for accurate time measurements. The trigger comparator uses a Schmitt trigger circuit with adjustable threshold.

For bootstrapping, a 1-5 MHz bandwidth oscilloscope is achievable with discrete transistors (no ICs needed) and a hand-blown CRT. Such an instrument reveals AC power waveforms, audio signals, and switching transients, sufficient for power system debugging and basic electronics work. Bandwidth above 20 MHz requires fast transistors (fT > 500 MHz) and careful circuit layout to minimize stray capacitance.

### Component Measurement

Beyond the standard instruments listed above, several specialized measurements arise in electronics production:

**Capacitance measurement**: A capacitance bridge (similar to Wheatstone bridge but with AC excitation) compares the unknown capacitor against a standard. The Schering bridge measures capacitance and dissipation factor (tan δ) simultaneously, important for assessing capacitor quality. A capacitor with high dissipation factor wastes energy as heat and indicates poor dielectric material or manufacturing defects. Simple RC timing methods (charge the capacitor through a known resistor, measure the time constant) give capacitance to ±5% with an oscilloscope and stopwatch.

**Inductance measurement**: The Maxwell-Wien bridge measures inductance in terms of a known capacitance and resistance. The Hay bridge is better for high-Q inductors. A simple resonance method (connect the inductor in parallel with a known capacitor, find the resonant frequency with a signal generator and oscilloscope: L = 1/(4π²f²C)) gives inductance to ±2% with minimal equipment.

**Transistor testing**: A simple curve tracer displays the I-V characteristics of a transistor on an oscilloscope screen. A staircase generator drives the base current in steps while a sawtooth sweeps the collector voltage. The resulting family of curves reveals gain (β = ΔIc/ΔIb), saturation voltage, breakdown voltage, and leakage current. For sorting transistors into matched pairs (important for differential amplifiers and push-pull output stages), measure β at a specific operating point (e.g., Ic = 1 mA, Vce = 5 V) and match to within ±5%.

## Key Deliverables

- D'Arsonval galvanometer movements (50 μA and 1 mA FSD)
- Multi-range ammeters (1 mA to 10 A) with manganin shunts
- Multi-range voltmeters (1 V to 1000 V) with multiplier resistors
- Wheatstone bridge for precision resistance measurement
- CRT oscilloscope (DC-20 MHz bandwidth minimum)
- Digital multimeter (3.5 or 4.5 digit, true RMS)
- Dynamometer wattmeter for power measurement
- Insulation tester (megger, 500-5000 V)
- Frequency counter (10 MHz timebase, 0.1 Hz resolution)
- Decade resistance box for bridge measurements and calibration
- Calibration standards (voltage reference, standard resistors, crystal oscillator)

## Safety & Hazards

- **High-voltage measurement**: The 1000 V voltmeter range and megger outputs (500-5000 V DC) can cause fatal electric shock. Current as low as 10 mA through the chest causes ventricular fibrillation. Always de-energize circuits before connecting or disconnecting meters. Use insulated probe tips with finger guards. When measuring live high-voltage circuits, keep one hand in your pocket (prevents current across the chest). Megger testing must never be performed on energized equipment.
- **Current measurement hazards**: An ammeter in parallel with a voltage source creates a short circuit through the low-resistance shunt. The resulting current is limited only by the source's capacity: a car battery through a 0.01 Ω shunt produces 1200 A, vaporizing the shunt and spraying molten metal. Always verify the meter is in current mode and connected in series before energizing. Current transformer secondaries must never be open-circuited while the primary is energized: the secondary voltage rises to dangerous levels (kilovolts), destroying the transformer insulation and creating a shock hazard.
- **CRT hazards**: Oscilloscope CRTs operate at 1-3 kV accelerating voltage (intensity and focus). The CRT itself is an implosion hazard: the evacuated glass envelope stores atmospheric pressure energy. Handle CRTs with safety glasses and face shield. Discharge the CRT anode (under the insulating cup on the bell) to the grounded chassis before servicing, using an insulated probe. The stored charge can deliver a painful but rarely fatal shock.
- **Megger testing hazards**: The megger's output of 500-5000 V DC, though current-limited to a few milliamps, can cause a startling shock that leads to a fall from a ladder or involuntary contact with energized equipment. Always verify the circuit is de-energized and disconnected from all power sources before testing insulation. Capacitive loads (long cables, large motor windings) store charge after the megger is removed: discharge by connecting the test leads together or to ground for at least 30 seconds after testing. Failure to discharge can result in a shock when handling the supposedly disconnected cable.
- **Shunt hazards**: Current shunts carrying 100+ A produce significant heating. A 100 A shunt at 75 mV dissipates 7.5 W, reaching 60-80°C surface temperature. At 1000 A (large industrial shunts), dissipation is 75 W, requiring heatsinking or forced air cooling. Burns from touching an energized shunt are a real risk. Install shunts in enclosures with ventilation openings, and label with maximum current rating. Never apply current exceeding the shunt's rating: overheating changes manganin's resistance and permanently shifts calibration.

---

**Calibration Management**: Maintain calibration records for every instrument with serial number, calibration date, due date, standard used (traceable to national standards), and as-found/as-left data. Calibration intervals: DMMs 6-12 months, oscilloscopes 12 months, meggers 12 months. Field calibration checks between formal calibrations using reference standards (voltage reference: 10.000V ±0.01% for DMM spot-check, precision resistor 100.00 Ω ±0.01% for ohmmeter verification). Out-of-tolerance instruments trigger a review of measurements taken since last known-good calibration.

## Limitations

- **Accuracy constraints**: Analog instruments (D'Arsonval meters) achieve 1-2% of full-scale accuracy at best. Digital multimeters improve this to 0.1-0.5%. Calibration-grade instruments (0.01-0.1%) require precision resistors and voltage references that are themselves calibration-dependent. The accuracy chain is only as strong as its weakest link.
- **Loading effects**: Voltmeters draw current from the circuit under test (finite input impedance). Ammeters introduce series resistance. These loading effects alter the circuit being measured. A 1000 Ω/V analog voltmeter on a 10V range draws 10 mA — significant in high-impedance circuits. FET-input and vacuum-tube voltmeters (10+ MΩ input impedance) minimize loading but are more complex.
- **Frequency response limitations**: Moving-coil meters respond to DC and low-frequency AC only. Rectifier-type AC meters work to ~10 kHz. True RMS measurement at higher frequencies requires thermocouple or electronic methods. Oscilloscopes extend bandwidth to MHz-GHz range but require CRT or LCD display technology.
- **Calibration dependency**: All electrical instruments drift with time, temperature, and mechanical shock. Resistors change value with aging. Meter movements lose magnetic strength. Calibration against known standards (standard cells, precision resistors) must be performed every 6-12 months for instruments used in critical measurements.
- **CRT oscilloscope complexity**: A cathode-ray tube oscilloscope requires a vacuum tube CRT, high-voltage power supply (1-5 kV for acceleration), sweep circuitry, and vertical amplifiers. This represents a significant electronics manufacturing capability. Simpler alternatives (moving-coil meters with rectifiers) sacrifice waveform visualization.

### Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Meter reads zero (no deflection) | Open coil, broken hair spring, or loose connection | Check continuity of coil and leads; inspect hair spring; verify series resistor not open |
| Meter reads low on all ranges | Weakened permanent magnet or aged calibration | Recalibrate against standard; replace magnet if severely weakened |
| Voltmeter loads circuit (reads low) | Meter impedance too low for circuit under test | Use FET-input voltmeter or DMM (>10 MΩ input); calculate loading error |
| Oscilloscope trace drifts vertically | DC offset drift in vertical amplifier | Allow warm-up (15-30 min); check DC balance adjustment; recalibrate |
| Megger reads too low (false leakage) | Moisture on test leads or surface contamination | Clean terminals and leads; dry insulation before testing; use guard terminal |
| DMM resistance reading unstable | Dirty test lead contacts or low battery | Clean probe tips; replace battery; check lead resistance by shorting probes |
| Ammeter reads zero with current flowing | Blown fuse in meter or open shunt resistor | Replace internal fuse; verify shunt resistor continuity; never measure voltage on current range |

## See Also

- [Precision Metrology](precision-metrology.md) — electrical standards, calibration infrastructure
- [Temperature & Pressure](temperature-pressure.md) — thermocouples, RTDs (electrical sensors)
- [Optical Instruments](optical-instruments.md) — spectroscopes, refractometers
- [Electricity](../energy/electricity.md) — power generation, transmission, electrical engineering
- [Electronics](../electronics/index.md) — vacuum tubes, transistors, circuit design
- [Electromechanical Computing](../computing/electromechanical.md) — relay logic and early computer instruments
- [Telecom / Radio](../telecom/radio.md) — RF measurement and signal detection

[← Back to Measurement](index.md)
