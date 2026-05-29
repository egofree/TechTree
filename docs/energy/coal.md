# Coal Mining & Combustion

> **Node ID**: energy.fuels.coal
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`ceramics.kilns`](../ceramics/kilns.md), [`energy.fuels`](fuels.md), `mining`
> **Enables**: None (leaf capability)
> **Timeline**: Years 15-25
> **Outputs**: coal
> **Critical**: No — coal supplements charcoal and enables steam power, but charcoal and wood can substitute where coal is unavailable

### Coal Types & Properties

**Strengths**:
- Highest energy density of any solid fuel (bituminous: 25-35 MJ/kg, anthracite: 35+ MJ/kg)
- Abundant and geologically widespread — found on every continent
- Stores indefinitely — no degradation over time, unlike biomass

**Weaknesses**:
- Sulfur content (0.5-5%) causes SO₂ emissions and iron contamination during smelting
- Ash content (5-20%) reduces usable energy and creates disposal problems
- Mining is hazardous — underground mines risk explosion (methane), collapse, and black lung disease
- Not all coal is suitable for coking — only specific bituminous coals produce metallurgical coke

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

**[Properties by rank](../glossary/properties-by-rank.md)** (typical ranges):

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

- **Washing**: Pass crushed coal through water trough. Coal (SG ~1.3) floats; rock (SG ~2.5) sinks. Simple but effective. Dense-media separation (using magnetite-water slurry of controlled density 1.3-1.8 SG) gives sharper separation for finer sizes. A Baum jig washer (pulsating water column) processes 50-200 tonnes/hour and is the standard industrial washing method. Wash water is recycled through settling ponds — coal fines settle and are recovered for briquetting.
- **Sorting**: Hand-pick obvious rock and waste from conveyor or picking table. Mechanical sorting (jig washers, shaking tables) uses density differences at larger scale. Froth flotation recovers fine coal (<0.5 mm) — air bubbles attach to coal particles (hydrophobic) while mineral particles (hydrophilic) sink.
- **Crushing**: Break large lumps to uniform size before washing and sizing. Roll crusher or jaw crusher reduces run-of-mine coal to <150 mm. Avoid over-crushing — fines are harder to wash and handle.
- **Sizing**: Screen into grades — lump (50-150 mm) for boilers and forge, small (10-50 mm) for gas producers, fines (<10 mm) for briquetting or sintering. Vibrating screens with 1-3 decks separate multiple sizes simultaneously.
- **Drying**: Air-dry in covered stockpile for lignite and high-moisture coal. Reduces transport weight and improves combustion. Rotary tube dryers using waste flue gas can reduce moisture from 50% to 15% — significant energy savings in transport and combustion.
- **Briquetting**: Press fines and dust into briquettes using a binder (pitch, tar, or clay at 5-10% by weight). Roll press or ram extruder at 100-200 bar. Converts waste fines into usable fuel. Essential for lignite fines, which are otherwise too dusty to handle and burn poorly. Briquette energy density: 18-22 MJ/kg with clay binder, 24-28 MJ/kg with pitch binder.
- **Washing yield**: Typical washed coal yield from run-of-mine bituminous coal is 60-80% by weight (20-40% rejected as waste rock and mineral matter). The calorific value of the washed product increases 15-30% relative to raw coal.

### Combustion Methods

How coal is burned matters as much as what type of coal is used. The combustion method determines efficiency, labor requirements, and how completely the fuel is consumed:

- **Hand-fired grate (grate firing)**: Coal shoveled onto a flat or stepped iron grate. Air flows upward through the fuel bed from an ash pit below. Operator controls air supply with a damper door. Simple, low capital cost, labor-intensive. Requires skill to maintain an even fuel bed and avoid burning through in patches. Suitable for small boilers, forges, and heating. Thermal efficiency ~50% — significant unburned carbon falls through grate with ash.
- **Mechanical stoker (stoker firing)**: Auger, ram, or chain grate feeds coal onto the grate automatically. Chain grate moves the entire fuel bed slowly through the furnace — coal enters at one end, ash falls off the other. More uniform combustion than hand-firing, lower labor. Requires power (steam or electric) to drive the mechanism. Thermal efficiency ~65-75%. Suitable for medium-sized boilers (industrial, institutional heating).
- **Pulverized coal firing**: Grind coal to powder (<75 μm, like talcum powder), blow into furnace with preheated air. The powder burns in suspension like a gas — rapid, complete combustion with flame temperatures exceeding 1500°C. Enables the highest steam temperatures and pressures. Requires ball or roller grinding mills (coal pulverizers consuming ~20-40 kWh per tonne of coal ground), forced-draft fans, and fine particle handling equipment. The method used in large power stations and high-pressure boilers. Thermal efficiency ~85-90% — the most efficient combustion method but the most complex and capital-intensive. Coal pulverizer types: ball mill (rotating cylinder charged with steel balls, 15-25 RPM), vertical spindle mill (rollers grinding coal on a rotating table, 30-50 RPM), or hammer mill (high-speed rotating hammers, 800-1500 RPM for softer coals).

**Ash fusion temperature**: Critical for all combustion methods — if ash melts (typically 1100-1400°C for bituminous coal), it forms clinker that blocks grates and gasifiers. High-ash-fusion coal (>1400°C) is preferred for stoker firing. Low-ash-fusion coal can be used in slagging gasifiers where molten ash is tapped continuously, like blast furnace slag.

### Environmental Concerns

- **Sulfur content (0.5-5%)**: On combustion, sulfur oxidizes to SO₂, which forms sulfuric acid in the atmosphere → acid rain. Damages forests, acidifies waterways, corrodes stone and metal structures. Wash coal to reduce sulfur before burning. Flue gas desulfurization (scrubbers using limestone slurry) removes SO₂ post-combustion but is complex.
- **Ash (5-20%)**: Non-combustible mineral residue. Disposal requires ash ponds or landfill. Fly ash (fine particles carried in flue gas) must be captured with electrostatic precipitators or bag filters to prevent air pollution. Bottom ash can be used as aggregate in concrete and road base.
- **Acid mine drainage**: Pyrite (FeS₂) in coal seams oxidizes when exposed to air and water during mining, producing sulfuric acid and dissolved iron. Drainage from mines and spoil piles can contaminate streams, killing aquatic life. Treatment: neutralize with limestone, contain runoff in settlement ponds.
- **Firedamp (methane)**: Methane (CH₄) trapped in coal seams is released during mining. Concentrations of 5-15% in air are explosive. Control by ventilation — large fans drive fresh air through mine workings. The **[Davy safety lamp](../glossary/davy-safety-lamp.md)** (invented 1815) encloses the flame in fine wire gauze screen — the gauze cools flame below ignition temperature, preventing firedamp ignition. The lamp flame changes color/height in the presence of methane, serving as a gas detector. Modern mines use electronic gas detectors.
- **Spontaneous combustion**: See [Storage & Safety](#storage-safety) below.

### Coal Combustion Calculations

Understanding stoichiometric air requirements is essential for efficient furnace and boiler design:

- **Stoichiometric air for bituminous coal**: Approximately 7-9 kg of air per kg of coal (average ~8 kg air/kg coal). This assumes complete combustion of carbon to CO₂: C + O₂ → CO₂. The theoretical oxygen requirement for pure carbon is 2.67 kg O₂ per kg C; air is 23.2% oxygen by mass, so ~11.5 kg air per kg of pure carbon. Real coal contains moisture, ash, and hydrogen, modifying the requirement.
- **Excess air**: Practical combustion requires 20-60% excess air above stoichiometric to ensure complete burn. Hand-fired grates: 40-60% excess air. Pulverized coal: 15-25% excess air. Too much excess air wastes heat (heating nitrogen that goes up the stack). Too little produces CO and unburned carbon in ash.
- **Flue gas volume**: ~10-12 m³ per kg of coal at stoichiometric, increasing with excess air. At 50% excess air, flue gas volume ~14-16 m³/kg. Chimney and flue sizing must accommodate this flow.
- **Theoretical flame temperature**: Bituminous coal with 20% excess air reaches ~1900-2100°C adiabatic flame temperature. Actual flame temperature is lower (~1200-1500°C) due to heat losses and dissociation.
- **Heat balance**: Of the coal's calorific value, roughly 80-90% is released as sensible heat in the furnace. Losses include: dry flue gas (10-20% — heated nitrogen and CO₂ leaving the stack), moisture in fuel and air (2-5%), unburned carbon in ash (1-5%), radiation from boiler surfaces (1-3%).

### Coal Grading by Calorific Value

Industrial consumers select coal grades by energy content, ash, and sulfur to match their application:

| Grade | Calorific Value | Ash | Sulfur | Typical Application |
|-------|----------------|-----|--------|-------------------|
| Premium steam coal | >28 MJ/kg | <8% | <1% | High-pressure boilers, power generation |
| Standard steam coal | 24-28 MJ/kg | 8-15% | 1-2% | Industrial boilers, forging |
| Low-grade thermal | 18-24 MJ/kg | 15-25% | 1-3% | Fluidized bed combustion, drying kilns |
| Coking coal | 28-33 MJ/kg | <10% | <1% | Coke oven feedstock exclusively |
| Domestic heating | 22-30 MJ/kg | <15% | <2% | House heating, cooking stoves |

**Blending**: Power stations often blend high-ash and low-ash coals to meet boiler specifications. A typical blend ratio: 60% medium-ash (20% ash) + 40% low-ash (8% ash) → blended ash ~15.2%. Sulfur can also be managed by blending — mix high-sulfur coal with low-sulfur coal to stay below emission thresholds.

### Coke Production Cross-Reference

Coking coal is the specific grade of bituminous coal (20-30% volatile matter, low sulfur, low ash) that softens, swells, and re-solidifies into hard, porous coke when heated to 900-1100°C in the absence of air. Coke is the indispensable fuel for blast furnace ironmaking and silicon reduction, burning at 1800-2100°C — far hotter than raw coal can achieve.

- **Testing for coking quality**: Heat a crushed sample in a covered crucible at 900°C for 10 minutes. A good coking coal produces a swollen, hard, coherent button. Non-coking coal produces powder.
- **Coking coal is a strategic resource**: Not all bituminous coal is suitable for coking. Low-phosphorus coking coal (<0.05% P) is particularly scarce and valuable — phosphorus cannot be removed from steel and causes cold shortness.
- **See full detail**: [coke.md](coke.md) for beehive ovens, by-product recovery ovens, coke quality specifications, and quenching methods.

### Coal Gasification

Coal can be converted to combustible gases by partial combustion or reaction with steam — useful for producing fuel gas without full combustion. Gasification is the bridge between solid coal and gaseous/liquid fuel applications:

- **Producer gas**: Blow air through a hot bed of coal or coke in a gasifier (vertical shaft furnace). Reactions: C + O₂ → CO₂ (combustion zone), then CO₂ + C → 2CO (reduction zone). Product gas: ~25% CO, ~55% N₂, ~10% H₂, minor CO₂ and CH₄. Low calorific value (~5 MJ/m³) due to nitrogen dilution. Suitable for firing furnaces and boilers directly — pipe gas from gasifier to burner without cooling. Simple technology, widely used in early industrial era and during fuel shortages (wood gasifiers for vehicles in WWII).
- **Water gas**: Blow steam through a hot bed of coke (not raw coal — coke to avoid tars). Reaction: C + H₂O → CO + H₂ (endothermic — requires alternating with air blast to reheat bed). Product gas: ~50% H₂, ~40% CO, ~5% CO₂, ~5% N₂. Higher calorific value (~11 MJ/m³) than producer gas. The endothermic steam reaction cools the bed; operators alternate 3-5 minute steam blasts with 2-3 minute air blasts to reheat. This cyclic operation produces two distinct gas streams — the "water gas" (steam blast, rich in H₂ and CO) and the "blow gas" (air blast, mostly N₂ and CO₂, often vented or used as heating fuel). Water gas temperature at the generator exit: ~500-700°C during steam blast, ~1000-1200°C during air blast. Used as chemical feedstock (source of hydrogen for ammonia synthesis via Haber-Bosch process at 400-500°C, 200-300 atm over iron catalyst).
- **Town gas (coal gas)**: Produced by destructive distillation of coal in coke ovens or retorts (heating coal in absence of air at 900-1100°C). Gas composition: ~50% H₂, ~30% CH₄, ~10% CO, with minor CO₂, C₂H₄, N₂. Calorific value ~18 MJ/m³. Byproducts: coke (solid), coal tar (source of chemicals: benzene, toluene, naphthalene, creosote), ammonia liquor. Historically the primary fuel for urban lighting and cooking before natural gas pipelines (19th century through mid-20th century). Coal tar was the foundation of the synthetic chemical industry. Full detail on coke production and byproduct recovery in [coke.md](coke.md).

**Water gas production detail**: The water gas process operates in two distinct phases that must alternate:
1. **Run (steam) phase**: Steam at 2-5 bar enters the bottom of a hot bed of coke (bed temperature ~1000-1200°C from the previous air blast). The endothermic C + H₂O reaction produces CO + H₂ while cooling the bed. Gas exit temperature: 500-700°C. Phase duration: 3-5 minutes until bed temperature drops below ~800°C.
2. **Blow (air) phase**: Air replaces steam. Exothermic C + O₂ reactions reheat the bed to 1000-1200°C. Blow gas (mostly N₂ + CO₂, low heating value) is either vented or burned in a waste heat boiler for steam generation. Phase duration: 1-3 minutes.
- **Carbureted water gas**: To increase calorific value, oil (gas oil or tar oil) is sprayed into the hot water gas in a carburetor chamber lined with checker brick at 800-1000°C. The oil cracks into light hydrocarbons (CH₄, C₂H₄, higher aromatics), raising the calorific value to 14-20 MJ/m³. This was the standard town gas production method before natural gas pipelines.

**[Gasifier construction](../glossary/gasifier-construction.md)** (for producer gas — simplest type): Vertical cylindrical shaft of firebrick or steel-lined refractory. Coal/charcoal charged from top. Air inlet (tuyere) near bottom. Grate at bottom supports fuel bed. Gas outlet near top (updraft) or at grate level (downdraft — cleaner gas, less tar). Diameter 0.5-3 m depending on output. Typical output: 100-5000 m³ gas/hour. The gasifier grate must rotate or be shaken periodically to break up clinker (ash that has fused into solid masses at high temperature). Clinker formation is worse with high-ash coal — use washed coal for gasification. Gas exit temperature: 400-600°C (updraft, sensible heat in gas) or 100-200°C (downdraft, heat consumed by reduction reactions).

### Storage & Safety

Coal in large piles can self-heat and ignite spontaneously from bacterial oxidation of pyrite (FeS₂) and slow reaction with air. This is a serious hazard at mines, power stations, and any facility storing large quantities of coal:
- **Pile size**: Limit stockpile height to 3-5 m. Avoid compaction (compressed coal oxidizes faster).
- **Ventilation**: Do NOT seal piles — trapped heat builds up. Instead, monitor temperature with iron rods pushed into pile (withdraw and feel — warm = danger, hot = move immediately).
- **Turnover**: Use oldest coal first (FIFO). Rotate stockpile within 3-6 months.
- **Firefighting**: Do NOT use water on a coal pile fire — steam explosion risk and water spreads the fire by creating channels for air. Instead: dig out burning section, spread thin to cool, or smother with fine damp sand. For underground coal seam fires, the only reliable method is to cut off air supply by sealing mine entries, or excavate the burning coal entirely. Some coal seam fires burn for decades or centuries (Centralia, Pennsylvania has burned since 1962).
- **Mine gases**: Beyond firedamp (methane), blackdamp (CO₂ + N₂, suffocating, collects in low spots) and afterdamp (CO, toxic, follows explosions) are lethal hazards in underground mines. Continuous ventilation and gas monitoring are essential. Canaries in cages were historically used as early-warning gas detectors — a canary succumbs to toxic gases before a human, giving miners time to evacuate.
- **Coal workers' pneumoconiosis (black lung)**: Chronic inhalation of coal dust causes progressive lung fibrosis. Prevention: wet cutting (water spray on drill and cutting heads), ventilation, and respiratory protection for all underground workers. Dust concentration limit: <2 mg/m³ of respirable dust.
- **Subsidence**: Underground mining removes support, causing surface ground to subside. Building damage, altered drainage, and disrupted infrastructure result. Fill mined voids with waste rock (stowing) where possible.

### Cross-References

- **Coke production** (refined coal): [coke.md](coke.md)
- **Steam power** (primary coal consumer): [steam-power.md](steam-power.md)
- **Fuel comparison table**: [fuels.md](fuels.md)
- **Mining methods**: [extraction.md](../mining/extraction.md)
- **Iron smelting** (coke-fueled blast furnace): [iron-steel.md](../metals/iron-steel.md)

### Combustion Equipment Selection

Matching combustion method to application determines overall system efficiency:

| Application | Recommended Method | Typical Efficiency | Notes |
|-------------|-------------------|-------------------|-------|
| Small forge/hearth | Hand-fired grate | 40-50% | Simple, controllable by skilled smith |
| Heating boiler (<500 kW) | Hand-fired or underfeed stoker | 55-65% | Underfeed stoker automates fuel feed |
| Industrial boiler (1-20 MW) | Chain grate stoker | 65-75% | Uniform combustion, low labor |
| Power station (>20 MW) | Pulverized coal firing | 85-90% | Requires grinding mills, forced draft |
| Gas production | Gasifier (fixed bed) | 65-75% (cold gas) | Converts solid to gas fuel |
| Coke production | Coke oven (by-product) | ~70% (coke yield) | Maximum byproduct recovery |

**Ash handling**: All coal combustion produces ash (5-20% of fuel weight). Bottom ash falls through the grate into an ash pit — remove regularly to prevent airflow blockage. Fly ash (fine particles entrained in flue gas) must be captured with cyclone separators (60-80% capture) or electrostatic precipitators (99%+ capture, requires electricity). Fly ash is usable as pozzolanic additive in cement, replacing 15-30% of Portland cement.

### Environmental Controls

- **Particulate emission**: Uncontrolled coal combustion emits 10-50 kg of fly ash per tonne of coal burned. Cyclone collectors reduce this to 2-10 kg/t, bag filters to <0.05 kg/t, and electrostatic precipitators to <0.02 kg/t. Without particulate control, surrounding areas suffer severe air quality degradation.
- **SO₂ control**: Flue gas desulfurization (FGD) sprays limestone (CaCO₃) slurry into the flue gas. Reaction: CaCO₃ + SO₂ + ½O₂ → CaSO₄·2H₂O (gypsum). Removes 90-97% of SO₂. Gypsum byproduct is usable in wallboard manufacture. Alternatively, simple wet scrubbers using seawater or alkaline waste water achieve 70-90% removal.
- **NOx control**: Formed from nitrogen in combustion air at temperatures above 1300°C. Control methods: staged combustion (primary zone fuel-rich, secondary zone air-rich — reduces peak temperature), flue gas recirculation (dilutes combustion air with inert gas, lowering peak temperature by 100-200°C), and low-NOx burners (designed to delay fuel-air mixing).

### Coal Storage & Transport

- **Stockpile management**: Coal stored outdoors degrades from weathering (oxidation, moisture cycling). Lignite degrades fastest — loses 5-15% calorific value per year of outdoor storage. Bituminous coal is more stable but still loses 1-3% per year. Anthracite is essentially stable indefinitely.
- **Transport**: By barge (cheapest per tonne-km, ~0.01-0.03 $/tkm), rail (standard for inland transport, 0.03-0.08 $/tkm), truck (flexible but expensive, 0.10-0.30 $/tkm), or conveyor (mine-mouth to power station, <10 km distance). A standard rail gondola car carries 90-100 tonnes of coal; a unit train of 100 cars delivers ~10,000 tonnes.
- **Handling equipment**: Bucket ladder reclaimer for stockpile retrieval (500-5000 t/hour). Conveyor belts (0.5-2.0 m wide, 2-5 m/s belt speed) for movement between receiving, storage, and consumption points. Chutes and transfer towers must be designed with minimum 50° angles to prevent coal bridging and plugging.

### Summary

Coal is the foundational fossil fuel of industrial civilization. It provides the highest energy density of any solid fuel, powers steam engines and furnaces, and feeds coke ovens for iron smelting. Understanding coal rank is essential: burning lignite where bituminous is needed wastes energy on evaporating moisture, while using anthracite for coking fails entirely (it won't soften and fuse). Coal gasification extends coal's utility to gaseous fuel applications, and town gas was historically the path to urban lighting and the chemical industry. The environmental costs — acid rain, mine drainage, air pollution — must be managed from the outset through coal washing, ventilation, and proper waste handling.

**Critical path**: The sequence from raw coal to industrial capability is: mine coal → wash and size → burn in boilers for steam power → select coking coal → produce coke → smelt iron at scale → build machines → generate electricity → bootstrap all subsequent industry.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*

---

**[Coal data summary](../glossary/coal-data-summary.md)** (typical bituminous, washed):
- Calorific value: 26-32 MJ/kg
- Carbon: 65-85% | Hydrogen: 4-6% | Oxygen: 5-15% | Sulfur: 0.5-2% | Ash: 5-12%
- Bulk density: 700-900 kg/m³ (loose), 1000-1200 kg/m³ (compacted)
- Stoichiometric air: ~8 kg air/kg coal
- Ash fusion temperature: 1100-1400°C

### Limitations

- **Environmental impact**: Coal combustion produces CO₂ (the dominant greenhouse gas), SO₂ (acid rain), NOₓ, and particulate matter. Sulfur content 0.5-2% creates significant air quality concerns.
- **Mining hazards**: Underground coal mining risks include methane explosions, coal dust explosions, roof collapse, and black lung disease. Surface mining causes habitat destruction and acid mine drainage.
- **Non-renewable**: Coal deposits are finite. Even large deposits deplete over decades of intensive mining.
- **Transportation cost**: Coal is bulky (700-900 kg/m³). Transport cost often exceeds mining cost for distances over 100 km, favoring mine-mouth power plants.
- **Ash disposal**: 5-12% ash by weight means a 1000 MW coal plant produces 200,000-500,000 tonnes of ash per year, requiring disposal or utilization (cement additive, road base).

### See Also

- [Coke Production](coke.md) — Coal processing for metallurgical coke
- [Steam Power](steam-power.md) — Coal-fired boilers and steam engines
- [Steam Turbines](steam-turbines.md) — Coal-fired power generation
- [Charcoal](charcoal.md) — Renewable alternative to coal for some applications
- [Fuels](fuels.md) — Comparative fuel properties
- [Cement Production](../chemistry/cement.md) — Major industrial coal consumer

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
