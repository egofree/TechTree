# Transistor Switch Circuits

> **Node ID**: `electronics.analog-circuits.transistor-switch-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md)
> **Outputs**: transistor-switch-designs
> **Timeline**: Years 20-30
> **Critical**: No — design pedagogy layer; the underlying transistor manufacturing (semiconductor-devices) is the critical prerequisite

This is the second of the two "Basic Semiconductor Circuits" entry points (alongside [Diode Circuits](analog-circuits.diode-circuits.md)). It teaches the transistor used the way digital logic and power control use it: as a two-state **switch** — fully ON (saturated, dropping ~0.2 V) or fully OFF (leakage only). It deliberately does *not* cover the transistor as a linear amplifier (that is [amplifier-fundamentals](analog-circuits.md), a later wave) nor as a logic gate element (discrete-logic-circuits, later). The physics of how a BJT or MOSFET is built is owned by [Semiconductor Devices](semiconductor-devices.md); this article only uses the resulting datasheet parameters (h_FE, V_CE(sat), R_DS(on), V_GS(th)).

## The Switch Model

### BJT as a switch — two regions only

A BJT has three regions of operation (cutoff, active, saturation). For switching we use exactly two and avoid the middle one:

- **CUTOFF (OFF)**: V_BE < ~0.6 V. Base current zero. Collector current ≈ leakage (nA). The switch is open.
- **SATURATION (ON)**: V_BE ≈ 0.7-0.8 V, AND we drive enough base current that the collector can't keep up. V_CE collapses to V_CE(sat) ≈ 0.1-0.3 V. The switch is closed — the transistor looks like a small resistor to the load.

The trap is the **active region** between them: there the transistor *amplifies* and dissipates large power (P = V_CE × I_C). A switch must transit the active region quickly and never sit in it. We guarantee saturation by over-driving the base — the **forced beta** trick below.

### Forced beta — guaranteeing saturation

Datasheet h_FE (e.g. 100-300 for a 2N3904) is specified in the *active* region and is unreliable for guaranteeing saturation, especially at low temperatures or between units. The robust design rule: **force the transistor into saturation by supplying far more base current than h_FE would require.** Pick a forced beta `β_forced = 10` (sometimes 20 for small-signal, 5 for power Darlingtons). Then:

```
  I_B(sat) = I_C(load) / β_forced      <-- intentionally 5-20× the active-region I_B
```

This guarantees V_CE(sat) < 0.3 V regardless of unit-to-unit h_FE variation, at the cost of extra base-drive current (irrelevant for a switch).

### MOSFET as a switch — voltage-driven

A MOSFET (enhancement mode) is OFF when V_GS < V_th (gate-source below threshold, ~2-4 V) and ON when V_GS is large enough to fully enhance the channel (V_GS = 10 V for standard, 4.5 V for logic-level). When fully ON the channel looks like a small resistor R_DS(on):

```
  P(conduction) = I_D² × R_DS(on)        <-- the only loss that matters when ON
```

Because the gate is a capacitor, steady-state gate current is ~zero — the MOSFET draws power *only* during the switching transition (charging/discharging Q_g). This makes MOSFETs the default choice for high-current or high-frequency switching; BJTs win only where low-voltage (V_DS < ~5 V) conduction loss is critical and base drive is cheap.

## Base/Gate Resistor Calculation

### BJT base resistor

Given a load current I_C, a control voltage V_drive, and a chosen forced beta:

```
  R_B = (V_drive - V_BE(sat)) / I_B(sat)
      = (V_drive - 0.7) × β_forced / I_C
```

### MOSFET gate resistor

The gate resistor does *not* set the on-state (gate current is ~0). It limits the peak current when charging/discharging the gate capacitance and damps ringing:

```
  I_gate(peak) = (V_drive - V_GS) / R_gate       <-- during the transition only
  R_gate = 10-100 Ω typical (small-signal), up to 4.7-47 Ω (fast power switching)
```

## Application Circuits

### 1. LED driver (low-side NPN switch)

A microcontroller or logic pin (3.3-5 V, a few mA) cannot drive a high-current LED directly. The transistor adds current gain.

```
   +V (+5 V or +12 V)
    |
   LED
    |
   R_limit   <-- sets LED current: R = (V_supply - V_LED - V_CE(sat)) / I_LED
    |
    *------ Collector
    |
   NPN (2N3904 / PN2222)   Emitter -- GND
    |
    Base
    |
   R_base --- Control in (from MCU pin, 0/5 V)
              R_base = (V_drive - 0.7) / I_base
```

### 2. Relay / contactor driver — WITH freewheeling diode

A relay coil needs more current than a logic pin can sink, and being inductive it *must* have a freewheeling diode (see [Diode Circuits](analog-circuits.diode-circuits.md)) or the transistor is destroyed on turn-off.

```
   +12 V
    |
    )||  Relay coil  (R = 240 Ω, L = 150 mH, I = 50 mA)
    )
    *---|<|---*   D1 freewheeling diode (1N4001), cathode to +12 V
    |         |
    *---------*-- Collector
    |
   NPN (2N3904)            Emitter -- GND
    |
   Base -- R_base -- Control in (0/5 V)
```

### 3. Light-activated switch (LDR + transistor)

A light-dependent resistor (LDR / photoresistor) has low resistance in light (~1 kΩ) and high resistance in dark (~1 MΩ). Put it in a voltage divider; the transistor threshold-crosses at the chosen light level and snaps the load ON.

```
   +V (+9 V)
    |
    +-------+---- Collector --> Load --> +V
    |       |
    R1      NPN (2N3904)  Emitter -- GND
    |       |
    +--*----+ Base
       |
       *---- LDR (to GND)   <-- LDR on the BOTTOM: bright light = low R = base
                                   voltage rises = transistor ON.
       |
      GND

  Swap R1 and LDR to invert (dark-activated, below).
  R1 ≈ LDR's mid-range resistance (~10 kΩ typical) sets the trip point.
  Add a 100 kΩ pot in series with R1 to trim the threshold.
```

### 4. Dark-activated switch

Same circuit, LDR moved to the TOP of the divider: in darkness the LDR resistance is high, the base voltage rises, and the transistor turns ON.

```
   +V
    |
    +-- LDR --*---- Collector --> Load --> +V
              |
              +--*-- Base (NPN)   Emitter -- GND
              |
             R1 (to GND)   <-- R1 on the BOTTOM: darkness = high LDR = base
                               voltage rises = transistor ON.
             GND
```

## Worked Example — base resistor for a 2N3904 switching a 12 V relay

**Spec**: switch a 12 V relay coil (240 Ω, 50 mA holding current) with a 2N3904 NPN. Control signal is a 0/5 V logic output. Use forced beta = 10.

1. **Collector current** (the load): `I_C = V_supply / R_coil = 12 V / 240 Ω = 50 mA`. (Below the 2N3904's 200 mA max — OK.)

2. **Required base current** at forced beta = 10:

   `I_B = I_C / β_forced = 50 mA / 10 = 5.0 mA`

3. **Base resistor**: the logic pin drives 5 V when high; V_BE(sat) ≈ 0.7 V.

   `R_B = (V_drive - V_BE(sat)) / I_B = (5.0 - 0.7) / 5.0 mA = 4.3 / 0.005 = 860 Ω`

4. **Standard value**: choose the nearest lower E12 value to *guarantee* enough base current (going lower raises I_B, deeper saturation). **R_B = 820 Ω** (gives I_B = 5.24 mA, β_forced ≈ 9.5). 

5. **Sanity checks**:
   - Logic pin current: 5.2 mA — within a typical MCU's 20 mA per-pin limit. OK.
   - 2N3904 power dissipation ON: `P = V_CE(sat) × I_C ≈ 0.2 × 50 mA = 10 mW`. Negligible (625 mW rating).
   - Coil needs a freewheeling diode (1N4001) or V_CE spikes to hundreds of volts on release. See [Diode Circuits — freewheeling](analog-circuits.diode-circuits.md).

**Result**: R_B = 820 Ω, plus a 1N4001 across the coil (cathode to +12 V).

## Worked Example — MOSFET gate drive for a 3 A load

**Spec**: switch a 3 A resistive load from a 12 V supply using an IRF540N (standard MOSFET, V_th = 2-4 V, R_DS(on) = 0.044 Ω at V_GS = 10 V). Control is a 0/12 V signal.

1. **On-state conduction loss**: `P = I² × R_DS(on) = 3² × 0.044 = 0.40 W`. Modest — needs no heatsink at this current (the TO-220 package dissipates ~1 W in free air).
2. **Gate drive voltage**: standard IRF540N needs V_GS = 10 V for the quoted R_DS(on). A 12 V signal fully enhances it. (A 5 V signal would *not* — use a logic-level IRL540 instead.)
3. **Gate resistor**: 47 Ω series, to damp ringing and limit peak gate current during the ~50 ns transition. Steady-state gate current is zero.
4. **Freewheeling**: only needed if the load is inductive. For a resistive heater/lamp, omit.

## Parameter Table — Transistor Switch Selection

| Transistor | Type | V_CE(sat) / R_DS(on) | Max current | Drive required | Typical use |
|------------|------|----------------------|-------------|----------------|-------------|
| 2N3904 | NPN BJT (small-signal) | 0.2-0.3 V | 200 mA | I_B = I_C / 10 (forced β=10), ~5 mA at 50 mA load | LED driver, small relay, signal switch |
| PN2222 / 2N2222 | NPN BJT (general) | 0.3-1.0 V | 600-800 mA | I_B = I_C / 10 | Multi-LED, small solenoid, buzzer |
| TIP31C | NPN BJT (power) | 0.2-1.2 V | 3 A | I_B = I_C / 10 (up to 300 mA base) | Motor, large relay, heater — needs heatsink |
| TIP122 | NPN Darlington | 1.5-2.5 V | 5 A | I_B = I_C / 250 (high gain, low base drive) | High-current with weak drive (V_CE(sat) loss is the penalty) |
| 2N7000 / 2N7002 | n-channel MOSFET (small) | 1.2-5.0 Ω | 200-400 mA | V_GS = 5 V (logic-level) | Logic-level load switch, replaces small BJT |
| IRLZ44N / IRL540 | n-channel MOSFET (logic-level) | 0.028-0.1 Ω | 20-47 A | V_GS = 5 V (logic-level — note "L") | High-current load direct from 5 V MCU pin |
| IRF540N | n-channel MOSFET (standard) | 0.044 Ω | 33 A | V_GS = 10 V (needs gate driver for 5 V logic) | High-current switch with 10-12 V gate drive |
| FQA11N90 | n-channel MOSFET (high-V) | 1.1 Ω | 11 A | V_GS = 10 V | Off-line / high-voltage switching (PFC, SMPS) |

**Selection rule of thumb**: small loads (< 200 mA) → 2N3904 (cheapest). Up to ~1 A from a logic pin → IRLZ44N (logic-level MOSFET, no base resistor, zero steady drive). Above 1 A or above ~5 V gate availability → standard MOSFET (IRF540N) with a 10-12 V gate drive. Use a Darlington (TIP122) only when drive current is scarce and you can afford the ~2 V saturation loss.

## Design Checklist

- [ ] Computed load current and confirmed it is < ½ the device's max rating.
- [ ] BJT: chose forced beta (10 typical), computed I_B, sized R_B from actual V_drive.
- [ ] MOSFET: confirmed V_GS available ≥ the value quoted for R_DS(on) (logic-level part if only 5 V available).
- [ ] Confirmed ON-state power dissipation (V_CE(sat)×I_C or I_D²×R_DS(on)) and sized heatsink if > 1 W.
- [ ] For inductive loads: added a freewheeling diode (cathode to +V) — verified polarity.
- [ ] Confirmed the control source can supply I_B (BJT) or the gate-switching current (MOSFET).
- [ ] Confirmed V_supply < device's V_CEO / V_DS(max) with margin.

## See Also

- [Semiconductor Devices](semiconductor-devices.md) — how BJTs and MOSFETs are manufactured; the origin of h_FE, V_CE(sat), R_DS(on), V_th. This article links, not re-derives.
- [Passive Components](passive-components.md) — the resistors (base/gate limiters), and the relay coils / LDRs used as loads and sensors above.
- [Diode Circuits](analog-circuits.diode-circuits.md) — the sibling entry point; the freewheeling diode that protects every relay driver lives there.
- [Analog Circuits](analog-circuits.md) — the parent capability hub.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
