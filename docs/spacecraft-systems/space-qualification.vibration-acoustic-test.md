# Vibration & Acoustic Test

> **Node ID**: spacecraft-systems.space-qualification.vibration-acoustic-test
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.space-qualification`](./space-qualification.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: qualification_test_reports
> **Critical**: No

Vibration and acoustic testing simulates the launch vehicle environment — random vibration from engine combustion (14.1 G rms Qualification, 9.5 G rms Acceptance), acoustic noise from rocket exhaust (146 dB OASPL), sine sweep for low-frequency structural modes, and pyrotechnic shock from stage separation. These tests verify that the spacecraft structure, electronics, and mechanisms survive the most mechanically severe phase of the mission. See [Space Qualification](./space-qualification.md) for full test level comparison.

## Overview

Random vibration testing uses an electromagnetic shaker table to apply a launch-vehicle-specific PSD profile across 20–2000 Hz for 2–3 minutes per axis (3 axes). Acoustic testing uses a reverberant chamber with high-powered horn arrays to apply the launch acoustic spectrum for 2–3 minutes. Sine vibration testing sweeps 5–100 Hz at 2–4 octaves/min to excite structural resonances. Pyrotechnic shock testing uses explosive bolts or a tuned shock machine to simulate stage separation transients.

## Key Parameters

| Test Type | Qualification | Acceptance | Frequency | Duration |
|-----------|--------------|-----------|-----------|----------|
| Random vibration | 14.1 G rms | 9.5 G rms | 20–2000 Hz | 2–3 min/axis |
| Sine vibration | 1.25× MEFL | 1.0× MEFL | 5–100 Hz | 2–4 oct/min |
| Acoustic | 146 dB OASPL | 142.5 dB OASPL | 31.5–10k Hz | 2–3 min |
| Pyrotechnic shock | 1500 g at 1 kHz | 1000 g at 1 kHz | 100–10k Hz | Near-field |

## Prerequisites

- Shaker table and instrumentation ([electronics](../electronics/))
- Cleanroom test environment ([cleanrooms](../cleanrooms/))
- Test standards MIL-STD-1540 / ECSS-E-ST-10-03 ([quality-control](../quality-control/))

## See Also

- [Space Qualification](./space-qualification.md) — parent capability
- [Thermal-Vacuum Test](./space-qualification.thermal-vacuum-test.md) — orbital thermal environment
- [EMC Test](./space-qualification.emc-test.md) — electromagnetic compatibility

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
