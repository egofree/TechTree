# Refrigeration

> **Node ID**: food-processing.refrigeration
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `chemistry`, `energy`, `metals`
> **Enables**: None
> **Critical**: No — refrigeration extends shelf life but canning and drying provide preservation without ongoing energy input
> **Timeline**: Years 20-30
> **Outputs**: refrigerated_food

## Overview

Refrigeration is mechanical cooling that slows microbial growth, chemical degradation, and enzymatic activity. It extends fresh food shelf life by 5-20× but requires continuous energy input — a fundamental limitation that distinguishes it from all other preservation methods. A refrigerator holds food at 0-4°C, where most bacteria double every 12-24 hours instead of every 20 minutes at 37°C. A freezer at -18°C halts microbial growth entirely, preserving food for 6-12 months with minimal quality loss.

The dominant technology is the vapor-compression refrigeration cycle: a refrigerant absorbs heat by evaporating in the cold space (evaporator, -10 to 4°C), then releases that heat by condensing in the warm space (condenser, 30-50°C). An electric or mechanical compressor drives the cycle. The coefficient of performance (COP) — ratio of cooling delivered to work input — ranges from 2 to 5 for typical food refrigeration systems.

Refrigeration depends on [energy](../energy/index.md) for mechanical compressors, [chemistry](../chemistry/index.md) for refrigerants, and [metals](../metals/index.md) for pipes, vessels, and heat exchangers. It appears in the bootstrap chain after electrical generation and metal fabrication are established (Years 20-30). Before mechanical refrigeration, ice harvested from frozen lakes and stored in insulated ice houses provided cold storage without any energy input — 50-70% of winter-harvested ice survived the summer in a well-built ice house.

For other preservation methods, see [Traditional Preservation](traditional-preservation.md), [Canning & Thermal Sterilization](canning.md), [Food Fermentation](fermentation.md), and [Pasteurization](pasteurization.md). Pasteurized products in particular require refrigeration to achieve their 5-7 day shelf life.

## Prerequisites

### Materials

- **Refrigerant**: ammonia (R717), R134a, or R404a — from [chemistry](../chemistry/index.md). Ammonia is the industrial standard for large systems; R134a and R404a for smaller commercial units.
- **Steel and copper tubing**: for refrigerant lines, evaporator, and condenser coils — from [metals](../metals/index.md). Copper preferred for its thermal conductivity (400 W/m·K).
- **Insulation**: cork, fiberglass, or foamed polymer — 10-20 cm thickness for cold-room walls. R-value target: R-20 to R-40.
- **Thermal storage medium** (ice bank systems): water, frozen to ice as a cold reservoir for load-smoothing.

### Equipment

- [Electric motor](../energy/electric-motor.md) or mechanical power source — drives the compressor, 0.5-1000 kW depending on scale
- Compressor — reciprocating (small), screw (large), or centrifugal (very large industrial)
- Evaporator coil — located inside the cold space; absorbs heat as refrigerant evaporates
- Condenser coil — located outside; rejects heat as refrigerant condenses
- Expansion valve — throttles high-pressure liquid refrigerant to low-pressure cold vapor
- Thermostat and temperature logging — calibrated to ±1°C

### Knowledge

- Thermodynamics of the vapor-compression cycle: evaporation absorbs heat (cold side), condensation releases heat (hot side). The compressor raises refrigerant pressure and temperature so heat can flow from cold to hot.
- Coefficient of Performance (COP) = cooling delivered (kW) ÷ work input (kW). Typical COP 2-5 for food refrigeration. Higher COP = more efficient.
- Cold chain integrity: a single temperature break can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential.

### Infrastructure

- Continuous electrical power — 0.5-2.0 kW per m³ of cold storage; 200-500 kWh/day for a 100 m³ freezer. Intermittent power requires ice-bank thermal storage.
- Backup power generator — cold chain failure destroys entire inventory. Diesel or steam backup required for industrial operations.
- Ventilation for ammonia refrigerant safety — ammonia leak detection alarms, forced-air exhaust

## Bill of Materials

Materials and capacities for three scales of refrigeration operation.

| Component | Domestic (0.1-0.5 kW) | Commercial (5-20 kW) | Industrial (50-1000 kW) |
|-----------|:----------------------:|:--------------------:|:-----------------------:|
| Refrigerant charge | 0.1-0.5 kg R134a | 5-20 kg R404a or R717 | 50-500 kg R717 (ammonia) |
| Compressor type | Hermetic reciprocating | Semi-hermetic reciprocating | Screw or centrifugal |
| Copper tubing | 3-5 m, 6-10 mm dia | 20-50 m, 12-20 mm dia | 100+ m, 20-50 mm dia steel |
| Insulation | 5 cm foamed polymer | 10 cm fiberglass or PIR | 15-20 cm PIR or mineral wool |
| Cold space volume | 0.1-0.5 m³ | 10-50 m³ | 100-1,000+ m³ |
| Electrical power | 0.1-0.5 kW (200-500 kWh/yr) | 5-20 kW (15-50 MWh/yr) | 50-500 kW (200-2000 MWh/yr) |
| Evaporator area | 0.5-2 m² finned coil | 5-20 m² finned coil | 50-200 m² multiple coils |
| Source | [Metals](../metals/index.md), [Polymers](../polymers/index.md) | [Metals](../metals/index.md), [Energy](../energy/index.md) | [Metals](../metals/index.md), [Energy](../energy/index.md) |

## Process Description

### Vapor-Compression Cycle

The refrigeration cycle moves heat from a cold space to a warm space by evaporating and condensing a refrigerant at controlled pressures.

1. **Compression**: The compressor draws low-pressure refrigerant vapor from the evaporator (typically -10 to 4°C, 1-3 bar) and compresses it to high pressure (10-25 bar). Compression raises both pressure and temperature — the vapor exits the compressor at 60-90°C.
2. **Condensation**: The hot high-pressure vapor flows through the condenser coil (located outside the cold space, 30-50°C ambient). It rejects heat to the surroundings and condenses to a high-pressure liquid. Air-cooled condensers use fans; water-cooled condensers use cooling water.
3. **Expansion**: The high-pressure liquid passes through an expansion valve (throttle), which drops its pressure to 1-3 bar. The pressure drop causes flash evaporation, cooling the refrigerant to -10 to 4°C.
4. **Evaporation**: The cold low-pressure liquid-vapor mixture enters the evaporator coil inside the cold space. It absorbs heat from the food and cold room air, fully evaporating back to vapor. The cycle repeats.
5. **Temperature control**: A thermostat monitors the cold-space temperature. When the setpoint (0-4°C for refrigeration, -18°C for freezing) is reached, the compressor cycles off. When temperature rises 1-2°C above setpoint, it cycles on.

### Pre-Mechanical Ice Harvesting (no energy input)

For civilizations without electricity, ice harvesting provides cold storage:

1. Cut ice blocks (50-100 kg each) from frozen lakes when ice reaches 15-30 cm thickness (mid-winter).
2. Transport blocks to an underground or heavily insulated ice house. Pack tightly with sawdust between layers as insulation.
3. A well-built ice house retains 50-70% of its ice through summer. Drain meltwater away — standing water accelerates melting.
4. Place food in a separate insulated chamber adjacent to (not touching) the ice. Cold air from the ice sinks into the food chamber.

### Cold Chain Management

1. Maintain product temperature from production through processing, transport, storage, and retail. Document temperature at each stage.
2. A single break in the cold chain allows bacterial growth that cooking may not fully eliminate. Frozen food that thaws must be treated as refrigerated food — it does not regain its original shelf life if refrozen.
3. Use recording thermometers (chart recorders or digital data loggers) in all cold storage. Calibrate to ±1°C.

## Quantitative Parameters

### Microbial Growth Rates by Temperature

| Food | Room Temp (25°C) | Refrigerated (4°C) | Frozen (-18°C) |
|------|:-----------------:|:------------------:|:--------------:|
| Raw meat | 4-8 hours | 3-5 days | 6-12 months |
| Raw fish | 4-6 hours | 1-2 days | 3-6 months |
| Fresh milk | 4-6 hours | 5-7 days | 3 months |
| Cooked rice | 6-8 hours | 4-6 days | 6 months |
| Cut fruit | 2-4 hours | 3-5 days | 6-12 months |
| Fresh vegetables | 1-2 days | 5-7 days | 8-12 months |
| Bread | 3-5 days (mold) | 7-10 days | 3-6 months |

### Refrigerant Comparison

| Refrigerant | Boiling Point (1 atm) | ODP | GWP | Toxicity | Typical Use |
|-------------|:---------------------:|:---:|:---:|:--------:|:-----------:|
| Ammonia (R717) | -33°C | 0 | 0 | High (300 ppm IDLH) | Industrial (10-1000 kW) |
| R134a | -26°C | 0 | 1430 | Low | Domestic/commercial |
| R404a (blend) | -47°C | 0 | 3922 | Low | Commercial freezers |
| R22 (historical) | -41°C | 0.05 | 1810 | Low | Phased out (ozone-depleting) |

ODP = Ozone Depletion Potential; GWP = Global Warming Potential (CO₂ = 1).

### Operating Parameters

| Parameter | Domestic Fridge | Commercial Cold Room | Industrial Freezer |
|-----------|:---------------:|:--------------------:|:------------------:|
| Evaporator temperature | -10 to 4°C | -10 to 2°C | -35 to -20°C |
| Condenser temperature | 30-50°C | 30-50°C | 30-50°C |
| COP (coefficient of performance) | 2.0-3.5 | 3.0-4.5 | 2.5-4.0 |
| Power consumption | 0.1-0.5 kW | 5-20 kW | 50-500 kW |
| Daily energy | 1-5 kWh/day | 50-200 kWh/day | 500-5000 kWh/day |
| Air change rate | Sealed | 2-4/hr (door openings) | 1-2/hr |

## Scaling Notes

- **Ice house** (pre-mechanical, 50-200 people): Harvest ice from frozen lakes in winter. Store in insulated underground chamber with sawdust. 50-70% of stored ice survives summer. Provides cold storage for community without any energy input. Minimum economic scale: 50 tonnes ice for useful cold storage through summer.
- **Mechanical cold room** (community, 500-2,000 people): 10-50 m³ cold room at 0-4°C. Ammonia absorption or small compressor. Requires 5-20 kW electrical or mechanical power. Cold storage for perishables: meat, dairy, produce.
- **Industrial cold storage** (10,000+ people): 100-1,000+ m³ cold rooms and freezers. Vapor-compression system with ammonia refrigerant. A 100 m³ cold room at -18°C requires 50-100 kW cooling capacity and 200-500 kWh/day electrical energy.
- **Cold chain scaling**: A single refrigerated truck requires 10-30 kW refrigeration capacity. Rail refrigerated cars: 15-40 kW. Cold chain logistics multiply energy requirements by distribution distance.
- **Non-linear scaling**: Compressor capacity scales with swept volume (cubic), but heat exchanger area scales with surface (square). At large scales, heat exchanger surface area becomes the bottleneck — multiple evaporator coils are required rather than a single large unit.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Freezer burn (dry, discolored patches on frozen food) | Poor packaging, temperature fluctuation, extended storage | Wrap tightly in moisture-proof material. Maintain -18°C continuously. Use within recommended time |
| Compressor runs continuously (high energy bills) | Door seal leak, ice buildup on evaporator, low refrigerant charge, condenser fouled | Replace door gaskets. Defrost evaporator. Check refrigerant pressure. Clean condenser coils |
| Temperature rises above setpoint | Compressor malfunction, refrigerant leak, power failure, condenser blocked | Maintain backup power generator. Inspect refrigerant lines for leaks. Install temperature alarms with battery backup |
| Slow freezing (mushy texture on thaw) | Overloaded freezer, insufficient airflow, blast freezer capacity exceeded | Freeze in smaller batches. Ensure airflow around products. Use blast freezer (-30 to -40°C) for quality-sensitive products |
| Ice buildup on evaporator coil | Defrost heater failure, frequent door openings, high humidity ingress | Activate defrost cycle. Minimize door opening time. Check door seals |
| Ammonia leak (acrid smell, eye irritation) | corroded pipe, failed gasket, overpressure rupture | Evacuate area. Isolate ammonia supply. Ventilate with forced air. Do NOT enter without SCBA above 300 ppm |

## Safety

- **Ammonia refrigerant**: Toxic at 300 ppm (IDLH), lethal at 5,000 ppm. Ammonia is a strong respiratory irritant — destroys lung tissue on contact with moist mucous membranes. Install ammonia leak detection alarms and forced ventilation in all machinery rooms. SCBA (self-contained breathing apparatus) required for entry above 300 ppm.
- **Cold chain integrity**: A single break in the cold chain can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential. Thawed frozen food must be used within the same timeframe as refrigerated food — refreezing does not restore safety.
- **Pressure vessel safety**: Refrigeration compressors and condensers operate at 10-25 bar. Follow pressure vessel safety protocols — regular inspection, pressure relief valves, lockout/tagout during maintenance.
- **Electrical hazards**: Industrial refrigeration uses 3-phase power at hundreds of kW. Arc flash hazard is severe. All maintenance requires lockout/tagout and electrical isolation.
- **Refrigerant displacement (non-ammonia)**: Freon-type refrigerants (R134a, R404a) are less acutely toxic than ammonia but are heavier than air. In confined spaces they displace oxygen, causing asphyxiation without warning. Ventilate all machinery rooms.

### Personal Protective Equipment

- Thermal-insulated gloves when handling frozen food or entering freezers (frostbite risk at -18°C within 30 minutes of unprotected skin exposure)
- SCBA and gas-tight chemical suit for ammonia leak response
- Arc-rated electrical PPE for industrial compressor maintenance

## Quality Control

### Acceptance Criteria

- **Cold room temperature**: 0-4°C for refrigerated storage, -18°C or below for frozen storage. Tolerance: ±1°C from setpoint. Alarm at +2°C deviation.
- **Air temperature distribution**: Maximum variation across cold room ≤2°C. Hot spots indicate poor airflow or insufficient evaporator coverage.
- **Product core temperature**: Frozen food must reach -18°C at core within 24 hours of loading. Monitor with probe thermometer inserted into product center.

### Testing Methods

- Calibrated thermometer — mercury or digital, ±0.5°C accuracy. Calibrate against ice-water bath (0.0°C reference).
- Recording thermometer / data logger — continuous temperature record. Required for all commercial cold storage. Download and review weekly.
- Infrared surface thermometer — non-contact, for rapid checks of product surface and cold room wall temperatures.
- Refrigerant pressure gauges — high-side (condenser) and low-side (evaporator) pressure. Compare to manufacturer charts to diagnose charge level and compressor health.

### Sampling Procedure

- Monitor cold room air temperature continuously (data logger at the warmest point in the room, typically near the door or ceiling).
- Check product core temperature on each batch entering cold storage.
- Review temperature logs daily for excursions. Any break >2 hours above 4°C requires quality assessment of affected product.

## Variations and Alternatives

- **Vapor-compression cycle** (modern standard): Electric compressor drives refrigerant cycle. COP 2-5. Dominant technology for all scales from domestic to industrial. Requires electricity or mechanical power.
- **Absorption refrigeration cycle**: Uses heat (steam, gas flame, solar thermal) instead of mechanical compression to drive the cycle. Ammonia-water or lithium bromide-water pair. COP 0.5-0.8 (lower than vapor-compression). Valuable where waste heat is available but electricity is not.
- **Ice harvesting** (pre-mechanical): Cut ice from frozen lakes in winter, store in insulated ice house. Zero energy input for the cold storage itself (only labor for harvesting). 50-70% of ice survives summer. Limited to cold-winter climates.
- **Evaporative cooling**: Water evaporates through porous clay vessel, cooling contents by 5-10°C below ambient. Works in dry climates. No energy input. Limited to above-refrigeration temperatures (10-15°C in dry climate).

### Refrigerant Selection Trade-offs

| Refrigerant | Energy Efficiency | Environmental Impact | Toxicity | Cost | Best For |
|-------------|:-----------------:|:-------------------:|:--------:|:----:|:--------:|
| Ammonia (R717) | Highest (COP 4-5) | Zero ODP, zero GWP | High | Low | Large industrial |
| R134a | Good (COP 3-4) | Zero ODP, high GWP | Low | Medium | Domestic/commercial |
| R404a | Moderate (COP 2.5-3.5) | Zero ODP, very high GWP | Low | Medium | Commercial freezers |

Ammonia is the clear choice for industrial-scale food refrigeration: highest efficiency, zero environmental impact, and lowest cost per kg. The toxicity risk is managed by confining refrigerant to machinery rooms with leak detection. For smaller operations where ammonia safety infrastructure is impractical, R134a or R404a are acceptable despite their global-warming impact.

## References

- [Food Preservation](preservation.md) — overview hub for all preservation methods
- [Pasteurization](pasteurization.md) — pasteurized products require refrigeration to achieve shelf life
- [Canning & Thermal Sterilization](canning.md) — shelf-stable preservation without refrigeration
- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking (no energy input)
- [Energy](../energy/index.md) — electrical power for compressors
- [Chemistry](../chemistry/index.md) — refrigerant chemistry (ammonia synthesis, halocarbon production)
- [Metals](../metals/index.md) — steel and copper tubing, pressure vessels
- [Electric Motors](../energy/electric-motor.md) — compressor drive
- [Dairy Processing](dairy.md) — cold storage for milk and dairy products

---

*Part of the [Bootciv Tech Tree](../index.md) • [Food Processing](./index.md) • [All Domains](../index.md)*
