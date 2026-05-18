# Advanced Glass Production

> **Node ID**: `glass.advanced`
> **Domain**: [Glass](./)
> **Dependencies**: `metallurgy.glass-lime`
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
  - **Synthetic fused silica** (highest purity, Photolithography+): Burn SiCl₄ in H₂/O₂ flame → SiO₂ deposits as soot → consolidate at 1500°C. 99.9999%+ purity. Requires chlorosilane chemistry from the Silicon stage.
- **Properties**: Thermal expansion 0.5×10⁻⁶/°C (virtually immune to thermal shock — can be heated red-hot and plunged into water). Transparent from UV (180 nm) through visible to IR (3.5 μm). Softening point ~1600°C. Working range 1800-2100°C.
- **Working**: Requires hydrogen-oxygen torch (3400°C flame temperature). Oxy-acetylene barely sufficient. Graphite tools for shaping (won't stick to silica). Patience — silica is very viscous even at working temperature.
- **Applications**: CZ crystal growth crucibles (consumable — dissolves slowly in molten silicon), UV optics, high-temperature windows, optical fiber preforms (much later).

**Glass tubing production**:
- **Drawing from molten glass**: Gather molten glass on hollow iron blowpipe. Blow initial bubble. While rotating, pull the bubble to draw tube of desired diameter (~5-30 mm OD). Cool while rotating to maintain roundness. Cut to length. Anneal.
- **Danner machine** (continuous tube drawing, Energy+ powered): Molten glass flows onto rotating inclined mandrel. Glass forms tube around mandrel. Drawn off by tractor belts at controlled speed. Speed determines wall thickness. Diameter 3-50 mm. Continuous lengths 10+ meters.
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
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
