# Electrochemical Surface Processes

> **Node ID**: electrochemistry.electrochemical-processes
> **Domain**: [Electrochemistry & Plating](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-80
> **Outputs**: electropolished_surfaces, electroformed_parts, electroless_nickel, ENIG_surfaces, electroless_copper
> **Critical**: Yes — electropolishing produces ultra-low-outgassing vacuum chamber surfaces; ENIG is the dominant PCB surface finish with no practical alternative

### Overview

This capability covers three electrochemical surface processes that are critical to semiconductor manufacturing and advanced engineering: electropolishing (controlled anodic dissolution for ultrasmooth surfaces), electroforming (building precision metal structures by electrodeposition onto a mandrel), and electroless plating (autocatalytic metal deposition without external current). Unlike the processes covered in [Electroplating](electroplating.md) (which deposits metal from an external source onto a cathode), these processes either dissolve material from the workpiece surface (electropolishing), build freestanding metal parts (electroforming), or deposit metal by chemical reduction without applied current (electroless plating).

For semiconductor manufacturing, electropolishing produces the ultra-smooth, chromium-enriched surfaces required for process chamber interiors (surface roughness Ra <0.1 μm, outgassing rate <10⁻¹⁰ Torr·L/s·cm²). Electroforming creates precision stampers for optical disc mastering and microfluidic device molds with sub-micron feature replication. Electroless nickel immersion gold (ENIG) is the dominant surface finish for PCBs, providing a flat, solderable, wire-bondable surface for BGA and QFP packages.

### Electropolishing

Electropolishing is the reverse of electroplating — the workpiece is the anode (not the cathode), and material is selectively dissolved from the surface. The process preferentially removes microscopic peaks and asperities (where current density is highest), producing a smooth, bright, defect-free surface. The result is simultaneously the smoothest surface finish achievable by any method and a chromium-enriched passive layer (for stainless steel).

**Process principle**:
- In electroplating: Cu²⁺ + 2e⁻ → Cu (reduction at cathode, metal deposits)
- In electropolishing: Cu → Cu²⁺ + 2e⁻ (oxidation at anode, metal dissolves)
- The key is the "polishing" mechanism: a viscous anodic film (concentrated metal salt + electrolyte) forms on the workpiece surface. This film is thicker at microscopic peaks (shorter diffusion path to bulk electrolyte) and thinner in valleys. The higher current density at peaks causes faster dissolution, leveling the surface. The process is self-limiting — once the surface is smooth, the anodic film thickness becomes uniform and dissolution rate equalizes across the surface.

**Stainless steel electropolishing** (most common application):
- **Electrolyte**: Concentrated mixture of phosphoric acid (H₃PO₄, 50-70% by volume) and sulfuric acid (H₂SO₄, 15-30% by volume) in water. Some formulations add glycerin (5-15%) as a viscous additive that stabilizes the anodic film. Specific gravity: 1.70-1.78.
- **Temperature**: 50-70°C. Higher temperature reduces viscosity and increases dissolution rate. Must be maintained ±2°C for uniform results.
- **Current density**: 10-40 mA/cm² (100-400 A/ft²). Lower current density produces finer finish; higher current density increases removal rate but may cause pitting or orange-peel texture.
- **Voltage**: 6-18 V DC (varies with electrolyte, temperature, and workpiece geometry). Constant current mode preferred for production.
- **Time**: 2-20 minutes depending on desired material removal (5-40 μm typical). Removal rate: approximately 1-3 μm/minute at 20 mA/cm².
- **Cathode**: Copper or lead plates. Inert — not consumed. Cathode-to-anode area ratio ≥3:1.
- **Agitation**: Mechanical stirring or electrolyte recirculation to maintain uniform temperature and concentration. Air agitation not used (would disrupt the anodic film).

**Surface quality achieved**:
- Surface roughness: Ra 0.05-0.2 μm from a starting Ra of 0.5-2.0 μm (mechanical polishing). Electropolishing improves Ra by 50-80%.
- Chromium enrichment: The electropolishing electrolyte preferentially dissolves iron and nickel from austenitic stainless steel, leaving a surface enriched in chromium. The surface Cr/Fe ratio increases from ~0.25 (bulk) to 1.5-3.0 (surface). This chromium-rich surface spontaneously forms a Cr₂O₃ passive film with superior corrosion resistance to mechanically polished surfaces.
- Outgassing: Electropolished surfaces have 10-100× lower outgassing rates than mechanically polished surfaces because the smooth surface has fewer adsorption sites for water vapor and atmospheric gases. Critical for vacuum chambers: electropolished 316L stainless steel achieves outgassing rates of ~10⁻¹⁰ Torr·L/s·cm² after 24-hour bake-out at 150°C.

**Semiconductor process chamber applications**:
- Etch chamber internals (aluminum with electropolished and anodized surfaces): 6061-T6 aluminum body, Type III hard anodized interior (400-600 HV), then electropolished to Ra <0.5 μm. The electropolished anodized surface is chemically inert (resists Cl₂, HBr, NF₃ plasmas) and has low particle generation.
- CVD chamber components: Electropolished 316L stainless steel or Inconel 625 for gas distribution manifolds, susceptor supports, and showerhead plates. Surface roughness Ra <0.25 μm prevents film buildup and particle generation.
- Vacuum fittings: CF (ConFlat) flanges with electropolished knife-edge sealing surfaces. The electropolished surface ensures reliable metal-to-metal sealing with copper gaskets at pressures below 10⁻¹¹ Torr.

### Electroforming

Electroforming builds freestanding metal parts by electrodepositing a thick metal layer onto a precisely machined mandrel (pattern master), then separating the deposited metal from the mandrel. The deposited metal replicates the mandrel surface with sub-micron fidelity — features on the mandrel are reproduced as negative impressions in the electroform.

**Nickel electroforming** (most common):
- **Mandrel materials**: Stainless steel (passivated surface for easy separation), aluminum (dissolved in NaOH after plating), wax or plastic (low-melting-point, melted out), or nickel (passivated with chromate film for separation). For precision optical surfaces, the mandrel is diamond-turned to Ra <5 nm.
- **Bath**: Sulfamate nickel (Ni(NH₂SO₃)₂, 300-450 g/L) + NiCl₂·6H₂O (5-15 g/L) + H₃BO₃ (30-45 g/L). Temperature 50-60°C, pH 3.5-4.5. See [Electroplating](electroplating.md) for sulfamate bath details.
- **Current density**: 10-50 mA/cm². Lower current density produces lower internal stress and finer grain structure.
- **Deposit thickness**: 50 μm to several mm. Growth rate: 10-25 μm/hour at 20 mA/cm².
- **Internal stress control**: Critical for electroforming. Stress causes distortion (curling, warping) upon mandrel separation. Sulfamate bath: 20-50 MPa tensile at standard conditions. Stress reducers (saccharin, 0.5-2 g/L) shift stress toward compressive. Zero-stress deposits achievable by balancing bath chemistry, current density, and stress reducer concentration. Measured by deposit stress analyzer (spiral contractometer or bent strip method).
- **Hardness**: 200-450 HV depending on bath chemistry. Sulfamate nickel: 200-300 HV as-deposited. Hardened by co-deposition of sulfur (from saccharin additive): up to 500 HV.

**Applications**:
- **Optical disc stampers** (CD, DVD, Blu-ray): Nickel electroforms (300 μm thick) replicated from photoresist-patterned glass masters. Blu-ray pit width: 130 nm, depth: 25 nm — the electroform must replicate these features with <5 nm deviation. Stamper lifetime: 30,000-100,000 discs before wear.
- **Micro-molding inserts**: Electroformed nickel inserts for injection molding of microfluidic devices, optical diffusers, and micro-lens arrays. Feature replication: sub-micron fidelity.
- **Precision bellows and diaphragms**: Thin-wall (50-200 μm) nickel bellows for pressure sensors, flexible seals, and expansion joints. Electroforming produces uniform wall thickness on complex geometries impossible to achieve by machining.
- **Rocket engine thrust chambers**: Electroformed nickel or copper alloy channels for regenerative cooling passages. Channel width: 0.5-2 mm, depth: 2-5 mm. The electroform reproduces the mandrel channels with zero draft angle (impossible by conventional casting).

**Copper electroforming** (for printed circuits and microstructures):
- **Bath**: Acid copper sulfate (CuSO₄ 60-80 g/L + H₂SO₄ 50-75 g/L) with organic additives for grain refinement.
- **Current density**: 15-30 mA/cm².
- **Applications**: High-density interconnect (HDI) PCB microvias, micro-coils for MEMS inductors, X-ray mask membranes (2-5 μm thick, >90% X-ray transparent).

### Electroless Plating

Electroless plating deposits metal from solution by autocatalytic chemical reduction — no external current is applied. The reducing agent (typically sodium hypophosphite for nickel, formaldehyde or glyoxylic acid for copper) reduces metal ions on the catalyzed surface. The deposit itself catalyzes further deposition, making the process self-sustaining once initiated. The key advantage is perfectly uniform coating thickness on all surfaces — no current distribution issues, no shielding, no anode placement constraints.

**Electroless nickel-phosphorus (Ni-P)**:
- **Bath composition**:
  - Nickel sulfate (NiSO₄·6H₂O): 20-30 g/L (provides Ni²⁺)
  - Sodium hypophosphite (NaH₂PO₂·H₂O): 20-30 g/L (reducing agent — reduces Ni²⁺ to Ni⁰, and itself oxidizes to phosphite PO₃³⁻)
  - Complexing agents: Lactic acid (20-30 g/L), glycolic acid (10-20 g/L), or citrate (10-20 g/L). Complex the Ni²⁺ ions to prevent spontaneous decomposition (the bath would plate out nickel on all surfaces including the tank walls without complexing agents). Also buffer the pH.
  - Stabilizers: Thiourea (1-5 mg/L), lead acetate (1-3 mg/L), or iodate (10-50 mg/L). Prevent spontaneous bath decomposition at ppm levels. Too much stabilizer slows or stops deposition.
- **Operating conditions**: Temperature 85-95°C, pH 4.5-5.0 (adjusted with NH₄OH or H₂SO₄). Deposition rate: 10-25 μm/hour.
- **Phosphorus content**: Controlled by pH and hypophosphite ratio.
  - Low-P (1-4% P): pH 5.0-5.5, harder, more crystalline. Magnetic. Used for wear resistance.
  - Mid-P (5-8% P): pH 4.5-5.0. Most common. Balanced properties.
  - High-P (9-13% P): pH 4.0-4.5. Amorphous (non-crystalline). Non-magnetic. Best corrosion resistance (no grain boundaries for corrosive attack). Used for disk drive platters and semiconductor packaging.
- **Hardness**: 500-700 HV as-plated. Heat treatment at 400°C for 1 hour precipitates Ni₃P particles, raising hardness to 900-1100 HV (comparable to hard chrome). This precipitation hardening mechanism is unique to electroless nickel.
- **Uniformity**: ±2-5 μm on complex geometries (±1-2% of nominal thickness). On a threaded fastener, the coating thickness on the thread crest, root, and flank varies by <5%. This is the supreme advantage over electroplating.
- **Bath life**: 3-8 metal turnovers (one turnover = all nickel initially in bath has been deposited and replenished). Bath is eventually discarded due to phosphite (Na₂HPO₃) accumulation — phosphite is a reaction byproduct that cannot be decomposed and eventually causes spontaneous bath decomposition.

**Electroless nickel immersion gold (ENIG)**:
ENIG is the dominant surface finish for printed circuit boards, providing a flat, solderable, and wire-bondable surface. It is a two-step process:

1. **Electroless nickel** (barrier layer): Deposit 3-8 μm of electroless nickel (mid-P, 7-9% P) directly on the copper pad. The nickel serves as a diffusion barrier, preventing copper from migrating into the solder joint (which would embrittle the joint). Deposition: 15-20 minutes at 85°C.
2. **Immersion gold** (protective layer): Immerse the nickel-coated board in a gold bath (KAu(CN)₂, 1-3 g/L Au, pH 4.0-5.0, citrate buffer, 80-90°C). Gold displaces nickel from the surface by galvanic exchange: 2Au⁺ + Ni⁰ → 2Au⁰ + Ni²⁺. The gold deposits as a thin (0.03-0.08 μm) flash coating that protects the nickel from oxidation. The process is self-limiting — when all exposed nickel is covered, the reaction stops (no more nickel available for displacement). Time: 8-15 minutes.

**ENIG quality issues**:
- **Black pad** (nickel corrosion): The most critical defect. If the nickel layer is over-attacked by the gold immersion solution, a brittle, phosphorus-rich layer forms at the nickel-gold interface. During soldering, this layer cracks, causing joint failure. Prevention: control nickel phosphorus content (7-9% P optimal), limit immersion gold time, and use mild gold bath chemistry.
- **Gold thickness**: Too thin (<0.03 μm) provides insufficient nickel protection. Too thick (>0.08 μm) wastes expensive gold and increases black pad risk due to longer immersion time.

**Electroless copper** (for PCB through-hole metallization):
- **Bath**: CuSO₄ (5-15 g/L Cu) + formaldehyde (HCHO, 5-15 g/L, reducing agent) + EDTA or tartrate (complexing agent) + NaOH to pH 12-13.
- **Temperature**: 25-45°C. Deposition rate: 1-5 μm/hour (slower than electroless nickel).
- **Surface preparation** (critical for non-conductors): The dielectric substrate (FR-4 epoxy-glass) must be catalytically activated before electroless copper will deposit. Sequence: (1) Etch in chromic acid or permanganate to create micro-roughness for mechanical adhesion. (2) Sensitize in SnCl₂ solution (adsorbs Sn²⁺ ions). (3) Activate in PdCl₂ solution (Sn²⁺ reduces Pd²⁺ to Pd⁰, creating palladium catalytic nuclei on the surface). (4) Immerse in electroless copper bath — copper deposits autocatalytically on the palladium nuclei.
- **Thickness**: Initial electroless copper deposit: 0.5-2 μm. This thin conductive layer is then thickened by electrolytic copper plating (electroplating) to 20-35 μm. The combination of electroless (for adhesion and coverage) + electrolytic (for thickness and speed) is the standard through-hole metallization process.

### Process Integration in Semiconductor Manufacturing

**ENIG for BGA substrate fabrication**:
- BGA (ball grid array) substrates use ENIG on copper pads for solder ball attachment. Nickel thickness: 5-8 μm. Gold thickness: 0.03-0.05 μm. The flat ENIG surface ensures reliable solder ball placement and reflow.
- Flip-chip substrates may use electroless nickel palladium immersion gold (ENEPIG) for improved wire bondability: EN (5 μm) + EPd (0.05-0.15 μm, electroless palladium) + IG (0.03 μm). The palladium interlayer prevents black pad and improves gold wire bond reliability.

**Electropolished process chambers**:
- Aluminum etch chambers: 6061-T6 body → precision machine → Type III hard anodize → electropolish → clean. Surface roughness: Ra <0.5 μm after electropolishing. Particle generation rate: <10 particles/m²/hour at 0.1 μm sensitivity.
- Stainless steel vacuum chambers: 316L body → precision machine → internal weld → electropolish → clean → vacuum bake (150°C, 24 hours). Outgassing rate after bake: <10⁻¹⁰ Torr·L/s·cm².

**Electroforming for microstructures**:
- LIGA (Lithographie, Galvanoformung, Abformung) process: X-ray lithography creates high-aspect-ratio PMMA resist molds (height: 100-1000 μm, aspect ratio up to 100:1). Nickel is electroformed into the mold, then the PMMA is dissolved, leaving freestanding nickel microstructures. Applications: micro-gears, micro-springs, micro-fluidic channels, and X-ray opaque masks for semiconductor lithography.

### Bath Management and Waste Treatment

**Electroless bath maintenance**:
- Nickel concentration: Replenish as depleted (monitored by colorimetric analysis or atomic absorption). Typical consumption: 5-10 g/L per hour of operation.
- Hypophosphite concentration: Replenished in proportion to nickel (molar ratio NaH₂PO₂:Ni ≈ 0.3-0.5). Both are consumed by the deposition reaction.
- pH: Continuously monitored and adjusted with NH₄OH or H₂SO₄. pH drift affects deposition rate and phosphorus content.
- Phosphite accumulation: The primary bath life limiter. Phosphite (H₂PO₃⁻) is a stable reaction byproduct. When phosphite reaches 80-120 g/L (after 3-8 turnovers), the bath must be replaced. Waste treatment: precipitate nickel with NaOH (pH 10-11), filter the Ni(OH)₂ sludge for hazardous waste disposal.

**Waste treatment**:
- **Rinse water**: Contains trace nickel, copper, gold, and organic additives. Treatment: ion exchange (chelating resin for heavy metal removal) followed by activated carbon (organic removal). Treated water recycled to rinse tanks.
- **Spent baths**: Acidic nickel or copper solutions with high metal content. Treatment: neutralize with NaOH to pH 9-11, precipitate metal hydroxides, filter sludge. Recover metals from sludge by acid leaching and electrowinning where economically justified.
- **Cyanide-containing waste** (from gold baths): Cyanide destruction by alkaline chlorination (NaOCl at pH 10-11: CN⁻ → OCN⁻ → CO₂ + N₂) or hydrogen peroxide oxidation. Must be performed before acidification to prevent HCN gas evolution.

### Electropolishing of Different Metals

**Aluminum electropolishing**:
- Electrolyte: Perchloric acid (HClO₄, 5-20%) in ethanol or acetic acid. **Extremely dangerous** — perchloric acid is a powerful oxidizer and forms explosive mixtures with organic solvents. Must be performed in a dedicated fume hood with wash-down capability. Temperature: <25°C (water-cooled cell). Voltage: 15-30V. Current density: 10-30 mA/cm².
- Alternative (safer): Phosphoric acid (H₃PO₄, 50-70%) + sulfuric acid (H₂SO₄, 15-25%) + chromic acid (CrO₃, 3-8%). Temperature: 70-85°C. Voltage: 10-25V. This is the "commercial" aluminum electropolish bath (Battelle formulation). Chromic acid provides the oxidizing power needed for aluminum.
- Result: Mirror-bright surface on aluminum alloys. Used for decorative reflectors, optical components, and precursor to anodizing (electropolished surfaces anodize more uniformly).

**Titanium electropolishing**:
- Electrolyte: Perchloric acid (HClO₄, 5-10%) in acetic acid, or sulfuric acid + hydrofluoric acid mixture. Temperature: <20°C. Voltage: 20-40V. Current density: 20-50 mA/cm².
- Result: Smooth, oxide-rich surface. Used for medical implant surfaces (improves biocompatibility and fatigue resistance by removing machining scratches that act as stress concentrators).

**Copper electropolishing**:
- Electrolyte: Phosphoric acid (H₃PO₄, 50-70%) in water. Temperature: 20-30°C. Voltage: 1.5-2.5V. Current density: 10-30 mA/cm². The low voltage reflects copper's low anodic dissolution potential.
- Application: Smoothing copper foil for PCB laminates, and polishing copper alloy components for optical applications.

### Electropolishing Equipment and Tooling

**Power supply**:
- Constant-current DC rectifier: 0-20V, 0-5000 A depending on workload size. Ripple <5%. Constant-current mode is preferred because the workpiece surface area changes as material dissolves (constant voltage would cause current to increase as the surface smooths, potentially leading to pitting).
- Pulse capability: Some electropolishing processes benefit from pulsed current (10-100 ms on, 10-100 ms off). The off-time allows the anodic film to reform, improving surface finish. Pulse electropolishing can achieve Ra <0.02 μm on 316L stainless steel.

**Fixturing**:
- The workpiece must be held with good electrical contact in the anodic (positive) position. Titanium or copper fixtures with spring-loaded contacts. Contact points leave small marks — position on non-critical surfaces. For tubular parts (sanitary tubing, pipes), a central cathode rod provides uniform internal electropolishing.
- Cathode design is critical for uniform current distribution. Complex shapes may require conformal cathodes (shaped to mirror the workpiece geometry with a uniform gap) or auxiliary cathodes for recessed areas. Typical anode-cathode gap: 20-100 mm.

**Electropolished surface characterization**:
- Surface roughness (profilometer): Ra, Rz, and Rq measurements. Electropolishing typically reduces Ra by 50-80% from the pre-polished state.
- Surface composition (XPS/ESCA): X-ray photoelectron spectroscopy measures the Cr/Fe ratio at the surface. A ratio >1.0 indicates effective chromium enrichment.
- Pitting resistance (ASTM B117 salt spray): Electropolished 316L stainless steel typically achieves 500-2000+ hours to first rust spot, compared to 24-100 hours for mechanically polished surfaces.
- Outgassing rate: Measured by throughput method in a vacuum chamber. Electropolished + baked 316L: ~10⁻¹⁰ Torr·L/s·cm². Mechanically polished: ~10⁻⁸ Torr·L/s·cm².

### Electroforming Process Detail

**Mandrel preparation and separation**:
- **Conductive mandrels** (stainless steel, nickel): The mandrel surface must be passivated to prevent the electroform from bonding permanently. Treatment: immersion in sodium dichromate (Na₂Cr₂O₇, 2-5%, 50-60°C, 10-30 min) or boiling in deionized water (forms a thin oxide release layer). After electroforming, mechanical force or thermal shock separates the electroform from the mandrel.
- **Sacrificial mandrels** (aluminum, wax, photoresist): The mandrel is destroyed during separation. Aluminum mandrels dissolved in NaOH (50-100 g/L, 50-70°C). Wax mandrels melted at 80-100°C. Photoresist mandrels dissolved in acetone or developer solution. Sacrificial mandrels allow complex internal geometries that cannot be released from permanent mandrels.
- **Mandrel surface preparation**: The mandrel surface finish is replicated in negative by the electroform. For optical-quality surfaces, the mandrel is diamond-turned to Ra <5 nm. For microstructured surfaces, the mandrel is patterned by photolithography (photoresist pattern on a conductive substrate).

**Multi-layer electroforming**:
- Complex parts can be built by sequentially electroforming different layers with different properties. Example: A mold insert with a hard wear surface and a tough backing — first deposit hard nickel (450 HV, with sulfur co-deposition from saccharin), then switch to ductile sulfamate nickel (200 HV) for the backing. The transition between layers must be clean (rinse, activate) to ensure interlayer adhesion.

### Electroless Plating on Non-Conductors

**Surface activation sequence** (for plastic and ceramic substrates):
1. **Etching**: Chromic acid (CrO₃, 300-500 g/L + H₂SO₄, 200-400 g/L, 60-70°C, 5-20 min) creates micro-roughness and introduces polar functional groups (-OH, -COOH) on the plastic surface for mechanical and chemical adhesion. The etch also removes surface contamination. Alternative for RoHS compliance: permanganate etch (KMnO₄, 30-50 g/L, NaOH, 60-70°C).
2. **Neutralization**: Sodium bisulfite (NaHSO₃, 10-20 g/L) reduces residual Cr⁶⁺ to Cr³⁺, preventing contamination of subsequent baths.
3. **Pre-activation**: Tin chloride (SnCl₂, 5-10 g/L in HCl) deposits a monolayer of Sn²⁺ ions on the etched surface.
4. **Activation**: Palladium chloride (PdCl₂, 0.1-0.5 g/L in HCl). Sn²⁺ reduces Pd²⁺ to Pd⁰, depositing catalytic palladium nuclei (1-5 nm particles) on the surface. The palladium nuclei catalyze electroless copper or nickel deposition.
5. **Acceleration**: Dilute acid or base removes excess tin without dislodging the palladium nuclei, exposing the active catalytic sites.

**Through-hole plating sequence** (PCB fabrication):
1. Drill holes through the PCB laminate (FR-4 epoxy-glass).
2. De-smear: Remove epoxy smear from drill holes using permanganate or plasma desmear.
3. Etchback: Remove a small amount of glass fiber to expose fresh copper inner-layer surfaces in the holes.
4. Electroless copper: Apply the 5-step activation sequence above, then deposit 0.5-2 μm electroless copper. The thin electroless copper makes the hole walls conductive.
5. Electrolytic copper: Panel plate the entire board with 20-35 μm electrolytic copper, building up the through-hole copper thickness. Current density: 15-30 mA/cm², time: 60-90 minutes.
6. Pattern and etch: Apply photoresist, pattern the circuit, and etch the unwanted copper. The through-holes remain plated.

### Defect Analysis

**Electropolishing defects**:
- **Pitting**: Small holes (10-100 μm) caused by inclusions in the base metal or excessive current density. Inclusions (sulfides, oxides) dissolve faster than the surrounding metal, creating pits. Prevention: use high-purity starting material, optimize current density.
- **Frosting**: Matte, white, non-reflective surface caused by insufficient current density or too-low electrolyte temperature. The anodic film does not form properly, and dissolution is non-uniform. Remedy: increase current density to 15-25 mA/cm², verify electrolyte temperature.
- **Edge attack**: Excessive material removal at sharp edges. Caused by current concentration at edges. Prevention: round all edges to >0.5 mm radius before electropolishing.

**Electroless nickel defects**:
- **Bath decomposition**: Spontaneous nickel plating throughout the bath (on tank walls, particles, everywhere) caused by too-high temperature, too-low stabilizer, or phosphite accumulation. The bath turns dark and must be discarded. Prevention: maintain temperature ±2°C, monitor stabilizer concentration, replace bath before phosphite exceeds limit.
- **Skip plating**: Unplated areas on an otherwise properly activated surface. Caused by insufficient surface activation (palladium coverage incomplete), contamination masking the surface, or insufficient etch. Remedy: verify activation solution freshness, increase etch time, clean the surface.

### Safety

**Perchloric acid explosion hazard**: Aluminum electropolishing uses 5-20% HClO₄ in ethanol or acetic acid. Perchloric acid is a powerful oxidizer that forms explosive perchlorate esters with organic solvents. Perchloric acid electropolishing MUST be performed in a dedicated fume hood with wash-down capability (perchloric acid fumes condense in ductwork and form explosive crystalline deposits). Never store perchloric acid near organic materials. A perchloric acid spill on organic flooring can cause delayed explosion.

**Electroless nickel bath decomposition**: Electroless nickel baths operate at 85-95°C with sodium hypophosphite (a reducing agent). If the bath temperature exceeds 95°C, or if stabilizer concentration drops too low, the bath undergoes uncontrolled autocatalytic decomposition — nickel plates out on all surfaces (tank walls, particles, plumbing) in an exothermic runaway reaction. The resulting nickel dust is pyrophoric when dry. Maintain temperature within ±2°C. Install high-temperature automatic bath dump or dilution system.

**Hexavalent chromium exposure**: Chromic acid (CrO₃) used in aluminum electropolishing and plastic etching contains hexavalent chromium (Cr⁶⁺), a confirmed human carcinogen (lung cancer). TLV-TWA: 0.025 mg/m³ (extremely low). All Cr⁶⁺ handling must be in closed systems with local exhaust ventilation. Workers must wear respiratory protection (P100 cartridge or supplied air). Replace chromic acid etching with permanganate etching where possible.

**Cyanide waste from gold baths**: Gold immersion baths contain potassium gold cyanide (KAu(CN)₂). Cyanide waste must be destroyed by alkaline chlorination (NaOCl at pH 10-11) BEFORE acidification — acidifying cyanide waste releases HCN gas, which is lethal at 300 ppm. Cyanide treatment must occur in a well-ventilated area with H₂S/HCN monitors.

**Nickel sensitization**: Nickel and nickel compounds are skin sensitizers (allergic contact dermatitis affects 10-20% of the general population). Repeated skin contact with nickel plating solutions causes sensitization that is permanent — once sensitized, even trace nickel exposure causes dermatitis. Wear nitrile gloves (double-gloved) when handling nickel solutions. Do not touch nickel-plated parts with bare hands.

### See Also

- **[Electroplating](electroplating.md)**: Copper damascene and electrolytic plating processes
- **[Anodizing](anodizing.md)**: Electrochemical oxide growth on aluminum and titanium
- **[Electrolysis](../chemistry/electrolysis.md)**: Fundamental electrochemistry principles
- **[Metal Finishing](../metals/finishing.md)**: Broader context of surface treatment processes

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electrochemistry & Plating](./index.md) • [All Domains](../index.md)*
