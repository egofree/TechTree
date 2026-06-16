# Propellant Casting

> **Node ID**: launch-vehicles.solid-propulsion.propellant-casting
> **Domain**: [Launch Vehicles](./index.md)
> **Dependencies**: [`launch-vehicles.solid-propulsion`](./solid-propulsion.md)
> **Enables**: None
> **Timeline**: Years 30-200+
> **Outputs**: cast_propellant
> **Critical**: No

Propellant casting is the mixing and pouring of composite solid propellant into the motor case around a shaped mandrel, then oven-curing the binder into a rubbery solid grain bonded to the case wall. This process is part of the [Solid Propulsion](./solid-propulsion.md) capability.

## Composite Propellant Formulation

The standard AP/Al/HTPB composite (68% AP / 16% Al / 14% HTPB + 2% additives):

| Component | Role | Mass Fraction |
|-----------|------|---------------|
| Ammonium perchlorate (AP) | Oxidizer | 65-70% |
| Aluminum powder (Al) | Metallic fuel | 14-18% |
| HTPB binder | Binder / fuel | 12-16% |
| Additives (Fe₂O₃, plasticizer, bonding agent) | Modifiers | ~2% |

## Casting Sequence

1. **Mixing**: blend AP (ground and classified to target particle size), aluminum powder, HTPB binder, plasticizer, and additives in a vertical planetary mixer under vacuum (to remove entrained air). Batch sizes up to 3,400 kg per mix.
2. **Casting**: pump the propellant slurry into the case around the mandrel, in incremental layers. Vacuum-assist during pour removes residual bubbles. The Shuttle SRB required ~150 batches per motor.
3. **Cure**: oven at 50-60°C for 3-7 days. The isocyanate cure agent (IPDI) cross-links the HTPB polymer chains into a solid rubber matrix.
4. **Mandrel removal**: extract the collapsible mandrel (multi-piece for star/finocyl shapes), leaving the finished port geometry.

## Safety

A mixing bowl of composite propellant contains more energy than an equivalent mass of TNT. Mixing and casting are done remotely, behind blast walls. Electrostatic discharge (ESD) is a hazard during dry-AP handling — all equipment is grounded, operators wear conductive gear. AP decomposes exothermically above 240°C; fire near a casting facility is a mass-burning (1.3 explosive) hazard.

## Quality Assurance

After cure, the grain is X-rayed for voids and cracks, ultrasonically C-scanned for propellant-case debonds, and bore-inspected for port-geometry conformance. Any void larger than a few centimeters or any debond larger than a few centimeters is a reject or rework condition.

See [Grain Design](./solid-propulsion.grain-design.md) for the mandrel geometry and [Solid Propulsion](./solid-propulsion.md) for the full capability.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Launch Vehicles](./index.md) • [All Domains](../index.md)*
