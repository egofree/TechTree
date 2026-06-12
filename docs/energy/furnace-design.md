# Furnace Design Principles

> **Node ID**: energy.furnace-design
> **Domain**: [Energy](./index.md)
> **Enables**: [`metals.blacksmithing`](../metals/blacksmithing.md)
> **Timeline**: Years 5-20
> **Outputs**: furnace_design, thermal_calculations, refractory_selection
> **Critical**: No — enables optimization of all furnace types but does not block initial construction

This article covers general furnace design principles — heat transfer, refractory selection, combustion, and efficiency — applicable to all furnace types. For specific furnaces, see [Blast Furnace](../metals/blast-furnace.md), [Electric Furnaces](./electric-furnaces.md), and [Kilns](../ceramics/kilns.md).

A furnace is any enclosed structure designed to contain and control high-temperature heat for processing materials. The fundamental design challenge is the same whether the furnace melts iron at 1500°C, fires pottery at 1200°C, or reduces silicon at 2000°C: deliver heat to the charge efficiently, contain it within the working zone, and protect the structure from self-destruction. Every furnace design balances four competing demands: **temperature** (hot enough for the process), **efficiency** (fuel energy converted to useful process heat), **durability** (lining and structure survive repeated heating), and **control** (temperature, atmosphere, and heating rate are predictable and repeatable).

## Heat Transfer Fundamentals

All heat transfer in a furnace occurs by three mechanisms: **conduction** through solids, **convection** via moving gases, and **radiation** from hot surfaces. The relative importance of each mechanism shifts dramatically with temperature.

**Conduction**: Heat flows through the furnace walls, refractory lining, and charge material. Fourier's law gives the steady-state heat flux through a flat wall:

    q = k × (T_hot − T_cold) / thickness

where q is heat flux (W/m²), k is thermal conductivity (W/(m·K)), T is temperature on each face (°C or K), and thickness is wall thickness (m). For a composite wall (e.g., dense firebrick + insulating brick + steel shell), calculate thermal resistance of each layer and sum them: q = ΔT / (R₁ + R₂ + R₃), where R = thickness / k for each layer.

Conduction dominates wall heat losses and determines how thick the refractory lining must be. A fireclay brick (k ≈ 1.2 W/(m·K)) at 230 mm thickness with 1200°C inside and 50°C outside conducts approximately 6.0 kW/m² — a significant continuous loss. Adding 115 mm of insulating firebrick (k ≈ 0.25 W/(m·K)) reduces this to roughly 2.5 kW/m².

**Convection**: Hot gases circulating inside the furnace transfer heat to the charge and walls. Newton's law of cooling:

    q_conv = h × (T_gas − T_surface)

where h is the convective heat transfer coefficient (W/(m²·K)). Typical values: natural convection in air 5-25 W/(m²·K), forced convection in furnaces 25-250 W/(m²·K). Convection dominates below approximately 600°C. In a wood-fired updraft kiln at 800°C, convection delivers roughly 30-40% of the heat to the ware; the rest is radiation.

**Radiation**: Electromagnetic emission from hot surfaces. Stefan-Boltzmann law:

    q_rad = ε × σ × (T₁⁴ − T₂⁴)

where ε is emissivity (0-1, most refractories 0.8-0.9), σ is the Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/(m²·K⁴)), and temperatures are in Kelvin. Radiation dominates above 600°C because of the T⁴ dependence. At 1200°C (1473 K) inside a furnace with 300°C (573 K) walls, radiation accounts for approximately 85-90% of total heat transfer to the charge. This is why furnace geometry that maximizes the view factor between the hot flame/refractory crown and the charge is so important at high temperatures.

**Practical implication**: Below 600°C, improving gas flow patterns (convection) is the main lever for uniform heating. Above 600°C, controlling surface emissivity and view factors (radiation) matters more. A furnace designed for 500°C annealing has fundamentally different geometry requirements than one designed for 1300°C smelting.

## Combustion Fundamentals

Combustion is the rapid oxidation of fuel releasing heat. For furnace design, the critical parameters are **stoichiometric air requirement**, **excess air**, and **adiabatic flame temperature**.

**Stoichiometry**: Complete combustion of carbon (the primary constituent of most solid fuels):

    C + O₂ → CO₂ + 393.5 kJ/mol

For a fuel with known composition, the stoichiometric (theoretical minimum) air requirement is calculated from the oxygen needed to fully oxidize all carbon, hydrogen, and sulfur. For bituminous coal (≈80% C, 5% H, 10% O by mass), stoichiometric air is approximately 8-9 kg air per kg fuel. By volume at standard conditions, this is roughly 6.5-7.5 m³ air per kg coal.

**Excess air**: Real furnaces always operate with excess air to ensure complete combustion and avoid unburned fuel (CO and soot). Typical excess air ratios:

| Furnace Type | Excess Air | O₂ in Flue Gas |
|---|---|---|
| Natural draft kiln | 100-200% | 10-14% |
| Forced draft with manual control | 50-100% | 7-10% |
| Forced draft with automatic control | 20-40% | 4-6% |
| Gas burner with automatic ratio control | 5-15% | 1-3% |

Too much excess air wastes fuel — every kilogram of excess air heated from ambient to flue gas temperature carries energy out the chimney. Too little excess air produces CO (incomplete combustion), wasting 70% of the fuel's energy per kilogram of carbon that burns to CO instead of CO₂.

**Adiabatic flame temperature**: The theoretical maximum flame temperature assuming no heat loss to surroundings:

    T_flame = (fuel energy + enthalpy of incoming air) / (mass_flow × specific_heat of products)

For natural gas with 15% excess air, adiabatic flame temperature is approximately 1950°C. Real flame temperatures are lower (1500-1800°C for gas, 1600-1900°C for pulverized coal) due to heat losses to the furnace walls and charge. The flame temperature sets the upper limit of what the furnace can achieve — the process temperature must always be below the flame temperature by a margin that drives heat transfer.

**Draft**: Combustion requires a continuous supply of air and removal of flue gases. Draft pressure (the pressure difference driving gas flow) is generated by: chimney height (natural draft), fans (forced draft), or both. Natural draft pressure from a chimney:

    ΔP ≈ 0.0342 × H × P_atm × (1/T_ambient − 1/T_flue_gas)

where H is chimney height (m), P_atm is atmospheric pressure (atm), and temperatures are in Kelvin. A 10 m chimney with flue gas at 800°C (1073 K) in 20°C (293 K) ambient produces roughly 9 Pa of draft — enough for a small batch kiln but inadequate for industrial furnaces requiring 50-200 Pa.

## Refractory Selection

Refractories are heat-resistant materials that line the furnace interior, protecting the structure from temperatures that would melt or weaken steel. Selecting the right refractory is the single most important material decision in furnace design.

**Key refractory properties**:

- **Refractoriness**: Maximum service temperature before softening. Must exceed the intended operating temperature by at least 100-200°C.
- **Thermal conductivity**: Determines heat loss through walls. Lower is better for insulation, higher is better for thermal shock resistance.
- **Thermal shock resistance**: Ability to withstand rapid temperature changes without cracking. Related to thermal conductivity, thermal expansion coefficient, and strength.
- **Slag resistance**: Chemical compatibility with the molten materials (slag, metal, glass) the refractory contacts. Basic slags (CaO-rich) attack acidic refractories (SiO₂), and vice versa.
- **Cold crushing strength**: Mechanical strength at room temperature — matters for structural loading during construction.

**Refractory materials by maximum service temperature**:

| Material | Composition | Max Service Temp | Thermal Conductivity | Best Application |
|---|---|---|---|---|
| Common fireclay | Al₂O₃ 25-45%, SiO₂ balance | 1200-1400°C | 1.0-1.5 W/(m·K) | General-purpose kiln and furnace lining |
| High-duty fireclay | Al₂O₃ 45-60% | 1400-1500°C | 1.2-1.8 W/(m·K) | Hot-face zones, iron smelting |
| Silica brick | >95% SiO₂ | 1650-1700°C | 1.0-1.5 W/(m·K) | Glass tank crowns, coke ovens (acidic) |
| High-alumina brick | Al₂O₃ 60-90% | 1600-1800°C | 1.5-2.5 W/(m·K) | High-temp zones, iron/steel furnaces |
| Magnesite (MgO) | >90% MgO | 1800-2000°C | 3.0-5.0 W/(m·K) | Basic steelmaking (EAF, BOF) |
| Dolomite | CaO·MgO | 1700-1900°C | 2.0-4.0 W/(m·K) | Basic steelmaking (cheaper than MgO) |
| Carbon / graphite | >95% C | 2500-3000°C (inert) | 15-40 W/(m·K) | Reducing environments (SAF, blast furnace hearth) |
| Zirconia (ZrO₂) | >90% ZrO₂ | 2000-2200°C | 2.0-3.0 W/(m·K) | Glass contact, extreme temperature |
| Insulating firebrick | Various (low density) | 1200-1400°C | 0.15-0.4 W/(m·K) | Backup insulation layer |
| Ceramic fiber blanket | Al₂O₃-SiO₂ fibers | 1200-1600°C | 0.05-0.15 W/(m·K) | Wrap insulation, seals, expansion joints |

**Acid-base matching rule**: The refractory must be chemically compatible with the slag or melt it contacts. Basic slags (high CaO, from limestone flux in steelmaking) dissolve acidic refractories (SiO₂). Acidic slags (high SiO₂, from silica-rich ores) dissolve basic refractories (MgO, CaO). Neutral refractories (Al₂O₃, carbon) resist both to varying degrees. Mismatching refractory and slag chemistry is the most common cause of premature lining failure.

## Furnace Geometry and Heat Distribution

The internal shape of the furnace determines how heat is distributed to the charge. Good geometry minimizes cold spots, avoids flame impingement on the charge (which causes localized overheating), and ensures uniform temperature across the working zone.

**Hearth area vs height**: The ratio of hearth (floor) area to chamber height determines whether the furnace is a **shallow bath** (large area, low height — good for melting, like an open hearth furnace) or a **shaft** (small area, tall — good for counterflow processing, like a blast furnace). Heat transfer to a shallow melt pool is dominated by radiation from the roof and flame. Heat transfer in a shaft furnace is dominated by convection as hot gases rise through the burden.

**Crown shape**: The roof of a furnace is typically arched (domed) rather than flat. An arch is structurally stable under compression from the thermal expansion of the brickwork and transfers thrust to the sidewalls. The arch also focuses radiation downward onto the hearth, improving heat transfer to the charge. A catenary arch (the shape a chain forms when hanging) is close to ideal — each brick is in pure compression with no bending. The arch rise (height of the crown above the spring line) is typically 15-25% of the span.

**Baffles and bag walls**: In downdraft kilns and many furnaces, baffles (called "bag walls" in kiln terminology) direct hot gases along a controlled path through the working zone before they reach the flue. Without baffles, hot gases take the shortest path from the firebox to the chimney, creating a hot channel with cold zones on either side. Bag walls should be tall enough to force gases over the top of the charge but leave a gap at the bottom for flow.

**Burner placement**: For furnaces with multiple burners (gas- or oil-fired), burner placement controls the heat distribution pattern:
- **Side firing**: Burners along both walls firing toward the center. Uniform heating across the width. Standard for most rectangular furnaces.
- **End firing**: Burners at one end firing down the length. Simpler construction but creates a temperature gradient along the furnace length. Used for tunnel kilns where the gradient is intentional.
- **Roof firing**: Flat-flame burners mounted in the roof, firing downward. Excellent radiation heating of the hearth but complex roof construction. Used in steel reheating furnaces.

**Flue placement**: Flue (exhaust) locations determine gas flow patterns. In a downdraft design, flues at floor level pull gases down through the charge, improving uniformity. In an updraft design, the flue at the top provides the simplest path but the least uniform heating. Flue cross-sectional area must be adequate to handle the gas volume without excessive back-pressure: roughly 1/15 to 1/20 of the hearth area for natural-draft furnaces.

## Temperature Measurement and Control

Controlling furnace temperature requires measuring it first. The choice of measurement method depends on the temperature range, required accuracy, and available instrumentation.

**Measurement methods**:

| Method | Range | Accuracy | Response Time | Notes |
|---|---|---|---|---|
| Visual observation (color) | 500-1500°C | ±50-100°C | Instant | Red heat ≈ 500°C, cherry red ≈ 700°C, orange ≈ 900°C, yellow ≈ 1100°C, white ≈ 1300°C+ |
| Pyrometric cones (Seger) | 600-1600°C | ±20°C | Slow (minutes) | Standardized ceramic pyramids that bend at rated temperature |
| Type K thermocouple (Ni-Cr/Ni-Al) | −200 to +1250°C | ±2-3°C | 1-10 seconds | Most common industrial thermocouple; degrades above 1100°C in oxidizing atmosphere |
| Type S thermocouple (Pt/Pt-10%Rh) | 0 to +1600°C | ±1-2°C | 1-10 seconds | High-accuracy standard; expensive; used for steel and glass |
| Type B thermocouple (Pt-30%Rh/Pt-6%Rh) | 0 to +1800°C | ±2-3°C | 1-10 seconds | For extreme temperatures; reference junction compensation not needed above 50°C |
| Optical pyrometer | 700-3000°C | ±10-20°C | Instant (non-contact) | Measures color of hot surface; requires knowledge of emissivity |
| Infrared thermometer | −50 to +2000°C | ±1-2% | 0.1-1 second | Non-contact; emissivity setting critical; affected by intervening gases or smoke |

**Temperature control strategies**:

- **Manual fuel regulation**: Operator adjusts fuel rate by visual observation of flame color and charge glow. Accurate to ±50-100°C. Used in all early-stage furnaces.
- **Damper control**: Adjusting chimney damper changes draft, changing air supply and combustion rate. Provides ±20-50°C control. Simple mechanism (a sliding plate in the flue).
- **Automatic burner control**: Gas valve + air damper linked by a mechanical ratio regulator or electronic controller. Thermocouple feedback to PID controller drives the valve. Accurate to ±5-10°C. Requires electricity.
- **Zone control**: Multiple thermocouples and burners divided into zones, each independently controlled. Achieves ±5°C uniformity across large furnaces. Required for tunnel kilns and continuous furnaces.

## Insulation vs Refractory Hot-Face Design

A well-designed furnace wall has distinct layers, each serving a different purpose:

**Hot-face (working lining)**: The inner layer that directly contacts the furnace atmosphere and charge. Must withstand the full process temperature, resist chemical attack from slag and furnace gases, and survive thermal cycling. Dense refractory brick (fireclay, high-alumina, magnesite — depending on application). Thermal conductivity is relatively high (1-5 W/(m·K)), so this layer alone provides little insulation.

**Backup insulation**: One or more layers behind the hot-face, designed to reduce heat loss. Insulating firebrick (k ≈ 0.15-0.4 W/(m·K)) or ceramic fiber blanket (k ≈ 0.05-0.15 W/(m·K)). Cannot withstand direct flame or slag contact — must be protected by the hot-face.

**Shell**: Steel plate (3-6 mm) enclosing the furnace. Provides structural support, contains the refractory, and serves as the final barrier against gas leaks. Shell temperature should be kept below 80°C for personnel safety; above this, external guards or warning labels are required.

**Design calculation**: Given a target interior temperature, select composite wall layers to achieve acceptable heat loss while keeping shell temperature below 80°C. Example for a 1200°C furnace:

| Layer | Material | Thickness | k (W/(m·K)) | Temperature Drop |
|---|---|---|---|---|
| Hot-face | Dense fireclay brick | 230 mm (2 courses) | 1.2 | 1200°C → 1050°C |
| Backup | Insulating firebrick | 230 mm (2 courses) | 0.25 | 1050°C → 450°C |
| Wrap | Ceramic fiber blanket | 50 mm | 0.10 | 450°C → 250°C |
| Shell | Steel plate | 6 mm | 50 | 250°C → 248°C |

Total heat loss: approximately 2.1 kW/m² of wall area. Compare to the same furnace with only dense fireclay (230 mm, no backup): approximately 6.0 kW/m² — nearly 3× the fuel waste.

**Thermal mass consideration**: Thick refractory walls take a long time to heat up (thermal lag). A furnace with 460 mm total wall thickness may require 8-12 hours to reach operating temperature from cold. For batch furnaces that cycle between hot and cold, thermal mass wastes energy on every cycle. For continuous furnaces that run for weeks or months at temperature, thermal mass is a one-time cost and insulation thickness is more important.

## Flue Gas Handling and Heat Recovery

Flue gases leaving the furnace carry significant energy. For a furnace operating at 1200°C with 50% excess air, flue gas exits at approximately 800-1000°C — containing 40-60% of the fuel's energy input. Recovering this waste heat is the single most effective way to improve furnace efficiency.

**Stack losses**: The two components of stack loss are **sensible heat** (hot gas carries energy out) and **latent heat** (water vapor from combustion of hydrogen in the fuel). Sensible heat loss is proportional to flue gas temperature and volume. Reducing either reduces the loss.

**Heat recovery methods**:

- **Combustion air preheat**: Pass flue gas through a heat exchanger (recuperator or regenerator) to preheat incoming combustion air. Every 100°C of air preheat saves approximately 2-3% fuel. A recuperator heating combustion air from 20°C to 400°C saves roughly 10-12% fuel.
- **Charge preheat**: Use flue gas to preheat the incoming charge material (scrap steel, ore, raw ceramics). Preheating scrap steel to 600°C before charging into an EAF reduces electrical energy consumption by 60-80 kWh per tonne.
- **Waste heat boiler**: Generate steam from flue gas heat. Economical when the furnace runs continuously and there is a use for the steam (power generation, process heat).
- **Counterflow design**: In continuous furnaces (tunnel kilns, shaft furnaces), arrange the charge flow so that hot outgoing product preheats incoming cold charge. This is the principle behind climbing kilns and blast furnace counterflow.

**Recuperator types**:

| Type | Effectiveness | Max Flue Gas Temp | Notes |
|---|---|---|---|
| Tube-in-tube (radiation) | 40-60% | 1100°C | Simple; flue gas flows through a large central tube, air through the annular gap |
| Plate finned (convection) | 50-70% | 800°C | Compact; higher pressure drop |
| Ceramic recuperator | 50-65% | 1400°C | For very high temperature flue gas; ceramic tubes resist thermal shock |
| Regenerator (checker brick) | 70-85% | 1500°C | Stores heat in brick checkerwork; alternating flow direction every 15-30 minutes |

**Draft control**: Flue gas must be removed from the furnace at the right rate. Too much draft pulls cold air in through door gaps and cracks (tramp air), wasting fuel heating air that bypasses the combustion zone. Too little draft causes back-pressure, pushing hot gases out through doors and observation ports (dangerous, wasteful). Target: slight negative pressure inside the furnace (2-5 Pa below atmospheric) at the flue exit.

## Fuel-to-Heat Efficiency

Furnace efficiency measures how much of the fuel energy input ends up as useful process heat in the charge:

    η = Q_useful / Q_fuel × 100%

where Q_useful is the energy absorbed by the charge (heating, melting, chemical reactions) and Q_fuel is the total fuel energy input (lower heating value × fuel mass).

**Efficiency by furnace type**:

| Furnace Type | Thermal Efficiency | Major Loss Path |
|---|---|---|
| Scove kiln (wood, open) | 10-20% | Flue gas (60-70%), wall losses (10-20%) |
| Updraft batch kiln (wood) | 15-25% | Flue gas (50-60%), wall losses (15-25%) |
| Downdraft kiln (wood/coal) | 20-30% | Flue gas (45-55%), wall losses (15-20%) |
| Gas-fired batch furnace | 25-40% | Flue gas (40-50%), wall losses (10-20%) |
| Electric resistance furnace | 80-95% | Wall losses only (no flue gas) |
| Blast furnace (coke) | 40-50% | Top gas (35-45%), cooling (5-10%) |
| Tunnel kiln (gas, continuous) | 40-60% | Flue gas (25-35%), wall losses (10-15%) |
| EAF (electric) | 55-75% | Off-gas (15-25%), cooling water (10-20%) |

**Heat balance**: A complete heat balance accounts for all energy flows:

    Fuel input = Useful heat + Flue gas loss + Wall loss + Opening loss + Cooling water loss + Unburned fuel loss

- **Useful heat**: Heating the charge from ambient to process temperature + latent heat of melting + endothermic reaction enthalpy.
- **Flue gas loss**: Sensible heat in dry flue gas + latent heat in water vapor. Calculated from flue gas temperature, volume, and composition.
- **Wall loss**: Steady-state conduction through the furnace walls (from the composite wall calculation above).
- **Opening loss**: Radiation through doors, ports, and gaps. An open 0.3 m × 0.3 m observation port at 1200°C radiates approximately 20 kW — a surprising amount.
- **Cooling water loss**: For water-cooled furnace elements (EAF panels, blast furnace tuyeres).
- **Unburned fuel loss**: Carbon monoxide and soot in the flue gas represent incomplete combustion. Minimized by adequate excess air.

**Quick efficiency estimate**: Measure flue gas temperature and O₂ content. Higher flue gas temperature = more waste heat. Higher O₂ = more excess air = more waste heat. A rough rule: flue gas loss ≈ (flue gas temperature − ambient temperature) × 0.5% per 10°C at 20% excess air. So a furnace with flue gas at 900°C and 20°C ambient loses roughly (900 − 20) × 0.05 ≈ 44% of fuel energy in the stack.

## Scaling and Dimensional Considerations

Furnace performance does not scale linearly with size. Understanding scaling laws prevents expensive design errors.

**Heat loss scales with surface area; output scales with volume**: A furnace that is twice as large in every dimension (2× length, 2× width, 2× height) has 8× the volume (charge capacity) but only 4× the surface area (heat loss area). This means larger furnaces are inherently more fuel-efficient per unit of output. This is why industrial furnaces are large and craft furnaces are inefficient.

**Specific fuel consumption** (kg fuel per kg product) decreases with furnace size:
- Small batch kiln (0.1 m³): 3-5 kg wood per kg pottery
- Medium batch kiln (1 m³): 1.5-2.5 kg wood per kg pottery
- Large tunnel kiln (30 m): 0.5-1.0 kg gas per kg product

**Wall thickness must increase with temperature, not with size**: A furnace operating at 1200°C needs the same refractory thickness regardless of whether it is 0.5 m or 5 m in diameter. However, larger furnaces have more thermal expansion in absolute terms, requiring expansion joints every 2-3 m of wall length (5-10 mm gap filled with ceramic fiber).

**Heating rate limits**: The maximum safe heating rate is limited by the thermal shock resistance of the refractory and the charge. Heating too fast causes spalling (surface flakes off the refractory) or cracking in the charge. For fireclay brick, the safe heating rate below 800°C is approximately 50-100°C/hour; above 800°C, 100-200°C/hour. These limits apply regardless of furnace size — a large furnace with many burners can heat faster only if the temperature is uniform.

**Burner density**: For gas- or oil-fired furnaces, the number of burners must provide uniform coverage without dead zones. A rough guide: one burner per 0.5-1.0 m² of hearth area for uniform heating. Burners should be staggered on opposite walls to create a swirling gas pattern that eliminates cold spots.

## Refractory Installation and Maintenance

**Dry-laid vs mortared**: Refractory bricks can be laid dry (no mortar, tight joints) or with refractory mortar. Dry-laid construction allows thermal expansion without mortar cracking but requires precisely ground brick faces. Mortared joints should be kept thin (2-3 mm) — thick mortar joints are the weak point that fails first under thermal cycling. Use matching mortar: fireclay mortar for fireclay brick, high-alumina mortar for high-alumina brick.

**Expansion joints**: All refractories expand when heated. Silica brick expands approximately 1.3% from room temperature to 1200°C — a 3 m wall grows 39 mm. Without expansion joints, the wall buckles and collapses. Leave expansion joints every 2-3 m of wall length, 5-10 mm wide, packed with ceramic fiber blanket (which compresses to accommodate expansion).

**Washing and spalling**: The two main failure modes for refractory linings:
- **Washing** (erosion): Molten slag or metal flowing across the refractory surface gradually dissolves and erodes the lining. Rate depends on slag chemistry, temperature, and velocity. Typical lining wear: 0.5-3 mm per 100 hours of operation in aggressive steelmaking environments.
- **Spalling**: Thermal shock or structural stress causes the refractory surface to crack and flake off in layers 10-50 mm thick. Causes: rapid heating/cooling, moisture penetration into the brickwork (steam pressure blows off the hot face), or large thermal gradients through the wall thickness.

**Lining life expectations**:

| Application | Lining Material | Expected Life | Failure Mode |
|---|---|---|---|
| Pottery kiln (1200°C, batch) | Fireclay brick | 500-2000 firings | Spalling, crack growth |
| EAF steelmaking (1650°C, basic slag) | Magnesite brick | 500-2000 heats | Slag washing at slag line |
| Blast furnace hearth (1500°C, reducing) | Carbon blocks | 5-15 years | Erosion from liquid iron |
| Glass tank (1500°C, continuous) | Fused-cast AZS | 5-10 years | Glass corrosion |
| Lime shaft kiln (1100°C, continuous) | High-alumina brick | 2-5 years | Thermal cycling spalling |

**Relining**: When the hot-face lining has worn to approximately 50% of original thickness, the furnace must be relined. Relining requires: cool down (24-72 hours), remove spent lining (manual demolition), repair the backup insulation if damaged, install new hot-face brick, dry and cure (7-28 days depending on size). Total downtime: 2-6 weeks for an industrial furnace.

## Safety in Furnace Design

**Refractory drying**: New refractory contains chemically bound and free moisture. Heating too fast converts this water to steam faster than it can escape through the pore structure, building pressure that explosively spalls the hot face. Dry-out schedule: 20-100°C at 10-15°C/hour (hold 12-24 hours at 100°C), 100-300°C at 20-30°C/hour (hold 8-12 hours at 300°C), then ramp to operating temperature at 50-100°C/hour.

**Carbon monoxide**: All combustion furnaces produce CO, especially during start-up and shutdown when combustion is incomplete. CO is lethal at 1200 ppm (NIOSH IDLH). CO is colorless, odorless, and produces no irritation. Ventilate all furnace areas. Install CO detectors with audible alarms. Evacuate at 50 ppm. Never enter a furnace enclosure during operation or immediately after shutdown without verifying CO concentration.

**Molten metal and slag**: Temperatures above the melting point of iron (1538°C) mean that any metal or slag spill will flow and ignite combustibles on contact. Furnace design must include: spill containment (tilting designs that direct spills to a safe area), dry charge materials (moisture in scrap causes steam explosions on contact with molten metal), and heat-resistant barriers around the tap area.

**Thermal radiation**: Open furnace doors at operating temperature emit intense infrared radiation. At 1200°C, an open 0.5 m × 0.5 m port emits approximately 170 kW of radiant heat — enough to cause burns within seconds at 2 m distance. Face shields with IR-filtering lenses are mandatory for furnace viewing. Limit exposure time near open ports.

**Refractory dust**: Cutting, grinding, or demolishing refractory brick generates respirable crystalline silica dust (from fireclay and silica brick) and alumina dust. Silica dust causes silicosis. Wear P100 respirators during refractory installation and removal. Wet cutting methods suppress dust.

## See Also

- [Electric Furnaces](electric-furnaces.md) — EAF, SAF, and resistance heating furnaces
- [Kilns](../ceramics/kilns.md) — Kiln construction for ceramics and lime
- [Blast Furnace](../metals/blast-furnace.md) — Iron smelting furnace design

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Energy](./index.md) • [All Domains](../../index.md)*

