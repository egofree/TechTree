# Core Mathematics

> **Node ID**: mathematics.core-mathematics
> **Domain**: [Mathematics & Formal Sciences](./index.md)
> **Dependencies**: `foundations`, `knowledge.writing`
> **Timeline**: Years 0-25
> **Outputs**: arithmetic, algebra, geometry, trigonometry, number_systems

## Problem

Every engineering discipline — from surveying a road to calculating stress in a beam to designing a feedback controller — rests on mathematical foundations. Without a systematic number system, engineers cannot specify dimensions. Without algebra, they cannot solve for unknown quantities. Without geometry and trigonometry, they cannot lay out structures or navigate. Core mathematics provides the shared language of quantitative reasoning that all subsequent technical work requires. This capability covers the mathematical tools that become available from the earliest counting through to the trigonometry and algebra needed for industrial-age engineering.

## Number Systems & Arithmetic

### Positional Notation

The foundation of all calculation. A positional number system uses a fixed base (radix) and assigns digit values based on position. In base-10 (decimal), the number 3,742 means 3×10³ + 7×10² + 4×10¹ + 2×10⁰. This invention — deceptively simple — enables:

- **Compact representation** of arbitrarily large numbers (Roman numerals require new symbols for each magnitude)
- **Algorithmic computation**: addition, subtraction, multiplication, and division follow mechanical procedures that work identically regardless of magnitude
- **Fractions via decimal extension**: 3.14159… = 3 + 1/10 + 4/100 + 1/1000 + 5/10000 + 9/100000

The Hindu-Arabic numeral system (digits 0-9 with positional notation and zero) is the single most important mathematical technology for bootstrap engineering. Without it, multiplication and division require reference tables or abacus; with it, any literate person can perform four-function arithmetic by following rules.

**Engineering application**: All measurement, costing, inventory, and dimensional specification in the bootstrap sequence relies on positional arithmetic. A furnace design specifying "firebrick chamber 120 cm × 80 cm × 60 cm" is meaningless without a number system that can represent and manipulate these quantities.

### Zero

Zero serves two independent functions: as a placeholder in positional notation (the difference between 101 and 11) and as a number in its own right (the additive identity: a + 0 = a). The placeholder function is essential for positional arithmetic to work — without zero, representing 1001 requires either a gap or a special symbol. The identity function simplifies algebraic manipulation and enables the coordinate systems used in engineering.

### Four-Function Arithmetic

**Addition** (a + b) and **subtraction** (a − b): combine or difference quantities. Fundamental to all accounting, inventory, and measurement.

**Multiplication** (a × b): repeated addition. Essential for area (length × width), volume, force (mass × acceleration), and cost calculation (quantity × unit price). The standard algorithm multiplies each digit pair and handles carries.

**Division** (a ÷ b): inverse of multiplication. Splits a quantity into equal parts or computes ratios. Essential for rates (speed = distance ÷ time), unit costs, and proportions (gear ratio = driver teeth ÷ driven teeth).

**Engineering application**: A foundry casting 15 ingots per batch, consuming 2.3 kg of copper per ingot, needs 15 × 2.3 = 34.5 kg of copper. If the mine produces 120 kg per week, the foundry can run 120 ÷ 34.5 ≈ 3.5 batches per week. Every resource allocation decision in the bootstrap chain requires this level of arithmetic.

### Fractions, Decimals, and Ratios

**Fractions** (a/b): represent parts of a whole. Operations follow rules: addition requires common denominators (1/3 + 1/4 = 4/12 + 3/12 = 7/12), multiplication is straightforward (2/3 × 3/5 = 6/15 = 2/5), division inverts and multiplies.

**Decimal fractions**: extend positional notation to the right of the decimal point. Easier for computation than common fractions because the same algorithms work as for integers. All engineering measurement naturally produces decimal values.

**Ratios and proportions**: a:b = c:d implies a×d = b×c. Used constantly in engineering: scale drawings (1:100), gear ratios (3:1 speed reduction), material mixtures (1 part cement : 2 parts sand : 3 parts gravel), and chemical stoichiometry (2H₂ + O₂ → 2H₂O, a 2:1 molar ratio).

**Engineering application**: Concrete mix design specifies water:cement ratio of 0.5 by weight. For 50 kg of cement, add 25 kg of water. Mortar uses a 1:3 cement:sand ratio — for 10 kg of cement, add 30 kg of sand.

### Orders of Magnitude & Estimation

Engineers must estimate before calculating precisely. An order-of-magnitude estimate identifies whether a result should be measured in grams, kilograms, or tonnes — catching gross errors before they become catastrophic.

**Technique**: Round all inputs to one significant figure, compute mentally, express result as a power of 10. Example: 347 × 23 ≈ 300 × 20 = 6,000 ≈ 10⁴. Exact answer: 7,981. The estimate confirms the exact result should be four digits, not three or five.

**Engineering application**: Estimating whether a beam will support a load before performing detailed stress analysis. Estimating material requirements (will a 1-tonne ore shipment yield enough copper for 200 ingots?) before committing resources.

## Algebra

### Variables and Equations

Algebra generalizes arithmetic by replacing specific numbers with symbols (variables). An equation states that two expressions are equal: 2x + 3 = 11. Solving means finding the value(s) of x that make the statement true.

**Linear equations** (ax + b = c): the simplest case, solvable by isolating x. Example: a furnace consumes 3 kg of charcoal per hour plus 5 kg for startup. If you have 50 kg, how many hours can it run? 3h + 5 = 50, so h = 15 hours.

**Simultaneous equations** (two or more equations with two or more unknowns): represent systems with multiple constraints. Example: a gear train has two shafts. Shaft A turns at 200 RPM. The gear ratio between A and B is 3:2. What speed does shaft B turn? Direct ratio: B = 200 × 2/3 = 133 RPM.

### Quadratic Equations

Equations of the form ax² + bx + c = 0. Solved by the quadratic formula: x = (−b ± √(b² − 4ac)) / (2a). Two solutions (or one repeated, or none real).

**Engineering application**: Projectile trajectory (ballistic arcs for mining explosives), lens focal length calculations, resonant frequency of LC circuits (f = 1/(2π√(LC))), and structural beam deflection curves all produce quadratic or reducible-to-quadratic equations.

### Polynomials and Factoring

Polynomials (axⁿ + bxⁿ⁻¹ + … + k) model many physical relationships. Factoring simplifies them: x² − 5x + 6 = (x − 2)(x − 3). Used for finding roots (where the function equals zero — critical points, equilibrium positions, resonant frequencies).

### Exponents and Logarithms

**Exponents**: aⁿ = a × a × … × a (n times). Rules: aⁿ × aᵐ = aⁿ⁺ᵐ, (aⁿ)ᵐ = aⁿᵐ, a⁰ = 1, a⁻ⁿ = 1/aⁿ.

**Logarithms**: the inverse of exponentiation. If aⁿ = x, then log_a(x) = n. Common log (base 10) and natural log (base e ≈ 2.718) are most used. Key rules: log(ab) = log(a) + log(b), log(a/b) = log(a) − log(b), log(aⁿ) = n × log(a).

**Engineering application**: Logarithms convert multiplication into addition — the operating principle of slide rules and logarithmic calculation. The decibel scale (dB = 20 log₁₀(V/V₀)) measures signal ratios. pH (−log₁₀[H⁺]) measures acidity. The Richter scale (logarithmic) measures earthquake intensity.

### Functions and Graphs

A function f(x) maps each input to exactly one output. Graphing functions on a coordinate plane reveals behavior: linear functions (straight lines), quadratic functions (parabolas), exponential functions (rapid growth/decay), logarithmic functions (rapid then leveling).

**Engineering application**: Stress-strain curves, voltage-current characteristics of components, cooling curves (temperature vs. time), production rate vs. input quantity — all are functions. Reading and interpreting graphs is essential for every engineering discipline.

## Geometry

### Euclidean Geometry

The mathematics of shapes, angles, distances, and areas in flat (2D) and solid (3D) space. Based on Euclid's axioms, which remain valid for all terrestrial-scale engineering.

**Key constructions with straightedge and compass**: perpendicular bisector, angle bisector, parallel line through a point, equilateral triangle. These constructions directly correspond to workshop layout operations.

### Areas and Volumes

**2D shapes**:
- Rectangle: A = length × width
- Triangle: A = ½ × base × height
- Circle: A = π × radius² (π ≈ 3.14159)
- Trapezoid: A = ½ × (a + b) × height

**3D solids**:
- Rectangular prism: V = l × w × h
- Cylinder: V = π × r² × h
- Sphere: V = (4/3) × π × r³
- Cone: V = (1/3) × π × r² × h

**Engineering application**: Calculate the volume of a crucible (cylinder) to determine how much metal it can hold. A cylindrical crucible with radius 8 cm and height 15 cm holds π × 8² × 15 ≈ 3,016 cm³ ≈ 3.0 liters. Copper density 8.96 g/cm³ → this holds about 27 kg of molten copper.

### Angles and Triangles

**Angle measurement**: degrees (full circle = 360°) or radians (full circle = 2π). Degrees are intuitive for construction; radians are natural for calculus.

**Triangle properties**: Sum of angles = 180°. Pythagorean theorem: a² + b² = c² (right triangles). This single relationship underpins all surveying, navigation, and construction layout.

**Engineering application**: A ramp rises 1.5 m over a horizontal distance of 8 m. The ramp length = √(1.5² + 8²) = √(2.25 + 64) = √66.25 ≈ 8.14 m. The angle = arctan(1.5/8) ≈ 10.6°.

### Coordinate Geometry

The Cartesian coordinate system (x, y) maps geometry to algebra. Every point is a number pair; every line is an equation (y = mx + b, where m is slope, b is y-intercept); every circle is (x−h)² + (y−k)² = r².

**Distance formula**: d = √((x₂−x₁)² + (y₂−y₁)²) — derived from Pythagorean theorem.

**Slope**: m = (y₂−y₁)/(x₂−x₁) — the rate of change, directly analogous to physical quantities like speed (distance/time), stress (force/area), and thermal gradient (temperature/distance).

**Engineering application**: CNC toolpath programming, surveying (mapping terrain coordinates), and any situation where geometry must be computed numerically rather than constructed physically.

## Trigonometry

### Right Triangle Trigonometry

For a right triangle with angle θ:
- **Sine**: sin(θ) = opposite / hypotenuse
- **Cosine**: cos(θ) = adjacent / hypotenuse
- **Tangent**: tan(θ) = opposite / adjacent = sin(θ) / cos(θ)

These ratios are constant for a given angle, regardless of triangle size. This means measuring one side and one angle determines all other sides.

**Pythagorean identity**: sin²(θ) + cos²(θ) = 1. Always true.

**Engineering application**: A mine shaft descends at 30° from horizontal. After 100 m along the shaft, the vertical depth = 100 × sin(30°) = 50 m, and horizontal distance = 100 × cos(30°) ≈ 86.6 m. Surveying a road around a hill: measure angles and distances, compute coordinates with trigonometry.

### General Triangles (Law of Sines and Cosines)

Not every triangle has a right angle. For any triangle:

**Law of Sines**: a/sin(A) = b/sin(B) = c/sin(C). Use when you know an angle and its opposite side plus one other angle or side.

**Law of Cosines**: c² = a² + b² − 2ab×cos(C). Use when you know two sides and the included angle, or all three sides.

**Engineering application**: Triangulation for land survey. Measure a baseline distance between two points, then angles from each endpoint to a target. The Law of Sines gives the distance to the target. This is how all pre-GPS surveying works.

### Trigonometric Identities

Key identities for simplifying engineering calculations:
- **Double angle**: sin(2θ) = 2sin(θ)cos(θ), cos(2θ) = cos²(θ) − sin²(θ)
- **Sum/difference**: sin(A±B) = sin(A)cos(B) ± cos(A)sin(B)
- **Product-to-sum**: sin(A)sin(B) = ½[cos(A−B) − cos(A+B)]

**Engineering application**: Alternating current analysis uses sinusoidal functions extensively. AC voltage: V(t) = V₀ sin(ωt + φ), where ω is angular frequency and φ is phase. Combining two AC signals requires angle addition formulas.

### Inverse Trigonometric Functions

arcsin, arccos, arctan: given a ratio, find the angle. Essential for converting measured ratios (e.g., slope = rise/run) back to angles for specification.

**Engineering application**: Measure the shadow of a 10 m pole as 6 m. Sun angle = arctan(10/6) ≈ 59°. This technique determines solar elevation for passive solar building design.

## Units, Dimensions, and Dimensional Analysis

### Unit Systems

Consistent units are essential. The metric system (SI) uses: meter (length), kilogram (mass), second (time), ampere (current), kelvin (temperature), mole (amount), candela (luminous intensity). Derived units: newton (force = kg⋅m/s²), joule (energy = N⋅m), watt (power = J/s), pascal (pressure = N/m²), volt (electric potential = W/A), ohm (resistance = V/A).

### Dimensional Analysis

Every physical quantity has dimensions (length L, mass M, time T, etc.). Equations must be dimensionally consistent — you cannot add meters to kilograms.

**Technique**: Check that both sides of an equation have the same dimensions. Example: kinetic energy E = ½mv² has dimensions [M][L/T]² = [M⋅L²/T²]. Work W = F⋅d has dimensions [M⋅L/T²][L] = [M⋅L²/T²]. They match — the equation is dimensionally valid.

**Engineering application**: Catch errors in formulas. If a calculation for pipe flow rate produces a result in m² (area) instead of m³/s (volume flow rate), something is wrong. Dimensional analysis catches this before the pipe is built.

### Unit Conversion

Convert between systems: 1 inch = 25.4 mm, 1 pound = 0.4536 kg, 1 psi = 6,895 Pa. Always multiply by conversion factors arranged so unwanted units cancel:

```
100 psi × (6,895 Pa / 1 psi) = 689,500 Pa = 689.5 kPa
```

**Engineering application**: Import specifications in different unit systems, verify material properties against reference data in different units, convert between measurement systems.

## Mathematical Reasoning & Proof

### Inductive and Deductive Reasoning

**Inductive**: Observe patterns, generalize. "Every iron sample I've tested conducts electricity → iron conducts electricity." Useful for forming hypotheses but not conclusive.

**Deductive**: Apply general rules to specific cases. "All metals conduct electricity. Iron is a metal. Therefore iron conducts electricity." Conclusive when premises are true.

**Engineering application**: Material testing uses inductive reasoning (sample testing → material properties). Design uses deductive reasoning (known properties + physics → predicted behavior).

### Proportionality and Scaling

Many physical relationships are proportional:
- Force ∝ mass × acceleration (F = ma)
- Heat flow ∝ temperature difference × area (Q̇ ∝ ΔT × A)
- Electrical resistance ∝ length / area (R = ρL/A)

Recognizing proportionality lets engineers scale designs: if a 10 cm beam deflects 1 mm under 100 kg, a 20 cm beam of the same material and cross-section deflects 8 mm under the same load (deflection scales as length³ for a simply supported beam).

**Engineering application**: Scale up a bench-scale chemical reaction to production volumes. If a 1-liter reactor produces 500 g of product in 2 hours, a 100-liter reactor (geometrically similar) does NOT simply produce 50 kg in 2 hours — heat transfer, mixing, and reaction kinetics scale differently. Understanding scaling laws prevents expensive failures.

## Practical Computation Methods

### Manual Calculation Techniques

**Lattice multiplication**: Visual grid method for multi-digit multiplication — easier to learn than the standard algorithm.

**Casting out nines**: Quick check for arithmetic errors. Sum the digits of each operand, perform the operation on the digit sums modulo 9, compare with the digit sum of the result. If they disagree, there's an error.

**Significant figures**: The precision of a result cannot exceed the precision of the least precise input. 3.14 × 2.0 = 6.3 (two significant figures, not 6.28). Engineers must track significant figures to avoid false precision.

### Interpolation and Extrapolation

**Linear interpolation**: Given two data points (x₁,y₁) and (x₂,y₂), estimate y at intermediate x: y = y₁ + (x−x₁) × (y₂−y₁)/(x₂−x₁).

**Engineering application**: Thermocouple tables give voltage at discrete temperatures (e.g., 100°C and 150°C). For a measured voltage between tabulated values, linear interpolation estimates the temperature. Material property tables (density vs. temperature, resistivity vs. temperature) are used the same way.

**Extrapolation** (estimating beyond known data) is risky — the trend may not continue. Use only when no alternative exists, and always flag the uncertainty.

## Key Concepts Summary

| Concept | Engineering Application | Bootstrap Relevance |
|---------|------------------------|---------------------|
| Positional arithmetic | All measurement, costing, inventory | Year 0 — counting and trade |
| Algebra | Solving for unknowns in design calculations | Year 5-10 — tool and structure design |
| Geometry | Area, volume, layout, construction | Year 5-10 — building, land measurement |
| Trigonometry | Surveying, navigation, AC circuits | Year 10-25 — roads, mines, power |
| Logarithms | Slide rules, decibels, pH, growth models | Year 10-25 — engineering calculation |
| Dimensional analysis | Error checking, unit conversion | Year 10+ — all quantitative work |
| Scaling laws | Scale-up from lab to production | Year 15+ — process engineering |

## Dependencies

- **Writing system** (`knowledge.writing`): Mathematical notation requires a writing system — symbols for digits, operators, variables, and geometric construction
- **Basic tools** (`foundations`): Measurement requires tools (rulers, compasses, sighting instruments); counting emerges from trade and resource management
- **Enables**: All downstream engineering disciplines, applied mathematics, computing, and formal systems
