# Chemical Recovery & Solvent Regeneration

> **Node ID**: chemistry.chemical-recovery
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`Distillation`](distillation.md), [`Electrolysis`](electrolysis.md), [`Solvent Production`](solvents.md), [`Mineral Acids`](acids.md)
> **Enables**: [`Chemistry`](./index.md), [`Semiconductor Chemicals`](semiconductor-chemicals.md), [`Electronics`](../electronics/index.md)
> **Timeline**: Years 20-50+
> **Outputs**: recovered_solvents, regenerated_acids, recovered_catalysts, distilled_water
> **Critical**: No — reduces chemical consumption but does not enable new capabilities

## 1. Overview

Chemical recovery regenerates spent industrial chemicals — solvents, acids, catalysts, and process water — to a purity level suitable for reuse in manufacturing. This is distinct from waste treatment (see [Waste Management](../ehs/waste-management.md)), which converts hazardous waste into dischargeable effluent. Recovery asks: how do we make this useful again?

The economic case for chemical recovery strengthens as chemical production scales. A semiconductor fab consuming 5,000 tonnes/year of solvents has a powerful incentive to recover and reuse 90%+ of spent solvent rather than purchasing fresh stock and paying for disposal. At smaller scales, the calculation favors disposal — a settlement producing 10 liters/month of ethanol has no need for solvent recovery.

Three recovery mechanisms dominate: **distillation** (separating chemicals by boiling point), **membrane separation** (filtering by molecular size or charge), and **chemical regeneration** (reversing the reaction that consumed the chemical). This capability builds on existing distillation and electrolysis infrastructure — the recovery process adds separation stages to standard chemical plant equipment.

## 2. Prerequisites

### Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Spent chemicals | Solvents, acids, catalysts from industrial processes | Manufacturing process waste streams |
| Distillation column | Copper or steel, 2–10 m, packed with ceramic or steel packing | [Distillation](distillation.md) |
| Membranes | Ion exchange, ultrafiltration, or diffusion dialysis | [Chemistry](./index.md) |
| Heat source | Steam or direct heating at 60–300°C | [Energy](../energy/index.md) |
| Cooling water | 10–30 m³/hour per column | [Water Treatment](water-treatment.md) |

### Tools & Equipment

| Equipment | Purpose | Source |
|-----------|---------|--------|
| Fractional distillation column | Solvent purification by boiling point | [Distillation](distillation.md) |
| Heat exchangers | Energy recovery from hot streams | [Metals](../metals/index.md) |
| pH meter and conductivity meter | Process control | [Measurement](../measurement/index.md) |
| Storage tanks | Segregated collection of spent and recovered chemicals | [Metals](../metals/index.md) |
| Pumps and piping | Chemical transfer | [Gas Handling](../gas-handling/index.md) |

### Knowledge

- Distillation theory: boiling point, reflux ratio, number of theoretical plates
- Chemical compatibility: which solvents can be mixed safely, which produce hazardous reactions
- Membrane operation: pressure, flow rate, fouling prevention

## 3. Bill of Materials

### BOM: Solvent Recovery by Distillation (per 1,000 L spent solvent)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Spent solvent (IPA, acetone, ethanol) | 1,000 L feed | Manufacturing waste streams | N/A — this is the feedstock |
| Steam (heating) | 150–400 kg (depending on boiling point) | [Energy](../energy/index.md) | Direct gas heating (less controllable) |
| Cooling water | 5–15 m³ | [Water Treatment](water-treatment.md) | Air-cooled condenser (climate-dependent) |
| Activated carbon (polishing) | 1–5 kg | [Chemistry](./index.md) | None for color body removal |
| Molecular sieve (drying) | 5–20 kg (regenerable) | [Chemistry](./index.md) | CaCl₂ desiccant (consumed, not regenerated) |
| Electrical energy | 10–50 kWh | [Energy](../energy/index.md) | Steam-driven pumps if available |

### BOM: Acid Recovery by Diffusion Dialysis (per 1,000 L spent acid)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Spent acid (H₂SO₄, HCl, HNO₃) | 1,000 L feed | Pickling, etching, cleaning waste | N/A — feedstock |
| Anion exchange membranes | 10–50 m² membrane area | [Chemistry](./index.md) | Electrodialysis (requires electricity) |
| Deionized water (receiving stream) | 500–1,500 L | [Water Treatment](water-treatment.md) | Tap water (reduces recovery purity) |
| Electricity | 5–15 kWh | [Energy](../energy/index.md) | Diffusion dialysis is passive (gravity-driven) |

## 4. Process Description

### 4.1 Solvent Recovery by Fractional Distillation

1. **Collect and segregate spent solvents.** Store each solvent type in dedicated tanks. Never mix solvent families — halogenated and non-halogenated solvents require separate recovery trains. Label all containers with solvent identity and estimated purity.

**Strengths**: Distillation recovery achieves 85-95% solvent purity suitable for reuse; energy cost (2-5 MJ/kg) is 5-10× cheaper than purchasing fresh solvent; reduces hazardous waste volume by 80-90%; well-understood technology with standard equipment.

**Weaknesses**: Azeotropes limit recovery purity for some solvent mixtures (e.g., ethanol-water); energy-intensive for high-boiling solvents; halogenated solvents require dedicated corrosion-resistant equipment; spent activated carbon and still bottoms remain as hazardous waste requiring disposal.

2. **Pre-treat.** Filter spent solvent through a 10–50 μm cartridge filter to remove suspended solids. Pass through activated carbon if color bodies or dissolved organics are present. This protects the distillation column from fouling.

3. **Charge the still.** Fill the reboiler with 500–2,000 L of pre-treated spent solvent. Seal the system and verify all connections. Open cooling water to the condenser.

4. **Heat to boiling.** Gradually raise reboiler temperature to the solvent boiling point (IPA: 82°C, ethanol: 78°C, acetone: 56°C). Establish reflux at a 3:1 to 10:1 reflux ratio for good separation. Monitor overhead temperature with ±0.5°C accuracy.

5. **Draw product.** When overhead temperature stabilizes within ±0.5°C of the pure solvent boiling point, begin drawing product at 50–200 L/hour. Monitor for temperature drift indicating a different component is approaching the top — stop draw and increase reflux if temperature rises >1°C.

6. **Dry the product.** If recovered solvent contains water (common with IPA and ethanol), pass through molecular sieve columns (3Å zeolite for water removal). Target: <0.5% water content for most industrial reuse.

7. **Collect residue.** The reboiler residue contains high-boiling contaminants, dissolved metals, and polymerized organics. Dispose via [Waste Management](../ehs/waste-management.md) or further processing.

### 4.2 Acid Recovery by Diffusion Dialysis

1. **Feed preparation.** Filter spent acid through a 5–25 μm filter to remove suspended solids that would foul membranes. Measure acid concentration and dissolved metal content.

2. **Set up dialysis stack.** Arrange anion exchange membranes in a plate-and-frame stack with alternating acid and water channels. Flow rates: acid feed 1–5 L/hour/m² membrane, water feed 1.2–1.5× acid flow rate (counter-current).

3. **Operate passively.** Diffusion dialysis is driven by concentration gradient — no electricity required. Acid (H⁺ and anion) diffuses through the membrane; dissolved metal cations are rejected. Recovery rate: 70–90% of free acid.

4. **Collect recovered acid.** The acid-enriched water stream contains 60–85% of the original acid concentration. Verify concentration by titration. Adjust with fresh acid if needed for process reuse.

5. **Manage metal-rich stream.** The depleted acid stream contains concentrated metal salts. Route to metal recovery (precipitation or electrowinning) or to waste treatment.

### 4.3 Catalyst Recovery

1. **Collect spent catalyst.** Solid catalysts (metals on carbon or alumina supports) are filtered or decanted from process streams. Homogeneous catalysts remain dissolved and require different recovery methods.

2. **Thermal regeneration (solid catalysts).** Heat spent catalyst to 400–600°C in air to burn off carbonaceous deposits (coking). Cool and screen to remove fines. Activity recovery: 80–95% of fresh catalyst.

3. **Metal recovery from spent catalyst.** Dissolve catalyst support in acid or alkali. Precipitate or plate the active metal (Pt, Pd, Ni, Co). See [Electrolysis](electrolysis.md) for electrowinning details.

## 5. Quantitative Parameters

### Solvent Recovery Rates and Purity

| Solvent | Boiling Point | Recovery Rate | Achievable Purity | Energy (kWh/1000L) |
|---------|--------------|---------------|-------------------|---------------------|
| Isopropanol (IPA) | 82°C | 90–98% | 99.0–99.5% | 15–35 |
| Acetone | 56°C | 85–95% | 99.0–99.5% | 10–25 |
| Ethanol | 78°C | 90–97% | 95.0–99.5% | 20–40 |
| NMP | 202°C | 80–92% | 98.0–99.0% | 35–60 |
| PGMEA | 146°C | 85–93% | 98.5–99.5% | 25–45 |
| Methanol | 65°C | 90–96% | 99.0–99.5% | 12–28 |

### Acid Recovery by Method

| Method | Acids Recovered | Recovery Rate | Purity | Energy |
|--------|----------------|---------------|--------|--------|
| Diffusion dialysis | H₂SO₄, HCl, HNO₃ | 70–90% | 60–85% of original | Passive (gravity) |
| Electrodialysis | H₂SO₄, HCl, HF | 80–95% | 80–90% of original | 50–200 kWh/m³ |
| Thermal decomposition | H₂SO₄ (to SO₃ → H₂SO₄) | 90–98% | >95% | High (furnace at 800°C) |
| Ion exchange | All mineral acids | 85–95% | 90–95% | 20–80 kWh/m³ |

### Membrane Performance Parameters

| Parameter | Diffusion Dialysis | Electrodialysis |
|-----------|-------------------|-----------------|
| Membrane type | Anion exchange | Bipolar or anion exchange |
| Operating pressure | 0.01–0.05 MPa | 0.05–0.2 MPa |
| Temperature range | 15–40°C | 20–45°C |
| Flow rate | 1–5 L/h/m² | 5–20 L/h/m² |
| Membrane lifetime | 2–5 years | 3–7 years |
| Acid recovery | 70–90% | 80–95% |
| Metal rejection | 90–98% | 85–95% |

## 6. Scaling Notes

**Minimum viable scale**: A simple pot still recovering 10–50 L/day of ethanol or IPA from laboratory waste. Requires a copper pot, condenser coil, and heat source. This is the bootstrap entry point — any settlement with distillation capability can recover solvents.

**Small industrial scale** (100–1,000 L/day): A dedicated fractional distillation column with automated reflux control and product draw. Requires steam supply and cooling water. Appropriate for a community with chemical manufacturing generating spent solvent streams.

**Full industrial scale** (10,000–100,000+ L/day): Continuous distillation trains with multiple columns, heat integration (feed preheated by product streams), and automated process control. Typical in chemical parks and semiconductor fabs. Capital cost: $500K–$5M per train.

**Key scaling factor**: Heat integration becomes economically critical above 1,000 L/day. Without heat recovery, distillation energy costs dominate. A feed-effluent heat exchanger recovers 60–80% of the heating energy, reducing steam demand proportionally.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Low purity in recovered solvent | Insufficient reflux ratio, column flooding, or damaged packing | Increase reflux ratio to 5:1 or higher; check packing condition; verify column is level |
| Emulsion formation during distillation | Surfactants or particulates in spent solvent | Pre-filter through activated carbon; add salt to break emulsion |
| Membrane fouling in diffusion dialysis | Suspended solids or organic fouling | Pre-filter to <5 μm; clean membranes with dilute alkali (2% NaOH) monthly |
| Low acid recovery rate | Spent acid too dilute (<10% wt), membrane degradation | Concentrate feed by evaporation before dialysis; check membrane integrity |
| Recovered catalyst has low activity | Incomplete coke burnoff, sintering of metal crystallites | Increase regeneration temperature by 50°C; limit regeneration time to prevent sintering |
| Azeotrope prevents full solvent-water separation | IPA-water (12% water) or ethanol-water (4% water) form azeotropes | Use molecular sieve drying (pressure-swing adsorption) or extractive distillation with ethylene glycol |

## 8. Safety

**Flammable solvent vapors** are the primary hazard in solvent recovery. All distillation equipment must be electrically grounded to prevent static sparks. Operate in a well-ventilated area with explosion-proof electrical fittings. IPA vapor (LEL 2%, UEL 12%) ignites easily — a single spark near the condenser outlet can cause flashback into the reboiler. Install flame arrestors on all vent lines.

**Acid burns** during acid recovery: H₂SO₄ and HCl at process concentrations (10–30%) cause severe skin burns within seconds. HF is lethal through skin absorption at concentrations >50%. PPE: chemical-resistant gloves (nitrile for H₂SO₄/HCl, neoprene for HF), face shield, chemical apron, and eye wash station within 10 seconds travel time.

**Toxic catalyst metals**: Spent catalysts containing nickel, cobalt, or chromium compounds are classified as hazardous waste. Inhalation of catalyst dust during handling causes respiratory sensitization. PPE: half-face respirator with P100 filter when handling dry catalyst.

**Nitrogen oxide (NOₓ) evolution**: Concentrated nitric acid recovery can release NO₂ (brown gas, lethal at 100 ppm). Provide local exhaust ventilation with scrubbing when recovering HNO₃. Gas detection: colorimetric tubes or electrochemical NO₂ sensor.

## 9. Quality Control

### Recovered Solvent Specification

| Parameter | Test Method | Typical Specification |
|-----------|------------|---------------------|
| Purity (GC) | Gas chromatography | >99.0% for most industrial reuse |
| Water content | Karl Fischer titration | <0.5% (varies by application) |
| Acidity | Titration with NaOH | <0.01% as acid |
| Non-volatile residue | Evaporation at 105°C | <10 mg/L |
| Color | Visual/UV-Vis | Clear, colorless |
| Specific gravity | Hydrometer or digital density meter | Within 0.001 of pure solvent value |

### Recovered Acid Specification

| Parameter | Test Method | Typical Specification |
|-----------|------------|---------------------|
| Acid concentration | Titration with standardized base | ±5% of target concentration |
| Dissolved metals | ICP-OES or AAS | <100 ppm total metals |
| Total suspended solids | Gravimetric (0.45 μm filter) | <50 mg/L |
| Organic contamination | TOC analysis or UV-Vis | <500 ppm C |

### Field Tests (No Lab Required)

- **Specific gravity**: Float a hydrometer in the recovered solvent. Compare to published values for pure solvent. Deviation indicates contamination.
- **Water test**: Add anhydrous copper sulfate (white) to the solvent. If it turns blue, water is present (CuSO₄ + 5H₂O → CuSO₄·5H₂O, blue).
- **Acid concentration**: Titrate 10 mL of recovered acid with 1N NaOH using phenolphthalein indicator. Calculate concentration from volume used.

## 10. Variations and Alternatives

### Recovery Method Selection Guide

| Situation | Best Method | Why |
|-----------|------------|-----|
| Single solvent with water | Fractional distillation | Boiling point difference sufficient |
| Azeotropic mixture | Extractive distillation or molecular sieve | Simple distillation cannot cross azeotrope |
| Acid with dissolved metals | Diffusion dialysis | Low energy, good metal rejection |
| Acid at high purity needed | Electrodialysis or thermal regeneration | Higher purity than diffusion dialysis |
| Solid catalyst with coke deposit | Thermal regeneration (calcination) | Restores active surface |
| Precious metal catalyst | Dissolution + precipitation/electrowinning | Metal value justifies recovery cost |
| Mixed solvent waste (unidentified) | Incineration with heat recovery | Separation not feasible; energy recovery is the only option |

### Comparison: Recovery vs. Disposal

| Factor | Recovery | Disposal |
|--------|----------|----------|
| Cost | Moderate (capital + operating) | Low (treatment chemicals) to high (hazardous waste fees) |
| Energy | Significant (distillation) | Low (treatment) |
| Material output | Reusable chemical | Treated effluent (no material value) |
| Applicable scale | >100 L/day economical | Any scale |
| Regulatory | Often required for large generators | Always required |

## 11. References

- [Distillation](distillation.md) — Distillation column design and operation
- [Electrolysis](electrolysis.md) — Electrowinning for metal recovery from spent catalyst
- [Acid Regeneration](sem-tech-acid-regeneration.md) — Membrane-based acid recovery for semiconductor fab
- [Solvent Production](solvents.md) — Primary solvent production processes
- [Mineral Acids](acids.md) — Primary acid production processes
- [Water Treatment](water-treatment.md) — Water purification for recovery process water
- [Waste Management](../ehs/waste-management.md) — Disposal of non-recoverable chemical waste
- [Metal Recycling](../metals/metal-recycling.md) — Metal recovery from scrap (parallel recovery domain)

---

*Part of the [Bootciv Tech Tree](../index.md) · [Chemistry](./index.md) · [All Domains](../index.md)*
