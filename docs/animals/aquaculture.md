# Aquaculture & Fisheries

> **Node ID**: animals.aquaculture
> **Domain**: [Animals](./index.md)
> **Dependencies**: [`animals.insect-farming`](insect-farming.md), [`foundations.tools-basic`](../foundations/tools-basic.md)
> **Enables**: [`agriculture.aquaponics`](../agriculture/aquaponics.md)
> **Timeline**: Years 2-10+
> **Outputs**: fish, shellfish, fish_oil, dried_fish, smoked_fish, fish_sauce, fish_guano
> **Critical**: Yes — highest protein conversion efficiency of any animal production system

## Problem

Aquaculture converts water surfaces into protein production systems. Fish convert feed to body mass at ratios of 1.2-2.0:1 (kg feed per kg gain), far more efficient than any land livestock. A 1000 m² pond stocked with carp can produce 200-600 kg of fish per year on minimal supplemental feeding, yielding protein that requires no pasture, no fencing, and no winter housing.

The practice splits into freshwater pond farming (the primary focus here) and coastal shellfish cultivation. Both rely on the same principles: provide the right environment, stock at appropriate densities, and manage water quality. Pond fish farming works from stone-age materials alone. Clay for lining, timber for drains, woven nets for harvest, and manure for fertilizing the water column.

## Prerequisites

- [Insect farming](insect-farming.md) — insect meal as supplemental fish feed
- [Basic tools](../foundations/tools-basic.md) — digging, net-making, and construction implements
- [Food and agriculture](../foundations/food-agriculture.md) — manure for pond fertilization, crop byproducts for feed
- [Water management](../foundations/index.md) — reliable water source and drainage

## Pond Construction

#### Site Selection

Choose ground with natural clay subsoil if available, as this eliminates the need to import lining material. Test by digging a 50 cm test pit, filling it with water, and checking seepage over 24 hours. Loss under 1 cm/day indicates adequate natural sealing. Valley floors, natural depressions, and areas downslope of springs are ideal. Avoid sandy or gravelly soils, which drain too fast to hold water without extensive lining.

Water source options, ranked by reliability:

1. **Spring-fed**: Best. Constant flow, stable temperature, no pumping needed. A spring delivering 5-10 L/min sustains a 1000 m² pond through evaporation losses.
2. **Stream diversion**: Reliable where streams flow year-round. Requires a diversion channel (30-50 cm wide, 20-30 cm deep) with a simple sluice gate (wooden plank sliding in timber grooves) to control inflow.
3. **Rainwater catchment**: Feasible in regions with 800+ mm annual rainfall. Pond captures direct precipitation plus runoff from a catchment area 5-10 times the pond surface.

#### Digging and Lining

Pond dimensions for subsistence production: 500-2000 m² surface area. Depth 1.5-3 m, with the deepest point at the drain end. Slope the bottom at 1-2% grade toward the outlet. Shallow margins (0.3-0.5 m depth) around the edge warm faster in spring, stimulating plankton growth and providing spawning habitat.

**Clay lining**: Where natural subsoil is permeable, spread a 15-30 cm layer of clay over the entire pond bottom and sides. Compact in 5 cm lifts using hand tampers or a heavy log dragged across the surface. The clay must be wet enough to bond (squeeze a handful; it should hold its shape without crumbling) but not so wet that it pumps underfoot. Bentonite clay, if available, seals at lower application rates (5-10 kg/m²) but is not essential.

**Embankments**: Build from excavated soil, compacted in layers. Crest width 1-2 m for foot access. Freeboard (height above maximum water level) of 30-50 cm prevents wave overtopping in wind. Side slopes no steeper than 1:2 (vertical:horizontal) on the water side to prevent slumping. Grass the outer slopes immediately to prevent erosion.

#### Water Control

**Drain pipe**: Install at the lowest point before filling. Clay or wooden pipe, 10-15 cm diameter, set through the embankment with puddled clay sealing around the outside. A wooden plug or sluice board controls outflow. The drain allows complete emptying for harvest and pond maintenance, which should happen annually.

**Overflow spillway**: Cut into the embankment crest at the maximum desired water level, 30-50 cm below the top. Line with stone or timber to prevent erosion. Width 50-100 cm for a 1000 m² pond. Never block the overflow; a pond that overtops an embankment can fail catastrophically.

**Inlet channel**: If stream-fed or spring-fed, dig a channel from the source to the pond. Include a settling basin (a widened section of channel, 1 × 1 × 0.5 m) to trap silt before it enters the pond. Fit a screen (woven willow or wire mesh, 5-10 mm openings) at the pond entrance to exclude wild fish predators.

## Fish Species

#### Carp (*Cyprinus carpio*)

The universal aquaculture fish. Tolerates turbid water, low oxygen (down to 3 mg/L), and temperatures from 4-35°C. Optimal growth at 15-25°C. Omnivorous: consumes plankton, insects, detritus, aquatic plants, and supplemental feed.

Mature weight 2-5 kg in ponds. Growth rate 2-3 kg/year with supplemental feeding, faster in warm climates. Can reach 1 kg from fingerling in a single growing season. Spawns in shallow, vegetated water when temperature exceeds 18°C. A 3 kg female produces 300,000-500,000 eggs per spawn, though survival in ponds without special spawning infrastructure is typically 5-15%.

Carp tolerate crowding better than most species and thrive on low-cost feeds, making them the first choice for subsistence ponds in temperate and subtropical climates.

#### Tilapia (*Oreochromis* spp.)

The best tropical aquaculture fish. Optimal growth at 25-30°C; stops feeding below 15°C; dies below 10°C. This limits tilapia to warm climates or heated water, but where conditions suit them, they outperform carp on plant-based feeds.

Mature weight 0.5-2 kg. Growth rate 0.5-1 kg/year with supplemental feeding. Herbivorous: feeds on algae, duckweed, aquatic plants, and agricultural byproducts. Breeds prolifically in ponds (mouthbrooding; female carries fertilized eggs in her mouth for 10-14 days). This makes maintaining breeding populations trivial but can lead to overpopulation and stunting if not managed by regular harvesting of small fish.

#### Trout (*Oncorhynchus mykiss*)

Cold-water species requiring clean, well-oxygenated water (dissolved oxygen above 6 mg/L, temperature 10-15°C). Not suitable for warm, stagnant ponds. Requires flowing water: spring-fed channels, raceways, or cold streams.

Mature weight 0.5-3 kg. Carnivorous: needs animal protein (insects, fish meal, bloodworms, or formulated feed). Growth rate 0.3-0.5 kg/year in ambient-temperature raceways. Does not spawn in still ponds; requires artificial propagation or stream access.

Trutch farming is harder than carp or tilapia but produces high-value fish in regions where cold spring water is abundant and warm-water species cannot grow.

#### Catfish (*Silurus glanis* and related species)

Hardy bottom-dwellers tolerant of turbid, low-oxygen water (down to 2-3 mg/L due to accessory breathing organs in many species). Temperature range 20-25°C optimal, but many species survive 4-30°C.

Mature weight 2-10 kg, faster growing than carp in warm water. Omnivorous scavengers: consume dead organic matter, insects, small fish, and supplemental feed. Can be raised at higher densities than carp due to air-breathing capability in some species. Handling requires care: spined fins can puncture skin.

## Stocking and Feeding

#### Stocking

Source fingerlings (5-15 cm length, 10-50 g weight) from wild catch using fine-mesh seine nets in streams and natural ponds, or from dedicated breeding ponds. A breeding pond of 200-500 m² with 20-30 adult carp produces enough fingerlings annually to stock 2-4 production ponds.

**Stocking density**:

- Extensive farming (no supplemental feed, natural productivity only): 1-3 fish per m². Expect 100-300 kg/ha/year.
- Semi-intensive (supplemental feed + pond fertilization): 3-5 fish per m². Expect 500-2000 kg/ha/year.
- Intensive (heavy feeding, water exchange): 5-10 fish per m². Requires continuous water flow and risks water quality crashes. Not recommended for basic setups.

Acclimate fingerlings to pond water temperature before release. Float the transport container in the pond for 30 minutes to equalize temperature, then gradually mix pond water into the container over another 30 minutes before releasing.

#### Feeding

Supplemental feed boosts production 3-5x over unfertilized ponds. Feed sources ranked by cost and availability:

1. **Agricultural byproducts**: Rice bran, wheat bran, oilseed cake (pressed residue after oil extraction), broken grains. Cheapest and most available.
2. **Duckweed (*Lemna* spp.)**: Grows on the pond surface itself. Protein content 25-35% dry weight. Can be harvested from a dedicated duckweed pond and fed fresh to tilapia and carp.
3. **Earthworms**: Raised in compost bins using kitchen waste and manure. Protein content 60-70% dry weight. Excellent feed but labor-intensive to produce in quantity.
4. **Insects**: Black soldier fly larvae, mealworms, termites. Can be cultivated. High protein, good for trout and catfish.
5. **Terrestrial plants**: Cut grass, vegetable trimmings, legume leaves. Tilapia and grass carp consume these directly.

**Feeding rate**: 2-5% of total fish body weight per day, split into 2-3 feedings. Reduce or suspend feeding when water temperature drops below 10°C (fish metabolism slows and uneaten feed degrades water quality). Observe feeding behavior: if fish stop consuming within 15-20 minutes, reduce the ration.

#### Pond Fertilization

Adding manure to the pond stimulates plankton blooms that form the base of the aquatic food chain. Fish do not eat manure directly; they eat the plankton, insects, and detritus that the manure supports.

**Application rate**: 10-20 kg fresh manure per 100 m² per week. Cattle, pig, or poultry manure all work. Poultry manure is richest in nitrogen but must be composted 2-4 weeks before adding to the pond to avoid ammonia spikes that kill fish. Distribute manure from a boat or by tossing from the bank around the pond margins.

Monitor water color: a healthy fertilized pond has a green tint (plankton bloom) with visibility of 25-40 cm (Secchi disk depth). If you can see the bottom at 50+ cm, the pond needs more fertilizer. If visibility drops below 20 cm, suspend fertilization until it clears; oxygen depletion follows overly dense blooms.

## Net and Trap Making

#### Cast Nets

Circular nets thrown by hand to envelop fish. Diameter 2-4 m for one-person use. Mesh size 1-2 cm (smaller mesh catches smaller fish; 1.5 cm is a good general-purpose size).

**Construction**: Netting made from linen or cotton thread (twine diameter 0.5-1.0 mm). The mesh is knotted (sheet bend or reef knot at each junction) or knotted using a netting needle and gauge. A gauge board sets mesh size consistently.

**Weighting**: Attach sinkers around the bottom perimeter at 10-15 cm intervals. Clay sinkers (dried in the sun or low-fired) work where lead is unavailable. Lead sinkers (10-30 g each) cast better and last longer but require lead smelting.

**Throwing technique**: Gather the net on one arm, grip the center ring in the teeth, and throw with a rotating arm motion that opens the net into a circle. Takes practice; expect 50-100 throws to learn.

#### Gill Nets

Wall-like nets that fish swim into, catching by the gills as they attempt to pass through. Length 25-50 m, depth 1-1.5 m. Mesh size determines catch: 5 cm mesh for 0.5-1 kg fish, 8 cm for 2-4 kg fish, 12 cm for 5+ kg fish.

Set gill nets across channels, at pond outlets, or suspended between stakes in open water. Fish swim into the net at night or in turbid conditions. Check twice daily; trapped fish die and spoil in warm water within 6-12 hours.

#### Seine Nets

Long nets dragged through the water to encircle fish. Length 10-30 m, depth 1.5-2.5 m, with floats along the top (cork, gourd, or sealed bamboo segments) and sinkers along the bottom. Requires 2-3 people to operate: two to pull the ends and one to manage the accumulation of fish in the center.

Seining is the most efficient method for harvesting a pond completely. Draw the net from one end of the pond to the other, concentrating fish into a shrinking area. Use for annual harvest or partial harvests to thin stunted populations.

#### Lines and Hooks

**Line making**: Twist linen or cotton thread into 2-4 ply for fishing line. Linen is stronger and more rot-resistant than cotton. For heavier line (large fish), use 6-8 ply or braided construction. Test breaking strength by hanging weights: 5 kg test is adequate for most pond fish, 10-15 kg for large catfish.

**Hook making**: Bone hooks (cut from large mammal rib or scapula, sharpened to a point, bent in boiling water or over a heated stone) work for small to medium fish. Iron wire hooks (forged from 2-4 mm wire) are stronger and hold their point longer. Sizes range from 2 cm (small panfish) to 10 cm (large catfish, river fish). Barbless hooks are simpler to make but lose more fish during the fight.

## Fish Processing

Fresh fish spoils within 6-12 hours at 25-30°C. Processing extends shelf life from days to months.

#### Sun Drying

Split fish along the backbone, remove guts and gills, and open flat (butterfly cut). Rub with salt if available (reduces insect damage and speeds drying). Lay on racks of woven reeds or wooden slats, skin side down. Elevate racks 50-80 cm off the ground for air circulation.

Drying time: 3-5 days in hot sun with low humidity. Fish is fully dried when it feels stiff and brittle, with no soft spots. Moisture content drops from 70-80% (fresh) to 15-25% (dried). Weight reduces to roughly 20-30% of fresh weight.

Storage: Bundle dried fish and keep in a dry, ventilated place. Properly dried fish keeps 3-6 months. Reconstitute by soaking in water for 30-60 minutes before cooking.

#### Smoking

Smoking deposits antimicrobial compounds from wood smoke onto the fish surface while simultaneously drying it.

**Cold smoking**: Hang split or whole gutted fish in a smokehouse (small enclosed room or chimney structure) with a smoldering fire that produces smoke without significant heat. Temperature 25-35°C. Duration 12-48 hours. Cold-smoked fish retains a soft texture and must be cooked before eating. Keeps 1-3 weeks at cool temperatures.

**Hot smoking**: Higher temperature, faster process. Smoke at 60-80°C for 4-8 hours. Hot-smoked fish is cooked through and has a firmer, drier texture. Keeps 1-2 weeks without refrigeration, longer if kept cool and dry.

Best smoking woods: hardwoods (oak, hickory, beech, alder). Avoid resinous softwoods (pine, spruce), which deposit bitter-tasting tars.

#### Salting

Salt preserves fish by drawing out moisture and creating a hypertonic environment that bacteria cannot tolerate.

**Dry salting**: Layer split fish and coarse salt in a barrel or vat, skin side down. Apply 200-400 g salt per kg of fish (heavier salting for longer storage in warm climates). Weight the top with a clean stone to press out liquid. After 7-14 days, remove fish and dry in the sun for 1-2 days. Properly salted fish keeps 6-12 months in a cool, dry place.

**Brine salting**: Submerge fish in saturated brine (250-300 g salt per liter of water) for 24-72 hours, then dry or smoke. Faster than dry salting but produces a less concentrated cure.

#### Fermentation

**Fish sauce**: Layer small fish (or fish scraps) with salt at a ratio of 3-4:1 fish to salt by weight (20-30% salt by total weight). Pack into earthenware jars or wooden barrels. Weigh down with a stone to submerge. Ferment in a warm place for 6-12 months. Liquid drawn off is fish sauce: rich in amino acids and umami flavor. The remaining paste can be used as a condiment or fertilizer.

Fish sauce production requires large quantities of salt but preserves protein indefinitely and produces a high-value seasoning that stores and transports easily.

## Shellfish Harvesting

#### Oyster Cultivation

Oysters grow in intertidal and shallow subtidal zones along temperate and subtropical coasts. Cultivation begins with spat (larval oyster) collection.

**Spat collectors**: Strings of oyster shells, ceramic tiles, or wooden sticks bundled together and placed in spat-fall areas during summer breeding season. Spat settle on the collectors within 2-4 weeks and begin growing.

**Grow-out**: Transfer collectors to growing areas (intertidal racks, suspended from rafts, or laid on the sea floor). Oysters reach market size (8-12 cm) in 1.5-3 years depending on water temperature and food availability. No feeding required; oysters filter phytoplankton from seawater.

**Harvest**: Collect at low tide by hand or with a short rake. Open with a knife. Eat fresh, or smoke, dry, or pickle for storage.

#### Mussel Cultivation

Mussels settle on any firm surface in the intertidal zone. Cultivation uses ropes or poles.

**Rope culture**: Hang ropes from rafts or longlines in bays and estuaries during spring. Mussel spat settle on the ropes naturally. Mussels grow to harvest size (5-8 cm) in 12-18 months. Harvest by pulling ropes and stripping mussels off by hand.

**Pole culture (bouchot method)**: Wrap mussel spat onto vertical wooden poles set into the intertidal zone. Mesh netting holds them in place until they attach by byssal threads. Harvest by scraping poles at low tide.

#### Clam Beds

Seed clams in sandy or muddy intertidal areas. Mark beds with stakes. Clams grow by filter feeding, requiring no input. Growth to harvest size (5-8 cm) takes 1.5-3 years depending on species and conditions. Harvest by digging with a fork or rake at low tide.

## Safety

**Waterborne parasites**: Freshwater fish in warm climates carry parasitic flukes (*Clonorchis*, *Opisthorchis*) in their flesh. Infection occurs when fish is eaten raw or undercooked. Cook all freshwater fish to an internal temperature of 63°C or above. Freezing at -20°C for 7 days also kills parasites, but this is impractical without modern freezer infrastructure. Salting and smoking at adequate temperatures reduce but do not eliminate all parasitic risk.

**Drowning**: Working in and around water carries inherent risk. Pond banks are slippery with clay and algae. Wading in deep mud can trap legs. Never work alone near deep water. Keep a rope or pole within reach for rescue. Children are at particular risk around ponds; fence or barrier the perimeter in family settlements.

**Hook injuries**: Fishing hooks penetrate skin easily and the barb makes removal difficult. Carry side cutters to snip the hook below the barb if embedded. Push the point through and cut off the barb rather than pulling back against it. Infection from water-contaminated hook wounds can progress rapidly; clean and bandage immediately.

**Water quality hazards**: Stagnant pond water can harbor *Leptospira* bacteria (from rodent urine), *Naegleria fowleri* (in warm freshwater), and harmful algal blooms (cyanobacteria, recognizable by blue-green surface scum). Do not drink untreated pond water. Avoid swimming in or contacting water with visible algal scum. Filter or boil all water drawn from ponds before consumption.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Fish dying in mass | Oxygen depletion from overfeeding or overcast weather | Stop feeding; add fresh water immediately; install emergency aerator (paddle wheel or air compressor) |
| Pond water green and murky | Algal bloom from excess nutrients (over-fertilized) | Reduce manure/fertilizer input; add fresh water to dilute; consider adding filter-feeding fish (silver carp) |
| Fish not growing | Water too cold, overcrowded, or insufficient feed | Monitor temperature (warmwater fish need >18°C); reduce stocking density; increase supplemental feeding |
| Pond leaking | Clay liner cracked or compromised by roots | Drain pond; repair liner with fresh clay (10-15 cm compacted); remove tree roots from pond walls |
| Parasites on fish | Poor water quality or overcrowding | Improve water quality; reduce stocking density; salt bath treatment (3-5% NaCl for 5-10 minutes) |
| Predation (birds, otters) | Unprotected pond | Install netting over pond; use decoy predators; maintain steep pond edges to discourage wading birds |

## See Also

- [Insect Farming](insect-farming.md) — insect meal as fish feed
- [Basic Tools](../foundations/tools-basic.md) — net-making and pond construction tools
- [Food & Agriculture](../foundations/food-agriculture.md) — manure and crop byproducts for pond management
- [Medicine](../health/medicine.md) — fish oil nutrition and waterborne disease
- [Shipping & Maritime](../transport/shipping.md) — coastal aquaculture and open-water fishing
- [Aquaponics](../agriculture/aquaponics.md) — integrated fish-plant production

[← Back to Animals](index.md)
