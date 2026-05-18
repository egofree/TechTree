# Hydrogen & Silane Production

> **Node ID**: chemistry.hydrogen-silane
> **Domain**: Chemistry
> **Timeline**: Years 25-50
> **Outputs**: hydrogen, silane, trichlorosilane

### Hydrogen Production

**Electrolysis of water**:
- **Apparatus**: Electrolytic cell with nickel or platinum electrodes. Electrolyte: 20-30% KOH solution (better conductivity than pure water, prevents corrosion of electrodes). Steel cell body. Asbestos or polymer diaphragm separates anode and cathode compartments (prevents H₂ and O₂ mixing).
- **Reactions**: Cathode: 2H₂O + 2e⁻ → H₂ + 2OH⁻. Anode: 2OH⁻ → ½O₂ + H₂O + 2e⁻. Overall: 2H₂O → 2H₂ + O₂.
- **Conditions**: 1.8-2.2 V per cell, 50-80°C, 0.1-3 MPa pressure. Current density 200-400 mA/cm². Stack multiple cells in series for desired production rate.
- **Energy consumption**: ~4-5 kWh per Nm³ H₂ (theoretical minimum 3.0 kWh/Nm³). Production rate proportional to current (Faraday's law: 1 A produces ~0.42 L H₂/hour at STP).
- **Purification**: Pass through palladium membrane (Pd tube heated to 300-400°C — only H₂ diffuses through Pd lattice, all other gases excluded). Or catalytic recombination (remove O₂ traces by reacting with H₂ over platinum catalyst → water, remove water with desiccant). Achieve 99.999%+ purity.

**Steam reforming** (Chemistry+, if natural gas or methane available):
- CH₄ + H₂O → CO + 3H₂ (endothermic, 700-900°C, Ni catalyst, 2-3 MPa)
- CO + H₂O → CO₂ + H₂ (water-gas shift, 350-450°C, Fe/Cr oxide catalyst)
- Remove CO₂ with amine scrubber or pressure swing adsorption (PSA). Result: 95-99% H₂.
- Much cheaper than electrolysis if methane is available.

### Silane Production (SiH₄)

**Process route** (from MG-Si, Silicon stage):
1. **Trichlorosilane synthesis**: MG-Si + 3HCl → SiHCl₃ + H₂ (fluidized bed reactor, 280-350°C, Cu catalyst). SiHCl₃ boils at 31.8°C — distill from higher-boiling SiCl₄ (bp 57.6°C) and lower-boiling gases.
2. **Redistribution reaction**: 4SiHCl₃ → 3SiCl₄ + SiH₄ (catalytic reactor, 60-80°C). Silane (SiH₄) boils at -112°C — cryogenically distill from SiCl₄.
3. **Purification**: Fractional distillation at cryogenic temperatures. Final purification through molecular sieves and catalytic getters (remove trace chlorosilanes, moisture, methane). Purity requirement: 99.9999%+ (6N+) for semiconductor use.

**Properties and handling**:
- Pyrophoric — spontaneously ignites on contact with air (auto-ignition temperature: room temperature or below for impure silane). Burns with intense flame.
- Storage and transport in stainless steel cylinders, under inert gas pressure. Piping: electropolished stainless steel, welded or VCR-type fittings (no threaded connections — leak potential). All lines purged with N₂ or Ar before introducing silane.
- Leak detection: silane sniffers (thermal conductivity sensors). If silane leaks and ignites, water spray to cool surroundings — do not attempt to extinguish burning silane (let it burn off, the alternative is accumulating explosive gas).
- **NEVER** allow silane to accumulate in confined spaces. Even 2-3% concentration in air can auto-detonate.

