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

### Storage & Distribution

**Hydrogen storage**:
- **Compressed gas**: Steel or composite cylinders at 200-700 bar. Simple and widely used. Energy density: 0.8-2.7 MJ/L at 200-700 bar. Heavier than other options per unit energy stored.
- **Metal hydrides**: LaNi₅ (lanthanum-nickel) or FeTi (iron-titanium) alloys absorb H₂ at moderate pressure (2-10 bar), release on heating (50-100°C). Safe — no high-pressure gas. Heavy (2-5% H₂ by weight). Good for stationary storage.
- **Cryogenic liquid H₂**: Liquefy at −253°C (20 K). Density 0.071 kg/L (much higher than compressed gas). Requires vacuum-insulated dewar. Boil-off 0.5-1%/day. Energy cost to liquefy: ~30% of H₂ energy content.

**Pipeline materials**:
- **Hydrogen**: Stainless steel 316L preferred. Carbon steel susceptible to hydrogen embrittlement (H₂ atoms diffuse into steel lattice, cause cracking under stress). Welded joints only — no threaded connections. Design for low stress. For low-pressure distribution: copper or polyethylene tubing acceptable.
- **Silane**: Electropolished stainless steel (316L or 304L) with PTFE-lined valves. VCR-type face-seal fittings — no elastomer O-rings (silane attacks many organics). All lines purged with N₂ or Ar before introducing silane. Minimum dead legs (pockets where gas can stagnate).
- **Leak detection**: Thermal conductivity sensors (silane has different thermal conductivity than air). Hydrogen: catalytic sensors or electrochemical cells. Ultrasonic leak detectors for high-pressure lines. Check all joints with helium mass spectrometer during commissioning.

### Quality Analysis

- **Gas chromatography (GC)**: Separate gas mixture on packed column (molecular sieve or porous polymer), detect with thermal conductivity detector (TCD). Quantifies impurities to ppm levels. Essential for H₂ purity (N₂, O₂, CO, CO₂, CH₄ contaminants) and SiH₄ purity (Si₂H₆, Si₃H₈, chlorosilanes, hydrocarbons).
- **Dew point measurement**: Quantifies moisture content. Aluminum oxide or capacitive sensor. Moisture is critical contaminant — causes oxidation in semiconductor processes. H₂ dew point must be below −70°C (<2.6 ppm H₂O).
- **Oxygen analyzer**: Electrochemical or zirconia sensor. O₂ in H₂ must be <1 ppm for semiconductor use.
- **Purity grades**: Semiconductor-grade H₂ requires >99.9999% (6N) purity. Silane for CVD requires >99.9% (3N) minimum, preferably >99.99% (4N). Each "N" represents an order of magnitude reduction in total impurities.

