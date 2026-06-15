# Compression Press (Heated Platen Press)

> **Node ID**: machine-tools.compression-press
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.index`](../energy/index.md)
> **Enables**: [`polymers.thermosets`](../polymers/thermosets.md), [`polymers.rubber`](../polymers/rubber.md), [`polymers.composites`](../polymers/composites.md), [`glass.fibers`](../glass/fibers.md)
> **Timeline**: Years 12-20
> **Outputs**: molded_thermoset_parts, vulcanized_rubber, laminated_sheet, consolidated_composites
> **Critical**: Yes — the workhorse of thermoset molding and rubber vulcanization; also used for laminate consolidation (FR-4 PCB substrates) and composite curing

## Overview

A compression press uses a hydraulic ram to force two heated platens together, compressing material placed between them inside a mold or directly on the platen surface. The combination of heat and pressure cures (cross-links) thermosetting polymers, vulcanizes rubber, consolidates laminates, and cures composite prepregs. Unlike an [injection molding machine](injection-molding-machine.md), the material is loaded directly into the open mold cavity — no injection unit or screw is needed.

The press generates force through a hydraulic cylinder acting on the moving platen. The stationary (lower) platen supports the mold. Clamping force is calculated as hydraulic pressure × cylinder bore area. A 150 mm bore cylinder at 20 MPa produces 350 kN (~35 tonnes). The heated platens transfer heat to the mold by conduction. Platen temperature control (±2-5°C uniformity) is critical — hot spots overcure, cold spots undercure.

Compression presses serve three distinct polymer processing functions: thermoset compression molding (phenolics, epoxy — 150-200°C, 10-30 MPa, 1-10 min), rubber vulcanization (140-160°C, 15-60 min), and laminate consolidation (FR-4 PCB substrate, phenolic laminate — 150-180°C, 3-10 MPa). The [hydraulic press](hydraulic-press.md) article covers the hydraulic system in detail; this article focuses on the heated platen additions and polymer-specific process requirements.

The compression press is simpler to build than an injection molding machine — it has no screw, no barrel, no injection hydraulic circuit. The mold is also simpler: two halves that close around the preform, with no runner system or gate design. The trade-off is slower cycle time (cure-limited rather than cooling-limited) and limited part complexity. For thermosets and rubber, which cannot be injection-molded (they cure irreversibly and would seize the screw), the compression press is the only practical forming method.

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for frame, platens, and tie rods
- [Machining capability](machining.md) — for platen surfacing, cylinder boring, frame fabrication
- [Hydraulic system](../energy/index.md) — pump, cylinder, valves (see [Hydraulic Press](hydraulic-press.md))
- [Electric heating elements](../energy/electric-furnaces.md) — cartridge heaters or cast-in heaters for platens
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, multiple zones

## Bill of Materials

### Frame

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame members) | 100-400 kg | A36 or equivalent, 15-30 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, no welding) |
| Steel bar (tie rods) | 4 pieces | 1045, 30-50 mm diameter, threaded both ends | [Iron & Steel](../metals/iron-steel.md) | Bolted flanges (heavier, less rigid) |

### Platens

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (platens) | 100-500 kg | A36 or 1045, 40-80 mm thick, machined flat | [Iron & Steel](../metals/iron-steel.md) | Cast iron platens (better heat distribution, brittle) |
| Cartridge heaters | 6-12 | 500-2000 W each, 220 V, 10-16 mm × 100-200 mm | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in tubular heaters (harder to replace) |
| Thermocouples | 2-4 | Type K, 0-300°C, inserted into platen body | [Measurement](../measurement/precision-metrology.md) | RTD sensors (more accurate, slower) |
| Thermal insulation | 5-10 kg | Calcium silicate or mineral wool board, 25 mm | [Ceramics](../ceramics/index.md) | Asbestos (historic, no longer acceptable) |

### Hydraulic System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hydraulic cylinder | 1 | Bore 100-200 mm, stroke 200-400 mm, rated to 20 MPa | [Energy Systems](../energy/index.md) | Screw mechanism (mechanical press) |
| Hydraulic pump | 1 | Gear or piston pump, 10-40 L/min at 20 MPa | [Energy Systems](../energy/index.md) | Hand pump (slower, acceptable for low-volume) |
| Electric motor | 1 | 5-30 kW, 3-phase | [Electric Motor](../energy/electric-motor.md) | Diesel engine (remote locations) |
| Hydraulic oil | 30-100 L | ISO VG 32 or 46 | [Lubricants](../chemistry/lubricants.md) | Filtered vegetable oil |
| Pressure gauge | 1 | 0-30 MPa, Bourdon tube | [Measurement](../measurement/precision-metrology.md) | None — safety-critical |

## Process Description

### Frame Construction

1. **Cut and prepare frame members**: Cut four upright columns (300-400 mm wide flange, 15-25 mm thick, 600-1000 mm tall) and two cross-members from steel plate. Mill mating surfaces flat within 0.05 mm.
2. **Weld or bolt frame**: Weld uprights to base cross-member with full-penetration fillet welds (E7018, 3.2 mm electrode). Reinforce with gusset plates (10 mm, triangular, 100 mm legs). Stress-relieve at 600°C for 2 hours to remove residual stress.
3. **Install tie rods**: Thread four rods (30-50 mm diameter) through the frame. Torque nuts alternately to preload the frame at 1.2× maximum working force.

**Calibration**: Check frame alignment with a straightedge — vertical members must be parallel within 0.05 mm per 100 mm.

**Expected performance**: Frame deflection at rated load: <0.5 mm.

### Heated Platens

4. **Machine platens**: Cut two steel plates to size (300-600 mm square, 50-80 mm thick for lower, 40-60 mm for upper). Mill both faces flat and parallel within 0.05 mm. Working face flatness: 0.02 mm per 100 mm.
5. **Drill heater holes**: Drill a grid of holes (10-16 mm diameter × 100-200 mm deep) on the non-working face. Space 50-80 mm apart for even heat distribution. Each platen typically has 6-12 heaters.
6. **Drill thermocouple wells**: Drill 2-4 holes (6 mm × 50-80 mm deep) from the platen edge toward center. Insert thermocouples with thermal compound. Place one near center and one near each edge.
7. **Install cartridge heaters**: Insert heaters (slip fit, 0.1-0.2 mm clearance). Wire in parallel circuits to PID controllers. Heater power density: 2-4 W/cm² of platen surface.
8. **Install thermal insulation**: Attach 25 mm calcium silicate board to non-working faces. Secure with sheet metal straps.
9. **Mount platens to frame**: Bolt lower platen to frame base (stationary). Mount upper platen on cylinder rod (moving). Align both parallel within 0.05 mm using straightedge and feeler gauges at four corners.

**Calibration**: Heat both platens to 180°C. Wait 30 minutes. Measure surface temperature at five points (center + four corners) with calibrated pyrometer. Maximum deviation: ±5°C. If hot/cold spots exceed this, redistribute heaters.

**Expected performance**: Temperature range: 100-250°C. Uniformity: ±5°C. Control accuracy: ±2°C. Heating rate: <30 minutes from cold to 180°C.

### Hydraulic System and Safety

10. **Mount hydraulic cylinder**: Bolt cylinder to frame head. Align rod axis perpendicular to platens within 0.1 mm per 100 mm. Connect rod to upper platen.
11. **Install hydraulic power unit**: Mount pump, motor, reservoir. Connect to 4-way directional valve, then to cylinder. Install pressure relief valve at 110% of rated.
12. **Fill and bleed**: Fill reservoir with filtered oil. Cycle cylinder 10-20 times to purge air.
13. **Install thermal guards**: Cover exposed heater wiring and hot platen surfaces with sheet metal guards. Attach warning labels.
14. **Install two-hand controls**: Wire platen-close valve to two-hand anti-tie-down station.
15. **Install stroke limiter**: Add adjustable mechanical stops to prevent ram over-travel.

**Calibration**: Install load cell between platens. Apply full hydraulic pressure. Measured force must match theoretical within ±5%. Verify at 25%, 50%, and 100% of rated pressure.

**Expected performance**: Closing speed: 10-50 mm/s (approach), 1-5 mm/s (pressing). System pressure: 10-20 MPa.

## Quantitative Parameters

### Machine Specifications

| Parameter | Value |
|-----------|-------|
| Maximum force | 10-500+ tons (size-dependent) |
| Platen size | 300 × 300 mm to 1000 × 1000 mm |
| Platen temperature range | 100-250°C (cartridge-heated) |
| Temperature uniformity | ±5°C across platen surface |
| Temperature control accuracy | ±2°C at setpoint |
| Daylight (max platen opening) | 200-600 mm |
| Stroke | 150-400 mm |
| Closing speed | 10-50 mm/s (approach), 1-5 mm/s (pressing) |
| Cycle time (thermoset) | 2-10 min (small parts) to 30-60+ min (large laminates) |
| Cycle time (rubber) | 15-60 min (cure-dependent) |
| Platen flatness | ±0.02 mm per 100 mm |
| Service life | 50,000+ cycles before platen resurfacing |

### Cure Parameters by Material

| Material | Temperature | Pressure | Cure Time | Application |
|----------|-------------|----------|-----------|-------------|
| Phenolic molding compound | 150-170°C | 15-30 MPa | 2-5 min | Electrical insulators, handles |
| Epoxy molding compound | 150-180°C | 5-15 MPa | 5-15 min | Electronic encapsulation |
| Polyester (SMC/BMC) | 140-160°C | 5-15 MPa | 2-5 min | Automotive panels |
| Rubber (general) | 140-160°C | 5-15 MPa | 15-60 min | Seals, gaskets, tires |
| FR-4 laminate (epoxy-glass) | 170-180°C | 3-7 MPa | 60-120 min | PCB substrates |
| Phenolic laminate | 150-160°C | 5-10 MPa | 30-60 min | Electrical panels |

### Preform Weight Guidelines

| Material | Part Weight | Preform Weight (part + 8%) | Flash Allowance |
|----------|------------|---------------------------|-----------------|
| Phenolic handle (50 g) | 50 g | 54 g | 4 g |
| Rubber seal (20 g) | 20 g | 22 g | 2 g |
| Epoxy encapsulation (100 g) | 100 g | 108 g | 8 g |
| SMC panel (500 g) | 500 g | 540 g | 40 g |

## Scaling Notes

- A 35-tonne press (150 mm cylinder at 20 MPa) with 300 × 300 mm platens handles most thermoset and rubber molding for small-to-medium parts.
- Scale to 100+ tonnes with 500 × 500 mm platens for large composite panels and laminate sheets. Platen heaters scale proportionally — a 500 × 500 mm platen requires 12-20 kW of heating power.
- Multi-daylight presses (multiple platen sets stacked vertically) double or triple throughput for thin parts like gaskets and seals. Each daylight opening processes independently.
- Vacuum bag consolidation (for aerospace composites) replaces the upper platen with a vacuum bag. Requires an autoclave for external pressure — build the compression press first; add autoclave capability when aerospace-grade composites are demanded.
- Hand-loaded presses cycle at 2-10 parts/hour for thermosets (cure time limited). Automated shuttle systems increase throughput by loading/unloading while the press is closed.
- Multiple platen zones with independent PID control allow temperature profiling across the platen surface. Useful when molds have non-uniform wall thickness that requires different cure rates.
- Daylight opening adjustment: The distance between platens at full open determines the maximum mold height. For deep-draw molds (200+ mm cavity depth), specify 400-600 mm daylight opening. Shallow molds need only 200-300 mm.
- Electrical power consumption: A 35-tonne press with 12 cartridge heaters at 1 kW each draws ~18 kW during heat-up and ~6 kW at steady state. Ensure the electrical supply can handle the peak demand during cold starts.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Uneven cure across part | Platen temperature not uniform | Check cartridge heaters (measure resistance); redistribute thermocouples; clean heater holes |
| Part sticking to mold | Insufficient mold release; mold surface degraded | Apply mold release (silicone or zinc stearate); polish mold surface; re-chrome-plate cavity |
| Excessive flash | Too much preform material; insufficient clamp pressure | Reduce preform weight to part weight + 5-8%; increase press pressure; check platen parallelism |
| Porosity in part | Trapped air or moisture | Pre-dry molding compound; add mold vents; reduce closing speed to allow air escape |
| Platen not reaching temperature | Failed heater or loose thermocouple | Measure heater resistance (open = failed); re-seat thermocouple; check wiring |
| Press force drifts during cure | Hydraulic seal leaking; relief valve wrong | Inspect and replace cylinder seals; verify relief valve setting; check oil level |
| Blisters in rubber parts | Trapped air; insufficient pressure | Add breather grooves in mold; increase pressure 10-20%; extend cure time 10% |
| Surface discoloration | Overcure (temp too high or time too long) | Reduce cure temperature 5-10°C; shorten cure time; verify thermocouple accuracy |
| Mold damage (scratched cavity) | Abrasive filler in compound; improper mold release | Polish mold surface; use zinc stearate release agent; filter fillers to remove oversize particles |
| Part dimension out of tolerance | Preform weight incorrect; platen not parallel | Weigh preforms to ±1% of target; check platen parallelism with dial indicator; adjust tie rod nuts |

## Safety

- **Crush hazard**: The press generates 10-500+ tons of force. Hands caught between closing platens or in the mold are catastrophically crushed. Two-hand anti-tie-down controls are mandatory. Safety gates with interlocks for automatic presses. A 35-tonne press at 20 MPa closes with enough force to amputate any limb caught between the platens.
- **Hot surfaces**: Platens at 150-200°C and molds at the same temperature cause severe thermal burns on contact. Guard all exposed hot surfaces. Use thermal gloves rated to 250°C when handling molds or loading preforms. Burns from 200°C steel are deep second-degree within 1 second of contact.
- **Hydraulic hazards**: System pressure at 20 MPa stores significant energy. Hydraulic injection injuries (oil under pressure penetrating skin through a pinhole leak) require immediate surgical debridement. Never use hands to search for hydraulic leaks — use cardboard or paper.
- **Vulcanization fumes**: Rubber curing releases H₂S (lethal at 100 ppm), SO₂, and mercaptans. Thermoset molding releases formaldehyde (phenolics, IDLH 40 ppm) and styrene (polyester). Provide local exhaust ventilation at 15-20 air changes per hour for curing areas.

## Quality Control

1. **Cure verification (thermosets)**: Break a test part from each batch. A fully cured thermoset fractures with a smooth, glassy break. Undercured shows a rough, fibrous fracture with a characteristic phenolic or amine odor.
2. **Hardness test (rubber)**: Measure Shore A hardness on a flat section of each vulcanized part. Must be within ±3 points of specification. Undercure produces soft spots; overcure produces hard, brittle rubber.
3. **Flash thickness**: Measure flash at parting line with a micrometer. Flash <0.1 mm for precision parts. Thick flash indicates excessive preform weight or insufficient clamp force.
4. **Dimensional check**: Measure critical dimensions with calipers on 3 parts per 100. Tolerance: ±0.1-0.25 mm.
5. **Platen temperature audit**: Monthly, measure platen surface temperature at five points with a calibrated pyrometer while at operating temperature. Maximum deviation from setpoint: ±5°C. Replace failed cartridge heaters immediately to prevent uneven cure.
6. **Hydraulic oil condition**: Check oil clarity and temperature monthly. Cloudy oil indicates water contamination — drain and replace. Oil temperature must not exceed 70°C during operation; higher temperatures degrade seals and reduce oil viscosity.

## Variations and Alternatives

- **Heated platen vs. steam-heated platen**: Electric cartridge heaters are simpler to install and control. Steam-heated platens use drilled channels with 3-10 bar steam — more uniform heating but require a steam boiler. Steam preferred for rubber vulcanization autoclaves; electric for thermoset molding.
- **Transfer molding**: Material is placed in a pot above the mold cavity and forced through runners into the closed mold by a plunger. Better dimensional accuracy for complex parts, but 5-15% material waste in runners. The same press is used — only the mold design changes.
- **Vacuum bag press**: For composite layups, a vacuum bag replaces the upper platen. Vacuum (0.8-0.95 bar) consolidates the layup. An autoclave adds external pressure. Covered in [Composites](../polymers/composites.md).
- **Mechanical (screw) press alternative**: A screw-driven press uses a threaded shaft instead of hydraulics. Simpler (no oil, no seals) but force is less controllable. Suitable for small parts at <10 tonnes.
- **Injection molding** ([injection-molding-machine.md](injection-molding-machine.md)): Faster cycle for thermoplastics but cannot process thermosets or rubber (which cure irreversibly and would seize the screw).
- Preform weight calculation: Weigh the finished part. Add 5-8% for flash and handling. The preform weight must be controlled to ±1% for consistent part quality. Overweight preforms produce excessive flash; underweight preforms produce incomplete parts.
- Mold venting: Trapped air in the mold cavity causes porosity, weak spots, and incomplete fill. Add vent channels 0.02-0.05 mm deep at the mold parting line in the last areas to fill. Vents allow air to escape but are too narrow for the viscous polymer to pass through.
- Typical platen heating power: 2-4 W/cm² of platen surface area. A 300 × 300 mm platen (900 cm²) requires 1.8-3.6 kW of heater power. Heat-up time from cold to 180°C: 20-30 minutes. Steady-state power draw at temperature: 30-40% of installed heater power (the rest is thermostatically cycled).
- Preform shape and placement: For simple flat parts, a rectangular preform slightly smaller than the mold cavity works. For complex parts, shape the preform to approximate the part geometry — this reduces flash and ensures even flow. Place the preform in the center of the cavity. For multi-cavity molds, weigh each preform individually to ±1% for consistent part weight across cavities.
- Mold release agents: Apply to the mold cavity before each cycle. Zinc stearate powder (dust onto the mold surface) is the most common for thermosets. Silicone spray for rubber. For production molding, semi-permanent release coatings (PTFE-based) last 50-200 cycles before reapplication. Do not use oil-based release agents with thermosets — they interfere with the curing reaction.
- Thermoset molding compound storage: Phenolic and epoxy molding compounds have a limited shelf life (3-12 months at room temperature). Store in sealed containers at 15-25°C. Moisture absorption causes blisters during curing. Pre-dry compound at 80-100°C for 30-60 minutes if storage conditions were humid. Compound that has been stored >12 months may require 10-20% longer cure time — test before committing to a production run.
- Mold cleaning procedure: After each production run, remove residual polymer and flash from the mold cavity. Clean with a brass wire brush (not steel — steel scratches the cavity surface) and solvent (acetone for thermosets). Inspect the cavity surface for scratches, dents, or chrome plating damage. Polish with fine abrasive paste if surface defects are visible. Re-apply mold release before the next production run.
- Startup and shutdown procedure: On startup, heat both platens to setpoint and allow 20-30 minutes for thermal equilibrium. Place a test preform in the mold and close the press for one cycle. Inspect the test part for cure quality (break test), flash thickness, and surface appearance before beginning production. On shutdown, turn off heaters and allow the press to cool with the platens open. Never leave the press closed with heaters on — continuous heat degrades the mold surface and wastes energy.
- Curing time optimization: The minimum cure time is determined by the thickest section of the part. Undercured parts are soft, weak, and have a characteristic uncured odor (phenolic or amine). Overcured parts are brittle and discolored. Find the minimum cure time by producing test parts at 30-second intervals (e.g., 2, 2.5, 3, 3.5 minutes) and testing each for hardness and break quality. Use the shortest time that produces a fully cured part — this maximizes production rate.
- Multi-daylight press throughput: For high-volume gasket and seal production, a press with 3-5 daylight openings processes 3-5 parts per cycle in the same footprint. Each opening has its own mold set. The operator loads/unloads one opening while the others are curing. This overlaps loading time with cure time, effectively tripling or quintupling throughput without increasing press size.
- Thermoset material handling: Molding compounds (phenolic, epoxy, polyester SMC) are supplied in bulk form — pellets, powder, or sheet. Pre-weigh preforms to ±1% of target weight before loading into the mold. For sheet molding compound (SMC), cut blanks to the mold cavity size plus 10-20% for flash. Store compounds in sealed containers at 15-25°C. Material that has exceeded its shelf life may require extended cure time or produce parts with poor surface finish.
- Mold material selection: Aluminum molds (6061-T6) are economical for short-to-medium production runs (<10,000 parts). Steel molds (P20 pre-hardened, 30-36 HRC) last 100,000+ parts and resist surface wear from abrasive fillers. For rubber molding, aluminum is sufficient — rubber compounds are non-abrasive. For phenolic molding with mineral fillers, steel molds are necessary — the abrasive filler rapidly erodes aluminum cavity surfaces.
- Flash trimming: After compression molding, trim flash from the part using a trimming press, a hand knife, or a rotary trimmer. The flash thickness at the parting line indicates mold condition: flash <0.1 mm indicates good mold fit and adequate clamp force. Flash >0.3 mm indicates excessive preform weight, worn mold parting line, or insufficient clamp force. Consistent flash patterns across a production run indicate a stable process; variable flash indicates a problem requiring investigation.
- Ejector pin design: Install ejector pins (5-10 mm diameter hardened steel rods) in the mold to push the cured part out of the cavity. Position pins in non-critical areas of the part (flat surfaces, thick sections) where the pin impression does not affect function. Spring-return ejector pins retract automatically when the mold opens. Without ejector pins, parts may stick in the cavity and require manual prying — which damages the mold surface over time.

## References

- [Injection Molding Machine](injection-molding-machine.md) — for thermoplastic parts requiring faster cycle and higher precision
- [Extruder](extruder.md) — for continuous thermoplastic profiles
- [Hydraulic Press](hydraulic-press.md) — hydraulic system construction shared with compression press
- [Thermosets](../polymers/thermosets.md) — thermoset materials processed in compression presses
- [Rubber](../polymers/rubber.md) — rubber vulcanization in compression presses
- [Composites](../polymers/composites.md) — composite layup consolidation using presses
- [Energy Systems](../energy/index.md) — hydraulic system design and component selection

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*

