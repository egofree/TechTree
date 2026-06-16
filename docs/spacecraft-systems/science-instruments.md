# Science Instruments

> **Node ID**: spacecraft-systems.science-instruments
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`optics`](../optics/index.md),
> [`silicon`](../silicon/index.md),
> [`electronics`](../electronics/index.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: science_payloads
> **Critical**: No — science instruments are the entire reason most spacecraft exist. A Mars orbiter without a spectrometer is an expensive bus. Yet the instruments build on the same optical, detector, and electronics foundations as telescopes and cameras — the science return comes from precision engineering, not exotic physics

Spaceborne science instruments are the eyes, ears, and chemical noses of every space mission. They convert photons, particles, magnetic fields, and surface samples into digital data that reveals the composition, structure, and dynamics of the universe. From the cosmic-ray detectors on Voyager (still operating after 45+ years) to the cryogenic spectrometers on JWST, all instruments share a common architecture: a collector (telescope, aperture, or sampler), a dispersive or selective element (grating, filter, magnetic lens), a detector (CCD, microchannel plate, solid-state sensor), and signal-processing electronics.

This article covers four instrument families: [particle detectors](./science-instruments.particle-detectors.md) for measuring charged and neutral radiation, [magnetometers](./science-instruments.magnetometers.md) for mapping magnetic fields, [spectrometers](./science-instruments.spectrometers.md) for analyzing electromagnetic spectra, and [in-situ probes](./science-instruments.in-situ-probes.md) for direct surface and atmospheric sampling. The [optics](../optics/index.md) domain supplies telescope mirrors, gratings, and filters. The [silicon](../silicon/index.md) domain provides the detector substrates. [Electronics](../electronics/index.md) delivers low-noise readout circuits. [Radiation safety](../ehs/radiation-safety.md) knowledge informs instrument calibration and shielding design.

## Overview

A science instrument is defined by three parameters: **sensitivity** (minimum detectable signal), **resolution** (ability to distinguish closely spaced features), and **dynamic range** (ratio of brightest to dimmest measurable signal). Every instrument design is a trade between these three, constrained by mass, power, data rate, and the radiation environment.

| Parameter | Unit | Meaning | Example |
|-----------|------|---------|---------|
| Sensitivity | photons/s, eV, nT | Minimum detectable signal above noise | JWST NIRCam detects <1 photon/s per pixel |
| Spectral resolution | λ/Δλ (R) | Ability to distinguish wavelengths | NIRSpec R~2700; MIRI R~1500-3500 |
| Spatial resolution | arcsec, m/pixel | Angular or ground-sample distance | Hubble WFC3: 0.04 arcsec/pixel |
| Temporal resolution | Hz, s | Sampling rate | Magnetometer: 0-128 Hz vector rate |
| Dynamic range | bits or ratio | Brightest-to-dimmest ratio | Hubble CCD: 16-bit (65,536 levels) |
| Field of view | deg², arcmin² | Instantaneous sky coverage | JWST NIRCam: 9.7 arcmin² |

## JWST Instruments

The James Webb Space Telescope (launched 2021) carries four science instruments behind a 6.5-m segmented gold-coated beryllium primary mirror, operating at cryogenic temperatures (40 K for near-IR, <7 K for mid-IR) maintained by a five-layer sunshield.

### NIRCam (Near-Infrared Camera)

NIRCam is JWST's primary imager, covering 0.6-5.0 microns. It images two fields simultaneously (modules A and B), each with a 2.2×2.2 arcmin field of view.

| Parameter | Value |
|-----------|-------|
| Wavelength | 0.6-5.0 μm |
| Detectors | 10× Teledyne H2RG HgCdTe arrays |
| Pixel format | 2048×2048 per detector |
| Pixel size | 18 μm (0.034 arcsec/pixel) |
| Field of view | 2.2×2.2 arcmin per module |
| Operating temp | ~37 K (predicted 39 K) |
| Coronagraphs | 5 coronagraphic masks (0.3-1.6") |
| Grism | slitless spectroscopy R~700 |

The H2RG (HAWAII-2RG) detector is the workhorse of near-IR astronomy: a 2048×2048 mercury-cadmium-telluride (HgCdTe) array read out through 32 output amplifiers at 100 kHz each, yielding a full-frame read time of ~10.7 s. The array achieves read noise of ~15 e- (double-correlated sampling) or <5 e- with up-the-ramp sampling (MULTIACCUM).

### NIRSpec (Near-Infrared Spectrograph)

NIRSpec is the first multi-object spectrograph in space, capable of obtaining spectra of 100+ objects simultaneously using a micro-shutter array.

| Parameter | Value |
|-----------|-------|
| Wavelength | 0.6-5.3 μm |
| Resolving power | R~100, R~1000, R~2700 |
| Detectors | 2× H2RG HgCdTe (2048×2048) |
| Micro-shutter array | 250×250 shutters, 100×200 μm each |
| Slit spectroscopy | 5 fixed slits, 0.2×3.2" |
| IFU | 3×3 arcsec integral field unit |
| Operating temp | ~37 K |

The micro-shutter array (MSA) is a remarkable MEMS device: 62,415 individually addressable shutters fabricated from silicon, each 100×200 μm, magnetically actuated to open or close. This allows NIRSpec to select multiple targets in a single field without slit-mask exchange mechanisms.

### MIRI (Mid-Infrared Instrument)

MIRI covers the 5-28 micron range with both an imager and a medium-resolution spectrometer (MRS). It is the only JWST instrument requiring active cooling to <7 K via a closed-cycle cryocooler.

| Parameter | Value |
|-----------|-------|
| Wavelength | 5-28 μm (imager), 5-28 μm (MRS) |
| Resolving power | R~1500-3500 (MRS) |
| Imager detector | 1024×1024 Si:As IBC array |
| MRS detectors | 2× 1024×1024 Si:As IBC |
| Operating temp | <7 K (cryocooler) |
| IFU channels | 4 simultaneous spectral channels |
| Coronagraph | 4 coronagraphic spots (10-23 μm) |

The Si:As Impurity Band Conduction (IBC) detectors operate at 6-7 K and detect mid-IR photons via arsenic impurity levels in silicon. Unlike HgCdTe, IBC detectors use blocked-impurity-band architecture to reduce dark current at very long wavelengths.

## Hubble Instruments

The Hubble Space Telescope (launched 1990, serviced 5 times) carries instruments covering UV through near-IR behind a 2.4-m primary mirror. Servicing missions replaced instruments, keeping Hubble at the cutting edge for 35+ years.

### WFC3 (Wide Field Camera 3)

WFC3 replaced WFPC2 in 2009 and provides wide-field imaging in two channels: UVIS (200-1000 nm) and IR (800-1700 nm).

| Parameter | UVIS Channel | IR Channel |
|-----------|-------------|-----------|
| Wavelength | 200-1000 nm | 800-1700 nm |
| Detector | 2× e2v CCD43 | Teledyne H1RG HgCdTe |
| Format | 4096×4096 (2K×4K×2) | 1024×1024 |
| Pixel scale | 0.04 arcsec | 0.13 arcsec |
| Field of view | 162×162 arcsec | 136×123 arcsec |
| Operating temp | -85 to -75 °C | 145 K (thermoelectric) |

The UVIS CCDs are thinned, back-illuminated devices optimized for UV quantum efficiency. At 200 nm, they achieve >30% QE — roughly double that of standard front-illuminated CCDs.

### COS (Cosmic Origins Spectrograph)

COS is a UV spectrograph installed in 2009, optimized for point-source spectroscopy in the far-UV (115-180 nm) and near-UV (170-320 nm).

| Parameter | FUV Channel | NUV Channel |
|-----------|------------|------------|
| Wavelength | 115-180 nm | 170-320 nm |
| Resolving power | R~20,000 (medium), R~3000 (low) | R~10,000-17,000 |
| Detector | CsI microchannel plate + cross-delay-line | CsTe MCP + cross-delay-line |
| Format | 16384×1024 (photon-counting) | 16384×1024 |
| Sensitivity | 10× better than STIS at 115 nm | 2× better than STIS |

COS uses microchannel plate (MCP) detectors because silicon CCDs have negligible QE below 110 nm. The MCP amplifies each UV photon into an electron cascade (gain ~10⁶), which strikes a cross-delay-line anode to register the photon position with <25 μm accuracy.

## Mars Rover Instruments

### CheMin (Chemistry and Mineralogy)

CheMin on NASA's Curiosity rover (Mars Science Laboratory, landed 2012) is the first X-ray diffraction/X-ray fluorescence (XRD/XRF) instrument used on another planet. It identifies mineral phases in powdered rock samples.

| Parameter | Value |
|-----------|-------|
| Technique | X-ray powder diffraction + fluorescence |
| X-ray source | Co K-alpha, 30 kV, 100 μA |
| Detector | CCD (1024×1024, energy-discriminating) |
| Sample wheel | 27 cells (5 ref, 22 unknown) |
| R-range | 1.0-15 Å (d-spacing) |
| 2-theta range | 5-50° |
| Mass | 10 kg |
| Power | 20-30 W |

CheMin's CCD operates in single-photon-counting mode: each X-ray photon is individually energy-dispersed, allowing simultaneous collection of diffraction patterns (from photon position) and fluorescence spectra (from photon energy). This dual-mode operation eliminates the need for separate XRD and XRF instruments.

### SAM (Sample Analysis at Mars)

SAM is Curiosity's suite of three in-situ instruments for organic and isotopic analysis of Martian soil and atmosphere.

| Component | Technique | Range | Sensitivity |
|-----------|-----------|-------|-------------|
| Quadrupole MS | Mass spectrometry | 2-535 Da | ppb (organics) |
| TLS | Tunable laser spectroscopy | CH4, CO2, H2O | sub-ppb (methane) |
| GC | Gas chromatography | 8 columns, C1-C12 | ppm-ppb |
| Sample handling | 74 sample cups, pyrolysis to 1100 °C | solids & gases | — |

The Tunable Laser Spectrometer (TLS) directs a 2-μm tunable diode laser through a multi-pass Herriott cell (effective path length 8.96 m) to measure isotopic ratios of CO2 and H2O, and trace methane at sub-ppb levels. Methane detection at <0.5 ppb required 1000+ laser sweeps averaged over 20 minutes.

## Spectrometer Types

### Dispersive (Grating/Prism)

Light is separated by wavelength using a diffraction grating or prism. The spectrum is focused onto a detector array, with each pixel recording a different wavelength. Used by NIRSpec, WFC3 grisms, and most UV/visible spectrometers.

- **Grating equation**: mλ = d(sin α + sin β), where d = groove spacing, α/β = incidence/diffraction angles
- **Blazed grating**: grooves shaped to concentrate energy into one diffraction order (typically 1st order)
- **Echelle**: high-order (m=10-100), coarse grooves, crossed with low-dispersion prism for 2D spectral format
- **Free spectral range**: Δλ = λ/m; echelle requires order-sorting filter or cross-disperser

### Fourier-Transform (FTS)

An FTS uses a Michelson interferometer to record an interferogram, then applies a Fourier transform to obtain the spectrum. Used by atmospheric sounders (e.g., Atmospheric Infrared Sounder on Aqua).

- **Advantage**: high throughput (Jacquinot advantage), simultaneous all-wavelength measurement (Fellgett advantage)
- **Resolution**: Δν = 1/(2×ΔL), where ΔL = maximum mirror travel
- **Typical**: 0.1-10 cm⁻¹ resolution in the thermal IR (3-15 μm)

### Fabry-Perot (Etalon)

A Fabry-Perot interferometer uses two parallel partially-reflective plates to create a resonant cavity, transmitting only specific wavelengths. Used for narrow-band imaging of emission lines (e.g., Mars Atmosphere and Volatile Evolution — MAVEN — IUVS).

- **Resolution**: R = π√F / (1-R²)^½ where R = plate reflectivity, F = finesse
- **Typical**: R~1000-10,000 for space etalons with F>20

## Detector Technologies

| Detector type | Wavelength range | Operating temp | Read noise | Dark current | Example use |
|--------------|-----------------|---------------|-----------|-------------|-------------|
| CCD | 300-1000 nm | -80 to -100 °C | 3-5 e- | 0.001 e-/s | Hubble WFC3 UVIS |
| CMOS (APS) | 300-1000 nm | -40 °C | 1-2 e- | 0.01 e-/s | Star trackers, snapshot imaging |
| HgCdTe (H2RG) | 0.6-5.4 μm | 30-77 K | 10-20 e- | 0.001-0.1 e-/s | JWST NIRCam/NIRSpec |
| Si:As IBC | 5-28 μm | 5-8 K | 14-50 e- | <0.1 e-/s | JWST MIRI |
| InSb | 3-5 μm | 30-77 K | 10-30 e- | 0.01-0.1 e-/s | Early-warning, astronomy |
| Microchannel plate | 10-200 nm | -30 °C | none (pulse counting) | <0.1 counts/s | Hubble COS FUV |
| Silicon strip | charged particles | -10 to -30 °C | 1-2 keV (energy) | none | Alpha Magnetic Spectrometer |

### HgCdTe (Mercury Cadmium Telluride)

HgCdTe is the dominant near-to-mid-IR detector material because its bandgap is tunable by adjusting the Hg/Cd ratio. A composition of Hg₀.₇Cd₀.₃Te has a 5-micron cutoff at 77 K; Hg₀.₅₅Cd₀.₄₅Te extends to 2.5 microns for near-IR.

- **Cutoff wavelength**: λ_c = 1.24 / E_g(x,T), where E_g is the composition-dependent bandgap
- **Manufacturing**: liquid-phase epitaxy (LPE) or molecular-beam epitaxy (MBE) on CdZnTe substrates
- **Readout**: bump-bonded to a silicon CMOS multiplexer (ROIC), forming a hybrid array
- **Largest format**: 4096×4096 (H4RG) — 16 million pixels, 10 cm diagonal

### CCD vs CMOS

Charge-coupled devices (CCDs) transfer charge across the array to a single readout amplifier, achieving very low noise but slow readout. Complementary metal-oxide-semiconductor (CMOS) sensors have an amplifier at every pixel, enabling fast, random-access readout at slightly higher noise. For space science, CCDs dominate UV/visible astronomy (low noise is critical) while CMOS increasingly replaces CCDs in high-frame-rate applications (wavefront sensing, autonomous navigation).

## Radiation Effects on Instruments

Space instruments operate in harsh radiation environments that degrade detector performance. See [radiation safety](../ehs/radiation-safety.md) for the full treatment of spacecraft radiation hardening.

| Effect | Mechanism | Detector impact | Mitigation |
|--------|-----------|-----------------|------------|
| Ionizing dose (TID) | Cumulative lattice damage | Increased dark current, RTN | Shielding, annealing |
| Displacement damage | Proton/neutron knock-on atoms | CTE degradation in CCDs | Inverted-mode (n-channel) CCDs |
| Single-event upsets | Cosmic-ray ionization | Hot pixels, transient spikes | Dodd filtering, pixel masking |
| Solar proton events | SPE particle fluxes | Sudden dark-current spikes | Operational safing, annealing |

For JWST at L2, the total ionizing dose behind the sunshield is <1 krad over 10 years. For a Jupiter mission (e.g., Europa Clipper), the dose can exceed 1 Mrad, requiring thick tantalum shielding around the detector assemblies.

## Instrument Calibration

Every science instrument requires calibration to convert raw detector output into physical units. Calibration establishes the relationship between measured signal (counts, volts, DN) and the incident physical quantity (photons, particles, field strength).

### Pre-Launch Calibration

Ground calibration uses known reference sources to characterize the instrument before launch:

- **Spectral calibration**: monochromator scan to map pixel-to-wavelength relationship
- **Photometric calibration**: NIST-traceable standard lamps and integrating spheres for absolute flux
- **Flat-field calibration**: uniform illumination source to map pixel-to-pixel gain variations
- **Dark calibration**: long exposures with shutter closed to measure dark current and hot pixels
- **Wavelength calibration**: emission-line lamps (Ar, Ne, Hg, Kr) for spectrograph line identification

### On-Orbit Calibration

Once in space, instruments are recalibrated periodically using on-board calibration sources and astronomical standards:

- **Astronomical standards**: spectrophotometric standard stars (e.g., BD+17°4708) with well-calibrated spectral energy distributions
- **On-board lamps**: tungsten or NIST lamps for flat-field tracking; deuterium lamps for UV response
- **Dark monitoring**: regular dark exposures to track radiation damage and new hot pixels
- **Degradation tracking**: comparison with stable astrophysical sources (white dwarfs, G-type stars)

For JWST, the calibration program consumes ~10-15% of total observing time, distributed across all science instruments each cycle. Hubble's CALSPEC database of standard stars is the foundation of flux calibration for all UV/optical space astronomy.

## Data Processing Pipeline

Raw instrument data is never delivered to scientists directly. A processing pipeline converts raw telemetry into calibrated, science-ready data products:

| Pipeline stage | Input | Output | Example |
|---------------|-------|--------|---------|
| Raw | Telemetry packets | Uncalibrated FITS files | CCSDS packets → ramp files |
| Detector processing | Raw ramps | Slope images (rate) | JWST pipeline: slope fitting, cosmic-ray removal |
| Calibration | Slope images | Calibrated images | Dark subtraction, flat-field, wavelength solution |
| Astrophysics | Calibrated images | Science products | Spectra, catalogs, mosaics |

The JWST calibration pipeline (jwst package) has 200+ processing steps across three stages, transforming raw detector ramps into publication-ready spectra and images.

## Strengths

- Enables direct measurement of physical quantities that cannot be determined any other way
- Multi-wavelength coverage (UV to far-IR, particles to magnetic fields) reveals complementary information
- In-situ analysis (CheMin, SAM) provides ground truth for remote sensing observations
- Cryogenic detectors (HgCdTe, IBC) achieve near-theoretical sensitivity limited only by photon shot noise
- Decades of heritage: Hubble's 35-year operating life demonstrates instrument longevity
- Servicing (Hubble) and modularity (JWST instrument module) enable technology upgrades

## Weaknesses

- Cryogenic instruments require complex cooling systems with limited lifetime (cryocooler wear, cryogen boil-off)
- Detector arrays are custom-fabricated in small quantities, leading to high cost and long lead times
- Radiation damage accumulates over mission lifetime, requiring periodic annealing and calibration updates
- Data volume from modern instruments (JWST generates ~50 GB/day) strains downlink capacity
- Instrument development takes 10-15 years from concept to launch, locking in old technology

## See Also

- [Particle Detectors](./science-instruments.particle-detectors.md) — solid-state, gas, and time-of-flight systems
- [Magnetometers](./science-instruments.magnetometers.md) — fluxgate, search-coil, and scalar instruments
- [Spectrometers](./science-instruments.spectrometers.md) — JWST, Hubble, and planetary instruments
- [In-Situ Probes](./science-instruments.in-situ-probes.md) — CheMin, SAM, and surface sampling
- [Optics](../optics/index.md) — telescope mirrors, gratings, and optical design
- [Silicon](../silicon/index.md) — detector substrates and CCD/CMOS fabrication
- [Electronics](../electronics/index.md) — low-noise readout and signal processing
- [Radiation Safety](../ehs/radiation-safety.md) — radiation environment and shielding
- [Radiation Hardening](./radiation-hardening.md) — spacecraft electronics protection

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
