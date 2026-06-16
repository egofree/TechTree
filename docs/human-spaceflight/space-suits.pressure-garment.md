# Pressure Garment Design

> **Node ID**: `human-spaceflight.space-suits.pressure-garment`
> **Domain**: [Human Spaceflight](./index.md)
> **Parent**: [Space Suits](./space-suits.md)
> **Dependencies**: [`human-spaceflight.space-suits`](./space-suits.md)
> **Outputs**: pressure_garments, suit_bladders, mobility_joints
> **Timeline**: Years 50-200+

## Overview

The pressure garment is the gas-retaining shell of a space suit: the bladder, restraint, and
mobility joint architecture that holds 4.3 psi (29.6 kPa) of pure oxygen against vacuum while
still letting the wearer bend every joint. Every design is a battle between pressure
retention (which wants a rigid balloon) and mobility (which wants a limp fabric).

## Layer Architecture

- **Bladder**: 0.25-0.50 mm cast urethane film on nylon ripstop. Gas-tight, flexible across
  -150°C to +120°C, resistant to thousands of pressure cycles.
- **Restraint**: Dacron and stainless steel cable network (linknet) that forces the bladder
  into a human shape under pressure, transferring load to the hard torso rings.
- **Mobility joints**: convolutes (rubber bellows, 1-3 Nm torque), bearings (titanium-race,
  near-zero torque), and conical/gimbal joints for compound bending.

## Hard Upper Torso (HUT)

The EMU's HUT is a fibreglass and stainless steel shell integrating helmet, arms, PLSS, and
life-support plumbing into one rigid core. The xEMU moves to rear-entry: the astronaut
climbs in through a back hatch, then seals against a suitport.

## See Also

- [Space Suits](./space-suits.md) — parent capability
- [Portable Life Support System](./space-suits.plss-design.md) — backpack consumables
- [Thermal Control Suit](./space-suits.thermal-control-suit.md) — LCVG undergarment

---

*Part of the [Bootciv Tech Tree](../index.md) • [Human Spaceflight](./index.md) • [All Domains](../index.md)*
