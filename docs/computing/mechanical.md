# Mechanical Calculation

> **Node ID**: computing.mechanical
> **Domain**: Computing & Automation
> **Timeline**: Years 10-40
> **Outputs**: calculation_aids

### Manual Calculation Aids

**Abacus**:
- **Construction**: Wooden frame with horizontal rods. Beads on each rod — upper beads (heaven beads, value 5 each) and lower beads (earth beads, value 1 each). Standard suanpan: 2 upper + 5 lower beads per rod. Soroban: 1 upper + 4 lower.
- **Operation**: Slide beads toward center bar to add, away to subtract. Each rod = one decimal place. Rightmost rod = ones, next = tens, etc. Carry: when lower beads exceed 4, reset and move one upper bead. When upper bead is used and lower beads exceed 4, reset both and carry 1 to next rod left.
- **Speed**: Trained operators perform addition/subtraction faster than electronic calculator data entry. 10-20 operations per second on sustained calculations. The abacus remains competitive for bulk arithmetic well into the electronic age.

**Slide rule**:
- **Principle**: Two logarithmic scales — sliding one scale relative to the other performs multiplication and division by adding/subtracting logarithms. log(a × b) = log(a) + log(b).
- **Construction**: Three strips of wood, plastic, or bamboo. Outer two fixed, middle strip slides. Cursor (transparent sliding window with hairline) for precise reading. Scale length typically 25 cm (10-inch rule).
- **Scales**: C and D scales (basic multiplication/division, 1-10 range). A and B (squares, 1-100 range). K (cubes). CI (reciprocal). S, T, ST (sine, tangent, small angles). L (linear, for reading log values directly).
- **Slide rule construction detail**: Lay out logarithmic scales using log₁₀ values — mark positions at log₁₀(n) × scale_length for each integer n from 1 to 10. For a 25 cm rule, mark 1 at 0 cm, 2 at 7.53 cm (log10(2)×25), 3 at 11.93 cm, etc. Engine-divide into subdivisions for 3-figure reading. Cursor: transparent celluloid or glass strip with fine hairline, held in spring-loaded frame sliding on body. Cursor enables precise alignment between non-adjacent scales and prevents parallax error.
- **Precision**: 3 significant figures typical for 25 cm rule. Longer rules (50 cm) give 4 figures. Precision limited by visual interpolation between graduations.
- **Operation for multiplication**: To compute a × b: slide C scale so its 1 align with a on D scale. Read result at b on C scale against D scale. Division: slide C scale so b align with a on D scale. Read result at 1 on C against D scale.
- **Applications**: Engineering calculations (stress, power, flow rates, electrical parameters), chemical stoichiometry, heat transfer, structural design. A single slide rule replaces hours of hand calculation with log tables.

**Nomograms**:
- **Principle**: Diagram with two or more scaled axes. Place straightedge connecting known values on two axes → read result on third axis. Instant calculation for specific formulas.
- **Construction**: Derive scale equations from formula. For formula Z = f(X, Y), compute scale positions for X and Y axes. Compute Z scale positions. Draw parallel or angled lines with graduated marks. Each nomogram encodes ONE specific formula.
- **Applications**: Ohm's law (V = IR), pipe flow (Hazen-Williams), heat transfer (Q = UAΔT), resistor color code, drill speed/feed for various materials. Print in technical manuals for rapid field use.

**Mathematical tables**:
- Pre-computed reference books with values of logarithms (4-6 place), trigonometric functions (sin, cos, tan for every arc-minute), exponential and hyperbolic functions, square and cube roots, unit conversion factors.
- **Production**: Compute by difference methods (add small increments using known derivatives). Typeset and print via printing press (Knowledge Preservation). Multiple proofreaders verify against independent calculations. Errors in tables cause engineering failures — accuracy is paramount.
- **Use**: Look up log values for multiplication/division (antilog for results). Look up trig values for surveying and engineering. Faster than slide rule for high precision (5-6 figures). Slower for 3-figure work.

### Mechanical Calculators

**Gear-based adder (Pascaline-type)**:
- **Principle**: Rotating digit wheel with 10 positions (0-9). When wheel passes from 9 to 0, mechanical carry mechanism advances next wheel by one position.
- **Construction**: Brass or steel digit wheels on common shaft. Each wheel has 10 teeth on one face and a single projecting pin on the other. When wheel completes full revolution, pin engages carry lever → advances next wheel by one position. Input by stylus rotating wheels to desired digits. Addition by rotating input wheels forward. Subtraction by rotating backward (or complement method).
- **Capability**: Addition, subtraction (and by repetition, multiplication and division). 6-8 digit capacity. Speed: faster than mental arithmetic for sums of many numbers.

**Stepped drum calculator (Leibniz/Arithmometer-type)**:
- **Principle**: Stepped drum (cylinder with teeth of increasing length: 1-tooth, 2-tooth... 9-tooth) engages with sliding gear. Position of sliding gear determines how many teeth engage → how many positions output wheel advances per drum revolution. One drum per digit position.
- **Operation**: Set input digits by positioning sliding gears (levers or knobs). Turn crank → drums rotate → each output wheel advances by input digit value. Carries propagate between digits automatically. Multiple crank turns = multiplication by number of turns. Division by repeated subtraction.
- **Capability**: Direct multiplication and division. 8-12 digit input, 16-20 digit accumulator. Speed: multiplication of two 8-digit numbers in ~15 seconds. The workhorse mechanical calculator from ~1820 to ~1960.
- **Construction requirements**: Precision gear-cutting, milling, drilling, and finishing — Machine Tools stage machine shop capability essential. Each calculator contains 1000-3000 precision parts. Manufacturing time: 100-300 skilled labor-hours per unit.

**Difference Engine** (Babbage-type):
- **Purpose**: Automatically tabulate polynomial functions. Compute mathematical tables (logarithms, trigonometric) without human error.
- **Principle**: Finite differences — any polynomial of degree n can be computed by repeated addition using n+1 columns of differences. Example: for quadratic ax² + bx + c, maintain three columns: value, first difference, second difference. Add second difference to first difference, then first difference to value. Repeat. Each step = next table entry.
- **Construction**: Columns of toothed wheels (31 digits per column, 7 columns for 6th-order polynomial). Each column adds to next via intricate carry mechanism. Crank handle drives all additions simultaneously. Automatic printing of results (inked type wheels impress onto paper, also into plaster or soft metal for stereotype printing plates).
- **Capability**: Tabulate any polynomial to 31-digit precision. Compute tables of logarithms, trigonometric functions, actuarial tables, ballistic trajectories. Eliminate human calculation errors from published tables.
- **Manufacturing challenge**: Requires thousands of parts with tolerances of ±0.025 mm. Precision casting, gear-cutting, milling, grinding. the Machine Tools stage are sufficient. Assembly and adjustment by skilled mechanic over weeks-months.

**Babbage Analytical Engine** (conceptual, requires advanced Machine Tools):
- **Store**: Columns of toothed wheels representing variable values (1000 columns × 50 digits each proposed). Memory for data and intermediate results — the conceptual ancestor of RAM.
- **Mill**: Set of gears and carries that perform arithmetic operations (add, subtract, multiply, divide) on values fetched from the store. The conceptual ancestor of the CPU. Operation selected by control cards.
- **Input**: Punched cards (adapted from Jacquard loom) — operation cards specify which calculation to perform, variable cards specify which store columns to read/write. Program = sequence of cards. Conditional branching achieved by reversing card chain direction (advance or back up based on result sign). The first general-purpose programmable computer concept, though never completed in Babbage's lifetime.

*Part of the [Bootciv Tech Tree](../) • [Computing](./) • [All Domains](../)*

