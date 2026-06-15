# Evaporator

> **Node ID**: chemistry.evaporator
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: None
> **Enables**: None
> **Timeline**: Years 10-25
> **Outputs**: concentrated_liquid, distilled_water
> **Critical**: No — evaporators concentrate solutions and recover solvents but can be replaced by simpler methods (open-pan evaporation, solar evaporation) at lower efficiency

## Overview

An evaporator concentrates a liquid solution by boiling off the solvent (typically water) as vapor, leaving the dissolved solids behind in a more concentrated liquid. Unlike distillation, which separates components by boiling point differences, evaporation simply removes bulk solvent to reduce volume, increase concentration, or recover purified solvent. The driving force is heat input that supplies the latent heat of vaporization (2,260 kJ/kg for water at 100°C).

Industrial evaporators operate under vacuum to lower the boiling point, reducing thermal degradation of heat-sensitive products and improving energy efficiency (lower temperature = lower heat loss). Multiple-effect arrangements use the vapor from one effect as the heating steam for the next effect at lower pressure, recovering 60-80% of the latent heat. A single-effect evaporator requires approximately 1.1 kg steam per kg water evaporated; a triple-effect requires only 0.4 kg steam per kg evaporated.

The evaporator is one of the most energy-intensive unit operations in the chemical industry. Evaporating 1,000 kg/h of water requires approximately 620-700 kW of heat input for a single-effect unit. At a steam cost of $20/tonne, the annual energy cost for a medium-sized evaporator (10,000 kg/h evaporation) exceeds $150,000. This energy penalty is why multiple-effect and MVR designs are standard for any plant with more than 5,000 hours/year of evaporation duty.

Product quality in evaporation is determined by the maximum temperature the product experiences and the residence time at that temperature. Heat-sensitive products (fruit juices, dairy, pharmaceutical extracts) degrade at temperatures above 60-80°C. For these products, falling-film evaporators operating under high vacuum (boiling point 40-60°C) with short residence time (10-30 seconds) are mandatory. Less sensitive products (salt brines, sugar solutions, inorganic chemicals) can tolerate higher temperatures (100-120°C) and longer residence times.

Four main configurations serve chemical processing: **forced-circulation** (pump circulates liquid through a shell-and-tube heater, best for scaling and fouling fluids), **falling-film** (liquid flows as a thin film down the inside of heated tubes, best for heat-sensitive products), **long-tube vertical** (natural circulation in long tubes, simple and common), and **wiped-film/thin-film** (mechanical wiper spreads liquid into a thin film on a heated surface, for viscous and heat-sensitive materials). The choice depends on product viscosity, heat sensitivity, and fouling tendency.

## Prerequisites

- **[Heat exchanger construction](heat-exchanger.md)**: Shell-and-tube heater is the core of most evaporator designs
- **[Steam supply](../energy/coal.md)**: 0.3-1.0 MPa saturated steam for heating
- **[Vacuum system](../gas-handling/vacuum.md)**: Steam ejector or liquid-ring vacuum pump to maintain 50-200 mmHg
- **[Circulation pump](../water/positive-displacement-pump.md)**: Centrifugal pump rated for boiling liquid service
- **[Stainless steel](../metals/iron-steel.md)**: 316L for corrosive service, carbon steel for non-corrosive

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Steel plate](../metals/iron-steel.md) (vessel) | 200-3,000 kg | 316L SS (corrosive), carbon steel (non-corrosive), 6-12 mm | [Iron & Steel](../metals/iron-steel.md) | Titanium (high-chloride), Hastelloy (acid) |
| [Steel tubing](../metals/forming.md) | 100-1,000 kg | 316L SS tubes, 25-50 mm OD, 2-3 mm wall, 2-6 m long | [Forming](../metals/forming.md) | Copper-nickel (seawater service) |
| [Steel plate](../metals/iron-steel.md) (tubesheets) | 50-300 kg | 316L SS or CS, 25-40 mm thick | [Iron & Steel](../metals/iron-steel.md) | — |
| [Steel pipe](../metals/forming.md) (circulation pump) | 50-200 kg | 316L SS, sized for circulation rate | [Forming](../metals/forming.md) | — |
| [Circulation pump](../water/positive-displacement-pump.md) | 1 unit | Centrifugal, corrosion-resistant, rated for boiling liquid | [Hydraulics](../water/positive-displacement-pump.md) | — (natural circulation for simple types) |
| [Vacuum system](../gas-handling/vacuum.md) | 1 unit | Steam ejector or liquid-ring vacuum pump, to 50-200 mmHg | [Vacuum](../gas-handling/vacuum.md) | Water aspirator (limited vacuum) |
| [Insulation](../construction/building-materials.md) | 20-50 m² | Mineral wool 50-100 mm, aluminum cladding | [Construction](../construction/building-materials.md) | — |
| [Steam supply](../energy/coal.md) | — | 0.3-1.0 MPa saturated steam | [Coal](../energy/coal.md) | Hot oil (higher temperature), electric heating (small scale) |

## Process Description

### Forced-Circulation Evaporator

1. **Fabricate the vapor body**: Construct a vertical cylindrical vessel (0.5-3 m diameter, 2-5 m tall) from 316L stainless steel. This is the vapor-liquid separation space where boiling occurs. The vessel has a tangential feed inlet near the bottom (creates a swirling flow that aids vapor-liquid separation), a vapor outlet at the top, and a concentrated liquid outlet at the bottom. The top may be fitted with a demister pad (wire mesh, 100-150 mm thick) to remove entrained liquid droplets from the vapor.

2. **Construct the heater**: Build a shell-and-tube heat exchanger (per [Heat Exchanger](heat-exchanger.md)): 1-4 m² shell diameter, 2-6 m tube length, 100-1,000 tubes. Process liquid flows through the tubes; steam heats the shell side. Design for the heating duty: Q = m × ΔHvap × evaporation rate, where m is the evaporation rate (kg/h), ΔHvap is the latent heat of vaporization. Steam consumption ≈ 1.1 × evaporation rate for single-effect (includes heating feed to boiling point plus heat losses).

3. **Connect circulation loop**: Pipe the concentrated liquid from the vapor body bottom through the circulation pump, through the heater (tubes), and back to the vapor body feed inlet. The pump circulates liquid at 2-5 m/s tube velocity (high velocity prevents scale deposition and boiling in the tubes — boiling occurs only when the heated liquid enters the lower-pressure vapor body). Circulation rate: 3-10× the feed rate.

4. **Install vacuum system**: Connect the vapor outlet to a condenser (shell-and-tube, water-cooled) and a vacuum source. The condenser captures the evaporated solvent vapor for recovery. Non-condensable gases (air leaking into the system) are removed by the vacuum pump or steam ejector. Operating pressure: 50-200 mmHg absolute (typical), reducing boiling point from 100°C to 40-70°C depending on the product.

  5. **Install feed and product connections**: Feed enters the circulation loop (or directly into the vapor body). Product (concentrated liquid) is withdrawn from the vapor body bottom at a rate that maintains the desired concentration. Install a sight glass on the vapor body for liquid level observation. Install a conductivity meter in the product line — conductivity increases with concentration and provides continuous concentration monitoring.

  **Strengths:**
  - Handles fouling and scaling fluids — high circulation velocity (2-5 m/s) prevents deposit buildup in heater tubes
  - Operates with viscous products (up to 50,000 mPa·s) that would foul falling-film designs
  - Forced circulation prevents boiling in the heater — boiling occurs only in the vapor body, reducing tube fouling
  - Proven design with extensive operating data across chemical, food, and pharmaceutical industries

  **Weaknesses:**
  - Higher energy consumption than falling-film (600-700 kWh/m³ vs. 500-600 kWh/m³ single-effect)
  - Circulation pump adds capital cost, maintenance, and electrical consumption (5-15 kW)
  - Longer residence time (10-60 minutes) than falling-film — not ideal for heat-sensitive products
  - Lower heat transfer coefficient than falling-film (1,500-3,000 vs. 1,500-4,000 W/m²·K)

### Multiple-Effect Arrangement

6. **Arrange effects in series**: Connect the vapor outlet from the first effect (Effect 1) to the heater shell of the second effect (Effect 2). Effect 2 operates at lower pressure than Effect 1, so the vapor from Effect 1 (at temperature T₁) can boil the liquid in Effect 2 (at temperature T₂ < T₁). Effect 2 vapor feeds Effect 3 heater, and so on. Temperature drop between effects: 8-15°C. Total temperature driving force divided by number of effects determines the per-effect temperature difference.

7. **Install inter-effect piping**: Each effect has its own vapor body, heater, and circulation loop. Vapor from Effect N feeds the heater of Effect N+1. Concentrated liquid flows from Effect 1 to Effect 2 to Effect N (forward feed) or vice versa (backward feed, for viscous products). Install transfer pumps between effects if gravity flow is insufficient.

8. **Install final condenser and vacuum**: The vapor from the last effect condenses in a final condenser (water-cooled shell-and-tube). The vacuum system pulls non-condensable gases from the last effect, maintaining the pressure cascade across all effects.

9. **Steam economy calculation**: Single-effect steam economy: 0.85-0.95 kg evaporated per kg steam. Double-effect: 1.6-1.9 kg/kg. Triple-effect: 2.4-2.8 kg/kg. Quadruple-effect: 3.2-3.6 kg/kg. Beyond 5-6 effects, the marginal gain in steam economy does not justify the additional equipment cost. The temperature difference between the first effect steam and the last effect condenser cooling water must be divided across all effects — adding effects reduces the ΔT per effect, requiring more heat transfer area per unit of evaporation.

10. **Forward vs. backward feed**: Forward feed (concentrated liquid flows from Effect 1 → Effect 2 → Effect N) is simpler — gravity flow moves liquid from higher to lower pressure. Backward feed (liquid flows from Effect N → Effect 1) pumps the concentrated (more viscous) product into higher-temperature effects where viscosity is lower — better heat transfer. Backward feed is preferred for viscous products (sugar solutions, CaCl₂ brines). Mixed feed arrangements combine both for optimal energy use.

  11. **Vapor bleed**: In multiple-effect evaporators, vapor can be bled from intermediate effects for preheating the feed or other process heating duties. Vapor bleeding reduces the steam flow to downstream effects but provides useful heat elsewhere in the plant. Optimize the bleed points using pinch analysis to maximize overall plant energy efficiency.

  **Strengths:**
  - Lowest steam consumption of all evaporator configurations (0.18-0.45 kg steam/kg water for 3-6 effects)
  - Each additional effect reduces steam cost by 30-50% — pays back in 1-3 years at high operating hours
  - Forward feed operates with gravity flow between effects — no inter-effect transfer pumps needed
  - Well-suited for large-scale continuous operations (sugar, salt, caustic soda production)

  **Weaknesses:**
  - Higher capital cost than single-effect — each effect adds a complete vapor body, heater, and circulation system
  - Temperature driving force divides across effects — total area increases roughly linearly with effect count
  - More complex control — liquid levels, concentrations, and pressures in all effects must be balanced
  - Backward feed requires inter-effect transfer pumps for the viscous, concentrated product

### Falling-Film Evaporator

10. **Construct the calandria (heating body)**: A single-pass shell-and-tube exchanger, mounted vertically, 3-8 m tube length. Liquid is distributed to the top of each tube and flows down the inside wall as a thin film (0.5-2 mm thick). Steam on the shell side heats the tube wall. The thin film provides excellent heat transfer (1,500-4,000 W/m²·K) with very short residence time (10-30 seconds) — ideal for heat-sensitive products (fruit juices, dairy, pharmaceutical extracts).

11. **Fabricate liquid distributor**: Install a distributor plate at the top of the calandria with precision holes or slots (1-3 mm diameter) feeding each tube. Uniform distribution is critical — a dry tube spot fouls rapidly. Verify distribution by running water through the distributor and observing flow from each tube. Each tube must receive ±10% of the average flow rate.

12. **Install vapor-liquid separator**: The two-phase mixture (concentrated liquid + vapor) exits the bottom of the calandria into a centrifugal separator. Vapor is drawn off to the condenser; concentrated liquid collects at the bottom for product withdrawal or recirculation. The separator must be sized to prevent liquid entrainment in the vapor stream: separator diameter must be large enough that the vapor velocity is below 1-2 m/s at the operating pressure. For a 10,000 kg/h evaporation rate at 100 mmHg, the vapor volume flow rate is approximately 35 m³/s, requiring a separator diameter of 1.5-2.5 m.

  13. **Install recirculation option**: For high concentration ratios (>5×), a single pass through the falling-film calandria may not achieve the target concentration. Install a recirculation loop: pump the concentrated liquid from the separator back to the distributor at the top of the calandria. Mix with fresh feed to maintain the minimum tube wetting rate. Recirculation increases the effective residence time but also increases the thermal exposure of the product.

  **Strengths:**
  - Shortest residence time of all evaporator types (10-30 seconds) — preserves heat-sensitive products (juice, dairy, pharmaceuticals)
  - Highest heat transfer coefficient (1,500-4,000 W/m²·K) — smallest heat transfer area per unit of evaporation
  - Single-pass operation avoids recirculation and thermal degradation of product
  - Achieves 1-3°C approach temperature — maximizes heat recovery potential

  **Weaknesses:**
  - Liquid distribution to every tube is critical — dry spots cause immediate fouling and product degradation
  - Cannot handle viscous products (>500 mPa·s) — film breaks up into rivulets above this viscosity
  - Limited to clean (non-fouling) fluids — any deposit in the thin film (0.5-2 mm) blocks flow
  - Distributor plate holes (1-3 mm) are easily plugged by suspended solids — requires filtered feed

## Calibration and Verification

1. **Heat balance test**: Run the evaporator at design conditions. Measure steam input (flow meter), feed rate, product rate, and vapor rate. Energy balance: steam heat input = feed heating + evaporation + heat losses. The balance should close within ±5%. Larger discrepancy indicates uninsulated surfaces, steam leaks, or instrumentation errors.

2. **Concentration test**: Feed a solution of known initial concentration. Measure product concentration (density meter or refractometer). Verify that the concentration ratio matches the volume reduction ratio: C_product / C_feed ≈ V_feed / V_product.

3. **Vacuum leak test**: Close all process connections. Pull vacuum to the design operating pressure. Close the vacuum valve. Monitor pressure rise for 30 minutes. Acceptable leak rate: <5% of operating pressure per 30 minutes. Higher rates indicate air leaks at flanges, valve packing, or instrument connections.

4. **Heat transfer coefficient verification**: Measure the overall heat transfer coefficient (U) during operation: U = Q / (A × LMTD). For forced-circulation: expected 1,500-3,000 W/m²·K (liquid to boiling liquid). For falling-film: 1,500-4,000 W/m²·K. If U is below 70% of design, suspect fouling on the tube side (scale, polymer deposits). Calculate U daily from operating data and plot the trend — this is the primary indicator of evaporator health.

5. **Vacuum system capacity test**: With the evaporator at design operating pressure, measure the temperature of the cooling water at the condenser inlet and outlet. The temperature rise should be 5-15°C. A smaller temperature rise with high cooling water flow indicates the condenser is oversized. A large temperature rise with inadequate vacuum indicates the condenser is undersized or fouled — the non-condensed vapor overloads the vacuum pump.

## Operating Procedure (Forced-Circulation Evaporator)

1. **Startup — vacuum system**: Start the vacuum pump or steam ejector. Pull the vapor body down to the design operating pressure (50-200 mmHg). Verify the vacuum holds with the feed valve closed (pressure rise <5%/30 min). If excessive leak rate: soap-test all flanges, valve packing, and instrument connections.
2. **Charge and circulate**: Fill the vapor body with feed solution to the operating level (visible in the sight glass, typically 30-50% of vessel height). Start the circulation pump. Verify flow through the heater (check discharge pressure gauge). The circulation rate should be 3-10× the feed rate.
3. **Admit steam**: Open the steam valve to the heater shell side. Start at 30-50% of design steam pressure. The heated liquid enters the vapor body and begins boiling at the reduced pressure. Monitor the vapor body liquid level — boiling causes the level to swell (apparent level rise of 10-30%). Adjust feed rate to maintain the target level.
4. **Establish steady state**: Gradually increase steam pressure to design value. Monitor product concentration (conductivity meter in the discharge line). When the product reaches the target concentration, begin product withdrawal at a rate that matches the evaporation rate: product rate = feed rate − evaporation rate.
5. **Operating adjustments**: If the product is too dilute: reduce feed rate or increase steam pressure. If the product is too concentrated (risk of precipitation or fouling): increase feed rate or reduce steam pressure. Monitor the heat transfer coefficient (calculate U from operating data daily). A declining U indicates fouling.
6. **Shutdown**: Close the steam valve. Stop the feed pump. Allow the system to cool to below 50°C. Release vacuum slowly (open the vacuum relief valve — do NOT let atmospheric air rush in, which could collapse the vessel). Drain the product. Flush the system with water.

## Quantitative Parameters

| Parameter | Single-Effect | Double-Effect | Triple-Effect | Falling-Film |
|-----------|--------------|---------------|---------------|--------------|
| Steam consumption (kg steam / kg water evaporated) | 1.0-1.2 | 0.55-0.65 | 0.35-0.45 | 1.0-1.2 (single) |
| Steam economy (kg evap / kg steam) | 0.85-0.95 | 1.6-1.9 | 2.4-2.8 | 0.85-0.95 |
| Operating temperature | 50-120°C | 50-110°C | 40-110°C | 50-90°C (vacuum) |
| Operating pressure | 50-200 mmHg | 50-200 mmHg (last) to atm (first) | 50-200 mmHg (last) to atm (first) | 30-150 mmHg |
| Evaporation capacity | 100-10,000 kg/h | 500-30,000 kg/h | 500-50,000 kg/h | 500-30,000 kg/h |
| Heat transfer coefficient | 1,500-3,000 W/m²·K | 1,200-2,500 W/m²·K per effect | 1,000-2,500 W/m²·K per effect | 1,500-4,000 W/m²·K |
| Residence time | 10-60 minutes | 20-90 minutes total | 30-120 minutes total | 10-30 seconds |
| Concentration ratio (product/feed) | 2-10× | 2-5× per effect | 2-5× per effect | 2-8× |
| Energy consumption | 600-700 kWh/m³ water evaporated | 300-350 kWh/m³ | 200-250 kWh/m³ | 600-700 kWh/m³ |

## Scaling Notes

- **Single to multiple effects**: Adding effects reduces steam consumption but increases capital cost. The economic breakpoint depends on steam cost and operating hours. At steam costs of $15-25/tonne and >6,000 operating hours/year, triple-effect is justified for most chemical evaporators.
- **Heat transfer area scaling**: Required heat transfer area A = Q / (U × ΔT). For a given evaporation rate, area is inversely proportional to the temperature driving force. Multiple-effect arrangements reduce ΔT per effect, requiring more total area. A triple-effect evaporator needs roughly 3× the heat transfer area of a single-effect for the same throughput.
- **Falling-film capacity limits**: Maximum tube length is limited by liquid distribution — below a minimum flow rate per tube (~0.5 L/min per meter of tube circumference), the film breaks up into rivulets. Scale by adding more tubes, not by lengthening existing tubes.
- **Viscosity limits**: Forced-circulation evaporators handle products up to 50,000 mPa·s. Falling-film types handle up to 500 mPa·s. Above these limits, wiped-film evaporators are required.
- **Heat recovery**: Use the hot condensate from the first-effect heater to preheat the feed. In a triple-effect evaporator, the condensate is at the first-effect steam temperature (100-120°C) and contains significant recoverable heat. A feed preheater using this condensate can reduce the first-effect steam consumption by 10-15%.
- **Boiling point elevation**: Dissolved solids raise the boiling point above that of pure water. For NaOH at 50% concentration: boiling point elevation is approximately 40°C. This means the heater must operate at 140°C to boil the solution at atmospheric pressure. Boiling point elevation reduces the effective temperature driving force and must be accounted for in the heat transfer area calculation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Heat transfer coefficient declining (>20% drop from baseline) | Tube-side fouling (mineral scale: CaCO₃, CaSO₄; organic polymer deposits); steam-side fouling (mud, rust) | Schedule chemical cleaning: acid wash (HCl 5-10%) for mineral scale, alkali wash (NaOH 2-5%) for organic deposits; inspect steam traps; consider anti-scalant dosing in feed |
| Product concentration below target | Insufficient steam supply; vacuum leak raising boiling point; feed rate too high | Increase steam pressure/flow; perform vacuum leak test (pressure rise <5%/30 min); reduce feed rate; verify condenser is removing non-condensables |
| Entrained liquid in overhead vapor (product loss) | Vapor velocity too high in separator; demister pad fouled or missing; liquid level too high in vapor body | Reduce boilup rate; install or clean demister pad (100-150 mm wire mesh); lower liquid level in vapor body; enlarge vapor body diameter |
| Tube plugging | Scale deposits thick enough to restrict flow; solidified product (if below solubility temperature); debris from construction | Increase circulation velocity to >3 m/s; maintain tube-side temperature above product solidification point; flush with hot water or solvent; chemical cleaning |
| Vacuum cannot reach design pressure | Air leaks at flanges or valve packing; vacuum pump or ejector worn; excessive non-condensable load | Soap-test all flanges under vacuum; repack valves; inspect ejector nozzles for erosion; install a second-stage ejector for deeper vacuum |
| Uneven distribution in falling-film (dry tube spots) | Distributor plate holes plugged; insufficient feed rate per tube; distributor plate not level | Clean distributor holes (wire brush or acid soak); verify feed rate meets minimum (≥0.5 L/min per m tube circumference); level the calandria within ±1 mm |
| Product foaming in vapor body | Surfactant impurities in feed; high boiling rate; fine suspended solids stabilizing foam | Add antifoam agent (silicone-based, 5-50 ppm); reduce boilup rate; install or replace demister pad; pre-filter the feed to remove fine solids |
| Product color darkening | Thermal degradation of heat-sensitive components; caramelization of sugars; Maillard reaction (proteins + sugars) | Reduce operating temperature (lower vacuum); switch from forced-circulation to falling-film (shorter residence time); add a nitrogen blanket to prevent oxidation |
| Entrainment of product in condensate | Excessive vapor velocity in separator; demister pad missing or fouled; liquid level too high in vapor body | Reduce boilup rate; install or clean demister pad; lower liquid level; install a centrifugal entrainment separator upstream of the condenser |
| Crystallization in heater tubes (unwanted) | Product concentration exceeding solubility limit in the heater; low feed rate causing excessive concentration in one pass | Maintain product concentration below the saturation point in the heater; increase circulation rate (3-10× feed rate); install online density meter to monitor concentration in real-time; add a flush connection for periodic descaling |

## Safety

- **Vacuum collapse**: The vapor body operates under vacuum. If the vacuum system fails and atmospheric pressure rushes in, the vessel can collapse inward if not designed for full external pressure. Design all vacuum vessels for full vacuum (external pressure collapse). Install vacuum relief valve.
- **Hot surfaces**: Steam-heated surfaces reach 100-180°C. Insulate all steam lines, heaters, and vapor body. Surface temperature <60°C. Emergency shower within 10 m.
- **Boiling liquid hazards**: The process liquid is at its boiling point. Flashing can occur at sample ports and drain valves. Use extended-stem valves to keep operators away from the flash point. Install splash guards on sample valves.
- **Chemical concentration**: As solvent evaporates, dissolved chemicals concentrate. Corrosive solutions become more corrosive; toxic solutions become more toxic. Verify materials of construction are compatible with the final product concentration, not just the feed.
- **Scale and fouling**: Mineral scale (CaCO₃, CaSO₄) deposits on heated tube surfaces reduce heat transfer and can block tubes. Schedule periodic chemical cleaning (acid wash for mineral scale, alkali wash for organic fouling). Monitor heat transfer coefficient — a 20% drop from baseline signals cleaning needed.

## Quality Control

- **Product concentration**: Measure by density meter (±0.1%), refractometer (±0.2%), or titration (±0.5%). Verify concentration meets specification at each sampling interval (typically every 1-2 hours for continuous operation).
- **Product color and clarity**: Visual inspection or spectrophotometric measurement. Discoloration indicates thermal degradation (reduce heating temperature or switch to falling-film). Haze indicates entrainment (check demister pad).
- **Condensate purity**: Measure total dissolved solids (TDS) in the condensed overhead vapor. For water recovery: TDS <10 ppm is acceptable for boiler feedwater. Higher TDS indicates entrainment from the vapor body.
- **Heat transfer coefficient trend**: Calculate U daily from operating data. Plot trend. A decline of >20% from the clean baseline requires investigation and likely cleaning.
- **Product density**: Measure product density with a calibrated hydrometer or inline density meter. Compare to the target density for the desired concentration. Density is the most reliable real-time indicator of product concentration for most inorganic solutions (NaOH, CaCl₂, sugar solutions).
- **Steam consumption tracking**: Measure steam flow to the heater daily. Calculate steam economy (kg water evaporated per kg steam consumed). Compare to the design steam economy. A decline in steam economy indicates increased heat losses (poor insulation, steam leaks) or fouling.
- **Vacuum system performance**: Record the vacuum level and condenser cooling water temperatures daily. A rise in operating pressure (higher boiling point) indicates vacuum system degradation (ejector nozzle wear, vacuum pump seal water temperature rise, air leaks).

## Variations and Alternatives

- **Mechanical vapor recompression (MVR)**: Compresses the overhead vapor to raise its condensation temperature, then uses it as the heating steam. MVR consumes electricity (compressor) instead of steam, achieving steam economy of 10-20× that of single-effect evaporation. Economical where electricity is cheaper than steam. The compressor is the critical component — typically a centrifugal or Roots-type blower.
- **Solar evaporation ponds**: The simplest evaporator — a shallow lined pond exposed to sunlight. Zero energy cost. Very slow (weeks to months). Requires large land area (5-20 m² per m³/year). Used for salt production, brine concentration, and mining leachate management. Not suitable for heat-sensitive, volatile, or valuable products.
- **Open-pan boiling**: Heat a shallow pan of liquid over a fire or steam coil. Simplest evaporator for small-scale operation (syrup production, salt making). No vacuum, no condenser. High energy cost. Product quality limited by high temperature.
- **Wiped-film evaporator**: A mechanical wiper blade spreads the process liquid into a thin film (0.1-1 mm) on the inner wall of a heated cylinder. Handles very viscous products (up to 100,000 mPa·s). Very short residence time (<60 seconds). Used for concentration of heat-sensitive, viscous, or fouling-prone materials. The wiper mechanism adds complexity and maintenance cost.
- **Vacuum pan evaporator**: A jacketed or coiled vessel operating under vacuum with gentle agitation. Used in the sugar industry for final concentration to crystallization point. Slow evaporation rate (limited by jacket area), but handles the high-viscosity massecuite (saturated sugar solution with crystals) that would plug a falling-film evaporator.
- **Submerged combustion evaporator**: Burn natural gas or fuel oil in a burner submerged directly in the solution. Combustion gases bubble through the liquid, providing direct heat transfer. Very high thermal efficiency (90-95%) — no heat exchanger surface to foul. The product is contaminated with combustion products (CO₂ dissolves to form carbonic acid). Used for concentration of waste brines and industrial effluents where product purity is not critical.
- **Thin-film (wiped-film) evaporator**: A rotating wiper blade system inside a vertical heated cylinder spreads the process liquid into a thin film (0.1-1 mm). Handles very viscous and heat-sensitive products. The wiper rotor is driven by a motor at 50-500 RPM. Heat transfer coefficient: 500-1,500 W/m²·K. Throughput limited to 50-2,000 kg/h per unit. Used for concentrating fruit juices, polymer solutions, and pharmaceutical extracts.

## References

- [Heat Exchanger](heat-exchanger.md) — the heater component of an evaporator
- [Crystallizer](crystallizer.md) — evaporation to supersaturation for crystal formation
- [Distillation Column](distillation-column.md) — separation by boiling point (not concentration)
- [Water Treatment](water-treatment.md) — brine concentration for zero liquid discharge
- [Distillation](distillation.md) — multiple-effect distillation and MVR principles
- [Chemical Recovery](chemical-recovery.md) — solvent recovery by evaporation
- [Alkalis](alkalis.md) — NaOH concentration by evaporation in chlor-alkali process
- [Food Processing](../food-processing/preservation.md) — juice and dairy concentration

## Evaporator Sizing Example

A triple-effect forced-circulation evaporator concentrating NaOH from 10% to 50% at a feed rate of 5,000 kg/h:

- **Feed rate**: 5,000 kg/h at 10% NaOH = 500 kg/h NaOH + 4,500 kg/h water
- **Product rate**: 500 / 0.50 = 1,000 kg/h at 50% NaOH
- **Evaporation rate**: 5,000 − 1,000 = 4,000 kg/h water evaporated
- **Steam consumption** (triple-effect, 0.40 kg/kg): 4,000 × 0.40 = 1,600 kg/h steam
- **Heat transfer area** (per effect, U = 1,500 W/m²·K, ΔT per effect ≈ 25°C): A = Q / (U × ΔT) ≈ 60 m² per effect × 3 effects = 180 m² total
- **Vacuum system**: Last effect at 100 mmHg (boiling point ≈ 52°C). Two-stage steam ejector or liquid-ring vacuum pump
- **Circulation pump**: 15,000 kg/h per effect (3× feed rate), 316L SS, rated for 100°C
- **Total power**: 45 kW (pumps) + 10 kW (vacuum) = 55 kW electrical + 1,600 kg/h steam
- **Condenser**: Water-cooled shell-and-tube, 50 m² area, 30,000 kg/h cooling water (25°C inlet, 35°C outlet)
- **Materials of construction**: 316L SS for all wetted parts (NaOH is corrosive to carbon steel at elevated temperature). Shell: carbon steel with 316L clad or solid 316L for the first effect (highest temperature). Last effect: 316L solid (lower temperature but highest NaOH concentration).

## Energy Efficiency Comparison

| Evaporator Type | Steam (kg/kg water) | Electrical (kWh/m³ water) | Complexity | Best Application |
|----------------|---------------------|---------------------------|------------|------------------|
| Single-effect | 1.0-1.2 | 5-10 | Low | Small scale, batch |
| Double-effect | 0.55-0.65 | 8-15 | Medium | Medium scale |
| Triple-effect | 0.35-0.45 | 10-20 | Medium | Large scale, NaOH |
| Six-effect | 0.18-0.25 | 12-25 | High | Sugar, very large scale |
| MVR (mechanical vapor recompression) | 0.02-0.05 (steam) + 30-50 (electric) | 30-50 | High | Milk, wastewater |
| TVR (thermal vapor recompression) | 0.35-0.50 | 5-10 | Medium | Retrofit existing single-effect |

## Startup and Shutdown Procedure

- **Cold startup**: Fill all effects with feed solution to operating level. Start the vacuum system on the last effect. Admit steam to the first effect calandria at 20% of design flow. Watch for boiling — it may be delayed if the solution is subcooled. Once boiling starts in the first effect, vapor flows to the second effect calandria and gradually brings it to temperature. Allow 30-60 minutes for all effects to reach steady state. Gradually increase steam flow to design rate while adjusting feed rate to maintain liquid levels.
- **Hot startup** (after brief shutdown): If the solution is still near boiling temperature, the startup is faster — typically 15-20 minutes. Admit steam and feed simultaneously, increasing both proportionally. Watch for foaming caused by residual surfactants or dissolved gases coming out of solution.
- **Normal shutdown**: Stop feed flow. Continue steam at 50% rate to concentrate remaining liquid to the target concentration. When product concentration is reached, stop steam. Break vacuum slowly with air (not nitrogen — nitrogen is expensive and unnecessary here). Drain all effects. Flush with water to prevent product solidification in the calandria tubes.
- **Emergency shutdown**: Trip the steam supply immediately. Close all vapor valves between effects to prevent pressure equalization (which can cause backflow and contamination). Break vacuum with air and drain. An uncontrolled vacuum loss while the solution is hot causes violent flashing (boiling) — keep vacuum on until temperature drops below 60°C.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
