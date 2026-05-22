# Timing

> **Type**: noun | **Tier**: critical | **Domains**: animals, computing, energy, polymers, transport

Operate time 5-15 ms (coil energized to contact closure). Release time 3-10 ms (coil de-energized to contact opening). The operate/release asymmetry arises because the armature has mechanical inertia and the magnetic field collapses gradually. Maximum practical clock frequency: 30-50 Hz with careful design.

## Context in the Tech Tree

Timing — the precise sequencing and synchronization of events — is fundamental to mechanical, electrical, and biological systems. In [Electromechanical Computing](../computing/electromechanical.md), relay timing limits the maximum clock frequency of relay-based computers, directly constraining computational speed. In [Charcoal](../energy/charcoal.md) production, the timing of the burn cycle determines charcoal quality. In [Natural Rubber](../polymers/natural.md) processing, the timing of coagulation and vulcanization affects material properties. In [Aviation](../transport/aviation.md), ignition timing determines engine power and efficiency.

## Technical Details

Electromechanical relay timing illustrates the physical constraints of timing in switching systems. When a relay coil is energized, current builds exponentially (governed by L/R time constant), the armature accelerates against mechanical inertia, and contacts close with a brief contact bounce (~1-5 ms of chatter). Total operate time: 5-15 ms. On release, the magnetic field collapses (flyback diode or spark gap limits the voltage spike), and the armature returns under spring force. Release time: 3-10 ms.

The asymmetry means relay computers clock at 30-50 Hz maximum — roughly a million times slower than modern electronic computers. Each relay in a computation path adds its own delay, and the critical path (longest chain of sequential relay operations per clock cycle) determines maximum frequency.

In internal combustion engines, ignition timing (5-40° before top dead center) must advance with engine speed to compensate for the finite flame propagation speed across the cylinder.

## Related Terms

- [Construction](./construction.md) — physical design affecting timing characteristics
- [Method](./method.md) — timing-dependent processing procedures
- [Advantages](./advantages.md) — benefits of precise timing control
- [Limitations](./limitations.md) — timing constraints on system performance
- [Range](./range.md) — operating timing specifications

## Appears In

- [Pest Management](../animals/pest-management.md)
- [Electromechanical Computing](../computing/electromechanical.md)
- [Charcoal](../energy/charcoal.md)
- [Natural Rubber](../polymers/natural.md)
- [Aviation](../transport/aviation.md)
