# Water Turbines

> **Node ID**: energy.gravity.water-turbines
> **Domain**: [Energy](./)
> **Dependencies**: `energy.gravity`, `metals.iron-steel`, `machine-tools`
> **Enables**: `energy.electricity` (prime mover for generators), `energy.storage` (reversible pump-turbines)
> **Timeline**: Years 12-25
> **Outputs**: hydraulic_power, electrical_generation, high_rpm_rotation

### Overview

Water turbines replace water wheels where higher heads, higher efficiencies, and faster rotation speeds are needed. They convert the gravitational potential energy of falling water into continuous rotary motion at 100-1000+ RPM — directly usable for electrical generators without the massive gear reductions that water wheels require. All turbine types require iron or steel construction and precision machining, making them dependent on the machine-tools stage. For lower-head applications with simpler construction, see [gravity.md](gravity.md) for water wheel types.

### Pelton Wheel (Impulse Turbine)

**Principle**: One or more high-velocity water jets from a nozzle strike spoon-shaped buckets mounted on the perimeter of a runner. All pressure conversion to kinetic energy happens at the nozzle — the runner operates in atmospheric pressure (not submerged). The jet's momentum transfers to the bucket, spinning the runner.

**Construction**:
- **Runner**: Cast iron or bronze hub with forged steel buckets bolted or cast integrally. Each bucket has a central splitter ridge that divides the incoming jet in half, redirecting each half through approximately 165° for maximum momentum transfer. Buckets are shaped to avoid interfering with the preceding bucket's exhaust.
- **Nozzle**: Converging needle nozzle — a conical needle (spear) moves in and out to vary the jet diameter and thus the flow rate. Needle actuated by a governor for speed regulation. Nozzle interior machined smooth to minimize turbulence.
- **Jet deflector**: A hinged plate that can swing into the jet path to deflect water away from the runner without closing the nozzle (rapid power reduction without water hammer in the penstock). Used for load rejection protection.
- **Casing**: Minimal — open housing since runner operates in air. A collector at the bottom returns spent water to the tailrace.

**Head range**: 30-1000+ m. Best suited for mountain streams with steep gradients. At 100 m head, jet velocity ≈ √(2 × 9.81 × 100) ≈ 44 m/s. The bucket tip speed is designed for approximately half the jet velocity for maximum efficiency.

**Efficiency**: 85-91% at design flow. Remains above 80% down to ~30% of rated flow (with proper nozzle regulation). Degrades at very low flows where nozzle losses become significant relative to power output.

**Power output**: 1-500+ HP. Small Pelton units (5-20 HP) are practical for remote mountainous sites with minimal infrastructure. Large installations in alpine regions reach hundreds of MW.

**Multi-jet arrangements**: 2-6 nozzles arranged around a single runner increase power without increasing runner diameter or speed. Each nozzle independently regulated for partial-load efficiency. Horizontal shaft (1-2 jets) or vertical shaft (4-6 jets) configurations.

### Francis Turbine (Reaction Turbine)

**Principle**: Water enters the runner radially from a spiral casing (volute), passes through adjustable guide vanes (wicket gates) that direct flow at the optimal angle, then flows through the curved runner blades and exits axially downward through a draft tube. Both pressure and velocity drop across the runner — it is a true reaction machine. The runner is fully submerged in water; the entire casing is pressurized.

**Construction**:
- **Spiral casing (volute)**: Cast iron or welded steel scroll-shaped casing of decreasing cross-section. Distributes water uniformly around the entire runner circumference. Design ensures constant velocity at the wicket gate entrance at all points around the circumference.
- **Wicket gates**: 12-24 adjustable guide vanes arranged in a circle around the runner. Each vane rotates on its own pivot. Connected by linkage to a single servomotor (hydraulic cylinder) for synchronized opening/closing. Controls both flow rate and flow angle — the primary speed regulation mechanism.
- **Runner**: Cast steel (small units) or fabricated/ welded steel (large units) with complex curved blade profiles. Blades are three-dimensionally curved — the water follows a spiral path from radial entry to axial exit. For small heads, the runner may have 8-12 blades; for large heads, 12-20 blades with longer, more closely spaced profiles.
- **Draft tube**: Conical tube extending from the runner exit downward to the tailrace. Its purpose is twofold: recover kinetic energy from the exiting water (acts as a diffuser, slowing the water and converting velocity to pressure), and allow the runner to be set above tailwater level for maintenance access while maintaining a pressure head at the runner exit. Draft tube must be carefully designed — poorly shaped tubes cause flow separation and energy loss.
- **Shaft**: Vertical configuration most common (runner at bottom, generator above waterline). Horizontal configurations exist for smaller units.

**Head range**: 3-300 m. The most versatile turbine type — the Francis turbine covers the widest range of heads and flows of any hydraulic turbine. Optimal for medium-head sites (30-200 m).

**Efficiency**: 80-94% at design flow. Francis turbines achieve the highest peak efficiency of any hydraulic turbine type. However, efficiency drops off more steeply at partial flow than Pelton or Kaplan (because the wicket gate angle becomes suboptimal at partial opening). Maintains above 80% from roughly 50-110% of rated flow.

**Power output**: 10-100,000+ HP. Scalable from small village installations to the largest hydroelectric stations in the world.

**Cavitation**: The primary operational hazard. As water accelerates through the runner, local pressure can drop below vapor pressure — microscopic bubbles form and then collapse violently against blade surfaces, pitting and eroding the metal. Prevention: install the runner sufficiently below tailwater level (submergence margin), keep runner surfaces smooth, avoid operating at very low flows where flow angles cause local low-pressure zones. Stainless steel runner blades resist cavitation damage better than carbon steel.

### Kaplan Turbine (Axial-Flow Reaction Turbine)

**Principle**: Propeller-type runner with adjustable blade pitch. Water flows axially (horizontally or vertically) through the runner — no radial component. The blade pitch adjusts automatically to match the flow angle for maximum efficiency across a wide range of flows. Conceptually similar to an outboard motor propeller running in reverse.

**Construction**:
- **Runner**: Hub containing the blade-pitch mechanism with 3-8 propeller blades bolted to the hub. Each blade rotates on its own axis within the hub. Internal linkage (levers or hydraulic piston) connects all blades so they pitch in unison. The mechanism must operate underwater under pressure — sealed bearings and a rotating oil feed through the hollow shaft.
- **Wicket gates**: Similar to Francis — adjustable guide vanes upstream of the runner. The Kaplan has both wicket gate adjustment AND blade pitch adjustment, coordinated by a cam mechanism to maintain optimal angles across the operating range.
- **Draft tube**: Essential — the entire pressure recovery happens in the draft tube. S-shaped (elbow) draft tube for horizontal shaft configurations. Vertical configurations use a straight conical draft tube.
- **Bulb turbine variant**: For very low-head river installations, the turbine and generator are housed in a streamlined underwater bulb (steel enclosure) placed directly in the river channel. Water flows around and through the bulb. Eliminates the spiral casing and reduces civil works.

**Head range**: 1-15 m. Designed for large rivers with low dams or run-of-river installations where the Francis turbine would require an impractically large runner diameter.

**Efficiency**: 80-92% at design flow. The key advantage is that efficiency remains high over a wide flow range — 85%+ from roughly 30-100% of rated flow — because the blade pitch continuously adapts. This makes Kaplan turbines ideal for rivers with significant seasonal flow variation.

**Power output**: 50-100,000+ HP. Typically installed in large run-of-river or low-head dam sites where enormous flow volumes are available.

**Precision requirements**: Kaplan turbines require the highest manufacturing precision of any turbine type. The blade-to-hub seals must be watertight under pressure. The blade pitch mechanism must move smoothly and synchronously. Cavitation risk is high at low heads — runner submergence is critical.

### Material Requirements

| Component | Pelton | Francis | Kaplan |
|-----------|--------|---------|--------|
| Runner | Cast iron/steel hub, forged steel buckets | Cast or fabricated steel, curved blades | Cast steel hub, forged steel blades |
| Casing | Minimal (open) | Cast iron or welded steel volute | Cast iron or steel, often concrete-embedded |
| Guide vanes | N/A | Bronze or stainless steel | Bronze or stainless steel |
| Shaft | Carbon steel | Carbon or alloy steel | Alloy steel (hollow for blade linkage) |
| Draft tube | N/A | Steel plate or concrete | Steel plate or concrete |

### Site Selection

Choosing the correct turbine type depends entirely on the site's head and flow characteristics:

- **High head (>100 m), low flow**: Pelton wheel. The only practical choice. Mountain streams, penstock-fed from reservoirs.
- **Medium head (10-300 m), medium flow**: Francis turbine. The dominant choice for most hydroelectric sites. Dam-fed or run-of-river with moderate head.
- **Low head (1-15 m), high flow**: Kaplan turbine. Large rivers, low dams, tidal barrages. Francis turbines are impractical here because the runner diameter would be enormous.
- **Very low head (<3 m), variable flow**: Bulb turbine (Kaplan variant). Run-of-river on large flat rivers.

### Safety and Hazards

- **Cavitation damage**: Causes pitting of runner blades, vibration, and eventual structural failure. Monitor for noise (sounds like gravel in the turbine), vibration, and performance drop. Repair pitted surfaces promptly — cavitation accelerates once pits form (they act as nucleation sites for more bubbles).
- **Water hammer**: Rapid valve closure on a long penstock creates a pressure shock wave that travels at the speed of sound in water (~1400 m/s). The resulting pressure spike can burst pipes or damage turbine casings. Prevention: surge tanks (standpipe on the penstock that absorbs the shock), slow-closing valves, jet deflectors (Pelton) that reduce power without closing the nozzle.
- **Runner runaway**: If the generator disconnects from the grid (load rejection) and the wicket gates fail to close, the turbine accelerates to runaway speed — typically 1.8-2.5× rated speed. Centrifugal forces scale with the square of speed — a 2× overspeed quadruples stress. Structural failure is possible. Prevention: governor-closed wicket gates with independent overspeed trip, jet deflectors (Pelton), and emergency gate upstream that can drop closed.
- **Entrapment and drowning**: Turbine pits and draft tube areas are confined spaces with water hazards. Lock-out/tag-out before entering. Ventilate confined spaces. Never enter a turbine pit without verifying isolation.

### Cross-References

- **Water wheels (simpler predecessors)**: [gravity.md](gravity.md)
- **Pumped hydro (reversible turbines)**: [storage.md](storage.md), [pumped-hydro.md](pumped-hydro.md)
- **Electrical generators driven by turbines**: [electricity.md](electricity.md)
- **Machine tools required for precision components**: [forming.md](../machine-tools/forming.md)

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
