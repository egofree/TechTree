# Spacecraft Data Buses

> **Node ID**: spacecraft-systems.obdh.data-buses
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.obdh`](./obdh.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: onboard_electronics
> **Critical**: No

Spacecraft data buses connect the flight computer to subsystems — sensors, actuators, power controllers, and payload electronics. The choice of bus trades data rate, determinism, fault tolerance, and heritage. See [Onboard Data Handling](./obdh.md) for the integrated avionics context.

## MIL-STD-1553B

The military standard 1553B bus, introduced 1978, is the most ubiquitous spacecraft data bus:

- **Topology**: Bus controller (BC) → up to 31 remote terminals (RT), dual-redundant
- **Data rate**: 1 Mbit/s fixed, Manchester bi-phase encoding
- **Word format**: 20 bits (16 data + 3 sync + 1 parity)
- **Latency**: deterministic 4-12 μs response time
- **Fault tolerance**: dual-redundant bus with automatic failover
- **Heritage**: every US military satellite since 1980, ISS, GPS, most large spacecraft

## SpaceWire (ECSS-E-ST-50-12C)

Modern high-speed serial bus for high-data-rate instruments:

- **Data rate**: 2-400 Mbit/s (typical 100-200 Mbit/s)
- **Topology**: point-to-point links + SpaceWire routers (packet-switched network)
- **Encoding**: Data-Strobe (DS), LVDS signaling on 4 twisted pairs
- **Protocol**: network addressing, optional RMAP remote memory access
- **Heritage**: Gaia, BepiColombo, Sentinel-series, James Webb ISIM

## CAN Bus

Lower-tier subsystem interface for small satellites:

- **Data rate**: 1 Mbit/s max (40 m), priority-based arbitration
- **Topology**: multi-master, differential twisted pair
- **Heritage**: CubeSats, small satellites, automotive

## Bus Comparison

| Bus | Rate | Determinism | Redundancy | Use case |
|-----|------|-------------|-----------|----------|
| 1553B | 1 Mbit/s | Guaranteed | Dual | Critical subsystems |
| SpaceWire | 200 Mbit/s | Packet-switched | Hot-spare | Instruments, payloads |
| CAN | 1 Mbit/s | Priority | Single | Low-tier interfaces |

## See Also

- [Onboard Data Handling](./obdh.md) — parent capability
- [Flight Computers](./obdh.flight-computers.md) — bus controller host
- [Electronics](../electronics/index.md) — bus transceiver ICs

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
