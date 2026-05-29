# Livestock Domestication & Husbandry

> **Node ID**: animals.domestication
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`foundations.tools-basic`](../foundations/tools-basic.md), [`foundations.food-agriculture`](../foundations/food-agriculture.md)
> **Enables**: [`animals.animal-materials`](animal-materials.md), [`animals.cattle`](cattle.md), [`animals.draft-power`](draft-power.md), [`animals.equines`](equines.md), [`animals.goats`](goats.md), [`animals.insect-farming`](insect-farming.md), [`animals.pest-management`](pest-management.md), [`animals.pigs`](pigs.md), [`animals.sericulture`](sericulture.md), [`animals.sheep`](sheep.md)
> **Timeline**: Years 1-30+
> **Outputs**: livestock, breeding_stock, manure, dairy, meat, eggs
> **Critical**: Yes — foundation node enabling all livestock and poultry species

## Problem

Domestication converts wild fauna into reliable, renewable sources of labor, food, fiber, and materials. Before domestication, humans rely entirely on hunting and gathering — protein intake is unpredictable, labor is limited to human muscle, and fiber comes only from wild plants. Domesticated animals provide continuous output: daily milk, annual fleece, seasonal offspring, steady draft power, and manure that sustains crop yields. A single dairy cow produces 3,000–6,000 liters of milk per year — equivalent to the protein from dozens of wild game animals, without the uncertainty of the hunt.

Without livestock you cannot plow: hand-digging limits farms to 0.5–1 hectare per family; ox-plowed farms reach 5–10 hectares. You cannot produce milk or dairy — the most efficient conversion of pasture to human-edible calories. You cannot source wool or leather from managed herds (hunt-based supply is seasonal and unreliable). You cannot maintain soil fertility — without manure, yields decline 2–5% per year under continuous cropping. You cannot produce eggs — the highest feed-to-protein conversion ratio of any food animal. You cannot transport goods beyond human carrying capacity. Without livestock, settlements remain small, farms remain limited, and surplus production is impossible.

Domestication is not a one-time event. It requires continuous daily management — feeding, watering, health monitoring, breeding, shelter maintenance — for the lifetime of the herd. A dairy cow produces for 5–10 lactations but needs milking every day during each 305-day lactation. Sheep need shearing annually. Fences need repair after every storm. This daily obligation is the price of the steady output that livestock provide.

## Prerequisites

- **Materials**: [Fencing materials](../construction/index.md) (timber posts, split rails, or stone for walls), [straw bedding](../plants/fiber-plants.md) (2–5 kg/day per large animal), [stored hay or silage](../foundations/food-agriculture.md) (1.2–1.8 tonnes per cattle beast for 120-day winter), [grain](../foundations/food-agriculture.md) for working animals and supplements (oats, barley, corn), [clean water](../foundations/index.md) source (40–80 L/day per cattle beast, 4–10 L/day per sheep)
- **Tools**: [Axes and saws](../machine-tools/index.md) for fence construction, [rope and harness](../textiles/rope-making.md) for leading and restraint, [pitchforks and wheelbarrows](../machine-tools/index.md) for mucking, [milking equipment](./index.md) (pails, stools, udder cloths), [ear tags or notching tools](./index.md) for identification, [hoof trimmers](./index.md) and [shears](./index.md) for sheep
- **Knowledge**: Animal behavior and flight zone (understanding stress-free handling), breeding cycles and estrus detection for each species, nutritional requirements by life stage (growth, lactation, pregnancy, work), common diseases and vaccination schedules, pasture management and rotational grazing principles
- **Infrastructure**: Secure fencing (post-and-rail, stone wall, or hedgerow — minimum 1.2 m for cattle, 1.0 m for sheep), shelter with dry bedding and ventilation, clean water delivery (troughs or piped spring), feed storage (hay barn, grain silo, or rodent-proof bins), quarantine enclosure at least 15 m from main herd

## Bill of Materials — Minimum Viable Homestead Livestock (5 species)

| Item | Specification | Quantity | Notes |
|------|--------------|----------|-------|
| Breeding cattle (1 bull + 3 cows) | 400–800 kg each, mixed ages | 4 head | 283-day gestation; first calves at 2–3 years |
| Breeding sheep (1 ram + 6 ewes) | 80–120 kg each | 7 head | 147-day gestation; twins are the management target |
| Breeding goats (1 buck + 3 does) | 30–80 kg each | 4 head | 150-day gestation; 2–3 kids per birth common |
| Breeding pigs (1 boar + 2 sows) | 150–250 kg each | 3 head | 114-day gestation; 8–12 piglets per litter |
| Laying hens (hens + 1 cockerel per 10) | 1.5–4.5 kg each | 20 hens + 2 cockerels | 200–300 eggs/hen/year; replace flock every 2–3 years |
| Fencing (post-and-rail) | Timber posts + split rails, 1.2–1.5 m high | 400–600 m | Encloses ~1 hectare at 400 m perimeter; add internal divisions for rotation |
| Winter hay | Sun-dried at early heading, baled or loose | 8–12 tonnes | 3 cattle × 1.5 t + 7 sheep × 0.4 t + 4 goats × 0.3 t + 15% buffer |
| Grain supplement | Oats, barley, or cracked corn | 500–1000 kg | For working oxen, lactating cows, and poultry through winter |
| Shelter (3-sided shed) | Timber frame, thatch or shingle roof, 3–4 m² per cattle beast | 50–60 m² floor area | Separate areas for cattle, small ruminants, and poultry |
| Water trough | Wood or stone, 100–200 L capacity | 2–3 units | Clean, fresh water daily; freeze-proof in winter |

### Overview

Animal domestication converts wild fauna into reliable, renewable sources of labor, food, fiber, and materials. Fifteen primary farmed species — eight mammalian livestock, seven poultry, plus insects — form the core of any pre-industrial animal husbandry system. Each fills a distinct niche in the settlement ecology, from traction power and milk production to waste conversion and pest control.

This article covers the shared foundations of livestock husbandry: housing, feeding, breeding, health, and safety. Individual species details live in dedicated articles linked below and in the comparison table.

Domestication begins with capture of wild or feral stock, progresses through taming and controlled breeding, and matures into managed herds with deliberate selection for productivity. The process spans years. Cattle and horses require 3-5 years from capture to first useful offspring; chickens and rabbits breed fast enough to establish productive flocks within a single season. Manure from all species closes the nutrient loop back to agriculture, making livestock indispensable for sustained crop yields.

Minimum viable startup: 2 breeding pairs per species, secure fencing, stored winter feed for 120 days, and a clean water source delivering at least 40 liters per large animal per day.

Initial capture and taming follows different strategies by species. Wild cattle and horses are driven into corrals (gradually constructed fences narrowing toward a pen). Sheep and goats are gathered from wild flocks using dogs or human drives during seasonal migrations. Pigs are trapped or their young are taken from wild sows. Chickens are lured with grain into cage traps. Taming requires daily calm contact over weeks. Young animals tame faster: a calf handled daily from birth becomes docile within a month; a wild-caught adult cow may take 6-12 months to accept handling. Food conditioning (grain, salt) accelerates trust in all species.

A comparison of the fifteen primary farmed species across the metrics that matter most for settlement planning:

| Species | Weight (kg) | Gestation (days) | Feed DM (kg/day) | Water (L/day) | Housing (m²) | Slaughter Age | Article |
|---------|-------------|-------------------|-------------------|---------------|--------------|---------------|---------|
| Cattle | 400-800 | 283 | 25-35 | 40-80 | 15-25 | 18-24 mo | [Cattle](cattle.md) |
| Bison | 400-900 | 270 | 25-35 | 40-80 | 15-25 | 18-24 mo | [Bison](bison.md) |
| Sheep | 80-120 | 147 | 1.5-3.0 | 4-10 | 2-4 | 4-6 mo | [Sheep](sheep.md) |
| Goats | 30-80 | 150 | 1.5-3.0 | 4-8 | 2-4 | 4-6 mo | [Goats](goats.md) |
| Pigs | 150-300 | 114 | 2.5-4.0 | 8-15 | 4-8 | 5-7 mo | [Pigs](pigs.md) |
| Horses | 400-700 | 335 | 10-20 | 30-50 | 15-25 | N/A (work) | [Equines](equines.md) |
| Donkeys | 180-450 | 365 | 5-10 | 15-25 | 10-15 | N/A (work) | [Equines](equines.md) |
| Camelids | 130-200 | 345 | 3-5 | 8-15 | 6-10 | N/A (fiber) | [Camelids](camelids.md) |
| Rabbits | 3-5 | 31 | 0.15-0.25 | 0.3-0.5 | 0.5-1.0 | 10-12 wk | [Rabbits](rabbits.md) |
| Chickens | 1.5-4.5 | 21 (inc.) | 0.1-0.15 | 0.25-0.4 | 0.05 (perch) | 6-16 wk | [Chickens](poultry-chickens.md) |
| Coturnix Quail | 0.1-0.2 | 17 (inc.) | 0.02-0.03 | 0.05 | 0.02-0.05 | 6-8 wk | [Coturnix](poultry-coturnix.md) |
| Ducks | 2-5 | 28 (inc.) | 0.12-0.2 | 0.5-1.0 | 0.5-1.0 | 7-10 wk | [Ducks](poultry-ducks.md) |
| Geese | 4-10 | 28-30 (inc.) | 0.15-0.3 | 0.5-1.0 | 2-5 | 12-20 wk | [Geese](poultry-geese.md) |
| Turkeys | 4-15 | 28 (inc.) | 0.15-0.4 | 0.5-1.0 | 20+ (range) | 16-24 wk | [Turkeys](poultry-turkeys.md) |
| Guinea Fowl | 1.2-1.6 | 26-28 (inc.) | 0.03-0.08 | 0.2-0.4 | Free range | 12-16 wk | [Guinea Fowl](poultry-guinea-fowl.md) |
| Pigeons | 0.35-0.8 | 17 (inc.) | 0.03-0.05 | 0.05-0.1 | 0.2 (loft) | 26-30 days | [Pigeons](poultry-pigeons.md) |

### Species Articles

**[Poultry](poultry.md)** (overview: [Poultry Farming](poultry.md)): [Chickens](poultry-chickens.md) · [Coturnix Quail](poultry-coturnix.md) · [Ducks](poultry-ducks.md) · [Geese](poultry-geese.md) · [Turkeys](poultry-turkeys.md) · [Guinea Fowl](poultry-guinea-fowl.md) · [Pigeons & Squab](poultry-pigeons.md)

**Livestock**: [Cattle](cattle.md) · [Sheep](sheep.md) · [Goats](goats.md) · [Pigs](pigs.md) · [Equines (Horses & Donkeys)](equines.md) · [Camelids](camelids.md) · [Bison](bison.md) · [Rabbits](rabbits.md)

**Insects**: [Insect Farming / BSF](insect-farming.md)

Several regionally critical species are not covered in dedicated articles because they require specific climate conditions unavailable to most settlements. Camels (*Camelus dromedarius* and *C. bactrianus*) thrive in arid regions, providing milk, meat, transport, and fiber. Water buffalo (*Bubalus bubalis*) are indispensable for rice paddy cultivation in tropical Asia. Yaks (*Bos grunniens*) provide all essentials at high altitude (3,000-5,000 m) on the Tibetan Plateau and Himalayan regions. Reindeer (*Rangifer tarandus*) sustain Arctic and sub-Arctic peoples with meat, milk, hides, and transport. These species are regionally critical but require specific climate conditions not available to most settlements.

### Housing Requirements

Shelter design varies by climate, but core principles hold everywhere: protection from wind and precipitation, adequate ventilation without drafts, dry bedding, and secure containment.

**Structure**: Timber-frame construction with wattle-and-daub infill or stone walls. Roof: thatch (rye straw, reed) or wooden shingles. Earthen floors with 10-20 cm of bedding material are standard. Drainage: slope floors 2-3% toward a drainage channel to carry urine and wash water out. For a 10-annel cattle byre, dimensions run roughly 6 × 30 m with a central feed aisle 1.5-2.0 m wide and stalls on each side. Roof pitch 20-30° for thatch, steeper sheds snow in cold climates.

**Bedding**: Straw (wheat, oat, barley) at 2-5 kg/day per large animal. Wood shavings or sawdust work where timber is plentiful. Peat moss absorbs 8-10 times its weight in liquid. Replace soiled bedding daily in tie stalls; deep-litter systems add fresh material weekly and muck out every 4-6 weeks. Composted manure and bedding, stacked for 6-12 months, produces stable fertilizer safe for direct field application.

**Ventilation**: Ridge vents or gap along the roof peak allow warm, moist air to escape. Eave gaps on both walls provide intake. Minimum ventilation rate: 4-6 air changes per hour for mature cattle. Ammonia must stay below 25 ppm. Sulfur dioxide from any combustion heating must be zero. In cold climates, balance ventilation against heat loss: under-ventilated barns condense moisture on walls and ceilings, rotting timber and promoting respiratory disease.

**Fencing types and construction**:
- **Post-and-rail**: Timber posts 10-15 cm diameter, set 60-80 cm deep in earth or concrete, spaced 2.5-3.0 m apart. Two to three horizontal rails of split timber (8-10 cm diameter) nailed or mortised to posts. Height 1.2-1.5 m for cattle and horses. Lifespan 10-20 years depending on wood species (oak and chestnut resist rot longest).
- **Woven wire**: Galvanized steel mesh (no stone-age substitute; use post-and-rail or hedges until wire is available). Mesh size 8-10 cm for sheep and goats, height 1.0-1.2 m. Add a single strand of barbed wire at 0.8 m height to deter cattle from leaning over.
- **Stone wall**: Dry-laid or mortared fieldstone, 1.0-1.2 m high, 0.5-0.6 m thick at base tapering to 0.3-0.4 m at top. Permanent, requires no maintenance, but labor-intensive to build. A single skilled waller builds 3-5 m of wall per day.
- **Hedgerow**: Hawthorn, blackthorn, or osage orange planted in a double row 30-40 cm apart. Saplings spaced 20-30 cm within each row. Takes 5-8 years to form an impenetrable barrier, then requires annual trimming to maintain density. Provides windbreak, wildlife habitat, and occasional fruit or nuts.

### Feed and Water

**Pasture carrying capacity**: Fertile lowland pasture supports 2-3 cattle or 10-15 sheep per hectare during the growing season. Hill pasture supports half that. Rotational grazing (move animals every 3-5 days to fresh paddock) increases utilization 20-30% compared to continuous grazing and reduces parasite loads.

**Hay for winter**: A 500 kg cattle beast consumes 10-15 kg hay/day through a 120-day winter. That is 1.2-1.8 tonnes of hay per animal per winter. Square bales at 20-25 kg each mean 50-90 bales per animal. Cut hay at early heading stage (before seed set) for maximum protein content (10-14% crude protein vs. 6-8% for mature cut).

**Fodder crops**: Turnips, mangels (fodder beet), and kale provide winter feed that can be grazed in situ or lifted and stored. Yield: 40-80 tonnes/ha for fodder beet. Oats and barley grown for grain produce straw as a secondary feed. Root crops are especially valuable because they stay in the ground through frost and can be lifted as needed through winter, avoiding storage losses. A hectare of fodder beet feeds 4-5 cattle through a 120-day winter.

**Silage**: Fermented chopped forage stored airtight (clamp silage: pit in ground, lined with clay, packed with chopped green material, covered with earth). pH drops to 3.8-4.5 through lactic acid fermentation, preserving feed for up to 2 years. Provides higher nutritional value than hay when made from leafy material cut early. A 500 kg cow eats 20-30 kg silage/day. Silage making requires airtight conditions; exposure to air causes mold and spoilage within days.

**Grain supplementation**: Working oxen need 2-4 kg grain/day (oats, barley, or cracked corn). Lactating dairy cows benefit from 3-5 kg/day. Poultry require grain as a dietary base (100-150 g/day). Horses in medium work need 2-5 kg/day. Sheep and goats on good pasture need grain only in late pregnancy. Over-feeding grain to ruminants causes acidosis (rumen pH drops below 5.5, causing bloat, lameness, and death). Introduce grain gradually over 10-14 days, never exceed 50% of dry matter intake.

**Water**: Clean water is non-negotiable. Contaminated water spreads leptospirosis, giardiasis, and coccidiosis. Troughs or natural water sources must be accessible within 500 m of grazing. Flow rate from a spring or well should exceed peak demand (morning and evening drinking). A trough for 20 cattle needs to deliver 400 L/hour during peak drinking times. Freeze-proof troughs (wooden box with stones at the base that can be heated) or twice-daily bucket delivery in freezing weather. Snow is not an adequate water source; animals lose body heat melting it and intake is unreliable.

### Breeding

**Selection criteria**: Choose breeding stock for conformation (sound legs, deep body, well-attached udder), temperament (docile animals are safer and more productive), and proven productivity (milk records, fleece weight, litter size). Cull animals that fail to meet thresholds. Maintain detailed records: birth dates, parentage, production metrics, health events. Ear notches or brand marks identify individuals when paper records are impractical.

**Estrus detection and breeding seasonality**: Cattle cycle year-round every 21 days (standing heat lasts 12-18 hours, observable by mounting behavior and clear vaginal mucus). Sheep and goats are seasonal breeders, cycling only during shortening daylight (autumn): sheep every 16-17 days, goats every 18-21 days. Sows cycle every 21 days year-round, with heat lasting 48-72 hours (characterized by standing reflex when pressure applied to the loin). Mares cycle every 21 days from spring through autumn, with estrus lasting 4-7 days. Chickens do not cycle; hens lay regardless of mating, and fertilized eggs develop only under incubation at 37-38°C for 21 days.

**Inbreeding avoidance**: A minimum effective breeding population of 50 animals per species maintains genetic diversity at levels that avoid inbreeding depression (reduced fertility, slower growth, higher mortality). In practice this means at least 15-20 breeding females and 3-5 unrelated males. Rotate or exchange breeding males with neighboring settlements every 3-4 generations. Track pedigrees to avoid mating animals sharing a parent or grandparent. The coefficient of inbreeding for offspring of first-cousin matings is 6.25%; for half-sibling matings, 12.5%. Keep the coefficient below 6.25% across the herd.

**Culling decisions**: Remove animals that are aggressive, chronically ill, infertile, or consistently low-producing. Cull cows that fail to conceive after two breeding seasons. Ewes that lose lambs repeatedly or produce single lambs when the flock average is twins are candidates. Culling rate of 15-20% per year in a cattle herd is normal and maintains productivity.

**Castration of males**: Elastrator banding (rubber ring applied to scrotum above testicles at 1-7 days old) cuts blood supply; testicles atrophy and fall off in 2-4 weeks. Emasculatome/crushing (Burdizzo clamp) severs the spermatic cord without incision, best at 2-8 weeks. Surgical removal (scalpel incision of the scrotum, pulling and cutting the cord) is the most reliable method, performed at 2-12 weeks with clean instruments and antiseptic. All methods require aseptic conditions and monitoring for infection in the following week.

**Artificial insemination basics**: Collecting semen from a superior male and depositing it in the female reproductive tract allows wider distribution of desirable genetics without moving live animals. Requires knowledge of female estrus cycles (cattle cycle every 21 days, sheep every 16-17 days during breeding season, goats every 18-21 days, pigs every 21 days, mares every 21 days from spring through autumn). Semen can be stored cool for 2-4 days in simple containers; frozen storage requires liquid nitrogen infrastructure beyond stone-age capability.

### Species Profiles

**Cattle (*Bos taurus*)**: Mature weight 400-800 kg depending on breed. Gestation 283 days (range 279-290). Dairy cows produce 10-20 L milk/day during a 305-day lactation, peaking at 25-35 L/day in the first 60 days post-calving. Dry period of 45-60 days before next calving is essential for udder health and fetal growth. Calves nurse colostrum (first milk, rich in antibodies, 7-9% fat vs. 3.5-4% in normal milk) within 6 hours of birth to acquire passive immunity. Wean at 6-8 months. Steers (castrated males) reach slaughter weight of 450-550 kg at 18-24 months on pasture plus grain finishing. Cattle convert feed at roughly 6:1 (kg feed dry matter per kg live weight gain), making them the least feed-efficient livestock but the most versatile — providing draft power, milk, leather, tallow, bone, and manure from a single species.

**Sheep (*Ovis aries*)**: Mature weight 80-120 kg for ewes, 100-180 kg for rams. Gestation 147 days (range 144-152). Ewes typically produce 1-3 lambs per birth; twins are the management target. Milk yield 0.5-2.0 L/day during a 120-180 day lactation. Fleece weight 2-5 kg per shearing (annual for most breeds). Feed requirement 1.5-3.0 kg dry matter/day. Sheep graze closer to the ground than cattle and prefer short, tender growth, making them ideal for managing pasture after cattle have taken the taller grass. stocking rate 10-15 ewes per hectare on good pasture. Lambs reach market weight of 35-45 kg at 4-6 months on good pasture.

**Goats (*Capra aegagrus hircus*)**: Mature weight 30-80 kg. Gestation 150 days (range 145-155). Dairy goats produce 2-5 L milk/day during a 250-305 day lactation. Goats are browsers rather than grazers — they prefer woody shrubs, brambles, and brush over grass, making them ideal for clearing overgrown land and managing invasive species. They will strip bark from young trees, so protect valuable timber. Stocking rate 8-12 goats per hectare on browse. Goats are more drought-tolerant than sheep and can thrive on marginal land unsuitable for crops. Bucks (intact males) are notoriously strong-smelling during breeding season; keep them separate from milking does to avoid tainting milk.

**Pigs (*Sus scrofa domesticus*)**: Mature weight 150-300 kg. Gestation 114 days (range 112-116, often remembered as "3 months, 3 weeks, 3 days"). Litter size 8-12 piglets for mature sows; first-litter gilts produce 6-8. Piglets weigh 1.0-1.5 kg at birth and double weight in the first week on sow milk (7-9% fat, the richest of any domestic livestock). Wean at 3-4 weeks for intensive systems, 6-8 weeks for pasture-based systems. Market weight 100-130 kg at 5-7 months. Feed conversion ratio 3:1 (kg feed per kg gain), better than cattle but worse than poultry. Pigs are omnivores: they consume kitchen waste, crop residues, whey from cheese-making, fallen fruit, and acorns. One sow can produce 20-25 market pigs per year across two litters. Pigs root (dig with their snout), which destroys pasture — use rotational paddocks or rings through the snout to prevent damage.

**Horses (*Equus caballus*) and donkeys (*Equus africanus asinus*)**: Horses mature at 400-700 kg; donkeys at 180-450 kg. Horse gestation 335 days (range 320-350); donkey gestation 365 days (range 340-390). Foals stand and nurse within 1-2 hours of birth. Horses are working animals, not primarily food animals — they provide transport, draft power, and military capability. A horse can pull 10-15% of its body weight at walking speed (4-6 km/h) for 8 hours. Donkeys are more drought-tolerant, require less feed (5-10 kg DM/day vs. 10-20 kg for horses), and are steadier in difficult terrain. Mules (horse mare × donkey jack) combine the size and strength of horses with the hardiness and sure-footedness of donkeys; they are sterile and cannot breed. Shoe working horses every 6-8 weeks; donkeys on soft ground may not need shoes.

**Poultry overview**: Chickens (*Gallus gallus domesticus*, 1.5-4.5 kg) produce 200-300 eggs/year from modern breeds. Ducks (*Anas platyrhynchos domesticus*, 2-5 kg) lay 150-250 eggs/year and forage aggressively on slugs, snails, and insects in wet areas. Geese (*Anser anser domesticus*, 4-10 kg) are aggressive grazers that mow grass, produce down, and serve as guard animals — their alarm calls carry 100+ m. Turkeys (*Meleagris gallopavo*, 4-15 kg) are efficient converters of grain and forage to meat. All poultry require grit (small stones 2-5 mm) for digestion in the gizzard, calcium supplementation (crushed oyster shell or bone) for eggshell formation, and protection from predators (foxes, hawks, weasels, raccoons). See the [Poultry Farming](poultry.md) article for detailed species-by-species management.

### Young Stock Management

**Colostrum and neonatal care**: All mammalian newborns must receive colostrum within 6 hours of birth. The gut closes to antibody absorption after 24 hours; failure to receive colostrum results in a 50-80% mortality rate in the first month. For orphaned or rejected neonates, bottle-feed warmed (38-39°C) colostrum from a stored supply (frozen or refrigerated from earlier births) at 10% of body weight in the first 24 hours, divided into 3-4 feedings.

**Milk feeding schedules**: Calves: 4-6 L/day whole milk or milk replacer (20% fat, 20% protein) in two feedings, reducing over 6-8 weeks. Lambs and kids: 0.5-1.0 L/day, weaning at 6-8 weeks. Piglets: nurse from the sow for 3-8 weeks; orphan piglets are fed every 2-3 hours with sow milk replacer for the first week. Foals: nurse at will from the mare; orphan foals require 15-20 L/day of mare milk replacer in frequent small feedings. Chickens: no milk; chicks eat starter crumble (20-24% protein) from day 1.

**CREEP FEEDING**: Provide supplemental feed to nursing young in an area accessible only to them (creep feeder: opening 30-40 cm wide for lambs, 60-70 cm for calves). Creep feed increases weaning weight by 15-25% and reduces the lactation demand on the dam, improving her condition for re-breeding. Start at 2-3 weeks of age; offer palatable grain (cracked corn, rolled oats, soy meal) at 16-18% protein. Intake ramps from 0.1 kg/day initially to 1.0-1.5 kg/day by weaning.

**Weaning**: Abrupt separation stresses young stock and dams. Gradual weaning (fence-line contact for 7 days where young and dam can see and smell but not nurse) reduces cortisol levels and weight loss. Post-weaning, monitor young stock daily for 2 weeks; weight loss exceeding 10% triggers investigation. Provide the highest-quality forage available to weanlings — their rumen or digestive system is still developing.

### Seasonal Management Calendar

**Spring (calving/lambing/kidding season)**: Move pregnant animals to clean, sheltered paddocks 2 weeks before expected births. Check ewes and does every 4 hours during lambing/kidding; cattle are lower-maintenance but check heifers (first-time mothers) frequently. Ensure colostrum supply or replacer is on hand. Vaccinate pregnant females for clostridial diseases 4-6 weeks before birth to pass immunity to offspring. Castrate and tail-dock lambs within the first week. Tag or notch all newborns for identification. Begin pasture turnout once grass is 10-15 cm tall; rotational graze to prevent over-grazing young growth. Shear sheep before lambing (pre-lamb shearing) or 4-6 weeks after, depending on climate. Start beehive inspections (see [Beekeeping](beekeeping.md)).

**Summer**: Peak forage growth — stockpile surplus as hay. Cut hay at early heading for maximum protein (10-14% CP). Monitor water consumption: cattle drink 50-80 L/day in hot weather, sheep 8-15 L/day. Provide shade (trees, open-sided shelters); heat stress above 25°C reduces feed intake and milk production in cattle by 10-20%. Apply fly control: pour-on treatments for cattle, dust baths for poultry. Wean spring-born young stock. Monitor for bloat on lush legume pastures (clover, alfalfa): rumen distension from gas fermentation can kill within hours. Prevent by transitioning animals to legume pasture gradually over 7-10 days.

**Autumn**: Breeding season for sheep and goats (shortening daylight triggers estrus). Flush ewes (increase nutrition 2-3 weeks before breeding) to increase ovulation rate and twinning percentage. Pregnancy-check cattle 40-60 days post-breeding. Cull open (non-pregnant) females and low producers. Stockpile feed: test hay quality, calculate winter feed budget (multiply daily needs by 120-150 winter days, add 15% buffer). Treat all livestock for internal parasites before housing. Shore up fencing and repair shelters. Harvest root crops for winter feed. Wean lambs and kids.

**Winter**: Feed stored forage (hay, silage, root crops). Cattle require 10-15 kg hay/day; sheep 1.5-2.5 kg/day; horses 8-15 kg/day. Provide windbreaks; effective temperature drops 1°C per 1 km/h wind speed above 8 km/h. Increase grain supplementation for working animals and pregnant females in the last trimester. Break ice on water troughs twice daily. Monitor body condition: dairy cows should maintain body condition score 2.5-3.0 on a 5-point scale; ribs should be palpable but not visible. Difficult births increase by 30-50% in under-conditioned females. Keep poultry houses above 0°C with deep bedding; egg production declines below 12°C daylight hours without supplemental light.

## Troubleshooting — Common Livestock Problems

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Cow not coming into estrus (anestrus) | Poor body condition (BCS <2.0 on 5-point scale); mineral deficiency (phosphorus, selenium); cystic ovaries | Improve nutrition — increase energy intake 10–15% above maintenance; supplement phosphorus (bone meal or dicalcium phosphate at 50–100 g/day); veterinary exam for ovarian cysts |
| Calf scours (diarrhea in neonates) | Inadequate colostrum; E. coli or rotavirus infection; cold, wet conditions | Ensure colostrum within 6 hours of birth; isolate scouring calves; oral electrolyte solution (NaCl 4 g + KCl 1 g + glucose 40 g per 2 L water, fed warm); clean and dry bedding |
| Bloat in cattle on legume pasture | Rapid fermentation of clover/alfalfa produces trapped gas in rumen | Transition animals to legume pasture gradually over 7–10 days; provide dry hay before turnout; in emergency: pass stomach tube to release gas, or trocar (puncture) left flank at the triangle between hip, last rib, and transverse processes |
| Sheep losing condition despite adequate pasture | Internal parasites (Haemonchus, Ostertagia); trace mineral deficiency (cobalt, copper) | Fecal egg count to confirm parasites; dose with anthelmintic; move to clean pasture after treatment; supplement trace minerals via loose mineral lick |
| Pigs fighting and tail-biting | Overcrowding; boredom; inadequate feed or water; drafts | Provide minimum 0.7 m² per grower pig; add chains, straw, or objects for enrichment; ensure continuous access to feed and water; eliminate drafts |
| Egg production drop in hens | Reduced daylight (<14 hours); molting; inadequate calcium; disease | Provide 14–16 hours light (artificial supplementation in winter); supplement calcium (crushed oyster shell ad lib); check for parasites and respiratory disease |
| Horses losing weight in winter | Insufficient energy intake; dental problems (hooks, waves); internal parasites | Increase hay to 2–2.5% of body weight; check teeth and float (file) sharp points if needed; deworm; provide windbreak shelter |
| Lame sheep (foot rot) | Bacterial infection (Fusobacterium) in wet conditions | Trim affected hooves; walk sheep through 5–10% copper sulfate foot bath; move to dry pasture; cull chronically affected animals |
| Abortion storm in sheep (multiple ewes aborting) | Toxoplasmosis (cat feces in feed); Campylobacter; listeriosis from spoiled silage | Keep cats away from feed stores; feed only well-fermented silage (pH <4.5); vaccinate breeding ewes for campylobacter and toxoplasmosis where available; isolate aborting ewes immediately |
| Predation losses (lambs, kids, poultry) | Inadequate fencing; no guard animals; night exposure | Install guard dogs (2–3 per 100 sheep); house poultry in predator-proof coop at night; repair fence gaps; remove carrion that attracts predators |

### Handling and Health

**Restraint techniques**: A well-constructed crush (narrow stall with head catch and side panels) is essential for cattle handling. Halter training (rope or leather headcollar) works for horses, donkeys, and halter-broken cattle. A leg rope or hobble restrains a cow's kick during milking or treatment. Sheep are controlled by sitting them on their hindquarters (the "turn" or "set") which calms them. Sheep crook (long pole with curved neck) catches individuals from a flock without chasing. Nose rings (copper or iron, 8-12 cm diameter) prevent bulls from pushing or charging. Pig boards (solid wooden panel 60 × 90 cm) shield handlers from charging sows.

**Quarantine**: Isolate all incoming animals for 30 days minimum in a separate enclosure at least 15 m from the main herd. Observe for coughing, diarrhea, lameness, discharge from eyes or nose, and abnormal behavior. Test for brucellosis and tuberculosis where testing is available. Never mix new stock with the herd until the quarantine period ends with no symptoms.

**Parasite management**: Internal parasites (gastrointestinal nematodes, liver flukes, coccidia) cause weight loss, anemia, diarrhea, and death in heavy infestations. Rotational grazing breaks parasite life cycles because most larvae die within 60-90 days without a host. Mixed-species grazing (cattle followed by sheep) reduces parasite loads because cattle nematodes do not reproduce in sheep and vice versa. Dose with anthelmintic compounds (see [Medicine](../health/medicine.md)) at the beginning and end of the grazing season. External parasites (lice, ticks, mites) are controlled by topical application of lime-sulfur dip or wood ash dust baths for poultry.

**Hoof care**: Cattle, sheep, goats, horses, and donkeys all need regular hoof trimming. Cattle on soft pasture may need trimming every 6-12 months; horses on dry ground self-wear hooves, but stabled horses need trimming every 6-8 weeks. Overgrown hooves cause lameness, which reduces feed intake, draft power, and breeding success. Sheep on wet pasture are prone to foot rot (bacterial infection between hoof claws, identified by foul smell and lameness). Trim affected hooves, apply copper sulfate foot bath (5-10% solution).

**[Common diseases](../glossary/common-diseases.md)** (identification only; treatment covered in [Medicine](../health/medicine.md)):
- **Foot-and-mouth**: Vesicles (fluid-filled blisters) on tongue, lips, feet, and teats. Causes drooling, lameness, fever. Spreads by contact and airborne transmission. Reportable; quarantine immediately.
- **Anthrax**: Sudden death without prior symptoms in cattle and sheep. Carcass bloated, blood from body openings does not clot. Do not open the carcass; spores contaminate soil for decades.
- **Brucellosis**: Abortion in late pregnancy, retained placenta, infertility. Transmissible to humans (undulant fever). Test breeding stock regularly.
- **Avian influenza (fowl plague)**: Respiratory distress, swollen head, cyanotic comb and wattles, sudden high mortality in poultry. Wild waterfowl are reservoirs; keep domestic poultry separated from wild bird contact.

### Record-Keeping

**Individual identification**: Tag every breeding animal with a unique number. Ear tags (plastic or metal) are the simplest method — apply at birth or within the first week. Ear notches (using a standardized notch code: different positions on left and right ear encode digits) provide permanent identification that does not fall out. Brands (freeze-brand with copper-alginate paste at -40°C, or hot iron for extensive rangeland systems) mark ownership. Microchips require electronic readers and are unnecessary at the stone-age level.

**Production records**: Track milk yield per cow at each milking (graduated bucket, record in liters). Weigh lambs, kids, and piglets at birth and weaning to calculate average daily gain (ADG, in grams/day). Target ADG: lambs 250-350 g/day, piglets 200-300 g/day, calves 700-900 g/day. Record fleece weight per sheep at shearing. Log egg production per hen weekly (a drop below 60% lay rate signals health problems, moulting, or inadequate light). Note breeding dates, expected birth dates, and actual birth dates to track reproductive efficiency. Calculate key metrics annually: calving interval (target <370 days), lambs born per ewe exposed (target >1.8), piglets weaned per sow per year (target >20), and eggs per hen per year.

**Health records**: Log every health event: date, animal ID, symptoms, treatment administered, outcome, and withdrawal period for milk or meat after medication. Record all deaths with suspected cause. A simple ledger book with one page per animal or a card file system organized by ID number works without any technology beyond paper and pencil. These records are essential for identifying patterns — if 3 of 10 calves born in March develop the same symptoms, the record reveals the cluster that would otherwise be invisible.

**Feed inventory**: Record hay and grain stores monthly. A 500 kg cow eating 12 kg hay/day consumes 1,440 kg over a 120-day winter. Know your total winter feed requirement (sum of all animals × daily need × winter days + 15% buffer) before autumn, and acquire or grow enough. Running out of feed in February is a catastrophe that record-keeping prevents.

### Cross-Domain Links

- **[Draft Power & Harnessing](draft-power.md)**: working oxen, horses, and donkeys for plowing, transport, and milling depends on domestication and training
- **[Animal-Derived Materials](animal-materials.md)**: leather, tallow, wool, horn, bone, sinew, and hide glue all come from domesticated livestock
- **[Poultry Farming](poultry.md)**: dedicated species articles and poultry-specific husbandry for all seven farmed bird species
- **[Insect Farming / BSF](insect-farming.md)**: black soldier fly and other insects for waste conversion, animal feed, and protein production
- **[Food & Agriculture](../foundations/food-agriculture.md)**: manure sustains crop yields; meat, milk, and eggs are primary protein sources
- **[Medicine](../health/medicine.md)**: disease diagnosis and treatment for both livestock and zoonotic transmission to humans

### Grazing Systems

**Rotational grazing**: Divide available pasture into 6-12 paddocks using temporary electric fencing or permanent fences. Graze each paddock for 3-5 days, then rotate to the next. Rest period allows regrowth: 20-30 days in spring (fast growth), 40-60 days in summer (slower growth). This system increases forage utilization by 20-30% compared to continuous grazing, reduces selective grazing (animals eat everything rather than only preferred species), and breaks parasite life cycles because most nematode larvae die within 60-90 days without a host on the pasture.

**Mixed-species grazing**: Cattle prefer grass, sheep graze forbs and short grass, goats browse woody plants. Running two or more species on the same land (either simultaneously or in sequence) utilizes 30-40% more of the available forage than single-species grazing. Cattle and sheep are the most common combination: cattle take the tall grass, sheep follow and graze closer to ground level. Goats and sheep share some dietary overlap but goats prefer browse. stocking density for mixed cattle-sheep: 2 cattle + 8 sheep per hectare on good pasture. Mixed grazing also dilutes parasite loads, as cattle nematodes cannot complete their life cycle in sheep and vice versa.

**Strip grazing**: For limited winter pasture or crop residue grazing, use a movable electric fence to allocate a fresh strip of forage daily. Animals graze the allocated strip completely before the fence advances, achieving 80-90% utilization with minimal waste. particularly effective for grazing standing corn, kale, or fodder beet through winter — the fence prevents trampling and fouling of ungrazed forage. Advance the fence 2-5 m/day depending on forage density and animal numbers.

**Dry lot and sacrifice paddocks**: In wet climates or during winter, keep animals on a well-drained lot (gravel or concrete pad, 15-25 m² per cattle beast) and bring feed to them rather than turning them onto saturated pasture where hoof damage destroys the sod. This sacrifice area preserves the main pasture for spring growth. Feed hay and silage in racks or bunks to reduce waste (floor feeding loses 25-40% to trampling and fouling; rack feeding loses 5-10%).

### Safety

**Zoonotic diseases**: Any disease that jumps from animals to humans is a zoonosis. The most significant in a livestock context: brucellosis (unpasteurized milk from infected cows or goats), ringworm (direct skin contact with infected animals), leptospirosis (urine-contaminated water), Q fever (birth fluids and manure aerosol), and rabies (bites from infected mammals). Pasteurize all milk (heat to 63°C for 30 minutes or 72°C for 15 seconds) to kill brucellosis organisms. Wear gloves when handling birth fluids or manure. Wash hands with soap after every contact with animals or their environment.

**Handling injuries**: A kick from a cow delivers 1,500-2,000 N of force, enough to fracture ribs or cause internal bleeding. A horse kick is similarly powerful and directed backward. A bull charge can kill. Never stand directly behind any large animal. Always have an escape route planned when working in close quarters. Use a crush or chute for any procedure on cattle. Two people should be present when handling large animals.

**Proper lifting**: A 40 kg feed sack or a 30 kg dead lamb are common lifting tasks. Bend at the knees, keep the load close to the body, and avoid twisting while carrying. Back injuries from livestock work are among the most common long-term disabilities in agricultural communities. Use a two-person lift for anything over 50 kg. Mechanical aids (tripod hoist, pulley systems) save backs during carcass handling and heavy equipment maintenance.

**Needle and sharp safety**: Hypodermic needles used for vaccinations and medical treatments are a puncture hazard. Dispose of used needles in a rigid, puncture-proof container (heavy-wall glass jar or metal can with a slit lid). Never recap a used needle. Scalpels used for castration or wound care are equally hazardous — use a dedicated sharps container. Accidental self-injection with livestock vaccines or medications requires immediate medical attention; record the substance and dose for the medical provider.

**Hygiene after contact**: Animal environments harbor bacteria (E. coli, Salmonella, Campylobacter) and parasites (Cryptosporidium, Giardia). Clean and dress all cuts and abrasions immediately, as infection from animal-borne bacteria in open wounds can progress to sepsis within 24-48 hours. Disinfect boots and tools that contact manure before entering food preparation areas.

**Parturition hazards**: Assisting with difficult births (dystocia) is a routine livestock task. Wear long gloves when reaching into the birth canal. Calving difficulty is common in first-calf heifers (breeds selected for large calves increase risk). Malpresentations (breech, head-back) require repositioning by hand. If correction fails within 30 minutes, the dam and offspring are at risk of death. After delivery, ensure the dam passes the placenta within 12 hours; retained placenta causes toxic metritis. Dip newborn navels in 7% iodine solution to prevent joint ill (navel infection leading to septic arthritis).

**Manure handling**: Fresh manure contains pathogens and attracts flies. Compost at 55-65°C for at least 3 days (turned pile method) to kill pathogens and weed seeds before field application. Raw manure applied to food crops must be incorporated at least 120 days before harvest of crops that touch the soil, or 90 days for crops that do not. Store manure on a concrete or clay-lined pad to prevent nutrient leaching into groundwater.

**Fire safety in barns**: Barn fires are catastrophic — they kill animals too panicked to flee and destroy winter feed stores. Store hay only after it has dried to below 18% moisture (probe with a hay moisture meter; above 25% moisture, spontaneous combustion is possible within 3-7 days of baling). Never store gasoline, oils, or other flammables in animal housing. Use lanterns with enclosed flames (or better, electric lighting when available). Maintain a firebreak of 10 m between hay storage and animal housing. Keep sand or water buckets near the barn entrance for emergency fire suppression.

**Predator protection**: Wolves, coyotes, foxes, big cats, and birds of prey all threaten livestock. Guard dogs (raised with the flock from puppyhood, 2-3 dogs per 100 head of sheep) are the most effective deterrent. Llamas and donkeys also guard sheep and goats against canids. Night housing in predator-proof enclosures (tight fencing, covered where hawks are a threat) reduces losses. Remove carrion promptly — it attracts predators. Electric fencing (one wire at 25 cm and one at 60 cm, 3,000-5,000 V pulse) deters most predators but requires wire and an energizer.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Animals](./index.md) • [All Domains](../index.md)*
