# Surface Preparation

> **Type**: noun | **Tier**: critical | **Domains**: chemistry, gas-handling, metals

The cleaning, degreasing, and activation of surfaces before coating, plating, bonding, or vacuum use. Poor surface preparation is responsible for 80-90% of premature coating and bond failures — it is the single most important step in any surface treatment process.

## Context in the Tech Tree

Surface preparation appears in [Electrolysis](../chemistry/electrolysis.md) for electrode preparation, [Vacuum Systems](../gas-handling/vacuum.md) for chamber internals, and [Finishing](../metals/finishing.md) for paint and plating adhesion. In each case, the quality of surface preparation directly determines the quality and longevity of the final result.

## Technical Details

For painting and plating, the standard preparation sequence is: degrease (alkaline soak or solvent wash) → acid pickle (remove oxide scale) → acid dip (activate surface) → rinse between each step → dry before coating. Abrasive blast cleaning to Sa 2.5 (near-white metal per ISO 8501-1) using angular grit at 0.4-0.7 MPa creates a 50-100 µm anchor profile for mechanical adhesion of paint. The blast profile gives the coating something to grip.

For vacuum chambers, surface preparation is equally critical but different: internal surfaces are electropolished (concentrated sulfuric-phosphoric acid electrolyte dissolves a thin layer, enriching surface chromium and reducing effective surface area by ~50%). Components are then cleaned with acetone followed by isopropyl alcohol, blown dry with oil-free nitrogen, wrapped in clean aluminum foil, and handled only with nitrile gloves. Bake-out at 150-400°C during initial pump-down accelerates outgassing by 10-100×.

For plating, surface preparation follows the same degrease-pickle-activate sequence but with tighter tolerances. Any oil or oxide residue prevents adhesion. A water-break test (continuous water film, no beading) confirms a clean surface before plating begins.

## Related Terms

- [Disadvantages](./disadvantages.md) — what happens without proper preparation
- [Advantages](./advantages.md) — benefits of thorough preparation
- [Principle](./principle.md) — principles behind surface preparation

## Appears In

- [Electrolysis](../chemistry/electrolysis.md)
- [Vacuum](../gas-handling/vacuum.md)
- [Finishing](../metals/finishing.md)
