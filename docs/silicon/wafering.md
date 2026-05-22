# Wafering

> **Node ID**: silicon.wafering
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`silicon.crystal-growth`](crystal-growth.md), [`machine-tools`](../machine-tools/index.md), `chemicals.acids-bases`
> **Timeline**: Years 45-60
> **Outputs**: silicon_wafers, polished_substrates

### Overview

Wafering transforms a single-crystal silicon ingot (boule) into thin, flat, mirror-polished disks that serve as substrates for semiconductor device fabrication. The process is a sequence of mechanical and chemical material removal steps, each progressively finer, that transforms a rough-sawn slice into an atomically flat surface. A 300 mm wafer must be flat to within 2 μm over its entire surface (a ratio of 1:150,000, roughly equivalent to a 1 km road surface varying by 7 mm).

### Ingot Preparation

A silicon boule as grown by the Czochralski (CZ) process is a cylindrical single crystal, 150-300 mm diameter, 1-2 m long, with a rounded crown (seed end) and a tapered tail. Before wafering, the boule must be prepared to a precise cylindrical geometry.

**Cropping**:
- The seed end (crown) and tail are cut off with a diamond-bladed band saw. These portions contain crystal defects (dislocations, inclusions, dopant concentration variations) from the seeding and termination of the crystal pull. Typically 50-100 mm is cropped from each end.
- The cropped pieces are not wasted. They are re-melted in the next crystal pull, recovering the high-purity silicon (electronic grade, >99.9999999% purity or 9N).

**Grinding to diameter**:
- The boule is mounted between centers on a cylindrical grinder. A diamond grinding wheel (200-300 mm diameter, diamond grit 100-200 mesh in resin bond) machines the outer surface to the target diameter with ±0.1 mm tolerance.
- Standard diameters: 150 mm (6 inch), 200 mm (8 inch), 300 mm (12 inch). The grinding removes the boule's as-grown surface, which has surface damage, oxides, and slight ovality from the pulling process.
- Grinding parameters: infeed 0.01-0.05 mm per pass, wheel speed 1500-3000 RPM, workpiece speed 50-200 RPM. Coolant: water with rust inhibitor and lubricant, flooded over the grinding zone at 10-20 liters/min. Dry grinding generates silica dust and overheats the surface.

**Orientation flat or notch**:
- A flat or notch is ground along the length of the boule to indicate the crystal orientation to the wafer fabrication equipment. Crystal orientation determines how the silicon cleaves (breaks along crystal planes), which matters for dicing finished devices.
- For 150 and 200 mm wafers, a flat is ground: the primary flat indicates the {110} plane (for <100> oriented crystals), and a secondary flat (shorter, at a specific angle to the primary) identifies the dopant type (n-type or p-type) and crystal orientation.
- For 300 mm wafers, a single small notch (V-shaped groove, approximately 1 mm deep, ~60° included angle) replaces the flat. The notch takes less material and wastes less silicon. The notch is ground with a shaped diamond wheel in a single pass.

### Wafering (Slicing)

Wafering cuts the cylindrical boule into thin slices (wafers). The two primary methods are inner-diameter (ID) blade sawing and wire sawing. Both are abrasive processes that remove a thin kerf of silicon between each wafer.

**[Inner-diameter (ID) blade saw](../glossary/inner-diameter-id-blade-saw.html)** (standard for 150 and 200 mm wafers):
- The ID saw uses a thin, flat steel blade with a circular hole in the center. The inner edge of the hole is plated with diamond abrasive particles (20-40 μm grain size in a nickel matrix). The blade is tensioned between a flanged collar that stretches it flat and rigid, like a drumhead.
- Blade dimensions: outer diameter 500-800 mm, inner hole (cutting edge) 150-250 mm, blade thickness 0.15-0.2 mm. The thin blade minimizes material loss (kerf). The blade tension must be precisely controlled (typically 30-50 N/mm of blade width) to prevent vibration and wandering.
- The ingot is mounted on a carriage that feeds horizontally into the spinning blade. The blade rotates at 1500-3000 RPM. Cut rate: 2-5 mm/min (a 200 mm wafer cut takes 40-100 minutes). Only one wafer is cut at a time.
- Kerf loss: 0.2-0.3 mm per wafer (the width of material turned into sawdust). For a 0.7 mm thick wafer, this means roughly 30% of the silicon is lost as kerf. A 1 m boule yields roughly 1000 wafers (each 0.7 mm) plus 200-300 mm of kerf waste.
- Coolant: water-soluble oil emulsion (5-10% concentration) or polyethylene glycol (PEG) solution, flooded over the cut zone at 5-15 liters/min to cool the blade, flush away silicon particles, and lubricate the cutting edge.

**[Wire saw](../glossary/wire-saw.html)** (standard for 300 mm wafers, gaining adoption for smaller diameters):
- A single continuous steel wire (0.12-0.18 mm diameter) is wound on grooved wire guides (pulley-like drums, 300-500 mm diameter) in a web of 200-500 parallel strands, spaced at the desired wafer thickness plus kerf (approximately 1.0-1.1 mm pitch for 300 mm wafers).
- The ingot is mounted on a holder and pressed down against the entire wire web simultaneously. As the wire reciprocates (oscillates back and forth at 5-15 m/s), an abrasive slurry cuts all wafers in parallel.
- Slurry composition: silicon carbide (SiC) particles, 10-20 μm grain size (F800-F1200 FEPA grade), suspended in polyethylene glycol (PEG) carrier (viscosity 50-200 cP at 25°C). The slurry is pumped continuously over the wires at 10-30 liters/min. The abrasive particles, trapped between the wire and the silicon, grind a narrow kerf by three-body abrasion.
- Feed rate: 0.1-0.3 mm/min (slower per-wafer rate than ID saw, but all wafers cut simultaneously, so total throughput is much higher). A 300 mm diameter, 1 m long ingot cuts in 4-8 hours, producing all 800-900 wafers at once.
- Kerf loss: 0.15-0.2 mm per wafer (less than ID saw because the wire is thinner than the blade). Less silicon waste means more wafers per boule, which matters when each boule costs thousands of dollars.
- Slurry management: a 300 mm ingot wire cut consumes 50-100 liters of slurry. Used slurry (containing SiC particles mixed with fine silicon powder, ~50% SiC, ~50% Si by weight) can be filtered, washed, and reconstituted, but fresh slurry gives better cutting performance and surface quality.

### Wafer Handling

Freshly cut wafers are fragile, sharp-edged, and easily contaminated by dust, fingerprints, and organic films. Automated handling systems move wafers through the processing sequence without human contact.

**Vacuum pickup**:
- Wafers are picked up by a vacuum wand (a flat polyurethane or PEEK nozzle with a shallow vacuum cup, connected to a low-vacuum source, typically 30-50 kPa below atmospheric). The vacuum holds the wafer by its back side only; the front (device) side must never be touched by anything solid.
- Vacuum pickup requires a smooth back surface. Rough-sawn wafers may not seal well; lapping improves the surface enough for reliable vacuum handling.

**Cassette-to-cassette automation**:
- Wafers are stored in slotted plastic cassettes (25-wafer capacity for 200 mm, 13-wafer for 300 mm). The slots are precision-machined to hold wafers vertically without contacting the front surface. Robots transfer wafers from input cassette to processing station to output cassette.
- This standardizes handling, reduces contamination from human contact (skin oils, particles), and prevents breakage from manual handling errors.

**Edge grinding**:
- After slicing, wafer edges are sharp (90° corners from the saw cut). Sharp edges chip easily during handling and generate particles that contaminate cleanrooms. Edge grinding rounds the wafer perimeter to a controlled profile (typically a compound curve with radii of 0.3-1.0 mm) using a diamond grinding wheel.
- The edge profile is critical for later processing steps: photolithography spin-coating, etching, and deposition all depend on uniform edge geometry to avoid thickness buildup or thinning at the periphery.

### Lapping

Sawn wafers have saw marks, waviness, and subsurface damage from the cutting process. Lapping removes bulk material and improves flatness using free abrasive slurry between two large flat plates.

**Double-sided lapping**:
- Wafers are placed in carriers (perforated brass or plastic plates, approximately 600-800 mm diameter) on a lapping machine with two large cast iron lapping plates (one above, one below, 800-1200 mm diameter). Abrasive slurry (aluminum oxide Al₂O₃, 5-15 μm grain size, in water or glycol carrier) is fed between the plates.
- The plates rotate in opposite directions, and the carriers orbit epicyclically (driven by a sun gear), ensuring uniform material removal from both wafer surfaces simultaneously. The random motion paths prevent directional scratch patterns.
- Material removal: 20-50 μm total (10-25 μm per side). This eliminates most saw damage and improves flatness to 2-5 μm total thickness variation (TTV) across a 200 mm wafer.
- Plate pressure: 10-30 kPa. Cycle time: 15-30 minutes per batch (typically 20-30 wafers per carrier for 200 mm, 10-15 for 300 mm).
- After lapping, wafers are cleaned thoroughly in an ultrasonic bath to remove all embedded abrasive particles. Any remaining Al₂O₃ particles on the wafer surface will cause scratches during the polishing step that follows.

### Etching

Lapping leaves a subsurface damage layer (microcracks and dislocations extending 5-15 μm deep from the mechanical grinding action). Etching removes this damaged layer chemically, exposing pristine single-crystal silicon underneath with no mechanical damage.

**Acid etching**:
- A mixture of nitric acid (HNO₃), hydrofluoric acid (HF), and acetic acid (CH₃COOH) in a typical ratio of 5:3:3 by volume. The nitric acid oxidizes the silicon surface to SiO₂; the hydrofluoric acid dissolves the SiO₂ as fast as it forms. Acetic acid serves as a diluent and buffer that moderates the reaction rate.
- Material removal: 10-20 μm per side. Etch rate: 10-30 μm/min at room temperature. The etch is isotropic (removes material equally in all directions), which rounds sharp corners but produces a smooth, damage-free surface.
- Safety: HF is extremely hazardous. It penetrates skin rapidly (the fluoride ion is small and lipophilic), chelates calcium and magnesium in tissue, and causes deep, painful burns that may not become apparent for hours. Systemic fluoride poisoning can cause cardiac arrhythmia and death. Calcium gluconate gel (2.5-5%) must be immediately available as first aid for skin contact, applied generously to the affected area. Full acid-resistant PPE (face shield, heavy nitrile gloves over neoprene gloves, chemical apron, rubber boots) is mandatory when handling HF.

**[Alkaline etching](../glossary/alkaline-etching.html)** (alternative, safer):
- Sodium hydroxide (NaOH) solution, 10-20% by weight, heated to 60-80°C. Etch rate: 5-15 μm/min. The alkaline etch is anisotropic (etches different crystal planes at different rates: {100} planes etch ~30× faster than {111} planes), producing a textured surface.
- For <100> oriented silicon, the alkaline etch reveals pyramidal textures (4-10 μm feature size) across the entire surface. These pyramids reduce surface reflection from ~35% (polished silicon) to 10-15%, which is beneficial for photovoltaic applications (more light enters the cell).
- Advantage: no HF required. Much safer than acid etching. The textured surface is actually preferred for solar cells. Disadvantage: the textured surface is not suitable for integrated circuit fabrication, which requires a mirror-smooth surface.

### Polishing (CMP)

Chemical-mechanical polishing (CMP) produces the mirror-smooth surface required for photolithography. The wafer surface must be flat to within a few nanometers over the entire wafer area for modern lithography to resolve sub-micron features with sufficient depth of focus.

**CMP process**:
- Wafers are mounted face-down on polishing heads (carriers) that press them against a rotating polyurethane polishing pad (typically 600-800 mm diameter, 1-2 mm thick closed-cell polyurethane). A colloidal silica slurry (SiO₂ particles, 0.05-0.1 μm diameter, 10-30% solids, suspended in NaOH solution at pH 10-11) is dispensed onto the pad surface.
- The alkaline slurry softens the topmost atomic layers of silicon (forms a thin hydrated SiO₂ layer), and the silica particles mechanically remove this softened layer by abrasion. The combined chemical and mechanical action removes material at 0.1-0.5 μm/min.
- Material removal: 5-10 μm total. Final surface roughness: < 0.5 nm Ra (arithmetic mean roughness). The surface appears mirror-smooth to the naked eye and reflects a clear image like a glass mirror.
- Polishing pressure: 20-40 kPa. Platen speed: 30-60 RPM. Carrier speed: 30-60 RPM (counter-rotating to platen for uniform removal). Slurry flow: 100-300 ml/min per polishing head.
- Pad conditioning: a diamond-embedded disk (200-300 grit diamond in nickel bond, 150-200 mm diameter) is pressed against the pad surface periodically (every 30-60 seconds during polishing) to regenerate its texture. Without conditioning, the pad glazes (surface pores compress closed) and removal rate drops by 50-80% over 30 minutes.

**[Double-sided polishing](../glossary/double-sided-polishing.html)** (for 300 mm wafers):
- Both sides polished simultaneously to achieve the tightest flatness requirements. TTV < 2 μm for 300 mm wafers. Local flatness (site flatness, measured over a 25 × 25 mm area): < 0.1 μm. This level of flatness is necessary for deep-UV lithography with depth-of-focus budgets of ±50 nm.

### Cleaning (RCA Clean)

After polishing, wafers carry residues of polishing slurry, organic contaminants (skin oils, airborne organics), metal ions (Fe, Cu, Ni from processing equipment), and particles (silica, pad debris). The RCA clean (developed by Werner Kern at RCA Laboratories in 1965) is the standard sequence for removing all contaminants without damaging the pristine silicon surface.

**SC-1 (Standard Clean 1)**: removes organic contaminants and particles.
- Solution: NH₄OH:H₂O₂:H₂O = 1:1:5 by volume at 75°C. Soak time: 10-20 minutes.
- The hydrogen peroxide (H₂O₂) oxidizes organic matter to CO₂ and water. The ammonium hydroxide (NH₄OH) provides alkalinity (pH ~10) that keeps the silicon surface and silica particles negatively charged through the entire process, preventing particles from re-depositing on the wafer surface by electrostatic repulsion (both the wafer and the particles have the same negative charge).
- Removes particles down to 0.1 μm and cleans organic films from the surface. Also removes some metallic contaminants (Au, Ag, Cu) by complexation with ammonia.
- After SC-1, wafers are rinsed in ultra-pure water (18.2 MΩ·cm resistivity, < 1 particle/mL > 0.1 μm, total organic carbon < 50 ppb) for 5-10 minutes in an overflow rinse tank.

**SC-2 (Standard Clean 2)**: removes metallic contaminants.
- Solution: HCl:H₂O₂:H₂O = 1:1:5 by volume at 75°C. Soak time: 10-20 minutes.
- Hydrochloric acid dissolves metal oxides and hydroxides, forming soluble metal chloride complexes (FeCl₃, CuCl₂, NiCl₂) that remain in solution and are rinsed away. The H₂O₂ keeps the silicon surface oxidized and passivated during cleaning.
- Removes alkali metals (Na, K), alkaline earth metals (Ca, Mg), and heavy metals (Fe, Ni, Cr, Cu, Zn) to surface concentrations below 10¹⁰ atoms/cm² (roughly one metal atom per 10,000 surface silicon atoms). Metal contamination at higher levels degrades gate oxide integrity and minority carrier lifetime.
- After SC-2, a final rinse in ultra-pure water and spin-dry (3000-5000 RPM, nitrogen blow) produces a clean, dry wafer ready for further processing.

**[Hydrofluoric acid dip](../glossary/hydrofluoric-acid-dip.html)** (optional, removes oxide):
- A brief dip (15-60 seconds) in dilute HF (1-5% by weight) removes the native oxide layer (SiO₂, ~1-2 nm thick) that grows naturally on silicon in air at room temperature. The HF etches SiO₂ selectively (etch rate ~100 nm/min for thermal oxide at 5% HF) but does not attack silicon.
- After HF dip, the surface is hydrogen-terminated (Si-H bonds instead of Si-O). The hydrogen-terminated surface is hydrophobic (water beads off) and passivated against re-oxidation for several hours in cleanroom air.
- The HF dip is used when the next processing step requires direct contact with the silicon surface (epitaxial growth, gate oxide formation, metal deposition). If the wafer is being stored or shipped, the native oxide is left in place as a protective layer.

**Drying methods**:
- **Spin rinse dryer**: wafers are spun at 3000-5000 RPM while rinsed with ultra-pure water, then blown dry with filtered hot nitrogen (60-80°C). Centrifugal force removes water from the surface. Fast (3-5 minutes per batch) but can generate particles from water droplets hitting the wafer surface at high speed.
- **[Marangoni drying](../glossary/marangoni-drying.html)** (for critical applications): the wafer is slowly withdrawn from a water bath at 1-5 mm/s while a thin layer of isopropyl alcohol (IPA) vapor is introduced at the water surface. The surface tension gradient between the IPA-rich meniscus and the pure water below (the Marangoni effect) pulls water off the wafer surface as it withdraws, leaving a dry, particle-free surface without mechanical force. Superior to spin drying for wafers with fragile microstructures.

### Wafer Specifications Summary

| Parameter | 150 mm | 200 mm | 300 mm |
|-----------|--------|--------|--------|
| Diameter tolerance | ±0.2 mm | ±0.2 mm | ±0.2 mm |
| Thickness | 0.6-0.7 mm | 0.7-0.8 mm | 0.7-0.8 mm |
| TTV (total thickness variation) | < 5 μm | < 3 μm | < 2 μm |
| Bow | < 30 μm | < 20 μm | < 10 μm |
| Warp | < 40 μm | < 30 μm | < 15 μm |
| Surface roughness (Ra) | < 0.5 nm | < 0.5 nm | < 0.5 nm |
| Orientation flat / notch | flat | flat | notch |
| Crystal orientation | <100> or <111> ±0.5° | <100> or <111> ±0.5° | <100> ±0.5° |
| Particles (> 0.1 μm) | < 10 per wafer | < 10 per wafer | < 5 per wafer |

### Wafer Inspection and Quality Control

Every wafer must be inspected after each major processing step. Defective wafers caught early save the expense of further processing on a part that will ultimately fail.

**Flatness measurement**:
- A capacitive probe or laser interferometer scans the wafer surface and maps thickness variation across the entire diameter. TTV (total thickness variation) is the difference between the thickest and thinnest points on the wafer. For a 300 mm wafer, TTV must be below 2 μm after polishing.
- Local flatness (site flatness): measured over a 25 × 25 mm area, must be below 0.1 μm for advanced lithography. This is verified by interferometric measurement at multiple sites across the wafer surface.

**Surface inspection**:
- Laser scattering: a laser beam scans the wafer surface at oblique incidence. Particles, scratches, and pits scatter light that is detected by photomultiplier tubes. The scatter intensity maps to defect size. Sensitivity: detects particles down to 0.1 μm on polished wafers.
- Bright-field/dark-field microscopy: manual or automated microscope inspection at 100-500× magnification. Used to classify defect types (particle, scratch, pit, haze) identified by laser scattering.

**Dimensional measurement**:
- Wafer diameter: measured with a laser micrometer at multiple points around the perimeter. Tolerance: ±0.2 mm.
- Notch depth and angle: measured with an optical comparator or laser profilometer. The notch must be centered on the crystal orientation within ±0.2°.

### Epitaxial Wafer Considerations

Many IC fabrication processes require an epitaxial layer: a thin (1-100 μm) single-crystal silicon layer grown on top of the polished wafer substrate by chemical vapor deposition (CVD). The epitaxial layer can have a different dopant type and concentration than the substrate, enabling advanced device structures.

**Epitaxial growth process**:
- Wafers are loaded into a quartz or silicon carbide reaction chamber and heated to 1050-1200°C in a hydrogen atmosphere. Silane (SiH₄) or trichlorosilane (SiHCl₃) gas is introduced. The gas decomposes on the hot wafer surface, depositing silicon atoms that adopt the crystal structure of the substrate (epitaxial alignment).
- Growth rate: 0.5-5 μm/min depending on temperature and precursor. The dopant gas (e.g., PH₃ for n-type, B₂H₆ for p-type) is added in controlled trace amounts (ppm level) to set the epitaxial layer's electrical properties.
- The polished wafer surface quality directly affects epitaxial layer quality. Any surface contamination disrupts growth, causing stacking faults, hillocks, or polycrystalline deposits. The RCA clean must be performed immediately before epitaxial growth.

### Cleanroom Requirements

Wafer processing after the final clean step must occur in a controlled environment where airborne particles are minimized. Even a single particle landing on a wafer between cleaning and photolithography can cause a device defect.

**Cleanroom classification** (ISO 14644-1):
- ISO Class 5 (formerly Class 100): < 3,520 particles per m³ ≥ 0.5 μm. Required for photolithography areas. Achieved by HEPA filtration (99.97% efficient at 0.3 μm) in laminar flow ceiling panels. Air changes: 200-600 per hour.
- ISO Class 6 (formerly Class 1,000): < 35,200 particles per m³ ≥ 0.5 μm. Suitable for wafer cleaning and etching areas.
- Personnel protocol: cleanroom garments (nylon-polyester woven coveralls, booties, hoods, gloves) that shed minimal particles. No cosmetics, no exposed skin below the neck. Air showers at entry locks blow particles off garments before entering the cleanroom.

### Key Deliverables

- Ingot preparation (cropping, grinding, orientation marking)
- Wafering by ID blade saw or wire saw with kerf management
- Double-sided lapping for flatness improvement
- Acid or alkaline etching for damage layer removal
- CMP polishing for mirror surface finish (sub-nanometer roughness)
- RCA cleaning sequence for contamination removal
- Wafer handling, edge finishing, and quality inspection
- Flatness, surface, and dimensional inspection methods
- Epitaxial wafer production considerations
- Ultra-pure water and cleanroom environment requirements

### Cross-References

- **Silicon crystal growth (ingot source)**: [crystal growth](crystal-growth.md)
- **Diamond abrasive tools**: [machine tools](../machine-tools/index.md)
- **Acids and bases for etching and cleaning**: [acids and bases](../chemistry/alkalis.md)
- **Ultra-pure water production**: [water treatment](../water/sem-tech-water-treatment.md)
- **Polishing pad and slurry chemistry**: [polymers](../polymers/index.md)

---

*Part of the [Bootciv Tech Tree](../index.md) · [Silicon](./index.md) · [All Domains](../index.md)*

[← Back to Silicon](index.md)
