# Geothermal Energy

> **Node ID**: energy.geothermal
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.steam-power`](steam-power.md), [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](electricity.md)
> **Enables**: [`energy.electricity`](electricity.md), [`energy.cooling`](cooling.md)
> **Timeline**: Years 20-50
> **Outputs**: geothermal_heat, geothermal_steam, geothermal_electricity, ground_source_heat_pump
> **Critical**: No — geothermal energy is regionally specific, providing baseload power where geological conditions permit

## 1. Overview

Geothermal energy harnesses heat from the Earth's interior, accessed either through natural hydrothermal manifestations (hot springs, geysers, fumaroles) or by drilling wells into hot rock formations. The Earth's interior heat flows outward at an average rate of 0.06 W/m² at the surface — too diffuse for economic extraction in most locations. However, in tectonically active regions (volcanic zones, fault boundaries, hot spot tracks), heat flow is 10-100× the average, making geothermal energy extraction practical and economically competitive.

Geothermal energy is unique among renewable sources: it provides continuous baseload power, unaffected by weather, seasons, or time of day. A geothermal power plant achieves 90-95% capacity factor (actual output / rated capacity), compared to 15-35% for wind and solar. This makes geothermal the most reliable renewable energy source — and the only one that can fully replace fossil-fueled baseload plants without storage.

Three technology tiers are covered: direct-use heating (hot water from shallow wells for building heating, greenhouses, and industrial processes), hydrothermal power generation (steam from deep wells driving turbines), and ground-source heat pumps (using shallow ground as a heat source/sink for heating and cooling).

## 2. Prerequisites

### Materials

- **Steel casing and tubing** — Well casing (200-500 mm diameter, 8-12 mm wall, API grade J55 or K55). Production tubing (75-150 mm). See [Iron & Steel](../metals/iron-steel.md).
- **Cement** — Well cement (API Class G or H) for casing-to-borehole annulus seal. See [Chemistry](../chemistry/index.md).
- **Reinforced concrete** — For power plant foundations, cooling tower basins, and containment structures.
- **Copper tubing** — For heat exchangers in binary cycle plants and ground-source heat pumps. See [Copper & Bronze](../metals/copper-bronze.md).
- **Refrigerant or working fluid** — Isobutane, isopentane, or R245fa for binary cycle plants; water/steam for flash plants. See [Chemistry](../chemistry/index.md).
- **HDPE or steel pipe** — For ground-source heat pump ground loops. See [Polymers](../polymers/index.md).

### Tools and Equipment

- **Drilling rig** — Rotary drilling rig capable of 500-3,000 m depth. See [Mining](../mining/index.md).
- **Wellhead equipment** — Blowout preventer, master valves, casing heads. See [Metals](../metals/index.md).
- **Steam turbine-generator** — For flash and dry steam plants. See [Steam Turbines](steam-turbines.md).
- **Pumps** — Downhole production pumps (for liquid-dominated wells), circulation pumps for binary cycle and heat pump systems. See [Steam Power](steam-power.md).

### Knowledge

- Geothermal resource assessment (temperature gradient drilling, geochemical surveys, resistivity surveys)
- Well drilling and completion in hard, hot rock formations
- Corrosion engineering (geothermal fluids are highly corrosive — H₂S, CO₂, chlorides, silica)

## 3. Bill of Materials

### Small Geothermal Direct-Use Heating System (500 kW thermal)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Steel well casing (200 mm, 8 mm wall) | 200-500 m | [Iron & Steel](../metals/iron-steel.md) | Fiberglass casing (lower temp rating, non-corrosive) |
| Cement (API Class G) | 20-50 tonnes | [Chemistry](../chemistry/index.md) | Standard Portland cement (lower temp resistance) |
| Steel production tubing (100 mm) | 200-500 m | [Iron & Steel](../metals/iron-steel.md) | Fiberglass tubing (corrosion-resistant, lower strength) |
| Plate heat exchanger (stainless steel 316L) | 1 unit | [Metals](../metals/index.md) | Shell-and-tube heat exchanger (larger, heavier) |
| HDPE distribution pipe (50-100 mm) | 500-2,000 m | [Polymers](../polymers/index.md) | Steel pipe (heavier, requires corrosion protection) |
| Circulation pump (5-15 kW) | 2 units | [Energy](./index.md) | None — electric pump required |
| Insulation (mineral wool, 50 mm) | 200-500 m² | [Chemistry](../chemistry/index.md) | Polyurethane foam (better R-value, higher cost) |

### Ground-Source Heat Pump (10 kW heating/cooling for a building)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| HDPE ground loop pipe (32 mm) | 300-500 m | [Polymers](../polymers/index.md) | Copper tubing (higher conductivity, corrosion risk) |
| Heat pump unit (compressor, evaporator, condenser) | 1 unit | [Energy](./index.md) | Absorption heat pump (lower COP, no compressor) |
| Bentonite grout (for borehole backfill) | 500-1,500 kg | [Chemistry](../chemistry/index.md) | Sand backfill (lower thermal conductivity) |
| Antifreeze fluid (propylene glycol, 25%) | 200-400 liters | [Chemistry](../chemistry/index.md) | Ethanol/water mix (lower freeze point, flammable) |

## 4. Process Description

### 4.1 Direct-Use Heating

1. **Drill a production well**: Drill into the geothermal reservoir using rotary drilling (tricone bit with drilling mud circulation). Target depth: 100-1,000 m depending on local temperature gradient. Typical gradient: 25-30°C/km in normal areas, 50-100°C/km in active geothermal zones.

2. **Complete the well**: Run steel casing into the borehole and cement the annulus. Perforate the casing at the production zone (geothermal aquifer) using shaped charges or a rotary mill. Install a downhole pump if the well does not flow artesian (most geothermal wells with temperatures 60-100°C are pumped).

3. **Produce hot fluid**: Pump geothermal fluid (water at 60-150°C) to the surface. Flow rate: 10-50 liters/second depending on well productivity and temperature. Typical well produces 0.5-5 MW thermal.

4. **Exchange heat**: Route geothermal fluid through a plate heat exchanger. The primary (geothermal) side heats clean secondary water in a closed loop. Heat exchanger prevents geothermal fluid (often corrosive and mineral-laden) from contacting the distribution system.

5. **Distribute heat**: Pump heated secondary water through insulated pipes to end users — building heating (radiators or underfloor), greenhouse heating, fish farming ponds, industrial drying, or lumber kilns.

6. **Reinject or dispose**: Spent geothermal fluid (cooled to 30-50°C) is reinjected into the reservoir through an injection well. Reinjection maintains reservoir pressure, prevents subsidence, and avoids surface water contamination. Locate injection well at least 500-1,000 m from production well to prevent premature thermal breakthrough.

### 4.2 Flash Steam Power Generation

1. **Drill deep production wells**: Target depth: 1,000-3,000 m into liquid-dominated geothermal reservoirs at 180-350°C. Well diameter: 200-300 mm. Multiple wells required (5-20 production wells for a 50 MW plant).

2. **Flash the brine**: Geothermal fluid arrives at the surface as pressurized hot water (>180°C). Route to a flash separator (pressure vessel) where pressure drops suddenly. The pressure drop causes a fraction of the water to flash to steam — typically 15-30% by mass at 180-250°C. Single-flash: one pressure stage. Double-flash: a second, lower-pressure flash extracts additional steam from the remaining liquid, increasing output by 15-25%.

3. **Drive the turbine**: Direct the separated steam through a steam turbine (see [Steam Turbines](steam-turbines.md)). Turbine inlet conditions: 5-15 bar, 150-250°C (low compared to fossil fuel plants at 100-240 bar, 540-600°C). Geothermal steam turbines use larger blade passages to handle higher flow volumes at lower pressures. Typical unit size: 20-120 MW.

4. **Condense and reinject**: Exhaust steam from the turbine enters a condenser (either water-cooled surface condenser or direct-contact condenser). Non-condensable gases (NCG — CO₂, H₂S, NH₃, CH₄, N₂) are removed by a gas extraction system (steam jet ejectors or vacuum pumps). NCG is 1-10% of steam flow by weight and must be removed to maintain condenser vacuum. Condensed water and remaining brine are reinjected.

5. **Treat NCG**: H₂S in NCG stream is toxic and odorous. Remove with a chemical scrubber (iron chelate or caustic soda) before venting CO₂ to atmosphere. Alternatively, convert H₂S to elemental sulfur via the Claus process for sale as a byproduct.

### 4.3 Ground-Source Heat Pump

1. **Install ground loop**: Bore vertical holes (50-200 m deep, 100-150 mm diameter) and insert HDPE U-tube loops. For a 10 kW heat pump, install 2-4 boreholes of 100 m depth each. Backfill boreholes with bentonite grout to ensure thermal contact between pipe and surrounding ground and to prevent aquifer cross-contamination. Alternatively, lay horizontal loops in trenches (1.5-2.0 m depth) if land area permits — requires 300-500 m² per 10 kW.

2. **Connect to heat pump**: The ground loop circulates a water-antifreeze mixture at 5-15°C (heating mode) or 20-30°C (cooling mode). The heat pump's evaporator extracts heat from the ground loop (heating mode) and the compressor raises the temperature to 40-60°C for distribution. In cooling mode, the cycle reverses — the heat pump rejects building heat into the ground loop.

3. **Distribute heating/cooling**: Heated water (40-60°C) feeds underfloor heating, radiators, or fan-coil units. Cooled water (7-12°C) feeds fan-coil units or chilled beams. COP (coefficient of performance): 3.0-5.0 for heating, 3.5-6.0 for cooling. A heat pump delivering 10 kW of heating draws only 2.5-3.5 kW of electricity — the remaining 6.5-7.5 kW comes from the ground.

## 5. Quantitative Parameters

### 5.1 Temperature Gradient and Well Depth

| Resource Type | Gradient (°C/km) | Well Depth (m) | Fluid Temperature (°C) | Application |
|---------------|-------------------|-----------------|------------------------|-------------|
| Normal (non-geothermal) | 20-30 | N/A (not economic) | <50 at depth | Ground-source heat pump only |
| Enhanced (moderate) | 40-60 | 1,000-2,000 | 80-150 | Direct-use heating |
| Hydrothermal (high) | 60-100+ | 500-3,000 | 150-350 | Flash steam power generation |
| Magmatic (volcanic) | 100-200+ | 500-2,000 | 250-400+ | Dry steam or supercritical |

### 5.2 Geothermal Power Plant Performance

| Plant Type | Resource Temp (°C) | Capacity (MW) | Thermal Efficiency (%) | Availability (%) | Cost ($/kW installed) |
|------------|-------------------|----------------|------------------------|-------------------|----------------------|
| Dry steam | 200-300+ | 20-150 | 15-20 | 90-97 | 1,500-3,000 |
| Single flash | 180-250 | 10-55 | 10-15 | 90-95 | 2,000-4,000 |
| Double flash | 180-250 | 15-80 | 12-18 | 90-95 | 2,500-4,500 |
| Binary (organic Rankine cycle) | 100-180 | 1-50 | 8-14 | 90-95 | 2,500-5,000 |
| Combined flash-binary | 150-250 | 20-100 | 12-18 | 85-95 | 3,000-5,500 |

Dry steam plants (Larderello, The Geysers) use steam directly from the reservoir — rare, occurring where the reservoir is naturally vapor-dominated. Flash plants are the most common type for liquid-dominated reservoirs above 180°C. Binary cycle plants use a secondary working fluid (isobutane, isopentane) boiled by geothermal heat — enabling power generation from lower-temperature resources (100-180°C).

### 5.3 Ground-Source Heat Pump Performance

| Parameter | Value |
|-----------|-------|
| COP (heating) | 3.0-5.0 |
| COP (cooling, EER) | 15-25 (equivalent to COP 3.5-6.0) |
| Ground temperature (undisturbed, 10+ m depth) | 10-16°C (varies by latitude) |
| Borehole thermal resistance | 0.05-0.15 K·m/W |
| Required borehole length (heating-dominated) | 10-20 m per kW capacity |
| Required trench length (horizontal loop) | 30-50 m per kW capacity |
| Loop fluid temperature (heating mode) | 0-10°C (entering heat pump) |
| Loop fluid temperature (cooling mode) | 25-35°C (entering heat pump) |
| Borehole lifetime | 50-100+ years |

## 6. Scaling Notes

### Domestic Scale (5-20 kW thermal)

A ground-source heat pump for a single building requires 2-4 boreholes of 100 m depth (or 150-300 m of horizontal trench). Drilling: portable drilling rig or hand-augered holes. Installation: 2-5 days. Requires electricity for the heat pump compressor (1.5-5 kW). Not achievable without electrically powered compressors and HDPE pipe.

### District Heating Scale (1-50 MW thermal)

A geothermal district heating system serves 100-5,000 buildings from a central well field. Requires: 2-10 production wells, 1-5 injection wells, distribution pipe network (5-30 km total length), and peak-load backup boilers. Well depth: 500-2,000 m. Drilling: truck-mounted rotary rig. Build time: 1-3 years.

### Power Generation Scale (10-500 MW electric)

A utility-scale geothermal power plant requires 5-30 production wells, 3-20 injection wells, a steam gathering system (insulated pipelines from wells to plant), a turbine-generator hall, cooling towers, and electrical switchyard. Well depth: 1,000-3,000 m. Drilling: large rotary rig (similar to oil and gas drilling). Exploration and development: 3-7 years. Plant lifetime: 25-40 years.

### Key Scale Breakpoints

- **10 kW**: Single ground-source heat pump for one building. Requires drilling equipment and refrigeration-cycle components.
- **1 MW**: Small binary or flash plant for industrial process heat and electricity. Requires multiple deep wells.
- **20 MW**: Minimum economic scale for flash steam power plant. Requires significant drilling investment and steam gathering infrastructure.
- **100+ MW**: Major geothermal field development. Comparable to a medium-sized coal or gas plant in output.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Declining well production (flow rate dropping) | Reservoir pressure decline from excessive extraction without adequate reinjection | Increase reinjection rate; drill make-up wells at reservoir margins; reduce production rate to match natural recharge |
| Scaling in wells and pipelines (calcite, silica) | Geothermal fluids are at or near mineral saturation; pressure drop causes CO₂ degassing which raises pH, precipitating calcite; cooling below silica saturation deposits amorphous silica | Inject acid (HCl) downhole to dissolve calcite scale; maintain fluid temperature above silica saturation until after heat extraction; install scale inhibitors (phosphate-based); pig pipelines regularly |
| Corrosion of steel casing and piping | Geothermal fluids contain H₂S (sulfidation), CO₂ (sweet corrosion), chlorides (pitting and stress corrosion cracking) | Use corrosion-resistant alloys (13Cr, Super 13Cr, or titanium for worst cases); monitor corrosion coupons; apply cathodic protection to external casing |
| Non-condensable gas (NCG) buildup in condenser | NCG (CO₂, H₂S) accumulates in condenser, reducing vacuum and turbine back-pressure | Size gas extraction system for maximum expected NCG load (1-10% of steam flow); maintain ejectors or vacuum pumps; monitor condenser pressure continuously |
| Thermal breakthrough (reinjection water reaches production well) | Injection well too close to production well, or preferential flow paths in reservoir fractures | Maintain minimum 500-1,000 m separation between injection and production wells; monitor production temperature — drop of >5°C over 5 years indicates breakthrough; redirect injection to more distant wells |
| Ground-source heat pump low COP (<2.5) | Undersized ground loop, or ground loop short-circuiting (hydraulic or thermal), or low ground thermal conductivity | Verify flow rate through ground loop matches design; check borehole grout is intact (no air gaps); add boreholes to increase ground loop capacity; check for groundwater flow that may be thermally short-circuiting the loop |

## 8. Safety

### Hydrogen Sulfide (H₂S)

H₂S is the primary safety hazard at geothermal power plants. It is present in geothermal steam at 50-5,000 ppm. H₂S is immediately dangerous to life and health (IDLH) at 100 ppm. At 300 ppm, it causes pulmonary edema. At 700+ ppm, it causes rapid unconsciousness and death by respiratory paralysis. H₂S deadens the sense of smell at concentrations above 100-150 ppm — victims cannot smell the gas that is killing them.

**Mitigations:**
- Install continuous H₂S monitors around the plant perimeter and in enclosed spaces, set to alarm at 5 ppm (OSHA PEL) and initiate emergency shutdown at 50 ppm.
- All workers carry personal H₂S monitors (electrochemical sensor, audible alarm at 10 ppm).
- Emergency breathing apparatus (self-contained or supplied-air) at all work stations.
- Wind socks visible from all areas for wind direction awareness — evacuate upwind on H₂S release.
- H₂S abatement system (Stretford process, LO-CAT, or biological oxidation) reduces stack emissions to <5 ppm.

### Well Blowout

Geothermal wells penetrate pressurized hot fluid zones. A blowout (uncontrolled flow of hot fluid and steam) during drilling is a severe hazard — the fluid temperature exceeds 200°C and the flow rate can reach hundreds of tonnes/hour. Use blowout preventers (BOPs) rated for geothermal service (high-temperature seals). Maintain well control by monitoring drilling mud weight and circulation. Have a kill procedure (pump heavy mud into the well to overcome formation pressure) ready before drilling into productive zones.

### Scaling and Plugging

Sudden silica or calcite scaling can plug wellbores and surface piping, causing pressure buildup. A plugged well with impaired flow can overpressure upstream equipment. Install pressure relief valves on all vessels and pipelines. Monitor pressure differentials across orifice plates and valves — a rising differential indicates scale buildup. Schedule preventive acid washing or mechanical cleaning before flow is critically restricted.

### Noise

Geothermal steam flashing produces intense noise (100-120 dB at the wellhead). Flash separators and steam vents are extremely loud. Hearing protection mandatory within the wellhead area (plugs + muffs for >100 dB). Enclose noisy equipment where possible. Directional steam vents pointed away from work areas.

## 9. Quality Control

### Well Productivity Testing

After completion, test each well by flowing it at several choke settings (valve positions that restrict flow). Measure: mass flow rate (kg/s), wellhead pressure (bar), enthalpy (kJ/kg, derived from separator conditions), and chemical composition (dissolved solids, non-condensable gases). Plot deliverability curve (flow rate vs. wellhead pressure). Minimum acceptable well: 3-5 MW electrical equivalent. Sub-commercial wells: side-track (deviate drilling to intercept better fractures) or use as injection wells.

### Reservoir Monitoring

- **Pressure**: Downhole pressure gauges (capillary tube or electronic) monitor reservoir pressure continuously. Decline rate should be <2 bar/year for sustainable operation. Faster decline indicates reservoir is being depleted faster than it recharges.
- **Temperature**: Monitor production well temperature. Decline of >1°C/year indicates cold water influx from reinjection or natural recharge.
- **Flow metering**: Orifice plate or Coriolis flow meters on each well. Track cumulative production for reservoir modeling.
- **Chemistry**: Sample geothermal fluid quarterly. Track chloride concentration (increasing chloride indicates cooler dilute water entering the reservoir — sign of cold water intrusion). Track silica concentration (decreasing silica indicates cooling — the fluid is no longer in equilibrium with reservoir rock).

### Ground-Source Heat Loop Testing

After installation, pressure-test the ground loop at 1.5× operating pressure for 30 minutes (no pressure drop acceptable). Measure thermal response by circulating fluid at constant heat injection rate and monitoring temperature evolution — calculate effective ground thermal conductivity from the response curve. Compare to design specification. Thermal conductivity of common ground types: gravel 0.4-0.7 W/m·K, clay 1.0-1.5 W/m·K, saturated sand 2.0-3.0 W/m·K, rock 2.0-5.0 W/m·K.

## 10. Variations and Alternatives

### Comparison of Geothermal Technologies

| Technology | Resource Temp | Output | Efficiency | Complexity | Best For |
|------------|--------------|--------|------------|------------|----------|
| Direct-use heating | 50-150°C | Hot water | 80-90% (heat delivery) | Low | District heating, greenhouses, aquaculture |
| Flash steam | 180-350°C | Electricity | 10-18% | Medium | Liquid-dominated reservoirs |
| Dry steam | 200-300+°C | Electricity | 15-20% | Medium | Vapor-dominated reservoirs (rare) |
| Binary (ORC) | 100-180°C | Electricity | 8-14% | Medium-High | Low-temp resources, co-produced fluids |
| Enhanced Geothermal Systems (EGS) | 150-300°C (engineered) | Electricity/heat | 10-15% | Very High | Locations without natural hydrothermal resources |
| Ground-source heat pump | 10-16°C (ambient) | Heating/cooling | COP 3-5 | Low-Medium | Building HVAC, any location |

### Enhanced Geothermal Systems (EGS)

In locations without natural hydrothermal resources (most of the world), EGS creates an artificial geothermal reservoir by hydraulic stimulation: drill two wells into hot but dry rock (typically granite at 3-5 km depth, 150-300°C), inject water at high pressure (10-30 MPa) to create or widen fractures in the rock, then circulate water between the injection and production wells through the fracture network, extracting heat from the rock. EGS potentially makes geothermal energy available anywhere, but the technology is still maturing — induced seismicity, fracture network control, and thermal depletion are ongoing challenges.

### Geothermal Heat Pump vs Air-Source Heat Pump

Ground-source heat pumps achieve COP 3.0-5.0 year-round because the ground temperature is stable (10-16°C). Air-source heat pumps achieve COP 2.5-4.0 in mild weather but COP drops to 1.5-2.0 in extreme cold (-15°C to -25°C) when heating demand is highest. The ground-source system's higher installed cost (drilling) is offset by lower operating cost over its 20-30 year lifetime.

## 11. References

- **[Steam Power](steam-power.md)** — Steam cycles, boilers, and prime movers
- **[Steam Turbines](steam-turbines.md)** — Turbine-generator sets for geothermal flash and dry steam plants
- **[Electricity Generation](electricity.md)** — Grid connection, transformers, and power distribution
- **[Power Distribution](power-distribution.md)** — Substation and switchyard equipment
- **[Cooling Systems](cooling.md)** — Heat pump refrigeration cycles, cooling towers
- **[Energy Storage](storage.md)** — Grid integration of geothermal baseload
- **[Mining](../mining/index.md)** — Drilling technology and well construction
- **[Iron & Steel](../metals/iron-steel.md)** — Well casing and tubing materials
- **[Chemistry](../chemistry/index.md)** — Working fluids, cement, corrosion inhibitors

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
