# Logic Design

> **Node ID**: computing.logic-design
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing.digital-logic`](digital-logic.md), [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md), [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md)
> **Enables**: [`computing.computer-architecture`](computer-architecture.md), [`computing.embedded-systems`](embedded-systems.md)
> **Timeline**: Years 45-60
> **Outputs**: combinational_circuits, sequential_circuits, state_machines, programmable_logic
> **Critical**: Yes — all digital hardware from microcontrollers to GPUs requires systematic logic design

## 1. Overview

Logic design is the engineering discipline of transforming Boolean algebra into physical circuits that perform computation. Where [`computing.digital-logic`](digital-logic.md) covers the physics of individual gates and arithmetic units at the transistor level, logic design addresses the system-level problem: how to organize thousands to billions of gates into correct, timing-compliant, testable digital systems.

The distinction matters. A single NAND gate is a device; a 32-bit carry-lookahead adder built from 1,400 NAND gates is a design. Logic design provides the methodology — Karnaugh maps, state machine encoding, HDL specification, timing analysis — that scales from hand-wired TTL prototypes to billion-transistor ASICs. Without systematic logic design, complex digital systems accumulate timing violations, undetected states, and untestable paths.

Logic design sits between gate-level physics (digital-logic) and processor-level organization (computer-architecture). It enables [`computing.computer-architecture`](computer-architecture.md) by providing the building-block design methodology, and it enables [`computing.embedded-systems`](embedded-systems.md) by providing the FPGA and CPLD design flow used in embedded control hardware.

**Boundary with software-bootstrapping**: This document covers hardware logic design — the physical arrangement of gates, flip-flops, and interconnects. HDL programming (Verilog/VHDL coding, testbench methodology, simulation) is a software activity covered in the software-bootstrapping domain. The boundary: gate-level timing and physical implementation lives here; HDL source code and simulation scripts live there.

## 2. Prerequisites

### Materials

- Semiconductor devices: diodes, BJTs, MOSFETs from [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md)
- Passive components: resistors, capacitors for pull-ups, decoupling, timing from [`electronics.passive-components`](../electronics/passive-components.md)
- Printed circuit boards from [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md)
- Logic ICs: TTL 74xx series or CMOS 4000/74HC series (requires semiconductor fab or trade)

### Tools and Equipment

- Oscilloscope (50+ MHz bandwidth for TTL timing verification)
- Logic analyzer (16+ channels for bus debugging)
- Breadboard or wire-wrap prototyping boards
- Soldering station (temperature-controlled, 25-80 W)
- Multimeter for continuity and voltage checks

### Knowledge

- Boolean algebra and De Morgan's laws (see [`computing.digital-logic`](digital-logic.md))
- Binary number representation (two's complement, fixed-point)
- Basic circuit analysis (Ohm's law, RC time constants)
- Clock discipline: setup/hold times, propagation delay

## 3. Bill of Materials

| Material | Quantity (per prototyping board) | Source | Alternatives |
|----------|----------------------------------|--------|-------------|
| TTL 74LS00 NAND gates | 10-20 ICs | [`electronics.assembly`](../electronics/assembly.md) — off-the-shelf or fabricated | CMOS 74HC00 (lower power, wider voltage range) |
| TTL 74LS86 XOR gates | 4-8 ICs | Semiconductor fab + packaging | Discrete transistor XOR (4× component count) |
| TTL 74LS74 D flip-flops | 8-16 ICs | Semiconductor fab + packaging | Cross-coupled NAND latch + clock gating |
| TTL 74LS283 4-bit adder | 2-4 ICs | Semiconductor fab + packaging | Ripple carry from full adders (slower) |
| 10 kΩ pull-up resistor array | 2-4 SIP packages | [`electronics.passive-components`](../electronics/passive-components.md) | Individual 10 kΩ resistors (4× board space) |
| 100 nF ceramic decoupling caps | 20-40 pieces | [`electronics.passive-components`](../electronics/passive-components.md) | 10 nF (marginal for high-speed switching) |
| Crystal oscillator (1-10 MHz) | 1 piece | Piezoelectric quartz crystal + amplifier circuit | RC relaxation oscillator (±20% stability) |
| Prototyping PCB or breadboard | 1 board | [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) | Wire-wrap board (reliable for DIP ICs) |
| 5V regulated power supply (1A) | 1 unit | [`electronics.power-electronics`](../electronics/power-electronics.md) | 7805 voltage regulator + transformer |

## 4. Process Description

### 4.1 Combinational Circuit Design

1. **Write the truth table.** List all 2ⁿ input combinations and the desired output for each. For a 4-input function, this is a 16-row table.

2. **Plot the Karnaugh map.** Transfer truth table outputs to the K-map grid. For 4 variables (A, B, C, D), arrange as a 4×4 grid where Gray code ordering ensures adjacent cells differ by one variable.

3. **Group the 1s.** Circle groups of 1, 2, 4, 8 adjacent cells. Each group eliminates variables. The goal: minimum number of largest possible groups covering all 1s. Don't-care entries (X) can be included in groups to enlarge them.

4. **Read the minimized expression.** Each group produces one AND term. Variables that change within the group are eliminated. The final expression is the OR of all group terms (sum-of-products form).

5. **Map to gate implementation.** SOP directly maps to NAND-NAND implementation (AND-OR equivalent). POS maps to NOR-NOR. Choose the form requiring fewer gates. Count total gate inputs as a proxy for transistor count.

6. **Verify with a test bench.** Apply all input combinations to the physical circuit. Compare measured outputs against the truth table. For 8+ input circuits (256+ rows), use a logic analyzer in automated stimulus mode.

### 4.2 Sequential Circuit Design

1. **Define the state diagram.** Draw circles for each state, arrows for transitions. Label each arrow with the input condition that triggers the transition and the output produced.

2. **Create the state table.** Tabulate: current state, input, next state, output. For N states and M inputs, the table has N × 2ᴹ rows.

3. **State encoding.** Assign binary codes to each state. Options:
   - **Binary encoding**: ⌈log₂ N⌉ flip-flops. Minimum flip-flops, maximum decoding logic.
   - **One-hot encoding**: N flip-flops, one bit per state. More flip-flops but simpler next-state logic. Standard for FPGA designs.
   - **Gray code encoding**: Adjacent states differ by one bit. Reduces glitching on state transitions.

4. **Derive next-state and output equations.** Use K-maps on the state table columns. Each flip-flop input (D) gets its own minimized equation. Each output gets its own equation.

5. **Implement and verify.** Wire the flip-flops, combinational next-state logic, and output logic. Test by stepping through all states manually (single-step clock) and at speed.

### 4.3 Programmable Logic Design Flow (FPGA/CPLD)

1. **Write HDL description.** Specify the design in a hardware description language (Verilog or VHDL). This is a software activity — see software-bootstrapping domain for HDL methodology.

2. **Synthesize.** The synthesis tool maps HDL constructs to the target device's lookup tables (FPGA) or macrocells (CPLD). Produces a netlist of primitive elements.

3. **Place and route.** Assign each logic element to a physical location on the device. Route interconnects through the programmable routing matrix. Critical path determines maximum clock frequency.

4. **Timing analysis.** Static timing analysis checks all paths against the clock period constraint. Setup and hold violations are flagged. The slowest path (critical path) sets f_max = 1 / (t_logic + t_su + t_clk_skew).

5. **Generate bitstream and program.** The place-and-route result generates a configuration bitstream. Load into the FPGA via JTAG or serial programming interface. For CPLDs, the configuration is non-volatile (EEPROM/flash).

## 5. Quantitative Parameters

### Gate-Level Timing

| Parameter | 74LS TTL | 74HC CMOS | 4000 CMOS | 180nm ASIC |
|-----------|----------|-----------|-----------|------------|
| Propagation delay (per gate) | 9 ns | 8 ns | 50 ns | 0.05 ns |
| Max clock frequency | 30-50 MHz | 50-80 MHz | 5-10 MHz | 1+ GHz |
| Supply voltage | 5V ±0.25V | 2-6V | 3-15V | 1.2-1.8V |
| Power per gate (static) | 2 mW | ~0 nW | ~0 nW | ~0.1 nW |
| Power per gate (dynamic) | 2 mW | CV²f | CV²f | CV²f |
| Fan-out | 10 | 50+ | 50+ | — |

### State Machine Encoding Comparison

| Encoding | Flip-flops (8 states) | Next-state logic | Decoding logic | Use case |
|----------|-----------------------|------------------|----------------|----------|
| Binary | 3 | Moderate | Moderate | General purpose |
| One-hot | 8 | Minimal | Minimal | FPGA (LUT-optimized) |
| Gray code | 3 | Moderate | Minimal | Low-glitch, async interfaces |

### Programmable Logic Device Comparison

| Device | Logic capacity | Max f_max | I/O pins | Configuration | Cost/unit |
|--------|---------------|-----------|----------|---------------|-----------|
| GAL 22V10 | 10 macrocells | 100 MHz | 22 | EEPROM (non-volatile) | $1-2 |
| CPLD (XC9500) | 72 macrocells | 178 MHz | 72 | Flash (non-volatile) | $5-15 |
| FPGA (Spartan-6) | 147K logic cells | 400 MHz | 300+ | SRAM (volatile) | $15-50 |
| FPGA (Artix-7) | 350K logic cells | 450 MHz | 500+ | SRAM (volatile) | $30-100 |

### Truth Table Sizes and K-map Limits

| Inputs (n) | Truth table rows | K-map dimensions | Practical? |
|-------------|-----------------|------------------|------------|
| 2 | 4 | 2×2 | Yes |
| 3 | 8 | 2×4 | Yes |
| 4 | 16 | 4×4 | Yes (standard) |
| 5 | 32 | 2×(4×4) | Difficult |
| 6 | 64 | 4×(4×4) | Impractical |
| 7+ | 128+ | — | Use Quine-McCluskey algorithm |

## 6. Scaling Notes

**From TTL prototype to FPGA**: A design prototyped with 50 TTL ICs on a breadboard (500 gates, 200 MHz max) translates to a single CPLD or small FPGA. The HDL rewrite replaces physical wiring with synthesizable code. Timing constraints change from gate propagation delays (ns) to place-and-route delays (ps to ns).

**From FPGA to ASIC**: An FPGA design targeting ASIC implementation requires:
- Replacing FPGA-specific primitives (LUTs, block RAM) with standard cell library equivalents
- Adding scan chains for manufacturing test (DFT — design for test)
- Clock tree synthesis (balanced H-tree distribution, 20 ps skew target)
- Power grid design (IR drop analysis, electromigration checks)
- The same HDL source targets both FPGA and ASIC with conditional compilation

**Critical path optimization**: At FPGA scale, the critical path determines performance. Techniques:
- Pipeline long combinational paths (add registers between stages)
- Retiming (move registers across combinational logic to balance stage delays)
- Use carry chains for arithmetic (dedicated fast routing in FPGA fabric)
- ASIC: custom cell sizing on the critical path, wider transistors for faster switching

**Minimum useful scale**: A single GAL 22V10 (10 macrocells) implements a state machine with up to 10 states plus combinational glue logic. This is the entry point for programmable logic design. Below this, use discrete TTL/CMOS gates.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Random output glitches on combinational outputs | Hazards due to unequal path delays through the logic | Add redundant consensus terms to cover hazard-producing transitions; or register outputs (synchronize to clock) |
| State machine enters wrong state | Setup/hold time violation on flip-flop inputs | Check clock-to-Q delay + combinational delay against clock period; add flip-flop to synchronize asynchronous inputs |
| Circuit works at low speed, fails at high speed | Critical path exceeds clock period | Reduce clock frequency or pipeline the long path; check datasheet propagation delays against design calculations |
| Excessive power consumption in CMOS design | Floating inputs causing mid-rail oscillation | Tie all unused inputs to VDD or GND; never leave CMOS inputs floating |
| Race condition in asynchronous design | Multiple paths with different delays to same element | Synchronize all signals to a single clock; avoid asynchronous reset/set unless absolutely necessary |
| FPGA configuration fails | Incorrect bitstream format or voltage levels on JTAG pins | Verify bitstream matches device and revision; check VCCIO voltage matches programming adapter |

## 8. Safety

- **Electrostatic discharge (ESD)**: CMOS inputs are protected by diode clamps but remain sensitive. A 100 V discharge (imperceptible to humans) destroys gate oxide. Handle all ICs on grounded mats with wrist straps. Store in conductive foam. Damage is cumulative — even sub-lethal discharges degrade reliability.
- **Supply voltage**: TTL is strictly 5V ±0.25V. CMOS tolerates wider ranges but exceeding maximum VDD (7V for HC, 15V for 4000 series) causes latchup — a parasitic thyristor fires, shorting VDD to ground, destroying the chip. Use current-limited bench supplies (100-200 mA) during prototyping.
- **Ground loops**: In mixed analog/digital prototyping, ground loops inject noise into sensitive logic inputs. Use a single ground point (star ground) for all power supply returns. Keep digital ground currents separate from analog ground returns.
- **Hot insertion**: Never insert or remove ICs with power applied. The momentary short between adjacent pins as the IC enters the socket can destroy both the IC and the socket. Power off, insert, then power on.

## 9. Quality Control

### Functional Verification

- **Truth table check**: Apply all input combinations to combinational circuits. Verify every output against the specification. For a 4-input circuit, this is 16 tests. Automate with a logic analyzer in stimulus-response mode.
- **State machine coverage**: Walk through every state transition in the state diagram. Verify correct next state and output for each transition. Use a logic analyzer to capture state sequences. A fully verified state machine covers all (state, input) pairs.

### Timing Verification

- **Propagation delay measurement**: Use an oscilloscope to measure the delay from input transition to output transition. Compare against the worst-case specification in the datasheet. Add 10-20% margin for temperature and voltage variation.
- **Setup/hold margin check**: Measure the time from data valid to clock edge (setup) and from clock edge to data change (hold). Setup margin must be positive and exceed the flip-flop's t_su specification. Hold margin must exceed t_h.

### Testability

- **Scan chain insertion** (ASIC): Replace each flip-flop with a scan flip-flop that can be chained into a serial shift register. In test mode, shift in any desired state, apply one clock, shift out the resulting state. Full controllability and observability of all flip-flops.
- **Boundary scan (JTAG)**: IEEE 1149.1 standard. Shift register around the IC perimeter allows testing board-level interconnections without physical probes. Supported by all modern FPGAs and complex ICs.

## 10. Variations and Alternatives

### Discrete Gate Implementation

Build combinational and sequential logic from individual SSI/MSI TTL or CMOS ICs. Each 14-pin DIP package contains 4 gates (NAND, NOR, XOR) or 2 flip-flops. A 32-bit counter requires 8 ICs. Practical for prototyping and low-volume production. Maximum complexity: ~100 ICs on a single board before wire management becomes unmanageable.

### Programmable Logic (GAL/CPLD)

Replace discrete glue logic with a single programmable device. A GAL 22V10 replaces up to 10 discrete ICs. EEPROM-based configuration is non-volatile (retains programming without power). In-system programmable (ISP) via JTAG. Ideal for state machines, address decoders, and interface glue logic.

### FPGA Implementation

Map the entire design to a field-programmable gate array. SRAM-based configuration allows infinite reprogramming. Modern FPGAs contain 10K to 10M+ logic elements, embedded RAM, DSP multipliers, and hardened I/O interfaces (PCIe, Ethernet, DDR memory controllers). The standard platform for digital prototyping and medium-volume production.

### ASIC Implementation

Commit the design to a custom silicon fabrication. Highest performance, lowest per-unit cost at volume (>100K units), but highest NRE (non-recurring engineering) cost ($100K-$10M for mask sets). The final step in the scaling path: prototype on FPGA, verify, then commit to ASIC for production.

### Design Methodology Comparison

| Method | Time to prototype | Unit cost | Max complexity | Performance |
|--------|-------------------|-----------|----------------|-------------|
| Discrete TTL | Hours-days | $5-50 | ~500 gates | 30-50 MHz |
| GAL/CPLD | Hours | $2-15 | ~200 macrocells | 100-200 MHz |
| FPGA | Days-weeks | $15-100 | 10K-10M logic elements | 200-500 MHz |
| ASIC | Months | $0.50-5 (at volume) | Unlimited | 1+ GHz |

## 11. References

- [`computing.digital-logic`](digital-logic.md) — Gate-level physics, transistor implementation, and arithmetic circuits. The prerequisite for logic design.
- [`computing.computer-architecture`](computer-architecture.md) — Processor-level organization that consumes logic design outputs.
- [`computing.embedded-systems`](embedded-systems.md) — Application of logic design in microcontroller and FPGA-based control systems.
- [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md) — Diodes, transistors, and thyristors that implement logic gates.
- [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) — PCB manufacturing for logic circuit assemblies.
- [`electronics.passive-components`](../electronics/passive-components.md) — Resistors, capacitors, and inductors required for logic circuit bias and decoupling.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Computing](./index.md) · [All Domains](../index.md)*
