# Advanced Glass Production

> **Node ID**: glass.advanced
> **Domain**: [Glass](./)
> **Dependencies**: `glass.basic`
> **Enables**: `silicon.crystal-growth`
> **Timeline**: Years 25-40
> **Outputs**: borosilicate_glass, fused_silica, quartz_crucibles, glass_tubing, glass_apparatus

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
  - **Type II (fused silica from flame)**: Feed quartz powder into hydrogen-oxygen flame (~2000°C). Particles fuse into clear boule. Very pure (flame volatilizes some impurities). Requires H₂ and O₂ (from the Energy stage electrolysis).
  - **Synthetic fused silica** (highest purity): Burn SiCl₄ in H₂/O₂ flame → SiO₂ deposits as soot → consolidate at 1500°C. 99.9999%+ purity. Requires chlorosilane chemistry from the Silicon stage.
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

**Quartz crucible manufacturing** (for CZ crystal growth):
- **Raw material**: High-purity SiO₂ (>99.99%) from refined quartz crystal or synthetic fused silica. Impurities (especially Al, Fe, Na) must be below ppm levels — they dissolve into molten silicon and dope the crystal uncontrollably.
- **Slip casting method**: Prepare quartz powder slurry (SiO₂ + water + deflocculant). Pour into porous plaster mold shaped as crucible interior. Water absorbed by plaster leaves dense powder shell. Demold after 1-4 hours. Air dry 24-48 hours.
- **Isostatic pressing method**: Fill quartz powder into rubber bag shaped as crucible exterior. Apply hydraulic pressure (100-200 MPa) uniformly. Produces denser, more uniform green body than slip casting.
- **Sintering**: Fire dried green body in electric furnace at 1700-1800°C under vacuum or inert atmosphere. Holds 2-8 hours. Shrinkage ~15-20%. Transparency of finished crucible directly indicates purity — cloudy or opaque regions contain bubbles, crystalline inclusions, or impurities.
- **Final dimensions**: Wall thickness 5-10 mm, diameter 200-450 mm for semiconductor use. Thicker walls last longer in CZ pull but reduce thermal responsiveness. Handle with clean gloves — surface contamination transfers to silicon melt.

**Glass tubing production — Danner process** (continuous):
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

*Part of the [Bootciv Tech Tree](../) • [Glass](./) • [All Domains](../)*
