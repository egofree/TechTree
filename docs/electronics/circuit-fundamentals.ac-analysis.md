# AC Circuit Analysis

> **Node ID**: electronics.circuit-fundamentals.ac-analysis
> **Domain**: [Electronics](index.md)
> **Dependencies**: [`electronics.electrical-systems`](electrical-systems.md), [`electronics.passive-components`](passive-components.md), [`electronics.circuit-fundamentals.dc-analysis`](circuit-fundamentals.dc-analysis.md)
> **Timeline**: Years 15-30
> **Outputs**: ac-circuit-analysis
> **Critical**: No — analytical knowledge, not a physical bottleneck; once the components and instruments exist, a practitioner derives all results from the rules below

This article teaches alternating-current (AC) circuit analysis from first principles. We assume you know DC theory — Ohm's law (`V = IR`), series/parallel resistor combinations, Kirchhoff's voltage and current laws, and `P = VI` for resistive circuits (the [DC analysis](circuit-fundamentals.dc-analysis.md) sibling article covers these in depth). Here we extend that toolkit to circuits driven by *sinusoidal* sources, where voltages and currents vary with time and energy storage elements (capacitors and inductors) create phase shifts between voltage and current.

AC is the TESLA foundation — the reason motors self-start, transformers step voltage up and down, and long-distance power transmission is practical. Every [transformer](electrical-systems.md), every induction [motor](electrical-systems.md), every RF antenna, and the entire electrical grid operate on AC principles. The [passive components](passive-components.md) — resistors, capacitors, and inductors — are the physical parts whose behavior we analyze here.

---

## 1. Sinusoidal Sources

### Why AC?

A DC source delivers constant voltage: `V(t) = 12 V` forever. An AC source delivers a voltage that oscillates sinusoidally around zero. In the late 1880s, Nikola Tesla and George Westinghouse championed AC over Thomas Edison's DC for power distribution, and they were right for three reasons:

1. **Transformers only work on AC.** A transformer changes voltage levels with no moving parts and 97-99% efficiency (see [Electrical Systems](electrical-systems.md)). This lets utilities transmit power at 100+ kV (low current, low I²R line loss) and distribute it at 120/240 V (safe for consumers). DC could not be transformed cheaply until power electronics (solid-state DC-DC converters) arrived a century later.

2. **AC motors are self-starting and simpler.** Tesla's polyphase induction motor has no brushes, no commutator, and no electrical connection to the rotor. A three-phase stator winding creates a *rotating* magnetic field that drags the rotor along. DC motors require brushes that wear out every 2,000-5,000 hours.

3. **Generators naturally produce AC.** A coil rotating in a magnetic field generates a sinusoidal EMF by Faraday's law. Converting this to smooth DC requires a commutator (mechanical rectifier) — extra complexity. Every alternator in every power plant worldwide produces AC natively.

### The Sinusoid

An AC voltage source produces a voltage that varies with time as:

```
v(t) = V_peak · sin(ωt + φ)
```

Where:

| Symbol | Name | Unit | Meaning |
|--------|------|------|---------|
| `v(t)` | Instantaneous voltage | volts (V) | Voltage at time t |
| `V_peak` | Peak amplitude | V | Maximum deviation from zero |
| `ω` | Angular frequency | rad/s | Rate of oscillation: ω = 2πf |
| `f` | Frequency | hertz (Hz) | Cycles per second |
| `T` | Period | seconds (s) | Time for one cycle: T = 1/f |
| `φ` | Phase angle | radians | Offset from t=0 reference |
| `t` | Time | s | Elapsed time |

At 60 Hz (North American grid), the period is `T = 1/60 = 16.67 ms` and the angular frequency is `ω = 2π × 60 = 377 rad/s`. At 50 Hz (Europe, most of Asia, Africa), `T = 20 ms` and `ω = 314 rad/s`.

```
  v(t)
   V_peak ─     ╭───╮               ╭───╮
            ╭───╯   ╰───╮           ╱       ╲
   0 ───────╱───────────╲─────────╱───────────╲──── t
            ╲           ╱ ╰───╮   ╱   ╰───╮
  -V_peak ─  ╰───╮   ╭───╯     ╰───╯       ╰───
                ╰───╯
            |← T →|
           one cycle (T = 1/f)
```

The current through a resistor driven by this source follows the same shape: `i(t) = (V_peak / R) · sin(ωt + φ)`. Voltage and current are *in phase* for a resistor. For capacitors and inductors, they are not — and that is where AC analysis gets interesting.

---

## 2. RMS and Peak Values

### The Problem with "Peak"

A 120 V wall outlet does not deliver 120 V peak. The voltage oscillates between +170 V and -170 V. The "120 V" is the *root-mean-square* (RMS) value — the DC-equivalent voltage that would deliver the same average power to a resistor.

### Deriving RMS

Average power in a resistor driven by `v(t) = V_peak · sin(ωt)`:

```
P_avg = (1/T) ∫₀ᵀ v(t)²/R dt
      = (V_peak²/R) · (1/T) ∫₀ᵀ sin²(ωt) dt
      = (V_peak²/R) · ½
      = V_peak² / (2R)
```

Setting this equal to the DC power formula `P = V_DC² / R`:

```
V_DC² / R = V_peak² / (2R)
V_DC = V_peak / √2
V_rms = V_peak / √2 ≈ 0.707 · V_peak
```

Conversely: `V_peak = V_rms × √2 ≈ 1.414 × V_rms`.

### Worked Example: Wall Outlet

A North American wall outlet is rated 120 V RMS at 60 Hz. What is the peak voltage and the instantaneous voltage at t = 5 ms?

```
V_peak = 120 × √2 = 169.7 V
ω = 2π × 60 = 377 rad/s
v(t) = 169.7 · sin(377t) volts

At t = 5 ms:
v(0.005) = 169.7 · sin(377 × 0.005)
         = 169.7 · sin(1.885)
         = 169.7 · sin(108°)
         = 169.7 × 0.951
         = 161.4 V
```

For a 240 V RMS outlet (Europe): `V_peak = 240 × √2 = 339.4 V`.

**All AC voltages in power systems and datasheets are RMS unless explicitly stated otherwise.** A 480 V three-phase motor nameplate means 480 V RMS. An oscilloscope showing a peak-to-peak value of 340 V on a 120 V circuit is showing `2 × 170 V` peak-to-peak.

---

## 3. Phasor Representation

### The Core Insight

Sinusoidal calculations with trig identities are painful. Charles Proteus Steinmetz (1893) had the key idea: **a sinusoid is the imaginary part of a rotating complex number**, and Ohm's law in the complex domain is algebra, not calculus.

### Euler's Identity

```
e^(jθ) = cos(θ) + j·sin(θ)
```

Therefore: `V_peak · sin(ωt + φ) = Im{V_peak · e^(j(ωt + φ))}`.

The term `e^(jωt)` is common to every signal at the same frequency, so we factor it out and work only with the amplitude and phase. This complex number is the **phasor**:

```
Ṽ = V_rms ∠φ = V_rms · e^(jφ)
```

### Phasor Diagram

A phasor is a vector in the complex plane. The horizontal axis is the real part, the vertical axis is the imaginary part. The angle is the phase φ relative to a reference (usually the source voltage).

```
                    Im
                    ↑
                    │      Ṽ = V∠φ
                    │     ╱
                    │    ╱
              V·sin φ ╱
                    │  ╱
                    │ ╱ φ (phase angle)
                    │╱_______________→ Re
                    0     V·cos φ

  The phasor rotates counterclockwise at ω rad/s.
  Its projection on the Im axis is the instantaneous voltage.
```

### Adding Sinusoids with Phasors

Two voltages in series: `v₁(t) = 100 sin(ωt) V` and `v₂(t) = 100 sin(ωt + 60°) V`. Adding them directly requires a trig identity. With phasors:

```
Ṽ₁ = 100∠0° = 100 + j0
Ṽ₂ = 100∠60° = 50 + j86.6

Ṽ_total = Ṽ₁ + Ṽ₂ = 150 + j86.6
|Ṽ_total| = √(150² + 86.6²) = √(22500 + 7500) = √30000 = 173.2 V
∠Ṽ_total = arctan(86.6/150) = arctan(0.577) = 30°

v_total(t) = 173.2 · sin(ωt + 30°) V
```

Two 100 V sources 60° apart sum to 173 V at 30° — not 200 V. This is why phasor addition matters: **voltages that are out of phase do not add arithmetically.**

### Phasor Convention Summary

| Time Domain | Phasor Domain |
|-------------|---------------|
| `v(t) = V_peak sin(ωt + φ)` | `Ṽ = (V_peak/√2) ∠φ = V_rms ∠φ` |
| `i(t) = I_peak sin(ωt + θ)` | `Ĩ = (I_peak/√2) ∠θ = I_rms ∠θ` |
| Addition, subtraction | Complex arithmetic |
| Differentiation: `dv/dt` | `jω · Ṽ` |
| Integration: `∫v dt` | `Ṽ / (jω)` |

The last two rows are the payoff. In the time domain, a capacitor's `i = C·dv/dt` is a differential equation. In the phasor domain, it becomes `Ĩ = jωC · Ṽ` — pure algebra, analogous to Ohm's law.

---

## 4. Reactance

Reactance is the AC analog of resistance for energy-storage elements. It measures how much a capacitor or inductor opposes the flow of sinusoidal current. Unlike resistance, reactance depends on frequency.

### Inductive Reactance (X_L)

An inductor stores energy in a magnetic field. Its voltage-current relationship is `v = L·di/dt`. In the phasor domain:

```
Ṽ = jωL · Ĩ  →  Ṽ/Ĩ = jωL

X_L = ωL = 2πfL    (inductive reactance, ohms)
```

The `j` factor means current *lags* voltage by 90° in an inductor. Physically: the inductor opposes changes in current. When voltage is at its peak, current is still climbing. When voltage returns to zero, current reaches its peak.

### Capacitive Reactance (X_C)

A capacitor stores energy in an electric field. Its voltage-current relationship is `i = C·dv/dt`. In the phasor domain:

```
Ĩ = jωC · Ṽ  →  Ṽ/Ĩ = 1/(jωC) = -j/(ωC)

X_C = 1/(ωC) = 1/(2πfC)    (capacitive reactance, ohms)
```

The `-j` factor means current *leads* voltage by 90° in a capacitor. Physically: current must flow first to deposit charge on the plates before voltage can build up.

### Reactance vs Frequency

| Property | Inductor (L) | Capacitor (C) |
|----------|-------------|---------------|
| Reactance | `X_L = 2πfL` | `X_C = 1/(2πfC)` |
| At DC (f→0) | `X_L → 0` (short) | `X_C → ∞` (open) |
| At high freq (f→∞) | `X_L → ∞` (open) | `X_C → 0` (short) |
| Phase of I vs V | Current lags by 90° | Current leads by 90° |
| Energy stored | ½LI² (magnetic) | ½CV² (electric) |
| Frequency trend | X_L increases with f | X_C decreases with f |

### Quantitative Parameter Table: Common Values at 50/60 Hz

| Component | Value | X_L at 50 Hz (Ω) | X_L at 60 Hz (Ω) | X_C at 50 Hz (Ω) | X_C at 60 Hz (Ω) |
|-----------|-------|-------------------|-------------------|-------------------|-------------------|
| Inductor | 1 mH | 0.314 | 0.377 | — | — |
| Inductor | 10 mH | 3.14 | 3.77 | — | — |
| Inductor | 100 mH | 31.4 | 37.7 | — | — |
| Inductor | 1 H | 314 | 377 | — | — |
| Inductor | 10 H | 3142 | 3770 | — | — |
| Capacitor | 1 nF | — | — | 3.18 M | 2.65 M |
| Capacitor | 100 nF | — | — | 31.8 k | 26.5 k |
| Capacitor | 1 µF | — | — | 3183 | 2653 |
| Capacitor | 10 µF | — | — | 318.3 | 265.3 |
| Capacitor | 100 µF | — | — | 31.8 | 26.5 |
| Capacitor | 1000 µF | — | — | 3.18 | 2.65 |

**Reading the table:** A 10 mH inductor at 60 Hz presents only 3.77 Ω of reactance — nearly a short circuit at power-line frequency. The same inductor at 10 kHz would present `X_L = 2π × 10000 × 0.01 = 628 Ω` — a substantial impedance. This is why inductors are effective high-frequency chokes but nearly transparent at DC/low frequency.

**Worked reactance calculation:** A 100 µF power-supply filter capacitor at 60 Hz:

```
X_C = 1 / (2π × 60 × 100×10⁻⁶)
    = 1 / (2π × 0.006)
    = 1 / 0.0377
    = 26.5 Ω
```

A capacitor this size at line frequency looks like a 26.5 Ω reactance — low enough to shunt AC ripple to ground in a filter, but high enough that it draws measurable current if connected directly across the line.

---

## 5. Impedance

### Definition

Impedance is the generalized AC opposition to current flow — the phasor-domain analog of resistance. It combines resistance (which dissipates energy) and reactance (which stores and releases energy):

```
Z = R + jX      (impedance, ohms)

|Z| = √(R² + X²)     (magnitude)
θ = arctan(X / R)     (phase angle)
```

Where `X = X_L - X_C` is the **net reactance**. Inductive reactance is positive; capacitive reactance is negative.

### Ohm's Law in the Phasor Domain

```
Ṽ = Ĩ · Z
```

This single equation replaces all the time-domain differential equations. The impedance `Z` encodes everything about how the circuit responds at a given frequency.

### Impedance of Individual Elements

| Element | Impedance Z | Phase of I vs V |
|---------|------------|-----------------|
| Resistor (R) | `R` (purely real) | In phase (0°) |
| Inductor (L) | `jωL = jX_L` | Current lags 90° |
| Capacitor (C) | `1/(jωC) = -jX_C` | Current leads 90° |

### Series and Parallel Combinations

**Series** (same current through all elements): impedances add directly.

```
Z_total = Z₁ + Z₂ + Z₃ + ...
```

**Parallel** (same voltage across all elements): reciprocals add.

```
1/Z_total = 1/Z₁ + 1/Z₂ + 1/Z₃ + ...

For two impedances: Z_total = (Z₁ · Z₂) / (Z₁ + Z₂)
```

### Worked Impedance Example: Series RLC Circuit

A series circuit consists of R = 100 Ω, L = 100 mH, and C = 10 µF, driven at 60 Hz, V_rms = 120 V.

**Step 1: Calculate individual reactances.**

```
X_L = 2πfL = 2π × 60 × 0.1 = 37.7 Ω
X_C = 1/(2πfC) = 1/(2π × 60 × 10×10⁻⁶) = 1/0.00377 = 265.3 Ω
```

**Step 2: Calculate net impedance.**

```
X = X_L - X_C = 37.7 - 265.3 = -227.6 Ω   (net capacitive)

Z = R + jX = 100 - j227.6 Ω

|Z| = √(100² + 227.6²) = √(10000 + 51802) = √61802 = 248.6 Ω
θ = arctan(-227.6 / 100) = arctan(-2.276) = -66.3°
Z = 248.6 ∠-66.3° Ω
```

The negative phase angle means the circuit is net capacitive — current leads voltage by 66.3°.

**Step 3: Calculate current.**

```
Ĩ = Ṽ / Z = 120∠0° / 248.6∠-66.3° = 0.483 ∠+66.3° A
```

**Step 4: Calculate individual element voltages.**

```
Ṽ_R = Ĩ × R = 0.483∠66.3° × 100 = 48.3 ∠66.3° V
Ṽ_L = Ĩ × jX_L = 0.483∠66.3° × 37.7∠90° = 18.2 ∠156.3° V
Ṽ_C = Ĩ × (-jX_C) = 0.483∠66.3° × 265.3∠-90° = 128.1 ∠-23.7° V
```

**Check KVL:** `Ṽ_R + Ṽ_L + Ṽ_C` should equal `Ṽ = 120∠0°`.

```
Ṽ_R = 48.3∠66.3° = 19.4 + j44.2
Ṽ_L = 18.2∠156.3° = -16.7 + j7.3
Ṽ_C = 128.1∠-23.7° = 117.3 - j51.5

Sum = (19.4 - 16.7 + 117.3) + j(44.2 + 7.3 - 51.5)
    = 120.0 + j0.0  ✓
```

**Key insight:** The capacitor voltage (128.1 V) exceeds the source voltage (120 V)! This is not a mistake — in a series RLC circuit, reactive element voltages can exceed the source voltage because `Ṽ_L` and `Ṽ_C` partially cancel (they are 180° apart). Only the phasor sum must equal the source. This "voltage gain" phenomenon is central to resonance (Section 7).

---

## 6. AC Power

In DC circuits, power is simple: `P = VI`. In AC circuits, the phase shift between voltage and current complicates things. Three different quantities carry the name "power."

### The Three Powers

| Quantity | Symbol | Unit | Formula | Physical Meaning |
|----------|--------|------|---------|------------------|
| Real power | P | watt (W) | `P = VI cos(θ)` | Energy actually consumed (heat, light, mechanical work) |
| Reactive power | Q | var (VAR) | `Q = VI sin(θ)` | Energy oscillating between source and L/C (no net consumption) |
| Apparent power | S | volt-ampere (VA) | `S = VI` | Total power the source must supply (what wires and transformers carry) |

Where θ is the phase angle between voltage and current (the impedance angle).

### The Power Triangle

```
              S = VI (apparent power, VA)
             ╱│
            ╱ │
           ╱  │
          ╱   │  Q = VI sin(θ) (reactive power, VAR)
         ╱    │
        ╱ θ   │
       ╱──────┘
      P = VI cos(θ) (real power, W)

  S² = P² + Q²    →    S = √(P² + Q²)
```

### Power Factor

```
Power Factor = cos(θ) = P / S
```

The power factor (PF) tells you what fraction of the apparent power does useful work:

- **PF = 1.0** (θ = 0°): Purely resistive load. All apparent power is real power. Ideal.
- **PF = 0.0** (θ = ±90°): Purely reactive load. Zero real power; current flows but no energy is consumed.
- **PF = 0.85 lagging** (θ > 0, inductive): Most common industrial load. Current lags voltage.
- **PF = 0.85 leading** (θ < 0, capacitive): Rare; some synchronous motors, capacitor banks.

### Why Power Factor Matters

A motor drawing 100 A at 0.8 PF from a 480 V source consumes the same real power as at 1.0 PF, but draws 25% more current:

```
At PF = 1.0:  P = 480 × 100 × 1.0 = 48 kW,  I = 100 A
At PF = 0.8:  P = 480 × 125 × 0.8 = 48 kW,  I = 125 A (25% more current!)
```

That extra 25 A heats the wires, transformer windings, and generator for no useful work. Utilities penalize industrial customers for PF below 0.90-0.95 because they must size generation and transmission for apparent power (VA), not real power (W).

### Worked Example: Power-Factor Correction

**Problem:** A factory operates a 480 V, 60 Hz induction motor drawing 50 A at PF = 0.70 lagging. Calculate the capacitance needed to correct the PF to 0.95 lagging.

**Step 1: Find current powers.**

```
θ₁ = arccos(0.70) = 45.6°
S₁ = V × I = 480 × 50 = 24,000 VA = 24 kVA
P = S₁ × cos(θ₁) = 24,000 × 0.70 = 16,800 W = 16.8 kW
Q₁ = S₁ × sin(θ₁) = 24,000 × sin(45.6°) = 24,000 × 0.714 = 17,140 VAR
```

**Step 2: Find required reactive power at new PF.**

Real power P is unchanged (the motor does the same work). The new power angle:

```
θ₂ = arccos(0.95) = 18.2°
Q₂ = P × tan(θ₂) = 16,800 × tan(18.2°) = 16,800 × 0.329 = 5,527 VAR
```

**Step 3: Calculate reactive power the capacitor must supply.**

```
Q_C = Q₁ - Q₂ = 17,140 - 5,527 = 11,613 VAR
```

The capacitor must supply 11,613 VAR of *leading* reactive power to cancel the motor's lagging reactive power.

**Step 4: Calculate capacitance.**

```
Q_C = V² / X_C  →  X_C = V² / Q_C

X_C = 480² / 11,613 = 230,400 / 11,613 = 19.84 Ω

C = 1 / (2πf × X_C) = 1 / (2π × 60 × 19.84) = 1 / 7,479 = 133.7 µF
```

**Step 5: Verify the new current.**

```
S₂ = √(P² + Q₂²) = √(16800² + 5527²) = √(282,240,000 + 30,547,729) = √312,787,729 = 17,686 VA
I_new = S₂ / V = 17,686 / 480 = 36.8 A
```

**Result:** Adding a 134 µF capacitor bank across the motor terminals reduces line current from **50 A to 36.8 A** — a 26% reduction — while delivering the same mechanical power. Wires, breakers, and transformer now carry less current, reducing I²R losses and freeing up capacity. This is why power-factor correction capacitors are standard equipment in industrial plants.

---

## 7. Resonance

### The Phenomenon

When inductive and capacitive reactances cancel each other (`X_L = X_C`), a series or parallel RLC circuit reaches **resonance**. At this specific frequency, the circuit's impedance is purely resistive — voltage and current are in phase. Resonance is the principle behind radio tuning, induction heating, oscillator circuits, and power-system harmonic filters.

### Resonant Frequency

Setting `X_L = X_C`:

```
ω₀L = 1/(ω₀C)
ω₀² = 1/(LC)

f₀ = 1 / (2π√(LC))
```

Where `f₀` is the resonant frequency in Hz, L is in henries, C is in farads.

### Series Resonant Circuit

```
        R        L        C
  ┌────[====]──[UUUU]──[═══]────┐
  │                              │
  ~ AC source                   (series RLC)
  │                              │
  └──────────────────────────────┘

  At resonance: X_L = X_C, so Z = R (minimum impedance)
  → current is maximum, V_L and V_C can exceed source voltage
```

At resonance in a series RLC circuit:

| Parameter | Value at Resonance |
|-----------|-------------------|
| Net reactance | `X = X_L - X_C = 0` |
| Impedance | `Z = R` (minimum, purely resistive) |
| Current | `I_max = V / R` (maximum) |
| Phase angle | `θ = 0°` (voltage and current in phase) |
| Power factor | `1.0` (unity) |
| Inductor voltage | `V_L = I × X_L = Q × V_source` (can be >> V_source) |
| Capacitor voltage | `V_C = I × X_C = Q × V_source` (can be >> V_source) |

### Parallel Resonant Circuit

```
       ┌──[UUUU]──┐
       │    L     │
  ─────┤          ├──[═══]─────
       │          │     C
       └──[====]──┘
          R (coil resistance, often in series with L)

  At resonance: impedance is MAXIMUM (opposite of series)
  → current is minimum, voltage across tank is maximum
```

In a parallel resonant ("tank") circuit, impedance reaches its *maximum* at resonance, and line current drops to a minimum while circulating current between L and C can be large.

### Q Factor (Quality Factor)

The Q factor measures how "sharp" the resonance peak is — how selectively the circuit responds to the resonant frequency versus nearby frequencies.

**Series RLC:**

```
Q = X_L / R = ω₀L / R = 1 / (ω₀CR)
```

**Parallel RLC:**

```
Q = R / X_L = R / (ω₀L) = ω₀CR
```

### Bandwidth

The bandwidth (BW) is the frequency range between the two half-power (-3 dB) points on either side of resonance:

```
BW = f₂ - f₁ = f₀ / Q      (Hz)
```

A high-Q circuit has a narrow bandwidth (sharp, selective). A low-Q circuit has a wide bandwidth (broad, less selective).

| Q Factor | Bandwidth (relative) | Application |
|----------|---------------------|-------------|
| 0.5 | 2 × f₀ (overdamped) | No resonance peak (wideband filters) |
| 1 | f₀ | Low selectivity |
| 10 | f₀/10 | Radio IF filter |
| 50 | f₀/50 | Crystal oscillator |
| 1000+ | f₀/1000 | Quartz crystal, cavity resonator |

### Worked Resonance Example

A series RLC circuit has R = 10 Ω, L = 1 mH, C = 100 nF. Find the resonant frequency, Q factor, and bandwidth.

```
f₀ = 1 / (2π√(LC))
   = 1 / (2π√(0.001 × 100×10⁻⁹))
   = 1 / (2π√(10⁻¹⁰))
   = 1 / (2π × 10⁻⁵)
   = 1 / (6.283 × 10⁻⁵)
   = 15,915 Hz ≈ 15.9 kHz

X_L at f₀ = 2π × 15915 × 0.001 = 100 Ω

Q = X_L / R = 100 / 10 = 10

BW = f₀ / Q = 15915 / 10 = 1591 Hz

Half-power points: f₁ = 15915 - 796 = 15,119 Hz, f₂ = 15915 + 796 = 16,711 Hz
```

At resonance, the inductor and capacitor voltages are `Q × V_source = 10 × V_source`. A 1 V source drives the series circuit, but 10 V appears across each reactive element. This **voltage magnification** is why series resonance is used in radio receivers (a tiny antenna signal becomes usable) and why it is dangerous in power systems (unintended resonance can destroy equipment).

---

## 8. Three-Phase Systems

### Why Polyphase?

Single-phase AC power pulsates: the instantaneous power `p(t) = v(t)·i(t)` crosses zero twice per cycle. A single-phase motor receives no torque at the zero-crossing instants, which is why single-phase induction motors need auxiliary starting windings and capacitors.

Tesla's three-phase system solves this by using three conductors, each carrying the same voltage but 120° apart in phase. At any instant, the sum of the three instantaneous powers is *constant* — it never drops to zero. This gives three advantages:

1. **Constant power delivery** — motors run smoothly with no torque pulsation.
2. **Self-starting motors** — the rotating magnetic field starts instantly without auxiliary windings.
3. **More power per conductor** — three-phase delivers √3 ≈ 1.73× more power per conductor than single-phase for the same conductor material.

### The Three Phases

```
  v_A(t) = V_peak · sin(ωt)           (phase A, reference)
  v_B(t) = V_peak · sin(ωt - 120°)    (phase B, lags A by 120°)
  v_C(t) = V_peak · sin(ωt - 240°)    (phase C, lags A by 240°)
```

```
 v(t)
  V_peak ─  ╭╮ A          ╭╮ A
            │ │   ╭╮ B    │ │   ╭╮ B
   0 ──────┼─┼───┼─┼──────┼─┼───┼─┼───────
           │ │  ╱  ╲      │ │  ╱  ╲
          ╱   ╲╱    ╲    ╱   ╲╱    ╲
 -V_peak  ╱           ╲  ╱           ╲
        ╱    ╲    ╱╲   ╲╱    ╲    ╱╲
                   ╲╱ C              ╲╦ C

  Phase A at 0°, B at -120°, C at -240° (= +120°)
  Sum of all three = 0 at every instant (balanced system)
```

### Line-to-Line vs Phase Voltage

In a three-phase system, each conductor carries a voltage relative to neutral (the **phase voltage**, V_φ) and each pair of conductors carries a voltage between them (the **line-to-line voltage**, V_LL). The relationship is:

```
V_LL = √3 × V_φ     ≈ 1.732 × V_φ
```

| System (line-to-line RMS) | Phase Voltage (L-N) | Common Use |
|---------------------------|---------------------|------------|
| 208 V | 120 V | Commercial (US) — 120 V outlets derived phase-to-neutral |
| 240 V | 139 V | Light industrial |
| 480 V | 277 V | Industrial (US) — 277 V fluorescent lighting |
| 4160 V | 2402 V | Medium-voltage distribution |
| 13.8 kV | 7.97 kV | Primary distribution |
| 138 kV | 79.7 kV | Sub-transmission |
| 345 kV | 199 kV | High-voltage transmission |

### Three-Phase Power

For a balanced three-phase load:

```
P_3φ = √3 × V_LL × I_L × cos(θ)

Where:
  V_LL = line-to-line voltage (V)
  I_L  = line current (A)
  θ   = phase angle between phase voltage and phase current
```

This is the single most-used formula in industrial power engineering. Note: the √3 factor appears because of the relationship between line and phase quantities, and `cos(θ)` is the power factor per phase.

### Worked Three-Phase Example

**Problem:** A 480 V three-phase induction motor draws 60 A per line at PF = 0.85 lagging. What is the real power, reactive power, and apparent power?

```
V_LL = 480 V,  I_L = 60 A,  cos(θ) = 0.85  →  θ = arccos(0.85) = 31.8°

Apparent power:
S = √3 × V_LL × I_L = 1.732 × 480 × 60 = 49,882 VA ≈ 49.9 kVA

Real power:
P = S × cos(θ) = 49,882 × 0.85 = 42,400 W ≈ 42.4 kW

Reactive power:
Q = S × sin(θ) = 49,882 × sin(31.8°) = 49,882 × 0.527 = 26,288 VAR ≈ 26.3 kVAR

Check: S² = P² + Q² → √(42.4² + 26.3²) = √(1797.8 + 691.7) = √2489.5 = 49.9 kVA ✓
```

**Motor sizing rule of thumb:** A three-phase motor at 480 V draws approximately 1.2 A per horsepower at full load (see [Electrical Systems](electrical-systems.md)). A 50 HP motor draws ~60 A — consistent with the example above, which represents roughly a 50 HP load.

---

## Summary: The AC Analysis Toolkit

| Problem | Method | Key Formula |
|---------|--------|-------------|
| DC-equivalent voltage for power | RMS conversion | `V_rms = V_peak / √2` |
| Convert sinusoid to algebra | Phasor transform | `v(t) = V_peak sin(ωt+φ)` → `Ṽ = V_rms ∠φ` |
| Inductor opposition to AC | Inductive reactance | `X_L = 2πfL` |
| Capacitor opposition to AC | Capacitive reactance | `X_C = 1/(2πfC)` |
| Total AC opposition | Impedance | `Z = R + jX`, `Ṽ = Ĩ·Z` |
| Real power consumed | Real power | `P = VI cos(θ)` |
| Efficiency of power transfer | Power factor | `PF = cos(θ) = P/S` |
| Correct bad power factor | Capacitor sizing | `C = Q_C / (2πf × V²)` |
| Frequency of max response | Resonance | `f₀ = 1/(2π√(LC))` |
| Selectivity of resonant circuit | Q factor | `Q = X_L/R` (series) |
| Frequency span of resonance | Bandwidth | `BW = f₀/Q` |
| Industrial power | Three-phase | `P = √3 × V_LL × I × cos(θ)` |

These tools let you predict how any linear AC circuit will behave — filter response, power consumption, phase relationships, resonance conditions — before you build it. Every amplifier bias network, every matching network, every power-distribution load flow, every transformer winding ratio is designed using this analytical framework.

---

## See Also

- [Circuit Fundamentals](circuit-fundamentals.md) — the parent capability: DC theory hub, scope, and progression
- [Passive Components](passive-components.md) — how resistors, capacitors, and inductors are physically constructed
- [Electrical Systems](electrical-systems.md) — transformers, motors, three-phase distribution, and power-factor correction equipment
- [Power Electronics](power-electronics.md) — switching converters that transform DC/AC power using semiconductor devices

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
