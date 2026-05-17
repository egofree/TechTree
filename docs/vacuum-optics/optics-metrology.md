# Optics & Inspection

> **Node ID**: `vacuum-optics.optics-inspection`
> **Domain**: [Vacuum, Optics & Advanced Glass](./)
> **Enables**: `vlsi-scaling.advanced-lithography`
> **Timeline**: Years 25-40
> **Outputs**: lenses, microscopes, optical_comparators, thermocouples, temperature_measurement, electrical_measurement

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
- **Applications**: Crystal defect inspection (Silicon), lithography alignment (Photolithography), defect analysis (Photolithography+), biological specimens (SQ5).

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
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
