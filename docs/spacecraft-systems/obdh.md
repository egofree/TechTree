# Onboard Data Handling

> **Node ID**: spacecraft-systems.obdh
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`computing`](../computing/index.md),
> `electronics`
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: onboard_electronics
> **Critical**: No — OBDH is the spacecraft's brain and nervous system; it processes commands, manages subsystems, stores science data, and executes the flight plan. Without it the spacecraft is inert debris. Yet OBDH is built from the same silicon and logic gates as any [computing](../computing/index.md) system, hardened for the space environment

Onboard Data Handling (OBDH) encompasses the spacecraft's digital infrastructure: the flight computer that runs the [flight software](./obdh.flight-software.md), the data buses that connect it to sensors and actuators, the mass storage that buffers science data between ground contacts, and the real-time operating system that orchestrates it all. Every spacecraft from a CubeSat to a deep-space probe has an OBDH subsystem — the difference is processor speed, memory capacity, and degree of redundancy.

This article covers four process areas: [flight computers](./obdh.flight-computers.md) (radiation-tolerant processors), [data buses](./obdh.data-buses.md) (SpaceWire, MIL-STD-1553B, CAN), [mass storage](./obdh.mass-storage.md) (solid-state recorders), and [flight software](./obdh.flight-software.md) (RTOS, command sequencing, fault management). The [computing](../computing/index.md) domain provides the processor architectures and logic design heritage; the [electronics](../electronics/index.md) domain supplies the integrated circuits, ASICs, and FPGA building blocks.

## Overview

A spacecraft flight computer is, at its core, a microprocessor executing software from memory — conceptually identical to a desktop PC. The differences are entirely in the implementation: radiation tolerance, fault tolerance, low power consumption, and the absolute requirement to never crash irrecoverably. A spacecraft computer that hangs cannot be rebooted by pressing a button; recovery requires a ground-commanded reset or a hardware watchdog timer that pulses power to the processor.

The dominant radiation-hardened processors are all derived from commercial architectures:
- **LEON3** (SPARC V8): open-source, European, used by ESA missions
- **RAD750** (PowerPC 750): the most flown rad-hard processor, used by NASA missions since 2005
- **RH1750** (MIL-STD-1750A): legacy 16-bit, still in use on older military satellites

## Radiation-Hardened Processors

### LEON3 (AT697F)

The LEON3 is a 32-bit SPARC V8 processor synthesizable in VHDL, designed by the European Space Research and Technology Centre (ESTEC) and Gaisler Research. The Atmel AT697F is the flight-qualified silicon implementation:

- **Architecture**: SPARC V8, 5-stage pipeline, hardware multiply/divide
- **Clock speed**: 100 MHz (AT697F), up to 50 MHz in radiation-degraded mode
- **Process node**: 0.35 μm ATMEL rad-hard CMOS
- **TID tolerance**: 300 krad (tested), design target 100 krad
- **SEL immunity**: > 80 MeV·cm²/mg (no destructive latchup)
- **Power**: 1 W typical at 100 MHz
- **Cache**: 8 KB instruction + 8 KB data
- **Heritage**: BepiColombo, Galileo FOC, Sentinel-series, ExoMars Trace Gas Orbiter

### RAD750

The RAD750 is BAE Systems' radiation-hardened PowerPC 750 (the same architecture as Apple's G3 iMac processor, 1997-1999). It is the most widely used deep-space processor:

- **Architecture**: PowerPC 750, 32-bit, superscalar (can issue 2 instructions per cycle)
- **Clock speed**: 133-200 MHz (rad-hard silicon), up to 264 MHz (acceptable risk)
- **Process node**: 0.25 μm (original), 0.15 μm (current RAD750)
- **TID tolerance**: 1 Mrad (tested), survives 200 krad without parametric failure
- **SEL immunity**: > 100 MeV·cm²/mg
- **Power**: 5-10 W typical (including L2 cache and I/O)
- **Cache**: 32 KB instruction + 32 KB data + 1 MB L2
- **Heritage**: Mars Reconnaissance Orbiter (2005), Curiosity rover (2011), Perseverance rover (2020), James Webb Space Telescope (2021), Psyche (2023)

### Processor Comparison

| Processor | Arch | Clock | Process | TID | Power | Notable missions |
|-----------|------|-------|---------|-----|-------|-----------------|
| LEON3 AT697F | SPARC V8 | 100 MHz | 0.35μm | 300 krad | 1 W | BepiColombo, Sentinel |
| RAD750 | PowerPC | 200 MHz | 0.15μm | 1 Mrad | 5-10 W | MRO, Curiosity, JWST |
| RAD5500 | PowerPC e5500 | 400-766 MHz | 45nm SOI | 1 Mrad | 5-15 W | Future NASA missions |
| RH1750A | MIL-STD-1750A | 25 MHz | 1.0μm | 1 Mrad | 5 W | Legacy DoD satellites |
| IBM RAD6000 | PowerPC 601 | 33 MHz | 0.5μm | 1 Mrad | 6-10 W | Mars Pathfinder, ISS |
| PROMetheus | LEON4 | 400 MHz | 28nm SOI | 500 krad | 4 W | Development (ESA) |

The progression from RAD6000 (33 MHz, Mars Pathfinder 1997) to RAD750 (200 MHz, Perseverance 2020) represents a 6× clock improvement over 23 years. By comparison, commercial desktop processors advanced from 300 MHz (Pentium II, 1997) to 5 GHz (Core i9, 2020) — a 16× improvement in the same period. Radiation-hardening imposes a 10-15× performance lag behind commercial silicon.

## Memory Technologies

Space-rated memory faces the same radiation challenges as processors, with additional sensitivity: a single-bit flip in code memory can corrupt the flight program, while in data memory it can corrupt science data or navigation state.

### SRAM vs SDRAM

| Parameter | Rad-hard SRAM | Rad-hard SDRAM | Commercial SDRAM |
|-----------|---------------|----------------|-----------------|
| Density | 1-4 Mbit | 64-256 Mbit | 8-16 Gbit |
| TID tolerance | 1 Mrad | 100-300 krad | 10-30 krad |
| SEU rate | <10⁻¹¹/bit/day | 10⁻⁹/bit/day | 10⁻⁷/bit/day |
| Speed (access) | 15-25 ns | 10-15 ns | 8-12 ns |
| Power/bit | High | Medium | Low |
| Refresh needed | No | Yes (4-8 kHz) | Yes (8 kHz) |
| Application | Program/code memory | Working data memory | Never in rad zone |

SRAM is preferred for critical code storage (no refresh, low SEU rate). SDRAM provides higher density for data buffers but requires EDAC and periodic scrubbing.

### Non-volatile memory

- **PROM/EEPROM**: stores bootstrap loader and golden flight code image; immune to SEU, 100 krad TID
- **NOR Flash**: stores flight software images; 1-16 MB typical; 30-100 krad TID; read-only in flight
- **NAND Flash**: mass storage (SSR); 1-10×10¹⁵ writes; 10-50 krad TID; requires wear-leveling
- **MRAM** (Magnetoresistive RAM): emerging technology; unlimited writes, no refresh, 1 Mrad TID; currently 1-16 Mbit density

## Data Buses

Spacecraft subsystems communicate over standardized serial buses. The choice of bus trades data rate, fault tolerance, EMI immunity, and heritage.

### MIL-STD-1553B

The military standard 1553B bus, introduced in 1978, is the most ubiquitous spacecraft data bus. It uses a dual-redundant transformer-coupled twisted-pair at 1 Mbit/s:

- **Topology**: Bus controller (BC) → Remote terminals (RT), up to 31 RTs per bus
- **Data rate**: 1 Mbit/s (fixed)
- **Encoding**: Manchester bi-phase (self-clocking)
- **Fault tolerance**: Dual-redundant bus with automatic failover
- **Word size**: 20 bits (16 data + 3 sync + 1 parity)
- **Message format**: Command word → Data words (1-32) → Status word
- **Response time**: 4-12 μs guaranteed (deterministic)
- **Heritage**: Essentially every US military satellite since 1980, ISS, GPS

### SpaceWire (IEEE 1355 / ECSS-E-ST-50-12C)

SpaceWire is the modern high-speed serial bus for spacecraft, designed by ESA for high-data-rate instruments:

- **Data rate**: 2-400 Mbit/s (typical 100-200 Mbit/s)
- **Encoding**: Data-Strobe (DS) encoding, LVDS signaling
- **Topology**: Point-to-point links + routers (packet-switched network)
- **Protocol**: Network layer addressing, optional RMAP (Remote Memory Access Protocol)
- **Cable**: 4 twisted pairs (8 signals), micro-miniature D-type connectors
- **Fault tolerance**: Hot-spare redundancy, packet-level error detection
- **Heritage**: Gaia (2013), BepiColombo (2018), Sentinel-series, James Webb (ISIM)

### CAN Bus (Controller Area Network)

CAN bus is used for lower-tier subsystem interface (power distribution, thermal control):

- **Data rate**: 1 Mbit/s max (40 m at 1 Mbit/s, 1 km at 50 kbit/s)
- **Topology**: Multi-master, differential twisted pair
- **Arbitration**: Non-destructive bit-wise (priority-based)
- **Error detection**: CRC + frame check + ACK monitoring
- **Heritage**: CubeSats, small satellites, automotive heritage (millions of units)

### Bus Comparison

| Bus | Rate | Topology | Latency | Redundancy | Heritage |
|-----|------|----------|---------|-----------|----------|
| MIL-STD-1553B | 1 Mbit/s | Bus | Deterministic (4-12μs) | Dual | Very high |
| SpaceWire | 200 Mbit/s | Network | Packet-switched | Hot-spare | High |
| CAN | 1 Mbit/s | Bus | Priority-based | Single | Automotive |
| Ethernet | 100-1000 Mbit/s | Switched | Variable | Optional | Emerging |
| Time-Triggered Eth | 1000 Mbit/s | Switched | Deterministic | Triple | TTEthernet |

## Mass Storage

The Solid State Recorder (SSR) replaces legacy tape recorders for storing science data between ground contacts. A LEO Earth-observation satellite may generate 500 GB of imagery per orbit but can only downlink during a 10-minute ground pass — the SSR buffers the data.

### SSR Architecture

- **Storage media**: NAND Flash (SLC for endurance, MLC for density)
- **Capacity**: 256 GB - 4 TB (typical for current missions)
- **Interface**: SpaceWire (200 Mbit/s) or SpaceFibre (2 Gbit/s)
- **Endurance**: 10,000-100,000 write cycles per cell (SLC)
- **TID tolerance**: 10-30 krad (requires spot shielding for electronics)
- **EDAC**: Reed-Solomon or BCH block coding per page; background scrubbing
- **File system**: POSIX-compatible (typically derived from Linux or VxWorks FAT)

Notable SSR implementations: MRO (560 GB), James Webb (58.8 GB for the ISIM), Hubble (upgraded from tape to 48 GB SSR in 1999, then 2 TB solid state). The Perseverance rover uses a 3 GB RAD750-compatible SSR for daily operations.

### Data compression

To maximize downlink utilization, SSRs typically implement hardware compression:
- **Lossless**: Rice, Lempel-Ziv (2:1 typical ratio)
- **Lossy**: JPEG2000, CCSDS Image Data Compression (8:1 to 32:1 for imagery)
- **Implementation**: FPGA co-processor, 100-500 Mbit/s throughput

## Flight Software

### Real-Time Operating Systems

| RTOS | Architecture | Notable features | Heritage |
|------|-------------|-----------------|----------|
| VxWorks | Preemptive priority | POSIX, certified for safety-critical | MER, MSL, JWST, Cygnus |
| RTEMS | Priority preemptive | OSEK, DO-178B certifiable | BepiColombo, Gaia, Solar Orbiter |
| Linux + PREEMPT_RT | Preemptive kernel | Full POSIX, open-source | CubeSats, Dragon, Starlink |
| OSEKworks | OSEK/VDX | Automotive safety, small footprint | Small satellites |

### Flight software architecture layers:

1. **Hardware abstraction layer (HAL)**: processor register access, DMA, interrupt handlers
2. **Board support package (BSP)**: specific hardware initialization, peripheral drivers
3. **RTOS**: task scheduling, inter-process communication, timers
4. **Subsystem services**: command dispatch, telemetry collection, file management
5. **Mission logic**: pointing control, fault management, autonomous operations

### Command sequencing

- **Relative time sequence (RTS)**: commands execute at offsets from sequence start
- **Absolute time sequence (ATS)**: commands execute at specified UTC times
- **Command load**: ground-uplinked command list, stored in SSR, validated before execution
- **Conditional commands**: if-then-else logic based on telemetry states (e.g., "if battery < 20% then enter safe mode")
- **Time-tagged commanding**: commands stored with future execution times for operations during communications blackout

### Watchdog and fault management

- **Hardware watchdog**: counter that resets the processor if not periodically serviced (typically 1-16 second timeout)
- **Software watchdog**: per-task watchdog monitoring within the RTOS
- **Fault detection, isolation, and recovery (FDIR)**: multi-tier fault response:
  - Tier 1: component-level (e.g., EDAC corrects single-bit upset)
  - Tier 2: subsystem-level (e.g., switch to redundant processor on heartbeat loss)
  - Tier 3: system-level (e.g., enter safe-hold mode pointing at sun for power)

## Processor Sizing Rules

Selecting a flight processor involves trading performance, power, radiation tolerance, and cost:

- **MIPS budget**: attitude control (5-20 MIPS), guidance/navigation (10-50 MIPS), payload processing (10-500 MIPS)
- **Memory footprint**: RTOS (200 KB-2 MB), flight application (1-50 MB), science buffer (256 MB-4 GB)
- **Power envelope**: CubeSat (0.5-2 W), small satellite (2-5 W), deep-space probe (5-15 W)
- **Cost**: commercial COTS ($10-100), COTS-upscreened ($1K-10K), rad-hard ($100K-$1M+)

## Troubleshooting

| Symptom | Likely cause | Diagnostic action |
|---------|-------------|-------------------|
| Processor hang | SEU in code SRAM or stack corruption | Hardware watchdog reset; reload golden image from PROM |
| Intermittent bus errors | 1553B terminal degraded or cable intermittent | Check RT status word; switch to redundant bus |
| SSR write failures | NAND flash bad blocks or TID degradation | Invoke wear-leveling remap; check page ECC statistics |
| High EDAC correction rate | Elevated radiation environment (trapped belts) | Monitor single-bit correction count; enter safe mode if > threshold |
| Software timing overrun | Task deadline miss from payload burst | Check RTOS task profiling; reduce non-critical task rates |
| Lost telemetry frames | SpaceWire link CRC errors or buffer overflow | Check link error counters; increase virtual channel buffer depth |

## Strengths

- Mature processor heritage: SPARC V8 and PowerPC have 25+ years of operational flight history
- Deterministic buses (1553B, SpaceWire) guarantee worst-case latency for critical commanding
- EDAC and TMR provide transparent single-bit-upset correction without software intervention
- Solid-state recorders have eliminated tape recorder failures (the single most common satellite anomaly of the 1980s)
- Open standards (LEON VHDL, CCSDS, SpaceWire) reduce vendor lock-in and enable multi-source procurement
- Watchdog timers and FDIR architectures enable autonomous fault recovery without ground intervention
- Dual-redundant processor chains provide failover within seconds of primary fault detection

## Weaknesses

- Rad-hard processors lag commercial silicon by 10-15 years in clock speed and 2-3 process generations
- Rad-hard parts are produced in small batches (hundreds per year) with 20-50× commercial pricing
- Memory density is 100-1000× lower than commercial: a 4 TB spacecraft SSR is equivalent to a $20 consumer SSD
- Single-event latchup risk in COTS parts can destroy components in milliseconds without current limiting
- Software complexity has grown faster than processor capability: JWST has ~400K lines of flight code vs Voyager's ~3K
- 1553B bus at 1 Mbit/s is a bottleneck for modern high-data-rate instruments
- Verification of flight software requires exhaustive testing — undiscovered timing bugs can cause years-long anomalies

## See Also

- [Flight Computers](./obdh.flight-computers.md) — LEON3, RAD750, processor selection
- [Data Buses](./obdh.data-buses.md) — SpaceWire, MIL-STD-1553B, CAN bus
- [Mass Storage](./obdh.mass-storage.md) — SSR, NAND flash, data compression
- [Flight Software](./obdh.flight-software.md) — RTOS, command sequencing, FDIR
- [Computing](../computing/index.md) — processor architecture heritage
- [Electronics](../electronics/index.md) — ICs, FPGAs, ASICs
- [Radiation Hardening](./radiation-hardening.md) — TID/SEE mitigation for OBDH components
- [TT&C Systems](./ttac.md) — downlink of stored telemetry data

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
