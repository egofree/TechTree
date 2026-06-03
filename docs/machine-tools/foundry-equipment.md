# Foundry Equipment

> **Node ID**: machine-tools.foundry-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.casting`](casting.md), [`ceramics`](../ceramics/index.md)
> **Enables**: [`machine-tools.iterative-bootstrap`](iterative-bootstrap.md), [`machine-tools.casting`](casting.md)
> **Timeline**: Years 5-15
> **Outputs**: crucibles, flasks, ladles, furnace_components
> **Critical**: Yes — foundry equipment is the prerequisite for all casting; without crucibles, furnaces, and molds, no complex metal parts can be produced

## Principle

Foundry equipment melts metal, contains molten metal, and shapes it into castings. The three essential subsystems are: (1) the furnace and crucible that heat metal above its melting point, (2) the flask and mold that define the casting shape, and (3) the ladle and pouring equipment that transfer molten metal safely from furnace to mold. Each subsystem must withstand repeated thermal cycling between ambient temperature and 700-1500°C without cracking, deforming, or contaminating the melt.

This article covers the construction of the primary foundry equipment. For casting procedures (sand preparation, pattern making, mold making, pouring technique), see [Casting](casting.md).

## Materials

### Crucible Furnace (Aluminum, Bronze)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel shell | 1 | 5 mm plate, 400 mm diameter × 500 mm tall, open top | [Iron & Steel](../metals/iron-steel.md) | Repurposed steel drum (thinner wall) |
| Refractory lining | 20-40 kg | Fireclay + grog (crushed refractory), 50 mm wall thickness | [Ceramics](../ceramics/index.md) | Commercial castable refractory (if available) |
| Clay-graphite crucible | 1 | 5-15 kg capacity, rated to 1400°C | [Ceramics](../ceramics/index.md) | Steel pipe with welded bottom (aluminum only, short life) |
| Charcoal | 50-100 kg | Lump charcoal, for fuel | [Energy](../energy/charcoal.md) | Coke (hotter, but requires coking coal) |
| Blower | 1 | Electric blower or hand-cranked fan, 100-300 L/min | [Energy](../energy/index.md) | Bellows (lower airflow, intermittent) |
| Steel pipe (tuyere) | 1 | 25-40 mm diameter, 200 mm long | [Iron & Steel](../metals/iron-steel.md) | Clay pipe (fragile) |

### Cupola Furnace (Cast Iron)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel shell | 1 | 5-10 mm plate, 40-60 cm bore × 2-4 m tall | [Iron & Steel](../metals/iron-steel.md) | — |
| Fireclay refractory brick | 100-200 | Standard 230 × 115 × 65 mm, rated to 1600°C | [Ceramics](../ceramics/index.md) | Rammed fireclay lining (less durable) |
| Tuyeres (air nozzles) | 2-4 | Steel pipe, 25-40 mm diameter | [Iron & Steel](../metals/iron-steel.md) | — |
| Blower | 1 | Forced air at 5-15 kPa, 5-20 m³/min | [Energy](../energy/index.md) | Multiple bellows in parallel (marginal) |
| Tap hole plug | Several | Clay or refractory material | [Ceramics](../ceramics/index.md) | — |

### Flasks (Mold Containers)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Pine or hardwood boards | 0.1 m³ | 25 mm thick, for flask sides | [Foundations](../foundations/tools-basic.md) | Steel plate (heavier, more durable) |
| Steel flat bar (reinforcement) | 10-20 kg | 25 × 3 mm, for flask edges and handles | [Iron & Steel](../metals/iron-steel.md) | — |
| Locating pins | 8-16 | 8 mm steel rod, 30 mm long | [Iron & Steel](../metals/iron-steel.md) | Wooden dowels (wear quickly) |
| Nails or screws | 100+ | 50 mm, for assembly | [Iron & Steel](../metals/iron-steel.md) | — |

### Ladles and Pouring Equipment

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel pipe (ladle body) | 1 | 100-150 mm diameter × 150 mm deep, welded bottom | [Iron & Steel](../metals/iron-steel.md) | Clay crucible used as ladle (fragile) |
| Steel rod (handle) | 1 | 20 mm diameter × 1.5 m long | [Iron & Steel](../metals/iron-steel.md) | — |
| Refractory wash | 2-5 kg | Fireclay slurry, for coating ladle interior | [Ceramics](../ceramics/index.md) | — |

## Prerequisites

- [Fireclay and refractory materials](../ceramics/index.md) — for furnace lining, crucibles, and ladle coatings
- [Charcoal or coke production](../energy/charcoal.md) — for furnace fuel
- [Iron and steel](../metals/iron-steel.md) — for furnace shells, flasks, and ladles
- [Bellows or blower](../energy/index.md) — for forced air to reach melting temperatures
- [Basic carpentry](../foundations/tools-basic.md) — for wooden flask construction

## Construction Steps

### Crucible Furnace (Charcoal-Fired, for Aluminum and Bronze)

1. **Form the steel shell**: Roll 5 mm steel plate into a cylinder 400 mm diameter × 500 mm tall. Weld the longitudinal seam with full penetration. Cut a 200 mm diameter hole in the bottom center for ash removal (with a removable cover plate). Cut a 30 mm diameter hole near the bottom side for the tuyere (air inlet). Weld steel angle-iron legs to the shell for support, raising the furnace 200 mm off the ground for ash access.
2. **Line the furnace with refractory**: Mix fireclay with 30% grog (crushed fired ceramic) and water to a stiff consistency. Apply 50 mm thick to the inner wall and bottom of the shell. Form a depression in the bottom to cradle the crucible. The inside diameter after lining should be 250-300 mm, leaving a 25-50 mm gap between the crucible and the wall for the fuel bed.
3. **Install the tuyere**: Insert a 30 mm steel pipe through the side hole, angled slightly downward (5-10°) toward the furnace center. The tuyere tip should be at the level of the crucible bottom, directing blast air into the fuel bed beneath and around the crucible. Seal the pipe-to-shell joint with refractory.
4. **Dry and fire the lining**: Air dry the refractory for 24-48 hours. Then build a small wood fire inside to drive off remaining moisture slowly (fast drying cracks the refractory). Over 4-6 hours, increase the fire intensity until the lining is thoroughly heated. Let cool. Inspect for cracks — hairline cracks are normal and seal with a thin fireclay wash on the next heat.
5. **Make or obtain a crucible**: Fire a clay-graphite crucible (mix 40% clay, 40% graphite, 20% grog; form over a mandrel; dry slowly; fire to 1200°C). Alternatively, for aluminum only (max 800°C), use a steel pipe with a welded bottom plate — it will oxidize but lasts 20-50 heats.
6. **Connect the blower**: Attach a steel pipe or flexible hose from the blower outlet to the tuyere. Install a simple damper (sliding plate) in the air line to control blast intensity. Full blast for maximum temperature; reduced blast for holding at temperature.

### Cupola Furnace (for Cast Iron)

7. **Form the shell**: Roll 5-10 mm steel plate into a cylinder, 40-60 cm internal diameter × 2-4 m tall. Weld the longitudinal seam. Weld a flat steel bottom plate with a 40 mm tap hole at the lowest point. Add a slag notch (slightly higher than the tap hole) on the opposite side.
8. **Line with refractory brick**: Line the interior with fireclay refractory brick set in fireclay mortar. Brick thickness: 65-115 mm. The lined bore should be 30-50 cm. At the tuyere level (20-30 cm above the bottom), leave openings in the brick matching the tuyere pipes.
9. **Install the tuyeres and wind box**: Weld 2-4 tuyere pipes (25-40 mm diameter steel pipe) through the shell into the refractory at evenly spaced positions around the circumference. On the outside, weld a sheet-metal wind box enclosing all tuyere inlets. Connect the blower to the wind box with a large-diameter hose or pipe.
10. **Add the charging door**: Cut a 200 × 300 mm opening in the shell at approximately 2/3 height. Fabricate a hinged steel door with a refractory lining. This is where coke, iron, and limestone are charged in alternating layers.
11. **Add the tap hole and slag notch**: The tap hole (40 mm diameter at the very bottom) is plugged with clay during operation and opened with a steel rod when iron is ready to tap. The slag notch (slightly above the tap hole) allows slag to overflow separately — slag floats on molten iron due to its lower density.

### Flasks (Cope and Drag Pairs)

12. **Cut the flask sides**: For a medium flask (400 × 400 × 150 mm per half), cut four pieces of 25 mm pine board: two at 400 mm long and two at 450 mm long (allowing for overlap at corners).
13. **Assemble the flask halves**: Nail or screw the boards into an open-top, open-bottom box. Reinforce the corners with steel flat bar (25 × 3 mm) screwed to the outside. The drag (bottom) and cope (top) are identical boxes.
14. **Install locating pins**: Drill two 8 mm holes through the cope sides at diagonally opposite corners. Install 8 mm steel pins that protrude 15 mm below the cope bottom edge. Drill matching holes in the drag top edge. The pins ensure the cope aligns precisely with the drag when the mold is closed — misalignment produces shifted castings.
15. **Add handles and cross-bars**: Screw steel flat bar handles to the outside of each flask half for lifting. Install a cross-bar inside the cope (across the top) to support the sand when the cope is filled and flipped.
16. **Seal the wood**: Paint or varnish the flask interior to prevent the wood from absorbing moisture from the green sand, which causes warping and delamination. Shellac or linseed oil works. Make 5-10 pairs of various sizes (200 × 200 to 600 × 600 mm).

### Ladles

17. **Make the ladle body**: Cut a 150 mm diameter disc from 3 mm steel plate. Form into a shallow bowl (150 mm deep) by hammering over a hollow form or by spinning on a lathe. Alternatively, weld a 100-150 mm diameter steel pipe section (150 mm tall) to a flat bottom plate. Weld a pouring spout into the rim.
18. **Attach the handle**: Weld a 20 mm diameter steel rod (1.5 m long) to the ladle body at a 90° angle. The long handle keeps the operator's hands away from the molten metal. Add a cross-grip at the handle end for two-handed pouring control.
19. **Coat with refractory wash**: Coat the ladle interior with a thin layer of fireclay slurry (fireclay + water to cream consistency). Dry slowly, then preheat before first use. The refractory coating prevents the molten metal from dissolving the steel ladle and provides a clean, smooth surface for pouring. Re-coat every 5-10 pours.

## Calibration and Verification

1. **Furnace temperature test**: Fill the crucible with aluminum scrap. Light the furnace, turn on the blower. The aluminum should melt within 20-40 minutes. If it takes longer, the blast is insufficient — check tuyere clearance and blower output. Target: 750-800°C for aluminum pouring.
2. **Crucible integrity**: Inspect the crucible before each use. Look for cracks, spalling, or glaze deterioration. A cracked crucible can fail during a pour, dumping 5-15 kg of molten metal — a life-threatening emergency. Tap the crucible with a wooden stick: a clear ring indicates soundness; a dull thud indicates cracking and the crucible must be retired.
3. **Flask alignment**: Close the flask halves with no sand inside. Check that the locating pins seat smoothly and the mating surfaces meet flush with no gap. A gap >0.5 mm between cope and drag allows metal to flash out during pouring.
4. **Ladle preheat**: Before each pour, preheat the ladle to 200-300°C. A cold ladle causes premature freezing of the first metal to enter, which can block the spout. Preheat by holding over the furnace exhaust or by filling with a small amount of molten metal and discarding it.

## Expected Performance

### Crucible Furnace

| Parameter | Value |
|-----------|-------|
| Maximum temperature | 1200-1400°C (charcoal + forced air) |
| Aluminum capacity | 5-15 kg per heat |
| Bronze/copper capacity | 5-10 kg per heat |
| Melting time (5 kg aluminum) | 20-40 minutes |
| Fuel consumption | 2-4 kg charcoal per kg aluminum |
| Crucible life (clay-graphite) | 50-200 heats |
| Crucible life (steel, aluminum only) | 20-50 heats |

### Cupola Furnace

| Parameter | Value |
|-----------|-------|
| Maximum temperature | 1350-1500°C |
| Cast iron melting rate | 500-1500 kg/hour (40 cm bore) |
| Coke consumption | 1 part coke to 8-10 parts iron by weight |
| Campaign duration | 4-12 hours continuous |
| Refractory lining life | 10-30 campaigns (before re-lining) |

### Flasks

| Parameter | Value |
|-----------|-------|
| Flask sizes (typical set) | 200 × 200, 300 × 300, 400 × 400, 600 × 600 mm |
| Flask depth per half | 100-300 mm |
| Locating pin accuracy | ±0.5 mm alignment between cope and drag |
| Wooden flask life | 200-500 pours (with sealant maintenance) |
| Steel flask life | Thousands of pours |

## Strengths

- Crucible furnace: simple to build, reaches aluminum and bronze melting temperatures with charcoal
- Cupola furnace: continuous melting, high throughput for cast iron — the workhorse of iron foundries
- Wooden flasks: fast to build, easily replaced, adequate for small-to-medium production
- Complete foundry setup achievable at the earliest stages of metallurgy

## Weaknesses

- Crucible furnace: limited to batch melting (5-15 kg per heat), not suitable for cast iron without a larger furnace
- Cupola furnace: requires significant forced air and coke supply, heavy and permanent installation
- Clay-graphite crucibles: fragile, susceptible to thermal shock, limited life span
- Wooden flasks: absorb moisture, warp, and burn if splashed with molten metal

## Safety

- **Molten metal burns**: Aluminum at 700°C and cast iron at 1400°C cause instant deep burns. Full PPE: face shield, leather apron, leather gloves (gauntlet), foundry boots (steel toe, no synthetic materials). Never pour over wet ground — moisture causes steam explosions.
- **Zinc fume (brass/bronze)**: Zinc boils at 907°C and generates zinc oxide fume causing "metal fume fever." Ventilate when melting brass. Work outdoors or with forced extraction.
- **Carbon monoxide**: Charcoal and coke furnaces produce CO. Work outdoors or with cross-ventilation. Never operate in an enclosed space.
- **Crucible failure**: A cracked crucible can disintegrate during a pour. Inspect every crucible before each use. Have a dry sand pit adjacent to the furnace for emergency disposal of a failed crucible.

## See Also

- [Casting](casting.md) — sand casting procedures, mold making, pattern design, and gating systems
- [Iron & Steel](../metals/iron-steel.md) — metal stock for casting and furnace construction
- [Ceramics](../ceramics/index.md) — refractory materials, crucibles, and fireclay
- [Charcoal Production](../energy/charcoal.md) — fuel for crucible and cupola furnaces
- [Iterative Bootstrap](iterative-bootstrap.md) — how castings become machine tools

[← Back to Machine Tools](index.md)
