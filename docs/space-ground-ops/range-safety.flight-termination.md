# Flight Termination

> **Node ID**: `space-ground-ops.range-safety.flight-termination`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Range Safety](./range-safety.md)
> **Dependencies**: [`space-ground-ops.range-safety`](./range-safety.md)
> **Outputs**: flight_termination
> **Timeline**: Years 50+

## Overview

The on-vehicle system that ends a flight when commanded (or autonomously determined) to have
departed its safe envelope. Engineered to a different standard than the rest of the stack:
must fire exactly when called, and must **never** fire spuriously.

## Components

- **Destruct charges** — linear shaped charges / exploding bridgewire detonators that
  rupture propellant tanks to **disperse** propellant (not detonate it as one mass),
  spreading it so it burns off without a tanked ground impact.
- **Command-destruct receiver** — listens on a dedicated UHF uplink for an encrypted
  **arm-then-fire** two-command sequence. A single garbled command cannot fire the system.
- **Safe-and-arm device** — physical, mechanical isolation (latching pins, rotating drums)
  so no software error can fire the charges inadvertently.

## Dual-Redundant Fail-Safe

Two independent strings (separate receivers, batteries, firing circuits, detonators) so
either can terminate alone. Strings are deliberately diverse — different vendors, different
crypto — so a common-cause fault is unlikely to disable both. Reliability target: probability
of "fail to terminate when commanded" below ~1×10⁻⁴, with inadvertent-fire probability
comparably tiny.

## Autonomous FTS (AFTS)

On-board computer compares GPS state against the pre-loaded envelope and arms/fires without
ground command; shrinks the ground footprint but places enormous weight on navigation and
rule-checking software integrity.

## See Also

- [Range Safety](./range-safety.md) — parent capability
- [Range Radar](./range-safety.range-radar.md) — the tracking that triggers the decision
