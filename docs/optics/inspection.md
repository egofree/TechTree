# Optics & Inspection

> **Node ID**: optics.inspection
> **Domain**: [Optics](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: [`measurement.optical-instruments`](../measurement/optical-instruments.md), [`optics.inspection.optical-coatings`](optical-coatings.md), [`optics.precision-instruments`](precision-instruments.md), [`vlsi-scaling.advanced-lithography`](../vlsi-scaling/advanced-lithography.md)
> **Timeline**: Years 25-40
> **Outputs**: lenses, microscopes, optical_comparators
> **Critical**: No — optical inspection enhances quality control but parts can be made without it

### Problem

Manufacturing precision components requires verifying that surfaces, dimensions, and defects meet specification. The unaided human eye resolves ~100 μm features — far too coarse for machined tolerances (±0.01 mm) or optical surfaces (λ/4 = 160 nm flatness). Without magnification, interferometry, and comparison techniques, there is no way to confirm that a lens surface is correct, a machined part meets tolerance, or a semiconductor wafer is defect-free. Optical inspection bridges the gap between what the machine produces and what the specification demands.

### Prerequisites

- [Glass production](../glass/index.md) — optical glass blanks for lenses and flats
- [Machine tools](../machine-tools/index.md) — grinding, lapping, and polishing capability
- [Abrasives](../machine-tools/bearings-abrasives.md) — SiC, emery, cerium oxide for grinding and polishing
- [Measurement fundamentals](../measurement/index.md) — calibration and traceability concepts
- [Light sources](../energy/electricity.md) — monochromatic light for interferometric testing

### Optics & Inspection

**Lens grinding and polishing**:
- **Rough grinding**: Fix glass blank to convex or concave cast iron tool (curve matched to desired radius). Add coarse abrasive (60-120 grit SiC or emery) and water. Stroke blank across tool in random pattern. Check radius with spherometer or template. Duration: 2-8 hours depending on size and depth.
- **Fine grinding**: Progress through finer abrasives (220, 320, 400, 600 grit). Each stage removes scratches from previous stage. Rinse thoroughly between grits (cross-contamination ruins finish).
- **Polishing**: Iron or pitch lap (pitch conforms to glass surface). Polishing compound: cerium oxide (CeO₂) slurry in water, or rouge (Fe₂O₃). Duration: 2-12 hours for optical quality. Test with laser or monochromatic light — interference fringes reveal surface errors.
- **Flat surfaces**: Use three-plate method (same principle as surface plate scraping). Grind three glass plates alternately until all show uniform contact.
- **Spherical surfaces**: Use full-diameter tool for convex, channel tool for concave. Test with knife-edge (Foucault test) for mirror surfaces — reveals zones and irregularities as shadows.
- **Surface quality targets**: Scratch/dig 60/40 for visual optics, 20/10 for imaging optics, 10/5 for laser optics. Measured under controlled illumination against standards.

**[Microscopes](../glossary/microscopes.md)** (critical for semiconductor inspection):
- **Compound microscope**: Objective lens (4x-100x) + eyepiece (10x). Total magnification 40x-1000x. Resolution limited by diffraction: ~λ/(2·NA) where NA = numerical aperture. At NA 0.65 with visible light: ~0.4 μm resolution.
- **Objective design**: Achromatic doublet (crown + flint glass, corrects chromatic aberration at two wavelengths) or apochromatic (three-element, three-wavelength correction — better, harder to make).
- **Illumination**: Brightfield (transmitted light through sample), darkfield (oblique illumination — edges glow, defects visible). Later: phase contrast, DIC (differential interference contrast).
- **Mechanical stage**: X-Y movement with graduated drums (0.01 mm resolution). Focus: coarse + fine (0.001 mm resolution). Requires Machine Tools stage precision machining.
- **Applications**: Crystal defect inspection (Silicon), lithography alignment (Photolithography), defect analysis, biological specimens.

**[Optical comparators](../glossary/optical-comparators.md)** (shadow projection for dimensional measurement):
- Light source projects silhouette of part onto screen. Magnification 10-50x. Compare shadow against overlay drawing (mylar with tolerance bands). Quick, non-contact measurement of external dimensions.

**[Spectroscopes](../glossary/spectroscopes.md)** (optional — material identification):
- **Prism spectroscope**: White light through slit → prism → splits into spectrum. Observe emission or absorption lines. Each element has unique spectral fingerprint.
- **Flame spectroscopy**: Dip sample in flame → characteristic color (Na = yellow, Cu = green/blue, Li = red, K = violet). Quick qualitative analysis.
- **Applications**: Ore identification, alloy verification, chemical analysis, astronomical observation.

### Telescope Construction

**[Refracting telescopes](../glossary/refracting-telescopes.md)** (lens-based):
- **Objective lens**: Grind and polish a large plano-convex or biconvex lens (crown glass). Focal length f = R/(n-1) for plano-convex. Typical amateur: 50-80 mm diameter, f/10-f/15 (500-1200 mm focal length).
- **Eyepiece**: Short-focus convex lens (Huygens: 2-element; later Ramsden, Kellner). Magnification = f_objective / f_eyepiece.
- **Tube construction**: Cardboard or rolled brass tube, blackened interior to reduce stray light. Diameter slightly larger than objective. Focuser tube slides for adjustment.
- **Mount types**: Alt-azimuth (simple up-down, left-right) for basic use. Equatorial mount (polar axis aligned to celestial pole) enables tracking by rotating one axis. Chromatic aberration: single lens shows color fringing; achromatic doublet (crown + flint) reduces it.

**[Reflecting telescopes](../glossary/reflecting-telescopes.md)** (mirror-based, no chromatic aberration):
- **Newtonian**: Flat diagonal (secondary) mirror deflects focus to side of tube. Simplest reflecting design. Primary mirror: parabolic. Most common amateur design.
- **Cassegrain**: Hyperbolic secondary reflects focus back through hole in primary. Compact tube, long effective focal length. More complex optics (two non-spherical surfaces).

### Mirror Grinding Procedure

**[Rough grinding](../glossary/rough-grinding.md)** (generating the curve):
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

**[Parabolizing](../glossary/parabolizing.md)** (figuring the sphere into a paraboloid):
- A sphere focuses parallel light to a zone, not a point. Paraboloid corrects this for on-axis images. Required for f-ratios faster than ~f/8.
- **Overhang stroke**: Extend mirror past lap edge by ~1/3 diameter on each stroke — wears center faster than edge, deepening central curve toward paraboloid.
- **Petal lap**: Modify pitch lap by cutting away petals — selective contact controls which zones are polished. Advanced technique for precise figure control.
- **[Foucault test](../glossary/foucault-test.md)** (knife-edge test): Place point light source at radius of curvature. Move razor blade across returning cone of light. Shadows reveal zones: sphere shows uniform gray; paraboloid shows characteristic "doughnut" shadow pattern. Measure zonal radii with Couder mask to quantify deviation from paraboloid.

### Prism Fabrication

- **Blank preparation**: Select optical glass block (BK7 equivalent or flint glass). Cut to rough prism shape with diamond saw or wire saw with SiC slurry.
- **Angle control**: Grind two refracting faces to specified angle (60° for equilateral dispersing prism, other angles for special purposes). Use sine bar or angle gauge to set grinding fixture. Tolerance: ±0.1° for spectroscopic use, ±0.01° for precision optics.
- **Fine grinding and polishing**: Same sequence as lens work (220 → 1200 grit → CeO₂ polish). Polish each face individually on flat lap. Faces must be flat to λ/4 (quarter-wavelength) over full aperture.
- **Testing**: Illuminate with collimated white light through slit → prism → observe spectrum on screen or with telescope. Sharp spectral lines indicate good polish and correct angle. Spectroscope built from own output — first instrument can certify subsequent ones.

### Optical Coatings

- **[Anti-reflection coating](../glossary/anti-reflection-coating.md)** (single-layer MgF₂):
  - Magnesium fluoride (MgF₂) deposited on lens surface. Thickness: λ/4 (quarter-wavelength, ~100 nm for center of visible spectrum). Refractive index n ≈ 1.38, between air (1.0) and glass (~1.5).
  - Reduces surface reflection from ~4% to ~1.3% per surface. On a 4-element lens (8 surfaces): transmission improves from ~72% to ~90%.
  - Deposition: thermal evaporation in vacuum chamber at 10⁻⁴ Pa (10⁻⁶ Torr). Heat MgF₂ in tungsten boat until it sublimes. Vapor condenses on rotating lens above. Monitor thickness with quartz crystal microbalance.
  - **Requires**: vacuum technology (rotary vane pump + diffusion pump), tungsten heating elements, MgF₂ source material.

- **[Mirror coating](../glossary/mirror-coating.md)** (aluminum):
  - Evaporate high-purity aluminum in vacuum at 10⁻⁴ Pa. Tungsten filament or boat, heated to melt aluminum (660°C) then to evaporation (~1200°C). Vapor deposits on mirror substrate above.
  - Reflectivity: ~92% for fresh aluminum (vs ~85% for silver, which tarnishes). Protective overcoat of SiO₂ (quarter-wave) extends lifetime.
  - **Requires**: same vacuum infrastructure as anti-reflection coating, plus aluminum source material.

### Optional: Vacuum Tube Electronics

- Not strictly required for semiconductor path, but provides:
  - Amplification experience (useful for test equipment)
  - Radio communication capability (valuable for coordination)
  - Understanding of electron physics
- **Requires**: Glass envelopes (glassblowing capability above), vacuum (rotary vane pump sufficient), cathode material (tungsten or thoriated tungsten — heated to emit electrons), anode (nickel plate), grid (fine wire spiral for triode), base and pins (glass-to-metal seals).
- **Evacuation**: Pump down to 10⁻⁴ Torr, bake tube to 300-400°C during pumping to drive off adsorbed gases, seal off. Getter (barium or magnesium flash strip) inside tube — flashes during initial activation, absorbs residual gases.

### Safety & Hazards

- **Laser eye hazards**: Alignment and testing lasers (even low-power HeNe at 1-5 mW) can cause permanent retinal burns from direct or reflected beam exposure. Never look into beam path. Use laser safety goggles matched to wavelength. Enclose beam paths where feasible.
- **Chemical etchants**: Lens and prism preparation may use hydrofluoric acid (HF) for glass etching — HF penetrates skin, attacks bone, causes delayed deep-tissue necrosis. Calcium gluconate gel must be available as first aid. Cerium oxide and rouge (Fe₂O₃) polishing slurries are low hazard but avoid inhalation of dried powders.
- **Vacuum chamber implosion**: Glass vacuum tubes and bell jars under vacuum can collapse violently. Wrap with tape or mesh, wear face shield during evacuation. Never use chipped or scratched glassware under vacuum.

### Visual Inspection Standards

**Scratch and dig classification (MIL-PRF-13830)**:
- The military specification for optical component surface quality. Every polished optical surface has minor imperfections. Scratch/dig specifies the maximum allowable size.
- **Scratch number**: 10, 20, 40, 60, 80. The number is NOT a physical dimension in any unit. It is a brightness comparison: a scratch of number S has the same scattering brightness as a standard scratch of width S μm when viewed under specified illumination. A scratch of number 10 is barely visible under 10× magnification; scratch 80 is visible to the naked eye.
- **Dig number**: Directly specifies the maximum dig (pit) diameter in hundredths of a millimeter. Dig 5 means pits no larger than 0.5 mm diameter. Dig 0.2 means pits no larger than 0.02 mm (20 μm).
- **Typical specifications**: 60/40 for general visual optics (eyepieces, finderscopes). 40/20 for camera lenses and binoculars. 20/10 for imaging optics and precision instruments. 10/5 for laser optics and photolithography lenses (any defect scatters laser energy or creates imaging artifacts).
- **Inspection method**: View the surface against a dark background with a bright, collimated light source at 5-10× magnification for routine inspection. Use 20-50× magnification for scratch/dig 20/10 and better. Compare suspect features against certified standard scratches on a reference piece. The inspection is subjective and requires trained operators.

### Interferometric Flatness Measurement

**Fizeau interferometer**:
- The workhorse instrument for measuring surface flatness and transmitted wavefront quality of optical components. A laser beam (typically HeNe, 632.8 nm) is expanded and collimated, then directed through a reference flat (a fused silica reference surface of known flatness, typically λ/20 or better). The reference flat and the test surface are placed in close proximity with a small wedge angle. Reflected beams from the two surfaces interfere, producing fringe patterns.
- **Fringe interpretation**: Each fringe represents one wavelength (632.8 nm) of height difference between the reference and test surfaces. Straight, equally-spaced fringes indicate a flat surface. Curved or irregular fringes indicate surface errors. A deviation of one fringe from straightness = λ (632.8 nm or ~0.63 μm) surface error. Modern digital interferometers capture fringe images and compute surface maps automatically.
- **Accuracy**: λ/20 (~32 nm) for a good Fizeau interferometer with a λ/20 reference flat. The reference flat is the accuracy limiter. For higher accuracy, use a calibrated reference and subtract its known errors from the measurement.
- **Applications**: Measure flatness of optical flats, mirror substrates, prism faces, and semiconductor wafer chucks. Measure parallelism of windows (transmitted wavefront). Measure radius of curvature of lenses (by measuring test plate contact fringes).

**Twyman-Green interferometer**:
- A variant suited for testing transmitted wavefront through a complete optical system (lenses, prisms, windows). The beam is split into reference and test arms. The test arm passes through the optic under test. The recombined beams form interference fringes that reveal the total wavefront error (surface figure + internal homogeneity + refractive index variations).
- Used to certify complete lens assemblies and imaging systems. A camera lens specified as λ/4 wavefront error is tested on a Twyman-Green or similar interferometer.

### Surface Roughness Measurement

**Stylus profilometer**:
- A diamond-tipped stylus (tip radius 2-5 μm) is drawn across the surface at constant speed (10-100 μm/s) with a light contact force (0.5-1.0 mg). The stylus rides over surface irregularities, and its vertical displacement is measured by an inductive or capacitive transducer. The vertical signal is recorded as a profile of surface height vs. position.
- **Vertical resolution**: 0.1 nm (1 Å) for a good stylus profilometer. Horizontal resolution limited by stylus tip radius (~2 μm). Features smaller than the tip radius are averaged out.
- **Scan length**: 50 μm to several millimeters. Longer scans average over larger areas. Short scans capture fine structure.
- **Output parameters**: Ra (arithmetic average roughness, typically 0.5-10 nm for polished optics), Rq (RMS roughness), Rz (average peak-to-valley height). For a well-polished optical surface, Ra < 1 nm.
- **Limitations**: The stylus contacts the surface, risking damage on soft coatings. Slow (one profile at a time). Does not provide a 2D surface map without repeated scans.

**White light interferometer (optical profilometer)**:
- Non-contact surface measurement using white light interferometry. A Michelson or Mirau interferometer objective focuses on the test surface. When the surface is at the exact focal position of the reference mirror, interference fringes appear with maximum contrast. A vertical scan maps the fringe contrast vs. height position at each pixel, producing a 3D surface height map.
- **Vertical resolution**: 0.01 nm (0.1 Å). Lateral resolution: ~0.5 μm (limited by microscope objective NA). Field of view: 50-500 μm depending on objective magnification.
- **Advantage over stylus**: non-contact (no damage risk), fast (full 3D map in seconds), higher vertical resolution. Especially suited for measuring polished optical surfaces, thin film step heights, and MEMS devices.
- **Limitation**: requires a reflective surface (transparent samples may need a thin metallic coating). Vibration-sensitive during measurement.

### Dimensional Inspection

**Optical comparator**:
- Projects a magnified silhouette of the part onto a screen (10-100× magnification). The operator compares the shadow against a mylar overlay drawing with tolerance bands, or measures dimensions directly on the screen with digital readout.
- Applications: thread profiles, gear tooth profiles, small machined parts, stamped components. Quick, non-contact, and suited for production floor inspection where coordinate measuring machines are too slow or expensive. Accuracy: ±0.01 mm at 20× magnification.
- Chart projection: the screen is a ground glass disk. A collimated light source illuminates the part from behind, casting a sharp shadow. The lens system determines magnification. Longer working distance objectives measure thicker parts. Helix adjustment on the stage tilts screw threads to present a true profile.

**Toolmaker's microscope**:
- A precision measuring microscope with a coordinate stage (X-Y travel 50-150 mm, readout resolution 0.001 mm). The stage uses linear encoder scales for direct digital position readout. Crosshair eyepiece or video camera with on-screen measurement cursors. Magnification: 10-200×.
- Applications: measure small feature dimensions (hole diameters, thread pitch, gear tooth spacing), angles (rotary stage or protractor eyepiece with 1 arc-minute resolution), and distances between features. The 0.001 mm (1 μm) resolution makes it suitable for inspecting precision machined parts, gauge blocks, and small optical components.

### Defect Classification for Optical Glass

Per MIL-G-174B (military specification for optical glass), defects are classified by type:

- **Scratches**: Linear marks on the polished surface from grinding, polishing, or handling. Classified by length and visibility. Long scratches (>10 mm) are more serious than short scratches of equal brightness because they intercept a larger portion of the light path.
- **Digs (pits)**: Circular or irregular depressions in the surface. Caused by abrasive inclusions, bubble exposure during polishing, or impact. Classified by diameter. Multiple small digs are less harmful than one large dig of equivalent total area.
- **Bubbles**: Internal gas-filled voids trapped during glass melting. Appear as bright spots when viewed with side illumination. Classified by diameter and number per unit volume. Small bubbles (<0.1 mm) scatter some light but are acceptable in most visual optics. Large bubbles (>0.5 mm) are rejectable for precision lenses.
- **Inclusions (stones, cords)**: Solid particles (unmelted batch material, refractory fragments) or streaks (composition variation from incomplete mixing) within the glass body. Stones scatter light and cause localized stress. Cords produce refractive index variations that distort transmitted wavefront. Both detected by schlieren or shadowgraph inspection.
- **Striae**: Thread-like regions of slightly different refractive index, caused by incomplete homogenization during melting. Visible as wavy distortions when viewing a grid pattern through the glass. Grade A striae (none visible) required for precision lenses. Grade B (minor striae) acceptable for illumination and condenser optics.

### Optical Assembly and Alignment

Building functional optical instruments from individual components requires systematic alignment:

- **Lens centering**: A lens must be mounted so that its mechanical axis coincides with its optical axis. Mount the lens in a precision cell on a lathe. Shine a laser through the lens while rotating the cell. If the reflected or transmitted beam wobbles, the lens is decentered. Adjust until the beam is stationary during rotation. Centration tolerance: 0.01-0.1 mm depending on the application.
- **Collimation testing**: Point a laser through the assembled optical system. Project the output beam onto a distant wall (10-30 m). A collimated beam maintains constant diameter at all distances. A converging beam shrinks; a diverging beam expands. Adjust spacing between lens elements until the beam diameter is constant across the test distance.
- **Star test**: Observe a point source (distant star or artificial pinhole) through the completed optical instrument. A perfect optical system produces a clean Airy disk (bright central spot surrounded by concentric diffraction rings). Aberrations distort the pattern: spherical aberration shows rings that are too bright; astigmatism shows a cross pattern; coma shows an asymmetric comet-shaped flare. This is the most sensitive test for overall image quality, capable of detecting wavefront errors of λ/10 or less.

### Environmental Testing of Optical Components

Optical components used in field instruments, military systems, and industrial environments must maintain performance under harsh conditions. Environmental testing verifies that coatings, cements, and substrate materials survive thermal, humidity, and mechanical stress without degradation.

**Temperature cycling**: Subject the optical component to repeated cycles between temperature extremes (typically -40°C to +80°C for military specification, 0°C to +60°C for commercial). Each cycle: ramp to cold extreme, hold 1 hour, ramp to hot extreme, hold 1 hour, return to ambient. Typical test: 20-100 cycles. Inspect after test for coating crazing (fine crack network caused by differential thermal expansion between coating and substrate), cement failure (Canada balsam or synthetic cement separating in doublet lenses), and glass fracture from residual stress. Measure transmitted wavefront before and after to detect figure distortion from thermal stress relief.

**Humidity resistance**: Expose the component to 95% relative humidity at 40-50°C for 24-96 hours (per MIL-STD-810). Tests coating adhesion and corrosion resistance. Moisture penetrates porous films (thermally evaporated coatings without IAD), causing optical performance to shift. Salt spray exposure (5% NaCl fog at 35°C, per ASTM B117) tests corrosion resistance of mirror coatings and metal housings. Bare aluminum mirrors corrode rapidly in salt spray; protected mirrors (SiO₂ overcoat) survive 48-96 hours without degradation.

**Abrasion testing**: Coating durability tested by rubbing with standard abrasive media under controlled conditions. Cheesecloth test (MIL-C-675): rub coated surface with cheesecloth pad (50 g force applied through a 6 mm diameter pad) for 25 cycles. Eraser test (MIL-C-48497): rub with standard eraser under 500-1000 g force for 20-50 cycles. Inspect for coating removal, scratching, or haze. Hard coatings (MgF₂, SiO₂) pass both tests easily. Soft coatings (silver, gold without overcoat) fail abrasion tests and require protective overcoats for any application involving handling.

**Adhesion testing**: Cross-hatch tape test per ASTM D3359: score a grid pattern (11 cuts in each direction, 1 mm spacing) through the coating to the substrate. Apply pressure-sensitive tape over the grid. Rub to ensure contact. Pull tape off rapidly at 180° angle. Inspect grid squares for coating removal. Rating 5B (no removal) required for military optics. Rating 3B or below indicates adhesion failure requiring process correction (typically insufficient substrate cleaning or missing plasma pretreatment step).

### Acceptance Sampling and Quality Assurance

Not every optical component can be inspected 100% (batch sizes in the hundreds or thousands make full inspection impractical). Statistical acceptance sampling determines how many pieces from a lot to inspect and what defect rate is acceptable.

**MIL-STD-105 (now ASTM E2234 / ISO 2859)**: The standard acceptance sampling system for attribute inspection. Given a lot size and an acceptable quality level (AQL), the standard specifies the sample size and the acceptance/rejection criteria (maximum number of defects allowed in the sample).

- **AQL selection**: AQL 0.65% for critical optics (laser lenses, photolithography elements, where any defect causes system failure). AQL 1.0% for imaging optics (camera lenses, telescope objectives). AQL 2.5% for general visual optics (viewfinders, illumination lenses, magnifiers). AQL 4.0% for non-critical components (windows, protective covers).
- **Inspection levels**: Normal inspection for routine production. Tightened inspection (larger sample, stricter criteria) when 2 of 5 consecutive lots are rejected. Reduced inspection (smaller sample) when 5 consecutive lots pass, indicating a stable, capable process.
- **Lot disposition**: If the number of defective units in the sample does not exceed the acceptance number, the lot passes. If it exceeds the acceptance number but not the rejection number, the lot is held for further review. If it exceeds the rejection number, the lot is rejected and returned for 100% screening or rework.

**Measurement system verification**: Before any acceptance inspection, verify that the measurement instruments themselves are accurate. Interferometers checked with certified reference flats (λ/20 traceable to national standards). Profilometers calibrated with step height standards (NIST-traceable). Microscopes verified with stage micrometers. Comparator magnification checked with glass scale standards. A measurement system analysis (Gage R&R) quantifies how much of the observed variation comes from the instrument vs. the part. If the measurement system contributes more than 10-30% of total observed variation, the instrument needs recalibration or replacement before it can reliably accept or reject parts.

**Documentation and traceability**: Each inspected component receives an inspection record documenting: part number, serial number, lot number, inspection date, inspector identity, instruments used (with calibration dates and serial numbers), measurements taken (with actual values and pass/fail against specification), and any deviations or non-conformances. This traceability is essential for high-reliability applications (aerospace, military, medical) where a component failure must be traceable back to its inspection records. Non-conforming parts are tagged, segregated from conforming inventory, and dispositioned by a review board (rework, use-as-is with engineering approval, or scrap).

**First-article inspection**: When a new optical component enters production, the first produced unit (or first three units from a new batch) undergoes complete dimensional, optical, and environmental inspection against the full specification. This first-article inspection verifies that the production process (tooling, machine settings, coating parameters) produces parts that meet every requirement, not just the ones checked during routine production sampling. Any out-of-tolerance dimension or optical parameter requires a process correction before production continues. First-article approval is a prerequisite for production release in military and aerospace contracts.

**Certificate of conformance**: Each lot of optical components ships with a certificate listing the measured values of all specified parameters (surface figure, scratch/dig, transmitted wavefront error, coating reflectance or transmittance curve, dimensional measurements). The certificate references the applicable drawing, specification, and purchase order. The inspector who performed the final inspection signs the certificate. For critical components (laser optics, lithography lenses), individual serialized test data accompanies each piece rather than a lot-level summary.

## Limitations

- **Subjectivity of visual inspection**: Visual inspection depends on the inspector's skill, experience, alertness, and consistency. Fatigue, lighting conditions, and individual visual acuity all affect defect detection rates. Studies show visual inspection catches 70-90% of defects under ideal conditions, declining significantly with fatigue or poor lighting.
- **Resolution limits**: Unaided human vision resolves ~100 μm features at 25 cm viewing distance. Magnification (loupes, microscopes) extends this to ~1 μm at 1000×. Sub-micron defects require interferometric or electron microscopy techniques beyond bootstrap capability.
- **No automated inspection**: Machine vision and automated optical inspection (AOI) require cameras, computers, and image processing software unavailable until the electronics and computing stages. All inspection is manual and therefore slow relative to automated systems.
- **Surface preparation dependency**: Inspection accuracy depends on surface cleanliness and preparation. A scratch may be hidden by oil film; contamination may be mistaken for a surface defect. Proper cleaning (solvent wash, lint-free wipes) must precede critical inspections.
- **Traceability gaps**: Without calibrated reference standards traceable to national metrology institutes, dimensional measurements have uncertain accuracy. Gauge blocks, optical flats, and angle standards provide local references but their absolute accuracy degrades over time through wear and corrosion.

### Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Interference fringes irregular (flat test) | Optical flat or test piece contaminated, or flat is worn | Clean both surfaces with solvent and lint-free wipe; re-press flat if pitch-lapped; verify flat against reference |
| Foucault test shows no shadow transition | Knife edge not at focus, or mirror has severe zones | Adjust knife-edge position laterally; verify light source alignment; check mirror for severe astigmatism |
| Microscope image blurry at high power | Objective not focused, oil immersion missing (for oil-type), or cover slip wrong thickness | Focus with coarse then fine adjustment; use immersion oil for 100× objectives; use 0.17 mm cover slips |
| Scratches appear after polishing | Abrasive cross-contamination between grit stages | Clean work area, tools, and glass thoroughly between grits; use separate containers for each grit |
| Spherometer readings inconsistent | Contact points worn, dirty, or spherometer not zeroed on reference flat | Clean contact points; zero on optical flat before each measurement session |
| Optical comparator silhouette unclear | Projector lamp misaligned or screen dirty | Align lamp filament; clean projector screen; verify magnification with stage micrometer |

## See Also

- [Precision Instruments](precision-instruments.md) — optical flats, lens manufacturing, autocollimators
- [Optical Coatings](optical-coatings.md) — coating application and quality verification
- [Measurement](../measurement/index.md) — precision metrology, optical instruments
- [Glass](../glass/index.md) — optical glass quality and defect classification
- [Machine Tools](../machine-tools/index.md) — surface finish standards for machined parts
- [Photolithography](../vlsi-scaling/advanced-lithography.md) — wafer inspection at semiconductor scale

[← Back to Optics](index.md)
