# Machine Code & Front-Panel Programming

> **Node ID**: software-bootstrapping.machine-code
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`computing.electronic`](../computing/electronic.md), [`computing.data-storage`](../computing/data-storage.md)
> **Enables**: [`software-bootstrapping.assemblers`](assemblers.md)
> **Timeline**: Years 50-60
> **Outputs**: binary_programs, bootstrap_loaders
> **Critical**: Yes — all software begins here; without machine code entry, the computer is inert hardware

## Problem

A computer without software is an expensive space heater. Before assemblers, compilers, or operating systems exist, the only way to make a computer do anything useful is to toggle binary instruction patterns into memory addresses using front-panel switches or hex keyboards. Every higher-level software tool traces back to this capability. The first assembler was written in machine code. The first compiler was assembled from machine code. The first operating system was bootstrapped from machine code entered by hand. This is the bedrock of the software bootstrap chain.

The process demands intimate knowledge of the target processor's instruction set architecture (ISA) — the hardware specification documented in [Electronic Computing](../computing/electronic.md). The programmer must encode each operation as a numeric opcode, calculate memory addresses for branch targets and data locations by hand, and track register usage and memory layout on paper. One wrong bit toggled into memory means the program crashes or produces wrong results. There is no editor, no debugger, no error checking — just the programmer, the front panel, and a pad of octal or hex notation.

## Prerequisites

### Hardware
- **Working computer** with front-panel switches or hex keypad ([computing.electronic](../computing/electronic.md)): The machine must be operational with accessible memory. The front panel provides address switches (set the memory location), data switches (set the instruction word), and control buttons (deposit, examine, step, run).
- **Memory** (at least 256 bytes, ideally 1-4 KB): Enough to hold a useful program. Early machines had 1-4 KB of magnetic core memory.
- **Paper tape reader/punch** or **magnetic storage** ([computing.data-storage](../computing/data-storage.md)): For saving and loading programs once entered. Without storage, programs are lost on power-off.

### Knowledge
- **ISA reference card**: The complete instruction set listing — every opcode, every addressing mode, every register encoding, every status flag. Typically a single photocopied or handwritten sheet.
- **Binary/hex/octal arithmetic**: Fluency in number base conversion. Most front panels display in octal (3 bits per digit) or hexadecimal (4 bits per digit).
- **Memory map**: Knowledge of which memory addresses are usable for programs, which are reserved for I/O devices, and where the processor starts executing on power-up (the reset vector).

### Infrastructure
- **Paper and pencil**: For writing out programs in binary/hex before toggling them in. Crossed-out and rewritten listings are the norm.
- **Reference documentation**: ISA manual, I/O device addresses, any existing subroutine libraries.
- **Patience**: Entering a 256-byte program takes 30-60 minutes via toggle switches. One error means starting over or finding and correcting the wrong bit.

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| Working computer with front panel | 1 unit | [computing.electronic](../computing/electronic.md) | Hex keypad + 7-segment display (later machines) |
| Paper tape (blank) | 50-200 m rolls | [computing.data-storage](../computing/data-storage.md) | Magnetic tape, cards |
| Paper tape punch | 1 unit | [computing.electromechanical](../computing/electromechanical.md) | Manual keypunch |
| Paper tape reader | 1 unit | [computing.electromechanical](../computing/electromechanical.md) | Photoelectric reader |
| Paper and pencils | Many sheets | Stationery supplies | None — essential for program planning |
| ISA reference card | 1 card | Manual documentation | Handwritten opcode table |

## Process Description

### Step 1: Write the Program on Paper

Write every instruction as a binary, octal, or hex value alongside its memory address. Use a two-column format: address on the left, instruction word on the right.

```
Addr    Hex     Meaning
0000    3E 05   LD A, 05h      ; Load accumulator with 5
0002    C3 10 00 JP 0010h      ; Jump to address 10h
...
0010    3C      INC A           ; Increment accumulator
0011    C3 10 00 JP 0010h      ; Loop forever
```

Calculate all branch target addresses by hand. Count bytes for each instruction (variable-length instruction sets like x86 require particular care). Double-check every address. A single off-by-one error in a branch target sends execution into the middle of a data word or another instruction.

### Step 2: Toggle the Program into Memory

1. Set the address switches on the front panel to the first address (0000h).
2. Press EXAMINE to read the current memory contents at that address.
3. Set the data switches to match the first instruction byte (3E).
4. Press DEPOSIT to write the byte into memory.
5. Press EXAMINE NEXT (or increment address manually) to advance to the next address.
6. Repeat for every byte of the program.

**Typical speed**: 30-60 seconds per instruction byte for an experienced operator. A 256-byte program takes 30-60 minutes.

### Step 3: Verify the Program

After entering all bytes, re-read each address and compare to the paper listing. Press EXAMINE at address 0000h, verify the displayed data matches the listing, then EXAMINE NEXT through the entire program. Correct any discrepancies by setting the correct data switches and pressing DEPOSIT.

### Step 4: Execute and Debug

Press RUN (or set the program counter to the start address and press RUN). Observe the results via front-panel indicator lights (data bus, address bus, status LEDs) or by examining memory locations where results should appear.

If the program does not work:
1. Press STOP (or HALT).
2. Examine the program counter — where did execution stop?
3. Examine registers (if front panel supports register display).
4. Examine memory locations that should have been modified.
5. Compare actual memory contents to expected values.
6. Correct errors by depositing corrected bytes.
7. Reset the program counter and run again.

### Step 5: Save to Paper Tape

Once the program works, punch it to paper tape for permanent storage. The punch records each byte as a row of holes on the tape. Label the tape with the program name, start address, entry point, and date.

### Bootstrap Loader

The most important machine code program is the **bootstrap loader** — a tiny program (typically 16-64 bytes) that reads a larger program from paper tape into memory and jumps to its start address. The bootstrap loader is toggled in by hand every time the computer is powered on (before ROM monitors exist).

**Typical PDP-8 bootstrap loader** (24 instructions, toggled in via front panel):
```
Addr    Oct     Function
7756    6014    Keyboard Reader Status → AC
7757    6011    Read character from Reader
7760    5357    JMP 7757 (wait for character ready)
7761    7106    Clear AC, begin memory pointer
7762    7006    Clear link
7763    7001    IOT: get character
...     ...     (loads program from paper tape to memory)
7775    5xxx    JMP to loaded program start
```

Once the bootstrap loader is toggled in and verified (24 bytes, ~10 minutes), it can load any larger program from paper tape in seconds. The bootstrap loader is the bridge from tedious manual entry to automated program loading.

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Front-panel entry speed | 30-60 sec/byte | Experienced operator |
| Hex keypad entry speed | 10-20 sec/byte | Faster than toggle switches |
| Paper tape read speed | 10-500 char/sec | Mechanical vs. optical reader |
| Paper tape punch speed | 10-50 char/sec | Electromechanical punch |
| Bootstrap loader size | 16-64 bytes | Machine-specific |
| Minimum useful program size | 32-256 bytes | Simple test routines |
| Typical bootstrap program | 256-2048 bytes | First assembler or monitor |
| Error rate (manual entry) | 1 error per 50-100 bytes | Human error in toggling |
| Verification time | 10-30 sec/byte | Re-reading and comparing |
| Power-on to running | 5-15 minutes | Toggle bootstrap, load program |

### Instruction Encoding Examples (8-bit processor)

| Instruction | Hex | Binary | Meaning |
|-------------|-----|--------|---------|
| NOP | 00 | 0000 0000 | No operation |
| LD A, nn | 3E nn | 0011 1110 data | Load 8-bit immediate |
| ADD A, n | C6 n | 1100 0110 data | Add immediate |
| JP nn | C3 nn nn | 1100 0011 lo hi | Jump to address |
| CALL nn | CD nn nn | 1100 1101 lo hi | Call subroutine |
| RET | C9 | 1100 1001 | Return from subroutine |
| OUT (n), A | D3 n | 1101 0011 port | Output to port |
| HALT | 76 | 0111 0110 | Halt processor |

## Scaling Notes

**From manual entry to automated loading**: The first programs are entered entirely by hand. As soon as a paper tape reader is available, the bootstrap loader eliminates most manual entry — only the 16-64 byte bootstrap needs to be toggled per power cycle. This is a 10-100× productivity improvement.

**From paper tape to magnetic media**: Once magnetic tape or disk storage is available, the bootstrap loader is stored on the medium itself, and a hardware ROM (or hardwired front-panel routine) reads the first sector, eliminating manual entry entirely.

**From single program to monitor program**: A monitor program (1-4 KB) provides hex keypad input, memory examination, simple debugging (single-step, breakpoint), and program loading from storage. The monitor is the ancestor of the operating system.

**Minimum viable bootstrap sequence**:
1. Toggle 24-byte bootstrap loader (10 min)
2. Load 1 KB paper tape program (10-30 sec)
3. Run program
4. Save working programs to paper tape
5. Eventually write a monitor program that replaces the toggle-in routine

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Program crashes immediately | Wrong entry point address; wrong instruction at address 0 | Verify program counter start address matches listing; re-examine first few instructions |
| Infinite loop in wrong place | Branch target address calculated incorrectly | Re-calculate all branch offsets by hand; verify each branch target matches listing |
| Garbage in memory after load | Paper tape reader misread (dirt, worn tape) | Clean reader heads; re-punch the tape; try a fresh copy |
| Front panel shows wrong data at address | Deposit failed (switch not fully toggled); memory fault | Re-toggle the byte and deposit again; if memory fault, test that address with known pattern (write FF, read, write 00, read, write AA, read) |
| Program works differently each run | Uninitialized memory; race condition with I/O | Initialize all memory locations the program uses before running; add explicit delay loops for I/O timing |
| Program runs but produces no output | Wrong I/O port address; device not connected | Verify port address matches hardware documentation; check device is powered and connected |
| Bootstrap loader fails to load tape | Wrong reader device code in bootstrap; reader not ready | Verify I/O instruction matches the actual paper tape reader hardware; ensure reader is loaded and online |

## Safety

- **Eye strain**: Toggling hundreds of binary values while staring at small indicator lights causes significant eye fatigue. Work in well-lit conditions. Take 10-minute breaks every 30 minutes of toggle entry.
- **Electrical hazard**: Front panels on early machines operate at logic-level voltages (5 V TTL), which are safe to touch. However, the power supply behind the panel contains lethal voltages. Never remove panel covers or reach behind the panel with power on.
- **Paper tape hazards**: Paper tape chads (the punched-out holes) are a slipping hazard on smooth floors. Collect and dispose of chads regularly. Paper tape dust is a mild respiratory irritant — avoid snorting or blowing tape debris.
- **Static electricity**: MOS-based computers (NMOS, CMOS) are sensitive to static discharge. Ground yourself to the chassis before touching the front panel or any circuit board. Do not toggle switches while standing on a carpet without grounding.

## Quality Control

**Verification checklist** — run for every program before first execution:
1. Re-read every address from memory; compare to paper listing byte-by-byte
2. Verify the entry point address is correct
3. Verify the reset vector (if the hardware loads the PC from a fixed address on reset)
4. Check that no data area overlaps with instruction area in memory
5. Verify I/O port addresses match the actual hardware configuration
6. For the bootstrap loader: test with a known-good paper tape before relying on it

**Functional test**: After loading, run a simple test (e.g., a program that writes a known pattern to an output port or memory location) before running the actual application.

## Variations and Alternatives

| Method | Speed | Error Rate | Best For |
|--------|-------|------------|----------|
| Toggle switches (binary) | Slowest (30-60 sec/byte) | High | First bootstraps on minimal hardware |
| Hex keypad + 7-segment | Medium (10-20 sec/byte) | Medium | Machines with hex entry panels |
| Octal entry (PDP-8 style) | Medium | Medium | 12-bit and 18-bit word machines |
| Paper tape input only | Fast (10-500 char/sec) | Low | Once bootstrap loader exists |
| ROM monitor | Fast (typed commands) | Low | Machines with built-in firmware |
| Cross-assembler on host machine | Fastest | Lowest | When a second computer is available |

**Cross-development alternative**: If another working computer exists, write and assemble programs on the host machine, then transfer the binary to the target machine via paper tape or serial link. This eliminates hand-toggling for all programs except the initial bootstrap loader.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Program crashes immediately on RUN | Wrong opcode toggled, or reset vector incorrect | Re-verify first 3-5 bytes against listing; confirm reset vector address matches hardware documentation |
| Infinite loop (no output) | Branch target address wrong by one byte | Recalculate all branch offsets; verify address labels match hex listing |
| Garbage on output device | I/O port address wrong or baud rate mismatch | Check I/O device address in ISA manual; verify serial baud rate and parity settings |
| Program works once then crashes | Self-modifying code corrupting instructions, or stack overflow | Trace through program on paper; check that data areas do not overlap code areas |
| Wrong results from arithmetic | Carry/overflow flag not handled, or wrong addressing mode | Re-verify each instruction's addressing mode bits; check flag behavior for subtract and compare |
| Paper tape loads garbage | Reader misaligned or tape not punched correctly | Clean reader heads; verify tape by visually inspecting punch holes; re-enter via front panel as fallback |

## See Also

- [Electronic Computing](../computing/electronic.md) — The hardware that runs machine code; ISA specifications, memory systems, I/O devices
- [Data Storage](../computing/data-storage.md) — Paper tape, magnetic media for program storage
- [Electromechanical Computing](../computing/electromechanical.md) — Paper tape punch and reader hardware
- [Assemblers, Linkers & Loaders](assemblers.md) — The next step: mnemonic representation replaces raw binary
- [Operating System Construction](operating-systems.md) — The monitor program that replaces manual entry

[← Back to Software Bootstrapping](index.md)
