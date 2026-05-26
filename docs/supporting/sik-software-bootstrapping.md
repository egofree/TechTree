# SIK Placement Test: Software-Bootstrapping Domain

> **Candidate Domain**: `software-bootstrapping`
> **Date**: 2026-05-25
> **Proposed By**: Sisyphus (Task 10)
> **Status**: PASS (with boundary conditions)
> **Risk Level**: HIGHEST — boundary conflict with existing `computing/` domain

---

## 1. Executive Summary

The `software-bootstrapping` domain covers the creation of software systems — assemblers, compilers, operating systems, and development tools — that run on computing hardware produced by the existing `computing/` domain. This SIK test evaluates whether software construction warrants its own domain or should remain within `computing/`.

**Verdict: PASS on all three SIK dimensions** — software construction has <50% overlap with hardware computing on infrastructure, knowledge, and practitioner profile. The split is justified. However, two boundary conditions must be enforced to prevent content bleed.

---

## 2. Existing Computing Domain Inventory

### 2.1 Current Nodes

| Node ID | Content | Lines |
|---------|---------|-------|
| `computing` | Domain node | — |
| `computing.mechanical` | Abacus, slide rules, mechanical calculators, difference engines | 222 |
| `computing.electromechanical` | Relay computing, punch card systems, automated machine tools, cam automation | 205 |
| `computing.electronic` | Vacuum tube and transistor computing, stored-program architecture, logic families, memory systems | 223 |
| `computing.digital-logic` | Boolean algebra, gate-level design, sequential circuits, arithmetic units, FPGA | 210 |
| `computing.data-storage` | Punch cards, magnetic media, optical storage, solid-state memory | 202 |

### 2.2 Current Edges (from computing nodes)

| From | To | Type | Meaning |
|------|----|------|---------|
| `computing` | `machine-tools` | tool | Hardware needs precision manufacturing |
| `computing.mechanical` | `machine-tools` | tool | Mechanical calc needs machining |
| `computing.mechanical` | `metals` | material | Brass/steel for gears |
| `computing.electromechanical` | `computing.mechanical` | tool | Builds on mechanical foundations |
| `computing.electromechanical` | `energy.electricity` | material | Needs electricity |
| `computing.electronic` | `computing.electromechanical` | tool | Builds on electromechanical |
| `computing.electronic` | `silicon.basic-devices` | material | Needs transistors/ICs |
| `computing.digital-logic` | `computing` | tool | Builds on computing domain |
| `computing.digital-logic` | `computing.electronic` | material | Needs electronic components |
| `computing.data-storage` | `computing` | tool | Storage serves computing |
| `computing.data-storage` | `polymers.thermoplastics` | material | Needs polymer substrates |

### 2.3 What computing/ Actually Covers

The computing domain is **hardware-focused**. Each capability documents the physical construction of computing devices:

- **Mechanical**: Wood, brass, steel → gear wheels, carry mechanisms, precision machining tolerances
- **Electromechanical**: Relays, solenoids, cams, punch card machinery → physical switching and counting
- **Electronic**: Vacuum tubes, transistors, PCBs → circuit-level hardware construction
- **Digital logic**: Gate-level transistor design → hardware building blocks
- **Data storage**: Physical media construction (magnetic coating, optical pits, flash cells)

Software is mentioned only in passing in `computing.electronic` (the "Programming" section — ~20 lines covering machine code, assembly language, and compilers as concepts that exist). The domain does not cover **how to build** these software systems.

---

## 3. SIK Test Evaluation

Per schema-spec.md §6.2, the SIK test evaluates three dimensions. Technologies belong in the same domain only if ALL THREE exceed 50%.

### 3.1 Physical Infrastructure Overlap: ~20% — FAIL (<50%)

| Dimension | computing/ (Hardware) | software-bootstrapping (Software) |
|-----------|----------------------|-----------------------------------|
| **Primary equipment** | Oscilloscopes, soldering irons, logic analyzers, PCB etching, semiconductor fab, precision machining tools | Text terminals, paper, pencils (early); the computer itself (later) |
| **Workspace** | Electronics lab, machine shop, cleanroom | Desk with terminal, reference manuals |
| **Materials consumed** | Silicon, copper, glass, chemicals, solder, PCB substrates | Paper, electricity (to run the computer) |
| **Supply chain** | Mining, chemicals, metals, glass, semiconductor fab | computing/ hardware (the computer itself) |
| **Utilities** | Clean power, cooling water, vacuum, compressed air | Electricity, lighting |

**Analysis**: The physical infrastructure for hardware construction and software construction are almost entirely disjoint. A hardware engineer uses oscilloscopes and soldering irons; a software developer uses a text terminal. The only shared infrastructure is the building and electricity. Software's primary "infrastructure" is the computer itself — a product of computing/, not shared infrastructure.

**Verdict: FAIL — ~20% overlap**

### 3.2 Knowledge Base Overlap: ~30% — FAIL (<50%)

| Knowledge Area | Shared? | Notes |
|----------------|---------|-------|
| Boolean algebra | YES | Both use Boolean logic; hardware for circuit design, software for program logic |
| Binary number representation | YES | Both work in binary |
| von Neumann architecture | PARTIAL | Hardware implements it; software targets it |
| Circuit design (analog/digital) | NO | Hardware-only |
| Semiconductor physics | NO | Hardware-only |
| Electromagnetic theory | NO | Hardware-only |
| Mechanical engineering | NO | Hardware-only (mechanical computing) |
| Formal language theory | NO | Software-only (compiler construction) |
| Automata theory | NO | Software-only |
| Algorithm complexity | NO | Software-only |
| Data structures | NO | Software-only |
| OS design (scheduling, memory mgmt) | NO | Software-only |
| Compiler construction (parsing, codegen) | NO | Software-only |
| Linker/loader design | NO | Software-only |

**Analysis**: Hardware and software share basic binary/Boolean foundations (~10-15% of total knowledge). The von Neumann architecture concept bridges them slightly. But the bulk of knowledge diverges completely: circuit design vs. compiler construction, semiconductor physics vs. automata theory, signal integrity vs. algorithm analysis.

**Verdict: FAIL — ~30% overlap**

### 3.3 Practitioner Profile Overlap: ~20% — FAIL (<50%)

| Dimension | Hardware Engineer | Software Developer |
|-----------|------------------|-------------------|
| **Primary skill** | Circuit design, soldering, PCB layout, signal analysis | Algorithm design, code writing, debugging, abstraction |
| **Tools of daily work** | Oscilloscope, multimeter, soldering station, CAD (EDA tools) | Text editor, compiler, debugger, version control |
| **Training background** | Electrical engineering, physics, mechanical engineering | Computer science, mathematics, formal methods |
| **Error mode** | Short circuit, wrong component, timing violation | Logic bug, off-by-one error, memory leak |
| **Testing method** | Oscilloscope traces, logic analyzer, thermal camera | Unit tests, integration tests, formal verification |
| **Retraining time** | Hardware → software: 1-2 years minimum | Software → hardware: 1-2 years minimum |

**Analysis**: In the bootstrap context, the same individuals may perform both roles. However, the skills and working methods are fundamentally different. A person who can design a TTL circuit is not automatically able to write a compiler — and vice versa. The SIK test measures whether a practitioner "could transition to another sub-area with reasonable retraining (<1 year)" — the answer is clearly no for hardware↔software transitions.

**Verdict: FAIL — ~20% overlap**

### 3.4 SIK Summary

| Dimension | Overlap | Threshold | Result |
|-----------|---------|-----------|--------|
| Physical Infrastructure | ~20% | >50% | **FAIL** |
| Knowledge Base | ~30% | >50% | **FAIL** |
| Practitioner Profile | ~20% | >50% | **FAIL** |

**All three dimensions FAIL the >50% threshold. Software-bootstrapping is a split candidate.**

---

## 4. Split Rule Evaluation

Per schema-spec.md §6.3:

### 4.1 Subgroup Identification

Software construction is the identifiable subgroup within computing that has the lowest infrastructure overlap with the rest of computing (~20%).

### 4.2 Size Check

The subgroup meets the minimum domain size:
- **5 capabilities**: machine-code programming, assemblers, compilers, operating systems, dev tools
- **At least 1 process each**: self-hosting compiler bootstrap, OS kernel construction, etc.
- Well above the "2-3 capabilities with at least 1 process each" minimum

### 4.3 Standalone Viability

Software-bootstrapping can form a standalone domain because:
1. It has a coherent internal narrative (the software bootstrap chain: binary → assembler → compiler → OS → tools)
2. It has clear dependencies on existing domains (computing/, knowledge/) and clear dependents (vlsi-scaling.eda-design, computing itself)
3. It has sufficient content depth (each capability warrants a full Markdown file comparable to existing computing/ files)

---

## 5. Override Conditions Check

### 5.1 Inter-Domain Coupling Override

**Would splitting create tight circular dependencies?**

No. The dependency is strictly one-directional:
- `software-bootstrapping` depends on `computing.electronic` (needs hardware to run)
- `software-bootstrapping` depends on `computing.data-storage` (needs storage for programs)
- `vlsi-scaling.eda-design` depends on `software-bootstrapping.compilers` (needs compiler to build EDA tools)

There is no cycle. Hardware comes first, software second. EDA software comes later but is a downstream consumer, not a circular dependency.

**Verdict: Override does NOT apply. No circular dependency.**

### 5.2 Bootstrap Stage Override

**Are hardware and software tightly coupled in the bootstrap sequence?**

Partially. The electronic.md "Programming" section shows that software concepts (machine code, assembly, compilers) are introduced alongside hardware. However:
- The bootstrap is **sequential**, not simultaneous: build hardware first, then write software for it
- The tight coupling is between `computing.electronic` (builds the computer) and `software-bootstrapping` (makes it useful), which is properly modeled as a dependency edge, not a reason to merge domains
- Similar sequential coupling exists between `foundations` and `metals` — nobody proposes merging those

**Verdict: Override does NOT apply. Coupling is sequential, properly modeled as edges.**

---

## 6. Domain Boundary Definition

### 6.1 Explicit IN List (software-bootstrapping/)

These topics belong in the new domain:

- Machine code programming: hand-entering binary via front-panel switches
- Assembler design and implementation: symbol tables, two-pass assembly, object file formats
- Linker and loader construction: symbol resolution, relocation, loading
- Compiler construction: lexical analysis, parsing, code generation, optimization
- Compiler bootstrapping: the self-hosting bootstrap sequence (write in asm → compile compiler with itself)
- Operating system construction: kernel, process management, memory management, file systems, device drivers
- Programming language design and implementation: interpreters, runtime systems
- Software development tools: text editors, debuggers, build systems, version control
- Algorithms essential for software construction: hash tables (symbol tables), tree traversal (ASTs), sorting (linkers), memory allocation
- Boot loaders and initialization sequences
- Error handling and debugging methodology

### 6.2 Explicit NOT List (stays in computing/)

These topics remain in the existing computing/ domain:

- ALL hardware design and construction (mechanical, electromechanical, electronic)
- Digital logic gate design at transistor level
- Memory cell design (SRAM, DRAM, flash)
- Printed circuit board design and manufacturing
- Vacuum tube and transistor circuit design
- Logic families (TTL, CMOS) as hardware implementations
- Computer architecture (von Neumann, accumulator, register-based) as hardware concepts
- Data storage media manufacturing (magnetic coating, optical pits)
- FPGA architecture and configuration (hardware platform)
- Power supply design for computing equipment
- I/O peripheral hardware design (CRT, keyboard, disk controller)

### 6.3 Gray Zone: How to Handle

Several topics straddle the boundary. Resolution:

| Topic | Home Domain | Rationale |
|-------|-------------|-----------|
| Instruction set architecture (ISA) | `computing.electronic` | ISA is a hardware contract; the hardware implements it |
| How to write a program IN an ISA | `software-bootstrapping.machine-code` | The act of programming, not the ISA spec |
| "Compilers exist" (conceptual mention) | `computing.electronic` | Contextual mention within hardware doc |
| How to BUILD a compiler | `software-bootstrapping.compilers` | The construction process |
| FPGA as a hardware platform | `computing.digital-logic` | Physical device |
| HDL programming for FPGA | `software-bootstrapping.dev-tools` | Software act of programming the FPGA |
| Boot ROM / firmware | Boundary — depends on content | Hardware-spec: computing. Software-prog: software-bootstrapping |

### 6.4 Cross-Reference Protocol

- `computing.electronic` "Programming" section stays but gains a note: "For detailed assembler and compiler construction, see [Software Bootstrapping](../software-bootstrapping/compilers.md)"
- `software-bootstrapping` files reference back to `computing.electronic` for hardware architecture details
- No content duplication — only forward references

---

## 7. Proposed Node List (7 nodes)

| # | Node ID | Level | Name | Description |
|---|---------|-------|------|-------------|
| 1 | `software-bootstrapping` | domain | Software Bootstrapping | Construction of software systems — assemblers, compilers, operating systems, and development tools — that transform computing hardware into programmable machines. Organizing axis: **bootstrap chain** (hand-entered binary → assembler → compiler → OS → dev tools). |
| 2 | `software-bootstrapping.machine-code` | capability | Machine Code & Front-Panel Programming | Hand-entered binary instructions via front-panel switches, hex keyboards, and paper tape bootstrap loaders. The starting point: the first programs are numeric opcodes toggled into memory addresses. |
| 3 | `software-bootstrapping.assemblers` | capability | Assemblers, Linkers & Loaders | Assembly language design (mnemonic opcodes, labels, directives), two-pass assembler construction, symbol table management, relocation, object file formats, and program loading. Assemblers are the first software tool built for any new architecture. |
| 4 | `software-bootstrapping.compilers` | capability | Compiler Construction | Lexical analysis, parsing (recursive descent, operator precedence), abstract syntax trees, code generation, basic optimization (constant folding, dead code elimination), and the self-hosting bootstrap sequence. The compiler is the most complex software bootstrapping challenge. |
| 5 | `software-bootstrapping.operating-systems` | capability | Operating System Construction | From bare-metal monitor programs to multi-tasking OS: boot loaders, interrupt handlers, process scheduling, memory management, file systems, device drivers, and shell/command interpreters. |
| 6 | `software-bootstrapping.dev-tools` | capability | Development Tools & Debugging | Text editors (line editors → screen editors), debuggers (breakpoints, register inspection, memory dumps), build systems (make-like dependency tracking), and basic version control. |
| 7 | `software-bootstrapping.compilers.self-hosting` | process | Self-Hosting Compiler Bootstrap | The specific bootstrap sequence: (1) write minimal compiler in assembly, (2) use it to compile a more capable version of itself written in the source language, (3) discard the assembly version. The moment a compiler can compile itself is the moment the software chain becomes self-sustaining. |

---

## 8. Proposed Edge List (13 edges)

| # | From (dependent) | To (prerequisite) | Type | Rationale |
|---|-----------------|-------------------|------|-----------|
| 1 | `software-bootstrapping` | `computing.electronic` | tool | Software requires electronic computing hardware to run |
| 2 | `software-bootstrapping` | `knowledge` | tool | Software construction requires formal knowledge (mathematics, logic) |
| 3 | `software-bootstrapping.machine-code` | `computing.electronic` | tool | Front-panel programming needs a working computer |
| 4 | `software-bootstrapping.machine-code` | `computing.data-storage` | tool | Bootstrap loaders need paper tape or other storage |
| 5 | `software-bootstrapping.assemblers` | `software-bootstrapping.machine-code` | tool | Assembler itself must first be written in machine code |
| 6 | `software-bootstrapping.compilers` | `software-bootstrapping.assemblers` | tool | Compiler construction requires an assembler to produce object code |
| 7 | `software-bootstrapping.compilers` | `knowledge` | tool | Compiler theory (formal languages, automata) comes from knowledge domain |
| 8 | `software-bootstrapping.compilers.self-hosting` | `software-bootstrapping.compilers` | tool | Self-hosting is a process within compiler capability |
| 9 | `software-bootstrapping.operating-systems` | `software-bootstrapping.assemblers` | tool | OS kernels initially written in assembly language |
| 10 | `software-bootstrapping.operating-systems` | `computing.data-storage` | tool | OS needs persistent storage for file systems |
| 11 | `software-bootstrapping.dev-tools` | `software-bootstrapping.compilers` | tool | Development tools are built using compilers |
| 12 | `software-bootstrapping.dev-tools` | `software-bootstrapping.assemblers` | tool | Some dev tools (debuggers) need assembly-level access |
| 13 | `vlsi-scaling.eda-design` | `software-bootstrapping.compilers` | tool | EDA tools require a compiler to build; this edge supplements the existing edge from eda-design to computing |

---

## 9. Organizing Axis

**Bootstrap Chain** (a variant of chronological):

The capabilities are ordered by the bootstrap sequence in which they appear:

```
machine-code → assemblers → compilers → operating-systems → dev-tools
```

Each capability builds on the one before it. The chain is strictly sequential because each tool is used to build the next:
1. **Machine code** is hand-entered to create the first assembler
2. **Assembler** is used to write the first compiler
3. **Compiler** enables writing the OS in a higher-level language
4. **OS** provides the platform for development tools

This is analogous to the `machine-tools` domain's **Precision Ladder** axis — each stage enables the next with increasing capability.

---

## 10. Impact on Existing Data

### 10.1 Nodes to Add

7 new nodes (listed in §7).

### 10.2 Edges to Add

13 new edges (listed in §8). The existing edge from `vlsi-scaling.eda-design` to `computing` remains — it represents hardware dependency. The new edge from `vlsi-scaling.eda-design` to `software-bootstrapping.compilers` adds the software dependency.

### 10.3 Content Changes to Existing Files

| File | Change | Rationale |
|------|--------|-----------|
| `docs/computing/electronic.md` "Programming" section | Add cross-reference note: "For detailed assembler and compiler construction methodology, see [Software Bootstrapping](../software-bootstrapping/compilers.md)" | Forward reference without content duplication |

No other existing files require changes.

---

## 11. Risk Assessment

### 11.1 Identified Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Content bleed between computing/ and software-bootstrapping/ | HIGH | Explicit IN/NOT lists in §6; gray zone resolution protocol |
| computing.electronic already mentions assemblers/compilers conceptually | MEDIUM | Keep mentions as conceptual context; forward-reference for construction details |
| FPGA programming (HDL) straddles boundary | LOW | Classify HDL programming under software-bootstrapping.dev-tools; FPGA hardware stays in computing.digital-logic |
| EDA dependency edge may seem redundant | LOW | Two edges serve different purposes: hardware dependency (computing) vs. software tool dependency (software-bootstrapping) |

### 11.2 Why This Was Flagged as Highest Risk

The computing/software boundary is inherently fuzzy because:
1. **Architects straddle both**: Computer architects design ISAs (hardware) and write assemblers (software)
2. **Firmware is both**: Boot ROMs are software stored in hardware
3. **Early computing was unified**: In the 1940s-50s, hardware and software were built by the same people
4. **Electronic.md already touches software**: The "Programming" section covers machine code, assembly, and compilers

However, the SIK test's purpose is precisely to resolve these fuzzy boundaries. The three-axis evaluation (infrastructure 20%, knowledge 30%, practitioner 20%) clearly shows that software construction is a distinct domain, even if the boundary has gray zones.

---

## 12. Final Verdict

### SIK Test Results

| Criterion | Verdict | Overlap |
|-----------|---------|---------|
| Physical Infrastructure >50% | **FAIL** (supports split) | ~20% |
| Knowledge Base >50% | **FAIL** (supports split) | ~30% |
| Practitioner Profile >50% | **FAIL** (supports split) | ~20% |

### Override Conditions

| Override | Applies? | Reason |
|----------|----------|--------|
| Inter-domain coupling | NO | No circular dependency; sequential bootstrap |
| Bootstrap stage | NO | Sequential, not simultaneous; properly modeled as edges |

### Domain Size

| Requirement | Met? | Details |
|-------------|------|---------|
| ≥2-3 capabilities | YES | 5 capabilities proposed |
| ≥1 process per capability | YES | 1 process node; each capability implies sub-processes |
| Sufficient for standalone | YES | Each capability warrants a full Markdown file |

### Overall Verdict: **PASS**

The `software-bootstrapping` domain is approved as a new domain with:
- **7 nodes** (1 domain + 5 capabilities + 1 process)
- **13 edges** (connecting to computing/, knowledge/, vlsi-scaling/)
- **Organizing axis**: Bootstrap Chain
- **Boundary**: Explicit IN/NOT lists with gray zone resolution
- **Content scope**: Software construction methodology (how to build assemblers, compilers, OS, dev tools)

---

## Appendix A: Detailed Boundary Analysis with computing/

### A.1 computing.electronic "Programming" Section Review

The electronic.md file contains ~20 lines in a "Programming" section covering:
- Machine code (binary instruction patterns)
- Assembly language (mnemonic representation)
- Assembler (two-pass, symbol table)
- Compiler (Fortran, COBOL, ALGOL)

**Assessment**: These are **conceptual descriptions** — "these things exist and are needed." They describe WHAT software is, not HOW to build it. No overlap with the proposed software-bootstrapping content, which covers construction methodology.

**Action**: Add a single cross-reference sentence after the compiler paragraph. No content removal needed.

### A.2 computing.digital-logic and FPGA

digital-logic.md covers FPGA as a **hardware platform** (configurable logic blocks, lookup tables). The boundary:

- **computing.digital-logic**: FPGA architecture, CLB structure, routing matrix, configuration storage → stays
- **software-bootstrapping.dev-tools**: HDL programming, synthesis tools, place-and-route → new domain

### A.3 computing.data-storage and File Systems

data-storage.md covers physical storage media. The boundary:

- **computing.data-storage**: How magnetic/optical/flash media are manufactured and how they store bits → stays
- **software-bootstrapping.operating-systems**: File system data structures (FAT, inodes, directories) that organize data on the media → new domain

### A.4 The Instruction Set Architecture Boundary

ISA is the sharpest boundary line. Resolution:

- **computing.electronic**: Documents the ISA as a hardware specification (opcodes, registers, addressing modes, interrupt mechanism). The ISA is part of the machine's design.
- **software-bootstrapping.machine-code**: Documents how a programmer USES that ISA (hand-entering opcodes, writing the first test programs). The ISA is a given; the focus is on the programming act.

---

## Appendix B: Comparison with Historical SIK Examples

### B.1 Glass/metals Split (schema-spec.md §6.5 Example 1)

- Infrastructure: ~60%, Knowledge: ~30%, Practitioner: ~20%
- Result: Split (2/3 dimensions below 50%)

### B.2 software-bootstrapping/computing Split (this test)

- Infrastructure: ~20%, Knowledge: ~30%, Practitioner: ~20%
- Result: Split (3/3 dimensions below 50%)

The software-bootstrapping split is even more strongly justified than the glass/metals split. All three dimensions are well below the 50% threshold, not just two.

### B.3 plants/foundations Split (schema-spec.md §6.5 Example 4)

- Infrastructure: ~30%, Knowledge: ~25%, Practitioner: ~20%
- Result: Split (3/3 dimensions below 50%)

The software-bootstrapping split is directly analogous to the plants/foundations split: the subgroup has its own distinct capabilities, its own knowledge base, and serves a fundamentally different purpose. Both are justified by clear SIK divergence plus sufficient domain size.
