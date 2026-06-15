# DC Circuit Analysis

> **Node ID**: electronics.circuit-fundamentals.dc-analysis
> **Domain**: [Electronics](index.md)
> **Dependencies**: [`electronics.passive-components`](passive-components.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Enables**: None
> **Timeline**: Years 15-30
> **Outputs**: dc-circuit-analysis
> **Critical**: No — circuit theory is analytical knowledge; a practiced practitioner can derive results from memory once components exist

This article teaches DC circuit analysis **from first principles**. It assumes you have copper wire, a battery, and some resistors ([passive components](passive-components.md)) wired together with [electrical systems](electrical-systems.md) infrastructure — but it assumes **no theory**. By the end you will be able to take any network of resistors and sources on paper and calculate every voltage and current in it, by hand, with nothing but arithmetic. This is the Edison-era foundation: everything electrical, from telegraphs to GPUs, is built on top of it.

The scope is strictly **DC** — direct current, where voltages and currents are constant in time. Capacitors and inductors in a DC steady state reduce to opens and shorts, so this article deals only with resistors and sources. Time-varying (AC) analysis is a separate article.

---

## 1. The Three Quantities: Voltage, Current, Resistance

### 1.1 The water analogy

Before equations, build intuition. Electricity in a wire behaves like water in a pipe:

| Electrical | Water analogy | What it measures |
|------------|---------------|------------------|
| **Charge** (coulomb, C) | A quantity of water (litres) | The "stuff" that moves |
| **Current** `I` (ampere, A = C/s) | Flow rate (litres/second) | How fast charge passes a point |
| **Voltage** `V` (volt, V) | Pressure (metres of head) | How hard each charge is pushed |
| **Resistance** `R` (ohm, Ω) | Pipe narrowness / friction | How much the pipe resists flow |

- **Voltage** is a *difference* in pressure between two points. A single point has no "voltage" in an absolute sense — it has a voltage *relative to* another point. This is why every voltmeter has two probes. We pick one point in a circuit, call it **ground** (0 V), and express all other node voltages relative to it.
- **Current** is the flow rate of charge through a cross-section of wire. By convention it flows from the higher-pressure (+) terminal to the lower-pressure (−) terminal — even though in metals the physical electrons travel the opposite way. This convention predates the discovery of the electron and is locked in; use it.
- **Resistance** is the friction of the wire itself. Copper has very low resistance (it is a wide, smooth pipe); a resistor is a deliberate narrowing that limits flow.

### 1.2 Units and scale

| Quantity | Unit | Symbol | Typical bench values |
|----------|------|--------|----------------------|
| Voltage | volt | V | 1.5 V (cell), 6 V, 12 V (battery), 24 V (plant bus) |
| Current | ampere | A | 0.001 A (1 mA, signal), 0.1–2 A (LED/lamp), 10 A (heater) |
| Resistance | ohm | Ω | 10 Ω – 10 MΩ (1 MΩ = 1 000 000 Ω) |
| Power | watt | W | 1/4 W (small resistor), 1–5 W (power resistor), 60 W (lamp) |

Engineers use SI prefixes constantly: `mA` = 10⁻³ A, `kΩ` = 10³ Ω, `MΩ` = 10⁶ Ω, `µ` (micro) = 10⁻⁶. Discipline with these prefixes prevents a factor-of-1000 error, which is the most common mistake in hand analysis.

---

## 2. Ohm's Law: V = I × R

### 2.1 Statement and derivation

Ohm's law (Georg Ohm, 1827) is an empirical observation: for a metal conductor at constant temperature, the current through it is **directly proportional** to the voltage across it. The constant of proportionality is the inverse of its resistance.

```
    I  ──────►
  ┌─────R─────┐
  │           │
( + ) V_R   ( − )      The voltage V_R across R drives current I through it.
  │           │
  └───────────┘

    V = I × R        (Ohm's law — all three forms)
    I = V ÷ R
    R = V ÷ I
```

Read this as: *the pressure difference (V) equals the flow rate (I) times the friction (R).* Double the pressure → double the flow. Double the resistance → halve the flow. This linear relationship holds for ideal resistors over the entire range where the resistor does not overheat or arc.

### 2.2 Worked example

A 12 V battery is connected across a 4.7 kΩ resistor. What current flows?

```
I = V ÷ R = 12 V ÷ 4700 Ω = 0.002553 A ≈ 2.55 mA
```

Sanity check the magnitude: a few milliamps through a kilohm-scale resistor from a bench battery is exactly right. If you got 2550 A, you forgot a prefix.

### 2.3 Worked example — finding an unknown resistance

You measure 9 V across a resistor and 30 mA through it. What is R?

```
R = V ÷ I = 9 V ÷ 0.030 A = 300 Ω
```

This is how an ohmmeter works internally: force a known small current, measure the resulting voltage, and divide.

---

## 3. Series and Parallel Resistance

A circuit rarely has one resistor. The two ways to combine two-terminal elements are **series** (end-to-end, one path) and **parallel** (side-by-side, two paths). Every resistive network, no matter how large, is built from these two combinations.

### 3.1 Series — the single path

```
    I ──────►
  ┌──R1──R2──R3──┐
  │              │
( + ) Vs       ( − )
  │              │
  └──────────────┘
```

In series the same current flows through every resistor. Each resistor drops some of the source voltage. Adding resistors in series always gives a **larger** total resistance — you are lengthening the pipe.

```
R_series = R1 + R2 + R3 + ...
```

**Worked example.** Three resistors in series: 100 Ω, 220 Ω, 470 Ω.

```
R_total = 100 + 220 + 470 = 790 Ω
```

With 12 V applied: `I = 12 ÷ 790 = 15.2 mA` through all three. The voltage across each is `V = I×R`:
- `V_100 = 0.0152 × 100 = 1.52 V`
- `V_220 = 0.0152 × 220 = 3.34 V`
- `V_470 = 0.0152 × 470 = 7.14 V`

Check: `1.52 + 3.34 + 7.14 = 12.0 V` ✓ — the drops sum to the source. This summation property is Kirchhoff's voltage law (§4), previewed.

### 3.2 Parallel — the branching path

```
        ┌──R1──┐
   ─────┤      ├─────
        ├──R2──┤
        │      │
        └──R3──┘
```

In parallel the same voltage appears across every resistor, but the current splits among them. Adding resistors in parallel always gives a **smaller** total resistance — you are adding pipes, so the combined flow is easier.

```
1 / R_parallel = 1/R1 + 1/R2 + 1/R3 + ...

    R_total = 1 ÷ (1/R1 + 1/R2 + 1/R3 + ...)
```

**The two-resistor shortcut** (memorise this — it is used constantly):

```
R_total = (R1 × R2) ÷ (R1 + R2)
```

**Worked example.** Two resistors in parallel: 1 kΩ and 1 kΩ.

```
R_total = (1000 × 1000) ÷ (1000 + 1000) = 1 000 000 ÷ 2000 = 500 Ω
```

Two equal resistors in parallel always give exactly half — intuitive: two identical pipes side by side carry twice the flow at the same pressure.

**Worked example.** 1 kΩ in parallel with 2.2 kΩ.

```
R_total = (1000 × 2200) ÷ (1000 + 2200) = 2 200 000 ÷ 3200 = 687.5 Ω
```

### 3.3 Quick combination rules

| Combination | Rule of thumb |
|-------------|---------------|
| Series resistors | Total is *larger* than the largest single one |
| Parallel resistors | Total is *smaller* than the smallest single one |
| N equal resistors in series | `N × R` |
| N equal resistors in parallel | `R ÷ N` |
| Resistor in parallel with 0 Ω (short) | Always 0 Ω |
| Resistor in series with ∞ Ω (open) | Always ∞ Ω |

---

## 4. Kirchhoff's Two Laws

Ohm's law handles one resistor. Kirchhoff's laws (Gustav Kirchhoff, 1845) handle **any** network. They are the two axioms from which all systematic circuit analysis is derived. Both are consequences of conservation laws — conservation of charge and conservation of energy.

### 4.1 Kirchhoff's Current Law (KCL) — conservation of charge

> **The algebraic sum of currents entering a node is zero.**

Equivalently: charge cannot pile up at a junction. What flows in must flow out.

```
         I1 ──►
              │
         ┌────┼────┐
         │    │    │
        I2   node  I3
         │    │    │
         ▼    ▼    ▼
```

Sign convention: currents **entering** the node are positive, currents **leaving** are negative (or vice versa — just be consistent). For the node above:

```
I1 − I2 − I3 = 0        ⟹        I1 = I2 + I3
```

KCL is the basis of the **node-voltage method** (§5). Every node gives one equation; collect enough nodes and you have a solvable system.

### 4.2 Kirchhoff's Voltage Law (KVL) — conservation of energy

> **The algebraic sum of voltages around any closed loop is zero.**

Equivalently: the pressure gained from the source is exactly spent by the drops across the loads. You cannot get more energy out of a loop than the source put in.

```
   ┌───R1───┬───R2───┐
   │        │        │
 ( + )               │
  Vs                 ●  (loop back to source −)
 ( − )               │
   │                 │
   └─────────────────┘
```

Walking the loop clockwise from Vs's negative terminal:

```
−Vs + V_R1 + V_R2 = 0        ⟹        Vs = V_R1 + V_R2
```

Sign convention for KVL: walk the loop in a chosen direction; a voltage **rise** (source − to +) is negative in the sum, a voltage **drop** (+ to −) is positive. Pick one direction per loop and stick to it.

KVL is the basis of the **mesh-current method** (§5). Each independent loop gives one equation.

---

## 5. Systematic Analysis: Node-Voltage and Mesh-Current

For circuits with more than two or three resistors, applying Ohm's law ad hoc becomes error-prone. Two systematic methods turn any linear circuit into a set of linear equations that can be solved by arithmetic. **Learn both; each is faster for certain topologies.**

### 5.1 Node-voltage method

**Idea.** Pick one node as the reference (ground, 0 V). Treat the voltage at every other node as an unknown. Apply KCL at each unknown node, expressing each branch current in terms of node voltages via Ohm's law (`I = (V_a − V_b)/R`). Solve the resulting linear system.

**Procedure.**
1. Choose a reference node (ground). Label it 0 V.
2. Label the remaining nodes `V_a`, `V_b`, …
3. At each labelled node, write KCL: sum of currents leaving = 0, with each current written as `(node − neighbour)/R`.
4. Solve the linear system for the node voltages.
5. Back-substitute to find any branch current or component voltage.

A voltage source tied directly between a node and ground fixes that node's voltage immediately (no KCL needed there). A voltage source between two non-ground nodes forms a "supernode" — write KCL for the combined region and add the constraint `V_a − V_b = Vs`.

### 5.2 Worked node-analysis example — two nodes, two sources

```
           R1 = 1 kΩ
   Va ●──────/\/\/\──────● V1 = 5 V
     │
     │ R2 = 2 kΩ
     │
   Vb ●──────/\/\/\──────● V2 = 9 V
     │
     │ R3 = 1 kΩ
     │
    ──●── GND (reference)
```

Wait — that is a ladder, and the labelled node is the single unknown `Vb`. Let me set up a cleaner, fully-worked two-node circuit:

```
   10 V ●───[ R1=2Ω ]──●───[ R3=4Ω ]──● 0 V (ground)
                        │
                       [R2=4Ω]
                        │
                        ● Vx  (this node goes to ground via R2)

   Re-drawn for clarity:

        2Ω              4Ω
   10V ●──/\/\──●a──/\/\──● 0V
               |
              4Ω (R2)
               |
              ● 0V

   Only ONE unknown node: Va.
```

Let us restate the circuit unambiguously: a 10 V source feeds node **a** through R1 = 2 Ω. From node **a**, R2 = 4 Ω goes to ground, and R3 = 4 Ω also goes to ground. Find `Va`.

**Step 1 — reference.** Ground is the bottom rail: 0 V. The single unknown is `Va`.

**Step 2 — KCL at node a.** Sum of currents leaving = 0. There are three branches at node a: toward the source (through R1), toward ground through R2, toward ground through R3.

Current leaving node a toward the 10 V source through R1: `(Va − 10) / 2`.
Current leaving node a to ground through R2: `(Va − 0) / 4`.
Current leaving node a to ground through R3: `(Va − 0) / 4`.

KCL:
```
(Va − 10)/2  +  Va/4  +  Va/4  =  0
```

**Step 3 — solve.** Multiply through by 4 to clear denominators:
```
2(Va − 10) + Va + Va = 0
2·Va − 20 + Va + Va = 0
4·Va = 20
Va = 5 V
```

**Step 4 — back-substitute for every current.**
- Through R1 (from source): `I1 = (10 − 5)/2 = 2.5 A`
- Through R2: `I2 = 5/4 = 1.25 A`
- Through R3: `I3 = 5/4 = 1.25 A`

**Step 5 — verify with KCL.** Current in = 2.5 A; current out = 1.25 + 1.25 = 2.5 A. ✓ Balance holds. The method works: one unknown, one equation, exact solution.

### 5.3 Mesh-current method

**Idea.** Identify the independent "window panes" (meshes) of the circuit. Assign each a circulating loop current. Apply KVL around each mesh, expressing each resistor drop as `(mesh current − neighbour mesh current) × R`. Solve the linear system.

**Procedure.**
1. Identify the independent meshes (the smallest loops that do not contain another loop inside them).
2. Assign each mesh a clockwise loop current: `I_A`, `I_B`, …
3. Write KVL around each mesh: sum of voltage rises (sources) = sum of voltage drops (resistors). A resistor shared by two meshes carries the *difference* of the two mesh currents.
4. Solve the linear system for the mesh currents.
5. Any real branch current is the algebraic sum of the mesh currents passing through it.

**When to choose which.** Node-voltage is faster when the circuit has fewer nodes than loops (many parallel branches). Mesh-current is faster when the circuit has fewer loops than nodes (many series elements, ladder-like). For a circuit with `N` independent nodes and `M` independent meshes, both methods yield the same number of equations — pick the smaller set.

---

## 6. Voltage and Current Dividers

Dividers are the **design formulas** of DC analysis — they let you read off a desired voltage or current by inspection, without setting up a full system. They appear everywhere: sensor bias networks, reference voltages, transistor base dividers, attenuators.

### 6.1 Voltage divider

Two resistors in series across a source. The voltage splits in proportion to the resistances.

```
              R1
   Vin ●──/\/\──●──/\/\──● 0V
                │   R2
                ●
               Vout  (voltage across R2)
```

```
Vout = Vin × R2 ÷ (R1 + R2)
```

Read it as: the output is the fraction `R2 / (R1 + R2)` of the input. The larger R2 relative to the total, the larger the output voltage.

**Worked example.** `Vin = 12 V`, `R1 = 1 kΩ`, `R2 = 2 kΩ`.

```
Vout = 12 × 2000 ÷ (1000 + 2000) = 12 × 2000 ÷ 3000 = 12 × 0.667 = 8.0 V
```

**Critical caveat — loading.** This formula assumes nothing draws current from the `Vout` node. The moment you connect a load, it appears in parallel with R2, lowers the effective bottom resistance, and drags `Vout` down. A voltage divider is a *signal* circuit, not a power supply. The rule of thumb: the load resistance must be at least 10× (ideally 100×) the divider's bottom leg for the formula to hold within tolerable error. This single fact motivates the invention of the regulated power supply and the emitter-follower buffer.

### 6.2 Current divider

Two resistors in parallel fed by a current source. The current splits inversely proportional to the resistances — the *smaller* resistor takes the *larger* share.

```
          ┌──[R1]──┐
   Iin ●──┤        ├──●
          └──[R2]──┘
```

Current through R1:
```
I_R1 = Iin × R2 ÷ (R1 + R2)
```

Note the symmetry: the current in one branch is proportional to the *other* resistor divided by the sum. This mirrors the voltage divider but with the opposite resistor in the numerator.

**Worked example.** `Iin = 30 mA`, `R1 = 2 kΩ`, `R2 = 1 kΩ`.

```
I_R1 = 30 mA × 1000 ÷ (2000 + 1000) = 30 × 0.333 = 10.0 mA
I_R2 = 30 mA × 2000 ÷ 3000            = 30 × 0.667 = 20.0 mA   (smaller R, bigger share)
```

Check: `10 + 20 = 30 mA` ✓.

---

## 7. Power: P = V × I = I² × R = V² ÷ R

### 7.1 The three forms

A resistor converts electrical energy into heat. The rate of that conversion is **power**, measured in watts (W = J/s). From the definitions of voltage (energy per charge) and current (charge per second), power is their product:

```
P = V × I        (definition)
```

Substituting Ohm's law (`V = IR` or `I = V/R`) gives two equivalent forms, useful when you only know two of the three quantities:

```
P = I² × R       (use when you know the current)
P = V² ÷ R       (use when you know the voltage)
```

All three are the same statement. Pick the one that uses the quantities you already have.

### 7.2 Worked example — sizing a resistor's wattage

A 100 Ω resistor has 12 V across it. How much power does it dissipate, and what physical resistor rating is safe?

```
P = V² ÷ R = 12² ÷ 100 = 144 ÷ 100 = 1.44 W
```

A standard 1/4 W (0.25 W) resistor would be destroyed here — it would need to shed 1.44 W as heat but can only handle 0.25 W before the resistive element overheats and fails. A **2 W** (or larger, 3 W / 5 W) power resistor is required, and even then it must be mounted with airflow. This calculation, done before reaching for a part, is what prevents a burned board.

A second view of the same circuit, using the current form: `I = V/R = 12/100 = 0.12 A`, then `P = I²R = 0.12² × 100 = 0.0144 × 100 = 1.44 W` — identical answer.

### 7.3 Power rating selection rule

| Resistor body style | Typical rating | Derate to (for reliability) |
|---------------------|----------------|------------------------------|
| 1/4 W axial carbon film | 0.25 W | ≤ 0.125 W (50% margin) |
| 1/2 W axial | 0.5 W | ≤ 0.25 W |
| 1 W axial | 1.0 W | ≤ 0.5 W |
| 2–5 W wirewound | 2–5 W | ≤ 1–2.5 W, with airflow |
| 10–50 W aluminium-housed | 10–50 W | bolted to a heatsink |

**Rule:** always run a resistor at no more than 50–60% of its rated power. At full rating the case can exceed 150 °C, which burns fingers, scorches boards, and shortens life. The derating curve on every resistor datasheet shows allowable power falling above 70 °C ambient — in a hot enclosure a "2 W" part may only be good for 1 W.

### 7.4 Source power and efficiency

The total power delivered by a source is `P_source = V_s × I_total`. The useful power delivered to the load is `P_load = V_load × I_load`. In a simple battery-plus-resistor circuit these are equal (the resistor is the only load). In a real system with internal source resistance `R_s`, some power is lost inside the source itself: `P_loss = I² × R_s`. The condition that maximises the power delivered to the load — **maximum power transfer** — occurs when `R_load = R_s`. This is derived in the network-theorems article; the practical upshot is why audio amplifiers are specified into matched 4 Ω / 8 Ω speakers and why radio antennas are matched to 50 Ω.

---

## 8. Reference Tables

### 8.1 E12 standard resistor series (10 per decade)

The E12 series is the baseline tolerance (±10%) value set. Each decade (1–10, 10–100, 100 Ω–1 kΩ, …) repeats these base numbers. A civilisation making resistors to E12 can stock just 12 values per decade and cover every design need with series/parallel combinations.

| Base | ×1 | ×10 | ×100 | ×1 k | ×10 k | ×100 k | ×1 M |
|------|----|-----|------|------|-------|--------|------|
| 1.0  | 1.0 Ω | 10 Ω | 100 Ω | 1.0 kΩ | 10 kΩ | 100 kΩ | 1.0 MΩ |
| 1.2  | 1.2 Ω | 12 Ω | 120 Ω | 1.2 kΩ | 12 kΩ | 120 kΩ | 1.2 MΩ |
| 1.5  | 1.5 Ω | 15 Ω | 150 Ω | 1.5 kΩ | 15 kΩ | 150 kΩ | 1.5 MΩ |
| 1.8  | 1.8 Ω | 18 Ω | 180 Ω | 1.8 kΩ | 18 kΩ | 180 kΩ | 1.8 MΩ |
| 2.2  | 2.2 Ω | 22 Ω | 220 Ω | 2.2 kΩ | 22 kΩ | 220 kΩ | 2.2 MΩ |
| 2.7  | 2.7 Ω | 27 Ω | 270 Ω | 2.7 kΩ | 27 kΩ | 270 kΩ | 2.7 MΩ |
| 3.3  | 3.3 Ω | 33 Ω | 330 Ω | 3.3 kΩ | 33 kΩ | 330 kΩ | 3.3 MΩ |
| 3.9  | 3.9 Ω | 39 Ω | 390 Ω | 3.9 kΩ | 39 kΩ | 390 kΩ | 3.9 MΩ |
| 4.7  | 4.7 Ω | 47 Ω | 470 Ω | 4.7 kΩ | 47 kΩ | 470 kΩ | 4.7 MΩ |
| 5.6  | 5.6 Ω | 56 Ω | 560 Ω | 5.6 kΩ | 56 kΩ | 560 kΩ | 5.6 MΩ |
| 6.8  | 6.8 Ω | 68 Ω | 680 Ω | 6.8 kΩ | 68 kΩ | 680 kΩ | 6.8 MΩ |
| 8.2  | 8.2 Ω | 82 Ω | 820 Ω | 8.2 kΩ | 82 kΩ | 820 kΩ | 8.2 MΩ |

Each step is roughly a 20% increase (the square of √10 ≈ 3.16 over 12 steps), so that adjacent values overlap under their ±10% tolerance bands. Finer series exist (E24 ±5%, E96 ±1%) but E12 is the bootstrap baseline.

### 8.2 Copper wire ampacity (continuous DC, chassis wiring, ≤ 30 °C rise)

Wire gauge limits how much current a conductor can carry before resistive (I²R) heating raises its temperature dangerously. The table below gives conservative continuous-current ratings for single insulated copper conductors in free air — the starting point for [electrical systems](electrical-systems.md) wiring.

| AWG | Diameter (mm) | Resistance (Ω per km, 20 °C) | Max current (A, chassis) |
|-----|---------------|------------------------------|--------------------------|
| 10 | 2.59 | 3.28 | 55 |
| 12 | 2.05 | 5.21 | 41 |
| 14 | 1.63 | 8.29 | 32 |
| 16 | 1.29 | 13.2 | 22 |
| 18 | 1.02 | 21.0 | 16 |
| 20 | 0.81 | 33.3 | 11 |
| 22 | 0.64 | 53.0 | 7 |
| 24 | 0.51 | 84.2 | 3.5 |
| 26 | 0.40 | 134 | 2.2 |
| 28 | 0.32 | 213 | 1.4 |
| 30 | 0.25 | 339 | 0.9 |

Use these ratings for the *power* wiring (battery to load). Signal currents (mA range) almost never heat the wire — there a smaller gauge is acceptable and is chosen for mechanical convenience, not ampacity. Derate by 30% for conductors bundled in a harness or run inside a hot enclosure.

---

## 9. Putting It Together — A Complete Analysis

To cement the method, here is the full workflow on a representative circuit that exercises every tool above.

```
        R1 = 1 kΩ            R2 = 2 kΩ
   12V ●──/\/\──●a──/\/\──●──► (to next stage as V_out)
              |
             R3 = 2 kΩ        ← load branch
              |
              ● 0V (ground)
```

**Goal:** find `Va` and the current drawn from the 12 V source.

**Step 1 — simplify.** R2 (2 kΩ) and R3 (2 kΩ) are in parallel from node a to ground:
```
R_23 = (2000 × 2000) ÷ (2000 + 2000) = 1 kΩ
```

**Step 2 — now R1 is in series with R_23.** This is a voltage divider:
```
Va = 12 V × R_23 ÷ (R1 + R_23) = 12 × 1000 ÷ (1000 + 1000) = 12 × 0.5 = 6.0 V
```

**Step 3 — back-substitute the branch currents.**
- Source current through R1: `I1 = (12 − 6)/1000 = 6 mA`
- Through R2: `I2 = 6/2000 = 3 mA`
- Through R3: `I3 = 6/2000 = 3 mA`

**Step 4 — verify KCL at node a.** In: 6 mA (from R1). Out: 3 + 3 = 6 mA. ✓
**Verify KVL around the outer loop.** `12 V = V_R1 + Va = 6 V + 6 V` ✓

**Step 5 — power.** Source delivers `P = 12 V × 0.006 A = 72 mW`. R1 dissipates `I1²R1 = 0.006² × 1000 = 36 mW` — a 1/4 W resistor is comfortable. Each parallel branch dissipates `3² mW/branch... = 0.003² × 2000 = 18 mW` (×2 branches = 36 mW). Check: 36 (R1) + 36 (loads) = 72 mW = source power ✓.

This five-step rhythm — **simplify, solve, back-substitute, verify KCL+KVL, check power** — is the discipline of a working circuit analyst. Do it on paper every time and the circuit will work on the bench the first time.

---

## 10. Summary of the Laws

| Law / tool | Equation | When to use |
|------------|----------|-------------|
| Ohm's law | `V = I·R` | Single resistor, known two of V/I/R |
| Series resistance | `R = R1 + R2 + …` | End-to-end chain |
| Parallel resistance | `R = 1/(1/R1 + 1/R2 + …)` | Branching paths |
| KCL | `Σ I_in = 0` at a node | Foundation of node-voltage method |
| KVL | `Σ V = 0` around a loop | Foundation of mesh-current method |
| Node-voltage | KCL in terms of node voltages | Networks with few nodes |
| Mesh-current | KVL in terms of loop currents | Networks with few loops |
| Voltage divider | `Vout = Vin·R2/(R1+R2)` | Tap a fraction of a voltage |
| Current divider | `I1 = Iin·R2/(R1+R2)` | Split a current between branches |
| Power | `P = V·I = I²R = V²/R` | Heat dissipation, wattage sizing |

These ten tools are the complete analytical toolkit for any DC resistive network. Every later electronics capability — amplifiers, power supplies, logic gates — reduces to these laws applied to more components. Master them once and they are never relearned.

---


## Safety

These circuits operate at low DC voltages (typically 5-24V) where electric shock risk is minimal. Observe standard ESD precautions: ground all workbench equipment, wear conductive wrist straps when handling MOSFETs and ICs, store sensitive devices in antistatic bags. Soldering iron tips reach 300-350°C — use stands, avoid burns, and work in a ventilated area to avoid flux fume inhalation (colophony flux causes occupational asthma). For circuits that switch mains AC or drive high-current loads (>1A), use isolation transformers and follow [PPE](../ehs/ppe.md) and [electrical safety](../ehs/chemical-safety.md) procedures.

## See Also

- [Circuit Fundamentals](circuit-fundamentals.md) — the parent capability hub; this article is one of its process children (the AC-analysis sibling article covers sinusoidal and reactive circuits).
- [Passive Components](passive-components.md) — how the resistors analysed here are physically manufactured; this article assumes they exist as catalog parts.
- [Electrical Systems](electrical-systems.md) — the voltage/current sources, wiring, and meters that excite and measure the circuits being analysed.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](index.md)*
