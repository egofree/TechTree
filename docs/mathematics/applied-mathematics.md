# Applied Mathematics

> **Node ID**: mathematics.applied-mathematics
> **Domain**: [Mathematics & Formal Sciences](./index.md)
> **Dependencies**: [`mathematics.core-mathematics`](core-mathematics.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 15-70
> **Outputs**: calculus, linear_algebra, differential_equations, probability_theory, statistical_methods, numerical_methods

## Problem

Core mathematics gives engineers algebra and geometry — tools for static, deterministic problems. But the real world is dynamic and uncertain: furnaces heat up over time, chemical reaction rates depend on temperature, manufacturing processes have random variation, and complex systems have dozens of interacting variables. Applied mathematics provides the tools to model continuous change (calculus), handle multi-variable systems (linear algebra), predict dynamic behavior (differential equations), quantify uncertainty (probability and statistics), and compute solutions when analytical methods fail (numerical methods). These capabilities are essential for process engineering, quality control, electronic design, and every discipline that goes beyond simple static analysis.

## Calculus

### The Concept of a Limit

The foundation of calculus. A limit describes the value a function approaches as its input approaches some value. lim(x→a) f(x) = L means f(x) gets arbitrarily close to L as x gets close to a.

**Why it matters for engineering**: Many physical quantities are defined as limits — instantaneous velocity is the limit of average velocity as the time interval approaches zero. The area of a curved shape is the limit of the sum of increasingly thin rectangular strips. Limits make these intuitive ideas mathematically precise.

### Differential Calculus

The derivative f'(x) = lim(h→0) [f(x+h) − f(x)] / h measures the instantaneous rate of change of a function. Geometrically, it is the slope of the tangent line at point x.

**Key rules**:
- **Power rule**: d/dx(xⁿ) = nxⁿ⁻¹
- **Product rule**: d/dx(uv) = u'v + uv'
- **Chain rule**: d/dx(f(g(x))) = f'(g(x)) × g'(x)
- **Exponential**: d/dx(eˣ) = eˣ (unique: function equals its own derivative)
- **Trigonometric**: d/dx(sin(x)) = cos(x), d/dx(cos(x)) = −sin(x)

**Engineering applications**:
- **Velocity and acceleration**: Position s(t) → velocity v(t) = ds/dt → acceleration a(t) = dv/dt = d²s/dt². Essential for mechanics, from machine design to ballistic trajectories.
- **Rate of reaction**: Chemical reaction rate = d[concentration]/dt. Used for reactor design, furnace optimization, and process control.
- **Thermal gradient**: dT/dx describes how temperature changes with position — critical for heat treatment, furnace design, and thermal stress analysis.
- **Electrical circuits**: Current i = dQ/dt (rate of charge flow). Voltage across an inductor: V = L × di/dt. These relationships define circuit behavior.
- **Optimization**: Find the maximum or minimum of a function by setting its derivative to zero. Used for maximizing efficiency, minimizing material usage, finding optimal operating points.

### Integral Calculus

The integral is the inverse of the derivative. If F'(x) = f(x), then ∫f(x)dx = F(x) + C. The definite integral ∫ₐᵇ f(x)dx computes the area under the curve f(x) from x=a to x=b.

**Fundamental theorem of calculus**: ∫ₐᵇ f(x)dx = F(b) − F(a). This connects the derivative (rate of change) with the integral (accumulated quantity).

**Engineering applications**:
- **Area and volume**: Compute the area of irregular shapes, volume of revolution (lathe-turned parts), and surface area of curved surfaces.
- **Work and energy**: W = ∫F·ds (work is the integral of force over distance). Energy stored in a spring: E = ∫kx dx = ½kx².
- **Total charge and energy**: Q = ∫i dt (total charge from current), E = ∫P dt (total energy from power).
- **Mass and heat balance**: Total mass flow through a pipe with varying velocity: ∫ρv(x) dA. Heat absorbed during a temperature change: Q = ∫m·c(T)dT.
- **Average values**: Average of f over [a,b] = (1/(b−a)) ∫ₐᵇ f(x)dx. Average power, average temperature, average flow rate.

### Differential Equations (Overview)

Equations involving derivatives: f(t, y, dy/dt, d²y/dt², …) = 0. These model any system that changes over time. Detailed treatment below, but the calculus connection: solving a differential equation means finding a function whose derivatives satisfy the given relationship.

### Multivariable Calculus

Engineering problems involve multiple variables simultaneously: temperature depends on position (x, y, z) and time (t); stress in a beam depends on the location within the beam.

**Partial derivatives**: ∂f/∂x measures how f changes with x while holding all other variables constant. Essential for understanding how each factor independently affects a system.

**Gradient**: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) — a vector pointing in the direction of steepest increase. Used for optimization algorithms and understanding heat flow (heat flows opposite to the temperature gradient).

**Engineering application**: Temperature distribution in a furnace wall depends on position (x through the wall thickness, y along the wall). The heat flux at any point is proportional to the negative temperature gradient: q = −k∇T. This requires partial derivatives to compute.

## Linear Algebra

### Vectors

A vector represents a quantity with both magnitude and direction: velocity (50 km/h northeast), force (100 N downward), electric field (5 V/m in the x-direction).

**Vector operations**:
- **Addition**: Component-wise. (1,2) + (3,4) = (4,6). Represents combined displacements, forces, velocities.
- **Scalar multiplication**: k(a,b) = (ka, kb). Scaling a force, velocity, or displacement.
- **Dot product**: a·b = a₁b₁ + a₂b₂ + … = |a||b|cos(θ). Gives the projection of one vector onto another. Used for work (W = F·d), angle between vectors, and checking orthogonality (a·b = 0 means perpendicular).
- **Cross product** (3D only): a×b produces a vector perpendicular to both a and b, with magnitude |a||b|sin(θ). Used for torque (τ = r×F) and electromagnetic force (F = qv×B).

### Matrices

A matrix is a rectangular array of numbers. Matrices represent linear transformations, systems of equations, and data tables.

**Matrix operations**:
- **Multiplication**: C = AB where Cᵢⱼ = Σₖ AᵢₖBₖⱼ. Not commutative (AB ≠ BA in general). Represents composition of transformations.
- **Transpose**: Aᵀ has rows and columns swapped. (AB)ᵀ = BᵀAᵀ.
- **Determinant**: det(A) is a scalar that indicates whether a matrix is invertible (det ≠ 0) and measures volume scaling. Used for solving systems and checking singularity.
- **Inverse**: A⁻¹ such that AA⁻¹ = I (identity). Used to solve Ax = b → x = A⁻¹b.

### Systems of Linear Equations

A system of n equations in n unknowns: Ax = b, where A is an n×n matrix, x is the unknown vector, b is the right-hand side. Solve by Gaussian elimination (row reduction) or matrix inversion.

**Engineering application**: Structural analysis of a truss: each joint has force balance equations (ΣFₓ = 0, ΣFᵧ = 0). With 10 joints, there are 20 equations in 20 unknowns (the member forces). Solving this system determines whether the structure is safe.

### Eigenvalues and Eigenvectors

For a matrix A, an eigenvector v satisfies Av = λv, where λ is the eigenvalue. The eigenvector is a direction that the matrix only scales (does not rotate). The eigenvalue is the scaling factor.

**Engineering application**:
- **Vibration analysis**: Natural frequencies of a structure are the square roots of the eigenvalues of the stiffness/mass matrix. If an excitation frequency matches a natural frequency → resonance → catastrophic failure.
- **Stress analysis**: Principal stresses are eigenvalues of the stress tensor. Von Mises stress (yield criterion) is computed from these.
- **Finite element analysis (FEA)**: The entire method reduces to solving a large system Ax = λx for natural modes or Ax = b for static loads.

## Differential Equations

### Ordinary Differential Equations (ODEs)

Equations involving derivatives of a function of one variable. Classified by order (highest derivative) and linearity.

**First-order linear ODE**: dy/dt + p(t)y = g(t). Solved by the integrating factor method. Applications: cooling (Newton's law: dT/dt = −k(T−T_ambient)), RC circuit charging (dV/dt = (V_source − V)/RC), radioactive decay (dN/dt = −λN).

**Second-order linear ODE with constant coefficients**: a(d²y/dt²) + b(dy/dt) + cy = f(t). This single equation type models an enormous range of engineering systems.

**Engineering applications**:
- **Spring-mass-damper**: m(d²x/dt²) + c(dx/dt) + kx = F(t). Models machine vibration, vehicle suspension, and building earthquake response. The characteristic equation mr² + cr + k = 0 determines whether the system is overdamped (no oscillation), critically damped (fastest return without oscillation), or underdamped (oscillatory).
- **RLC circuit**: L(d²q/dt²) + R(dq/dt) + q/C = V(t). Electrically identical to spring-mass-damper: L↔m, R↔c, 1/C↔k. Natural frequency ω₀ = 1/√(LC), damping ratio ζ = R/(2√(L/C)).
- **Heat conduction**: ∂T/∂t = α(∂²T/∂x²) (one-dimensional, this is actually a PDE — see below). Determines how long it takes for a forging to reach uniform temperature, or how fast heat leaks through a furnace wall.

### Partial Differential Equations (PDEs)

Equations involving partial derivatives of functions of multiple variables. Most real engineering problems produce PDEs rather than ODEs.

**Heat equation**: ∂T/∂t = α∇²T. Describes temperature evolution in a solid over time. Used for heat treatment design, furnace optimization, thermal stress prediction.

**Wave equation**: ∂²u/∂t² = c²∇²u. Describes vibration, sound, and electromagnetic wave propagation. Used for acoustic design, structural vibration analysis, and antenna design.

**Laplace's equation**: ∇²φ = 0. Describes steady-state heat flow, electrostatic potential, and fluid flow. Used for furnace design (steady-state temperature distribution) and electric field analysis.

**Engineering application**: Designing a heat treatment cycle for steel requires solving the heat equation to determine how long to hold at temperature for the heat to penetrate to the core of the workpiece. For a cylindrical billet of radius R with thermal diffusivity α, the characteristic time is t ≈ R²/(4α). A 5 cm radius steel billet (α ≈ 12 mm²/s) needs about 5²/(4×0.012) ≈ 520 seconds ≈ 9 minutes for thermal equilibration.

### Laplace Transforms

A technique for converting differential equations into algebraic equations. L{f(t)} = F(s) = ∫₀^∞ f(t)e⁻ˢᵗ dt. Transforms derivatives into multiplications by s: L{df/dt} = sF(s) − f(0).

**Engineering application**: Control system design. A PID controller's transfer function is Kp + Ki/s + Kd×s. The Laplace transform converts the differential equation of the plant + controller into an algebraic equation that can be analyzed for stability (poles in the left half s-plane = stable).

## Probability & Statistics

### Descriptive Statistics

**Measures of central tendency**: Mean (average: μ = Σxᵢ/n), median (middle value), mode (most frequent). For manufacturing, the mean gives the typical dimension; the median is robust against outliers.

**Measures of spread**: Standard deviation (σ = √(Σ(xᵢ−μ)²/n)), variance (σ²), range (max − min). Standard deviation quantifies process variability — the key metric for quality control.

**Engineering application**: A production line turns out steel rods with diameter μ = 10.00 mm, σ = 0.02 mm. If the specification is 10.00 ± 0.05 mm, virtually all rods pass (±2.5σ). If σ were 0.03 mm, about 5% would fail. Reducing σ directly improves yield.

### Probability Distributions

**Normal (Gaussian) distribution**: The bell curve. Defined by mean μ and standard deviation σ. About 68% of values within ±1σ, 95% within ±2σ, 99.7% within ±3σ. Models measurement errors, manufacturing variations, and natural phenomena.

**Binomial distribution**: Number of successes in n independent trials, each with probability p. Mean = np, std dev = √(np(1−p)). Models pass/fail testing, defect counting.

**Poisson distribution**: Number of events in a fixed interval when events occur independently at constant rate λ. Mean = variance = λ. Models equipment failures, radioactive decay counts, defect density.

**Engineering application**: Yield analysis for semiconductor fabrication. If each process step has 99% yield and there are 100 steps, overall yield = 0.99¹⁰⁰ ≈ 37%. To achieve 90% overall yield, each step must yield approximately 99.9%.

### Statistical Process Control (SPC)

Monitor a manufacturing process using control charts. Plot sample means (X̄ chart) and ranges (R chart) over time. If a point falls outside the control limits (typically ±3σ from the mean), the process is out of control — investigate and correct before producing defective parts.

**Engineering application**: A foundry tracks the weight of cast ingots. Control chart shows the process mean is 10.2 kg with control limits at 10.0 and 10.4 kg. When a point falls at 10.5 kg, the operator knows the mold has worn or the pour temperature has drifted — correct before producing off-spec product.

### Regression and Curve Fitting

Fit a mathematical model to experimental data. Least-squares regression finds the line (or curve) that minimizes the sum of squared errors between model predictions and observations.

**Linear regression**: y = mx + b. Find m and b that best fit the data points.

**Engineering application**: Calibrate a thermocouple by measuring its voltage at known temperatures. Linear regression gives the calibration curve V(T) = aT + b. All subsequent temperature readings use this curve. Similar calibration applies to pressure gauges, flow meters, and load cells.

### Hypothesis Testing

Formally test whether observed data is consistent with a hypothesis. Example: Is a new alloy significantly stronger than the old one, or is the observed difference just random variation?

**t-test**: Compare two sample means. If the t-statistic exceeds the critical value, the difference is statistically significant.

**Engineering application**: Compare the yield strength of two heat treatment protocols. If the difference is not statistically significant (p > 0.05), use the cheaper/faster protocol. If significant, use the stronger one for critical applications.

## Numerical Methods

### Why Numerical Methods?

Most real-world engineering problems cannot be solved analytically (in closed form). The differential equations are too complex, the geometries are irregular, or the material properties are nonlinear. Numerical methods compute approximate solutions to any desired accuracy.

### Root Finding

Find x such that f(x) = 0.

**Bisection method**: Start with an interval [a,b] where f(a) and f(b) have opposite signs. Repeatedly halve the interval, keeping the half where the sign change occurs. Converges reliably but slowly (one binary digit per iteration).

**Newton's method**: xₙ₊₁ = xₙ − f(xₙ)/f'(xₙ). Much faster convergence (quadratic) but requires the derivative and may diverge if the initial guess is poor.

**Engineering application**: Find the operating point of a nonlinear circuit (diode equation: I = I₀(e^(V/Vₜ) − 1)). Find the temperature at which a material phase transition occurs. Find the flow rate at which pipe friction equals available pressure head.

### Numerical Integration

Compute ∫ₐᵇ f(x)dx when no antiderivative exists in closed form.

**Trapezoidal rule**: Approximate the area under the curve as a series of trapezoids. ∫ₐᵇ f(x)dx ≈ (h/2)[f(a) + 2f(x₁) + 2f(x₂) + … + f(b)], where h = (b−a)/n.

**Simpson's rule**: Fit parabolas instead of trapezoids. More accurate for smooth functions. ∫ₐᵇ f(x)dx ≈ (h/3)[f(a) + 4f(x₁) + 2f(x₂) + 4f(x₃) + … + f(b)].

**Engineering application**: Compute the energy produced by a varying power source over time: E = ∫₀ᵀ P(t)dt. Compute total heat absorbed by a material during heating with temperature-dependent specific heat: Q = ∫m·c(T)dT.

### Numerical Solution of ODEs

**Euler's method**: yₙ₊₁ = yₙ + h×f(tₙ, yₙ). Simple but inaccurate (first-order). Step size h must be very small for acceptable error.

**Runge-Kutta methods**: Use multiple evaluations of f per step for higher accuracy. The fourth-order Runge-Kutta (RK4) method is the workhorse: accuracy O(h⁴) with only four function evaluations per step.

**Engineering application**: Simulate the temperature evolution of a furnace during heating and cooling cycles. Simulate the transient response of an electronic circuit. Simulate the trajectory of a projectile with air resistance (nonlinear ODE with no closed-form solution).

### Finite Difference Methods for PDEs

Replace continuous derivatives with discrete differences: ∂T/∂t ≈ (Tᵢⁿ⁺¹ − Tᵢⁿ)/Δt, ∂²T/∂x² ≈ (Tᵢ₊₁ − 2Tᵢ + Tᵢ₋₁)/Δx². This converts the PDE into a system of algebraic equations that can be solved iteratively.

**Engineering application**: Compute the temperature distribution in a furnace wall during transient heating (solving the heat equation numerically). Compute stress distributions in complex geometries (early FEA). Compute fluid flow patterns in pipes and channels.

## Key Concepts Summary

| Concept | Engineering Application | Bootstrap Relevance |
|---------|------------------------|---------------------|
| Differential calculus | Rates of change: velocity, reaction rate, thermal gradient | Year 15-25 — process modeling |
| Integral calculus | Accumulated quantities: work, energy, total mass flow | Year 15-25 — energy and material balances |
| Linear algebra | Systems of equations, FEA, structural analysis | Year 25-40 — engineering analysis |
| ODEs | Dynamic systems: circuits, vibrations, heat transfer | Year 25-40 — process and circuit design |
| PDEs | Spatial-temporal phenomena: heat, waves, fields | Year 40-70 — advanced simulation |
| Probability & statistics | SPC, yield analysis, measurement uncertainty | Year 15-25 — quality control |
| Numerical methods | Computer-aided engineering, simulation | Year 30-70 — CAD, CAM, FEA, EDA |

## Dependencies

- **Core mathematics** (`mathematics.core-mathematics`): Algebra, trigonometry, and coordinate geometry are prerequisites for calculus and all subsequent applied topics
- **Enables**: Process modeling (chemistry), circuit design (electronics), structural analysis (machine tools), quality control (manufacturing), and all numerical computation (computing)

---
*Part of the [Bootciv Tech Tree](../index.md) • [Mathematics & Formal Sciences](./index.md) • [All Domains](../index.md)*
