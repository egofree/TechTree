# Synthetic Aperture Radar

> **Node ID**: spacecraft-systems.earth-observation.sar-radar
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.earth-observation`](./earth-observation.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: eo_payloads
> **Critical**: No

Synthetic aperture radar (SAR) transmits microwave pulses and processes the coherent backscatter to produce high-resolution imagery day or night, through clouds and rain. See [Earth Observation Payloads](./earth-observation.md) for the integrated sensing context.

## Architecture

SAR synthesises a long antenna by coherently combining echoes collected along the satellite's flight path. Azimuth resolution equals half the physical antenna length (independent of range). Range resolution depends on pulse bandwidth. The radar operates in L-band (24 cm), C-band (5.6 cm), or X-band (3 cm), each offering different penetration and resolution trade-offs.

## Key Components

1. **Phased-array antenna**: 3-12 m planar array with hundreds of T/R modules for electronic beam steering
2. **Chirp generator**: linear FM modulator producing 10-100 MHz bandwidth pulses for range compression
3. **Transmitter/receiver**: TWT or solid-state amplifier, 2-6 kW peak power, low-noise receiver front-end
4. **Data downlink**: raw or partially-focused SAR data at 100-600 Mbps, often via X-band or Ka-band link

## Key Parameters

- **Frequency**: L (1.26 GHz), C (5.4 GHz), X (9.65 GHz)
- **Resolution**: 1 m (Spotlight) to 20 m (ScanSAR)
- **Swath**: 10 km (Spotlight) to 500 km (ScanSAR)
- **Antenna size**: 3 × 1 m (X-band) to 12 × 3 m (L-band)
- **Peak power**: 2-6 kW
- **Mass**: 200-800 kg

## See Also

- [Earth Observation Payloads](./earth-observation.md) — parent capability
- [Electronics](../electronics/index.md) — RF electronics and T/R modules
- [Radio Communications](../telecom/radio.md) — radar heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
