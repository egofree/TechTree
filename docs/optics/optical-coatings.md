# Optical Coatings

> **Node ID**: optics.inspection.optical-coatings
> **Domain**: [Optics](./index.md)
> **Dependencies**: [`optics.inspection`](inspection.md), `vacuum.basics`
> **Enables**: [`vlsi-scaling.advanced-lithography`](../vlsi-scaling/advanced-lithography.md), `optics.precise-instruments`
> **Timeline**: Years 30-40
> **Outputs**: ar_coated_lenses, aluminized_mirrors, coated_optical_components

### Why Optical Coatings Matter

Every air-glass interface reflects a portion of incident light. For uncoated glass (refractive index n ≈ 1.5), Fresnel reflection at normal incidence is approximately 4% per surface ((n-1)/(n+1))² = (0.5/2.5)² = 0.04). A simple camera lens with 4 elements (8 air-glass surfaces) transmits only ~72% of entering light — 28% is lost to reflections. These reflections also cause ghost images, flare, and reduced contrast.

Anti-reflection (AR) coatings reduce surface reflections, increasing light transmission and image quality. Reflective coatings maximize mirror reflectivity for telescopes, beam delivery, and illumination systems. Both are essential for precision optical instruments.

### Vacuum Deposition Fundamentals

Optical coatings are applied by **[thermal evaporation](../glossary/thermal-evaporation.html)** in a vacuum chamber — the most accessible deposition technology at bootstrap stage.

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

### Multi-Layer Anti-Reflection Coatings

Single-layer MgF₂ reduces reflection to ~1.3% at one wavelength. Multi-layer coatings push this further by adding additional quarter-wave layers of alternating high and low refractive index materials.

**Two-layer (V-coat)**:
- Design: layer 1 is a quarter-wave of intermediate index (e.g., Al₂O₃, n ≈ 1.62), layer 2 is a quarter-wave of low index (MgF₂, n ≈ 1.38). Together they create a V-shaped reflection curve with a deep minimum at the design wavelength.
- Performance: <0.2% reflection at the design wavelength. But the bandwidth is narrow — reflection rises steeply on either side. Useful for monochromatic systems (laser optics, narrowband sensors) where performance at one wavelength is paramount.
- Deposition: two sequential evaporation steps without breaking vacuum. Deposit Al₂O₃ first (sublimes from tungsten boat at ~1800°C), then MgF₂. The quartz crystal monitor tracks each layer independently.

**Broadband multi-layer AR (2-4 layers)**:
- Design: stack of 2-4 quarter-wave layers with carefully chosen refractive indices. Common material pairs: TiO₂ (n ≈ 2.3, high) / SiO₂ (n ≈ 1.46, low), or Ta₂O₅ (n ≈ 2.1) / SiO₂. Each additional layer adds a degree of freedom for optimizing the reflection curve across a wider wavelength band.
- Performance: <0.5% average reflection across the full visible spectrum (400-700 nm). A 4-layer design can push this to <0.25% across visible and into the near-IR.
- Trade-off: more layers require tighter thickness control (±2 nm per layer) and longer deposition time. Each layer must be deposited without breaking vacuum to avoid interfacial contamination.

### High-Reflection Coatings

**Quarter-wave stack (dielectric mirror)**:
- Principle: alternate quarter-wave layers of high-index (H) and low-index (L) materials. At the design wavelength, reflections from each interface add constructively (in phase), building up total reflectivity. The more layer pairs, the higher the reflectivity.
- Typical stack: (HL)^N H, where N = number of pairs. Substrate | L | H | L | H | ... | H | air. Each layer is λ/4 optical thickness at the design wavelength.
- Materials: TiO₂/SiO₂ for visible, Si/SiO₂ for near-IR, ZnSe/ThF₄ for mid-IR. The index contrast between H and L materials determines how many pairs are needed: higher contrast means fewer pairs for the same reflectivity.
- Performance: 5-7 pairs achieve >99% reflectivity. 10-15 pairs reach >99.9%. The reflection band has a finite width centered on the design wavelength: Δλ/λ ≈ (4/π)·arcsin((nH - nL)/(nH + nL)). For TiO₂/SiO₂: bandwidth ~180 nm centered on 550 nm.

**Metal + dielectric enhancement**:
- An aluminum mirror overcoated with a quarter-wave stack (2-4 layers) boosts reflectivity from ~92% to >97% across the visible. The dielectric layers enhance reflection by constructive interference while the aluminum provides a broadband base.
- Advantage over bare dielectric mirror: broader bandwidth, fewer layers needed. The metal layer ensures reasonable reflectivity even at wavelengths outside the dielectric design band.

### Optical Filters

**Bandpass interference filters**:
- Design: two quarter-wave reflector stacks separated by a half-wave spacer layer (Fabry-Perot cavity). The cavity creates a narrow transmission peak between two reflection bands.
- Bandwidth (FWHM): 1-50 nm depending on spacer thickness and reflector stack design. Narrower bandwidth requires higher-reflectivity stacks (more layer pairs) and thicker spacers.
- Peak transmission: 50-90% depending on design. Narrower bandwidth sacrifices peak transmission.
- Applications: spectral analysis (selecting a single emission line), fluorescence microscopy (excitation/emission filters), laser line cleanup.
- Angular sensitivity: peak wavelength shifts blue at non-normal incidence (λ_shift = λ₀·√(1 - (sin θ / n_eff)²)). A filter designed for 550 nm at normal incidence shifts to ~540 nm at 20° incidence. Limits the useful cone angle.

**Long-pass and short-pass filters (edge filters)**:
- Design: a gradual transition from blocking to transmission at a specified edge wavelength. Constructed from many thin layers (20-50) with computer-optimized thicknesses (not simple quarter-wave stacks).
- Long-pass: transmits wavelengths above the edge, blocks below. Used to block UV while passing visible, or block visible while passing IR.
- Short-pass: the reverse. Transmits below the edge, blocks above.
- Blocking: optical density (OD) >4 (transmission <0.01%) in the blocked region. Edge steepness: transition from OD 4 to 50% transmission within 10-30 nm.

**Neutral density (ND) filters**:
- Purpose: attenuate light uniformly across a wavelength range without altering the spectral distribution. Used for controlling exposure in imaging, preventing detector saturation, and reducing laser power for alignment.
- Metallic ND filters: thin Inconel (Ni-Cr-Fe alloy) or carbon film deposited on glass. Optical density proportional to film thickness. OD 0.1 (79% transmission) to OD 4.0 (0.01% transmission). Spectrally flat from 400-2000 nm. Absorbing: incident power converts to heat, which limits maximum power handling.
- Reflective ND filters: partially transparent metallic film that reflects rather than absorbs. Lower thermal load. Used for high-power laser applications.

### Sputter Deposition

Thermal evaporation produces porous, columnar films that absorb moisture over time, shifting their optical properties. Sputtering produces denser, more durable coatings.

**DC magnetron sputtering**:
- Process: Argon gas at 1-10 mTorr is ionized by a DC plasma (~500 V, 1-10 kW). A magnetic field behind the target traps electrons near the target surface, increasing ionization efficiency. Ar⁺ ions bombard the target, ejecting atoms that deposit on the substrate. Deposition rate: 0.1-5 nm/s depending on material and power.
- Advantages over thermal evaporation: denser films (bulk-like density), better adhesion (arriving atoms have higher kinetic energy), more uniform composition for alloys (thermal evaporation fractionates by vapor pressure). The dense film structure resists moisture absorption, so the optical properties remain stable over time.
- Disadvantages: higher equipment complexity (magnetron, RF power supply for insulating targets), higher argon consumption, slower deposition rate for some materials compared to thermal evaporation.

**RF sputtering for insulators**:
- DC sputtering only works with conductive targets (charge buildup on insulating targets stops the process). RF sputtering at 13.56 MHz alternates the polarity, preventing charge accumulation. Works for SiO₂, TiO₂, Al₂O₃, and other dielectric coating materials. Requires an impedance-matching network between the RF generator and the sputtering chamber.

### Durable Coatings for Demanding Applications

**Hard carbon coatings for IR optics**:
- Germanium and zinc selenide IR optics (thermal imaging, 8-14 μm band) require anti-reflection coatings that survive harsh environments. Diamond-like carbon (DLC) coatings provide both AR function (n ≈ 1.8-2.2, intermediate between air and Ge at n ≈ 4.0) and extreme mechanical durability (hardness ~20-40 GPa). DLC is deposited by plasma-enhanced chemical vapor deposition (PECVD) from hydrocarbon gas (CH₄ or C₂H₂). Thickness: 1-3 μm. Survives rain erosion at high velocity, sand impact, and salt spray.

**High-power laser mirrors**:
- Dielectric quarter-wave stacks for laser mirrors must withstand high energy densities without damage. Laser damage threshold (LDT) is the maximum fluence (J/cm²) a coating can tolerate without irreversible change.
- Damage mechanisms: thermal absorption at defects (dust, nodules, contamination), multiphoton ionization in the film, and electric field enhancement at layer interfaces. Clean deposition (Class 100 cleanroom loading, pre-cleaned substrates) is more important than material choice for achieving high LDT.
- Typical performance: electron-beam deposited SiO₂/Ta₂O₅ stacks achieve >1 J/cm² LDT at 1064 nm, 10 ns pulse. Ion-assisted deposition (IAD, where an ion beam bombards the growing film) produces denser films with LDT >5 J/cm².
- Thermal management: high-power CW laser mirrors (kW-class) absorb 0.1-1% of incident power as heat. Substrate must be thermally conductive (copper, aluminum, or silicon) and may require active water cooling. Coating thermal expansion mismatch causes stress that can crack the film if temperature excursions exceed ~50°C.

### Coating Design and Simulation

Designing multi-layer coatings requires calculating reflection and transmission for arbitrary stacks of thin films. The transfer matrix method solves this: each layer is represented by a 2×2 matrix relating electric field amplitudes at its boundaries. The total stack response is the matrix product of all individual layer matrices.

For bootstrap design work, a simple spreadsheet can compute reflectivity of a 1-4 layer stack at normal incidence. The inputs are layer thicknesses, refractive indices, and the wavelength range. Iterate layer parameters to minimize reflection (AR) or maximize reflection (mirror) at the target wavelength. Free software tools (OpenFilters, Essential Macleod) automate this optimization for complex designs.

### Coating Durability Testing

Applied coatings must survive handling, cleaning, and environmental exposure. Standard tests qualify coating durability:

- **Adhesion test (tape test)**: Press adhesive tape (3M 610 or equivalent) firmly onto the coated surface. Pull off rapidly at 180° angle. No coating should transfer to the tape. Perform after a 24-hour post-deposition aging period (some coatings, particularly MgF₂, continue to stress-relieve over hours).
- **Abrasion test (eraser rub)**: Rub the coated surface with a standard eraser (Mil-E-12397) under a 1 lb (450 g) load for 20-50 strokes. The coating must not scratch, haze, or delaminate. This test simulates routine cleaning. MgF₂ single-layer coatings on soft glass sometimes fail this test; SiO₂ overcoated surfaces pass easily.
- **Humidity test**: Expose coated optics to 95% relative humidity at 50°C for 24 hours. Inspect for haze, spotting, or adhesion failure. Porous thermal-evaporated films are more susceptible than dense sputtered films. Humidity causes refractive index shifts in porous films as water fills voids, permanently altering the optical performance.
- **Salt spray (for external optics)**: Expose to 5% NaCl fog at 35°C for 24-48 hours per ASTM B117. Simulates marine and coastal environments. Tests both coating and substrate corrosion resistance. Protected aluminum mirrors (SiO₂ overcoat) survive; bare aluminum develops pinhole corrosion.

### Half-Wave Absentee Layers and Matching

A half-wave optical thickness layer (λ/2n physical thickness) acts as an absentee layer at the design wavelength. It has no effect on the reflectance or phase of the stack at that wavelength, because the round-trip optical path through the layer is exactly one wavelength, returning the reflected and transmitted beams to their original phase relationship.

This property is useful as a spacer and matching tool. In a quarter-wave stack mirror, inserting a half-wave layer between the stack and the substrate (or between the stack and air) does not alter the mirror's reflectivity at the design wavelength. But it does change the electric field distribution inside the coating, which affects laser damage threshold. A half-wave silica overcoat on a high-reflector stack moves the peak electric field away from the outer surface, reducing the risk of damage from surface contamination.

Half-wave layers also serve as non-interfering "buffer" layers during deposition. If a particular material combination has poor adhesion or high stress, a thin half-wave layer of a compatible intermediate material (often Al₂O₃, n ≈ 1.62) can be inserted without affecting optical performance, improving mechanical durability.

### Admittance Diagrams for Multi-Layer Optimization

The optical admittance of a coating stack at each interface determines the overall reflectance. Admittance Y is defined as the ratio of the magnetic to electric field amplitudes at a given plane in the coating. Starting from the substrate (admittance Y_sub = n_sub), each layer transforms the admittance according to its thickness and refractive index. Plotting the admittance trajectory in the complex plane (real vs. imaginary parts) as you move through the layer stack reveals the coating behavior at a glance.

An admittance circle traces a semicircle in the complex plane for each quarter-wave layer. A low-index layer (MgF₂, n = 1.38) pulls the admittance toward 1.0 (air), reducing reflection. A high-index layer (TiO₂, n = 2.3) pushes the admittance away from 1.0, increasing reflection. For a broadband AR coating, the admittance trajectory spirals inward toward Y = 1.0 (perfect match to air) across a range of wavelengths.

This graphical approach helps designers understand why certain layer sequences work, diagnose problems in existing designs (a loop in the admittance plot indicates an impedance mismatch at that wavelength), and identify where additional layers would help. It is especially valuable for non-quarter-wave designs, where layer thicknesses deviate from the λ/4 rule and the admittance trajectory is not a simple semicircle.

### Thermal Evaporation Process Parameters

**Resistive evaporation**: A tungsten or molybdenum boat (0.1-0.5 mm thick sheet, folded into a "V" or dimpled shape) carries the source material. Current of 10-50 A at 3-10 V heats the boat by Joule heating. Temperature control is by variac or SCR power supply. Deposition rate depends on source temperature and source-to-substrate distance: typical rates 0.1-5 nm/s for common coating materials. The quartz crystal monitor reads thickness in real time with ±1 nm accuracy, and the operator manually adjusts power to maintain a constant rate.

**Electron-beam evaporation**: For refractory materials (TiO₂, Ta₂O₅, SiO₂) that require temperatures above 2000°C, an electron beam (5-10 kV, 0.1-1 A) is magnetically deflected into a water-cooled copper crucible containing the source material. The beam heats only a small spot, creating a localized melt pool while the surrounding material acts as its own crucible liner. This avoids contamination from boat material. Deposition rates 0.5-10 nm/s. The beam can be rastered across the source surface for uniform consumption. More complex than resistive evaporation (requires high-voltage power supply, magnetic deflection, water cooling), but essential for high-index oxides.

**Process pressure and film quality**: At base pressures of 10⁻⁴ to 10⁻⁵ Torr, the mean free path of evaporated atoms exceeds the source-to-substrate distance (typically 25-40 cm), so atoms travel in straight lines without gas-phase collisions. If pressure is too high (10⁻³ Torr or worse), evaporated atoms scatter off residual gas molecules, producing a frosty, porous film with columnar microstructure. These columnar films absorb moisture from the air after removal from vacuum, causing the refractive index to shift upward and the spectral performance to drift ("moisture shift"). Ion-assisted deposition (IAD), where a broad-beam ion source bombards the growing film with 50-500 eV Ar⁺ or O₂⁺ ions during deposition, compacts the film and eliminates moisture shift entirely.

**Substrate heating during deposition**: Many coating materials require elevated substrate temperature for proper film density and adhesion. MgF₂ deposits optimally at substrate temperatures of 250-300°C, which drives off adsorbed water from the glass surface and promotes dense film growth. Substrate heating is achieved by radiant heaters (quartz lamps or resistance heaters) behind the substrate holder. The trade-off: higher substrate temperature improves film density but increases thermal stress during cool-down, especially for thick coatings or coatings on substrates with different thermal expansion coefficients. Thermal stress can cause cracking in thick MgF₂ films (>2 μm) deposited on borosilicate glass.

**Multi-source deposition**: For coatings requiring more than one material (all multi-layer designs), the vacuum chamber contains two or more evaporation sources, each in a separate crucible with its own shutter. The operator (or automated controller) opens one shutter, deposits the first layer to target thickness, closes that shutter, then opens the next source's shutter for the second layer. The entire multi-layer stack is deposited in a single pump-down cycle without breaking vacuum between layers. Breaking vacuum between layers introduces a contaminant interface (adsorbed water and atmospheric gases) that degrades optical performance and adhesion at that boundary.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Optics](./index.md) • [All Domains](../index.md)*
