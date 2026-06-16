# EMC Test

> **Node ID**: spacecraft-systems.space-qualification.emc-test
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.space-qualification`](./space-qualification.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: emc_test_reports
> **Critical**: No

Electromagnetic compatibility (EMC) testing verifies that the spacecraft's electronics do not interfere with each other or with the launch vehicle, and that the spacecraft can tolerate external electromagnetic threats. The governing standard is MIL-STD-461, which defines conducted emissions (CE102), radiated emissions (RE102), conducted susceptibility (CS101, CS114), and radiated susceptibility (RS103) test methods covering 10 kHz to 40 GHz. See [Space Qualification](./space-qualification.md) for the full MIL-STD-461 test method reference.

## Overview

EMC testing requires a screened room (Faraday cage providing >80 dB isolation from ambient electromagnetic noise), Line Impedance Stabilisation Networks (LISNs) for conducted emission measurements, and an anechoic chamber with calibrated field generation for radiated susceptibility. The test article is powered through the LISNs, and emissions are measured with a spectrum analyser or EMI receiver. Susceptibility is tested by irradiating the article with a known field strength and monitoring for functional anomalies.

## Key Parameters

| Test | Method | Frequency | Limit / Level |
|------|--------|-----------|--------------|
| CE102 | Conducted emissions (power) | 10 kHz–10 MHz | 60–94 dBμV |
| CS101 | Conducted susceptibility (power) | 30 Hz–150 kHz | 2–7 Vrms |
| CS114 | Conducted susceptibility (cable) | 10 kHz–200 MHz | 40–109 dBμA |
| RE102 | Radiated emissions | 10 kHz–18 GHz | 24–70 dBμV/m |
| RS103 | Radiated susceptibility | 2 MHz–40 GHz | 5–200 V/m |

## Prerequisites

- EMC test instrumentation and receivers ([electronics](../electronics/))
- Screened room / anechoic chamber construction ([cleanrooms](../cleanrooms/))
- MIL-STD-461 test procedures ([quality-control](../quality-control/))

## See Also

- [Space Qualification](./space-qualification.md) — parent capability
- [Thermal-Vacuum Test](./space-qualification.thermal-vacuum-test.md) — orbital thermal environment
- [Vibration & Acoustic Test](./space-qualification.vibration-acoustic-test.md) — launch environment

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
