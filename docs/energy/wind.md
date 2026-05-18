# Wind Power

> **Node ID**: energy.wind
> **Domain**: [Energy](./)
> **Dependencies**: `foundations`, `metals.copper-bronze` or `metals.iron-steel`
> **Enables**: `energy.steam-power` (millwright skills transfer), `agriculture` (grain milling), `water-systems` (pumping)
> **Timeline**: Years 5-15
> **Outputs**: wind_power, mechanical_rotation, ground_grain, pumped_water

### Overview

Wind power converts kinetic energy of moving air into rotational mechanical work via sails or blades mounted on a rotating shaft. Historically the second major mechanical power source after water (see [Gravity/Water](./gravity.md)), windmills enabled settlement of plains and coasts where flowing water was unavailable. Power available in wind scales with the cube of wind speed — a site with 8 m/s wind delivers almost 5× the power of a 5 m/s site, making site selection critical.

**Wind power density** (power available per unit area swept by the rotor):
- P = 0.5 × ρ × A × v³ × Cp
- Where: ρ = air density (~1.225 kg/m³ at sea level, 15°C), A = swept area (m²), v = wind speed (m/s), Cp = power coefficient (theoretical max 0.593 — the Betz limit)
- Example: 6 m diameter rotor at 7 m/s: A = 28.3 m², P_theoretical = 0.5 × 1.225 × 28.3 × 343 = ~5,950 W. At Cp = 0.25 (typical traditional mill): ~1,490 W (~2 HP)

### Windmill Types

**Post mill** (earliest, simplest — 12th century onward):
- **Structure**: Entire mill body (wooden house containing gears and millstones) sits on a massive vertical wooden post (~0.5-0.8 m diameter oak or chestnut). Body rotates around post to face wind. Four horizontal cross-trees at base support post via quarter-bars and sloping struts.
- **Sails**: 4-8 cloth sails on wooden frames, attached to a horizontal windshaft. Sail span typically 6-12 m (diameter 12-24 m). Rotation: 10-25 RPM depending on wind.
- **Rotation mechanism**: Tail pole extends from rear of mill body. Miller pushes tail pole to rotate entire body around central post. Tack rope and winch assist for larger mills.
- **Power output**: 2-8 HP in good wind (7-10 m/s). Sufficient for one pair of millstones or a small saw.
- **Advantages**: Simple construction, entire mechanism accessible for maintenance, can be built with timber and basic ironwork.
- **Limitations**: Small size limited by structural stability of post, manual wind-tracking is slow and dangerous in storms, entire structure must be shut down and restrained when not in use.

**Tower mill** (improved — 14th century onward):
- **Structure**: Fixed masonry or brick tower (cylindrical or tapered, 6-12 m tall, 4-8 m diameter at base, walls 0.3-0.6 m thick). Only the cap (roof) with attached sails rotates to face wind. Much more stable than post mill — allows larger sails and taller towers for stronger, steadier wind.
- **Cap rotation**: Tail fan (small secondary rotor) or fantail automatically turns cap to face wind. Pre-fantail: manual capstan with chain and worm gear. Fantail (invented 1745): small 6-bladed rotor mounted at 90° to main sails. When wind blows from the side, fantail spins, driving worm gear that rotates cap until fantail faces wind edge-on and stops. Self-regulating.
- **Sails**: 4 sails, span 8-15 m each (diameter 16-30 m). Windshaft of cast iron or forged steel, 0.15-0.25 m diameter, 3-5 m long.
- **Power output**: 5-20 HP at rated wind speed. Can drive 2-3 pairs of millstones simultaneously.
- **Tower height**: Each meter of height above ground gains ~0.1-0.2 m/s wind speed over flat terrain (wind shear effect). Tower mills at 10-15 m effective hub height capture significantly more energy than post mills at 5-8 m.

**Smock mill** (tower mill variant — common for drainage pumping):
- **Structure**: Octagonal (usually) wooden tower clad in weatherboard, with rotating cap. Shaped like a traditional smock — wider at base, tapering to top. Cheaper than masonry tower, lighter on foundations.
- **Primary use**: Water pumping (drainage of lowlands, polders). Scoop wheel or Archimedes screw driven by wind via gear train.
- **Common in**: Netherlands, East Anglia (England). Some drove sawmills or oil presses instead.

### Sail and Blade Design

**Common sail** (cloth on wooden frame — standard for centuries):
- **Frame**: Wooden lattice of spruce or pine, ~1.0-1.5 m wide × 5-12 m long per sail. 4-8 horizontal bars (sail bars) connected to main stock (longitudinal beam bolted to windshaft).
- **Sailcloth**: Hemp or flax canvas, 0.4-0.6 kg/m². Reefed (partially furled) by removing or rolling canvas — miller adjusts sail area to control speed and power in varying wind. Fully reefed in storms to prevent structural damage.
- **Performance**: Cp ≈ 0.15-0.20. Simple, repairable, but inefficient — cloth belly (camber) is uncontrolled and varies with wind load.

**Spring sail** (wooden shutters — 1772, Andrew Meikle):
- **Construction**: Wooden frame divided into 6-8 rectangular panels (shutters) hinged along their top edge. Each shutter connected by linkage to a spring-loaded regulation bar. Shutters open automatically when wind force exceeds spring tension, spilling excess air — self-regulating speed control.
- **Spring tension**: Adjustable via chain from inside mill (no need to stop mill to reef). Response time: shutters begin opening within 1-2 seconds of gust. Prevents overspeeding in gusty conditions.
- **Advantages**: Operate in wider wind range (4-18 m/s vs. 5-12 m/s for common sails), safer in storms, no miller needs to climb sail frame to adjust canvas.
- **Performance**: Cp ≈ 0.20-0.25. More consistent power output.

**Patent sail** (spring sail variant with hinged flaps):
- Each shutter pivots on a central axis. Connected via rods to adjustable spider on windshaft. Allows variable pitch from inside mill — like a giant throttle. Most advanced traditional sail type.

### Wind Speed Measurement and Site Assessment

**Anemometer** (cup anemometer, 1846 — but simpler methods suffice):
- **Basic method**: Wind vane for direction. Beaufort scale estimation by observation (leaves rustle = 1-2 m/s, small branches move = 3-5 m/s, small trees sway = 6-8 m/s, large branches move = 9-12 m/s).
- **Cup anemometer construction**: Three or four hemispherical cups (3-5 cm radius) mounted on arms from a central vertical shaft. Shaft rotation speed proportional to wind speed. Calibrate by carrying in known wind or timing rotation in steady breeze. ~1 rotation/second ≈ 1 m/s (depends on cup size and arm length).
- **Site assessment**: Measure wind at proposed hub height for at least 3-12 months before building. Log daily averages. Minimum viable average: 4-5 m/s for post mill, 5-7 m/s for tower mill (higher investment demands better resource).
- **Terrain effects**: Ridge tops and hilltops accelerate wind (speed-up factor 1.2-1.8×). Valleys channel wind along axis. Forests and buildings create turbulence — site at least 10× height of upwind obstacles away.
- **Prevailing wind**: Determine dominant wind direction(s). Mill must face into prevailing wind for maximum operating hours. Record wind direction with simple vane and counting board.

### Mechanical Power Transmission

**Gear train** (wooden gears — standard technology):
- **Windshaft to vertical shaft**: Brake wheel (large crown gear, 1.5-3 m diameter, cast iron or oak with wooden teeth) on horizontal windshaft meshes with wallower (lantern gear — two flanged discs connected by wooden or iron staves) on vertical main shaft. Gear ratio typically 5:1 to 8:1 — converts slow sail rotation (10-25 RPM) to faster stone speed (60-150 RPM).
- **Gear materials**: Apple, hornbeam, or ironbark teeth for durability (dense, close-grained hardwoods). Iron gear rims possible with metallurgy. Wooden teeth wear and break — expected, designed for easy replacement. Grease with tallow or tar.
- **Upright shaft**: Oak or iron-banded wood, 0.15-0.3 m diameter, supported by stone or iron bearings at bottom (thrust bearing carries entire rotating mass — iron plate on hardwood or stone). Stone neck bearing at top.
- **Sack hoist**: Auxiliary drive from upright shaft via belt or chain to lift grain sacks to top of mill. Saves enormous manual labor.
- **Brake**: Large wooden brake blocks clamping the brake wheel rim. Operated by lever from inside mill. Essential — must stop mill in storms or emergencies.

### Wind Pump (Water Pumping)

**Farm wind pump** (American water-pumping windmill — 1854 onward, but buildable with iron-age technology):
- **Rotor**: Multi-bladed (12-24) steel or wooden vanes on 3-8 m diameter wheel. High starting torque (many blades) — essential for starting a loaded pump. Low tip-speed ratio (~1.0) optimized for torque, not speed.
- **Pump**: Reciprocating piston pump in borehole or well. Pump rod connects to rotor shaft via pitman arm (crank mechanism converting rotary to reciprocating motion). Stroke: 100-200 mm, rate: 10-30 strokes/minute.
- **Output**: 0.5-5 m³/hour depending on wind speed, lift height, and rotor diameter. Typical: 3 m rotor, 10 m lift, 5 m/s wind → ~1 m³/hour.
- **Overspeed protection**: Tail vane hinged with spring or counterweight. Excessive wind pushes rotor out of wind (furling). Returns automatically when wind drops.
- **Critical for**: Drinking water, livestock watering, small-scale irrigation, drainage. Runs unattended for days. No fuel required.

### Construction Sequence

1. **Select site**: Elevated, unobstructed, prevailing wind direction. Measure wind for months if possible.
2. **Build tower/foundation**: Stone or timber. Must withstand full wind load on furled sails — worst case. Guy wires or struts for post mill.
3. **Fabricate windshaft**: Oak trunk (0.2-0.3 m diameter, 3-5 m long) or forged iron. Iron windshaft far superior — stronger, smaller, longer-lived. Requires `metallurgy.iron-steel`.
4. **Build sail frames and install canvas or shutters**: Balance all sails — uneven weight causes destructive vibration.
5. **Install gear train**: Brake wheel on windshaft, wallower on upright shaft. Mesh carefully — backlash causes hammering and rapid wear.
6. **Connect to load**: Millstones, saw, pump, or generator.
7. **Install brake and storm protection**: Non-negotiable. Uncontrolled runaway mill destroys itself in minutes.

### Wind Power Parameters (Quick Reference)

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

---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*

