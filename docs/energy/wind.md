# Wind Power

> **Node ID**: energy.wind
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`chemistry.lubricants`](../chemistry/lubricants.md), `textiles`
> **Enables**: [`energy.storage`](storage.md), [`energy.electricity`](electricity.md)
> **Timeline**: Years 5-15
> **Outputs**: wind_power, mechanical_rotation, ground_grain, pumped_water
> **Critical**: No — wind supplements water and steam power; wind variability limits reliability without storage or complementary sources

Wind power converts kinetic energy of moving air into rotational mechanical work via sails or blades mounted on a rotating shaft. Historically the second major mechanical power source after water (see [Gravity/Water](./gravity.md)), windmills enabled settlement of plains and coasts where flowing water was unavailable. Power available in wind scales with the cube of wind speed — a site with 8 m/s wind delivers almost 5× the power of a 5 m/s site, making site selection critical.

**[Wind power density](../glossary/wind-power-density.md)** (power available per unit area swept by the rotor):
- P = 0.5 × ρ × A × v³ × Cp
- Where: ρ = air density (~1.225 kg/m³ at sea level, 15°C), A = swept area (m²), v = wind speed (m/s), Cp = power coefficient (theoretical max 0.593 — the Betz limit)
- Example: 6 m diameter rotor at 7 m/s: A = 28.3 m², P_theoretical = 0.5 × 1.225 × 28.3 × 343 = ~5,950 W. At Cp = 0.25 (typical traditional mill): ~1,490 W (~2 HP)

## Prerequisites

- [Lubricants](../chemistry/lubricants.md) — bearing lubrication for rotating machinery
- [Textiles](../textiles/index.md) — sail cloth for traditional windmills
- [Iron & Steel](../metals/iron-steel.md) — shafts, gears, and tower construction

## Windmill Types

**[Post mill](../glossary/post-mill.md)** (earliest, simplest — 12th century onward):
- **Structure**: Entire mill body (wooden house containing gears and millstones) sits on a massive vertical wooden post (~0.5-0.8 m diameter oak or chestnut). Body rotates around post to face wind. Four horizontal cross-trees at base support post via quarter-bars and sloping struts.
- **Sails**: 4-8 cloth sails on wooden frames, attached to a horizontal windshaft. Sail span typically 6-12 m (diameter 12-24 m). Rotation: 10-25 RPM depending on wind.
- **Rotation mechanism**: Tail pole extends from rear of mill body. Miller pushes tail pole to rotate entire body around central post. Tack rope and winch assist for larger mills.
- **Power output**: 2-8 HP in good wind (7-10 m/s). Sufficient for one pair of millstones or a small saw.
- **Advantages**: Simple construction, entire mechanism accessible for maintenance, can be built with timber and basic ironwork.
- **Limitations**: Small size limited by structural stability of post, manual wind-tracking is slow and dangerous in storms, entire structure must be shut down and restrained when not in use.

**Strengths**:
- Simplest windmill to build — timber and basic ironwork only
- Entire mechanism accessible for maintenance from inside the mill body
- Can be rotated to face any wind direction via tail pole

**Weaknesses**:
- Structural stability limits size — post mills rarely exceed 8 HP
- Manual wind-tracking is slow and dangerous in storms
- Entire structure must be shut down and restrained in high winds

**[Tower mill](../glossary/tower-mill.md)** (improved — 14th century onward):
- **Structure**: Fixed masonry or brick tower (cylindrical or tapered, 6-12 m tall, 4-8 m diameter at base, walls 0.3-0.6 m thick). Only the cap (roof) with attached sails rotates to face wind. Much more stable than post mill — allows larger sails and taller towers for stronger, steadier wind.
- **Cap rotation**: Tail fan (small secondary rotor) or fantail automatically turns cap to face wind. Pre-fantail: manual capstan with chain and worm gear. Fantail (invented 1745): small 6-bladed rotor mounted at 90° to main sails. When wind blows from the side, fantail spins, driving worm gear that rotates cap until fantail faces wind edge-on and stops. Self-regulating.
- **Sails**: 4 sails, span 8-15 m each (diameter 16-30 m). Windshaft of cast iron or forged steel, 0.15-0.25 m diameter, 3-5 m long.
- **Power output**: 5-20 HP at rated wind speed. Can drive 2-3 pairs of millstones simultaneously.
- **Tower height**: Each meter of height above ground gains ~0.1-0.2 m/s wind speed over flat terrain (wind shear effect). Tower mills at 10-15 m effective hub height capture significantly more energy than post mills at 5-8 m.

**Strengths**:
- Fixed tower is structurally stable — allows larger sails and taller towers for more power
- Fantail mechanism provides automatic wind-tracking without operator intervention
- Multiple pairs of millstones (2-3) can be driven simultaneously

**Weaknesses**:
- Masonry tower requires brick or stone construction skills — more resource-intensive than post mill
- Cap rotation mechanism (worm gear, fantail) adds mechanical complexity
- Tall tower is a lightning strike target — requires grounding

**[Smock mill](../glossary/smock-mill.md)** (tower mill variant — common for drainage pumping):
- **Structure**: Octagonal (usually) wooden tower clad in weatherboard, with rotating cap. Shaped like a traditional smock — wider at base, tapering to top. Cheaper than masonry tower, lighter on foundations.
- **Primary use**: Water pumping (drainage of lowlands, polders). Scoop wheel or Archimedes screw driven by wind via gear train.
- **Common in**: Netherlands, East Anglia (England). Some drove sawmills or oil presses instead.

## Sail and Blade Design

**[Common sail](../glossary/common-sail.md)** (cloth on wooden frame — standard for centuries):
- **Frame**: Wooden lattice of spruce or pine, ~1.0-1.5 m wide × 5-12 m long per sail. 4-8 horizontal bars (sail bars) connected to main stock (longitudinal beam bolted to windshaft).
- **Sailcloth**: Hemp or flax canvas, 0.4-0.6 kg/m². Reefed (partially furled) by removing or rolling canvas — miller adjusts sail area to control speed and power in varying wind. Fully reefed in storms to prevent structural damage.
- **Performance**: Cp ≈ 0.15-0.20. Simple, repairable, but inefficient — cloth belly (camber) is uncontrolled and varies with wind load.

**[Spring sail](../glossary/spring-sail.md)** (wooden shutters — 1772, Andrew Meikle):
- **Construction**: Wooden frame divided into 6-8 rectangular panels (shutters) hinged along their top edge. Each shutter connected by linkage to a spring-loaded regulation bar. Shutters open automatically when wind force exceeds spring tension, spilling excess air — self-regulating speed control.
- **Spring tension**: Adjustable via chain from inside mill (no need to stop mill to reef). Response time: shutters begin opening within 1-2 seconds of gust. Prevents overspeeding in gusty conditions.
- **Advantages**: Operate in wider wind range (4-18 m/s vs. 5-12 m/s for common sails), safer in storms, no miller needs to climb sail frame to adjust canvas.
- **Performance**: Cp ≈ 0.20-0.25. More consistent power output.

**[Patent sail](../glossary/patent-sail.md)** (spring sail variant with hinged flaps):
- Each shutter pivots on a central axis. Connected via rods to adjustable spider on windshaft. Allows variable pitch from inside mill — like a giant throttle. Most advanced traditional sail type.

## Wind Speed Measurement and Site Assessment

**[Anemometer](../glossary/anemometer.md)** (cup anemometer, 1846 — but simpler methods suffice):
- **Basic method**: Wind vane for direction. Beaufort scale estimation by observation (leaves rustle = 1-2 m/s, small branches move = 3-5 m/s, small trees sway = 6-8 m/s, large branches move = 9-12 m/s).
- **Cup anemometer construction**: Three or four hemispherical cups (3-5 cm radius) mounted on arms from a central vertical shaft. Shaft rotation speed proportional to wind speed. Calibrate by carrying in known wind or timing rotation in steady breeze. ~1 rotation/second ≈ 1 m/s (depends on cup size and arm length).
- **Site assessment**: Measure wind at proposed hub height for at least 3-12 months before building. Log daily averages. Minimum viable average: 4-5 m/s for post mill, 5-7 m/s for tower mill (higher investment demands better resource).
- **Terrain effects**: Ridge tops and hilltops accelerate wind (speed-up factor 1.2-1.8×). Valleys channel wind along axis. Forests and buildings create turbulence — site at least 10× height of upwind obstacles away.
- **Prevailing wind**: Determine dominant wind direction(s). Mill must face into prevailing wind for maximum operating hours. Record wind direction with simple vane and counting board.

## Mechanical Power Transmission

**[Gear train](../glossary/gear-train.md)** (wooden gears — standard technology):
- **Windshaft to vertical shaft**: Brake wheel (large crown gear, 1.5-3 m diameter, cast iron or oak with wooden teeth) on horizontal windshaft meshes with wallower (lantern gear — two flanged discs connected by wooden or iron staves) on vertical main shaft. Gear ratio typically 5:1 to 8:1 — converts slow sail rotation (10-25 RPM) to faster stone speed (60-150 RPM).
- **Gear materials**: Apple, hornbeam, or ironbark teeth for durability (dense, close-grained hardwoods). Iron gear rims possible with metallurgy. Wooden teeth wear and break — expected, designed for easy replacement. Grease with tallow or tar.
- **Upright shaft**: Oak or iron-banded wood, 0.15-0.3 m diameter, supported by stone or iron bearings at bottom (thrust bearing carries entire rotating mass — iron plate on hardwood or stone). Stone neck bearing at top.
- **Sack hoist**: Auxiliary drive from upright shaft via belt or chain to lift grain sacks to top of mill. Saves enormous manual labor.
- **Brake**: Large wooden brake blocks clamping the brake wheel rim. Operated by lever from inside mill. Essential — must stop mill in storms or emergencies.

## Wind Pump (Water Pumping)

**[Farm wind pump](../glossary/farm-wind-pump.md)** (American water-pumping windmill — 1854 onward, but buildable with iron-age technology):
- **Rotor**: Multi-bladed (12-24) steel or wooden vanes on 3-8 m diameter wheel. High starting torque (many blades) — essential for starting a loaded pump. Low tip-speed ratio (~1.0) optimized for torque, not speed.
- **Pump**: Reciprocating piston pump in borehole or well. Pump rod connects to rotor shaft via pitman arm (crank mechanism converting rotary to reciprocating motion). Stroke: 100-200 mm, rate: 10-30 strokes/minute.
- **Output**: 0.5-5 m³/hour depending on wind speed, lift height, and rotor diameter. Typical: 3 m rotor, 10 m lift, 5 m/s wind → ~1 m³/hour.
- **Overspeed protection**: Tail vane hinged with spring or counterweight. Excessive wind pushes rotor out of wind (furling). Returns automatically when wind drops.
- **Critical for**: Drinking water, livestock watering, small-scale irrigation, drainage. Runs unattended for days. No fuel required.

## Construction Sequence

1. **Select site**: Elevated, unobstructed, prevailing wind direction. Measure wind for months if possible.
2. **Build tower/foundation**: Stone or timber. Must withstand full wind load on furled sails — worst case. Guy wires or struts for post mill.
3. **Fabricate windshaft**: Oak trunk (0.2-0.3 m diameter, 3-5 m long) or forged iron. Iron windshaft far superior — stronger, smaller, longer-lived. Requires `metals.iron-steel`.
4. **Build sail frames and install canvas or shutters**: Balance all sails — uneven weight causes destructive vibration.
5. **Install gear train**: Brake wheel on windshaft, wallower on upright shaft. Mesh carefully — backlash causes hammering and rapid wear.
6. **Connect to load**: Millstones, saw, pump, or generator.
7. **Install brake and storm protection**: Non-negotiable. Uncontrolled runaway mill destroys itself in minutes.

## Wind Power Parameters (Quick Reference)

| Parameter | Post Mill | Tower Mill | Wind Pump |
|-----------|-----------|------------|-----------|
| Rotor diameter | 12-24 m | 16-30 m | 3-8 m |
| Hub height | 5-8 m | 10-15 m | 6-12 m |
| Rated wind speed | 8-10 m/s | 8-12 m/s | 6-8 m/s |
| Cut-in wind speed | 4-5 m/s | 4-5 m/s | 3-4 m/s |
| Power output | 2-8 HP | 5-20 HP | 0.2-2 HP |
| Rotation speed | 10-25 RPM | 10-20 RPM | 15-40 RPM |
| Useful wind range | 5-14 m/s | 5-18 m/s | 3-12 m/s |
| Primary load | Grain milling | Multi-purpose | Water pumping |


## Safety & Hazards

- **Structural failure**: Windmill towers and rotors are subject to extreme forces in high winds. Overspeed in storms can destroy rotors and throw debris hundreds of meters. Furling mechanism (turns rotor out of wind) or brakes must be functional. Never approach a windmill in high winds.
- **Height hazards**: Windmill towers require climbing for maintenance. Fall protection needed. Ladders with rest platforms every 10m. Never climb in icy or high-wind conditions.
- **Rotating machinery**: Windmill main shaft, gear train, and machinery move with significant force. Guard all rotating components. Disconnect or brake before maintenance.
- **Lightning**: Tall windmill towers attract lightning. Ground the structure. Do not approach during electrical storms.

## Blade and Sail Construction Detail

**Wooden frame sail**: The traditional windmill sail is built around a spruce spar (the main longitudinal member), typically 50 × 75 mm cross-section for a 5 m blade length. Horizontal sail bars (roughly 25 × 50 mm, spaced 400-600 mm apart) are mortised through or bolted to the spar, creating a ladder-like frame. Canvas or hemp sailcloth is laced or nailed to this frame. The cloth is tensioned with ropes threaded through grommets, allowing the miller to adjust the camber (belly) of the sail. Angle of attack is set at 5-15° relative to the plane of rotation and can be adjusted by spring or counterweight mechanisms that allow the sail to feather (turn parallel to the wind) in gusts.

**Sailcloth weight and durability**: Standard hemp or flax canvas weighs 0.4-0.6 kg/m² and lasts 2-5 years before UV degradation and fatigue require replacement. Cotton canvas is lighter but degrades faster. Sailcloth must be kept dry when the mill is idle to prevent rot. Tarred sailcloth (painted with pine tar or linseed oil) lasts longer but is heavier and stiffer.

**Spring-loaded regulation**: The spring sail (invented 1772) replaces canvas with wooden shutters hinged along their top edge. Each shutter is connected by iron linkage rods to a longitudinal batten, which is spring-loaded. When wind pressure on a shutter exceeds the spring tension, the shutter opens, spilling excess air. The spring tension is adjustable from inside the mill, so the miller can regulate speed without stopping or climbing the sails. Response time: 1-2 seconds.

## Tower Mill Construction

**Tower structure**: A brick or stone tower 8-15 m tall, tapering from 4-8 m diameter at the base to 3-5 m at the cap curb (the circular track on which the cap rotates). Wall thickness: 0.3-0.6 m at the base, thinning to 0.2-0.4 m at the top. The tower must be plumb and the cap curb perfectly level and circular for smooth cap rotation. Brick towers used English bond or Flemish bond for structural strength. Stone towers used dressed ashlar or rubble masonry with lime mortar.

**Cap rotation mechanism**: The cap sits on a curb (a cast iron or oak ring) and rotates on wooden rollers or greased iron slipper bearings. A tail pole extends from the rear of the cap down to ground level. The miller pushes the tail pole to rotate the entire cap into the wind. For larger towers, a capstan (vertical winch) with chain and worm gear provides mechanical advantage. The fantail (invented 1745) automates this: a small 6-bladed rotor at 90° to the main sails drives a worm gear that turns the cap. When the cap is properly aligned, the fantail faces the wind edge-on and stops. Any cross-wind spins the fantail and corrects the alignment.

**Wooden gear mechanism inside the tower**: The brake wheel (large crown gear, 1.5-3 m diameter) is mounted on the horizontal windshaft. It meshes with the wallower (a lantern pinion) on the vertical upright shaft. Below, the great spur wheel (another large crown gear on the upright shaft) drives the stone nuts (smaller gear wheels directly above each pair of millstones). Each stone nut can be engaged or disengaged independently via a tampian bar (lighting gear), allowing the miller to run one, two, or three pairs of stones depending on available wind power.

## Water Pumping Windmill Detail

**Halladay pattern (1854)**: The classic American farm windmill, designed by Daniel Halladay. The multiblade rotor consists of 15-30 flat or slightly curved steel (or wooden) vanes mounted on a lattice frame. Rotor diameter 3-8 m. The high number of blades gives a high starting torque, essential for starting a reciprocating pump under load. Low tip-speed ratio (~1.0, compared to 5-7 for electricity-generating rotors) means the wheel turns slowly but powerfully.

**Starting performance**: The multiblade rotor starts reliably in winds as low as 3 m/s. This low cut-in speed is important for water pumping, where continuous operation at low wind speeds delivers more total water over a season than a high-performance rotor that only works in strong winds.

**Pumping capacity**: A 3 m diameter Halladay windmill at 5 m/s wind speed pumps roughly 500 L/hour from a 10 m lift. A 6 m diameter unit at 6 m/s pumps roughly 3,000-5,000 L/hour from a 20 m lift. The gearbox provides a 3.5:1 ratio, converting the slow rotor rotation (15-40 RPM) to a faster crank speed for the pump. Pump stroke: 100-200 mm. Pump cylinder diameter: 50-150 mm depending on required flow and lift.

**Overspeed protection**: The tail vane is hinged and spring-loaded. In normal wind, the tail holds the rotor perpendicular to the wind. When wind speed exceeds the safe operating range (typically 12-15 m/s), the wind force on the offset rotor pushes the rotor out of the wind (furling), reducing the swept area presented to the wind. The spring tension determines the furling speed. The rotor returns to face the wind automatically when the wind drops.

## Wind Resource Assessment

**Power in the wind**: The fundamental relationship is P = 0.5 × ρ × A × v³ × Cp. Air density ρ = 1.225 kg/m³ at sea level and 15°C (decreasing with altitude and temperature). The cubic dependence on wind speed means small increases in wind speed produce large increases in power. A site with 8 m/s average wind delivers (8/5)³ = 4.1× the power of a 5 m/s site.

**Betz limit**: No wind rotor can extract more than 16/27 (59.3%) of the kinetic energy in the wind. This is because the wind must retain enough kinetic energy to flow away from the rotor and make room for incoming air. Practical traditional windmills achieve Cp = 0.15-0.30, well below the Betz limit. Modern wind turbines with optimized airfoil blades reach Cp = 0.40-0.50.

**Wind speed distribution**: Wind speed at any site follows a Weibull distribution (a skewed probability distribution). The mean wind speed is not the most common speed; the most probable speed is typically 70-80% of the mean. Typical inland mean speeds: 4-8 m/s. Coastal and ridge-top sites: 7-12 m/s. The Weibull shape parameter (k) describes the spread: k ≈ 2 (Rayleigh distribution) is typical for many inland sites. A site with mean 6 m/s and k = 2 has a most probable wind speed of about 4.8 m/s and delivers wind above 3 m/s roughly 75% of the time.

**Wind measurement protocol**: Measure wind speed at the proposed hub height for at least 3-12 months using a cup anemometer and data logger. Shorter measurement periods risk missing seasonal variations. Compare measurements against a nearby long-term reference station to correct for atypical years. The economic viability of a wind power installation depends critically on the actual wind resource, which cannot be estimated reliably from maps or casual observation.

## Storm Protection Methods

**Turning sails parallel to wind**: The oldest method of storm protection. In a post mill, the miller turns the entire mill body so the sail frame faces edge-on to the wind. In a tower mill, the cap is rotated to point the sails away from the wind. This must be done before the storm arrives. Once the wind is at storm force, manual rotation becomes impossible.

**Spring-loaded folding mechanism**: Spring sails and patent sails provide automatic protection. Each shutter or blade panel is spring-loaded to open when wind force exceeds the spring tension. In a violent gust, all shutters open simultaneously, spilling the wind through the sail frame rather than catching it. The mill continues to turn slowly but the driving force is greatly reduced.

**Mechanical brake band**: A friction brake (wooden or iron brake blocks clamping the brake wheel rim) provides positive stopping. The brake is operated by a lever inside the mill, typically with a screw or ratchet mechanism to hold it engaged. The brake must be strong enough to hold the windshaft stationary in a full gale with furled sails. If the brake fails and the sails are caught in a storm, the only recourse is to cut the sail frames away with axes before the mill destroys itself.

## Blade and Sail Construction Detail

**Wooden frame sail**: The traditional sail is built around a spruce spar (50 × 75 mm cross-section for a 5 m blade). Horizontal sail bars (25 × 50 mm, spaced 400-600 mm) are mortised through the spar, creating a ladder-like frame. Canvas or hemp sailcloth is laced to this frame and tensioned with ropes through grommets. Angle of attack: 5-15° relative to the rotation plane, adjustable by spring or counterweight mechanisms that feather the sail in gusts.

**Sailcloth**: Standard hemp or flax canvas, 0.4-0.6 kg/m², lasts 2-5 years before UV degradation. Tarred canvas lasts longer but is heavier and stiffer. Must be kept dry when idle to prevent rot.

## Tower Mill Construction

**Tower structure**: Brick or stone, 8-15 m tall, tapering from 4-8 m diameter at base to 3-5 m at the cap curb. Wall thickness: 0.3-0.6 m at base, thinning to 0.2-0.4 m at top. The cap curb must be perfectly level and circular for smooth cap rotation.

**Cap rotation**: The cap sits on a curb and rotates on wooden rollers or greased iron bearings. A tail pole extends to ground level for manual rotation. The fantail (invented 1745) automates this: a small 6-bladed rotor at 90° to the main sails drives a worm gear that rotates the cap to face the wind.

**Internal gear train**: Brake wheel (crown gear, 1.5-3 m diameter) on the windshaft meshes with the wallower (lantern pinion) on the upright shaft. The great spur wheel on the upright shaft drives stone nuts above each pair of millstones. Each stone nut engages or disengages independently, letting the miller run 1-3 pairs of stones depending on wind power.

## Water Pumping Windmill (Halladay Pattern)

**Multiblade rotor**: 15-30 flat or slightly curved vanes on a lattice frame, 3-8 m diameter. High blade count gives high starting torque for starting a loaded pump. Low tip-speed ratio (~1.0) optimized for torque, not speed. Starts reliably in 3 m/s wind.

**Pumping capacity**: A 3 m rotor at 5 m/s pumps roughly 500 L/hour from 10 m lift. A 6 m rotor at 6 m/s pumps 3,000-5,000 L/hour from 20 m lift. Gear ratio 3.5:1. Pump stroke: 100-200 mm. Pump cylinder: 50-150 mm diameter.

**Overspeed protection**: Hinged tail vane with spring. Wind force on the offset rotor pushes it out of the wind above 12-15 m/s (furling). Returns automatically when wind drops.

## Wind Resource Assessment

**Power formula**: P = 0.5 × ρ × A × v³ × Cp. Air density ρ = 1.225 kg/m³ at sea level, 15°C. The cubic dependence on wind speed means an 8 m/s site delivers (8/5)³ = 4.1× the power of a 5 m/s site.

**Betz limit**: Maximum extractable power: Cp = 0.593. Practical traditional mills: Cp = 0.15-0.30. Modern turbines: Cp = 0.40-0.50.

**Wind speed distribution**: Wind follows a Weibull distribution. The most probable speed is typically 70-80% of the mean. Typical inland means: 4-8 m/s. With Rayleigh distribution (k ≈ 2), a 6 m/s mean site delivers wind above 3 m/s roughly 75% of the time.

**Measurement protocol**: Measure at proposed hub height for at least 3-12 months with cup anemometer and data logger. Compare against nearby long-term reference to correct for atypical years.

**Terrain effects**: Ridge tops and hilltops accelerate wind by a factor of 1.2-1.8× due to compression of streamlines. Valleys channel wind along their axis. Forests and buildings create turbulence for 10-20× their height downwind. Wind shear: each meter of height above ground gains roughly 0.1-0.2 m/s over flat terrain due to reduced surface friction. Hub heights of 10-15 m (tower mill) capture significantly more energy than 5-8 m (post mill).

**Seasonal wind patterns**: In temperate latitudes, wind speeds are typically 30-50% higher in winter than in summer due to stronger pressure gradients from greater temperature differences. This seasonal pattern historically matched grain milling demand (harvest in autumn, grinding through winter). For water pumping, the seasonal match is reversed: summer irrigation demand coincides with lower wind speeds, requiring larger rotors or storage tanks to buffer low-wind periods.

**Anemometer calibration**: Cup anemometers require calibration against a known standard. A simple field method: mount the anemometer on a vehicle driven at constant speed on a calm day, recording rotation rate versus vehicle speed. Factor in vehicle speedometer error. Periodic recalibration ensures data reliability for investment decisions.

## Limitations

- **Intermittency**: Wind is variable and unpredictable. Capacity factors typically 20-40% — a 1 MW turbine produces 0.2-0.4 MW on average. Requires energy storage or backup generation.
- **Site dependency**: Wind resources vary dramatically by location. Good sites require annual average wind speeds >6 m/s at hub height. Detailed wind survey (12+ months) needed before investment.
- **Energy storage requirement**: Wind peaks rarely coincide with demand peaks. Without storage (batteries, pumped hydro, hydrogen), excess wind energy is curtailed.
- **Structural loads**: Wind turbines experience extreme cyclic loading. Fatigue failure of blades, tower, and drivetrain is the primary lifetime limiter.
- **Material demands**: Large blades require lightweight composites (fiberglass, carbon fiber). Tower construction uses significant steel and concrete.
- **Noise and visual impact**: Mechanical noise from gearboxes and aerodynamic noise from blade tips. Large turbines visible from considerable distances.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Windmill producing less power than expected | Poor blade angle or low wind speed at hub height | Adjust sail/blade pitch; raise tower height (wind speed increases with height); verify wind survey data |
| Excessive vibration or rumbling | Blade imbalance or bearing wear | Balance blades (add/remove weight); check main shaft bearings; inspect gear teeth for wear |
| Yaw mechanism stuck (not facing wind) | Rust or mechanical seizure in turntable | Lubricate turntable bearing; free seized mechanism; check wind vane linkage |
| Blade fatigue cracking | Cyclic loading exceeding design limits | Reduce operational speed in high winds; add blade tip brakes; inspect blades monthly for crack initiation |
| Generator overheating | Sustained high wind overloading electrical system | Install overspeed protection (mechanical brake, feathering); verify generator rating matches rotor output |
| Tower base corrosion | Moisture accumulation at ground level | Apply protective coating; improve drainage around base; inspect annually and repaint |

## See Also

- [Energy Storage](storage.md) — battery and other storage for intermittent wind power
- [Electricity Generation](electricity.md) — generators and grid integration
- [Pumped Hydro](pumped-hydro.md) — large-scale storage complementary to wind
- [Redox Flow Batteries](sem-tech-redox-flow-batteries.md) — medium-duration grid storage
- [Composites](../polymers/composites.md) — materials for turbine blade construction
- [Gravity & Water](gravity.md) — water power as complementary mechanical energy source

[← Back to Energy](index.md)
