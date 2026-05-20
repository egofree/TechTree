# Fiber Plants

> **Node ID**: plants.fiber-plants
> **Domain**: [Plants & Botanical Resources](./)
> **Timeline**: Years 0-10
> **Outputs**: plant_fibers, raw_fiber

### Overview

Fiber plants are the botanical source of the cordage, thread, and woven materials that underpin every stage of civilization bootstrapping. Before metal wire or synthetic polymers, all rope, twine, netting, basketry, and textiles came from plant (and animal) fibers. Cordage is a Year 0 necessity — binding spear points to shafts, lashing shelter frames, making snares and fishnets, carrying loads with simple bags. As material culture advances, spun and woven plant fibers become clothing, sailcloth, canvas, sacks, hammocks, and eventually the belts and drive bands for early machinery.

This capability covers the cultivation, harvesting, and primary extraction of bast (stem), leaf, and seed fibers from plant species. The downstream processing of extracted fibers into yarn, cordage, and cloth is covered in [Fiber Preparation](../textiles/fibers.md) and [Spinning](../textiles/spinning.md).

### Fiber Categories by Plant Anatomy

Different plant organs yield fibers with distinct properties, requiring different extraction methods:

- **Bast (stem) fibers**: Extracted from the phloem (inner bark) of certain dicot stems. Long, strong fibers ideal for cordage and textiles. Examples: flax (linen), hemp, jute, ramie, nettle. Require retting to separate fiber bundles from the woody core.
- **Leaf fibers**: Extracted from the leaves of certain monocots. Typically coarser and stiffer than bast fibers, excellent for rope and coarse textiles. Examples: sisal (agave), abacá (Manila hemp), henequen. Extracted by decortication (crushing and scraping).
- **Seed/fruit fibers**: Attached to seeds or fruit husks. Shorter staple length, processed differently from bast/leaf fibers. Examples: cotton (seed fiber), coir (coconut husk fiber).
- **Whole-stem grasses**: Some grasses and reeds are used whole (split or unsplit) for basketry, thatching, and wattle. Not true fiber extraction — see [Structural Plants](./structural-plants.md).

### Fiber Extraction Methods

**Retting** (for bast fibers — flax, hemp, jute, ramie, nettle):

Retting uses moisture and microbial action to decompose the pectins binding fiber bundles to the woody core (shives) and outer bark. The three principal methods:

1. **Water retting**: Submerge bundled stalks in a pond, slow river, or purpose-built retting tank for 5-14 days (temperature dependent — warm water rets faster). Anaerobic bacteria break down pectin. Produces the highest-quality fiber. Test readiness by bending a stalk — fibers should separate cleanly from the woody core. Over-retting weakens fiber significantly.
2. **Dew retting**: Spread stalks thinly on a grass field, turn periodically. Dew and rainfall provide moisture; aerobic fungi and bacteria do the work. Takes 2-5 weeks depending on climate. Lower quality than water retting but requires no water infrastructure.
3. **Stand retting**: Leave cut stalks standing in the field. Slowest method, least labor. Suitable for coarse fiber (rope, sacking) where fine quality is not needed.

After retting, stalks are dried thoroughly before further processing (breaking, scutching, hackling — see [Fiber Preparation](../textiles/fibers.md)).

**Decortication** (for leaf fibers — sisal, abacá, henequen):

Crush leaves between rollers or beat them with wooden mallets to separate the fibrous strands from the fleshy pulp. Scrape away residual pulp with a blunt knife or edged wooden blade. Wash extracted fiber strands and dry in the sun. Produces long, stiff fiber bundles suitable for rope, twine, and coarse cloth. Can be done entirely by hand with simple tools.

**Ginning** (for seed fibers — cotton):

Separate the seed from the fiber. Hand-ginning (finger-picking) processes ~500 g/hour. A single-roller gin (wooden roller against a fixed blade) increases throughput 10x. Seed cotton passes between roller and blade — fiber is pulled through, seeds are crushed or deflected. See [Fiber Preparation](../textiles/fibers.md) for detailed ginning methods.

**Hand-stripping** (for husk fibers — coir):

Soak coconut husks in water (brackish or fresh) for 2-6 months to soften the pith, then beat with wooden mallets to loosen fibers. Hand-strip long fibers from the softened husk. Coir fiber is exceptionally rot-resistant, making it ideal for marine rope, matting, and erosion control.

### Key Species

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

### Cultivation Considerations

Fiber crop cultivation ranges from zero-effort foraging (nettle) to intensive agriculture (cotton):

- **Bast fiber crops** (flax, hemp, jute): Sow densely (flax at 40-60 kg/ha) to produce tall, unbranched stalks with long fibers. Excessive branching shortens fiber length. Harvest before seed maturation for best fiber quality (stalks yellow at bottom third for flax; pollen shedding for hemp).
- **Leaf fiber crops** (sisal, abacá): Perennial plantations — plant once, harvest for 7-15 years. Sisal produces ~25 leaves/year after maturity; each leaf yields 2-3% dry fiber by weight.
- **Cotton**: Requires warm climate, 150+ frost-free days, moderate but reliable water. Very labor-intensive to harvest by hand — each boll must be picked individually. Cottonseed can be pressed for oil (food/lamp fuel), making it a dual-purpose crop.
- **Nettle**: No cultivation required in most temperate zones. Harvest wild stands in late summer when stems are mature. Stands regenerate from rhizomes. Manage by cutting annually to prevent woody overgrowth.
- **Hemp**: The most forgiving fiber crop. Grows on marginal soil, needs minimal fertilizer, suppresses weeds through dense canopy shading. Deep taproot improves soil structure. Historically the most widely cultivated fiber plant for rope and canvas.

### Harvesting and Processing

Timing of harvest critically affects fiber quality:

- **Bast fibers**: Harvest when stalks begin to yellow but before full maturity. At this stage, fiber strength peaks and pectin content is optimal for retting. Pull entire plants (don't cut) for maximum fiber length — root end produces the longest fibers. Tie in bundles (handful-sized) for retting.
- **Leaf fibers**: Cut outer leaves when they begin to droop (2-3 years after planting for sisal). Inner leaves continue growing. Process immediately — decorticate fresh leaves; dried leaves are difficult to strip.
- **Cotton**: Pick open bolls as they mature (not all at once — bolls open progressively over 4-6 weeks). Dry in sun, then gin to remove seeds.
- **Coir**: Husk coconuts at harvest. Soak husks for fiber extraction as needed — dry husks store for months.

After extraction, all plant fibers must be dried thoroughly before storage. Moist fiber molds rapidly and loses strength. Store dried fiber in dry, ventilated conditions protected from rodents.

### Yields and Economics

Approximate dry fiber yields under hand-cultivation conditions:

- Flax: 200-400 kg/ha fiber (plus linseed)
- Hemp: 300-800 kg/ha fiber (1-3 tonnes dry stalk)
- Jute: 1,500-2,500 kg/ha dry fiber (very high yield in tropical climates)
- Sisal: 600-1,000 kg/ha fiber from mature plantation
- Cotton: 500-1,000 kg/ha lint (hand-picked)
- Ramie: 800-1,200 kg/ha fiber (multiple harvests per year from perennial stand)
- Nettle: ~100-200 kg/ha from managed wild stands (low yield but zero input cost)

Labor requirements vary enormously. Cotton requires the most hand-labor per unit fiber (picking individual bolls). Hemp and jute are the most labor-efficient per hectare for bulk fiber. Nettle is free but yields the least per area.

### Safety & Hazards

- **Skin irritation**: Nettle stems and leaves cause contact dermatitis (urticaria) from formic acid and histamine in trichomes. Wear thick gloves when harvesting. The irritation fades within hours and does not cause lasting damage.
- **Retting water contamination**: Water retting produces foul-smelling, bacteria-laden water. Do not ret in drinking water sources. Retting ponds should be downstream and separate from water supply. The organic load from retting can deplete oxygen and kill fish in small water bodies.
- **Dust inhalation**: Processing dry fiber (hacking, scutching) generates fine dust. Work in well-ventilated areas. Prolonged exposure causes byssinosis (brown lung) — a chronic respiratory condition.
- **Hemp confusion**: Industrial hemp (*Cannabis sativa* grown for fiber) contains negligible psychoactive compounds but is visually identical to drug varieties. In a bootstrap context this distinction is irrelevant — all hemp is a fiber crop.

### Dependencies

- Requires: [Plants & Botanical Resources](./) (tool) — botanical knowledge and species identification
- Feeds into: [Fiber Preparation](../textiles/fibers.md) (material — raw_fiber)
- Feeds into: [Spinning](../textiles/spinning.md) (material — plant_fibers)
- Related: [Edible Plants](./edible-plants.md) (dual-use species — flax seeds, agave, coconut)
- Related: [Structural Plants](./structural-plants.md) (thatching and wattle materials)

---

*Part of the [Bootciv Tech Tree](../) • [Plants](./) • [All Domains](../)*