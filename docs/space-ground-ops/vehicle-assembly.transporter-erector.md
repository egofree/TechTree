# Transporter/Erector & Crawler

> **Node ID**: space-ground-ops.vehicle-assembly.transporter-erector
> **Domain**: [Space Ground Operations](./index.md)
> **Dependencies**: [`space-ground-ops.vehicle-assembly`](./vehicle-assembly.md)
> **Enables**: None
> **Timeline**: Years 50+
> **Outputs**: integrated_vehicles
> **Critical**: No

The transporter/erector launcher (TEL) and Crawler-Transporter (CT) move the fully-assembled launch vehicle from the VAB to the launch pad. The two CTs at Kennedy Space Center (CT-1 and CT-2) were built by Marion Power Shovel in 1965-1966; each masses 2,721 tonnes empty and carries up to 5,450 tonnes of MLP plus vehicle, for an 8,200-tonne gross vehicle weight. The CT has four tracked bogies (57 shoes each, 1.1 t per shoe) driven by diesel-electric propulsion: two 2,750-hp Alco diesels generate electricity for sixteen 1,000-hp DC traction motors. Maximum loaded speed is 1.6 km/hr; fuel consumption is 350 L/km. A laser-guided hydraulic leveling system holds the deck within ±15 cm across the 40m × 35m footprint (±0.2° angular), keeping the MLP and vehicle vertical during transport. For non-CT operations (Falcon 9 at SLC-40, Soyuz at Baikonur), the TEL is a strongback truss that carries the vehicle horizontally and erects it at the pad in 30-60 minutes.

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Crawler empty mass | 2,721 t (CT-1 and CT-2) |
| Maximum payload (MLP + vehicle) | 5,450 t (Saturn V stack) |
| Gross mass (loaded) | 8,200 t |
| Crawler dimensions | 40m × 35m × 6.1m |
| Number of tracks | 4 (2 per side) |
| Maximum speed (empty) | 3.2 km/hr |
| Fuel consumption | 350 L/km |
| Traction motors | 16 × 1,000 hp DC |
| Leveling accuracy | ±15 cm over 40m × 35m (±0.2°) |

## Process Overview

1. **Chassis fabrication**: Cast/forge crawler steel frame; machine bogie pivot points
2. **Drive system**: Install 2 diesel-electric generator sets; wire 16 traction motors
3. **Tracking**: Assemble 4 × 57-shoe track loops; tension to specification
4. **Leveling system**: Install 4 hydraulic jacking cylinders (1.8m bore); commission laser reference
5. **Crawlerway**: Construct 5.6 km river-gravel-surface road from VAB to LC-39A/B

## Prerequisites

- Vehicle Assembly capability (parent)
- Heavy machinery construction (diesel-electric drive, hydraulics)
- Construction capability for crawlerway paving

## See Also

- [Vehicle Assembly](./vehicle-assembly.md) — parent capability
- [Vertical Assembly Building](./vehicle-assembly.vab-facilities.md) — origin of rollout
- [Launch Complex](./launch-complex.md) — destination at pad
- [Machine Tools](../machine-tools/index.md) — heavy machinery heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Space Ground Operations](./index.md)*
