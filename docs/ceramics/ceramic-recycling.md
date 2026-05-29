# Ceramic & Refractory Recycling

> **Node ID**: ceramics.ceramic-recycling
> **Domain**: [Ceramics & Refractories](./index.md)
> **Dependencies**: [`Pottery & Clay Products`](pottery.md), [`Advanced Ceramics`](advanced-ceramics.md), [`Kiln Construction`](kilns.md), [`Mining`](../mining/index.md)
> **Enables**: [`Ceramics`](./index.md), [`Construction`](../construction/index.md), [`Refractories`](../chemistry/refractories.md)
> **Timeline**: Years 10-50+
> **Outputs**: recycled_ceramic_aggregate, grog, refractory_reclaim, ceramic_fillers
> **Critical**: No — reduces raw material consumption but does not unlock new capabilities

Ceramic recycling reclaims fired clay products, refractory bricks, and technical ceramics from end-of-life products and manufacturing waste for reuse as grog (pre-fired clay additive), aggregate, or reprocessed refractory feedstock. Unlike glass and metals, ceramics cannot be remelted and re-formed — once fired, the crystalline structure is permanent. Ceramic "recycling" is therefore a downcycling process: the material is crushed and reused as an aggregate or additive rather than returned to its original form.

The primary recovered material is **grog** — crushed, fired ceramic added to raw clay to reduce shrinkage, improve thermal shock resistance, and control drying behavior. Grog has been used since antiquity; potters have always crushed broken pots and added the fragments to new clay bodies. This is one of the oldest forms of material recycling.

Refractory recycling is economically significant because refractory bricks are consumed in large quantities by metallurgical furnaces, glass tanks, and cement kilns. A basic oxygen furnace relines every 1,000–3,000 heats, generating 100–500 tonnes of spent refractory. Recovering the still-serviceable portions for reuse or reprocessing reduces both raw material costs and landfill burden.

This capability is distinct from waste disposal. Ceramic waste that cannot be recycled (contaminated with heavy metals, radioactive material, or hazardous slag) is handled by [Waste Management](../ehs/waste-management.md).

## Prerequisites

## Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Waste ceramics | Broken pottery, spent refractories, manufacturing rejects | Collection from potters, demolition, furnace relining |
| Clay (if making new products with grog) | Plastic clay body for re-forming | [Pottery](pottery.md) |
| Energy (crushing) | 5–30 kWh per tonne of ceramic waste | [Energy](../energy/engine.md) |

## Tools & Equipment

| Equipment | Purpose | Source |
|-----------|---------|--------|
| Jaw crusher or hammer mill | Primary size reduction of ceramic waste | [Machine Tools](../machine-tools/index.md) |
| Ball mill (optional) | Fine grinding to specific grog size grades | [Mining Processing](../mining/processing.md) |
| Vibrating screens | Size classification of crushed grog | [Mining Processing](../mining/processing.md) |
| Magnetic separator | Remove iron contamination (steel fragments from refractory anchors) | [Mining Processing](../mining/processing.md) |
| Kiln | Firing new ceramic products containing recycled grog | [Kilns](kilns.md) |

## Knowledge

- Identification of ceramic types: earthenware, stoneware, porcelain, fireclay, high-alumina, silica, magnesite, silicon carbide
- Understanding of grog sizing effects on clay body properties (coarse grog: thermal shock resistance; fine grog: smooth surface)
- Refractory condition assessment: distinguishing chemically attacked zones (usable for less demanding applications) from structurally sound zones

## Bill of Materials

## BOM: Grog Production from Waste Pottery (per tonne of grog)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Waste ceramics (broken pots, rejects) | 1,050–1,100 kg | Potters, manufacturing waste | Spent refractories (different properties) |
| Electricity (crushing) | 10–30 kWh | [Energy](../energy/engine.md) | Manual crushing with sledgehammer (labor-intensive) |
| Water (dust suppression) | 50–200 L | [Water Treatment](../chemistry/water-treatment.md) | Dry process with dust collection |
| Screens (replacement wear) | 1–5 m²/year | [Metals](../metals/index.md) | Hand-sorting by size (slow, inconsistent) |

## BOM: Spent Refractory Processing (per tonne of spent refractory)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Spent refractories (mixed) | 1,000 kg | Furnace relining waste | N/A — feedstock |
| Steel (anchors, bands) | 10–50 kg recovered | Magnetic separation | Sell as scrap metal |
| Sorting labor | 1–4 person-hours/tonne | Manual sorting | Automated XRF sorting (high capital cost) |
| Crushing energy | 15–40 kWh/tonne | [Energy](../energy/engine.md) | Drop-weight crusher (lower throughput) |

## Process Description

## 4.1 Grog Production from Waste Pottery

1. **Collect and sort.** Gather broken pots, kiln wasters, and manufacturing rejects. Sort by ceramic type: earthenware (fired 800–1100°C, porous, red/buff), stoneware (fired 1200–1300°C, vitrified, gray/brown), and porcelain (fired 1250–1400°C, white, translucent). Do not mix types — different fired densities and absorption rates affect clay body behavior unpredictably.

2. **Remove glaze contamination.** Glazed sherds can be used as grog, but the glaze may contain lead or other toxic metals. For food-contact ware, use only unglazed waste or glazed waste with known non-toxic glaze composition. For structural ceramics (tiles, bricks), glazed grog is acceptable.

3. **Crush.** Feed sorted ceramic waste into a jaw crusher. Set gap to 20–40 mm for primary crush. A hammer mill produces a more uniform product at smaller sizes (5–20 mm). For fine grog (<2 mm), use a ball mill with ceramic grinding media.

4. **Screen into size grades.** Pass crushed material through a series of vibrating screens:
   - Coarse grog: 5–10 mm — structural brick, large sculptural work
   - Medium grog: 2–5 mm — general-purpose pottery, garden pots
   - Fine grog: 0.5–2 mm — tableware, tiles, smooth surfaces
   - Dust (<0.5 mm): discard or use as filler in cement

5. **Store dry.** Keep grog in dry storage. Grog does not absorb water readily (it is already fired), but moisture between particles can cause weighing inaccuracies and clay body inconsistencies.

## 4.2 Spent Refractory Recovery

1. **Assess and sort during furnace relining.** As spent refractories are removed from the furnace, sort into categories by visual inspection:
   - **Hot face** (directly exposed to molten metal/slag): heavily infiltrated with slag, often not recyclable for refractory use. Downcycle to aggregate.
   - **Intermediate zone**: moderately infiltrated, may be reusable in less demanding applications (backup lining, insulation).
   - **Cold face** (outer layer): relatively uncontaminated, often reusable directly as refractory brick for non-critical applications.

2. **Remove metallic inclusions.** Pass through a magnetic separator to remove steel anchors, banding, and iron-rich slag. Remove non-magnetic metals (aluminum, copper) by hand sorting or eddy-current separation.

3. **Crush and screen.** Crush serviceable refractory to target size (10–50 mm for re-use as aggregate, <5 mm for reprocessing into new refractory). Screen into grades.

4. **Reprocess into new refractory (optional).** Mix crushed spent refractory with fresh raw materials (clay, alumina, silica) at 20–40% recycled content. Press and fire as new bricks. Recycled content above 40% typically compromises refractory properties.

5. **Downcycle non-recoverable material.** Heavily contaminated refractory that cannot be returned to refractory use can be:
   - Crushed to aggregate for road base or concrete (must pass leach testing for heavy metals)
   - Used as landfill cover material
   - Processed for metal recovery (some spent refractories contain significant chromium, magnesite, or alumina values)

## 4.3 Technical Ceramic Recovery

1. **Identify material.** Technical ceramics (alumina, zirconia, silicon carbide) have high material value. Separate by type using visual inspection (color, fracture surface), hardness testing, and density measurement.

2. **Crush to powder.** Ball mill technical ceramic waste to <100 μm powder. The powder can be reused as sintering additive, filler, or abrasive grit.

3. **Reprocess or downcycle.** Alumina powder recovered from grinding wheels and electronic substrates can be re-sintered into lower-grade alumina components. Silicon carbide powder is reusable as an abrasive. Zirconia recovery is economically marginal due to phase transformation during reprocessing.

## Quantitative Parameters

## Grog Properties by Size Grade

| Size Grade | Particle Size | Bulk Density | Water Absorption | Primary Use |
|------------|--------------|-------------|-----------------|-------------|
| Coarse | 5–10 mm | 1.0–1.4 g/cm³ | <5% (already fired) | Structural brick, sculpture |
| Medium | 2–5 mm | 1.1–1.5 g/cm³ | <5% | General pottery, garden pots |
| Fine | 0.5–2 mm | 1.2–1.6 g/cm³ | <5% | Tableware, tiles |
| Dust | <0.5 mm | 1.3–1.7 g/cm³ | <5% | Cement filler, soil amendment |

## Grog Content Effects on Clay Body

| Grog Content | Drying Shrinkage | Firing Shrinkage | Thermal Shock Resistance | Workability |
|-------------|-----------------|-----------------|--------------------------|-------------|
| 0% (no grog) | 6–10% | 5–12% | Poor | Excellent |
| 10% | 5–8% | 4–10% | Fair | Good |
| 20% | 4–6% | 3–8% | Good | Moderate |
| 30% | 3–5% | 2–6% | Very good | Reduced |
| 50% | 2–3% | 1–4% | Excellent | Difficult |

## Refractory Recovery Parameters

| Refractory Type | Service Life | Recoverable Fraction | Recycled Content in New Brick | Energy Savings vs. Primary |
|----------------|-------------|---------------------|------------------------------|---------------------------|
| Fireclay (Al₂O₃ 30–45%) | 6–24 months | 40–60% | 20–40% | 15–25% |
| High-alumina (Al₂O₃ 60–90%) | 12–48 months | 30–50% | 15–30% | 20–35% |
| Silica (SiO₂ >93%) | 12–36 months | 20–40% | 10–25% | 10–20% |
| Magnesite (MgO >85%) | 6–24 months | 30–50% | 15–30% | 20–30% |
| Silicon carbide (SiC) | 24–60 months | 40–60% | 20–40% | 25–40% |

## Energy Comparison: Grog Production vs. Primary Clay Processing

| Operation | Grog from Waste (kWh/tonne) | Primary Clay Processing (kWh/tonne) | Savings |
|-----------|-----------------------------|--------------------------------------|---------|
| Extraction | 0 (already available) | 5–15 (quarrying) | 100% |
| Crushing | 10–30 | 15–40 | 30–50% |
| Grinding | 5–20 (optional) | 20–60 | 50–70% |
| Firing | 0 (already fired) | 400–1,200 (kiln at 1000–1400°C) | 100% |
| Total | 15–50 | 440–1,315 | 90–96% |

## Scaling Notes

**Minimum viable scale**: A single potter crushing broken pots with a hammer and adding the fragments to new clay. Zero capital investment. This has been standard practice for thousands of years and remains the bootstrap entry point.

**Small industrial scale** (1–10 tonnes/day of grog): A jaw crusher (5–20 kW), vibrating screen, and covered storage area. One operator. Appropriate for a pottery community or brick works generating consistent waste.

**Industrial scale** (50–500 tonnes/day): Refractory recycling plants at steel mills process relining waste continuously. Automated sorting (XRF for composition), multi-stage crushing, magnetic separation, and quality testing. Capital cost: $1M–$10M.

**Key constraint**: Ceramic recycling is limited by the downcycling nature of the process. Each cycle reduces the material to a less demanding application. After 2–3 cycles, the material ends up as construction aggregate. This is not a closed loop — it is a cascade.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Grog causes spalling in fired ware | Grog too coarse for the application, or thermal expansion mismatch between grog and clay body | Reduce grog particle size; match grog material to clay body (stoneware grog for stoneware clay) |
| Recycled refractory bricks crack in service | Hidden slag infiltration weakens structural integrity; recycled content too high | Limit recycled content to 30% for critical applications; visually inspect and discard slag-infiltrated pieces |
| Mixed ceramic types produce inconsistent grog | Earthenware and stoneware grog mixed — different densities and absorption | Sort by type before crushing; test unknowns by water absorption (earthenware >5%, stoneware <2%) |
| Dust generation during crushing exceeds safe levels | Insufficient water spray; crusher not enclosed | Install water mist spray at crusher feed and discharge; enclose crusher with dust extraction |
| Low recovery rate from spent refractories | Over-sorting — too much material classified as contaminated | Train sorters to distinguish surface contamination (removable) from deep infiltration (not reusable) |
| Glazed grog causes pinholing in new ware | Glaze vaporizes during firing, releasing gas into the clay body | Use only unglazed waste for food-contact ware; fire glazed grog separately to burn off glaze first |

## Safety

**Silica dust**: Ceramic crushing generates respirable crystalline silica (RCS). Silica dust exposure at >0.025 mg/m³ (8-hour TWA) causes silicosis after years of exposure. This is the primary occupational hazard in ceramic recycling. Control: local exhaust ventilation at crusher discharge, water mist suppression, enclosed processing areas. PPE: half-face respirator with P100 filter when visible dust is present. Health monitoring: chest X-ray every 3–5 years for workers with regular dust exposure.

**Heavy impacts**: Jaw crushers and hammer mills have powerful moving parts. Never reach into a crusher to clear a jam — use a pry bar from outside the guard. Lock-out/tag-out before maintenance. Hearing protection required near operating crushers (90–105 dB).

**Refractory slag handling**: Spent refractories from metallurgical furnaces may contain entrained heavy metals (Cr, Ni, V from steelmaking slag). Handle with gloves. Test for leachable metals before using as construction aggregate. If chromium (VI) is suspected (green staining on magnesite refractories), treat as hazardous waste — see [Waste Management](../ehs/waste-management.md).

**Thermal stress**: Refractory bricks removed from furnaces may retain heat for 24–48 hours. Use thermal gloves (rated to 500°C) during relining operations. Infrared thermometer check before handling.

## Quality Control

## Grog Quality Tests

| Test | Method | Specification |
|------|--------|--------------|
| Particle size distribution | Sieve analysis (10 mm, 5 mm, 2 mm, 0.5 mm) | Per size grade specification (see §5) |
| Firing temperature indication | Color and fracture surface | Stoneware: gray-brown, conchoidal fracture. Earthenware: red/buff, granular fracture |
| Iron contamination | Magnetic test on sample | <0.1% by weight magnetic material |
| Water absorption of grog particles | Boil test (immerse 24h, measure weight gain) | <5% for stoneware grog, 5–15% for earthenware grog |
| Bulk density | Weigh known volume | Per size grade (see §5) |

## Recycled Refractory Quality Tests

| Test | Method | Acceptance |
|------|--------|------------|
| Chemical composition | XRF or ICP-OES | Al₂O₃, SiO₂, MgO within ±5% of target grade |
| Apparent porosity | Water absorption under vacuum | <20% for structural refractory use |
| Cold crushing strength | Hydraulic press test | >15 MPa for backup lining |
| Slag infiltration depth | Cross-section, visual or microscopy | <25% of brick thickness for reuse |

## Field Test (No Lab Required)

- **Earthenware vs. stoneware**: Lick the ceramic surface. Earthenware feels sticky/tongue-adheres (porous). Stoneware feels smooth/non-adherent (vitrified). This is the traditional potter's test.
- **Refractory grade estimate**: Scratch with a steel nail. Fireclay is easily scratched; high-alumina resists scratching; silicon carbide cannot be scratched by steel.

## Variations and Alternatives

## Ceramic Recycling Routes Compared

| Route | Input | Output | Value Added | Notes |
|-------|-------|--------|-------------|-------|
| Grog for pottery | Broken pots, wasters | Sized grog additive | Medium — improves clay body properties | Oldest form of ceramic recycling |
| Refractory reuse (direct) | Spent refractory bricks | Re-sorted bricks for backup lining | High — no reprocessing needed | Limited to cold-face and intermediate zones |
| Refractory reprocessing | Crushed spent refractory | New refractory bricks (20–40% recycled) | High — returns to original use | Requires blending with fresh raw materials |
| Construction aggregate | Any ceramic waste | Road base, concrete filler | Low — downcycling | Last resort before landfill |
| Abrasive grit | Technical ceramics (Al₂O₃, SiC) | Grinding and polishing media | Medium — value in hardness | Ball mill to specific grit sizes |
| Soil amendment | Low-fired earthenware | Horticultural aggregate (improves drainage) | Low | Must be free of toxic glazes |

## When NOT to Recycle Ceramics

- Refractories contaminated with chromium (VI) — hazardous waste (green staining)
- Lead-glazed ceramics for food-contact applications
- Radioactive ceramics (luminescent dials, some vintage tiles)
- Ceramic fiber insulation (respirable fiber hazard — handle as hazardous material per waste management protocols)

## See Also

- [Pottery & Clay Products](pottery.md) — clay body formulation and firing processes that use grog
- [Advanced Ceramics](advanced-ceramics.md) — technical ceramic properties and reprocessing
- [Kiln Construction](kilns.md) — kiln lining materials (refractories) that generate recyclable waste
- [Kiln Firing](kiln-firing.md) — firing processes that generate wasters and kiln furniture waste
- [Refractory Materials](../chemistry/refractories.md) — refractory production from primary raw materials
- [Mining](../mining/index.md) — source of clay and minerals (what recycling replaces)
- [Metal Recycling](../metals/metal-recycling.md) — parallel recovery domain for metals
- [Glass Recycling](../glass/glass-recycling.md) — parallel recovery domain for glass
- [Waste Management](../ehs/waste-management.md) — disposal of non-recyclable ceramic waste

[← Back to Ceramics & Refractories](index.md)
