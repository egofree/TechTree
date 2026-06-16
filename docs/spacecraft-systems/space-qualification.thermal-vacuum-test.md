# Thermal-Vacuum Test

> **Node ID**: spacecraft-systems.space-qualification.thermal-vacuum-test
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.space-qualification`](./space-qualification.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: qualified_hardware
> **Critical**: No

Thermal-vacuum (TVAC) testing simulates the combined effects of vacuum and the extreme thermal environment of space. Spacecraft hardware is cycled between hot and cold plateaus (typically −170°C to +120°C) at vacuum below 1×10⁻⁵ torr, with survival soaks at extremes beyond the predicted flight environment. TVAC exposes outgassing, thermal-structural failures, cold-welding, and electronic drift that no other test can detect. See [Space Qualification](./space-qualification.md) for the full test level philosophy.

## Overview

A TVAC chamber consists of a vacuum vessel, liquid-nitrogen-cooled thermal shrouds (for cold bias), and infrared quartz lamps (for hot heating). The test article is mounted on a thermal plate for conductive coupling. A standard qualification test runs 8–14 thermal cycles between hot and cold plateaus, with 4–8 hour dwells at each extreme for thermal equilibrium. Functional tests are performed at each plateau to verify operation across the full temperature range.

## Key Parameters

| Parameter | Qualification | Acceptance | Notes |
|-----------|--------------|-----------|-------|
| Vacuum level | <1×10⁻⁵ torr | <1×10⁻⁵ torr | High vacuum regime |
| Hot plateau | Flight max + 10°C | Flight max | Thermal margin |
| Cold plateau | Flight min − 10°C | Flight min | Thermal margin |
| Number of cycles | 8–14 | 4–8 | Cycle count margin |
| Dwell time per plateau | 4–8 hours | 4–6 hours | Thermal equilibrium |

## Prerequisites

- Vacuum chamber infrastructure ([vacuum](../vacuum/))
- Cleanroom AI&T environment ([cleanrooms](../cleanrooms/))
- Test standards and instrumentation ([quality-control](../quality-control/))

## See Also

- [Space Qualification](./space-qualification.md) — parent capability
- [Vibration & Acoustic Test](./space-qualification.vibration-acoustic-test.md) — launch environment
- [EMC Test](./space-qualification.emc-test.md) — electromagnetic compatibility

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
