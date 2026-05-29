# Building Materials & Methods

> **Node ID**: construction.building-materials
> **Domain**: [Construction](./index.md)
> **Dependencies**: [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: [`construction.industrial-buildings`](./industrial-buildings.md), [`construction.structural-engineering`](./structural-engineering.md)
> **Timeline**: Years 5-25
> **Outputs**: timber_frames, masonry_walls, roofing_systems, waterproofing, scaffolding, hoisting_equipment
> **Critical**: Yes — all permanent structures require building materials; without them, civilization remains limited to temporary shelters



Building materials and methods cover the production and use of timber, stone, brick, roofing, waterproofing, scaffolding, and hoisting systems for permanent construction. These materials form the structural backbone of every building in the bootstrap chain — from houses and workshops to factories and fortifications.

The capability begins with timber framing (the first structural material workable with hand tools) and progresses through stone masonry, fired brick, and manufactured roofing as the industrial base develops. Each material has specific structural properties, construction techniques, and failure modes that dictate where and how it can be used.

Position in the dependency chain: [basic tools](../foundations/tools-basic.md) enable timber work and stone dressing. Downstream, [structural engineering](./structural-engineering.md) applies these materials to designed structures, and [industrial buildings](./industrial-buildings.md) requires heavy-duty versions of all these materials for factory construction.


## Prerequisites

## Materials

- **Timber**: Hardwood (oak, chestnut) or softwood (pine, fir) logs, 150-400 mm diameter, 2-8 m length. Green or seasoned.
- **Stone**: Limestone, sandstone, or granite from quarry or field collection. Block size: 100-600 mm per side.
- **Clay**: For mud brick and fired brick. Plasticity index >10. Free from organic matter.
- **Sand**: For mortar. Clean, well-graded, 0.1-2 mm particle size.
- **[Lime](../ceramics/lime.md)**: For lime mortar. Quicklime (CaO) or hydrated lime.
- **Bitumen**: For waterproofing. Natural asphalt or distilled from petroleum.

## Tools and Equipment

- [Basic hand tools](../foundations/tools-basic.md): Axe, adze, saw, chisel, hammer, square, plumb bob, level.
- [Rope](../textiles/rope-making.md): Manila or hemp, 12-25 mm diameter, for hoisting and scaffolding lashings.
- Measuring rods: 1-2 m graduated sticks for layout.
- Balance scales: For weighing mortar ingredients.

## Knowledge

- **Timber grading**: Identifying knots, grain direction, shakes, and seasoning quality.
- **Stone dressing**: Chisel technique for squaring stone blocks.
- **Mortar mixing**: Proportions, water content, working time.
- **Structural intuition**: Understanding load paths, compression, tension, and bracing.

## Infrastructure

- Timber storage: Covered, ventilated area for seasoning (air drying 1 year per 25 mm thickness).
- Lime pit: For slaking quicklime and storing lime putty.
- Scaffold timber: 75-100 mm diameter poles for temporary works.


## Bill of Materials

| Material | Quantity per 100 m² Floor Area | Source | Alternatives |
|----------|-------------------------------|--------|-------------|
| Structural timber (framing) | 8-15 m³ | [Forestry](../plants/structural-plants.md) — oak or pine | Steel sections (see [Iron & Steel](../metals/iron-steel.md)) |
| Lime mortar | 3-8 m³ | [Lime Production](../ceramics/lime.md) — quicklime + sand | Clay mortar (weaker, water-soluble) |
| Stone (rubble) | 15-40 m³ | [Mining](../mining/index.md) — quarry or field stone | Fired brick (see below) |
| Fired brick | 3,000-8,000 bricks | [Ceramics](../ceramics/index.md) — clay fired at 900-1100°C | Sun-dried mud brick (1-2 MPa, dry climates only) |
| Roofing slate or tile | 1,500-3,000 pieces | [Mining](../mining/index.md) or [Ceramics](../ceramics/index.md) | Thatch (temporary, fire risk), metal sheet |
| Nails and hardware | 20-50 kg | [Iron & Steel](../metals/iron-steel.md) | Timber pegs (19-25 mm oak or ash) |
| Rope (scaffolding/hoisting) | 100-300 m | [Rope Making](../textiles/rope-making.md) | Withies (flexible willow/hazel branches) |


## Process Description

## Timber Framing

**Principle**: Timber carries both compression and tension loads. Properly joined frames span 6-12 m and support multi-story structures for centuries. The joinery (not iron fasteners) provides structural integrity.

**Prerequisites**:
- Seasoned timber: moisture content 12-18%. Air-dry 1 year per 25 mm thickness. Softwood seasons in 6-12 months for 50 mm boards; hardwood requires 2-3 years.
- [Basic hand tools](../foundations/tools-basic.md): framing chisel (25-50 mm), mallet, hand saw, try square, plumb bob.
- Timber specifications: oak heartwood preferred for structural members (bending strength 50-70 MPa). Knots <1/3 beam width. No end splits >100 mm.

**Materials**:
- Oak beams: 150 × 200 mm to 250 × 300 mm for main frames, ±5 mm tolerance on cross-section.
- Oak pegs: 19-25 mm diameter, 200-300 mm length, riven (split, not sawn) for maximum strength.
- Floor joists: 50 × 200 mm to 75 × 250 mm, at 400-600 mm spacing.

**Construction**:

1. Select and grade timber. Reject any beam with knots >1/3 width, splits >1/3 depth, or insect damage. Measure moisture content with probe: target 12-18%. If above 18%, sticker-stack and wait.

2. Layout joints on beam ends using square and scriber. Mortise dimensions: 1/3 beam width deep, width matching tenon ±0.5 mm. Tenon: 1/3 beam width long, thickness 1/3 beam width.

3. Cut mortises with framing chisel and mallet. Work from both faces to meet in center. Clean sidewalls with chisel — bearing surface must be flat within 1 mm over the mortise depth.

4. Cut tenons with back saw and shoulder plane. Tenon width: beam width minus 2 × shoulder (shoulder = 1/6 beam width each side). Tenon length: 1.3 × mortise depth for through-tenon.

5. Drill peg holes offset 3-5 mm toward tenon shoulder (draw-bore technique). This pulls the joint tight when peg is driven. Peg diameter: 19-25 mm. Peg hole diameter: 1 mm undersized for interference fit.

6. Assemble frame on level ground (sill beams first, then posts, then beams). Drive pegs with mallet. Check each joint: no gap >1 mm at shoulder. If gap exists, draw-bore offset was insufficient — redrill with greater offset.

7. Erect frame using block-and-tackle hoisting (see [Rope Making](../textiles/rope-making.md) for rope specs). Brace each post with temporary diagonal poles (75 mm diameter, 3-4 m length) before releasing hoist.

8. Install knee braces at every post-to-beam connection: minimum 1.2 m length, 45° angle, mortise-tenon joints at both ends. These resist lateral loads (wind, racking). Without bracing, frames collapse sideways.

**Calibration / Verification**:
- Check plumb of every post with plumb bob: deviation ≤6 mm per 3 m height.
- Check level of every beam with spirit level or water level: deviation ≤3 mm over 3 m span.
- Measure brace angles: 40-50° acceptable range.
- Load test floor joists with 2 kN/m² distributed load (stacked sandbags or water containers). Maximum deflection must not exceed L/360 (where L = span in mm). For a 4 m span: ≤11 mm deflection.

**Expected Performance**:
- Beam span-to-depth ratio: 15:1 to 20:1 for floor joists (deflection-controlled), 10:1 to 15:1 for heavily loaded beams.
- Post slenderness ratio (height/least-dimension): ≤50 for main posts, ≤30 for heavily loaded columns.
- Deflection limit: L/360 for floors, L/240 for roofs.
- Properly framed structure lifespan: 200-500+ years if kept dry and protected from insects.

**Applications**: Houses, barns, workshops, bridges, scaffolding, hoisting frames.

**Strengths**:
- Renewable resource — timber regrows in 25-80 years depending on species
- Workable with hand tools — no industrial base required beyond axes and saws
- Provides both compression and tension capacity — versatile structural material
- Lightweight relative to strength — easy to transport and erect without heavy machinery

**Weaknesses**:
- Combustible — requires fire protection measures (plaster, metal cladding, chemical treatment)
- Subject to rot and insect damage — must be kept dry; ground contact reduces lifespan to 5-15 years
- Anisotropic — strength varies by grain direction; perpendicular-to-grain compression only 3-5 MPa
- Shrinkage during seasoning — green timber shrinks 3-6% radially, joints loosen if assembled before drying

## Stone Masonry

**Principle**: Stone excels in compression (20-250 MPa) but has negligible tensile strength. Masonry structures exploit this by keeping all structural elements in compression through geometry (arches, vaults, thick walls) and massive weight.

**Prerequisites**:
- [Stone source](../mining/index.md): Quarry or field stone. Limestone (30-80 MPa compressive strength) and sandstone (20-60 MPa) are workable; granite (100-200 MPa) is harder but stronger.
- [Lime mortar](../ceramics/lime.md): Quicklime slaked to lime putty, mixed with sand at 1:2.5 to 1:3 ratio by volume.
- Stone dressing tools: Chisel, hammer, square, plumb bob, string line.

**Materials**:
- Ashlar (dressed stone): Blocks 150-300 mm course height, length 200-600 mm, width = wall thickness. Joint thickness: 3-6 mm for ashlar, 10-25 mm for rubble.
- Rubble stone: Angular fragments 100-300 mm, sorted roughly by size.
- Lime mortar: Mix 1:2.5 lime putty:sand by volume. Compressive strength: 2-5 MPa (carbonation cure, 4-12 weeks to full strength).
- Through-stones: Full-width stones every 1.5 m vertically, every 2 m horizontally — prevent wall delamination.

**Construction**:

1. Excavate foundation trench to subsoil (minimum 600 mm deep, 300 mm below frost line in cold climates). Width: wall thickness + 200 mm each side. Fill bottom 150 mm with compacted gravel.

2. Lay first course (foundation course) of largest, flattest stones. Bed each stone in mortar with full bearing — no rocking. Level within ±5 mm per stone. Course height: 200-400 mm.

3. For ashlar masonry: dress each stone to ±3 mm on all faces. Check with square — all corners must be 90° ±2°. Joint thickness: 3-6 mm, filled flush with mortar.

4. For rubble masonry: select stones to fit together with minimal voids. Fill all gaps with mortar and small stone fragments (spalls). Maximum void content: 25% of wall volume. Course height: irregular but maintain roughly horizontal bedding.

5. Lay each subsequent course with staggered vertical joints (bond pattern). Overlap between courses: ≥100 mm or ≥1/3 stone length. Break joints ensure structural continuity.

6. Install through-stones at 1.5 m vertical intervals, extending full wall width. These prevent the wall from splitting into inner and outer leaves.

7. Point all joints (tool mortar surface with pointing iron) while mortar is still workable. Flush joints for weather resistance; raked joints for aesthetic effect (interior only — raked joints trap water externally).

8. Cure mortar by keeping walls damp for 7 days in hot/dry weather. Cover with damp sacking. Lime mortar gains strength over months through carbonation — initial set in 24-48 hours, structural strength in 4-12 weeks.

**Calibration / Verification**:
- Plumb check every 1 m of height: deviation ≤10 mm per 3 m.
- Level check each course with string line: deviation ≤5 mm per 3 m run.
- Bond pattern check: verify overlap ≥1/3 stone length at every third joint.
- Tap test: strike each stone with hammer — hollow ring indicates void beneath (lift and relay). Solid ring indicates full bearing.

**Expected Performance**:
- Wall compressive strength: 30-40% of individual stone strength (mortar joint weakness).
- Load-bearing wall: minimum 150 mm per story height (single-story: 300 mm minimum for unreinforced rubble, 200 mm for ashlar).
- Fire resistance: inherent — stone and mortar are non-combustible. 4+ hour rating for 200 mm wall.
- Lifespan: 500-2000+ years for stone masonry in dry conditions with adequate mortar.

**Applications**: Load-bearing walls, foundations, retaining walls, fortifications, bridge abutments.

**Strengths**:
- Non-combustible — inherent fire resistance, no treatment required
- Massive thermal mass — moderates interior temperature swings, reduces heating and cooling loads
- Extremely durable — stone walls last centuries to millennia with minimal maintenance
- High compressive strength — supports heavy vertical loads (multi-story buildings, vaulted ceilings)

**Weaknesses**:
- Labor-intensive — dressing ashlar stone produces 2-5 finished blocks per mason per day
- No tensile capacity — walls cannot span openings without arches or lintels
- Heavy — requires massive foundations; settlement risk on weak soils
- Skilled labor required — stone masonry quality depends entirely on craftsman skill

## Brick Masonry

**Principle**: Fired clay brick provides consistent, modular building units with predictable strength (10-50 MPa compressive). The standardized size enables rapid construction compared to stone, while fired clay offers weather resistance superior to timber or mud brick.

**Prerequisites**:
- [Clay](../ceramics/index.md): Suitable clay body with plasticity index >10, free of organic matter and excessive lime nodules.
- Kiln firing capability: Temperature 900-1100°C for 12-48 hours. See [Ceramics](../ceramics/index.md) for kiln specifications.
- Mortar: Lime mortar or [cement mortar](../chemistry/cement.md). Mix: 1:3 to 1:4 cement:sand or 1:2.5 lime:sand by volume.

**Materials**:
- Fired clay brick: Standard size 215 × 102.5 × 65 mm (UK) or 230 × 110 × 65 mm (metric). Compressive strength: 10-20 MPa (common brick), 50+ MPa (engineering brick).
- Mortar: 1:1:6 (cement:lime:sand) for general work, 1:0.25:3 for high-strength. Joint thickness: 10 mm ±2 mm.
- Wall ties: Galvanized iron wire ties, 3 mm diameter, 200 mm long, at 450 mm vertical × 900 mm horizontal spacing for cavity walls.

**Construction**:

1. Sort bricks by color and size. Reject cracked, warped, or underfired bricks (salmon-colored, crumbly). Batch similar-size bricks together for consistent joints.

2. Mix mortar to stiff-but-workable consistency. Test: hold a scoop of mortar inverted on a trowel — it should cling without sliding off for 5+ seconds. Use within 2 hours of mixing (lime mortar: within 4 hours).

3. Lay corner leads first (build corners 4-6 courses ahead of infill). This establishes level and plumb for the wall run. Check each corner lead course with spirit level in both directions.

4. Spread mortar bed 10 mm thick on previous course. Furrow with trowel point (creates suction for brick placement). Apply mortar to brick end (head joint) before placing.

5. Place brick, press down to 10 mm joint thickness. Tap with trowel handle to align with string line. Check level. Trim excess mortar with trowel.

6. Maintain bond pattern: English bond (alternating stretcher and header courses) or Flemish bond (alternating stretchers and headers within each course). Minimum overlap: 1/4 brick length (56 mm minimum).

7. Tool joints when mortar is thumbprint-hard (pressed with thumb leaves slight impression): press mortar firmly with jointing iron for weather-resistant concave or flush profile.

8. Build in wall openings (doors, windows) with temporary timber frames. Install lintels (steel angle or reinforced concrete) over openings. Lintel bearing: minimum 150 mm each side.

**Calibration / Verification**:
- Level: ±6 mm per 3 m run, ±12 mm per story height.
- Plumb: ±6 mm per 3 m height.
- Joint thickness: 10 mm ±3 mm (measure 10 joints, average must be 10 ±1 mm).
- Brick compressive test: sample 5 bricks per 10,000, crush in test rig. Minimum average strength: 10 MPa for load-bearing walls.

**Expected Performance**:
- Compressive strength of brickwork: 30-40% of individual brick strength (e.g., 20 MPa bricks yield 6-8 MPa brickwork in 1:4 mortar).
- Wall thickness: one brick (215-230 mm) for single-story load-bearing; two bricks for two-story.
- Fire resistance: 2 hours for 100 mm solid brick, 4+ hours for 200 mm.
- Waterproofing: brickwork absorbs water — requires external rendering or weatherproofing in exposed locations.

**Applications**: Load-bearing walls, infill panels, partition walls, chimneys, garden walls, foundations above grade.

**Strengths**:
- Modular and standardized — enables rapid, predictable construction
- Consistent quality — manufactured units have predictable structural properties unlike natural stone
- Fire-resistant — non-combustible, maintains structural integrity in fire
- Good moisture regulation — fired clay absorbs and releases moisture, moderating interior humidity

**Weaknesses**:
- Requires kiln firing — energy-intensive (900-1100°C for 12-48 hours per kiln load)
- Limited tensile strength — same constraint as stone masonry, requires arches or lintels for openings
- Porous — absorbs water, requires external weatherproofing or rendering in exposed conditions
- Mortar joint is the weak point — wall strength is 30-40% of brick unit strength

## Roofing Systems

**Principle**: Roofing must shed water, support its own weight plus snow and wind loads, and resist lateral spreading forces that push walls apart. Truss geometry converts loads into axial forces in individual members, enabling timber to span 5-20 m.

**Prerequisites**:
- Seasoned timber for trusses (see Timber Framing above for specs).
- [Rope](../textiles/rope-making.md) or metal strapping for temporary bracing.
- Roofing material: slate, clay tile, or metal sheet.
- [Basic hand tools](../foundations/tools-basic.md).

**Materials**:
- Truss timber: 100 × 150 mm to 150 × 250 mm for rafters and tie beams, ±3 mm tolerance.
- King-post: 100 × 100 mm, length = rise minus 100 mm.
- Nails or pegs: 100 mm wire nails or 19 mm oak pegs.
- Slate: 4-8 mm thick, 200-400 mm × 100-250 mm pieces. Weight: 0.5 kN/m².
- Clay tile: Interlocking or plain, 300 × 200 mm typical. Weight: 0.6 kN/m². Fired at 900-1000°C.
- Metal sheet: 0.5 mm galvanized steel, corrugated 75 mm depth. Weight: 0.15 kN/m².

**Construction** (King-Post Truss):

1. Cut rafters to calculated length with plumb cuts at peak and birdsmouth cuts at wall plate. Rafter angle: 30-45° (steeper sheds snow, uses more timber). Tolerance: ±3 mm on all cuts.

2. Cut tie beam to span length ±3 mm. Mark king-post location at exact midpoint.

3. Cut king-post to calculated height (rise minus tie beam depth minus rafter depth at peak). Square both ends within ±1 mm.

4. Assemble truss flat on ground. Join rafters at peak with half-lap joint secured by bolt or peg. Connect king-post to rafters with mortise-tenon or notched joint. Connect rafter feet to tie beam with birdsmouth joint.

5. Install trusses at 3-5 m spacing for residential, 6-10 m for industrial buildings. Hoist with block and tackle. Set on wall plate with birdsmouth bearing full width of wall plate.

6. Install purlins (horizontal beams) between trusses at 1.0-1.5 m spacing, spanning between trusses. Purlin size: 50 × 150 mm minimum, fixed with notched joints to rafters.

7. Install roof decking (25 mm boards or 12 mm plywood) or battens (25 × 50 mm at spacing per roofing material type — 100 mm for slate, 300 mm for metal sheet).

8. Install roofing material from bottom eave to top ridge, overlapping uphill. Slate: minimum 75 mm headlap, nailed with 2 copper or galvanized nails per slate. Metal sheet: overlap 1.5 corrugations, screw at every second corrugation at overlaps.

**Calibration / Verification**:
- Rafter spacing: ±10 mm tolerance.
- Truss plumb: ±5 mm per 3 m height.
- Roof pitch: measure angle with bevel gauge, ±2° of design.
- Slate headlap: measure overlap on 10 slates, minimum 75 mm all.
- Load test: pile 1.5 kN/m² (sandbags) on completed roof. Maximum deflection: L/240 of rafter span.

**Expected Performance**:
- Total roof design load: 1.5-4.5 kN/m² (dead load 0.5-1.2, snow 0.5-2.5, wind uplift 0.5-1.5).
- Truss spans: king-post 5-9 m, queen-post 8-14 m, hammer-beam 12-20 m.
- Roof lifespan: slate 100+ years, clay tile 50+ years, metal sheet 25-50 years, thatch 10-20 years.

**Applications**: All buildings — residential, commercial, industrial, agricultural.

**Strengths**:
- Truss geometry enables long spans without interior columns — open floor plans
- Multiple roofing materials available at different tech levels — adaptable to available resources
- Roof slope sheds water and snow — primary weather protection for structure below
- Modular construction — trusses prefabricated on ground, erected rapidly

**Weaknesses**:
- Wind uplift is a critical failure mode — lightweight roofing (metal sheet) can peel off if not adequately fastened
- Snow loading can cause progressive collapse — flat or low-pitch roofs vulnerable in heavy snow climates
- Roof geometry creates lateral spreading forces — tie beams or rigid connections mandatory to prevent wall bow-out
- Working at height during construction — fall hazard for carpenters and roofers


## Quantitative Parameters

## Structural Timber Properties

| Property | Softwood (Pine) | Hardwood (Oak) | Notes |
|----------|:---------------:|:--------------:|-------|
| Density | 450-550 kg/m³ | 600-750 kg/m³ | Oak ~30% heavier |
| Bending strength | 30-45 MPa | 50-70 MPa | Allowable ~1/3 of ultimate |
| Compression ∥ grain | 25-35 MPa | 40-55 MPa | Along grain |
| Compression ⊥ grain | 3-5 MPa | 6-10 MPa | Across grain — much weaker |
| Tension ∥ grain | 50-80 MPa | 80-120 MPa | Knots reduce significantly |
| Elastic modulus | 9-12 GPa | 10-14 GPa | Stiffness |
| Moisture content (green) | 30-50% | 30-50% | Must season before structural use |
| Moisture content (seasoned) | 12-18% | 12-18% | Air-dry 1 year per 25 mm thickness |
| Shrinkage (green to dry) | 3-5% radial | 4-6% radial | Tangential shrinkage ~2× radial |

## Stone Properties

| Stone | Compressive Strength (MPa) | Workability | Best Use |
|-------|:-------------------------:|:-----------:|----------|
| Granite | 100-200 | Very hard | Foundations, bridge abutments |
| Limestone | 30-80 | Moderate | Wall construction, carving |
| Sandstone | 20-60 | Easy | Wall construction, decorative carving |
| Slate | 70-150 | Splits easily | Roofing tiles, flooring |

## Roof Loading

| Load Type | Typical Value (kN/m²) | Notes |
|-----------|:---------------------:|-------|
| Dead load (roofing) | 0.3-0.7 | Slate: 0.5, Clay tile: 0.6, Metal sheet: 0.15 |
| Dead load (structure) | 0.3-0.5 | Timber framing + decking |
| Snow load | 0.5-2.5 | Depends on climate; steep roofs shed snow |
| Wind uplift | 0.5-1.5 | Critical for lightweight roofing |
| **Total design load** | **1.5-4.5** | Dead + live with safety factor |

## Brick Properties

| Parameter | Common Brick | Engineering Brick |
|-----------|:-----------:|:-----------------:|
| Compressive strength | 10-20 MPa | 50+ MPa |
| Water absorption | 15-25% | <7% |
| Frost resistance | Moderate | Excellent |
| firing temperature | 900-1050°C | 1050-1150°C |
| Color | Red/orange/buff | Dark red/blue |


## Scaling Notes

- **Single building (50-100 m² floor area)**: 2-4 workers, 1-3 months construction. Materials: 5-10 m³ timber, 10-30 m³ stone or 3000-8000 bricks, 2-5 m³ mortar. Hand tools only.

- **Village construction (20-50 buildings)**: 10-20 workers, 2-5 years total construction time. Requires organized timber seasoning (start 1-2 years before construction), lime mortar production, and brick kiln operation. Coordinate through [division of labor](../economics-organization/division-of-labor.md).

- **Industrial building (500-2000 m² floor area)**: Requires steel framing (see [Iron & Steel](../metals/iron-steel.md)) for long spans. See [Industrial Buildings](./industrial-buildings.md) for specifications.

- **Scaling timber production**: A mature oak forest yields 3-5 m³/ha/year sustainable harvest. A 100 m² timber-framed building requires 8-15 m³ — equivalent to 2-5 hectares of mature forest for one year.

- **Scaling brick production**: A single clamp kiln fires 5,000-20,000 bricks per batch (1-2 weeks cycle). A 100 m² brick house requires 3,000-8,000 bricks — one kiln firing. Industrial-scale continuous kilns (Hoffman kiln) produce 20,000-50,000 bricks/day.


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Timber frame racking (leaning sideways) | Missing or inadequate knee braces | Install 1.2 m minimum knee braces at every post-to-beam connection at 45° angle |
| Mortar joints eroding rapidly | Weak mortar (excess sand), acidic rain, freeze-thaw | Increase lime content to 1:2 ratio; repoint with hydraulic lime mortar; ensure wall caps shed water |
| Brick wall cracking at corners | Differential settlement, missing toothing at junctions | Ensure foundation is level and on uniform soil; build corners simultaneously with walls (tooth joints) |
| Roof leaking at valleys and penetrations | Inadequate flashing, broken slates/tiles, insufficient overlap | Install [copper flashing](../metals/iron-steel.md) (0.5-0.7 mm) at all valleys and penetrations; replace broken units; verify headlap ≥75 mm |
| Timber rot at ground contact level | Soil moisture, no damp-proof course | Install slate or bitumen damp-proof course 150 mm above ground level; replace rotted timber with stone base |
| Excessive floor deflection (springy floor) | Joists undersized, excessive spacing | Reduce joist spacing to 400 mm; increase joist depth (rule of thumb: span mm / 15 = depth mm); add mid-span bridging |
| Roof sagging at midspan | Tie beam failure (tension split), rafter undersized | Replace tie beam with larger section; add collar tie at mid-height of rafters; consider queen-post truss for longer spans |
| Masonry wall bulging outward | Lateral load (earth pressure, wind), inadequate wall thickness | Increase wall thickness to minimum L/20 where L = wall height; add buttresses at 2-3 m spacing; install wall ties for cavity walls |


## Safety

- **Falls from scaffolding and roof work**: The primary construction hazard. Scaffold planks must be secured against wind lift. Workers on roof framing use safety lines tied to structural members (not scaffolding). Historical fatality rate: 1-3 deaths per major building project from falls. Minimum: toe boards (150 mm) and guardrails (1.0 m) on all scaffolding at height >2 m.

- **Stone and brick falling from wall tops**: Material hoisted to wall-top working level can fall on workers below. Establish exclusion zones (3 m minimum) below active hoisting areas. Hard hats mandatory within 10 m of active masonry work. A 5 kg brick falling 6 m delivers 300 J impact — lethal.

- **Lime mortar burns**: Quicklime (CaO) reacts exothermically with moisture in skin, causing chemical burns. Wear leather gloves when handling quicklime and lime putty. Slaking quicklime produces temperatures exceeding 100°C — add lime to water (never water to lime) to control reaction rate. Eye protection mandatory during slaking.

- **Timber cutting injuries**: Hand saws and axes cause lacerations. Chisel work sends chips flying — eye protection required. Saw injury rate: approximately 1 serious laceration per 500 worker-hours of saw operation.

- **Roof collapse during construction**: Incomplete trusses and unbraced framing are unstable. Never remove temporary bracing until all permanent connections are complete. Do not stack materials on partially completed roof framing — it was not designed for construction loads.

- **Scaffold collapse**: Scaffold capacity: 1.2 kN/m² (light duty — workers and hand tools only). Never use scaffolding for material storage. Inspect all rope lashings daily — replace any rope showing wear, fraying, or UV degradation. Maximum scaffold height without intermediate tie-in to structure: 6 m.


## Quality Control

- **Timber moisture content**: Test with probe-type moisture meter before assembly. Accept: 12-18% for structural use. Reject: >20% (risk of shrinkage and joint loosening). Test 10% of timbers per delivery.

- **Mortar testing**: Make 50 mm cube test samples from each mortar batch. Crush at 28 days. Accept: ≥2 MPa for lime mortar, ≥5 MPa for cement mortar. Discard any batch that fails.

- **Brick quality**: Visual inspection for cracks, warpage, underfiring. Ring test: strike brick with hammer — clear ring indicates good firing, dull thud indicates underfired (reject). Water absorption test: soak 24 hours, weight gain <20% for exterior brick.

- **Wall plumb and level**: Check every 1 m of height. Tolerance: ±10 mm plumb per 3 m, ±6 mm level per 3 m. Out-of-tolerance walls must be corrected before proceeding.

- **Roof watertightness**: Flood-test flat roofs with 25 mm standing water for 24 hours. Sloped roofs: inspect after first heavy rain. No leaks acceptable at completion.


## Variations and Alternatives

| Building Method | Material | Structural Capacity | Cost (Labor) | Best For |
|----------------|----------|--------------------|-------------|---------|
| Timber frame | Oak/pine | Medium (beams: 50-70 MPa bending) | Low-moderate | Houses, barns, workshops; rapid construction |
| Stone masonry (ashlar) | Limestone/sandstone | High (compression: 30-80 MPa) | Very high | Permanent structures, fortifications, churches |
| Stone masonry (rubble) | Field stone | Moderate (5-15 MPa brickwork equiv.) | Moderate | Foundation walls, retaining walls, agricultural buildings |
| Fired brick | Clay | Moderate (10-20 MPa brickwork) | Moderate | Urban construction, chimneys, repeatable modular buildings |
| Mud brick (adobe) | Clay + straw | Low (1-2 MPa) | Low | Dry climates only; temporary or low-cost construction |
| Cob (earth + straw) | Subsoil + straw | Low (1-3 MPa) | Low | Thick walls (≥400 mm); dry climates; same limitations as adobe |

## Material Selection Decision Criteria

- **Use timber when**: spans >3 m, rapid construction needed, tensile capacity required, weight must be minimized.
- **Use stone when**: permanence is paramount, fire resistance required, compressive loads dominate, material is locally abundant.
- **Use brick when**: standardized modular construction is desired, quality control is important, intermediate cost between timber and stone.
- **Use mud brick only when**: climate is dry (<500 mm annual rainfall), no kiln firing is available, temporary construction is acceptable.


## See Also

- [Lime Production](../ceramics/lime.md) — Lime mortar for masonry construction
- [Cement & Concrete](../chemistry/cement.md) — Portland cement and concrete for industrial construction
- [Stone & Wood Tools](../foundations/index.md) — Basic toolmaking for construction work
- [Rope Making](../textiles/rope-making.md) — Rope for hoisting, scaffolding, and lashing
- [Iron & Steel](../metals/iron-steel.md) — Structural steel, nails, and hardware
- [Structural Engineering](./structural-engineering.md) — Beam design, column design, and foundation theory
- [Industrial Buildings](./industrial-buildings.md) — Heavy-duty construction specifications



[← Back to Construction](index.md)
