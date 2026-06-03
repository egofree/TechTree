# Anvil

> **Node ID**: machine-tools.anvil
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.casting`](casting.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 5-15
> **Outputs**: forged_parts, shaped_metal
> **Critical**: Yes — the anvil is the single most important tool in the smithy; every forged part begins on the anvil face

## Principle

An anvil is a massive, hard, flat-topped block that provides a rigid surface against which metal is shaped by hammering. The anvil face absorbs and returns hammer energy — a hard, flat surface reflects energy back into the workpiece, making each blow more effective. The anvil mass (20-200 kg) must greatly exceed the hammer mass (1-8 kg) so that the anvil does not move significantly under impact. The ratio of anvil mass to hammer mass should be at least 20:1 for efficient forging. The standard London-pattern anvil provides a flat face for general hammering, a rounded horn for bending curves, a step (shoulder) for supporting work at the edge, and a hardy hole (square) and pritchel hole (round) for holding tooling.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Wrought iron or cast steel (body) | 50-150 kg | Single block, London or double-horn pattern | [Iron & Steel](../metals/iron-steel.md) | Granite or basalt boulder (earliest stage) |
| High-carbon steel (face plate) | 5-15 kg | 0.8-1.0% C, 10-20 mm thick, welded to body top | [Iron & Steel](../metals/iron-steel.md) | Carburized wrought iron face (thinner hard layer) |
| Hardwood stump (base) | 1 | Oak or ash, 400-500 mm diameter × 600-700 mm tall | [Foundations](../foundations/tools-basic.md) | Steel stand (heavier, no shock absorption) |
| Steel spikes or bolts (mounting) | 4-6 | 12-16 mm diameter, 200 mm long | [Iron & Steel](../metals/iron-steel.md) | Chain or iron straps (less rigid) |

## Prerequisites

- [Iron production](../metals/iron-steel.md) — wrought iron or cast steel for the body
- [High-carbon steel](../metals/iron-steel.md) — for the hardened face plate
- [Casting capability](casting.md) — if casting the body from cast steel
- [Forge welding capability](joining.md) — for welding the face plate to the body
- [Heat treatment capability](../metals/iron-steel.md) — for hardening and tempering the face

## Construction Steps

### Stone Anvil (Earliest Stage)

1. **Select a suitable stone**: Find a large granite or basalt boulder (50+ kg) with a naturally flat top surface. The stone should be at least 300 mm wide × 400 mm long on the top face, with enough mass to resist moving under hammer blows.
2. **Dress the face**: Chip the top surface flat with another hard stone. The flat area should be at least 200 × 200 mm. A flat surface is essential — convexity causes workpieces to skitter off under hammering.
3. **Set the anvil**: Bury the base of the boulder in packed earth or embed in a heavy timber frame so it does not shift during use. The working height should be approximately knuckle-height when the smith stands beside it (650-750 mm).

The stone anvil bounces hammer energy poorly and chips under repeated steel hammering, but it is sufficient for copper, bronze, and early iron work. Plan to upgrade to an iron anvil as soon as iron production allows.

### Iron Anvil with Steel Face (Primary Build)

4. **Cast or forge the body**: Cast the body from cast steel (preferred for uniformity) or forge from wrought iron. The London-pattern body has: a flat top (face) area 100-150 mm wide × 300-400 mm long, a conical horn extending 200-300 mm from one end, a flat step (table) between the face and horn, and a waist leading to a base with two feet. Overall length: 500-700 mm. Overall height: 200-250 mm. Weight: 50-150 kg.
5. **Prepare the face plate**: Forge a plate of high-carbon steel (0.8-1.0% C) to the dimensions of the face area: 100-150 mm wide × 300-400 mm long × 10-20 mm thick. The face plate must be flat and of uniform thickness. Grind the bottom face smooth for good contact with the body.
6. **Forge-weld the face plate to the body**: Heat the body top surface and the face plate bottom to bright yellow-white (~1300°C). Apply borax flux. Place the face plate on the body top and strike firmly with a sledge hammer to forge-weld the two together. Work from the center outward to expel flux and scale. Multiple heats may be needed for a complete weld. The face plate must be fully bonded to the body — any voids cause the face to ring dead (dull sound) and eventually crack.
7. **Drill the hardy and pritchel holes**: After the face is welded and cooled, drill a square hole (hardy hole, 25-30 mm square) through the face and body near the horn end. Drill a round hole (pritchel hole, 12-16 mm diameter) between the hardy hole and the horn. These holes hold tooling (hardy cutters, swages, pritchel punches) during use.
8. **Heat-treat the face**: Heat the entire face plate to 780-820°C (cherry red for 0.8-1.0% C steel). Quench in oil (not water — the thin face plate on the heavy body creates severe thermal stress). Temper immediately at 250-300°C for 1-2 hours to 55-60 HRC. The face should be hard enough to resist denting from hammer blows but not so hard that it chips. Test with a file: the file should skate on the face without cutting.
9. **Grind the face flat**: Grind the hardened face flat and true. The face must be flat within 0.1 mm over its full length and free of visible hammer marks from the forge-welding. Use a surface grinder if available, or hand-grind with a large abrasive stone. Polish to a smooth finish (1-3 μm Ra) — roughness marks workpieces.
10. **Mount the anvil on a stump**: Select a hardwood stump (oak or ash, 400-500 mm diameter × 600-700 mm tall). Cut the top flat. Cut a recess in the top matching the anvil base footprint to 10-20 mm depth — the anvil seats in this recess and cannot shift. Secure with steel spikes driven through holes in the anvil feet into the stump, or with iron straps bolted across the feet. The working height (face top to floor) should be knuckle-height: 650-750 mm for a standing smith.

## Calibration and Verification

1. **Ring test**: Strike the face lightly with a hardened steel hammer. A good anvil produces a clear, sustained ring (~2-3 seconds). A dead, dull sound indicates a crack in the body or a poorly bonded face plate — the anvil will not return energy efficiently.
2. **Flatness check**: Place a precision straightedge across the face. No gap should exceed 0.1 mm. Check along the length, across the width, and diagonally.
3. **Hardness test**: Attempt to file the face with a standard bastard-cut file. The file must not cut — if it does, the face is undertreated and will dent in service. Target: 55-60 HRC.
4. **Rebound test**: Drop a 25 mm steel ball bearing from 300 mm onto the face. It should rebound to at least 200 mm (67% rebound ratio). Lower rebound indicates a soft face or a poorly bonded plate. This test characterizes the anvil's energy return.
5. **Stability test**: Strike the anvil face with a 4 kg sledge at full swing. The anvil must not shift, rock, or move on its stump. If it moves, re-secure the mounting.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Face hardness | 55-60 HRC |
| Face flatness | ±0.1 mm over face length |
| Rebound ratio | 65-80% (steel ball test) |
| Working height | 650-750 mm (face to floor) |
| Face dimensions | 100-150 mm wide × 300-400 mm long |
| Horn length | 200-300 mm |
| Hardy hole | 25-30 mm square |
| Pritchel hole | 12-16 mm round |
| Weight | 50-150 kg (100+ kg preferred) |
| Service life | Decades to centuries (face may need re-grinding every 5-10 years) |
| Minimum anvil-to-hammer mass ratio | 20:1 |

## Strengths

- Returns hammer energy efficiently — a hard face with a massive body makes each blow productive
- Versatile — flat face for general work, horn for bending curves, hardy hole for tooling, step for chiseling
- Service life measured in decades — a well-maintained anvil outlasts generations of smiths
- Stone anvils require no metallurgy — available at the earliest stage of metalworking

## Weaknesses

- Iron anvil production itself requires advanced forging capability — a bootstrapping challenge (need iron to make the tools to work iron)
- Heavy and immobile once mounted — not a portable tool
- Face plate forge-welding is a critical operation — a poor weld produces a dead-sounding anvil that absorbs rather than returns energy
- Hardened face is brittle — never strike the face directly with hardened steel tools (chisels, punches). Strike only on the step or use a soft (copper or brass) drift between the tool and the face

## Safety

- **Heavy lifting**: A 100 kg anvil requires 2-3 people or a hoist to position. Never lift alone. Secure the anvil to its stump before working — a falling anvil is lethal.
- **Hammer rebound**: A glancing blow can send the hammer rebounding toward the operator. Maintain a firm, two-handed grip on the hammer.
- **Hot metal on anvil**: Scale and hot metal fragments fly off under hammering. Safety glasses (ANSI Z87.1) mandatory.
- **Noise**: Sustained hammering on an anvil produces noise levels of 95-110 dB. Hearing protection recommended for extended forging sessions.

## See Also

- [Forming](forming.md) — forging operations performed on the anvil
- [Iron & Steel](../metals/iron-steel.md) — iron and steel production for anvil construction
- [Casting](casting.md) — casting the anvil body
- [Joining](joining.md) — forge-welding the face plate to the body
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence

[← Back to Machine Tools](index.md)
