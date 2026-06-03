# Compression Press (Heated Platen Press)

> **Node ID**: machine-tools.compression-press
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`machine-tools.machining`](machining.md), [`energy.hydraulics`](../energy/hydraulics.md)
> **Enables**: [`polymers.thermosets`](../polymers/thermosets.md), [`polymers.rubber`](../polymers/rubber.md), [`polymers.composites`](../polymers/composites.md), [`glass.fibers`](../glass/fibers.md)
> **Timeline**: Years 12-20
> **Outputs**: molded_thermoset_parts, vulcanized_rubber, laminated_sheet, consolidated_composites
> **Critical**: Yes — the workhorse of thermoset molding and rubber vulcanization; also used for laminate consolidation (FR-4 PCB substrates) and composite curing

## Principle

A compression press uses a hydraulic ram to force two heated platens together, compressing material placed between them inside a mold or directly on the platen surface. The combination of heat and pressure cures (cross-links) thermosetting polymers, vulcanizes rubber, consolidates laminates, and cures composite prepregs. Unlike an injection molding machine, the material is loaded directly into the open mold cavity — no injection unit or screw is needed.

The press generates force through a hydraulic cylinder acting on the moving platen. The stationary (lower) platen supports the mold. Clamping force is calculated as hydraulic pressure × cylinder bore area. A 150 mm bore cylinder at 20 MPa produces 350 kN (~35 tonnes). The heated platens transfer heat to the mold by conduction. Platen temperature control (±2-5°C uniformity) is critical — hot spots overcure, cold spots undercure.

Compression presses serve three distinct polymer processing functions:

1. **Thermoset compression molding**: Phenolic, epoxy, and polyester molding compounds are placed in a heated mold cavity. The mold closes under pressure (10-30 MPa cavity pressure), and the material cures by cross-linking (150-200°C, 1-10 minutes).
2. **Rubber vulcanization**: Uncured rubber preforms are compressed in a heated mold. Sulfur cross-linking proceeds at 140-160°C for 15-60 minutes.
3. **Laminate consolidation**: Prepreg sheets (resin-impregnated fabric) are stacked between caul plates and pressed at 150-180°C under 3-10 MPa to produce laminated sheet (FR-4 PCB substrate, phenolic laminate).

## Prerequisites

- [Steel plate and bar](../metals/iron-steel.md) — for frame, platens, and tie rods
- [Machining capability](machining.md) — for platen surfacing, cylinder boring, frame fabrication
- [Hydraulic system](../energy/hydraulics.md) — pump, cylinder, valves
- [Electric heating elements](../energy/electric-furnaces.md) — cartridge heaters or cast-in heaters for platens
- [Temperature controllers](../electronics/electrical-systems.md) — PID-type, multiple zones

## Materials

### Frame

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (frame members) | 100-400 kg | A36 or equivalent, 15-30 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron frame (heavier, no welding) |
| Steel bar (tie rods) | 4 pieces | 1045, 30-50 mm diameter, threaded both ends | [Iron & Steel](../metals/iron-steel.md) | Bolted flanges (heavier, less rigid) |
| Bolts and nuts | 5-15 kg | Grade 8.8, M16-M24 | [Fasteners](../metals/fasteners.md) | Riveted joints (non-adjustable) |

### Platens

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (platens) | 100-500 kg | A36 or 1045, 40-80 mm thick, machined flat | [Iron & Steel](../metals/iron-steel.md) | Cast iron platens (better heat distribution, more brittle) |
| Cartridge heaters | 6-12 | 500-2000 W each, 220 V, 10-16 mm diameter × 100-200 mm | [Electric Furnaces](../energy/electric-furnaces.md) | Cast-in tubular heaters (embedded in platen, harder to replace) |
| Thermocouples | 2-4 | Type K, 0-300°C, inserted into platen body | [Measurement](../measurement/precision.md) | RTD sensors (more accurate, slower response) |
| Thermal insulation | 5-10 kg | Calcium silicate or mineral wool board, 25 mm thick | [Ceramics](../ceramics/index.md) | Asbestos (historic, no longer acceptable) |

### Hydraulic System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Hydraulic cylinder | 1 | Bore 100-200 mm, stroke 200-400 mm, rated to 20 MPa | [Hydraulics](../energy/hydraulics.md) | Screw mechanism (mechanical press, slower, no hydraulic seals) |
| Hydraulic pump | 1 | Gear or piston pump, 10-40 L/min at 20 MPa | [Hydraulics](../energy/hydraulics.md) | Hand pump (slower cycling, acceptable for low-volume) |
| Electric motor | 1 | 5-30 kW, 3-phase | [Electric Motors](../energy/electric-motors.md) | Diesel engine (remote locations) |
| Hydraulic oil | 30-100 L | ISO VG 32 or 46 | [Lubricants](../petroleum/lubricants.md) | Filtered vegetable oil (shorter oil life) |
| Pressure gauge | 1 | 0-30 MPa, Bourdon tube | [Measurement](../measurement/precision.md) | None — safety-critical indicator |
| Pressure relief valve | 1 | Pilot-operated, set to 110% of max working pressure | [Hydraulics](../energy/hydraulics.md) | None — safety-critical component |

## Construction Steps

### Frame

1. **Cut and prepare frame members**: Cut four upright columns (300-400 mm wide flange, 15-25 mm thick, 600-1000 mm tall) and two cross-members (same section, 400-600 mm wide) from steel plate. An H-frame design with four tie rods is preferred for rigidity. Mill mating surfaces flat within 0.05 mm.

2. **Weld or bolt frame**: For a welded H-frame: weld uprights to base cross-member with full-penetration fillet welds (E7018, 3.2 mm electrode). Reinforce with gusset plates (10 mm, triangular, 100 mm legs). Stress-relieve the completed frame at 600°C for 2 hours to remove welding residual stress. Alternatively, use bolted construction with Grade 8.8 bolts for disassembly capability.

3. **Install tie rods**: Thread four rods (30-50 mm diameter) through the frame. Install nuts on both ends. Torque alternately and evenly to preload the frame — preload must exceed the maximum working force by 20% to prevent joint separation during pressing.

### Platens

4. **Machine platens**: Cut two steel plates to size (300-600 mm square, 50-80 mm thick for the lower platen; 40-60 mm thick for the upper platen). Mill both faces flat and parallel within 0.05 mm across the full surface. Surface finish: 1.6 μm Ra or better. The working face (mold contact side) must be flat within 0.02 mm per 100 mm to ensure uniform pressure on the mold.

5. **Drill heater holes**: Drill a grid pattern of holes (10-16 mm diameter × 100-200 mm deep) into each platen for cartridge heaters. Space holes 50-80 mm apart in a uniform grid to provide even heat distribution. Drill from the non-working face (bottom for lower platen, top for upper platen). Each platen typically has 6-12 heaters.

6. **Drill thermocouple wells**: Drill 2-4 holes (6 mm diameter × 50-80 mm deep) from the edge of each platen toward the center. Insert thermocouples and pack with thermal compound for good thermal contact. Place one thermocouple near the center and one near each edge to monitor temperature uniformity.

7. **Install cartridge heaters**: Insert cartridge heaters into the drilled holes. The heaters should be a slip fit (0.1-0.2 mm clearance) for easy replacement. Connect heaters in parallel circuits to a PID temperature controller. Wire each platen on a separate controller. Heater power density: 2-4 W/cm² of platen surface area for adequate heating rate.

8. **Install thermal insulation**: Attach 25 mm calcium silicate or mineral wool insulation board to the non-working face of each platen. This reduces heat loss and protects the hydraulic cylinder and frame from radiant heat. Secure with sheet metal straps or high-temperature adhesive.

9. **Mount platens to frame**: Bolt the lower platen to the frame base (stationary). Mount the upper platen on the hydraulic cylinder rod (moving). Align both platens parallel within 0.05 mm over the full platen area using a precision straightedge and feeler gauges at four corners. Shim the lower platen as needed.

### Hydraulic System

10. **Mount hydraulic cylinder**: Bolt the hydraulic cylinder to the frame head (top cross-member). Align cylinder rod axis perpendicular to the platens within 0.1 mm per 100 mm. Connect the cylinder rod to the upper platen with a threaded connection or flange.

11. **Install hydraulic power unit**: Mount pump, motor, and reservoir on the machine base or a separate skid. Connect pump outlet to a 4-way, 3-position directional control valve. Connect valve output to cylinder ports. Install pressure relief valve in the pump-to-valve line, set to 22 MPa (110% of 20 MPa rated).

12. **Install pressure gauge and controls**: Mount a 0-30 MPa pressure gauge in the line between valve and cylinder. The gauge is the primary indicator of press force — operators use pressure readings to control the process. Install a pressure switch or transducer if automated force control is desired.

13. **Fill and bleed**: Fill reservoir with filtered hydraulic oil. Bleed air from the system by cycling the cylinder slowly 10-20 times.

### Safety Features

14. **Install thermal guards**: Cover all exposed heater wiring and hot platen surfaces with sheet metal guards. The guards prevent accidental contact with surfaces at 150-200°C. Attach warning labels indicating hot surfaces.

15. **Install two-hand controls**: Wire the platen-close valve to a two-hand anti-tie-down control station. The operator must press both buttons simultaneously to close the press; releasing either button stops platen motion. This prevents hands from being in the danger zone during closing.

16. **Install stroke limiter**: Add adjustable mechanical stops to prevent the ram from over-traveling when no mold is installed. This protects the platens from slamming together.

## Calibration and Verification

1. **Platen parallelism**: Close the platens on a precision straightedge placed diagonally. Measure gap at four corners with feeler gauges. Maximum deviation: 0.05 mm per 300 mm of platen width. Adjust by shimming the lower platen or re-aligning the cylinder.

2. **Temperature uniformity**: Heat both platens to 180°C (typical thermoset molding temperature). Wait 30 minutes for thermal equilibrium. Measure surface temperature at five points (center + four corners) with a calibrated pyrometer. Maximum deviation across the platen: ±5°C. If hot or cold spots exceed ±5°C, redistribute or replace cartridge heaters.

3. **Force calibration**: Place a calibrated load cell between the platens. Apply full hydraulic pressure. Compare measured force to theoretical (pressure × cylinder bore area). Force must be within ±5% of calculated value. Verify at three pressure levels: 25%, 50%, and 100% of rated.

4. **Temperature control response**: Set platen temperature to 180°C. Record time to reach setpoint from cold start (target: <30 minutes). Apply a step change to 200°C. Verify overshoot is <5°C and settling time is <5 minutes.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Maximum force | 10-500+ tons (size-dependent) |
| Platen size | 300 × 300 mm to 1000 × 1000 mm |
| Platen temperature range | 100-250°C (cartridge-heated) |
| Temperature uniformity | ±5°C across platen surface |
| Temperature control accuracy | ±2°C at setpoint |
| Daylight (max platen opening) | 200-600 mm |
| Stroke | 150-400 mm |
| Closing speed | 10-50 mm/second (approach), 1-5 mm/second (final pressing) |
| Hydraulic system pressure | 10-20 MPa (typical) |
| Cycle time (thermoset) | 2-10 minutes (small parts) to 30-60+ minutes (large laminates) |
| Cycle time (rubber) | 15-60 minutes (cure-dependent) |
| Platen flatness | ±0.02 mm per 100 mm |
| Service life | 50,000+ cycles before platen resurfacing needed |

## Strengths

- Simple and robust — no screw, no injection unit, fewer moving parts than an injection molder
- Processes materials that cannot be injection-molded — thermosets (which cure irreversibly) and rubber (which vulcanizes)
- Lower mold cost than injection molds — compression molds need no runner system, no injection pressure containment
- Handles large parts — platen presses can be scaled to 1 m × 1 m or larger for composite panels and laminate sheets
- Versatile — same machine processes thermosets, rubber, laminates, and composites by changing molds and temperature settings

## Weaknesses

- Slow cycle time — cure/vulcanization times of 2-60+ minutes vs. 15-120 seconds for injection molding
- Manual loading and unloading — each cycle requires the operator to load preforms and remove parts (unless automated with a shuttle system)
- Flash is inevitable — excess material squeezes out at the mold parting line and must be trimmed
- Limited part complexity — compression molding produces parts with simpler geometry than injection molding; undercuts, thin ribs, and complex cores are difficult

## Variations and Alternatives

- **Heated platen vs. steam-heated platen**: Electric cartridge heaters (described above) are simpler to install and control. Steam-heated platens use drilled channels with 3-10 bar steam — more uniform heating but require a steam boiler. Steam is preferred for rubber vulcanization autoclaves; electric for thermoset molding.
- **Transfer molding**: A variation where material is placed in a pot above the mold cavity and forced through runners into the closed mold by a plunger. Better dimensional accuracy for complex parts, but 5-15% material waste in the runner system. Transfer molding is a mold design variation, not a different machine — the same press is used.
- **Vacuum bag press**: For composite layups, a vacuum bag replaces the upper platen. Vacuum (0.8-0.95 bar) consolidates the layup. An autoclave adds external pressure on top of vacuum. Both are covered in the [Composites](../polymers/composites.md) article.
- **Mechanical (screw) press alternative**: A screw-driven press uses a threaded shaft instead of hydraulics. Simpler (no oil, no seals) but force is less controllable. Suitable for small parts at low force (<10 tonnes).

## Safety

- **Crush hazard**: The press generates 10-500+ tons of force. Hands caught between closing platens or in the mold are catastrophically crushed. Two-hand anti-tie-down controls are mandatory. Safety gates with interlocks for automatic presses.
- **Hot surfaces**: Platens at 150-200°C and molds at the same temperature cause severe thermal burns on contact. Guard all exposed hot surfaces. Use thermal gloves rated to 250°C when handling molds or loading preforms.
- **Hydraulic hazards**: System pressure at 20 MPa stores significant energy. Hydraulic injection injuries (oil under pressure penetrating skin) require immediate surgical debridement. Never use hands to search for leaks — use cardboard or paper.
- **Vulcanization fumes**: Rubber curing releases H₂S, SO₂, and mercaptans. Thermoset molding releases formaldehyde (phenolics) and styrene (polyester). Provide local exhaust ventilation at the press — 15-20 air changes per hour for curing areas.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Uneven cure across part | Platen temperature not uniform | Check cartridge heaters (measure resistance); redistribute thermocouple positions; clean heater holes for better contact |
| Part sticking to mold | Insufficient mold release; mold surface degraded | Apply mold release (silicone or zinc stearate); polish mold surface; re-chrome-plate mold cavity |
| Excessive flash | Too much material in preform; insufficient clamp pressure | Reduce preform weight to part weight + 5-8%; increase press pressure; check platen parallelism |
| Porosity in part | Trapped air or moisture in material | Pre-dry molding compound; add mold vents; reduce closing speed to allow air escape before full pressure |
| Platen not reaching temperature | Failed heater or loose thermocouple | Measure heater resistance (open circuit = failed); re-seat thermocouple; check heater wiring connections |
| Press force drifts during cure | Hydraulic seal leaking; relief valve set wrong | Inspect and replace cylinder seals; verify relief valve setting with gauge; check oil level |

## See Also

- [Injection Molding Machine](injection-molding-machine.md) — for thermoplastic parts requiring faster cycle and higher precision
- [Extruder](extruder.md) — for continuous thermoplastic profiles
- [Thermosets](../polymers/thermosets.md) — thermoset materials processed in compression presses
- [Rubber](../polymers/rubber.md) — rubber vulcanization in compression presses
- [Composites](../polymers/composites.md) — composite layup consolidation using presses
- [Hydraulics](../energy/hydraulics.md) — hydraulic system design and component selection

[← Back to Machine Tools](index.md)
