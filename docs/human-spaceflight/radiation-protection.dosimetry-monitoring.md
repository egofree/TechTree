# Dosimetry & Monitoring

> **Node ID**: human-spaceflight.radiation-protection.dosimetry-monitoring
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.radiation-protection`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: radiation_protection
> **Critical**: No

Dosimetry and monitoring is the layered system of active and passive radiation detectors that measure crew dose as it accumulates. Passive detectors provide the dose-of-record: OSLiD (optically stimulated luminescent dosimeters) for total photon and charged particle dose, and CR-39 plastic nuclear track detectors (PNTD) for high-LET heavy ion and neutron spectroscopy. Active detectors provide real-time data: tissue-equivalent proportional counters (TEPC) for dose equivalent rate, and charged particle directional spectrometers for spatial dose mapping. Each crew member wears a personal dosimeter suite, and the ISS has six fixed area monitors across its modules.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| OSLiD sensitivity | 10 µSv - 10 Sv | Landauer InLight spec |
| CR-39 LET range | 5-1,000 keV/µm | Track-etch method |
| TEPC energy range | 0.3-1,000 keV/µm | Far West Technology |
| Personal dosimeter readout | Weekly + post-flight | Dose-of-record chain |
| Area monitors on ISS | 6 (TEPC + REM) | Distributed across modules |
| ISS dose per 6-month increment | 50-100 mSv | Measured by suite |

## Prerequisites

- [Radiation Protection](./radiation-protection.md) — parent capability

## See Also

- [Radiation Protection](./radiation-protection.md) — parent capability
- [Storm Shelters](./radiation-protection.storm-shelters.md) — operational response to detected SPE
- [Space Medicine](./space-medicine.md) — dose limits and health effects
