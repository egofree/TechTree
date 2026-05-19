# Thermoplastic Polymers

> **Node ID**: polymers.thermoplastics

Process-level reference for thermoplastics relevant to the tech tree. Covers synthesis routes, processing conditions, properties, and key applications. Feedstocks come from [Petrochemicals](../chemistry/petroleum-alternatives.md); polymerization reactors and extruders rely on the Machine Tools stage.

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

## Processing Methods

Converting raw thermoplastic granules or powder into finished products requires controlled heating, shaping, and cooling. All methods share the same basic cycle: heat above melt temperature → shape → cool below solidification temperature.

### Injection Molding

**Principle**: Heat plastic to melt (180-300°C depending on polymer), inject under high pressure (50-200 MPa) into a closed steel mold, cool until solid, eject finished part.

**Machine design**: Heated barrel with a reciprocating screw. The screw has a dual function — it rotates to melt and convey plastic forward (friction + external heater bands provide heat), then pushes forward axially to inject the accumulated melt into the mold. Barrel zones: feed zone (cool, accepts granules), compression zone (melting), metering zone (homogenized melt).

**Mold**: Two steel plates (cavity and core) with machined cavity defining part shape. Includes cooling channels (water circulation for temperature control), ejector pins (push part out after cooling), runner system (channels conveying melt from injection point to cavity), and gate (narrow entry into cavity — controls flow and breaks clean when part is ejected). Mold design is the dominant cost — precision-machined tool steel, $10K-$100K+ for production molds.

**Cycle time**: 10-60 seconds depending on part size and wall thickness. Cooling time dominates (typically 50-70% of cycle).

**Products**: Housings, containers, gears, fittings, caps, complex 3D shapes with tight tolerances. The highest-volume plastic processing method.

**Bootstrap approach**: Manual plunger machine — heated barrel (externally heated steel tube), lever-actuated plunger (manual force replaces hydraulic injection), simple brass or steel mold (two plates clamped together, hand-machined cavity). Much slower cycle (minutes, not seconds) and lower pressure, but achievable without precision hydraulics. Start with low-melt-temperature polymers (LDPE, PS) to minimize heating demands.

### Extrusion

**Principle**: Continuous process. A rotating screw pushes melted plastic through a shaped die, producing a product of constant cross-section indefinitely.

**Barrel and screw**: Similar to injection molding but the screw only rotates (no reciprocating action). Three zones: feed (granules enter), compression (melting), metering (steady pressure to die). Barrel heated by external bands. L/D ratio (length-to-diameter) typically 20:1 to 30:1 — longer screws give better mixing and steady output.

**Die**: Steel plate with shaped orifice. Circle → rod or tube (pipe). Slot → sheet or film. Complex profile → window frames, weather stripping, custom shapes. Die design is critical — plastic swells exiting the die (die swell, typically 10-30%), and flow must be balanced across the orifice for uniform product.

**Downstream equipment**: Cooling bath (water tank, often with sizing sleeves for pipes), puller (pair of rollers or caterpillar belt at controlled speed — maintains tension and dimensions), cutter (rotating saw for rigid profiles, hot wire or knife for flexible). Winder for continuous film or filament.

**Products**: Pipes, tubes, sheets, films, filaments (including 3D printing filament), wire insulation, window profiles, weather stripping, hoses.

### Blow Molding

**Principle**: Form a hollow tube of molten plastic (parison), enclose it in a split mold, inflate with compressed air to take the mold's internal shape. Produces hollow objects.

**Extrusion blow molding**: Continuous parison extruded downward between two open mold halves. Mold closes around parison, pinching bottom. Compressed air (0.2-1.0 MPa) injected through blow pin at top inflates parison against mold walls. Mold cooled (water channels). Mold opens, part ejected. Trim flash (pinched excess at mold seam). For bottles, jerry cans, fuel tanks, drums. Mold can be aluminum or even wood for low-pressure, short-run products — much cheaper than injection molds.

**Injection blow molding**: First, injection mold a preform (test-tube-shaped thick-walled tube with finished thread neck). Then transfer preform to blow mold, heat to soften, inflate with air. Better dimensional control, especially neck finish (screw threads). Used for precision bottles (PET beverage bottles).

### Thermoforming

**Principle**: Heat a flat plastic sheet until rubbery (just above Tg but below melt temperature), then form it over or into a mold using vacuum, pressure, or mechanical force.

**Equipment**: Infrared or radiant heaters above the sheet (heat to ~110-160°C depending on polymer — PS, PE, ABS, PVC common). Vacuum table below sheet. Mold (male or female — male = drape over convex shape, female = suck into concave cavity).

**Vacuum forming** (simplest method): Clamp heated sheet over mold. Apply vacuum through small holes drilled in mold surface (0.5-1 mm holes, closely spaced). Atmospheric pressure (0.1 MPa) pushes softened sheet onto mold. Simple, low-cost. Mold can be wood, plaster, cast aluminum — no steel tooling required. Products: trays, containers, signs, blister packs, boat hulls (large molds), aircraft fairings.

**Pressure forming**: Apply compressed air above sheet in addition to vacuum below — higher forming pressure for sharper detail and deeper draws.

**Limitations**: Wall thickness varies — corners and deep draws thin out. Sheet must be purchased or produced (via extrusion) first. Limited to thin-walled parts. But extremely low tooling cost makes it ideal for prototyping and short runs.

### Compression Molding

**Principle**: Place pre-measured plastic (powder, granules, or preform) in a heated mold cavity. Close mold (upper platen descends). Apply pressure (5-30 MPa). Hold until part cures (thermosets) or cools below solidification (thermoplastics). Open mold, eject part.

**Equipment**: Hydraulic press with heated platens (electric cartridge heaters or steam). Press capacity: 10-500+ tons depending on part size. Mold: two steel plates with machined cavity, guide pins for alignment, ejector mechanism.

**Advantages**: Simple, low-cost tooling relative to injection molding (no runner system, lower pressures). Minimal material waste (no runners or gates). Can mold very large parts. Works with both thermoplastics and thermosets.

**Primary use**: Thermoset molding (phenolic, epoxy, melamine — heat + pressure cures crosslinks). Also used for thermoplastic sheet (heated sheet compressed between mold halves) and rubber vulcanization. Products: electrical insulators, appliance handles, composite panels, brake pads, large flat components.

## Key Milestones

- ☐ **Chemistry stage**: LDPE production via high-pressure autoclave (requires pressure vessel capability)
- ☐ **Chemistry stage**: Suspension PVC from ethylene/chlorine feedstocks (ties to chlorine plant from the Chemistry stage chemistry)
- ☐ **Chemistry stage**: Crystal PS from styrene monomer (simplest thermoplastic to start with)
- ☐ **Chemistry stage**: Nylon 6,6 condensation polymerization (requires vacuum-capable autoclave)
- ☐ **Chemistry stage**: HDPE via Ziegler-Natta catalyst (requires TiCl₄ from the Chemistry stage chlorosilane chemistry)
- ☐ **Chemistry stage**: PTFE precursor chain (R-22 from chloroform + HF; HF available from the Chemistry stage fluorspar processing)
- ☐ **Vacuum & Optics stage**: PTFE sintering at 380°C (requires furnace control beyond typical polymer processing)
- ☐ **Vacuum & Optics**: EPS foam production (requires pentane recovery and steam molding)

### Safety & Hazards

- **PTFE fume fever (polymer fume fever)**: Overheating PTFE above 350°C decomposes it into toxic pyrolysis products including perfluoroisobutylene (PFIB, lethal at low ppm) and carbonyl fluoride. Inhalation causes polymer fume fever — flu-like symptoms (chills, fever, cough, chest tightness) appearing 4-8 hours after exposure. Repeated episodes cause permanent lung damage. Control processing temperatures strictly — PTFE sintering at 380°C must use calibrated temperature controllers with high-limit shutoff. Never smoke after handling PTFE (contaminated hands transfer PTFE to cigarettes, which then pyrolyze it at the tip). Ventilate sintering ovens to outside air.
- **Pyrophoric triethylaluminum (TEA) catalyst**: The Ziegler-Natta catalyst system (TiCl₄/AlEt₃) for HDPE uses triethylaluminum as a co-catalyst. TEA ignites spontaneously on contact with air — even trace moisture causes violent ignition. Handle only under inert atmosphere (nitrogen or argon blanket) in sealed, purged systems. Never expose to air or water. For fires, use Class D dry powder extinguisher (dry sand or Met-L-X) — never use water, CO₂, or foam, which react violently with burning organoaluminum compounds. Store in approved flammable-metal cabinets under inert gas.
- **Molten polymer burns (200-300°C)**: Extruded, injected, or compressed thermoplastics at processing temperatures stick to skin on contact and cannot be wiped off — wiping spreads the burn over a larger area. If molten polymer contacts skin, cool immediately under running water for at least 15 minutes. Do not attempt to peel or wipe off. Wear heat-resistant gloves, long sleeves, and a face shield when operating extruders, injection molding machines, or any melt-processing equipment.
- **Plastic dust explosions**: Thermoplastic powders (PVC, PE, nylon, PS) form explosive dust clouds when fine particles are suspended in air during grinding, pelletizing, or transfer operations. Dust explosion requires: suspended dust above MEC (minimum explosive concentration), confinement, and an ignition source. Maintain ventilation to keep dust concentrations below MEC. Eliminate ignition sources (static discharge — ground all equipment, no open flames, explosion-proof electrical in dust-generating areas). Clean up accumulated dust regularly — layered dust re-entrained by a primary explosion fuels devastating secondary explosions.

---

*Part of the [Bootciv Tech Tree](../) • [Polymers](./) • [All Domains](../)*
