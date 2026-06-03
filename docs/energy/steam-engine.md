# Steam Engine (Reciprocating)

> **Node ID**: energy.steam-power.steam-engine
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.casting`](../machine-tools/casting.md)
> **Enables**: [`energy.steam-power.steam-turbines`](steam-turbines.md), [`transport.railways`](../transport/railways.md), [`marine.propulsion`](../marine/propulsion.md), [`mining.drilling`](../mining/drilling.md)
> **Timeline**: Years 15-25
> **Outputs**: rotary_mechanical_power, reciprocating_steam_power
> **Critical**: Yes — the reciprocating steam engine is the first practical mechanical prime mover independent of geography; required before steam turbines or large-scale electricity generation

## Principle

A reciprocating steam engine converts the pressure energy of steam into mechanical work through a piston moving in a cylinder. High-pressure steam from a [boiler](boiler.md) enters the cylinder, pushing the piston through its power stroke. The steam is then exhausted — either to atmosphere (non-condensing) or to a condenser that creates vacuum on the exhaust side, increasing the pressure differential and efficiency. A crankshaft and connecting rod convert the piston's linear motion to rotary output.

The governing relationship is: Force = Pressure × Area. A piston of 400 mm diameter at 10 bar steam pressure produces F = 10 × 10⁵ Pa × π × (0.2)² m² ≈ 125,700 N ≈ 12.8 tonnes of force. This force, applied over the stroke length at several cycles per minute, produces continuous rotary power. Efficiency improves with higher boiler pressure, earlier steam cutoff (expansive working), condenser vacuum, and multiple expansion stages.

## Prerequisites

- [Cast iron cylinder](../machine-tools/casting.md) — bored to ±0.1 mm tolerance on a boring machine
- [Wrought iron or steel plate](../metals/iron-steel.md) — for boiler, steam pipes, and structural frame
- [Boiler](boiler.md) — producing steam at 5-15 bar for high-pressure engines, or 0.5-2 bar for early Watt-style engines
- [Boring machine](../machine-tools/machining.md) — for cylinder precision
- [Foundry](../machine-tools/casting.md) — for cylinder block, flywheel, and valve chest castings
- [Lubricants](../chemistry/lubricants.md) — tallow or mineral oil for cylinder and bearing lubrication

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Cast iron cylinder block](../machine-tools/casting.md) | 1 piece | 300-500 mm bore × 400-800 mm stroke, 400-800 kg | Foundry | Steel fabrication (welded, heavier) |
| [Wrought iron or steel piston rod](../metals/iron-steel.md) | 1 piece | 60-120 mm diameter × 1.5-3 m long, turned | Forge/machine shop | None — precision-turned shaft required |
| [Cast iron flywheel](../machine-tools/casting.md) | 1 piece | 1.5-3 m diameter, 500-1500 kg | Foundry | Built-up flywheel (plate + spokes) |
| [Wrought iron or steel connecting rod](../metals/iron-steel.md) | 1 piece | 50-80 mm × 100-150 mm cross-section, forged | Forge | Steel casting |
| [Brass valve fittings](../metals/copper-bronze.md) | 5-10 kg | Steam valve, throttle valve, drain cocks | Foundry | Bronze fittings |
| [Hemp or leather packing](../plants/fiber-plants.md) | 2-5 kg | Piston rings and gland packing | Agriculture | Asbestos rope (historical, avoid) |
| [Wrought iron steam pipes](../metals/iron-steel.md) | 20-50 kg | 50-100 mm bore, flanged joints | Forge/machine shop | Copper pipes (expensive) |
| [Steel bolts and nuts](../metals/fasteners.md) | 10-20 kg | M16-M30, Grade 5.8+ | Machine shop | Riveted joints |
| [Lubricating oil](../chemistry/lubricants.md) | 10-20 liters | Cylinder oil + bearing oil | Chemistry | Tallow (shorter life) |
| [Cast iron bed plate](../machine-tools/casting.md) | 1 piece | 2-4 m × 1-2 m × 100-200 mm thick, 500-2000 kg | Foundry | Fabricated steel frame |

## Construction Steps

### Cylinder and Valve Chest

1. **Cast the cylinder block** in gray cast iron (Grade 20-25). Use a foundry sand mold with a core for the bore. Include integrally cast valve chest, steam inlet, and exhaust ports. Casting weight: 400-800 kg depending on size. Allow 2-3 mm machining allowance on bore.

2. **Bore the cylinder** on a horizontal boring machine to final diameter. Target tolerance: ±0.10 mm cylindricity over full stroke length. Surface finish: Ra 1.6-3.2 μm (the piston packing will conform to surface irregularities, but bore must be round and straight).

3. **Machine the valve chest face** flat for the slide valve or valve cover mounting. Surface finish Ra 3.2 μm. Drill and tap bolt holes on 100-150 mm spacing around the port face perimeter.

4. **Cut steam ports** in the valve face: one admission port and one exhaust port, each approximately 10-15% of bore cross-sectional area. Port edges should be smooth to minimize throttling losses.

### Piston and Running Gear

5. **Turn the piston** from cast iron to fit the bore with 0.20-0.40 mm diametral clearance. Cut two to four ring grooves for hemp packing rings. The piston body should be 50-80 mm thick, lightweight enough to reduce reciprocating mass but rigid under steam pressure.

6. **Forge the piston rod** from wrought iron or medium-carbon steel (1045). Turn to final diameter, thread both ends (one for piston attachment, one for crosshead). Surface finish: Ra 0.8 μm on the gland sealing area.

7. **Fabricate the crosshead** from cast iron or steel. Bore for piston rod fit, machine flat slides on either side for crosshead guide. Crosshead pin diameter: 40-80 mm, hardened and ground.

8. **Forge the connecting rod** from wrought iron or steel. Big end bore for crankpin: 60-100 mm diameter, split for bearing insertion. Small end bore for crosshead pin. Length: 2-4× the stroke. Machine bearing surfaces and drill for lubrication passages.

### Crankshaft and Flywheel

9. **Forge or build up the crankshaft**. For smaller engines (<50 HP), forge from a single billet of medium-carbon steel with a crank throw equal to half the stroke. For larger engines, build up from separate crank web forgings and a crankpin, shrunk and keyed together. Crankpin diameter: 80-150 mm, hardened to HRC 40-50.

10. **Turn the main bearing journals** on a lathe to ±0.05 mm tolerance. Surface finish: Ra 0.8 μm. Install in split bearing housings with babbitt-lined shells. Bearing clearance: 0.1% of shaft diameter.

11. **Mount the flywheel** on the crankshaft using a keyed shrink fit. The flywheel stores energy during the power stroke and returns it during the exhaust and return strokes, maintaining smooth rotation. Flywheel weight: 500-1500 kg depending on engine size and speed.

### Valve Gear and Governor

12. **Install the slide valve or piston valve** in the valve chest. A simple D-slide valve (cast iron, lap-fitted to port face) moves back and forth, alternately opening steam and exhaust ports. For higher efficiency, use a Corliss rotary valve gear with separate admission and exhaust valves at each cylinder end.

13. **Mount the eccentric(s)** on the crankshaft to drive the valve. One eccentric for single-acting (simple forward/reverse), two eccentrics for double-acting with Stephenson valve gear. Eccentric throw: 25-50 mm, keyed to shaft.

14. **Install the centrifugal governor** (flyball type). Two rotating balls on hinged arms, driven from the crankshaft via bevel gears or belt. As speed increases, balls swing outward, raising a sleeve that partially closes the throttle valve. Calibrate by adjusting the spring or counterweight to maintain rated speed within ±5%.

### Assembly and Steam Connections

15. **Mount the cylinder on the bedplate** with the crankshaft main bearings aligned. Use a machinist's level to verify that the cylinder bore is parallel to the crankshaft axis within 0.05 mm/m. Shim as needed.

16. **Install the crosshead guides** and verify that the piston rod moves through the gland packing without binding through the full stroke. Adjust guide alignment until crosshead slides freely.

17. **Connect the steam supply** from the [boiler](boiler.md) via a throttle valve and steam pipe (50-100 mm bore, rated for 1.5× working pressure). Install a drain cock at the lowest point of the steam pipe to remove condensate before starting.

18. **Install the exhaust system** — either a pipe to atmosphere (non-condensing, simpler) or a connection to a surface condenser (condensing, higher efficiency). For condensing operation, see [Steam Turbines](steam-turbines.md) for condenser design.

19. **Pressure-test the entire steam side** at 1.5× working pressure with the throttle valve open and cylinder disconnected. Verify no leaks at flanges, valve chest cover, and gland packing.

## Calibration and Verification

1. **Bar the engine over** by hand (using a bar in the flywheel spoke holes). The engine must rotate through the full 360° without binding. If resistance is felt, locate and correct the interference before applying steam.

2. **Check valve timing**: With the flywheel at top dead center (TDC), the steam admission port should begin to open. Adjust the eccentric position on the crankshaft to achieve correct admission timing. Verify cutoff occurs at the design point (typically 25-50% of stroke for expansive working).

3. **First steam test**: Open drain cocks. Crack the throttle valve to admit low-pressure steam. The engine should rotate slowly, with condensate blowing out of drain cocks. When drains blow clear steam (cylinder is warm), close drain cocks and gradually open throttle to full.

4. **Measure speed**: Use a tachometer to verify the engine runs at rated speed (typically 100-300 RPM for stationary engines). Adjust governor spring to set the desired speed. Speed regulation should be within ±5% from no-load to full-load.

5. **Check bearing temperatures** after 30 minutes of running at full load. Babbitt bearing temperatures should not exceed 80°C. Hot bearings indicate misalignment, insufficient clearance, or inadequate lubrication.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Power output (50 HP class) | 30-55 kW (40-70 HP) |
| Operating speed | 100-300 RPM |
| Steam pressure (early Watt) | 0.5-2 bar |
| Steam pressure (high-pressure) | 5-15 bar |
| Thermal efficiency (single-expansion) | 5-8% |
| Thermal efficiency (compound) | 8-12% |
| Steam consumption | 8-15 kg/HP-hour (non-condensing), 5-8 kg/HP-hour (condensing) |
| Cylinder bore | 200-800 mm (design-dependent) |
| Stroke | 300-1500 mm (design-dependent) |
| Flywheel diameter | 1.5-3 m |
| Dry weight (complete engine) | 3-15 tonnes |
| Service life before major overhaul | 10,000-30,000 hours |

## Strengths

- Burns any fuel — coal, wood, oil, gas, agricultural waste — unlike internal combustion engines that require refined fuel
- External combustion allows continuous, clean burning at optimal conditions
- High starting torque — full torque at zero speed, ideal for driving machinery from rest
- Simplicity at low pressures — early atmospheric and Watt-style engines require only basic foundry and boring capability

## Weaknesses

- Low power-to-weight ratio (0.01-0.05 kW/kg) — far heavier than internal combustion or electric motors for equivalent power
- Slow startup — 30 minutes to several hours to raise steam from cold
- Requires continuous boiler attention — water level, fuel feed, pressure monitoring
- Low thermal efficiency (5-12%) compared to steam turbines (30-40%) or diesel engines (35-45%)

## Safety

- **Boiler explosion**: The engine is only as safe as its boiler. A boiler at 10 bar stores enough energy to level a building. Never operate with defective safety valves or low water. See [Boiler](boiler.md) for detailed boiler safety procedures.
- **Steam burns**: Steam at working pressure (150-200°C) causes instantaneous third-degree burns. Insulate all steam pipes. Never open a steam valve without verifying the downstream system is prepared.
- **Rotating machinery**: The flywheel and crankshaft have enormous rotational inertia. Loose clothing, tools, or body parts caught in the rotating mechanism cause severe injury. Guard all moving parts. Never reach into the engine while it is running.
- **Blowdown scalding**: Blowdown water from the boiler is at boiling temperature. Discharge blowdown to a safe drain, never onto the floor.

## See Also

- [Steam Power](steam-power.md) — overview of steam power systems, engine types, and efficiency improvements
- [Boiler](boiler.md) — boiler construction for steam supply
- [Steam Turbines](steam-turbines.md) — turbine replacement for reciprocating engines in power generation
- [Electricity Generation](electricity.md) — generators driven by steam engines
- [Iron & Steel](../metals/iron-steel.md) — materials for engine construction
- [Casting](../machine-tools/casting.md) — cylinder block and flywheel casting
- [Machining](../machine-tools/machining.md) — precision boring of cylinders

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
