# Salt / Halite Production

> **Node ID**: mining.salt
> **Domain**: [Mining](./index.md)
> **Dependencies**: [`Food Processing`](food-processing.md), [`Electrolysis`](electrolysis.md)
> **Enables**: [`Energy`](energy.md)
> **Timeline**: Years 1-10
> **Outputs**: salt, brine, rock-salt
> **Critical**: No

## Overview

Extraction of halite (rock salt) and brine from underground deposits, salt pans, and seawater evaporation. Salt is essential for food preservation, chlor-alkali electrolysis (chlorine and caustic soda), and as a chemical feedstock. Enables the foundational inorganic chemistry of the industrial revolution.

This technology is characteristic of the Stone Age era of industrial development. It builds on earlier foundational techniques while enabling more precise and controlled manufacturing outcomes.

Primary outputs: `salt`, `brine`, `rock-salt`. These materials or products serve as inputs for downstream manufacturing and processing steps.

Salt is one of the few minerals that humans consume directly in large quantities. Beyond its role as a flavoring agent, salt preserves meat and fish by drawing out moisture and inhibiting bacterial growth — without refrigeration, salting is the primary long-term food preservation method. Industrially, salt feeds the chlor-alkali process (electrolysis of brine to produce chlorine gas and sodium hydroxide), which underpins bleaching, disinfection, and much of the chemical industry. Salt also serves as a raw material for soda ash (sodium carbonate) production via the Solvay process.

Historically, salt was so economically important that it served as currency (the word "salary" derives from the Roman practice of paying soldiers in salt). Control of salt production and trade was a major source of political power.

## Prerequisites

### Materials

- **Seawater or brine** — the primary raw material for evaporation methods. Seawater contains ~3.5% dissolved salts (predominantly NaCl). Brine springs may be much more concentrated.
- **Fuel (for boiling methods)** — wood, coal, or peat for heating brine pans. Fuel consumption is substantial — boiling off 1,000 liters of brine to recover ~260 kg of salt requires burning roughly equivalent energy in fuel.
- **Clay or stone** — for lining evaporation ponds and constructing boiling pans. Clay-lined ponds prevent brine from seeping into the ground.

### Equipment

- **Evaporation ponds**: Shallow, clay-lined basins with controlled inlet and outlet channels. Series of ponds at increasing salinity (concentrators leading to crystallizers). Gravity flow between ponds where possible.
- **Boiling pans**: Large flat iron or ceramic pans over fire hearths. Iron pans conduct heat better and last longer; ceramic pans are available at lower technology levels.
- **Rakes and hoes**: Wooden or iron tools for harvesting crystallized salt from pond bottoms.
- **Hydrometer**: Glass or sealed reed float for measuring brine density (specific gravity).
- **Storage**: Covered, dry storage for finished salt. Salt absorbs moisture from humid air. Wooden bins or sealed clay containers.
- [Food Processing](food-processing.md) — material dependency
- [Electrolysis](electrolysis.md) — material dependency

### Downstream Applications

Salt produced by these methods serves three primary purposes in a bootstrap civilization:

1. **Food preservation**: Salting meat and fish at 10-20% concentration prevents bacterial growth for months. The most energy-efficient food preservation method available at any technology level.
2. **Chemical feedstock**: Electrolysis of brine produces chlorine gas (bleaching, disinfection, water treatment) and sodium hydroxide (soap making, paper pulping, chemical manufacturing). The chlor-alkali process is the gateway to industrial inorganic chemistry.
3. **Iodization**: Adding potassium iodide at 20-40 mg per kg of salt prevents iodine deficiency disorders (goiter, cretinism) — the simplest public health intervention available. Requires only trace amounts of KI and basic mixing equipment.

### Knowledge

- Understanding of brine concentration and saturation behavior — how salt precipitates at different concentration levels
- Familiarity with pond management for solar evaporation — flow rates, pond depth, and crystallizer timing
- Ability to assess salt purity by taste, appearance, and simple dissolution testing
- Safety training for underground mining operations (where applicable) and brine boiling hazards
- Understanding of seasonal effects on evaporation rates and production planning

### Infrastructure

- **Evaporation pond system** (solar method): Series of shallow clay-lined ponds with intake channels from the sea or brine source, interconnected by gravity-flow channels, and a final crystallizer pond for harvesting. Land requirement: hectares for production-scale output.
- **Boiling house** (boiling method): Building with fire hearths and ventilation flues for brine evaporation. Fuel storage area. Drainage for spent brine.
- **Mine infrastructure** (rock salt): Shaft access, ventilation, haulage, and groundwater pumping. Similar to conventional mining operations.
- **Dry storage**: Covered warehouse with raised floor. Salt must be kept dry from production through to end use.

## Process Description

Salt extraction varies dramatically by deposit type and geography. The three principal methods — seawater evaporation, solution mining, and rock salt mining — each suit different geological settings and technology levels.

### Step-by-Step Procedure

1. Survey the site to confirm presence and concentration of the target material. Document geological conditions. Coastal sites for solar evaporation; inland salt flats or brine springs for pan evaporation; geological survey for underground deposits.
2. Prepare the extraction site: clear vegetation, establish drainage, set up equipment. Install safety barriers for underground operations.
3. Begin extraction using the method appropriate to deposit type and depth:
   - **Solar evaporation (coastal)**: Draw seawater into a series of shallow, interconnected ponds. As water evaporates under sun and wind, salt concentration increases. In the final crystallizer pond, salt crystals precipitate and settle to the clay-lined bottom. Harvest by raking crystals to the edge and draining remaining brine. Requires warm, dry climate with consistent wind. Cycle time: weeks to months depending on weather. Multiple ponds allow continuous production — as one pond crystallizes, the next is concentrating.
   - **Solution mining (brine wells)**: Drill or dig a shaft into a salt deposit. Pump water down the shaft to dissolve the salt. Bring the saturated brine back to the surface. Boil the brine in iron or ceramic pans over a fire to evaporate the water, leaving crystalline salt. Fuel consumption is high — wood or coal. This method accesses deep salt beds without excavating solid rock.
   - **Rock salt mining**: When salt deposits form solid underground layers (bedded deposits or salt domes), mine the solid rock salt directly using conventional mining techniques (room-and-pillar). Crush the mined rock salt and purify by dissolving and re-crystallizing if higher purity is needed. Alternatively, use the rock salt directly for road de-icing and industrial applications where purity is less critical.
4. Process extracted material through crushing, washing, or re-crystallization to concentrate the product and remove impurities.
5. Transport processed material to storage. Record yield and quality for each batch.
6. Rehabilitate the site as operations progress — backfill, regrade, revegetate.

### Extraction Methods Comparison

| Method | Deposit Type | Energy Required | Purity | Climate Dependency |
|--------|-------------|----------------|--------|-------------------|
| Solar evaporation | Seawater | Sunlight only | Moderate | High — needs sun and wind |
| Solution mining + boiling | Underground salt bed | High (fuel for boiling) | High | None |
| Rock salt mining | Solid salt deposit | Moderate (drilling, hauling) | Low to moderate | None |
| Salt pan evaporation (inland) | Brine springs | Sunlight + some fuel | Moderate | Moderate |

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Seawater salinity | ~3.5% | Varies by location; higher in arid coastal regions |
| Brine saturation | ~26% NaCl by weight | Point at which crystallization begins |
| Solar evaporation rate | Climate-dependent | Hot, dry, windy conditions optimal |
| Boiling pan temperature | Near boiling point | Fuel-intensive; wood or coal consumption high |
| Crystal size | Process-dependent | Slow evaporation = larger crystals; rapid boiling = fine grains |

## Safety Considerations

This process involves specific hazards requiring trained personnel and protective measures:

- **Cave-ins**: Underground rock salt mining shares all the structural hazards of conventional mining. Salt is relatively plastic under geological pressure — rooms may close over time. Maintain generous pillar dimensions.
- **Salt dust inhalation**: Rock salt mining and crushing produce fine salt dust. Prolonged inhalation irritates respiratory passages. Mechanical ventilation required for underground operations.
- **Brine flooding**: Underground salt is soluble. Water intrusion into a salt mine dissolves the walls and floor, potentially causing rapid flooding. Monitor for water ingress constantly.
- **Thermal burns**: Brine boiling operations involve open fires and hot concentrated brine. Salt splatter at high temperature causes severe burns.
- **Sun exposure and heat**: Solar evaporation ponds are typically in hot, arid climates. Workers face heat exhaustion and severe sun exposure during pond maintenance and salt harvesting.

### Personal Protective Equipment

- Safety glasses or face shield — brine splatter at boiling temperature causes eye damage
- Heat-resistant gloves for handling hot brine pans and boiled salt
- Respiratory protection for salt dust during crushing and handling operations
- Hearing protection in underground mining operations
- Steel-toe boots for mine operations and heavy equipment handling
- Sun hat and long sleeves for solar pond workers — prolonged exposure to sun reflected off white salt surfaces intensifies UV exposure

### Emergency Procedures

- Maintain first aid kit with burn treatment for brine boiling operations. Hot concentrated brine causes deep burns that are worse than hot water due to the salt content.
- Know locations of emergency shutoffs for brine pumps and mine water pumps.
- Establish evacuation routes and assembly points. Underground salt mines must have clear exit routes marked.
- Train all personnel on flood response for underground mines. Water ingress is the primary life-threatening hazard in salt mining — salt dissolves, so flooding can be rapid and catastrophic.
- For solar pond operations, have shade structures and water available for workers experiencing heat exhaustion.

## Quality Control

### Acceptance Criteria

- **Salt (food grade)**: White to off-white color, free of visible impurities (sand, clay, organic matter). Taste is purely salty with no bitter aftertaste (bitterness indicates magnesium or calcium salts). Moisture content low enough that salt flows freely.
- **Brine**: Clear, saturated solution (~26% NaCl). Specific gravity measured with a hydrometer. Free of suspended solids.
- **Rock Salt**: Minimum 90% NaCl content. Contaminating minerals (gypsum, anhydrite, clay) acceptable for industrial use but not for food.

### Testing Methods

- **Purity test**: Dissolve a weighed sample in water. Filter to remove insoluble impurities (weigh the residue). Evaporate the filtered solution and weigh the recovered salt. Purity = recovered salt / original sample × 100%.
- **Taste test**: Quick field method — food-grade salt should taste purely salty. Bitterness indicates magnesium salts; astringency indicates calcium.
- **Hydrometer reading**: Measure brine specific gravity to determine saturation level. Saturated brine at room temperature has a specific gravity of approximately 1.20.
- **Visual inspection**: Color, crystal size, and presence of foreign material. Pure salt is white; discoloration indicates impurities.

### Sampling Protocol

- Inspect first-article output against full specification. For food-grade salt, check color, taste, and moisture.
- Sample subsequent production at defined intervals. Test purity by dissolution method on a representative sample from each batch.
- Record all measurements for trend analysis. Track salt purity and moisture content over time.
- Reject and investigate any out-of-specification results. Contaminated salt may contain harmful minerals or organic matter.
- For underground mining, also track roof conditions and pillar stability in active areas on a regular schedule.

## Scaling Notes

Transitioning from bench-scale to production involves these considerations:

- **Bench scale (individual/family)**: Small salt pan or beach boiling. Sufficient for local food preservation needs. Output measured in kilograms per week.
- **Pilot scale (community)**: Series of interconnected solar evaporation ponds, or a brine well with multiple boiling pans. Multiple workers. Output measured in tonnes per season.
- **Production scale (industrial)**: Large coastal salt works covering hectares; deep solution mines with mechanical brine pumps and industrial-scale evaporation. Output measured in thousands of tonnes per year. Feeds chemical industry (chlor-alkali plants) in addition to food preservation.

Key scaling challenges: fuel supply for brine boiling (solar evaporation avoids this constraint but is climate-limited), land area for evaporation ponds, and transportation logistics from remote salt deposits to population centers.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low recovery | Wrong parameters for ore grade | Adjust leach time and concentration |
| Equipment blockage | Material buildup | Install screening; regular cleaning |
| Water ingress | Groundwater intrusion | Improve drainage; add pumping |
| Product contamination | Cross-contamination | Separate streams; clean between batches |

## Variations and Alternatives

- **Solar evaporation (coastal ponds)**: Lowest energy input, highest climate dependency. Works best in arid coastal regions with consistent sun and wind. The dominant method in suitable climates — Mediterranean, tropical coasts, salt lakes.
- **Brine boiling (inland)**: Works anywhere brine springs or salt deposits are accessible. Fuel-intensive but climate-independent. The traditional method in Northern Europe where solar evaporation is impractical.
- **Rock salt mining**: Accesses deep solid deposits. Requires conventional mining capability (shafts, ventilation, haulage). Produces salt that may need re-crystallization for food-grade purity. Useful for industrial-scale supply.
- **Salt from salt lakes**: Natural saline lakes (Dead Sea, Great Salt Lake) produce salt by simple evaporation. Harvesting is straightforward but may require purification to remove undesirable co-precipitated minerals.

## References

- [Mining Engineering & Extractive Metallurgy](mining.md) — parent capability
- [Mining Domain](./index.md) — domain overview and related capabilities
- [Food Processing](food-processing.md) — upstream dependency (material)
- [Electrolysis](electrolysis.md) — upstream dependency (material)
- [Energy](energy.md) — downstream capability

Salt production connects to [Food Processing](food-processing.md) through food preservation (salting, curing), to [Chemistry](../chemistry/index.md) through the chlor-alkali electrolysis process and soda ash production, and to [Health](../health/index.md) through iodization programs that prevent goiter and cretinism.

The availability of salt often determines the viability of a settlement. Inland communities without access to salt deposits must trade for it — historically, salt trade routes were among the first long-distance commercial networks. A community that can produce surplus salt has a trade good with universal demand.


### Material Handling

Proper handling of input materials and products is essential for consistent results:

- Store finished salt in covered, dry containers. Salt is hygroscopic — it absorbs atmospheric moisture and clumps or dissolves in high humidity. Sealed wooden kegs or clay jars with tight lids.
- Use FIFO (first-in, first-out) inventory management. Older salt may have absorbed moisture and caked.
- Label all containers with source, date produced, and grade (food or industrial).
- Inspect salt before use — reject any that shows discoloration, contamination, or excessive moisture.
- Segregate waste streams: bittern (the concentrated residual brine after salt crystallization) contains magnesium and potassium salts that can be processed separately or used for other applications.
- Protect stored salt from rain and flooding. A flooded salt store is a total loss.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Mining](./index.md) · [All Domains](../index.md)*
