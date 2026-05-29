# Metallurgical-Grade Silicon Production

> **Node ID**: silicon.mg-si-production
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`energy.electric-furnaces`](../energy/electric-furnaces.md), `mining`
> **Dependencies**: [`energy.electric-furnaces`](../energy/electric-furnaces.md), [`mining.quarrying`](../mining/index.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-40
> **Outputs**: mg_silicon
> **Critical**: Yes — gateway to all semiconductor and solar cell manufacturing

## Metallurgical-Grade Silicon (MG-Si) Production

**Process**: Carbothermic reduction of quartz in submerged arc electric furnace.
- **Reaction**: SiO₂ + 2C → Si + 2CO (endothermic, ΔH ≈ +690 kJ/mol)
- **Temperature**: ~1800-2100°C in the reaction zone
- **Raw materials**:
  - **Quartz**: High-purity SiO₂ (>98%). Crushed to 2-10 cm lumps. Impurities (Fe, Al, Ca) become contaminants in product silicon.
  - **Carbon reductant**: Mix of charcoal, coke, and wood chips (provides porosity for gas escape). Coal/coke alone produces dense charge that traps gas.
  - **Typical charge ratio**: ~2 tonnes quartz + 1 tonne carbon → ~1 tonne MG-Si (+ byproducts)
- **Furnace construction**:
  - **Shell**: Steel, 3-8 m diameter, lined with carbon refractory (prebaked carbon blocks or rammed carbon paste).
  - **Electrodes**: 1-3 prebaked graphite electrodes (Søderberg self-baking electrodes possible). Diameter 300-800 mm. Suspended from hydraulic hoists, adjustable height.
  - **Power**: 5-30 MW per furnace. Three-phase AC (for 3-electrode furnace). Voltage 100-250V, current 20,000-100,000 A.
  - **Tapping**: Molten silicon (density 2.33 g/cm³, lighter than slag) tapped from furnace bottom through taphole into cast iron molds or ladle. Tap every 1-4 hours.
- **Energy consumption**: ~11-13 kWh/kg MG-Si (this is enormous — a 1 tonne/day furnace needs ~500 kW continuous).
- **MG-Si purity**: ~97-99% Si. Major impurities: Fe (0.3-0.8%), Al (0.2-0.7%), Ca (0.1-0.5%), Ti, Mn, C. Not pure enough for electronics or efficient solar cells.
- **Crushing**: Break MG-Si ingots to 1-10 cm chunks with jaw crusher, then ball mill to 100-500 μm powder for chemical purification.

**Strengths**:
- Carbothermic reduction is a single-step process from quartz to metallic silicon — no intermediate chemistry required
- Well-established at industrial scale with 50+ years of operating experience and known failure modes

**Weaknesses**:
- Enormous energy consumption at 11-13 kWh/kg makes MG-Si production uneconomic without cheap, continuous electricity
- Product purity limited to 97-99% — insufficient for electronics or efficient solar cells without further purification

## Yield & Material Balance

- **Silicon yield**: 75-85% of theoretical. Losses come from SiO gas escaping the furnace (SiO₂ + C → SiO + CO at intermediate temperatures), silicon dissolving into slag, and spillage during tapping.
- **Specific consumption**: ~2.7-3.0 tonnes quartz + 1.0-1.4 tonnes carbon reductant per tonne of MG-Si produced. Wood chips add ~0.5-1.0 tonnes for porosity (partial reductant, partial gas channel).
- **Improving yield**: Charge porosity is critical. Too dense → SiO gas trapped, forms SiO₂ fume that condenses in off-gas system (lost silicon). Too porous → uneven heating, cold spots. Wood chip ratio is a tuning parameter.

**Strengths**:
- 75-85% silicon yield is achievable with proper charge porosity management — wood chips provide a simple tuning parameter
- Silica fume byproduct (200-400 kg/t Si) has commercial value as concrete additive, partially offsetting raw material costs

**Weaknesses**:
- 15-25% of silicon input lost as SiO fume and slag — represents significant raw material waste
- Yield highly sensitive to charge porosity; requires experienced operators to tune wood chip ratio for specific quartz/reductant combinations

## Electrode Consumption

Electrodes are a major operating cost and a bootstrapping dependency:
- **Prebaked graphite electrodes**: Consumption ~400-500 kg per tonne Si. Higher cost, lower consumption, more consistent operation. Must be manufactured off-site (see [electric-furnaces.md](../energy/electric-furnaces.md) for electrode manufacturing).
- **Søderberg self-baking electrodes**: Consumption ~300-400 kg per tonne Si. Carbon paste (petroleum coke + coal tar pitch) added continuously at top of electrode column. Furnace heat bakes the paste as it descends — no separate graphitization step needed. Simpler supply chain but less pure (contaminants from paste enter silicon).
- **Choice for bootstrapping**: Søderberg electrodes are easier to produce (no graphitization furnace required) but introduce more impurities. For MG-Si destined for chemical purification (Siemens process), this is acceptable since impurities are removed downstream.

**Strengths**:
- Søderberg self-baking electrodes eliminate the need for a separate graphitization furnace — lower bootstrapping complexity
- Prebaked electrodes give more consistent operation and lower impurity levels when downstream purity justifies the cost

**Weaknesses**:
- Both electrode types consume 300-500 kg per tonne Si — a major operating cost and continuous supply chain burden
- Søderberg paste baking releases volatile organic emissions requiring dedicated capture and treatment

## Off-Gas Handling

The furnace produces large volumes of hot, toxic gas:
- **CO gas**: ~2.5-3.5 tonnes CO per tonne Si. Carbon monoxide is flammable (LFL 12.5% in air) and acutely toxic (binds hemoglobin 200× stronger than O₂). Must be captured, never vented untreated.
  - **Flaring**: Burn CO to CO₂ at the furnace hood. Simple but wastes chemical energy. Requires continuous pilot light — if flame extinguishes, raw CO accumulates.
  - **Energy recovery**: Route CO to a boiler or gas turbine for co-generation. Recovers ~30-40% of furnace electrical input as thermal energy. Requires gas cleaning (dust, SiO fume) before combustion.
- **SiO fume**: Silicon monoxide vapor condenses to ultrafine SiO₂ particles (<1 μm) in the off-gas. Known as "silica fume." Collected in baghouse filters. ~200-400 kg per tonne Si. Valuable byproduct — sold as pozzolanic additive for high-strength concrete, or reprocessed.
- **Dust**: Quartz fines and carbon particles entrained in gas stream. Removed by cyclone separators + baghouse. Recycle coarse dust to furnace charge.

**Strengths**:
- CO gas energy recovery (30-40% of electrical input) significantly improves overall plant energy efficiency
- Silica fume byproduct sells as high-value pozzolanic concrete additive, turning a waste stream into revenue

**Weaknesses**:
- CO is acutely toxic and flammable — any off-gas system leak creates immediate life safety hazard
- Silica fume particles (<1 μm) require baghouse filtration; filter bags need frequent replacement

## Slag Management

- **Slag formation**: Impurities in quartz and reductant (Al₂O₃, CaO, FeO, MgO) form a molten slag layer floating above the denser silicon. Slag is intentionally managed — sometimes flux (lime, silica) is added to control slag viscosity and trap impurities.
- **Slag composition** (typical): 30-50% SiO₂, 15-30% Al₂O₃, 10-20% CaO, 5-15% SiC, balance FeO, MgO. Varies with raw material quality.
- **Tapping**: Slag tapped separately from silicon through a higher taphole (slag floats on silicon). Some furnaces use a single taphole with sequential tapping (slag first, then silicon).
- **Disposal or reuse**: Slag can be crushed and used as road base aggregate or construction fill. If heavy metal content is low, it may be returned to the furnace as partial charge (recovers trapped silicon). Some operators sell slag to cement manufacturers as a silica source.

**Strengths**:
- Slag acts as an impurity sink, trapping Al₂O₃, CaO, and FeO that would otherwise contaminate the silicon product
- Crushed slag has secondary market value as construction aggregate or cement additive, reducing disposal costs

**Weaknesses**:
- Slag carries 3-8% entrained silicon per pass — a direct product loss
- Heavy metal content in slag may classify it as hazardous waste, requiring specialized disposal

## Furnace Startup & Shutdown

- **Cold startup** (from ambient): Preheat furnace with gas burners or resistive heating to ~800-1000°C over 24-48 hours. This dries the lining and prevents thermal shock cracking of carbon refractory. Then charge raw materials, lower electrodes, strike arc, and gradually increase power over 6-12 hours to full load. Full production reached in 24-72 hours.
- **Hot restart** (after brief interruption <4 hours): Electrodes still hot, lining warm. Re-strike arc and ramp power over 2-4 hours.
- **Planned shutdown**: Reduce power gradually over 4-8 hours. Raise electrodes. Seal furnace to retain heat. A well-sealed furnace retains >500°C for 24+ hours, enabling easier restart.
- **Emergency shutdown**: Cut power immediately. Raise electrodes. Risk: molten silicon freezes in taphole, requiring drilling or oxygen lancing to clear. Keep taphole open during emergency drain if possible.

**Strengths**:
- Hot restart possible within 4 hours of interruption — furnace lining retains enough heat to re-strike arc quickly
- Well-sealed furnace retains >500°C for 24+ hours, providing a wide window for planned restart

**Weaknesses**:
- Cold startup takes 24-72 hours to reach full production — a significant productivity loss
- Emergency shutdown often requires oxygen lancing to clear frozen taphole, adding hazard and downtime

## Raw Material Preparation

**Quartz processing**:
- **Source**: High-purity quartzite or vein quartz with SiO₂ content >98%. Lower purity quartz introduces more Fe, Al, and Ca into the silicon product, increasing downstream refining burden.
- **Crushing**: Jaw crusher reduces quarry rock to 50-150 mm lumps. Secondary cone crusher or hammer mill to 10-50 mm. Screening separates oversized material for re-crushing. Target size distribution: 10-100 mm lumps. Fines (<5 mm) are problematic because they reduce charge permeability, blocking gas escape and causing irregular furnace operation.
- **Washing**: Water wash removes clay and surface contamination. Reduce surface impurities (especially iron from crushing equipment) that do not originate from the quartz itself.
- **Storage**: Covered storage to keep quartz dry. Wet quartz causes steam explosions in the furnace.

**Carbon reductant preparation**:
- **Petroleum coke**: Primary reductant. Fixed carbon >95%, low ash (<1%), low volatile matter. Crushed to 5-30 mm. Low impurity content makes it preferable for silicon destined for semiconductor-grade purification.
- **Coal**: Bituminous coal with low ash (<8%) and low sulfur. Higher ash introduces more impurities (Fe, Al, Ca) into the silicon. Crushed to 5-30 mm.
- **Wood chips**: 10-50 mm chips from hardwood or softwood. Not primarily a reductant but a charge porosity agent. Provides channels for CO and SiO gas to escape the charge column. Typically 10-20% of total carbon in the charge mix. Also introduces some silica from bark/ash.
- **Mixing ratio**: Approximately 2:1 SiO₂:C by weight (stoichiometric is ~2.5:1 for SiO₂ + 2C → Si + 2CO, but excess carbon compensates for losses and incomplete reaction). The actual ratio is tuned to furnace conditions: too much carbon produces SiC (silicon carbide) crusts; too little leaves unreacted SiO₂.

**Strengths**:
- Wood chips serve dual purpose — porosity agent and partial reductant — reducing the need for expensive petroleum coke
- Simple washing and screening of quartz removes surface contamination that would otherwise enter the silicon product

**Weaknesses**:
- Fines (<5 mm) from quartz crushing reduce charge permeability and must be screened out, wasting 5-15% of crushed quartz
- Moisture in stored quartz causes steam explosions in the furnace, requiring covered storage in all weather

## Furnace Operation Detail

**Submerged arc furnace**:
- **Electrical system**: 3-phase AC power supply. Each of three electrodes carries one phase. Current passes from electrode through the charge material (which acts as resistance) to the reaction zone. Voltage between electrodes: 100-250V. Current per electrode: 20,000-100,000 A. Total power: 10,000-30,000 kVA for a medium furnace.
- **Electrode positioning**: Hydraulic hoists adjust electrode height continuously to maintain optimal electrical conditions. If electrode is too high, arc lengthens and voltage rises. If too low, electrode dips into the molten pool, causing short circuit. Automatic regulators maintain constant current by adjusting electrode position in real time.
- **Electrode consumption**: 80-120 kg per tonne of silicon produced. Electrodes burn away at the tip (oxidation and sublimation of carbon in the reaction zone at >1800°C). New electrode sections are added at the top (Søderberg paste or threaded prebaked joints).
- **Temperature profile**: Charge surface ~500-800°C. Mid-charge ~1200-1600°C. Reaction zone at electrode tips ~1700-2000°C. Tapping zone ~1550-1650°C. The gradient from surface to reaction zone spans >1000°C over ~2 m.

**Tapping operation**:
- **Frequency**: Every 1-2 hours from each taphole. A furnace with two tapholes alternates between them.
- **Procedure**: Open taphole by drilling or burning through the clay/carbon plug that sealed it after the previous tap. Molten silicon (density 2.33 g/cm³) flows out under gravity into a refractory-lined cast iron ladle. Silicon temperature at tap: ~1550-1650°C.
- **Slag tapping**: Slag (density ~2.5-3.0 g/cm³, but often lighter due to gas bubbles) may be tapped from a higher taphole before silicon tapping. Some operations tap slag and silicon sequentially from the same hole.
- **Taphole maintenance**: After tapping, plug the hole with clay or carbon paste. The taphole refractory lining erodes over time and must be re-lined periodically (every few weeks to months).

**Strengths**:
- Hydraulic electrode positioning with automatic current regulation maintains stable arc conditions without constant operator intervention
- Temperature gradient from surface to reaction zone spans >1000°C over ~2 m, naturally separating reaction zones from charge handling

**Weaknesses**:
- Electrode consumption of 80-120 kg/t Si requires continuous section addition — any interruption in electrode supply halts the furnace
- Taphole refractory erosion necessitates re-lining every few weeks, requiring planned maintenance shutdowns

## MG-Si Refining

**Gas blowing** (post-tap refining in the ladle):
- **Purpose**: Reduce impurity levels in tapped MG-Si from ~95-97% to 97-99% before casting.
- **Air blowing**: Blow compressed air through a submerged lance into the molten silicon. Oxygen preferentially reacts with Al and Ca, forming Al₂O₃ and CaO that float to the surface as slag skimmed off. Removes 50-70% of aluminum and 60-80% of calcium. Also removes some iron as iron silicide slag.
- **Oxygen blowing**: More aggressive than air. Faster impurity removal but higher silicon oxidation losses (some Si forms SiO₂ slag). Used when raw silicon has high impurity levels.
- **Chlorine blowing**: Pass Cl₂ gas through molten silicon. Chlorine reacts with Al, Ca, and Ti to form volatile chlorides (AlCl₃ boils at 180°C, CaCl₂ melts at 772°C). Extremely effective but produces toxic gas (HCl, Cl₂) requiring scrubbing. Used only when downstream purification demands lower starting impurity levels.
- **Result**: Refined MG-Si at 97-99% purity, typically 98-98.5%. Major remaining impurities: Fe (0.3-0.8%), Al (0.1-0.4%), Ca (0.05-0.2%), and trace Ti, Mn, B, P.

**Strengths**:
- Gas blowing reduces Al by 50-70% and Ca by 60-80% in a single ladle treatment — fast, low-cost upgrade
- Chlorine blowing is extremely effective for Ti and trace metal removal when downstream purity demands it

**Weaknesses**:
- Chlorine blowing produces toxic HCl and Cl₂ gas requiring wet scrubbing — adds complexity and hazard
- Oxygen blowing oxidizes some silicon along with impurities, reducing yield by 2-5%

## Production Scale and Economics

**Furnace sizes**:
- **Small (5-10 MVA)**: Produces 2,000-4,000 tonnes MG-Si per year. Suitable for bootstrap-scale operations. Can be built with moderate industrial capability. Power consumption: 5-10 MW continuous.
- **Medium (15-25 MVA)**: Produces 6,000-12,000 tonnes/year. The most common size in the industry. Requires dedicated power supply (10-20 MW).
- **Large (30+ MVA)**: Produces 12,000-20,000+ tonnes/year. Economies of scale but requires very large power infrastructure. Modern plants cluster multiple furnaces at a single site near cheap hydroelectric or geothermal power.

**Energy intensity**:
- **Specific consumption**: 11-15 kWh per kg of MG-Si produced. This is the major cost component, representing 20-25% of total production cost. A furnace producing 10 tonnes/day consumes 110,000-150,000 kWh/day, equivalent to the power consumption of a small town.
- **Power supply**: Silicon furnaces run 24/7/365. Interruptions cause the charge to freeze, requiring expensive and time-consuming restart. Firm, continuous power supply is a siting requirement. Locations near hydroelectric dams are preferred (cheap baseload power). Solar or wind alone cannot provide the reliability needed without massive battery storage.
- **Energy recovery**: CO off-gas combustion can recover 30-40% of electrical input as thermal energy (steam generation, co-generation). This improves overall plant efficiency but adds complexity.

**Strengths**:
- Hydroelectric power siting gives near-zero marginal electricity cost, making MG-Si competitive at $1.50-2.50/kg
- CO energy recovery offsets 30-40% of furnace electricity, improving plant economics

**Weaknesses**:
- 11-15 kWh/kg energy intensity means a 10 t/day furnace draws 110-150 MWh/day — requiring dedicated power infrastructure
- 24/7/365 operation with no tolerance for interruptions excludes solar/wind without massive battery storage

## Safety Hazards

Operating a submerged arc furnace for silicon production involves severe hazards:
- **CO gas poisoning**: Carbon monoxide is colorless, odorless, and lethal at 0.1% concentration in air for 1 hour. Off-gas system leaks are the primary risk. Fixed CO detectors with audible alarms mandatory in furnace building. Personnel must evacuate at >50 ppm. Never enter furnace hood area without supplied-air respirator during operation.
- **Molten silicon**: Pours at ~1450-1600°C. Contact causes immediate deep burns. Molten silicon on wet surfaces or water causes steam explosion — catastrophic ejection of molten metal. All molds, ladles, and tools must be thoroughly pre-dried. No water in tapping area. Pouring ladle must be lined with dry refractory.
- **Arc flash**: 20,000-100,000 A at 100-250V. Electrode adjustment system failure can cause short circuit with explosive energy release. Arc flash boundary: 2-5 m minimum. Flame-resistant clothing, face shield, insulating gloves required near electrode hoists.
- **Silica dust inhalation**: Quartz handling (crushing, loading) generates respirable crystalline SiO₂ dust. Causes silicosis (irreversible lung scarring) after years of exposure. Dust suppression: wet crushing, enclosed conveyor systems, local exhaust ventilation. Respirator (P100) required in dusty areas.
- **Burns from hot surfaces**: Furnace shell, electrode columns, and tap ladles are 200-600°C on exterior. Thermal gloves (rated to 500°C minimum) and face protection for all tapping operations. Mark hot zones with barricades.
- **Cooling water hazard**: Furnace components (electrode clamps, shell panels) are water-cooled. A cooling water leak into the furnace causes immediate steam explosion. Monitor cooling water flow and temperature continuously. Automatic shutdown on flow loss.

## Environmental Management

**Air emissions control**:
- **Particulate matter**: Baghouse filters (fabric filter bags, 2-5 m long, in a steel housing) capture SiO₂ fume and dust at >99.5% efficiency. Filter bags made of woven fiberglass or PTFE felt, rated for continuous operation at 200-260°C. Gas enters the baghouse, particles deposit on the outside of the bags, clean gas exits through the bag interior. Bags cleaned periodically by reverse air pulse or mechanical shaking. Captured silica fume collected in sealed hoppers for sale or disposal.
- **CO management**: Furnace off-gas contains 70-90% CO by volume. CO must be either flared (burned to CO₂ in an elevated flare stack with continuous pilot light) or recovered as fuel gas. CO recovery requires gas cleaning (remove dust, cool to ambient, compress) before use in boilers or gas turbines. CO has a heating value of ~10 MJ/m³, roughly one-third of natural gas.
- **SO₂ emissions**: If coal or petroleum coke contains sulfur, SO₂ appears in the off-gas. Control: use low-sulfur reductants (<1% sulfur), or install wet scrubbing (limestone slurry absorbs SO₂, producing CaSO₃/CaSO₄ waste).

**Solid waste management**:
- **Slag**: 200-400 kg per tonne of silicon. Non-hazardous if heavy metals are below regulatory limits. Can be crushed and used as construction aggregate, road base, or cement additive. Test for leachable heavy metals before any land application.
- **Refractory waste**: Carbon refractory lining replaced every 2-5 years. Spent refractory may contain silicon carbide and metal silicides. Can be recycled as partial charge material or disposed as industrial waste.
- **Silica fume**: 200-400 kg per tonne of silicon. When collected, it is a valuable pozzolanic additive for high-strength concrete (reacts with calcium hydroxide in cement, improving strength and durability). Particle size: 0.1-0.5 μm (100× finer than cement). Market value offsets collection costs.

**Strengths**:
- Baghouse filtration achieves >99.5% particulate capture, meeting stringent air quality regulations
- Silica fume byproduct generates $200-600/tonne revenue, partially offseting operating costs

**Weaknesses**:
- CO recovery requires gas cleaning and compression before combustion — adds capital cost and maintenance
- Baghouse filter bags (fiberglass/PTFE) require replacement every 2-5 years at significant cost

## Quality Control in MG-Si Production

**Chemical analysis**:
- **X-ray fluorescence (XRF)**: Non-destructive technique that measures elemental composition of solid samples. X-rays excite inner-shell electrons in the sample; emitted characteristic X-rays identify and quantify each element. Measures all elements heavier than sodium simultaneously. Accuracy: ±0.1-1% for major elements (Si, Fe, Al, Ca). Analysis time: 5-15 minutes per sample. No sample dissolution required.
- **Spark optical emission spectroscopy (Spark OES)**: Electric spark vaporizes a small area of the solid silicon sample. Emitted light is dispersed by a grating spectrometer, and the intensity of characteristic wavelengths quantifies each element. Measures: Si, Fe, Al, Ca, Ti, Mn, Cr, Ni, Cu, V, and others. Accuracy: ±0.01% for trace elements. Faster than XRF for trace metals. Requires calibration with certified reference standards.
- **Sampling procedure**: Take drill cores or grab samples from at least 5 locations across each cast ingot (silicon composition varies from top to bottom and center to edge due to segregation during solidification). Composite the analyses for a representative result. Sample weight: 50-200 g per location, crushed and split to a representative sub-sample for analysis.

**Acceptance criteria for MG-Si**:
- **Grade 553**: Si ≥98.5%, Fe ≤0.5%, Al ≤0.5%, Ca ≤0.3%. The most common commercial grade. Used for aluminum alloying and silicone production.
- **Grade 441**: Si ≥99.0%, Fe ≤0.4%, Al ≤0.4%, Ca ≤0.1%. Higher purity, used for chemical silicon applications.
- **Solar grade feedstock**: Si ≥98.5%, B ≤30 ppm, P ≤40 ppm. Boron and phosphorus limits are critical because these elements are electrically active in silicon and difficult to remove by physical refining.

**Strengths**:
- XRF provides non-destructive multi-element analysis in 5-15 minutes with no sample dissolution — fast turnaround for process control
- Spark OES achieves ±0.01% accuracy for trace metals, sufficient for grading MG-Si into commercial specifications

**Weaknesses**:
- Segregation during solidification means a single grab sample is not representative — requires 5+ locations per ingot
- Both XRF and Spark OES require certified reference standards for calibration, adding a supply chain dependency

## Furnace Design Variants

**Single-phase vs. three-phase**:
- **Three-phase furnace**: Three electrodes arranged in a triangle (delta configuration). Most common design for medium and large furnaces. Balanced three-phase load on the power supply. Current paths between electrode pairs create three independent reaction zones that merge in the center of the furnace bed.
- **Single-phase (two-electrode) furnace**: Two electrodes, used for smaller furnaces (2-5 MVA). Simpler power supply but unbalanced load on the electrical grid. Electrodes can be arranged with one above the other (vertical) or side by side (horizontal current path through the charge). Less common in modern practice.

**Electrode types in detail**:
- **Prebaked graphite electrodes**: Manufactured from petroleum coke, coal tar pitch, and graphite. Process: Mix coke and pitch → extrude into cylinders → bake at 800-1200°C to carbonize the pitch binder → graphitize at 2500-3000°C (transforms amorphous carbon to crystalline graphite). The graphitization step requires enormous energy (~3-5 kWh/kg electrode) and a dedicated graphitization furnace (Acheson or LWG type). Diameter range: 200-800 mm. Length: 1.5-3 m per section. Sections joined by threaded nipples (carbon nipples screwed into both sections). Electrical resistivity: 5-10 μΩ·m. Current carrying capacity: 15-35 A/cm².
- **Søderberg self-baking electrodes**: Steel casing (1.5-2 mm thick steel sheet) filled with carbon paste (calcined petroleum coke + coal tar pitch, ~75:25 ratio). The paste is a soft, tarry mass at room temperature. As the electrode descends into the furnace hot zone, the heat bakes the paste progressively: ~200°C → paste softens, ~500°C → pitch volatiles escape (smoke), ~800-1000°C → pitch carbonizes and binds the coke particles into a solid carbon electrode, >1200°C → partial graphitization. Advantages: continuous electrode (add paste at the top, never stop to change electrode sections), lower cost than prebaked. Disadvantages: less consistent quality, higher impurity content (iron from casing, ash from pitch), smoke and volatile emissions during baking.

**Strengths**:
- Three-phase design provides balanced electrical load and three merged reaction zones for higher throughput
- Søderberg electrodes eliminate the need for off-site graphitization, reducing bootstrapping complexity

**Weaknesses**:
- Prebaked electrodes require a dedicated graphitization furnace at 2500-3000°C (~3-5 kWh/kg) — a significant energy investment
- Single-phase furnaces create unbalanced grid loads, limiting their use to smaller installations

## Silicon Carbide (SiC) Formation

An inevitable side reaction in the silicon furnace:
- SiO₂ + 3C → SiC + 2CO (at 1500-1800°C)
- SiC is extremely hard (Mohs 9.5) and chemically inert. It does not melt at furnace temperatures but sublimes above 2700°C. Excess SiC forms crusts that block gas flow and reduce silicon yield.
- SiC also forms from the reverse reaction: SiO gas + C → SiC + CO. This occurs in the cooler upper regions of the charge column where SiO vapor contacts carbon particles.
- Management: Maintain correct SiO₂:C ratio (excess carbon promotes SiC). Control charge permeability (SiC crusts block gas escape, requiring the furnace to be "poked" with steel bars to break up crusts). Accept that some SiC formation is inevitable and manage its effects through furnace operation practices.

**Strengths**:
- SiC crusts can be broken up mechanically ("poking") without shutting down the furnace
- Small amounts of SiC in the charge bed act as a conductive medium that helps maintain stable arc conditions

**Weaknesses**:
- SiC crusts reduce gas permeability, forcing operators to manually poke the charge — a hazardous operation near 500-800°C charge surface
- SiC formation consumes both silicon and carbon without producing salable product, directly reducing yield

## Silicon Casting and Solidification

**Ingot casting**:
- **Mold preparation**: Cast iron or steel molds, preheated to 200-400°C to prevent thermal shock. Coat mold interior with a refractory wash (SiC or Si₃N₄-based) to prevent iron contamination of the silicon and to ease ingot release. The coating must be dry before pouring (residual moisture causes steam explosions).
- **Pouring**: Liquid silicon from the taphole flows into the mold via a refractory-lined launder (channel). Pour temperature: ~1550-1650°C. Pour rate controlled to avoid splashing and turbulence (turbulent flow traps gas bubbles in the solidifying silicon). Fill the mold steadily without interruption.
- **Solidification**: Silicon contracts ~10% by volume on solidification (unusual: most metals contract only a few percent). This causes significant shrinkage pipes (cavities) at the top of the ingot. Allow ingot to cool in the mold for 12-24 hours before knockout (removal from mold). The ingot surface is rough and contaminated with mold coating material.

**Ingot crushing and sizing**:
- **Primary crushing**: Break ingot into 100-300 mm chunks with a hydraulic hammer or drop ball (heavy steel ball dropped from a crane onto the ingot). Primary crushing must overcome silicon's hardness (Mohs 7, similar to quartz) and its brittleness (fractures conchoidally).
- **Secondary crushing**: Jaw crusher reduces chunks to 10-50 mm lumps. Jaw crusher gap adjusted to control output size. The crusher liners must be hardened steel or manganese steel (silicon is abrasive). Liner wear introduces iron contamination (~0.01-0.05% Fe from crusher wear per pass). Use magnetic separation after crushing to remove steel fragments.
- **Fine grinding** (for chemical purification feed): Ball mill or hammer mill to 100-500 μm powder. Ball mill: rotating cylinder containing steel or ceramic balls and silicon chunks. Tumbling action grinds silicon between the balls. Grinding media wear is a significant contamination source. Alumina (Al₂O₃) ceramic grinding media reduces iron contamination compared to steel balls. Mill for 2-8 hours depending on target particle size. Screen to remove oversize material and recycle to the mill.

**Particle size classification**:
- **Sieve analysis**: Stack of graduated sieves (10 mm, 5 mm, 2 mm, 1 mm, 500 μm, 250 μm, 125 μm, 75 μm) on a mechanical shaker. Load sample on the top sieve, shake for 15-30 minutes. Weigh the material retained on each sieve. Plot particle size distribution (cumulative percent passing vs. sieve size). Target: >90% of material in the 1-10 cm range for furnace charge, 100-500 μm for chemical purification.
- **Air classification**: For fine powders (<100 μm), use an air classifier (centrifugal separator that separates particles by terminal velocity in an air stream). Lighter particles are carried upward by the air flow; heavier particles fall out. Adjustable cutoff size by varying air velocity. Used to remove fines (<50 μm) from the furnace charge (fines reduce permeability) and to produce uniform powder for the Siemens process.

**Strengths**:
- Air classification produces uniform particle size distributions without screens or sieves — no mesh wear or blinding
- Sieve analysis provides direct, visual particle size distribution data usable for process tuning

**Weaknesses**:
- Ball milling with steel media introduces iron contamination (~0.01-0.05% Fe per pass), requiring magnetic separation
- Silicon's 10% volume contraction on solidification causes shrinkage cavities that reduce usable ingot yield

## Energy Balance and Sustainability

**Energy accounting for the silicon production chain**:
- MG-Si production: 11-15 kWh/kg (submerged arc furnace, electricity)
- Crushing and sizing: 0.5-1.0 kWh/kg (jaw crusher, ball mill)
- Total MG-Si gate energy: ~12-16 kWh/kg

**Silicon as an energy carrier**: The energy invested in producing MG-Si is recovered many times over when the silicon is converted into solar cells. A silicon solar cell (15% efficiency, 25-year lifetime) generates approximately 3-5 kWh per gram of silicon over its lifetime. The energy payback time for the entire silicon-to-solar-cell chain is 1-3 years, after which the solar cell produces net energy for 22-24 years. This positive energy return is what makes the bootstrap chain viable.

**Carbon footprint**: MG-Si production emits CO₂ from two sources: (1) the carbothermic reduction reaction itself (SiO₂ + 2C → Si + 2CO, and the CO is later burned to CO₂), producing ~3.5 tonnes CO₂ per tonne Si; and (2) electricity generation for the furnace, producing 0-5 tonnes CO₂ per tonne Si depending on the power source (0 for hydroelectric, ~5 for coal-fired electricity). Using hydroelectric power and recycling the CO gas for energy recovery reduces the total carbon footprint to ~4 tonnes CO₂ per tonne MG-Si.

**Strengths**:
- Solar cells generate 3-5 kWh/g over 25 years — energy payback time of 1-3 years for the full silicon-to-solar chain
- Hydroelectric siting reduces carbon footprint to ~4 t CO₂/t MG-Si, competitive with other bulk metals

**Weaknesses**:
- Total MG-Si gate energy of 12-16 kWh/kg makes silicon one of the most energy-intensive bulk materials produced
- CO₂ emissions of 3.5-8.5 t/t Si (depending on power source) are significant without renewable electricity

## Silicon Dust Handling

**Dust explosion hazard**: Silicon powder finer than 100 μm is a combustible dust. When suspended in air at concentrations above ~100 g/m³, it can ignite and explode. The minimum ignition energy is ~100 mJ (low enough for static discharge). Kst value (dust explosion class): ~100-200 bar·m/s (St class 1, moderate explosion hazard). Prevention: enclose crushing and milling equipment, collect dust at source with local exhaust ventilation, use explosion-proof electrical equipment in dusty areas, ground all equipment to prevent static buildup, and store fine powder in sealed containers away from ignition sources.

**Silica exposure**: Silicon metal dust (crystalline Si) is less hazardous than pure SiO₂ dust (quartz) for silicosis risk, but SiO₂ contamination from quartz raw material is always present. Occupational exposure limits: 0.025 mg/m³ respirable crystalline silica (8-hour TWA). Achievable only with enclosed, ventilated equipment and respiratory protection. Health monitoring: chest X-ray and lung function testing every 1-3 years for workers with regular silica dust exposure.

**Bootstrap scaling considerations**: A minimal silicon production facility for bootstrapping semiconductor capability starts with a single 5 MWA furnace producing ~2,000 tonnes MG-Si per year. This provides enough silicon to feed a small polysilicon plant (producing ~500 tonnes/year of semiconductor-grade polysilicon), which feeds a CZ crystal puller producing ~200 tonnes/year of single crystal ingots. The entire chain, from quartz mine to finished wafers, requires approximately 50-100 MW of dedicated electrical power. The facility should be sited near hydroelectric or geothermal power to ensure continuous, low-cost electricity. Every kilogram of silicon that goes into solar cells generates 3-5 kWh per year of electricity, creating the positive feedback loop that drives exponential capacity growth in the bootstrap chain.

**Strengths**:
- 5 MVA bootstrap furnace feeds the entire silicon-to-semiconductor chain with only ~5 MW continuous power
- Positive energy feedback: each kg of silicon in solar cells generates 3-5 kWh/year for 25 years

**Weaknesses**:
- Full chain (quarry to wafers) requires 50-100 MW — a major infrastructure commitment before any semiconductor output
- Silicon powder finer than 100 μm is a combustible dust (Kst 100-200 bar·m/s) requiring explosion-proof equipment

## Casting Practice and Powder Production

**Standard casting parameters**: Cast iron molds preheated to 200-300°C prevent thermal cracking of the ingot surface. Typical ingot size for chemical-grade production: 5-50 kg. Cooling time before demolding: 2-4 hours for standard ingots. Larger ingots (>100 kg, used for aluminum alloying or direct sales) require controlled cooling at 50-100°C/hour through the 1414°C solidification point to prevent internal stress cracking from silicon's unusually high volume contraction (~10%) on solidification. Without controlled cooling, large ingots develop radial cracks that render portions unusable for chemical processing.

**Powder production for chemical use**: Jaw crush primary ingot chunks to <50 mm, then ball mill with alumina grinding media to <1 mm. Air classify to target size distribution: the classifier's adjustable rotor speed sets the cutoff between fines and product. Typical chemical-grade silicon powder: 0.1-5 mm particle size, bulk density 1.0-1.5 g/cm³. Finer powder (<150 µm) feeds the Siemens process and fluidized bed reactors; coarser grades (1-10 mm) charge directly into submerged arc furnaces for re-melting or go to aluminum alloying customers.

**Strengths**:
- Alumina grinding media minimizes iron contamination compared to steel balls — critical for chemical-grade feedstock
- Air classification provides continuous, adjustable particle size control without screen blinding issues

**Weaknesses**:
- Controlled cooling of large ingots at 50-100°C/hour extends casting cycle time significantly
- Ball milling is energy-intensive at 0.5-1.0 kWh/kg, adding to the already high energy cost of the silicon chain


[← Back to Silicon](index.md)
