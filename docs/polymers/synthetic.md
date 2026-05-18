# Synthetic Polymers & Elastomers

> **Domain**: Polymers | **Node ID**: polymers.rubber.synthetic
> **Timeline**: Years 20-50
> **Outputs**: nitrile_rubber, neoprene, silicone_elastomers, polyurethane

Synthetic polymers fill gaps natural rubber cannot: oil resistance (NBR), flame retardancy (neoprene), extreme-temperature service (silicone), and tunable hardness (polyurethane). Each requires specific monomer feedstocks and controlled polymerization conditions. See [Rubber Production](./rubber.md) for natural rubber vulcanization and compounding recipes shared across all elastomers.

### Nitrile Rubber (NBR, Buna-N)

**Monomer source chain**:
- **Butadiene** (C₄H₆): Co-product of ethylene production via steam cracking of naphtha (750-900°C, 0.1-0.5 s residence). Also producible from ethanol via Lebedev process (2 C₂H₅OH → C₄H₆ + 2 H₂O + H₂ over ZnO/Al₂O₃ at 400-450°C) — the fermentation route, critical when petrochemicals are unavailable.
- **Acrylonitrile** (CH₂=CHCN): Propylene ammoxidation — CH₂=CHCH₃ + NH₃ + 1.5 O₂ → CH₂=CHCN + 3 H₂O over Bi-Mo oxide catalyst at 400-500°C. Requires propylene (steam cracking or FCC) and ammonia (Haber-Bosch).

**Emulsion copolymerization**:
- Reactor: Glass-lined or stainless steel stirred tank, 5-50 m³. Jacketed for temperature control.
- Charge: Butadiene (55-75 parts) + acrylonitrile (25-45 parts) + water (200 parts) + sodium dodecyl sulfate (emulsifier, 2-5 parts) + potassium persulfate or redox initiator (ferrous sulfate + hydroperoxide for cold process). Tertiary dodecyl mercaptan as chain transfer agent (0.3-0.5 parts) controls molecular weight.
- **Cold NBR** (30-50°C): Superior properties — more linear chains, less branching. Batch time 6-12 hours to 70-80% conversion. Short-stopped with hydroquinone or DMDTC. Coagulated with CaCl₂ or Al₂(SO₄)₃ + dilute acid. Washed, dried on hot roll dryer (80-100°C).
- **Hot NBR** (50-70°C): Faster reaction, more branching. Used when processing ease matters more than ultimate properties.

**Key property tradeoff**: Higher acrylonitrile content → better oil/fuel resistance, higher glass transition temperature (less flexible at low temperature). Grades: Low-ACN (18-22%, Tg ≈ -50°C), Medium-ACN (30-35%, Tg ≈ -35°C), High-ACN (40-50%, Tg ≈ -15°C).

**Applications**: Fuel hoses (High-ACN), oil seals and O-rings (Medium-ACN), chemical-resistant gloves for cleanroom and HF handling (Medium-ACN, 0.1-0.3 mm thin-wall dipped goods), printing rolls, conveyor belts for oily environments.

### Neoprene (Polychloroprene, CR)

**Monomer route — acetylene process**:
- **Acetylene** → chloroprene via two-step route: C₂H₂ + 2 HCl → 1,1-dichloroethane (CuCl₂ catalyst, 150-200°C). Dehydrochlorination: 1,1-C₂H₂Cl₂ → CH₂=CCl-CH=CH₂ (chloroprene) at 450-550°C over activated carbon. Overall yield ~70%.
- Alternative butadiene route (see [Rubber Production](./rubber.md)) uses butadiene + Cl₂ → dichlorobutene → chloroprene. Both routes are viable; acetylene route is simpler when calcium carbide → acetylene infrastructure exists.

**Polymerization**: Emulsion polymerization at 40-50°C, 2-8 hours. Sulfur-modified grades copolymerize with elemental sulfur (0.5-1.5%) for improved processing. Gel grades contain crosslinked domains for dimensional stability.

**Cure system**: Metal oxide cure — zinc oxide (5 phr) + magnesium oxide (4 phr). No sulfur required. MgO acts as acid scavenger (absorbs HCl released during processing). Cure 150-180°C, 5-20 minutes via compression molding or autoclave.

**Properties**: Moderate oil resistance (inferior to NBR but adequate for intermittent contact). Excellent weather, ozone, and UV resistance (chlorine content). Self-extinguishing — flame retardant without additives. Tensile strength 10-25 MPa, elongation 300-600%, Tg ≈ -45°C.

**Applications**: Wire and cable insulation (electrical + flame retardant), wetsuits (closed-cell foam — nitrogen-blown neoprene foam, 1.5-3 mm, provides thermal insulation in water), contact adhesives (solvent-based neoprene cement for woodworking and shoe assembly), conveyor belts, gaskets, vibration isolation mounts.

### Silicone Elastomers (PDMS)

**Precursor chain**: MG-Si + CH₃Cl → dimethyl dichlorosilane via Rochow-Müller process (Cu catalyst, 250-300°C) → hydrolysis → cyclic/linear siloxanes → polydimethylsiloxane (PDMS). See [Rubber Production](./rubber.md) for detailed precursor chemistry.

**Crosslinking systems** (practical selection guide):
- **Peroxide cure (HTV — high temperature vulcanizing)**: Mix PDMS gum (high molecular weight, ~500,000 g/mol) with dicumyl peroxide (0.5-2%) and fumed silica filler on two-roll mill. Cure 150-175°C, 5-15 min. Peroxide decomposes to free radicals that crosslink methyl groups. Leaves volatile byproducts — post-cure at 200°C for 2-4 hours to drive them off. Cheapest system. Used for: seals, gaskets, tubing.
- **Platinum addition cure (LSR — liquid silicone rubber)**: Two-part system — Part A (vinyl-functional PDMS + Pt catalyst at ~10 ppm) + Part B (vinyl PDMS + Si-H crosslinker). Mix 1:1, cure at 100-150°C or room temperature (RTV grades). No byproducts, precise stoichiometric cure. Superior dimensional accuracy. Used for: medical devices, food-contact items, optical components. Pt catalyst is expensive but used at extremely low loading.
- **RTV-1 (room temperature vulcanizing, single-component)**: Acetoxy-functional silane crosslinker cures on exposure to atmospheric moisture. Skin forms in 10-30 min, full cure 24-48 hours. Familiar as "bathtub caulk." Used for: sealing, bonding, potting.

**Filler**: Fumed silica (10-40 phr, 7-40 nm SiO₂ particles from flame hydrolysis of SiCl₄) is essential — unfilled PDMS has tensile strength <0.5 MPa; filled reaches 6-10 MPa. Extending filler (ground quartz, 50-200 phr) reduces cost for non-critical applications.

**Applications**: High-temperature seals and gaskets (service -60°C to +250°C — unmatched temperature range), medical tubing (biocompatible, sterilizable), electronic potting and encapsulation (excellent dielectric: ε ≈ 3, tan δ ≈ 0.001), mold-making (RTV for casting resins, low-tack release), bake-ware, food-grade tubing.

### Polyurethane (PU)

**Monomer sources**:
- **Diisocyanates**: Toluene diisocyanate (TDI) — toluene → dinitrotoluene (HNO₃) → reduction to TDA (catalytic hydrogenation) → phosgenation (COCl₂, from CO + Cl₂) → TDI. Or MDI — aniline + formaldehyde → MDA → phosgenation → MDI. Phosgene is extremely toxic (1 ppm lethal) — rigorous containment mandatory.
- **Polyols**: Polyether polyols from propylene oxide (propylene + O₂) + ethylene oxide (ethylene + O₂) polymerization initiated by glycerol or sucrose. Polyester polyols from dicarboxylic acids (adipic acid) + diols (ethylene glycol). Polyol molecular weight (200-10,000 g/mol) determines final polymer flexibility.
- **Chain extenders**: 1,4-butanediol or ethylene glycol (short diols that form hard segments).

**Foam formulations**:
- **Flexible foam** (mattresses, cushions): Polyether polyol (MW ~3000, 100 parts) + TDI (50-60 parts) + water (3-5 parts — generates CO₂ blowing agent: H₂O + NCO → urea + CO₂) + silicone surfactant (1 part) + stannous octoate catalyst (0.2 parts) + amine catalyst (0.3 parts). Cream time 10-15 s, rise time 60-90 s. Density 18-40 kg/m³.
- **Rigid foam** (insulation): Polyether polyol (MW ~400, highly functional, 100 parts) + polymeric MDI (130-180 parts) + water (1-2 parts) + HCFC or pentane blowing agent (10-20 parts) + silicone surfactant (2 parts) + amine catalyst (1 part). Density 28-50 kg/m³. Thermal conductivity 0.020-0.025 W/(m·K) — among the best insulation materials.

**Solid PU forms**:
- **Cast elastomers**: Prepolymer (isocyanate-terminated) + chain extender (BDO), mix and pour into heated mold. Cure 100-120°C, 30-60 min. Hardness Shore A 70 to Shore D 75. Applications: industrial wheels, rollers, bushings, wear pads. Abrasion resistance exceeds all other elastomers.
- **Coatings and adhesives**: Two-component PU coatings (polyol + isocyanate) cure to tough, chemical-resistant films. Used for floor coatings, marine finishes, protective topcoats.

**PU in the bootstrap context**: Rigid PU foam is the highest-performance insulation achievable at moderate technology level. It dramatically reduces energy needs for furnaces, kilns, refrigeration, and building heating. Flexible foam provides sealing gaskets and vibration damping. Cast PU rollers serve in wire saw wafering equipment and printing presses.

### Cross-References

- **Monomer precursors**: Petrochemical cracking products (ethylene, propylene, butadiene) from [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md). Ethanol-based butadiene from fermentation.
- **MG-Si for silicones**: [MG-Si Production](../silicon/mg-si-production.md)
- **Phosgene for isocyanates**: CO + Cl₂ over activated carbon — requires [chlor-alkali electrolysis](../chemistry/electrolysis.md) and CO from producer gas.
- **Vulcanization equipment**: Two-roll mills, Banbury mixers, compression molds — shared with [Rubber Production](./rubber.md)
