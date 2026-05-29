# Industrial Buildings & Heavy Foundations

> **Node ID**: construction.industrial-buildings
> **Domain**: [Construction](./index.md)
> **Dependencies**: [`construction.building-materials`](./building-materials.md), [`energy.electricity`](../energy/electricity.md)
> **Enables**: [`machine-tools.machining`](../machine-tools/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 15-40
> **Outputs**: industrial_facilities, machine_foundations, vibration_isolation, crane_runways, factory_floors
> **Critical**: Yes — precision manufacturing requires vibration-isolated foundations; heavy industry requires crane runways and reinforced floors



Industrial buildings differ fundamentally from residential construction. They must support heavy point loads from machinery (5-50 tonnes per machine), resist dynamic forces from forging hammers and stamping presses (5-50 kJ per blow), provide clear spans of 15-30 m for production lines, and accommodate overhead cranes moving 5-50 tonnes. The building is not just shelter — it is an integral part of the production system.

Every machine tool, forge hammer, steam engine, and generator requires a foundation designed to carry its weight and resist its dynamic forces. A lathe with 0.01 mm tolerance cannot sit on a floor that deflects 0.1 mm under a passing forklift. A forge hammer delivering 50 kJ blows will destroy its own foundation and the surrounding building if not properly isolated.

This capability depends on [building materials](./building-materials.md) for basic construction, [structural engineering](./structural-engineering.md) for design calculations, [electricity](../energy/electricity.md) for power distribution, and [cement and concrete](../chemistry/cement.md) for reinforced concrete structures.


## Prerequisites

## Materials

- **[Structural steel](../metals/iron-steel.md)**: HEB 200-400 columns, IPE 300-600 beams. Grade S235 or S355.
- **[Cement and concrete](../chemistry/cement.md)**: Minimum C25/30 for floors, C30/37 for machine foundations. Coarse aggregate 10-20 mm, clean sand, potable water.
- **[Reinforcing steel](../metals/iron-steel.md)**: Rebar 8-32 mm diameter, grade 400-500 MPa yield. Deformed bars for bond.
- **Crushed stone subbase**: 150-300 mm compacted layer, 20-40 mm aggregate.

## Tools and Equipment

- [Concrete mixing equipment](../chemistry/cement.md): Batch mixer or continuous mixer.
- [Steel erection tools](../metals/iron-steel.md): Cranes, bolt torque wrenches, welding equipment.
- Surveying instruments: Theodolite or level for foundation layout (±5 mm tolerance over 30 m).
- Concrete vibrator: For compacting poured concrete (eliminates voids >5 mm).

## Knowledge

- **Reinforced concrete design**: Understanding of rebar placement, cover requirements, and load paths.
- **Vibration isolation theory**: Natural frequency, damping, transmissibility calculations.
- **Machine foundation design**: Mass ratio, bearing pressure, dynamic load factors.

## Infrastructure

- Road access for concrete delivery trucks and steel delivery vehicles.
- Power supply for concrete mixers, vibrators, and cranes.
- Water supply for concrete mixing and curing.


## Bill of Materials

| Material | Quantity per 1000 m² Factory | Source | Alternatives |
|----------|------------------------------|--------|-------------|
| Structural steel (frame) | 15-40 tonnes | [Iron & Steel](../metals/iron-steel.md) | Reinforced concrete frame (heavier, fire-resistant) |
| Concrete (floor slab, 200 mm) | 200 m³ | [Cement](../chemistry/cement.md) | Timber floor on sleepers (light duty only) |
| Rebar (floor and foundations) | 8-20 tonnes | [Iron & Steel](../metals/iron-steel.md) | Steel fiber reinforcement (30-50 kg/m³) |
| Crushed stone subbase | 150-300 m³ | [Mining](../mining/index.md) | Compacted earth (settles, uneven support) |
| Corrugated metal roofing | 800-1200 m² | [Metals](../metals/index.md) | Asbestos-cement sheet (health hazard) |
| Crane rail (QU70-QU120) | 100-200 m | [Iron & Steel](../metals/iron-steel.md) | Standard railway rail (lower capacity) |
| Waterproofing membrane | 500-1000 m² | [Chemistry](../chemistry/index.md) | Bituminous coating (shorter lifespan) |
| Expansion joint filler | 50-100 m | [Polymers](../polymers/index.md) or cork | Bitumen-impregnated fiberboard |


## Process Description

## 4.1 Steel-Frame Factory Construction

**Principle**: Steel columns at regular spacing support roof trusses spanning 15-30 m, providing column-free interior space for production lines. The steel frame carries all vertical and lateral loads. Cladding provides weather enclosure only — it is not structural.

**Prerequisites**:
- [Structural steel](../metals/iron-steel.md): HEB 200-400 columns, IPE 300-600 beams. Minimum grade S235 (yield strength 235 MPa).
- [Cement and concrete](../chemistry/cement.md): For column foundations and floor slab. Minimum C25/30.
- Crane for erection: Minimum 5-tonne capacity, 10 m lift height.

**Materials**:
- Columns: HEB 200-400, length 6-12 m (clear height). Steel grade S235 or S355. Base plates 300-500 mm square, 20-30 mm thick, with 4-8 anchor bolts per column.
- Roof trusses: IPE or welded built-up sections. Span: 15-30 m. Weight: 30-80 kg/m of truss length.
- Purlins: Z-profile or IPE 100-160 at 1.5-2.5 m spacing spanning between trusses.
- Bolts: Grade 8.8 high-strength bolts, 16-24 mm diameter, for all structural connections.
- Foundation concrete: C25/30 minimum. Pad footings: 1.5-3.0 m square, 0.5-1.5 m deep.

**Construction**:

1. Survey and mark column grid lines. Column spacing: 6-10 m (bay width) × 18-30 m (bay length). Set reference benchmarks at building corners. Tolerance: ±5 mm on grid dimensions.

2. Excavate pad footings for each column. Dimensions: 1.5-3.0 m square × 0.5-1.5 m deep (sized by column load ÷ soil bearing capacity — see [Structural Engineering](./structural-engineering.md)). Compact subgrade to 95% standard Proctor density.

3. Cast concrete pad footings. Place anchor bolt template (plywood jig with pre-drilled holes matching column base plate) before pouring. Anchor bolts: 4-8 per column, 20-30 mm diameter, embedded 400-600 mm with hook or plate anchor at bottom. Bolt position tolerance: ±3 mm. Concrete: C25/30 minimum. Cure 7 days before loading.

4. Erect steel columns. Bolt base plate to anchor bolts with leveling nuts. Plumb each column: ±5 mm per 6 m height. Shim under base plate for level (maximum 10 mm shims — grout void after plumbing). Tighten anchor bolts to 50% of rated torque initially; full torque after grouting.

5. Erect roof trusses. Hoist with crane, bolt to column caps. Install temporary bracing (steel cable or angle iron) diagonally between columns before releasing crane. Truss alignment: ±10 mm of theoretical grid position.

6. Install permanent lateral bracing: X-bracing in roof plane and wall plane at every 4th-6th bay. Bracing members: steel angle 50 × 50 × 5 mm minimum, bolted or welded to columns and trusses.

7. Install purlins at 1.5-2.5 m spacing, spanning between trusses. Bolt to truss top chords with 2 × 12 mm bolts per connection. Sag rods (12 mm threaded rod) at mid-span and third-points prevent purlin rollover.

8. Install roof cladding (corrugated metal sheet, 0.5 mm steel) from eave to ridge, overlapping 1.5 corrugations horizontally and 150 mm vertically. Fasten with self-tapping screws at every second corrugation at overlaps. Minimum roof pitch: 5° for corrugated, 10° for standing seam.

**Calibration / Verification**:
- Column plumb: ±5 mm per 6 m height (check with theodolite from two directions).
- Truss alignment: ±10 mm of theoretical position (check with string line and tape).
- Bolt torque: Verify 10% of bolts with torque wrench — all must be within ±10% of specified torque (grade 8.8, 20 mm: 450 Nm).
- Roof watertightness: Inspect after first rainfall — no leaks at penetrations, flashings, or overlaps.

**Expected Performance**:
- Clear span: 15-30 m column-free space.
- Clear height: 6-12 m (accommodates crane + tallest machine).
- Design life: 50-100 years with maintenance (repaint every 15-25 years to prevent corrosion).
- Load capacity: Floor 10-50 kN/m², crane 5-50 tonnes, snow 0.5-2.5 kN/m², wind per local code.

**Applications**: Machine shops, foundries, assembly plants, warehouses, steel fabrication shops.

**Strengths**:
- Fast erection — bolted connections, prefabricated components, 4-8 weeks for a 2000 m² building
- Clear spans without interior columns — flexible floor layout for production lines
- Easily modified or expanded — add bays by extending frame and cladding
- High strength-to-weight ratio — lighter foundations than concrete equivalent

**Weaknesses**:
- Corrosion — steel must be painted or galvanized; repaint every 15-25 years; corrosion in 5-10 years if untreated in marine/industrial atmosphere
- Fire vulnerability — steel loses 50% strength at 600°C; requires intumescent coating for 1-2 hour fire rating
- Thermal conductivity — steel frames conduct heat, creating thermal bridges that increase heating/cooling costs
- Skilled erection required — crane operation, bolt tightening, welding must meet specifications

## 4.2 Machine Foundation Construction

**Principle**: Machine foundations isolate dynamic equipment vibrations from the building structure and prevent excessive settlement under static and dynamic loads. Foundation mass (3-10× machine mass) absorbs vibration energy. Proper isolation prevents a forge hammer from cracking its own foundation and the adjacent precision grinder from producing out-of-tolerance parts.

**Prerequisites**:
- [Reinforced concrete](../chemistry/cement.md): Minimum C25/30 for general, C30/37 for heavy dynamic loads.
- [Rebar](../metals/iron-steel.md): 12-25 mm diameter deformed bars.
- Vibration isolation materials: Neoprene pads (5-15 Hz natural frequency) or steel spring isolators (1-5 Hz).
- Equipment specifications: Machine weight, operating speed (RPM), dynamic forces, anchor bolt pattern.

**Materials**:
- Concrete: C25/30 to C35/45 depending on equipment. Maximum aggregate 20 mm. Slump: 75-125 mm (workable but not watery). Water-cement ratio: ≤0.45 for low shrinkage.
- Reinforcement: 12-25 mm deformed rebar, grade 400-500 MPa. Typical: 20-25 mm bars at 150-200 mm spacing each way, top and bottom mats.
- Anchor bolts: 16-50 mm diameter, grade 4.6 or 8.8. Embedded depth: 30-40× bolt diameter. Hooked or plate-headed at bottom.
- Isolation material: Neoprene pads (50-100 mm thick, 5-15 Hz natural frequency) or steel springs (static deflection 25-100 mm, 1-5 Hz natural frequency).

**Construction** (Block Foundation for Lathe, 1-5 tonnes):

1. Calculate foundation dimensions. Mass ratio: foundation mass ≥ 3× machine mass for rotating equipment. Base area: sized for soil bearing pressure under combined static + dynamic loads (allowable bearing: soil capacity ÷ 1.5 safety factor). Depth: minimum 0.6× foundation width (to resist rocking).

2. Excavate foundation pit. Dimensions: machine footprint + 300 mm clearance each side for formwork. Depth: calculated foundation depth + 100 mm for blinding concrete. Subgrade: compacted to 95% Proctor density.

3. Cast blinding layer: 50-75 mm of lean concrete (1:3:6 mix, C15) to provide clean, level working surface for rebar placement.

4. Fabricate and place rebar cage. Bottom mat first (tension from bending), then vertical ties, then top mat (temperature/shrinkage). Bar spacing: 150-200 mm each way. Cover: 50 mm minimum to soil, 40 mm to forms. Tie all intersections with wire.

5. Install anchor bolt template (plywood jig matching machine base bolt pattern). Position anchor bolts through template, suspend from template with wire. Verify bolt positions against machine drawings: ±3 mm tolerance. Bolt projection above finished concrete: per machine manufacturer spec (typically 75-150 mm with threads).

6. Pour concrete in one continuous operation — no construction joints in the block. Vibrator consolidation: insert vibrator at 0.5 m spacing, withdraw slowly to avoid voids. Finish top surface level within ±3 mm using straightedge.

7. Cure concrete: keep moist for 7 days minimum (wet sacking or ponding). Do not load for 28 days (concrete reaches design strength). Grout pad under machine base: 50-75 mm non-shrink grout (1:1 cement:sand, water-cement ratio 0.30, 50+ MPa) for precise leveling.

**Calibration / Verification**:
- Foundation level: ±3 mm over the machine footprint area (check with precision level, 0.02 mm/m sensitivity).
- Anchor bolt positions: ±3 mm of theoretical (check with tape and square against machine drawing).
- Concrete strength: Crush test cylinders (3 per pour) at 28 days. Accept: ≥specified grade (C25/30 minimum).
- Vibration isolation performance: Start machine. Measure floor vibration velocity at 3 m distance with vibrometer. Accept: <0.5 mm/s for standard machine tools, <0.1 mm/s for precision grinders.

**Expected Performance**:
- Foundation settlement: <5 mm total for block foundations on competent soil (bearing capacity >150 kN/m²).
- Vibration isolation: 85-98% reduction at frequencies above 2× foundation natural frequency.
- Floor vibration limits: standard machine tool <0.5 mm/s, precision grinder <0.1 mm/s, optical inspection <0.05 mm/s.

**Applications**: Lathes, milling machines, grinders, forge hammers, stamping presses, generators, compressors.

**Strengths**:
- Isolates precision equipment from building vibrations — maintains machining tolerances
- Massive concrete absorbs dynamic energy — prevents vibration transmission to adjacent equipment
- Long service life — properly constructed foundation lasts 50-100+ years
- Simple design principle — mass ratio and bearing area calculations are straightforward

**Weaknesses**:
- Concrete curing time — 28 days to full strength delays machine installation
- Heavy — large foundations require excavation and concrete placement equipment
- Difficult to modify — once poured, foundation dimensions cannot be easily changed
- Soil-dependent — performance depends on soil bearing capacity; weak soils require piling or mat foundations

## 4.3 Industrial Floor Construction

**Principle**: Industrial floors carry concentrated point loads from machinery, forklifts (2-5 tonnes), and stored materials. Floor flatness directly affects equipment installation precision and forklift operation. Reinforced concrete slab-on-grade is the standard solution.

**Prerequisites**:
- [Concrete](../chemistry/cement.md): C25/35 to C35/45 for industrial floors.
- [Rebar or steel fiber](../metals/iron-steel.md): Welded wire mesh or deformed bars.
- Subgrade: Compacted to 95% Proctor density. Subbase: 150-300 mm crushed stone.
- Flatness requirements: FF 30-50 general industrial, FF 50-80 for precision areas.

**Materials**:
- Concrete: C25/35 minimum for general industrial, C35/45 for heavy-duty. Air-entrained 4-6% for freeze-thaw resistance. Maximum aggregate 20 mm. Slump: 75-100 mm.
- Reinforcement: Welded wire mesh (150 × 150 × 5 mm) or steel fiber (30-50 kg/m³). For heavy loads: 16-20 mm rebar at 200 mm spacing each way.
- Dry-shake hardener: Corundum or emery aggregate, 3-5 kg/m², floated into wet surface for abrasion resistance.
- Curing compound: Liquid membrane-forming compound applied immediately after finishing.

**Construction**:

1. Prepare subgrade: strip topsoil, compact subgrade to 95% Proctor density. Place subbase: 150-300 mm crushed stone (20-40 mm), compacted in 75 mm lifts.

2. Install formwork (steel or timber) at slab perimeter and at control joint locations. Form height: slab thickness (150-300 mm). Level forms within ±3 mm over 3 m using laser level.

3. Place reinforcement on chairs (plastic or concrete supports, 50 mm height) to maintain position during concrete placement. Overlap mesh 300 mm at splices. Rebar cover: 50 mm bottom, 40 mm top.

4. Place concrete: discharge directly from mixer truck or pump. Spread with rakes and shovels. Target: complete pour in one day to avoid cold joints. Vibrator consolidation along edges and around embedments.

5. Strike off surface with vibrating screed (2-4 m wide) riding on forms. This produces initial level surface within ±6 mm of design elevation.

6. Float surface when bleed water disappears: power float (rotating disc) for large areas, hand float for edges and tight spots. Apply dry-shake hardener at this stage — broadcast 3-5 kg/m² in two passes (2/3 first pass, 1/3 second pass), float into surface.

7. Cut control joints with early-entry saw within 12-24 hours of pouring. Joint depth: 1/4 slab thickness. Spacing: 4-6 m each direction (30× slab thickness is the maximum spacing rule). Joints create planned crack locations.

8. Apply curing compound immediately after final troweling. Maintain moisture for 7 days minimum. Keep traffic off slab for 3 days (foot traffic only), 7 days (light loads), 28 days (full design loads).

**Calibration / Verification**:
- Floor flatness: Measure with 3 m straightedge — maximum gap ≤3 mm for general industrial, ≤1.5 mm for precision areas. Alternatively: FF number method (FF 30-50 general, FF 50-80 precision).
- Surface level: ±6 mm from design elevation over 3 m, ±15 mm over entire floor area.
- Concrete strength: Crush test cylinders at 28 days — must meet specified grade.
- Joint depth: Verify 1/4 slab depth at saw-cut joints with depth gauge.

**Expected Performance**:
- Floor load classes: light 5-10 kN/m², medium 10-20 kN/m², heavy 20-50 kN/m², very heavy 50+ kN/m².
- Forklift point load: 2-tonne forklift with 2-tonne load = 100 kN per wheel. Check floor capacity at point loads, not just uniform load.
- Abrasion resistance: Dry-shake hardener surface withstands 10-20 years of forklift traffic before resurfacing needed.
- Crack control: Properly jointed floors crack at joints (planned); random cracks indicate inadequate joint spacing or excessive drying shrinkage.

**Applications**: Factory floors, warehouse floors, workshops, loading docks, parking structures.

**Strengths**:
- High load capacity — reinforced concrete slab supports heavy point loads from machinery and forklifts
- Durable surface — dry-shake hardener provides 10-20 years of abrasion resistance under forklift traffic
- Flat surface enables precision equipment installation — FF 50-80 flatness achievable with proper technique
- Economical at scale — slab-on-grade is the cheapest floor system per square meter for industrial loads

**Weaknesses**:
- Subgrade preparation is critical — settlement from inadequate compaction causes slab cracking that cannot be repaired without replacement
- Joints are maintenance points — joint edges spall under heavy forklift traffic, requiring periodic repair
- Limited resistance to chemical spillage — acids and solvents attack concrete surface; requires chemical-resistant coating (epoxy, minimum 3 mm)
- Heavy equipment point loads may exceed design — always check concentrated loads separately from uniform load rating


## Quantitative Parameters

## Vibration Isolation Parameters

| Equipment Type | Max Floor Velocity (mm/s) | Max Floor Displacement (mm) | Isolation Method |
|---------------|:-------------------------:|:--------------------------:|------------------|
| Optical inspection | 0.05 | 0.001 | Air springs (0.5-2 Hz) |
| Precision grinder | 0.1 | 0.005 | Spring isolators (2-5 Hz) |
| Coordinate measuring machine | 0.2 | 0.010 | Neoprene pads + inertia block |
| Standard machine tool | 0.5 | 0.025 | Neoprene pads (5-15 Hz) |
| General factory floor | 1.0 | 0.050 | Cork pads or direct mount |

## Crane Runway Design Parameters

| Parameter | Light Crane (<10 t) | Heavy Crane (≥10 t) |
|-----------|:-------------------:|:-------------------:|
| Beam deflection limit | L/800 | L/1000 |
| Rail tolerance (alignment) | ±1 mm | ±0.5 mm |
| Rail gauge tolerance | ±1 mm | ±0.5 mm |
| Lateral load (% capacity) | 10% | 10% |
| Rail clip spacing | 500-600 mm | 500-600 mm |

## Concrete Mix Ratios for Industrial Use

| Application | Mix (C:S:A by weight) | W/C Ratio | 28-day Strength (MPa) | Notes |
|-------------|:---------------------:|:---------:|:---------------------:|-------|
| Machine foundation | 1:1.5:3 | 0.40-0.45 | 35-45 | High strength, low shrinkage |
| Factory floor slab | 1:2:4 | 0.45-0.50 | 25-35 | Standard structural |
| Foundation blinding | 1:3:6 | 0.60 | 15-20 | Leveling layer only |
| Grout (non-shrink) | 1:1 (cement:sand) | 0.30 | 50+ | Machine leveling pads |

## Rebar Reference

| Bar Diameter (mm) | Cross-section (mm²) | Weight (kg/m) | Yield Strength (MPa) |
|:-----------------:|:-------------------:|:-------------:|:-------------------:|
| 8 | 50 | 0.40 | 400-500 |
| 12 | 113 | 0.89 | 400-500 |
| 16 | 201 | 1.58 | 400-500 |
| 20 | 314 | 2.47 | 400-500 |
| 25 | 491 | 3.85 | 400-500 |
| 32 | 804 | 6.31 | 400-500 |


## Scaling Notes

- **Small workshop (100-300 m²)**: Single-story, timber or light steel frame, 150 mm concrete floor on compacted subbase. No crane. Hand-operated hoists. Construction: 4-8 weeks.

- **Medium factory (500-2000 m²)**: Steel frame, 200 mm reinforced concrete floor, 5-10 tonne overhead crane in one bay. Requires concrete mixer and small crane for erection. Construction: 2-4 months.

- **Large industrial plant (2000-10,000 m²)**: Multi-bay steel frame, heavy-duty floors (300 mm, 20-50 kN/m²), multiple cranes (10-50 tonnes), vibration-isolated precision areas. Requires full construction crew (20-50 workers), concrete batching plant, 20-50 tonne erection crane. Construction: 6-18 months.

- **Machine foundation scaling**: Lathe (1-5 t): 1.5-2.5 m deep block, 1.2× machine footprint. Forge hammer (5-50 kJ): 10-15× hammer weight, timber/cork padding, sand gap isolation. Steam engine (50-500 HP): 2-3 m deep, isolated from floor slab. Generator (100-1000 kVA): mass ≥5× generator mass, anti-vibration mounts at base.


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Floor cracking at mid-panel (no joint) | Control joints too widely spaced, excessive shrinkage | Cut additional joints at 4-6 m spacing; next pour: reduce spacing or add steel fiber |
| Machine vibrating excessively on foundation | Foundation mass insufficient, isolation material wrong frequency | Add inertia mass (concrete block on top); verify isolation natural frequency is <0.5× machine operating frequency |
| Crane runway beam bouncing | Beam undersized, deflection exceeds L/800 | Stiffen beam with cover plates welded to flanges; reduce crane speed; check beam for fatigue cracking |
| Concrete floor surface dusting (powdering) | Low cement content, over-troweled, inadequate curing | Apply chemical hardener (sodium silicate solution); improve curing practice for next pour |
| Steel column base plate corrosion | Water ponding at base, no grout seal | Grout under base plate to seal gap; paint exposed steel; improve drainage away from column base |
| Floor joint spalling | Joint edges not supported, heavy forklift traffic | Install joint armor (steel angle) at load-bearing joints; fill joints with semi-rigid epoxy |
| Machine foundation settling unevenly | Weak soil pocket under one corner, inadequate subgrade preparation | Underpin settled corner with concrete pile or grout injection; for new foundations: probe subgrade before pouring |
| Roof leaking at penetration (vent, skylight) | Inadequate flashing, no curb, sealant failure | Install raised curb (150 mm) around penetration; flash with 0.5 mm copper; reseal annually |


## Safety

- **Concrete burns**: Wet cement (pH 12-13) causes chemical burns with prolonged skin contact. Wear gauntlet gloves when handling wet concrete. Wash skin immediately if contact occurs. Eye protection mandatory during concrete pouring — splatter can cause corneal burns.

- **Steel erection falls**: Working at heights of 6-12 m during frame erection is the most dangerous construction phase. Safety harnesses tied to completed structure members are mandatory. Minimum 2 workers for any steel erection task. Historical fatality rate: 1-2 per 100,000 worker-hours for steel erection.

- **Crane operations**: Overhead cranes moving 5-50 tonnes create crush hazard. Never stand under suspended load. Use tag lines to control load swing. Crane runway beams must be inspected annually for fatigue cracking at weld details — a cracked runway beam can drop the crane.

- **Concrete vibrator vibration exposure**: Hand-held concrete vibrators transmit vibration to operators' hands, causing hand-arm vibration syndrome (white finger) with chronic exposure. Limit continuous use to 30 minutes; rotate operators; use anti-vibration gloves.

- **Machine foundation excavation collapse**: Trenches deeper than 1.5 m for machine foundations must be shored (timber or hydraulic shoring) before worker entry. Soil collapses kill quickly — burial above the waist causes crush asphyxiation within minutes.

- **Reinforcing steel impalement**: Exposed rebar sticking up from foundations presents impalement hazard. Cover all exposed bar ends with plastic caps or bend over before leaving work area.


## Quality Control

- **Concrete testing**: Take 3 test cylinders per 50 m³ poured. Crush at 7 and 28 days. Reject batches that fail to meet 28-day specified strength. Slump test at delivery: 75-125 mm. Reject concrete with slump >150 mm (excess water weakens concrete).

- **Rebar inspection**: Check bar diameter (caliper measurement ±0.5 mm), spacing (tape measure ±10 mm), cover (cover meter, non-destructive), and lap length (minimum 40× bar diameter for tension laps).

- **Steel frame alignment**: Survey column plumb and beam level after erection. Plumb: ±5 mm per 6 m. Level: ±5 mm per 10 m span. Bolt torque verification on 10% of bolts.

- **Floor flatness**: Straightedge test at 3 m intervals in two directions. Maximum gap: ≤3 mm general, ≤1.5 mm precision. Document all measurements.

- **Crane runway alignment**: Rail straightness ±1 mm per 10 m, gauge ±0.5 mm. Runway beam camber within L/1000 of design.


## Variations and Alternatives

| Foundation Type | Load Capacity | Vibration Isolation | Cost | Best For |
|----------------|:------------:|:-------------------:|:----:|----------|
| Block foundation | High (massive) | Good (mass absorbs energy) | Moderate | Individual machines, engines, generators |
| Mat (raft) foundation | Very high (distributed) | Moderate | High | Multiple machines on weak soil |
| Table foundation | Moderate (elevated) | Excellent (isolation at supports) | High | Precision equipment, CMMs, wafer tools |
| Direct mount on slab | Low (no isolation) | None | Low | Light equipment, storage racks, workbenches |
| Pile-supported foundation | Very high (transfers to deep strata) | Good (mass + isolation) | Very high | Very heavy machines on weak soil |

## Decision Criteria for Foundation Type

- **Use block foundation when**: single machine, soil bearing capacity >150 kN/m², vibration isolation needed but not extreme.
- **Use mat foundation when**: multiple machines close together, soil <150 kN/m², differential settlement must be minimized.
- **Use table foundation when**: precision equipment (grinders, CMMs), vibration must be <0.1 mm/s at floor level.
- **Use direct mount when**: light equipment (<500 kg), no dynamic loads, vibration not a concern.


## See Also

- [Building Materials & Methods](./building-materials.md) — Timber framing, masonry, scaffolding
- [Structural Engineering](./structural-engineering.md) — Beam design, column design, foundation theory
- [Cement & Concrete](../chemistry/cement.md) — Concrete mix design, rebar, and curing
- [Lubricants](../chemistry/lubricants.md) — Machinery lubrication systems
- [Energy](../energy/index.md) — Electrical power supply to industrial buildings
- [Machine Tools](../machine-tools/index.md) — The heavy equipment that requires specialized foundations
- [Iron & Steel](../metals/iron-steel.md) — Structural steel production and properties



[← Back to Construction](index.md)
