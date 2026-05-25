# Building Materials & Methods

> **Node ID**: construction.building-materials
> **Domain**: Construction & Structural Engineering
> **Dependencies**: [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 5-25
> **Outputs**: timber_frames, masonry_walls, roofing_systems, waterproofing, scaffolding, hoisting_equipment

## Timber Framing & Joinery

Timber is the first structural material available for building. Properly joined timber frames can span 6-12 m and support multi-story structures for centuries. The key advantage: timber is renewable, workable with hand tools, and provides both compression and tension capacity.

### Structural Timber Properties

| Property | Softwood (Pine) | Hardwood (Oak) | Notes |
|----------|:---------------:|:--------------:|-------|
| Density | 450-550 kg/m³ | 600-750 kg/m³ | Oak ~30% heavier |
| Bending strength | 30-45 MPa | 50-70 MPa | Allowable ~1/3 of ultimate |
| Compression ∥ grain | 25-35 MPa | 40-55 MPa | Along grain |
| Compression ⊥ grain | 3-5 MPa | 6-10 MPa | Across grain — much weaker |
| Tension ∥ grain | 50-80 MPa | 80-120 MPa | Knots reduce significantly |
| Elastic modulus | 9-12 GPa | 10-14 GPa | Stiffness |
| Moisture content (green) | 30-50% | 30-50% | Must season before use |
| Moisture content (seasoned) | 12-18% | 12-18% | Air-dry 1 year per 25 mm thickness |
| Shrinkage (green to dry) | 3-5% radial | 4-6% radial | Tangential shrinkage is ~2× radial |

### Timber Seasoning

Fresh-cut (green) timber contains 30-50% moisture. It must be dried to 12-18% for structural use. Green timber shrinks as it dries — joints loosen and members warp if assembled green.

- **Air drying**: Stack timber with 25 mm stickers between layers in a covered, ventilated space. Drying rate: 1 year per 25 mm of thickness for softwood, 2 years per 25 mm for hardwood. Southern exposure accelerates drying.
- **Kiln drying**: Heated chamber at 60-80°C with controlled humidity. Dries 25 mm boards in 1-2 weeks. Risk of case-hardening and checking if too rapid.
- **Checking**: Surface cracks from too-rapid drying. Acceptable if <1/4 beam depth. Unacceptable if it penetrates >1/3 depth — beam must be rejected or re-graded.

### Key Joinery Types

**Mortise-and-tenon**: The fundamental timber joint. A rectangular projection (tenon, typically 1/3 beam width) fits into a matching socket (mortise). Secured with hardwood pegs (oak or ash, 19-25 mm diameter). Peg holes offset 3-5 mm to draw joint tight. Load transfer: bearing on tenon cheeks (compression ∥ grain) and peg shear.

**Dovetail**: Fan-shaped tenon resists pull-out. Used for tension connections — tie beams to wall plates, rafter feet to wall plates. Angle: 1:6 to 1:8 slope for softwood (shallower to avoid shear failure), 1:4 to 1:5 for hardwood. Minimum depth: 1/3 beam depth.

**Scarf joint**: End-to-end splicing of timbers too short for the span. Half-lap (simplest, 4× beam depth overlap), tabled scarf (with wedge, 6× depth), or scarfed with bridles (strongest, 8× depth). All scarf joints reduce beam strength by 30-50% at the joint.

**Housed joints**: Mortise extends through the receiving member. Provides superior resistance to twisting and racking. Used for floor joists into beams (joist pockets) and rafter feet into wall plates.

### Timber Frame Design Parameters

- **Beam span-to-depth ratio**: 15:1 to 20:1 for floor joists (deflection-controlled), 10:1 to 15:1 for heavily loaded beams.
- **Deflection limit**: L/360 for floors (L = span), L/240 for roofs. Excessive deflection causes plaster cracking and occupant discomfort.
- **Post (column) slenderness**: Height-to-least-dimension ratio ≤ 50 for main posts, ≤ 30 for heavily loaded columns. Above this, buckling governs design.
- **Bracing**: Knee braces (minimum 1.2 m length, 45° angle) required at every post-to-beam connection to resist lateral loads (wind, racking). Without bracing, frames collapse sideways.

## Stone & Masonry Construction

### Stone Types for Construction

| Stone | Compressive Strength | Workability | Best Use |
|-------|:-------------------:|:-----------:|----------|
| Granite | 100-200 MPa | Very hard | Foundations, bridge abutments |
| Limestone | 30-80 MPa | Moderate | Wall construction, decorative |
| Sandstone | 20-60 MPa | Easy | Wall construction, carving |
| Slate | 70-150 MPa | Splits easily | Roofing tiles, flooring |

### Ashlar Masonry (Cut Stone)

Regularly shaped stones with finely dressed faces. Highest quality masonry — minimum joint thickness (3-6 mm). Each stone cut to exact dimensions with chisel and hammer.

- **Course height**: 150-300 mm per course for standard ashlar.
- **Bond pattern**: Overlap between courses must be ≥ 100 mm or ≥ 1/3 stone length to maintain structural bond.
- **Through-stones**: Full-width stones extending through the entire wall thickness at 1.5 m vertical intervals. Prevent wall delamination into inner and outer leaves.

### Rubble Masonry (Uncut Stone)

Roughly shaped or unshaped stones laid in mortar. Less expensive and faster than ashlar. Requires thicker mortar joints (10-25 mm).

- **Random rubble**: Stones placed without regular courses. Requires skilled masons for stable arrangement. Wall thickness: minimum 400 mm for single-story, 600 mm for two-story.
- **Coursed rubble**: Stones roughly sorted by height into horizontal courses. Stronger than random rubble due to more regular load distribution. Course height: 150-300 mm.
- **Mortar**: Lime mortar (see [Lime Production](../ceramics/lime.md)) for flexibility and breathability. Cement mortar for high-strength applications (see [Cement & Concrete](../chemistry/cement.md)). Mix: 1:3 (cement:sand) or 1:2.5 (lime:sand) by volume.

### Brick Masonry

Sun-dried mud brick (adobe): Simplest — clay mixed with straw, dried in sun. Compressive strength: 1-2 MPa. Suitable for dry climates only. Wall thickness: minimum 300 mm for single-story.

Fired clay brick: Fired at 900-1100°C. Compressive strength: 10-50 MPa (common brick 10-20 MPa, engineering brick 50+ MPa). Standard size: 215 × 102.5 × 65 mm (UK) or 230 × 110 × 65 mm (metric). Wall thickness: one brick thick (215-230 mm) for single-story load-bearing.

- **Bonding**: English bond (alternating stretchers and headers per course) or Flemish bond (alternating stretchers and headers within each course). Both provide adequate structural bond.
- **Mortar joints**: 10 mm standard. Raked joints for aesthetic, flush or tooled for weather resistance.
- **Compressive strength of brickwork**: Approximately 30-40% of individual brick strength due to mortar joint weakness. A wall of 20 MPa bricks in 1:4 mortar achieves 5-8 MPa.

## Roofing Systems

### Timber Roof Trusses

The roof is the most complex timber structure in a building. It must span the full width of the building, support its own weight plus snow and wind loads, and resist lateral spreading forces.

**King-post truss**: Simplest truss. Span: 5-9 m. Components: two rafters (inclined), one king post (vertical, from peak to tie beam), one tie beam (horizontal, prevents wall spreading). Rafter angle: 30-45° (steeper sheds snow better, shallower uses less timber).

**Queen-post truss**: Two vertical queen posts. Span: 8-14 m. Allows a flat ceiling between the posts while the outer sections remain open. Queen posts carry compression loads from the rafters down to the tie beam.

**Hammer-beam truss**: For spans 12-20 m. Short horizontal hammer beams project from the wall, supported by curved brackets. Eliminates the need for a full-span tie beam — critical for large halls and churches. The most efficient timber truss form for long spans.

**Truss spacing**: 3-5 m on center for residential, 6-10 m for industrial buildings. Purlins (horizontal beams spanning between trusses) carry the roof decking.

### Roof Loading

| Load Type | Typical Value | Notes |
|-----------|:------------:|-------|
| Dead load (roofing) | 0.3-0.7 kN/m² | Slate: 0.5, Clay tile: 0.6, Metal sheet: 0.15 |
| Dead load (structure) | 0.3-0.5 kN/m² | Timber framing + decking |
| Snow load | 0.5-2.5 kN/m² | Depends on climate; steep roofs shed snow |
| Wind uplift | 0.5-1.5 kN/m² | Critical for lightweight roofing |
| **Total design load** | **1.5-4.5 kN/m²** | Dead + live with safety factor |

### Roofing Materials

**Slate**: Natural stone split into thin (4-8 mm) tiles. Extremely durable (100+ years). Heavy (0.5 kN/m²). Fixed with copper or galvanized nails to timber battens. Minimum roof pitch: 25°. Overlap: minimum 75 mm headlap.

**Clay tile**: Fired at 900-1000°C. Interlocking or plain tiles. Durable (50+ years). Heavy (0.6 kN/m²). Minimum pitch: 30° for plain tiles, 15° for interlocking. Two tiles nailed per square meter at minimum.

**Metal roofing**: Galvanized steel or copper sheet. Lightweight (0.15 kN/m²). Corrugated profile for stiffness — 0.5 mm steel sheet with 75 mm corrugation depth spans 1.2-1.5 m between purlins. Fast installation. Minimum pitch: 5° for corrugated, 10° for standing seam. Condensation control required (ventilated air gap below metal).

**Thatch (emergency/temporary)**: Reed or straw bundles, 300 mm thick. Good insulation. Fire risk — treat with borax solution (5% by weight). Maximum building height: 2 stories. Not suitable for industrial buildings.

## Waterproofing

### Foundation Waterproofing

Below-grade walls and foundations must resist water penetration. Hydrostatic pressure from groundwater forces water through any crack or pore.

- **Bituminous coating**: Hot-applied bitumen (asphalt) at 180-200°C, 2-3 coats to 3-5 mm total thickness. Applied to exterior of foundation walls. Protects against moisture but not full hydrostatic head.
- **Cementitious waterproofing**: Portland cement + fine sand + waterproofing additive (sodium silicate or acrylic emulsion). Trowel-applied in 2-3 coats. Can resist moderate hydrostatic pressure. Best for positive-side (exterior) application.
- **Clay blanket**: Compacted clay (bentonite or natural clay with >30% fines) 150-300 mm thick placed against foundation wall. Swells when wet, sealing cracks. Zero maintenance. Must be protected from drying out during construction.
- **Drainage layer**: Gravel (20-40 mm) 150-200 mm thick against foundation wall with perforated drain pipe at footing level. Relieves hydrostatic pressure — the most effective approach combined with any membrane.

### Above-Grade Waterproofing

- **Lead flashing**: 1.5-2.0 mm sheet lead shaped around roof-wall junctions, chimneys, and valleys. Lead is malleable, corrosion-resistant, and lasts 100+ years. Soldered or welted joints.
- **Copper flashing**: 0.5-0.7 mm sheet copper. Lighter than lead, equally durable. Patinas to green (copper carbonate) — protective and attractive.
- **Bitumen felt**: Organic or fiberglass mat saturated with bitumen. Used as underlayment beneath roofing materials. Minimum 2 layers for low-slope roofs. Torch-applied or nailed.

## Scaffolding & Hoisting

### Timber Scaffolding

Temporary structure providing access to work at height. Built from timber poles (75-100 mm diameter), planks (250-40 mm × 50 mm minimum), and rope lashings.

- **Standards (vertical members)**: 100 mm diameter poles, maximum 4 m spacing. Founded on firm base plates or sole plates (250 × 250 mm timber pads) to prevent settling.
- **Ledgers (horizontal members)**: 75 mm diameter poles, lashed to standards at 2 m vertical intervals.
- **Putlogs (wall ties)**: 75 mm poles, one end lashed to ledger, other end inserted into wall mortar joint (70 mm minimum embedment). Spacing: 1.2-1.5 m.
- **Working platform**: 50 mm thick planks, minimum 600 mm wide (two planks). Planks overlap standards by minimum 300 mm. Toe boards (150 mm) prevent tools falling.
- **Capacity**: Light duty scaffolding — 1.2 kN/m² (workers and hand tools only). NEVER use for material storage.

### Hoisting Systems

**Block and tackle**: Rope reeved through pulley blocks. Mechanical advantage equals number of rope parts supporting the load. 4:1 purchase is common — 100 kg pull lifts 400 kg. Use manila or hemp rope minimum 20 mm diameter (safe working load ~400 kg for 4:1 system).

**Windlass / crab winch**: Horizontal drum wound with rope, turned by crank handle. Drum diameter 150-200 mm. Crank radius 300-400 mm. Gear ratio (if compound) provides 4-8× mechanical advantage. Capacity: 500-2000 kg depending on rope size and gear ratio.

**Scaffold hoist**: Light crane mounted on scaffolding standard. Jib arm 1.5-2.5 m. Chain block or lever hoist on jib. Capacity: 500-1000 kg. Used for raising bricks, mortar, and timber to working height.

**Safety**: Never exceed rated capacity. Inspect rope for wear, fraying, and degradation before each use. Minimum safety factor: 5:1 for fiber rope, 4:1 for chain. Tag lines control load swing. Keep hoisting area clear below.

## Cross-References

- **[Lime Production](../ceramics/lime.md)**: Lime mortar for masonry construction — fundamental binder
- **[Cement & Concrete](../chemistry/cement.md)**: Portland cement and concrete — cross-reference for concrete mix designs
- **[Stone & Wood Tools](../foundations/index.md)**: Basic toolmaking for construction
- **[Rope Making](../textiles/rope-making.md)**: Rope for hoisting, scaffolding, and lashing
- **[Metals](../metals/index.md)**: Structural steel, nails, and hardware

---

*Part of the [Bootciv Tech Tree](../index.md) • [Construction](./index.md) • [All Domains](../index.md)*
