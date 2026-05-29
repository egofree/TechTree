# Irrigation Systems

> **Node ID**: agriculture.irrigation
> **Domain**: [Agriculture](./index.md)
> **Dependencies**: [`agriculture`](./index.md), [`water.procurement`](../water/procurement.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Enables**: [`food-processing`](../food-processing/index.md), [`agriculture.soil-management`](soil-management.md)
> **Timeline**: Years 0-15+
> **Outputs**: irrigation_water, irrigated_land, water_delivery_infrastructure
> **Critical**: Yes — in arid and semi-arid climates, irrigation is the difference between productive agriculture and subsistence failure


Irrigation is the controlled delivery of water to crops at times and quantities that natural rainfall does not provide. Without irrigation, agriculture is limited to regions and seasons where precipitation meets crop water requirements — roughly 500-800 mm during the growing season for most cereals. Irrigation extends cultivation into arid regions, lengthens growing seasons, and stabilizes yields against drought. The earliest irrigation systems — simple diversion canals from rivers — predate written records and were the enabling technology for the first civilizations in Mesopotamia, the Nile valley, the Indus valley, and China.

The core engineering challenge is moving water from a source (river, well, spring, reservoir) to the root zone of plants at the right time, in the right amount, without eroding soil, waterlogging roots, or wasting labor. Different methods suit different scales, terrains, and water sources. This capability covers gravity-fed channels, furrow irrigation, basin flooding, water-lifting devices (shaduf, Archimedes screw, saqiya), and low-pressure drip systems. It does not cover pumps powered by electric motors or internal combustion engines — those belong to [Water → Distribution](../water/distribution.md).

Position in the dependency chain: irrigation requires [Water Procurement](../water/procurement.md) (a water source and basic collection infrastructure) and builds on [Foundations → Agriculture](../foundations/food-agriculture.md) (basic cultivation knowledge). It enables reliable [Food Processing](../food-processing/index.md) by guaranteeing crop yields and supports [Soil Management](soil-management.md) by providing the water needed for cover crop establishment and compost activation.

## Prerequisites

**Materials**:
- Water source (river, stream, spring, well, or reservoir) with reliable minimum flow
- Earth, clay, or stone for canal and channel construction
- Wood for water-lifting devices (shaduf, scoop wheels, Archimedes screw)
- Fiber cordage or rope for bucket-and-pulley systems
- Clay or fired pipe for small-scale conveyance (optional, improves efficiency)

**Tools and equipment**:
- [Digging sticks and hoes](../foundations/tools-basic.md) for earth-moving
- [Shovels](../foundations/tools-basic.md) (wooden or iron) for canal excavation
- [Carpentry tools](../foundations/tools-basic.md) for water-lifting device construction
- [Clay pots](../ceramics/pottery.md) or buckets for water transport
- [Rope and cordage](../textiles/fibers.md) for lifting mechanisms

**Knowledge**:
- Surveying: estimating slope by eye or with a water level (two stakes and a filled hose or channel)
- Soil permeability assessment (dig a test pit, fill with water, measure infiltration rate)
- Crop water requirements by growth stage
- Seasonal water availability patterns

**Infrastructure**:
- Cleared and graded land suitable for canal or furrow construction
- Access to water source with legal/social allocation (water rights, communal scheduling)


## Gravity Canal System (1 km canal, 50 L/sec capacity)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Excavated earth | 200-500 m³ | On-site digging | Stone-lined channel (longer life, more labor) |
| Clay sealant (if sandy soil) | 50-100 m³ | Local clay deposit | Compacted earth liner, bentonite if available |
| Stone for intake structure | 5-20 tonnes | Local quarry or field stone | Timber weir (shorter life, 5-10 years) |
| Wood for sluice gates | 2-4 gates, 1×1.5 m each | [Tools → Woodworking](../foundations/tools-basic.md) | Stone gates with sliding grooves |
| Gravel for canal bed (anti-erosion) | 20-50 tonnes | River gravel | Compacted clay base |
| Labor for construction | 200-500 person-days | Community labor | Draft animal assistance for earth-moving |

## Shaduf (Single Water-Lifting Device)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Wooden beam (lever arm) | 3-4 m, 10-15 cm diameter | [Tools → Woodworking](../foundations/tools-basic.md) | Bamboo bundle |
| Counterweight (stone or clay) | 30-60 kg | Local stone | Earthen jar filled with sand |
| Bucket or skin bag | 10-20 L capacity | [Ceramics](../ceramics/pottery.md) or animal hide | Woven basket with clay lining |
| Fiber rope | 3-5 m | [Textiles → Fibers](../textiles/fibers.md) | Leather thong |
| Pivot post | 1.5-2 m wooden post | Local timber | Stone pillar with notch |
| Stone foundation | 100-200 kg | Field stone | Compacted earth pad |

## Low-Pressure Drip System (1 Hectare, Clay Pipe)

| Material | Quantity per Hectare | Source | Alternatives |
|----------|---------------------|--------|-------------|
| Clay pipes (10 cm diameter) | 500-1,000 m length | [Ceramics](../ceramics/pottery.md) | Bamboo tubes with drilled holes |
| Distribution headers (15 cm diameter) | 100-200 m | [Ceramics](../ceramics/pottery.md) | Hollowed logs |
| Filter screen (coarse cloth) | 2-4 m² | [Textiles](../textiles/fibers.md) | Sand filter box at intake |
| Emitters (perforated clay plugs) | 2,000-5,000 units | [Ceramics](../ceramics/pottery.md) | Small holes drilled in bamboo |
| Gravel for bed preparation | 5-10 m³ | River gravel | Sand base |


## Gravity Canal Construction

1. **Survey the route**: Walk the path from water source to field. Use a water level (two stakes 5-10 m apart, connect with water-filled channel or hose) to establish a consistent gradient of 0.1-0.5% (10-50 cm drop per 100 m). Too steep: water erodes the canal bed. Too flat: water pools, silts up, flow slows.
2. **Mark the alignment**: Drive stakes every 5-10 m along the planned canal center-line. Connect with string. The canal follows the contour, not the straight line — contour following minimizes earth-moving.
3. **Excavate the intake**: At the river or stream, build a simple diversion weir. Pile stone across part of the stream channel, 30-50 cm high, angled 30-45° to the flow. The weir raises water level enough to spill into the canal intake. Leave a gap at the downstream end for fish passage and flood overflow.
4. **Dig the canal**: Excavate a trapezoidal channel: bottom width 30-50 cm, top width 50-80 cm, depth 30-50 cm. Pile excavated earth on the downhill side to form a levee. Compact the canal bed and sides by tamping with wooden block or driving livestock along the wetted surface.
5. **Install sluice gates**: At 100-200 m intervals, insert wooden or stone gates into grooves cut into the canal walls. Gates control flow distribution to different field sections. A simple sliding gate: a flat board that drops into a slot across the canal.
6. **Seal leaks**: If the soil is sandy or gravelly, line the canal with puddled clay (clay mixed with water to a plastic consistency, smeared 5-10 cm thick on the canal bed and sides). Compact thoroughly. A well-sealed earthen canal loses 10-20% of flow to seepage; an unlined sandy canal loses 40-60%.
7. **Test the flow**: Open the intake and observe water movement. Flow should be steady, not turbulent. If water backs up at any point, the gradient is insufficient — re-dig that section deeper. If erosion occurs at any point, widen the canal or reduce the gradient.

**Strengths**:
- Gravity-fed operation requires no energy input after construction — water flows continuously without pumps or fuel
- Canal systems serve multiple users — a single 1 km canal can irrigate 10-40 hectares
- Construction uses locally available materials (earth, clay, stone) with hand tools

**Weaknesses**:
- Requires precise gradient control (0.1-0.5%) — surveying errors cause silting or erosion
- Annual de-silting costs 20-50 person-days per km of canal in silty water regions
- Unlined sandy canals lose 40-60% of water to seepage; clay lining requires 50-100 m³ per km

## Furrow Irrigation

1. **Prepare the field**: Plow or hoe the field into raised beds (beds) and channels (furrows). Bed width: 60-100 cm. Furrow depth: 15-25 cm. Furrow spacing: matched to crop row spacing.
2. **Set the siphon or gate**: At the head of each furrow, install a small gate (wooden slide) or use a siphon (clay tube over the field boundary) to control flow into each furrow.
3. **Apply water**: Open the head gate and allow water to flow down the furrow. Target flow rate: 0.5-2.0 L/sec per furrow. Water should reach the end of the furrow in 30-60 minutes for most soils.
4. **Monitor infiltration**: After water reaches the furrow end, close the gate. The water in the furrow infiltrates into the soil over 1-6 hours depending on soil type. Clay soils absorb slowly; sandy soils absorb rapidly.
5. **Repeat as needed**: Irrigate when the top 15-20 cm of soil feels dry to the touch. Typical frequency: every 3-7 days in dry season, every 7-14 days in moderate climate.

**Strengths**:
- 50-70% application efficiency — better than flood irrigation with less water waste
- Simple to implement — plow or hoe is the only tool needed for bed and furrow preparation
- Compatible with gravity canal systems — no pump or pressurization required

**Weaknesses**:
- Labor-intensive — 3-6 person-hours per hectare per irrigation event for gate management
- Uneven water distribution on sloped or uneven fields without precise leveling
- Furrow erosion on sandy soils at gradients above 0.5% — limits use on steep terrain

## Water-Lifting with a Shaduf

1. **Set up the shaduf**: Mount the lever beam on the pivot post so the bucket end is longer than the counterweight end (ratio 3:1 to 5:1). Attach the bucket to the long end and the counterweight to the short end.
2. **Fill the bucket**: Pull the bucket end down to the water source (river, canal, or well). The counterweight assists the pull. Submerge the bucket to fill — allow 10-20 liters.
3. **Lift and swing**: Release tension. The counterweight swings the bucket upward. Guide the bucket over the irrigation channel or field.
4. **Dump the water**: Tip the bucket by pulling a release cord or rotating the handle. Water flows into the distribution channel.
5. **Cycle rate**: An experienced operator lifts 10-15 buckets per minute. At 15 L per bucket: 150-225 L/min, or 9,000-13,500 L/hour. One shaduf can irrigate 0.1-0.2 hectares per day.

**Strengths**:
- Simplest water-lifting device — can be built in 2-4 hours from a wooden beam, rope, bucket, and counterweight
- Counterweight makes lifting easy — a 15 L bucket feels like 3-5 kg of effort with a 3:1 ratio
- No energy source required beyond human labor — operates without electricity, fuel, or animal power

**Weaknesses**:
- Limited lift height of 1-3 m — cannot draw from deep wells
- Sustained operation is physically taxing — 6-8 hours of shaduf operation causes shoulder and back strain
- Single operator irrigates only 0.1-0.2 ha per day — insufficient for fields larger than 1 ha without multiple devices

## Archimedes Screw Operation

1. **Build the screw**: Construct a helical blade inside a wooden or metal cylinder, 20-40 cm diameter, 2-5 m long. The cylinder sits in a trough or pipe at 30-45° angle from horizontal. Blade pitch: 15-25 cm between turns.
2. **Install at the water source**: Place the lower end submerged in the water source. The upper end empties into an irrigation channel or reservoir.
3. **Turn the screw**: Rotate the screw by hand crank, foot treadle, or animal gear. Each rotation lifts a pocket of water one blade-pitch up the incline.
4. **Flow rate**: A 30 cm diameter screw turning at 40-60 RPM lifts 5-15 L/sec through 1-3 m of head. Two operators can sustain this output for several hours.
5. **Maintenance**: Check the cylinder seal (gap between blade and casing should be <5 mm). Large gaps allow backflow and reduce efficiency. Re-line the trough with clay or replace leather seals as needed.

**Strengths**:
- Moves 5-15 L/sec through 1-3 m of head — 3-10× the output of a shaduf
- Can be powered by hand crank, foot treadle, or animal gear — flexible energy sources
- Handles muddy or debris-laden water without clogging — suitable for river water with suspended sediment

**Weaknesses**:
- Construction requires precise helical blade fabrication — more complex than a shaduf (10-20 hours of carpentry)
- Blade-to-casing gap of >5 mm causes 20-40% efficiency loss — regular adjustment needed
- Limited to lifts of 1-5 m — deeper wells require Persian wheel or bucket chain systems


## Crop Water Requirements by Growth Stage

| Crop | Total Season (mm) | Establishment (mm/day) | Vegetative (mm/day) | Flowering (mm/day) | Grain Fill (mm/day) |
|------|-------------------|----------------------|--------------------|--------------------|--------------------|
| Wheat | 450-650 | 2-3 | 3-5 | 5-7 | 3-5 |
| Rice (paddy) | 1,000-1,500 | 5-7 | 6-8 | 8-10 | 6-8 |
| Maize | 500-800 | 3-4 | 4-6 | 6-8 | 4-6 |
| Barley | 350-500 | 2-3 | 3-5 | 5-6 | 3-4 |
| Vegetables (mixed) | 400-600 | 3-4 | 4-6 | 5-7 | 4-5 |
| Cotton | 600-1,000 | 2-3 | 4-6 | 7-9 | 3-5 |

## Water-Lifting Device Comparison

| Device | Maximum Lift (m) | Flow Rate (L/hr) | Operators Required | Energy Source | Construction Complexity |
|--------|------------------|-------------------|--------------------|--------------|-----------------------|
| Shaduf | 1-3 | 5,000-15,000 | 1 | Human | Low |
| Bucket chain (manual) | 2-5 | 5,000-15,000 | 6-10 | Human | Low-Medium |
| Archimedes screw | 1-5 | 10,000-55,000 | 1-2 | Human | Medium |
| Saqiya (animal-powered) | 3-10 | 30,000-110,000 | 1 animal + 1 person | Animal | Medium-High |
| Persian wheel (animal) | 5-15 | 15,000-50,000 | 1 animal + 1 person | Animal | Medium |
| Counterpoise lift | 1-2 | 3,000-8,000 | 1 | Human | Low |

## Canal Flow Rates by Channel Dimensions

| Channel Width × Depth (cm) | Gradient (%) | Flow Rate (L/sec) | Hectares Served |
|----------------------------|-------------|-------------------|-----------------|
| 20 × 15 | 0.2 | 8-12 | 2-4 |
| 30 × 20 | 0.2 | 15-25 | 5-8 |
| 40 × 30 | 0.2 | 30-50 | 10-16 |
| 50 × 40 | 0.15 | 50-80 | 16-25 |
| 60 × 50 | 0.1 | 80-120 | 25-40 |

Flow estimates assume earthen canal with Manning's roughness coefficient n ≈ 0.025-0.035. Lined canals (clay, stone) carry 15-30% more water at the same gradient.

## Irrigation Application Efficiency by Method

| Method | Application Efficiency | Labor per Hectare per Irrigation | Water Loss (Evaporation + Runoff) | Suitable Soil Types |
|--------|----------------------|--------------------------------|-----------------------------------|--------------------|
| Flood/basin | 40-60% | 2-4 person-hours | 40-60% | Heavy clay, leveled land |
| Furrow | 50-70% | 3-6 person-hours | 30-50% | Most soils |
| Border strip | 50-65% | 2-4 person-hours | 35-50% | Medium texture, leveled |
| Drip (clay pipe) | 70-90% | 1-2 person-hours (once installed) | 10-30% | All soils |
| Sprinkler (pressurized) | 65-80% | 0.5-1 person-hours | 20-35% | All soils |

## Head Loss in Earthen Canals

| Parameter | Typical Value | Impact |
|-----------|--------------|--------|
| Seepage loss | 10-60% per km (unlined) | Major — line canals in sandy soil |
| Seepage loss | 5-15% per km (clay-lined) | Acceptable for most applications |
| Evaporation loss | 2-5% per km in hot, arid climate | Minor compared to seepage |
| Siltation rate | 5-20 cm depth per year (murky water) | Requires annual de-silting |
| Vegetation obstruction | 10-30% flow reduction if unmanaged | Clear weeds monthly during irrigation season |

## Scaling Notes

**Individual garden (0.05-0.2 ha)**: Hand-watering with buckets or clay pots directly from a well or river. Daily labor: 1-2 hours. No infrastructure required beyond the water source. Suitable for household vegetable gardens. Yield improvement over rain-fed: 50-100%.

**Small field (0.5-2 ha)**: Furrow irrigation fed by a short canal (50-200 m) from a nearby water source, or one or two shadufs lifting from a well or river. Construction labor: 20-50 person-days. One full-time irrigator during dry season. This is the scale at which irrigation becomes a distinct labor role.

**Village system (5-20 ha)**: Permanent canal network 0.5-3 km in length, with intake structure, distribution gates, and communal maintenance schedule. Requires coordinated labor for construction (200-1,000 person-days) and ongoing maintenance (canal clearing, gate repair). Supports 30-80 families. Water allocation scheduling (which fields get water on which days) becomes a governance function.

**Regional system (50+ ha)**: Large canal networks 5-20 km long, potentially with multiple water sources and intermediate reservoirs. Requires [Machine Tools](../machine-tools/machining.md)-level engineering for weirs, gates, and measuring structures. Enables agriculture in arid regions that would otherwise be desert. This is the scale of historical Mesopotamian and Egyptian irrigation systems that supported the first cities.

**Key bottleneck**: Siltation. Every canal silts up. Without annual de-silting (clearing accumulated sediment), flow capacity drops 20-40% per year. De-silting is the single largest maintenance cost of any gravity canal system.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Canal flow rate declining | Siltation, vegetation growth, or bank erosion narrowing the channel | De-silt annually (dig out accumulated sediment); clear weeds and roots monthly; repair eroded banks with compacted earth |
| Water not reaching end of furrow | Insufficient flow, soil too permeable, or furrow too long | Increase flow rate (widen canal or add shaduf); shorten furrows to 50-80 m for sandy soil; add clay to furrow bottom |
| Waterlogging in lower fields | Excess water application, poor drainage, or perched water table | Reduce irrigation frequency; dig drainage ditches between fields; plant water-tolerant crops in low spots |
| Salinity buildup in soil | Irrigation water contains dissolved salts; evaporation concentrates salts at surface | Apply extra water (leaching fraction of 10-20%) to flush salts below root zone; improve drainage; switch to drip irrigation to reduce evaporation |
| Shaduf rope breaking | Wear from repeated flexing and moisture exposure | Inspect daily; replace every 2-4 weeks in heavy use; use natural fiber rope at minimum 15 mm diameter |
| Canal bank breach | Erosion from high flow, animal damage, or root penetration | Reduce flow rate immediately; plug breach with clay and compact; reinforce with stone or timber; fence canal from livestock |
| Uneven water distribution | Canal gradient not uniform; some furrows steeper than others | Re-survey and re-grade canal; install flow dividers at distribution points; adjust individual furrow gates |
| Algae blocking emitters (drip system) | Sunlight on water in pipes promotes algal growth | Cover header pipes with earth or black cloth; install coarse filter at intake; flush lines weekly |

## Safety

- **Drowning hazard**: Canals and reservoirs with steep banks and murky water. Children and non-swimmers are at highest risk. Fence canal crossings near settlements. Mark deep sections. Never work alone near deep water.
- **Waterborne disease**: Irrigation water from rivers or open canals may carry pathogens (E. coli, Giardia, Schistosoma). Do not drink irrigation water without treatment (see [Water → Basic Treatment](../water/basic-treatment.md)). Wear boots in flooded fields — schistosomiasis and leptospirosis infect through skin contact with contaminated water.
- **Structural failure**: Canal banks, weirs, and sluice gates can fail under flood conditions. Inspect after every heavy rain. Do not camp or store valuables downstream of canal embankments. Design spillways to handle 2× normal peak flow.
- **Malaria and mosquito-borne disease**: Standing water in canals and flooded fields breeds mosquitoes. Drain standing water within 5-7 days. Stock fish in permanent canal sections to eat larvae. Clear vegetation from canal edges where mosquitoes rest.
- **Physical injury from water-lifting devices**: Shaduf and scoop wheel mechanisms have moving parts that pinch fingers and strike heads. Keep clothing and hair clear of rotating shafts. Maintain wooden pivots — worn pivots cause sudden drops.
- **Hypothermia**: Working in flooded fields in cold weather. Water conducts heat 25× faster than air. Limit exposure to cold irrigation water to 2-3 hours maximum. Wear waterproof boots and change wet clothes promptly.


## Canal Flow Verification

| Parameter | Acceptable Range | Test Method |
|-----------|-----------------|-------------|
| Canal gradient | 0.1-0.5% | Water level between two stakes 20 m apart: 2-10 cm difference |
| Flow velocity | 0.3-1.0 m/sec (earthen canal) | Float a stick 10 m: should take 10-33 seconds |
| Seepage loss | <15% per km (lined canal) | Measure flow at intake and 1 km downstream; difference <15% |
| Silt depth | <10 cm accumulated | Probe canal bed with marked stick at 50 m intervals |
| Gate seal leakage | <5% of flow when closed | Visual: no visible water passing closed gate |

## Irrigation Application Check

| Parameter | Target | Test Method |
|-----------|--------|-------------|
| Soil moisture after irrigation | Field capacity (20-35% by volume for most soils) | Squeeze test: soil forms ball, no water drips |
| Wetting depth | 30-60 cm below surface | Push a steel rod into soil — it stops at dry layer |
| Distribution uniformity | >75% (ratio of minimum to maximum infiltration) | Measure soil moisture at 5+ points across the field 24 hours after irrigation |
| Salinity (if applicable) | <4 dS/m in root zone (salt-sensitive crops) | Taste test: salty taste indicates problem; confirm with conductivity meter when available |


## Irrigation Method Selection by Situation

| Situation | Recommended Method | Why |
|-----------|-------------------|-----|
| River valley, flat terrain, clay soil | Basin flooding | Simple, low infrastructure, clay holds water well |
| River valley, flat terrain, sandy/loam soil | Furrow irrigation | Less water wasted than flooding, good control |
| Hillside terrain with spring above | Contour canal + furrow | Gravity-fed, no lifting required |
| Well, 3-10 m depth, moderate area | Saqiya or Persian wheel | Animal power provides sustained output |
| Well, 1-3 m depth, small area | Shaduf | Simplest device for this lift range |
| Arid climate, limited water | Clay-pipe drip | Highest water-use efficiency, reduces evaporation |
| Rice paddy | Controlled flooding with bunds | Rice requires continuous shallow flooding |
| Seasonally waterlogged lowland | Raised beds with drainage channels | Combines drainage and irrigation in one system |

## Regional Historical Systems

- **Mesopotamian canal networks** (3000 BCE+): Canals 10-30 km long diverting Tigris/Euphrates water. Supported the first urban civilization. Required centralized labor organization for construction and de-silting — irrigation and state formation were inseparable.
- **Egyptian basin irrigation** (Nile flood): Low basins (1-2 m deep, 500-5,000 hectares each) flooded annually by the Nile inundation. No lifting required — the river did the work. Supported dense populations for millennia with minimal technology.
- **Qanat systems** (Persia, 1000 BCE+): Gently sloping underground tunnels carrying water from aquifer outcrops on mountain slopes to surface fields 5-30 km away. Eliminated evaporation losses. Construction required precise surveying over long distances. Still operational in Iran today.
- **Chinampas** (Aztec, Lake Texcoco): Lake-based raised beds irrigated by capillary rise from surrounding water. No canals or lifting needed. Extremely productive (up to 7 harvests/year).

## Water Conservation Strategies

| Strategy | Water Saved | Trade-off |
|----------|------------|-----------|
| Night irrigation (reduce evaporation) | 15-25% | Requires nighttime labor or automation |
| Mulching between rows (reduce soil evaporation) | 10-30% | Labor to apply mulch; may harbor pests |
| Clay-lined canals (reduce seepage) | 20-40% of canal losses | Upfront labor investment |
| Drip vs. flood (reduce total application) | 30-50% | Higher infrastructure cost, more maintenance |
| deficit irrigation (apply less than full ET) | 20-40% | 10-30% yield reduction; acceptable for some crops |

## See Also

- [Foundations → Agriculture & Food Production](../foundations/food-agriculture.md) — basic cultivation, grain yields, food preservation
- [Water → Procurement](../water/procurement.md) — water sources, well digging, spring capture
- [Water → Distribution](../water/distribution.md) — pressurized pipe systems, pumps, municipal water
- [Water → Basic Treatment](../water/basic-treatment.md) — filtration, sedimentation, pathogen removal
- [Agriculture → Soil Management](soil-management.md) — soil fertility, composting, salinity management
- [Food Processing](../food-processing/index.md) — downstream processing of irrigated crops
- [Ceramics → Pottery](../ceramics/pottery.md) — clay pipes, vessels, and irrigation components
- [Foundations → Stone & Wood Tools](../foundations/tools-basic.md) — digging sticks, hoes, wooden construction
- [Textiles → Fibers](../textiles/fibers.md) — rope and cordage for lifting devices



[← Back to Agriculture](index.md)
