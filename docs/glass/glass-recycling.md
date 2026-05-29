# Glass Recycling & Cullet Recovery

> **Node ID**: glass.glass-recycling
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`Basic Glass Production`](basic.md), [`Advanced Glass Production`](advanced.md), [`Mining`](../mining/index.md), [`Energy`](../energy/index.md)
> **Enables**: [`Glass`](./index.md), [`Construction`](../construction/index.md), [`Electronics`](../electronics/index.md)
> **Timeline**: Years 15-50+
> **Outputs**: glass_cullet, recycled_glass, mixed_cullet_feedstock
> **Critical**: No — reduces raw material consumption but does not unlock new capabilities


Glass recycling reclaims glass from end-of-life products (containers, windows, fiberglass, electronic scrap) and processes it into cullet — crushed glass fragments that serve as feedstock for new glass production. Adding cullet to the glass batch reduces raw material consumption (sand, soda ash, limestone) by a proportional amount and lowers melting energy by 2–3% for every 10% cullet in the batch.

Unlike metals, glass is not recycled into its original composition — it is remelted into new glass products, often at a lower specification. Clear container glass becomes new bottles; green and amber glass may become insulation fiberglass or construction aggregate. The key constraint is color separation: clear cullet contaminated with colored glass produces off-color product.

Glass recycling differs fundamentally from metal recycling in one critical way: glass does not degrade with remelting. Metal alloys accumulate tramp elements over multiple recycling cycles, but glass chemistry is stable — the same SiO₂·Na₂O·CaO molecules can be melted and re-formed indefinitely. This makes glass theoretically 100% recyclable, though practical color sorting and contamination limits restrict actual recovery rates.

The boundary with waste management is clear: this document covers converting waste glass into reusable cullet feedstock. See [Waste Management](../ehs/waste-management.md) for disposal of non-recyclable glass waste (contaminated with hazardous substances, mixed with non-glass materials).

## Prerequisites

- [Basic Glass Production](basic.md) — primary glass melting from raw materials
- [Advanced Glass Production](advanced.md) — borosilicate and fused silica production
- [Mining](../mining/index.md) — silica sand source (what recycling replaces)
- [Energy](../energy/engine.md) — furnace fuel supply

## Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Waste glass | Post-consumer containers, flat glass, fiberglass | Collection from demolition, manufacturing scrap, consumer waste |
| Water | 1–5 m³ per tonne of cullet (washing) | [Water Treatment](../chemistry/water-treatment.md) |
| Fuel (natural gas or oil) | 0.5–1.5 GJ per tonne of cullet processed | [Energy](../energy/engine.md) |

## Tools & Equipment

| Equipment | Purpose | Source |
|-----------|---------|--------|
| Crusher or impact mill | Size reduction of glass to cullet (10–50 mm) | [Machine Tools](../machine-tools/index.md) |
| Vibrating screen | Size classification of cullet | [Ore Processing](../mining/processing.md) |
| Magnetic separator | Remove ferrous contamination (caps, wire) | [Mining Processing](../mining/processing.md) |
| Eddy-current separator | Remove aluminum contamination (caps, foil) | [Mining Processing](../mining/processing.md) |
| Optical sorter | Color separation (clear, green, amber) | [Measurement](../measurement/index.md) |
| Glass furnace | Remelting cullet into new glass | [Basic Glass](basic.md) |

## Knowledge

- Visual identification of glass types: soda-lime (containers, windows), borosilicate (laboratory), lead glass (crystal, CRT)
- Understanding of ceramic and stone contamination (ceramic fragments in cullet cause defects in new glass — stones and ceramics don't melt at glass furnace temperatures)
- Furnace operation with variable cullet ratios


## BOM: Container Glass Cullet Processing (per tonne of input waste glass)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Waste glass (mixed containers) | 1,000 kg | Collection programs | Manufacturing cullet (cleaner, less processing) |
| Water (washing) | 1–3 m³ | [Water Treatment](../chemistry/water-treatment.md) | Air classification (dry process, lower quality) |
| Detergent (optional) | 0.1–0.5 kg | [Chemistry](../chemistry/index.md) | Hot water alone (less effective on organics) |
| Electricity (crushing + sorting) | 15–40 kWh | [Energy](../energy/engine.md) | Diesel generator |
| Natural gas (drying) | 0.1–0.3 GJ | [Energy](../energy/engine.md) | Waste heat from furnace exhaust |

## BOM: Cullet-to-Glass Furnace Charge (per tonne of new glass)

| Component | All-Primary | 50% Cullet | 90% Cullet | Notes |
|-----------|------------|-----------|-----------|-------|
| Silica sand | 720 kg | 360 kg | 72 kg | Reduced proportionally with cullet |
| Soda ash (Na₂CO₃) | 210 kg | 105 kg | 21 kg | Major cost saving with cullet |
| Limestone (CaCO₃) | 100 kg | 50 kg | 10 kg | Minor cost saving |
| Cullet | 0 kg | 500 kg | 900 kg | Replaces raw materials 1:1 by weight |
| Energy (melting) | 4.0–5.5 GJ | 3.2–4.5 GJ | 2.0–3.0 GJ | 2–3% reduction per 10% cullet |


## Container Glass Cullet Processing

1. **Collect and transport.** Gather waste glass from curbside collection, drop-off centers, or manufacturing scrap. Transport to processing facility. Glass is heavy and abrasive — use steel-bodied trucks and skip-cars.

2. **Pre-sort manually.** Remove obvious contaminants on a sorting belt: ceramics (plates, mugs), Pyrex/borosilicate (different melting point), metal objects, plastic bags, and light bulbs (contain lead or mercury). Train sorters to recognize problem items by visual inspection. Sort rate: 3–8 tonnes/hour per sorting position.

3. **Crush to cullet.** Feed sorted glass into an impact crusher or hammer mill. Target size: 10–50 mm (⅜ to 2 inch). Oversize returns to the crusher. Undersize (<5 mm, called "fines") is collected separately — fines have lower market value due to higher contamination risk.

4. **Remove ferrous metals.** Pass crushed cullet over a magnetic separator (belt magnet or drum magnet). Removes steel caps, wire, nails, and iron fragments. Residual ferrous contamination: <50 g/tonne after magnetic separation.

5. **Remove non-ferrous metals.** Pass cullet through an eddy-current separator to remove aluminum caps, foil, and copper wire. Eddy current induces a repulsive force on conductive metals, ejecting them from the cullet stream.

6. **Wash (if needed).** For food-contaminated containers, wash cullet in a rotary drum with warm water (40–60°C) and mild detergent. Rinse with clean water. Drain and dry. For clean cullet (manufacturing scrap), washing may not be required.

7. **Color sort.** Pass cullet through an optical sorter that identifies glass color (clear, green, amber) using visible-light sensors and air jets to deflect pieces into separate bins. Clear cullet is the most valuable — amber contamination of clear cullet must be <1% for premium bottle-to-bottle recycling.

8. **Size classify.** Screen cullet into size fractions: coarse (25–50 mm), medium (10–25 mm), and fines (<10 mm). Furnaces prefer uniform size for consistent melting. Fines may be used in fiberglass or construction applications.

## Flat Glass (Window) Recycling

1. **Remove frames and hardware.** Dismantle windows: separate aluminum or wood frames, rubber gaskets, and sealant from the glass pane. Wire brush to remove residual adhesive.

2. **Test for coatings.** Some architectural glass has low-E coatings (silver or tin oxide) or laminated interlayers (PVB plastic). Coated glass can be recycled but requires de-coating (acid wash or mechanical abrasion) for some applications. Laminated glass must have the PVB interlayer removed.

3. **Crush and process as cullet.** Follow steps 3–8 of container glass processing. Flat glass produces cleaner cullet than container glass (no food residue, fewer contaminants).

## Fiberglass and Specialty Glass Recovery

1. **Collect fiberglass waste.** Manufacturing offcuts, end-of-life fiberglass insulation, and fiberglass-reinforced plastic (FRP) scrap.

2. **Shred to liberate fibers.** Mechanical shredding reduces fiberglass to short fiber lengths (1–20 mm). Separate from binder resin by thermal treatment (400–500°C to burn off organic binder) or solvent dissolution.

3. **Reprocess.** Clean glass fibers can be remelted with virgin batch material. Fiber-to-fiber recycling is difficult — most fiberglass waste is downcycled into construction products (cement additive, road base).


## Cullet Quality Specifications

| Grade | Color Purity | Ceramic/Stone | Ferrous Metal | Organic | Application |
|-------|-------------|---------------|---------------|---------|-------------|
| Premium clear | >99.5% clear | <25 g/t | <5 g/t | <500 g/t | Clear container glass (bottle-to-bottle) |
| Premium green | >98% green | <50 g/t | <5 g/t | <500 g/t | Green container glass |
| Premium amber | >98% amber | <50 g/t | <5 g/t | <500 g/t | Amber container glass |
| Mixed color | Any mix | <100 g/t | <10 g/t | <1000 g/t | Fiberglass, colored glass |
| Construction grade | Any | <500 g/t | <50 g/t | <5000 g/t | Road base, aggregate, sand substitute |

## Energy and Raw Material Savings

| Cullet % in Furnace Charge | Energy Savings | Raw Material Savings | CO₂ Reduction | Furnace Temperature Effect |
|---------------------------|----------------|---------------------|---------------|---------------------------|
| 0% (all primary) | Baseline | Baseline | Baseline | Baseline |
| 25% | 5–8% | 25% | 10–15% | 10–20°C lower melt temp |
| 50% | 10–15% | 50% | 20–30% | 20–40°C lower |
| 75% | 15–22% | 75% | 30–45% | 30–60°C lower |
| 90%+ | 20–30% | 90% | 40–60% | 40–80°C lower |

Cullet reduces energy because it is already partially reacted — the silicate network formed during the original melting does not need to be re-formed from raw materials. Each 10% cullet reduces batch melting energy by approximately 2.5–3.0%.

## Processing Parameters

| Operation | Throughput | Energy | Key Control |
|-----------|-----------|--------|-------------|
| Crushing | 5–50 t/hour | 1–3 kWh/tonne | Gap setting controls max size |
| Magnetic separation | 5–50 t/hour | 0.5–1.5 kWh/tonne | Belt speed and magnet strength |
| Eddy current separation | 5–30 t/hour | 1–2 kWh/tonne | Rotor speed (2000–4000 RPM) |
| Optical color sorting | 3–15 t/hour | 2–5 kWh/tonne | Camera calibration, air jet pressure |
| Washing | 5–20 t/hour | 0.5–1.5 kWh/tonne | Water temperature, detergent dose |
| Screening | 10–100 t/hour | 0.3–1.0 kWh/tonne | Screen aperture sizes |

## Scaling Notes

**Minimum viable scale**: A settlement with a glass furnace can add 10–30% cullet to the batch with minimal processing — crush clean glass scrap by hand or with a simple crusher, pick out obvious contaminants, and add to the furnace charge. No color sorting needed if mixed-color cullet is acceptable (produces green-tinted glass).

**Small industrial scale** (5–50 tonnes/day): A dedicated cullet processing line with crusher, magnetic separator, and manual color sorting. Requires 2–5 workers. Output: mixed-color cullet suitable for colored container glass or fiberglass.

**Full industrial scale** (100–1,000+ tonnes/day): Automated processing with optical sorting, eddy-current separation, air classification, and washing. Capital cost: $2M–$15M. Output: color-sorted premium cullet for bottle-to-bottle recycling.

**Scale breakpoint**: Optical color sorting becomes economical above 20–30 tonnes/day throughput. Below this, manual sorting is cheaper. Above 100 tonnes/day, multi-spectral sorters (detecting ceramic and stone by NIR absorption) justify their $300K–$800K cost.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Stones (unmelted particles) in new glass | Ceramic contamination in cullet — ceramics don't melt at glass furnace temperature | Install ceramic detection (X-ray or NIR sorter); improve manual pre-sorting |
| Color variation in recycled glass bottles | Mixed color cullet contaminating clear batch | Tighten color sorting to <0.5% off-color; reduce cullet ratio in clear glass |
| Foaming in furnace when using high cullet | Organic contamination (food residue, labels) decomposing and releasing gas | Improve washing; add fines removal (organics concentrate in fines); preheat cullet to burn off organics |
| Refractory damage from cullet fines | Fine cullet (<5 mm) carries concentrated contaminants and erodes furnace refractories | Remove fines by screening; limit fines content to <10% of cullet |
| Low cullet recovery rate | Excessive breakage during collection/transport generates fines lost to dust | Use padded collection containers; minimize handling steps |
| Aluminum contamination causes seeds (bubbles) in glass | Aluminum metal reacts with silica at melt temperature, releasing gas | Improve eddy-current separation; test cullet for Al with spark test |
| Cullet producing off-color glass | Color contamination — mixed cullet in clear batch | Improve optical sorting; separate by color before crushing; use contaminated cullet for amber/green glass only |
| Seeds and bubbles in remelted glass | Organic contamination (labels, food residue) | Wash cullet before crushing; burn off organics at 500°C preheat; increase fining time in furnace |
| Furnace refractory damage from cullet | Ceramic or stone contamination in cullet feed | Install magnetic separation for ferrous; density separation for ceramics; manual pick line for large contaminants |
| Low cullet recovery rate | Breakage during collection or inadequate sorting | Use separate collection bins for glass; reduce handling steps; train collection crews |
| Ceramic stones in final product | Heat-resistant ceramic (pyroceram) mixed in cullet | UV fluorescence sorting (ceramic glows differently); X-ray transmission sorting for high-value cullet |
| Excessive fine particles (<0.5 mm) | Over-crushing or insufficient screening | Adjust crusher gap; add screening step; fines can be used in construction aggregate |

## Safety

**Laceration hazard**: Broken glass edges are the primary injury risk in cullet processing. Cut-resistant gloves (Level A4 minimum) mandatory for all manual sorting and handling. Safety glasses with side shields. Steel-toe boots. Long sleeves. Handling full glass containers before crushing is more hazardous than handling cullet.

**Dust inhalation**: Crushing glass generates fine silica dust (<10 μm). Prolonged inhalation causes silicosis. Local exhaust ventilation at crusher discharge and screening points with 0.5 m/s capture velocity. Respiratory protection: half-face respirator with P100 filter when dust is visible or during crusher maintenance.

**Glass furnace hazards**: Remelting cullet involves the same hazards as primary glass production — furnace temperature 1100–1500°C, risk of thermal burns from molten glass or furnace radiation, and potential for furnace failure. See [Basic Glass](basic.md) for furnace safety protocols.

**Heavy metal contamination**: Lead glass (crystal, CRT glass) contains 20–30% PbO. Lead oxide fume at furnace temperatures is toxic. Never mix lead glass with soda-lime cullet — it contaminates the entire batch and creates a lead exposure hazard. Separate and label all lead glass. PPE: respiratory protection if lead glass is processed.


## Cullet Quality Tests

| Test | Method | Frequency | Specification |
|------|--------|-----------|---------------|
| Ceramic/stone content | Visual inspection of 5 kg sample | Every truckload | <25 g/t (premium), <100 g/t (standard) |
| Ferrous metal | Magnet test on 5 kg sample | Every truckload | <5 g/t |
| Color purity | Visual + optical count | Every truckload | >99.5% single color (premium) |
| Organic content | Loss on ignition at 550°C | Weekly composite | <0.1% LOI |
| Particle size distribution | Sieve analysis (25 mm, 10 mm, 5 mm screens) | Daily | 90% passing 25 mm, <10% passing 5 mm |
| Moisture content | Oven dry at 105°C | Daily | <5% |

## Glass Product Quality from Recycled Cullet

| Parameter | Test Method | Acceptance |
|-----------|------------|------------|
| Seeds (bubbles) | Visual count per 100 cm² | <5 seeds/100 cm² |
| Stones (unmelted inclusions) | Visual inspection | 0 stones per article |
| Color (L*a*b*) | Spectrophotometer | Within ±2 ΔE of standard |
| Striae (cord) | Polarized light | Not visible at 1× magnification |

## Field Test (No Lab Required)

- **Ceramic vs. glass test**: Tap the piece with a metal object. Glass rings (high-pitched, sustained); ceramic thuds (dull, short). Alternatively, try to scratch with a steel nail — glass is harder than steel, ceramic may be scratched.
- **Lead glass test**: Lead glass is noticeably heavier than soda-lime glass (density 3.1 vs 2.5 g/cm³). A lead crystal wine glass weighs ~30% more than a soda-lime equivalent.


## Recycling Route Comparison

| Route | Input | Output | Yield | Energy Savings | Notes |
|-------|-------|--------|-------|----------------|-------|
| Bottle-to-bottle | Sorted container glass | New containers | 85–95% | 20–30% | Highest value — requires clean, color-sorted cullet |
| Container-to-fiberglass | Mixed container glass | Fiberglass insulation | 80–90% | 15–20% | Lower quality requirement; mixed colors acceptable |
| Flat glass recycling | Window glass | New flat glass or containers | 85–95% | 20–25% | Cleaner than containers; may have coatings |
| Fiberglass downcycling | Fiberglass waste | Construction aggregate | 70–85% | 5–10% | Lowest value; avoids landfill |
| Glass sand | Any glass | Construction sand substitute | 90–95% | N/A (not remelted) | No furnace needed; crushed to sand size |

## When Cullet Recycling Is Not Feasible

- **Mixed glass types** (soda-lime + borosilicate + lead): Different melting points and chemistry prevent co-melting. Separate or downcycle to construction aggregate.
- **Highly contaminated glass** (embedded in composite materials, painted, laminated): Cost of cleaning exceeds value of recovered glass.
- **Small volumes** (<1 tonne/day): Manual sorting and small-batch remelting may work, but energy savings are minimal.

## See Also

- [Basic Glass Production](basic.md) — primary glass melting from raw materials
- [Advanced Glass Production](advanced.md) — borosilicate and fused silica production
- [Mining](../mining/index.md) — source of silica sand (what recycling replaces)
- [Energy](../energy/engine.md) — furnace fuel supply
- [Metal Recycling](../metals/metal-recycling.md) — parallel recovery domain for metals
- [Ceramic Recycling](../ceramics/ceramic-recycling.md) — related recovery capability for ceramics
- [Waste Management](../ehs/waste-management.md) — disposal of non-recyclable glass waste
- [Ore Processing](../mining/processing.md) — crushing and separation equipment shared with cullet processing

[← Back to Glass](index.md)
