# Digital Logic

> **Node ID**: computing.digital-logic
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing`](./index.md), [`computing.electronic`](electronic.md), [`mathematics.formal-systems`](../mathematics/formal-systems.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-50
> **Outputs**: logic_gates, combinational_circuits, sequential_circuits, arithmetic_units, memory_elements


Every computation a processor performs reduces to operations on binary signals: voltage present or absent, stored charge or no charge. Digital logic provides the foundational building blocks that manipulate these binary states. Without a solid grasp of gate-level design, building anything from a simple counter to a full CPU is impossible. This page covers the theory and transistor-level implementation of the logic families, combinational circuits, sequential elements, and arithmetic units that form the hardware layer of all [computing](./index.md).

## Boolean Algebra Fundamentals

George Boole's 1854 algebra formalizes binary reasoning. Variables take values 0 or 1. Three basic operations underpin everything:

- **AND**: Output is 1 only when all inputs are 1. Symbol: A · B (or AB).
- **OR**: Output is 1 when any input is 1. Symbol: A + B.
- **NOT**: Output is the complement of the input. Symbol: Ā (or ¬A).

From these three, all other operations derive. Key identities: A · 0 = 0, A · 1 = A, A + 0 = A, A + 1 = 1, A · Ā = 0, A + Ā = 1. De Morgan's laws convert between AND and OR: (A · B)̄ = Ā + B̄ and (A + B)̄ = Ā · B̄. These laws are essential for simplifying circuits and converting between logic families.

**Derived gates**:

- **NAND**: (A · B)̄. A universal gate: any Boolean function can be implemented using NAND gates alone.
- **NOR**: (A + B)̄. Also universal.
- **[XOR](../glossary/xor.md)** (exclusive-OR): A ⊕ B = A·B̄ + Ā·B. Output is 1 when inputs differ. Used in parity checking and adders.
- **XNOR**: (A ⊕ B)̄. Output is 1 when inputs match. Used in comparators.

## Transistor-Level Implementation

## CMOS Inverter

The simplest CMOS gate uses two transistors: one PMOS (pull-up) and one NMOS (pull-down). Input high: NMOS conducts, output pulled to ground (0). Input low: PMOS conducts, output pulled to VDD (1). Static power consumption is near zero because one transistor is always off, preventing a direct path from VDD to ground. Switching power follows P = CV²f, where C is the load capacitance, V is supply voltage, and f is switching frequency.

**Strengths**:
- Near-zero static power: only one transistor conducts in either steady state
- Full rail-to-rail output swing (0V to VDD), providing maximum noise margin

**Weaknesses**:
- Dynamic power scales with frequency and capacitance (P = CV²f), limiting maximum clock speed at high densities
- Requires both NMOS and PMOS transistors, complicating the manufacturing process compared to single-type logic

## CMOS NAND Gate

A 2-input NAND uses 4 transistors: two PMOS in parallel (pull-up network) and two NMOS in series (pull-down network). When both inputs are high, both NMOS conduct, pulling output low. Any other combination leaves at least one NMOS off and at least one PMOS on, pulling output high. NAND is the workhorse of digital design because its transistor count is minimal and its output drives well.

**Strengths**:
- Universal gate: any Boolean function can be built from NAND gates alone, reducing inventory to one gate type
- Parallel PMOS pull-up provides strong drive current even with low supply voltage

**Weaknesses**:
- Series NMOS chain increases pull-down resistance — delays grow with the number of series transistors in multi-input variants
- Transistor count per gate (4 for 2-input) doubles the area of a single-transistor pass-gate

## CMOS NOR Gate

A 2-input NOR also uses 4 transistors: two PMOS in series and two NMOS in parallel. When any input is high, the corresponding NMOS conducts, pulling output low. Output is high only when all inputs are low.

**Strengths**:
- Simple implementation of the OR-NOT function with only 4 transistors
- Parallel NMOS pull-down provides fast discharge of the output node

**Weaknesses**:
- Series PMOS pull-up network is slower than the NAND's parallel PMOS, making NOR gates asymmetric in rise/fall times
- Not as widely used as NAND — fewer standard cell libraries optimize for NOR

## Transistor Sizing

In CMOS, PMOS transistors have roughly 2-3× lower carrier mobility than NMOS transistors. To match rise and fall times, PMOS transistors are made 2-3× wider than NMOS transistors. A minimum-size inverter might use W/L = 1 for NMOS and W/L = 2-3 for PMOS. Matching rise/fall times is critical for noise margin and timing predictability.

**Strengths**:
- Matched rise/fall times eliminate timing asymmetry that causes clock skew and data errors
- Proper sizing maximizes noise margin by equalizing the switching threshold near VDD/2

**Weaknesses**:
- Larger PMOS transistors consume more die area — a significant cost factor in billion-transistor chips
- Sizing must be re-optimized for each process node (mobility ratios change with technology scaling)

## Logic Families

Decision criteria: Use CMOS for any new design. Use TTL (74LS) only when interfacing with legacy systems or when CMOS is unavailable. Use 74HC (CMOS with TTL-compatible inputs) when mixing CMOS and TTL in the same system.

## Resistor-Transistor Logic (RTL)

The earliest integrated logic family (1960s). Uses a resistor at the collector and a transistor as a switch. NOR gate: two transistors share a collector resistor; either input high turns on its transistor, pulling output low. Slow (100 ns propagation), poor noise margin, high power dissipation. Fan-out limited to 3-5. Obsolete but historically important as the first IC logic family.

**Strengths**:
- Simplest transistor-based logic to build — only resistors and bipolar transistors, no diodes or multi-emitter structures
- Fewest components per gate at the time, enabling the first commercially viable integrated circuits

**Weaknesses**:
- 100 ns propagation delay limits clock speeds to under 5 MHz
- Fan-out of only 3-5 gates restricts circuit complexity; cascading stages degrades signal levels

## Diode-Transistor Logic (DTL)

Diodes perform the AND function, a transistor provides inversion and gain. Faster than RTL, better noise margin. Still limited by slow transistor turn-off (saturation storage time). Replaced by TTL in the mid-1960s.

**Strengths**:
- Diode inputs provide better noise immunity than RTL — input threshold is one diode drop (~0.7V) higher
- Higher fan-out (8) than RTL, supporting more complex circuits

**Weaknesses**:
- Transistor saturation storage time limits switching speed (~30 ns) compared to Schottky-clamped TTL
- Diode forward voltage drop reduces logic swing, eating into noise margin at low supply voltages

## Transistor-Transistor Logic (TTL)

The 74xx series defined digital electronics for three decades. Uses multi-emitter NPN transistors for input logic, a totem-pole output stage for active pull-up and pull-down. Standard TTL: 5V supply, 10 ns propagation delay, 10 mW per gate, fan-out of 10. Low-power Schottky (74LS): 5V, 9 ns, 2 mW, the most popular variant. TTL voltage levels: logic low below 0.8V, logic high above 2.0V, with a 1.2V noise margin in between.

**Strengths**:
- 10 ns propagation delay supports clock speeds up to 35 MHz — fast enough for early microprocessors
- Robust 1.2V noise margin and standardized 5V supply make TTL tolerant of breadboard prototyping with long wires

**Weaknesses**:
- 10 mW per gate static power (74xx) makes TTL impractical for VLSI — a 10,000-gate chip dissipates 100W
- Fixed 5V supply limits use in battery-powered and low-voltage systems

## CMOS Logic (4000 Series)

CD4000 series: supply voltage 3-15V, propagation delay ~50 ns at 5V (faster at higher voltage). Near-zero static power consumption (nanoamp leakage only). Output swings rail-to-rail. Fan-out virtually unlimited (input current is gate leakage, ~1 pA). The 74HC series later combined CMOS power advantages with TTL-compatible pinouts. Modern [computing](./index.md) runs entirely on CMOS due to its power efficiency at high densities.

**Strengths**:
- Near-zero static power enables billion-transistor chips without thermal overload
- Wide supply range (3-15V) and rail-to-rail output provide flexibility in power supply design

**Weaknesses**:
- 50 ns propagation delay at 5V is slower than TTL (10 ns), limiting use in high-speed applications at low voltage
- CMOS inputs are ESD-sensitive — gate oxide ruptures at ~100V discharge, requiring handling precautions

## Logic Family Comparison

| Family | Supply | Delay | Power/Gate | Fan-out | Best Use |
|--------|--------|-------|------------|---------|----------|
| RTL | 3.6V | 100 ns | 20 mW | 3-5 | Historical only |
| DTL | 5V | 30 ns | 10 mW | 8 | Historical only |
| TTL 74xx | 5V | 10 ns | 10 mW | 10 | Legacy glue logic |
| 74LS | 5V | 9 ns | 2 mW | 10 | Legacy prototyping |
| CMOS 4000 | 3-15V | 50 ns | ~0 static | 50+ | Low-power, wide supply |
| 74HC | 2-6V | 8 ns | ~0 static | 50+ | General-purpose new design |

## Combinational Logic Design

## Truth Tables and Boolean Expressions

Every combinational function is fully specified by its truth table: a list of all input combinations and the corresponding output. For n inputs, the table has 2ⁿ rows. The Boolean expression is read directly from rows where the output is 1 (sum-of-products, SOP) or 0 (product-of-sums, POS).

## Karnaugh Maps

A Karnaugh map (K-map) arranges truth table outputs in a grid where adjacent cells differ by exactly one variable. Groups of 1, 2, 4, 8... adjacent cells can be combined, eliminating variables. A group of 4 cells eliminates 2 variables. The goal is to cover all the 1s with the fewest largest groups, yielding a minimized expression. For 4 variables, the K-map is a 4×4 grid. Beyond 6 variables, K-maps become impractical and algorithmic methods (Quine-McCluskey) are used.

## SOP and POS Forms

Sum-of-products: OR together multiple AND terms (minterms). Directly maps to NAND-NAND implementation. Product-of-sums: AND together multiple OR terms (maxterms). Maps to NOR-NOR implementation. The minimized form determines the gate count and propagation delay of the final circuit.

## Sequential Logic

Combinational logic has no memory. Sequential logic adds state through feedback. For timing and clock generation in sequential systems, see [electronic circuits](electronic.md).

## SR Latch

Two cross-coupled NAND gates form the simplest memory element. Set (S=0) forces Q=1. Reset (R=0) forces Q=0. S=R=1 holds the previous state. The forbidden state S=R=0 drives both outputs high, and when both inputs return to 1 simultaneously, the final state is unpredictable (race condition). The SR latch is the building block for all sequential circuits.

**Strengths**:
- Only 2 gates (4 transistors in CMOS) — the smallest possible memory element
- Asynchronous: no clock required, state changes immediately on input transitions

**Weaknesses**:
- Forbidden state (S=R=0 for NAND-based, S=R=1 for NOR-based) causes indeterminate output
- No timing control — susceptible to glitches and races in combinatorial feedback paths

## Gated D Latch

An SR latch with an enable (clock) input and a single data input. When the clock is high, Q follows D. When the clock goes low, Q holds the last value. Transparent during the high phase, which can cause instability in cascaded designs.

**Strengths**:
- Single data input eliminates the forbidden state problem of the SR latch
- Simple to build — only 4 NAND gates plus an inverter (10 transistors)

**Weaknesses**:
- Transparent during the high clock phase — cascaded latches can propagate changes through multiple stages in one clock cycle
- Level-sensitive design requires careful timing to avoid data corruption

## D Flip-Flop

Two D latches in master-slave configuration, clocked on opposite phases. The master latch samples D when clock is high; the slave updates Q when clock goes low. Output changes only on the clock edge (negative-edge-triggered). The D flip-flop is the standard register element in modern design. Setup time (data must be stable before clock edge) and hold time (data must remain stable after clock edge) are critical timing parameters. Typical setup: 1-3 ns, hold: 0.5-1 ns in 180nm CMOS.

**Strengths**:
- Edge-triggered: output changes only at clock edges, eliminating transparency issues of latches
- Standard element for all synchronous [logic design](logic-design.md) and [computer architecture](computer-architecture.md)

**Weaknesses**:
- Requires ~20 transistors (CMOS transmission-gate implementation), roughly 2× the area of a D latch
- Setup and hold time violations cause metastability — the output hovers between 0 and 1 for an indeterminate period

## JK Flip-Flop

A generalization of the SR that handles the previously forbidden state. J=K=1 toggles the output. Useful in counter designs. Largely replaced by D flip-flops in modern ASIC design because D flops use fewer transistors and scan-chain testing is simpler with D-type elements.

**Strengths**:
- No forbidden state — all input combinations produce defined behavior
- Toggle mode (J=K=1) enables direct construction of binary counters without external XOR feedback

**Weaknesses**:
- Requires more transistors than a D flip-flop for equivalent functionality
- Catching (ones-catching or zeros-catching) on asynchronous inputs can cause unintended state changes

## Register Files

An array of D flip-flops (or latches) addressed by a read/write address. A 32×8 register file stores 32 words of 8 bits each. Read: decode address, enable tri-state output from selected register. Write: decode address, gate clock to selected register. Register files are the fastest storage in a processor, accessed every cycle.

**Strengths**:
- Single-cycle read/write access — faster than any cache or main memory
- Addressable structure allows compact instruction set design (e.g., 3-operand instructions addressing any of 32 registers)

**Weaknesses**:
- Area scales linearly with register count × word width — a 32×32 register file requires 1024 flip-flops plus decode logic
- Read and write to the same address in one cycle requires a bypass (forwarding) network to avoid stale data

## Arithmetic Circuits

## Half Adder

Adds two single-bit numbers. Sum = A ⊕ B (XOR gate). Carry = A · B (AND gate). Two gates, no carry input from a previous stage.

**Strengths**:
- Only 2 gates (5 transistors in CMOS for XOR + AND) — minimal hardware
- No carry input simplifies the truth table to a 2-input function

**Weaknesses**:
- Cannot accept a carry input from a previous stage, making it useless as a standalone multi-bit adder
- No carry output suitable for chaining — full adders needed for any practical arithmetic

## Full Adder

Adds two bits plus a carry input. Sum = A ⊕ B ⊕ Cin. Carry out = (A · B) + (Cin · (A ⊕ B)). Implemented with two half adders and one OR gate (9 transistors in CMOS). The full adder is the fundamental building block of all multi-bit adders.

**Strengths**:
- Accepts carry input, enabling arbitrary-width addition by chaining full adders
- Carry-out signal propagates to the next stage, supporting ripple-carry and lookahead architectures

**Weaknesses**:
- Carry propagation through the XOR chain adds 2 gate delays per stage
- 9 transistors per bit — multi-bit adders consume significant area (72 transistors for 8-bit)

## Ripple Carry Adder

Chain N full adders: carry out of bit 0 feeds carry in of bit 1, and so on. For an 8-bit adder, the carry must ripple through all 8 stages. Propagation delay = N × t_carry, where t_carry is the carry propagation delay per stage (~2 gate delays). For a 32-bit adder at 10 ns per stage, worst-case delay is 320 ns. Simple but slow.

**Strengths**:
- Regular layout — identical full adder cells abut in a row, simplifying physical design
- Minimal area overhead: no extra logic beyond the N full adder cells

**Weaknesses**:
- O(N) delay — a 32-bit adder is 4× slower than an 8-bit adder, making ripple carry impractical for wide arithmetic above 8-16 bits
- Worst-case delay occurs when carry propagates through all stages (e.g., 011...1 + 100...0), making timing unpredictable

## Carry-Lookahead Adder

Precomputes carry signals using generate (G = A · B) and propagate (P = A ⊕ B) terms. Carry out of stage i: C_i+1 = G_i + P_i · C_i. By expanding recursively, all carries compute in parallel from the inputs, without waiting for ripple. A 4-bit lookahead unit computes all carries in 2 gate delays. Multi-bit adders chain lookahead blocks with group generate/propagate. Delay grows as log₂(N) rather than N. The standard approach for adders wider than 8 bits.

**Strengths**:
- O(log N) delay — a 32-bit carry-lookahead adder computes in ~6 gate delays vs. 64 for ripple carry
- Predictable worst-case delay, independent of operand values

**Weaknesses**:
- Generate/propagate logic fan-in increases with block size — a 4-bit lookahead block requires 5-input AND/OR gates
- Irregular layout compared to ripple carry, making physical design more complex

## Other Arithmetic Units

- **Comparator**: XOR-based bit comparison. Equality check: AND of all XNOR outputs. Magnitude comparison uses cascaded gate logic.
- **Multiplier**: Array multiplier uses N² AND gates plus adders. Booth encoding reduces partial products. Wallace tree compresses partial products in logarithmic depth.
- **ALU**: Combines adder, logic unit (AND, OR, XOR), and shifter with a multiplexed output selected by operation code. A 4-bit ALU (e.g., 74181) fits in a single IC.

## Memory Elements

## ROM (Read-Only Memory)

Permanent data stored during manufacturing. Mask-programmed ROM uses presence or absence of a transistor at each intersection. One-time programmable (OTP) ROM blows fuses to store data. Access time: 10-100 ns. Non-volatile. Used for firmware, lookup tables, and boot code.

**Strengths**:
- Non-volatile: data survives power loss — essential for boot code and firmware
- Access time of 10-100 ns is fast enough for instruction fetch in moderate-speed processors

**Weaknesses**:
- Mask-programmed ROM requires a custom fabrication mask per design — a new mask set costs $10,000-$100,000 at even modest nodes
- OTP ROM can only be written once — errors are permanent

## SRAM (Static Random-Access Memory)

Six transistors per cell: two cross-coupled inverters form a bistable latch, plus two access transistors connect the latch to bit lines. Read: precharge bit lines to VDD/2, assert word line, sense differential voltage. Write: drive bit lines to desired values, assert word line to overpower the latch. Fast access (1-10 ns). No refresh needed. Volatile (loses data when power is removed). Used for CPU caches and register files. Area: ~0.1 μm² per cell in 65nm process.

**Strengths**:
- 1-10 ns access time — the fastest writable memory technology
- No refresh required: data is stable as long as power is applied, simplifying the memory controller

**Weaknesses**:
- 6 transistors per cell (vs. 1 transistor + 1 capacitor for DRAM) makes SRAM 4-6× more expensive per bit
- Volatile: all data is lost on power failure; [data storage](data-storage.md) systems use SRAM only for caching

## DRAM (Dynamic Random-Access Memory)

One transistor plus one capacitor per cell. Data is stored as charge on the capacitor: charged = 1, discharged = 0. Charge leaks away through junction leakage (time constant ~10-100 ms), requiring periodic refresh (read and rewrite every row, typically every 64 ms). Slower than SRAM (30-70 ns access) but much denser and cheaper per bit. A 1Gb DRAM chip stores over one billion cells in ~50 mm². The dominant technology for main memory in all computing systems.

**Strengths**:
- 1T+1C cell is 4-6× denser than SRAM, enabling gigabit-capacity chips at low cost
- Standardized interface (DDR, LPDDR) enables commodity manufacturing and broad compatibility

**Weaknesses**:
- Refresh cycle (every 64 ms) consumes power and steals bus bandwidth — each refresh cycle pauses normal read/write operations
- 30-70 ns access latency is 3-10× slower than SRAM, requiring cache hierarchies to hide the delay

## Clock Distribution and Timing

## Clock Signal

A square wave (typically) that synchronizes all sequential elements. Duty cycle near 50% for edge-triggered designs. Clock frequency determines the maximum throughput of the processor. Modern processors run at 1-5 GHz.

## Setup and Hold Time

Every flip-flop requires its data input to be stable during a window around the clock edge. Setup time (t_su): data must be valid before the clock edge. Hold time (t_h): data must remain valid after the clock edge. Violation causes metastability, where the output hovers between 0 and 1 for an indeterminate period.

## Clock Skew

The clock signal arrives at different flip-flops at slightly different times due to wire length differences and buffer delays. Skew reduces the effective clock period. If clock skew exceeds the hold time, a flip-flop captures the wrong data. Managing skew requires balanced clock trees (H-tree or mesh topology) and careful layout. In a 5 GHz processor, the clock period is 200 ps, and skew must be kept below ~20 ps.

## Critical Path

The longest propagation path through combinational logic between two flip-flops determines the maximum clock frequency: f_max = 1 / (t_logic + t_su + t_skew). Pipeline stages break long combinational paths into shorter segments, raising f_max at the cost of latency (more clock cycles to complete an operation).

## Programmable Logic

## PAL (Programmable Array Logic)

A fixed OR array with a programmable AND array. The user configures which inputs connect to each AND term by blowing fuses (one-time programmable). Each output has a fixed number of product terms (typically 4-8). Fast (5-10 ns) but inflexible. The 16R8 PAL (8 outputs, 8 registered) was widely used for state machines and address decoding.

**Strengths**:
- 5-10 ns propagation delay — fast enough for address decoding and glue logic in microprocessor systems
- One-time programming is simple: no special development tools beyond a PAL programmer

**Weaknesses**:
- One-time programmable (fuse-based): design errors require discarding the device
- Fixed number of product terms per output (typically 4-8) limits logic complexity per macrocell

## GAL (Generic Array Logic)

Reprogrammable version of PAL using EEPROM cells instead of fuses. The 22V10 GAL (10 macrocells, 22 inputs) became the standard small programmable device. Each macrocell can be configured as combinational or registered output, with selectable polarity.

**Strengths**:
- Reprogrammable (EEPROM-based): design iterations do not consume devices
- Configurable macrocell (combinational or registered, selectable polarity) supports both state machine and combinatorial logic in one device

**Weaknesses**:
- 10 macrocells limit design complexity — insufficient for anything beyond simple state machines and address decoding
- EEPROM endurance of ~100 erase/write cycles limits the number of design iterations

## FPGA (Field-Programmable Gate Array)

An array of configurable logic blocks (CLBs) connected by a programmable routing matrix. Each CLB contains a lookup table (LUT, typically 4-6 input), a flip-flop, and multiplexers. Configuration stored in SRAM (volatile, loaded at power-up). Modern FPGAs contain millions of LUTs, embedded SRAM blocks, DSP multiplier units, and even hardened processor cores. FPGAs bridge the gap between software flexibility and ASIC performance: configure the hardware for a specific task, reconfigure when requirements change. The bootstrapping path can use FPGAs to prototype processor designs before committing to mask-programmed ASICs.

**Strengths**:
- Reconfigurable in seconds: design changes require no fabrication — upload a new bitstream
- Millions of logic elements enable prototyping entire processor architectures, including the [computer architecture](computer-architecture.md) pipeline

**Weaknesses**:
- SRAM-based configuration is volatile — bitstream must be reloaded from external flash on every power-up
- 10-20× slower and 10-50× less dense than an equivalent ASIC, limiting performance and cost-effectiveness in volume production

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



[← Back to Computing](index.md)
