# Fire Detection & Suppression

> **Node ID**: human-spaceflight.eclss.fire-detection-suppression
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eclss`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eclss_systems
> **Critical**: Yes

Fire detection and suppression protects the crewed cabin from ignition and sustained combustion. Because buoyant convection is absent in microgravity, flames are spherical, spread slower along solid fuels (1-10 mm/s versus 10-100 mm/s on Earth), and produce more soot and CO; without forced ventilation they self-extinguish within seconds in their own combustion products. This makes smoke transport entirely dependent on cabin ventilation flow, so detectors are placed in ventilation return ducts rather than at the ceiling.

Detection uses paired photoelectric and ionisation smoke sensors sensitive to 0.003-0.3 µm particulate; suppression employs portable 2.7 kg CO2 extinguishers in each module plus fixed water-mist systems behind equipment racks where smouldering fires are most likely. After any fire event the cabin atmosphere is scrubbed through fresh LiOH and charcoal beds and particulate filters are replaced.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Flame spread rate | 1-10 mm/s | Earth: 10-100 mm/s |
| Flame shape | Spherical | No buoyant convection |
| Self-extinguishment | 10-30 s in stagnant air | Ventilation < 1 cm/s |
| Smoke detector type | Photoelectric + ionisation | 0.003-0.3 µm particles |
| Detector location | Ventilation return ducts | Smoke transported by forced flow |
| Portable extinguisher | 2.7 kg CO2 | One per module |
| Fixed suppression | Water mist (5-10 µm droplets) | Behind equipment racks |
| Post-fire scrub | LiOH + charcoal | Atmosphere cleanup |

## Prerequisites

- [Environmental Control & Life Support](./eclss.md) — parent capability
- [Atmosphere Management](./eclss.atmosphere-management.md) — post-fire atmosphere scrubbing

## See Also

- [ECLSS](./eclss.md) — parent capability
- [Atmosphere Management](./eclss.atmosphere-management.md) — LiOH charcoal post-fire cleanup
- [Waste Management](./eclss.waste-management.md) — waste storage ignition sources
