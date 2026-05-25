# Advanced Glass Production

> **Node ID**: glass.advanced
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`glass.basic`](basic.md)
> **Enables**: [`glass.advanced.glassblowing`](advanced-glassblowing.md), [`glass.fibers`](fibers.md), [`glass.photomask-substrates`](photomask-substrates.md), [`silicon.crystal-growth`](../silicon/crystal-growth.md)
> **Timeline**: Years 25-40
> **Outputs**: borosilicate_glass, fused_silica, quartz_crucibles, glass_tubing, glass_apparatus

### Advanced Glass Production

**[Borosilicate glass](../glossary/borosilicate-glass.md)** (Pyrex-type — thermal shock resistant):
- **Composition**: 70-80% SiO₂, 7-13% B₂O₃ (boron trioxide from borax or boric acid), 4-8% Na₂O, 2-7% Al₂O₃. Thermal expansion coefficient ~3×10⁻⁶/°C (vs. soda-lime glass ~9×10⁻⁶/°C — 3x more resistant to thermal shock).
- **Boron sources**: Borax (Na₂B₄O₇·10H₂O) from dry lake deposits (Turkey, California, Tibet). Dissolve in water, crystallize. Or boric acid (H₃BO₃) from borax + acid.
- **Melting**: Mix batch, melt in covered crucible at 1500-1600°C (higher than soda-lime glass). Requires gas or oil-fired furnace with forced air, or electric furnace. 12-24 hours for complete homogenization. Stir with fired clay rod.
- **Working properties**: Stiffer than soda-lime glass. Working range 800-1100°C. Annealing at 560°C. Cool slowly (6-12 hours from annealing to room temperature).
- **Applications**: Laboratory glassware (beakers, flasks, distillation columns), chemical apparatus (resists most acids, alkalis at moderate temperatures), telescope mirror blanks, bakeware.

**[Fused silica / quartz glass](../glossary/fused-silica-quartz-glass.md)** (critical for semiconductor crucibles):
- **Composition**: 100% SiO₂. No flux. Melting point ~1700°C (actually softens gradually, no sharp melting point — it's a glass).
- **Raw material**: High-purity quartz crystal (>99.5% SiO₂). Clear, inclusion-free. Mine from pegmatite veins or high-grade quartzite.
- **Production methods**:
  - **Type I (fused quartz)**: Melt natural quartz crystal in electric furnace (resistance-heated graphite or tungsten crucible, 1700-2000°C) under vacuum or inert atmosphere. Produces translucent or transparent fused silica. Bubble-free material requires vacuum degassing during melt.
  - **Type II (fused silica from flame)**: Feed quartz powder into hydrogen-oxygen flame (~2000°C). Particles fuse into clear boule. Very pure (flame volatilizes some impurities). Requires H₂ and O₂ (from the Energy stage electrolysis).
  - **[Synthetic fused silica](../glossary/synthetic-fused-silica.md)** (highest purity): Burn SiCl₄ in H₂/O₂ flame → SiO₂ deposits as soot → consolidate at 1500°C. 99.9999%+ purity. Requires chlorosilane chemistry from the Silicon stage.
- **Properties**: Thermal expansion 0.5×10⁻⁶/°C (virtually immune to thermal shock — can be heated red-hot and plunged into water). Transparent from UV (180 nm) through visible to IR (3.5 μm). Softening point ~1600°C. Working range 1800-2100°C.
- **Working**: Requires hydrogen-oxygen torch (~2800°C flame temperature). Oxy-acetylene produces a hotter flame (~3100°C) but introduces carbon contamination; hydrogen-oxygen is preferred for purity (only combustion product is water vapor). Graphite tools for shaping (won't stick to silica). Patience — silica is very viscous even at working temperature.
- **Applications**: CZ crystal growth crucibles (consumable — dissolves slowly in molten silicon), UV optics, high-temperature windows, optical fiber preforms (much later).

**Glassworking techniques**:
- **Cutting**: Score with diamond or hardened steel wheel, snap. Or hot-wire cut (nichrome wire heated to ~600°C — thermal stress cracks glass along wire line).
- **Bending**: Heat area in gas flame, bend to shape. Anneal.
- **Sealing (glass-to-glass)**: Heat edges of both pieces to softening temperature (~700°C for borosilicate). Press together. Flame-polish seam. Anneal. Matched glasses (same expansion coefficient) seal reliably.
- **Glass-to-metal seals**: Match expansion coefficient of glass to metal. Tungsten and molybdenum seal to borosilicate glass. Copper (Dumet wire — copper-clad nickel-iron alloy) seals to soda-lime glass. Graded seals use intermediate glasses to bridge expansion mismatch.
- **Grinding and polishing**: See Optics section below.

### Glassblowing & Scientific Apparatus

**[Lampworking](../glossary/lampworking.md)** (bench-scale glassblowing with torch):
- **Torch**: Gas-air (moderate temperature, ~1200°C) for soft glass. Gas-oxygen (~2000°C) for borosilicate. Propane-oxygen for quartz.
- **Basic operations**: Rotate tubing in flame to heat evenly. Pull to draw thin walls or capillary. Push to thicken. Blow (by mouth through tube) to expand. Score and break to cut. Fuse joints by heating overlapping pieces.
- **Standard apparatus**:
  - **Round-bottom flask**: Blow bubble, detach, fire-polish neck, add flared rim.
  - **Condenser (Liebig)**: Inner tube through outer jacket. Two side arms for water in/out. Sealed at both ends.
  - **Distillation column**: Tube with internal constriction rings or packed with glass helices. Side arm near top for condenser connection.
  - **Thistle funnel**: Tube with flared top and bulb reservoir, narrow delivery tube.
  - **Vacuum manifold**: Complex assembly with multiple ports, stopcocks, and connection points for vacuum line distribution.
- **Annealing**: ALL glass apparatus must be annealed after working. Residual stress from uneven cooling causes spontaneous fracture (sometimes weeks later). Place in annealing oven at appropriate temperature (560°C for borosilicate), hold 30-60 minutes, cool at 1-2°C/minute to below strain point.

**[Quartz crucible manufacturing](../glossary/quartz-crucible-manufacturing.md)** (for CZ crystal growth):
- **Raw material**: High-purity SiO₂ (>99.99%) from refined quartz crystal or synthetic fused silica. Impurities (especially Al, Fe, Na) must be below ppm levels — they dissolve into molten silicon and dope the crystal uncontrollably.
- **Slip casting method**: Prepare quartz powder slurry (SiO₂ + water + deflocculant). Pour into porous plaster mold shaped as crucible interior. Water absorbed by plaster leaves dense powder shell. Demold after 1-4 hours. Air dry 24-48 hours.
- **Isostatic pressing method**: Fill quartz powder into rubber bag shaped as crucible exterior. Apply hydraulic pressure (100-200 MPa) uniformly. Produces denser, more uniform green body than slip casting.
- **Sintering**: Fire dried green body in electric furnace at 1700-1800°C under vacuum or inert atmosphere. Holds 2-8 hours. Shrinkage ~15-20%. Transparency of finished crucible directly indicates purity — cloudy or opaque regions contain bubbles, crystalline inclusions, or impurities.
- **Final dimensions**: Wall thickness 5-10 mm, diameter 200-450 mm for semiconductor use. Thicker walls last longer in CZ pull but reduce thermal responsiveness. Handle with clean gloves — surface contamination transfers to silicon melt.

**[Glass tubing production — Danner process](../glossary/glass-tubing-production-danner-process.md)** (continuous):
- Molten glass flows from furnace forehearth onto a rotating inclined refractory mandrel (hollow ceramic cylinder, tilted ~15° from horizontal, rotating at 5-20 RPM). Glass wraps around mandrel forming a ribbon.
- Air blown through hollow mandrel center inflates the glass ribbon into a tube. Air pressure and draw speed control inner diameter. Mandrel diameter sets minimum bore.
- Tube drawn off continuously by tractor belts or rollers at controlled speed (1-20 m/min). Speed determines wall thickness — faster draw = thinner walls.
- Tube cools while being drawn (10+ meters of travel). Cut to length by scoring and snapping. Annealed in lehr before packaging.
- Produces tubing 3-50 mm OD in continuous lengths. Wall thickness tolerance ±0.1 mm with good process control.

### Safety & Hazards

- **Extreme-temperature glassworking**: Borosilicate melts at 1500-1600°C; fused silica requires 1700-2100°C working temperatures. Hydrogen-oxygen torches produce flame temperatures of ~2800°C. At these temperatures, severe burns occur on brief skin contact and radiation burns are possible at close range. Wear heat-resistant gloves, arm guards, face shield, and closed-toe boots. Use appropriate eye protection — intense visible and infrared radiation from molten silica and oxy-hydrogen flames can cause retinal damage (welding-grade shaded lenses for fused silica work).
- **Lead and heavy metal toxicity from glass additives**: Glazes and specialty glasses use lead oxide (PbO) as a flux, along with cobalt, manganese, and other metal oxide colorants. Lead oxide is toxic by inhalation (dust) and ingestion — causes cumulative neurological, renal, and reproductive damage. Handle all glass batch powders containing lead, cobalt, or barium with gloves and respiratory protection. Weigh and mix in ventilated areas. Wash hands thoroughly before eating or drinking.
- **Chlorosilane hazards in synthetic fused silica**: The synthetic fused silica process burns SiCl₄ in a hydrogen-oxygen flame. Silicon tetrachloride is corrosive, reacts violently with moisture to produce hydrochloric acid fumes, and causes severe respiratory damage. Handle only in closed, well-ventilated systems with acid-resistant equipment. Emergency response: flood exposed skin or eyes with copious water for 15+ minutes; move to fresh air if inhaled.
- **Hydrogen gas explosion risk**: Hydrogen-oxygen torch systems and furnaces used for fused silica work involve stored or piped hydrogen gas. Hydrogen forms explosive mixtures with air at 4-75% concentration and ignites with very low energy. Leak-test all connections before each use. Store cylinders away from heat and ignition sources. Never use hydrogen in unventilated spaces. In case of hydrogen fire, shut off gas supply if safely possible — do not attempt to extinguish a hydrogen flame without stopping the gas flow.

### Optical Glass Production

Optical glass demands exceptional homogeneity (no striae, bubbles, or compositional variation) and precisely controlled refractive index. The tolerances are far tighter than for container or window glass.

**[Continuous melting](../glossary/continuous-melting.md)** (production method for optical glass):
- Raw materials batched to ±0.01% accuracy (vs. ±2% for container glass). Weighing errors shift the refractive index outside specification.
- Melt in a platinum-lined tank furnace. Platinum is inert and introduces no contamination, unlike clay crucibles which dissolve slowly into the glass. Tank capacity: 100-500 liters for optical grades.
- Mechanical stirring throughout the melt: platinum paddle stirrer at 5-20 RPM, run continuously for 8-24 hours. Stirring eliminates striae (compositional layers that refract light unevenly). Without stirring, convection currents in the melt create layers of slightly different composition.
- **Fining**: Antimony trioxide (Sb₂O₃) at 0.1-0.3% added as fining agent. Hold at 1500-1600°C for 4-6 hours. Bubbles must be eliminated entirely — even a 50 μm bubble creates a visible defect in an optical element.
- **Annealing for optical glass**: Far more critical than for ordinary glass. Hold at annealing point for days to weeks (not hours). Cool at 0.1-1°C/hour through the strain point. A 100 mm lens blank may require 2-4 weeks of annealing. The goal is to reduce residual stress below the level that would cause measurable optical distortion (stress birefringence). Refractive index tolerance: ±0.001 for standard optical glass, ±0.0001 for precision grades.

### Lens Grinding and Polishing

Transforming a glass blank into a precision optical surface requires sequential abrasive stages, each finer than the last:

**Rough grinding**:
- Use silicon carbide (SiC) abrasive, grit 80-220. Coat the grinding tool (a cast iron or glass tool of the desired curvature — convex for a concave lens, concave for a convex lens) with abrasive slurry (SiC + water). Rub the lens blank against the tool in long strokes, rotating both.
- Grit 80 removes ~0.1 mm per minute. Grit 220 produces a uniform matte surface with ~50-70 μm pits. Rough grinding establishes the basic curvature radius to within ±0.5 mm.

**Fine grinding**:
- Progress through SiC 400, 600, then aluminum oxide (Al₂O₃) 12 μm and 5 μm. Each stage removes the pits left by the previous, coarser stage. Clean the lens and tool thoroughly between stages — a single stray grain of coarse abrasive will scratch the surface and require dropping back a stage.
- After 5 μm Al₂O₃, the surface appears semi-transparent with ~3-5 μm pits. The curvature radius should be within ±0.05 mm of target.

**Polishing**:
- Polish with cerium oxide (CeO₂) slurry (0.5-3 μm particle size) on a pitch lap. The lap is made from pine pitch or optical pitch poured onto a convex/concave tool and pressed to match the lens curvature while warm. Channels cut into the pitch surface (V-grooves, 3-5 mm wide, spaced 10-15 mm apart) allow the polish slurry to flow and prevent the lap from sticking.
- Polishing removes the final ~1-2 μm of surface damage. A properly polished surface shows no visible defects under 10× magnification and has surface roughness below 10 nm RMS. Total polishing time for a 50 mm diameter lens: 1-4 hours depending on curvature.

**Testing**: Measure the focal length by auto-collimation or by projecting a distant point source to a sharp focus. Test surface quality with a knife-edge test (Foucault test) or interferometry. An acceptable lens shows no zones (rings of different curvature) under the knife-edge test, and the surface deviates from the ideal curve by less than λ/4 (quarter-wave) across the full aperture.

### Mirror Making

Concave mirrors for telescopes and reflectors require a parabolic surface (or spherical for small apertures where the difference is negligible):

**Grinding a spherical mirror**: Same process as lens grinding — grind the glass blank against a convex tool with successively finer abrasives. For mirrors, both pieces tend toward complementary spherical surfaces naturally (any high spot on one contacts the other and gets ground down preferentially). A 150 mm f/8 mirror (1200 mm focal length) is close enough to spherical that no parabolizing is needed.

**Parabolizing**: For faster mirrors (f/6 and below), the sphere must be corrected to a paraboloid. Use a smaller polishing lap (sub-diameter lap, ~60% of mirror diameter) with longer strokes on the mirror edges and shorter strokes at the center. The goal is to remove more glass from the edge zones, deepening the curve from spherical to parabolic.

**Foucault knife-edge test**: The definitive test for mirror figure. Place a point light source (pinhole illuminated by LED or candle) at the mirror's center of curvature. The reflected light returns to a focus near the source. Intercept the returning cone with a razor blade (knife-edge) mounted on a micrometer stage. Moving the blade laterally across the beam: a perfect sphere darkens uniformly across the entire mirror face. Any zone that appears bright or shadowed ahead of the rest indicates a surface error. Accuracy: can detect surface errors of λ/8 to λ/20 (50-100 nm) with careful measurement. Build a Foucault tester from a micrometer slide, razor blade, and LED in an afternoon.

**Mirror coating**: After polishing and figuring to the required accuracy, the glass surface must be coated with a reflective layer. Aluminum vaporized in vacuum (thermal evaporation from a tungsten filament) deposits a 80-100 nm aluminum layer. Reflectivity: ~88% across the visible spectrum. Protected with a thin SiO overcoat (~50 nm) for scratch resistance.

### Prism Manufacturing

Prisms require flat surfaces at precise angles:

- **Right-angle prism**: Two 45° faces and one 90° face. Grind each face flat (see flat surface production below), then bevel the edges at 45° to form the hypotenuse face. Angular tolerance: ±5 arc-minutes for standard work, ±30 arc-seconds for precision optics.
- **[Equilateral prism](../glossary/equilateral-prism.md)** (60° angles): Used for dispersion spectroscopy. The three faces must be flat to λ/4 and angles equal to within ±2 arc-minutes.
- **Testing**: Measure angles with an autocollimator (telescope with a built-in light source that reflects off the prism face). Check flatness by placing the prism face against an optical flat (see below) and counting interference fringes under monochromatic light.

### Flat Surface Production

Guaranteed flatness comes from a self-correcting process using three plates:

- Take three flat plates (cast iron or glass, 100-200 mm diameter). Lap plate A against plate B with fine abrasive. Then lap plate B against plate C. Then lap plate C against plate A. Continue cycling through all three pairs.
- Each pair converges toward flatness because concave and convex errors cancel when you alternate which plate serves as the tool. After sufficient cycling, all three plates are flat to within a fraction of a wavelength of light (λ/10 to λ/20).
- Test by placing the finished plate against a reference optical flat under monochromatic light (sodium vapor lamp, 589 nm). Interference fringes (Newton's rings) reveal surface errors. One fringe = λ/2 = 295 nm height difference. A truly flat surface shows straight, parallel fringes.

### Tempered Glass

Thermal tempering increases the strength of soda-lime glass by 3-5×:

- **Process**: Heat the glass to 620-650°C (above the strain point but below the softening point). Then rapidly cool (quench) both surfaces with compressed air jets. The surfaces cool and contract first, then the interior cools more slowly. The still-hot interior tries to contract as it cools, pulling the already-rigid surfaces into compression. The result: surfaces in high compression (~100 MPa), interior in tension.
- Glass always fails from surface flaws in tension. Pre-compressing the surface means an applied tensile load must overcome the residual compression before the surface goes into tension. Net tensile strength increases to 150-250 MPa (vs. 30-90 MPa for annealed glass).
- When tempered glass breaks, the stored strain energy causes it to shatter into small, relatively harmless cubes rather than sharp shards. This is why tempered glass is required for car windows, shower doors, and glass doors.
- Tempered glass cannot be cut, drilled, or ground after tempering — any disruption of the surface compression causes instantaneous catastrophic failure. All shaping must be completed before the tempering process.

### Glass-to-Metal Seal Detail

Glass-to-metal seals are critical for vacuum tubes, electrical feedthroughs, and chemical apparatus:

**Tungsten to borosilicate**: Tungsten (CTE ~4.5 × 10⁻⁶/°C) seals directly to borosilicate glass (CTE ~3.3 × 10⁻⁶/°C). The mismatch of ~1 × 10⁻⁶/°C is small enough that the seal survives thermal cycling without cracking. Pre-oxidize the tungsten wire by heating in air to ~800°C until a thin blue oxide layer forms. This oxide layer improves wetting — the glass flows around and bonds to the metal surface more reliably than to bare metal. Seal diameter: typically 0.5-2 mm wire through 3-8 mm glass tubing.

**Copper (Dumet) to soda-lime**: Dumet wire is a copper-clad nickel-iron alloy (42% Ni, 58% Fe core, Cu cladding). The composite CTE (~7 × 10⁻⁶/°C) matches soda-lime glass (~9 × 10⁻⁶/°C) closely enough for reliable sealing. The copper cladding provides a plastically deformable layer that absorbs residual stress from the small CTE mismatch. Used for incandescent lamp stems and electrical feedthroughs.

**Graded seals**: For large expansion mismatches (e.g., copper at 17 × 10⁻⁶/°C to borosilicate at 3.3 × 10⁻⁶/°C), use a series of intermediate glasses with progressively changing CTE. Each glass sleeve in the series seals to the next, creating a stepped transition. Typically 3-5 intermediate glasses bridge the gap. The step between adjacent glasses should not exceed 2 × 10⁻⁶/°C CTE difference. Graded seals are used in vacuum tube envelopes, high-pressure lamp housings, and cryogenic feedthroughs.

### Glass Fiber Production

**Glass wool (insulation)**: Molten glass flows through a spinner (rotating disk with thousands of small holes, 0.5-1 mm diameter, spinning at 2,000-4,000 RPM). Centrifugal force extrudes the glass into fine fibers 5-15 μm diameter, 5-15 cm long. A binder (phenolic resin, 5-10% by weight) is sprayed onto the fibers as they form. The fibrous mat is cured at 200°C and cut to size. Thermal conductivity: 0.03-0.04 W/(m·K) — excellent insulation. Density: 10-50 kg/m³.

**Continuous glass fiber (structural)**: Molten glass flows through a platinum bushing (a plate with 200-4000 holes, 0.8-2.0 mm diameter) under gravity. The emerging glass strands are attenuated (drawn) by a high-speed winder at 1,000-3,000 m/min, reducing the diameter to 5-24 μm. A sizing (thin coating of polymer + coupling agent) is applied immediately to protect the fiber surface from abrasion and improve bonding with resin matrices. Tensile strength of individual E-glass fibers: 3,000-3,800 MPa (far stronger than bulk glass due to the flaw-free surface created by the drawing process).

### Optical Glass Types and Applications

Different glass compositions serve different optical purposes. The key properties are refractive index (RI) and dispersion (Abbe number):

- **[Crown glass](../glossary/crown-glass.md)** (low dispersion): Soda-lime or borosilicate base, RI 1.50-1.54, Abbe number 55-65. Used for the convex (positive) elements in achromatic lens doublets. The low dispersion means it bends different wavelengths of light nearly equally, reducing chromatic aberration.
- **[Flint glass](../glossary/flint-glass.md)** (high dispersion): Lead glass base, RI 1.58-1.72, Abbe number 25-40. Used for the concave (negative) element in achromatic doublets. The high RI allows a shallower curve for the same optical power, reducing spherical aberration. The combination of a crown convex and flint concave element, cemented together, produces an achromatic lens that focuses two wavelengths to the same point.
- **[ED glass](../glossary/ed-glass.md)** (extra-low dispersion): Borosilicate with rare earth oxides (lanthanum, La₂O₃), RI 1.65-1.80, Abbe number 45-55. Further reduces chromatic aberration in apochromatic lens designs. Requires rare earth element extraction from monazite or bastnäsite ores.

### Glass Storage and Handling

Finished glass products require careful handling to prevent damage:

- **Scratch prevention**: Glass surfaces scratch easily (Mohs 6-7). Store glass plates and sheets with paper interleaving between them. Never slide one glass sheet across another — lift and place. For optical glass, store in individual felt-lined containers.
- **Thermal shock**: Even borosilicate glass can crack if subjected to rapid, uneven temperature changes. Allow glassware to reach room temperature before exposing it to hot liquids. Never place hot glassware on a cold, wet surface — the thermal gradient can exceed the material's shock resistance.
- **Chemical compatibility**: Soda-lime glass dissolves slowly in strong alkalis (NaOH, KOH) above 60°C. Borosilicate resists alkalis better but still shows attack above 100°C. HF (hydrofluoric acid) dissolves all glass rapidly — never store or handle HF in glass containers. Use polyethylene or PTFE containers for HF.
- **Impact protection**: The practical tensile strength of glass (30-90 MPa) is much lower than its theoretical strength (~10 GPa) due to surface flaws. Even a light impact that doesn't visibly damage the glass can create micro-cracks that will grow under subsequent thermal or mechanical stress, leading to delayed failure.

### Quartz Crucible Quality Control

The quality of quartz crucibles for CZ crystal growth directly impacts silicon wafer quality:

- **Bubble inspection**: Illuminate the crucible wall with a bright light. Bubbles appear as bright spots. For semiconductor-grade crucibles, bubbles larger than 50 μm are rejectable in the inner (silicon-contact) wall. Outer wall bubbles up to 200 μm are tolerated. Bubbles near the inner surface can detach during CZ pulling, contaminating the silicon melt.
- **Dimensional tolerance**: Inside diameter ±1 mm for a 300 mm crucible. Ovality (out-of-roundness) less than 1 mm. Wall thickness variation less than 0.5 mm around the circumference. Thickness uniformity ensures even heat transfer during crystal growth.
- **Purity verification**: Test crucible material by ICP-MS (inductively coupled plasma mass spectrometry) or GDMS (glow discharge mass spectrometry). Key impurity limits for semiconductor use: Al <10 ppm, Fe <1 ppm, Na <0.5 ppm. Metallic impurities in the crucible dissolve into molten silicon during CZ growth, doping the crystal uncontrollably. Solar-grade crucibles tolerate higher impurity levels (Al <20 ppm, Fe <5 ppm) because solar cell efficiency is less sensitive to trace contamination.
- **Cristobalite check**: After sintering, check for cristobalite (crystalline SiO₂) formation by X-ray diffraction. Cristobalite indicates the crucible was held too long above 1470°C during sintering. Crystalline regions are brittle and prone to cracking during thermal cycling. Reject crucibles showing more than 5% cristobalite by volume.

### Glass Ceramics (Vycor-Type)

Glass ceramics combine the formability of glass with the mechanical strength and thermal stability of crystalline ceramics:

- **Process**: Melt a borosilicate glass with a specific composition (75% SiO₂, 20% B₂O₃, 5% Na₂O). Form into the desired shape by conventional glass forming. Heat treat at 500-600°C to induce phase separation — the glass separates into two interpenetrating phases: a silica-rich phase and a sodium-borate-rich phase. Leach in hot acid (HCl or H₂SO₄) to dissolve the sodium-borate phase, leaving a porous silica skeleton (~70% of original volume, pore size 2-10 nm). Heat to 900-1000°C to sinter and consolidate the porous structure into a dense, high-silica glass (96% SiO₂, 3% B₂O₃, 1% other).
- **Properties**: CTE 0.75 × 10⁻⁶/°C (very low — approaching fused silica). Continuous use temperature: 900°C. Thermal shock resistance: can be heated to 900°C and quenched in water. Very resistant to chemical attack. Used for laboratory ware, high-temperature windows, and precision optical substrates.
- **Advantage over fused silica**: Can be formed at conventional glassworking temperatures (the initial forming is done before leaching and consolidation), unlike fused silica which requires 1800-2100°C working temperatures. This makes complex shapes achievable with standard glassblowing equipment.

### Optical Coating and Surface Treatment

**Anti-reflective coating**: A thin layer of magnesium fluoride (MgF₂) deposited on the glass surface reduces reflection losses. The coating thickness is λ/4 (quarter-wavelength, typically 100-130 nm for visible light), and the coating's refractive index should be the geometric mean of glass (1.52) and air (1.00): √(1.52 × 1.00) = 1.23. MgF₂ (RI 1.38) is the closest practical material. Deposited by thermal evaporation in vacuum (~10⁻⁵ torr). Reduces surface reflection from ~4% to ~1.5% per surface. For a lens with 4 air-glass surfaces, total transmission improves from ~85% to ~94%.

**Mirror coating**: Aluminum deposited by vacuum evaporation produces a reflective surface with ~88% reflectance across the visible spectrum. Silver gives ~95% reflectance but tarnishes in air (requires protective overcoat). Protected aluminum (Al + SiO overcoat, 50-80 nm) resists oxidation and scratching, maintaining reflectance for years. For the bootstrap sequence, aluminum evaporation requires a vacuum chamber (~10⁻⁵ torr), a tungsten filament boat, and aluminum wire or foil.

**Chemical strengthening**: An alternative to thermal tempering for thin glass (1-3 mm). Immerse the glass in a bath of molten potassium nitrate (KNO₃) at 400-450°C for 4-16 hours. Large K⁺ ions (0.133 nm radius) exchange with smaller Na⁺ ions (0.095 nm) in the glass surface. The larger potassium ions crowd the surface layer, placing it in compression. Compressive stress: 300-700 MPa (much higher than thermal tempering). Used for smartphone screens (Gorilla Glass) and aircraft windshields. The glass can be cut after treatment (unlike thermally tempered glass), but the strengthening effect is limited to the thin surface layer (~20-50 μm deep).

### Precision Bore Tubing

For scientific glassware requiring precise internal diameters (thermometer tubing, chromatography columns, capillary tubing):

- **Process**: Start with standard glass tubing. Insert a precision-ground steel mandrel (tolerance ±0.01 mm) into the tube. Heat the glass in a furnace to softening temperature. Apply slight internal pressure to expand the glass against the mandrel. Cool while maintaining pressure. Withdraw the mandrel after the glass is below strain point.
- **Result**: Internal diameter matches the mandrel to within ±0.02 mm along the full length. Wall thickness is uniform because the glass flows to equalize under surface tension and internal pressure.
- **Capillary tubing**: For very fine bore (0.1-1.0 mm), draw tubing vertically from a molten glass reservoir through a precision die. The draw speed (1-50 m/min) controls the outer diameter; internal pressure controls the bore. Diameter tolerance: ±5%. Used for thermometer capillaries, microfluidic devices, and gas chromatography columns.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Glass](./index.md) • [All Domains](../index.md)*
