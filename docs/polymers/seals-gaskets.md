# Seals, Gaskets & Packing

> **Node ID**: polymers.seals-gaskets
> **Domain**: [Polymers & Composites](./index.md)
> **Dependencies**: [`polymers.rubber`](./rubber.md) (elastomer feedstock), [`machine-tools.machining`](../machine-tools/machining.md) (precision molds)
> **Enables**: [`energy.storage`](../energy/storage.md) (pressure vessel seals), [`gas-handling.basic`](../gas-handling/basic.md) (pipe flange gaskets), [`water`](../water/index.md) (pump shaft seals)
> **Timeline**: Years 10-30
> **Outputs**: o-rings, gaskets, compression-packing, lip-seals
> **Critical**: No — seals are essential for fluid systems but multiple fabrication routes exist


## Overview

![Bellow Seal Gate Valve](../images/polymers/polymers_seals-gaskets.jpg)

> *Image: Valvesonlyusa03, CC0*

Seals, gaskets, and packing are the components that prevent fluid escape at joints, rotating shafts, and valve stems. Every pressure vessel, pipe flange, pump, valve, and engine depends on at least one sealing element. Without them, pressurized systems leak, hydraulic power is lost, and chemical processes contaminate their surroundings.

The four main categories serve distinct functions. **O-rings** are toroidal elastomeric seals that block fluid passage when compressed between two mating surfaces inside a machined groove. **Gaskets** are flat or profiled sheets cut to fit between bolted flanges, sealing static joints under compression. **Compression packing** (also called gland packing) is braided rope-like material packed around valve stems and pump shafts, where the rotating or reciprocating motion prevents use of a static seal. **Lip seals** (shaft seals) have a flexible elastomeric lip that rides against a rotating shaft, retaining lubricant and excluding contaminants.

Material selection dominates seal performance. Temperature, pressure, chemical exposure, and shaft speed determine which elastomer or non-elastomeric material survives in service. A seal that swells, hardens, or extrudes under operating conditions fails regardless of how precisely it was manufactured. The material compatibility table in Section 5 covers five common elastomers against five fluid media.

This capability sits downstream of [Rubber Production](./rubber.md) (vulcanized compound feedstock) and [Machining](../machine-tools/machining.md) (precision mold cavities and grooves), and upstream of every fluid-handling system in the tech tree.


## Prerequisites

### Materials
- [Vulcanized rubber compound](./rubber.md) (NR, NBR, neoprene, EPDM, or silicone — selected by service conditions)
- [PTFE sheet](./thermoplastics.md) (chemically inert, -200°C to +260°C service range)
- Cork-rubber sheet (cork granules 50-70% by volume blended with NR or NBR binder, compressed and vulcanized)
- Compressed fiber sheet (cellulose or aramid fibers with NBR or SBR binder, compressed at 10-20 MPa)
- Braided yarn for packing (PTFE-coated glass fiber, graphite yarn, or aramid fiber)

### Tools and Equipment
- [Compression mold](../machine-tools/hydraulic-press.md) with heated platens (10-50 ton capacity, 150-180°C)
- [Injection molding machine](../machine-tools/machining.md) for high-volume O-ring production (50-200 MPa injection pressure)
- Steel rule die or [CNC cutter](../machine-tools/machining.md) for gasket cutting from sheet
- Braiding machine (16-36 carrier, maypole pattern) for compression packing
- [Hydraulic press](../machine-tools/hydraulic-press.md) (5-20 ton) for packing ring forming
- Shore A durometer (ASTM D2240) for hardness verification
- Micrometer or caliper (0.01 mm resolution) for dimensional inspection

### Infrastructure
- Ventilated mixing and molding area (vulcanization fume extraction)
- Temperature-controlled curing oven or autoclave (140-180°C)
- Clean storage for finished seals (dust-free, away from UV and ozone sources)


## Bill of Materials

### O-Ring Compound (per 1000 O-rings, AS568-214 size: 25.07 mm ID × 3.53 mm CS)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| NBR compound (Shore A 70, pre-mixed) | 1.8-2.2 kg | [Rubber Production](./rubber.md) — nitrile compound | FKM compound (fluorocarbon, for fuel/chemical service), EPDM (for steam/water) |
| Mold release agent (zinc stearate) | 10-20 g | [Chemistry](../chemistry/alkalis.md) — zinc stearate powder | Silicone spray (may contaminate critical seals) |
| Mold cleaning solvent (isopropanol) | 50-100 ml | [Chemistry](../chemistry/solvents.md) — IPA | Toluene (stronger, higher exposure risk) |

### Flat Gasket (per 100 gaskets, 150 mm NB ANSI 150 flange, 1.5 mm thick)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| NBR rubber sheet (Shore A 60, 1.5 mm) | 4.5-5.0 kg | [Rubber Production](./rubber.md) — sheeted compound | Cork-rubber sheet (lower pressure rating), compressed fiber sheet (higher temperature) |
| Steel rule die (custom) | 1 unit | [Machine Tools](../machine-tools/machining.md) — laser-cut die board with steel rule blade | Hand-cut from template (slower, less precise) |

### Compression Packing (per 10 packing sets, 5 rings each, 12 mm × 12 mm cross-section for 50 mm shaft)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| PTFE-coated glass fiber yarn | 3.5-4.0 kg | [Thermoplastics](./thermoplastics.md) + [Textiles](../textiles/index.md) | Graphite yarn (higher temperature, lower chemical resistance to oxidizers), aramid fiber (abrasion-resistant) |
| PTFE dispersion (for coating) | 0.5-1.0 kg | [Thermoplastics](./thermoplastics.md) — PTFE fine powder aqueous dispersion | None — PTFE coating is the standard surface treatment |

### Lip Seal (per 500 seals, 50 mm shaft diameter)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| NBR compound (Shore A 72 lip, Shore A 85 body) | 8-10 kg | [Rubber Production](./rubber.md) — dual-durometer compound | FKM for high-temperature shafts (above 120°C) |
| Steel inner case (stamped, 1.0 mm CRS) | 500 units | [Metals](../metals/index.md) — cold-rolled steel strip, stamped | Stainless steel (corrosive environments) |
| Garter spring (spring steel wire, 0.5 mm) | 500 units | [Metals](../metals/index.md) — spring wire coiled | None — spring provides radial lip loading


## Process Description

### O-Ring Manufacturing

**Principle**: An O-ring is a torus of vulcanized elastomer that seals when compressed 15-30% of its cross-section between two mating surfaces. The seal operates in two modes: static (face seal or radial seal between non-moving parts) and dynamic (reciprocating or rotary motion across the seal surface). Compression of the cross-section fills the gland clearance gap, and system pressure energizes the seal against the low-pressure side of the groove.

**Prerequisites**: Compounded rubber (mixed on two-roll mill or Banbury per [Rubber Production](./rubber.md)). Precision mold cavity machined to ±0.02 mm tolerance (groove dimensions specified by AS568 or ISO 3601). Hydraulic press with heated platens.

**Materials**:
- Rubber compound preform (weight = O-ring volume × compound density × 1.05 for flash, typically 1.5-3.0 g per O-ring for standard sizes)
- Mold release (zinc stearate or silicone spray)

**Procedure**:
1. Weigh preform to ±2% of target weight. Excess material causes thick flash; insufficient material causes underfill and voids.
2. Place preform in mold cavity. Close mold halves.
3. Compress at 10-20 MPa platen pressure. Heat to 150-170°C (NBR), 160-180°C (EPDM), or 140-160°C (NR). Cure time: 3-8 minutes for injection molding, 8-15 minutes for compression molding (time depends on cross-section thickness — roughly 1 minute per mm of section).
4. Open mold. Eject O-ring. Trim flash at parting line (flash thickness target: <0.13 mm, removed by cryogenic deflashing or manual trimming).
5. Post-cure in air oven at 150°C for 4 hours (reduces compression set by 10-20% for NBR and EPDM).

**Calibration/Verification**:
- Cross-section diameter: Measure at 4 points 90° apart with optical comparator or micrometer. Tolerance: ±0.10 mm for standard commercial grade (ISO 3601-1 Class B), ±0.05 mm for precision grade (Class A).
- Inner diameter: Measure with cone gauge or optical system. Tolerance: ±0.20 mm for standard sizes below 50 mm ID.
- Hardness: Shore A durometer at 3 points on cross-section. Target: ±3 Shore A units of specification.

**Expected Performance**:
- Service pressure: 0-35 MPa static (with proper gland design and anti-extrusion backup rings above 10 MPa)
- Temperature range: -40°C to +120°C (NBR), -50°C to +150°C (EPDM), -20°C to +200°C (FKM)
- Seal life: 1000-10,000 hours dynamic, 5-20 years static (depends on temperature, pressure cycling, fluid compatibility)

### Gasket Cutting from Sheet Materials

**Principle**: Flat gaskets seal bolted flange joints by filling surface irregularities under bolt compression. The gasket material must be compliant enough to conform to flange faces (surface roughness Ra 3.2-12.5 μm typical for non-metallic gaskets) yet strong enough to resist internal pressure without blowout. Bolt load compresses the gasket to 30-50% of original thickness, creating the seal.

**Prerequisites**: Sheet material (rubber, cork-rubber, PTFE, or compressed fiber) in correct thickness. Steel rule die or cutting template. Clicker press or hydraulic press (5-10 tons) for die cutting.

**Materials**:
- Rubber sheet (NR, NBR, neoprene) — 0.5-6.0 mm thickness, Shore A 50-80
- Cork-rubber sheet — 1.5-6.0 mm, for low-pressure water and oil service (PN 10-16)
- PTFE sheet — 1.0-6.0 mm, for chemical service (all acids, bases, solvents except molten alkali metals)
- Compressed fiber sheet — 0.5-3.0 mm, for steam and hydrocarbon service to 400°C

**Procedure**:
1. Select sheet material and thickness per service conditions (see Material Selection table in Section 5).
2. Mount steel rule die on clicker press cutting board. Steel rule blade height: 23-32 mm, blade thickness 0.7-1.0 mm, bevel angle 20-25°.
3. Place sheet on cutting board under die. Actuate press. Cutting pressure: 5-15 MPa on blade edge. One stroke per gasket for rubber and cork-rubber; PTFE may require two strokes or a sharper blade due to its tendency to deform rather than shear.
4. Remove cut gasket from die. Inspect inner and outer edges for nicks, tears, or burrs. PTFE gaskets: check for delamination at cut edges.
5. For hand-cut gaskets (no die available): trace flange gasket footprint onto sheet material using the flange face as a template. Cut with a sharp utility knife or fine-tooth coping saw. Punch bolt holes with a hollow punch set (3-5 mm undersized from bolt diameter for clearance).

**Calibration/Verification**:
- Thickness: Measure at 4 points with micrometer. Tolerance: ±10% of nominal thickness.
- Inner and outer diameter: Measure with caliper. Tolerance: ±0.5 mm.
- Visual: No cracks, tears, or foreign inclusions. PTFE gaskets must have smooth, unfractured cut edges.

**Expected Performance**:
- Maximum service pressure: 1.0-4.0 MPa (rubber/cork), 2.0-7.0 MPa (compressed fiber), 0.5-2.0 MPa (PTFE unfilled, increases to 4.0 MPa with filled PTFE)
- Temperature range: -30°C to +120°C (rubber), -40°C to +150°C (cork-rubber), -200°C to +260°C (PTFE), up to +400°C (compressed fiber)
- Bolt stress: 10-30 MPa on gasket area for rubber; 20-60 MPa for compressed fiber

### Compression Packing for Valve Stems and Pump Shafts

**Principle**: Compression packing is a set of braided rings packed into a stuffing box (cylindrical bore around the shaft) and compressed by a gland follower. Axial compression from the gland forces the packing radially inward against the shaft and outward against the stuffing box wall. The packing rings deform to fill surface irregularities and create a labyrinth seal. Controlled leakage of 20-60 drops per minute is normal and necessary for lubrication and cooling of dynamic packing.

**Prerequisites**: Braided packing material (PTFE-coated glass, graphite, aramid). Braiding machine for yarn preparation. Stuffing box dimensions known (shaft diameter, box bore, depth). Gland follower and bolting in serviceable condition.

**Materials**:
- PTFE-coated glass fiber yarn (braided, square cross-section): standard for water and mild chemical service
- Graphite yarn (braided, die-formed rings): for high-temperature steam service above 250°C
- Aramid fiber yarn (braided): for abrasive slurries and high-speed shafts (rotational speed above 10 m/s peripheral speed)

**Procedure**:
1. Measure stuffing box bore, shaft diameter, and box depth. Calculate packing cross-section: (box bore - shaft diameter) / 2. Typical cross-section: 6-25 mm.
2. Cut packing rings from continuous braid. Wrap braid around shaft at exact shaft diameter, mark cut point at 45° angle (scarf cut). Each ring should be a snug fit around the shaft with no gap at the scarf joint.
3. Install first ring in stuffing box. Tamp to bottom with split bushing and mallet. Stagger scarf joints 90° between successive rings.
4. Install remaining rings (typically 4-7 rings per stuffing box), staggering each scarf joint 90° from the previous ring.
5. Install gland follower. Tighten gland nuts finger-tight, then 1/2 turn with wrench. Do not overtighten — packing needs controlled leakage for cooling.
6. Start equipment. Expect initial leakage of 100-200 ml/hour. Adjust gland in 1/4-turn increments over the first 4-8 hours of operation until leakage stabilizes at 20-60 drops/minute (approximately 30-100 ml/hour).

**Calibration/Verification**:
- Leakage rate: Measure with graduated cylinder over 15 minutes. Target: 30-100 ml/hour for water service. Zero leakage indicates overtightening and will cause packing overheating and shaft scoring.
- Gland temperature: IR thermometer or touch. Target: within 15°C of process fluid temperature. If gland is hot to touch (>55°C on a water pump), packing is too tight — loosen gland 1/4 turn.
- Shaft condition: Check for scoring under packing area after first 100 hours. Grooves deeper than 0.1 mm in the shaft indicate abrasive wear — consider harder packing material or shaft sleeve.

**Expected Performance**:
- Service life: 6-24 months depending on shaft speed, temperature, and fluid aggressiveness
- Shaft speed: up to 25 m/s peripheral speed (PTFE packing), 15 m/s (graphite)
- Pressure: up to 3.5 MPa (standard stuffing box design), 7.0 MPa with live-loaded gland

### Lip Seal Construction for Rotating Shafts

**Principle**: A lip seal has a precision-molded elastomeric lip that contacts the shaft at a narrow band (0.25-0.50 mm contact width). A garter spring provides radial load (typically 0.5-1.5 N/mm of shaft circumference) maintaining lip contact as the elastomer relaxes over time. The lip geometry includes a hydrodynamic pumping rib (molded spiral or helical pattern on the air side) that pumps any leakage fluid back into the sealed cavity during shaft rotation.

**Prerequisites**: Dual-durometer rubber compound (soft lip, hard body). Metal stamping for inner case. Garter spring wire. Precision mold with insert for spring groove. Shaft surface finish: Ra 0.2-0.8 μm, no helical grinding marks.

**Materials**:
- NBR compound (Shore A 70-75 for lip, Shore A 82-88 for body)
- Cold-rolled steel strip (1.0 mm thick, stamped to inner case profile)
- Spring steel wire (0.4-0.6 mm diameter, coiled to garter spring)
- Mold release (zinc stearate)

**Procedure**:
1. Stamp inner case from CRS strip on progressive die. Case OD tolerance: ±0.05 mm. Burr height: <0.10 mm.
2. Degrease stamped case in solvent bath (isopropanol). Apply adhesive primer (chemosil or phenolic-based) to bonding surfaces.
3. Load metal case into mold cavity. Place garter spring in mold groove.
4. Inject rubber compound at 60-80°C barrel temperature, 50-150 MPa injection pressure, 150-170°C mold temperature. Cure time: 30-90 seconds depending on compound and wall thickness.
5. Eject seal. Trim flash. Post-cure at 150°C for 2-4 hours.
6. Inspect lip contact surface under 10× magnification. No nicks, tears, or inclusion defects in the sealing lip area.

**Calibration/Verification**:
- Lip inner diameter: Measure with tapered gauge. Must be 1.5-3.0 mm smaller than shaft diameter (interference fit provides initial radial load without spring).
- Radial load: Measure with spring scale pulling lip away from mandrel. Target: 1.0-2.5 N per cm of shaft circumference (total radial load = lip interference + garter spring force).
- Outer case diameter: Measure with caliper. Tolerance: ±0.08 mm (press-fit into housing bore).

**Expected Performance**:
- Shaft speed: up to 15 m/s peripheral speed (NBR lip)
- Pressure: 0-0.03 MPa standard, up to 0.5 MPa with pressure-supported designs
- Service life: 2000-8000 hours at rated speed and temperature
- Temperature: -40°C to +120°C (NBR), -20°C to +200°C (FKM)


## Quantitative Parameters

### Material Compatibility Table

| Material / Medium | Water (20°C) | Mineral Oil (80°C) | 10% NaOH (60°C) | 10% H₂SO₄ (60°C) | Steam (150°C) |
|-------------------|-------------|--------------------|------------------|-------------------|---------------|
| **NR** (natural rubber) | Excellent | Poor (swells 100%+) | Good | Poor | Poor |
| **NBR** (nitrile) | Excellent | Excellent (<5% swell) | Fair | Poor | Fair |
| **Neoprene** (CR) | Excellent | Good (<15% swell) | Excellent | Fair | Good |
| **EPDM** | Excellent | Poor (swells 80%+) | Excellent | Excellent | Excellent |
| **PTFE** | Excellent | Excellent | Excellent | Excellent | Excellent |

Rating criteria: Excellent = volume swell <5%, hardness change <5 Shore A after 70 hours immersion at test temperature per ASTM D471. Good = swell 5-15%. Fair = swell 15-30% with usable but reduced service life. Poor = swell >30% or material degradation, do not use.

### O-Ring Groove Dimensions (Radial Static Seal, ISO 3601-2)

| Cross-Section (mm) | Groove Width (mm) | Groove Depth (mm) | Squeeze (%) | Max Gap (mm) |
|---------------------|-------------------|--------------------|--------------|---------------|
| 1.78 | 2.40 | 1.33 | 17-25 | 0.08 |
| 2.62 | 3.60 | 2.02 | 17-25 | 0.12 |
| 3.53 | 4.80 | 2.74 | 17-25 | 0.15 |
| 5.33 | 7.10 | 4.19 | 17-25 | 0.20 |
| 7.00 | 9.50 | 5.54 | 17-25 | 0.25 |

### Durometer Selection Guide

| Shore A | Application | Examples |
|---------|-------------|---------|
| 50-60 | Low-pressure static seals, large cross-sections | Pipe flange gaskets, door seals |
| 60-70 | General-purpose static and dynamic seals | Hydraulic cylinder seals, O-rings for pumps |
| 70-80 | High-pressure static, moderate dynamic | High-pressure hydraulic O-rings, valve stem seals |
| 80-90 | High-pressure extrusion-resistant | Backup rings, high-pressure static seals (above 20 MPa) |

### Molding Parameters by Process

| Parameter | Compression Molding | Transfer Molding | Injection Molding |
|-----------|--------------------|-----------------|-------------------|
| Pressure (MPa) | 10-20 | 5-15 | 50-200 |
| Temperature (°C) | 150-170 | 150-170 | 150-180 |
| Cycle time (min) | 8-15 | 5-10 | 0.5-2 |
| Part accuracy (mm) | ±0.15 | ±0.10 | ±0.05 |
| Flash thickness (mm) | 0.10-0.30 | 0.05-0.15 | <0.05 |
| Best for | Large gaskets, low volume | Complex shapes | High-volume O-rings |


## Scaling Notes

- **Bench scale** (hand-cut gaskets, single-cavity compression mold): 10-50 seals/day. Suitable for maintenance shops and one-off replacement parts. Tooling cost: $100-500 for a simple compression mold.
- **Pilot scale** (multi-cavity compression mold, clicker press for sheet cutting): 200-1000 seals/day. Requires a hydraulic press and die-cutting capability. Tooling cost: $500-5000.
- **Production scale** (injection molding with 20-100 cavity molds): 5000-50,000 O-rings/day. Injection molds cost $10,000-50,000 but amortize over 1-10 million parts. Cycle times of 30-90 seconds per shot make this economical only above ~10,000 units per size.
- **Gasket cutting scales linearly**: A clicker press with one die produces 200-400 gaskets/hour from sheet stock. Adding a second press or a CNC cutter doubles throughput.
- **Packing production**: Braiding machines run continuously at 10-30 m/min of braided rope output. A single 24-carrier braider produces 50-100 kg of packing yarn per 8-hour shift. Die-forming (cutting and pressing rings from braid) adds 30-60 seconds per ring.
- **Mold bottleneck**: Precision mold cavities (±0.02 mm) require [machining](../machine-tools/machining.md) on a jig grinder or CNC milling machine. Mold lead time: 2-8 weeks. In a bootstrap scenario, single-cavity hand-finished molds are the realistic starting point.


## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| O-ring extrusion into clearance gap | Pressure exceeds gap limit for material hardness | Reduce clearance gap; install anti-extrusion backup ring (PTFE, 0.5-1.0 mm thick); increase durometer to Shore A 80-90 |
| O-ring compression set (flat spots, no rebound) | Undercure, wrong compound, or excessive temperature | Verify cure time/temperature with rheometer; select lower compression-set compound (EPDM <25% vs. NBR <35% at 70°C); reduce operating temperature |
| Gasket blowout from flange | Insufficient bolt load for operating pressure | Increase bolt torque (target 30-50% of bolt yield stress); use thicker or softer gasket material; check flange flatness (<0.2 mm deviation across face) |
| Packing overheating (gland hot to touch) | Gland overtightened, no cooling leakage | Loosen gland 1/4-1/2 turn; verify leakage is 20-60 drops/minute; check shaft for scoring or misalignment (<0.05 mm TIR) |
| Packing leakage excessive (>200 ml/hour) | Worn packing rings, shaft scored, or insufficient gland compression | Replace packing set; inspect shaft — scoring >0.1 mm requires shaft sleeve or replacement; tighten gland 1/4 turn |
| Lip seal leaking immediately | Shaft surface too rough (Ra >0.8 μm) or too smooth (Ra <0.2 μm), wrong installation direction | Polish shaft to Ra 0.2-0.8 μm with plunge grinding (no helical marks); install seal with lip facing the fluid being sealed |
| Lip seal lip hardening and cracking | Operating temperature exceeds elastomer rating | Switch to FKM (up to 200°C) or silicone (up to 230°C); check heat source (bearing failure, process temperature) |
| Gasket chemical attack (swelling, degradation) | Wrong material for process fluid | Cross-reference with Material Compatibility table; replace with chemically resistant material (PTFE for universal resistance) |
| O-ring spiral failure (helical cuts on surface) | Excessive friction in reciprocating service | Reduce surface roughness of cylinder bore; add lubrication; use PTFE-coated O-ring or lower-durometer compound |

## Safety

- **Rubber compounding ingredients**: Accelerators (MBT, TMTD, CBS) and sulfur are skin sensitizers causing allergic contact dermatitis (Type IV hypersensitivity). Sensitization is cumulative and irreversible — once sensitized, even trace exposure triggers dermatitis. Handle all compounding powders with nitrile gloves (not latex — latex allergy risk is separate). Use local exhaust ventilation during weighing and mixing. OSHA PEL for sulfur dust: 15 mg/m³ total dust, 5 mg/m³ respirable fraction.
- **Vulcanization fumes**: Heated rubber releases volatile organic compounds including H₂S, SO₂, and amine decomposition products from accelerators. Acute exposure above 50 ppm H₂S causes respiratory irritation; 100 ppm is IDLH (NIOSH). Cure ovens and press areas require local exhaust ventilation with minimum 15 air changes/hour. Position operators upwind of mold opening. Use calibrated H₂S detectors in curing areas.
- **PTFE fume hazard**: PTFE decomposes above 260°C, releasing toxic fumes including perfluoroisobutylene (PFIB). Polymer fume fever (flu-like symptoms) occurs at 300-400°C decomposition products. Never heat PTFE gaskets above 260°C. If accidental overheating occurs, evacuate area and ventilate for 30 minutes minimum before re-entry. PTFE cutting produces fine dust — wear dust mask (N95 minimum) during cutting operations.
- **Mold and press hazards**: Hydraulic presses at 10-20 MPa (100-200 bar) apply several tons of force. Never reach into mold area while press is actuated. Two-hand trip controls mandatory. Heated platens at 150-180°C cause second-degree burns on 1-second contact. Use thermal gloves rated to 200°C for mold handling.
- **Cutting hazards**: Steel rule dies have exposed sharp edges. Store dies blade-down on magnetic strip or in protective sheaths. Clicker press requires two-hand actuation and light curtain or physical guard over cutting area.

## Quality Control

### O-Ring Acceptance Criteria
- **Cross-section**: ±0.10 mm (commercial) or ±0.05 mm (precision) per ISO 3601-1
- **Hardness**: ±3 Shore A of specified value, measured at 3 points
- **Visual**: No nicks, cuts, flow marks, or contamination on sealing surface. Flash thickness <0.13 mm
- **Compression set**: ASTM D395 Method B, 22 hours at specified service temperature. NBR: <35%. EPDM: <25%. FKM: <30%

### Gasket Acceptance Criteria
- **Thickness**: ±10% of nominal, measured at 4 points
- **Dimensional**: Inner and outer diameter ±0.5 mm
- **Visual**: No cracks, tears, delamination (PTFE), or foreign inclusions
- **Material verification**: Shore A hardness within ±5 units of specification

### Packing Acceptance Criteria
- **Cross-section**: ±0.5 mm of nominal braided size
- **Density**: 1.2-1.6 g/cm³ for PTFE-coated glass (measured by weighing a known length)
- **Yarn integrity**: No loose strands or broken yarns on surface

### Field Tests (No Lab Equipment)
- **O-ring squeeze test**: Place O-ring in groove with mating surface. Proper squeeze: O-ring compresses 15-25% of cross-section. Visually, the O-ring should be slightly flattened at contact points but still round elsewhere. If O-ring rolls freely in groove, groove is too wide. If O-ring bottoms out in groove, groove is too deep.
- **Gasket impression test**: Tighten flange bolts in star pattern to specified torque. Open flange after 30 minutes. The gasket should show full, even compression marks across the entire sealing face — gaps indicate warped flanges or uneven bolt loading.
- **Packing leakage observation**: Run pump or valve. Count drops per minute at gland follower. Target: 20-60 drops/minute (each drop ≈ 0.05 ml). Zero leakage with a cool gland is overtight. Profuse leakage with a hot gland is undertight or worn.


## Variations and Alternatives

### Non-Elastomeric Gasket Materials

When elastomers cannot meet temperature or chemical requirements:

| Material | Temperature Range | Chemical Resistance | Typical Use |
|----------|-------------------|--------------------|-------------|
| PTFE (unfilled) | -200°C to +260°C | Universal (all acids, bases, solvents) | Chemical flanges, laboratory fittings |
| PTFE (glass-filled, 25% glass fiber) | -200°C to +260°C | Universal, higher creep resistance | Higher-pressure chemical service |
| Compressed fiber (aramid + NBR binder) | -40°C to +400°C | Oils, steam, mild chemicals | Steam flanges, heat exchanger joints |
| Expanded graphite sheet | -200°C to +450°C (oxidizing), +2500°C (inert) | Most chemicals, not strong oxidizers | High-temperature steam, exhaust flanges |
| Mica-based (phlogopite mica + binder) | up to +900°C | Limited — alkaline service | Exhaust manifolds, furnace door gaskets |

### O-Ring Alternatives for Special Conditions

- **Quad rings (X-rings)**: Four-lobed cross-section that seals in two planes simultaneously. Lower friction than O-rings in reciprocating service (friction coefficient 0.3-0.5 vs. 0.5-0.8 for O-rings). Same groove dimensions as O-rings — direct drop-in replacement.
- **U-cup seals**: U-shaped cross-section for reciprocating hydraulic cylinders. Pressure-energized — higher system pressure increases sealing force. No anti-extrusion ring needed up to 35 MPa.
- **V-ring seals**: V-stacked packing sets (3-5 rings per set) for reciprocating rods. Adjustable compression via gland nut. Service to 40 MPa. Can be tightened in service without shutdown.

### Low-Technology Seal Methods

In bootstrap scenarios without precision molding:
- **Packed gland with hemp or flax**: Natural fiber packing, lubricated with tallow or graphite grease. Service to 0.5 MPa, 80°C. Short service life (2-4 weeks) but requires no synthetic materials. See [Textiles](../textiles/index.md) for fiber sources.
- **Leather cup packing**: Chromed leather cups for low-speed reciprocating pumps. Service to 2 MPa. Used in hand pumps and well pumps for centuries before rubber seals.
- **Lead gaskets**: Soft metal gaskets for flanged joints in water and low-pressure steam service. Service to 1.0 MPa, 200°C. Requires only [lead casting](../metals/index.md) capability. Replace frequently — lead creeps under load.


## References

- [Rubber Production](./rubber.md) — vulcanization chemistry, compounding ingredients, and molding methods
- [Synthetic Rubbers](./synthetic.md) — NBR, neoprene, EPDM, and FKM elastomer properties
- [Thermoplastic Polymers](./thermoplastics.md) — PTFE sheet and rod stock for gaskets and packing
- [Machining](../machine-tools/machining.md) — mold cavity machining and surface finish requirements
- [Hydraulic Press](../machine-tools/hydraulic-press.md) — compression and transfer molding press requirements
- [Gas Handling](../gas-handling/basic.md) — O-ring and gasket applications in gas distribution systems
- [Water](../water/index.md) — pump shaft seals and pipe flange gaskets for water infrastructure
- ISO 3601-1:2012 — O-ring dimensions and tolerances
- ASTM D471 — Rubber property: effect of liquids (immersion testing for chemical compatibility)
- ASTM D395 — Rubber property: compression set


---

*Part of the [Bootciv Tech Tree](../index.md) • [Polymers & Composites](./index.md) • [All Domains](../index.md)*
