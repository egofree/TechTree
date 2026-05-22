# Advanced Ceramics & Refractories

> **Node ID**: ceramics.advanced-ceramics
> **Domain**: Ceramics & Refractories
> **Dependencies**: [Pottery & Clay Products](pottery.md), [Kiln Construction](kilns.md), [Mining](../mining/index.md)
> **Enables**: [Silicon](../silicon/index.md), [Energy](../energy/index.md)
> **Timeline**: Years 15-50
> **Outputs**: alumina ceramics, zirconia ceramics, silicon carbide, silicon nitride, refractory linings, ceramic insulation, technical ceramics

## Overview

Basic pottery and fireclay refractories serve well up to about 1200-1400°C. Beyond that — for steel furnaces, glass tanks, silicon processing, and chemical reactors — you need advanced ceramics: materials engineered for extreme temperatures, chemical resistance, wear resistance, and electrical insulation. This capability transforms ceramics from a craft into an industrial materials science.

The jump from earthenware to technical ceramics requires:
- **[Purer raw materials](../glossary/purer-raw-materials.md)** (mined bauxite, zircon sand, quartzite rather than common clay)
- **[Higher firing temperatures](../glossary/higher-firing-temperatures.md)** (1600-2200°C, requiring improved kilns and fuel)
- **[Precision forming](../glossary/precision-forming.md)** (dry pressing, isostatic pressing, slip casting with controlled rheology)
- **[Controlled atmospheres](../glossary/controlled-atmospheres.md)** (reducing, inert, or vacuum sintering)

## Alumina (Al₂O₃)

Alumina is the most widely used technical ceramic — hard, electrically insulating, chemically inert, and serviceable to 1700-1900°C.

### Raw Material: Bauxite and the Bayer Process

**[Bauxite](../glossary/bauxite.md)** is the primary aluminum ore, typically containing 40-60% Al₂O₃ as gibbsite (Al(OH)₃), boehmite (AlOOH), or diaspore (AlOOH). Found in tropical and subtropical lateritic deposits.

**[Bayer process](../glossary/bayer-process.md)** (produces high-purity alumina powder):
1. **[Crush and grind](../glossary/crush-and-grind.md)** bauxite ore to <150 μm
2. **[Digest](../glossary/digest.md)** in concentrated NaOH (caustic soda) at 140-240°C under pressure in autoclave. Aluminum hydroxides dissolve as sodium aluminate: Al(OH)₃ + NaOH → NaAl(OH)₄
3. **[Settle and filter](../glossary/settle-and-filter.md)** to remove insoluble red mud (iron oxides, silica, titania)
4. **[Precipitate](../glossary/precipitate.md)** aluminum trihydrate by seeding with fine Al(OH)₃ crystals and cooling. Pure Al(OH)₃ crystals form.
5. **[Calcine](../glossary/calcine.md)** at 1100-1200°C to drive off water: 2 Al(OH)₃ → Al₂O₃ + 3 H₂O. Produces α-alumina (corundum) powder, 99.0-99.99% pure.

The Bayer process requires caustic soda (from [alkali production](../chemistry/index.md)) and significant heat energy. Red mud disposal is an environmental challenge (highly alkaline waste).

### Alumina Ceramic Production

**Powder preparation**:
- Ball mill calcined alumina to 1-5 μm particle size (12-72 hours with alumina grinding media)
- Add organic binders (PVA, PEG) for green strength — 2-5% by weight
- Optionally spray-dry for free-flowing granules (50-200 μm spheres for automated pressing)

**Forming**:
- **Dry pressing**: Fill steel die with powder, apply 50-100 MPa uniaxial pressure. Simple shapes (tiles, disks, plates). Fast cycle (10-20 parts/minute). Green density ~60% theoretical. Wall thickness variation causes density gradients — limit aspect ratio.
- **Isostatic pressing**: Fill rubber mold with powder, apply 100-300 MPa hydrostatic pressure in oil-filled vessel. Uniform density in all directions. Complex shapes. Used for spark plug insulators, large tubes, radome domes.
- **Slip casting**: Disperse powder in water with deflocculant (sodium silicate). Pour into plaster mold. Water absorbs into plaster → solid layer builds. Drain excess. For thin-walled hollow shapes.
- **Extrusion**: Mix powder with plasticizers, force through die. Continuous lengths (tubes, rods, honeycomb structures).

**Sintering**:
- Heat to 1600-1800°C for 2-4 hours in air
- Shrinkage 15-20% — design green body oversized
- Ramp slowly (1-5°C/minute) through 200-600°C to burn out organics without cracking
- At peak temperature, atomic diffusion bonds particles → porosity decreases → density reaches 95-99% theoretical
- Cool slowly through critical ranges

### Properties and Applications

| Property | Value |
|----------|-------|
| Hardness | 9 Mohs (second only to diamond and SiC) |
| Compressive strength | 2000-3000 MPa |
| Flexural strength | 300-400 MPa |
| Electrical resistivity | >10¹⁴ Ω·cm |
| Dielectric constant | ~10 |
| Thermal conductivity | 25-35 W/(m·K) |
| Max service temperature | 1700-1900°C |

**Applications**:
- **Electrical insulators**: Spark plugs, high-voltage insulators, substrate for hybrid circuits, feedthroughs for vacuum chambers
- **Wear parts**: Valve seats, seals, bearings, thread guides
- **Cutting tools**: Alumina + TiC composite inserts for high-speed machining of cast iron and steel
- **Chemical-resistant linings**: Pipe linings, pump components for corrosive chemical handling
- **Ballistic armor**: Hard, lightweight ceramic tiles for personal and vehicle armor
- **Dental and medical implants**: Biocompatible, high strength
- **Semiconductor substrates**: 96% Al₂O₃ substrates cofired with tungsten metallization for hybrid circuit packages

## Zirconia (ZrO₂)

Zirconia combines extreme temperature resistance (up to 2200°C) with excellent thermal insulation and, when stabilized, good mechanical toughness.

### Raw Material: Zircon Sand

**[Zircon](../glossary/zircon.md)** (ZrSiO₄) is mined from heavy mineral sand deposits (beach sands, river placers). **[Baddeleyite](../glossary/baddeleyite.md)** (natural ZrO₂) is rarer but requires less processing.

**Chemical processing to pure ZrO₂**:
1. **Alkali fusion**: Mix zircon sand with NaOH, heat to 600-700°C → sodium zirconate forms
2. **Water leach**: Dissolve sodium zirconate in water, filter off insoluble silica
3. **Precipitation**: Add acid (HCl or H₂SO₄) to precipitate zirconium hydroxide
4. **Calcination**: Heat to 800-1000°C → pure ZrO₂ powder

### Phase Stabilization

Pure zirconia undergoes a destructive phase transformation at ~1170°C (monoclinic → tetragonal) with ~4% volume change. This causes catastrophic cracking during thermal cycling.

**Solution**: Add stabilizers (5-15 mol% Y₂O₃, CaO, or MgO) to maintain the cubic (or partially tetragonal) phase at all temperatures:
- **Fully stabilized zirconia (FSZ)**: 8-12 mol% Y₂O₃. Remains cubic. Used where thermal shock resistance matters.
- **Partially stabilized zirconia (PSZ)**: 3-5 mol% Y₂O₃. Retains some transformable tetragonal phase. Transformation toughening — cracks propagate, local tetragonal→monoclinic transformation creates compressive stress that arrests the crack. Highest toughness of any ceramic.
- **[Y-TZP](../glossary/y-tzp.md)** (yttria-tetragonal zirconia polycrystal): Fine-grained, fully tetragonal. The toughest technical ceramic. Used for cutting tools, dental crowns, knife blades.

### Properties and Applications

| Property | Value |
|----------|-------|
| Service temperature | Up to 2200°C |
| Thermal conductivity | 2-3 W/(m·K) (excellent thermal insulator) |
| Flexural strength | 500-1000 MPa (PSZ, transformation-toughened) |
| Fracture toughness | 8-12 MPa·√m (exceptional for a ceramic) |
| Oxygen ion conductivity | Conducts O²⁻ at >600°C |

**Applications**:
- **Cutting tools**: Y-TZP inserts for machining alloys where alumina is too brittle
- **Thermal barrier coatings**: YSZ (yttria-stabilized zirconia) plasma-sprayed onto turbine blades and combustion chamber surfaces. Allows higher operating temperatures → more efficient engines.
- **Oxygen sensors**: Zirconia electrolyte in lambda sensors for combustion control. At >600°C, oxygen ion conductivity allows measurement of oxygen partial pressure difference between reference air and exhaust gas.
- **Crucibles**: For melting specialty alloys, noble metals, and optical glasses. Chemically inert to most molten metals.
- **Dental ceramics**: Tooth-colored, high-strength crowns and bridges.
- **Solid oxide fuel cells**: YSZ electrolyte membrane conducts oxygen ions at 800-1000°C.

## Silicon Carbide (SiC)

Silicon carbide is exceptionally hard, an excellent thermal conductor, and survives extreme temperatures. It is both a structural ceramic and an electrical heating element material.

### Acheson Process (Primary Synthesis)

The original industrial SiC synthesis method, still used for abrasive-grade material:

1. **Charge preparation**: Mix silica sand (SiO₂, ≥99%) with petroleum coke (C, ≥95%) in roughly 1:3 molar ratio. Add sawdust (creates porosity for CO gas escape) and sodium chloride (removes impurities as volatile chlorides).
2. **Acheson furnace**: Build a rectangular bed of the charge mixture ~15 m long × 3 m wide × 3 m high. Embed graphite core electrodes along the length.
3. **Resistance heating**: Pass 2000-5000 A of electric current through the graphite core. Core heats to 2200-2500°C. Heat conducts outward into the charge.
4. **Reaction**: SiO₂ + 3C → SiC + 2CO (g). Takes 12-36 hours. CO gas must be managed (flammable, toxic).
5. **Product**: Intergrown SiC crystals in a cylindrical mass around the core. Green SiC (higher purity, ≥99% SiC) near the core, black SiC (slightly less pure) farther out. Unreacted material at the edges is recycled.
6. **Crushing and classification**: Break up the SiC mass. Crush in jaw crusher, then ball mill. Classify by grain size via sieving and sedimentation.

Energy consumption: 6-12 kWh/kg SiC. Requires substantial electrical power.

### Sintered and Reaction-Bonded SiC

For structural ceramics (not just abrasive grit), the Acheson product must be further processed:

**Reaction-bonded SiC (RBSC)**:
- Mix SiC powder with carbon (graphite or carbon black) and binder
- Form to desired shape (pressing, extrusion, slip casting)
- Fire at 1400-1600°C in contact with molten silicon
- Silicon infiltrates the porous body: Si (liquid) + C → SiC (solid)
- Result: ~85-90% SiC + 10-15% residual free silicon. Near-net shape (minimal shrinkage). Good for complex parts. Limited temperature capability above silicon melting point (1414°C).

**Sintered SiC (SSiC)**:
- Fine SiC powder (<1 μm) + sintering aids (B₄C or Al₂O₃+Y₂O₃, 0.5-3%)
- Form by pressing or isostatic pressing
- Sinter at 2100-2200°C in argon or vacuum
- Result: >98% dense, <2% porosity. Highest purity and temperature capability. Shrinkage ~15-20%.
- Best mechanical and chemical properties of all SiC ceramics.

### Properties and Applications

| Property | Value |
|----------|-------|
| Hardness | 9.5 Mohs |
| Flexural strength | 400-600 MPa (sintered) |
| Thermal conductivity | 80-120 W/(m·K) — excellent (better than most metals) |
| Thermal expansion | 4.0-4.5 × 10⁻⁶/°C (low) |
| Thermal shock resistance | Exceptional (high conductivity + low expansion) |
| Chemical resistance | Inert to most acids, alkalis, and molten metals |
| Electrical conductivity | Semiconductor — conducts at high temperature |

**Applications**:
- **Heating elements**: SiC glows at high temperature while conducting electricity. "Glow-bar" or "Siliconit" furnace elements. Resistance increases with temperature (self-limiting). Service temperature up to 1600°C in air. Used in ceramic kilns, heat treatment furnaces, and laboratory furnaces.
- **Abrasives**: SiC grinding wheels, sandpaper, blasting grit. Harder than aluminum oxide — cuts glass, stone, and cast iron well. The original Acheson product.
- **Mechanical seals**: Face seals for pumps handling corrosive or abrasive fluids. SiC-on-SiC seal faces have extremely low wear rates.
- **Kiln furniture**: Batts, props, and setters that support ware in kilns. High thermal conductivity ensures even heating. Survives repeated thermal cycling.
- **Body armor**: SiC ceramic tiles in composite armor systems. Lower density than alumina → lighter armor for equivalent protection.
- **Heat exchangers**: High-temperature, corrosion-resistant tube-and-shell heat exchangers for chemical processing.
- **Semiconductor furnace components**: Wafer boats, paddles, and process tubes. Chemically inert in semiconductor processing atmospheres.

## Silicon Nitride (Si₃N₄)

Silicon nitride offers the best combination of high-temperature strength, thermal shock resistance, and fracture toughness among the non-oxide ceramics.

### Production Methods

**Reaction bonding (RBSN)**:
1. Start with silicon metal powder (relatively easy to produce — see [silicon production](../silicon/index.md))
2. Form to shape by pressing or slip casting
3. Fire at 1200-1400°C in nitrogen atmosphere (N₂ gas, 0.1-2 MPa)
4. Nitridation: 3 Si + 2 N₂ → Si₃N₄. Volume increase ~22% but mostly fills internal porosity.
5. Result: 70-85% dense. No shrinkage (near-net shape). Lower strength than dense Si₃N₄ but simpler processing. No sintering aids needed.

**Hot pressing (HPSN)**:
1. Mix Si₃N₄ powder (produced by direct nitridation or silicon diimide decomposition) with sintering aids (MgO, Y₂O₃, Al₂O₃ — 5-10%)
2. Load into graphite die
3. Apply 20-30 MPa pressure while heating to 1700-1800°C in nitrogen atmosphere
4. Result: >99% dense. Highest strength. Limited to simple shapes (uniaxial pressing). Expensive process.

**Gas pressure sintering (GPSSN)**:
1. Mix Si₃N₄ powder with sintering aids (Y₂O₃ + Al₂O₃)
2. Form by isostatic pressing or injection molding
3. Sinter at 1800-2000°C under high nitrogen pressure (1-10 MPa) — prevents Si₃N₄ decomposition
4. Result: >99% dense. Complex shapes possible. Best balance of properties and manufacturability.

### Properties and Applications

| Property | Value |
|----------|-------|
| Flexural strength | 600-1200 MPa (hot-pressed) |
| Fracture toughness | 5-8 MPa·√m |
| Thermal shock resistance | Excellent (survives 700-1000°C quench without fracture) |
| Max service temperature | 1200-1400°C (in air, long-term) |
| Creep resistance | Superior to SiC and alumina at 1200-1400°C |
| Density | 3.2 g/cm³ (lightweight — lower than alumina at 3.9) |

**Applications**:
- **Turbine components**: Si₃N₄ turbine blades and vanes for gas turbines. Withstands high centrifugal stress at 1200°C+. Lighter than nickel superalloys. Primary application driving development.
- **Bearings**: Hybrid ceramic bearings (Si₃N₄ balls, steel races) for high-speed machine tool spindles. Lower density → lower centrifugal stress → higher RPM. Harder than steel → less wear. Used in precision [machine tools](../machine-tools/index.md).
- **Cutting tools**: Si₃N₄ inserts for high-speed roughing of cast iron. Tougher than alumina inserts. Can take heavier cuts at higher speeds.
- **Weld pins and rollers**: Contact parts in resistance welding. Non-stick to molten metal, resists spatter, electrically insulating.
- **Diesel engine components**: Glow plugs, prechamber inserts, turbocharger rotors. Allows elimination of cooling system in some designs.

## Refractory Linings

Refractories are the workhorse of high-temperature industry — the inner linings of furnaces, kilns, reactors, and crucibles that contain heat and molten material.

### Fireclay Refractories (Basic)

The starting point. See [Pottery](pottery.md) for basic fireclay brick production.

- **Composition**: Aluminosilicate clay (25-45% Al₂O₃), fired to 1200-1400°C
- **Service temperature**: 1200-1500°C
- **Thermal conductivity**: 1-2 W/(m·K)
- **Porosity**: 15-25%
- **Applications**: Furnace linings, kiln interiors, forge hearths, chimney flues
- **Limitation**: Softens above 1400°C. Poor slag resistance. Inadequate for steel furnaces and silicon processing.

### High-Alumina Refractories

- **Composition**: Calcined bauxite or diaspore (50-95% Al₂O₃), pressed with clay binder, fired 1500-1700°C
- **Key phase**: Mullite (3Al₂O₃·2SiO₂) forms above 1600°C — excellent high-temperature strength
- **Service temperature**: 1500-1800°C
- **Advantage over fireclay**: Higher strength, better slag resistance, lower porosity
- **Applications**: Steel furnace linings, glass tank furnaces, CZ crystal growth furnace insulation, high-fire ceramic kilns

### Silica Refractories

- **Composition**: Quartzite (≥95% SiO₂) + 2-3% lime binder, fired 1450-1500°C
- **Phase conversion**: Quartz → cristobalite + tridymite during firing. Must complete during manufacture (15% volume expansion).
- **Service temperature**: Up to 1650°C
- **Unique property**: Very low thermal expansion above 600°C (cristobalite stable). Excellent volume stability at high temperature.
- **Critical weakness**: Poor thermal shock below 600°C (α-β quartz inversion at 573°C causes sudden 0.8% volume change → cracking)
- **Applications**: Coke oven walls, glass furnace crowns, acid steelmaking furnaces

### Magnesia Refractories

- **Composition**: Periclase (MgO) from calcined magnesite or seawater-precipitated Mg(OH)₂, fired 1800-2000°C
- **Service temperature**: 1800-2000°C+
- **Advantage**: Excellent basic slag resistance. Essential for basic oxygen steelmaking.
- **Weakness**: High thermal expansion (~13.5 × 10⁻⁶/°C) → poor thermal shock resistance
- **Applications**: Basic oxygen furnaces, cement rotary kilns, copper smelting furnaces

### Carbon and Graphite Refractories

- **Composition**: Coke or graphite + pitch binder, fired 1000-1300°C in reducing atmosphere. Graphitization at 2500-3000°C for graphite grade.
- **Service temperature**: 2000-3000°C+ in reducing or inert atmosphere. NOT usable in oxidizing atmosphere above ~400°C.
- **Properties**: High thermal conductivity, excellent thermal shock resistance, non-wetting by most metals
- **Applications**: Blast furnace hearths, EAF electrodes, crucibles for reactive metals, SiC furnace cores

### Insulating Refractories

Not all refractories need maximum density. Insulating firebricks and ceramic fiber provide thermal resistance:

**Insulating firebrick**:
- Porosity 60-80%, density 0.5-1.0 g/cm³
- Made by adding sawdust or vermiculite to clay — organics burn out during firing, leaving pores
- Thermal conductivity 0.15-0.4 W/(m·K) vs. 1-2 for dense brick
- Lower temperature rating (max 1200-1400°C)
- Use as backup layer behind dense hot-face refractory

**Ceramic fiber blanket**:
- Al₂O₃-SiO₂ fibers (melt aluminosilicate, spin or blow into fibers, collect as blanket)
- Density 0.1-0.3 g/cm³, thermal conductivity 0.05-0.15 W/(m·K)
- Service temperature 1200-1600°C
- Cut with scissors, wrap around furnace — lightweight and easy to install
- Replaces massive brick linings → faster heat-up, less fuel, smaller furnace structure
- **Health hazard**: Ceramic fibers are a potential carcinogen (similar to asbestos). Use respiratory protection during handling.

## Ceramic Processing Techniques Summary

### Powder Preparation

- **Ball milling**: Rotate porcelain or rubber-lined steel mill with alumina/zirconia grinding media and raw powder. 12-72 hours reduces particle size to sub-micron. Wet milling (add water or solvent) prevents agglomeration and produces finer powder.
- **Calcination**: Heat powder below sintering temperature to decompose precursors and initiate solid-state reactions. Example: Al(OH)₃ → Al₂O₃ + H₂O at 1200°C.
- **Spray drying**: Atomize slurry (powder + water + binder) into hot air. Produces spherical granules (50-200 μm) with good flow properties for automated pressing.

### Sintering Fundamentals

- Heat green (unfired) body to 0.7-0.9 × melting temperature
- Atomic diffusion causes particle bonding → porosity decreases → density increases → strength increases
- Shrinkage 10-20%. Grain growth occurs simultaneously (larger grains → stronger but more brittle)
- **Temperature control**: ±5-10°C at peak. Ramp 1-5°C/minute to avoid thermal shock. Soak 1-4 hours at peak. Total cycle 12-48 hours.
- **Atmosphere control**:
  - Air: for oxide ceramics (alumina, zirconia)
  - Reducing (H₂/N₂ or CO): for non-oxides (SiC, Si₃N₄)
  - Inert (Ar): prevent unwanted oxidation
  - Vacuum: remove evolved gases, achieve highest density

## Ceramic Applications in Semiconductor Manufacturing

Advanced ceramics are indispensable in semiconductor fabrication:

### Furnace Components

- **CZ crystal growth furnace**: Alumina or zirconia insulation surrounding the fused silica crucible. Graphite susceptor for induction heating. Argon atmosphere to prevent oxidation.
- **Diffusion/oxidation furnace**: Fused silica process tube (1100-1200°C). Silicon carbide heating elements. Alumina support furniture.
- **Wafer handling**: Alumina or SiC wafer boats, paddles, end caps for furnace pusher systems.

### Substrates and Packages

- **Alumina substrates**: 96% Al₂O₃, 0.5-1.0 mm thick, cofired with tungsten metallization. Hybrid circuit substrates, resistor networks. Excellent thermal conductivity for heat dissipation.
- **Ceramic IC packages**: Multilayer alumina with internal W/Mo traces. Cofired at 1600°C in reducing atmosphere. Hermetically sealed with Au-Sn solder lid. Superior to plastic for high-reliability applications.

### Seals and Vacuum Components

- **Mechanical seals**: SiC or alumina seal faces for pumps handling HF, HNO₃, and solvents in [semiconductor fab](../photolithography/index.md).
- **Vacuum feedthroughs**: Alumina insulators carrying electrical conductors through vacuum chamber walls while maintaining vacuum seal.

## Safety

### Dust Hazards (Silicosis)

Many ceramic raw materials produce fine dust during crushing, grinding, and powder handling:
- **[Crystalline silica](../glossary/crystalline-silica.md)** (quartz, cristobalite, tridymite): Causes silicosis — irreversible lung scarring. Exposure limit: 0.025 mg/m³ respirable (ACGIH TLV). Wet grinding wherever possible. Respiratory protection (P100 mask minimum) during all dry powder handling.
- **Alumina dust**: Less hazardous than silica but still a respiratory irritant. Maintain <5 mg/m³.
- **Ceramic fiber**: Suspected carcinogen. Handle with full respiratory protection and protective clothing.

### High-Temperature Burns

- Ceramics are fired at 1200-2200°C. Surfaces above 60°C cause burns on contact. Above 200°C, contact burns are deep tissue within seconds.
- Use infrared thermometers or thermocouples to verify temperature before approaching. Assume all kilns and furnace surfaces are hot.
- Kiln furniture and fired ware retain heat for hours after kiln shutdown. Use heavy leather or Kevlar gloves rated for the expected temperature.

### Kiln and Furnace Safety

- **CO hazard**: Carburizing and reducing atmospheres produce carbon monoxide. Adequate ventilation mandatory. CO detectors in all kiln areas.
- **Electrical hazard**: Electric kilns operate at 240-480V, high current. Lockout/tagout procedures for all maintenance. Ground fault protection.
- **Thermal expansion**: Refractory linings expand on heating. Provide expansion joints (5-10 mm per meter of length) to prevent buckling and structural damage.
- **Moisture explosion**: Moisture in refractories flashes to steam during rapid heating. Dry all refractory installations slowly (24-48 hours at 100-200°C) before bringing to full temperature. New or repaired linings must be thoroughly dried.

### Chemical Hazards

- **[HF etching](../glossary/hf-etching.md)** of ceramics requires full acid-handling PPE: face shield, HF-rated gloves (neoprene), apron. Calcium gluconate gel must be immediately available (HF antidote for skin exposure).
- **[Binders and solvents](../glossary/binders-and-solvents.md)** used in ceramic processing (PVA, PEG, organic solvents) require standard chemical safety practices.

## Integration Points

| Stage | Contribution |
|-------|-------------|
| Metals | Fireclay and high-alumina refractories for smelting furnaces and forge hearths |
| Machine Tools | Alumina wear parts, cutting tool inserts, precision ceramic components |
| Energy | Refractory linings for steam boilers, furnace insulation, SiC heating elements |
| Chemistry | Magnesia, zirconia, SiC refractories for chemical reactors and acid handling |
| Silicon | High-alumina furnace linings, CZ hot zone insulation, SiC furnace components |
| Photolithography | Ceramic IC packages, alumina substrates, mechanical seals for corrosive chemicals |

## Key Deliverables

- High-alumina refractory brick production for furnaces operating above 1500°C
- Silicon carbide heating elements for electric furnace operation
- Alumina technical ceramics (insulators, substrates, wear parts, cutting tools)
- Zirconia ceramics for thermal barrier coatings, oxygen sensors, and specialty crucibles
- Silicon nitride components for high-temperature, high-stress applications
- Insulating firebrick and ceramic fiber blanket for efficient furnace construction
- Ceramic substrates and packages for semiconductor device assembly

---

*Part of the [Bootciv Tech Tree](../index.md) • [Ceramics & Refractories](./index.md) • [All Domains](../index.md)*
