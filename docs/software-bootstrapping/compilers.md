# Compiler Construction

> **Node ID**: software-bootstrapping.compilers
> **Domain**: [Software Bootstrapping](./index.md)
> **Dependencies**: [`software-bootstrapping.assemblers`](assemblers.md), [`knowledge`](../knowledge/index.md)
> **Enables**: [`software-bootstrapping.operating-systems`](operating-systems.md), [`software-bootstrapping.dev-tools`](dev-tools.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 55-70
> **Outputs**: compiled_programs, high_level_languages
> **Critical**: Yes — compilers enable programming at human-readable abstraction levels, a 5-10× productivity multiplier over assembly language


A compiler translates programs written in a high-level language (Fortran, C, Pascal, or any similar language) into machine code or assembly language. Where assembly language provides a one-to-one mnemonic mapping to machine instructions, a high-level language lets the programmer express algorithms in terms of variables, expressions, loops, and functions — the compiler handles register allocation, instruction selection, and address management.

The compiler is the most complex software bootstrapping challenge. A simple two-pass assembler might be 1,000-2,500 lines of code; a working compiler is 5,000-50,000 lines depending on language complexity and optimization level. The bootstrap problem is acute: to compile a program, you need a compiler; to build a compiler, you need a compiler. The solution is the [self-hosting bootstrap](self-hosting.md) sequence.

Compilers unlock a fundamental productivity leap. A programmer can write 5-10× more functionality per day in a high-level language compared to assembly, because the compiler handles the tedious details of instruction encoding, register management, and calling conventions. This productivity multiplier is what makes operating systems, applications, and development tools feasible at scale.

## Prerequisites

## Software
- **Working assembler** ([assemblers](assemblers.md)): The compiler's code generator produces assembly output (or object code directly). The assembler is part of the toolchain.
- **Linker and loader** ([assemblers](assemblers.md)): Compiled programs may reference external libraries; the linker resolves these references.

## Knowledge
- **Formal language theory**: Regular expressions (for lexical analysis), context-free grammars (for parsing), automata theory.
- **Data structures**: Trees (abstract syntax trees), hash tables (symbol tables), stacks (parsing, code generation).
- **Algorithms**: Tree traversal, graph coloring (register allocation), topological sort (dependency analysis).
- **Target ISA**: Complete knowledge of the machine's instruction set, register set, and calling conventions.

## Hardware
- **Computer with ≥32 KB memory**: A compiler needs significantly more memory than an assembler — the symbol table, parse tree, and intermediate representations are all memory-intensive. 32-128 KB is realistic for a basic compiler.
- **Adequate storage**: Source files, intermediate files, and generated assembly/object files. Magnetic storage (disk or tape) is essentially required; paper tape is too slow for compiler I/O.

## Bill of Materials

| Item | Quantity | Source | Alternatives |
|------|----------|--------|-------------|
| Computer with ≥32 KB memory | 1 unit | [computing.electronic](../computing/electronic.md) | Cross-compile on host machine |
| Magnetic storage (disk/tape) | Adequate | [computing.data-storage](../computing/data-storage.md) | Paper tape (impractical for compilation speed) |
| Working assembler | 1 unit | [assemblers](assemblers.md) | Compiler generates binary directly (skips assembly step) |
| Formal language reference | 1 document | [knowledge](../knowledge/index.md) | Textbook on compiler construction |

## Process Description

## Phase 1: Lexical Analysis (Scanning)

The lexical analyzer (scanner) reads the source program character by character and groups characters into tokens — the smallest meaningful units of the language.

**Token types for a simple language**:
| Token Type | Examples | Description |
|------------|----------|-------------|
| IDENTIFIER | x, count, total_sum | Variable and function names |
| NUMBER | 42, 3.14, 0xFF | Numeric literals |
| KEYWORD | if, while, return, int | Reserved words |
| OPERATOR | +, -, *, /, ==, < | Arithmetic and comparison |
| DELIMITER | (, ), {, }, ;, , | Punctuation |
| STRING | "hello world" | String literals |

**Implementation**: A finite automaton. For each character, determine whether to continue the current token or start a new one. Identifiers: start with a letter, continue with letters and digits. Numbers: digits, optionally with a decimal point. Operators: single or double character (distinguish `=` from `==`, `<` from `<=`).

**Output**: A stream of tokens, each with type and value. Example: `x = 42 + y;` → `IDENT(x) ASSIGN NUMBER(42) PLUS IDENT(y) SEMI`

## Phase 2: Parsing (Syntax Analysis)

The parser consumes the token stream and builds a parse tree (or abstract syntax tree — AST) that represents the program's grammatical structure.

**Grammar example** (simplified expression grammar):
```
expr    → expr + term | expr - term | term
term    → term * factor | term / factor | factor
factor  → NUMBER | IDENTIFIER | ( expr )
```

**Recursive descent parser**: The most straightforward approach for bootstrap compilers. Write one function per grammar rule. Each function consumes tokens and returns a tree node:

```
parseExpr():
    left = parseTerm()
    while currentToken is PLUS or MINUS:
        op = currentToken
        advance()
        right = parseTerm()
        left = BinaryOp(op, left, right)
    return left

parseTerm():
    left = parseFactor()
    while currentToken is STAR or SLASH:
        op = currentToken
        advance()
        right = parseFactor()
        left = BinaryOp(op, left, right)
    return left

parseFactor():
    if currentToken is NUMBER:
        return NumberLiteral(currentToken.value)
    if currentToken is IDENTIFIER:
        return Variable(currentToken.value)
    if currentToken is LPAREN:
        advance()
        expr = parseExpr()
        expect(RPAREN)
        return expr
```

**Output**: An abstract syntax tree. For `x = 42 + y`:

```
      ASSIGN
     /      \
   x        ADD
           /   \
         42     y
```

## Phase 3: Semantic Analysis

Walk the AST and perform:
- **Type checking**: Verify that operators have compatible operand types. `int + int → int`. Flag type mismatches as errors.
- **Symbol table construction**: For each scope (global, function, block), record variable names, types, and storage locations (stack offset, register, memory address).
- **Declaration checking**: Verify that every variable used has been declared (or is a built-in).

## Phase 4: Code Generation

Walk the AST and emit assembly code (or machine code directly) for each node:

**Simple code generation for expressions**:
```
genCode(ASSIGN node):
    genCode(right_child)     ; Result left in accumulator
    emit "STA address_of_left_child"  ; Store to variable

genCode(ADD node):
    genCode(left_child)      ; Left operand in accumulator
    emit "PUSH ACC"          ; Save accumulator
    genCode(right_child)     ; Right operand in accumulator
    emit "POP TEMP"          ; Restore left to temp register
    emit "ADD TEMP, ACC"     ; Add

genCode(NUMBER node):
    emit "LDA value"         ; Load immediate

genCode(VARIABLE node):
    emit "LDA address_of_variable"
```

**Function call convention**: The compiler must establish a calling convention — how arguments are passed, where the return value goes, who saves and restores registers:
1. Caller pushes arguments onto the stack (right to left or left to right)
2. Caller executes CALL (pushes return address)
3. Callee pushes saved registers, allocates local variables on the stack
4. Callee executes, places return value in designated register
5. Callee pops saved registers, executes RET
6. Caller pops arguments from the stack

## Phase 5: Basic Optimization

Even a simple compiler should perform these optimizations:

**Constant folding**: Evaluate constant expressions at compile time. `2 + 3 * 4` → `14` in the generated code, not a runtime computation.

**Dead code elimination**: Remove code that can never execute (code after a return statement, unreachable branches of constant conditions).

**Strength reduction**: Replace expensive operations with cheaper ones. `x * 2` → `x + x` or `x << 1` (shift is faster than multiply on most processors).

**Register allocation**: Use registers efficiently instead of loading and storing every temporary to memory. Even simple linear scan allocation (assign variables to registers in order of first use, spill to stack when registers run out) provides significant speedup.

## Quantitative Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Compilation speed | 10-100 lines/sec | Depends on machine speed and I/O |
| Compilation time (10,000-line program) | 2-15 min | On vintage hardware; seconds on modern machines |
| Compiler memory requirement | 32-128 KB | Code + AST + symbol tables + buffers |
| Generated code size ratio | 1.2-3× assembly | Compiled code is larger than hand-tuned assembly |
| Execution speed ratio | 0.5-0.9× hand assembly | Compiled code is slower than hand-optimized assembly |
| Programmer productivity | 5-10× assembly | Lines of correct functionality per day |
| Basic compiler size | 5,000-15,000 lines | Minimal language, no optimization |
| Optimizing compiler size | 20,000-100,000 lines | Significant optimization passes |
| Symbol table size (1,000 names) | 10-30 KB | Name + type + scope + address |

## Language Feature Complexity

| Feature | Additional Lines of Code | Difficulty |
|---------|------------------------|------------|
| Integer arithmetic + variables | 2,000-3,000 (baseline) | Moderate |
| If/else branching | +500-800 | Easy |
| While/for loops | +500-800 | Easy |
| Functions with arguments | +1,000-2,000 | Moderate |
| Arrays with indexing | +500-1,000 | Moderate |
| Structs/records | +1,000-2,000 | Moderate |
| Pointers | +1,500-3,000 | Hard |
| Strings | +800-1,500 | Moderate |
| Type checking | +1,000-2,000 | Moderate |
| Separate compilation | +2,000-4,000 | Hard |

## Scaling Notes

**From interpreter to compiler**: An interpreter is simpler to build (no code generation phase — evaluate the AST directly). An interpreter for a simple language might be 2,000-5,000 lines. Start with an interpreter to validate the language design, then build a compiler for performance.

**From single-pass to multi-pass**: The simplest compiler reads source and emits code in one pass (no AST construction). This limits optimization but is the fastest approach. A multi-pass compiler builds an AST, performs analysis and optimization, then generates code. Each additional pass adds capability but increases compilation time and memory usage.

**From basic to optimizing**: The first compiler should focus on correctness — generate correct code, even if inefficient. Optimization passes (constant folding, dead code elimination, register allocation, instruction scheduling) are added incrementally. Each optimization pass adds 1,000-5,000 lines and 10-30% to compilation time.

**From one language to many**: Once the compiler framework works, the front end (lexer + parser) can be replaced for different source languages while keeping the same back end (code generator + optimizer). This is the "retargetable compiler" approach. Each new language front end costs 2,000-5,000 lines.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Generated code crashes | Wrong calling convention; stack misalignment; missing register save/restore | Trace through the generated assembly for a simple test function; compare to hand-written equivalent |
| Wrong results from arithmetic | Operator precedence error in parser; type conversion bug | Test each operator individually with known inputs and outputs |
| "Stack overflow" at compile time | Recursive parser hitting infinite recursion (left-recursive grammar) | Rewrite grammar to eliminate left recursion; or add recursion depth limit |
| Compilation takes too long | Quadratic algorithm (e.g., linear search in symbol table) | Replace linear search with hash table lookup |
| "Out of memory" during compilation | AST too large for available memory | Process functions independently (free each function's AST after code generation); use disk-based intermediate storage |
| Miscompiled large functions | Register allocator spills incorrectly; code generation bug for edge case | Reduce function size; test with simpler functions first; add diagnostic output showing register allocation decisions |

## Safety

- **No physical hazards**: Compiler construction is purely intellectual work.
- **Mental fatigue**: Debugging a miscompiling compiler is among the most mentally taxing software debugging tasks. The bug could be in the lexer, parser, semantic analyzer, or code generator — and the only symptom is wrong output from the compiled program. Take frequent breaks.
- ** Frustration management**: A miscompiling compiler can waste hours of debugging time on the wrong hypothesis. Always test with the simplest possible program that demonstrates the bug before investigating complex cases.

## Quality Control

**Compiler test suite**: A comprehensive compiler test covers:
1. **Lexical tests**: Every token type, boundary cases (empty strings, very long identifiers, all operators)
2. **Parsing tests**: Every grammar rule, error cases (missing semicolons, unbalanced parentheses)
3. **Code generation tests**: Every operator, every statement type, function calls, recursion
4. **End-to-end tests**: Known programs with known expected output (e.g., compute factorial of 10 = 3,628,800; sort an array and verify order)

**Regression testing**: Every change to the compiler should be validated against the full test suite. Keep a library of test programs and their expected outputs.

## Variations and Alternatives

| Approach | Complexity | Performance | Best For |
|----------|-----------|-------------|----------|
| Interpreter | Low (2-5K LOC) | 10-100× slower than compiled | Rapid prototyping, teaching |
| Simple compiler (no optimization) | Medium (5-15K LOC) | 0.5-0.8× hand assembly | First compiler, bootstrapping |
| Optimizing compiler | High (20-100K LOC) | 0.8-1.2× hand assembly | Production use |
| Threaded code interpreter (Forth-style) | Low (1-3K LOC) | 3-10× slower than compiled | Minimal footprint, fast implementation |
| Transpiler (to C or assembly) | Medium | Depends on target compiler | Leveraging existing compiler back end |

## See Also

- [Assemblers, Linkers & Loaders](assemblers.md) — The prerequisite toolchain
- [Self-Hosting Compiler Bootstrap](self-hosting.md) — Making the compiler compile itself
- [Knowledge](../knowledge/index.md) — Formal language theory, automata, data structures
- [Electronic Computing](../computing/electronic.md) — Target ISA and processor architecture
- [Development Tools](dev-tools.md) — Editors and debuggers for writing compilers


[← Back to Software Bootstrapping](index.md)
