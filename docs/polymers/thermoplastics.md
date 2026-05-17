# Thermoplastic Polymers

Process-level reference for thermoplastics relevant to the tech tree. Covers synthesis routes, processing conditions, properties, and key applications. Feedstocks come from [Petrochemicals](../petrochemicals/petroleum-alternatives.md); polymerization reactors and extruders rely on the Machine Tools stage.

## Polymer Processes

### Polyethylene (PE)

Ethylene gas polymerization. Two industrial routes with very different conditions:

**LDPE** (low-density): High-pressure free radical process. 1000-3000 atm, 100-300°C, peroxide initiator (e.g., benzoyl peroxide). Tubular or autoclave reactor. Branched chain structure gives flexible, transparent material.

**HDPE** (high-density): Low-pressure Ziegler-Natta process. 1-20 atm, 50-80°C, TiCl₄/AlEt₃ catalyst system. Linear chain structure yields stiffer, stronger material with higher crystallinity.

Properties: chemically resistant, easy processing, inexpensive, good electrical insulator. Applications: containers, piping, cable insulation, moisture barriers, blown film, geomembranes.

### Polyvinyl Chloride (PVC)

Monomer route: ethylene + Cl₂ → 1,2-dichloroethane (EDC) → thermal pyrolysis at 450-550°C → vinyl chloride monomer (VCM) + HCl byproduct.

Polymerization: suspension process. Water continuous phase, 40-70°C, peroxide initiator (e.g., lauroyl peroxide). PVC powder recovered by centrifugation and drying.

- **Rigid PVC** (uPVC): no plasticizer. Pipes, fittings, valves, chemical-resistant ductwork.
- **Flexible PVC**: add plasticizers (DOP, DINP at 20-50 phr) for tubing, wire insulation, flooring, sheet goods.

Note: VCM is a confirmed human carcinogen. Monomer handling requires closed systems, leak detection, and exposure monitoring. Residual VCM in finished product must meet regulatory limits.

### Nylon (Polyamide)

**Nylon 6,6**: adipic acid + hexamethylenediamine → nylon salt (pH-controlled aqueous solution) → melt condensation polymerization in autoclave at 250-280°C. Vacuum applied in later stages to drive off water and push molecular weight up.

**Nylon 6**: caprolactam ring-opening polymerization at ~260°C, water-initiated. Simpler single-monomer route but slightly different property profile.

Properties: high tensile strength, low coefficient of friction, excellent abrasion resistance, moderate moisture absorption (affects dimensions). Applications: bearings, gears, fibers (rope, textile, tire cord), fasteners, monofilament, engineering components.

### Polystyrene (PS)

Styrene polymerization via free radical mechanism. 80-120°C, bulk or suspension process. Peroxide or thermal self-initiation.

- **Crystal PS**: transparent, rigid, brittle. Good optical clarity and dimensional stability. Disposable labware, optical components, packaging.
- **Expanded PS (EPS)**: impregnate PS beads with pentane blowing agent (3-8%), then steam expansion at ~100°C in closed molds. Lightweight insulation foam. Packaging, insulation board, disposable food containers.

### PTFE (Teflon)

Precursor chain (requires careful temperature control at each stage):

1. Chloroform + HF (antimony pentafluoride catalyst) → chlorodifluoromethane (R-22)
2. R-22 pyrolysis at 650-700°C → tetrafluoroethylene (TFE) + byproduct HCl. This pyrolysis is not trivial: temperature must be tightly controlled to minimize hexafluoropropylene and perfluoroisobutylene byproducts, the latter being extremely toxic.

TFE polymerization: aqueous dispersion or granular process, 20-80°C, persulfate initiator (ammonium persulfate). High molecular weight achieved rapidly.

PTFE does not melt-flow like other thermoplastics. It must be **sintered** above its melting point (~380°C, well above most thermoplastics) in a controlled cycle, or paste-extruded with a lubricant carrier that is later evaporated off.

Properties: chemically inert (resists nearly all solvents, acids, and bases), very low coefficient of friction, service temperature range -200 to +260°C, excellent dielectric. Applications: chemically inert seals and gaskets, non-stick surfaces, wire insulation, bearing surfaces, diaphragm pump membranes.

### Name-Only Mentions

- **Polycarbonate**: bisphenol-A + phosgene interfacial condensation; impact-resistant windows, optical discs
- **ABS**: acrylonitrile + butadiene + styrene terpolymer; injection-molded housings, enclosures, pipe fittings
- **Acrylic (PMMA)**: methyl methacrylate bulk or suspension polymerization; transparent windows, optical components, light guides

## Key Milestones

- [ ] **Chemistry stage**: LDPE production via high-pressure autoclave (requires pressure vessel capability)
- [ ] **Chemistry stage**: Suspension PVC from ethylene/chlorine feedstocks (ties to chlorine plant from the Chemistry stage chemistry)
- [ ] **Chemistry stage**: Crystal PS from styrene monomer (simplest thermoplastic to start with)
- [ ] **Chemistry stage**: Nylon 6,6 condensation polymerization (requires vacuum-capable autoclave)
- [ ] **Chemistry stage**: HDPE via Ziegler-Natta catalyst (requires TiCl₄ from the Chemistry stage chlorosilane chemistry)
- [ ] **Chemistry stage**: PTFE precursor chain (R-22 from chloroform + HF; HF available from the Chemistry stage fluorspar processing)
- [ ] **Vacuum & Optics stage**: PTFE sintering at 380°C (requires furnace control beyond typical polymer processing)
- [ ] **Vacuum & Optics+**: EPS foam production (requires pentane recovery and steam molding)
