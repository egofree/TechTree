# Electronic Computing

> **Node ID**: computing.electronic
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing.electromechanical`](electromechanical.md), [`electronics.assembly`](../electronics/assembly.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Enables**: [`computing.digital-logic`](digital-logic.md)
> **Timeline**: Years 50-70+
> **Outputs**: electronic_computers
> **Critical**: No — computing enhances capability but is not strictly required for survival

### Vacuum Tube Logic

**Triode operation**:
- **[Vacuum tube](../glossary/vacuum-tube.md)** (thermionic valve): Heated cathode emits electrons → electrons flow toward positively-charged anode (plate) through vacuum. Control grid between cathode and anode modulates electron flow — small voltage change on grid produces large change in plate current. This is amplification, the basis for all active electronic switching.
- **Requirements**: Glass envelope (glassblowing), vacuum (10⁻³ to 10⁻⁵ Torr, mechanical vacuum pump), heated cathode (oxide-coated nickel, ~700-1000°C, 0.5-2 W heater power per tube). Tube filaments burn out — mean time between failures 2,000-10,000 hours per tube.
- **Logic gates**: Grid biased to cutoff (tube off = logic 0) or conduction (tube on = logic 1). Resistor in plate circuit converts current to voltage. Two tubes with common plate resistor = NOR gate. NOR is functionally complete — any Boolean function implementable with NOR gates alone. Inverting output gives OR. Cascading gives AND.

**Flip-flop and register circuits**:
- **Eccles-Jordan flip-flop**: Two triodes cross-coupled (each plate drives the other's grid). Two stable states — one tube conducting, the other cut off. Trigger pulse toggles state. One bit of storage. Four tubes per flip-flop (two dual-triode envelopes).
- **Registers**: Chain of flip-flops stores multi-bit values. 20-bit accumulator register = 80 tubes. 10 such registers = 800 tubes just for working storage.

**[ENIAC-era architecture](../glossary/eniac-era-architecture.md)** (1945):
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
- **[CMOS](../glossary/cmos.md)** (Complementary MOS): p-channel and n-channel transistors in complementary pairs. One transistor always off → near-zero static power consumption. Power proportional to switching frequency (CV²f). 10-100× lower power than NMOS at low frequencies. Enables battery-powered devices and high-density ICs. Propagation delay: 5-50 ns. The dominant logic family from ~1980 onward.

**Advantages over tubes**: 100× smaller, 1000× more reliable (no filament burnout), 10-100× lower power, instant-on (no warm-up), compatible with printed circuit boards. Enables computers that run for months without hardware failure.

### Stored-Program Architecture (von Neumann)

**Principle**: Program instructions stored in same memory as data — contrast with ENIAC's cable-patching. Computer fetches, decodes, and executes instructions sequentially. Changed instructions change program without rewiring.

**Components**:
- **[CPU](../glossary/cpu.md)** (Central Processing Unit): Arithmetic Logic Unit (ALU) performs addition, subtraction, AND, OR, NOT, shifts. Control unit generates timing signals and decodes instructions. Register file: small fast storage (accumulator, index registers, program counter, instruction register, status flags).
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

**[Mercury delay line memory](../glossary/mercury-delay-line-memory.md)** (EDVAC, early stored-program machines):
- **Principle**: Electrical signal converted to acoustic pulse in mercury-filled tube. Pulse travels length of tube at ~1,450 m/s (speed of sound in mercury). At far end, transducer converts back to electrical signal, amplifies, and retransmits. Data circulates as a continuous stream of pulses.
- **Capacity**: ~500-1,000 bits per tube. Multiple tubes per machine. EDVAC design: 1,000 words of 44 bits = 44 tubes.
- **Access time**: ~0.5-1 ms per bit (must wait for desired pulse to reach the read end). Sequential access, not random.
- **Disadvantages**: Heavy (mercury is 13.6 g/cm³), temperature-sensitive (mercury velocity changes with temperature, requiring thermostatic control at 40°C ±0.1°C), mechanical fragility. Replaced by magnetic core as soon as core became available.

**[Plated wire memory](../glossary/plated-wire-memory.md)** (later improvement):
- **Structure**: Thin copper wire (0.1 mm diameter) electroplated with permalloy (Ni-Fe alloy, ~1 μm thick). Wires woven through ferrite keeper planes. Magnetic domains along the wire store bits. Non-destructive read (unlike core memory) — the sense signal is proportional to the stored bit without flipping it.
- **Advantages**: Faster read cycle (no rewrite needed), lower power, radiation-hard (used in space and military applications when core was being phased out elsewhere).

**[Early DRAM](../glossary/early-dram.md)** (Dynamic Random Access Memory):
- **Cell**: One transistor + one capacitor. Charge on capacitor = stored bit. Capacitor leaks — must be refreshed (read and rewritten) every 2-64 ms. Circuit simplicity enables high density.
- **[Intel 1103](../glossary/intel-1103.md)** (1970): 1 Kbit chip. First commercially successful DRAM. Replaced core memory in most systems by 1974. Access time: 300-600 ns.
- **Scaling**: DRAM density doubles roughly every 3 years (1 Kbit → 4 Kbit → 16 Kbit → 64 Kbit...). Each generation uses finer photolithography. DRAM becomes the technology driver for semiconductor manufacturing.

### Transistor Revolution: From Tubes to Solid State

**[Point-contact transistor](../glossary/point-contact-transistor.md)** (Bardeen and Brattain, December 1947):
- **Structure**: Two fine gold contacts (~50 μm spacing) pressed against a germanium crystal surface. The germanium slab sits on a metal base. One contact is the emitter, one is the collector, the base is the crystal itself.
- **Operation**: Small current at the emitter contact modulates a larger current at the collector contact. Current gain ~2-20. Fragile and difficult to reproduce consistently. Noisy and unstable over temperature.
- **Significance**: The first solid-state amplifier. Proved that semiconductor amplification was possible. Not practical for mass production but launched the entire transistor industry.

**[Junction transistor](../glossary/junction-transistor.md)** (Shockley, 1951):
- **Structure**: Three-layer semiconductor sandwich: n-p-n or p-n-p. The narrow middle layer (base, ~10-50 μm thick) controls current flow between emitter and collector.
- **Advantages over point-contact**: More reproducible, higher gain (β = 50-300), lower noise, better temperature stability. Manufacturable by alloy or grown-junction techniques.
- **Fabrication**: Alloy junction: place indium dots on both sides of thin n-type germanium wafer, heat to form p-type alloyed regions → pnp transistor. Grown junction: pull crystal from melt while changing dopant type during growth.

**Advantages over vacuum tubes**: 100× smaller, 1000× more reliable (no filament burnout), 10-100× lower power, instant-on (no warm-up), compatible with printed circuit boards. Enables computers that run for months without hardware failure.

### Logic Families

**Direct-coupled transistor logic (DCTL)**:
- Simplest transistor logic. Output of one transistor directly drives base of the next. No resistors between stages. Minimal component count. Poor noise margin and severe fanout limitation (current hogging: one transistor with slightly lower Vbe steals base current from paralleled transistors). Obsolete for practical systems.

**Resistor-transistor logic (RTL)**:
- Base resistor on each transistor input. Multiple inputs through separate base resistors = NOR gate. Simple, few components, easy to design. Used in early ICs (Fairchild μL900 series, 1961). Poor noise margin (~0.2 V), low fanout (~5), slow (~50 ns propagation at best). Supplanted by DTL and TTL by the mid-1960s.

**Diode-transistor logic (DTL)**:
- Input diodes perform AND function. Transistor inverts → NAND gate. Better noise margin than RTL (~0.5 V), higher fanout (~8). Propagation delay ~25-50 ns. Required more diodes per gate but diodes were cheap. Popular in early 1960s before TTL took over.

**[Transistor-transistor logic (TTL)](../glossary/transistor-transistor-logic-ttl.md)** (the dominant logic family 1965-1985):
- **7400 series**: 5 V supply, 10 ns typical propagation delay, 10 mW per gate, fanout 10. Multi-emitter input transistor replaces DTL input diodes. Totem-pole output stage provides active pull-up and pull-down for fast edges.
- **Variants**: Low-power TTL (74L series, 1 mW/gate, 33 ns), high-speed TTL (74H, 22 mW, 6 ns), Schottky TTL (74S, 19 mW, 3 ns — Schottky clamped transistor prevents deep saturation, faster turn-off), low-power Schottky (74LS, 2 mW, 9 ns — the most popular variant).

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

### EDVAC Architecture: Stored-Program Design

The EDVAC (Electronic Discrete Variable Automatic Computer), described in John von Neumann's 1945 "First Draft" report, established the architecture that nearly all subsequent computers follow:

**Key principles**:
- **Binary representation**: All data and instructions represented in binary (0 and 1), not decimal as in ENIAC. Binary simplifies arithmetic circuitry (two-state devices like relays, tubes, and transistors map naturally to binary). A single bit is stored as one flip-flop or one magnetic core.
- **Stored program**: Instructions stored in the same memory as data. The CPU fetches instructions from memory, decodes them, and executes them. To change the program, change the contents of memory rather than rewire patch cables. This is the single most important architectural insight in computing.
- **Serial arithmetic**: Numbers processed one bit at a time through a single arithmetic unit, reducing hardware at the cost of speed. Serial addition of two 40-bit numbers takes 40 clock cycles. Parallel arithmetic (processing all bits simultaneously) is faster but requires 40× more hardware.

**Memory: mercury delay lines**:
- Mercury-filled steel tubes, ~1 m long. Electrical pulses converted to sound waves travel through the mercury at ~1,450 m/s. At the far end, the signal is amplified and re-circulated. Each tube stores a sequence of pulses (a "word") that cycles through continuously. Access time: the average wait for a particular word to reach the read end (~0.5 ms for a 1 m tube).
- Capacity: ~1,000 words of 40-44 bits. Multiple tubes provide additional storage.

**I/O and peripheral devices**:
- **Magnetic tape**: Early magnetic tape systems recorded data on paper or plastic tape coated with iron oxide particles. Recording density: 100-500 bits per inch. Read/write speed: 50-150 inches per second. Replaced paper tape and punch cards for program and data storage due to higher capacity and rewritability.
- **Magnetic drum**: Rotating drum (see Electromechanical Computing) served as random-access secondary storage. Capacity: 1,000-16,000 words. Access time: 8-50 ms. Used for programs, subroutines, and data files too large for main memory.

### Software Development on Early Machines

**Program loading**: On stored-program machines, a small "bootstrap" program is entered by hand via front-panel switches (toggle binary instructions directly into memory addresses). This bootstrap program reads a larger loader program from paper tape or magnetic drum, which in turn loads the user's application program. The term "bootstrapping" (later shortened to "booting") comes from this sequence: the computer pulls itself up by its own bootstraps.

**Subroutine libraries**: Common mathematical functions (sine, cosine, logarithm, square root) are coded as subroutines and stored on paper tape or magnetic drum. The programmer calls a subroutine by inserting a jump instruction at the appropriate point in the main program. The subroutine executes, stores its result, and jumps back to the instruction following the call. Reusable subroutines are the earliest form of software reuse.

**Error detection**: Parity bits appended to each memory word detect single-bit errors (if the parity is wrong, the word is corrupt). Hamming codes detect and correct single-bit errors while detecting double-bit errors. These coding schemes become essential as memory sizes increase and error rates become statistically significant.

### Printed Circuit Board Technology

**Board construction**:
- **Substrate**: FR-4 (flame-retardant epoxy resin reinforced with woven fiberglass cloth). Thickness: 0.8-3.2 mm (1.6 mm most common). Copper foil (35 μm thick, "1 oz copper") laminated to one or both surfaces.
- **Patterning**: Photoresist applied to copper surface. UV exposure through artwork (negative or positive). Develop. Etch exposed copper in ferric chloride (FeCl₃) or ammonium persulfate. Strip resist. Result: copper traces (tracks) forming the circuit interconnections.
- **Plated through-holes**: Drill holes through the board at component lead locations. Electroless copper plating deposits a thin copper layer on the hole walls, connecting top and bottom copper layers. Followed by electrolytic copper plating to build up thickness (~25 μm). This creates vias (vertical interconnections) between layers.
- **Solder mask**: Green epoxy coating over the entire board except component pads and vias. Prevents solder bridges between adjacent traces during wave soldering.
- **Silkscreen**: White text printed on solder mask, showing component outlines, reference designators (R1, C2, U3), and polarity markings.

**Assembly**:
- **Through-hole**: Component leads inserted through drilled holes, soldered on the opposite side. Wave soldering: board passes over a wave of molten solder (260°C Sn-Pb or Sn-Ag-Cu) that contacts the bottom surface, soldering all joints simultaneously. Manual soldering for prototypes and rework.
- **Surface mount (SMT)**: Components soldered directly to surface pads (no through-holes). Smaller components, higher density. Solder paste (solder powder + flux, printed onto pads through a stainless steel stencil). Components placed by pick-and-place machine. Reflow soldering: board passes through a conveyor oven with temperature profile (preheat 150°C, ramp to 250°C peak, cool). The solder paste melts, wets the pads and component leads, and solidifies on cooling.

### Power Supply Design

**Linear power supply**:
- **Transformer**: Steps AC mains voltage down to the desired level (e.g., 120V AC → 12V AC). Laminated iron core transformer, efficiency 85-95%. Output is isolated from mains (safety).
- **Rectification**: Full-wave bridge rectifier (4 diodes) converts AC to pulsating DC. Ripple frequency: 120 Hz (for 60 Hz mains, 100 Hz for 50 Hz).
- **Filtering**: Large electrolytic capacitor (1000-10,000 μF) smooths the pulsating DC. Ripple voltage: Vr = Iload/(f × C). For 1A load, 4700 μF capacitor, 120 Hz: Vr ≈ 1.8V peak-to-peak.
- **Regulation**: Series pass transistor (or IC regulator like 7805 for +5V, 7812 for +12V) maintains constant output voltage despite input variation and load changes. Dropout voltage: 2-3V (input must be at least 2-3V above output). Efficiency: Output power / Input power ≈ Vout/Vin (typically 30-60% — the rest is dissipated as heat in the pass transistor). Heat sinking required.

**[Switching power supply](../glossary/switching-power-supply.md)** (higher efficiency):
- **Principle**: Convert DC to high-frequency AC (20-200 kHz), transform to desired voltage, rectify and filter. The high frequency allows a much smaller transformer than a 50/60 Hz linear supply. Regulation by pulse-width modulation (PWM): vary the duty cycle of the switching transistor to maintain constant output voltage.
- **Efficiency**: 75-95%. Much less waste heat than linear supplies.
- **Complexity**: Requires high-speed switching transistors, fast diodes, PWM controller IC, and careful EMI suppression (the fast switching edges generate radio-frequency interference that must be filtered at the input and output).

**Oscillator circuits**:
- **RC relaxation oscillator**: Capacitor charges through resistor toward supply voltage. When capacitor voltage reaches a threshold, a discharge path activates, discharging the capacitor rapidly. The cycle repeats. Frequency: f ≈ 1/(2RC × ln(3)) for a simple Schmitt trigger oscillator. Stability: poor (±10-20% with temperature and supply variation). Adequate for clock generation where precise frequency is not critical.
- **Crystal oscillator**: Piezoelectric quartz crystal resonates at a precise frequency determined by its physical dimensions (thickness for AT-cut crystals). Frequency stability: ±10-50 ppm over temperature (-40°C to +85°C). Used for all precision timing: CPU clocks, real-time clocks, communication system frequency references. Standard frequencies: 32.768 kHz (real-time clocks, 2¹⁵ = 32768), 3.579545 MHz (NTSC color burst), 10 MHz (frequency standard). The crystal operates as a very high-Q (10,000-1,000,000) resonant element in the feedback loop of an amplifier.

### Memory Evolution: From Cores to Chips

**Magnetic core memory (4-wire threading detail)**:
- **Wire functions**: Each core is threaded with four wires: X select and Y select (each carries half-switching current, addressing a specific core at the intersection), sense wire (detects the voltage pulse when a core flips state during read), and inhibit wire (carries opposing current during write to prevent unwanted switching of cores on the same X or Y line). Threading requires high dexterity or semi-automated machines.
- **Cycle timing**: 0.5-5 μs full read-write cycle. Read is destructive (flips the core to "0"), so every read must be followed by a rewrite of the original value. Non-destructive read variants exist but add complexity.
- **Plane organization**: A 256 × 256 core plane stores 64 Kbit. Planes are stacked to form words: a 16-bit memory at 64K addresses requires 16 planes, each with 65,536 cores, totaling 1,048,576 individually threaded cores.
- **Cost trajectory**: ~$1 per bit in 1960, falling to ~$0.01 per bit by 1975.

**Semiconductor memory arrival**:
- **[Intel 1103 DRAM](../glossary/intel-1103-dram.md)** (1970): 1 Kbit organized as 1,024 × 1 bit. Three-transistor cell design. Access time 300-600 ns. Replaced magnetic core in most new designs by 1974.
- **[Intel 1702 EPROM](../glossary/intel-1702-eprom.md)** (1971): 2 Kbit (256 × 8) erasable programmable read-only memory. Program via 25-50 V pulses injecting charge onto floating gates. Erase by UV exposure through a quartz window in the ceramic package for 15-20 minutes. Rewritable firmware storage for microcode and bootstrap programs.
- **[Intel 2816 EEPROM](../glossary/intel-2816-eeprom.md)** (1978): 16 Kbit (2K × 8) electrically erasable PROM. Byte-level erasure using on-chip charge pumps, no UV source needed. The ancestor of modern Flash memory. Write endurance ~10⁴ cycles for early devices.

**Storage hierarchy (latency range)**:
- **CPU registers**: <1 ns. Dozens to hundreds of bytes, integrated into the processor core.
- **Cache (SRAM)**: 1-10 ns. KB to MB. Six-transistor cells, fast but expensive per bit. L1/L2/L3 levels with increasing size and latency.
- **Main memory (DRAM)**: 50-100 ns. MB to GB. One-transistor, one-capacitor cells requiring periodic refresh. Orders of magnitude cheaper than SRAM.
- **Solid-state storage (flash)**: 10-100 μs. GB to TB. Non-volatile, block-erase architecture.
- **Hard disk drive**: 5-15 ms seek + rotational latency. TB scale. Mechanical positioning, persistent, cheapest per bit for online storage.
- **Magnetic tape**: 10-100 seconds (sequential access). TB to PB. Lowest cost per bit, used for archival backup.

**I/O evolution timeline**:
- **[Teletype](../glossary/teletype.md)** (1940s-1960s): 10 characters/second (110 baud). Electromechanical, printed on paper roll. Interactive computing at human typing speed.
- **[Line printer](../glossary/line-printer.md)** (1960s): 300-1,000 lines/minute, 80-132 characters per line. Impact printing, batch output.
- **[Video display terminal](../glossary/video-display-terminal.md)** (1970s): 9,600 baud serial, 24 × 80 character CRT display. Cursor addressing enables full-screen editing.
- **[Graphics display](../glossary/graphics-display.md)** (1970s-1980s): Bitmapped 1024 × 768 pixels. Frame buffer memory maps to screen. Enables CAD, visualization, GUIs.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Computing](./index.md) • [All Domains](../index.md)*
