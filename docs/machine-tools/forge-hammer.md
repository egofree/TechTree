# Forge Hammer (Power Hammer)

> **Node ID**: machine-tools.forge-hammer
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.casting`](casting.md), [`machine-tools.machining`](machining.md)
> **Enables**: [`machine-tools.forming`](forming.md), [`metals.iron-steel`](../metals/iron-steel.md)
> **Timeline**: Years 10-20
> **Outputs**: forged_parts, billets, die_forgings
> **Critical**: No — hand sledges and strikers can substitute at lower throughput, but power hammers multiply productive output by 5-10× and enable closed-die forging

## Principle

A power hammer lifts a heavy ram (tup) and releases it to strike the workpiece on an anvil, delivering repeated blows at 80-300 strikes per minute. The mechanized blow replaces the two-person striker team (smith + sledge man), multiplying both the force and consistency of hand forging. The ram is raised by one of several mechanisms — a cam and spring (helve hammer), a crank and leaf spring (spring helve), or compressed air/steam (air hammer) — and falls by gravity. The impact energy (E = m × g × h) determines the working capacity: a 25 kg ram falling 300 mm delivers 73 J per blow.

## Materials

### Spring Helve Hammer (Intermediate Build)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hardwood timber (frame) | 0.2 m³ | Oak or ash, 150 × 150 mm posts, 2.5 m tall | [Foundations](../foundations/tools-basic.md) | Welded steel frame (requires more fabrication) |
| Cast iron (anvil block) | 100-200 kg | Gray cast iron, 200 × 200 × 300 mm minimum | [Casting](casting.md) | Steel block (less vibration damping) |
| Steel (ram/tup) | 25-40 kg | Medium-carbon steel (0.4-0.5% C), hardened face | [Iron & Steel](../metals/iron-steel.md) | Cast iron ram (acceptable for light work) |
| Leaf spring | 1 | Vehicle leaf spring, 1.0-1.5 m long, 50 mm wide | [Iron & Steel](../metals/iron-steel.md) | Laminated spring (forge-welded leaves) |
| Crankshaft | 1 | Forged steel, 50-100 mm throw | [Machining](machining.md) | Eccentric sheave on shaft |
| Flywheel | 1 | Cast iron, 300-400 mm diameter, 20-30 kg | [Casting](casting.md) | Weighted disk on crankshaft |
| Bearings | 4-6 | Bronze bushings, matched to shaft diameter | [Casting](casting.md) | Greased bores in hardwood blocks |
| Belt or chain drive | 1 | Leather belt or roller chain, for power input | [Animals](../animals/animal-materials.md) | Direct drive from water wheel shaft |

### Helve Hammer (Simplest Build)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hardwood beam (helve) | 1 | 3-4 m long, 150 × 150 mm oak | [Foundations](../foundations/tools-basic.md) | Steel I-beam (more rigid) |
| Stone or iron (anvil) | 100-200 kg | Flat-top boulder or cast block | [Foundations](../foundations/tools-basic.md) | Welded steel anvil block |
| Cam | 1 | Wood or cast iron, mounted on water-wheel shaft | [Casting](casting.md) | Crank and connecting rod |
| Hammer head | 1 | 15-50 kg cast iron or steel, bolted to helve end | [Iron & Steel](../metals/iron-steel.md) | — |

## Prerequisites

- [Casting capability](casting.md) — for anvil block, flywheel, and frame components
- [Machining capability](machining.md) — for crankshaft, bearings, and ram alignment surfaces
- [Iron and steel](../metals/iron-steel.md) — for ram, crankshaft, and spring
- [Power source](../energy/index.md) — water wheel (3-5 HP), line shaft, or electric motor for powered operation
- [Belt drive or line shaft](iterative-bootstrap.md) — for power transmission from source to crankshaft

## Construction Steps

### Spring Helve Hammer

1. **Build the frame**: Erect four hardwood posts (150 × 150 mm oak or ash) in a rectangular plan, 1.0 m wide × 1.5 m deep. Brace with cross-timbers at the base and mid-height. The frame must be rigid — frame flex absorbs blow energy that should go into the workpiece. Bolt the posts to a heavy timber sill and anchor the sill to the floor with stakes or bolts.
2. **Install the anvil block**: Place a 100-200 kg cast iron or steel anvil block on a solid foundation (compacted earth or concrete pad) in the center of the frame. The anvil must not move under repeated blows — embed it in the ground if possible. The top face should be 700-800 mm above floor level (comfortable working height).
3. **Mount the leaf spring**: Bolt one end of a vehicle leaf spring (1.0-1.5 m long) to the top of the frame at the rear. The spring extends forward over the anvil. Bolt or clamp the ram to the free end of the spring, directly above the anvil face.
4. **Fabricate the ram**: Forge or cast a 25-40 kg steel or cast iron ram. The bottom face (striking surface) should be flat, 80-100 mm wide × 120-150 mm long. Harden the face if steel: heat to 820-850°C, oil quench, temper at 350-400°C to 45-50 HRC. Attach the ram to the spring end with a through-bolt and reinforcing plates.
5. **Build the crank assembly**: Turn a crankshaft from forged steel with a 50-100 mm throw (this determines the ram stroke). Mount the crankshaft in bronze bushings on the frame, positioned so the crank engages the spring (or a connecting rod to the spring) at its midpoint. Mount a cast iron flywheel (300-400 mm diameter, 20-30 kg) on the crankshaft to smooth the impulse loading.
6. **Connect the drive**: Attach a belt pulley or chain sprocket to the crankshaft. Connect to the power source (water wheel, line shaft, or motor) via belt or chain. For a hand-cranked version, mount a 400-500 mm crank handle on the flywheel extension.
7. **Adjust the stroke and blow force**: The crank lifts the spring and ram, then releases them to fall. Adjust the crank-to-spring engagement point to control the stroke height. For lighter blows, reduce the crank throw or add an adjustable stop that limits spring deflection. The blow energy is proportional to the ram mass times the fall height: E = m × g × h.

### Helve Hammer (Simpler Build, Water-Powered)

8. **Prepare the helve beam**: Select a straight hardwood beam (oak or ash), 3-4 m long, 150 × 150 mm section. Bolt the hammer head (15-50 kg) to one end. The beam pivots at a fulcrum point located 1/3 to 1/2 of the way from the hammer end.
9. **Install the pivot**: Mount the fulcrum on a heavy timber frame — a steel pin through the beam, supported by notched hardwood posts. The pivot must resist the repeated impact loads without loosening.
10. **Mount the cam**: On the water-wheel shaft, mount a cam (wood or cast iron) that lifts the tail end of the helve beam once per revolution. As the cam passes, the beam falls by gravity, and the hammer head strikes the anvil. The stroke is 30-60 cm.
11. **Adjust blow rate**: The blow rate equals the water-wheel RPM. Typical water-wheel speed: 5-20 RPM, producing 5-20 blows per minute. This is slower than a spring helve hammer but delivers much heavier blows (the long helve arm multiplies the fall distance).

## Calibration and Verification

1. **Blow force measurement**: Place a soft copper bar (20 mm thick) on the anvil. Strike one blow at full stroke. Measure the indentation depth and diameter. Calculate approximate force from the hardness and indentation geometry. A 25 kg ram at 300 mm stroke should indent 20 mm copper by approximately 3-5 mm.
2. **Alignment check**: Place a dye-coated flat steel plate on the anvil. Strike one blow. The impression should be uniform across the full face — if one side is deeper, the ram is not parallel to the anvil. Adjust the spring mounting or ram attachment.
3. **Run test**: Operate the hammer at full speed for 30 minutes. Check for excessive vibration, frame loosening, bearing heating, or spring fatigue. The crankshaft bearings should not exceed 60°C. Tighten all bolts after the run-in period.
4. **Frequency check**: Count the blows per minute. Spring helve: target 150-300 BPM. Helve hammer: 5-20 BPM (water-wheel dependent). If the rate is too fast, the workpiece does not have time to reposition between blows.

## Expected Performance

| Parameter | Spring Helve | Helve (Water) | Air/Steam |
|-----------|-------------|---------------|-----------|
| Ram weight | 25-40 kg | 15-50 kg | 50-5000 kg |
| Blow energy | 70-120 J | 100-300 J | 500-50,000 J |
| Blows per minute | 150-300 | 5-20 | 60-200 |
| Stroke length | 50-150 mm | 300-600 mm | 300-1200 mm |
| Capacity (mild steel) | Up to 30 mm square | Up to 50 mm square | Up to 300 mm square |
| Power required | 1-3 HP | 3-5 HP (water wheel) | 10-50 HP (compressed air or steam) |
| Duty cycle | Continuous | Continuous | Continuous |

## Strengths

- Multiplies forging output 5-10× over hand-sledge work — a single operator produces what a smith + striker team does
- Consistent blow force and frequency — better part uniformity than hand striking
- Spring helve hammer constructable with basic machine tools and salvaged leaf spring

## Weaknesses

- Noise and vibration — power hammers transmit significant vibration to the floor and surrounding structure. Isolate the anvil block from the frame with a timber or rubber pad
- Limited control over blow force on simple designs — the operator controls workpiece position but not individual blow energy (fixed by crank throw and ram weight)
- Requires a power source — hand-cranking is exhausting for more than a few minutes; sustained operation needs water wheel, engine, or motor

## Safety

- **Noise**: Power hammers produce impact noise exceeding 100 dB. Hearing protection mandatory — earplugs rated NRR 25+.
- **Pinch points**: The ram-to-anvil gap closes with tons of force. Never place hands on the anvil during operation. Use tongs to position workpieces. Install a treadle-operated clutch so the operator controls when blows occur.
- **Flying scale**: Hot forging produces scale fragments that fly off under hammer blows. Safety glasses (ANSI Z87.1) and face shield mandatory.
- **Frame failure**: A cracked spring or loose bolt can launch the ram sideways. Inspect the spring, pivots, and bolts daily. Replace cracked springs immediately.

## Variations and Alternatives

- **Helve hammer**: Beam pivoted at one end, hammer head at the other. Simplest mechanism. Raised by cam on water-wheel shaft, falls by gravity. Stroke 30-60 cm, 50-150 kg blow equivalent. The first mechanized forging tool.
- **Tilt hammer**: Similar to helve but the tail is lifted by cams. 80-200 blows/minute in early water-powered forges. More compact than helve.
- **Spring helve hammer** (this article's primary build): Heavy timber frame, 15-40 kg head on leaf spring. Crank-driven, 150-300 blows/minute. The best intermediate build — constructable with basic machine tools.
- **Steam or air hammer** (later): 500-5000 kg capacity. Requires [Steam Power](../energy/steam-power.md) or compressed air. The production forging tool of industrial civilization.

## See Also

- [Forming](forming.md) — forging operations and procedures using the hammer
- [Casting](casting.md) — casting the anvil block and flywheel
- [Machining](machining.md) — machining the crankshaft and bearings
- [Iron & Steel](../metals/iron-steel.md) — heat treatment of the ram face
- [Iterative Bootstrap](iterative-bootstrap.md) — machine tool construction sequence

[← Back to Machine Tools](index.md)
