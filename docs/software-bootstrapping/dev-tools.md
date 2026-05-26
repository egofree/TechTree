# Development Tools & Debugging

> **Node ID**: software-bootstrapping.dev-tools
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`software-bootstrapping.compilers`](compilers.md), [`software-bootstrapping.assemblers`](assemblers.md)
> **Enables**: Productive software development at scale
> **Timeline**: Years 60-75
> **Outputs**: text_editors, debuggers, build_systems
> **Critical**: No — programs can be written without these tools, but productivity is severely limited

## Overview

Development tools are the software that helps write, test, and maintain other software. A text editor creates and modifies source code; a debugger inspects and controls program execution; a build system automates compilation and linking; version control tracks changes over time.

Without development tools, programming is possible but painful — source code is entered via teletype with no ability to correct errors except by re-punching the entire line or using a correction tape. Debugging means inserting print statements and recompiling. Building means manually issuing compile and link commands for each source file. Version control means keeping dated copies of source files.

Development tools transform programming from an ordeal into a craft. Each tool addresses a specific bottleneck:
- **Editor**: Writing and modifying source code (replaces teletype entry)
- **Debugger**: Finding and fixing bugs (replaces print-statement debugging)
- **Build system**: Managing compilation of multi-file projects (replaces manual compile commands)
- **Version control**: Tracking changes and enabling collaboration (replaces dated file copies)

## Prerequisites

### Software
- **Working compiler** ([compilers](compilers.md)): Development tools are written in a high-level language. The compiler is needed to build them.
- **Working assembler** ([assemblers](assemblers.md)): Some tools (debuggers in particular) need assembly-level access to processor state.
- **Operating system** ([operating-systems](operating-systems.md)): Development tools run under an OS that provides file I/O, terminal I/O, and process control.

### Hardware
- **CRT terminal**: A video display terminal (24 × 80 characters minimum) with keyboard. Essential for interactive editing. Teletype output is too slow for screen editing.
- **Disk storage**: Source files, object files, and executables. Development generates many files — a typical project might have 50-200 source files, each 100-2,000 lines.

### Knowledge
- **Terminal I/O programming**: Screen addressing, character attributes, keyboard input handling.
- **Data structures**: Buffer gap (editor), trees (build dependency graph), diffs (version control).

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| CRT terminal | 1 unit | [computing.electronic](../computing/electronic.md) | Teletype (line editors only, no screen editing) |
| Disk storage | ≥1 MB | [computing.data-storage](../computing/data-storage.md) | Magnetic tape (sequential, slow) |
| Working compiler + assembler | 1 each | [compilers](compilers.md), [assemblers](assemblers.md) | Cross-development on host machine |
| Operating system | 1 instance | [operating-systems](operating-systems.md) | Bare-metal monitor (minimal tools) |

## Process Description

### Text Editor

**Line editor (ed-style)** — the simplest form:
- Operates on one line at a time. No screen display of the full file.
- Commands: `a` (append lines), `d` (delete line), `p` (print line), `s/old/new/` (substitute text), `w` (write file), `q` (quit).
- Address range: `1,10p` prints lines 1-10. `$` = last line. `.` = current line.
- Implementation: Read entire file into a memory buffer (or work from a temporary file if memory is limited). Process commands one at a time.

**Screen editor (vi/emacs-style)** — requires CRT terminal:
- Display a full screen of text (24 × 80 characters). Cursor indicates current position.
- Commands are single keystrokes: move cursor (arrow keys or h/j/k/l), insert text (`i`), delete character (`x`), delete line (`dd`), search (`/pattern`), save (`:w`).
- Implementation requires terminal escape sequences to position the cursor, clear lines, and scroll the display.

**Buffer gap implementation**:
The editor stores the file as a single buffer with a gap at the cursor position:

```
[Text before cursor] [GAP] [Text after cursor]
```

- Insert: Write character at the start of the gap, advance gap start pointer. O(1).
- Delete: Move gap start backward by one character. O(1).
- Move cursor: Copy characters from one side of the gap to the other. O(n) worst case but amortized O(1) for sequential access.

**Memory usage**: File size + gap size (typically 1-10 KB). Files larger than available memory require paging (load portions from disk as needed).

### Debugger

A debugger allows the programmer to:
- **Set breakpoints**: Mark an instruction address where execution should pause.
- **Single-step**: Execute one instruction, then pause.
- **Examine registers**: Display the current values of all processor registers.
- **Examine memory**: Display memory contents at any address (hex dump).
- **Modify memory/register**: Change values to test hypotheses about bugs.

**Implementation**:

**Breakpoint mechanism**: Replace the instruction at the breakpoint address with a trap instruction (software interrupt). When the processor hits the trap, control transfers to the debugger. The debugger saves the register state, displays it, and waits for user commands. To continue execution, the debugger restores the original instruction, sets the processor to single-step mode, executes the original instruction, re-inserts the trap, and resumes.

**Register display**: After a breakpoint or single-step, dump all registers:

```
PC=0042 SP=7F00 AF=0042 BC=1234 DE=5678 HL=9ABC
Flags: Z=1 N=0 H=1 C=0
```

**Memory dump**: Display memory in hex and ASCII:

```
0040: 3E 05 C3 10 00 3C C3 10 00 76 00 00 00 00 00 00  >........v......<
0050: 48 65 6C 6C 6F 20 57 6F 72 6C 64 00 00 00 00 00  Hello World.....
```

**Watchpoints**: Monitor a memory location and break when it changes. Implementation: check the watched locations after each single-step. Slow (10-100× slowdown) but invaluable for finding memory corruption bugs.

### Build System

A build system automates the compilation process for multi-file projects:

**Makefile syntax**:
```
target: prerequisites
    command to build target from prerequisites

program.o: program.c program.h
    compiler -c program.c -o program.o

program: program.o utils.o
    linker program.o utils.o -o program
```

**Operation**:
1. Read the makefile (a text file listing targets, prerequisites, and build commands).
2. For each target, check if any prerequisite is newer than the target (using file timestamps).
3. If a prerequisite is newer, execute the build command.
4. Process targets in dependency order (topological sort of the dependency graph).

**Dependency graph**: The build system constructs a directed graph where each node is a file and edges represent dependencies. A topological sort produces the correct build order. Parallel builds are possible when independent targets exist.

**Implementation**: A basic make-like tool is 500-2,000 lines of code. It reads a configuration file, checks file timestamps, and executes shell commands.

### Version Control

**Simple approach — numbered backups**: Before editing a file, copy `program.c` to `program.c.bak`. Before the next edit, copy to `program.c.bak.1`. Incremental, requires manual management.

**Diff-based approach**: Store only the differences (deltas) between versions. To reconstruct version N, start with the original and apply deltas 1 through N.

**Diff algorithm**: Compare two files line by line. Find the longest common subsequence (LCS). Everything not in the LCS is a deletion (from the old file) or an insertion (in the new file). Output: a list of line ranges to delete and insert.

```
*** program.c.v1     Mon May 25 10:00:00 2026
--- program.c.v2     Mon May 25 11:00:00 2026
***************
*** 10,12 ****
    int x = 5;
!   int y = 10;
    int z = x + y;
--- 10,12 ----
    int x = 5;
!   int y = 20;
    int z = x + y;
```

**Repository structure**:
```
.project/
    HEAD          (pointer to latest version)
    versions/
        1.diff
        2.diff
        3.diff
    metadata/
        log       (commit messages, dates, authors)
```

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Line editor size | 500-2,000 lines | Simple command interpreter |
| Screen editor size | 2,000-10,000 lines | Terminal handling adds complexity |
| Debugger size | 1,000-5,000 lines | Breakpoint + register + memory display |
| Build system size | 500-2,000 lines | Basic dependency tracking |
| Version control size | 2,000-8,000 lines | Diff algorithm + repository management |
| Editor memory usage | File size + 1-10 KB | Buffer gap overhead |
| Screen refresh time | 50-200 ms | Full screen redraw over serial terminal |
| Compilation of editor | 2-10 min | Self-hosting compilation of a 5,000-line editor |
| Diff computation (1,000-line file) | 1-5 sec | LCS algorithm O(n²) |
| Debugger slowdown (single-step) | 10-100× | Each instruction requires trap + register dump |

### Editor Performance Comparison

| Editor Type | Memory | Start-up Time | Edit Operations/sec |
|-------------|--------|--------------|---------------------|
| Line editor (ed) | 4-20 KB | <0.1 sec | Limited by typing speed |
| Screen editor (vi-like) | 16-64 KB | 0.5-2 sec | Immediate (screen updates) |
| Editor with syntax highlighting | 32-128 KB | 1-5 sec | Immediate |

## Scaling Notes

**From line editor to screen editor**: The line editor works on any terminal (teletype, hard-copy). The screen editor requires a CRT terminal with cursor addressing. The productivity improvement is dramatic — the programmer can see and modify any part of the file instantly, rather than navigating line-by-line.

**From single-file to project-level build**: A simple compiler invocation handles one source file. A build system handles projects with dozens or hundreds of source files, recompiling only the files that changed. For a 100-file project, this reduces build time from "recompile everything" (30 minutes) to "recompile 3 changed files" (1 minute).

**From manual backups to version control**: Numbered backups work for small projects. Version control with diffs works for projects up to thousands of files. Distributed version control (like git) handles massive projects, but is far beyond bootstrap needs.

**From single developer to team**: Version control enables multiple developers to work on the same codebase. The simplest approach: one developer at a time ("lock" a file before editing). More sophisticated: merge changes from multiple simultaneous editors.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Editor corrupts file on save | Buffer overflow; disk full during write | Write to a temporary file first, then rename (atomic replace); check disk space before saving |
| Debugger shows wrong register values | Context not properly saved; examining wrong stack frame | Verify breakpoint handler saves ALL registers before any other operation |
| Build system recompiles everything | File timestamps incorrect (clock not set); all prerequisites listed | Verify system clock; use incremental build with proper dependency tracking |
| Version control produces garbled diff | Files with mixed line endings; tab vs. spaces inconsistency | Normalize line endings before diffing; use consistent formatting |
| Editor crashes on large files | Buffer overflow; memory exhaustion | Implement file paging (load portions from disk); add file size limits with warnings |

## Safety

- **Data loss risk**: The most significant hazard. An editor bug can destroy source code. Always save to a new file (or create a backup) before making large edits.
- **No physical hazards**: Development tools are purely software. Safety concerns are limited to data integrity and eye strain from prolonged terminal use.
- **Eye strain**: Prolonged CRT use (8+ hours) causes eye fatigue. Use a monitor with minimal flicker (refresh rate ≥60 Hz). Take 10-minute breaks every hour.

## Quality Control

**Editor testing**: Create a test file, perform insert, delete, search, replace, save, reload. Verify file contents match expectations after each operation.

**Debugger testing**: Set a breakpoint in a known program, verify register values match hand-calculated values. Single-step through a known sequence and verify each instruction produces expected register changes.

**Build system testing**: Create a project with known dependencies, modify one source file, verify only the necessary targets are rebuilt. Verify the output binary is correct.

**Version control testing**: Save a file, make changes, save again, revert to the first version. Verify the reverted file matches the original exactly (byte-for-byte comparison).

## Variations and Alternatives

| Tool Type | Simplest Version | Full Version | When to Upgrade |
|-----------|-----------------|-------------|-----------------|
| Editor | Line editor (ed) | Screen editor (vi/emacs) | Once CRT terminal available |
| Debugger | Front-panel single-step | Software debugger with breakpoints | Once OS supports trap instructions |
| Build system | Shell script | Make-like dependency tracker | Once project exceeds 5-10 source files |
| Version control | Numbered backups | Diff-based repository | Once project exceeds 10-20 source files |

**Forth-style development**: Forth blurs the line between editor, compiler, and debugger. The Forth interpreter provides immediate feedback — type a word definition and test it instantly. No separate compile step. Development is conversational rather than batch-oriented. A Forth system with built-in editor and debugger fits in 4-8 KB.

## References

- [Compiler Construction](compilers.md) — Development tools are built with compilers
- [Assemblers, Linkers & Loaders](assemblers.md) — Assembly-level debugging tools
- [Operating System Construction](operating-systems.md) — OS provides the execution environment for development tools
- [Electronic Computing](../computing/electronic.md) — Terminal hardware, I/O controllers

---
*Part of the [Bootciv Tech Tree](../index.md) • [Software Bootstrapping](./index.md) • [All Domains](../index.md)*
