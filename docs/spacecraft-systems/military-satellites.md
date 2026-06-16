# Military Satellites

> **Node ID**: spacecraft-systems.military-satellites
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`defense`](../defense/index.md),
> [`defense.weapons`](../defense/weapons.md),
> [`optics`](../optics/index.md),
> [`silicon`](../silicon/index.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: reconnaissance_systems
> **Critical**: No — military satellites provide intelligence, warning, and space-domain awareness that no other platform can deliver. Reconnaissance imaging from orbit offers persistent, global coverage impossible from aircraft. Early-warning satellites detect missile launches within 30-60 seconds of ignition. All systems described here are based on publicly-documented, open-source specifications

Military satellites represent the oldest application of space technology — the first American military satellite (GRAB, 1960) and the first reconnaissance satellite (CORONA, 1960) predated the first weather satellite. This article covers three mission areas based entirely on publicly-documented systems: [reconnaissance imaging](./military-satellites.reconnaissance-imaging.md) for high-resolution Earth observation, [early-warning](./military-satellites.early-warning.md) for missile-launch detection (SBIRS, DSP), and [space surveillance](./military-satellites.space-surveillance.md) for tracking objects in orbit.

The [defense](../defense/index.md) domain provides the doctrinal requirements and mission architecture. [Defense weapons](../defense/weapons.md) heritage informs co-orbital and counter-space system concepts. The [optics](../optics/index.md) domain supplies large-aperture telescope mirrors and adaptive-optics systems. The [silicon](../silicon/index.md) domain provides focal-plane detector arrays (HgCdTe, InSb, silicon CCDs).

## Overview

Military satellite missions share common characteristics: they operate from specific orbits optimized for their mission, use sensors tuned to detect particular signatures, and must survive hostile environments (radiation, anti-satellite threats, jamming). The three mission areas have distinct orbital and sensor requirements:

| Mission | Primary orbit | Key sensor | Latency | Heritage |
|---------|--------------|-----------|---------|----------|
| Reconnaissance (optical) | Sun-synchronous LEO (250-1000 km) | CCD/CMOS focal plane | Hours (stored) to realtime | CORONA (1960), KH-series |
| Reconnaissance (radar) | LEO (500-800 km) | SAR antenna | Hours to realtime | Lacrosse/Onyx (1988) |
| Early warning | GEO + HEO | Infrared staring + scanning | <1 minute | DSP (1970), SBIRS (2011) |
| Space surveillance | Ground-based + LEO | Optical + radar | Hours | GEODSS, Space Fence |
| Navigation (GPS) | MEO (20,200 km) | Atomic clocks | Realtime | Navstar GPS (1978) |

## Reconnaissance Imaging

### Optical Reconnaissance

Optical reconnaissance satellites use large telescopes to image the ground at high resolution. The publicly-acknowledged resolution limit for open-source systems is approximately 10 cm ground-sample distance (GSD), though the theoretical diffraction limit for a 2.4-m aperture at 500 km altitude is ~6 cm at 550 nm wavelength (Rayleigh criterion: θ = 1.22λ/D).

| Parameter | Value | Notes |
|-----------|-------|-------|
| Aperture | 2-3 m (estimated, KH-11 class) | Hubble-sized mirrors; shared manufacturing |
| Altitude | 250-1000 km (typical 500 km) | Sun-synchronous for consistent lighting |
| Inclination | 97-98° (sun-sync) | Covers all latitudes |
| Orbital period | 90-105 min | 2-3 passes per day per target |
| GSD (best) | 10-15 cm (publicly stated) | Commercial: 25-30 cm (Maxar WorldView) |
| Focal plane | Time-delay-integration (TDI) CCD | TDI enables imaging at high ground velocity |
| Swath width | 10-50 km | Narrow for high resolution |
| Data rate | 100s of Mbps | Downlinked to relay satellites |

The diffraction-limited resolution is set by the telescope aperture and wavelength:

```
GSD = H × 1.22 × λ / D
```

Where H = altitude (m), λ = wavelength (m), D = aperture diameter (m). At H=500 km, λ=550 nm, D=2.4 m: GSD = 500,000 × 1.22 × 550×10⁻⁹ / 2.4 = 0.14 m. Atmospheric turbulence (seeing) limits ground resolution to ~5-10 cm even for perfect optics.

### TDI CCD Operation

Time-delay-integration CCDs solve the problem of imaging fast-moving ground targets from orbit. The spacecraft ground-track velocity at 500 km altitude is approximately 7 km/s. A conventional camera would smear the image unless the exposure time were extremely short (<1 ms), limiting sensitivity.

A TDI CCD has multiple rows of pixels aligned with the ground track. As the image moves across the detector, charge is transferred from row to row at exactly the rate the image moves. This effectively tracks the target, allowing long integration times:

| Parameter | Value |
|-----------|-------|
| TDI stages | 32, 64, 96, or 128 rows typical |
| Effective exposure | N_stages × single-row dwell time |
| Signal gain | Linear with N_stages (e.g., 96× for 96-stage) |
| Smear constraint | Sync error <0.5 pixel across TDI array |

### Commercial High-Resolution Imaging

Since 2000, commercial satellite imagery has approached government-class resolution:

| Operator | Satellite | GSD (pan) | GSD (multispectral) | Altitude |
|----------|-----------|-----------|---------------------|----------|
| Maxar | WorldView-3 | 0.31 m | 1.24 m | 617 km |
| Maxar | WorldView-4 | 0.31 m | 1.24 m | 617 km |
| Airbus | Pleiades Neo | 0.30 m | 1.2 m | 620 km |
| Planet | SkySat | 0.50 m | 2.0 m | 450 km |
| Planet | Dove (constellation) | 3.0 m | 3.0 m | 400-600 km |

WorldView-3's 1.1-m aperture telescope achieves 0.31 m GSD from 617 km. It also has 8-band multispectral (400-1040 nm) and 8-band SWIR (1195-2365 nm) capability for material identification and cloud-penetration.

### SAR (Synthetic Aperture Radar)

SAR provides all-weather, day-or-night imaging by illuminating the ground with microwave pulses and processing the returned echoes. SAR resolution is independent of range (unlike optical) and is determined by the synthetic aperture length:

| Parameter | Value | Notes |
|-----------|-------|-------|
| Frequency | X-band (8-12 GHz), L-band (1-2 GHz) | X: high resolution; L: foliage penetration |
| Resolution | 0.3-3 m (spotlight mode) | Independent of altitude |
| Swath width | 10-50 km (stripmap), 400 km (ScanSAR) | Trade-off with resolution |
| Polarimetry | Single, dual, quad, compact | Quad-pol enables full scattering matrix |
| Power | 1-5 kW peak transmitter | TWTA or solid-state amplifier |

SAR achieves high cross-range resolution by synthesizing a long antenna from the satellite's motion. A 10-m real antenna at X-band has a 3-dB beamwidth of ~0.7°, giving ~6 km cross-range resolution at 500 km. But by coherently integrating returns over 5 km of satellite travel, the synthetic aperture is effectively 5 km long, yielding ~1.5 m cross-range resolution.

## Early Warning

### DSP (Defense Support Program)

The Defense Support Program was the first operational satellite-based missile warning system, operational from 1970 to the 2020s. DSP satellites in geosynchronous orbit used staring infrared sensors to detect the hot exhaust plumes of ballistic missile launches.

| Parameter | Value | Notes |
|-----------|-------|-------|
| First launch | 1970 (DSP Flight 1) | Operational from 1970 |
| Orbit | Geosynchronous (GEO) | 3-satellite constellation |
| Sensor | Pseudo-linear array | 3.6 μm primary band |
| Detector | HgCdTe (mercury-cadmium-telluride) | Cooled to ~77 K (Stirling cryocooler) |
| Pixel count | ~6000 (linear array) | Scanned full-disk every 10 seconds |
| Wavelength | 2.7 μm and 4.3 μm (CO₂ band) | Dual-band for false-alarm rejection |
| Report latency | 30-60 seconds from launch ignition | Downlinked to ground stations |
| DSP-20 (final) | Launched 2007 | Last in the series |

The 4.3-micron CO₂ absorption band is used because ballistic missile exhaust contains significant CO₂, and the Earth's atmosphere is opaque at this wavelength — meaning the background (Earth) is dark at 4.3 μm, while the missile plume is bright. This provides high contrast against the background.

The 3.6-micron HgCdTe detector arrays were linear arrays of approximately 6000 elements. The sensor used a rotating Schwarzschild (f/1.4) telescope to scan the full Earth disk every 10 seconds, building a raster image line by line. Each pixel covered approximately 3×3 km on the Earth's disk from GEO distance (36,000 km).

### SBIRS (Space Based Infrared System)

SBIRS is the successor to DSP, providing faster, more sensitive missile-warning with both scanning and staring sensors in GEO orbit plus additional sensors in highly elliptical orbit (HEO) for polar coverage.

| Parameter | SBIRS GEO | SBIRS HEO | Notes |
|-----------|-----------|-----------|-------|
| Orbit | Geosynchronous | Highly elliptical | HEO covers polar regions |
| Scanning sensor | Full-disk, every ~1 second | — | Faster than DSP (10 s) |
| Staring sensor | Regional, high revisit | Regional | For tracking, not just detection |
| Wavelengths | SWIR + MWIR (multi-band) | SWIR + MWIR | Short-wave + mid-wave IR |
| Detector type | HgCdTe arrays (large format) | HgCdTe arrays | Staring focal planes (no scan) |
| Report latency | <20 seconds (estimated) | <20 seconds | Publicly stated as "seconds" |
| First launch | 2011 (GEO-1) | 2006 (HEO-1, hosted payload) | — |
| Constellation | 4 GEO + 2 HEO (planned) | — | Full operational capability |

The SBIRS scanning sensor surveys the entire field of regard in seconds, looking for new launch signatures. Once a potential threat is detected, the staring sensor is tasked to continuously track the missile through its trajectory. This two-sensor architecture enables both rapid detection (scanning) and precision tracking (staring).

The HEO sensors ride as hosted payloads on national-security satellites in Molniya-type orbits (apogee ~39,000 km, perigee ~1,000 km, 63.4° inclination), providing coverage of the North Pole region that is difficult to observe from GEO.

### Infrared Detector Technology

Early-warning sensors rely on cryogenically-cooled infrared detector arrays:

| Detector | Band | Temp | Array format | Use |
|----------|------|------|-------------|-----|
| HgCdTe (MWIR) | 3-5 μm | 77 K (Stirling) | Up to 2048×2048 | SBIRS, DSP, astronomy |
| InSb (indium antimonide) | 3-5 μm | 30-77 K | Up to 2048×2048 | Alternative MWIR |
| HgCdTe (LWIR) | 8-12 μm | 40-77 K | 640×512 | Thermal imaging |
| QWIP (quantum well) | 8-12 μm | 40-60 K | 1024×1024 | Long-wave IR research |

At 4.3 microns, a photon has energy E = hc/λ = 4.6×10⁻²⁰ J = 0.29 eV. HgCdTe with a composition tuned for 5-micron cutoff has a bandgap of ~0.25 eV at 77 K, absorbing these photons efficiently with low dark current.

## GPS Military Signals

The Navstar GPS constellation provides precision navigation and timing for military and civilian users worldwide. Military receivers use encrypted signals resistant to jamming and spoofing.

| Signal | Frequency | Modulation | Encryption | Use |
|--------|-----------|------------|------------|-----|
| C/A (civilian) | 1575.42 MHz (L1) | BPSK(1), 1.023 Mcps | None | Standard positioning |
| P(Y) (military) | 1227.60 (L2), 1575.42 (L1) | BPSK(10), 10.23 Mcps | Y-code encryption | Precision positioning |
| M-code | 1227.60 (L2), 1575.42 (L1) | BOC(10,5) split-spectrum | MNSA crypto | Next-gen military |
| L1C (civilian) | 1575.42 (L1) | TMBOC | None | GPS III civil signal |

The P(Y)-code provides 10× higher chipping rate than C/A (10.23 vs 1.023 Mcps), yielding ~10× better range precision (~30 cm vs ~3 m). The Y-code is the P-code encrypted with a secret W-key, preventing unauthorized use and signal spoofing.

M-code uses Binary Offset Carrier (BOC) modulation that splits the signal spectrum, placing power away from the center frequency. This provides:

- **Jam resistance**: signal energy spread over wider bandwidth, harder to jam
- **Separation from civil signals**: M-code and C/A coexist on L1/L2 without interference
- **Autonomous navigation**: M-code receivers can acquire signals without first locking C/A

## Space Surveillance Network (SSN)

The US Space Surveillance Network tracks objects in Earth orbit to maintain the satellite catalog, predict collisions, and warn of reentries. The catalog contains 40,000+ objects larger than 10 cm.

### GEODSS (Ground-based Electro-Optical Deep Space Surveillance)

GEODSS uses 1-meter telescopes at three sites (Diego Garcia, Maui, Socorro NM) to track deep-space objects (GEO and HEO) by reflected sunlight.

| Parameter | Value |
|-----------|-------|
| Telescope aperture | 1.0 m |
| Sites | 3 (global longitude coverage) |
| Detector | 4096×4096 CCD (back-illuminated) |
| Field of view | 1.68° × 1.68° per frame |
| Magnitude limit | 16th visual magnitude |
| Objects tracked | GEO satellites, debris >1 m |
| Operating mode | Stare-and-track, sidereal and track-rate |

### Space Fence

The Space Fence (operational 2020) is an S-band radar system on Kwajalein Atoll that detects uncued objects in LEO as they pass through its radar fence.

| Parameter | Value |
|-----------|-------|
| Frequency | S-band (2.0-2.2 GHz, ~15 cm wavelength) |
| Location | Kwajalein Atoll (2nd site planned for Australia) |
| Detection size | ~5 cm at 1000 km (estimated) |
| Coverage | ±36° azimuth fan beam |
| Catalog additions | ~10,000 new objects/year (estimated) |
| Operating mode | Uncued detection + tracking |

The shorter S-band wavelength (15 cm) compared to the legacy Air Force Space Surveillance System (VHF, 1.5 m wavelength) enables detection of much smaller debris — 5 cm vs 30 cm — dramatically increasing the tracked object count. The radar operates in a bistatic configuration with separate transmit and receive antennas, and uses phased-array technology for electronic beam steering without moving parts.

A second Space Fence site was planned for Western Australia but was not constructed. The system's S-band frequency also provides measurement of object orbital parameters to 10-meter accuracy, sufficient for precise orbit determination and conjunction assessment.

Combined with GEODSS optical tracking for deep-space objects and the Ground-based Radar Prioritized System (GRPS) for high-priority LEO targets, the SSN maintains custody of active satellites and warns operators of predicted close approaches.

### Catalog Statistics

The public satellite catalog maintained by 18th Space Defense Squadron (18 SDS, formerly JSpOC) contains objects tracked by radar and optical sensors worldwide. Two-line element sets (TLEs) are published for non-sensitive objects via Space-Track.org, enabling anyone to predict satellite passes.

| Orbit regime | Tracked objects | Size threshold |
|-------------|----------------|----------------|
| LEO (<2000 km) | ~25,000 | >10 cm |
| MEO (2000-35,786 km) | ~2,000 | >1 m |
| GEO (~35,786 km) | ~2,000 | >1 m |
| Total cataloged | ~40,000+ | Varies by altitude |
| Estimated >1 cm in LEO | ~1,000,000 | Too small to track |

The total population of orbital debris >1 cm in LEO is estimated at over one million objects, most too small to track individually but large enough to disable a satellite on impact (kinetic energy at 7 km/s: E = ½mv² = ½ × 0.01 × 7000² = 245 kJ — equivalent to 60 g of TNT).

## Strengths

- Global, persistent coverage impossible from aircraft or ground platforms
- Optical reconnaissance provides unambiguous imagery for treaty verification and intelligence
- Early-warning satellites detect missile launches within seconds, enabling response time
- Space surveillance prevents catastrophic collisions and tracks orbital debris
- Commercial imagery (Maxar, Planet) provides dual-use capability and open-data transparency
- All technologies described are based on publicly-documented specifications from open-source references

## Weaknesses

- Satellites in predictable orbits are vulnerable to anti-satellite (ASAT) systems
- Reconnaissance satellites have revisit times of hours to days — not continuous monitoring
- Cloud cover defeats optical imaging (SAR addresses this but at lower resolution)
- Infrared sensors require cryogenic cooling with limited cryocooler lifetime (5-10 years)
- Space debris population is growing, increasing collision risk for all satellites
- Missile-warning false alarms remain a concern — DSP historically had background clutter issues from forest fires and reflections

## See Also

- [Reconnaissance Imaging](./military-satellites.reconnaissance-imaging.md) — optical and SAR satellites
- [Early Warning](./military-satellites.early-warning.md) — SBIRS, DSP, infrared sensors
- [Space Surveillance](./military-satellites.space-surveillance.md) — SSN, GEODSS, Space Fence
- [Defense](../defense/index.md) — defense domain doctrine and requirements
- [Defense Weapons](../defense/weapons.md) — weapons heritage and counter-space concepts
- [Optics](../optics/index.md) — telescope mirrors and optical design
- [Silicon](../silicon/index.md) — detector arrays and focal planes
- [TT&C Systems](./ttac.md) — spacecraft communications for data downlink
- [Radiation Hardening](./radiation-hardening.md) — spacecraft electronics protection

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
