# Reconnaissance Imaging

> **Node ID**: spacecraft-systems.military-satellites.reconnaissance-imaging
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.military-satellites`](./military-satellites.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: reconnaissance_systems
> **Critical**: No

Reconnaissance imaging satellites provide high-resolution Earth observation for intelligence, mapping, and disaster response. See [Military Satellites](./military-satellites.md) for the full mission context. All specifications below are from publicly-documented sources.

## Optical Imaging

Optical reconnaissance satellites use large-aperture telescopes (2-3 m estimated) in sun-synchronous LEO (250-1000 km). Ground-sample distance (GSD) is set by diffraction: GSD = H × 1.22 × λ / D. At 500 km, 550 nm, and D=2.4 m, the theoretical limit is ~14 cm. Commercial systems (Maxar WorldView-3) achieve 31 cm GSD from a 1.1-m aperture at 617 km.

### TDI CCD Focal Planes

Time-delay-integration (TDI) CCDs track the moving ground image by transferring charge row-to-row at the ground-track velocity (7 km/s at 500 km). A 96-stage TDI array effectively integrates for 96× the single-row dwell time, enabling high signal-to-noise at the short pixel dwell times imposed by orbital motion.

## SAR Imaging

Synthetic aperture radar (SAR) provides all-weather imaging by illuminating the ground with microwave pulses (X-band 8-12 GHz or L-band 1-2 GHz). Cross-range resolution is set by synthetic aperture length, not range: a 5-km synthetic aperture yields ~1.5 m resolution independent of altitude. Resolution: 0.3-3 m in spotlight mode.

## Key Parameters

- **Optical GSD**: 10-30 cm (government); 31-50 cm (commercial)
- **SAR resolution**: 0.3-3 m (spotlight); 10-50 km swath (stripmap)
- **Orbit**: sun-synchronous, 97-98° inclination, 90-105 min period
- **Revisit time**: 2-3 passes/day per target from single satellite
- **Data downlink**: 100s of Mbps via relay satellite or direct downlink

## See Also

- [Military Satellites](./military-satellites.md) — parent capability
- [Optics](../optics/index.md) — telescope mirrors and optical design
- [Silicon](../silicon/index.md) — TDI CCD and focal-plane arrays
- [Early Warning](./military-satellites.early-warning.md) — infrared sensing

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
