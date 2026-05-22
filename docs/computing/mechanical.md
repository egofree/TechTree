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

**[Difference Engine](../glossary/difference-engine.html)** (Babbage-type):
- **Purpose**: Automatically tabulate polynomial functions. Compute mathematical tables (logarithms, trigonometric) without human error.
- **Principle**: Finite differences — any polynomial of degree n can be computed by repeated addition using n+1 columns of differences. Example: for quadratic ax² + bx + c, maintain three columns: value, first difference, second difference. Add second difference to first difference, then first difference to value. Repeat. Each step = next table entry.
- **Construction**: Columns of toothed wheels (31 digits per column, 7 columns for 6th-order polynomial). Each column adds to next via intricate carry mechanism. Crank handle drives all additions simultaneously. Automatic printing of results (inked type wheels impress onto paper, also into plaster or soft metal for stereotype printing plates).
- **Capability**: Tabulate any polynomial to 31-digit precision. Compute tables of logarithms, trigonometric functions, actuarial tables, ballistic trajectories. Eliminate human calculation errors from published tables.
- **Manufacturing challenge**: Requires thousands of parts with tolerances of ±0.025 mm. Precision casting, gear-cutting, milling, grinding. The Machine Tools stage is sufficient. Assembly and adjustment by skilled mechanic over weeks-months.

**[Babbage Analytical Engine](../glossary/babbage-analytical-engine.html)** (conceptual, requires advanced Machine Tools):
- **Store**: Columns of toothed wheels representing variable values (1000 columns × 50 digits each proposed). Memory for data and intermediate results — the conceptual ancestor of RAM.
- **Mill**: Set of gears and carries that perform arithmetic operations (add, subtract, multiply, divide) on values fetched from the store. The conceptual ancestor of the CPU. Operation selected by control cards.
- **Input**: Punched cards (adapted from Jacquard loom) — operation cards specify which calculation to perform, variable cards specify which store columns to read/write. Program = sequence of cards. Conditional branching achieved by reversing card chain direction (advance or back up based on result sign). The first general-purpose programmable computer concept, though never completed in Babbage's lifetime.

### Specialized Calculation Devices

**[Napier's bones](../glossary/napiers-bones.html)** (multiplication rods):
- **Construction**: Ten rectangular rods (numbered 0-9), each divided into nine squares. Each square shows the product of the rod's digit multiplied by the row number (1-9), with tens above a diagonal line and units below. An eleventh rod serves as the multiplier index.
- **Operation**: Arrange rods side by side to form the multiplicand digits. Read across the row corresponding to the multiplier digit, adding diagonal pairs to get partial products. Multi-digit multiplication requires one row per multiplier digit, with positional offset.
- **Speed**: Multiplication of two 4-digit numbers in 30-60 seconds. Reduces multiplication to a lookup and addition task, eliminating the need to memorize multiplication tables beyond single digits.
- **Materials**: Wood, ivory, bone, or metal. Engraved or stamped markings. Requires only basic crafting skills.

**[Mechanical integrators](../glossary/mechanical-integrators.html)** (analog computing):
- **Ball-and-disk integrator**: A steel ball sits between a rotating disk and a cylindrical output roller. The ball contacts the disk at a radial position set by an input shaft. The disk rotates at constant speed. The ball transmits rotation to the output roller at a rate proportional to the ball's radial position (distance from disk center). Moving the ball outward increases the output roller speed. This multiplies a continuous variable (ball position = input) by another (disk rotation = time or another variable). Output: rotation angle = integral of input over time.
- **Accuracy**: ±0.5-1% of full scale. Limited by ball slip, friction, and mechanical play.
- **Applications**: Fire control computers (naval gunnery, anti-aircraft), where target range, bearing, speed, and wind must be integrated continuously. Differential analyzers (Bush-type, 1930s): arrays of integrators connected by shafts solve differential equations mechanically. These were the primary computing engines for scientific problems before electronic computers.

**Cam-based function generators**:
- **Principle**: A cam with a carefully shaped profile converts uniform input rotation into a follower displacement that represents a mathematical function. The cam profile is the function "writ large" in metal.
- **Design**: For function y = f(x), compute follower displacement at many x values. Transfer these displacements to the cam blank via dividing head and milling machine. The result is a cam that "computes" the function in real time as it rotates.
- **Common functions**: Sine/cosine (eccentric circular cam), square root (specially profiled cam), logarithmic cam for range correction in fire control. Combinations of cams and linkages compute multi-variable functions.
- **Accuracy**: Limited by machining precision, typically ±0.1-0.5% of full-scale output. Cam wear degrades accuracy over time — hardened steel surfaces are essential.

**[Curta calculator](../glossary/curta-calculator.html)** (handheld stepped drum):
- **Design**: Cylindrical housing containing a stepped drum mechanism miniaturized to handheld size. Input sliders on the barrel set digits. Crank handle on top performs addition. Multiplication by repeated cranking with carriage shift. Subtraction via complement method with reversed crank direction (crank folds out for subtraction).
- **Capacity**: 11-digit input, 15-digit result counter, 8-digit revolution counter. Weighs ~230 g.
- **Manufacturing**: Requires 605 precision parts. Machining tolerances ±0.01 mm on critical dimensions. The most complex mechanical calculator produced in significant numbers (~80,000 units). Demonstrates the upper limit of purely mechanical calculation before electronics.

### Mechanical Memory and Counting

**Counter wheels and registers**:
- **Decade counter**: Ten-tooth ratchet wheel with detent. Each input pulse (via electromagnet or mechanical linkage) advances wheel by one position. Carry lever trips when wheel passes 9, advancing next wheel. Used in: tabulating machines, odometers, revolution counters, frequency counters.
- **Veeder-Root counter**: Sealed counter mechanism with numbered drums visible through a window. Direct mechanical input via shaft. Counts up to 999,999 or more. Industrial standard for production counting.

**[Keyboard-driven calculators](../glossary/keyboard-driven-calculators.html)** (late mechanical era, 1900-1960):
- **[Full-keyboard machines](../glossary/full-keyboard-machines.html)** (Friden, Marchant): Ten-key rows (0-9) for each digit position. Press keys to set the number, pull lever to engage. Automatic multiplication: set multiplier on keyboard, pull multiply lever, machine iterates through digits automatically, shifting carriage between digit positions. Division similarly automated. Speed: multiplication of two 10-digit numbers in 5-10 seconds.
- **[Ten-key machines](../glossary/ten-key-machines.html)** (later design): Compact, resembling modern calculator layout. Enter digits sequentially, machine positions them internally. Electric motor drive replaces hand crank (1940s onward). These machines dominated business computation until electronic calculators displaced them in the 1970s.

### Mechanical Analog Computing

**[Differential analyzer](../glossary/differential-analyzer.html)** (Bush-type, 1930s):
- **Purpose**: Solve ordinary differential equations numerically by mechanical integration. The first general-purpose analog computer.
- **Components**: Multiple mechanical integrators (ball-and-disk type) interconnected by shafts and gear trains. Each integrator solves one variable. Input shafts represent known quantities; output shafts represent computed quantities. Addition performed by differential gear (summing two shaft rotations). Multiplication by a constant via gear ratio.
- **Setup**: To solve dy/dx = f(x, y), connect integrators and adders with shafts to represent the mathematical relationships. The machine runs continuously, and the output shaft rotation traces the solution y(x) on a pen plotter.
- **Accuracy**: 0.1-1% of full scale, limited by friction, backlash, and torsion in the shafts. The accuracy is sufficient for engineering problems (structural analysis, ballistics, power network transients) where 2-3 significant figures are adequate.
- **Scale**: The MIT Differential Analyzer (1931) had 6 integrators and solved 6th-order equations. Later versions at MIT and elsewhere had up to 18 integrators. Setup time: hours to days to reconfigure interconnections for a new equation.

**Fire control computers**:
- **Problem**: Compute gun elevation and azimuth to hit a moving target from a moving platform (ship), accounting for wind, range, projectile ballistic characteristics, and ship motion.
- **Mechanism**: Arrays of cams, differentials, multipliers, and integrators, all connected by shafts. Input dials set target range, bearing rate, wind speed, and ship speed. Cams generate ballistic correction functions. Differentials sum corrections. Output shafts drive the gun aiming mechanism directly. The computer solves the fire control problem in real time, continuously, as inputs change.
- **Accuracy**: Sufficient for naval engagements at ranges of 10-30 km. The US Navy Mark 1 Fire Control Computer contained ~3,000 precision parts and weighed ~1,360 kg.

### Printing and Recording

**Mechanical counters with printout**:
- **Adding machine with tape**: Keyboard input, full add/subtract, running total printed on paper tape. Each entry stamped sequentially. The printed tape provides an audit trail for accounting. Mechanism: type bars strike inked ribbon against paper tape, driven by the same key press that operates the counter.
- **Strip chart recorder**: Pen on paper strip driven at constant speed by clockwork or synchronous motor. Pen deflection proportional to measured variable (temperature via bimetallic strip, pressure via Bourdon tube, voltage via galvanometer). Records continuous variation over time. Essential for process monitoring, weather recording, and scientific observation.

### Materials and Manufacturing

**Precision requirements for mechanical calculation**:
- **Gear cutting**: Involute tooth profile generated by hobbing (rotating cutter synchronized with gear blank rotation) or milling with formed cutter. Module (tooth size) = pitch diameter / number of teeth. Typical calculator gears: module 0.5-1.0 mm, 20-60 teeth. Tooth spacing tolerance: ±0.01 mm. Backlash (play between meshing gears): <0.02 mm for carry mechanism reliability.
- **Lathe requirements**: Precision lathe with lead screw accuracy ±0.01 mm per 300 mm length. Graded fits: shaft turned to within ±0.005 mm of nominal diameter for press-fit bearing seats. Surface finish: <1.6 μm Ra for bearing surfaces.
- **Materials**: Brass (easy to machine, self-lubricating, corrosion resistant) for gear wheels and digit drums. Hardened steel (case-hardened or through-hardened) for carry levers, ratchets, and detent springs. Phosphor bronze for bearings. Nickel silver for shafts. Each calculator uses 5-15 different alloys.

**Tolerancing and adjustment**:
- Every mechanical calculator requires hand adjustment after assembly. The carry mechanism is the most sensitive: carry levers must engage reliably at every digit transition from 9 to 0, but must NOT falsely trigger at other transitions. Adjust by bending carry lever arms, filing detent profiles, and shimming bearing positions. A skilled adjuster spends 10-40 hours per machine on final calibration.
- Wear compensation: All moving parts wear during use. Digit wheels and carry levers are designed with adjustable pivot points or replaceable wear strips. Machines require periodic cleaning and re-lubrication (every 3-12 months depending on use intensity). Bearing oil: light machine oil (viscosity 10-30 cSt at 40°C).

### Historical Context

The development of mechanical calculation follows a clear progression of increasing complexity and manufacturing capability:

1. **[Abacus and counting board](../glossary/abacus-and-counting-board.html)** (ancient to present): Requires zero manufacturing infrastructure. Wood, beads, and cord. Remains competitive for certain calculations well into the electronic age.
2. **[Napier's bones and sector](../glossary/napiers-bones-and-sector.html)** (~1600): Requires only basic woodworking or metalworking. Individual rods can be made by hand with simple tools.
3. **[Gear-based adders](../glossary/gear-based-adders.html)** (~1640-1820): Requires precision brass casting and gear cutting. Pascal and Leibniz machines demanded manufacturing tolerances unavailable in their era, which limited production.
4. **[Difference Engine](../glossary/difference-engine.html)** (~1820-1850): Requires machine tools capable of ±0.025 mm tolerances on thousands of parts. Babbage's engine was not completed in his lifetime partly because manufacturing technology had not yet caught up with his designs.
5. **[Mass-produced mechanical calculators](../glossary/mass-produced-mechanical-calculators.html)** (~1880-1970): Enabled by precision machine tools, interchangeable parts, and specialized factory production. The Arithmometer (1820, Thomas de Colmar) was the first commercially successful calculator; the Comptometer (1887, Felt) and later Friden and Marchant machines dominated business computing for decades.

**Bootstrap path for mechanical calculation**: In a civilization rebuilding scenario, the progression would be similar but compressed. The abacus requires nothing. Nomograms and slide rules require only printing and basic drafting. Gear-based adders require a working machine shop (lathe, milling machine, precision measuring instruments). The Difference Engine and Analytical Engine require advanced machine tools capable of interchangeable parts at ±0.025 mm tolerance. Each level of manufacturing capability enables a corresponding level of mechanical calculation, and each level of calculation accelerates engineering and scientific work needed for the next manufacturing level.

**Key skills for mechanical calculator construction**:
- **Instrument making**: Precision marking, filing, and fitting to ±0.01 mm. Hand scraping of bearing surfaces. Heat treatment of springs and wear surfaces. These skills are best learned through apprenticeship with an experienced instrument maker.
- **Gear cutting**: Generating correct involute tooth profiles requires either a dividing head and formed cutter (for small quantities) or a hobbing machine (for production). Gear tooth measurement with vernier calipers or gear tooth micrometers.
- **Assembly and adjustment**: The carry mechanism of any mechanical calculator is the most demanding subassembly. Each carry lever must be individually fitted and adjusted. This is not mass-production work; each machine is individually tuned by a skilled mechanic.

### Gear Manufacturing for Calculators

The precision required for mechanical calculator gears exceeds typical machine shop work. Each gear must maintain consistent tooth spacing and involute profile to prevent jamming and calculation errors:

- **Involute profile**: Calculator gears use involute tooth profiles (the same geometry as modern machinery gears) for smooth, constant-velocity-ratio power transmission. Generate the profile using a gear hobbing machine (a hobbing cutter shaped like a worm gear, rotating in synchronized mesh with the blank) or a gear shaper (a cutting tool that reciprocates axially while the blank rotates incrementally).
- **Tooth spacing accuracy**: ±0.01 mm on pitch circle for acceptable calculator operation. A single tooth with excessive spacing causes the carry mechanism to misfire. The dividing head or indexing mechanism on the hobbing machine must be accurate to ±1 arc-minute over a full revolution.
- **Materials**: Brass (easy to machine, self-lubricating, corrosion-resistant) for most calculator gears. Hardened steel for high-wear components (carry levers, stepped drums). Phosphor bronze for bearings. Nickel plating on brass gears prevents tarnish and reduces friction.
- **Finishing**: After hobbing, deburr all tooth edges with a fine file or abrasive wheel. Lap mating gear pairs together with fine abrasive compound to seat the tooth surfaces. Test by rotating through the full engagement cycle: any tight spots indicate a high tooth that needs further lapping.

### Number Representation in Mechanical Systems

Mechanical calculators represent numbers through physical position:

- **Rotary decimal (most common)**: Each digit is a wheel with 10 positions (0-9), readable through a window. Multiple wheels on a common shaft represent multi-digit numbers. Addition rotates wheels forward; subtraction rotates backward. Carry mechanisms propagate between adjacent digit wheels. Used in Pascaline, Arithmometer, and most desktop calculators.
- **Linear pinboard**: Napier's bones and Genaille-Lucas rulers use linear positioning of numbered rods. The operator arranges rods to form the multiplicand and reads partial products by scanning across rows. No carry mechanism needed; the operator performs the carries mentally when summing partial products.
- **Stepped drum position**: In the Leibniz wheel, each digit position has a drum with teeth of length 1 through 9. A sliding gear engages a selectable number of teeth. The axial position of the sliding gear determines how many units are added per drum revolution. This converts a linear input (lever position) to a rotary addition step, enabling direct multiplication through repeated addition.
- **Pinion count**: Difference engines and the Analytical Engine represent numbers as the angular position of toothed wheels with 10 or more teeth. Each wheel has 31-50 teeth (supporting 31-50 digit precision). The angular displacement of a wheel from its zero position encodes the digit value. Addition is performed by physically rotating one wheel by an amount proportional to the value on another wheel, using a gear train that ensures the correct angular increment.

### Speed and Capability Comparison

| Device | Addition speed | Multiplication speed | Precision | Year introduced |
|--------|---------------|---------------------|-----------|-----------------|
| Abacus (soroban) | 10-20 ops/sec | N/A (mental alg.) | Unlimited digits | Ancient |
| Slide rule (25 cm) | Instant | 5-10 sec | 3 sig figs | ~1630 |
| Pascaline | 1-2 sec/add | 30-60 sec (repeated add) | 8 digits | 1642 |
| Arithmometer | 1-2 sec/add | 15-20 sec | 12-16 digits | ~1820 |
| Difference Engine | Automatic | N/A (tabulates polynomials) | 31 digits | 1855 (Scheutz) |
| Friden calculator | 0.5 sec/add | 5-10 sec (auto) | 10-12 digits | ~1940 |

### Detailed Device Specifications

**Soroban operating detail**:
- **Configuration**: 13+ rods standard (21 rods for advanced work). One upper bead (value 5) and four lower beads (value 1 each) per rod, separated by a horizontal reckoning bar. Frame dimensions: roughly 30 × 6 cm for a 13-rod unit, beechwood or bamboo.
- **Addition technique**: Set first addend on the beads. Process the second addend digit by digit, left to right (most significant digit first, opposite to pencil-and-paper right-to-left). For each digit, add the value using a combination of upper and lower bead movements. Example: adding 7 to a rod showing 4: move up one upper bead (+5) and two lower beads (+2), net +7. If the rod exceeds 9, clear it and carry 1 left. Trained operators sustain 10-20 additions per minute on multi-digit numbers.
- **Subtraction**: Reverse of addition. Remove bead values digit by digit. If insufficient beads remain, borrow from the next left rod. Speed matches addition for practiced users.
- **Division**: Performed by repeated subtraction or via a memorized division table (similar to multiplication tables but for quotients). Considerably slower than multiplication, roughly 3-5 operations per minute for multi-digit work.

**Napier's bones lattice multiplication**:
- **Rod detail**: Each of the ten rods (digits 0-9) is divided into 9 cells. Each cell shows the product of the rod's digit × the row number (1-9), with tens digit above a diagonal slash and units digit below. Rod 7, row 8: cell reads "5/6" (56, with 5 above and 6 below the diagonal).
- **Lattice method for multi-digit multiplication**: To multiply 467 × 38, arrange rods 4, 6, 7 side by side. For the 8 row: read 3/2, 4/8, 5/6 across the three rods. Sum each diagonal column right to left with carries: 6, 2+8+5=15 (write 5, carry 1), 3+4+1=8, 3 = 3736. Repeat for the 3 row (rod arrangement ×3 = 1401), shifted one position left. Sum the partial products: 3736 + 14010 = 17746.

**Slide rule scale reference**:
- **C and D scales**: Identical single-cycle logarithmic scales (1 to 10). Primary multiplication/division scales. To multiply a × b, align C-1 with D-a, read D at C-b.
- **CI scale**: Reciprocal of C scale, reading right to left. Multiplying on CI is equivalent to dividing on C. Allows chain calculations without cursor repositioning. To compute 1/a, read CI opposite D-a.
- **A and B scales**: Two-cycle logarithmic scales (1-10-100). A is the square of D at any position. To square a number, set cursor at a on D, read a² on A. Square root: cursor on A, read root on D.
- **K scale**: Three-cycle logarithmic scale (1-10-100-1000). Cube and cube root analogously to A/B for squares.
- **L scale**: Linear scale 0 to 1. Reads log₁₀ directly. Set cursor at n on D, read log₁₀(n) on L. Reverse for antilogarithm.
- **S, T, ST scales**: Sine (S, range 5.7° to 90°), tangent (T, range 5.7° to 45°), and small-angle combined (ST, range 0.57° to 5.7°, where sin θ ≈ tan θ ≈ θ in radians). Used with D scale. Set cursor at angle on S, read sine on D.
- **Accuracy limits**: A 25 cm rule resolves about 3 significant figures. Reading error comes from visual interpolation between graduations, which at 1 mm spacing on the C scale corresponds to roughly 0.2-0.5% of reading. A 50 cm rule improves to 4 figures. Circular slide rules (effective scale length 50-125 cm) achieve 4-5 figures.

**Pascaline carry mechanism detail**:
- **Weighted pawl carry**: Each digit wheel carries a small weighted pawl (gravity-assisted catch). As the wheel rotates from 9 toward 0, the pawl reaches a protruding peg on its wheel. The pawl's weight carries it over the peg during normal rotation, but at the 9-to-0 transition the pawl drops into a slot on the adjacent (next-higher) wheel's carry lever, pulling it forward by one position. This is the carry.
- **Simultaneous carry problem**: Multi-digit carries (e.g., 999 + 1) must propagate through all digits. The Pascaline uses a staggered pawl arrangement where each carry lever is slightly offset, so carries ripple leftward in sequence rather than all at once. This prevents mechanical binding from simultaneous forces.
- **Input**: The operator uses a stylus to rotate each digit wheel to the desired number, visible through a display window. The stylus fits into radial slots on the wheel face. Addition: rotate all input digits forward. Subtraction: the Pascaline uses a complement display (two number rows per wheel, one for addition, one for subtraction, viewed through a sliding bar).

**Leibniz stepped drum detail**:
- **Drum geometry**: A brass cylinder approximately 40 mm diameter × 50 mm long, with 9 longitudinal ribs (teeth) of increasing axial extent. The first rib has a tooth length of 1 unit, the second 2 units, up to the ninth rib at 9 units. A 10th position (no teeth) represents zero.
- **Sliding gear engagement**: A small gear wheel rides on a keyed shaft alongside the drum. The operator positions this gear by moving a slider lever (labeled 0-9). At position 3, the gear engages only the first 3 units of tooth length. When the drum makes one full revolution, the gear turns by exactly 3 teeth worth, adding 3 to the accumulator digit.
- **Multiplication procedure**: To multiply 456 × 78, set the input sliders to 4-5-6. Turn the crank 8 times (units digit of multiplier). The carriage shifts one position left. Turn the crank 7 times (tens digit). The accumulator now reads 35,568. Total time: ~15 seconds for an experienced operator.
- **Division as repeated subtraction**: Set dividend in accumulator, divisor on input sliders. Repeatedly subtract until the accumulator goes negative (detected by a bell), then add back once and record the count as one quotient digit. Shift carriage right. Repeat for each quotient digit. Slower than multiplication, roughly 30-60 seconds per digit.

**Difference Engine construction details**:
- **[Babbage's Design No. 2](../glossary/babbages-design-no-2.html)** (1847-1849, never built in his lifetime): 7th-order polynomial evaluator with 31-digit numbers. Estimated 25,000 parts, total weight approximately 15 tons. The Science Museum London built it from Babbage's plans in 1991: it works perfectly, vindicating his design after 150 years.
- **Finite difference method example**: To tabulate x² for x = 1, 2, 3..., start with value=1, first difference=3 (2²-1²), second difference=2 (constant for quadratics). Each step: add 2nd diff to 1st diff (3→5→7...), then add 1st diff to value (1→4→9...). Only additions required, no multiplication. Higher-order polynomials need more difference columns but the principle is identical.
- **Carry propagation**: The most demanding mechanical problem. Babbage's solution uses a vertical stack of 31 digit wheels per column. Each wheel has a projecting tooth that, on passing 9→0, lifts a spring-loaded lever that advances the wheel above by one position. Carries propagate upward (ones to tens to hundreds) during a single crank rotation. The timing must allow each carry to complete before the next triggers.

**Ball-and-disk integrator operating parameters**:
- **Tilt angle range**: The input ball carriage travels radially across the disk from center to rim. At center (tilt angle 0°), output is zero. At the rim (maximum tilt, roughly 15° offset from center to edge), output equals full disk rotation rate. The ball position encodes a continuous variable from 0 to 1 (normalized).
- **Multiplication of two variables**: Feed variable A as ball position, variable B as disk rotation rate. The output roller rotation equals the integral of A × B over time. By holding B constant for a fixed interval, the output equals A × B × Δt.
- **Fire control application**: US Navy Mark 1 through Mark 9 fire control computers used arrays of ball-and-disk integrators. Inputs: target bearing rate, range rate, wind speed, ship velocity components, projectile ballistic data (stored as cam profiles). Each integrator computed one term of the fire control equations. Output shafts drove gun elevation and train indicators directly. The Mark 1 contained about 3,000 precision parts and weighed 1,360 kg.

**Cam function generation detail**:
- **2D cam (single-input function)**: For y = f(x), the cam rotates proportional to x. A follower rides the cam profile, its displacement proportional to y. The cam profile is machined to produce the desired displacement at each angular position. A sine-function cam is simply a circle mounted eccentrically (off-center). A logarithmic cam requires a specially computed profile.
- **3D cam (two-input function)**: A cylindrical cam with a groove or surface that varies in depth along its length (input 1: rotation) and along its axis (input 2: linear shift). A follower riding the groove outputs f(x, y). Used in fire control to compute range corrections as a function of both target range and wind speed.
- **Manufacturing**: Cut cam profiles on a milling machine using a dividing head for angular positioning. For each angular position, set the cutter to the computed radial depth. Finish with filing and lapping. Hardened steel (Rockwell C 55-60) for wear resistance. The profile must be accurate to ±0.01 mm to achieve ±0.1% function accuracy.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Computing](./index.md) • [All Domains](../index.md)*

