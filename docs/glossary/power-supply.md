# Power Supply

> **Type**: infrastructure | **Tier**: critical | **Domains**: energy, silicon

Silicon furnaces run 24/7/365. Interruptions cause the charge to freeze, requiring expensive and time-consuming restart. Firm, continuous power supply is a siting requirement for energy-intensive industrial processes. Locations near hydroelectric dams are preferred for cheap baseload power.

## Context in the Tech Tree

Reliable power supply is a non-negotiable prerequisite for high-temperature industrial processes. In [Metallurgical-Grade Silicon Production](../silicon/mg-si-production.md), the submerged-arc electric furnace draws 10-30 MW continuously — a power interruption of even minutes allows the charge to solidify, requiring days of work and significant cost to restart. In [Energy Storage](../energy/storage.md), the power supply must be matched to battery bank voltage and capacity for proper charging. In [Steam Turbines](../energy/steam-turbines.md), the generator must maintain precise frequency and voltage output to serve as a stable power source.

## Technical Details

The power requirements for silicon production are extreme. A typical MG-Si furnace operates at 10-30 MVA (megavolt-amperes), consuming 11,000-14,000 kWh per tonne of silicon produced. The furnace must run continuously because the charge is a molten mass at 1800-2000°C — if power is lost, the material freezes solid in the furnace vessel, forming a "bear" that must be drilled or blasted out before the furnace can be restarted. This is why silicon smelters are sited near hydroelectric dams (cheap, reliable baseload power) or large coal-fired stations with firm supply contracts.

Solar or wind alone cannot provide the reliability needed without massive battery storage — a multi-day weather event could shut down the furnace. The power supply must be firm (guaranteed delivery) and continuous (no interruptions). Battery backup for a 20 MW furnace load would require hundreds of MWh of storage — feasible technically but extremely expensive.

For smaller-scale applications, DC power supplies for battery charging must provide constant-current/constant-voltage profiles with tight voltage regulation (±0.1V per cell for lead-acid) to avoid overcharge damage.

## Related Terms

- [Energy Consumption](./energy-consumption.md) — the power demand that the supply must meet
- [Requirements](./requirements.md) — specifications the power supply must satisfy
- [Production Rates](./production-rates.md) — throughput that depends on continuous power availability

## Appears In

- [Metallurgical-Grade Silicon Production](../silicon/mg-si-production.md)
- [Energy Storage](../energy/storage.md)
- [Steam Turbines](../energy/steam-turbines.md)
