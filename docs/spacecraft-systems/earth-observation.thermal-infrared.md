# Thermal Infrared Sensors

> **Node ID**: spacecraft-systems.earth-observation.thermal-infrared
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.earth-observation`](./earth-observation.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: eo_payloads
> **Critical**: No

Thermal infrared (TIR) sensors detect radiation emitted by the Earth's surface at mid-wave (3-5 μm) and long-wave (8-12 μm) infrared wavelengths, measuring surface temperature, active fires, volcanic activity, and urban heat. See [Earth Observation Payloads](./earth-observation.md) for the integrated sensing context.

## Architecture

TIR sensors use either **microbolometer arrays** (uncooled, lower sensitivity) or **photovoltaic detector arrays** (cooled with cryocoolers, high sensitivity). Landsat TIRS and VIIRS use cooled HgCdTe or QWIP detectors. The optics must be entirely reflective (mirrors) or use specialised infrared-transmitting materials (germanium, zinc selenide) since ordinary glass is opaque beyond 2.5 μm.

## Key Components

1. **Telescope**: all-reflective design (mirrors), athermalised over orbital temperature swing
2. **Detector array**: HgCdTe, QWIP, or microbolometer, 640×512 to 2000×2000 pixels
3. **Cryocooler**: Stirling-cycle cooler for MWIR/LWIR detectors, 0.1-2 W at 40-80 K
4. **Blackbody calibrator**: onboard reference for radiometric calibration, viewed between Earth scenes

## Key Parameters

- **Wavelength**: 3-5 μm (MWIR), 8-12 μm (LWIR)
- **GSD**: 30 m (Landsat TIRS) to 375 m (VIIRS)
- **NEΔT**: 0.05-0.5 K (noise-equivalent temperature difference)
- **Accuracy**: ±0.5-1.0 K (surface temperature)
- **Detector temperature**: 40-100 K (cooled) or 300 K (microbolometer)
- **Mass**: 20-100 kg
- **Power**: 30-150 W (including cryocooler)

## See Also

- [Earth Observation Payloads](./earth-observation.md) — parent capability
- [Measurement](../measurement/index.md) — radiometric calibration and blackbody references
- [Silicon](../silicon/index.md) — infrared detector fabrication

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
