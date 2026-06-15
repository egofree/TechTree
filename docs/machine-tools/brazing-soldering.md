# Brazing & Soldering

> **Node ID**: machine-tools.joining.brazing-soldering
> **Domain**: [Machine Tools Bootstrap](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`metals.alloys`](../metals/alloys.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Enables**: [`energy.steam-power`](../energy/steam-power.md)
> **Timeline**: Years 5-30
> **Outputs**: brazed_joints, soldered_joints
> **Critical**: No — filler alloy joining methods where the base metal does not melt

Brazing and soldering join metals using a filler alloy that melts below the base metal's melting point. Brazing uses fillers melting above 450°C (brass, silver alloys) for structural joints. Soft soldering uses low-melting alloys (tin-lead, tin-silver) below 450°C for electrical connections, plumbing, and sheet metal seams. For fusion and solid-state welding processes, see [Welding](./welding.md). For mechanical fastening with rivets, see [Riveting](./riveting.md). For the parent overview, see [Metal Joining](./joining.md).

## Brazing

Brazing joins metals using a filler alloy that melts above 450°C but below the melting point of the base metal. Capillary action draws molten filler into the joint gap. The base metal never melts, which means dissimilar metals can be joined and heat distortion is minimal.

**Brass brazing (spelter brazing)**:
- **Filler alloy**: Brass (copper-zinc). Typical composition: 60% Cu / 40% Zn (melts ~900°C, flows at ~950°C). Produce by alloying copper and zinc in a crucible — see [Iron & Steel](../metals/iron-steel.md) for copper and zinc sourcing.
- **Flux**: Borax paste (borax + water). Melts at ~743°C, dissolves oxides, allows filler to wet and flow.
- **Joint clearance**: 0.05-0.20 mm (total gap). Too tight — filler cannot enter. Too wide — capillary action fails, filler pools. Precision matters.
- **Heating method**: Forge or torch. Heat entire joint area uniformly to bright red (~950°C). Apply brazing rod — brass melts on contact, flows into joint by capillary action. The joint should fill completely — visible as a continuous fillet at both ends.
- **Joint strength**: Shear strength ~150-250 MPa in the filler. Stronger than soft solder by 5-10×.
- **Applications**: Bicycle frames, tool handles, pipe fittings, tank seams, cast iron repairs (cast iron is difficult to forge weld but braze-joins well), joining dissimilar metals (steel to copper, steel to brass).

**Construction steps for a brass-brazed lap joint**:
1. Clean both joint surfaces to bright metal with abrasive cloth or file. Remove all oxide, oil, and dirt — contamination prevents filler wetting.
2. Position the parts with 0.05-0.20 mm joint clearance. Clamp or wire the parts together to maintain alignment during heating.
3. Apply borax flux paste to the joint area, coating both surfaces and the joint line.
4. Heat the joint area uniformly with a forge or torch. Bring the entire joint to bright red (~950°C). Heat the base metal, not the filler — the hot base metal melts the filler on contact.
5. Touch the brazing rod to the joint edge. The brass melts and flows into the gap by capillary action. Feed rod until a continuous fillet appears at both ends of the joint.
6. Allow the joint to cool slowly in still air. Do not quench — thermal shock cracks the brittle brass filler.

**Calibration**: Inspect the joint visually — a continuous fillet of brass should be visible at both ends of the joint with no gaps, voids, or bare spots. Pull-test a sample joint: brass-brazed mild steel lap joint fails at 150-250 MPa shear stress in the filler.

**Expected performance**: Shear strength: 150-250 MPa. Temperature resistance: up to ~300°C continuous (filler weakens above this). Joint clearance: 0.05-0.20 mm. Brazing temperature: 900-950°C.

**Materials specifications**: Brass brazing rod (60% Cu / 40% Zn, 1.5-3 mm diameter), borax flux (powder, mixed with water to paste consistency), mild steel or copper workpieces.

**Strengths**:
- Joins dissimilar metals — steel to copper, steel to brass, cast iron to steel
- Low distortion — base metal never melts, heat-affected zone is narrow
- Filler flows by capillary action into complex joint geometries, producing a continuous seal

**Weaknesses**:
- Joint is limited to ~300°C service temperature — brass filler softens above this
- Joint clearance must be precisely controlled (0.05-0.20 mm) — too tight or too wide and capillary action fails
- Brass filler contains zinc — heating above 900°C generates toxic zinc oxide fumes, requiring ventilation

**Silver brazing (silver soldering, hard soldering)**:
- **Filler alloy**: Silver-copper-zinc ternary. Compositions and melting ranges:
  - Easy-flo: 50% Ag / 15% Cu / 35% Zn — melts 620-690°C. Lowest temperature, flows easily.
  - Medium: 45% Ag / 30% Cu / 25% Zn — melts 670-740°C. Good general-purpose.
  - Hard: 75% Ag / 20% Cu / 5% Zn — melts 740-780°C. Highest strength, highest cost.
- **Flux**: Borax-based or fluoride-based paste. Fluoride fluxes are more aggressive at dissolving stubborn oxides (stainless steel, nickel alloys) but produce toxic fumes — use with ventilation.
- **Advantages over brass brazing**: Lower temperature (less thermal distortion), narrower joint gap capability, stronger joints in thin-wall assemblies. Critical for instrument work, jewelry, and fine mechanisms.
- **Cost consideration**: Silver is expensive. Reserve silver brazing for applications where the lower temperature or higher strength justifies the cost.

**Strengths**:
- Lower temperature than brass brazing (620-780°C vs. 900-950°C) — less thermal distortion
- Higher joint strength (150-300 MPa shear) with narrower joint gaps
- Excellent for thin-wall assemblies and fine mechanisms

**Weaknesses**:
- Silver is expensive — filler cost is 10-50× that of brass brazing rod
- Fluoride fluxes produce toxic fumes requiring forced ventilation
- Narrow melting range on some alloys requires precise temperature control

## Soft Soldering

The lowest-temperature joining method. Soldering fills joints with a low-melting alloy (below 450°C, typically 180-250°C). The resulting joint is mechanically weaker than brazing or welding but sufficient for electrical connections, plumbing, and sheet metal seams.

**Solder alloys**:
- **Tin-lead (Sn-Pb)**: The classic solder. 60/40 Sn/Pb melts at 183-190°C (eutectic 63/37 melts sharply at 183°C). 50/50 melts at 183-215°C (pasty range). Produce by melting tin and lead together in an iron ladle. Tin from cassiterite (SnO₂) reduction; lead from galena (PbS) roasting and smelting.
- **Lead-free alternatives**: Tin-silver (Sn-3.5% Ag, melts ~221°C), tin-copper (Sn-0.7% Cu, melts ~227°C), tin-bismuth (Sn-42% Bi, melts ~139°C — low-temperature applications). These require sourcing silver, copper, or bismuth.

**Flux types**:
- **Rosin (colophony)**: Purified pine resin. Dissolves thin oxide layers at soldering temperature. Non-corrosive, non-conductive — safe for electronics. Does NOT clean heavily oxidized or dirty surfaces.
- **Zinc chloride (killed spirits)**: Dissolve zinc metal in hydrochloric acid until bubbling stops. Aggressive flux — removes heavy oxidation. MUST be washed off after soldering or it corrodes the joint. Used for plumbing and sheet metal work.
- **Plumbing flux (tallow + sal ammoniac)**: Rendered fat mixed with ammonium chloride. Greasy paste that sticks to pipe surfaces, cleans oxides, and displaces water. Standard for copper pipe soldering.

**Construction steps for a soldered copper pipe joint**:
1. Clean the outside of the pipe and the inside of the fitting with abrasive cloth or wire brush to bright metal. Clean at least 10 mm beyond the joint depth.
2. Apply flux to both cleaned surfaces. Use rosin flux for electronics, zinc chloride or tallow/sal ammoniac for plumbing.
3. Assemble the joint — push the pipe fully into the fitting. Twist slightly to spread the flux evenly.
4. Heat the joint with a torch (propane or butane, flame temperature ~1900°C). Heat the fitting, not the pipe — the fitting mass conducts heat to the joint. Touch solder to the joint edge — when the joint is hot enough, solder melts and flows into the gap by capillary action (the "sweat" method).
5. Feed solder until a continuous fillet appears around the entire joint circumference. Remove heat.
6. Hold the joint still until the solder solidifies (2-5 seconds). Movement during solidification produces a weak, crystalline ("cold") joint with matte, grainy appearance instead of bright, shiny surface.

**Calibration**: Inspect the joint — solder fillet should be continuous, smooth, and shiny. A dull, grainy fillet indicates a "cold" joint (moved during solidification or insufficient heat). Pressure-test plumbing joints at 1.5× working pressure (hold for 15 minutes, no leaks). Electrical joints: pull-test with 10 N force — the wire must not separate from the terminal.

**Expected performance**: Joint shear strength: 20-50 MPa (Sn-Pb). Service temperature: up to ~120°C continuous (60/40 Sn-Pb softens above 150°C). Soldering temperature: 220-260°C for 60/40 Sn-Pb. Joint gap: 0.05-0.15 mm for capillary flow.

**Materials specifications**: Tin-lead solder (60/40 Sn/Pb, 1-3 mm diameter wire with rosin core for electronics, or bar solder for plumbing), rosin flux (electronics) or zinc chloride flux (plumbing), propane torch, abrasive cloth.

**Strengths**:
- Lowest temperature joining method — minimal heat distortion, safe for heat-sensitive components
- Excellent for electrical connections — low resistance, reliable contact
- Simple equipment — soldering iron or small torch suffices

**Weaknesses**:
- Low mechanical strength (20-50 MPa shear) — not suitable for structural loads
- Lead-containing solders are toxic — lead exposure causes neurological damage, especially in children
- Service temperature limited to ~120°C — joints weaken and fail above 150°C

## Prerequisites & Bill of Materials

**Prerequisites**:
- [Copper and zinc production](../metals/iron-steel.md) for brass brazing rod
- [Silver sourcing](../metals/alloys.md) for silver brazing alloys (optional, for fine work)
- [Tin and lead production](../metals/alloys.md) for soft solder
- [Borax](../chemistry/index.md) for brazing flux
- Forge or torch capable of reaching 950°C for brass brazing
- Soldering iron or propane torch for soft soldering (250°C)

**Bill of Materials**:

| Item | Specification | Quantity per Session | Source |
|------|--------------|---------------------|--------|
| Brass brazing rod | 60% Cu / 40% Zn, 1.5-3 mm dia | 0.5-2 m | Alloy copper + zinc in crucible |
| Borax flux | Powder, mixed with water to paste | 50-200 g | Natural mineral deposit |
| Silver brazing alloy | 45-50% Ag, Cu, Zn, 1-2 mm wire | 0.1-0.5 m | Silver + copper + zinc alloy |
| Tin-lead solder | 60/40 Sn/Pb, 1-3 mm wire | 0.5-2 m | Tin + lead alloy |
| Rosin flux | Pine resin, purified | 20-50 g | Pine tree resin distillation |
| Zinc chloride flux | Zn dissolved in HCl | 50-100 mL | Zinc + hydrochloric acid |
| Propane torch | Flame temp ~1900°C | 1 unit | Petroleum refining + compressed gas |
| Abrasive cloth | 80-120 grit | 0.5-1 sheet | Sand/grit on cloth backing |

## Scaling Notes

Brazing and soldering scale from individual bench work to production lines:

- **Workshop scale**: Single torch or forge, hand-fed filler rod. One operator produces 10-50 joints per hour depending on complexity. Adequate for maintenance, prototyping, and small-batch fabrication.
- **Production scale**: Multiple torch stations or conveyorized furnace brazing. Furnace brazing heats assemblies in a controlled-atmosphere furnace (hydrogen or dissociated ammonia atmosphere to prevent oxidation), with pre-placed brazing preforms (rings, washers, or paste). Production rate: 100-1000 joints per hour. Used for heat exchangers, automotive radiators, and tool fabrication.
- **Electronics assembly scale**: Wave soldering (PCBs passed over a wave of molten solder) or selective soldering (robotic soldering iron). Requires precise temperature control (250±10°C) and flux management. Production rate: 500-5000 joints per hour.

**Critical bottleneck**: Silver availability. Silver brazing alloys are 10-50× more expensive than brass filler. Reserve silver brazing for applications where lower temperature or finer joints justify the cost. Brass brazing with borax flux handles 90% of structural joining needs at a fraction of the cost.

## Quality Control

Brazed and soldered joints are verified by visual, mechanical, and leak testing:

1. **Visual inspection**: Brazed joint — continuous fillet of brass visible at both ends of the joint, no gaps, voids, or bare spots. The fillet should be smooth and concave, not convex (convex fillet indicates insufficient heat or too-wide gap). Soldered joint — bright, shiny, smooth fillet. Dull, grainy, or crystalline appearance indicates a "cold" joint (moved during solidification or insufficient heat).

2. **Mechanical testing**: Pull-test sample joints from each batch. Brass-brazed mild steel lap joint: must withstand 150-250 MPa shear stress in the filler. Silver-brazed joint: 150-300 MPa. Soft soldered joint: 20-50 MPa. Test at least one sample per batch; for critical applications, test three samples and average.

3. **Leak testing (plumbing and pressure joints)**: Pressurize with water at 1.5× working pressure. Hold for 15 minutes minimum. No leaks, no pressure drop. For gas joints, use soap bubble test at working pressure. For high-vacuum brazed joints, helium leak test to 10⁻⁹ mbar·L/s.

4. **Cross-section metallography** (production quality control): Cut a sample joint, mount, polish, and etch. Inspect at 50-200× magnification for voids, incomplete fill, and filler-base metal interaction. Voids >5% of joint area reject the batch.

5. **Capillary flow test**: For new joint designs, assemble a test joint with a glass plate replacing one metal surface. Heat and apply filler. Observe filler flow through the transparent glass to verify capillary action fills the gap completely.

## Variations and Alternatives

| Joining Method | Temp (°C) | Joint Strength (MPa) | Gap Tolerance (mm) | Dissimilar Metals | Best For |
|---------------|-----------|---------------------|--------------------|--------------------|----------|
| Soft solder (Sn-Pb) | 180-250 | 20-50 | 0.05-0.15 | Yes | Electronics, plumbing, sheet metal |
| Silver braze | 620-780 | 150-300 | 0.03-0.13 | Yes | Instruments, fine mechanisms |
| Brass braze | 870-950 | 150-250 | 0.05-0.20 | Yes | Structural joints, cast iron repair |
| Forge weld | 1200-1300 | 250-400 | N/A (pressure) | No (same metal only) | Iron/steel bars, chains |
| Arc weld (SMAW) | ~6000 arc | 350-480 | N/A (filler) | Limited | Structural steel, heavy fab |
| Riveting | Cold/900°C | 80-150 (shear) | N/A | Yes | Boilers, bridges, ship hulls |

## Method Selection Guide

| Method | Temp Range | Joint Strength | Equipment | Best For |
|--------|-----------|---------------|-----------|----------|
| Soft soldering | 180-250°C | 20-50 MPa | Soldering iron, flux | Electrical connections, plumbing, sheet metal seams |
| Silver brazing | 620-780°C | 150-300 MPa | Torch, silver alloy, flux | Fine mechanisms, instruments, dissimilar metals |
| Brass brazing | 870-950°C | 150-250 MPa | Forge/torch, brass rod, borax | Structural joints, cast iron, pipe fittings |

## Safety

- **Eye protection**: Safety glasses (ANSI Z87.1 rated) at all times. Goggles or face shield for grinding and wire brushing.
- **Fire prevention**: Hot metal, sparks, and slag are ignition sources. Clear the area 10+ m of combustibles. Have water bucket, sand, and fire extinguisher ready.
- **Burns**: All brazing and soldering methods involve temperatures above 180°C. Use pliers, tongs, and gloves to handle hot work.
- **Fumes and ventilation**: Soldering fumes (lead, flux acids), brazing fumes (zinc oxide from brass — causes "metal fume fever," flu-like symptoms for 24 hours). Work in well-ventilated areas. Respirators (N95 minimum) for confined-space work. Forced ventilation or fume extraction for enclosed spaces.
- **Lead safety**: Lead-containing solders are toxic. Wash hands after handling. Do not eat or drink in soldering areas. Lead exposure causes neurological damage, especially in children.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Brass-brazed joint has gaps/voids in fillet (incomplete capillary fill) | Joint clearance outside 0.05-0.20 mm range, or base metal not heated uniformly to ~950°C bright red | Adjust joint gap to 0.05-0.20 mm using shims; heat entire joint area uniformly (heat the base metal, not the filler); verify filler flows by capillary action — continuous fillet must appear at both ends |
| Soldered copper pipe joint leaks under 1.5× working pressure test | Cold joint (moved during solidification), or surfaces not cleaned to bright metal beyond 10 mm from joint edge | Reheat and re-solder: clean both surfaces to bright metal with abrasive cloth; hold joint still 2-5 seconds after removing heat; look for bright, shiny fillet (dull/grainy = cold joint — remelt and redo) |
| Silver braze filler balls up instead of flowing into joint | Insufficient flux coverage, or base metal temperature too low for capillary wetting | Apply flux to all joint surfaces before heating; heat base metal (not filler) until flux turns glassy and clear; touch filler rod to joint — it should melt and flow by capillary action |
| Zinc oxide fume exposure causes "metal fume fever" (chills, fever 4-8 hrs after brazing) | Overheating brass filler above 950°C generates copious ZnO fume | Maintain brazing temperature at 900-950°C (bright red, not yellow-white); use local exhaust ventilation at the joint; wear N95 respirator if ventilation is inadequate |
| Solder won't wet copper surface (beads up instead of spreading) | Surface oxidation or contamination preventing solder adhesion | Re-clean to bright metal with abrasive cloth; apply fresh flux immediately after cleaning; do not touch cleaned surfaces with bare fingers (skin oils prevent wetting) |

## Cross-References

- [Welding](./welding.md) — fusion and solid-state welding processes
- [Riveting](./riveting.md) — mechanical fastening with rivets
- [Metal Joining](./joining.md) — parent overview of all joining methods
- [Iron & Steel](../metals/iron-steel.md) — base metals and copper/zinc sourcing
- [Chemistry Index](../chemistry/index.md) — flux chemistry
- [Electricity](../energy/electricity.md) — power for torch operations

---

*Part of the [Bootciv Tech Tree](../index.md) · [Machine Tools Bootstrap](./index.md) · [Metal Joining](./joining.md) · [All Domains](../index.md)*

## See Also

- [Joining](joining.md) — mechanical and thermal joining methods
- [Machine Tools Index](./index.md) — overview of all machine tool capabilities
