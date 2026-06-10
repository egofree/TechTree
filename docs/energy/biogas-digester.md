# Biogas Digester

> **Node ID**: energy.biomass-energy.biogas-digester
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.biomass-energy`](biomass-energy.md), [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.fermentation`](../chemistry/fermentation.md)
> **Enables**: [`energy.electricity`](electricity.md), [`chemistry.ammonia`](../chemistry/ammonia.md)
> **Timeline**: Years 5-20
> **Outputs**: biogas, digestate_fertilizer
> **Critical**: No — biogas provides cooking gas and small-scale electricity from waste, but is supplementary to other energy sources

## Overview

A biogas digester (anaerobic digester) is a sealed vessel in which organic material decomposes in the absence of oxygen, producing a gas mixture of approximately 60% methane (CH₄) and 35-40% carbon dioxide (CO₂). Methanogenic archaea — microorganisms that thrive in oxygen-free environments at 30-60°C — perform the conversion in four biochemical stages: hydrolysis (complex organics → simple sugars, amino acids, fatty acids), acidogenesis (simple molecules → volatile fatty acids), acetogenesis (fatty acids → acetic acid + H₂ + CO₂), and methanogenesis (acetic acid + H₂ + CO₂ → CH₄ + CO₂).

Biogas digesters occupy a unique niche in the bootstrap chain: they convert waste streams (animal manure, food scraps, sewage, crop residues) into both energy and fertilizer without requiring any fuel input. Every livestock operation generates manure; every kitchen generates food waste. A digester captures the methane these wastes would release anyway, providing 1-3 m³ of cooking gas per day from a family-scale unit while producing a mineralized digestate with 20-40% more plant-available nitrogen than raw manure. For communities without access to petroleum fuels or grid electricity, biogas provides the first gaseous fuel available — years before coal gas or natural gas infrastructure. The digester is also a sanitation improvement: thermophilic operation (50-60°C) achieves >99.9% pathogen reduction in human and animal waste.

The key operating parameters are: temperature (30-40°C for mesophilic, 50-60°C for thermophilic), pH (6.8-7.5), carbon-to-nitrogen ratio (20-30:1 in the feedstock), and hydraulic retention time (20-40 days for mesophilic). Biogas calorific value: 21-24 MJ/m³ (about 60% of natural gas). Each cubic meter of digester volume produces 0.3-0.6 m³ of biogas per day at steady state. Cross-reference: [Biomass Energy](biomass-energy.md) for the full range of biomass conversion pathways; [Fermentation](../chemistry/fermentation.md) for biochemical processing fundamentals.

Biogas does have limitations that prevent it from serving as a primary industrial energy source. The low energy density (21-24 MJ/m³ vs. 36-40 MJ/m³ for natural gas) means large volumes are needed for significant power output. The 20-40 day retention time makes the process slow to respond to demand changes. And the daily feeding requirement means the digester needs consistent labor — it is not a "set and forget" system. These constraints make biogas best suited for steady, baseline energy production from waste streams, supplemented by faster-responding energy sources like [photovoltaics](photovoltaics.md) or [steam engines](steam-engine.md) for peak loads.

## Prerequisites

- [Brick or concrete construction materials](../ceramics/kilns.md) — for digester walls
- [Steel plate](../metals/iron-steel.md) — for gas holder
- [Cement and sand](../chemistry/cement.md) — for mortar and waterproofing
- [Animal manure or food waste](biomass-energy.md) — regular feedstock supply
- [Water supply](../water/basic-treatment.md) — for slurry mixing
- Basic masonry skills — bricklaying, plastering, waterproof coating application
- Daily labor commitment — 30-60 minutes for feeding, mixing, and monitoring

## Bill of Materials

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

## Process Description

### Fixed-Dome Digester

**Principle**: Organic slurry decomposes anaerobically inside a sealed underground brick dome. As bacteria produce biogas, pressure builds in the dome, displacing digestate into the outlet chamber. When gas is drawn off for cooking or lighting, pressure drops and digestate flows back. The dome is permanently gas-tight — there are no moving parts in the gas collection system.

**Prerequisites**:
- [Brick and cement construction](../ceramics/kilns.md) capability
- [Waterproof cement coating](../chemistry/cement.md) materials
- Excavation tools (shovel, pick, wheelbarrow)
- Steel pipe and valve [fabrication](../metals/iron-steel.md)

**Construction**:

1. **Excavate the pit**: Dig a cylindrical pit 3 m diameter × 2 m depth (approximately 14 m³ total, 6-8 m³ working volume). Slope the bottom slightly toward the outlet for slurry flow. Compact the base soil.

2. **Build the walls**: Lay brick walls in cement mortar (1:4 cement:sand ratio) from pit floor to 200 mm above ground level. Wall thickness: one brick (200 mm) for small digesters, two bricks (400 mm) for larger. Keep walls plumb and joints fully filled — the digester must be gas-tight.

3. **Construct the inlet chamber**: Build a vertical channel (300-400 mm wide) on one side of the digester, from ground level down to near the bottom. This is where fresh slurry enters. The inlet pipe should extend to within 300 mm of the digester floor to ensure fresh feed reaches the bottom.

4. **Construct the outlet (displacement) chamber**: Build a wider chamber (600-800 mm) on the opposite side. The outlet overflow level determines the gas pressure — higher outlet = higher gas pressure (typically 40-80 cm water gauge, 4-8 kPa). The outlet also serves as the access point for removing spent digestate.

5. **Cast the dome roof**: Form a hemispherical dome over the digester using ferrocement technique — layers of steel mesh embedded in rich cement mortar (1:3 cement:sand, 30-40 mm thick). The dome must be perfectly gas-tight. Apply waterproof cement slurry (neat cement with sodium silicate) on both interior and exterior surfaces. Cure for 7 days keeping damp.

6. **Install the gas outlet**: Cast a 25 mm steel pipe into the crown of the dome, threading the upper end for a valve connection. Seal the pipe-to-dome joint carefully — this is a common leak point.

7. **Connect the H₂S filter**: Fill a small steel drum with iron oxide-impregnated wood shavings (iron sponge). Connect between the digester gas outlet and the gas appliance. H₂S in raw biogas corrodes engine parts and produces sulfuric acid — the filter removes it by converting H₂S to iron sulfide.

8. **Install the gas delivery pipe**: Run 25 mm galvanized steel pipe from the H₂S filter to the point of use (kitchen burner, lamp, engine). Slope the pipe toward the digester at 10 mm/m so condensate drains back. Install a drip leg (low point with drain valve) at the lowest point of the piping.

9. **Waterproof the interior**: Apply two coats of neat cement slurry (cement mixed with water to a paintable consistency) to all interior brick and concrete surfaces. This seals the pores and makes the digester gas-tight. Test by filling with water — the level should not drop more than 10 mm in 24 hours.

**Calibration**:

1. Fill the completed digester with water before adding any feedstock. Monitor the water level for 24 hours — drop should be <10 mm. If the level drops, locate and repair the leak.
2. After filling with slurry and producing gas, close all gas valves and monitor gas pressure for 4 hours. Pressure should remain constant — any drop indicates a gas leak. Check with soapy water at all joints and fittings.
3. Insert a thermometer 300 mm into the slurry through a capped pipe. Daily temperature: target 30-40°C (mesophilic). Below 20°C, methanogenic bacteria become inactive and gas production stops.
4. Test slurry pH weekly using litmus paper or a pH meter. Target: 6.8-7.5. Below 6.5 indicates acid accumulation — stop feeding and add lime (CaCO₃) to raise pH above 7.0 before resuming.
5. Measure daily gas volume with a gas meter or by measuring gas holder displacement. Target: 0.3-0.6 m³ biogas per m³ digester volume per day at steady state (reached 30-60 days after initial loading).

**Expected performance**: Biogas yield 0.3-0.6 m³ per m³ digester volume per day. Methane content 55-70% by volume. Gas pressure 4-8 kPa (40-80 cm water gauge). Digester lifetime 15-30 years. Cooking gas equivalent: 1 m³ biogas ≈ 0.5 kg LPG ≈ 0.6 liters kerosene.

**Applications**: Household cooking (1-3 m³/day fuels 2-4 hours of cooking), gas lighting, small engine fuel for electricity generation (see [Electricity Generation](electricity.md)), and digestate as fertilizer for agriculture.

**Strengths**:
- No moving parts in gas collection — maintenance limited to valve and pipe inspection
- Underground construction provides natural insulation, maintaining stable slurry temperature year-round
- 15-30 year service life with no steel corrosion (all masonry construction)
- Lower material cost than floating-bell design (no steel drum or water seal trough required)

**Weaknesses**:
- Gas pressure varies with stored gas volume (4-8 kPa range) — appliances must tolerate pressure swings
- Gas-tightness depends on construction quality — a leaky dome requires draining the entire digester to repair
- No visual indication of gas volume — must rely on a pressure gauge rather than direct observation
- Construction requires skilled masonry for the hemispherical dome; poor workmanship causes chronic gas leaks

### Floating-Bell (Gas Holder) Variation

**Principle**: Identical anaerobic digestion process, but instead of a fixed dome, gas collects under a cylindrical steel drum (the bell) that floats in a water seal trough. As gas accumulates, the bell rises; as gas is consumed, it falls. The bell provides constant gas pressure determined by its weight divided by cross-section area.

**Construction**: Weld a cylindrical steel drum (1.0-1.5 m diameter × 0.8-1.2 m height) with an open bottom and a domed top with gas outlet pipe. The drum floats in a water seal trough around the digester opening, rising as gas accumulates and falling as gas is consumed. Paint exterior with rust-preventative paint. Gas pressure is constant at the weight of the bell divided by its cross-section area (typically 3-8 cm water gauge).

**Strengths**:
- Visual indication of gas volume (bell height shows remaining gas)
- Constant gas pressure regardless of gas volume
- Easier to identify and repair gas leaks (above-ground bell)
- Lower construction precision required than fixed-dome (no need for gas-tight dome)

**Weaknesses**:
- Steel bell corrodes — requires annual painting with rust-preventative coating
- Water seal can evaporate in hot climates — requires periodic topping up
- Above-ground component is vulnerable to physical damage
- Higher cost than fixed-dome due to steel drum fabrication

## Quantitative Parameters

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

### Feedstock Yields by Type

| Feedstock | Biogas Yield (m³/kg VS) | Methane Content (%) | C:N Ratio | Notes |
|-----------|--------------------------|---------------------|-----------|-------|
| Cattle manure | 0.20-0.30 | 55-60 | 18-25:1 | Reliable baseline feedstock; low VS content requires large volumes |
| Pig manure | 0.30-0.50 | 60-65 | 12-20:1 | Higher yield than cattle; watch for ammonia accumulation |
| Poultry manure | 0.35-0.60 | 60-65 | 8-12:1 | High nitrogen — must co-digest with carbon-rich material to reach C:N 20-30:1 |
| Food waste | 0.40-0.60 | 55-70 | 15-20:1 | Highest per-kg yield; grind to <10 mm particles for rapid hydrolysis |
| Crop residues (straw) | 0.20-0.35 | 55-60 | 60-100:1 | Too high C:N alone — co-digest with manure. Pre-treat with NaOH to improve digestibility |
| Grass clippings | 0.30-0.45 | 55-60 | 15-25:1 | Seasonal availability; compost briefly to reduce lignin before feeding |
| Sewage sludge | 0.30-0.50 | 60-65 | 6-10:1 | Requires co-digestion; pathogen kill requires thermophilic operation or post-treatment |

VS = volatile solids (organic fraction). Total solids (TS) of typical feedstocks: manure 15-25%, food waste 20-35%, crop residues 80-95%. Dilute high-TS feedstocks to 8-12% TS in the digester for proper mixing and bacterial activity.

The C:N ratio is the most common feedstock quality problem. Cattle manure at 18-25:1 is close to ideal. Poultry manure at 8-12:1 is too nitrogen-rich and will generate ammonia that inhibits methanogens. Crop residues at 60-100:1 are too carbon-rich, leading to nitrogen starvation of the bacterial population. Co-digestion — mixing high-nitrogen and high-carbon feedstocks — solves both problems simultaneously.

## Scaling Notes

| Scale | Digester Volume | Daily Feedstock | Gas Production | Primary Use | Estimated Cost |
|-------|----------------|-----------------|----------------|-------------|----------------|
| Household (1 family) | 4-8 m³ | 10-30 kg manure + water | 1-3 m³/day | Cooking (2-4 hours/day) | $200-800 (materials) |
| Small farm | 15-30 m³ | 50-150 kg mixed waste | 5-12 m³/day | Cooking + lighting + small engine | $1,000-3,000 |
| Community | 50-100 m³ | 200-500 kg mixed waste | 20-50 m³/day | Cooking cluster + engine-generator (3-10 kW) | $5,000-15,000 |
| Industrial | 500-5000 m³ | 2-20 tonnes/day | 200-2000 m³/day | Electricity generation (50-500 kW) | $50,000-500,000 |

Scaling is approximately linear: twice the volume produces twice the gas, provided the surface-to-volume ratio does not cause heat loss problems at larger scales. Insulate digesters larger than 30 m³ in temperate climates — the internal heat from bacterial activity alone is insufficient below 15°C ambient.

Minimum economic scale: a 4 m³ digester fed with manure from 3-5 cattle produces enough gas for one family's cooking needs. Below this, the labor of daily feeding and mixing exceeds the value of gas produced. In cold climates (<10°C winter ambient), insulation and supplemental heating (solar hot water or waste heat diversion) are mandatory additions that increase the minimum viable scale to 8-10 m³.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gas production stopped | Temperature dropped below 20°C | Insulate digester; add solar water heater to feed water; in cold climates, build underground where soil temperature is stable |
| Gas production stopped | pH dropped below 6.5 (sour digester) | Stop feeding immediately; add lime (CaCO₃) at 0.5-1.0 kg/m³ to raise pH above 7.0; resume feeding gradually at 50% rate |
| Low methane (<45%) | Excessive water in feedstock (dilute slurry) | Increase feedstock solids concentration to 8-12% TS; check for water leaks into digester |
| Foaming in digester | Overfeeding or high-fat content in feedstock | Reduce feed rate by 50%; dilute with water; avoid adding grease or oil in quantity |
| Gas leaks (pressure drops) | Cracked dome or pipe joint failure | Empty digester, locate cracks, repair with cement slurry; check all pipe joints with soapy water |
| Scum layer blocks gas release | Floating material (straw, fiber) forming mat | Install a manual stirrer (central shaft with paddles); or stir slurry by agitating inlet pipe weekly |
| Foul odor from digestate | Incomplete digestion (short retention time) | Increase retention time by reducing daily feed volume; check if digester is oversized for current feed rate |
| Digestate too wet (flows freely) | Over-dilution with water | Reduce water addition; target 8-12% total solids in influent slurry |

## Safety

- **Biogas explosion**: Biogas (55-70% CH₄) is explosive at 5-15% concentration in air. Never use open flames, welding, or spark sources near gas holders and piping. Ground all metal gas piping to prevent static discharge ignition. Install a flame arrestor (wire mesh or water seal) on the gas line between digester and appliances.
- **H₂S toxicity**: Raw biogas contains 100-3000 ppm H₂S. IDLH = 100 ppm (NIOSH). The iron oxide filter must be installed before any gas reaches occupied spaces. Ventilate gas holder enclosures. H₂S deadens the sense of smell at >100 ppm — lack of odor does NOT mean safe air.
- **Asphyxiation**: Biogas displaces oxygen. Do not enter an enclosed digester that has been sealed — it may contain lethal concentrations of CO₂ and CH₄ with insufficient O₂. Ventilate for 30+ minutes before entry. Use a gas detector or candle test (candle extinguished = do not enter).
- **Iron sponge fire hazard**: Spent iron oxide (iron sulfide) is pyrophoric — it can spontaneously ignite when exposed to air. Replace filter media in a well-ventilated area, moisten spent media with water before disposal. Never pile spent iron sponge — spread thinly outdoors.
- **Pathogen risk**: Mesophilic digesters (30-40°C) reduce but do not eliminate pathogens. Digestate may still contain E. coli, Salmonella, and helminth eggs. Wear gloves when handling. Apply to fields with minimum 30-day interval before harvest of crops consumed raw. Thermophilic operation (50-60°C) achieves greater pathogen kill (>99.9%) but is harder to maintain.
- **Scalding from slurry**: Fresh digestate exits at 30-60°C. Avoid skin contact. Wear waterproof boots and gloves when handling digestate or cleaning overflow channels.

## Quality Control

- **Gas composition**: Test with a combustible gas analyzer or simple flame test monthly. Blue flame = >50% methane. Yellow flame = low methane — investigate temperature, pH, and C:N ratio.
- **pH monitoring**: Weekly. Target 6.8-7.5. Use litmus paper (±0.5 pH unit accuracy, sufficient for digester monitoring) or a calibrated pH meter.
- **Digestate nutrient content**: Test annually for nitrogen (Kjeldahl method), phosphorus, and potassium. Well-digested manure digestate typically contains 1.5-2.5% total N, 0.5-1.5% P₂O₅, 1.0-2.0% K₂O on a dry-weight basis. Compare to raw manure: mineralization during digestion increases plant-available nitrogen by 20-40%.
- **Retention time verification**: Add a dye tracer (non-toxic food coloring) to the inlet. Measure time until dye appears at the outlet. Actual HRT should match design HRT (20-40 days). Short-circuiting (dye appears in <10 days) indicates dead zones — install baffles.
- **Gas holder integrity**: Monthly visual inspection for corrosion (steel bell) or UV cracking (flexible membrane). Paint steel gas holders annually with rust-preventative coating.

## Variations and Alternatives

### Continuous vs. Batch Operation

**Continuous (plug-flow or stirred-tank)**: Feed slurry daily at one end; digestate overflows at the other. Gas production is steady. The fixed-dome and floating-bell designs described above are continuous systems. Hydraulic retention time (HRT) of 20-40 days means the active digester volume must be 20-40× the daily feed volume.

**Batch**: Load the digester, seal it, and wait 30-60 days for complete digestion. Gas production peaks in weeks 2-4 and tapers off. Simpler to build but requires multiple digesters operated in staggered rotation for steady gas output. Common in agricultural settings where seasonal crop residues are available in bulk. Minimum 3 batch digesters in staggered rotation for continuous gas supply.

### Covered Lagoon

For large-scale operations (livestock farms with >500 cattle): an existing manure lagoon covered with a flexible HDPE membrane captures biogas naturally produced by anaerobic decomposition. No heating, no mixing — relies on ambient temperature (gas production ceases below 15°C). Gas yield: 0.10-0.20 m³/m² of lagoon surface per day. Low capital cost but seasonal and low-efficiency. Suitable for warm climates only.

### Tubular (Bag) Digester

A long cylindrical polyethylene or PVC bag (3-5 m long, 1-2 m diameter) with inlet at one end and outlet at the other. The cheapest design (~$50-100 for materials). Unheated, relying on ambient temperature. Lifetime: 2-5 years (UV degradation). Widely adopted in tropical developing countries (Vietnam, Cambodia, Colombia) for household cooking gas. Gas production: 0.5-1.5 m³/day from 10-20 kg manure. Not recommended for cold climates — no heating mechanism and poor insulation.

## References

- [Biomass Energy](biomass-energy.md) — full coverage of anaerobic digestion, biogas yields by feedstock, and gasification
- [Gasifier](gasifier.md) — thermochemical gasification for dry biomass
- [Heat Engines](engine.md) — engines modified for biogas fuel
- [Electricity Generation](electricity.md) — engine-generator sets for biogas electricity
- [Fuels](fuels.md) — comparative fuel properties
- [Fermentation](../chemistry/fermentation.md) — biochemical conversion processes
- [Ammonia Production](../chemistry/ammonia.md) — nitrogen recovery from digestate
- [Water Treatment](../water/basic-treatment.md) — digester effluent treatment

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Energy](./index.md) • [All Domains](../../index.md)*
