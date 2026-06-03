# Injection Molding Machine

> **Node ID**: machine-tools.injection-molding-machine
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.hydraulics`](../energy/hydraulics.md), [`machine-tools.extruder`](extruder.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`polymers.rubber`](../polymers/rubber.md), [`chemistry.packaging-testing`](../chemistry/packaging-testing.md)
> **Timeline**: Years 15-25
> **Outputs**: molded_parts, precision_plastic_components
> **Critical**: Yes — the highest-volume plastic processing method; over 50% of all thermoplastic products are injection-molded

## Principle

An injection molding machine melts thermoplastic granules in a heated barrel using a rotating screw (reciprocating screw design), then rams the screw forward to inject the molten polymer under high pressure (50-200 MPa) into a closed steel mold. The mold is cooled until the polymer solidifies, then opened to eject the finished part. The cycle repeats: plastication (screw rotates to melt and convey polymer while retracting) → injection (screw rams forward as a plunger) → packing/holding (pressure maintained as polymer cools and shrinks) → cooling → mold open → ejection → mold close.

The machine has two primary units: the injection unit (barrel, screw, heater bands, hydraulic cylinder) and the clamping unit (stationary and moving platens, hydraulic cylinder or toggle mechanism). The clamping force must exceed the injection pressure × projected part area to prevent the mold from opening (flashing). A part with 200 cm² projected area at 100 MPa injection pressure requires 200 tons clamp force minimum — typically sized to 1.2-1.5× this value.

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for platens, frame, and tie bars
- [Machining capability](machining.md) — for barrel boring, screw turning, platen surfacing
- [Hydraulic system](../energy/hydraulics.md) — pump, cylinders, valves, for injection and clamp
- [Electric motor](../energy/electric-motors.md) — 10-75 kW for hydraulic pump drive
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, one per heating zone (3-5 zones)
- [Extruder construction knowledge](extruder.md) — the injection unit barrel and screw are functionally identical to an extruder

## Materials

### Clamping Unit

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (platens) | 200-800 kg | A36 or higher, 50-100 mm thick, machined flat | [Iron & Steel](../metals/iron-steel.md) | Cast iron platens (better vibration damping, heavier) |
| Steel bar (tie bars) | 4 pieces | 1045 or 4140, 50-100 mm diameter, ground and polished | [Iron & Steel](../metals/iron-steel.md) | None — tie bars are the only practical tension member |
| Hydraulic cylinder (clamp) | 1 | Bore 100-250 mm, stroke 200-500 mm, rated to 20 MPa | [Hydraulics](../energy/hydraulics.md) | Toggle mechanism (mechanical advantage, less controllable) |
| Toggle pins (if toggle clamp) | 5-7 | Hardened steel, 30-60 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Full-hydraulic design (simpler but larger cylinder needed) |

### Injection Unit

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Barrel | 1 | Seamless tubing or bored solid bar, nitriding steel (4140), ID 25-80 mm | [Forming](../metals/forming.md) | Same as extruder barrel construction |
| Screw | 1 | Alloy steel (4140 or 4340), hard-faced flights, 25-80 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Plunger (non-reciprocating screw — simpler, no screw rotation) |
| Band heaters | 3-5 | Ceramic-insulated, 2-8 kW each, 220-480 V | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in aluminum heaters |
| Thermocouples | 3-5 | Type K, 0-400°C | [Measurement](../measurement/precision.md) | RTD sensors |
| Hydraulic cylinder (injection) | 1 | Bore 80-200 mm, stroke 100-300 mm, rated to 20 MPa | [Hydraulics](../energy/hydraulics.md) | Mechanical plunger (lever-actuated, limited pressure) |
| Nozzle | 1 | Hardened tool steel, tapered bore, with shutoff valve | [Iron & Steel](../metals/iron-steel.md) | Open nozzle (simpler, material drools between shots) |

### Hydraulic System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hydraulic pump | 1 | Variable displacement piston pump, 20-100 L/min at 20 MPa | [Hydraulics](../energy/hydraulics.md) | Fixed displacement gear pump (wastes energy at low flow) |
| Hydraulic oil | 50-200 L | ISO VG 32 or 46, filtered to 25 μm | [Lubricants](../petroleum/lubricants.md) | Filtered vegetable oil (degrades faster) |
| Pressure relief valve | 1 | Pilot-operated, set to 110% of max system pressure | [Hydraulics](../energy/hydraulics.md) | None — safety-critical component |
| Directional control valves | 2-4 | 4-way, 3-position, solenoid-operated, rated to 21 MPa | [Hydraulics](../energy/hydraulics.md) | Manual valves (slower cycle, operator fatigue) |
| Hydraulic hoses and fittings | 5-10 m | Rated to 1.5× max system pressure | [Hydraulics](../energy/hydraulics.md) | Steel tubing (permanent, no flex) |

## Construction Steps

### Clamping Unit

1. **Machine platens**: Cut three steel plates (two stationary, one moving) to size. For a 100-ton machine: 500 × 500 × 75 mm thick. Mill all faces flat and parallel within 0.05 mm. Drill four tie-bar holes through all three platens, aligned within 0.1 mm positional tolerance. The moving platen slides on the tie bars.

2. **Prepare tie bars**: Turn four bars from 1045 or 4140 steel, 60-80 mm diameter. Thread both ends (M60-80, 4-pitch ACME or unified thread). Surface finish: polished to 0.4 μm Ra on the sliding portion. Hardness: 28-32 HRC (ductile enough to avoid brittle fracture under cyclic tension). Tie bars are the highest-stress components — any surface defect (tool mark, scratch) becomes a fatigue initiation site.

3. **Assemble clamping frame**: Place fixed platen at one end. Thread tie bars through fixed platen. Install moving platen on tie bars with bronze bushings (sliding fit: 0.05-0.10 mm clearance). Install tail stock platen at opposite end. Thread nuts onto tie bar ends. Torque nuts alternately and evenly to preload the frame (preload = 1.2× maximum clamp force to prevent joint separation during injection).

4. **Install clamp cylinder**: Mount hydraulic cylinder on the tail stock platen, aligned with platen centerline within 0.1 mm. Connect cylinder rod to moving platen via a clevis or flange joint. For a full-hydraulic clamp, the cylinder bore area × max pressure must equal the rated clamp force: a 100-ton machine at 20 MPa requires a 250 mm bore cylinder (π/4 × 250² × 20 = 98 tonnes).

5. **Install ejector system**: Mount a small hydraulic cylinder (25-40 mm bore) in the center of the moving platen for part ejection. The ejector rod pushes an ejector plate that drives mold ejector pins. Stroke: 50-100 mm.

### Injection Unit

6. **Build barrel and screw**: Construct the barrel and screw following the same procedure as [extruder construction](extruder.md) steps 4-11. Key difference: the injection screw must be shorter (L/D 18-22:1) and have a check valve (non-return ring) at the tip. The check valve allows polymer to flow past the screw tip during plastication (screw rotating) but seals during injection (screw ramming forward). Machine a sliding ring valve: a free-floating ring that moves 2-3 mm axially to open/close flow passages.

7. **Install screw drive**: Mount a hydraulic motor (or electric motor with gear reducer) to drive the screw for plastication. The motor must overcome melt viscosity in the barrel — torque requirement: 50-200 N·m per mm of screw diameter at 100 RPM. Mount the motor on a linear bearing carriage so the entire injection unit (barrel + screw + motor) can slide forward and back.

8. **Install injection cylinder**: Mount a hydraulic cylinder behind the screw drive carriage. During injection, this cylinder pushes the entire injection unit forward (nozzle against mold sprue bushing), then pushes the screw forward to inject melt. Injection pressure = cylinder force / screw cross-sectional area. For 150 MPa injection pressure with a 40 mm screw: required force = π/4 × 40² × 150 = 188 kN. At 20 MPa hydraulic pressure, cylinder bore = √(188,000 / (20 × π/4)) ≈ 110 mm.

9. **Mount nozzle**: Install a hardened steel nozzle at the barrel tip. The nozzle has a tapered orifice (3-6 mm exit diameter) that seats against the mold sprue bushing. Include a spring-loaded shutoff valve in the nozzle body to prevent melt drool between shots.

10. **Mount injection unit to frame**: Bolt the injection unit base to the machine frame on linear guideways. The injection unit must slide forward smoothly under hydraulic pressure to seat the nozzle against the mold — alignment tolerance: nozzle tip to mold sprue bushing within 0.1 mm concentricity.

### Hydraulic System

11. **Install hydraulic power unit**: Mount reservoir (100-300 L), pump, and electric motor on the machine base. Connect pump outlet to a manifold block distributing flow to clamp cylinder, injection cylinder, screw motor, and ejector cylinder. Install pressure relief valve set to 22 MPa (110% of 20 MPa rated pressure).

12. **Install control valves**: Mount directional control valves on the manifold for each hydraulic function: clamp open/close, injection forward/back, screw rotate, ejector forward/back. For manual operation: use lever-operated valves. For automatic cycling: use solenoid valves controlled by a relay logic panel or PLC.

13. **Connect and bleed**: Connect all hoses and tubing. Fill reservoir with filtered hydraulic oil. Bleed air from each circuit by cycling each cylinder slowly 10-20 times with bleeder valves open.

### Controls

14. **Wire temperature zones**: Connect each barrel band heater to its PID controller with thermocouple feedback. Set temperature limits with high-limit shutoff (barrel overtemperature causes polymer degradation and gas generation — potentially explosive in a sealed barrel).

15. **Install limit switches**: Mount limit switches on the moving platen (mold closed, mold open positions), injection unit (nozzle seated, retracted), and ejector (forward, back). These switches provide position feedback for automatic cycling.

16. **Wire safety interlocks**: The machine must NOT inject unless: (a) mold is fully closed and clamp force is at setpoint, (b) nozzle is seated against sprue bushing, (c) operator's two-hand controls are engaged (if manual mode). Wire these interlocks in series with the injection valve solenoid.

## Calibration and Verification

1. **Platen parallelism**: With tie bars torqued to specification, measure the gap between fixed and moving platens at four corners with a precision straightedge and feeler gauges. Maximum deviation: 0.05 mm per 500 mm of platen width. Adjust by shimming tie bar nuts.

2. **Clamp force calibration**: Install a calibrated load cell between the platens. Apply full hydraulic pressure to the clamp cylinder. Compare measured force to theoretical (pressure × cylinder bore area). Verify force is within ±5% of rated value. Check force uniformity at four positions on the platen.

3. **Injection pressure test**: Install a pressure transducer in the nozzle. Perform a test injection (air shot — no mold, inject into open air). Verify peak injection pressure reaches setpoint within ±5%.

4. **Temperature calibration**: Set all barrel zones to 200°C. After 30 minutes stabilization, measure barrel surface temperature with a calibrated pyrometer at each zone. Zone temperature must match setpoint within ±3°C.

5. **Cycle test**: Run 50 automatic cycles with a test mold (simple flat plaque, 100 × 100 × 3 mm). Weigh each part. Part weight variation must be <±0.5% across 50 shots. Cycle time consistency: <±2% variation.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Clamp force range | 50-500+ tons (industrial to 5000+ tons) |
| Injection pressure | 50-200 MPa |
| Shot size (volume) | 10-5000 cm³ (machine-dependent) |
| Screw diameter | 25-80 mm (typical: 40-60 mm) |
| Screw L/D ratio | 18-22:1 |
| Cycle time | 15-120 seconds (part-dependent) |
| Production rate | 30-240 parts/hour per cavity |
| Number of heating zones | 3-5 (barrel) + 1 (nozzle) |
| Temperature range | 160-320°C (polymer-dependent) |
| Mold temperature control | 20-100°C (water-circulated) |
| Hydraulic system pressure | 14-20 MPa (typical) |
| Motor power | 10-75 kW |
| Dimensional tolerance (molded parts) | ±0.05-0.25 mm |
| Service life (before major rebuild) | 50,000-200,000 operating hours |

## Strengths

- Highest-volume, lowest per-part cost for complex 3D shapes — once the mold is made, each part costs pennies in material and machine time
- Excellent dimensional consistency — ±0.05-0.25 mm tolerances achievable in production
- Wide material range — virtually every thermoplastic can be injection-molded, plus many elastomers
- Fully automatable — once parameters are set, the machine cycles without operator intervention

## Weaknesses

- High machine cost — a 100-ton injection molder costs $20,000-100,000+ new; requires precision machining and hydraulic expertise to build
- High tooling cost — production molds cost $10,000-100,000+ (P20 tool steel, precision machined); requires 10,000+ parts to amortize
- Limited to parts with uniform wall thickness — thick sections require disproportionately long cooling time (scales with wall thickness²)
- Complex hydraulic system — pumps, valves, cylinders, and seals all require maintenance; oil leaks are inevitable

## Variations and Alternatives

- **Reciprocating screw vs. plunger**: The reciprocating screw (described above) is the standard design — it both plasticates and injects. A simpler plunger machine uses a separate ram to push pre-melted polymer from a heated pot into the mold. Plunger machines are easier to build but provide poor melt homogeneity and low shot-to-shot consistency.
- **Hydraulic vs. toggle clamp**: Hydraulic clamp provides direct, controllable force and is simpler to build. Toggle clamp (mechanical linkage) multiplies a small cylinder force into large clamp force but is harder to design and requires precise linkage geometry.
- **Hand-operated injection molder**: For bootstrapping, a lever-actuated plunger in a heated barrel can produce simple parts at low pressure (10-30 MPa). Clamp by bolting the mold halves together. Functional for prototyping and low-volume parts in LDPE, PS, and PP.
- **All-electric machine**: Replaces hydraulics with servo motors and ball screws for each axis. Cleaner, more precise, more energy-efficient, but requires servo motor and ball screw manufacturing capability beyond bootstrap level.

## Safety

- **Crush hazard (clamp)**: The clamp generates 50-500+ tons of force. A hand caught between closing mold halves is catastrophically crushed. Install two-hand anti-tie-down controls (operator must press both buttons simultaneously to close the mold; releasing either button stops motion). Never reach into the mold area during automatic cycling. Install safety gates with interlock switches.
- **High-pressure injection**: Polymer at 50-200 MPa can penetrate skin through the nozzle or mold parting line. Injection injuries require immediate surgical debridement. Never look directly at the nozzle during an air shot. Install a splash guard between the injection unit and operator station.
- **Molten polymer burns**: Nozzle and barrel surfaces reach 200-320°C. Use heat-resistant gloves when changing nozzles or purging the barrel. Molten polymer sticks to skin — cool under running water for 15+ minutes, do not peel.
- **Hydraulic hazards**: System pressure at 20 MPa stores significant energy. Hydraulic injection injuries (oil penetrating skin through a pinhole leak) require immediate surgery. Never use hands to search for hydraulic leaks — use cardboard. Install pressure relief valve and verify function monthly.
- **Mold handling**: Production molds weigh 50-500+ kg. Use hoists or cranes for mold installation. Never lift a mold manually above waist height.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Short shots (incomplete fill) | Insufficient injection pressure or melt too viscous | Increase injection pressure 10-20%; raise barrel temperature 5-10°C; increase injection speed; verify screw check valve is sealing |
| Flash (excess at parting line) | Insufficient clamp force or mold worn | Increase clamp force; reduce injection pressure; inspect mold parting line for wear; check platen parallelism |
| Sink marks | Insufficient holding pressure or time; wall thickness variation | Increase holding pressure and time; redesign part for ±10% wall thickness uniformity |
| Part weight variation >±1% | Screw check valve leaking or inconsistent feeding | Inspect and replace check valve ring; verify hopper feed is uninterrupted; check screw retraction position consistency |
| Nozzle drool | Barrel temperature too high at nozzle zone; no shutoff valve | Lower nozzle zone temperature 5-10°C; install spring-loaded nozzle shutoff valve |
| Machine won't build clamp force | Hydraulic pump worn or relief valve set too low | Check pump flow rate at pressure; verify relief valve setting; inspect cylinder seals for bypass |

## See Also

- [Extruder](extruder.md) — shared barrel/screw technology
- [Blow Molding Equipment](blow-molding-equipment.md) — injection blow molding uses an injection molder for preforms
- [Compression Press](compression-press.md) — simpler alternative for thermosets and rubber
- [Thermoforming Equipment](thermoforming-equipment.md) — lower-cost alternative for large sheet-formed parts
- [Hydraulics](../energy/hydraulics.md) — hydraulic system design, fluid selection, pump types
- [Machining](machining.md) — barrel boring, screw turning, platen surfacing
- [Injection Molding Process](../polymers/thermoplastics.md) — polymer-specific injection parameters

[← Back to Machine Tools](index.md)
