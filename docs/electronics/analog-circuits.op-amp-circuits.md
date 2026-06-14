# Op-Amp Circuits

> **Node ID**: `electronics.analog-circuits.op-amp-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.amplifier-fundamentals`](analog-circuits.amplifier-fundamentals.md)
> **Outputs**: op-amp-circuit-designs
> **Timeline**: Years 20-35
> **Critical**: No — design pedagogy layer; the underlying op-amp IC manufacturing (semiconductor-devices) and the resistors/capacitors (passive-components) are the critical prerequisites

The operational amplifier is the most versatile analog integrated circuit ever built. A single 8-pin package, two supply rails, and a handful of resistors and capacitors replace rooms full of carefully biased discrete-transistor stages. This article teaches the **design pedagogy**: the ideal model that makes every equation linear, the canonical closed-loop topologies (inverting, non-inverting, follower, summing, difference), integration and differentiation, the comparator and Schmitt trigger with hysteresis, and the active filters that replace bulky inductors with op-amp gain. It is the third rung of the [analog-circuits](analog-circuits.md) ladder, sitting above amplifier fundamentals.

This article does **not** cover the 555 timer (that is [timer-circuits](analog-circuits.md)), does not re-derive passive-filter theory (see [filter-circuits](power-supply-circuits.filter-circuits.md) for cutoff frequencies and roll-off), and does not re-teach how the op-amp IC is physically manufactured — that belongs to [semiconductor devices](semiconductor-devices.md). We treat the op-amp as a catalog part with a datasheet.

## The Ideal Op-Amp Model

An op-amp is a high-gain differential amplifier: it amplifies the voltage *difference* between its two inputs by a very large factor.

```
                    V+ (non-inverting input)
                     │
                     ├───▶│\
                     │    │ \   A_OL  (open-loop gain,
                    ─┤    │  \    very large: 10^5 to 10^6)
                     │    │   ├───────▶ V_out
                     ├───▶│  /
                     │    │ /
                    V- (inverting input)
```

The **ideal op-amp** has four properties that make every design equation a one-line algebra result:

| Parameter | Ideal | Symbol |
|-----------|-------|--------|
| Open-loop gain | infinite | A_OL → ∞ |
| Input impedance | infinite | Z_in → ∞ (no current into either input) |
| Output impedance | zero | Z_out → 0 (drives any load) |
| Bandwidth | infinite | (gain flat to DC) |
| Input bias current | zero | I_B = 0 |
| Input offset voltage | zero | V_os = 0 |

### The Golden Rules

With **negative feedback** (a fraction of the output wired back to the inverting input), the ideal model collapses to two rules that solve essentially every circuit:

1. **No current flows into either input** (infinite Z_in). The inputs draw nothing.
2. **The op-amp drives its output so that V+ = V−** (the *virtual short* or *virtual ground*). Because A_OL is enormous, the input difference must be ≈ 0 for the output to sit anywhere finite: V_out = A_OL × (V+ − V−), so (V+ − V−) = V_out / A_OL ≈ 0.

These two rules — no input current, and equal input voltages — are the entire analytical engine of this article. They are approximations; the [real-world parameter table](#real-op-amp-parameter-table) below shows how close modern ICs come.

## Basic Closed-Loop Topologies

### Inverting Amplifier

The input signal drives the inverting (−) input through R_in; the output is fed back through R_f. The non-inverting (+) input is grounded. By the golden rules, the − input is a **virtual ground** (held at 0 V by feedback) and draws no current, so all of R_in's current flows through R_f.

```
                      R_f
              ┌────█████────┐
              │             │
   Vin ──█████─├─\          │
          R_in │  \         │
               │   ├────────┴──▶ V_out
          ┌────┤  /
          │    │ /
          │    └─
          ▼
         GND (V+ = 0)

   V- is a VIRTUAL GROUND (held at 0 by feedback)
   I_in = Vin / R_in  flows entirely through R_f
   V_out = -I_in × R_f = -(R_f / R_in) × Vin
```

**Gain**: A_v = V_out / V_in = **−R_f / R_in** (the minus sign = inversion).

Input impedance = R_in (because V− is a virtual ground). Output impedance ≈ 0.

### Non-Inverting Amplifier

The input drives the (+) input directly. The feedback divider (R_f over R_in to ground) sets the gain. By the virtual short, V− = V+ = V_in, so the divider voltage equals V_in.

```
                    ┌──────────────┐
                    │              │
   Vin ──┬──────────┤+ \           │
         │          │   \          │
         │          │    ├─────────┴──▶ V_out
         │          │   /     │
         │          │-/       │
         │     ┌────┘         │
         │     │              │
         │    ─┤─  (V- = Vin) │
         │     │         R_f  │
         │     ├────████──────┘
         │     │
         │    ─┤─
         │     │
         ▼     ▼
        R_in  GND
        █████
```

**Gain**: A_v = **1 + R_f / R_in** (always positive, always ≥ 1).

Input impedance = ideal-∞ (in practice, the IC's common-mode input impedance, typically 10^12 Ω for FET-input parts). Output impedance ≈ 0.

### Voltage Follower (Buffer)

A non-inverting amplifier with R_f = 0 and R_in = open. The output is wired straight back to V−. Gain = 1 + 0/∞ = 1.

```
   Vin ──┬──────────┤+ \
         │          │   \
         │          │    ├───────▶ V_out
         │          │   /    │
         │          │-/      │
         │     ┌────┘        │
         └─────┴─────────────┘
              (feedback = short)

   V_out = Vin  (gain = +1)
```

The follower is the universal **impedance matcher**: it presents an infinite input impedance to a weak source and a zero output impedance to a heavy load. It is the analog of a mechanical torque converter — it isolates stages so a high-impedance sensor can drive a low-impedance cable without signal loss.

### Summing Amplifier (Inverting Adder)

An extension of the inverting amplifier: multiple inputs each feed the virtual-ground node through their own resistor. Because the summing junction is at 0 V, the inputs do not interact.

```
   V1 ──█████─┐
        R1   │
   V2 ──█████─┼─── V- (virtual ground) ──┤-\
        R2   │                          │  \
   V3 ──█████─┤                          │   ├────▶ V_out
        R3   │            R_f           │  /
        ┌────┼──────────█████───────────┤+→GND
        │    │
        ▼    ▼
       GND  GND

   V_out = -(R_f/R1·V1 + R_f/R2·V2 + R_f/R3·V3)

   If R1 = R2 = R3 = R:  V_out = -(R_f/R)·(V1 + V2 + V3)
```

This is the heart of every analog mixer and every R-2R digital-to-analog converter. With equal input resistors it is a true voltage adder; with unequal resistors it is a weighted sum.

### Difference Amplifier (Subtractor)

A single op-amp that amplifies the difference between two inputs. R_in on the − side and R_g on the + side form the two divider paths.

```
              R_f
   V1 ──█████─┬────█████─┬──▶├─\
        R_in  │          │   │  \
              ├───┤-         │   ├────▶ V_out
              │   └────█████─┤+/
   V2 ──█████─┤        R_g   │
        R_g   │              │
              │              │
              ▼              │
             GND             ▼
                            GND (via R_in)

   If all four resistors are equal R:
       V_out = V2 - V1
   If R_f = R_in matched:
       V_out = (R_f/R_in) × (V2 - V1)
```

The difference amplifier is the front end of every instrumentation system: it extracts the small voltage across a bridge sensor while rejecting the large common-mode voltage both leads sit on. Precision depends on resistor **matching** — a 1% mismatch between the four resistors limits common-mode rejection to about 48 dB.

## Integration and Differentiation

Swapping the feedback or input resistor for a capacitor turns the op-amp into a **mathematical operator** in the time domain. These two circuits are the analog ancestors of every digital filter and PID controller.

### Integrator

Replace R_f in the inverting amplifier with a capacitor C. The current through R_in charges the capacitor, and the output is the (inverted) integral of the input.

```
                      C
              ┌──────||─────┐
              │             │
   Vin ──█████─├─\          │
          R_in │  \         │
               │   ├────────┴──▶ V_out
          ┌────┤  /
          │    │ /
          │    └─
          ▼
         GND

   I = Vin / R_in  charges C continuously
   V_out = -(1/RC) · ∫ Vin dt
```

A constant +V_in produces a negative-going voltage ramp at the output — the circuit literally *accumulates* input over time. Practical integrators need a high-value reset resistor in parallel with C (or a reset switch) to bleed off the offset-voltage integration that would otherwise slowly saturate the output.

### Differentiator

Swap R and C: put C in the input path and R in the feedback. The output is the (inverted) time-derivative of the input.

```
                      R_f
              ┌────█████────┐
              │             │
   Vin ───||──├─\          │
          C   │  \         │
               │   ├────────┴──▶ V_out
          ┌────┤  /
          │    │ /
          │    └─
          ▼
         GND

   V_out = -RC · (dVin/dt)
```

The differentiator outputs a spike whenever the input changes; a steady input gives zero output. It amplifies high-frequency noise (gain rises with frequency), so practical differentiators add a small series resistor to C to roll off the gain above the band of interest.

## Comparator and Schmitt Trigger

Run an op-amp **without negative feedback** (open loop) and its enormous gain turns it into a **comparator**: any input difference larger than a few microvolts slams the output to one supply rail or the other. A comparator is a 1-bit analog-to-digital converter.

```
   V_in ───────┤+ \
                │   \
   V_ref ──────┤-    ├──────▶ V_out
                │   /        (saturates to +Vcc or -Vee)
                │-/
```

If V_in > V_ref, output → +Vcc. If V_in < V_ref, output → −Vee. (Dedicated comparator ICs like the LM311 switch faster and tolerate larger saturation than op-amps used as comparators, but a 741 works for slow signals.)

### The Problem: Noise Chatter

A plain comparator with a noisy input crossing the threshold slowly will *chatter* — its output flips rapidly back and forth as the input wiggles through V_ref.

### Schmitt Trigger — Hysteresis Cures Chatter

Add **positive feedback** (a fraction of the output fed to the + input). Now the threshold itself *shifts* depending on the current output state. The circuit has **memory**: once it switches high, the input must fall significantly further to switch it back. The gap between the upper and lower thresholds is the **hysteresis**.

```
                          R_f
              ┌──────────█████──────────┐
              │                         │
              ├────────────┐            │
              │            │            │
   Vin ──█████─├─\         │            │
         R_in  │  \        │            │
               │   ├───────┴────────────┴──▶ V_out
          ┌────┤  /
          │    │ /     R_g
          │    └─  ┌────█████────┐
          │         │            │
          ▼         ▼            ▼
         GND       GND          GND

   (Inverting Schmitt: Vin drives − input via R_in,
    positive feedback to + input via R_f/R_g divider)
```

**Threshold calculations** (inverting Schmitt, output saturates at ±V_sat):

```
   V+ is set by the R_f / R_g divider on V_out:

       V+ = V_out · R_g / (R_g + R_f)      (+ input at virtual divider)

   Upper threshold (V_out = +V_sat, going DOWN through it switches LOW):
       V_T+ = +V_sat · R_g / (R_g + R_f)

   Lower threshold (V_out = -V_sat, going UP through it switches HIGH):
       V_T- = -V_sat · R_g / (R_g + R_f)

   Hysteresis width = V_T+ - V_T- = 2·V_sat·R_g / (R_g + R_f)
```

See the [worked Schmitt example](#worked-example-2-schmitt-trigger-with-2-v-hysteresis) below for the design math.

## Active Filters

A [passive RC filter](power-supply-circuits.filter-circuits.md) rolls off at 20 dB/decade per reactive element and cannot produce voltage gain. An **active filter** wraps an op-amp around the RC network to (a) provide gain in the passband, (b) sharpen the roll-off without inductors, and (c) present a high input / low output impedance so filter stages can be cascaded without loading each other. We do not re-derive the passive cutoff theory here — see [filter-circuits](power-supply-circuits.filter-circuits.md) for f_c = 1/(2πRC) and the 20 dB/decade roll-off.

### First-Order Sallen-Key Low-Pass

The Sallen-Key topology is a second-order filter built from one op-amp, two resistors, and two capacitors. It is the workhorse active filter — unity-gain (follower) configuration is simplest; the version below shows gain.

```
   Vin ──█████─┬───█████─┬───┤+ \            ┌──▶ V_out
         R1   │    R2   │   │   \            │
              │         │   │    ├───────────┘
            ─┤─       ─┤─   │   /   (output fed to +,
            C1        C2    │-/     so V+ = V_out)
              │         │   │
              │         └───┘
              ▼
             GND

   Second-order low-pass: 40 dB/decade roll-off above f_c
   f_c = 1 / (2π √(R1·R2·C1·C2))
   Q (peaking) set by ratio of components and gain
```

For the common case R1 = R2 = R and C1 = C2 = C, the cutoff is f_c = 1/(2πRC) — the same formula as the passive RC filter — but the roll-off is 40 dB/decade (twice as steep) and the op-amp buffers the output.

### First-Order Sallen-Key High-Pass

Swap R and C positions: capacitors in series, resistors to ground. Same topology, same f_c, opposite response — passes high frequencies, blocks DC and lows.

```
   Vin ───||───┬────||────┬───┤+ \          ┌──▶ V_out
         C1   │    C2    │   │   \          │
              │          │   │    ├─────────┘
            ─┤─        ─┤─   │-/
            R1         R2    │
              │          │   │
              ▼          ▼   ▼
             GND        GND GND
```

### Band-Pass (Cascaded or Multiple-Feedback)

A band-pass filter passes a band of frequencies between a lower and upper cutoff. The simplest realization cascades a high-pass stage (f_c1) and a low-pass stage (f_c2) with f_c1 < f_c2; the [filter-circuits](power-supply-circuits.filter-circuits.md) article covers the center-frequency and bandwidth math (f_0 = √(f_c1·f_c2), BW = f_c2 − f_c1, Q = f_0/BW). The op-amp's buffering role is what lets the two stages coexist without one loading the other down.

## Worked Example 1: Inverting Amplifier with A_v = −10

**Design goal**: An inverting amplifier with a voltage gain of −10 (magnitude 10, inverted polarity) for audio frequencies (20 Hz–20 kHz), using a TL072 op-amp on ±12 V supplies.

### Step 1 — Pick the gain ratio

```
   A_v = -R_f / R_in = -10
   ⇒  R_f / R_in = 10
```

### Step 2 — Choose standard values

```
   Let R_in = 10 kΩ  (a convenient audio input impedance)
   Then R_f = 10 × R_in = 100 kΩ  (standard E12 value)
```

Check: A_v = −100k / 10k = **−10** ✓

### Step 3 — Bandwidth check

The TL072 has a gain-bandwidth product of 3 MHz. The closed-loop bandwidth is GBW / |A_v|:

```
   BW = 3 MHz / 10 = 300 kHz
```

300 kHz ≫ 20 kHz audio band, so the gain is flat across the entire audio range with 15× margin. ✓

### Step 4 — Slew-rate check

The TL072 slew rate is 13 V/µs. The maximum sine-wave frequency before slew-induced distortion at a given peak output amplitude V_p is:

```
   f_max(slew) = SR / (2π·V_p) = 13×10^6 / (2π · 10) = 207 kHz
```

At V_p = 10 V (±12 V supplies allow ≈ ±10 V swing), full-power bandwidth is 207 kHz — far above the 20 kHz audio band. ✓

### Step 5 — DC considerations

The TL072 is a FET-input op-amp; input bias current is ~65 pA, negligible across 10 kΩ. Input offset voltage (3 mV typ) appears at the output multiplied by the noise gain (1 + R_f/R_in = 11): V_out(offset) ≈ 33 mV. For audio (AC-coupled) this is irrelevant; for DC-coupled measurement, use an offset-null trimmer or a lower-offset part (OP07, OPAxxx).

### Summary

```
   ┌───────────────────────────────────────────────┐
   │  Inverting amp, A_v = -10, audio:             │
   │  • R_in: 10 kΩ                                │
   │  • R_f:  100 kΩ                               │
   │  • Op-amp: TL072 (or LM358 for single-supply) │
   │  • Bandwidth: 300 kHz (15× margin over audio) │
   │  • Slew-safe to 207 kHz at ±10 V swing        │
   └───────────────────────────────────────────────┘
```

## Worked Example 2: Schmitt Trigger with ±2 V Hysteresis

**Design goal**: An inverting Schmitt trigger on ±12 V supplies (V_sat ≈ ±10 V) with a total hysteresis width of 4 V (−2 V to +2 V thresholds), so that any noise smaller than ±2 V cannot cause chatter.

### Step 1 — Threshold spec

```
   V_T+ = +2 V  (output is HIGH; input must rise above +2 V to switch LOW)
   V_T- = -2 V  (output is LOW; input must fall below -2 V to switch HIGH)
   Hysteresis = V_T+ - V_T- = 4 V
```

### Step 2 — Relate thresholds to the feedback divider

For an inverting Schmitt with the + input driven by a divider from V_out:

```
   V_T+ = +V_sat · β      where β = R_g / (R_g + R_f)
   V_T- = -V_sat · β
```

Solve for β from V_T+:

```
   β = V_T+ / V_sat = 2 / 10 = 0.2
```

### Step 3 — Pick resistor values

```
   β = R_g / (R_g + R_f) = 0.2
   ⇒  R_g / R_f = 0.2 / 0.8 = 1/4

   Let R_g = 10 kΩ  ⇒  R_f = 4 × R_g = 40 kΩ
   (use 39 kΩ standard + 1 kΩ trim, or 40.2 kΩ 1%)
```

### Step 4 — Verify

```
   β = 10k / (10k + 40k) = 10/50 = 0.2 ✓
   V_T+ = +10 × 0.2 = +2.0 V ✓
   V_T- = -10 × 0.2 = -2.0 V ✓
   Hysteresis = 4.0 V (noise up to ±2 V cannot trip it) ✓
```

### Summary

```
   ┌────────────────────────────────────────────────┐
   │  Inverting Schmitt, ±2 V hysteresis:           │
   │  • R_g: 10 kΩ (+ input to ground)             │
   │  • R_f: 40 kΩ (+ input to V_out)              │
   │  • β = 0.2, V_sat = ±10 V                     │
   │  • Thresholds: +2.0 V / -2.0 V                 │
   │  • Immune to < 4 V p-p noise around threshold  │
   └────────────────────────────────────────────────┘
```

## Real Op-Amp Parameter Table

The ideal model is a fiction; real parts have finite gain, finite bandwidth, residual offset, and slew-rate limits. The table below compares the textbook ideal against three of the most common general-purpose op-amps.

| Parameter | Ideal | LM741 | TL072 | LM358 |
|-----------|-------|-------|-------|-------|
| Open-loop gain (A_OL) | ∞ | 200 V/mV (106 dB) | 200 V/mV (106 dB) | 100 V/mV (100 dB) |
| Gain-bandwidth product (GBW) | ∞ | 1.5 MHz | 3 MHz | 1 MHz |
| Slew rate (SR) | ∞ | 0.5 V/µs | 13 V/µs | 0.5 V/µs |
| Input offset voltage (V_os) | 0 | 2 mV (typ), 6 mV max | 3 mV (typ), 10 mV max | 2 mV (typ), 7 mV max |
| Input bias current (I_B) | 0 | 80 nA | 65 pA (FET) | 45 nA |
| Input impedance (Z_in) | ∞ | 2 MΩ | 10^12 Ω (FET) | ~10^9 Ω |
| Supply voltage range (Vcc/−Vee) | — | ±3 V to ±18 V | ±2.25 V to ±9 V (single 4.5–18 V) | 3 V to 32 V (single) |
| Output swing (per supply) | rail-to-rail | ±13 V on ±15 V | ±13.5 V on ±15 V | 0 to Vcc−1.5 V |
| Noise (broadband) | 0 | moderate (bipolar) | 4 nV/√Hz (quiet, FET) | moderate |
| Single-supply capable? | — | no (needs dual) | yes (with biasing) | yes (designed for it) |
| Input stage | — | bipolar (BJT) | JFET | bipolar (BJT) |
| Typical use | — | teaching, slow analog | audio, low-noise, hi-Z | battery, single-supply |

**How to read this table when designing:**

- **GBW sets bandwidth**: closed-loop BW = GBW / |noise gain|. A TL072 at noise gain 10 runs to 300 kHz; an LM741 at the same gain runs to 150 kHz.
- **Slew rate sets full-power frequency**: f_max = SR / (2π·V_peak). The 741 (0.5 V/µs) slews full-power only to 9 kHz at 10 V peak — it distorts full-volume audio. The TL072 (13 V/µs) is fine to 200 kHz.
- **V_os sets DC accuracy**: every millivolt of offset appears at the output multiplied by the noise gain. Precision DC work wants < 1 mV; use the offset-null pins or a precision part (OP07, OPA2188).
- **Supply range**: the LM358 (3–32 V single supply) is the universal battery-powered choice; the TL072 prefers symmetric ±5 V to ±9 V; the 741 is a dual-supply ±15 V part.

## Prerequisites

- **[Semiconductor Devices](semiconductor-devices.md)** — supplies the op-amp IC itself; the origin of A_OL, GBW, slew rate, V_os. This article uses the datasheet, not the physics.
- **[Passive Components](passive-components.md)** — the resistors that set gain (R_f, R_in), the capacitors that integrate/differentiate and set filter cutoffs, the matched resistor quads for difference amplifiers.
- **[Filter Circuits](power-supply-circuits.filter-circuits.md)** — the passive-filter theory (f_c, roll-off, Q) that the active filters in this article extend with op-amp gain.

## See Also

- [Analog Circuits](analog-circuits.md) — the parent capability hub; the pedagogical ladder this article sits on.
- [Filter Circuits](power-supply-circuits.filter-circuits.md) — passive RC/LC filter theory referenced by the active-filter section above.
- [Multivibrator Circuits](analog-circuits.multivibrator-circuits.md) — the sibling article that uses the op-amp comparator and Schmitt trigger to build astable, monostable, and bistable timing circuits.
- [Interface Circuits](interface-circuits.md) — ADC/DAC front ends consume the op-amp buffer, summing, and active-filter techniques taught here.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
