# Solar Thermal Energy

> **Node ID**: energy.solar-thermal
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels.charcoal`](charcoal.md), [`ceramics.pottery`](../ceramics/pottery.md), [`metals.copper-bronze`](../metals/copper-bronze.md)
> **Enables**: [`energy.steam-power`](steam-power.md), [`energy.electricity`](electricity.md)
> **Timeline**: Years 5-30
> **Outputs**: solar_heat, solar_steam, concentrated_solar_power, solar_furnace_heat
> **Critical**: No — supplemental energy source that reduces fuel consumption and enables high-temperature processes without electricity


Solar thermal energy captures concentrated sunlight to produce heat at temperatures from 80°C (water heating) to 3,500°C (solar furnaces). Unlike photovoltaic panels that convert light directly to electricity, solar thermal systems use mirrors and lenses to focus sunlight onto a receiver, generating intense heat that can drive steam turbines, power industrial processes, or melt metals. The technology spans from simple flat-plate water heaters (achievable with wood, glass, and copper) to heliostat fields with central towers (requiring precision optics and control systems).

Solar thermal fills a gap in the bootstrap energy chain: it provides high-temperature heat without consuming fuel, and does so with infrastructure that scales from individual workshops to utility-scale power plants. A 10 m² parabolic trough collector in a sunny region delivers 5-8 kW thermal peak — enough to run a small steam engine or heat a kiln. At utility scale, concentrated solar power (CSP) plants deliver 50-500 MW with thermal energy storage for nighttime operation.

## Prerequisites

## Materials

- **Glass** — Flat window glass (3-6 mm) for flat-plate collectors; curved or bent glass for parabolic troughs. See [Glass](../glass/basic.md).
- **Copper tubing** — For heat exchangers and absorber plates. See [Copper & Bronze](../metals/copper-bronze.md).
- **Mirror material** — Silvered glass (silver deposit on glass backing), polished metal (aluminum, stainless steel), or aluminized polymer film.
- **Steel** — For structural supports, tracking mechanisms, and receiver tubes. See [Iron & Steel](../metals/iron-steel.md).
- **Insulation** — Mineral wool, fiberglass, or cork for reducing thermal losses from receivers and piping.
- **Heat transfer fluid** — Water, mineral oil, or molten salt (sodium nitrate/potassium nitrate eutectic) depending on operating temperature.

## Tools and Equipment

- **Glass bending/forming** — For parabolic trough reflectors. See [Glass](../glass/basic.md).
- **Metalworking** — Cutting, welding, and bending copper and steel. See [Machine Tools](../machine-tools/index.md).
- **Pumps and piping** — Circulating heat transfer fluid. See [Steam Power](steam-power.md).
- **Tracking mechanism** — Clockwork, weight-driven, or motorized sun-tracking for concentrators.

## Knowledge

- Solar geometry (declination, hour angle, altitude/azimuth)
- Optics (reflection, focal length, concentration ratio)
- Heat transfer (conduction, convection, radiation)

## Bill of Materials

## Flat-Plate Solar Water Heater (2 m² collector, 200 liter tank)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Copper tubing (15 mm OD, 1 mm wall) | 15-20 m | [Copper & Bronze](../metals/copper-bronze.md) | Stainless steel tubing (lower conductivity) |
| Flat glass sheet (4 mm, 2 m²) | 1 sheet | [Glass](../glass/basic.md) | Polycarbonate sheet (lower temp rating, UV degrades) |
| Steel sheet (1 mm, absorber plate backing) | 2 m² | [Iron & Steel](../metals/iron-steel.md) | Aluminum sheet |
| Mineral wool insulation (50 mm) | 4 m² | [Chemistry](../chemistry/index.md) | Cork, straw (lower R-value) |
| Steel or copper tank (200 liter) | 1 unit | [Metals](../metals/index.md) | Concrete tank with waterproof liner |
| Black paint (matte, high absorptivity) | 1 liter | [Chemistry](../chemistry/index.md) | Soot mixed with linseed oil |
| Silicone or rubber gasket | 5 m | [Polymers](../polymers/index.md) | Clay/putty seal (less durable) |

## Parabolic Trough Collector (10 m² aperture)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Curved glass mirror (4 mm, 10 m²) | 10 m² | [Glass](../glass/basic.md) | Polished aluminum sheet (70-80% reflectivity vs 90-95% for silvered glass) |
| Steel receiver tube (50 mm OD) with selective coating | 5-8 m | [Iron & Steel](../metals/iron-steel.md) | Copper tube (better conductivity, lower max temp) |
| Pyrex/glass envelope tube (80 mm OD) | 5-8 m | [Glass](../glass/basic.md) | None — needed for vacuum insulation |
| Steel support structure | 50-80 kg | [Iron & Steel](../metals/iron-steel.md) | Wood (limited lifespan, lower rigidity) |
| Heat transfer fluid (mineral oil) | 50-100 liters | [Chemistry](../chemistry/index.md) | Water (limited to 100°C at atmospheric pressure) |
| Tracking mechanism (gear motor, controller) | 1 unit | [Electronics](../electronics/index.md) | Manual adjustment (labor-intensive) |

## Process Description

## 4.1 Solar Water Heating (Flat-Plate Collector)

1. **Build the absorber plate**: Paint a copper or steel sheet matte black (absorptivity >0.95). Solder or braze copper tubing in a serpentine pattern on the back of the plate. The tubing carries water or heat transfer fluid.

2. **Assemble the collector box**: Construct a shallow wooden or metal box (100-150 mm deep). Install the absorber plate inside on 50 mm mineral wool insulation. Cover the top with a single pane of glass, sealed with a rubber gasket. The air gap between glass and absorber (25-40 mm) provides greenhouse-effect insulation.

3. **Connect the storage tank**: Position the storage tank above the collector. Use thermosiphon circulation — hot water rises from collector to tank, cold water descends from tank to collector — no pump needed. Pipe runs should be short (<3 m) and insulated with 25 mm mineral wool.

4. **Fill and bleed**: Fill the system with water. Bleed all air from the collector tubing (air pockets block thermosiphon flow).

 5. **Operate**: The collector heats water to 50-80°C on sunny days. A 2 m² collector in a temperate climate produces 6-10 kWh thermal per day in summer, 2-4 kWh in winter.

**Materials**:
- [Copper tubing](../metals/copper-bronze.md) (15 mm OD, 1 mm wall, 15-20 m serpentine)
- [Flat glass sheet](../glass/index.md) (4 mm thick, 2 m², low-iron tempered glass preferred)
- [Steel sheet](../metals/iron-steel.md) (1 mm thick, 2 m², absorber plate backing)
- [Mineral wool insulation](../chemistry/index.md) (50 mm thick, 4 m², 50-100 kg/m³ density)
- [Steel or copper storage tank](../metals/index.md) (200 liter, 1.5 mm wall minimum)
- [Black paint](../chemistry/index.md) (matte, solar absorptivity >0.95)
- [Silicone or rubber gasket](../polymers/index.md) (5 m, food-grade silicone, 3-5 mm diameter cord)

**Calibration / Verification**:
1. After assembly, pressure-test the collector loop at 2 bar for 30 minutes (no pressure drop acceptable).
2. Fill with water and bleed all air from the collector tubing through the bleed valve at the highest point.
3. On a clear day with solar irradiance >700 W/m², measure the temperature rise between tank bottom (cold) and collector outlet (hot) (target: 15-30°C temperature rise at peak sun).
4. Calculate daily thermal output: Q = V × ρ × Cp × ΔT (target: 6-10 kWh/day in summer for 2 m² collector in temperate climate).
5. Verify thermosiphon flow by touching the flow and return pipes — the flow pipe from collector top should be noticeably hotter than the return pipe from tank bottom.

**Expected Performance**:
- Thermal output: 6-10 kWh/day in summer, 2-4 kWh/day in winter (2 m² collector, temperate climate)
- Peak water temperature: 50-80°C on sunny days
- Collector efficiency: 40-55% (thermal energy collected / solar energy incident)
- Stagnation temperature: 120-180°C (unpressurized, no flow — design venting to prevent steam)
- Thermosiphon flow rate: 0.01-0.05 L/s (no pump required)

**Strengths**:
- No moving parts or pumps — thermosiphon circulation is passive and maintenance-free
- Buildable with basic materials (copper tubing, flat glass, steel sheet)
- 20-30 year operational lifetime with minimal maintenance (clean glass annually)
- Reduces water heating fuel consumption by 50-70% in temperate climates

**Weaknesses**:
- No output at night or during heavy overcast — requires backup heating for hot water
- Seasonal variation — winter output is 30-40% of summer output
- Freezing risk in cold climates — requires drain-back design or antifreeze in closed loop
- Low maximum temperature (80°C) limits applications to water heating and space heating

## 4.2 Parabolic Trough Concentrator

1. **Form the parabolic reflector**: Bend glass sheet into a parabolic curve using a mold and heat, or attach polished aluminum sheet to a parabolic-shaped steel frame. The parabola focuses sunlight onto a line (the receiver tube) running along the focal axis. For a trough with 2 m aperture width and 1.5 m focal length: focal point diameter ≈ 15-25 mm.

2. **Install the receiver tube**: The receiver is a steel tube (50 mm OD) with a selective coating (black chrome or black nickel electroplated — absorptivity >0.95, emissivity <0.15). Surround the receiver with a glass envelope tube and evacuate to <0.01 Pa to eliminate convective heat loss. The selective coating and vacuum together reduce thermal losses by 80-90% compared to a bare black tube.

3. **Mount the trough on a tracking system**: A single-axis tracking system rotates the trough east-to-west to follow the sun. Use a clockwork mechanism, a shadow-sensor controller (two photovoltaic cells on a divider — the motor turns until both cells receive equal light), or a computed solar position algorithm with a microcontroller.

4. **Connect the heat transfer loop**: Pump heat transfer fluid (mineral oil for 150-300°C, synthetic oil for 300-400°C, molten salt for 400-560°C) through the receiver tubes. The heated fluid circulates to a heat exchanger that generates steam.

 5. **Generate power or process heat**: Route steam to a turbine-generator set (see [Steam Turbines](steam-turbines.md)) or use the heat directly for industrial processes (drying, distillation, cooking, metal melting).

**Materials**:
- [Curved glass mirror](../glass/index.md) (4 mm thick, 10 m² aperture, silvered glass reflectivity 90-95%)
- [Steel receiver tube](../metals/iron-steel.md) (50 mm OD, selective coating absorptivity >0.95, emissivity <0.15)
- [Pyrex/glass envelope tube](../glass/index.md) (80 mm OD, evacuated to <0.01 Pa)
- [Steel support structure](../metals/iron-steel.md) (50-80 kg, galvanized or painted)
- [Heat transfer fluid](../chemistry/index.md) (mineral oil, 50-100 liters, rated to 300°C)
- [Tracking mechanism](../electronics/index.md) (gear motor + shadow sensor controller)

**Calibration / Verification**:
1. Align the trough to true south (northern hemisphere) and verify tracking axis is level (±0.5° tolerance using a precision spirit level).
2. Check parabolic shape accuracy by placing a straight edge across the trough at multiple points — maximum gap should be <5 mm over the full length.
3. Measure receiver tube focal alignment: place a target rod at the calculated focal point. Sunlight reflected from the trough should concentrate on a spot no wider than 25 mm diameter.
4. Measure heat transfer fluid temperature rise at peak sun (target: 30-80°C rise depending on flow rate).
5. Verify tracking accuracy by observing the concentrated line on the receiver — it should remain centered throughout the tracking day (tolerance: ±5 mm deviation from receiver center).

**Expected Performance**:
- Thermal output: 5-8 kW thermal peak per 10 m² collector in DNI >800 W/m²
- Receiver tube temperature: 300-500°C with mineral oil or molten salt
- Concentration ratio: 30-100x (aperture area / receiver area)
- Collector efficiency: 55-70% at design conditions
- Tracking accuracy: ±0.1° (motorized), ±1° (manual)

**Strengths**:
- Achieves temperatures (300-500°C) suitable for steam generation and industrial processes
- Modular — multiple troughs can be ganged to increase output
- Well-proven technology with decades of commercial operation
- Thermal energy storage (molten salt) enables output after sunset

**Weaknesses**:
- Requires curved glass or precision-formed reflectors — not achievable without glass manufacturing
- Tracking system (motorized) adds complexity, power consumption, and maintenance
- Single-axis tracking loses 10-15% of available energy vs. two-axis tracking
- Concentrated flux creates safety hazards (burn risk, retinal damage)

## 4.3 Heliostat Field (Central Receiver)

1. **Construct heliostats**: Each heliostat is a flat mirror (2-10 m²) on a two-axis tracking mount. The mirror tracks the sun and reflects beam onto a fixed central receiver at the top of a tower. Typical field: 100-10,000 heliostats surrounding the tower.

2. **Build the central receiver**: A heat exchanger mounted on a tower (50-150 m height). The receiver absorbs concentrated sunlight from all heliostats simultaneously. Flux densities reach 200-1,000 kW/m². Construct from high-temperature alloy tubes (Inconel or stainless steel) carrying molten salt or supercritical steam.

 3. **Thermal storage**: Store heat in a two-tank molten salt system — one hot tank (565°C), one cold tank (290°C). Draw hot salt through a steam generator when power is needed. Storage capacity of 2-15 hours enables nighttime generation. Molten salt: 60% NaNO₃ + 40% KNO₃ (Solar Salt), melting point 220°C.

**Materials**:
- [Flat glass mirrors](../glass/index.md) (2-10 m² per heliostat, silvered, 4 mm thick)
- [Two-axis tracking mount](../electronics/index.md) (steel frame, gear motors, azimuth + elevation actuators)
- [Central receiver](../metals/index.md) (Inconel or stainless steel 316L tubes, 50-80 mm OD, rated to 600°C)
- [Tower structure](../metals/iron-steel.md) (steel lattice, 50-150 m height)
- [Molten salt](../chemistry/index.md) (60% NaNO₃ + 40% KNO₃, "Solar Salt," melting point 220°C, 500-5,000 tonnes)
- [Hot and cold salt tanks](../metals/iron-steel.md) (carbon steel shell, insulated, 10-40 m diameter)

**Calibration / Verification**:
1. Calibrate each heliostat individually: command it to reflect sunlight onto a target on the tower. Measure beam centroid position — must be within ±1 m of receiver center at 100 m tower height (±0.5° pointing accuracy).
2. Verify receiver tube surface temperature with infrared pyrometer during first operation (target: 500-600°C at design DNI). Exceeding 650°C risks receiver tube failure.
3. Measure molten salt flow rate and temperature rise through receiver (target: 290°C inlet, 565°C outlet at design conditions).
4. Test thermal storage: charge the hot tank, then discharge through steam generator at rated power. Verify discharge duration matches design (target: 2-15 hours at rated thermal output).
5. Check salt chemistry quarterly: nitrate/nitrite ratio, chloride content (<100 ppm), and melting point (220°C ±5°C).

**Expected Performance**:
- Central receiver flux density: 200-1,000 kW/m² (at design DNI of 800-1,000 W/m²)
- Receiver thermal output: 50-500 MW thermal depending on heliostat field size
- Concentration ratio: 300-1,500x
- Thermal storage capacity: 2-15 hours of full-load generation
- Overall solar-to-electric efficiency: 15-25%
- Heliostat field availability: >98% (individual heliostat failures do not shut down the plant)

**Strengths**:
- Highest operating temperature of any solar thermal technology (500-1,000+°C)
- Thermal storage (molten salt) enables generation on demand, day or night
- Decoupled energy collection (heliostats) and power conversion (receiver + turbine)
- Utility-scale power output (50-500 MW) matches conventional power plants

**Weaknesses**:
- Most complex solar thermal technology — hundreds of precision tracking mirrors and a central control system
- Requires tall tower (50-150 m) — major civil engineering project
- Molten salt freezes below 220°C — all salt piping requires heat tracing and careful thermal management
- Minimum economic scale of 50 MW — not suitable for small installations

## Quantitative Parameters

## 5.1 Concentration Ratios and Achievable Temperatures

| System Type | Concentration Ratio | Peak Temperature (°C) | Thermal Efficiency (%) | Aperture Area per kW thermal |
|-------------|--------------------|-----------------------|----------------------|------------------------------|
| Flat-plate collector | 1x (no concentration) | 80-100 | 40-55 | 2-4 m² |
| Evacuated tube collector | 1x (no concentration) | 120-200 | 45-65 | 1.5-3 m² |
| Parabolic trough | 30-100x | 300-500 | 55-70 | 1.5-2.5 m² |
| Parabolic dish | 500-3,000x | 500-1,500 | 60-75 | 1.2-2.0 m² |
| Heliostat / central tower | 300-1,500x | 500-1,000+ | 55-70 | 1.5-3 m² |
| Solar furnace (fixed concentrator) | 5,000-16,000x | 2,000-3,500 | 40-60 | N/A (research) |

Concentration ratio is the ratio of collector aperture area to receiver area. Higher concentration = higher temperature but tighter tracking tolerances and higher optical precision required.

## 5.2 Direct Normal Irradiance (DNI) by Region

| Region | Annual DNI (kWh/m²/year) | Daily Peak (W/m²) | Suitability |
|--------|--------------------------|--------------------:|-------------|
| Sahara / Arabian Desert | 2,400-2,800 | 900-1,000 | Excellent for all CSP |
| Southwestern US / Mexico | 2,200-2,700 | 850-950 | Excellent for all CSP |
| Mediterranean / North Africa | 1,800-2,400 | 800-900 | Good for trough and tower |
| Temperate (Central Europe) | 1,000-1,400 | 600-750 | Marginal for CSP; good for flat-plate |
| Tropical humid | 1,000-1,500 | 500-700 | Poor for CSP (cloud cover); flat-plate OK |
| Northern latitudes (>55°) | 700-1,000 | 400-600 | Flat-plate water heating only |

CSP (trough and tower) requires DNI >1,800 kWh/m²/year for economic viability. Flat-plate collectors work on diffuse radiation and function in any climate.

## 5.3 Land Area Requirements

| System | Power Output | Land Area | Land Use Factor |
|--------|-------------|-----------|-----------------|
| Parabolic trough plant (50 MW) | 50 MW electric | 125-200 hectares | 2.5-4.0 ha/MW |
| Solar tower plant (100 MW, 10h storage) | 100 MW electric | 350-500 hectares | 3.5-5.0 ha/MW |
| Flat-plate water heating | 2 kW thermal | 4-6 m² | 2-3 m²/kW |
| Solar furnace (Odeillo-type) | 1 MW thermal peak | 2,000 m² (mirror area) | Research scale |

Land use factor for CSP is 2.5-5.0 ha/MW, roughly 3× the land area of equivalent PV due to spacing between collectors and the need for single-axis or dual-axis tracking clearances.

## Scaling Notes

## Bench Scale (1-5 kW thermal)

A single flat-plate collector (2-4 m²) or a small parabolic trough (5 m² aperture) produces 1-5 kW thermal peak. Construction: hand tools, copper tubing, flat glass. Tracking: manual or none (flat-plate). Heat output: 50-80°C water. Sufficient for domestic hot water, small-scale food drying, or preheating boiler feedwater. Build time: 1-3 days.

## Workshop Scale (10-50 kW thermal)

A 20 m² parabolic trough array (4-5 troughs, each 4 m × 1 m aperture) produces 10-20 kW thermal at 200-400°C. Requires: glass bending or polished aluminum reflectors, a pump and heat exchanger, simple sun tracking. Applications: steam generation for a small engine, cooking, industrial drying, metal melting (aluminum, copper). Build time: 2-4 weeks.

## Utility Scale (10-500 MW electric)

A commercial CSP plant requires hundreds of precision-manufactured collector assemblies, a steam turbine-generator, thermal storage, and a power block. Construction: heavy machinery for earthwork, precision manufacturing for mirrors and receivers, electrical engineering for grid connection. Minimum economic scale: 10-50 MW. Build time: 1-3 years. Not achievable in early bootstrap — requires the full industrial ecosystem including glass manufacturing, precision metalworking, and electrical grid infrastructure.

## Key Scale Breakpoints

- **1 kW**: Single flat-plate collector, no tracking, thermosiphon circulation. Buildable with stone-age + copper-age materials.
- **10 kW**: Small parabolic trough, single-axis tracking, pumped circulation. Requires glass bending, copper tubing, basic mechanics.
- **100 kW**: Trough array or dish-Stirling system. Requires precision optics, heat-resistant receiver materials, thermal oil or steam systems.
- **50 MW**: Utility-scale CSP with thermal storage and steam turbine. Requires the full industrial supply chain.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low outlet temperature (<50% of expected) | Cloudy conditions, dirty reflector, air in receiver tube | Clean reflectors; bleed air from heat transfer loop; check DNI with pyranometer |
| Receiver tube overheating (>design limit) | Pump failure or loss of heat transfer fluid flow | Install high-temperature alarm; automatic defocus mechanism (rotate trough away from sun); check pump operation and fluid level |
| Glass envelope breakage on evacuated tube | Thermal shock from cold rain on hot glass, or hail impact | Install hail guards; use borosilicate glass (lower thermal expansion); replace individual tubes |
| Tracking drift (mirror not aimed at sun) | Sensor misalignment, gear wear, or controller failure | Recalibrate sun sensor; inspect and lubricate gears; check controller power supply and software |
| Heat transfer fluid degradation | Mineral oil oxidizes above 300°C; darkens and thickens | Maintain fluid below rated maximum; install inline filter; replace fluid per schedule (2-5 years for mineral oil) |
| Mirror reflectivity loss | Dust, sand, or pollution deposition on mirror surface | Wash mirrors weekly in dry climates (water spray and squeegee); more frequent in dusty environments |
| Thermal storage salt freeze | Molten salt solidifies below 220°C in piping | Trace-heated piping (electrical heat tracing or steam trace); maintain salt temperature >260°C during idle; emergency drain to cold tank |
| Steam generator tube leak | Thermal cycling fatigue, or salt-side corrosion | Inspect tubes with eddy current testing annually; maintain salt chemistry (chlorides <100 ppm); use corrosion-resistant alloys (316L stainless minimum) |

## Safety

## High-Temperature Hazards

- **Receiver tube surfaces**: Parabolic trough receiver tubes reach 300-500°C. Central receiver surfaces exceed 800°C. Direct contact causes immediate severe burns. Install radiation shields and barriers around receiver assemblies. Post temperature warning signs.
- **Concentrated solar flux**: Reflected sunlight from heliostats or dish concentrators produces flux densities capable of igniting clothing and causing instantaneous retinal damage. Never look directly at the receiver from within the mirror field. Workers in heliostat fields must wear UV-protective clothing and avoid standing in reflected beam paths.
- **Heat transfer fluid**: Mineral oil at 300°C causes severe burns on contact. Molten salt at 565°C is a crystalline solid at room temperature but flows like water when heated — a salt spill solidifies into a hard crust that can trap and continue burning underlying material. Use full-face shield, heat-resistant gloves (rated to 500°C), and body protection when handling hot salt systems. Spill containment: concrete berms around salt tanks.

## Glass Hazards

- **Evacuated tube implosion**: Evacuated glass tubes are under atmospheric pressure (1 bar external, vacuum internal). A tube break produces an implosion followed by scatter of glass fragments at high velocity. Wear safety glasses and face shield when handling evacuated tubes. Wrap tubes in protective film to contain fragments if breakage occurs.

## Structural Hazards

- **Wind loading**: Parabolic troughs and heliostats present large sail areas to the wind. At 25 m/s wind speed, a 10 m² heliostat experiences ~3,000 N of force. Design mounting structures for local maximum wind loads with a 1.5× safety factor. Stow mirrors face-down (horizontal) when wind exceeds design speed.
- **Thermal expansion**: Steel receiver tubes expand 6-7 mm per 10 m length per 100°C temperature rise. Provide expansion loops or bellows in piping. Rigidly constrained pipes will buckle and crack.

## Quality Control

## Mirror Reflectivity

Measure specular reflectivity with a reflectometer at the mirror surface. New silvered glass mirrors: 90-95% reflectivity. Acceptable after installation: >88%. Below 85%: clean or replace. Measure annually at 5-10 representative points per collector field.

## Receiver Tube Vacuum

Evacuated receiver tubes must maintain vacuum below 0.1 Pa for effective insulation. Test: measure the temperature of the glass envelope — if the envelope is hot (>60°C when receiver is at operating temperature), vacuum has been lost. Failed tubes show visible getter discoloration (the getter is a barium deposit that turns white when it has absorbed gas). Replace failed tubes — performance drops 30-50% with vacuum loss.

## Heat Transfer Fluid Quality

- **Mineral oil**: Measure acidity (TAN — total acid number). New oil: <0.05 mg KOH/g. Replace when TAN exceeds 0.5 — acidic oil corrodes steel piping. Measure viscosity at 40°C: new oil 20-30 cSt. Replace when viscosity exceeds 40 cSt (oxidation thickening).
- **Molten salt**: Test nitrate/nitrite ratio. Target: 60% NaNO₃ / 40% KNO₃ by weight. Measure chloride content (<100 ppm — chlorides cause stress corrosion cracking in stainless steel). Test melting point: should be 220°C ±5°C. High melting point indicates contamination or incorrect proportions.

## System Thermal Performance

Measure daily thermal energy output: Q = ṁ × Cp × ΔT, where ṁ = mass flow rate (kg/s), Cp = specific heat capacity of fluid (kJ/kg·K), ΔT = temperature difference between outlet and inlet (K). Compare to expected output for the day's DNI. Performance below 80% of theoretical indicates mirror soiling, receiver degradation, or tracking errors.

## Variations and Alternatives

## Comparison of Solar Thermal Technologies

| Technology | Operating Temp | Complexity | Storage | Best For |
|------------|---------------|------------|---------|----------|
| Flat-plate collector | 40-80°C | Low | Hot water tank (50-200 liter) | Domestic hot water, space heating, preheat |
| Evacuated tube collector | 80-200°C | Low-Medium | Hot water or pressurized water | Industrial process heat, absorption cooling |
| Parabolic trough | 150-400°C | Medium | Molten salt or pressurized steam | Power generation, industrial process heat |
| Linear Fresnel | 150-300°C | Medium-Low | Molten salt | Lower-cost alternative to troughs; fixed receiver |
| Parabolic dish + Stirling | 500-800°C | High | None (direct conversion) | Small-scale power generation (5-50 kW) |
| Heliostat / power tower | 500-1,000°C | High | Molten salt (2-15 hours) | Utility-scale power with nighttime generation |
| Solar furnace | 1,000-3,500°C | Very high | None | Materials research, solar chemistry, metal melting |

## Linear Fresnel Reflector

A lower-cost alternative to parabolic troughs: flat mirror strips mounted on the ground, each tilted to reflect sunlight onto a fixed elevated receiver tube. No curved glass needed — flat mirrors are cheaper to manufacture. Concentration ratio: 20-40x. Temperature: 150-300°C. Lower optical efficiency than troughs (60-65% vs 70-75%) but significantly lower capital cost. Easier to clean and maintain (mirrors near ground level).

## Solar Cooking and Drying

Low-temperature solar thermal applications do not require concentration:
- **Solar box cooker**: Insulated box with glass lid and reflector panels. Interior reaches 120-160°C. Cooks food in 1-3 hours. Construction: cardboard, aluminum foil, glass. Buildable at any tech level.
- **Solar food dryer**: Cabinet with solar-heated air intake. Drying temperature 50-70°C. Preserves fruits, vegetables, meat without fuel consumption. Construction: wood, glass, wire mesh.

## See Also

- **[Steam Power](steam-power.md)** — Steam engines driven by solar-generated steam
- **[Steam Turbines](steam-turbines.md)** — Turbine-generator sets for CSP power conversion
- **[Energy Storage](storage.md)** — Thermal energy storage integration with CSP
- **[Electricity Generation](electricity.md)** — Grid connection for CSP power plants
- **[Power Distribution](power-distribution.md)** — Transformers and grid infrastructure for utility-scale CSP
- **[Glass Manufacturing](../glass/index.md)** — Mirror and receiver tube glass production
- **[Copper & Bronze](../metals/copper-bronze.md)** — Copper tubing for heat exchangers
- **[Iron & Steel](../metals/iron-steel.md)** — Structural steel for collector mounts and piping



[← Back to Energy](index.md)
