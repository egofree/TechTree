# Earth Observation Payloads

> **Node ID**: spacecraft-systems.earth-observation
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: `optics`, `silicon`, `electronics`, `measurement`
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: eo_payloads
> **Critical**: No — Earth observation builds on mature optical, detector, and RF technologies; the challenge is pushing resolution, spectral coverage, and sensitivity to their physical limits under spacecraft constraints of mass, power, and data downlink

Earth observation (EO) payloads are the eyes of a spacecraft pointed back at Earth. They capture electromagnetic radiation reflected or emitted from the surface across the spectrum from visible light through thermal infrared to microwave radar, transforming photons into data that maps crops, tracks ships, measures ground deformation, monitors wildfires, and counts buildings. The first weather satellite (TIROS-1, 1960) returned grainy 0.3-megapixel television images; today's WorldView-4 captures 0.31-metre panchromatic imagery across 13 km swaths. This 600× improvement in ground resolution over six decades represents the steady conquest of optical, detector, data-processing, and attitude-control limits — not a single breakthrough.

This article covers four process areas: [optical imagers](./earth-observation.optical-imagers.md) (high-resolution panchromatic and multispectral imaging), [synthetic aperture radar](./earth-observation.sar-radar.md) (all-weather microwave imaging), [hyperspectral imagers](./earth-observation.hyperspectral.md) (hundreds of narrow spectral bands), and [thermal infrared sensors](./earth-observation.thermal-infrared.md) (surface temperature mapping). The [optics](../optics/index.md) domain supplies telescope mirrors, lenses, and optical coatings; [silicon](../silicon/index.md) provides the CCD and CMOS detector arrays; [electronics](../electronics/index.md) delivers the readout ICs and signal chains; [measurement](../measurement/index.md) underpins the radiometric calibration that makes imagery quantitatively useful.

## Ground Sample Distance

Ground sample distance (GSD) is the physical size of one pixel projected onto the Earth's surface. It is the single most important EO metric — a 0.3-m GSD image can identify individual vehicles, a 3-m image can resolve buildings, a 30-m image can distinguish urban from forest. GSD is set by telescope aperture, orbital altitude, and detector pixel pitch:

```
GSD = H × p / f
```

where H is orbital altitude, p is detector pixel pitch, and f is telescope focal length. For a 600 km orbit, 10 μm pixels, and a 1.2-m focal length telescope (typical of WorldView-class), GSD = 600,000 × 0.000010 / 1.2 = 0.5 m. The diffraction limit sets a floor: at 500 nm wavelength and 0.5-m aperture, the Rayleigh limit is 1.22 × 5×10⁻⁷ / 0.5 = 1.22 μrad, giving 0.73 m at 600 km.

### Representative Imaging Systems

| System | Operator | Orbit | GSD (pan) | GSD (MS) | Swath | Revisit |
|--------|----------|-------|-----------|----------|-------|---------|
| WorldView-3 | Maxar (DigitalGlobe) | 617 km SSO | 0.31 m | 1.24 m | 13.1 km | <1 day |
| WorldView-4 | Maxar | 617 km SSO | 0.31 m | 1.24 m | 13.2 km | <1 day |
| GeoEye-1 | Maxar | 681 km SSO | 0.41 m | 1.65 m | 15.2 km | <3 days |
| Pleiades-HR | Airbus (CNES) | 694 km SSO | 0.5 m | 2.0 m | 20 km | daily |
| PlanetScope | Planet Labs | 475 km SSO | — | 3.0 m | 24 km | daily (fleet) |
| Landsat-9 | NASA/USGS | 705 km SSO | 15 m | 30 m | 185 km | 16 days |
| Sentinel-2A/B | ESA (Copernicus) | 786 km SSO | 10 m | 10-60 m | 290 km | 5 days |
| SPOT-6/7 | Airbus | 694 km SSO | 1.5 m | 6.0 m | 60 km | daily |

Sub-metre resolution (WorldView, GeoEye, Pleiades) requires large telescopes (1+ metre aperture) flying at the lowest practical altitude, pushing mass, stability, and pointing budgets. Medium-resolution constellations (PlanetScope, Sentinel-2) trade resolution for coverage and revisit, using fleets of small satellites to achieve daily global imaging.

## Optical Imager Architecture

A pushbroom imager — the standard for modern EO — uses a linear or 2D detector array that stares downward as the spacecraft moves forward, sweeping a strip of ground across the array like a broom. Each pixel integrates photons for a few milliseconds (the time for the sub-satellite point to advance one GSD), then the array is read out and the next line is captured.

### Telescope Design

- **All-refractive**: lenses only, compact, limited to visible/NIR, used for wide-field (PlanetScope)
- **All-reflective (Cassegrain/Ritchey-Chrétien)**: mirrors only, no chromatic aberration, broadest spectral range, used for high-res (WorldView, Pleiades)
- **Catadioptric**: mirrors + corrector lenses, balanced performance, used for Landsat, Sentinel-2
- **Off-axis three-mirror anastigmat (TMA)**: no central obstruction, excellent stray-light control, used for WorldView-3

WorldView-3's telescope is a 1.1-m aperture off-axis TMA with a 13.3-m focal length (f/12). The mirror is ultra-low-expansion (ULE) glass, polished to λ/40 (12 nm RMS) and coated with protected aluminium. The structure is designed so thermal expansion does not change focus by more than 1% of the depth of field across the -50 °C to +50 °C orbital temperature swing.

### Detector Arrays

Modern EO imagers use either CCD (charge-coupled device) or CMOS (complementary metal-oxide-semiconductor) arrays. WorldView-3 uses CCDs; newer systems increasingly use CMOS for lower power and on-chip processing.

| Parameter | CCD (WorldView-3) | CMOS (modern) | Unit |
|-----------|-------------------|---------------|------|
| Pixel pitch | 8-10 | 5-10 | μm |
| Array size | 35K × 1 (stitched) | 10K × 10K | pixels |
| Quantum eff. (550 nm) | 70-80 | 70-85 | % |
| Read noise | 10-15 | 2-5 | e⁻ |
| Dark current | 0.5-1.0 | 0.1-0.5 | e⁻/s |
| Dynamic range | 70-80 | 80-90 | dB |
| Readout speed | 5-10 | 30-60 | MPix/s |
| Power per array | 1-2 | 0.3-0.8 | W |

The linear array must span the full swath. WorldView-3 stitches 35,000 pixels across 13.1 km — each pixel corresponds to 0.37 m on the ground. Stitching is done mechanically (abutting physically separate CCDs) or optically (using a Schlömilch prism to split and recombine the image).

## Multispectral & Hyperspectral Bands

Every material reflects and absorbs light at characteristic wavelengths. Soil, vegetation, water, concrete, and asphalt have distinct spectral signatures that EO imagers exploit by capturing multiple discrete wavelength bands (multispectral) or hundreds of contiguous narrow bands (hyperspectral).

### Band Comparison Table

| Band | Wavelength | Application | WorldView-3 | Landsat-9 | Sentinel-2 |
|------|-----------|-------------|-------------|-----------|------------|
| Coastal | 400-450 | Water depth, aerosols | Yes (8-band) | — | — |
| Blue | 450-510 | Bathymetry, soil/veg | Yes | Yes (30 m) | Yes (10 m) |
| Green | 510-580 | Vegetation vigour | Yes | Yes (30 m) | Yes (10 m) |
| Yellow | 585-625 | Vegetation stress | Yes | — | — |
| Red | 630-690 | Chlorophyll absorption | Yes | Yes (30 m) | Yes (10 m) |
| Red Edge | 705-745 | Plant health, species | Yes | — | Yes (20 m) |
| NIR | 770-900 | Biomass, water delineation | Yes | Yes (30 m) | Yes (10 m) |
| NIR-2 | 860-1040 | Vegetation, atmosphere | Yes | — | — |
| SWIR-1 | 1550-1590 | Snow/cloud, moisture | Yes (3.7 m) | Yes (30 m) | Yes (20 m) |
| SWIR-2 | 1640-1680 | Burn scars, minerals | — | Yes (30 m) | — |
| SWIR-3 | 1710-1750 | Cloud, snow, soil | Yes (3.7 m) | — | — |
| SWIR-4 | 2145-2185 | Lignite, uranium | Yes (3.7 m) | — | — |
| SWIR-5 | 2185-2225 | Rock, mineral mapping | Yes (3.7 m) | — | — |
| SWIR-6 | 2295-2365 | Soil, man-made | Yes (3.7 m) | — | — |
| MWIR | 3300-3500 | Active fire, heat | — | — | — |
| LWIR | 10,300-11,300 | Surface temperature | Yes (5 m TIR) | Yes (100 m) | — |
| Cirrus | 1360-1390 | Thin cloud detection | Yes | — | — |

WorldView-3's 29 bands (8 visible/NIR + 8 SWIR + 12 CAVIS atmospheric) represent the state of the art in commercial multispectral imaging. Landsat-9's 11 bands provide 50+ years of continuity for climate and land-cover studies. Hyperspectral imagers (covered separately) extend this to 200+ contiguous bands.

### Spectral Signature Examples

- **Healthy vegetation**: strong reflectance in NIR (770-900 nm) due to leaf cell structure, sharp red-edge transition (700-740 nm), strong absorption in red (chlorophyll) and blue
- **Dry soil**: gradual increasing reflectance from 400-1300 nm, no red-edge feature, moderate SWIR reflectance
- **Clear water**: low reflectance overall, decreasing further in NIR and SWIR (water absorbs >1200 nm), enabling shoreline delineation
- **Snow**: high visible reflectance (>80%), distinctive absorption dips at 1020 and 1250 nm, low SWIR reflectance (<20%) — distinguishes from cloud

## Synthetic Aperture Radar

Synthetic aperture radar (SAR) solves the fundamental limitation of optical imaging: clouds. SAR transmits microwave pulses and measures the backscattered return, producing imagery day or night, through cloud and rain. By coherently combining returns collected along the satellite's flight path, a short physical antenna synthesizes a much longer "aperture," achieving metre-scale resolution independent of altitude.

### SAR Resolution Physics

**Azimuth (along-track) resolution** of a real-aperture radar is `R λ / D` — it degrades with range. SAR synthesis overcomes this: the synthetic aperture length is the beam footprint on the ground `R λ / D`, and the azimuth resolution becomes `D / 2` — independent of range and wavelength. A 5-m antenna achieves 2.5-m azimuth resolution at any altitude.

**Range (cross-track) resolution** depends on pulse bandwidth: `ρ_r = c / (2B)`. A 50 MHz pulse gives 3 m range resolution. Pulse compression (chirped FM) achieves this bandwidth without extreme peak power by sweeping frequency over the pulse duration.

| Parameter | Sentinel-1 (C-band) | TerraSAR-X (X-band) | ALOS-2 (L-band) |
|-----------|---------------------|---------------------|------------------|
| Frequency | 5.405 GHz | 9.65 GHz | 1.258 GHz |
| Wavelength | 5.6 cm | 3.1 cm | 23.8 cm |
| Resolution (SLC) | 5 × 20 m | 1-3 m | 3-10 m |
| Swath | 250 km | 10-100 km | 25-350 km |
| Incidence angle | 20-47° | 20-55° | 8-70° |
| Polarization | Single, dual, dual+ | Single, dual, quad | Single, dual, quad |
| Antenna size | 12.3 × 0.82 m | 4.8 × 0.7 m | 9.9 × 2.9 m |
| Peak power | 4.4 kW | 2.3 kW | 6.0 kW |

L-band (24 cm) penetrates vegetation and dry soil, revealing forest structure and subsurface features. C-band (5.6 cm) balances penetration and resolution — the workhorse for ice, ocean, and land monitoring. X-band (3 cm) provides the highest resolution but minimal penetration, ideal for surface mapping and urban monitoring.

### SAR Imaging Modes

- **Stripmap**: continuous along-track imaging, balanced resolution and swath, the baseline mode
- **ScanSAR**: electronically steers the beam across multiple sub-swaths, widening swath at the cost of azimuth resolution (Sentinel-1: 250 km swath, 20 m resolution)
- **Spotlight**: steers the beam to illuminate a fixed target longer, trading swath for azimuth resolution (TerraSAR-X Spotlight: 1 m resolution, 10 km swath)
- **Staring Spotlight**: maximizes illumination time, sub-metre azimuth resolution (TerraSAR-X: 0.25 m)

## Thermal Infrared

Thermal infrared (TIR) sensors measure surface temperature by detecting emitted longwave radiation. Earth (at ~300 K) emits peak radiation near 10 μm (Wien's displacement law). TIR imagers capture this emission through atmospheric windows at 3-5 μm (MWIR) and 8-12 μm (LWIR), mapping surface temperature, active fires, volcanic activity, and urban heat islands.

Landsat-9's TIRS instrument captures two thermal bands (10.6 μm and 12.0 μm) at 100 m resolution, enabling split-window surface temperature retrieval to ±1 K accuracy. VIIRS (Suomi-NPP, JPSS) captures 6 thermal bands including a 375 m "day-night band" that detects active fires down to 10 m × 10 m sub-pixel hotspots. MODIS provides global daily thermal data at 1 km resolution for fire and temperature monitoring.

## Data Volume & Downlink

EO payloads generate enormous data volumes. WorldView-3 produces up to 680 gigabits per orbit in 29-band mode. Sentinel-2 captures 1.5 TB per orbit across its 290-km swath. This data must be stored onboard and downlinked during ground-station passes.

| System | Data per orbit | Compression | Downlink rate | Band |
|--------|---------------|-------------|---------------|------|
| WorldView-3 | 680 Gbit | 2:1 DPCM | 800 Mbps | X-band |
| Sentinel-2 | 1.5 TB | lossless JPEG2000 | 560 Mbps | X-band + Ka-band |
| Landsat-9 | 400 Gbit | 2:1 (lossy) | 384 Mbps | X-band |
| PlanetScope (per sat) | 2 Gbit | 3:1 | 200 Mbps | X-band |
| Planet (fleet, daily) | 7 TB | — | multiple X-band | X-band |

Data compression is essential. Lossless JPEG2000 achieves 2:1 on typical imagery; near-lossless 3:1; lossy 4-8:1 for browse products. Onboard solid-state recorders use radiation-hardened flash memory (typically 256 GB - 5 TB depending on mission class).

## Calibration & Validation

Quantitative EO requires radiometric calibration: each pixel value must map to a known physical quantity (W·m⁻²·sr⁻¹·μm⁻¹ for reflectance, K for temperature). Calibration happens at three levels:

1. **Pre-flight**: integrate sphere or known source, characterize absolute radiometry and spectral response
2. **Onboard**: lamps, solar diffusers, or blackbodies measure sensor drift in orbit. Sentinel-2 uses a 40-cm Spectralon diffuser illuminated by the Sun once per orbit
3. **Vicarious**: image invariant ground targets (Libya-4 desert, Railroad Valley Playa, Antarctica) with independently measured surface reflectance to validate post-launch

Landsat-9 achieves ±3% radiometric accuracy and ±0.5 K thermal accuracy — sufficient for 50-year climate data records. WorldView-3 achieves ±5% absolute and ±2% relative band-to-band radiometry. The [measurement](../measurement/index.md) domain provides the metrology chain that makes these accuracies traceable to SI standards.

## Orbits for Earth Observation

Nearly all imaging satellites fly in sun-synchronous orbit (SSO), a near-polar low Earth orbit phased so the satellite crosses the equator at the same local solar time on every pass. This constant illumination angle is critical: it ensures that changes in image brightness reflect real surface changes, not Sun-angle artefacts.

| Orbit type | Altitude | Inclination | Period | Use case |
|-----------|----------|-------------|--------|----------|
| SSO (AM) | 400-800 km | 97-99° | 90-100 min | Optical (morning lighting) |
| SSO (PM) | 400-800 km | 97-99° | 90-100 min | Optical (afternoon lighting) |
| SSO (dawn-dusk) | 600-800 km | 98° | 100 min | SAR, lidar (constant Sun) |
| Non-SSO LEO | 400-600 km | 45-55° | 90 min | Mid-latitude access |
| GEO | 35,786 km | 0° | 24 hr | Weather, continuous regional |

The mean local solar time (MLST) of the descending node defines the orbit: Landsat uses 10:00 AM, Sentinel-2 uses 10:30 AM, WorldView uses 10:30 AM. Dawn-dusk SSO (06:00 / 18:00) provides constant illumination for SAR and lidar missions, and keeps the solar panels continuously Sun-lit — useful for power-hungry radar payloads.

## Pointing & Stability

High-resolution imaging demands exquisite attitude stability. WorldView-3 achieves 0.31 m GSD from 617 km, requiring pointing stability better than 0.005° (18 arcseconds) during the 0.5-ms integration time. Any motion during integration smears the image, degrading the effective GSD:

```
Smear = ω × H × t_int
```

At 600 km altitude, a 1-ms integration, and 0.01°/s drift: smear = 0.000175 × 600,000 × 0.001 = 0.1 m — negligible. But at 0.1°/s drift, smear = 1 m, destroying the sub-metre advantage. Reaction wheel jitter, solar array drive vibration, and cryocooler micro-vibration must all be actively suppressed.

| System | GSD | Required stability | Integration time |
|--------|-----|--------------------|------------------|
| WorldView-3 | 0.31 m | <0.002°/s | 0.4 ms |
| Pleiades | 0.5 m | <0.005°/s | 0.5 ms |
| Sentinel-2 | 10 m | <0.03°/s | 2.0 ms |
| Landsat-9 | 15-30 m | <0.05°/s | 4.4 ms |

Many high-res imagers also **slew** the spacecraft forward, backward, or sideways to image targets not directly below. WorldView-3 can slew 45° off-nadir, extending its effective revisit to under a day for any point on Earth — but at the cost of increased GSD (0.31 m at nadir becomes ~0.52 m at 45° off-nadir) and atmospheric path length.

## Atmospheric Correction

Light reflected from Earth's surface passes through the atmosphere, which scatters and absorbs at wavelength-dependent rates. Aerosol scattering (Rayleigh at short wavelengths, Mie at all wavelengths) adds a "haze" component; water vapour, ozone, and CO₂ absorb at specific bands. Atmospheric correction removes these effects to recover true surface reflectance.

- **Rayleigh scattering**: proportional to λ⁻⁴, dominates below 500 nm (blue sky), removed using band ratios or radiative transfer models
- **Aerosol scattering**: wavelength-dependent, spatially variable, estimated from dark-object subtraction or ancillary AERONET data
- **Water vapour absorption**: strong bands at 940, 1140, 1400, 1900 nm — these bands are avoided or used to estimate column water vapour
- **Ozone absorption**: band at 550-650 nm, corrected using TOMS/OMI column ozone data

WorldView-3's 12-band CAVIS (Clouds, Aerosols, water Vapour, Ice, Snow) atmospheric sensor flies alongside the imager to measure atmospheric properties simultaneously, enabling pixel-level correction. Without correction, 20-40% of observed radiance may be atmospheric path radiance rather than surface signal.

## SAR Interferometry (InSAR)

When a satellite images the same area from two slightly different positions (or on two passes), the phase difference between the returns reveals surface topography or deformation. SAR interferometry (InSAR) measures millimetre-scale ground movement — subsidence, earthquake displacement, volcanic inflation, glacier flow — over 100-km swaths.

- **Topographic InSAR**: two antennas separated by a fixed baseline (single-pass, SRTM mission) produce a digital elevation model. SRTM achieved 30 m posting, 6 m height accuracy.
- **Differential InSAR (DInSAR)**: two images of the same scene taken at different times reveal deformation between passes. Sentinel-1 routinely detects 1-cm ground motion from 700 km altitude.
- **Persistent scatterer InSAR (PSInSAR)**: stacks dozens of images over months/years, tracking phase-stable points (buildings, rocks) to millimetre-per-year velocities. Used for urban subsidence and volcano monitoring.
- **Limitations**: phase ambiguity (2π = one wavelength = 2.8 cm for C-band), atmospheric water vapour causes centimetre-level path delay errors, temporal decorrelation in vegetated areas.

## Troubleshooting

| Symptom | Likely cause | Diagnostic action |
|---------|-------------|-------------------|
| Blurry imagery | Jitter or attitude drift | Check gyro/reaction wheel logs; verify ADCS bandwidth |
| Banding in image | Detector line non-uniformity | Run relative radiometric calibration; check dark-frame |
| Low SNR in NIR | Detector degradation or coating aging | Check pre-flight vs in-orbit dark current trends |
| Geolocation offset | Star tracker or orbit error | Verify star tracker bias; check GPS/POD accuracy |
| SAR phase noise | Baseline decorrelation or atmosphere | Check perpendicular baseline; apply atmospheric phase screen |
| TIR calibration drift | Cryocooler temperature change | Monitor cold-finger temperature; update bias table |

## Strengths

- Mature technology: 60+ years of heritage from TIROS-1 (1960) to WorldView-4 (2016)
- Diverse sensing modalities: optical, SAR, hyperspectral, thermal — each reveals different Earth properties
- Constellations enable daily revisit: PlanetScope (200+ sats), Sentinel (twin sats), Maxar (6 sats)
- Radiometric calibration makes imagery quantitatively useful for science and policy
- CCSDS and OGC standards ensure interoperability across sensors and agencies

## Weaknesses

- Sub-metre optical requires large, expensive telescopes and exquisite pointing stability (0.01° or better)
- Cloud cover defeats optical imaging — SAR is the only all-weather option, at lower resolution
- Hyperspectral data volumes (hundreds of bands) strain downlink and processing infrastructure
- Thermal infrared requires cryocoolers for MWIR detectors, adding power and lifetime risk
- Data downlink is often the bottleneck: X-band ground stations are limited and expensive

## See Also

- [Optical Imagers](./earth-observation.optical-imagers.md) — telescope and detector design for high-resolution imaging
- [Synthetic Aperture Radar](./earth-observation.sar-radar.md) — SAR physics, modes, and hardware
- [Hyperspectral Imagers](./earth-observation.hyperspectral.md) — hundreds of spectral bands for material identification
- [Thermal Infrared Sensors](./earth-observation.thermal-infrared.md) — surface temperature and active fire detection
- [Optics](../optics/index.md) — telescope mirror manufacturing and optical coatings
- [Silicon](../silicon/index.md) — CCD and CMOS detector fabrication
- [Electronics](../electronics/index.md) — readout ICs, ADCs, and signal chains
- [Measurement](../measurement/index.md) — radiometric calibration and traceability
- [TT&C Systems](./ttac.md) — data downlink for high-volume imagery

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
