# Gas Purification

> **Node ID**: gas-handling.gas-purification
> **Domain**: [Gas Handling](./index.md)
> **Dependencies**: [`gas-handling.basic`](basic.md) (compressors, piping), [`chemistry.air-separation`](../chemistry/air-separation.md) (cryogenic cooling), [`chemistry.acids`](../chemistry/acids.md) (reagent production)
> **Enables**: [`chemistry.hydrogen-silane`](../chemistry/hydrogen-silane.md) (ultra-pure H₂), [`silicon.purification`](../silicon/purification.md) (reactor-grade gases), [`photolithography.fab-processes`](../photolithography/fab-processes.md) (process gas purity)
> **Timeline**: Years 25-45
> **Outputs**: purified_gases, scrubbed_gases, dried_gases, high_purity_gases
> **Critical**: Yes — semiconductor fabrication requires gases at 99.999-99.9999% purity; impurities at ppb levels kill device yield

Gas purification removes contaminants — moisture, oxygen, hydrocarbons, particulates, and trace impurities — from process gas streams to meet the purity requirements of downstream consumers. In the bootstrap chain, basic gas handling produces compressed gases at 98-99% purity, but semiconductor fabrication demands 5N-6N (99.999-99.9999%) purity with individual contaminant species controlled to parts-per-billion levels.

A single water molecule or oxygen atom in a silane stream during CVD deposition creates a defect in the growing silicon film. A hydrocarbon contaminant in an argon stream during crystal growth introduces carbon impurities that degrade minority carrier lifetime in the finished wafer. The economic impact scales exponentially: a 10 ppb increase in O₂ contamination in nitrogen used for wafer handling can reduce yield by 5-15% at sub-micron geometries.

This capability covers four purification methods ordered by increasing specificity: bulk scrubbing (removing percent-level contaminants), adsorption (removing ppm-level contaminants), catalytic purification (removing specific trace species to ppb), and cryogenic separation (exploiting boiling-point differences for bulk gas purification). Each method addresses a different contaminant concentration range, and a complete gas purification train combines multiple stages.

## Prerequisites

- **Materials**: Steel piping, copper tubing, PTFE gaskets, activated carbon, silica gel, molecular sieves (zeolites), copper catalyst, palladium membrane material
- **Tools and equipment**: [Basic gas handling](basic.md) — compressors, piping, valves, pressure regulators; [Electric furnaces](../energy/electric-furnaces.md) for regeneration heating; [Machine tools](../machine-tools/index.md) for vessel fabrication
- **Knowledge**: Thermodynamics of adsorption, catalytic reaction kinetics, gas chromatography for purity verification
- **Infrastructure**: Compressed air or nitrogen for purging, electrical power for heater elements, ventilation for off-gas treatment

## Bill of Materials

| Material | Quantity (per purification train) | Source | Alternatives |
|----------|-----------------------------------|--------|-------------|
| Activated carbon (GAC, 4-8 mesh) | 50-200 kg per adsorber vessel | [Chemistry](../chemistry/index.md) — coconut shell or coal-based carbon | Wood charcoal (lower capacity, higher ash) |
| Silica gel (3-5 mm beads) | 25-100 kg per dryer bed | [Chemistry](../chemistry/index.md) — sodium silicate + sulfuric acid | Alumina gel (higher temperature tolerance) |
| Molecular sieve 3Å | 25-75 kg per dryer bed | [Chemistry](../chemistry/index.md) — synthetic zeolite from alumina + silica | Molecular sieve 4Å (less selective, absorbs CO₂) |
| Copper catalyst (BTS catalyst) | 5-20 kg per O₂ removal bed | [Metals](../metals/index.md) — copper on alumina support | Manganese oxide (lower capacity, slower kinetics) |
| PTFE gaskets | Per flange connection | [Polymers](../polymers/index.md) | Compressed fiber gaskets (higher outgassing) |
| Stainless steel 316L tubing | 50-200 m per train | [Metals](../metals/index.md) | Copper tubing (not for ultra-high purity) |
| Heating elements (Nichrome) | 2-10 kW per regeneration heater | [Energy](../energy/index.md) — resistance wire | Gas-fired heaters (less precise temperature control) |
| Calcium chloride (CaCl₂) | 10-50 kg per rough dryer | [Chemistry](../chemistry/index.md) — limestone + HCl | Not regenerable — discard after saturation |


## Scrubbing (Bulk Contaminant Removal)

1. Route contaminated gas stream into the bottom of a packed scrubber column. The column is a vertical steel vessel (0.3-1.5 m diameter, 2-6 m height) filled with ceramic or plastic packing (Raschig rings, Pall rings, or structured packing) to maximize gas-liquid contact area.
2. Flow scrubbing liquid countercurrent to the gas — liquid enters at the top through a spray distributor and trickles down through the packing by gravity while gas rises. The liquid absorbs target contaminants by dissolution or chemical reaction.
3. For acid gas removal (HCl, Cl₂, HF, SO₂, H₂S): use 5-20% NaOH solution in water. Monitor scrubber solution pH continuously; replace when pH drops below 10. Acid gases react to form salts (e.g., Cl₂ + 2NaOH → NaCl + NaOCl + H₂O).
4. For ammonia removal: use 5-10% H₂SO₄ solution. Ammonia is absorbed and neutralized to ammonium sulfate.
5. For general particulate and soluble gas removal: use water scrubbing. Water absorbs water-soluble species (HCl, HF, NH₃, SO₂) by physical dissolution.
6. Collect spent scrubber solution in a holding tank for neutralization and disposal. Never discharge untreated scrubber effluent.

**Strengths:**
- Countercurrent packed-column design maximizes gas-liquid contact area, achieving 90-99% removal of target contaminants in a single pass
- NaOH scrubber converts toxic acid gases (Cl₂, HCl, H₂S) to non-toxic salts, enabling safe atmospheric discharge

**Weaknesses:**
- Scrubber solutions become spent and require neutralization and disposal — continuous waste stream generation
- Cannot achieve ppb-level purity — residual contaminant levels of 10-100 ppm are the practical floor for wet scrubbing

## Adsorption Drying and Purification

1. Load two adsorber vessels in a lead-lag (twin-bed) configuration. While vessel A is online adsorbing moisture from the process gas, vessel B is offline being regenerated. Switch when the online vessel reaches breakthrough (downstream moisture exceeds specification).
2. Fill each adsorber vessel with the appropriate adsorbent in layers: coarse activated carbon at the inlet (removes organics and oils), molecular sieve 3Å in the middle (removes water to <1 ppm), and a polishing layer of molecular sieve 4Å or 5Å at the outlet (removes CO₂ and residual traces).
3. Flow gas downward through the bed at a superficial velocity of 0.1-0.3 m/s. Higher velocities cause channeling (gas finds preferential paths through the bed, bypassing adsorbent). Lower velocities reduce throughput.
4. Monitor outlet gas with a moisture analyzer (electrolytic or capacitive hygrometer). When moisture exceeds the setpoint (typically 1-5 ppm for industrial grade, <0.1 ppm for semiconductor grade), switch to the standby vessel.
5. Regenerate the spent vessel by heating to 250-350°C while flowing a purge gas (dry nitrogen or a slipstream of the purified product gas) through the bed in the reverse direction (countercurrent to the adsorption flow). The heated purge gas drives off adsorbed water and contaminants. Continue for 4-8 hours until outlet dew point reaches -70°C or lower.
6. Cool the regenerated bed to operating temperature by flowing cold purge gas before placing it back in service.

**Strengths:**
- Twin-bed lead-lag configuration provides continuous purification — one bed is always online while the other regenerates
- Molecular sieve 3Å achieves <1 ppm H₂O outlet purity with 15-25% water capacity by weight, and is fully regenerable at 250-350°C for 3-7 year service life

**Weaknesses:**
- Regeneration requires 250-350°C heating for 4-8 hours — significant energy input (50-200 kWh/ton adsorbent)
- Gas channeling at velocities above 0.3 m/s bypasses adsorbent, causing premature breakthrough

## Catalytic Purification (Oxygen and Hydrogen Removal)

1. For oxygen removal from inert gases (N₂, Ar, He): pass the gas through a bed of reduced copper catalyst at 200-400°C. Copper reacts with trace O₂ to form CuO, removing oxygen to below 1 ppb. The catalyst bed is contained in a heated stainless steel vessel with internal thermocouples to verify uniform temperature.
2. Regenerate the spent copper catalyst by flowing dilute hydrogen (2-5% H₂ in N₂) through the bed at 250-350°C. Hydrogen reduces CuO back to metallic copper (CuO + H₂ → Cu + H₂O). The water vapor is carried out by the purge gas. Monitor exit gas for moisture to confirm regeneration is complete.
3. For hydrogen removal from inert or oxygen-containing streams: pass gas through a palladium or platinum catalyst bed at ambient to 100°C. The catalyst promotes oxidation of H₂ to H₂O (if O₂ is present) or adsorption onto the catalyst surface. The resulting water is removed by a downstream adsorbent dryer.
4. For hydrocarbon removal: catalytic oxidation at 300-400°C over a platinum or palladium catalyst converts hydrocarbons to CO₂ and H₂O, which are then removed by downstream adsorption. This approach removes methane, ethylene, and other light hydrocarbons that adsorbents capture poorly.

**Strengths:**
- Copper catalyst removes O₂ to below 1 ppb — the deepest oxygen removal achievable by any non-cryogenic method
- Catalytic oxidation converts trace hydrocarbons to easily-removable CO₂ and H₂O, solving the problem of methane's poor adsorption

**Weaknesses:**
- Reduced copper and palladium catalysts are pyrophoric — exposure to air after regeneration causes rapid oxidation and potential ignition
- Catalysts are poisoned by sulfur compounds and halogens — a single exposure to H₂S or chlorine permanently degrades the catalyst bed

## Cryogenic Separation

Cryogenic separation is covered in detail in [Air Separation](../chemistry/air-separation.md). For gas purification specifically, partial condensation at controlled cryogenic temperatures exploits differences in boiling points to separate gas mixtures:

1. Pre-cool the mixed gas stream to approximately -50°C using a heat exchanger against returning cold product gas (countercurrent recuperative heat exchanger).
2. Further cool to the target separation temperature using liquid nitrogen (LN₂, -196°C) or controlled Joule-Thomson expansion. For CO₂ removal from methane, cool to -55°C (CO₂ freezes at -78.5°C at 1 atm but deposits from gas streams at higher temperatures under pressure). For N₂/CH₄ separation, cool to -160 to -180°C.
3. Separate the condensed or frozen fraction from the remaining gas by gravity in a phase separator or by filtration. The condensed fraction is the higher-boiling-point component.
4. Warm the purified gas stream through the countercurrent heat exchanger, recovering cold energy from the incoming stream. This recuperative heat exchange reduces LN₂ consumption by 70-90%.

**Strengths:**
- Exploits boiling-point differences for bulk separation — achieves 99-99.999% purity in a single stage for favorable mixtures
- Countercurrent heat recovery reduces LN₂ consumption by 70-90%, making the process economically viable

**Weaknesses:**
- Requires liquid nitrogen (-196°C) — cryogenic infrastructure is a major capital investment
- Feed gas must be pre-dried to <1 ppm H₂O to prevent ice formation that blocks heat exchanger passages

## Quantitative Parameters

| Parameter | Scrubbing | Adsorption Drying | Catalytic O₂ Removal | Cryogenic Separation |
|-----------|-----------|-------------------|----------------------|---------------------|
| Contaminant range | 0.1-10% (bulk) | 10 ppm - 1% | 1 ppm - 100 ppm | 0.01-100% (bulk) |
| Outlet purity | 10-100 ppm residual | <1 ppm H₂O, <5 ppm CO₂ | <1 ppb O₂ | 99-99.999% |
| Operating temperature | 20-60°C | 20-40°C (adsorb), 250-350°C (regen) | 200-400°C | -80 to -196°C |
| Operating pressure | 1-10 bar | 1-30 bar | 1-10 bar | 1-50 bar |
| Cycle time | Continuous | 4-24 hours adsorption, 4-8 hours regeneration | 3-12 months per charge | Continuous |
| Pressure drop | 0.05-0.3 bar/m bed | 0.02-0.1 bar/m bed | 0.01-0.05 bar/m bed | 0.5-2 bar total |
| Energy consumption | 0.5-2 kWh/1000 m³ gas | 50-200 kWh/ton adsorbent (regeneration) | 0.5-5 kWh/1000 m³ gas | 0.3-1.5 kWh/Nm³ gas |

## Adsorbent Capacity by Type

| Adsorbent | Water Capacity (wt%) | Regeneration Temperature | Cycle Life | Target Contaminant |
|-----------|----------------------|--------------------------|------------|-------------------|
| Silica gel | 30-40% | 150-200°C | 2-5 years | H₂O (bulk drying) |
| Molecular sieve 3Å | 15-25% | 250-350°C | 3-7 years | H₂O (deep drying) |
| Molecular sieve 4Å | 15-22% | 250-350°C | 3-7 years | H₂O, CO₂ |
| Molecular sieve 13X | 20-30% | 250-350°C | 3-5 years | H₂O, CO₂, H₂S |
| Activated carbon | 5-15% (organics) | 120-150°C (steam) | 1-3 years | Organics, oil vapor |
| Calcium chloride | ~30% (non-regen) | N/A (single use) | Single use | H₂O (rough drying) |
| P₂O₅ | Reacts to form H₃PO₄ | N/A (single use) | Single use | H₂O (ultimate polishing) |

## Scaling Notes

- **Bench scale**: Single adsorber column (25-50 mm diameter, 0.5 m bed height) processes 1-10 L/min of gas. Adequate for laboratory purification of cylinder gas. Manual switchover for regeneration.
- **Pilot scale**: Twin-bed adsorber system (100-200 mm diameter, 1-2 m bed height) processes 10-100 L/min. Automated valve sequencing for lead-lag switching. Heated regeneration with integrated blower. This is the minimum scale for producing semiconductor-grade nitrogen from compressed air.
- **Production scale**: Multiple trains of twin-bed adsorbers (0.3-1.5 m diameter, 2-4 m bed height) process 100-10,000+ m³/hour. Full PLC control with moisture breakthrough detection, automatic bed switching, and regeneration scheduling. Waste heat recovery from regeneration exhaust reduces energy consumption by 30-50%.
- **Scale-up bottleneck**: Adsorbent bed diameter. Above ~1.5 m diameter, gas distribution across the bed becomes non-uniform. Solution: use multiple smaller beds in parallel rather than a single large vessel. Each bed sees the same flow per unit cross-sectional area.
- **Economic minimum**: A twin-bed adsorber with 100 mm diameter vessels produces ~50 L/min of dried gas (sufficient for one CVD reactor). Below this scale, pre-purified cylinder gas is more cost-effective than on-site purification.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Moisture breakthrough after <2 hours on-line | Adsorbent exhausted or contaminated with oil | Regenerate at higher temperature (350°C) for longer (8-12 hours). If oil contamination suspected, replace adsorbent — oil fouls pores irreversibly. |
| High pressure drop across adsorber | Adsorbent dust or fines from thermal cycling | Install a 5-10 μm particulate filter upstream. Replace degraded adsorbent. Avoid rapid heating/cooling during regeneration. |
| Incomplete O₂ removal by copper catalyst | Catalyst not fully reduced, or temperature too low | Reduce catalyst with H₂/N₂ mixture at 350°C for 4-6 hours. Verify inlet gas temperature is above 200°C during operation. |
| Scrubber pH drops rapidly | High contaminant load in feed gas | Increase scrubber solution concentration. Add second scrubber in series. Pre-treat gas stream with a bulk removal step before the scrubber. |
| Regeneration takes excessively long | Insufficient purge gas flow or heater undersized | Verify purge gas flow rate (minimum 0.5 bed volumes per hour). Check heater output against nameplate rating. Verify thermocouple calibration. |
| Color change on indicator silica gel persists after regeneration | Adsorbent permanently contaminated or regeneration incomplete | If color does not revert from pink to blue after 8 hours at 250°C, replace adsorbent. Organic contamination can block active sites permanently. |
| Product gas contamination after regeneration | Incomplete cooling before returning to service | Cool regenerated bed to within 10°C of operating temperature before switching online. Hot adsorbent does not adsorb effectively. |
| Cryogenic separator frosting or ice buildup | Moisture in feed gas freezing at cold surfaces | Install adequate pre-drying (adsorbent dryer) before cryogenic stage. Moisture must be below 1 ppm before reaching cryogenic temperatures. |

## Safety

**Catalyst fire hazard**: Reduced copper and palladium catalysts are pyrophoric when freshly regenerated and exposed to air. The finely divided metal surface oxidizes rapidly, generating enough heat to ignite surrounding materials. After regeneration, cool the catalyst bed under inert gas (N₂ or Ar) to below 50°C before exposing to air. Store spent catalyst in sealed containers under water or inert atmosphere until disposal or reprocessing.

**Scrubber solution hazards**: Caustic scrubber solutions (NaOH) at 5-20% concentration cause severe chemical burns on skin contact and permanent eye damage. Wear chemical splash goggles, face shield, rubber apron, and nitrile gloves when handling scrubber solutions. Acid scrubber solutions present analogous burn and inhalation hazards. Neutralize spent scrubber solutions to pH 6-9 before disposal.

**Regeneration heater safety**: Adsorbent regeneration at 250-350°C involves heating enclosed vessels with potentially flammable desorbed contaminants. If oil or organic vapors are present in the adsorbent, the combination of heat and desorbed hydrocarbons can create an explosive atmosphere. Purge the vessel thoroughly with nitrogen before heating. Never regenerate an oil-contaminated adsorbent bed without first confirming it has been purged of flammable vapors.

**Cryogenic hazards**: Liquid nitrogen at -196°C causes cryogenic burns on skin contact (tissue destruction identical to third-degree burns). LN₂ expands 700× upon vaporization — trapped liquid in enclosed piping or vessels can generate enormous pressure. Install pressure relief valves on all cryogenic vessels and piping. Vent cryogenic gas to atmosphere in a well-ventilated area — nitrogen displaces oxygen and causes asphyxiation in confined spaces without warning. See [Basic Gas Handling](basic.md) for inert gas asphyxiation protocols.

**P₂O₅ handling**: Phosphorus pentoxide reacts violently with water to form phosphoric acid, generating heat. Handle with chemical-resistant gloves, face shield, and respiratory protection (dust mask or powered air purifying respirator). Store in sealed containers under dry atmosphere. Spill response: cover with dry sand or vermiculite, then carefully transfer to a container. Do not add water.

## Quality Control

**Moisture analysis**: Measure dew point or moisture content at the purification train outlet. For industrial-grade gas: dew point -40°C (~127 ppm H₂O). For semiconductor-grade gas: dew point -70°C (~2.5 ppm H₂O) or better. Electrolytic hygrometer measures 0-1000 ppm with ±5% accuracy. Capacitive hygrometer measures 0.1-1000 ppm with ±2% accuracy. Calibrate monthly against a traceable moisture standard.

**Oxygen analysis**: Electrochemical O₂ sensor measures 0-1000 ppm O₂. Galvanic cell sensor measures 0-25% O₂. For catalytic purifier verification: use a zirconia O₂ sensor capable of measuring 0-10 ppb. Semiconductor-grade nitrogen must contain <1 ppb O₂. Verify with online sensor and periodic grab-sample analysis by gas chromatography.

**Hydrocarbon analysis**: Gas chromatography with flame ionization detector (GC-FID) measures total hydrocarbons to 10 ppb. Sample at the purification train outlet weekly. Target: <100 ppb total hydrocarbons for semiconductor-grade gases (methane is the most persistent trace impurity in nitrogen).

**Particulate measurement**: Install 0.2 μm membrane filter at outlet. Weigh filter before and after a known gas volume (gravimetric method). Target: <1 particle per cubic foot ≥0.2 μm for semiconductor-grade gas. Online particle counters using laser light scattering provide continuous monitoring.

**Gas chromatography verification**: Monthly analysis of product gas by GC with appropriate detectors (TCD for permanent gases, FID for hydrocarbons, ECD for electronegative species). Confirms that all major contaminants are below specification in a single analytical run.

## Variations and Alternatives

| Method | Purity Achievable | Best For | Limitations |
|--------|-------------------|----------|-------------|
| Scrubbing (wet) | 10-100 ppm residual | Bulk acid/base gas removal | Cannot achieve ppb purity; generates liquid waste |
| Scrubbing (dry — solid reagents) | 1-10 ppm | Small-scale, batch applications | Reagent consumed and must be replaced |
| Adsorption (molecular sieve) | <1 ppm H₂O, <5 ppm CO₂ | Continuous drying and CO₂ removal | Requires periodic regeneration; cannot remove O₂ or H₂ |
| Catalytic purification | <1 ppb O₂ or H₂ | Semiconductor-grade gas polishing | Catalyst degrades with poisons (sulfur, halogens) |
| Cryogenic separation | 99-99.999% | Bulk gas separation (air separation, CO₂ removal) | High energy cost for small-scale; LN₂ logistics |
| Palladium membrane (H₂ purification) | 99.99999% (7N) | Hydrogen purification for semiconductor use | Pd membranes expensive; H₂S poisons membrane |
| Pressure Swing Adsorption (PSA) | 99-99.99% N₂ or O₂ from air | On-site nitrogen or oxygen generation | Lower purity than cryogenic; adsorbent replacement every 5-10 years |

**Pressure Swing Adsorption (PSA)** is an energy-efficient alternative to cryogenic separation for producing nitrogen or oxygen from air at moderate purities. PSA uses two adsorbent beds operating in alternating cycles: one adsorbs at elevated pressure (3-10 bar) while the other desorbs at near-atmospheric pressure. Carbon molecular sieve adsorbs O₂ faster than N₂, producing N₂ at 95-99.5% purity. Zeolite molecular sieve adsorbs N₂ faster than O₂, producing O₂ at 90-95% purity. PSA systems are mechanically simpler than cryogenic plants and require no refrigeration, but cannot achieve the >99.99% purity levels that cryogenic distillation provides.

**Getters (metal-based reactive purification)**: Titanium, zirconium, and rare-earth alloy getters chemically bind trace contaminants (O₂, N₂, H₂O, CO, CO₂) at elevated temperatures (400-800°C). Non-evaporable getters (NEG) are heated once to activate and then continuously absorb contaminants at room temperature. Used for maintaining ultra-high purity in sealed systems (vacuum chambers, gas cabinets) over long periods. Capacity is limited (typically 0.1-1% of getter mass in absorbed contaminants). Ideal for polishing the last ppb of contaminants from an already-purified stream.

## Purification Train Configuration by Gas Type

Different gases require different purification stages arranged in series. The general principle: remove bulk contaminants first (cheaper methods), then polish to final purity (expensive methods). Below are the standard trains for common process gases.

**Nitrogen (from compressed air to semiconductor grade)**:
1. Coalesce filter (remove oil mist and particulates from compressor)
2. Carbon adsorber (remove trace hydrocarbons)
3. Molecular sieve dryer (remove water to <1 ppm)
4. Catalytic deoxo unit (copper catalyst at 250°C, remove O₂ to <1 ppb)
5. Particulate filter (0.003 μm, remove catalyst fines)
6. Result: N₂ at 99.9999% (6N), O₂ <1 ppb, H₂O <1 ppb, THC <1 ppb

**Hydrogen (from electrolysis to semiconductor grade)**:
1. Water separator (remove bulk water from electrolysis cell)
2. Palladium membrane purifier (H₂ diffuses through Pd alloy at 350-400°C; all other gases rejected). Pd membrane is the single most effective H₂ purification technology — achieves 7N purity in one step.
3. Molecular sieve dryer (polish residual moisture)
4. Result: H₂ at 99.99999% (7N), O₂ <0.1 ppb, H₂O <0.5 ppb

**Argon (from air separation to semiconductor grade)**:
1. Cryogenic distillation (primary separation from air, 99-99.99%)
2. Catalytic deoxo (copper catalyst, remove O₂ to <1 ppb)
3. Molecular sieve dryer (remove H₂O to <1 ppm)
4. Zirconium getter (remove N₂, O₂, H₂, CO, CO₂ residual traces)
5. Result: Ar at 99.9999% (6N), all impurities <1 ppb

## Purification Cost Comparison

| Method | Capital Cost | Operating Cost | Purity Level | Best Application |
|--------|-------------|----------------|-------------|-----------------|
| Wet scrubbing | $5K-50K | $1-5/KCF gas | 10-100 ppm residual | Bulk acid gas removal |
| Adsorbent dryer (twin-bed) | $10K-100K | $2-10/KCF gas | <1 ppm H₂O | Continuous drying |
| Catalytic deoxo | $20K-150K | $1-5/KCF gas | <1 ppb O₂ | O₂ polishing |
| PSA generator | $30K-300K | $3-15/KCF gas | 95-99.5% | On-site N₂/O₂ production |
| Pd membrane | $50K-500K | $5-20/KCF gas | 99.99999% | H₂ ultra-purification |
| Cryogenic plant | $500K-5M | $10-50/KCF gas | 99-99.999% | Bulk air separation |

## Common Purification Mistakes

- **Putting the dryer before the particulate filter**: Adsorbent beds act as depth filters — particulates clog pore structure and reduce capacity. Always install a particulate filter (5-10 μm) upstream of any adsorbent bed.
- **Regenerating with wet purge gas**: If the regeneration purge gas contains moisture, the adsorbent re-adsorbs water during the very process meant to clean it. Use dry nitrogen (dew point below -70°C) for regeneration.
- **Operating catalytic purifiers below minimum temperature**: Copper catalyst kinetics drop sharply below 180°C. The catalyst appears to be working (some O₂ is removed) but outlet purity is 10-100× worse than specification. Always verify catalyst bed temperature with a thermocouple, not the heater setpoint.
- **Neglecting to replace saturated adsorbent**: Adsorbent capacity is finite. After 2-5 years of operation, the adsorbent's effective capacity drops due to pore fouling, thermal cycling damage, and chemical degradation. A declining cycle time (breakthrough happening sooner) is the early warning sign.

## See Also

- [Basic Gas Handling](basic.md) — piping, compressors, and gas distribution infrastructure
- [Air Separation & Bulk Gas Production](../chemistry/air-separation.md) — cryogenic distillation of liquid air
- [Hydrogen & Silane Production](../chemistry/hydrogen-silane.md) — ultra-pure hydrogen via Pd membrane
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — exhaust gas abatement via scrubbing
- [Vacuum Technology](vacuum.md) — vacuum system bake-out and outgassing management
- [Core Fab Processes](../photolithography/fab-processes.md) — gas purity requirements for CVD and PVD

[← Back to Gas Handling](index.md)
