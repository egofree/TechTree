# Photoresists, Masks & Lithography

> **Node ID**: photolithography.resists-masks
> **Domain**: [Photolithography & IC Fabrication](./)
> **Dependencies**: `chemistry`, `polymers.thermosets`
> **Enables**: `vlsi-scaling.advanced-lithography`
> **Timeline**: Years 40-70
> **Outputs**: photoresists, masks, lithography_tools, patterned_wafers

### Photoresists

**Bitumen resist** (simplest, historical — Niépce, 1826):
- Dissolve bitumen of Judea (natural asphalt) in lavender oil or turpentine. Coat on substrate. Expose to UV through mask (hours of exposure — very slow). Exposed areas harden (polymerize), unexposed areas dissolve in solvent. Low resolution (~100 μm+), very slow, but requires zero chemistry infrastructure.

**Dichromated gelatin** (mid-19th century):
- Mix gelatin (from animal collagen) with ammonium dichromate ((NH₄)₂Cr₂O₇, ~5-10%). Coat on substrate. UV exposure causes Cr(VI) → Cr(III) reduction, cross-linking gelatin (insoluble). Unexposed gelatin washes away in warm water. Resolution ~10-50 μm. Chromium compounds are toxic and carcinogenic — handle with care.

**Novolac + DNQ resist** (standard positive-tone photoresist, requires the Chemistry stage organic chemistry):
- **Novolac resin**: Phenol + formaldehyde condensation polymer (m-cresol variant for photoresist). See [Polymers](../polymers/index.md) for production. Molecular weight ~2000-5000. Dissolves in aqueous base (NaOH or TMAH).
- **DNQ sensitizer**: Diazonaphthoquinone sulfonate (from naphthol + diazotization). ~20-30% by weight in resist. Function: DNQ acts as dissolution inhibitor — unexposed resist does NOT dissolve in developer. UV exposure → DNQ undergoes Wolff rearrangement → forms indene carboxylic acid → actually ENHANCES dissolution in aqueous base. This is the positive-tone mechanism.
- **Solvent**: Ethyl lactate or propylene glycol monomethyl ether acetate (PGMEA). ~60-80% of resist formulation.
- **Spin coating**: Dispense ~2-5 ml resist on wafer center. Spin at 1000-6000 RPM for 30-60 seconds. Centrifugal force spreads resist uniformly. Thickness: 0.5-3 μm (depends on viscosity and spin speed — roughly t ∝ 1/√ω). Edge bead removal (EBR): spray solvent at wafer edge while spinning to remove thick bead that forms at edge.
- **Soft bake (pre-bake)**: 90-110°C for 60-90 seconds on hot plate. Drives off solvent. Residual solvent <3%.
- **Exposure**: UV light (365 nm i-line, 405 nm h-line, or 436 nm g-line from mercury lamp). Dose: 50-200 mJ/cm². Exposed regions become soluble.
- **Post-exposure bake (PEB)**: 110-130°C for 60-90 seconds. Improves pattern definition by reducing standing wave effects.
- **Development**: Aqueous base — 2.38% TMAH (tetramethylammonium hydroxide) for 30-90 seconds with gentle agitation. TMAH preferred over NaOH (metal-ion-free developer — sodium contamination degrades MOS devices).
- **Hard bake**: 120-150°C for 60-120 seconds. Cross-links resist for etch resistance. Not always needed.

**Negative-tone resists** (exposed regions become insoluble):
- **SU-8** (epoxy-based, modern): Epoxy novolac resin + triarylsulfonium salt photoacid generator (PAG). UV exposure generates acid → PEB causes acid-catalyzed epoxy cross-linking. Highly cross-linked, excellent chemical resistance. Can pattern thick films (5-500 μm) in a single coat. Used for MEMS structures, thick passivation, electroplating molds. Resolution limited by swelling during development (~2-5 μm minimum for thin films).
- **Isoprene-based** (historical): Cyclized polyisoprene + bis-azide sensitizer. UV exposure causes azide to form nitrene radicals, cross-linking the rubber. Unexposed regions dissolve in xylene. Swelling during development limits resolution to ~2-3 μm. Historically important (Kodak KTFR, early IC production in 1960s-70s). Largely replaced by positive resists due to swelling artifacts.

### Polymer Packaging Materials
- **Epoxy encapsulation**: Two-part epoxy for die attach and hermetic sealing — see [Polymers](../polymers/index.md) and [Semiconductor Packaging & Testing](../chemistry/packaging-testing.md)
- **Plastic substrates and lead frames**: Molded plastic packages for integrated circuits
- **Phenolic laminate (FR-4)**: PCB substrate material from phenolic or epoxy resin impregnated glass fabric — see [Polymers](../polymers/index.md)
- **Photoresist dependency**: Novolac resin (phenol + formaldehyde condensation polymer) production path documented in [Polymers](../polymers/index.md), with monomer feedstocks from [Petrochemicals](../petrochemicals/petroleum-alternatives.md)
- **Solvent recovery**: PGMEA and ethyl lactate can be reclaimed by fractional distillation for reuse, reducing cost and waste stream. Acetone recovery similarly practical.

### Mask Making
- **Mask blanks**: Fused quartz (synthetic silica) substrate, 6″×6″×0.25″ (152×152×6.35 mm), polished to λ/4 flatness. Chrome layer (80-100 nm sputtered Cr) provides opaque regions. Resist coated on top of chrome for patterning. Quartz is essential for i-line (365 nm) transmission — soda-lime glass absorbs below 350 nm.
- **1× masks (contact/proximity printing)**: Pattern generated at 1:1 scale. Photo-repeater: a precision X-Y stage positions a small aperture over the mask blank; a single pattern feature is exposed, then the stage steps to the next position. Repeats the same pattern across the entire mask. Alignment marks exposed at the same time. Resolution limited to ~2-3 μm due to 1:1 imaging.
- **4×/5× reticles (projection steppers)**: Pattern drawn at 4× or 5× final size on the reticle. Stepper optics reduce to 1× on wafer. Allows higher mask resolution and easier defect management. Written by electron-beam (e-beam) lithography: focused 10-30 keV electron beam raster-scans the resist on the chrome. Spot size 10-50 nm. Write time: 1-8 hours per reticle depending on pattern density.
- **Mask inspection**: Die-to-die comparison (compare two identical pattern areas on same mask — any difference is a defect) or die-to-database (compare mask pattern against design data — detects both defects and dimensional errors). Inspection sensitivity: 0.25-1.0× minimum feature size.
- **Mask repair**: Focused ion beam (FIB) — Ga⁺ ions sputter-remove chrome bridges (clear defects) or deposit carbon patches to fill missing chrome (opaque defects). Laser repair for larger defects. Repaired masks are re-inspected. Yield: a good 1× mask is critical — one defect repeats on every die.
- **Pellicles**: Thin transparent membrane (nitrocellulose ~1 μm thick, or fluoropolymer such as CYTOP) mounted on an aluminum frame (5-10 mm standoff height above mask surface). Seals the mask pattern area — any particle that lands on the pellicle is far enough above the mask plane to be out of focus and not print. Pellicle must transmit >99% at exposure wavelength. Replaceable when damaged. Essential for production masks; omit for development or low-volume work.

### Lithography Tools
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

### Resist Stripping

After pattern transfer (etch or implant), photoresist must be removed before the next process step. Stripping method depends on whether the resist has been hard-baked, plasma-etched, or implanted (crosslinked resist is much harder to remove). Incomplete resist removal is a common yield killer — residue particles cause defects in subsequent deposition and etch steps.
- **Oxygen plasma ashing**: RF plasma (13.56 MHz, 100-500 W, O₂ flow 50-200 sccm, 0.5-2 Torr, 150-300°C). Oxygen radicals oxidize resist to CO₂ + H₂O (volatile products). Removes ~1-5 μm/min depending on conditions. Dry process — no liquid waste. Typically used as first step to remove bulk resist, followed by wet clean for residue.
- **Piranha solution**: H₂SO₄:H₂O₂ at 3:1 ratio (add peroxide slowly to sulfuric acid — vigorous exotherm, temperature reaches 100-130°C). Attacks organic material aggressively. Dissolves resist and removes metallic contaminants. Use immediately after mixing (peroxide decomposes rapidly). Extremely dangerous — burns skin on contact, can cause explosions if mixed with organics. Always add peroxide TO acid, never reverse.
- **Acetone**: For non-crosslinked resist (resist that has not been severely hard-baked or plasma-damaged). Soak 5-10 min at room temperature or 50°C. Acetone swells and dissolves the resin. Follow with IPA rinse (acetone leaves residue) and N₂ dry. Cannot remove hard-baked or plasma-crosslinked resist.
- **Standard strip sequence**: Oxygen plasma ash (remove bulk) → piranha clean (remove residue and metals) → DI water rinse → N₂ dry. For non-critical steps: acetone → IPA → N₂ dry.
- **Safety notes**: Piranha solution is the most dangerous wet chemical in the fab. Mix only in dedicated fume hood with acid-resistant PPE (face shield, acid gloves, apron). Never store piranha — decompose with excess water before disposal. Oxygen plasma equipment requires proper RF grounding and O₂ leak detection. Acetone and IPA are fire hazards — no ignition sources, use in ventilated areas.

### Hazards & Safety

- **PGMEA developer / ethyl lactate carrier**: Both cause respiratory and eye irritation at concentrations above 50 ppm. Use in ventilated wet benches with local exhaust. Wear nitrile gloves and safety glasses. Prolonged skin contact causes defatting and dermatitis.
- **Dichromate toxicity**: Ammonium dichromate ((NH₄)₂Cr₂O₇) contains Cr(VI), a confirmed human carcinogen (lung, nasal sinus). Inhalation of dust or mist is the primary route. If dichromated-gelatin resists are used for mask blanks, handle powder in a fume hood with particulate respirator (P100). Substitute novolac/DNQ resists whenever possible to eliminate chromium exposure entirely.
- **Mercury UV lamps**: High-pressure mercury arc lamps emit intense UV (g-line 436 nm through deep UV) and generate ozone. Enclose lamp housings completely; interlock covers so lamp cannot operate with housing open. Replace lamps at rated lifetime (~1000 hours) — aging lamps risk envelope rupture and mercury release. Mercury spill protocol: evacuate area, use mercury spill kit (sulfur powder or zinc dust), never vacuum.
- **Piranha solution** (H₂SO₄:H₂O₂ 3:1): The most dangerous wet chemical in photoresist stripping. Mix only in dedicated fume hood with acid-resistant PPE (face shield, heavy-duty acid gloves, chemical apron). Always add peroxide TO acid, never reverse — violent exotherm can cause boiling and spattering. Never store — decompose with excess water before disposal. Contact with organics can cause explosion.
- **Photoresist disposal**: Spent resist, developer, and rinse water containing dissolved organics are hazardous waste. Collect in labeled, compatible containers. Do not pour down any drain. PGMEA and ethyl lactate waste can be reclaimed by fractional distillation; contaminated waste must be incinerated by licensed hazardous-waste contractor.

---

*Part of the [Bootciv Tech Tree](../) • [Photolithography](./) • [All Domains](../)*
