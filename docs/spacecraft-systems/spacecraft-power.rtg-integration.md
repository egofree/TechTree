# RTG Integration

> **Node ID**: spacecraft-systems.spacecraft-power.rtg-integration
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.spacecraft-power`](./spacecraft-power.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: spacecraft_power
> **Critical**: No

Integration of radioisotope thermal generators into the spacecraft power bus for deep-space missions where solar flux is too low for practical arrays. The RTG itself is manufactured by the [energy.radioisotope-power](../energy/radioisotope-power.md) capability — this process covers the mechanical mounting, thermal interfacing, electrical DC-DC conversion, and launch safety qualification. The MMRTG (125W BOL, ~4.8 kg Pu-238) and GPHS-RTG (300W BOL, 7.8 kg Pu-238) are the two flight-qualified designs.

## Key Parameters

| Parameter | MMRTG | GPHS-RTG |
|-----------|-------|----------|
| Electrical output (BOL) | 125W | 300W |
| Thermal output | 2,000W | 4,400W |
| Pu-238 mass | ~4.8 kg | 7.8 kg |
| System specific power | 2.8 W/kg | 5.2 W/kg |
| Degradation rate | ~1.2%/yr | ~1.2%/yr |
| Flight heritage | Curiosity, Perseverance | Voyager, Cassini, New Horizons |

## Process Overview

1. **Mechanical mounting**: Interface bracket design for RTG mass (45 kg MMRTG, 57 kg GPHS-RTG) and launch loads
2. **Thermal interface**: Heat pipe routing from RTG fins to spacecraft thermal bus; waste heat redirection
3. **Electrical integration**: MPPT DC-DC converter for RTG variable output voltage
4. **Parallel source management**: Battery buffering for peak loads above RTG continuous output
5. **Launch safety analysis**: Impact, reentry, and explosion containment verification per nuclear safety protocols
6. **Integration test**: Thermal vacuum cycling with RTG simulator, EMI verification

## Prerequisites

- Energy.radioisotope-power capability (RTG manufacturing and fuel fabrication)
- Launch vehicle nuclear safety review process (Presidential directive for U.S. launches)
- Thermal management subsystem for 2-4 kW waste heat dissipation

## See Also

- [Spacecraft Power Systems](./spacecraft-power.md) — parent capability
- [Power Management and Distribution](./spacecraft-power.power-management-distribution.md) — bus integration
- [Radioisotope Power](../energy/radioisotope-power.md) — RTG manufacturing and thermoelectric conversion

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
