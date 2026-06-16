# Ranging and Doppler

> **Node ID**: spacecraft-systems.ttac.ranging-doppler
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.ttac`](./ttac.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ttac_systems
> **Critical**: No

Ranging and Doppler measurements provide spacecraft position and velocity for orbit determination. The ground station measures round-trip signal delay (range) and frequency shift (Doppler) to reconstruct the spacecraft trajectory. See [TT&C Systems](./ttac.md) for the integrated communications context.

## Sequential Ranging

A sequence of sinusoidal tones modulated on the uplink and coherently turned around on the downlink. Phase delay of each tone measures range:

1. Highest tone (e.g., 500 kHz) provides precision (1-3 m) but has short ambiguity distance (300 m)
2. Lower tones (100, 20, 4 kHz) resolve ambiguity sequentially up to 37.5 km
3. Ground station correlates received tones against reference to extract phase delay
4. Range accuracy: 1-3 m typical; limited by SNR, multipath, and clock stability

## Pseudo-Noise (PN) Ranging

A single PN code replaces the tone sequence, simplifying the signal:

- **CCSDS T4B code**: 1,009,471 chips at ~1 MHz clock; ambiguity 1009 km; precision 1.5 m
- **CCSDS T2B code**: 49,147 chips; faster acquisition; 1.7 m precision
- Spacecraft regenerates and turns around the PN code; ground correlator measures delay
- Advantage: single signal, better jitter performance at low SNR (deep-space)

## Doppler Measurement

The spacecraft velocity along the line of sight causes a frequency shift: Δf = f × v/c.

- X-band sensitivity: 28 Hz per m/s; Ka-band: 88 Hz per m/s
- Two-way coherent Doppler (spacecraft locked to uplink) achieves 0.03 mm/s precision at X-band
- Integration time: 10-60 seconds typical; longer integration improves precision
- Combined with range: spacecraft position to <1 m in LEO, <10 km at Mars

## Key Parameters

- **Ranging precision**: 1-3 m (sequential), 1.5-1.7 m (PN)
- **Doppler precision**: 0.03-0.1 mm/s (X-band), 0.01 mm/s (Ka-band)
- **Range ambiguity**: 37.5 km (sequential), 1009 km (T4B PN)
- **Integration time**: 10-60 s for Doppler; 1-100 s for ranging

## See Also

- [TT&C Systems](./ttac.md) — parent capability
- [RF Transponders](./ttac.rf-transponders.md) — coherent turn-around for Doppler
- [Ground Link Budget](./ttac.ground-link-budget.md) — link margin for ranging signals

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
