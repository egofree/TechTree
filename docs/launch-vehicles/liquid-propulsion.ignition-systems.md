# Ignition Systems

> **Node ID**: launch-vehicles.liquid-propulsion.ignition-systems
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.liquid-propulsion`](./liquid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: ignition_systems
> **Critical**: No

Starting a liquid rocket engine requires a precisely sequenced ignition event within a narrow timing window. Too early — the propellant has not filled the chamber, flame blows out. Too late — propellant accumulates and detonates on ignition, destroying the chamber. See [Liquid Propulsion](./liquid-propulsion.md) for the integrated engine context.

## Ignition Methods

- **Pyrotechnic (TEA-TEB)**: Triethylaluminum/triethylborane — a pyrophoric liquid that ignites spontaneously on contact with oxygen. Sprayed into the chamber ahead of the main propellant flow. Used by Merlin (visible as the green flash at ignition). Simple and reliable but consumes a finite stored charge per ignition.
- **Torch igniter**: A spark plug ignites a small fuel-oxidizer mixture in a torch chamber; the torch flame ignites the main chamber. Used by RS-25 and most staged-combustion engines. Restartable for multiple burns.
- **Laser ignition**: A focused laser pulse ignites a small propellant pocket. Under development for deep-space restartable engines requiring decades of storage reliability.
- **Hypergolic**: Propellant combinations (hydrazine + N2O4) ignite on contact — no igniter needed. Used in orbital maneuvering engines and Apollo LM. Each injection is an ignition event.

## Staged Ignition Sequence

1. Purge chamber with inert gas (helium) to remove residual propellant or air
2. Open igniter (spray TEA-TEB or fire spark plug)
3. Crack fuel valve (lead or lag relative to oxidizer by 50-200 ms)
4. Open oxidizer valve — ignition occurs within 10-50 ms of propellant mixing
5. Ramp turbopump to full speed over 2-5 seconds (avoiding chamber pressure spike)
6. Close igniter once self-sustaining combustion is confirmed

## Key Parameters

- **Ignition delay**: 10-50 ms (propellant-dependent)
- **TEA-TEB charge**: 0.1-1 kg per ignition (engine-dependent)
- **Spark energy (torch igniter)**: 50-200 mJ per spark
- **Restart capability**: Pressure-fed and gas-generator engines: yes. Staged combustion: difficult (requires preburner restart sequence)

## See Also

- [Liquid Propulsion](./liquid-propulsion.md) — parent capability
- [Engine Cycles](./liquid-propulsion.engine-cycles.md) — cycle determines ignition complexity

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md)*
