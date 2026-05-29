# Chickens (*Gallus gallus domesticus*)

> **Node ID**: animals.poultry.chickens
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.poultry`](poultry.md), [`animals.insect-farming`](insect-farming.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 0-5
> **Outputs**: eggs, chicken_meat, feathers, manure
> **Critical**: Yes — gateway livestock for settlement food systems; lowest barriers to entry of any domestic animal

### Overview

Chickens are the most widely kept poultry species worldwide, descended from the red junglefowl (*Gallus gallus*) of Southeast Asia. Domesticated approximately 8,000 years ago, chickens provide eggs, meat, feathers, and manure with relatively modest infrastructure requirements. A small flock of 10-20 hens supplies a household with 15-30 eggs per week while producing nitrogen-rich manure (1.5% N — the highest of any common livestock) for garden fertility. Chickens are the gateway livestock for settlement food systems: they accept a wide range of feeds, reproduce readily, reach slaughter weight quickly, and require no specialized butchering equipment.

Mature weight ranges from 1.5-2.5 kg for hens to 2.5-3.5 kg for roosters in dual-purpose breeds. Point-of-lay occurs at 18-22 weeks. Broilers reach slaughter weight (2.0-2.5 kg) at 6-8 weeks on intensive feed, or 12-16 weeks on range. A well-managed laying hen produces 200-300 eggs per year in modern breeds, 150-200 in heritage breeds, with each egg weighing 50-65 g.

## Prerequisites

| Requirement | Source | Notes |
|-------------|--------|-------|
| Grain feed (corn, wheat, oats) | [`agriculture`](../agriculture/soil-management.md) | 100-150 g/day per hen |
| Protein supplement (soy, peas) | [`agriculture`](../agriculture/soil-management.md) | 14-24% of diet depending on age |
| Secure coop with wire mesh | [`construction`](../construction/building-materials.md) | 0.1-0.2 m² per bird indoor |
| Oyster shell or limestone grit | [`mining`](../mining/processing.md) | Free-choice for layers |
| Clean water system | [`water`](../water/basic-treatment.md) | 250-400 mL/bird/day |
| Brooder with heat source | [`foundations.tools-basic`](../foundations/tools-basic.md) | 35°C initial for chicks |

### Bill of Materials

Materials listed for a 25-hen flock per year.

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Layer feed (16-18% protein) | 1,000-1,400 kg | [`agriculture`](../agriculture/soil-management.md) | Home-mixed grain + protein supplement |
| Oyster shell | 25-50 kg | [`mining`](../mining/processing.md) | Crushed eggshells (recycled) |
| Bedding (pine shavings/straw) | 200-400 kg | [`plants`](../plants/index.md) | Deep litter method |
| Feed storage (metal bins) | 2-3 units (35-50 L) | [`metals`](../metals/index.md) | Rodent-proof containers |
| Wire mesh (hardware cloth) | 10-20 m² | [`metals`](../metals/index.md) | For coop vents and run |

### Breed Selection

**Layer breeds**:
Optimized for egg production. Leghorn hens produce 280-320 white eggs per year at 100-150 g feed/day. Rhode Island Red hens produce 250-300 brown eggs per year and are more cold-hardy and disease-resistant than Leghorns. Sussex hens yield 240-260 eggs per year and are calm, reliable foragers. Layer breeds are lightweight (1.5-2.0 kg hens) and convert feed efficiently to eggs (2-2.5 kg feed per kg of egg mass).

**Broiler breeds**:
Optimized for rapid meat production. Cornish Cross reaches 2.0-2.5 kg live weight at 6-8 weeks on 3.0-3.5 kg feed per kg of live weight. Rapid growth demands high-protein feed (21-24% protein starter, 18-20% grower) and careful management to prevent leg problems and heart failure. Not suitable for breeding — hybrid vigor does not persist in offspring. Heritage broiler alternatives (Dark Cornish, Delaware) grow more slowly (12-16 weeks to slaughter weight) but are self-reproducing and healthier on range.

**Dual-purpose breeds**:
Balanced for both eggs and meat. Rhode Island Red, Plymouth Rock, Orpington, Sussex, and Wyandotte hens produce 200-260 eggs per year while reaching 3-4 kg live weight — large enough for a respectable carcass at the end of their productive laying life (2-3 years). Dual-purpose breeds are the practical choice for self-sufficient settlements: a single flock provides ongoing eggs and periodic meat without maintaining separate layer and broiler breeding programs. Roosters of these breeds reach 3.5-4.5 kg.

### Housing and Coop Construction

**Coop dimensions**:
Allow 0.1-0.2 m² floor space per bird inside the coop and 4-6 m² per bird in outdoor runs. A flock of 20 hens requires a minimum 2-4 m² coop plus 80-120 m² outdoor run. Coop height: 1.5-2.0 m at the peak for human access during cleaning.

**Perches**:
Provide 20-25 cm of perch length per bird. Round or rectangular wooden dowels 4-5 cm diameter (or 4×6 cm with rounded edges). Position perches 60-90 cm above the floor with 30-35 cm horizontal spacing between perches. Chickens instinctively roost elevated at night to avoid ground predators. Smooth, rounded perches prevent foot injuries and bumblefoot infections. Place dropping boards 15-20 cm below perches for easier manure collection.

**Nest boxes**:
One nest box per 4-5 hens, dimensions 30 × 30 × 30 cm. Position nest boxes 60-90 cm above floor level in a dark, quiet area of the coop. Line with straw, wood shavings, or dried grass. Hens prefer enclosed, secluded nests — a simple wooden box with a sloped roof (to prevent roosting on top) and a 15 cm entrance opening works well. Collect eggs daily to discourage broodiness and egg-eating.

**Floor and bedding**:
Solid wood or concrete floor covered with 10-15 cm of deep litter (wood shavings, straw, or shredded leaves). Deep litter method: add fresh bedding material on top as needed, allowing manure and bedding to compost in place. The composting action generates heat and beneficial microbes that reduce odor and disease. Complete cleanout every 6-12 months yields valuable compost. Avoid wire floors — they cause foot deformities and do not provide the composting benefit.

**Ventilation**:
Critical for respiratory health. Ammonia from droppings causes respiratory disease above 25 ppm. Provide ventilation openings near the roofline (warm, ammonia-laden air rises) totaling at least 0.1 m² per 10 birds. Cover vents with hardware cloth (woven wire mesh with openings under 2.5 cm) to exclude predators while allowing airflow. Do not create drafts at perch level — chickens tolerate cold but not cold drafts on their combs and wattles.

**Predator protection**:
Woven wire mesh (hardware cloth) with openings under 2.5 cm on all windows, vents, and openings — chicken wire (2.5-5 cm hexagonal mesh) excludes chickens but not weasels, mink, or rats. Solid floor or buried wire apron: extend wire mesh 30 cm outward from the coop foundation, then bury it 15-20 cm deep, or pour a concrete slab floor. Raccoons, foxes, and dogs dig under coop walls. Automatic or manually operated pop door closes at dusk to prevent nocturnal predator access. Enclose outdoor run with wire mesh roof (hawks, owls) and buried wire apron along the perimeter.

### Feeding and Nutrition

**Layer feed requirements**:
100-150 g layer feed per day per hen, containing 16-18% protein, 3.5-4.0% calcium (essential for eggshell formation). Calcium supplementation: offer free-choice oyster shell or crushed limestone in a separate hopper — hens regulate their own calcium intake. Grit (small stones, 2-5 mm) must also be available free-choice for digestion since chickens have no teeth and rely on the gizzard to grind feed.

**Free-ranging and foraging**:
Free-ranging hens forage insects, seeds, worms, and greens, supplementing 20-40% of their dietary intake. Chickens consume 30-80 g of forage per day depending on pasture quality. Rotation of the flock through garden beds after harvest provides pest control and manure fertilization simultaneously. Stocking density for free-range: 4-6 m² per bird minimum; overstocking destroys vegetation and increases parasite load.

**Water**:
250-400 ml of clean water per bird per day, doubling in hot weather (above 30°C). Water deprivation for 12+ hours causes a measurable drop in egg production; 24-36 hours without water can trigger a complete molt and cessation of laying for weeks. Use nipple drinkers or gravity-flow bell drinkers to maintain cleanliness. Position waterers in shade during summer to prevent algae growth and heat stress.

**Feed storage**:
Store feed in rodent-proof containers (metal trash cans or sealed plastic barrels). Mice and rats consume and contaminate feed — a single rat eats 20-30 g of feed per day and spreads disease. Keep feed dry to prevent mold; aflatoxin from *Aspergillus flavus* mold is lethal to chickens at low concentrations.

### Brooding and Incubation

**Natural brooding**:
A broody hen sits on a clutch of 10-14 eggs for 21 days, leaving the nest briefly once or twice daily to eat, drink, and defecate. She turns the eggs, maintains incubation temperature, and protects the chicks after hatching. Heritage breeds (Cochin, Silkie, Orpington) go broody readily; commercial layers (Leghorn) have had broodiness bred out almost entirely. A broody hen is the simplest incubation method — no equipment required.

**Artificial incubation**:
Maintain incubator temperature at 37-38°C (37.5°C optimal) with 50-65% relative humidity for the first 18 days. Turn eggs 3-5 times daily (or use an automatic egg turner) to prevent the embryo from sticking to the shell membrane. Stop turning on day 18 and increase humidity to 65-70% for the final 3 days (hatching phase). Candling on day 7 and day 14 identifies infertile eggs (clear) and dead embryos (blood ring) for removal. Fertility rate: 85-95% from healthy breeding flock. Hatch rate from fertile eggs: 80-90% with proper incubation.

**Chick brooding (0-6 weeks)**:
Provide a heat source (brooder lamp or heat plate) maintaining 32-35°C in the first week, decreasing by 2-3°C per week until ambient temperature is reached at 5-6 weeks. Feed chick starter (18-21% protein) for the first 6-8 weeks. Provide clean water in shallow dishes to prevent drowning. Floor space: 250 cm² per chick initially, increasing as they grow. Mortality should be under 5% with proper management.

### Egg Production

**Laying cycle**:
Hens begin laying at 18-22 weeks of age. Peak production occurs at 26-30 weeks, with 90-95% of the flock laying daily. Production gradually declines 10-15% per year thereafter. A hen's ovary releases a yolk every 24-26 hours during active laying; the egg traverses the oviduct over 24-25 hours, receiving albumen, shell membranes, and a calcium carbonate shell.

**Molting**:
Annual feather renewal process, typically triggered by decreasing daylight in autumn. Hens stop laying for 6-12 weeks while redirecting protein to feather growth. Forced molting (withholding feed for 7-14 days) was a commercial practice to synchronize flock production — it is stressful and not recommended for small flocks. Allow natural molt; supplement protein during this period (20-22% feed or add sunflower seeds, peas, or mealworms).

**Light management**:
Hens require 14-16 hours of light per day to maintain egg production. In temperate latitudes, supplemental lighting in the coop during winter months (a single 5-10 watt LED bulb on a timer) maintains production. Never reduce daylight hours below 14 during the laying period. Light intensity: 10-20 lux at perch level (enough to read a newspaper).

**Egg collection and storage**:
Collect eggs daily, ideally twice daily in warm weather. Fresh unwashed eggs keep 2-3 weeks at room temperature (15-20°C) — the bloom (cuticle) on the shell protects against bacterial penetration. Washing removes the bloom; washed eggs must be refrigerated (4°C) and consumed within 2 weeks. For longer storage, coat eggs in food-grade mineral oil or waterglass (sodium silicate solution) to seal shell pores, extending shelf life to 6-12 months at cool temperatures.

### Meat Production

**Dressed carcass yield**:
70-75% of live weight after plucking and evisceration. A 2.0 kg live broiler yields approximately 1.4-1.5 kg dressed carcass. A 3.0 kg dual-purpose hen yields 2.1-2.3 kg dressed carcass. Broilers reach 2.0-2.5 kg at 6-8 weeks on intensive feed; heritage breeds reach the same weight at 12-16 weeks on range.

**Processing**:
Slaughter by cervical dislocation (small birds) or cone killing (insert head through a metal cone, sever the jugular vein and carotid artery with a sharp knife — unconsciousness within 10-15 seconds, death within 1-2 minutes from blood loss). Bleed for 2-3 minutes. Scald at 55-60°C for 30-60 seconds to loosen feathers, then pluck by hand or mechanical plucker. Eviscerate through a vent incision, removing intestines, crop, and trachea. Save liver, heart, and gizzard. Chill carcass in cold water (0-4°C) for 2-4 hours to set the meat.

**Feed conversion**:
Broilers: 1.5-1.8 kg feed per kg of live weight gain (highly efficient — among the best of any livestock). Layers: 2.0-2.5 kg feed per kg of egg mass. Dual-purpose on range: 2.5-3.5 kg feed per kg of live weight, supplemented by 20-40% foraged intake.

### Health and Disease

**Common diseases**:
- **Coccidiosis**: Protozoan parasite (*Eimeria* spp.) causing bloody diarrhea and weight loss in young birds. Prevent with clean dry litter and coccidiostat in feed (or allow controlled exposure to build immunity). Treat with amprolium in water.
- **Marek's disease**: Herpesvirus causing tumors and paralysis. Vaccinate chicks at day 1 (subcutaneous injection of live attenuated vaccine). Nearly 100% effective when properly administered. Without vaccination, mortality can reach 30-60% in infected flocks.
- **Newcastle disease**: Viral infection causing respiratory distress, neurological symptoms, and sudden death. Highly contagious. No treatment — prevention through biosecurity and vaccination where the disease is endemic.
- **Avian influenza**: Viral disease with strains ranging from low-pathogenic (mild respiratory symptoms) to highly pathogenic (rapid mortality up to 90-100%). Biosecurity: prevent contact with wild waterfowl (primary reservoir), quarantine new birds for 30 days, disinfect equipment between flocks.
- **Fowl pox**: Viral disease causing scabby lesions on comb, wattles, and skin. Transmitted by mosquitoes. Usually self-limiting with low mortality. Vaccine available.

**Parasites**:
- **Northern fowl mite**: Causes anemia, reduced egg production. Treat with permethrin dust or diatomaceous earth in dust baths.
- **Lice**: Flat, straw-colored insects on skin and feathers. Cause irritation and reduced production. Treat with dust baths containing wood ash and diatomaceous earth.
- **Intestinal worms** (roundworms, capillary worms, tapeworms): Cause weight loss and reduced egg production. Prevent by rotating pasture, keeping litter dry. Treat with fenbendazole or ivermectin (observe egg withdrawal period).

**Biosecurity measures**:
Quarantine new birds for 30 days before integrating with the flock. Disinfect coop and equipment between flocks. Limit visitor access to the coop area. Control rodents (rats carry disease and consume feed). Provide dust bathing areas (sand, wood ash, diatomaceous earth) for natural parasite control. Remove dead birds immediately and determine cause of death.

### Manure Management

Chicken manure is the highest-nitrogen common livestock manure at approximately 1.5% N, 1.0% P₂O₅, and 0.5% K₂O by fresh weight. Production rate: 0.05-0.1 kg per bird per day. Fresh chicken manure is too hot (high nitrogen) to apply directly to plants — it burns roots. Compost for 6-8 weeks with carbonaceous bedding material (straw, wood shavings, leaves) at a carbon-to-nitrogen ratio of 25-30:1. The deep litter system in the coop effectively pre-composts manure. After composting, apply at 2-5 kg per m² of garden bed as a complete fertilizer. A flock of 20 hens produces approximately 500-700 kg of compost-ready manure per year.

### Cross-Domain Links

- **[Beekeeping](beekeeping.md)** — complementary pollination and honey-wax production
- **[Domestication](domestication.md)** — species domestication history and breed development
- **[Farming](../agriculture/index.md)** — chicken manure as fertilizer, pest control in crop rotations
- **[Food Preservation](../food-processing/index.md)** — egg storage, meat curing, and preservation

### Safety

**Pathogen handling**:
Raw chicken meat commonly carries *Salmonella* and *Campylobacter* bacteria. Wash hands thoroughly after handling live chickens, raw meat, or eggs. Cook chicken to an internal temperature of 74°C to kill pathogens. Clean and disinfect processing surfaces and tools after butchering. Do not wash raw chicken under running water — this splashes bacteria up to 50 cm in all directions.

**Rooster aggression**:
Roosters defend their flock and may attack humans, especially during breeding season. Spurring (sharp leg spurs) and pecking can cause significant injury. Manage aggressive roosters by never turning your back, carrying a shield (piece of cardboard or a rake), and culling persistently aggressive individuals. A good rooster alerts the flock to aerial predators and maintains flock order without attacking his keeper.

**Dust and respiratory protection**:
Poultry dust (feather dander, dried manure, bedding particles) causes respiratory irritation and can carry bacteria. Wear a dust mask when cleaning the coop. Ventilation in the coop is the primary control measure. Histoplasmosis (fungal infection from soil enriched with bird droppings) is a risk when cleaning accumulations of old manure — wear respiratory protection and wet down dry material before disturbance.

### Production Metrics

**Egg production benchmarks**: Modern hybrid layers (Leghorn-derived) produce 280-320 eggs per year at peak, consuming 100-130 g of feed per day (2.0-2.2 kg feed per kg of egg mass). Heritage dual-purpose breeds produce 200-260 eggs per year at 110-150 g feed per day (2.5-3.0 kg feed per kg of egg mass). Egg weight progression: pullets (first-year hens) lay 48-54 g eggs; second-year hens lay 58-65 g eggs; third-year hens lay 62-70 g eggs with declining frequency. Annual egg mass per hen: 15-18 kg (hybrids) or 12-15 kg (heritage). At $0.40-0.60 per kg feed, each dozen eggs costs $0.80-1.20 in feed. A flock of 25 hens produces 5,000-7,500 eggs per year (approximately 300-450 kg of egg mass), generating $750-2,500 in annual retail value at $3-5 per dozen.

**Meat production benchmarks**: Cornish Cross broilers reach 2.5 kg live weight at 42-49 days on 4.5-5.0 kg of feed (FCR 1.6-1.8). Heritage breeds (Delaware, Wyandotte) reach 2.0-2.5 kg at 84-112 days on 6-8 kg of feed (FCR 2.5-3.5). Dressed yield: 70-75% of live weight. A batch of 25 Cornish Cross broilers produces 44-47 kg of dressed carcass from 110-125 kg of feed in 6-7 weeks. Annual production potential from a breeding flock of 5 hens and 1 rooster: 60-80 chicks hatched (assuming 6-8 clutches of 10-12 fertile eggs with 80-85% hatch rate), yielding 84-100 kg of dressed chicken at 1.2-1.3 kg each at 12-16 weeks.

### Regional Adaptations

Chickens adapt to virtually every inhabited climate on Earth, from equatorial tropics to subarctic homesteads. In hot climates (above 35°C), chicken feed intake drops 10-20% and eggshell quality deteriorates (thinner shells, more cracks) — providing shade, misters, or wet feed restores 80-90% of normal production. Lightweight breeds (Leghorn, Ancona) with large combs and wattles radiate heat more efficiently and tolerate heat 3-5°C better than heavy breeds. In cold climates (below -10°C), large single combs suffer frostbite at temperatures below -12°C; rose comb and pea comb breeds (Wyandotte, Brahma, Ameraucana) are hardier. Supplemental lighting (14-16 hours total per day using a single 5-10 watt LED bulb on a timer) prevents the 40-60% egg production decline that occurs naturally from November through February at latitudes above 40°N. Deep litter bedding (30-40 cm) in the coop generates composting heat that raises coop temperature 5-10°C above ambient. Free-ranging hens in temperate climates forage 20-40% of their diet from insects and vegetation during spring through autumn; this drops to under 5% during winter when snow cover eliminates ground forage.

### Historical Development

Chickens descend from the red junglefowl (*Gallus gallus*) of Southeast and South Asia, domesticated approximately 8,000-10,000 years ago. The earliest undisputed chicken bones come from northern China (5400 BCE), with additional early sites in Pakistan (Mehrgarh, 4000 BCE) and Thailand (Ban Non Wat, 2000 BCE). Initial domestication was likely for cockfighting and religious purposes rather than food — egg and meat production were secondary benefits. Dispersal to Europe occurred via two routes: overland through Central Asia and the Caucasus (reaching Greece by 800 BCE) and maritime through the Indian Ocean to East Africa and the Mediterranean. The Roman Empire developed the first intensive poultry systems, including artificial incubation using warmed clay ovens capable of hatching 10,000+ chicks simultaneously. Selective breed development accelerated in 19th-century Europe and North America — the first poultry exhibition (London, 1845) showcased dozens of standardized breeds. Modern hybrid layer and broiler lines were developed in the 1940s-1960s through crossing genetically distinct inbred lines, creating birds that outperform purebreds by 20-40% through heterosis (hybrid vigor). For bootstrapping, a founding flock of 10 hens and 2 roosters of a dual-purpose breed (Rhode Island Red, Plymouth Rock, or Sussex) provides 2,000-2,600 eggs and 40-60 kg of dressed chicken in the first year, with self-sustaining reproduction producing 60-100 chicks per year from the second year onward.

### Nutritional Requirements

**Protein requirements by age**: Chicks require 20-24% crude protein in starter feed (0-6 weeks), decreasing to 16-18% in grower (6-12 weeks), and 15-16% in layer ration (16+ weeks). Broilers need higher sustained protein: 23-24% starter (0-3 weeks), 20-21% grower (3-6 weeks), 18-19% finisher (6-8 weeks). Protein deficiency below 14% causes reduced growth, poor feathering, and a 30-50% drop in egg production within 7-10 days. The limiting amino acid for poultry is methionine — supplement at 0.3-0.5% of diet using fish meal (2.3% methionine), sunflower seeds (0.6%), or synthetic DL-methionine. A basic all-grain ration of 50% cracked corn, 25% wheat, 20% peas or soybean meal, and 5% supplement (oyster shell, grit, mineral mix) provides approximately 16-18% protein suitable for layers.

**Calcium and vitamin requirements**: Each egg shell contains 2.0-2.5 g of calcium carbonate, deposited during 18-20 hours of shell formation — the hen mobilizes 10-15% of her total skeletal calcium for each egg. Laying hens require 3.5-4.0% dietary calcium, provided as free-choice oyster shell (38% calcium) or limestone (33-38% calcium) in particles of 2-5 mm diameter. Vitamin D3 (cholecalciferol) at 3,000-4,000 IU per kg of feed is essential for calcium absorption — deficiency produces thin-shelled eggs, reduced lay rates, and skeletal deformity (rickets in growing birds). Free-range hens obtain vitamin D from sunlight exposure (15-30 minutes of direct sun on unfeathered skin synthesizes adequate D3), but confined hens require dietary supplementation.

### Processing and Products

**Egg grading and storage**: Grade AA eggs have a thick, firm albumen (white height above 6 mm when measured with a micrometer on a flat glass plate), a centered, firm yolk, and a clean, unbroken shell. Grade A allows slightly thinner whites (4-6 mm height). Fresh egg specific gravity (measured by float test in salt water solutions): eggs that sink in 1.025 SG water are under 3 days old; eggs that float in 1.080 SG water are over 21 days old. Storage at 4°C extends grade A quality from 7-10 days (room temperature) to 4-6 weeks. Waterglass preservation (sodium silicate, 1:10 ratio with water) extends storage to 6-12 months at 10-15°C.

**Chicken meat processing**: Slaughter weight of 2.0-2.5 kg yields a 1.4-1.9 kg dressed carcass (70-75% dressing percentage). Carcass breakdown: breast (25-30% of carcass), thighs (18-22%), drumsticks (12-15%), wings (10-12%), back and neck (15-18%), and giblets (5-7%). A processed broiler provides 4-6 servings of meat. Rendering fat from abdominal fat pads and skin yields 100-200 g of chicken fat per bird (schmaltz), with a smoke point of 185°C and a distinctive flavor valued in traditional cooking. Bones simmered for 8-12 hours produce 1.5-2.0 L of bone broth containing 6-10 g of protein per 100 mL and significant quantities of collagen, glycine, and minerals (calcium, phosphorus, magnesium).

**Feather and byproduct utilization**: A processed chicken yields 80-120 g of feathers (90% keratin protein), usable as insulation in bedding or, when hydrolyzed under pressure (140°C, 30-60 minutes), as a slow-release nitrogen fertilizer (12-14% N) applied at 50-100 g per m². Blood (30-50 mL per bird, 16-18% protein) is collected at slaughter for blood sausage or dried as blood meal (80-85% protein, 12-13% nitrogen) — an extremely fast-acting nitrogen fertilizer. Chicken feet (40-60 g each) are edible and produce excellent broth; heads and intestines are fed to other livestock or composted.

### Health Management Calendar

**Vaccination schedule**: Marek's disease vaccine administered subcutaneously (0.2 mL) at day 1 in the hatchery or brooder — this herpesvirus vaccine is nearly 100% effective at preventing tumor formation when given before exposure. Newcastle disease and infectious bronchitis vaccine: first dose at 10-14 days via eye drop or drinking water, booster at 4-6 weeks. Fowl pox vaccine: wing web stab at 6-8 weeks. Laryngotracheitis vaccine (where endemic): eye drop at 4-6 weeks. Coccidiosis prevention: anticoccidial medication in starter feed (lasalocid, monensin, or salinomycin) for the first 12-16 weeks, or controlled exposure through litter contact to build natural immunity. Vaccination costs approximately $0.05-0.15 per bird for the full schedule — one of the highest-return investments in poultry management, preventing losses of 30-60% in unvaccinated flocks.

**Parasite control schedule**: External parasites (northern fowl mite, chicken lice) are controlled by providing dust bathing areas (a shallow bin of 50% sand, 30% wood ash, 20% diatomaceous earth, measuring 30 × 30 × 15 cm) accessible at all times; birds dust bathe 2-3 times weekly for 10-20 minutes each session. Internal parasites (roundworms, capillary worms, tapeworms) are treated with fenbendazole (5 mg/kg body weight in feed for 5 consecutive days) or ivermectin (0.2 mg/kg, single dose orally) at the start and end of the outdoor grazing season. Observe a 7-14 day egg withdrawal period after any anthelmintic treatment. Pasture rotation (moving chickens to fresh ground every 3-5 years for the same species, or alternating with crops) breaks parasite life cycles — most poultry nematode larvae die within 6-12 months without a host.

**Seasonal management**: Spring (March-May): introduce replacement pullets, begin pasture access when grass reaches 10-15 cm, increase nesting box availability. Summer (June-August): provide shade and extra water (consumption doubles above 30°C), collect eggs twice daily to prevent heat spoilage, monitor for fly populations. Autumn (September-November): cull spent hens (those that have completed their second laying season), process surplus roosters, deep-clean and lime-wash the coop, stockpile feed for winter. Winter (December-February): install supplemental lighting (14-16 hours total, using a timer on a 5-10 watt LED bulb), add extra bedding (build deep litter to 20-30 cm for composting heat), prevent water from freezing (heated waterers or twice-daily replacement), reduce ventilation to balance moisture removal with heat retention.

### Economic Analysis

**Cost of production**: A small-scale layer operation of 25 hens incurs annual costs of approximately $200-350: feed ($150-250 at $0.40-0.60 per kg, 5-7.5 kg per hen per day), bedding ($10-20), supplemental calcium and grit ($5-10), replacement pullets ($30-60 at $3-6 each for 10 birds). Revenue from egg sales: 5,000-7,500 eggs per year at $0.20-0.50 each ($1,000-3,750). Net annual profit: $650-3,400 depending on market and management. A broiler batch of 25 birds incurs costs of $75-135 (chicks at $2-3 each, feed at $45-60, processing supplies $5-10) and produces 35-47 kg of dressed chicken valued at $175-470 at $5-10 per kg. Return on investment: 2-4× per batch, with 4-6 batches possible per year in a continuous production system.

**Self-sufficiency calculations**: A family of 4-6 people requires approximately 700-1,000 eggs and 100-150 kg of chicken meat per year for adequate protein intake. This requires a laying flock of 10-15 hens producing 200-250 eggs each (2,000-3,750 eggs total) and 4-6 batches of 10-15 broilers annually (40-90 birds, producing 56-135 kg dressed meat). Feed requirement: 2,000-3,500 kg of layer feed plus 250-600 kg of broiler feed per year. A 0.2-hectare grain plot producing 2,000-3,000 kg of corn or wheat per year at 4-6 tonnes per hectare provides roughly 50-70% of total poultry feed from on-farm production, with protein supplementation (soybeans, peas, or insects) making up the deficit.

**Flock reproduction calculations**: A breeding flock of 8 hens and 2 roosters (heritage dual-purpose breed) produces 72-96 fertile eggs per clutch (assuming 9-12 eggs per hen × 8 hens, 85-90% fertility rate). Incubation hatch rate of 80-90% yields 58-86 chicks per clutch. Three natural hatches per year (spring, summer, early autumn) produce 174-258 chicks annually — sufficient to maintain the laying flock (replace 8-10 hens per year), produce 100-150 broilers for meat, and retain 30-50 surplus birds for sale or trade. This self-sustaining reproduction rate makes chickens the most demographically productive livestock species per unit of feed and management input.

### Housing Design Specifications

**Coop construction details**: A well-built coop for 25 hens measures 3.0 × 2.5 m (7.5 m² floor area) with 1.8 m ceiling height at the peak. Frame: 50 × 100 mm timber posts at 60 cm spacing, sheathed with 20 mm tongue-and-groove boards or 12 mm plywood. Roof: corrugated galvanized steel or cedar shingles on 25 × 50 mm rafters at 60 cm spacing, with 20-30° pitch. Floor: pressure-treated 25 mm boards on 50 × 100 mm joists at 40 cm spacing, or concrete slab (100 mm thick over compacted gravel). Insulation (for cold climates): 50 mm rigid foam between studs, covered with 6 mm plywood interior sheathing. Two windows (30 × 40 cm) on the south wall with hardware cloth and hinged shutters. Pop hole: 30 × 30 cm on the east wall with a sliding door operated by cord from outside.

**Nest box bank**: Four nest boxes arranged in a 2 × 2 bank, each 30 × 30 × 30 cm, mounted 60-90 cm above floor level. Construction: 12 mm plywood with a 15 × 20 cm entrance opening, sloped top (15° pitch to prevent roosting on top), and a hinged back panel for egg collection from outside the coop. Fill with 8-10 cm of straw or wood shavings; replace when soiled. Total nest box cost: $15-25 in materials. One nest box per 5-6 hens minimizes competition and reduces egg breakage from overcrowding.

**Roosting bar specifications**: Three parallel roosting bars (4 × 6 cm with rounded top edges, 90 cm long) mounted 60-70 cm above the floor with 30-35 cm horizontal spacing. Capacity: 20-25 hens at 20-25 cm perching space per bird. Material: hardwood (oak, maple) for durability; softwood (pine) splinters and harbors mites. A dropping board (60 × 90 cm sheet metal or smooth plywood) mounted 15 cm below the roosts collects 60-70% of nighttime droppings for easy removal — scrape daily into the compost pile. The remaining 30-40% falls to the deep litter floor.
**Run and fencing**: An enclosed outdoor run of 80-120 m² for 25 hens (3.2-4.8 m² per bird) is fenced with 1.5 m tall woven wire (5 × 10 cm mesh) with a hardware cloth apron (30 cm above ground + 30 cm buried outward) to exclude digging predators. Top: wire mesh or bird netting to exclude hawks and owls. A movable run (chicken tractor: 1.2 × 2.4 m frame covered with wire mesh, moved daily to fresh ground) allows pasture rotation without permanent fencing — one tractor accommodates 8-12 hens and fertilizes 1,000-1,500 m² of garden per year when moved daily. Shade structures (tarp or corrugated metal on a 1.5 m high frame) in the run prevent heat stress — chickens die at internal temperatures above 46°C and reduce egg production above 30°C.

**Feed and water infrastructure**: A gravity-feed PVC pipe feeder (5 cm diameter pipe, 60 cm long, with 3-4 cm feeding holes cut at 8 cm intervals along the bottom 30 cm) holds 1.5-2.0 kg of feed and feeds 8-12 hens for 2-3 days. Cost: $5-10 in materials. Water: a 5-gallon (19 L) bucket with 4-6 poultry nipple drinkers screwed into the bottom, suspended at 30-40 cm height, provides clean water for 20-25 hens for 3-4 days. The nipple system eliminates spillage and contamination that open waterers suffer, reducing waterborne disease incidence by 50-70%. One bucket refill per week (in moderate weather) or every 3-4 days (in hot weather above 30°C) is sufficient.
Deep litter management produces 200-400 kg of compost per year from a 25-hen coop — valuable enough as fertilizer to offset 30-50% of total flock feed costs when applied to intensive vegetable production at 3-5 kg per m². Combined with the 2,000-3,750 eggs and 40-100 kg of dressed meat, a well-managed small flock provides one of the highest returns on investment of any agricultural enterprise available to a bootstrapping settlement.
The deep litter method deserves special attention: when managed correctly (adding 2-3 cm of fresh pine shavings or straw weekly, keeping the litter slightly damp but not wet, and allowing the birds to scratch and aerate it), the bedding-manure mixture composts in place, reaching 40-50°C internally and supporting beneficial bacteria that suppress pathogens. After 6-12 months, a complete cleanout yields 100-200 kg of finished compost with an NPK analysis of approximately 1.5-0.8-0.5, suitable for direct garden application without additional composting.
Chickens are, without question, the single most important livestock species for a bootstrapping settlement — they offer the fastest return on investment, the lowest barriers to entry, and the broadest range of products (eggs, meat, feathers, manure, pest control) from any single species in the animal domain. Every settlement should establish chickens as its first livestock priority within the first year.
Each additional 10 hens beyond a household's needs produces surplus eggs worth $300-600 annually in barter or market value — making even a modest flock a viable income generator alongside its primary food security role. The combination of rapid reproduction, low feed costs, minimal space requirements, and high product diversity makes chickens the single most efficient converter of grain and forage into human food among all domesticated animals.
The hen-to-human ratio for self-sufficiency is approximately 2-3 hens per person for eggs alone, or 3-5 hens per person for eggs plus periodic meat from culling spent hens and surplus roosters. A community of 50 people requires a flock of 100-250 hens housed in 10-50 m² of coop space, consuming 10-38 kg of feed daily, and producing 20,000-75,000 eggs per year.
A well-managed 25-hen flock also produces 500-700 kg of nitrogen-rich manure per year, fertilizing 100-350 m² of intensive vegetable production and closing the nutrient loop between livestock and crop production in the settlement food system.
This integration of egg, meat, and fertilizer production from a single species with minimal infrastructure makes chickens the cornerstone of any settlement's livestock strategy.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Animals](./index.md) • [All Domains](../index.md)*
