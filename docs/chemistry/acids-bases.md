# Acids & Bases

> **Node ID**: chemistry.acids-bases
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: None
> **Enables**: `chemistry`
> **Timeline**: Years 10-30
> **Outputs**: sulfuric_acid, hydrochloric_acid, nitric_acid, sodium_hydroxide, sodium_carbonate, hydrofluoric_acid, phosphoric_acid
> **Critical**: No — overview capability linking acid and base production; see individual articles for detailed processes

## Overview

Industrial acids and alkalis underpin nearly all chemical processing: ore leaching, metal pickling, glass etching, textile finishing, soap and detergent production, and semiconductor wafer cleaning. The progression runs from wood-ash lye (K₂CO₃) through lime (CaO), soda ash (Na₂CO₃), and on to strong mineral acids and caustic soda (NaOH).

Sulfuric acid alone accounts for ~60% of global chemical production by volume — a civilization's industrial maturity can be measured by its H₂SO₄ output. The contact process (96-98% H₂SO₄ via V₂O₅ catalyst at 400-450°C) is the backbone route, while the lead chamber process (62-70%) provides a bootstrap alternative that avoids vanadium. Nitric acid from the Ostwald process (NH₃ oxidation over Pt-Rh gauze at 850-950°C) and hydrochloric acid (direct H₂ + Cl₂ synthesis or salt + H₂SO₄) complete the mineral acid set.

On the alkali side, soda ash (Na₂CO₃) via the Solvay process and caustic soda (NaOH) via chlor-alkali electrolysis or lime-soda causticization are the two highest-volume bases. Before synthetic alkalis, wood-ash potash served for glass and soap at artisanal scale. This article provides cross-referenced process details and a bootstrap sequencing guide; the detailed process articles cover individual acids and alkalis in depth.

## Prerequisites

### Materials

- **Sulfur** (elemental, ≥99% S) or **pyrite** (FeS₂, >45% S) — feedstock for H₂SO₄. Source: [Mining](../mining/index.md) — volcanic sulfur deposits or sulfide ore roasting
- **Salt** (NaCl, >97%) — feedstock for HCl, chlorine, and soda ash. Source: [Mining](../mining/index.md) — rock salt or solar evaporation of seawater
- **Limestone** (CaCO₃, >95%) — feedstock for lime (CaO) and Solvay soda ash. Source: [Mining](../mining/index.md)
- **Saltpeter** (NaNO₃) or **ammonia** (NH₃) — feedstock for HNO₃. Source: natural nitrate deposits or [Ammonia Production](ammonia.md)
- **Fluorspar** (CaF₂, >97%) — feedstock for HF. Source: [Mining](../mining/index.md)
- **Phosphate rock** (Ca₃(PO₄)₂, 30-34% P₂O₅) — feedstock for phosphoric acid. Source: [Mining](../mining/index.md)

### Tools and Equipment

- [Reactor vessels](reactor-vessel.md) — lead-lined or acid-brick-lined steel for H₂SO₄; glass-lined for HCl and HNO₃
- [Acid production](acids.md) — contact process converter (V₂O₅ catalyst bed), lead chamber sequence, absorption towers
- [Alkali production](alkalis.md) — Solvay carbonation tower, lime-soda causticization pans, chlor-alkali electrolysis cells
- [Heat exchangers](heat-exchanger.md) — acid-resistant (silicon iron, graphite, or tantalum) for heat recovery
- [Distillation columns](distillation-column.md) — HCl absorption, HNO₃ concentration

### Knowledge

- Acid-base stoichiometry and pH scale: neutralization reactions, normality calculations, titration endpoints
- Materials of construction: which metals/alloys/polymers resist which acids at which concentrations and temperatures (e.g., concentrated H₂SO₄ in steel, dilute H₂SO₄ attacks steel; HCl requires rubber-lined steel or Hastelloy)
- Thermodynamics of exothermic dilution: H₂SO₄ dilution releases 880 kJ/kg — always add acid to water, never water to acid

### Infrastructure

- Ventilation with acid gas scrubbing (NaOH caustic scrubbers on tail gas)
- Acid-resistant flooring and drainage (acid-brick, vinyl ester grout)
- Emergency deluge showers and eyewash stations at 10 m maximum distance from any acid handling point
- Power supply for electrochemical routes ([Electrolysis](electrolysis.md))

## Bill of Materials

| Material | Quantity per tonne product | Source | Alternatives |
|----------|---------------------------|--------|-------------|
| Sulfur (for H₂SO₄ contact process) | 0.33-0.35 t S per t H₂SO₄ | [Mining](../mining/index.md) — Frasch or volcanic sulfur | Pyrite (FeS₂, 0.75 t per t H₂SO₄), smelter off-gas SO₂ |
| Vanadium pentoxide (V₂O₅ catalyst) | 0.1-0.3 kg per t H₂SO₄/year | [Mining](../mining/index.md) — vanadium ore | Platinum catalyst (costly), NOₓ gas (lead chamber process) |
| Salt (for Solvay Na₂CO₃) | 1.5-1.6 t NaCl per t Na₂CO₃ | [Mining](../mining/index.md) — rock salt or brine | — |
| Limestone (for Solvay Na₂CO₃) | 1.2-1.4 t CaCO₃ per t Na₂CO₃ | [Mining](../mining/index.md) — high-calcium limestone | — |
| Ammonia (Solvay makeup) | 1-3 kg NH₃ per t Na₂CO₃ (recycled) | [Ammonia Production](ammonia.md) | Coke-oven gas NH₃ (pre-Haber-Bosch) |
| Salt (for HCl, Leblanc route) | 1.6 t NaCl per t HCl | [Mining](../mining/index.md) | Direct H₂ + Cl₂ synthesis |
| Phosphate rock (for H₃PO₄) | 2.7-3.0 t rock per t P₂O₅ | [Mining](../mining/index.md) | — |
| Electrical energy (chlor-alkali NaOH) | 2,100-2,800 kWh per t NaOH | [Energy](../energy/index.md) — baseload required | Lime-soda causticization (no electricity, but lower purity) |

## Process Description

This section summarizes the major acid and base production routes. Each route links to its dedicated article for full process detail.

### Sulfuric Acid — Contact Process

1. Burn molten sulfur in dry air: S + O₂ → SO₂ at 1000-1100°C. Gas composition: 7-10% SO₂, 11-14% O₂, balance N₂.
2. Cool the gas to 400-450°C in a waste heat boiler (generates steam).
3. Pass over V₂O₅ catalyst beds (typically 3-4 beds) at 400-450°C: 2SO₂ + O₂ → 2SO₃. Inter-bed cooling maintains the temperature window. Conversion: 97-99.5% with double absorption.
4. Absorb SO₃ in 98% H₂SO₄ (not water — SO₃ + H₂O is violently exothermic and creates acid mist). Formation of oleum (H₂S₂O₇) at 20-65% free SO₃.
5. Dilute oleum with water or dilute acid to the target concentration (93%, 96%, or 98%).

See [Mineral Acid Production](acids.md) for full detail including the lead chamber alternative.

### Nitric Acid — Ostwald Process

1. Catalytically oxidize ammonia: 4NH₃ + 5O₂ → 4NO + 6H₂O over Pt-Rh gauze at 850-950°C. Air-NH₃ mixture at 9-12% NH₃ (below 15% lower explosive limit).
2. Cool gas; NO spontaneously oxidizes: 2NO + O₂ → 2NO₂ below 150°C.
3. Absorb NO₂ in water counter-currently at 4-10 bar: 3NO₂ + H₂O → 2HNO₃ + NO. Product: 55-68% HNO₃.

See [Ammonia Production](ammonia.md) and [Mineral Acid Production](acids.md) for full detail.

### Soda Ash — Solvay Process

1. Dissolve NaCl in water to saturated brine; purify by precipitation of Ca²⁺ (with Na₂CO₃) and Mg²⁺ (with NaOH).
2. Absorb NH₃ gas into the purified brine to form ammoniated brine.
3. Pass ammoniated brine counter-current to CO₂ gas in a carbonation tower: NaCl + NH₃ + CO₂ + H₂O → NaHCO₃↓ + NH₄Cl. Bicarbonate precipitates at 27-35°C.
4. Filter and calcine NaHCO₃ at 175-200°C: 2NaHCO₃ → Na₂CO₃ + CO₂ + H₂O. Recycle CO₂ to the carbonation tower.
5. Recover NH₃ from the NH₄Cl filtrate by reaction with lime (CaO) in a distillation still: 2NH₄Cl + CaO → 2NH₃ + CaCl₂ + H₂O. Recycle NH₃ to step 2.

See [Alkali Production](alkalis.md) for full detail.

### Caustic Soda — Chlor-Alkali Electrolysis

1. Purify saturated brine (300-320 g/L NaCl) to <20 ppb Ca+Mg for membrane cells.
2. Electrolyze in membrane or diaphragm cells: 2NaCl + 2H₂O → Cl₂ + H₂ + 2NaOH at 80-90°C.
3. Collect Cl₂ from the anode (dry with H₂SO₄), H₂ from the cathode, and 30-33% NaOH from the catholyte.
4. Evaporate caustic to 50% concentration if required.

See [Chlor-Alkali Process](chlor-alkali.md) for full detail.

## Quantitative Parameters

| Parameter | H₂SO₄ (Contact) | H₂SO₄ (Lead Chamber) | HNO₃ (Ostwald) | HCl (Direct Synthesis) |
|-----------|-----------------|---------------------|----------------|----------------------|
| Reaction temperature | 400-450°C (converter) | 50-80°C (chambers) | 850-950°C (oxidation), 4-10 bar (absorption) | 400-500°C (burner) |
| Product concentration | 96-98% H₂SO₄ | 62-70% H₂SO₄ | 55-68% HNO₃ | 31-37% HCl |
| Catalyst | V₂O₅ on silica | Nitrogen oxides (NOₓ) | Pt-Rh gauze (90/10) | None (direct combination) |
| Catalyst life | 5-10 years | Continuous gas recycle | 0.5-2 years (Pt loss: 0.05-0.5 g/t HNO₃) | N/A |
| Conversion efficiency | 97-99.5% (double absorption) | 85-90% | 95-98% (NH₃→NO) | >99% |
| Energy consumption | 60-100 kWh/t H₂SO₄ | 20-40 kWh/t (lower temp) | ~1 MWh/t HNO₃ (net exporter with waste heat) | 2.0-2.5 MWh/t HCl |

| Parameter | Na₂CO₃ (Solvay) | NaOH (Chlor-Alkali) | NaOH (Lime-Soda) | K₂CO₃ (Potash) |
|-----------|-----------------|---------------------|-------------------|----------------|
| Reaction temperature | 27-35°C (carbonation), 175-200°C (calcine) | 80-90°C (cell) | 80-90°C (causticizer) | Leach at ambient, evaporate at 100°C |
| Product purity | >99.2% Na₂CO₃ | 30-50% NaOH solution | 10-15% NaOH (dilute) | 85-95% K₂CO₃ |
| Chemical recovery | >70% NH₃ recycled | N/A (electrolytic) | 85-90% Na₂CO₃→NaOH conversion | N/A (leaching) |
| Energy consumption | 0.5-0.8 MWh/t Na₂CO₃ | 2,100-2,800 kWh/t NaOH | 0.3-0.5 MWh/t NaOH + steam | 0.2-0.5 MWh/t (evaporation) |
| Feedstock ratio | 1.5 t NaCl + 1.3 t limestone per t Na₂CO₃ | 1.7 t NaCl + 2.0 t H₂O per t NaOH | 1.3 t Na₂CO₃ + 0.8 t CaO per t NaOH | ~4-8 t wood ash per t K₂CO₃ |

## Scaling Notes

- **Bench scale**: Laboratory glassware produces 0.5-5 kg/batch of acids or alkalis. Sufficient for process demonstration and reagent preparation. Lead chamber process is demonstrable in a single 10-L glass vessel.
- **Pilot scale**: 50-500 kg/day. A single Solvay carbonation column or a small contact process converter with one catalyst bed. Validates material balances and chemical recovery cycles.
- **Production scale**: 50-1,000+ tonnes/day. Contact process plants of 500-2,000 t H₂SO₄/day are standard. Solvay plants of 200-1,000 t Na₂CO₃/day. Chlor-alkali plants of 100-500 t Cl₂/day.

Key scaling bottlenecks:
- **Sulfuric acid**: Heat removal in the SO₂→SO₃ converter dominates scale. Large converters use multiple catalyst beds with inter-bed cooling. Acid-resistant brick and lead lining limit vessel size.
- **Soda ash**: Ammonia recovery still is the largest equipment item. The Solvay process requires ~3 m³ cooling water per tonne Na₂CO₃ — water availability limits plant scale in arid regions.
- **Chlor-alkali**: DC power supply is the primary scale driver. A 100,000 t/year plant draws ~50 MW continuously. Brine purification to ppb hardness scales nonlinearly — ion exchange resin volume increases faster than throughput.
- **Minimum economic scale**: H₂SO₄ contact process is economic at 50-100 t/day. Below that, the lead chamber process is competitive. Solvay soda ash requires 200+ t/day to justify ammonia recovery infrastructure. Below that, Trona ore mining (natural Na₂CO₃) or potash are more economic.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| H₂SO₄ converter SO₂ conversion below 97% | V₂O₅ catalyst poisoned by arsenic, chlorine, or fluorine in feed gas; catalyst bed temperature outside 400-450°C window | Purify feed gas: remove As by electrostatic precipitator, halogens by scrubbing; verify catalyst bed inlet temperature is 420-440°C; replace poisoned catalyst |
| Lead chamber acid strength below 60% | Insufficient NOₓ circulation or chamber temperature too high (reduces NO₂ absorption) | Increase NOₓ gas feed rate; spray-cool chambers to maintain 50-70°C; check Gay-Lussac tower for NOₓ loss |
| Solvay NaHCO₃ precipitation yield below 65% | Ammonia concentration in brine too low; CO₂ absorption rate insufficient; carbonation temperature above 40°C | Verify NH₃ absorption saturator is delivering 85-90 g NH₃/L brine; check CO₂ compressor discharge pressure (target 2-3 atm); reduce cooling water temperature to maintain 27-35°C in carbonation tower |
| Chlor-alkali cell voltage rising above baseline | Membrane fouling from Ca/Mg hardness above 20 ppb; or electrode coating degradation | Check brine purification: Ca+Mg must be <20 ppb for membrane cells; regenerate ion exchange resin; inspect DSA anode coating — replace if active layer visibly eroded |
| HNO₃ absorption column tail gas NOₓ above 200 ppm | Insufficient absorption pressure; column temperature too high; NO oxidation too slow | Increase absorption pressure to 4-10 bar; verify column cooling water flow (maintain 20-30°C); add molecular sieve or extended absorption section; consider catalytic NOₓ destruction |
| Caustic soda product contains >0.5% NaCl | Diaphragm cell inherently produces salt-contaminated caustic; or membrane cell has pinhole leak | For diaphragm cells: evaporate and crystallize out NaCl (50% caustic contains ~1% NaCl); for membrane cells: inspect membrane with backlight for pinholes, replace damaged sheets |
| HCl product appears yellow-green | Dissolved chlorine contamination from excess Cl₂ in synthesis burner; or iron contamination from corroded steel piping | Adjust H₂:Cl₂ feed ratio to 1.00-1.05:1 (slight H₂ excess prevents free Cl₂); replace steel piping with glass or PVC; verify burner temperature is 400-500°C for complete reaction |

## Safety

- **Sulfuric acid**: Concentrated H₂SO₄ (98%) causes severe thermal and chemical burns. Always add acid to water. Heat of dilution: 880 kJ/kg. PPE: face shield, neoprene gloves, rubber apron. Spill: contain with sand or vermiculite, neutralize with lime or soda ash. IDLH: 15 mg/m³.
- **Nitric acid**: Powerful oxidizer. Contact with organics (paper, wood, solvents) causes spontaneous fire. Toxic NO₂ fumes evolve on decomposition or contact with metals. Store in aluminum (concentrated) or glass. PPE: acid splash goggles, nitrile gloves, acid-resistant apron, respiratory protection if fuming. IDLH: 25 ppm.
- **Hydrochloric acid**: HCl gas irritates respiratory tract at 5 ppm. Concentrated acid (37%) fumes in moist air. Scrub all vent gases through NaOH solution. Store in rubber-lined steel, glass, PVC, or polypropylene. PPE: face shield, PVC gloves and apron. IDLH: 50 ppm.
- **Hydrofluoric acid**: Uniquely lethal — penetrates skin, binds tissue calcium and magnesium causing deep necrosis and cardiac arrest. Burns involving >5% body area or concentrated HF are life-threatening. Calcium gluconate gel (2.5%) must be available at all HF work stations. Immediate application to skin contact areas prevents systemic toxicity. PPE: full acid splash suit, face shield, neoprene or butyl rubber gloves (double-gloved). IDLH: 30 ppm. See [Mineral Acid Production](acids.md) for detailed HF safety protocols.
- **Caustic soda (NaOH)**: 30-50% NaOH causes severe chemical burns that penetrate tissue. Eye contact with 50% NaOH risks permanent blindness within seconds. Emergency shower and eyewash mandatory at all caustic handling points. 50% NaOH freezes at 12°C — heated storage requires thermal insulation and trace heating. PPE: full-length chemical splash suit, face shield, neoprene gloves and boots.
- **Ammonia** (for Ostwald acid and Solvay alkali): IDLH 300 ppm. Liquid ammonia causes frostbite and chemical burns. See [Ammonia Production](ammonia.md) for detailed protocols.
- **Chlorine** (for chlor-alkali NaOH and HCl synthesis): IDLH 10 ppm. Extremely toxic by inhalation. See [Chlor-Alkali Process](chlor-alkali.md) for detailed protocols.

### Emergency Procedures

- Acid splash on skin: immediately flush with copious water for 15 minutes minimum. Remove contaminated clothing. For HF exposure, apply calcium gluconate gel immediately and seek emergency medical attention.
- Acid in eyes: use eyewash station for 15 minutes minimum, holding eyelids open. Seek medical attention.
- Large acid spill: contain with sand or acid spill kit. Do NOT neutralize concentrated acid with base directly (violent exotherm). Absorb first, then neutralize residual with lime or soda ash.
- NO₂ or Cl₂ gas release: evacuate downwind. Activate emergency scrubber (caustic circulation). Self-contained breathing apparatus for response team.

## Quality Control

### Acceptance Criteria

| Product | Concentration | Key Impurity Limits | Test Method |
|---------|--------------|---------------------|-------------|
| H₂SO₄ (commercial) | 93%, 96%, or 98% | Fe <50 ppm, As <1 ppm, Cl <10 ppm | Titration with NaOH (normality); ICP for metals |
| HNO₃ (commercial) | 55-68% | HCl <5 ppm, H₂SO₄ <10 ppm, Cl <5 ppm | Titration; specific gravity (1.40 ≈ 68%) |
| HCl (commercial) | 31-37% | Fe <10 ppm, free Cl₂ <0.003%, SO₄ <50 ppm | Titration with NaOH; iodometric for free Cl₂ |
| NaOH (commercial) | 30% or 50% | NaCl <0.1% (membrane), <1.5% (diaphragm); Fe <10 ppm | Titration; gravimetric for NaCl |
| Na₂CO₃ (commercial) | >99.2% Na₂CO₃ | NaCl <0.5%, Fe₂O₃ <0.004%, insoluble <0.05% | Acidimetric titration; gravimetric for insolubles |
| HF (commercial) | 40%, 48%, or 70% | H₂SiF₆ <0.5%, H₂SO₄ <0.05%, Fe <5 ppm | Acidimetric titration; gravimetric for sulfate |

### Sampling Protocol

- Tank truck or rail car delivery: sample from top, middle, and bottom of vessel. Three 500 mL samples in acid-resistant bottles.
- Batch production: sample every 2-4 hours during steady-state. Analyze concentration and impurity panel.
- On-line monitoring: continuous density measurement for H₂SO₄ and NaOH concentration. pH probes for dilute acid/base streams.

### Field Tests

- **Sulfuric acid concentration by density**: 98% H₂SO₄ has specific gravity 1.84 at 20°C. Hydrometer reading gives concentration to ±0.5%.
- **Caustic soda concentration by density**: 50% NaOH has specific gravity 1.53 at 20°C.
- **Acid-base neutralization**: titrate 10 mL sample with 1 M NaOH or HCl using phenolphthalein or methyl orange indicator. Calculate normality from volume consumed.

## Variations and Alternatives

| Route | Product | Advantages | Disadvantages | When to Use |
|-------|---------|-----------|---------------|-------------|
| Contact process (V₂O₅) | H₂SO₄ 96-98% | High purity, high concentration, efficient | Requires V₂O₅ catalyst and clean SO₂ feed | Standard industrial route |
| Lead chamber (NOₓ gas) | H₂SO₄ 62-70% | No vanadium needed, tolerates impure SO₂ | Lower concentration, NOₓ emissions | Bootstrap alternative before V₂O₅ available |
| Ostwald (NH₃ oxidation) | HNO₃ 55-68% | High yield, net energy exporter | Requires ammonia feedstock and Pt-Rh gauze | Standard route post-Haber-Bosch |
| Saltpeter distillation | HNO₃ 90-95% | Simple equipment (retort) | Limited by nitrate deposits; batch process | Bootstrap or when nitrate deposits exist |
| Solvay process | Na₂CO₃ >99% | Cheap feedstock, high purity | Complex plant, ammonia recovery required | Standard industrial route |
| Trona ore mining | Na₂CO₃ (natural) | No chemical plant needed | Requires natural Na₂CO₃ deposits | Where Trona deposits exist |
| Chlor-alkali (membrane) | NaOH 30-50% + Cl₂ + H₂ | Co-products, high purity | Energy-intensive, requires brine purification | Standard electrochemical route |
| Lime-soda causticization | NaOH 10-15% | No electricity, simple equipment | Dilute product, lower purity | Bootstrap before electrolysis available |
| Wood ash leaching | K₂CO₃ 85-95% | No industrial plant needed | Land-intensive (4-8 t wood per t K₂CO₃) | Artisanal scale; glass and soap making |

### Regional Adaptations

- **Arid regions without salt deposits**: Soda ash from Trona ore (natural Na₂CO₃·NaHCO₃·2H₂O) where deposits exist (Green River, Wyoming; Lake Magadi, Kenya). Avoids the Solvay process entirely.
- **Coastal locations with cheap electricity**: Chlor-alkali from seawater brine. Co-located with chlorine consumers (PVC, pulp bleaching, water treatment) to minimize Cl₂ transport.
- **Regions with sulfur deposits**: Direct sulfur burning for H₂SO₄. Regions without sulfur: pyrite roasting or smelter off-gas recovery (non-ferrous metal smelters produce large SO₂ streams).

## References

- [Mineral Acid Production](acids.md) — detailed processes for H₂SO₄, HCl, HNO₃, HF, H₃PO₄, including materials of construction and troubleshooting
- [Alkali Production](alkalis.md) — detailed Solvay, Leblanc, lime-soda causticization, and potash processes
- [Ammonia Production](ammonia.md) — Haber-Bosch enabling Ostwald HNO₃ and Solvay soda ash
- [Electrolysis](electrolysis.md) — chlor-alkali process for NaOH, Cl₂, and H₂ co-production
- [Chlor-Alkali Process](chlor-alkali.md) — detailed membrane, diaphragm, and mercury cell processes
- [Iron & Steel](../metals/iron-steel.md) — pickling acid consumption in steel processing
- [Basic Semiconductor Devices](../silicon/basic-devices.md) — HF and H₂SO₄ in wafer processing
- [Potash](potash.md) — wood-ash potash production detail
- [Soap](soap.md) — caustic soda and soda ash in saponification

---
*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
