# Magnetometers

> **Node ID**: spacecraft-systems.science-instruments.magnetometers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.science-instruments`](./science-instruments.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: science_payloads
> **Critical**: No

Spaceborne magnetometers measure magnetic field strength and direction, enabling mapping of planetary magnetospheres, the interplanetary magnetic field, and crustal magnetic anomalies. See [Science Instruments](./science-instruments.md) for the full instrument context.

## Types

1. **Fluxgate magnetometer**: measures DC to ~10 Hz vector fields using a saturable core driven through its B-H hysteresis loop. Precision: ~1 pT (10⁻¹² T). Used on every planetary mission (Voyager, Cassini, MAVEN, Juno). Typical range: ±65,000 nT (covers Earth's surface field) to ±1000 nT (interplanetary).
2. **Search-coil (induction) magnetometer**: measures AC field variations (1 Hz to 100 kHz) via Faraday induction in a solenoid coil. Sensitivity: ~1 pT/√Hz at 10 Hz. Used for plasma-wave studies on Cluster, MMS.
3. **Scalar magnetometer (optically pumped)**: measures total field magnitude (no direction) using Zeeman splitting in helium or alkali-metal vapor. Absolute accuracy: ~0.1 nT. Used on Swarm, Ørsted, CHAMP for geomagnetic mapping.
4. **Overhauser magnetometer**: proton precession in a paramagnetic solution; absolute accuracy ~0.1 nT. Heritage from Oersted satellite.

## Key Parameters

- **Dynamic range**: 0.1 nT to 100,000 nT (interplanetary to planetary surface)
- **Resolution**: 1-10 pT for fluxgate; 0.1 nT absolute for scalar
- **Sample rate**: 1-128 vectors/s typical
- **Boom deployment**: 3-11 m boom to escape spacecraft magnetic interference (Juno: 11 m)

## See Also

- [Science Instruments](./science-instruments.md) — parent capability
- [Electronics](../electronics/index.md) — low-noise readout electronics
- [Silicon](../silicon/index.md) — signal processing electronics

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
