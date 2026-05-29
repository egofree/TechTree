# Computer Architecture

> **Node ID**: computing.computer-architecture
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing.logic-design`](logic-design.md), [`computing.electronic`](electronic.md), [`computing.data-storage`](data-storage.md)
> **Enables**: [`computing.embedded-systems`](embedded-systems.md), semiconductor fab automation control systems
> **Timeline**: Years 50-70+
> **Outputs**: cpu_designs, memory_hierarchy, bus_architecture, io_systems
> **Critical**: Yes — the architecture determines whether logic gates become a useful processor or an unorganized collection of transistors


Computer architecture defines the structure and behavior of a computing system as seen by the programmer: the instruction set, register organization, memory hierarchy, I/O mechanisms, and interconnect (bus) topology. It is the contract between hardware and software — the ISA specifies what the hardware must do, and the microarchitecture specifies how the hardware does it.

This capability sits at the intersection of [`computing.logic-design`](logic-design.md) (gate-level implementation) and software-bootstrapping (the software that runs on the hardware). The architect makes the critical design decisions — RISC vs. CISC, word size, cache organization, pipeline depth — that determine performance, complexity, and bootstrappability for decades.

Architecture is distinct from logic design and embedded systems:
- **Logic design** answers "how do I build correct circuits from gates?" — timing, state machines, synthesis
- **Computer architecture** answers "what circuits do I build, and how do they interact?" — ISA, memory hierarchy, buses
- **Embedded systems** answers "how do I deploy a complete hardware-software system for a specific control task?" — microcontroller selection, firmware, sensor interfacing

**Boundary with software-bootstrapping**: This document covers the hardware architecture — the physical organization of CPU, memory, buses, and I/O. Instruction set design is documented here as a hardware specification (opcodes, registers, addressing modes). How to write programs in that ISA, build assemblers, or implement compilers is software construction — see the software-bootstrapping domain.

## Prerequisites

## Materials

- Working logic gates and flip-flops from [`computing.logic-design`](logic-design.md)
- Memory components (SRAM, DRAM, ROM) from [`computing.data-storage`](data-storage.md)
- PCB assemblies from [`electronics.assembly`](../electronics/assembly.md)
- Passive components for decoupling and termination from [`electronics.passive-components`](../electronics/passive-components.md)

## Tools and Equipment

- Logic analyzer (32+ channels for bus and instruction decode debugging)
- Oscilloscope (200+ MHz for timing analysis)
- ROM programmer (for microcode and boot code)
- FPGA development board (for architecture prototyping before ASIC commitment)

## Knowledge

- Combinational and sequential logic design (see [`computing.logic-design`](logic-design.md))
- Stored-program concept (see [`computing.electronic`](electronic.md))
- Binary arithmetic: two's complement, fixed-point, floating-point representation
- Boolean algebra and state machine design

## Bill of Materials

| Component | Quantity (per CPU prototype) | Source | Alternatives |
|-----------|------------------------------|--------|-------------|
| FPGA (50K+ logic elements) | 1 | [`computing.digital-logic`](digital-logic.md) — programmable logic | Discrete TTL/CMOS ICs (100-500× board space) |
| SRAM (1-4 Mb, 10 ns access) | 1-4 chips | [`computing.data-storage`](data-storage.md) | Register file from flip-flops (small, fast, expensive) |
| ROM/Flash (128 KB-1 MB) | 1 chip | [`computing.data-storage`](data-storage.md) | EPROM (UV-erasable, reusable) |
| Crystal oscillator (10-50 MHz) | 1 | Piezoelectric quartz crystal circuit | RC oscillator (±20% tolerance) |
| Voltage regulator (3.3V or 5V, 2A) | 1 | [`electronics.power-electronics`](../electronics/power-electronics.md) | Linear regulator (simple, inefficient) |
| Decoupling capacitors (100 nF) | 20-50 | [`electronics.passive-components`](../electronics/passive-components.md) | 10 nF (marginal at >50 MHz) |
| 4-layer PCB (power, ground, 2 signal) | 1 | [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) | 2-layer (acceptable below 20 MHz) |

## Process Description

## Instruction Set Architecture (ISA) Design

1. **Define the data path width.** Choose 8-bit (simplest, minimal transistors), 16-bit (good balance for embedded), or 32-bit (standard for general-purpose). Word size determines register width, ALU width, data bus width, and maximum addressable memory.

2. **Choose the register set.** Options:
   - **Accumulator machine**: One implicit register (A). Instructions: `ADD addr`, `SUB addr`, `LOAD addr`, `STORE addr`, `JMP addr`. Minimum hardware, maximum memory traffic.
   - **Register-memory machine**: Multiple registers (8-16). Instructions operate on register-register or register-memory pairs. IBM System/360 model.
   - **Load-store machine (RISC)**: Only LOAD and STORE access memory. All arithmetic operates on registers. Requires more registers (32+). MIPS, RISC-V, ARM model.

3. **Define the instruction format.** Fixed-length (RISC: all instructions 32 bits) or variable-length (CISC: 1-15 bytes). Fixed-length simplifies decoding and pipelining. Variable-length encodes common instructions compactly.

4. **Specify addressing modes.** How operands are identified:
   - **Immediate**: Operand is in the instruction itself (e.g., `ADD R1, #5`)
   - **Register**: Operand is in a register (e.g., `ADD R1, R2`)
   - **Direct**: Instruction contains the memory address (e.g., `LOAD R1, 0x1000`)
   - **Register indirect**: Register contains the memory address (e.g., `LOAD R1, (R2)`)
   - **Indexed**: Register + offset for array access (e.g., `LOAD R1, (R2 + offset)`)
   RISC architectures typically support 3-4 modes; CISC architectures support 8-12.

5. **Assign opcodes.** Reserve opcode space for future expansion. Use a regular encoding that simplifies decode logic. Group related operations (arithmetic, logic, branch, memory) into contiguous opcode ranges.

## Datapath Design

1. **Design the ALU.** Implement addition, subtraction, AND, OR, XOR, NOT, shifts (logical and arithmetic). Add zero-detect and sign-detect flags for branch conditions. An 8-bit ALU requires ~200 gates; a 32-bit ALU requires ~2,000 gates.

2. **Design the register file.** N registers of W bits each. Two read ports and one write port per cycle (typical 3-operand instruction: read two sources, write one result). Implement with SRAM array or flip-flop bank with multiplexed read and decoded write.

3. **Design the data bus.** Connect ALU, register file, memory interface, and I/O. Single bus (simplest, one transfer per cycle), dual bus (simultaneous read operands), or dedicated point-to-point connections (highest bandwidth, most wiring).

## Control Unit Design

1. **Finite state machine approach.** Define the micro-operations for each instruction as a sequence of states. Each state asserts control signals (register write-enable, ALU operation, memory read/write, bus select). The state machine advances through fetch → decode → execute → writeback. For a simple accumulator machine: 3-5 states per instruction.

2. **Microcoded approach.** Store the control sequence in a ROM (control store). Each instruction's execution is a microprogram: a sequence of microinstructions read from the control store. Enables complex instructions (CISC) without complex state machine logic. The control store is a ROM indexed by opcode and micro-address. Modify instructions by changing control store contents, not hardware.

## Memory Hierarchy Design

1. **Registers** (< 1 ns access): Fastest, smallest, most expensive per bit. Architecturally visible — programmer or compiler manages register allocation. 8-32 registers typical.

2. **Cache — L1** (1-3 ns, 16-64 KB): Small fast SRAM between CPU and main memory. Direct-mapped (simplest, 1 comparator per line), set-associative (2-4 way, better hit rate), or fully associative (best hit rate, most comparators). Cache line size: 16-64 bytes. Hit rate target: 90-95% for L1.

3. **Cache — L2** (5-10 ns, 256 KB-4 MB): Larger, slower SRAM. Unified (instruction + data) or separate. Acts as a backstop for L1 misses. Hit rate target: 95-99%.

4. **Main memory — DRAM** (50-100 ns, MB-GB): The primary storage for programs and data. Accessed through a memory controller that manages refresh, row/column addressing, and burst transfers. Bandwidth: 1-20 GB/s depending on bus width and clock rate.

5. **Storage hierarchy trade-offs**:

| Level | Access time | Size | Cost/bit | Technology |
|-------|-------------|------|----------|------------|
| Register | <1 ns | 64 B-1 KB | Highest | Flip-flops |
| L1 cache | 1-3 ns | 16-64 KB | High | SRAM (6T cell) |
| L2 cache | 5-10 ns | 256 KB-4 MB | Medium | SRAM |
| Main memory | 50-100 ns | 1 MB-64 GB | Low | DRAM (1T1C cell) |
| SSD/flash | 10-100 μs | 8 GB-4 TB | Very low | NAND flash |
| Hard disk | 5-15 ms | 100 GB-20 TB | Lowest | Magnetic platters |

## Bus Architecture

1. **Single bus (Von Neumann)**: One shared bus for instruction fetch, data load/store, and I/O. Simple wiring. Bottleneck: only one transfer per cycle. Adequate for simple processors at low clock rates.

2. **Harvard architecture**: Separate instruction and data buses. Simultaneous instruction fetch and data access doubles memory bandwidth. Standard for microcontrollers and DSPs. Requires two memory systems.

3. **System bus** (CPU, memory, I/O controllers share a common bus):
   - **Address bus**: CPU outputs the target address. Width determines addressable space: 16-bit → 64 KB, 32-bit → 4 GB.
   - **Data bus**: Carries read/write data. Width determines transfer size: 8-bit, 16-bit, 32-bit.
   - **Control bus**: Read/write strobes, interrupt lines, bus request/grant for DMA.
   - Bus bandwidth = (bus width × clock frequency) / transfer_cycles. Example: 32-bit bus at 100 MHz, 2 cycles per transfer = 200 MB/s.

4. **Direct Memory Access (DMA)**: Peripheral device requests bus ownership from CPU. CPU grants bus. Peripheral transfers data directly to/from memory without CPU involvement. CPU can continue executing from cache during DMA. Essential for high-bandwidth I/O (disk, network, display).

## Quantitative Parameters

## RISC vs. CISC Comparison

| Parameter | RISC (MIPS, RISC-V) | CISC (x86, VAX) |
|-----------|---------------------|------------------|
| Instruction length | Fixed (32-bit) | Variable (1-15 bytes) |
| Instruction count per task | Higher (more instructions) | Lower (complex instructions) |
| Clock cycles per instruction | 1 (pipelined) | 1-20 (variable) |
| Register count | 32 | 8-16 |
| Addressing modes | 3-4 | 8-12 |
| Microcode required | No (hardwired control) | Yes (complex decode) |
| Pipeline depth | 5-7 stages | Variable |
| Design complexity | Lower | Higher |

## Pipeline Stage Timing (5-stage RISC)

| Stage | Function | Latency |
|-------|----------|---------|
| IF (Instruction Fetch) | Read instruction from memory/cache | 1 cycle |
| ID (Instruction Decode) | Decode opcode, read register file | 1 cycle |
| EX (Execute) | ALU operation or address calculation | 1 cycle |
| MEM (Memory Access) | Load/store data cache access | 1 cycle (hit), 10-50 cycles (miss) |
| WB (Writeback) | Write result to register file | 1 cycle |

Ideal throughput: 1 instruction completed per cycle (IPC = 1.0). Pipeline hazards (data dependencies, branch mispredictions, cache misses) reduce real IPC to 0.5-1.5 on simple pipelines, 2-4 on superscalar out-of-order designs.

## Cache Performance

| Parameter | L1 direct-mapped | L1 4-way set-associative | L2 8-way |
|-----------|------------------|--------------------------|----------|
| Capacity | 16 KB | 32 KB | 256 KB |
| Access latency | 2 cycles | 3 cycles | 8-12 cycles |
| Hit rate (speculative) | 85-90% | 92-96% | 95-99% |
| Miss penalty | 8-30 cycles (L2) | 8-30 cycles (L2) | 50-200 cycles (DRAM) |
| Power per access | 0.1-0.5 nJ | 0.3-1.0 nJ | 1-5 nJ |

## Bus Bandwidth by Architecture

| Bus type | Width | Clock | Bandwidth | Use case |
|----------|-------|-------|-----------|----------|
| I²C | 1-bit serial | 100 kHz-3.4 MHz | 12.5 KB/s-425 KB/s | Low-speed sensor I/O |
| SPI | 1-bit serial | 1-50 MHz | 125 KB/s-6.25 MB/s | Flash, ADC, display |
| 8-bit parallel | 8 bits | 10 MHz | 10 MB/s | Simple microcontroller bus |
| 32-bit parallel | 32 bits | 100 MHz | 400 MB/s | General-purpose system bus |
| DDR4 memory bus | 64 bits | 1.6-3.2 GHz (data rate) | 12.8-25.6 GB/s | Main memory interface |

## Scaling Notes

**From accumulator to register file**: An accumulator machine needs only one register — the ALU always writes to the accumulator. Adding 4-8 general-purpose registers reduces memory traffic by 40-60% (more operands kept on-chip). Cost: 4-8× register hardware plus register-address decoding in instructions.

**From single-cycle to pipelined**: A single-cycle processor completes one instruction per (long) clock cycle. The clock period is set by the slowest instruction. Pipelining divides execution into stages, each completing in one short clock cycle. Throughput increases by the number of pipeline stages (ideal case). Cost: pipeline registers between stages (area overhead), hazard detection and forwarding logic (complexity).

**From scalar to superscalar**: Issue multiple instructions per cycle by replicating execution units (2 ALUs, 2 memory ports). Requires instruction-level parallelism (ILP) in the code and dynamic scheduling logic (reservation stations, reorder buffer). Modern CPUs issue 4-8 instructions per cycle.

**Minimum useful processor**: An 8-bit accumulator machine with 16 instructions, 256 bytes RAM, and 1 KB ROM can be implemented in ~2,000 gates on a small FPGA. This is sufficient for control tasks (reading sensors, driving actuators, running simple state machines) and represents the entry point for computer architecture bootstrapping.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Incorrect instruction execution | Microcode ROM error or hardwired control logic bug | Single-step through instruction micro-operations; compare control signal assertions against specification |
| Memory read returns wrong data | Timing violation: address not stable before read strobe | Insert wait states; check address setup time against memory access time |
| Processor hangs after branch | Branch target calculation error (off-by-one in PC update) | Verify branch offset encoding (relative vs. absolute); check PC increment logic |
| Cache miss rate unexpectedly high | Conflict misses in direct-mapped cache | Increase associativity (2-way or 4-way); increase cache size; align frequently-accessed data to different cache sets |
| Bus contention — data corruption | Two devices driving bus simultaneously | Verify bus arbitration logic; check DMA request/grant handshake; add bus keeper resistors |
| Interrupt lost during processing | Interrupt signal shorter than interrupt sampling period | Edge-triggered latch on interrupt input; increase interrupt sampling rate; use level-sensitive interrupts |

## Safety

- **High-speed clock signals**: A 100 MHz clock has 3.3 ns edges with significant high-frequency content. Use controlled-impedance PCB traces (50 Ω) for clock distribution. Unterminated clock lines cause reflections that produce double-clocking (flip-flops trigger twice per cycle). Terminate clock lines with series resistors at the source or parallel termination at the destination.
- **Power supply sequencing**: Multi-voltage designs (e.g., 3.3V I/O with 1.2V core) require power-up sequencing. If the I/O ring powers up before the core, the I/O drivers may attempt to drive into an unpowered core, causing latchup. Apply core voltage first, then I/O voltage. Reverse on power-down.
- **Thermal management**: A CPU dissipating 5-25 W in a 25 mm² die area requires heatsinking. Junction temperature above 100-150°C causes timing degradation and eventual failure. Attach heatsink with thermal compound (0.5-1.0 °C/W thermal resistance). For >10 W, add forced-air cooling.
- **Bus contention damage**: If two drivers simultaneously assert opposite states on a bus, the resulting short circuit can exceed driver current ratings and destroy the ICs. Use open-drain or tri-state bus configurations with appropriate pull-up resistors.

## Quality Control

## Functional Verification

- **ISA compliance test**: Write a test program that executes every instruction in the ISA with known operand patterns. Compare register and memory results against a reference model (software simulator). A minimal ISA (16 instructions) requires ~50 test cases.
- **Boundary condition testing**: Test arithmetic at overflow (MAX_INT + 1), underflow (MIN_INT - 1), divide by zero, and carry propagation across word boundaries.

## Performance Verification

- **Benchmark programs**: Run standardized workloads:
  - **Dhrystone**: Synthetic integer benchmark. Measures MIPS (millions of instructions per second). Simple but not representative of real workloads.
  - **CoreMark**: More modern synthetic benchmark. Better correlation with real application performance.
  - **Real applications**: Sort, matrix multiply, FFT — measure actual throughput on workloads relevant to the bootstrap.

## Timing Closure

- **Static timing analysis (STA)**: Check all register-to-register paths against the target clock period. No path may have a total delay (combinational logic + setup time + clock skew) exceeding the clock period. Timing must close at worst-case conditions (slow process corner, high temperature, low voltage).

## Variations and Alternatives

## Accumulator Architecture

The simplest useful processor design. One implicit accumulator register. All ALU results go to the accumulator. Instructions: LOAD, STORE, ADD, SUB, AND, OR, JMP, JZ (jump if zero). 8-16 instructions total. Can be implemented in ~1,500-2,000 gates. The canonical bootstrap architecture: PDP-8, early microcontrollers, most teaching processors.

## Stack Machine

Operands are on a hardware stack rather than in registers. Instructions: PUSH, POP, ADD (pops two, pushes result). Zero-operand format — the instruction encodes only the operation. Very compact code (bytecode interpreters use this model). Hardware implementation requires a stack pointer and stack memory. Forth language targets stack machines directly.

## Register-Window Architecture (RISC)

Used in SPARC and some RISC-V implementations. The large register file is divided into windows, with overlapping registers between adjacent windows for fast parameter passing in procedure calls. Reduces memory traffic for function calls at the cost of complex register file management.

## VLIW (Very Long Instruction Word)

The compiler explicitly schedules parallel operations. Each instruction contains multiple operation fields (e.g., integer ALU, floating-point, memory, branch) issued simultaneously. Simplifies hardware (no dynamic scheduling) but shifts complexity to the compiler. Used in DSPs (TI C6000) and Itanium.

## Architecture Comparison for Bootstrapping

| Architecture | Gate count | Compiler complexity | Code density | Bootstrap priority |
|-------------|------------|--------------------|-------------|--------------------|
| 8-bit accumulator | ~2,000 | Trivial | Low | First (minimum viable) |
| 16-bit register (4 regs) | ~5,000 | Simple | Medium | Second |
| 32-bit RISC (16 regs) | ~20,000 | Moderate | Medium | Third |
| 32-bit CISC | ~50,000+ | Complex | High | Last |

## See Also

- [`computing.logic-design`](logic-design.md) — Gate-level design methodology used to implement processor datapaths and control units.
- [`computing.electronic`](electronic.md) — Vacuum tube and transistor computing history; stored-program architecture origins.
- [`computing.digital-logic`](digital-logic.md) — Transistor-level gate implementation, arithmetic circuits, and memory cells.
- [`computing.data-storage`](data-storage.md) — Memory technologies (SRAM, DRAM, flash, magnetic) used in the memory hierarchy.
- [`computing.embedded-systems`](embedded-systems.md) — Application of processor architecture in dedicated control systems.
- [`electronics.semiconductor-devices`](../electronics/semiconductor-devices.md) — Transistors and diodes that implement processor logic.
- [`electronics.pcb-fabrication`](../electronics/pcb-fabrication.md) — PCB design for high-speed processor bus routing.



[← Back to Computing](index.md)
