# Dye Plants

> **Node ID**: plants.dye-plants
> **Domain**: [Plants & Botanical Resources](./)
> **Timeline**: Years 5-10
> **Outputs**: natural_dyes, plant_pigments

### Overview

Plants that yield natural colorants for dyeing textiles, leather, wood, ink, and coatings. Natural dyes have been the primary source of color for human material culture from prehistory through the 19th century, when synthetic aniline dyes superseded them. In a bootstrap context, dye plants provide the only practical path to colored textiles before the organic chemistry infrastructure needed for synthetic dyes exists. Color serves not only aesthetics but signaling (military uniforms, trade goods, social markers) and functional purposes (UV protection, mildew resistance from tannin-rich dyes).

This capability covers the cultivation, harvesting, and primary extraction of dye substances from plant material. The downstream application of dyes to fiber and cloth is covered in [Dyeing](../textiles/dyeing.md).

### Dye Extraction Methods

The three principal methods for extracting color from plant material, listed in order of increasing complexity:

1. **Hot water extraction (decoction)**: Chop or crush fresh or dried plant material, simmer in water at 60-90°C for 30-60 minutes. Strain through cloth. This is the simplest and most widely applicable method, effective for most dye plants including madder, weld, walnut hulls, and onion skins. The dye bath can be reused until exhausted — typically 2-3 dips per batch of material.

2. **Fermentation extraction**: Used primarily for indigo precursors from woad and indigo plants. Crush fresh leaves, pack into a vat with warm (40-50°C) alkaline water (traditionally wood ash lye or stale urine provides the alkali). Ferment for 12-48 hours, stirring occasionally. The indican in the leaves hydrolyzes to indoxyl, which oxidizes to insoluble blue indigo pigment when the liquor is beaten with air. The pigment settles as sludge, is collected, pressed, and dried into indigo cakes.

3. **Solvent extraction**: For concentrated dyes or when water extraction is inefficient. Uses alcohol (ethanol from fermentation) or alkaline solutions to pull pigments from tough plant material like bark, roots, and heartwood. Requires a closed vessel to prevent solvent evaporation. Yields more concentrated dye stuff suitable for trade or storage.

### Mordanting and Color Fixation

Most natural dyes are not substantive — they do not bond directly to fiber and require a mordant to achieve wash-fastness. The choice of mordant dramatically shifts the final color from a given dye plant. Common mordants available in a bootstrap context:

- **Alum (potassium aluminum sulfate)**: The universal mordant. Sourced from alunite stone (KAl(SO₄)₂(OH)₆) by roasting and leaching, or from natural alum deposits near volcanic soils. Brightens and clarifies most dye colors.
- **Iron (ferrous sulfate)**: Darkens and "saddens" colors — yellows become olive greens, blues become grays, pinks become purples. Made by dissolving iron scraps in vinegar. Overuse weakens protein fibers.
- **Tannin**: Oak galls, sumac leaves, pomegranate rinds, and chestnut bark provide tannins. Essential as a pre-mordant for cellulose fibers (linen, cotton) to help alum bond. Also useful as a standalone brown dye.
- **Copper (copper sulfate)**: Shifts yellows toward green and brightens greens. Made by dissolving copper in acid. Toxic — handle with care.

See [Dyeing](../textiles/dyeing.md) for detailed mordant preparation procedures and fiber-specific protocols.

### Color Range by Plant Source

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

### Common Dye Plants

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

### Cultivation Considerations

Dye plant cultivation integrates into existing agricultural patterns without requiring specialized equipment:

- **Annuals** (weld, coreopsis, safflower, Japanese indigo): Sow from seed each year. Can rotate with food crops.
- **Biennials** (woad, weld in cold climates): Establish in year one, harvest dye material in year two. Allow some plants to set seed for continuation.
- **Perennials** (madder, dyer's broom, shrubs): Plant once, harvest for years. Madder roots need 2-3 years before first harvest. Dedicate permanent beds.
- **Trees** (walnut, pomegranate, brazilwood): Long-term investment. Walnut trees produce nuts and dye hulls simultaneously — dual-purpose.

Most dye plants tolerate poor soils and require minimal inputs beyond weeding and moderate water. Weld and woad grow well on marginal land unsuitable for food crops.

### Harvesting and Processing

Timing affects dye yield significantly:

- **Leaves** (indigo, woad): Harvest before flowering when indican/glucosinolate levels peak. Multiple harvests per season possible.
- **Roots** (madder, bedstraw): Dig in autumn after 2-3 years of growth when pigment concentration is highest. Wash, dry, and store whole; chop just before use.
- **Flowers** (weld, coreopsis, chamomile): Pick at full bloom. Dry in shade to preserve color.
- **Hulls and bark** (walnut, oak): Collect green walnut hulls at nut harvest. Bark from pruned branches — never strip bark from live trees in rings.

Fresh plant material gives stronger colors than dried, but dried material stores for years and enables trade. Dry all material in shade to prevent UV degradation of pigments.

### Yield and Economics

Approximate dry plant material needed per 100g of wool fiber (alum-mordanted):

- Madder root: 50-100g (deep red)
- Weld: 100-200g (clear yellow)
- Walnut hulls: 50-100g (rich brown)
- Woad/indigo leaves: 500-1000g fresh (1-2g indigo pigment extracted)
- Coreopsis flowers: 50-100g (orange)

Indigo is the most labor-intensive dye per unit color — roughly 4-5 kg of fresh woad leaves yield 1 gram of indigo pigment. True indigo (*Indigofera*) is roughly 5-10x more productive per leaf weight than woad, making it the preferred species wherever climate allows.

### Dependencies

- Requires: [Plants & Botanical Resources](./) (tool)
- Feeds into: [Dyeing](../textiles/dyeing.md) (material — natural_dyes, plant_pigments)
- Related: [Fiber Plants](./fiber-plants.md) (companion capability — fiber production)

---

*Part of the [Bootciv Tech Tree](../) • [Plants](./) • [All Domains](../)*
