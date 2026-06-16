# Optical Imagers

> **Node ID**: spacecraft-systems.earth-observation.optical-imagers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.earth-observation`](./earth-observation.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: eo_payloads
> **Critical**: No

Optical imagers capture reflected sunlight (visible and near-infrared) to produce high-resolution panchromatic and multispectral imagery of the Earth's surface. See [Earth Observation Payloads](./earth-observation.md) for the integrated sensing context.

## Architecture

Modern high-resolution imagers use a **pushbroom** architecture: a linear or 2D detector array stares downward as the spacecraft orbits, sweeping a strip of ground. Each pixel integrates for milliseconds before readout. The telescope is typically an off-axis three-mirror anastigmat (TMA) or Ritchey-Chrétien design with sub-metre aperture.

## Key Components

1. **Telescope**: 0.3-1.5 m aperture, ULE glass mirrors, λ/40 surface figure, stable against thermal distortion
2. **Detector array**: CCD or CMOS, 10K-35K pixel linear (stitched), 8-10 μm pitch, 70-85% quantum efficiency
3. **Band-select optics**: filters or dichroic beamsplitters separate panchromatic, multispectral, and SWIR bands onto separate arrays
4. **Readout electronics**: low-noise ADCs (14-16 bit), correlated double sampling, 5-60 MPix/s throughput

## Key Parameters

- **GSD**: 0.3 m (WorldView-4) to 30 m (Landsat)
- **Swath**: 13 km (WorldView) to 290 km (Sentinel-2)
- **Bands**: 1 (pan) to 29 (WorldView-3) across VIS/NIR/SWIR
- **Telescope aperture**: 0.3-1.5 m
- **Mass**: 100-500 kg for high-resolution systems
- **Power**: 100-600 W

## See Also

- [Earth Observation Payloads](./earth-observation.md) — parent capability
- [Optics](../optics/index.md) — telescope mirror manufacturing
- [Silicon](../silicon/index.md) — CCD and CMOS detector fabrication

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
