# Polymer Elastomers

Process-level reference for elastomer materials in the tech tree. Covers natural rubber, synthetic rubbers, silicone elastomers, and the equipment needed to compound and cure them.

[← Polymers: Polymers & Composites](../polymers/overview.md)

## Precursors

All elastomers need vulcanization chemistry (sulfur or peroxide crosslinkers) and reinforcing fillers. Natural rubber comes from latex-bearing plants. Synthetic rubbers and silicones need petrochemical or chlorosilane feedstocks from [Petrochemicals](../petrochemicals/petroleum-alternatives.md).

### Natural Rubber

**Source**: Latex from *Hevea brasiliensis* (tropical), guayule shrub or Russian dandelion (temperate alternatives).

**Process**:
1. **Latex collection** — tapped from living trees or crushed from guayule/dandelion roots; 30-40% rubber hydrocarbon in latex emulsion
2. **Coagulation** — add dilute acetic or formic acid to break the emulsion; separate the rubber crumb
3. **Washing and drying** — remove residual acid and proteins; sheet or crepe form
4. **Mastication** — pass through two-roll mill or internal mixer to soften and reduce molecular weight; mechanical shearing at 40-80°C
5. **Compounding** — blend on mill or in Banbury mixer with:
   - Sulfur (1.5-3 phr) — crosslinking agent
   - Accelerators (e.g., mercaptobenzothiazole, 0.5-1.5 phr)
   - Zinc oxide (3-5 phr) — activator
   - Stearic acid (1-2 phr) — co-activator
   - Carbon black (20-50 phr) — reinforcement
   - Antioxidants (1-2 phr)
6. **Vulcanization** — compression molding or steam autoclave at **140-180°C**, **5-30 minutes** depending on thickness and accelerator system. Steam pressure 3-10 bar in autoclave mode.

**Cured properties**: Tensile strength 17-28 MPa, elongation at break 400-650%, good resilience and tear strength.

**Applications**: Tires, drive belts, seals, gaskets, electrical insulation, vibration dampers, hoses.

### Synthetic Rubber — Nitrile (NBR)

**Precursors**: Butadiene + acrylonitrile (both from [Petrochemicals](../petrochemicals/petroleum-alternatives.md) cracking and ammoxidation).

**Process**:
1. **Emulsion polymerization** — monomers emulsified in water with surfactant, free-radical initiator (persulfate or peroxide). Reaction at **30-50°C** (cold NBR for better properties) or up to 80°C (hot NBR). Polymerization time 6-12 hours.
2. **Short-stopping** — add terminating agent at ~70-80% conversion to control molecular weight
3. **Coagulation** — salt/acid addition to break emulsion; rubber crumb separated, washed, dried
4. **Compounding and vulcanization** — similar sulfur cure system to natural rubber; 150-180°C, 5-20 min

**Properties**: Oil and fuel resistance increases with acrylonitrile content (18-50%). Medium acrylonitrile grades (28-34%) balance oil resistance with low-temperature flexibility.

**Applications**: Fuel hoses, O-rings, oil seals, gaskets, gloves, hydraulic tubing.

### Silicone Elastomers

**Precursors**: Dimethyl dichlorosilane → hydrolysis → cyclic/linear siloxanes. Chlorosilane route ties to the Chemistry stage chloride chemistry and [Petrochemicals](../petrochemicals/petroleum-alternatives.md) silicon metal production.

**Process**:
1. **Base polymer** — polydimethylsiloxane (PDMS) gum, high molecular weight (300k-600k g/mol)
2. **Crosslinking methods**:
   - **Peroxide cure**: Mix PDMS with organic peroxide (dicumyl peroxide, benzoyl peroxide). Cure at **150-175°C**, 5-15 min. Peroxide decomposes to form free radicals that crosslink methyl groups.
   - **Platinum-catalyzed addition cure**: Vinyl-functional PDMS + Si-H crosslinker + Pt catalyst. Cures at **100-150°C** (or room temperature for RTV grades). Cleaner cure, no peroxide decomposition byproducts.
3. **Filler reinforcement** — fumed silica (10-40 phr) for mechanical strength; extends to 6-10 MPa tensile strength

**Properties**: Service temperature **-60 to 250°C**, excellent electrical insulation, good chemical inertness, low toxicity.

**Applications**: High-temperature seals and gaskets, medical tubing, mold-making compounds, electronic potting and encapsulation, food-grade tubing.

### Neoprene (Polychloroprene)

**Precursors**: Chloroprene monomer. Two routes: (a) acetylene + HCl (older route), or (b) butadiene + Cl₂ followed by dehydrochlorination (modern route, requires [Petrochemicals](../petrochemicals/petroleum-alternatives.md) butadiene).

**Process**:
1. **Monomer production** — butadiene chlorination at ~250°C, then caustic treatment to eliminate HCl and yield chloroprene
2. **Emulsion polymerization** — chloroprene in aqueous emulsion with free-radical initiator at **40-50°C**, 2-8 hours. Sulfur-modified grades use sulfur co-monomer for better processing.
3. **Compounding** — metal oxide cure system (zinc oxide + magnesium oxide, no sulfur needed); carbon black or silica reinforcement
4. **Vulcanization** — **150-180°C**, 5-20 min in compression mold or autoclave

**Properties**: Moderate oil and chemical resistance, good weather and ozone resistance, flame retardant (self-extinguishing due to chlorine content). Tensile strength 10-25 MPa.

**Applications**: Wetsuits, wire and cable insulation, conveyor belts, adhesive formulations, gaskets, industrial hoses.

### Elastomer Processing Equipment

| Equipment | Function | Phase Available | Notes |
|-----------|----------|-----------------|-------|
| Two-roll mill | Compounding, sheet formation, mastication | Machine Tools | Cast iron or steel rolls, adjustable gap, friction ratio 1:1.2 to 1:3 |
| Banbury internal mixer | High-shear batch compounding | Machine Tools+ | Faster than open mill, enclosed chamber with rotors |
| Calender | Continuous sheet formation to controlled thickness | Machine Tools+ | 3-4 roll configurations, 0.1-5 mm thickness range |
| Compression molding press | Vulcanization of shaped parts | Machine Tools+ | Hydraulic or mechanical, heated platens, 50-200 ton capacity |
| Steam autoclave | Batch vulcanization of extruded or wrapped goods | Energy | Steam at 3-10 bar, temperature control ±2°C |
| Extruder (rubber) | Continuous profiles (hoses, tubing, weatherstrip) | Machine Tools+ | Cold-feed or hot-feed screw design, downstream vulcanization |
| Autoclave/RTV chamber | Silicone curing (addition-cure grades) | Chemistry | Temperature-controlled oven, optional vacuum degassing |

Stage dependencies: Mills, calenders, and presses rely on Machine Tools stage cast iron and machining capability. Steam autoclaves require Energy stage boiler and steam systems. Silicone processing needs Chemistry stage chlorosilane chemistry.

### Key Milestones

- [ ] **Energy stage**: Natural rubber vulcanization (latex collection → sulfur cure → gaskets, belts, seals)
- [ ] **Energy stage**: Two-roll mill and compression press operational for rubber compounding
- [ ] **Chemistry stage**: Nitrile rubber (NBR) production once butadiene and acrylonitrile feedstocks available from Petrochemicals
- [ ] **Chemistry stage**: Neoprene production once chloroprene monomer route is established
- [ ] **Chemistry stage**: Calender and extruder operational for continuous rubber sheet and profiles
- [ ] **Chemistry stage**: Silicone elastomer production via peroxide cure once chlorosilane chemistry is online
- [ ] **Vacuum & Optics+**: Platinum-catalyzed silicone (addition cure) for precision medical and electronic-grade parts
- [ ] **Silicon+**: Fluoroelastomers for aggressive chemical environments (semiconductor fab seals, plasma equipment)

[← Polymers: Polymers & Composites](../polymers/overview.md)
