# Metal Forming

> **Node ID**: machine-tools.forming
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 5-15
> **Outputs**: formed_metal_parts, bar_stock, sheet_metal, wire, plate, rod

### Overview

Metal forming reshapes solid metal through plastic deformation — applying force at controlled temperatures to change cross-section, bend, or elongate stock without removing material. Forming retains nearly 100% of the workpiece mass and produces the bar stock, sheet, wire, and shaped blanks that feed every downstream process: machine tools, construction, electrical wiring, and mechanisms.

The critical variables are **temperature** (hot vs cold working), **force** (hammer, press, or roll), and **reduction ratio** (how much cross-section changes per pass). Metals deform more easily when hot — yield strength drops by 60-80% above recrystallization temperature.

### Forging Temperatures by Metal

Every metal has a forging range — hot enough to be plastic, cool enough to avoid burning or crumbling.

| Metal | Forging Range | Color (approx.) | Notes |
|-------|--------------|-----------------|-------|
| Copper | 700–900°C | Dark cherry to orange | Very forgiving, wide working range. Oxidizes green. |
| Bronze (90/10 Cu/Sn) | 650–800°C | Dark red to cherry | Narrower range than copper — cracks if too cold, crumbles if too hot. |
| Wrought iron | 1000–1200°C | Bright orange to yellow | Must reheat frequently — loses heat fast. Sparks when hammered (slag). |
| Low-carbon steel (0.1–0.3% C) | 800–1150°C | Cherry to bright yellow | The workhorse forging metal. Wide range. |
| Medium-carbon steel (0.3–0.5% C) | 800–1100°C | Cherry to orange | Stronger but less ductile — avoid working below 800°C. |
| High-carbon steel (0.6–1.0% C) | 800–1050°C | Cherry to orange | Narrow range. Overheating causes burning (grain boundary melting). |

Below these ranges, metal work-hardens rapidly and may crack. Above them, the metal burns (grain boundaries oxidize, producing a crumbly, ruined forging that cannot be salvaged).

### Forge Work

**Open-die forging** (hand forging): Smith heats stock in a charcoal forge, positions on anvil, strikes with hammers or sledges. Shape controlled by hammer placement, stock rotation, and tooling (swages, fullers, flatters).
- **Drawing out**: Hammer along the length to reduce cross-section and elongate. Rotate 90° every few blows for square section.
- **Upsetting**: Hammer on end to thicken cross-section. Risk of buckling if length > 3× diameter.
- **Bending**: Heat bend zone, hammer over anvil horn. Minimum radius ~2× stock thickness.
- **Punching and drifting**: Drive punch through hot metal, enlarge with drift. Punch from both sides to meet in middle for cleaner holes.

**Closed-die forging** (impression forging): Metal compressed between shaped dies containing the negative of the desired part. Flash (excess) squeezes out at parting line and is trimmed. Requires dies machined to tolerance (see [Iterative Bootstrap](./iterative-bootstrap.md)). Advantages: repeatable parts, good grain flow, near-net shape. Used for connecting rods, gear blanks, wrenches.

### Hammer Forming

**Sledge hammer** (4–8 kg, two-handed): The fundamental heavy forging tool. One person holds work with tongs; a striker delivers sledge blows. Effective for drawing out bars 25–75 mm square, upsetting ends, driving punches. Blow force: ~10–25 kN.

**Power hammer** (mechanized forging):
- **Helve hammer**: Beam pivoted at one end, hammer head at the other. Raised by cam on water-wheel shaft, falls by gravity. Stroke 30–60 cm, 50–150 kg blow equivalent. The first mechanized forging tool.
- **Tilt hammer**: Similar but tail is lifted. 80–200 blows/minute in early water-powered forges.
- **Spring helve hammer** (intermediate build): Heavy timber frame, 15–40 kg head on leaf spring. Crank-driven, 150–300 blows/minute. Constructable with basic machine tools.
- **Steam or air hammer** (later): 500–5000 kg capacity. Requires [Steam Power](../energy/steam-power.md).

### Rolling Mill

Rolling reduces cross-section of heated metal by passing it between counter-rotating rolls. Each pass reduces thickness 10–30% and elongates proportionally.

**Hand-operated rolling mill** (the bootstrap starting point):
- Two hardened steel or cast iron rolls, 75–150 mm diameter, 150–300 mm face length. Mounted in a cast iron or fabricated steel frame with adjustable gap (screw-down mechanism).
- Drive: hand crank or foot treadle through gear reduction (3:1 to 6:1). Two operators — one cranks, one feeds stock.
- Capacity: hot rolling of copper, bronze, and soft iron bar up to ~10 mm thick. Cold rolling of copper and brass sheet to ~1 mm.
- Roll pressure: 50–150 kN for hot steel at 15–20% reduction.

**Powered rolling mill** (water wheel or engine):
- Rolls 200–400 mm diameter, 400–800 mm face. Drive via gears or belt from water wheel (3–10 HP minimum).
- Can roll iron bar from 50 mm square bloom down to 10 mm round in 6–10 passes, reheating between passes.
- **Reduction per pass**: 15–25% for hot steel. Greater reduction causes excessive roll force and uneven deformation.
- **Roll material**: Cast iron for copper/brass. Forged or cast steel for iron/steel. Rolls must be harder than the workpiece.

**Sheet rolling** (flat sheet from ingot):
1. Cast ingot (copper, brass, or steel) 20–40 mm thick. Soak at forging temperature 30–60 min.
2. Pass through rolls, reduce 2–3 mm per pass. Rotate 180° between passes for even reduction.
3. Reheat every 4–6 passes. Anneal at 500–700°C when reduction exceeds 40–50% from last anneal.
4. Target: copper sheet to 0.5 mm (hand mill) or 0.1 mm (powered mill).

### Wire Drawing

Wire drawing pulls metal rod through progressively smaller dies, reducing diameter and increasing length. Unlike rolling, wire drawing is done cold.

**Draw plate** (the bootstrap tool): Hardened high-carbon steel (0.8–1.0% C) plate, 10–25 mm thick, with tapered holes graduating in size (e.g., 8.0 mm down to 1.0 mm in 0.5 mm steps). Each hole: ~30° included angle entrance, short straight bearing section (~1× diameter), back-relief.

**Procedure**:
1. **Point the rod**: File one end to a taper that fits through the first die.
2. **Lubricate**: Apply tallow, beeswax, or soap solution. Without lubrication, rod galls and sticks in die.
3. **Pull through die** with tongs or draw bench hook (chain drive with 0.5–1 m lever arm for wire > 2 mm). Pull force: 5–30 kN.
4. **Anneal** every 3–5 passes at 500–700°C for copper, 650–800°C for iron. Work hardening makes wire brittle without annealing.
5. **Reduction per pass**: 15–25% area reduction. Total from rod to finished wire: 80–95% area reduction.

**Fine wire** (< 1 mm): Use draw bench with capstan (rotating drum). Speed 30–100 m/min for copper. Dies are tungsten carbide inserts. Copper wire down to 0.1 mm achievable — the wire for [electromagnetic coils](../energy/electricity.md).

### Sheet Metal Forming

**Bending**: Clamp sheet in vise or bending brake (hinged leaf brake — constructable from flat bar and angle iron). Minimum bend radius = 1× sheet thickness for soft metals, 2–3× for harder alloys.

**Seaming**: Fold edges of two sheets together and hammer flat (Pittsburgh seam, double seam). Produces airtight and watertight joints for ductwork and containers. No heat required.

**Raising and sinking**: Shape sheet into bowls and domes by hammering over stakes (shaped anvils). Raising = hammering outside (thins and curves). Sinking = hammering into a hollow. Copper and brass raise cold; iron requires heating.

**Spinning**: Clamp sheet against a form on a lathe. Apply pressure with a rounded tool while the mandrel rotates. Used for bowls, cups, reflectors. Requires a lathe (see [Iterative Bootstrap](./iterative-bootstrap.md)).

### Annealing Between Operations

Cold working accumulates strain, increasing hardness and reducing ductility. Annealing restores ductility by allowing recrystallization. **Rule of thumb**: anneal when cross-section has been reduced 40–50% from last anneal, or every 3–5 wire drawing passes.

| Metal | Anneal Temperature | Time | Cooling |
|-------|-------------------|------|---------|
| Copper | 500–700°C | 30–60 min | Air cool or water quench |
| Brass (70/30) | 400–600°C | 30–60 min | Air cool |
| Bronze | 600–700°C | 30–60 min | Air cool |
| Wrought iron | 700–900°C | 30–60 min | Air cool |
| Steel (low carbon) | 700–900°C | 30–60 min | Furnace cool (slow) |

### Safety Concerns

- **Flying sparks and scale**: Forge work produces hot metal fragments. Leather apron, safety glasses, and face shield for bloom consolidation. Keep fire extinguishing sand nearby.
- **Burns**: Metal at forging temperature (700–1200°C) causes instant deep burns on contact. Use properly fitting tongs — if stock slips from tongs, it flies. Test tongs by clamping cold stock and shaking hard before using on hot work.
- **Pinch points**: Rolling mills and draw benches produce crushing forces. Never place hands between rolls or near draw chain.
- **Repetitive strain**: Hammer forging limits productive hours to 4–6/day. Power hammers reduce this.
- **Carbon monoxide**: Charcoal and coal forges produce CO in enclosed spaces. Ventilate smithies — work outdoors or with open doors and roof vents.

### Cross-References

- [Iron & Steel](../metals/iron-steel.md) — bloom smelting, carburization, heat treatment
- [Iterative Bootstrap](./iterative-bootstrap.md) — building the rolling mill and draw bench from castings
- [Bearings & Abrasives](./bearings-abrasives.md) — grinding and finishing formed parts
- [Electricity](../energy/electricity.md) — drawn copper wire for generators and motors

---

*Part of the [Bootciv Tech Tree](../) • [Machine Tools](./) • [All Domains](../)*
