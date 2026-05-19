# Coal Mining & Combustion

> **Node ID**: energy.fuels.coal
> **Domain**: Energy
> **Timeline**: Years 15-25
> **Outputs**: coal

### Coal Types & Properties

Not all coal is equal. Rank (degree of metamorphism) determines energy content, impurity load, and suitable applications.

| Type | Carbon | Energy | Moisture | Volatiles | Primary Use |
|------|--------|--------|----------|-----------|-------------|
| Lignite | 25-35% | 15-25 MJ/kg | 30-60% | 45-55% | Power generation (dried) |
| Sub-bituminous | 35-45% | 20-28 MJ/kg | 15-30% | 35-45% | Steam boilers, heating |
| Bituminous | 45-86% | 25-35 MJ/kg | 5-15% | 15-45% | Coking, steam, forging |
| Anthracite | 86-97% | 35+ MJ/kg | <5% | <8% | Clean heating, smithing |

**Selection for coking**: Bituminous coal with 20-30% volatile matter, low sulfur (<1%), moderate ash (<10%). Not all coal makes good coke — test by heating a small sealed sample and checking if the residue is hard and porous (good coke) vs. powdery (non-coking coal).

### Coal Rank Progression

Coal forms from plant material buried and compressed over geological time. The rank progression reflects increasing heat and pressure over millions of years. Peat accumulates in wetlands where plant debris does not fully decompose (anaerobic conditions). As peat is buried under sediment, increasing pressure drives out water and increasing temperature drives off volatile compounds, concentrating fixed carbon. Progression from peat to anthracite typically requires 50-300 million years. Higher-rank coal is found in geologically older, more deeply buried deposits.

The rank of a coal deposit is determined primarily by the maximum temperature and pressure it experienced during burial. Rapidly buried coal in tectonically active regions may reach bituminous or anthracite rank faster than slowly buried coal in stable basins.

| Rank | Carbon (dry, ash-free) | Energy | Key Properties |
|------|----------------------|--------|----------------|
| Peat | ~50% | 10-15 MJ/kg | High moisture (75-90% wet), crumbles, fibrous texture, not yet true coal |
| Lignite (brown coal) | 60-70% | 15-20 MJ/kg | Brown color, crumbles, high moisture (30-60%), shrinks and cracks on drying |
| Sub-bituminous | 70-76% | 20-24 MJ/kg | Dark brown to black, moderate moisture (15-30%), still relatively soft |
| Bituminous | 76-90% | 24-35 MJ/kg | Black, breaks into blocky chunks, most common steam coal, good coking varieties |
| Anthracite | 90-95% | 30-35 MJ/kg | Black with metallic luster, conchoidal fracture, very hard, low volatile matter, cleanest burn |

**Field identification by rank**:
- **Peat**: Brown, fibrous, crumbles easily. Visible plant fragments. Feels spongy when wet.
- **Lignite**: Brown to dark brown, crumbles, stains fingers. Dries to powder.
- **Sub-bituminous**: Dark brown to black, still relatively soft. Does not stain as much as lignite.
- **Bituminous**: Black and dense, breaks into blocky rectangular pieces along natural fractures (cleats). Most common industrial coal.
- **Anthracite**: Black with metallic luster, very hard, breaks with conchoidal (shell-like) fracture. Feels denser and heavier than bituminous. Difficult to ignite but burns very clean with little smoke.

**Properties by rank** (typical ranges):

| Property | Lignite | Sub-bituminous | Bituminous | Anthracite |
|----------|---------|----------------|------------|------------|
| Fixed carbon | 25-30% | 30-45% | 45-85% | 85-95% |
| Volatile matter | 45-55% | 35-45% | 15-45% | 2-8% |
| Ash content | 5-15% | 5-15% | 3-20% | 5-15% |
| Sulfur content | 0.5-3% | 0.3-2% | 0.5-5% | 0.5-1.5% |

### Coal Mining

See [Mining](../mining/extraction.md) for full extraction methods. Key considerations for coal specifically:

- **Drift mining**: Horizontal tunnel into hillside coal seam. Simplest access where geology allows.
- **Shaft mining**: Vertical shaft to deeper seams. Requires winding gear, ventilation, and water pumping (steam engines solve the pumping problem — see [Steam Power](steam-power.md)).
- **Roof support**: Timber pit props at 1-2 m intervals. Replace when cracking sounds are heard.

**Mining methods by deposit depth and scale**:

- **Surface / open-cast (strip mining)**: Remove overburden (soil and rock above the coal seam) with dragline or shovel, then dig coal. Used for near-surface seams (<60 m depth). Overburden-to-coal ratio must be favorable (typically <10:1). Fastest, cheapest, safest method. Reclaim land after mining by replacing overburden and topsoil. Suitable for lignite and sub-bituminous deposits. The method of choice where geology permits — most of the world's lignite is mined this way.
- **Room-and-pillar**: Mine horizontal tunnels (rooms) into the coal seam, leaving pillars of coal for roof support. Pillars are typically 8-15 m square, rooms 5-10 m wide. Recovery ~50% (half the coal stays in pillars). Used for flat-lying seams at moderate depth. Can extract pillars on retreat (retreat mining) for higher recovery, but with increased roof collapse risk.
- **Longwall**: A shearer (rotary cutting drum on an armored chain) moves back and forth along a coal face 200-300 m wide, cutting coal in slices 0.6-1.0 m thick. Hydraulic roof supports (chocks, individually adjustable) advance with the shearer. Roof is allowed to collapse behind the supports (goaf). Recovery ~80%, the highest of any underground method. Requires sophisticated hydraulic equipment. Most productive underground method for thick, uniform seams. Well-suited to the steam-hydraulic technology level.

### Coal Preparation

Raw coal contains rock, clay, and sulfur-bearing minerals that reduce efficiency and increase smoke:
- **Washing**: Pass crushed coal through water trough. Coal (SG ~1.3) floats; rock (SG ~2.5) sinks. Simple but effective. Dense-media separation (using magnetite-water slurry of controlled density) gives sharper separation for finer sizes.
- **Sorting**: Hand-pick obvious rock and waste from conveyor or picking table. Mechanical sorting (jig washers, shaking tables) uses density differences at larger scale.
- **Crushing**: Break large lumps to uniform size before washing and sizing. Roll crusher or jaw crusher reduces run-of-mine coal to <150 mm. Avoid over-crushing — fines are harder to wash and handle.
- **Sizing**: Screen into grades — lump (50-150 mm) for boilers and forge, small (10-50 mm) for gas producers, fines (<10 mm) for briquetting or sintering.
- **Drying**: Air-dry in covered stockpile for lignite and high-moisture coal. Reduces transport weight and improves combustion.
- **Briquetting**: Press fines and dust into briquettes using a binder (pitch, tar, or clay). Converts waste fines into usable fuel. Essential for lignite fines, which are otherwise too dusty to handle and burn poorly.

### Combustion Methods

How coal is burned matters as much as what type of coal is used. The combustion method determines efficiency, labor requirements, and how completely the fuel is consumed:

- **Hand-fired grate (grate firing)**: Coal shoveled onto a flat or stepped iron grate. Air flows upward through the fuel bed from an ash pit below. Operator controls air supply with a damper door. Simple, low capital cost, labor-intensive. Requires skill to maintain an even fuel bed and avoid burning through in patches. Suitable for small boilers, forges, and heating. Thermal efficiency ~50% — significant unburned carbon falls through grate with ash.
- **Mechanical stoker (stoker firing)**: Auger, ram, or chain grate feeds coal onto the grate automatically. Chain grate moves the entire fuel bed slowly through the furnace — coal enters at one end, ash falls off the other. More uniform combustion than hand-firing, lower labor. Requires power (steam or electric) to drive the mechanism. Thermal efficiency ~65-75%. Suitable for medium-sized boilers (industrial, institutional heating).
- **Pulverized coal firing**: Grind coal to powder (<75 μm, like talcum powder), blow into furnace with preheated air. The powder burns in suspension like a gas — rapid, complete combustion with flame temperatures exceeding 1500°C. Enables the highest steam temperatures and pressures. Requires ball or roller grinding mills, forced-draft fans, and fine particle handling equipment. The method used in large power stations and high-pressure boilers. Thermal efficiency ~85-90% — the most efficient combustion method but the most complex and capital-intensive.

### Environmental Concerns

- **Sulfur content (0.5-5%)**: On combustion, sulfur oxidizes to SO₂, which forms sulfuric acid in the atmosphere → acid rain. Damages forests, acidifies waterways, corrodes stone and metal structures. Wash coal to reduce sulfur before burning. Flue gas desulfurization (scrubbers using limestone slurry) removes SO₂ post-combustion but is complex.
- **Ash (5-20%)**: Non-combustible mineral residue. Disposal requires ash ponds or landfill. Fly ash (fine particles carried in flue gas) must be captured with electrostatic precipitators or bag filters to prevent air pollution. Bottom ash can be used as aggregate in concrete and road base.
- **Acid mine drainage**: Pyrite (FeS₂) in coal seams oxidizes when exposed to air and water during mining, producing sulfuric acid and dissolved iron. Drainage from mines and spoil piles can contaminate streams, killing aquatic life. Treatment: neutralize with limestone, contain runoff in settlement ponds.
- **Firedamp (methane)**: Methane (CH₄) trapped in coal seams is released during mining. Concentrations of 5-15% in air are explosive. Control by ventilation — large fans drive fresh air through mine workings. The **Davy safety lamp** (invented 1815) encloses the flame in fine wire gauze screen — the gauze cools flame below ignition temperature, preventing firedamp ignition. The lamp flame changes color/height in the presence of methane, serving as a gas detector. Modern mines use electronic gas detectors.
- **Spontaneous combustion**: See [Storage & Safety](#storage--safety) below.

### Coal Gasification

Coal can be converted to combustible gases by partial combustion or reaction with steam — useful for producing fuel gas without full combustion. Gasification is the bridge between solid coal and gaseous/liquid fuel applications:

- **Producer gas**: Blow air through a hot bed of coal or coke in a gasifier (vertical shaft furnace). Reactions: C + O₂ → CO₂ (combustion zone), then CO₂ + C → 2CO (reduction zone). Product gas: ~25% CO, ~55% N₂, ~10% H₂, minor CO₂ and CH₄. Low calorific value (~5 MJ/m³) due to nitrogen dilution. Suitable for firing furnaces and boilers directly — pipe gas from gasifier to burner without cooling. Simple technology, widely used in early industrial era and during fuel shortages (wood gasifiers for vehicles in WWII).
- **Water gas**: Blow steam through a hot bed of coke (not raw coal — coke to avoid tars). Reaction: C + H₂O → CO + H₂ (endothermic — requires alternating with air blast to reheat bed). Product gas: ~50% H₂, ~40% CO, ~5% CO₂, ~5% N₂. Higher calorific value (~11 MJ/m³) than producer gas. Used for heating and as chemical feedstock (source of hydrogen for ammonia synthesis via Haber process).
- **Town gas (coal gas)**: Produced by destructive distillation of coal in coke ovens or retorts (heating coal in absence of air at 900-1100°C). Gas composition: ~50% H₂, ~30% CH₄, ~10% CO, with minor CO₂, C₂H₄, N₂. Calorific value ~18 MJ/m³. Byproducts: coke (solid), coal tar (source of chemicals: benzene, toluene, naphthalene, creosote), ammonia liquor. Historically the primary fuel for urban lighting and cooking before natural gas pipelines (19th century through mid-20th century). Coal tar was the foundation of the synthetic chemical industry.

**Gasifier construction** (for producer gas — simplest type): Vertical cylindrical shaft of firebrick or steel-lined refractory. Coal/charcoal charged from top. Air inlet (tuyere) near bottom. Grate at bottom supports fuel bed. Gas outlet near top (updraft) or at grate level (downdraft — cleaner gas, less tar). Diameter 0.5-3 m depending on output. Typical output: 100-5000 m³ gas/hour.

### Storage & Safety

Coal in large piles can self-heat and ignite spontaneously from bacterial oxidation of pyrite (FeS₂) and slow reaction with air. This is a serious hazard at mines, power stations, and any facility storing large quantities of coal:
- **Pile size**: Limit stockpile height to 3-5 m. Avoid compaction (compressed coal oxidizes faster).
- **Ventilation**: Do NOT seal piles — trapped heat builds up. Instead, monitor temperature with iron rods pushed into pile (withdraw and feel — warm = danger, hot = move immediately).
- **Turnover**: Use oldest coal first (FIFO). Rotate stockpile within 3-6 months.
- **Firefighting**: Do NOT use water on a coal pile fire — steam explosion risk and water spreads the fire by creating channels for air. Instead: dig out burning section, spread thin to cool, or smother with fine damp sand. For underground coal seam fires, the only reliable method is to cut off air supply by sealing mine entries, or excavate the burning coal entirely. Some coal seam fires burn for decades or centuries (Centralia, Pennsylvania has burned since 1962).
- **Mine gases**: Beyond firedamp (methane), blackdamp (CO₂ + N₂, suffocating, collects in low spots) and afterdamp (CO, toxic, follows explosions) are lethal hazards in underground mines. Continuous ventilation and gas monitoring are essential. Canaries in cages were historically used as early-warning gas detectors — a canary succumbs to toxic gases before a human, giving miners time to evacuate.

### Cross-References

- **Coke production** (refined coal): [coke.md](coke.md)
- **Steam power** (primary coal consumer): [steam-power.md](steam-power.md)
- **Fuel comparison table**: [fuels.md](fuels.md)
- **Mining methods**: [extraction.md](../mining/extraction.md)
- **Iron smelting** (coke-fueled blast furnace): [iron-steel.md](../metals/iron-steel.md)

### Summary

Coal is the foundational fossil fuel of industrial civilization. It provides the highest energy density of any solid fuel, powers steam engines and furnaces, and feeds coke ovens for iron smelting. Understanding coal rank is essential: burning lignite where bituminous is needed wastes energy on evaporating moisture, while using anthracite for coking fails entirely (it won't soften and fuse). Coal gasification extends coal's utility to gaseous fuel applications, and town gas was historically the path to urban lighting and the chemical industry. The environmental costs — acid rain, mine drainage, air pollution — must be managed from the outset through coal washing, ventilation, and proper waste handling.

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
