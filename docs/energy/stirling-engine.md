# Stirling Engine

> **Node ID**: energy.stirling-engine
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`machine-tools.machining`](../machine-tools/machining.md), [`metals.casting`](../metals/casting.md), [`chemistry.lubricants`](../chemistry/lubricants.md)
> **Enables**: Small-scale power from any heat source, solar thermal generation, waste heat recovery
> **Timeline**: Years 15-25
> **Outputs**: stirling_mechanical_power, cryocoolers
> **Critical**: No — Stirling engines provide useful small-scale power but are not on the critical path to semiconductor manufacturing

Closed-cycle external combustion engine. Working gas (air, helium, or hydrogen) is permanently sealed inside the engine and alternately heated and cooled. No valves, no explosions, just smooth, quiet operation. Invented by Robert Stirling in 1816, decades before internal combustion engines.

**Principle**: Working gas is shuttled between hot and cold spaces by a displacer. When gas is in the hot space it expands, pushing the power piston. When gas moves to the cold space it contracts, allowing the piston to return. The cycle is thermodynamically reversible. Theoretical efficiency approaches the Carnot limit: η = 1 - T_cold/T_hot.

The regenerator is the key innovation that makes the Stirling cycle practical. It sits between the hot and cold spaces and acts as a thermal sponge. As hot gas flows through it toward the cold side, the regenerator absorbs heat, cooling the gas before it reaches the cold exchanger. When gas flows back toward the hot side, the regenerator returns that stored heat, pre-warming the gas before it reaches the hot exchanger. Without the regenerator, the gas would dump its heat to the cold side and then require the same heat again from the external source, wasting energy and slashing efficiency. A well-designed regenerator recovers 90-95% of the heat that would otherwise be lost in each cycle. Wire mesh (stacked stainless steel screens) or sintered metal matrices provide the high surface area and low flow resistance needed.

## Prerequisites

- [Machine tools](../machine-tools/iterative-bootstrap.md) for cylinder boring and piston fitting
- Basic foundry for cast iron cylinder and displacer
- Sealing capability (lapped piston-cylinder fit)
- Heat exchanger materials (copper or steel tubing)
- Regenerator material (wire mesh or sintered metal)
- [Lubricants](../chemistry/lubricants.md) for piston seal

## Materials

| Material | Quantity | Specification | Source |
|----------|----------|--------------|--------|
| Cast iron | 5-50 kg | For cylinder block, displacer, flywheel | [Casting](../metals/casting.md) |
| Steel bar | 2-10 kg | For crankshaft, connecting rod, piston rod | [Iron & Steel](../metals/iron-steel.md) |
| Stainless steel tubing | 1-5 m | 6-12 mm OD, for heat exchanger tubes | [Iron & Steel](../metals/iron-steel.md) |
| Copper tubing | 1-3 m | 6-10 mm OD, for cold-side heat exchanger | [Copper](../metals/copper.md) |
| Stainless steel wire mesh | 50-200 cm² | 80-200 mesh, for regenerator | [Wire Drawing](../metals/wire-drawing.md) |
| PTFE seal material | 10-50 g | Piston seal rings | [Polymers](../polymers/rubber.md) |
| Graphite powder | 100-500 g | Piston/cylinder lubrication | [Mining](../mining/index.md) |

## Configurations

- **Alpha**: Two separate cylinders, one hot and one cold, each with its own piston. 90° phase angle between pistons. Highest power density but more complex seals at both hot and cold cylinders.
- **Beta**: Single cylinder with displacer and power piston in-line. Displacer moves gas between hot and cold ends; power piston extracts work. Most common configuration for small engines. The displacer and piston share the same bore, simplifying construction.
- **Gamma**: Separate expansion (hot) cylinder and compression (cold) cylinder connected by a displacer. Lower power density but mechanically simple. Often used for low-temperature difference engines where the hot source is only 50-200°C above ambient (solar thermal, waste heat recovery).

## Manufacture

Machine cylinder bore to 25-50 μm tolerance. Fit piston with minimal clearance and a lapped seal. Fabricate hot-side and cold-side heat exchangers with maximum surface area. The hot-side exchanger uses internal fins or narrow tubes to transfer heat from the external source into the working gas. The cold-side exchanger rejects waste heat, often using water cooling for maximum temperature differential. Install regenerator (porous matrix) between hot and cold spaces. Assemble crankshaft, connecting rod, and displacer mechanism. Seal working gas port and charge with working fluid.

**Heat exchanger design**: The heat exchangers are the largest and most expensive components in a Stirling engine, often accounting for 40-60% of the total engine volume and cost. The hot-side exchanger must operate continuously at 500-800°C while transferring heat into the pressurized working gas. Tubular designs (bundles of small-diameter stainless steel or Inconel tubes) are common because they can withstand both the temperature and the internal gas pressure. Finned tubes increase surface area but add manufacturing complexity. The cold-side exchanger has an easier thermal environment but must reject the same total heat flow. Water cooling with a shell-and-tube or plate design is most effective; air cooling with finned surfaces works but requires much more surface area and a fan. The temperature difference between the heat source and the working gas is a direct efficiency loss: every degree of temperature drop across the heat exchanger wall reduces the effective T_hot and therefore the Carnot efficiency. This drives heat exchanger designs toward maximum surface area and minimum wall thickness, within the constraints of pressure containment and mechanical strength.

**Sealing challenges**: The piston seal must contain the working gas at 5-20 MPa pressure while sliding against the cylinder wall with minimal friction. In conventional engines, piston rings seal against the cylinder with combustion gases providing the pressure behind the rings. In a Stirling engine, the working gas pressure acts behind the seal at all times, and the seal must work in both directions (compression and expansion). Several approaches exist: lapped metal piston-cylinder fits (very tight clearance, works at moderate pressure), PTFE-based composite seals (low friction, good sealing, temperature limited to ~260°C), and rolled-sock seals (thin metal diaphragm that flexes to accommodate the piston stroke, completely separating the working gas from the crankcase). Each approach has tradeoffs between leakage rate, friction loss, maximum temperature, and manufacturing difficulty. Seal leakage is the primary cause of long-term efficiency degradation in Stirling engines: as the working gas slowly escapes, the mean pressure drops and power output declines.

## Operating Parameters

Thermal efficiency 5-40% depending on temperature ratio. Key parameter: T_hot/T_cold should be maximized. Typical operating temperatures: 500-800°C hot end, 20-100°C cold end. Power density 10-100x lower than internal combustion engines of similar size. Efficiency improves with higher mean pressure. Helium at 10-20 MPa achieves best results.

External combustion is the defining advantage. Unlike internal combustion engines, the Stirling engine's working gas never contacts combustion products. The heat source warms the hot heat exchanger from outside, and the sealed working gas transfers that thermal energy into mechanical work. Any heat source at sufficient temperature works: concentrated solar, biomass combustion, waste heat from industrial processes, geothermal, even radioisotope decay (as in space probes).

Helium and hydrogen are the preferred working gases due to high thermal conductivity and low viscosity, which minimize heat exchanger losses. Operating pressures of 5-20 MPa mean the engine casing must be a pressure vessel. Air at atmospheric pressure works for simple demonstration engines but produces very low power density, roughly 1/10 the output of helium at equivalent pressure. Hydrogen offers the best thermodynamic performance but permeates steel at high temperature and is flammable if it leaks.

Heater temperature typically 650-800°C, cooler temperature 20-60°C. Theoretical Carnot efficiency for 700°C heater and 40°C cooler: η_Carnot = 1 - 313/973 = 67.8%. Practical Stirling engines achieve 30-40% thermal efficiency, meaning real-world output is roughly half the theoretical maximum. The gap comes from heat exchanger temperature differences, regenerator ineffectiveness, mechanical friction, and pressure drop through heat exchangers.

## Safety & Hazards

> **Safety warning**: Pressurized working gas at up to 20 MPa in high-performance engines with helium or hydrogen. Vessel failure releases high-pressure gas explosively — a 20 MPa vessel rupture produces a blast wave equivalent to 0.5-1.0 kg of TNT per liter of compressed gas volume. Pressure relief valves mandatory on all sealed Stirling systems, set to open at 1.1× maximum allowable working pressure. Hydrogen working fluid is flammable (LEL 4% in air) and permeates many seal materials — a hydrogen leak at 15 MPa ignites from static discharge. Detect and eliminate leaks before pressurizing. Hot end surfaces reach 500-800°C, causing third-degree burns in under 1 second on contact. Hot heat exchangers retain thermal energy for extended periods after shutdown due to thermal inertia of the hot-side mass (a 10 kg cast iron heater head at 700°C stores ~3.5 MJ of thermal energy and takes 2-4 hours to cool below 60°C). Allow full cooling before servicing.

- **Pressure vessel rupture**: The engine cylinder and heat exchanger housings are pressure vessels. At 20 MPa working pressure, a 100 mm bore cylinder has a force of ~160 kN (~16 tonnes) on the cylinder head. The cylinder wall must be designed to withstand this pressure with a 3-4× safety factor. Use forged steel cylinder construction for pressures above 10 MPa. Never weld on a pressurized Stirling engine. Hydrostatic-test the assembled cylinder and heat exchangers at 1.5× working pressure before filling with working gas.
- **Hydrogen embrittlement**: Hydrogen at 500-800°C and 15-20 MPa permeates into steel grain boundaries, causing embrittlement. After 1,000-5,000 hours of operation with hydrogen, the hot-end steel components lose 30-50% of their ductility. Inspect hot-end components for cracking during scheduled overhauls. Use Inconel or stainless steel (austenitic grades resist embrittlement better than ferritic) for hot-end heat exchanger tubes. Never reuse a hydrogen-exposed steel component beyond its certified service life.
- **Crankcase explosion (hydrogen engines)**: If the piston seal leaks hydrogen into the crankcase, a flammable mixture can accumulate. The crankcase is normally at atmospheric pressure, so hydrogen leaking at 15 MPa through a tiny seal gap expands ~150× in volume. A crankcase hydrogen concentration reaching 4% (LEL) can detonate from a spark (bearing, static). Install crankcase hydrogen detectors with alarms at 1% concentration and automatic engine shutdown at 2%. Vent the crankcase continuously with a forced-air purge.
- **Cold-end frostbite**: The cold-side heat exchanger in a Stirling cryocooler (running in reverse) can reach -196°C (liquid nitrogen temperature). Skin contact causes instantaneous frostbite. Handle cold-end components with insulated gloves. Allow the cold end to warm above 0°C before servicing. Never touch a running cryocooler's cold finger.

## Scaling Notes

Stirling engine production scales with precision machining capability:

- **Workshop scale** (1-5 engines/year): Hand-lapped cylinder and piston on a lathe. Cast iron cylinder poured in a small foundry. Copper tubing heat exchangers bent and soldered by hand. Wire mesh regenerator cut from stainless screens. Air at atmospheric pressure as working gas. Power output: 1-50 W. One skilled machinist. Adequate for demonstration, educational, and small solar thermal applications.

- **Engine shop scale** (10-100 engines/year): Precision-bored cylinder on a lathe or boring mill. Helium charge at 2-10 MPa. Brazed stainless steel heat exchanger tubes. Machined regenerator housing. Power output: 100 W - 5 kW. 3-5 workers. This scale supports biomass CHP, small solar generators, and waste heat recovery units.

- **Industrial scale** (limited production): Hydrogen at 15-20 MPa. Investment-cast Inconel heat exchanger heads. Sintered metal regenerator. Power output: 5-100 kW. Requires nickel superalloy capability and advanced seal manufacturing. Used for submarine AIP systems and industrial CHP.

**Critical bottleneck**: Dynamic sealing at high pressure and temperature. The piston seal must hold 5-20 MPa while sliding at speeds of 1-5 m/s. PTFE seals wear out in 200-2,000 hours at these conditions. Metal labyrinth seals leak more but last longer. Seal life is the primary maintenance cost driver for Stirling engines.

## Quality Control

| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Cylinder bore diameter | Inside micrometer at 3 positions | ±25 μm taper and out-of-round over full stroke length |
| Piston-to-cylinder clearance | Dial bore gauge + outside micrometer | 25-50 μm (0.025-0.050 mm) diametral clearance |
| Cylinder bore surface finish | Profilometer | Ra 0.2-0.4 μm for long seal life |
| Heat exchanger leak test | Pressurize to 1.5× working pressure with N₂, hold 30 min | Zero pressure drop |
| Regenerator pressure drop | Differential pressure gauge at design flow | <5% of mean cycle pressure |
| Regenerator effectiveness | Measure temperatures at inlet/outlet on both passes | >90% heat recovery (ideally 95%+) |
| Overall engine leak rate | Helium leak detector on sealed engine | <10⁻⁶ atm·cc/s |
| Crankshaft runout | Dial indicator on mains and crankpin | <0.02 mm total runout |

## Applications

Small-scale solar thermal power generation, biomass combined heat and power (CHP), waste heat recovery, cryocoolers (running in reverse as heat pump), demonstration and educational engines. Stirling engines are also used in submarine propulsion (AIP systems) where silence matters more than power density.

**Strengths**:
- External combustion: any heat source works (solar, biomass, waste heat, geothermal, radioisotope)
- Extremely quiet operation (no combustion explosions)
- High theoretical efficiency approaching Carnot limit
- Can run in reverse as cryocooler or heat pump
- Long service life: no fuel contamination of lubricating oil, no corrosive combustion products inside cylinders
- Achievable with moderate machining capability (lathe, basic foundry)

**Weaknesses**:
- Lower power density and higher weight per kW than IC engines
- Dynamic sealing at high temperature is difficult: leakage reduces efficiency over time
- Slow thermal response to load changes (heat exchangers have thermal inertia)
- Expensive heat exchangers required on both hot and cold sides
- Helium and hydrogen working fluids require high-pressure sealing (hydrogen permeates many materials)
- Regenerator must have high surface area and low pressure drop: wire mesh or sintered metal required

**Free-piston variants**: Some Stirling engine designs use a single piston that serves as both displacer and power piston, eliminating the separate displacer mechanism. These "free-piston" Stirling engines use gas springs and the pressure differential between hot and cold spaces to drive the piston oscillation without a crankshaft. The simplicity is attractive, but tuning the gas spring resonance to match the desired operating frequency requires precise design. Free-piston Stirling engines have been developed for space power applications (radioisotope Stirling generators) where long life and zero maintenance matter more than simplicity of design.

**Working gas selection**: The choice of working gas has a major impact on performance. Air is the simplest choice: free, non-flammable, non-toxic, and compatible with any seal material. But air has relatively high viscosity and low thermal conductivity, which means larger heat exchangers and more friction loss for a given power output. Helium improves both properties significantly and is inert, making it the preferred gas for most practical Stirling engines. Hydrogen offers the best thermodynamic performance of all (lowest viscosity, highest thermal conductivity, highest specific heat ratio) but carries flammability risk if it leaks from the high-pressure casing. Hydrogen also permeates steel at elevated temperature, causing embrittlement over time.

**Ideal Stirling cycle**: The theoretical cycle consists of four processes: (1) isothermal expansion at T_hot, where the gas absorbs heat from the hot source and expands, doing work on the piston; (2) constant-volume (isochoric) cooling as gas passes through the regenerator, depositing heat; (3) isothermal compression at T_cold, where the gas rejects heat to the cold sink and is compressed by the piston; (4) constant-volume heating as gas passes back through the regenerator, recovering stored heat. The theoretical efficiency equals Carnot because heat is added and rejected isothermally. Real engines deviate from the ideal because heat exchangers have finite area, the regenerator has less than 100% effectiveness, and mechanical friction absorbs some of the piston work.

Power modulation in Stirling engines is less responsive than in internal combustion engines. Changing the heat input rate (fuel flow, solar concentration) takes seconds to minutes because heat exchangers have thermal mass. This characteristic makes Stirling engines better suited for steady-load applications than for applications with rapidly varying power demand.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Power output declining over weeks | Working gas (helium or hydrogen at 5-20 MPa) leaking past piston seal; each 1% pressure drop reduces power output proportionally | Pressure-test the sealed crankcase; locate leaks with soap solution at sealed joints. Re-lap piston-cylinder fit (spec 25-50 μm clearance). For hydrogen working fluid, check for steel embrittlement at hot-end temperatures of 500-800°C. Re-pressurize with fresh working gas |
| Engine won't start or produces minimal power | Regenerator fouled or clogged — the porous matrix (wire mesh or sintered metal) between hot and cold spaces has accumulated debris or corrosion products, blocking gas flow | The pressure drop across the regenerator should be <5% of mean cycle pressure. Measure pressure drop with differential gauges. Remove and clean or replace regenerator matrix. For wire mesh regenerators, replace with fresh stainless steel screens (80-200 mesh). A fouled regenerator that has lost 20% of its flow area reduces power output by 30-50% |
| Excessive noise or knocking | Piston-to-cylinder clearance too large — the piston rocks in the bore at each reversal point, producing a metallic knock | Measure bore diameter at three positions and piston diameter. Clearance should be 25-50 μm (0.025-0.050 mm). If clearance exceeds 75 μm, the piston rocks and the seal cannot maintain gas pressure. Re-lap piston and cylinder or install oversize piston with fresh lapping. The lapping compound should be 15-25 μm aluminum oxide for final finish |
| Hot-end heat exchanger tube cracking | Thermal fatigue from repeated heating and cooling cycles — each start/stop cycle thermally shocks the hot-end tubes | Hot-end tubes at 700°C experience thermal expansion of ~8 mm per meter of length. Constrained tubes crack from cyclic strain. Ensure expansion bends or bellows accommodate movement. For tubes that have cracked, weld-repair is temporary — replacement with Inconel 625 or 316L stainless steel tubes is the permanent fix |
| Cold-end overheating (temperature rising above 80°C) | Cooling water flow insufficient or cold-side heat exchanger fouled | The cold side must reject 60-70% of the total heat input. For a 1 kW Stirling engine, the cold side rejects ~600-700 W. Water cooling flow rate needed: ~1 L/min for a 10°C temperature rise. If water flow is adequate, check for scale buildup inside the cold-side heat exchanger tubes and descale with mild acid solution |
| Regenerator effectiveness dropping | Regenerator matrix sintering — at temperatures above 600°C, fine wire mesh screens bond together, reducing surface area and heat storage capacity | Inspect regenerator through access ports. Replace with coarser mesh that resists sintering, or use packed ball-type regenerator (3 mm stainless steel balls). Regenerator effectiveness below 85% warrants replacement |
| Phase angle between displacer and piston incorrect | Phase angle must be ~90° (alpha) or the correct mechanical relationship (beta/gamma) for optimum gas shuttling. Incorrect phase angle reduces power by 30-60% | For alpha configurations, check the timing gears or crank throw angles. For beta/gamma, check the displacer rod linkage length and crankpin position. The optimal phase angle varies: typically 80-100° for maximum power, 110-130° for maximum efficiency |
| Engine stalls when load is applied | Insufficient torque at low speed — Stirling engines have lower torque at startup than at design speed | Reduce the starting load. Apply load gradually after the engine reaches stable operation. Pre-heat the hot end for 10-30 minutes before applying mechanical load |
| Piston seal wear requiring replacement every 200-500 hours | Piston rubbing speed and temperature too high for the seal material. PTFE-based seals degrade above 260°C | Check piston surface finish: Ra 0.2-0.4 μm is required for long seal life. For high-pressure applications (>10 MPa), use filled-PTFE (glass-filled or carbon-filled) seals instead of pure PTFE |

## See Also

- [Heat Engines](engine.md) — overview of all heat engine types
- [Internal Combustion Engines](internal-combustion.md) — Otto and Diesel cycle engines
- [Gas Turbines](gas-turbine.md) — Brayton cycle engines
- [Steam Engine](steam-engine.md) — reciprocating steam engines
- [Solar Thermal](solar-thermal.md) — concentrated solar heat source
- [Lubricants](../chemistry/lubricants.md) — piston seal lubrication
- [Machine Tools](../machine-tools/iterative-bootstrap.md) — machining capability

## Variations and Alternatives

| Stirling Variant | Configuration | Power Output | Working Gas | Best Application |
|-----------------|--------------|-------------|-------------|-----------------|
| Low-temperature delta (LTD) | Gamma, large displacer | 1-50 W | Air, atmospheric | Demonstration, educational, solar pond |
| Small beta | Beta, single cylinder | 10-500 W | Air or helium, 1-5 MPa | Small solar thermal, biomass CHP |
| Medium alpha | Alpha, two cylinders | 500 W - 5 kW | Helium, 5-15 MPa | Waste heat recovery, micro-CHP |
| High-performance | Alpha or beta | 5-100 kW | Hydrogen, 15-20 MPa | Submarine AIP, industrial CHP |
| Free-piston | Beta, no crankshaft | 100 W - 10 kW | Helium, 5-10 MPa | Space power, long-life unmanned stations |
| Cryocooler (reverse) | Any | 1-100 W cooling | Helium, 5-20 MPa | Infrared detector cooling, superconductor cooling |

**Compared to internal combustion**: Stirling engines produce 10-100× less power per unit weight than Otto or Diesel engines. A 1 kW Stirling engine weighs 20-100 kg; a 1 kW gasoline engine weighs 1-5 kg. However, the Stirling's external combustion means it can use any heat source, including concentrated sunlight and waste heat that internal combustion engines cannot use. For applications where fuel flexibility, silence, or long service life matter more than weight, the Stirling is competitive.

**Compared to steam engines**: Both are external combustion. Steam engines require a boiler (pressure vessel with risk of explosion), water treatment, and condenser. Stirling engines require no boiler, no water treatment, and no condenser — the working gas is permanently sealed. However, steam engines achieve higher power density and have a much larger industrial knowledge base. For a bootstrapping civilization, the steam engine's higher performance usually makes it the preferred external combustion choice once boiler technology is mastered.

## Historical Context

Robert Stirling patented the Stirling engine in 1816 as a safer alternative to steam engines, whose boiler explosions were a frequent and deadly occurrence in the early Industrial Revolution. The key innovation was the regenerator (which Stirling called the "economiser"), a porous matrix that stored and released heat each cycle, dramatically improving efficiency over non-regenerative hot-air engines.

Early Stirling engines found limited commercial success because they could not compete with the rapidly improving steam engine in power density or cost. The Stirling engine's sealing challenges — containing working gas at pressure with a sliding piston seal — were fundamentally harder than the steam engine's packing gland seal against liquid water.

Modern interest in Stirling engines revived in the mid-20th century for applications where silence and fuel flexibility mattered: submarine air-independent propulsion, space radioisotope power systems (NASA's Advanced Stirling Radioisotope Generator), and solar dish-electric systems (where a parabolic mirror concentrates sunlight onto the Stirling engine's hot end). The Philips company in the Netherlands developed the most advanced Stirling engines of the 20th century, achieving 40% thermal efficiency with hydrogen at 20 MPa — rivaling diesel engine efficiency with the advantage of external combustion.

For a bootstrapping civilization, the Stirling engine occupies a niche between simple steam engines and complex internal combustion engines. It requires only a lathe and basic foundry — no boiler, no petroleum refining, no fuel injection precision. A civilization with bronze-age metalworking and a charcoal furnace can build a working Stirling engine, producing mechanical power from concentrated sunlight or biomass combustion.

## Expected Performance

| Configuration | Bore × Stroke | Working Gas / Pressure | Hot-End Temp | Power Output | Thermal Efficiency |
|--------------|--------------|----------------------|-------------|-------------|-------------------|
| Gamma, LTD | 200 mm × 100 mm | Air, atmospheric | 100-200°C | 1-5 W | 1-3% |
| Beta, small | 50 mm × 40 mm | Air, 0.5 MPa | 500°C | 10-50 W | 5-10% |
| Beta, medium | 80 mm × 60 mm | Helium, 5 MPa | 650°C | 200-500 W | 20-30% |
| Alpha, large | 120 mm × 80 mm | Helium, 10 MPa | 700°C | 2-5 kW | 25-35% |
| Alpha, high-perf | 150 mm × 100 mm | Hydrogen, 15 MPa | 750°C | 10-50 kW | 35-40% |
| Free-piston | 60 mm × 20 mm | Helium, 7 MPa | 650°C | 100-500 W | 25-30% |

**Performance scaling rules**:
- Power scales approximately with (bore)² × (stroke) × (mean pressure) × (speed)
- Efficiency scales with temperature ratio T_hot/T_cold — every 100°C increase in hot-end temperature improves Carnot efficiency by ~5-10 percentage points
- Doubling mean working gas pressure approximately doubles power output (for the same engine geometry)
- Helium provides ~2× the power of air at the same pressure; hydrogen provides ~3× the power of air

**Bill of Materials — 500 W Beta Stirling Engine**:

| Component | Material | Dimensions | Manufacturing Method |
|-----------|----------|------------|---------------------|
| Cylinder block | Cast iron (class 30) | 80 mm bore × 120 mm length | Cast, then bored on lathe to ±25 μm |
| Power piston | Cast iron | 79.95 mm OD × 40 mm length | Turned on lathe, lapped to 25-50 μm clearance |
| Displacer | Thin-wall steel | 78 mm OD × 80 mm length, 1 mm wall | Turned, welded end caps, light weight critical |
| Displacer rod | Steel | 8 mm OD × 150 mm length | Turned on lathe |
| Crankshaft | Steel (1045) | 20 mm main journal, 15 mm crankpin | Turned, milled keyways, ground journals |
| Connecting rod (×2) | Steel | 10 mm × 30 mm × 120 mm | Turned ends, milled body, drilled big-end |
| Flywheel | Cast iron | 200 mm OD × 30 mm thick | Cast, turned, balanced |
| Hot-side heat exchanger | 316L SS tubing | 6 mm OD × 0.5 mm wall × 20 tubes, 150 mm long | Tube bundle brazed into housing |
| Cold-side heat exchanger | Copper tubing | 8 mm OD × 0.7 mm wall × 15 tubes, 150 mm long | Tube bundle soldered into housing |
| Regenerator | SS wire mesh | 80 mm dia × 30 mm thick, 100 mesh | Stacked screens in housing |
| Seals | PTFE (filled) | Piston ring profile | Machined from stock |
| Cooling water jacket | Steel sheet | 1 mm thick, formed and welded | Welded shell around cold exchanger |

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
