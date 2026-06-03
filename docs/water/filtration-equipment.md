# Filtration Equipment

> **Node ID**: water.filtration-equipment
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`ceramics.pottery`](../ceramics/index.md), [`chemistry.cement`](../chemistry/cement.md)
> **Enables**: [`water.basic-treatment`](basic-treatment.md), [`water.sem-tech-water-treatment`](sem-tech-water-treatment.md), [`water.desalination`](desalination.md)
> **Timeline**: Years 5-25
> **Outputs**: filtered_water, strained_fluid
> **Critical**: No — basic filtration can be achieved with a bucket of sand, but engineered filtration equipment is necessary for reliable, high-throughput water treatment and industrial process filtration

## Principle

Filtration removes suspended solids from a fluid by passing it through a porous medium that captures particles while allowing the fluid to pass. The mechanisms include:

- **Straining (sieving)**: Particles larger than the pore openings are physically blocked. This is the primary mechanism in mesh screens, cartridge filters, and membrane filters with defined pore sizes.
- **Depth filtration**: Particles are trapped within the tortuous interstitial spaces of a granular bed (sand, gravel, activated carbon) or fibrous matrix. Particles smaller than the nominal pore size are captured by interception, diffusion, and electrostatic adhesion.
- **Cake filtration**: Accumulated retained particles form a porous cake on the filter surface, which itself acts as the filtering medium. The cake often captures finer particles than the original filter medium. This is the dominant mechanism in sand filters and filter presses after initial mat formation.

This article covers the construction of three filtration devices:

- **Sand filter vessel**: A contained bed of graded sand that removes suspended solids by depth filtration. The workhorse of water treatment — removes particles from 10-100+ μm with a mature biological layer (slow sand) or 5-50 μm (rapid sand). Gravity-driven or pressure-fed.
- **Cartridge filter housing**: A pressure vessel that holds a replaceable cylindrical filter element (pleated, wound, or melt-blown) with a defined nominal pore rating (0.1-100 μm). Used as final polishing filtration before RO membranes, ED stacks, or distribution.
- **Strainer (basket filter)**: A coarse mesh screen (perforated metal, 0.5-5 mm openings) inserted in a pipe to catch large debris (leaves, twigs, stones, rags) before pumps and delicate equipment. Line-sized, cleanable, reusable.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Concrete or ferrocement (sand filter tank) | 2-10 m³ | 1:2:4 mix (cement:sand:gravel), for gravity filters | [Chemistry: Cement](../chemistry/cement.md) | Steel tank (pressure sand filters), HDPE tank |
| Steel plate (pressure vessel) | 20-100 kg | A36 or A285, 6-12 mm wall, for pressure sand filters and cartridge housings | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (corrosive service) |
| Filter sand (silica sand) | 0.5-5 m³ | Effective size 0.15-0.55 mm, uniformity coefficient 1.5-3.0, for sand filter bed | Quarry or river | Crushed quartz, anthracite (dual-media filters) |
| Gravel (support bed) | 0.1-1.0 m³ | Graded 2-30 mm, layered coarse-to-fine under sand bed | Quarry or river | — |
| Stainless steel mesh (strainer) | 0.01-0.1 m² | Perforated 304 or 316 stainless, 0.5-5 mm hole diameter, 30-50% open area | [Metals](../metals/index.md) | Monel or Hastelloy (seawater) |
| Cartridge filter elements | 1-12 per housing | Polypropylene pleated or string-wound, 0.5-100 μm nominal rating | [Polymers](../polymers/index.md) | Ceramic elements (high-temperature, reusable) |
| Rubber gaskets | 1 set | EPDM or Buna-N, sized to flange diameter | [Elastomers](../polymers/elastomers.md) | PTFE envelope gaskets (chemical service) |

## Construction Steps

### Gravity Sand Filter (Concrete Tank)

1. **Construct the tank**: Build a rectangular or circular tank from reinforced concrete. Internal dimensions: filter bed area sized to the required flow rate. Hydraulic loading rate for slow sand: 0.1-0.4 m/hour. For rapid sand (with chemical coagulation): 5-15 m/hour. A slow sand filter serving 200 people at 100 L/person/day requires approximately 3 m² filter area (30,000 L/day ÷ 0.2 m/hour ÷ 24 hours ÷ 1000 L/m³ ≈ 6.25 m² — size for peak demand). Tank depth: 1.5-2.0 m (0.6-1.5 m sand bed + 1.0 m water depth + 0.2 m freeboard).
2. **Install underdrain system**: Place perforated PVC pipes (15-25 mm diameter, 5 mm holes at 100 mm spacing on the underside) on the tank floor in a grid pattern (300-600 mm spacing between laterals). Connect laterals to a main collector pipe that exits the tank through a sealed penetration. The underdrain collects filtered water without creating channels in the sand.
3. **Layer gravel support bed**: Cover the underdrain with 150-300 mm of graded gravel. Bottom layer: 15-30 mm gravel, 100 mm deep. Middle layer: 5-15 mm gravel, 50-100 mm deep. Top layer: 2-5 mm gravel, 50 mm deep. Each layer must be leveled flat. The gravel prevents sand from entering and blocking the underdrain.
4. **Add filter sand**: Fill with silica sand to a depth of 600-1500 mm. Add sand in 150 mm layers, washing each layer to remove fines before adding the next. Target effective size (d₁₀): 0.15-0.35 mm for slow sand, 0.45-0.55 mm for rapid sand. Uniformity coefficient (d₆₀/d₁₀): 1.5-3.0. Sand too fine → excessive head loss, short filter runs. Sand too coarse → poor particle removal.
5. **Install inlet and outlet weirs**: Install an inlet weir (V-notch or rectangular) that distributes raw water gently across the sand surface without disturbing it. Install an outlet weir with a float valve that maintains 50-100 mm of water above the sand at all times — the biological layer (schmutzdecke) dies if it dries out.
6. **Commission**: Fill the filter slowly from the bottom up (backfill through the underdrain) to drive air out of the sand bed. Once filled, switch to top-down filtration at a reduced rate. For slow sand filters, the biological layer requires 1-4 weeks to develop. During ripening, the output is not safe for drinking.

### Pressure Sand Filter (Steel Tank)

7. **Fabricate the pressure vessel**: Roll steel plate (6-12 mm thick) into a cylinder. Weld the longitudinal seam with full penetration (SAW). Weld dished heads (ellipsoidal or torispherical) to both ends. The top head includes a manway (300-400 mm diameter flanged opening) for sand access. Install flanged inlet, outlet, and drain connections. The vessel must be designed for the operating pressure (typically 3-10 bar) per pressure vessel code.
8. **Internal components**: Install an underdrain lateral system (hub and laterals, or a false bottom with nozzles) at the bottom of the vessel. Layer gravel and sand as described for the gravity filter. The sand bed depth is typically 600-900 mm. The freeboard above the sand allows 30-50% bed expansion during backwash.
9. **Piping and valves**: Connect inlet (raw water), outlet (filtered water), backwash inlet (reverse flow from bottom), and backwash waste (overflow to drain) to a valve manifold. Four valves: filter inlet, filter outlet, backwash inlet, backwash waste. Normal operation: open inlet and outlet, close backwash valves. Backwash: close inlet and outlet, open backwash inlet and waste.
10. **Backwash system**: Pressure sand filters require periodic backwashing to remove accumulated solids. Reverse the flow direction: pump clean water upward through the bed at a rate sufficient to fluidize and expand the sand bed by 30-50%. Backwash rate: 30-50 m/hour for 5-10 minutes, until the overflow water runs clear. The upward flow lifts and scours the sand grains, releasing trapped particles to the waste drain. Without backwashing, the filter clogs and head loss exceeds the available pressure.

### Cartridge Filter Housing

11. **Fabricate the housing body**: Machine or weld a cylindrical pressure vessel from stainless steel (304 for general water, 316L for corrosive or high-purity service). Length: 250-1000 mm (accommodating standard 10-inch or 40-inch cartridge elements). Diameter: sized for the number of elements (single or multi-round housing). Design pressure: 5-10 bar typical.
12. **Machine the internals**: Install a perforated plate at the bottom that seats the cartridge elements. Each element has a spring-loaded sealing mechanism (knife-edge seal or O-ring) that creates a positive seal between unfiltered (outside) and filtered (inside) chambers. Any bypass of unfiltered water renders the filter useless.
13. **Install inlet/outlet connections**: Inlet on the side (unfiltered water enters the housing and flows outside-to-inside through the cartridge). Outlet on the bottom or end cap (filtered water from the cartridge core). Install a pressure gauge on each side. Pressure drop across a clean element: 0.05-0.15 bar. Replace the element when pressure drop reaches 0.7-1.0 bar above clean.
14. **Seal the housing**: Install an O-ring on the housing closure (swing bolt or threaded cap). The closure allows cartridge replacement without disconnecting the piping.

### Inline Strainer (Basket Filter)

15. **Fabricate the body**: Cast or machine a Y-shaped or basket-shaped body from cast iron, bronze, or stainless steel. The body has a straight-through flow passage (inlet to outlet) with a branch opening that holds the strainer basket. The branch is sealed with a bolted cover or cap.
16. **Make the strainer basket**: Form a cylindrical or conical basket from perforated stainless steel sheet (0.5-5 mm hole diameter, 30-50% open area). Weld a flange at the basket top that seats against a gasket in the body. The basket must be removable for cleaning.
17. **Install in pipeline**: The strainer mounts in the pipeline with flanged or threaded ends. Install on the suction side of pumps (protects pump impellers from debris) and before delicate equipment (control valves, heat exchangers, membrane systems). Provide a isolation valve on each side for basket removal without draining the pipeline.

## Expected Performance

| Parameter | Slow Sand Filter | Pressure Sand Filter | Cartridge Filter | Basket Strainer |
|-----------|-----------------|---------------------|-----------------|-----------------|
| Removal rating | 10-100+ μm (biological layer enhances) | 5-50 μm | 0.1-100 μm (element-dependent) | 500-5000 μm |
| Turbidity removal | 90-99% | 80-95% | 95-99% | Coarse debris only |
| Flow rate | 0.1-0.4 m/hour | 5-15 m/hour | 5-50 L/min per element | Unlimited (line-sized) |
| Operating pressure | Gravity (0.1-0.3 bar) | 3-10 bar | 1-10 bar | Line pressure |
| Backwash/cleaning | Scraping top 1-2 cm of sand | Reverse flow, 30-50 m/hour | Replace element | Remove and clean basket |
| Service interval | 1-3 months (scraping) | 12-48 hours (backwash) | 1-6 months (element life) | Weekly to monthly |
| Filter media life | 5-10 years (full sand replacement) | 3-5 years (sand replacement) | Single-use elements | Indefinite (cleanable) |

## Calibration and Verification

1. **Sand filter media verification**: Before loading sand, sieve a representative sample through a stack of standard sieves (2 mm, 1 mm, 0.5 mm, 0.25 mm, 0.15 mm). Plot the grain size distribution curve. Read d₁₀ (10% finer) and d₆₀ (60% finer). Effective size = d₁₀. Uniformity coefficient = d₆₀ / d₁₀. If the sand does not meet specification, wash or re-sieve.
2. **Cartridge filter integrity**: After installing a new cartridge, pressurize the housing to 0.5 bar with clean water. Hold for 5 minutes. Inspect the downstream side for particles (shine a flashlight through a sight glass or sample port). Any particles indicate a damaged element or bypass seal.
3. **Backwash rate verification**: For pressure sand filters, measure the backwash flow rate (flow meter or timed fill) and observe the sand bed expansion through a sight glass or by removing the top manway. Target expansion: 30-50% (sand surface rises by 30-50% of bed depth). Too low → incomplete cleaning. Too high → sand washes out of the filter.

## Strengths

- Sand filters are constructible from local materials (sand, gravel, concrete) with no manufactured components — the most accessible treatment technology
- Cartridge filters provide precise, defined removal ratings from 0.1-100 μm — the standard for protecting downstream equipment (membranes, instruments)
- Basket strainers protect pumps and valves from debris with minimal pressure drop and zero consumables
- Pressure sand filters are compact relative to their throughput — 5-15× smaller footprint than gravity sand for equivalent capacity

## Weaknesses

- Slow sand filters require enormous area relative to throughput (1 m² per 50-200 people served)
- Pressure sand filters require a backwash water supply at high flow rate — typically 10-20% of the filtered water volume is consumed for backwashing
- Cartridge filters are consumable — elements are discarded after use (1-6 months). Without a supply chain, they are not sustainable long-term.
- Sand filters do not remove dissolved contaminants (salts, metals, organics) — only suspended solids and (for slow sand) some microorganisms

## Safety

- **Confined space entry**: Sand filter tanks are confined spaces. Never enter without testing the atmosphere (O₂ >19.5%, no toxic gases), ventilating, and using a safety harness with a surface attendant.
- **Pressure vessel**: Pressure sand filter tanks are pressure vessels. Never open the manway while the vessel is pressurized. Verify zero pressure on the gauge before removing bolts.
- **Biological hazard**: Slow sand filter schmutzdecke contains concentrated microorganisms, including potential pathogens. Wear gloves when scraping the filter surface. Wash hands thoroughly after maintenance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Filtered water turbidity >5 NTU | Sand too coarse; biological layer not established; filter rate too high; cracked underdrain allowing bypass | Check sand grain size (target d₁₀ = 0.15-0.35 mm for slow sand). Allow ripening period. Reduce filtration rate. Inspect underdrain. |
| Head loss exceeds available pressure | Filter bed clogged; surface crust too thick; insufficient backwash frequency | For gravity sand: scrape surface layer. For pressure sand: increase backwash frequency and duration. Check for mudball formation (agglomerated sand and silt that resists backwashing). |
| Sand appearing in filtered water | Underdrain broken; gravel support layer disturbed; sand too fine for backwash rate | Inspect underdrain laterals. Re-layer gravel support bed. Reduce backwash rate to prevent sand carryover. |
| Cartridge filter pressure drop too high immediately after installation | Wrong pore size (too fine for the application); element collapsed; excessive flow rate per element | Verify element rating matches specification. Check element for damage. Reduce flow or add elements in parallel. |
| Short filter run times (clogging rapidly) | High raw water turbidity; inadequate pretreatment; mudballs in sand bed | Add pre-sedimentation or coarse screening before the filter. For pressure sand: apply air scour before backwash to break up mudballs. |

## See Also

- [Basic Water Treatment](basic-treatment.md) — slow sand filtration for drinking water
- [SEM Tech Water Treatment](sem-tech-water-treatment.md) — cartridge pre-filtration for ED stacks
- [Desalination](desalination.md) — media filtration and cartridge guards for RO
- [Ceramics](../ceramics/index.md) — ceramic filter elements for household water treatment
- [Chemistry: Cement](../chemistry/cement.md) — concrete tank construction for gravity filters
- [Water Valves](water-valves.md) — valve manifolds for filter backwash control

[← Back to Water](index.md)
