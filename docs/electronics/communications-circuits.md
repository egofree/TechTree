# Communications Circuits

> **Node ID**: electronics.communications-circuits
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md), [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Timeline**: Years 25-50
> **Outputs**: communication-circuit-design
> **Critical**: No — communications circuits extend electronics into wireless and wired information transfer, but they are not on the minimum-viable bootstrap critical path

## Overview

Communications circuits transmit and receive information by impressing a signal onto a carrier. This capability owns the **Tesla-era AC/RF lineage** — the thread that begins with resonant transformers (Tesla coils), radio-frequency tuning, and runs through the Forrest Mims III *Communications Projects* to modern modulation, oscillator, and receiver design. It is the design-pedagogy hub, not a deep article.

The Tesla grounding matters because RF is an AC phenomenon: resonant LC circuits, impedance, and phase — the tools of [AC circuit analysis](circuit-fundamentals.ac-analysis.md) — are what make a tuned circuit select one station out of the ether. Every radio receiver is, at its core, a Tesla-era resonant tank circuit followed by a detector.

The family follows the signal chain of a communications link: **modulation** (impress information onto a carrier — AM, FM, or digital), **RF oscillator** (generate the carrier itself — LC, crystal, or PLL), and **receiver** (select, amplify, and detect the signal — tuned RF, superheterodyne, AGC). This covers enough to build a working AM/FM receiver, a simple transmitter, and a wired serial data link using RS-232, RS-485, or CAN bus.

This capability stays at the **Forrest Mims III / introductory level**. It does not cover Smith charts, impedance-matching network synthesis, phased-array and beamforming antenna systems, advanced digital modulation (QAM, PSK constellations), or software-defined radio (SDR). Those belong to a specialized RF engineering track beyond the bootstrap horizon.

## Prerequisites

### Materials

- **Transistors for RF** — 2N3904 (general NPN, f_T = 300 MHz, usable to ~100 MHz), 2N2222 (f_T = 250 MHz), or BF494 (RF-specific, f_T = 120 MHz). From [semiconductor devices](semiconductor-devices.md).
- **RF diodes** — 1N60 or 1N34A (germanium point-contact, low V_f = 0.3 V for envelope detection), 1N4148 (silicon, higher V_f = 0.7 V but faster).
- **Variable capacitors** — 10–365 pF polyvaricon (for AM radio tuning). From [passive components](passive-components.md).
- **Inductors** — ferrite rod antenna (for AM broadcast), hand-wound air-core coils on PVC forms (for shortwave), 455 kHz / 10.7 MHz IFT (intermediate-frequency transformers) for superheterodyne receivers.
- **Crystals** — 10 MHz, 16 MHz HC-49 (for crystal oscillators and PLL references). From [passive components](passive-components.md).
- **Interface ICs** — MAX232 (RS-232 line driver/receiver), MAX485 (RS-485 transceiver), MCP2515 (CAN controller). From [semiconductor devices](semiconductor-devices.md).
- **Op-amp / LM386** — audio power amplifier (250 mW, for receiver audio stage). From [analog circuits](analog-circuits.md).

### Tools and Equipment

- Oscilloscope (≥20 MHz, ideally 100 MHz) for observing RF waveforms and modulation envelopes.
- Signal generator (100 kHz–30 MHz, AM/FM capable) for receiver alignment.
- Frequency counter (for crystal oscillator calibration).
- DMM for DC bias verification.

### Knowledge

- [Circuit fundamentals](circuit-fundamentals.md) — AC reactance (X_C, X_L), impedance, resonance (f₀ = 1/2π√(LC)), Q factor.
- [Analog circuits](analog-circuits.md) — transistor amplifier biasing, oscillator circuits (Colpitts, Hartley, Wien bridge).
- Decibels (dB): power ratio (10·log₁₀(P₁/P₀)); voltage ratio (20·log₁₀(V₁/V₀)).

## Bill of Materials

| Component | Quantity (per AM receiver build) | Source | Alternatives |
|-----------|--------------------------------|--------|--------------|
| Ferrite rod antenna (10 cm, 550–1700 kHz) | 1 | [Passive components](passive-components.md) | External wire antenna + external inductor |
| Variable capacitor (10–365 pF, polyvaricon) | 1 | [Passive components](passive-components.md) | Varactor diode (1N4007, voltage-tuned) |
| 1N34A germanium diode (envelope detector) | 2 | [Semiconductor devices](semiconductor-devices.md) | 1N60 (schottky); 1N4148 (silicon, higher loss) |
| 2N3904 NPN transistor (RF amplifier) | 3–5 | [Semiconductor devices](semiconductor-devices.md) | 2N2222, BF494 (RF) |
| 455 kHz IFT (intermediate-frequency transformer) | 3 | [Passive components](passive-components.md) | 10.7 MHz IFT (for FM receiver) |
| LM386 audio amplifier IC (DIP-8) | 1 | [Semiconductor devices](semiconductor-devices.md) | Discrete transistor audio stage |
- 10 kΩ volume potentiometer, log taper | 1 | [Passive components](passive-components.md) | Linear taper (less ideal for audio) |
| 8 Ω speaker or 32 Ω headphone | 1 | [Electrical systems](electrical-systems.md) | Piezo buzzer (lower quality) |
| Resistor assortment (E12, ¼ W) | 5 each value | [Passive components](passive-components.md) | 1% metal-film for tuned stages |
| Capacitor assortment (10 pF–1 µF) | 3 each value | [Passive components](passive-components.md) | Silver-mica for stable RF |

## Process Description

### Step 1: Build a Crystal Radio (Simplest Receiver)

The simplest possible receiver: a tuned LC circuit (selects the station) followed by a diode detector (rectifies the RF envelope) and a high-impedance earphone. No power supply required — the received signal powers the earphone directly.

1. Wind ~60 turns of enamelled wire on a ferrite rod (or cardboard tube, 10 cm). This is the antenna inductor L. Tap every 10 turns for impedance matching.
2. Connect a variable capacitor (10–365 pF) across L. The resonant frequency: f₀ = 1/(2π√(LC)). With L = 240 µH and C = 365 pF → f₀ ≈ 540 kHz (bottom of AM band). With C = 10 pF → f₀ ≈ 1027 kHz. This tunes the 540–1700 kHz AM broadcast band.
3. Connect a 1N34A germanium diode (low V_f = 0.3 V is essential — silicon's 0.7 V would block weak stations) from the top of the tank to ground.
4. Connect a 100 pF capacitor and a crystal earpiece (or 47 kΩ + audio transformer for low-impedance headphones) across the detector output.
5. Ground the circuit to a cold-water pipe or earth stake.

**Expected**: with a good antenna (10 m wire) and ground, you should hear the strongest local AM station. Range is typically 10–50 km for a clear-channel station at night. *(Deep article: [receiver-circuits](communications-circuits.receiver-circuits.md))*

### Step 2: Build an RF Oscillator (Colpitts)

Generate a carrier with a Colpitts oscillator: a 2N3904 with an LC tank in the collector circuit and a capacitive divider (C1, C2) feeding the emitter. The Barkhausen criterion requires loop gain ≥ 1 and phase shift = 0°. Choose L and C_total = C1·C2/(C1+C2) for the desired frequency.

For a 1 MHz oscillator: L = 100 µH, C_total = 253 pF → C1 = 560 pF, C2 = 470 pF (C_total = 255 pF). Verify the output on the oscilloscope — a clean 1 MHz sine at ~1 V peak. Coupling a keyed audio tone into the base produces an AM-modulated CW (Morse) transmitter. *(Deep article: [rf-oscillator-circuits](communications-circuits.rf-oscillator-circuits.md))*

### Step 3: AM Modulation and Demodulation

Modulate the oscillator's amplitude by injecting an audio signal (1 kHz, 100 mV) into the transistor base through a coupling capacitor. The output amplitude varies with the audio — this is amplitude modulation (AM). The modulation index m = (V_max − V_min)/(V_max + V_min) should stay below 1 (100%) to avoid distortion.

Demodulate with the crystal-radio detector: the diode rectifies the RF, and the RC filter (100 pF) removes the carrier, leaving the audio envelope. *(Deep article: [modulation-circuits](communications-circuits.modulation-circuits.md))*

### Step 4: Superheterodyne Receiver (Introductory)

Build the standard receiver architecture invented by Edwin Armstrong (1918):
1. **RF amplifier**: one or two tuned stages amplify the desired station.
2. **Mixer**: combine the received RF with a local oscillator (LO) offset by the intermediate frequency (IF). For AM broadcast, IF = 455 kHz. The LO tunes from 995–2155 kHz to receive 540–1700 kHz (LO = RF + IF).
3. **IF amplifier**: 2–3 tuned stages at 455 kHz, providing most of the receiver's gain and selectivity. Fixed-tuned IFTs make the filter shape precise.
4. **Detector**: germanium diode envelope detector (as in Step 1) recovers the audio.
5. **Audio amplifier**: LM386 (gain 20–200) drives a speaker.
6. **AGC**: feed the detector DC level back to the IF amplifier to reduce gain on strong signals — automatic gain control.

### Step 5: Wired Serial Communication (RS-232, RS-485, CAN)

For wired digital communication:
- **RS-232** (point-to-point, ±12 V levels, MAX232 level shifter): connect two devices at up to 115.2 kbaud over <15 m. The standard serial port protocol (start bit, 8 data bits, optional parity, stop bit).
- **RS-485** (differential, multi-drop, MAX485 transceiver): connect up to 32 devices on a twisted-pair bus at up to 10 Mbaud over 1.2 km. Differential signaling rejects common-mode noise.
- **CAN bus** (MCP2515 controller + transceiver): automotive-grade multi-master bus at up to 1 Mbaud. Built-in error detection and arbitration.

## Quantitative Parameters

### Wired Serial Protocol Comparison

| Parameter | RS-232 | RS-485 | CAN bus | I²C | SPI |
|-----------|--------|--------|---------|-----|-----|
| Signaling | Single-ended | Differential | Differential | Single-ended | Single-ended |
| Voltage levels | ±3 to ±15 V (±12 V typ) | ±2 V differential (A−B) | ±2 V differential (CAN_H−CAN_L) | 0–Vcc (3.3/5 V) | 0–Vcc |
| Max data rate | 115.2 kbaud (classic) | 10 Mbaud | 1 Mbaud (40 m), 50 kbaud (1 km) | 3.4 MHz (HS) | 50 MHz |
| Max distance | 15 m | 1.2 km (at 100 kbaud) | 1 km (at 50 kbaud) | 1 m | 0.3 m |
| Max nodes | 1 (point-to-point) | 32 (standard), 256 (extended) | 110 (standard), 247 (extended) | 127 (7-bit addr) | 1 master, N slaves |
| Topology | Point-to-point | Daisy chain (bus) | Bus (multi-master) | Multi-drop (bus) | Star (master-slave) |
| Noise immunity | Low (single-ended) | High (differential) | High (differential) | Low (short range) | Low (short range) |
| Typical use | PC serial, modem legacy | Industrial multi-drop | Automotive, industrial | Board-level sensors | Board-level fast peripherals |

### AM / FM Modulation Comparison

| Parameter | AM (amplitude modulation) | FM (frequency modulation) |
|-----------|-------------------------|--------------------------|
| What varies with signal | Carrier amplitude | Carrier frequency |
| Modulation index (m) | 0 to 1 (100%); >1 = distortion | β = Δf/f_signal (no hard limit) |
| Bandwidth | 2 × f_signal_max (both sidebands) | 2 × (Δf + f_signal) (Carson's rule) |
| Noise immunity | Low (noise adds to amplitude) | High (amplitude limiters reject noise) |
| Audio quality | 3 kHz max (AM broadcast) | 15 kHz (FM broadcast) |
| Carrier freq (broadcast) | 540–1700 kHz | 88–108 MHz |
| IF frequency | 455 kHz | 10.7 MHz |
| Power efficiency | 33% (DSB-SC: 50%) | Constant envelope → 100% (class C PA) |
| Receiver complexity | Simple (envelope detector) | Complex (limiter + discriminator / PLL) |

### RF Oscillator Comparison

| Oscillator | Frequency range | Stability | Phase noise | Best for |
|-----------|----------------|-----------|------------|----------|
| RC phase-shift | 1 Hz–100 kHz | Poor (1% drift) | High | Audio, low frequency |
- Wien-bridge (RC) | 1 Hz–1 MHz | Medium (0.1%) | Medium | Audio sine (low distortion) |
- LC (Colpitts, Hartley) | 100 kHz–500 MHz | Medium (0.01–0.1%) | Low-Medium | RF carriers (general) |
- Crystal (Pierce) | 1–100 MHz | Excellent (10–50 ppm) | Very low | Frequency references, clocks |
- PLL (phase-locked loop) | DC–GHz | Crystal-derived | Low | Tunable RF (synthesizer) |
- DDS (direct digital) | DC–500 MHz | Crystal-derived | Low | Programmable frequency, SDR |

### Receiver Selectivity and Sensitivity Benchmarks

| Receiver type | Sensitivity (min detectable) | Selectivity (adjacent rejection) | IF bandwidth | Complexity |
|---------------|-----------------------------|--------------------------------|--------------|-----------|
| Crystal radio | ~1 mV/m (strong local only) | Poor (Q of tank ~50) | None | Lowest |
- TRF (tuned RF, 1920s) | ~100 µV/m | Poor (Q ~100) | None | Low |
- Superheterodyne (AM broadcast) | ~50 µV/m | Good (±10 kHz at −6 dB) | 6–10 kHz | Medium |
- Superheterodyne (FM broadcast) | ~5 µV | Good (±200 kHz at −6 dB) | 180 kHz | Medium-high |
- Modern SDR | ~0.5 µV | Excellent (digital filter) | Programmable | High |

## Scaling Notes

- **Crystal radio scale**: passive (no power), receives the strongest local station. Range 10–50 km. The floor of communications capability — achievable with wire, a diode, and an earphone.
- **AM transmitter scale**: a 1 MHz Colpott oscillator with 1 mW output. Range ~100 m with a 10 m wire antenna. Legal under FCC Part 15 (unlicensed, <100 mW). Sufficient for a school or farm broadcast.
- **Superheterodyne receiver scale**: the standard AM/FM broadcast receiver. 5–10 transistors (or one IC like the LM386 + discrete RF). Reproducible from discrete components once [transistor manufacturing](semiconductor-devices.md) is available.
- **Industrial serial bus scale**: RS-485 over twisted pair connects 32 PLCs across a 1 km factory floor at 115.2 kbaud. The backbone of [industrial control](industrial-control.md) networks before Ethernet displaced it.
- **High-frequency / bandwidth scale**: above 30 MHz, parasitic capacitance and inductance of breadboards dominate. RF work above HF (3–30 MHz) requires a ground-plane PCB, shielded enclosures, and impedance-controlled traces (50 Ω). This is the boundary of introductory-level RF.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Crystal radio receives no stations | Poor ground connection, or antenna too short, or diode reversed | Connect ground to a metal cold-water pipe; use ≥10 m wire antenna; verify diode polarity (germanium bar = cathode) |
| RF oscillator doesn't start | Loop gain < 1, or wrong LC ratio, or transistor f_T too low for the frequency | Increase transistor bias current; verify C1/C2 ratio (Colpitts: C2 ≈ C1/8); use RF transistor (f_T > 5×f_osc) |
| Oscillator frequency drifts | Temperature variation of L and C, or hand capacitance near the tank | Use temperature-compensated capacitors (NPO/C0G ceramic); shield the tank; switch to crystal oscillator for stability |
| AM modulation distorted (flattened peaks) | Modulation index > 1 (overmodulation), or transistor gain nonlinearity | Reduce audio drive (target m ≈ 0.8); use automatic modulation control; verify on oscilloscope |
| Superheterodyne receives image frequencies | Image rejection inadequate (RF preselector not selective enough) | Add a tuned RF stage before the mixer to reject the image (RF + 2·IF); use higher IF (455 kHz for AM has image at RF + 910 kHz) |
| RS-485 bus errors at high baud rate | Missing or incorrect termination (reflections), or stubs too long | Terminate both ends with 120 Ω; keep stubs <0.3 m; reduce baud rate for long runs (1.2 km at 100 kbaud) |
| CAN bus communication fails | Incorrect termination (60 Ω measured across bus), or bit timing mismatch | Verify 120 Ω at each end (60 Ω net); configure sample point at 75–87.5% of bit time; check baud rate matches on all nodes |

## Safety

- **Transmitting without a license**: Broadcasting RF on licensed bands (AM, FM, shortwave, cellular) without authorization is illegal in most jurisdictions and can interfere with emergency communications. Use unlicensed bands (ISM: 13.56 MHz, 433 MHz, 2.4 GHz) or stay below Part 15 limits (field strength <30 µV/m at 3 m for AM).
- **RF exposure**: Transmit antennas radiate RF energy. At close range to a high-power transmitter (>10 W), RF exposure can cause tissue heating (the 1 GHz+ microwave oven effect). Follow FCC OET-65 exposure limits: <0.2 mW/cm² for the general public at cellular frequencies.
- **High voltage in transmitters**: Tube-type RF amplifiers run at 300–2000 VDC plate voltage. This is lethal. Use interlocks that disconnect the supply when the enclosure is opened. Bleed the plate capacitor before touching.
- **Antenna tower safety**: Installing a roof antenna near power lines is a frequent cause of electrocution. Maintain ≥3 m clearance from any power line. Use a fall-arrest harness on towers above 3 m.
- **Lead-acid battery for portable radios**: A 12 V 7 Ah gel-cell (common for portable radios) can deliver 100+ A into a short — enough to melt wire and start fires. Fuse the battery at 5–10 A.

## Quality Control

### Acceptance Criteria

- Crystal radio: receives at least one identifiable station with clear (if quiet) audio in the headphone.
- RF oscillator: produces a clean sine at the designed frequency ±10% (LC) or ±50 ppm (crystal); start-up within 100 ms.
- AM transmitter: modulation index adjustable 0–80%; audio intelligible on a calibrated reference receiver at 10 m.
- Superheterodyne receiver: sensitivity ≤100 µV/m (reproduces broadcast with listenable audio); selectivity rejects the adjacent channel (±10 kHz) by ≥20 dB.
- RS-485 bus: zero framing errors over a 10 000-frame test at the designed baud rate; 120 Ω termination measured across the bus.

### Testing Methods

- Frequency counter: connect to the oscillator output (via a 10:1 probe to avoid loading); verify within tolerance.
- Modulation meter (or oscilloscope): measure modulation index from the RF envelope (V_max, V_min → m = (V_max − V_min)/(V_max + V_min)).
- Spectrum analyzer: observe the carrier and sidebands; verify bandwidth and spurious emissions.
- BER (bit error rate) test for serial buses: transmit 10⁶ known bits; count errors. Target BER <10⁻⁶ for industrial links.

## Variations and Alternatives

### Receiver Architecture Comparison

| Architecture | Era | Selectivity | Sensitivity | Complexity | Notes |
|-------------|------|-----------|------------|-----------|-------|
| Coherer (spark) | 1895–1905 | None | Poor | Low | Earliest; unreliable |
- Crystal radio (direct) | 1905–1920 | Poor | Poor | Low | Passive; no gain |
- TRF (tuned RF) | 1920–1930 | Poor | Moderate | Medium | Multiple tuned stages |
- Superheterodyne | 1918–present | Good | Good | Medium-high | Industry standard for 100+ years |
- SDR (software-defined radio) | 2000–present | Excellent (digital) | Excellent | High (requires DSP) | Modern standard |

### Modulation for Digital Data

| Modulation | Bits per symbol | Required SNR (for BER 10⁻⁶) | Bandwidth efficiency | Used in |
|-----------|----------------|---------------------------|---------------------|---------|
| OOK / ASK | 1 | 13.5 dB | 1 bit/Hz | IR remote, RFID |
| FSK (2-level) | 1 | 10.5 dB | 1 bit/Hz | Bluetooth (GFSK), RTTY |
| BPSK | 1 | 10.5 dB | 1 bit/Hz | GPS, deep space |
| QPSK | 2 | 13.5 dB | 2 bit/Hz | Satellite, 3G |
| 16-QAM | 4 | 20.5 dB | 4 bit/Hz | Wi-Fi, cable modem |
| 64-QAM | 6 | 26.5 dB | 6 bit/Hz | DVB, DOCSIS |
| 256-QAM | 8 | 32.5 dB | 8 bit/Hz | Wi-Fi 6, cable |

Higher-order modulation packs more bits per symbol but requires a higher signal-to-noise ratio. This trade-off is the Shannon-Hartley theorem in practice: C = B·log₂(1 + S/N).

## References

- [Electrical systems](electrical-systems.md) — AC theory, transformers, and resonance are the substrate of every RF circuit. The tuned LC tank is a Tesla-era invention.
- [Passive components](passive-components.md) — inductors and capacitors set the resonant frequency; their quality (Q) directly determines oscillator stability and receiver selectivity.
- [Circuit fundamentals](circuit-fundamentals.ac-analysis.md) — phasors, reactance, impedance, resonance.
- [Analog circuits](analog-circuits.md) — transistor amplifier biasing and [oscillator circuits](analog-circuits.oscillator-circuits.md).
- [Industrial control](industrial-control.md) — Modbus and fieldbus protocols use these serial data links.
- [Optoelectronic circuits](optoelectronic-circuits.md) — IR and fiber-optic links are LED-driver + photodetector pairs.
- Deep articles: [modulation-circuits](communications-circuits.modulation-circuits.md), [rf-oscillator-circuits](communications-circuits.rf-oscillator-circuits.md), [receiver-circuits](communications-circuits.receiver-circuits.md).

---
*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md)*
