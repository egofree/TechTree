# Rubber Compounding

> **Node ID**: transport.tire-manufacturing.rubber-compounding
> **Domain**: [Transport](./index.md)
> **Dependencies**: [`transport.tire-manufacturing`](tire-manufacturing.md)
> **Timeline**: Years 20-40+
> **Outputs**: tire_cord
> **Critical**: No

Rubber compounding is the formulation and mixing step that turns raw elastomers into a usable engineering material. A Banbury internal mixer (counter-rotating rotors in a hardened steel chamber) blends natural rubber, SBR, and polybutadiene with carbon black, silica, processing oils, antioxidants, accelerators, and sulfur in a precisely sequenced 3-5 minute batch at 130-160 C. Mixing order matters: silica and silane must be added early (high temperature for the coupling reaction), while sulfur and accelerator go in last (a "productive" or final mix at <110 C) to avoid scorch — premature cross-linking in the mixer.

## Calendering and Ply Stock

After mixing, the compound is sheeted on a two-roll mill and fed to a **calender** — a stack of 3-4 large precision-rolled steel cylinders. The calender forces the rubber into a uniform 0.5-2 mm sheet, or sandwiches it onto textile cord fabric to produce **rubberized ply stock** (the body plies and belt plies used downstream in tire building). Calendering tolerance is ±0.05 mm — variation here becomes uniformity and imbalance problems in the finished tire.

## Compound Families

A single tire uses 6-12 distinct compounds (tread, sidewall, inner liner, bead filler, etc.), each mixed separately and tailored to its job. The tread compound — where the magic triangle of rolling resistance, wear, and grip is fought — is the most fiercely engineered.

## Prerequisites

- [Polymers](../polymers/index.md) — natural and synthetic rubber supply
- [Chemistry](../chemistry/index.md) — carbon black, silica, accelerators, antioxidants
- [Textiles](../textiles/index.md) — dipped cord fabric for calendering

## See Also

- [Tire Manufacturing](tire-manufacturing.md) — parent capability overview
- [Tire Building](tire-manufacturing.tire-building.md) — consumes the calendered ply stock

---

*Part of the [Bootciv Tech Tree](../index.md) • [Transport](./index.md)*
