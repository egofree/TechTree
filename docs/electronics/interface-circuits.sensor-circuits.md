# Sensor Circuits

> **Node ID**: `electronics.interface-circuits.sensor-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md),
> [`electronics.interface-circuits.adc-circuits`](interface-circuits.adc-circuits.md)
> **Enables**: None
> **Outputs**: sensor-circuit-designs
> **Timeline**: Years 30-50
> **Critical**: No — interface-circuit pedagogy; the underlying semiconductor devices and passive-component manufacturing capabilities are the critical prerequisites

A sensor converts a **physical quantity** — magnetic field, temperature, mechanical strain, light, liquid level — into an electrical parameter (a voltage, a resistance, a current, or a contact closure). Raw sensor outputs are almost never directly usable: a thermistor's resistance changes only a few percent per degree, a strain gauge moves a tenth of an ohm, a Hall element produces millivolts buried in noise. **Signal conditioning** is the analog circuitry that turns that frail raw signal into a clean, bounded, low-impedance voltage (or a robust current loop) suitable for an [ADC](interface-circuits.adc-circuits.md) to digitize or a comparator to threshold.

The conditioning building blocks — [op-amp](analog-circuits.md) amplifiers, [Schmitt triggers](analog-circuits.md), analog switches, precision references — come from [Semiconductor Devices](semiconductor-devices.md); the precision matched [resistors](passive-components.md) that build bridge networks and dividers, and the low-leakage capacitors that build integrators and debouncers, come from [Passive Components](passive-components.md). This article does **not** re-derive op-amp or comparator internals (see [Analog Circuits](analog-circuits.md)) and does **not** re-teach photodiode/phototransistor physics (see [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md) for light-sensor front-ends).

---

## 1. What Signal Conditioning Does

Every sensor chain performs some subset of five operations, in roughly this order:

```
   physical     ┌──────────┐   raw       ┌──────────┐  conditioned  ┌─────┐  digital
   quantity ──► │  sensor  │ ── signal ─► │condition-│ ── voltage ──► │ ADC │ ──► word
   (B, T, ε,..) └──────────┘   (R,V,I)    │  ing     │   (0..V_ref)  └─────┘
                                        └──────────┘
```

1. **Excitation.** Passive sensors (thermistors, RTDs, strain gauges) change impedance; they need an external voltage or current to produce a measurable signal. Active sensors (Hall ICs, photodiodes) generate their own voltage/current but still need a supply.
2. **Amplification.** Raw signals are small — microvolts to millivolts. A non-inverting op-amp stage or an instrumentation amplifier lifts them into a useful range.
3. **Filtering.** A low-pass filter rejects high-frequency noise and, placed before an ADC, acts as the **anti-alias filter** (see [ADC Circuits](interface-circuits.adc-circuits.md) §1).
4. **Linearization.** Many sensors (notably NTC thermistors) are nonlinear. Linearization can be analog (positive/negative temperature coefficient networks) or, more cheaply today, done in firmware after digitization.
5. **Offset / null adjustment.** Bridges and dividers need a zero-adjust so the output reads zero at the reference condition, cancelling tolerance buildup.

### Amplification: non-inverting vs instrumentation

A single [op-amp](analog-circuits.md) non-inverting stage gives high input impedance and a precise gain `A_v = 1 + R_f/R_g`. For a single-ended sensor signal sharing a common ground with the conditioner this is enough. But bridge sensors (strain gauge, RTD) produce a **differential** signal — the useful information is the *difference* between two nodes, both riding on a large common-mode voltage. Rejecting that common-mode component demands an **instrumentation amplifier** (in-amp): a differential stage with very high common-mode rejection (CMRR > 100 dB), settable gain via one resistor, and high impedance on *both* inputs. A classic three-op-amp in-amp buffers each input with a follower and subtracts them in a difference stage; integrated in-amps (AD620, INA128) put this on one chip.

### Filtering: why a low-pass is almost always the first stage

Sensor signals are slow — temperature changes in seconds, strain in milliseconds, Hall fields in microseconds. Noise, by contrast, is broadband (mains hum at 50/60 Hz, RF pickup, switch-mode ripple). A simple RC low-pass with `f_c = 1/(2πRC)` set a decade above the signal's highest frequency removes most interference. For mains rejection a twin-T notch or an integrating ADC (see [ADC Circuits](interface-circuits.adc-circuits.md) §4) targets 50/60 Hz directly.

### The 4-20 mA current loop

In industrial environments where sensor and readout are tens or hundreds of metres apart, a voltage signal is hopeless — cable resistance, ground offsets, and induced noise corrupt it. The **4-20 mA current loop** solves this: the sensor (a "transmitter") regulates the current in the loop between 4 mA (live zero — distinguishes "zero reading" from "broken wire") and 20 mA (full scale). Current is unaffected by cable resistance (within the transmitter's voltage budget), the receiver reads it as a single precision resistor to ground (e.g. 250 Ω → 1-5 V), and the loop can even power the sensor (two-wire transmitter). It is the de facto industrial sensor interface and the reason every PLC analog input card expects a 250 Ω burden.

---

## 2. Hall-Effect Sensors (Magnetic Field → Voltage)

A Hall-effect sensor measures magnetic field via the Lorentz force on moving charge carriers. When a current `I` flows lengthwise through a thin conducting plate immersed in a perpendicular field `B`, the carriers are deflected sideways, accumulating charge on one edge until the resulting transverse electric field balances the magnetic force. The steady-state transverse voltage — the **Hall voltage** — is:

```
    V_H = I · B / (n · e · t)

    n = carrier density (m^-3)
    e = electron charge  = 1.602e-19 C
    t = plate thickness (m)
```

The raw Hall voltage in a silicon Hall element is tiny — a few millivolts to a few tens of millivolts at typical fields — and rides on a large common-mode offset. Integrated Hall sensors add on-chip amplification, offset cancellation (chopper stabilization), and either a linear output (voltage ∝ B, e.g. ~1.3 mV/G) or a built-in threshold comparator for a clean digital switch output that snaps high when |B| exceeds a trip point (~a few mT).

### Hall interface circuit (linear, discrete-friendly)

For a linear Hall IC (3-pin: VCC, GND, V_OUT), the signal chain is amplification + filtering + thresholding:

```
                          V_CC (+5 V)
                            │
                         ┌──┴──┐
                         │ Hall│  linear Hall IC, ~V_CC/2 quiescent,
                         │ IC  │  sensitivity ≈ 1.3 mV/G, swings ±~1.3 V
                         └──┬──┘
                            │ V_hall (analog, high-Z)
                            │
              ┌─────────────┴──────────────┐
              │                            │
           ┌──┴──┐                       ┌─┴─┐
           │  R  │                       │ C │  RC low-pass: f_c = 1/(2πRC)
           │     │                       │   │  e.g. R=10k, C=1µF → f_c≈16 Hz
           └──┬──┘                       └─┬─┘  (rejects 50/60 Hz hum + RF)
              │                            │
              ▼ ┌────────────┐             │
                │ non-inv    │             │
                │ op-amp     │◄────────────┘
                │ A=1+Rf/Rg  │
                └─────┬──────┘
                      │ V_out (amplified, filtered)
                      │
                   ┌──┴──┐
                   │Schmt│  optional: threshold + hysteresis
                   │trig │  → clean digital "magnet present" bit
                   └──┬──┘
                      │
                      ▼ digital out (or → ADC)
```

For a Hall **switch** (e.g., door-open detector, rpm pickup), the on-chip Schmitt trigger already does the thresholding and the part outputs a clean logic level — no external amplifier needed, just a pull-up resistor on the open-collector output. The conditioning work is then purely placement (the field falls off as 1/r³ for a small magnet) and adding a small ceramic capacitor across VCC-GND for supply decoupling.

### Worked note: Hall in a rpm counter

A small magnet glued to a rotating shaft passes a Hall switch once per revolution. The Hall output pulses once per turn; a microcontroller counts pulses over a gate time `T_gate` and computes `rpm = 60 × counts / T_gate`. The conditioning circuit is the Hall switch + 10 kΩ pull-up + 100 nF supply decoupler — three components. This is the basis of every brushless motor commutation sensor and most bicycle speedometers.

---

## 3. Reed Switches (Magnetic Actuation of Contacts)

The reed switch is the simplest magnetic sensor: two ferromagnetic contact blades sealed in a glass capsule. A nearby permanent magnet or coil magnetizes the blades, attracting them and closing the contact — no semiconductor physics, no power supply, just mechanics. It is binary (open/closed), fast (~0.1–1 ms), and good for millions of operations.

### The bounce problem

Mechanical contacts do not close cleanly. The blades rebound on impact and "bounce" open and closed for **0.1–10 ms** before settling. Read raw, this looks like a burst of tens of pulses instead of one clean edge. Two standard debounce remedies:

**Hardware debounce (RC + Schmitt):** An RC network integrates the noisy waveform into a single slow edge; a [Schmitt trigger](analog-circuits.md) snaps it clean via hysteresis.

```
   +5 V
     │
     │     ┌─── R1 (e.g. 10 kΩ) ───┬─────────┐
     │     │                       │         │
   ┌─┴─┐  ─┤                      ─┤        ├─► Schmitt trigger (74HC14) ──► clean OUT
   │reed│  │        C (e.g. 100 nF)│        │
   │sw  │  │                        │       │
   └─┬─┘  ─┘                       ─┘       │
     │      (to GND)                         │  hysteresis: V_T+ ≈ 3.3 V, V_T- ≈ 1.7 V
   GND                                      │  RC time constant τ = R1·C = 1 ms
                                             │  ≫ bounce period → integrates it away
```

During bounce, the capacitor cannot charge or discharge through a full τ between bounces, so the Schmitt input slews monotonically; the hysteresis guarantees a single clean output transition. **Firmware debounce** (sample every 10 ms, accept a level only if stable for N samples) achieves the same thing in software and costs zero components — the usual modern choice for an [embedded system](../computing/embedded-systems.md).

---

## 4. Temperature: NTC Thermistor

A **thermistor** is a resistor whose value changes strongly with temperature. **NTC** (negative temperature coefficient) types drop in resistance as they warm — the common choice for general measurement; **PTC** types rise sharply past a switch temperature — used for overcurrent/overtemp protection or self-regulating heaters. A typical 10 kΩ NTC moves roughly −4%/°C at room temperature: large enough to read with a simple divider, small enough to need amplification for real resolution.

### The beta model (single-parameter approximation)

The full Steinhart-Hart equation is a three-coefficient logarithmic fit (R → 1/T) that gives ±0.02 °C across a wide span. For most conditioning work a one-parameter **beta model** is enough over a 0–100 °C window:

```
    R(T) = R(T0) · exp[ β · (1/T − 1/T0) ]

    T, T0 in kelvin;  R(T0) is the rated resistance at T0 (usually 25 °C = 298.15 K)
    β  is the material constant (typically 3380–4300 K for NTC)
```

### Voltage divider front-end

The cheapest NTC front-end is a two-resistor divider: the thermistor on top from a stable reference, a fixed resistor to ground, and the junction read by an ADC (or further amplified). Putting the NTC on top makes `V_out` **rise** with temperature (NTC falls, so the bottom resistor takes a larger share) — a convenient polarity.

```
    V_ref (e.g. 5 V)
      │
      ├───[ NTC thermistor, R(T) ]──┬──► V_out  (to ADC / buffer)
      │                              │
      ├───[ R_ref = 10 kΩ ]───┐      │
                              │      │
                             GND   (V_out = V_ref · R_ref / (R(T) + R_ref))
```

### Worked example: 10 kΩ NTC, β = 3950, R_ref = 10 kΩ, V_ref = 5 V

Apply the beta model at the two endpoints and the midpoint:

```
    T0 = 25 °C = 298.15 K,  R0 = 10 000 Ω,  β = 3950 K
```

| Temperature | T (K) | R(T) = R0·exp[β(1/T−1/T0)] | V_out = 5·R_ref/(R+R_ref) |
|-------------|-------|-----------------------------|---------------------------|
| 0 °C | 273.15 | 10 000·exp(3950·(1/273.15−1/298.15)) = **33.62 kΩ** | 5·10k/(33.62k+10k) = **1.146 V** |
| 25 °C | 298.15 | 10 000·exp(0) = **10.00 kΩ** | 5·10k/(10k+10k) = **2.500 V** |
| 50 °C | 323.15 | 10 000·exp(3950·(1/323.15−1/298.15)) = **3.588 kΩ** | 5·10k/(3.588k+10k) = **3.680 V** |

### Nonlinearity check

A perfectly linear sensor would produce a straight line between the 0 °C and 50 °C endpoints. Comparing sensitivities over the two halves of the range:

```
    Sensitivity 0→25 °C :  (2.500 − 1.146) / 25 = 54.16 mV/°C
    Sensitivity 25→50 °C :  (3.680 − 2.500) / 25 = 47.20 mV/°C

    Chord slope 0→50 °C :  (3.680 − 1.146) / 50 = 50.68 mV/°C
    Linear prediction at 25 °C : 1.146 + 25·0.05068 = 2.413 V
    Actual at 25 °C           : 2.500 V
    Deviation (nonlinearity)  : +87 mV  ≈ +1.7 °C equivalent
```

The divider bows about **13 %** steeper on the cold half than on the warm half. Two practical fixes:

1. **Pick R_ref = R(T_midpoint).** Choosing the reference resistor equal to the thermistor's resistance at the center of the measurement range maximizes sensitivity where it matters and balances the curvature.
2. **Linearize in firmware.** After digitizing, apply the inverse beta equation (`T = 1 / [1/T0 + ln(R/R0)/β]`) — fractions of a °C across the whole usable range, no precision analog network required. This is the overwhelming modern practice because a [microcontroller](../computing/embedded-systems.md) is already reading the ADC.

A note on **self-heating**: the divider current dissipates `P = V²/R` in the thermistor. A 10 kΩ NTC at 5 V dissipates 2.5 mW; with a typical dissipation constant of 7 mW/°C (in still air) that is ~0.36 °C of self-induced warming. Dropping V_ref or raising R_ref reduces it; the trade-off is lower sensitivity.

---

## 5. Temperature: RTD and the Wheatstone Bridge

The **resistance temperature detector** (RTD) is a precision platinum (Pt) wire or film whose resistance rises almost linearly with temperature — the standard for industrial accuracy. The canonical Pt100 is 100 Ω at 0 °C with a temperature coefficient α ≈ 0.00385 Ω/Ω/°C, giving `R(T) ≈ R0·(1 + αT)` → 138.5 Ω at 100 °C, 292.5 Ω at 500 °C. The change is small (0.385 Ω/°C) so lead resistance and contact resistance would swamp the reading without care.

### The Wheatstone bridge

A Wheatstone bridge turns a small resistance change into a differential voltage centered on zero. Four resistors in a diamond, an excitation voltage across the top/bottom nodes, and the output taken across the left/right nodes:

```
                   V_exc
                     │
            ┌────────┴────────┐
            │                 │
         ┌──┴──┐           ┌──┴──┐
         │ R1  │           │ R2  │   (reference arm)
         │(ref)│           │(ref)│
         └──┬──┘           └──┬──┘
            │                 │
            ├── V_out (+) ────┤    ◄── differential output → instrumentation amp
            │                 │
         ┌──┴──┐           ┌──┴──┐
         │RTD  │           │ R4  │   (R4 = R0 to balance the bridge at 0 °C)
         │R(T) │           │     │
         └──┬──┘           └──┬──┘
            │                 │
            └────────┬────────┘
                     │
                    GND
```

At balance (V_out = 0) the four arms satisfy `R1/R2 = RTD/R4`. When the RTD changes by ΔR, the bridge outputs a small differential voltage approximately:

```
    V_out ≈ (V_exc / 4) · (ΔR / R0)        (quarter-bridge, small ΔR)
```

For a Pt100 with V_exc = 5 V at ΔT = +1 °C: ΔR = 0.385 Ω, so V_out ≈ (5/4)·(0.385/100) ≈ **4.8 mV/°C** — clean, differential, and zero at the reference temperature, so the in-amp can use its full gain on the signal of interest rather than on a large offset.

### Lead resistance: 3-wire and 4-wire compensation

A Pt100's lead wires add maybe 0.1–1 Ω per lead — equivalent to 0.25–2.6 °C of error. Two compensation schemes defeat this:

- **3-wire:** One lead is in each of the two lower arms of the bridge; if both leads have equal resistance their offsets cancel. The industrial default when the sensor is a few metres away.
- **4-wire (Kelvin):** Two leads carry the excitation current, two sense the voltage across the RTD with a high-impedance meter (zero current, so zero lead drop). Removes lead resistance entirely — the laboratory choice for highest accuracy.

---

## 6. Strain Gauge (Mechanical Strain → Resistance)

A strain gauge is a fine metal foil grid bonded to a surface; stretching it lengthens and thins the foil, raising its resistance by a tiny amount. The **gauge factor** relates fractional resistance change to mechanical strain:

```
    GF = (ΔR/R) / ε        ε = strain (dimensionless, typically 1e-6 to 1e-3)
    GF ≈ 2.0  for metal-foil gauges
```

For a 120 Ω gauge at 1000 microstrain (a moderate load): ΔR/R = GF·ε = 2·0.001 = 0.002, so ΔR = 0.24 Ω. This is unmeasurable directly — the bridge is mandatory.

### Quarter / half / full bridge

How many of the four bridge arms are active gauges determines sensitivity:

```
    Quarter bridge (1 active):   V_out ≈ (V_exc · GF · ε) / 4
    Half bridge  (2 active):     V_out ≈ (V_exc · GF · ε) / 2     (e.g. one tension, one compression)
    Full bridge  (4 active):     V_out ≈       V_exc · GF · ε      (e.g. bending beam: 2 tension, 2 compression)
```

```
                       V_exc
                         │
                ┌────────┴────────┐
                │                 │
          ┌─────┴─────┐     ┌─────┴─────┐
          │ R₁ gauge  │     │ R₂ gauge  │
          │ (tension) │     │ (tension) │      ◄── full bridge on a bending beam:
          └─────┬─────┘     └─────┬─────┘           R1,R4 tension; R2,R3 compression
                │                 │                  (or vice-versa) → all four contribute
                ├── V_out (+) ────┤                  additively, and temperature cancels
                │                 │
          ┌─────┴─────┐     ┌─────┴─────┐
          │ R₃ gauge  │     │ R₄ gauge  │
          │ (compr.)  │     │ (compr.)  │
          └─────┬─────┘     └─────┬─────┘
                │                 │
                └────────┬────────┘
                         │
                        GND
```

### Worked gain computation (full bridge load cell)

A 350 Ω full-bridge load cell, V_exc = 5 V, GF = 2, at full rated load ε = 1000 µε:

```
    V_out = V_exc · GF · ε = 5 · 2 · 0.001 = 10 mV  (full-scale differential)
```

To bring that to a 0–5 V [ADC](interface-circuits.adc-circuits.md) span, the instrumentation amplifier needs a gain of about `5 V / 10 mV = 500`. Dedicated load-cell ADCs (HX711 etc.) integrate a 128×-gain in-amp and a 24-bit sigma-delta converter, achieving sub-microvolt resolution in one chip — the modern replacement for the discrete bridge + in-amp + 16-bit ADC chain. Note the **full bridge** inherently cancels temperature: all four gauges drift together, so the ratios (and thus the balance) are unaffected.

---

## 7. Light Sensors (Recap)

Light sensing splits cleanly into two regimes, both covered in depth by the sibling article [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md):

- **Photoconductive (LDR / CdS cell):** a passive resistor whose conductance rises with photon flux. The front-end is the same two-resistor voltage divider as the thermistor in §4, with the LDR substituting for the NTC. Simple, cheap, slow (tens of ms response), and banned in EU (RoHS — cadmium content) for new designs.
- **Photovoltaic / photoconductive junction (photodiode, phototransistor):** an active semiconductor junction generating a photocurrent proportional to flux. The front-end is a **transimpedance amplifier** (op-amp with feedback resistor, `V_out = I_photo · R_f`), taught in full — including the compensation capacitor, bandwidth, and noise analysis — in [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md). This article does not re-derive it.

For light-sensor conditioning work, apply the principles of §1 (excite or not per sensor type, amplify, low-pass-filter, optionally linearize the logarithmic response) using the front-end topologies from the photodetector article.

---

## 8. Liquid-Level Sensing

Level measurement is mostly a materials-and-packaging problem (corrosion, fouling, pressure rating) layered onto one of two electrical principles:

- **Conductive probes:** two (or more) bare metal electrodes dip into a conductive liquid (water, acid). Liquid bridges the electrodes → low resistance; dry → open. A small AC excitation (not DC, to avoid electrolysis) drives the probe; a rectifier + Schmitt produces a clean wet/dry bit per electrode. Stacking several electrodes at different heights gives a discrete level reading. Cheap, robust, conductive-liquid-only.
- **Capacitive level sensing:** two insulated electrodes form a capacitor whose dielectric is part air (κ≈1) and part liquid (water κ≈80). As the liquid rises, capacitance rises proportionally. An RC oscillator (see [multivibrator circuits](analog-circuits.md)) converts the capacitance to a frequency, counted by a microcontroller; or a capacitance-to-digital IC measures it directly. Works with non-conductive liquids (oil, fuel) where conductive probes fail.

Both reduce, after the front-end, to the same generic chain — amplify, filter, threshold or digitize — that this article's §1 establishes.

---

## Sensor Parameter Reference

| Sensor type | Measurand | Typical range | Raw output | Typical conditioning circuit |
|-------------|-----------|---------------|------------|------------------------------|
| **Hall (linear IC)** | Magnetic field B | ±100 mT | voltage ≈ V_CC/2 ± k·B | buffer + RC LPF (+ Schmitt for switch) |
| **Hall (switch IC)** | Field presence | on/off at trip | open-collector logic | pull-up + 100 nF decoupler |
| **Reed switch** | Field/contact | on/off | contact closure | RC debounce + Schmitt (or firmware) |
| **NTC thermistor** | Temperature | −40 to +125 °C | resistance (kΩ, nonlinear) | divider + ADC (+ beta fit in FW) |
| **RTD (Pt100)** | Temperature | −200 to +600 °C | resistance (Ω, ~linear) | Wheatstone bridge + 3/4-wire + in-amp |
| **Thermocouple** | Temperature | −200 to +1700 °C | voltage (µV/°C) | cold-junction comp + high-gain in-amp |
| **Strain gauge** | Strain / load | µε to mε | ΔR/R ≈ GF·ε | Wheatstone (1/2/4-arm) + in-amp |
| **LDR (CdS)** | Light | 1 to ~10 000 lux | resistance (kΩ) | divider + ADC |
| **Photodiode** | Light | wide | photocurrent (µA) | transimpedance amp (see photodetector-circuits) |
| **Conductive probe** | Liquid level | wet/dry | contact closure | AC excite + rectifier + Schmitt |
| **Capacitive probe** | Liquid level | continuous | capacitance (pF) | RC oscillator → frequency, or C-to-digital |

### Selection heuristics

| Measurement need | Recommended sensor | Why |
|------------------|--------------------|-----|
| Room/household temperature, ±1 °C | NTC thermistor + divider | One-cent part, enough resolution after FW linearization |
| Process temperature, ±0.1 °C, industrial | Pt100 RTD + 3-wire bridge | Linear, stable, accurate across wide range |
| Furnace temperature > 500 °C | Thermocouple (type K) | Survives the heat where RTD/thermistor fail |
| Weight / force / pressure | Strain-gauge load cell (full bridge) | Bridge cancels temperature; HX711 digitizes cheaply |
| Door/position/rpm, magnet-bearing | Hall switch or reed | Non-contact, wear-free, simple conditioning |
| Ambient light on/off (night detection) | LDR + divider | Cheapest; fine for a threshold |
| Precision light measurement | Photodiode + transimpedance amp | Speed + linearity (see photodetector-circuits) |
| Industrial transmitter, 100+ m wiring | Any sensor → 4-20 mA loop | Immune to lead resistance and noise |

---

## Prerequisites

- [Semiconductor Devices](semiconductor-devices.md) — the op-amps (non-inverting, instrumentation), Schmitt triggers, comparators, analog switches, and bandgap references that build every conditioning stage in this article.
- [Passive Components](passive-components.md) — the precision matched resistors of the Wheatstone bridges and dividers, the low-leakage capacitors of the RC filters and debounce networks, and the 250 Ω burden resistor that turns a 4-20 mA loop into a 1-5 V signal.
- [Analog Circuits](analog-circuits.md) — op-amp configurations, Schmitt-trigger hysteresis, and active filter theory (no internals re-derived here).
- [Interface Circuits](interface-circuits.md) — parent capability; the analog/digital bridge of which this article owns the sensor side.

## Scope Boundary

This article covers the **major sensor families and their conditioning circuits**. It does **not** cover:

- **ADC theory and architectures** (sampling, quantization, SAR / flash / sigma-delta) — owned by the sibling [ADC Circuits](interface-circuits.adc-circuits.md) article; sensor outputs are assumed to feed an ADC taught there.
- **Photodiode / phototransistor front-ends** (transimpedance amplifiers, avalanche bias, noise analysis) — owned by [Photodetector Circuits](optoelectronic-circuits.photodetector-circuits.md); light sensors are only recapped here.
- **Thermocouple cold-junction compensation** in full depth — touched on as a row in the parameter table; the detailed analog cold-junction design belongs with precision analog instrumentation, not a major-family survey.
- **Digital-bus smart sensors** (I²C/SPI temperature sensors, MEMS accelerometer digital output) — these push the conditioning onto the sensor IC's silicon; covered under [Computing: embedded systems](../computing/embedded-systems.md).
- **Op-amp and comparator internals** — see [Analog Circuits](analog-circuits.md).

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
