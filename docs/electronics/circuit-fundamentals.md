# Circuit Fundamentals

> **Node ID**: electronics.circuit-fundamentals
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`electronics.passive-components`](passive-components.md), [`electronics.electrical-systems`](electrical-systems.md)
> **Timeline**: Years 15-30
> **Outputs**: circuit-analysis
> **Critical**: No — circuit theory is analytical knowledge, not a physical bottleneck; a practiced practitioner can derive results from memory once components exist

Circuit fundamentals is the body of theory that lets you predict what a network of components will do *before* you build it. It does not manufacture anything itself — it is the analytical lens applied to the outputs of [Passive Components](passive-components.md) and [Electrical Systems](electrical-systems.md). Without it, every circuit is built by trial and error; with it, a designer can specify resistor, capacitor, and inductor values on paper and expect a working prototype on the first build.

This capability is the family hub for the DC and AC theory articles that follow. It does not duplicate the component-construction knowledge in [Passive Components](passive-components.md) (which covers how to *make* resistors, capacitors, and inductors) nor the power-distribution knowledge in [Electrical Systems](electrical-systems.md). Instead, it assumes those components exist and asks: given a bag of parts, how do we reason about the voltages and currents in any interconnection?

## What This Hub Covers

The progression below is the standard pedagogical order. Each layer extends the previous one and is documented in its own process article (linked where it exists).

1. **DC fundamentals** — voltage, current, resistance; Ohm's law (`V = IR`); power (`P = VI`); series and parallel combinations; voltage and current dividers. The algebra of circuits that do not change over time. *(Process article: dc-analysis — forthcoming.)*

2. **Network analysis** — Kirchhoff's voltage law (KVL) and current law (KCL); node-voltage and mesh-current methods; solving linear systems of 2–N unknowns by hand. These are the universal tools that work on *any* linear circuit, no matter how many branches.

3. **Network theorems** — Thévenin and Norton equivalent circuits (collapse any two-terminal linear network to a single source and impedance); superposition; maximum power transfer; source transformation. These reduce complex networks to simpler models and are used constantly in amplifier, filter, and power-supply design.

4. **Energy storage elements** — capacitors and inductors as elements that store energy in electric and magnetic fields; the `v-i` relationships `i = C·dv/dt` and `v = L·di/dt`; the concept of a *time-varying* response and natural/forced response of first-order RC and RL circuits.

5. **AC fundamentals** — sinusoidal sources; the phasor transform (represent a sinusoid as a complex number); reactance (`X_C = 1/(2πfC)`, `X_L = 2πfL`); impedance `Z = R + jX`; AC power (real, reactive, apparent); RMS values. *(Process article: ac-analysis — forthcoming.)*

6. **Frequency response** — transfer functions; Bode plots; first- and second-order filters (low-pass, high-pass, band-pass); resonance in series and parallel RLC circuits; bandwidth and Q.

## Prerequisites at a Glance

| Prereq | Why it is needed |
|--------|------------------|
| [Passive Components](passive-components.md) | Provides the physical R, L, C parts whose behavior circuit theory models. You cannot analyze what you cannot identify. |
| [Electrical Systems](electrical-systems.md) | Provides voltage/current sources, wiring, and meters — the bench equipment that turns theory into measurable results and the sources that excite the circuits being analyzed. |

## Relationship to Other Electronics Capabilities

Circuit fundamentals is *not* a prerequisite in the bootstrap dependency chain the way metallurgy or chemistry is — components must exist before theory is useful. It is, however, a prerequisite in the *knowledge* chain: every later electronics capability (active circuits, power converters, oscillators, amplifiers) is designed using these analytical tools. The forthcoming process articles `dc-analysis` and `ac-analysis` will live under this capability and provide the worked examples, schematics, and quantitative parameter tables that this hub deliberately omits.

## Why This Is Era `industrial`, Not `electronic`

DC and AC circuit theory was essentially complete by the late 19th century — Ohm (1827), Kirchhoff (1845), Thévenin (1883), Steinmetz's phasor method (1893). It belongs to the same era as dynamos, telegraphs, and incandescent lighting. The `electronic` era (tubes, transistors, integrated circuits) builds *on top of* this foundation but does not redefine it. Marking the era as `industrial` keeps the timeline honest: a civilization with copper wire, batteries, and galvanometers can derive and verify all of this material.

## See Also

- [Passive Components](passive-components.md) — the physical R, L, C parts this theory analyzes
- [Electrical Systems](electrical-systems.md) — sources, wiring, and measurement instruments
- [Power Electronics](power-electronics.md) — application of circuit theory to switching converters
- [Semiconductor Devices](../silicon/basic-devices.md) — active devices whose bias networks are designed with this theory

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](index.md)*
