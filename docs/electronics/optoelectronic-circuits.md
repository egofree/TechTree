# Optoelectronic Circuits

> **Node ID**: electronics.optoelectronic-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md)
> **Enables**: None
> **Timeline**: Years 25-50
> **Outputs**: optoelectronic-interface
> **Critical**: No — optoelectronic circuits extend electronics into light-based sensing, signaling, and isolation, but they are not on the minimum-viable bootstrap critical path

## Overview

Optoelectronic circuits convert between electrical energy and photons. Where [semiconductor devices](semiconductor-devices.md) exploit the behavior of charge carriers in solids for amplification and switching, optoelectronic circuits exploit the **emission** of light (LEDs, IR diodes, laser diodes) and the **absorption** of light (photodiodes, phototransistors, light-dependent resistors) to bridge the electrical and optical domains. The third family — **optocouplers** — uses an LED and a photodetector in one package to transfer signals across an isolation barrier with no galvanic connection.

The learning progression follows three stages, each adding one concept. **LED driver circuits** teach constant-current limiting: every LED is a current-controlled device, and the design challenge is setting the drive current precisely (R = (V_supply − V_f)/I_f for the simplest case, escalating to transistor current sources and dedicated driver ICs). **Photodetector circuits** teach transimpedance: converting the tiny photocurrent (nanoamps to microamps) into a usable voltage with an op-amp transimpedance amplifier (V_out = I_photo × R_feedback). **Optocoupler circuits** teach galvanic isolation: transferring a signal across a 5000 VAC barrier using light, characterized by the current transfer ratio (CTR = I_output / I_input).

Optoelectronic circuits are the foundation for isolated feedback in [switching power supplies](power-supply-circuits.switching-regulators.md), industrial sensing in [automation](../automation/index.md), fiber-optic and IR data links, and safety interlocks (light curtains). For the broader RF/wireless communications thread, see [communications circuits](communications-circuits.md).

## Prerequisites

### Materials

- **LEDs** — 5 mm (T-1¾) through-hole: red (620–625 nm, V_f = 1.8–2.0 V), green (520 nm, V_f = 2.0–2.2 V), blue (460–470 nm, V_f = 3.0–3.3 V), infrared (940 nm, V_f = 1.2 V). High-power white (350 mA, V_f = 3.3 V, 100+ lm). From [semiconductor devices](semiconductor-devices.md).
- **Photodiodes** — BPW34 (silicon PIN, 950 nm peak, 0.62 A/W responsivity, 20 ns response). From [semiconductor devices](semiconductor-devices.md).
- **Phototransistors** — BPV11 (NPN, 850 nm peak, collector current proportional to light). Slower than photodiodes (5 µs) but higher gain.
- **LDR (light-dependent resistor)** — GL5528 (CdS, 10 kΩ @ 10 lux, dark resistance 1 MΩ+). RoHS-restricted in some regions; use phototransistor where compliance matters.
- **Optocouplers** — 4N35 (general-purpose, CTR 50–600%, 5000 VAC isolation), 6N137 (high-speed, 10 MBd), PC817 (common, low-cost). From [semiconductor devices](semiconductor-devices.md).
- **Op-amps** — TL072 (low-noise for transimpedance), LM358 (single-supply). From [analog circuits](analog-circuits.md).
- **Resistors and capacitors** — E12 assortment from [passive components](passive-components.md).

### Tools and Equipment

- DC bench supply (0–30 V) from [Electrical Systems](electrical-systems.md).
- Digital multimeter (for LED forward voltage and photodiode dark current measurement).
- Oscilloscope (≥20 MHz) for switching-speed and pulse-response characterization.
- Optional: lux meter for absolute light output, or a second photodiode as a reference detector.

### Knowledge

- [Circuit fundamentals](circuit-fundamentals.md) — Ohm's law (current-limiting resistor calculation), RC filtering.
- [Analog circuits](analog-circuits.md) — op-amp transimpedance topology, transistor current sources, Schmitt trigger.

## Bill of Materials

| Component | Quantity (per lab station) | Source | Alternatives |
|-----------|---------------------------|--------|--------------|
| LED assortment (red, green, blue, IR, 5 mm) | 5 each | [Semiconductor devices](semiconductor-devices.md) | High-power 1 W white LED (350 mA) |
| BPW34 photodiode (silicon PIN, 950 nm) | 5 | [Semiconductor devices](semiconductor-devices.md) | BPW41N (higher speed) |
| BPV11 phototransistor (NPN) | 5 | [Semiconductor devices](semiconductor-devices.md) | TEPT5700 (ambient light) |
| GL5528 CdS LDR | 5 | [Semiconductor devices](semiconductor-devices.md) | Phototransistor (RoHS-compliant) |
| 4N35 optocoupler (DIP-6, CTR 50–600%) | 5 | [Semiconductor devices](semiconductor-devices.md) | PC817 (low-cost, same form factor) |
| 6N137 high-speed optocoupler (10 MBd) | 2 | [Semiconductor devices](semiconductor-devices.md) | HCPL-2531 (dual) |
| TL072 dual op-amp (for transimpedance) | 2 | [Semiconductor devices](semiconductor-devices.md) | LM358 (single-supply) |
| 2N3904 NPN transistor (for LED drivers) | 10 | [Semiconductor devices](semiconductor-devices.md) | 2N2222 (higher current), BC547 |
| Resistor assortment (E12, ¼ W) | 5 each value | [Passive components](passive-components.md) | 1% metal-film for precision transimpedance |
| Capacitor 100 nF ceramic | 20 | [Passive components](passive-components.md) | 1 µF for slower response |

## Process Description

### Step 1: LED Driver — Current-Limiting Resistor

The simplest LED circuit. Compute the series resistor: R = (V_supply − V_f) / I_f. For a red LED (V_f = 1.8 V) driven from 5 V at I_f = 10 mA: R = (5 − 1.8) / 0.01 = 320 Ω → use 330 Ω (E12). Verify: the measured V_f across the LED should be 1.8–2.0 V at the rated current; the resistor drops the remainder (5 − 1.9 = 3.1 V). Compute resistor power: P = I²·R = 0.01²·330 = 33 mW → ¼ W resistor is adequate.

**Critical**: LEDs are *current* devices. A 2 V LED directly across 5 V (no resistor) draws unlimited current and burns out in milliseconds. Never connect an LED without a current limiter.

*(Deep article: [led-driver-circuits](optoelectronic-circuits.led-driver-circuits.md))*

### Step 2: LED Driver — Transistor Constant Current

For multiple LEDs or higher current, use a transistor current source. An NPN (2N3904) with two diodes (1N4148) biasing the base at 1.4 V sets the emitter at 0.7 V; with R_E = 70 Ω, I_E = 0.7/70 = 10 mA — constant regardless of LED V_f variation or supply fluctuation. This drives 2–3 LEDs in series (each V_f ~2 V, total ~6 V) from a 12 V supply with stable current.

### Step 3: Photodiode Transimpedance Amplifier

Convert photocurrent to voltage with an op-amp transimpedance amplifier (TIA). Wire the photodiode reverse-biased (cathode to V+, anode to op-amp inverting input). The op-amp holds the anode at virtual ground; the photocurrent flows entirely through R_feedback. Output: V_out = −I_photo × R_f.

For R_f = 1 MΩ and I_photo = 1 µA (moderate indoor light on a BPW34): V_out = −1 V. Dark current (~2 nA on BPW34) produces only 2 mV offset. Add a small capacitor (1–10 pF) in parallel with R_f to prevent oscillation from the photodiode's junction capacitance.

*(Deep article: [photodetector-circuits](optoelectronic-circuits.photodetector-circuits.md))*

### Step 4: Phototransistor Light Switch

Build a light-activated switch: a phototransistor (BPV11) drives an NPN transistor (2N3904), which energizes a relay when the light exceeds a threshold. Set the threshold with a potentiometer in the base divider. The phototransistor replaces an LDR for higher speed and reliability. A dark-activated switch inverts the logic (NC contact).

### Step 5: Optocoupler Digital Isolation

Drive the LED side of a 4N35 optocoupler from a 5 V logic signal through a 220 Ω resistor (I_f = (5 − 1.2)/220 = 17 mA). The phototransistor on the isolated side pulls a 10 kΩ pull-up resistor to ground when the LED is on. With CTR = 100%, the phototransistor sinks 1.7 mA — more than enough to pull 10 kΩ to 5 V below the rail. The two grounds are separated by the 5000 VAC isolation barrier.

*(Deep article: [optocoupler-circuits](optoelectronic-circuits.optocoupler-circuits.md))*

### Step 6: PWM LED Dimming

Drive the LED from a microcontroller PWM pin through a transistor. At 200 Hz PWM with 8-bit resolution (0–255 duty cycle), the perceived brightness is proportional to duty cycle (human eye integrates above ~100 Hz). At 50% duty, the LED appears half-bright. This is the basis of [LED dimming](analog-circuits.timer-circuits.md) and matrix multiplexing.

## Quantitative Parameters

### LED Forward Voltage and Wavelength by Color

| LED color | Wavelength (nm) | V_f (typical @ 20 mA) | V_f range | Luminous intensity (5 mm LED) | Luminous efficacy |
|-----------|----------------|----------------------|-----------|------------------------------|-------------------|
| Infrared | 940 | 1.2 V | 1.0–1.5 V | Not visible (IR) | N/A (radiant) |
| Red | 620–625 | 1.85 V | 1.7–2.0 V | 5–20 mcd | 50–100 lm/W |
| Orange | 605 | 2.0 V | 1.9–2.2 V | 5–15 mcd | 50–100 lm/W |
| Yellow | 585–590 | 2.1 V | 1.9–2.3 V | 5–20 mcd | 50–100 lm/W |
| Green | 520–525 | 2.1 V | 1.9–2.4 V | 5–30 mcd | 60–120 lm/W |
| Blue | 460–470 | 3.2 V | 2.8–3.4 V | 5–20 mcd | 30–60 lm/W (older) |
| White (phosphor) | Broadband (450 + phosphor) | 3.3 V | 3.0–3.6 V | 5000–20000 mcd | 80–200 lm/W |
| UV (near) | 395–405 | 3.4 V | 3.2–3.8 V | Not visible | N/A (radiant) |

High-power white LEDs (1–100 W) achieve 100–200 lm/W at 350 mA–3 A drive current, but require thermal management (junction temperature <125 °C).

### Photodetector Comparison

| Device | Responsivity | Dark current | Response time | Best for |
|--------|-------------|-------------|---------------|----------|
| Photodiode (BPW34, PIN) | 0.62 A/W @ 950 nm | 2 nA @ 20 V reverse | 20 ns | Precision, high-speed |
| Phototransistor (BPV11) | Equivalent gain ×h_FE | 100 nA | 5 µs | Switching, simple (no TIA needed) |
| LDR (GL5528, CdS) | Non-linear (R varies) | N/A (R_dark ~1 MΩ) | 10–100 ms (slow) | Ambient light sensing (slow) |
| Solar cell (large photodiode) | 0.3–0.5 A/W | N/A (self-powered) | µs–ms | Energy harvesting |

### Optocoupler Key Parameters

| Optocoupler | CTR (min) | Isolation voltage | Bandwidth / data rate | LED current | Best for |
|-------------|-----------|-------------------|----------------------|-------------|----------|
| 4N35 | 50% (@ 10 mA LED) | 5000 VAC | ~300 kHz | 10–20 mA | General-purpose, low-speed |
| PC817 | 50% (@ 5 mA) | 5000 VAC | ~80 kHz | 5–20 mA | Low-cost, opto-isolated feedback |
| 6N137 | Not applicable (logic out) | 5000 VAC | 10 MBd | 5 mA | High-speed digital isolation |
| HCPL-2531 | Not applicable (logic out) | 3750 VAC | 1 MBd (dual) | 5 mA | Bidirectional digital |
| MOC3020 (triac driver) | N/A (triac out) | 7500 VAC | Zero-crossing | 15 mA | AC mains triac drive (solid-state relay) |
| AMC1200 (analog isolation) | Linear (gain 1) | 4250 VAC | 100 kHz (analog) | N/A (differential in) | Isolated current/voltage sensing |

### LED Current-Limiting Resistor Values

| Supply voltage | Red LED (V_f = 1.8 V) @ 10 mA | Green LED (V_f = 2.1 V) @ 10 mA | Blue/White LED (V_f = 3.3 V) @ 10 mA | High-power white (V_f = 3.3 V) @ 350 mA |
|---------------|------------------------------|-------------------------------|-------------------------------------|---------------------------------------|
| 3.3 V | 150 Ω | 120 Ω | 0 Ω (needs boost) | N/A (needs driver) |
| 5 V | 330 Ω | 300 Ω | 180 Ω | 5.7 Ω (3 W) |
| 9 V | 750 Ω | 680 Ω | 560 Ω | 16 Ω (3 W) |
| 12 V | 1 kΩ | 1 kΩ | 820 Ω | 25 Ω (5 W) |
| 24 V | 2.2 kΩ | 2.2 kΩ | 2 kΩ | 56 Ω (10 W) |

Formula: R = (V_supply − V_f) / I_f. Power rating: P_R = I²·R; use at least 2× margin.

## Scaling Notes

- **Indicator scale**: a single 5 mm LED at 10 mA on a breadboard. The default teaching build. Total power <0.1 W.
- **Backlight / matrix scale**: 8×8 LED matrix multiplexed at 1/8 duty cycle. Drive each LED at 8× the rated peak current (e.g., 80 mA for 10 mA rated average) for 1/8 of the time. Requires transistor drivers and microcontroller scanning. Total power ~1–2 W.
- **Illumination scale**: 1–10 W high-power white LED at 350 mA–3 A. Requires a constant-current driver (buck topology, [switching regulators](power-supply-circuits.switching-regulators.md)) and a heatsink (junction must stay below 125 °C — thermal resistance budget ~10 °C/W for a 5 W LED). Luminous flux 100–1000 lm.
- **Isolation barrier scale**: optocoupled feedback in an offline switching supply. The optocoupler (PC817) closes the regulation loop across the 5000 VAC isolation barrier between primary (mains) and secondary (low-voltage output). Bandwidth (~80 kHz) limits the control loop crossover to ~5–8 kHz.
- **Bottleneck at scale**: high-power LED efficiency drops at elevated junction temperature (−0.3%/°C above 25 °C) and at high drive current (efficiency droop above rated current). Thermal management dominates the design above 5 W per LED.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| LED too dim | Current-limiting resistor too large, or LED V_f higher than assumed | Measure V_f at rated current; recompute R = (V_supply − V_f)/I_f; verify supply voltage under load |
| LED burned out instantly | No current-limiting resistor, or supply connected reverse for prolonged time | Always include a series resistor; verify polarity (anode = longer lead, flat side = cathode) |
| Photodiode reading is noisy | Ambient 50/60 Hz hum coupling, or op-amp noise, or insufficient shielding | Shield the photodiode in a light-tight enclosure; use shielded cable; add 1–10 pF feedback cap in the TIA; verify op-amp is low-noise (TL072, not LM741) |
| Phototransistor switch oscillates at threshold | No hysteresis (relay chatters as light crosses threshold) | Add Schmitt trigger (op-amp with positive feedback, 5–10% hysteresis); use a second transistor as a latch |
| Optocoupler output not toggling | LED drive current too low (below min CTR), or output pull-up too strong | Measure LED current; ensure ≥5 mA for PC817/4N35; increase pull-up resistor (10 kΩ → 47 kΩ); verify CTR (may have aged — optocoupler LEDs dim) |
| Optocoupler response too slow | Saturated phototransistor (storage time), or high pull-up resistor (RC with junction capacitance) | Use a pull-up <10 kΩ; add a base-emitter resistor to bleed stored charge; switch to 6N137 (logic-output, fast) |
| High-power LED overheats | Inadequate heatsink (junction exceeds 125 °C) | Compute P = V_f × I_f = 3.3 × 0.35 = 1.2 W (for a 1 W LED); add heatsink with θ < (125 − T_amb)/P = 80 °C/W; use thermal pad |

## Safety

- **High-power LED eye hazard**: A 1 W white LED at close range exceeds the 10 mW/cm² retinal exposure limit (IEC 62471). Do not look directly at high-power LEDs. Diffuse the beam or install behind a cover.
- **Laser diode hazard**: Laser diodes (even 5 mW, class 3R) cause permanent retinal damage before the blink reflex (~0.25 s). Use proper beam stops and interlocks. Class 3B (>5 mW) requires key control and emission indicators.
- **IR LED invisibility**: IR LEDs (940 nm) emit no visible light — the operator cannot see whether they are on. Use a digital camera (which sees near-IR) to verify operation. Do not assume an IR LED is off just because it appears dark.
- **Optocoupler mains isolation**: When an optocoupler (MOC3020) drives a triac on AC mains, the LED side is at logic potential (safe) but the triac side is at mains potential (lethal). Maintain 8 mm creepage/clearance between the two sides on the PCB. Do not exceed the optocoupler's rated isolation (5000–7500 VAC peak).
- **UV LED skin/eye exposure**: UV LEDs (395 nm and shorter) cause photokeratitis (welder's flash) and accelerate skin aging. Use UV-blocking safety glasses when working with UV LEDs above 1 mW radiant output.

## Quality Control

### Acceptance Criteria

- LED forward voltage within datasheet range at the rated current (e.g., 1.8–2.0 V for red at 20 mA). Reject LEDs outside the range — they may be counterfeit or from a different batch.
- Optocoupler CTR within datasheet range (50–600% for 4N35 at 10 mA LED current). CTR varies widely between units — design for the minimum.
- Photodiode dark current below datasheet maximum (2 nA for BPW34 at 20 V reverse). Excessive dark current indicates a leaky or damaged device.
- Optocoupler isolation tested at 5000 VAC for 1 minute (dielectric withstand). This is a production-line test; do not repeat it on a used optocoupler.

### Testing Methods

- LED V_f test: drive at rated current; measure V_f with DMM. Bins by V_f are sold commercially.
- Photodiode responsivity: illuminate with a calibrated light source (or compare to a reference photodiode); measure photocurrent. Compare to datasheet A/W.
- Optocoupler CTR test: drive LED at 5 mA; measure phototransistor collector current at 5 V V_CE. CTR = I_C / I_LED × 100%.

## Variations and Alternatives

### Photodetection Strategy Selection

| Sensor | Sensitivity | Speed | Complexity | Best for |
|--------|------------|-------|-----------|----------|
| Photodiode + TIA | High (µA range) | Fast (ns) | High (op-amp needed) | Precision, instrumentation, fiber-optic |
| Phototransistor | Moderate (mA range) | Slow (µs) | Low (one resistor) | Switching, presence detection |
| LDR (CdS) | Low (non-linear) | Very slow (ms) | Lowest (one resistor) | Ambient light, day/night switch |
| Photodiode (solar cell mode) | High (zero-bias, self-powered) | Moderate | Low | Energy harvesting, low-power |

### Optocoupler vs Digital Isolator

| Parameter | Optocoupler (4N35/PC817) | Digital isolator (ADuM1201) |
|-----------|------------------------|----------------------------|
| Isolation voltage | 5000 VAC | 5000 VAC |
| Data rate | <300 kHz (general), 10 MBd (6N137) | 100 Mbit/s |
| Propagation delay | 2–5 µs (general), 75 ns (6N137) | 15–30 ns |
| LED wear | Yes (CTR drops 50% in 50 000 hr) | No (no LED) |
| Power consumption | 5–20 mA per channel (LED drive) | 1–3 mA per channel |
| Cost | $0.20–1.00 | $2.00–5.00 |
| Best for | Low-cost, low-speed, feedback loops | High-speed digital (SPI, RS-485) |

Modern designs use digital isolators (capacitive or magnetic) for speed-critical isolation and optocouplers only for cost-sensitive or analog-isolation applications.

## References

- [Semiconductor devices](semiconductor-devices.md) — LEDs, photodiodes, phototransistors, optocouplers.
- [Analog circuits](analog-circuits.md) — op-amp transimpedance amplifier, transistor current sources, Schmitt trigger.
- [Circuit fundamentals](circuit-fundamentals.md) — Ohm's law for current-limiting resistors, RC filtering.
- [Power supply circuits](power-supply-circuits.md) — optocoupled feedback in [switching regulators](power-supply-circuits.switching-regulators.md).
- [Communications circuits](communications-circuits.md) — IR and fiber-optic data links.
- Deep articles: [led-driver-circuits](optoelectronic-circuits.led-driver-circuits.md), [photodetector-circuits](optoelectronic-circuits.photodetector-circuits.md), [optocoupler-circuits](optoelectronic-circuits.optocoupler-circuits.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
