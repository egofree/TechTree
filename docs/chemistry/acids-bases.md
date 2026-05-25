# Acids & Bases

> **Node ID**: chemistry.acids-bases
> **Domain**: Chemistry
> **Timeline**: Years 10-30
> **Outputs**: sulfuric_acid, hydrochloric_acid, nitric_acid, sodium_hydroxide, sodium_carbonate

## Overview

Industrial acids and alkalis underpin nearly all chemical processing: ore leaching, metal pickling, glass etching, textile finishing, soap and detergent production, and semiconductor wafer cleaning. The progression runs from wood-ash lye (K₂CO₃) through lime (CaO), soda ash (Na₂CO₃), and on to strong mineral acids and caustic soda (NaOH).

## Sulfuric Acid Production

Sulfuric acid (H₂SO₄) is the most-produced industrial chemical globally (~200 million tonnes/year). Its production volume is a direct indicator of industrial capacity. Two processes exist: the lead chamber process (70% H₂SO₄, simpler, for bootstrapping) and the contact process (96-98% H₂SO₄, more efficient, requires vanadium catalyst).

**Lead chamber process** (operational at smaller scale):
1. Burn sulfur (S) or iron pyrite (FeS₂) in air to produce SO₂: S + O₂ → SO₂ at 800-1000°C. From pyrite: 4FeS₂ + 11O₂ → 2Fe₂O₃ + 8SO₂. Sulfur burn yields 7% SO₂ by volume in exit gas.
2. Mix SO₂ with air, steam, and nitrogen oxides (NOₓ catalyst) in a large lead-lined chamber (10-20 m long, 5-10 m wide, 5-8 m tall). The reaction proceeds at 30-50°C. NOₓ is introduced as nitric acid (HNO₃) vapor.
3. Chamber reactions: SO₂ + NO₂ + H₂O → H₂SO₄ + NO. The NO is re-oxidized: 2NO + O₂ → 2NO₂, regenerating the catalyst. This is the key cycle — nitrogen oxides act as oxygen carriers.
4. Acid condenses on chamber walls and drips to collection troughs. Product: 62-70% H₂SO₄ (chamber acid). Concentrate by boiling in glass or lead vessels: water boils off, acid concentrates to 78% (boiling point 185°C at 78% concentration).
5. Lead is used because 78% H₂SO₄ forms an insoluble PbSO₄ layer that protects the metal from further attack. Above 85%, lead dissolves — use glass or steel.
6. Yield: 2-3 tonnes H₂SO₄ per tonne sulfur burned. NOₓ loss: 5-10 kg HNO₃ per tonne H₂SO₄ (makeup required).
7. Disadvantages: dilute product, lead construction required, NOₓ emissions. Advantages: no expensive catalyst, works at moderate temperature.

**Contact process** (higher purity, requires catalyst):
1. Burn sulfur to SO₂ (same as above, but target 7-10% SO₂ in air, dried through sulfuric acid scrubbers).
2. Clean and dry the gas: pass through 98% H₂SO₄ in a drying tower to remove moisture (water poisons the vanadium catalyst and creates acid mist downstream). Electrostatic precipitators remove dust.
3. Catalytic oxidation: 2SO₂ + O₂ ⇌ 2SO₃ over vanadium pentoxide catalyst (V₂O₅, 7-10% on silica support, promoted with K₂O and Na₂O). Operating temperature: 400-450°C (first pass), cooling to 400°C between stages. Pressure: 1-2 atm. Conversion: 97-99.5% through 3-4 catalyst beds with inter-stage cooling.
4. SO₃ absorption: Pass SO₃ through 98% H₂SO₄ in a packed absorption tower. SO₃ + H₂O (in H₂SO₄) → H₂SO₄. Do NOT absorb directly into water — forms a persistent, dangerous sulfuric acid mist. Product: 98-99% H₂SO₄ or 20-22% oleum (H₂SO₄ dissolved in SO₃, used for sulfonation reactions).
5. Double absorption (modern): After the first absorption, remaining SO₂ is passed through another catalyst bed and second absorber to achieve 99.5%+ conversion, reducing emissions to <100 ppm SO₂.
6. Catalyst: V₂O₅ on silica, promoted with K₂SO₄/Na₂SO₄. Life: 5-10 years. Temperature activation: above 380°C. Does not deactivate from mild poisoning (robust). See [Catalyst Production](./catalysts.md) for vanadium sourcing.

**Sulfuric acid properties**: Density 1.84 g/mL (98%). Boiling point 337°C (98%). Miscible with water — extremely exothermic (always add acid to water, never water to acid: the heat of dilution is 880 kJ/kg H₂SO₄). Concentrated acid chars organic matter on contact by dehydration. Freezing point: 10°C for 98%, 3°C for 93%.

**Uses**: Fertilizer production (60% of global H₂SO₄ goes to phosphate fertilizer: Ca₃(PO₄)₂ + 2H₂SO₄ → Ca(H₂PO₄)₂ + 2CaSO₄). Metal pickling (removes oxide scale from steel before galvanizing or plating: 10-25% H₂SO₄ at 50-70°C). Petroleum refining (alkylation catalyst). Lead-acid batteries (37% H₂SO₄ electrolyte, density 1.28 g/mL). Chemical synthesis (nitration, sulfonation, esterification).

## Hydrochloric Acid Production

HCl gas dissolves in water to form hydrochloric acid (up to 38% w/w at room temperature). Three production routes exist for a bootstrapping civilization:

**From salt and sulfuric acid** (Leblanc byproduct):
- NaCl + H₂SO₄ → NaHSO₄ + HCl↑ (150-200°C, first stage)
- NaHSO₄ + NaCl → Na₂SO₄ + HCl↑ (550-600°C, salt cake furnace)
- Capture HCl gas by bubbling through water in absorption towers (graphite or glass-packed). Product: 30-32% HCl (concentrated hydrochloric acid, density 1.16 g/mL).
- This route produces HCl as a byproduct of soda ash production — economically attractive.

**Direct synthesis from hydrogen and chlorine**:
- H₂ + Cl₂ → 2HCl (burns in quartz or graphite combustion chamber at 2000°C+)
- Feed gases: electrolytic H₂ and Cl₂ from [chlor-alkali process](./electrolysis.md)
- Burner: quartz tube 10-15 cm diameter, graphite-lined combustion chamber. Gas flow: stoichiometric ratio H₂:Cl₂ = 1:1. Product gas is 100% HCl, absorbed in water to 31-33%.
- Most economical route when chlor-alkali electrolysis is operational.

**Organic chlorination byproduct**: Chlorination of hydrocarbons (e.g., benzene + Cl₂ → chlorobenzene + HCl) produces HCl as a byproduct. Absorb in water to produce commercial HCl. Typically 80-90% of organic industry HCl comes from this route.

**Properties**: 37% HCl has density 1.19 g/mL. Azeotrope at 20.2% HCl (boils at 108.6°C at 1 atm — cannot concentrate past 20% by simple distillation). Fuming above 25% concentration — HCl gas escapes. Strong acid, pKₐ = -7. Extremely corrosive to most metals; stored in glass, rubber-lined steel, or PVC containers.

**Uses**: Steel pickling (15-20% HCl at 40-60°C, removes oxide scale faster than H₂SO₄). [HCl is preferred over H₂SO₄ for pickling because it produces a cleaner surface and the spent solution (waste acid) can be more easily regenerated](../metals/iron-steel.md). pH adjustment in water treatment. Food processing (gelatin production, corn syrup hydrolysis). Pharmaceutical synthesis.

## Nitric Acid Production

**From Chile saltpeter (NaNO₃) — pre-Ostwald route**:
- NaNO₃ + H₂SO₄ → NaHSO₄ + HNO₃↑ (heated in cast iron or glass retort at 120-150°C)
- Distill HNO₃ vapor (bp 83°C for 68% azeotrope, 120°C for anhydrous). Condense in water-cooled glass or stoneware receiver.
- Yield: ~0.8 kg HNO₃ per kg NaNO₃. Requires concentrated H₂SO₄ (93%+).
- Limited by saltpeter availability — suitable for bootstrap but not scalable.

**Ostwald process** (industrial, from ammonia):
1. Catalytic oxidation: 4NH₃ + 5O₂ → 4NO + 6H₂O over Pt-Rh gauze (90% Pt / 10% Rh) at 850-950°C. Contact time <1 millisecond. Conversion: 95-98%. Air-NH₃ mixture: 9-12% NH₃ (below lower explosive limit ~15%).
2. NO oxidation: 2NO + O₂ → 2NO₂ at 20-50°C (slow, third-order kinetics). Requires large reaction volume or elevated pressure (4-8 bar) to achieve acceptable rate.
3. Absorption: 3NO₂ + H₂O → 2HNO₃ + NO in packed column at 4-10 bar. The NO byproduct re-oxidizes and is re-absorbed in subsequent trays. Column height: 20-40 m. Product: 55-68% HNO₃.
4. Concentration to 90-100% requires dehydration: mix with concentrated H₂SO₄ or Mg(NO₃)₂ to "drag" water out, then distill HNO₃ at reduced pressure (bp 83°C at 1 atm for 68%, lower at reduced pressure for higher concentrations).

**Properties**: 68% HNO₃ (concentrated, azeotrope) has density 1.41 g/mL. Fuming nitric acid (86-100%) is a powerful oxidizer — ignites organic matter on contact. Yellow color from dissolved NO₂. Attacks all metals except gold, platinum, and some stainless alloys. Stored in aluminum or stainless steel tanks (forms passive oxide layer).

**Uses**: Fertilizer production (ammonium nitrate: NH₃ + HNO₃ → NH₄NO₃). Explosive manufacture (nitroglycerin, TNT, nitrocellulose — see [Explosives](./explosives.md)). Organic synthesis (nitration of aromatic compounds). Metal etching and passivation. Rocket propellant (as oxidizer with kerosene or hydrazine).

## Caustic Soda (Sodium Hydroxide)

**Lime-soda process** (no electrolysis required):
- Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃↓
- React in agitated steel tank at 80-90°C for 1-2 hours. Conversion: 85-92%.
- Filter CaCO₃ sludge (filter press or rotary vacuum). Wash cake with hot water to recover entrained NaOH. CaCO₃ can be reburned (CaCO₃ → CaO + CO₂ at 900-1000°C) to regenerate Ca(OH)₂.
- Concentrate dilute NaOH (10-12%) by evaporation in multiple-effect vacuum evaporators to 50% NaOH (standard commercial grade). Further concentration requires nickel-clad vessels (NaOH attacks steel above ~60% at elevated temperature).
- Energy: 2-3 tonnes steam per tonne NaOH (50% solution).
- See [Alkali Production](./alkalis.md) for detailed process description.

**Electrolytic NaOH** (from [chlor-alkali process](./electrolysis.md)):
- Co-product with Cl₂ and H₂ from brine electrolysis. Membrane cells produce 30-33% NaOH directly; diaphragm cells produce 10-12% requiring evaporation.
- Higher purity and lower cost at scale, but requires electricity (2,100-2,500 kWh per tonne Cl₂) and membrane or diaphragm technology.

**Properties**: 50% NaOH solution has density 1.53 g/mL. Solid NaOH (flake or pearl) melts at 318°C. Dissolution in water releases 44.5 kJ/mol — adding 1 kg NaOH to 1 L water raises temperature above 90°C. Extremely caustic: causes deep, penetrating chemical burns that may not be immediately painful (alkali anesthetizes nerve endings). PPE: chemical splash goggles, face shield, neoprene gloves, rubber apron.

**Uses**: Soap making (saponification of fats: 100 kg tallow + 14-16 kg NaOH → ~100 kg soap + 10-12 kg glycerol at 60-80°C). Pulp and paper (kraft process: NaOH + Na₂S digests wood lignin at 160-180°C, 8-12 bar). Textile mercerization (20-25% NaOH at 15-20°C swells cotton fibers, increasing dye uptake 20-30%). Petroleum refining (removes H₂S and organic acids from fuel streams). Aluminum production (Bayer process: NaOH dissolves alumina from bauxite at 150-250°C).

## Soda Ash (Sodium Carbonate)

**Leblanc process** (first synthetic route):
1. Salt cake: NaCl + H₂SO₄ → Na₂SO₄ + 2HCl (two-stage, 150-600°C). HCl captured for [hydrochloric acid production](#hydrochloric-acid-production).
2. Black ash: Na₂SO₄ + 2C + CaCO₃ → Na₂CO₃ + CaS + 2CO₂ (900-1000°C, reverberatory furnace).
3. Leach Na₂CO₃ with water. CaS residue (4 tonnes per tonne Na₂CO₃) produces toxic H₂S when wet — oxidize to CaSO₄ (gypsum) before disposal.
4. Energy-intensive and polluting but produces both Na₂CO₃ and HCl from salt and sulfur.

**Solvay process** (preferred when ammonia available):
- NaCl + NH₃ + CO₂ + H₂O → NaHCO₃↓ + NH₄Cl. Heat NaHCO₃ → Na₂CO₃ + CO₂ + H₂O.
- Ammonia recovered by distilling NH₄Cl with Ca(OH)₂ (from limestone). CO₂ from lime kiln. NH₃ makeup only 1-2 kg per tonne Na₂CO₃.
- Throughput: 100-3000 tonnes/day. Energy: 7-10 GJ/tonne Na₂CO₃.
- See [Solvay Process](./solvay.md) for detailed step-by-step.

**Uses**: Glass manufacturing (Na₂CO₃ lowers SiO₂ melting point from 1710°C to ~1000°C — 15-20% Na₂CO₃ in glass batch). Detergent builder (water softener: Na₂CO₃ precipitates Ca²⁺ as CaCO₃). Chemical feedstock (converted to NaOH via causticization). pH adjustment in water treatment.

## Hydrofluoric Acid Production

CaF₂ (fluorite/fluorspar) + H₂SO₄ (conc.) → 2HF↑ + CaSO₄ at 150-300°C in horizontal rotary kiln (steel shell, internally carbon-lined). Absorb HF gas in water to 48-50% concentration (density 1.16 g/mL). Anhydrous HF (bp 19.5°C) produced by distillation — stored in steel cylinders (HF passivates steel surface).

**Hazards**: HF is uniquely dangerous among acids. It penetrates skin immediately, binds calcium in tissue → hypocalcemia → cardiac arrest. Even 2.5% body surface area exposure to concentrated HF can be lethal. Treatment: calcium gluconate gel (2.5%) applied immediately to exposed skin, massaged in for 15+ minutes. Full PPE mandatory: face shield, neoprene gloves (not latex — HF penetrates latex), rubber apron. All HF work areas must have calcium gluconate stations within 10 seconds reach.

**Uses**: Glass etching and frosting (HF dissolves SiO₂: SiO₂ + 4HF → SiF₄ + 2H₂O; followed by SiF₄ + 2HF → H₂SiF₆). Aluminum smelting (HF reacts with Al₂O₃ to form AlF₃, added to cryolite bath). Petroleum alkylation catalyst (concentrated HF or H₂SO₄). Semiconductor etching (dilute HF removes SiO₂ oxide layers — see [Basic Devices](../silicon/basic-devices.md)). Uranium processing (HF converts UF₄ to UF₆ for isotopic enrichment).

## Pickling Acid Management

Steel pickling generates spent acid containing FeSO₄ or FeCl₂ (100-150 g/L iron) plus residual free acid (50-100 g/L). Discharge is environmentally unacceptable. Recovery methods:

**Acid regeneration** (spray roasting):
- Spray spent HCl into a roaster at 600-800°C. HCl vapor and water evaporate; Fe₂O₃ particles form and settle to bottom. Absorb HCl vapor in water → regenerated 18-20% HCl for reuse.
- Fe₂O₃ byproduct: 50-65% Fe, suitable for iron ore sinter feed or pigment production.
- Energy: 2.5-3.5 GJ per tonne regenerated HCl.

**Neutralization**: Treat spent acid with lime (Ca(OH)₂) or NaOH to pH 8-9. Iron precipitates as Fe(OH)₃. Filter sludge (20-40% solids). Landfill sludge. Simple but wastes the acid value.

## Acid-Base Safety

**Sulfuric acid**: Concentrated H₂SO₄ (98%) causes severe thermal and chemical burns. Always add acid to water (never water to acid — violent boiling and spattering). Heat of dilution: 880 kJ/kg. Stored in steel tanks (98% grade; dilute H₂SO₄ attacks steel). PPE: face shield, acid-resistant gloves (neoprene), rubber apron. Spill response: contain with sand or earth, neutralize with lime or soda ash, then flush with water.

**Nitric acid**: Concentrated HNO₃ is a powerful oxidizer. Contact with organic materials (paper, wood, solvents) can cause fire. Produces toxic NO₂ fumes (brown gas, TLV 3 ppm). Store in stainless steel or glass. Fuming HNO₃ requires ventilated storage.

**Hydrochloric acid**: HCl gas irritates respiratory tract at 5 ppm, dangerous at 100 ppm. Scrub vent gases through NaOH solution. Stored in rubber-lined steel, glass, or PVC containers. Steel is not suitable for HCl service.

**Caustic soda**: NaOH causes deep chemical burns that penetrate tissue (dissolves lipids, saponifies proteins). Eye contact with 50% NaOH causes immediate corneal damage — permanent blindness risk. Emergency shower and eyewash within 10 seconds travel distance. Neutralize waste solutions with dilute HCl to pH 6-9 before discharge.

**General acid handling**: Always work in well-ventilated areas or under fume hoods. Never mix acids with bleach (NaOCl) — produces toxic chlorine gas. Never mix HNO₃ with organic solvents — explosion risk. Label all containers with contents, concentration, and hazard. Keep sodium bicarbonate (NaHCO₃) or lime available for emergency neutralization of acid spills.

## Phosphoric Acid

Phosphoric acid (H₃PO₄) is the gateway to phosphate fertilizers, which supply phosphorus — one of the three primary plant macronutrients (N, P, K). Global production exceeds 50 million tonnes/year, with 90% going to fertilizer.

**Wet process** (from phosphate rock):
- Grind phosphate rock (Ca₃(PO₄)₂, 30-34% P₂O₅) to <150 μm.
- React with 93-98% H₂SO₄ at 70-85°C in a series of agitated tanks (4-6 reactors, total residence time 2-6 hours).
- Ca₃(PO₄)₂ + 3H₂SO₄ → 2H₃PO₄ + 3CaSO₄↓ (gypsum precipitates).
- Filter gypsum through vacuum belt filter. Wash cake to recover entrained H₃PO₄. Product: 25-32% P₂O₅ wet-process acid (containing impurities: Fe, Al, Mg, F, organic matter).
- Concentrate by vacuum evaporation to 40-54% P₂O₅. Fluorine evolves as SiF₄/HF — scrub with water to produce fluosilicic acid (H₂SiF₆, used for water fluoridation or AlF₃ production).
- For higher purity (food-grade): solvent extraction with organic solvents (tributyl phosphate in kerosene) separates H₃PO₄ from impurities.

**Thermal process** (from elemental phosphorus):
- Reduce phosphate rock with coke in an electric arc furnace at 1400-1500°C: Ca₃(PO₄)₂ + 3SiO₂ + 5C → 3CaSiO₃ + 5CO + P₂↑. Condense P₂ vapor as white phosphorus (P₄, mp 44°C, highly toxic, ignites spontaneously in air).
- Burn P₄ in air: P₄ + 5O₂ → P₄O₁₀ (phosphorus pentoxide, extremely hygroscopic).
- Hydrate: P₄O₁₀ + 6H₂O → 4H₃PO₄. Product: 85% H₃PO₄, very pure (suitable for food and electronics).
- Energy-intensive (electric arc furnace at 1500°C consumes ~14,000 kWh per tonne P₄) but produces ultra-pure acid.

**Properties**: 85% H₃PO₄ has density 1.69 g/mL. Non-volatile (does not fume). Mild acid (pKₐ₁ = 2.1). Non-oxidizing at room temperature — safer to handle than HNO₃ or H₂SO₄. Solidifies at 21°C (85%). Stored in steel or rubber-lined tanks.

## Acid Concentration Techniques

Simple distillation concentrates volatile acids (HCl, HNO₃) but sulfuric and phosphoric acids are non-volatile and concentrate by boiling off water. Key azeotropes limit simple distillation:

| Acid | Azeotrope concentration | Boiling point |
|------|------------------------|---------------|
| HCl | 20.2% at 1 atm | 108.6°C |
| HNO₃ | 68% at 1 atm | 122°C |
| H₂SO₄ | 98.3% (technical max) | 337°C |
| HF | 38% at 1 atm | 112°C |

To exceed azeotrope concentrations: (1) Vacuum distillation (lowers boiling point, shifts azeotrope). (2) Extractive distillation (add H₂SO₄ to HNO₃ mixture — H₂SO₄ "holds" water more strongly, allowing HNO₃ to distill at higher concentration). (3) Pressure-swing distillation (azeotrope composition shifts with pressure).

## Materials of Construction for Acid Service

| Material | H₂SO₄ (dilute) | H₂SO₄ (conc.) | HCl | HNO₃ | HF | NaOH |
|----------|----------------|----------------|-----|------|----|------|
| Carbon steel | ✗ (corrodes) | ✓ (passivates) | ✗ | ✗ | ✗ | ✓ (dilute) |
| Stainless 316 | ✓ (room temp) | ✓ (<60°C) | ✗ | ✓ | ✗ | ✓ |
| Lead | ✓ (to 78%) | ✗ (>85%) | ✗ | ✗ | ✗ | ✗ |
| Glass/ceramic | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (hot) |
| PVC/CPVC | ✓ (room temp) | ✗ (hot) | ✓ | ✓ (dilute) | ✓ | ✓ |
| Rubber (natural) | ✓ (dilute) | ✗ | ✓ | ✗ | ✗ | ✓ (dilute) |
| PTFE (Teflon) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Lead is uniquely suited for dilute H₂SO₄ (<78%) — forms protective PbSO₄ layer. Carbon steel works for concentrated H₂SO₄ (>90%) and concentrated HNO₃ (>80%) — both passivate steel. Glass and PTFE are universal but expensive. PVC is the workhorse for HCl and dilute acids at ambient temperature.

## Bootstrap Sequence

1. **Wood ash potash** (Year 1-5): Burn hardwood, leach ash with water, evaporate to K₂CO₃. For glass and soft soap. Land-intensive, not scalable.
2. **Lime from limestone** (Year 3-8): CaCO₃ → CaO at 900-1200°C in shaft kiln. Slake with water → Ca(OH)₂ for mortar, whitewash, and causticization.
3. **Lead chamber H₂SO₄** (Year 8-15): From elemental sulfur or pyrite. Produces 62-70% acid for pickling and fertilizer. Requires lead sheet construction.
4. **HCl from salt + H₂SO₄** (Year 10-15): Leblanc salt cake step, or direct synthesis from H₂ + Cl₂ once electrolysis available.
5. **HNO₃ from saltpeter** (Year 10-15): NaNO₃ + H₂SO₄ distillation. Limited by nitrate deposits.
6. **Solvay soda ash** (Year 15-25): Requires ammonia. Displaces Leblanc for Na₂CO₃ production.
7. **Contact process H₂SO₄** (Year 15-25): V₂O₅ catalyst. Produces 96-98% acid. Requires clean, dry SO₂ gas.
8. **Ostwald HNO₃** (Year 20-30): From ammonia and air over Pt-Rh gauze. Requires [ammonia production](./ammonia.md) via Haber-Bosch.
9. **Electrolytic NaOH** (Year 25+): Chlor-alkali membrane cells produce NaOH + Cl₂ + H₂. See [Electrolysis](./electrolysis.md).

## Cross-Domain Links

- **[Alkali Production](./alkalis.md)**: detailed Solvay, Leblanc, causticization, and potash processes
- **[Solvay Process](./solvay.md)**: dedicated article on the ammonia-soda process
- **[Ammonia Production](./ammonia.md)**: Haber-Bosch process enabling Ostwald nitric acid and Solvay soda ash
- **[Electrolysis](./electrolysis.md)**: chlor-alkali process for NaOH, Cl₂, and H₂ co-production
- **[Refractories](./refractories.md)**: furnace linings for acid and alkali production equipment
- **[Iron & Steel](../metals/iron-steel.md)**: pickling acid consumption in steel processing
- **[Basic Semiconductor Devices](../silicon/basic-devices.md)**: HF and H₂SO₄ in wafer processing

---

*Part of the [Chemistry Domain](index.md) • [All Domains](../index.md)*

[← Back to Chemistry](index.md)
