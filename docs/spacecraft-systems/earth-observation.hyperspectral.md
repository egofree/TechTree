# Hyperspectral Imagers

> **Node ID**: spacecraft-systems.earth-observation.hyperspectral
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.earth-observation`](./earth-observation.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: eo_payloads
> **Critical**: No

Hyperspectral imagers capture hundreds of contiguous, narrow spectral bands (typically 5-10 nm wide) across the visible, near-infrared, and shortwave infrared spectrum, enabling material identification by spectral fingerprint. See [Earth Observation Payloads](./earth-observation.md) for the integrated sensing context.

## Architecture

A hyperspectral imager uses an **imaging spectrometer**: a telescope feeds light through a slit onto a diffraction grating or prism, which disperses the spectrum onto a 2D detector. One axis of the detector is spatial (across-track), the other is spectral (wavelength). Each ground pixel yields a full reflectance spectrum — a "data cube" with hundreds of layers.

## Key Components

1. **Telescope**: compact reflecting design feeding the spectrometer slit
2. **Spectrometer**: Offner or Dyson design with grating or prism, 0.4-2.5 μm range, 5-10 nm resolution
3. **2D detector array**: HgCdTe or InGaAs, 640×512 to 2048×2048 pixels, cooled to 100-150 K
4. **Cryocooler**: Stirling or pulse-tube cooler for SWIR detector, 0.5-2 W cooling at 77 K

## Key Parameters

- **Spectral range**: 400-2500 nm (VIS/NIR/SWIR)
- **Spectral bands**: 100-400 contiguous bands
- **Spectral resolution**: 5-10 nm (FWHM)
- **GSD**: 20-30 m typical (from 600 km orbit)
- **Swath**: 7-30 km
- **Mass**: 50-200 kg
- **Power**: 50-200 W (including cryocooler)

## See Also

- [Earth Observation Payloads](./earth-observation.md) — parent capability
- [Optics](../optics/index.md) — spectrometer grating and prism manufacturing
- [Silicon](../silicon/index.md) — HgCdTe and InGaAs detector arrays

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
