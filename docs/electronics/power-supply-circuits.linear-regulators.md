# Linear Regulators

> **Node ID**: `electronics.power-supply-circuits.linear-regulators`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](./semiconductor-devices.md),
> [`electronics.passive-components`](./passive-components.md),
> [`electronics.power-supply-circuits.rectifier-circuits`](./power-supply-circuits.rectifier-circuits.md)
> **Enables**: None
> **Outputs**: regulated-dc-power
> **Timeline**: Years 20-40
> **Critical**: No

Linear regulation is the third and final stage of a classic DC power supply — it takes the [filtered](./power-supply-circuits.filter-circuits.md) but still-rough DC from the filter capacitor and delivers a stable, precise output voltage that does not move with line variations or load changes. This article covers the **circuit-level design pedagogy** of linear regulator topologies: the zener shunt reference, the series pass-transistor (emitter-follower) regulator, the bandgap voltage reference, and the low-dropout (LDO) regulator. We treat the transistor and zener as building blocks whose physics is covered in [semiconductor-devices](./semiconductor-devices.md); here we focus on topology, feedback, and thermal design.

The upstream stages — [rectification](./power-supply-circuits.rectifier-circuits.md) and [filtering](./power-supply-circuits.filter-circuits.md) — produce a DC level with residual ripple that still varies 5–20% under load. A linear regulator removes that variation entirely: the output is as clean as the voltage reference inside it, with ripple rejection of 40–80 dB. The price is heat — every volt dropped across the regulator becomes waste power proportional to load current. For high-current or large step-down ratios, the [switching regulator](./power-supply-circuits.switching-regulators.md) is the efficient alternative. System-level regulator manufacturing (packaging, industrial deployment) belongs to [power-electronics](./power-electronics.md).

## The Fundamental Principle

A linear regulator is a **dissipative series element** — a transistor or resistive device that sits between the raw input and the clean output, dropping whatever voltage is left over. A feedback loop continuously compares a fraction of the output against a stable voltage reference and adjusts the series element to keep the output constant:

```
   Raw DC in ─────▶ ┌──────────┐ ─────▶ Regulated out
   (V_in, rippled)  │  Series  │       (V_out, clean)
                    │  element │
                    └────┬─────┘
                         │
                    ┌────┴─────┐
                    │ Feedback │ ◀── Error amplifier ◀── V_ref
                    │ divider  │                        (zener/bandgap)
                    └──────────┘
```

Because the series element is dissipative (it burns the excess voltage as heat), efficiency is limited: η = V_out / V_in. A 5V output from a 12V input is at best 42% efficient — the other 58% becomes heat in the pass transistor. This is the defining trade-off of linear regulation: **simplicity, low noise, and fast transient response in exchange for poor efficiency at large dropout voltages**.

## Voltage References

Every linear regulator is only as accurate as its voltage reference. Two reference types dominate.

### Zener Diode Reference

A zener diode operated in reverse breakdown maintains an approximately constant voltage across a wide current range. The zener voltage V_Z is set by doping levels during manufacture — common values are 3.3V, 5.1V, 5.6V, 6.2V, 12V. Above roughly 5.6V, the avalanche mechanism dominates and the temperature coefficient goes positive (+2 mV/°C); below 5.6V, true zener breakdown has a negative tempco (−2 mV/°C). The 5.6V zener sits near the crossover where these cancel, giving the lowest drift — historically the most stable single-zener reference value.

```
                 R_s (series)
   V_in ─────█████──────┬──────────────▶ V_out ≈ V_Z
                        │
                     ┌──┴──┐
                     │  Z  │  zener (reverse-biased)
                     │     │  V_Z = 5.1 V
                     └──┬──┘
                        │
   GND ─────────────────┴──────────────▶ 0V
```

The series resistor R_s sets the zener operating current. It must supply both the zener bias current (to keep it in breakdown) and the load current:

```
   R_s = (V_in − V_Z) / (I_Z + I_load)

   where I_Z = zener bias current (typically 5–20 mA for good regulation)
```

**Zener dynamic resistance** R_z (typically 5–50 Ω for a 5.1V zener) causes the output to sag slightly under load: ΔV_out = ΔI_load × R_z. This is why a bare zener is a reference, not a regulator — it works for milliamperes but cannot supply significant load current without help.

### Bandgap Reference

The bandgap reference (Widlar, 1971) generates a temperature-stable ~1.2V (the silicon bandgap voltage extrapolated to 0K) by summing two quantities with opposite temperature coefficients: a base-emitter voltage V_BE (tempco −2 mV/°C) and a thermal-voltage-derived term ΔV_BE scaled up (tempco +2 mV/°C). When they cancel, the output is nearly flat over temperature:

```
   V_ref = V_BE + K × ΔV_BE  ≈  1.2V  (temperature-stable)

   where ΔV_BE = V_T × ln(N)  (difference of two V_BE at different currents)
         V_T = kT/q ≈ 25.85 mV at 300K (thermal voltage)
```

Bandgap references dominate modern IC regulators (7805, LM317, LT3045) because they need no zener (which requires a high breakdown voltage and large area). They achieve 10–50 ppm/°C drift in precision designs. The [semiconductor-devices](./semiconductor-devices.md) article covers the BJT V_BE physics; here we use the result: a stable ~1.2V that the error amplifier scales to any desired output.

## Zener Shunt Regulator

The simplest complete regulator: the zener reference IS the regulator. The series resistor drops the excess voltage; the zener clamps the output. Load current changes are absorbed by the zener (less load current = more zener current, keeping R_s drop roughly constant).

```
                 R_s
   V_in ─────█████──────┬──────────────▶ V_out = V_Z
                        │                 (for I_load << I_Z)
   (12V)            ┌───┴───┐          ┌──┴──┐
                    │       │          │  R  │
                    │ Zener │          │ LOAD│
                    │ 5.1V  │          └──┬──┘
                    │       │             │
                    └───┬───┘             │
                        │                 │
   GND ─────────────────┴─────────────────┘
```

**Design constraint**: the zener must always remain in breakdown. Worst case is at minimum V_in and maximum I_load:

```
   I_Z(min) = (V_in(min) − V_Z) / R_s − I_load(max)  >  I_Z(knee)

   I_Z(knee) ≈ 0.25 mA (minimum current to stay in breakdown)
```

**Limitation**: efficiency is poor and the zener dissipates (V_in − V_Z) × I_Z continuously even at zero load. Practical only for currents below ~50 mA (reference supplies, bias rails). For higher currents, add a pass transistor.

## Series Pass Transistor (Emitter Follower)

To deliver more current than a zener alone can handle, add an NPN transistor as an emitter follower. The zener sets the base voltage; the emitter follows at V_base − V_BE (≈ 0.7V). The transistor provides current gain (β), so the zener only supplies base current (I_load / β), while the transistor carries the full load current.

```
                 R_s
   V_in ─────█████──────┬──────────┬─────▶ V_out = V_Z − V_BE
                        │          │       (≈ V_Z − 0.7V)
                        ▼ B    ┌───┴───┐
                     ┌─────┐   │       │
                     │NPN  │   │  R    │
                     │pass │   │ LOAD  │
                     │Q1   │   │       │
                     └──┬──┘   └───┬───┘
                        │ E        │
   GND ─────────────────┴──────────┘
```

**Current gain**: the zener bias current now only needs to supply I_load / β. For β = 100 and I_load = 100 mA, the zener supplies only 1 mA — easy for any zener. The transistor dissipates (V_in − V_out) × I_load, so it needs heatsinking for currents above ~100 mA.

**Load regulation**: V_out = V_Z − V_BE. Since V_BE drops ~60 mV per decade of collector current, a 100:1 load change shifts V_out by ~120 mV. Better than a bare zener, but not precision. Adding a feedback error amplifier (below) eliminates this.

**Dropout voltage**: the regulator needs V_in ≥ V_out + V_BE + V_Rs-drop ≈ V_out + 2V minimum. This is the classic "2V dropout" of standard linear regulators like the 7805. An LDO (below) reduces this to <0.5V.

## Low-Dropout (LDO) Regulator

An LDO replaces the NPN emitter follower with a PNP transistor (or P-channel MOSFET) in common-emitter (common-source) configuration. This allows the regulator to operate with V_in only slightly above V_out — the dropout voltage is just V_CE(sat) of the PNP (≈ 0.1–0.5V) instead of V_BE + overhead.

```
                                          Error amplifier
                                       ┌──────────────────┐
   V_in ───────┬────────────┐          │                  │
               │            │          │  V_ref ─┐        │
               ▼ E     ┌────┴────┐     │         │        │
            ┌─────┐    │         │     │      ┌──┴──┐     │
            │ PNP │    │ R1      │─────┼──────┤  −   ├─────┼──▶ Drive
            │pass │    │ (top)   │     │      │     │     │     PNP base
            │Q1   │    └────┬────┘     │      │  +  │     │
            └──┬──┘         │          │      └──┬──┘     │
               │ C     ┌────┴────┐     │         │        │
   V_out ◀─────┴───────┤ R2      │─────┘         │
                        │ (bot)   │          feedback
                        └────┬────┘          fraction
                             │
   GND ──────────────────────┴────────────────────
```

The feedback divider (R1, R2) sets the output voltage:

```
   V_out = V_ref × (1 + R1/R2)
```

Because the PNP pass element is in common-emitter mode, it provides voltage gain — which makes the LDO feedback loop conditionally unstable. LDOs require a specific output capacitor ESR range (typically 0.1–5 Ω) for stability: too low ESR and the loop oscillates; too high ESR and transient response degrades. This ESR window is the most important design constraint in LDO application — always consult the datasheet's capacitor stability chart.

**Dropout voltage** definition: the minimum V_in − V_out where regulation is still maintained. Below dropout, the output tracks V_in minus the dropout and is no longer regulated. A modern LDO like the LT3045 achieves 200 mV dropout at 500 mA.

## Thermal Design

Linear regulators are dissipative — the pass transistor burns P_diss = (V_in − V_out) × I_load as heat. This heat must flow from the silicon junction to the ambient air through a chain of thermal resistances. If the junction exceeds its maximum temperature (typically 150°C for silicon), the device is destroyed.

### Power Dissipation

```
   P_diss = (V_in − V_out) × I_load + V_q × I_q

   where:
     V_in  = input voltage (worst case: maximum line voltage)
     V_out = regulated output voltage
     I_load = load current (worst case: maximum load)
     V_q   = quiescent/ground-pin current (typically 5–10 mA; usually negligible)
```

The first term dominates. Example: a 7805 dropping 12V to 5V at 1A dissipates (12 − 5) × 1 = 7W. At 3A load, that rises to 21W — the regulator needs a substantial heatsink.

### Thermal Resistance Chain

Heat flows through a series of thermal resistances (analogous to electrical resistance; temperature is voltage, power is current):

```
   Junction ──θJC──▶ Case ──θCS──▶ Heatsink ──θSA──▶ Ambient

   θJA(total) = θJC + θCS + θSA

   T_junction = T_ambient + P_diss × θJA(total)

   θJC  = junction-to-case thermal resistance (set by package; e.g. TO-220: 4 °C/W)
   θCS  = case-to-sink (thermal grease/pad; typically 0.5–1.0 °C/W)
   θSA  = sink-to-ambient (set by heatsink size; 0.5–50 °C/W)
```

**Design rule**: T_junction must stay below T_j(max) (150°C for most silicon, 125°C for some). Design for T_ambient(max) = 50°C (inside an enclosure) to leave margin:

```
   θSA(max) = (T_j(max) − T_ambient) / P_diss − θJC − θCS

   Example: 7W dissipation, TO-220 (θJC = 4 °C/W), grease (θCS = 0.5 °C/W):
   θSA(max) = (150 − 50) / 7 − 4 − 0.5 = 14.3 − 4.5 = 9.8 °C/W
```

Select a heatsink with θSA ≤ 9.8 °C/W. A small clip-on TO-220 heatsink (e.g., 10 °C/W) is marginal; a moderate finned heatsink (5 °C/W) with the tab bolted down provides comfortable margin. For P_diss > 10W, forced air (a fan) is usually required.

### Heatsink Selection Guide

| θSA (°C/W) | Heatsink Type | Typical Power (natural convection) | Example |
|-------------|---------------|-----------------------------------|---------|
| 50–80 | TO-220 tab only (no sink) | < 1.5W | — |
| 20–40 | Small clip-on fin | 1.5–3W | Avid 5073 |
| 10–20 | Medium vertical fin | 3–7W | Avid 5300 |
| 3–8 | Large extruded fin | 7–20W | Wakefield 641 |
| 1–3 | Large + forced air (fan) | 20–60W | Large extruded + 40 mm fan |
| < 1 | Liquid / heat pipe | > 60W | Cold plate |

### Thermal Shutdown

Most IC regulators (7805, LM317, LT3045) include internal thermal shutdown that disables the pass transistor when T_junction reaches 150–170°C. This is a safety net, not a design strategy — repeated thermal cycling degrades the die and solder joints. Design for T_junction ≤ 125°C under worst-case conditions.

## Worked Example: 5V Regulator from 12V (Zener + NPN Follower, 100 mA Load)

**Design goal**: A regulated 5V output at 100 mA load from a 12V unregulated input, using a zener reference and NPN emitter-follower pass transistor.

### Step 1 — Choose the Zener

Select a 5.6V zener (e.g., 1N5232B). Why 5.6V? The emitter follower drops V_BE ≈ 0.6–0.7V, giving V_out = V_Z − V_BE = 5.6 − 0.6 = 5.0V. The 5.6V zener also has near-zero temperature coefficient (crossover point), giving good stability.

### Step 2 — Calculate the Series Resistor R_s

The zener must be biased above its knee current (I_Z ≥ 1 mA) at worst case (min V_in, max load). The pass transistor needs base current I_B = I_load / β. Assume β = 50 (conservative for a power transistor at 100 mA):

```
   I_B = I_load / β = 100 mA / 50 = 2 mA

   R_s must supply I_B + I_Z(min):
   R_s(max) = (V_in(min) − V_Z) / (I_B + I_Z(min))
            = (12 − 5.6) / (2 mA + 1 mA)
            = 6.4 / 0.003 = 2133 Ω

   Select: 1.8 kΩ (standard value, gives margin)
```

Verify zener current at nominal V_in (12V):
```
   I_Rs = (12 − 5.6) / 1800 = 3.56 mA
   I_Z = I_Rs − I_B = 3.56 − 2.0 = 1.56 mA  ✓ (above knee)
```

### Step 3 — Output Voltage

```
   V_out = V_Z − V_BE = 5.6 − 0.6 = 5.0V  ✓
```

At full load, V_BE rises slightly (to ~0.7V at 100 mA), so V_out ≈ 4.9V. This is acceptable for a simple regulator; an IC regulator with feedback holds ±2%.

### Step 4 — Power Dissipation and Heatsink

```
   P_diss(pass) = (V_in − V_out) × I_load = (12 − 5) × 0.1 = 0.7W
   P_diss(zener) = V_Z × I_Z = 5.6 × 1.56 mA = 8.7 mW (negligible)
   P_diss(R_s) = (V_in − V_Z)² / R_s = 6.4² / 1800 = 22.7 mW
```

The pass transistor dissipates 0.7W. Using a TO-92 small-signal package (θJA = 200 °C/W free air):

```
   T_j = T_ambient + P_diss × θJA = 50 + 0.7 × 200 = 190°C  ✗ (exceeds 150°C!)
```

A TO-92 cannot dissipate 0.7W without a heatsink. Switch to a TO-220 package (θJA = 62 °C/W free air, θJC = 4 °C/W):

```
   Free air: T_j = 50 + 0.7 × 62 = 93°C  ✓ (within limit, 57°C margin)
```

A TO-220 with no heatsink handles 0.7W comfortably. For loads above ~200 mA at this dropout, add a small clip-on heatsink.

### Step 5 — Ripple Rejection

The zener's dynamic resistance R_z ≈ 25 Ω at 1.5 mA. Input ripple is attenuated by the R_s / R_z divider:

```
   Ripple rejection ≈ R_z / (R_s + R_z) = 25 / (1800 + 25) = 0.014 → −37 dB

   For 1V p-p input ripple: output ripple ≈ 14 mV p-p
```

This is adequate for many loads. An IC regulator like the 7805 achieves 60–80 dB ripple rejection via its active error amplifier — far better.

### Summary

```
   ┌──────────────────────────────────────────────────────────┐
   │  5V / 100 mA zener + NPN follower regulator BOM:         │
   │  • R_s: 1.8 kΩ, ¼W resistor                              │
   │  • D1: 1N5232B zener (5.6V, ½W)                          │
   │  • Q1: TIP31C NPN (TO-220, β≥50 @ 100 mA)                │
   │  Output: 5.0V at 100 mA, ~14 mV ripple                   │
   │  Pass transistor dissipation: 0.7W (TO-220, no heatsink) │
   │  Efficiency: V_out/V_in = 5/12 = 42%                     │
   └──────────────────────────────────────────────────────────┘
```

## Linear Regulator Parameter Comparison

| Regulator Type | Dropout Voltage | PSRR (ripple rej.) | Efficiency (typical) | Noise | Quiescent Current | Typical IC |
|---------------|----------------|--------------------|-----------------------|-------|-------------------|------------|
| Zener shunt | V_in − V_Z | 20–40 dB | 20–40% | Moderate (R_z) | I_Z (5–20 mA) | 1N5232B + R |
| NPN follower | ~2V | 40–60 dB | V_out/V_in | Low | 2–5 mA | Discrete (TIP31 + zener) |
| Standard IC (7805) | 2V | 62–80 dB @ 120Hz | V_out/V_in | 40 µVrms | 5 mA | 7805, 7812, LM340 |
| Adjustable IC (LM317) | 2V | 65 dB @ 120 Hz | V_out/V_in | 0.003% | 5 mA (50 µA adj pin) | LM317, LM337 |
| Low-dropout (LDO) | 0.1–0.5V | 40–75 dB | V_out/V_in | 8–100 µVrms | 1–30 mA | LT3045, LP2950, MIC5219 |
| Precision LDO | 0.2V | 76–90 dB | V_out/V_in | 0.8 µVrms | 5–15 mA | LT3045, LT3042 |

**Notes on the table**:
- **PSRR** (Power Supply Rejection Ratio): how much input ripple is suppressed at the output. Higher is better. Falls with frequency — a 7805 rejects 120 Hz ripple by 80 dB but only ~40 dB at 100 kHz.
- **Noise**: the regulator's own internally generated noise (mostly from the reference and error amplifier). Precision LDOs like the LT3045 achieve sub-microvolt noise — essential for low-level analog (ADC references, VCO supplies).
- **Efficiency**: for all linear types, η ≈ V_out / V_in. A low dropout helps efficiency by allowing a lower V_in (closer to V_out), reducing wasted voltage.

## Capacitor Selection for Linear Regulators

| Position | Capacitor Type | Value | Purpose |
|----------|---------------|-------|---------|
| Input bypass | Ceramic (X7R) | 0.33–1 µF | High-frequency decoupling, input lead inductance |
| Input bulk | Aluminum electrolytic | 10–100 µF | Hold-up energy, low-frequency ripple |
| Output bypass | Ceramic (X7R) | 0.1–1 µF | High-frequency transient response |
| Output bulk | Aluminum / tantalum | 10–100 µF | Load transient energy storage |
| LDO output | Per datasheet (ESR-critical) | 1–22 µF | Loop stability (ESR window 0.1–5 Ω) |

**Critical for LDOs**: the output capacitor ESR MUST be within the datasheet's stability window. A ceramic capacitor (near-zero ESR) on an LDO that expects 1 Ω ESR can cause oscillation. Always check the "capacitor ESR range" graph in the datasheet. For standard regulators (7805, LM317), almost any output capacitor is stable — they are internally compensated.

## When to Use a Linear vs. Switching Regulator

| Factor | Linear | Switching |
|--------|--------|-----------|
| Noise | Ultra-low (10 µV) | Higher (10–100 mV switching ripple) |
| Efficiency (low dropout) | Excellent (if V_in ≈ V_out) | 85–95% regardless of ratio |
| Efficiency (large dropout) | Poor (V_out/V_in) | 85–95% regardless of ratio |
| Complexity | Very low (1 IC + 2 caps) | High (IC + inductor + diode + caps + layout) |
| Cost | Low ($0.10–2) | Higher ($1–10 + magnetics) |
| Size | Small (no magnetics) | Larger (inductor needed) |
| Best for | Low-noise analog, ADC refs, post-regulation | Battery devices, high current, large step-down |

A common architecture: a switching regulator does the large, efficient step-down (e.g., 24V → 5.5V at 92%), followed by an LDO for the final clean rail (5.5V → 5.0V at 91%, with 60 dB ripple rejection). The LDO's low dropout keeps efficiency high while removing the switching ripple that the switching regulator cannot.

## Boundary with Switching Regulators and Power Electronics

This article covers **linear** regulation only — dissipative series elements. The companion article on [switching regulators](./power-supply-circuits.switching-regulators.md) covers PWM-based buck, boost, and flyback topologies that achieve 85–95% efficiency by storing energy in inductors instead of burning it as heat.

The [power-electronics](./power-electronics.md) capability covers **system-level deployment** — packaging regulators into industrial equipment, multi-rail systems, thermal management for high-power assemblies, and EMC compliance. The boundary: this article teaches *how to design the regulator circuit*; power-electronics teaches *how to build the system around it*.

## Prerequisites

- **[Semiconductor Devices](./semiconductor-devices.md)** — zener diode breakdown physics, BJT V_BE and β, MOSFET threshold and R_DS(on), IC regulator internal architecture.
- **[Passive Components](./passive-components.md)** — resistor power ratings, capacitor ESR and stability, thermal interface materials.
- **[Rectifier Circuits](./power-supply-circuits.rectifier-circuits.md)** — the upstream stage that produces unregulated DC.
- **[Filter Circuits](./power-supply-circuits.filter-circuits.md)** — the ripple-reduction stage that precedes regulation.


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- **[Switching Regulators](./power-supply-circuits.switching-regulators.md)** — the high-efficiency alternative for large dropout or high current.
- **[Power Supply Circuits](./power-supply-circuits.md)** — parent capability: the full rectifier→filter→regulator chain.
- **[Power Electronics](./power-electronics.md)** — system-level regulator manufacturing and industrial deployment.
- **[Semiconductor Devices](./semiconductor-devices.md)** — zener, BJT, and MOSFET device physics.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
