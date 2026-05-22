# Temperature Control

> **Type**: noun | **Tier**: critical | **Domains**: ceramics, chemistry, energy, measurement, silicon, vlsi-scaling

Product purity is maintained by controlling column temperatures. The temperature at the top of the distillation column indicates distillate composition — for binary systems, the temperature directly maps to composition via the vapor-liquid equilibrium curve.

## Context in the Tech Tree

Temperature control — the ability to maintain a process at a specified temperature within narrow tolerances — is essential for reproducible manufacturing. In [Distillation](../chemistry/distillation.md), a temperature controller adjusts reflux ratio or reboiler heat to maintain constant overhead temperature, directly determining product purity. In [CZ Crystal Pulling](../silicon/cz-pulling.md), molten silicon temperature must be held within ±0.5°C to maintain single-crystal growth. In [Advanced Ceramics](../ceramics/advanced-ceramics.md), sintering profiles with controlled heating and cooling rates determine final microstructure and mechanical properties.

## Technical Details

Temperature control systems range from simple on/off thermostats to sophisticated PID (Proportional-Integral-Derivative) controllers. A bimetallic strip thermostat provides ±2-5°C accuracy with mechanical simplicity — brass and steel laminated together bend at different rates when heated, opening or closing electrical contacts. PID controllers achieve ±0.1-1°C stability by continuously adjusting heater power based on the error (proportional), accumulated error over time (integral), and rate of change (derivative).

In distillation, a "sensitive tray" near the feed point is controlled rather than the top temperature, as it shows the strongest response to composition changes. For multicomponent columns, multiple temperature controllers operate at different heights to manage the separation of several products simultaneously.

In crystal growth, the melt temperature is controlled by adjusting power to the resistance or RF heater, with thermocouple or optical pyrometer feedback. The pull rate and rotation speed also affect the thermal environment at the crystal-melt interface.

## Related Terms

- [Applications](./applications.md) — specific uses of temperature-controlled processes
- [Principle](./principle.md) — thermodynamic basis for temperature-composition relationships
- [Construction](./construction.md) — building temperature-controlled equipment
- [Vibration Isolation](./vibration-isolation.md) — companion requirement for precision thermal equipment

## Appears In

- [Advanced Ceramics](../ceramics/advanced-ceramics.md)
- [Distillation](../chemistry/distillation.md)
- [Electric Furnaces](../energy/electric-furnaces.md)
- [Precision Metrology](../measurement/precision-metrology.md)
- [CZ Crystal Pulling](../silicon/cz-pulling.md)
- [Advanced Lithography](../vlsi-scaling/advanced-lithography.md)
