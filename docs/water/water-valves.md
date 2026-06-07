# Water Valves

> **Node ID**: water.water-valves
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.sewage`](sewage.md), [`water.desalination`](desalination.md)
> **Timeline**: Years 10-25
> **Outputs**: flow_control, isolation, pressure_regulation
> **Critical**: No — simple plug valves and gate valves can be improvised from wood and leather, but engineered valves are essential for reliable pressurized distribution systems

## Overview

A valve controls fluid flow by introducing a variable restriction into a pipe. Valves are essential in every pressurized water system — they isolate sections for maintenance, regulate flow and pressure, prevent backflow, and provide emergency shutoff. A [distribution network](distribution.md) without valves is uncontrollable: any leak or repair requires shutting down the entire system.

Simple plug valves and gate valves can be improvised from wood and leather for low-pressure gravity systems. Engineered valves — precision-cast bronze or iron bodies with machined seats and stems — are necessary for reliable pressurized distribution at 5-40 bar.

This article covers the four primary valve types used in water service (gate, globe, ball, check) and their construction from cast and machined metal components. Each type serves a distinct function: gate valves for full-flow isolation, globe valves for throttling control, ball valves for fast quarter-turn shutoff, and check valves for automatic backflow prevention.

**Valve sizing principle**: An undersized valve creates excessive pressure drop and restricts flow even fully open. An oversized valve is difficult to control in the throttling range (small changes in stem position produce large flow changes). Rule of thumb: size throttling valves to produce 30-70% of the total system pressure drop at design flow when 50-70% open. For isolation-only service (gate and ball valves), match the valve nominal size to the pipe size.

## Prerequisites

- [Bronze or brass casting](../metals/index.md) for small valve bodies (up to 100 mm)
- [Cast iron casting](../metals/iron-steel.md) for medium and large valve bodies (50-600 mm)
- [Machine tools](../machine-tools/machining.md) — lathe for stem turning, boring for body machining, milling for keyways
- [Polymers](../polymers/index.md) — PTFE for ball valve seats, rubber for gate valve seats, packing materials
- [Precision grinding](../machine-tools/machining.md) for seat facing and ball polishing

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Bronze (valve body, small sizes) | 1-5 kg | C83600 or C84400 (85-5-5-5), for valves up to 100 mm | [Metals](../metals/index.md) | Brass (lower pressure) |
| Cast iron (valve body, medium sizes) | 5-50 kg | Class 30 gray iron, for gate and globe valves 50-300 mm | [Iron & Steel](../metals/iron-steel.md) | Ductile iron (higher pressure) |
| Stainless steel (corrosive service) | 2-20 kg | 316L for water treatment, chemical dosing | [Metals](../metals/index.md) | — |
| Brass (ball valve body) | 1-5 kg | C36000, chrome-plated brass ball | [Metals](../metals/index.md) | Stainless steel ball and body (chemical service) |
| Valve seat material | 1 per valve | PTFE (ball valves), bronze (globe valves), rubber (gate valves) | [Polymers](../polymers/index.md) | Stellite (high-temperature) |
| Packing (stem seal) | 1 set | PTFE/graphite packing rings or O-rings, sized to stem diameter | [Polymers](../polymers/index.md) | Leather (historical, low-pressure) |
| Handwheel or lever | 1 | Cast iron handwheel (gate/globe) or steel lever (ball), sized for required torque | [Iron & Steel](../metals/iron-steel.md) | — |

## Process Description

### Gate Valve (Bronze, 50 mm)

**Principle**: A flat gate (wedge) slides perpendicular to the flow direction, lifting out of the flow path when fully open. Minimal pressure drop in the full-open position because the gate clears the flow path entirely. Used for isolation (fully open or fully closed) — not for throttling. Partially open gate valves vibrate and erode the gate seating surfaces.

**Prerequisites**: [Bronze casting](../metals/index.md), [machining capability](../machine-tools/machining.md), [PTFE or rubber seats](../polymers/index.md).

**Materials**: Bronze body casting (2-3 kg), bronze wedge (0.5-1 kg), brass stem (0.3-0.5 kg), PTFE packing, cast iron handwheel.

**Construction**:

1. **Cast the valve body**: Use a sand mold with cores forming the inlet/outlet passages and the internal wedge cavity. Pour bronze at 1050-1100°C. The body has a flat seating surface where the gate closes (the valve seat). Machine the seat flat to 0.02 mm across the full diameter.
2. **Machine the bonnet and stuffing box**: The bonnet bolts to the body and contains the stem stuffing box (packed gland where the stem exits). Bore the stuffing box 0.10 mm larger than the stem diameter. Drill and tap the bonnet flange for body bolts (4-8 bolts, M8-M16 depending on size).
3. **Make the gate (wedge)**: Cast or machine a tapered wedge from bronze. The taper (typically 1-3° per side) ensures line contact sealing when the gate is forced into the closed position against the seats. Machine the gate faces flat to 0.01 mm.
4. **Make the stem**: Turn the stem from brass bar. Machine a raised thread (Acme thread for strength — trapezoidal profile, 2-4 mm pitch) on the upper portion. The lower end has a T-head that engages a slot in the gate, allowing the gate to slide on the stem while the stem rotates. The stem rises as the gate opens (rising-stem design — visual indication of valve position).
5. **Assemble**: Place the gate in the body cavity. Thread the stem through the bonnet. Install packing rings in the stuffing box around the stem. Bolt the bonnet to the body. Screw on the handwheel. Test by turning — the gate should slide smoothly from full-closed to full-open in 5-12 turns (depending on size).

**Calibration**: Close the valve fully. Pressurize one side to rated working pressure. Check the other side for leakage. Zero visible leakage is acceptable for metal-seated gate valves. Measure operating torque (typically 5-20 N·m for a 50 mm gate valve at rated pressure).

**Expected performance**: Size range: 15-1200 mm. Pressure rating: 10-40 bar. Pressure drop (full open): negligible. Opening speed: slow (5-12 turns). Service life: 20-50 years. Not suitable for throttling.

**Strengths**:
- Lowest pressure drop of any isolation valve — preferred for main distribution lines
- Simple, rugged construction with few wearing parts
- Visual position indication with rising-stem design (stem extends when open)

**Weaknesses**:
- Slow operation — 5-12 turns from closed to open
- Not suitable for throttling — partially open gates vibrate and erode
- Rising-stem design requires clearance above the valve for the stem to extend

### Globe Valve

**Principle**: A disc or plug moves axially against a circular seat (orifice). The flow path makes an S-shaped bend through the valve body. Higher pressure drop than gate valves (even fully open) but excellent throttling characteristics — flow is roughly linear with stem position. Used for flow regulation and control.

**Prerequisites**: [Bronze or cast iron casting](../metals/iron-steel.md), [machining](../machine-tools/machining.md), [seat materials](../polymers/index.md).

**Materials**: Cast iron or bronze body (2-10 kg), bronze disc (0.5-2 kg), brass stem with Acme thread, packing.

**Construction**:

6. **Cast and machine the body**: The globe valve body has an internal baffle that forces flow through a horizontal seat (orifice). Cast the body with the baffle integral. Machine the seat opening to the design diameter and face the seating surface flat.
7. **Make the disc and stem**: Machine the disc (the throttling element) from bronze with a flat or conical seating face that mates with the body seat. The stem connects to the disc via a swivel joint that allows the disc to self-align to the seat. Turn the stem with Acme thread.
8. **Assemble and pack**: Install the stem through the bonnet stuffing box. Connect the disc to the stem. Bolt the bonnet to the body. Install packing. The disc seats against the flow direction — pressure assists sealing.

**Calibration**: With the valve 50% open, measure flow at a known pressure differential. Flow should be approximately linear with stem position from 20-80% open. Measure full-closed leakage (zero visible leakage at rated pressure).

**Expected performance**: Size range: 15-300 mm. Pressure rating: 10-40 bar. Pressure drop (full open): 0.5-2.0 bar (S-bend loss). Throttling: excellent (linear characteristic). Service life: 15-30 years.

**Strengths**:
- Excellent throttling control — flow is roughly linear with stem position
- Seat and disc are replaceable without removing the valve body from the pipeline
- Pressure assists sealing — reliable shutoff even after years of service

**Weaknesses**:
- Significant pressure drop even fully open (0.5-2.0 bar from S-shaped flow path)
- Higher cost than gate or ball valves of the same size
- Larger body footprint than gate valve for the same pipe size

### Ball Valve

**Principle**: A sphere with a bore (port) through its center rotates 90° to align the bore with the pipe (open) or present a solid face to the flow (closed). Full-bore ball valves have a port diameter equal to the pipe inside diameter — zero additional pressure drop when open. Quarter-turn operation (fast opening/closing). Used for isolation where fast shutoff is needed.

**Prerequisites**: [Brass or stainless steel body](../metals/index.md), [PTFE seats](../polymers/index.md), [precision machining](../machine-tools/machining.md) for ball polishing.

**Materials**: Brass body (1-3 kg), chrome-plated brass ball (0.3-1 kg), PTFE seats (2), O-ring stem seals, steel lever handle.

**Construction**:

9. **Machine the body**: Bore a spherical chamber in the brass body to accept the ball. Drill inlet and outlet ports on opposite sides. Machine the seat grooves for PTFE seats (one on each side of the ball). Thread or bore the stem passage from the top of the body to the spherical chamber.
10. **Make the ball**: Turn a brass or stainless steel sphere on a lathe. Bore a full-port hole through the center (diameter equals pipe ID for full-bore, or 70-80% for reduced-port). Polish the sphere to 0.2 μm Ra — surface roughness causes seat leakage.
11. **Machine the stem**: Turn the stem with a flat or square at the lower end that engages a slot in the ball. Install O-ring seals on the stem. The stem turns 90° from closed to open.
12. **Assemble**: Place PTFE seats in the body grooves. Drop the ball into the chamber. Insert the stem through the top bore into the ball slot. Install the handle (lever). Test by rotating — the ball should snap from closed to open with a firm feel from the PTFE seat compression.

**Calibration**: Verify 90° rotation from closed to open. In the closed position, pressurize one side to rated pressure. Check the other side — zero drops per minute for PTFE-seated ball valves. Measure operating torque (typically 5-15 N·m for 50 mm ball valve).

**Expected performance**: Size range: 6-300 mm. Pressure rating: 10-70 bar. Pressure drop (full open, full-bore): negligible. Opening speed: fast (quarter turn). Seat life: 5-10 years (PTFE). Service life: 15-30 years.

**Strengths**:
- Fast quarter-turn operation — ideal for emergency shutoff
- Zero pressure drop when full-bore — no flow restriction
- Tight shutoff with PTFE seats — zero leakage at rated pressure
- Compact body compared to gate valve of same size

**Weaknesses**:
- Not suitable for throttling — partial opening creates high-velocity jet that erodes seats
- Large sizes (>200 mm) require high operating torque — gear operators or powered actuators needed
- PTFE seats degrade above 200°C (not relevant for water service but limits industrial versatility)
- Quick closure can cause water hammer in long pipelines

### Swing Check Valve

**Principle**: Allows flow in one direction only. A disc or flapper is pushed open by forward flow and falls shut when flow reverses. Prevents backflow that could damage pumps, drain tanks, or contaminate supplies. No external actuator — operates automatically from flow direction. Essential on every [pump discharge](centrifugal-pump.md) and at cross-connections between potable and non-potable systems.

**Prerequisites**: [Cast iron or bronze body](../metals/iron-steel.md), [hinge pin and disc](../metals/index.md), [rubber or metal seat](../polymers/index.md).

**Materials**: Cast iron body (2-15 kg), bronze disc (0.5-3 kg), hinge pin (stainless steel, 10-20 mm diameter), rubber seat ring.

**Construction**:

13. **Cast the body**: Similar to a globe valve body but with an internal hinge pin. The disc swings open on a hinge above the seat. Cast with integral hinge pin bosses.
14. **Make the disc and hinge**: Machine a flat disc from bronze that covers the seat orifice with 2-3 mm overlap. Attach the disc to a hinge arm (bronze bar) via a pinned joint. The hinge arm pivots on a pin mounted in the body bosses.
15. **Assemble**: Install the hinge arm and disc in the body. Install the hinge pin through the body bosses and hinge arm. Close the body with a bolted cover plate. The disc should swing freely from closed (hanging by gravity) to fully open (parallel to flow) with no binding.

**Calibration**: Blow air through the valve in the forward direction — the disc should swing open freely. Reverse the flow direction — the disc should seat firmly with no audible leakage. For installed testing: start and stop the pump and listen for a single clean click as the check valve closes. Repeated banging (slamming) indicates the valve is too large for the flow or lacks damping.

**Expected performance**: Size range: 15-600 mm. Pressure rating: 10-40 bar. Pressure drop (full open): 0.1-0.5 bar (disc weight). Closing: automatic. Service life: 10-20 years (hinge pin wear is the limiting factor).

**Strengths**:
- Automatic operation — no external power or actuator required
- Protects pumps and equipment from reverse flow damage
- Simple construction with minimal moving parts

**Weaknesses**:
- Disc slam on flow reversal creates water hammer in long pipelines
- Pressure drop from disc weight (0.1-0.5 bar)
- Hinge pin wear causes disc flutter and leakage over time
- Oversized check valves slam harder — size for minimum forward velocity >1 m/s

## Quantitative Parameters

| Parameter | Gate Valve | Globe Valve | Ball Valve | Check Valve |
|-----------|-----------|-------------|------------|-------------|
| Size range | 15-1200 mm | 15-300 mm | 6-300 mm | 15-600 mm |
| Pressure rating | 10-40 bar | 10-40 bar | 10-70 bar | 10-40 bar |
| Pressure drop (full open) | Negligible | 0.5-2.0 bar (S-bend loss) | Negligible (full-bore) | 0.1-0.5 bar (disc weight) |
| Throttling ability | Poor (not designed for it) | Excellent (linear characteristic) | Poor (not designed for it) | N/A (automatic) |
| Opening speed | Slow (5-12 turns) | Slow (5-15 turns) | Fast (quarter turn) | Instant (automatic) |
| Leakage (closed, new) | Zero (metal-to-metal seat) | Zero (metal-to-metal seat) | Zero (PTFE seat) | Zero (metal-to-metal or rubber seat) |
| Service life | 20-50 years | 15-30 years | 15-30 years (seat replacement 5-10 years) | 10-20 years (hinge wear) |
| Operating torque (50 mm) | 5-20 N·m | 10-25 N·m | 5-15 N·m | N/A (automatic) |

### Valve Sizing by Application

| Application | Valve Type | Size | Material | Flow Velocity | Notes |
|-------------|-----------|------|----------|--------------|-------|
| Household main shutoff | Gate or ball | 25 mm | Bronze | 1-2 m/s | Accessible location required |
| Household fixture stops | Ball | 15 mm | Brass | 1-3 m/s | Quarter-turn under sinks/toilets |
| Village main isolation | Gate | 80-150 mm | Cast iron | 1-2 m/s | Every 200-500 m of main |
| Pump discharge isolation | Gate or ball | Match pump | Cast iron/bronze | 2-3 m/s | Upstream of check valve |
| Pump discharge check | Swing check | Match pump | Cast iron | >1 m/s min | Prevents backspin on pump |
| Filter backwash control | Globe | 50-100 mm | Bronze | 3-5 m/s backwash | Throttling service |
| Chemical dosing line | Globe or needle | 6-15 mm | 316L stainless | 0.5-1 m/s | Corrosion-resistant trim |
| District PRV station | Pressure reducing | 80-200 mm | Ductile iron | 1-2 m/s | Reduces trunk main pressure |
| Air release at high points | Air release | 25-50 mm | Bronze | N/A | Automatic float type |

### Valve Installation Torque Specifications

| Valve Size | Bolt Diameter | Bolt Count | Torque (Nm) | Notes |
|-----------|--------------|-----------|------------|-------|
| 25 mm | M10 | 4 | 20-30 | Hand-tight + 1/4 turn with wrench |
| 50 mm | M12 | 4 | 35-50 | Cross-pattern tightening |
| 100 mm | M16 | 8 | 70-100 | Use torque wrench |
| 150 mm | M20 | 8 | 140-200 | Lubricate bolts before assembly |
| 200 mm | M20 | 12 | 140-200 | Two-stage tightening: 50% then 100% |
| 300 mm | M24 | 16 | 250-350 | Re-torque after 24 hours |

## Scaling Notes

- **Household** (15-50 mm): Bronze gate valves for main isolation, brass ball valves for fixture shutoff, single swing check valve on pump discharge. Total valve count for a household: 5-15. Hand-operation only. Installation with pipe wrenches.
- **Village distribution** (50-200 mm): Cast iron gate valves at every branch connection and every 200-500 m of main for sectional isolation. Swing check valves on pump discharges. Globe valves for filter backwash control. Total valve count: 20-100. Install in valve boxes with access covers.
- **Municipal system** (200-600 mm): Large gate or butterfly valves on trunk mains. Pressure reducing valves (PRVs) at district metering zones to maintain 3-6 bar distribution pressure. Air release valves at all high points. Combination air valves at deep well pump discharges. Total valve count: hundreds to thousands. Gear operators on valves >200 mm.
- **Industrial process** (15-300 mm): Globe control valves with pneumatic or electric actuators for automated flow regulation. Ball valves for chemical isolation. Check valves on every pump discharge. Non-return valves on boiler feed lines. Valve specification per service: material, pressure class, end connection, and actuator type.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Valve leaks when closed | Seat damaged by debris or erosion; gate/disc not fully seated; packing leak mistaken for seat leak | Disassemble and inspect seat faces. Re-lap seat and disc surfaces with lapping compound. Verify full closure by counting turns. Replace packing if leak is at the stem. |
| Valve stuck open or closed | Gate wedged in guides (gate valve); stem corroded; debris trapped in ball seat | Apply penetrating oil to the stem. Tap the handwheel with a soft hammer (never use a pipe wrench on the handwheel). Disassemble and clean if stuck. |
| Ball valve handle spins freely | Stem stripped or broken; ball pinion sheared | Disassemble and replace stem. Verify handle torque rating matches valve size. |
| Check valve slams (loud bang) | High reverse flow velocity; oversized valve; no flow damping | Install a spring-loaded check valve (faster closing, less slam). Add a surge anticipator on the pipeline. Reduce valve size to maintain minimum forward velocity >1 m/s. |
| Valve will not close fully | Debris trapped between disc and seat; stem bent; gate guides worn | Flush the valve body with system pressure while cycling. Inspect internals if flushing fails. Replace bent stems. |
| Globe valve will not regulate flow | Disc worn flat (lost conical profile); seat eroded from cavitation at high pressure drop | Replace disc and re-machine seat. For high pressure drop applications, use two globe valves in series to split the drop. |
| Water hammer when ball valve closes | Rapid closure on long pipeline with high flow velocity | Close valve slowly (1-2 seconds minimum for ball valves). Install a water hammer arrestor or surge anticipator on the pipeline. Consider a slow-closing gate valve instead. |

## Safety

- **Water hammer**: Rapid valve closure (especially quarter-turn ball valves) in long pipelines creates a pressure surge proportional to the fluid velocity and the speed of closure. A 1 m/s flow velocity stopped in 0.1 seconds produces approximately 10 bar surge pressure. Close valves slowly, or install surge suppressors. On pipelines >500 m with flow velocities >2 m/s, motorized slow-closing actuators (30-60 second closure time) are mandatory.
- **Trapped pressure**: A closed valve can trap pressurized fluid between two isolation valves. Install a bleed valve (drain) between isolation valves to relieve trapped pressure before disassembly. Never remove a valve from a pressurized line — verify zero pressure on both sides with a gauge before loosening bolts.
- **Valve blowout**: A valve with corroded or undersized body bolts can blow the bonnet off under pressure. Inspect bolt condition during maintenance — replace any bolt with visible corrosion, stretching, or thread damage. Never reuse gaskets after disassembly.
- **Valve packing under pressure**: Tightening packing glands on a pressurized valve can force the packing material into the stuffing box in an uncontrolled manner. If the packing is leaking too much to tighten safely, isolate and depressurize the line before repacking.

## Quality Control

- **Shell test**: Pressurize the valve body (with gate/disc in partially open position) with water to 1.5× the rated working pressure. Hold for 5 minutes. No visible leaks at the body, bonnet, or joints. This verifies the pressure-containing envelope.
- **Seat test**: Close the valve fully. Pressurize one side to 1.1× rated working pressure. Observe the other side for leakage. Acceptance: zero visible leakage for metal-seated gate and globe valves; zero drops per minute for PTFE-seated ball valves.
- **Operating torque test**: Measure the torque required to operate the valve from full-closed to full-open at rated pressure. Gate and globe valves: typically 5-50 N·m depending on size and pressure. Ball valves: typically 5-30 N·m. Excessive torque indicates seat damage, misalignment, or undersized actuator.
- **Seat flatness verification**: For gate and globe valves, check the seat flatness with a surface plate and feeler gauge. Flatness tolerance: 0.02 mm across the full seat diameter. A non-flat seat leaks regardless of closing force.
- **Material verification**: Verify casting material by spark testing (cast iron produces short orange sparks; bronze produces no sparks; steel produces long white sparks) or by hardness test (Brinell). Using the wrong material for the service (e.g., brass instead of bronze for a high-pressure valve) causes premature failure.

## Variations and Alternatives

### Butterfly Valve

A circular disc mounted on a shaft through the center of the pipe rotates 90° to open or close the flow passage. In the open position, the disc is parallel to the flow (edge-on), presenting minimal obstruction. In the closed position, the disc rotates perpendicular to the flow and seals against an elastomer seat lining the valve body.

**Prerequisites**: [Cast iron or ductile iron body](../metals/iron-steel.md), stainless steel disc, [elastomer seat](../polymers/index.md).

**Expected performance**: Large-diameter isolation (150-2400 mm). Pressure rating: PN10-PN25 (10-25 bar). Quarter-turn operation. The disc remains in the flow path even when open — creates 0.1-0.5 bar pressure drop.

**Strengths**:
- Compact and lightweight compared to gate valves of the same size — a 300 mm butterfly valve weighs 1/3 of an equivalent gate valve
- Quarter-turn operation for fast opening and closing
- Available in very large sizes (up to 2400 mm) where gate valves are not feasible
- Lower cost than gate valves above 200 mm

**Weaknesses**:
- The disc remains in the flow path even when open — creates 0.1-0.5 bar pressure drop
- Not suitable for throttling in most designs (disc edge erosion and cavitation at partial opening)
- Elastomer seat limits temperature capability (typically <80°C for EPDM, <120°C for Viton)

### Plug Valve

A cylindrical or tapered plug with a bore through it rotates in the valve body to align the bore with the pipe (open) or present a solid face to the flow (closed). Similar to a ball valve but with a cylindrical or conical plug instead of a sphere. Lubricated plug valves have a grease injection system that seals and lubricates the plug-body interface.

**Prerequisites**: [Cast iron or steel body](../metals/iron-steel.md), precision-ground plug, lubricant injection fitting.

**Expected performance**: Size range: 25-600 mm. Pressure rating: 10-25 bar. Quarter-turn operation.

**Strengths**:
- Simple, rugged construction with few parts
- Lubricated versions handle abrasive slurries that destroy ball valve seats
- Quarter-turn operation
- Can be maintained in-line by injecting fresh lubricant

**Weaknesses**:
- Lubricated plug valves require periodic grease injection (every 100-500 cycles)
- Higher torque than ball valves of the same size (friction between plug and body)
- Not suitable for precise throttling

### Pressure Reducing Valve (PRV)

A self-actuating globe valve that maintains a constant downstream pressure regardless of upstream pressure variations. A spring-loaded diaphragm senses downstream pressure and modulates the valve disc position to maintain the setpoint. As downstream pressure rises above setpoint, the diaphragm moves to close the valve further. As downstream pressure drops, the spring opens the valve wider.

**Prerequisites**: Globe valve body, diaphragm actuator ([rubber](../polymers/rubber.md) or [elastomer](../polymers/index.md)), pressure spring, pilot sensing line.

**Expected performance**: Size range: 25-300 mm. Reduces trunk main pressure (10-25 bar) to safe distribution pressure (3-6 bar). Self-regulating — no external power required.

**Strengths**:
- Self-regulating — no external power or control system required
- Protects downstream piping and fixtures from overpressure
- Adjustable setpoint via spring tension

**Weaknesses**:
- The pressure reduction creates energy loss (dissipated as heat and noise)
- Diaphragm is a wearing part — replace every 5-10 years
- Can cause cavitation noise if the pressure drop ratio exceeds 3:1 — install in multiple stages for high pressure reduction

## References

- [Water Distribution](distribution.md) — valve placement in distribution networks
- [Pipe Fabrication](pipe-fabrication.md) — pipe materials and jointing methods
- [Centrifugal Pump](centrifugal-pump.md) — check valves on pump discharges
- [Filtration Equipment](filtration-equipment.md) — valve manifolds for filter backwash control
- [Basic Gas Handling](../gas-handling/basic.md) — gas service valves and regulators
- [Iron & Steel](../metals/iron-steel.md) — materials for valve bodies and internals
- [Piping Systems](../gas-handling/piping-systems.md) — gas piping valves and fittings

---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
