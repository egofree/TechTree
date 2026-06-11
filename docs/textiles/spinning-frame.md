# Spinning Frame

> **Node ID**: textiles.spinning-frame
> **Domain**: [Textiles](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`textiles.spinning`](spinning.md)
> **Enables**: [`textiles.weaving`](weaving.md) (mass-scale yarn supply)
> **Timeline**: Years 15-25
> **Outputs**: yarn at industrial scale (10-100× hand spinning)
> **Critical**: Yes — mechanized spinning breaks the hand-spinning bottleneck that limits cloth production to the pace of individual spinners

## Overview

Mechanized spinning replaces hand drafting and twisting with powered rollers and high-speed spindles. Three systems dominate industrial spinning, each suited to different yarn types and production needs:

- **[Water Frame](spinning-frame-water.md)** (Arkwright, 1769) — Roller drafting with flyer winding. Produces firm, even warp yarn. The first mechanized spinning system to achieve commercial success. Spindle speed 4,000-6,000 rpm, yarn count Ne 10-40.

- **[Spinning Mule](spinning-frame-mule.md)** (Crompton, 1779) — Combines roller drafting with carriage travel. Produces the finest, most uniform yarn of any system (Ne 20-200+). Mechanically complex; self-acting mule has 100+ moving parts.

- **[Ring Frame](spinning-frame-ring.md)** (Thorpe, 1828) — Traveler-and-ring system with continuous motion. Simplest mechanism, highest production rate. Dominant since 1900 (~80% of cotton yarn then, ~70% of short-staple today). Spindle speed up to 15,000 rpm.

## Shared Prerequisites

All three spinning frame types share the same core dependencies:

- [Precision machining](../machine-tools/machining.md) — rollers bored and ground to ±0.02 mm, spindles turned true
- [Iron & Steel](../metals/iron-steel.md) — cast iron frames, forged steel rollers, hardened steel rings and travelers
- [Bearings](../machine-tools/bearings-abrasives.md) — reliable plain or roller bearings for high-speed spindles (3,000-15,000 rpm)
- [Power source](../energy/index.md) — water wheel (original), steam engine (19th century), or electric motor (20th century)
- [Spinning](spinning.md) — fiber preparation (carding, combing, roving) as input to the frame

## Shared Safety Concerns

- **High-speed spindles**: All frame types spin at 4,000-15,000 rpm. Guard spindle rails. Inspect for cracks before each shift.
- **Entanglement**: Loose clothing, hair, or jewelry caught in rotating parts causes severe injury. Guard all belts and gears.
- **Dust and fly**: Fiber dust causes byssinosis ("brown lung"). Ventilate spinning rooms. Wear dust masks.
- **Noise**: Ring frames at 10,000+ rpm generate 85-95 dB. Hearing protection required.

## See Also

- [Water Frame](spinning-frame-water.md) — detailed water frame construction and operation
- [Spinning Mule](spinning-frame-mule.md) — detailed mule construction and operation
- [Ring Frame](spinning-frame-ring.md) — detailed ring spinning construction and operation
- [Spinning](spinning.md) — hand spinning methods, fiber preparation, twist and yarn properties
- [Weaving](weaving.md) — loom-based cloth production from spun yarn
- [Carding Machine](carding-machine.md) — fiber preparation for spinning frame feed
- [Machine Tools](../machine-tools/index.md) — precision machining for rollers and spindles
- [Energy](../energy/index.md) — power sources for driving spinning frames

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Textiles](./index.md) • [All Domains](../../index.md)*
