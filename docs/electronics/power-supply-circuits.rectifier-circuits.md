# Rectifier Circuits

> **Node ID**: `electronics.power-supply-circuits.rectifier-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md),
> [`electronics.passive-components`](./passive-components.md),
> [`electronics.circuit-fundamentals.ac-analysis`](./circuit-fundamentals.ac-analysis.md),
> [`electronics.analog-circuits.diode-circuits`](./analog-circuits.diode-circuits.md)
> **Outputs**: rectified-dc
> **Timeline**: Years 20-40
> **Critical**: No

Rectification is the first stage of every power supply — the process of converting bidirectional AC current into unidirectional (pulsating) DC. This article covers the **circuit-level design pedagogy** of diode rectifier topologies: how the diodes are arranged, how the output waveform looks, how to calculate ripple voltage, and how to select diodes and transformers for a given load. The diode physics itself (pn junction formation, forward/reverse characteristics, V-I curve) is covered in [semiconductor-devices](./semiconductor-devices.md) — this article treats the diode as a one-way valve and focuses on topology.

The downstream stages — [filtering](./power-supply-circuits.filter-circuits.md) the pulsating waveform and [regulating](./power-supply-circuits.md) the result to a stable voltage — are separate articles. System-level rectifier manufacturing (packaging, thermal management, industrial deployment) belongs to [power-electronics](./power-electronics.md).

## The Fundamental Principle

A diode conducts when its anode is positive relative to its cathode (forward bias) and blocks when reversed. By arranging diodes in specific topologies, we steer both half-cycles of an AC waveform so that current always flows through the load in the same direction. The output is no longer alternating — but it is not yet smooth DC. It is pulsating DC whose ripple frequency depends on the topology:

| Topology | Diode Count | Output Pulses per Cycle | Ripple Frequency (60 Hz in) | Ripple Factor (no filter) |
|----------|------------|------------------------|----------------------------|---------------------------|
| Half-wave | 1 | 1 | 60 Hz | 1.21 (121%) |
| Full-wave center-tap | 2 | 2 | 120 Hz | 0.48 (48%) |
| Bridge | 4 | 2 | 120 Hz | 0.48 (48%) |
| 3-phase half-wave | 3 | 3 | 360 Hz | 0.17 (17%) |
| 3-phase bridge | 6 | 6 | 360 Hz | 0.042 (4.2%) |

Ripple factor γ = V_rms(ripple) / V_dc. Lower is better. Note that even the best unfiltered rectifier (3-phase bridge) still has 4.2% ripple — filtering is always needed for clean DC.

## Half-Wave Rectifier

The simplest topology: a single diode in series with the load. Only the positive half-cycle passes through; the negative half-cycle is blocked.

```
         Transformer                Diode          Load
  AC mains ──▶ ╔═══════╗      A ┌───┐ K         ┌──────┐
  120V, 60Hz   ║       ║  ─────┤ ▶ │───────────▶│  R   │
               ║ iron  ║       │   │            │ LOAD │
         ──▶   ║ core  ║       └───┘            └──┬───┘
               ║       ║                            │
               ╚═══════╝                            │
                 ╦═══╦                              │
    Secondary ──╬ ─── ╬─────────────────────────────┘
                 ╩═══╩
              center-tap
              (not used here)

  Input:  V = Vp sin(ωt)        Output across load:

  ┌──────────────┐            ┌──────────────┐
  │   /\    /\   │            │  /\     /\   │     Only positive
  │  /  \  /  \  │            │ /  \   /  \  │  ←  half-cycles pass.
  │ /    \/    \ │            │/    \_/    \ │     Gap during
  │/      AC     │            │      DC      │     negative half
  └──────────────┘            └──────────────┘
```

**Ripple voltage** (capacitor-input filter, half-wave):

```
  V_ripple = I_load / (f · C)

  where:
    f       = ripple frequency = mains frequency (60 Hz for half-wave)
    C       = filter capacitance (farads)
    I_load  = DC load current (amps)
```

The ripple appears at the line frequency because only one pulse per cycle reaches the output. This makes half-wave the hardest topology to filter — for the same ripple spec, it needs twice the capacitance of a full-wave design.

**Average DC output** (no filter): V_dc = Vp / π ≈ 0.318 × Vp, where Vp is the peak secondary voltage.

**Peak Inverse Voltage (PIV)** the diode must withstand: PIV = Vp. During the negative half-cycle, the full peak voltage appears across the blocking diode.

## Full-Wave Center-Tap Rectifier

Uses a transformer with a center-tapped secondary and two diodes. Each diode conducts on alternate half-cycles, so both halves of the AC waveform contribute to the output. The center tap serves as the DC return (ground).

```
                         D1
                    A ┌───┐ K
            ┌────────┤ ▶ ├──────────┐
            │        └───┘          │
     ╔══════╣                       ├──▶ ┌──────┐
     ║      ║ top half               │    │  R   │
AC   ║ iron ║                  +─────┘    │ LOAD │──── 0V
mains║ core ║                          ┌──┴──────┤── ground
     ║      ║        ┌───┐             │         │
     ╚══════╬────────┤ ▶ ├─────────────┘         │
            │     D2 └───┘                       │
            └────────────────────────────────────┘
              ──╦── center tap (ground) ─────────┘
                ╩

  Both half-cycles rectified. Ripple at 2× line freq (120 Hz).
```

**Ripple voltage** (capacitor-input filter, full-wave):

```
  V_ripple = I_load / (f_ripple · C) = I_load / (2f · C)

  where f_ripple = 2 × mains frequency (120 Hz for 60 Hz input)
```

This is half the ripple of half-wave for the same capacitor, because the filter capacitor is recharged twice per cycle instead of once.

**Average DC output** (no filter): V_dc = 2Vp / π ≈ 0.637 × Vp (where Vp is half-secondary peak).

**PIV per diode**: 2Vp (each diode sees the full secondary voltage when its counterpart conducts — the conducting diode clamps one end to ground, so the full end-to-end voltage appears across the off diode).

**Trade-off**: The center-tap transformer only uses half the secondary winding at a time, so copper utilization is poor. The transformer must be physically larger for a given power rating than a bridge-rectifier transformer. However, only 2 diodes are needed and only one diode drop (0.7V) is lost in the conduction path, which matters for low-voltage outputs.

## Bridge Rectifier

The most common single-phase topology. Four diodes arranged in a diamond (H-bridge) steer both half-cycles without needing a center-tapped transformer. For each half-cycle, a different pair of diagonal diodes conducts.

```
               ┌─── D2 ───┐        ┌─── D4 ───┐
         ┌─────┤ ▶       ├── + ───┤ ▶       ├─────┐
         │     └──────────┘   │    └──────────┘     │
  AC ────┤ AC terminal 1      │               AC terminal 2 ────┐
  in     │                  LOAD R            │                  │
         │                     │              │                  │
         │     ┌──────────┐   │   ┌──────────┐     │
         └─────┤ ▶       ├─── 0V ──┤ ▶       ├─────┘
               └─── D1 ───┘        └─── D3 ───┘

  Positive half-cycle: D1+D4 conduct, D2+D3 block
  Negative half-cycle: D2+D3 conduct, D1+D4 block
```

Or drawn as the classic diamond:

```
            D1
       A ┌───┐ K
    ┌────┤ ▶ ├────┐
    │    └───┘    ├──▶ +Vdc ──┐
  AC1            │            │
    │    ┌───┐   │         LOAD R
    └────┤ ▶ ├───┘            │
       A │   │ K              │
          D3                  │
             D2               │
          K ┌───┐ A           │
    ┌────┤ ▶ ├────┐           │
    │    └───┘    ├──▶ 0V ────┘
  AC2            │
    │    ┌───┐   │
    └────┤ ▶ ├───┘
       K │   │ A
          D4
```

**Ripple voltage** (capacitor-input filter, full-wave): Same as center-tap:

```
  V_ripple = I_load / (2f · C)       (120 Hz ripple for 60 Hz input)
```

**Average DC output** (no filter): V_dc = 2Vp / π ≈ 0.637 × Vp (Vp = full secondary peak).

**PIV per diode**: Vp (each diode only sees the peak secondary voltage — the lowest PIV of any topology for a given output). This is the key advantage over center-tap.

**Trade-off**: Two diode drops are always in the conduction path (0.7V + 0.7V = 1.4V for silicon), reducing efficiency at low output voltages. For a 5V supply, 1.4V is 28% of the output — significant. Schottky diodes (V_F = 0.3V each, 0.6V total) mitigate this.

### Bridge Rectifier IC Modules

The four diodes are commonly packaged as a single bridge rectifier IC (e.g., KBP, WOG, GBL packages) with 4 pins: two AC inputs (~), one positive (+), one negative (−). This simplifies assembly and ensures matched thermal characteristics. Ratings: 1–50A, 50–1000V.

## Polyphase Rectification

For industrial power levels (above ~5 kW), three-phase rectification is standard. It produces much lower ripple without any filter, and the ripple frequency is 6× the line frequency (360 Hz for 60 Hz input), making filtering trivial.

### Three-Phase Half-Wave (3 diodes)

Each phase feeds through one diode to a common output. The diode whose phase voltage is highest at any instant conducts; the others block. Three pulses per cycle:

```
  Phase A ──────┤ ▶ ├──────┐
                 D1         │
  Phase B ──────┤ ▶ ├──────┼──▶ +Vdc ── LOAD ──┐
                 D2         │                    │
  Phase C ──────┤ ▶ ├──────┘                    │
                 D3                               │
  Neutral ────────────────────────────────────────┘

  Output: 3 pulses per cycle, 360 Hz ripple for 60 Hz in.
  V_dc = 1.17 × V_phase_rms (no filter)
```

### Three-Phase Bridge (6 diodes)

Two three-diode groups (upper and lower) form a full bridge. Six pulses per cycle — the gold standard for industrial DC power:

```
  Phase A ──────┬──────────────┬─────────┐
                │              │         │
             ┌───┐          ┌───┐       │
             │ ▶ │ D1       │ ▶ │ D4    │
             └───┘          └───┘       │
                │              │         │
  Phase B ──┬───┴──────────┬───┴─────── │
            │              │         │  │
         ┌───┐          ┌───┐       │  │
         │ ▶ │ D3       │ ▶ │ D6    │  │
         └───┘          └───┘       │  │
            │              │         │  │
  Phase C ──┴───┬──────────┴─────────┘  │
                │              │         │
             ┌───┐          ┌───┐       │
             │ ▶ │ D5       │ ▶ │ D2    │
             └───┘          └───┘       │
                │              │         │
                ├──────────────┤    ┌────┴────┐
                │              │    │  LOAD   │
              +Vdc           0V    └─────────┘

  Output: 6 pulses per cycle, 360 Hz ripple for 60 Hz in.
  V_dc = 1.35 × V_line_rms (no filter)
  Ripple factor: 4.2% (no filter needed for motor loads)
```

**Ripple** (capacitor-input): V_ripple = I_load / (6f · C) — six times less than half-wave for the same capacitor.

**PIV per diode**: √2 × V_line_rms (peak line-line voltage).

## Ripple Voltage Calculation — Unified Formula

All capacitor-input ripple calculations reduce to one formula:

```
  V_ripple(p-p) = I_load / (N · f · C)

  where:
    N = pulses per cycle (1 = half-wave, 2 = full-wave, 3 = 3φ HW, 6 = 3φ bridge)
    f = AC input frequency (Hz)
    C = filter capacitance (F)
    I_load = DC load current (A)
```

This formula assumes the capacitor discharges approximately linearly between charging pulses (valid when V_ripple << V_dc). The capacitor recharges to the peak voltage at each pulse, then supplies the load current between pulses. Lower ripple requires either more pulses (N), more capacitance (C), or higher frequency (f — the basis for switching power supply advantages).

## Diode Selection

Three parameters determine diode suitability for a rectifier application:

### 1. Peak Inverse Voltage (PIV / V_RRM)

The maximum reverse voltage the diode must block without conducting or breaking down. Select a diode rated at **2× the calculated PIV** for safety margin:

| Topology | PIV per diode | Rule of thumb |
|----------|--------------|---------------|
| Half-wave | Vp (sec peak) | ≥ 2 × Vp |
| Full-wave center-tap | 2 × Vp (half-sec) | ≥ 4 × Vp |
| Bridge | Vp (sec peak) | ≥ 2 × Vp |
| 3φ bridge | √2 × V_LL | ≥ 2√2 × V_LL |

If the PIV is exceeded, the diode enters avalanche breakdown and conducts in reverse — destroying itself and feeding AC back to the load.

### 2. Average Forward Current (I_F(AV))

The diode must carry the load current averaged over a full cycle. In a bridge rectifier, each diode carries current for half the cycle, so I_F(AV) per diode = I_load / 2. Select a diode rated at **1.5–2× the calculated average** for thermal margin. At 1A DC load in a bridge, each diode sees 0.5A average — use 1A-rated diodes minimum.

### 3. Forward Voltage Drop (V_F)

Power lost per diode = V_F × I_avg. Silicon PN diodes: 0.7–1.0V. Schottky: 0.2–0.4V. For low-voltage outputs (<12V), Schottky diodes are strongly preferred — a 1.4V drop (two silicon diodes in a bridge) wastes 12% of a 12V supply and 28% of a 5V supply.

### Surge Current (I_FSM)

At power-on, the filter capacitor is discharged and initially appears as a short circuit. The first half-cycle can draw a massive surge current (10–100× rated current for one cycle). The diode's surge rating (I_FSM, non-repetitive) must exceed this. Typically: I_FSM ≥ 25 × I_load.

## Worked Example: Bridge Rectifier for 12V DC at 1A

**Design goal**: 12V DC at 1A load, from 120V AC / 60 Hz mains, using a bridge rectifier with capacitor filter. Target ripple ≤ 1V p-p.

### Step 1 — Transformer Selection

The DC output under load = V_peak − V_ripple/2 − 2×V_F(diode). We want 12V at the load. Working backwards:

```
  V_dc ≈ V_peak − V_ripple/2 − 1.4V (two diode drops)

  12V ≈ V_peak − 0.5V − 1.4V
  V_peak ≈ 13.9V

  V_rms(secondary) = V_peak / √2 = 13.9 / 1.414 = 9.83V
```

Select a **10V RMS** secondary transformer (standard value). Actual peak: 10 × √2 = 14.14V. With diode drops and ripple: 14.14 − 1.4 − 0.5 = 12.2V DC. Close enough.

**Transformer VA rating**: 1.2–1.8× the DC output power to account for capacitor charging peaks and transformer heating. DC power = 12V × 1A = 12W. Select a **15 VA** (or larger) transformer.

### Step 2 — Filter Capacitor

Target ripple: 1V p-p at 120 Hz (full-wave):

```
  C = I_load / (2f · V_ripple) = 1.0 / (2 × 60 × 1.0) = 8333 μF

  Select: 10,000 μF (10000 μF), 25V electrolytic capacitor
```

The 25V rating provides margin above the 14.1V peak. Standard capacitor value (10 mF) gives V_ripple = 1.0/(120 × 0.01) = 0.83V — better than target.

### Step 3 — Diode Selection

```
  PIV = V_peak = 14.14V → Select ≥ 2× = 30V minimum
  I_F(AV) per diode = I_load / 2 = 0.5A → Select ≥ 1A
  I_FSM (surge) = 25 × I_load = 25A minimum
  V_F = 0.7V (silicon) or 0.3V (Schottky, preferred for 12V)
```

**Selection**: 1N5822 Schottky (3A, 40V, V_F = 0.34V at 3A) — generous current margin, adequate PIV, low forward loss. Four needed for the bridge. Power loss per bridge: 2 × 0.34 × 1A = 0.68W.

Alternative: KBP206 bridge module (2A, 600V) — simpler assembly, higher PIV margin, but higher V_F (1.1V per pair = 1.1W loss).

### Step 4 — Bleeder Resistor (optional)

A resistor across the capacitor discharges it safely when power is removed. Select for ~5× RC time constant under 1 second and bleed current <10% of load:

```
  R_bleeder = V_dc / I_bleeder = 12V / 0.1A = 120Ω (2W)
  Discharge time: 5 × R × C = 5 × 120 × 0.01 = 6 seconds
```

Or use 1kΩ (1/4W): bleed current = 12mA (1.2% of load), discharge in 50 seconds.

### Step 5 — Fuse

Primary-side fuse: 15VA / 120V = 0.125A. Select a 0.25A slow-blow fuse (allows magnetizing inrush current). Secondary-side fuse (optional): 1.5A fast-blow.

### Summary

```
  ┌─────────────────────────────────────────────────────────┐
  │  Final BOM:                                             │
  │  • 120V:10V transformer, 15 VA                          │
  │  • 4× 1N5822 Schottky diodes (or KBP206 bridge module)  │
  │  • 10,000 μF / 25V electrolytic capacitor               │
  │  • 1 kΩ / ¼W bleeder resistor                           │
  │  • 0.25A slow-blow fuse (primary)                       │
  │  Output: 12.2V DC, 0.83V p-p ripple, 1A capability      │
  └─────────────────────────────────────────────────────────┘
```

Note: 12.2V unregulated will rise to ~14V at light load and sag under heavy load. A downstream [voltage regulator](./power-supply-circuits.md) (linear or switching) is needed for a stable 12.0V.

## Transformer Sizing Considerations

The transformer secondary RMS voltage must account for:

1. **Diode drops**: subtract 2×V_F (bridge) or 1×V_F (center-tap).
2. **Ripple**: subtract V_ripple/2 from the average.
3. **Line tolerance**: mains voltage varies ±10%. Design for low-line (108V input).
4. **Regulation**: transformer output sags 5–15% from no-load to full-load.

A common mistake: selecting a 12V transformer for a 12V DC supply. After diode drops (1.4V), ripple (0.8V), regulation (1.2V), and low-line (1.2V), the output at full load drops to ~8.4V — far below 12V. Rule of thumb: the transformer secondary RMS should be 1.2–1.5× the target DC voltage for a filtered supply with regulator headroom.

## Comparison with System-Level Rectification

This article covers **circuit-level design** — selecting topology, calculating ripple, choosing diodes, sizing transformers. The [power-electronics](./power-electronics.md) capability covers **system-level deployment** — packaging rectifiers into industrial equipment, thermal management for high-power bridges, controlled thyristor rectifiers for motor drives, and harmonic compliance with IEEE 519. The boundary is: this article teaches *how to design the circuit*; power-electronics teaches *how to build the system around it*.

## Prerequisites

- **[Semiconductor Devices](./semiconductor-devices.md)** — diode construction, V-I characteristics, forward/reverse recovery, V_F and PIV physics.
- **[Passive Components](./passive-components.md)** — transformers (turns ratio, VA rating), capacitors (ESR, ripple current rating), bleeder resistors.
- **[Electrical Systems](./electrical-systems.md)** — mains wiring, safety grounding, fusing, transformer isolation.
- AC circuit theory (RMS, peak, frequency, reactance) — *forthcoming ac-analysis article*.

## See Also

- **[Filter Circuits](./power-supply-circuits.filter-circuits.md)** — the next stage: smoothing rectifier output into low-ripple DC.
- **[Power Supply Circuits](./power-supply-circuits.md)** — parent capability: the full rectifier→filter→regulator chain.
- **[Power Electronics](./power-electronics.md)** — system-level rectifier manufacturing, controlled thyristor bridges, three-phase industrial systems.
- **[Semiconductor Devices](./semiconductor-devices.md)** — diode physics, Schottky vs. PN junction, zener references.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
