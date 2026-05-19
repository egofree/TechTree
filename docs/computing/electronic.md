# Electronic Computing

> **Node ID**: computing.electronic
> **Domain**: Computing & Automation
> **Timeline**: Years 50-70+
> **Outputs**: electronic_computers

### Vacuum Tube Logic

**Triode operation**:
- **Vacuum tube** (thermionic valve): Heated cathode emits electrons → electrons flow toward positively-charged anode (plate) through vacuum. Control grid between cathode and anode modulates electron flow — small voltage change on grid produces large change in plate current. This is amplification, the basis for all active electronic switching.
- **Requirements**: Glass envelope (glassblowing), vacuum (10⁻³ to 10⁻⁵ Torr, mechanical vacuum pump), heated cathode (oxide-coated nickel, ~700-1000°C, 0.5-2 W heater power per tube). Tube filaments burn out — mean time between failures 2,000-10,000 hours per tube.
- **Logic gates**: Grid biased to cutoff (tube off = logic 0) or conduction (tube on = logic 1). Resistor in plate circuit converts current to voltage. Two tubes with common plate resistor = NOR gate. NOR is functionally complete — any Boolean function implementable with NOR gates alone. Inverting output gives OR. Cascading gives AND.

**Flip-flop and register circuits**:
- **Eccles-Jordan flip-flop**: Two triodes cross-coupled (each plate drives the other's grid). Two stable states — one tube conducting, the other cut off. Trigger pulse toggles state. One bit of storage. Four tubes per flip-flop (two dual-triode envelopes).
- **Registers**: Chain of flip-flops stores multi-bit values. 20-bit accumulator register = 80 tubes. 10 such registers = 800 tubes just for working storage.

**ENIAC-era architecture** (1945):
- **Scale**: 17,468 vacuum tubes, 70,000 resistors, 10,000 capacitors, 7,200 crystal diodes. 30 tons, 167 m² floor space. Power consumption: ~150 kW. Heat dissipation required forced-air cooling.
- **Architecture**: 20 accumulators (each a 10-digit decimal counter using ring circuits), multiplier, divider/square-root unit, function tables (read-only lookup via switches), master clock (100 kHz ring oscillator). All decimal, not binary.
- **Programming**: Physical patch cables on plug boards — rewiring required for each new program. Setup time: hours to days. No stored program.
- **Performance**: 5,000 additions per second, 357 multiplications per second. 1,000× faster than electromechanical relay calculators.
- **Reliability**: Several tube failures per day. Diagnosed by margin testing (reducing voltages to find marginal tubes). Replacement required every 2-3 days on average.

### Transistor Circuits

**Bipolar Junction Transistor (BJT) switching**:
- **npn transistor**: Emitter grounded, base driven high → collector current flows (transistor on, Vce ≈ 0.2 V saturation). Base driven low → collector current ceases (transistor off, Vce ≈ supply voltage). One transistor + one resistor = digital inverter. Switching speed: 1-100 MHz depending on construction (alloy junction = slow, diffused planar = fast).
- **Transistor-transistor logic (TTL)**: Multi-emitter input transistor implements AND function, output stage provides inversion and drive. Standard 5 V supply. Propagation delay: 10-30 ns per gate. Power: ~10 mW per gate. Fan-out: 10 (one gate output drives 10 gate inputs). The workhorse logic family of the 1960s-1970s.

**MOSFET logic**:
- **NMOS**: n-channel enhancement-mode MOSFETs. Pull-down transistor + pull-up resistor (or depletion-mode load). Low input current (gate is capacitor). Simpler fabrication than TTL (fewer diffusions, no buried layer). Used in early microprocessors (Intel 4004, 8008, 8080). Power dissipation: ~0.5-2 mW per gate. Speed: 50-200 ns propagation.
- **CMOS** (Complementary MOS): p-channel and n-channel transistors in complementary pairs. One transistor always off → near-zero static power consumption. Power proportional to switching frequency (CV²f). 10-100× lower power than NMOS at low frequencies. Enables battery-powered devices and high-density ICs. Propagation delay: 5-50 ns. The dominant logic family from ~1980 onward.

**Advantages over tubes**: 100× smaller, 1000× more reliable (no filament burnout), 10-100× lower power, instant-on (no warm-up), compatible with printed circuit boards. Enables computers that run for months without hardware failure.

### Stored-Program Architecture (von Neumann)

**Principle**: Program instructions stored in same memory as data — contrast with ENIAC's cable-patching. Computer fetches, decodes, and executes instructions sequentially. Changed instructions change program without rewiring.

**Components**:
- **CPU** (Central Processing Unit): Arithmetic Logic Unit (ALU) performs addition, subtraction, AND, OR, NOT, shifts. Control unit generates timing signals and decodes instructions. Register file: small fast storage (accumulator, index registers, program counter, instruction register, status flags).
- **Memory**: Read/write storage for both instructions and data. Addressed by numeric location. Early machines: 1-64 KB. Access time: 1-10 μs (magnetic core) or 0.1-1 μs (transistorized).
- **I/O**: Peripheral interfaces connect CPU to external devices (card readers, printers, tape units). Programmed I/O (CPU polls device status) or interrupt-driven (device signals CPU when ready).

**Instruction cycle**: Fetch instruction from memory address in program counter → increment program counter → decode instruction → fetch operands → execute in ALU → store result → repeat. Clock rate: 100 kHz (early tube machines) to 1-10 MHz (transistor machines). One instruction typically takes 1-20 clock cycles.

### Memory Systems

**Magnetic core memory**:
- **Structure**: Grid of tiny ferrite rings (0.5-2 mm outer diameter), each threaded with 3-4 wires. Each core stores one bit (clockwise vs counterclockwise magnetization). Core planes stacked to form multi-bit words.
- **Read**: Drive current through X and Y select wires at half-switching current each — only the core at the intersection receives full current, flipping its state. Sense wire detects the induced voltage pulse (or absence thereof). Destructive read — must rewrite after reading.
- **Write**: Same X/Y drive, with inhibit wire carrying opposing current to prevent switching for "0" bits. Enables selective writing.
- **Performance**: 1-10 μs cycle time. Non-volatile (retains data without power). Capacity: 4-32 KB typical per installation. Cost: ~$1 per bit in 1960 (the dominant memory technology 1955-1975).
- **Manufacturing**: Threading cores by hand or semi-automated machines. 1 MB system = ~8 million cores, each hand-threaded with 3-4 wires. Labor-intensive.

**Early DRAM** (Dynamic Random Access Memory):
- **Cell**: One transistor + one capacitor. Charge on capacitor = stored bit. Capacitor leaks — must be refreshed (read and rewritten) every 2-64 ms. Circuit simplicity enables high density.
- **Intel 1103** (1970): 1 Kbit chip. First commercially successful DRAM. Replaced core memory in most systems by 1974. Access time: 300-600 ns.
- **Scaling**: DRAM density doubles roughly every 3 years (1 Kbit → 4 Kbit → 16 Kbit → 64 Kbit...). Each generation uses finer photolithography. DRAM becomes the technology driver for semiconductor manufacturing.

### Input/Output Systems

**Punched card I/O**: 80-column Hollerith cards (see [Electromechanical Computing](./electromechanical.md)). Card reader: 100-2,000 cards/minute. Card punch: 50-300 cards/minute. Primary input medium through the 1970s.

**Paper tape**: 5, 6, or 8 channel continuous paper strip. Holes punched by tape punch attached to teletype or keypunch. Read by photoelectric or mechanical reader at 10-500 characters/second. Cheaper and more compact than cards for small programs. Used for CNC machine tool programs and telegraphy.

**Teletype/teleprinter**: Electromechanical typewriter that generates digital codes (5-bit Baudot or 8-bit ASCII) as keys are pressed. Prints received characters on paper. 10-30 characters/second. Primary interactive terminal for early computers. Built-in paper tape punch/reader on many models.

**Line printer**: Print one full line (80-132 characters) at a time via impact. Chain printer: character slugs on rotating chain, hammer fires when correct character aligns with print position. Speed: 300-2,000 lines/minute. Noisy but fast — primary output for batch computing.

### Programming

**Machine code**: Binary instruction patterns loaded directly into memory. Each instruction = opcode + operand(s). Example: 0010 0001 0101 = "add contents of address 21 to accumulator." Error-prone, no readability. Earliest programs entered via front-panel switches (toggle binary into memory locations).

**Assembly language**: Mnemonic representation of machine code. `ADD 21` instead of `0010 0001 0101`. One-to-one correspondence with machine instructions. Symbolic labels for branch targets (loop start, subroutine entry). Still architecture-specific.

**Assembler**: Program that translates assembly language to machine code. Two-pass: first pass collects label addresses into symbol table, second pass generates binary instructions using resolved addresses. One of the first programs written for any new computer — self-hosting once operational.

**Compiler**: Translates high-level language (Fortran, COBOL, ALGOL) to machine code. Fortran (1957): first widely-used compiler. Optimizing compiler for scientific computation. Converts mathematical expressions to efficient register usage and instruction sequences. Enables programmers to write 5-10× faster than assembly.

### Early Computer Architectures

**Accumulator machine**: Single implicit register (accumulator) receives all ALU results. Instructions: `ADD address`, `SUB address`, `STORE address`, `LOAD address`. Simple to implement, few transistors. Most early architectures (EDVAC, EDSAC, PDP-8). 1-address instruction format.

**Register-based machine**: Multiple general-purpose registers (4-16). Instructions specify source and destination registers: `ADD R1, R2, R3`. More complex hardware but generates shorter, faster code. IBM System/360 (16 registers) established the model.

**Word sizes**: Define data width and address space. 8-bit (microcontrollers, early hobby computers), 12-bit (PDP-8), 16-bit (PDP-11, early minicomputers), 32-bit (IBM System/360, VAX). Larger word = larger directly-addressable memory (16-bit → 64 KB, 32-bit → 4 GB) and wider arithmetic. Word size determines ALU width, register width, data bus width, and memory alignment.

### Safety & Hazards

- **CRT high voltage (25-30 kV)**: Cathode ray tubes and large vacuum tube circuits operate at lethal potentials. The CRT envelope and its anode connection carry 25-30 kV during operation, and the tube's internal capacitance can retain a dangerous charge for hours or days after power-off. Always discharge CRT anodes and high-voltage capacitors to chassis ground using a properly insulated discharge tool before servicing. Observe the one-hand rule: keep one hand behind your back when probing live high-voltage circuits to prevent current across the chest.
- **Vacuum tube implosion**: Large vacuum tubes (especially CRTs) hold a hard vacuum behind a glass envelope. Atmospheric pressure (~101 kPa) loads every square centimeter of the glass. A crack or impact can cause sudden violent implosion, launching glass fragments at high velocity. Wear eye protection (safety goggles or face shield) when handling vacuum tubes. Handle tubes by their bases, not the glass envelope. Dispose of cracked tubes by contained implosion in a heavy cloth bag or puncture the anode button to equalize pressure slowly.
- **Solder fumes (lead-based solder)**: Traditional tin-lead solder (60/40 or 63/37 Sn-Pb) generates fumes during soldering — primarily from the rosin flux core, which releases formaldehyde and other irritants. Lead itself does not vaporize at soldering temperatures (~230°C) but accumulates on surfaces and hands as oxide dust. Use local exhaust ventilation (fume extractor or open window). Wash hands thoroughly after soldering, especially before eating. Lead-free solders (SAC305: Sn-Ag-Cu) eliminate lead exposure but produce similar flux fumes.
- **Stored energy in capacitors**: Power supply filter capacitors in tube-era and transistor-era equipment store lethal energy — a 100 µF capacitor charged to 300 V holds 4.5 J, enough to cause ventricular fibrillation. Large high-voltage capacitors in CRT circuits store far more. Charge can persist for hours after power-off due to low leakage paths. Always discharge all capacitors with a bleed resistor (100 Ω to 1 kΩ, 2 W minimum) before touching any circuitry. Never short capacitor terminals with a screwdriver — the arc damages components and can spray molten metal.

---

*Part of the [Bootciv Tech Tree](../) • [Computing](./) • [All Domains](../)*
