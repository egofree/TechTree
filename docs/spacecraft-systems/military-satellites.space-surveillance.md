# Space Surveillance

> **Node ID**: spacecraft-systems.military-satellites.space-surveillance
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.military-satellites`](./military-satellites.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: reconnaissance_systems
> **Critical**: No

Space surveillance networks detect, track, and catalog objects in Earth orbit — active satellites, spent rocket bodies, and orbital debris. See [Military Satellites](./military-satellites.md) for the full mission context. All specifications below are from publicly-documented sources.

## GEODSS (Ground-based Electro-Optical Deep Space Surveillance)

GEODSS uses 1.0-m telescopes at three sites (Diego Garcia, Maui, Socorro NM) to track deep-space objects (GEO and HEO) by reflected sunlight. Each site covers 120° of longitude, providing near-global coverage. Detector: 4096×4096 back-illuminated CCD with 1.68°×1.68° field of view. Magnitude limit: 16th visual magnitude — sufficient to track 1-m objects at GEO distance (36,000 km).

## Space Fence

The Space Fence (operational 2020) is an S-band (2.0-2.2 GHz, 15-cm wavelength) phased-array radar on Kwajalein Atoll that detects uncued objects in LEO as they pass through its ±36° azimuth fan beam. Detection threshold: ~5 cm at 1000 km altitude. The shorter S-band wavelength (vs the legacy VHF system's 1.5 m) enables tracking of much smaller debris, adding ~10,000 new objects per year to the catalog.

## Catalog Statistics

The public satellite catalog (maintained by 18th Space Defense Squadron, published via Space-Track.org) contains 40,000+ tracked objects:

- **LEO (<2000 km)**: ~25,000 objects >10 cm
- **MEO**: ~2,000 objects >1 m
- **GEO**: ~2,000 objects >1 m
- **Estimated >1 cm in LEO**: ~1,000,000 (too small to track)

A 1-cm object impacting at 7 km/s carries 245 kJ of kinetic energy — enough to disable a satellite. Collision avoidance maneuvers are executed when predicted miss distance falls below warning thresholds.

## Key Parameters

- **Optical aperture**: 1.0 m (GEODSS)
- **Radar wavelength**: 15 cm (Space Fence, S-band)
- **Detection size**: 5 cm at 1000 km (Space Fence); 1 m at GEO (GEODSS)
- **Catalog size**: 40,000+ tracked objects
- **Tracking accuracy**: 10-100 m position (varies by object and sensor)

## See Also

- [Military Satellites](./military-satellites.md) — parent capability
- [Optics](../optics/index.md) — telescope design for GEODSS
- [Silicon](../silicon/index.md) — CCD arrays for optical tracking
- [TT&C Systems](./ttac.md) — satellite tracking infrastructure

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
