# Water Power

> **Node ID**: energy.gravity
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`chemistry.lubricants`](../chemistry/lubricants.md), `textiles`
> **Enables**: [`energy.gravity.water-turbines`](water-turbines.md), [`energy.storage.pumped-hydro`](pumped-hydro.md)
> **Timeline**: Years 5-15
> **Outputs**: water_power, mechanical_rotation, ground_grain, pumped_water
> **Critical**: No — water power provides reliable mechanical energy but alternative power sources (steam, wind) can substitute where water is unavailable

### Overview

Water power converts the gravitational potential energy of flowing or falling water into rotational mechanical work. Historically the first non-animal industrial power source, water wheels enabled surplus grain milling, metalworking (bellows and trip hammers), wood sawing, and textile fulling centuries before wind or steam. A reliable stream with 2 m of head and 100 L/s flow can deliver ~1.5 kW (2 HP) of continuous mechanical power — day and night, rain or shine, fuel-free.

**[Hydraulic power calculation](../glossary/hydraulic-power-calculation.md)** (fundamental formula for all water power):
- P = η × ρ × g × Q × H
- Where: η = overall efficiency (0.20-0.90 depending on wheel/turbine type), ρ = water density (1000 kg/m³), g = gravitational acceleration (9.81 m/s²), Q = volumetric flow rate (m³/s), H = available head (m)
- Example: Overshot wheel, η = 0.65, Q = 0.1 m³/s, H = 4 m → P = 0.65 × 1000 × 9.81 × 0.1 × 4 = ~2,551 W (~3.4 HP)

### Water Wheel Types

**[Undershot wheel](../glossary/undershot-wheel.md)** (simplest, lowest efficiency — ancient, widely used):
- **Principle**: Flat paddles dip into flowing water below the wheel. Water current pushes paddles, turning the wheel. No head required — works on horizontal flow velocity alone.
- **Efficiency**: ~20-30%. Most energy lost to turbulence as water rushes past and around paddles.
- **Construction**: Wooden paddles (oak or elm, 5-10 cm thick) bolted to wooden spokes mounted on wooden or iron axle (30-50 cm diameter). Wheel diameter 2-5 m, width 0.5-2 m. Paddle depth in water ~20-40 cm.
- **Site requirements**: Stream or river with reliable flow, ~0.5 m/s+ water velocity. Can be enhanced with a sluice gate and narrow channel to concentrate and accelerate flow onto the paddles.
- **Power output**: 0.5-3 HP depending on water velocity and wheel size. Sufficient for grain grinding, bellows operation, and small sawmills.
- **Advantages**: Simplest construction, works on flat terrain with no elevation change, easiest to maintain. Paddles can be replaced individually.
- **Limitations**: Low efficiency, output varies directly with stream flow (seasonal variability), ice and debris can damage paddles in flood.

**Materials**:
- [Oak or elm paddles](../plants/index.md) (5-10 cm thick, 0.5-2 m long, 20-40 per wheel)
- [Wooden spokes](../plants/index.md) (oak, 10-15 cm diameter, 8-16 per wheel)
- [Iron axle](../metals/iron-steel.md) (30-50 cm diameter, 1-3 m long) or [wooden axle](../plants/index.md) (oak, 40-60 cm diameter)
- [Iron bolts and bands](../metals/iron-steel.md) (10-20 mm bolts, 30-50 mm flat bar bands)

**Calibration / Verification**:
1. Measure wheel RPM with a stopwatch over 10 revolutions (target: 3-10 RPM depending on wheel diameter and water velocity).
2. Measure water velocity at the paddle face with a float test (target: >0.5 m/s for practical output).
3. Verify paddle clearance from the mill race floor (target: 20-40 cm immersion in flowing water).
4. Check bearing temperature after 1 hour of operation — if bearings are hot to touch (>60°C), increase lubrication with tallow.

**Expected Performance**:
- Efficiency: 20-30% (hydraulic power input to shaft power output)
- Power output: 0.5-3 HP (0.4-2.2 kW) depending on water velocity and wheel size
- Shaft speed: 3-10 RPM
- Bearing friction loss: 5-10% of output

**[Breastshot wheel](../glossary/breastshot-wheel.md)** (intermediate — requires moderate head):
- **Principle**: Water enters buckets or paddles at roughly the axle height (breast level) and exits at the bottom. Combines impulse (water hitting buckets) with partial gravity (water weight in buckets as they descend). Requires a headrace delivering water at or near the axle height.
- **Efficiency**: ~35-50%. Significant improvement over undershot because buckets capture water and gravity assists through the descent.
- **Construction**: Wheel diameter 3-8 m, width 0.5-2 m. Buckets or curved paddles (not flat) designed to catch and hold water. Wooden construction with iron bands and hardware; later wheels used iron buckets. Breast wall (stone or timber) fits closely around the lower arc to prevent water spilling out of buckets prematurely.
- **Site requirements**: 1-3 m of head. Headrace (channel or flume) delivers water to wheel at axle level. Tailrace carries spent water away.
- **Power output**: 2-8 HP at typical flows. Well-suited to moderate-gradient streams.
- **Advantages**: Good efficiency without requiring the tall structure of an overshot wheel. Works with heads too low for overshot but too high for undershot efficiency gains.

**Materials**:
- [Oak frame and spokes](../plants/index.md) (5-10 cm thick structural members)
- [Curved paddles or iron buckets](../metals/iron-steel.md) (2-3 mm sheet iron, shaped to hold water)
- [Iron bands and tie-rods](../metals/iron-steel.md) (15-25 mm round bar)
- [Iron axle](../metals/iron-steel.md) (30-50 cm diameter) or [wooden axle](../plants/index.md)
- [Stone or timber breast wall](../mining/index.md) (fitted around lower wheel arc with <10 mm clearance)

**Calibration / Verification**:
1. Measure head between headrace water level and tailrace water level (target: 1-3 m).
2. Verify breast wall clearance around the wheel — maximum 10 mm gap. Gaps larger than 20 mm allow water to spill without doing work.
3. Measure wheel RPM at design flow (target: 3-12 RPM).
4. Check bucket filling — at operating speed, buckets should fill to 60-80% capacity without spilling over the sides.

**Expected Performance**:
- Efficiency: 35-50% (improved by breast wall seal quality)
- Power output: 2-8 HP (1.5-6 kW) at typical flows
- Shaft speed: 3-12 RPM

**Strengths**:
- Good efficiency (35-50%) without requiring tall headrace structures
- Works with moderate heads (1-3 m) that are common on small streams
- Iron buckets and tight breast wall push efficiency toward 55%

**Weaknesses**:
- Efficiency depends heavily on breast wall seal — worn or loose walls waste 10-20% of power
- Requires a headrace delivering water at axle height — more civil engineering than undershot
- Seasonal flow variation reduces output during dry periods

**[Overshot wheel](../glossary/overshot-wheel.md)** (highest efficiency water wheel — requires significant head):
- **Principle**: Water is delivered to the top of the wheel via a headrace and sluice, filling buckets at the crown. Water's weight in descending buckets drives the wheel — primarily a gravity machine, not an impulse machine. Buckets empty at the bottom into the tailrace.
- **Efficiency**: ~60-70%. Approaches the theoretical maximum for a gravity wheel because nearly all potential energy is captured.
- **Construction**: Wheel diameter 3-10 m (larger diameter = more buckets = more torque). Width 0.5-3 m. Closely spaced buckets with lips to retain water during descent. Oak frame with iron tie-rods and bolts; iron axles preferred when available. Axle bearings: stone blocks lubricated with tallow, or iron collars on hardwood.
- **Headrace and sluice**: Wooden flume or stone-lined channel delivering water from upstream mill pond to the wheel crown. Sluice gate (wooden or iron) controls flow to regulate speed and power. Penstock length depends on available head — can be 10-100+ m.
- **Tailrace**: Stone-lined or timber channel carrying spent water away. Must have sufficient slope to prevent back-flooding which would submerge lower buckets and create drag.
- **Power output**: 3-15+ HP for typical installations. Exceptional historical wheels reached 50-60 HP.
- **Advantages**: Highest efficiency of all water wheels, relatively constant power output if pond level is maintained, works well even with variable stream flow (pond acts as buffer).
- **Limitations**: Requires significant head (at least 2-3 m, ideally 4-8 m). Needs a dam or weir to create the mill pond. More complex civil engineering (headrace, sluice, tailrace). Vulnerable to floods and ice damage.

**Materials**:
- [Oak frame with closely spaced buckets](../plants/index.md) (5-10 cm thick members, 30-80 buckets per wheel)
- [Iron tie-rods and bolts](../metals/iron-steel.md) (15-25 mm round bar, prevents spreading)
- [Iron axle](../metals/iron-steel.md) (40-60 cm diameter, forged or cast) preferred; wooden axle acceptable for smaller wheels
- [Stone or iron bearings](../metals/index.md) lubricated with [tallow](../animals/index.md)
- [Wooden headrace/flume](../plants/index.md) (timber, 0.5-1.0 m wide, 10-100+ m length)

**Calibration / Verification**:
1. Measure available head from mill pond surface to tailrace water level (target: 3-10 m).
2. Verify sluice gate opens and closes freely — gate must seal within 5 mm when fully closed to stop the wheel.
3. Check bucket spacing: buckets should retain water throughout descent with no spill over the crown. Maximum bucket gap: 50-80 mm.
4. Measure wheel RPM at full sluice opening (target: 3-10 RPM). Faster indicates undersized wheel; slower indicates excessive friction.
5. Verify tailrace clearance: at maximum flow, tailrace water level must be at least 30 cm below the lowest bucket to prevent back-drag.

**Expected Performance**:
- Efficiency: 60-70% (highest of all water wheel types)
- Power output: 3-15+ HP (2.2-11+ kW) depending on head and flow
- Shaft speed: 3-10 RPM
- Mill pond buffer: 50-200 m³ provides hours of full-power operation during low-flow periods

**Strengths**:
- Highest efficiency of all water wheels (60-70%)
- Pond acts as buffer — relatively constant output even with variable stream flow
- Gravity-driven — lower mechanical stress than impulse-type wheels

**Weaknesses**:
- Requires significant head (2-3 m minimum, 4-8 m ideal) — limits site selection
- Needs dam or weir plus headrace — substantial civil engineering
- Vulnerable to flood damage and winter icing of headrace

### Dam and Mill Pond Construction

**[Dam basics](../glossary/dam-basics.md)** (creating the head and pond):
- **[Earth dam](../glossary/earth-dam.md)** (simplest): Compacted clay core with earth and stone shoulders. Height 2-5 m, crest width 2-3 m, upstream slope 1:2 (horizontal:vertical), downstream slope 1:2.5. Puddle clay core (0.5-1 m thick) keyed into natural subsoil to prevent seepage. Overflow spillway on one side to pass flood water safely.
- **Timber crib dam**: Log cribs (rectangular timber frames) filled with stone, stacked and pinned. Cross-planks on upstream face sealed with clay. Suitable for heads of 2-4 m. Easier to build than masonry in forested areas.
- **Masonry dam**: Stone blocks laid in lime or cement mortar on bedrock. Requires quarry stone, masonry skills, and cement. For heads 3-8 m. Longest-lasting option.
- **Mill pond**: Storage volume to buffer flow variability. Even a small pond (50-200 m³) allows the wheel to run at full power during brief low-flow periods. Intake screen (timber bar rack with 5-10 cm spacing) prevents debris from entering the headrace.

### Water Turbines

Water turbines replace water wheels where higher heads and efficiencies are available. They rotate faster (100-1000+ RPM vs. 5-20 RPM for wheels) and are far more compact for equivalent power. Turbines require iron or steel construction and precision machining — they are a post-water-wheel technology dependent on `machine-tools`.

**[Pelton wheel](../glossary/pelton-wheel.md)** (impulse turbine — high head, low flow):
- **Principle**: One or more water jets from a nozzle strike spoon-shaped buckets on the runner perimeter. The jet's kinetic energy transfers to the bucket — all pressure conversion happens at the nozzle, not in the runner. Runner operates in air (not submerged).
- **Head range**: 30-1000+ m. Best suited for mountain streams with steep gradients.
- **Efficiency**: Up to 85-91% at design flow.
- **Construction**: Cast iron or bronze runner with forged steel buckets. Buckets split the jet in half (splitter ridge) and redirect it ~165° for maximum momentum transfer. Nozzle diameter 5-50 mm, jet velocity = √(2gH) — at 100 m head, jet velocity ~44 m/s. Often multiple nozzles (2-6) on a single runner for more power at partial flow.
- **Power output**: 1-500+ HP. Small units (5-20 HP) are practical for mountainous sites.
- **Advantages**: Excellent for high-head, low-flow sites. Simple, robust, tolerant of debris (large buckets don't clog easily). Easy to govern (deflect jet or vary nozzle opening).

**Materials**:
- [Cast iron or bronze runner hub](../metals/index.md) (200-500 mm diameter)
- [Forged steel buckets](../metals/iron-steel.md) (bolted to hub, splitter ridge machined to ±1 mm)
- [Converging needle nozzle](../metals/iron-steel.md) (bronze or steel, 5-50 mm jet diameter)
- [Steel penstock pipe](../metals/iron-steel.md) (100-300 mm diameter, rated to 10-50 bar)

**Calibration / Verification**:
1. Measure jet velocity: v = √(2gH). At 100 m head, v ≈ 44 m/s. Verify nozzle diameter produces target flow (Q = A × v).
2. Check bucket splitter ridge alignment — must bisect the jet within ±2 mm. Misalignment wastes 5-10% efficiency.
3. Measure runner speed at full flow (target: approximately half the jet velocity for maximum efficiency).
4. Verify bearing temperature after 2 hours of operation (target: <60°C with grease lubrication).

**Expected Performance**:
- Efficiency: 85-91% at design flow
- Power output: 1-500+ HP (0.7-370+ kW)
- Runner speed: 200-1,000 RPM
- Head range: 30-1,000+ m

**Strengths**:
- Highest efficiency of any turbine type at high head sites (up to 91%)
- Operates in air — no submerged runner, simplifies maintenance
- Tolerant of debris — large bucket openings don't clog

**Weaknesses**:
- Limited to high-head sites (>30 m) — useless on low-gradient rivers
- Nozzle erosion from high-velocity water and suspended sediment requires periodic replacement
- Jet deflection for governing wastes water — less efficient at partial load than variable-guide-vane designs

**[Francis turbine](../glossary/francis-turbine.md)** (reaction turbine — medium head, medium flow):
- **Principle**: Water enters the runner radially from a spiral casing (volute), passes through adjustable guide vanes (wicket gates) that direct flow at the optimal angle, then flows through the runner blades and exits axially via the draft tube. Both pressure and velocity drop across the runner — a true reaction machine.
- **Head range**: 3-300 m. The most versatile turbine type.
- **Efficiency**: 80-94% at design flow.
- **Construction**: Cast iron or steel spiral casing, adjustable bronze or steel guide vanes, cast steel runner with complex curved blades, steel draft tube. Requires precision casting and machining — the runner blade profiles must be accurate within ~1 mm for good efficiency. Wicket gate mechanism allows flow regulation for speed control.
- **Power output**: 10-100,000+ HP (scalable from small installations to major hydroelectric stations).
- **Advantages**: Highest efficiency of any hydraulic turbine at design point, excellent speed regulation via wicket gates, wide operating range. The dominant turbine for hydroelectric generation.
- **Limitations**: Complex construction requiring precision manufacturing. Susceptible to cavitation if draft tube submergence is insufficient. Not practical without iron/steel industry and machine tools.

**[Kaplan turbine](../glossary/kaplan-turbine.md)** (axial-flow reaction turbine — low head, high flow):
- **Principle**: Propeller-type runner with adjustable blade pitch (like an outboard motor running in reverse). Water flows axially through the runner — no radial component. Adjustable blades allow efficient operation over a wide flow range.
- **Head range**: 1-15 m. Designed for large rivers with low dams.
- **Efficiency**: 80-92% at design flow, maintains good efficiency over a wide flow range due to adjustable blades.
- **Construction**: Similar to Francis but with propeller runner. Adjustable blade mechanism (hub contains linkage to rotate blades) requires precision engineering. Steel or cast iron construction throughout.
- **Power output**: 50-100,000+ HP. Typically installed in large run-of-river or low-head dam sites.
- **Advantages**: Excellent for low-head, high-flow sites where Francis turbines would be too large. Adjustable blades maintain efficiency across varying flows. Compact for its power.
- **Limitations**: Requires the most precision manufacturing of any turbine type. Cavitation risk is high at low heads — runner must be set below tailwater level.

### Power Transmission

**[Getting rotational power from wheel/turbine to the load:](../glossary/getting-rotational-power-from-wheelturbine-to-the-load.md)**

- **[Direct drive](../glossary/direct-drive.md)** (simplest): Wheel axle directly drives the load (millstones, saw, etc.) via gears or crank. Load must be adjacent to the wheel. Limited to one or two loads.
- **[Flat-rod system](../glossary/flat-rod-system.md)** (Stangenkunst — transmitting power over distance): Wooden or iron rods connected in a push-pull arrangement transmit reciprocating motion from water wheel to distant mine pumps or machinery. Rods supported on rocking posts every 10-20 m. Can transmit 5-10 HP over 1-2 km. Used extensively in Central European mining from the 16th century.
- **[Rope drive](../glossary/rope-drive.md)** (transmitting rotation over distance): Endless hemp or wire rope running on grooved pulleys (V-groove for grip). Can transmit 5-50 HP over 100-500 m. Rope speed 10-20 m/s. Sag and stretch require tensioning device. Superseded flat rods for new installations once good rope was available.
- **[Line shaft](../glossary/line-shaft.md)** (distributing power within a building): Horizontal iron shaft (50-100 mm diameter) running the length of the workshop, supported by hung bearings from ceiling joists. Driven by water wheel via bevel gears or belt. Each machine connected by belt drive from countershaft on the line shaft. Cone pulleys on each machine provide 2-4 speed ranges. A single 10 HP water wheel can drive an entire small workshop of 5-8 machines simultaneously via line shaft.

**[Belt and gear connections:](../glossary/belt-and-gear-connections.md)**
- **Flat belt**: Leather or canvas belt, 50-200 mm wide, connecting pulleys of different diameter for speed change. Speed ratio = driven pulley diameter / driver pulley diameter. Slip of 2-5% is normal and acts as a safety clutch. Minimum pulley diameter ~30× belt thickness to avoid cracking.
- **Wooden gears**: Apple, hornbeam, or ironbark teeth on oak hubs. Grease with tallow. Wooden teeth wear and break — designed for easy replacement. Typical gear ratio 3:1 to 8:1 from water wheel to millstones.
- **Iron gears**: Cast iron gear rims with machined teeth, far more durable. Require foundry and machine tools. Standard for all post-1700 installations.

### Site Assessment and Construction Sequence

1. **Survey for head and flow**: Measure available fall (head) with level and staff — even 1 m of head is usable. Estimate flow by timing a float over a known distance (surface speed × 0.8 × cross-section area ≈ flow rate). Record seasonal variations — a wheel sized for spring flood will idle in summer drought.
2. **Select wheel type by head**: 0-1 m → undershot; 1-3 m → breastshot; 3+ m → overshot. Higher heads open turbine options.
3. **Build dam and headrace**: If head requires it. Earth or timber crib for small heads. Stone or concrete for permanent installations. Headrace: wooden flume or stone-lined channel, sloped ~1:500 to maintain flow velocity without excessive turbulence.
4. **Construct wheel**: Assemble frame on-site. Oak or chestnut preferred for durability in wet conditions. Iron tie-rods prevent spreading. Mount on axle with bearings set in stone or timber foundations — must be level and aligned.
5. **Install sluice gate and control**: Adjustable flow control is essential. Wooden slide gate with lever or screw lift. Tailrace must be clear to prevent back-flooding.
6. **Connect to load**: Millstones, saw, bellows, or generator. Gear ratio and belt drive to match load speed requirements.
7. **Maintain**: Grease bearings daily (tallow). Inspect for ice damage after winter. Replace worn paddles/buckets. Clear debris from intake screen and tailrace.

### Water Power Parameters (Quick Reference)

| Parameter | Undershot | Breastshot | Overshot | Pelton | Francis | Kaplan |
|-----------|-----------|------------|----------|--------|---------|--------|
| Head range | 0-1 m | 1-3 m | 3-10+ m | 30-1000+ m | 3-300 m | 1-15 m |
| Efficiency | 20-30% | 35-50% | 60-70% | 85-91% | 80-94% | 80-92% |
| Power range | 0.5-3 HP | 2-8 HP | 3-15+ HP | 1-500+ HP | 10-100,000+ HP | 50-100,000+ HP |
| Wheel/runner speed | 3-10 RPM | 3-12 RPM | 3-10 RPM | 200-1000 RPM | 100-600 RPM | 60-300 RPM |
| Construction | Wood | Wood/iron | Wood/iron | Iron/steel | Iron/steel | Iron/steel |
| Precision required | Low | Low | Moderate | Moderate | High | Very high |

### Safety & Hazards

- **Dam failure**: Dam breaches release catastrophic flood waves. Historical death tolls in thousands. Proper dam construction: wide base, compacted earth or masonry, overflow spillway for flood events, regular inspection for seepage and cracking. Never build large dams on unstable foundations.
- **Water wheel entanglement**: Water wheels and turbines have powerful rotating components. Guard all accessible moving parts. Never approach a running water wheel — the force can pull a person under. Emergency stop mechanism for maintenance.
- **Penstock pressure**: Pressurized water pipes (penstocks) can burst if over-pressured or corroded. Pressure relief valves. Regular inspection. Never stand in front of penstock fittings under pressure.
- **Flash floods**: Water-powered installations on rivers are vulnerable to flash floods. Monitor upstream conditions. Emergency shutdown procedure. Evacuation plan for flood events.
- **Drowning**: Working near water intakes, dams, and mill races. Drowning risk. Safety ropes. Never work alone near water installations. Life jackets when working on or near water.

### Dam Construction in Detail

**Earth dam cross-section**: A small earth dam for a mill pond (2-10 m height) follows a standard profile. The clay core is the waterproof barrier, 1-2 m wide at the crest and expanding to 3-5 m at the base in a trapezoidal shape. The core is keyed into the natural subsoil or bedrock (a trench cut below the dam base and filled with puddled clay) to prevent under-seepage. On both sides of the core, compacted earth shoulders provide structural mass.

**Compaction method**: Earth is placed in lifts (layers) of 200-300 mm thickness. Each lift is compacted at optimum moisture content (the water content at which the soil achieves maximum density for a given compaction effort, typically 12-18% for clay soils). Compaction methods: hand tamper, animal-drawn roller, or mechanized vibratory roller. Too dry and the soil won't compact; too wet and it becomes plastic and squashes rather than densifies. The Proctor compaction test determines optimum moisture for each soil type.

**Slope ratios**: Upstream face slopes at 1:2.5 to 1:3 (horizontal:vertical) to resist wave erosion and sudden drawdown slumping. Downstream face slopes at 1:2 to 1:2.5. Flatter slopes are more stable but require more material. The crest width (3-5 m) allows vehicle access for maintenance and provides additional structural mass.

**Overflow spillway**: A concrete or masonry spillway with an ogee crest (S-shaped profile matching the underside of a nappe of falling water) is the safest flood passage. The spillway is sized for the maximum probable flood, not the average flood. For small dams, a broad-crested weir or drop-inlet spillway may substitute. The spillway must be separate from the dam embankment if possible (cut into the adjacent hillside) so that overflow never flows over the earth dam itself, which would erode it rapidly.

### Water Wheel Efficiency Comparison

**Undershot wheel (20-30% efficient)**: The simplest construction but least efficient. Flat paddles dip into the current and the wheel is driven entirely by the impulse of flowing water. Most energy is lost to turbulence as water deflects around the paddles without doing work. Improved versions use a close-fitting stone or timber channel (mill race) that concentrates flow onto the paddles, raising efficiency to perhaps 30%. Best for flat terrain with no available head.

**Breastshot wheel (35-55% efficient)**: Water enters at roughly axle height, filling buckets. The combined effect of water impact (impulse) and the weight of water in descending buckets (gravity) drives the wheel. The closely fitted breast wall (stone or timber curving around the lower arc) prevents water from spilling out of buckets before they reach the bottom. Efficiency depends heavily on how well the breast wall seals against the wheel. A well-built breastshot wheel with iron buckets and tight breast wall reaches 55%.

**Overshot wheel (60-75% efficient)**: Water is delivered to the top of the wheel via a headrace and flume, filling buckets at the crown. This is primarily a gravity machine: the weight of water in the descending half of the wheel provides the driving force. The buckets must be closely spaced with retaining lips to hold water during the descent, and the wheel must be sized so buckets empty cleanly at the bottom without dragging water back up. The headrace requires its own engineering: a wooden flume or stone-lined channel delivering water from the mill pond to the wheel crown, with a sluice gate for flow control.

### Power Transmission with Wooden Gear Trains

**Lantern pinion and crown gear**: The standard gear pair for converting slow wheel rotation to faster output speeds. The crown gear (also called the wallower or face gear) is a flat disc with wooden or iron teeth pegged around its circumference. The lantern pinion is a pair of flanged discs connected by iron or hardwood staves (round pins). The two mesh at 90° to transfer motion between horizontal wheel shaft and vertical millstone shaft. A single stage achieves 3-5:1 speed ratio.

**Wooden teeth**: Apple, hornbeam, or ironbark (dense, close-grained hardwoods) are turned or carved into gear teeth. Wooden teeth absorb shock loads that would break cast iron teeth, a significant advantage in water-powered machinery where flow variations cause torque spikes. The teeth are designed to be the sacrificial element: when a tooth breaks, a new one is pegged into the hub in minutes. Grease with tallow or tar to reduce wear. Expected tooth life: 1-5 years depending on load and lubrication.

**Iron teeth for heavy duty**: When the load exceeds what wooden teeth can reliably carry (above roughly 5-10 HP), cast iron gear rims with machined teeth are substituted. Iron teeth last decades rather than years but transmit shock directly to the shaft and bearings. The gear blank is a cast iron rim shrunk onto a wooden or iron hub, with teeth cut by milling or planing. Requires a foundry and machine tools.

**Multi-stage gearing**: For applications needing higher speed ratios (such as driving a generator from a slow water wheel), two or more gear stages are cascaded. Each stage adds a 3-5:1 ratio, so two stages yield 9-25:1 and three stages yield 27-125:1. Each stage introduces friction losses of 2-5%, so total transmission efficiency drops with each added stage. A well-maintained two-stage wooden gear train transmits power at roughly 85-90% efficiency.

### Specific Power Calculation Examples

The fundamental hydraulic power formula P = η × ρ × g × Q × H applies to every water power installation.

**Example 1, overshot wheel**: A stream delivers 50 L/s (0.05 m³/s) with 5 m of head. Using an overshot wheel at 65% efficiency: P = 0.65 × 1000 × 9.81 × 0.05 × 5 = 1,595 W ≈ 2.1 HP. This drives a single pair of millstones (typical requirement: 1.5-3 HP).

**Example 2, undershot wheel**: A river with no head but 1.5 m/s flow velocity, channel width 1.5 m, paddle depth 0.3 m. Effective flow area: 0.45 m². Flow intercepted: 0.45 × 1.5 = 0.675 m³/s. Equivalent head from velocity: H = v²/(2g) = 1.5²/19.62 = 0.115 m. At 25% efficiency: P = 0.25 × 1000 × 9.81 × 0.675 × 0.115 = 190 W ≈ 0.25 HP. Marginal but usable for small tasks.

**Example 3, Pelton turbine**: Mountain stream with 80 m head and 10 L/s (0.01 m³/s) flow. Pelton efficiency 88%: P = 0.88 × 1000 × 9.81 × 0.01 × 80 = 6,906 W ≈ 9.3 HP. Enough to drive a small generator producing 5-6 kW of electricity.

### Dam Construction in Detail

**Earth dam cross-section**: A small earth dam for a mill pond (2-10 m height) follows a standard profile. The clay core is the waterproof barrier, 1-2 m wide at the crest and expanding to 3-5 m at the base in a trapezoidal shape. The core is keyed into the natural subsoil or bedrock (a trench cut below the dam base and filled with puddled clay) to prevent under-seepage. On both sides of the core, compacted earth shoulders provide structural mass.

**Compaction method**: Earth is placed in lifts of 200-300 mm thickness. Each lift is compacted at optimum moisture content (typically 12-18% for clay soils). The Proctor compaction test determines optimum moisture for each soil type. Too dry and the soil won't compact; too wet and it squashes rather than densifies. Compaction methods: hand tamper, animal-drawn roller, or mechanized vibratory roller.

**Slope ratios**: Upstream face slopes at 1:2.5 to 1:3 (horizontal:vertical) to resist wave erosion and drawdown slumping. Downstream face slopes at 1:2 to 1:2.5. The crest width (3-5 m) allows vehicle access for maintenance.

**Overflow spillway**: A concrete or masonry spillway with an ogee crest (S-shaped profile matching the underside of falling water) is the safest flood passage. The spillway is sized for the maximum probable flood, not the average flood. For small dams, a broad-crested weir or drop-inlet spillway substitutes. The spillway should be cut into the adjacent hillside so overflow never flows over the earth dam itself.

### Water Wheel Efficiency Comparison

**Undershot wheel (20-30% efficient)**: The simplest construction but least efficient. Flat paddles dip into the current. Improved versions use a close-fitting stone or timber channel that concentrates flow onto the paddles, raising efficiency to perhaps 30%. Best for flat terrain with no available head.

**Breastshot wheel (35-55% efficient)**: Water enters at roughly axle height, filling buckets. The closely fitted breast wall prevents water from spilling out before the bottom. Efficiency depends heavily on breast wall seal quality. A well-built iron-bucket wheel with tight breast wall reaches 55%.

**Overshot wheel (60-75% efficient)**: Water delivered to the top via headrace and flume fills buckets at the crown. Primarily a gravity machine. Buckets must be closely spaced with retaining lips and sized to empty cleanly at the bottom.

### Power Transmission with Wooden Gear Trains

**Lantern pinion and crown gear**: The standard gear pair for converting slow wheel rotation to faster output. The crown gear (face gear) is a flat disc with wooden or iron teeth pegged around its circumference. The lantern pinion is a pair of flanged discs connected by iron or hardwood staves. The two mesh at 90°. A single stage achieves 3-5:1 speed ratio.

**Wooden teeth**: Apple, hornbeam, or ironbark (dense, close-grained hardwoods) are carved into gear teeth. Wooden teeth absorb shock loads that would break cast iron teeth. They are designed to be sacrificial: when a tooth breaks, a new one is pegged in minutes. Grease with tallow or tar. Tooth life: 1-5 years depending on load and lubrication.

**Iron teeth for heavy duty**: Above roughly 5-10 HP, cast iron gear rims with machined teeth are substituted. Iron teeth last decades but transmit shock directly to shafts and bearings. The gear blank is a cast iron rim shrunk onto a wooden or iron hub.

**Multi-stage gearing**: For applications needing higher speed ratios (such as driving a generator from a slow water wheel), two or more gear stages are cascaded. Each stage adds a 3-5:1 ratio. Two stages yield 9-25:1, three stages yield 27-125:1. Each stage introduces 2-5% friction loss. A well-maintained two-stage wooden gear train transmits power at roughly 85-90% overall efficiency.

**Belt drive addition**: Flat leather or canvas belts (50-200 mm wide) connecting pulleys of different diameters provide additional speed changes with built-in slip protection. Speed ratio equals driven pulley diameter divided by driver pulley diameter. Slip of 2-5% is normal and acts as a safety clutch, preventing catastrophic damage if the driven machine jams. Minimum pulley diameter is roughly 30× belt thickness to avoid cracking the leather.

**Line shaft distribution**: A single water wheel of 10 HP can drive an entire small workshop of 5-8 machines simultaneously via a horizontal line shaft. The iron shaft (50-100 mm diameter) runs the length of the workshop, supported by hung bearings from ceiling joists. Each machine connects via its own belt drive from a countershaft, with cone pulleys providing 2-4 speed ranges.

### Limitations

- **Power ceiling**: Water wheels top out at ~50-100 kW for the largest installations. Overshot wheels rarely exceed 3-4 m width and 10 m diameter due to structural limits of timber construction.
- **Site dependency**: Water power requires flowing water with usable head. Suitable sites are fixed by geography and cannot be relocated. Drought and freezing can halt production seasonally.
- **Speed variability**: Water flow varies with seasons and weather. Power output fluctuates accordingly, making consistent shaft speed difficult without governors and flywheels.
- **Head limitations**: Gravity-powered mechanical systems (weights, pendulums) provide extremely low energy density. A 1-tonne weight falling 10 m stores only 98 kJ — equivalent to ~2 grams of gasoline.
- **Ice and debris**: Winter freezing blocks water channels. Debris (leaves, branches, silt) requires constant trash rack cleaning. Flood events can damage or destroy water wheel installations.

### See Also

- [Water Turbines](water-turbines.md) — Modern evolution of water power
- [Pumped Hydro](pumped-hydro.md) — Gravity-based energy storage at scale
- [Steam Power](steam-power.md) — Alternative prime mover not dependent on water flow
- [Machine Tools](../machine-tools/index.md) — Workshop machines driven by line shafts
- [Energy Storage](storage.md) — Overview of energy storage technologies
- [Wind Power](wind.md) — Another renewable energy source

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
