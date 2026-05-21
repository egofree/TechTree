# Production Rates

> **Type**: noun | **Tier**: operational | **Domains**: metals, energy, silicon

A small charcoal blast furnace (5-6 m shaft height) produces 0.5-2 tonnes of pig iron per day. A larger furnace (10+ m) with coke fuel and steam-powered blast produces 10-50 tonnes per day. Continuous operation — once lit, a blast furnace runs for years between relinings (campaign life 5-10 years). Stopping and restarting is extremely difficult.

## Context in the Tech Tree

Production rates quantify the throughput of industrial processes and determine whether a technology can meet demand at a given development stage. In [Iron & Steel Production](../metals/iron-steel.md), production rates span from bloomery furnaces (a few kg per heat) through blast furnaces (tonnes per day) to modern basic oxygen furnaces (hundreds of tonnes per hour). In [Charcoal Production](../energy/charcoal.md), rates depend on kiln design — from earth kilns (batch, days per cycle) to continuous retorts. In [Metallurgical-Grade Silicon Production](../silicon/mg-si-production.md), a single furnace produces 5-20 tonnes per day of silicon, with the entire plant producing 20,000-100,000 tonnes per year.

## Technical Details

Production rate is determined by the intersection of process thermodynamics, equipment scale, and energy availability. A bloomery furnace produces only a few kg of iron per heat because reduction occurs in a small zone at the top of the char bed — the rate is limited by air supply (bellows capacity) and heat transfer through the charge. A blast furnace produces orders of magnitude more because it operates continuously with forced blast, counter-current gas-solid flow, and much larger reaction volume.

The continuity of operation is critical for many high-temperature processes. Blast furnaces and silicon furnaces run for years between maintenance shutdowns because restarting from cold is expensive and risky — the refractory lining experiences thermal shock, and remelting a frozen charge requires enormous energy. This is why reliable [Power Supply](./power-supply.md) is essential for these processes.

For planning purposes, production rates must be matched to downstream consumption. A silicon furnace producing 10 tonnes/day of MG-Si feeds into a purification plant that produces 2-3 tonnes/day of polysilicon, which supports wafer production of perhaps 1000-5000 wafers/day. Understanding these cascading rate relationships is essential for balanced plant design.

## Related Terms

- [Power Supply](./power-supply.md) — reliable power enables continuous production
- [Performance](./performance.md) — production rate as a key performance metric
- [Energy Consumption](./energy-consumption.md) — energy per unit of production

## Appears In

- [Iron & Steel Production](../metals/iron-steel.md)
- [Charcoal Production](../energy/charcoal.md)
- [Metallurgical-Grade Silicon Production](../silicon/mg-si-production.md)
