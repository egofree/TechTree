# Thermal Insulation

> **Node ID**: ceramics.thermal-insulation
> **Domain**: [Ceramics](./index.md)
> **Dependencies**: [`Energy`](energy.md), [`Cryogenics`](cryogenics.md)
> **Enables**: [`Basic Glass Production`](basic.md), [`Ceramics & Refractories`](ceramics.md)
> **Timeline**: Years 15-30
> **Outputs**: mineral-wool, ceramic-fiber, foam-insulation
> **Critical**: No

## Overview

Thermal insulation materials slow the movement of heat between a hot zone and a cooler environment. In an industrial civilization, the ability to retain heat in furnaces, kilns, steam pipes, and buildings directly determines energy efficiency and process viability. This capability covers three product families: mineral wool (spun from molten rock or slag), ceramic fiber blankets (alumina-silica fibers for temperatures above 1000 degrees C), and foam insulation (polymer-based closed-cell boards for ambient-temperature applications).

Mineral wool production traces back to the observation that volcanic eruptions produce natural fiber blankets when molten basalt hits the air. Industrial mineral wool replicates this by melting basalt, diabase, or blast furnace slag at 1300 to 1500 degrees C, then spinning the melt through a high-speed rotor or blowing it with steam jets. The resulting tangled mat of glassy fibers traps still air, which is the actual insulating medium. Ceramic fiber takes the same principle to higher temperatures by using alumina and silica raw materials that resist recrystallization at 1200+ degrees C. Foam insulation boards, the youngest of the three families, trap gas bubbles inside a polymer matrix for building envelopes and refrigeration.

All three families work by the same physical mechanism: dividing a continuous gas space into many small pockets, which suppresses convection, and interposing solid barriers, which block radiation at high temperatures. The thermal conductivity of mineral wool hovers around 0.035 to 0.040 W/(m K), ceramic fiber around 0.08 to 0.15 W/(m K) at mean temperature, and rigid foam boards around 0.020 to 0.028 W/(m K). Despite the higher thermal conductivity of ceramic fiber at room temperature, its advantage is that it retains insulating capability at temperatures where mineral wool would have long since melted or sintered.

Water resistance varies significantly between the three families. Mineral wool absorbs water readily and loses most of its insulating value when wet. Hydrophobic treatments (silicone or mineral oil emulsions) are added during production to improve water shedding, but prolonged immersion will eventually saturate the material. Ceramic fiber is hydrophobic by nature and does not absorb water. Closed-cell foam boards resist water absorption due to their cell structure, but the facing material and joint detailing determine whether water can penetrate the insulation system as a whole.

Primary outputs: `mineral-wool`, `ceramic-fiber`, `foam-insulation`.

## Prerequisites

### Materials

- **Basalt, diabase, or blast furnace slag**: The primary raw material for mineral wool. Slag from iron smelting is the cheapest source when available. Basalt and diabase are mined and crushed to 5 to 10 cm feed size. The chemical composition of the feed material affects the fiber properties: higher silica content produces more chemically resistant fibers, while higher calcium and magnesium content lowers the melting temperature
- **Alumina and silica**: Raw materials for ceramic fiber. Kaolin clay (approximating a 50/50 alumina-silica blend) is a common starting point. Higher alumina content raises the maximum service temperature. Zirconia can be added for grades that must withstand 1400+ degrees C
- **Phenolic or acrylic resin binder**: Applied as a spray during fiber formation to hold the wool mat together. Cured in an oven at 200 to 250 degrees C
- **Polyol and isocyanate**: The two reactive components for polyurethane foam insulation. Mixed at a 1:1 ratio by volume; the exothermic reaction creates CO2 or uses a blowing agent to expand the foam
- **Coke or natural gas**: Fuel to reach melting temperatures. Mineral wool cupola furnaces consume 150 to 200 kg of coke per ton of melt. Electric furnaces avoid the fuel handling but require high-capacity electrical supply (5 to 10 MW for a medium-scale plant)

### Equipment

- **Cupola or electric furnace**: A shaft furnace for melting rock or slag. Cupola furnaces use coke as fuel and air blast. Electric arc or resistance furnaces avoid combustion gases contaminating the melt. Electric furnaces produce cleaner fiber (fewer impurities from the fuel) but have higher operating costs in regions with expensive electricity
- **Spinning rotor or steam blower**: The fiberizing device. A high-speed spinning disc (2000 to 4000 RPM) throws molten material into fine fibers. Alternatively, high-pressure steam or air jets attenuate a stream of melt into fibers. The spinning rotor method gives better control over fiber diameter and produces fewer shot particles, making it the preferred method for higher-quality insulation grades
- **Collection chamber and conveyor**: A cyclone chamber where fibers settle onto a moving conveyor belt, forming a continuous mat. The suction beneath the perforated conveyor draws fibers downward and compacts the mat. The conveyor speed directly controls the mat thickness and density
- **Curing oven**: A through-feed oven at 200 to 250 degrees C that crosslinks the binder resin, bonding the fibers into a rigid board or blanket. The oven must provide uniform temperature across its full width to avoid variations in binder cure. Over-cured binder becomes brittle and loses adhesion. Under-cured binder leaves the board tacky and produces formaldehyde emissions
- **Foam dispensing machine**: A high-pressure mixing head that combines polyol and isocyanate, dispenses the mixture into a mold or onto a conveyor, where it expands and cures. The mixing head must deliver the two components at precisely controlled temperatures and pressures (typically 100 to 200 bar) to ensure proper mixing and consistent cell structure

### Knowledge

- Understanding how fiber diameter (3 to 8 micrometers for mineral wool, 2 to 4 micrometers for ceramic fiber) affects thermal performance and respirability
- Binder chemistry: phenolic resin cure schedules and how over-cure embrittles the board. Under-cure leaves the binder tacky and produces formaldehyde odor. The cure window for phenolic binder is relatively narrow, typically 200 to 250 degrees C for 5 to 15 minutes
- Foam chemistry: the role of catalysts (amine for gelling, tin for blowing) and surfactants in controlling cell structure. The ratio of gelling catalyst to blowing catalyst determines whether the foam rises before it sets (producing low-density open-cell foam) or sets before it rises fully (producing higher-density closed-cell foam)
- Density management: how mat thickness and compression affect both thermal conductivity and mechanical strength. Higher density mineral wool boards are stronger but conduct more heat through the solid fiber network. The optimum density for most building insulation applications is 30 to 60 kg/m3

### Infrastructure

- A furnace hall with high-capacity ventilation to remove fumes from binder cure and slag melting. The ventilation system should be designed to capture fumes at the source (curing oven exhaust, furnace tap stream) rather than relying on general room air exchange
- Fuel storage and handling for cupola furnaces (coke bins, charging skips). Coke storage must be covered to prevent rain from wetting the charge, which would reduce furnace efficiency and generate steam during charging
- A dry, enclosed space for foam chemical storage. Isocyanates react with moisture and must be kept sealed. The storage temperature should be controlled between 15 and 25 degrees C to maintain the viscosity within the pumpable range

## Process Description

### Mineral Wool Production

1. **Feed preparation**: Crush basalt, diabase, or slag to 5 to 10 cm pieces. Blend with coke (for cupola furnaces) in the correct charge ratio, typically 3 to 4 parts stone per 1 part coke by weight. The coke serves dual purpose as fuel and as a reducing agent that affects the oxidation state of iron in the melt, which in turn affects the fiber color and properties
2. **Melting**: Charge the cupola furnace. Air blast at 50 to 100 mbar drives combustion. Melt temperature reaches 1300 to 1500 degrees C. Tap the molten stream continuously from the furnace forehearth
3. **Fiberizing**: The molten stream falls onto a spinning rotor or into a steam jet. A four-rotor cascade system is common: the first rotor flings melt into filaments, subsequent rotors further attenuate them. Fiber diameter settles at 4 to 8 micrometers
4. **Binder spray**: Phenolic or acrylic resin emulsion is sprayed into the fiber stream in the collection chamber. The binder coats individual fibers with a thin film, typically 2 to 5 percent of finished product weight
5. **Mat formation**: Fibers settle onto a perforated conveyor under suction. The mat thickness and density are controlled by conveyor speed and suction rate. Typical finished densities: 30 to 200 kg/m3 depending on grade
6. **Curing oven**: The mat passes through a through-feed oven at 200 to 250 degrees C for 5 to 15 minutes. The binder crosslinks, bonding fiber intersections into a cohesive board
7. **Finishing**: Trim edges, cut to length, and optionally face with aluminum foil or glass tissue. Package for shipment. Aluminum foil facing serves as a vapor barrier in building applications and improves the surface emissivity for radiant heat reflection in furnace linings

The production rate is determined by the bottleneck step. In most mineral wool plants, the bottleneck is the fiberizing and collection stage, which limits how fast the mat can be built up to the target thickness. The curing oven and cutting line must be sized to keep up with the fiberizing output. A well-balanced line produces finished board at a rate of 2 to 10 tons per hour depending on the product density and thickness.

### Ceramic Fiber Production

1. **Melt**: Kaolin or blended alumina-silica is melted in an electric resistance furnace at 1700 to 1900 degrees C. The higher temperature (compared to mineral wool) reflects the higher melting point of alumina-rich compositions
2. **Blow or spin**: A stream of molten material is attenuated by high-pressure air or steam, or spun from a rotor. Fiber diameter is finer than mineral wool, typically 2 to 4 micrometers
3. **Needling**: The collected fiber blanket is passed through a needling loom that mechanically entangles the fibers with barbed needles, building structural integrity without relying on binder. Needling density (punctures per square centimeter) controls the blanket's tensile strength and its ability to maintain shape under thermal cycling. Higher needling density produces a stronger but stiffer blanket
4. **Heat treatment**: The blanket is fired at 800 to 1100 degrees C to burn off shot (unfiberized particles) and stabilize the fiber microstructure against shrinkage at service temperature. Without this heat treatment, the fibers would undergo irreversible crystallographic changes during first use at high temperature, shrinking the blanket and opening gaps in the furnace lining

### Foam Insulation Production

1. **Chemical mixing**: Polyol (containing catalyst, surfactant, blowing agent, and flame retardant) and isocyanate are metered into a high-pressure mixing head at a controlled ratio
2. **Dispensing and expansion**: The reacting mixture is dispensed into a continuous mold or onto a moving conveyor belt. Cream time (onset of expansion) occurs in 5 to 15 seconds. Rise time (full expansion) in 60 to 120 seconds. Gel time (when the foam sets) follows shortly after
3. **Curing**: The foam board passes through a heated tunnel at 40 to 60 degrees C to complete the polymerization. Full cure takes 24 hours at room temperature, but handling strength is reached in minutes
4. **Cutting**: Trim the expanded bun or slab to the target dimensions. Cut edges are trimmed square. Boards are typically 20 to 200 mm thick. The cutting operation generates polyurethane dust that must be collected and handled as non-hazardous solid waste

Mineral wool production is the most energy-intensive of the three processes because it requires melting rock. A typical mineral wool plant consumes 2 to 4 GJ of energy per ton of finished product. Ceramic fiber production is similar but requires even higher melt temperatures, offset by lower production volumes. Foam insulation production is comparatively energy-efficient because the polymerization reaction is exothermic and the expansion is driven by chemical blowing agents rather than external heat.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Mineral wool melt temperature | 1300 to 1500 degrees C | Cupola or electric furnace |
| Ceramic fiber melt temperature | 1700 to 1900 degrees C | Electric resistance furnace |
| Fiber diameter (mineral wool) | 4 to 8 micrometers | Controlled by rotor speed and melt viscosity |
| Fiber diameter (ceramic fiber) | 2 to 4 micrometers | Finer fibers for higher-temperature grades |
| Binder content | 2 to 5 percent by weight | Phenolic or acrylic |
| Curing oven temperature | 200 to 250 degrees C | 5 to 15 min residence time |
| Foam cream time | 5 to 15 seconds | Onset of expansion after mixing |
| Foam density (finished) | 30 to 45 kg/m3 | Rigid board stock |
| Mineral wool finished density | 30 to 200 kg/m3 | Lighter blankets to heavy boards |
| Ceramic fiber classification temperature | 1260 to 1400 degrees C | Maximum continuous service temperature |

## Safety Considerations

- **Respirable fibers**: Mineral wool and ceramic fiber particles below 3 micrometers in diameter are respirable. Prolonged inhalation causes lung irritation. Ceramic fiber (refractory ceramic fiber, RCF) is classified as a possible carcinogen (IARC Group 2B). Wear P100 respirators during production, cutting, and installation. Enclose fiberizing equipment and use local exhaust ventilation. After installation, fibers can be released when the insulation is disturbed during maintenance, so access to insulated areas should be controlled
- **Binder fumes**: Phenolic resin curing releases formaldehyde and phenol vapors. These are irritants and formaldehyde is a known carcinogen (IARC Group 1). The curing oven exhaust must be scrubbed or thermally oxidized before release. Workers in the curing area must be monitored for formaldehyde exposure
- **Isocyanate exposure**: Polyurethane foam production involves methylene diphenyl diisocyanate (MDI). MDI is a respiratory sensitizer. Repeated exposure can cause asthma. Use supplied-air respirators or positive-pressure hoods during foam dispensing. Isocyanate spills must be neutralized with an ammonia solution before cleanup
- **Burns and thermal hazards**: Cupola furnaces, molten slag, and curing ovens present severe burn risks. Melt temperatures exceed 1300 degrees C. Use heat-resistant PPE near the furnace and fiberizing area
- **Dust explosion**: Crushed stone, coke, and polymer powders can form explosive dust clouds. Maintain dust collection systems and avoid open flames in material handling areas

### Personal Protective Equipment

- P100 respirator or supplied-air hood when handling fiber products or isocyanates
- Heat-resistant gloves and face shield near melt furnaces
- Chemical-resistant gloves and goggles during foam chemical handling
- Long-sleeved coveralls to minimize skin contact with fibers

### Emergency Procedures

- Fiber release: evacuate area, allow fibers to settle, then clean with HEPA vacuum (never dry-sweep)
- Isocyanate spill: evacuate, don respiratory protection, contain with absorbent, neutralize with dilute ammonia solution, collect waste for hazardous disposal
- Furnace breach: shut off fuel and air blast, evacuate the furnace hall, allow to cool before inspection
- Binder fire in the curing oven: shut off the conveyor and oven heat. Close the fire dampers to starve the fire of oxygen. Use CO2 or dry chemical extinguisher. Phenolic resin fires produce thick, toxic smoke (formaldehyde, phenol). Respiratory protection is mandatory during firefighting in the curing area

## Quality Control

### Acceptance Criteria

Thermal insulation products are sold on their declared thermal conductivity (lambda value), which must be certified by testing in an accredited laboratory. The declared value includes a safety margin (the 90/90 fractile) to account for production variability. Meeting the declared lambda is the primary commercial requirement. All other quality checks support confidence in that single number.

- **Mineral wool**: Density within 5 percent of target. Thermal conductivity at 10 degrees C mean temperature not exceeding 0.040 W/(m K) for standard grades. Shot content (unfiberized beads) below 30 percent by weight
- **Ceramic fiber**: Linear shrinkage after 24-hour soak at classification temperature not exceeding 4 percent. Shot content below 15 percent. Tensile strength sufficient to handle without tearing
- **Foam insulation**: Density within 10 percent of target. Closed-cell content above 90 percent (measured by gas pycnometry). Compressive strength meeting grade specification (typically 100 to 250 kPa)

### Testing Methods

- **Thermal conductivity**: Measured with a guarded hot plate (ASTM C177) or heat flow meter (ASTM C518). Test at 10 or 24 degrees C mean temperature. This is the primary performance specification

The guarded hot plate method places the insulation sample between a heated plate and a cooled plate. At steady state, the heat flow through the sample equals the electrical power input to the heater, divided by the plate area and sample thickness. This gives thermal conductivity directly. The heat flow meter is faster and cheaper but requires calibration against a guarded hot plate. Both methods assume one-dimensional heat flow, which requires that the sample edges are well-insulated.

- **Density**: Weigh a known volume sample. Report in kg/m3
- **Shot content**: Pass a known mass of wool through a 250-micrometer sieve. Weigh the retained fraction (shot particles) and express as a percentage
- **Linear shrinkage**: Heat a sample at the classification temperature for 24 hours. Measure dimensional change. High shrinkage indicates the fiber will not hold its shape at service temperature
- **Closed-cell content**: Gas pycnometry measures the volume of gas-accessible cells. Closed-cell content below 85 percent indicates processing problems in foam production
- **Compressive strength**: Load a foam sample at a constant rate until 10 percent deformation. Report the stress at that point

### Sampling Protocol

- Test thermal conductivity on every production lot (per shift or per 1000 m2, whichever is more frequent)
- Measure density on three samples per lot, one from the start, middle, and end of the production run
- Perform shrinkage testing on ceramic fiber at least once per production campaign or when raw material sources change
- Conduct closed-cell content testing on foam boards at least once per production run, sampling from the start, middle, and end of the bun
- Record all test results by lot number. Thermal conductivity trending upward over multiple lots can indicate a gradual shift in fiber diameter or binder content that individual lot checks might not catch
- Water absorption testing on mineral wool boards exposed to high humidity. Excess water absorption degrades thermal performance and can promote mold growth in building applications. The hydrophobic treatment applied during production must be verified periodically

## Scaling Notes

Thermal insulation scales along two axes: production volume and product variety.

- **Small scale (batch)**: A small cupola or crucible furnace melts 50 to 200 kg of rock per batch. Fiberizing by hand-blowing with a steam lance. Mat laid by hand and cured in a batch oven. Output: a few hundred m2 of board per day. Suitable for meeting local demand for furnace lining and building insulation
- **Medium scale (semi-continuous)**: A continuous cupola or electric furnace feeding a multi-rotor fiberizing machine. Automatic binder spray and conveyor collection. Throughput: 1 to 5 tons of wool per hour. Curing oven integrated into the line. This is the typical scale for a regional insulation plant
- **Large scale (continuous line)**: A large electric furnace (5 to 10 MW) feeding a cascade fiberizing system with multiple spinning rotors. Automatic density control via feedback from mat weigh scales. Cutting and packaging automated. Throughput: 10 to 30 tons per hour. Foam production scales from bench-scale mixing heads (1 kg/min) to continuous slab lines (100+ kg/min)

Key scaling challenges: melting energy scales with throughput but furnace wall losses are relatively fixed, so larger furnaces are more energy-efficient per ton. Fiberizing uniformity depends on maintaining constant melt viscosity, which becomes harder at higher throughput. Binder distribution becomes less uniform in wider mats.

Product variety also drives scale decisions. A small insulation plant can produce mineral wool in a range of densities by adjusting the conveyor speed and binder rate. Adding ceramic fiber requires a separate electric furnace and different fiberizing equipment. Foam insulation requires entirely different chemical handling infrastructure. A full-spectrum insulation plant is a significant industrial investment, while a mineral-wool-only plant can start at a modest scale and expand as demand grows.

Transport costs favor regional production. Mineral wool and foam boards are low-density, high-volume products that are expensive to ship long distances. A plant serving a 300 km radius can compete with imports from further away even if the remote plant is larger and more efficient. This economic pattern encourages distributed, medium-scale insulation manufacturing rather than centralized megaplants.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| High shot content (coarse beads in wool) | Melt temperature too low or rotor speed too slow | Increase furnace temperature by 50 to 100 degrees C. Increase rotor speed. Check that the melt stream is centered on the rotor |
| Fiber blanket tears during handling | Insufficient needling or binder content too low | Increase needling passes. Raise binder spray rate by 1 to 2 percent |
| Excessive shrinkage in ceramic fiber at service temperature | Alumina content too low for the grade. Fiber recrystallizing | Use a higher-alumina blend. Check raw material purity. Consider zirconia-stabilized grades for temperatures above 1300 degrees C |
| Foam collapses or has open cells | Incorrect catalyst ratio. Isocyanate index too low. Moisture contamination in polyol | Check metering pumps. Verify the isocyanate-to-polyol ratio. Dry the polyol tank and purge with dry air |
| Uneven board density across width | Uneven binder spray distribution or inconsistent fiber landing pattern | Adjust spray nozzle positions. Check suction uniformity under the conveyor. Clean perforated conveyor belt |
| Formaldehyde odor from cured mineral wool board | Undercured binder. Oven temperature too low or line speed too fast | Raise oven temperature by 10 to 20 degrees C or slow the conveyor |

## Variations and Alternatives

- **Calcium silicate board**: A molded and autoclaved product of lime and silica. Rigid, high-temperature insulation (up to 1000 degrees C) used for pipe insulation and furnace backup. Stronger than mineral wool at equivalent density but more expensive to produce
- **Refractory castable**: A hydraulic-setting concrete made with calcium aluminate cement and lightweight aggregate. Poured or gunned into place for custom furnace linings. Not fibrous, but serves the same thermal management role in high-temperature equipment
- **Aerogel blanket**: Silica aerogel particles bonded into a fiber matrix. Extremely low thermal conductivity (around 0.013 W/(m K)) at a premium price. Used where space is at a premium, such as subsea pipeline insulation
- **Vermiculite and perlite**: Expanded mineral aggregates. Exfoliated vermiculite (heated to pop the layered structure) and expanded perlite (popped volcanic glass) are loose-fill insulations for cavity walls and high-temperature packing. Low cost, limited structural strength
- **Cellular glass**: Crushed glass mixed with a blowing agent and fired in a mold. Produces a rigid, closed-cell, completely inorganic foam. Fireproof and water-resistant. Used in below-grade and industrial applications where moisture resistance is required
- **Polystyrene foam (EPS/XPS)**: Expanded polystyrene (EPS, molded beads) and extruded polystyrene (XPS, continuous extrusion) are the most common building insulation boards. Lower temperature resistance than polyurethane (starts to soften above 75 degrees C) but cheaper and easier to produce. XPS has better moisture resistance than EPS due to its closed-cell structure
- **Asbestos (historical)**: Naturally occurring fibrous silicate minerals that were widely used for high-temperature insulation before their health hazards were understood. Asbestos insulation is no longer produced, but understanding its properties and how to identify it remains relevant for renovation and remediation work in older industrial buildings

## References

- [Ceramics & Refractories](ceramics.md) — parent capability
- [Ceramics Domain](./index.md) — domain overview and related capabilities
- [Energy](energy.md) — upstream dependency (material)
- [Cryogenics](cryogenics.md) — upstream dependency (material)
- [Basic Glass Production](basic.md) — downstream capability
- [Ceramics & Refractories](ceramics.md) — downstream capability


---

*Part of the [Bootciv Tech Tree](../index.md) · [Ceramics](./index.md) · [All Domains](../index.md)*

*Part of the [Bootciv Tech Tree](../index.md) · [Ceramics](./index.md) · [All Domains](../index.md)*
