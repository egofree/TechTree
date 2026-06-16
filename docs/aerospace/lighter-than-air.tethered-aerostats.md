# Tethered Aerostats

> **Node ID**: aerospace.lighter-than-air.tethered-aerostats
> **Domain**: [Aerospace](./index.md)
> **Dependencies**: [`aerospace.lighter-than-air`](lighter-than-air.md)
> **Timeline**: Years 12-20
> **Outputs**: aerostats
> **Critical**: No

Tethered aerostats are stationary buoyant platforms anchored to the ground by a cable. A helium-filled envelope lifts a payload — typically antennas, radar, cameras, or meteorological instruments — to an operating altitude of hundreds to thousands of meters, where it remains for days or weeks. No propulsion or navigation system is required, making aerostats the simplest and lowest-cost gas-lift platform to deploy and operate.

## Design and Operation

A typical tactical aerostat uses a 500-15,000 m³ helium-filled envelope, loitering at 1,000-4,500 m altitude. The tether cable serves double duty: it anchors the aerostat against wind drift and carries power and data lines to the payload. The envelope uses high-barrier polymer laminate fabrics (Tedlar/PET/urethane) to minimize helium leakage, achieving permeation rates below 0.5 L/m²/day. A single aerostat can remain aloft for 2-4 weeks before requiring retrieval for helium topping-off.

Payload capacity ranges from 50 kg (small observation aerostats) to 2,000+ kg (large radar platforms like the JLENS system). Winch systems on the ground station raise and lower the aerostat for payload servicing and weather avoidance.

## Applications

- **Communications relay**: Loitering at 3,000-5,000 m, a tethered aerostat provides line-of-sight radio and data coverage over a 200-400 km radius, acting as a "poor man's satellite."
- **Surveillance**: Radar and optical payloads detect low-flying aircraft, vessels, and ground vehicles. The TARS (Tethered Aerostat Radar System) program monitors the US southern border.
- **Weather monitoring**: Instrumented aerostats provide continuous atmospheric profiling at fixed locations.
- **Mining and industrial site monitoring**: Aerostats offer persistent aerial observation of remote industrial operations.

## Prerequisites

- [Lighter-than-Air overview](lighter-than-air.md) — buoyancy physics, envelope materials
- [Chemistry](../chemistry/index.md) — helium supply (air separation or natural gas extraction)
- [Polymers](../polymers/index.md) — low-permeability barrier films for long-duration helium retention
- [Textiles](../textiles/index.md) — woven envelope substrate and load webbing

## See Also

- [Lighter-than-Air](lighter-than-air.md) — parent capability overview
- [Hot-Air Balloons](lighter-than-air.hot-air-balloons.md) — thermal lift, simplest LTA
- [Gas Airships](lighter-than-air.gas-airships.md) — powered, steerable flight
- [Aviation](aviation.md) — heavier-than-air aircraft

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md) • [All Domains](../index.md)*
