# Alkali Production

> **Node ID**: `chemistry.alkalis`
> **Also covers**: `energy.electrolysis`
> **Domain**: [Chemistry](./)
> **Dependencies**: `energy.electricity`, `mining`
> **Enables**: `specialty-gases.dopant-etch-gases`, `specialty-gases.hydrogen-silane`
> **Timeline**: Years 20-35
> **Outputs**: soda_ash, caustic_soda, sodium_carbonate, electrolysis, chlorine, hydrogen, oxygen, aluminum, caustic_soda, pure_copper
> **Note**: Electrolysis is listed under both Energy and Chemistry domains.

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
- **Electrolysis of brine** (preferred): See Electrolysis Scale-Up section below. Produces Cl₂ + H₂ + NaOH simultaneously. Most efficient route.

### Electrolysis Scale-Up

**Chlor-alkali process** (most important industrial electrolysis):
- **Cell types**:
  - **Diaphragm cell**: Asbestos or polymer diaphragm separates anode and cathode compartments. Prevents Cl₂ and NaOH from mixing (would form NaOCl — bleach). Products: Cl₂ gas, H₂ gas, 10-12% NaOH solution (requires evaporation to 50%).
  - **Membrane cell** (modern): Ion-exchange membrane (Nafion or equivalent — perfluorinated polymer, Chemistry+ chemistry). More efficient, produces directly 30-35% NaOH. But membrane requires PTFE-like fluoropolymer.
- **Anode**: Dimensionally stable anode (DSA) — titanium coated with RuO₂/IrO₂. Or graphite (cheaper, consumed slowly ~2-5 kg/tonne Cl₂). Carbon anodes work for startup.
- **Cathode**: Steel or nickel. Hydrogen evolves at cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻.
- **Operating conditions**: 3.2-3.8V per cell, 2-5 kA/m² current density. Temperature 80-90°C. NaCl concentration ~25%.
- **Energy consumption**: ~2,100-2,500 kWh per tonne of Cl₂. Major power load.

**Water electrolysis**:
- **Alkaline electrolyzer**: 25-30% KOH electrolyte. Nickel electrodes. Temperature 60-80°C. Cell voltage 1.8-2.2V. Current efficiency ~95-99%.
- **Products**: Ultra-pure H₂ and O₂. H₂ purity critical for semiconductor processes (the Silicon-Photolithography stage transition).
- **Energy**: ~50-55 kWh per kg H₂ (thermodynamic minimum 33 kWh/kg).

**Aluminum production** (Hall-Héroult process — enormous power consumer):
- **Feedstock**: Purified alumina (Al₂O₃) from bauxite via Bayer process: dissolve bauxite in hot NaOH (150-250°C, 5-30 bar), filter impurities (red mud), precipitate Al(OH)₃, calcine at 1100-1200°C → Al₂O₃.
- **Electrolysis**: Dissolve Al₂O₃ in molten cryolite (Na₃AlF₆, melting point 1012°C) at 950-1000°C. Carbon anodes, carbon-lined steel cathode. Al³⁺ + 3e⁻ → Al (liquid aluminum pools at bottom, tapped periodically). Carbon consumed: 2O²⁻ + C → CO₂.
- **Operating conditions**: 4.0-4.5V, 150-400 kA per cell, ~13-15 kWh/kg Al.
- **Power requirement**: A small aluminum plant (10,000 tonnes/year) needs ~15 MW continuous. This is why aluminum was more expensive than gold before cheap electricity.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
