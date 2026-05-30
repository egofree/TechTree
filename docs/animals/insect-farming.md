# Insect Farming (Black Soldier Fly)

> **Node ID**: animals.insect-farming
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.domestication`](domestication.md)
> **Enables**: [`animals.aquaculture`](aquaculture.md), [`animals.poultry.chickens`](poultry-chickens.md)
> **Timeline**: Years 1-10+
> **Outputs**: bsf_larvae, protein_meal, chicken_feed, fish_feed, frass_fertilizer, compost
> **Critical**: Yes — closes the nutrient loop by converting waste streams into animal feed protein


In a bootstrapping civilization, protein is the limiting nutrient for both humans and livestock. Fish meal (the traditional animal feed protein source) requires ocean fishing fleets. Soybean meal requires large-scale agriculture, oil pressing, and transport. BSF farming converts waste — food scraps, manure, brewery grain, crop residues — into 40-45% protein feed using nothing more than a wooden box and organic waste. The conversion efficiency is extraordinary: 1.4-2.0 kg of wet biowaste produces 1 kg of fresh larvae in 14-18 days. No other protein production system matches this speed and efficiency with zero purchased inputs.

Without BSF farming: no cost-effective animal feed protein without fishing or soybean farming (both require infrastructure far beyond early settlement capability), no closed-loop waste management (organic waste accumulates, attracts vermin, and loses its nutrient value), no high-protein supplement for aquaculture (fish farming depends on protein feed — without BSF or fish meal, farmed fish grow 50-70% slower), no rapid composting pathway (BSF larvae process waste 5-10× faster than traditional composting). Without BSF farming, every scrap of animal feed protein must come from land-intensive grain or labor-intensive wild harvest.

BSF farming closes the loop between waste and food production. Settlement waste → BSF larvae → animal feed → eggs, meat, fish → more waste → more larvae. Each cycle recovers 15-20% of the waste stream's protein content as usable animal feed. Frass (larval excrement) returns nitrogen, phosphorus, and potassium to the soil. A settlement with BSF farming converts a waste disposal problem into a feed production asset.

## Prerequisites

- **Materials**: [Organic waste](../foundations/food-agriculture.md) (food scraps, manure, crop residues — 5-200 kg/day depending on scale), [timber or concrete](../construction/index.md) for bin construction, [corrugated cardboard](../knowledge/writing.md) for ovitraps (egg-laying substrates), [pond liner or clay](../ceramics/index.md) for waterproofing wooden bins, [dry carbon material](../plants/fiber-plants.md) (straw, sawdust, dry leaves) for moisture control in substrate
- **Tools**: [Handsaw and hammer](../machine-tools/index.md) for bin construction, [thermometer](../measurement/index.md) for substrate temperature monitoring, [screw press or hydraulic press](../machine-tools/index.md) for oil extraction from dried larvae, [screen or tarp](../textiles/fibers.md) for sun-drying larvae, [stone mill or hammer mill](../machine-tools/machining.md) for grinding dried larvae into meal
- **Knowledge**: BSF life cycle and environmental requirements (temperature, humidity, light), substrate preparation (particle size, moisture content 65-75%), self-harvesting ramp design (30-45° angle, collection channel), population management (colony self-regulation through feed supply)
- **Infrastructure**: Covered, shaded area for bins (larvae prefer dark, temperatures 25-30°C), drainage for leachate collection, drying area (full sun exposure for sun-drying, or solar dryer), storage for dried product (dry, cool, below 15% moisture, protected from rodents)

## Bill of Materials — Medium-Scale BSF Unit (50 kg waste/day)

| Item | Specification | Quantity | Notes |
|------|--------------|----------|-------|
| Rearing bin | Concrete block or timber, 3 m × 1.5 m × 0.6 m, waterproof-lined | 1 unit | Opaque walls (larvae prefer dark); drainage at lowest point |
| Self-harvesting ramps | Timber or sheet metal, 15-20 cm wide, 30-45° angle | 4-6 ramps | Lead to collection channels (5-8 cm diameter pipe) |
| Collection buckets | 10-20 L plastic or galvanized steel | 2-4 | Prepupae drop into buckets via collection channels |
| Ovitraps | Corrugated cardboard strips, 5 × 15 cm | 10-20 strips | Suspended above substrate; replace when egg-laden |
| Adult breeding enclosure | Fine mesh (1 mm openings), 1 × 1 × 1 m frame | 1 unit | Allows mating in contained space; needs bright light |
| Thermometer | Dial or digital, 0-50°C range | 1 | Insert into substrate mass; overheating >40°C kills larvae |
| Substrate (daily input) | Food waste, manure, or mixed organic waste | 50 kg/day | 65-75% moisture; chop to <5 cm particles |
| Dry carbon material | Straw, sawdust, or dry leaves | 5-10 kg/day | Mix with wet waste to control moisture |
| Drying screens | Wire mesh on wooden frames, 1 × 2 m | 2-3 frames | For sun-drying harvested prepupae |
| Storage containers | Sealed buckets or barrels with tight lids | 2-4 | For dried larvae; must be rodent-proof and dry |


Insect farming with Black Soldier Fly (BSF, *Hermetia illucens*) converts organic waste into high-protein animal feed and nutrient-rich fertilizer using minimal land, water, and infrastructure. BSF larvae consume almost any organic matter — food waste, manure, brewery grain, slaughter byproducts — and convert it to body mass at remarkable efficiency: 1 tonne of biowaste yields 150-200 kg of fresh larvae in just 14-18 days.

Unlike bees (the only truly domesticated insect), BSF are managed rather than domesticated. Adult flies are not pests — they do not bite, do not carry disease, do not visit human food, and do not enter dwellings. Adults live only 5-8 days, during which they mate and lay eggs but do not eat, relying entirely on fat stores accumulated during the larval stage. This makes BSF farming hygienic and compatible with human settlements.

BSF farming fills a critical niche in a bootstrapping civilization: it closes the nutrient loop by converting waste streams into animal feed protein, reducing dependence on wild-caught fish meal or imported soybean meal. The system scales from a single household bin (processing 5 kg waste per day) to industrial operations handling tonnes per day.

## Life Cycle

**Egg**: Female flies lay 500-900 eggs in clusters near decaying organic matter, in crevices or on cardboard strips provided as ovitraps (egg-laying traps). Eggs are 1 mm long, cream-colored. Incubation: 3-5 days at 25-30°C.

**Larva** (5 instars, 14-18 days at optimal conditions):
The workhorse stage. Larvae are cream-colored, legless grubs reaching 20-25 mm length and 0.1-0.2 g each at maturity. They feed continuously, consuming 25-50 mg of substrate per larva per day. At optimal temperature (27-30°C) they grow 10,000-fold from hatch to prepupa in about two weeks. Temperature below 20°C slows growth dramatically; below 10°C, development halts. They tolerate a wide pH range (3-11) in their substrate.

**Prepupa**: Final larval instar before pupation. Ceases feeding, empties gut, and changes color from cream to dark brown-black as the exoskeleton hardens and sclerotizes. This is the self-harvesting stage — prepupae instinctively climb upward and away from the feeding mass, seeking dry, dark crevices for pupation. This behavior is exploited by ramp-based harvesting systems.

**Pupa**: Immobile, dark brown, 15-20 mm. Pupation lasts 14-21 days at 25-27°C. Does not feed. Vulnerable to desiccation and predation.

**Adult**: 15-20 mm long, wasp-like in appearance (black body, transparent wings) but harmless — no sting, no bite. Adults do not feed; they survive on fat reserves from the larval stage. Lifespan: 5-8 days. Mating occurs in flight, requiring enclosure with natural or artificial light. Females lay eggs within 2-3 days of mating. Adults are strong fliers and will disperse if not contained, but they do not infest homes or food stores.

**Environmental requirements for optimal growth**:
- Temperature: 25-30°C (larvae), 27°C (pupation), 25-30°C with 60-80% humidity (adult mating)
- Light: Adults require bright light for mating (natural sunlight or equivalent). Larvae prefer darkness — light triggers pupation behavior.
- Humidity: 60-80% for all stages. Below 50%, eggs desiccate; above 90%, fungal problems develop.
- Substrate moisture: 65-75% for larval feed (squeezing a handful should yield a few drops of water).

## BSF Bin Construction

**Small-scale bin** (household, 5-10 kg waste/day):

Construct a rectangular container from timber planks, concrete, or clay-brick. Dimensions: 1 × 2 × 0.5 m (length × width × height). The bin must be opaque (larvae prefer dark conditions) and waterproof-lined if made from timber (use pond liner, clay render, or food-safe plastic sheeting).

**Ramp system for self-harvesting**:
The key innovation. Attach ramps (timber or sheet metal, 15-20 cm wide) to the interior walls at a 30-45° angle, positioned 5-10 cm above the substrate surface. Prepupae climb the ramps seeking pupation sites. At the top of each ramp, position a collection channel or pipe (5-8 cm diameter) that leads to a collection bucket outside the bin. Prepupae follow the channel and drop into the bucket, self-harvesting without manual sorting.

**Lid and adult enclosure**:
Cover the bin with a lid that allows some airflow but prevents adult flies from escaping if breeding on-site. For breeding, a separate cage or net enclosure (1 × 1 × 1 m minimum) of fine mesh (1 mm openings) surrounds the bin and an ovitrap (corrugated cardboard strips or small wooden blocks with crevices, suspended above the substrate).

**Drainage**:
Install a drain at the lowest point of the bin (pipe or channel) to collect leachate — the liquid that drains from decomposing waste. Leachate can be diluted 1:10 with water and used as liquid fertilizer, though it is too strong for direct application.

**Medium-scale unit** (50-200 kg waste/day):
Concrete or concrete-block construction, 3-5 m × 1-2 m × 0.6 m. Multiple ramp channels feeding into central collection troughs. Partition into sections for continuous production: one section receives fresh waste daily while another section's larvae mature and self-harvest. This rotation ensures continuous output. Cover with a roof structure for weather protection.

## Feed Substrates

BSF larvae consume nearly any organic matter except materials high in cellulose/lignin (woody material, paper) or toxic compounds.

**Excellent substrates** (high conversion, rapid growth):
- Food waste (restaurant, household, market scraps)
- Fruit and vegetable processing waste
- Brewery spent grain and distiller's grain
- Manure (poultry, pig, cattle — composted or fresh)
- Slaughter waste (blood, offal, bone meal — mixed with carbon source)
- Fish processing waste

**Acceptable substrates** (slower growth, lower conversion):
- Crop residues (stalks, husks, cobs — must be chopped or shredded)
- Restaurant grease trap waste (dilute with dry carbon material)
- Paper/cardboard (shredded, soaked — low nutrition, serves mainly as bulk)

**Avoid**:
- Citrus peels (d-limonene and other essential oils are toxic to larvae)
- Pine needles and conifer material (toxic resins)
- High-salt materials (pickling brine, soy sauce waste — salt tolerance is limited)
- Pesticide-contaminated material (larvae bioaccumulate some toxins)
- Wood chips and sawdust (indigestible lignin, though usable as bedding)

**Preparation**: Chop or shred substrate to particles under 5 cm for fastest consumption. Mix wet and dry materials to achieve 65-75% moisture. Pre-composting for 1-2 days (allowing microbial breakdown to begin) increases palatability and larval growth rate by 10-20%.

## Nutritional Profile and Processing

**Fresh whole larvae** (prepupae, ~44% dry matter):
- Crude protein: 40-45% of dry weight
- Crude fat: 30-35% of dry weight
- Ash (minerals): 5-10% of dry weight
- Calcium: 5-8% of dry weight (unusually high for insects, due to mineral-rich substrates)
- Amino acid profile: comparable to fish meal, with methionine as the limiting amino acid

**Processing methods**:

1. **Sun-drying**: Spread larvae in thin layer on screens or tarps. Full sun, 2-3 days in hot dry weather. Stir occasionally. Moisture drops below 10%. Risk of fly contamination and uneven drying in humid climates. Low labor, no equipment needed.

2. **Oven-drying**: Spread on trays in oven or solar dryer at 60°C for 6-12 hours until moisture below 10%. More consistent than sun-drying. Requires fuel or solar dryer construction.

3. **Defatting**: Press dried larvae in a screw press or hydraulic press to extract fat (BSF oil). Yield: 15-25% of dry weight as oil. The remaining defatted meal has 55-60% protein — comparable to premium fish meal. BSF oil can be used as animal feed energy source, biodiesel feedstock, or soap making.

4. **Milling**: Grind dried larvae (whole or defatted) in a stone mill or hammer mill to produce protein meal. Particle size 0.5-2 mm for mixing into animal feed rations.

## Products and Applications

**Live larvae** (fresh):
- Direct feed for chickens, ducks, and pigs. Chickens consume 20-50 g larvae per day, providing 30-50% of their protein needs. Feed live by scattering in poultry range or in troughs.
- Fish feed for [aquaculture](./aquaculture.md). Tilapia and catfish accept live BSF larvae eagerly. Feed at 2-5% of fish body weight per day.
- Live larvae keep 3-5 days in cool, dark, ventilated conditions. Do not store in sealed containers — they generate heat and moisture that promote spoilage.

**Dried larvae** (whole):
- Shelf-stable for 6-12 months in dry, cool storage. Feed whole to poultry or fish, or mill into meal.
- Trade good — dried larvae are compact, lightweight, high-value protein that stores and transports easily.

**Protein meal** (dried and milled, optionally defatted):
- Mix into formulated feeds at 20-40% of total ration. Partially or fully replaces fish meal in most animal feed formulations.
- Amino acid supplementation with methionine (or methionine-rich plant sources like sesame meal) improves the protein quality of BSF meal to match fish meal.

**BSF oil** (pressed from dried larvae):
- Lauric acid content (25-35% of fat) similar to coconut oil — antimicrobial properties.
- Energy supplement in animal feed (8-9 kcal/g).
- Potential soap and candle making (similar to tallow).

**Frass** (larval excrement + shed skins + undigested residue):
- Insect waste remaining after larvae are harvested. Nutrient analysis: approximately 3% nitrogen, 2% phosphorus, 1.5% potassium (similar to bat guano).
- Contains chitin from shed exoskeletons — chitin stimulates plant immune responses and suppresses soil pathogens.
- Apply at 1-2 kg/m² as soil amendment or top-dressing. Can be mixed into potting soil at 10-20% by volume.
- Not as biologically active as vermicompost (see [soil management](../agriculture/soil-management.md)), but faster to produce and higher in mineral nutrients.

## Comparison with Other Edible Insects

| Feature | Black Soldier Fly | Mealworm (*Tenebrio molitor*) | House Cricket (*Acheta domesticus*) |
|---------|-------------------|-------------------------------|-------------------------------------|
| Feed conversion | 1.4-2.0:1 (wet weight) | 2.5-3.5:1 | 1.7-2.5:1 |
| Protein (dry weight) | 40-45% | 50-60% | 55-65% |
| Fat (dry weight) | 30-35% | 30-40% | 15-25% |
| Substrate range | Very broad (any organic waste) | Narrow (grain-based) | Moderate (grain + vegetable) |
| Self-harvesting | Yes (prepupal migration) | No (manual harvest) | No (manual harvest) |
| Temperature optimum | 27-30°C | 25-28°C | 28-32°C |
| Adult stage eats | No | Yes | Yes |
| Space efficiency | Very high (vertical stacking) | Moderate | Moderate |
| Primary use | Animal feed (livestock, fish) | Human food, pet feed | Human food, pet feed |
| Disease risk | Very low | Low (grain mites) | Moderate (cricket paralysis virus) |

BSF excels at waste conversion and animal feed production. Mealworms and crickets are better suited for direct human consumption due to higher protein content and better flavor, but they require higher-quality feed (grain-based) and lack self-harvesting capability.

## Colony Establishment and Management

**Obtaining starter colony**:
Wild BSF are found on every continent except Antarctica in temperate and tropical regions. They naturally colonize compost piles, manure heaps, and decaying organic matter. To attract wild flies: place an open container of rotting fruit or kitchen waste in a warm, shaded outdoor location. Within 1-4 weeks (depending on local BSF population and season), wild females will lay eggs in the substrate. Provide ovitraps (corrugated cardboard strips) for egg collection. Transfer egg-laden cardboard to a prepared rearing bin with fresh substrate.

Once established, a self-sustaining colony requires only: (1) continuous supply of organic waste, (2) a contained area for adult mating and egg-laying, and (3) protection from extreme temperatures and heavy rain.

**Population management**:
A well-managed colony is self-regulating. Female flies lay eggs proportional to available substrate — when food is scarce, fewer eggs are laid and larvae take longer to develop, naturally reducing population. When food is abundant, the colony expands rapidly. To increase production: add more substrate and more rearing bins. To decrease: stop feeding some bins and allow the larvae to pupate, then collect and process the prepupae.

**Temperature management**:
In cold climates (<15°C), BSF activity ceases. Maintain indoor or greenhouse rearing spaces with temperatures above 20°C for year-round production. In hot climates (>35°C), provide shade and ventilation — larvae generate metabolic heat and can overheat in sealed bins, killing the colony. A simple thermometer inserted into the substrate mass alerts to overheating risk.

**Pest and disease management**:
BSF larvae outcompete most other insects (including houseflies) for food resources. A healthy BSF colony suppresses housefly populations because BSF larvae consume substrate faster and at higher temperatures. Problems include:
- **Mites**: Appear in overly dry or overcrowded conditions. Reduce density and increase substrate moisture.
- **Fungal growth**: Excessive moisture or poor drainage. Improve drainage, add dry carbon material, and reduce water content of feed.
- **Ants**: May raid bins for larvae. Place bin legs in water moats or apply diatomaceous earth barriers.
- **Predatory birds**: Chickens will eagerly eat prepupae from collection buckets. Cover collection points.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Larvae not growing (stunted, small at 14+ days) | Substrate too dry or too wet; temperature below 20°C; poor-quality feed | Adjust moisture to 65-75% (squeeze handful — a few drops should fall); warm bin to 25-30°C; add higher-quality feed (food waste, grain) |
| Colony die-off (larvae dying en masse) | Overheating (>40°C from metabolic heat in sealed bin); toxic substrate (citrus, pine, pesticides); anaerobic conditions (waterlogged) | Ventilate bin immediately; reduce substrate depth to <15 cm; remove toxic material; improve drainage |
| Houseflies outnumbering BSF in bin | BSF colony too small to compete; insufficient BSF eggs; substrate too fresh (houseflies prefer fresh waste) | Add more BSF eggs from ovitraps; pre-compost waste 1-2 days before adding to bin (reduces housefly attractiveness); increase BSF larval density |
| Prepupae not climbing ramps | Ramps at wrong angle (too steep or too flat); ramps not positioned above substrate surface; ramps too smooth for larvae to grip | Set ramps at 30-45° angle; position 5-10 cm above substrate; add texture to ramps (rough timber, wire mesh overlay) |
| Ants raiding bins for larvae | Bin in contact with ground; no ant barrier | Place bin legs in water-filled cans or moats; apply diatomaceous earth or ash ring around bin base; elevate bin on stands |
| Adult flies not mating | Insufficient light (need bright sunlight equivalent); enclosure too small; temperature below 25°C | Provide direct sunlight or bright artificial light (>2000 lux); increase enclosure size to minimum 1 m³; warm enclosure to 25-30°C |
| Fungal growth on substrate | Excessive moisture (>80%); poor drainage; overcrowding | Add dry carbon material (straw, sawdust) to absorb moisture; clear drainage channels; reduce substrate depth |
| Mites on larvae | Overly dry conditions; overcrowding; poor ventilation | Increase substrate moisture to 70%; reduce larval density; improve bin ventilation; mites are rarely fatal but reduce growth rate |
| Bad odor from bin | Anaerobic decomposition (waterlogged substrate); overfeeding (waste accumulates faster than larvae consume) | Improve drainage; reduce daily feed input; add dry carbon material; stir substrate gently to aerate |
| Larvae escaping bin | Substrate too wet (larvae flee flooding); bin walls too low; overcrowding | Reduce moisture to 65-75%; raise bin walls to >50 cm; split colony into additional bins |

## Bootstrap Sequence

1. **Wild-colonized compost** (Year 0-1): Begin by attracting wild BSF to compost heaps with food waste and manure. Observe life cycle. Collect prepupae by hand from compost pile edges. Feed directly to chickens. No infrastructure needed — BSF naturally colonize suitable organic matter in most climates.

2. **Basic bin with ramp harvest** (Year 1-3): Construct timber or concrete bin with ramp self-harvesting system. Manage feed inputs and moisture. Separate adult breeding area from larval rearing. Dry excess larvae in the sun for storage. Begin feeding dried larvae to fish in aquaculture ponds.

3. **Expanded multi-bin operation** (Year 3-5): Multiple bins in rotation for continuous production. Process larvae with screw press for oil extraction. Mill defatted meal for formulated feed. Collect and apply frass to crop fields. Integrate with poultry and fish farming as a waste-to-feed converter.

4. **Industrial-scale waste processing** (Year 5-10+): Large concrete or steel processing units handling community-scale organic waste. Continuous-flow through systems. Mechanical drying (solar dryer or waste-heat dryer). Quality-controlled protein meal production. Full integration with livestock, aquaculture, and agriculture as the primary protein recycling pathway.

## See Also

- [Aquaculture](aquaculture.md) — BSF larvae as fish feed, replacing wild-caught fish meal
- [Poultry Farming](poultry.md) — BSF larvae as high-protein chicken and duck feed
- [Pigs](pigs.md) — BSF larvae as pig feed supplement
- [Domestication & Husbandry](domestication.md) — livestock feed requirements and protein needs
- [Soil Management](../agriculture/soil-management.md) — BSF frass as fertilizer; BSF bins as composting method
- [Vermiculture](../agriculture/soil-management-vermiculture.md) — complementary waste processing; BSF pre-processes waste that worms finish
- [Food & Agriculture](../foundations/food-agriculture.md) — agricultural waste streams feed BSF larvae; closing nutrient loops
- [Waste Management](../ehs/index.md) — organic waste processing and sanitation
- [Chemistry: Oils & Fats](../chemistry/index.md) — BSF oil extraction and processing

## Safety

**Adult BSF are not pests**:
Black Soldier Fly adults do not bite, sting, or carry diseases. They are not attracted to human food, living spaces, or garbage cans (they prefer decomposing organic matter for egg-laying). They are often mistaken for wasps due to their black-and-clear-wing appearance, but they are entirely harmless. BSF presence actually reduces housefly and blowfly populations by competitive exclusion.

**Allergen concerns**:
Insect proteins can cause allergic reactions in sensitive individuals, particularly those with shellfish allergies (chitin cross-reactivity). Handle larvae with gloves if sensitive. Dust from dried and milled larvae can cause respiratory irritation — wear a cloth mask when milling or handling large quantities of dried meal.

**Pathogen reduction**:
BSF larvae reduce pathogen loads in waste substrates. Studies show 90-99% reduction in *Salmonella* and *E. coli* populations during larval processing. The combination of larval digestive enzymes, antimicrobial peptides in larval gut secretions, and the thermophilic conditions in active BSF bins (substrate reaches 35-45°C from larval metabolic heat) contributes to pathogen suppression. However, BSF processing alone does not produce pathogen-free material — always compost frass at 55°C+ before applying to food crops.

**Chemical contaminants**:
BSF larvae bioaccumulate certain contaminants from their substrate: heavy metals (lead, cadmium, mercury), pesticides, and mycotoxins. Larvae raised on contaminated waste produce contaminated meal. Use clean organic waste sources for larvae intended as animal feed. Avoid using industrial waste, treated lumber scraps, or pesticide-sprayed crop residues.

**Handling precautions**:
- Wash hands after handling larvae or frass
- Keep processing areas separate from food preparation
- Do not feed BSF larvae raised on manure to other animals without drying or cooking (pathogen risk from substrate)
- Dry larvae to below 10% moisture for safe long-term storage — above 15%, mold and aflatoxin risk increases rapidly



[← Back to Animals](index.md)
