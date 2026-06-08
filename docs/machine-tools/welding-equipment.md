# Welding Equipment

> **Node ID**: machine-tools.welding-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](../energy/electricity.md), [`machine-tools.joining`](joining.md)
> **Enables**: [`construction.structural-engineering`](../construction/structural-engineering.md), [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining`](joining.md)
> **Timeline**: Years 15-30
> **Outputs**: welded_joints, cut_steel
> **Critical**: No — forge welding, brazing, and riveting can substitute for many structural applications, but arc and gas welding are faster, stronger, and enable fabrication of complex structures impossible by other methods

## Overview

![Welding equipment - panoramio](../images/machine-tools/machine-tools_welding-equipment.jpg)

> *Image: ecom, CC BY-SA 3.0*

Welding equipment generates the intense heat needed to melt and fuse metals. Two methods dominate the bootstrap sequence: oxy-acetylene welding (a 3100°C flame from combusted gases) and shielded metal arc welding (SMAW, a 6000°C electric arc between a consumable electrode and the workpiece). Oxy-acetylene requires gas production infrastructure (calcium carbide + water for acetylene, compressed oxygen) but no electricity. SMAW requires electrical power but no gas supply — the electrode coating generates its own shielding atmosphere. Both produce joints with tensile strength matching or exceeding the base metal.

This article covers the construction and setup of welding equipment. For welding technique, joint design, and procedure, see [Joining](joining.md). For welded frame construction, see [Hydraulic Press](hydraulic-press.md) and [Machine Tools](./index.md).

Oxy-acetylene welding uses the combustion of acetylene (C₂H₂) in oxygen to produce a flame temperature of approximately 3100°C. The reaction is: 2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O + heat. In the neutral flame (correct oxygen-to-acetylene ratio), the inner cone reaches 3100°C and provides a localized, controllable heat source suitable for welding thin-to-medium plate (0.5-6 mm) and for cutting any thickness of ferrous metal. The oxy-acetylene torch also serves as a cutting tool: a separate oxygen jet oxidizes and blows away the steel, cutting at 200-500 mm/min in 6 mm plate. No other portable cutting method approaches this versatility.

SMAW generates heat from an electric arc between a consumable coated electrode and the workpiece. The arc temperature at the electrode tip reaches ~6000°C — hot enough to melt any structural metal. The electrode coating serves three functions: it decomposes to form a shielding gas (CO₂, H₂) that prevents atmospheric contamination of the molten weld pool; it deposits a slag coating over the solidifying weld that protects it from oxidation; and it stabilizes the arc by providing an ionized path. Different electrode coatings produce different welding characteristics: cellulose coatings (E6010) give deep penetration on dirty steel, rutile coatings (E6013) give smooth beads on clean sheet, and basic (low-hydrogen) coatings (E7018) give the highest tensile strength for structural work.

## Prerequisites

### Oxy-Acetylene Welding

- [Calcium carbide production](../energy/electric-furnaces.md) — electric arc furnace required (CaO + 3C → CaC₂ + CO at 2200°C)
- [Oxygen supply](../chemistry/index.md) — cryogenic air separation or chemical generation (barium oxide cycle)
- [Compressed gas cylinders](forming.md) — seamless steel, rated for gas service
- [Rubber hose production](../polymers/rubber.md) — reinforced hose for gas transport

### SMAW (Arc Welding)

- [Electrical power supply](../energy/electricity.md) — minimum 5 kW for 150 A welding (DC generator, rectifier, or transformer)
- [Electrode production](../chemistry/index.md) — wire drawing + flux coating (cellulose, rutile, or limestone-based)
- [Welding cable](../energy/electricity.md) — heavy copper conductor with heat-resistant insulation

## Bill of Materials

### Oxy-Acetylene Welding Setup

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Brass or bronze (torch body) | 1-2 kg | Two control valves, mixing chamber, swappable tips | [Casting](../metals/casting.md) | Steel body (corrosion risk) |
| Copper (welding tips) | 0.5 kg | Orifice 0.5-3 mm, several sizes | [Forming](forming.md) | Brass tips (softer, wear faster) |
| Diaphragm regulators | 2 | Reduce cylinder pressure to working pressure | [Machining](machining.md) | Needle valves only (less precise) |
| Rubber hoses with fabric reinforcement | 5-10 m | Color-coded: red = fuel, blue/green = oxygen | [Polymers](../polymers/rubber.md) | Steel tubing (inflexible) |
| Steel cylinders (oxygen) | 1 | 40 L, rated to 15-20 MPa | [Forming](forming.md) | Cannot substitute — pressure vessel |
| Steel cylinders (acetylene) | 1 | 40 L, acetone-filled with porous mass, rated to 1.5 MPa | [Forming](forming.md) | Gas generator (on-demand acetylene) |
| Mild steel filler rod | 5-10 kg | 1.5-3 mm diameter, matching base metal | [Iron & Steel](../metals/iron-steel.md) | Cut strips from same material |

### SMAW (Arc Welding) Setup

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Welding power supply | 1 | 50-200 A DC or AC, 20-30 V arc, 60% duty cycle | [Electricity](../energy/electricity.md) | DC generator from motor/alternator |
| Electrode holder | 1 | Insulated handle, spring-loaded jaw, rated to 300 A | [Machining](machining.md) | Modified pliers with insulation |
| Ground clamp | 1 | Heavy spring clamp, braided copper lead | [Iron & Steel](../metals/iron-steel.md) | Bolted ground connection |
| Welding cables | 5-10 m | #2 AWG copper, insulated, with terminals | [Electricity](../energy/electricity.md) | Cannot substitute — current capacity critical |
| Covered electrodes | 5-20 kg | E6013 (general) or E7018 (structural), 2.5-4.0 mm | [Chemistry](../chemistry/index.md) | Bare wire + external flux |
| Welding helmet | 1 | Shade #10-#14 filter lens | [Glass](../glass/index.md) | Fixed shade plate |
| Chipping hammer | 1 | Hardened steel, pointed end + chisel end | [Iron & Steel](../metals/iron-steel.md) | Flat-head screwdriver |
| Wire brush | 1 | Stiff steel bristles | [Iron & Steel](../metals/iron-steel.md) | — |
| Steel welding table | 1 | Flat steel plate, 600 × 600 mm minimum, grounded | [Iron & Steel](../metals/iron-steel.md) | Steel mesh grate over firebrick |

## Process Description

### Oxy-Acetylene Torch Construction

1. **Cast or machine the torch body**: Cast a brass or bronze torch body (~200 mm long) with two inlet ports (oxygen and acetylene), two needle valves, and a mixing chamber. Machine valve seats for gas-tight shutoff.
2. **Machine the welding tips**: Turn copper tips on the lathe with precise internal orifices (0.5, 1.0, 1.6, 2.0, 3.0 mm). Thread the tip base to screw into the torch body. The tip must seat gas-tight — any leak produces a secondary flame.
3. **Assemble the regulators**: Each regulator reduces cylinder pressure (oxygen: 15 MPa, acetylene: 1.5 MPa) to working pressure (oxygen: 0.1-0.5 MPa, acetylene: 0.01-0.1 MPa). Two gauges per regulator: cylinder pressure and working pressure. The acetylene regulator must be a dedicated low-pressure type — never interchange regulators.
4. **Connect the hoses**: Green/blue hose to oxygen (right-hand thread), red hose to acetylene (left-hand thread to prevent cross-connection). Secure with hose clamps.
5. **Set up the cylinders**: Secure both cylinders upright in a cart or chained to a wall. Install regulators. Connect hoses and torch. Verify correct hose-to-valve matching.

**Calibration**: Close all torch valves, open cylinder valves. Apply soapy water to all connections — any bubble indicates a leak. Zero leaks acceptable on acetylene (explosion risk). Light the torch: open acetylene valve, ignite with spark lighter. Adjust to a sooty flame ~50 mm long. Gradually open oxygen until the flame is neutral: sharp inner cone 2-5 mm, blue-white, pale blue outer envelope (~3100°C).

**Expected performance**: Flame temperature: ~3100°C. Welding speed: 2-5 mm/s. Penetration per pass: 1-3 mm. Cutting speed (6 mm plate): 200-500 mm/min.

**Strengths**:
- No electricity required — gas supply enables welding in locations without power
- Dual-purpose: welds and cuts with the same torch (swap tip for cutting attachment)
- Fine heat control via gas valves — suitable for thin sheet (0.5 mm) and brazing

**Weaknesses**:
- Requires calcium carbide production (2200°C electric furnace) and oxygen supply — heavy infrastructure
- Slower than arc welding on plate >3 mm — gas flame spreads heat over a wider zone, causing more distortion
- Acetylene is explosive above 0.15 MPa — cylinder handling and storage require strict safety protocols

### SMAW Power Supply Construction

6. **Obtain or build a DC generator**: A DC motor driven by a prime mover produces DC current suitable for welding. Alternatively, use a transformer-rectifier: step down AC to 50-80 V open circuit, rectify to DC with silicon diodes. Output: 50-200 A at 20-30 V arc voltage.
7. **Add current control**: Install a variable resistor (rheostat) in series with the output, or use a tapped transformer with multiple output taps. Calibrate the ammeter with a clamp meter.
8. **Make the electrode holder**: Fabricate from an insulated handle (wood or phenolic resin), spring-loaded jaw to grip the electrode, and brass/copper conductor connecting jaw to cable terminal. The handle must insulate the operator from the welding circuit.
9. **Prepare the ground connection**: Attach a heavy braided copper lead to a spring clamp. Clamp must make clean metal-to-metal contact with the workpiece. Poor ground causes erratic arc and overheating.
10. **Build the welding table**: Weld a flat steel plate (600 × 600 × 10 mm) to an angle iron frame. Attach a ground bolt to the plate. Place on a non-flammable floor (concrete or earth — not wood).

**Calibration**: Set current to 100 A. Weld a test bead on 6 mm mild steel plate with 3.2 mm E7018. Correct arc sound: frying bacon. Too loud with spatter: reduce amperage. Sticky, irregular arc: increase amperage. Measure ground resistance: <0.1 Ω between clamp and table surface.

**Expected performance**: Arc temperature: ~6000°C. Weld tensile strength: 350-480 MPa (E7018). Deposition rate: 1-3 kg/hour. Open circuit voltage: 50-80 V.

**Strengths**:
- Higher deposition rate than oxy-acetylene on plate >3 mm — arc concentrates heat in a smaller zone
- Electrode coating generates its own shielding gas — no separate gas supply needed
- Equipment is portable (generator + cables) and works outdoors in wind that would blow away gas shielding

**Weaknesses**:
- Requires electrical power (5 kW minimum) — limits use to locations with generator or grid access
- Slag removal required between passes — adds a cleaning step that gas welding does not need
- Electrode stub loss (50-60 mm unusable per rod) wastes 10-15% of consumable material

## Quantitative Parameters

### Oxy-Acetylene Parameters

| Parameter | Value |
|-----------|-------|
| Flame temperature | ~3100°C |
| Welding speed | 2-5 mm/second |
| Penetration per pass | 1-3 mm (full penetration up to 3 mm single pass) |
| Tensile strength | 300-450 MPa (mild steel) |
| Cutting speed (6 mm plate) | 200-500 mm/min |
| Maximum cutting thickness | 300+ mm steel |
| Gas consumption (welding) | Acetylene: 0.1-0.5 m³/hr; Oxygen: 0.1-0.5 m³/hr |

### SMAW Parameters

| Parameter | Value |
|-----------|-------|
| Arc temperature | ~6000°C |
| Weld tensile strength | 350-480 MPa (E7018 on mild steel) |
| Deposition rate | 1-3 kg/hour |
| Duty cycle | 60% at rated current |
| Electrode consumption | 0.5-1.0 electrodes per 100 mm weld (3.2 mm, 6 mm plate) |
| Open circuit voltage | 50-80 V |
| Arc voltage | 20-30 V |
| Current range | 50-300 A |

### Amperage vs. Material Thickness

| Material Thickness | Electrode Diameter | Amperage (E6013) | Amperage (E7018) |
|--------------------|--------------------|--------------------|--------------------|
| 1.5-2.0 mm | 2.0 mm | 40-70 A | — |
| 2.0-4.0 mm | 2.5 mm | 60-90 A | 70-100 A |
| 4.0-8.0 mm | 3.2 mm | 80-120 A | 90-140 A |
| 8.0-12 mm | 4.0 mm | 110-160 A | 120-180 A |
| 12-20 mm | 5.0 mm | 150-220 A | 160-240 A |

### Electrode Selection Guide

| Electrode | Coating Type | Current | Best For | Amperage (3.2 mm) |
|-----------|-------------|---------|----------|--------------------|
| E6010 | Cellulose | DC+ | Root passes, deep penetration on dirty steel | 80-130 A |
| E6011 | Cellulose | AC/DC | Same as E6010 but AC-compatible | 80-130 A |
| E6013 | Rutile | AC/DC | General-purpose, easy to strike, thin sheet | 70-120 A |
| E7018 | Basic (low-hydrogen) | AC/DC+ | Structural steel, high-strength joints | 90-140 A |
| E7024 | Iron powder | AC/DC | High-deposition flat welding | 110-170 A |

### Oxy-Acetylene Flame Types

| Flame Type | O₂:C₂H₂ Ratio | Inner Cone | Temperature | Application |
|------------|---------------|------------|-------------|-------------|
| Carburizing (excess acetylene) | <1:1 | Long, feathered | ~2800°C | Soft soldering, silver brazing, surface carburizing |
| Neutral | 1:1 | Sharp, 2-5 mm | ~3100°C | Steel welding (standard), brazing |
| Oxidizing (excess oxygen) | >1:1 | Short, pointed | ~3300°C | Brass welding, cutting |

## Scaling Notes

- A 150 A DC welding set handles plate up to 12 mm with multiple passes. This covers most structural fabrication needs.
- Scale to 300+ A for heavy plate (>12 mm) and production fillet welding. Higher current requires larger cables (#2/0 AWG) and a higher-capacity power source.
- Oxy-acetylene cutting scales to any thickness — the flame cuts by oxidizing the steel, so cutting speed depends on kerf width and oxygen flow, not equipment size. A cutting torch attachment replaces the welding tip on the same torch body.
- Multiple welders can work simultaneously from a single power source using a multiple-operator welding system — a transformer with multiple output stations.
- A simple battery bank (12 V, 200+ Ah) can serve as a crude DC welding source for thin sheet (1-3 mm) at 80-120 A. Not suitable for structural work but functional for field repair.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Porosity (small holes in weld bead) | Contaminated base metal; damp electrodes; insufficient shielding | Clean joint surfaces to bright metal; dry electrodes at 100°C for 1 hour; increase arc length slightly for E7018 |
| Undercut (groove at weld toe) | Excessive amperage; too fast travel speed; incorrect electrode angle | Reduce amperage 10-15%; slow travel speed; hold electrode at 10-15° from vertical with 5-10° drag |
| Spatter (droplets around weld) | Arc too long; amperage too high; dirty surface | Shorten arc to 2-3 mm; reduce amperage; clean base metal |
| Incomplete penetration | Insufficient amperage; root gap too narrow; wrong electrode | Increase amperage 10%; open root gap to 1-2 mm; use E6010 for open-root welding |
| Cracking (hot or cold) | High restraint; hydrogen in weld metal; rapid cooling | Use E7018 (low-hydrogen); preheat thick sections (>12 mm) to 100-150°C; fill crater at weld end |
| Erratic arc (SMAW) | Poor ground; contaminated electrode; worn cable connections | Clean ground contact; replace damp/damaged electrode; tighten cable terminals |
| Backfire (oxy-acetylene) | Tip overheating; incorrect pressure; tip partially blocked | Cool tip in water; verify pressure settings; clean tip orifice with proper tip cleaner |
| Uneven weld bead (oxy-acetylene) | Uneven travel speed; inconsistent filler feed | Practice consistent travel speed (2-5 mm/s); feed filler rod at a steady rate; rest the hand on a support for stability |
| Arc blow (arc wanders, SMAW) | Magnetic fields deflecting arc in DC welding | Switch to AC; weld toward the ground clamp; wrap the ground cable around the workpiece; use a heavier ground connection |

## Safety

- **Eye protection**: Welding helmet with shade #10-#14 filter lens for arc welding. Goggles with shade #5 for oxy-acetylene. UV radiation from the arc causes photokeratitis (welder's flash — 24-48 hours of extreme pain and temporary blindness). Even brief arc flashes without protection cause injury.
- **Fire prevention**: Sparks travel 5-10 m from welding. Clear the area of combustibles for 10+ m. Keep a Class ABC fire extinguisher within arm's reach. Hot slag can smolder in cracks and crevices for hours before igniting.
- **Fumes**: Welding produces metal oxide fumes (iron oxide, manganese), ozone, and hexavalent chromium (from stainless electrodes). Ventilate or use fume extraction. Respirator (N95 minimum) for confined spaces. Manganese exposure causes manganism (Parkinson's-like neurological damage).
- **Burns**: Molten metal spatter at 1500°C. Leather gloves (gauntlet length), leather apron or heavy cotton jacket (no synthetics — they melt onto skin). Sparks down the boot cuff are a common burn site — lace boots to the top.
- **Electrical shock** (SMAW): Open circuit voltage 50-80 V can be lethal in wet conditions. Keep dry. Insulate from ground. Never weld in rain or standing water. Replace cracked or damaged cable insulation immediately.
- **Cylinder handling**: Secure oxygen and acetylene cylinders upright. Never expose acetylene cylinders to >40°C. Open acetylene cylinder valve no more than 1.5 turns. Never use oil on oxygen fittings — oil + pressurized oxygen = explosion. Acetylene is unstable above 0.2 MPa; cylinders contain acetone to dissolve the gas safely.

## Quality Control

1. **Visual inspection**: Check every weld bead for porosity, undercut, spatter, incomplete fusion, and cracks. The bead should be uniform width with a slightly convex profile. Reject any weld with visible cracks or undercut >1 mm.
2. **Penetration test**: For structural joints, weld a test coupon of the same thickness and joint configuration. Break the coupon and examine the cross-section — root penetration must be full through the plate thickness.
3. **Dimensional check**: Measure fillet weld leg length with a weld gauge. Minimum leg length must meet specification (typically equal to the thinner plate thickness for structural joints).
4. **Electrode storage**: E7018 electrodes absorb moisture from air, which causes hydrogen cracking. Store in a rod oven at 120°C. If electrodes have been exposed to humid air for >4 hours, re-dry at 260°C for 1 hour before use.
5. **Weld positioner alignment**: When welding structural joints, verify fit-up before welding: root gap 1-2 mm for open-root joints, root face even on both sides, no mismatch >1.5 mm. Poor fit-up produces defective welds regardless of technique.
6. **Gas flow verification (oxy-acetylene)**: Check regulator gauges before each session. Acetylene working pressure must never exceed 0.15 MPa (acetylene becomes unstable above 0.2 MPa). Oxygen working pressure: 0.1-0.5 MPa. Verify flame character: neutral flame has a sharp inner cone ~2-5 mm long; a feathered inner cone indicates excess acetylene (carburizing); a short, pointed inner cone indicates excess oxygen (oxidizing).

## Variations and Alternatives

- **SMAW vs. oxy-acetylene**: SMAW is faster, produces stronger joints, and requires only electricity and electrodes. Oxy-acetylene is portable, dual-purpose (welds and cuts), and works without electricity. Build both capabilities for maximum flexibility.
- **Gas tungsten arc welding (GTAW/TIG)**: Uses a non-consumable tungsten electrode with separate filler rod and inert gas (argon) shielding. Produces the highest-quality welds but requires argon supply and more skill. Build SMAW capability first.
- **Gas metal arc welding (GMAW/MIG)**: Uses a continuous wire feed with inert gas shielding. Faster than SMAW for production work but requires wire feed mechanism and gas supply. Build SMAW first.
- **Forge welding**: The oldest method — heat steel to 1100-1300°C in a forge and hammer the joint. No electricity or gas required. Limited to low-carbon steel. Produces joints with 80-90% of base metal strength. See [Joining](joining.md).
- **Brazing**: Joins metals using a filler (brass, bronze, or silver alloy) that melts below the base metal melting point. Lower temperature, lower distortion, but lower joint strength (typically 300-500 MPa for silver braze). See [Joining](joining.md).
- **Resistance welding**: Passes high current (500-20,000 A) through the workpiece contact point, generating enough resistance heat to melt a small weld nugget. Used for sheet metal lap joints. Requires a heavy-duty transformer and copper electrodes. Fast (0.1-1 second per weld) but limited to overlapping sheet joints.
- Edge preparation for structural welding: Plate edges >3 mm thick require beveling (30-37.5° single-V or double-V) to achieve full penetration. For a 6 mm plate, a single-V groove with 1-2 mm root gap and 1 mm root face produces a sound full-penetration weld in 2-3 passes. Unbeveled square-butt joints are limited to plate <3 mm.
- Weld joint strength: A properly executed E7018 weld on mild steel develops tensile strength of 480-550 MPa — exceeding the base metal strength (typically 350-450 MPa for A36). The weld metal is stronger than the base metal; failure occurs in the heat-affected zone (HAZ) adjacent to the weld, where the base metal has been thermally cycled.
- Electrode consumption estimation: For a 3.2 mm E7018 electrode welding 6 mm plate, each electrode deposits approximately 300 mm of weld bead. A 100 mm fillet weld consumes 0.3-0.5 electrodes. For a full-day structural welding session (8 hours at 60% duty cycle), plan 3-5 kg of electrode consumption.
- Storage of compressed gases: Oxygen cylinders store gas at 15 MPa. Acetylene cylinders store dissolved acetylene at 1.5 MPa in an acetone-filled porous matrix. Store both upright, secured with chains, in a well-ventilated area away from heat sources (>40°C causes acetylene cylinders to become unstable). Separate oxygen and fuel-gas cylinders by at least 6 m or a fire-rated barrier. Never roll cylinders — transport on a cart with the cylinder secured upright.
- Welding position: Flat (1G) welding is the easiest and fastest — gravity holds the molten pool in place. Horizontal (2G), vertical (3G), and overhead (4G) positions require lower amperage (10-15% reduction) and faster travel speed to prevent the molten pool from sagging. Practice flat welding until consistent before attempting out-of-position work. E7018 electrodes produce better out-of-position welds than E6013 due to the faster-freezing basic slag.

## References

- [Joining](joining.md) — welding technique, joint design, electrode selection, and procedure
- [Iron & Steel](../metals/iron-steel.md) — base metals for welding
- [Electricity](../energy/electricity.md) — power supply for arc welding
- [Electric Furnaces](../energy/electric-furnaces.md) — for calcium carbide production (oxy-acetylene)
- [Chemistry](../chemistry/index.md) — for electrode flux coating materials
- [Hydraulic Press](hydraulic-press.md) — press construction using welded frame
- [Forge Hammer](forge-hammer.md) — alternative joining by forge welding

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*
