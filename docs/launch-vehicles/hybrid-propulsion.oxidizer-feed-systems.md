# Oxidizer Feed Systems

> **Node ID**: launch-vehicles.hybrid-propulsion.oxidizer-feed-systems
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.hybrid-propulsion`](./hybrid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: oxidizer_feed_systems
> **Critical**: No

Oxidizer feed system design is the engineering of the liquid or gaseous oxidizer delivery path in a hybrid rocket engine. The feed architecture determines chamber pressure, throttle response, and whether the engine is pressure-fed or pump-fed. This process is part of the [Hybrid Propulsion](./hybrid-propulsion.md) capability.

## Pressure-Fed Systems

The oxidizer tank is pressurized to 3-7 MPa, forcing liquid oxidizer through the injector into the combustion chamber. Simple and reliable; limited to chamber pressures below ~5 MPa.

- **Helium-pressurized LOX**: high-pressure helium (20-35 MPa) stored in COPVs (composite overwrapped pressure vessels), regulated down to drive LOX from its tank. Standard liquid-engine heritage.
- **N2O self-pressurization**: nitrous oxide's vapor pressure (~5 MPa at 20°C) expels it from the tank without a separate pressurant — a major simplicity gain. Used on SpaceShipOne (74 kN) and SpaceShipTwo (270 kN). Hazard: N2O can thermally decompose if heated above 300°C or adiabatically compressed (the 2007 Scaled Composites accident).

## Pump-Fed Systems

A turbopump (or electric motor-driven pump) raises the oxidizer to 10-30 MPa for high-pressure injection. Enables higher chamber pressure, higher Isp (better expansion ratio), and lighter oxidizer tanks.

- **GOX turbopump**: liquid LOX is pumped, gasified in a heat exchanger, and injected as gaseous oxygen. Higher mixture uniformity and combustion efficiency. Used in the AMROC H-1800 (1,050 kN, the most powerful hybrid ever tested).
- **Electric pump**: a battery-powered motor drives a centrifugal pump, as in Rocket Lab's Rutherford liquid engine. Simpler than a gas-generator turbine; feasible for small-to-medium hybrids.

## Throttle and Control

The oxidizer valve is the throttle. A ball or butterfly valve, driven by electric or hydraulic actuator, modulates flow from ~20% to 100% thrust in 0.5-2 s. The fuel flow follows via the regression law, keeping O/F roughly constant across the range. Closing the valve shuts down combustion in 50-200 ms; reopening with an igniter restarts it — enabling stop/restart mission profiles impossible with solid motors.

See [Fuel Grain Design](./hybrid-propulsion.fuel-grain-design.md) for the fuel side and [Hybrid Propulsion](./hybrid-propulsion.md) for the full capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
