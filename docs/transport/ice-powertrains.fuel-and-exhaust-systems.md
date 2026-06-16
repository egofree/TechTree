# Fuel & Exhaust Systems

> **Node ID**: transport.ice-powertrains.fuel-and-exhaust-systems
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.ice-powertrains`](./ice-powertrains.md)
> **Timeline**: Years 20-40+
> **Outputs**: fuel_systems, exhaust_systems
> **Critical**: No

This process covers fuel storage, delivery, metering, and exhaust aftertreatment. Fuel delivery evolved from the **carburetor** (venturi-drawn metering, no electricity, imprecise mixture) through **port fuel injection (PFI)** — electric pump at 3-5 bar, ECU-controlled injector per cylinder, lambda-sensor feedback holding λ = 1.00 — to **direct injection (GDI)** at 100-250 bar, spraying into the cylinder for charge cooling and higher compression, at the cost of intake-valve carbon deposits. Bosch and Denso are the reference injection-system suppliers.

Exhaust aftertreatment targets four pollutants: CO, HC, NOx, and particulate matter (PM). The **three-way catalytic converter (TWC)** — a ceramic honeycomb (400-900 cpsi) washcoated with γ-Al₂O₃ carrying Pt/Pd/Rh — oxidizes CO and HC to CO₂/H₂O while reducing NOx to N₂, but only works at stoichiometric (λ = 1.00 ± 0.005). Lead and sulfur poison the catalyst, mandating unleaded, low-sulfur fuel. For diesels, the **diesel particulate filter (DPF)** traps soot (wall-flow cordierite or SiC monolith) and regenerates at 550-650°C by oxidizing trapped carbon; **selective catalytic reduction (SCR)** injects AdBlue (32.5% urea) which hydrolyzes to NH₃ and reduces NOx over a vanadium or zeolite catalyst. The **EVAP** canister (activated carbon) captures fuel-tank vapor for purge into the intake.

Catalyst conversion efficiency is highly temperature-dependent: the TWC "lights off" (reaches 50% conversion) at ~250-300°C and reaches peak (>95%) at 400-800°C. A cold-start catalyst takes 60-120 seconds to reach light-off, during which the majority of a trip's total emissions occur — the "cold-start penalty" that drives close-coupled catalyst placement and electrically heated catalysts.

## Prerequisites

- [ICE Powertrains](./ice-powertrains.md) — parent capability, catalyst chemistry detail
- [Internal Combustion Engines](../energy/internal-combustion.md) — the combustion that produces the exhaust
- [Fuels](../energy/fuels.md) — unleaded gasoline, low-sulfur diesel
- [Iron & Steel](../metals/iron-steel.md) — exhaust manifolds, stainless steel exhaust piping

## See Also

- [ICE Powertrains](./ice-powertrains.md) — parent capability overview
- [Drivetrain Architecture](./ice-powertrains.drivetrain-architecture.md) — companion powertrain subsystem
- [Fuels](../energy/fuels.md) — fuel composition and refining

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transportation & Logistics](./index.md) • [All Domains](../index.md)*
