# Passive Components

> **Node ID**: electronics.passive-components
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`chemistry.acids`](../chemistry/acids.md), [`ceramics`](../ceramics/index.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Enables**: [`electronics.power-electronics`](power-electronics.md), [`electronics.assembly`](assembly.md), [`computing.electronic`](../computing/electronic.md)
> **Timeline**: Years 15-40
> **Outputs**: resistors, capacitors, inductors, transformers
> **Critical**: Yes — every electronic circuit requires passive components for filtering, timing, impedance matching, and energy storage

## 1. Overview

Passive components — resistors, capacitors, and inductors — are the fundamental building blocks of every electronic circuit. Unlike active devices (transistors, diodes), passive components do not amplify signals. They control current flow, store energy, filter signals, set time constants, and provide impedance matching. A typical circuit board contains 5-20 passive components for every active device.

In the bootstrap chain, passive components bridge [electrical systems](electrical-systems.md) (power distribution) and [semiconductor devices](../silicon/basic-devices.md) (active electronics). Without capacitors, power supplies produce unusable rippled DC. Without resistors, transistor bias circuits cannot function. Without inductors, switching power converters and radio-frequency circuits are impossible.

This document covers construction methods for each passive component type at three levels: hand-built (survival/bootstrap), workshop (small-batch production), and industrial (automated mass production). The emphasis is on materials, construction techniques, and achievable parameter ranges at each level.

## 2. Prerequisites

### Materials
- **Copper wire**: Drawn from [electrolytic copper](../chemistry/electrolysis.md), diameters 0.05-2.0 mm, purity >99.9%
- **Carbon/graphite**: From [charcoal](../energy/charcoal.md) processing or mined graphite, purity >95%
- **Ceramic dielectrics**: Titanium dioxide (TiO₂), barium titanate (BaTiO₃) from [ceramics](../ceramics/index.md) production
- **Aluminum foil**: 6-20 μm thickness, >99% purity from [metals processing](../metals/iron-steel.md)
- **Insulation materials**: [Polymer films](../polymers/thermoplastics.md) (PVC, polyester, polypropylene), paper, mica
- **Ferrite powders**: Iron oxide (Fe₂O₃) + manganese oxide (MnO) or zinc oxide (ZnO), sintered at 1000-1300°C
- **Tin/lead solder**: From [metals smelting](../metals/index.md)

### Tools
- [Wire drawing dies](../machine-tools/machining.md) for consistent wire diameters
- [Winding machines](../machine-tools/index.md) for coils and transformers
- [Pottery kiln](../ceramics/index.md) or [electric furnace](../energy/electric-furnaces.md) for ceramic firing (1000-1400°C)
- Resistance bridge or multimeter for measurement (see [Electrical Instruments](../measurement/electrical-instruments.md))

### Knowledge
- Ohm's law: V = IR; resistivity: R = ρL/A
- Capacitance: C = ε₀εᵣA/d; energy storage: E = ½CV²
- Inductance: L = μ₀μᵣN²A/l; energy storage: E = ½LI²
- Reactance: X_C = 1/(2πfC); X_L = 2πfL
- Impedance: Z = √(R² + (X_L - X_C)²)

## 3. Bill of Materials

| Material | Quantity (per 1000 resistors, carbon comp) | Source | Alternatives |
|----------|-------------------------------------------|--------|-------------|
| Carbon powder (graphite, >95% C) | 0.5-1.0 kg | [Charcoal](../energy/charcoal.md) processing | Carbon black from incomplete combustion |
| Ceramic binder (clay) | 0.3-0.5 kg | [Ceramics](../ceramics/index.md) | Phenolic resin |
| Copper wire (0.5 mm dia) | 50-100 m | [Electrolysis](../chemistry/electrolysis.md) | Brass wire (higher resistance) |
| Insulating paint/lacquer | 0.1-0.2 L | [Polymers](../polymers/index.md) | Wax, shellac |

| Material | Quantity (per 1000 capacitors, ceramic disc) | Source | Alternatives |
|----------|---------------------------------------------|--------|-------------|
| Barium titanate powder (BaTiO₃) | 2-5 kg | [Ceramics](../ceramics/index.md) | Titanium dioxide (lower εᵣ) |
| Silver paste (for electrodes) | 0.1-0.2 kg | [Metals](../metals/index.md) | Copper paste (requires atmosphere control) |
| Ceramic binder | 0.3-0.5 kg | [Ceramics](../ceramics/index.md) | Organic binders |

| Material | Quantity (per 100 inductors, power) | Source | Alternatives |
|----------|-------------------------------------|--------|-------------|
| Copper magnet wire (0.2-1.0 mm) | 2-10 km | [Electrolysis](../chemistry/electrolysis.md) | Aluminum wire (larger diameter for same R) |
| Ferrite core material | 5-20 kg | [Ceramics](../ceramics/index.md) sintering | Iron powder + binder (lower μ, higher loss) |
| Insulating tape/ sleeving | 0.5-2.0 m² | [Polymers](../polymers/index.md) | Paper, cloth tape |

## 4. Process Description

### 4.1 Resistor Construction

#### Carbon Composition Resistors

1. Mix carbon powder with ceramic binder (clay or phenolic resin) in ratios from 5:1 (low resistance, ~10 Ω) to 1:10 (high resistance, ~10 MΩ). The carbon-to-binder ratio determines resistivity.
2. Press mixture into cylindrical pellets (6 mm dia × 18 mm long for ½W rating) at 50-100 MPa.
3. Embed tinned copper lead wires (0.6 mm dia, 30 mm long) into each end of the pellet before pressing.
4. Fire at 300-500°C for 1-2 hours to cure binder. Do not exceed 600°C — carbon oxidizes in air above 700°C.
5. Measure resistance. Sort into tolerance bands (±5%, ±10%, ±20%).
6. Coat with insulating paint or lacquer. Color-code with resistance value bands.
7. Mark value with paint bands (4-band or 5-band color code).

**Achievable range**: 1 Ω to 22 MΩ. Power ratings: ¼W to 2W. Tolerance: ±10-20% (hand-made), ±5% (controlled process).

#### Wire-Wound Resistors

1. Select resistance wire: nichrome (Ni-Cr 80/20, ρ = 1.10 × 10⁻⁶ Ω·m) or constantan (Cu-Ni 55/45, ρ = 0.49 × 10⁻⁶ Ω·m).
2. Calculate wire length: L = R × A / ρ, where A is wire cross-section area.
3. Wind wire tightly onto ceramic or fiberglass core (3-15 mm dia × 10-50 mm long). For non-inductive winding, use bifilar technique (fold wire in half, wind both halves together — opposing fields cancel).
4. Secure wire ends with mechanical clamps or spot-weld to terminal lugs.
5. Coat with vitreous enamel (fire at 700-900°C) or silicone cement for high-power types.

**Achievable range**: 0.1 Ω to 100 kΩ. Power ratings: 1W to 200W. Tolerance: ±1-5%. Inductance is a concern — use bifilar winding for precision or high-frequency applications.

#### Film Resistors (Metal Film / Carbon Film)

1. Deposit thin resistive film onto ceramic rod (2-4 mm dia × 6-12 mm long). Carbon film: pyrolytic deposition from hydrocarbon gas at 900-1100°C. Metal film: sputtering or evaporation of Ni-Cr alloy (50-200 nm thick).
2. Cut a helical groove through the film using a diamond-tipped cutting tool. The groove lengthens the current path, increasing resistance. Trim to target value by adjusting groove pitch.
3. Crimp end caps with lead wires. Coat with epoxy.

**Achievable range**: 1 Ω to 10 MΩ. Power: ⅛W to 1W. Tolerance: ±0.1-1%. Best stability and lowest noise of all types.

### 4.2 Capacitor Construction

#### Ceramic Disc Capacitors

1. Mix BaTiO₃ powder with organic binder (paraffin wax or PVA). Press into discs (5-15 mm dia × 1-3 mm thick) at 50-100 MPa.
2. Sinter at 1200-1350°C for 1-4 hours. Cool slowly (2-5°C/min through Curie point at ~120°C for BaTiO₃) to achieve desired crystal structure.
3. Apply silver paste electrodes to both faces. Fire at 600-800°C for 10-20 minutes to bond silver to ceramic.
4. Solder tinned copper leads (0.6 mm dia) to silver electrodes.
5. Dip in phenolic or epoxy coating for insulation and moisture protection.

**Achievable range**: 1 pF to 100 nF (Class 1, NP0/C0G), 100 pF to 10 μF (Class 2, X7R/Y5V). Voltage ratings: 50V to 5000V. Tolerance: ±5% (Class 1), +80/-20% (Class 2).

#### Electrolytic Capacitors (Wet)

1. Etch aluminum foil (0.05-0.1 mm thick) in HCl or NaOH solution to increase surface area 20-200×. Etch pit depth: 1-50 μm.
2. Form the dielectric (Al₂O₃) by anodizing the etched foil in boric acid or ammonium pentaborate solution at 50-600V DC. Oxide thickness: 1.2-1.5 nm/V of formation voltage. Formation time: 30-120 minutes.
3. Layer: anode foil + electrolyte-soaked paper separator + cathode foil. Roll into cylindrical winding (6-35 mm dia × 10-50 mm long).
4. Insert winding into aluminum can. Impregnate with electrolyte (ethylene glycol + boric acid + ammonium salts, resistivity 100-300 Ω·cm).
5. Seal with rubber bung and aluminum lid. Crimp or weld closure. Form safety vent (scored aluminum or rubber plug that releases at 2-10 atm).

**Achievable range**: 0.1 μF to 1 F. Voltage: 3V to 600V. Tolerance: ±20%. ESR: 0.01-10 Ω depending on size/frequency. Lifetime: 2000-15,000 hours at rated temperature (85°C or 105°C).

#### Film Capacitors

1. Draw [polymer film](../polymers/thermoplastics.md) to 2-20 μm thickness (polyester, polypropylene, or polycarbonate).
2. Vacuum-deposit aluminum (20-50 nm) onto one or both sides of film as electrodes. Alternatively, use separate metal foil layers.
3. Wind two metallized films offset by 1-2 mm (so each extends beyond the other on opposite sides). Roll into cylindrical or rectangular form.
4. Spray zinc or solder metal end coatings (schoopage) to contact the exposed metal edges on each end.
5. Attach leads to end coatings by soldering or welding. Encapsulate in epoxy.

**Achievable range**: 100 pF to 100 μF. Voltage: 50V to 2000V. Tolerance: ±1-5%. Self-healing: metallized types clear localized shorts by evaporating the thin metal around the fault.

### 4.3 Inductor Construction

1. Select core material: air core (no core, lowest inductance), iron powder (μᵣ = 10-100), ferrite (μᵣ = 500-15,000). Core geometry: rod, toroid, E-core, pot core.
2. Calculate turns: N = √(L × l / (μ₀ × μᵣ × A)), where L = desired inductance, l = magnetic path length, A = core cross-section area.
3. Wind copper magnet wire (enameled, 0.05-2.0 mm dia) onto core. Layer winding for solenoids; sectional or progressive winding for high-frequency toroids.
4. For E-core or pot core types: assemble core halves around winding, clamp or cement. Gap the core (insert paper or plastic shim) to prevent saturation: gap length l_g = μ₀ × N² × A / L.
5. Insulate and secure winding with tape or varnish dip (impregnate at 100-130°C for 1-4 hours to improve thermal and mechanical stability).
6. Tin lead ends by removing enamel (mechanically or with solder pot at 400-450°C).

**Achievable range**: 1 nH to 100 H. Current: 1 mA to 1000A (size-dependent). Frequency: DC to 100 MHz (core-dependent).

## 5. Quantitative Parameters

### Resistor Parameters

| Parameter | Carbon Composition | Wire-Wound | Metal Film |
|-----------|-------------------|------------|------------|
| Resistance range | 1 Ω — 22 MΩ | 0.1 Ω — 100 kΩ | 1 Ω — 10 MΩ |
| Power rating | ¼ — 2W | 1 — 200W | ⅛ — 1W |
| Tolerance | ±10-20% | ±1-5% | ±0.1-1% |
| Temperature coefficient | ±500-2000 ppm/°C | ±20-100 ppm/°C | ±5-50 ppm/°C |
| Voltage coefficient | 200-2000 ppm/V | <1 ppm/V | <1 ppm/V |
| Maximum voltage | 250-500V | 200-1000V | 200-500V |
| Noise | High (carbon) | Very low | Very low |
| Frequency response | Poor (>100 kHz) | Poor (inductive) | Good (>100 MHz) |
| Stability (1000h at 70°C) | ±5-15% | ±0.1-1% | ±0.1-0.5% |
| Operating temperature | -55 to 125°C | -55 to 250°C | -55 to 175°C |

### Capacitor Parameters

| Parameter | Ceramic (C0G) | Ceramic (X7R) | Electrolytic (Al) | Film (PP) |
|-----------|--------------|----------------|-------------------|-----------|
| Capacitance range | 1 pF — 100 nF | 100 pF — 10 μF | 0.1 μF — 1 F | 100 pF — 100 μF |
| Tolerance | ±5% | ±10 to +80/-20% | ±20% | ±1-5% |
| Temperature range | -55 to 125°C | -55 to 125°C | -40 to 105°C | -40 to 105°C |
| Temp. coefficient | 0 ±30 ppm/°C | ±15% over range | ±0.5-2%/°C | ±1-2% over range |
| Voltage range | 50 — 5000V | 10 — 200V | 3 — 600V | 50 — 2000V |
| Dissipation factor | <0.1% | 1-5% | 5-25% | <0.1% |
| ESR (at 1 kHz) | <1 mΩ | 10-100 mΩ | 10-1000 mΩ | 1-50 mΩ |
| Leakage current | — | — | 0.01 CV μA | — |
| Lifetime (at rated temp) | Unlimited | Unlimited | 2000-15,000 hours | Unlimited |

### Inductor Parameters

| Parameter | Air Core | Iron Powder | MnZn Ferrite | NiZn Ferrite |
|-----------|----------|-------------|--------------|--------------|
| Inductance range | 1 nH — 100 μH | 1 μH — 100 mH | 100 μH — 100 H | 10 μH — 10 mH |
| Permeability (μᵣ) | 1 | 10-100 | 1500-15,000 | 100-1500 |
| Frequency range | 1 MHz — 1 GHz | 1 kHz — 5 MHz | 1 kHz — 2 MHz | 500 kHz — 100 MHz |
| Saturation flux density | — | 1.0-1.5 T | 0.3-0.5 T | 0.2-0.35 T |
| Core loss (at 100 kHz, 100 mT) | — | 200-500 mW/cm³ | 50-200 mW/cm³ | 100-300 mW/cm³ |
| Max operating temperature | Wire insulation limit | 200°C | 100-150°C (Curie) | 150-250°C |
| Typical applications | RF tuning, filters | EMI suppression, DC-DC | Power transformers, inductors | RF transformers, antennas |

## 6. Scaling Notes

### From Workshop to Production

- **Bench scale**: Hand-wind coils, hand-mix carbon resistor compositions. Output: 10-50 components per day. Resistance tolerance ±20%. Suitable for prototyping and one-off circuits.
- **Pilot scale**: Semi-automatic winding machines, hydraulic press for ceramic discs. Output: 100-1000 components per day. Tolerance improves to ±5-10%. Justifies dedicated resistor/capacitor production lines.
- **Production scale**: Automated winding, tape-and-reel packaging, automated testing and sorting. Output: 10,000-1,000,000 components per day. Tolerance ±0.1-1%. Laser trimming for precision resistors achieves ±0.01%.

### Scale Bottlenecks

- **Wire drawing**: Consistent magnet wire requires precision dies and annealing ovens. Wire diameter variation of ±5% causes inductance variation of ±10%.
- **Ceramic sintering**: Kiln temperature uniformity (±5°C) directly affects dielectric constant and capacitor tolerance. Batch-to-batch variation dominates over within-batch variation.
- **Ferrite processing**: Sintering atmosphere (air vs. nitrogen) and cooling rate through Curie temperature control permeability within a factor of 2-3×. Requires tight process control for repeatable inductors.
- **Etching (electrolytic capacitors)**: Etch uniformity across the foil determines capacitance consistency. Foil-to-foil variation of ±20% is common.

### Minimum Economic Scale

A workshop producing 500-1000 passive components per week justifies dedicated winding and pressing equipment. Below this, hand-wound coils and hand-mixed resistors suffice for circuit prototyping.

## 7. Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Resistor drift >10% over time | Moisture absorption in carbon comp | Coat with moisture-resistant lacquer; use film resistors instead |
| Carbon resistor value too high | Insufficient carbon content or poor mixing | Increase carbon-to-binder ratio; mix longer for homogeneity |
| Wire-wound resistor inductance causes oscillation | Inductive winding at high frequency | Use bifilar (non-inductive) winding; switch to film resistor |
| Capacitor short circuit | Dielectric breakdown from overvoltage | Derate voltage to 50-70% of rating; use thicker dielectric |
| Electrolytic capacitor bulging/venting | Internal pressure from electrolyte decomposition | Check for reverse polarity; reduce ripple current; replace |
| Electrolytic capacitor high ESR | Electrolyte drying out | Replace; operate below 85°C; use higher-temperature rated part |
| Film capacitor value shifts with temperature | Wrong dielectric material | Switch from polyester (high TC) to polypropylene (low TC) |
| Inductor saturates at lower current than expected | Core gap too small or missing | Increase core gap length; use larger core cross-section |
| Toroid winding has high inter-winding capacitance | Turns wound too uniformly (layered) | Use progressive (sector) winding to reduce distributed capacitance |
| Ferrite core cracks during assembly | Mechanical stress from clamping | Use cushioning gasket; do not over-tighten clamps |
| Resistor noise in audio circuits | Carbon composition type inherently noisy | Replace with metal film (lower noise by 10-100×) |

## 8. Safety

- **Electrolytic capacitor explosion risk**: Electrolytic capacitors contain volatile electrolyte. Reverse polarity, overvoltage, or excessive ripple current causes internal heating, gas generation, and pressure buildup. The safety vent is designed to release at 2-10 atm — but if the vent fails, the can ruptures violently, spraying hot electrolyte (corrosive, contains boric acid and organic solvents). Wear eye protection when working with large electrolytic capacitors (>100 μF, >50V). Discharge all capacitors through a 100-1000 Ω resistor before handling. Never apply AC voltage to a polarized capacitor.
- **Ceramic dust inhalation**: Grinding or sanding fired ceramic capacitors and ferrite cores generates fine silica and metal oxide dust (BaTiO₃, Fe₂O₃, MnO). Use dust extraction and a particulate respirator (N95 or better). Barium compounds are toxic if ingested — wash hands after handling BaTiO₃ powder.
- **Wire drawing hazards**: Drawing fine magnet wire involves high-speed rotating capstans and sharp dies. Pinch points. The soapy drawing lubricant is slippery — keep floors clear. Burns from annealing ovens at 400-600°C — use heat-resistant gloves.
- **Lead solder fumes**: When tinning resistor or capacitor leads with Sn/Pb solder, lead oxide fumes and flux vapors are generated. Use local exhaust ventilation (fume extractor at 0.3-0.5 m/s capture velocity). Lead-free solder (SAC305, Sn/Cu) eliminates lead exposure but requires higher temperatures (217-227°C).
- **Kiln/furnace hazards**: Sintering ceramics and ferrites requires 1000-1350°C kilns. Surface temperature of kiln exterior: 60-120°C — burn risk. Use thermal gloves and face shield when loading/unloading. Ensure adequate ventilation — organic binders burn off during firing, producing CO, CO₂, and volatile organic compounds.

## 9. Quality Control

### Resistor Testing
- **Resistance measurement**: 4-wire (Kelvin) method for values <10 Ω. Bridge or DMM for 10 Ω to 10 MΩ. Accuracy requirement: 4× better than the tolerance being verified (e.g., measure ±5% resistors to ±1.25%).
- **Temperature coefficient test**: Measure resistance at -55°C, +25°C, +125°C. Calculate TCR = (R₂-R₁)/(R₁ × (T₂-T₁)). Must be within specified ppm/°C range.
- **Load life test**: Apply rated power at 70°C for 1000 hours. Resistance drift must remain within ±5% (carbon comp) or ±1% (film).
- **Voltage coefficient test**: Measure at 10% and 100% rated voltage. Carbon composition: VCR <2000 ppm/V. Film: VCR <1 ppm/V.

### Capacitor Testing
- **Capacitance and dissipation factor**: Measure at 1 kHz (1 MHz for small ceramics) using LCR meter or capacitance bridge. Tolerance must match specification.
- **Insulation resistance**: Apply rated voltage DC for 60 seconds. Leakage current: I < 0.01 × C × V (μA). Equivalent: IR > 100/C (MΩ·μF product). Lower limit: 1000 MΩ for ceramic, 10,000 MΩ for film.
- **Voltage proof (hi-pot)**: Apply 2-3× rated voltage for 5-60 seconds. No breakdown or flashover.
- **ESR measurement**: At 100 kHz for electrolytic, compare to specification. ESR increase >50% from initial value indicates degradation.

### Inductor Testing
- **Inductance measurement**: LCR meter at operating frequency. Tolerance: typically ±5-10%.
- **Saturation current test**: Increase DC bias current until inductance drops 10-30% from zero-bias value. Record I_sat. Must meet or exceed rated value.
- **Core loss measurement**: Apply AC voltage at operating frequency. Measure core temperature rise. Calculate loss from temperature rise: P_core = m × C_p × ΔT/Δt.
- **Hi-pot test**: 500-2000V between winding and core for 60 seconds. Leakage <1 mA.

## 10. Variations and Alternatives

| Component Type | Alternative | Trade-off |
|---------------|-------------|-----------|
| Carbon comp resistor | Metal film resistor | Film has better stability, lower noise, tighter tolerance; carbon comp handles transient pulses better |
| Wire-wound resistor | Thick film (cermet) resistor | Thick film is non-inductive, smaller; wire-wound handles higher power, lower TCR |
| Ceramic capacitor | Mica capacitor | Mica has better stability and lower loss; ceramic has higher volumetric efficiency |
| Electrolytic capacitor | Tantalum capacitor | Tantalum has higher CV per volume, lower ESR; but higher cost and failure mode is dramatic (ignition) |
| Aluminum electrolytic | Solid polymer electrolytic | Polymer has much lower ESR, longer life; but lower voltage range (2-35V) and higher cost |
| Film capacitor | Paper capacitor (oil-filled) | Paper/oil handles higher voltage and power; film has lower loss and better stability |
| Ferrite core inductor | Iron powder core inductor | Iron powder has higher saturation (1.0-1.5T vs. 0.3-0.5T); ferrite has lower loss at high frequency |
| Toroidal inductor | E-core inductor | Toroid has lower EMI radiation and higher inductance per turn; E-core is easier to wind and allows gap adjustment |

### Historical Bootstrap Methods
- **Early resistors**: Pencil lead (carbon-clay composite, ~20-200 Ω depending on hardness). Length of nichrome wire wrapped on a form. Lamp black (soot) mixed with shellac.
- **Early capacitors**: Leyden jar (glass jar with tin foil inside and outside, ~100-1000 pF at 10-50 kV). Mica sheets with tin foil layers. Paper soaked in beeswax with aluminum foil.
- **Early inductors**: Coils wound on wooden or cardboard forms. Iron wire bundles as cores (high loss but available early). Crystal radio coils: 50-200 turns of wire on oatmeal box (air core, 100-500 μH).

### Regional Adaptations
- Where barium is unavailable, use titanium dioxide (TiO₂, εᵣ ≈ 100) for ceramic capacitors instead of BaTiO₃ (εᵣ ≈ 1000-10000). Lower capacitance per volume but adequate for many applications.
- Where petrochemical-derived polymer films are unavailable, use oil-impregnated paper as capacitor dielectric. Voltage rating and reliability are lower, but functional.
- Where nickel-chromium alloy is unavailable for resistance wire, use iron wire (ρ = 0.97 × 10⁻⁷ Ω·m, high TCR of +5000 ppm/°C) or constantan if copper-nickel alloy is available.

## 11. References

- **[Electronics Assembly](assembly.md)**: passive component mounting and soldering on PCBs
- **[Electrical Systems](electrical-systems.md)**: power distribution using transformers and inductors
- **[Basic Semiconductor Devices](../silicon/basic-devices.md)**: active devices that require passive components for bias and filtering
- **[Power Electronics](power-electronics.md)**: converters that rely on capacitors and inductors as energy storage elements
- **[Ceramics](../ceramics/index.md)**: ceramic substrate and dielectric material production
- **[Electrolysis](../chemistry/electrolysis.md)**: copper and aluminum production for conductors and capacitor foils
- **[Polymers](../polymers/thermoplastics.md)**: insulation films and encapsulation materials
- **[Charcoal](../energy/charcoal.md)**: carbon source for composition resistors

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electronics](./index.md) • [All Domains](../index.md)*
