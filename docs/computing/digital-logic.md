# Digital Logic

> **Node ID**: computing.digital-logic
> **Domain**: [Computing](./index.md)
> **Dependencies**: `semiconductors`, `electrical-systems`
> **Timeline**: Years 40-50
> **Outputs**: logic_gates, combinational_circuits, sequential_circuits, arithmetic_units, memory_elements

## Problem

Every computation a processor performs reduces to operations on binary signals: voltage present or absent, stored charge or no charge. Digital logic provides the foundational building blocks that manipulate these binary states. Without a solid grasp of gate-level design, building anything from a simple counter to a full CPU is impossible. This page covers the theory and transistor-level implementation of the logic families, combinational circuits, sequential elements, and arithmetic units that form the hardware layer of all computing.

## Boolean Algebra Fundamentals

George Boole's 1854 algebra formalizes binary reasoning. Variables take values 0 or 1. Three basic operations underpin everything:

- **AND**: Output is 1 only when all inputs are 1. Symbol: A · B (or AB).
- **OR**: Output is 1 when any input is 1. Symbol: A + B.
- **NOT**: Output is the complement of the input. Symbol: Ā (or ¬A).

From these three, all other operations derive. Key identities: A · 0 = 0, A · 1 = A, A + 0 = A, A + 1 = 1, A · Ā = 0, A + Ā = 1. De Morgan's laws convert between AND and OR: (A · B)̄ = Ā + B̄ and (A + B)̄ = Ā · B̄. These laws are essential for simplifying circuits and converting between logic families.

**Derived gates**:

- **NAND**: (A · B)̄. A universal gate: any Boolean function can be implemented using NAND gates alone.
- **NOR**: (A + B)̄. Also universal.
- **[XOR](../glossary/xor.html)** (exclusive-OR): A ⊕ B = A·B̄ + Ā·B. Output is 1 when inputs differ. Used in parity checking and adders.
- **XNOR**: (A ⊕ B)̄. Output is 1 when inputs match. Used in comparators.

## Transistor-Level Implementation

### CMOS Inverter

The simplest CMOS gate uses two transistors: one PMOS (pull-up) and one NMOS (pull-down). Input high: NMOS conducts, output pulled to ground (0). Input low: PMOS conducts, output pulled to VDD (1). Static power consumption is near zero because one transistor is always off, preventing a direct path from VDD to ground. Switching power follows P = CV²f, where C is the load capacitance, V is supply voltage, and f is switching frequency.

### CMOS NAND Gate

A 2-input NAND uses 4 transistors: two PMOS in parallel (pull-up network) and two NMOS in series (pull-down network). When both inputs are high, both NMOS conduct, pulling output low. Any other combination leaves at least one NMOS off and at least one PMOS on, pulling output high. NAND is the workhorse of digital design because its transistor count is minimal and its output drives well.

### CMOS NOR Gate

A 2-input NOR also uses 4 transistors: two PMOS in series and two NMOS in parallel. When any input is high, the corresponding NMOS conducts, pulling output low. Output is high only when all inputs are low.

### Transistor Sizing

In CMOS, PMOS transistors have roughly 2-3× lower carrier mobility than NMOS transistors. To match rise and fall times, PMOS transistors are made 2-3× wider than NMOS transistors. A minimum-size inverter might use W/L = 1 for NMOS and W/L = 2-3 for PMOS. Matching rise/fall times is critical for noise margin and timing predictability.

## Logic Families

### Resistor-Transistor Logic (RTL)

The earliest integrated logic family (1960s). Uses a resistor at the collector and a transistor as a switch. NOR gate: two transistors share a collector resistor; either input high turns on its transistor, pulling output low. Slow (100 ns propagation), poor noise margin, high power dissipation. Fan-out limited to 3-5. Obsolete but historically important as the first IC logic family.

### Diode-Transistor Logic (DTL)

Diodes perform the AND function, a transistor provides inversion and gain. Faster than RTL, better noise margin. Still limited by slow transistor turn-off (saturation storage time). Replaced by TTL in the mid-1960s.

### Transistor-Transistor Logic (TTL)

The 74xx series defined digital electronics for three decades. Uses multi-emitter NPN transistors for input logic, a totem-pole output stage for active pull-up and pull-down. Standard TTL: 5V supply, 10 ns propagation delay, 10 mW per gate, fan-out of 10. Low-power Schottky (74LS): 5V, 9 ns, 2 mW, the most popular variant. TTL voltage levels: logic low below 0.8V, logic high above 2.0V, with a 1.2V noise margin in between.

### CMOS Logic (4000 Series)

CD4000 series: supply voltage 3-15V, propagation delay ~50 ns at 5V (faster at higher voltage). Near-zero static power consumption (nanoamp leakage only). Output swings rail-to-rail. Fan-out virtually unlimited (input current is gate leakage, ~1 pA). The 74HC series later combined CMOS power advantages with TTL-compatible pinouts. Modern computing runs entirely on CMOS due to its power efficiency at high densities.

### Logic Family Comparison

| Family | Supply | Delay | Power/Gate | Fan-out |
|--------|--------|-------|------------|---------|
| RTL | 3.6V | 100 ns | 20 mW | 3-5 |
| DTL | 5V | 30 ns | 10 mW | 8 |
| TTL 74xx | 5V | 10 ns | 10 mW | 10 |
| 74LS | 5V | 9 ns | 2 mW | 10 |
| CMOS 4000 | 3-15V | 50 ns | ~0 static | 50+ |
| 74HC | 2-6V | 8 ns | ~0 static | 50+ |

## Combinational Logic Design

### Truth Tables and Boolean Expressions

Every combinational function is fully specified by its truth table: a list of all input combinations and the corresponding output. For n inputs, the table has 2ⁿ rows. The Boolean expression is read directly from rows where the output is 1 (sum-of-products, SOP) or 0 (product-of-sums, POS).

### Karnaugh Maps

A Karnaugh map (K-map) arranges truth table outputs in a grid where adjacent cells differ by exactly one variable. Groups of 1, 2, 4, 8... adjacent cells can be combined, eliminating variables. A group of 4 cells eliminates 2 variables. The goal is to cover all the 1s with the fewest largest groups, yielding a minimized expression. For 4 variables, the K-map is a 4×4 grid. Beyond 6 variables, K-maps become impractical and algorithmic methods (Quine-McCluskey) are used.

### SOP and POS Forms

Sum-of-products: OR together multiple AND terms (minterms). Directly maps to NAND-NAND implementation. Product-of-sums: AND together multiple OR terms (maxterms). Maps to NOR-NOR implementation. The minimized form determines the gate count and propagation delay of the final circuit.

## Sequential Logic

Combinational logic has no memory. Sequential logic adds state through feedback.

### SR Latch

Two cross-coupled NAND gates form the simplest memory element. Set (S=0) forces Q=1. Reset (R=0) forces Q=0. S=R=1 holds the previous state. The forbidden state S=R=0 drives both outputs high, and when both inputs return to 1 simultaneously, the final state is unpredictable (race condition). The SR latch is the building block for all sequential circuits.

### Gated D Latch

An SR latch with an enable (clock) input and a single data input. When the clock is high, Q follows D. When the clock goes low, Q holds the last value. Transparent during the high phase, which can cause instability in cascaded designs.

### D Flip-Flop

Two D latches in master-slave configuration, clocked on opposite phases. The master latch samples D when clock is high; the slave updates Q when clock goes low. Output changes only on the clock edge (negative-edge-triggered). The D flip-flop is the standard register element in modern design. Setup time (data must be stable before clock edge) and hold time (data must remain stable after clock edge) are critical timing parameters. Typical setup: 1-3 ns, hold: 0.5-1 ns in 180nm CMOS.

### JK Flip-Flop

A generalization of the SR that handles the previously forbidden state. J=K=1 toggles the output. Useful in counter designs. Largely replaced by D flip-flops in modern ASIC design because D flops use fewer transistors and scan-chain testing is simpler with D-type elements.

### Register Files

An array of D flip-flops (or latches) addressed by a read/write address. A 32×8 register file stores 32 words of 8 bits each. Read: decode address, enable tri-state output from selected register. Write: decode address, gate clock to selected register. Register files are the fastest storage in a processor, accessed every cycle.

## Arithmetic Circuits

### Half Adder

Adds two single-bit numbers. Sum = A ⊕ B (XOR gate). Carry = A · B (AND gate). Two gates, no carry input from a previous stage.

### Full Adder

Adds two bits plus a carry input. Sum = A ⊕ B ⊕ Cin. Carry out = (A · B) + (Cin · (A ⊕ B)). Implemented with two half adders and one OR gate (9 transistors in CMOS). The full adder is the fundamental building block of all multi-bit adders.

### Ripple Carry Adder

Chain N full adders: carry out of bit 0 feeds carry in of bit 1, and so on. For an 8-bit adder, the carry must ripple through all 8 stages. Propagation delay = N × t_carry, where t_carry is the carry propagation delay per stage (~2 gate delays). For a 32-bit adder at 10 ns per stage, worst-case delay is 320 ns. Simple but slow.

### Carry-Lookahead Adder

Precomputes carry signals using generate (G = A · B) and propagate (P = A ⊕ B) terms. Carry out of stage i: C_i+1 = G_i + P_i · C_i. By expanding recursively, all carries compute in parallel from the inputs, without waiting for ripple. A 4-bit lookahead unit computes all carries in 2 gate delays. Multi-bit adders chain lookahead blocks with group generate/propagate. Delay grows as log₂(N) rather than N. The standard approach for adders wider than 8 bits.

### Other Arithmetic Units

- **Comparator**: XOR-based bit comparison. Equality check: AND of all XNOR outputs. Magnitude comparison uses cascaded gate logic.
- **Multiplier**: Array multiplier uses N² AND gates plus adders. Booth encoding reduces partial products. Wallace tree compresses partial products in logarithmic depth.
- **ALU**: Combines adder, logic unit (AND, OR, XOR), and shifter with a multiplexed output selected by operation code. A 4-bit ALU (e.g., 74181) fits in a single IC.

## Memory Elements

### ROM (Read-Only Memory)

Permanent data stored during manufacturing. Mask-programmed ROM uses presence or absence of a transistor at each intersection. One-time programmable (OTP) ROM blows fuses to store data. Access time: 10-100 ns. Non-volatile. Used for firmware, lookup tables, and boot code.

### SRAM (Static Random-Access Memory)

Six transistors per cell: two cross-coupled inverters form a bistable latch, plus two access transistors connect the latch to bit lines. Read: precharge bit lines to VDD/2, assert word line, sense differential voltage. Write: drive bit lines to desired values, assert word line to overpower the latch. Fast access (1-10 ns). No refresh needed. Volatile (loses data when power is removed). Used for CPU caches and register files. Area: ~0.1 μm² per cell in 65nm process.

### DRAM (Dynamic Random-Access Memory)

One transistor plus one capacitor per cell. Data is stored as charge on the capacitor: charged = 1, discharged = 0. Charge leaks away through junction leakage (time constant ~10-100 ms), requiring periodic refresh (read and rewrite every row, typically every 64 ms). Slower than SRAM (30-70 ns access) but much denser and cheaper per bit. A 1Gb DRAM chip stores over one billion cells in ~50 mm². The dominant technology for main memory in all computing systems.

## Clock Distribution and Timing

### Clock Signal

A square wave (typically) that synchronizes all sequential elements. Duty cycle near 50% for edge-triggered designs. Clock frequency determines the maximum throughput of the processor. Modern processors run at 1-5 GHz.

### Setup and Hold Time

Every flip-flop requires its data input to be stable during a window around the clock edge. Setup time (t_su): data must be valid before the clock edge. Hold time (t_h): data must remain valid after the clock edge. Violation causes metastability, where the output hovers between 0 and 1 for an indeterminate period.

### Clock Skew

The clock signal arrives at different flip-flops at slightly different times due to wire length differences and buffer delays. Skew reduces the effective clock period. If clock skew exceeds the hold time, a flip-flop captures the wrong data. Managing skew requires balanced clock trees (H-tree or mesh topology) and careful layout. In a 5 GHz processor, the clock period is 200 ps, and skew must be kept below ~20 ps.

### Critical Path

The longest propagation path through combinational logic between two flip-flops determines the maximum clock frequency: f_max = 1 / (t_logic + t_su + t_skew). Pipeline stages break long combinational paths into shorter segments, raising f_max at the cost of latency (more clock cycles to complete an operation).

## Programmable Logic

### PAL (Programmable Array Logic)

A fixed OR array with a programmable AND array. The user configures which inputs connect to each AND term by blowing fuses (one-time programmable). Each output has a fixed number of product terms (typically 4-8). Fast (5-10 ns) but inflexible. The 16R8 PAL (8 outputs, 8 registered) was widely used for state machines and address decoding.

### GAL (Generic Array Logic)

Reprogrammable version of PAL using EEPROM cells instead of fuses. The 22V10 GAL (10 macrocells, 22 inputs) became the standard small programmable device. Each macrocell can be configured as combinational or registered output, with selectable polarity.

### FPGA (Field-Programmable Gate Array)

An array of configurable logic blocks (CLBs) connected by a programmable routing matrix. Each CLB contains a lookup table (LUT, typically 4-6 input), a flip-flop, and multiplexers. Configuration stored in SRAM (volatile, loaded at power-up). Modern FPGAs contain millions of LUTs, embedded SRAM blocks, DSP multiplier units, and even hardened processor cores. FPGAs bridge the gap between software flexibility and ASIC performance: configure the hardware for a specific task, reconfigure when requirements change. The bootstrapping path can use FPGAs to prototype processor designs before committing to mask-programmed ASICs.

## Construction Notes

Building digital logic from discrete transistors is educational but impractical for any useful system. A single 8-bit ALU requires hundreds of transistors. The practical path runs through SSI (small-scale integration) ICs (gates, flip-flops in 14-16 pin DIP packages) for prototyping, then CPLD or FPGA for medium complexity, then custom ASIC for volume production. For bootstrapping purposes, TTL or CMOS SSI/MSI chips (74xx series) provide immediate access to working logic. Design entry starts with schematic capture, moves to hardware description languages (Verilog, VHDL) for anything beyond a handful of chips.

## Key Deliverables

- Working logic gates (NAND, NOR, AND, OR, XOR, NOT) in available logic family
- Combinational building blocks: multiplexers, decoders, comparators
- Sequential elements: SR latches, D flip-flops, registers
- Arithmetic: full adders, carry-lookahead adders, ALU
- Memory: SRAM arrays, DRAM controller, ROM
- Clock distribution network with acceptable skew
- Programmable logic (PAL/GAL for glue logic, FPGA for prototyping)

## Safety & Hazards

- **Electrostatic discharge (ESD)**: CMOS inputs are protected by diode clamps but remain sensitive. A 100V discharge (imperceptible to humans) destroys gate oxide in NMOS/PMOS transistors. Handle all ICs on grounded mats with wrist straps. Store in conductive foam or antistatic bags. Never insert or remove ICs with power applied.
- **Supply voltage**: TTL is strictly 5V ±0.25V. CMOS tolerates wider ranges but exceeding maximum VDD (7V for HC, 15V for 4000 series) causes latchup, a parasitic thyristor fires and shorts VDD to ground, destroying the chip instantly. Current-limited bench supplies (100-200 mA) limit damage during prototyping.
- **Heat**: An IC running at elevated temperature has increased propagation delay and leakage current. Junction temperature above 150°C causes irreversible damage. For prototyping on breadboards, limit power dissipation to ~0.5W per IC. Production designs use thermal analysis and heatsinking.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Computing](./index.md) · [All Domains](../index.md)*

[← Back to Computing](index.md)
