# Alkali Production

> **Node ID**: chemistry.alkalis
> **Domain**: Chemistry
> **Timeline**: Years 20-35
> **Outputs**: soda_ash, caustic_soda, sodium_carbonate

### Alkali Production

**Leblanc process** (first synthetic soda ash):
- **Step 1**: NaCl + H₂SO₄ → NaHSO₄ + HCl (salt cake furnace, 150-200°C, then 550-600°C for complete reaction to Na₂SO₄). HCl byproduct captured as hydrochloric acid.
- **Step 2**: Na₂SO₄ + 2C (coke/charcoal) + CaCO₃ (limestone) → Na₂CO₃ + CaS + 2CO₂. Black ash furnace, 900-1000°C. Mix and roast for 1-2 hours.
- **Step 3**: Leach black ash with water. Na₂CO₃ dissolves. CaS and impurities remain as residue. Crystallize Na₂CO₃ (soda ash) from solution by evaporation.
- **Pollution**: CaS waste (4 tonnes per tonne Na₂CO₃) creates H₂S (rotten egg gas) when exposed to rain. Major environmental problem historically. Oxidize with air to convert to CaSO₄ (gypsum — useful building material).

**Solvay process** (more efficient, later):
- **Principle**: NaCl + NH₃ + CO₂ + H₂O → NaHCO₃ (precipitates) + NH₄Cl. Heat NaHCO₃ → Na₂CO₃ + CO₂ + H₂O. Recycle NH₃ and CO₂.
- **Ammonia recovery**: Heat NH₄Cl with Ca(OH)₂ (slaked lime) → NH₃ + CaCl₂ + H₂O. Calcium chloride is waste product.
- **CO₂ source**: Heat limestone (CaCO₃ → CaO + CO₂) in lime kiln. CaO used for ammonia recovery.
- **Advantages over Leblanc**: Less waste, lower energy, continuous process. But requires ammonia (from coal distillation or Haber-Bosch).
- **Throughput**: 100-1000+ tonnes/day in mature plants.

**Caustic soda (NaOH)**:
- **Lime-soda process**: Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃ (precipitates). Filter, evaporate to 50% NaOH solution. Simple but produces CaCO₃ sludge.
- **Electrolysis of brine** (preferred): See [Electrolysis](electrolysis.md). Produces Cl₂ + H₂ + NaOH simultaneously. Most efficient route.

**Potash (K₂CO₃) — pre-industrial alkali**:
- **Source**: Plant ashes, especially hardwood (oak, beech, maple). Land plants concentrate potassium from soil.
- **Process**: Leach wood ash with water → dissolve K₂CO₃ (sodium and calcium salts are less soluble). Filter through cloth or sand bed. Evaporate filtrate in iron or clay pots → crude potash (brown, 50-70% K₂CO₃). Calcine (heat to 800-900°C) to burn off organic impurities → pearl ash (white, 80-95% K₂CO₃).
- **Yield**: 5-10% of dry wood weight. One hectare of forest yields ~1-2 tonnes potash. Very land-intensive.
- **Uses**: Glass making (K₂CO₃ lowers melting point of silica), soap (potash + fat → soft soap), fertilizer (potassium source).

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

**Raw materials balance** (per tonne Na₂CO₃ produced):
- NaCl: ~1.5 tonnes (at 72% conversion efficiency)
- CaCO₃ (limestone): ~1.2 tonnes
- Coke/coal (for lime kiln): ~0.1 tonnes
- Steam: ~1.5 tonnes
- NH₃ makeup: ~1-2 kg
- Energy: ~7-10 GJ/tonne Na₂CO₃

### Leblanc Process — Detailed Steps

The Leblanc process was the first industrial method for producing soda ash from salt (patented 1791). It is more polluting and less efficient than Solvay but requires no ammonia, making it potentially relevant for bootstrapping:

- **Step 1 (Salt cake)**: NaCl + H₂SO₄ → NaHSO₄ + HCl (150-200°C), then NaHSO₄ + NaCl → Na₂SO₄ + HCl (550-600°C). Product: sodium sulfate (salt cake). HCl gas captured as hydrochloric acid (useful byproduct for pickling steel, chemical synthesis).
- **Step 2 (Black ash)**: Na₂SO₄ + 2C (coke/charcoal) + CaCO₃ (limestone) → Na₂CO₃ + CaS + 2CO₂. Rotary furnace or reverberatory furnace at 900-1000°C. Mix and roast for 1-2 hours. The coal reduces Na₂SO₄ to Na₂S, which reacts with CaCO₃.
- **Step 3 (Leaching)**: Crush and leach black ash with water. Na₂CO₃ dissolves (soluble). CaS and unreacted solids remain as residue. Crystallize Na₂CO₃·10H₂O (washing soda) by cooling, or calcine to anhydrous Na₂CO₃ (soda ash) by heating to 150°C.
- **Pollution**: CaS waste (~4 tonnes per tonne Na₂CO₃) creates H₂S (toxic, rotten-egg gas) when exposed to rainwater. Historically caused massive environmental damage. Mitigation: oxidize CaS waste with air to CaSO₄ (gypsum — useful for plaster and wallboard).

### Causticization — Converting Soda Ash to Caustic Soda

Sodium hydroxide (NaOH, caustic soda) is produced from sodium carbonate by reaction with slaked lime:

**Lime-soda (causticization) process**:
- **Reaction**: Na₂CO₃ (aq) + Ca(OH)₂ (slaked lime) → 2NaOH (aq) + CaCO₃↓
- Conducted in agitated steel tanks at 80-90°C. The reaction is an equilibrium — NaOH conversion is typically 85-92% depending on concentrations and temperature.
- **Filtration**: CaCO₃ precipitate filtered off (filter press or rotary vacuum filter). CaCO₃ is washed and sent to the lime kiln for reburning (CaCO₃ → CaO → Ca(OH)₂), closing the calcium loop.
- **Evaporation**: The dilute NaOH solution (10-12%) is concentrated by evaporation in multiple-effect vacuum evaporators (steam-heated) to produce 50% NaOH solution (standard commercial grade). Further concentration to 73% or solid NaOH flakes requires higher-temperature evaporation in nickel-clad vessels (NaOH attacks steel above ~60% concentration at elevated temperatures).
- **Energy**: ~2-3 tonnes steam per tonne NaOH (50% solution).
- This route is simpler than electrolysis but produces CaCO₃ sludge and is less economical at large scale. For bootstrapping without electrolysis infrastructure, causticization provides NaOH from Solvay soda ash.

### Potash from Wood Ashes — Pre-Industrial Alkali

Before synthetic alkalis, potash (K₂CO₃) was the primary alkali source for glassmaking, soap, and textile processing:

**Detailed process**:
1. **Harvest and burn**: Burn hardwood (oak, beech, maple preferred — conifers give lower K₂CO₃ yield) to complete combustion. The ash contains 5-15% K₂CO₃, plus CaCO₃, K₂SO₄, KCl, silica, and trace elements.
2. **Leach**: Pack ash into a wooden or stone leaching vat with a drain at the bottom. Pour hot water over ash repeatedly until the lye (leachate) tests at sufficient density (~20° Baumé, ~1.16 g/mL). The K₂CO₃ dissolves; insoluble CaCO₃, SiO₂, and char remain. Filter through cloth or sand bed.
3. **Evaporate**: Boil the lye in iron or clay pots to concentrate. Crude potash crystallizes out — brown color from organic impurities and iron contamination. Yield: ~100 kg K₂CO₃ per tonne of hardwood ash.
4. **Calcine (optional purification)**: Heat crude potash to 800-900°C in a reverberatory furnace to burn off organic impurities. Product: pearl ash (white to grey, 80-95% K₂CO₃). Further purification by recrystallization from water achieves >98% purity.
- **Land intensity**: One hectare of mature hardwood forest yields ~1-2 tonnes of potash per harvest cycle (decades of regrowth required). This is a hunter-gatherer approach to alkali — useful for bootstrapping but not scalable to industrial volumes.
- **Industrial potash**: Modern K₂CO₃ is produced from mined potassium minerals (e.g., reaction of KCl with MgCO₃, or electrolysis of KCl).

### Lime Chemistry Detail

**Quicklime (CaO) production**: Limestone (CaCO₃) heated in a lime kiln to 900-1200°C. CaCO₃ → CaO + CO₂. The reaction is endothermic (ΔH = +178 kJ/mol) — requires substantial fuel. Shaft kiln (vertical, continuous): limestone fed at top, fuel (coke, gas, wood) burned in middle, quicklime drawn at bottom. Temperature gradient: top 400°C (preheat), middle 1100°C (calcination zone), bottom 100°C (cooling). Rotary kiln: inclined rotating cylinder 30-60 m long. Better heat transfer, higher throughput, but higher capital cost. Yield: 56 kg CaO per 100 kg CaCO₃ (theoretical — practical yield ~95%).

**Slaked lime (Ca(OH)₂)**: CaO + H₂O → Ca(OH)₂. Highly exothermic (65 kJ/mol). Add quicklime to water in a slaking tank — never water to quicklime. The resulting lime putty or milk of lime (slurry) is used directly in Solvay ammonia recovery, mortar making, water treatment, and causticization.

**Lime mortar setting**: Ca(OH)₂ + CO₂ (from air) → CaCO₃ + H₂O. Sets by carbonation — absorbs CO₂ from atmosphere over weeks to months. Hydraulic lime (containing clay impurities) also sets by hydration of calcium silicates — sets underwater. Roman concrete (opus caecementicium) used hydraulic lime + volcanic ash (pozzolana) — 2000-year durability.

**Lime kiln designs**: (1) Flare kiln (batch): stone arch with fuel underneath, limestone stacked above. Simple, labor-intensive. (2) Shaft kiln (continuous): feed at top, discharge at bottom, fuel injected at middle. Most common for moderate scale. (3) Rotary kiln: inclined rotating tube 30-60 m long. Fuel and limestone enter same end, product exits the other. Best quality and throughput.

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

1. **Wood ash potash** (Year 1-5): Burn hardwood, leach ash with water, evaporate to K₂CO₃. For glass and soft soap. Land-intensive, not scalable.
2. **Leblanc process** (Year 10-20): Salt + H₂SO₄ → soda ash. Heavy pollution (HCl, CaS waste). Captures HCl for acid production. Provides both Na₂CO₃ and HCl.
3. **Lime-soda causticization** (Year 15-25): Na₂CO₃ + Ca(OH)₂ → NaOH. For soap, paper chemicals. Requires lime kiln.
4. **Solvay process** (Year 20-35): Continuous, efficient, less waste. Requires ammonia (coke oven or Haber-Bosch). Displaces Leblanc.
5. **Electrolytic NaOH** (Year 25+): Chlor-alkali membrane cells produce NaOH + Cl₂ + H₂. Most efficient. See [Electrolysis](electrolysis.md).

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

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
