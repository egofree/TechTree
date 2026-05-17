# Mechanical Computing & Automation

> **Node ID**: `computing`
> **Domain**: [Mechanical Computing & Automation](./)
> **Dependencies**: `machine-tools`
> **Enables**: `vlsi-scaling.eda-design`
> **Timeline**: Years 10-70+
> **Outputs**: slide_rules, mechanical_calculators, automated_machines, punch_cards, feedback_control

## Problem

Design and process control calculations for semiconductor work are extremely tedious by hand. Electronic computers arrive very late (Photolithography). Mechanical computing bridges the gap, enabling faster iteration and more complex designs.

## Technologies &amp; Systems

### Manual Calculation Aids

**Abacus**:
- **Construction**: Wooden frame with horizontal rods. Beads on each rod — upper beads (heaven beads, value 5 each) and lower beads (earth beads, value 1 each). Standard suanpan: 2 upper + 5 lower beads per rod. Soroban: 1 upper + 4 lower.
- **Operation**: Slide beads toward center bar to add, away to subtract. Each rod = one decimal place. Rightmost rod = ones, next = tens, etc. Carry: when lower beads exceed 4, reset and move one upper bead. When upper bead is used and lower beads exceed 4, reset both and carry 1 to next rod left.
- **Speed**: Trained operators perform addition/subtraction faster than electronic calculator data entry. 10-20 operations per second on sustained calculations. The abacus remains competitive for bulk arithmetic well into the electronic age.

**Slide rule**:
- **Principle**: Two logarithmic scales — sliding one scale relative to the other performs multiplication and division by adding/subtracting logarithms. log(a × b) = log(a) + log(b).
- **Construction**: Three strips of wood, plastic, or bamboo. Outer two fixed, middle strip slides. Cursor (transparent sliding window with hairline) for precise reading. Scale length typically 25 cm (10-inch rule).
- **Scales**: C and D scales (basic multiplication/division, 1-10 range). A and B (squares, 1-100 range). K (cubes). CI (reciprocal). S, T, ST (sine, tangent, small angles). L (linear, for reading log values directly).
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

### Automation &amp; Control

**Cams and followers**:
- **Cam**: Rotating or sliding piece with shaped profile. **Follower**: lever or rod that moves in response to cam profile. Convert continuous rotary motion into complex, pre-programmed linear or oscillating motion.
- **Design**: Plot desired follower displacement vs. cam rotation angle. Transfer to cam blank. Cut profile with dividing head and milling machine. Harden cam surface (case-harden low-carbon steel — heat to 900°C, pack in charcoal, hold, quench).
- **Applications**: Automate machine tool cycles (feed, cut, retract, index), valve timing in engines, printing press coordination, textile machinery patterns. Each cam is a mechanical "program" — one revolution = one complete cycle.

**Linkages**:
- **Four-bar linkage**: Two rotating links (crank and follower), one connecting rod (coupler), and one fixed link (frame). Converts rotary motion to oscillating, or vice versa. Modify link lengths to change motion characteristics.
- **Slider-crank**: Crank + connecting rod + sliding piston. Converts rotary to linear (or vice versa). Used in every piston engine and pump.
- **Pantograph**: Linked parallelogram for scaling drawings. One tracing point follows original, cutting head produces scaled copy. Used for engraving maps, type, and decorative patterns. Ratio adjustable by changing pivot point.
- **Applications**: Convert motion between types (rotary ↔ linear ↔ oscillating), amplify force (lever principle), reproduce patterns at different scales, compute geometric relationships (mechanical analog computing).

**Governors**:
- **Centrifugal governor** (Watt governor): Two heavy balls on hinged arms rotate with engine shaft. As speed increases, centrifugal force swings balls outward → arms move collar downward → linkage reduces steam valve opening → engine slows. As speed decreases, balls fall inward → valve opens wider → engine speeds up. Equilibrium speed set by spring tension or weight adjustment.
- **Performance**: Maintains speed within ±2-5% of setpoint under varying load. Response time: 1-5 seconds. Essential for steam engines, water wheels, and any rotating machinery requiring constant speed.
- **Improved versions**: Porter governor (heavier central load for wider speed range), Proell governor (additional springs for faster response), Hartnell governor (spring-loaded for compact installation).

**Feedback control**:
- **Thermostat**: Bimetallic strip (brass + steel laminated strip — brass expands more than steel when heated, causing strip to bend). At set temperature, bent strip opens electrical contacts → heater off. As temperature drops, strip straightens → contacts close → heater on. Hysteresis: small gap between on and off temperatures (1-3°C). For furnaces, ovens, incubators.
- **Pressure regulator**: Spring-loaded diaphragm or piston. Downstream pressure pushes against spring. If pressure exceeds setpoint → valve closes. If below → valve opens. Maintains constant delivery pressure despite upstream fluctuations. For steam, compressed air, gas distribution.
- **Float valve**: Buoyant float on lever arm operates valve. Water level rises → float rises → valve closes inlet. Level drops → float drops → valve opens. Simple, reliable liquid level control for tanks, boilers, reservoirs.

### Integration with Manufacturing

**Cam-operated turret lathe**:
- **Turret**: Indexable tool holder (6-8 positions). Each position holds a different cutting tool (turning, facing, drilling, boring, threading, parting). Cam drum rotates → trip levers index turret → advance tool → cut → retract → index to next tool. Cycle repeats automatically. One operator can run 3-5 machines simultaneously.
- **Production rate**: 10-50 parts/hour depending on complexity. Each part identical to the last (within machine tolerance). This is the foundation of mass production — interchangeable parts by machine rather than hand fitting.

**Automatic screw machine**:
- Specialized for high-volume production of small turned parts (screws, bolts, shafts, pins). Bar stock fed through collet. Multiple cross-slides and turret tools operate in sequence under cam control. Cycle time: 5-30 seconds per part. Produces thousands of identical parts per day. THE machine that enabled the hardware industry.

**Pattern-following milling** (tracing):
- **Tracer mill**: Stylus follows a master template (wood, plaster, or metal pattern). Hydraulic or electrical linkage drives milling cutter to duplicate pattern in workpiece. Enables production of complex 3D shapes (dies, molds, turbine blades) without direct CNC capability. Accuracy: ±0.05-0.1 mm depending on tracer mechanism.

### Punch Card Systems

**Punch card** (for data and program storage):
- **Card**: Stiff paper card (187 × 83 mm, the "IBM card" or "Hollerith card"). 12 rows × 80 columns. Each column represents one character. Punch holes in specific row positions to encode data (numeric 0-9, or alphanumeric via zone punches in rows 0, 11, 12 combined with digit punches).
- **Card punch**: Keyboard-operated machine that punches holes in card. Operator types data → machine punches corresponding hole pattern.
- **Card reader**: Spring-loaded metal brushes or photoelectric sensors detect presence/absence of holes as card passes through reader. Converts hole pattern to electrical signals.
- **Tabulating machine**: Reads punch cards, counts, sorts, and accumulates data. Electromagnetic counters and relays perform basic arithmetic and logical operations. Herman Hollerith's 1890 census machine was the breakthrough — processed 1890 US census data in months vs. years.
- **Application**: Census data, inventory tracking, payroll, process recipes (encode process parameters on cards → feed into machine that controls cam timing), and later (Photolithography) as program input for early computers.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Machine Tools | Precision gears for calculators; jigs/fixtures for production; slide rules |
| Energy | Governors for steam engines; process control instruments; punch card systems |
| Chemistry | Calculations for chemical processes, distillation column design |
| Silicon | Crystal growth process control, temperature profiling |
| Photolithography | Stepper motor control, process sequencing, mask pattern calculation, early computers |

## Key Deliverables

- Slide rules and mathematical tables for all engineers
- Working mechanical calculator (stepped drum or difference engine)
- Cam-operated automated machine tools (turret lathe, screw machine)
- Process control instrumentation (thermostats, pressure regulators, governors)
- Punch card data processing system
- Nomogram charts for common engineering calculations
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
