# Photomask Glass Substrates & ULE Glass

> **Node ID**: glass.photomask-substrates
> **Domain**: [Glass](./index.md)
> **Dependencies**: [`glass.advanced`](advanced.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md)
> **Enables**: [`photolithography`](../photolithography/index.md), [`semiconductors`](../electronics/index.md)
> **Timeline**: Years 40-70
> **Outputs**: photomask_blanks, ule_glass, precision_optical_substrates
> **Critical**: Yes — photomask substrates directly determine minimum feature size and yield in IC fabrication; no photolithography without them

## Problem

Photomask substrates are the flat glass plates that carry the circuit pattern image projected onto silicon wafers during photolithography. A photomask blank consists of an ultra-flat glass substrate, a thin opaque film (typically chromium, 60-100 nm), and optionally an anti-reflective coating. The glass substrate must be dimensionally stable, optically transparent at exposure wavelengths, and free of defects that would print onto the wafer. Photomask quality directly determines the yield and minimum feature size achievable in IC fabrication — a single substrate defect can render an entire wafer useless.

Photomask substrates demand glass tolerances 10-100× tighter than standard optical glass. Where a telescope mirror might accept λ/4 (158 nm at 633 nm) surface error over its aperture, a photomask substrate must achieve flatness better than 250 nm over the entire 152 mm × 152 mm (6-inch) active area, with near-zero thermal expansion to prevent pattern distortion during exposure.

## Prerequisites

- [Advanced glass](advanced.md) — fused silica production, precision melting and forming
- [Photolithography fab processes](../photolithography/fab-processes.md) — mask use in semiconductor fabrication
- [Precision instruments](../optics/precision-instruments.md) — interferometric flatness measurement
- [Machine tools](../machine-tools/index.md) — precision grinding and polishing equipment
- [Refractories](../chemistry/refractories.md) — high-temperature furnace linings for glass melting

## Substrate Materials

**Fused silica (amorphous SiO₂)** — the dominant photomask substrate material:
- **Composition**: 100% SiO₂, amorphous (non-crystalline). Produced by flame hydrolysis of SiCl₄ or by melting natural quartz crystal.
- **Coefficient of thermal expansion (CTE)**: 0.52 × 10⁻⁶/°C (0.52 ppm/°C) at 0-200°C. Exceptionally low — the material barely changes size with temperature changes during mask handling and exposure.
- **Transmission**: >90% from 200 nm (deep UV) through visible to 2.5 μm (IR). Transparent at i-line (365 nm), g-line (436 nm), and h-line (405 nm) mercury lamp wavelengths used in photolithography exposure tools.
- **Refractive index**: 1.458 at 633 nm, 1.511 at 193 nm (ArF DUV). Homogeneity: ±1 × 10⁻⁶ across the substrate (striae-free).
- **Softening point**: ~1600°C. No practical deformation risk at semiconductor processing temperatures.
- **Density**: 2.20 g/cm³. A 152 mm × 152 mm × 6.35 mm blank weighs approximately 320 g.
- **Knoop hardness**: 500 kg/mm² — hard enough to resist scratches during handling but polishable to optical finish.

**Borosilicate glass (Schott Borofloat 33 type)** — used for lower-resolution masks (features >5 μm):
- **Composition**: ~80% SiO₂, ~13% B₂O₃, ~4% Na₂O, ~2% Al₂O₃.
- **CTE**: 3.3 × 10⁻⁶/°C — six times higher than fused silica. Acceptable for contact/proximity printing where thermal expansion during exposure does not critically affect alignment.
- **Advantage**: Significantly cheaper than fused silica (~1/5 the cost). Available in large sheets from float glass process.
- **Limitation**: Higher CTE limits use to coarse-feature lithography. UV transmission degrades below 300 nm (boron absorption edge), unsuitable for deep UV lithography.
- **Use case**: Prototyping, low-volume mask production for features ≥5 μm, alignment masks, and test structures.

## ULE Glass (Ultra-Low Expansion)

ULE glass (Corning Code 7972) is a titanium silicate glass with a coefficient of thermal expansion approaching zero — the most thermally stable glass available for photomask and precision optical applications:

- **Composition**: ~92.5% SiO₂ (silica), ~7.5% TiO₂ (titanium dioxide). The titanium dioxide is dissolved in the silica glass network, not a separate crystalline phase.
- **CTE**: 0 ± 30 × 10⁻⁹/°C (0 ± 30 ppb/°C) over the range 5-35°C. The near-zero expansion results from a compensating mechanism: the silica network expands with temperature while the TiO₂ component contracts, producing a net CTE that crosses zero near room temperature. This is 100× more stable than fused silica and 300× more stable than borosilicate glass.
- **Zero-crossing temperature**: The CTE passes through zero at approximately 20-25°C, which can be adjusted during manufacturing by controlling the TiO₂ concentration. Each batch is measured and the zero-crossing temperature certified.
- **Density**: 2.21 g/cm³ (marginally denser than fused silica due to TiO₂).
- **Refractive index**: 1.484 at 633 nm (slightly higher than fused silica due to TiO₂ contribution).
- **Transmission**: Similar to fused silica in the visible and near-UV, but absorption increases below 260 nm due to TiO₂ charge transfer bands. Acceptable for i-line (365 nm) and longer wavelengths. Not suitable for 193 nm (ArF) or 248 nm (KrF) DUV exposure.
- **Knoop hardness**: 480 kg/mm². Slightly softer than fused silica — requires gentler polishing to avoid subsurface damage.
- **Applications in EUV lithography**: ULE glass is the substrate material for EUV photomask blanks (reflective masks, not transmissive). EUV masks use a multilayer Mo/Si Bragg reflector stack on a ULE substrate. The near-zero CTE prevents dimensional drift of the absorber pattern relative to the multilayer reflector during exposure. EUV mask blanks require flatness <50 nm p-v over 100 mm × 130 mm active area — feasible only with ULE's dimensional stability.

## Photomask Substrate Manufacturing

**Fused silica blank production (flame hydrolysis / soot process)**:
1. **Feedstock**: Silicon tetrachloride (SiCl₄) vapor carried in oxygen gas. SiCl₄ produced from metallurgical-grade silicon + chlorine, or from high-purity quartz + chlorine at 600-800°C.
2. **Deposition**: SiCl₄ + 2H₂O → SiO₂ + 4HCl. Burn SiCl₄ in hydrogen-oxygen flame. Silica particles (soot) deposit on a rotating target mandrel, building up a cylindrical boule (ingot) over 24-72 hours. Boule diameter: 200-300 mm.
3. **Consolidation**: Heat the porous soot boule to 1500-1600°C in a furnace under helium atmosphere. The soot sinters into a fully dense, transparent fused silica glass. Helium permeates the porous structure to prevent trapping gas bubbles. Consolidation shrinkage: ~15-20% linear.
4. **Annealing**: Slow cool through the strain point at 0.1-1°C/hour to reduce residual stress below 2 nm/cm birefringence. Annealing cycle: 2-4 weeks for large boules.

**ULE glass production**:
1. **Feedstock**: Silicon tetrachloride (SiCl₄) and titanium tetrachloride (TiCl₄) vapors, separately metered and mixed in controlled ratio. The TiCl₄/SiCl₄ ratio determines the final TiO₂ concentration and hence the CTE zero-crossing temperature.
2. **Flame hydrolysis**: Burn the mixed chlorides in an oxy-hydrogen flame. Both SiO₂ and TiO₂ deposit simultaneously as a mixed soot on the rotating mandrel. TiO₂ incorporates into the amorphous silica network — not as crystalline rutile but as dissolved Ti⁴⁺ ions in tetrahedral coordination.
3. **Consolidation**: Same process as fused silica — heat to 1500-1600°C in helium. The consolidated glass is a homogeneous amorphous titanium silicate.
4. **CTE certification**: Each boule is sampled at multiple positions. CTE measured by interferometric dilatometry with precision ±5 ppb/°C. Only boules meeting 0 ± 30 ppb/°C specification are accepted for photomask blank production.

**Precision blank fabrication**:
1. **Sawing**: Cut boule into rectangular slabs using diamond-blade saws. Slab dimensions for 6-inch mask: 152.4 mm × 152.4 mm × 6.35 mm (6" × 6" × ¼"). Saw kerf: 0.3-0.5 mm. Surface damage layer from sawing: 20-50 μm deep.
2. **Grinding**: Remove saw damage with coarse abrasive (SiC 220 grit), then progressively finer grinding (SiC 400 → 600 → 1200). Each stage removes the damage layer from the previous stage. Final grind leaves 3-5 μm surface roughness.
3. **Lapping**: Lap both faces on cast iron lapping plates with aluminum oxide slurry (9 μm → 3 μm → 1 μm). Produces flat surfaces with <1 μm roughness. Flatness at this stage: ~1-2 μm over 150 mm.
4. **Precision polishing**: Polish on polyurethane polishing pads with colloidal silica slurry (30-80 nm particle size, pH 10-11). Chemical-mechanical polishing (CMP) mechanism: the alkaline slurry slightly dissolves the silica surface while the abrasive particles mechanically remove the softened layer. Material removal rate: 0.1-0.5 μm/hour. Target surface roughness: <0.5 nm RMS (measured by atomic force microscope over 1 μm × 1 μm area).
5. **Flatness correction**: Local polishing with small-diameter tools (20-40 mm) to correct residual flatness errors. Guided by interferometric flatness map. Iterative process — measure, polish, re-measure — achieving final flatness <250 nm peak-to-valley over 152 mm × 152 mm.

## Specifications

**Standard 6-inch (152 mm) photomask blank specifications**:

| Parameter | Specification | Measurement Method |
|-----------|--------------|-------------------|
| Dimensions | 152.4 ± 0.1 mm × 152.4 ± 0.1 mm × 6.35 ± 0.05 mm | Calipers, micrometer |
| Surface flatness (front) | <250 nm p-v over 142 mm × 142 mm clear aperture | Fizeau interferometer, λ = 633 nm |
| Surface flatness (back) | <500 nm p-v | Fizeau interferometer |
| Surface roughness (front) | <0.5 nm RMS over 1 μm × 1 μm | AFM |
| Parallelism (wedge) | <10 arc-seconds (≈3 μm over 152 mm) | Autocollimator |
| Thickness uniformity | ±25 μm across substrate | Contact profilometer |
| Bubble/inclusion defects | 0 defects >10 μm in clear aperture | Dark-field illumination, 50× |
| Scratch/dig | 10/5 per MIL-PRF-13830B | Visual inspection, 100 W lamp |
| Striae (refractive index variation) | <1 × 10⁻⁶ | Shadowgraph or interferometry |
| Residual birefringence | <2 nm/cm | Polarimeter |
| CTE (fused silica) | 0.52 ± 0.02 × 10⁻⁶/°C | Dilatometer |
| CTE (ULE) | 0 ± 30 × 10⁻⁹/°C (5-35°C) | Interferometric dilatometer |

**Defect classification**:
- **Critical**: Any defect >0.5 μm in the active area (clear or opaque spot) is a mask-killing defect. At 4× reduction lithography, a 0.5 μm mask defect prints as a 125 nm defect on the wafer.
- **Major**: Scratches >5 μm wide, chips >50 μm from edge, bubbles >20 μm.
- **Minor**: Surface blemishes <5 μm, handling marks outside active area.

**Photomask blank cost structure** (indicative):
- Fused silica 6" blank (uncoated): $200-400
- Fused silica 6" blank (Cr coated + AR): $500-1000
- ULE 6" blank (uncoated): $2000-5000
- EUV ULE blank (with Mo/Si multilayer): $50,000-100,000+

## Chromium Film Deposition

Photomask blanks are coated with an opaque film that is patterned to create the mask image:

**Chromium (Cr) film** — the standard opaque layer:
- **Thickness**: 60-100 nm (typically 70-80 nm for i-line masks). Optical density >3.0 at 365 nm (i-line), meaning <0.1% transmission.
- **Deposition**: DC magnetron sputtering from a 99.95% pure chromium target. Argon sputter gas at 2-5 mTorr, power density 5-15 W/cm². Deposition rate: 2-5 nm/s. Substrate rotation ensures thickness uniformity ±2% across 152 mm.
- **Sputtering system requirements**: Vacuum chamber evacuated to <5 × 10⁻⁷ Torr before backfilling with argon. The system must achieve base vacuum without oil contamination — use turbomolecular or cryogenic pumps (not diffusion pumps which backstream oil). Film stress must be controlled (compressive stress <200 MPa) to prevent substrate bending.
- **Anti-reflective coating**: A second layer of Cr₂O₃ (chromium oxide, 20-30 nm) may be deposited on top of the chromium to reduce reflections from the chromium surface during exposure. Reflectivity reduced from ~60% to <5% at exposure wavelength.

**Alternative opaque films**:
- **MoSi (molybdenum silicide)**: Used for phase-shift masks (attenuated PSM). Thickness 60-80 nm. Transmits 4-8% at exposure wavelength with 180° phase shift relative to clear areas. Requires reactive sputtering in Ar/O₂ mixture.
- **TaBN (tantalum boron nitride)**: Used for EUV absorber layers. Higher etch selectivity than Cr for fine-feature patterning.

## Substrate Quality Control

**Flatness measurement**:
- **Fizeau interferometer**: The definitive flatness measurement. A reference optical flat (λ/20 flatness, certified) is placed above the substrate with a small air wedge. Laser illumination (He-Ne, 633 nm) creates interference fringes (Fizeau fringes). Each fringe corresponds to λ/2 = 316 nm height difference. Flatness is reported as peak-to-valley (p-v) deviation across the clear aperture. Automated fringe analysis (phase-shifting interferometry) achieves λ/100 (6 nm) resolution.
- **Acceptance**: <250 nm p-v for production photomask blanks. <100 nm p-v for high-end blanks used at ≤0.25 μm features.

**Defect inspection**:
- **Dark-field illumination**: Illuminate the blank surface at a low angle with intense white light. Scratches, pits, and particles scatter light into the viewing optics while the pristine surface remains dark. Sensitivity: detects defects down to 0.3 μm at 100× magnification.
- **Laser scanning**: A focused laser beam (488 nm or 532 nm) scans the surface in a raster pattern. Scattered light is collected by photomultiplier tubes. Defects are detected as intensity spikes above the background scatter level. Sensitivity: 50-80 nm particle detection. Throughput: 5-10 minutes per 6-inch blank.
- **Classification**: Automated defect review at 1000× magnification (bright-field microscope) classifies each defect as particle (removable by cleaning), scratch (permanent), pit (permanent), or bubble (permanent in bulk). Only blanks with zero permanent defects in the active area are shipped.

**Birefringence measurement**:
- A polarized laser beam passes through the substrate. Stress birefringence rotates the polarization plane proportionally to the internal stress. A rotating analyzer measures the rotation angle. Residual stress must be <2 nm/cm (retardation) to prevent polarization-dependent effects during exposure.

## Thermal Management During Exposure

During lithographic exposure, the photomask absorbs a fraction of the exposure energy, causing local heating:

**Fused silica thermal behavior during exposure**:
- Absorption at 365 nm (i-line): ~1-2% for uncoated fused silica, 60%+ for chromium areas.
- Temperature rise in Cr-coated areas during a single exposure flash: ~0.01-0.1°C (depending on exposure dose and pulse duration).
- Thermal expansion per °C for 152 mm substrate: 152 mm × 0.52 × 10⁻⁶/°C = 79 nm/°C. A 0.1°C temperature rise causes 7.9 nm expansion — significant for sub-250 nm features.
- Steady-state temperature rise during continuous scanning: 0.5-2°C above ambient, requiring active substrate cooling in exposure tools.

**ULE glass advantage for DUV/EUV**:
- Thermal expansion per °C for 152 mm ULE substrate: 152 mm × 30 × 10⁻⁹/°C = 4.6 nm/°C (maximum, using the ±30 ppb spec). This is 17× less than fused silica.
- For EUV masks, the thermal stability of ULE is essential: EUV absorber patterns at 13.5 nm wavelength require placement accuracy of <1 nm, and even micro-degree temperature fluctuations would cause unacceptable pattern drift on fused silica.

## Substrate Handling and Storage

**Cleaning**:
- **Spin-rinse-dry (SRD)**: Rinse substrate with ultra-pure water (18.2 MΩ·cm) while spinning at 2000-4000 RPM. Centrifugal force removes particles. Final rinse with isopropyl alcohol for spot-free drying. Particle removal efficiency: >95% for particles >0.5 μm.
- **Megasonic cleaning**: 1 MHz acoustic waves in ultra-pure water cavitate near the substrate surface, dislodging sub-micron particles without contact. Particle removal: >90% for 0.1-0.5 μm particles. No mechanical contact — zero scratch risk.
- **Piranha clean**: H₂SO₄:H₂O₂ (3:1) at 120°C removes organic contamination. 10-15 minute immersion. Must be followed by ultra-pure water rinse. Extremely hazardous — hot concentrated acid with active oxygen.

**Storage**:
- Store in individual nitrogen-purged containers with the polished surface facing a soft contact pad (non-woven polyester).
- Class 100 (ISO 5) or better cleanroom storage environment. A single 1 μm particle deposited on the substrate surface after cleaning becomes a mask defect.
- Shelf life: Indefinite for fused silica and ULE if kept clean. Chromium film may oxidize over years in humid air — store at <40% relative humidity.
- Handle only with vacuum wands (never manual) after final cleaning. Finger oils create permanent stains on the chromium surface.

## Substrate Sizing for Different Lithography Generations

| Mask Format | Substrate Size | Thickness | Typical Use |
|-------------|---------------|-----------|-------------|
| 3-inch | 76.2 × 76.2 mm | 3.18 mm | Legacy, research |
| 4-inch | 101.6 × 101.6 mm | 6.35 mm | Contact/proximity printing |
| 5-inch | 127.0 × 127.0 mm | 6.35 mm | Early projection printing |
| 6-inch | 152.4 × 152.4 mm | 6.35 mm | Standard i-line, DUV |
| 6-inch (EUV) | 152.4 × 152.4 mm | 6.35 mm | EUV lithography (ULE) |

The 6-inch format is standard since the 1990s. The 0.25× reticle field on a 6-inch mask (maximum ~104 mm × 132 mm patterned area at 4× reduction) provides a 26 mm × 33 mm exposure field on the wafer, sufficient for most die sizes.

## Bootstrap Sequencing

Producing photomask substrates from scratch requires the full glass production chain plus semiconductor-grade cleanliness:

1. **Glass production**: Fused silica boule from SiCl₄ flame hydrolysis (requires [`glass.advanced`](advanced.md) fused silica capability + chlorine chemistry from [`chemistry.acids`](../chemistry/acids.md)).
2. **Silicon tetrachloride source**: SiCl₄ from MG-silicon + Cl₂ at 300-500°C. Requires metallurgical-grade silicon production + chlorine electrolysis. Alternatively, high-purity quartz + chlorine at 600-800°C.
3. **Precision machining**: Diamond sawing, grinding, lapping. Requires machine tools capable of ±5 μm tolerance and abrasives (SiC, Al₂O₃, colloidal silica) from [`machine-tools.bearings-abrasives`](../machine-tools/bearings-abrasives.md).
4. **Precision polishing**: CMP with colloidal silica. Requires sub-100 nm colloidal particles and polyurethane polishing pads. Surface measurement via Fizeau interferometry requires [`optics.inspection`](../optics/inspection.md) and [`measurement.precision-metrology`](../measurement/precision-metrology.md).
5. **Chromium sputtering**: Requires DC magnetron sputtering system (vacuum <5 × 10⁻⁷ Torr, turbomolecular pump), chromium target (99.95% pure), argon gas. Vacuum capability from [`gas-handling.vacuum`](../gas-handling/vacuum.md).
6. **Cleanroom handling**: Substrate cleaning and inspection in Class 100 (ISO 5) or better environment. Requires [`photolithography.cleanrooms`](../photolithography/cleanrooms.md).
7. **Metrology**: Fizeau interferometer for flatness, AFM for roughness, laser scattering for defects, polarimeter for birefringence. Total metrology investment significant but achievable with optical domain capability.

## Safety & Hazards

- **Silicon tetrachloride handling**: SiCl₄ is corrosive, reacts violently with water/moisture producing HCl gas and silica particulate. Causes severe respiratory damage. Handle in closed, dry systems with acid-resistant seals. Emergency: flood with water — SiCl₄ hydrolysis generates heat and HCl but dilution is the only practical response. Use full-face respirator with acid gas cartridges for spill response.
- **Titanium tetrachloride handling**: TiCl₄ is even more reactive with water than SiCl₄, producing dense white TiO₂/HCl fume clouds. Extremely hazardous — both corrosive and obscuring vision. Double-contained piping mandatory. Store under inert atmosphere.
- **HF in cleaning**: Piranha and other cleaning solutions may contain hydrofluoric acid for surface treatment. HF causes severe chemical burns with delayed symptoms and systemic fluoride poisoning. Calcium gluconate gel must be immediately available.
- **Precision glass handling**: Photomask blanks have optically polished surfaces with roughness <0.5 nm. ANY contact with the polished surface (even clean gloves) will scratch it. Handle only by edges, use vacuum wands for polished face contact.
- **Vacuum system hazards**: Sputtering systems operate at high vacuum with large glass viewports. Implosion risk — all vacuum chamber viewports must be safety-shielded. High voltage (500-1000 V DC) for sputtering plasma — lockout/tagout mandatory during maintenance.
- **Chromium toxicity**: Chromium metal is less toxic than hexavalent chromium (Cr VI), but sputtering targets and deposited films generate fine particles during handling and cleaning. Inhalation of Cr particles causes respiratory sensitization. Use HEPA-filtered local exhaust ventilation when handling Cr targets or cleaning sputtering chambers.

## Phase-Shift Mask Substrate Considerations

Phase-shift masks (PSM) require additional optical specifications beyond standard binary masks:

**Attenuated PSM (half-tone)**:
- The substrate must support MoSi absorber films with precise optical constants. MoSi transmits 4-8% of exposure wavelength with a 180° phase shift relative to clear areas.
- Substrate homogeneity becomes critical: refractive index variation must be <0.5 × 10⁻⁶ across the active area (half the standard tolerance) because phase-shift errors directly translate to linewidth variation on the wafer.
- Thickness tolerance tightens to ±10 μm (vs. ±25 μm for binary masks) because optical path length through the substrate affects phase calculation.

**Alternating PSM (Levenson-type)**:
- Requires substrate regions that are either etched to a precise depth (λ/2n depth where n is the refractive index of the substrate at the exposure wavelength) or left unetched. For fused silica at 365 nm: etch depth = 365 / (2 × 1.511) = 120.8 nm. Etch depth tolerance: ±3 nm.
- The substrate must withstand reactive ion etching (RIE) with CHF₃/CF₄ chemistry to create the phase trenches without inducing micro-cracking or sub-surface damage. Fused silica etch rate in CHF₃: ~30 nm/minute.

## Substrate Reclamation

Damaged or obsolete photomask blanks can be reclaimed, reducing the cost of substrate production:

- **Process**: Strip the chromium film in ceric ammonium nitrate solution (Ce(NH₄)₂(NO₃)₆, 10% in HNO₃) at 50-60°C. Chromium dissolves in 5-15 minutes, leaving a clean fused silica surface.
- **Re-polish**: After stripping, the substrate may require re-polishing to remove any surface damage from the previous patterning cycle. A light polish (0.1-0.5 μm removal) with colloidal silica restores the surface to specification.
- **Yield**: Approximately 80-90% of blanks can be reclaimed after one use. After 2-3 reclamation cycles, accumulated surface damage and edge chips reduce yield to <50%. ULE blanks are typically not reclaimed due to their higher value and tighter specifications.
- **Economics**: Reclamation costs ~20-30% of new blank cost, making it economically attractive for prototyping and development masks.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Flatness not meeting spec after polish | Uneven lap pressure or pitch not conforming | Re-press pitch lap; vary stroke pattern; measure frequently with interferometer |
| Subsurface damage visible after etching | Fine grinding stage insufficient or grit contamination | Return to finer grit (sequence 9 μm → 3 μm → 1 μm); clean between stages |
| Chromium adhesion failure | Surface contamination before deposition | Plasma clean substrate immediately before sputtering; verify no organic residue |
| Inclusion defect in fused silica | Raw material impurity (Al, Fe, Na) or furnace contamination | Source higher-purity SiCl₄ precursor; use fused silica furnace linings; inspect blanks with dark-field illumination |
| Thermal expansion too high for mask use | Wrong glass type (borosilicate instead of fused silica) | Verify material identity via refractive index measurement (fused silica n=1.511 at 365 nm) |
| Phase-shift etch depth out of tolerance | RIE rate drift or endpoint detection error | Calibrate etch rate before each run; use interferometric endpoint detection; measure depth with profilometer |

## See Also

- [Advanced glass](advanced.md) — fused silica and borosilicate production
- [Optical coatings](../optics/optical-coatings.md) — chromium and anti-reflective coating application
- [Precision instruments](../optics/precision-instruments.md) — interferometric flatness measurement
- [Photolithography](../photolithography/index.md) — mask use in semiconductor fabrication
- [Semiconductors](../electronics/index.md) — IC manufacturing overview
- [Inspection](../optics/inspection.md) — defect detection and surface quality standards

[← Back to Glass](index.md)
