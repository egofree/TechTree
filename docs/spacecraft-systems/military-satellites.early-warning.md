# Early Warning

> **Node ID**: spacecraft-systems.military-satellites.early-warning
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.military-satellites`](./military-satellites.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: reconnaissance_systems
> **Critical**: No

Early-warning satellites detect ballistic missile launches via their thermal plume signatures in the infrared. See [Military Satellites](./military-satellites.md) for the full mission context. All specifications below are from publicly-documented sources.

## DSP (Defense Support Program)

Operational from 1970, DSP satellites in geosynchronous orbit used a rotating Schwarzschild telescope with a linear HgCdTe detector array (~6000 elements) to scan the full Earth disk every 10 seconds. The primary detection band is 4.3 microns — the CO₂ absorption band — where missile exhaust is bright against a dark Earth background. Report latency: 30-60 seconds from launch ignition.

## SBIRS (Space Based Infrared System)

SBIRS (operational from 2011) provides faster detection with both scanning (full-disk in ~1 second) and staring sensors (regional tracking) in GEO, plus hosted payloads in highly elliptical orbit (HEO) for polar coverage. Multi-band SWIR and MWIR HgCdTe detector arrays enable detection and tracking through boost, post-boost, and midcourse phases.

## Infrared Detector Technology

| Detector | Band | Operating temp | Use |
|----------|------|---------------|-----|
| HgCdTe (MWIR) | 3-5 μm | 77 K (Stirling cryocooler) | Primary early-warning sensor |
| InSb | 3-5 μm | 30-77 K | Alternative MWIR detector |
| QWIP | 8-12 μm | 40-60 K | Long-wave IR research |

At 4.3 microns, photon energy is 0.29 eV. HgCdTe with a ~5-micron cutoff bandgap (~0.25 eV at 77 K) absorbs these photons efficiently. Cryogenic cooling to 77 K (via Stirling-cycle cryocoolers) is essential to suppress thermally-generated dark current to usable levels.

## Key Parameters

- **Detection wavelength**: 2.7 μm and 4.3 μm (CO₂ band) primary bands
- **Scan revisit**: 10 seconds (DSP); ~1 second (SBIRS scanning)
- **Report latency**: 30-60 s (DSP); seconds (SBIRS)
- **Constellation**: 3 GEO (DSP); 4 GEO + 2 HEO (SBIRS)

## See Also

- [Military Satellites](./military-satellites.md) — parent capability
- [Silicon](../silicon/index.md) — detector arrays and readout electronics
- [Reconnaissance Imaging](./military-satellites.reconnaissance-imaging.md) — optical and SAR systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
