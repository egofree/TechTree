# Cooling Systems & Refrigeration

> **Node ID**: energy.cooling
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.electricity`](electricity.md), [`machine-tools`](../machine-tools/index.md), [`chemistry`](../chemistry/index.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`chemistry.air-separation`](../chemistry/air-separation.md), [`photolithography.cleanrooms`](../photolithography/cleanrooms.md), [`silicon.crystal-growth`](../silicon/crystal-growth.md)
> **Timeline**: Years 20-30
> **Outputs**: refrigeration, industrial_cooling, ice_production

### Overview

Refrigeration moves heat from a cold region to a hot region using external energy — it does not "make cold" but pumps heat against its natural gradient. Two principal cycles serve bootstrap industry: **[absorption refrigeration](../glossary/absorption-refrigeration.md)** (heat-driven, no moving parts in the refrigerant circuit, usable with waste heat or flame) and **[vapor-compression refrigeration](../glossary/vapor-compression-refrigeration.md)** (mechanically driven, higher COP, requires electric motor or engine). Both cycles depend on a refrigerant that evaporates at low temperature (absorbing heat) and condenses at higher temperature (rejecting heat). Ice manufacturing and cold storage extend these cycles into practical food preservation and process cooling.

### Absorption Refrigeration

**[Ammonia-water system](../glossary/ammonia-water-system.md)** (the first practical refrigeration cycle, industrially deployed from the 1850s):

- **Working pair**: Ammonia (NH₃) as refrigerant, water (H₂O) as absorbent. Ammonia boils at -33.3°C at atmospheric pressure, making it ideal for below-freezing applications.
- **Generator** (desorber): Strong ammonia-water solution (typically 35-40% NH₃ by weight) heated to 80-150°C by steam, flame, or waste heat. Heat drives ammonia vapor out of solution. Pressure in generator: 10-15 bar.
- **Condenser**: Ammonia vapor flows to condenser, cooled by water jacket or air finned tubes. Vapor condenses to liquid ammonia at ~25-40°C. Condensing pressure: 10-15 bar (corresponding to ~25-40°C saturation temperature).
- **Expansion valve**: Liquid ammonia passes through restriction (capillary or orifice), dropping pressure to 1-3 bar. Flash evaporation cools the remaining liquid to ~-10 to -30°C.
- **Evaporator**: Low-pressure liquid ammonia evaporates in coils immersed in brine tank or air duct, absorbing heat from the surroundings. This is the cooling effect. Evaporating at -10 to -33°C depending on pressure.
- **Absorber**: Ammonia vapor from evaporator is absorbed by weak solution returning from generator. Absorption is exothermic — requires cooling water (20-30°C). The strong solution is pumped back to generator by a small liquid pump (the ONLY moving part in the refrigerant circuit, requiring ~0.5-2 kW for a 100 kW cooling capacity unit).
- **Solution heat exchanger**: Recover heat between hot weak solution leaving generator and cold strong solution entering generator. Improves COP from ~0.3 to ~0.5-0.7.
- **[COP](../glossary/cop.md)** (Coefficient of Performance): 0.4-0.7 (cooling output ÷ heat input). Lower than vapor-compression, but fueled by waste heat that would otherwise be discarded.
- **Heat source temperature**: Minimum 80°C for single-effect. Double-effect units (using two generators in series) require 150-200°C but achieve COP 1.0-1.4.
- **Advantages**: Few moving parts, heat-driven (works with steam, exhaust gas, solar thermal), no electricity required for small units. Ideal for bootstrap phase where electricity is scarce.
- **Limitations**: Bulky, lower COP, ammonia toxicity (see Safety).

### Vapor-Compression Refrigeration

**[The dominant modern cycle](../glossary/the-dominant-modern-cycle.md)** (requires electric motor or engine drive):

- **Compressor**: Raises refrigerant vapor from low pressure (evaporator) to high pressure (condenser). Four types, in order of complexity:
  - **Reciprocating (piston)**: 2-16 cylinders, 500-3000 RPM. Capacity 5-500 kW. Requires crankshaft, pistons, valves (reed or ring plate), connecting rods — directly builds on internal combustion engine machining skills. Volumetric efficiency ~65-85%.
  - **Rotary (scroll/screw)**: Scroll (two interleaving spiral scrolls, one orbiting) or screw (two meshing helical rotors). Capacity 10-2000 kW. Higher efficiency, fewer moving parts than reciprocating. Requires precision machining of scroll profiles (CNC or master template tracing).
  - **Centrifugal**: Impeller accelerates refrigerant vapor outward. Capacity 300-10,000+ kW. For large industrial and district cooling. Requires high-speed precision rotor balancing.
  - **Pressure ratio**: Typically 3:1 to 10:1 (e.g., evaporator at 1.5 bar → condenser at 12 bar for ammonia).
- **Condenser**: Same function as absorption cycle — reject heat from high-pressure refrigerant. Water-cooled (shell-and-tube, 5-10°C water temperature rise) or air-cooled (finned tubes with forced airflow). Condensing temperature typically 30-50°C.
- **Expansion valve**: Thermostatic expansion valve (TXV) or capillary tube. TXV uses remote bulb sensing evaporator outlet temperature to modulate flow — maintains proper superheat (5-10°C above saturation) and prevents liquid slugging the compressor.
- **Evaporator**: Same as absorption cycle. Direct-expansion coils (refrigerant evaporates directly in air or liquid) or flooded shell (refrigerant pools in shell, liquid to be cooled flows through tubes).
- **COP**: 2.5-5.0 (cooling output ÷ electrical input). Much higher than absorption, but requires reliable electricity.
- **Compressor power**: For 100 kW cooling at COP 3.0, compressor draws ~33 kW electrical. Motor sizing: add 10-20% margin → 40 kW motor.

### Refrigerant Properties

| Refrigerant | Designation | Boiling point (1 atm) | ODP | GWP | Notes |
|-------------|-------------|----------------------|-----|-----|-------|
| Ammonia | R-717 | -33.3°C | 0 | 0 | Excellent thermodynamic properties, toxic, flammable at 15-28% in air |
| CO₂ | R-744 | -78.5°C (sublimes) | 0 | 1 | Very high operating pressure (40-100 bar), requires robust components |
| Propane | R-290 | -42.1°C | 0 | ~3 | Good properties, highly flammable, charge limit ~150 g for safety |
| Isobutane | R-600a | -11.7°C | 0 | ~3 | Lower pressure, flammable, used in domestic refrigerators |
| Water | R-718 | 100°C | 0 | 0 | Vacuum-pressure systems only, very high latent heat |

- **Bootstrap recommendation**: Ammonia (R-717) is the first-choice refrigerant. It can be produced from coke oven ammonia liquor (byproduct of coke production — see [Fuel Production](fuels.md)), has excellent thermodynamic properties (high latent heat ~1370 kJ/kg), and zero environmental impact. CO₂ (R-744) is the second choice — available from combustion or fermentation, but the high operating pressures demand stronger vessel construction.

### Ice Manufacturing

**[Can ice system](../glossary/can-ice-system.md)** (the earliest industrial ice production method):

- **Brine tank**: Large insulated tank (concrete or steel-lined wood) filled with calcium chloride (CaCl₂) brine, maintained at -10 to -15°C. Brine specific gravity: 1.20-1.26 (23-28% CaCl₂ by weight). Brine must not freeze at operating temperature — CaCl₂ eutectic is -55°C at 29.6%.
- **Ice cans**: Rectangular sheet-metal molds (typically 25-150 kg capacity), filled with clean water, immersed in brine tank. Brine circulates around cans by stirrer or pump.
- **Cooling source**: Ammonia or other refrigerant coils immersed in brine tank, or shell-and-tube brine chiller. Brine cooled to -10 to -15°C.
- **Freezing time**: 12-36 hours depending on can size. Ice freezes from outside in — center freezes last. Clear ice requires agitation of water during freezing (air bubbled through water to exclude trapped air bubbles and minerals).
- **Harvesting**: Hoist cans from brine, dip briefly in warm water tank to release ice block from can walls. Dump ice block onto conveyor or slide.
- **Daily capacity**: A 3 × 6 meter brine tank with 100-200 cans produces 5-20 tonnes of ice per day depending on refrigeration capacity and can size.

**[Plate ice and flake ice](../glossary/plate-ice-and-flake-ice.md)** (continuous production, later development):
- Refrigerant flows inside vertical plates; water flows over outside surface. Ice forms as 5-15 mm layer, harvested by hot-gas defrost cycle. Higher throughput but more complex machinery.

### Cold Storage Design

**[Insulation materials](../glossary/insulation-materials.md)** (in order of availability):

| Material | Thermal conductivity (W/m·K) | Typical thickness | Notes |
|----------|------------------------------|-------------------|-------|
| Cork board | 0.035-0.045 | 150-300 mm | Traditional choice, rot-resistant, compressible |
| Sawdust | 0.05-0.08 | 200-400 mm | Cheap, settles over time, fire hazard |
| Straw bale | 0.05-0.07 | 300-500 mm | Very cheap, requires vapor barrier, pest risk |
| Mineral wool | 0.03-0.04 | 100-200 mm | From slag or rock, fireproof, needs Chemistry stage |
| Expanded polystyrene | 0.03-0.04 | 100-200 mm | Petrochemical product, much later |

- **Vapor barrier**: Essential on the warm side of insulation. Asphalt-impregnated paper, galvanized steel sheet, or aluminum foil. Prevents moisture ingress that destroys insulation effectiveness and causes structural frost heave.
- **Floor insulation**: 150-200 mm of insulation under concrete slab on grade. Heater cables or ventilation under slab to prevent ground freezing (frost heave destroys floors at -20°C rooms).
- **Temperature zones**: +2 to +5°C (chill store, fruit/vegetables), -18 to -25°C (frozen store), -30 to -40°C (hard frozen / blast freezer). Each zone requires its own insulated room and evaporator.

### Industrial Process Cooling

- **Compressor intercoolers**: Multi-stage air compressors require interstage cooling (water jackets or shell-and-tube) to approach isothermal compression. Uncooled two-stage compressor loses ~15% efficiency.
- **Chemical reactor cooling**: Exothermic reactions (nitric acid absorption, polymerization) require jacketed reactors with chilled water or brine circulation. Chilled water at 5-10°C from refrigeration plant.
- **Bearing and machine tool cooling**: Continuous oil or water cooling on heavy machine tools (grinders, large lathes) removes cutting heat. Typically 15-25°C cooling water circulated through machine.
- **Semiconductor fab cooling**: Cleanrooms require precise temperature control (22 ± 0.5°C) and humidity control (40-50% RH). Chilled water (5-7°C) feeds air handling units. Process tools (implanters, CVD reactors) may require glycol-chilled water at -10 to +10°C.

### Safety

- **Ammonia (NH₃)**: IDLH (Immediately Dangerous to Life or Health) = 300 ppm. Irritating at 25-50 ppm. Lethal at 5000+ ppm. Flammable range 15-28% in air. Detectors mandatory in all ammonia plant rooms. Emergency ventilation at 30+ air changes per hour. Full-face respirator with ammonia cartridges for entry into plant rooms. Ammonia leaks detected by smell at 5 ppm (excellent self-alarming property).
- **CO₂ (R-744)**: Asphyxiant at >10% concentration. High-pressure hazard — 40-100 bar operating pressure requires rated pressure vessels, relief valves, and burst discs. CO₂ leaks are odorless — detectors required.
- **Hydrocarbon refrigerants** (propane, isobutane): Highly flammable. Charge limits and spark-free components mandatory. Ventilation and leak detection essential.
- **Brine**: CaCl₂ brine is corrosive to steel. Use corrosion inhibitors (sodium chromate or sodium nitrite, 2000-3000 ppm). Inspect brine tank and coils annually.
- **Pressure vessels**: Condensers, receivers, and evaporators are pressure vessels. Design to ASME or equivalent code. Hydrostatic test at 1.5× design pressure. Relief valves on every pressure vessel, piped to safe discharge point.

### Parameters Summary

| Parameter | Absorption (NH₃-H₂O) | Vapor-compression (R-717) |
|-----------|-----------------------|--------------------------|
| COP | 0.4-0.7 (single-effect) | 2.5-5.0 |
| Drive energy | Heat (80-200°C) | Electricity or mechanical |
| Cooling capacity range | 10-5000 kW | 0.5-10,000+ kW |
| Evaporator temperature | -60 to +10°C | -70 to +15°C |
| Moving parts (refrigerant side) | 1 pump | 1 compressor + valves |
| Refrigerant cost | Low (NH₃ from coke ovens) | Low |
| Noise | Low | Moderate to high |

### Absorption Cycle: Detailed Operating Parameters

The ammonia absorption cycle runs on four main temperature zones, each corresponding to a major component. Getting these zones right determines whether the cycle produces ice or wastes fuel.

**Generator (desorber) at 120-150°C**: Heat input drives ammonia vapor out of the ammonia-water solution. The generator temperature must be high enough to liberate ammonia but not so high that water vapor carries over (water contamination in the refrigerant circuit reduces efficiency and can freeze in the evaporator). A rectifier (fractionating column) above the generator strips water vapor from the ammonia. Generator heat input for a 100 kW cooling plant: roughly 140-250 kW of thermal energy, depending on COP.

**Condenser at 30-40°C**: Ammonia vapor condenses at the pressure maintained in the high-side circuit (10-15 bar, corresponding to a saturation temperature of 25-40°C). Cooling water at 20-30°C removes the latent heat. Condenser heat rejection equals the sum of evaporator cooling load plus generator heat input.

**Evaporator at -10 to 0°C**: Liquid ammonia evaporates at 1-3 bar, absorbing heat from the brine or air surrounding the coils. For ice production, the evaporator cools brine to -10 to -15°C, which in turn freezes water in the ice cans. The temperature difference between evaporating refrigerant and the brine (approach temperature) is typically 3-8°C.

**Absorber at 30-40°C**: Weak solution returning from the generator absorbs ammonia vapor from the evaporator. This process is exothermic and must be cooled, typically with the same cooling water supply as the condenser. Absorber cooling load is roughly equal to the evaporator cooling load.

**COP range**: Single-effect ammonia absorption achieves COP of 0.5-0.7 under design conditions. This means 100 kW of cooling requires 140-200 kW of heat input. Lower than vapor-compression, but the heat can come from waste sources: engine exhaust, boiler flue gas, solar thermal collectors, or process steam.

### Ice Block Production Details

**Ice can sizing**: Standard can sizes produce blocks from 25 kg to 135 kg. A 25 kg block (roughly 250 × 150 × 250 mm) freezes in 12-18 hours. A 135 kg block (roughly 550 × 250 × 350 mm) takes 36-48 hours. Larger blocks are more energy-efficient per kilogram (lower surface-to-volume ratio means less brine circulation needed per unit of ice).

**Brine tank layout**: A typical production tank measures 3 × 6 m with 100-200 cans arranged in rows. Agitators (propeller-type stirrers) circulate brine at 0.3-0.6 m/s around the cans to maintain uniform temperature. Without agitation, warm brine stratifies near the cans, slowing freezing.

**Clear ice production**: Trapped air bubbles and dissolved minerals make ice cloudy. To produce clear blocks (preferred for food display and transport), compressed air is bubbled through the water in each can during freezing. This pushes dissolved air and minerals toward the last-unfrozen center. Some producers also pre-boil the water to remove dissolved gases. The center core, where impurities concentrate, can be reamed out and discarded after harvesting.

**Harvesting cycle**: After the freeze period, an overhead hoist lifts can racks from the brine. Each can is dipped in a warm water trough (40-50°C) for 30-60 seconds, melting a thin layer against the can wall. The block slides out onto a gravity conveyor. Cans are refilled with fresh water and returned to the brine tank. A well-run plant turns over cans 1-2 times per day.

### Cold Storage Room Construction

**Wall assembly (cold store at -18°C)**: A typical wall section from inside to outside consists of the inner cladding (galvanized steel or aluminum sheet, 0.5-1.0 mm), insulation layer, vapor barrier, structural wall, and outer cladding. The insulation is the critical element.

**Cork insulation**: The traditional choice for cold storage from the 1890s through the 1950s. Cork board panels 100-150 mm thick provide R-value of roughly 3-4 per inch (thermal conductivity 0.035-0.045 W/m·K). Cork is naturally rot-resistant, dimensionally stable, and does not absorb moisture readily. Panels are bonded with hot asphalt or bituminous adhesive. For -18°C storage, total wall insulation thickness of 150-200 mm of cork is standard.

**Expanded polystyrene (EPS)**: Modern replacement for cork, with similar thermal conductivity (0.030-0.040 W/m·K). EPS panels 150-200 mm thick are standard for frozen storage. Available as plain board or as factory-laminated sandwich panels (steel facings with EPS core) that serve as both insulation and structural wall. EPS must be kept away from heat sources above 75°C.

**Vapor barrier placement**: The vapor barrier always goes on the warm side of the insulation. In a cold store, that means the exterior side. Without it, warm humid air migrates through the wall, condenses inside the cold insulation, freezes, and gradually destroys the insulation value. Materials: 0.1 mm polyethylene film (modern), asphalt-impregnated building paper, or continuous galvanized steel sheet with sealed joints. Lap all seams at least 100 mm and seal with compatible mastic.

**Insulated doors**: Cold store doors are a major source of heat gain. Standard construction: 100 mm thick insulated panel (same material as walls), clad in steel or aluminum on both faces. Magnetic or compression gaskets around the perimeter maintain an air-tight seal when closed. Sliding doors preferred (no swing clearance needed). Door heaters (low-wattage electric resistance wires in the frame) prevent ice buildup on the gasket at temperatures below -10°C.

### Refrigeration Load Calculation

The total refrigeration load for a cold storage room has four components that must be calculated independently and summed.

**Transmission load (Q_transmission)**: Heat conducting through walls, floor, and ceiling. Q = U × A × ΔT, where U is the overall heat transfer coefficient (W/m²·K) of the wall assembly, A is the surface area (m²), and ΔT is the temperature difference between inside and outside. Example: a 10 × 8 × 4 m room at -18°C in a 30°C ambient. Walls + ceiling + floor area ≈ 304 m². With 150 mm cork (U ≈ 0.25 W/m²·K), Q = 0.25 × 304 × 48 ≈ 3,648 W ≈ 3.6 kW continuous.

**Product load**: Heat that must be removed from goods entering the room to cool or freeze them to storage temperature. Includes sensible heat above freezing, latent heat of fusion (for freezing), and sensible heat below freezing. Example: 5,000 kg of beef entering at 10°C, frozen to -18°C. Specific heat above freezing ≈ 3.2 kJ/kg·K (cool 10°C to -1°C = 35.2 kJ/kg). Latent heat of fusion ≈ 230 kJ/kg. Specific heat below freezing ≈ 1.7 kJ/kg·K (cool -1°C to -18°C = 28.9 kJ/kg). Total per kg = 294.1 kJ. Total = 1,471 MJ. If this must occur in 24 hours: 1,471 MJ / 86,400 s ≈ 17 kW average.

**Infiltration load**: Warm air entering through door openings. Each air change introduces warm, humid air that must be cooled and dehumidified. Estimate: 1-2 air changes per hour for rooms with moderate door traffic. The enthalpy difference between outside and inside air determines the load. At 30°C ambient and -18°C room temperature, each kilogram of infiltrated air carries roughly 60-80 kJ of heat that the refrigeration system must remove.

**Equipment load**: Heat from lights, motors, and people inside the room. Electric lights: 10-20 W/m² of floor area. Fan motors on evaporator coils: 0.5-2 kW each. Workers: each person contributes roughly 250-300 W of sensible and latent heat. Sum all internal heat sources.

### Ammonia Absorption Cycle Temperature Zones

The ammonia absorption cycle runs on four main temperature zones, each corresponding to a major component. Getting these zones right determines whether the cycle produces ice or wastes fuel.

**Generator (desorber) at 120-150°C**: Heat input drives ammonia vapor out of the ammonia-water solution. The generator temperature must be high enough to liberate ammonia but not so high that water vapor carries over (water contamination in the refrigerant circuit reduces efficiency and can freeze in the evaporator). A rectifier (fractionating column) above the generator strips water vapor from the ammonia. Generator heat input for a 100 kW cooling plant: roughly 140-250 kW of thermal energy, depending on COP.

**Condenser at 30-40°C**: Ammonia vapor condenses at the pressure maintained in the high-side circuit (10-15 bar, corresponding to a saturation temperature of 25-40°C). Cooling water at 20-30°C removes the latent heat. Condenser heat rejection equals the sum of evaporator cooling load plus generator heat input.

**Evaporator at -10 to 0°C**: Liquid ammonia evaporates at 1-3 bar, absorbing heat from the brine or air surrounding the coils. For ice production, the evaporator cools brine to -10 to -15°C, which in turn freezes water in the ice cans. The temperature difference between evaporating refrigerant and the brine (approach temperature) is typically 3-8°C.

**Absorber at 30-40°C**: Weak solution returning from the generator absorbs ammonia vapor from the evaporator. This process is exothermic and must be cooled, typically with the same cooling water supply as the condenser. Absorber cooling load is roughly equal to the evaporator cooling load.

**COP range**: Single-effect ammonia absorption achieves COP of 0.5-0.7 under design conditions. This means 100 kW of cooling requires 140-200 kW of heat input.

### Ice Block Production Details

**Ice can sizing and freeze time**: Standard can sizes produce blocks from 25 kg to 135 kg. A 25 kg block (roughly 250 × 150 × 250 mm) freezes in 12-18 hours. A 135 kg block (roughly 550 × 250 × 350 mm) takes 36-48 hours. Larger blocks are more energy-efficient per kilogram because the lower surface-to-volume ratio means less brine circulation needed per unit of ice produced.

**Clear ice production**: Trapped air bubbles and dissolved minerals make ice cloudy. To produce clear blocks (preferred for food display and transport), compressed air is bubbled through the water in each can during freezing. This pushes dissolved air and minerals toward the last-unfrozen center. Some producers also pre-boil the water to remove dissolved gases. The center core, where impurities concentrate, can be reamed out and discarded after harvesting.

### Cold Storage Room Construction

**Wall assembly (cold store at -18°C)**: A typical wall section from inside to outside consists of the inner cladding (galvanized steel or aluminum sheet, 0.5-1.0 mm), insulation layer, vapor barrier, structural wall, and outer cladding. The insulation is the critical element.

**Cork insulation**: The traditional choice for cold storage from the 1890s through the 1950s. Cork board panels 100-150 mm thick provide R-value of roughly 3-4 per inch (thermal conductivity 0.035-0.045 W/m·K). Cork is naturally rot-resistant, dimensionally stable, and does not absorb moisture readily. Panels are bonded with hot asphalt or bituminous adhesive.

**Expanded polystyrene (EPS)**: Modern replacement for cork, with similar thermal conductivity (0.030-0.040 W/m·K). EPS panels 150-200 mm thick are standard for frozen storage. Available as plain board or as factory-laminated sandwich panels (steel facings with EPS core) that serve as both insulation and structural wall.

**Vapor barrier placement**: The vapor barrier always goes on the warm side of the insulation. In a cold store, that means the exterior side. Without it, warm humid air migrates through the wall, condenses inside the cold insulation, freezes, and gradually destroys the insulation value. Materials: 0.1 mm polyethylene film, asphalt-impregnated building paper, or continuous galvanized steel sheet with sealed joints.

**Insulated doors**: Cold store doors are a major source of heat gain. Standard construction: 100 mm thick insulated panel, clad in steel or aluminum on both faces, with magnetic or compression gaskets around the perimeter. Door heaters (low-wattage electric resistance wires in the frame) prevent ice buildup on the gasket at temperatures below -10°C.

### References

- Dossat, R.J., *Principles of Refrigeration*, 5th ed.
- ASHRAE Handbook — Fundamentals (refrigerant properties, load calculations)
- Stoecker, W.F., *Industrial Refrigeration Handbook* (ammonia systems, ice plants)
- Hodge, B.K., *Analysis and Design of Energy Systems* (absorption cycle thermodynamics)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
