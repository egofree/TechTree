# Anvil

> **Node ID**: machine-tools.anvil
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.casting`](../metals/casting.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 5-15
> **Outputs**: forged_parts, shaped_metal
> **Critical**: Yes — the anvil is the single most important tool in the smithy; every forged part begins on the anvil face

## Overview

![Anvil, 5 kg in a jewellery workshop](../images/machine-tools/machine-tools_anvil.jpg)

> *Anvil, 5 kg in a jewelry workshop. Studio photography made in the shop/workshop of Sophies Silver (Swedish spelling), Sankt Hansgatan 34, Visby, Gotland, Sweden.*

> *Image: W.carter, CC BY-SA 4.0*

An anvil is a massive, hard, flat-topped block that provides a rigid surface against which metal is shaped by hammering. The anvil face absorbs and returns hammer energy — a hard, flat surface reflects energy back into the workpiece, making each blow more effective. The anvil mass (20-200 kg) must greatly exceed the hammer mass (1-8 kg) so that the anvil does not move significantly under impact. The ratio of anvil mass to hammer mass should be at least 20:1 for efficient forging. The standard London-pattern anvil provides a flat face for general hammering, a rounded horn for bending curves, a step (shoulder) for supporting work at the edge, and a hardy hole (square) and pritchel hole (round) for holding tooling.

The anvil is the foundational tool of the forge shop. Before the lathe, before the rolling mill, before any powered machine tool, the anvil enables a smith to shape hot metal into useful forms: tools, hardware, structural brackets, and machine components. In the bootstrap sequence, the anvil is needed at the earliest stage of metalworking — first as a stone block for copper and bronze work, then as an iron-faced anvil for steel forging. Every [forging operation](forming.md) described in this tech tree assumes a functional anvil.

This article covers the construction and setup of anvils at three bootstrap stages: stone anvil (earliest, no metallurgy required), wrought iron anvil with steel face (intermediate, requires [iron production](../metals/iron-steel.md)), and cast steel anvil (advanced, requires [casting](../metals/casting.md)). For forging operations performed on the anvil, see [Forming](forming.md).

The anvil face serves three distinct zones. The **primary face** (center, flat, polished) is where most hammering occurs — drawing, upsetting, and planishing. The **horn** provides a curved surface for bending circles, arcs, and scrolls. The **step** (table) between the face and horn has a sharp corner used for cutting with a chisel (the workpiece overhangs the step, and the chisel cuts against the edge). The hardy hole holds a range of tooling: hardy cutters (for cutting bar), swages (for shaping round or square cross-sections), and fullers (for grooving and shouldering). The pritchel hole supports punches for piercing holes in hot metal.

## Prerequisites

- [Iron production](../metals/iron-steel.md) — wrought iron or cast steel for the body (stone anvil requires no metallurgy)
- [High-carbon steel](../metals/iron-steel.md) — for the hardened face plate (0.8-1.0% C)
- [Casting capability](../metals/casting.md) — for casting the body from cast steel (or forge from wrought iron)
- [Forge welding capability](joining.md) — for welding the face plate to the body
- [Heat treatment capability](../metals/iron-steel.md) — for hardening and tempering the face
- [Grinding capability](bearings-abrasives.md) — for surfacing the face flat after heat treatment

## Bill of Materials

### Stone Anvil (Earliest Stage)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Granite or basalt boulder | 1 | 50+ kg, minimum 300 × 400 mm flat top | Natural | Any hard, dense stone with a flat face |
| Earth or timber (mounting) | — | Packed earth bed or heavy timber cradle | [Construction](../construction/index.md) | Steel stand (heavier, no shock absorption) |

### Iron Anvil with Steel Face (Primary Build)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Wrought iron or cast steel (body) | 50-150 kg | London or double-horn pattern, single block | [Iron & Steel](../metals/iron-steel.md) | Stack of heavy steel plates (welded, less mass) |
| High-carbon steel (face plate) | 5-15 kg | 0.8-1.0% C, 10-20 mm thick | [Iron & Steel](../metals/iron-steel.md) | Carburized wrought iron face (thinner hard layer) |
| Borax (forge welding flux) | 1-2 kg | Anhydrous borax | [Chemistry](../chemistry/index.md) | Sand (less effective flux) |
| Quenching oil | 5-10 L | Mineral oil or vegetable oil | [Chemistry](../chemistry/lubricants.md) | Brine (faster cooling, higher cracking risk) |
| Hardwood stump (base) | 1 | Oak or ash, 400-500 mm diameter × 600-700 mm tall | [Foundations](../foundations/tools-basic.md) | Steel stand (heavier, no shock absorption) |
| Steel spikes or bolts (mounting) | 4-6 | 12-16 mm diameter, 200 mm long | [Iron & Steel](../metals/iron-steel.md) | Chain or iron straps (less rigid) |

## Process Description

### Stone Anvil (Earliest Stage)

1. **Select a suitable stone**: Find a large granite or basalt boulder (50+ kg) with a naturally flat top surface. The stone should be at least 300 mm wide × 400 mm long on the top face, with enough mass to resist moving under hammer blows.
2. **Dress the face**: Chip the top surface flat with another hard stone. The flat area should be at least 200 × 200 mm. A flat surface is essential — convexity causes workpieces to skitter off under hammering.
3. **Set the anvil**: Bury the base of the boulder in packed earth or embed in a heavy timber frame so it does not shift during use. The working height should be approximately knuckle-height when the smith stands beside it (650-750 mm).

**Calibration**: Place a straightedge across the dressed face. Maximum gap: 1 mm. Drop a 200 g steel ball from 200 mm — it should bounce 50-80 mm (25-40% rebound). A stone anvil absorbs most energy, but this is acceptable for copper, bronze, and early iron work.

**Expected performance**: Face flatness: ±1 mm. Rebound ratio: 25-40%. Service life: months to years before chipping degrades the face. Suitable for copper, bronze, and soft iron only.

**Materials specifications**: Granite or basalt boulder, 50+ kg, with a naturally flat or dressable top face at least 200 × 200 mm.

The stone anvil bounces hammer energy poorly and chips under repeated steel hammering, but it is sufficient for copper, bronze, and early iron work. Plan to upgrade to an iron anvil as soon as iron production allows.

**Strengths**:
- No metallurgy required — find a suitable boulder and dress it with stone tools
- Available immediately at the start of metalworking, before any furnace or forge exists
- Sufficient mass (50-100 kg) provides a stable working platform for copper and bronze

**Weaknesses**:
- Very poor rebound ratio (25-40%) — most hammer energy is absorbed by the stone rather than returned to the workpiece
- Face chips and degrades under steel hammering — unsuitable for ferrous metals beyond early soft iron
- No hardy hole, pritchel hole, or horn — no tooling support, no bending curves, no punching capability

### Cast Steel Anvil (Advanced — Requires Casting)

11. **Cast the body from cast steel**: Use a sand mold shaped to the London pattern. The casting must be sound (no internal voids, no cold shuts). Inspect by ringing — a clear ring indicates a sound casting. The cast steel body eliminates the forge-welding step required for a wrought iron body and provides a more uniform base for the face plate.
12. **Machine the body**: Mill the top surface flat for face plate attachment. Drill the hardy and pritchel holes. Grind the horn smooth. The body should weigh 50-150 kg depending on the intended service.
13. **Follow steps 5-10** from the Iron Anvil section above for face plate attachment, heat treatment, grinding, and mounting.

**Strengths**:
- Uniform body from a single casting — no forge-welding required, eliminating the risk of face plate delamination
- Superior rebound ratio (70-85%) due to homogeneous steel structure throughout
- Can be produced in any shape or pattern (London, double-horn, continental) by changing the mold

**Weaknesses**:
- Requires a large steel casting capability (50-200 kg pour) with sound casting technique — internal voids ruin the anvil
- Sand mold preparation for the London pattern is complex (horn, waist, feet, hardy hole core)
- If the casting is defective (cold shuts, shrinkage cavities), the entire pour is wasted — high material risk

### Iron Anvil with Steel Face (Primary Build)

4. **Cast or forge the body**: Cast the body from cast steel (preferred for uniformity) or forge from wrought iron. The London-pattern body has: a flat top (face) area 100-150 mm wide × 300-400 mm long, a conical horn extending 200-300 mm from one end, a flat step (table) between the face and horn, and a waist leading to a base with two feet. Overall length: 500-700 mm. Overall height: 200-250 mm. Weight: 50-150 kg.
5. **Prepare the face plate**: Forge a plate of high-carbon steel (0.8-1.0% C) to the dimensions of the face area: 100-150 mm wide × 300-400 mm long × 10-20 mm thick. The face plate must be flat and of uniform thickness. Grind the bottom face smooth for good contact with the body.
6. **Forge-weld the face plate to the body**: Heat the body top surface and the face plate bottom to bright yellow-white (~1300°C). Apply borax flux. Place the face plate on the body top and strike firmly with a sledge hammer to forge-weld the two together. Work from the center outward to expel flux and scale. Multiple heats may be needed for a complete weld. The face plate must be fully bonded to the body — any voids cause the face to ring dead (dull sound) and eventually crack.
7. **Drill the hardy and pritchel holes**: After the face is welded and cooled, drill a square hole (hardy hole, 25-30 mm square) through the face and body near the horn end. Drill a round hole (pritchel hole, 12-16 mm diameter) between the hardy hole and the horn. These holes hold tooling (hardy cutters, swages, pritchel punches) during use.
8. **Heat-treat the face**: Heat the entire face plate to 780-820°C (cherry red for 0.8-1.0% C steel). Quench in oil (not water — the thin face plate on the heavy body creates severe thermal stress). Temper immediately at 250-300°C for 1-2 hours to 55-60 HRC. The face should be hard enough to resist denting from hammer blows but not so hard that it chips.
9. **Grind the face flat**: Grind the hardened face flat and true. The face must be flat within 0.1 mm over its full length and free of visible hammer marks from the forge-welding. Use a surface grinder if available, or hand-grind with a large abrasive stone. Polish to a smooth finish (1-3 μm Ra) — roughness marks workpieces.
10. **Mount the anvil on a stump**: Select a hardwood stump (oak or ash, 400-500 mm diameter × 600-700 mm tall). Cut the top flat. Cut a recess in the top matching the anvil base footprint to 10-20 mm depth — the anvil seats in this recess and cannot shift. Secure with steel spikes driven through holes in the anvil feet into the stump, or with iron straps bolted across the feet. The working height (face top to floor) should be knuckle-height: 650-750 mm for a standing smith.

**Calibration**: Strike the face lightly with a hardened steel hammer. A good anvil produces a clear, sustained ring (~2-3 seconds). A dead, dull sound indicates a crack in the body or a poorly bonded face plate. Drop a 25 mm steel ball bearing from 300 mm onto the face — it should rebound to at least 200 mm (67% rebound ratio). Place a precision straightedge across the face — no gap should exceed 0.1 mm.

**Expected performance**: Face hardness: 55-60 HRC. Face flatness: ±0.1 mm over face length. Rebound ratio: 65-80% (steel ball test). Service life: decades to centuries (face may need re-grinding every 5-10 years).

**Materials specifications**: High-carbon steel plate (0.8-1.0% C, 10-20 mm thick, 100-150 × 300-400 mm), wrought iron or cast steel body (50-150 kg), borax flux, quenching oil, hardwood stump (400-500 mm diameter).

**Strengths**:
- Does not require a large-capacity steel casting pour — wrought iron body can be forged from available stock
- Face plate can be replaced independently when worn — the body lasts centuries with periodic re-facing
- Well-documented technique used by smiths for millennia; forgiving of minor imperfections in the body

**Weaknesses**:
- Forge-welding the face plate to the body requires a large hearth (1300°C+) and multiple heats for full bonding
- Face plate delamination risk — incomplete welds create voids that eventually crack under repeated impact
- Rebound ratio (65-80%) is lower than a solid cast steel anvil due to the iron-steel interface absorbing energy

## Quantitative Parameters

### Anvil Specifications

| Parameter | Stone Anvil | Iron Anvil (50-75 kg) | Iron Anvil (100-150 kg) |
|-----------|------------|----------------------|------------------------|
| Weight | 50-100 kg | 50-75 kg | 100-150 kg |
| Face hardness | N/A (stone) | 55-60 HRC | 55-60 HRC |
| Face flatness | ±1 mm | ±0.1 mm | ±0.1 mm |
| Rebound ratio | 25-40% | 65-75% | 70-80% |
| Face dimensions | 200 × 200 mm min | 100 × 300 mm | 150 × 400 mm |
| Working height | 650-750 mm | 650-750 mm | 650-750 mm |
| Service life | Months to years | Decades | Centuries |
| Suitable metals | Copper, bronze, soft iron | All ferrous and non-ferrous | All ferrous and non-ferrous |

### Rebound and Energy Return

| Anvil Condition | Rebound Ratio | Energy Returned | Diagnosis |
|-----------------|---------------|-----------------|-----------|
| New, properly hardened | 70-80% | High | Optimal |
| Good used condition | 65-75% | Good | Acceptable |
| Face plate delaminating | 40-55% | Poor | Repair or replace |
| Stone anvil | 25-40% | Low | Expected for stone |
| Face dented or soft | <50% | Low | Re-harden or re-grind |

### Hardy Hole and Pritchel Hole Dimensions

| Anvil Weight | Hardy Hole (square) | Pritchel Hole (round) |
|--------------|--------------------|-----------------------|
| 50-75 kg | 20-25 mm | 10-12 mm |
| 75-120 kg | 25-28 mm | 12-16 mm |
| 120-200 kg | 28-32 mm | 16-20 mm |

### Anvil Types and Characteristics

| Type | Weight | Face Hardness | Rebound | Cost (labor) | Best For |
|------|--------|---------------|---------|-------------|----------|
| Stone boulder | 50-100 kg | N/A (stone) | 25-40% | Minimal | Copper, bronze, earliest iron |
| Railroad rail | 20-40 kg | 30-40 HRC (as-rolled) | 40-55% | Minimal | Light forging, bootstrap |
| Wrought iron + steel face | 50-150 kg | 55-60 HRC | 65-80% | High (forge welding) | All-purpose smithing |
| Cast steel + steel face | 50-200 kg | 55-60 HRC | 70-85% | Medium (casting) | Production forging |
| Block (no horn) | 50-200 kg | 55-60 HRC | 65-80% | Low (simple geometry) | Straight forging only |

## Scaling Notes

- A 50-75 kg iron anvil handles most hand-forging work for the bootstrap sequence: tools, hardware, brackets, and small structural parts. Start here.
- Scale to 100-150 kg when producing large forged components (crankshafts, axles, structural beams). The added mass returns more energy and resists movement under heavy sledge work.
- The minimum anvil-to-hammer mass ratio is 20:1 for efficient forging. A 4 kg sledge requires an 80+ kg anvil. A 1 kg hand hammer works well on a 50 kg anvil.
- Stone anvils are the earliest option and require no metallurgy. Use stone for copper and bronze work while iron production is being established. Transition to iron anvils as soon as wrought iron or cast steel is available.
- Double-horn anvils (horn on both ends) are preferred for production forging — one horn is always accessible regardless of the workpiece position. London-pattern (one horn, one heel) is more common and easier to cast.
- Anvil height affects forging efficiency: too low forces the smith to bend (back strain), too high reduces hammer swing. The correct height places the face at knuckle height when the smith stands beside it with arms relaxed.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Dead ring (dull thud when struck) | Face plate delaminated from body; crack in body | Re-forge-weld the face plate if accessible; check for cracks with dye penetrant; replace the anvil if the body is cracked |
| Face dents under hammer blows | Face plate too soft (undertreated) | Re-harden: heat face to 780-820°C, oil quench, temper at 250-300°C; verify hardness with file test (file should skate, not cut) |
| Anvil rings excessively (harsh, loud tone) | Face plate too hard; insufficient tempering | Re-temper at 300-350°C for 2 hours; a slightly softer face is better than a brittle one that chips |
| Anvil walks on stump during use | Stump recess too shallow; mounting loose | Deepen the stump recess to 20 mm; add iron straps bolted across the feet; re-drive mounting spikes |
| Face develops swayed (concave) surface | Normal wear from decades of center-face hammering | Re-grind flat; consider this a sign of a well-used, productive anvil — a concave face of 0.5 mm is still functional |
| Horn chips or cracks | Heavy hammering on the horn (horn is softer than face) | Avoid using the horn for heavy drawing; grind smooth any chips to prevent them from marking workpieces |
| Hardy hole walls deform | Oversized hardy tools forced into the hole | Make hardy tool shanks to fit with 0.1-0.3 mm clearance; do not drive hardy tools with a sledge |

## Safety

- **Heavy lifting**: A 100 kg anvil requires 2-3 people or a hoist to position. Never lift alone. Secure the anvil to its stump before working — a falling anvil is lethal.
- **Hammer rebound**: A glancing blow can send the hammer rebounding toward the operator. Maintain a firm, two-handed grip on the hammer. Never strike the hardened face directly with another hardened tool (chisel, punch) — use the step or a copper/brass drift between the tool and the face. Hardened steel-on-hardened steel contact produces flying steel chips at high velocity.
- **Hot metal on anvil**: Scale and hot metal fragments fly off under hammering. Safety glasses (ANSI Z87.1 impact rated) mandatory. Long-handled [forging tongs](forming.md) keep hands away from hot metal.
- **Noise**: Sustained hammering on an anvil produces noise levels of 95-110 dB. Prolonged exposure above 85 dB causes permanent hearing loss. Hearing protection (NRR 25+ earplugs or earmuffs) recommended for extended forging sessions.
- **Anvil stability**: An unsecured anvil can tip or shift during heavy hammering, creating a crush hazard. Verify the anvil is firmly seated in its stump recess and secured with spikes or straps before each session.
- **Hot scale accumulation**: Oxide scale flakes off hot steel during forging and accumulates on the anvil face and floor. Scale is a slip hazard and a fire hazard — sweep the area regularly. Scale in the eye causes corneal abrasion — wear safety glasses at all times in the forge area.
- **Quenching oil fire risk**: During face plate heat treatment, quenching in oil can ignite the oil if the workpiece is too large or the oil bath is too shallow. Use a covered quench tank with at least 3× the workpiece volume of oil. Keep a Class B fire extinguisher within 3 m. Never quench in oil near open flames.
- **Forge welding fume**: Forge welding with borax flux at 1300°C produces boron oxide fumes. Work in a well-ventilated area or use local exhaust ventilation. Prolonged inhalation of boron oxide irritates the respiratory tract.

## Quality Control

1. **Ring test**: Strike the face lightly with a hardened steel hammer. A good anvil produces a clear, sustained ring (~2-3 seconds). A dead, dull sound indicates a crack in the body or a poorly bonded face plate — the anvil will not return energy efficiently.
2. **Flatness check**: Place a precision straightedge across the face. No gap should exceed 0.1 mm. Check along the length, across the width, and diagonally.
3. **Hardness test**: Attempt to file the face with a standard bastard-cut file. The file must not cut — if it does, the face is undertreated and will dent in service. Target: 55-60 HRC.
4. **Rebound test**: Drop a 25 mm steel ball bearing from 300 mm onto the face. It should rebound to at least 200 mm (67% rebound ratio). Lower rebound indicates a soft face or a poorly bonded plate. This test characterizes the anvil's energy return.
5. **Stability test**: Strike the anvil face with a 4 kg sledge at full swing. The anvil must not shift, rock, or move on its stump. If it moves, re-secure the mounting.
6. **Face plate bond test**: Tap the face at multiple points with a small hammer. All points should ring the same clear tone. A dull spot indicates a void between the face plate and body — the face will eventually crack at this location.
7. **Hardy hole fit check**: Insert a standard hardy tool (25 mm square shank) into the hardy hole. It should slide in with 0.1-0.3 mm clearance — tight enough that the tool stands upright without tilting, loose enough to remove by hand. An oversized hardy hole allows the tool to tilt, producing uneven cuts. An undersized hole requires driving the tool in with a hammer, which damages both the tool and the hole.

## Variations and Alternatives

- **Stone anvil**: The earliest option. Requires no metallurgy. A flat granite or basalt boulder set in the ground. Sufficient for copper, bronze, and early iron. Poor energy return. Upgrade when iron production is established.
- **London-pattern anvil (this article's primary build)**: The standard design for 300+ years. Flat face, conical horn, step, hardy hole, pritchel hole. The most versatile single-anvil design. Weight 50-150 kg.
- **Double-horn anvil**: Horns on both ends (one round, one flat/square). No heel. Preferred by production smiths — one horn is always accessible regardless of workpiece position. More complex to cast or forge.
- **Stake anvil (beaked anvil)**: A small anvil (5-20 kg) on a long spike driven into a stump or bench. Used for specialized shaping and planishing. Not a substitute for a full-size anvil but a useful supplement for light work.
- **Block anvil (no horn)**: A simple rectangular block of hardened steel, 50-200 kg. No horn, no holes. Easiest iron anvil to make — requires no complex casting. Limited versatility but adequate for straight forging.
- **Railroad rail anvil**: A section of steel railroad rail (cut 300-400 mm long) placed flange-up on a stump. The rail head provides a hard, narrow working surface. Free if rail is available. Limitations: narrow face (70 mm), no horn, no holes. Adequate for light forging and as a bootstrap anvil.
- [Forge hammer](forge-hammer.md): Power hammers replace hand hammering on the anvil for production work. The anvil block in a power hammer serves the same function but on a larger scale (anvil mass 10-15× ram mass).
- Anvil accessories: A set of hardy tools (cutter, swage, fuller, bick) transforms the anvil from a simple block into a versatile forming station. Each tool has a square shank that fits the hardy hole. The most commonly used are the hardy cutter (for severing bar) and the bottom swage (for shaping round cross-sections). Make hardy tools from medium-carbon steel (0.5% C), hardened to 50-55 HRC.
- Stump preparation: The stump must be flat-topped and level. Check with a spirit level in two directions. The recess for the anvil base should be a snug fit — the anvil should seat with firm hand pressure and not rock. If the stump cracks or checks (splits) over time, replace it — a cracked stump transmits vibration poorly and allows the anvil to shift.

## References

- [Forming](forming.md) — forging operations performed on the anvil
- [Iron & Steel](../metals/iron-steel.md) — iron and steel production for anvil construction
- [Casting](../metals/casting.md) — casting the anvil body
- [Joining](joining.md) — forge-welding the face plate to the body
- [Bearings & Abrasives](bearings-abrasives.md) — abrasive materials for face grinding
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence
- [Forge Hammer](forge-hammer.md) — power hammer construction, which uses a scaled-up anvil block
- Anvil face hardness: 55-60 HRC balances wear resistance and toughness. Below 50 HRC, the face dents under hammer impact. Above 65 HRC, the face chips under heavy use.
- Anvil-to-hammer mass ratio: minimum 20:1 for hand forging. A 100 kg anvil works well with hammers up to 4 kg. For heavier sledge work (6-8 kg), use a 150+ kg anvil.
- Anvil face maintenance: Clean the face with a wire brush after each forging session. Remove scale buildup that marks subsequent workpieces. Apply a light film of oil to prevent rust during storage. Re-grind the face when dents or sway exceed 0.5 mm.
- Working height adjustment: If the anvil face is too low, place hardwood shims under the stump. If too high, trim the stump top. The correct height places the face at the smith's knuckle height when standing with arms relaxed — typically 650-750 mm from floor to face top. A height error of ±25 mm is tolerable; beyond that, it causes back strain or reduced hammer efficiency.
- Face plate weld quality: The forge-weld bond between the face plate and body determines the anvil's acoustic properties and energy return. Test by tapping with a hammer at 100 mm intervals across the face — all points should produce the same clear, sustained ring. A dull sound at any point indicates an unbonded area (a void between face and body). Small voids (<20 mm diameter) are tolerable; large voids cause the face to crack under concentrated hammer impact.
- Anvil face care during use: Never strike the face with hardened steel tools (chisels, punches, fullers) directly. Always place a copper or brass drift between the hardened tool and the face. The hardened face (55-60 HRC) is harder than most tools, and hardened steel-on-hardened steel contact chips both surfaces. The step (table) between the face and horn is intentionally softer (45-50 HRC) for chisel cutting — use the step for cutting operations, not the main face.
- Heat treatment verification: After hardening and tempering the face plate, verify with a file test. A standard bastard-cut file must skate on the face without cutting. If the file cuts, the face is undertreated — re-harden at 800°C and re-temper. Check multiple points across the face — uneven heating during forge-welding or hardening can produce soft spots that dent in service.
- Typical anvil weight for different work: Light bench work (jewelry, small hardware): 25-50 kg. General smithing (tools, brackets): 75-100 kg. Heavy forging (large structural parts, production work): 100-200 kg. The working face width should be 100-150 mm — wider anvils are more stable for wide workpieces but heavier to maneuver during installation.
- Heat color reference for face plate treatment: When hardening the face plate, the target temperature is 780-820°C (cherry red for 0.8-1.0% C steel). Use the following color guide: dark cherry red = 600°C (too cold — incomplete austenitization), cherry red = 780-820°C (correct range), bright cherry red = 850-900°C (slightly overheated — grain growth risk), orange = 900-1000°C (too hot — decarburization and grain coarsening). A pyrometer or thermocouple is more reliable than color judgment but the color guide is functional for bootstrap heat treatment.
- Anvil positioning in the forge shop: Place the anvil within 1-2 steps of the forge (hearth) so the smith can transfer hot metal quickly without losing heat. Allow 1.5-2 m clearance on all sides for hammer swing. Position the anvil so the horn points toward the smith's non-dominant side (left for right-handed smiths). The slack tub (water quench) should be within arm's reach on the opposite side from the forge. This triangular arrangement (forge → anvil → slack tub) minimizes wasted motion during forging.
- Face plate thickness and wear allowance: A 10 mm face plate provides sufficient working material for decades of use. Each regrinding removes 0.5-1.0 mm. With a 10 mm plate, the anvil can be resurfaced 5-10 times before the face plate becomes too thin to retain hardness (minimum 5 mm for effective heat treatment). A 20 mm face plate on a production anvil extends service life to a century or more. When the face plate is ground below 5 mm, the hardened layer is exhausted and the underlying wrought iron body is exposed — at this point, the face must be replaced.
- Anvil hardy tool set: A functional smithy requires a set of hardy tools: hardy cutter (for severing bar stock — sharpened edge facing up, cutting edge 50-80 mm wide), bottom swage (for shaping round cross-sections — matching top swage held in the hammer hand), bottom fuller (for grooving and shouldering — radiused edge, 10-20 mm width), and pritchel (for punching holes). Each tool has a square shank fitting the hardy hole with 0.1-0.3 mm clearance. Make hardy tools from medium-carbon steel (0.5% C), hardened to 50-55 HRC — hard enough to hold an edge, tough enough to resist chipping under hammer impact.
- Rebound test for anvil condition: Drop a 25 mm steel ball bearing from 300 mm onto the face. A good anvil rebounds the ball 250-290 mm (80-95% rebound). A worn or soft face rebounds less than 200 mm (65% rebound). Cast iron anvils (not forged steel) typically rebound 50-60%. This test is quick, repeatable, and requires only a ball bearing — use it when evaluating a used anvil before purchase.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
