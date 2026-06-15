# Amplifier Fundamentals

> **Node ID**: `electronics.analog-circuits.amplifier-fundamentals`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md), [`electronics.passive-components`](passive-components.md), [`electronics.analog-circuits.transistor-switch-circuits`](analog-circuits.transistor-switch-circuits.md), [`electronics.circuit-fundamentals.ac-analysis`](circuit-fundamentals.ac-analysis.md)
> **Enables**: None
> **Outputs**: amplifier-designs
> **Timeline**: Years 20-35
> **Critical**: No — design pedagogy layer; the underlying transistor manufacturing (semiconductor-devices) is the critical prerequisite

This article is the discrete-transistor foundation of all analog electronics: how a single BJT or MOSFET, biased into its linear (active) region, turns a tiny input signal into a larger copy at the output. It covers the three BJT configurations (common-emitter, common-collector / emitter follower, common-base) and their MOSFET counterparts (common-source, common-drain / source follower, common-gate), the DC bias networks that hold the operating point, the coupling and bypass capacitors that pass AC while blocking DC, and the hybrid-pi small-signal model that lets you compute gain, input impedance, and output impedance by hand.

**Boundary**: The physics of how a BJT or MOSFET is built, and the meaning of β / V_BE / V_th, are owned by [Semiconductor Devices](semiconductor-devices.md) — this article links, not re-derives. The use of a transistor as a saturated two-state switch is covered in [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md); this article stays in the linear active region. The AC concepts used below — reactance, impedance, coupling and bypass capacitor frequency response — are derived in [AC Circuit Analysis](circuit-fundamentals.ac-analysis.md). Operational, power, and RF amplifiers are later waves: op-amps integrate dozens of transistors onto one die (out of scope here), [Power Amplifiers](analog-circuits.power-amplifiers.md) deliver watts to a load, and RF stages add impedance matching and frequency-selective networks.

## Why Biasing Matters

A transistor is a three-terminal device whose output current is controlled by a small input quantity (base current for a BJT, gate-source voltage for a MOSFET). To *amplify* — that is, to produce an output that is a faithful, scaled-up copy of the input — two conditions must hold:

1. **The device must sit in its linear (active) region.** For a BJT that means the base-emitter junction is forward biased (~0.6-0.7 V) and the collector-emitter voltage is large enough that the collector current depends only on base current, not on V_CE. For a MOSFET it means V_GS is above threshold and V_DS is large enough that the device is in saturation (the constant-current region). If the device saturates (switch ON) or cuts off (switch OFF), the output clips and amplification stops — that is exactly what a [transistor switch](analog-circuits.transistor-switch-circuits.md) wants, and exactly what an amplifier must avoid.

2. **The operating point (Q-point) must be stable.** The quiescent collector current I_CQ and collector-emitter voltage V_CEQ set the centre about which the signal swings. β (h_FE) doubles from 25 °C to 100 °C and varies 3:1 between units of the same part number; V_BE drops 2.2 mV/°C. A naive bias circuit that works on the breadboard today will drift into clipping tomorrow. The **voltage-divider bias** below is the standard fix.

The Q-point also sets the maximum undistorted swing. For a CE amplifier running from V_CC with the collector sitting at V_CEQ, the output can swing up to within ~0.2 V of V_CC (saturation limit) and down to wherever the load line hits cutoff. The largest symmetrical swing is achieved when V_CEQ ≈ V_CC / 2.

## DC Bias Networks

### Fixed Bias (the bad example)

A single base resistor from V_CC sets I_B = (V_CC − V_BE) / R_B, and I_C = β × I_B. Simple, two resistors — but I_C tracks β directly. Since β varies 3:1 between units and 2:1 over temperature, the Q-point moves unpredictably. Never use this for production; it appears in textbooks only as a warning.

### Voltage-Divider Bias (the standard)

Two resistors R1 (top, to V_CC) and R2 (bottom, to ground) form a divider that sets a stiff base voltage. An emitter resistor R_E then closes the feedback loop: if I_C tries to rise (β up, temperature up), the emitter voltage V_E = I_E × R_E rises too, which reduces V_BE (because the base is held stiff), which reduces I_C. This is **DC negative feedback** and it is the single most important idea in biasing.

```
                    V_CC (+12 V)
                     |
                     R_C        <-- collector load; sets voltage gain and V_CEQ
                     |
                     *----+----> v_out (via coupling cap)
                     |    |
                     |    C_cb (stray, ignored at DC)
                     C    |
                  NPN Q1  |
                     |    |
                     +----* Base
                     |    |
                     E    +----+---- R1 (upper divider, to V_CC)
                     |         |
                     R_E       R2 (lower divider, to GND)
                     |         |
                    GND       GND

   R_E is bypassed by C_E at signal frequencies (see below), so AC gain
   is set by R_C alone, while DC bias stability is set by R_E + R1//R2.
```

**Stiffness rule**: the divider is "stiff" (base voltage barely loads when base current flows) when the divider current I_div = V_CC / (R1 + R2) is at least 10× the base current I_B = I_C / β. Under that rule the base voltage is approximately:

```
   V_B  ≈ V_CC × R2 / (R1 + R2)         <-- divider, base lightly loaded
   V_E  = V_B − V_BE  ≈ V_B − 0.7 V
   I_E  ≈ I_C  = V_E / R_E              <-- the Q-point collector current
   V_C  = V_CC − I_C × R_C              <-- the Q-point collector voltage
   V_CE = V_C − V_E  ≈ V_CC/2  (design target)
```

The emitter resistor makes I_C nearly independent of β: a doubling of β barely moves I_C, because the feedback through R_E cancels it. That is why every robust discrete amplifier uses voltage-divider bias.

### Emitter Bias / Self Bias

Adding a negative supply (−V_EE) and returning R_E to it makes the Q-point even stiffer and lets V_CEQ approach V_CC/2 more closely. Common in differential and RF amplifiers; rare in single-ended audio work where a single supply is the norm.

## Coupling and Bypass Capacitors

These are the three capacitor jobs that turn a DC bias network into an AC amplifier:

| Capacitor | Position | Job | Cutoff rule |
|-----------|----------|-----|-------------|
| **C_in** (coupling) | In series with the base, between signal source and base | Blocks the source's DC from disturbing the Q-point; passes the AC signal | X_C << R_in at the lowest frequency of interest |
| **C_out** (coupling) | In series with the collector, between collector and load | Blocks the collector's DC (V_CEQ) from the load; passes the amplified AC | X_C << R_load |
| **C_E** (bypass) | In parallel with R_E, from emitter to ground | Shorts R_E at signal frequencies so AC gain is set by R_C alone (R_E would otherwise divide the gain by 1 + g_m·R_E) | X_C << R_E at the lowest frequency; sets the amplifier's low-frequency roll-off |

Typical values for audio (20 Hz – 20 kHz): C_in = C_out = 1-10 μF (electrolytic), C_E = 47-470 μF (electrolytic — R_E is small, so C_E must be large). At these values the capacitors look like short circuits at mid-band (1 kHz) and open circuits at DC, which is exactly the design intent.

## The Hybrid-Pi Small-Signal Model

To compute gain and impedance we replace the transistor with a linear model valid for *small* signals (a few mV at the base — small enough that the exponential I-V curve looks linear). The hybrid-pi is the standard BJT model:

```
                B (base)
                |
                r_pi       <-- base-emitter resistance: r_pi = β / g_m
                |
       +--------+--------+
       |                 |
      v_pi              g_m·v_pi      <-- voltage-controlled current source
       |                 |               transconductance: g_m = I_CQ / V_T
       +--------+--------+
                |
                E (emitter)

   v_pi = voltage across base-emitter (the small-signal input)
   V_T  = thermal voltage ≈ 25.9 mV at 300 K
   g_m  = I_CQ / V_T  ≈ 40 × I_CQ(mA) mS   (rule of thumb)
   r_pi = β / g_m
   r_o  = V_A / I_CQ  (Early voltage output resistance; usually large, often ignored)
```

The transconductance g_m is the single number that determines gain. For a 1 mA Q-point, g_m ≈ 40 mS; for 100 μA, g_m ≈ 4 mS. This is why a higher Q-point current gives more gain at the cost of more power dissipation.

**MOSFET small-signal model** is structurally identical — replace r_pi with an open gate (infinite input resistance at DC), and use g_m = μ_n C_ox (W/L) (V_GSQ − V_th). The voltage-controlled current source g_m·v_gs is the same idea.

### Voltage Gain — Common-Emitter (CE)

With C_E bypassing R_E, the small-signal collector current g_m·v_pi flows through R_C (and the load, if any). The output voltage is the negative of that product — negative because an increase in base voltage raises collector current, which pulls the collector *down*:

```
   A_v = v_out / v_in = − g_m × R_C'        where R_C' = R_C // R_load

   For I_CQ = 1 mA (g_m = 40 mS), R_C = 4 kΩ, no load:
       A_v = −0.040 × 4000 = −160
```

The minus sign is the CE's signature: the output is **180° out of phase** with the input. Without C_E the gain becomes A_v = −g_m·R_C / (1 + g_m·R_E) — much smaller but far more stable and predictable, because it depends only on resistor ratios. That "degenerated" form is the basis of the op-amp differential input.

### Input Impedance

The base of a CE stage looks like r_pi in parallel with the bias divider:

```
   Z_in (base)  = r_pi ( = β / g_m )
   Z_in (stage) = r_pi // R1 // R2
```

For β = 200, g_m = 40 mS: r_pi = 5 kΩ. With R1 = 47 kΩ, R2 = 10 kΩ, the stage Z_in ≈ 5 kΩ // 47 kΩ // 10 kΩ ≈ 3.1 kΩ. This is the load the *previous* stage sees; if you cascade two CE stages, the second stage's Z_in loads the first stage's R_C and reduces its gain. A **CC (emitter follower)** stage is the standard fix: it has Z_in ~ β × R_E, far higher, and Z_out ~ 1/g_m, far lower — it isolates stages from each other.

### Output Impedance

The collector of a CE stage looks like R_C (the transistor's own output resistance r_o is usually much larger):

```
   Z_out (CE) ≈ R_C
```

For a CC stage it is far lower: Z_out ≈ 1/g_m ≈ 25 Ω at I_CQ = 1 mA. That is why emitter followers drive low-impedance loads (coax, speakers via a power stage, long cables) without losing all their gain.

## The Three BJT Configurations

The configuration is named after the terminal that is **AC-grounded** (common to input and output):

### Common-Emitter (CE) — the voltage workhorse

Emitter AC-grounded (via C_E), input at base, output at collector. High voltage gain (A_v = −g_m·R_C), moderate Z_in (~kΩ), moderate Z_out (~R_C), 180° phase inversion. This is where almost all voltage gain is made in a multistage amplifier.

```
                V_CC
                 |
                 R_C
                 |
   v_in --C_in--+----+---> v_out (via C_out)
                 |    |
                Base  |
                 |    |
                 NPN  |
                 |    |
                 +----+-- R_E -- GND
                 |    |
                 |   C_E (bypasses R_E at AC)
                GND  GND

   A_v ≈ −g_m × R_C  (with C_E), or −R_C/R_E (without, "emitter degeneration")
   Z_in = r_pi // R1 // R2
   Z_out ≈ R_C
   Phase: 180° inversion
```

### Common-Collector (CC) — the emitter follower, an impedance transformer

Collector AC-grounded (at V_CC, which is AC ground), input at base, output at emitter. Voltage gain ≈ +1 (slightly less — there is no inversion, hence "follower"), high Z_in (β × R_E), low Z_out (1/g_m). Used as a buffer: it isolates a high-impedance source from a low-impedance load without losing voltage.

```
                V_CC
                 |
                 +---- Collector (AC-grounded at V_CC)
                 |
   v_in --C_in--+---- Base
                 |
                 NPN
                 |
                 +----*----> v_out (via C_out, ~ = v_in)
                 |    |
                 R_E  (load)
                 |
                GND

   A_v ≈ +1  (unity, no inversion — "follower")
   Z_in ≈ β × R_E     (high — isolates source)
   Z_out ≈ 1/g_m      (low — drives heavy load)
   Phase: 0° (in-phase)
```

### Common-Base (CB) — the current-to-voltage converter

Base AC-grounded (via a base bypass capacitor to ground), input at emitter, output at collector. Voltage gain like CE (A_v = +g_m·R_C, no inversion), but Z_in is very low (~1/g_m, looking into the emitter) and Z_out ≈ R_C. Used in cascode combinations (to kill Miller capacitance at high frequency) and in RF front-ends where a low-Z input matches a transmission line.

```
                V_CC
                 |
                 R_C
                 |
                 +----> v_out (via C_out)
                 |
                 Collector
                 |
                 NPN
                 |
        v_in ----+ Emitter
                 |
                 Base ---- C_base ---- GND  (base AC-grounded)

   A_v ≈ +g_m × R_C
   Z_in ≈ 1/g_m  ≈ 25 Ω at 1 mA  (low!)
   Z_out ≈ R_C
   Phase: 0° (non-inverting)
```

## The MOSFET Configurations

The same three configurations exist, named by the AC-grounded terminal. Because the gate draws ~zero DC current, MOSFET amplifiers can have extremely high input impedance (limited only by the bias resistors), at the cost of slightly lower g_m than a BJT at the same current.

### Common-Source (CS) — the MOSFET voltage workhorse

Source AC-grounded, input at gate, output at drain. Voltage gain A_v = −g_m × R_D, 180° phase inversion. The most common single-transistor MOSFET amplifier. Because the gate is a capacitor, Z_in is set entirely by the bias divider and can be made arbitrarily large (e.g. 1-10 MΩ with a large R1//R2).

### Common-Drain (CD) — the source follower

Drain AC-grounded at V_DD, input at gate, output at source. Voltage gain A_v ≈ +1, high Z_in, low Z_out ≈ 1/g_m. The MOSFET buffer; widely used to drive low-Z loads from a high-Z source without loading it.

### Common-Gate (CG) — the low-Z input

Gate AC-grounded, input at source, output at drain. Like CB: low Z_in (~1/g_m), voltage gain without inversion. Used in cascodes and RF.

## Configuration Comparison Table

| Config | A_v (typical) | Z_in | Z_out | Phase | Typical application |
|--------|---------------|------|-------|-------|---------------------|
| **CE (common-emitter)** | −g_m·R_C ≈ −100 to −300 | r_pi // R_bias ≈ 1-5 kΩ | ≈ R_C ≈ 1-10 kΩ | 180° invert | Voltage gain — the workhorse of multi-stage amplifiers |
| **CC (emitter follower)** | ≈ +0.95 to +0.99 | β × R_E ≈ 50-500 kΩ | 1/g_m ≈ 10-100 Ω | 0° | Buffer / impedance matcher — isolates high-Z source from low-Z load |
| **CB (common-base)** | +g_m·R_C ≈ +100 to +300 | 1/g_m ≈ 25 Ω | ≈ R_C ≈ 1-10 kΩ | 0° | RF front-end, cascode (kills Miller capacitance), current-to-voltage |
| **CS (common-source)** | −g_m·R_D ≈ −5 to −50 | R1//R2 (gate open) ≈ 100 kΩ-10 MΩ | ≈ R_D ≈ 1-10 kΩ | 180° invert | MOSFET voltage amp; very high Z_in; sensor front-end |
| **CD (source follower)** | ≈ +0.8 to +0.95 | R1//R2 ≈ 100 kΩ-10 MΩ | 1/g_m ≈ 50-500 Ω | 0° | MOSFET buffer; electrometer / ESD-sensitive inputs |
| **CG (common-gate)** | +g_m·R_D ≈ +5 to +50 | 1/g_m ≈ 100-1000 Ω | ≈ R_D ≈ 1-10 kΩ | 0° | RF, cascode top element |

## Worked Example — Design a CE Amplifier for A_v = 20, V_CC = 12 V, I_CQ = 1 mA

**Spec**: common-emitter stage running from a 12 V supply, Q-point at I_C = 1 mA, small-signal voltage gain |A_v| = 20 into a high-impedance load. Use a small-signal NPN (2N3904), β = 200 typical.

### Step 1 — Transconductance

```
   g_m = I_CQ / V_T = 1 mA / 25.9 mV ≈ 38.7 mS  (call it 40 mS)
```

### Step 2 — Collector resistor R_C (gain sets R_C)

With C_E bypassing R_E, |A_v| = g_m × R_C. Solve for R_C:

```
   R_C = |A_v| / g_m = 20 / 0.0387 ≈ 517 Ω
```

But this ignores loading and the swing limit. Pick the next **higher** standard value to keep gain honest after load losses: **R_C = 560 Ω** (E12). Re-check gain: A_v = −0.0387 × 560 ≈ −21.7 — within 10% of target, fine.

### Step 3 — Q-point collector voltage (swing check)

```
   V_C = V_CC − I_C × R_C = 12 − (1 mA × 560 Ω) = 12 − 0.56 = 11.44 V
```

That is far too close to V_CC (only 0.56 V of headroom up, 11.4 V down). The stage will clip on positive swings immediately. **The conflict**: a high gain demanded a large R_C, which dropped almost all of V_CC, leaving no swing room. The fix is one of:

- **Accept lower gain** and use a smaller R_C: with R_C = 2.2 kΩ, V_C = 12 − 2.2 = 9.8 V, swing ≈ ±4 V, but |A_v| = 0.0387 × 2200 ≈ 85 — too much. Add emitter degeneration (next option).
- **Add emitter degeneration** (drop C_E, split R_E into R_E1 + R_E2, bypass only R_E2). Then |A_v| ≈ R_C / R_E1 — set by resistor ratio, independent of g_m. For |A_v| = 20 with R_C = 2.2 kΩ: R_E1 = 2200/20 = 110 Ω. Add R_E2 = 1 kΩ (bypassed by C_E) for DC stability. Total R_E = 1.11 kΩ for DC, 110 Ω for AC. This is the production-grade design.

We adopt the second option. Recompute the bias network around the new R_E.

### Step 4 — Emitter voltage and current (re-biased design)

```
   V_E = I_E × R_E ≈ 1 mA × 1.11 kΩ = 1.11 V       (DC)
   V_B = V_E + V_BE = 1.11 + 0.7 = 1.81 V
```

### Step 5 — Bias divider R1, R2 (10× base current rule)

Base current I_B = I_C / β = 1 mA / 200 = 5 μA. Make divider current 10× that:

```
   I_div = 10 × I_B = 50 μA
   R1 + R2 = V_CC / I_div = 12 / 50 μA = 240 kΩ
   V_B = V_CC × R2 / (R1 + R2) = 1.81 V
       → R2 = (V_B / V_CC) × (R1 + R2) = (1.81/12) × 240 kΩ = 36.2 kΩ  → 36 kΩ
       → R1 = 240 − 36 = 204 kΩ  → 200 kΩ
```

### Step 6 — Verify Q-point and gain

```
   V_B = 12 × 36/(200+36) = 1.83 V      V_E = 1.83 − 0.7 = 1.13 V
   I_C = V_E / R_E = 1.13 / 1.11 kΩ = 1.02 mA              ✓ (target 1 mA)
   V_C = 12 − (1.02 × 2.2) = 9.76 V
   V_CE = 9.76 − 1.13 = 8.63 V  (swings toward V_CC/2 = 6 V; OK, conservative)
   Swing room: up to 12 − 9.76 = 2.2 V (saturation), down by ~9 V (cutoff)
                → symmetrical swing ≈ ±2 V before clipping (good for line-level)
   |A_v| (mid-band, with C_E) = R_C / R_E1 = 2200 / 110 = 20.0   ✓ exact
```

### Step 7 — Coupling and bypass capacitors (audio band, 20 Hz – 20 kHz)

Stage Z_in ≈ r_pi // R1 // R2 = (200/0.0387) // 200k // 36k ≈ 5.17 kΩ // 30.4 kΩ ≈ 4.4 kΩ. Choose C_in so X_C ≤ Z_in / 10 at 20 Hz:

```
   C_in ≥ 1 / (2π × 20 × (4400/10)) ≈ 1.8 μF       → use 2.2 μF film/electrolytic
   C_E: bypasses R_E2 = 1 kΩ, X_C ≤ 100 Ω at 20 Hz → C_E ≥ 80 μF → use 100 μF
   C_out: into a 10 kΩ load, X_C ≤ 1 kΩ at 20 Hz   → C_out ≥ 8 μF → use 10 μF
```

**Final BOM**: Q1 = 2N3904, R_C = 2.2 kΩ, R_E1 = 110 Ω, R_E2 = 1 kΩ, R1 = 200 kΩ, R2 = 36 kΩ, C_in = 2.2 μF, C_out = 10 μF, C_E = 100 μF. Measured |A_v| ≈ 20, Z_in ≈ 4.4 kΩ, Z_out ≈ 2.2 kΩ, with a Q-point stable against β and temperature thanks to the emitter degeneration feedback.

## Multi-Stage Coupling

A single CE stage rarely gives enough gain. The classic two-stage audio preamp is **CE → CC**: the CE provides the voltage gain, the CC (emitter follower) drops the output impedance to drive the next cable or load without losing the gain to loading. Why not CE → CE? Because the second stage's Z_in (~4 kΩ) loads the first stage's R_C (~2.2 kΩ) and halves its gain. The CC buffer breaks that interaction.

Three coupling styles for cascading:

- **RC coupling** (capacitor + R_C): what we built above. Cheap, blocks DC between stages, but the coupling cap sets a low-frequency roll-off and R_C wastes V_CC headroom.
- **Direct coupling** (no capacitor): the next stage's base connects straight to the previous collector. No low-frequency roll-off (down to DC), but the Q-points interact — you must design the bias networks together. Used inside op-amps and other ICs where resistors are cheap and offsets can be matched.
- **Transformer coupling**: provides impedance transformation as well as DC isolation; the standard at RF and in tube-era audio. Lossy at low frequency, so the audio bass roll-off is set by the transformer magnetising inductance, not a capacitor.

## Design Checklist

- [ ] Chose the configuration by what you need: voltage gain → CE/CS; impedance buffering → CC/CD; low-Z input → CB/CG.
- [ ] Set the Q-point with voltage-divider bias; confirmed I_div ≥ 10 × I_B for stiffness.
- [ ] Placed V_CEQ near V_CC / 2 for maximum symmetrical swing; checked that gain demand did not starve the swing (the Step 3 trap).
- [ ] Used emitter degeneration (split R_E, partial bypass) when |A_v| must be a precise, stable value — gain is then set by resistor ratio, not g_m.
- [ ] Sized C_in, C_out, C_E so X_C ≤ 0.1 × (driven impedance) at the lowest frequency of interest.
- [ ] Computed Z_in and confirmed it will not load the previous stage into oblivion; added a CC buffer if it would.
- [ ] Computed power dissipation P = V_CEQ × I_CQ per device; confirmed it is within package rating, derated 1.5%/°C above 25 °C ambient.
- [ ] For high-frequency use, checked the gain-bandwidth product f_T and the Miller capacitance; considered a cascode (CE + CB stack) if Miller is killing bandwidth.


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- [Semiconductor Devices](semiconductor-devices.md) — the physics and fabrication of BJTs and MOSFETs; the origin of β, V_BE, V_th, g_m. This article links, not re-derives.
- [Passive Components](passive-components.md) — the resistors (bias network, collector load, emitter degeneration) and capacitors (coupling, bypass) that every circuit above is built from.
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — the sibling entry point; covers the saturated ON/OFF use of the same transistors. The switch deliberately does what the amplifier must avoid (leaving the active region).
- [Diode Circuits](analog-circuits.diode-circuits.md) — the other sibling; covers the first active circuits built with a single diode.
- [Analog Circuits](analog-circuits.md) — the parent capability hub.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
