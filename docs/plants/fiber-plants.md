# Fiber Plants

> **Node ID**: plants.fiber-plants
> **Domain**: [Plants & Botanical Resources](./index.md)
> **Dependencies**: [`plants`](./index.md), [`textiles.spinning`](../textiles/spinning.md)
> **Enables**: `plants.fiber-plants.allium-paniculatum`, `plants.fiber-plants.amaranthus-albus`, [`textiles.fibers`](../textiles/fibers.md)
> **Timeline**: Years 0-10
> **Outputs**: plant_fibers, raw_fiber
> **Critical**: Yes — cordage and textiles from plant fibers are Year 0 necessities for shelter, tools, and clothing


Fiber plants are the botanical source of the cordage, thread, and woven materials that underpin every stage of civilization bootstrapping. Before metal wire or synthetic polymers, all rope, twine, netting, basketry, and textiles came from plant (and animal) fibers. Cordage is a Year 0 necessity — binding spear points to shafts, lashing shelter frames, making snares and fishnets, carrying loads with simple bags. As material culture advances, spun and woven plant fibers become clothing, sailcloth, canvas, sacks, hammocks, and eventually the belts and drive bands for early machinery.

This capability covers the cultivation, harvesting, and primary extraction of bast (stem), leaf, and seed fibers from plant species. The downstream processing of extracted fibers into yarn, cordage, and cloth is covered in [Fiber Preparation](../textiles/fibers.md) and [Spinning](../textiles/spinning.md).

## Fiber Categories by Plant Anatomy

Different plant organs yield fibers with distinct properties, requiring different extraction methods:

- **Bast (stem) fibers**: Extracted from the phloem (inner bark) of certain dicot stems. Long, strong fibers ideal for cordage and textiles. Examples: flax (linen), hemp, jute, ramie, nettle. Require retting to separate fiber bundles from the woody core.
- **Leaf fibers**: Extracted from the leaves of certain monocots. Typically coarser and stiffer than bast fibers, excellent for rope and coarse textiles. Examples: sisal (agave), abacá (Manila hemp), henequen. Extracted by decortication (crushing and scraping).
- **Seed/fruit fibers**: Attached to seeds or fruit husks. Shorter staple length, processed differently from bast/leaf fibers. Examples: cotton (seed fiber), coir (coconut husk fiber).
- **Whole-stem grasses**: Some grasses and reeds are used whole (split or unsplit) for basketry, thatching, and wattle. Not true fiber extraction — see [Structural Plants](./structural-plants.md).

## Fiber Extraction Methods

**[Retting](../glossary/retting.md)** (for bast fibers — flax, hemp, jute, ramie, nettle):

Retting uses moisture and microbial action to decompose the pectins binding fiber bundles to the woody core (shives) and outer bark. The three principal methods:

1. **Water retting**: Submerge bundled stalks in a pond, slow river, or purpose-built retting tank for 5-14 days (temperature dependent — warm water rets faster). Anaerobic bacteria break down pectin. Produces the highest-quality fiber. Test readiness by bending a stalk — fibers should separate cleanly from the woody core. Over-retting weakens fiber significantly.

**Strengths**:
- Highest fiber quality — uniform pectin breakdown produces long, clean, strong fibers
- Fastest retting method — 5-14 days vs. 2-5 weeks for dew retting
- Controllable — water temperature and duration can be adjusted to match conditions
- Produces the finest linen — water-retted flax yields fibers smooth enough for fine cloth
- Consistent results between batches when water temperature is managed

**Weaknesses**:
- Requires a pond, tank, or slow-moving river — not available in all locations
- Water pollution — retting water becomes foul-smelling and depletes oxygen (anaerobic bacterial activity)
- Labor-intensive — stalks must be bundled, weighted down, then retrieved from water
- Over-retting risk — leaving stalks too long weakens fiber significantly; requires frequent testing
- Retting tanks occupy space and require maintenance — purpose-built tanks are a capital investment

2. **Dew retting**: Spread stalks thinly on a grass field, turn periodically. Dew and rainfall provide moisture; aerobic fungi and bacteria do the work. Takes 2-5 weeks depending on climate. Lower quality than water retting but requires no water infrastructure.

**Strengths**:
- No water infrastructure required — uses only dew and rainfall
- Lowest labor input — spread stalks and turn occasionally, no bundling or retrieval
- No water pollution — aerobic decomposition does not produce foul anaerobic byproducts
- Scalable — can be done across any grass field large enough to spread stalks thinly
- Works in any climate with regular dew or rainfall

**Weaknesses**:
- Slowest reliable method — 2-5 weeks vs. 5-14 days for water retting
- Lower fiber quality — uneven pectin breakdown produces coarser, less uniform fibers
- Weather-dependent — drought stalls retting; heavy rain can over-ret and rot the fibers
- Large land area required — stalks must be spread thinly (not stacked) for even moisture exposure
- Less consistent between batches — temperature and humidity vary daily

3. **Stand retting**: Leave cut stalks standing in the field. Slowest method, least labor. Suitable for coarse fiber (rope, sacking) where fine quality is not needed.

**Strengths**:
- Least labor of any method — cut stalks and leave them, no handling until fully retted
- No infrastructure or land preparation — uses the field where the crop grew
- Zero water consumption — relies entirely on natural precipitation and humidity
- Lowest cost — no investment in tanks, ponds, or field preparation

**Weaknesses**:
- Slowest method — 4-8+ weeks depending on weather
- Lowest fiber quality — uneven, coarse fibers suitable only for rope and sacking
- Unreliable — dependent entirely on weather; drought years produce un-retted, unusable stalks
- Risk of total loss — standing stalks can be blown down, eaten by animals, or destroyed by heavy rain

After retting, stalks are dried thoroughly before further processing (breaking, scutching, hackling — see [Fiber Preparation](../textiles/fibers.md)).

**[Decortication](../glossary/decortication.md)** (for leaf fibers — sisal, abacá, henequen):

Crush leaves between rollers or beat them with wooden mallets to separate the fibrous strands from the fleshy pulp. Scrape away residual pulp with a blunt knife or edged wooden blade. Wash extracted fiber strands and dry in the sun. Produces long, stiff fiber bundles suitable for rope, twine, and coarse cloth. Can be done entirely by hand with simple tools.

**[Ginning](../glossary/ginning.md)** (for seed fibers — cotton):

Separate the seed from the fiber. Hand-ginning (finger-picking) processes ~500 g/hour. A single-roller gin (wooden roller against a fixed blade) increases throughput 10x. Seed cotton passes between roller and blade — fiber is pulled through, seeds are crushed or deflected. See [Fiber Preparation](../textiles/fibers.md) for detailed ginning methods.

**[Hand-stripping](../glossary/hand-stripping.md)** (for husk fibers — coir):

Soak coconut husks in water (brackish or fresh) for 2-6 months to soften the pith, then beat with wooden mallets to loosen fibers. Hand-strip long fibers from the softened husk. Coir fiber is exceptionally rot-resistant, making it ideal for marine rope, matting, and erosion control.

## Key Species

Species cataloged in the tech tree with fiber use from the plants database:

| Species | Common Name | Family | Fiber Type | Notes |
|---------|-------------|--------|------------|-------|
| *Allium paniculatum* | Pale garlic | Allioideae | Bast (stem) | Widely cultivated, naturalized across Mediterranean. Tubular hollow leaves yield usable fiber. |
| *Amaranthus albus* | Common tumbleweed | Amaranthaceae | Bast (stem) | Annual herb, native to Americas. Dried stems yield coarse fiber. |

Well-known fiber plants that should be prioritized for cultivation in a bootstrap setting, selected for fiber quality, yield, and historical importance:

| Plant | Scientific Name | Fiber Type | Primary Products | Cultivation |
|-------|----------------|------------|------------------|-------------|
| Flax | *Linum usitatissimum* | Bast (stem) | Linen cloth, thread, cordage, linseed oil | Annual; temperate; sow spring, harvest ~100 days; well-drained soil |
| Hemp | *Cannabis sativa* | Bast (stem) | Rope, canvas, sackcloth, paper | Annual; 2-4 m tall; extremely hardy, minimal water; most widely adapted fiber crop |
| Jute | *Corchorus capsularis* | Bast (stem) | Sacking, burlap, twine | Annual; tropical; requires warm wet climate; 3-4 month growing cycle |
| Ramie | *Boehmeria nivea* | Bast (stem) | Fine cloth, fishing nets, thread | Perennial; subtropical; strongest natural bast fiber; requires degumming |
| Nettle | *Urtica dioica* | Bast (stem) | Cordage, coarse cloth, netting | Perennial; temperate; grows wild everywhere; no cultivation needed — forage |
| Sisal | *Agave sisalana* | Leaf | Rope, twine, mats, dartboards | Perennial; arid/tropical; drought-tolerant; leaves harvested 2-3 years after planting |
| Abacá | *Musa textilis* | Leaf | Marine rope, Manila hemp, tea bags | Perennial; tropical; related to banana; exceptionally strong salt-water-resistant fiber |
| Cotton | *Gossypium* spp. | Seed | Cloth, thread, medical bandaging | Annual shrub; 150-180 frost-free days; warm climate; requires ginning |
| Kenaf | *Hibiscus cannabinus* | Bast (stem) | Rope, paper, sacking | Annual; tropical/subtropical; fast-growing (4-5 m in 150 days) |
| Coir | *Cocos nucifera* | Fruit husk | Marine rope, matting, erosion control | Palm tree; tropical; husk byproduct of coconut food harvest; rot-resistant |

Note: The current plants species catalog (plants.json) contains only 2 species with `primary_use: "fiber"` (Allium paniculatum, Amaranthus albus). The major fiber crops listed above are documented from general botanical and historical knowledge. Adding targeted fiber crop species to the catalog is a future data-enrichment task.

## Cultivation Considerations

Fiber crop cultivation ranges from zero-effort foraging (nettle) to intensive agriculture (cotton):

- **Bast fiber crops** (flax, hemp, jute): Sow densely (flax at 40-60 kg/ha) to produce tall, unbranched stalks with long fibers. Excessive branching shortens fiber length. Harvest before seed maturation for best fiber quality (stalks yellow at bottom third for flax; pollen shedding for hemp).
- **Leaf fiber crops** (sisal, abacá): Perennial plantations — plant once, harvest for 7-15 years. Sisal produces ~25 leaves/year after maturity; each leaf yields 2-3% dry fiber by weight.
- **Cotton**: Requires warm climate, 150+ frost-free days, moderate but reliable water. Very labor-intensive to harvest by hand — each boll must be picked individually. Cottonseed can be pressed for oil (food/lamp fuel), making it a dual-purpose crop.
- **Nettle**: No cultivation required in most temperate zones. Harvest wild stands in late summer when stems are mature. Stands regenerate from rhizomes. Manage by cutting annually to prevent woody overgrowth.
- **Hemp**: The most forgiving fiber crop. Grows on marginal soil, needs minimal fertilizer, suppresses weeds through dense canopy shading. Deep taproot improves soil structure. Historically the most widely cultivated fiber plant for rope and canvas.

## Harvesting and Processing

Timing of harvest critically affects fiber quality:

- **Bast fibers**: Harvest when stalks begin to yellow but before full maturity. At this stage, fiber strength peaks and pectin content is optimal for retting. Pull entire plants (don't cut) for maximum fiber length — root end produces the longest fibers. Tie in bundles (handful-sized) for retting.
- **Leaf fibers**: Cut outer leaves when they begin to droop (2-3 years after planting for sisal). Inner leaves continue growing. Process immediately — decorticate fresh leaves; dried leaves are difficult to strip.
- **Cotton**: Pick open bolls as they mature (not all at once — bolls open progressively over 4-6 weeks). Dry in sun, then gin to remove seeds.
- **Coir**: Husk coconuts at harvest. Soak husks for fiber extraction as needed — dry husks store for months.

After extraction, all plant fibers must be dried thoroughly before storage. Moist fiber molds rapidly and loses strength. Store dried fiber in dry, ventilated conditions protected from rodents.

## Yields and Economics

Approximate dry fiber yields under hand-cultivation conditions:

- Flax: 200-400 kg/ha fiber (plus linseed)
- Hemp: 300-800 kg/ha fiber (1-3 tonnes dry stalk)
- Jute: 1,500-2,500 kg/ha dry fiber (very high yield in tropical climates)
- Sisal: 600-1,000 kg/ha fiber from mature plantation
- Cotton: 500-1,000 kg/ha lint (hand-picked)
- Ramie: 800-1,200 kg/ha fiber (multiple harvests per year from perennial stand)
- Nettle: ~100-200 kg/ha from managed wild stands (low yield but zero input cost)

Labor requirements vary enormously. Cotton requires the most hand-labor per unit fiber (picking individual bolls). Hemp and jute are the most labor-efficient per hectare for bulk fiber. Nettle is free but yields the least per area.

## Flax Processing Detail

Flax (*Linum usitatissimum*) produces the finest plant fiber — linen — and warrants detailed treatment of each processing stage:

**Retting**: The critical step. Bundle stalks in handful-sized sheaves (12-15 cm diameter). Submerge in still water (pond, retting tank) at 15-25°C:
- At 15°C: 10-14 days to full ret
- At 20°C: 7-10 days
- At 25°C: 5-7 days (risk of over-retting increases)
- Test readiness: Snap a stalk — fibers should separate cleanly from the woody shive core without manual pulling. Under-retted stalks resist separation; over-retted fibers are weak and discolored
- Dew retting alternative: Spread stalks on grass field, turn every 2-3 days. Takes 3-5 weeks. Produces coarser, darker fiber but requires no water infrastructure

**Breaking**: Pass dried, retted stalks through a flax break (wooden cradle with hinged blades). Crushes the brittle woody shive into fragments while leaving flexible fiber bundles intact. Break each handful 3-5 times.

**Scutching**: Beat the broken stalks against a flat wooden blade (scutching knife) or scutching mill. Knocks loose shive fragments free from fiber bundles. Yields: approximately 20-25% of retted stalk weight becomes clean fiber; the remainder is shive (usable as fuel or building material).

**Hackling**: Draw scutched fiber through graduated combs (hackles) — coarse (8-12 teeth/dm), medium (15-20), fine (25-35). Longer fibers (line) pass through; shorter broken fibers (tow) are caught in the comb teeth. Hackling grades:
- Rough hackle: Removes remaining shive, aligns fibers. Line fiber length: 30-90 cm
- Fine hackle: Splits fiber bundles, produces smooth, aligned sliver. Tow (short fiber, 5-15 cm) collected separately — spun into coarse yarn for sacking and tow cloth
- Line fiber yield: ~15% of dry stalk weight. Tow fiber yield: ~5-8%

## Hemp Processing

Hemp (*Cannabis sativa*) is the most productive and forgiving bast fiber crop:

**[Dew retting](../glossary/dew-retting.md)** (preferred for hemp): Cut stalks at ground level (hemp grows 2-4 m tall). Leave in the field in rows, turn weekly. Retting takes 3-5 weeks depending on rainfall and temperature. Hemp's thick, woody core requires longer retting than flax. Advantages: no water infrastructure, no pollution, minimal labor. Disadvantage: weather-dependent, coarser fiber.

**[Water retting](../glossary/water-retting.md)** (higher quality): Submerge bundled hemp stalks in water for 4-8 days at 20°C. Hemp rets faster than flax due to higher pectin content. Produces lighter-colored, stronger fiber. The retting water becomes highly polluted — must be isolated from drinking supply.

**Decortication for hemp**: For coarse applications (rope, sacking), mechanical decortication bypasses retting entirely. Crush green stalks between fluted rollers, then scrape away woody core with a blade. Produces coarse, green-tinted fiber suitable for rope and industrial textiles. Less labor than retting but lower quality.

Hemp fiber length: 0.5-5.5 m (bundle length); individual fiber cells 0.5-5.0 cm long, 10-50 μm diameter. Tensile strength: 550-900 MPa (fiber bundle). Hemp produces 2-3x more fiber per hectare than flax under equivalent conditions.

## Cotton Cultivation Detail

Cotton (*Gossypium* spp.) is unique as a seed fiber — the only widely cultivated plant fiber that does not require retting or decortication:

**Climate requirements**:
- 150-200 frost-free days minimum (optimal: 180+ days)
- 600-1,200 mm water during growing season (or equivalent irrigation)
- Mean temperature 20-30°C during boll development; below 15°C growth stops
- Well-drained, slightly alkaline soil (pH 6.0-8.0); sensitive to waterlogging

**Cultivation cycle**:
- Sow when soil temperature reaches 16°C for 3 consecutive days (typically 2-3 weeks after last frost)
- Row spacing: 75-100 cm; plant density: 80,000-120,000 plants/ha
- First flowers appear 60-70 days after planting; bolls open 50-70 days after flowering
- Hand-picking: 20-50 kg seed cotton per person per day. Multiple passes through field as bolls open progressively over 4-6 weeks
- Gin turnout: 30-42% lint by weight (remainder is cottonseed — press for oil yielding 15-20% by weight)

**Varieties by climate**: Upland cotton (*G. hirsutum*) — temperate/subtropical, 90% of world production; Pima/Egyptian (*G. barbadense*) — hot arid, extra-long staple (33-38 mm); Tree cotton (*G. arboreum*) — tropical, drought-tolerant, short staple.

## Jute, Ramie, and Sisal

**Jute (*Corchorus capsularis*, *C. olitorius*)**:
- Highest yielding bast fiber: 1,500-2,500 kg/ha dry fiber
- Growing cycle: 90-120 days; requires warm (25-35°C), humid climate with 1,500-2,500 mm rainfall
- Harvest: cut stalks at ground level before pod formation. Retting 8-20 days in slow-moving water. Strip fiber from stalk by hand under water
- Jute fiber: 1-4 m long, relatively weak (tensile strength ~400 MPa) but inexpensive. Primary use: sacking (burlap), carpet backing, erosion control fabric
- Jute sticks (woody core after retting): 4-5 tonnes/ha, used as fuel and fencing

**Ramie (*Boehmeria nivea*)**:
- Strongest natural bast fiber: tensile strength 870-1,100 MPa (fiber cell), 5-6x stronger than cotton
- Perennial: harvest 3-6 times/year from established stands; productive for 6-8 years
- Yield: 800-1,200 kg/ha dry fiber per year
- **Degumming requirement**: Raw ramie contains 20-30% gum (pectin and hemicellulose). Must be degummed before spinning. Chemical degumming: boil in 1-2% NaOH solution for 1-2 hours. Biological degumming: ferment in water 24-48 hours
- Fiber length: 10-20 cm individual cells; white, silky luster. Used for fishing nets (resists rot in water), fine cloth

**Sisal (*Agave sisalana*)**:
- Leaf fiber: decorticate fresh leaves by crushing between rollers and scraping
- Yield: 600-1,000 kg/ha dry fiber from mature plantation; 25-30 leaves/plant/year; 2-3% fiber by leaf weight
- Plantation life: 7-12 years productive. First harvest 2-3 years after planting
- Tensile strength: 350-600 MPa. Resists degradation in saltwater — used for marine rope, twine
- Drought-tolerant; grows in semi-arid tropical regions on poor soils

## Fiber Testing and Quality

Assessing fiber quality without modern laboratory equipment:

**Tensile strength (simple test)**: Hang a known weight from a single fiber bundle of measured cross-section. Compare breaking weight to diameter. Relative ranking: ramie > hemp > flax > nettle > jute > sisal > coir.

**Fineness ( tactile assessment)**: Rub fiber between thumb and forefinger. Finer fiber (flax line, cotton) feels smooth and silky; coarse fiber (sisal, coir) feels scratchy and stiff. Fineness correlates with spinnability — finer fibers produce finer yarn.

**Length distribution**: Separate a handful of hackled fiber. Measure longest fiber (line) and note proportion of short fiber (tow). High line-to-tow ratio indicates better processing quality. Flax line: 30-90 cm; tow: 5-15 cm. Hemp line: 50-150 cm.

**Color and cleanliness**: Clean, well-retted fiber is pale (flax: light gold; hemp: light gray-brown). Dark, muddy fiber indicates over-retting or dirty retting water. Green patches indicate under-retting.

## Fiber Blending for Application

Different applications benefit from combining fibers with complementary properties:

| Application | Blend | Rationale |
|-------------|-------|-----------|
| General rope | Hemp + jute (70:30) | Hemp provides strength; jute adds bulk at lower cost |
| Marine rope | Abacá or sisal (100%) | Saltwater resistance; abacá preferred for highest strength |
| Fine cloth | Flax line (100%) | Longest, finest bast fiber produces smooth linen |
| Coarse sacking | Jute (100%) or hemp tow | Economical, adequate strength for bags |
| Fishing nets | Ramie (100%) or hemp | Rot resistance in water; ramie preferred where available |
| Canvas/tent cloth | Hemp (100%) | Water resistance, durability, mildew resistance |
- Cotton-linen blends (50:50) combine cotton's softness with linen's strength for clothing
- Nettle fiber can substitute for flax in any application with comparable results; nettle cloth historically called " Scots cloth"

## Safety & Hazards

- **Skin irritation**: Nettle stems and leaves cause contact dermatitis (urticaria) from formic acid and histamine in trichomes. Wear thick gloves when harvesting. The irritation fades within hours and does not cause lasting damage.
- **Retting water contamination**: Water retting produces foul-smelling, bacteria-laden water. Do not ret in drinking water sources. Retting ponds should be downstream and separate from water supply. The organic load from retting can deplete oxygen and kill fish in small water bodies.
- **Dust inhalation**: Processing dry fiber (hacking, scutching) generates fine dust. Work in well-ventilated areas. Prolonged exposure causes byssinosis (brown lung) — a chronic respiratory condition.
- **Hemp confusion**: Industrial hemp (*Cannabis sativa* grown for fiber) contains negligible psychoactive compounds but is visually identical to drug varieties. In a bootstrap context this distinction is irrelevant — all hemp is a fiber crop.

## Dependencies

- Requires: [Plants & Botanical Resources](./index.md) (tool) — botanical knowledge and species identification
- Feeds into: [Fiber Preparation](../textiles/fibers.md) (material — raw_fiber)
- Feeds into: [Spinning](../textiles/spinning.md) (material — plant_fibers)
- Related: [Edible Plants](./edible-plants.md) (dual-use species — flax seeds, agave, coconut)
- Related: [Structural Plants](./structural-plants.md) (thatching and wattle materials)



[← Back to Plants](index.md)
