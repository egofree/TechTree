# Oscillator Circuits

> **Node ID**: `electronics.analog-circuits.oscillator-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.amplifier-fundamentals`](analog-circuits.amplifier-fundamentals.md)
> **Outputs**: oscillator-designs
> **Timeline**: Years 25-40
> **Critical**: No — design pedagogy layer; the active devices and resonator crystals come from semiconductor-devices

An oscillator is a circuit that produces a periodic output waveform *with no input signal*. It is the electronic embodiment of a self-sustaining feedback loop: a fraction of the amplifier's output is fed back to its input at exactly the right amplitude and phase, and thermal noise seeds the oscillation until it grows to a stable amplitude. Every clock in every microcontroller, every carrier in every radio transmitter, every tone in every musical synthesizer, and every time base in every oscilloscope traces back to one of the circuits in this article.

The active devices — BJTs, MOSFETs, op-amps, and the quartz crystal itself — are manufactured in [Semiconductor Devices](semiconductor-devices.md). The resistors, capacitors, and inductors that set the frequency are covered in [Passive Components](passive-components.md). This article teaches how to *combine* them into a stable oscillator, without re-deriving device physics or the underlying LC resonance theory (that lives in [AC Analysis](circuit-fundamentals.ac-analysis.md) §7 — read it first; this article assumes you understand `f₀ = 1/(2π√(LC))`, Q factor, and the tank circuit).

This article covers general-purpose oscillators — the audio, ultrasonic, and low-MHz clock sources that every bench needs. RF-specific topologies (VFOs, PLL synthesizers, DDS, microwave cavity oscillators) are out of scope and belong to a later wave.

---

## 1. The Barkhausen Criterion

### The Self-Sustaining Loop

Every sinusoidal oscillator is a feedback amplifier pushed to the edge of instability. Consider the canonical feedback loop:

```
              ┌────────────────┐
   xin ──>(+) │   amplifier A  │──> xout
          ▲   └────────────────┘
          │            │
          │    ┌───────┴───────┐
          │    │ feedback net  │
          │    │   gain = β    │
          │    └───────┬───────┘
          │            │
          └────────────┘
              xfb = β·xout

   Loop gain = A·β
```

For the oscillation to *start* and *sustain itself*, two conditions must hold simultaneously. These are the **Barkhausen criterion**:

1. **Loop-gain magnitude ≥ 1**: `|A·β| ≥ 1`. The signal, after one trip around the loop (through the amplifier and back through the feedback network), must return at least as large as it started. If `|A·β| < 1`, thermal noise decays to silence. If `|A·β| = 1` exactly, the amplitude holds steady. In practice we design for `|A·β| ≈ 1.05–1.2` at startup so oscillation builds from noise, then an amplitude-stabilization mechanism (nonlinear gain reduction, AGC, a clipping diode, or simply the amplifier saturating) brings the loop gain down to exactly 1.0 at the desired output level.

2. **Loop phase shift = 360° (2π) — or any integer multiple of 360°**: the feedback signal must arrive back at the input *in phase* with the existing signal, so it adds constructively rather than canceling. The amplifier itself often contributes 180° of inversion (a common-emitter or inverting op-amp stage), so the feedback network must contribute the remaining 180° at the oscillation frequency.

### Why It Is Not "Infinite Gain"

A common beginner misconception is that `|A·β| > 1` causes runaway to infinity. It would, if the amplifier were perfectly linear. Real amplifiers clip, and a JFET or op-amp's open-loop gain falls as amplitude rises. The system therefore settles at *exactly* the amplitude where `|A·β| = 1` — the loop gain reduces itself to unity via nonlinearity. This is why pure-sinusoidal oscillators need *gentle* amplitude limiting (a slow AGC, a small lamp with positive temperature coefficient in the Wien bridge) to keep distortion low, while square-wave relaxation oscillators rely on hard clipping and care nothing about distortion.

### The Two Design Questions

Every oscillator design reduces to answering two questions:

| Question | Answered by | Mechanism |
|----------|-------------|-----------|
| *At what frequency* does phase = 360°? | The frequency-selective feedback network | RC ladder, Wien bridge, LC tank, or crystal |
| *Is the gain enough* at that frequency? | The active device's gain, compared to the network's loss | Loop-gain check: `|Aβ| ≥ 1` |

The oscillator families below are distinguished entirely by *how* the feedback network answers the first question. RC oscillators use a resistor-capacitor phase-shift network. LC oscillators use an inductor-capacitor tank. Crystal oscillators use the mechanical resonance of a piezoelectric quartz plate. Relaxation oscillators abandon sine waves entirely and use a comparator's hysteresis.

---

## 2. RC Oscillators

RC oscillators use only resistors and capacitors (no inductors) to set the frequency, making them ideal for the audio-to-low-ultrasonic range (1 Hz to ~1 MHz), where inductors would be bulky, lossy, and hard to wind. The trade-off is poor frequency stability — RC tolerances are ±5–20% and they drift with temperature.

### RC Phase-Shift Oscillator

The classic teaching oscillator. An inverting amplifier (common-emitter BJT or inverting op-amp, contributing 180°) drives a *ladder* of three RC high-pass stages. Each RC stage contributes 60° of phase shift at the oscillation frequency, for 3 × 60° = 180° from the network. Total: 180° (amplifier) + 180° (network) = 360°. Barkhausen's phase condition is met.

```
                       C1        C2        C3
              ┌──┤├──┬──┤├──┬──┤├──┬────────┐
              │      │      │      │        │
             R1     R2     R3     Rload     │
              │      │      │      │        │
             GND    GND    GND    GND       │
              └─ -60°┘─ -60°┘─ -60°┘        │
                                          │
              ┌───────────────┐            │
              │  inverting    │ xout ──────┘ (feedback tap
              │  amplifier    │                  at last cap)
              │   gain = -A   │
              └───────┬───────┘
                      │
                      └── first RC stage driven here (signal xin + xfb)

   3 stages × 60° = 180° network shift
   + 180° amplifier inversion = 360° total → oscillation
```

For the standard 3-stage equal-value design (R₁ = R₂ = R₃ = R, C₁ = C₂ = C₃ = C), the oscillation frequency and required gain are:

```
f_osc = 1 / (2π·R·C·√6)   ≈   1 / (15.4·R·C)

Required amplifier gain |A| ≥ 29    (the network attenuates by 1/29)
```

The √6 factor comes from solving the phase condition of the 3-stage ladder; the gain of 29 is the network's insertion loss at the oscillation frequency (the amplifier must overcome it). This is why you rarely see phase-shift oscillators built with a single low-gain transistor — most single-BJT stages only manage |A| ≈ 20–50 at best, leaving little margin. An op-amp is the modern choice.

### Wien-Bridge Oscillator

The Wien-bridge oscillator is the *premium* RC oscillator: it produces very low-distortion sine waves by using a *non-inverting* amplifier (zero phase shift) and a lead-lag network that contributes 0° net shift at the oscillation frequency. The amplitude is stabilized by a small nonlinear element — historically a tungsten-filament lamp whose resistance rises with heating, providing smooth AGC. Hewlett-Packard's first product (the 1938 HP200A audio oscillator) was a Wien-bridge design, and the lamp-stabilized topology is still the textbook low-distortion sine source.

```
          R1            C1 (series)
   xout ──/\/\/\──┬─────┤├─────┬── xin'  (to + input of amp)
                   │             │
                   │            R3 (shunt)
                   │            ┤├ C3
                   │             │
                  GND           GND

        └─ lead-lag network: 0° phase shift at f = 1/(2π·R·C)
           attenuation = 1/3 at f_osc

   ┌────────────────────────┐
   │  non-inverting op-amp  │── xout
   │  gain = 1 + Rf/Rg = 3  │      (gain set just above 3)
   └───────────┬────────────┘
               │ (+) input ← xin' from network above
               │
          Rf ──/\/\/\──┐   (Rf is often the lamp: R rises with
                         │    amplitude, gain drops to exactly 3 → low distortion)
          Rg ──/\/\/\──┘
               │
              GND

   Oscillation condition: gain × (1/3) = 1  →  gain = 3
   f_osc = 1 / (2π·R·C)
```

For the Wien network (with R₁=R₃=R, C₁=C₃=C), at the frequency where the phase shift is exactly 0°, the network transfer function peaks at 1/3 with zero phase:

```
f_osc = 1 / (2π·R·C)

Required amplifier gain ≥ 3      (the network passes exactly 1/3 of the output)
```

The lamp trick: a small incandescent bulb in the Rf position has a cold resistance of, say, 100 Ω. As the output amplitude grows, the bulb heats, its resistance rises to perhaps 200 Ω, and the closed-loop gain `1 + Rf/Rg` falls toward exactly 3.0 — gently and smoothly, with no clipping. The result is THD (total harmonic distortion) below 0.1%, far better than any phase-shift or LC oscillator. Modern versions replace the lamp with a JFET used as a voltage-controlled resistor.

---

## 3. LC Oscillators

For frequencies above ~100 kHz, RC networks require inconveniently small capacitors and large phase shift. LC oscillators replace them with a parallel inductor-capacitor **tank** — the same resonant circuit analyzed in [AC Analysis §7](circuit-fundamentals.ac-analysis.md). At resonance (`f₀ = 1/(2π√(LC))`) the tank presents a purely resistive impedance and the inductor/capacitor voltages are in phase opposition (180° apart) and Q times larger than the source. The tank *itself* selects the frequency; the active device only replenishes the energy lost to parasitic resistance.

The three classic LC topologies differ only in *how* they tap the tank to extract a feedback signal:

### Colpitts Oscillator (Capacitive Divider Feedback)

The Colpitts uses two capacitors in series (C₁, C₂) across the inductor L. The junction of C₁ and C₂ is grounded (or tied to the emitter), and the feedback is taken from the capacitive divider. This is the most popular LC oscillator because C₁ and C₂ are stable, cheap, and easy to obtain in close tolerances.

```
                                  L
                       ┌──[UUUUUUUUUU]──┐
                       │                 │
                       │       Q1 (BJT)  │
            C1   ┌─────┴────┐    ┌───────┴── Vcc via RFC
        ───┤├────┤  emitter │    │  collector
              │   │  (common│    │
              │   │   base) │    │
              ●───┤         │    │
              │   └────┬────┘    │
              │        │         │
            C2    bias network  output tap (from collector)
              │   (R1,R2,Re)    │
             GND       │        │
                       GND      ●─── xout

   Tank: C1 in series with C2, parallel with L.
   C_eq = C1·C2 / (C1 + C2)    (series combination)
   Feedback ratio = C1/C2 (fraction fed to emitter).
```

The resonant frequency uses the *series equivalent* of the two capacitors:

```
f_osc = 1 / (2π·√(L·C_eq))

   where  C_eq = (C1·C2) / (C1 + C2)      (series equivalent)

   Oscillation condition: transistor gm·X_C2 ≥ some minimum
   (roughly: loop gain ≥ 1; the capacitive ratio sets feedback fraction)
```

### Hartley Oscillator (Inductive Divider Feedback)

The Hartley is the mirror image of the Colpitts: it uses a *tapped inductor* (two windings L₁, L₂ on one core, or a single inductor with a tap) and a single capacitor. The feedback is taken from the inductive divider. Hartleys were dominant in tube-era radios because variable inductors (with a wiper or slider) were easier to build than variable capacitors; today the Colpitts is preferred because capacitors are cheaper and more stable.

```
                       L1        L2
                ┌─[UUUUUUU]─●─[UUUUUUU]─┐
                │          │            │
                │       (tap)           │
                │          │            │
                │          │            C   (single cap, shunts the whole tank)
                │          │            │
                │      emitter of Q1    │
                │      (common base)    │
                │                        │
              GND                      ──Vcc

   Tank: L1 + L2 (series, magnetically coupled or not) parallel with C.
   L_eq = L1 + L2 (+ 2M if mutual coupling M)
   Feedback ratio = L2/L1 (inductive divider).
```

```
f_osc = 1 / (2π·√(L_eq·C))

   where  L_eq = L1 + L2   (add 2·M if the windings are coupled)
```

### Clapp Oscillator (Series-Tuned Colpitts)

The Clapp adds a small capacitor C₃ *in series* with the LC tank of a Colpitts. Because C₃ is much smaller than C₁ and C₂, it dominates the resonant frequency — and since a single small capacitor has far better stability than the transistor's internal capacitances (which appear across C₁ and C₂ and vary with temperature and bias), the Clapp is the most stable of the three LC oscillators. It is the bridge between simple LC oscillators and crystal oscillators.

```
f_osc = 1 / (2π·√(L·C_eff))

   where 1/C_eff = 1/C1 + 1/C2 + 1/C3   (all three in series)
   since C3 << C1, C2:   C_eff ≈ C3     → f_osc ≈ 1/(2π·√(L·C3))
```

### Worked Example — Colpitts at 1 MHz

Design a Colpitts oscillator to run at approximately 1 MHz using L = 10 µH and equal-value feedback capacitors C₁ = C₂ = 2.5 nF.

**Step 1: Find the series-equivalent capacitance.**

```
C_eq = (C1·C2) / (C1 + C2)
     = (2.5 nF × 2.5 nF) / (2.5 nF + 2.5 nF)
     = (6.25 nF²) / (5.0 nF)
     = 1.25 nF
```

**Step 2: Compute the oscillation frequency.**

```
f_osc = 1 / (2π·√(L·C_eq))
      = 1 / (2π·√(10×10⁻⁶ × 1.25×10⁻⁹))
      = 1 / (2π·√(1.25×10⁻¹⁴))
      = 1 / (2π × 1.118×10⁻⁷)
      = 1 / (7.025×10⁻⁷)
      ≈ 1.42 MHz
```

**Result and correction.** The given values land the oscillator at **1.42 MHz**, about 42% high. To hit the design target of exactly 1.0 MHz, increase the capacitance. Solve for the required C_eq:

```
C_eq_required = 1 / ((2π·f)²·L)
              = 1 / ((2π × 1×10⁶)² × 10×10⁻⁶)
              = 1 / (3.948×10¹³ × 1×10⁻⁵)
              = 1 / (3.948×10⁸)
              ≈ 2.53 nF
```

With equal capacitors, `C_eq = C/2`, so each cap must be `2 × 2.53 nF = 5.06 nF`. Choose the nearest standard value, **C₁ = C₂ = 5.1 nF** (E12 series), giving C_eq = 2.55 nF and:

```
f_osc = 1 / (2π·√(10 µH × 2.55 nF)) ≈ 0.996 MHz      ✓ (within 0.4%)
```

**Step 3: Check loop gain.** The feedback fraction is C₁/C₂ = 1.0 (equal caps). With a transistor gm of 20 mS (a 2N3904 at I_C ≈ 0.5 mA) and X_C2 = 1/(2π·1 MHz·5.1 nF) ≈ 31 Ω, the loop-gain product gm·X_C2 ≈ 0.6 — adequate for a Colpitts (which oscillates readily once gm·X_C2 > ~0.2). The oscillator will start reliably.

---

## 4. Crystal Oscillators

A quartz crystal is the highest-Q resonator available without resorting to a microwave cavity. It works by the **piezoelectric effect**: mechanical stress on the quartz plate produces a voltage, and an applied voltage produces mechanical strain. The plate therefore behaves electrically as a series RLC circuit (its mechanical resonance) in parallel with a static capacitance C₀ (the electrodes), all packaged in a tiny metal can.

```
   Crystal electrical equivalent (Butterworth-Van Dyke model):

        ┌── C₀ ──┐         (C₀ = electrode shunt capacitance, ~3-7 pF)
   ┌────┤        ├────┐
   │    └────────┘    │
   │     ┌── R_s ──┐  │     (R_s = motional resistance, ~10-100 Ω)
   ●─────┤         ├──●     (L_m = motional inductance, ~mH to H!)
   │     └── L_m ──┘  │     (C_m = motional capacitance, ~fF)
   │     └── C_m ──┐  │
   │     ┌─────────┘  │
   └──────────────────┘

   Q = (1/R_s)·√(L_m / C_m)   ≈ 10,000 to 1,000,000+
   (vs. Q ≈ 50-200 for a discrete LC tank)

   Series resonance:   f_s = 1 / (2π·√(L_m·C_m))
   Parallel resonance: f_p = f_s·√(1 + C_m/C₀)    (slightly above f_s)
```

The extraordinary Q (10,000–1,000,000+) comes from the mechanical inertia of the quartz plate — L_m is enormous (millihenries to henries) while C_m is tiny (femtofarads), a combination impossible to achieve with physical inductors and capacitors. The result is frequency stability measured in **parts per million (ppm)**: a cheap crystal holds ±50 ppm over 0–70 °C, a temperature-compensated crystal oscillator (TCXO) holds ±2 ppm, and an oven-controlled crystal oscillator (OCXO) holds ±0.01 ppm. Compare this to an LC oscillator's ±1000 ppm and an RC oscillator's ±10,000 ppm.

The **AT-cut** crystal is the most common cut (the plate is sliced from the quartz at an angle of ~35° to the optical axis). It provides an inflection in its temperature-frequency curve near 25 °C, giving excellent stability around room temperature. AT-cut crystals operate in *thickness-shear* mode, with frequency inversely proportional to plate thickness: a 1 MHz crystal is ~1.7 mm thick; a 20 MHz crystal is ~83 µm thick; fundamental-mode operation becomes impractical above ~30–40 MHz because the plate is too thin to manufacture. Higher frequencies use **overtone** operation (3rd, 5th, 7th odd mechanical overtones), which are near — but not exactly — integer multiples of the fundamental.

### Pierce Crystal Oscillator

The Pierce is the most common crystal oscillator circuit — it is the one used inside virtually every microcontroller (the "crystal input" pins). It uses a single inverting digital gate (a CMOS inverter biased into its linear region by a feedback resistor Rf of ~1 MΩ) as the amplifier, with the crystal providing the 180° phase shift and the two load capacitors (C₁, C₂) completing the π-network.

```
                 Rf (~1 MΩ, biases inverter into linear region)
              ┌──────/\/\/\──────┐
              │                  │
        C1   │   ┌────────────┐  │   C2
   XOUT ─┤├──┴───┤   CMOS     ├──┴──┤├── XIN
              │    │  inverter  │   │
              │    │  (NOT gate)│   │
              │    └─────┬──────┘   │
              │          │          │
              │      ┌───┴───┐      │
              │      │ XTAL  │      │
              │      │ quartz│      │
              │      │1-30MHz│      │
              │      └───┬───┘      │
             GND        GND        GND

   The crystal acts as a high-Q inductor at the operating frequency.
   C1, C2 + stray capacitance form the load capacitance C_L:
       C_L = (C1·C2)/(C1+C2) + C_stray
   Crystal is specified for a load cap (e.g. 18 pF, 20 pF) —
   choose C1 = C2 = 2·(C_L - C_stray)   (C_stray ≈ 5-7 pF)
```

For a 16 MHz crystal specified with C_L = 18 pF, and assuming C_stray = 5 pF:

```
C1 = C2 = 2·(C_L - C_stray) = 2·(18 - 5) = 26 pF    → use 27 pF standard
```

The Pierce's appeal is simplicity: one gate, one crystal, two caps, one feedback resistor. The digital output is a clean square wave suitable for clocking logic. For a purer sine wave, the crystal is moved into a Colpitts-style circuit (the Clapp / Butler / Miller topologies) with a transistor front-end.

---

## 5. Relaxation Oscillators

A relaxation oscillator abandons the sinusoidal waveform entirely. It charges a capacitor through a resistor until the voltage reaches an upper threshold, then *discharges* (or charges negative) until a lower threshold is reached, then repeats. The output is a square wave, triangle wave, or sawtooth — never a clean sine. The advantage is extreme simplicity: one op-amp or comparator, one capacitor, two or three resistors. The disadvantage is poor frequency accuracy and stability — but for applications that only need "a periodic pulse" (blink an LED, clock a counter, sweep a scope), the relaxation oscillator is unbeatable.

```
                 R (charge resistor)
   Vcc ──/\/\/\──────┬──────┐
                      │      │
                      ●──────┤(+)
                     C │     │
                      │   ┌──┴──┐  op-amp / comparator
                     GND  │     │  with HYSTERESIS (Schmitt trigger)
                          │     │
                          └──┬──┘
                             │(-)
   Feedback divider R1/R2 sets thresholds:
       V_high = Vcc · R2/(R1+R2)        (charge until V_C reaches this)
       V_low  = -Vcc · R2/(R1+R2)       (discharge until V_C reaches this)

   Output: square wave. Capacitor voltage: triangle/exponential.
```

The period depends on the RC time constant and the hysteresis band:

```
T = 2·R·C·ln( (Vcc + V_high) / (Vcc - V_high) )

   For symmetric thresholds at ±Vcc/3:
   T ≈ 2.2·R·C        f ≈ 0.45 / (R·C)
```

Relaxation oscillators are the spiritual ancestor of the 555 timer (covered in [Timer Circuits](analog-circuits.timer-circuits.md)) — the 555 simply integrates the comparators, flip-flop, and discharge transistor into one 8-pin package.

---

## Parameter Table — Oscillator Type Selection

| Oscillator type | Frequency range | Stability (over 0–60 °C) | Distortion (THD) | Typical application |
|-----------------|-----------------|--------------------------|------------------|---------------------|
| RC phase-shift | 1 Hz – 100 kHz | ±5–20% (poor) | 1–5% | Cheap teaching lab sine source, rough audio tone |
| Wien-bridge (lamp-stabilized) | 10 Hz – 1 MHz | ±1–2% | 0.01–0.1% | Low-distortion audio test oscillator, function generator |
| Colpitts (LC) | 30 kHz – 300 MHz | ±0.1–1% (±1000 ppm) | 1–5% | RF local oscillator, variable-frequency oscillator (VFO) |
| Hartley (LC) | 30 kHz – 100 MHz | ±0.1–1% | 1–5% | Old-style tube radios (tapped-coil tuning) |
| Clapp (LC) | 100 kHz – 100 MHz | ±0.05–0.5% (best LC stability) | 1–5% | VFO needing decent frequency stability |
| Pierce (crystal) | 32 kHz – 30 MHz | ±20–50 ppm | square wave (rich harmonics) | MCU clock, digital logic clock, RTC |
| Miller / Butler (crystal) | 1 MHz – 30 MHz | ±10–30 ppm | <1% (sine output) | Precision frequency standard, RF transmitter reference |
| TCXO (temp-compensated crystal) | 1 MHz – 40 MHz | ±1–2 ppm | square / clipped sine | GPS, cellular baseband, precision timing |
| OCXO (oven-controlled crystal) | 5 MHz – 20 MHz | ±0.001–0.01 ppm | sine | Frequency counter reference, rubidium fallback |
| Relaxation (op-amp) | 0.1 Hz – 1 MHz | ±5–20% (poor) | square/triangle | LED flasher, sweep generator, clock divider seed |

## Design Checklist

- [ ] Chosen RC, LC, or crystal based on required frequency stability (RC ≥ ±1%, LC ≈ ±0.1%, crystal ≤ ±50 ppm).
- [ ] Verified Barkhausen phase condition: 360° total (amplifier inversion + network shift).
- [ ] Computed loop gain |A·β| and confirmed ≥ 1 with startup margin (design for 1.05–1.2).
- [ ] For LC oscillators: confirmed C₁, C₂ large enough to swamp transistor stray capacitances (C₁, C₂ ≫ C_internal).
- [ ] For crystal oscillators: computed load capacitance C_L and selected C₁, C₂ so that (C₁·C₂)/(C₁+C₂) + C_stray matches the crystal's specified C_L.
- [ ] Provided amplitude stabilization (lamp, AGC, JFET, or soft clipping) for low-distortion sine outputs.
- [ ] Decoupled the power supply (0.1 µF ceramic close to the device) so supply ripple does not modulate the frequency.
- [ ] For variable-frequency designs, verified the tuning range does not push the loop gain below 1 (oscillation dropout) or into hard saturation (distortion).

## See Also

- [Analog Circuits](analog-circuits.md) — the parent capability hub: scope, progression, and sibling articles.
- [Timer Circuits](analog-circuits.timer-circuits.md) — the sibling article: the 555 timer is a packaged, precision relaxation oscillator with comparators and a flip-flop on one chip.
- [Semiconductor Devices](semiconductor-devices.md) — how the BJTs, MOSFETs, op-amps, and the quartz crystal resonators are manufactured.
- [Passive Components](passive-components.md) — the resistors, capacitors, and inductors every oscillator above relies on for frequency selection.
- [AC Analysis](circuit-fundamentals.ac-analysis.md) §7 — the resonance theory (f₀, Q, bandwidth) that LC oscillators are built upon; this article links rather than re-derives.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
