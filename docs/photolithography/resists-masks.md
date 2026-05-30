# Photoresists, Masks & Lithography

> **Node ID**: photolithography.resists-masks
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`chemistry.basic`](../chemistry/index.md), [`glass.basic`](../glass/basic.md), [`polymers.thermosets`](../polymers/thermosets.md)
> **Enables**: [`vlsi-scaling.advanced-lithography`](../vlsi-scaling/advanced-lithography.md)
> **Timeline**: Years 40-70
> **Outputs**: photoresists, masks, lithography_tools, patterned_wafers
> **Critical**: Yes — photolithographic patterning is the defining process of semiconductor manufacturing

## Photoresists

**[Bitumen resist](../glossary/bitumen-resist.md)** (simplest, historical — Niépce, 1826):
- Dissolve bitumen of Judea (natural asphalt) in lavender oil or turpentine. Coat on substrate. Expose to UV through mask (hours of exposure — very slow). Exposed areas harden (polymerize), unexposed areas dissolve in solvent. Low resolution (~100 μm+), very slow, but requires zero chemistry infrastructure.

**[Dichromated gelatin](../glossary/dichromated-gelatin.md)** (mid-19th century):
- Mix gelatin (from animal collagen) with ammonium dichromate ((NH₄)₂Cr₂O₇, ~5-10%). Coat on substrate. UV exposure causes Cr(VI) → Cr(III) reduction, cross-linking gelatin (insoluble). Unexposed gelatin washes away in warm water. Resolution ~10-50 μm. Chromium compounds are toxic and carcinogenic — handle with care.

**[Novolac + DNQ resist](../glossary/novolac-dnq-resist.md)** (standard positive-tone photoresist, requires the Chemistry stage organic chemistry):
- **Novolac resin**: Phenol + formaldehyde condensation polymer (m-cresol variant for photoresist). See [Polymers](../polymers/index.md) for production. Molecular weight ~2000-5000. Dissolves in aqueous base (NaOH or TMAH).
- **DNQ sensitizer**: Diazonaphthoquinone sulfonate (from naphthol + diazotization). ~20-30% by weight in resist. Function: DNQ acts as dissolution inhibitor — unexposed resist does NOT dissolve in developer. UV exposure → DNQ undergoes Wolff rearrangement → forms indene carboxylic acid → actually ENHANCES dissolution in aqueous base. This is the positive-tone mechanism.
- **Solvent**: Ethyl lactate or propylene glycol monomethyl ether acetate (PGMEA). ~60-80% of resist formulation.
- **Spin coating**: Dispense ~2-5 ml resist on wafer center. Spin at 1000-6000 RPM for 30-60 seconds. Centrifugal force spreads resist uniformly. Thickness: 0.5-3 μm (depends on viscosity and spin speed — roughly t ∝ 1/√ω). Edge bead removal (EBR): spray solvent at wafer edge while spinning to remove thick bead that forms at edge.
- **Soft bake (pre-bake)**: 90-110°C for 60-90 seconds on hot plate. Drives off solvent. Residual solvent <3%.
- **Exposure**: UV light (365 nm i-line, 405 nm h-line, or 436 nm g-line from mercury lamp). Dose: 50-200 mJ/cm². Exposed regions become soluble.
- **Post-exposure bake (PEB)**: 110-130°C for 60-90 seconds. Improves pattern definition by reducing standing wave effects.
- **Development**: Aqueous base — 2.38% TMAH (tetramethylammonium hydroxide) for 30-90 seconds with gentle agitation. TMAH preferred over NaOH (metal-ion-free developer — sodium contamination degrades MOS devices).
- **Hard bake**: 120-150°C for 60-120 seconds. Cross-links resist for etch resistance. Not always needed.

**[Negative-tone resists](../glossary/negative-tone-resists.md)** (exposed regions become insoluble):
- **[SU-8](../glossary/su-8.md)** (epoxy-based, modern): Epoxy novolac resin + triarylsulfonium salt photoacid generator (PAG). UV exposure generates acid → PEB causes acid-catalyzed epoxy cross-linking. Highly cross-linked, excellent chemical resistance. Can pattern thick films (5-500 μm) in a single coat. Used for MEMS structures, thick passivation, electroplating molds. Resolution limited by swelling during development (~2-5 μm minimum for thin films).
- **[Isoprene-based](../glossary/isoprene-based.md)** (historical): Cyclized polyisoprene + bis-azide sensitizer. UV exposure causes azide to form nitrene radicals, cross-linking the rubber. Unexposed regions dissolve in xylene. Swelling during development limits resolution to ~2-3 μm. Historically important (Kodak KTFR, early IC production in 1960s-70s). Largely replaced by positive resists due to swelling artifacts.

**Strengths**:
- Novolac/DNQ positive-tone system provides 0.25-1.0 μm resolution with i-line exposure — well-understood chemistry with 50+ years of production use
- SU-8 negative resist can pattern 5-500 μm thick films in a single coat — unmatched for MEMS and electroplating molds

**Weaknesses**:
- Bitumen resist requires hours of exposure with ~100 μm+ resolution — only suitable for initial experimentation
- Isoprene-based negative resists suffer swelling during development, limiting resolution to ~2-3 μm

## Polymer Packaging Materials
- **Epoxy encapsulation**: Two-part epoxy for die attach and hermetic sealing — see [Polymers](../polymers/index.md) and [Semiconductor Packaging & Testing](../chemistry/packaging-testing.md)
- **Plastic substrates and lead frames**: Molded plastic packages for integrated circuits
- **Phenolic laminate (FR-4)**: PCB substrate material from phenolic or epoxy resin impregnated glass fabric — see [Polymers](../polymers/index.md)
- **Photoresist dependency**: Novolac resin (phenol + formaldehyde condensation polymer) production path documented in [Polymers](../polymers/index.md), with monomer feedstocks from [Petrochemicals](../polymers/index.md)
- **Solvent recovery**: PGMEA and ethyl lactate can be reclaimed by fractional distillation for reuse, reducing cost and waste stream. Acetone recovery similarly practical.

## Mask Making
- **Mask blanks**: Fused quartz (synthetic silica) substrate, 6″×6″×0.25″ (152×152×6.35 mm), polished to λ/4 flatness. Chrome layer (80-100 nm sputtered Cr) provides opaque regions. Resist coated on top of chrome for patterning. Quartz is essential for i-line (365 nm) transmission — soda-lime glass absorbs below 350 nm.
- **1× masks (contact/proximity printing)**: Pattern generated at 1:1 scale. Photo-repeater: a precision X-Y stage positions a small aperture over the mask blank; a single pattern feature is exposed, then the stage steps to the next position. Repeats the same pattern across the entire mask. Alignment marks exposed at the same time. Resolution limited to ~2-3 μm due to 1:1 imaging.
- **4×/5× reticles (projection steppers)**: Pattern drawn at 4× or 5× final size on the reticle. Stepper optics reduce to 1× on wafer. Allows higher mask resolution and easier defect management. Written by electron-beam (e-beam) lithography: focused 10-30 keV electron beam raster-scans the resist on the chrome. Spot size 10-50 nm. Write time: 1-8 hours per reticle depending on pattern density.
- **Mask inspection**: Die-to-die comparison (compare two identical pattern areas on same mask — any difference is a defect) or die-to-database (compare mask pattern against design data — detects both defects and dimensional errors). Inspection sensitivity: 0.25-1.0× minimum feature size.
- **Mask repair**: Focused ion beam (FIB) — Ga⁺ ions sputter-remove chrome bridges (clear defects) or deposit carbon patches to fill missing chrome (opaque defects). Laser repair for larger defects. Repaired masks are re-inspected. Yield: a good 1× mask is critical — one defect repeats on every die.
- **Pellicles**: Thin transparent membrane (nitrocellulose ~1 μm thick, or fluoropolymer such as CYTOP) mounted on an aluminum frame (5-10 mm standoff height above mask surface). Seals the mask pattern area — any particle that lands on the pellicle is far enough above the mask plane to be out of focus and not print. Pellicle must transmit >99% at exposure wavelength. Replaceable when damaged. Essential for production masks; omit for development or low-volume work.

**Strengths**:
- E-beam mask writing at 10-50 nm spot size enables 4×/5× reticles with features far smaller than optical lithography limits
- Pellicle membrane keeps particles 5-10 mm above mask plane — out of depth of focus, so they don't print as defects

**Weaknesses**:
- E-beam write time of 1-8 hours per reticle makes masks expensive ($5K-50K each)
- FIB mask repair introduces Ga⁺ contamination and ≤10 nm substrate damage — repaired sites have slightly different optical properties

## Lithography Tools
- **Contact/proximity printing**: Mask touches (or nearly touches) wafer → UV exposure
  - Simple but damages mask and wafer. Proximity gap of 10-50 μm reduces damage at cost of resolution loss (near-field diffraction limits minimum feature to ~√(λ × gap) ≈ 2-5 μm for 20 μm gap at i-line).
- **Projection printing**: Lens projects mask image onto wafer
  - Requires good optics (from the Vacuum & Optics stage). Resolution ≈ k₁·λ/NA where k₁ ≈ 0.5-0.8 (process factor), λ is wavelength, NA is numerical aperture.
- **Mercury arc lamp**: Discharge in high-pressure mercury vapor inside quartz envelope. Emission lines: g-line (436 nm), h-line (405 nm), i-line (365 nm). I-line preferred for sub-micron lithography (shorter wavelength = better resolution). Lamp power 350-1000 W, lifetime ~1000 hours. Intensity monitoring required — dose control is ±2% for critical layers.
- **Numerical aperture (NA)**: NA = n·sin(θ) where n is medium refractive index (air: 1.0, immersion fluid: 1.44 for water) and θ is half-angle of light cone. Higher NA = better resolution but shallower depth of focus. Typical projection lenses: NA 0.28-0.60 for i-line steppers.
- **Step-and-repeat stage mechanics**: Precision X-Y stage with laser interferometer position feedback (resolution λ/1000 ≈ 0.6 nm for HeNe laser). Wafer held by vacuum chuck on stage. Stage moves wafer to each exposure field, settles (vibration <50 nm), exposes, steps to next field. Throughput: 20-60 wafers/hour depending on field size and exposure dose. Stage leveling: autolevel sensors map wafer height at each field to maintain focus.
- **Alignment marks**: Patterns etched into wafer at first lithography level (typically a cross, bar-in-bar, or grating structure). Subsequent layers align to these marks using alignment microscopes with video image processing. Overlay tolerance: typically 1/3 to 1/5 of minimum feature size (e.g., ±0.2 μm for 1 μm features). Global alignment (two marks per wafer) vs. field-by-field alignment (marks in every die — more accurate but slower).
- **Focus and depth of focus (DoF)**: DoF ≈ ±k₂·λ/NA² where k₂ ≈ 0.5-1.0. For i-line (365 nm) at NA 0.45: DoF ≈ ±1.8 μm. Gate-level lithography requires tight focus control — any wafer topography or tilt degrades critical dimension uniformity. Auto-focus systems (air gauge or optical) compensate at each exposure field.
- **Coherence and standing waves**: Partial coherence of illumination (σ parameter, typically 0.5-0.7) controls the balance between resolution and standing-wave interference effects in the resist. Standing waves cause linewidth rippling on sidewalls — mitigated by post-exposure bake (PEB) which promotes acid diffusion and smooths the profile.

**Strengths**:
- Projection printing with NA 0.28-0.60 achieves sub-micron resolution via the Rayleigh criterion (k₁·λ/NA)
- Laser interferometer stage positioning with λ/1000 ≈ 0.6 nm resolution enables precise step-and-repeat exposure

**Weaknesses**:
- Depth of focus shrinks as NA increases (DoF ≈ ±k₂·λ/NA²) — requires flatter wafers and better autofocus
- Mercury arc lamps degrade ~10% per 100 hours and risk catastrophic envelope rupture releasing mercury

## Resist Stripping

After pattern transfer (etch or implant), photoresist must be removed before the next process step. Stripping method depends on whether the resist has been hard-baked, plasma-etched, or implanted (crosslinked resist is much harder to remove). Incomplete resist removal is a common yield killer — residue particles cause defects in subsequent deposition and etch steps.
- **Oxygen plasma ashing**: RF plasma (13.56 MHz, 100-500 W, O₂ flow 50-200 sccm, 0.5-2 Torr, 150-300°C). Oxygen radicals oxidize resist to CO₂ + H₂O (volatile products). Removes ~1-5 μm/min depending on conditions. Dry process — no liquid waste. Typically used as first step to remove bulk resist, followed by wet clean for residue.
- **Piranha solution**: H₂SO₄:H₂O₂ at 3:1 ratio (add peroxide slowly to sulfuric acid — vigorous exotherm, temperature reaches 100-130°C). Attacks organic material aggressively. Dissolves resist and removes metallic contaminants. Use immediately after mixing (peroxide decomposes rapidly). Extremely dangerous — burns skin on contact, can cause explosions if mixed with organics. Always add peroxide TO acid, never reverse.
- **Acetone**: For non-crosslinked resist (resist that has not been severely hard-baked or plasma-damaged). Soak 5-10 min at room temperature or 50°C. Acetone swells and dissolves the resin. Follow with IPA rinse (acetone leaves residue) and N₂ dry. Cannot remove hard-baked or plasma-crosslinked resist.
- **Standard strip sequence**: Oxygen plasma ash (remove bulk) → piranha clean (remove residue and metals) → DI water rinse → N₂ dry. For non-critical steps: acetone → IPA → N₂ dry.
- **Safety notes**: Piranha solution is the most dangerous wet chemical in the fab. Mix only in dedicated fume hood with acid-resistant PPE (face shield, acid gloves, apron). Never store piranha — decompose with excess water before disposal. Oxygen plasma equipment requires proper RF grounding and O₂ leak detection. Acetone and IPA are fire hazards — no ignition sources, use in ventilated areas.

**Strengths**:
- Oxygen plasma ashing removes bulk resist at 1-5 μm/min as volatile CO₂ + H₂O — no liquid waste stream
- Standard ash → piranha → rinse sequence removes all resist types including heavily crosslinked post-implant crust

**Weaknesses**:
- Piranha solution (H₂SO₄:H₂O₂ 3:1) reaches 100-130°C and can explode on contact with organics — the most dangerous wet chemical in the fab
- Acetone cannot remove hard-baked or plasma-crosslinked resist — limited to non-critical stripping only

## Hazards & Safety

- **PGMEA developer / ethyl lactate carrier**: Both cause respiratory and eye irritation at concentrations above 50 ppm. Use in ventilated wet benches with local exhaust. Wear nitrile gloves and safety glasses. Prolonged skin contact causes defatting and dermatitis.
- **Dichromate toxicity**: Ammonium dichromate ((NH₄)₂Cr₂O₇) contains Cr(VI), a confirmed human carcinogen (lung, nasal sinus). Inhalation of dust or mist is the primary route. If dichromated-gelatin resists are used for mask blanks, handle powder in a fume hood with particulate respirator (P100). Substitute novolac/DNQ resists whenever possible to eliminate chromium exposure entirely.
- **Mercury UV lamps**: High-pressure mercury arc lamps emit intense UV (g-line 436 nm through deep UV) and generate ozone. Enclose lamp housings completely; interlock covers so lamp cannot operate with housing open. Replace lamps at rated lifetime (~1000 hours) — aging lamps risk envelope rupture and mercury release. Mercury spill protocol: evacuate area, use mercury spill kit (sulfur powder or zinc dust), never vacuum.
- **Piranha solution** (H₂SO₄:H₂O₂ 3:1): The most dangerous wet chemical in photoresist stripping. Mix only in dedicated fume hood with acid-resistant PPE (face shield, heavy-duty acid gloves, chemical apron). Always add peroxide TO acid, never reverse — violent exotherm can cause boiling and spattering. Never store — decompose with excess water before disposal. Contact with organics can cause explosion.
- **Photoresist disposal**: Spent resist, developer, and rinse water containing dissolved organics are hazardous waste. Collect in labeled, compatible containers. Do not pour down any drain. PGMEA and ethyl lactate waste can be reclaimed by fractional distillation; contaminated waste must be incinerated by licensed hazardous-waste contractor.

## Positive Photoresist Chemistry

**Novolac-DNQ system in detail**:
- **Novolac resin**: A condensation polymer of m-cresol (or a mixture of m-cresol and p-cresol) with formaldehyde. The cresol-formaldehyde ratio and reaction conditions control molecular weight (target: 2,000-5,000 Da). Novolac is soluble in aqueous base on its own. The dissolution rate in TMAH developer is high (~100-500 nm/s).
- **DNQ (diazonaphthoquinone sulfonate)**: Attached to the novolac as a dissolution inhibitor. DNQ is a hydrophobic molecule that suppresses the novolac dissolution rate by 100-1000×. Unexposed resist: DNQ inhibits → does not dissolve. After UV exposure: DNQ undergoes Wolff rearrangement to form indene carboxylic acid (ICA), which is hydrophilic and actually accelerates dissolution of the novolac matrix.
- **Developer**: 2.38% TMAH (tetramethylammonium hydroxide) in water. This is the industry-standard developer for i-line and g-line resists. TMAH is preferred over NaOH or KOH because sodium and potassium ions contaminate MOS gate oxides (mobile ion contamination shifts threshold voltage). TMAH is an organic base that leaves no metallic contamination.
- **Resolution**: 0.25-1.0 μm with i-line (365 nm) exposure, depending on NA and process optimization. The theoretical limit for i-line is ~0.25 μm (k₁ = 0.25 at NA 0.65), but practical production limits are 0.35-0.5 μm.
- **Contrast (γ)**: 2-4 for DNQ-novolac resists. Contrast determines how sharply the resist transitions from unexposed (not dissolved) to exposed (fully dissolved). Higher contrast → steeper sidewalls → better pattern transfer. γ is measured from the characteristic curve (normalized resist thickness remaining vs. log exposure dose).

**Strengths**:
- DNQ dissolution inhibitor provides 100-1000× dissolution rate contrast between exposed and unexposed regions — sharp pattern definition
- TMAH developer is metal-ion-free, eliminating Na/K contamination that shifts MOS threshold voltage

**Weaknesses**:
- Resolution limited to 0.25-1.0 μm with i-line (365 nm) — shorter wavelengths require different resist chemistry
- Novolac resin requires phenol-formaldehyde polymerization — organic chemistry infrastructure dependency

## Negative Photoresist Chemistry

**SU-8 thick resist**:
- **Composition**: Epoxy novolac resin (average 8 epoxy groups per molecule — the source of the name "SU-8") + triarylsulfonium salt photoacid generator (PAG). The PAG generates a strong acid (HF or HSbF₆) upon UV exposure.
- **Exposure and PEB**: UV exposure generates acid at each exposed location. During PEB (post-exposure bake, 95°C, 1-5 min), the acid catalyzes cross-linking of the epoxy groups. Each acid molecule participates in many cross-linking reactions (chemical amplification — one photon generates one acid, which catalyzes many bonds). This makes SU-8 extremely sensitive despite its thick films.
- **Thick film capability**: 5-500 μm in a single spin coat by adjusting viscosity (solids content 50-85% in cyclopentanone or gamma-butyrolactone). Used for MEMS structures, microfluidic channels, electroplating molds. Thick films require extended exposure dose (100-500 mJ/cm² at 365 nm for 100 μm film).
- **Limitations**: Swelling during development (organic developer: propylene glycol methyl ether acetate, PGMEA) distorts fine features. Internal stress from cross-linking can cause cracked films on thick coatings. Difficult to strip after cross-linking (requires hot NMP or plasma ashing at high power). Minimum resolution: ~2 μm for thin films, degrades to 10-20 μm for films >100 μm thick.

**Historical isoprene-based negative resist** (KTFR-type):
- **Composition**: Cyclized polyisoprene (synthetic rubber) + bis-azide photosensitizer. Upon UV exposure, bis-azide photolyzes to form nitrene radicals, which cross-link the rubber chains at random points. Cross-linked rubber is insoluble in xylene developer.
- **Swelling problem**: During development, the developer (xylene) penetrates and swells the un-crosslinked resist. When the resist is rinsed (IPA or heptane), it shrinks back, but the pattern dimensions have shifted. This swelling limits resolution to ~2-3 μm and causes pattern distortion in dense features. The shift from negative to positive resists in the 1970s was driven primarily by this swelling limitation.

**Strengths**:
- SU-8 chemical amplification provides extreme sensitivity — one photon triggers 100-1000 cross-linking reactions
- SU-8 patterns 5-500 μm thick films in a single coat — unmatched for MEMS structures and electroplating molds

**Weaknesses**:
- SU-8 swelling during PGMEA development distorts features below ~2 μm and degrades to 10-20 μm resolution for films >100 μm
- Isoprene-based negative resists suffer xylene swelling that limits resolution to ~2-3 μm — replaced by positive resists in 1970s

## Resist Processing Parameters

**Spin coating physics**:
- **Thickness relationship**: t ∝ 1/√ω, where t is film thickness and ω is angular velocity. Doubling spin speed reduces thickness by ~30% (1/√2). For a given resist viscosity η and spin speed ω: t ≈ k × (η/ω)^(1/2), where k is a constant depending on resist solids content and evaporation rate.
- **Typical parameters**: 1000 RPM (thick coat, 3-5 μm), 3000 RPM (standard, 1.0-1.5 μm), 6000 RPM (thin coat, 0.5-0.8 μm). Ramp rate: 1000-5000 RPM/s acceleration. Slow ramp produces more uniform films but may allow edge bead buildup.
- **Edge bead**: Centrifugal force drives excess resist to the wafer edge, forming a thickened ring (edge bead) 2-5 mm wide. Edge bead removal (EBR): spray solvent (PGMEA or ethyl lactate) at the wafer edge while spinning at 500-1500 RPM. Removes the bead, preventing subsequent contact printing problems (edge bead holds the mask away from the wafer center).

**Soft bake optimization**:
- **Purpose**: Remove 80-90% of casting solvent from the resist film. Residual solvent causes adhesion failure and T-topping (incomplete exposure at the resist surface where dissolved oxygen quenches the photoreaction).
- **Temperature**: 90-110°C on a hot plate (the resist is in intimate contact with the hot plate surface for uniform heating). Oven baking is less uniform and takes 5-10× longer.
- **Time**: 60-120 seconds. Over-baking causes premature DNQ decomposition (reducing photospeed) and poor adhesion. Under-baking leaves too much solvent, causing development defects and bubble formation during exposure.
- **Uniformity**: ±1°C across the hot plate surface. Non-uniform baking creates development rate variations that translate into linewidth variation across the wafer.

**Exposure and development**:
- **Dose**: 50-200 mJ/cm² for i-line (365 nm) with standard DNQ-novolac resist. Dose depends on resist thickness (thicker resist absorbs more light, needs higher dose), substrate reflectivity (highly reflective substrates increase effective dose by reflecting light back through the resist), and feature size (small features diffract light and may receive less dose than large open areas).
- **Development time**: Puddle development: dispense developer onto stationary wafer, let stand 30-60 seconds, then spin dry. Over-development erodes resist sidewalls (CD loss). Under-development leaves scum (unexposed resist residue in cleared areas). Optimize by developing test wafers at varying times and measuring linewidth with a microscope.
- **Critical dimension (CD) control**: Target ±5-10% of nominal linewidth for production. CD depends on exposure dose, development time, bake temperatures, resist thickness, and substrate conditions. All must be controlled simultaneously.

**Strengths**:
- Spin coating thickness follows t ∝ 1/√ω — predictable and repeatable from 0.5-5 μm by adjusting spin speed
- Soft bake at 90-110°C for 60-90 seconds achieves ±1°C uniformity on hot plate — sufficient for CD control

**Weaknesses**:
- Edge bead requires separate EBR solvent spray step — adds process complexity
- CD depends on 6+ simultaneous parameters (dose, focus, resist thickness, development time, PEB temperature, reticle CD) — complex statistical process control required

## Mask Fabrication Detail

**Photomask blank manufacturing**:
- **Quartz substrate**: Synthetic fused silica, 152×152×6.35 mm (6"×6"×¼"), polished to λ/4 flatness (λ = 633 nm, so ~160 nm peak-to-valley surface deviation). Surface roughness <0.5 nm Ra. The substrate must transmit >90% at the exposure wavelength (i-line 365 nm). Soda-lime glass is NOT suitable because it absorbs below ~350 nm.
- **Chrome deposition**: Sputter 80-100 nm chromium film. Optical density >3.0 at 365 nm (blocks >99.9% of exposure light). Adhesion layer: 5-10 nm CrO₂ between chrome and quartz. Chrome must be uniform in thickness (±2 nm) for consistent optical density across the mask.
- **Resist coating**: Spin-coat electron-beam resist (positive tone: PMMA or ZEP-520A; or negative tone: HSQ — hydrogen silsesquioxane) on the chrome surface.

**Electron-beam writing**:
- **Principle**: Focused electron beam (10-50 keV) scans the resist-coated mask blank in a raster or vector pattern. The beam spot size (10-50 nm) determines minimum feature size on the mask. E-beam achieves much higher resolution than optical lithography because the electron wavelength (~0.005 nm at 30 keV) is far shorter than UV light.
- **Write time**: 1-8 hours per reticle, depending on pattern density and spot size. Dense patterns (memory chips) take longer than sparse patterns (analog circuits). The e-beam writes one pixel at a time, so write time scales with total pattern area.
- **Placement accuracy**: ±20 nm over the entire 100×100 mm pattern area. Achieved by interferometric stage position measurement (laser interferometer, λ/64 resolution ≈ 10 nm). Environmental control: temperature ±0.1°C, vibration isolation, magnetic shielding.

**Mask inspection and repair**:
- **Die-to-die comparison**: Compare two identical die patterns on the same mask using a scanning electron beam or UV microscope. Any difference between the two indicates a defect. Detects all defect types but requires two identical pattern areas on the mask.
- **Die-to-database comparison**: Compare the mask pattern against the design database (CAD data). Detects both defects and dimensional errors (CD variations). More comprehensive but requires precise registration between the inspection image and the design data. Minimum detectable defect size: ≥0.25 μm for advanced masks.
- **Focused ion beam (FIB) repair**: Ga⁺ ion beam at 30 keV. For opaque defects (extra chrome where it should be clear): Ga⁺ ions sputter-etch away the excess chrome. For clear defects (missing chrome): ion-beam-induced deposition of a carbon-based patch to fill the gap. Damage to the quartz substrate limited to ≤10 nm depth. Repaired sites are slightly higher or lower than the surrounding chrome, causing minor CD variation but vastly better than leaving the defect unrepaired.

**Strengths**:
- Fused silica mask substrate polished to λ/4 flatness with Cr optical density >3.0 — blocks >99.9% of exposure light
- E-beam placement accuracy of ±20 nm over 100×100 mm pattern area enables 4× reticles for sub-micron wafer features

**Weaknesses**:
- E-beam write time of 1-8 hours per reticle makes masks expensive and creates a throughput bottleneck
- FIB Ga⁺ repair introduces ion contamination and ≤10 nm substrate damage at repaired sites

## Lithography Process Optimization

**Focus-exposure matrix (FEM)**:
- **Purpose**: Determine the optimal exposure dose and focus setting for each lithography layer. The FEM is the most critical characterization experiment in lithography process development.
- **Method**: Expose a matrix of fields on a test wafer, varying exposure dose in one axis and focus offset in the other. Typical ranges: dose 50-200 mJ/cm² in 10-20 steps, focus -2.0 to +2.0 μm in 0.2-0.4 μm steps. After development, measure critical dimensions (CD) at each field.
- **Bossung curve**: Plot CD vs. dose at each focus setting. The "sweet spot" is the dose and focus combination where CD changes least with small perturbations (maximum process window). At the optimal dose, the resist image is most tolerant of focus and exposure variations that inevitably occur in production.
- **Depth of focus (DoF)**: The range of focus positions where CD remains within specification (typically ±10% of target). For i-line (365 nm) at NA 0.50: DoF ≈ ±1.0 μm. The DoF shrinks with increasing NA and decreasing wavelength, which is why shorter-wavelength lithography requires flatter wafers and better autofocus systems.

**Critical dimension (CD) control**:
- **Sources of CD variation**: Exposure dose non-uniformity (±2% across field), focus variation (±0.2 μm wafer flatness, ±0.1 μm stage leveling), resist thickness variation (±2 nm), development time variation (±2 seconds), post-exposure bake temperature (±1°C), reticle CD error (±20 nm). All contribute to total CD budget.
- **CD budget allocation**: For a 1.0 μm feature with ±10% tolerance (900-1100 nm), the total CD budget is 100 nm (3σ). Typical allocation: reticle errors 30 nm, exposure/focus 40 nm, resist processing 20 nm, etch bias 10 nm.
- **Statistical process control (SPC)**: Measure CD on sample wafers from each lot. Plot on X-bar and R charts. Investigate any point outside control limits (±3σ) or showing a trend (7 points in a row on one side of the mean). CD data drives reticle requalification, equipment maintenance, and process adjustments.

**Overlay registration**:
- **Measurement**: Optical overlay metrology tool measures alignment mark position on the wafer and compares to design coordinates. Reports overlay error as (dX, dY) at each measurement site, typically at 10-20 sites per wafer.
- **Sources of overlay error**: Reticle placement error (±20 nm), stage positioning error (±10 nm with laser interferometer), lens distortion (±30 nm across the field), wafer distortion (thermal expansion, stress from deposited films).
- **Correction**: Modern steppers apply intra-field corrections (grid scaling, rotation, lens distortion correction) and inter-field corrections (wafer scaling, rotation, translation) based on overlay measurements from a calibration wafer. Residual overlay error after correction: ±30-50 nm for i-line steppers.

**Strengths**:
- Focus-exposure matrix (FEM) identifies the process "sweet spot" where CD is most tolerant of dose and focus variations
- SPC with X-bar and R charts catches CD drift before it impacts production yield

**Weaknesses**:
- DoF of only ±1.0 μm for i-line at NA 0.50 — any wafer topography or tilt degrades CD uniformity
- CD budget of 100 nm (3σ) for 1.0 μm features must be allocated across 6+ error sources, leaving thin margins

## Defect Density and Yield

**Yield model**: Yield = (1 - D·A)ⁿ, where D = defect density (defects/cm² per layer), A = die area (cm²), n = number of critical lithography layers. For a die of 0.5 cm² with 7 critical layers and a defect density of 0.5 defects/cm² per layer: Yield = (1 - 0.5 × 0.5)⁷ = (0.75)⁷ = 0.133 = 13.3%. Reducing defect density to 0.1/cm² per layer: Yield = (0.95)⁷ = 0.698 = 69.8%. This exponential relationship between defect density and yield is why cleanroom discipline and contamination control are so important.

**Defect sources by type**:
- **Particles**: Largest category. Sources: people, process chemicals, equipment wear, wafer handling. Detected by laser scattering inspection. Prevented by: cleanroom protocols, point-of-use chemical filtration (0.05-0.2 μm filters on all process chemicals), clean wafer handling (vacuum wands, not manual).
- **Pattern defects**: Missing features, bridges, CD errors. Sources: reticle defects, focus/exposure errors, resist scumming. Detected by die-to-die inspection of patterned wafers. Prevented by: reticle inspection and repair, FEM optimization, proper development.
- **Scratches**: Mechanical damage from wafer handling, probing, or cassette transfer. Detected by visual inspection and scatterometry. Prevented by: proper wafer handling procedures, clean cassette maintenance.

**Strengths**:
- Yield model (1 - D·A)ⁿ provides clear quantitative link between defect density and profitability — drives investment in contamination control
- Reducing defect density from 0.5 to 0.1/cm² per layer improves yield from 13% to 70% for a 7-layer process — enormous economic incentive

**Weaknesses**:
- Exponential yield model means each additional lithography layer multiplies yield loss — 7 critical layers is already challenging
- Defect density is cumulative across all process steps — contamination from any single step degrades overall yield

## Lithography Equipment Maintenance

**Mercury lamp maintenance**:
- **Lifetime tracking**: Mercury arc lamps degrade with use. Output intensity drops ~10% per 100 hours of operation. Replace at manufacturer-rated lifetime (typically 800-1200 hours) or when intensity drops below the process minimum (established during qualification). A lamp that fails catastrophically (envelope rupture) releases mercury into the exposure tool housing, requiring extensive cleanup.
- **Replacement procedure**: Power down and cool lamp housing (lamp surface reaches >600°C during operation; wait 30+ minutes). Remove old lamp, clean housing interior with IPA. Install new lamp with cotton gloves (skin oils on the quartz envelope create hot spots that cause premature failure). Align lamp in the reflector (eccentricity <0.5 mm). Power up and re-calibrate intensity. Log lamp serial number and installation date.
- **Intensity recalibration**: After lamp replacement, re-measure exposure intensity at the wafer plane with a calibrated radiometer. Adjust exposure time or dose to compensate for any change. Re-qualify CD on a test wafer before resuming production.

**Lens care**:
- **Contamination**: Projection lenses are multi-element glass assemblies costing $100K-$1M+. Any contamination on the lens surface (outgassed organics, resist volatiles, water spots) degrades image quality. Lenses are enclosed in a sealed barrel with dry nitrogen purge to prevent contamination and moisture absorption (some lens glasses are hygroscopic).
- **Cleaning**: Never touch lens surfaces. If cleaning is required, use lens tissue with reagent-grade acetone in a gentle single-wipe motion (no rubbing). Inspect with a collimated light source at grazing angle to detect films and particles.
- **Environmental control**: Lens performance varies with temperature and atmospheric pressure (refractive index of air changes). Temperature-controlled lens barrel maintains ±0.1°C. Barometric pressure changes compensated by adjusting the distance between lens elements (focus adjustment).

**Stage calibration**:
- **Laser interferometer alignment**: The X-Y stage position is measured by reflecting a HeNe laser beam off mirrors attached to the stage. Interference fringes count stage position with λ/4 resolution (~158 nm for 633 nm HeNe). The interferometer beams must be aligned parallel to the stage travel direction within ±5 arc-seconds, or cosine error accumulates over long travels. Realign after any stage maintenance or mechanical shock.
- **Stage flatness mapping**: Use an autocollimator or capacitive probe to map the stage surface flatness across the entire travel range. Deviation from flat causes focus errors. Shim the stage mounting points to correct tilt. Re-map after any mechanical adjustment.

**Strengths**:
- Laser interferometer stage positioning at λ/4 ≈ 158 nm resolution provides repeatable field-to-field placement
- Nitrogen-purged lens barrel at ±0.1°C prevents contamination and refractive index drift in $100K-$1M projection optics

**Weaknesses**:
- Mercury lamp replacement every 800-1200 hours requires 30+ minute cooldown, lamp alignment, and intensity recalibration
- Lens cleaning risks damaging $100K-$1M optics — single-wipe-only protocol with no rubbing allowed

## Alignment and Overlay Control

**Alignment mark design**:
- **Marks must survive all process steps** from first lithography through final passivation. Choose mark structures in areas that will not be covered by opaque metal layers. Common design: a cross-in-box pattern (a cross etched into the wafer, surrounded by a rectangular frame, also etched) at the first lithography level. Subsequent layers have matching cross-in-box patterns that overlay on the original marks.
- **Mark clarity**: Alignment marks degrade with each process step (oxidation rounds sharp corners, etch undercuts features, deposition fills trenches). Design marks with feature sizes 5-10× larger than minimum circuit features (e.g., 5 μm mark lines for 0.5 μm circuit features) so they remain readable after degradation.
- **Mark placement**: Global alignment marks (2-4 per wafer) at the wafer edge, outside the die area. Local alignment marks (in each die) for field-by-field alignment (more accurate but slower). The choice depends on overlay tolerance requirements.

**Overlay error compensation**:
- **Grid correction**: Measure overlay at multiple points on a calibration wafer. Compute the best-fit grid correction (translation, rotation, scaling) and apply to all subsequent wafers in the lot. Reduces systematic overlay errors (reticle scaling error, stage scaling error) to residual random errors.
- **Inter-field correction**: Apply different corrections at each exposure field on the wafer. Compensates for wafer-level distortions (thermal expansion non-uniformity, film stress gradients). Requires an enhanced global alignment (EGA) measurement step where overlay is measured at ~20 points across the wafer, then the correction model is computed and applied to each field individually.

**Process window qualification**:
- **CD vs. pitch**: Measure CD at different pitches (line width vs. space width) to verify that dense and isolated features print at the same size. Dense features receive less exposure due to diffraction effects, while isolated features receive more. The difference is "proximity effect." Correct by optical proximity correction (OPC) on the reticle (adding serifs or hammerheads to feature corners to compensate for the optical diffraction that rounds them during exposure).
- **Process window analysis**: Vary exposure dose and focus on a test reticle containing dense, isolated, and minimum-size features. For each feature type, determine the dose/focus region where CD is within specification. The intersection of all individual process windows is the common process window. If the common window is too small, process adjustments are needed (different NA, illumination mode, or resist process).

**Strengths**:
- Grid correction (translation, rotation, scaling) from calibration wafer measurements reduces systematic overlay errors to ±30-50 nm residual
- OPC on reticles compensates for proximity effect — dense and isolated features print at the same CD

**Weaknesses**:
- Alignment marks degrade with each process step (oxidation, etch, deposition) — must be designed 5-10× larger than minimum features
- Common process window shrinks as feature sizes decrease — tighter tolerance on all parameters simultaneously

## Photoresist Stripper Chemistry

**Resist removal after high-dose implant or plasma etch**:
- Heavily crosslinked resist (from ion implantation at >10¹⁵ ions/cm², or from extended plasma etching with polymerizing chemistries) becomes essentially a carbonaceous glass. Standard solvents cannot dissolve it. Oxygen plasma ashing removes the bulk, but a thin carbon-rich crust remains.
- **[Piranha clean](../glossary/piranha-clean.md)** (H₂SO₄:H₂O₂ 3:1 to 4:1): The most aggressive organic removal chemistry available. The mixture generates persulfuric acid (Caro's acid, H₂SO₅), a powerful oxidizer that attacks even heavily crosslinked carbon. Temperature: 100-130°C (exothermic mixing provides the heat). Immersion time: 10-30 minutes for heavily crosslinked resist. Must be used in a dedicated acid fume hood with acid-resistant plumbing (Piranha attacks most organic drain materials). Never store: decompose by slow dilution with cold water before disposal.
- **Downstream plasma ash**: Remote plasma (oxygen plasma generated upstream, neutral oxygen radicals flow to the wafer without ion bombardment). Gentler than direct plasma ashing (no physical damage to underlying films). Used as a pre-clean before Piranha to remove the bulk of the resist, reducing Piranha consumption and extending bath life.

**Strengths**:
- Piranha (H₂SO₄:H₂O₂ 3:1) generates persulfuric acid that attacks even heavily crosslinked carbon crust — the most aggressive organic removal available
- Downstream plasma ash removes bulk resist without ion bombardment damage to underlying films

**Weaknesses**:
- Piranha attacks most organic drain materials — requires dedicated acid-resistant plumbing and fume hood
- Piranha must be decomposed by slow dilution with cold water before disposal — cannot be stored

## Chemically Amplified Resists (CAR)

**Principle**: Developed for deep UV (DUV) lithography at 248 nm (KrF excimer) and 193 nm (ArF excimer) wavelengths. A photoacid generator (PAG, typically triphenylsulfonium or onium salt) absorbs a photon and releases a strong acid (e.g., HSbF₆, HBF₄). During post-exposure bake (PEB), the acid catalyzes deprotection of the resist polymer — each acid molecule participates in 100-1000 deprotection reactions before being consumed. This chemical amplification means one photon triggers many chemical events, dramatically increasing sensitivity. CAR sensitivity: 10-50 mJ/cm² versus 100-200 mJ/cm² for conventional DNQ-novolac resists at comparable wavelengths. The amplified reaction chain also improves contrast (γ = 5-15) because the amplification is highly nonlinear — a small dose difference produces a large solubility change.

**PAG concentration**: 5-15% by weight in the resist formulation. Higher PAG loading increases sensitivity but reduces etch resistance (PAG molecules displace the carbon-rich polymer that provides plasma resistance). Trade-off: sensitivity vs. etch selectivity. Typical PAG loading is optimized at 8-10% for production resists.

**Environmental stability**: CAR resists are sensitive to airborne basic contaminants (amines, ammonia, NMP). Even ppb-level amine contamination neutralizes the photogenerated acid at the resist surface, causing "T-topping" — a narrowed resist profile at the top. Solution: amine-free cleanroom air (chemical filtration with activated carbon or citric acid-impregnated filters), sealed resist bottles, and minimal air exposure between coating and PEB.

**Strengths**:
- Chemical amplification provides 10-50 mJ/cm² sensitivity vs. 100-200 mJ/cm² for DNQ-novolac — 4-10× faster exposure
- CAR contrast (γ = 5-15) is much higher than DNQ-novolac (γ = 2-4) — steeper sidewalls for better pattern transfer

**Weaknesses**:
- Ppb-level airborne amines neutralize photogenerated acid, causing T-topping — requires chemical filtration in cleanroom air
- PAG loading trades sensitivity against etch resistance — higher PAG reduces plasma resistance

## Multilayer Resist Systems

**Bottom anti-reflective coating (BARC)**: A thin organic or inorganic layer (30-80 nm) spun onto the wafer before photoresist. BARC absorbs exposure light that passes through the resist, preventing reflection from the substrate. Without BARC, reflected light creates standing wave interference in the resist, causing linewidth rippling on sidewalls and swing curves (periodic CD variation with resist thickness). BARC optical properties: refractive index n and extinction coefficient k tuned so that reflected light from the BARC-substrate interface cancels by destructive interference. BARC is removed during the plasma etch that transfers the resist pattern to the underlying film — it etches at a controlled rate relative to the resist (etch selectivity 1:1 to 2:1).

**Top coat for immersion lithography**: At 193 nm immersion, water fills the gap between the projection lens and the wafer. The top coat is a thin (30-90 nm) hydrophobic polymer layer spun onto the resist surface to prevent water from leaching resist components (PAG, solvent) into the immersion fluid. Top coat contact angle with water: 70-90° (hydrophobic enough to prevent water residues, wettable enough for uniform water meniscus during scanning). After exposure, the top coat is stripped in developer or a separate solvent before development of the underlying resist.

**Strengths**:
- BARC eliminates standing wave interference and swing curves — dramatically improves CD uniformity across varying substrate reflectivities
- Immersion top coat prevents PAG leaching into water, protecting both resist performance and lens contamination

**Weaknesses**:
- BARC adds an extra spin-coat step and must be removed during pattern transfer etch — added process complexity
- Top coat must balance hydrophobicity (70-90° contact angle) with developer strippability — narrow formulation window

## Pellicle Detail

**Construction**: A thin transparent membrane stretched taut over an aluminum frame (5-10 mm standoff height above the mask chrome surface). Two pellicle materials are common: (1) nitride membrane, ~800 nm thick, for i-line and g-line exposure — silicon nitride deposited by LPCVD on a silicon carrier, then released by etching the carrier away; (2) fluoropolymer membrane (CYTOP or Teflon AF), ~2.8 μm thick, for DUV wavelengths where nitride absorbs too strongly. Both achieve >99% transmission at their designed exposure wavelength.

**Function**: Any particle landing on the pellicle membrane is 5-10 mm above the mask plane — well outside the depth of focus of the projection optics. The particle is blurred to invisibility on the wafer image and does not print as a defect. Without a pellicle, a single 1 μm particle on the mask would repeat as a defect on every die across the wafer.

**Lifetime and replacement**: Pellicle membranes degrade under prolonged UV exposure (photolysis and ozone attack). Rated lifetime: ~10,000 exposure cycles for i-line nitride pellicles. Inspect pellicles before each production run for tears, wrinkles, or accumulated particles. Replace damaged pellicles immediately — a torn pellicle provides zero protection.

**Strengths**:
- Pellicle keeps particles 5-10 mm above mask plane — out of depth of focus, so they don't print as repeating defects on every die
- >99% transmission at exposure wavelength means no measurable light loss in the imaging path

**Weaknesses**:
- Nitride pellicles absorb at DUV wavelengths, requiring fluoropolymer alternatives — additional material supply chain
- Rated lifetime of ~10,000 cycles means pellicles are consumables requiring regular inspection and replacement

## Advanced Mask Inspection and Repair

**Actinic inspection**: Die-to-die comparison at the exposure wavelength (actinic inspection) catches defects that would print on the wafer but might be invisible at other inspection wavelengths. KLA/Tencor systems scan at 1-5 cm²/min with sensitivity down to 50 nm defects on 4× reticles. The tool compares transmitted and reflected light images from two adjacent die sites on the mask; any difference exceeding the detection threshold flags as a defect. Actinic inspection is slower than broadband brightfield but catches wavelength-specific printing failures that other methods miss.

**Mask repair precision**: FIB systems using Ga⁺ ions at 30 keV sputter-remove chrome opaque defects with 10 nm precision. For clear defects, electron beam induced deposition (EBID) builds up a carbon-containing patch from a precursor gas to fill the gap. Post-repair inspection verifies each repair site meets quality requirements with ≤10 nm placement error relative to the intended mask geometry. Repaired sites have slightly different optical density than original chrome, causing minor CD variation, but this is always preferable to leaving the defect unrepaired.

**Strengths**:
- Actinic inspection at exposure wavelength catches defects that would print but are invisible at other wavelengths
- FIB repair achieves 10 nm precision with ≤10 nm placement error — makes otherwise scrap masks usable

**Weaknesses**:
- Actinic inspection at 1-5 cm²/min is slow — full reticle inspection takes 30-60 minutes
- Repaired sites have slightly different optical density than original chrome, causing minor but measurable CD variation
## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Resist pattern T-topping — narrowed profile at top of resist | Airborne amine contamination (NMP, ammonia) neutralizing photogenerated acid at resist surface during CAR exposure; chemical filtration failed | Replace activated carbon filters in cleanroom air recirculation; maintain amine concentration <1 ppb in litho bay; minimize time between resist coat and PEB; verify sealed resist bottles are not left open |
| CD variation exceeds ±10% across wafer — 100 nm (3σ) on 1.0 μm features | Exposure dose non-uniformity ±2% across field; hot plate soft bake temperature variation >±1°C; development time tolerance ±2 seconds exceeded | Recalibrate exposure dose uniformity at wafer plane with radiometer; verify hot plate uniformity at ±1°C; optimize puddle development time with test wafer matrix; re-run FEM to find process sweet spot |
| Resist adhesion failure — lifting during wet etch in BHF | Soft bake temperature too high (>110°C) causing premature DNQ decomposition; insufficient dehydration bake before spin coat; contaminated wafer surface | Soft bake at 90-110°C for 60-90 seconds on hot plate; add HMDS (hexamethyldisilazane) prime step before resist coating to promote adhesion; verify wafer surface is clean (RCA clean immediately before resist coat) |
| SU-8 thick film cracking after PEB at 95°C | Internal stress from epoxy cross-linking exceeds adhesion strength; rapid thermal ramp during PEB; film thickness >200 μm on rigid substrate | Reduce PEB ramp rate to 1-2°C/min; use multi-step PEB (65°C → 95°C gradual transition); reduce film thickness or apply to substrate with matched CTE; verify PEB duration is 1-5 min not exceeded |
| Pellicle membrane torn — repeating particle defects on every die | Pellicle exceeded rated lifetime of ~10,000 exposure cycles; mechanical contact during mask handling; UV photolysis degraded nitride membrane | Replace pellicle immediately; inspect handling procedures for mechanical contact; track exposure cycle count per mask; use fluoropolymer (CYTOP ~2.8 μm) pellicles for DUV wavelengths where nitride absorbs |
| Mask chrome optical density below 3.0 at 365 nm — faint image on wafer | Chrome layer (80-100 nm) non-uniform or too thin from sputtering; CrO₂ adhesion layer degraded; chrome etched during resist strip | Re-sputter chrome to 80-100 nm target with ±2 nm uniformity; verify CrO₂ adhesion layer (5-10 nm); use oxygen plasma ashing for resist removal instead of wet strip that attacks chrome; measure OD with densitometer before release |
| Focus-exposure matrix shows no common process window for dense and isolated features | Depth of focus only ±1.0 μm at i-line NA 0.50; proximity effect causes dense lines to print differently than isolated; insufficient OPC on reticle | Apply OPC (serifs on corners, hammerheads on line ends) to reticle; reduce NA slightly for larger DoF; adjust partial coherence σ toward 0.5-0.7; if still no common window, split into separate exposures for dense and isolated features |
| Alignment marks unreadable after 4+ process layers | Mark features (designed at circuit minimum size) degraded by oxidation rounding corners, etch undercut, and deposition filling trenches | Redesign alignment marks 5-10× larger than minimum circuit features (e.g., 5 μm mark lines for 0.5 μm circuit features); use marks in areas protected from metal deposition; verify mark visibility at each process step with alignment microscope |
| Mercury lamp intensity drops >10% between replacements — CD shift on production wafers | Lamp approaching 800-1200 hour rated lifetime; output drops ~10% per 100 hours; radiometer calibration drifted | Track lamp hours and replace at rated lifetime; recalibrate radiometer after each lamp replacement; adjust exposure time to compensate for measured intensity drop; re-qualify CD on test wafer before production resume |
| Piranha solution (H₂SO₄:H₂O₂ 3:1) temperature exceeds 130°C — violent boiling | Adding peroxide too quickly to sulfuric acid; using warm H₂SO₄; ratio exceeded (too much H₂O₂) | Always add H₂O₂ slowly to H₂SO₄ (never reverse); use room-temperature acid; maintain 3:1 ratio precisely; mix in dedicated acid fume hood with face shield and acid-resistant PPE; decompose with cold water before disposal |

## See Also

- [Basic Glass](../glass/basic.md) — glass substrates for photomasks
- [Thermosets](../polymers/thermosets.md) — polymer chemistry for photoresists
- [Chemistry Index](../chemistry/index.md) — chemical synthesis fundamentals
- [Core Fab Processes](fab-processes.md) — lithography in the fab process flow
- [Cleanrooms](cleanrooms.md) — cleanroom requirements for lithography
- [Advanced Lithography](../vlsi-scaling/advanced-lithography.md) — DUV and EUV scaling
- [Photomask Substrates](../glass/photomask-substrates.md) — mask blank materials

[← Back to Photolithography](index.md)
