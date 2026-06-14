# Discrete Logic Circuits

> **Node ID**: `electronics.control-circuits.discrete-logic-circuits`
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.semiconductor-devices`](semiconductor-devices.md),
> [`electronics.passive-components`](passive-components.md),
> [`electronics.analog-circuits.transistor-switch-circuits`](analog-circuits.transistor-switch-circuits.md)
> **Outputs**: discrete-logic-designs
> **Timeline**: Years 25-45
> **Critical**: No

This article is about **how logic gates are built and used as electronic components** — how a transistor becomes an inverter, how two transistors become a NAND gate, and how the 74xx TTL and 4000 CMOS integrated-circuit families package those gates into the building blocks of every digital system. It assumes you already understand the [transistor as a switch](analog-circuits.transistor-switch-circuits.md) and the [diode](analog-circuits.diode-circuits.md) as a one-way element. It complements [Relay Logic Circuits](control-circuits.relay-logic.md), where the same AND/OR/NOT functions were built from electromechanical contacts.

> **Boundary statement.** This article covers how gates are *built* and *used* as electronic components. For Boolean algebra identities, De Morgan's laws, Karnaugh maps, Quine-McCluskey minimization, sum-of-products / product-of-sums forms, and HDL/FPGA design, see [Digital Logic](../computing/digital-logic.md) and [Logic Design](../computing/logic-design.md). Those articles teach the *mathematics* of combining gates; this one teaches the *hardware* of making a gate at all. Truth tables appear here only to confirm that a circuit does what its name claims, not as a design tool.

## Truth Tables for the Basic Gates

Every circuit below is defined by the Boolean function it computes. We list the truth tables once so we can check each transistor implementation against its specification.

| A | B | AND | NAND | OR | NOR | XOR | NOT A |
|---|---|-----|------|----|-----|-----|-------|
| 0 | 0 |  0  |  1   |  0 |  1  |  0  |   1   |
| 0 | 1 |  0  |  1   |  1 |  0  |  1  |   1   |
| 1 | 0 |  0  |  1   |  1 |  0  |  1  |   0   |
| 1 | 1 |  1  |  0   |  1 |  0  |  0  |   0   |

The two **universal gates** are NAND and NOR: any Boolean function can be built from NANDs alone, or from NORs alone. This is why every transistor-level gate family leads with NAND and NOR — they are the cheapest 2-input functions to build from bipolar transistors (NAND: two in series; NOR: two in parallel), and CMOS NAND/NOR have the most symmetric transistor sizing. AND and OR are then made by following a NAND or NOR with an inverter.

## Transistor-Level Gates (Resistor-Transistor Logic)

The earliest transistor logic used discrete bipolar junction transistors (BJTs) operated as switches — saturated (on) or cut off (off) — with resistors as the pull-up element. This is **resistor-transistor logic (RTL)**, and it is the easiest way to see *why* a transistor makes a gate.

### NOT Gate (Single-Transistor Inverter)

A single NPN transistor with a collector pull-up resistor is an inverter. When the input is LOW (below ~0.7 V), the base-emitter junction is not forward biased, the transistor is cut off, no collector current flows, and the output sits at V_CC (HIGH) because the pull-up resistor has no current to drop voltage across. When the input is HIGH, base current flows through the base resistor, the transistor saturates (collector-emitter voltage drops to V_CE(sat) ≈ 0.2 V), and the output is pulled LOW.

```
       +V_CC (5 V)
        |
        |
       R_C (1 kΩ)
        |
        +--------+-----> OUT (LOW when A HIGH, HIGH when A LOW)
        |
        C
   A --B  (NPN, e.g. 2N3904)
        E
        |
       GND
```

**Design rule.** Size R_B so the base current drives the transistor into saturation with a "forced beta" of about 10: I_B = I_C / 10. For a collector current of ~5 mA (V_CC / R_C = 5 V / 1 kΩ), the base current must be at least 0.5 mA. At V_IN = 5 V and V_BE = 0.7 V, R_B = (5 − 0.7) / 0.5 mA ≈ 8.6 kΩ → use 8.2 kΩ. This forced-beta margin guarantees saturation even with β variation across temperature and between transistors. The [transistor-switch-circuits article](analog-circuits.transistor-switch-circuits.md) derives this in full.

### NAND Gate (Two NPN in Series)

A NAND gate is two inverters' transistor paths stacked in series: both transistors must turn on (both inputs HIGH) for the output to be pulled LOW. If either input is LOW, its transistor is cut off, the series path is broken, and the output stays HIGH via the pull-up.

```
       TRANSISTOR NAND GATE (RTL)

        +V_CC (5 V)
         |
        R_C (1 kΩ)
         |
         +-----------+-----> OUT  (= NOT (A AND B))
         |
         C   (Q1)
    A --B|    2N3904
         E
         |
         C   (Q2)   [series: both must conduct to pull OUT low]
    B --B|    2N3904
         E
         |
        GND

    A=0 OR B=0  ->  one transistor cut off  ->  OUT = HIGH  (NAND=1)
    A=1 AND B=1 ->  both saturated          ->  OUT ≈ 0.2 V (NAND=0)
```

Trace the truth table: A=0, B=0 → Q1 off → OUT = 5 V (1). A=1, B=0 → Q2 off → OUT = 5 V (1). A=0, B=1 → Q1 off → OUT = 5 V (1). A=1, B=1 → both saturated → OUT ≈ 0.2 V (0). This is NAND.

### NOR Gate (Two NPN in Parallel)

A NOR gate is two transistor paths in parallel: if *either* transistor turns on (either input HIGH), it pulls the output LOW. Only when both are off (both inputs LOW) does the output stay HIGH.

```
       TRANSISTOR NOR GATE (RTL)

        +V_CC (5 V)
         |
        R_C (1 kΩ)
         |
         +-----------+-----> OUT  (= NOT (A OR B))
         |
         +-------+---+
         |       |
         C       C   (Q2)
    A --B|Q1    B|
         E       E
         |       |
         +---+---+
             |
            GND

    A=0 AND B=0 ->  both off  ->  OUT = HIGH  (NOR=1)
    A=1 OR  B=1 ->  one or both conduct ->  OUT ≈ 0.2 V  (NOR=0)
```

**Why NAND/NOR and not AND/OR.** A 2-input RTL NAND is two transistors + one resistor; an AND would need a NAND followed by an inverter (three transistors + two resistors). Because NAND and NOR are universal (any function can be made from them alone), every logic family optimizes for NAND/NOR first. AND and OR are always "NAND/NOR + inverter."

**RTL limitations.** RTL is slow (~100 ns propagation delay), has poor noise margin (the output LOW is V_CE(sat) ≈ 0.2 V but the input threshold is V_BE(sat) ≈ 0.7 V, leaving only ~0.5 V of margin), and fan-out is only 3–5 (each downstream gate loads the pull-up resistor and drags the HIGH level down). It was historically important as the first IC logic family but is obsolete for any practical design. We build it here only to understand what a gate *is*.

## Diode-Transistor Logic (DTL)

Before TTL, **diode-transistor logic** improved on RTL by using diodes to perform the AND/OR function and a single transistor inverter for gain and level restoration. A DTL NAND gate uses input diodes as a diode-AND network feeding a transistor inverter:

```
       DTL NAND GATE

    A --|>|--+    (input diodes: anode in, cathode common)
    B --|>|  |
              X---- R_B ----B  (Q1 inverter)
              |               E
             R (2 kΩ to       C-----> OUT
             V_CC, pull-up)   |
                            R_C
                             |
                            GND

   If A OR B is LOW, that diode pulls node X LOW -> Q1 OFF -> OUT HIGH (NAND=1)
   If A AND B are HIGH, both diodes reverse-bias -> X rises -> Q1 ON -> OUT LOW (NAND=0)
```

The diode AND-network is cheap, but the diode forward drops (~0.7 V each) eat into the noise margin, and the transistor still suffers saturation storage time on turn-off (~30 ns). DTL was the bridge from RTL to TTL in the early 1960s and is now historical. It matters to us only because it introduces the idea of separating the logic function (diodes) from the gain element (transistor) — the same separation TTL formalizes with the multi-emitter transistor.

## TTL (74xx Series)

**Transistor-transistor logic (TTL)**, introduced by Texas Instruments as the 7400 series in 1964, was the dominant logic family for 30 years. The genius of TTL is the **multi-emitter transistor** input: a single NPN transistor with two (or more) emitters, each acting as an input, replaces the input diode network of DTL. The multi-emitter transistor is both the logic element (it performs the AND of the inputs internally) and the driver for the output stage, in one device.

### 7400 NAND Internals

A standard 7400 NAND gate contains four transistors and several resistors:

- **Q1** — multi-emitter NPN. Each emitter is an input (A, B). If any input is LOW, that emitter pulls Q1's base low, Q1 saturates, and it steals current from Q2's base (turning Q2 off). Only when ALL inputs are HIGH does Q1 reverse-active conduct into Q2's base (turning Q2 on).
- **Q2** — phase splitter. Its emitter drives Q4 (pull-down) and its collector drives Q3 (pull-up), with opposite phases. When Q2 is on, Q4 is driven on and Q3 is pulled low; when Q2 is off, Q4 is off and Q3 is driven on.
- **Q3, Q4** — the **totem-pole output**. Q3 (the top NPN with a 130 Ω collector resistor) actively pulls the output HIGH; Q4 (the bottom NPN) actively pulls it LOW. They are never both on at once (Q2 ensures complementary drive), so the output is actively driven in both directions — fast edges, high drive, no passive pull-up resistor.

```
       7400 TTL NAND (simplified)

       V_CC
        |
       R1(4k)        R2(1.6k)   R3(130) |
        |               |                |
        +----+         C3 (Q3 coll)     |
        |    |         |                |
       B1   |        |/  Q3 (pull-up)   +----> OUT
    A -E1   |      ---| (top of         |
    B -E2   |      |   |  totem)        |
       C1   |      |   E --+-- diode ---+
        |   |      |         (level shift)
        +--B2      |              |
           Q2(phase)C2            C4
           splitter|              |
           |   E   |           B4 |
           R4(1k) |              | Q4 (pull-down)
           |     GND             | (bottom of totem)
           +----B4?              E
                                 |
                                GND

   Inputs HIGH -> Q1 reverse-active -> Q2 ON -> Q4 ON, Q3 OFF -> OUT LOW
   Any input LOW -> Q1 saturated -> Q2 OFF -> Q4 OFF, Q3 ON -> OUT HIGH
```

(The schematic is simplified; the actual 7400 die has Q1 as a true multi-emitter structure and a Baker-clamp-like network. The behavioral summary above is what matters for using the part.)

### TTL Logic Levels

The 7400 series defines its logic levels relative to a 5 V supply:

| Parameter | Symbol | TTL limit | Meaning |
|-----------|--------|-----------|---------|
| Input LOW (max) | V_IL | 0.8 V | any input ≤ 0.8 V is guaranteed read as logic 0 |
| Input HIGH (min) | V_IH | 2.0 V | any input ≥ 2.0 V is guaranteed read as logic 1 |
| Output LOW (max) | V_OL | 0.4 V | a TTL output driving LOW guarantees ≤ 0.4 V |
| Output HIGH (min) | V_OH | 2.4 V | a TTL output driving HIGH guarantees ≥ 2.4 V |
| Supply | V_CC | 5.0 V ± 0.25 V | strict; out of range = malfunction or latchup |

The **noise margin** is the gap between what the output guarantees and what the input requires:

- **LOW noise margin:** NM_L = V_IL − V_OL = 0.8 − 0.4 = **0.4 V**. A noise spike of up to 0.4 V on a LOW line will not cause a false read.
- **HIGH noise margin:** NM_H = V_OH − V_IH = 2.4 − 2.0 = **0.4 V**. A noise dip of up to 0.4 V on a HIGH line will not cause a false read.

These 0.4 V margins are modest — TTL works on a breadboard with short wires but rings badly on long traces because the totem-pole output has a fast edge (~1–2 ns) that reflects off unterminated ends. (The troubleshooting notes in [Digital Logic](../computing/digital-logic.md) cover decoupling-capacitor placement and transmission-line behavior in detail.)

### Fan-Out

A TTL output can drive a limited number of TTL inputs. Each input, when LOW, sources current (it pulls current *out of* the driving output through the emitter of Q1 — about 1.6 mA, called I_IL, the low-level input current). The output must sink this current and still hold V_OL below 0.4 V; a standard TTL output can sink 16 mA (I_OL). **Fan-out** = I_OL / I_IL = 16 / 1.6 = **10**. A standard TTL gate can drive 10 standard TTL inputs; the 11th would drag V_OL above 0.4 V and corrupt the logic.

### Supply and Power

TTL runs on **5 V ± 0.25 V** — a strict requirement. A 74LS00 (low-power Schottky) gate draws about 2 mW static, so a 14-pin quad-NAND package with four active gates draws ~8 mW. A board of 50 TTL chips draws ~400 mW from the 5 V rail — manageable, but a reminder that TTL is power-hungry compared to CMOS. The supply must be well-regulated; a dip below 4.75 V can cause a gate to read a marginal HIGH as a LOW, and a spike above 5.5 V can trigger **latchup** (a parasitic thyristor in the IC structure fires and shorts V_CC to ground, destroying the chip unless current-limited).

## CMOS (4000 Series)

**Complementary MOS (CMOS)** logic uses a PMOS transistor as the pull-up and an NMOS transistor as the pull-down, arranged so that exactly one is on for any given input. The 4000 series (RCA, 1968) was the first commercially successful CMOS logic family; the 74HC series later married CMOS internals to TTL-compatible pinouts.

### CMOS Inverter

A CMOS inverter is two MOSFETs: a PMOS (source to V_DD, drain to output) and an NMOS (source to ground, drain to output), with their gates tied together as the input.

```
       CMOS INVERTER

        V_DD
         |
        Source (PMOS)
         |---
    A ---|    Q_p (PMOS: on when A LOW, off when A HIGH)
         |---
         +--------+-----> OUT
         |---
    A ---|    Q_n (NMOS: on when A HIGH, off when A LOW)
         |---
        Source (NMOS)
         |
        GND

   A=0 -> Q_p ON, Q_n OFF -> OUT = V_DD  (1)
   A=1 -> Q_p OFF, Q_n ON -> OUT = 0 V   (0)
```

The defining property of CMOS: **in steady state, there is never a conducting path from V_DD to ground.** When A=0, Q_n is off, so even though Q_p is on, no DC current flows (the output load is high impedance). When A=1, Q_p is off. The only current is sub-threshold leakage (nanoamps). This near-zero **static power** is what makes CMOS scalable to billion-transistor chips — a billion TTL gates would dissipate megawatts; a billion CMOS gates dissipate milliwatts at DC.

**Dynamic power** is paid only on switching: each transition charges or discharges the load capacitance C_load through the supply voltage V_DD, at the switching frequency f. The dynamic power is P = C · V² · f. At 5 V and 1 MHz with C = 5 pF, P = 5 pF · 25 · 1 MHz = 0.125 µW per gate — negligible at low frequency, dominant at high frequency. This is why modern CPUs run at ~1 V (the squared V term dominates) and why clock gating (turning off f to idle blocks) is the primary power-saving technique.

### CMOS NAND (4 transistors)

A 2-input CMOS NAND uses two PMOS in parallel (pull-up network) and two NMOS in series (pull-down network):

```
       CMOS NAND (4 transistors)

          V_DD
           |
        +--+--+
        |     |
       Q_p1  Q_p2  (PMOS in parallel)
        |     |
        A     B     (gates)
        |     |
        +--+--+
           |
          OUT
           |
        +--+--+
        |     |
        A     B     (gates)
        |     |
       Q_n1--Q_n2   (NMOS in series: BOTH must be on to pull OUT low)
              |
            GND

   A=1 AND B=1 -> both NMOS on -> OUT low; both PMOS off
   else         -> at least one PMOS on -> OUT high
```

Any input LOW turns on its parallel PMOS and pulls OUT HIGH; only when ALL inputs are HIGH do both series NMOS turn on and pull OUT LOW. The NOR is the dual: PMOS in series, NMOS in parallel.

### CMOS Characteristics

- **Rail-to-rail output:** a CMOS output drives fully to V_DD (HIGH) and fully to ground (LOW), because the on-resistance of a MOSFET is low and there is no saturation voltage drop. This gives the largest possible logic swing.
- **High input impedance:** a CMOS input is a gate oxide capacitor — it draws ~1 pA DC. Fan-out is effectively unlimited for DC (limited only by the capacitance that slows the edge: each input adds ~5 pF, and after ~50 inputs the RC delay becomes the speed limit rather than the gate's own propagation delay).
- **Wide supply range:** the 4000 series works from **3 to 15 V**. Logic levels are proportional to V_DD: V_IH ≈ 0.7·V_DD, V_IL ≈ 0.3·V_DD, and V_OH ≈ V_DD, V_OL ≈ 0. So at V_DD = 5 V, V_IH ≈ 3.5 V and V_IH ≈ 1.5 V; at V_DD = 10 V, the thresholds scale up.
- **Slower than TTL at 5 V:** 4000-series propagation delay is ~50–100 ns at 5 V (faster at 10–15 V, because higher V_DD overdrives the MOSFETs). The 74HC series (CMOS with TTL pinouts) achieves ~8 ns at 5 V, matching TTL speed.

**ESD sensitivity.** The thin gate oxide of a CMOS input ruptures at ~100 V — an imperceptible electrostatic discharge. CMOS parts must be handled on grounded mats with wrist straps and stored in conductive foam. TTL, with its robust emitter junctions, is nearly immune by comparison.

## Logic-Level Parameter Comparison

| Parameter | TTL 74xx | TTL 74LS | CMOS 4000 (5 V) | CMOS 74HC (5 V) |
|-----------|----------|----------|-----------------|------------------|
| Supply V_DD | 5.0 ± 0.25 V | 5.0 ± 0.25 V | 3–15 V | 2–6 V |
| V_IL (max) | 0.8 V | 0.8 V | 1.5 V | 1.5 V |
| V_IH (min) | 2.0 V | 2.0 V | 3.5 V | 3.5 V |
| V_OL (max) | 0.4 V | 0.4 V | 0.05 V | 0.1 V |
| V_OH (min) | 2.4 V | 2.4 V | 4.95 V | 4.9 V |
| NM_L (low) | 0.4 V | 0.4 V | 1.45 V | 1.4 V |
| NM_H (high) | 0.4 V | 0.4 V | 1.45 V | 1.4 V |
| Fan-out (same family) | 10 | 10 | 50+ | 50+ |
| Propagation delay | 10 ns | 9 ns | 50–100 ns | 8 ns |
| Static power / gate | 10 mW | 2 mW | ~0 (nA leakage) | ~0 (nA leakage) |
| Dynamic power / gate | 10 mW | 2 mW | C·V²·f (e.g. 0.1 µW @ 1 MHz) | C·V²·f (e.g. 0.1 µW @ 1 MHz) |
| Typical use | legacy glue | legacy prototype | low-power, wide supply | general new design |

**Interfacing TTL to CMOS.** A 74HC output (rail-to-rail) drives a TTL input directly — its HIGH (4.9 V) is well above V_IH (2.0 V). A TTL output driving a CMOS input is the problem case: a TTL HIGH (guaranteed only ≥ 2.4 V) is below the 74HC V_IH (3.5 V) when the CMOS is at 5 V. The fix is a **pull-up resistor** (1–10 kΩ from the TTL output to V_CC) to lift the HIGH level to ~5 V, or use **74HCT** (CMOS with TTL-compatible input thresholds, V_IH = 2.0 V). The 4000-series CMOS driving TTL is fine on HIGH (rail-to-rail HIGH >> 2.0 V) but marginal on LOW sink current: a 4000-series output can sink only ~0.5 mA at 5 V, less than the 1.6 mA a TTL input sources, so fan-out is 0 (it cannot drive even one standard TTL input directly). Use a 74HC/74HCT buffer, or a 4049/4050 CMOS-to-TTL level shifter.

## Open-Collector / Open-Drain Outputs

The totem-pole output of a standard TTL gate cannot have its outputs connected together — if one drives HIGH (Q3 on) and another drives LOW (Q4 on), the direct conflict shorts V_CC to ground through both output stages, drawing destructive current. **Open-collector** (TTL) and **open-drain** (CMOS) outputs omit the pull-up transistor (Q3) entirely: the output is just the collector (or drain) of the pull-down transistor, which can only pull LOW or release (float).

A single external **pull-up resistor** on the shared line provides the HIGH level. When any connected gate pulls LOW, the line goes LOW. When *all* connected gates release, the resistor pulls the line HIGH. This is the **wired-AND** function: the line is HIGH only if all open-collector outputs are off (all inputs satisfy the HIGH condition).

```
       OPEN-COLLECTOR WIRED-AND

        V_CC
         |
        R_pullup (4.7 kΩ)
         |
         +--------+--------+-------> BUS (HIGH only if all 3 outputs off)
         |        |        |
        C1       C2       C3   (open-collector outputs, can only pull LOW)
        |        |        |
      GATE A   GATE B   GATE C

    BUS = A_nAND-out AND B_nAND-out AND C_nAND-out  (wired-AND)
    Any gate pulling LOW -> BUS LOW
    All gates off       -> BUS HIGH (via pull-up)
```

### Pull-up Resistor Sizing

The pull-up resistor must satisfy two constraints:

1. **LOW sink:** when one output pulls LOW, it must sink the current through R_pullup (plus any downstream input current) and still hold V_OL. For TTL, I_OL = 16 mA, V_OL = 0.4 V: R_min = (V_CC − V_OL) / I_OL = (5 − 0.4) / 16 mA = 287 Ω. In practice, with several inputs sourcing into the LOW line, the effective floor is higher.
2. **HIGH speed:** when all outputs release, R_pullup charges the total bus capacitance (C_bus = sum of all input capacitances + wire capacitance, often 10–50 pF) up to V_CC. The RC time constant τ = R · C sets the rise time: for R = 4.7 kΩ and C = 50 pF, τ = 235 ns — too slow for >1 MHz. For a fast bus, R must drop toward 1 kΩ or below.

**Standard value:** 4.7 kΩ is the canonical I²C / open-collector pull-up, good for low-speed buses up to ~100 kHz. For 400 kHz I²C, drop to 2.2 kΩ; for 1 MHz, ~1 kΩ. The [passive-components article](passive-components.md) covers resistor tolerance and power rating.

**Level shifting.** An open-collector gate with its pull-up tied to a *different* voltage than V_CC is a simple level shifter: a 5 V TTL open-collector output with its pull-up to 12 V translates a 0/5 V signal into a 0/12 V signal. This is how 3.3 V logic drives 5 V peripherals and vice versa in mixed-voltage systems.

## Tri-State Buffers

A **tri-state buffer** adds a third output state — **high-impedance (high-Z)** — to the normal HIGH and LOW. When the **enable** input is de-asserted, both the pull-up and pull-down transistors in the output stage turn off, and the output presents a very high impedance (leakage only, ~1 µA) to the line. This is distinct from open-collector (which can only pull LOW or float) — a tri-state output actively drives HIGH, actively drives LOW, or disconnects entirely.

```
       TRI-STATE BUFFER

         ---\
   IN --|    \---> OUT
         ---/
          |
        /EN  (enable: when EN=0, OUT = high-Z regardless of IN)
```

Tri-state is what makes **bus sharing** possible: multiple devices drive the same bus line, but only one has its enable asserted at a time. The others are in high-Z and are electrically invisible (they neither drive nor load the line). This is how a microprocessor address/data bus works — the CPU drives the bus during a write cycle, a memory chip drives it during a read cycle, and only the addressed device enables its output.

**Critical rule:** at most one tri-state output may be enabled on a shared line at any time. If two enable simultaneously, the result is the same destructive conflict as tying two totem-pole outputs together — one drives HIGH, the other drives LOW, and large shoot-through current flows. Bus contention is a common cause of intermittent failures and damaged drivers.

Tri-state is implemented in both TTL (74LS244 octal buffer, 74LS373 octal latch) and CMOS (74HC244, 74HC373, and the 74LVC family for low-voltage logic). The enable is often **active-low** (a bubble on the pin), reflecting the convention that "not enabled" = "safe default = high-Z."

## Putting It Together: Building a Working Gate Circuit

To actually build a logic circuit from discrete logic ICs, you need:

1. **Decoupling capacitors.** A 0.1 µF ceramic capacitor across V_CC-to-GND, placed within 1 cm of each IC's power pins. Logic gates draw sharp current spikes on every switching edge (the totem-pole momentarily conducts as Q3 and Q4 overlap); without local decoupling, these spikes appear on the V_CC rail and couple into every other chip as noise. This is the single most important rule of TTL breadboarding.
2. **A clean, regulated 5 V supply.** A 7805 linear regulator (see [linear-regulators](power-supply-circuits.linear-regulators.md)) fed from a 9 V battery or wall adapter provides the required 5 V ± 0.25 V. Current-limited bench supplies (100–200 mA) limit damage if a wiring error shorts the rail.
3. **Tied-down unused inputs.** A floating TTL input tends to read as HIGH (the multi-emitter transistor's base floats up) but is unreliable and picks up noise. Tie unused inputs to V_CC (through a 1 kΩ resistor) or ground. For CMOS, this is *critical*: a floating CMOS input drifts to mid-rail, turning on both PMOS and NMOS, creating a DC path that dissipates 10+ mW per input and can destroy the chip.
4. **ESD precautions (CMOS).** Grounded mat, wrist strap, conductive storage. Never handle bare CMOS dies or 4000-series parts on a carpeted day without grounding.

A first project: a quad-NAND 7400 on a breadboard, with two switches on the inputs, an LED + 330 Ω current-limit resistor on the output, and a 0.1 µF decoupling cap across the power pins. Toggle the switches and verify the truth table above. This is the "hello world" of digital electronics — the moment the abstraction of Boolean logic becomes a glowing LED in your hand.

## From Discrete Gates to Sequential Logic

Every circuit in this article is **combinational**: the output is a pure function of the current inputs, with no memory. The moment we add **feedback** — routing an output back to an input — a gate network gains state. Two cross-coupled NOR gates become an SR latch, the simplest memory element. Add a clock and you have a flip-flop. Stack flip-flops and you have counters and shift registers. That is the subject of the companion article, [Sequential Logic Circuits](control-circuits.sequential-logic-circuits.md).

## See Also

- [Control Circuits](control-circuits.md) — parent capability: the design-pedagogy hub for relay, ladder, discrete, and sequential logic.
- [Sequential Logic Circuits](control-circuits.sequential-logic-circuits.md) — the companion article: latches, flip-flops, counters, shift registers built from the gates in this article.
- [Relay Logic Circuits](control-circuits.relay-logic.md) — the electromechanical predecessor: the same AND/OR/NOT functions and the seal-in latch, built from relay contacts.
- [Transistor Switch Circuits](analog-circuits.transistor-switch-circuits.md) — the BJT and MOSFET as switches, including forced-beta saturation design; the foundation on which the transistor-level gates here are built.
- [Diode Circuits](analog-circuits.diode-circuits.md) — diode clippers, clampers, and detectors; the diode-AND network of DTL extends these.
- [Multivibrator Circuits](analog-circuits.multivibrator-circuits.md) — the bistable multivibrator is the discrete-transistor ancestor of the flip-flop.
- [Semiconductor Devices](semiconductor-devices.md) — BJT and MOSFET physics, V-I curves, and the saturation/cutoff regions that make switching possible.
- [Passive Components](passive-components.md) — resistors (pull-ups, pull-downs, base bias) and capacitors (decoupling).
- [Digital Logic](../computing/digital-logic.md) — Boolean algebra, De Morgan's laws, Karnaugh maps, and logic minimization; the mathematics this hardware implements.
- [Logic Design](../computing/logic-design.md) — HDL, FPGA, and system-level design methodology for scaling beyond discrete gates.

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
