# Flight Computers

> **Node ID**: spacecraft-systems.obdh.flight-computers
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.obdh`](./obdh.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: onboard_electronics
> **Critical**: No

The flight computer is the spacecraft's central processor — it executes the flight software, processes commands, collects telemetry, and controls all subsystems. See [Onboard Data Handling](./obdh.md) for the integrated avionics context.

## Rad-Hard Processors

1. **LEON3 (AT697F)**: SPARC V8, 100 MHz, 0.35 μm, 300 krad TID, 1 W. European heritage (BepiColombo, Sentinel).
2. **RAD750**: PowerPC 750, 200 MHz, 0.15 μm, 1 Mrad TID, 5-10 W. NASA heritage (MRO, Curiosity, JWST).
3. **RAD5500**: PowerPC e5500, 400-766 MHz, 45 nm SOI, 1 Mrad. Next-generation NASA missions.
4. **RH1750A**: MIL-STD-1750A, 25 MHz, legacy 16-bit. Older DoD satellites.

## Architecture

A typical flight computer board contains:
- **Processor**: RAD750 or LEON3 (single or dual-redundant)
- **Boot PROM**: radiation-immune memory storing golden flight code image (16-64 MB)
- **SRAM**: working memory with EDAC (32-256 MB)
- **Flash**: flight software images and data storage (256 MB-4 GB)
- **FPGA**: co-processor for high-speed tasks (compression, packetization, bus interface)
- **Bus interfaces**: SpaceWire, MIL-STD-1553B, CAN, discrete I/O

## Key Parameters

- **Clock speed**: 100-200 MHz (rad-hard); 1+ GHz (COTS for LEO CubeSats)
- **TID tolerance**: 100 krad (minimum); 1 Mrad (rad-hard)
- **SEL immunity**: > 80 MeV·cm²/mg (rad-hard); > 37 (upscreened COTS)
- **Power**: 1-15 W depending on processor class
- **Memory**: 32-256 MB SRAM, 256 MB-4 GB flash
- **MIPS budget**: 20-500 MIPS depending on mission complexity

## See Also

- [Onboard Data Handling](./obdh.md) — parent capability
- [Data Buses](./obdh.data-buses.md) — interfaces connecting flight computer to subsystems
- [Flight Software](./obdh.flight-software.md) — software executing on the flight computer
- [Radiation Hardening](./radiation-hardening.md) — TID/SEE qualification of processors

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
