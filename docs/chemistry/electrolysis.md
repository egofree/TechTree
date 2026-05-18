# Electrolysis

> **Node ID**: chemistry.electrolysis
> **Domain**: Chemistry
> **Timeline**: Years 20-30
> **Outputs**: electrolysis, chlorine, hydrogen, oxygen, aluminum, caustic_soda, pure_copper

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
- **Products**: Ultra-pure H₂ and O₂. H₂ purity critical for semiconductor processes (see [Hydrogen & Silane Production](hydrogen-silane.md)).
- **Energy**: ~50-55 kWh per kg H₂ (thermodynamic minimum 33 kWh/kg).

**Aluminum production** (Hall-Héroult process — enormous power consumer):
- **Feedstock**: Purified alumina (Al₂O₃) from bauxite via Bayer process: dissolve bauxite in hot NaOH (150-250°C, 5-30 bar), filter impurities (red mud), precipitate Al(OH)₃, calcine at 1100-1200°C → Al₂O₃.
- **Electrolysis**: Dissolve Al₂O₃ in molten cryolite (Na₃AlF₆, melting point 1012°C) at 950-1000°C. Carbon anodes, carbon-lined steel cathode. Al³⁺ + 3e⁻ → Al (liquid aluminum pools at bottom, tapped periodically). Carbon consumed: 2O²⁻ + C → CO₂.
- **Operating conditions**: 4.0-4.5V, 150-400 kA per cell, ~13-15 kWh/kg Al.
- **Power requirement**: A small aluminum plant (10,000 tonnes/year) needs ~15 MW continuous. This is why aluminum was more expensive than gold before cheap electricity.

**Copper electrorefining** (produces 99.99% pure Cu from impure anodes):
- **Cell**: Impure copper cast anode (from smelter, ~98-99% Cu). Pure copper starter sheet cathode (thin Cu foil). Electrolyte: CuSO₄ (150-200 g/L) + H₂SO₄ (150-200 g/L) in aqueous solution. Temperature 50-65°C.
- **Reaction**: Cu (anode) → Cu²⁺ + 2e⁻ (dissolution). Cu²⁺ + 2e⁻ → Cu (cathode, pure deposit). Cell voltage only 0.2-0.3 V (very low — most energy goes to pumping electrolyte, not overcoming thermodynamics). Current density: 200-300 A/m².
- **Impurities**: Ag, Au, Pt, Se, Te do not dissolve — settle as "anode slime" (valuable byproduct, recovered for precious metals). Ni, Fe, Zn dissolve but do not plate at cathode with proper voltage control. As, Sb, Bi must be controlled — can co-deposit.
- **Anode slime recovery**: Collect slime, treat with H₂SO₄ + oxidant → dissolve Cu, Se, Te. Melt residual → Doré metal (Ag + Au). Electrorefine silver. Gold and PGMs recovered from silver cell slimes. Revenue from precious metals often exceeds cost of copper refining.

### Electrode Materials & Cell Design

**Electrode materials by process**:

| Process | Anode | Cathode | Notes |
|---------|-------|---------|-------|
| Chlor-alkali | DSA (Ti + RuO₂/IrO₂) or graphite | Steel or nickel | Graphite consumed ~2-5 kg/t Cl₂ |
| Water electrolysis | Nickel or Ni-coated steel | Nickel or Ni-coated steel | Inert — neither electrode consumed |
| Aluminum | Carbon (consumed: C + O → CO₂) | Carbon-lined steel | Carbon is both electrode and reactant |
| Copper refining | Impure Cu (consumed) | Pure Cu starter sheet | Consumable anode — impurities left behind |

- **Selection criteria**: Inert electrodes (Pt, graphite, DSA) for processes where the electrode must not participate. Consumable electrodes (Cu, Zn, C) where anode dissolution is the desired reaction. Cost and availability dominate — graphite is cheap and versatile, DSA requires titanium and ruthenium.

**Cell configurations**:
- **Tank cell**: Simple rectangular tank (concrete or steel-lined). Electrodes hang in electrolyte. Batch or semi-continuous. Used for copper refining. Easy to build and maintain, but large footprint per unit production.
- **Filter press cell**: Flat electrodes and separators clamped together like a stack. Electrolyte flows through channels between plates. Continuous operation, compact, good heat removal. Used for chlor-alkali and advanced water electrolysis. Higher manufacturing precision required.
- **Membrane cell** (chlor-alkali specific): Ion-exchange membrane (Nafion) replaces diaphragm. Allows Na⁺ through but blocks Cl⁻ and OH⁻. Produces higher-purity NaOH directly at 30-35% concentration. Requires fluoropolymer chemistry.
