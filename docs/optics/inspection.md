# Optics & Inspection

> **Node ID**: optics.inspection
> **Domain**: [Optics](./)
> **Enables**: `vlsi-scaling.advanced-lithography`
> **Timeline**: Years 25-40
> **Outputs**: lenses, microscopes, optical_comparators

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
- **Mechanical stage**: X-Y movement with graduated drums (0.01 mm resolution). Focus: coarse + fine (0.001 mm resolution). Requires Machine Tools stage precision machining.
- **Applications**: Crystal defect inspection (Silicon), lithography alignment (Photolithography), defect analysis, biological specimens (SQ5).

**Optical comparators** (shadow projection for dimensional measurement):
- Light source projects silhouette of part onto screen. Magnification 10-50x. Compare shadow against overlay drawing (mylar with tolerance bands). Quick, non-contact measurement of external dimensions.

**Spectroscopes** (optional — material identification):
- **Prism spectroscope**: White light through slit → prism → splits into spectrum. Observe emission or absorption lines. Each element has unique spectral fingerprint.
- **Flame spectroscopy**: Dip sample in flame → characteristic color (Na = yellow, Cu = green/blue, Li = red, K = violet). Quick qualitative analysis.
- **Applications**: Ore identification, alloy verification, chemical analysis, astronomical observation.

### Telescope Construction

**Refracting telescopes** (lens-based):
- **Objective lens**: Grind and polish a large plano-convex or biconvex lens (crown glass). Focal length f = R/(n-1) for plano-convex. Typical amateur: 50-80 mm diameter, f/10-f/15 (500-1200 mm focal length).
- **Eyepiece**: Short-focus convex lens (Huygens: 2-element; later Ramsden, Kellner). Magnification = f_objective / f_eyepiece.
- **Tube construction**: Cardboard or rolled brass tube, blackened interior to reduce stray light. Diameter slightly larger than objective. Focuser tube slides for adjustment.
- **Mount types**: Alt-azimuth (simple up-down, left-right) for basic use. Equatorial mount (polar axis aligned to celestial pole) enables tracking by rotating one axis. Chromatic aberration: single lens shows color fringing; achromatic doublet (crown + flint) reduces it.

**Reflecting telescopes** (mirror-based, no chromatic aberration):
- **Newtonian**: Flat diagonal (secondary) mirror deflects focus to side of tube. Simplest reflecting design. Primary mirror: parabolic. Most common amateur design.
- **Cassegrain**: Hyperbolic secondary reflects focus back through hole in primary. Compact tube, long effective focal length. More complex optics (two non-spherical surfaces).

### Mirror Grinding Procedure

**Rough grinding** (generating the curve):
- Fix glass blank (borosilicate or soda-lime) to workbench. Use cast iron or glass tool of equal diameter.
- Coarse silicon carbide (60-80 grit SiC) with water. Stroke blank across tool in W-pattern, rotating slowly. For concave mirror: blank on top. Convex tool drives curve into blank.
- Check sagitta (depth at center) with straightedge and feeler gauge: sagitta = r²/(2R) where r = radius of blank, R = desired radius of curvature. Target: within 10% of desired f-ratio.

**Fine grinding sequence** (removing coarse scratches):
- Progress through grits: 220 → 320 → 400 → 600 → 1200. Each grit removes pits from previous stage. Typical: 30-60 minutes per grit.
- **Critical**: Wash blank, tool, and work surface thoroughly between grits. A single grain of coarse grit will scratch the fine-ground surface, requiring regression to that grit stage.
- After 1200 grit: surface appears smooth but is still opaque (frosted appearance). Micro-pits remain, removed during polishing.

**Polishing**:
- Make pitch lap: pour soft pine pitch over tool, press against mirror to conform. Channel with 1-2 cm grooves (allows pitch to flow and conform during polishing).
- Polishing compound: cerium oxide (CeO₂) slurry, ~10% by weight in water. Faster and cleaner than traditional rouge (Fe₂O₃).
- Duration: 4-12 hours for 100-200 mm mirror. Slow strokes, moderate pressure. Surface transitions from translucent to fully transparent.

**Parabolizing** (figuring the sphere into a paraboloid):
- A sphere focuses parallel light to a zone, not a point. Paraboloid corrects this for on-axis images. Required for f-ratios faster than ~f/8.
- **Overhang stroke**: Extend mirror past lap edge by ~1/3 diameter on each stroke — wears center faster than edge, deepening central curve toward paraboloid.
- **Petal lap**: Modify pitch lap by cutting away petals — selective contact controls which zones are polished. Advanced technique for precise figure control.
- **Foucault test** (knife-edge test): Place point light source at radius of curvature. Move razor blade across returning cone of light. Shadows reveal zones: sphere shows uniform gray; paraboloid shows characteristic "doughnut" shadow pattern. Measure zonal radii with Couder mask to quantify deviation from paraboloid.

### Prism Fabrication

- **Blank preparation**: Select optical glass block (BK7 equivalent or flint glass). Cut to rough prism shape with diamond saw or wire saw with SiC slurry.
- **Angle control**: Grind two refracting faces to specified angle (60° for equilateral dispersing prism, other angles for special purposes). Use sine bar or angle gauge to set grinding fixture. Tolerance: ±0.1° for spectroscopic use, ±0.01° for precision optics.
- **Fine grinding and polishing**: Same sequence as lens work (220 → 1200 grit → CeO₂ polish). Polish each face individually on flat lap. Faces must be flat to λ/4 (quarter-wavelength) over full aperture.
- **Testing**: Illuminate with collimated white light through slit → prism → observe spectrum on screen or with telescope. Sharp spectral lines indicate good polish and correct angle. Spectroscope built from own output — first instrument can certify subsequent ones.

### Optical Coatings

- **Anti-reflection coating** (single-layer MgF₂):
  - Magnesium fluoride (MgF₂) deposited on lens surface. Thickness: λ/4 (quarter-wavelength, ~100 nm for center of visible spectrum). Refractive index n ≈ 1.38, between air (1.0) and glass (~1.5).
  - Reduces surface reflection from ~4% to ~1.3% per surface. On a 4-element lens (8 surfaces): transmission improves from ~72% to ~90%.
  - Deposition: thermal evaporation in vacuum chamber at 10⁻⁴ Pa (10⁻⁶ Torr). Heat MgF₂ in tungsten boat until it sublimes. Vapor condenses on rotating lens above. Monitor thickness with quartz crystal microbalance.
  - **Requires**: vacuum technology (rotary vane pump + diffusion pump), tungsten heating elements, MgF₂ source material.

- **Mirror coating** (aluminum):
  - Evaporate high-purity aluminum in vacuum at 10⁻⁴ Pa. Tungsten filament or boat, heated to melt aluminum (660°C) then to evaporation (~1200°C). Vapor deposits on mirror substrate above.
  - Reflectivity: ~92% for fresh aluminum (vs ~85% for silver, which tarnishes). Protective overcoat of SiO₂ (quarter-wave) extends lifetime.
  - **Requires**: same vacuum infrastructure as anti-reflection coating, plus aluminum source material.

### Optional: Vacuum Tube Electronics

- Not strictly required for semiconductor path, but provides:
  - Amplification experience (useful for test equipment)
  - Radio communication capability (valuable for coordination, SQ3)
  - Understanding of electron physics
- **Requires**: Glass envelopes (glassblowing capability above), vacuum (rotary vane pump sufficient), cathode material (tungsten or thoriated tungsten — heated to emit electrons), anode (nickel plate), grid (fine wire spiral for triode), base and pins (glass-to-metal seals).
- **Evacuation**: Pump down to 10⁻⁴ Torr, bake tube to 300-400°C during pumping to drive off adsorbed gases, seal off. Getter (barium or magnesium flash strip) inside tube — flashes during initial activation, absorbs residual gases.

### Safety & Hazards

- **Laser eye hazards**: Alignment and testing lasers (even low-power HeNe at 1-5 mW) can cause permanent retinal burns from direct or reflected beam exposure. Never look into beam path. Use laser safety goggles matched to wavelength. Enclose beam paths where feasible.
- **Chemical etchants**: Lens and prism preparation may use hydrofluoric acid (HF) for glass etching — HF penetrates skin, attacks bone, causes delayed deep-tissue necrosis. Calcium gluconate gel must be available as first aid. Cerium oxide and rouge (Fe₂O₃) polishing slurries are low hazard but avoid inhalation of dried powders.
- **Vacuum chamber implosion**: Glass vacuum tubes and bell jars under vacuum can collapse violently. Wrap with tape or mesh, wear face shield during evacuation. Never use chipped or scratched glassware under vacuum.

---

*Part of the [Bootciv Tech Tree](../) • [Optics](./) • [All Domains](../)*
