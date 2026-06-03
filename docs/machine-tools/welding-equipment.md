# Welding Equipment

> **Node ID**: machine-tools.welding-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.electricity`](../energy/electricity.md), [`machine-tools.joining`](joining.md)
> **Enables**: [`construction.structural-engineering`](../construction/structural-engineering.md), [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.joining`](joining.md)
> **Timeline**: Years 15-30
> **Outputs**: welded_joints, cut_steel
> **Critical**: No — forge welding, brazing, and riveting can substitute for many structural applications, but arc and gas welding are faster, stronger, and enable fabrication of complex structures impossible by other methods

## Principle

Welding equipment generates the intense heat needed to melt and fuse metals. Two methods dominate the bootstrap sequence: oxy-acetylene welding (a 3100°C flame from combusted gases) and shielded metal arc welding (SMAW, a 6000°C electric arc between a consumable electrode and the workpiece). Oxy-acetylene requires gas production infrastructure (calcium carbide + water for acetylene, compressed oxygen) but no electricity. SMAW requires electrical power but no gas supply — the electrode coating generates its own shielding atmosphere. Both produce joints with tensile strength matching or exceeding the base metal.

This article covers the construction and setup of welding equipment. For welding technique and procedure, see [Joining](joining.md).

## Materials

### Oxy-Acetylene Welding Setup

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Brass or bronze (torch body) | 1-2 kg | Two control valves, mixing chamber, swappable tips | [Casting](casting.md) | Steel body (corrosion risk with moisture) |
| Copper (welding tips) | 0.5 kg | Orifice 0.5-3 mm, several sizes | [Forming](forming.md) | Brass tips (softer, wear faster) |
| Diaphragm regulators | 2 | Reduce cylinder pressure to working pressure | [Machining](machining.md) | Needle valves only (less precise control) |
| Rubber hoses with fabric reinforcement | 5-10 m | Color-coded: red = fuel, blue/green = oxygen | [Polymers](../polymers/elastomers.md) | Steel tubing (inflexible) |
| Steel cylinders (oxygen) | 1 | 40 L, rated to 15-20 MPa | [Forming](forming.md) | Cannot substitute — pressure vessel |
| Steel cylinders (acetylene) | 1 | 40 L, acetone-filled with porous mass, rated to 1.5 MPa | [Forming](forming.md) | Gas generator (on-demand acetylene) |
| Mild steel filler rod | 5-10 kg | 1.5-3 mm diameter, matching base metal | [Iron & Steel](../metals/iron-steel.md) | Cut strips from same material |

### SMAW (Arc Welding) Setup

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Welding power supply | 1 | 50-200 A DC or AC, 20-30 V arc, 60% duty cycle | [Electricity](../energy/electricity.md) | DC generator from motor/alternator |
| Electrode holder | 1 | Insulated handle, spring-loaded jaw, rated to 300 A | [Machining](machining.md) | Modified pliers with insulation (temporary) |
| Ground clamp | 1 | Heavy spring clamp, braided copper lead | [Iron & Steel](../metals/iron-steel.md) | Bolted ground connection |
| Welding cables | 5-10 m | #2 AWG copper, insulated, with terminals | [Electricity](../energy/electricity.md) | Cannot substitute — current capacity critical |
| Covered electrodes | 5-20 kg | E6013 (general) or E7018 (structural), 2.5-4.0 mm | [Chemistry](../chemistry/index.md) | Bare wire + external flux (unreliable) |
| Welding helmet | 1 | Shade #10-#14 filter lens | [Glass](../glass/index.md) | Fixed shade plate (no auto-darkening needed) |
| Chipping hammer | 1 | Hardened steel, pointed end + chisel end | [Iron & Steel](../metals/iron-steel.md) | Flat-head screwdriver (inferior) |
| Wire brush | 1 | Stiff steel bristles | [Iron & Steel](../metals/iron-steel.md) | — |
| Steel welding table | 1 | Flat steel plate, 600 × 600 mm minimum, grounded | [Iron & Steel](../metals/iron-steel.md) | Steel mesh grate over firebrick |

## Prerequisites

### Oxy-Acetylene Welding

- [Calcium carbide production](../energy/electric-furnaces.md) — electric arc furnace required (CaO + 3C → CaC₂ + CO at 2200°C)
- [Oxygen supply](../chemistry/index.md) — cryogenic air separation or chemical generation (barium oxide cycle)
- [Compressed gas cylinders](forming.md) — seamless steel, rated for gas service
- [Rubber hose production](../polymers/elastomers.md) — reinforced hose for gas transport

### SMAW (Arc Welding)

- [Electrical power supply](../energy/electricity.md) — minimum 5 kW for 150 A welding (DC generator, rectifier, or transformer)
- [Electrode production](../chemistry/index.md) — wire drawing + flux coating (cellulose, rutile, or limestone-based)
- [Welding cable](../energy/electricity.md) — heavy copper conductor with heat-resistant insulation

## Construction Steps

### Oxy-Acetylene Torch

1. **Cast or machine the torch body**: Cast a brass or bronze torch body, approximately 200 mm long, with two inlet ports (oxygen and acetylene), two needle valves, and a mixing chamber at the front. The mixing chamber is a cylindrical cavity where the two gases blend before reaching the tip. Machine the valve seats for gas-tight shutoff.
2. **Machine the welding tips**: Turn copper tips on the lathe with a precise internal orifice. Make a set of tips with orifice diameters 0.5, 1.0, 1.6, 2.0, and 3.0 mm. Thread the tip base to screw into the torch body. Smaller tips for thin metal, larger for thick. The tip must seat gas-tight against the torch body — any leak at the tip joint produces a secondary flame.
3. **Assemble the regulators**: Each regulator reduces cylinder pressure (oxygen: 15 MPa, acetylene: 1.5 MPa) to working pressure (oxygen: 0.1-0.5 MPa, acetylene: 0.01-0.1 MPa). The regulator body is brass, with a spring-loaded diaphragm and an adjustment screw. Two gauges per regulator: cylinder pressure and working pressure. The acetylene regulator must be a dedicated low-pressure type — never use an oxygen regulator on acetylene (or vice versa).
4. **Connect the hoses**: Green/blue hose to oxygen, red hose to acetylene. Left-hand thread on the acetylene connections (to prevent cross-connection). Right-hand thread on oxygen. Secure all connections with hose clamps.
5. **Set up the cylinders**: Secure both cylinders upright in a cart or chained to a wall. Install regulators. Connect hoses. Connect torch. Verify correct hose-to-valve matching before proceeding.

### SMAW Power Supply (DC Generator)

6. **Obtain or build a DC generator**: A DC motor run in reverse (driven by a prime mover) produces DC current suitable for welding. Alternatively, use a transformer-rectifier combination: step down AC mains voltage to 50-80 V open circuit, then rectify to DC with silicon diodes. Output: 50-200 A at 20-30 V arc voltage.
7. **Add current control**: Install a variable resistor (rheostat) in series with the output, or use a tapped transformer with multiple output taps (coarse adjustment). Fine adjustment via the rheostat. Calibrate the ammeter on the front panel by measuring output current with a clamp meter.
8. **Make the electrode holder**: Fabricate from an insulated handle (wood or phenolic resin), a spring-loaded jaw to grip the electrode, and a brass or copper conductor connecting the jaw to the cable terminal. The handle must insulate the operator from the welding circuit.
9. **Prepare the ground connection**: Attach a heavy braided copper lead to a spring clamp. The clamp must make clean metal-to-metal contact with the workpiece or welding table. Poor ground connection causes erratic arc and overheating at the connection point.

### Welding Table

10. **Build the welding table**: Weld a flat steel plate (600 × 600 × 10 mm) to a frame of angle iron. Attach a ground bolt to the plate. The table must be level and sturdy enough to support workpieces while allowing clamping. Place on a non-flammable floor (concrete or earth — not wood).

## Calibration and Verification

### Oxy-Acetylene

1. **Leak test**: Close all torch valves. Open cylinder valves. Apply soapy water to all connections — any bubble indicates a leak. Tighten or replace leaking connections. Zero leaks acceptable on acetylene (explosion risk).
2. **Flame adjustment**: Open torch acetylene valve, ignite with spark lighter. Adjust to a sooty flame ~50 mm long. Gradually open oxygen valve until the flame becomes neutral: sharp inner cone 2-5 mm, blue-white, with pale blue outer envelope. This is the ~3100°C welding flame.
3. **Test weld**: Weld a bead on scrap mild steel plate (3 mm). The bead should be smooth, convex, uniform width with no porosity, spatter, or undercut. Break the test coupon — the weld must not fail at the fusion line.

### SMAW

4. **Amperage calibration**: Set the current to 100 A. Weld a test bead on 6 mm mild steel plate with 3.2 mm E7018. Correct arc sound: frying bacon. Too loud with spatter: reduce amperage. Sticky, irregular arc: increase amperage.
5. **Penetration test**: Weld a butt joint on 6 mm plate with root gap. Break the joint and examine the cross-section — root penetration must be full through the plate thickness.
6. **Ground continuity**: Measure resistance between the ground clamp and the welding table surface with a multimeter. Resistance must be <0.1 Ω.

## Expected Performance

### Oxy-Acetylene Welding

| Parameter | Value |
|-----------|-------|
| Flame temperature | ~3100°C |
| Welding speed | 2-5 mm/second |
| Penetration per pass | 1-3 mm (full penetration up to 3 mm single pass) |
| Tensile strength | 300-450 MPa (mild steel) |
| Cutting speed (6 mm plate) | 200-500 mm/min |
| Maximum cutting thickness | 300+ mm steel |
| Gas consumption (welding) | Acetylene: 0.1-0.5 m³/hr; Oxygen: 0.1-0.5 m³/hr |

### SMAW (Arc Welding)

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

## Strengths

- Oxy-acetylene: portable, dual-purpose (welds and cuts), no electricity needed
- SMAW: simple equipment (power supply + electrodes), works outdoors in wind, all-position capability
- Both produce joints stronger than the base metal when executed correctly

## Weaknesses

- Oxy-acetylene requires gas production infrastructure (calcium carbide, oxygen)
- SMAW requires electrical power and electrode production
- Both produce wide heat-affected zones (5-15 mm) that distort thin sheet
- Fumes and UV radiation require ventilation and shielding

## Safety

- **Eye protection**: Welding helmet with shade #10-#14 filter lens for arc welding. Goggles with shade #5 for oxy-acetylene. UV radiation from the arc causes photokeratitis (welder's flash — 24-48 hours of extreme pain and temporary blindness).
- **Fire prevention**: Sparks travel 5-10 m from welding. Clear the area of combustibles for 10+ m. Keep fire extinguisher ready.
- **Fumes**: Welding produces metal oxide fumes, ozone, and (for some electrodes) hexavalent chromium. Ventilate or use fume extraction. Respirator (N95 minimum) for confined spaces.
- **Burns**: Molten metal spatter at 1500°C. Leather gloves (gauntlet length), leather apron or heavy cotton jacket (no synthetics — they melt onto skin).
- **Electrical shock** (SMAW): Open circuit voltage 50-80 V can be lethal in wet conditions. Keep dry. Insulate the operator from ground. Never weld in rain or standing water.

## See Also

- [Joining](joining.md) — welding technique, joint design, electrode selection, and procedure
- [Iron & Steel](../metals/iron-steel.md) — base metals for welding
- [Electricity](../energy/electricity.md) — power supply for arc welding
- [Electric Furnaces](../energy/electric-furnaces.md) — for calcium carbide production (oxy-acetylene)
- [Chemistry](../chemistry/index.md) — for electrode flux coating materials
- [Hydraulic Press](hydraulic-press.md) — press construction using welded frame

[← Back to Machine Tools](index.md)
