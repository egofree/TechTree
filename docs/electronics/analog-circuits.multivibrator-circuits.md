# Multivibrator Circuits

> **Node ID**: `electronics.analog-circuits.multivibrator-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.transistor-switch-circuits`](analog-circuits.transistor-switch-circuits.md)
> **Outputs**: multivibrator-designs
> **Timeline**: Years 20-35
> **Critical**: No — design pedagogy layer; the underlying transistor/op-amp IC manufacturing (semiconductor-devices) and the R/C timing components (passive-components) are the critical prerequisites

A multivibrator is a two-state **regenerative** circuit: it uses positive feedback to snap cleanly between two voltage levels. The three flavors are named by how many of those levels are *stable*:

```
   ASTABLE       MONOSTABLE       BISTABLE
   (0 stable)    (1 stable)       (2 stable)
       │              │                │
       ▼              ▼                ▼
   free-running   triggered pulse   set / reset
   oscillator     (one-shot)        flip-flop
   (clock)        (timer delay)     (memory)
```

This article is the fourth rung of the [analog-circuits](analog-circuits.md) ladder — it sits above [op-amp circuits](analog-circuits.op-amp-circuits.md) (whose comparator and Schmitt-trigger sections supply the threshold theory multivibrators rely on) and is the bridge from linear amplification into free-running timing. It does **not** cover the 555 timer (that is [timer-circuits](analog-circuits.md), which integrates a bistable flip-flop and two comparators onto one chip) and does not re-teach comparator/Schmitt theory (see [op-amp-circuits](analog-circuits.op-amp-circuits.md)). We treat transistors and op-amps as catalog parts with datasheets from [semiconductor-devices](semiconductor-devices.md).

## The Common Idea: Positive Feedback

Every multivibrator hinges on the same trick — a loop with **loop gain greater than one** and **phase that adds** (positive feedback). A tiny perturbation is amplified and fed back in-phase, so the system runs away to one rail or the other in microseconds. This is the opposite of the op-amp's negative-feedback circuits, which converge; positive feedback *diverges*, and that divergence is what gives the clean, fast switching.

```
        +─────── gain stage ───────+
        │                          │
        ▼                          │
     ───┴───  × A  ────────────────┤
        ▲                          │
        │      feedback network    │
        └────────────── β ─────────+

   Loop gain = A · β  > 1   AND  feedback is in-phase (positive)
   ⇒  any input noise grows exponentially → output slams to a rail
```

The three multivibrator types differ only in *what holds the circuit in each state* — a capacitor (astable, no stable state), a trigger pulse (monostable, one stable state), or nothing at all (bistable, two stable states).

## Astable — The Free-Running Oscillator

The astable multivibrator has **no stable state**: it switches continuously between its two levels, producing a square wave with no input signal. It is the simplest electronic clock and the classic "two transistors, two capacitors, four resistors" textbook circuit.

### Discrete-Transistor Astable (Cross-Coupled)

Two BJTs, each with its collector driving the other's base through a capacitor. While one transistor is ON (saturated), its collector is low, holding the other OFF, and the coupling capacitor from the ON transistor's collector is busy discharging — pulling the OFF transistor's base down — until the timing RC crosses 0.6 V and the OFF transistor turns ON, snapping the pair into the opposite state. The snap is regenerative (positive feedback through the cross-coupling).

```
              +Vcc
               │
          ┌────┴────┐
          │         │
        R_c1       R_c2        ← collector load resistors
          │         │
   Q1  ───┤         ├───  Q2   (NPN transistors, e.g. 2N3904)
          │         │
        ──┴──     ──┴──
          │         │
          ▼         ▼
          ├────||───┤   C1, C2 cross-couple collector→opposite base
          │ C2      │   (C1 couples Q2 collector → Q1 base)
          │         │
       ──┤─  R_B1 ──┤─  R_B2   ← base bias resistors
       ──┤─       ──┤─
          │         │
          ▼         ▼
         GND       GND

   While Q1 ON (V_C1 ≈ 0), C2 charges through R_B2,
   Q2 base held low → Q2 OFF (V_C2 ≈ +Vcc).
   When C2 discharges so Q2 base reaches +0.6 V → Q2 snaps ON,
   Q1 snaps OFF. Now C1 takes its turn. The cycle repeats forever.
```

**Frequency** (symmetric design, R_B1 = R_B2 = R, C1 = C2 = C):

```
   Each half-period = the time for the coupling capacitor to
   discharge from +Vcc down to +0.6 V through R_B.  Analysis
   gives one half-period t_H = 0.69 · R · C  (the 0.69 = ln 2).

   Full period  T = 2 · t_H = 1.38 · R · C
   Frequency    f = 1 / T = 1 / (1.38 · R · C)

   Commonly written (per-half):  t_H = 0.69 R C
                  so        f ≈ 1 / (0.69 R C)  for the half-period form
```

(See the [worked example](#worked-example-transistor-astable-at-1-khz) for the arithmetic.)

**Duty cycle**: with equal R and C on both sides the output is 50% (a true square wave). Unequal R/C on the two sides gives an asymmetric duty cycle (a pulse train).

### Op-Amp Astable (Comparator + RC)

Replace the cross-coupled transistors with a single op-amp configured as a [Schmitt trigger](analog-circuits.op-amp-circuits.md) (positive feedback via a divider), and put an RC network on the inverting input. The capacitor charges and discharges between the two Schmitt thresholds; each time it crosses a threshold the output snaps, reversing the direction of capacitor charge.

```
                          R_f
              ┌──────────█████──────────┐
              │                         │
              ├───┐                     │
              │   │                     │
          ┌───┴──┐│             ┌──▶ V_out (square wave)
          │      ││             │
          │     ─┤─  C          │
          │      ││  (timing)   │
   V- ◀────      ││             │
   (RC node)     │└─────────────┴──▶├─+
          │      │                  │  \
          │      │        R_g       │   \
          ▼      ▼        ─████─    │    ├──── feedback
         GND    GND           │     │   /     to + input
                              ▼     │  /
                             GND    └─+

   Capacitor C charges through R toward V_out;
   when V_C hits the Schmitt upper threshold V_T+, output snaps LOW,
   C discharges toward the lower threshold V_T-, output snaps HIGH, ...
   ⇒ continuous square wave at f = 1/(2·R·C·ln(1+2·R_g/R_f))
```

**Frequency** (for the op-amp astable with divider ratio β = R_g/(R_g + R_f)):

```
   f = 1 / [ 2 · R · C · ln(1 + 2·β/(1−β)) ]

   For β = R_f = R_g (i.e. the symmetric Schmitt), this simplifies to
   f = 1 / (2 · R · C · ln 3) ≈ 1 / (2.2 · R · C)
```

The op-amp astable is the precision version of the discrete design: thresholds are set by resistor ratios (not V_BE drops that drift with temperature), and the only timing inaccuracy is capacitor tolerance.

## Monostable — The One-Shot

The monostable multivibrator has **exactly one stable state**. It sits there indefinitely until a trigger pulse kicks it into the *quasi-stable* state, where it stays for a fixed duration T (set by an RC time constant) before snapping back to stable on its own. It produces a single clean pulse of **predetermined width** regardless of the trigger's shape or width.

```
       trigger in                  output
   (narrow pulse)                  (fixed width T)
        │                              │
        ▼                              ▼
   ─────┐     ┌────────────────────────┐     ┌─────
        │     │                        │     │
        └─────┘                        └─────┘
        trigger                   T = 0.69 R C
        (can be short             (width set by R, C,
         and noisy)                independent of trigger)
```

**Discrete realization**: one stable state has Q1 ON (held there by R_B), Q2 OFF. A negative trigger pulse on Q1's base momentarily cuts Q1 OFF; the cross-coupling regeneratively snaps Q2 ON; the timing capacitor C then discharges through R for T = 0.69·R·C, after which Q1 turns back ON and the circuit returns to its stable state, ready for the next trigger.

**Op-amp realization**: an op-amp Schmitt trigger held in its stable state by a clamping diode, with a differentiating trigger input. The trigger pushes it past the threshold; the timing RC then ramps the input back over T = 0.69·R·C, at which point it re-crosses the threshold and snaps back.

**Applications**: debounce-free pulse generation, pulse stretching (turning a glitch into a clean logic pulse), time-delay relays, retriggerable one-shots in watchdog timers, and the "monostable mode" of the 555 timer ([timer-circuits](analog-circuits.md)).

## Bistable — The Flip-Flop

The bistable multivibrator has **two stable states**: once placed in either, it stays there indefinitely (drawing only leakage current) until a deliberate **set** or **reset** signal flips it. It is the canonical **memory element** — the ancestor of every SR latch, JK flip-flop, and static RAM cell.

```
              +Vcc
               │
          ┌────┴────┐
          │         │
        R_c1       R_c2
          │         │
   Q1  ───┤◀──||||──├───  Q2   (cross-coupled: each collector
          │    R_B   │           drives the other's base)
        ──┴──     ──┴──
          │         │
          ▼         ▼
        SET       RESET  (trigger inputs, via capacitors)
          │         │
         GND       GND

   Two stable states:  (Q1 ON,  Q2 OFF)  OR  (Q1 OFF, Q2 ON)
   A pulse on SET  forces (Q1 OFF, Q2 ON)  → stores a "1"
   A pulse on RESET forces (Q1 ON,  Q2 OFF) → stores a "0"
   With no trigger, it remembers its last state indefinitely.
```

The regeneration (each collector pulling the opposite base) is what makes the states *stable*: any small drift away from a state is opposed by the feedback. The circuit is the transistor-level SR latch; in digital logic it is built from two cross-coupled NOR or NAND gates.

## Op-Amp Multivibrators Summary

The op-amp realizations of all three types share one building block — the [Schmitt trigger](analog-circuits.op-amp-circuits.md) — and differ only in what is wired to the inverting input:

| Type | Input at V− | Behavior | Period |
|------|-------------|----------|--------|
| Astable | RC charging network | Free-runs between thresholds | 2·R·C·ln(1+2R_g/R_f) |
| Monostable | RC + clamp diode; trigger via differentiator | One pulse per trigger, width T | T = 0.69·R·C (pulse width) |
| Bistable | DC level / direct input | Stays put until SET/RESET | infinite (memory) |

The discrete-transistor versions are cheaper (two 5-cent transistors vs. one op-amp) and were historically first; the op-amp versions are more accurate (thresholds set by resistor ratios, not V_BE) and easier to design.

## Worked Example: Transistor Astable at 1 kHz

**Design goal**: A symmetric (50% duty cycle) discrete-transistor astable multivibrator oscillating at **1 kHz**, using the specified R = 10 kΩ base resistors and C = 72 nF coupling capacitors, on a +5 V supply with 2N3904 NPN transistors.

### Step 1 — Frequency formula

```
   f = 1 / (1.38 · R · C)     (symmetric: R_B1 = R_B2 = R, C1 = C2 = C)
```

### Step 2 — Plug in the values

```
   R · C = 10,000 Ω × 72 × 10^-9 F
         = 10,000 × 72 nF
         = 720 µs

   T = 1.38 × 720 µs = 994 µs
   f = 1 / T = 1 / 994 µs ≈ 1006 Hz ≈ 1.0 kHz ✓
```

The 72 nF value is chosen because 1.38 × 10 kΩ × 72 nF = 994 µs ≈ 1 ms period ⇒ 1 kHz. The closest standard value is 68 nF (giving 1.06 kHz) or 75 nF (giving 962 Hz, ~1.04 kHz); 72 nF is a 6.8 nF + 68 nF parallel combination or a 5% E12 selection.

### Step 3 — Size the collector loads

The collector resistor R_c must allow enough collector current to saturate the ON transistor at the chosen base drive. With R_B = 10 kΩ and Vcc = 5 V:

```
   Base current when ON:  I_B = (Vcc − 0.7) / R_B = 4.3 / 10k = 0.43 mA
   With forced beta = 10 (saturated switching):  I_C(sat) = 10 · I_B = 4.3 mA
   R_c = (Vcc − V_CE(sat)) / I_C(sat) = (5 − 0.2) / 4.3 mA ≈ 1.1 kΩ
   Select: 1.0 kΩ  (standard value; gives I_C ≈ 4.8 mA, slightly over-driven ✓)
```

### Step 4 — Check the recovery

After a transistor turns OFF, its collector must rise back to +Vcc through R_c in time for the next half-cycle. The collector-node time constant is R_c × (stray + junction capacitance) ≈ 1 kΩ × 10 pF ≈ 10 ns, negligible versus the 500 µs half-period. The square-wave edges are therefore clean, limited only by transistor f_T. ✓

### Step 5 — Output waveform

```
   V_C1 (Q1 collector):
        +5V ┤┌─────────┐┌─────────┐┌──────   (HIGH while Q1 OFF)
            ││         ││         ││
       +0.2V┘└─────────┘└─────────┘└──────   (LOW  while Q1 ON, saturated)
            │← 497 µs →│← 497 µs →│
            ← half-period →← half-period →

   V_C2 is the exact complement (180° phase shift).
   f ≈ 1.0 kHz, 50% duty cycle, rise/fall time < 100 ns.
```

### Summary

```
   ┌──────────────────────────────────────────────────────┐
   │  Symmetric transistor astable, f ≈ 1 kHz:            │
   │  • Q1, Q2: 2N3904 NPN (or BC547)                    │
   │  • R_c1 = R_c2 = 1.0 kΩ  (collector loads)          │
   │  • R_B1 = R_B2 = 10 kΩ  (base/timing resistors)     │
   │  • C1 = C2 = 72 nF      (timing capacitors)         │
   │  • Vcc = +5 V                                        │
   │  • T = 994 µs, f ≈ 1006 Hz, 50% duty cycle          │
   │  • Edges < 100 ns (collector recovery << half-period)│
   └──────────────────────────────────────────────────────┘
```

## Parameter and Selection Notes

| Parameter | Discrete transistor astable | Op-amp astable | 555 timer (for reference) |
|-----------|----------------------------|----------------|---------------------------|
| Typical freq. range | 1 Hz – 1 MHz | 0.1 Hz – 100 kHz | 1 Hz – 100 kHz (classic) |
| Frequency accuracy | ±10–20% (V_BE drift, R/C tol.) | ±5% (resistor ratios dominate) | ±1–5% (with stable R, C) |
| Threshold stability | poor (V_BE = 0.6 V drifts with temp) | excellent (set by R ratios) | good (1/3, 2/3 Vcc dividers) |
| Edge speed | fast (< 100 ns, regenerative) | set by op-amp slew rate | ~100 ns |
| Component count | 2 transistors, 4 R, 2 C | 1 op-amp, 3 R, 1 C | 1 IC, 2 R, 1 C |
| Cost (bootstrap context) | lowest | low | lowest if IC available |
| Best for | teaching, simple clocks | precision, low drift | general-purpose timing |

## Prerequisites

- **[Semiconductor Devices](semiconductor-devices.md)** — supplies the BJTs (2N3904, BC547) and op-amps (LM741, TL072, LM358) these circuits are built from. Design pedagogy assumes they exist as catalog parts with known datasheets (h_FE, V_CE(sat), slew rate).
- **[Passive Components](passive-components.md)** — the resistors that set collector/base current and the capacitors that set the timing period (T = 0.69·R·C).
- **[Op-Amp Circuits](analog-circuits.op-amp-circuits.md)** — the comparator and Schmitt-trigger theory that the op-amp multivibrator realizations rely on for their thresholds.

## See Also

- [Analog Circuits](analog-circuits.md) — the parent capability hub; the pedagogical ladder this article sits on.
- [Op-Amp Circuits](analog-circuits.op-amp-circuits.md) — the comparator and Schmitt-trigger sections supply the threshold theory used by the op-amp multivibrators above.
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — the saturation/cutoff and forced-beta theory the discrete-transistor multivibrators depend on.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
