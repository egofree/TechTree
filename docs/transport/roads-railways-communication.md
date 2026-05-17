# Transportation, Logistics & Communication

> **Node ID**: `transport`
> **Domain**: [Transportation, Logistics & Communication](./)
> **Dependencies**: `energy`, `machine-tools`, `metallurgy`, `mining`
> **Timeline**: Years 5-50+
> **Outputs**: roads, bridges, vehicles, canals, railways, telegraph, logistics_systems

## Problem

Semiconductor fabrication requires raw materials from diverse sources (quartz, iron, coal, fluorite, copper, sulfur, etc.), concentrated labor forces, and coordination across distances. Without transportation and communication infrastructure, operations remain village-scale.

## Technologies &amp; Systems

### Road Construction

**Survey and alignment**:
- **Route selection**: Follow natural terrain — avoid steep grades (>8% for animal-drawn, >5% for heavy carts). Minimize stream crossings. Prefer ridgelines and valley floors. Map route with compass and level (A-frame level or water level for grade control).
- **Grading**: Cut high spots, fill low spots. Target cross-section: crowned surface (10-15 cm higher at center than edges) for drainage, 3-5 m wide for two-way cart traffic. Ditches on both sides, 30-50 cm deep. Compact roadbed by rolling (heavy stone or iron roller, 1-3 tonnes, drawn by animals or winch).

**Road surfaces**:
- **Dirt road**: Compacted native soil. Adequate for dry climates. Becomes impassable mud in wet weather. Maintain by grading and drainage.
- **Gravel road**: 15-30 cm crushed rock (5-10 cm stone) over compacted subgrade. Top layer: 5-10 cm finer gravel (1-3 cm). Cambered for drainage. Requires periodic re-grading. Serviceable in most weather. 10-20 km/h cart speed.
- **Macadam road**: Three layers of progressively finer broken stone (base: 10 cm stone, middle: 5 cm, surface: 2-3 cm). Each layer compacted with heavy roller. Interlocking angular stones create stable surface. Water-bound macadam: water + stone dust fills voids → sets hard. Tar-bound macadam (Chemistry+): hot coal tar penetrates surface → waterproof, more durable.
- **Paving** (Energy+): Stone blocks (granite, 15-20 cm cubes) or cast concrete slabs on prepared base. Durable, handles heavy loads. Labor-intensive. For high-traffic routes and urban areas.

**Bridge construction**:
- **Timber beam bridge**: Simple span up to 10 m. Wooden beams (30-50 cm diameter logs or 20×30 cm sawn timbers) on stone abutments. Deck planking on top. Design load: 2-5 tonnes for cart traffic. Pressure-treat timber with creosote (Chemistry) or replace every 10-20 years.
- **Stone arch bridge**: Spans 5-30+ m. Build timber centering (temporary falsework) in arch shape. Lay stone voussoirs (wedge-shaped stones) from both abutments toward center. Place keystone. Remove centering. Arch is self-supporting — load transfers horizontally to abutments. Extremely durable (centuries). Requires skilled masonry.
- **Truss bridge** (the Machine Tools-Energy stage transition): Triangular framework of iron or steel members. Pratt or Howe truss design. Spans 20-100+ m. Calculate member sizes from expected loads (dead load + live load + wind load with safety factor of 2-4). Connections: riveted or pinned. Much faster to erect than stone arch.

### Wheeled Vehicles

**Cart construction** (Metallurgy):
- **Wheels**: Wooden spoke wheels (hub, 8-12 spokes, felloes/rim). Hub: turned on lathe from elm or oak (interlocking grain resists splitting). Spokes: ash (strong, flexible). Rim: bent oak or ash felloes, joined by iron strakes (iron bands shrunk on — heat band, place on wheel, cool → tight fit). Wheel diameter 1-1.5 m.
- **Axles**: Hardwood (oak) or iron. Fixed axle (wheels rotate on axle) or rotating axle (axle turns with wheels). Grease with tallow or animal fat for lubrication.
- **Body**: Wooden platform or box (1.5-2 m × 1-1.5 m) on axle. Load capacity: 500-1000 kg for animal-drawn cart.
- **Draft**: Single animal (ox, horse, mule) pulls 500-1500 kg on level road. Ox: slower (3-4 km/h) but stronger steady pull. Horse: faster (5-8 km/h) but less steady pulling power. Two animals double the load.

**Wagon** (heavier, the Metallurgy-Machine Tools stage transition):
- Larger version of cart, 2-4 wheels, covered or open. Leaf spring suspension (Machine Tools+ — stacked steel strips, improve ride over rough roads). Load 2-5 tonnes. Four-horse team typical for long-distance freight.

### Water Transport

**Canal construction**:
- **Route**: Follow contour lines to minimize elevation change. Where elevation must change, use locks.
- **Lock construction**: Stone or timber chamber 5-8 m wide × 25-35 m long. Gates at each end (mitre gates — V-shaped, water pressure holds closed). Fill/empty chamber via paddles (sluice valves in gates). Raise/lower boats 2-5 m per lock. Lock cycle time: 10-20 minutes.
- **Canal dimensions**: Prism shape (trapezoidal cross-section). Bottom width 4-6 m, water depth 1.5-2 m. Clay puddle lining (compacted clay, 30 cm thick) to prevent leakage through permeable soils. Towpath on one bank for draft animals.
- **Barge**: Flat-bottomed wooden boat, 4-5 m wide × 20-30 m long. Load 20-100 tonnes. Drawn by horse or mule on towpath at 3-5 km/h. Canal transport is 10-50x cheaper per tonne-km than road transport for bulk materials.

**Port facilities**:
- Wharf or pier: timber or stone construction. Crane for loading/unloading (wooden derrick with hand-winch or horse whim, lift 1-5 tonnes). Warehouse adjacent. 100-500 tonnes/day throughput for well-equipped port.

### Railways (Energy+)

**Track construction**:
- **Subgrade**: Graded and compacted earth foundation. Ballast: crushed stone (10-15 cm layer) for drainage and load distribution.
- **Rails**: Initially iron straps on wooden stringers (strap rail — iron bar 2.5-5 cm wide × 1-1.5 cm thick nailed to timber). By the Energy stage: wrought iron or steel T-rails (inverted-T cross section, 15-30 kg/m, rolled in iron rolling mill). Rail length: 5-10 m sections, joined by fish plates (steel plates bolted through rail web holes).
- **Gauge**: Standard gauge 1435 mm (4 ft 8½ in). Standardize early — different gauges prevent network interoperability. This specific gauge is the global standard derived from Roman chariot wheel spacing.
- **Sleepers (ties)**: Timber (treated with creosote or tar), 2.4-2.7 m long × 20-25 cm wide × 12-15 cm thick. Spaced every 0.6-0.8 m. Rails spiked to sleepers with cut spikes (L-shaped iron spikes driven into wood).
- **Grade**: Maximum 2-3% for steam locomotives. Minimum curve radius 150-300 m. Gentle grades and curves = lower fuel consumption, higher speed, less wear.

**Steam locomotive** (Energy):
- **Boiler**: Fire-tube boiler (fire tubes carry hot gas through water space). Pressure 0.7-1.5 MPa. Diameter 1-1.5 m, length 3-5 m. 50-200 fire tubes, 5 cm diameter each. Coal-fired firebox at one end, smokebox and chimney at other. Steam dome on top for dry steam collection.
- **Cylinders**: 2 cylinders, 30-50 cm bore, 40-60 cm stroke. Steam admitted alternately on each side of piston (double-acting). Slide valve or piston valve, actuated by Stephenson valve gear (link motion — adjustable cutoff for steam economy). Operating pressure: 0.7-1.0 MPa.
- **Power**: 50-200 HP. Speed: 30-80 km/h. Tractive effort: 2000-10000 kgf. Haul 50-200 tonnes on level track.
- **Driving wheels**: 4-8 driven wheels (coupled by connecting rods). Leading and trailing trucks (unpowered wheels) for stability.

### Telegraph Communication

**Principles**:
- Electrical current through wire → electromagnetic effect at receiver. Encode information as sequences of current on/off (binary code — Morse code: dots and dashes represent letters and numbers).
- **Circuit**: Battery (or generator) → telegraph key (switch) → transmission wire → sounder (electromagnet + armature) → ground return (earth completes circuit — single wire sufficient for most installations).

**Telegraph key**:
- Spring-loaded lever with electrical contacts. Press lever → contacts close → current flows → remote sounder clicks. Release → spring opens contacts → sounder clacks. "Dot" = short press (~0.1 s). "Dash" = long press (~0.3 s). Pause between elements ~0.1 s, between letters ~0.3 s, between words ~0.7 s.

**Sounder**:
- Electromagnet (iron core with many turns of fine copper wire — 5-20 Ω resistance). Armature (iron bar) held above electromagnet core by spring. When current flows → electromagnet pulls armature down → "click" sound. When current stops → spring pulls armature up → "clack" sound. Operator listens to click-clack pattern and translates to letters. Trained operators achieve 20-40 words per minute.

**Wire and line construction**:
- **Wire**: Iron or copper wire, 2-4 mm diameter. Iron stronger (less sag between poles) but higher resistance (poor conductor). Copper better conductor but requires more support. Galvanized iron wire (zinc-coated for corrosion resistance) common compromise. Resistance: ~10-50 Ω/km depending on wire gauge.
- **Poles**: Wooden poles (treated timber, 6-10 m tall), spaced 40-60 m apart. Wire attached via glass or ceramic insulators (prevents current leakage through wet pole). Single wire on cross-arm. Ground wire at each station.
- **Range**: Direct current from batteries effective to ~50-100 km (voltage drop in wire limits range). For longer distances: relay stations every 50-100 km (incoming signal activates relay → re-transmits on fresh battery to next station). Or use higher voltage (100-200V from generator). Transcontinental telegraph: ~5000 km with ~50-100 relay stations.

**Battery for telegraph**:
- **Daniell cell**: Copper electrode in CuSO₄ solution | unglazed porcelain separator | zinc electrode in ZnSO₄ or dilute H₂SO₄ solution. Voltage: 1.1V per cell. Stack 10-50 cells in series for desired line voltage (10-50V). Stable output, long life. Or use DC generator (Energy+) for higher voltage.

**Morse code** (standardized):
```
A .-    B -...  C -.-.  D -..   E .     F ..-.  G --.   H ....
I ..    J .---  K -.-   L .-..  M --    N -.    O ---   P .--.
Q --.-  R .-.   S ...   T -     U ..-   V ...-  W .--   X -..-
Y -.--  Z --..
0 -----  1 .----  2 ..---  3 ...--  4 ....-  5 .....
6 -....  7 --...  8 ---..  9 ----.
```

**Telegraph network**:
- Hub-and-spoke topology: Central station connects to multiple outstations. Switchboard (manual patch panel) connects any pair of lines. Message routing: operator receives message, re-transmits to destination line.
- **Throughput**: 20-40 words/minute per line. For coordination of distant mining, manufacturing, and construction operations, this is transformative — decisions that took days by courier now take minutes.

### Logistics Management

**Standardized containers**:
- Wooden crates in standard sizes (0.5 m³, 1.0 m³, 2.0 m³). Stackable. Labeled with contents, weight, destination, handling instructions. Enables efficient loading of carts, wagons, rail cars.

**Inventory management**:
- **Ledger system**: Double-entry bookkeeping. Track all materials in, out, and on hand. Perpetual inventory (update with every transaction). Periodic physical count to verify ledger accuracy.
- **Reorder points**: Minimum stock levels for critical materials. When stock falls below reorder point → trigger procurement. Prevents stockouts that halt production.
- **Buffer stocks**: Maintain 2-4 weeks of critical materials (coal, iron, copper, chemicals). Protects against supply disruption.

**Warehouse design**:
- Dry, well-ventilated building. Organized by material type. Heavy materials on ground floor (structural load). Flammables in separate fireproof building. Chemicals in ventilated, bunded (liquid-tight containment) area. Shelving for small items. Open floor for bulk materials. Loading dock for vehicle access. Inventory control at entry/exit.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundations | Paths, basic transport, writing for records |
| Metallurgy | Iron tools for road building, wheeled vehicles, timber bridges |
| Machine Tools | Precision parts for rail, standardization of gauges and containers |
| Energy | Steam transport, telegraph, railways, iron bridges |
| the Silicon-Photolithography stage transition | Specialized transport for hazardous chemicals, cleanroom supplies |

## Safety Concerns

### Road & Bridge Construction
- **Falls from height**: Bridge construction over water or ravines. Use safety lines (rope harness secured to fixed point). Minimum 1 m temporary railing on all elevated work platforms.
- **Landslides during grading**: Cutting into hillsides can trigger slides, especially after rain. Cut slopes to stable angle (1:1 for most soils, 1:1.5 for clay). Inspect after heavy rain before resuming work.
- **Rock blasting** (if used): Secure minimum 200 m exclusion zone. Use safety fuse (burns at ~1 cm/s — cut fuse length for desired delay, minimum 60 seconds). No radio transmitters near electric detonators. Store explosives in separate magazine, 50+ m from occupied buildings.
- **Stone arch centering failure**: Falsework can collapse under partial load. Build centering to carry 2× total stone weight. Do not remove until keystone is fully seated and mortar set (7-28 days for lime mortar, 3-7 days for hydraulic lime).

### Steam Locomotive Operations
- **Boiler explosion**: Most lethal hazard. Causes: low water level (crown sheet exposed → overheats → fails at pressure), overpressure (safety valve malfunction), corrosion/thinning. **Prevention**: Two independent water gauges (try cocks as backup). Two safety valves set at design pressure + 10%. Hydraulic test boiler to 1.5× working pressure before first firing and annually thereafter. Regular inspection for scale, corrosion, and cracking. Blow down boiler daily to remove sediment. Never exceed rated pressure.
- **Coupling and shunting injuries**: Workers crushed between cars during coupling. **Prevention**: Link-and-pin coupling requires worker between cars — use buffer and chain system when available (Energy+). Fixed coupling height and standardized drawgear. Communication by hand signals or whistle codes before any movement. No person between cars during movement.
- **Derailment**: Caused by broken rails, washouts, excessive speed on curves, obstructions on track. **Prevention**: Walk track daily on active sections. Speed limits: 30 km/h on main line, 15 km/h on curves, 10 km/h in yards. Replace cracked rails immediately. Ballast drainage to prevent washout.
- **Runaway on grade**: Loaded train on downhill exceeds braking capacity. **Prevention**: Maximum 2-3% grade. Locomotive brake (steam brake or air brake, Energy+) plus hand brake on tender. Apply brakes before descending grade. Never coast. If brakes fail: deliberately derail on uphill side into embankment (pre-planned derailment points on long grades).
- **Fire risk**: Locomotive sparks ignite trackside vegetation, wooden bridges, buildings. Spark arrester (mesh screen in smokebox) mandatory. Clear vegetation 5 m each side of track in fire-prone areas. Water cart on train for firefighting.

### Canal and Water Transport
- **Drowning**: Lock chambers, canal banks, loading docks. Provide grab lines along lock walls. Life rings at each lock. Non-swimmers restricted from lock operation.
- **Lock gate failure**: Water pressure (5-8 m head = 50-80 kN/m²) can overwhelm gate. Build gates with 2× structural capacity. Inspect iron fittings for corrosion annually. Never open both lock gates simultaneously.
- **Canal bank collapse**: Saturated soil fails, especially after rapid drawdown (emptying lock quickly). Maintain constant water level where possible. Puddle clay lining prevents internal erosion. Inspect banks weekly.

### Telegraph
- **Electrical shock**: Telegraph lines carry 10-200V at low current — unlikely to be lethal but can cause burns and reflex injuries (falling from pole). Higher-voltage lines (generator-fed, 100-200V) can cause muscle contraction and inability to let go. **Prevention**: Insulate all terminals. Ground equipment properly. De-energize line before repair work on poles. Work on poles with safety belt.
- **Lightning strike**: Overhead wire attracts lightning. Install lightning arrestors at each station (spark gap to ground — normal voltage too low to arc, lightning voltage jumps gap and shunts to ground). Ground wire at every 10th pole.
- **Line worker falls**: Pole climbing with gaffs (spiked boots) and safety belt. Minimum pole condition: no rot, no cracks at ground level. Replace poles showing decay.

### General Transport Safety
- **Load securing**: Unsecured loads shift and overturn vehicles. Rope or chain all loads. Maximum load height: 1.5× vehicle width. Distribute weight evenly (60% over front axle, 40% over rear for carts).
- **Animal handling**: Draft animals can kick, bite, bolt. Approach from front/side, never directly behind. Use harness with breeching (rump strap) for braking on downhill. Shoe animals regularly (every 6-8 weeks) to prevent hoof injuries.
- **Night operations**: Minimal lighting (lanterns only). Reduce all speeds to 50% of daytime limits. Place lanterns on stationary obstacles. No rail movement at night without clear track verification.

## Key Deliverables

- All-weather road network connecting mining, processing, and manufacturing sites
- Water transport (canals, barges) for bulk material movement
- Standardized transport vehicles and containers
- Working telegraph communication network between all major sites
- Railway system for high-volume transport (Energy+)
- Inventory and logistics management system with ledger tracking
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
