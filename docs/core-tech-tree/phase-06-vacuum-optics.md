# Phase 6: Vacuum, Optics, Glass & Pre-Semiconductor Tech

**Timeline**: Years 25–40
**Goal**: Controlled environments and inspection capability.
**Dependencies**: [Phase 3](phase-03-machine-tools.md) (precision machining), [Phase 4](phase-04-energy.md) (energy), [Phase 5](phase-05-chemistry.md) (glass, chemicals)

## Objectives

- Build vacuum pumps and chambers for deposition/evaporation processes
- Produce advanced glass apparatus (tubing, envelopes, lenses)
- Develop optical inspection tools (microscopes, comparators)
- Establish early metrology for semiconductor-grade measurement

## Key Technologies

### Advanced Glass Production

**Borosilicate glass** (Pyrex-type — thermal shock resistant):
- **Composition**: 70-80% SiO₂, 7-13% B₂O₃ (boron trioxide from borax or boric acid), 4-8% Na₂O, 2-7% Al₂O₃. Thermal expansion coefficient ~3×10⁻⁶/°C (vs. soda-lime glass ~9×10⁻⁶/°C — 3x more resistant to thermal shock).
- **Boron sources**: Borax (Na₂B₄O₇·10H₂O) from dry lake deposits (Turkey, California, Tibet). Dissolve in water, crystallize. Or boric acid (H₃BO₃) from borax + acid.
- **Melting**: Mix batch, melt in covered crucible at 1500-1600°C (higher than soda-lime glass). Requires gas or oil-fired furnace with forced air, or electric furnace. 12-24 hours for complete homogenization. Stir with fired clay rod.
- **Working properties**: Stiffer than soda-lime glass. Working range 800-1100°C. Annealing at 560°C. Cool slowly (6-12 hours from annealing to room temperature).
- **Applications**: Laboratory glassware (beakers, flasks, distillation columns), chemical apparatus (resists most acids, alkalis at moderate temperatures), telescope mirror blanks, bakeware.

**Fused silica / quartz glass** (critical for semiconductor crucibles):
- **Composition**: 100% SiO₂. No flux. Melting point ~1700°C (actually softens gradually, no sharp melting point — it's a glass).
- **Raw material**: High-purity quartz crystal (>99.5% SiO₂). Clear, inclusion-free. Mine from pegmatite veins or high-grade quartzite.
- **Production methods**:
  - **Type I (fused quartz)**: Melt natural quartz crystal in electric furnace (resistance-heated graphite or tungsten crucible, 1700-2000°C) under vacuum or inert atmosphere. Produces translucent or transparent fused silica. Bubble-free material requires vacuum degassing during melt.
  - **Type II (fused silica from flame)**: Feed quartz powder into hydrogen-oxygen flame (~2000°C). Particles fuse into clear boule. Very pure (flame volatilizes some impurities). Requires H₂ and O₂ (from Phase 4 electrolysis).
  - **Synthetic fused silica** (highest purity, Phase 8+): Burn SiCl₄ in H₂/O₂ flame → SiO₂ deposits as soot → consolidate at 1500°C. 99.9999%+ purity. Requires chlorosilane chemistry from Phase 7.
- **Properties**: Thermal expansion 0.5×10⁻⁶/°C (virtually immune to thermal shock — can be heated red-hot and plunged into water). Transparent from UV (180 nm) through visible to IR (3.5 μm). Softening point ~1600°C. Working range 1800-2100°C.
- **Working**: Requires hydrogen-oxygen torch (3400°C flame temperature). Oxy-acetylene barely sufficient. Graphite tools for shaping (won't stick to silica). Patience — silica is very viscous even at working temperature.
- **Applications**: CZ crystal growth crucibles (consumable — dissolves slowly in molten silicon), UV optics, high-temperature windows, optical fiber preforms (much later).

**Glass tubing production**:
- **Drawing from molten glass**: Gather molten glass on hollow iron blowpipe. Blow initial bubble. While rotating, pull the bubble to draw tube of desired diameter (~5-30 mm OD). Cool while rotating to maintain roundness. Cut to length. Anneal.
- **Danner machine** (continuous tube drawing, Phase 4+ powered): Molten glass flows onto rotating inclined mandrel. Glass forms tube around mandrel. Drawn off by tractor belts at controlled speed. Speed determines wall thickness. Diameter 3-50 mm. Continuous lengths 10+ meters.
- **Applications**: Thermometer tubing, condenser tubes, vacuum tube envelopes, chemical apparatus, fluorescent lamp tubes.

**Glassworking techniques**:
- **Cutting**: Score with diamond or hardened steel wheel, snap. Or hot-wire cut (nichrome wire heated to ~600°C — thermal stress cracks glass along wire line).
- **Bending**: Heat area in gas flame, bend to shape. Anneal.
- **Sealing (glass-to-glass)**: Heat edges of both pieces to softening temperature (~700°C for borosilicate). Press together. Flame-polish seam. Anneal. Matched glasses (same expansion coefficient) seal reliably.
- **Glass-to-metal seals**: Match expansion coefficient of glass to metal. Tungsten and molybdenum seal to borosilicate glass. Copper (Dumet wire — copper-clad nickel-iron alloy) seals to soda-lime glass. Graded seals use intermediate glasses to bridge expansion mismatch.
- **Grinding and polishing**: See Optics section below.

### Glassblowing & Scientific Apparatus

**Lampworking** (bench-scale glassblowing with torch):
- **Torch**: Gas-air (moderate temperature, ~1200°C) for soft glass. Gas-oxygen (~2000°C) for borosilicate. Propane-oxygen for quartz.
- **Basic operations**: Rotate tubing in flame to heat evenly. Pull to draw thin walls or capillary. Push to thicken. Blow (by mouth through tube) to expand. Score and break to cut. Fuse joints by heating overlapping pieces.
- **Standard apparatus**:
  - **Round-bottom flask**: Blow bubble, detach, fire-polish neck, add flared rim.
  - **Condenser (Liebig)**: Inner tube through outer jacket. Two side arms for water in/out. Sealed at both ends.
  - **Distillation column**: Tube with internal constriction rings or packed with glass helices. Side arm near top for condenser connection.
  - **Thistle funnel**: Tube with flared top and bulb reservoir, narrow delivery tube.
  - **Vacuum manifold**: Complex assembly with multiple ports, stopcocks, and connection points for vacuum line distribution.
- **Annealing**: ALL glass apparatus must be annealed after working. Residual stress from uneven cooling causes spontaneous fracture (sometimes weeks later). Place in annealing oven at appropriate temperature (560°C for borosilicate), hold 30-60 minutes, cool at 1-2°C/minute to below strain point.

**Quartz crucible production** (for CZ crystal growth):
- Fabricate from fused silica using one of: (a) arc-melted fused quartz — mold shape from quartz powder in graphite mold, arc-melt surfaces to fuse; (b) slip-cast — pour quartz powder slurry into plaster mold, dry, sinter at 1700°C. Wall thickness 5-10 mm. Diameter 200-450 mm for semiconductor use.

### Vacuum Technology

**Mechanical pumps** (foundation of all vacuum work):

**Piston pump** (simplest, lower vacuum):
- **Construction**: Cast iron cylinder, machined piston with leather cup seal, inlet and outlet check valves (leather or steel flappers). Driven by crank from motor or hand wheel.
- **Performance**: ~10-100 L/min pumping speed. Ultimate vacuum ~10-50 Torr (rough vacuum).
- **Applications**: Initial roughing pump, gas transfer, compression.

**Rotary vane pump** (workhorse — achieves medium vacuum):
- **Principle**: Eccentric rotor in cylindrical stator. Spring-loaded vanes slide in rotor slots, maintaining contact with stator wall. Gas enters inlet port, trapped between vanes and stator, compressed, expelled through exhaust valve.
- **Construction**: Cast iron stator (bored to ~0.01 mm tolerance on Phase 3 lathe/boring machine). Steel rotor. Steel or carbon fiber vanes. Oil-filled for sealing and lubrication (oil seals microscopic gaps between vanes and stator).
- **Oil requirements**: Low vapor pressure vacuum oil (see [SQ 10](../side-quests/sq-10-lubricants-oils.md)). Mineral oil with low volatility, or silicone oil. Oil changed regularly — contaminated oil limits ultimate vacuum.
- **Performance**: 1-50 L/min (small), 50-500 L/min (medium). Ultimate vacuum: ~10⁻² to 10⁻³ Torr (0.01-0.001 Pa). Single-stage: ~10⁻² Torr. Two-stage: ~10⁻³ Torr.
- **Gas ballast**: Small valve admits air during compression phase to prevent condensation of vapors (water, solvents) in pump oil. Essential when pumping wet systems.

**Diffusion pump** (high vacuum, no moving parts):
- **Principle**: Boiler heats silicone or hydrocarbon oil → vapor jets shoot downward → gas molecules from vacuum chamber diffuse into vapor stream → carried to exhaust → removed by backing pump. No moving parts, very reliable.
- **Backing pump requirement**: Diffusion pump requires a mechanical backing pump (rotary vane) to maintain foreline pressure below ~0.5 Torr. Without backing, diffusion pump stalls and oil backstreams into chamber.
- **Performance**: Pumping speed 50-10,000 L/s. Ultimate vacuum: ~10⁻⁶ to 10⁻⁸ Torr with proper trapping and baking.
- **Oil**: Silicone oil (DC-704, DC-705) or Santovac (polyphenyl ether). Low vapor pressure, high thermal stability. Oil heated to ~150-200°C in boiler.
- **Cold trap**: Liquid nitrogen cooled baffle between diffusion pump and chamber. Condenses backstreaming oil vapor. Essential for clean vacuum. LN₂ from Phase 5 air liquefaction.

**Vacuum chambers**:
- **Materials**: Steel or stainless steel (welded construction, all seams seal-welded). Aluminum (lighter, easier to machine, but more porous to He). Glass bell jars (for small systems — visual observation).
- **Design**: Cylindrical or spherical (uniform stress distribution). Viewports (glass windows with CF or ISO flanges). Multiple ports for feedthroughs (electrical, mechanical, gas).
- **Surface preparation**: Electropolish stainless steel internal surfaces (smooth surface = less outgassing). Clean with acetone, then alcohol, then bake.

**Vacuum measurement**:
- **Rough vacuum (760-1 Torr)**: Bourdon tube gauge (mechanical). U-tube manometer (oil or mercury — measures pressure difference directly).
- **Medium vacuum (1-10⁻³ Torr)**: Thermocouple gauge or Pirani gauge (heated wire — thermal conductivity of gas depends on pressure). Inexpensive, reliable.
- **High vacuum (10⁻³-10⁻⁸ Torr)**: Penning ionization gauge (cold cathode ionizes gas, ion current proportional to pressure). Bayard-Alpert ion gauge (hot cathode version, more accurate). Calibration against McLeod gauge (absolute pressure measurement using compressed gas column — primary standard).

**Leak detection**:
- **Bubble test**: Pressurize system, spray soap solution on exterior, watch for bubbles. Finds large leaks.
- **Helium leak detector** (Phase 8+): Mass spectrometer tuned to He. Spray He on exterior, detect He entering vacuum system. Sensitivity ~10⁻¹² atm·cc/s. The gold standard.
- **Tesla coil**: High-frequency spark probe. Spark penetrates small holes in glass apparatus (visible discharge inside). Glass systems only.

### Optics & Inspection

**Lens grinding and polishing**:
- **Rough grinding**: Fix glass blank to convex or concave cast iron tool (curve matched to desired radius). Add coarse abrasive (60-120 grit SiC or emery) and water. Stroke blank across tool in random pattern. Check radius with spherometer or template. Duration: 2-8 hours depending on size and depth.
- **Fine grinding**: Progress through finer abrasives (220, 320, 400, 600 grit). Each stage removes scratches from previous stage. Rinse thoroughly between grits (cross-contamination ruins finish).
- **Polishing**: Iron or pitch lap (pitch conforms to glass surface). Polishing compound: cerium oxide (CeO₂) slurry in water, or rouge (Fe₂O₃). Duration: 2-12 hours for optical quality. Test with laser or monochromatic light — interference fringes reveal surface errors.
- **Flat surfaces**: Use three-plate method (same principle as surface plate scraping). Grind three glass plates alternately until all show uniform contact.
- **Spherical surfaces**: Use full-diameter tool for convex, channel tool for concave. Test with knife-edge (Foucault test) for mirror surfaces — reveals zones and irregularities as shadows.
- **Surface quality targets**: Scratch/dig 60/40 for visual optics, 20/10 for imaging optics, 10/5 for laser optics. Measured under controlled illumination against standards.

**Microscopes** (critical for semiconductor inspection):
- **Compound microscope**: Objective lens (4x-100x) + eyepiece (10x). Total magnification 40x-1000x. Resolution limited by diffraction: ~λ/(2·NA) where NA = numerical aperture. At NA 0.65 with visible light: ~0.4 μm resolution.
- **Objective design**: Achromatic doublet (crown + flint glass, corrects chromatic aberration at two wavelengths) or apochromatic (three-element, three-wavelength correction — better, harder to make).
- **Illumination**: Brightfield (transmitted light through sample), darkfield (oblique illumination — edges glow, defects visible). Later: phase contrast, DIC (differential interference contrast).
- **Mechanical stage**: X-Y movement with graduated drums (0.01 mm resolution). Focus: coarse + fine (0.001 mm resolution). Requires Phase 3 precision machining.
- **Applications**: Crystal defect inspection (Phase 7), lithography alignment (Phase 8), defect analysis (Phase 8+), biological specimens (SQ5).

**Optical comparators** (shadow projection for dimensional measurement):
- Light source projects silhouette of part onto screen. Magnification 10-50x. Compare shadow against overlay drawing (mylar with tolerance bands). Quick, non-contact measurement of external dimensions.

**Spectroscopes** (optional — material identification):
- **Prism spectroscope**: White light through slit → prism → splits into spectrum. Observe emission or absorption lines. Each element has unique spectral fingerprint.
- **Flame spectroscopy**: Dip sample in flame → characteristic color (Na = yellow, Cu = green/blue, Li = red, K = violet). Quick qualitative analysis.
- **Applications**: Ore identification, alloy verification, chemical analysis, astronomical observation.

### Early Metrology & Analytical Tools

- **Thermocouples**: Two dissimilar metals joined at junction. Voltage produced proportional to temperature difference between junction and reference. Type K (chromel-alumel): -200 to +1250°C. Type S (Pt-Pt/Rh): 0 to 1600°C. Calibrate against freezing/boiling points of standard substances.
- **Resistance temperature detectors (RTDs)**: Platinum wire, resistance changes with temperature. Very accurate (±0.1°C). Used for precision temperature control in crystal growth.
- **Pressure gauges**: Bourdon tube (C-shaped flattened tube, straightens with pressure), diaphragm gauge, capacitance manometer (electronic, very accurate).
- **Electrical measurement**: Galvanometer (moving coil in magnetic field — detects current to μA range), Wheatstone bridge (precision resistance measurement — 4 resistors in diamond, null detector), voltmeter (galvanometer with series resistor), ammeter (galvanometer with shunt resistor).

### Optional: Vacuum Tube Electronics

- Not strictly required for semiconductor path, but provides:
  - Amplification experience (useful for test equipment)
  - Radio communication capability (valuable for coordination, SQ3)
  - Understanding of electron physics
- **Requires**: Glass envelopes (glassblowing capability above), vacuum (rotary vane pump sufficient), cathode material (tungsten or thoriated tungsten — heated to emit electrons), anode (nickel plate), grid (fine wire spiral for triode), base and pins (glass-to-metal seals).
- **Evacuation**: Pump down to 10⁻⁴ Torr, bake tube to 300-400°C during pumping to drive off adsorbed gases, seal off. Getter (barium or magnesium flash strip) inside tube — flashes during initial activation, absorbs residual gases.

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| Rotary vane pumps | Phase 7 (crystal growth backing), Phase 8 (evaporation backing, dry etch) |
| Diffusion pumps | Phase 8 (evaporation, sputtering, CVD), Phase 7 (high-vacuum crystal growth) |
| Quartz crucibles | Phase 7 (Czochralski growth — consumable) |
| Microscopes | Phase 7 (crystal inspection), Phase 8 (alignment, defect analysis) |
| Fused silica | Phase 7 (crucibles), Phase 8 (mask substrates, UV optics) |
| Lens/optics capability | Phase 8 (lithography lenses, mask reduction optics) |
| Borosilicate glassware | Phase 5+ (all chemical apparatus), Phase 7-8 (processing equipment) |
| Temperature measurement | Phase 7 (crystal growth control ±0.5°C), Phase 8 (diffusion furnace control) |
| Vacuum measurement | Phase 7-8 (all vacuum process monitoring) |

## Practical Bottlenecks

- **Vacuum seal quality**: Achieving and maintaining good vacuum requires precise machining (flange flatness), good seal materials (Viton O-rings, copper gaskets, or indium wire), and ultra-clean assembly procedures. One fingerprint inside a vacuum chamber can take hours to outgas.
- **Optical quality**: Lens precision directly impacts lithography capability later. First lenses will have spherical aberration, chromatic aberration, and surface imperfections. Iterate on polishing technique.
- **Quartz crucible production**: Fused silica requires extremely high temperatures (1700°C+) and pure quartz feedstock. The crucibles are consumables (dissolve in molten silicon) — need a steady supply. Each CZ pull consumes one crucible.
- **Outgassing**: All materials inside vacuum chambers release adsorbed gases. Metals outgas H₂, H₂O, CO, CO₂. Plastics outgas enormously. Baking chambers at 150-300°C for 12-24 hours under vacuum dramatically reduces outgassing.

## Safety Concerns

- **Implosion of vacuum chambers**: Atmospheric pressure is ~10 tonnes/m². Even small chambers store enormous energy. Use shielding (polycarbonate or wire cage around glass bell jars). Never exceed design pressure differential. Spherical shapes resist implosion best.
- **Glass cuts and burns during glassblowing**: Hot glass looks identical to cold glass. Use didymium glasses (filter sodium flare, make hot glass visible). Rotate work continuously for even heating. Never hold hot glass over body.
- **High voltage** (if vacuum tubes attempted): 50-300V DC for tube plate supplies. Shock hazard. One-hand rule. Insulated tools.
- **Mercury exposure** (if mercury manometers/gauges used): Mercury vapor is neurotoxic. Use in well-ventilated area. Spill cleanup: sulfur powder binds mercury. Consider digital gauges to avoid mercury entirely.

## Side Quest Dependencies

- **[SQ 10 — Lubricants & Oils](../side-quests/sq-10-lubricants-oils.md)**: Oil-sealed rotary vane pumps require lubricants with low vapor pressure. Early pumps may use specially refined animal or vegetable oils; mineral oils become available with petroleum chemistry (SQ12). Vacuum pump oil quality directly impacts achievable vacuum levels.
- **[SQ 14: Polymers & Composites](../side-quests/sq-14-polymers-composites.md)** — polymer seals, gaskets, and O-rings needed for vacuum systems; cleanroom materials

[← Phase 5](phase-05-chemistry.md) | [Overview](overview.md) | [Phase 7: Silicon →](phase-07-silicon.md)
