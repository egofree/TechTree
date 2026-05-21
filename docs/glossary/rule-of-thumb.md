# Rule of Thumb

> **Type**: heuristic | **Tier**: operational | **Domains**: silicon, vlsi-scaling

Keep foreline piping between the vacuum chamber and the pump as short and wide as practical. A 1 m length of 25 mm ID pipe has a molecular flow conductance of ~30 L/s for N₂. If the pump has a speed of 300 L/s but is connected through this pipe, the effective pumping speed at the chamber is only ~27 L/s. The pipe chokes the pump. Double the pipe diameter → four times the conductance.

## Context in the Tech Tree

Rules of thumb are practical heuristics — simplified design guidelines that capture complex engineering relationships in memorable form. They are not exact, but they prevent the most common mistakes. In [Vacuum Systems](../vlsi-scaling/vacuum-systems.md), the rule about foreline piping prevents a frequent error: buying a large pump and then choking it with narrow, long piping. In [Heat Treatment](../metals/iron-steel.md), rules of thumb guide soak times (1 hour per inch of section thickness) and quench selection (water for plain carbon, oil for alloy steels). In [Casting](../machine-tools/casting.md), rules guide riser sizing (riser volume must exceed the shrinkage volume of the casting section it feeds).

## Technical Details

The foreline piping rule illustrates the physics behind a rule of thumb. In molecular flow regime (high vacuum, where gas molecules travel wall-to-wall without colliding with each other), conductance through a pipe scales with the cube of the diameter and inversely with length. The effective pumping speed at the chamber is given by: 1/S_effective = 1/S_pump + 1/C_pipe, where C_pipe is the conductance. When C_pipe << S_pump, the pipe dominates — the expensive pump becomes irrelevant.

The practical implication: always use the shortest, widest practical foreline. Double the pipe diameter and conductance increases by 4× (actually closer to d³/L for long pipes, but the "double diameter = quadruple conductance" rule is close enough for planning). A 50 mm pipe has roughly 4× the conductance of a 25 mm pipe, turning an effective pumping speed of 27 L/s into ~120 L/s — a dramatic improvement for the cost of a larger pipe fitting.

Other tech tree rules of thumb: furnace power scales as ~500 kWh per tonne of silicon (for planning power supply), blast furnace production scales roughly with hearth diameter squared, and a good earth ground for telegraph has <5 Ω resistance (measure with three-point fall-of-potential test). These heuristics are not substitutes for detailed engineering calculation, but they enable quick feasibility estimates during planning.

## Related Terms

- [Principle](./principle.md) — the underlying physics that rules of thumb approximate
- [Process Parameters](./process-parameters.md) — the exact values that rules of thumb estimate
- [Procedure](./procedure.md) — formal steps where rules of thumb inform judgment calls

## Appears In

- [Vacuum Systems](../vlsi-scaling/vacuum-systems.md)
- [Iron & Steel Production](../metals/iron-steel.md)
- [Casting](../machine-tools/casting.md)
