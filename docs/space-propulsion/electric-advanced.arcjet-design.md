# Arcjet Design

> **Node ID**: space-propulsion.electric-advanced.arcjet-design
> **Domain**: [Space Propulsion](./index.md)
> **Dependencies**: [`space-propulsion.electric-advanced`](./electric-advanced.md)
> **Enables**: None
> **Timeline**: Years 50-200+
> **Outputs**: advanced_thrusters
> **Critical**: No

Arcjets are electrothermal thrusters that heat a propellant gas using a DC arc discharge between a central cathode and a concentric anode nozzle. The gas reaches 10,000–20,000 K at the arc core — far above any structural material's melting point — before expanding through a converging-diverging nozzle to produce thrust. Hydrazine arcjets (500–800 s Isp at 1–2 kW) have flown on dozens of GEO communication satellites for north-south station-keeping since the 1990s. See [Electric Propulsion — Advanced](./electric-advanced.md) for the integrated context.

## Process Description

1. **Cathode preparation**: 2% thoriated tungsten (WT20) is machined to a sharp-tipped electrode (1–3 mm tip radius) that concentrates the arc attachment.
2. **Anode/nozzle machining**: the anode is a converging-diverging nozzle machined from tungsten or thoriated tungsten, with a 1–2 mm throat diameter.
3. **Regenerative cooling channels**: the incoming cold propellant flows through channels machined into the nozzle body before reaching the arc region, absorbing waste heat.
4. **Arc ignition**: a high-voltage pulse (2–5 kV) breaks down the gas gap; the discharge then transitions to a steady DC arc at 80–150 V, 5–20 A.
5. **Constricted arc column**: the arc is constricted through the narrow nozzle throat, maximizing energy transfer to the propellant via ohmic heating and radiative absorption.
6. **Nozzle expansion**: the hot gas expands through the diverging section, converting thermal enthalpy to directed kinetic energy.

## Key Parameters

- **Propellant**: hydrazine (N₂H₄), ammonia (NH₃), or hydrogen (H₂)
- **Arc voltage**: 80–150 V DC
- **Arc current**: 5–20 A
- **Power**: 0.3–30 kW (flight units at 1–2 kW)
- **Thrust**: 0.1–2 N
- **Isp**: 450–800 s (hydrazine), 600–900 s (ammonia), 1000–2000 s (hydrogen)
- **Efficiency**: 25–40% (frozen flow and radiation losses)
- **Cathode lifetime**: 500–1500 hr (thoriated tungsten erosion)

## Prerequisites

- Thoriated tungsten electrode manufacturing
- Precision nozzle machining (tungsten, μm tolerance)
- Regenerative cooling channel design

## See Also

- [Electric Propulsion — Advanced](./electric-advanced.md) — parent capability
- [VASIMR Design](./electric-advanced.vasimr-design.md) — RF plasma alternative
- [Magnetoplasmadynamic](./electric-advanced.magnetoplasmadynamic.md) — electromagnetic alternative

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Propulsion](./index.md)*
