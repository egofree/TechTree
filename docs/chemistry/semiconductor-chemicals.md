# Semiconductor Process Chemicals

> **Node ID**: chemistry.semiconductor-chemicals
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.hydrogen-silane`](hydrogen-silane.md), [`chemistry.dopant-etch-gases`](dopant-etch-gases.md)
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`silicon.basic-devices`](../silicon/basic-devices.md)
> **Timeline**: Years 40-70
> **Outputs**: photoresist, tmah_developer, boe_etchant, cmp_slurry, cleanroom_chemicals
> **Critical**: Yes — semiconductor process chemicals (photoresist, etchants, CMP slurries, cleaning solutions) are consumed in every step of integrated circuit fabrication. Without ultra-pure chemicals at ppb trace metal levels, semiconductor manufacturing yields collapse to zero.


Semiconductor fabrication consumes chemicals at purity levels 1000× stricter than reagent grade — metallic impurities below 1 ppb, particles filtered to 0.003 μm. This page covers the liquid-phase process chemicals distinct from the gas-phase dopant and etch gases cataloged in [Dopant & Etch Gases](dopant-etch-gases.md): photoresists (organic polymers patterned by UV light), developers (TMAH), wet etchants (buffered oxide etch), CMP slurries (mechanochemical planarization), and cleanroom cleaning chemicals. Solvents used in wafer cleaning (IPA, acetone, xylene) are cataloged in [Solvents](solvents.md); this page addresses their specific semiconductor applications without duplicating general solvent chemistry.

## Photoresist Chemistry

Photoresists are radiation-sensitive polymer films that transfer a mask pattern onto a wafer surface. They are the enabling material of photolithography — without them, there is no integrated circuit fabrication.

#### DNQ/Novolac Positive Resist (g-line/i-line)

The workhorse resist for feature sizes down to ~0.35 μm (i-line, 365 nm). Two-component system:

**Novolac resin** (base-soluble matrix polymer):
- Phenol-formaldehyde condensation polymer (novolak type, acid-catalyzed).
- Molecular weight 3,000-15,000 Da. Glass transition temperature (Tg) ~120°C.
- Soluble in aqueous base (TMAH developer) due to phenolic hydroxyl groups.
- Synthesized from m-cresol (3-methylphenol) and formaldehyde in acidic conditions (oxalic acid catalyst, 100-110°C, 4-8 hours). The m-cresol isomer provides the dissolution properties needed for high contrast — para-cresol and ortho-cresol novolacs have inferior dissolution inhibition/release behavior.
- Dissolved in ethyl lactate or propylene glycol monomethyl ether acetate (PGMEA) as casting solvent for spin coating.

**DNQ photoactive compound** (PAC, dissolution inhibitor):
- Diazonaphthoquinone (DNQ), typically esterified with a ballast molecule (trihydroxybenzophenone ester of DNQ sulfonic acid).
- Weight fraction: 20-35% of total solids (resin + PAC). Higher PAC loading increases contrast but reduces photospeed.
- Mechanism: DNQ is insoluble in aqueous base and inhibits novolac dissolution. Upon UV exposure (365-436 nm), DNQ undergoes Wolff rearrangement: DNQ → ketene → indene carboxylic acid. The carboxylic acid product is highly soluble in aqueous TMAH developer, enabling selective dissolution of exposed regions.

**Photoresist processing steps**:
1. **Spin coating**: Dispense 2-4 mL of resist solution onto wafer. Spin at 3000-5000 RPM for 30 seconds. Film thickness inversely proportional to √(spin speed): typically 0.8-2.0 μm for g/i-line resists at 25-35% solids content. Thickness uniformity ±5% across 200 mm wafer.
2. **Soft bake (prebake)**: 90-110°C for 60-90 seconds on a hot plate. Removes casting solvent (ethyl lactate bp 154°C; PGMEA bp 146°C) to ~3-5% residual solvent. Too much residual solvent causes film flow (pattern deformation); too little causes adhesion failure.
3. **Exposure**: Mercury lamp g-line (436 nm) or i-line (365 nm). Dose: 50-200 mJ/cm². Higher dose needed for thicker films. Exposure tool numerical aperture (NA) determines resolution: resolution ≈ k₁λ/NA, where k₁ ≈ 0.5-0.8.
4. **Post-exposure bake (PEB)**: 100-120°C for 60 seconds. Completes the Wolff rearrangement and improves pattern fidelity by reducing standing wave effects (interference between incident and reflected light creates sinusoidal dose variation through the resist thickness).
5. **Development**: 2.38% TMAH aqueous solution (see TMAH section below). 60-90 seconds with gentle agitation. Dissolves exposed regions. Development rate ratio (exposed:unexposed) >1000:1 for high-contrast resists.
6. **Hard bake**: 120-140°C for 60 seconds. Crosslinks residual resin to improve etch resistance and adhesion. Must stay below Tg of the resist to prevent thermal flow.

**Strengths**: DNQ/novolac resist system is well-proven for 350 nm+ features with >1000:1 dissolution contrast; spin coating produces uniform films across 200-300 mm wafers; aqueous TMAH developer is non-toxic compared to organic solvent developers; six-step process is standardized across the entire industry.

**Weaknesses**: DNQ/novolac cannot resolve below ~250 nm (absorbs at DUV wavelengths); CAR resists are extremely sensitive to airborne amine contamination at ppb levels (requires filtered cleanroom air); spin coating wastes ~95% of dispensed resist; photoresist is a single-use consumable with no recovery path; tight process windows (±0.5°C temperature, ±5% thickness) require precise equipment control.

**Resolution vs sensitivity tradeoff**: Higher PAC loading increases contrast (steeper dissolution curve) but requires higher exposure dose. Thinner resist films resolve smaller features but provide less etch resistance. For i-line lithography at 0.35 μm: ~1.0 μm resist thickness, ~150 mJ/cm² dose, contrast (γ) ≈ 3-5.

#### Chemically Amplified Resists (CAR)

Required for deep UV (DUV, 248 nm and 193 nm) lithography where photon flux is limited. DUV sources (KrF excimer at 248 nm, ArF excimer at 193 nm) produce fewer photons per unit area than mercury lamps, so the resist must amplify each photon's effect.

**Mechanism**: A single photon generates one photoacid molecule (from a photoacid generator, PAG). During PEB (90-130°C, 60-120 seconds), the photoacid catalyzes hundreds to thousands of deprotection reactions in the polymer matrix — chemical amplification. One photon → ~1000 chemical events.

**248 nm (KrF) resist system**: Poly(hydroxystyrene) (PHS) base polymer with t-BOC (tert-butoxycarbonyl) protecting groups. PAG: triphenylsulfonium triflate (TPS-OTf) at 2-10 wt%. Exposure: TPS-OTf + hν → strong acid (CF₃SO₃H). PEB: acid cleaves t-BOC groups from PHS, converting the polymer from insoluble (protected) to soluble (deprotected, phenolic OH exposed) in aqueous TMAH. Amplification factor: 800-1500 deprotection events per photon.

**193 nm (ArF) resist system**: Cannot use phenolic polymers (phenol absorbs strongly at 193 nm). Acrylic or alicyclic polymers (poly(norbornene-maleic anhydride) or COMA — cycloolefin-maleic anhydride) with acid-labile protecting groups (ethyl adamantyl, methyl adamantyl). PAG: similar sulfonium or iodonium salts with fluorinated anions. The alicyclic backbone provides the etch resistance that phenolic groups provided in earlier resists.

**Environmental stability concern**: CAR resists are sensitive to airborne base contaminants (amines, ammonia, NMP) at ppb levels. Ambient amine molecules neutralize the photoacid at the resist surface, causing T-topping (underdeveloped top layer). Solution: chemically filtered air supply (activated carbon + acid-impregnated filter) in the lithography bay, maintaining <1 ppb amine concentration. Seal coated wafers in nitrogen-purged containers between exposure and PEB.

**Resolution achievements**: CAR at 193 nm with immersion lithography (water between lens and wafer, NA >1.0) resolves features to ~38 nm half-pitch (double-patterning techniques extend this further).

## TMAH Developer

Tetramethylammonium hydroxide (N(CH₃)₄OH, TMAH) is the standard aqueous developer for positive photoresists.

**Properties**:
- Strong organic base (pKb ≈ -0.2). Completely dissociated in water.
- Colorless liquid, miscible with water in all proportions. Available as 25% aqueous solution.
- **Standard semiconductor concentration: 2.38% TMAH in water** (the industry-standard developer, "MF-26A" equivalent).
- Boiling point: ~102°C at 2.38% concentration.

**Developer chemistry**: TMAH dissolves exposed positive resist by deprotonating phenolic hydroxyl groups on the novolac resin (or deprotected CAR polymer), converting the polymer to its water-soluble phenolate salt. Unexposed regions remain insoluble because the DNQ dissolution inhibitor (or unreacted protecting groups in CAR) blocks base access to the phenolic sites.

**Process parameters**:
- Development temperature: 23 ± 0.5°C. Temperature uniformity critical — development rate changes ~5%/°C.
- Development time: 60-90 seconds (puddle development) or 30-60 seconds (spray development).
- Endpoint detection: monitor dissolved resist products in the developer stream using optical absorption at 310 nm (novolac chromophore absorption).

**Anisotropic silicon etch**: Concentrated TMAH (5-25%) at 70-90°C etches silicon anisotropically — etching <100> planes ~30× faster than <111> planes. Etch rate: 0.5-1.0 μm/min for <100> silicon at 80°C, 10% TMAH. Produces V-grooves and pyramidal pits bounded by {111} planes. Used for MEMS structures, inkjet nozzles, and silicon micromachining. Adding IPA (isopropanol, 5-15% by volume) to TMAH reduces surface roughness by promoting hydrogen bubble detachment — bubbles otherwise cause localized etch non-uniformity.

**TMAH production**: Produced by reacting trimethylamine (TMA) with water in an electrochemical cell, or by reacting TMA with silver oxide. Commercial synthesis: trimethylamine (from methanol + ammonia over catalyst) is reacted with methyl chloride to form tetramethylammonium chloride, then electrolyzed or reacted with silver oxide to produce TMAH.

**Toxicity**: TMAH is highly corrosive and toxic. Dermal contact with concentrated solutions causes severe chemical burns and systemic toxicity (tetramethylammonium ion is a neurotoxin — blocks neuromuscular transmission). Fatal industrial accidents have occurred from skin exposure to 25% TMAH. Handle in enclosed systems with chemical-resistant gloves (butyl rubber) and eye protection. At 2.38% concentration (developer strength), acute toxicity is lower but still requires proper PPE.

## Buffered Oxide Etch (BOE)

Buffered oxide etch (also called BHF — buffered hydrofluoric acid) is the standard wet etchant for silicon dioxide (SiO₂) in semiconductor fabrication. It provides controlled, uniform etching without the rapid, aggressive attack of concentrated HF.

**Composition**: Mixture of hydrofluoric acid (HF) and ammonium fluoride (NH₄F). The NH₄F buffer maintains a constant fluoride ion concentration, preventing depletion of the active etching species.

**Common formulations**:
- **7:1 BOE**: 7 parts NH₄F (40% aqueous) to 1 part HF (49% aqueous). Most common for general oxide etching. SiO₂ etch rate: ~70-80 nm/min at 23°C. Selectivity over silicon: effectively infinite (HF does not etch silicon).
- **5:1 BOE**: Higher etch rate, ~100-120 nm/min at 23°C. Used for thicker oxide removal.
- **10:1 BOE**: Lower etch rate, ~50-60 nm/min. Better control for thin oxide etching.
- **20:1 BOE**: Very slow, ~25-30 nm/min. For critical thickness control.

**Etch chemistry**: HF etches SiO₂ by breaking Si-O bonds: SiO₂ + 6HF → H₂SiF₆ + 2H₂O. The ammonium fluoride buffers the HF by providing excess F⁻ ions: NH₄F → NH₄⁺ + F⁻. The dominant etching species is HF₂⁻ (bifluoride ion), formed by HF + F⁻ → HF₂⁻. The buffered solution maintains a constant concentration of HF₂⁻ even as HF is consumed, giving a stable etch rate over time (unlike pure HF, which slows as it depletes).

**Etch rate dependence on oxide type**:
- Thermally grown SiO₂ (dry): ~70 nm/min (7:1 BOE, 23°C) — dense, stoichiometric oxide.
- Thermally grown SiO₂ (wet): ~80 nm/min — slightly more porous due to hydroxyl incorporation.
- CVD SiO₂ (TEOS): ~90 nm/min — less dense than thermal oxide.
- PECVD SiO₂: ~120 nm/min — significantly less dense, more porous.
- BPSG (borophosphosilicate glass): ~200-400 nm/min — much faster due to phosphate and borate content increasing solubility.
- PSG (phosphosilicate glass): ~150-250 nm/min.

**Photoresist adhesion during BOE**: HF undercuts photoresist by attacking the SiO₂-Si interface. HMDS (hexamethyldisilazane) adhesion promoter is applied before resist coating to improve adhesion. Even with HMDS, BOE undercuts resist by 50-200 nm per side — significant for features below 2 μm. Vapor-phase HF etching (no liquid contact) eliminates undercut for critical applications.

**Safety**: BOE contains HF. All HF safety protocols apply (see [Acids](acids.md) for HF hazards). Calcium gluconate gel must be immediately available. Etch bench must have: HF-resistant container (PTFE or HDPE — never glass), calcium gluconate station within 10 seconds reach, eye wash and safety shower, HF-specific training for all operators. Even dilute HF (<1%) can cause delayed but serious burns — the fluoride ion penetrates skin and decalcifies bone.

## CMP Slurry Chemistry

Chemical mechanical polishing (CMP) planarizes wafer surfaces between deposition and lithography steps, enabling multilayer interconnect. The CMP process is covered in detail in [Dopant & Etch Gases](dopant-etch-gases.md); this section provides the chemical formulation details. CMP slurry is a colloidal suspension of abrasive particles in a chemically reactive solution.

#### Oxide CMP (SiO₂ planarization)

**Slurry composition**:
- Abrasive: Colloidal silica (SiO₂) particles, 30-70 nm diameter. Produced by the Stöber process (hydrolysis of tetraethyl orthosilicate TEOS in ethanol with ammonia catalyst) or by alkali silicate neutralization.
- pH: 10.11 (alkaline, adjusted with KOH). High pH keeps silica particles negatively charged and well-dispersed (zeta potential <-30 mV).
- Solids content: 12-30 wt% silica.
- Common commercial slurry: SS-12 (12% colloidal silica) or SS-25 (25% colloidal silica).

**Removal mechanism (Preston's equation)**: Removal rate (RR) = Kp × P × V, where Kp is Preston's coefficient (material-specific constant), P is applied pressure (psi), and V is relative velocity between wafer and polishing pad (ft/min). For oxide CMP: Kp ≈ 3-8 × 10⁻¹³ cm²/dyne. Typical conditions: P = 3-5 psi, V = 150-300 ft/min → RR = 100-300 nm/min.

**Selectivity**: Oxide-to-nitride selectivity typically 4:1 to 10:1 (achieved by adding ceria or adjusting pH). Nitride acts as an etch stop in shallow trench isolation (STI) CMP.

#### Metal CMP (Cu, W, Al)

**Copper CMP slurry**:
- Abrasive: Colloidal silica (30-50 nm) or alumina (Al₂O₃, 100-200 nm). Alumina provides faster removal but worse surface finish.
- Oxidizer: Hydrogen peroxide (H₂O₂, 1-5%) or potassium iodate (KIO₃) at 1-3 wt%. H₂O₂ oxidizes copper to CuO/Cu₂O: 2Cu + H₂O₂ → Cu₂O + H₂O; Cu₂O + H₂O₂ → 2CuO + H₂O. The oxide layer is mechanically removed by abrasive particles.
- Complexing agent: Glycine (aminoacetic acid, 0.5-2%) dissolves copper oxide into soluble complexes: CuO + 2NH₂CH₂COOH → Cu(NH₂CH₂COO)₂ + H₂O.
- Corrosion inhibitor: Benzotriazole (BTA, 0.01-0.1%) forms a passivating Cu-BTA film on recessed areas, protecting them while protruding areas are abraded away. This chemical selectivity is what enables planarization (without BTA, CMP would simply thin the film uniformly).
- pH: 4-7 (slightly acidic to neutral). Controlled with HNO₃ or KOH.
- Removal rate: 200-800 nm/min for copper.

**Tungsten CMP slurry**:
- Abrasive: Alumina (Al₂O₃, 50-200 nm) or colloidal silica.
- Oxidizer: Ferric nitrate (Fe(NO₃)₃, 5-15%) or hydrogen peroxide. Fe³⁺ oxidizes W to WO₃: W + 6Fe³⁺ + 3H₂O → WO₃ + 6Fe²⁺ + 6H⁺.
- pH: 2-4 (acidic). Iron-based oxidizers require acidic conditions.
- Removal rate: 150-500 nm/min for tungsten.

#### Post-CMP Cleaning

After polishing, slurry particles and metallic contaminants must be completely removed. A single remaining silica particle (50 nm) between two metal lines can create a short circuit.

**Cleaning sequence** (see also [Dopant & Etch Gases](dopant-etch-gases.md)):
1. **PVA brush scrubbing**: Soft polyvinyl alcohol brush roller rotates against the wafer surface under DI water or dilute NH₄OH (1-2%) at 20-40°C. Mechanical action dislodges particles; NH₄OH provides electrostatic repulsion (zeta potential) to prevent re-adhesion.
2. **Megasonic clean**: 0.8-1.6 MHz acoustic cavitation in DI water generates microscopic bubbles that implode at the wafer surface, dislodging sub-micron particles without mechanical contact. Power density: 10-50 W/cm².
3. **Marangoni drying**: IPA vapor introduced at the meniscus between the water film and wafer surface. Surface tension gradient (water: 72 mN/m → IPA-water: ~23 mN/m) pulls the water film off the surface, leaving a dry, particle-free surface without water marks.

## Cleanroom Chemicals

#### Ultrapure Water (UPW)

Ultrapure water is the most-consumed chemical in semiconductor fabrication — a modern fab uses 3-8 million liters per day. Production is covered in [Industrial Water Treatment](water-treatment.md); key semiconductor-grade specs:

- Resistivity: 18.2 MΩ·cm at 25°C (theoretical maximum for pure water).
- Total organic carbon (TOC): <1 ppb. Organic contamination causes hazing on wafer surfaces and photoresist adhesion failure.
- Dissolved oxygen: <5 ppb. Oxygen in rinse water re-oxidizes freshly etched or cleaned surfaces.
- Particles: <0.5 per mL at ≥0.05 μm.
- Bacteria: <1 per 100 mL. Bacteria colonize water distribution systems and shed endotoxins that interfere with thin film adhesion.
- Dissolved silica: <0.5 ppb. Silica deposits on wafer surfaces during drying.
- Metal ions: each individual metal <0.01 ppb (10 ppt). Na, K, Fe, Cu, Zn, Al, Cr are the most critical — even trace metals cause threshold voltage shifts in MOSFETs.

UPW distribution system: PVDF (polyvinylidene fluoride) or high-purity PFA piping. Continuous recirculation at 1-3 m/s velocity to prevent bacterial growth. UV (185/254 nm) irradiation for TOC destruction and bacterial control. Final 0.05 μm ultrafiltration membrane at point of use.

#### IPA (Isopropanol) — Semiconductor Applications

General IPA properties are covered in [Solvents](solvents.md). Semiconductor-specific uses:

- **Wafer drying agent**: Marangoni drying (described above). Vapor-phase IPA eliminates water marks on hydrophilic surfaces.
- **Photoresist edge bead removal (EBR)**: IPA or PGMEA sprayed at wafer edge during spin coating to remove the thick resist bead that forms at the edge (would cause contact with the mask in contact printing). EBR width: 1-3 mm from wafer edge.
- **General cleaning**: IPA-dampened cleanroom wipers for tool surfaces. Chamber cleaning after maintenance. Evaporates cleanly without residue (vapor pressure 33 mmHg at 20°C).

**Semiconductor-grade IPA**: Purity 99.999%+, metallic impurities <1 ppb each, particles <25/mL at ≥0.2 μm, water content <100 ppm (for drying applications). Stored in 316L stainless steel or fluoropolymer containers.

#### Acetone — Semiconductor Applications

Acetone (CH₃COCH₃, bp 56°C) is covered as a solvent in [Solvents](solvents.md) and [Petroleum](petroleum-alternatives.md). Semiconductor uses:

- **Photoresist stripping**: Bulk resist removal before plasma ashing. Acetone swells and dissolves novolac-based resists at room temperature in 1-5 minutes. For hardened (post-hard-bake) or crosslinked resists, heating acetone to 50-55°C improves stripping efficiency. Not effective for fully crosslinked resists or deep UV (DUV) resists — these require plasma ashing or specialized strippers (NMP-based or DMSO-based).
- **Surface cleaning**: Degreasing wafer surfaces before thermal oxidation or film deposition. Acetone followed by IPA rinse followed by DI water rinse followed by N₂ blow-dry is the standard "solvent clean" sequence.
- **Chamber cleaning**: Wiping CVD and etch chamber internals during maintenance.

#### Piranha Etch (SPM)

**Composition**: Sulfuric acid (H₂SO₄) : hydrogen peroxide (H₂O₂) = 3:1 to 4:1 by volume. Also called "piranha solution" or "sulfuric-peroxide mixture" (SPM).

**Preparation**: Always add H₂O₂ to H₂SO₄, NEVER the reverse. The reaction is extremely exothermic — temperature reaches 100-130°C. Use a PTFE or glass vessel in a chemical fume hood. Prepare fresh immediately before use — piranha decomposes within 30-60 minutes (the peroxide decomposes, and the mixture loses its oxidative power).

**Chemistry**: H₂SO₄ dehydrates organic contaminants while H₂O₂ provides atomic oxygen for oxidation. The combination produces Caro's acid (H₂SO₅): H₂SO₄ + H₂O₂ → H₂SO₅ + H₂O. Caro's acid is an extremely powerful oxidizer that destroys virtually all organic materials, converting them to CO₂ + H₂O.

**Applications**:
- **Photoresist stripping**: Removes heavily crosslinked or ion-implanted resist that acetone and plasma ashing cannot fully remove. Immersion time: 10-30 minutes at 100-130°C. Dissolves resist completely, including sidewall polymer deposits from etching.
- **Surface cleaning and hydrophilization**: Leaves silicon surface terminated with -OH groups (hydrophilic, contact angle <10°). Essential for photoresist adhesion — hydrophobic surfaces cause resist delamination during development and etching.
- **Particle removal**: Oxidizes organic particles to CO₂ and H₂O. Inorganic particles are lifted off by the vigorous oxygen evolution (bubbles provide mechanical agitation).

**Safety**: Piranha is one of the most dangerous solutions in a semiconductor fab. The mixture boils spontaneously if organic material is added in quantity. It reacts explosively with significant amounts of organics (solvents, photoresist chunks). Never store in sealed containers — gas evolution (O₂) builds pressure and can rupture the container. Never add to organic solvents. PPE: acid-resistant apron, face shield, chemical splash goggles, HF-rated gloves (even though piranha is not HF, the same heavy nitrile or neoprene gloves provide adequate protection). Emergency shower within 10 seconds of travel. Piranha waste is neutralized by slow addition to large volumes of cold water (never the reverse), then neutralized with NaOH before disposal.

#### RCA Clean (SC-1 and SC-2)

The RCA clean is the foundation of semiconductor wafer cleaning, developed by Werner Kern at RCA in 1965. Hydrogen peroxide chemistry is covered in [Solvents](solvents.md); here the specific formulations and their semiconductor functions:

**SC-1 (Standard Clean 1) — Particle and organic removal**:
- Composition: NH₄OH : H₂O₂ : H₂O = 1:1:5 (by volume, at 75-80°C).
- Ammonium hydroxide (NH₄OH, 28-30% aqueous) provides alkaline conditions (pH ~10) and electrostatic repulsion between particles and wafer surface (both acquire negative zeta potential, preventing re-deposition).
- H₂O₂ oxidizes organic contaminants to CO₂ and H₂O. Also oxidizes the silicon surface to a thin SiO₂ layer (1-2 nm), undercutting and releasing particles.
- Process: 10-20 minutes at 75-80°C. Must be freshly mixed — H₂O₂ decomposes rapidly at these temperatures. Bath life: 20-30 minutes before H₂O₂ depletion.
- Particle removal efficiency: >99% for particles ≥0.5 μm.

**SC-2 (Standard Clean 2) — Metal removal**:
- Composition: HCl : H₂O₂ : H₂O = 1:1:6 (by volume, at 75-80°C).
- Hydrochloric acid (HCl, 37% aqueous) provides chloride ions that form soluble complexes with metal ions: Fe³⁺ + 6Cl⁻ → FeCl₆³⁻; Cu²⁺ + 4Cl⁻ → CuCl₄²⁻. These complexes are desorbed from the surface and remain in solution.
- H₂O₂ maintains oxidizing conditions to keep metals in their higher oxidation states (more soluble).
- Process: 10-20 minutes at 75-80°C. Less vigorous than SC-1; bath life somewhat longer.
- Metal removal: reduces surface metal contamination from ~10¹¹-10¹² atoms/cm² to <10⁹ atoms/cm².

**Typical cleaning sequence**: SC-1 → DI water rinse → HF dip (1-2% HF, 15-30 seconds, removes native oxide and leaves H-terminated hydrophobic surface) → DI water rinse → SC-2 → DI water rinse → N₂ dry. The HF dip between SC-1 and SC-2 is optional — it removes the oxide grown during SC-1 and any particles trapped in that oxide.

#### Hydrofluoric Acid Dip (HF Last)

A brief dip in dilute HF (0.5-2% aqueous) strips the native or chemical oxide from silicon, leaving a hydrogen-terminated surface:

- Etch rate: ~2 nm/sec for thermal SiO₂ at 1% HF, 23°C.
- Contact angle: ~70-80° (hydrophobic). Water beads and rolls off.
- Application: pre-thermal-oxidation clean (removes native oxide for uniform gate oxide growth), pre-epitaxy clean (hydrogen-terminated surface is atomically clean for epitaxial growth).
- Stability: H-terminated surface is metastable — it re-oxidizes in air over hours to days. Process wafers quickly after HF dip (within 30 minutes for gate oxide growth, within 2 hours for less critical steps).
- Safety: All HF protocols apply. At 0.5-2% concentration, the immediate burn risk is lower than concentrated HF, but systemic fluoride toxicity (hypocalcemia) is still possible from prolonged skin contact. Same PPE as BOE.

## Wet Etch Process Integration

Wet etching is isotropic (etches equally in all directions) — this limits its use for fine features. Below ~2 μm feature size, anisotropic dry (plasma) etching in [Dopant & Etch Gases](dopant-etch-gases.md) is required. However, wet etching remains essential for:

- **Field oxide removal** (large areas, not critical dimension): BOE or concentrated HF.
- **Backside wafer cleaning**: Remove processing contamination from the wafer backside before high-temperature steps.
- **Sacrificial layer release** (MEMS): HF vapor etches SiO₂ release layers without stiction issues that liquid HF causes.
- **Silicon anisotropic etching**: TMAH or KOH for MEMS structures (V-grooves, membranes, cantilevers).
  - **KOH** (potassium hydroxide): 30-45% aqueous, 70-90°C. <100>:<111> selectivity ~400:1. Etch rate: 1.0-1.5 μm/min at 80°C, 40% KOH. Disadvantage: K⁺ ions are a fast-diffusing contaminant in MOS devices — requires thorough cleaning after KOH etch. TMAH is preferred for IC-compatible processing.
  - **TMAH**: 5-25% aqueous, 70-90°C. <100>:<111> selectivity ~30:1. Etch rate: 0.5-1.0 μm/min at 80°C, 10% TMAH. Advantage: IC-compatible (no alkali metal contamination). Disadvantage: lower selectivity than KOH, rougher surface finish.

## Limitations

- **Purity requirements dwarf standard chemical production**: Semiconductor-grade chemicals require metallic impurities <1 ppb, particles <25/mL at ≥0.2 μm. Achieving this requires dedicated cleanroom-packaged production lines, multiple purification stages, and lot-by-lot trace metal analysis by ICP-MS. The infrastructure for electronic-grade chemical production rivals the fab itself in cost and complexity.
- **Photoresist resolution ceiling**: DNQ/novolak resists cannot resolve below ~0.35 μm (limited by optical diffraction and resist contrast). CAR resists extend to ~38 nm with 193 nm immersion lithography but require extraordinary environmental control (ppb-level amine filtration) and sophisticated polymer chemistry (meta-stable protecting groups with tight dose-response curves).
- **CMP defectivity**: Slurry particles left on the wafer after CMP are a leading cause of yield loss in multilayer interconnect processes. Post-CMP cleaning must achieve >99.999% particle removal efficiency — a single 50 nm silica particle can bridge two metal lines spaced 100 nm apart, creating a short circuit.
- **Wet etch isotropy limits feature size**: BOE and other wet etchants undercut the mask by an amount equal to the etch depth. For a 1 μm oxide etch, the undercut is ~1 μm per side, consuming 2 μm of feature space. Below ~2 μm features, dry (plasma) etching is mandatory for anisotropic (vertical sidewall) pattern transfer.
- **Environmental and safety burden**: BOE contains HF (lethal, bone-dissolving). Piranha is explosively reactive with organics. TMAH is a neurotoxin at moderate concentrations. CMP slurry generates thousands of liters of metal-laden wastewater per day requiring treatment. The chemical hazard footprint of semiconductor manufacturing is substantial and requires continuous investment in safety infrastructure, training, and abatement systems.

## See Also

- **[Solvents](solvents.md)**: IPA, acetone, hydrogen peroxide — general solvent chemistry and RCA clean overview
- **[Dopant & Etch Gases](dopant-etch-gases.md)**: Gas-phase etch chemistry (CF₄, Cl₂, SF₆), CMP slurry overview, and plasma etch system details
- **[Acids](acids.md)**: HF production and safety protocols
- **[Industrial Water Treatment](water-treatment.md)**: UPW production (RO + EDI + UV + UF to 18.2 MΩ·cm)
- **[Photoresists, Masks & Lithography](../photolithography/resists-masks.md)**: Lithography process integration using the chemicals described here
- **[Cleanrooms](../photolithography/cleanrooms.md)**: Cleanroom construction and contamination control
- **[Core Fab Processes](../photolithography/fab-processes.md)**: Full IC fabrication flow using wet and dry etch



[← Back to Chemistry](index.md)
