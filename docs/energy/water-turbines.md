# Water Turbines

> **Node ID**: energy.gravity.water-turbines
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.gravity`](gravity.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 12-25
> **Outputs**: hydraulic_power, electrical_generation, high_rpm_rotation
> **Critical**: No — water turbines provide efficient hydroelectric generation but are limited to sites with suitable head and flow


Water turbines replace water wheels where higher heads, higher efficiencies, and faster rotation speeds are needed. They convert the gravitational potential energy of falling water into continuous rotary motion at 100-1000+ RPM — directly usable for electrical generators without the massive gear reductions that water wheels require. All turbine types require iron or steel construction and precision machining, making them dependent on the machine-tools stage. For lower-head applications with simpler construction, see [gravity.md](gravity.md) for water wheel types.

## Pelton Wheel (Impulse Turbine)

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

**Strengths**:
- Highest efficiency at high-head sites (85-91% at design flow)
- Simple, robust construction — runner operates in air, not submerged
- Large bucket openings tolerate moderate debris without clogging
- Multiple nozzles allow efficient partial-load operation

**Weaknesses**:
- Limited to high-head sites (30-1000+ m) — useless on low-gradient rivers
- Requires precision machining of bucket profiles (±1 mm) for good efficiency
- Nozzle erosion from high-velocity water with suspended sediment needs periodic repair
- Single-jet units have poor efficiency below 30% of rated flow

## Francis Turbine (Reaction Turbine)

**Principle**: Water enters the runner radially from a spiral casing (volute), passes through adjustable guide vanes (wicket gates) that direct flow at the optimal angle, then flows through the curved runner blades and exits axially downward through a draft tube. Both pressure and velocity drop across the runner — it is a true reaction machine. The runner is fully submerged in water; the entire casing is pressurized.

**Construction**:
- **Spiral casing (volute)**: Cast iron or welded steel scroll-shaped casing of decreasing cross-section. Distributes water uniformly around the entire runner circumference. Design ensures constant velocity at the wicket gate entrance at all points around the circumference.
- **Wicket gates**: 12-24 adjustable guide vanes arranged in a circle around the runner. Each vane rotates on its own pivot. Connected by linkage to a single servomotor (hydraulic cylinder) for synchronized opening/closing. Controls both flow rate and flow angle — the primary speed regulation mechanism.
- **Runner**: Cast steel (small units) or fabricated/ welded steel (large units) with complex curved blade profiles. Blades are three-dimensionally curved — the water follows a spiral path from radial entry to axial exit. For small heads, the runner may have 8-12 blades; for large heads, 12-20 blades with longer, more closely spaced profiles.
- **Draft tube**: Conical tube extending from the runner exit downward to the tailrace. Its purpose is twofold: recover kinetic energy from the exiting water (acts as a diffuser, slowing the water and converting velocity to pressure), and allow the runner to be set above tailwater level for maintenance access while maintaining a pressure head at the runner exit. Draft tube must be carefully designed — poorly shaped tubes cause flow separation and energy loss.
- **Shaft**: Vertical configuration most common (runner at bottom, generator above waterline). Horizontal configurations exist for smaller units.

**Head range**: 3-300 m. The most versatile turbine type — the Francis turbine covers the widest range of heads and flows of any hydraulic turbine. Optimal for medium-head sites (30-200 m).

**Efficiency**: 80-94% at design flow. Francis turbines achieve the highest peak efficiency of any hydraulic turbine type. However, efficiency drops off more steeply at partial flow than Pelton or Kaplan (because the wicket gate angle becomes suboptimal at partial opening). Maintains above 80% from roughly 50-110% of rated flow.

**Strengths**:
- Highest peak efficiency of any hydraulic turbine (up to 94%)
- Most versatile head range (3-300 m) — covers the widest range of sites
- Wicket gate mechanism provides excellent speed regulation for grid frequency control
- Scalable from village installations (10 HP) to major hydroelectric stations (100,000+ HP)

**Weaknesses**:
- Complex runner blade profiles require precision casting and machining (±1 mm tolerance)
- Pressurized casing must withstand full hydrostatic head at the inlet
- Cavitation risk if runner is not set sufficiently below tailwater level
- Efficiency drops steeply below 50% of rated flow — poor for highly variable flow sites

## Kaplan Turbine (Axial-Flow Reaction Turbine)

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

**Strengths**:
- Maintains high efficiency (85%+) over wide flow range (30-100% of rated) due to adjustable blade pitch
- Only practical turbine for very low-head sites (1-15 m) with high flow volumes
- Compact runner diameter compared to Francis for the same low-head application

**Weaknesses**:
- Most complex turbine to manufacture — blade pitch mechanism inside a submerged hub
- Blade-to-hub seals must be watertight under pressure while allowing rotation
- High cavitation risk at low heads — runner must be set well below tailwater level
- Requires precision engineering beyond what early machine shops can deliver

## Material Requirements

| Component | Pelton | Francis | Kaplan |
|-----------|--------|---------|--------|
| Runner | Cast iron/steel hub, forged steel buckets | Cast or fabricated steel, curved blades | Cast steel hub, forged steel blades |
| Casing | Minimal (open) | Cast iron or welded steel volute | Cast iron or steel, often concrete-embedded |
| Guide vanes | N/A | Bronze or stainless steel | Bronze or stainless steel |
| Shaft | Carbon steel | Carbon or alloy steel | Alloy steel (hollow for blade linkage) |
| Draft tube | N/A | Steel plate or concrete | Steel plate or concrete |

## Site Selection

Choosing the correct turbine type depends entirely on the site's head and flow characteristics:

- **High head (>100 m), low flow**: Pelton wheel. The only practical choice. Mountain streams, penstock-fed from reservoirs.
- **Medium head (10-300 m), medium flow**: Francis turbine. The dominant choice for most hydroelectric sites. Dam-fed or run-of-river with moderate head.
- **Low head (1-15 m), high flow**: Kaplan turbine. Large rivers, low dams, tidal barrages. Francis turbines are impractical here because the runner diameter would be enormous.
- **Very low head (<3 m), variable flow**: Bulb turbine (Kaplan variant). Run-of-river on large flat rivers.

## Safety and Hazards

- **Cavitation damage**: Causes pitting of runner blades, vibration, and eventual structural failure. Monitor for noise (sounds like gravel in the turbine), vibration, and performance drop. Repair pitted surfaces promptly — cavitation accelerates once pits form (they act as nucleation sites for more bubbles).
- **Water hammer**: Rapid valve closure on a long penstock creates a pressure shock wave that travels at the speed of sound in water (~1400 m/s). The resulting pressure spike can burst pipes or damage turbine casings. Prevention: surge tanks (standpipe on the penstock that absorbs the shock), slow-closing valves, jet deflectors (Pelton) that reduce power without closing the nozzle.
- **Runner runaway**: If the generator disconnects from the grid (load rejection) and the wicket gates fail to close, the turbine accelerates to runaway speed — typically 1.8-2.5× rated speed. Centrifugal forces scale with the square of speed — a 2× overspeed quadruples stress. Structural failure is possible. Prevention: governor-closed wicket gates with independent overspeed trip, jet deflectors (Pelton), and emergency gate upstream that can drop closed.
- **Entrapment and drowning**: Turbine pits and draft tube areas are confined spaces with water hazards. Lock-out/tag-out before entering. Ventilate confined spaces. Never enter a turbine pit without verifying isolation.

## Cross-References

- **Water wheels (simpler predecessors)**: [gravity.md](gravity.md)
- **Pumped hydro (reversible turbines)**: [storage.md](storage.md), [pumped-hydro.md](pumped-hydro.md)
- **Electrical generators driven by turbines**: [electricity.md](electricity.md)
- **Machine tools required for precision components**: [forming.md](../machine-tools/forming.md)

## Pelton Turbine: Bucket Geometry and Performance

**Bucket design**: Each Pelton bucket is a double-hemispherical cup with a central splitter ridge that divides the incoming jet into two equal halves. The splitter ridge must be sharp (knife-edge) and aligned exactly with the jet centerline. The jet enters through a notch cut in the bucket rim so that the bucket can pass through the jet without interference from the preceding bucket. Bucket width is 3-4 times the jet diameter to fully contain the splashing water.

**Pitch diameter and jet ratio**: The runner pitch diameter (the circle on which the jet strikes the buckets) is typically 10-20 times the jet diameter. This ratio (D/d) is called the jet ratio. Small jet ratios (< 10) mean fewer buckets are in the jet path at once, which is less efficient. Large jet ratios (> 20) require unnecessarily large and heavy runners. The number of buckets is typically 15-30, spaced closely enough that one bucket is always fully in the jet.

**Speed ratio**: The peripheral speed of the runner at the pitch circle is expressed as a fraction of the jet velocity: φ = π × D × n / (60 × √(2gH)), where n is the rotational speed in RPM. The optimal speed ratio for maximum efficiency is approximately 0.46 (the runner moves at roughly half the jet speed). This is derived from momentum transfer theory: maximum power transfer occurs when the bucket speed is half the jet speed, because the water exits the bucket with near-zero velocity relative to the ground.

**Efficiency characteristics**: Peak efficiency reaches 90% for well-designed Pelton wheels operating at design flow. The efficiency curve is relatively flat between 30-100% of rated flow when needle-nozzle regulation is used, because the jet velocity remains constant (full head is always available) and only the jet diameter changes. At very low flows, friction in the nozzle and bucket windage losses become proportionally larger.

**Head range**: Pelton wheels are the standard choice for high-head sites from 200 m to 2000 m. The jet velocity at 200 m head is roughly 63 m/s; at 1000 m head, roughly 140 m/s. These velocities demand precise bucket profiles and robust construction to resist erosion from the high-speed water jet.

## Francis Turbine: Runner Design and Specific Speed

**Runner geometry**: The Francis runner has 12-20 curved blades mounted between an upper crown (band) and a lower band (shroud). Water enters radially at the outer diameter and exits axially at the inner diameter (the "eye"). The blades are three-dimensionally twisted: the inlet edge is nearly radial, while the outlet edge is nearly axial. This twist accommodates the changing flow direction as water passes through the runner. The blade profiles must be accurate to within 1-2 mm for good efficiency.

**Adjustable guide vanes (wicket gates)**: 12-24 guide vanes surround the runner, pivoting on individual pins. All vanes are linked to a single servomotor that opens and closes them in unison. The vanes serve two functions: they control the flow rate (and thus power output), and they direct the water onto the runner blades at the optimal angle for each operating point. The vane angle determines both the tangential and radial components of the inlet velocity.

**Specific speed (Ns)**: The Francis turbine family spans specific speeds of Ns = 60-300 (where Ns = n × √P / H^(5/4), with n in RPM, P in kW, H in meters). Low specific speed (Ns ≈ 60-120) Francis runners are narrow with long blades, suited for high heads (100-300 m). High specific speed (Ns ≈ 200-300) runners are wide with shorter blades, suited for lower heads (30-80 m). The specific speed determines the overall runner geometry and must be selected to match the site conditions.

**Draft tube energy recovery**: The draft tube is not merely an exit passage. It is a carefully shaped diffuser that decelerates the water leaving the runner, converting kinetic energy into pressure. A well-designed draft tube recovers 60-80% of the kinetic energy at the runner exit. Without it, that energy would be lost. The tube typically flares from the runner exit diameter to roughly 2-3× that diameter at the tailwater, with a cone half-angle of 4-8° (wider angles cause flow separation).

**Efficiency**: 90-95% peak efficiency at the design point for well-constructed Francis turbines. This is the highest peak efficiency of any hydraulic turbine type. However, efficiency falls off more steeply at part-load than either Pelton or Kaplan turbines, because the fixed blade angles cannot adapt to the changed flow conditions.

## Kaplan Turbine: Adjustable Blades and Low-Head Performance

**Runner blade design**: The Kaplan runner has 4-8 propeller blades mounted on a central hub. Each blade rotates on its own trunnion (pivot bearing) within the hub. An internal linkage mechanism (pushrods, levers, or a hydraulic piston inside the hub shaft) moves all blades in unison. The blade angle adjusts from roughly 15° (low flow, fine pitch) to 40° (high flow, coarse pitch) relative to the plane of rotation. The mechanism must be watertight: oil-filled hubs with rotary shaft seals keep river water out of the linkage.

**Specific speed and application**: Kaplan turbines span specific speeds Ns = 300-800, the highest of any reaction turbine. This makes them suitable for the lowest heads and highest flow rates. At Ns = 800, the runner resembles a ship propeller with broad, widely spaced blades. The high specific speed means high rotational speed for a given head and power, which is advantageous for direct coupling to generators without gearing.

**Efficiency at low heads**: Kaplan turbines achieve 85-92% efficiency at design flow for heads of 2-30 m. The flat efficiency curve across a wide flow range is their key advantage: 85%+ efficiency from roughly 30-100% of rated flow. This contrasts with Francis turbines, which may drop to 70% at half-load. For run-of-river installations with widely varying seasonal flows, the Kaplan's part-load performance is critical to annual energy production.

**Cavitation management**: At low heads, the runner operates close to the tailwater level, and the pressure drop across the blades can easily fall below the vapor pressure of water. Kaplan runners are typically installed with the blade centerline 2-5 m below the minimum tailwater level (submergence). This hydrostatic pressure head suppresses cavitation. The required submergence increases with specific speed. Stainless steel blade surfaces resist cavitation pitting better than carbon steel.

## Site Selection Worked Example

Consider a site with 50 m of available head and a reliable flow of 5 m³/s.

**Power estimate**: P = η × ρ × g × Q × H. Assuming 85% overall efficiency for a well-designed Francis installation: P = 0.85 × 1000 × 9.81 × 5 × 50 = 2,084,625 W ≈ 2.08 MW. This falls squarely in the medium-head range, confirming the Francis turbine as the correct choice.

**Turbine selection**: At 50 m head and 2 MW, the specific speed Ns is roughly 150-200 for an optimal Francis runner. This dictates a runner diameter of approximately 1 m and a rotational speed near 500 RPM (for 50 Hz generation, this would couple to a 12-pole generator or use a speed-increasing gearbox to reach 750 or 1000 RPM).

**Runner diameter estimate**: The runner outer diameter is roughly D = (4 × Q / (π × v_m))^(1/2), where v_m is the meridional flow velocity. For 50 m head and Francis turbine, v_m ≈ 5-7 m/s. With v_m = 6 m/s: D = (4 × 5 / (π × 6))^(1/2) ≈ 1.03 m. A runner of roughly 1 m diameter is consistent with this flow and head.

**Annual energy**: If the flow is available 80% of the year (operating 7,000 hours), annual energy production is roughly 2,085 × 7,000 = 14,595 MWh ≈ 14.6 GWh. At a capacity factor of roughly 80%, this is a productive mid-scale installation suitable for powering a small town or industrial facility.

## Pelton Turbine: Bucket Geometry and Performance

**Bucket design**: Each Pelton bucket is a double-hemispherical cup with a central splitter ridge dividing the incoming jet into two equal halves. The splitter ridge must be knife-edge sharp and aligned exactly with the jet centerline. The jet enters through a notch cut in the bucket rim. Bucket width is 3-4 times the jet diameter to fully contain the splashing water.

**Pitch diameter and jet ratio**: The runner pitch diameter (where the jet strikes) is typically 10-20 times the jet diameter. This ratio (D/d) is the jet ratio. Small jet ratios (< 10) mean fewer buckets in the jet path, reducing efficiency. Number of buckets: 15-30, spaced so one is always fully in the jet.

**Speed ratio**: φ = π × D × n / (60 × √(2gH)) ≈ 0.46 for maximum efficiency. The runner moves at roughly half the jet speed, because maximum power transfer occurs when water exits the bucket with near-zero ground-relative velocity.

**Efficiency**: Peak 90% for well-designed units. The efficiency curve is flat between 30-100% of rated flow with needle-nozzle regulation, because jet velocity stays constant while only jet diameter changes.

**Head range**: Standard for high-head sites from 200 m to 2000 m. Jet velocity at 200 m: ~63 m/s; at 1000 m: ~140 m/s. These velocities demand precise bucket profiles and robust construction.

## Francis Turbine: Runner Design and Specific Speed

**Runner geometry**: 12-20 curved blades between an upper crown and lower band (shroud). Water enters radially at the outer diameter and exits axially at the inner diameter. Blades are three-dimensionally twisted: inlet nearly radial, outlet nearly axial. Blade profiles must be accurate within 1-2 mm for good efficiency.

**Adjustable guide vanes**: 12-24 pivoting vanes linked to a single servomotor. They control flow rate and direct water onto the runner blades at the optimal angle for each operating point.

**Specific speed (Ns = n√P/H^(5/4))**: Francis spans Ns = 60-300. Low Ns (60-120) means narrow runners with long blades for high heads (100-300 m). High Ns (200-300) means wide runners with shorter blades for lower heads (30-80 m).

**Draft tube energy recovery**: A carefully shaped diffuser decelerates water leaving the runner, converting kinetic energy into pressure. A well-designed draft tube recovers 60-80% of exit kinetic energy. Tube flares from runner exit diameter to 2-3× that diameter at tailwater, with cone half-angle of 4-8°.

**Efficiency**: 90-95% peak, highest of any hydraulic turbine type. Falls off more steeply at part-load than Pelton or Kaplan because fixed blade angles cannot adapt to changed flow conditions.

## Kaplan Turbine: Adjustable Blades

**Runner blades**: 4-8 propeller blades mounted on a central hub, each rotating on its own trunnion. An internal linkage (pushrods or hydraulic piston inside the hub) moves all blades in unison. Blade angle: 15-40° relative to the rotation plane. The mechanism must be watertight: oil-filled hubs with rotary shaft seals keep river water out.

**Specific speed**: Ns = 300-800, the highest of any reaction turbine. High rotational speed for a given head and power, advantageous for direct generator coupling. At Ns = 800, the runner resembles a ship propeller with broad, widely spaced blades.

**Low-head efficiency**: 85-92% at design flow for heads of 2-30 m. Flat efficiency curve: 85%+ from 30-100% of rated flow, critical for run-of-river installations with seasonal flow variation.

**Cavitation management**: Kaplan runners are installed with blade centerline 2-5 m below minimum tailwater level (submergence) to suppress cavitation. Required submergence increases with specific speed. Stainless steel blades resist pitting better than carbon steel.

## Penstock Design for High-Head Installations

**Penstock sizing**: The penstock (pressure pipe from the intake to the turbine) is a major civil works component for high-head sites. Diameter is selected to balance capital cost (larger pipe costs more) against head loss from friction (smaller pipe loses more head). The Darcy-Weisbach equation gives friction loss: h_f = f × (L/D) × (v²/2g), where f is the friction factor, L is pipe length, D is diameter, and v is flow velocity. Typical penstock velocities: 2-5 m/s. Economic diameter typically results in head loss of 3-8% of gross head.

**Penstock materials**: Steel pipe (welded or riveted) is standard for medium and high heads. Wood-stave pipe (wooden staves bound with steel bands) is a viable alternative for heads up to 30-50 m where timber is abundant. Concrete pipe suits low-head, large-diameter applications. PVC and GRP (glass-reinforced plastic) are modern alternatives for small installations.

**Surge protection**: Rapid valve closure on a long penstock creates water hammer, a pressure shock wave traveling at the speed of sound in water (~1400 m/s). The resulting pressure spike ΔP = ρ × c × Δv, where c is the wave speed and Δv is the velocity change. For a penstock flowing at 3 m/s: ΔP = 1000 × 1400 × 3 = 4.2 MPa (42 bar). A surge tank (standpipe connected to the penstock near the powerhouse) absorbs this shock by allowing water level to rise freely.

## Turbine Selection Guide

**Head-based selection**: High head (>100 m), low flow: Pelton wheel, the only practical choice. Medium head (10-300 m), medium flow: Francis turbine, the dominant choice for most hydroelectric sites. Low head (1-15 m), high flow: Kaplan turbine, for large rivers and low dams. Very low head (<3 m): Bulb turbine (Kaplan variant) for run-of-river on flat rivers.

**Flow variability consideration**: If the site has highly variable seasonal flow, Kaplan turbines maintain efficiency over a wider range (85%+ from 30-100% flow). Francis turbines have higher peak efficiency but drop off more steeply at part-load. Pelton wheels with multiple nozzles can shut off individual nozzles to maintain efficiency at reduced flow.

**Power calculation reminder**: The fundamental formula P = η × ρ × g × Q × H applies to all turbine types.

## Limitations

- **Site specificity**: Hydroelectric potential depends entirely on local geography (head and flow). Not all locations have viable hydro resources.
- **Seasonal variation**: River flow varies seasonally. Dry-season power output may be 20-50% of wet-season output, requiring seasonal storage or supplemental generation.
- **Environmental impact**: Dams alter river ecosystems, block fish migration, and change downstream sediment transport. Reservoir creation inundates land.
- **Sedimentation**: Reservoirs gradually fill with sediment, reducing storage capacity over 50-100+ years. Sediment management is an ongoing operational challenge.
- **Long construction time**: Dam and powerhouse construction is a multi-year civil engineering project requiring heavy equipment and skilled labor.
- **Freezing**: In cold climates, ice formation on intakes and draft tubes can block flow. Trash racks require heating or mechanical raking in winter.

## See Also

- [Energy Storage](storage.md) — Pumped hydroelectric storage
- [Pumped Hydro](pumped-hydro.md) — Large-scale energy storage using hydro infrastructure
- [Gravity Power](gravity.md) — Water wheels and early hydroelectric development
- [Steam Turbines](steam-turbines.md) — Turbine technology for thermal power
- [Electricity Generation](electricity.md) — Generators and power distribution


[← Back to Energy](index.md)
