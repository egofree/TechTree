# Solar Thermal Collector

> **Node ID**: energy.solar-thermal.collector
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.solar-thermal`](solar-thermal.md), [`glass.basic`](../glass/basic.md), [`metals.copper-bronze`](../metals/copper-bronze.md)
> **Enables**: [`energy.steam-power`](steam-power.md), [`energy.cooling`](cooling.md)
> **Timeline**: Years 5-20
> **Outputs**: solar_heat, heated_water, process_heat
> **Critical**: No — solar thermal collectors supplement fuel-fired heat sources, reducing fuel consumption where sunlight is available

## Overview

A solar thermal collector absorbs solar radiation and converts it to usable heat. Two fundamental designs exist: **flat-plate collectors** (no concentration, 40-80°C output) and **parabolic trough concentrators** (30-100× concentration, 300-500°C output). Both rely on the selective surface principle — a surface that absorbs strongly in the solar spectrum (absorptivity >0.95) but emits weakly in the infrared (emissivity <0.15), minimizing radiative heat loss while maximizing solar energy capture.

The energy balance is: Q_useful = (Solar irradiance × Aperture area × Optical efficiency) - (Thermal losses from receiver). Flat-plate collectors lose heat by convection and radiation from the entire absorber surface. Concentrating collectors reduce thermal losses by focusing sunlight onto a small receiver area, achieving higher temperatures at the cost of requiring sun tracking.

Peak solar irradiance at Earth's surface: 800-1000 W/m² (direct normal irradiance, DNI). Annual solar energy: 1000-2800 kWh/m²/year depending on latitude and climate. Solar thermal collectors convert this free energy into usable heat with no fuel cost and minimal maintenance, making them one of the most cost-effective energy technologies available at the bootstrap stage.

The selective surface is the key enabling technology for all solar thermal collectors. A surface with high solar absorptivity (>0.95) and low infrared emissivity (<0.15) captures solar energy while minimizing reradiation losses. Black chrome electroplated on steel or copper achieves α > 0.95, ε < 0.10 — but requires electroplating capability. For bootstrap contexts without electroplating, matte black paint (α ≈ 0.95, ε ≈ 0.90) works for flat-plate collectors operating below 80°C, where convective losses dominate over radiative losses anyway. Cross-reference: [Solar Thermal Energy](solar-thermal.md) for large-scale concentrating systems; [Cooling](cooling.md) for absorption chillers driven by solar heat.

## Bill of Materials

### Flat-Plate Collector (2 m², water heating)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Copper tubing](../metals/copper-bronze.md) | 15-20 m | 15 mm OD, 1 mm wall, serpentine pattern | [Copper & Bronze](../metals/copper-bronze.md) | Stainless steel tubing (lower conductivity) |
| [Flat glass sheet](../glass/basic.md) | 1 sheet | 4 mm thick, 2 m², low-iron tempered | [Glass](../glass/basic.md) | Polycarbonate (UV degrades, lower temp) |
| [Steel sheet (absorber plate)](../metals/iron-steel.md) | 2 m² | 0.5-1.0 mm, painted matte black | [Iron & Steel](../metals/iron-steel.md) | Copper sheet (better conductivity, expensive) |
| [Mineral wool insulation](../chemistry/index.md) | 1-2 m² | 50 mm thick, 50-100 kg/m³ | [Chemistry](../chemistry/index.md) | Cork (lower R-value), straw (fire risk) |
| [Steel or copper tank](../metals/index.md) | 1 unit | 200 liters, 1.5 mm wall | [Metals](../metals/index.md) | Concrete tank with liner |
| [Black paint](../chemistry/index.md) | 1 liter | Matte, solar absorptivity >0.95 | [Chemistry](../chemistry/index.md) | Soot mixed with linseed oil |
| [Rubber or silicone gasket](../polymers/index.md) | 5 m | 3-5 mm cord, food-grade silicone | [Polymers](../polymers/index.md) | Clay putty (less durable) |
| [Wood or steel framing](../plants/structural-plants.md) | 5-10 m | 25 × 50 mm timber or 1 mm steel | [Plants](../plants/index.md) | Aluminum extrusion |

### Parabolic Trough Collector (10 m² aperture)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Curved glass mirror](../glass/basic.md) | 10 m² | 4 mm, silvered, reflectivity 90-95% | [Glass](../glass/basic.md) | Polished aluminum (70-80% reflectivity) |
| [Steel receiver tube](../metals/iron-steel.md) | 5-8 m | 50 mm OD, selective coating | [Iron & Steel](../metals/iron-steel.md) | Copper tube (better conductivity, lower max temp) |
| [Glass envelope tube](../glass/basic.md) | 5-8 m | 80 mm OD, borosilicate, evacuated | [Glass](../glass/basic.md) | None — required for vacuum insulation |
| [Steel support structure](../metals/iron-steel.md) | 50-80 kg | Galvanized, parabolic frame | [Iron & Steel](../metals/iron-steel.md) | Wood (limited rigidity, rot) |
| [Heat transfer fluid](../chemistry/index.md) | 50-100 liters | Mineral oil, rated to 300°C | [Chemistry](../chemistry/index.md) | Water (limited to 100°C at 1 atm) |
| [Tracking mechanism](../electronics/index.md) | 1 unit | Gear motor + shadow sensor controller | [Electronics](../electronics/index.md) | Manual adjustment (labor-intensive) |
| [Circulation pump](steam-power.md) | 1 unit | 0.5-1 kW, rated for fluid temperature | [Energy](./index.md) | Thermosiphon (limited height) |

## Process Description

### Flat-Plate Collector

1. **Build the absorber plate**: Paint a copper or steel sheet matte black (two coats, cured at 100°C for 1 hour). Solder or braze copper tubing in a serpentine pattern on the back of the plate, spacing tubes 100-150 mm apart. Test solder joints at 2 bar water pressure for 30 minutes — zero leaks acceptable.

2. **Assemble the collector box**: Build a shallow wooden or metal box (100-150 mm deep). Install 50 mm mineral wool insulation on the bottom and sides. Place the absorber plate (painted side up) on top of the insulation.

3. **Install the glass cover**: Lay a single pane of 4 mm flat glass on top of the box, sealed with silicone gasket around the perimeter. The 25-40 mm air gap between glass and absorber provides greenhouse-effect insulation (glass transmits visible light but blocks infrared re-radiation from the absorber).

4. **Seal the box** with weatherproofing — paint or varnish all exterior wood, caulk all joints. The box must be watertight to prevent insulation degradation.

5. **Mount the storage tank** above the collector (minimum 0.5 m height difference for thermosiphon flow). Connect the collector outlet to the tank top (hot) and tank bottom to the collector inlet (cold) with insulated copper pipe. Slope pipes at 10-20 mm/m toward the collector for drainage.

6. **Fill and bleed**: Fill the system with water. Open the bleed valve at the highest point until water flows (all air purged). Close bleed valve. The system is now ready for thermosiphon circulation — no pump required.

**Strengths**:
- No moving parts or pumps — thermosiphon circulation is entirely passive, requiring no electrical supply
- Buildable with basic materials — copper tubing, flat glass, steel sheet, mineral wool, and matte black paint
- 20-30 year service life — the only wearing component is the selective coating (10-15 years), which can be reapplied
- Reduces fuel consumption 50-70% for domestic hot water heating in sunny climates

**Weaknesses**:
- Maximum outlet temperature of 80°C limits applications to water heating and low-temperature process heat
- No output at night and winter output is 30-40% of summer — requires backup heat source
- Freezing risk in cold climates — must use drain-back design or glycol antifreeze, adding complexity
- Large collector area required per kW of thermal output (~2 m² per kW peak)

### Parabolic Trough Collector

7. **Form the parabolic reflector**: Bend glass sheet into a parabolic curve using a mold and heat, or attach polished aluminum sheet to a parabolic-shaped steel frame. The parabola equation y = x²/(4f) defines the curve, where f is the focal length. For a 2 m aperture width with f = 0.5 m: the focal point is 500 mm above the vertex.

8. **Install the silver backing** (if using glass): Apply silver nitrate solution to the concave surface, reduce to metallic silver. Protect with copper backing and paint. Reflectivity: 90-95%.

9. **Mount the receiver tube** at the focal line. The receiver is a steel tube (50 mm OD) with a selective coating (black chrome electroplated — absorptivity >0.95, emissivity <0.15). Surround the receiver with a glass envelope tube (80 mm OD borosilicate), evacuate to <0.1 Pa (0.001 mbar). The vacuum eliminates convective heat loss from the receiver.

10. **Fabricate the support structure** from galvanized steel. The trough rotates on a single horizontal axis (east-west tracking). Mount the pivot bearings on steel posts set in concrete foundations.

11. **Install the tracking system**: A small gear motor (10-30 W) drives the trough rotation. A shadow-sensor controller (two photovoltaic cells on a divider — motor turns until both cells receive equal light) provides simple, reliable sun tracking. Accuracy: ±0.1°.

12. **Connect the heat transfer loop**: Route heat transfer fluid (mineral oil) through the receiver tube in a closed loop. Install a circulation pump (0.5-1 kW), an expansion tank, a pressure gauge, and a temperature indicator at the receiver outlet.

**Strengths**:
- Achieves 300-500°C outlet temperature — sufficient for steam generation, industrial process heat, and [absorption cooling](cooling.md)
- Modular and scalable — multiple trough sections can be ganged on a common heat transfer loop
- Proven commercial technology — parabolic trough plants have operated since the 1980s with 25+ year lifetimes
- Higher thermal efficiency (55-70%) than flat-plate collectors at temperatures above 80°C

**Weaknesses**:
- Requires curved glass mirrors or precision-formed reflectors — more demanding manufacturing than flat-plate
- Single-axis tracking system adds motors, controllers, bearings, and ongoing maintenance
- Only captures direct normal irradiance (DNI) — diffuse light from clouds is not concentrated
- Higher cost per m² than flat-plate — the reflector, receiver tube, vacuum envelope, and tracker all add expense

## Calibration and Verification

1. **Flat-plate pressure test**: Pressurize the collector tubing at 2 bar for 30 minutes. Zero pressure drop acceptable.

2. **Flat-plate thermal test**: On a clear day with solar irradiance >700 W/m², measure the temperature rise between tank bottom (cold) and collector outlet (hot). Target: 15-30°C at peak sun. Calculate daily thermal output: Q = V × ρ × Cp × ΔT. Target: 6-10 kWh/day for 2 m² in summer.

3. **Parabolic alignment**: Place a target rod at the calculated focal point. Sunlight reflected from the trough should concentrate on a line no wider than 25 mm diameter. Adjust mirror mounting if focal line is wider.

4. **Parabolic thermal test**: At peak sun (DNI >800 W/m²), measure heat transfer fluid temperature rise through the receiver. Target: 30-80°C rise depending on flow rate. Receiver tube temperature should reach 300-500°C at design flow rate.

5. **Tracking accuracy**: Observe the concentrated line on the receiver throughout the day. It should remain centered within ±5 mm of receiver center. Adjust controller sensitivity if tracking drifts.

## Quantitative Parameters

### Flat-Plate Collector

| Parameter | Value |
|-----------|-------|
| Thermal output | 6-10 kWh/day (summer, 2 m², temperate) |
| Peak water temperature | 50-80°C |
| Collector efficiency | 40-55% |
| Stagnation temperature | 120-180°C (no flow) |
| Thermosiphon flow rate | 0.01-0.05 L/s (passive) |
| Service life | 20-30 years (glass cover), 10-15 years (selective coating) |

### Parabolic Trough Collector

| Parameter | Value |
|-----------|-------|
| Thermal output | 5-8 kW peak per 10 m² (DNI >800 W/m²) |
| Receiver temperature | 300-500°C |
| Concentration ratio | 30-100× |
| Collector efficiency | 55-70% |
| Tracking accuracy | ±0.1° (motorized), ±1° (manual) |
| Mirror reflectivity (new) | 90-95% |
| Service life | 25-30 years (mirrors), 15-20 years (selective coating) |

## Collector Type Comparison

| Parameter | Flat-Plate | Evacuated Tube | Parabolic Trough |
|-----------|-----------|----------------|-----------------|
| Outlet temperature | 40-80°C | 80-200°C | 300-500°C |
| Efficiency (at design temp) | 40-55% | 50-70% | 55-70% |
| Tracking required | No | No | Single-axis |
| Cost per m² | Lowest | Medium | Highest |
| Complexity to build | Low | Medium | High |
| Freeze protection | Drain-back or glycol | Not needed (vacuum insulated) | Not needed (heat transfer fluid) |
| Best application | Domestic hot water, space heating | Process heat, cold-climate hot water | Steam generation, industrial process heat |
| Buildable with bootstrap tech? | Yes (Year 5-10) | Yes (Year 10-15, glass skill) | Yes (Year 15-20, metalworking) |

### Evacuated-Tube Collector

An alternative to flat-plate collectors that achieves higher temperatures (80-200°C) without concentration. Each tube consists of two concentric glass tubes with vacuum between them (eliminating convective heat loss). The inner tube has a selective coating (absorptivity >0.95, emissivity <0.06). Heat pipe or direct-flow designs transfer heat from the inner tube to a manifold.

- **Construction**: Borosilicate glass tubes, 40-70 mm OD, 1.2-2.0 m long, sealed at one end. The vacuum (<0.01 Pa) provides insulation equivalent to 100 mm of mineral wool. No tracking required.
- **Performance**: Collector efficiency 50-70% at 80°C outlet (flat-plate drops to 25-35% at this temperature). Each tube produces 50-80 W peak. Tubes can be individually replaced without draining the system.
- **Application**: Medium-temperature process heat (80-150°C), solar cooling (absorption chiller drive), domestic hot water in cold climates (vacuum insulation eliminates freeze risk).
- **Limitation**: Fragile — glass tubes break under impact. Manufacturing borosilicate glass tubes with vacuum seals requires precision glassworking capability. Higher cost per m² than flat-plate.

The vacuum inside each tube must be maintained at <0.01 Pa (0.0001 mbar) for effective insulation. Loss of vacuum is visible as condensation or fogging on the inner surface of the outer tube. Individual tube replacement takes minutes without draining the system — this is a significant maintenance advantage over flat-plate collectors where a single leak can require full system drainage.

## Scaling Notes

| Scale | Collector Area | Thermal Output (summer) | Application | Estimated Cost |
|-------|---------------|------------------------|-------------|----------------|
| Household hot water | 2-4 m² flat-plate | 8-15 kWh/day | Domestic hot water (150-300 liters) | $300-800 |
| Multi-family building | 10-30 m² flat-plate | 40-100 kWh/day | Hot water for 10-30 apartments | $2,000-8,000 |
| Process heat (low-temp) | 50-200 m² flat-plate | 200-700 kWh/day | Food drying, washing, pasteurization | $10,000-50,000 |
| Process heat (medium) | 50-100 m² evacuated tube | 200-500 kWh/day | Industrial cleaning, chemical processing | $20,000-60,000 |
| Steam generation | 500-2000 m² parabolic trough | 250-1500 kWh/day | Steam for engines or industrial process | $100,000-500,000 |

Solar thermal output is seasonal. In temperate latitudes (40-50°), summer output is 3-5× winter output for flat-plate collectors. Parabolic troughs with tracking lose less in winter because they track the sun. System sizing should be based on the application's minimum heat requirement and supplemented with fuel-fired backup during low-solar periods.

Minimum economic scale: a 2 m² flat-plate collector for household hot water, replacing 3-5 kg/day of fuelwood or 1-2 kg/day of LPG. Payback time: 1-3 years in fuel savings. Below this scale, the labor of construction exceeds the value of fuel saved.

For parabolic trough systems, the minimum economic scale is approximately 10 m² aperture (one trough module), producing 5-8 kW peak thermal output. At this scale, the trough can drive a small [absorption chiller](cooling.md) or supplement a [boiler](boiler.md) for steam generation. The tracking system cost is amortized over a larger collector area, making multi-trough arrays (50-200 m²) more economical per installed kW than single troughs.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Flat-plate output lower than expected | Air leak under glass cover (moisture condensation visible) | Reseal the glass-to-frame gasket with silicone; check for frame corrosion creating gaps |
| Flat-plate output lower than expected | Selective coating degraded (visible fading) | Reapply selective coating (black chrome electroplating or solar paint); the coating lifetime is 10-15 years |
| Parabolic trough not reaching design temperature | Mirror reflectivity reduced by dust or oxidation | Clean mirrors with water and soft cloth monthly in dusty environments; re-silver if reflectivity drops below 80% |
| Parabolic trough not reaching design temperature | Misaligned tracking or focal point shifted | Recheck parabolic curve with a straightedge; verify receiver tube is at calculated focal distance; recalibrate sun sensor |
| Thermosiphon not circulating (flat-plate) | Airlock in piping or insufficient height difference | Bleed air from the highest point; verify tank bottom is ≥0.5 m above collector top; check that pipes slope upward from collector to tank |
| Overheating and boiling (stagnation) | Pump failure or no hot water draw during peak sun | Install a heat dissipation radiator or shade the collector during extended idle periods; stagnation temperature (120-180°C) can damage some components |
| Evacuated tube condensation inside outer tube | Vacuum lost (tube compromised) | Replace the tube — vacuum loss eliminates insulation and the tube performs no better than single-glazing |
| Heat transfer fluid degradation | Mineral oil oxidized (darkened, thickened) | Drain and replace fluid; mineral oil has a service life of 3-5 years at 250-300°C. Install a nitrogen blanket in the expansion tank to slow oxidation |

## Quality Control

- **Flat-plate pressure test**: Pressurize absorber tubing at 2 bar for 30 minutes before assembly into the collector box. Zero pressure drop. After installation, re-test at 1.5× operating pressure.
- **Flat-plate thermal performance**: Measure daily heat output Q = V × ρ × Cp × ΔT for at least 3 clear days. Compare to calculated output: Q = Aperture area × Solar irradiance × Collector efficiency (from manufacturer curve at operating ΔT). Actual output within 85-115% of calculated is acceptable.
- **Parabolic focal alignment**: Place a target rod at the calculated focal point. The concentrated image should be a line no wider than 25 mm (for a 50 mm receiver tube, this means >50% of reflected energy strikes the receiver). Check alignment at solar noon and ±2 hours.
- **Parabolic mirror reflectivity**: Measure with a reflectometer. New mirrors: 90-95%. Below 80%: clean and re-silver. Below 70%: replace.
- **Selective coating absorptivity/emissivity**: Test with a spectrophotometer (if available) or by comparing stagnation temperature to theoretical — a stagnation temperature below 150°C for a well-insulated flat-plate collector indicates degraded coating.
- **Tracking accuracy (parabolic)**: Log receiver temperature throughout the day. Temperature should peak within ±10 minutes of solar noon and not drop more than 10% during midday tracking. Step losses (tracking stops for >5 minutes) indicate controller or motor problems.
- **System annual performance**: Install a heat meter (flow meter + temperature sensors on supply and return). Record total thermal energy produced monthly. Compare to expected output based on local solar resource data. Annual output within ±15% of prediction indicates a healthy system.

A simple field test for flat-plate collector performance: on a clear day with solar irradiance >700 W/m², measure the temperature rise between the tank bottom (cold inlet) and collector outlet (hot outlet). A 2 m² collector should produce 15-30°C temperature rise at peak sun with thermosiphon flow. Less than 10°C rise indicates poor absorber coating, air leaks, or insulation problems.

## Safety

- **Parabolic concentrated flux**: Reflected sunlight from trough concentrators produces flux densities of 50-100 kW/m² at the focal line — sufficient to ignite clothing, melt plastics, and cause retinal damage within seconds. Never look directly at the receiver from within the mirror field. Install warning signs. Fencing around parabolic arrays is mandatory.
- **Hot heat transfer fluid**: Mineral oil at 300°C causes immediate deep-tissue burns on skin contact — the oil adheres and continues to transfer heat. Use insulated piping (minimum 50 mm mineral wool + aluminum jacket) on all lines above 60°C. Never open a pressurized hot oil line — the fluid may flash to vapor. Wear long sleeves, heat-resistant gloves, and face shield when working on hot oil systems.
- **Evacuated tube implosion**: Evacuated glass tubes are under external atmospheric pressure (101 kPa). A tube break produces a violent implosion with glass fragments traveling at high speed. Wear safety glasses when handling tubes. Wrap tubes in cloth during transport. Replace cracked tubes immediately — they are a laceration hazard.
- **Stagnation burns**: Flat-plate collectors reach 120-180°C when fluid is not circulating (pump failure, power outage). The absorber plate, glass cover, and nearby piping are dangerously hot. Allow 2+ hours of shade or night cooling before servicing a stagnated collector.
- **Freeze damage**: In cold climates, water-filled flat-plate collectors can freeze and burst copper tubing. Use a drain-back system (collector drains when pump stops) or fill with propylene glycol antifreeze (30-50% concentration protects to -20°C to -40°C). Do not use ethylene glycol — it is toxic if leaked into potable water.
- **Pressure buildup (parabolic trough)**: Heat transfer fluid expands with temperature — mineral oil expands approximately 7% from 20°C to 300°C. Install an expansion tank sized to accommodate this volume change. Without an expansion tank, pressure builds until a fitting or joint fails.

## References

- [Solar Thermal Energy](solar-thermal.md) — full coverage of solar thermal technologies, heliostats, and thermal storage
- [Steam Power](steam-power.md) — steam generation from solar-heated fluid
- [Steam Turbines](steam-turbines.md) — power generation from solar-generated steam
- [Glass Manufacturing](../glass/basic.md) — mirror and cover glass production
- [Copper & Bronze](../metals/copper-bronze.md) — tubing for absorber plates and receivers
- [Cooling Systems](cooling.md) — absorption cooling driven by solar heat
- [Fuels](fuels.md) — comparative energy sources for backup heating

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
