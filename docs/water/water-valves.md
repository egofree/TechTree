# Water Valves

> **Node ID**: water.water-valves
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.sewage`](sewage.md), [`water.desalination`](desalination.md)
> **Timeline**: Years 10-25
> **Outputs**: flow_control, isolation, pressure_regulation
> **Critical**: No — simple plug valves and gate valves can be improvised from wood and leather, but engineered valves are essential for reliable pressurized distribution systems

## Principle

A valve controls fluid flow by introducing a variable restriction into a pipe. The four primary valve types differ in how they create that restriction:

- **Gate valve**: A flat gate (wedge) slides perpendicular to the flow direction, lifting out of the flow path when fully open. Minimal pressure drop in the full-open position because the gate clears the flow path entirely. Used for isolation (fully open or fully closed) — not for throttling. Partially open gate valves vibrate and erode the gate seating surfaces.
- **Globe valve**: A disc or plug moves axially against a circular seat (orifice). The flow path makes an S-shaped bend through the valve body. Higher pressure drop than gate valves (even fully open) but excellent throttling characteristics — flow is roughly linear with stem position. Used for flow regulation and control.
- **Ball valve**: A sphere with a bore (port) through its center rotates 90° to align the bore with the pipe (open) or present a solid face to the flow (closed). Full-bore ball valves have a port diameter equal to the pipe inside diameter — zero additional pressure drop when open. Quarter-turn operation (fast opening/closing). Used for isolation where fast shutoff is needed.
- **Check valve (non-return)**: Allows flow in one direction only. A disc, ball, or flapper is pushed open by forward flow and falls shut when flow reverses. Prevents backflow that could damage pumps, drain tanks, or contaminate supplies. No external actuator — operates automatically from flow direction.

Valve sizing is critical: an undersized valve creates excessive pressure drop and restricts flow even fully open. An oversized valve is difficult to control in the throttling range (small changes in stem position produce large flow changes). Rule of thumb: size the valve to produce 30-70% of the total system pressure drop at design flow when 50-70% open.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Bronze (valve body, small sizes) | 1-5 kg | C83600 or C84400 (85-5-5-5), for valves up to 100 mm | [Metals](../metals/index.md) | Brass (lower pressure) |
| Cast iron (valve body, medium sizes) | 5-50 kg | Class 30 gray iron, for gate and globe valves 50-300 mm | [Iron & Steel](../metals/iron-steel.md) | Ductile iron (higher pressure) |
| Stainless steel (corrosive service) | 2-20 kg | 316L for water treatment, chemical dosing | [Metals](../metals/index.md) | — |
| Brass (ball valve body) | 1-5 kg | C36000, chrome-plated brass ball | [Metals](../metals/index.md) | Stainless steel ball and body (chemical service) |
| Valve seat material | 1 per valve | PTFE (ball valves), bronze (globe valves), rubber (gate valves) | [Polymers](../polymers/index.md) | Stellite (high-temperature) |
| Packing (stem seal) | 1 set | PTFE/graphite packing rings or O-rings, sized to stem diameter | [Polymers](../polymers/index.md) | Leather (historical, low-pressure) |
| Handwheel or lever | 1 | Cast iron handwheel (gate/globe) or steel lever (ball), sized for required torque | [Iron & Steel](../metals/iron-steel.md) | — |

## Construction Steps

### Gate Valve (Bronze, 50 mm)

1. **Cast the valve body**: Use a sand mold with cores forming the inlet/outlet passages and the internal wedge cavity. Pour bronze at 1050-1100°C. The body has a flat seating surface where the gate closes (the valve seat). Machine the seat flat to 0.02 mm across the full diameter.
2. **Machine the bonnet and stuffing box**: The bonnet bolts to the body and contains the stem stuffing box (packed gland where the stem exits). Bore the stuffing box 0.10 mm larger than the stem diameter. Drill and tap the bonnet flange for body bolts (4-8 bolts, M8-M16 depending on size).
3. **Make the gate (wedge)**: Cast or machine a tapered wedge from bronze. The taper (typically 1-3° per side) ensures line contact sealing when the gate is forced into the closed position against the seats. Machine the gate faces flat to 0.01 mm.
4. **Make the stem**: Turn the stem from brass bar. Machine a raised thread (Acme thread for strength — trapezoidal profile, 2-4 mm pitch) on the upper portion. The lower end has a T-head that engages a slot in the gate, allowing the gate to slide on the stem while the stem rotates. The stem rises as the gate opens (rising-stem design — visual indication of valve position).
5. **Assemble**: Place the gate in the body cavity. Thread the stem through the bonnet. Install packing rings in the stuffing box around the stem. Bolt the bonnet to the body. Screw on the handwheel. Test by turning — the gate should slide smoothly from full-closed to full-open in 5-12 turns (depending on size).

### Globe Valve

6. **Cast and machine the body**: The globe valve body has an internal baffle that forces flow through a horizontal seat (orifice). Cast the body with the baffle integral. Machine the seat opening to the design diameter and face the seating surface flat.
7. **Make the disc and stem**: Machine the disc (the throttling element) from bronze with a flat or conical seating face that mates with the body seat. The stem connects to the disc via a swivel joint that allows the disc to self-align to the seat. Turn the stem with Acme thread.
8. **Assemble and pack**: Install the stem through the bonnet stuffing box. Connect the disc to the stem. Bolt the bonnet to the body. Install packing. The disc seats against the flow direction — pressure assists sealing.

### Ball Valve

9. **Machine the body**: Bore a spherical chamber in the brass body to accept the ball. Drill inlet and outlet ports on opposite sides. Machine the seat grooves for PTFE seats (one on each side of the ball). Thread or bore the stem passage from the top of the body to the spherical chamber.
10. **Make the ball**: Turn a brass or stainless steel sphere on a lathe. Bore a full-port hole through the center (diameter equals pipe ID for full-bore, or 70-80% for reduced-port). Polish the sphere to 0.2 μm Ra — surface roughness causes seat leakage.
11. **Machine the stem**: Turn the stem with a flats or square at the lower end that engages a slot in the ball. Install O-ring seals on the stem. The stem turns 90° from closed to open.
12. **Assemble**: Place PTFE seats in the body grooves. Drop the ball into the chamber. Insert the stem through the top bore into the ball slot. Install the handle (lever). Test by rotating — the ball should snap from closed to open with a firm feel from the PTFE seat compression.

### Swing Check Valve

13. **Cast the body**: Similar to a globe valve body but with an internal hinge pin. The disc swings open on a hinge above the seat. Cast with integral hinge pin bosses.
14. **Make the disc and hinge**: Machine a flat disc from bronze that covers the seat orifice with 2-3 mm overlap. Attach the disc to a hinge arm (bronze bar) via a pinned joint. The hinge arm pivots on a pin mounted in the body bosses.
15. **Assemble**: Install the hinge arm and disc in the body. Install the hinge pin through the body bosses and hinge arm. Close the body with a bolted cover plate. The disc should swing freely from closed (hanging by gravity) to fully open (parallel to flow) with no binding.

## Expected Performance

| Parameter | Gate Valve | Globe Valve | Ball Valve | Check Valve |
|-----------|-----------|-------------|------------|-------------|
| Size range | 15-1200 mm | 15-300 mm | 6-300 mm | 15-600 mm |
| Pressure rating | 10-40 bar | 10-40 bar | 10-70 bar | 10-40 bar |
| Pressure drop (full open) | Negligible | 0.5-2.0 bar (S-bend loss) | Negligible (full-bore) | 0.1-0.5 bar (disc weight) |
| Throttling ability | Poor (not designed for it) | Excellent (linear characteristic) | Poor (not designed for it) | N/A (automatic) |
| Opening speed | Slow (5-12 turns) | Slow (5-15 turns) | Fast (quarter turn) | Instant (automatic) |
| Leakage (closed, new) | Zero (metal-to-metal seat) | Zero (metal-to-metal seat) | Zero (PTFE seat) | Zero (metal-to-metal or rubber seat) |
| Service life | 20-50 years | 15-30 years | 15-30 years (seat replacement 5-10 years) | 10-20 years (hinge wear) |

## Calibration and Verification

1. **Shell test**: Pressurize the valve body (with gate/disc in partially open position) with water to 1.5× the rated working pressure. Hold for 5 minutes. No visible leaks at the body, bonnet, or joints. This verifies the pressure-containing envelope.
2. **Seat test**: Close the valve fully. Pressurize one side to 1.1× rated working pressure. Observe the other side for leakage. Acceptance: zero visible leakage for metal-seated gate and globe valves; zero drops per minute for PTFE-seated ball valves.
3. **Operating torque test**: Measure the torque required to operate the valve from full-closed to full-open at rated pressure. Gate and globe valves: typically 5-50 N·m depending on size and pressure. Ball valves: typically 5-30 N·m. Excessive torque indicates seat damage, misalignment, or undersized actuator.

## Strengths

- Gate valves provide the lowest pressure drop of any isolation valve — preferred for main distribution lines where friction losses must be minimized
- Globe valves offer precise throttling control — the standard for flow regulation, chemical dosing, and pressure reduction
- Ball valves operate with a fast quarter-turn — ideal for emergency shutoff and applications requiring quick isolation
- Check valves protect equipment automatically without power or operator action — essential on every pump discharge

## Weaknesses

- Gate valves should not be used for throttling — partially open gates vibrate, erode seats, and can wedge in position
- Globe valves have significant pressure drop even fully open — the S-shaped flow path adds 0.5-2.0 bar of loss
- Ball valves in large sizes (>200 mm) require high torque to operate — gear operators or powered actuators needed
- Swing check valves slam shut on flow reversal — causes water hammer (pressure surge) in long pipelines. Use spring-loaded or cushioned check valves to mitigate.

## Safety

- **Water hammer**: Rapid valve closure (especially quarter-turn ball valves) in long pipelines creates a pressure surge proportional to the fluid velocity and the speed of closure. A 1 m/s flow velocity stopped in 0.1 seconds produces approximately 10 bar surge pressure. Close valves slowly, or install surge suppressors.
- **Trapped pressure**: A closed valve can trap pressurized fluid between two isolation valves. Install a bleed valve (drain) between isolation valves to relieve trapped pressure before disassembly.
- **Valve blowout**: A valve with corroded or undersized body bolts can blow the bonnet off under pressure. Inspect bolt condition during maintenance. Never remove a valve from a pressurized line.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Valve leaks when closed | Seat damaged by debris or erosion; gate/disc not fully seated; packing leak mistaken for seat leak | Disassemble and inspect seat faces. Re-lap seat and disc surfaces with lapping compound. Verify full closure by counting turns. Replace packing if leak is at the stem. |
| Valve stuck open or closed | Gate wedged in guides (gate valve); stem corroded; debris trapped in ball seat | Apply penetrating oil to the stem. Tap the handwheel with a soft hammer (never use a pipe wrench on the handwheel). Disassemble and clean if stuck. |
| Ball valve handle spins freely | Stem stripped or broken; ball pinion sheared | Disassemble and replace stem. Verify handle torque rating matches valve size. |
| Check valve slams (loud bang) | High reverse flow velocity; oversized valve; no flow damping | Install a spring-loaded check valve (faster closing, less slam). Add a surge anticipator on the pipeline. Reduce valve size to maintain minimum forward velocity >1 m/s. |

## See Also

- [Water Distribution](distribution.md) — valve placement in distribution networks
- [Pipe Fabrication](pipe-fabrication.md) — pipe materials and jointing methods
- [Centrifugal Pump](centrifugal-pump.md) — check valves on pump discharges
- [Basic Gas Handling](../gas-handling/basic.md) — gas service valves and regulators
- [Iron & Steel](../metals/iron-steel.md) — materials for valve bodies and internals
- [Piping Systems](../gas-handling/piping-systems.md) — gas piping valves and fittings

[← Back to Water](index.md)
