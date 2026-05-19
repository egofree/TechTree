# Optical Coatings

> **Node ID**: optics.inspection.optical-coatings
> **Domain**: [Optics](./)
> **Dependencies**: `optics.inspection`, `vacuum.basics`
> **Enables**: `vlsi-scaling.advanced-lithography`, `optics.precise-instruments`
> **Timeline**: Years 30-40
> **Outputs**: ar_coated_lenses, aluminized_mirrors, coated_optical_components

### Why Optical Coatings Matter

Every air-glass interface reflects a portion of incident light. For uncoated glass (refractive index n ≈ 1.5), Fresnel reflection at normal incidence is approximately 4% per surface ((n-1)/(n+1))² = (0.5/2.5)² = 0.04). A simple camera lens with 4 elements (8 air-glass surfaces) transmits only ~72% of entering light — 28% is lost to reflections. These reflections also cause ghost images, flare, and reduced contrast.

Anti-reflection (AR) coatings reduce surface reflections, increasing light transmission and image quality. Reflective coatings maximize mirror reflectivity for telescopes, beam delivery, and illumination systems. Both are essential for precision optical instruments.

### Vacuum Deposition Fundamentals

Optical coatings are applied by **thermal evaporation** in a vacuum chamber — the most accessible deposition technology at bootstrap stage.

**Vacuum requirements**:
- Base pressure: 10⁻³ to 10⁻⁴ Pa (10⁻⁵ to 10⁻⁶ Torr). This ensures evaporated coating material travels in a straight line from source to substrate without scattering off residual gas molecules. Higher pressures cause porous, poorly adherent films with reduced optical quality.
- Pumping system: Rotary vane (oil-sealed) backing pump achieves ~1 Pa. Add a diffusion pump (oil vapor) or turbomolecular pump for high vacuum. The diffusion pump is simpler and more robust at bootstrap stage — requires only an oil heater and cooled baffle, no precision bearings.
- Chamber: Steel or glass bell jar, 30-50 cm diameter, with vacuum flanges, electrical feedthroughs (for heater power and thickness monitor), viewing ports, and substrate rotation mechanism.

**Thermal evaporation process**:
1. **Clean substrates**: Ultrasonic clean glass or mirror substrates in detergent, rinse in deionized water, rinse in ethanol, dry with clean air or nitrogen. Any surface contamination (dust, oils, fingerprints) produces coating defects — pinholes, adhesion failure, or scattering sites.
2. **Load chamber**: Place substrates on a rotating holder above the evaporation source. Rotation ensures uniform coating thickness across all surfaces — a flat, stationary substrate receives a coating that is thicker in the center (directly above source) than at the edges (cosine distribution).
3. **Pump down**: Close chamber, start backing pump. When chamber pressure reaches ~10 Pa, start diffusion pump (or turbomolecular pump). Wait for base pressure to stabilize at 10⁻⁴ Pa or better. Typical pump-down time: 30-60 minutes.
4. **Pre-deposition**: Heat the evaporation source briefly with shutter closed. This outgasses residual contaminants from the source material. Wait for pressure to recover to base level.
5. **Deposit**: Open shutter. Heat source material to evaporation temperature. Vapor travels upward and condenses on substrate surfaces. Monitor thickness in real-time. Close shutter when target thickness is reached.
6. **Cool and vent**: Allow substrates to cool (10-20 minutes) before venting chamber. Rapid cooling can cause thermal stress cracking in the coating. Vent with dry nitrogen if available (prevents moisture condensation on fresh coating).

### Anti-Reflection Coating: Single-Layer MgF₂

**Principle**: A single thin layer of magnesium fluoride (MgF₂) on a glass surface reduces reflection by destructive interference. Light reflected from the air-MgF₂ interface and the MgF₂-glass interface travel different optical path lengths. At the target wavelength, these reflected waves are exactly out of phase (180° difference) and cancel each other.

**Design parameters**:
- **Material**: Magnesium fluoride (MgF₂), refractive index n ≈ 1.38. This is between air (n = 1.0) and glass (n ≈ 1.5), which is necessary — the intermediate index ensures the two reflected waves have comparable amplitudes (necessary for effective cancellation).
- **Thickness**: λ/4 optical thickness = λ/(4n) physical thickness. For center of visible spectrum (λ = 550 nm): thickness = 550/(4 × 1.38) = ~100 nm. At this thickness, the coating provides optimal anti-reflection at 550 nm (green) and reduced reflection across the visible band.
- **Deposition**: Sublime MgF₂ from a tungsten boat or molybdenum crucible. MgF₂ sublimes (transitions directly from solid to vapor) at ~1200°C without melting, which simplifies the process. Tungsten boats are heated by passing high current (10-50 A at low voltage, ~3-10 V) through them.

**Performance**:
- Reduces surface reflection from ~4% to ~1.3% per surface at 550 nm.
- Transmission improvement: a 4-element lens (8 surfaces) goes from ~72% to ~90% total transmission.
- Wavelength dependence: optimal at the design wavelength, less effective at shorter and longer wavelengths. Reflection increases to ~2% at the extremes of the visible spectrum (400 nm and 700 nm). This residual reflection gives coated lenses a characteristic purple/violet tint (reflected light peaks at wavelengths where coating is less effective — blue and red).
- Limitation: single-layer MgF₂ is adequate for BK7-type glass (n ≈ 1.52) but less effective for high-index glass (n > 1.7), where the index mismatch between MgF₂ and glass is larger. Multi-layer coatings (2-7+ layers of alternating high and low index materials) achieve <0.5% reflection across the full visible band but require precise thickness control and multiple deposition steps.

### Mirror Coating: Aluminum

**Principle**: Evaporate a thin layer of pure aluminum onto a polished glass (or other) substrate. The aluminum layer, typically 80-150 nm thick, forms a highly reflective metallic surface.

**Deposition**:
- **Source**: High-purity aluminum wire (99.99%) coiled in a tungsten basket or boat. Aluminum melts at 660°C and evaporates rapidly at ~1200°C.
- **Process**: Heat tungsten basket to melt aluminum. Once molten, aluminum wets the tungsten and spreads, increasing surface area for evaporation. The evaporation rate is fast — a typical 100 nm coating deposits in 10-30 seconds.
- **Substrate preparation**: The mirror substrate must be optically polished (surface quality λ/10 or better, where λ = 550 nm — surface errors < 55 nm peak-to-valley). The coating faithfully replicates the substrate surface — any scratches or irregularities are preserved in the reflective surface.

**Performance**:
- **Fresh aluminum**: ~92% reflectivity across the visible spectrum (400-700 nm). Relatively uniform — aluminum is a broadband reflector, unlike silver which varies more across wavelengths.
- **Protective overcoat**: Bare aluminum oxidizes quickly in air, forming a thin (2-5 nm) Al₂O₃ layer. This native oxide stabilizes the surface and is transparent, so it does not significantly reduce reflectivity. For enhanced protection (against abrasion and chemical attack), apply a quarter-wave layer of SiO₂ (silicon dioxide) over the aluminum. The SiO₂ overcoat extends mirror life significantly with minimal reflectance loss (<1%).
- **Comparison with silver**: Silver has higher peak reflectivity (~95% at 550 nm) but tarnishes rapidly in air (sulfide formation, turning dark). Aluminum is preferred for general-purpose mirrors due to its stability and ease of application. Silver requires a protective overcoat (SiO₂, MgF₂, or Al₂O₃) and is used where maximum reflectivity is critical.

### Thickness Monitoring

Precise control of coating thickness is essential — the difference between a functional AR coating and a useless one is ~10 nm (10% of the target thickness).

**Quartz crystal microbalance (QCM)**:
- A thin quartz crystal oscillates at its resonant frequency (~5-6 MHz). As coating material deposits on the crystal surface, the added mass decreases the resonant frequency.
- Frequency shift is proportional to deposited mass: Δf = -C × Δm, where C is a calibration constant determined by the crystal properties.
- The crystal is mounted in the vacuum chamber next to the substrates. An oscillator circuit drives the crystal and measures frequency. A digital display shows frequency change, which is calibrated to read thickness directly.
- Accuracy: typically ±1-2 nm for thin films. Sensitive to temperature (crystal frequency shifts ~1 ppm/°C) — temperature control or compensation is needed for best accuracy.
- Limitation: the crystal must be replaced periodically as coating builds up (crystal sensitivity degrades with thickness). Each crystal is good for ~10-20 depositions.

**Optical monitoring (alternative)**:
- Monitor transmission or reflection of a test glass through a viewport in the vacuum chamber using a light source and detector.
- As coating thickness increases, the optical signal oscillates (constructive/destructive interference). The signal passes through extrema (maxima or minima) at each quarter-wave thickness increment.
- Advantages: directly measures optical thickness (what matters for coating function), insensitive to temperature. Disadvantage: requires optical access through viewport and more complex setup.

### Coating Defects and Troubleshooting

- **Pinholes**: Small uncoated spots caused by dust on the substrate or spitting from the evaporation source. Prevent by thorough substrate cleaning and pre-melting source material with shutter closed. Pinholes scatter light and reduce coating performance.
- **Poor adhesion**: Coating flakes or rubs off substrate. Caused by contaminated substrates (oils, fingerprints) or insufficient substrate cleaning. Plasma cleaning (glow discharge in vacuum) immediately before deposition improves adhesion by removing the last molecular layers of contamination.
- **Non-uniform thickness**: Uneven coating across substrate. Caused by incorrect source-substrate geometry or insufficient substrate rotation. Ensure substrate rotates during deposition and that source-to-substrate distance is appropriate (typically 25-40 cm).
- **Stress cracking**: Coating cracks after removal from vacuum. Caused by excessive thermal stress (substrate too hot during deposition) or intrinsic stress in the film. MgF₂ tends toward compressive stress; aluminum has tensile stress. Control deposition rate and substrate temperature.
- **Haze/scattering**: Coated surface appears foggy rather than clear. Caused by porous film (deposited at too high a chamber pressure), or by micro-particles from a dirty chamber. Clean chamber regularly. Ensure adequate base pressure before deposition.

### Safety & Hazards

- **Vacuum chamber implosion**: Glass bell jars and vacuum chambers under vacuum can collapse violently if cracked or chipped. Wrap glass bell jars with tape or mesh for fragmentation retention. Inspect for chips, scratches, and star cracks before every use — never use damaged glassware under vacuum. Metal chambers are preferred for safety. Wear face shield when pumping down or venting.
- **Hot evaporation sources**: Tungsten boats and baskets operate at 1200-2000°C during deposition — glowing yellow-white. Severe thermal burns on contact. Allow sources to cool fully (10-20 minutes) before opening chamber. Handle boats with tongs during loading and unloading.
- **Toxic coating materials**: MgF₂ dust is moderately toxic if inhaled (fluoride compounds affect bone and kidneys). Handle powder source material with gloves and dust mask. Avoid generating dust. Aluminum is lower hazard but fine powder is a fire and inhalation risk.
- **Vacuum pump fluids**: Diffusion pumps use silicone or hydrocarbon oil that can backstream into the chamber and contaminate coatings. Use a cold trap (liquid nitrogen or chilled baffle) between pump and chamber. Diffusion pump oil is hot during operation (~200°C) — thermal burn risk if pump is opened while hot.
- **Electrical hazards**: Evaporation sources carry high current (10-50 A) at low voltage (3-10 V) from a heavy-duty power supply. The current is sufficient to cause severe burns or fire if cables short. Insulate all connections. Use properly rated cables and connectors. Interlock the chamber door to cut power when opened.

---

*Part of the [Bootciv Tech Tree](../) • [Optics](./) • [All Domains](../)*
