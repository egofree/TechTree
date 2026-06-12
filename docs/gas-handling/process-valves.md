# Industrial Process Valves

> **Node ID**: gas-handling.process-valves
> **Domain**: [Gas Handling](./index.md)
> **Enables**: `gas-handling`
> **Timeline**: Years 15-35
> **Outputs**: process_valves, control_valves, check_valves, actuated_valves
> **Critical**: Yes — chemical plants, steam systems, and gas processing cannot operate safely without valves rated for the service conditions

## Overview

Industrial process valves control fluid flow in chemical reactors, steam distribution, gas pipelines, and high-pressure process systems. Unlike [water distribution valves](../water/water-valves.md), which operate near ambient temperature at moderate pressure with non-corrosive media, process valves must handle steam above 200°C, corrosive chemicals (acids, alkalis, chlorinated solvents), flammable or toxic gases, and pressures from vacuum to 200+ bar — sometimes several of these simultaneously on a single valve.

A chemical plant with 500 process vessels needs 2,000-5,000 valves. Each must be specified by body material, pressure class, seat material, end connection, and actuator type to match the service. A carbon-steel gate valve that lasts 30 years in steam service will corrode through in weeks if installed in a sulfuric acid line. A bronze globe valve rated for 16 bar water will fail catastrophically at 16 bar steam (200°C) because bronze loses half its yield strength between 20°C and 200°C.

This article covers the six primary valve types used in process service (gate, globe, ball, butterfly, check, control) and their construction from forged or cast steel bodies. Each type serves a distinct function: gate valves for full-flow isolation, globe valves for throttling, ball valves for fast quarter-turn shutoff, butterfly valves for large-diameter isolation, check valves for automatic backflow prevention, and control valves for automated process regulation.

This article covers industrial process valves for chemical, steam, gas, and high-temperature/high-pressure service. For water distribution valves, see [Water Valves](../water/water-valves.md). For valve sealing materials, see [Seals, Gaskets & Packing](../polymers/seals-gaskets.md).

## Prerequisites

- [Iron and steel production](../metals/iron-steel.md) — carbon steel forgings and castings for valve bodies; stainless steel (304L, 316L) for corrosive service
- [Machine tools](../machine-tools/machining.md) — lathe for stem turning, boring bar for body machining, milling for keyways and bolt holes, surface grinding for seat finishing
- [Steel casting](../metals/casting.md) — investment or sand casting for valve bodies in sizes above 50 mm
- [Seals and gaskets](../polymers/seals-gaskets.md) — PTFE packing, graphite packing, spiral-wound gaskets for bonnet joints
- [Non-ferrous metals](../metals/non-ferrous.md) — bronze or brass for small valve bodies and trim components

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Carbon steel (ASTM A216 WCB) | 5-200 kg per valve | Forged or cast body for steam, oil, non-corrosive gas service, rated PN16-PN40 | [Iron & Steel](../metals/iron-steel.md) | Low-alloy steel (Cr-Mo) for high-temperature steam above 400°C |
| Stainless steel (304L or 316L) | 5-150 kg per valve | Corrosive chemical service, food-grade, or clean-in-place systems | [Iron & Steel](../metals/iron-steel.md) | Alloy 20, Hastelloy C for severe corrosion (H₂SO₄, HCl) |
| Bronze (C92200 or C95400) | 1-20 kg per valve | Small-bore gas service (15-50 mm), low-pressure steam below 10 bar | [Non-ferrous Metals](../metals/non-ferrous.md) | Brass (lower pressure, non-critical service only) |
| Stem material (416 SS or 17-4 PH) | 0.5-5 kg per valve | Hardened stainless for stem, must resist galling in packing | [Iron & Steel](../metals/iron-steel.md) | Carbon steel with chrome plating (corrosion risk at packing) |
| Seat material | 1 set per valve | PTFE (−50 to 200°C), reinforced PTFE (−50 to 250°C), Stellite overlay (to 600°C) | [Polymers](../polymers/index.md) | PEEK (to 260°C), metal-to-metal (high-temp) |
| Packing (stem seal) | 1 set per valve | Graphite foil rings or PTFE/graphite interbraided, sized to stem diameter | [Seals & Gaskets](../polymers/seals-gaskets.md) | chevron V-packing (higher friction, better seal at high pressure) |
| Bonnet gasket | 1 per valve | Spiral-wound (304SS/graphite) or RTJ metal ring joint | [Seals & Gaskets](../polymers/seals-gaskets.md) | Flat PTFE envelope gasket (low-pressure only) |

## Process Description

### Gate Valve (Carbon Steel, 100 mm, PN40)

**Principle**: A flat wedge slides perpendicular to flow, clearing the bore when open. Minimal pressure drop in the full-open position because the gate retracts entirely out of the flow path. Used for isolation (fully open or fully closed) in steam lines, process piping, and gas mains. Not for throttling — partially open gate valves create high-velocity jets that erode the seating surfaces.

**Prerequisites**: [Carbon steel casting or forging](../metals/iron-steel.md), [machining](../machine-tools/machining.md), [graphite packing](../polymers/seals-gaskets.md).

**Materials**: Carbon steel body (ASTM A216 WCB, 15-25 kg), stainless steel wedge (410 SS, 2-4 kg), 416 SS stem (1-2 kg), graphite packing, spiral-wound bonnet gasket, cast iron handwheel.

**Construction**:

1. **Cast or forge the valve body**: For 100 mm PN40, investment-cast the body in WCB carbon steel. The body has an inlet and outlet port (flanged or butt-weld ends) and an internal cavity for the wedge. Pour at 1550-1600°C. Normalize at 900°C for 1 hour per 25 mm section thickness, air cool. This relieves casting stresses and refines the grain structure.
2. **Machine the body**: Bore the seat pockets to ±0.05 mm diameter. Face the seat surfaces flat to 0.01 mm across the full diameter — the wedge must seal metal-to-metal against these surfaces. Drill and tap bonnet bolt holes (8× M16 for PN40 100 mm). Bore the stuffing box (bonnet bore) 0.10 mm larger than the stem diameter.
3. **Machine the wedge**: Mill the wedge from 410 SS bar stock with a 2° taper per side. Grind the seating faces to 0.8 μm Ra surface finish. The taper forces line-contact sealing when the gate closes against the body seats.
4. **Make the stem**: Turn the stem from 416 SS on a lathe. Cut an Acme thread (trapezoidal profile, 4 mm pitch) on the upper portion. Machine a T-head on the lower end that engages a slot in the wedge. Harden the stem to HRC 28-32 for wear resistance in the packing.
5. **Assemble**: Place the wedge in the body cavity. Thread the stem through the bonnet. Install graphite packing rings in the stuffing box — stagger the ring joints 90° apart. Compress the packing gland to 60-70% of full gland nut torque. Bolt the bonnet to the body using the spiral-wound gasket. Torque bolts in a cross-pattern sequence to 70-100 N·m (M16 bolts, PN40). Mount the handwheel.

**Calibration**: Close the valve. Pressurize one side to 40 bar (rated pressure). Hold for 5 minutes. Zero visible leakage past the seats is acceptable for metal-seated gate valves. Measure operating torque: 15-40 N·m for 100 mm at rated pressure. Verify full travel: count turns from closed to open (6-10 turns for 100 mm).

**Expected performance**: Size range: 25-600 mm. Pressure rating: PN16-PN100 (16-100 bar). Temperature: −29°C to 425°C (carbon steel WCB). Pressure drop (full open): negligible. Service life: 20-40 years. Not suitable for throttling.

**Strengths**:
- Straight-through flow path — lowest pressure drop of any isolation valve
- Bidirectional sealing — installs in either flow direction
- Rising-stem design provides visual position indication

**Weaknesses**:
- Slow operation — 6-15 turns from closed to open
- Not for throttling — gate erosion and vibration at partial opening
- Large body envelope — requires more installation space than ball or butterfly valves

### Globe Valve (Stainless Steel, 50 mm, PN40)

**Principle**: A disc moves axially onto a circular seat. Flow makes an S-shaped bend through the body, passing through the seat orifice. Higher pressure drop than gate valves but excellent throttling characteristics — flow is approximately linear with stem travel from 20-80% open. Used for flow regulation, pressure reduction, and sampling in chemical and steam service.

**Prerequisites**: [Stainless steel casting](../metals/casting.md), [precision machining](../machine-tools/machining.md), [seat facing materials](../polymers/seals-gaskets.md).

**Materials**: 316L SS body (5-10 kg), 316L disc with Stellite 6 overlay on seating face (0.5-1 kg), 17-4 PH stem (0.5-1 kg), graphite packing, spiral-wound gasket.

**Construction**:

6. **Cast the body**: Investment-cast the globe body in 316L with integral internal baffle. The baffle forces flow through a horizontal seat orifice. Solution-anneal at 1050-1100°C, quench in water. Pickle in 10% HNO₃ + 2% HF to remove scale.
7. **Machine the seat and disc**: Bore the seat orifice to design diameter. Face the seating surface and apply Stellite 6 overlay by GTAW (TIG) welding — the hard face resists erosion and wire-drawing at high pressure drops. Machine the disc with a 15° conical seating face to match. Lap disc to seat with 600-grit compound for line-contact seal.
8. **Assemble**: Connect disc to stem via a swivel joint (allows self-alignment). Install stem through bonnet stuffing box. Pack with graphite rings. Bolt bonnet with gasket. Install handwheel. The disc seats against the flow direction — upstream pressure assists sealing.

**Calibration**: With valve 50% open, flow should be 40-60% of full-open flow (linear characteristic). Verify zero leakage at rated pressure closed. Measure throttling range: 10-90% of stem travel should correspond to 5-95% of flow capacity.

**Expected performance**: Size range: 15-300 mm. Pressure rating: PN16-PN100. Temperature: −196°C to 600°C (with appropriate body material). Pressure drop (full open): 0.3-1.5 bar (S-bend). Throttling: excellent. Service life: 15-30 years (trim replaceable without removing body).

**Strengths**:
- Excellent throttling — linear flow characteristic
- Replaceable seat and disc without removing body from pipeline
- Pressure assists sealing — reliable shutoff

**Weaknesses**:
- Significant pressure drop even fully open
- Higher cost than gate or ball valve per size
- Directional — must install with flow under the disc

### Control Valve (Globe-pattern, Pneumatically Actuated)

**Principle**: A globe-valve body with a characterized plug (equal-percentage, linear, or quick-opening) driven by a pneumatic diaphragm actuator. A positioner receives a 3-15 psi (0.2-1.0 bar) instrument air signal and modulates the actuator to position the plug precisely. Used for automated flow, pressure, temperature, and level control in continuous process plants.

**Prerequisites**: [Globe valve body](#globe-valve-stainless-steel-50-mm-pn40), [instrument air system](basic.md), [machining](../machine-tools/machining.md).

**Materials**: Globe body (per material above), characterized plug (equal-percentage cage or contoured plug), pneumatic diaphragm actuator (6-30 N·m spring range for 50 mm valve), electropneumatic positioner.

**Construction**:

9. **Select the valve body**: Use a globe-pattern body sized by Cv (flow coefficient), not by pipe diameter. Calculate Cv from design flow, inlet pressure, outlet pressure, and fluid properties. A valve sized to match the pipe will be oversized and hunt (oscillate around setpoint). Target 50-70% of stem travel at normal design flow.
10. **Machine the plug and cage**: For equal-percentage characteristic, machine a contoured plug or a cage with shaped ports. The cage is a cylindrical sleeve with port windows — as the plug rises, progressively larger ports are exposed, giving an equal-percentage flow characteristic (each equal increment of travel produces an equal percentage change in flow). Hard-face plug and cage seating surfaces with Stellite 6.
11. **Mount the actuator**: Bolt the pneumatic diaphragm actuator to the bonnet. Connect the actuator stem to the valve stem with a coupling. Calibrate the stroke: 0% signal = fully closed (or fully open for fail-open valves), 100% signal = fully open. Adjust the positioner zero and span. Verify that 3 psi input produces 0% travel and 15 psi produces 100% travel.

**Calibration**: Apply a 4-20 mA signal (converted to 3-15 psi by an I/P converter). Verify stem position at 25%, 50%, 75%, and 100% signal. Stroking time should be 2-10 seconds for full travel (50 mm valve). Check bench set: the spring range must produce rated thrust at supply pressure. Hysteresis (difference in position between increasing and decreasing signal) must be below 2% of span.

**Expected performance**: Size range: 15-300 mm. Pressure rating: PN16-PN400 (with appropriate body). Cv range: 0.1-500. Actuator supply: 3-15 psi instrument air. Stroking time: 2-15 seconds. Positioner accuracy: ±1% of span. Service life: 10-20 years (packing and trim replaced every 3-5 years in severe service).

**Strengths**:
- Automated, continuous process control
- Characterized flow curves (equal-percentage, linear, quick-opening)
- Fail-safe: spring-return actuators fail to closed or open on air loss

**Weaknesses**:
- Requires clean, dry instrument air supply at 5-7 bar
- Periodic calibration needed (positioner drift: 1-2% per year)
- Higher cost and maintenance than manual valves

### Ball Valve (Floating Ball, 50 mm, PN40)

**Principle**: A sphere with a bore rotates 90° to open or close. In process service, the ball is typically "floating" — upstream pressure pushes the ball against the downstream seat, enhancing the seal. Used for fast quarter-turn isolation in chemical and gas service where tight shutoff is required.

**Prerequisites**: [Stainless or carbon steel body](../metals/iron-steel.md), [PTFE or reinforced seats](../polymers/index.md), [precision machining](../machine-tools/machining.md) for ball sphericity.

**Materials**: 316L SS body (3-6 kg), 316L SS ball, chrome-plated (0.5-1 kg), reinforced PTFE seats (2), graphite stem packing, lever or gear operator.

**Construction**:

12. **Machine the body**: Bore a spherical chamber in the body. Machine inlet and outlet ports. Cut seat grooves for the PTFE seats — one on each side of the ball. Bore the stem passage from the top.
13. **Make the ball**: Turn a sphere on a lathe from 316L SS. Bore a full-port hole through the center (equal to pipe ID for full-bore, or 70-80% for reduced-bore). Grind and polish the sphere to 0.2 μm Ra — surface roughness causes seat leakage. Chrome-plate the ball to HRC 55-60 for scratch resistance.
14. **Assemble**: Place PTFE seats in body grooves. Insert ball. Install stem with packing. Bolt body halves together (or insert body insert into body). Torque body bolts to compress seats uniformly. Test 90° rotation from closed to open.

**Calibration**: Pressurize to rated pressure (40 bar) with ball closed. Zero drops per minute past PTFE seats. Verify 90° rotation. Measure operating torque: 10-25 N·m for 50 mm. For fire-safe rated valves, perform a fire test per API 607: heat to 650-980°C for 30 minutes, then verify low leakage through the seats (graphite backup seals activate when PTFE burns out).

**Expected performance**: Size range: 6-300 mm. Pressure rating: PN16-PN100. Temperature: −50°C to 250°C (PTFE seats); to 400°C with metal seats. Pressure drop (full open, full-bore): negligible. Opening: quarter turn. Service life: 15-30 years.

**Strengths**:
- Fast quarter-turn isolation
- Tight shutoff with PTFE seats (bubble-tight)
- Full-bore design — no flow restriction when open

**Weaknesses**:
- Not for throttling — high-velocity jet erodes seats at partial opening
- PTFE seats soften above 200°C (use metal seats for higher temperature)
- Fire-safe version requires secondary metal seat and graphite packing

### Butterfly Valve (Wafer-type, 200 mm, PN16)

**Principle**: A circular disc on a shaft through the pipe center rotates 90° — edge-on parallel to flow (open) or perpendicular blocking flow (closed). The disc seals against an elastomer or PTFE liner inside the body. Dominant choice for large-diameter isolation (150-2400 mm) where gate valves are too heavy and expensive.

**Prerequisites**: [Ductile iron or carbon steel body](../metals/iron-steel.md), stainless steel disc, [elastomer liner](../polymers/rubber.md), [machining](../machine-tools/machining.md).

**Materials**: Ductile iron body (ASTM A536 65-45-12, 10-20 kg), 316L SS disc (3-8 kg), EPDM or Viton liner, 416 SS shaft.

**Construction**:

15. **Cast the body**: Sand-cast a short wafer body (fits between pipe flanges, no flange on the valve itself). Machine the body bore to accept the elastomer liner. Drill and bore the shaft bore through the body top and bottom.
16. **Make the disc and shaft**: Turn the disc from 316L plate to a slightly convex profile (eccentric disc — offset from shaft center so the disc lifts off the seat before rotating, reducing seat wear). Machine the shaft from 416 SS. Key the disc to the shaft.
17. **Install the liner and assemble**: Press the EPDM or Viton liner into the body bore. Insert the disc and shaft through the liner. Install shaft bearings and seals. Mount the lever or gear operator. The wafer body bolts between pipeline flanges using long through-bolts.

**Calibration**: In the closed position, the disc edge must press uniformly into the liner all around the circumference — verify with a 0.05 mm feeler gauge (zero insertion at any point). Torque test: 30-80 N·m for 200 mm at rated pressure. Verify 90° rotation with no binding.

**Expected performance**: Size range: 50-2400 mm. Pressure rating: PN10-PN25. Temperature: −20°C to 150°C (EPDM liner); −10°C to 200°C (Viton liner). Pressure drop (full open): 0.1-0.5 bar. Service life: 10-20 years (liner replacement).

**Strengths**:
- Lightweight and compact — 1/3 the weight of a gate valve at the same size
- Quarter-turn operation
- Economical above 150 mm where gate valves become expensive
- Available in very large sizes (to 2400 mm)

**Weaknesses**:
- Disc remains in the flow path — creates 0.1-0.5 bar pressure drop when open
- Elastomer liner limits temperature (max 200°C for Viton)
- Not suitable for severe throttling — disc edge cavitation

### Swing Check Valve (Carbon Steel, 100 mm, PN40)

**Principle**: A disc on a hinge arm swings open with forward flow and falls shut on flow reversal. Prevents backflow that could damage pumps, contaminate chemical batches, or allow dangerous reverse reactions. No external actuator — automatic from flow direction.

**Prerequisites**: [Carbon steel body](../metals/iron-steel.md), [stainless hinge and disc](../metals/non-ferrous.md), [machining](../machine-tools/machining.md).

**Materials**: WCB carbon steel body (8-15 kg), 316L disc (1-3 kg), 17-4 PH hinge pin (10-15 mm diameter), Stellite-faced seat.

**Construction**:

18. **Cast the body**: Similar to a globe body but with a horizontal hinge pin above the seat. Cast with integral hinge bosses. Machine the seat face and apply Stellite overlay.
19. **Make the disc and hinge arm**: Machine a flat disc from 316L with 2-3 mm overlap past the seat edge. Attach to a hinge arm via a pinned joint. The hinge arm pivots on the body-mounted pin.
20. **Assemble**: Install hinge arm and disc in the body. Insert hinge pin through bosses. Close with bolted cover plate. Disc swings freely from closed (hanging by gravity) to fully open (parallel to flow).

**Calibration**: Blow air through in the forward direction — disc opens freely. Reverse flow — disc seats with no audible leakage. Test at rated pressure: zero visible leakage past the seat. Check slamming tendency: if the valve bangs on pump shutdown, the disc may be oversized for the flow rate.

**Expected performance**: Size range: 15-600 mm. Pressure rating: PN16-PN100. Pressure drop (full open): 0.1-0.5 bar. Closing: automatic. Service life: 10-20 years (hinge pin wear limits life).

**Strengths**:
- Automatic — no actuator or power required
- Protects pumps, reactors, and vessels from reverse flow

**Weaknesses**:
- Disc slam causes water hammer in long pipelines
- Oversized valves slam harder — size for minimum forward velocity above 1 m/s
- Hinge pin wear causes disc flutter and seat leakage

## Quantitative Parameters

### Pressure-Temperature Ratings by Body Material

| Body Material | Standard | PN16 (16 bar) | PN40 (40 bar) | PN100 (100 bar) | Max Temp |
|--------------|----------|---------------|---------------|-----------------|----------|
| Carbon steel (WCB) | ASTM A216 | −29°C to 425°C at 16 bar | −29°C to 425°C at 40 bar (derated above 300°C) | −29°C to 300°C at 100 bar | 425°C |
| 304L stainless | ASTM A351 CF8 | −196°C to 800°C at 16 bar | −196°C to 540°C at 40 bar | −196°C to 350°C at 100 bar | 800°C (derated) |
| 316L stainless | ASTM A351 CF8M | −196°C to 800°C at 16 bar | −196°C to 540°C at 40 bar | −196°C to 350°C at 100 bar | 800°C (derated) |
| Bronze (C92200) | ASTM B61 | −30°C to 230°C at 16 bar | −30°C to 200°C at 20 bar (max) | Not rated | 230°C |
| Ductile iron | ASTM A536 | −20°C to 300°C at 16 bar | −20°C to 250°C at 25 bar (max) | Not rated | 300°C |

### Valve Type Comparison for Process Service

| Parameter | Gate | Globe | Ball | Butterfly | Check | Control |
|-----------|------|-------|------|-----------|-------|---------|
| Size range (mm) | 25-600 | 15-300 | 6-300 | 50-2400 | 15-600 | 15-300 |
| Pressure class | PN16-PN100 | PN16-PN100 | PN16-PN100 | PN10-PN25 | PN16-PN100 | PN16-PN400 |
| Pressure drop (open) | Negligible | 0.3-1.5 bar | Negligible | 0.1-0.5 bar | 0.1-0.5 bar | 0.5-3.0 bar |
| Throttling | No | Excellent | No | Poor | N/A | Excellent |
| Opening speed | Slow (6-15 turns) | Slow (6-15 turns) | Fast (quarter turn) | Fast (quarter turn) | Automatic | 2-15 sec |
| Leakage (new, closed) | Zero (metal seat) | Zero (metal seat) | Zero (PTFE seat) | Near-zero (liner) | Zero (metal seat) | 0.01-0.1% Cv (ANSI Class IV-VI) |
| Service life (years) | 20-40 | 15-30 | 15-30 | 10-20 | 10-20 | 10-20 (trim 3-5) |

### Seat Material Temperature Limits

| Seat Material | Min Temp | Max Temp | Application |
|--------------|----------|----------|-------------|
| PTFE (Virgin) | −50°C | 200°C | Clean chemical service, tight shutoff |
| Reinforced PTFE (15% glass) | −50°C | 250°C | Steam and chemical, better creep resistance |
| PEEK | −40°C | 260°C | High-temp chemical, radiation resistant |
| Stellite 6 (Co-Cr alloy) | −200°C | 600°C | High-temperature steam, erosive service |
| EPDM elastomer | −40°C | 150°C | Water, dilute chemicals, steam below 150°C |
| Viton (FKM) | −20°C | 200°C | Hydrocarbons, acids, high-temp chemical |
| Graphite (flexible) | −200°C | 500°C+ | Fire-safe stem packing, high-temp gaskets |

## Scaling Notes

- **Bench / workshop** (15-50 mm): Bronze and brass globe and ball valves for laboratory and pilot-plant use. Manual handwheel or lever actuation. Threaded (NPT or BSPP) end connections. Total valve count for a bench-scale setup: 5-20. Machined from bar stock, no casting needed.
- **Pilot plant** (25-100 mm): Carbon steel or stainless steel gate, globe, and ball valves. Flanged connections (PN16 or PN40). Some control valves with pneumatic actuators on critical loops. Total valve count: 30-100. Bodies cast or forged. Manual isolation valves with a few actuated control valves.
- **Full chemical plant** (50-300 mm): Steel and alloy valves across all types. 2,000-5,000 valves per plant. 30-60% are control valves with pneumatic or electric actuators. Butt-weld end connections above 50 mm for leak-free service. Material selection per service: carbon steel for steam and hydrocarbons, 316L for acids and alkalis, alloy 20 or Hastelloy for severe corrosion. Every process line has block-and-bleed valve arrangements for positive isolation during maintenance.
- **Steam distribution** (50-600 mm): Gate valves for main isolation, globe valves for pressure reducing stations, check valves on boiler feeds and condensate returns. PN40 minimum for saturated steam above 10 bar (180°C). For superheated steam above 400°C, specify Cr-Mo low-alloy steel bodies (ASTM A217 WC9) — carbon steel creeps and loses strength at sustained high temperature.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gate valve passes flow when fully closed | Seat faces scored by wire-drawing (high-velocity leak erodes a groove in the seat); wedge not fully seated; debris trapped between wedge and seat | Disassemble and inspect seat faces. Re-lap seating surfaces with 600-grit compound. Verify full closure by counting turns. Install a downstream drain to verify zero leakage during isolation. |
| Globe control valve hunts (oscillates) | Valve oversized for the process flow; positioner gain too high; air supply pressure fluctuating | Resize valve Cv for actual operating flow (target 50-70% travel). Reduce positioner gain. Install an air regulator at the valve. Add a volume booster if stroking time exceeds 10 seconds. |
| Ball valve stem leaks to atmosphere | Packing degraded from thermal cycling; packing gland loose; stem scored from galling | Tighten packing gland nuts 1/4 turn. If leak persists, isolate valve, depressurize, and repack. Replace stem if scored deeper than 0.1 mm. For fire-safe valves, verify the secondary graphite packing is intact. |
| Butterfly valve liner extrudes past flange | Over-compression from excessive flange bolt torque; liner material softened by temperature above rating; chemical attack on liner | Re-torque flange bolts to manufacturer specification (do not over-tighten). Check process temperature against liner rating. Replace liner with appropriate material (EPDM → Viton for hydrocarbon service). |
| Check valve slams on pump shutdown | High reverse flow velocity; oversized valve; no damping | Install a spring-loaded silent check valve (faster closing). Reduce valve size to maintain forward velocity above 1 m/s at minimum flow. Add a dashpot or oil-filled damper on the hinge pin for large check valves. |
| Control valve cavitation noise (loud, gravelly) | Pressure drop across valve exceeds the vapor pressure of the liquid — bubbles form and collapse, eroding the plug and cage | Calculate the cavitation index: σ = (P₁ − Pv) / (P₁ − P₂). If σ < 1.0, cavitation is severe. Install two valves in series to split the pressure drop. Use an anti-cavitation trim (multi-stage cage). |
| Stem packing leaks after repacking | Rings installed without staggering joints; wrong packing size; gland cocked (not perpendicular to stem) | Stagger ring joints 90° apart. Verify packing cross-section matches stuffing box dimensions (gap < 0.5 mm). Check gland alignment with a dial indicator — cocked glands cause uneven compression and stem scoring. |

## Safety

- **Trapped pressure between isolation valves**: Two closed valves can trap pressurized, toxic, or flammable fluid. Install a bleed valve (drain) between every pair of isolation valves. Open the bleed before disassembling any valve — verify zero pressure with a gauge. For toxic gas service (H₂S, HCN, chlorine), the bleed must vent to a closed drain or scrubber, not to atmosphere.
- **Valve blowout (bonnet ejection)**: A valve body with corroded or undertorqued bonnet bolts can blow the bonnet off under pressure. The bonnet becomes a projectile. Inspect bolt condition during every maintenance outage — replace bolts with visible corrosion, thread damage, or permanent elongation. Never reuse bonnet gaskets. Torque bonnet bolts in a cross-pattern to the specified value using a calibrated torque wrench.
- **Packing blowout**: Removing packing from a live-pressurized valve can blow the packing rings out of the stuffing box with lethal force. Never remove packing from a valve that has pressure on one side. Isolate, depressurize, and verify zero pressure before repacking. For high-pressure gas service (above 50 bar), use live-loaded packing (spring-loaded gland follower) that maintains compression as packing consolidates.
- **Steam valve burns**: Gate and globe valves in steam service above 150°C conduct heat through the body and stem. Handwheels and levers can reach 60-80°C. Wear insulated gloves when operating steam valves. Install extended bonnets on valves in steam service above 200°C — the packing is located further from the process, keeping packing temperature below 250°C (graphite packing limit).
- **Chemical exposure during valve maintenance**: Drain and flush chemical lines before valve disassembly. Even after draining, residual liquid in the valve cavity can contain concentrated acid or alkali. Wear chemical splash goggles, face shield, and chemical-resistant gloves rated for the specific chemical (check glove permeation charts — nitrile for acids, butyl rubber for ketones, Viton for aromatics).
- **Valve failure in toxic gas service**: A packing leak or seat leak on a chlorine, ammonia, or H₂S line releases toxic gas to the atmosphere. Install double-packed stems with a lantern ring vented to a scrubber. Use bellows-sealed valves for the most hazardous gases — the bellows isolates the stem from the atmosphere, with zero fugitive emissions. Provide emergency isolation valves (quarter-turn ball valves) accessible from a safe distance on every toxic gas line.

## Quality Control

- **Shell (hydrostatic) test**: Pressurize the valve body (with disc/gate partially open) with water to 1.5× rated working pressure. Hold for 5 minutes. Zero visible leaks at body, bonnet, or joints. This verifies the pressure-containing envelope. Record test pressure and hold time on the valve test certificate.
- **Seat (closure) test**: Close the valve. Pressurize one side to 1.1× rated working pressure. Observe the other side. Metal-seated gate and globe valves: zero visible leakage. PTFE-seated ball valves: zero drops per minute. Control valves: per ANSI/FCI 70-2 Class IV (0.01% of rated Cv) or Class V (0.0005 mL per minute per mm of seat diameter per bar differential).
- **Backseat test**: For gate and globe valves with a backseat (a shoulder on the stem that seals against the bonnet when the valve is fully open), open the valve fully, remove the packing, and pressurize. Zero leakage past the backseat verifies that the valve can be repacked under pressure.
- **Operating torque / thrust test**: Measure torque from closed to open at rated differential pressure. Compare to manufacturer specification. Excessive torque (>2× rated) indicates seat damage, misalignment, or undersized actuator. Record torque at 0%, 25%, 50%, 75%, and 100% open.
- **Material verification**: Verify body material by PMI (positive material identification) using a handheld XRF analyzer — a carbon steel valve installed in a stainless line will corrode rapidly. Spark testing (visual) works for field checks: carbon steel produces long white sparks; stainless produces short, few sparks; bronze produces no sparks.
- **Fire-type test** (for fire-safe rated valves): Per API 607 / ISO 10497. Heat the closed valve to 650-980°C for 30 minutes while pressurized. Measure leakage during burning and after cool-down. Through-seat leakage must not exceed 200 mL per minute per inch of nominal diameter. External (stem) leakage must not exceed 100 mL per minute per inch. This test verifies that the secondary metal seat and graphite packing function when the primary PTFE elements burn away.

## Variations and Alternatives

### Plug Valve

A cylindrical or tapered plug with a bore rotates in the body to align the bore with the pipe (open) or block flow (closed). Lubricated plug valves inject grease between the plug and body to seal and lubricate. Used in petroleum and slurry service where ball valve seats would erode. Size: 25-600 mm, PN10-PN25.

### Needle Valve

A small globe valve with a long tapered needle instead of a flat disc. Very fine flow adjustment — the long taper gives precise control over small flow rates. Used for instrument impulse lines, sample points, and chemical dosing at low flow rates. Size: 6-25 mm. Cv: 0.1-2.0.

### Diaphragm Valve

A flexible diaphragm (rubber or PTFE) pressed against a weir by a compressor. The process fluid is isolated from the stem and packing by the diaphragm — zero stem leakage. Used for corrosive chemicals, slurries, and sterile/pharmaceutical service. Size: 15-300 mm. Temperature limited to 150°C (rubber) or 180°C (PTFE).

### Pressure Safety Valve (PSV)

A spring-loaded valve that opens automatically when system pressure exceeds the setpoint, discharging fluid to prevent equipment rupture. Not a process control valve — a safety device. Set at 110% of maximum allowable working pressure (MAWP). Sized to discharge the full process flow without the system pressure exceeding 121% of MAWP (per API 520). Reclose when pressure drops to 93-96% of setpoint (blowdown 4-7%). Must be tested and sealed — never tamper with the adjustment cap in service.

### Actuation Methods Comparison

| Method | Torque Range | Speed | Fail Position | Complexity | Use When |
|--------|-------------|-------|---------------|------------|----------|
| Manual (handwheel) | 5-500 N·m | Slow (seconds to minutes) | Last position | Lowest | Infrequent operation, low safety consequence |
| Manual (lever) | 5-100 N·m | Fast (quarter turn) | Last position | Lowest | Ball and butterfly valves, frequent operation |
| Pneumatic (diaphragm) | 10-1000 N·m | 2-15 seconds | Spring return (fail closed/open) | Medium | Process control, safety shutdown, most common actuator |
| Electric (motor) | 50-5000 N·m | 10-120 seconds | Last position (or battery fail) | High | Large valves, no instrument air available, remote locations |
| Hydraulic | 500-50,000 N·m | 1-30 seconds | Last position (or accumulator) | Highest | Very large valves (>600 mm), high-pressure applications |

## References

- [Basic Gas Handling](basic.md) — gas piping infrastructure and valve requirements for compressed gas
- [Gas Distribution Piping Systems](piping-systems.md) — system-level valve placement in gas distribution networks
- [Water Valves](../water/water-valves.md) — water distribution valves (different service conditions, different article)
- [Seals, Gaskets & Packing](../polymers/seals-gaskets.md) — stem packing, bonnet gaskets, and seat materials
- [Iron & Steel](../metals/iron-steel.md) — body materials: carbon steel, stainless steel, and alloy steels
- [Machining](../machine-tools/machining.md) — turning, boring, milling, and grinding operations for valve components
- [Steam Power](../energy/steam-power.md) — steam distribution valve requirements and pressure-temperature derating

---
*Part of the [Bootciv Tech Tree](../../index.md) • [Gas Handling](./index.md) • [All Domains](../../index.md)*
