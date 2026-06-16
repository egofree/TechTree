# Total Ionizing Dose Design

> **Node ID**: spacecraft-systems.radiation-hardening.tid-design
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.radiation-hardening`](./radiation-hardening.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: radhard_electronics
> **Critical**: No

Total Ionizing Dose (TID) design addresses the cumulative degradation of semiconductor parameters due to ionizing radiation over the mission lifetime. See [Radiation Hardening](./radiation-hardening.md) for the integrated radiation context.

## Mechanism

Ionizing radiation creates electron-hole pairs in the SiO₂ gate oxide of MOS transistors. Holes trapped near the Si/SiO₂ interface cause threshold voltage shift: NMOS Vth decreases, PMOS Vth increases. At sufficient dose, the transistor stops switching correctly.

1. **Hole generation**: ~8×10¹² pairs per rad(Si) per cm³ of SiO₂
2. **Hole transport**: drift to Si/SiO₂ interface (μs to seconds)
3. **Trap buildup**: permanent interface states, slow anneal at T > 100°C
4. **Threshold shift**: ΔVth = -Q_ox / C_ox
5. **Leakage increase**: field-oxide parasitic transistors turn on

## Rad-Hard Process Technologies

- **SOI (Silicon-on-Insulator)**: thin device layer on buried oxide; 100-1000× TID improvement over bulk CMOS. Used in LEON3, RAD750.
- **SOS (Silicon-on-Sapphire)**: device silicon on sapphire substrate; ultimate isolation. Legacy RH1750.
- **SiGe HBT**: inherent TID tolerance to 1-5 Mrad without hardening. RF transponders.
- **Bulk CMOS + guard rings**: annular transistors, guard bands; 30-100 krad at no cost premium.

## Dose Levels and Margins

| Orbit | Annual dose (2.5mm Al) | Design target (2× margin) |
|-------|----------------------|--------------------------|
| LEO (600 km) | 3-10 krad | 20-30 krad |
| GEO | 10-50 krad | 100-300 krad |
| Jupiter | 1,000-10,000 krad | 1-30 Mrad |

## Key Parameters

- **Failure threshold**: 10-30 krad (modern deep-submicron); 50-300 krad (0.35-0.5 μm); 1 Mrad (SOI)
- **Design margin**: 2× (standard), 3× (critical components)
- **Annealing**: partial recovery at T > 100°C; exploited in some long missions

## See Also

- [Radiation Hardening](./radiation-hardening.md) — parent capability
- [SEE Mitigation](./radiation-hardening.see-mitigation.md) — complementary SEE hardening
- [Shielding Design](./radiation-hardening.shielding-design.md) — reducing dose at component level
- [Silicon](../silicon/index.md) — semiconductor fabrication processes

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
