# Aquaponics

> **Node ID**: agriculture.aquaponics
> **Domain**: [Agriculture](./)
> **Dependencies**: `animals.aquaculture`, `agriculture.soil-management`, `foundations.food-agriculture`
> **Enables**: `agriculture.hydroponic-ph-control`
> **Timeline**: Years 3-10+
> **Outputs**: fish, vegetables, herbs, filtered_water

### Overview

Aquaponics is an integrated food production system that combines fish farming (aquaculture) with soil-less plant cultivation in a single recirculating water loop. Fish produce ammonia-rich waste; bacteria convert that ammonia to nitrate; plants absorb the nitrate as fertilizer; the cleaned water returns to the fish tank. The result is two crops (fish and plants) from one water input, with the plants serving as the water filtration system for the fish and the fish providing free fertilizer for the plants.

Aquaponics is a **lower-technology** approach than chemical hydroponic systems. Where hydroponics requires precise chemical pH adjustment (adding phosphoric acid or potassium hydroxide), aquaponics achieves pH stability through natural biological buffering — calcium carbonate from crushed shells, bones, or limestone dissolves slowly to maintain pH in the 6.5-7.0 range. The nitrogen cycle is driven entirely by naturally occurring bacteria. No chemical inputs are needed for the core system beyond fish food and supplemental minerals (iron, calcium, potassium) that fish food does not provide in sufficient quantity. The more advanced [hydroponic pH control](./sem-tech-hydroponics.md) systems, which use electromembrane electrodialysis for ion-by-ion nutrient management, build upon the principles established by aquaponics but require substantially more industrial infrastructure.

A small aquaponic system — a 500-1000 L fish tank, a 1-2 m² grow bed, an air pump, and a water pump — produces 20-40 kg of fish and 30-60 kg of vegetables per year in a footprint of 3-4 m². This is meaningful protein and vegetable production from a system small enough to operate in a courtyard, greenhouse, or indoor room.

### System Design

#### Components

**Fish tank**: 500-1000 L for a household system. Food-grade polyethylene tank, or a concrete/brick tank lined with pond liner or waterproofed with cement render. Opaque or dark-colored to reduce algae growth. Minimum depth 40-60 cm. Located at or below the level of the grow beds to allow gravity drain-back.

**Grow beds** (plant cultivation area):
The grow bed to fish tank volume ratio should be 1:1 to 2:1. For a 500 L fish tank, plan 500-1000 L of grow bed volume. Three design approaches:

1. **Media-based grow bed** (simplest, recommended for beginners):
   A container filled with inert growing media — gravel (10-20 mm diameter, washed), expanded clay pebbles (hydroton), or lava rock. Media provides root support and surface area for beneficial bacteria. Flood and drain cycle: fill the bed with fish water, then drain it back (using a bell siphon or timed pump). This cycle delivers water and nutrients to roots, then draws air (oxygen) into the media as the water drains. Container depth 25-30 cm. Media size 10-20 mm (too small restricts water flow; too large provides insufficient surface area for bacteria). Avoid limestone gravel (raises pH excessively) and calcareous stone.

2. **NFT (Nutrient Film Technique)**:
   Plants sit in small cups or net pots in horizontal pipes (PVC, 50-100 mm diameter, with holes cut for pots). A thin film of water (1-2 mm deep) flows continuously through the pipe bottom, bathing the dangling roots. More water-efficient and lighter than media beds. Requires a solids filter (media bed or clarifier) before the NFT pipes because fish solids clog the narrow channels. More complex piping and plumbing.

3. **DWC (Deep Water Culture / Raft system)**:
   Plants float on polystyrene rafts on a tank of water 20-30 cm deep, with roots dangling directly into the aerated water. No media needed. Excellent for leafy greens. Requires a solids filter and biofilter (separate container with bio-media) because there is no gravel to host bacteria. Highest water volume but lowest maintenance of root systems.

**Water pump**: Submersible pump in the fish tank, rated to cycle the total water volume 1-2 times per hour. For a 1000 L system, a pump rated at 1000-2000 L/hr. Pumps require electricity (solar panel + battery, wind generator, or grid power). For non-electric systems, a hand-operated pump or a gravity-driven flow design (fish tank above grow beds, with a solar-powered or hand-cranked pump to lift water back) is possible but labor-intensive.

**Air pump + airstones**: Continuous aeration is essential. Dissolved oxygen must remain above 5 mg/L at all times for fish health. Air pump rated at 5-10 L/min for a household system, with airstones in the fish tank and (optionally) in the biofilter or sump. During power outages, battery backup or hand-operated bellows maintain aeration. Fish begin dying within 1-2 hours without aeration at warm temperatures (>25°C).

**Plumbing**: PVC pipes, connectors, and valves for water circulation. Bell siphon (for media bed flood-and-drain) or timer (for pump on/off cycling). Standpipe overflow in fish tank. Drain lines returning water from grow beds to fish tank by gravity.

**Biofilter** (if not using media beds):
A separate container filled with bio-media (plastic bioballs, shredded PVC bottles, lava rock, or clay shards) with water flowing through continuously. Provides surface area for nitrifying bacteria. Not needed with media-based grow beds (the media itself serves as the biofilter). For NFT and DWC systems, a biofilter is essential.

#### Bell Siphon (for media beds)

The bell siphon is the key mechanism for flood-and-drain cycling in media-based grow beds. It requires no moving parts, no timer, and no electricity for the drain cycle itself.

**Construction**:
- **Standpipe**: Vertical PVC pipe (25-32 mm diameter) set in the bottom of the grow bed, rising to the desired flood level (approximately 25 cm). Water rises to the top of this pipe and begins flowing down through it.
- **Bell**: A wider pipe (50-75 mm diameter, 5-10 cm taller than the standpipe) with a sealed cap on top, placed over the standpipe. Small holes (3-5 mm) drilled near the bottom of the bell allow water to enter. As water rises above the standpipe inside the bell, it begins to siphon, rapidly draining the bed.
- **Media guard**: A perforated pipe or cylinder around the bell, preventing gravel from entering the siphon mechanism.

**Cycle**: Water pumped into the grow bed fills it to the top of the standpipe. The bell siphon triggers and drains the bed rapidly (emptying in 2-5 minutes). The siphon breaks when air enters the bell at low water level. The cycle repeats, typically filling in 10-15 minutes and draining in 2-5 minutes, yielding 3-4 cycles per hour.

### The Nitrogen Cycle

Aquaponics depends on a biological process — the nitrogen cycle — in which bacteria convert toxic fish waste into plant-available nutrients. This cycle must be established before adding fish to the system.

**Step 1 — Ammonia (NH₃/NH₄⁺)**:
Fish excrete ammonia through their gills and in their waste. Ammonia is highly toxic to fish — concentrations above 1 mg/L cause stress, and above 2-3 mg/L are lethal. In a cycled system, ammonia is consumed almost as fast as it is produced, maintaining near-zero levels.

**Step 2 — Nitrite (NO₂⁻)**:
*Nitrosomonas* bacteria oxidize ammonia to nitrite. Nitrite is also toxic to fish — it binds to hemoglobin and prevents oxygen transport (brown blood disease). Concentrations above 1 mg/L are dangerous. These bacteria colonize all wet surfaces in the system, especially the grow bed media and biofilter.

**Step 3 — Nitrate (NO₃⁻)**:
*Nitrobacter* bacteria oxidize nitrite to nitrate. Nitrate is relatively non-toxic to fish (tolerated at 100-200 mg/L) and is the primary form of nitrogen that plants absorb. Plants in the grow bed consume nitrate, removing it from the water and completing the cycle.

**System cycling** (establishing the nitrogen cycle):
Before adding fish, the system must develop sufficient bacterial colonies to process waste. This takes 4-6 weeks.

1. Fill system with dechlorinated water. Run pump and aerator continuously.
2. Add an ammonia source: pure ammonia (ammonium hydroxide, 3-5 mg/L concentration in the water) or a small amount of fish food (which decomposes to release ammonia). Alternatively, add a inoculant of bacteria from an established aquarium or pond (speeds cycling significantly).
3. Test water daily using simple test kits (liquid reagent or test strips):
   - Week 1-2: Ammonia rises, then begins to fall as *Nitrosomonas* colonize.
   - Week 2-3: Nitrite rises (ammonia is being converted). This is the "nitrite spike" — the highest-risk period.
   - Week 3-4: Nitrite begins to fall as *Nitrobacter* colonize. Nitrate appears.
   - Week 4-6: Ammonia and nitrite both read near zero within 24 hours of adding ammonia. Nitrate rises steadily.
4. When ammonia and nitrite remain at zero 24 hours after adding ammonia, the system is cycled and ready for fish.

**Temperature and cycling**: Bacterial activity doubles for every 10°C increase (within the range 10-35°C). Systems cycle faster at 25-30°C than at 15-20°C. Below 10°C, cycling slows dramatically.

### Fish Species

#### Tilapia (*Oreochromis* spp.)

The standard aquaponics fish. Fast growth (500 g in 6-8 months under optimal conditions), tolerate crowding (20-40 kg/m³), omnivorous (accept plant-based and insect-based feeds), and thrive at 26-30°C. Tolerate pH 6.0-9.0. Breeding is prolific — mouthbrooding females produce 100-500 fry per spawn, and generation time is 5-7 months.

Drawbacks: Require warm water (>20°C for growth, >15°C to survive). In temperate climates, need heated water or indoor/greenhouse systems in winter. Susceptible to cold shock below 12°C. Not suitable for unheated outdoor systems in cold climates.

Feed: 2-3% body weight per day at optimal temperature. Accept BSF larvae (see [Insect Farming](../animals/insect-farming.md)), duckweed, algae, commercial pellets, agricultural byproducts (rice bran, oilseed cake). Protein requirement: 28-35% for optimal growth.

#### Carp (*Cyprinus carpio*)

Cold-hardy alternative to tilapia. Tolerate 4-35°C, optimal growth at 20-28°C. Accept lower water quality than tilapia. Omnivorous. Growth to 500 g-1 kg in one season with adequate feeding. Suitable for unheated outdoor systems in temperate climates.

Drawbacks: Slower growth than tilapia at warm temperatures. Lower market value in many regions. More tolerant of poor water quality, which can lead to neglect of water quality management.

#### Catfish (various species)

Tolerate low dissolved oxygen (some species have accessory air-breathing organs), turbid water, and crowding. Optimal 24-28°C. Growth to 500 g in 4-6 months. Accept animal-based feeds (BSF larvae, fish meal, blood meal). Suitable where water quality management is less precise.

#### Other options

- **Trout**: Require cold water (10-15°C) and high dissolved oxygen (>6 mg/L). Not suitable for warm-water systems. Excellent growth in cold climates with clean spring water.
- **Perch** (*Perca flavescens*): Cold-water tolerant, accept pellet feed. Moderate growth rate.
- **Goldfish / koi**: Hardy, attractive, tolerate wide conditions. Low food value but useful for cycling a system before introducing food fish, or for ornamental aquaponics.

### Plant Selection

#### Excellent (leafy greens and herbs)

These plants thrive on the nitrogen-rich water from fish systems and have low to moderate potassium and calcium requirements.

- **Lettuce** (all varieties): 4-6 weeks from transplant to harvest. The most reliable aquaponic crop.
- **Spinach**: 4-6 weeks. Prefers cooler temperatures (15-20°C). Bolts in heat.
- **Basil**: 4-6 weeks. High value, strong growth, tolerates warm water.
- **Kale**: 6-8 weeks. Cold-hardy, nutritious, continuous harvest (pick outer leaves).
- **Swiss chard**: 6-8 weeks. Heat-tolerant alternative to spinach.
- **Pak choi / bok choy**: 4-5 weeks. Fast-growing Asian green.
- **Watercress**: Grows directly in water — exceptionally well-suited to DWC systems.
- **Mint**: Aggressive grower — plant in the system to filter water, but contain it (mint will overtake other plants if not managed).

#### Moderate (requires potassium and calcium supplementation)

- **Tomatoes**: 12-16 weeks. Require potassium and calcium supplements (fish waste provides abundant nitrogen but insufficient K and Ca for fruiting). Add wood ash (potassium) and crushed eggshells or limestone (calcium) to the system or as a top-dressing in the grow bed.
- **Peppers**: 12-16 weeks. Same supplementation needs as tomatoes.
- **Cucumbers**: 8-12 weeks. Vigorous vines, require trellising.
- **Strawberries**: 12-16 weeks to first harvest. Perennial — continues producing.

**Potassium and calcium supplementation**:
Fish feed provides nitrogen and phosphorus abundantly, but potassium and calcium are consumed by plants faster than fish waste supplies them. Supplementation options (all natural, no chemical pH adjusters needed):
- **Potassium**: Wood ash (rich in potassium carbonate — add 1-2 tablespoons per 100 L system volume weekly), kelp meal, or banana peel extract (soak banana peels in water for 48 hours).
- **Calcium**: Crushed eggshells, crushed oyster shells, or agricultural limestone (calcium carbonate). Place in a mesh bag in the fish tank or sump — they dissolve slowly, releasing calcium and providing natural pH buffering. This is the primary pH management strategy: calcium carbonate sources dissolve to maintain pH at 6.5-7.0 without any chemical addition.
- **Iron**: Chelated iron (iron DTPA or iron EDTA) at 2-5 mg/L, added every 2-4 weeks. Iron deficiency shows as yellowing between leaf veins (interveinal chlorosis) on new growth. Without chelated iron supplement, most aquaponic systems develop iron deficiency over time.

#### Unsuitable

- **Root crops** (potatoes, carrots, onions): Grow media is too wet for most root crops. Can be grown in a separate wicking bed fed with aquaponic water.
- **Large fruiting trees**: Root systems too large, nutrient demand exceeds what fish waste provides.
- **Acid-loving plants** (blueberries, azaleas): Require pH 4.5-5.5; aquaponic systems run at pH 6.5-7.0.

### Water Quality Management

#### pH

Target: 6.5-7.0. This is a compromise between fish comfort (prefer 7.0-8.0), plant nutrient availability (prefer 5.5-6.5), and bacterial activity (prefer 7.0-8.0). At pH 6.5-7.0, all three function adequately.

**Natural buffering**: The key advantage of aquaponics over hydroponics. Calcium carbonate sources (crushed shells, limestone chips, concrete blocks) in the system dissolve slowly when pH drops below 7.0, releasing carbonate ions that neutralize acid and raise pH. When pH rises above 7.5, the carbonate source stops dissolving. This passive self-regulation maintains pH within a tolerable range without chemical addition or active management. This is fundamentally different from hydroponic systems, which require regular manual or automated addition of phosphoric acid or potassium hydroxide to maintain pH. The [hydroponic pH control](./sem-tech-hydroponics.md) article describes a much more advanced industrial approach using electromembrane electrodialysis — a technology that presupposes the industrial infrastructure to manufacture ion exchange membranes, power supplies, and sensor arrays. Aquaponics achieves comparable biological results using shells and bacteria.

**pH drift downward** (most common): Normal in maturing systems. Fish and bacterial respiration produces carbon dioxide, which forms carbonic acid. Plants release hydrogen ions when absorbing ammonium. Natural buffering from calcium carbonate usually compensates. If pH drops below 6.0, add crushed shells or limestone. Do not use chemical bases (sodium hydroxide, potassium hydroxide) — these cause rapid pH swings that stress fish and bacteria.

**pH drift upward**: Less common. May occur in new systems with concrete or limestone components still leaching alkalinity. Allow time for the system to equilibrate. If persistent, reduce calcium carbonate sources.

#### Water Temperature

- Tilapia systems: 26-30°C optimal. Below 20°C, growth slows. Below 15°C, fish stop eating. Below 10°C, fish die.
- Carp systems: 20-28°C optimal. Tolerate down to 4°C.
- Trout systems: 10-15°C optimal. Above 20°C, stress and disease risk increase. Above 25°C, lethal.

Temperature management: In cold climates, greenhouse enclosure with thermal mass (water tanks, stone, or earth berms) moderates temperature swings. A 1000 L fish tank provides significant thermal inertia — it takes 24-48 hours for the water temperature to change significantly. In hot climates, shade cloth over the fish tank and partial burying of the tank (ground temperature is more stable than air temperature) prevent overheating.

#### Dissolved Oxygen

Maintain above 5 mg/L at all times. Warm water holds less dissolved oxygen: at 30°C, saturation is only 7.5 mg/L; at 10°C, saturation is 11.3 mg/L. This makes warm-water tilapia systems more vulnerable to oxygen depletion (warm water, high fish metabolism, low oxygen capacity).

Continuous aeration with an air pump and airstones is non-negotiable. Backup: battery-powered air pump for power outages, or a venturi aerator (uses water flow from the pump to draw in air — no separate air pump needed but reduces water flow rate by 10-20%).

#### Ammonia and Nitrite Monitoring

Test ammonia and nitrite weekly (more frequently during system cycling and after any system disruption — pump failure, overfeeding, temperature shock). Acceptable levels:
- Ammonia: below 0.5 mg/L (ideally near zero in a cycled system)
- Nitrite: below 0.5 mg/L (ideally near zero)
- Nitrate: 20-100 mg/L (below 20 suggests insufficient fish waste for plants; above 150 suggests insufficient plants or need for water exchange)

**Emergency ammonia spike**: If ammonia exceeds 2 mg/L, immediately stop feeding, perform a 30-50% water change, increase aeration, and add a bacteria inoculant if available. Identify the cause (overfeeding, dead fish, pump failure, filter crash).

### Fish Management

#### Stocking Density

- **Conservative** (low-risk, recommended): 20 kg of fish per cubic meter of water (20 kg/m³). For a 1000 L tank, stock a maximum of 20 kg total fish weight.
- **Moderate**: 30 kg/m³. Requires excellent water quality management and reliable aeration.
- **Intensive**: 40 kg/m³ and above. Requires continuous monitoring, backup systems, and experienced management. High risk of catastrophic loss from equipment failure.

Start conservative. Stock at 10-15 kg/m³ when fish are small and increase as the biofilter matures and bacterial processing capacity grows.

#### Feeding

Feed 2-3% of total fish body weight per day, split into 2-3 feedings. A system with 20 kg of tilapia receives 400-600 g of feed per day.

**Feed sources**:
- Commercial fish pellets (simplest, highest quality)
- BSF larvae (see [Insect Farming](../animals/insect-farming.md)) — excellent protein source, can replace 50-100% of commercial feed
- Duckweed (*Lemna* spp.) — 25-35% protein, grows on the fish tank surface itself
- Earthworms (see [Vermiculture](./soil-management-vermiculture.md))
- Agricultural byproducts: rice bran, soybean meal, blood meal

**Feeding rule**: Fish should consume all feed within 15 minutes. If feed remains after 15 minutes, reduce the ration. Uneaten feed decomposes to ammonia, degrading water quality. Fish appetite varies with temperature — reduce feeding when water is below 20°C (for tilapia) or above 28°C (for trout).

### System Startup

1. **Build the system**: Assemble fish tank, grow bed(s), plumbing, bell siphon, pump, and air pump. Check all connections. Fill with dechlorinated water. Test the bell siphon cycle (fill and drain 3-4 times to verify timing).
2. **Add bio-media and plant**: Fill grow beds with washed gravel or clay pebbles. Plant seedlings in the media (or set up NFT pipes / DWC rafts). Start with fast-growing plants (lettuce, basil) to begin consuming nutrients.
3. **Cycle the system** (4-6 weeks): Add ammonia source. Test daily. Wait for ammonia and nitrite to read zero.
4. **Add fish**: Stock at low density (10-15 kg/m³). Introduce fish gradually — add 25% of final intended stocking at first, then increase over 2-4 weeks as the bacterial colony grows to match the increasing ammonia load. Acclimate fish to water temperature before release (float transport container in the tank for 30 minutes).
5. **Monitor daily**: Check that pump and aerator are running. Observe fish behavior (listless fish at surface = oxygen or ammonia problem). Check water flow through grow beds. Test ammonia and nitrite weekly.
6. **Begin harvesting plants**: 4-6 weeks after planting. Harvest outer leaves of leafy greens (continuous production) or whole plants. Replant immediately.
7. **Harvest fish**: When they reach target size (tilapia: 400-500 g at 6-8 months). Remove the largest fish and replace with fingerlings to maintain steady production.

### Aquaponics vs Hydroponics — Technology Level

It is important to understand where aquaponics sits on the technology spectrum relative to other growing methods:

| Parameter | Aquaponics | Basic Hydroponics | SEM Tech Hydroponics |
|-----------|-----------|-------------------|---------------------|
| pH control | Natural (calcium carbonate buffering) | Manual chemical dosing | Electromembrane electrodialysis |
| Nutrient source | Fish waste + bacteria | Dissolved mineral salts | Refined mineral solutions + ED control |
| pH precision | ±0.3-0.5 units | ±0.3-0.5 units | ±0.1 units |
| Required infrastructure | Tank, gravel, pump, fish | Tank, media, pump, chemicals | ED stack, membranes, sensors, power supply |
| Industrial prerequisites | Basic plumbing, electricity | Basic chemistry, electricity | Polymer membranes, electronics, precision manufacturing |
| Biological complexity | High (fish, bacteria, plants) | Low (plants only) | Low (plants only) |
| Operating inputs | Fish food, seeds | Mineral salts, acid/base | Electricity |
| Skill level | Moderate (living system management) | Moderate (chemistry management) | High (industrial process control) |

Aquaponics achieves functional nutrient delivery using natural biological processes and simple materials. The "advanced" aspects are biological knowledge (nitrogen cycle, fish health) rather than industrial capacity. Hydroponic pH control — and especially the SEM Tech electromembrane approach — requires manufacturing capabilities (membrane fabrication, precision electronics, chemical synthesis) that come much later in the bootstrap sequence. Aquaponics is attainable at the level of basic plumbing and electricity; hydroponic pH control requires a functioning chemical industry.

### Cross-Domain Links

- **[Aquaculture](../animals/aquaculture.md)** — fish farming techniques, pond construction, fish species, and feeding that underpin aquaponic fish production
- **[Insect Farming](../animals/insect-farming.md)** — BSF larvae as fish feed, closing the nutrient loop
- **[Vermiculture](./soil-management-vermiculture.md)** — worm castings and worm tea as supplemental plant nutrients in aquaponics
- **[Soil Management](./soil-management.md)** — broader composting and soil fertility context
- **[SEM Tech Hydroponics](./sem-tech-hydroponics.md)** — MORE ADVANCED technology that builds on aquaponics concepts; requires industrial membrane manufacturing

### Safety

**Waterborne disease**: Aquaponic water contains fish waste and bacteria. Do not drink system water. Wash hands after handling fish, grow bed media, or system water. Fish can carry *Salmonella* and *Streptococcus* spp. — maintain good hygiene around the system, especially if children have access.

**Electrical safety**: Water pumps and air pumps operate in and around water. Use ground-fault circuit interrupters (GFCIs) on all electrical outlets near the system. Secure all cables above water level. Do not operate damaged pumps. Solar-powered systems with low-voltage DC pumps (12V) reduce shock risk significantly compared to mains-powered AC pumps.

**Fish health and water quality**: Ammonia and nitrite spikes kill fish rapidly. Test water regularly, especially in new systems. Never overfeed — excess food is the most common cause of ammonia spikes. Maintain continuous aeration — fish die within 1-2 hours without oxygen in warm water. Have a backup aeration plan (battery-powered air pump, or even a bucket brigade to splash water for emergency aeration).

**Heavy metals**: Do not use galvanized metal (zinc-coated) components in the system — zinc is toxic to fish at low concentrations. Copper is also toxic to fish (and to invertebrates like shrimp and snails). Use plastic, stainless steel, or ceramic components for plumbing and fittings. Lead solder in plumbing is a contamination risk — use lead-free connections.

**Plant food safety**: Fish waste can contain human pathogens if the fish are fed manure or contaminated feed. Use only clean feed sources (commercial pellets, BSF larvae raised on food waste, duckweed from clean water). Wash all aquaponic produce before eating. Leafy greens (lettuce, basil) grown in media beds may have media particles trapped in leaves — rinse thoroughly.

---

[← Back to Agriculture](index.md)
