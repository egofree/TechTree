# Photodetector Circuits

> **Node ID**: `electronics.optoelectronic-circuits.photodetector-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md)
> **Enables**: None
> **Outputs**: photodetector-designs
> **Timeline**: Years 25-50
> **Critical**: No — photodetectors extend electronics into light sensing for measurement, communication, and control, but they are not on the minimum-viable bootstrap critical path

This is the inverse of the [LED driver article](optoelectronic-circuits.led-driver-circuits.md): where that article teaches how to convert electricity **into** light, this article teaches how to convert light **into** electricity. A photodiode is a [pn junction](semiconductor-devices.md) operated so that incident photons generate charge carriers; a phototransistor is the same idea with built-in gain; a light-dependent resistor is a non-junction bulk-conductivity sensor. The semiconductor device physics and manufacturing are covered under [Semiconductor Devices](semiconductor-devices.md) — this article teaches the **circuit design**: how to turn tiny photocurrents into usable voltage signals and light-activated control actions.

The governing challenge of photodetector circuit design is **signal magnitude**. A typical silicon photodiode in indoor light produces a photocurrent on the order of **1–10 µA** — three orders of magnitude smaller than an LED drive current. The central design task is therefore **current-to-voltage conversion and amplification**: turning microamps into volts that downstream logic, meters, or actuators can read. Every circuit below is a variation on that theme, optimized for a different speed/sensitivity/complexness trade-off.

---

## 1. Photodiode Circuits

The photodiode is the fastest, most linear, but lowest-signal light sensor. Photons absorbed in the depletion region create electron-hole pairs that the junction field sweeps out as a reverse current proportional to the light flux.

There are two fundamental operating **modes**, set by how the diode is biased:

| Mode | Bias | How it works | Trade-off |
|------|------|--------------|-----------|
| **Photoconductive** (reverse-biased) | V_R applied (e.g. −5 V) | Depletion region widens → more photons collected, lower capacitance | Faster response, higher dark current, some nonlinearity |
| **Photovoltaic** (unbiased, zero-bias) | Short-circuited or into a virtual ground | Self-generated photocurrent, no external field | Lower dark current (best low-light linearity), slower (higher C_j) |

For most measurement applications, photoconductive mode is the default — the speed advantage and wider depletion region outweigh the slight dark-current penalty. Photovoltaic mode wins for precision low-light work (solar-cell metrology, photometry) where dark-current error matters more than bandwidth.

### 1a. Photoconductive (reverse-biased) photodiode — simple load resistor

The simplest readout: reverse-bias the diode through a load resistor. Photocurrent develops a voltage across R_L proportional to light intensity.

```
              V_supply (−5 V or −9 V)
                 │
                 │   (reverse bias: cathode to −V)
                 ├─── Cathode (┬───┐)
                 │             │   │ Photodiode
                 │             │   │ (reverse-biased)
                 │             └───┘
                 │             │
                 ├────── R_L ──┤
                 │             │
                 │             Anode ──── V_out
                 │             │
                 │            GND

    V_out = −I_photo × R_L      (signal swings negative)
```

**Limitation:** R_L and the diode's junction capacitance C_j form an RC low-pass filter that limits speed. With R_L = 100 kΩ and C_j = 10 pF, the time constant is 1 ms — useless for anything faster than ~1 kHz. Raising R_L for more sensitivity makes it slower. This is the core problem that motivates the transimpedance amplifier.

### 1b. Transimpedance Amplifier (TIA) — the standard photodiode front-end

The transimpedance amplifier (TIA) uses an [op-amp](analog-circuits.md) to hold the photodiode at a fixed voltage (a **virtual ground**) while converting the photocurrent to an output voltage through a feedback resistor. Because the diode voltage never moves (the op-amp's inverting input is a virtual ground), the junction capacitance never charges or discharges — eliminating the R_L · C_j speed penalty of §1a.

```
                     V_supply (+)
                          │
                          │
                      ┌───┴────┐
                      │  +     │
                      │ Op-Amp ├────── V_out
                      │  −     │
                      └───┬────┘
                          │
              ┌───────────┤
              │           │
              │           ├── R_f (feedback resistor)
              │           │   │
              │           └───┘
              │           │
        ┌─────┴─────┐    │
        │Photodiode │────┴──── inverting input (virtual ground)
        │(zero-V_bias│
        │/photocond.)│
        └─────┬─────┘
              │
             GND (cathode to ground, or to −V_bias for photoconductive)

    V_out = −I_photo × R_f
```

The governing equation is the heart of transimpedance design:

```
    V_out = −I_photo × R_f
```

The output is a **voltage proportional to photocurrent**, with the proportionality constant R_f. The diode sees a virtual short (zero voltage across it) regardless of light level, so its capacitance is effectively decoupled from the signal path — bandwidth is set by the op-amp's gain-bandwidth product and R_f, not by C_j alone.

### Worked example: TIA for 10 µA photocurrent with 100 kΩ feedback

A photodiode produces I_photo = 10 µA under the target illumination. Choose R_f = 100 kΩ:

```
    V_out = −I_photo × R_f
          = −(10 × 10⁻⁶ A) × (100 × 10³ Ω)
          = −1.0 V
```

The TIA delivers a clean **1.0 V** signal from a 10 µA photocurrent — a comfortable span for any analog-to-digital converter or meter. The trade-offs:

- **Sensitivity:** doubling R_f to 200 kΩ gives 2.0 V output for the same 10 µA (more sensitivity). But the same op-amp swing clips at 1 µA (output would try to reach 200 mV — fine — or at 25 µA the output saturates at 5 V).
- **Bandwidth:** R_f and the feedback capacitance C_f set the dominant pole: f_−3dB ≈ 1 / (2π · R_f · C_f). With R_f = 100 kΩ and C_f = 5 pF, the bandwidth is ~320 kHz — ample for optical communications or fast sensing. Lowering C_f extends bandwidth but risks oscillation.
- **Noise:** R_f's thermal noise (√(4kTR_f·BW)) is the dominant noise source. A larger R_f improves the **signal-to-noise ratio** because signal scales with R_f but resistor noise scales only with √R_f — making high-R_f TIAs dramatically more sensitive than low-R_f ones (this is why precision photometry uses R_f values up to 1 GΩ).

For high-speed operation (photoconductive mode), reverse-bias the diode cathode to a negative rail instead of ground — the virtual-ground principle still holds, but the diode now has the reverse bias it needs to reduce C_j and speed up carrier collection.

---

## 2. Phototransistor Circuits

The phototransistor is a [BJT](semiconductor-devices.md) whose base-collector junction is exposed to light. Photocurrent in the base-collector junction acts as base current, amplified by the transistor's current gain β — so a phototransistor produces a usable collector current from far less light than a photodiode. The trade-off: much slower response (µs vs. ns), wider β spread, and poorer linearity.

### Common-emitter light switch

The workhorse circuit: the phototransistor's collector is pulled up to V_supply through a load resistor; incident light turns the transistor on, pulling the collector toward ground.

```
              V_supply (+5 V)
                 │
                 ├─── R_L (e.g. 10 kΩ) ───┐
                 │                        │
                 │                        ▼  V_out (HIGH = dark, LOW = lit)
                 │                     ┌─────┐
                 │                     │  C  │
                 │    light ──────────►│Photo│ NPN phototransistor
                 │                     │  B  │ (base driven by photons)
                 │                     │     │
                 │                     │  E  │
                 │                     └──┬──┘
                 │                        │
                 │                       GND
```

With no light: transistor is off, no collector current flows, V_out sits at V_supply (logic HIGH). With incident light: photocurrent is amplified by β, collector current flows through R_L, V_out falls toward ground (logic LOW).

**Output equation:** V_out = V_supply − (β · I_photo) · R_L. Choose R_L so that at the target light level the transistor saturates (V_out < 0.5 V for a clean logic LOW):

```
    For β = 100, I_photo = 5 µA (modest indoor light):
    I_C = β × I_photo = 100 × 5 µA = 500 µA
    To pull V_out to ~0 V from 5 V: R_L = (5 − 0) / 500 µA = 10 kΩ
```

This is 100× more sensitive than a bare photodiode with the same R_L — that is the phototransistor's reason to exist. The cost is that β varies wildly between devices (50–500 typical), so the threshold set by R_L is only approximate; for precise trip points, use a photodiode + TIA or add a comparator with hysteresis.

**Variants:**
- **Common-collector (emitter follower):** output at the emitter follows light intensity linearly over a limited range — used as an analog light sensor.
- **Darlington phototransistor:** two transistor stages give β ≈ 10 000, but at the cost of much slower response (100 µs+) and 2× V_BE offset — used where sensitivity matters more than speed.

---

## 3. Light-Dependent Resistor (LDR) Circuits

The LDR (photoconductive cell, often cadmium-sulfide CdS) is a non-junction sensor whose bulk resistance falls with incident light. In darkness an LDR reads 1–10 MΩ; in bright light it falls to 100 Ω–1 kΩ. Unlike a photodiode, the LDR responds slowly (10–100 ms) and is bulky, but it is cheap, passes significant current directly, and interfaces to logic without amplification.

### 3a. Voltage divider (analog light level)

The simplest readout: pair the LDR with a fixed resistor in a voltage divider. The output voltage tracks illumination.

```
              V_supply (+5 V)
                 │
                 ├─── R_fixed ───┬──── V_out
                 │               │
                 │               ├── LDR ────┐
                 │               │           │
                 │               GND         GND
```

With the LDR on the bottom (as shown): V_out = V_supply · R_LDR / (R_fixed + R_LDR) — output rises with light. Swap them (LDR on top, fixed below): output falls with light. Choose R_fixed near the LDR's mid-range resistance (~10 kΩ) for the most linear response around the trip point.

### 3b. Light-activated switch

Adding a transistor (or comparator) to the divider creates a switch that trips when light exceeds a threshold — a daylight sensor, optical interrupter, or conveyor object-detector.

```
              V_supply (+5 V)
                 │
                 ├─── R_LDR ────┬─── base of Q1 (NPN)
                 │              │
                 │              ├── R_fixed ─── GND
                 │              │
                 │              │   (divider sets V_base)
                 │              ▼
                 │          ┌─────┐
                 │          │  C  │──── V_out ──── load (relay, LED)
                 │          │ Q1  │
                 │          │  E  │
                 │          └──┬──┘
                 │             │
                 │            GND
```

In **light**, the LDR's resistance falls, V_base rises above V_BE (0.7 V), Q1 turns on, the load energizes. In **darkness**, the LDR's resistance rises, V_base falls below V_BE, Q1 turns off. The fixed resistor sets the trip threshold; replacing R_fixed with a potentiometer makes the threshold adjustable.

### 3c. Dark-activated switch

Swap the LDR and the fixed resistor in the divider — now V_base rises in **darkness** and the load energizes when light is removed (security lights, streetlamp control, darkroom interlock). The same circuit, flipped:

```
              V_supply (+5 V)
                 │
                 ├─── R_fixed ────┬─── base of Q1
                 │                │
                 │                ├── R_LDR ─── GND
                 │                │
                 │                ▼
                 │            (rest identical)
```

---

## Worked Example: Complete TIA Design (recap)

Design a photodiode front-end to detect a 10 µA photocurrent (typical of indoor ambient light on a 5 mm² silicon photodiode):

| Step | Value | Calculation |
|------|-------|-------------|
| 1. Pick R_f for full-scale at max light | R_f = 100 kΩ | R_f = V_out(full-scale) / I_photo(max) = 1.0 V / 10 µA |
| 2. Verify output | V_out = 1.0 V | V_out = I_photo × R_f = 10 µA × 100 kΩ |
| 3. Pick C_f for stability | C_f = 5 pF | Sets f_c = 1/(2π·R_f·C_f) ≈ 320 kHz |
| 4. Verify op-amp GBW | GBW ≥ 2π·R_f·C_f·f_c² / A_cl | Use op-amp with GBW ≥ 1 MHz |
| 5. Verify dark-current error | I_dark ≈ 1 nA → V_dark = 100 µV | 0.01% of signal — negligible |

This is the design used in optical pick-offs, ambient-light sensors, and fiber-optic receivers operating at moderate data rates.

---

## Photodetector Parameter Reference

| Detector type | Sensitivity (typ.) | Response time | Spectral range | Typical circuit |
|---------------|-------------------|---------------|----------------|-----------------|
| Photodiode (Si, PIN) | 0.5 A/W (630 nm) | 1–10 ns (reverse-biased) | 200–1100 nm (peak ~850 nm) | TIA (§1b) |
| Photodiode (GaAsP) | 0.2 A/W | 1–5 µs | 300–680 nm (visible) | TIA or reverse-bias load |
| Phototransistor (NPN, Si) | β × 0.5 A/W (gain 50–500×) | 2–50 µs | 400–1100 nm | Common-emitter switch (§2) |
| LDR (CdS photoresistor) | nonlinear (100 Ω–10 MΩ range) | 10–100 ms | 400–700 nm (visible, eye-like) | Voltage divider / switch (§3) |
| Photovoltaic (solar cell, Si) | 0.3–0.5 A/W (illuminated) | 10–100 µs | 300–1100 nm | Direct load or battery charge |
| Avalanche photodiode (APD) | 50–100 A/W (with internal gain) | 0.1–1 ns | 400–1100 nm | High-voltage reverse bias + TIA |

**Spectral note:** silicon photodiodes are blind beyond ~1100 nm (band gap of Si = 1.12 eV); for mid-IR detection use InGaAs (cut-off ~1700 nm) or thermopile / pyroelectric sensors. **Response time** scales inversely with sensitivity for a given device class — faster devices always cost sensitivity, because sensitivity requires collecting more photons, which means larger area or slower integration.

---

## Design Heuristics

| Design goal | Recommended detector | Recommended circuit |
|-------------|---------------------|---------------------|
| Precision light measurement (photometry) | Photodiode (photovoltaic mode) | TIA with high R_f (§1b) |
| Fast optical signal (kHz–MHz) | PIN photodiode (reverse-biased) | TIA (§1b) |
| Cheap light/dark switch | Phototransistor or LDR | Common-emitter (§2) or divider (§3) |
| High-sensitivity low-light detection | Photodiode + high-gain TIA | R_f = 1–100 MΩ |
| Eye-response (visible-only) measurement | CdS LDR or filtered photodiode | Voltage divider (§3a) |
| IR detection (remote controls, IR links) | IR photodiode (940 nm peak) | TIA or phototransistor |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the photodiode is a reverse-biased pn junction, the phototransistor a BJT with an optically active base-collector junction; their construction and physics live there.
- [Passive Components](passive-components.md) — the feedback and load resistors used in every circuit here.
- [Analog Circuits](analog-circuits.md) — op-amp configurations (inverting, transimpedance), transistor biasing, and comparator circuits.
- DC circuit analysis (Ohm's law, voltage dividers) — covered under the circuit-fundamentals track.

## Scope Boundary

This article covers light **detection** circuits only. It does **not** cover:

- Photodiode / phototransistor semiconductor physics or manufacturing — see [Semiconductor Devices](semiconductor-devices.md).
- Optocoupler circuits (isolated signal transfer using paired LED + photodetector) — a separate [Optoelectronic Circuits](optoelectronic-circuits.md) article.
- IR communications circuits (modulation, carrier, demodulation) — a separate article.
- Image sensors (CCD, CMOS imager arrays) — those are VLSI devices covered under [Computing](../computing/electronic.md) and VLSI scaling.

The companion process — converting electricity into light with LEDs — is covered in the sibling article [LED Driver Circuits](optoelectronic-circuits.led-driver-circuits.md).

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
