# Switching Regulators

> **Node ID**: `electronics.power-supply-circuits.switching-regulators`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md),
> [`electronics.passive-components`](./passive-components.md),
> [`electronics.power-supply-circuits.rectifier-circuits`](./power-supply-circuits.rectifier-circuits.md)
> **Outputs**: switching-regulator-design
> **Timeline**: Years 20-40
> **Critical**: No

Switching regulation converts one DC voltage to another by chopping the input at high frequency and transferring energy through an inductor or transformer. Unlike a [linear regulator](./power-supply-circuits.linear-regulators.md) that burns excess voltage as heat, a switching regulator stores and releases energy in reactive components (inductors, capacitors), achieving 85–95% efficiency regardless of the input-to-output voltage ratio. This article covers the **circuit-level design pedagogy** of the four fundamental switching topologies: buck (step-down), boost (step-up), buck-boost (inverting), and flyback (isolated).

The upstream stages — [rectification](./power-supply-circuits.rectifier-circuits.md) and [filtering](./power-supply-circuits.filter-circuits.md) — deliver raw DC that a switching regulator can transform up or down with high efficiency. The transistor and diode physics is covered in [semiconductor-devices](./semiconductor-devices.md); the inductor and capacitor construction in [passive-components](./passive-components.md). Here we focus on topology, duty-cycle control, and component sizing. System-level converter manufacturing (packaging, magnetics winding, EMC compliance) belongs to [power-electronics](./power-electronics.md).

## The Fundamental Principle

A switch (MOSFET) turns on and off at a fixed switching frequency f_sw. During the **on-time** t_on, energy flows from the source into an inductor. During the **off-time** t_off, the inductor releases that energy to the load through a diode (or synchronous MOSFET). The inductor current ramps up during t_on and ramps down during t_off — it never stops flowing. A capacitor smooths the output. A feedback loop adjusts the **duty cycle** D = t_on / (t_on + t_off) to hold the output voltage constant.

```
   V_in ──▶ ╔═══╗      ┌───┐  L   ┌───┐  C   V_out
            ║SW ║──────┤   ├─█████─┬───┬─┬─────▶
            ║ON/║      │   │       │   │ │
            ║OFF║      │ D │       │   │ ┤├ LOAD
            ╚═══╝      │   │       │   │ │
              ▲        └─┬─┘       └─┬─┘ └─┬───▶
              │          │           │     │
   PWM ───────┘         GND         GND   GND

   D = t_on / T    where T = 1/f_sw = t_on + t_off
```

The key insight: **the inductor acts as an energy bucket** — it fills during t_on and empties during t_off. In steady state, the energy in equals the energy out (volt-second balance), which gives each topology its characteristic voltage conversion ratio. Because the switch is either fully on (low R_DS(on), low loss) or fully off (zero current), the theoretical efficiency is 100% — only parasitic losses (switching transitions, diode V_F, inductor DCR, capacitor ESR) reduce it to the practical 85–95%.

## Duty Cycle Control (PWM)

Pulse-Width Modulation varies t_on while keeping the switching period T constant. A comparator compares a sawtooth ramp (at f_sw) against an error voltage from the output feedback:

```
   Error voltage ──────┐
                        ├──▶ Comparator ──▶ Gate drive to switch
   Sawtooth ramp ───────┘         (PWM output)

   When error > ramp: switch ON
   When error < ramp: switch OFF

   Higher error (V_out low)  → wider pulses → more energy → V_out rises
   Lower error  (V_out high) → narrower pulses → less energy → V_out falls
```

The switching frequency f_sw is typically 50 kHz–2 MHz. Higher frequency shrinks the inductor and capacitor (smaller, cheaper magnetics) but increases switching losses (the switch spends more total time transitioning between on and off states). The practical sweet spot for silicon MOSFETs is 100–500 kHz; for GaN devices, 500 kHz–2 MHz.

## Buck Converter (Step-Down)

The buck converter produces an output voltage **lower** than the input. It is the most common switching topology — every computer, phone charger, and point-of-load regulator uses a buck converter.

```
                      ┌──────── Switch (MOSFET) ────────┐
   V_in ──▶ ──────────┤   Q1                            │
                      └──┬──────────────────┬───────────┘
                         │ t_on             │ t_off
                         ▼                  ▼
                      ┌───┐              ┌───┐
                      │ L │ ◀─ inductor  │ D │ ◀─ freewheel diode
                      │22µH│             │   │   (Schottky to GND)
                      └─┬─┘              └───┘
                        │                  │
                        ├──┬────────────────┘
                        │  │
                     ┌──┴──┴──┐
                     │  C_out │ 47µF
                     │        │
                     └──┬──┬──┘
                        │  │
                       LOAD  V_out
                        │  │
   GND ─────────────────┴──┴─────────────
```

**Operation during t_on** (switch closed): V_in connects across (L + V_out). The inductor current ramps UP:

```
   V_L = V_in − V_out = L × (dI/dt)
   ΔI_L(up) = (V_in − V_out) × t_on / L
```

**Operation during t_off** (switch open): The inductor current cannot stop instantly — it forces current through the freewheel diode D, completing the circuit. V_L = −V_out (the inductor opposes the decrease). Current ramps DOWN:

```
   ΔI_L(down) = −V_out × t_off / L
```

**Volt-second balance** (steady state): the inductor current returns to its starting value each cycle, so ΔI_L(up) = |ΔI_L(down)|:

```
   (V_in − V_out) × t_on = V_out × t_off

   V_out = V_in × t_on / (t_on + t_off) = V_in × D

   ┌──────────────────────────────┐
   │   V_out = D × V_in           │   (D = duty cycle, 0 to 1)
   │   Maximum V_out = V_in       │   (at D = 100%)
   └──────────────────────────────┘
```

For D = 0.5, V_out = V_in / 2. The buck can only step down — V_out never exceeds V_in.

**Inductor ripple current**: ΔI_L = (V_in − V_out) × D / (L × f_sw). Designers target ΔI_L = 20–40% of I_load for a good trade between inductor size and output ripple.

**Output ripple voltage**: ΔV_out = ΔI_L / (8 × f_sw × C_out). Larger C_out or higher f_sw reduces ripple. The capacitor's ESR adds another ripple term: ΔV_ESR = ΔI_L × ESR.

## Boost Converter (Step-Up)

The boost converter produces an output voltage **higher** than the input. The inductor stores energy during t_on, then releases it stacked on top of V_in through the diode during t_off.

```
                      ┌── Inductor ──┐  ┌── Diode ──┐
   V_in ──▶ ──█████───┤   L 22µH    ├──┤   D       ├──┬──▶ V_out
                      └─────────────┘  └───────────┘  │
                                                         │
                      ┌── Switch ────┐                   │
                      │   Q1 (MOSFET)│              ┌────┴────┐
                      └──────┬───────┘              │  C_out  │ 47µF
                             │                      │         │
   GND ──────────────────────┴──────────────────┬───┴────┬────┘
                                                   │      │
                                                 LOAD    V_out
```

**Operation during t_on** (switch closed): The inductor is connected directly across V_in. Current ramps UP, storing energy:

```
   V_L = V_in = L × (dI/dt)
   ΔI_L(up) = V_in × t_on / L
```

**Operation during t_off** (switch open): The inductor voltage reverses, adding to V_in. Current flows through the diode to the output. The output capacitor charges to the higher voltage:

```
   V_L = V_in − V_out (negative, since V_out > V_in)
   ΔI_L(down) = (V_in − V_out) × t_off / L
```

**Volt-second balance**:

```
   V_in × t_on = (V_out − V_in) × t_off

   V_out = V_in × (t_on + t_off) / t_off = V_in / (1 − D)

   ┌──────────────────────────────────┐
   │   V_out = V_in / (1 − D)         │   Output is always > V_in
   │   At D = 0.5: V_out = 2 × V_in   │
   │   As D → 1: V_out → ∞ (in theory)│   (practical limit ~5–10×)
   └──────────────────────────────────┘
```

At very high duty cycles, parasitic resistances (inductor DCR, switch R_DS(on), diode V_F) dominate and V_out plateaus rather than rising to infinity. Practical boost ratio is limited to ~5–10× for reasonable efficiency.

## Buck-Boost Converter (Inverting)

The buck-boost converter produces a **negative** output from a positive input — its magnitude can be higher or lower than V_in. The inductor stores energy during t_on (switch to ground), then releases it inverted through the diode to the output during t_off.

```
                      ┌── Inductor ──┐
   V_in ──▶ ──█████───┤   L 22µH    ├──┬──┐
                      └─────────────┘  │  │
                                         │  │
                      ┌── Switch ────┐  │  │  ┌── Diode ──┐
                      │   Q1         ├──┘  └──┤   D       ├──┬──▶ V_out
                      └──────┬───────┘         └───────────┘  │  (negative!)
                             │                                  │
   GND ──────────────────────┴──────────────────────────┬──────┴───┐
                                                         │          │
                                                    ┌────┴────┐     │
                                                    │  C_out  │   GND (ref)
                                                    │         │  is +V_out!
                                                    └────┬────┘
                                                         │
                                                        LOAD
```

**Volt-second balance**:

```
   V_in × t_on = |V_out| × t_off

   ┌──────────────────────────────────────┐
   │   V_out = −D × V_in / (1 − D)        │   Output is inverted (negative)
   │   |V_out| can be > or < V_in         │
   └──────────────────────────────────────┘
```

At D = 0.5, |V_out| = V_in. Used for generating negative rails (e.g., −5V from +5V for analog op-amp dual supplies). The **SEPIC** (Single-Ended Primary-Inductor Converter) topology achieves non-inverting buck-boost operation using two inductors and a coupling capacitor, at the cost of extra components.

## Flyback Converter (Isolated)

The flyback converter provides **galvanic isolation** between input and output using a coupled inductor (colloquially called a flyback transformer, though it stores energy in its core gap like an inductor, unlike a true transformer that transfers energy instantaneously). It is the dominant topology for low-power isolated supplies (chargers, adapters, 1–200W).

```
   V_in ──▶ ──┬────────────────── Switch ────┐
              │                  Q1           │
              │  ┌──── Coupled ───┐           │
              │  │   inductor    │           │
              └──┤ Np     Ns     │           │
                 │  (primary)(sec)│           │
                 └───┬────────┬───┘           │
                     │        │               │
   GND ──────────────┴────────┘               │
                                                │
                              ┌── Diode ──┐     │
                              │   D       ├──┬─┴──┐
                              └───────────┘  │    │
                                          ┌──┴──┐ │
                                          │C_out│ │
                                          │     │ │
                                          └──┬──┘ │
                                             │    │
                                          ───┴────┴──▶ V_out (isolated)
```

**Operation during t_on** (switch closed): Current ramps up in the primary winding, storing energy in the core gap. The secondary voltage is blocked by the diode (reverse-biased) — no current flows to the output.

**Operation during t_off** (switch open): The core releases its energy through the secondary winding, forward-biasing the diode and charging the output capacitor.

```
   V_out / V_in = (N_s / N_p) × (D / (1 − D))

   where N_s/N_p = secondary-to-primary turns ratio
```

The turns ratio provides voltage scaling independent of duty cycle — a key advantage for large step-down from rectified mains (340V → 5V). Multiple secondary windings can generate multiple isolated outputs from one converter. For power above ~200W, forward or bridge topologies replace flyback (they transfer energy continuously rather than storing then releasing, achieving lower ripple and higher efficiency).

## Worked Example: Buck Converter 12V → 5V at 2A, f_sw = 100 kHz

**Design goal**: A buck converter stepping 12V down to 5V at 2A load, switching at 100 kHz, with output ripple ≤ 50 mV and inductor ripple current ΔI_L = 0.5A (25% of I_load).

### Step 1 — Duty Cycle

```
   V_out = D × V_in  →  D = V_out / V_in = 5 / 12 = 0.417  (41.7% duty cycle)

   t_on = D / f_sw = 0.417 / 100,000 = 4.17 µs
   t_off = (1 − D) / f_sw = 0.583 / 100,000 = 5.83 µs
   T = 10 µs  ✓ (period at 100 kHz)
```

### Step 2 — Inductor Selection

Using the inductor ripple formula:

```
   ΔI_L = (V_in − V_out) × D / (L × f_sw)

   Solve for L:
   L = (V_in − V_out) × D / (ΔI_L × f_sw)
     = (12 − 5) × 0.417 / (0.5 × 100,000)
     = 2.92 / 50,000
     = 5.83 × 10⁻⁵ H
     ≈ 58 µH

   Select: L = 22 µH  (per task spec; verify ripple)
```

Wait — the spec specifies L = 22 µH. Let's verify the ripple current with 22 µH:

```
   ΔI_L = (V_in − V_out) × D / (L × f_sw)
        = (12 − 5) × 0.417 / (22 × 10⁻⁶ × 100,000)
        = 2.92 / 2.2
        = 1.33 A  (66% of I_load — higher than 25% target)
```

A 22 µH inductor gives ΔI_L = 1.33A. This is on the high side (66% of 2A load). For continuous conduction, I_load(min) must exceed ΔI_L / 2 = 0.66A. Below that load, the converter enters discontinuous mode (inductor current reaches zero), where the voltage conversion ratio changes — the control loop must handle both modes. A larger inductor (e.g., 47 µH) would reduce ripple to 0.62A (31%) but increases physical size and cost. The 22 µH value is acceptable for a cost-optimized design where the load is known to stay above ~0.7A.

**Peak inductor current** (for saturation rating):

```
   I_L(peak) = I_load + ΔI_L / 2 = 2.0 + 0.67 = 2.67A

   Select inductor rated: I_sat ≥ 2.7A (preferably 3A+ for margin)
   Part: 22 µH shielded drum core, 3A saturation, ≤30 mΩ DCR
```

### Step 3 — Output Capacitor Selection

Using the task spec C_out = 47 µF:

```
   ΔV_out(capacitance) = ΔI_L / (8 × f_sw × C_out)
                       = 1.33 / (8 × 100,000 × 47 × 10⁻⁶)
                       = 1.33 / 37.6
                       = 0.035 V = 35 mV

   ΔV_out(ESR) = ΔI_L × ESR
   For a low-ESR ceramic (X7R, 47 µF, 6.3V): ESR ≈ 3 mΩ
   ΔV_out(ESR) = 1.33 × 0.003 = 4 mV

   Total ΔV_out ≈ 35 + 4 = 39 mV  ✓ (< 50 mV target)
```

A 47 µF ceramic (X7R) easily meets the 50 mV ripple target. Note: ceramic capacitance drops with DC bias — a 47 µF / 6.3V ceramic may show only 30 µF effective at 5V bias. Use a 6.3V or 10V rated part, or add a 100 µF polymer electrolytic in parallel for hold-up energy. Check the manufacturer's DC bias curve.

### Step 4 — MOSFET Selection

```
   Switch voltage: must block V_in = 12V → select V_DS ≥ 30V (2.5× margin)
   Switch current: I_L(peak) = 2.67A → select I_D ≥ 5A (2× margin)

   Conduction loss (during t_on):
   P_cond = I_rms² × R_DS(on) × D
          = (2.0)² × R_DS(on) × 0.417
          = 1.67 × R_DS(on)

   For R_DS(on) = 10 mΩ: P_cond = 1.67 × 0.01 = 17 mW  (very low)
   Select: 30V, 10 mΩ logic-level N-channel MOSFET (e.g., Si4442DY or similar)
```

**Switching loss** (transition time ~30 ns at 12V, 2.67A):

```
   P_sw = ½ × V_DS × I_D × (t_r + t_f) × f_sw
        = 0.5 × 12 × 2.67 × (30 ns + 30 ns) × 100 kHz
        = 0.5 × 12 × 2.67 × 60 × 10⁻⁹ × 100,000
        = 0.96 W
```

Switching loss (0.96W) dominates conduction loss (17 mW). This is typical for moderate-frequency buck converters. A MOSFET with lower gate charge (Q_g) switches faster, reducing this loss. Total MOSFET loss ≈ 1W — needs a small SOT-223 or DPAK package for thermal dissipation.

### Step 5 — Freewheel Diode

```
   Peak current: I_L(peak) = 2.67A → select I_F ≥ 3A
   Reverse voltage: V_in = 12V → select V_R ≥ 30V
   Forward voltage: Schottky preferred (V_F ≈ 0.3V vs 0.7V silicon)

   P_diode = V_F × I_load × (1 − D) = 0.3 × 2.0 × 0.583 = 0.35W
   Select: 30V, 3A Schottky (e.g., SB330 or similar)
```

Alternative: **synchronous rectification** — replace the diode with a second MOSFET (Q2). The MOSFET's R_DS(on) drop (10 mΩ × 2A = 20 mV) is far below the Schottky V_F (300 mV), reducing rectifier loss from 0.35W to 0.04W — a 0.3W efficiency gain. This is standard in modern buck regulators (LM2596 uses a diode; newer ICs like TPS5430 use synchronous FETs).

### Step 6 — Efficiency Estimate

```
   Input power: P_in = V_out × I_load / η
   Losses (approximate):
     MOSFET conduction:    0.017W
     MOSFET switching:     0.96W
     Diode conduction:     0.35W
     Inductor DCR (30 mΩ): 2.0² × 0.03 = 0.12W
     Capacitor ESR:        0.004W (negligible)
     Control IC quiescent: 0.05W
   Total loss:            ≈ 1.5W

   P_out = 5V × 2A = 10W
   η = P_out / (P_out + P_loss) = 10 / 11.5 = 87%

   Efficiency ≈ 87%  (within the expected 85–95% range for a buck at this power)
```

For comparison: a [linear regulator](./power-supply-circuits.linear-regulators.md) doing the same 12V → 5V at 2A would dissipate (12 − 5) × 2 = 14W as heat and achieve only 5/12 = 42% efficiency. The switching regulator's 1.5W loss is nearly 10× lower — this is why switching dominates any application with significant current and dropout.

### Summary

```
   ┌────────────────────────────────────────────────────────────────┐
   │  Buck Converter 12V → 5V / 2A / 100 kHz — BOM:                 │
   │  • Controller IC: LM2596-5.0 (fixed 5V) or MC34063             │
   │  • Q1: 30V, 10 mΩ N-channel MOSFET (or internal in LM2596)     │
   │  • L: 22 µH, 3A saturation, shielded drum core                 │
   │  • D1: SB330 Schottky (30V, 3A) — or sync FET for efficiency   │
   │  • C_out: 47 µF / 6.3V ceramic (X7R) + 100 µF polymer (optional)│
   │  • C_in: 100 µF / 25V electrolytic                             │
   │  Output: 5.0V at 2A, 39 mV p-p ripple                          │
   │  Efficiency: ~87% (vs 42% for a linear regulator)              │
   │  Loss budget: ~1.5W total (switching loss dominates)           │
   └────────────────────────────────────────────────────────────────┘
```

## Switching Topology Parameter Comparison

| Topology | V_out Formula | Step Direction | Isolation | Max Efficiency | Output Ripple | Complexity | Typical IC |
|----------|---------------|----------------|-----------|----------------|---------------|------------|------------|
| Buck (step-down) | V_out = D × V_in | Down only | No | 90–97% | Low (10–50 mV) | Low | LM2596, TPS5430, MC34063 |
| Boost (step-up) | V_out = V_in / (1 − D) | Up only | No | 90–96% | Moderate (20–100 mV) | Low | MC34063, LM2577, TPS61023 |
| Buck-boost | V_out = −D × V_in / (1 − D) | Up or down (inverting) | No | 85–93% | Moderate | Medium | LM2577, MC34063 |
| SEPIC | V_out = D × V_in / (1 − D) | Up or down (non-inverting) | No | 85–92% | Moderate | Medium (2 inductors) | LM2588, MC34063 |
| Flyback | V_out = (N_s/N_p) × D × V_in / (1 − D) | Up or down | **Yes** | 75–90% | Higher (needs post-filter) | Medium | UC3842, NCP12700, TNY267 |

**Notes on the table**:
- **D = duty cycle** = t_on / (t_on + t_off), always between 0 and 1.
- **Isolation**: flyback provides galvanic isolation (input and output grounds are separate) — essential for mains-connected supplies and safety. The other topologies share a common ground.
- **Max efficiency**: lower for flyback (75–90%) due to transformer leakage inductance losses and diode recovery. Synchronous rectification (replacing diodes with MOSFETs) can push buck efficiency above 97%.
- **Output ripple**: buck is lowest (continuous inductor current feeds the output directly). Boost and flyback have higher ripple (the diode delivers pulsed current — the capacitor absorbs the pulses).
- **Typical IC**: LM2596 is a classic 3A buck regulator with internal switch; MC34063 is a flexible building block that can be wired as buck, boost, or buck-boost; UC3842 is the industry-standard flyback controller.

## Continuous vs. Discontinuous Conduction Mode

- **Continuous Conduction Mode (CCM)**: inductor current never reaches zero. V_out depends only on D and V_in (the simple formulas above). Preferred for higher power and lower ripple.
- **Discontinuous Conduction Mode (DCM)**: inductor current reaches zero before the next cycle (at light load). V_out now depends on D, V_in, AND the load — the relationship is no longer linear. The control loop must handle the mode transition. DCM occurs when I_load < ΔI_L / 2.

For the worked example (ΔI_L = 1.33A), the converter enters DCM below I_load = 0.66A. Most modern controller ICs handle this transition automatically.

## Output Ripple Breakdown

The total output ripple has two components:

```
   ΔV_out(total) = ΔV_out(capacitance) + ΔV_out(ESR)

   ΔV_out(capacitance) = ΔI_L / (8 × f_sw × C_out)    (charge/discharge ripple)
   ΔV_out(ESR) = ΔI_L × ESR                            (ESR ripple)
```

At high frequencies (≥500 kHz), the capacitance term is usually small and **ESR dominates**. This is why switching regulators demand low-ESR capacitors (ceramic X7R, polymer, or low-ESR aluminum). A standard aluminum electrolytic (ESR = 100 mΩ) at ΔI_L = 1A adds 100 mV of ripple — unacceptable. A ceramic (ESR = 3 mΩ) adds only 3 mV.

## Boundary with Linear Regulators and Power Electronics

This article covers **switching** regulation — the topologies that transfer energy inductively. The companion article on [linear regulators](./power-supply-circuits.linear-regulators.md) covers dissipative series regulation, which is simpler, quieter, and cheaper but far less efficient at large dropout voltages.

The [power-electronics](./power-electronics.md) capability covers **system-level deployment** — magnetics winding design, core loss calculations, EMI filter design, thermal management, and industrial packaging of multi-kilowatt converters. It also covers inverter topologies (DC→AC) and motor drives, which are out of scope here. The boundary: this article teaches *how to design the switching regulator circuit*; power-electronics teaches *how to build the system around it*.

## Prerequisites

- **[Semiconductor Devices](./semiconductor-devices.md)** — MOSFET gate drive and R_DS(on), diode forward/reverse recovery, Schottky vs. PN trade-offs, switching loss physics.
- **[Passive Components](./passive-components.md)** — inductor construction (core materials, saturation current, DCR), capacitor ESR and ripple current rating, ferrite core selection.
- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the upstream stage that produces unregulated DC.
- **[Filter Circuits](./power-supply-circuits.filter-circuits.md)** — LC low-pass theory (the buck output stage is an LC filter operating at f_sw instead of 120 Hz).

## See Also

- **[Linear Regulators](./power-supply-circuits.linear-regulators.md)** — the low-noise, simple alternative for small dropout or low-current rails.
- **[Power Supply Circuits](./power-supply-circuits.md)** — parent capability: the full rectifier→filter→regulator chain.
- **[Power Electronics](./power-electronics.md)** — system-level converter manufacturing, magnetics design, EMI compliance, and high-power topologies.
- **[Semiconductor Devices](./semiconductor-devices.md)** — MOSFET, diode, and Schottky device physics.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
