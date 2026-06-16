# Atomic Clocks

> **Node ID**: spacecraft-systems.navigation-payload.atomic-clocks
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.navigation-payload`](./navigation-payload.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: pnt_payloads
> **Critical**: No

Atomic clocks are the heart of every GNSS satellite. They provide the ultra-stable frequency reference from which all navigation signals are derived. See [Navigation & PNT Payloads](./navigation-payload.md) for the integrated navigation context.

## Architecture

Three clock technologies dominate GNSS: **rubidium** (compact, reliable, the workhorse), **caesium** (primary frequency standard, shorter life), and **hydrogen maser** (best stability, highest mass and power). Each satellite carries 2-4 clocks for redundancy, and the ground segment selects the best performer.

## Clock Types

1. **Rubidium (RAFS)**: vapour cell at 6.835 GHz, lamp-pumped optical pumping, 1×10⁻¹³/day stability, 3-5 kg, 15-30 W
2. **Caesium**: atomic beam at 9.193 GHz, magnetic state selection, primary SI second definition, 12 kg, 30 W
3. **Passive hydrogen maser**: hydrogen storage bulb at 1.420 GHz, 1×10⁻¹⁴/day stability, 18 kg, 60 W
4. **Active hydrogen maser**: self-sustaining microwave oscillation, 2×10⁻¹⁴/day, 20 kg, 70 W

## Key Parameters

- **Output frequency**: 10.23 MHz (GPS), 10.0 MHz (Galileo)
- **Allan deviation**: 1×10⁻¹² (Rb @1s) to 3×10⁻¹³ (PHM @1s)
- **Daily drift**: 5×10⁻¹⁴ (Galileo RAFS) to 2×10⁻¹⁴ (PHM)
- **Temperature sensitivity**: 1×10⁻¹³/°C
- **Magnetic sensitivity**: 1×10⁻¹³/Gauss
- **Lifetime**: 8-12+ years

## See Also

- [Navigation & PNT Payloads](./navigation-payload.md) — parent capability
- [Measurement](../measurement/index.md) — horology and precision timing
- [Electronics](../electronics/index.md) — frequency synthesis electronics

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
