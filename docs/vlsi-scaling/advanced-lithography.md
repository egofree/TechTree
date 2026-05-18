# Advanced Lithography

> **Node ID**: vlsi-scaling.advanced-lithography
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./)
> **Dependencies**: `photolithography.resists-masks`, `optics.inspection`
> **Timeline**: Years 70-200+
> **Outputs**: advanced_lithography, euv_capability, duv_capability

### Advanced Lithography Scaling

**Contact/proximity printing** (Photolithography baseline — features down to ~2-5 μm):
- Mask contacts or nearly contacts wafer. Simple, but mask damage from contact limits yield. Good enough for early production.

**Projection steppers/scanners** (features down to ~0.5 μm):
- **Step-and-repeat**: Lens projects reduced mask image (typically 5:1 or 10:1 reduction) onto one exposure field (~20×20 mm). Stage steps to next field. Each wafer requires 50-200+ exposures.
- **Alignment**: Automatic alignment using microscope + pattern recognition. Overlay accuracy: ±0.1-0.5 μm.
- **I-line (365 nm)**: Mercury lamp + narrowband filter. Features down to ~0.35 μm with resolution enhancement techniques (RET): phase-shift masks, off-axis illumination, optical proximity correction (OPC).

**DUV lithography** (features down to ~0.07 μm with immersion):
- **KrF excimer laser** (248 nm): Features down to ~0.25 μm. Laser gas: Kr + F₂ mixture, electrically pumped. 1000 Hz pulse rate, ~10 W output.
- **ArF excimer laser** (193 nm): Features down to ~0.13 μm (dry), ~0.07 μm (immersion). Immersion: water layer between lens and wafer increases numerical aperture (NA >1.0).
- **Resist chemistry**: Chemically amplified resists (CAR) — photoacid generator (PAG) produces acid on exposure, acid catalytically cleaves protecting groups during PEB, amplifying sensitivity 10-100x. Required for low DUV exposure doses. Environmental stability challenging (airborne base contaminants neutralize acid).

**EUV lithography** (features below 7 nm — extremely long-term):
- **Source**: 13.5 nm wavelength from tin (Sn) plasma. High-power CO₂ laser hits Sn droplets at 50 kHz → plasma emits EUV. Power: 200-500 W at intermediate focus. Everything absorbs EUV — must use reflective optics, not lenses.
- **Optics**: Multilayer Mo/Si mirrors (40+ bilayer pairs, ~3 nm period each). Each mirror reflects ~70% of EUV. 10-mirror system transmits only ~3% of source light. Mirror figure accuracy: <0.1 nm RMS.
- **Resist**: New chemically amplified resists, metal-oxide resists, or molecular glass resists. Sensitivity, resolution, and line-edge roughness (LER) are competing requirements.
- **Vacuum**: Entire beam path must be in high vacuum (EUV absorbed by any gas).
- **This is one of the last achievements — incredibly demanding.** Even with full modern knowledge, EUV required 20+ years and $10B+ investment by ASML and partners.

### Stepper and Scanner Mechanical Design

A modern lithography scanner is one of the most precise machines ever built. The wafer stage must position a 300 mm silicon wafer with nanometer accuracy while moving at 500-700 mm/s.

**Wafer stage**:
- **Air bearing stage**: Wafer chuck rides on a granite block supported by air bearings (pressurized air film, ~3-5 μm gap). Frictionless motion enables smooth, vibration-free scanning. Linear motors drive X/Y axes; reaction masses on the same air bearing cancel recoil forces so the machine frame doesn't vibrate.
- **Position measurement**: Heterodyne laser interferometers (HeNe laser, λ = 632.8 nm) measure stage position with sub-nanometer resolution. Multiple interferometer beams (typically 4-6 axes) simultaneously measure X, Y, rotation (θx, θy, θz), and stage mirror flatness corrections.
- **Overlay accuracy**: <2.5 nm (3σ) on current immersion scanners for 300 mm wafers. This means every layer must align to the previous layer within a few atoms of the target position across the entire 707 cm² wafer.
- **Vibration isolation**: Pneumatic isolators and active vibration cancellation (accelerometers feed back to piezo actuators) suppress floor vibrations to <1 nm at the lens-wafer gap.

**Reticle stage**: Similar air-bearing design for the mask. Scans in synchrony with the wafer stage at a velocity ratio determined by the reduction optics (4:1 reduction → reticle stage moves 4x faster than wafer stage). Must maintain synchronization to <1 nm during the scan exposure.

### Excimer Laser Construction

Excimer (excited dimer) lasers produce DUV light from gas mixtures that only lase in an excited state. They are the workhorse light source for DUV lithography.

**Common types**:
| Laser | Wavelength | Gas Mix | Power | First Use |
|-------|-----------|---------|-------|-----------|
| KrF | 248 nm | Kr + F₂ + Ne/He buffer | 20-40 W | ~1994 (250 nm node) |
| ArF | 193 nm | Ar + F₂ + Ne/He buffer | 20-60 W | ~2000 (130 nm node) |
| F₂ | 157 nm | F₂ + He/Ne buffer | 2-5 W | Never deployed in production |

**Key subsystems**:
- **Discharge tube**: Ceramic or metal tube (~50-100 cm long) with pre-ionization pins that create a uniform plasma before the main discharge. Electrodes must withstand highly corrosive fluorine gas — typically nickel or aluminum alloys.
- **Discharge circuit**: High-voltage (15-30 kV) thyratron or solid-state switch discharges a capacitor bank through the gas in ~100 ns pulses. Peak current: 10-50 kA. Pulse energy: 5-30 mJ per pulse.
- **Gas handling system**: Excimer laser gas degrades with use (fluorine reacts with tube materials, generates impurities). Closed-cycle gas system with purifiers and gas replenishment. Typical gas lifetime: 1-5 million pulses before gas exchange.
- **Repetition rate**: 1000-6000 Hz (modern ArF lasers). Higher rep rate → more wafer throughput, but also more thermal load on optics and gas.
- **Spectral purity**: Intracavity line-narrowing optics (etalons, prisms) reduce bandwidth to <0.5 pm FWHM — required for chromatic aberration control in high-NA projection lenses.

### Immersion Fluid System

At 193 nm (ArF), dry lithography hits a numerical aperture ceiling of ~0.93 due to the maximum practical lens half-angle. Immersion introduces a fluid (ultrapure water) between the final lens element and the wafer, raising NA to 1.35 and enabling ~40 nm half-pitch resolution.

**Water as immersion fluid**:
- Refractive index of water at 193 nm: n ≈ 1.44. This directly multiplies the achievable NA (NA = n × sin θ, where θ is the collection half-angle).
- **Purity**: 18.2 MΩ·cm deionized water, filtered to remove particles >20 nm, degassed to prevent bubble formation (bubbles scatter DUV light and cause defects).
- **Temperature control**: ±0.01°C stability required. Refractive index of water changes by ~1×10⁻⁴/°C at 193 nm — even 0.1°C variation causes measurable focus drift across the exposure field. Temperature-controlled water circulation system integrated into the scanner lens assembly.
- **Flow control**: Continuous water flow through the lens-wafer gap (~1-2 mm area) at 0.1-0.5 L/min. Must fill and drain without bubbles as the stage scans at 500+ mm/s. A meniscus-shaped water boundary follows the lens across the wafer.

**Defect management**: Water contact with the wafer surface can extract photoresist components (leaching), which then deposit on the lens. Topcoat layers on resist or inherently hydrophobic resist surfaces mitigate this.

### Resolution Enhancement Techniques (RET)

Lithography at k₁ < 0.5 (well below the Rayleigh limit of k₁ = 0.25 for coherent illumination) requires aggressive optical tricks to print features that the raw lens cannot resolve.

**Optical Proximity Correction (OPC)**: Pre-distorts mask shapes to compensate for diffraction-induced pattern distortions. Lines that are too close together print wider than isolated lines (proximity effect) — OPC adds serifs, hammerheads, and sub-resolution assist features to equalize printed linewidths across all pattern densities. Modern OPC is computed by full-chip simulation on large compute clusters.

**Phase Shift Masks (PSM)**: Alternating aperture PSM etches adjacent mask apertures to different depths, creating a 180° phase shift between them. Destructive interference at feature edges sharpens the aerial image, improving contrast and resolution. Attenuated PSM (partially transmitting chrome) provides a milder benefit with simpler mask fabrication.

**Sub-Resolution Assist Features (SRAF)**: Small features added to the mask that are too small to print themselves (~0.5× the target feature size) but modify the diffraction pattern to improve printing of nearby main features. Used extensively with off-axis illumination.

**Off-axis illumination**: Conventional on-axis illumination has limited depth of focus at small features. Dipole, quadrupole, and annular illumination shapes redirect light at oblique angles through the lens, improving contrast for specific pattern orientations (lines/spaces) at the cost of restricted pattern flexibility.

### Throughput and Cost

Lithography is typically the throughput bottleneck and cost driver of a semiconductor fab.

**Throughput data** (typical modern equipment):
| Tool Type | Wafer Size | Throughput | Cost/Tool |
|-----------|-----------|------------|-----------|
| I-line stepper | 200 mm | 80-120 wafers/hr | $2-5M |
| KrF scanner | 200 mm | 100-150 wafers/hr | $5-10M |
| ArF dry scanner | 300 mm | 150-200 wafers/hr | $10-20M |
| ArF immersion scanner | 300 mm | 200-275 wafers/hr | $30-80M |
| EUV scanner | 300 mm | 100-180 wafers/hr | $200-350M |

**Cost impact**: Lithography capital accounts for 30-50% of total fab equipment cost. At nodes below 45 nm using 193 nm ArF immersion, features smaller than the ~38 nm half-pitch limit require double, triple, or quadruple patterning — each additional pattern needs a full litho-etch cycle, multiplying process steps, mask count, and defect risk. EUV's value proposition is collapsing multiple patterning passes back to a single exposure, but at $200-350M per scanner, only the highest-volume fabs can justify it.
### Hazards & Safety

- **F₂ gas (157 nm lithography)**: Molecular fluorine is extremely reactive — etches glass, ignites organic materials on contact, and causes severe chemical burns to lungs and skin. Storage and delivery require passivated nickel or Monel plumbing; no glass or elastomer components in the gas path. F₂ scrubbers (soda-lime or activated alumina) mandatory on all exhaust. Never deployed in volume production partly due to these handling difficulties.
- **Kr / Ar excimer gas mixtures**: The noble gases (Kr, Ar) with fluorine are asphyxiation risks in confined spaces — they are odorless, colorless, and displace oxygen. Use O₂ monitors in laser rooms; alarm at 19.5 % O₂. Fluorine component adds the reactivity hazards noted above.
- **DUV radiation (248 nm, 193 nm)**: Deep UV causes severe corneal burns (photokeratitis) and skin erythema at doses far below visible-light thresholds. Enclose all beam paths with interlocked covers — the beam must terminate if any enclosure panel is opened. Wear DUV-rated safety glasses (OD 6+ at 193-248 nm) during alignment or maintenance. Check interlock function weekly.
- **High-voltage laser discharge (15-30 kV)**: Excimer laser discharge circuits store lethal energy in capacitor banks. Interlock the laser power supply so capacitors discharge through a bleeder resistor when panels are opened. Wait ≥5 × the RC time constant before servicing. Post "DANGER — HIGH VOLTAGE" signage. Only trained, authorized personnel may service laser power supplies.

---
*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
