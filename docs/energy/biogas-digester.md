# Biogas Digester

> **Node ID**: energy.biomass-energy.biogas-digester
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.biomass-energy`](biomass-energy.md), [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.fermentation`](../chemistry/fermentation.md)
> **Enables**: [`energy.electricity`](electricity.md), [`chemistry.ammonia`](../chemistry/ammonia.md)
> **Timeline**: Years 5-20
> **Outputs**: biogas, digestate_fertilizer
> **Critical**: No — biogas provides cooking gas and small-scale electricity from waste, but is supplementary to other energy sources

## Principle

A biogas digester (anaerobic digester) is a sealed vessel in which organic material decomposes in the absence of oxygen, producing a gas mixture of approximately 60% methane (CH₄) and 35-40% carbon dioxide (CO₂). Methanogenic archaea — microorganisms that thrive in oxygen-free environments at 30-60°C — perform the conversion in four biochemical stages: hydrolysis (complex organics → simple sugars, amino acids, fatty acids), acidogenesis (simple molecules → volatile fatty acids), acetogenesis (fatty acids → acetic acid + H₂ + CO₂), and methanogenesis (acetic acid + H₂ + CO₂ → CH₄ + CO₂).

The key operating parameters are: temperature (30-40°C for mesophilic, 50-60°C for thermophilic), pH (6.8-7.5), carbon-to-nitrogen ratio (20-30:1 in the feedstock), and hydraulic retention time (20-40 days for mesophilic). Biogas calorific value: 21-24 MJ/m³ (about 60% of natural gas). Each cubic meter of digester volume produces 0.3-0.6 m³ of biogas per day at steady state.

## Prerequisites

- [Brick or concrete construction materials](../ceramics/kilns.md) — for digester walls
- [Steel plate](../metals/iron-steel.md) — for gas holder
- [Cement and sand](../chemistry/cement.md) — for mortar and waterproofing
- [Animal manure or food waste](biomass-energy.md) — regular feedstock supply
- [Water supply](../water/basic-treatment.md) — for slurry mixing

## Materials

### Family-Scale Digester (6 m³, fixed-dome type)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Brick](../ceramics/kilns.md) | 2000-3000 pcs | Standard fired clay brick, 200 × 100 × 65 mm | [Ceramics](../ceramics/kilns.md) | Concrete block, ferrocement |
| [Cement](../chemistry/cement.md) | 500-800 kg | Portland cement, OPC 42.5 | [Chemistry](../chemistry/cement.md) | Lime mortar (more porous) |
| [Sand](../chemistry/index.md) | 1500-2500 kg | Clean building sand, river sand | [Chemistry](../chemistry/index.md) | — |
| [Steel plate (gas holder)](../metals/iron-steel.md) | 15-25 kg | 3 mm thick, welded into dome or floating bell | [Iron & Steel](../metals/iron-steel.md) | Flexible PVC membrane (limited life) |
| [PVC pipe (inlet/outlet)](../polymers/thermoplastics.md) | 6-10 m | 110 mm OD, standard wall | [Polymers](../polymers/thermoplastics.md) | Clay pipe (higher leakage) |
| [Galvanized steel pipe (gas)](../metals/iron-steel.md) | 5-10 m | 25 mm OD, threaded fittings | [Iron & Steel](../metals/iron-steel.md) | PVC pipe (lower pressure rating) |
| [Brass or steel valves](../metals/copper-bronze.md) | 2-3 pcs | 25 mm, gas-rated | [Metals](../metals/index.md) | Wooden plug (not recommended) |
| [Waterproof cement additive](../chemistry/index.md) | 5-10 kg | Sodium silicate or bitumen coating | [Chemistry](../chemistry/index.md) | Plastic sheet (less permanent) |
| [Iron oxide chips (H₂S filter)](../chemistry/index.md) | 5-10 kg | Wood shavings coated with iron oxide | [Chemistry](../chemistry/index.md) | Activated carbon (expensive) |

## Construction Steps

### Fixed-Dome Digester

1. **Excavate the pit**: Dig a cylindrical pit 3 m diameter × 2 m depth (approximately 14 m³ total, 6-8 m³ working volume). Slope the bottom slightly toward the outlet for slurry flow. Compact the base soil.

2. **Build the walls**: Lay brick walls in cement mortar (1:4 cement:sand ratio) from pit floor to 200 mm above ground level. Wall thickness: one brick (200 mm) for small digesters, two bricks (400 mm) for larger. Keep walls plumb and joints fully filled — the digester must be gas-tight.

3. **Construct the inlet chamber**: Build a vertical channel (300-400 mm wide) on one side of the digester, from ground level down to near the bottom. This is where fresh slurry enters. The inlet pipe should extend to within 300 mm of the digester floor to ensure fresh feed reaches the bottom.

4. **Construct the outlet (displacement) chamber**: Build a wider chamber (600-800 mm) on the opposite side. The outlet overflow level determines the gas pressure — higher outlet = higher gas pressure (typically 40-80 cm water gauge, 4-8 kPa). The outlet also serves as the access point for removing spent digestate.

5. **Cast the dome roof**: Form a hemispherical dome over the digester using ferrocement technique — layers of steel mesh embedded in rich cement mortar (1:3 cement:sand, 30-40 mm thick). The dome must be perfectly gas-tight. Apply waterproof cement slurry (neat cement with sodium silicate) on both interior and exterior surfaces. Cure for 7 days keeping damp.

6. **Install the gas outlet**: Cast a 25 mm steel pipe into the crown of the dome, threading the upper end for a valve connection. Seal the pipe-to-dome joint carefully — this is a common leak point.

7. **Connect the H₂S filter**: Fill a small steel drum with iron oxide-impregnated wood shavings (iron sponge). Connect between the digester gas outlet and the gas appliance. H₂S in raw biogas corrodes engine parts and produces sulfuric acid — the filter removes it by converting H₂S to iron sulfide.

8. **Install the gas delivery pipe**: Run 25 mm galvanized steel pipe from the H₂S filter to the point of use (kitchen burner, lamp, engine). Slope the pipe toward the digester at 10 mm/m so condensate drains back. Install a drip leg (low point with drain valve) at the lowest point of the piping.

9. **Waterproof the interior**: Apply two coats of neat cement slurry (cement mixed with water to a paintable consistency) to all interior brick and concrete surfaces. This seals the pores and makes the digester gas-tight. Test by filling with water — the level should not drop more than 10 mm in 24 hours.

### Floating-Bell (Gas Holder) Variation

10. **Fabricate the gas holder**: Weld a cylindrical steel drum (1.0-1.5 m diameter × 0.8-1.2 m height) with an open bottom and a domed top with gas outlet pipe. The drum floats in a water seal trough around the digester opening, rising as gas accumulates and falling as gas is consumed. Paint exterior with rust-preventative paint. Gas pressure is constant at the weight of the bell divided by its cross-section area (typically 3-8 cm water gauge).

## Calibration and Verification

1. **Water test**: Fill the completed digester with water before adding any feedstock. Monitor the water level for 24 hours — drop should be <10 mm. If the level drops, locate and repair the leak (re-mortar joints, apply additional waterproof coating).

2. **Gas tightness test**: After the digester is filled with slurry and producing gas, close all gas valves and monitor gas pressure for 4 hours. Pressure should remain constant — any drop indicates a gas leak. Check with soapy water at all joints and fittings.

3. **Temperature monitoring**: Insert a thermometer 300 mm into the slurry through a capped pipe. Daily temperature: target 30-40°C (mesophilic). Below 20°C, methanogenic bacteria become inactive and gas production stops.

4. **pH monitoring**: Test slurry pH weekly using litmus paper or a pH meter. Target: 6.8-7.5. Below 6.5 indicates acid accumulation (sour digester) — stop feeding and add lime (CaCO₃) to raise pH above 7.0 before resuming.

5. **Gas production**: Measure daily gas volume with a gas meter or by measuring gas holder displacement. Target: 0.3-0.6 m³ biogas per m³ digester volume per day at steady state (reached 30-60 days after initial loading).

6. **Gas quality (flame test)**: Biogas that supports a stable blue flame has >50% methane content. Below 45% methane — check temperature, C:N ratio, and retention time.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Biogas yield | 0.3-0.6 m³ per m³ digester volume per day |
| Methane content | 55-70% by volume |
| Calorific value | 21-24 MJ/m³ |
| Daily gas production (6 m³ digester) | 1.8-3.6 m³ biogas/day |
| Hydraulic retention time | 20-40 days (mesophilic) |
| Operating temperature | 30-40°C (mesophilic), 50-60°C (thermophilic) |
| Feedstock C:N ratio | 20-30:1 |
| pH | 6.8-7.5 |
| Gas pressure (fixed dome) | 4-8 kPa (40-80 cm water gauge) |
| Gas pressure (floating bell) | 3-8 kPa (constant) |
| Digester lifetime | 15-30 years (brick/concrete), 5-10 years (flexible membrane) |
| Cooking gas equivalent | 1 m³ biogas ≈ 0.5 kg LPG ≈ 0.6 liters kerosene |

## Strengths

- Converts waste (manure, food scraps) into energy and fertilizer simultaneously
- Continuous process — daily feeding produces steady gas output
- Simple construction with low-tech materials (brick, concrete, steel plate)
- Digestate has higher plant-available nitrogen than raw manure due to mineralization
- No fuel purchase required — uses waste that would otherwise decompose unproductively

## Weaknesses

- Requires consistent daily feeding — interrupted feeding causes process instability
- Temperature-sensitive — below 20°C, gas production stops (must insulate in cold climates)
- Biogas has low energy density (21-24 MJ/m³) compared to natural gas (36-40 MJ/m³)
- Slow process — 20-40 day retention time means slow response to increased demand
- H₂S in raw biogas corrodes engines and pipework if not filtered

## Safety

- **Biogas explosion**: Biogas (60% CH₄) is explosive at 5-15% concentration in air. Never use open flames, welding, or spark sources near gas holders and piping. Ground all metal gas piping to prevent static discharge ignition.
- **H₂S toxicity**: Raw biogas contains 100-3000 ppm H₂S. IDLH = 100 ppm. The iron oxide filter must be installed before any gas reaches occupied spaces. Ventilate gas holder enclosures.
- **Asphyxiation**: Biogas displaces oxygen. Do not enter an enclosed digester that has been sealed — it may contain lethal concentrations of CO₂ and CH₄ with insufficient O₂. Always ventilate before entry.
- **Iron sponge fire hazard**: Spent iron oxide (iron sulfide) is pyrophoric — it can spontaneously ignite when exposed to air. Replace filter media in a well-ventilated area, moisten spent media with water before disposal.
- **Pathogen risk**: Digestate may still contain pathogens (especially in mesophilic digesters). Wear gloves when handling. Apply to fields with minimum 30-day interval before harvest of crops consumed raw.

## See Also

- [Biomass Energy](biomass-energy.md) — full coverage of anaerobic digestion, biogas yields by feedstock, and gasification
- [Gasifier](gasifier.md) — thermochemical gasification for dry biomass
- [Heat Engines](engine.md) — engines modified for biogas fuel
- [Electricity Generation](electricity.md) — engine-generator sets for biogas electricity
- [Fuels](fuels.md) — comparative fuel properties
- [Fermentation](../chemistry/fermentation.md) — biochemical conversion processes
- [Ammonia Production](../chemistry/ammonia.md) — nitrogen recovery from digestate

---

*Part of the [Bootciv Tech Tree](../index.md) · [Energy](./index.md) · [All Domains](../index.md)*
