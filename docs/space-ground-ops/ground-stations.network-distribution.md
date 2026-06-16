# Network Distribution

> **Node ID**: `space-ground-ops.ground-stations.network-distribution`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Ground Stations](./ground-stations.md)
> **Dependencies**: [`space-ground-ops.ground-stations`](./ground-stations.md)
> **Outputs**: network_distribution
> **Timeline**: Years 50+

## Overview

The scheduling, cross-support, and data-routing layer that turns a set of independent
stations into a coordinated global network serving a fleet of spacecraft.

## CCSDS Space Link Extension (SLE)

The international standard interface letting one agency's station serve another's mission:

- **Return-all-frames / return-channel frames** — deliver received frames upstream.
- **Return-product packets** — deliver decommutated data products.
- **Forward-cltu / forward-data** — uplink commands and crypto units.
- **Tracking / radiometric** — deliver range, Doppler, ΔDOR products.

Because SLE is standardised, ESA↔NASA cross-support becomes a paperwork exercise, not a
software port.

## Network Orchestration

Above SLE sits the scheduling layer. Missions submit pass requests; the scheduler reconciles
them against station availability and emits a conflict-free schedule, configuring each
station for every pass. Routine conflicts resolve automatically; oversubscribed resources
(the 70-m dishes) escalate to an operator.

## Cross-Support

Agreements that let the global network behave as one distributed resource — essential for
deep-space missions whose target is visible to only one complex at a time.

## See Also

- [Ground Stations](./ground-stations.md) — parent capability
- [Mission Control](./mission-control.md) — the data consumer at the network's far end
