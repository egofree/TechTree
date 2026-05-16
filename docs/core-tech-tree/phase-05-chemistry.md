# Phase 5: Chemical Industry Scale-Up

**Timeline**: Years 20–35  
**Goal**: Bulk reagents, gases, and materials processing.  
**Dependencies**: [Phase 3](phase-03-machine-tools.md) (pumps, columns, valves, reactors), [Phase 4](phase-04-energy.md) (energy, electrolysis), [Phase 2](phase-02-metallurgy.md) (glass, ceramics)

## Objectives

- Produce bulk mineral acids (sulfuric, nitric, hydrochloric, hydrofluoric)
- Manufacture alkalis (soda ash, caustic soda)
- Scale electrolysis for industrial gases and metals
- Build distillation, reaction, and purification infrastructure
- Handle and purify industrial gases

## Key Technologies

### Sulfuric Acid (The "King of Chemicals")
- **Lead chamber process** (earlier, lower purity): SO₂ + NOx + H₂O + air in lead-lined chambers
- **Contact process** (later, higher purity): V₂O₅ catalyst, SO₂ → SO₃ → H₂SO₄
- Sulfur sources: elemental sulfur deposits, pyrite roasting, smelter off-gases
- Foundation for: nitric acid (via nitre + H₂SO₄), HCl, and most downstream chemistry

### Other Mineral Acids
- **Nitric acid**: NaNO₃ or KNO₃ + H₂SO₄ → HNO₃ (distillation)
- **Hydrochloric acid**: NaCl + H₂SO₄ → HCl (or direct H₂ + Cl₂ combustion)
- **Hydrofluoric acid**: CaF₂ (fluorite) + H₂SO₄ → HF (EXTREMELY HAZARDOUS)
  - HF dissolves glass — handles in plastic, lead, or wax-coated vessels
  - Critical for: silicon etching, glass etching, fluoride chemistry

### Alkali Production
- **Leblanc process**: NaCl + H₂SO₄ → Na₂SO₄ → Na₂CO₃ + CaS (with limestone/coal)
- **Solvay process** (more efficient, later): NaCl + NH₃ + CO₂ → NaHCO₃ → Na₂CO₃
  - Requires ammonia (from coal distillation or later Haber-Bosch)
- **Caustic soda (NaOH)**: Na₂CO₃ + Ca(OH)₂ → NaOH, or direct electrolysis of brine

### Electrolysis Scale-Up
- **Chlor-alkali process**: NaCl solution → Cl₂ + H₂ + NaOH
- **Water electrolysis**: H₂O → H₂ + O₂ (for high-purity gases)
- **Aluminum** (later): Hall-Héroult process (Al₂O₃ in molten cryolite)
- **Magnesium, sodium**: Electrolysis of molten salts

### Infrastructure
- **Distillation columns**: Fractional distillation for purification
- **Reactors**: Acid-resistant vessels (glass-lined, ceramic, lead)
- **Piping, valves, pumps**: Corrosion-resistant materials
- **Heat exchangers**: For process efficiency
- **Gas handling**: Compression, storage, purification (drying, scrubbing)

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| HF acid | Phase 7 (Si etching), Phase 8 (wafer etching) |
| H₂SO₄, HCl, HNO₃ | Phase 5 (all chemistry), Phase 7 (cleaning), Phase 8 (etching) |
| NaOH, Na₂CO₃ | Phase 5 (processes), Phase 7 (cleaning), glass production |
| H₂, O₂, N₂, Cl₂ | Phase 7 (atmosphere), Phase 8 (etch gases, CVD precursors) |
| Aluminum | Phase 6 (lightweight equipment), Phase 8 (metallization) |
| Distillation capability | Phase 7 (chlorosilane purification), Phase 8 (solvent purification) |

## Practical Bottlenecks

- **HF safety**: Hydrofluoric acid is uniquely dangerous — penetrates skin, attacks bone, systemic toxicity
- **Catalysts**: Vanadium pentoxide (contact process), platinum (catalysis) — may require sourcing
- **Corrosion resistance**: Handling hot acids requires specialized materials (glass-lined, lead, or later plastics)
- **Scale transition**: Lab chemistry → industrial tonnage is a massive engineering challenge

## Safety Concerns

- **HF acid**: Lethal even at small exposure — requires calcium gluconate gel on-site, full PPE
- **Acid burns**: H₂SO₄, HNO₃, HCl all cause severe chemical burns
- **Toxic gases**: Cl₂, HCl gas, NOx — ventilation and gas masks essential
- **Explosion risks**: H₂ is extremely flammable; dust explosions in chemical plants

## Purity Note

Start with industrial-grade purity for bulk chemicals. Semiconductor-grade purity requires additional distillation, filtration, and handling protocols that come later. This is an iterative process.

[← Phase 4](phase-04-energy.md) | [Overview](overview.md) | [Phase 6: Vacuum & Optics →](phase-06-vacuum-optics.md)
