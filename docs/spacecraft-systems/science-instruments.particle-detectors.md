# Particle Detectors

> **Node ID**: spacecraft-systems.science-instruments.particle-detectors
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.science-instruments`](./science-instruments.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: science_payloads
> **Critical**: No

Particle detectors measure energetic charged particles (electrons, protons, alpha particles, heavy ions) and, indirectly, neutral particles (neutrons, gamma rays) in the space environment. See [Science Instruments](./science-instruments.md) for the full instrument context.

## Detector Types

1. **Solid-state silicon detectors (SSD)**: reverse-biased silicon diodes; each charged particle deposits energy proportional to dE/dx, enabling energy spectroscopy. Heritage from Van Allen Probes, Solar Orbiter.
2. **Proportional counters**: gas-filled tubes where particles ionize gas; pulse height proportional to deposited energy. Used on Chandra X-ray Observatory (proportional counter array).
3. **Microchannel plates (MCP)**: detect UV photons and low-energy charged particles via secondary electron multiplication (gain ~10⁶). Used in time-of-flight systems.
4. **Time-of-flight (TOF)**: measures particle velocity by timing flight between two thin foils; combined with energy measurement yields particle mass. Heritage from Cassini INMS, MAVEN STATIC.
5. **Semiconductor pixel/strip detectors**: position-sensitive silicon arrays tracking individual particle trajectories. AMS-02 on the ISS uses a 7-layer silicon tracker.

## Key Parameters

- **Energy range**: 1 keV to 100s of MeV (varies by detector type)
- **Energy resolution**: ΔE/E ~5-10% for solid-state; ~20% for proportional counters
- **Geometric factor**: effective aperture × solid angle (cm²·sr), determines counting rate
- **Time resolution**: 1-100 ms typical for space plasma measurements

## See Also

- [Science Instruments](./science-instruments.md) — parent capability
- [Spectrometers](./science-instruments.spectrometers.md) — electromagnetic spectrum analysis
- [Silicon](../silicon/index.md) — detector substrate material
- [Electronics](../electronics/index.md) — charge-sensitive preamplifier readout

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
