# Mass Storage

> **Node ID**: spacecraft-systems.obdh.mass-storage
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.obdh`](./obdh.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: onboard_electronics
> **Critical**: No

The Solid State Recorder (SSR) stores science data, telemetry, and flight software between ground station contacts. A LEO satellite may generate hundreds of GB per orbit but downlink for only 10 minutes per pass. See [Onboard Data Handling](./obdh.md) for the integrated avionics context.

## SSR Architecture

1. **Storage media**: NAND flash — SLC (single-level cell) for endurance, MLC (multi-level cell) for density
2. **Controller**: FPGA or ASIC implementing wear-leveling, bad-block management, and EDAC
3. **Interface**: SpaceWire (200 Mbit/s) or SpaceFibre (2 Gbit/s) to the flight computer
4. **File system**: POSIX-compatible, typically derived from FAT or custom flight file system

## Key Parameters

- **Capacity**: 256 GB - 4 TB (current flight missions)
- **NAND type**: SLC (10,000-100,000 write cycles) or MLC (3,000-10,000 cycles)
- **TID tolerance**: 10-30 krad (requires spot shielding for controller electronics)
- **EDAC**: Reed-Solomon or BCH per page; background scrubbing
- **Read/write speed**: 100-500 Mbit/s (SpaceWire limited); 2 Gbit/s (SpaceFibre)
- **Mass**: 1-5 kg typical
- **Power**: 5-20 W active, <1 W idle

## Data Compression

To maximize downlink utilization, SSRs implement hardware compression:
- **Lossless**: Rice, Lempel-Ziv (2:1 typical ratio)
- **Lossy**: JPEG2000, CCSDS Image Data Compression (8:1 to 32:1 for imagery)
- **Throughput**: 100-500 Mbit/s via FPGA co-processor

## Notable SSRs

- MRO: 560 GB (largest at launch, 2005)
- JWST: 58.8 GB for ISIM instrument data
- Hubble: upgraded from tape to 48 GB SSR (1999), then 2 TB (2009)
- Perseverance: 3 GB RAD750-compatible daily operations store

## See Also

- [Onboard Data Handling](./obdh.md) — parent capability
- [Flight Computers](./obdh.flight-computers.md) — SSR controller host
- [Telemetry Formatting](./ttac.tm-formatting.md) — data readout during ground passes
- [Radiation Hardening](./radiation-hardening.md) — TID tolerance of NAND flash

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
