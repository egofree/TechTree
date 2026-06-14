# Inverter Circuits

> **Node ID**: `electronics.power-conversion-circuits.inverter-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md),
> [`electronics.passive-components`](./passive-components.md)
> **Outputs**: inverter-circuit-design
> **Timeline**: Years 30-50
> **Critical**: No

An inverter converts DC power into AC power. This is the mirror image of [rectifier circuits](./power-supply-circuits.rectifier-circuits.md) (AC→DC): where a rectifier uses passive diodes that steer whichever way the AC happens to flow, an inverter must **actively synthesize** an AC waveform from a DC source by rapidly opening and closing switches. This article covers the **circuit-level design pedagogy** — the H-bridge topology, square-wave and sinusoidal pulse-width modulation (SPWM), dead-time, device selection, and LC output filtering.

The boundary with the parent capability is explicit: this article teaches *how to design the switching circuit* that produces AC. The [power-electronics](./power-electronics.md) capability covers **system-level deployment** — packaging inverters into solar grid-tie systems, UPS units, and industrial cabinets, plus harmonic compliance, thermal management, and three-phase space-vector modulation. The [semiconductor devices](./semiconductor-devices.md) article covers the *physics* of the MOSFET/IGBT switches; here they are treated as controlled valves that open and close on command.

## The Fundamental Problem

A DC source (battery, solar panel, rectified mains) provides a constant voltage that flows in one direction. An AC load (motor, grid, appliance) expects a voltage that reverses polarity dozens of times per second and follows a smooth sinusoidal shape. We cannot turn DC into sine waves with transformers or linear amplifiers at any reasonable efficiency — a linear amplifier dissipating the difference between a DC rail and a sine would waste ~60% of the power as heat.

The solution is **switching**: use semiconductor switches (MOSFETs or IGBTs) that are either fully ON (near-zero voltage across them) or fully OFF (zero current through them). In both states the switch dissipates almost no power (P = V × I ≈ 0). By switching thousands of times per second and arranging the pulses cleverly, the *average* voltage seen by the load traces a sine wave. The high-frequency switching ripple is then stripped away by a passive LC filter. The result: 90–98% efficient DC→AC conversion with no dissipative element in the main power path.

```
   DC source            Switching network          LC filter          AC load
   (battery)            (4 switches in H)          (inductor+cap)     (motor)
     ┌──┐    ──▶ ╔═══════════════════╗ ──▶ ╔═══════════╗ ──▶ ┌─────┐
  +  │  │        ║  S1   ┊   S2      ║      ║  L     C  ║      │     ║
     │  │  ──▶   ║      LOAD         ║      ║           ║      │  R  ║
     │  │        ║  S3   ┊   S4      ║      ║           ║      │  L  ║
  ─  │  │    ──▶ ╚═══════════════════╝ ──▶ ╚═══════════╝ ──▶ │     ║
     └──┘                                                     └─────┘

   constant DC  ──▶  pulsed (PWM)  ──▶  smoothed sine  ──▶  load
```

The entire art of inverter design lives in three places: **how the four switches are wired** (the H-bridge), **how their on/off timing is chosen** (PWM strategy), and **how the result is filtered** (LC design). The sections below cover each in turn.

## The H-Bridge Topology

The full-bridge (H-bridge) is the standard single-phase inverter topology. Four controlled switches (S1–S4) are arranged in two vertical legs, with the load connected across the midpoints. Each switch has an anti-parallel diode (the switch's body diode in a MOSFET, or an external fast-recovery diode across an IGBT) to carry inductive load current when no switch is on.

```
                    +Vdc (DC bus +)
                     │
          ┌──────────┴──────────┐
          │                     │
        ┌─┴─┐                 ┌─┴─┐
        │S1 │                 │S2 │     Switches S1–S4: power MOSFETs
        │   │                 │   │              or IGBTs
        └─┬─┘                 └─┬─┘
          │       ┌───┐         │
          ├───────┤   ├─────────┤    ◀── AC output
          │       │ L │         │        (load)
          │       │ O │         │
          │       │ A │         │
          │       │ D │         │
          ├───────┤   ├─────────┤
          │       └───┘         │
        ┌─┴─┐                 ┌─┴─┐
        │S3 │                 │S4 │
        │   │                 │   │
        └─┬─┘                 └─┬─┘
          │                     │
          └──────────┬──────────┘
                     │
                    ───  (DC bus − / ground)
```

Each switch also carries a parallel diode (shown simplified). The diodes are essential: when an inductive load's current must keep flowing but all switches are off (during dead-time or on the "wrong" half-cycle), the diodes provide a return path and return energy to the DC bus. Without them, switching off an inductive current would produce a destructive voltage spike (V = L × dI/dt).

### Diagonal Switching — Producing AC

The two switches in one leg (S1 over S3, or S2 over S4) must **never** be on simultaneously — that would short the DC bus directly through both devices (a "shoot-through" fault that destroys them in microseconds). Instead, current is routed through the load by turning on **diagonal pairs**:

- **Positive half-cycle**: S1 + S4 ON, S2 + S3 OFF. Current flows: +Vdc → S1 → load (left-to-right) → S4 → ground. The load sees approximately +Vdc.
- **Negative half-cycle**: S2 + S3 ON, S1 + S4 OFF. Current flows: +Vdc → S2 → load (right-to-left) → S3 → ground. The load sees approximately −Vdc.
- **Zero state**: all switches OFF (current freewheels through the anti-parallel diodes).

By alternating the two diagonal pairs, the voltage across the load reverses polarity — that is already an AC waveform. The *shape* of that waveform depends entirely on **how long** each pair stays on during each cycle, which is the subject of PWM.

## Square-Wave Inverter

The simplest inverter switches each diagonal pair for exactly half the output period. The result is a **square wave** alternating between +Vdc and −Vdc at the output frequency (50 or 60 Hz).

```
   Switch
   states:        S1+S4 ON              S2+S3 ON              S1+S4
   S1,S4  ┌─────────────────┐┌─────────────────┐┌─────────────
          │                 ││                 ││
   ───────┤                 ├┤                 ├┤──────────────
          │                 ││                 ││
   S2,S3  │                 ││                 ││
          └─────────────────┘└─────────────────┘└─────────────
             T/2               T/2

   Output
   across     ┌─────────────┐   ┌─────────────┐   ┌─────────
   load:      │   +Vdc      │   │             │   │
              │             │   │             │   │
   ───────────┤             ├───┤             ├───┤──────────
              │             │   │   −Vdc      │   │
              │             │   │             │   │
              └─────────────┘   └─────────────┘   └─────────
                 T/2               T/2

   Fourier:  v(t) = (4Vdc/π) × [sin(ωt) + (1/3)sin(3ωt) + (1/5)sin(5ωt) + ...]
```

**Output (fundamental) RMS voltage**: the first (fundamental) Fourier component of a ±Vdc square wave has an amplitude of 4Vdc/π. Its RMS value is:

```
   V1,rms = (4Vdc/π) / √2 = 0.900 × Vdc
```

So a 170 V DC bus produces a 153 V RMS fundamental — enough for a 120 V load with some margin. But the square wave also contains large odd harmonics: the 3rd is 1/3 of the fundamental, the 5th is 1/5, and so on. The total harmonic distortion (THD) of an ideal square wave is about **48%** — far too high for motors (extra heating, torque ripple), transformers (core saturation), and audio electronics (buzz). It is acceptable only for crude loads like incandescent lamps or universal motors, which is why square-wave inverters are now restricted to the cheapest consumer models.

The path to a clean sine wave is to abandon "all-or-nothing" half-cycle switching and instead pulse the switches rapidly so that the *average* output voltage tracks a sine. That technique is PWM.

## Sinusoidal Pulse-Width Modulation (SPWM)

SPWM (also called "bipolar PWM" when generated by an H-bridge) encodes a low-frequency sine wave into a stream of high-frequency pulses. The principle: compare a **sine reference** (the desired output, 50/60 Hz) against a **triangle carrier** (much higher frequency — the switching frequency). Whenever the sine is greater than the triangle, turn on the S1+S4 diagonal; whenever the sine is less, turn on S2+S3.

```
   Amplitude
        ▲
   +Vdc │    ┌──┐      ┌────┐    ┌──────┐   ┌──┐      ← wide pulses
        │   ─┘  └──────┘    └────┘      └───┘  └──    (sine near peak)
        │  / \                                / \
        │ /   \   sine reference (fo)        /   \     ← desired output
        │/     \                            /     \
        │       \        /\        /\      /       \
        │        \      /  \      /  \    /         \
        │         \____/    \____/    \__/           \
   −Vdc │  ────────────────────────────────────────  ← narrow pulses
        │       (sine near zero)               (sine near zero)
        │
        ├──────┬──────┬──────┬──────┬──────┬──────▶ time
              carrier periods (1/fs each)

   When sine > carrier  ─▶  S1+S4 ON  ─▶  +Vdc across load
   When sine < carrier  ─▶  S2+S3 ON  ─▶  −Vdc across load
```

At the peaks of the sine, the sine stays above the triangle for most of each carrier period, so the +Vdc pulses are **wide**. Near the zero crossings, the sine crosses the triangle near its midpoint, so the pulses are **narrow and balanced** (roughly equal +Vdc and −Vdc dwell, averaging to zero). After the LC filter removes the high-frequency carrier, what remains is a clean sine wave whose amplitude is set by how wide the pulses get.

### Modulation Index and Output Voltage

The **modulation index** mₐ controls how tall the sine reference is relative to the triangle:

```
   mₐ = V_reference(peak) / V_carrier(peak)
```

- **mₐ ≤ 1.0** (linear region): the output fundamental RMS (line-neutral, single-phase H-bridge) is:

```
   V1,rms = (mₐ × Vdc) / √2
```

- **mₐ > 1.0** (overmodulation): the output saturates at the square-wave limit (V1,rms = 0.900 × Vdc) but low-order harmonics (3rd, 5th, 7th) reappear. Overmodulation trades waveform purity for more output voltage.
- **mₐ = 1.0** gives the maximum *clean* output: V1,rms = 0.707 × Vdc.

To hit a specific AC output from a given DC bus, size mₐ accordingly (worked example below).

### Worked SPWM Example — 230 V AC from a 400 V DC Bus

**Design goal**: synthesize a 230 V RMS, 50 Hz sine wave from a 400 V DC bus (typical of a rectified 230 V mains or a 48 V battery boosted to 400 V). Switching frequency 16 kHz.

**Step 1 — Required modulation index.** Use the linear-region formula and solve for mₐ:

```
   V1,rms = (mₐ × Vdc) / √2
   230    = (mₐ × 400) / 1.414
   mₐ     = (230 × 1.414) / 400 = 0.813
```

mₐ = 0.81 is comfortably below 1.0 — we are in the linear region, so the output will be a clean sine with low harmonics. Good design practice leaves 10–20% headroom (mₐ ≤ 0.9) so that bus voltage sag under load does not push the control into saturation.

**Step 2 — Output voltage verification.** Check the peak voltage the load sees (before the LC filter, the pulses are ±Vdc; after, the fundamental is what matters):

```
   V1,peak = mₐ × Vdc = 0.813 × 400 = 325 V
   V1,rms  = 325 / √2  = 230 V   ✓
```

**Step 3 — Switching period and carrier.** With fs = 16 kHz, each carrier period is Tₛ = 1/16000 = 62.5 µs. Over one 50 Hz output cycle (20 ms) the carrier produces 16000/50 = **320 switching pulses**. That is plenty of resolution — the sine is sampled 320 times per cycle, so the lowest significant harmonic in the output sits near the carrier (16 kHz ± multiples of 50 Hz), far above the 50 Hz fundamental and trivially removed by the LC filter.

**Step 4 — Estimate the dominant harmonic.** In bipolar SPWM the first significant harmonic cluster centers at the carrier frequency fₛ and its sidebands (fₛ ± 2fₒ, fₛ ± 4fₒ, ...). With fₛ = 16 kHz these are at ~15.9–16.1 kHz — inaudible and well above the filter cutoff. The low-order harmonics (3rd, 5th, 7th, 9th) that plague square-wave inverters are **natively suppressed** by SPWM and typically sit 40+ dB below the fundamental, giving THD < 3–5% even before filtering.

**Step 5 — Power and device current.** If the load draws 4.6 A RMS at 230 V (≈ 1 kVA), the switch peak current is approximately √2 × 4.6 = 6.5 A plus the filter inductor ripple (design for 20–30% ripple). Select switches rated ≥ 2× this current and ≥ 1.3× the DC bus: from the [semiconductor-devices](./semiconductor-devices.md) catalog a 600 V, 20 A MOSFET (e.g., an IRF type) is a comfortable fit.

## Dead-Time

Real switches do not turn off instantly. A MOSFET takes 20–100 ns to turn off, but its gate driver has finite drive current and there is parasitic gate resistance and capacitance; an IGBT is slower still (200–500 ns, with a "tail current" that lingers). If the controller commands the upper switch of a leg OFF and the lower switch ON at the same instant, both will briefly be partially ON at the same time — and the DC bus is shorted directly through the leg (S1 and S3 in series across +Vdc/ground).

This **shoot-through** condition produces a current spike limited only by the switches' on-resistance and bus parasitics — easily hundreds of amps — that destroys both devices in microseconds. The defense is **dead-time**: a deliberate gap (t_dt = 0.5–2.0 µs for MOSFETs, 2–4 µs for IGBTs) inserted between turning one switch off and turning its complement on, guaranteeing one is fully off before the other begins conducting.

```
   Ideal command     S1: ─────────┐         ┌──────────
   (no dead-time)         OFF     │ ON      │     OFF
                                  │         │
                              ────┘         └────
                                  │         │
                       S3:        │┌────────┐
                              OFF ││  ON    │  OFF
                              ────┘└────────┘────
                                  ◄▲►
                              shoot-through!  ← both partially ON

   With dead-time      S1: ─────────┐              ┌──────────
                                  │              │
                              ────┘              └────
                                            ◄────▲────▶
                                  │      │  dead-time  │
                       S3:        │      │   (both OFF)│
                              ────┘      └────────────┘────
                                  OFF  delay  ON
```

During the dead-time, neither switch is on, so the inductive load current must flow through the anti-parallel diodes — which is exactly what they are there for. The penalty is a small **output voltage error**: for one dead-time interval per switching edge, the output voltage is determined by the load current direction (via the diode) rather than the controller command. The accumulated error over a half-cycle produces a low-order distortion (5th, 7th harmonics) proportional to (t_dt × fₛ). At 16 kHz with 1 µs dead-time this is about 1.6% of the period — visible in precision measurements and corrected in digital controllers by "dead-time compensation" algorithms.

### Setting the Dead-Time

| Device type | Typical t_dt | Reason |
|-------------|--------------|--------|
| Logic-level MOSFET (low voltage) | 100–300 ns | Fast switching, low gate charge |
| Power MOSFET (TO-220/TO-247) | 0.5–1.0 µs | Gate charge 30–150 nC, driver finite current |
| IGBT module (industrial) | 2.0–4.0 µs | Tail current extends turn-off |
| SiC MOSFET | 200–500 ns | Very fast, but dv/dt sensitivity |

Too little dead-time → shoot-through failures. Too much → output distortion and reduced maximum duty cycle. The right value is the smallest gap that guarantees turn-off completes under worst-case conditions (high temperature, low gate-drive voltage, maximum load current).

## MOSFET vs IGBT Selection

The choice of switching device is the dominant decision in inverter design after the topology. The [semiconductor-devices](./semiconductor-devices.md) article covers the physics of each; here we focus on **when to choose which** for an inverter. The decision hinges on a single trade-off: conduction loss vs switching loss, and how each scales with voltage.

**Power MOSFETs** conduct through a resistive channel (R_DS(on)). Conduction loss is I² × R_DS(on), and in silicon R_DS(on) rises roughly as V_DS²·⁵ — so above ~600 V the on-resistance becomes impractically high. But MOSFETs switch very fast (10–100 ns) because they are majority-carrier devices with no stored charge, so switching loss is low even at high frequency. This makes them ideal for **low-voltage, high-frequency** inverters (12/24/48 V battery systems, point-of-load, switching at 50–200 kHz).

**IGBTs** conduct like a BJT (fixed ~1.5–2.5 V saturation voltage, V_CE(sat)). Conduction loss is I × V_CE(sat), which is roughly linear in current and **independent of voltage** — so at high voltage an IGBT loses far less than a MOSFET whose R_DS(on) has ballooned. The penalty is a "tail current" at turn-off (minority carrier recombination) that makes them slower (5–40 kHz practical) and increases switching loss. IGBTs dominate **high-voltage, high-power** inverters (motor drives, grid-tie, EV traction).

```
   Conduction loss
   (per device)
        ▲
        │                ┌─── IGBT: P = I × Vce(sat)
        │              ╱         (slope ~ constant in V)
        │            ╱
        │          ╱     ──── MOSFET: P = I² × Rds(on)
        │        ╱              (rises as V²·⁵ with rating)
        │      ╱
        │    ╱
        │  ╱
        │╱
        └────────────────────────────────────────▶ current

   Cross-over: at high voltage (≥600 V) IGBT wins on conduction;
   at low voltage MOSFET wins on switching loss + adequate Rds(on).
```

| Application | Bus voltage | Switch freq | Best device | Reason |
|-------------|-------------|-------------|-------------|--------|
| 12/24 V car inverter | 12–48 V | 50–200 kHz | MOSFET | Low R_DS(on) at low V; fast |
| 48 V telecom / solar | 48–100 V | 20–100 kHz | MOSFET | Low R_DS(on); high f shrinks filter |
| Residential solar (string) | 300–400 V | 5–20 kHz | MOSFET (superjunction) or IGBT | Crossover zone; SiC if available |
| Motor drive (480 V) | 575–800 V | 2–8 kHz | IGBT (1200 V) | High V → MOSFET R_DS(on) too high |
| EV traction | 300–800 V | 8–20 kHz | IGBT or SiC MOSFET | SiC for efficiency, IGBT for cost |
| Grid-tie utility | 1000–1500 V | 1–5 kHz | IGBT (1700–3300 V) | Very high V; modular stacks |
| HVDC / FACTS | 1000–10000 V | line freq | Thyristor / IGCT | Highest power; gate-turn-off not PWM |

The wide-bandgap devices (SiC MOSFET, GaN HEMT) shift these boundaries upward: SiC MOSFETs combine IGBT-like voltage handling with MOSFET-like switching speed, enabling 50–250 kHz switching at 650–3300 V. They are covered in [semiconductor-devices](./semiconductor-devices.md); the circuit design here treats them as faster, lower-loss drop-ins once available.

## Output Filtering — the LC Filter

The raw H-bridge output is a sequence of ±Vdc pulses at the switching frequency. The load wants a smooth 50/60 Hz sine. A passive **LC low-pass filter** between the bridge and the load removes the high-frequency switching content while passing the low-frequency fundamental.

```
   H-bridge                      LC filter                 Load
   output ──▶ ╔═══╗ ──▶ ────L─────┬─────────┬───── ──▶ ┌─────┐
             ║   ║          │         │              │     ║
             ║PWM║          │         │              │ AC  ║
             ║   ║          C        (Rd)            │ load║
             ║   ║          │         │              │     ║
   ground ──▶ ╚═══╝ ──▶ ────────────┴─────────┴───── ──▶ └─────┘

   Filter cutoff:  fc = 1 / (2π √(LC))   ◀── set well above fo, well below fs
```

The design rule for placing the cutoff frequency f_c:

```
   f_o  (output)  ≪  f_c  ≪  f_s  (switching)

   f_o  = 50/60 Hz
   f_s  = 5–20 kHz
   f_c  = 1–5 kHz  (typical: a decade above fo, a decade or more below fs)
```

Placing f_c at roughly √(f_o × fₛ) — the geometric mean — gives the best compromise. For 50 Hz output and 16 kHz switching, that is √(50 × 16000) ≈ **900 Hz**. From there pick L and C to hit the cutoff:

```
   fc = 1 / (2π √(LC))   ──▶   LC = 1 / (2π fc)²

   For fc = 1 kHz:   LC = 1 / (2π × 1000)² = 2.53 × 10⁻⁸
                     Pick L = 2 mH  ──▶  C = 2.53×10⁻⁸ / 0.002 = 12.7 µF
                     ──▶ use L = 2 mH, C = 10–15 µF (film capacitor).
```

**Practical values** for a 1–5 kW single-phase inverter switching at 16 kHz: L = 1–5 mH (ferrite or iron-powder core, ~20 turns), C = 5–20 µF (polypropylene film — not electrolytic, which has high ESR and short life at ripple frequency). The inductor must handle the full load current without saturating; the capacitor must handle the ripple current at the switching frequency. Both components come from [passive-components](./passive-components.md).

A damping resistor (Rd, 1–10 Ω, a few watts) in series with a small capacitor across the output is sometimes added to suppress the filter's natural resonance (Q control) — without it, transient load steps can ring at f_c.

## Parameter Table — Inverter Design Space

The table below maps the typical operating envelope of single-phase H-bridge inverters across power levels:

| Power range | Switch freq | Efficiency | Output THD | Typical device | DC bus | Filter |
|-------------|-------------|-----------|-----------|----------------|--------|--------|
| 50–200 W (cabin UPS) | 20–50 kHz | 85–92% | < 5% | MOSFET, 60–100 V | 12/24 V | L=0.5 mH, C=5 µF |
| 200 W–1 kW (home inverter) | 16–25 kHz | 90–95% | < 5% | MOSFET, 100–250 V | 48 V | L=1 mH, C=10 µF |
| 1–5 kW (residential solar) | 8–20 kHz | 93–97% | < 3% | Superjunction MOSFET, 600 V | 350–400 V | L=2 mH, C=10 µF |
| 5–20 kW (commercial) | 5–16 kHz | 95–97% | < 3% | IGBT, 600–1200 V | 575–800 V | L=2–5 mH, C=10–20 µF |
| 20–100 kW (industrial) | 2–8 kHz | 95–98% | < 3% | IGBT module, 1200 V | 575–800 V | L=5 mH, C=20–50 µF |
| 100 kW–1 MW (grid-tie) | 1–5 kHz | 96–98% | < 3% | IGBT module, 1700–3300 V | 1000–1500 V | LCL filter |

Notes on the table:
- **Efficiency** is end-to-end (DC bus to AC output, including filter and gate-drive losses); the dominant loss shifts from switching loss (low power, high f) to conduction loss (high power, high current) as power increases.
- **THD < 3%** at the load is the common target — well under the IEEE 519 5% limit at the point of common coupling. Achievable with SPWM + a properly sized LC filter.
- **Switching frequency** drops as power rises because switching loss (Pₛw = ½ V I (t_r + t_f) fₛ) scales with both current and frequency; at high current, lowering fₛ is the only way to keep junction temperature under control. The filter must then grow (larger L, C) to keep f_c well below fₛ.
- At 100 kW+, the simple LC filter is replaced by an **LCL filter** (two inductors with a shunt capacitor) which gives 40 dB/decade (instead of 20) of high-frequency attenuation, allowing smaller magnetics for the same ripple spec — but it introduces a resonant peak that must be passively or actively damped.

## Comparison with System-Level Inverters

This article owns the **circuit-design pedagogy**: how the four switches are arranged, how SPWM timing is computed, how dead-time is set, how the LC filter is sized. The [power-electronics](./power-electronics.md) capability owns **system-level deployment**:

| This article (circuit design) | power-electronics.md (system level) |
|-------------------------------|-------------------------------------|
| H-bridge topology, diagonal switching | Single-phase vs three-phase inverter selection |
| SPWM modulation index, mₐ | Space-vector modulation (15% better DC bus use) |
| Dead-time calculation per device | Three-phase 6-switch motor drive architecture |
| MOSFET vs IGBT per voltage/power | Paralleling devices, IGBT modules, bus-bar design |
| LC filter component sizing | LCL grid-tie filters, IEEE 519 harmonic compliance |
| Gate-drive timing (this article) | Gate-driver isolation, desat protection, packaging |

The boundary is: read this article to *design the switching circuit*; read power-electronics to *build the product around it*.

## Prerequisites

- **[Semiconductor Devices](./semiconductor-devices.md)** — MOSFET and IGBT construction, R_DS(on), V_CE(sat), gate charge, switching characteristics, body/anti-parallel diodes. This article treats them as controlled switches.
- **[Passive Components](./passive-components.md)** — inductor core selection (saturation current, Bmax), capacitor type and ESR (film vs electrolytic for ripple current), the magnetics that make up the LC filter.
- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the inverse operation (AC→DC) and the source of the DC bus that an inverter consumes.
- **[Filter Circuits](./power-supply-circuits.filter-circuits.md)** — LC low-pass filter cutoff design (f_c = 1/(2π√LC)), the same math used here for the inverter output filter.
- **[Circuit Fundamentals: AC Analysis](./circuit-fundamentals.ac-analysis.md)** — RMS vs peak, sinusoidal waveform properties, reactance, impedance.

## See Also

- **[Power Conversion Circuits](./power-conversion-circuits.md)** — parent capability: DC→AC inversion, variable-frequency drive architecture, switching-device selection at the circuit level.
- **[Power Electronics](./power-electronics.md)** — system-level inverter applications: grid-tie solar, UPS, three-phase motor drives, harmonic compliance.
- **[Semiconductor Devices](./semiconductor-devices.md)** — MOSFET/IGBT physics, device parameters, wide-bandgap (SiC, GaN) devices.
- **[Passive Components](./passive-components.md)** — inductor and capacitor construction, core materials, ripple-current ratings.
- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the AC→DC mirror image, source of the DC bus an inverter consumes.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
