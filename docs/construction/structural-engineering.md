# Structural Engineering

> **Node ID**: construction.structural-engineering
> **Domain**: Construction & Structural Engineering
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 10-40
> **Outputs**: structural_designs, load_calculations, foundation_plans, connection_details

## Fundamental Principles

Structural engineering ensures buildings and structures support their intended loads without excessive deflection, cracking, or collapse. Three fundamental principles govern all structural design:

1. **Equilibrium**: Forces must balance. The sum of all forces and moments acting on a structure must equal zero. If they don't, the structure moves — which means failure.
2. **Compatibility**: Deformations must be physically possible. A beam that sags too much cracks the walls it rests on. A column that shortens too much under load shifts the entire frame.
3. **Constitutive relations**: Material behavior under stress. Steel yields at 250 MPa. Concrete crushes at 30-50 MPa. Timber crushes perpendicular to grain at 3-5 MPa. These material limits define structural capacity.

### Safety Factors

No material is perfect. No calculation is exact. Safety factors account for uncertainty:

| Material | Safety Factor (ULS) | Safety Factor (SLS) | Reason |
|----------|:-------------------:|:-------------------:|--------|
| Steel | 1.5-1.67 | 1.0-1.5 | Uniform, predictable |
| Concrete | 1.5 (material) × 1.5 (load) | 1.0 | Variable quality, brittle failure |
| Timber | 2.0-3.0 | 1.0-1.5 | Natural defects, moisture variability |
| Masonry | 3.0-5.0 | 1.0 | Highly variable, no tensile capacity |

ULS = Ultimate Limit State (collapse prevention). SLS = Serviceability Limit State (deflection, cracking).

## Beam Theory

A beam is a horizontal structural member that carries loads perpendicular to its length. Beam design is the most common structural calculation.

### Simply Supported Beam (Most Common)

Beam rests on two supports. Maximum bending moment occurs at midspan for uniformly distributed loads.

**Uniformly distributed load (UDL)**:
- Maximum bending moment: M = wL²/8
- Maximum shear force: V = wL/2
- Maximum deflection: δ = 5wL⁴/(384EI)
- Where: w = load per unit length (kN/m), L = span (m), E = elastic modulus (GPa), I = second moment of area (m⁴)

**Point load P at midspan**:
- Maximum bending moment: M = PL/4
- Maximum shear force: V = P/2
- Maximum deflection: δ = PL³/(48EI)

### Cantilever Beam

One end fixed, one end free. Higher stresses for the same span — used for balconies, overhanging roofs, and cantilever bridges.

**UDL on cantilever**:
- Maximum bending moment at support: M = wL²/2
- Maximum deflection at free end: δ = wL⁴/(8EI)
- Deflection is 5× that of a simply supported beam of the same span — cantilevers are inherently less stiff.

### Beam Design Tables

**Steel beams (S235, fy = 235 MPa)** — Allowable bending stress: 140 MPa (factor 1.67)

| Section | Depth (mm) | Flange Width (mm) | Mass (kg/m) | Ixx (cm⁴) | Max UDL Span (m) at 10 kN/m |
|---------|:----------:|:------------------:|:-----------:|:----------:|:---------------------------:|
| IPE 100 | 100 | 55 | 8.1 | 171 | 2.5 |
| IPE 160 | 160 | 82 | 15.8 | 689 | 4.0 |
| IPE 200 | 200 | 100 | 22.4 | 1,943 | 5.5 |
| IPE 270 | 270 | 135 | 36.1 | 5,790 | 7.5 |
| IPE 360 | 360 | 170 | 57.1 | 16,227 | 10.0 |
| IPE 450 | 450 | 190 | 77.6 | 33,742 | 12.5 |
| IPE 600 | 600 | 220 | 122.4 | 92,080 | 17.0 |

Approximate rule of thumb: steel beam depth (mm) ≈ span (mm) / 20 to span (mm) / 25.

**Timber beams (softwood, grade C24)** — Allowable bending stress: 7.5 MPa (factor ~3)

| Beam Size (mm) | Max UDL Span (m) at 2 kN/m | Max UDL Span (m) at 4 kN/m |
|:---------------:|:--------------------------:|:--------------------------:|
| 50 × 100 | 1.8 | 1.4 |
| 50 × 150 | 2.7 | 2.1 |
| 50 × 200 | 3.5 | 2.8 |
| 75 × 200 | 4.1 | 3.2 |
| 100 × 200 | 4.6 | 3.7 |
| 100 × 250 | 5.5 | 4.4 |
| 100 × 300 | 6.5 | 5.1 |

Approximate rule: timber beam depth (mm) ≈ span (mm) / 10 to span (mm) / 15.

**Reinforced concrete beams** — Span-to-depth ratio: 12:1 to 20:1 (deflection-controlled)

| Span (m) | Approx. Overall Depth (mm) | Typical Width (mm) | Tension Rebar (approx.) |
|:--------:|:-------------------------:|:------------------:|:----------------------:|
| 3 | 250-300 | 200 | 2×16 mm |
| 4 | 300-350 | 250 | 3×16 mm |
| 5 | 350-450 | 250 | 3×20 mm |
| 6 | 450-550 | 300 | 3×25 mm |
| 8 | 600-700 | 350 | 4×25 mm |
| 10 | 750-900 | 400 | 4×32 mm |

## Column Design

Columns carry axial compression loads. Unlike beams, columns fail by buckling (lateral instability) rather than material crushing.

### Euler Buckling Formula

The critical buckling load for a slender column:

**Pcr = π²EI / (KL)²**

Where: Pcr = critical buckling load (N), E = elastic modulus (Pa), I = minimum second moment of area (m⁴), K = effective length factor, L = column length (m).

**Effective length factor K**:
- Fixed-fixed (both ends restrained): K = 0.5
- Pinned-pinned (both ends hinged): K = 1.0 (most common assumption)
- Fixed-free (cantilever): K = 2.0 (worst case)
- Fixed-pinned: K = 0.7

**Slenderness ratio**: λ = KL/r, where r = √(I/A) = radius of gyration.
- λ < 50: Short column — material crushing governs.
- 50 < λ < 150: Intermediate — both buckling and crushing considered.
- λ > 150: Slender — Euler buckling governs (never design here for buildings).

### Steel Column Load Table (S235)

| Section | Length 3 m | Length 4 m | Length 5 m | Length 6 m |
|---------|:----------:|:----------:|:----------:|:----------:|
| HEB 100 | 450 kN | 340 kN | 260 kN | 200 kN |
| HEB 140 | 850 kN | 680 kN | 540 kN | 430 kN |
| HEB 180 | 1,400 kN | 1,150 kN | 920 kN | 750 kN |
| HEB 220 | 2,100 kN | 1,780 kN | 1,470 kN | 1,220 kN |
| HEB 260 | 3,000 kN | 2,580 kN | 2,180 kN | 1,840 kN |

Values include safety factor of 1.5.

### Reinforced Concrete Column Design

- **Minimum size**: 300 × 300 mm for main columns, 250 × 250 mm for secondary.
- **Reinforcement**: 0.8-4.0% of cross-sectional area. Minimum 4 bars (one per corner). Bar diameter: 16-32 mm.
- **Ties/links**: 8-10 mm bars at spacing ≤ 15× longitudinal bar diameter, ≤ 300 mm, and ≤ smallest column dimension.
- **Concrete grade**: Minimum C25/30 for structural columns.
- **Approximate load capacity**: 0.4 × fck × Ag + 0.67 × fy × As (simplified). For 400 × 400 mm C30 column with 1.6% reinforcement: ~2,800 kN.

## Arch & Vault Design

Arches convert vertical loads into compressive forces along the arch curve. Stone and masonry excel in compression but fail in tension — arches exploit this by keeping the entire structure in compression.

### Semicircular Arch

- **Rise-to-span ratio**: 0.5 (half-circle)
- **Thrust at abutments**: H = wL²/(8h) where h = rise, L = span, w = load per unit length
- **Critical dimension**: Abutment thickness must resist horizontal thrust. Minimum abutment width ≈ 1/3 to 1/2 of span for unreinforced masonry.
- **Ring thickness**: Minimum 1/15 of span for stone arches, 1/10 for brick. 5 m span → 330 mm stone or 500 mm brick ring thickness.

### Pointed Arch (Gothic)

- More efficient than semicircular — lower horizontal thrust for the same span.
- Rise-to-span ratio: 0.5 to 1.0 (taller arches produce less thrust).
- Enables larger windows (more light) between structural buttresses.

### Vault

An arch extended in the third dimension. Barrel vault (simplest): semicircular arch extended linearly. Groin vault: two barrel vaults intersecting at right angles — concentrates thrust at the four corner piers, allowing walls between piers to be opened with windows.

- **Barrel vault thrust**: Same as arch (per unit length). Continuous wall buttress required along both sides.
- **Groin vault thrust**: Concentrated at corners. Pier dimensions: 1/8 to 1/6 of vault span.

## Truss Analysis

A truss is a structural framework of straight members connected at nodes (joints). Members carry only axial forces (tension or compression) — no bending. This makes trusses highly efficient for long spans.

### Common Truss Types

**Pratt truss**: Diagonal members slope downward toward center. Diagonals in tension, verticals in compression. Efficient for gravity loads. Span: 10-60 m.

**Warren truss**: Equilateral triangle pattern. Alternating tension-compression diagonals. No verticals (simpler fabrication). Span: 10-50 m.

**Howe truss**: Diagonal members slope upward toward center. Diagonals in compression, verticals in tension. Good for timber construction (compression diagonals in wood, tension verticals in steel rod). Span: 10-30 m.

### Method of Joints

At each joint, the forces must satisfy equilibrium: ΣFx = 0 and ΣFy = 0. Solve joint by joint, starting from a support where reaction forces are known.

**Example: 10 m span Pratt truss, 5 panels, UDL = 10 kN/m**:
- Total load: 100 kN. Each node load: 20 kN.
- Support reactions: 50 kN each (symmetric).
- Top chord: Compression, maximum near center. Peak: ~125 kN.
- Bottom chord: Tension, maximum near center. Peak: ~125 kN.
- Diagonals: Tension, maximum near supports. Peak: ~28 kN.
- Verticals: Compression, maximum near supports. Peak: ~20 kN.

## Foundation Design

Foundations transfer structural loads to the ground. The bearing capacity of soil determines foundation size.

### Soil Bearing Capacity

| Soil Type | Allowable Bearing Capacity | Notes |
|-----------|:-------------------------:|-------|
| Hard rock | 1,000-10,000 kN/m² | Granite, basalt |
| Soft rock | 300-1,000 kN/m² | Sandstone, shale |
| Dense gravel/sand | 300-600 kN/m² | Good foundation material |
| Medium sand | 150-300 kN/m² | Acceptable |
| Loose sand | 50-100 kN/m² | Poor — prone to settlement |
| Stiff clay | 150-300 kN/m² | Acceptable if dry |
| Soft clay | 50-100 kN/m² | Poor — settlement problems |
| Organic soil/peat | <25 kN/m² | Unusable — must excavate or pile |

### Strip Footing (Wall Foundation)

Continuous strip of concrete beneath load-bearing walls. Width determined by wall load ÷ soil bearing capacity.

**Minimum dimensions**: Width ≥ 2 × wall thickness. Depth ≥ 300 mm below ground level (frost line in cold climates: 600-1200 mm).

**Reinforcement**: Minimum 3 bars top and bottom, 10 mm diameter, in each direction. Concrete: minimum C20/25.

**Example**: Wall load 80 kN/m, soil bearing capacity 200 kN/m² → footing width = 80/200 = 0.4 m. Use 500 mm minimum width for constructability.

### Pad Footing (Column Foundation)

Square or rectangular concrete pad under individual columns.

**Area**: A = Column load / Soil bearing capacity. For 500 kN column on 200 kN/m² soil → A = 2.5 m² → 1.6 m × 1.6 m pad.

**Thickness**: Minimum 300 mm or pad width × 0.35 (to resist punching shear). Punching shear check: critical perimeter at 1.5× slab thickness from column face. Shear stress = column load / (perimeter × effective depth) ≤ 0.5 MPa for unreinforced.

**Reinforcement**: Bottom mesh (tension from bending). Bar diameter: 12-20 mm at 150-200 mm spacing each way.

### Settlement

All foundations settle under load. Total settlement should be limited to:
- 25 mm for isolated foundations on sand
- 50 mm for isolated foundations on clay
- Differential settlement (one corner vs another): limit to L/500 (where L = distance between points)

Excessive differential settlement causes wall cracking, door/window sticking, and structural distress.

## Connection Design

### Steel Connections

**Bolted connections**: High-strength bolts (grade 8.8, proof load 580 MPa) in clearance holes (+2 mm). Minimum 2 bolts per connection. Edge distance ≥ 2× bolt diameter. Bolt spacing: 3-6× bolt diameter.

**Single-shear capacity of 20 mm Grade 8.8 bolt**: ~145 kN (double for double-shear).

**Welded connections**: Fillet welds (most common). Leg length: minimum 6 mm for 10 mm plate, increases with plate thickness. Weld capacity: 0.7 × leg length × weld length × 200 MPa (for E43 electrodes). A 6 mm fillet weld carries ~0.84 kN per mm of length.

**Riveted connections**: Hot-driven rivets (19-25 mm diameter). Clamp plates tightly. Shear capacity similar to same-diameter bolt. Largely superseded by bolts and welds but historically important.

### Timber Connections

**Bolted timber joints**: Steel bolts through drilled holes. Bolt capacity governed by timber bearing (crushing) perpendicular to grain. 20 mm bolt in 75 mm thick softwood: ~15 kN per bolt in single shear. Minimum 2 bolts per connection.

**Timber pegs**: Traditional — 19-25 mm hardwood pegs in mortise-tenon joints. Peg shear capacity: ~2-4 kN per peg. Used in traditional timber framing.

**Metal brackets**: Modern — galvanized steel brackets (joist hangers, post bases) nailed or bolted to timber. Provides standardized, reliable connections. Nail capacity in withdrawal: ~1 kN per 4 mm × 75 mm nail in softwood.

## Cross-References

- **[Building Materials & Methods](building-materials.md)**: Timber, masonry, and roofing material properties
- **[Industrial Buildings & Heavy Foundations](industrial-buildings.md)**: Machine foundations and vibration isolation
- **[Cement & Concrete](../chemistry/cement.md)**: Concrete mix designs, rebar, and curing — cross-reference for reinforced concrete
- **[Iron & Steel](../metals/iron-steel.md)**: Structural steel production and properties
- **[Precision Metrology](../measurement/index.md)**: Measurement instruments for construction accuracy
- **[Mathematics](../mathematics/index.md)**: Calculus and geometry for structural analysis

---

*Part of the [Bootciv Tech Tree](../index.md) • [Construction](./index.md) • [All Domains](../index.md)*
