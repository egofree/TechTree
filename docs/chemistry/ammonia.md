# Ammonia Production

> **Node ID**: chemistry.ammonia
> **Domain**: Chemistry
> **Dependencies**: [`chemistry.air-separation`](air-separation.md), [`chemistry.electrolysis`](electrolysis.md), [`energy`](../energy/index.md), [`metals`](../metals/index.md)
> **Enables**: [`health`](../health/index.md), [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`chemistry.explosives`](explosives.md)
> **Timeline**: Years 20-50
> **Outputs**: ammonia, ammonium_nitrate, urea, nitric_acid

### Overview

Ammonia (NH₃) is the second most important industrial chemical after sulfuric acid. The Haber-Bosch process — fixing atmospheric nitrogen as ammonia — feeds roughly half the world's population through synthetic fertilizers. Without industrial ammonia, global agriculture is limited to natural nitrogen sources: guano, saltpeter deposits, and biological nitrogen fixation by legumes. The invention of Haber-Bosch in 1909–1913 removed the nitrogen constraint on civilization growth.

Modern ammonia production consumes ~1-2% of global energy output and ~1.8% of CO₂ emissions, primarily from natural gas-derived hydrogen feedstock. A bootstrapping civilization must build ammonia synthesis to escape the Malthusian trap — but the process demands high-pressure metallurgy, hydrogen production, and air separation as prerequisites.

### Haber-Bosch Process

The overall reaction is deceptively simple:

**N₂ + 3H₂ ⇌ 2NH₃** (ΔH = -92 kJ/mol, exothermic)

The triple bond in N₂ (945 kJ/mol) is one of the strongest in chemistry. Breaking it requires an iron-based catalyst, elevated temperature (for kinetics), and extreme pressure (to shift equilibrium toward the product side, since 4 moles of gas become 2 moles).

**Operating conditions**:
- **Temperature**: 400-500°C. Lower temperature favors equilibrium conversion (exothermic reaction) but slows kinetics. The catalyst is essentially inactive below ~350°C.
- **Pressure**: 15-30 MPa (150-300 bar). Higher pressure dramatically favors NH₃ formation (Le Chatelier). Early plants operated at 20 MPa; modern plants use 15-20 MPa with improved catalysts.
- **Catalyst**: Promoted magnetite (Fe₃O₄, reduced in-situ to porous metallic iron). Promoters: K₂O (1-2%, increases activity), Al₂O₃ (2-4%, structural stabilizer — prevents iron sintering), CaO (1-2%, additional structural promoter). Catalyst particle size: 1.5-3 mm (larger for radial-flow converters to reduce pressure drop), loaded as irregular granules.
- **Conversion per pass**: Only 10-15% of the N₂+H₂ feed converts to NH₃ per pass through the converter. The unreacted gas is recycled — this is critical to process economics.
- **Equilibrium conversion**: At 450°C and 20 MPa with a 3:1 H₂:N₂ feed, equilibrium gives ~16% NH₃. At 30 MPa, ~27%. The gap between equilibrium and actual conversion represents the catalyst's kinetic limitation.

**Converter design principles**:
- The reaction is exothermic, so the converter must remove heat to maintain the 400-500°C operating window while achieving high conversion.
- Feed gas enters cold and is preheated by the hot product gas in internal heat exchangers. The temperature profile through the catalyst beds is the primary design variable.
- Converter walls are thick alloy steel (Cr-Mo or Cr-Mo-V steels) to withstand 15-30 MPa at 400-500°C. Internal temperatures are higher than wall temperatures — the cold feed gas flows along the inside of the pressure shell, cooling it.

### Converter Designs

Three major converter designs represent the historical progression of Haber-Bosch engineering:

**[Quench converter](../glossary/quench-converter.html)** (original design, 1910s-1960s):
- Multiple adiabatic catalyst beds (typically 3-5 beds) stacked in a single pressure vessel.
- Cold feed gas injected between beds (cold-shot quench) to control temperature. After each bed, the gas heats up (exothermic reaction); quench gas brings it back down before the next bed.
- Simple mechanical construction — no internal cooling tubes. But temperature control is crude: quench dilutes the reacting gas with unreacted feed, reducing conversion per pass.
- Maximum bed inlet temperature controlled by quench flow rate. Typical profile: bed 1 inlet 400°C → outlet 500°C, quench to 425°C, bed 2 inlet 425°C → outlet 475°C, quench to 430°C, bed 3 inlet 430°C → outlet 460°C.
- Still used in some older plants due to mechanical simplicity and ease of catalyst loading.

**Tube-cooled (TVA-type) converter**:
- Catalyst packed outside tubes; cold feed gas flows through tubes embedded in the catalyst bed. Heat transfers continuously from catalyst to tube gas, providing near-isothermal operation.
- Better temperature control than quench design. Higher conversion per pass (12-17% vs. 10-13%).
- Disadvantage: tubes complicate catalyst loading and unloading. Tube leaks are difficult to repair — require complete shutdown and catalyst removal.
- Internal heat exchanger at the top of the vessel preheats incoming gas using hot product gas.

**[Radial-flow converter](../glossary/radial-flow-converter.html)** (modern, 1960s-present):
- Gas flows radially inward through an annular catalyst bed (from outer perimeter to central collection pipe) rather than axially through a cylindrical bed.
- Much larger cross-sectional flow area → lower pressure drop (0.2-0.5 MPa vs. 1-2 MPa for axial flow). This allows use of smaller catalyst particles (1.5-2.0 mm) which have higher activity (more surface area), without excessive pressure drop.
- Typically 2-3 beds in series with inter-stage cooling (indirect heat exchangers or quench).
- Highest single-pass conversion of the three designs (14-18%). Favored for modern large-capacity plants (1,000-3,000 tonnes NH₃/day).
- Examples: Haldor Topsøe S-200/S-250, KBR advanced ammonia process (KAAP) using ruthenium-based catalyst on graphite support for the top bed.

### Recycle Loop and Product Recovery

The 10-15% conversion per pass means 85-90% of the feed gas is unreacted and must be recycled:

**Recycle loop design**:
- Converter effluent (NH₃ + unreacted N₂ + H₂) is cooled to condense ammonia. At 20 MPa and -10 to 0°C, most NH₃ condenses as liquid (NH₃ condensation temperature at 20 MPa is ~50°C — cooling to 0°C recovers ~85-90% of the NH₃ as liquid).
- Liquid ammonia is separated in a high-pressure separator vessel. Unreacted gas (still at high pressure) is returned to the converter feed by a recycle compressor.
- **Purge gas**: Inerts (CH₄ from SMR, Ar from air separation) accumulate in the recycle loop. A small purge stream (~5-10% of recycle flow) is continuously withdrawn to prevent inert buildup above ~10-15% of the gas composition. The purge gas is burned as fuel or sent to a hydrogen recovery unit (cryogenic or membrane).
- **Product**: Liquid ammonia at ~-33°C, stored under moderate pressure (~10 bar) or refrigerated at atmospheric pressure.

**Energy integration**:
- The recycle compressor adds ~3-5 MPa pressure to overcome loop pressure drop (converter bed + heat exchangers + piping).
- Feed gas is compressed from atmospheric pressure to loop pressure (15-30 MPa) in a multi-stage centrifugal or reciprocating compressor with inter-stage cooling. Compression power: ~0.5-0.8 MWh per tonne NH₃.
- Product chilling requires refrigeration compressors: ~0.1-0.2 MWh per tonne NH₃.
- Total energy for synthesis loop: ~0.6-1.0 MWh per tonne NH₃ (excluding feedstock production).

### Feedstock Production

The two feedstocks — hydrogen and nitrogen — come from very different sources:

**[Hydrogen from steam methane reforming (SMR)](../glossary/hydrogen-from-steam-methane-reforming-smr.html)** (dominant route, ~80% of global production):
- **Step 1 — Primary reformer**: CH₄ + H₂O → CO + 3H₂ at 700-850°C, 3-4 MPa, over Ni/Al₂O₃ catalyst in vertically suspended tubes inside a gas-fired furnace. Endothermic (ΔH = +206 kJ/mol). The furnace is the largest single equipment item in an ammonia plant.
- **Step 2 — Secondary reformer**: Residual CH₄ (5-10% from primary) is reformed with air (which also introduces the N₂ needed for ammonia synthesis). Air is injected and partially combusted: CH₄ + O₂ → CO₂ + H₂O (provides heat), then remaining CH₄ + H₂O → CO + H₂ over Ni catalyst. Exit temperature: 950-1000°C. Gas composition: ~56% H₂, ~22% N₂, ~12% CO, ~8% CO₂ + H₂O.
- **Step 3 — Shift conversion**: CO + H₂O → CO₂ + H₂. Two stages: high-temperature shift (350-400°C, Fe-Cr catalyst) and low-temperature shift (200-250°C, Cu-Zn-Al catalyst). Converts most CO to CO₂ while producing additional H₂.
- **Step 4 — CO₂ removal**: Absorb CO₂ in amine solution (MEA, MDEA) or physical solvent (Selexol, Rectisol). CO₂ is stripped from the solvent and either vented, used for urea production, or sequestered. CO₂ from SMR is the largest source of greenhouse gas emissions in ammonia production (~1.6 tonnes CO₂ per tonne NH₃).
- **Step 5 — Methanation**: Residual CO and CO₂ (0.2-0.5%) are hydrogenated back to CH₄ over Ni catalyst at 300-400°C. CO and CO₂ are severe catalyst poisons for the Haber-Bosch iron catalyst — must be reduced to <10 ppm total. The small amount of CH₄ formed is tolerated as an inert.
- **Overall SMR stoichiometry**: CH₄ + 2H₂O → CO₂ + 4H₂ (after shift and CO₂ removal). Plus N₂ from the air in the secondary reformer. Feed gas to synthesis: ~74% H₂, ~24% N₂, ~1-2% CH₄, <10 ppm CO+CO₂.

**[Hydrogen from electrolysis](../glossary/hydrogen-from-electrolysis.html)** (clean route, growing):
- Water electrolysis produces pure H₂ and O₂. See [Electrolysis](electrolysis.md) for detailed cell designs.
- N₂ must be supplied separately (from air separation) since there is no secondary reformer to introduce air.
- Energy: ~50-55 kWh per kg H₂ (alkaline electrolysis). Ammonia requires ~178 kg H₂ per tonne NH₃ → ~9-10 MWh per tonne NH₃ just for hydrogen. This is 5-10× the energy cost of SMR-derived hydrogen, but produces zero CO₂ emissions if the electricity is renewable.
- Currently economic only where electricity is very cheap (<$0.02/kWh) or where carbon pricing is high.

**Nitrogen from air separation**:
- See [Air Separation](air-separation.md) for detailed plant design.
- Cryogenic distillation of air produces 99.999% pure N₂. Required because O₂ poisons the Haber-Bosch catalyst and because precise N₂:H₂ ratio control (1:3 stoichiometry) is needed.
- For SMR-based plants, N₂ comes from the air injected into the secondary reformer — no separate air separation needed. This is the main advantage of the SMR route.
- For electrolysis-based plants, a dedicated air separation unit is required.

**Syngas purification**:
- **Sulfur removal**: Natural gas feedstock contains H₂S and organic sulfur compounds (mercaptans, thiophenes) which permanently poison the Ni reforming catalyst. Desulfurization: pass gas over ZnO absorbent at 350-400°C (H₂S + ZnO → ZnS + H₂O) after hydrogenation of organic sulfur over Co-Mo catalyst.
- **CO₂ specification**: <10-50 ppm in feed to synthesis loop. CO₂ forms carbamates and ammonium carbonate in the converter, plugging catalyst pores.
- **Moisture**: Dew point below -50°C. Water reversibly poisons the iron catalyst.

### Ammonia Storage and Handling

**Anhydrous ammonia properties**:
- Boiling point: -33.3°C at atmospheric pressure. Colorless gas with pungent, suffocating odor (detectable at ~5 ppm — serves as its own warning).
- Liquid density: 0.68 kg/L at -33°C. Vapor pressure: 10 bar at 25°C.
- Highly soluble in water (forming ammonium hydroxide, NH₄OH). Dissolution is strongly exothermic.

**Storage methods**:
- **[Pressurized storage](../glossary/pressurized-storage.html)** (ambient temperature): Steel spherical or cylindrical pressure vessels at 10-17 bar. Design temperature: 0-40°C. Vessel size: 500-5,000 tonnes. Refrigeration only required if ambient temperature causes excessive pressure. Most common for intermediate storage at production plants.
- **[Refrigerated storage](../glossary/refrigerated-storage.html)** (low temperature, near-atmospheric pressure): Insulated steel tanks at -33°C, slightly above atmospheric pressure. Double-wall construction with insulated annular space. Tank size: 10,000-50,000 tonnes. External refrigeration system (compressor + condenser) maintains temperature by condensing boil-off vapor. Used for large-scale storage and import/export terminals.
- **Semi-refrigerated**: Combination — moderate pressure (2-5 bar) and moderate cooling (-10 to 0°C). Smaller refrigeration equipment than fully refrigerated. Used for transport vessels and mid-size storage.

**Transport**:
- **Pipeline**: Carbon steel, 100-250 mm diameter, operating at 15-25 bar. The US Gulf Coast ammonia pipeline network spans ~1,500 km. Pipeline transport is the cheapest mode for large volumes over land.
- **Rail and road**: Pressure tank cars and tanker trucks (10-17 bar). Capacity: 30-70 tonnes per car. DH-105 pressure relief valves prevent over-pressurization.
- **Marine**: Refrigerated cargo ships at -33°C. Capacity: 10,000-50,000 tonnes per vessel. Ammonia is the second most transported chemical by sea (after sulfuric acid).

**Safety**:
- **Toxicity**: IDLH (immediately dangerous to life and health) = 300 ppm. Ammonia attacks eyes, respiratory tract, and skin. Fatal at ~5,000-10,000 ppm. Liquid ammonia causes frostbite and chemical burns simultaneously.
- **Flammability**: Flammable range 15-28% in air. Auto-ignition temperature: 651°C. Harder to ignite than hydrocarbons but fires do occur.
- **Emergency response**: Large water sprays to knock down vapor clouds (ammonia is highly water-soluble). Evacuate downwind. Full-face SCBA (self-contained breathing apparatus) for emergency responders. Ammonia vapor is lighter than air when warm but can pool at ground level when cold (density of cold NH₃ vapor is greater than air).
- **Materials compatibility**: Carbon steel is acceptable for anhydrous ammonia. DO NOT use copper, zinc, or their alloys (brass, bronze) — ammonia causes stress corrosion cracking. Valves and instruments use stainless steel components.

### Fertilizer Production Bridge

Ammonia is the gateway to virtually all synthetic nitrogen fertilizers. This is the economic justification for the entire Haber-Bosch industry:

**[Ammonium nitrate](../glossary/ammonium-nitrate.html)** (NH₄NO₃, 33-34% N):
- NH₃ + HNO₃ → NH₄NO₃. Neutralization reaction is exothermic — produces steam.
- Concentrate the resulting solution to 95-97% by vacuum evaporation. Solidify by prilling (spraying droplets from the top of a tower, solidifying as they fall) or granulation.
- **Safety**: Ammonium nitrate is a strong oxidizer. It has caused some of the largest industrial explosions in history (Oppau 1921, Texas City 1947, Beirut 2020). Store separately from combustible materials. Keep below 50°C. Do not confine in sealed containers when heated. Commercial fertilizer-grade NH₄NO₃ is treated with anti-caking agents and may be coated to reduce detonation sensitivity.
- Requires nitric acid from the Ostwald process (see below and [Mineral Acid Production](acids.md)).

**[Urea](../glossary/urea.html)** (CO(NH₂)₂, 46% N — highest nitrogen content of any solid fertilizer):
- **Step 1**: 2NH₃ + CO₂ → NH₂COONH₄ (ammonium carbamate) at 140-200°C, 14-20 MPa.
- **Step 2**: NH₂COONH₄ → CO(NH₂)₂ + H₂O (endothermic dehydration). Conversion: 50-70% per pass in conventional plants; 70-80% in advanced designs with higher temperature/pressure.
- **Unreacted recycle**: The urea solution contains unreacted carbamate and NH₃/CO₂. Recycle by stripping with NH₃ gas (Stamicarbon process) or CO₂ (Snamprogetti process) at reduced pressure.
- **Prilling/granulation**: Concentrate urea solution by vacuum evaporation to 96-99%, then prill or granulate. Dust from prilling is explosive — dust collection required.
- **CO₂ source**: From SMR in the ammonia plant — the urea process consumes ~0.75 tonnes CO₂ per tonne urea, partially offsetting the CO₂ emissions from ammonia production.
- **Advantages**: Highest N content, solid (easy to transport), slow-release in soil (hydrolyzes to NH₃ over days-weeks), and can be blended with other fertilizers.

**[Ammonium sulfate](../glossary/ammonium-sulfate.html)** ((NH₄)₂SO₄, 21% N + 24% S):
- NH₃ + H₂SO₄ → (NH₄)₂SO₄. Direct neutralization. Also produced as byproduct of coke oven gas scrubbing (NH₃ + H₂SO₄) and caprolactam production.
- Lower nitrogen content than urea or ammonium nitrate, but the sulfur content is valuable for sulfur-deficient soils.

**[Superphosphate and ammonium phosphates](../glossary/superphosphate-and-ammonium-phosphates.html)** (NPK bridge):
- **Single superphosphate**: Ca₃(PO₄)₂ + 2H₂SO₄ → Ca(H₂PO₄)₂ + 2CaSO₄. Phosphate rock + sulfuric acid. Contains P and Ca but no nitrogen.
- **Ammonium phosphate**: NH₃ + H₃PO₄ → (NH₄)H₂PO₄ (MAP, monoammonium phosphate, 11% N + 52% P₂O₅) or 2NH₃ + H₃PO₄ → (NH₄)₂HPO₄ (DAP, diammonium phosphate, 18% N + 46% P₂O₅). These combine nitrogen and phosphorus in the most widely traded fertilizer commodities.
- Phosphoric acid from [Mineral Acid Production](acids.md).

### Ostwald Process — Nitric Acid from Ammonia

The Ostwald process converts ammonia to nitric acid (HNO₃) via catalytic oxidation. Together, Haber-Bosch and Ostwald form the nitrogen chemicals chain: N₂ → NH₃ → HNO₃.

**Step 1 — Ammonia oxidation**:
- 4NH₃ + 5O₂ → 4NO + 6H₂O (ΔH = -905 kJ, strongly exothermic)
- Catalyst: Pt-Rh gauze (90% Pt / 10% Rh), woven wire mesh, 0.06 mm wire diameter, 3-5 layers. Catalyst temperature: 850-950°C. Contact time: <1 millisecond.
- Air-NH₃ mixture: 9-12% NH₃ by volume (below the lower explosive limit of ~15%). Too much air wastes energy compressing it; too little reduces conversion.
- Conversion efficiency: 95-98%. Catalyst loss: 0.05-0.5 g Pt per tonne HNO₃ (gauze slowly evaporates at operating temperature — Pt is recovered from the downstream filter or from plant turnaround scrap).
- The hot gas (850-900°C) is cooled in a waste heat boiler to generate high-pressure steam (the Ostwald plant is a net energy exporter).

**Step 2 — NO oxidation**:
- 2NO + O₂ → 2NO₂ (ΔH = -114 kJ)
- Occurs spontaneously as gas cools below ~150°C. Third-order kinetics (rate ∝ [NO]²[O₂]) — very slow at low NO concentrations.
- Requires large reaction volume or elevated pressure (4-8 bar) to achieve acceptable conversion in reasonable equipment size. The rate-determining step of the overall process.

**Step 3 — Absorption**:
- 3NO₂ + H₂O → 2HNO₃ + NO (ΔH = -117 kJ)
- Counter-current absorption in packed columns (bubble-cap trays or ceramic packing) at 4-10 bar. The NO byproduct is re-oxidized to NO₂ and re-absorbed in subsequent trays — the column height (20-40 m) accommodates multiple NO→NO₂→HNO₃ cycles.
- Product: 55-68% HNO₃ depending on absorption pressure and column design. Concentration to 90-100% requires additional dehydration with Mg(NO₃)₂ or H₂SO₄.

See [Mineral Acid Production](acids.md) for complete Ostwald process detail including plant scale, energy balance, and higher-concentration methods.

### Other Applications

**Solvay ammonia supply**: The Solvay process (see [Alkali Production](alkalis.md)) uses NH₃ as a recyclable intermediate in soda ash production. While most NH₃ is recovered internally, the 1-2 kg/tonne makeup requirement plus initial plant charge demand a continuous ammonia source. Haber-Bosch ammonia replaced coke-oven gas as the primary Solvay NH₃ supply after 1910.

**Refrigeration**: Ammonia is one of the oldest and most efficient refrigerants (R-717). Vapor-compression refrigeration cycle: liquid NH₃ evaporates at low pressure (~2 bar, -20°C) absorbing heat, then compressed to ~10 bar, condensed at ~25°C releasing heat. COP (coefficient of performance): 4-5 for industrial systems. Used in large industrial refrigeration (cold storage, ice plants, food processing) — not in domestic refrigerators due to toxicity concerns.

**Explosives**: NH₄NO₃ + fuel oil (ANFO) is the most widely used industrial explosive (mining, quarrying). Nitroglycerin and TNT also originate from the ammonia-nitric acid chain. See [Explosives](explosives.md).

**Nylon**: Adipic acid (from cyclohexane oxidation with HNO₃) + hexamethylenediamine (from butadiene or adipic acid via NH₃ chemistry) → nylon 6,6. The synthetic fiber industry depends on ammonia-derived intermediates.

**Cleaning agents**: Aqueous ammonia (5-10% NH₃ in water, "ammonia water") is a common household and industrial cleaner. Effective at dissolving grease, neutralizing acids, and removing stains.

### Catalyst Production

The Haber-Bosch iron catalyst is itself a product of industrial chemistry:

**Magnetite catalyst manufacture**:
- Melt purified Fe₃O₄ (magnetite) with promoter oxides (K₂O, Al₂O₃, CaO) in an electric arc furnace at ~1600°C. Cast into ingots, crush to 1.5-5 mm granules.
- The promoters serve distinct functions: Al₂O₃ and CaO form structural "scaffolding" within the reduced iron particles, preventing sintering (loss of surface area) during years of operation at 400-500°C. K₂O is an electronic promoter — it donates electrons to the iron surface, weakening N₂ adsorption and facilitating hydrogenation of surface nitrogen atoms.
- **Activation**: The magnetite (Fe₃O₄) must be reduced to metallic iron in-situ by flowing H₂/N₂ synthesis gas at 350-450°C for 24-72 hours. Reduction is exothermic — must be controlled carefully to avoid sintering the freshly formed iron. The reduced catalyst is pyrophoric — ignites spontaneously in air. Must be passivated (thin oxide layer) for safe handling and transport.

**[Ruthenium catalyst](../glossary/ruthenium-catalyst.html)** (advanced, used in KBR KAAP process):
- Ru on graphite (activated carbon) support, promoted with Ba and K. 10-20× higher activity per unit mass than iron catalyst.
- Enables operation at lower pressure (7-10 MPa) and moderate temperature (350-450°C).
- Cost: Ruthenium is rare (~$500-1000/oz). Only economic for the top bed of a multi-bed converter, where it handles the most kinetically demanding conversion.
- Sensitivity: Ru catalyst is poisoned by trace oxygen compounds. Requires very clean synthesis gas (<1 ppm O₂, H₂O, CO, CO₂).

### Bootstrap Sequence

The path to industrial ammonia production follows a specific build order constrained by the prerequisite infrastructure:

**Stage 1: Coke-oven ammonia** (Years 15-25)
- Coal destructive distillation (coke ovens at 1000-1200°C) produces coke oven gas containing ~1-2% NH₃ by volume. Scrub with water or dilute H₂SO₄ to recover ammonium sulfate ((NH₄)₂SO₄) or ammonia liquor.
- A medium coke plant (1,000 tonnes coal/day) yields ~5-10 tonnes NH₃/day. Enough for early Solvay plants and limited fertilizer production.
- This is pre-Haber-Bosch ammonia — limited by coal supply but requires no high-pressure equipment.

**Stage 2: Early Haber-Bosch** (Years 20-35)
- Requires: high-pressure steel vessels (15-20 MPa, Cr-Mo alloy steels), hydrogen (from coke-oven gas separation or early electrolysis), nitrogen (from air separation or Linde fractionation), iron catalyst.
- First plant scale: 30-100 tonnes NH₃/day. Sufficient to replace coke-oven ammonia for Solvay supply and begin synthetic fertilizer production.
- Key bottleneck: high-pressure compressor reliability. Early compressors were massive reciprocating machines with frequent seal and valve failures.

**Stage 3: Full-scale Haber-Bosch with SMR** (Years 30-50)
- Requires: natural gas (or coal gasification), steam reforming furnace, shift converters, CO₂ removal, air separation for nitrogen, centrifugal synthesis gas compressors.
- Plant scale: 500-3,000 tonnes NH₃/day. Energy consumption: 28-35 GJ per tonne NH₃ (modern plants). This is the mature industry.
- Enables massive fertilizer production → agricultural expansion → population growth support.

**Stage 4: Electrolysis-based ammonia** (Years 40+)
- Requires: cheap, abundant electricity (hydroelectric, nuclear, or solar/wind), alkaline water electrolysis, dedicated air separation.
- Zero-carbon ammonia route. Energy cost is 5-10× higher than SMR per tonne NH₃, but no CO₂ emissions.
- The long-term sustainable path — dependent on energy infrastructure development.

**Why ammonia matters for bootstrapping**: The nitrogen constraint is one of the hardest limits on agricultural productivity. Without synthetic nitrogen fertilizer, crop yields plateau at ~1-2 tonnes/hectare for cereal crops. With ammonium nitrate or urea fertilizer, yields reach 5-10 tonnes/hectare. Haber-Bosch is the difference between feeding 3-4 billion people and feeding 8+ billion. In a bootstrap scenario, achieving ammonia synthesis is the single most important milestone for food security after water and basic agriculture.

### Safety and Hazards

**Ammonia synthesis loop**:
- High-pressure hydrogen service (15-30 MPa, H₂+N₂+NH₃ mixture). Hydrogen embrittlement is the primary metallurgical concern — steel loses ductility under high-pressure hydrogen at elevated temperature. Use only approved Cr-Mo alloys. Inspect vessels regularly for cracking.
- Synthesis gas is flammable/explosive when mixed with air. Purge with N₂ before introducing H₂. Purge with N₂ before opening to air (the reduced iron catalyst is pyrophoric).

**Ammonia handling**:
- Full-face respirator or SCBA for any release response. Ammonia gas attacks moist tissues (eyes, lungs, mucous membranes). Detectable odor at ~5 ppm serves as warning, but olfactory fatigue occurs rapidly — do not rely on smell alone.
- Water spray systems for emergency dilution of vapor releases. Ammonia is extremely water-soluble — 1 liter of water absorbs ~700 liters of NH₃ gas at 20°C.
- Liquid ammonia causes severe frostbite and chemical burns. Double-glove with chemical-resistant gloves (butyl rubber) and face shield.

**Catalyst handling**:
- Reduced iron catalyst is pyrophoric — store and handle under inert atmosphere (N₂). Passivate before disposal by controlled exposure to low-O₂ gas (1-2% O₂ in N₂) over 24-48 hours.
- Spent catalyst may contain metal sulfides and heavy metals — treat as hazardous waste.

**Ammonium nitrate storage**:
- Store in cool, dry, well-ventilated areas away from combustible materials, organic substances, acids, and heat sources. Maximum storage temperature: 50°C.
- Large stockpiles must be separated by firewalls. The Beirut explosion (2020) was caused by ~2,750 tonnes of NH₄NO₃ stored improperly for 6 years.
- See [Explosives](explosives.md) for detailed ammonium nitrate safety protocols.

---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
