# Flight Software

> **Node ID**: spacecraft-systems.obdh.flight-software
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.obdh`](./obdh.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: onboard_electronics
> **Critical**: No

Flight software is the real-time program that runs on the flight computer, executing the mission plan, managing subsystems, collecting telemetry, and responding to faults. See [Onboard Data Handling](./obdh.md) for the integrated avionics context.

## Real-Time Operating Systems

| RTOS | Architecture | Heritage |
|------|-------------|----------|
| VxWorks | Preemptive priority | MER, MSL, JWST, Cygnus |
| RTEMS | Priority preemptive | BepiColombo, Gaia, Solar Orbiter |
| Linux + PREEMPT_RT | Preemptive kernel | CubeSats, Dragon, Starlink |

## Software Architecture Layers

1. **Hardware abstraction layer (HAL)**: processor register access, DMA, interrupt handlers
2. **Board support package (BSP)**: hardware initialization, peripheral drivers
3. **RTOS**: task scheduling, inter-process communication, timers, semaphores
4. **Subsystem services**: command dispatch, telemetry collection, file management
5. **Mission logic**: pointing control, fault management, autonomous operations

## Command Sequencing

- **Relative time sequence (RTS)**: commands execute at offsets from sequence start
- **Absolute time sequence (ATS)**: commands execute at specified UTC times
- **Conditional commands**: if-then-else logic based on telemetry states
- **Time-tagged commanding**: stored with future execution times for blackout operations

## Fault Management (FDIR)

Multi-tier fault detection, isolation, and recovery:
- **Tier 1 (component)**: EDAC corrects single-bit upsets; watchdog timer resets hung tasks
- **Tier 2 (subsystem)**: switch to redundant processor on heartbeat loss; failover to backup bus
- **Tier 3 (system)**: enter safe-hold mode pointing at sun for power; await ground intervention

## Key Parameters

- **Code size**: 100K-500K lines (modern missions); ~3K lines (Voyager, 1977)
- **Task count**: 50-200 concurrent tasks
- **Timing**: hard real-time deadlines of 1-100 ms for attitude control loops
- **Watchdog timeout**: 1-16 seconds (hardware); per-task software watchdogs

## See Also

- [Onboard Data Handling](./obdh.md) — parent capability
- [Flight Computers](./obdh.flight-computers.md) — hardware platform for flight software
- [Data Buses](./obdh.data-buses.md) — subsystem interfaces managed by software
- [Computing](../computing/index.md) — processor architecture heritage

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
