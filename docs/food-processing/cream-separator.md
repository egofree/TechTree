# Cream Separator

> **Node ID**: food-processing.cream-separator
> **Domain**: [Food Processing](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md), [`food-processing.dairy`](dairy.md)
> **Enables**: efficient butter and cream production at village scale
> **Timeline**: Years 15-25
> **Outputs**: cream (20-50% fat), skim milk (<0.1% fat)
> **Critical**: No — gravity separation works but takes 12-24 hours; the separator processes milk in seconds

## Principle

A centrifugal cream separator exploits the density difference between milk fat (0.93 g/cm³) and milk serum (1.036 g/cm³) in a high-speed rotating bowl. When milk enters a spinning bowl at 6,000-8,000 rpm, centrifugal force pushes the denser skim milk outward while the lighter cream migrates inward. The two streams are collected separately as they discharge at different radii.

The key innovation (Gustaf de Laval, 1878) is the disc stack: a series of conical stainless steel discs spaced 0.5-1.0 mm apart, stacked inside the bowl. The narrow gap between discs dramatically shortens the distance fat globules must travel to reach the cream layer. Without discs, separation in a simple bowl requires very high rpm (15,000+) and produces incomplete separation. With discs, separation is complete at 6,000-8,000 rpm in a compact bowl.

Centrifugal force at the bowl rim: F_c = m × ω² × r, where ω = 2π × rpm/60. At 7,000 rpm with a 100 mm bowl radius, centrifugal acceleration is approximately 5,400× gravity. This extreme force separates cream from skim in seconds rather than the 12-24 hours required for gravity settling.

## Prerequisites

- [Stainless steel or tinned copper](../metals/iron-steel.md) — all milk-contact surfaces must be non-reactive and smooth
- [Precision machining](../machine-tools/machining.md) — bowl boring to ±0.02 mm, dynamic balancing to ±0.01 mm
- [Bearings](../machine-tools/bearings-abrasives.md) — high-speed bearings rated for radial loads at 6,000-8,000 rpm
- [Dairy Processing](dairy.md) — milk handling, hygiene, and cream utilization
- [Power source](../energy/index.md) — hand crank via step-up gear (100-500 W human power) or 0.5-2 kW motor

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Stainless steel (bowl and discs) | 5-15 kg | 304 or 316 grade, food-contact surface finish Ra <0.8 μm | [Iron & Steel](../metals/iron-steel.md) | Tinned copper (heavier, needs re-tinning) |
| Steel shaft (spindle) | 2-5 kg | 20-30 mm diameter, ground to ±0.01 mm, hardened | [Iron & Steel](../metals/iron-steel.md) | None — precision required |
| Cast iron or steel (housing) | 10-30 kg | Frame, bearing housings, drive housing | [Iron & Steel](../metals/iron-steel.md) | Welded steel plate |
| Bearings | 2-4 pcs | Precision ball bearings, rated for 8,000+ rpm with radial load | [Bearings](../machine-tools/bearings-abrasives.md) | Bronze sleeve bearings (shorter life at high rpm) |
| Drive gears | 1 set | Step-up ratio 4:1 to 8:1 (hand crank to bowl) or 1:1 belt drive (motor) | [Iron & Steel](../metals/iron-steel.md) | Belt drive (less positive) |
| Rubber or cork (vibration mounts) | 4 pcs | For frame isolation | [Polymers](../polymers/index.md) | Leather pads |
| Sanitary seals | 2-4 pcs | Food-grade rubber O-rings or U-cups for bowl sealing | [Polymers](../polymers/index.md) | Leather packing (lower pressure, needs frequent replacement) |

## Construction Steps

### Bowl Assembly

1. **Machine the bowl body**: Turn the bowl body from a solid stainless steel blank or deep-drawn shell. Bowl diameter: 100-200 mm. Bowl height: 80-150 mm. The inner surface must be concentric with the bore within 0.02 mm and polished to Ra <0.8 μm. Any roughness traps milk residue and creates sanitation problems. Machine a central bore (20-30 mm) for the spindle shaft, and external threads or a lock ring groove for the bowl cover.

2. **Machine the disc stack**: Cut 15-30 conical discs from 0.3-0.5 mm stainless steel sheet. Each disc is a shallow cone (half-angle 4-6° from flat, 80-170 mm diameter) with spacing ribs (3-6 small dimples or projections stamped on the upper surface) that maintain 0.5-1.0 mm gap between adjacent discs. Punch a central hole (20-30 mm) and 3-6 distribution holes (5-8 mm) near the outer edge. The distribution holes align vertically when discs are stacked, forming channels that route milk downward through the disc stack.

3. **Assemble the disc stack**: Stack discs on the central spindle in the bowl body, alternating orientation if using directional discs. The spacing ribs must face upward on each disc. Place a top disc (without distribution holes, acts as a deflector) at the top of the stack. The disc stack is held in place by a centering collar and a lock nut on the spindle.

4. **Machine the bowl cover**: Turn a stainless steel cover with a central cream discharge tube (pointing upward, inner diameter 5-10 mm) and a skim milk discharge tube (pointing outward at the bowl rim, diameter 10-15 mm). The cover seals to the bowl body with a food-grade O-ring. The cover must be concentric with the bowl within 0.05 mm — any eccentricity causes dynamic imbalance.

5. **Dynamic balance the bowl assembly**: Mount the complete bowl (body, discs, cover, spindle) in a balancing machine. Spin at 500 rpm and measure imbalance. Remove material (drill shallow pockets on the heavy side of the bowl body) until residual imbalance is below 0.5 g·mm per kg of bowl mass. This step is critical — an unbalanced 10 kg bowl at 7,000 rpm generates destructive vibration within seconds. Professional separators are balanced to 0.01 mm.

### Frame and Drive

6. **Construct the frame**: Build a rigid frame from cast iron or welded steel plate. The frame must support the bearing housing (which carries the bowl and spindle) and the drive mechanism. Include vibration-isolation mounts (rubber or cork pads) at the frame base. The frame must be heavy enough (15-30 kg) to absorb residual vibration without walking across the floor.

7. **Install the spindle and bearings**: Mount the spindle in a pair of precision ball bearings in the bearing housing. Upper bearing (closest to bowl): angular contact bearing to handle both radial and axial (thrust) loads. Lower bearing: deep groove ball bearing. The spindle extends through both bearings, with the bowl mounted on the upper end and the drive pulley or gear on the lower end.

8. **Install the drive mechanism**:
   - **Hand-crank version**: Mount a step-up gear train (4:1 to 8:1 ratio) between the hand crank and the spindle. A bevel gear or worm gear converts the horizontal crank rotation to vertical spindle rotation. The operator cranks at 60-80 rpm; the spindle turns at 5,000-6,000 rpm. Install a one-way clutch so the bowl coasts when the operator pauses, maintaining separation during brief interruptions.
   - **Motor version**: Mount a belt drive from a 0.5-2 kW electric motor (1,400-1,800 rpm) to the spindle via a step-up pulley (3:1 to 5:1 ratio). Belt drive absorbs vibration and provides some overload protection.

9. **Install the feed and discharge system**: Mount a feed pipe (stainless steel, 10-15 mm diameter) that delivers milk to the center of the bowl (inside the disc stack). Milk enters at the center, flows outward through the disc gaps, separates, and exits: cream through the central discharge tube (upper), skim milk through the peripheral discharge tube (lower/outward). Connect food-grade tubing to both discharge outlets for collection.

10. **Install the cream adjustment valve**: Mount an adjustable valve on the cream discharge outlet. By restricting the cream outlet, the operator controls cream fat content: restricting flow increases cream residence time in the bowl, producing thicker cream (up to 50% fat). Opening the valve produces thinner cream (20-30% fat). Mark the valve with 3-4 detent positions for common cream grades.

## Calibration and Verification

1. **Balance verification**: Run the empty bowl at full speed (6,000-8,000 rpm). Place a glass of water on the frame — vibration should not cause visible ripples. If ripples appear at any speed, re-balance the bowl assembly. Maximum acceptable vibration amplitude: 0.02 mm at the bearing housing.

2. **Separation efficiency test**: Process 10 liters of whole milk (4% fat). Collect the skim milk output and measure fat content using a Gerber butyrometer or Babcock test. Target: skim milk fat content <0.1%. If fat content exceeds 0.3%, increase bowl speed, check disc stack assembly, or reduce feed rate.

3. **Cream fat content adjustment**: Run milk at constant feed rate. Adjust the cream valve through its range while collecting cream samples. Measure fat content of each sample. Create a reference chart mapping valve position to cream fat percentage for the operator.

4. **Throughput verification**: Time how long it takes to process a known volume of milk at the standard feed rate. Verify that throughput matches design specification: 100-200 L/hour (hand-cranked) or 500-5,000+ L/hour (motorized).

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Bowl speed | 6,000-8,000 rpm |
| Bowl diameter | 100-200 mm |
| Number of discs | 15-30 |
| Throughput (hand-cranked) | 100-200 L/hour |
| Throughput (motorized) | 500-5,000+ L/hour |
| Cream fat content | Adjustable: 20-50% |
| Skim milk fat content | <0.1% |
| Centrifugal acceleration | ~5,000-10,000× gravity at bowl rim |
| Power (hand crank) | 100-500 W human power |
| Power (motor) | 0.5-2 kW |
| Separation time | Seconds (vs. 12-24 hours for gravity) |
| Bearing life | 1-3 years with regular lubrication |
| Bowl balance tolerance | ≤0.01 mm residual imbalance |

## Strengths

- Separates cream from skim in seconds vs. 12-24 hours for gravity settling — enables same-day processing of fresh milk
- Achieves <0.1% fat in skim milk vs. 0.5-1.0% from gravity separation — higher cream yield per liter
- Cream fat content adjustable (20-50%) by regulating the discharge valve
- Continuous processing — feed milk in, cream and skim flow out simultaneously

## Weaknesses

- Bowl at 6,000-8,000 rpm requires dynamic balancing to 0.01 mm — imbalance causes destructive vibration
- Stainless steel or tinned copper construction demands precision metalworking capability
- Bearings at high radial loads need regular lubrication and replacement (every 1-3 years)
- All milk-contact surfaces must be disassembled and cleaned daily — 15-30 minutes of sanitation per use

## Safety

- **Rotational energy**: A 10 kg bowl at 7,000 rpm stores significant kinetic energy. Never open the bowl housing while the bowl is spinning. Install a locking mechanism that prevents housing opening until the bowl has stopped. A spinning bowl released from its bearings becomes a dangerous projectile.
- **Imbalance vibration**: If the separator begins vibrating violently during operation, shut down immediately. Imbalance is caused by uneven loading (feeding milk too fast), foreign objects in the bowl, or bearing failure. Continued operation with vibration causes bearing destruction and potential bowl disintegration.
- **Sanitation**: All milk-contact surfaces must be cleaned after every use. Milk residue supports bacterial growth (Listeria, Salmonella). Disassemble bowl, discs, and feed tubes. Wash with hot soapy water (60°C), rinse, sanitize with 200 ppm chlorine solution or 25 ppm peracetic acid.
- **Pinch points**: The gear train and belt drive present pinch hazards. Guard all drive components. Keep hands clear during operation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Vibration at full speed | Bowl unbalanced, foreign object inside, or bearing worn | Stop immediately. Inspect bowl for foreign objects. Re-balance if needed. Check bearings for roughness or play. |
| Skim milk contains visible cream (fat >0.3%) | Bowl speed too low, feed rate too high, or disc stack misassembled | Increase bowl speed. Reduce feed rate. Disassemble and re-stack discs ensuring correct spacing rib orientation. |
| Cream too thin (<20% fat) | Cream valve too open or feed rate too low | Close cream valve slightly. Verify milk fat content (must be 3.5-4.5% input). |
| Milk leaking from bowl cover | Cover seal (O-ring) worn or cover not tightened | Replace O-ring. Tighten cover lock ring. Check sealing surface for scratches. |
| Bearings running hot (>70°C) | Insufficient lubrication, bearing worn, or misalignment | Grease bearings. Check bearing condition. Verify spindle alignment in housing. |
| Bowl speed drops under load | Drive belt slipping or hand-crank torque insufficient | Tighten belt. Reduce feed rate. For hand-crank units, ensure operator maintains steady cranking pace. |

## See Also

- [Dairy Processing](dairy.md) — butter, cheese, and yogurt production from separated cream
- [Metals](../metals/iron-steel.md) — stainless steel for food-contact surfaces
- [Machine Tools](../machine-tools/index.md) — precision turning for bowl and spindle
- [Bearings](../machine-tools/bearings-abrasives.md) — high-speed bearing selection
- [Health & Sanitation](../health/sanitation.md) — dairy hygiene protocols

[← Back to Food Processing](index.md)
