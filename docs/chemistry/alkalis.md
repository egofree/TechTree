# Alkali Production

> **Node ID**: chemistry.alkalis
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`mining.processing`](../mining/processing.md)
> **Enables**: [`chemistry.explosives`](explosives.md), [`chemistry.pulp-chemicals`](pulp-chemicals.md), [`chemistry.soap`](soap.md), [`metals.aluminum`](../metals/aluminum.md), [`textiles.finishing`](../textiles/finishing.md)
> **Timeline**: Years 20-35
> **Outputs**: soda_ash, caustic_soda, sodium_carbonate
> **Critical**: Yes — soda ash (Na₂CO₃) and caustic soda (NaOH) are essential for glass manufacturing, soap production, paper pulping, and aluminum extraction. The Solvay process is one of the foundational chemical industries.

### Alkali Production

**[Leblanc process](../glossary/leblanc-process.md)** (first synthetic soda ash):
- **Step 1**: NaCl + H₂SO₄ → NaHSO₄ + HCl (salt cake furnace, 150-200°C, then 550-600°C for complete reaction to Na₂SO₄). HCl byproduct captured as hydrochloric acid.
- **Step 2**: Na₂SO₄ + 2C (coke/charcoal) + CaCO₃ (limestone) → Na₂CO₃ + CaS + 2CO₂. Black ash furnace, 900-1000°C. Mix and roast for 1-2 hours.
- **Step 3**: Leach black ash with water. Na₂CO₃ dissolves. CaS and impurities remain as residue. Crystallize Na₂CO₃ (soda ash) from solution by evaporation.
- **Pollution**: CaS waste (4 tonnes per tonne Na₂CO₃) creates H₂S (rotten egg gas) when exposed to rain. Major environmental problem historically. Oxidize with air to convert to CaSO₄ (gypsum — useful building material).

**Strengths**: First synthetic route to soda ash from salt (1791); produces HCl as valuable co-product; no ammonia required — suitable for early bootstrapping; well-understood batch chemistry.

**Weaknesses**: Massive CaS waste (4 t per t Na₂CO₃) releasing toxic H₂S; energy-intensive (multiple furnace stages at 150-1000°C); historically caused severe environmental damage; completely displaced by Solvay wherever ammonia is available.

**[Solvay process](../glossary/solvay-process.md)** (more efficient, later):
- **Principle**: NaCl + NH₃ + CO₂ + H₂O → NaHCO₃ (precipitates) + NH₄Cl. Heat NaHCO₃ → Na₂CO₃ + CO₂ + H₂O. Recycle NH₃ and CO₂.
- **Ammonia recovery**: Heat NH₄Cl with Ca(OH)₂ (slaked lime) → NH₃ + CaCl₂ + H₂O. Calcium chloride is waste product.
- **CO₂ source**: Heat limestone (CaCO₃ → CaO + CO₂) in lime kiln. CaO used for ammonia recovery.
- **Advantages over Leblanc**: Less waste, lower energy, continuous process. But requires ammonia (from coal distillation or Haber-Bosch).
- **Throughput**: 100-1000+ tonnes/day in mature plants.

**Strengths**: Continuous process with low operating costs; ammonia efficiently recycled (1-2 kg makeup per tonne Na₂CO₃); much less waste and pollution than Leblanc; scalable to 3,000 tonnes/day.

**Weaknesses**: Requires ammonia supply (from Haber-Bosch or coke ovens); CaCl₂ waste (~10 t per t Na₂CO₃) causes salinity in waterways; capital-intensive (carbonation towers, calciner, ammonia still); NaCl conversion limited to ~72-75%.

**Caustic soda (NaOH)**:
- **Lime-soda process**: Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃ (precipitates). Filter, evaporate to 50% NaOH solution. Simple but produces CaCO₃ sludge.
- **[Electrolysis of brine](../glossary/electrolysis-of-brine.md)** (preferred): See [Electrolysis](electrolysis.md). Produces Cl₂ + H₂ + NaOH simultaneously. Most efficient route.

**Strengths (lime-soda)**: No electricity required; simple equipment (tank + filter + evaporator); CaCO₃ can be reburned to close the lime loop; works with Solvay/Leblanc soda ash.

**Weaknesses (lime-soda)**: Only 85-92% conversion; high steam consumption (2-3 t/t NaOH); CaCO₃ sludge handling; max 50% NaOH without nickel-clad equipment.

**Strengths (electrolytic)**: Highest purity NaOH; co-produces valuable Cl₂ and H₂; most economical at large scale.

**Weaknesses (electrolytic)**: Requires reliable electricity (2,100-2,500 kWh/t Cl₂); Cl₂/NaOH demand ratio is fixed; high capital cost for cell rooms.

**Potash (K₂CO₃) — pre-industrial alkali**:
- **Source**: Plant ashes, especially hardwood (oak, beech, maple). Land plants concentrate potassium from soil.
- **Process**: Leach wood ash with water → dissolve K₂CO₃ (sodium and calcium salts are less soluble). Filter through cloth or sand bed. Evaporate filtrate in iron or clay pots → crude potash (brown, 50-70% K₂CO₃). Calcine (heat to 800-900°C) to burn off organic impurities → pearl ash (white, 80-95% K₂CO₃).
- **Yield**: 5-10% of dry wood weight. One hectare of forest yields ~1-2 tonnes potash. Very land-intensive.
- **Uses**: Glass making (K₂CO₃ lowers melting point of silica), soap (potash + fat → soft soap), fertilizer (potassium source).

**Strengths**: Available from wood ashes with Stone Age technology; no industrial infrastructure needed; co-produces soft soap (potassium-based); potassium is essential for plant growth (fertilizer).

**Weaknesses**: Extremely land-intensive (1-2 t/ha, decades regrowth); low yield (5-10% of wood weight); impure product (50-70% K₂CO₃ before calcination); cannot scale to industrial volumes; deforestation pressure.

**Baking soda (NaHCO₃) via Solvay intermediates**:
- The Solvay process precipitates NaHCO₃ before thermal decomposition. Divert this intermediate: NaCl + NH₃ + CO₂ + H₂O → NaHCO₃↓ + NH₄Cl. Filter, wash, dry at low temperature (<50°C to prevent decomposition). Food-grade NaHCO₃ requires additional purification.
- **Thermal decomposition**: Heat NaHCO₃ to 80-100°C → Na₂CO₃ + CO₂ + H₂O. This is the route to soda ash from baking soda. Both directions are useful depending on which product is needed.

### Solvay Process — Detailed Step-by-Step

The Solvay (ammonia-soda) process produces sodium carbonate (Na₂CO₃, soda ash) from salt (NaCl) and limestone (CaCO₃), with ammonia (NH₃) as a recyclable intermediate. It displaced the Leblanc process in the late 19th century due to lower cost and pollution:

**Step 1: Ammonia absorption in brine**
- Saturated brine (NaCl solution, ~300 g/L at 20°C) flows down through an absorption tower countercurrent to rising NH₃ gas. The brine absorbs ammonia exothermically (ΔH = -35 kJ/mol), forming ammoniated brine (NaCl + NH₃ in solution).
- Cooling is necessary — the absorption tower uses water jackets or internal cooling coils to keep temperature below 30°C. Higher temperature reduces NH₃ solubility and shifts equilibrium against carbonation.
- The ammoniated brine also absorbs some CO₂ from the ammonia recovery section (see Step 5), forming small amounts of ammonium carbonate ((NH₄)₂CO₃). This is acceptable — it decomposes in the next step.

**Step 2: Carbonation — NaHCO₃ precipitation**
- CO₂ gas (from lime kiln, ~35-40% CO₂) is bubbled up through the ammoniated brine in a carbonation tower (series of bubble-cap trays or packed sections).
- **Reaction**: NH₃ + CO₂ + NaCl + H₂O → NaHCO₃↓ + NH₄Cl
- Sodium bicarbonate (NaHCO₃) precipitates because it has low solubility in the concentrated brine at the process temperature (15-20°C is optimal — higher temperature increases NaHCO₃ solubility, reducing yield).
- Carbonation proceeds in two stages: First pass with weaker CO₂ (from the calciner, ~70% CO₂), then a second pass with kiln CO₂. Total residence time: 1.5-3 hours.
- NaCl conversion efficiency: ~72-75%. The remaining NaCl stays in solution and is recycled with the mother liquor.

**Step 3: Filtration**
- The NaHCO₃ slurry from the carbonation tower is filtered on rotary vacuum filters or centrifuges. The filter cake is crude NaHCO₃ (contains ~15% moisture, plus traces of NH₄Cl and NaCl).
- Wash with cold water to remove adhering mother liquor (which contains NH₄Cl — too valuable to waste). Wash water joins the mother liquor for ammonia recovery.
- Mother liquor (filtrate) contains: NH₄Cl, unreacted NaCl, some (NH₄)₂CO₃. This is the feed for ammonia recovery (Step 5).

**Step 4: Calcination (thermal decomposition)**
- Wet NaHCO₃ cake is heated in a rotary kiln or fluidized-bed calciner at 160-230°C.
- **Reaction**: 2NaHCO₃ → Na₂CO₃ + CO₂↑ + H₂O↑
- The CO₂ and steam driven off are recovered — CO₂ is recycled to the carbonation tower (it's concentrated, ~90%+ CO₂ after condensing out water vapor). Heat recovery: hot flue gases from the calciner furnace preheat incoming NaHCO₃.
- Product: light soda ash (Na₂CO₃, density ~500 kg/m³) or dense soda ash (if the light ash is further processed by rehydration and recalcination to increase bulk density to ~1000 kg/m³ for easier shipping).

**Step 5: Ammonia recovery (the key to process economics)**
- Mother liquor from filtration is mixed with slaked lime (Ca(OH)₂) in a distillation column (ammonia still).
- **Reaction**: 2NH₄Cl + Ca(OH)₂ → 2NH₃↑ + CaCl₂ + 2H₂O
- Steam strips NH₃ from the solution. Recovered NH₃ gas is recycled to Step 1 (ammonia absorption). NH₃ makeup requirement: ~1-2 kg per tonne Na₂CO₃ (small losses from the closed loop).
- **Ca(OH)₂ source**: Limestone (CaCO₃) is calcined in a lime kiln: CaCO₃ → CaO + CO₂. The CaO is slaked with water: CaO + H₂O → Ca(OH)₂. The CO₂ from the lime kiln is the CO₂ source for Step 2.
- **Waste**: Calcium chloride (CaCl₂) solution is the main waste stream — ~10 tonnes of CaCl₂ per tonne of Na₂CO₃. Uses for CaCl₂: de-icing, dust control, concrete additive. Historically discharged to waterways (causes salinity problems).

**[Raw materials balance](../glossary/raw-materials-balance.md)** (per tonne Na₂CO₃ produced):
- NaCl: ~1.5 tonnes (at 72% conversion efficiency)
- CaCO₃ (limestone): ~1.2 tonnes
- Coke/coal (for lime kiln): ~0.1 tonnes
- Steam: ~1.5 tonnes
- NH₃ makeup: ~1-2 kg
- Energy: ~7-10 GJ/tonne Na₂CO₃

**Strengths (Solvay detailed)**: Near-complete ammonia recycle (only 1-2 kg makeup per tonne); CO₂ also recycled from calciner and lime kiln; well-established continuous process operable by medium-skilled workforce; 100-3000 tonnes/day throughput.

**Weaknesses (Solvay detailed)**: CaCl₂ waste (10 t per t Na₂CO₃) with limited market; NaCl conversion limited to 72-75% — remainder recycled but increases brine handling; carbonation tower temperature must be precisely controlled (15-20°C optimal); requires parallel lime kiln and ammonia still operations.

### Leblanc Process — Detailed Steps

The Leblanc process was the first industrial method for producing soda ash from salt (patented 1791). It is more polluting and less efficient than Solvay but requires no ammonia, making it potentially relevant for bootstrapping:

- **Step 1 (Salt cake)**: NaCl + H₂SO₄ → NaHSO₄ + HCl (150-200°C), then NaHSO₄ + NaCl → Na₂SO₄ + HCl (550-600°C). Product: sodium sulfate (salt cake). HCl gas captured as hydrochloric acid (useful byproduct for pickling steel, chemical synthesis).
- **Step 2 (Black ash)**: Na₂SO₄ + 2C (coke/charcoal) + CaCO₃ (limestone) → Na₂CO₃ + CaS + 2CO₂. Rotary furnace or reverberatory furnace at 900-1000°C. Mix and roast for 1-2 hours. The coal reduces Na₂SO₄ to Na₂S, which reacts with CaCO₃.
- **Step 3 (Leaching)**: Crush and leach black ash with water. Na₂CO₃ dissolves (soluble). CaS and unreacted solids remain as residue. Crystallize Na₂CO₃·10H₂O (washing soda) by cooling, or calcine to anhydrous Na₂CO₃ (soda ash) by heating to 150°C.
- **Pollution**: CaS waste (~4 tonnes per tonne Na₂CO₃) creates H₂S (toxic, rotten-egg gas) when exposed to rainwater. Historically caused massive environmental damage. Mitigation: oxidize CaS waste with air to CaSO₄ (gypsum — useful for plaster and wallboard).

**Strengths**: No ammonia required — key advantage for early bootstrapping before Haber-Bosch; produces HCl as valuable co-product for steel pickling and chemical synthesis; batch process compatible with simple furnace construction; historically proven (dominated 1791-1880s).

**Weaknesses**: CaS waste (4 t per t Na₂CO₃) releases toxic H₂S when wet; multiple high-temperature furnace stages (150-1000°C); much higher energy consumption than Solvay; HCl emissions historically killed surrounding vegetation; completely displaced by Solvay where ammonia is available.

### Causticization — Converting Soda Ash to Caustic Soda

Sodium hydroxide (NaOH, caustic soda) is produced from sodium carbonate by reaction with slaked lime:

**Lime-soda (causticization) process**:
- **Reaction**: Na₂CO₃ (aq) + Ca(OH)₂ (slaked lime) → 2NaOH (aq) + CaCO₃↓
- Conducted in agitated steel tanks at 80-90°C. The reaction is an equilibrium — NaOH conversion is typically 85-92% depending on concentrations and temperature.
- **Filtration**: CaCO₃ precipitate filtered off (filter press or rotary vacuum filter). CaCO₃ is washed and sent to the lime kiln for reburning (CaCO₃ → CaO → Ca(OH)₂), closing the calcium loop.
- **Evaporation**: The dilute NaOH solution (10-12%) is concentrated by evaporation in multiple-effect vacuum evaporators (steam-heated) to produce 50% NaOH solution (standard commercial grade). Further concentration to 73% or solid NaOH flakes requires higher-temperature evaporation in nickel-clad vessels (NaOH attacks steel above ~60% concentration at elevated temperatures).
- **Energy**: ~2-3 tonnes steam per tonne NaOH (50% solution).
- This route is simpler than electrolysis but produces CaCO₃ sludge and is less economical at large scale. For bootstrapping without electrolysis infrastructure, causticization provides NaOH from Solvay soda ash.

**Strengths**: No electricity or membrane technology required; CaCO₃ byproduct can be reburned to close the lime loop; straightforward equipment (agitated tank + filter + evaporator); well-suited for bootstrapping scenarios.

**Weaknesses**: Equilibrium-limited to 85-92% conversion; high steam consumption for evaporation (2-3 t/t NaOH); produces 50% NaOH max in steel equipment — higher concentrations need nickel-clad vessels; CaCO₃ sludge handling adds operational complexity.

### Potash from Wood Ashes — Pre-Industrial Alkali

Before synthetic alkalis, potash (K₂CO₃) was the primary alkali source for glassmaking, soap, and textile processing:

**Detailed process**:
1. **Harvest and burn**: Burn hardwood (oak, beech, maple preferred — conifers give lower K₂CO₃ yield) to complete combustion. The ash contains 5-15% K₂CO₃, plus CaCO₃, K₂SO₄, KCl, silica, and trace elements.
2. **Leach**: Pack ash into a wooden or stone leaching vat with a drain at the bottom. Pour hot water over ash repeatedly until the lye (leachate) tests at sufficient density (~20° Baumé, ~1.16 g/mL). The K₂CO₃ dissolves; insoluble CaCO₃, SiO₂, and char remain. Filter through cloth or sand bed.
3. **Evaporate**: Boil the lye in iron or clay pots to concentrate. Crude potash crystallizes out — brown color from organic impurities and iron contamination. Yield: ~100 kg K₂CO₃ per tonne of hardwood ash.
4. **Calcine (optional purification)**: Heat crude potash to 800-900°C in a reverberatory furnace to burn off organic impurities. Product: pearl ash (white to grey, 80-95% K₂CO₃). Further purification by recrystallization from water achieves >98% purity.
- **Land intensity**: One hectare of mature hardwood forest yields ~1-2 tonnes of potash per harvest cycle (decades of regrowth required). This is a hunter-gatherer approach to alkali — useful for bootstrapping but not scalable to industrial volumes.
- **Industrial potash**: Modern K₂CO₃ is produced from mined potassium minerals (e.g., reaction of KCl with MgCO₃, or electrolysis of KCl).

**Strengths**: Requires only fire, water, and clay/iron pots — Stone Age technology; produces both alkali (K₂CO₃) and soft soap directly; potassium is essential for glass, soap, and fertilizer; pearl ash (>95% K₂CO₃) achievable with simple calcination.

**Weaknesses**: Catastrophically land-intensive (1-2 t/ha, decades of forest regrowth); yield is only 5-10% of dry wood weight; cannot scale beyond artisanal production; deforestation is inevitable at scale; conifer ash gives much lower K₂CO₃ yield than hardwood.

### Lime Chemistry Detail

**Quicklime (CaO) production**: Limestone (CaCO₃) heated in a lime kiln to 900-1200°C. CaCO₃ → CaO + CO₂. The reaction is endothermic (ΔH = +178 kJ/mol) — requires substantial fuel. Shaft kiln (vertical, continuous): limestone fed at top, fuel (coke, gas, wood) burned in middle, quicklime drawn at bottom. Temperature gradient: top 400°C (preheat), middle 1100°C (calcination zone), bottom 100°C (cooling). Rotary kiln: inclined rotating cylinder 30-60 m long. Better heat transfer, higher throughput, but higher capital cost. Yield: 56 kg CaO per 100 kg CaCO₃ (theoretical — practical yield ~95%).

**Slaked lime (Ca(OH)₂)**: CaO + H₂O → Ca(OH)₂. Highly exothermic (65 kJ/mol). Add quicklime to water in a slaking tank — never water to quicklime. The resulting lime putty or milk of lime (slurry) is used directly in Solvay ammonia recovery, mortar making, water treatment, and causticization.

**Lime mortar setting**: Ca(OH)₂ + CO₂ (from air) → CaCO₃ + H₂O. Sets by carbonation — absorbs CO₂ from atmosphere over weeks to months. Hydraulic lime (containing clay impurities) also sets by hydration of calcium silicates — sets underwater. Roman concrete (opus caecementicium) used hydraulic lime + volcanic ash (pozzolana) — 2000-year durability.

**Lime kiln designs**: (1) Flare kiln (batch): stone arch with fuel underneath, limestone stacked above. Simple, labor-intensive. (2) Shaft kiln (continuous): feed at top, discharge at bottom, fuel injected at middle. Most common for moderate scale. (3) Rotary kiln: inclined rotating tube 30-60 m long. Fuel and limestone enter same end, product exits the other. Best quality and throughput.

**Strengths (lime cycle)**: Limestone is abundant worldwide; shaft kiln is simple continuous equipment; CaCO₃ → CaO → Ca(OH)₂ → CaCO₃ loop is closable; lime has dozens of uses (mortar, causticization, water treatment, flue gas desulfurization, steel flux); 56 kg CaO per 100 kg CaCO₃ with 90-95% practical yield.

**Weaknesses (lime cycle)**: Calcination is strongly endothermic (+178 kJ/mol) — fuel-intensive; quicklime is hazardous (violent reaction with water, caustic burns); slaked lime has limited solubility (1.73 g/L at 20°C); kiln thermal efficiency only 50-70%; CO₂ emissions are intrinsic to the chemistry.

### Ammonia Sources for Solvay

The Solvay process requires ~1-2 kg NH₃ makeup per tonne Na₂CO₃. But the ammonia still must be continuously operated, requiring a steady supply:

1. **Coke oven gas**: Coal carbonization in coke ovens produces gas containing ~1% NH₃. Scrub with sulfuric acid to produce (NH₄)₂SO₄ (ammonium sulfate fertilizer). The NH₃ can be liberated by reaction with Ca(OH)₂ for Solvay use. This was the primary ammonia source before Haber-Bosch.
2. **Haber-Bosch synthesis**: N₂ + 3H₂ → 2NH₃ at 400-500°C, 15-30 MPa. Provides pure, abundant NH₃. See [Ammonia Production](ammonia.md). The modern route.
3. **Calcium cyanamide**: CaC₂ + N₂ → CaCN₂ + C. CaCN₂ + H₂O → CaCO₃ + 2NH₃. Used in early 20th century before Haber-Bosch scaled.

### Environmental Impact

**Leblanc pollution**: The Leblanc process was notorious. CaS waste (4 tonnes per tonne soda ash) released H₂S gas. HCl emissions killed vegetation around plants. The Alkali Act of 1863 (UK) forced producers to absorb HCl in water (creating a market for hydrochloric acid). This was the first modern environmental legislation.

**Solvay waste**: Calcium chloride (CaCl₂) waste — 10 tonnes per tonne soda ash. Historically discharged to rivers, causing salinity. Modern uses: de-icing roads, dust control, concrete accelerator. Some plants achieve zero liquid discharge.

**Electrolysis mercury pollution**: Mercury cell chlor-alkali plants lost Hg to waterways — caused Minamata disease. Largely phased out under Minamata Convention (2017). Membrane cells produce no mercury waste.

### Bootstrap Sequence

1. **[Wood ash potash](../glossary/wood-ash-potash.md)** (Year 1-5): Burn hardwood, leach ash with water, evaporate to K₂CO₃. For glass and soft soap. Land-intensive, not scalable.
2. **[Leblanc process](../glossary/leblanc-process.md)** (Year 10-20): Salt + H₂SO₄ → soda ash. Heavy pollution (HCl, CaS waste). Captures HCl for acid production. Provides both Na₂CO₃ and HCl.
3. **[Lime-soda causticization](../glossary/lime-soda-causticization.md)** (Year 15-25): Na₂CO₃ + Ca(OH)₂ → NaOH. For soap, paper chemicals. Requires lime kiln.
4. **[Solvay process](../glossary/solvay-process.md)** (Year 20-35): Continuous, efficient, less waste. Requires ammonia (coke oven or Haber-Bosch). Displaces Leblanc.
5. **[Electrolytic NaOH](../glossary/electrolytic-naoh.md)** (Year 25+): Chlor-alkali membrane cells produce NaOH + Cl₂ + H₂. Most efficient. See [Electrolysis](electrolysis.md).

### Alkali Uses Summary

| Product | Chemical | Primary Uses |
|---------|----------|-------------|
| Caustic soda | NaOH | Soap and detergent production, paper pulping, chemical processing, drain cleaner |
| Potash | K₂CO₃ | Glass making (lowers SiO₂ melting point), soft soap, fertilizer (potassium source) |
| Soda ash | Na₂CO₃ | Glass making, chemical feedstock, water softening, detergent builder |
| Slaked lime | Ca(OH)₂ | Mortar and plaster (sets by CO₂ absorption), water treatment, ammonia recovery in Solvay |

### Safety & Hazards

- **Caustic chemical burns**: NaOH and KOH solutions cause severe, deep-tissue chemical burns that may not be immediately painful (alkali numbs nerve endings). Concentrated solutions dissolve skin and eye tissue. Wear chemical splash goggles, rubber gloves, and aprons. Eye wash stations mandatory in alkali handling areas.
- **Exothermic dissolution**: Dissolving NaOH or KOH in water releases significant heat. Solution can boil if added too quickly. Always add alkali to water slowly with stirring — never add water to solid alkali (violent spattering). Use heat-resistant containers.
- **Lime hazards**: Quicklime (CaO) reacts violently with water — CaO + H₂O → Ca(OH)₂ releases 65 kJ/mol. The reaction can generate temperatures above 150°C, causing steam explosions if water is added too quickly to large quantities. Always add lime to water (not water to lime). The resulting slaked lime (Ca(OH)₂) is also caustic — causes chemical burns on skin and eyes. PPE: long sleeves, gloves, eye protection.
- **Hydrogen chloride gas**: The Leblanc process produces HCl gas at 150-600°C. HCl is corrosive to respiratory tract and metal equipment. Scrub exhaust gases with water or alkali solution. Ventilate salt cake furnaces to outdoors.
- **Eye damage**: Even dilute caustic splashes can cause permanent corneal damage. Safety goggles (not just glasses) are mandatory for all alkali operations. Flush eye contact immediately with water for 15+ minutes and seek medical attention.
- **Ammonia hazards** (Solvay process): NH₃ gas is a severe respiratory irritant. TLV: 25 ppm. Ammonia absorption towers and distillation columns must be in well-ventilated areas. Emergency shower and eye wash required near ammonia-handling equipment.

 ---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*

## Causticization Detail

The lime-soda process converts sodium carbonate to sodium hydroxide, the stronger alkali needed for soap making, paper pulping, and chemical processing.

**Reaction equilibrium**: Na₂CO₃(aq) + Ca(OH)₂(s) ⇌ 2NaOH(aq) + CaCO₃(s). The equilibrium constant K = [NaOH]² / [Na₂CO₃]. At 80-90°C, conversion reaches 85-92% depending on initial concentrations. Higher temperature increases reaction rate but shifts equilibrium slightly toward reactants (the reaction is mildly exothermic). Typical operating conditions: 10-12% Na₂CO₃ feed solution, 80-90°C, 1-2 hours residence time with agitation. The CaCO₃ precipitate particle size (10-50 μm) affects filtration rate and washing efficiency.

**Separation**: CaCO₃ sludge is separated by vacuum filtration or pressure filtration. The filter cake is washed with hot water to recover entrained NaOH (each tonne of CaCO₃ retains 0.3-0.5 tonnes of solution in the filter cake). The washed CaCO₃ is reburned in the lime kiln (CaCO₃ → CaO + CO₂ at 900-1000°C, ΔH = +178 kJ/mol), closing the calcium loop. Lime kiln fuel: natural gas, coal, or coke. The CO₂ from the kiln can be captured and used for carbonation in the Solvay process.

**NaOH concentration**: The dilute caustic solution (10-12% NaOH from the causticizer) is concentrated by evaporation. Multiple-effect vacuum evaporators (typically triple-effect) use steam to boil off water at progressively lower pressures and temperatures (first effect at 100-120°C, third effect at 50-70°C). Energy consumption: 2-3 tonnes steam per tonne of NaOH (as 50% solution). Commercial caustic soda is sold as 50% aqueous solution (standard grade), 73% solution, or solid flakes/particles (>98% NaOH). Solid NaOH production requires further evaporation in nickel-clad equipment at 400-500°C to remove the last water (steel corrodes above ~60% NaOH at elevated temperatures).

## Solvay Process Economics

**Raw material balance**: Per tonne of Na₂CO₃ produced, the Solvay process consumes approximately 2.2 tonnes of NaCl (at 72% conversion efficiency in the carbonation tower, accounting for recycle) and 2.0 tonnes of limestone (CaCO₃). Ammonia makeup is only 1-2 kg per tonne Na₂CO₃ due to efficient recovery. Steam consumption: 1.5-3.0 tonnes per tonne Na₂CO₃. Electrical power: 50-100 kWh per tonne. Total energy: 7-10 GJ per tonne Na₂CO₃.

**Capital and scale**: A Solvay plant is capital-intensive (carbonation towers, calciner, ammonia still, lime kiln, multiple heat exchangers) but has low operating costs. Economical at 100+ tonnes/day. The Leblanc process requires less capital but higher operating costs and generates far more waste. Modern Solvay plants produce 500-3,000 tonnes/day of soda ash.

## Lime Cycle

The lime cycle (CaCO₃ → CaO → Ca(OH)₂ → CaCO₃) is central to alkali production, cement manufacture, steelmaking (flux), and many other processes.

**Calcination**: CaCO₃ → CaO + CO₂ at 900-1000°C. ΔH = +178 kJ/mol (strongly endothermic). This is the most energy-intensive step. In a shaft kiln: limestone (50-150 mm pieces) fed at the top descends through three zones. Preheating zone (200-800°C): kiln exhaust gases preheat stone. Calcination zone (900-1000°C): fuel (coke, gas) burns and decomposes the stone. Cooling zone (100-400°C): rising combustion air cools the quicklime product, preheating the air for combustion. Residence time: 12-24 hours. Kiln thermal efficiency: 50-70%. Yield: 56 kg CaO per 100 kg CaCO₃ (theoretical, based on molecular weights 56/100). Practical yield 90-95% of theoretical, depending on kiln temperature uniformity and stone size.

**Slaking**: CaO + H₂O → Ca(OH)₂. ΔH = -64 kJ/mol (exothermic, can raise slurry temperature to 90-100°C). Add quicklime to water (never water to quicklime: the violent reaction can cause steam explosions with large quantities). The resulting slaked lime (Ca(OH)₂, also called milk of lime when suspended in water) is a soft white powder, slightly soluble in water (1.73 g/L at 20°C, solubility decreases with temperature). Particle size after slaking: 1-20 μm. Used as slurry (milk of lime at 15-25% solids) for causticization, mortar, water softening, and flue gas desulfurization.

## Alkali Safety

**NaOH hazard detail**: A 50% NaOH solution causes immediate, severe chemical burns on skin contact. The alkali dissolves skin lipids and saponifies tissue proteins, creating a deep, penetrating injury that may not be immediately painful (alkali anesthetizes nerve endings). Eye contact with concentrated NaOH causes immediate corneal damage and potential blindness. Required PPE: chemical splash goggles (not safety glasses), face shield, neoprene or nitrile gloves, rubber apron, long sleeves. Emergency shower and eyewash within 10 seconds travel distance.

**Dissolution exotherm**: Dissolving solid NaOH in water releases 44.5 kJ/mol. Adding 1 kg NaOH to 1 L water generates enough heat to raise the solution temperature above 90°C. Always add solid to water slowly with stirring. Never add water to solid NaOH in a container (the concentrated solution at the contact point can boil violently, spraying caustic). Use heat-resistant containers (polyethylene, polypropylene, or stainless steel, not glass which may crack from thermal shock).

**Environmental hazard**: NaOH solutions are highly toxic to aquatic life (pH >10 is lethal to most fish and invertebrates). Neutralize waste caustic solutions with dilute HCl or H₂SO₄ to pH 6-9 before discharge. Spill response: contain, dilute with water, neutralize with weak acid, then flush.

## Alkali Applications in Industry

**Soap making**: Saponification of fats and oils with NaOH produces sodium salts of fatty acids (soap) and glycerol. Typical formula: 100 kg tallow (or coconut/palm oil blend) + 14-16 kg NaOH (as 50% solution) → 100 kg soap + 10-12 kg glycerol. Temperature: 60-80°C. The reaction is exothermic (ΔH ≈ -10 kJ/mol). Cold process (artisan): mix NaOH solution with melted oils at 35-40°C, pour into molds, cure 4-6 weeks. Hot process (industrial): heat to 80-100°C with continuous agitation in a crutcher (mixing vessel), add salt (NaCl) to salt out the soap (graining), separate glycerol-rich lye, wash and dry the soap base, mill with perfume and color, extrude and stamp into bars.

**Textile processing**: Scouring: cotton fibers treated with 1-3% NaOH at 80-100°C to remove natural waxes, pectins, and impurities before dyeing. Mercerization: cotton fabric treated with 20-25% NaOH at 15-20°C under tension. The alkali swells the cotton fibers, converting cellulose I to cellulose II crystal structure, increasing dye uptake 20-30%, adding silk-like luster, and improving tensile strength 10-20%. The fabric must be held under tension during treatment and rinsing to prevent shrinkage.

### Alkali Waste Management

**Caustic soda waste**: Dilute NaOH rinse water and spent solutions must be neutralized with dilute hydrochloric acid to pH 6-9 before discharge to waterways. The neutralization reaction NaOH + HCl → NaCl + H₂O produces common salt, which is non-toxic at moderate concentrations but can cause freshwater salinity problems if discharged in large volumes.

**Soda ash waste**: Spent or off-spec Na₂CO₃ can be redirected to glass batch as a cullet replacement, where it serves as the flux to lower silica melting temperature. Soda ash waste is also usable in water softening (precipitates Ca²⁺ and Mg²⁺ as carbonates). This circular routing avoids disposal entirely.

**Lime sludge from causticization**: The CaCO₃ sludge from the lime-soda process can be reburned in the lime kiln at 900-1000°C to regenerate CaO (CaCO₃ → CaO + CO₂), which is then slaked back to Ca(OH)₂ for reuse, closing the lime loop. This recycling reduces limestone consumption by 80-90% and eliminates the disposal problem for the largest waste stream in alkali production.

## Limitations

- **Chlorine co-production**: The chlor-alkali process produces Cl₂ and NaOH in a fixed 1:1.12 mass ratio. Chlorine demand does not always match caustic demand, creating market imbalances. Regions with high pulp-and-paper or alumina refining demand (caustic-intensive) may lack matching chlorine consumers, and vice versa.
- **Solvay ammonia consumption**: The Solvay process releases NH₃ from ammonium chloride by reaction with lime (CaO). Ammonia recovery is 95-98% — not 100%. Makeup NH₃ consumption is 1-5 kg per tonne Na₂CO₃, requiring a parallel Haber-Bosch ammonia plant or external NH₃ supply.
- **Lime requirement**: Both causticization and Solvay processes consume limestone (CaCO₃) and produce lime sludge (CaCO₃ or CaCl₂). The lime loop is not fully closed — continuous limestone quarrying is required at 1.0-1.5 tonnes CaCO₃ per tonne NaOH (causticization) or 1.2-1.8 tonnes per tonne Na₂CO₃ (Solvay).
- **Energy intensity**: Electrolytic caustic soda production consumes 2,100-2,500 kWh per tonne NaOH. The Solvay process uses thermal energy (steam) rather than electricity but still requires 7-12 GJ per tonne Na₂CO₃.

## See Also

- **[Solvents](solvents.md)**: NaOH as a reagent and cleaning agent
- **[Electrolysis](electrolysis.md)**: Chlor-alkali membrane cell technology
- **[SEM Tech](sem-tech.md)**: Low-cost ion exchange membranes for chlor-alkali cells
- **[Solvay Process](solvay.md)**: Detailed sodium carbonate production
- **[Acids](acids.md)**: Complementary acid-base chemistry
- **[Soap](soap.md)**: NaOH in saponification

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
