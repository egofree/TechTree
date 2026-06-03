# Wire Drawing Die (Draw Plate)

> **Node ID**: machine-tools.wire-drawing-die
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 10-20
> **Outputs**: wire, drawn_rod
> **Critical**: Yes — wire drawing produces the copper wire for generators, motors, and transformers; no substitute process exists for making long, uniform-diameter wire

## Principle

Wire drawing pulls metal rod through a die (hardened steel plate with tapered holes) of progressively smaller diameter. Each die reduces the cross-section by 15-25% and elongates the wire proportionally. The die entrance bell (30° included angle) guides the metal into the bearing section (short, straight, ~1× diameter long), where the actual reduction occurs. The back-relief angle prevents the drawn wire from scoring the die exit. Drawing is performed cold — the metal work-hardens with each pass, increasing tensile strength by 50-100%. Annealing every 3-5 passes restores ductility for further reduction.

The draw plate is the bootstrap form of wire drawing dies: a single hardened steel plate with multiple tapered holes graduating in size from 8.0 mm down to 1.0 mm. It requires no specialized die-making equipment — only a drill, reamers, and heat treatment capability.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| High-carbon steel plate | 1 | 0.8-1.0% C, 15 mm thick × 100 mm × 200 mm | [Iron & Steel](../metals/iron-steel.md) | Tool steel (O1, D2 — better wear life, harder to source) |
| Tapered reamer | 1 | 30° included angle | [Machining](machining.md) | Ground and polished punch (less precise) |
| Straight reamer set | 1 set | 1.0-8.0 mm in 0.5 mm steps | [Machining](machining.md) | Precision-ground drill bits (oversized by 0.1-0.2 mm) |
| Quenching oil | 2-5 L | Mineral oil or vegetable oil | [Lubricants](../chemistry/lubricants.md) | Brine (faster cooling, higher cracking risk) |
| Abrasive paste | 1 set | 180, 320, 600, 1200 grit | [Bearings & Abrasives](bearings-abrasives.md) | Natural emery + oil (slower but functional) |
| Tapered mandrel (polishing) | 1 set | Hardwood or steel, matching die sizes | [Machining](machining.md) | Wrapped dowel with abrasive paper |

## Prerequisites

- [High-carbon steel](../metals/iron-steel.md) — for the die plate (must be through-hardenable to 58-62 HRC)
- [Drilling and reaming capability](machining.md) — for creating precise, tapered holes
- [Heat treatment capability](../metals/iron-steel.md) — hardening and tempering to 58-62 HRC
- [Abrasive polishing capability](bearings-abrasives.md) — for finishing die holes to mirror smoothness

## Construction Steps

1. **Prepare the plate**: Start with a flat plate of high-carbon steel (0.8-1.0% C), 15 mm thick × 100 mm × 200 mm. Mill or grind both faces flat and parallel to 0.05 mm. The faces must be flat for uniform die performance.
2. **Mark hole positions**: Layout two rows of holes, spaced 15 mm apart center-to-center, 15 mm from the edges. Mark hole diameters from 8.0 mm down to 1.0 mm in 0.5 mm steps. Smaller holes toward one end; larger toward the other. A plate with 15 holes covers the range 8.0 mm to 1.0 mm in 0.5 mm increments.
3. **Drill undersized holes**: Drill each hole 0.3 mm undersize using a drill press. Use the appropriate drill bit for each diameter. Maintain perpendicularity — the hole axis must be perpendicular to the plate face within 0.05 mm over the 15 mm plate thickness.
4. **Ream to final diameter**: Ream each hole to final diameter tolerance ±0.02 mm with a straight reamer. The straight section through the full plate thickness serves as the bearing land.
5. **Form the entrance bell**: On one face of the plate, use a tapered reamer (30° included angle) to countersink each hole to approximately 2-3 mm depth. This creates the entrance bell that guides the wire into the bearing section. The transition from bell to bearing must be smooth — a sharp step causes wire marking.
6. **Form the back relief**: On the opposite face, countersink each hole with a 45° countersink to 0.5 mm depth. This prevents the drawn wire from contacting the die exit edge.
7. **Harden the plate**: Heat the entire plate to 780-820°C in a furnace or forge (cherry red for 0.8-1.0% C steel). Soak for 15-20 minutes at temperature for uniform austenitization. Quench in oil (not water — high-carbon steel cracks in water). Agitate during quenching to break the vapor blanket.
8. **Temper**: Reheat to 200-250°C for 1-2 hours. This tempers the martensite to 58-62 HRC while retaining most of the as-quenched hardness. The die must be hard enough to resist wear but not so hard that it chips.
9. **Polish the die holes**: This is the critical finishing step. Wrap 180-grit abrasive paper around a tapered hardwood mandrel and work each hole to remove scale and roughness from heat treatment. Progress through 320, 600, and finish with 1200 grit paste. The bearing surface (straight section) must be mirror-smooth — any roughness causes galling and increases draw force. Inspect with a 10× loupe: the surface should show no visible scratches or tool marks.

## Calibration and Verification

1. **Pin gauge test**: Pass a precision-ground steel pin (known diameter, ±0.01 mm) through each die hole. The pin should pass through with light finger pressure — if it requires force, the die is undersized; if it falls through freely, the die is oversized. Record the actual diameter for each hole.
2. **Wire test**: Draw a short length of copper wire through each successive die. Measure the wire diameter before and after each pass with a micrometer (0.01 mm resolution). The actual reduction should match the calculated reduction within ±2%. If the wire tears or galls, the die surface needs more polishing.
3. **Pull force measurement**: For a reference wire diameter and material, measure the pull force with a spring scale. Normal draw force for copper wire is: F = σ_y × A × ln(A₀/A_f), where A₀ is the initial area and A_f is the final area. If the measured force exceeds the calculated force by more than 20%, the die has excessive friction (insufficient polish or wrong entrance angle).

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Reduction per pass | 15-25% area reduction |
| Wire diameter tolerance | ±0.05 mm per die |
| Die life (soft metals — copper, brass) | 200-500 passes before hole enlarges beyond tolerance |
| Die life (hard metals — iron, steel) | 50-200 passes |
| Pull force (copper, 3 mm → 2.5 mm) | 5-15 kN |
| Pull force (steel, 3 mm → 2.5 mm) | 15-30 kN |
| Minimum wire diameter (steel die) | 1.0 mm |
| Minimum wire diameter (tungsten carbide die) | 0.1 mm |
| Number of holes per plate | 10-20 (graduated sizes) |

## Strengths

- Simple equipment — a hardened steel plate and pulling force suffice for bootstrap wire production
- Produces wire with precise, consistent diameter (±0.05 mm per die)
- Cold drawing work-hardens the wire, increasing tensile strength by 50-100%
- One plate covers a wide range of wire diameters

## Weaknesses

- Requires annealing every 3-5 passes to prevent work-hardening embrittlement — adds time and fuel cost
- Die wear causes diameter drift — dies must be monitored and replaced periodically
- Maximum single-pass reduction is limited to 25% — many passes needed for large diameter changes
- Steel dies wear faster than tungsten carbide inserts on high-volume production

## Draw Bench (for Wire > 2 mm)

A draw bench provides the mechanical advantage to pull wire through dies when hand force is insufficient:

- **Chain-driven draw bench**: A heavy chain runs along a 2-3 m long bed. A gripping jaw on the chain grabs the pointed end of the wire. A hand-cranked or powered sprocket drives the chain, pulling the wire through the die mounted at the head of the bench. Pull force: 10-50 kN.
- **Capstan draw bench** (for fine wire < 2 mm): The wire wraps multiple turns around a rotating drum (capstan). Friction between the wire and drum provides the pulling force. Speed: 30-100 m/min for copper. The wire exits the capstan and is coiled on a take-up spool.

## Safety

- **Whipping wire**: Wire under tension can snap and whip violently. Stand to the side of the draw line, never in line with the wire. Wear safety glasses.
- **Pinch points**: The draw bench chain and die mounting create pinch hazards. Keep hands clear of the chain drive.
- **Sharp ends**: Pointed wire ends (for threading through dies) are sharp. Handle with gloves or pliers.

## See Also

- [Forming](forming.md) — wire drawing procedures and annealing schedules
- [Machining](machining.md) — drilling and reaming operations for die construction
- [Bearings & Abrasives](bearings-abrasives.md) — abrasive polishing materials for die finishing
- [Iron & Steel](../metals/iron-steel.md) — high-carbon steel for die plate material
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence

[← Back to Machine Tools](index.md)
