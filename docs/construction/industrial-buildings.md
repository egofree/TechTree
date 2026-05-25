# Industrial Buildings & Heavy Foundations

> **Node ID**: construction.industrial-buildings
> **Domain**: Construction & Structural Engineering
> **Dependencies**: [`energy.electricity`](../energy/electricity.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 15-40
> **Outputs**: industrial_facilities, machine_foundations, vibration_isolation, crane_runways, factory_floors

## Overview

Industrial buildings differ fundamentally from residential construction. They must support heavy point loads from machinery, resist dynamic forces from forging hammers and stamping presses, provide clear spans of 15-30 m for production lines, and accommodate overhead cranes moving 5-50 tonnes. The building is not just shelter — it is an integral part of the production system.

Every machine tool, forge hammer, steam engine, and generator requires a foundation designed to carry its weight and resist its dynamic forces. A lathe with 0.01 mm tolerance cannot sit on a floor that deflects 0.1 mm under a passing forklift. A forge hammer delivering 50 kJ blows will destroy its own foundation (and the surrounding building) if not properly isolated.

## Industrial Building Types

### Steel-Frame Factory

The dominant industrial building type. Steel columns (HEB 200-400) at 6-10 m spacing, steel roof trusses spanning 15-30 m, steel purlins at 1.5-2.5 m spacing, and corrugated metal or asbestos-cement roof sheeting.

**Design parameters**:
- Clear height: 6-12 m (minimum clearance for crane + tallest machine)
- Bay width: 6-10 m (column spacing)
- Bay length: 18-30 m (between expansion joints)
- Roof pitch: 5-10° (minimum for drainage)
- Floor: 150-300 mm reinforced concrete slab on compacted subgrade
- Wall cladding: Corrugated metal sheet, brick, or concrete block

**Steel framing advantages**: Fast erection (bolted connections), clear spans without interior columns, easily modified or expanded, resists wind and seismic loads, fire-resistant with intumescent coating.

### Reinforced Concrete Frame Factory

For heavy industry with high floor loads, chemical exposure, or fire risk. Concrete columns (400-600 mm), concrete beams (300-600 mm wide × 500-1000 mm deep), and concrete roof slabs (150-200 mm).

**Advantages over steel**: Inherent fire resistance (2-4 hour rating without protection), chemical resistance (concrete is inert to most industrial chemicals), corrosion resistance (no exposed steel to rust), superior vibration damping (concrete mass absorbs dynamic energy).

**Disadvantages**: Slower construction (concrete curing time), heavier (larger foundations required), more difficult to modify or demolish.

### Multi-Story Industrial Buildings

For light manufacturing, assembly, and warehousing in space-constrained sites. 3-6 stories, floor-to-floor height 3.5-5 m, floor live load 5-15 kN/m² (vs 2 kN/m² for offices).

- **Beam-column frame**: Steel or concrete. Beam span: 6-10 m.
- **Flat slab**: Concrete slab supported directly on columns (no beams). Simpler formwork, flexible layout. Span: 6-8 m. Minimum slab thickness: L/30 (200-270 mm).
- **Floor vibration**: Critical for precision equipment. Natural frequency of floor must exceed equipment forcing frequency by 50% minimum.

## Machine Foundations

### Design Philosophy

Machine foundations serve three purposes: (1) support the machine weight without excessive settlement, (2) transmit dynamic forces to the ground without damaging the machine or adjacent equipment, and (3) prevent transmission of vibration to the rest of the building.

### Foundation Types

**Block foundation**: Massive concrete block (3-5× machine weight) supporting the machine directly. Simplest design. Used for reciprocating machines (engines, compressors) and rotating machines (motors, turbines).

- **Mass ratio**: Foundation mass / machine mass ≥ 3 for rotating equipment, ≥ 5 for reciprocating equipment.
- **Base area**: Sized for soil bearing capacity under combined static + dynamic loads.
- **Depth**: Minimum 0.6× foundation width (to resist rocking).
- **Concrete grade**: Minimum C25/30. No construction joints in the block — monolithic pour required.

**Mat (raft) foundation**: A thick concrete slab covering the entire machine area, supporting multiple machines. Used when individual footings would overlap or when soil is weak.

- **Thickness**: 600-1500 mm depending on loads and spacing.
- **Reinforcement**: Heavy bottom mat (tension from bending) and top mat (temperature/shrinkage). Typical: 20-32 mm bars at 150-200 mm spacing each way, top and bottom.
- **Advantage**: Distributes loads uniformly, reduces differential settlement between machines.

**Table foundation**: Elevated concrete platform supported by columns or piers, isolating the machine from floor vibrations. Used for precision equipment (precision grinders, coordinate measuring machines, wafer processing tools).

- **Natural frequency**: Designed to be 50% below or above the machine operating frequency to avoid resonance.
- **Isolation**: Neoprene pads or spring isolators at support points.

### Foundation Design for Specific Equipment

**Lathe (1-5 tonne)**: Block foundation 1.5-2.5 m deep, 1.2× machine footprint area. Leveling wedges at anchor bolt positions. Maximum floor deflection under adjacent traffic: <0.05 mm.

**Forge hammer (5-50 kJ)**: Massive block foundation (10-15× hammer weight). Timber or cork padding between hammer base and foundation (impact isolation). Foundation pit surrounded by 150 mm sand gap (vibration isolation from building). Adjoining floor slabs must be separated by expansion joint.

**Steam engine (50-500 HP)**: Block foundation 2-3 m deep, isolated from building floor slab. Anchor bolts: 4-8× 30-50 mm diameter, embedded 600-900 mm with plate anchors at bottom. Grout pad under engine base: 50-75 mm non-shrink grout for precise leveling.

**Generator (100-1000 kVA)**: Block foundation with mass ≥ 5× generator mass. Balanced rotating loads but requires vibration isolation for adjacent sensitive equipment. Anti-vibration mounts (spring or rubber) at foundation base if required.

## Vibration Isolation

### Principles

Vibration in buildings originates from machinery (rotating imbalance, impact forces), external traffic, and human activity. For precision manufacturing, vibration must be limited to:

| Equipment Type | Maximum Floor Velocity | Maximum Floor Displacement |
|---------------|:---------------------:|:-------------------------:|
| Optical inspection | 0.05 mm/s | 0.001 mm |
| Precision grinder | 0.1 mm/s | 0.005 mm |
| Coordinate measuring machine | 0.2 mm/s | 0.010 mm |
| Standard machine tool | 0.5 mm/s | 0.025 mm |
| General factory floor | 1.0 mm/s | 0.050 mm |

### Isolation Methods

**Inertia block**: A massive concrete block (5-10× equipment mass) placed between the machine and the floor. The block's inertia resists vibration excitation. Natural frequency: f = (1/2π) × √(k/m) where k = isolation spring stiffness, m = block mass. Lower frequency = better isolation.

**Spring isolators**: Steel coil springs supporting the inertia block or machine. Available in 1-25 Hz natural frequency range. Isolation efficiency: 85-98% above 2× natural frequency. Minimum static deflection: 25 mm for 3 Hz isolation, 100 mm for 1.5 Hz isolation.

**Rubber/neoprene pads**: Elastomeric pads under equipment. Simpler than springs. Natural frequency: 5-15 Hz. Isolation efficiency: 50-80%. Limited by rubber creep under sustained load. Replace every 10-15 years.

**Cork pads**: Compressed natural cork sheets (50-150 mm thick). Natural frequency: 10-20 Hz. Good for high-frequency vibration isolation (>30 Hz). Low cost, fire-resistant. Used under rail tracks and heavy machinery.

**Air springs**: Pressurized air bags supporting the equipment. Lowest natural frequency achievable (0.5-2 Hz). Excellent isolation (>99% above 5 Hz). Require compressed air supply and leveling control. Used for semiconductor equipment and precision metrology.

### Vibration Isolation Design Example

**Problem**: 10-tonne precision grinder (operating at 1500 RPM = 25 Hz) needs floor vibration <0.1 mm/s. Adjacent forge hammer generates 10 Hz vibrations.

**Solution**: Inertia block (50 tonnes) on spring isolators with 3 Hz natural frequency.
- Transmissibility at 10 Hz: T = 1/((f/fn)² - 1) = 1/((10/3)² - 1) = 0.10 → 90% isolation
- Transmissibility at 25 Hz: T = 1/((25/3)² - 1) = 0.015 → 98.5% isolation
- Static deflection: δ = g/(2πfn)² = 9.81/(2π×3)² = 0.028 m = 28 mm
- Spring stiffness required: k = (2πfn)² × m = (2π×3)² × 50,000 = 17.8 MN/m total

## Crane Runway Design

### Overhead Traveling Cranes

Industrial buildings frequently require overhead cranes for material handling. The crane runway is the structural system supporting the crane rails — typically two parallel beams spanning the building length.

**Crane capacity**: 5-50 tonnes typical for machine shops and foundries. 100+ tonnes for heavy steel fabrication.

**Crane runway beam design**:
- Span: 6-30 m (building bay width)
- Steel section: Compound welded I-beam or standard HEB profile
- Deflection limit: L/800 for light cranes (<10 t), L/1000 for heavy cranes (≥10 t). Tighter than normal beam deflection limits because crane operation causes visible and uncomfortable bouncing.
- Lateral load: 10% of crane capacity (from crane braking and load swinging)
- Fatigue: Crane runways experience millions of load cycles. Fatigue design required. Detail category: ≥ 71 (welded) or ≥ 112 (bolted connections).

**Crane rail**: Special steel rail (QU70-QU120) or standard railway rail bolted to runway beam. Rail clips at 500-600 mm spacing. Rail splice: fishplates with minimum 4 bolts per joint. Rail tolerance: ±1 mm alignment, ±0.5 mm gauge.

**Columns supporting crane runway**: Must resist combined axial load (building + crane dead load) + bending moment from crane lateral forces + fatigue from repeated crane loads. Typical: HEB 300-500 in steel, or 400-600 mm reinforced concrete.

## Industrial Flooring

### Floor Load Classification

| Floor Class | Live Load (kN/m²) | Typical Use |
|:----------:|:-----------------:|-------------|
| Light | 5-10 | Assembly, light storage |
| Medium | 10-20 | Machine shops, warehousing |
| Heavy | 20-50 | Heavy machinery, steel stock |
| Very heavy | 50+ | Foundries, forge shops |

### Floor Construction

**Slab-on-grade**: Most common. Reinforced concrete slab (150-300 mm) on compacted granular subbase (150-300 mm crushed stone). Subbase prevents settlement and provides uniform support.

- **Joint spacing**: 4-6 m in each direction (control joints for shrinkage cracking). Saw-cut joints at 1/4 slab depth within 12-24 hours of pouring.
- **Reinforcement**: Welded wire mesh (150 × 150 mm × 5 mm) or steel fiber (30-50 kg/m³). Prevents crack widening.
- **Wear surface**: Monolithic dry-shake hardener (corundum or emery aggregate) floated into wet concrete surface. Provides abrasion resistance for forklift traffic.
- **Flatness**: Floor flatness specification (FF/FL numbers). FF 30-50 for general industrial, FF 50-80 for precision equipment areas. Measured with 3 m straightedge — maximum gap ≤ 3 mm for general, ≤ 1.5 mm for precision.

**Raised access floor**: For areas requiring under-floor services (electrical, compressed air, data). Steel or concrete panels on adjustable pedestals. Panel size: 600 × 600 mm. Floor height: 150-600 mm above structural slab. Load capacity: 5-20 kN/m². Not suitable for heavy equipment.

### Floor Loading from Equipment

Point loads from machine tools create concentrated stresses far exceeding the uniform floor load rating. A 5-tonne lathe on 1 m² base exerts 50 kN/m² — 5× the "heavy" floor rating.

**Rule of thumb**: Machine base area must spread load to ≤ allowable floor bearing pressure. If machine base is too small, provide a steel spreader plate or concrete plinth.

**Forklift loads**: A 2-tonne forklift carrying a 2-tonne load on 200 mm wide wheels exerts 100 kN per wheel. This single point load can exceed floor capacity. Wheel load contact area must be checked.

## Steel Reinforcement Specifications

### Rebar Grades and Sizes

| Bar Diameter (mm) | Cross-section (mm²) | Weight (kg/m) | Yield Strength (MPa) |
|:-----------------:|:-------------------:|:-------------:|:-------------------:|
| 8 | 50 | 0.40 | 400-500 |
| 10 | 79 | 0.62 | 400-500 |
| 12 | 113 | 0.89 | 400-500 |
| 16 | 201 | 1.58 | 400-500 |
| 20 | 314 | 2.47 | 400-500 |
| 25 | 491 | 3.85 | 400-500 |
| 32 | 804 | 6.31 | 400-500 |
| 40 | 1,257 | 9.86 | 400-500 |

### Concrete Mix Ratios for Industrial Use

| Application | Mix (C:S:A by weight) | W/C Ratio | 28-day Strength | Notes |
|-------------|:---------------------:|:---------:|:---------------:|-------|
| Machine foundation | 1:1.5:3 | 0.40-0.45 | 35-45 MPa | High strength, low shrinkage |
| Factory floor slab | 1:2:4 | 0.45-0.50 | 25-35 MPa | Standard structural |
| Foundation blinding | 1:3:6 | 0.60 | 15-20 MPa | Leveling layer only |
| Grout (non-shrink) | 1:1 (cement:sand) | 0.30 | 50+ MPa | Machine leveling pads |
| Mass concrete (dams) | 1:3:6 | 0.50-0.60 | 15-20 MPa | Low heat of hydration |

## Waterproofing Industrial Buildings

Industrial buildings have specific waterproofing needs beyond residential construction:

- **Machine pit waterproofing**: Below-grade pits for equipment must be tanked (fully waterproofed). Bentonite clay panels or sheet membrane (PVC or modified bitumen) applied to exterior. Interior drainage sump with automatic pump as backup.
- **Chemical-resistant flooring**: Acid-resistant ceramic tiles or epoxy coating on concrete. Minimum 3 mm epoxy for light chemical exposure, 6 mm for moderate, acid-brick with chemical-resistant mortar for heavy exposure.
- **Roof drainage**: Minimum 1% slope (1:100) for flat roofs. Gutters sized for maximum rainfall intensity (100 mm/hour design). Overflow provisions (secondary drains or scuppers) at 50 mm above primary drain level.

## Cross-References

- **[Building Materials & Methods](building-materials.md)**: Timber framing, masonry, scaffolding
- **[Structural Engineering](structural-engineering.md)**: Beam design, column design, foundation theory
- **[Cement & Concrete](../chemistry/cement.md)**: Concrete mix design, rebar, and curing — cross-reference for detailed concrete specifications
- **[Lubricants](../chemistry/lubricants.md)**: Machinery lubrication systems
- **[Energy](../energy/index.md)**: Electrical power supply to industrial buildings
- **[Machine Tools](../machine-tools/index.md)**: The heavy equipment that requires these specialized foundations

---

*Part of the [Bootciv Tech Tree](../index.md) • [Construction](./index.md) • [All Domains](../index.md)*
