# Refrigeration

> **Node ID**: food-processing.refrigeration
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: `chemistry`, `energy`, `metals`
> **Critical**: No — refrigeration extends shelf life but canning and drying provide preservation without ongoing energy input
> **Timeline**: Years 20-30
> **Outputs**: refrigerated_food

Refrigeration is mechanical cooling that slows microbial growth, chemical degradation, and enzymatic activity. It extends fresh food shelf life by 5-20× but requires continuous energy input — a fundamental limitation that distinguishes it from all other preservation methods. Refrigeration depends on [energy](../energy/index.md) for mechanical compressors, [chemistry](../chemistry/index.md) for refrigerants, and [metals](../metals/index.md) for pipes and vessels.

For other preservation methods, see [Traditional Preservation](traditional-preservation.md), [Canning & Thermal Sterilization](canning.md), [Food Fermentation](fermentation.md), and [Pasteurization](pasteurization.md).

## Temperature Zones

- **Refrigerator**: 0-4°C (fresh food). Most bacteria double every 12-24 hours at this temperature (vs. 20 minutes at 37°C).
- **Freezer**: -18°C or below (long-term storage). Microbial growth is essentially halted.
- **Blast freezer**: -30°C to -40°C (rapid freezing for quality preservation). Prevents large ice crystal formation.

## Microbial Growth Rates by Temperature

At 4°C, most bacteria double every 12-24 hours (vs. 20 minutes at 37°C). At -18°C, growth is essentially halted.

| Food | Room Temp (25°C) | Refrigerated (4°C) | Frozen (-18°C) |
|------|:----------------:|:------------------:|:--------------:|
| Raw meat | 4-8 hours | 3-5 days | 6-12 months |
| Raw fish | 4-6 hours | 1-2 days | 3-6 months |
| Fresh milk | 4-6 hours | 5-7 days | 3 months |
| Cooked rice | 6-8 hours | 4-6 days | 6 months |
| Cut fruit | 2-4 hours | 3-5 days | 6-12 months |
| Fresh vegetables | 1-2 days | 5-7 days | 8-12 months |
| Bread | 3-5 days (mold) | 7-10 days | 3-6 months |

## Ice Production

**Pre-mechanical**: Ice harvested from frozen lakes, stored in insulated ice houses (sawdust insulation, underground). 50-70% of stored ice survives summer.

**Mechanical**: Ammonia absorption or vapor-compression cycle. Ice harvesting from frozen lakes provides 50-200 tonnes of natural ice per winter, enabling cold storage without mechanical refrigeration.

## Cold Chain

Continuous refrigeration from production to consumption. A single break in the cold chain can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential.

**Strengths**:
- At 4°C, bacterial doubling time extends from 20 minutes (37°C) to 12-24 hours — extends fresh food shelf life by 5-20×
- Freezing at -18°C halts microbial growth entirely, preserving food for 6-12 months with minimal quality loss
- Ice harvesting from frozen lakes provides 50-200 tonnes of natural ice per winter, enabling cold storage without mechanical refrigeration

**Weaknesses**:
- Mechanical refrigeration requires 0.5-2.0 kW per m³ of cold storage and 200-500 kWh/day for a 100 m³ freezer — massive energy demand
- Cold chain is fragile: a single power failure or equipment breakdown can destroy an entire inventory of frozen food
- Blast freezing (-30°C to -40°C) is needed for quality preservation; slow freezing creates large ice crystals that rupture cell walls and produce mushy texture on thawing

## Scaling Notes

- **Ice house** (pre-mechanical, 50-200 people): Harvest ice from frozen lakes in winter. Store in insulated underground chamber with sawdust. 50-70% of stored ice survives summer. Provides cold storage for community without any energy input.
- **Mechanical cold room** (community, 500-2,000 people): 10-50 m³ cold room at 0-4°C. Ammonia absorption or small compressor. Requires 5-20 kW electrical or mechanical power. Cold storage for perishables: meat, dairy, produce.
- **Industrial cold storage** (10,000+ people): 100-1,000+ m³ cold rooms and freezers. Vapor-compression system with ammonia or freon refrigerant. A 100 m³ cold room at -18°C requires 50-100 kW cooling capacity and 200-500 kWh/day electrical energy.
- **Cold chain scaling**: A single refrigerated truck requires 10-30 kW refrigeration capacity. Rail refrigerated cars: 15-40 kW. Cold chain logistics multiply energy requirements by distribution distance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Freezer burn | Poor packaging, temperature fluctuation, extended storage | Wrap tightly in moisture-proof material. Maintain -18°C continuously. Use within recommended time |
| Equipment failure | Compressor malfunction, refrigerant leak, power failure | Maintain backup power generator. Inspect refrigerant lines regularly. Install temperature alarms with battery backup |
| Slow freezing (mushy texture) | Overloaded freezer, insufficient airflow, blast freezer capacity exceeded | Freeze in smaller batches. Ensure airflow around products. Use blast freezer for quality-sensitive products |

## Safety

- **Cold chain integrity**: A single break in the cold chain can allow dangerous bacterial growth. Temperature monitoring with recording devices is essential for all cold storage.
- **Refrigerant safety**: Ammonia (NH₃) is toxic at 300 ppm and lethal at 5,000 ppm. Ammonia refrigeration systems require leak detection and ventilation. Freon refrigerants are less toxic but may displace oxygen in confined spaces.
- **Pressure vessel safety**: Refrigeration compressors and condensers operate at elevated pressures. Follow pressure vessel safety protocols.

## See Also

- [Food Preservation](preservation.md) — overview hub for all preservation methods
- [Pasteurization](pasteurization.md) — pasteurized products require refrigeration
- [Canning & Thermal Sterilization](canning.md) — shelf-stable preservation without refrigeration
- [Traditional Preservation](traditional-preservation.md) — drying, salting, smoking
- [Energy](../energy/index.md) — electrical power for compressors
- [Chemistry](../chemistry/index.md) — refrigerant chemistry

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Food Processing](./index.md) • [All Domains](../../index.md)*
