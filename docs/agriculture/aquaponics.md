# Aquaponics

> **Node ID**: agriculture.aquaponics
> **Domain**: [Agriculture](./index.md)
> **Dependencies**: [`agriculture`](./index.md), [`animals.aquaculture`](../animals/aquaculture.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Enables**: [`agriculture.hydroponic-ph-control`](sem-tech-hydroponics.md), [`food-processing`](../food-processing/index.md)
> **Timeline**: Years 3-10+
> **Outputs**: fish, vegetables, herbs, filtered_water
> **Critical**: No — aquaponics provides high-density integrated food production but is not the only path to reliable agriculture; conventional soil-based farming and separate aquaculture are viable alternatives


Aquaponics is an integrated food production system that combines fish farming (aquaculture) with soil-less plant cultivation in a single recirculating water loop. Fish produce ammonia-rich waste; bacteria convert that ammonia to nitrate; plants absorb the nitrate as fertilizer; the cleaned water returns to the fish tank. The result is two crops (fish and plants) from one water input, with the plants serving as the water filtration system for the fish and the fish providing free fertilizer for the plants.

Aquaponics is a **lower-technology** approach than chemical hydroponic systems. Where hydroponics requires precise chemical pH adjustment (adding phosphoric acid or potassium hydroxide), aquaponics achieves pH stability through natural biological buffering — calcium carbonate from crushed shells, bones, or limestone dissolves slowly to maintain pH in the 6.5-7.0 range. The nitrogen cycle is driven entirely by naturally occurring bacteria. No chemical inputs are needed for the core system beyond fish food and supplemental minerals (iron, calcium, potassium) that fish food does not provide in sufficient quantity. The more advanced [hydroponic pH control](./sem-tech-hydroponics.md) systems, which use electromembrane electrodialysis for ion-by-ion nutrient management, build upon the principles established by aquaponics but require substantially more industrial infrastructure.

A small aquaponic system — a 500-1000 L fish tank, a 1-2 m² grow bed, an air pump, and a water pump — produces 20-40 kg of fish and 30-60 kg of vegetables per year in a footprint of 3-4 m².

Position in the dependency chain: aquaponics depends on [Aquaculture](../animals/aquaculture.md) (fish farming knowledge) and [Agriculture](./index.md) (plant cultivation). It enables the more advanced [SEM Tech Hydroponics](./sem-tech-hydroponics.md) systems and supports [Food Processing](../food-processing/index.md) with consistent fish and vegetable harvests.

## Prerequisites

**Materials**:
- Fish tank (500-1000 L for household system): food-grade polyethylene, or concrete/brick tank lined with pond liner
- Grow bed containers: watertight boxes, tubs, or custom-built beds (25-30 cm depth)
- Growing media: gravel (10-20 mm, washed), expanded clay pebbles, or lava rock
- PVC pipes, connectors, and valves for water circulation
- Submersible water pump rated at 1000-2000 L/hr for 1000 L system
- Air pump + airstones (5-10 L/min rating)
- Fish: tilapia, carp, or catfish fingerlings (see [Aquaculture](../animals/aquaculture.md))
- Fish food: commercial pellets, BSF larvae, or duckweed (see [Insect Farming](../animals/insect-farming.md))

**Tools and equipment**:
- [Carpentry tools](../foundations/tools-basic.md) for grow bed and frame construction
- [PVC cutting and joining tools](../foundations/tools-basic.md) for plumbing
- [Ceramics](../ceramics/pottery.md) or plastic containers for sump and filter
- Water test kit (ammonia, nitrite, nitrate, pH) — liquid reagent or test strips
- Thermometer for water temperature monitoring

**Knowledge**:
- Nitrogen cycle (ammonia → nitrite → nitrate) and bacterial colonization requirements
- Fish health assessment (gill color, swimming behavior, feeding response)
- Water chemistry: pH, ammonia, nitrite, nitrate testing and interpretation
- Bell siphon construction and flood-and-drain cycling

**Infrastructure**:
- Reliable electricity supply (solar + battery, wind, or grid) for continuous pump and aerator operation
- Sheltered location (greenhouse, indoor room, or covered area) for temperature control
- Water source for initial fill and make-up water (see [Water Procurement](../water/procurement.md))

## Bill of Materials

## Household Aquaponic System (1000 L fish tank)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Fish tank (500-1000 L) | 1 | [Ceramics](../ceramics/pottery.md), polyethylene tank, or concrete | IBC tote, stock tank |
| Grow bed container (25-30 cm deep) | 1-2 (total 500-1000 L volume) | [Tools → Woodworking](../foundations/tools-basic.md) with pond liner | Plastic tubs, concrete boxes |
| Growing media (gravel 10-20 mm) | 200-400 L | Local quarry or river gravel | Expanded clay (hydroton), lava rock |
| Submersible water pump (1000-2000 L/hr) | 1 | [Electronics](../electronics/index.md) or commercial | Hand pump (labor-intensive) |
| Air pump (5-10 L/min) + airstones | 1 | [Electronics](../electronics/index.md) or commercial | Bellows aerator (manual) |
| PVC pipes and fittings (25-50 mm) | 5-10 m | [Chemistry → PVC](../chemistry/index.md) or plumbing supply | Bamboo tubes, rubber hose |
| Bell siphon components (PVC pipes) | 1 set | Plumbing supply | Hand-drilled holes with manual drain |
| Fish fingerlings | 20-50 | [Aquaculture](../animals/aquaculture.md) | Wild-caught (disease risk) |
| Water test kit (ammonia, nitrite, nitrate, pH) | 1 | Chemical supply | Visual observation (less precise) |

## Supplemental Mineral Amendments

| Material | Quantity | Purpose | Source |
|----------|----------|---------|--------|
| Crushed eggshells or oyster shells | 500 g-2 kg | Calcium supplement + pH buffer | Kitchen waste, coastal collection |
| Wood ash | 100-200 g per 100 L weekly | Potassium supplement | [Fire-Making](../foundations/fire.md) |
| Chelated iron (iron DTPA) | 2-5 mg/L every 2-4 weeks | Iron supplement (prevents chlorosis) | [Chemistry](../chemistry/index.md) or commercial |

## Process Description

## System Design and Assembly

**Fish tank**: 500-1000 L for a household system. Food-grade polyethylene tank, or a concrete/brick tank lined with pond liner or waterproofed with cement render. Opaque or dark-colored to reduce algae growth. Minimum depth 40-60 cm. Located at or below the level of the grow beds to allow gravity drain-back.

**Grow beds** (plant cultivation area):
The grow bed to fish tank volume ratio should be 1:1 to 2:1. For a 500 L fish tank, plan 500-1000 L of grow bed volume. Three design approaches:

1. **Media-based grow bed** (simplest, recommended for beginners):
   A container filled with inert growing media — gravel (10-20 mm diameter, washed), expanded clay pebbles (hydroton), or lava rock. Media provides root support and surface area for beneficial bacteria. Flood and drain cycle: fill the bed with fish water, then drain it back (using a bell siphon or timed pump). Container depth 25-30 cm. Media size 10-20 mm. Avoid limestone gravel (raises pH excessively) and calcareous stone.

2. **NFT (Nutrient Film Technique)**:
   Plants sit in small cups or net pots in horizontal pipes (PVC, 50-100 mm diameter, with holes cut for pots). A thin film of water (1-2 mm deep) flows continuously through the pipe bottom, bathing the dangling roots. More water-efficient and lighter than media beds. Requires a solids filter before the NFT pipes because fish solids clog the narrow channels.

3. **DWC (Deep Water Culture / Raft system)**:
   Plants float on polystyrene rafts on a tank of water 20-30 cm deep, with roots dangling directly into the aerated water. No media needed. Requires a solids filter and biofilter (separate container with bio-media).

**Water pump**: Submersible pump in the fish tank, rated to cycle the total water volume 1-2 times per hour. For a 1000 L system, a pump rated at 1000-2000 L/hr. Pumps require electricity (solar panel + battery, wind generator, or grid power).

**Air pump + airstones**: Continuous aeration is essential. Dissolved oxygen must remain above 5 mg/L at all times for fish health.

**Bell siphon** (for media beds): The key mechanism for flood-and-drain cycling. No moving parts, no timer, no electricity for the drain cycle itself.

Construction:
- **Standpipe**: Vertical PVC pipe (25-32 mm diameter) set in the bottom of the grow bed, rising to the desired flood level (approximately 25 cm).
- **Bell**: A wider pipe (50-75 mm diameter, 5-10 cm taller than the standpipe) with a sealed cap on top, placed over the standpipe. Small holes (3-5 mm) drilled near the bottom.
- **Media guard**: A perforated pipe or cylinder around the bell, preventing gravel from entering the siphon.

Cycle: Water fills the grow bed to the top of the standpipe. The bell siphon triggers and drains the bed rapidly (2-5 minutes). The siphon breaks when air enters. The cycle repeats 3-4 times per hour.

**Strengths**:
- Media-based system requires no separate biofilter — the gravel media provides bacterial surface area
- Bell siphon operates without moving parts or timers — reliable and maintenance-free
- Single water pump and air pump are the only powered components — low energy demand (50-100W)

**Weaknesses**:
- System requires continuous electricity — pump failure kills fish within 1-2 hours in warm water
- Gravel media (200-400 L) is heavy — grow beds weigh 300-600 kg when full and must be supported
- PVC plumbing requires precise fitting — leaks cause water loss and can drain the fish tank

## Nitrogen Cycle Establishment

Aquaponics depends on the nitrogen cycle — bacteria convert toxic fish waste into plant-available nutrients. This cycle must be established before adding fish.

**Step 1 — Ammonia (NH₃/NH₄⁺)**:
Fish excrete ammonia through their gills and in their waste. Ammonia is highly toxic to fish — concentrations above 1 mg/L cause stress, and above 2-3 mg/L are lethal.

**Step 2 — Nitrite (NO₂⁻)**:
*Nitrosomonas* bacteria oxidize ammonia to nitrite. Nitrite is also toxic to fish — it binds to hemoglobin and prevents oxygen transport (brown blood disease). Concentrations above 1 mg/L are dangerous.

**Step 3 — Nitrate (NO₃⁻)**:
*Nitrobacter* bacteria oxidize nitrite to nitrate. Nitrate is relatively non-toxic to fish (tolerated at 100-200 mg/L) and is the primary form of nitrogen that plants absorb.

**System cycling** (establishing the nitrogen cycle):
Before adding fish, the system must develop sufficient bacterial colonies to process waste. This takes 4-6 weeks.

1. Fill system with dechlorinated water. Run pump and aerator continuously.
2. Add an ammonia source: pure ammonia (ammonium hydroxide, 3-5 mg/L concentration) or a small amount of fish food (which decomposes to release ammonia). Alternatively, add inoculant bacteria from an established aquarium or pond.
3. Test water daily using test kits:
   - Week 1-2: Ammonia rises, then begins to fall as *Nitrosomonas* colonize.
   - Week 2-3: Nitrite rises (ammonia is being converted). This is the "nitrite spike" — the highest-risk period.
   - Week 3-4: Nitrite begins to fall as *Nitrobacter* colonize. Nitrate appears.
   - Week 4-6: Ammonia and nitrite both read near zero within 24 hours of adding ammonia.
4. When ammonia and nitrite remain at zero 24 hours after adding ammonia, the system is cycled and ready for fish.

**Temperature and cycling**: Bacterial activity doubles for every 10°C increase (within the range 10-35°C). Systems cycle faster at 25-30°C than at 15-20°C. Below 10°C, cycling slows dramatically.

**Strengths**:
- Once established, the nitrogen cycle is self-sustaining — bacteria reproduce to match the ammonia load
- Inoculant from an established aquarium or pond can reduce cycling time from 4-6 weeks to 2-3 weeks
- The nitrogen cycle requires no chemical inputs — bacteria, ammonia, and oxygen are all that is needed

**Weaknesses**:
- 4-6 week cycling period before any fish can be added — delays system startup significantly
- Nitrite spike during weeks 2-3 is toxic to fish — any fish added prematurely will die
- Bacterial colonies crash if the pump stops for more than 4-6 hours (bacteria suffocate without oxygenated water flow)

## Fish Management

### Tilapia (*Oreochromis* spp.)

The standard aquaponics fish. Fast growth (500 g in 6-8 months under optimal conditions), tolerate crowding (20-40 kg/m³), omnivorous (accept plant-based and insect-based feeds), and thrive at 26-30°C. Tolerate pH 6.0-9.0. Breeding is prolific — mouthbrooding females produce 100-500 fry per spawn.

Feed: 2-3% body weight per day at optimal temperature. Accept BSF larvae (see [Insect Farming](../animals/insect-farming.md)), duckweed, algae, commercial pellets, agricultural byproducts (rice bran, oilseed cake). Protein requirement: 28-35% for optimal growth.

### Carp (*Cyprinus carpio*)

Cold-hardy alternative to tilapia. Tolerate 4-35°C, optimal growth at 20-28°C. Accept lower water quality than tilapia. Omnivorous. Growth to 500 g-1 kg in one season with adequate feeding. Suitable for unheated outdoor systems in temperate climates.

### Catfish (various species)

Tolerate low dissolved oxygen (some species have accessory air-breathing organs), turbid water, and crowding. Optimal 24-28°C. Growth to 500 g in 4-6 months. Accept animal-based feeds (BSF larvae, fish meal, blood meal). Suitable where water quality management is less precise.

### Stocking Density

- **Conservative** (low-risk, recommended): 20 kg of fish per cubic meter of water (20 kg/m³). For a 1000 L tank, stock a maximum of 20 kg total fish weight.
- **Moderate**: 30 kg/m³. Requires excellent water quality management and reliable aeration.
- **Intensive**: 40 kg/m³ and above. Requires continuous monitoring, backup systems, and experienced management. High risk of catastrophic loss from equipment failure.

Start conservative. Stock at 10-15 kg/m³ when fish are small and increase as the biofilter matures.

**Feeding**: Feed 2-3% of total fish body weight per day, split into 2-3 feedings. A system with 20 kg of tilapia receives 400-600 g of feed per day.

**Feeding rule**: Fish should consume all feed within 15 minutes. If feed remains after 15 minutes, reduce the ration. Uneaten feed decomposes to ammonia, degrading water quality.

**Strengths**:
- Tilapia reach harvest size (400-500 g) in 6-8 months — 2-3 crops per year with staggered stocking
- Multiple fish species available for different climate zones — tilapia for tropical, carp for temperate, catfish for low-oxygen conditions
- Fish feed can be produced on-site using BSF larvae and duckweed, reducing dependence on commercial pellets

**Weaknesses**:
- Tilapia require warm water (>20°C for growth) — heated water or indoor systems needed in temperate climates, adding energy cost
- Overfeeding is the most common cause of ammonia spikes — 15-minute feeding rule requires daily attention
- Fish disease spreads rapidly in recirculating systems — one sick fish can infect the entire tank within 24-48 hours

## Plant Management

**Excellent aquaponic crops** (leafy greens and herbs — thrive on nitrogen-rich fish water):
- **Lettuce** (all varieties): 4-6 weeks from transplant to harvest. The most reliable aquaponic crop.
- **Spinach**: 4-6 weeks. Prefers cooler temperatures (15-20°C). Bolts in heat.
- **Basil**: 4-6 weeks. High value, strong growth, tolerates warm water.
- **Kale**: 6-8 weeks. Cold-hardy, nutritious, continuous harvest (pick outer leaves).
- **Swiss chard**: 6-8 weeks. Heat-tolerant alternative to spinach.
- **Pak choi / bok choy**: 4-5 weeks. Fast-growing Asian green.
- **Watercress**: Grows directly in water — exceptionally well-suited to DWC systems.
- **Mint**: Aggressive grower — plant in the system to filter water, but contain it (mint will overtake other plants).

**Moderate aquaponic crops** (requires potassium and calcium supplementation):
- **Tomatoes**: 12-16 weeks. Require potassium and calcium supplements.
- **Peppers**: 12-16 weeks. Same supplementation needs as tomatoes.
- **Cucumbers**: 8-12 weeks. Vigorous vines, require trellising.
- **Strawberries**: 12-16 weeks to first harvest. Perennial.

**Potassium and calcium supplementation**:
Fish feed provides nitrogen and phosphorus abundantly, but potassium and calcium are consumed faster than fish waste supplies them.
- **Potassium**: Wood ash (1-2 tablespoons per 100 L system volume weekly), kelp meal, or banana peel extract.
- **Calcium**: Crushed eggshells, crushed oyster shells, or agricultural limestone. Place in a mesh bag in the fish tank or sump — they dissolve slowly, releasing calcium and providing natural pH buffering.
- **Iron**: Chelated iron (iron DTPA or iron EDTA) at 2-5 mg/L, added every 2-4 weeks. Iron deficiency shows as yellowing between leaf veins (interveinal chlorosis) on new growth.

**Strengths**:
- Leafy greens grow 20-30% faster in aquaponics than in soil due to constant nutrient availability
- Continuous harvest possible — pick outer leaves and the plant keeps producing
- No weeding, no soil-borne diseases, and no crop rotation required

**Weaknesses**:
- Fruiting crops (tomatoes, peppers) require supplemental potassium and calcium that fish waste does not provide
- Iron deficiency develops in most systems within 2-3 months without chelated iron supplement
- Root crops and large fruiting trees are unsuitable for aquaponic growing

## Water Quality Management

**pH**: Target: 6.5-7.0. This is a compromise between fish comfort (prefer 7.0-8.0), plant nutrient availability (prefer 5.5-6.5), and bacterial activity (prefer 7.0-8.0).

**Natural buffering**: Calcium carbonate sources (crushed shells, limestone chips) dissolve slowly when pH drops below 7.0, releasing carbonate ions that neutralize acid. When pH rises above 7.5, the carbonate source stops dissolving. This passive self-regulation maintains pH without chemical addition. This is fundamentally different from hydroponic systems, which require regular addition of phosphoric acid or potassium hydroxide (see [SEM Tech Hydroponics](./sem-tech-hydroponics.md)).

**pH drift downward** (most common): Fish and bacterial respiration produces CO₂, which forms carbonic acid. If pH drops below 6.0, add crushed shells or limestone.

**Water Temperature**:
- Tilapia systems: 26-30°C optimal. Below 20°C growth slows. Below 15°C fish stop eating. Below 10°C fish die.
- Carp systems: 20-28°C optimal. Tolerate down to 4°C.
- Trout systems: 10-15°C optimal. Above 20°C stress increases. Above 25°C lethal.

**Dissolved Oxygen**: Maintain above 5 mg/L at all times. Warm water holds less dissolved oxygen: at 30°C, saturation is only 7.5 mg/L; at 10°C, saturation is 11.3 mg/L.

**Ammonia and Nitrite Monitoring**: Test weekly (more frequently during cycling and after disruptions). Acceptable levels:
- Ammonia: below 0.5 mg/L (ideally near zero)
- Nitrite: below 0.5 mg/L (ideally near zero)
- Nitrate: 20-100 mg/L

**Strengths**:
- Natural calcium carbonate buffering maintains pH 6.5-7.0 without chemical inputs
- Once cycled, ammonia and nitrite remain near zero with proper feeding
- Water quality testing uses simple colorimetric kits — no electronic instruments required

**Weaknesses**:
- pH below 6.0 or above 8.0 causes simultaneous stress to fish, plants, and bacteria — narrow operating window
- Dissolved oxygen below 5 mg/L is lethal to fish within hours in warm water — continuous aeration is mandatory
- Ammonia spikes from overfeeding or dead fish can kill an entire tank within 24 hours

## System Startup and Operation

1. **Build the system**: Assemble fish tank, grow bed(s), plumbing, bell siphon, pump, and air pump. Check all connections. Fill with dechlorinated water. Test the bell siphon cycle (fill and drain 3-4 times).
2. **Add bio-media and plant**: Fill grow beds with washed gravel or clay pebbles. Plant seedlings (start with fast-growing plants: lettuce, basil).
3. **Cycle the system** (4-6 weeks): Add ammonia source. Test daily. Wait for ammonia and nitrite to read zero.
4. **Add fish**: Stock at low density (10-15 kg/m³). Acclimate fish to water temperature before release (float transport container in the tank for 30 minutes).
5. **Monitor daily**: Check that pump and aerator are running. Observe fish behavior (listless fish at surface = oxygen or ammonia problem). Test ammonia and nitrite weekly.
6. **Begin harvesting plants**: 4-6 weeks after planting. Harvest outer leaves of leafy greens (continuous production) or whole plants. Replant immediately.
7. **Harvest fish**: When they reach target size (tilapia: 400-500 g at 6-8 months). Remove the largest fish and replace with fingerlings.

**Strengths**:
- Step-by-step startup process is methodical — each phase builds on the previous one
- Lettuce provides visual confirmation that the system is working within 4-6 weeks of planting
- Staggered fish stocking allows continuous harvest once the system is established

**Weaknesses**:
- Total startup time is 6-10 weeks (4-6 weeks cycling + 2-4 weeks plant growth before first harvest)
- System requires daily monitoring (5-10 minutes) — neglect for more than 24 hours can kill fish
- First-time systems commonly lose fish during the learning curve — start with inexpensive fish

## Quantitative Parameters

## Fish Growth Rates in Aquaponics

| Species | Optimal Temperature (°C) | Time to 500 g | Feed Conversion Ratio | Stocking Density (kg/m³) |
|---------|-------------------------|----------------|----------------------|--------------------------|
| Tilapia | 26-30 | 6-8 months | 1.5-2.0 | 20-40 |
| Carp | 20-28 | 8-12 months | 2.0-3.0 | 15-30 |
| Catfish | 24-28 | 4-6 months | 1.8-2.5 | 30-50 |
| Trout | 10-15 | 8-12 months | 1.2-1.5 | 15-25 |

## Aquaponic Crop Yield and Timeline

| Crop | Time to Harvest (weeks) | Yield per m² per Year (kg) | Notes |
|------|------------------------|---------------------------|-------|
| Lettuce | 4-6 | 30-60 | Most reliable aquaponic crop |
| Basil | 4-6 | 20-40 | High value, continuous harvest |
| Spinach | 4-6 | 25-45 | Bolts above 25°C |
| Kale | 6-8 | 20-40 | Continuous outer-leaf harvest |
| Tomatoes | 12-16 | 10-20 | Requires K and Ca supplementation |
| Cucumbers | 8-12 | 15-30 | Requires trellising |

## Aquaponic System Water Budget

| Parameter | Value | Notes |
|-----------|-------|-------|
| Total system volume (household) | 1,000-2,000 L | Fish tank + grow beds + plumbing |
| Daily water loss (evaporation + transpiration) | 5-20 L/day (1-2% of system volume) | Higher in hot, dry climates |
| Daily make-up water needed | 5-20 L/day | Replace evaporation losses |
| Annual water use | 2,000-7,000 L/year | Compare: soil garden uses 50,000-100,000 L/year for same area |
| Water use efficiency vs. soil | 90-95% less water than soil-based growing | Primary advantage of recirculating systems |

## pH, Ammonia, Nitrite, and Nitrate Targets

| Parameter | Target Range | Danger Level | Effect of Deviation |
|-----------|-------------|-------------|-------------------|
| pH | 6.5-7.0 | <6.0 or >8.0 | Low pH kills bacteria; high pH locks up iron |
| Ammonia (NH₃) | <0.5 mg/L (ideally 0) | >2 mg/L | Lethal to fish at 2-3 mg/L |
| Nitrite (NO₂⁻) | <0.5 mg/L (ideally 0) | >1 mg/L | Prevents oxygen transport in fish blood |
| Nitrate (NO₃⁻) | 20-100 mg/L | >150 mg/L | Below 20: insufficient nutrients; above 150: water exchange needed |
| Dissolved oxygen | >5 mg/L | <3 mg/L | Fish die within 1-2 hours below 2 mg/L in warm water |
| Temperature (tilapia) | 26-30°C | <15°C or >33°C | Growth stops below 20°C; death below 10°C or above 35°C |

## Scaling Notes

**Household system (500-1,000 L)**: Single fish tank + 1-2 grow beds. Produces 20-40 kg fish and 30-60 kg vegetables per year in 3-4 m² footprint. Daily maintenance: 5-10 minutes (feeding, visual check). Weekly maintenance: 15-30 minutes (water testing, filter cleaning). Suitable for a family's supplemental protein and greens.

**Multi-tank system (2,000-5,000 L)**: 2-4 fish tanks + 4-8 grow beds. Staggered fish cohorts for continuous harvest. Produces 100-200 kg fish and 150-300 kg vegetables per year. Requires 1-2 hours of daily attention. Suitable for a small community or restaurant supply.

**Commercial system (10,000+ L)**: Multiple tanks with automated monitoring and feeding. Dedicated greenhouse structure. Requires [Water Distribution](../water/distribution.md) infrastructure and backup power systems. Produces 500+ kg fish and 1,000+ kg vegetables per year. Full-time operation.

**Key bottleneck**: Continuous electricity. Pumps and aerators must run 24/7. A power outage exceeding 2-4 hours in warm weather kills fish from oxygen depletion. Solar + battery backup is mandatory for any system in an area with unreliable grid power.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Fish gasping at surface | Low dissolved oxygen or high ammonia | Increase aeration immediately; test ammonia; perform 30-50% water change if ammonia >2 mg/L |
| Ammonia spike (>2 mg/L) | Overfeeding, dead fish, or biofilter crash | Stop feeding; remove dead fish; perform water change; add bacteria inoculant |
| Nitrite spike (>1 mg/L) | Incomplete cycling or biofilter disruption | Add salt (1-3 g/L NaCl — reduces nitrite toxicity); stop feeding for 24 hours; increase aeration |
| Plants yellowing (new growth) | Iron deficiency | Add chelated iron at 2-5 mg/L |
| Plants yellowing (old leaves) | Nitrogen deficiency | Increase fish feeding rate; check that biofilter is processing ammonia to nitrate |
| pH dropping below 6.0 | Carbonic acid accumulation from fish/bacterial respiration | Add crushed shells or limestone; check that buffer material is present in system |
| Green water (algae bloom) | Excess light on fish tank + high nutrients | Cover fish tank to exclude light; reduce feeding; add more plants to consume nutrients |
| Bell siphon not triggering | Clogged with debris or wrong standpipe height | Clean media guard; adjust standpipe height; check for root intrusion |
| Fish not eating | Water temperature too low (tilapia <20°C), or disease | Check temperature; test ammonia and nitrite; observe fish for signs of disease |

## Safety

- **Waterborne disease**: Aquaponic water contains fish waste and bacteria. Do not drink system water. Wash hands after handling fish, grow bed media, or system water. Fish can carry *Salmonella* and *Streptococcus* spp. — maintain good hygiene around the system, especially if children have access.
- **Electrical safety near water**: Water pumps and air pumps operate in and around water. Use ground-fault circuit interrupters (GFCIs) on all electrical outlets near the system. Secure all cables above water level. Do not operate damaged pumps. Solar-powered systems with low-voltage DC pumps (12V) reduce shock risk significantly compared to mains-powered AC pumps.
- **Fish health and water quality**: Ammonia and nitrite spikes kill fish rapidly. Test water regularly, especially in new systems. Never overfeed — excess food is the most common cause of ammonia spikes. Maintain continuous aeration — fish die within 1-2 hours without oxygen in warm water (>25°C). Have a backup aeration plan (battery-powered air pump, or a bucket brigade to splash water for emergency aeration).
- **Heavy metals**: Do not use galvanized metal (zinc-coated) components in the system — zinc is toxic to fish at concentrations as low as 0.1 mg/L. Copper is also toxic to fish (and to invertebrates like shrimp and snails) at concentrations above 0.02 mg/L. Use plastic, stainless steel, or ceramic components for plumbing and fittings. Lead solder in plumbing is a contamination risk — use lead-free connections.
- **Plant food safety**: Fish waste can contain human pathogens if the fish are fed manure or contaminated feed. Use only clean feed sources (commercial pellets, BSF larvae raised on food waste, duckweed from clean water). Wash all aquaponic produce before eating. Leafy greens grown in media beds may have gravel particles trapped in leaves — rinse thoroughly.

## Quality Control

## Water Quality Monitoring Schedule

| Parameter | Frequency | Target | Action Threshold |
|-----------|-----------|--------|-----------------|
| pH | Weekly (daily during cycling) | 6.5-7.0 | <6.0: add calcium carbonate; >8.0: reduce buffer material |
| Ammonia (NH₃) | Weekly (daily during cycling) | <0.5 mg/L | >2 mg/L: emergency water change, stop feeding |
| Nitrite (NO₂⁻) | Weekly (daily during cycling) | <0.5 mg/L | >1 mg/L: add salt, increase aeration |
| Nitrate (NO₃⁻) | Weekly | 20-100 mg/L | <20: increase feeding; >150: partial water exchange |
| Dissolved oxygen | Daily observation of fish behavior | >5 mg/L | Fish gasping at surface: increase aeration immediately |
| Temperature | Daily | Species-dependent (see table) | Outside range: add/remove heat source |

## System Performance Benchmarks

| Metric | Target | Warning | Measurement Method |
|--------|--------|---------|-------------------|
| Fish feed conversion ratio | 1.5-2.0 | >3.0 (overfeeding or disease) | Total feed given ÷ total fish weight gain |
| Plant growth rate | Species-specific (see table) | <50% of expected rate | Days from transplant to harvest |
| Water clarity | Clear to slightly green | Brown or opaque | Visual inspection (turbidity indicates solids problem) |
| Bell siphon cycle frequency | 3-4 cycles per hour | <2 or >6 per hour | Time fill and drain cycles |

## Variations and Alternatives

## Aquaponics vs Other Growing Methods

| Parameter | Aquaponics | Soil-Based Gardening | Hydroponics |
|-----------|-----------|---------------------|-------------|
| Water use | Very low (recirculating) | High (irrigation) | Low (recirculating) |
| Fertilizer input | Fish food only | Compost, manure, amendments | Mineral salts, acid/base |
| Protein output | Yes (fish) | No | No |
| Complexity | High (living system) | Low | Medium |
| Daily attention required | 5-10 minutes | 15-30 minutes during season | 5-15 minutes |
| Startup time | 6-10 weeks | Days (plant seeds) | 1-2 weeks |
| Failure mode | Fish death (catastrophic) | Pest/disease (gradual) | Nutrient imbalance (gradual) |

## System Configuration Selection

| Situation | Recommended Configuration | Why |
|-----------|--------------------------|-----|
| Beginner, warm climate | Media bed + tilapia + lettuce | Simplest setup, most forgiving |
| Temperate climate, outdoor | Media bed + carp + kale | Carp tolerate cold water without heating |
| Limited space, indoor | DWC raft + tilapia + herbs | Highest yield per m², compact footprint |
| Semi-arid, water-scarce | NFT pipes + tilapia + greens | Lowest water use of any food production method |
| Integration with BSF farming | Media bed + tilapia + fruiting crops | BSF larvae feed fish; fish waste feeds plants |

## See Also

- [Aquaculture](../animals/aquaculture.md) — fish farming techniques, pond construction, fish species, and feeding that underpin aquaponic fish production
- [Insect Farming](../animals/insect-farming.md) — BSF larvae as fish feed, closing the nutrient loop
- [Vermiculture](./soil-management-vermiculture.md) — worm castings and worm tea as supplemental plant nutrients in aquaponics
- [Soil Management](./soil-management.md) — broader composting and soil fertility context
- [SEM Tech Hydroponics](./sem-tech-hydroponics.md) — more advanced technology that builds on aquaponics concepts; requires industrial membrane manufacturing
- [Water Procurement](../water/procurement.md) — water sources for system fill and make-up water
- [Water → Basic Treatment](../water/basic-treatment.md) — dechlorination and water quality for aquaponic use
- [Foundations → Agriculture](../foundations/food-agriculture.md) — basic cultivation knowledge
- [Food Processing](../food-processing/index.md) — downstream processing of aquaponic fish and vegetables



[← Back to Agriculture](index.md)
