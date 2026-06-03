# Boiler (Steam Generator)

> **Node ID**: energy.steam-power.boiler
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.joining`](../machine-tools/joining.md)
> **Enables**: [`energy.steam-power.steam-engine`](steam-engine.md), [`energy.steam-power.steam-turbines`](steam-turbines.md), [`energy.geothermal`](geothermal.md)
> **Timeline**: Years 15-25
> **Outputs**: pressurized_steam
> **Critical**: Yes — without a boiler there is no steam power; boilers are the sole source of pressurized steam for engines, turbines, and industrial processes

## Principle

A boiler is a pressure vessel that converts water into steam by transferring heat from combustion gases through metal walls. Two fundamental architectures exist: **fire-tube** (hot gases pass through tubes surrounded by water) and **water-tube** (water flows through tubes surrounded by hot gases). In both cases, the rate of steam production is limited by the heat transfer surface area and the temperature differential between the combustion gases and the boiling water.

The governing relationship is: Steam production (kg/h) = Heat input (kW) × Boiler efficiency / Enthalpy of vaporization (~2260 kJ/kg at atmospheric pressure, less at higher pressure). A boiler burning 10 kg/hour of coal (28 MJ/kg) at 70% efficiency produces: 10 × 28,000 × 0.70 / 2260 ≈ 87 kg/hour of steam. Boiler pressure is determined by the steam demand: low-pressure (0.5-2 bar) for heating and early engines; medium-pressure (5-15 bar) for most engines and industrial processes; high-pressure (20-100+ bar) for steam turbines and power generation.

## Prerequisites

- [Wrought iron or steel plate](../metals/iron-steel.md) — for shell, tubes, and furnace
- [Riveting or welding capability](../machine-tools/joining.md) — for pressure vessel assembly
- [Plate rolling machine](../metals/forming.md) — for cylindrical shell and tube forming
- [Foundry](../machine-tools/casting.md) — for furnace grates, doors, and fittings
- [Feed water pump](steam-power.md) — to maintain water level under pressure
- [Fuel supply](fuels.md) — coal, wood, oil, or gas

## Materials

### Fire-Tube Boiler (Lancashire type, ~50 HP, 10 bar)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate (shell)](../metals/iron-steel.md) | 2000-3000 kg | 8-15 mm thick, A285 or equivalent | [Iron & Steel](../metals/iron-steel.md) | Wrought iron plate (riveted, heavier) |
| [Steel plate (tube sheets)](../metals/iron-steel.md) | 400-800 kg | 15-25 mm thick, flat | [Iron & Steel](../metals/iron-steel.md) | Forged plate |
| [Steel fire tubes (2)](../metals/iron-steel.md) | 1600 kg total | 600-900 mm diameter × 6 m, corrugated, 6-10 mm wall | [Forming](../metals/forming.md) | Plain tubes (weaker under external pressure) |
| [Steel stay bolts](../metals/iron-steel.md) | 200-400 pcs | 20-25 mm diameter, threaded both ends | [Iron & Steel](../metals/iron-steel.md) | Welded stays |
| [Wrought iron rivets](../metals/iron-steel.md) | 2000-4000 pcs | 16-25 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Welded seams (later technology) |
| [Cast iron furnace grate](../machine-tools/casting.md) | 50-100 kg | Bar grate, 25 mm bars at 30 mm spacing | [Foundry](../machine-tools/casting.md) | Steel bar grate |
| [Cast iron fire doors](../machine-tools/casting.md) | 2 pcs | With air damper control | [Foundry](../machine-tools/casting.md) | Steel fabrication |
| [Brass safety valves (2)](../metals/copper-bronze.md) | 2 pcs | Spring-loaded, rated to 110% of working pressure | [Foundry](../metals/copper-bronze.md) | Weighted lever type |
| [Steel steam dome](../metals/iron-steel.md) | 50-100 kg | 300-500 mm diameter, 400-600 mm tall | [Forming](../metals/iron-steel.md) | — |
| [Firebrick lining](../ceramics/kilns.md) | 100-200 pcs | 230 × 115 × 65 mm, rated to 1400°C | [Ceramics](../ceramics/kilns.md) | Castable refractory |

### Water-Tube Boiler (Babcock & Wilcox type, ~200 HP, 20 bar)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Seamless steel tubes](../metals/forming.md) | 2000-4000 kg | 50-80 mm OD, 3-5 mm wall, 3-6 m long | [Forming](../metals/forming.md) | Welded tubes (weaker) |
| [Steel plate (drums)](../metals/iron-steel.md) | 1500-2500 kg | 12-25 mm thick, for steam and mud drums | [Iron & Steel](../metals/iron-steel.md) | — |
| [Steel headers/manifolds](../metals/iron-steel.md) | 500-1000 kg | Cast or fabricated, tube connection points | [Iron & Steel](../metals/iron-steel.md) | Forged headers |
| [Steel casing](../metals/iron-steel.md) | 500-1000 kg | 3-6 mm, insulated with mineral wool | [Iron & Steel](../metals/iron-steel.md) | Brick enclosure |
| [Firebrick](../ceramics/kilns.md) | 200-400 pcs | Furnace lining, rated to 1400°C | [Ceramics](../ceramics/kilns.md) | Castable refractory |
| [Refractory insulation](../chemistry/refractories.md) | 200-500 kg | Mineral wool or castable, 50-100 mm thick | [Chemistry](../chemistry/index.md) | — |

## Construction Steps

### Fire-Tube Boiler (Lancashire)

1. **Roll the shell plate** into a cylinder on a plate rolling machine. Diameter: 2.0-2.5 m. Length: 5-7 m. Overlap the longitudinal seam by 3-5 rivet diameters for a butt-strapped joint.

2. **Drill rivet holes** through both plates of each seam using a drilling jig for accurate alignment. Hole diameter: 1.5 mm larger than rivet diameter. Deburr all holes.

3. **Drive red-hot rivets** through holes, hammer flat on both sides with pneumatic or hand riveting hammers. Rivet pitch: 3-5× rivet diameter. Test each rivet by striking — a solid ring indicates proper tightness, a dull thud indicates a loose rivet that must be replaced.

4. **Weld or rivet the tube sheets** (flat end plates, 15-25 mm thick) to the shell. Tube sheets carry the full pressure load and must be reinforced with stay bolts.

5. **Install stay bolts** through both tube sheets on a 150-200 mm grid pattern. Thread both ends, pass through drilled holes, secure with nuts and washers on the outside. Stay bolts prevent the flat tube sheets from bulging under pressure. Each stay bolt carries the pressure load from its tributary area: at 10 bar with 175 mm grid spacing, each stay bolt carries ~3000 N.

6. **Insert the fire tubes** (corrugated steel, 600-900 mm diameter) through the tube sheets. Weld or expand the tube ends into the tube sheet holes. Corrugated tubes resist collapse from external water pressure and provide more heating surface than plain tubes.

7. **Install the furnace grate** at the front of each fire tube. Cast iron bar grate, 25 mm bars at 30 mm spacing, with an ash pit below. The grate supports the coal bed while allowing primary air to pass upward through the fuel.

8. **Construct the firebrick lining** in the combustion chamber and around the fire tube entrances. Minimum 115 mm firebrick on all surfaces exposed to direct flame. Brick protects the steel shell from flame impingement and reduces heat loss.

9. **Install fittings**: Mount the steam dome on top of the shell (provides dry steam separate from water spray). Fit two spring-loaded safety valves on the dome or shell top. Install a Bourdon tube pressure gauge, two glass water level gauges, a blowdown valve at the bottom, and a feed water check valve on the side.

10. **Install the fusible plug** in the crown of each fire tube. The plug has a tin or lead alloy core (melting point 230-300°C) screwed through the tube sheet. If water level drops below the fire tube crown, the core melts and steam/water sprays onto the fire, extinguishing it.

11. **Hydrostatic test**: Fill the completed boiler with water, pressurize to 1.5× working pressure (15 bar test for a 10 bar boiler). Hold for 30 minutes. Inspect every rivet, seam, and fitting for leaks. Zero leaks acceptable. Any weeping rivets must be re-driven or replaced.

### Water-Tube Boiler (Babcock & Wilcox type)

12. **Fabricate the steam drum and mud drum** from rolled steel plate, welded longitudinal seams. Steam drum: 600-1000 mm diameter, positioned at top. Mud drum: 300-500 mm diameter, at bottom. Both drums have tube stubs for water tube connections.

13. **Bend water tubes** to shape using a tube bender. Each tube connects the mud drum to the steam drum, passing through the combustion chamber in a staggered arrangement. Tube OD: 50-80 mm, wall 3-5 mm. Bend radius: minimum 3× tube OD to prevent flattening.

14. **Expand or weld tube ends** into drum stubs. Roller expansion creates a mechanical seal by plastically deforming the tube end into the drum hole. For higher pressures (>20 bar), weld tube-to-drum joints.

15. **Construct the furnace enclosure** with firebrick walls and a steel casing. Install the coal grate or oil/gas burner at the bottom. Hot gases rise through the staggered tube bank, transferring heat to water inside the tubes.

16. **Install the same fittings** as the fire-tube boiler: safety valves (2), pressure gauge, water level gauges, blowdown valve, feed water check valve. Add a continuous blowdown valve for surface water impurity removal.

17. **Hydrostatic test** at 1.5× working pressure. Inspect all tube joints, drum seams, and header connections.

## Calibration and Verification

1. **Safety valve calibration**: Test each safety valve by raising boiler pressure to its set point. Verify the valve opens fully and re-seats cleanly at 5% below set pressure. Adjust spring tension until the set pressure is within ±2% of design.

2. **Water level gauge verification**: Blow down (drain and refill) both water gauges to verify they are not blocked. The water level visible in the gauge glass should match the actual water level — confirm by comparing the two independent gauges.

3. **Pressure gauge calibration**: Compare the installed Bourdon tube gauge against a calibrated reference gauge. Maximum error: ±1.5% of full scale.

4. **Combustion efficiency test**: Measure flue gas temperature and oxygen content. Target: flue gas 150-250°C (below 150°C risks acid condensation; above 300°C wastes heat). Oxygen 4-8% indicates correct excess air. Calculate boiler efficiency from heat balance: η = 1 - (flue gas loss + radiation loss + unburned carbon loss).

5. **Steam purity test**: Collect a steam sample from the steam dome outlet. Measure conductivity — target <10 μS/cm for saturated steam. High conductivity indicates water carryover (foaming or high water level).

## Expected Performance

### Fire-Tube (Lancashire)

| Parameter | Value |
|-----------|-------|
| Steam production | 3,000-10,000 kg/hour |
| Working pressure | 7-10 bar (up to 15 bar max) |
| Steam temperature | 170-200°C (saturated) |
| Thermal efficiency | 65-75% |
| Heating surface area | 40-80 m² |
| Water capacity | 5,000-12,000 liters |
| Dry weight | 8-20 tonnes |
| Cold start time | 2-4 hours |
| Fuel consumption (coal) | 400-1,200 kg/hour |
| Shell plate thickness | 8-15 mm |

### Water-Tube (Babcock & Wilcox type)

| Parameter | Value |
|-----------|-------|
| Steam production | 5,000-30,000 kg/hour |
| Working pressure | 15-100 bar |
| Steam temperature | 200-540°C (with superheater) |
| Thermal efficiency | 80-90% (with economizer and air preheater) |
| Heating surface area | 100-500 m² |
| Water capacity | 2,000-8,000 liters (less than fire-tube) |
| Cold start time | 30-90 minutes (faster than fire-tube) |
| Fuel consumption (coal) | 600-4,000 kg/hour |

## Strengths

- **Fire-tube**: Simple construction, large water volume stores energy well (accommodates fluctuating demand), easy to clean and inspect, relatively tolerant of poor feed water quality
- **Water-tube**: Higher pressure capability (small tubes withstand internal pressure better), faster response to load changes, safer failure mode (small tube burst vs. shell rupture), higher efficiency achievable

## Weaknesses

- **Fire-tube**: Limited to ~15 bar (shell design limits pressure), large water volume means a shell failure releases enormous stored energy, slow to raise steam from cold
- **Water-tube**: More complex construction (many tube joints), more sensitive to feed water quality (scale in narrow tubes causes rapid failure), higher initial cost

## Safety

- **Boiler explosion**: The primary lethal hazard. A Lancashire boiler at 10 bar with 8,000 liters of water contains enough stored energy to level a building. Causes: low water (overheated steel loses strength), overpressure (blocked or tampered safety valves), corrosion (thin shell ruptures), stay bolt failure.
- **Prevention**: Two independent safety valves (never one), daily water gauge verification, annual hydraulic test at 1.5× working pressure, regular internal inspection for corrosion and cracking. Never operate a boiler with known defects. Never tie down or block a safety valve.
- **Low water**: If water drops below the fire tubes, the uncovered steel overheats, weakens, and the boiler explodes under pressure. If water level is uncertain or dropping, shut down the fire immediately. Do NOT add cold water to an overheated boiler — the thermal shock can cause immediate failure.
- **Steam burns**: Steam at 10 bar is 180°C and carries 5× more heat energy than water at the same temperature. Insulate all steam pipes and fittings. Never approach a steam leak without full protection.

## See Also

- [Steam Power](steam-power.md) — steam power systems overview, operating procedures, and efficiency improvements
- [Steam Engine](steam-engine.md) — reciprocating engines driven by boiler steam
- [Steam Turbines](steam-turbines.md) — turbines for power generation from boiler steam
- [Fuels](fuels.md) — coal, wood, oil, and gas for boiler firing
- [Iron & Steel](../metals/iron-steel.md) — plate steel for boiler shells and tubes
- [Joining](../machine-tools/joining.md) — riveting and welding for pressure vessel assembly
- [Refractories](../chemistry/refractories.md) — firebrick and castable linings
- [Water Treatment](../water/basic-treatment.md) — feed water quality for scale prevention

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
