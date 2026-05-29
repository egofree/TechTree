# Dye Plants

> **Node ID**: plants.dye-plants
> **Domain**: [Plants & Botanical Resources](./index.md)
> **Dependencies**: [`plants`](./index.md), [`textiles.dyeing`](../textiles/dyeing.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 5-10
> **Outputs**: natural_dyes, plant_pigments
> **Critical**: No — color is important for signaling and trade but not strictly required for survival


Plants that yield natural colorants for dyeing textiles, leather, wood, ink, and coatings. Natural dyes have been the primary source of color for human material culture from prehistory through the 19th century, when synthetic aniline dyes superseded them. In a bootstrap context, dye plants provide the only practical path to colored textiles before the organic chemistry infrastructure needed for synthetic dyes exists. Color serves not only aesthetics but signaling (military uniforms, trade goods, social markers) and functional purposes (UV protection, mildew resistance from tannin-rich dyes).

This capability covers the cultivation, harvesting, and primary extraction of dye substances from plant material. The downstream application of dyes to fiber and cloth is covered in [Dyeing](../textiles/dyeing.md).

## Dye Extraction Methods

The three principal methods for extracting color from plant material, listed in order of increasing complexity:

1. **Hot water extraction (decoction)**: Chop or crush fresh or dried plant material, simmer in water at 60-90°C for 30-60 minutes. Strain through cloth. This is the simplest and most widely applicable method, effective for most dye plants including madder, weld, walnut hulls, and onion skins. The dye bath can be reused until exhausted — typically 2-3 dips per batch of material.

2. **Fermentation extraction**: Used primarily for indigo precursors from woad and indigo plants. Crush fresh leaves, pack into a vat with warm (40-50°C) alkaline water (traditionally wood ash lye or stale urine provides the alkali). Ferment for 12-48 hours, stirring occasionally. The indican in the leaves hydrolyzes to indoxyl, which oxidizes to insoluble blue indigo pigment when the liquor is beaten with air. The pigment settles as sludge, is collected, pressed, and dried into indigo cakes.

3. **Solvent extraction**: For concentrated dyes or when water extraction is inefficient. Uses alcohol (ethanol from fermentation) or alkaline solutions to pull pigments from tough plant material like bark, roots, and heartwood. Requires a closed vessel to prevent solvent evaporation. Yields more concentrated dye stuff suitable for trade or storage.

**Hot water extraction (decoction)**:

**Strengths**:
- Simplest method — requires only a pot, water, and heat source
- Works for the majority of dye plants (madder, weld, walnut, onion skins)
- No special equipment or chemicals — water is the universal solvent
- Dye bath reusable 2-3 times — multiple dips per batch of material
- Fast — 30-60 minutes to produce a working dye bath

**Weaknesses**:
- Cannot extract water-insoluble pigments — indigo precursors require fermentation instead
- Heat degrades some delicate pigments — madder alizarin breaks down above 85°C
- Dilute dye bath — large volumes of water needed relative to pigment yield
- Bulky to store and transport — water-based dye baths are heavy and spoil within days
- Inefficient for tough materials — bark and heartwood release little pigment in plain water

**Fermentation extraction**:

**Strengths**:
- Only method for indigo precursor extraction — no alternative for blue dye production
- Uses free materials — plant leaves, water, and alkaline ash lye (no purchased chemicals)
- Produces concentrated, storable indigo cakes — a trade-grade commodity
- Low technology — requires only a vat, warmth, and time

**Weaknesses**:
- Slow — 12-48 hours fermentation plus settling time
- Unpleasant — anaerobic fermentation produces strong odors
- Requires fresh leaf material — dried leaves lose indican content rapidly
- Low yield — woad produces only 0.1-0.2% indigo by weight (1-2 g per kg leaves)
- Temperature-sensitive — must maintain 40-50°C; too hot kills bacteria, too cold stalls fermentation

**Solvent extraction**:

**Strengths**:
- Highest dye concentration — produces concentrated dyestuff suitable for trade and long-term storage
- Extracts pigments from tough materials — bark, roots, and heartwood that resist water extraction
- Smaller volumes than water extraction — concentrated product is lighter to transport
- Works for pigments that are poorly water-soluble — alcohol and alkaline solutions reach compounds water cannot

**Weaknesses**:
- Requires closed vessel — solvent evaporation wastes alcohol and creates fire hazard
- Higher technology threshold — needs ethanol production (distillation) or prepared alkaline solutions
- More expensive per batch — solvent costs exceed water extraction significantly
- Fire risk with alcohol solvents — ethanol vapors are flammable
- Not needed for most common dye plants — overkill when simple water extraction suffices

## Mordanting and Color Fixation

Most natural dyes are not substantive — they do not bond directly to fiber and require a mordant to achieve wash-fastness. The choice of mordant dramatically shifts the final color from a given dye plant. Common mordants available in a bootstrap context:

- **Alum (potassium aluminum sulfate)**: The universal mordant. Sourced from alunite stone (KAl(SO₄)₂(OH)₆) by roasting and leaching, or from natural alum deposits near volcanic soils. Brightens and clarifies most dye colors.
- **Iron (ferrous sulfate)**: Darkens and "saddens" colors — yellows become olive greens, blues become grays, pinks become purples. Made by dissolving iron scraps in vinegar. Overuse weakens protein fibers.
- **Tannin**: Oak galls, sumac leaves, pomegranate rinds, and chestnut bark provide tannins. Essential as a pre-mordant for cellulose fibers (linen, cotton) to help alum bond. Also useful as a standalone brown dye.
- **Copper (copper sulfate)**: Shifts yellows toward green and brightens greens. Made by dissolving copper in acid. Toxic — handle with care.

See [Dyeing](../textiles/dyeing.md) for detailed mordant preparation procedures and fiber-specific protocols.

## Color Range and Key Species

Different plant organs produce different color families. Understanding which part to harvest and when is essential for predictable results:

| Color | Primary Plant Sources | Plant Part | Notes |
|-------|----------------------|------------|-------|
| Blue | Indigo (*Indigofera tinctoria*), woad (*Isatis tinctoria*) | Leaves | Indigo is unique — no mordant needed, applied via reduction vat |
| Red | Madder (*Rubia tinctorum*), brazilwood (*Caesalpinia echinata*) | Roots, heartwood | Madder roots need 2-3 years growth; extract at 70-80°C max |
| Yellow | Weld (*Reseda luteola*), dyer's broom (*Genista tinctoria*), goldenrod (*Solidago*) | Aerial parts | Weld gives the clearest yellow; harvest at flowering peak |
| Orange | Coreopsis, dyer's chamomile (*Anthemis tinctoria*) | Flowers | Often achieved by madder at low concentration with tin mordant |
| Green | Weld + indigo overdye, or natural gray-green from plant tops | Aerial parts | True green typically requires a two-bath process |
| Brown | Walnut hulls, oak bark, cutch (*Acacia catechu*), tea | Hulls, bark | Walnut gives rich brown with no mordant needed |
| Black | Oak galls + iron, or indigo + madder + iron | Galls, leaves | Always an overdye — no single plant gives true black |
| Purple | Logwood (*Haematoxylum campechianum*), bedstraw + iron | Heartwood, roots | Logwood was a major colonial-era trade commodity |

## Common Dye Plants

Well-known dye plants that should be prioritized for cultivation in a bootstrap setting, selected for color yield, ease of cultivation, and historical importance:

| Plant | Scientific Name | Color | Part Used | Cultivation |
|-------|----------------|-------|-----------|-------------|
| True indigo | *Indigofera tinctoria* | Blue | Leaves | Tropical/subtropical perennial; annual in temperate zones |
| Woad | *Isatis tinctoria* | Blue | Leaves | Hardy biennial; temperate climate; lower indigo yield than true indigo |
| Madder | *Rubia tinctorum* | Red | Roots | Perennial; harvest roots at 2-3 years; needs support to climb |
| Weld | *Reseda luteola* | Yellow | Aerial parts | Biennial; grows in poor soil; highest natural yellow lightfastness |
| Dyer's broom | *Genista tinctoria* | Yellow | Aerial parts | Perennial shrub; hardy, drought-tolerant |
| Dyer's chamomile | *Anthemis tinctoria* | Yellow-orange | Flowers | Perennial; easy to grow |
| Walnut | *Juglans regia* | Brown | Green hulls | Tree; hulls from nut harvest provide abundant brown dye |
| Coreopsis | *Coreopsis tinctoria* | Orange-red | Flowers | Annual; prolific bloomer |
| Japanese indigo | *Persicaria tinctoria* | Blue | Leaves | Annual; more cold-tolerant than true indigo |
| Safflower | *Carthamus tinctorius* | Yellow/pink | Flowers | Annual; pink requires careful extraction |
| Pomegranate | *Punica granatum* | Yellow-brown | Rind | Tree; rind is both dye and tannin mordant |
| Saint John's wort | *Hypericum perforatum* | Red-yellow | Aerial parts | Perennial; color depends on mordant |
| Bedstraw | *Galium verum* | Red-yellow | Roots | Perennial; related to madder |
| Rhubarb | *Rheum spp.* | Yellow | Roots | Perennial; also edible |

Note: The current plants species catalog (plants.json) does not yet include dedicated dye plant entries. The species listed above are documented from general botanical and historical knowledge. Adding targeted dye species to the catalog is a future data-enrichment task.

## Woad — *Isatis tinctoria* (Brassicaceae)

Woad is the only practical source of blue dye in temperate climates. It was the primary blue dye plant of Europe from the Iron Age through the Middle Ages, until supplanted by imported indigo in the 16th century.

**Cultivation**: Hardy biennial. Sow seeds in spring (2-3 kg/ha), thin to 20 cm spacing. First-year rosette leaves harvested for dye. Overwinters as a rosette, flowers and sets seed in year two. Tolerates poor, alkaline soils. Yield: 3-5 tonnes fresh leaves/ha from first-year plants.

**Indigo extraction (fermentation process)**:
1. Harvest first-year leaves (June-September). Crush or grind fresh leaves to break cell walls
2. Pack crushed leaves into a wooden vat or clay-lined pit. Add warm (25-30°C) water to cover. Add alkali: wood ash lye (potassium carbonate, pH 9-10) or stale urine (ammonia)
3. Ferment for 12-15 days at 25-30°C. The glucoside isatan B hydrolyzes to indoxyl. Stir every 2-3 days. The liquor turns yellow-green and develops a characteristic sharp smell
4. Beat the fermented liquor vigorously with paddles for 15-30 minutes to introduce air. Indoxyl oxidizes to insoluble blue indigo pigment (indigotin). Blue froth forms on the surface
5. Allow pigment to settle (2-4 hours). Decant supernatant liquid. Collect blue sludge, press into cakes, dry
6. **Yield**: approximately 1-2 g indigo pigment per kg fresh woad leaves (0.1-0.2% extraction rate). This is 5-10x lower than true indigo (*Indigofera tinctoria*, which yields 0.5-2% indigo from leaves)

**Application**: Indigo pigment is insoluble in water. To dye fiber, the pigment must be reduced (indigo vat) using a reducing agent (fermented bran, urine, or later, sodium hydrosulfite). The reduced form (leuco-indigo, yellow-green) is water-soluble and penetrates fiber. Upon exposure to air, it re-oxidizes to blue indigo, trapped permanently within the fiber. No mordant required — indigo is a substantive (vat) dye.

## Madder — *Rubia tinctorum* (Rubiaceae)

Madder roots produce the most important natural red dye, used since antiquity (evidence from 3,000 BCE Egypt). The active dye compound is alizarin (1,2-dihydroxyanthraquinone), along with purpurin and other anthraquinones.

**Cultivation**: Perennial climbing plant. Sow seeds in spring or plant root cuttings. Requires support (trellis or poles) — stems reach 1-2 m. Prefers deep, well-drained, slightly alkaline soil (pH 7.0-8.0). Roots need 2-3 years to accumulate sufficient dye content. Plants are productive for 5-10 years.

**Harvesting**: Dig roots in autumn (September-November) after 2-3 years' growth. Autumn harvest yields highest alizarin concentration (peaks as top growth dies back). Wash thoroughly, dry slowly in shade. Roots may be used whole, chopped, or ground to powder. Dried roots store for 2+ years. Yield: 2,000-4,000 kg dried root/ha from a 3-year-old planting.

**Dye extraction**: Simmer dried, chopped roots in water at 70-80°C (do not boil — temperatures above 85°C degrade alizarin and produce duller browns) for 60-90 minutes. Strain. The dye bath is deep red-orange. Multiple extractions from the same roots (3-4 baths of decreasing intensity) maximize yield.

**Mordant requirements**: Madder requires alum mordant on protein fibers (wool, silk) for bright red. On cellulose fibers (cotton, linen), use tannin pre-mordant followed by alum. Iron mordant shifts color toward deep purple-brown. Tin mordant brightens to orange-red (but tin is harsh on fibers and rarely available early).

**Colorfastness**: Excellent lightfastness (rating 6-7 on 8-point blue wool scale). Good wash-fastness when properly mordanted. Alizarin is one of the most stable natural dye compounds — madder-dyed textiles from ancient Egypt retain visible red color after 5,000 years.

## Weld — *Reseda luteola* (Resedaceae)

Weld produces the clearest, most lightfast yellow of any natural dye plant. Known since the Neolithic (identified on Iron Age textile finds from Hallstatt, Austria).

**Cultivation**: Biennial or annual. Sow in spring on well-drained soil. Tolerates poor, chalky, marginal land unsuitable for food crops. First year produces a rosette; second year sends up flower spikes to 1.5 m. Harvest entire aerial parts at full flower (June-July) when luteolin concentration peaks. Yield: 1,500-3,000 kg fresh aerial parts/ha.

**Active compound**: Luteolin (a flavone) and derivatives. Concentration peaks at flowering — earlier harvest gives pale yellow; later (seed set) gives duller color. Leaves and flower spikes both contain dye; stems contain less.

**Dye extraction**: Simmer fresh or dried aerial parts in water at 80-90°C for 45-60 minutes. Strain. Dye bath is bright yellow-green. Use at 50-100% weight of fiber (WOF) for dried plant material; 200% WOF for fresh. Alum mordant produces clear, bright yellow. Iron mordant shifts to olive green.

**Colorfastness**: Best lightfastness of any natural yellow dye (rated 6-7 on blue wool scale). This is why weld was the primary yellow dye of the European textile industry for over 2,000 years, used for the yellow component of the Lincoln Green (weld yellow + woad blue).

## Walnut — *Juglans regia* (Juglandaceae)

Walnut hulls produce a rich, lightfast brown dye that requires no mordant — one of the few substantive non-indigo natural dyes.

**Cultivation**: Deciduous tree, 15-25 m. Requires 180+ frost-free days; deep, well-drained soil. Begins producing nuts at 5-8 years; full production at 15-20 years. A mature tree yields 50-100 kg nuts/year. The green hulls surrounding the shell are the dye source — a dual-purpose crop (food + dye).

**Harvesting for dye**: Collect green hulls at nut harvest (autumn). Hulls must be processed green (before they turn black and decompose). Each nut yields 15-25 g of green hull material. A tree yielding 80 kg nuts produces approximately 15-25 kg green hulls for dye.

**Dye extraction**: Simmer green hulls in water at 80-90°C for 60 minutes. Strain. The dye bath is deep brown. No mordant needed — juglone (5-hydroxy-1,4-naphthoquinone) bonds directly to protein fibers. On wool, produces medium to dark brown depending on concentration (30-60% WOF). On cotton, produces lighter tan. Iron mordant deepens to near-black.

**Colorfastness**: Excellent lightfastness and wash-fastness. Juglone is chemically stable and forms covalent bonds with protein fiber. One of the most reliable and easy-to-use natural dyes. Also functions as a mild insect repellent on dyed fabric.

## Cultivation Yields per Hectare

Approximate annual dry dye material yields under hand cultivation:

| Plant | Dry Material Yield (kg/ha) | Dye Extraction Rate | Dye per ha (kg) | Primary Color |
|-------|---------------------------|-------------------|-----------------|---------------|
| Woad (fresh leaves) | 3,000-5,000 | 0.1-0.2% indigo | 3-10 | Blue |
| True indigo (fresh leaves) | 4,000-6,000 | 0.5-2.0% indigo | 20-120 | Blue |
| Madder (dried root, 3-yr) | 2,000-4,000 | 2-4% alizarin | 40-160 | Red |
| Weld (dried aerial parts) | 1,000-2,000 | 1-2% luteolin | 10-40 | Yellow |
| Walnut (green hulls, mature trees) | 1,500-3,000 (mixed orchard) | 5-10% juglone | 75-300 | Brown |

True indigo is the most productive blue dye source by 5-10x over woad. Where climate permits (frost-free tropical/subtropical), indigo (*Indigofera tinctoria*) should always be preferred over woad for blue.

## Mordant Requirements by Plant and Fiber

| Dye Plant | Wool (protein) | Cotton/Linen (cellulose) | Notes |
|-----------|---------------|--------------------------|-------|
| Woad/indigo | None (vat dye) | None (vat dye) | Substantive — no mordant needed |
| Madder | Alum (15-20% WOF) | Tannin + Alum (10% tannin, 15-20% alum) | Cellulose requires tannin pre-mordant |
| Weld | Alum (15-20% WOF) | Tannin + Alum | Alum brightens; iron shifts to olive |
| Walnut | None (substantive) | Alum optional (deepens) | One of few substantive brown dyes |
| Coreopsis | Alum (15-20% WOF) | Tannin + Alum | Tin shifts to bright orange |
| Pomegranate rind | None (high tannin) | None (acts as own mordant) | Produces yellow-brown; tannin-rich |
| Oak galls | Iron (5-10% WOF) | Iron | Produces blue-black; tannin content very high |

## Colorfastness Reference

Lightfastness and wash-fastness ratings for key natural dyes (8-point scale; 8 = excellent):

| Dye Source | Color | Lightfastness (protein fiber) | Wash-fastness | Notes |
|-----------|-------|------------------------------|---------------|-------|
| Indigo (woad/indigo) | Blue | 7-8 | 4-5 | Excellent lightfastness; moderate wash-fastness (gradual fading with repeated washing) |
| Madder (alizarin) | Red | 6-7 | 4-5 | Best red lightfastness of any natural dye |
| Weld (luteolin) | Yellow | 6-7 | 4 | Best yellow lightfastness; natural yellows generally fade faster than blues/reds |
| Walnut (juglone) | Brown | 7-8 | 5 | Excellent both; substantive dye bonds tightly |
| Oak gall + iron | Black | 6-7 | 4-5 | Iron-tannate black; slight browning over decades |
| Coreopsis | Orange | 4-5 | 3-4 | Moderate lightfastness — fades to lighter orange with UV exposure |
| Safflower (carthamin) | Pink | 2-3 | 2-3 | Poor lightfastness — fades significantly within months. Not suitable for permanent color |

## Cultivation Considerations

Dye plant cultivation integrates into existing agricultural patterns without requiring specialized equipment:

- **Annuals** (weld, coreopsis, safflower, Japanese indigo): Sow from seed each year. Can rotate with food crops.
- **Biennials** (woad, weld in cold climates): Establish in year one, harvest dye material in year two. Allow some plants to set seed for continuation.
- **Perennials** (madder, dyer's broom, shrubs): Plant once, harvest for years. Madder roots need 2-3 years before first harvest. Dedicate permanent beds.
- **Trees** (walnut, pomegranate, brazilwood): Long-term investment. Walnut trees produce nuts and dye hulls simultaneously — dual-purpose.

Most dye plants tolerate poor soils and require minimal inputs beyond weeding and moderate water. Weld and woad grow well on marginal land unsuitable for food crops.

## Harvesting and Processing

Timing affects dye yield significantly:

- **Leaves** (indigo, woad): Harvest before flowering when indican/glucosinolate levels peak. Multiple harvests per season possible.
- **Roots** (madder, bedstraw): Dig in autumn after 2-3 years of growth when pigment concentration is highest. Wash, dry, and store whole; chop just before use.
- **Flowers** (weld, coreopsis, chamomile): Pick at full bloom. Dry in shade to preserve color.
- **Hulls and bark** (walnut, oak): Collect green walnut hulls at nut harvest. Bark from pruned branches — never strip bark from live trees in rings.

Fresh plant material gives stronger colors than dried, but dried material stores for years and enables trade. Dry all material in shade to prevent UV degradation of pigments.

## Yield and Economics

Approximate dry plant material needed per 100g of wool fiber (alum-mordanted):

- Madder root: 50-100g (deep red)
- Weld: 100-200g (clear yellow)
- Walnut hulls: 50-100g (rich brown)
- Woad/indigo leaves: 500-1000g fresh (1-2g indigo pigment extracted)
- Coreopsis flowers: 50-100g (orange)

Indigo is the most labor-intensive dye per unit color — roughly 4-5 kg of fresh woad leaves yield 1 gram of indigo pigment. True indigo (*Indigofera*) is roughly 5-10x more productive per leaf weight than woad, making it the preferred species wherever climate allows.

## Safety

- **Alum (potassium aluminum sulfate)**: The most common mordant. Irritant to skin and eyes at concentrated solutions (20%+ w/v). Inhalation of alum powder irritates respiratory tract. Handle with gloves when preparing solutions. Dissolve in hot water in a ventilated area.
- **Copper sulfate**: Toxic by ingestion (vomiting at 100 mg dose, lethal at 10-20 g). Blue crystals resemble candy — store in labeled containers away from food. Causes liver and kidney damage with chronic exposure. Handle with gloves; never pour copper-laden dye bath into waterways — toxic to aquatic life at <1 mg/L.
- **Iron sulfate**: Moderately toxic. Causes gastrointestinal distress at 1-5 g doses. Overuse on fiber degrades protein fibers (wool, silk) — iron acts as a catalyst for oxidative fiber damage, causing blackened, brittle fabric over years. Limit to 5-10% WOF on protein fibers.
- **Indigo vat (alkaline reducing solution)**: Traditional urine vats reach pH 9-10 (skin irritant). Chemical reduction vats using sodium hydrosulfite release sulfur dioxide gas — use in ventilated area. Alkaline solutions cause chemical burns on prolonged skin contact.
- **Wood ash lye (potassium carbonate)**: pH 11-12. Causes severe chemical burns to skin and eyes. Always add lye to water (never water to lye — causes splashing). Wear eye protection when preparing lye solutions.
- **General dye plant hazards**: Some dye plants (dyer's broom, broom) contain quinolizidine alkaloids — toxic if ingested in large quantities. Handle dye plants as you would any mildly toxic plant: wash hands after handling, keep away from food preparation areas.

## See Also

- [Textiles: Dyeing](../textiles/dyeing.md) — downstream application of natural dyes to fiber and cloth
- [Fiber Plants](./fiber-plants.md) — companion capability for fiber production
- [Chemistry](../chemistry/index.md) — alum, copper sulfate, and other mordant production
- [Plants & Botanical Resources](./index.md) — species catalog and botanical knowledge


[← Back to Plants](index.md)
