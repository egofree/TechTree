# Thermoplastic Polymers

> **Node ID**: polymers.thermoplastics

Process-level reference for thermoplastics relevant to the tech tree. Covers synthesis routes, processing conditions, properties, and key applications. Feedstocks come from [Petrochemicals](../chemistry/petroleum-alternatives.md); polymerization reactors and extruders rely on the Machine Tools stage.

## Polymer Processes

### Polyethylene (PE)

Ethylene gas polymerization. Two industrial routes with very different conditions:

**[LDPE](../glossary/ldpe.md)** (low-density): High-pressure free radical process. 1000-3000 atm, 100-300°C, peroxide initiator (e.g., benzoyl peroxide). Tubular or autoclave reactor. Branched chain structure gives flexible, transparent material.

**[HDPE](../glossary/hdpe.md)** (high-density): Low-pressure Ziegler-Natta process. 1-20 atm, 50-80°C, TiCl₄/AlEt₃ catalyst system. Linear chain structure yields stiffer, stronger material with higher crystallinity.

Properties: chemically resistant, easy processing, inexpensive, good electrical insulator. Applications: containers, piping, cable insulation, moisture barriers, blown film, geomembranes.

### Polyvinyl Chloride (PVC)

Monomer route: ethylene + Cl₂ → 1,2-dichloroethane (EDC) → thermal pyrolysis at 450-550°C → vinyl chloride monomer (VCM) + HCl byproduct.

Polymerization: suspension process. Water continuous phase, 40-70°C, peroxide initiator (e.g., lauroyl peroxide). PVC powder recovered by centrifugation and drying.

- **[Rigid PVC](../glossary/rigid-pvc.md)** (uPVC): no plasticizer. Pipes, fittings, valves, chemical-resistant ductwork.
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

PTFE does not melt-flow like other thermoplastics. It must be **[sintered](../glossary/sintered.md)** above its melting point (~380°C, well above most thermoplastics) in a controlled cycle, or paste-extruded with a lubricant carrier that is later evaporated off.

Properties: chemically inert (resists nearly all solvents, acids, and bases), very low coefficient of friction, service temperature range -200 to +260°C, excellent dielectric. Applications: chemically inert seals and gaskets, non-stick surfaces, wire insulation, bearing surfaces, diaphragm pump membranes.

### Name-Only Mentions

- **Polycarbonate**: bisphenol-A + phosgene interfacial condensation; impact-resistant windows (notched Izod 850-1000 J/m — virtually unbreakable by impact), optical discs (CD/DVD substrate, 1.2 mm injection-molded disc — polycarbonate's optical clarity and dimensional stability enable the sub-micron pit geometry required for data storage), eyeglass lenses, safety helmets, automotive headlamp lenses
- **ABS**: acrylonitrile + butadiene + styrene terpolymer; injection-molded housings (LEGO bricks are injection-molded ABS — dimensional tolerance ±0.01 mm for the interlocking studs, demonstrating the material's moldability and consistency), enclosures, pipe fittings, automotive interior trim, 3D printing filament (FDM printers — ABS prints at 220-250°C, requires heated bed at 100-110°C to prevent warping)
- **Acrylic (PMMA)**: methyl methacrylate bulk or suspension polymerization; transparent windows (light transmission 92% — clearer than glass at 90%), optical components, light guides (fiber optic faceplates, edge-lit signage), aquariums (cast PMMA sheets up to 300 mm thick, withstanding hydrostatic pressure), dentures, automotive taillight lenses, aircraft canopies (WWII fighter aircraft used PMMA canopies — 10× lighter than equivalent glass, shatterproof)

## Processing Methods

Converting raw thermoplastic granules or powder into finished products requires controlled heating, shaping, and cooling. All methods share the same basic cycle: heat above melt temperature → shape → cool below solidification temperature.

### Injection Molding

**Principle**: Heat plastic to melt (180-300°C depending on polymer — PS 180-220°C, PE 200-260°C, PP 220-260°C, PC 280-320°C), inject under high pressure (50-200 MPa) into a closed steel mold, cool until solid, eject finished part.

**Machine design**: Heated barrel with a reciprocating screw. The screw has a dual function — it rotates to melt and convey plastic forward (friction + external heater bands provide heat — ~70% of melting energy comes from mechanical shear, 30% from external heaters), then pushes forward axially to inject the accumulated melt into the mold. Barrel zones: feed zone (cool, accepts granules from hopper), compression zone (channel depth decreases, melting occurs via shear heating), metering zone (shallow, constant-depth channel, homogenized melt at uniform temperature).

**Mold**: Two steel plates (cavity and core — usually P20 tool steel for production molds, hardened to HRC 30-35 for wear resistance) with machined cavity defining part shape. Includes cooling channels (water circulation at 10-30°C for temperature control — cooling capacity must remove the heat of the injected melt, typically 10-30 kW per molding cycle), ejector pins (push part out after cooling — activated by a hydraulic or mechanical ejector plate), runner system (channels conveying melt from injection point to cavity — cold runners are machined into the mold plates and ejected with the part; hot runners use heated probes to keep the runner channel molten between shots, eliminating runner waste), and gate (narrow entry into cavity — controls flow pattern and breaks clean when part is ejected. Gate types: edge gate, pinpoint gate, fan gate, submarine gate — each suited to different part geometries). Mold design is the dominant cost — precision-machined tool steel, $10K-$100K+ for production molds. Mold lifetime: 100,000-1,000,000+ shots depending on polymer abrasiveness (glass-filled nylon wears molds fastest).

**Cycle time**: 10-60 seconds depending on part size and wall thickness. Cooling time dominates (typically 50-70% of cycle). Thicker walls require disproportionately longer cooling — a 4 mm wall takes ~4× longer to cool than a 2 mm wall (cooling time scales roughly with wall thickness squared, following Fourier's law of heat conduction).

**Products**: Housings (the highest-volume application — virtually every plastic enclosure from TV remotes to laptop cases to automotive interior trim is injection-molded), containers (food containers, bottle caps, pails — PP and PE dominate), gears and bearings (nylon and acetal/POM gears replace metal in many low-load applications — nylon gears run quietly without lubrication), fittings (pipe fittings, electrical connectors, plumbing hardware), caps and closures (screw caps, snap-fit lids — injection molding produces the precision threads and sealing surfaces required), complex 3D shapes with tight tolerances (±0.05-0.25 mm depending on material and size — tighter tolerances achievable with low-shrinkage materials like polycarbonate vs. high-shrinkage like polyethylene). The highest-volume plastic processing method — over 50% of all thermoplastic products are injection-molded.

**Bootstrap approach**: Manual plunger machine — heated barrel (externally heated steel tube, 30-50 mm bore diameter), lever-actuated plunger (manual force replaces hydraulic injection — a 1 m lever arm gives ~10:1 mechanical advantage, so a 50 kg force on the lever produces ~5 kN injection force, sufficient for small parts in low-viscosity polymers), simple brass or steel mold (two plates clamped together with bolts, hand-machined cavity — surface finish depends on the mold-maker's skill). Much slower cycle (minutes, not seconds) and lower pressure, but achievable without precision hydraulics. Start with low-melt-temperature polymers (LDPE at 105-115°C, PS at 180-200°C) to minimize heating demands. A bootstrap injection molder can produce functional parts (bushings, spacers, simple housings, washers, caps) that would otherwise require metal machining — dramatically reducing the need for precision metalworking in early stages of industrialization.

### Extrusion

**Principle**: Continuous process. A rotating screw pushes melted plastic through a shaped die, producing a product of constant cross-section indefinitely. The most versatile thermoplastic processing method — any shape that can be extruded through a die profile can be produced continuously.

**Barrel and screw**: Similar to injection molding but the screw only rotates (no reciprocating action). Three zones: feed (granules enter from hopper, channel is deep to accept loose material), compression (channel depth decreases progressively, melting occurs via shear heating from the rotating screw and conduction from barrel heater bands — the primary heat source is mechanical shear, not external heaters), metering (shallow, constant-depth channel, steady pressure to die, homogenized melt at uniform temperature). Barrel heated by external bands (typically 3-5 zones, each with independent temperature control). L/D ratio (length-to-diameter) typically 20:1 to 30:1 — longer screws give better mixing, more uniform melt temperature, and steadier output pressure. Short screws (L/D <15:1) are cheaper but produce less uniform output.

**Die**: Steel plate with shaped orifice. Circle → rod or tube (pipe). Slot → sheet or film (a 1.5 m wide slot die produces flat film at 50-200 m/min). Complex profile → window frames, weather stripping, custom shapes. Die design is critical — plastic swells exiting the die (die swell, typically 10-30% — the polymer's viscoelastic memory causes it to expand after the constraining die wall is removed), and flow must be balanced across the orifice for uniform product (a poorly designed die produces uneven wall thickness — thicker at the center or edges depending on flow characteristics). Die land length (the straight section of the die orifice) is typically 10-30× the gap width to allow the polymer to relax and produce stable output.

**Downstream equipment**: Cooling bath (water tank, often with sizing sleeves for pipes — the pipe passes through a precisely-sized cooled metal ring that sets the OD while water contacts the outer surface), puller (pair of rollers or caterpillar belt at controlled speed — maintains tension and dimensions; pull speed must be precisely matched to extruder output for consistent dimensions), cutter (rotating saw for rigid profiles, hot wire or knife for flexible). Winder for continuous film or filament — film is wound onto rolls at 50-200 m/min, filament is wound onto spools for subsequent drawing and weaving.

**Products**: Pipes (PVC, PE, PP — the largest application by volume; PVC-U pipe production exceeds 30 million tonnes/year globally), tubes (medical tubing, automotive fuel lines), sheets (flat sheet for thermoforming, 0.5-6 mm thick), films (packaging film, agricultural film — LDPE blown film is the single largest thermoplastic product by tonnage), filaments (including 3D printing filament — PLA, ABS, PETG sold on 1 kg spools at 1.75 mm diameter), wire insulation (PVC and PE cable compounds — telecommunications wire, power cable insulation), window profiles (PVC-U extruded profiles for double-glazed window frames), weather stripping (flexible PVC and EPDM profiles), hoses (reinforced and unreinforced).

### Blow Molding

**Principle**: Form a hollow tube of molten plastic (parison), enclose it in a split mold, inflate with compressed air to take the mold's internal shape. Produces hollow objects.

**Extrusion blow molding**: Continuous parison extruded downward between two open mold halves. Mold closes around parison, pinching bottom. Compressed air (0.2-1.0 MPa) injected through blow pin at top inflates parison against mold walls. Mold cooled (water channels). Mold opens, part ejected. Trim flash (pinched excess at mold seam). For bottles, jerry cans, fuel tanks, drums. Mold can be aluminum or even wood for low-pressure, short-run products — much cheaper than injection molds. Blow ratio (maximum diameter of blown part / initial parison diameter): 2:1 to 7:1 — higher blow ratios require more elastic polymers (LDPE, PP) and careful die design to avoid excessive thinning at corners.

**Injection blow molding**: First, injection mold a preform (test-tube-shaped thick-walled tube with finished thread neck — the neck finish is molded to final precision in this step). Then transfer preform to blow mold, heat to soften (for PET: heat to 100-110°C, above Tg of 73°C but below cold crystallization temperature of 140°C), inflate with air (0.3-1.5 MPa) and stretch axially with a stretch rod. The biaxial stretching (radial + axial) orients the PET molecules in two directions, dramatically improving barrier properties (O₂ permeability reduced 2-3×), tensile strength (300%+ improvement), and clarity. Used for PET beverage bottles (2-stage process: preform molded centrally, then shipped to bottling plant for stretch-blow molding on-site — this is why new water bottles have a small injection-molded "gate mark" on the center of the base).

### Thermoforming

**Principle**: Heat a flat plastic sheet until rubbery (just above Tg but below melt temperature), then form it over or into a mold using vacuum, pressure, or mechanical force. Tg targets: PS (~95°C), PE (~110-120°C, below melt but above softening point), ABS (~105°C), PVC (~80-90°C).

**Equipment**: Infrared or radiant heaters above the sheet (heat to ~110-160°C depending on polymer — PS, PE, ABS, PVC common). Vacuum table below sheet. Mold (male or female — male = drape over convex shape, female = suck into concave cavity).

**[Vacuum forming](../glossary/vacuum-forming.md)** (simplest method): Clamp heated sheet over mold. Apply vacuum through small holes drilled in mold surface (0.5-1 mm holes, closely spaced at 10-20 mm centers). Atmospheric pressure (0.1 MPa) pushes softened sheet onto mold. Simple, low-cost. Mold can be wood, plaster, cast aluminum — no steel tooling required. Products: trays, containers, signs, blister packs, boat hulls (large molds — a 3 m boat hull can be vacuum-formed from 6 mm HDPE sheet over a wooden male mold), aircraft fairings.

**Pressure forming**: Apply compressed air above sheet (0.3-0.7 MPa) in addition to vacuum below — higher forming pressure for sharper detail and deeper draws. Pressure forming produces parts with detail resolution approaching injection molding at a fraction of the tooling cost.

**Twin-sheet thermoforming**: Heat two sheets simultaneously, form each against a separate mold half, then clamp the two mold halves together while the sheets are still hot — the two halves weld together at the contact surfaces to form a hollow, double-wall part. Used for: pallets, structural panels, hollow luggage, double-wall containers.

**Limitations**: Wall thickness varies — corners and deep draws thin out (draw ratio — depth of draw to minimum dimension — typically limited to 0.5:1 for vacuum forming, up to 1.5:1 for pressure forming with plug assist). Sheet must be purchased or produced (via extrusion) first. Limited to thin-walled parts (typically 0.5-6 mm starting sheet thickness). But extremely low tooling cost makes it ideal for prototyping and short runs — a wooden mold costs $50-200 vs. $10,000-50,000 for an injection mold of similar size.

**Material requirements**: Not all thermoplastics thermoform well. Amorphous polymers (PS, ABS, PVC, PMMA) have a broad softening range and form easily. Semi-crystalline polymers (PE, PP, nylon) have a narrow melting range — they transition from rigid to fully liquid over a very narrow temperature band (~10-20°C), making them difficult to thermoform (the sheet sags uncontrollably once the crystallites melt). HDPE and PP require special techniques (sag bands, plug assist) to control material distribution during forming.

### Compression Molding

**Principle**: Place pre-measured plastic (powder, granules, or preform) in a heated mold cavity. Close mold (upper platen descends). Apply pressure (5-30 MPa). Hold until part cures (thermosets) or cools below solidification (thermoplastics). Open mold, eject part.

**Equipment**: Hydraulic press with heated platens (electric cartridge heaters or steam — steam provides more uniform temperature and faster recovery after mold opening). Press capacity: 10-500+ tons depending on part size. Daylight (maximum mold opening height): 200-1500 mm. Mold: two steel plates with machined cavity, guide pins for alignment, ejector mechanism.

**Advantages**: Simple, low-cost tooling relative to injection molding (no runner system, lower pressures, simpler mold construction — no side actions needed for parts with straight-pull geometry). Minimal material waste (no runners or gates — only flash at the parting line, typically <1% of part weight). Can mold very large parts (compression presses up to 2000+ tons can mold parts 1-2 m in diameter). Works with both thermoplastics and thermosets. Excellent for fiber-reinforced thermosets — compression molding preserves fiber length better than injection molding (the low-flow process minimizes fiber breakage).

**Primary use**: Thermoset molding (phenolic, epoxy, melamine — heat + pressure cures crosslinks). Also used for thermoplastic sheet (heated sheet compressed between mold halves) and rubber vulcanization. Products: electrical insulators, appliance handles, composite panels, brake pads, large flat components, melamine dinnerware, rubber O-rings and gaskets.

## Specific Polymer Properties

### Polyethylene Grades

**[HDPE](../glossary/hdpe.md)** (high-density polyethylene): Density 0.94-0.97 g/cm³. Melt temperature 130-135°C. Tensile strength 25-45 MPa. Modulus 0.8-1.5 GPa. High crystallinity (70-90%) gives stiffness, chemical resistance, and low moisture absorption (<0.01% water absorption at 24 hours). ESCR (environmental stress crack resistance): 10-1000+ hours (F50, bent strip test in Igepal surfactant — critical for chemical tank and pipe applications where stress cracking is the primary failure mode). Used for: chemical storage tanks (rotational molding — HDPE powder tumbled in a heated mold at 250-300°C, wall thickness 3-10 mm), pipes (gas distribution SDR 11 — Standard Dimension Ratio 11, meaning wall thickness = OD/11; working pressure up to 0.4 MPa for gas; water supply SDR 17, up to 1.0 MPa), bottles (blow-molded milk jugs, detergent containers — 30-60 g weight), geomembranes (landfill liners, 1-2.5 mm thickness, welded with hot air or extrusion welder), wire and cable insulation.

**[LDPE](../glossary/ldpe.md)** (low-density polyethylene): Density 0.91-0.93 g/cm³. Melt temperature 105-115°C. Tensile strength 8-25 MPa. Long-chain branching from the high-pressure free-radical process reduces crystallinity (40-60%), giving a flexible, transparent material. Melt flow index (MFI): 0.1-50 g/10 min (lower MFI = higher molecular weight = tougher but harder to process). Used for: film (packaging, agricultural mulch — 15-200 μm thickness, production rate 50-200 m/min on blown film line), squeeze bottles, bread bags, moisture barriers, ice cube trays, heat-shrink tubing (cross-linked LDPE expands when heated above 100°C — used for electrical insulation splices and battery terminal covers).

**[LLDPE](../glossary/lldpe.md)** (linear low-density polyethylene): Density 0.915-0.925 g/cm³. Produced with Ziegler-Natta or metallocene catalysts at low pressure, copolymerizing ethylene with butene, hexene, or octene (2-8% comonomer). Combines the strength of HDPE with the flexibility of LDPE. Metallocene-catalyzed LLDPE (mLLDPE) has narrower molecular weight distribution (Mw/Mn ~2 vs. 4-6 for Ziegler-Natta), giving better optical clarity and more consistent sealing performance. Used for: stretch wrap (cling film — LLDPE's high elongation and puncture resistance make it ideal), heavy-duty sacks, agricultural film, multilayer packaging sealant layers.

### Polypropylene (PP)

Density 0.90 g/cm³ (one of the lightest commodity plastics). Melt temperature 160-165°C. Tensile strength 30-40 MPa. Modulus 1.1-1.6 GPa. Good chemical resistance to acids, alkalis, and solvents at room temperature. Higher temperature capability than PE — continuous service to 100-120°C. Hinge property: thin sections (0.2-0.5 mm) can be flexed millions of cycles without failure (living hinge — used in pill boxes, DVD cases). Autoclavable — used for laboratory containers that must withstand 121°C steam sterilization. Used for: injection-molded containers, battery cases, automotive interior components, carpet fibers, rope, geotextile fabrics.

### PVC Formulations

**Rigid PVC (uPVC)**: Tin stabilizer (0.5-3 phr, typically dibutyltin dilaurate or methyltin mercaptide — prevents HCl elimination during processing). Lubricant (1-5 phr, calcium stearate or paraffin wax — reduces friction in extruder and prevents sticking to mold surfaces). Impact modifier (0-10 phr, MBS or CPE — prevents brittle fracture). Processing aid (0-3 phr, acrylic — improves melt flow). Extrusion temperature: 160-190°C (narrow window — above 200°C, HCl elimination causes rapid degradation and discoloration). Used for: pressure pipes (PVC-U, up to 1.6 MPa working pressure at 20°C), window profiles, guttering, siding, chemical-resistant ductwork.

**Flexible PVC**: Plasticizer 30-80 phr (DOP/DEHP most common — di-2-ethylhexyl phthalate, converts rigid PVC into a soft, rubbery material). Plasticizer molecules insert between polymer chains, reducing intermolecular forces and increasing free volume. More plasticizer → softer, more flexible. 30 phr: semi-rigid (wire insulation). 50 phr: flexible (hose, tubing). 80 phr: very soft (gaskets, shoe soles). Heat stabilizer (2-4 phr, Ba/Zn or Ca/Zn systems). Used for: wire insulation, medical tubing, flooring, shower curtains, inflatable structures, conveyor belts.

### Extrusion Parameters

**Screw design**: L/D ratio 20-30:1 (length-to-diameter). Longer screws provide better melting, mixing, and pressure stability at the die. Three functional zones: feed zone (deep channel, accepts granules), compression zone (channel depth decreases, melting occurs via shear heating and conduction from barrel), metering zone (shallow channel, steady pressure to die, homogenized melt).

**Temperature zones** (barrel, from hopper to die): PE: 160°C → 180°C → 220°C → 240°C (die). PVC: 160°C → 170°C → 180°C → 190°C (die — temperature must increase gradually, never exceed 200°C). PP: 180°C → 200°C → 220°C → 240°C (die). Die temperature typically 5-10°C above the last barrel zone to prevent freeze-off at the die lips.

**Screw speed**: 50-200 RPM. Higher speed → higher output but shorter residence time (risk of incomplete melting). Output rate for a 60 mm diameter screw: 50-200 kg/hour depending on polymer and speed.

**Downstream sizing**: Pipe extrusion uses a sizing sleeve (calibrator) — a water-cooled metal tube slightly larger than the final pipe OD. The extruded pipe enters the calibrator under slight internal air pressure (0.01-0.05 MPa) and is cooled to shape. Vacuum sizing uses a perforated sleeve with vacuum applied through the perforations to pull the hot pipe against the sleeve wall.

### Injection Molding Parameters

**Clamp force calculation**: Clamp force (tons) = projected area of part and runners (cm²) × cavity pressure (30-50 MPa) / 9.81. Example: a 200 cm² part requires 60-100 tons clamp force. Undersized clamp allows mold to open during injection, producing flash.

**Cycle time breakdown**: Injection (1-5 seconds) → packing/holding (2-10 seconds, maintains pressure as part cools and shrinks) → cooling (10-90 seconds, typically 50-70% of total cycle — part must cool below deflection temperature before ejection) → mold open/eject (2-5 seconds). Total cycle: 15-120 seconds. Faster cycles mean higher production rate — a 20-second cycle produces 180 parts/hour per cavity.

**Shrinkage**: PE: 1.5-3.0%. PP: 1.0-2.5%. PVC: 0.2-0.4%. Nylon 6,6: 1.0-1.5% (varies with moisture content — dry mold vs. humid environment). Mold dimensions must be oversized to compensate.

### Recycling and Reprocessing

Thermoplastics can be reprocessed by grinding finished products back into granules, washing (to remove labels, adhesives, and contaminants), and re-extruding into pellets. However, each thermal processing cycle causes some degradation:

- **Chain scission**: Thermal and shear exposure during re-extrusion breaks polymer chains, reducing molecular weight and therefore tensile strength and impact resistance. Typical property loss: ~5-10% per reprocessing cycle for PE and PP. After 3-5 cycles, properties may degrade to the point where the material is unsuitable for its original application.
- **Contamination**: Mixed polymer types (PE + PP + PVC in waste stream) are incompatible — even 2-5% PVC contamination in a PE recycle stream causes dark specks and degraded properties. Sorting by resin identification code (1-7) is essential. Density separation (float-sink tanks: PE/PP float in water, PVC/PET sink) is the most practical automated sorting method.
- **Additive depletion**: Stabilizers, plasticizers, and antioxidants are consumed during first-life service and reprocessing. Virgin stabilizer (0.1-0.5% antioxidant) must be added during re-extrusion to prevent accelerated degradation in the second-life product.
- **Food contact**: Recycled plastic may contain contaminants from previous use that migrate into food. Most jurisdictions require functional barriers or specific recycling processes (e.g., PET bottle-to-bottle recycling with deep vacuum depolymerization) for food-contact recycled content.

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

- **PTFE fume fever (polymer fume fever)**: Overheating PTFE above 350°C decomposes it into toxic pyrolysis products including perfluoroisobutylene (PFIB, lethal at low ppm) and carbonyl fluoride. Inhalation causes polymer fume fever — flu-like symptoms (chills, fever, cough, chest tightness) appearing 4-8 hours after exposure. Repeated episodes cause permanent lung damage. Control processing temperatures strictly — PTFE sintering at 380°C must use calibrated temperature controllers with high-limit shutoff. Never smoke after handling PTFE (contaminated hands transfer PTFE to cigarettes, which then pyrolyze it at the tip). Ventilate sintering ovens to outside air. PTFE starts to decompose detectably at 260°C — the recommended maximum continuous service temperature.
- **Pyrophoric triethylaluminum (TEA) catalyst**: The Ziegler-Natta catalyst system (TiCl₄/AlEt₃) for HDPE uses triethylaluminum as a co-catalyst. TEA ignites spontaneously on contact with air — even trace moisture causes violent ignition. Handle only under inert atmosphere (nitrogen or argon blanket) in sealed, purged systems. Never expose to air or water. For fires, use Class D dry powder extinguisher (dry sand or Met-L-X) — never use water, CO₂, or foam, which react violently with burning organoaluminum compounds. Store in approved flammable-metal cabinets under inert gas. TEA autoignition temperature: below room temperature on contact with air — the compound literally ignites spontaneously.
- **Molten polymer burns (200-300°C)**: Extruded, injected, or compressed thermoplastics at processing temperatures stick to skin on contact and cannot be wiped off — wiping spreads the burn over a larger area. If molten polymer contacts skin, cool immediately under running water for at least 15 minutes. Do not attempt to peel or wipe off. Wear heat-resistant gloves, long sleeves, and a face shield when operating extruders, injection molding machines, or any melt-processing equipment. PE and PP at processing temperature (~220-260°C) cause deep dermal burns — the low thermal conductivity of the polymer means it retains heat against the skin for an extended period, transferring more total energy than a brief contact with a metal surface at the same temperature.
- **Plastic dust explosions**: Thermoplastic powders (PVC, PE, nylon, PS) form explosive dust clouds when fine particles are suspended in air during grinding, pelletizing, or transfer operations. Dust explosion requires: suspended dust above MEC (minimum explosive concentration), confinement, and an ignition source. Maintain ventilation to keep dust concentrations below MEC. Eliminate ignition sources (static discharge — ground all equipment, no open flames, explosion-proof electrical in dust-generating areas). Clean up accumulated dust regularly — layered dust re-entrained by a primary explosion fuels devastating secondary explosions. PE dust MEC: 20-30 g/m³ (very low — easily achieved in grinding operations). PS dust Kst (deflagration index): 110-160 bar·m/s (St Class 1 — strong explosion hazard).
- **VCM (vinyl chloride monomer) exposure**: PVC production involves VCM, a confirmed human carcinogen (IARC Group 1) causing angiosarcoma of the liver. Monomer handling requires closed systems, continuous air monitoring, and explosion-proof equipment. See [Synthetic Polymers](./synthetic.md) for full VCM hazard data. Residual VCM in finished PVC product: typically <1 ppm (reduced from >1000 ppm in the 1970s before the cancer link was established — historical PVC factory workers had elevated liver cancer rates).

---

### Processing Summary

| Process | Output | Speed | Cost | Best For |
|---|---|---|---|---|
| Injection molding | Discrete parts | 10-60 s cycle | High tooling | Complex 3D, high volume |
| Extrusion | Continuous profile | 1-200 m/min | Low tooling | Pipes, sheet, film, wire |
| Blow molding | Hollow parts | 5-30 s cycle | Medium tooling | Bottles, tanks, containers |
| Thermoforming | Sheet-formed parts | 1-5 min cycle | Very low tooling | Large flat/curved parts |
| Compression molding | Flat/ simple parts | 2-10 min cycle | Low tooling | Thermosets, rubber, large parts |

All thermoplastic processing methods share the fundamental cycle: heat above melt temperature → shape under pressure or vacuum → cool below solidification temperature → remove finished part. The choice of process depends on part geometry, production volume, material, and available tooling budget.

---

[← Back to Polymers](index.md)
