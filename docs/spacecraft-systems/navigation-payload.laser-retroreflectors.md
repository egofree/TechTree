# Laser Retroreflectors

> **Node ID**: spacecraft-systems.navigation-payload.laser-retroreflectors
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.navigation-payload`](./navigation-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: pnt_payloads
> **Critical**: No

Laser retroreflector arrays (LRA) are passive panels of corner-cube prisms that reflect laser pulses back to ground-based satellite laser ranging (SLR) stations, enabling millimetre-level orbit determination. See [Navigation & PNT Payloads](./navigation-payload.md) for the integrated navigation context.

## Architecture

Each retroreflector is a **corner cube** — a triangular prism cut from fused silica with three mutually perpendicular reflecting faces. Light entering the cube reflects off each face once and exits parallel to the incoming beam, regardless of incidence angle (within ±15°). An array of 30-90 cubes is mounted on the satellite's Earth-facing panel with known position relative to the centre of mass.

## Key Components

1. **Corner cubes**: fused silica, 25-40 mm aperture, λ/10 surface figure, protected aluminium coating on back faces
2. **Mounting panel**: invar or CFRP base with thermally controlled cube seats, maintaining co-alignment over ±50°C
3. **Baffle**: optional sun shade to reduce stray light heating of the cubes

## Key Parameters

- **Number of cubes**: 30 (GPS III) to 90 (Galileo)
- **Cube aperture**: 25-40 mm diameter
- **Reflection efficiency**: >80% over field of view
- **Field of view**: ±15° half-angle
- **Return signal**: ~10⁶ photons/sr at 1000 km (532 nm, 100 mJ pulse)
- **Mass**: 1-3 kg (passive, no power)
- **SLR accuracy**: 5-15 mm range precision

## See Also

- [Navigation & PNT Payloads](./navigation-payload.md) — parent capability
- [Optics](../optics/index.md) — corner-cube prism manufacturing and alignment
- [Measurement](../measurement/index.md) — precision ranging and orbit determination

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
