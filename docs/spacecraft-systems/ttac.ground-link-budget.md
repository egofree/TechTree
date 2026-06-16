# Ground Link Budget

> **Node ID**: spacecraft-systems.ttac.ground-link-budget
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.ttac`](./ttac.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: ttac_systems
> **Critical**: No

The ground link budget is the accounting of all gains and losses in the RF path between the spacecraft and ground station. It determines whether the link closes at the required data rate and bit error rate. See [TT&C Systems](./ttac.md) for the integrated communications context.

## Link Budget Equation

The fundamental equation for received bit energy-to-noise-density ratio:

```
Eb/N0 = EIRP + Gr - L_path - L_pointing - L_atmos - L_impl 
        - 10log(k) - 10log(Tsys) - 10log(Rb) + G_coding
```

## Budget Components

1. **EIRP** (Effective Isotropic Radiated Power): Tx power + Tx antenna gain - circuit loss. Typical spacecraft: 10-50 dBW.
2. **Path loss**: free-space spreading loss: L = 20log(4πR/λ). At X-band (8.4 GHz) and Mars distance (375M km): -272 dB.
3. **G/T** (figure of merit): ground antenna gain minus system noise temperature. DSN 70-m: 51 dB/K at X-band.
4. **Atmospheric loss**: rain fade (0.5-20 dB depending on band and weather), oxygen/water vapor absorption.
5. **Pointing loss**: spacecraft and ground antenna misalignment; 1° at X-band costs ~1 dB.
6. **Implementation loss**: hardware imperfections (phase noise, quantization, filter mismatch): 1-2 dB.
7. **Coding gain**: convolutional (5-7 dB), concatenated RS+convolutional (8-10 dB), Turbo/LDPC (8-10 dB at lower rates).

## Margin Requirements

- **Minimum margin**: 3 dB for nominal operations
- **Critical link margin**: 6 dB for safe-mode commanding
- **Weather margin**: 3-6 dB at Ka-band for rain fade (site diversity as backup)
- **End-of-life margin**: account for TWTA degradation (1-2 dB over mission lifetime)

## DSN Ground Stations

| Station | Dish | G/T (X-band) | Tx power |
|---------|------|-------------|----------|
| DSS-14/43/63 | 70-m | 51 dB/K | 20 kW |
| DSS-34/54/65 | 34-m BWG | 46 dB/K | 20 kW |

## See Also

- [TT&C Systems](./ttac.md) — parent capability
- [RF Transponders](./ttac.rf-transponders.md) — spacecraft-side EIRP contribution
- [Telemetry Formatting](./ttac.tm-formatting.md) — coding gain from CCSDS codes

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
