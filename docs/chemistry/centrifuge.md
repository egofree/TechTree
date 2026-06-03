# Centrifuge

> **Node ID**: chemistry.centrifuge
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`metals.bearings`](../machine-tools/bearings-abrasives.md)
> **Enables**: [`chemistry.fermentation`](fermentation.md), [`chemistry.water-treatment`](water-treatment.md), [`metals.metal-recycling`](../metals/metal-recycling.md)
> **Timeline**: Years 20-35
> **Outputs**: separated_solids, clarified_liquid
> **Critical**: No — filter presses and settling tanks can substitute for most centrifuge applications at lower throughput and higher labor cost

## Principle

A centrifuge separates solids from liquids (or two immiscible liquids) by applying centrifugal force many times greater than gravity. A rotating bowl or basket spins at 1,000-15,000 RPM, creating a radial acceleration of 500-15,000 × g. Solid particles denser than the liquid migrate outward to the bowl wall; clarified liquid remains in the center and overflows a weir or is discharged continuously. The separation efficiency depends on the particle size, density difference between solid and liquid, liquid viscosity, and the centrifugal force (proportional to RPM² × bowl radius).

Two main configurations serve chemical processing: **disc-stack centrifuge** (stack of closely spaced conical discs inside a bowl, continuous or semi-continuous, for fine particles and liquid-liquid separation) and **basket centrifuge** (perforated cylindrical basket lined with filter cloth, batch operation, for coarser particles and easier dewatering). The disc-stack centrifuge is the standard for fermentation broth clarification, oil-water separation, and catalyst recovery. The basket centrifuge is simpler to construct and suitable for crystalline product recovery.

The key engineering challenge is dynamic balancing. A rotating assembly at 5,000 RPM with even 1 gram of imbalance at 200 mm radius generates 55 N of vibration force. Precision balancing to ISO 1940 G6.3 or better is mandatory. Bearings must handle radial loads, axial loads, and the high-speed rotation with minimal vibration.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| [Stainless steel](../metals/iron-steel.md) (bowl) | 50-200 kg | 316L, centrifugally cast or fabricated, balanced | [Iron & Steel](../metals/iron-steel.md) | Titanium (corrosive), Hastelloy (acid service) |
| [Steel shaft](../metals/iron-steel.md) | 20-50 kg | 4140 or 316 SS, 40-80 mm diameter, ground and polished | [Iron & Steel](../metals/iron-steel.md) | — |
| [Bearings](../machine-tools/bearings-abrasives.md) | 2-4 units | Angular contact ball bearings, precision grade P5 or better | [Bearings](../machine-tools/bearings-abrasives.md) | Tapered roller bearings (higher load, lower speed) |
| [Electric motor](../energy/electricity.md) | 1 unit | 1-30 kW, 3-phase, 1,500-3,600 RPM (with belt drive for higher speed) | [Electricity](../energy/electricity.md) | Hydraulic motor (hazardous area) |
| [V-belts or gears](../machine-tools/machining.md) | 1 set | Step-up drive 1:2 to 1:5 ratio for bowl speed | [Machining](../machine-tools/machining.md) | Direct drive (motor at bowl speed — requires special motor) |
| [Filter cloth](../textiles/fibers.md) | 1-4 sheets | Polyester or polypropylene, 50-200 μm pore | [Textiles](../textiles/fibers.md) | Stainless mesh (reusable, finer filtration) |
| [Steel plate](../metals/iron-steel.md) (frame) | 100-300 kg | A36 structural, vibration-damped base | [Iron & Steel](../metals/iron-steel.md) | Cast iron base (heavier, better damping) |
| [Vibration isolators](../polymers/elastomers.md) | 4-8 units | Rubber or spring mounts, rated for centrifuge weight at operating speed | [Elastomers](../polymers/elastomers.md) | Concrete inertia block (stationary installation) |

## Construction Steps

### Basket Centrifuge (Simpler Design)

1. **Fabricate the basket**: Spin-form or fabricate a cylindrical bowl (200-600 mm diameter, 150-400 mm tall) from 316L stainless steel, 3-5 mm wall thickness. The bottom is solid; the top is open. Drill 3-6 mm diameter perforations over the cylindrical wall on 10-20 mm triangular pitch (15-30% open area). Machine the inside surface smooth (Ra <1.6 μm) for cleanability.

2. **Machine the shaft**: Turn the drive shaft from 4140 or 316 stainless steel bar stock. Diameter: 40-60 mm. The shaft must be straight within 0.02 mm over its full length. One end has a precision taper (Morse taper or custom) for mounting the basket; the other end has a keyway and pulley mounting surface.

3. **Mount bearings**: Install two angular contact ball bearings (precision grade P5 or better) in the bearing housing. Bearing arrangement: back-to-back (DB) configuration to handle both radial and axial loads. Preload the bearings per manufacturer specification to eliminate internal clearance at operating speed. The bearing housing is a rigid steel casting or weldment bolted to the frame.

4. **Assemble shaft and basket**: Mount the basket on the tapered shaft end. Secure with a locknut. Install a retaining collar. The basket-shaft assembly must be dynamically balanced: spin the assembly in a balancing machine at 50-70% of operating speed. Add or remove material (drill holes or weld weights) at the correction planes until imbalance is below ISO 1940 G6.3 grade (e.g., for a 20 kg rotor at 3,000 RPM, permissible imbalance per plane ≈ 20 g·mm).

5. **Fabricate the housing and frame**: Weld a cylindrical housing around the basket to contain any splashed liquid and direct filtrate to a drain. The housing has a hinged lid with a lock that prevents opening while the basket is spinning (safety interlock). Mount the bearing housing and motor on a rigid base frame with vibration isolator pads.

6. **Install drive system**: Mount the electric motor on adjustable slides. Install V-belt drive with step-up pulleys (motor pulley small, centrifuge pulley large) to achieve the target bowl speed: bowl RPM = motor RPM × (motor pulley diameter / centrifuge pulley diameter). For a 1,750 RPM motor and a 1:2 step-up, bowl speed = 3,500 RPM. Install a belt guard.

7. **Install filter media**: Line the inside of the perforated basket with filter cloth, secured at the top rim by a retaining ring. The cloth must overlap itself by at least 50 mm to prevent solids bypassing through gaps.

### Disc-Stack Centrifuge (Higher Performance)

8. **Fabricate the bowl**: Machine the bowl from a centrifugally cast 316L stainless steel blank (150-300 mm diameter). The bowl is a pressure vessel — it must withstand the centrifugal stress at operating speed. Minimum wall thickness: σ = ρ × ω² × R² / (2 × S), where ρ = material density, ω = angular velocity, R = bowl radius, S = allowable stress. At 10,000 RPM and 150 mm radius, the centrifugal stress in stainless steel is approximately 50-100 MPa — within allowable limits for 316L.

9. **Machine disc stack**: Cut 20-100 conical discs from 0.5-1.0 mm 316L stainless sheet. Each disc has a cone angle of 35-50° and 3-6 spacing pins (1-3 mm tall) welded to the upper surface to maintain disc separation. The disc stack provides a large settling area in a small volume: effective settling area = number of discs × disc area × (sin θ), where θ is the half-cone angle.

10. **Assemble bowl and disc stack**: Stack the discs on the central feed pipe inside the bowl. Secure the disc stack with a top nut. Install the bowl on the drive shaft. Dynamic balance the complete rotating assembly. Disc-stack centrifuge bowls typically operate at 5,000-15,000 RPM and require balancing to G2.5 grade (tighter than basket type).

11. **Install feed and discharge systems**: The feed slurry enters through the central feed pipe and is distributed to the disc stack. Clarified liquid (light phase) discharges through a top centripetal pump. Separated solids accumulate in the bowl periphery and are discharged either manually (batch), through nozzle ports at the bowl periphery (continuous), or by periodic full-bowl ejection (self-cleaning type).

## Calibration and Verification

1. **Vibration test**: Run the centrifuge at full speed unloaded (empty bowl). Measure vibration velocity at the bearing housing with a vibration meter. Acceptable: <2.5 mm/s RMS. Above 4.5 mm/s indicates imbalance, misalignment, or bearing damage — do not operate.

2. **Balance verification**: After any maintenance involving the rotating assembly, re-check dynamic balance. Run at 50%, 75%, and 100% of rated speed. Vibration must remain below 2.5 mm/s at all speeds.

3. **Separation test**: Process a test slurry of known particle size and concentration. Measure the solids content in the centrate (clarified liquid) and the cake. For a disc-stack centrifuge processing fermentation broth: centrate should have <0.5% suspended solids (from an initial 5-20% in the feed). For a basket centrifuge: cake solids should be 40-70% by weight after spin-drying.

4. **Motor current check**: Measure motor current at full load. Should not exceed motor nameplate rating. Excessive current indicates feed rate too high, solids loading too heavy, or bearing friction.

## Expected Performance

| Parameter | Basket Centrifuge | Disc-Stack Centrifuge |
|-----------|-------------------|----------------------|
| Bowl diameter | 200-600 mm | 150-300 mm |
| Operating speed | 1,000-3,500 RPM | 5,000-15,000 RPM |
| Centrifugal force | 500-2,000 × g | 5,000-15,000 × g |
| Minimum particle size separated | 5-20 μm | 0.5-5 μm |
| Throughput (liquid) | 0.5-10 m³/h | 1-50 m³/h |
| Cake solids (after spin) | 40-70% | 20-50% (solids discharge slurry) |
| Feed solids concentration | 5-50% | 0.1-20% |
| Cycle time (batch) | 10-60 min | — (continuous) |
| Motor power | 1-15 kW | 5-30 kW |
| Operation mode | Batch | Continuous or semi-continuous |
| Bearing life | 10,000-30,000 hours | 5,000-15,000 hours |

## Safety

- **Rotor burst**: A bowl failure at 10,000 RPM releases fragments with kinetic energy comparable to a small explosion. The centrifuge housing must contain a rotor burst without penetration. Reinforced steel housing, minimum 10 mm plate. Never operate with the lid open. Safety interlock prevents motor start with lid open.
- **Imbalance vibration**: Running an imbalanced centrifuge causes catastrophic bearing failure and possible structural damage. Install vibration switch: automatic motor shutdown if vibration exceeds trip level (typically 7-10 mm/s). Investigate and correct any imbalance before restarting.
- **Chemical exposure**: Centrifuge feed and discharge may contain corrosive or toxic chemicals. Seal all feed and discharge connections. Secondary containment under the centrifuge. PPE for chemical handling during basket cleaning and cloth replacement.
- **Pinch points and rotation**: The rotating basket is the primary hazard. Never reach into the housing while the basket is spinning (coasting down after motor stop counts). Mechanical brake or regenerative braking to stop the basket within 2-5 minutes. Do not open the lid until rotation has fully stopped.
- **Noise**: Centrifuges at 5,000+ RPM generate 80-95 dB noise. Hearing protection required in the operating area. Enclose the centrifuge in a sound-dampened housing for continuous operation.

## See Also

- [Filter Press](filter-press.md) — alternative solid-liquid separation (batch, lower cost)
- [Fermentation](fermentation.md) — cell and mycelium recovery from broth
- [Water Treatment](water-treatment.md) — sludge dewatering
- [Crystallizer](crystallizer.md) — crystal recovery by centrifugation

[← Back to Chemistry](index.md)
