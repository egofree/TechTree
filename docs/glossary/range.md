# Range

> **Type**: noun | **Tier**: operational | **Domains**: transport

100-300 km typical for light aircraft. Lift equation: L = ½ρv²SCL, where ρ = air density, v = airspeed, S = wing area, CL = lift coefficient. At 80 km/h with 15 m² wing area and CL = 0.8, lift equals approximately 1800 N — sufficient for a 180 kg aircraft at sea level.

## Context in the Tech Tree

Range — the operational distance a vehicle or signal can cover — is a key performance parameter in transportation and communications. In [Light Aircraft](../transport/light-aircraft.md), range is determined by fuel capacity, engine fuel consumption, and aerodynamic efficiency. In [Telegraph Communication](../transport/telegraph.md), range is limited by signal attenuation in the cable (resistance and capacitance reduce pulse amplitude with distance). Understanding range limitations drives infrastructure planning: how many relay stations are needed, where fuel depots must be placed, and what routes are feasible.

## Technical Details

For aircraft, range depends on the Breguet range equation: R = (η/c) × (L/D) × ln(W_initial/W_final), where η is propeller efficiency, c is specific fuel consumption, L/D is lift-to-drag ratio, and W represents initial and final aircraft weights (the difference being fuel consumed). Practical light aircraft achieve 100-300 km range, limited by fuel tank capacity and the modest efficiency of small piston engines.

Aerodynamic design parameters that affect range include wing configuration (high-wing vs. low-wing affects drag and structural weight), wing loading (higher loading = faster cruise but longer takeoff roll), and aspect ratio (higher aspect ratio = better L/D but structurally heavier). The lift equation L = ½ρv²SCL shows that lift scales with the square of airspeed — doubling speed quadruples lift, but also quadruples drag.

For telegraph cables, range is limited by resistance (voltage drop along the conductor) and capacitance (charge storage in the insulation). At transatlantic distances (~4000 km), cable resistance and capacitance are so large that individual Morse pulses are attenuated and smeared, requiring sensitive mirror galvanometers and skilled operators to decode. Repeaters were not available until electronic amplification (vacuum tubes) was developed decades later.

## Related Terms

- [Performance](./performance.md) — range as a key performance metric
- [Requirements](./requirements.md) — minimum range specifications for operational needs
- [Power Supply](./power-supply.md) — energy source that determines range

## Appears In

- [Light Aircraft](../transport/light-aircraft.md)
- [Telegraph Communication](../transport/telegraph.md)
