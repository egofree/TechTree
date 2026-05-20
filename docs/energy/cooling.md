# Cooling Systems & Refrigeration

> **Node ID**: energy.cooling
> **Domain**: [Energy](./)
> **Dependencies**: `energy.electricity`, `machine-tools`, `chemistry`, `metals.iron-steel`
> **Enables**: `chemistry.air-separation`, `photolithography.cleanrooms`, `silicon.crystal-growth`
> **Timeline**: Years 20-30
> **Outputs**: refrigeration, industrial_cooling, ice_production

### Overview

Refrigeration moves heat from a cold region to a hot region using external energy — it does not "make cold" but pumps heat against its natural gradient. Two principal cycles serve bootstrap industry: **absorption refrigeration** (heat-driven, no moving parts in the refrigerant circuit, usable with waste heat or flame) and **vapor-compression refrigeration** (mechanically driven, higher COP, requires electric motor or engine). Both cycles depend on a refrigerant that evaporates at low temperature (absorbing heat) and condenses at higher temperature (rejecting heat). Ice manufacturing and cold storage extend these cycles into practical food preservation and process cooling.

### Absorption Refrigeration

**Ammonia-water system** (the first practical refrigeration cycle, industrially deployed from the 1850s):

- **Working pair**: Ammonia (NH₃) as refrigerant, water (H₂O) as absorbent. Ammonia boils at -33.3°C at atmospheric pressure, making it ideal for below-freezing applications.
- **Generator** (desorber): Strong ammonia-water solution (typically 35-40% NH₃ by weight) heated to 80-150°C by steam, flame, or waste heat. Heat drives ammonia vapor out of solution. Pressure in generator: 10-15 bar.
- **Condenser**: Ammonia vapor flows to condenser, cooled by water jacket or air finned tubes. Vapor condenses to liquid ammonia at ~25-40°C. Condensing pressure: 10-15 bar (corresponding to ~25-40°C saturation temperature).
- **Expansion valve**: Liquid ammonia passes through restriction (capillary or orifice), dropping pressure to 1-3 bar. Flash evaporation cools the remaining liquid to ~-10 to -30°C.
- **Evaporator**: Low-pressure liquid ammonia evaporates in coils immersed in brine tank or air duct, absorbing heat from the surroundings. This is the cooling effect. Evaporating at -10 to -33°C depending on pressure.
- **Absorber**: Ammonia vapor from evaporator is absorbed by weak solution returning from generator. Absorption is exothermic — requires cooling water (20-30°C). The strong solution is pumped back to generator by a small liquid pump (the ONLY moving part in the refrigerant circuit, requiring ~0.5-2 kW for a 100 kW cooling capacity unit).
- **Solution heat exchanger**: Recover heat between hot weak solution leaving generator and cold strong solution entering generator. Improves COP from ~0.3 to ~0.5-0.7.
- **COP** (Coefficient of Performance): 0.4-0.7 (cooling output ÷ heat input). Lower than vapor-compression, but fueled by waste heat that would otherwise be discarded.
- **Heat source temperature**: Minimum 80°C for single-effect. Double-effect units (using two generators in series) require 150-200°C but achieve COP 1.0-1.4.
- **Advantages**: Few moving parts, heat-driven (works with steam, exhaust gas, solar thermal), no electricity required for small units. Ideal for bootstrap phase where electricity is scarce.
- **Limitations**: Bulky, lower COP, ammonia toxicity (see Safety).

### Vapor-Compression Refrigeration

**The dominant modern cycle** (requires electric motor or engine drive):

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

**Can ice system** (the earliest industrial ice production method):

- **Brine tank**: Large insulated tank (concrete or steel-lined wood) filled with calcium chloride (CaCl₂) brine, maintained at -10 to -15°C. Brine specific gravity: 1.20-1.26 (23-28% CaCl₂ by weight). Brine must not freeze at operating temperature — CaCl₂ eutectic is -55°C at 29.6%.
- **Ice cans**: Rectangular sheet-metal molds (typically 25-150 kg capacity), filled with clean water, immersed in brine tank. Brine circulates around cans by stirrer or pump.
- **Cooling source**: Ammonia or other refrigerant coils immersed in brine tank, or shell-and-tube brine chiller. Brine cooled to -10 to -15°C.
- **Freezing time**: 12-36 hours depending on can size. Ice freezes from outside in — center freezes last. Clear ice requires agitation of water during freezing (air bubbled through water to exclude trapped air bubbles and minerals).
- **Harvesting**: Hoist cans from brine, dip briefly in warm water tank to release ice block from can walls. Dump ice block onto conveyor or slide.
- **Daily capacity**: A 3 × 6 meter brine tank with 100-200 cans produces 5-20 tonnes of ice per day depending on refrigeration capacity and can size.

**Plate ice and flake ice** (continuous production, later development):
- Refrigerant flows inside vertical plates; water flows over outside surface. Ice forms as 5-15 mm layer, harvested by hot-gas defrost cycle. Higher throughput but more complex machinery.

### Cold Storage Design

**Insulation materials** (in order of availability):

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

### References

- Dossat, R.J., *Principles of Refrigeration*, 5th ed.
- ASHRAE Handbook — Fundamentals (refrigerant properties, load calculations)
- Stoecker, W.F., *Industrial Refrigeration Handbook* (ammonia systems, ice plants)
 - Hodge, B.K., *Analysis and Design of Energy Systems* (absorption cycle thermodynamics)

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
