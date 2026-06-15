# Analog Circuits

> **Node ID**: electronics.analog-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](../silicon/basic-devices.md), [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Timeline**: Years 20-45
> **Outputs**: analog-signal-processing
> **Critical**: No — pedagogy layer; underlying active and passive device manufacturing capabilities are the critical prerequisites

## Overview

This capability is the **design pedagogy hub** for every major analog circuit family that processes continuous signals. It does not re-explain how diodes, transistors, resistors, or capacitors are *made* — that is owned by [semiconductor devices](../silicon/basic-devices.md) and [passive components](passive-components.md). Instead it teaches how to *analyze and design* with those components: how to bias a transistor, close a feedback loop around an op-amp, satisfy the Barkhausen criterion in an oscillator, and predict the free-running frequency of a 555 timer.

Analog circuit design is learned as a ladder — each rung unlocks the next. Diode and transistor-switch circuits are the entry point (a single nonlinear device as a switch or clipper). Amplifier fundamentals add small-signal BJT/MOSFET biasing, gain, and impedance. Op-amp circuits use the ideal model and feedback to build integrators, Schmitt triggers, and active filters. Multivibrators bridge to timing, which splits into oscillators (frequency generation) and timers (the 555). This progression maps onto the Forrest M. Mims III notebook sequence — *Basic Semiconductor Circuits* → *Op Amp IC Circuits* → *555 Timer Circuits* — which has trained three generations of engineers from first principles.

Analog is the substrate beneath every power supply, sensor interface, and radio. The [power supply circuits](power-supply-circuits.md) and [interface circuits](interface-circuits.md) capabilities both consume the op-amp and comparator techniques taught here. [Communications circuits](communications-circuits.md) builds RF oscillators and receivers on the same amplifier foundations.

## Prerequisites

### Materials

- **Diodes** — 1N4148 (small-signal, 100 V, 200 mA), 1N4001–1N4007 (rectifier, 50–1000 V, 1 A), and 3–5 V zener diodes from [semiconductor devices](../silicon/basic-devices.md), for clipper, clamper, and reference circuits.
- **Transistors** — 2N3904/2N2222 (NPN) and 2N3906/2N2907 (PNP) BJTs (general-purpose small-signal); IRF510 or IRLZ44N N-channel MOSFETs for switching loads above 100 mA.
- **Op-amps** — LM741 (general-purpose, bipolar, ±15 V supply), LM358 (dual, single-supply 3–32 V, low power), TL072/TL082 (JFET input, low noise, ±15 V). From [semiconductor devices](../silicon/basic-devices.md).
- **Passive components** — E12 resistor assortment, ceramic/electrolytic capacitors, and 555 timer (NE555 or LM555) from [passive components](passive-components.md).

### Tools and Equipment

- DC bench supply (0–30 V dual) from [Electrical Systems](electrical-systems.md).
- Oscilloscope (dual-channel, ≥20 MHz) for observing waveforms, measuring gain, and characterizing frequency response.
- Signal generator (sine/square/triangle, 10 Hz–1 MHz) for amplifier and filter characterization.
- Digital multimeter for DC bias-point verification.

### Knowledge

- [Circuit fundamentals](circuit-fundamentals.md) — Ohm's law, Kirchhoff's laws, Thévenin equivalents, reactance and impedance. Every analog circuit is analyzed with these tools.
- Transistor biasing math — solving the quiescent operating point (Q-point) from the load line and the bias network.

## Bill of Materials

| Component | Quantity (per lab station) | Source | Alternatives |
|-----------|---------------------------|--------|--------------|
| LM741 op-amp (8-pin DIP) | 5 | [Semiconductor devices](../silicon/basic-devices.md) | LM358 (single-supply), TL072 (low-noise) |
| LM358 dual op-amp (8-pin DIP) | 5 | [Semiconductor devices](../silicon/basic-devices.md) | LM324 (quad single-supply) |
| TL072 dual op-amp (JFET input) | 5 | [Semiconductor devices](../silicon/basic-devices.md) | TL082, LF353 |
| 2N3904 NPN transistor | 10 | [Semiconductor devices](../silicon/basic-devices.md) | 2N2222 (higher current), BC547 |
| 2N3906 PNP transistor | 10 | [Semiconductor devices](../silicon/basic-devices.md) | 2N2907, BC557 |
| IRF510 N-channel MOSFET | 3 | [Semiconductor devices](../silicon/basic-devices.md) | IRLZ44N (logic-level gate) |
| 1N4148 small-signal diode | 20 | [Semiconductor devices](../silicon/basic-devices.md) | 1N914 |
| NE555 timer (8-pin DIP) | 5 | [Semiconductor devices](../silicon/basic-devices.md) | LM555, TLC555 (CMOS, low power) |
| Resistor assortment (E12, ¼ W) | 5 each value | [Passive components](passive-components.md) | E24 1% metal-film for precision gain |
| Capacitor assortment (10 pF–1000 μF) | 3 each value | [Passive components](passive-components.md) | Film caps for low-leakage timing |
| 8-pin DIP IC sockets | 20 | [Passive components](passive-components.md) | Solder ICs directly (not recommended for prototyping) |
| Solderless breadboard (830 tie-points) | 1 | [Electrical Systems](electrical-systems.md) | Perfboard + solder |

## Process Description

### Step 1: Transistor Switch Circuits

Build an NPN common-emitter switch driving an LED or relay coil. Compute the base resistor: R_base = (V_drive − 0.7 V) / (I_C / h_FE), with I_C set by the load (e.g., 20 mA for an LED) and h_FE from the transistor datasheet (minimum 100 for 2N3904). Drive the base hard (forced beta of 10–20× the actual I_C) to ensure saturation, where V_CE(sat) ≈ 0.2 V. Verify: when on, V_CE should read <0.3 V; when off, V_CE = V_CC. *(Deep article: [transistor-switch-circuits](analog-circuits.transistor-switch-circuits.md))*

### Step 2: Amplifier Fundamentals — Small-Signal Biasing

Build a common-emitter amplifier with voltage-divider bias. Set the Q-point at V_CE ≈ V_CC/2 for maximum symmetric swing. Choose R1/R2 divider current at 10× the base current to make bias independent of h_FE. Compute the AC voltage gain: A_v = −g_m · R_C (unbypassed emitter resistor reduces gain to A_v ≈ −R_C / R_E). Verify by injecting a 1 kHz sine (10 mV peak) at the base and measuring the output amplitude on the oscilloscope. *(Deep article: [amplifier-fundamentals](analog-circuits.amplifier-fundamentals.md))*

### Step 3: Op-Amp Closed-Loop Topologies

Build the three canonical op-amp circuits with an LM741 or TL072:
- **Inverting**: A_v = −R_f/R_in. Use R_in = 10 kΩ, R_f = 100 kΩ for A_v = −10. The (−) input is a virtual ground.
- **Non-inverting**: A_v = 1 + R_f/R_in. Use R_in = 10 kΩ, R_f = 100 kΩ for A_v = +11.
- **Voltage follower**: A_v = 1. Wire output directly to (−) input. Tests buffer action — output tracks input with near-zero output impedance.

Verify each gain at 1 kHz; confirm the output is undistorted (a clean sine on the scope). Increase frequency until gain drops 3 dB (−0.707 of low-frequency gain) to find the bandwidth. *(Deep article: [op-amp-circuits](analog-circuits.op-amp-circuits.md))*

### Step 4: Active Filters

Build a first-order low-pass filter (RC + op-amp buffer) with cutoff f_c = 1/(2πRC). With R = 16 kΩ and C = 1 nF, f_c ≈ 10 kHz. Characterize by sweeping the generator from 100 Hz to 100 kHz and plotting output amplitude vs frequency. Extend to a second-order Sallen-Key low-pass (Q = 0.707 for Butterworth response). *(Cross-reference: [filter-circuits](power-supply-circuits.filter-circuits.md))*

### Step 5: Oscillators and Timers

Build a Wien-bridge oscillator (op-amp + RC lead-lag network) at 1 kHz — verify the Barkhausen criterion (loop gain ≥ 1, phase shift = 0°). Then build a 555 astable with R1 = 10 kΩ, R2 = 47 kΩ, C = 100 nF: f = 1.44/((R1 + 2·R2)·C) ≈ 130 Hz. Measure frequency on the scope and compare to the formula. *(Deep articles: [oscillator-circuits](analog-circuits.oscillator-circuits.md), [timer-circuits](analog-circuits.timer-circuits.md))*

## Quantitative Parameters

### Real Op-Amp Comparison

| Parameter | LM741 | LM358 | TL072 |
|-----------|-------|-------|-------|
| Open-loop gain (A_OL) | 200 000 (106 dB) | 100 000 (100 dB) | 200 000 (106 dB) |
| Input impedance | 2 MΩ (bipolar) | High (bipolar, ~1 MΩ) | 10¹² Ω (JFET) |
| Input bias current | 80 nA | 40 nA | 65 pA |
| Input offset voltage | 1 mV (typ), 5 mV (max) | 2 mV (typ), 7 mV (max) | 3 mV (typ), 10 mV (max) |
| Gain-bandwidth product | 1 MHz | 1 MHz | 3 MHz |
| Slew rate | 0.5 V/µs | 0.5 V/µs (rising), 0.3 V/µs (falling) | 13 V/µs |
| Supply voltage range | ±5 V to ±18 V | 3 V to 32 V (or ±1.5 to ±16) | ±5 V to ±18 V |
| Quiescent current (per amp) | 1.7 mA | 0.5 mA | 1.4 mA |
| Noise (input voltage) | Not specified (bipolar, ~20 nV/√Hz) | 40 nV/√Hz @ 1 kHz | 18 nV/√Hz @ 1 kHz |
| Packages | 8-pin DIP/SOIC | 8-pin DIP/SOIC (dual) | 8-pin DIP/SOIC (dual) |
| Best use | General-purpose, teaching | Single-supply, battery, low power | Audio, low-noise, JFET input |

### Key Analog Design Equations

| Circuit | Parameter | Formula | Example |
|---------|-----------|---------|---------|
| Inverting amp | Voltage gain | A_v = −R_f / R_in | R_f=100k, R_in=10k → A_v = −10 |
| Non-inverting amp | Voltage gain | A_v = 1 + R_f/R_in | R_f=100k, R_in=10k → A_v = +11 |
| Voltage follower | Gain | 1 | Buffer; Z_out ≈ 0 |
| Common-emitter (unbypassed R_E) | Voltage gain | A_v ≈ −R_C / R_E | R_C=4.7k, R_E=470 → A_v = −10 |
| Common-collector (emitter follower) | Current gain | h_FE (transistor β) | 50–300 for 2N3904 |
| First-order low-pass filter | Cutoff frequency | f_c = 1/(2πRC) | R=16k, C=1nF → f_c ≈ 10 kHz |
| 555 astable | Frequency | f = 1.44 / ((R1+2R2)·C) | R1=10k, R2=47k, C=100nF → f ≈ 130 Hz |
| Wien-bridge oscillator | Frequency | f = 1/(2πRC) | R=16k, C=10nF → f ≈ 1 kHz |
| Colpitts oscillator | Frequency | f = 1/(2π√(L·C_series)) | C_eq = C1·C2/(C1+C2) |
| Full-power bandwidth | f_p | SR / (2π·V_peak) | SR=0.5V/µs, V_peak=10V → f_p ≈ 8 kHz |

## Scaling Notes

Analog circuits scale from single-op-amp breadboard prototypes to thousand-transistor monolithic ICs. The governing equations do not change, but the dominant constraints shift:

- **Bench scale**: single op-amps, ±15 V supplies, through-hole DIP packages, ¼ W resistors. Bandwidth limited by op-amp GBW (1 MHz for LM741 → 100 kHz at gain 10) and breadboard parasitics (~2 pF between adjacent rows).
- **Instrumentation scale**: low-noise JFET op-amps (TL072, OP07), precision resistors (0.1%), ground-plane PCBs. Noise floor drops from millivolts to microvolts. Essential for [sensor signal conditioning](interface-circuits.sensor-circuits.md).
- **Power scale**: [power amplifiers](analog-circuits.power-amplifiers.md) deliver watts to hundreds of watts. Heat dissipation (P = V·I) forces Class AB or Class D topologies; efficiency (η = P_out/P_dc) replaces voltage gain as the figure of merit.
- **Integration scale**: hundreds of op-amps on one die (active-filter arrays, analog computers). Matching between components on the same die (~0.1%) is far better than discrete — this is why monolithic filters achieve precision impossible with separate parts.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Op-amp output stuck at rail (±13 V on ±15 V supply) | No negative feedback (R_f open), or input exceeds common-mode range, or gain is set so high the input offset saturates the output | Check R_f continuity; verify inputs are within common-mode range (LM741: within ±12 V on ±15 V supply); reduce gain or add offset-null trim |
| Oscillation in op-amp circuit (output shows high-frequency sine at unity gain) | Unintended feedback via supply rails (poor decoupling), or capacitive load (>100 pF) with high-impedance feedback | Add 100 nF ceramic decoupling capacitor directly across supply pins (4 and 7) to ground; add 50–100 Ω output isolation resistor for capacitive loads |
| Transistor amplifier output clipped on one side | Q-point not centered (V_CE too close to V_CC or 0 V) | Re-bias: adjust R1/R2 divider so V_CE ≈ V_CC/2 at quiescent; verify h_FE and recompute bias currents |
| 555 astable frequency wrong by >10% | Electrolytic timing capacitor tolerance (−20%/+80%), or timing resistor tolerance | Use film or ceramic (C0G/NP0) capacitor for timing; verify R1, R2 with DMM; LM555 tolerance is ~1–5% |
| Wien-bridge oscillator won't start | Loop gain < 1 at startup (Barkhausen not satisfied) | Increase gain above unity — add a small-signal lamp (classic Wien) or AGC (JFET as variable resistor) to stabilize amplitude |
| Excessive noise / hum in audio amplifier | 50/60 Hz mains pickup via ground loops, unshielded input leads, or poor supply decoupling | Star-ground the supply returns; use shielded coax for low-level signals; add 100 µF + 100 nF decoupling at each op-amp supply pin |

## Safety

- **Op-amp supply voltage**: Exceeding the maximum rated supply (±18 V for LM741/LM358, ±22 V absolute max) destroys the IC. Verify supply polarity and magnitude before inserting the op-amp. Reverse polarity (−15 V on V+ pin) causes immediate failure.
- **Power-transistor heat**: A TO-92 2N3904 dissipating >0.5 W overheats; a TO-220 MOSFET without a heatsink dissipating >1 W overheats. Compute P = V_DS · I_D; add heatsink (thermal resistance <10 °C/W) for any device above 1 W continuous.
- **Capacitor discharge**: Filter capacitors charged to >25 V deliver a skin-penetrating shock. Discharge through a bleeder resistor (1 kΩ, 1 W) before touching the circuit.
- **High-frequency RF**: Oscillators above 1 MHz emit EMI that can interfere with nearby instruments. Keep leads short; use a ground plane.

## Quality Control

### Acceptance Criteria

- Measured op-amp gain within ±5% of R_f/R_in for the inverting amplifier (limited by resistor tolerance).
- Output undistorted sine wave: THD < 1% at 1 kHz (verify on oscilloscope — a clean sine with no flattening at peaks).
- Bandwidth: 3-dB frequency within ±10% of 1/(2πRC) for first-order filters, or within the specified f_c for second-order stages.
- Oscillator frequency within ±5% of calculated (limited by component tolerance); amplitude stable over 1 minute of observation.

### Testing Methods

- Measure gain at multiple frequencies (100 Hz, 1 kHz, 10 kHz, 100 kHz) to plot the frequency response.
- Sine-wave injection test: drive the amplifier with a clean 1 kHz sine and observe the output for clipping, crossover distortion (Class AB), or oscillation.
- Offset null: for precision applications, null the input offset voltage using the LM741 offset-null potentiometer (pins 1, 5) — adjust for 0 V output with input grounded.

## Variations and Alternatives

### Amplifier Class Comparison

| Class | Topology | Max efficiency | Conduction angle | Best for |
|-------|----------|---------------|-----------------|----------|
| A | Single transistor, always conducting | 25% (inductor load 50%) | 360° | Linear, low distortion, low power |
| B | Push-pull, each transistor conducts 180° | 78.5% | 180° | Power; has crossover distortion |
| AB | Push-pull with small idle bias | 50–60% | 190° | Audio — standard for Hi-Fi |
| D | PWM-switched MOSFETs | 90%+ | Switching | Battery-powered, high-power audio |

### Op-Amp Selection Guide

| Need | Choose | Why |
|------|--------|-----|
| Teaching, general-purpose | LM741 | Ubiquitous, documented, offset-null pins |
| Single-supply / battery | LM358 | Operates 3–32 V, ground-referenced inputs |
| Low-noise audio | TL072 | JFET input (65 pA bias), 18 nV/√Hz noise |
| High-frequency | LM6172 (100 MHz GBW) | Wide bandwidth, 3000 V/µs slew rate |
| Precision DC | OP07 | 10 µV offset, 0.2 µV/°C drift, chopper-stabilized |
| Rail-to-rail I/O | MCP6002 | Single-supply 1.8–6 V, inputs and output swing to rails |

### Oscillator Trade-offs

- **RC phase-shift / Wien-bridge**: Simple, frequency set by R and C, no inductor needed. Stability ~1% with good components. Best below 1 MHz.
- **LC (Colpitts, Hartley)**: Higher frequency (100 kHz–100 MHz), higher Q, better stability. Requires inductor.
- **Crystal (Pierce)**: Best stability (10–50 ppm), fixed frequency. Cannot tune significantly. Used for clocks and RF references. *(See [oscillator-circuits](analog-circuits.oscillator-circuits.md) and [rf-oscillator-circuits](communications-circuits.rf-oscillator-circuits.md).)*

### Transistor Configurations Comparison

| Configuration | Voltage gain | Current gain | Input impedance | Output impedance | Phase | Typical use |
|---------------|-------------|-------------|----------------|-----------------|-------|-------------|
| Common-emitter (CE) | High (−R_C/R_E) | h_FE | Medium (1–10 kΩ) | High (~R_C) | 180° | General amplifier |
| Common-collector (CC, emitter follower) | ≈1 | h_FE + 1 | High (10–100 kΩ) | Low (1/r_e) | 0° | Buffer, impedance matching |
| Common-base (CB) | High | ≈1 | Low (~r_e, 26 Ω) | High (~R_C) | 0° | RF / cascode |
| Common-source (MOSFET) | −g_m·R_D | ∞ (voltage-driven) | Very high (10¹² Ω) | High (~R_D) | 180° | High-input-Z amplifier |
| Common-drain (MOSFET source follower) | ≈1 | ∞ | Very high | Low | 0° | Buffer |
| Darlington (2× NPN cascade) | High | h_FE² (10 000+) | Very high | High | 0° (emitter follower variant) | High-gain, high-current drive |

### Frequency Response of Single-Stage Amplifier

A single CE amplifier stage has three frequency regions determined by coupling and bypass capacitors:

| Region | Frequency range | Gain behavior | Limiting element |
|--------|----------------|--------------|------------------|
| Low frequency | DC – f_L | Gain rises 20 dB/decade | Coupling/bypass capacitors (C_c, C_E) |
| Mid-band | f_L – f_H | Flat (maximum gain A_v) | Not limited — this is the usable band |
| High frequency | Above f_H | Gain falls −20 dB/decade | Transistor parasitics (C_cb, C_be) and GBW |

f_L ≈ 1/(2π·R_in·C_c) (coupling cap with input resistance). f_H ≈ GBW/A_v (gain-bandwidth product divided by mid-band gain). Example: LM741 with GBW = 1 MHz at gain 100 → f_H = 1 MHz/100 = 10 kHz. This is why high-gain op-amp stages need high-GBW parts.

## References

- [Semiconductor devices](../silicon/basic-devices.md) — diodes, BJTs, MOSFETs, op-amps, and the 555 timer.
- [Passive components](passive-components.md) — resistors, capacitors, inductors used in every analog circuit.
- [Circuit fundamentals](circuit-fundamentals.md) — Ohm's law, Kirchhoff's laws, impedance analysis.
- [Power supply circuits](power-supply-circuits.md) — rectifiers and regulators feed these analog stages.
- [Interface circuits](interface-circuits.md) — ADCs/DACs consume the op-amp comparator and active-filter techniques taught here.
- [Communications circuits](communications-circuits.md) — RF oscillators and receivers build on the amplifier fundamentals here.
- Deep articles: [diode-circuits](analog-circuits.diode-circuits.md), [transistor-switch-circuits](analog-circuits.transistor-switch-circuits.md), [amplifier-fundamentals](analog-circuits.amplifier-fundamentals.md), [power-amplifiers](analog-circuits.power-amplifiers.md), [op-amp-circuits](analog-circuits.op-amp-circuits.md), [multivibrator-circuits](analog-circuits.multivibrator-circuits.md), [oscillator-circuits](analog-circuits.oscillator-circuits.md), [timer-circuits](analog-circuits.timer-circuits.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
