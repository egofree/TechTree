# Wafering

> **Node ID**: silicon.wafering
> **Domain**: [Silicon](./index.md)
> **Dependencies**: [`silicon.crystal-growth`](crystal-growth.md)
> **Enables**: [`silicon.basic-devices`](basic-devices.md)
> **Timeline**: Years 45-60
> **Outputs**: silicon_wafers, polished_substrates, epitaxial_wafers
> **Critical**: Yes — polished wafers are the substrate for all semiconductor device fabrication


Wafering transforms a single-crystal silicon ingot (boule) into thin, flat, mirror-polished disks that serve as substrates for semiconductor device fabrication. The process is a sequence of mechanical and chemical material removal steps, each progressively finer, that transforms a rough-sawn slice into an atomically flat surface. A 300 mm wafer must be flat to within 2 μm over its entire surface (a ratio of 1:150,000, roughly equivalent to a 1 km road surface varying by 7 mm).

## Ingot Evaluation and Preparation

After CZ or FZ crystal growth, the ingot (150-300 mm diameter, 1-3 m long, 30-150 kg) must be evaluated and prepared to precise cylindrical geometry before wafering.

**Ingot inspection**:
- **Resistivity mapping**: Four-point probe measurements every 25-50 mm along the ingot length. Target: 1-50 Ω·cm for most CMOS applications (dopant concentration 10¹⁴-10¹⁶ atoms/cm³). Resistivity variation along the ingot should be <5% for premium wafers.
- **Oxygen content**: FTIR (Fourier transform infrared spectroscopy) measures interstitial oxygen (O_i) at 1107 cm⁻¹ absorption peak. CZ silicon contains 5-20 ppma oxygen (from dissolution of the SiO₂ crucible). Oxygen above 15 ppma can form SiO₂ precipitates during thermal processing (useful for internal gettering of metallic impurities, but excessive precipitation causes warpage).
- **Carbon content**: FTIR at 607 cm⁻¹, target <0.5 ppma (carbon nucleates defects).
- **Crystallographic orientation**: X-ray diffraction or Laue back-reflection to confirm <100> or <111> orientation within ±0.5° of the seed crystal axis.

**Cropping**:
- The seed end (crown) and tail are cut off with a diamond-bladed band saw (blade speed 1500-3000 m/min, feed rate 5-20 mm/min). These portions contain crystal defects (dislocations, inclusions, dopant concentration variations) from the seeding and termination of the crystal pull. Typically 50-100 mm is cropped from each end. The cropped pieces are not wasted — they are re-melted in the next crystal pull, recovering the high-purity silicon (electronic grade, >9N purity). Typical yield loss from cropping: 10-20% of ingot length.

**Grinding to diameter**:
- The boule is mounted between centers on a cylindrical grinder. A diamond grinding wheel (200-300 mm diameter, diamond grit 100-200 mesh in resin bond) machines the outer surface to the target diameter with ±0.1 mm tolerance.
- Standard diameters: 150 mm (6 inch), 200 mm (8 inch), 300 mm (12 inch). The grinding removes 0.5-3.0 mm from the boule's as-grown surface, which has surface damage, oxides, and slight ovality from the pulling process.
- Grinding parameters: infeed 0.01-0.05 mm per pass, wheel speed 1500-3000 RPM, workpiece speed 50-200 RPM. Coolant: deionized water, flooded over the grinding zone at 10-20 liters/min. Dry grinding generates silica dust and overheats the surface.

**Orientation flat or notch**:
- A flat or notch is ground along the length of the boule to indicate the crystal orientation to the wafer fabrication equipment. Crystal orientation determines how the silicon cleaves (breaks along crystal planes), which matters for dicing finished devices.
- For 150 and 200 mm wafers, a flat is ground: the primary flat indicates the {110} plane (for <100> oriented crystals), and a secondary flat (shorter, at a specific angle to the primary) identifies the dopant type (n-type or p-type) and crystal orientation.
- For 300 mm wafers, a single small notch (V-shaped groove, approximately 1 mm deep, ~60° included angle) replaces the flat. The notch takes less material and wastes less silicon. The notch is ground with a shaped diamond wheel in a single pass.

**Strengths**:
- Cropped seed/tail pieces are re-melted in the next crystal pull, recovering >9N purity silicon with zero waste
- Cylindrical grinding achieves ±0.1 mm diameter tolerance, sufficient for all downstream processing

**Weaknesses**:
- Cropping removes 10-20% of ingot length — significant yield loss before wafering even begins
- Diamond grinding wheel wear introduces contamination and requires periodic wheel dressing

## Wafering (Slicing)

Wafering cuts the cylindrical boule into thin slices (wafers). The two primary methods are inner-diameter (ID) blade sawing and wire sawing. Both are abrasive processes that remove a thin kerf of silicon between each wafer.

**[Inner-diameter (ID) blade saw](../glossary/inner-diameter-id-blade-saw.md)** (standard for 150 and 200 mm wafers):
- The ID saw uses a thin, flat steel blade with a circular hole in the center. The inner edge of the hole is plated with diamond abrasive particles (20-40 μm grain size in a nickel matrix). The blade is tensioned between a flanged collar that stretches it flat and rigid, like a drumhead.
- Blade dimensions: outer diameter 500-800 mm, inner hole (cutting edge) 150-250 mm, blade thickness 0.15-0.2 mm. The thin blade minimizes material loss (kerf). The blade tension must be precisely controlled (typically 30-50 N/mm of blade width) to prevent vibration and wandering.
- The ingot is mounted on a carriage that feeds horizontally into the spinning blade. The blade rotates at 1500-3000 RPM. Cut rate: 2-5 mm/min (a 200 mm wafer cut takes 40-100 minutes). Only one wafer is cut at a time.
- Kerf loss: 0.2-0.3 mm per wafer (the width of material turned into sawdust). For a 0.7 mm thick wafer, this means roughly 30% of the silicon is lost as kerf. A 1 m boule yields roughly 1000 wafers (each 0.7 mm) plus 200-300 mm of kerf waste.
- Coolant: water-soluble oil emulsion (5-10% concentration) or polyethylene glycol (PEG) solution, flooded over the cut zone at 5-15 liters/min to cool the blade, flush away silicon particles, and lubricate the cutting edge.

**[Wire saw](../glossary/wire-saw.md)** (standard for 300 mm wafers, gaining adoption for smaller diameters):
- A single continuous steel wire (0.08-0.18 mm diameter, high-carbon steel, tensile strength 3500-4500 MPa) is wound on grooved wire guides (pulley-like drums, 300-600 mm diameter) in a web of 200-800 parallel strands, spaced at the desired wafer thickness plus kerf (approximately 1.0-1.1 mm pitch for 300 mm wafers).
- The ingot is mounted on a holder and pressed down against the entire wire web simultaneously. As the wire reciprocates (oscillates back and forth at 5-15 m/s), an abrasive slurry cuts all wafers in parallel.
- Slurry composition: silicon carbide (SiC) particles, 8-25 μm grain size (300-600 grit), suspended in polyethylene glycol (PEG) carrier (viscosity 50-200 cP at 25°C). The slurry is pumped continuously over the wires at 10-30 liters/min. The abrasive particles, trapped between the wire and the silicon, grind a narrow kerf (100-180 μm wide) by three-body abrasion.
- Feed rate: 0.1-0.4 mm/min (slower per-wafer rate than ID saw, but all wafers cut simultaneously, so total throughput is much higher). A 300 mm diameter, 1 m long ingot cuts in 8-20 hours, producing all 800-900 wafers at once.
- Kerf loss: 0.12-0.18 mm per wafer (less than ID saw because the wire is thinner than the blade). Less silicon waste means more wafers per boule. Wire consumption: 20-50 km of wire per ingot (used once — the abrasive slurry degrades the wire surface).
- Slurry management: a 300 mm ingot wire cut consumes 50-100 liters of slurry. Used slurry (containing SiC particles mixed with fine silicon powder, ~50% SiC, ~50% Si by weight) can be filtered by centrifuge to separate SiC abrasive from silicon powder and depleted carrier, then remixed with fresh abrasive.

**Strengths**:
- Wire saw cuts all 800-900 wafers from a 300 mm ingot simultaneously in 8-20 hours — orders of magnitude higher total throughput than ID saw
- Wire kerf of 100-180 μm wastes ~30% less silicon per wafer than ID blade saw (200-300 μm kerf)

**Weaknesses**:
- Wire saw consumes 20-50 km of single-use steel wire per ingot — a significant consumable cost
- Slurry management (50-100 L per ingot, mixed SiC/Si waste) requires centrifuge recovery or disposal as industrial waste

## Wafer Handling

Freshly cut wafers are fragile, sharp-edged, and easily contaminated by dust, fingerprints, and organic films. Automated handling systems move wafers through the processing sequence without human contact.

**Vacuum pickup**:
- Wafers are picked up by a vacuum wand (a flat polyurethane or PEEK nozzle with a shallow vacuum cup, connected to a low-vacuum source, typically 30-50 kPa below atmospheric). The vacuum holds the wafer by its back side only; the front (device) side must never be touched by anything solid.
- Vacuum pickup requires a smooth back surface. Rough-sawn wafers may not seal well; lapping improves the surface enough for reliable vacuum handling.

**Cassette-to-cassette automation**:
- Wafers are stored in slotted plastic cassettes (25-wafer capacity for 200 mm, 13-wafer for 300 mm). The slots are precision-machined to hold wafers vertically without contacting the front surface. Robots transfer wafers from input cassette to processing station to output cassette.
- This standardizes handling, reduces contamination from human contact (skin oils, particles), and prevents breakage from manual handling errors.

**Edge grinding**:
- After slicing, wafer edges are sharp (90° corners from the saw cut). Sharp edges chip easily during handling and generate particles that contaminate cleanrooms. Edge grinding rounds the wafer perimeter to a controlled profile (typically a compound curve with radii of 0.3-1.0 mm) using a diamond grinding wheel (300-600 grit) on a CNC edge grinder.
- The edge profile is critical for later processing steps: photolithography spin-coating, etching, and deposition all depend on uniform edge geometry to avoid thickness buildup or thinning at the periphery.
- Material removal: 0.1-0.3 mm from the wafer diameter. After edge rounding, the wafer diameter is reduced to final specification (200.0 ±0.2 mm or 300.0 ±0.2 mm).

**Strengths**:
- Vacuum pickup handles wafers without contacting the front (device) surface, eliminating contamination
- Edge grinding prevents chipping during handling and reduces particle generation in cleanrooms

**Weaknesses**:
- Cassette-to-cassette automation requires precision robotics — significant capital cost for small-scale operations
- Edge grinding removes 0.1-0.3 mm from diameter, wasting silicon and requiring tight CNC control for consistent profiles

## Lapping

Sawn wafers have saw marks, waviness, and subsurface damage from the cutting process. Lapping removes bulk material and improves flatness using free abrasive slurry between two large flat plates.

**Double-sided lapping**:
- Wafers are placed in carriers (perforated brass or plastic plates, approximately 600-800 mm diameter) on a lapping machine with two large cast iron lapping plates (one above, one below, 800-1200 mm diameter). Abrasive slurry (aluminum oxide Al₂O₃, 5-15 μm grain size, in water or glycol carrier) is fed between the plates.
- The plates rotate in opposite directions, and the carriers orbit epicyclically (driven by a sun gear), ensuring uniform material removal from both wafer surfaces simultaneously. The random motion paths prevent directional scratch patterns.
- Material removal: 20-50 μm total (10-25 μm per side). This eliminates most saw damage and improves flatness to 2-5 μm total thickness variation (TTV) across a 200 mm wafer. Lapped wafer thickness: 725 ±10 μm (200 mm) or 925 ±10 μm (300 mm).
- Plate pressure: 10-30 kPa. Cycle time: 15-30 minutes per batch (typically 20-30 wafers per carrier for 200 mm, 10-15 for 300 mm).
- After lapping, wafers are cleaned thoroughly in an ultrasonic bath to remove all embedded abrasive particles. Any remaining Al₂O₃ particles on the wafer surface will cause scratches during the polishing step that follows.

**Strengths**:
- Double-sided lapping achieves 2-5 μm TTV across a 200 mm wafer — sufficient for most device fabrication
- Epicyclic carrier motion produces uniform, non-directional material removal with no preferential scratch pattern

**Weaknesses**:
- Al₂O₃ abrasive particles embed in the wafer surface and must be completely removed by ultrasonic cleaning before CMP
- Lapping removes only 20-50 μm — insufficient to eliminate deep saw damage, requiring etching as an intermediate step

## Etching

Lapping leaves a subsurface damage layer (microcracks and dislocations extending 5-15 μm deep from the mechanical grinding action). Etching removes this damaged layer chemically, exposing pristine single-crystal silicon underneath with no mechanical damage.

**Acid etching**:
- A mixture of nitric acid (HNO₃), hydrofluoric acid (HF), and acetic acid (CH₃COOH) in a typical ratio of 5:3:3 by volume (or 10:1 to 20:1 HNO₃:HF for the "chemical milling" step). The nitric acid oxidizes the silicon surface to SiO₂; the hydrofluoric acid dissolves the SiO₂ as fast as it forms. Acetic acid serves as a diluent and buffer that moderates the reaction rate. Net reaction: Si + 4HNO₃ + 6HF → H₂SiF₆ + 4NO₂ + 4H₂O.
- Material removal: 10-30 μm per side. Etch rate: 1-30 μm/min at room temperature depending on concentration and temperature. The etch is isotropic (removes material equally in all directions), which rounds sharp corners but produces a smooth, damage-free surface.
- Safety: HF is extremely hazardous. It penetrates skin rapidly (the fluoride ion is small and lipophilic), chelates calcium and magnesium in tissue, and causes deep, painful burns that may not become apparent for hours. Systemic fluoride poisoning can cause cardiac arrhythmia and death. Calcium gluconate gel (2.5-5%) must be immediately available as first aid for skin contact, applied generously to the affected area. Full acid-resistant PPE (face shield, heavy nitrile gloves over neoprene gloves, chemical apron, rubber boots) is mandatory when handling HF.

**[Alkaline etching](../glossary/alkaline-etching.md)** (alternative, safer):
- Sodium hydroxide (NaOH) or KOH solution, 10-40% by weight, heated to 60-90°C. Etch rate: 0.5-15 μm/min. The alkaline etch is anisotropic (etches different crystal planes at different rates: {100} planes etch ~30× faster than {111} planes), producing a textured surface.
- For <100> oriented silicon, the alkaline etch reveals pyramidal textures (4-10 μm feature size) across the entire surface. These pyramids reduce surface reflection from ~35% (polished silicon) to 10-15%, which is beneficial for photovoltaic applications (more light enters the cell).
- Advantage: no HF required. Much safer than acid etching. The textured surface is actually preferred for solar cells. Disadvantage: the textured surface is not suitable for integrated circuit fabrication, which requires a mirror-smooth surface.

**Strengths**:
- Acid etching removes 10-30 μm of subsurface damage in minutes, exposing pristine single-crystal silicon
- Alkaline etching produces pyramidal texture that reduces surface reflection from ~35% to 10-15% — ideal for solar cells without HF hazard

**Weaknesses**:
- HF-based acid mixtures are among the most dangerous chemicals in semiconductor manufacturing — systemic fluoride poisoning can cause cardiac arrest
- Isotropic acid etching rounds corners and undercuts features, limiting use for patterned substrates

## Polishing (CMP)

Chemical-mechanical polishing (CMP) produces the mirror-smooth surface required for photolithography. The wafer surface must be flat to within a few nanometers over the entire wafer area for modern lithography to resolve sub-micron features with sufficient depth of focus.

**CMP process**:
- Wafers are mounted face-down on polishing heads (carriers) that press them against a rotating polyurethane polishing pad (typically 600-800 mm diameter, 1-2 mm thick closed-cell polyurethane on a felt or compressed foam sub-pad). A colloidal silica slurry (SiO₂ particles, 20-80 nm diameter, 10-30% solids, suspended in NaOH or KOH solution at pH 10-11) is dispensed onto the pad surface at 100-300 mL/min.
- The alkaline slurry softens the topmost atomic layers of silicon (forms a thin hydrated SiO₂ layer), and the silica particles mechanically remove this softened layer by abrasion. The combined chemical and mechanical action removes material at 0.1-2.0 μm/min.
- Material removal: 5-30 μm total. Final surface roughness: < 0.5 nm Ra (arithmetic mean roughness), typically 0.1-0.3 nm RMS for prime-grade wafers. The surface appears mirror-smooth to the naked eye and reflects a clear image like a glass mirror.
- Polishing pressure: 20-40 kPa (2-5 psi). Platen speed: 30-80 RPM. Carrier speed: 20-60 RPM (counter-rotating to platen for uniform removal). Slurry flow: 100-300 ml/min per polishing head.
- Pad conditioning: a diamond-embedded disk (200-300 grit diamond in nickel bond, 150-200 mm diameter) is pressed against the pad surface periodically (every 30-60 seconds during polishing) to regenerate its texture. Without conditioning, the pad glazes (surface pores compress closed) and removal rate drops by 50-80% over 30 minutes.

**[Double-sided polishing](../glossary/double-sided-polishing.md)** (for 300 mm wafers):
- Both sides polished simultaneously on a double-side polishing machine. The wafer floats between two polishing platens (upper and lower) in a carrier with oversized windows. Upper platen clockwise, lower counter-clockwise. This produces wafers with identical surface quality on both sides and eliminates the "mirror-perfect front / hazy back" asymmetry of single-side polished (SSP) wafers.
- DSP wafers have superior flatness (TTV < 2 μm for 300 mm) because the double-sided process is inherently self-correcting for thickness variation. Local flatness (site flatness, measured over a 25 × 25 mm area): < 0.1 μm. This level of flatness is necessary for deep-UV lithography with depth-of-focus budgets of ±50 nm. Most 300 mm prime wafers are DSP.
- Nanotopography: <5 nm over 2 × 2 mm area (the "waviness" at intermediate spatial frequencies — affects gate oxide uniformity).

**Strengths**:
- CMP achieves <0.5 nm Ra surface roughness — mirror-smooth, required for sub-micron lithography depth of focus
- Double-sided polishing achieves TTV <2 μm for 300 mm wafers with site flatness <0.1 μm over 25 × 25 mm

**Weaknesses**:
- Colloidal silica slurry (pH 10-11) is a chemical burn hazard and environmental disposal challenge
- Pad conditioning every 30-60 seconds is required — without it, removal rate drops 50-80% in 30 minutes

## Cleaning (RCA Clean)

After polishing, wafers carry residues of polishing slurry, organic contaminants (skin oils, airborne organics), metal ions (Fe, Cu, Ni from processing equipment), and particles (silica, pad debris). The RCA clean (developed by Werner Kern at RCA Laboratories in 1965) is the standard sequence for removing all contaminants without damaging the pristine silicon surface.

**SC-1 (Standard Clean 1)**: removes organic contaminants and particles.
- Solution: NH₄OH:H₂O₂:H₂O = 1:1:5 by volume at 75-85°C. Soak time: 10-20 minutes.
- The hydrogen peroxide (H₂O₂) oxidizes organic matter to CO₂ and water. The ammonium hydroxide (NH₄OH) provides alkalinity (pH ~10) that keeps the silicon surface and silica particles negatively charged through the entire process, preventing particles from re-depositing on the wafer surface by electrostatic repulsion (both the wafer and the particles have the same negative charge).
- Removes particles down to 0.1 μm and cleans organic films from the surface. Also removes some metallic contaminants (Au, Ag, Cu) by complexation with ammonia.
- After SC-1, wafers are rinsed in ultra-pure water (18.2 MΩ·cm resistivity, < 1 particle/mL > 0.1 μm, total organic carbon < 50 ppb) for 5-10 minutes in an overflow rinse tank.

**SC-2 (Standard Clean 2)**: removes metallic contaminants.
- Solution: HCl:H₂O₂:H₂O = 1:1:6 by volume at 75-85°C. Soak time: 10-20 minutes.
- Hydrochloric acid dissolves metal oxides and hydroxides, forming soluble metal chloride complexes (FeCl₃, CuCl₂, NiCl₂) that remain in solution and are rinsed away. The H₂O₂ keeps the silicon surface oxidized and passivated during cleaning.
- Removes alkali metals (Na, K), alkaline earth metals (Ca, Mg), and heavy metals (Fe, Ni, Cr, Cu, Zn) to surface concentrations below 10¹⁰ atoms/cm² (roughly one metal atom per 10,000 surface silicon atoms). Metal contamination at higher levels degrades gate oxide integrity and minority carrier lifetime.
- After SC-2, a final rinse in ultra-pure water and spin-dry (3000-5000 RPM, nitrogen blow) produces a clean, dry wafer ready for further processing.

**[Hydrofluoric acid dip](../glossary/hydrofluoric-acid-dip.md)** (optional, removes oxide):
- A brief dip (15-60 seconds) in dilute HF (1-5% by weight) removes the native oxide layer (SiO₂, ~1-2 nm thick) that grows naturally on silicon in air at room temperature. The HF etches SiO₂ selectively (etch rate ~100 nm/min for thermal oxide at 5% HF) but does not attack silicon.
- After HF dip, the surface is hydrogen-terminated (Si-H bonds instead of Si-O). The hydrogen-terminated surface is hydrophobic (water beads off) and passivated against re-oxidation for several hours in cleanroom air.
- The HF dip is used when the next processing step requires direct contact with the silicon surface (epitaxial growth, gate oxide formation, metal deposition). If the wafer is being stored or shipped, the native oxide is left in place as a protective layer.

**Drying methods**:
- **Spin rinse dryer**: wafers are spun at 3000-5000 RPM while rinsed with ultra-pure water, then blown dry with filtered hot nitrogen (60-80°C). Centrifugal force removes water from the surface. Fast (3-5 minutes per batch) but can generate particles from water droplets hitting the wafer surface at high speed.
- **[Marangoni drying](../glossary/marangoni-drying.md)** (for critical applications): the wafer is slowly withdrawn from a water bath at 1-5 mm/s while a thin layer of isopropyl alcohol (IPA) vapor is introduced at the water surface. The surface tension gradient between the IPA-rich meniscus and the pure water below (the Marangoni effect) pulls water off the wafer surface as it withdraws, leaving a dry, particle-free surface without mechanical force. Superior to spin drying for wafers with fragile microstructures.

**Strengths**:
- SC-1/SC-2 sequence removes particles to 0.1 μm and metals to <10¹⁰ atoms/cm² — the industry standard for 60+ years
- Marangoni drying leaves zero water marks or particle adders, critical for sub-100 nm device fabrication

**Weaknesses**:
- RCA clean uses three hazardous chemicals (NH₄OH, H₂O₂, HCl) at 75-85°C — requires dedicated ventilation and PPE
- HF dip produces hydrophobic surface that re-contaminates within hours, requiring immediate downstream processing

## Wafer Cleaning Technology

**Ultrapure water (UPW) production**: Wafer cleaning requires water of extreme purity: resistivity 18.2 MΩ·cm (theoretical maximum for pure water at 25°C), total organic carbon (TOC) <1 ppb, particles <1/mL at ≥0.05 μm, dissolved oxygen <10 ppb, silica <1 ppb, metals <10 ppt (parts per trillion) each. UPW production system: municipal water → multimedia filter (5-20 μm) → activated carbon (removes chlorine and organics) → water softener (removes Ca²⁺, Mg²⁺) → reverse osmosis (RO, 95-99% rejection of dissolved ions at 10-20 bar, produces 70-80% permeate) → electrodeionization (EDI, continuous ion exchange + electrodialysis, polishing to <0.1 μS/cm) → mixed-bed ion exchange (final polishing to 18.2 MΩ·cm) → UV sterilization (254 nm, kills bacteria and breaks down TOC) → ultrafiltration (0.01 μm membrane, final particle removal) → distribution loop (continuous recirculation at 2-5 m/s velocity through PVDF or PFA piping, maintained at 20-25°C). UPW consumption: 5-20 L per wafer processed (a fab processing 50,000 wafers/month consumes 5,000-30,000 m³/day of UPW).

**Megasonic cleaning**: Conventional ultrasonic cleaning (20-40 kHz) is too aggressive for patterned wafers — cavitation bubbles (1-50 μm) collapse with sufficient force to damage delicate structures (metal lines, low-k dielectrics). Megasonic cleaning (800-2000 kHz) uses much smaller cavitation bubbles (0.1-1.0 μm) that provide gentle but effective particle removal from submicron features. A megasonic transducer (lead zirconate titanate, PZT, piezoelectric ceramic, 50-150 mm diameter) is mounted on the backside of a quartz tank filled with cleaning solution (dilute SC-1 at 50-60°C). Acoustic power density: 5-20 W/cm². Particle removal efficiency: >95% for 0.1-1.0 μm particles, <1% feature damage rate. Used after CMP and before gate oxidation.

**Single-wafer spin cleaning**: Modern 300 mm fabs use single-wafer spin cleaners rather than batch immersion tanks (better particle control, less chemical consumption). The wafer spins at 300-1000 RPM on a vacuum chuck while nozzles dispense cleaning solutions (alternating SC-1, DI water rinse, DHF, DI water rinse, SC-2, final DI water rinse and N₂ spin-dry). Chemical flow: 50-200 mL/min per nozzle. Cycle time: 60-180 seconds per wafer. Particle adders: <2 particles ≥0.09 μm per wafer per clean cycle. Chemical consumption: 30-80% less than batch cleaning.

**Strengths**:
- Megasonic cleaning (800-2000 kHz) removes >95% of 0.1-1.0 μm particles with <1% feature damage — safe for patterned wafers
- Single-wafer spin cleaning uses 30-80% less chemical than batch immersion while adding <2 particles per cycle

**Weaknesses**:
- UPW production requires multi-stage purification (RO, EDI, UV, UF) consuming 5,000-30,000 m³/day for a large fab
- UPW quality spec of <10 ppt metals demands continuous monitoring and frequent membrane replacement

## Epitaxial Wafer Production

Many IC fabrication processes require an epitaxial layer: a thin (1-100 μm) single-crystal silicon layer grown on top of the polished wafer substrate by chemical vapor deposition (CVD). The epitaxial ("epi") layer has precisely controlled doping (type, concentration, and profile) independent of the substrate. This decoupling allows, for example, a lightly doped (high resistivity) epi layer on a heavily doped (low resistivity) substrate — the standard configuration for CMOS logic wafers (p/p+ or n/n+), where the substrate provides low resistance for backside contact and the epi layer provides the high-quality device region.

**CVD epitaxy process**:
- Load polished wafers into a horizontal or vertical epitaxial reactor (batch: 10-50 wafers per run, or single-wafer for 300 mm). Heat to 1050-1200°C in hydrogen atmosphere (H₂ carrier gas at 30-100 L/min, atmospheric pressure or reduced pressure at 50-200 Torr). Etch the wafer surface with HCl gas (1-5% in H₂, 2-5 minutes at 1150°C) to remove any residual native oxide and subsurface damage — HCl etches silicon at ~1-3 μm/min at this temperature, removing 2-10 μm. Then introduce silicon source gas: trichlorosilane (SiHCl₃, TCS) at 0.1-1.0% in H₂, or silane (SiH₄) at 0.01-0.1% in H₂. Silicon deposits on the hot wafer surface, growing a single-crystal layer that replicates the substrate crystal structure.
- Growth rate: TCS at 1100°C: 0.5-2.0 μm/min. Silane at 900°C: 0.1-0.5 μm/min (lower temperature, but higher defect density if temperature is too low — "haze" from polycrystalline nucleation).
- Doping: add phosphine (PH₃) for n-type epi or diborane (B₂H₆) for p-type epi, at 0.01-100 ppm in the gas stream. Dopant concentration in the epi layer is proportional to the dopant gas partial pressure (Henry's law). Typical epi layer thickness: 2-20 μm for CMOS, 50-100 μm for power devices. Epi layer resistivity uniformity: ±5-10% across the wafer, ±5% wafer-to-wafer within a batch.
- The polished wafer surface quality directly affects epitaxial layer quality. Any surface contamination disrupts growth, causing stacking faults, hillocks, or polycrystalline deposits. The RCA clean must be performed immediately before epitaxial growth.

**Strengths**:
- Epi layer doping is decoupled from substrate — enables p/p+ and n/n+ CMOS configurations with independently optimized resistivity
- CVD epitaxy at 0.5-2.0 μm/min provides ±5-10% resistivity uniformity across the wafer

**Weaknesses**:
- Autodoping tail extends 0.5-3.0 μm into the epi layer from substrate dopant evaporation at 1050-1200°C
- Silane and phosphine/diborane dopant gases are pyrophoric and extremely toxic — requiring gas cabinets with continuous exhaust

**Autodoping control**: Dopant atoms from the heavily doped substrate evaporate during the high-temperature epi process and incorporate into the growing epi layer, causing a transition region at the substrate-epi interface where the doping level gradually changes from substrate to epi concentration. This "autodoping tail" extends 0.5-3.0 μm into the epi layer. Minimize by: (1) Using reduced pressure (50-150 Torr) — lower pressure increases the mean free path and sweeps evaporated dopant away from the surface faster. (2) Growing a thin undoped "buffer" layer first (0.5-1.0 μm), then growing the doped epi layer on top. (3) Using lower growth temperature (950-1050°C instead of 1100-1200°C) — reduces dopant evaporation from the substrate but also reduces growth rate.

## SOI (Silicon-on-Insulator) Wafers

**SIMOX (Separation by IMplanted Oxygen)**: Implant oxygen ions (O⁺) at 150-200 keV into a standard silicon wafer at a dose of 1-2 × 10¹⁸ O⁺/cm². The oxygen is implanted at a depth of 100-300 nm below the surface. Anneal at 1300-1350°C for 4-6 hours in argon + 0.5% O₂. The implanted oxygen reacts with silicon to form a continuous buried SiO₂ layer (the "BOX" — Buried OXide, 100-400 nm thick). The silicon above the BOX is the device layer (50-200 nm thick). SIMOX produces a uniform, high-quality BOX but the high-dose implant causes crystal damage in the device layer that requires careful annealing. Implantation cost: $200-500 per wafer (200 mm).

**Bonded SOI**: Thermally oxidize a "handle" wafer (0.5-2.0 μm SiO₂) and a "device" wafer. Clean both wafers in RCA chemistry. Bring the two oxide surfaces into contact at room temperature — van der Waals forces bond the wafers instantly (spontaneous bonding when surfaces are atomically clean and flat, roughness <0.5 nm RMS). Anneal at 800-1100°C for 1-4 hours to convert the weak van der Waals bonds to strong Si-O-Si covalent bonds (bond strength >10 MPa, approaching bulk silica fracture strength). Then thin the device wafer from the backside: coarse grind to within 10-20 μm of target, then CMP to final device layer thickness (10 nm to 100 μm depending on application). Bonded SOI produces thicker, more uniform BOX layers than SIMOX (up to 5 μm BOX), with lower defect density in the device layer.

**Smart Cut process**: The most commercially important SOI wafer production method (developed by LETI/Soitec). Start with a "donor" wafer. Implant hydrogen ions (H⁺) at 50-200 keV through the thermal oxide to a dose of 2-8 × 10¹⁶ H⁺/cm². The hydrogen creates a "smart cut" plane at the implant depth (50-500 nm below the surface). Bond the donor wafer (hydrogen-implanted) to a handle wafer (with or without oxide). Anneal at 400-600°C — hydrogen gas bubbles form at the implant plane, exerting pressure that causes the donor wafer to split along the hydrogen-rich plane, transferring a thin silicon layer onto the handle wafer. The result: a SOI wafer with a device layer of precisely controlled thickness (equal to the hydrogen implant depth). The remaining donor wafer is reclaimed, repolished, and reused (95%+ material utilization). Smart Cut SOI wafer production capacity: >5 million wafers/year (2023).

**Strengths**:
- Smart Cut achieves 95%+ donor wafer material utilization — the remaining wafer is reclaimed and reused
- Bonded SOI produces BOX layers up to 5 μm thick with lower defect density than SIMOX implantation

**Weaknesses**:
- SIMOX requires high-dose O⁺ implantation ($200-500 per wafer) causing crystal damage requiring careful annealing
- Van der Waals bonding requires atomically flat surfaces (roughness <0.5 nm RMS) — any particle prevents bonding

## Wafer Thickness and Thinning

**Standard thicknesses**: 150 mm wafers: 625 μm. 200 mm wafers: 725 μm. 300 mm wafers: 775 μm. These thicknesses are set by mechanical handling requirements (a 300 mm wafer at 775 μm thick sags only 50-100 μm under gravity — thin enough to sag uncontrollably would jam in automated wafer handlers). The wafer must be thick enough to resist fracture during handling, thermal cycling (warpage from CTE mismatch between the wafer and deposited films), and vacuum chucking (100-500 mbar suction on the backside for lithography and process tools).

**Backgrinding (wafer thinning)**: For power devices, MEMS, and 3D packaging, wafers are thinned from the backside after front-end processing. Mechanical backgrinding: coarse grind with 400-600 grit diamond wheel (removal rate 5-20 μm/min) to within 20-50 μm of target thickness, then fine grind with 2000-4000 grit (removal rate 0.5-2.0 μm/min) to final thickness +5 μm, then CMP polish (removes 3-5 μm of grinding damage). Minimum achievable thickness by mechanical grinding: 50-100 μm for 200 mm, 75-150 μm for 300 mm (thinner wafers fracture under the grinding load). For extreme thinning (<50 μm): use wet chemical etching (TMAH 25% at 80°C, etch rate 10-30 μm/hour) or atmospheric downstream plasma (ADP) etching (etch rate 5-20 μm/min). Ultra-thin wafers (25-50 μm) are handled on tape frames or temporary bonded to carrier wafers during thinning and subsequent processing.

**Stress relief after grinding**: Mechanical grinding leaves subsurface damage (micro-cracks, residual compressive stress in a 1-5 μm surface layer). If not removed, these cracks propagate during subsequent thermal processing, causing wafer fracture. CMP removes 3-10 μm from the ground surface to eliminate all subsurface damage. Dry etch (SF₆/O₂ plasma, 5-20 μm removal) is an alternative for stress relief — plasma etching is isotropic and damage-free. The combination of coarse grinding → fine grinding → CMP or dry etch produces a thin, flat, stress-free wafer ready for backside processing.

**Strengths**:
- Coarse grinding removes 5-20 μm/min, enabling rapid thinning from 775 μm to 100 μm in under 2 hours
- CMP or plasma etch stress relief eliminates subsurface micro-cracks that would propagate during thermal processing

**Weaknesses**:
- Minimum mechanical grinding thickness of 50-100 μm (200 mm) — thinner wafers fracture under grinding load
- Ultra-thin wafers (<50 μm) require temporary bonding to carrier wafers, adding process complexity

## Gettering

**Purpose**: Metallic impurities (Fe, Cu, Ni, Au) dissolved in silicon create deep-level traps that reduce minority carrier lifetime (from >1000 μs in ultra-pure silicon to <1 μs with 10¹²-10¹³ atoms/cm³ of Fe). Gettering captures these impurities at benign locations away from the active device region (the front surface where transistors are built).

**Intrinsic gettering**: CZ silicon containing 8-15 ppma interstitial oxygen can be heat-treated to precipitate SiO₂ particles inside the wafer bulk (not at the surface). Process: (1) High-low-high cycle: 1100°C for 4-16 hours (dissolves any existing nuclei and out-diffuses oxygen from a 10-30 μm surface "denuded zone"), then 650-750°C for 4-32 hours (nucleates oxygen precipitates in the bulk), then 1000°C for 4-16 hours (grows the precipitates to 50-200 nm). The SiO₂ precipitates act as gettering sites — they attract metallic impurities away from the surface denuded zone. Effective for Fe, Ni, Cu (reduces surface metal concentration by 10-100×). The denuded zone (10-30 μm from each surface) remains precipitate-free and provides a clean region for device fabrication.

**Extrinsic gettering**: Create intentional damage or stress on the wafer backside to attract impurities. Methods: (1) Mechanical back-damage: sandblast or scratch the wafer backside (roughness Ra 0.5-5.0 μm) — the damaged region gettering sites are active at temperatures above 800°C. (2) Phosphorus diffusion gettering: diffuse phosphorus into the backside at 900-1000°C from a POCl₃ source — P-Si pairs form and trap metallic impurities. (3) Polysilicon backside: deposit 1-3 μm of polysilicon on the wafer backside — the grain boundaries getter metals. (4) Argon ion implantation: implant Ar⁺ at 100-200 keV into the backside — the implant damage creates gettering sites. All methods work by creating high-energy sites (dislocations, grain boundaries, or precipitates) that are thermodynamically favorable for metallic impurity segregation.

**Strengths**:
- Intrinsic gettering reduces surface metal concentration by 10-100× using only oxygen already present in CZ silicon
- Extrinsic gettering methods (mechanical back-damage, polysilicon deposition) are simple and compatible with standard fab processes

**Weaknesses**:
- Intrinsic gettering requires CZ silicon with 8-15 ppma oxygen — FZ silicon lacks sufficient oxygen for precipitate formation
- Phosphorus diffusion gettering adds a high-temperature processing step (900-1000°C) that may affect thermal budgets

## Wafer Reclaim

**Purpose**: Test wafers (used for equipment qualification, process development, and monitor wafers) can be reclaimed (stripped of all deposited films and polished) and reused 3-10 times before the wafer becomes too thin for handling. Reclaim saves 50-70% compared to buying new prime wafers.

**Reclaim process**: (1) Strip all films: wet etch or plasma etch to remove photoresist, oxides, nitrides, metals, and polysilicon. Sequential stripping: O₂ plasma ash for resist → HF (5%) for oxide → H₃PO₄ at 160°C for Si₃N₄ → HCl:H₂O₂:H₂O for metals. (2) Surface inspection: verify all films removed, measure residual particles and defects. (3) Light CMP polish: remove 3-10 μm from the wafer surface to eliminate any embedded particles or subsurface damage from previous processing. (4) Final clean and inspection to prime wafer specifications. Reclaim yield: 85-95% per cycle (5-15% loss from breakage, excessive thinning, or unrecoverable defects). A 300 mm prime wafer costs $30-80 new. A reclaimed 300 mm wafer costs $10-25.

**Strengths**:
- Reclaim saves 50-70% vs. new prime wafers — test/monitor wafers reused 3-10 times before retirement
- 85-95% reclaim yield per cycle makes economics attractive for high-volume fabs using thousands of test wafers/month

**Weaknesses**:
- Each reclaim cycle removes 3-10 μm, eventually making the wafer too thin for handling after 3-10 cycles
- Sequential stripping (plasma → HF → H₃PO₄ → HCl) is a multi-step chemical process requiring dedicated equipment

## Wafer Quality Metrics

**Oxygen precipitation**: CZ-grown silicon contains 5-20 ppma interstitial oxygen (from dissolution of the SiO₂ crucible during crystal growth). During wafer processing at 900-1200°C, oxygen can precipitate as SiO₂ particles (50-500 nm) in the wafer bulk. These precipitates are beneficial for intrinsic gettering but harmful if they form in the device active region (within 10-30 μm of the front surface). Oxygen precipitation is controlled by: (1) Adjusting initial oxygen content (target 12-16 ppma for balanced gettering). (2) Thermal history of the wafer (rapid thermal processing at >1000°C dissolves precipitates; slow cooling through 650-800°C nucleates them). (3) Denuded zone formation (high-temperature out-diffusion step at 1100°C depletes oxygen from the surface region).

**Metallic contamination limits**: Maximum acceptable surface metal concentrations on prime wafers (measured by TXRF — Total Reflection X-ray Fluorescence, or VPD-ICPMS): Fe <5 × 10⁹ atoms/cm², Cu <5 × 10⁹, Ni <5 × 10⁹, Al <1 × 10¹⁰, Na <1 × 10¹⁰, Cr <1 × 10¹⁰, Zn <1 × 10¹⁰. At the front-end process line (gate oxidation), limits are 10-100× stricter (<10⁸ atoms/cm² for Fe, Cu, Ni). Iron is the most problematic contaminant: Fe interstitials act as deep-level recombination centers (energy level Ev + 0.39 eV), reducing minority carrier lifetime from >1000 μs to <10 μs at 10¹² cm⁻³ Fe concentration.

**Particle specifications**: Prime wafer particle limits (per SEMI M1): 200 mm wafers: ≤10 particles ≥0.12 μm LPD per wafer. 300 mm wafers: ≤30 particles ≥0.09 μm LPD per wafer. Particles are measured by laser surface scanning (darkfield or brightfield). Each process step adds 5-50 particles per wafer on average — a 30-step CMOS process can accumulate 500-1500 particles per wafer. Particle kill ratio: approximately 10-30% of particles ≥0.5 μm that land on active device areas cause yield-limiting defects.

**Strengths**:
- TXRF and VPD-ICPMS measure surface metals down to 10⁹ atoms/cm² — sensitive enough for gate oxide quality control
- Laser surface scanning detects particles down to 0.09 μm with full-wafer mapping for yield prediction

**Weaknesses**:
- Each process step adds 5-50 particles — a 30-step CMOS flow accumulates 500-1500 particles even in ISO Class 5 cleanrooms
- Iron contamination at just 10¹² cm⁻³ reduces minority carrier lifetime from >1000 μs to <10 μs

## Wafer Inspection and Quality Control

Every wafer must be inspected after each major processing step. Defective wafers caught early save the expense of further processing on a part that will ultimately fail.

**Flatness measurement**:
- A capacitive probe or laser interferometer (Fizeau interferometer) scans the wafer surface and maps thickness variation at 10,000-100,000 points. TTV (total thickness variation) is the difference between the thickest and thinnest points. Report: site flatness (SFQR — maximum front surface deviation within a fixed site area), global flatness (GBIR — maximum deviation over the entire wafer). For advanced nodes (<100 nm): SFQR <0.10 μm over 25 × 8 mm site, GBIR <3 μm over 300 mm wafer.

**Surface inspection**:
- **Laser scattering**: a laser beam scans the wafer surface at oblique incidence. Particles, scratches, and pits scatter light detected by photomultiplier tubes. Sensitivity: detects particles down to 0.1 μm on polished wafers. Mapping resolution: 0.1-1.0 μm minimum detectable defect size. Each wafer is mapped with defect locations (x,y coordinates) for yield prediction. Rejection criteria: >10 LPDs ≥0.16 μm on 200 mm, >30 LPDs ≥0.12 μm on 300 mm.
- **Brightfield/darkfield microscopy**: manual or automated microscope inspection at 100-500× magnification. Used to classify defect types (particle, scratch, pit, haze, crystal-originated particles/COPs — octahedral voids 50-200 nm formed during crystal growth by vacancy aggregation).

**Strengths**:
- Fizeau interferometer maps thickness at 10,000-100,000 points — detects site flatness deviations <0.10 μm over 25 × 8 mm sites
- Laser scattering detects particles down to 0.1 μm with x,y coordinate mapping for yield correlation

**Weaknesses**:
- Full-surface optical inspection at 0.1 μm sensitivity processes only 5-20 wafers/hour — throughput bottleneck for high-volume fabs
- COPs (crystal-originated particles, 50-200 nm voids) are intrinsic to CZ growth and cannot be eliminated by wafer processing

## Wafer-Level Metrology

**Film thickness measurement**: Ellipsometry measures the change in polarization of reflected light (Ψ and Δ angles) at 150-800 nm wavelength to determine thin film thickness (1 nm to 10 μm) and refractive index. Spectroscopic ellipsometry (SE) scans 200-800 nm wavelengths, fitting the data to an optical model of the film stack. Accuracy: ±0.1 nm for SiO₂ films >10 nm thick. For ultra-thin gate oxides (1-3 nm), X-ray reflectometry (XRR) provides better accuracy (±0.02 nm for films 1-50 nm).

**Dopant profiling**: Secondary Ion Mass Spectrometry (SIMS): sputter the wafer surface with a focused Cs⁺ or O₂⁺ ion beam (1-10 keV) and analyze the ejected secondary ions by mass spectrometry. Depth resolution: 1-5 nm per decade of concentration. Detection limits: B, P, As in Si: 10¹⁴-10¹⁶ atoms/cm³. Spreading Resistance Profiling (SRP): press two tungsten carbide probe tips (1-5 μm radius) onto a beveled wafer surface and measure local resistivity. Depth resolution: 5-20 nm. Used to verify implant dose and junction depth after annealing.

**Defect inspection**: Brightfield inspection (broadband light, minimum detectable defect 50-100 nm), darkfield inspection (low-angle illumination, more sensitive to particles and bumps), and electron beam inspection (3-10 nm resolution, very slow — used for sample inspection). Throughput: 5-20 wafers per hour for full-surface optical inspection at 0.1 μm sensitivity.

**Strengths**:
- Spectroscopic ellipsometry measures film thickness to ±0.1 nm for SiO₂ >10 nm — non-destructive, fast, and repeatable
- SIMS achieves 10¹⁴-10¹⁶ atoms/cm³ detection limits for B, P, As with 1-5 nm depth resolution for junction profiling

**Weaknesses**:
- SIMS is destructive (sputters the wafer surface) and slow — not suitable for in-line production monitoring
- Electron beam inspection at 3-10 nm resolution is too slow for full-wafer scans, limited to sample defect review

## Wafer Handling and Automation

**FOUP (Front-Opening Unified Pod)**: Standard wafer carrier for 300 mm wafers (SEMI E62 standard). Holds 25 wafers in a sealed, nitrogen-purged enclosure with a front-opening door (interfacing with tool load ports). Material: polycarbonate or PEEK shell, carbon-filled for ESD protection (surface resistivity 10⁵-10⁹ Ω/sq). Internal environment: <1% O₂, <1% RH (nitrogen purge prevents native oxide growth). Wafer pitch: 10 mm. FOUP weight with 25 × 300 mm wafers: ~8 kg. FOUP cost: $300-800 each. An automated 300 mm fab has 5,000-20,000 FOUPs in circulation. See [Cleanrooms](../photolithography/cleanrooms.md).

**SMIF (Standard Mechanical InterFace)**: The 200 mm equivalent — a sealed pod (SEMI E19) that mates with a load port on the process tool. The tool opens the pod door mechanically, maintaining the clean environment inside. SMIF pods hold 25 × 200 mm wafers. Each SMIF pod is opened 30-60 times during a typical CMOS process flow. Pod integrity: <1 particle ≥0.12 μm added per open-close cycle.

**Wafer orientation in cassette**: Wafers are loaded into the cassette with the notch (or flat) pointing toward the cassette hinge pin (SEMI standard orientation). The notch must be at a specific angular position (bottom-center for notch wafers, or the flat faces the cassette back for flat wafers). The cassette slots are tapered to prevent wafer edge contact with the cassette walls.

**Strengths**:
- FOUP nitrogen purge maintains <1% O₂ and <1% RH, preventing native oxide growth during wafer storage and transport
- SMIF pods add <1 particle ≥0.12 μm per open-close cycle — minimal contamination during 30-60 openings per process flow

**Weaknesses**:
- A 300 mm fab requires 5,000-20,000 FOUPs at $300-800 each — $1.5-16M in wafer carrier inventory alone
- FOUPs at 8 kg each pose repetitive strain injury risk for operators handling overhead load ports

## Thermal Processing of Wafers

**Rapid Thermal Processing (RTP)**: Heat a single wafer to 600-1200°C in seconds (ramp rate 50-250°C/s) using an array of halogen lamps (1-2 kW each, 20-200 lamps per system, total power 50-300 kW) above and below the wafer. Temperature measurement: pyrometer (optical, 4-5 μm wavelength, ±1-3°C accuracy) or thermocouple (type K or S). Uniformity: ±2-5°C across 300 mm wafer at 1000°C (controlled by lamp zone power adjustment — 4-10 independently controlled zones). Process applications: (1) Implant anneal: activate dopants at 950-1100°C for 10-30 seconds. (2) Gate oxidation: grow 1-5 nm SiO₂ gate oxide at 800-1000°C for 5-60 seconds. (3) Silicide formation: react deposited metal (Ti, Co, Ni) with silicon at 500-800°C.

**Furnace processing (batch)**: Horizontal or vertical tube furnace processes 25-200 wafers simultaneously in a quartz or silicon carbide tube (150-350 mm diameter, 1.5-3.0 m long). Heating elements (SiC or MoSi₂) in 3-5 independently controlled zones maintain temperature uniformity of ±0.5-1.0°C at 600-1200°C. Ramp rate: 5-20°C/min. Process gases: N₂ (inert), O₂ (oxidation), H₂ (reducing), Ar (inert diluent), HCl (cleaning — volatilizes metallic contaminants). Applications: field oxidation (300-1000 nm SiO₂ in wet O₂ for 2-8 hours), gate oxidation (5-50 nm SiO₂ in dry O₂ for 30-120 minutes), LPCVD deposition (Si₃N₄, polysilicon, SiO₂). Throughput: 10-50 wafers/hour depending on process time.

**Strengths**:
- RTP achieves 50-250°C/s ramp rate — fast enough to activate dopants without excessive diffusion (thermal budget control)
- Batch furnace processes 25-200 wafers simultaneously at ±0.5-1.0°C uniformity — high throughput for oxidation and CVD

**Weaknesses**:
- RTP lamp arrays consume 50-300 kW per system — enormous peak power demand
- Furnace ramp rate limited to 5-20°C/min, requiring long cycle times (2-8 hours for thick oxide growth)

## Wafer Specifications Summary

| Parameter | 150 mm (6") | 200 mm (8") | 300 mm (12") |
|-----------|-------------|-------------|--------------|
| Diameter tolerance | ±0.3 mm | ±0.2 mm | ±0.2 mm |
| Thickness | 625 ±15 μm | 725 ±10 μm | 775 ±10 μm |
| TTV max | < 5 μm | < 3 μm | < 2 μm |
| Bow max | < 30 μm | < 15 μm | < 10 μm |
| Warp max | < 40 μm | < 20 μm | < 12 μm |
| Surface roughness (RMS) | < 0.5 nm | < 0.3 nm | < 0.2 nm |
| Particles max | 20 (≥0.16 μm) | 10 (≥0.12 μm) | 50 (≥0.09 μm) |
| Orientation flat/notch | flat | flat | notch |
| Crystal orientation | <100> or <111> ±0.5° | <100> or <111> ±0.5° | <100> ±0.5° |
| Weight per wafer | ~27 g | ~53 g | ~128 g |
| Typical price | $8-15 | $10-25 | $30-80 |

## Wafer Sort and Die Preparation

**Wafer sort (probe test)**: Before dicing, each die on the wafer is electrically tested by probing the bond pads with a probe card (100-10,000 fine tungsten or beryllium-copper needles, each 25-50 μm tip diameter, contacting aluminum bond pads 50-100 μm square). The prober steps across the wafer in a serpentine pattern, testing each die in 0.1-5.0 seconds. Tests include: DC parametric (leakage currents, threshold voltages, breakdown voltages), functional (basic logic or memory operation at low speed), and yield mapping (pass/fail map of the entire wafer — a 300 mm wafer with 10 mm × 10 mm die contains ~700 die; typical yield 70-95%). Failed die are inked or electronically mapped for exclusion during packaging. Wafer sort throughput: 5-20 wafers per hour per prober.

**Dicing (wafer → die)**: Mount the wafer face-up on dicing tape (UV-curable adhesive on a stainless steel or plastic ring frame). Dice with a diamond-impregnated resin-bond blade (20-35 μm thick, rotating at 30,000-60,000 RPM). Blade feed rate: 1-10 mm/s. Cut depth: through the wafer plus 20-50 μm into the tape. Kerf width: 25-40 μm. Street width (space between adjacent die reserved for dicing): 50-150 μm. Alternative: laser dicing (nanosecond or picosecond laser at 355-1064 nm, ablates silicon at 0.1-1.0 mm/s) — narrower kerf (2-5 μm), no mechanical damage, but slower and more expensive.

**Die attach and wire bonding**: After dicing, individual die are picked from the expanded tape by a die bonder (vacuum collet, 5-20 mN pickup force, placement accuracy ±25-50 μm) and bonded to a leadframe or package substrate with die attach adhesive (silver-filled epoxy, thermal conductivity 1-5 W/(m·K), cured at 150-180°C for 30-120 minutes; or eutectic Au-Si solder for high-power devices). Wire bonding connects each die pad to the corresponding package lead with 25 μm gold wire (ball bonding: thermosonic at 200-250°C, 50-150 mN force, 60-120 kHz ultrasonic energy for 10-30 ms). A typical IC has 50-500 wire bonds, each taking 30-100 ms. Wire bond pull strength: >40 mN (25 μm Au wire). See [Electronics Assembly](../electronics/assembly.md).

**Known good die (KGD)**: For multi-chip modules and system-in-package (SiP) applications, bare die must be fully tested to the same quality level as packaged parts. KGD testing includes: full-speed functional test at the wafer level (requires high-speed probe cards with 10+ GHz bandwidth), burn-in at 125-150°C under bias for 24-168 hours, and hot/cold test at -40°C to +125°C. KGD cost premium: 20-50% over standard die. Without KGD, assembly yield of multi-chip modules degrades multiplicatively — a 4-chip module with 95% good die each has only 81.5% module yield; with KGD at 99.5% confidence, module yield improves to 98.0%.

**Die yield economics**: For a 300 mm wafer costing $50-80, containing ~700 die of 10 × 10 mm each at 80% yield, the cost per known-good die is ~$0.089 — the wafer is the cheapest part of semiconductor manufacturing. The subsequent processing (30-50 process steps) adds $200-1000 per wafer. This is why semiconductor manufacturing is fundamentally a yield business: a 10% yield improvement (80% → 90%) on a $1000 wafer saves ~$125 per wafer in effective die cost, worth $12.5 million per year on a 100,000 wafers/month fab.

**Strengths**:
- Wafer sort identifies failed die before packaging, avoiding $5-50 waste per die on parts that would fail anyway
- Diamond blade dicing at 30,000-60,000 RPM produces 25-40 μm kerf — narrow enough to preserve die area

**Weaknesses**:
- Probe card contact (25-50 μm tips on 50-100 μm pads) damages bond pads — limits probe iterations
- KGD testing adds 20-50% cost premium, but essential for multi-chip modules where yields multiply

## Cost Structure of Wafer Production

**Capital equipment costs** (300 mm prime wafer production line, 100,000 wafers/month capacity): Wire saws ($500K-1.5M each, 5-10 units), lapping machines ($300K-800K each, 3-5 units), CMP polishers ($400K-1M each, 5-10 units), cleaning systems ($300K-1M each, 3-5 units), inspection tools ($500K-2M each, 5-10 units), cleanroom facility ($5K-15K per m², 2000-5000 m² Class 10-100). Total capital investment: $50-200 million. Depreciation: 5-7 years straight-line.

**Operating costs per wafer** (300 mm prime, approximate breakdown): Polysilicon feedstock: $5-10. Crystal growth: $5-10. Wafering (wire saw, slurry, waste): $5-15. Lapping and CMP (abrasives, pads, chemicals): $5-15. Cleaning (chemicals, UPW): $2-5. Inspection and metrology: $2-5. Cleanroom overhead: $5-15. Labor: $3-8. Overhead and depreciation: $10-25. Total: $42-108 per 300 mm prime wafer (selling price: $30-80 for commodity, $80-200+ for epi or specialty).

**Strengths**:
- Polysilicon feedstock at $5-10/wafer is a small fraction of total cost — wafer value is in processing, not raw material
- 5-7 year depreciation on $50-200M capital gives $10-25/wafer at 100K wafers/month — manageable unit economics

**Weaknesses**:
- Total capital investment of $50-200M for a 100K wafers/month line — enormous upfront commitment
- CMP consumables (slurry, pads) at $5-15/wafer are the single largest variable cost after silicon

## Wafer Shipping and Storage

**Nitrogen-purged packaging**: Each 300 mm wafer is placed in an individual slot of a 25-wafer FOUP or wafer shipper (SEMI E57 standard). The shipper is sealed with two nested bags — inner bag (ESD-safe polyethylene, heat-sealed) and outer bag (polyethylene, also heat-sealed). Between the bags, a desiccant packet (silica gel, 5-10 g) absorbs residual moisture. The inner bag is purged with nitrogen (99.999% purity, <5 ppm O₂, <5 ppm H₂O) before sealing — the inert atmosphere prevents native oxide growth (bare silicon grows ~0.1-0.2 nm/day of SiO₂ in clean, dry air; in nitrogen, <0.02 nm/day). Shipping box: corrugated cardboard with foam cushioning (15-30 g/cm² shock absorption rated for 1.5 m drop). Shelf life: 12-24 months in original sealed packaging at 20-25°C, 40-60% RH. After opening, wafers should be used within 24-72 hours.

**Edge exclusion**: Wafer specifications define an "edge exclusion zone" — a ring 2-5 mm from the wafer edge where device fabrication is not performed. For a 300 mm wafer with 3 mm edge exclusion, the usable area is 67,929 mm² out of 70,686 mm² total — a 3.9% loss. For 200 mm with 3 mm edge exclusion: 29,557 mm² out of 31,416 mm² — a 5.9% loss. Smaller wafers lose proportionally more area to edge exclusion, one of the economic drivers for migrating to larger wafer diameters.

**Strengths**:
- Nitrogen-purged packaging limits oxide growth to <0.02 nm/day — wafers remain usable for 12-24 months in sealed packaging
- Double-bag sealing with desiccant and N₂ purge protects wafers during shipping without refrigeration

**Weaknesses**:
- After opening, wafers must be used within 24-72 hours — tight scheduling requirement for fab operations
- Edge exclusion wastes 3.9-5.9% of wafer area depending on diameter, incentivizing migration to larger wafers

## Cleanroom Requirements

Wafer processing after the final clean step must occur in a controlled environment where airborne particles are minimized. Even a single particle landing on a wafer between cleaning and photolithography can cause a device defect.

**Cleanroom classification** (ISO 14644-1):
- ISO Class 5 (formerly Class 100): < 3,520 particles per m³ ≥ 0.5 μm. Required for photolithography areas. Achieved by HEPA filtration (99.97% efficient at 0.3 μm) in laminar flow ceiling panels. Air changes: 200-600 per hour.
- ISO Class 6 (formerly Class 1,000): < 35,200 particles per m³ ≥ 0.5 μm. Suitable for wafer cleaning and etching areas.
- Personnel protocol: cleanroom garments (nylon-polyester woven coveralls, booties, hoods, gloves) that shed minimal particles. No cosmetics, no exposed skin below the neck. Air showers at entry locks blow particles off garments before entering the cleanroom.

## Safety & Hazards

Wafering involves mechanical cutting, chemical etching, and polishing with hazardous materials. Each process stage has distinct risks.

**Wire saw and ID blade saw**:
- The wire saw's continuous steel wire (0.08-0.18 mm) runs at 5-15 m/s under high tension (20-40 N per strand). Wire breakage sends a lash of steel wire across the work area. **Enclose the wire saw** with interlocked guards that stop the machine when opened. Never reach into the wire web while the machine is running.
- Silicon ingots weigh 30-150 kg. Use mechanical lifting aids (overhead crane, vacuum lift) for ingot loading.
- Wire consumption produces 20-50 km of used wire per ingot — spent wire is sharp and contaminated, must be collected in sealed containers.
- ID blade saws spin at 1500-3000 RPM with a diamond-edged cutting surface. Eye protection required — silicon fragments eject from the cut zone.
- Noise levels: 80-95 dB during sawing. Hearing protection (earplugs or earmuffs, NRR 25+) required for extended operation.

**Silicon dust and slurry hazards**:
- Wire sawing generates fine silicon powder (1-20 μm) mixed with SiC abrasive in the slurry. Silicon dust is a respiratory irritant and chronic inhalation risk (silicosis). Wear N95 or P100 respirators when handling dry silicon waste or changing slurry. Slurry recycling areas require local exhaust ventilation.
- Lapping slurry (Al₂O₃ or SiC in water/glycol) is a mechanical irritant to skin and eyes. The glycol carrier is slippery on floors — clean spills immediately to prevent falls.
- CMP slurry is alkaline (pH 10-11, KOH or NaOH) and causes chemical burns with prolonged skin contact. The colloidal silica particles (20-80 nm) are too fine to feel on the skin but can cause eye irritation. Wear chemical splash goggles and nitrile gloves when handling CMP slurry.

**Chemical etching**:
- The HNO₃/HF/CH₃COOH acid mixture is extremely hazardous. HF penetrates skin rapidly, chelates calcium and magnesium in tissue, and causes deep burns that may not become apparent for hours. Systemic fluoride poisoning can cause cardiac arrhythmia and death. **Calcium gluconate gel (2.5-5%) must be immediately available** as first aid for skin contact, applied generously to the affected area. Full acid-resistant PPE (face shield, heavy nitrile gloves over neoprene gloves, chemical apron, rubber boots) is mandatory.
- Nitric acid (HNO₃) produces toxic NO₂ gas during the etch reaction. Perform acid etching only in a fume hood or ventilated wet bench with a minimum face velocity of 0.5 m/s (100 fpm). NO₂ exposure causes delayed pulmonary edema — symptoms may not appear for 4-12 hours. NO₂ exposure limit: 5 ppm TWA (OSHA PEL).
- Alkaline etching (NaOH or KOH at 60-90°C) is less immediately dangerous than HF but causes severe thermal and chemical burns. Hot caustic splashes are a significant risk — use face shields and chemical-resistant aprons.

**RCA cleaning**:
- SC-1 (NH₄OH/H₂O₂/H₂O at 75°C): ammonium hydroxide fumes are irritating to eyes and respiratory tract. Hydrogen peroxide is a strong oxidizer — never mix with organic solvents. The hot solution can splash — wear face shield and chemical-resistant gloves.
- SC-2 (HCl/H₂O₂/H₂O at 75°C): hydrochloric acid fumes are corrosive to respiratory tract and metal equipment. Ventilation required.
- Dilute HF dips (1-5%): even dilute HF is hazardous. The same calcium gluconate and PPE protocols apply as for concentrated HF.

**High-temperature processing (epitaxy, RTP, furnace)**:
- Epitaxial reactors operate at 1050-1200°C. External surfaces can reach 60-150°C — thermal burn hazard. Interlocked guards prevent access to hot zones. Allow cool-down time before maintenance.
- **Hydrogen gas**: Epitaxy uses H₂ carrier gas at 30-100 L/min. Hydrogen is flammable at 4-75% concentration in air and ignites with very low energy (0.017 mJ). Leak detection: hydrogen sensors in the exhaust and room air, set to alarm at 1% (25% of LEL). Emergency shutdown: automatic hydrogen supply shutoff on alarm.
- **Silane (SiH₄) and trichlorosilane (SiHCl₃)**: Silicon source gases for epitaxy. Silane is pyrophoric — spontaneously ignites on contact with air at concentrations above ~2%. Trichlorosilane is flammable and releases HCl on contact with moisture. Gas cabinets with inert gas purge, automatic shutoff valves, and dedicated exhaust lines are mandatory.
- **Dopant gases**: Phosphine (PH₃) and diborane (B₂H₆) are extremely toxic (TLV 50 ppb for PH₃, 100 ppb for B₂H₆) and pyrophoric. Used in trace amounts (ppm level) but cylinder changes and line leaks pose fatal exposure risk. Gas cabinets must be continuously exhausted, with automatic cylinder valve closure on detection of any leak.
- RTP lamps produce intense infrared radiation. Do not view lamp operation directly — use filtered viewing ports or camera systems.

**Mechanical hazards**:
- Automated wafer handling robots (cassette-to-cassette transfer) have pinch points and crushing hazards. Never reach into the robot work envelope during operation. Interlocked access doors should be standard.
- Lapping machines have heavy platens (50-200 kg) rotating at 20-60 RPM. Hands or clothing caught between the platens causes severe crush injuries.
- Diamond grinding wheels rotate at 1500-5000 RPM. Safety glasses with side shields are mandatory.
- CMP polishing platens rotate at 30-80 RPM with significant mass (50-200 kg). Pinch hazards between the carrier head and platen surface. Pad conditioning disks are diamond-impregnated and abrasive — handle with gloves.
- FOUPs with 25 × 300 mm wafers weigh ~8 kg. Operators handling FOUPs repeatedly risk repetitive strain injuries. Use ergonomic FOUP lift assists for overhead load ports.

**General PPE requirements** for wafering operations:
- Safety glasses with side shields at all times (face shield when handling chemicals)
- Nitrile gloves (chemical handling) or leather work gloves (mechanical operations)
- Hearing protection (sawing, grinding, lapping operations)
- Lab coat or chemical-resistant apron
- Closed-toe shoes with slip-resistant soles (glycol spills on floors)

## Key Deliverables

- Ingot evaluation, preparation, cropping, grinding, and orientation marking
- Wafering by ID blade saw or wire saw with kerf management
- Edge rounding and wafer handling automation
- Double-sided lapping for flatness improvement
- Acid or alkaline etching for damage layer removal
- CMP polishing for mirror surface finish (sub-nanometer roughness)
- Double-side polishing (DSP) for 300 mm wafers
- RCA cleaning sequence for contamination removal
- Advanced cleaning (megasonic, single-wafer spin, UPW production)
- Epitaxial wafer production with autodoping control
- SOI wafer production (SIMOX, bonded SOI, Smart Cut)
- Wafer thinning (backgrinding) and stress relief
- Gettering (intrinsic and extrinsic)
- Wafer reclaim for test/monitor wafers
- Flatness, surface, and dimensional inspection methods
- Wafer-level metrology (film thickness, dopant profiling, defect inspection)
- Wafer sort, dicing, die attach, and yield economics
- Thermal processing (RTP and furnace)
- FOUP/SMIF handling and cleanroom environment requirements
- Wafer shipping, storage, and packaging

## Cross-References

- **Silicon crystal growth (ingot source)**: [crystal growth](crystal-growth.md)
- **CZ crystal pulling equipment**: [CZ Pulling](cz-pulling.md)
- **Silicon purification (feedstock)**: [purification](purification.md)
- **Diamond abrasive tools**: [machine tools](../machine-tools/index.md)
- **Acids and bases for etching and cleaning**: [acids and bases](../chemistry/alkalis.md)
- **Ultra-pure water production**: [water treatment](../water/sem-tech-water-treatment.md)
- **Polishing pad and slurry chemistry**: [polymers](../polymers/index.md)
- **Photolithography (wafer flatness requirements)**: [lithography](../vlsi-scaling/lithography.md)
- **CMP equipment and slurries**: [advanced processes](../vlsi-scaling/advanced-processes.md)
- **Cleanroom design**: [cleanrooms](../photolithography/cleanrooms.md)
- **Electronics assembly (die attach, wire bonding)**: [assembly](../electronics/assembly.md)


## See Also

- [Crystal Growth](crystal-growth.md) — single-crystal ingot production
- [Basic Devices](basic-devices.md) — device fabrication from wafers
- [Czochralski Pulling](cz-pulling.md) — CZ ingot pulling process
- [Purification](purification.md) — polysilicon purification upstream
- [MG-Si Production](mg-si-production.md) — metallurgical-grade silicon feedstock
- [Precision Metrology](../measurement/precision-metrology.md) — wafer flatness measurement

[← Back to Silicon](index.md)
