# Propellant Storage Facilities

> **Node ID**: space-ground-ops.launch-complex.propellant-facilities
> **Domain**: [Space Ground Operations](./index.md)
> **Dependencies**: [`space-ground-ops.launch-complex`](./launch-complex.md)
> **Enables**: None
> **Timeline**: Years 50+
> **Outputs**: launch_pads
> **Critical**: No

The propellant storage farm holds the thousands of tonnes of cryogenic and storable propellants consumed by an orbital launch vehicle, and transfers them to the vehicle in the final hours of the countdown. At LC-39A/B, the LOX storage is a 3,400 m³ vacuum-insulated stainless steel sphere holding 3,860 tonnes of liquid oxygen at -183°C; the LH2 sphere is 3,200 m³ (226 tonnes at -253°C); the RP-1 tank is 1,250 m³ (1,010 tonnes, ambient). Boil-off rates of 0.2-0.5%/day (LOX) and 0.3-0.8%/day (LH2) are managed via continuous reliquefaction or controlled venting. Transfer lines are chilled down beginning at T-8 hours; fast-fill reaches 30,000 L/min for LOX, with stable replenish mode maintaining 100% tank level until T-30 minutes.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| LOX storage capacity (LC-39A) | 3,400 m³ (3,860 t) |
| LH2 storage capacity (LC-39A) | 3,200 m³ (226 t) |
| LOX storage temperature | -183°C |
| LH2 storage temperature | -253°C |
| LOX boil-off rate | 0.2-0.5%/day |
| LH2 boil-off rate | 0.3-0.8%/day |
| LOX fast-fill rate | 30,000 L/min |
| LH2 fast-fill rate | 20,000 L/min |
| Transfer line chill-down time | 4-6 hours |
| Tank pressurization (final) | LOX 3.0 bar; LH2 3.4 bar |

## Process Overview

1. **Tank construction**: Erect vacuum-insulated double-wall stainless steel sphere; pack perlite insulation under vacuum between shells
2. **Line installation**: Route 200m of chillable transfer piping from tank to umbilical arm; install vacuum jacket and MLI wraps
3. **Chill-down**: Cool LOX lines from ambient to -183°C over 4-6 hours; LH2 to -253°C
4. **Fill sequence**: Slow-fill at 7,600 L/min to 20%; fast-fill to 100%; stable replenish
5. **Pressurization**: Pressurize vehicle tanks at T-30 min to flight pressure (LOX 3.0 bar, LH2 3.4 bar)

## Prerequisites

- Launch Complex capability (parent)
- Cryogenics.liquefaction-storage capability (Dewar vessels, vacuum insulation, MLI)
- Gas-handling capability (helium pressurization, GN2 purge, GH2 vent)

## See Also

- [Launch Complex](./launch-complex.md) — parent capability
- [Gas Liquefaction & Storage](../cryogenics/liquefaction-storage.md) — cryogenic storage fundamentals
- [Gas Handling](../gas-handling/index.md) — pressurization and vent systems

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Ground Operations](./index.md)*
