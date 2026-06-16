# Logistics Resupply

> **Node ID**: human-spaceflight.space-stations.logistics-resupply
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `human-spaceflight.space-stations`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 50-200+
> **Outputs**: space_stations, cargo_resupply
> **Critical**: Yes

Logistics resupply encompasses the cargo vehicles, manifesting systems, and rendezvous and capture operations that sustain a continuously crewed space station. Four vehicles currently service the ISS: SpaceX Cargo Dragon 2, Northrop Grumman Cygnus, JAXA HTV (Kounotori), and Roscosmos Progress. Each delivers pressurised cargo — food, water, oxygen, spare parts, experiments — and disposes of trash on destructive reentry.

Cargo Dragon 2 is unique in its ability to return significant payload to Earth, critical for returning failed hardware and completed experiment samples. The other vehicles burn up during controlled atmospheric reentry after cargo transfer and trash loading.

## Key Parameters

| Vehicle | Upmass (kg) | Downmass (kg) | Interface | Cadence |
|---------|------------|---------------|-----------|---------|
| Cargo Dragon 2 | 3,300 | 2,500 | IDA docking | 2-3/yr |
| Cygnus | 3,500 | 0 | CBM berthing | 2/yr |
| HTV | 5,200 | 0 | CBM berthing | 1/yr |
| Progress MS | 2,500 | 0 | Probe-drogue | 3-4/yr |

## Consumables per Crew Member

- Oxygen: 0.84 kg/day; Water: 3.0 kg/day; Food (dry): 1.5 kg/day
- Total: ~6.3 kg/person/day minimum; a crew of six over one year needs ~13,800 kg

## Rendezvous and Capture Sequence

1. Launch vehicle inserts cargo spacecraft ~50 km below station
2. Phasing orbits raise altitude over 2-3 days; relative nav via K-band radar then LIDAR
3. Hold points at 30 km, 1 km, 250 m, 30 m for go/no-go checks
4. Final approach at 3-10 cm/s; robotic arm captures berthing vehicle or docking system auto-captures

## Prerequisites

- [Space Stations](./space-stations.md) — parent capability
- [Robotic Manipulator Arms](./space-stations.robotic-arms.md) — arm captures berthing vehicles
- [Structural Docking](./space-stations.structural-docking.md) — CBM berthing interface

## See Also

- [Space Stations](./space-stations.md) — parent capability
- [Robotic Manipulator Arms](./space-stations.robotic-arms.md) — arm performs berthing capture
- [Structural Docking + Berthing](./space-stations.structural-docking.md) — berthing interface
