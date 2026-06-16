# Thermal & Humidity Control

> **Node ID**: human-spaceflight.eclss.thermal-humidity-control
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.eclss`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: eclss_systems
> **Critical**: Yes

Thermal and humidity control removes metabolic heat and condensate from the crewed cabin to maintain 18-27°C air temperature and 25-75% relative humidity. A condensing heat exchanger (CHX) cools cabin air below its dew point, condensing 1.2-2.0 kg of water vapour per crew member per day onto hydrophilic coatings and wicking it into a centrifugal water separator for routing to the Water Recovery System. The CHX couples through an interface heat exchanger to the spacecraft's external ammonia radiator loop, rejecting all waste heat to deep space.

Each crew member's Liquid Cooling and Ventilation Garment (LCVG) supplements cabin-air cooling during exercise, circulating 80-100 kg/h of chilled water through capillary tubes in the suit undergarment and removing up to 750 W of metabolic heat. Cabin-air cooling alone removes 150-350 W per crew member plus equipment dissipation.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Cabin air temperature | 18-27°C | Crew-selectable setpoint |
| Relative humidity | 25-75% | Nominal 45% |
| Cabin dew point | 9-12°C | Drives CHX coolant temperature |
| CHX coolant inlet | 4-7°C | Inhibited water, freeze-protected to -5°C |
| Condensate per crew | 1.5-3.0 kg/day | Wicked to WRS |
| LCVG heat removal | up to 750 W | Exercise period |
| LCVG water flow | 80-100 kg/h | Through capillary tubes |
| Cabin air flow at CHX | 100-150 m³/h | Per air revitalisation loop |

## Prerequisites

- [Environmental Control & Life Support](./eclss.md) — parent capability
- [Spacecraft Thermal Control](../spacecraft-systems/thermal-control.md) — external radiator loop heritage

## See Also

- [ECLSS](./eclss.md) — parent capability
- [Atmosphere Management](./eclss.atmosphere-management.md) — sibling process
- [Water Recovery](./eclss.water-recovery.md) — receives condensate
