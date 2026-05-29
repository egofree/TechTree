# Thermoplastic Polymers

> **Node ID**: polymers.thermoplastics
> **Domain**: [Polymers & Composites](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`chemistry.petroleum-alternatives`](../chemistry/petroleum-alternatives.md), [`machine-tools`](../machine-tools/index.md)
> **Enables**: [`computing.data-storage`](../computing/data-storage.md), [`electronics.electrical-systems`](../electronics/electrical-systems.md)
> **Timeline**: Years 15-50
> **Outputs**: polyethylene, PVC, nylon, polystyrene, PTFE
> **Critical**: No — thermoplastics expand material capability but the critical path uses metals and ceramics at earlier stages


Thermoplastic polymers soften when heated and harden when cooled — a reversible process that enables melting, shaping, and recycling. Unlike [thermosets](./thermosets.md) (which permanently crosslink during cure), thermoplastics can be repeatedly remelted and reprocessed, making them the dominant class of polymers by volume. Global thermoplastic production exceeds 350 million tonnes/year, with polyethylene alone accounting for over 100 million tonnes.

The thermoplastics covered here span from polyethylene (achievable at Chemistry stage with high-pressure reactors) through PVC and nylon (Chemistry–Vacuum stages) to PTFE and polycarbonate (advanced petrochemical industry). Processing methods — injection molding, extrusion, blow molding, thermoforming, compression molding — convert raw polymer granules into finished products. Feedstocks come from [petrochemical cracking](../chemistry/petroleum-alternatives.md); polymerization reactors and extruders rely on [machine tools](../machine-tools/index.md).

## Prerequisites

## Materials
- Ethylene, propylene, styrene, vinyl chloride monomer (from [petrochemicals](../chemistry/petroleum-alternatives.md))
- Chlorine (for PVC — from [chlor-alkali electrolysis](../chemistry/electrolysis.md))
- HF (for PTFE — from fluorspar CaF₂ + H₂SO₄)
- Adipic acid + hexamethylenediamine (for nylon 6,6 — from cyclohexane/benzene via petrochemical routes)
- Titanium tetrachloride + triethylaluminum (Ziegler-Natta catalyst for HDPE, PP)

## Tools and Equipment
- [Extruder](../machine-tools/machining.md) (single-screw or twin-screw, L/D 20-30:1, with heated barrel)
- [Injection molding machine](../machine-tools/forming.md) (hydraulic or toggle clamp, 50-500 tons)
- Compression mold or heated press (for thermoforming)
- Blow molding equipment (for bottles and hollow parts)

## Infrastructure
- Electrical power (continuous, for extruder and injection molding machine heaters — 5-50 kW)
- Cooling water (for mold cooling and extrusion sizing — 5-20 liters/minute)
- Compressed air (for blow molding — 0.2-1.5 MPa)
- Ventilation (for polymer fume extraction during melt processing)

## Bill of Materials

## Polyethylene (HDPE) — per tonne polymer

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Ethylene (C₂H₄, >99.9%) | 1.02-1.05 tonnes | [Petrochemicals](../chemistry/petroleum-alternatives.md) — steam cracking of naphtha or ethane | Ethylene from ethanol dehydration (alumina catalyst, 350-400°C) |
| TiCl₄ (Ziegler-Natta catalyst) | 0.2-0.5 kg | [Chemistry](../chemistry/electrolysis.md) — Ti + Cl₂ | Metallocene catalyst (higher cost, narrower MW distribution) |
| Triethylaluminum (co-catalyst) | 0.2-0.5 kg | Organic synthesis — Al + H₂ + C₂H₄ | None — pyrophoric, handle under nitrogen |
| Hexane (solvent, for slurry process) | 50-100 kg (recovered) | [Solvents](../chemistry/solvents.md) | Isobutane (slightly higher boiling point) |

## PVC (Rigid) — per tonne polymer

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Vinyl chloride monomer (VCM) | 1.01-1.03 tonnes | [Chemistry](../chemistry/electrolysis.md) — ethylene + Cl₂ → EDC → pyrolysis at 450-550°C | Acetylene + HCl → VCM (coal-based route) |
| Lauroyl peroxide (initiator) | 0.5-2.0 kg | Organic synthesis | Other peroxide initiators |
| Tin stabilizer (dibutyltin dilaurate) | 5-30 kg | [Chemistry](../chemistry/petroleum-alternatives.md) | Ca/Zn stabilizers (lower performance), lead stabilizers (toxic) |
| Calcium stearate (lubricant) | 10-50 kg | [Chemistry](../chemistry/alkalis.md) | Paraffin wax |
| Impact modifier (MBS or CPE) | 0-100 kg | [Petrochemicals](../chemistry/petroleum-alternatives.md) | None needed for non-impact applications |

## Nylon 6,6 — per tonne polymer

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Adipic acid (HOOC(CH₂)₄COOH) | 0.57 tonnes | [Petrochemicals](../chemistry/petroleum-alternatives.md) — cyclohexane + HNO₃ oxidation | Nylon 6 from caprolactam (single monomer route) |
| Hexamethylenediamine (HMDA) | 0.52 tonnes | [Petrochemicals](../chemistry/petroleum-alternatives.md) — butadiene + HCN → adiponitrile → hydrogenation | From acrylonitrile electrolytic dimerization |
| Nitrogen (inert atmosphere) | 50-100 m³ | [Air separation](../chemistry/air-separation.md) | Argon (more expensive) |

## Process Description

## 4.1 Polyethylene (LDPE and HDPE)

**Principle**: Ethylene (C₂H₄) polymerizes to form long chains of —CH₂—CH₂— units. Two industrial routes produce different chain structures: high-pressure free-radical polymerization creates branched chains (LDPE, flexible, transparent), while low-pressure Ziegler-Natta catalytic polymerization creates linear chains (HDPE, stiff, opaque, higher crystallinity).

**Prerequisites**: Ethylene monomer (>99.9% purity, from [steam cracking](../chemistry/petroleum-alternatives.md) of naphtha or ethane). For LDPE: high-pressure reactor (1000-3000 atm) and peroxide initiator. For HDPE: Ziegler-Natta catalyst system (TiCl₄/AlEt₃) and low-pressure reactor (1-20 atm).

**Materials**:
- Ethylene (C₂H₄, >99.9%): 100 parts
- For LDPE: Benzoyl peroxide or oxygen (0.01-0.1%): free radical initiator
- For HDPE: TiCl₄ (catalyst, 0.02-0.05%): 0.2-0.5 kg/tonne
- For HDPE: Triethylaluminum (co-catalyst, 0.02-0.05%): 0.2-0.5 kg/tonne

**Procedure (LDPE — High-Pressure Process)**:
1. Compress ethylene gas to 1000-3000 atm using multi-stage hypercompressors. Compressor seals must handle these pressures — clearance <0.01 mm on piston rings.
2. Preheat compressed ethylene to 100-150°C.
3. Inject peroxide initiator. Polymerization temperature: 100-300°C (controlled by initiator feed rate and reactor cooling). Tubular reactor (50-1500 m long, 25-75 mm bore) or autoclave (stirred, 0.5-3 m³).
4. Polymerization occurs in milliseconds to seconds. Ethylene conversion: 15-30% per pass (unreacted ethylene recycled).
5. Depressurize through let-down valve. Separated molten polymer is extruded through a strand die, water-cooled, and pelletized into 2-4 mm granules.
6. Unreacted ethylene is recycled to the compressor inlet after purification (removal of low-MW oligomers).

**Procedure (HDPE — Ziegler-Natta Slurry Process)**:
1. Prepare catalyst slurry: TiCl₄ + AlEt₃ in hexane diluent. Both are moisture-sensitive — handle under nitrogen blanket. Triethylaluminum is pyrophoric (ignites spontaneously in air).
2. Feed ethylene gas (1-20 atm) and catalyst slurry into the reactor. Temperature: 50-80°C. Polymerization is exothermic — reactor must be jacketed for cooling.
3. Polymer precipitates as solid particles in the hexane slurry. Conversion: 95-98% of ethylene.
4. Deactivate catalyst residue with isopropanol. Wash polymer with hexane to remove catalyst residues. Catalyst residues (<10 ppm Ti) cause color and stability issues if not removed.
5. Centrifuge to separate polymer from hexane. Dry in fluidized bed dryer at 80-100°C to <0.02% moisture.
6. Extrude into pellets (2-4 mm granules) with stabilizer addition (antioxidant, 0.05-0.2%).

**Calibration/Verification**:
- Density measurement (ASTM D1505): LDPE: 0.91-0.93 g/cm³ (float). HDPE: 0.94-0.97 g/cm³ (sink in water, float in saturated NaCl at 1.20 g/cm³). Density determines crystallinity.
- Melt Flow Index (MFI, ASTM D1238): Weight of polymer extruded through standard die in 10 minutes at 190°C under 2.16 kg load. LDPE: 0.1-50 g/10 min. HDPE: 0.1-30 g/10 min. Lower MFI = higher molecular weight = tougher but harder to process.
- Tensile test (ASTM D638): LDPE: 8-25 MPa. HDPE: 25-45 MPa. Below-spec tensile indicates contamination, insufficient molecular weight, or oxidative degradation.

**Expected Performance**:
- LDPE: Tensile 8-25 MPa, elongation 100-600%, melt temp 105-115°C, density 0.91-0.93 g/cm³
- HDPE: Tensile 25-45 MPa, elongation 10-1000%, melt temp 130-135°C, density 0.94-0.97 g/cm³
- Chemical resistance: Resistant to most acids, alkalis, and solvents at room temperature. Attacked by strong oxidizers (concentrated HNO₃) and some hydrocarbons at elevated temperature.
- Water absorption: <0.01% (24 hours) — excellent moisture barrier

**Strengths**:
- LDPE: Flexible, transparent, easy to process at low temperature (105-115°C melt), inexpensive, excellent moisture barrier
- HDPE: Stiff, strong (25-45 MPa), excellent chemical resistance, low moisture absorption, good stress crack resistance in higher grades
- Both: Recyclable — can be reprocessed 3-5 times before properties degrade below useful levels; inexpensive (lowest cost commodity polymer)

**Weaknesses**:
- LDPE: Low strength (8-25 MPa), poor high-temperature capability (softens above 80°C), high gas permeability (not suitable for CO₂ barrier in carbonated beverages)
- HDPE: Opaque (not transparent), higher processing temperature required, susceptible to environmental stress cracking in certain grades
- Both: Flammable (burn like hydrocarbon fuel), poor UV resistance without stabilizers, creep under sustained load

## 4.2 Polyvinyl Chloride (PVC)

**Principle**: Vinyl chloride monomer (VCM) polymerizes via free-radical suspension polymerization. Water is the continuous phase; VCM droplets (stabilized by suspending agents) polymerize to form porous PVC powder particles (100-150 μm). The resulting polymer is inherently rigid and heat-sensitive — it begins to decompose (releasing HCl) above 200°C, requiring heat stabilizers for processing.

**Prerequisites**: VCM (from ethylene + Cl₂ → 1,2-dichloroethane → pyrolysis at 450-550°C → VCM + HCl). Jacketed stainless steel reactor (40-70°C). Centrifuge or filter for polymer recovery. VCM is a confirmed human carcinogen (IARC Group 1) — closed handling systems mandatory.

**Materials**:
- Vinyl chloride monomer (VCM, CH₂=CHCl, >99.9%): 100 parts
- Deionized water (continuous phase): 150-250 parts
- Polyvinyl alcohol or gelatin (suspending agent): 0.05-0.2 parts
- Lauroyl peroxide or azobisisobutyronitrile (initiator): 0.05-0.2 parts
- For rigid PVC: tin stabilizer 0.5-3 phr, calcium stearate 1-5 phr, impact modifier 0-10 phr
- For flexible PVC: plasticizer (DOP/DINP) 30-80 phr, Ba/Zn or Ca/Zn stabilizer 2-4 phr

**Procedure**:
1. Charge reactor with deionized water and suspending agent. Purge with nitrogen.
2. Add VCM monomer. Stir at 150-300 RPM to create monomer droplets (100-300 μm diameter).
3. Add initiator. Heat to 40-70°C (jacket temperature). Polymerization is exothermic — cooling must maintain temperature within ±2°C.
4. React for 6-12 hours to 85-95% conversion. Monitor by pressure drop (VCM is consumed and pressure decreases as polymer forms).
5. Recover unreacted VCM by depressurization and steam stripping. VCM is recycled. Residual VCM in polymer must be reduced to <1 ppm (food-contact grade: <0.1 ppm).
6. Slurry discharged to centrifuge. Wash PVC cake with water. Dry in flash dryer or fluidized bed at 50-60°C to <0.3% moisture.
7. Sieve to remove oversized particles (>250 μm). Package as PVC resin powder.

**Calibration/Verification**:
- K-value (Fikentscher): Measures intrinsic viscosity — relates to molecular weight. Target: K57-70 (most common grades). K57-60 = easy processing (pipe, profile). K65-70 = higher strength (film, sheet). Measure by 0.5% solution viscosity in cyclohexanone at 25°C.
- Residual VCM: Gas chromatography headspace analysis. Must be <1 ppm (regulatory requirement). Above 5 ppm requires additional stripping.
- Apparent density: Pour PVC powder through funnel into 100 ml cylinder, weigh. Target: 0.45-0.55 g/cm³. Too low (<0.40) causes feeding problems in extruder; too high (>0.60) indicates insufficient porosity for plasticizer absorption.

**Expected Performance**:
- Rigid PVC: Tensile 45-55 MPa, modulus 2.5-3.5 GPa, service temperature up to 60°C (continuous), density 1.35-1.45 g/cm³
- Flexible PVC: Tensile 10-25 MPa (depends on plasticizer type and loading), elongation 150-450%, service temperature -20 to +60°C
- Chemical resistance: Resistant to acids, alkalis, alcohols, and many solvents. Attacked by ketones, chlorinated hydrocarbons, and aromatic hydrocarbons.
- Flame resistance: Self-extinguishing (chlorine content acts as flame retardant) — LOI ~45% (vs. ~18% for PE and PP)

**Strengths**:
- Inherently flame retardant — the chlorine content (57% by weight) provides self-extinguishing properties without additives; LOI ~45% (highest of any commodity thermoplastic)
- Versatile — rigid PVC for pipes and profiles; flexible PVC for wire insulation, tubing, and flooring; the same base polymer serves both markets with different additive packages
- Excellent chemical resistance — resistant to most acids, alkalis, and oxidizers at room temperature; standard material for chemical drain pipe and ductwork

**Weaknesses**:
- Narrow processing window — decomposes above 200°C (releases HCl gas, which is corrosive and toxic); extrusion temperature must stay in 160-190°C range with ±5°C control
- VCM is a confirmed human carcinogen (IARC Group 1, causing angiosarcoma of the liver) — monomer handling requires closed systems, continuous air monitoring, and explosion-proof equipment
- Plasticizer migration — flexible PVC loses plasticizers over time, becoming brittle; phthalate plasticizers (DOP) are endocrine disruptors under regulatory scrutiny

## 4.3 Nylon (Polyamide 6,6)

**Principle**: Nylon 6,6 is formed by melt condensation polymerization of adipic acid (6 carbons) with hexamethylenediamine (6 carbons). The reaction produces amide bonds (—NH—CO—) and water as a byproduct. Removing water drives the equilibrium toward high molecular weight. The polymer has high crystallinity, giving excellent mechanical properties (tensile 70-85 MPa molded, 500-900 MPa as drawn fiber).

**Prerequisites**: Adipic acid (from cyclohexane → oxidation with HNO₃). Hexamethylenediamine (from butadiene + HCN → adiponitrile → catalytic hydrogenation). Autoclave capable of 250-280°C under vacuum (<5 mmHg). Nitrogen atmosphere for oxidation prevention.

**Materials**:
- Adipic acid (HOOC(CH₂)₄COOH, >99.5%): equimolar with HMDA
- Hexamethylenediamine (HMDA, H₂N(CH₂)₆NH₂, >99%): equimolar with adipic acid
- Water (for nylon salt preparation): 30-50% by weight
- Nitrogen (inert atmosphere): continuous purge
- Acetic acid (molecular weight regulator, optional): 0.5-2.0% by weight (limits MW by capping chain ends)

**Procedure**:
1. Prepare nylon salt solution: Dissolve adipic acid and HMDA in water (30-50% concentration). Adjust pH to 7.0-7.5 with precise stoichiometric control — even 0.1% imbalance in amine:acid ratio limits achievable molecular weight. pH is the critical control parameter.
2. Concentrate salt solution in evaporator to ~60% solids at 80-100°C under atmospheric pressure.
3. Transfer to autoclave. Purge with nitrogen. Heat to 250-280°C under nitrogen pressure (1.7-2.0 MPa — pressure prevents water from boiling off too fast and entraining monomer).
4. Hold at 250-280°C for 1-2 hours under autogenous pressure (pre-polymerization stage). Conversion reaches ~80-90%.
5. Apply vacuum in stages: atmospheric → 100 mmHg → 10 mmHg → <5 mmHg over 30-60 minutes. This drives off water and pushes molecular weight to 12,000-15,000 g/mol (number average). The vacuum stage is critical — the condensation equilibrium (amine + carboxylic acid ⇌ amide + water) must be driven to completion by removing water.
6. Extrude molten polymer through a strand die into water bath. Pelletize into 2-4 mm granules.
7. For fiber production: Melt spin at 260-280°C through spinneret (15-100 holes, 0.2-0.5 mm diameter). Cold draw 3-5× at room temperature to orient polymer chains, increasing crystallinity from ~30% to 50-60% and tensile from ~100 MPa to 500-900 MPa.

**Calibration/Verification**:
- Relative viscosity (RV): 1% solution in 96% H₂SO₄ at 25°C. Target: RV 40-60 (corresponds to MW 12,000-15,000). Below RV 30 = low MW (weak, brittle). Above RV 70 = difficult processing (high melt viscosity).
- Moisture content: Nylon absorbs moisture rapidly. Dry to <0.2% before processing (dry at 80°C, vacuum oven, 12-24 hours). Karl Fischer titration or weight loss at 105°C.
- Melting point (DSC): Target 255-262°C for nylon 6,6. Deviation >5°C indicates incorrect stoichiometry or contamination.

**Expected Performance**:
- Molded tensile: 70-85 MPa (dry), 40-55 MPa (conditioned at 50% RH)
- Fiber tensile: 500-900 MPa (cold drawn 3-5×)
- Elongation at break: 30-100% (molded), 15-30% (fiber)
- Coefficient of friction: 0.1-0.3 (vs. steel-on-steel 0.5-0.8) — nylon bearings run without lubrication
- Moisture absorption: 2.0-2.5% at 50% RH, 8-10% at saturation — causes dimensional change (0.2-0.5% swelling) and reduces stiffness 30-50%

**Strengths**:
- High tensile strength and toughness — 70-85 MPa molded (highest of any unreinforced commodity thermoplastic)
- Self-lubricating — coefficient of friction 0.1-0.3, enabling unlubricated gears and bearings that run quietly
- Excellent abrasion resistance — 10× better than cotton; used for rope, tire cord, and mechanical components

**Weaknesses**:
- Moisture absorption — 2-2.5% at 50% RH causes dimensional swelling (0.2-0.5%) and reduces stiffness 30-50% from dry to conditioned state; must be accounted for in precision molding
- Requires drying before processing — nylon granules must be dried to <0.2% moisture before melt processing or steam bubbles cause voids and surface defects
- Limited high-temperature capability — continuous service limited to 80-120°C (dry) or 60-80°C (wet); loses 50% stiffness above Tg (~50°C dry, lower when wet)

## 4.4 PTFE (Teflon)

**Principle**: Tetrafluoroethylene (TFE) polymerizes to form polytetrafluoroethylene — a fully fluorinated carbon chain (—CF₂—CF₂—)ₙ. The strong C—F bonds and fluorine shielding of the carbon backbone create a chemically inert, thermally stable material with the lowest coefficient of friction of any solid (0.04-0.10). PTFE does not melt-flow — it must be sintered above 327°C or paste-extruded with a lubricant carrier.

**Prerequisites**: TFE monomer from R-22 pyrolysis: (1) Chloroform + HF (SbF₅ catalyst) → chlorodifluoromethane (R-22). (2) R-22 pyrolysis at 650-700°C → TFE + HCl. Temperature must be tightly controlled — byproducts include hexafluoropropylene and perfluoroisobutylene (PFIB, extremely toxic). [HF production](../chemistry/electrolysis.md) from fluorspar (CaF₂ + H₂SO₄).

**Materials**:
- TFE (CF₂=CF₂, >99.99%): 100 parts. TFE is explosive in certain concentration ranges and must be handled with extreme care.
- Ammonium persulfate (initiator): 0.01-0.1%
- Water (aqueous dispersion medium)

**Procedure (Granular PTFE)**:
1. Polymerize TFE in aqueous dispersion at 20-80°C with persulfate initiator. High molecular weight achieved rapidly (MW >1,000,000 g/mol). Granular process produces ~500 μm particles.
2. Coagulate PTFE dispersion with electrolyte. Filter and dry at 150-200°C.
3. Preform PTFE powder in a mold at 20-35 MPa at room temperature (cold pressing — PTFE does not flow at any temperature below decomposition at ~400°C).
4. Sinter the preform in an oven: Heat from room temperature to 380°C at 50-100°C/hour. Hold at 380°C for 1-4 hours (depending on wall thickness — rule of thumb: 1 hour per 10 mm thickness). Cool at 20-50°C/hour to below 250°C (controlled cooling prevents thermal stress cracking). Total sintering cycle: 8-24 hours.
5. Machine sintered billet to final dimensions (PTFE can be turned, milled, drilled, and tapped with standard metalworking tools).

**Calibration/Verification**:
- Specific gravity (ASTM D792): Target 2.14-2.20 g/cm³. Below 2.10 indicates incomplete sintering (residual porosity). Above 2.22 indicates measurement error.
- Tensile test (ASTM D639, Type IV specimen): Target 20-35 MPa. Below 14 MPa indicates insufficient sintering or contamination.
- Elongation at break: Target 200-400%. Below 100% indicates over-sintering or thermal degradation.
- Dielectric strength: Target >40 kV/mm (ASTM D149). PTFE is one of the best electrical insulators.

**Expected Performance**:
- Tensile strength: 20-35 MPa
- Elongation at break: 200-400%
- Service temperature range: -200°C to +260°C (widest of any thermoplastic)
- Coefficient of friction: 0.04-0.10 (lowest of any solid material)
- Chemical resistance: Resists nearly all solvents, acids (including aqua regia), and bases. Only molten alkali metals, fluorine, and some fluorinated compounds attack PTFE.
- Dielectric constant: 2.0-2.1

**Strengths**:
- Chemically inert — resists virtually all chemicals including concentrated acids, bases, and solvents; the standard material for gaskets and seals in corrosive service
- Ultra-low friction — coefficient 0.04-0.10 (lowest of any solid); used for non-stick surfaces, bearing surfaces, and slide plates
- Widest temperature range of any thermoplastic: -200°C to +260°C continuous service

**Weaknesses**:
- Cannot be melt-processed by conventional methods (injection molding, extrusion) — PTFE does not flow below its decomposition temperature; requires expensive sintering or paste extrusion
- Creep (cold flow) — PTFE deforms under sustained load even at room temperature; gaskets require reinforcement (filled PTFE with glass or bronze) or design accommodation (full-face gaskets, not line-contact)
- PTFE fume hazard — overheating above 350°C produces toxic pyrolysis products including PFIB (lethal at low ppm). Sintering at 380°C must use calibrated controllers with high-limit shutoff

## 4.5 Injection Molding

**Principle**: Heat plastic granules to melt temperature (180-320°C depending on polymer), inject under high pressure (50-200 MPa) into a closed steel mold, cool until solid, eject finished part. The highest-volume plastic processing method — over 50% of all thermoplastic products are injection-molded.

**Prerequisites**: Injection molding machine (hydraulic or electric, clamp force 50-500+ tons). Steel mold (P20 tool steel, hardened to HRC 30-35). Granulated thermoplastic resin (dried if hygroscopic — nylon, PET). Cooling water supply (10-30°C, 5-20 liters/minute). Electrical power (5-50 kW depending on machine size).

**Materials**:
- Thermoplastic granules (2-4 mm pellets), dried to <0.2% moisture (for nylon, PET, PC)
- Mold release agent (silicone spray, for difficult-release polymers)
- Mold coolant (water at 10-30°C)

**Procedure**:
1. Dry hygroscopic resins (nylon, PET, PC) in dehumidifying hopper dryer at 80-120°C for 2-4 hours to <0.2% moisture. Skip for PE, PP, PVC (non-hygroscopic).
2. Load granules into machine hopper. Set barrel temperature zones (from hopper to nozzle): PE: 160-240°C (4 zones). PP: 180-240°C. PVC: 160-190°C (do NOT exceed 200°C). Nylon: 240-280°C. PS: 180-220°C. Allow 30-60 minutes for temperature stabilization.
3. Set mold temperature via coolant flow: PE/PP: 20-40°C (cool mold for fast cycle). Nylon: 60-80°C (warm mold for crystallinity). PC: 80-100°C (hot mold to reduce internal stress).
4. Set injection pressure: 50-200 MPa (first stage — filling). Set holding pressure: 30-80 MPa (second stage — packing as part cools and shrinks).
5. Start machine in semi-automatic mode. Observe first shots for short shots (incomplete fill), flash (excess material at parting line), or sink marks (surface depressions over thick sections).
6. Adjust parameters: Increase injection pressure if short shots appear. Increase holding pressure/time if sink marks appear. Decrease injection pressure or increase clamp force if flash appears.
7. Once acceptable parts are produced, switch to automatic mode. Typical cycle: injection (1-5 s) → holding (2-10 s) → cooling (10-90 s, 50-70% of total cycle) → mold open/eject (2-5 s). Total: 15-120 s.
8. Inspect parts at regular intervals (every 50-100 shots): dimensional check with calipers at critical dimensions, visual inspection for flash, short shots, sink marks, and discoloration.

**Calibration/Verification**:
- Dimensional check: Measure critical dimensions with digital calipers (±0.01 mm). Compare to drawing tolerances. Typical injection molding tolerance: ±0.05-0.25 mm depending on material and size. PE/PP shrinkage 1.5-3.0%, PVC 0.2-0.4%, nylon 1.0-1.5% — mold dimensions must be oversized to compensate.
- Weight check: Weigh 10 consecutive shots. Weight must be consistent within ±0.5%. Increasing weight indicates flash; decreasing weight indicates short shots or insufficient holding pressure.
- Visual standard: Compare to approved sample for color, surface finish, and absence of defects (burns, silver streaks, weld lines in critical areas).

**Expected Performance**:
- Cycle time: 15-120 seconds (depends on part size and wall thickness; cooling time scales roughly with wall thickness²)
- Production rate: 30-240 parts/hour per cavity
- Dimensional tolerance: ±0.05-0.25 mm (tighter with low-shrinkage materials like PC; looser with high-shrinkage PE)
- Mold lifetime: 100,000-1,000,000+ shots (glass-filled nylon is most abrasive, wearing molds fastest)

**Strengths**:
- Highest-volume, lowest per-part cost for complex 3D shapes — once mold is made, each part costs pennies in material and machine time
- Excellent dimensional consistency — ±0.05-0.25 mm tolerances achievable in production; consistent part-to-part repeatability
- Wide material range — virtually every thermoplastic can be injection-molded, from soft LDPE to rigid PPS

**Weaknesses**:
- High tooling cost — $10,000-$100,000+ for production molds (P20 tool steel, precision machined); amortization requires 10,000+ parts to be economical
- Long lead time for molds — 4-12 weeks from design to production mold
- Limited to parts with uniform wall thickness — thick sections require disproportionately long cooling time (cooling scales with wall thickness²); thin-wall design (1-3 mm) is optimal

## 4.6 Extrusion

**Principle**: A rotating screw pushes melted plastic through a shaped die, producing a product of constant cross-section indefinitely. The most versatile thermoplastic processing method — pipes, sheets, films, wire insulation, and profiles are all extruded.

**Prerequisites**: Single-screw extruder (L/D 20-30:1, barrel diameter 30-120 mm). Shaped die for the target profile. Downstream equipment: cooling bath, puller, cutter or winder. Electrical power (10-100 kW).

**Materials**:
- Thermoplastic granules (PE, PVC, PP, PS, nylon) — pre-dried if hygroscopic

**Procedure**:
1. Set barrel temperature zones (from hopper to die). PE: 160°C → 180°C → 220°C → 240°C (die). PVC: 160°C → 170°C → 180°C → 190°C (die — never exceed 200°C). PP: 180°C → 200°C → 220°C → 240°C (die).
2. Start screw at low speed (10-20 RPM). Begin feeding granules. Allow polymer to melt and fill the barrel (2-5 minutes).
3. Increase screw speed to target (50-200 RPM). Adjust puller speed to match extruder output for consistent dimensions. Output rate for 60 mm screw: 50-200 kg/hour.
4. For pipe extrusion: Route extrudate through sizing sleeve (water-cooled metal ring) to set OD. Apply internal air pressure (0.01-0.05 MPa) to prevent pipe collapse. Water-cool in bath (2-4 m long) at 15-25°C.
5. Cut to length (rotating saw for rigid profiles) or wind onto rolls (film and filament).
6. Monitor dimensions continuously with laser micrometer or manual caliper checks every 15-30 minutes. Wall thickness tolerance: ±5-10% of nominal.

**Calibration/Verification**:
- Dimensional check: Measure OD, ID, and wall thickness at 3 points along a 1 m sample. OD tolerance: ±0.5-1.0 mm for pipes. Wall thickness tolerance: ±5-10%. Use ultrasonic wall thickness gauge for non-destructive measurement.
- Output rate: Weigh extrudate produced in 60 seconds. Target ±5% of specification. Deviations indicate feeding inconsistencies or melt temperature variations.
- Surface quality: Visual inspection for sharkskin (rough surface from melt fracture), die lines (longitudinal streaks from die damage), or color streaking (poor mixing).

**Expected Performance**:
- Output rate: 50-200 kg/hour (60 mm screw diameter)
- Line speed: 1-200 m/minute (depending on product — film is fastest)
- Wall thickness tolerance: ±5-10% of nominal
- Die swell: 10-30% (polymer expands after exiting die — die orifice must be smaller than target dimension)

**Strengths**:
- Continuous process — produces unlimited length of constant cross-section; ideal for pipes, wire insulation, and film
- Lower tooling cost than injection molding — extrusion dies cost $1,000-10,000 (vs. $10,000-100,000+ for injection molds)
- Versatile — any shape that can be drawn through a die profile can be extruded: circles (rod, pipe), slots (sheet, film), complex profiles (window frames, weather stripping)

**Weaknesses**:
- Limited to constant cross-section parts — cannot produce features perpendicular to extrusion direction (holes, flanges, undercuts)
- Dimensional control depends on consistent screw speed, temperature, and puller speed — requires active monitoring and adjustment
- Start-up waste — 5-20 kg of material wasted during start-up until process stabilizes and dimensions are on-spec

## Quantitative Parameters

## Thermoplastic Properties Comparison

| Property | LDPE | HDPE | PP | Rigid PVC | Nylon 6,6 | PS (crystal) | PTFE |
|----------|------|------|-----|-----------|-----------|---------------|------|
| Density (g/cm³) | 0.92 | 0.95 | 0.90 | 1.40 | 1.14 | 1.05 | 2.17 |
| Tensile (MPa) | 8-25 | 25-45 | 30-40 | 45-55 | 70-85 | 35-55 | 20-35 |
| Melt temp (°C) | 105-115 | 130-135 | 160-165 | N/A (decomposes) | 255-262 | 100-110 | 327 (sinter) |
| Service max (°C) | 80 | 100 | 120 | 60 | 120 | 80 | 260 |
| Shrinkage (%) | 1.5-3.0 | 1.5-3.0 | 1.0-2.5 | 0.2-0.4 | 1.0-1.5 | 0.3-0.6 | 3.0-6.0 |
| Water absorption (%) | <0.01 | <0.01 | <0.01 | <0.1 | 2.0-2.5 | <0.05 | <0.01 |

## Processing Methods Comparison

| Method | Output | Cycle Speed | Tooling Cost | Best For |
|--------|--------|-------------|-------------|----------|
| Injection molding | Discrete parts | 10-60 s cycle | High ($10K-100K+) | Complex 3D shapes, high volume |
| Extrusion | Continuous profile | 1-200 m/min | Low ($1K-10K) | Pipes, sheet, film, wire |
| Blow molding | Hollow parts | 5-30 s cycle | Medium ($3K-30K) | Bottles, tanks, containers |
| Thermoforming | Sheet-formed parts | 1-5 min cycle | Very low ($50-1K) | Large flat/curved parts, short runs |
| Compression molding | Flat/simple parts | 2-10 min cycle | Low ($500-5K) | [Thermosets](./thermosets.md), rubber, large parts |

## Extrusion Temperature Profiles (°C)

| Polymer | Zone 1 | Zone 2 | Zone 3 | Zone 4 (Die) |
|---------|--------|--------|--------|--------------|
| PE | 160 | 180 | 220 | 240 |
| PVC | 160 | 170 | 180 | 190 |
| PP | 180 | 200 | 220 | 240 |
| PS | 170 | 190 | 200 | 210 |
| Nylon 6,6 | 240 | 250 | 270 | 280 |

## Scaling Notes

- **Injection molding**: Clamp force scales with projected area of the part. A 200 cm² part needs 60-100 tons clamp. Industrial machines range from 50 tons (small parts) to 5000+ tons (automotive bumpers). Bootstrapping: manual plunger machine (heated barrel, lever-actuated plunger, simple brass mold) produces functional parts at a fraction of the cost.
- **Extrusion**: Output rate scales with screw diameter. 30 mm screw: 10-30 kg/hour. 60 mm screw: 50-200 kg/hour. 120 mm screw: 500-1500 kg/hour. Longer L/D ratio (25-30:1) provides better mixing and more stable output than short screws (15-20:1).
- **Blow molding**: Extrusion blow molding is the simplest route for hollow parts. Mold can be aluminum or even wood for low-pressure, short-run products — much cheaper than injection molds. PET stretch-blow molding requires two-stage process (preform injection → reheat → stretch-blow) but produces the strongest, clearest bottles.
- **Minimum bootstrap scale**: A hand-cranked extruder (20 mm screw, 500 mm L/D) can produce small-diameter rod and tube from LDPE or PS. An electrically heated plunger molder can produce simple parts. Both are achievable at moderate technology level without precision hydraulics.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Short shots (incomplete fill) | Insufficient injection pressure or melt temperature | Increase injection pressure 10-20%; raise barrel temperature 5-10°C; increase injection speed |
| Flash (excess material at parting line) | Insufficient clamp force or excessive injection pressure | Increase clamp force; reduce injection pressure; check mold alignment and wear |
| Sink marks (surface depressions) | Insufficient holding pressure/time; wall thickness too variable | Increase holding pressure and time; redesign part for more uniform wall thickness (target ±10% variation) |
| Warpage (part bends after ejection) | Uneven cooling; asymmetric wall thickness | Equalize mold cooling (check water flow in all channels); redesign for symmetric wall thickness; lower ejection temperature |
| Silver streaks (moisture) | Wet resin (nylon, PET, PC) | Dry resin to <0.2% moisture (80-120°C, dehumidifying dryer, 2-4 hours) |
| Burns (dark spots) | Trapped air or gas overheated in mold | Add or enlarge mold vents (0.02-0.05 mm deep channels at parting line); reduce injection speed |
| PVC discoloration (yellow/brown) | Temperature exceeded 200°C; insufficient stabilizer | Lower barrel temperature; verify tin stabilizer at 0.5-3 phr; check for hot spots in barrel |
| Extrudate dimension variation | Screw speed fluctuation; inconsistent feed; temperature variation | Stabilize screw speed (DC drive controller); ensure consistent hopper feeding; check barrel heater zones |

## Safety

- **PTFE fume fever**: Overheating PTFE above 350°C decomposes it into toxic pyrolysis products including perfluoroisobutylene (PFIB, lethal at low ppm) and carbonyl fluoride. Inhalation causes polymer fume fever — flu-like symptoms (chills, fever, cough) appearing 4-8 hours after exposure. Sintering at 380°C must use calibrated temperature controllers with high-limit shutoff. Never smoke after handling PTFE (contaminated hands transfer PTFE to cigarettes, which pyrolyze it at the tip). Ventilate sintering ovens to outside air.
- **Pyrophoric triethylaluminum (TEA)**: The Ziegler-Natta co-catalyst for HDPE ignites spontaneously on contact with air. Handle only under inert atmosphere (nitrogen) in sealed, purged systems. For fires: Class D dry powder extinguisher (dry sand or Met-L-X). NEVER use water, CO₂, or foam. TEA autoignition temperature: below room temperature on contact with air.
- **Molten polymer burns (200-320°C)**: Melted thermoplastics stick to skin on contact and cannot be wiped off — wiping spreads the burn. If molten polymer contacts skin, cool immediately under running water for 15+ minutes. Do NOT peel or wipe. Wear heat-resistant gloves, long sleeves, and face shield when operating extruders or injection molding machines.
- **Plastic dust explosions**: Fine thermoplastic powders (PE, PVC, PS) form explosive dust clouds. PE dust MEC: 20-30 g/m³. PS dust Kst: 110-160 bar·m/s (St Class 1). Ground all equipment. Maintain ventilation. Clean up accumulated dust regularly.
- **VCM exposure** (PVC production): Confirmed human carcinogen (IARC Group 1). Closed systems, continuous air monitoring, explosion-proof equipment. See [Synthetic Polymers](./synthetic.md) for full hazard data. Residual VCM in finished PVC: <1 ppm (food-grade: <0.1 ppm).

## Quality Control

## Incoming Resin
- **Melt Flow Index (MFI)**: ASTM D1238. Verify MFI is within specification (±10% of nominal). Out-of-range MFI indicates wrong grade, degradation, or contamination.
- **Moisture content**: Karl Fischer titration. Nylon and PET must be <0.2% before processing. PE, PP, PVC: <0.05%.
- **Visual**: Check granules for contamination (black specks, foreign material, color variation).

## Processed Parts
- **Dimensional inspection**: Digital calipers at critical dimensions, every 50-100 shots. Record and trend — gradual drift indicates mold wear or process drift.
- **Weight consistency**: Weigh 10 consecutive parts. Variance must be <0.5%.
- **Visual inspection**: Flash, short shots, sink marks, burns, silver streaks, weld lines, discoloration.
- **Tensile test** (destructive, periodic): ASTM D638. Verify tensile strength and elongation meet material specification.

## Extruded Products
- **OD and wall thickness**: Ultrasonic gauge or caliper at 3 points per 1 m sample. Wall thickness tolerance: ±5-10%.
- **Surface quality**: Visual — no sharkskin, die lines, or discoloration.
- **Pressure test** (PVC pipe): Hydrostatic test at 2× working pressure for 1 hour. No leaks, no deformation.

## Variations and Alternatives

## Blow Molding
- **Extrusion blow molding**: Continuous parison extruded downward, enclosed in split mold, inflated with compressed air (0.2-1.0 MPa). Produces bottles, jerry cans, fuel tanks. Blow ratio (max diameter / initial parison diameter): 2:1 to 7:1. Mold can be aluminum or wood for low-pressure products.
- **Injection blow molding**: Injection mold a preform (test-tube shape), then reheat and stretch-blow with air (0.3-1.5 MPa). Biaxial stretching orients PET molecules, improving barrier properties (O₂ permeability reduced 2-3×) and tensile strength (300%+ improvement). Used for PET beverage bottles.

## Thermoforming
- **Vacuum forming**: Heat sheet to just above Tg (PS ~95°C, PE ~110-120°C, PVC ~80-90°C). Apply vacuum through 0.5-1 mm holes in mold surface. Atmospheric pressure (0.1 MPa) pushes sheet onto mold. Mold can be wood, plaster, or cast aluminum. Products: trays, containers, signs, boat hulls.
- **Pressure forming**: Compressed air (0.3-0.7 MPa) above sheet + vacuum below. Higher forming pressure for sharper detail. Draw ratio limited to 0.5:1 for vacuum, 1.5:1 for pressure forming with plug assist.

## Additional Thermoplastics (Name-Only References)
- **Polycarbonate**: Bisphenol-A + phosgene; impact resistance 850-1000 kJ/m²; optical discs (CD/DVD); safety goggles. See [Synthetic Polymers](./synthetic.md).
- **ABS**: Acrylonitrile + butadiene + styrene; LEGO bricks (tolerance ±0.01 mm); 3D printing filament (FDM at 220-250°C). See [Synthetic Polymers](./synthetic.md).
- **Acrylic (PMMA)**: Light transmission 92%; aircraft canopies; aquariums. See [Synthetic Polymers](./synthetic.md).
- **Polypropylene (PP)**: Density 0.90 g/cm³ (lightest commodity plastic); living hinge (0.2-0.5 mm, millions of flex cycles); autoclavable at 121°C. Similar to PE but higher service temperature.

## See Also

- **[Thermosets](thermosets.md)**: Irreversibly crosslinked polymers — higher temperature capability but cannot be reprocessed
- **[Composites](composites.md)**: Fiber-reinforced polymers using thermoplastic or thermoset matrices
- **[Synthetic Polymers](synthetic.md)**: Synthetic elastomers (NBR, neoprene, silicone, PU) and specialty polymers (polycarbonate, acrylic)
- **[Natural Polymers](natural.md)**: Rubber, gutta-percha, shellac, and other bio-based polymers
- **[Petrochemicals](../chemistry/petroleum-alternatives.md)**: Monomer and feedstock production
- **[Coatings](../chemistry/coatings.md)**: Paint and protective coating formulations using thermoplastic binders
- **[Solvents](../chemistry/solvents.md)**: Solvents for polymer processing and cleaning
- **[Electrolysis](../chemistry/electrolysis.md)**: Chlorine and NaOH production for PVC
- **[Electrical Systems](../electronics/electrical-systems.md)**: Wire and cable insulation using PE, PVC, and silicone
- **[Data Storage](../computing/data-storage.md)**: Optical disc substrates (polycarbonate, PMMA)


[← Back to Polymers & Composites](index.md)
