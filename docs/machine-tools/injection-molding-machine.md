# Injection Molding Machine

> **Node ID**: machine-tools.injection-molding-machine
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.index`](../energy/index.md), [`machine-tools.extruder`](extruder.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`polymers.rubber`](../polymers/rubber.md), [`chemistry.packaging-testing`](../chemistry/packaging-testing.md)
> **Timeline**: Years 15-25
> **Outputs**: molded_parts, precision_plastic_components
> **Critical**: Yes — the highest-volume plastic processing method; over 50% of all thermoplastic products are injection-molded

## Overview

An injection molding machine melts thermoplastic granules in a heated barrel using a rotating screw (reciprocating screw design), then rams the screw forward to inject the molten polymer under high pressure (50-200 MPa) into a closed steel mold. The mold is cooled until the polymer solidifies, then opened to eject the finished part. The cycle repeats: plastication (screw rotates to melt and convey polymer while retracting) → injection (screw rams forward as a plunger) → packing/holding (pressure maintained as polymer cools and shrinks) → cooling → mold open → ejection → mold close.

The machine has two primary units: the injection unit (barrel, screw, heater bands, hydraulic cylinder) and the clamping unit (stationary and moving platens, hydraulic cylinder or toggle mechanism). The clamping force must exceed the injection pressure × projected part area to prevent the mold from opening (flashing). A part with 200 cm² projected area at 100 MPa injection pressure requires 200 tons clamp force minimum — typically sized to 1.2-1.5× this value.

Injection molding produces complex three-dimensional parts with ±0.05-0.25 mm tolerance at cycle times of 15-120 seconds. It is the highest-volume plastic processing method, consuming over 50% of all thermoplastic resin produced. Once the mold is made, each part costs pennies in material and machine time. The [extruder](extruder.md) shares the barrel-and-screw technology; the injection molder adds the clamping unit, mold, and injection hydraulic circuit.

The injection molding cycle has five phases. **Plastication**: the screw rotates to melt and convey polymer granules from the hopper through the heated barrel, building a reservoir of melt in front of the screw tip. The screw retracts as melt accumulates. **Injection**: the hydraulic cylinder rams the screw forward as a plunger, forcing melt through the nozzle into the closed mold at 50-200 MPa. **Packing/holding**: pressure is maintained as the polymer cools and shrinks — this phase compensates for volumetric shrinkage (1.5-3% for most thermoplastics). **Cooling**: the mold temperature control system extracts heat until the part is rigid enough to eject. **Ejection**: the mold opens, and mechanical ejector pins push the part off the mold core.

Mold design is a specialized discipline in itself. The mold must distribute melt evenly through a runner system to one or more cavities, maintain uniform temperature via cooling channels, allow air to escape through vents (0.02-0.05 mm deep), and release the finished part without damage. Mold construction from hardened tool steel (P20 or H13) is covered in the [machining](machining.md) article. A single-cavity mold for a simple part may weigh 50-100 kg and cost weeks of machining time. Multi-cavity molds (4-64 cavities) multiply output but require correspondingly larger clamp force and precision alignment.

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for platens, frame, and tie bars
- [Machining capability](machining.md) — for barrel boring, screw turning, platen surfacing
- [Hydraulic system](../energy/index.md) — pump, cylinders, valves, for injection and clamp
- [Electric motor](../energy/electric-motor.md) — 10-75 kW for hydraulic pump drive
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, one per heating zone (3-5 zones)
- [Extruder construction knowledge](extruder.md) — the injection unit barrel and screw are functionally identical to an extruder

## Bill of Materials

### Clamping Unit

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (platens) | 200-800 kg | A36 or higher, 50-100 mm thick, machined flat | [Iron & Steel](../metals/iron-steel.md) | Cast iron platens (better vibration damping, heavier) |
| Steel bar (tie bars) | 4 pieces | 1045 or 4140, 50-100 mm diameter, ground and polished | [Iron & Steel](../metals/iron-steel.md) | None — tie bars are the only practical tension member |
| Hydraulic cylinder (clamp) | 1 | Bore 100-250 mm, stroke 200-500 mm, rated to 20 MPa | [Energy Systems](../energy/index.md) | Toggle mechanism (mechanical advantage, less controllable) |

### Injection Unit

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Barrel | 1 | Seamless tubing or bored solid bar, nitriding steel (4140), ID 25-80 mm | [Forming](../metals/forming.md) | Same as extruder barrel construction |
| Screw | 1 | Alloy steel (4140 or 4340), hard-faced flights, 25-80 mm diameter | [Iron & Steel](../metals/iron-steel.md) | Plunger (non-reciprocating screw — simpler, no screw rotation) |
| Band heaters | 3-5 | Ceramic-insulated, 2-8 kW each, 220-480 V | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in aluminum heaters |
| Thermocouples | 3-5 | Type K, 0-400°C | [Measurement](../measurement/precision-metrology.md) | RTD sensors |
| Hydraulic cylinder (injection) | 1 | Bore 80-200 mm, stroke 100-300 mm, rated to 20 MPa | [Energy Systems](../energy/index.md) | Mechanical plunger (lever-actuated, limited pressure) |

### Hydraulic System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hydraulic pump | 1 | Variable displacement piston pump, 20-100 L/min at 20 MPa | [Energy Systems](../energy/index.md) | Fixed displacement gear pump |
| Hydraulic oil | 50-200 L | ISO VG 32 or 46, filtered to 25 μm | [Lubricants](../chemistry/lubricants.md) | Filtered vegetable oil |
| Pressure relief valve | 1 | Pilot-operated, set to 110% of max system pressure | [Energy Systems](../energy/index.md) | None — safety-critical |
| Directional control valves | 2-4 | 4-way, 3-position, solenoid-operated, rated to 21 MPa | [Energy Systems](../energy/index.md) | Manual valves (slower cycle) |

## Process Description

### Clamping Unit Assembly

1. **Machine platens**: Cut three steel plates (two stationary, one moving) to size. For a 100-ton machine: 500 × 500 × 75 mm thick. Mill all faces flat and parallel within 0.05 mm. Drill four tie-bar holes through all three platens, aligned within 0.1 mm positional tolerance.
2. **Prepare tie bars**: Turn four bars from 1045 or 4140 steel, 60-80 mm diameter. Thread both ends (M60-80, 4-pitch ACME or unified thread). Surface finish: polished to 0.4 μm Ra on the sliding portion. Hardness: 28-32 HRC. Tie bars are the highest-stress components — any surface defect becomes a fatigue initiation site.
3. **Assemble clamping frame**: Place fixed platen at one end. Thread tie bars through fixed platen. Install moving platen on tie bars with bronze bushings (sliding fit: 0.05-0.10 mm clearance). Install tail stock platen. Torque nuts alternately and evenly to preload the frame at 1.2× maximum clamp force.
4. **Install clamp cylinder**: Mount hydraulic cylinder on the tail stock platen, aligned with platen centerline within 0.1 mm. Connect cylinder rod to moving platen via a clevis or flange joint. For a 100-ton machine at 20 MPa: 250 mm bore cylinder required.

**Calibration**: Measure platen parallelism with a precision straightedge and feeler gauges at four corners. Maximum deviation: 0.05 mm per 500 mm. Install a load cell between platens and apply full hydraulic pressure — measured force must match theoretical within ±5%.

**Expected performance**: Clamp force: 50-500+ tons. Platen parallelism: ±0.05 mm. Tie bar preload: 1.2× rated clamp force.

### Injection Unit Assembly

5. **Build barrel and screw**: Construct following the same procedure as [extruder construction](extruder.md) steps 4-11. Key difference: the injection screw must be shorter (L/D 18-22:1) and have a check valve (non-return ring) at the tip. Machine a sliding ring valve: a free-floating ring that moves 2-3 mm axially to open/close flow passages.
6. **Install screw drive**: Mount a hydraulic motor to drive the screw for plastication. Torque requirement: 50-200 N·m per mm of screw diameter at 100 RPM. Mount on a linear bearing carriage so the entire injection unit slides forward and back.
7. **Install injection cylinder**: Mount a hydraulic cylinder behind the screw drive carriage. During injection, this cylinder pushes the entire injection unit forward (nozzle against mold sprue bushing), then pushes the screw forward to inject melt. For 150 MPa injection pressure with a 40 mm screw: required force = π/4 × 40² × 150 = 188 kN. At 20 MPa hydraulic pressure, cylinder bore ≈ 110 mm.
8. **Mount nozzle**: Install a hardened steel nozzle at the barrel tip with a tapered orifice (3-6 mm exit diameter). Include a spring-loaded shutoff valve to prevent melt drool between shots.

**Calibration**: Install a pressure transducer in the nozzle. Perform an air shot (no mold, inject into open air). Verify peak injection pressure reaches setpoint within ±5%. Set all barrel zones to 200°C, wait 30 minutes, measure barrel surface temperature with a pyrometer — zone temperature must match setpoint within ±3°C.

**Expected performance**: Injection pressure: 50-200 MPa. Screw diameter: 25-80 mm. Shot size: 10-5000 cm³. Barrel temperature: 160-320°C.

### Hydraulic System and Controls

9. **Install hydraulic power unit**: Mount reservoir (100-300 L), pump, and electric motor on the machine base. Connect pump outlet to a manifold block distributing flow to clamp cylinder, injection cylinder, screw motor, and ejector cylinder. Install pressure relief valve set to 22 MPa.
10. **Install control valves**: Mount directional control valves for each hydraulic function. For manual operation: lever-operated valves. For automatic cycling: solenoid valves controlled by relay logic or PLC.
11. **Wire temperature zones**: Connect each barrel band heater to its PID controller with thermocouple feedback. Set high-limit shutoff (barrel overtemperature causes polymer degradation — potentially explosive in a sealed barrel).
12. **Wire safety interlocks**: The machine must NOT inject unless: (a) mold is fully closed and clamp force is at setpoint, (b) nozzle is seated against sprue bushing, (c) operator's two-hand controls are engaged. Wire these interlocks in series with the injection valve solenoid.

**Calibration**: Run 50 automatic cycles with a test mold (simple flat plaque, 100 × 100 × 3 mm). Weigh each part — part weight variation must be <±0.5% across 50 shots. Cycle time consistency: <±2%.

## Quantitative Parameters

### Machine Specifications

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

### Injection Parameters by Material

| Material | Melt Temp (°C) | Mold Temp (°C) | Injection Press (MPa) | Hold Press (MPa) |
|----------|----------------|----------------|-----------------------|-------------------|
| LDPE | 160-240 | 20-40 | 50-100 | 30-60 |
| HDPE | 200-280 | 20-60 | 70-120 | 40-80 |
| PP | 200-260 | 20-60 | 70-120 | 40-80 |
| PS | 180-250 | 20-60 | 60-120 | 30-70 |
| ABS | 210-260 | 50-80 | 80-140 | 50-90 |
| PVC (rigid) | 170-200 | 20-50 | 80-150 | 50-100 |
| Nylon 6 | 240-290 | 60-90 | 80-140 | 50-90 |

### Cycle Time Breakdown (100 × 100 × 3 mm PP Plaque)

| Phase | Duration |
|-------|----------|
| Mold close | 1-2 s |
| Injection (fill) | 0.5-2 s |
| Packing/hold | 2-5 s |
| Cooling | 8-15 s |
| Mold open + ejection | 1-3 s |
| **Total** | **13-27 s** |

## Scaling Notes

- A 50-ton machine with a 30 mm screw produces small parts (up to 50 g shot weight) at high cycle rates. Sufficient for prototyping and low-volume production.
- A 100-200 ton machine with a 40-60 mm screw is the general-purpose workhorse — handles most consumer product and industrial part production. Shot weight up to 500 g.
- Multi-cavity molds multiply output: a 4-cavity mold on a 100-ton machine produces 120-960 parts/hour. Cavity count is limited by clamp force and shot volume.
- Thin-wall molding (wall thickness <1 mm) requires high injection speed (200-500 mm/s) and high pressure (150-200 MPa). This demands a high-flow hydraulic pump or accumulator.
- A hand-operated injection molder (lever-actuated plunger in a heated barrel) can produce simple parts at 10-30 MPa. Clamp by bolting mold halves together. Functional for bootstrapping LDPE, PS, and PP parts.
- Energy consumption: A 100-ton hydraulic injection molder draws 15-30 kW during peak operation (injection + clamp). Annual energy cost can exceed the machine's purchase price. Electric machines reduce energy use by 50-70% but require servo motor manufacturing capability.
- Runner system design: Cold runners (sprue, runners, gates) consume 15-30% of shot volume as waste. Regrind and reuse this material at up to 20% of the total blend. Hot runner systems eliminate runner waste but require heated nozzles and manifold — build cold runner systems first.
- Gate design: The gate is the narrow connection between the runner and the cavity. Gate type affects part appearance and fill pattern. Edge gates (rectangular, 0.5-2 mm thick) are simplest. Submarine gates (tunnel-shaped, self-cutting) automatically separate the runner from the part during ejection. Gate size controls fill rate — too small causes high shear and material degradation; too large leaves a visible mark on the part and requires manual trimming.
- Machine leveling: Level the machine base to within 0.05 mm/m using a precision level. An unlevel machine produces uneven tie rod loading, accelerated platen wear, and inconsistent clamp force distribution across the mold. Check level monthly and after any relocation.
- Nozzle temperature control: The nozzle zone must maintain the polymer at the target melt temperature. A cold nozzle causes the melt to solidify at the tip (cold slug), blocking injection. An overheated nozzle causes drool (melt leaking from the tip between shots). Install a separate PID controller for the nozzle zone with ±2°C accuracy.
- Mold vent cleaning: Mold vents (0.02-0.05 mm deep channels at the parting line) allow trapped air to escape during injection. Vents clog with residual polymer and flash after 1,000-10,000 shots depending on the material. Clean vents with a brass scraper or compressed air during scheduled mold maintenance. Blocked vents cause burning (trapped air ignites at high pressure), short shots, and weak weld lines.
- Startup sequence: Heat all barrel zones to setpoint and wait 30-45 minutes for thermal equilibrium. Set all mold cooling water to operating temperature. Perform an air shot (no mold) to verify melt temperature and injection pressure. Install the mold, set clamp force, and run 5-10 shots into the mold before starting production — the first shots are undersize and discarded. Total startup waste: 5-20 shots depending on mold complexity.
- Shutdown sequence: Purge the barrel with LDPE or the current material until the extrudate runs clear. Retract the injection unit from the mold. Turn off heaters and barrel temperature controllers. Close the mold with low clamp force (to protect the parting line from debris). Never leave the screw retracted with heaters on — the small volume of melt in the nozzle degrades rapidly.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Short shots (incomplete fill) | Insufficient injection pressure or melt too viscous | Increase injection pressure 10-20%; raise barrel temperature 5-10°C; increase injection speed; verify screw check valve is sealing |
| Flash (excess at parting line) | Insufficient clamp force or mold worn | Increase clamp force; reduce injection pressure; inspect mold parting line for wear; check platen parallelism |
| Sink marks | Insufficient holding pressure or time; wall thickness variation | Increase holding pressure and time; redesign part for ±10% wall thickness uniformity |
| Part weight variation >±1% | Screw check valve leaking or inconsistent feeding | Inspect and replace check valve ring; verify hopper feed is uninterrupted; check screw retraction position consistency |
| Nozzle drool | Barrel temperature too high at nozzle zone; no shutoff valve | Lower nozzle zone temperature 5-10°C; install spring-loaded nozzle shutoff valve |
| Machine won't build clamp force | Hydraulic pump worn or relief valve set too low | Check pump flow rate at pressure; verify relief valve setting; inspect cylinder seals for bypass |
| Burn marks on part | Trapped air in mold overheating; injection speed too high | Add or enlarge mold vents (0.02-0.05 mm deep); reduce injection speed; reduce packing pressure |
| Warpage after ejection | Uneven cooling; residual stress from high packing pressure | Reduce packing pressure; ensure uniform mold cooling; increase cooling time 10-20%; use fixture to constrain shape during cooling |
| Silver streaks on part surface | Moisture in resin; degraded polymer in barrel | Pre-dry hygroscopic resins (nylon, PET, ABS) per material spec; purge barrel; reduce rear zone temperature |
| Jetting (snake-like flow pattern) | Gate too large; injection speed too fast for small gate | Reduce injection speed; decrease gate diameter; add a restriction or tab gate to redirect flow |
| Delamination (layers peel apart) | Contaminated resin; incompatible material blend | Clean hopper and barrel; avoid mixing different polymer types; purge thoroughly between material changes |

## Safety

- **Crush hazard (clamp)**: The clamp generates 50-500+ tons of force. A hand caught between closing mold halves is catastrophically crushed. Install two-hand anti-tie-down controls (operator must press both buttons simultaneously to close the mold; releasing either button stops motion). Never reach into the mold area during automatic cycling. Safety gates with interlock switches are mandatory.
- **High-pressure injection**: Polymer at 50-200 MPa can penetrate skin through the nozzle or mold parting line. Injection injuries require immediate surgical debridement — the hot polymer solidifies in tissue. Never look directly at the nozzle during an air shot. Install a splash guard between the injection unit and operator station.
- **Molten polymer burns**: Nozzle and barrel surfaces reach 200-320°C. Use heat-resistant gloves when changing nozzles or purging the barrel. Molten polymer sticks to skin — cool under running water for 15+ minutes, do not peel.
- **Hydraulic hazards**: System pressure at 20 MPa stores significant energy. Hydraulic injection injuries (oil penetrating skin through a pinhole leak) require immediate surgery. Never use hands to search for hydraulic leaks — use cardboard. Install pressure relief valve and verify function monthly.
- **Mold handling**: Production molds weigh 50-500+ kg. Use hoists or cranes for mold installation. Never lift a mold manually above waist height.

## Quality Control

1. **Part weight consistency**: Weigh 10 consecutive parts on a precision scale (0.01 g resolution). Weight variation must be <±0.5%. Weight integrates injection pressure, packing time, and screw position consistency.
2. **Dimensional sampling**: Measure critical dimensions with calipers on 5 parts per 100. Tolerance: ±0.05-0.25 mm depending on part design and mold quality. Track dimensions over time to detect gradual mold wear.
3. **Visual inspection**: Check every part for short shots, flash, sink marks, weld lines, and surface blemishes. Reject rate should be <2% in steady-state production.
4. **Mold maintenance log**: Record shot count per mold. Schedule mold cleaning and inspection every 10,000-50,000 shots depending on material abrasiveness.
5. **Cycle time monitoring**: Track cycle time for each production run. A gradual increase (>5% over baseline) indicates developing problems: worn screw check valve, degraded heater band, or mold vent blockage. Address before part quality degrades.
6. **Screw and barrel inspection**: Measure screw-to-barrel clearance annually. New clearance: 0.05-0.15 mm radial. When clearance exceeds 0.3 mm, shot-to-shot consistency degrades. Resurface or replace the screw. Check the check valve ring for wear — a worn ring allows melt to flow backward during injection, reducing effective injection pressure.

## Variations and Alternatives

- **Reciprocating screw vs. plunger**: The reciprocating screw (described above) is the standard design — it both plasticates and injects. A simpler plunger machine uses a separate ram to push pre-melted polymer from a heated pot into the mold. Plunger machines are easier to build but provide poor melt homogeneity and low shot-to-shot consistency.
- **Hydraulic vs. toggle clamp**: Hydraulic clamp provides direct, controllable force and is simpler to build. Toggle clamp (mechanical linkage) multiplies a small cylinder force into large clamp force but is harder to design and requires precise linkage geometry.
- **Hand-operated injection molder**: For bootstrapping, a lever-actuated plunger in a heated barrel can produce simple parts at low pressure (10-30 MPa). Clamp by bolting the mold halves together. Functional for prototyping and low-volume parts in LDPE, PS, and PP.
- **All-electric machine**: Replaces hydraulics with servo motors and ball screws for each axis. Cleaner, more precise, more energy-efficient, but requires servo motor and ball screw manufacturing capability beyond bootstrap level.
- **Compression molding** ([Compression Press](compression-press.md)): Alternative for thermosets, rubber, and large flat parts. Lower tooling cost but slower cycle and limited part complexity.
- Mold temperature control: Circulate water through drilled channels in the mold at 10-25°C for most thermoplastics. Higher mold temperatures (60-80°C) improve crystallization in semi-crystalline polymers (nylon, PP) but increase cycle time. A 1 kW chiller per 100 cm² of mold surface area is the rough sizing guideline. Mold temperature variation across the cavity produces differential shrinkage and warpage — keep coolant flow balanced between mold halves.
- Runner system economics: A two-plate cold runner mold for a 50 g part with a 4-cavity layout produces 4 parts per cycle but generates 15-25 g of runner waste per cycle. Over 100,000 cycles, that is 1.5-2.5 tonnes of reground waste. A hot runner system eliminates this waste but adds $5,000-20,000 in heated nozzles and manifold — build cold runner systems first.
- Shot size calculation: The screw must deliver enough melt to fill the cavity (or cavities), the runner system, and compensate for shrinkage. Shot volume = (part volume × number of cavities) + runner volume + 10% safety margin. The screw stroke (injection volume) must exceed this calculated shot volume. A 40 mm screw with 150 mm stroke has a maximum injection volume of π/4 × 40² × 150 = 188 cm³.

## References

- [Extruder](extruder.md) — shared barrel/screw technology
- [Blow Molding Equipment](blow-molding-equipment.md) — injection blow molding uses an injection molder for preforms
- [Compression Press](compression-press.md) — simpler alternative for thermosets and rubber
- [Thermoforming Equipment](thermoforming-equipment.md) — lower-cost alternative for large sheet-formed parts
- [Energy Systems](../energy/index.md) — hydraulic system design, fluid selection, pump types
- [Machining](machining.md) — barrel boring, screw turning, platen surfacing
- [Injection Molding Process](../polymers/thermoplastics.md) — polymer-specific injection parameters

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Machine Tools](./index.md) • [All Domains](../../index.md)*
