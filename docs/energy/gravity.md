# Water Power

> **Node ID**: energy.gravity
> **Domain**: [Energy](./)
> **Dependencies**: `foundations`, `metals.copper-bronze` or `metals.iron-steel`
> **Enables**: `energy.steam-power` (boiler feedwater pumping, mechanical skills), `foundations.food-agriculture` (grain milling), `health.sanitation` (pumping), `energy.electricity` (prime mover for generators)
> **Timeline**: Years 5-15
> **Outputs**: water_power, mechanical_rotation, ground_grain, pumped_water

### Overview

Water power converts the gravitational potential energy of flowing or falling water into rotational mechanical work. Historically the first non-animal industrial power source, water wheels enabled surplus grain milling, metalworking (bellows and trip hammers), wood sawing, and textile fulling centuries before wind or steam. A reliable stream with 2 m of head and 100 L/s flow can deliver ~1.5 kW (2 HP) of continuous mechanical power — day and night, rain or shine, fuel-free.

**Hydraulic power calculation** (fundamental formula for all water power):
- P = η × ρ × g × Q × H
- Where: η = overall efficiency (0.20-0.90 depending on wheel/turbine type), ρ = water density (1000 kg/m³), g = gravitational acceleration (9.81 m/s²), Q = volumetric flow rate (m³/s), H = available head (m)
- Example: Overshot wheel, η = 0.65, Q = 0.1 m³/s, H = 4 m → P = 0.65 × 1000 × 9.81 × 0.1 × 4 = ~2,551 W (~3.4 HP)

### Water Wheel Types

**Undershot wheel** (simplest, lowest efficiency — ancient, widely used):
- **Principle**: Flat paddles dip into flowing water below the wheel. Water current pushes paddles, turning the wheel. No head required — works on horizontal flow velocity alone.
- **Efficiency**: ~20-30%. Most energy lost to turbulence as water rushes past and around paddles.
- **Construction**: Wooden paddles (oak or elm, 5-10 cm thick) bolted to wooden spokes mounted on wooden or iron axle (30-50 cm diameter). Wheel diameter 2-5 m, width 0.5-2 m. Paddle depth in water ~20-40 cm.
- **Site requirements**: Stream or river with reliable flow, ~0.5 m/s+ water velocity. Can be enhanced with a sluice gate and narrow channel to concentrate and accelerate flow onto the paddles.
- **Power output**: 0.5-3 HP depending on water velocity and wheel size. Sufficient for grain grinding, bellows operation, and small sawmills.
- **Advantages**: Simplest construction, works on flat terrain with no elevation change, easiest to maintain. Paddles can be replaced individually.
- **Limitations**: Low efficiency, output varies directly with stream flow (seasonal variability), ice and debris can damage paddles in flood.

**Breastshot wheel** (intermediate — requires moderate head):
- **Principle**: Water enters buckets or paddles at roughly the axle height (breast level) and exits at the bottom. Combines impulse (water hitting buckets) with partial gravity (water weight in buckets as they descend). Requires a headrace delivering water at or near the axle height.
- **Efficiency**: ~35-50%. Significant improvement over undershot because buckets capture water and gravity assists through the descent.
- **Construction**: Wheel diameter 3-8 m, width 0.5-2 m. Buckets or curved paddles (not flat) designed to catch and hold water. Wooden construction with iron bands and hardware; later wheels used iron buckets. Breast wall (stone or timber) fits closely around the lower arc to prevent water spilling out of buckets prematurely.
- **Site requirements**: 1-3 m of head. Headrace (channel or flume) delivers water to wheel at axle level. Tailrace carries spent water away.
- **Power output**: 2-8 HP at typical flows. Well-suited to moderate-gradient streams.
- **Advantages**: Good efficiency without requiring the tall structure of an overshot wheel. Works with heads too low for overshot but too high for undershot efficiency gains.

**Overshot wheel** (highest efficiency water wheel — requires significant head):
- **Principle**: Water is delivered to the top of the wheel via a headrace and sluice, filling buckets at the crown. Water's weight in descending buckets drives the wheel — primarily a gravity machine, not an impulse machine. Buckets empty at the bottom into the tailrace.
- **Efficiency**: ~60-70%. Approaches the theoretical maximum for a gravity wheel because nearly all potential energy is captured.
- **Construction**: Wheel diameter 3-10 m (larger diameter = more buckets = more torque). Width 0.5-3 m. Closely spaced buckets with lips to retain water during descent. Oak frame with iron tie-rods and bolts; iron axles preferred when available. Axle bearings: stone blocks lubricated with tallow, or iron collars on hardwood.
- **Headrace and sluice**: Wooden flume or stone-lined channel delivering water from upstream mill pond to the wheel crown. Sluice gate (wooden or iron) controls flow to regulate speed and power. Penstock length depends on available head — can be 10-100+ m.
- **Tailrace**: Stone-lined or timber channel carrying spent water away. Must have sufficient slope to prevent back-flooding which would submerge lower buckets and create drag.
- **Power output**: 3-15+ HP for typical installations. Exceptional historical wheels reached 50-60 HP.
- **Advantages**: Highest efficiency of all water wheels, relatively constant power output if pond level is maintained, works well even with variable stream flow (pond acts as buffer).
- **Limitations**: Requires significant head (at least 2-3 m, ideally 4-8 m). Needs a dam or weir to create the mill pond. More complex civil engineering (headrace, sluice, tailrace). Vulnerable to floods and ice damage.

### Dam and Mill Pond Construction

**Dam basics** (creating the head and pond):
- **Earth dam** (simplest): Compacted clay core with earth and stone shoulders. Height 2-5 m, crest width 2-3 m, upstream slope 1:2 (horizontal:vertical), downstream slope 1:2.5. Puddle clay core (0.5-1 m thick) keyed into natural subsoil to prevent seepage. Overflow spillway on one side to pass flood water safely.
- **Timber crib dam**: Log cribs (rectangular timber frames) filled with stone, stacked and pinned. Cross-planks on upstream face sealed with clay. Suitable for heads of 2-4 m. Easier to build than masonry in forested areas.
- **Masonry dam**: Stone blocks laid in lime or cement mortar on bedrock. Requires quarry stone, masonry skills, and cement. For heads 3-8 m. Longest-lasting option.
- **Mill pond**: Storage volume to buffer flow variability. Even a small pond (50-200 m³) allows the wheel to run at full power during brief low-flow periods. Intake screen (timber bar rack with 5-10 cm spacing) prevents debris from entering the headrace.

### Water Turbines

Water turbines replace water wheels where higher heads and efficiencies are available. They rotate faster (100-1000+ RPM vs. 5-20 RPM for wheels) and are far more compact for equivalent power. Turbines require iron or steel construction and precision machining — they are a post-water-wheel technology dependent on `machine-tools`.

**Pelton wheel** (impulse turbine — high head, low flow):
- **Principle**: One or more water jets from a nozzle strike spoon-shaped buckets on the runner perimeter. The jet's kinetic energy transfers to the bucket — all pressure conversion happens at the nozzle, not in the runner. Runner operates in air (not submerged).
- **Head range**: 30-1000+ m. Best suited for mountain streams with steep gradients.
- **Efficiency**: Up to 85-91% at design flow.
- **Construction**: Cast iron or bronze runner with forged steel buckets. Buckets split the jet in half (splitter ridge) and redirect it ~165° for maximum momentum transfer. Nozzle diameter 5-50 mm, jet velocity = √(2gH) — at 100 m head, jet velocity ~44 m/s. Often multiple nozzles (2-6) on a single runner for more power at partial flow.
- **Power output**: 1-500+ HP. Small units (5-20 HP) are practical for mountainous sites.
- **Advantages**: Excellent for high-head, low-flow sites. Simple, robust, tolerant of debris (large buckets don't clog easily). Easy to govern (deflect jet or vary nozzle opening).

**Francis turbine** (reaction turbine — medium head, medium flow):
- **Principle**: Water enters the runner radially from a spiral casing (volute), passes through adjustable guide vanes (wicket gates) that direct flow at the optimal angle, then flows through the runner blades and exits axially via the draft tube. Both pressure and velocity drop across the runner — a true reaction machine.
- **Head range**: 3-300 m. The most versatile turbine type.
- **Efficiency**: 80-94% at design flow.
- **Construction**: Cast iron or steel spiral casing, adjustable bronze or steel guide vanes, cast steel runner with complex curved blades, steel draft tube. Requires precision casting and machining — the runner blade profiles must be accurate within ~1 mm for good efficiency. Wicket gate mechanism allows flow regulation for speed control.
- **Power output**: 10-100,000+ HP (scalable from small installations to major hydroelectric stations).
- **Advantages**: Highest efficiency of any hydraulic turbine at design point, excellent speed regulation via wicket gates, wide operating range. The dominant turbine for hydroelectric generation.
- **Limitations**: Complex construction requiring precision manufacturing. Susceptible to cavitation if draft tube submergence is insufficient. Not practical without iron/steel industry and machine tools.

**Kaplan turbine** (axial-flow reaction turbine — low head, high flow):
- **Principle**: Propeller-type runner with adjustable blade pitch (like an outboard motor running in reverse). Water flows axially through the runner — no radial component. Adjustable blades allow efficient operation over a wide flow range.
- **Head range**: 1-15 m. Designed for large rivers with low dams.
- **Efficiency**: 80-92% at design flow, maintains good efficiency over a wide flow range due to adjustable blades.
- **Construction**: Similar to Francis but with propeller runner. Adjustable blade mechanism (hub contains linkage to rotate blades) requires precision engineering. Steel or cast iron construction throughout.
- **Power output**: 50-100,000+ HP. Typically installed in large run-of-river or low-head dam sites.
- **Advantages**: Excellent for low-head, high-flow sites where Francis turbines would be too large. Adjustable blades maintain efficiency across varying flows. Compact for its power.
- **Limitations**: Requires the most precision manufacturing of any turbine type. Cavitation risk is high at low heads — runner must be set below tailwater level.

### Power Transmission

**Getting rotational power from wheel/turbine to the load:**

- **Direct drive** (simplest): Wheel axle directly drives the load (millstones, saw, etc.) via gears or crank. Load must be adjacent to the wheel. Limited to one or two loads.
- **Flat-rod system** (Stangenkunst — transmitting power over distance): Wooden or iron rods connected in a push-pull arrangement transmit reciprocating motion from water wheel to distant mine pumps or machinery. Rods supported on rocking posts every 10-20 m. Can transmit 5-10 HP over 1-2 km. Used extensively in Central European mining from the 16th century.
- **Rope drive** (transmitting rotation over distance): Endless hemp or wire rope running on grooved pulleys (V-groove for grip). Can transmit 5-50 HP over 100-500 m. Rope speed 10-20 m/s. Sag and stretch require tensioning device. Superseded flat rods for new installations once good rope was available.
- **Line shaft** (distributing power within a building): Horizontal iron shaft (50-100 mm diameter) running the length of the workshop, supported by hung bearings from ceiling joists. Driven by water wheel via bevel gears or belt. Each machine connected by belt drive from countershaft on the line shaft. Cone pulleys on each machine provide 2-4 speed ranges. A single 10 HP water wheel can drive an entire small workshop of 5-8 machines simultaneously via line shaft.

**Belt and gear connections:**
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

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
