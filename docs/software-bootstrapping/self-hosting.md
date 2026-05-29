# Self-Hosting Compiler Bootstrap

> **Node ID**: software-bootstrapping.compilers.self-hosting
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`software-bootstrapping.compilers`](compilers.md)
> **Enables**: Self-sustaining software toolchain — the compiler no longer depends on any other language for its own construction
> **Timeline**: Years 55-70
> **Outputs**: self_hosting_compiler
> **Critical**: Yes — the moment a compiler compiles itself is the moment the software chain becomes self-sustaining; no further assembly or machine code is needed to produce new versions of the compiler

## Problem

Self-hosting is the process by which a compiler for language X is itself written in language X, and can compile its own source code to produce a working copy of itself. This is the keystone of the software bootstrap chain: once achieved, the compiler is self-sustaining — it can be improved, extended, and rebuilt using only its own language, without ever returning to assembly or machine code.

The bootstrap sequence has three phases:
1. **Write a minimal compiler in assembly language** (or machine code). This compiler understands a subset of the target language — enough to compile a simple version of itself.
2. **Write the full compiler in the target language** (the language the compiler compiles). Use the minimal assembly-written compiler to compile this full version.
3. **Use the full compiler to compile itself**. Discard the assembly-written version. The compiler is now self-hosting.

From this point forward, any change to the compiler's source code is compiled by the previous version of the compiler. The chain is unbroken: every version of the compiler is produced by the previous version, tracing back to the original assembly-written seed.

## Prerequisites

- [Compiler Construction](compilers.md) — the compiler being bootstrapped
- [Assemblers, Linkers & Loaders](assemblers.md) — tools needed to build the seed compiler
- [Machine Code & Front-Panel Programming](machine-code.md) — the origin of the bootstrap chain
- [Operating System Construction](operating-systems.md) — file system needed for bootstrap process

## Prerequisites

## Software
- **Working compiler for the target language** ([compilers](compilers.md)): Either a minimal version written in assembly, or a cross-compiler running on a different machine.
- **Assembler** ([assemblers](assemblers.md)): Needed to build the initial seed compiler from assembly source.
- **Operating system with file system** ([operating-systems](operating-systems.md)): The bootstrap process involves many file operations — source files, intermediate files, compiled binaries, test programs.

## Knowledge
- **Complete language specification**: The self-hosted compiler must handle every language feature that appears in its own source code. If the compiler uses feature X, the compiler must be able to compile feature X.
- **Metacircularity**: Understanding that a program can process programs — the compiler is both the tool and the artifact it produces.

## Hardware
- **Sufficient memory**: The compiler compiling itself requires enough memory for the compiler's symbol tables, AST, and code generation during compilation of its own (large) source file. Typically 2-4× the memory needed to compile a normal program.

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| Working seed compiler (assembly-written) | 1 instance | [compilers](compilers.md) | Cross-compiler on host machine |
| Compiler source code (in target language) | 1 file, 5,000-50,000 lines | Written by developer | N/A |
| Disk storage | ≥500 KB | [computing.data-storage](../computing/data-storage.md) | Multiple tapes (slow but functional) |
| Test programs | 20-100 files | Written by developer | Existing program library |

## Process Description

## Phase 1: Write the Seed Compiler in Assembly

Write a minimal compiler in assembly language that understands enough of the target language to compile a simplified version of itself.

**Seed compiler requirements**:
- Lexical analysis (tokenizer)
- Parser for a subset of the language (no fancy features — basic types, functions, if/else, while, expressions)
- Code generation (simple, no optimization)
- Symbol table management
- File I/O (read source, write assembly output)

**Seed compiler size**: 2,000-8,000 lines of assembly language. This is a significant effort — 1-4 months of full-time work for an experienced assembly programmer.

**Seed language subset**: Intentionally limited to features needed by the full compiler:
- Integer types only (no structs, no floats)
- Functions with parameters and return values
- If/else, while loops
- Basic arithmetic and comparison operators
- Arrays (for symbol table, buffers)
- No separate compilation (one source file only)

## Phase 2: Write the Full Compiler in the Target Language

Using the seed compiler to test incrementally, write the full compiler in the target language:

**Development strategy**:
1. Write the lexer in the target language. Compile with the seed compiler. Test.
2. Write the parser in the target language. Compile with the seed compiler. Test.
3. Write the semantic analyzer. Compile. Test.
4. Write the code generator. Compile. Test.
5. Write the optimizer passes. Compile. Test.
6. Assemble all components into the full compiler source.

**Testing at each step**: After writing each component, compile it with the seed compiler and run test programs. Fix any bugs in both the component and the seed compiler (the seed compiler may have limitations that surface when compiling more complex code).

## Phase 3: The Self-Compilation (T0 — Bootstrap Moment)

This is the critical moment — compile the full compiler with itself:

1. **Compile the full compiler source using the seed compiler**:
   ```
   seed_compiler full_compiler.src -o full_compiler_v1.bin
   ```
   This produces the first binary of the full compiler, compiled from the target language source.

2. **Compile the full compiler source using the full compiler v1**:
   ```
   full_compiler_v1.bin full_compiler.src -o full_compiler_v2.bin
   ```
   This produces the second binary, compiled by the compiler itself.

3. **Verify v1 and v2 are functionally identical**:
   - Both binaries should produce the same output when compiling any test program.
   - If they differ, there is a bug — the compiler is miscompiling some feature that it uses internally.
   - Fix the bug and repeat from step 1.

4. **Discard the seed compiler**: Once v1 and v2 agree, the seed compiler is no longer needed. The full compiler is self-hosting.

**Verification protocol**:
```
# Compile test suite with v1 and v2 — outputs must match
full_compiler_v1.bin test_program.src -o test_v1.bin
full_compiler_v2.bin test_program.src -o test_v2.bin
diff test_v1.bin test_v2.bin   # Must show no differences

# Run compiled test programs — results must be correct
run test_v1.bin   # Produces expected output
run test_v2.bin   # Produces identical expected output
```

## Phase 4: Iterative Improvement

Once self-hosting is achieved, the compiler can be improved using itself:

1. Add a new optimization pass to the compiler source code.
2. Compile the modified source with the current compiler.
3. The new binary is both the improved compiler AND the output of the previous version.
4. Verify: compile a test program with both old and new compilers. If the new one generates better code (smaller, faster, or both) without breaking correctness, the improvement is accepted.

**Retrograde bug risk**: A bug introduced into the compiler can propagate through self-compilation. If version N has a bug that miscompiles feature X, and the compiler's own source uses feature X, version N+1 will be miscompiled. Always maintain a known-good backup binary.

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Seed compiler development time | 1-4 months | Assembly language, one developer |
| Seed compiler size | 2,000-8,000 lines of assembly | Minimal language subset |
| Full compiler source size | 5,000-50,000 lines | Depends on language complexity |
| Self-compilation time (v1 → v2) | 5-60 min | Depends on machine speed and compiler size |
| Memory for self-compilation | 2-4× normal compilation | Compiler source is large; symbol tables are big |
| Verification test suite size | 20-100 test programs | Cover all language features |
| Bootstrap iterations (typical) | 3-10 | Bug-fix cycles before v1 and v2 agree |
| Total bootstrap effort | 6-18 months | From start to self-hosting, one developer |

## Bootstrap Complexity by Language

| Language Complexity | Seed Compiler LOC | Full Compiler LOC | Bootstrap Effort |
|--------------------|--------------------|--------------------|-----------------|
| Minimal (Forth-like) | 500-1,500 | 2,000-5,000 | 1-3 months |
| Simple (C-like, no structs) | 2,000-5,000 | 10,000-20,000 | 3-6 months |
| Moderate (C with structs) | 3,000-8,000 | 20,000-50,000 | 6-12 months |
| Complex (C++, Rust-like) | 10,000-30,000 | 50,000-200,000 | 1-3 years |

## Scaling Notes

**From seed to full**: The seed compiler implements only the minimal language subset. The full compiler adds all remaining features. Each new feature is tested by: (1) adding it to the source, (2) compiling with the seed compiler, (3) running the resulting binary on test programs.

**From single-pass to optimizing**: The initial self-hosted compiler may be simple (no optimization). Optimization passes are added incrementally — each pass is tested by re-compiling the compiler with itself and verifying that generated code quality improves without breaking correctness.

**Cross-compilation alternative**: If a working computer with an existing compiler is available, the entire bootstrap can be done as cross-compilation. Write the full compiler on the host machine (using the host's language and tools), generate target-machine code, and transfer the binary to the target. This eliminates the need for a seed compiler entirely.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| v1 and v2 binaries differ | Bug in code generation for a feature the compiler uses internally | Binary diff the outputs; find the first differing instruction; trace back to the source construct that generates it; fix the code generator |
| v2 crashes when compiling | Bug in compiler's own code that only manifests at larger scale (stack overflow, memory corruption) | Run v2 with verbose logging; compare memory layout with v1; check for buffer overflows in the compiler's own symbol table |
| Self-compilation takes too long | Quadratic algorithm in the compiler (e.g., linear symbol table search) | Profile the compilation; identify the bottleneck; optimize the specific algorithm (usually symbol table lookup or parser backtracking) |
| Compiler works but generated code is wrong | Subtle bug in code generation that doesn't affect the compiler's own execution but affects generated programs | Test with programs that exercise edge cases (deeply nested expressions, many variables, recursive calls) |
| Cannot add a new feature because the seed compiler doesn't support it | Seed compiler's language subset is too limited | Extend the seed compiler's assembly source to support the new feature, then re-bootstrap |

## Safety

- **Always keep a known-good binary**: Before modifying the compiler source, save a backup copy of the current working compiler binary. If the modified compiler fails to compile itself correctly, revert to the backup. Never delete the only working copy.
- **Verify after every change**: After any change to the compiler source, re-bootstrap and verify that v1 and v2 agree. Do not accumulate multiple changes without verification — debugging is much harder with multiple interacting changes.
- **No physical hazards**: Self-hosting is a purely software process. The risks are data integrity and lost time, not physical harm.

## Quality Control

**Bootstrap verification protocol**:
1. Compile compiler source with current compiler → produce binary A.
2. Compile compiler source with binary A → produce binary B.
3. Compile a comprehensive test suite with both A and B.
4. Compare outputs: all generated binaries must be byte-identical.
5. Run all generated test programs: all outputs must be correct.

**Regression test suite**: Maintain a library of programs that exercise every language feature. Run this suite after every compiler change. Any failure means the change introduced a bug.

**Performance benchmark**: Compile a standard benchmark program with each compiler version. Track compilation time and generated code quality over time. Regression in either metric signals a problem.

## Variations and Alternatives

| Bootstrap Method | Effort | Risk | Best For |
|-----------------|--------|------|----------|
| Assembly seed → self-host | High | Medium | When no other compiler exists |
| Cross-compile from host | Medium | Low | When a host machine with tools is available |
| Interpret a subset first | Low | Low | Rapid prototyping, validate language design |
| Staged: interpreter → simple compiler → full compiler | Medium | Low | Incremental approach with checkpoints |

**The Ken Thompson trick**: In his 1984 Turing Award lecture, Thompson demonstrated that a self-hosting compiler can contain a hidden "backdoor" — the compiler can be modified to inject malicious code into a specific program (like the login command) whenever it compiles it, and this injection persists through self-compilation. The lesson: the only way to trust a self-hosted compiler is to audit the source code (and verify that the binary matches the audited source).

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Bootstrap fails — stage 2 compiler crashes | Stage 1 (seed) compiler has a bug in a rarely-used code path | Reduce stage 2 source to minimal subset that compiles successfully; add one feature at a time; add diagnostics to stage 1 |
| Self-compilation produces different binary each time | Non-deterministic behavior (timestamps, hash ordering, uninitialized memory) | Eliminate all sources of non-determinism; fix uninitialized variables; use deterministic hash tables |
| Stage 2 compiler runs but produces wrong code | Bug in code generation that only triggers when compiling complex programs | Write targeted test programs that exercise each code generation path; compare stage 2 output against stage 1 output |
| Bootstrap works on one machine but fails on another | Endianness, word size, or ABI differences | Use fixed-width integer types; avoid pointer-to-integer casts; test on both architectures during development |
| Compiler cannot find its own runtime library | Search path hardcoded relative to build directory | Use relative paths based on compiler executable location; add configurable library search path |
| Regression — new compiler version breaks existing programs | Silent semantics change in language or code generation | Maintain comprehensive test suite; run all tests before accepting any compiler change; bisect to find failing commit |

## See Also

- [Compiler Construction](compilers.md) — the compiler being bootstrapped
- [Assemblers, Linkers & Loaders](assemblers.md) — tools needed to build the seed compiler
- [Machine Code & Front-Panel Programming](machine-code.md) — the origin of the bootstrap chain
- [Operating System Construction](operating-systems.md) — file system needed for bootstrap process
- [Electronic Computing](../computing/electronic.md) — hardware that runs the compiled compiler

[← Back to Software Bootstrapping](index.md)
