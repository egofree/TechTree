# Filter Circuits

> **Node ID**: `electronics.power-supply-circuits.filter-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.passive-components`](./passive-components.md), [`electronics.circuit-fundamentals.ac-analysis`](./circuit-fundamentals.ac-analysis.md)
> **Outputs**: filtered-dc
> **Timeline**: Years 20-40
> **Critical**: No

Filtering is the second stage of every power supply — the process of reducing the AC ripple from a [rectifier](./power-supply-circuits.rectifier-circuits.md) to a tolerable level, producing near-DC voltage. This article covers the **circuit-level design pedagogy** of passive LC and RC filter networks for power supply ripple reduction, plus the four canonical signal filter types (low-pass, high-pass, band-pass, band-stop) that every analog designer must know.

All filters here are **passive** — built from capacitors and inductors only. Active filters (using op-amps for gain and sharper roll-off) are covered in a forthcoming op-amp-circuits article. Switching regulators that achieve regulation through high-frequency filtering belong to [power-electronics](./power-electronics.md).

## The Fundamental Principle

A filter exploits the **frequency-dependent impedance** of reactive components:

- A capacitor's impedance decreases with frequency: X_C = 1 / (2πfC). At DC (f=0), it is an open circuit. At high frequency, it is a short.
- An inductor's impedance increases with frequency: X_L = 2πfL. At DC, it is a short circuit. At high frequency, it is an open.

For power supply filtering, we want to pass DC (f=0) and attenuate ripple (f = 120 Hz, 360 Hz, or higher). This is a **low-pass** function. For signal filtering, we may want any of the four canonical responses.

Every filter has a **cutoff frequency** f_c — the boundary between the passband and stopband — and a **roll-off** — the rate of attenuation increase beyond f_c. A first-order filter (one reactive element) rolls off at 20 dB/decade. A second-order filter (two reactive elements, e.g., LC) rolls off at 40 dB/decade.

```
  Attenuation
  (dB)
    0 ├─ ─ ─ ─ ─ ─ ─┬────────  Passband (flat)
      │              │ ╲
   −3 │              │  ╲  ← f_c (cutoff, −3 dB point)
      │              │   ╲
      │              │    ╲     First order: −20 dB/decade
  −20 │              │     ╲
      │              │      ╲    Second order: −40 dB/decade
  −40 │              │       ╲   (steeper)
      │              │        ╲
  −60 ├──────────────┴─────────╲────────  Stopband
      0.1          f_c       10×f_c      Frequency (log scale)
```

## Power Supply Filters

These filter networks follow a rectifier to smooth its pulsating DC output. They all act as low-pass function: pass the DC average, attenuate the ripple frequency.

### Capacitor-Input Filter (C Filter)

The simplest and most common: a large capacitor in parallel with the load. The capacitor charges to the peak rectifier voltage during the brief conduction window, then discharges into the load between pulses.

```
  From rectifier                    Load
  ────────┬───────────────┬─────────┐
          │               │         │
          ├───┬───┐       │      ┌──┴──┐
          │   │   │       │      │  R  │
          │   ▼   │       │      │ LOAD│
          │  ===  C      │      └──┬──┘
          │  ===  │       │         │
          │   │   │       │         │
  ────────┴───┴───┴───────┴─────────┘
              Filter capacitor
              (electrolytic, 1000–10000 μF)
```

**Ripple voltage** (from the [rectifier article](./power-supply-circuits.rectifier-circuits.md)):

```
  V_ripple(p-p) = I_load / (N · f · C)

  N = pulses per cycle, f = line frequency, C = capacitance
```

**Design note**: The capacitor's **Equivalent Series Resistance (ESR)** adds a ripple component independent of capacitance: V_ripple(ESR) = I_peak × ESR. For a 4700 μF / 25V aluminum electrolytic, ESR ≈ 30–100 mΩ at 120 Hz. At 1A load with I_peak ≈ 3–5× I_load (capacitor charging spikes), ESR ripple = 5A × 0.05Ω = 0.25V. This ESR ripple cannot be reduced by adding more capacitance — it requires a lower-ESR capacitor type (polymer, tantalum, ceramic) or a multi-stage filter.

### LC Filter (Choke-Input / Inductor-Input)

An inductor (choke) in series with the rectifier output, followed by a capacitor across the load. The inductor opposes current changes (V = L × dI/dt), smoothing the charging spikes into a gentler waveform. The capacitor then removes the residual ripple.

```
  From rectifier         Series       Load
                  L      choke
  ────────┬───────█████──────┬─────────┐
          │                  │         │
          │               ┌──┴──┐   ┌──┴──┐
          │               │  C  │   │  R  │
          │               │     │   │ LOAD│
          │               └──┬──┘   └──┬──┘
          │                  │         │
  ────────┴──────────────────┴─────────┘
```

**Cutoff frequency** (LC low-pass):

```
  f_c = 1 / (2π √(LC))
```

At frequencies well above f_c, attenuation ≈ (f_c / f)² (40 dB/decade). A 120 Hz ripple is attenuated by (f_c/120)² relative to DC.

**Advantages over C filter**:
- 40 dB/decade roll-off (vs 20 dB/decade for C alone) — much better ripple attenuation per unit capacitance.
- Reduced peak diode current — the inductor spreads charging over a longer window.
- Better voltage regulation — output sags less under load variation.

**Disadvantages**:
- The inductor (choke) is physically large, heavy, and expensive — iron-core inductors of 1–10 H at 1A are massive.
- Transient response is slower — the inductor resists current changes, delaying response to load steps.

**Design rule**: For choke-input filters, the inductance must exceed a **critical inductance** L_crit = R_load / (3ω), where ω = 2πf_ripple, or the inductor current never reaches zero and the filter reverts to capacitor-input behavior. At 120 Hz and 12Ω load: L_crit = 12 / (3 × 754) = 5.3 mH.

### π-Filter (Pi Section / CLC)

A capacitor followed by an LC section — shaped like the Greek letter π. The input capacitor charges to the peak voltage (like a C filter), then the LC section removes most of the residual ripple. The result is very low output ripple with moderate component count.

```
  From rectifier              Load
  ─────┬───────┬───────█████───┬─────────┐
       │       │       L       │         │
       │    ┌──┴──┐         ┌──┴──┐   ┌──┴──┐
       │    │ C1  │         │ C2  │   │  R  │
       │    │     │         │     │   │ LOAD│
       │    └──┬──┘         └──┬──┘   └──┬──┘
       │       │               │         │
  ─────┴───────┴───────────────┴─────────┘
        ╲   |   ╱   ← π shape: C1, L, C2
         ╲  |  ╱
```

**Cutoff frequency**: Same as LC: f_c = 1 / (2π√(LC2)), where C2 is the output capacitor.

**Attenuation**: The input capacitor C1 reduces ripple before the LC stage; the LC stage then applies 40 dB/decade. Total attenuation is roughly the product of the two stages. Typical π-filter achieves 40–60 dB ripple reduction (100–1000×) at 120 Hz.

**Advantages**:
- Lowest ripple of any passive filter — the dual-capacitor topology is very effective.
- Reasonable component sizes — C1 handles bulk energy storage, LC handles fine smoothing.

**Disadvantages**:
- High peak diode current — C1 acts like a capacitor-input filter, drawing sharp charging spikes.
- The series inductor still adds cost, size, and weight (though less than choke-input for the same attenuation).

### CLC Filter

The CLC filter is structurally identical to the π-filter (Capacitor–Inductor–Capacitor). The term "CLC" emphasizes the component sequence; "π-filter" emphasizes the topological shape. They are the same circuit. Some texts distinguish them by whether the inductor is a true choke (designed for high inductance at DC bias) vs. a small RF choke. In this article, π-filter and CLC are synonymous.

## Worked Example: π-Filter for 5V Supply

**Design goal**: 5V DC output at 1A load with ≤ 100 mV p-p ripple, following a full-wave bridge rectifier at 60 Hz (120 Hz ripple frequency).

### Step 1 — Input Stage (C1)

C1 is sized as a standard capacitor-input filter. Assume the rectifier peak voltage is 8V (allowing headroom for a 5V linear regulator downstream). Target V_ripple(C1) = 1V p-p (coarse, to be refined by LC stage):

```
  C1 = I_load / (2f · V_ripple1) = 1.0 / (120 × 1.0) = 8333 μF

  Select: 8200 μF, 16V electrolytic (standard value)
```

### Step 2 — LC Stage Attenuation Required

The LC stage must reduce 1V p-p ripple to ≤ 100 mV:

```
  Attenuation needed = 1.0 / 0.1 = 10× (20 dB)

  For a second-order LC at f = 120 Hz:
  Attenuation = (f / f_c)² ≥ 10
  f / f_c ≥ √10 = 3.16
  f_c ≤ 120 / 3.16 = 38 Hz
```

### Step 3 — Select L and C2

Choose f_c = 30 Hz (margin below 38 Hz):

```
  f_c = 1 / (2π√(L·C2)) = 30 Hz
  L·C2 = 1 / (2π·30)² = 1 / 35531 = 2.81 × 10⁻⁵

  Select C2 = 2200 μF (standard, low-ESR aluminum or polymer):
  L = 2.81 × 10⁻⁵ / 0.0022 = 0.0128 H = 12.8 mH

  Select: 15 mH choke rated ≥ 1A (iron-core or ferrite with gap)
```

Verify cutoff: f_c = 1 / (2π√(0.015 × 0.0022)) = 1 / (2π × 0.005745) = 27.7 Hz ✓

### Step 4 — Verify Ripple at Output

```
  Attenuation at 120 Hz = (f_c / f)² = (27.7 / 120)² = 0.0533

  V_ripple(output) = V_ripple(C1) × 0.0533 = 1.0 × 0.0533 = 53 mV ✓
```

53 mV < 100 mV target — design meets spec with margin.

### Step 5 — ESR Check

C2 ESR at 120 Hz ≈ 35 mΩ (typical 2200 μF / 16V aluminum). Ripple current through C2 is small (most AC blocked by L), so ESR contribution ≈ 0.05V × (R_ESR / X_C2). At 120 Hz, X_C2 = 1/(2π×120×0.0022) = 0.6Ω. ESR is 5% of X_C — adds ~5% to ripple. Total ≈ 56 mV. Still within spec.

### Summary

```
  ┌──────────────────────────────────────────────────────────┐
  │  π-Filter BOM (for 5V / 1A / ≤100mV ripple):             │
  │  • C1: 8200 μF / 16V electrolytic                        │
  │  • L:  15 mH / 1A iron-core choke                        │
  │  • C2: 2200 μF / 16V low-ESR electrolytic                │
  │  Result: 53 mV p-p ripple (47% margin below 100 mV)      │
  │  Roll-off: 40 dB/decade above f_c = 27.7 Hz             │
  └──────────────────────────────────────────────────────────┘
```

## Power Supply Filter Parameter Table

| Filter Type | Components | Cutoff Formula | Roll-off | Attenuation at 120 Hz (typical) | Typical Application |
|-------------|-----------|----------------|----------|--------------------------------|---------------------|
| C (capacitor-input) | 1 C | — (pole at f=0) | 20 dB/dec | 10–20 dB | General-purpose, low-cost supplies |
| RC (resistor + C) | 1 R, 1 C | f_c = 1/(2πRC) | 20 dB/dec | 10–20 dB | Signal coupling, low-current bias filtering |
| LC (choke-input) | 1 L, 1 C | f_c = 1/(2π√(LC)) | 40 dB/dec | 30–40 dB | High-current industrial supplies, audio |
| π / CLC | 2 C, 1 L | f_c = 1/(2π√(LC₂)) | 40 dB/dec | 40–60 dB | Low-ripple bench supplies, instrument references |
| CRC (two-stage RC) | 2 C, 1 R | f_c = 1/(2πR√(C₁C₂)) | 40 dB/dec | 30–40 dB | Low-current circuits where inductors are impractical |

Note: RC and CRC filters are unsuitable for power supply output stages at significant current — the series resistor wastes power (P = I²R). They are used for signal-level filtering and bias-line decoupling. For any load current above ~50 mA, use LC or π filters.

## Signal Filters

Beyond power supply smoothing, the same reactive components build the four canonical **signal filters** used throughout analog electronics. These shape the frequency content of signals — removing noise, isolating bands, or separating AC from DC.

### Low-Pass Filter (LPF)

Passes frequencies below f_c, attenuates frequencies above. The most common filter in electronics — used for anti-aliasing, noise removal, and converting PWM to analog.

**RC low-pass**:

```
            R                    Output
  Vin ─────█████──────┬──────────────┐
                      │              │
                   ┌──┴──┐        ┌──┴──┐
                   │  C  │        │     │
                   │     │        │ R_L │
                   └──┬──┘        └──┬──┘
                      │              │
  GND ────────────────┴──────────────┘

  f_c = 1 / (2πRC)
  At f_c: V_out = V_in / √2 = 0.707 × V_in (−3 dB)
  Above f_c: −20 dB/decade roll-off
```

Example: R = 1.6 kΩ, C = 0.1 μF → f_c = 1/(2π × 1600 × 10⁻⁷) = 995 Hz ≈ 1 kHz. Signals below 1 kHz pass; signals above are attenuated.

### High-Pass Filter (HPF)

Passes frequencies above f_c, blocks DC and low frequencies. Used for AC coupling, removing DC offset, and bass cut.

**RC high-pass** (swap R and C from the LPF):

```
            C                    Output
  Vin ──────||────────┬──────────────┐
                      │              │
                   ┌──┴──┐        ┌──┴──┐
                   │  R  │        │     │
                   │     │        │ R_L │
                   └──┬──┘        └──┬──┘
                      │              │
  GND ────────────────┴──────────────┘

  f_c = 1 / (2πRC)
  Below f_c: −20 dB/decade roll-off
  At DC: infinite attenuation (capacitor blocks DC)
```

### Band-Pass Filter (BPF)

Passes a band of frequencies between a lower and upper cutoff, attenuating both below f_c1 and above f_c2. Built by cascading a high-pass (f_c1) and a low-pass (f_c2):

```
  Vin ──[ HPF ]──▶ V_mid ──[ LPF ]──▶ V_out
         f_c1                   f_c2

  Passband: f_c1 < f < f_c2
  Center frequency: f_0 = √(f_c1 × f_c2)
  Bandwidth: BW = f_c2 − f_c1
  Q factor: Q = f_0 / BW
```

Used in radio (station selection), audio (equalizer bands), and instrumentation (isolating a signal frequency from noise).

### Band-Stop Filter (BSF / Notch)

Attenuates a band of frequencies, passing both below and above. Also called a notch filter when the stopband is narrow. Used to remove a specific interference frequency (e.g., 60 Hz mains hum).

A common notch topology is the **twin-T** network:

```
  Vin ──┬─── R ───┬─── R ───┬───▶ V_out
        │         │         │
        ├─── C ───┤         ├─── 2C ───┐
        │         │         │          │
        │         ├── R/2 ──┤          │
        │         │         │          │
  GND ──┴─────────┴─────────┴──────────┘

  Notch frequency: f_notch = 1 / (2πRC)
  Attenuation at f_notch: very high (ideal twin-T → ∞)
  Attenuation elsewhere: passes signal
```

## Filter Order and Roll-off

| Order | Reactive Elements | Roll-off | Circuit Example |
|-------|------------------|----------|-----------------|
| 1st | 1 (C or L) | 20 dB/decade (6 dB/octave) | RC low-pass |
| 2nd | 2 (LC or RC+RC) | 40 dB/decade (12 dB/octave) | LC filter |
| 3rd | 3 (CLC or 3-stage RC) | 60 dB/decade (18 dB/octave) | π-filter |
| 4th | 4 (2× LC cascade) | 80 dB/decade (24 dB/octave) | Cascaded LC |
| n-th | n | 20n dB/decade | Butterworth, Chebyshev, etc. |

Each additional reactive element adds 20 dB/decade to the roll-off. Higher-order filters achieve steeper transitions between passband and stopband, but require more components and introduce more phase shift (which matters in feedback loops). For power supply filtering, 2nd-order (LC) or 3rd-order (π) is almost always sufficient.

## Cutoff Frequency Reference

| Filter Configuration | Cutoff Frequency f_c | Notes |
|---------------------|----------------------|-------|
| RC low-pass | 1 / (2πRC) | R in ohms, C in farads |
| RC high-pass | 1 / (2πRC) | Same formula, swap R/C position |
| LC low-pass | 1 / (2π√(LC)) | L in henries, C in farads |
| LC high-pass | 1 / (2π√(LC)) | Swap L and C positions |
| π-filter (CLC) | 1 / (2π√(L·C₂)) | C₂ is the output capacitor |
| Twin-T notch | 1 / (2πRC) | R/C in one branch, 2C/R÷2 in the other |

## Capacitor Selection for Power Filters

| Capacitor Type | Range | ESR (120 Hz) | Ripple Current | Best For |
|---------------|-------|-------------|----------------|----------|
| Aluminum electrolytic | 1–100,000 μF | 30–200 mΩ | Moderate | Bulk energy storage (C1 in π-filter) |
| Low-ESR aluminum | 100–10,000 μF | 10–50 mΩ | High | Switching supply outputs |
| Polymer (OS-CON) | 10–1000 μF | 5–20 mΩ | Very high | High-ripple, low-ESR applications |
| Tantalum | 0.1–1000 μF | 20–100 mΩ | Low (fail short!) | Low-current, compact |
| Ceramic (X7R) | 0.001–100 μF | 2–10 mΩ | Very high | High-frequency decoupling, small values |
| Film (polypropylene) | 0.001–10 μF | 1–5 mΩ | Very high | Audio, snubbers, precision |

For power supply filter capacitors, the **ripple current rating** is as important as capacitance. The capacitor must absorb and deliver the ripple current without overheating. Exceeding the ripple current rating shortens capacitor life dramatically (electrolyte boils, vents, dries out — the "capacitor plague" failure mode).

## Boundary with Active and Switching Filters

This article covers **passive** filters only:

- **Active filters** (op-amp + RC networks for precision frequency shaping, Sallen-Key, multiple-feedback topologies) provide gain, steep roll-off without inductors, and tunable cutoff. They are covered in a forthcoming op-amp-circuits article. Active filters dominate signal processing but are not used for raw power supply ripple (op-amps cannot handle amps of current).

- **Switching regulators** (buck, boost, flyback) achieve both regulation and filtering through high-frequency PWM. Their output LC filter operates at 20–500 kHz (not 120 Hz), making the inductor and capacitor 100–1000× smaller. These belong to [power-electronics](./power-electronics.md), not this article.

The progression: rectifier → passive filter (this article) → linear regulator (simple, low-noise) OR switching regulator (efficient, complex). This article teaches the passive filter stage that precedes both.

## Prerequisites

- **[Passive Components](./passive-components.md)** — capacitor construction (dielectric types, ESR, ripple current), inductor construction (core materials, saturation current), resistor power ratings.
- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the preceding stage that produces the pulsating DC this article filters.
- AC circuit theory (reactance, impedance, frequency response) — *forthcoming ac-analysis article*.

## See Also

- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the upstream stage; ripple frequency and amplitude originate here.
- **[Power Supply Circuits](./power-supply-circuits.md)** — parent capability: the full rectifier→filter→regulator chain.
- **[Power Electronics](./power-electronics.md)** — switching regulators that combine filtering with regulation at high frequency.
- **[Passive Components](./passive-components.md)** — capacitor and inductor construction, ESR, saturation, and selection.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
