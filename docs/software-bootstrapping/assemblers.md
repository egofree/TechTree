# Assemblers, Linkers & Loaders

> **Node ID**: software-bootstrapping.assemblers
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`software-bootstrapping.machine-code`](machine-code.md), [`computing.data-storage`](../computing/data-storage.md)
> **Enables**: [`software-bootstrapping.compilers`](compilers.md), [`software-bootstrapping.operating-systems`](operating-systems.md)
> **Timeline**: Years 50-60
> **Outputs**: assembly_language, object_files, executable_programs
> **Critical**: Yes — assemblers are the first software tool built for any new architecture, enabling all subsequent software development

## Overview

An assembler translates human-readable mnemonic instructions (assembly language) into machine code binary. Where machine code programming requires the programmer to remember that `3E 05` means "load the accumulator with 5," assembly language lets them write `LD A, 5` — a dramatic improvement in readability, writability, and maintainability.

The assembler is the first software tool built for any new computer. The bootstrap sequence is: (1) hand-enter a minimal assembler in machine code via front panel, (2) use that assembler to assemble larger programs, (3) eventually rewrite the assembler in its own assembly language and use the first assembler to assemble it — making the assembler self-hosting.

Beyond the assembler itself, this capability includes linkers (which combine multiple object files into a single executable) and loaders (which place the executable into memory and start execution). Together, these three tools form the software toolchain that enables all higher-level software construction.

## Prerequisites

### Software
- **Working machine code entry capability** ([machine-code](machine-code.md)): The assembler itself must first be written in machine code or on a cross-development system.
- **ISA reference**: Complete instruction set specification from [computing.electronic](../computing/electronic.md).

### Hardware
- **Computer with sufficient memory**: The assembler needs at least 4-8 KB to operate (program + symbol table + input buffer + output buffer). A practical assembler for a real ISA needs 8-32 KB.
- **Storage for source and output**: Paper tape or magnetic storage for both the assembly source file and the generated object code.

### Knowledge
- **Formal grammar basics**: Understanding of labels, opcodes, operands, and directives as syntactic categories.
- **Symbol table algorithms**: Hash tables or binary search for label lookup.
- **Relocation concepts**: Understanding that object code may need address adjustment when combined with other modules.

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| Computer with ≥8 KB memory | 1 unit | [computing.electronic](../computing/electronic.md) | Cross-assemble on host machine |
| Paper tape or magnetic storage | Adequate for source + output | [computing.data-storage](../computing/data-storage.md) | Any writable persistent storage |
| Teletype or terminal | 1 unit | [computing.electronic](../computing/electronic.md) | Paper tape punch for source entry |
| Assembly language reference | 1 document | Custom per ISA | Handwritten opcode mnemonic list |

## Process Description

### Assembly Language Design

Before writing the assembler, define the assembly language syntax:

**Instruction format**: `[label:] OPCODE [operand] [;comment]`

```
LOOP:   LD A, (HL)      ; Load byte at address in HL
        CP 0             ; Compare with zero
        JR Z, DONE       ; Jump if zero
        CALL PROCESS     ; Process the byte
        INC HL           ; Next byte
        JR LOOP          ; Repeat
DONE:   RET              ; Return
```

**Directives** (pseudo-operations that control assembly, not generate code):
- `ORG addr` — set the origin (starting address for subsequent code)
- `DB value` — define byte (data, not instruction)
- `DW value` — define word (2-byte value)
- `DS count` — define storage (reserve bytes)
- `EQU value` — equate symbol to value (constant definition)
- `END` — end of source program

### Two-Pass Assembly

The assembler makes two passes over the source file:

**Pass 1 — Collect labels and calculate addresses**:
1. Initialize the location counter to the ORG address (or 0 if no ORG).
2. Read each source line.
3. If the line has a label, record `label = current location counter value` in the symbol table.
4. Advance the location counter by the instruction size (1-4 bytes depending on opcode and addressing mode).
5. When `END` is reached, Pass 1 is complete. The symbol table now contains every label and its address.

**Pass 2 — Generate object code**:
1. Reset the location counter to the ORG address.
2. Read each source line again.
3. Look up the opcode mnemonic in the opcode table → get the binary encoding.
4. Evaluate the operand: if it is a label, look it up in the symbol table (built during Pass 1) and substitute the numeric address. If it is a numeric literal, use it directly.
5. Combine opcode and operand into the final binary instruction word.
6. Write the binary instruction to the output file.
7. Advance the location counter.

**Why two passes?** Forward references. A program can jump to a label that appears later in the source:

```
        JR Z, DONE       ; References DONE, which hasn't been seen yet
        ...               ; Several more instructions
DONE:   RET               ; Label DONE is defined here
```

Without two passes, the assembler cannot resolve `DONE` when it first encounters the jump. Pass 1 collects all labels; Pass 2 resolves all references.

### Symbol Table Implementation

The symbol table maps label names to numeric addresses. For a small assembler (<100 labels), a simple linear search works. For larger programs (100-10,000 labels), use a hash table:

**Hash table approach**:
1. Choose a prime number of buckets (e.g., 31, 61, 127).
2. Hash the label name: sum ASCII values, modulo bucket count.
3. Each bucket is a linked list of (name, address) pairs.
4. Lookup: hash the name, search the bucket's list. O(1) average, O(n) worst case.
5. Insertion: hash the name, append to the bucket's list.

**Memory requirement**: Each symbol table entry uses ~8-20 bytes (label name + address + link pointer). 1,000 labels × 16 bytes = 16 KB. This is a significant memory commitment on a machine with 32 KB total.

### Linker Operation

The linker combines multiple independently assembled object files into a single executable:

1. **Load all object files**: Read each object file's symbol table (exported symbols) and relocation table.
2. **Assign addresses**: Allocate memory segments for each module, one after another. Record the base address of each module.
3. **Resolve external references**: For each undefined symbol in each module, search all other modules' exported symbols for a match.
4. **Relocate addresses**: Add each module's base address to all address references within that module.
5. **Write the executable**: Concatenate the relocated code from all modules into the output file.

**Relocation table**: For each instruction that contains an absolute address, the assembler records the offset in the object file. The linker adds the module's base address to each such location.

### Loader Operation

The loader reads an executable file into memory and starts execution:

1. Read the executable header (start address, size, entry point).
2. Copy the code bytes into memory at the start address.
3. If the program has relocations, apply them (add the actual load address to each relocatable reference).
4. Set the program counter to the entry point.
5. Transfer control to the loaded program.

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Pass 1 speed | 20-100 lines/sec | Paper tape input; limited by I/O |
| Pass 2 speed | 20-100 lines/sec | Same I/O bottleneck |
| Assembly time (1,000-line program) | 10-50 sec | Paper tape; 2-5 sec on magnetic storage |
| Symbol table entry size | 8-20 bytes | Name + address + link |
| Typical symbol table capacity | 100-5,000 labels | Memory-constrained machines |
| Object file overhead | 5-20% | Header + relocation table |
| Linker speed | 1-5 modules/sec | I/O bound |
| Minimum assembler memory | 4-8 KB | Code + tables + buffers |
| Practical assembler memory | 8-32 KB | For real programs with many labels |
| First assembler size | 512-2,048 bytes | Written in machine code |

### Assembler Complexity Metrics

| Component | Lines of Code | Memory Usage |
|-----------|--------------|-------------|
| Opcode table | 50-200 entries | 200-800 bytes |
| Symbol table (data structure) | Variable | 500-5,000 bytes |
| Pass 1 logic | 200-500 lines | 1-2 KB |
| Pass 2 logic | 300-700 lines | 1-3 KB |
| Expression evaluator | 100-300 lines | 500-1,500 bytes |
| I/O routines | 100-200 lines | 500-1,000 bytes |
| **Total assembler** | **1,000-2,500 lines** | **4-12 KB** |

## Scaling Notes

**From single-pass to two-pass**: The simplest assembler is single-pass, requiring all labels to be defined before use (backward references only). This is too restrictive for real programs. Two-pass assembly handles forward references and is worth the complexity.

**From absolute to relocatable**: The simplest assembler produces absolute code (hardcoded addresses). Relocatable object files allow the linker to place code anywhere in memory, enabling modular programming and library reuse. Adding relocation adds ~30% to assembler complexity.

**From single module to libraries**: Once the linker works, frequently-used subroutines can be assembled into library files. The linker pulls in only the modules that the program references. A standard I/O library might contain 20-50 modules (print decimal, read line, string operations, math functions), of which a typical program uses 5-10.

**Macro assembler**: Macros allow the programmer to define named instruction sequences that are expanded inline during assembly. A macro assembler adds 500-1,000 lines of code to the basic assembler but can reduce source program size by 30-50% for repetitive instruction patterns.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| "Undefined symbol" error | Label misspelled; label defined in wrong module; missing module from linker input | Check spelling; verify label exists in source; ensure all needed object files are linked |
| "Duplicate symbol" error | Same label defined in two modules | Rename one label; use local labels or scope rules |
| Program crashes at startup | Wrong ORG address; code loaded at wrong address by loader | Verify ORG matches the expected load address; check loader configuration |
| Branches go to wrong addresses | Location counter misaligned by variable-length instructions | Check instruction size calculations; verify all addressing modes produce correct byte counts |
| Assembler runs out of memory | Symbol table too large for available memory | Reduce label count; increase hash table efficiency; add symbol table overflow to disk/secondary storage |
| Object file corrupted | Paper tape read error during assembly | Re-punch the source tape; clean reader heads; verify checksums |
| Relocation error in linker | Assembler generated wrong relocation entries | Verify all absolute address references are marked for relocation; check instruction encoding for absolute vs. relative addressing |

## Safety

- **No physical hazards**: Assembly programming is a purely intellectual activity. The primary risk is frustration and fatigue from debugging symbolic errors.
- **Repetitive strain**: Typing assembly programs on a teletype or keyboard for extended periods causes hand and wrist strain. Take breaks every 30 minutes.
- **Eye strain**: Reading assembly listings on paper or CRT for extended debugging sessions. Ensure adequate lighting.

## Quality Control

**Assembler self-test**: Assemble a test program with known output. Compare the generated binary to the expected binary byte-by-byte. The test should cover:
- Every instruction in the opcode table (at least one test per opcode)
- Every addressing mode
- Forward and backward references
- Expression evaluation (arithmetic in operands)
- ORG, DB, DW, DS, EQU directives
- Error detection (undefined symbol, duplicate label, invalid opcode)

**Linker test**: Link two or more object files. Verify that cross-module references resolve correctly and that relocated addresses are adjusted properly.

**Loader test**: Load an executable, examine memory at the load address, verify bytes match the executable file contents, verify the program runs correctly.

## Variations and Alternatives

| Assembler Type | Complexity | When to Use |
|----------------|-----------|-------------|
| Single-pass, absolute | Simplest | Very first assembler; no forward references needed |
| Two-pass, absolute | Moderate | Most bootstrap scenarios |
| Two-pass, relocatable | Complex | Once modular programming begins |
| Macro assembler | More complex | High-volume production code |
| Cross-assembler (runs on different machine) | Moderate | When a host computer is available |
| One-pass with backpatching | Moderate | Memory-constrained environments where two-pass is too expensive |

**Cross-assembler strategy**: Write the assembler to run on an already-working computer (the "host"), generating object code for the target machine. This eliminates the need to write the first assembler in machine code — the host's existing tools handle source editing, file I/O, and debugging. Transfer the assembled binary to the target via paper tape or serial link.

## References

- [Machine Code & Front-Panel Programming](machine-code.md) — The prerequisite: entering binary by hand
- [Electronic Computing](../computing/electronic.md) — ISA specifications, processor architecture
- [Compiler Construction](compilers.md) — The next step: higher-level language translation
- [Operating System Construction](operating-systems.md) — Programs assembled here need an OS to manage resources
- [Development Tools](dev-tools.md) — Editors and debuggers that assist assembly programming

---
*Part of the [Bootciv Tech Tree](../index.md) • [Software Bootstrapping](./index.md) • [All Domains](../index.md)*
