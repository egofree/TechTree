# Radiation Shielding Design

> **Node ID**: spacecraft-systems.radiation-hardening.shielding-design
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.radiation-hardening`](./radiation-hardening.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: radhard_electronics
> **Critical**: No

Radiation shielding design reduces the particle flux reaching spacecraft electronics by interposing mass between the radiation environment and sensitive components. The primary material is the spacecraft's own aluminum structure, supplemented by localized spot shielding for critical parts. See [Radiation Hardening](./radiation-hardening.md) for the integrated radiation context.

## Aluminum Equivalent Shielding

Spacecraft electronics are housed inside aluminum walls of varying thickness:

| Shielding (mm Al) | LEO dose/yr | GEO dose/yr |
|-------------------|-------------|-------------|
| 1 mm | 10-30 krad | 100-500 krad |
| 2.5 mm | 3-10 krad | 30-100 krad |
| 5 mm | 1-5 krad | 10-50 krad |
| 10 mm | 0.5-2 krad | 5-20 krad |

## Dose-Depth Curves

The dose-depth curve plots total dose vs. shielding thickness for a given orbit. Key features:

1. **Steep falloff**: at low thickness (1-3 mm), adding material dramatically reduces proton dose
2. **Knee**: 3-8 mm Al, where diminishing returns set in (protons mostly stopped)
3. **Bremsstrahlung limit**: electrons hitting high-Z material produce secondary X-rays; aluminum (low-Z) minimizes this
4. **Power law**: dose ∝ t^(-n) where n ≈ 1-2 below the knee, flattening above

## Spot Shielding

For specific sensitive components, localized high-density shielding supplements the structural aluminum:

- **Tantalum dome**: 2-5 mm Ta over processor package (density 16.6 g/cm³, 2× Al effectiveness)
- **Tungsten inserts**: 1-2 mm W in critical bays (density 19.3 g/cm³)
- **Graded-Z**: layering low-Z (outer Al) → mid-Z → high-Z (inner Ta) minimizes secondary radiation
- **Mass cost**: 50-500 g per component

## Design Trade-offs

- **Mass vs. dose**: doubling shielding doubles mass; diminishing returns past the knee
- **GCR immunity**: galactic cosmic rays cannot be practically shielded (10 cm Al barely attenuates)
- **SPE protection**: 5-10 mm Al provides adequate shielding for most solar particle events
- **Electron vs. proton**: electrons produce bremsstrahlung in high-Z; protons are best stopped by low-Z

## Key Parameters

- **Standard wall thickness**: 2-4 mm Al (outer), 1-3 mm (internal bays)
- **Spot shield thickness**: 5-10 mm Al equivalent on critical components
- **Dose reduction**: 10-20× at 10 mm vs. unshielded (LEO); limited by bremsstrahlung floor

## See Also

- [Radiation Hardening](./radiation-hardening.md) — parent capability
- [TID Design](./radiation-hardening.tid-design.md) — designing components for residual dose
- [SEE Mitigation](./radiation-hardening.see-mitigation.md) — mitigating particles that penetrate shielding
- [Radiation Safety](../ehs/radiation-safety.md) — radiation environment knowledge

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
