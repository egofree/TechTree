# Blow Molding Equipment

> **Node ID**: machine-tools.blow-molding-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`machine-tools.extruder`](extruder.md), [`metals.iron-steel`](../metals/iron-steel.md), [`energy.hydraulics`](../energy/hydraulics.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`chemistry.packaging-testing`](../chemistry/packaging-testing.md)
> **Timeline**: Years 18-28
> **Outputs**: bottles, tanks, hollow_containers, ducting
> **Critical**: No — other methods (rotational molding, welded sheet) can produce hollow parts, but blow molding is the only economical route for high-volume bottle production

## Principle

Blow molding produces hollow plastic parts by extruding or injecting a tube of molten polymer (the parison), enclosing it in a split mold, and inflating it with compressed air against the mold cavity walls. The polymer solidifies on contact with the cooled mold surface, taking the mold's shape. Two principal methods exist:

**Extrusion blow molding**: A continuous parison is extruded downward from a die head. When the parison reaches sufficient length, a split mold closes around it, pinching the bottom and sealing the top around a blow pin. Compressed air (0.2-1.5 MPa) inflates the parison against the mold cavity. After cooling, the mold opens and the part is ejected with flash at the pinch-off points. This is the simpler method, suitable for bottles, jerry cans, drums, and fuel tanks.

**Injection blow molding**: A preform (test-tube shape) is first injection-molded, then reheated and stretch-blown inside the final mold cavity. Biaxial stretching (axial + radial) orients the polymer molecules, dramatically improving tensile strength (300%+ improvement) and gas barrier properties (O₂ permeability reduced 2-3×). Used for PET beverage bottles. This method requires an [injection molding machine](injection-molding-machine.md) for the preform stage.

The blow ratio (maximum molded diameter / initial parison diameter) determines part geometry complexity. Typical blow ratios: 2:1 to 4:1 for standard parts, up to 7:1 for deep-draw containers. Higher blow ratios require higher melt strength polymers and precise parison wall thickness control.

## Prerequisites

- [Extruder](extruder.md) — for parison extrusion in extrusion blow molding
- [Steel plate](../metals/iron-steel.md) — for mold construction and machine frame
- [Compressed air supply](../energy/pneumatics.md) — 0.2-1.5 MPa, clean and dry
- [Hydraulic system](../energy/hydraulics.md) — for mold closing and clamping
- [Cooling water](../water/index.md) — for mold temperature control

## Materials

### Parison Die Head

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Tool steel (die body) | 10-30 kg | P20 or H13, for die head and mandrel | [Iron & Steel](../metals/iron-steel.md) | Mild steel (shorter life, lower precision) |
| Band heater (die head) | 1-2 | 1-3 kW, matched to die geometry | [Electric Furnaces](../energy/electric-furnaces.md) | Gas torch (poor temperature control) |
| Thermocouple | 1 | Type K, 0-400°C | [Measurement](../measurement/precision.md) | RTD sensor |

### Mold

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Aluminum (mold cavities) | 20-100 kg | 6061-T6 or 7075-T6, machined to bottle profile | [Metals](../metals/nonferrous.md) | Steel mold (heavier, harder to machine, better durability) |
| Steel (pinch-off inserts) | 2-5 kg | Hardened tool steel (D2 or O1), sharpened cutting edges | [Iron & Steel](../metals/iron-steel.md) | Brass (wears quickly, acceptable for short runs) |
| Copper tubing (cooling channels) | 5-15 m | 8-12 mm OD, soldered into mold body | [Metals](../metals/nonferrous.md) | Drilled steel cooling channels (harder to fabricate) |
| Guide pins and bushings | 4 sets | Hardened steel, 12-20 mm diameter | [Machine Tools](./index.md) | Tapered alignment dowels (non-adjustable) |

### Mold Clamping and Blow System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (mold mounting platens) | 50-200 kg | A36, 30-50 mm thick | [Iron & Steel](../metals/iron-steel.md) | Cast iron (heavier, better damping) |
| Hydraulic cylinder (clamp) | 1 | Bore 80-150 mm, stroke 200-400 mm, rated to 14 MPa | [Hydraulics](../energy/hydraulics.md) | Pneumatic cylinder (lower force, faster cycle) |
| Blow pin assembly | 1 | Hardened steel tube, 5-15 mm bore, with air inlet and seal | [Iron & Steel](../metals/iron-steel.md) | Standard pipe nipple (no seal, less precise) |
| Air regulator and valve | 1 | 0-2.0 MPa range, solenoid or manual | [Pneumatics](../energy/pneumatics.md) | Needle valve (less repeatable inflation) |
| Stripper plate | 1 | Aluminum or steel, sized to part ejection | [Iron & Steel](../metals/iron-steel.md) | Manual ejection (operator lifts part from mold) |

## Construction Steps

### Parison Die Head

1. **Machine die body**: Turn the die body from P20 tool steel on a lathe. The die head has a conical interior that channels the melt from the extruder barrel into an annular gap between the die body (outer) and the mandrel (inner). The annular gap width determines parison wall thickness: for a 2 mm parison wall, gap = 2 mm at the die lip. Machine the interior to a smooth taper (0.4 μm Ra finish) to prevent dead spots where polymer can degrade.

2. **Machine mandrel**: Turn the mandrel (center pin) from tool steel. The mandrel fits inside the die body with the annular gap set by the mandrel's outer diameter vs. the die body's inner diameter. For adjustable parison wall thickness: machine the mandrel mounting with a threaded adjustment so the mandrel can be raised or lowered by 0.5-2.0 mm, changing the annular gap at the die lip.

3. **Install die heater**: Clamp a band heater around the die body. Wire to a separate PID temperature controller. The die must be at the same temperature as the last barrel zone to prevent premature parison solidification. Install thermocouple in the die wall, 5 mm from the melt channel.

### Blow Mold

4. **Machine mold cavities**: For an aluminum bottle mold: CNC mill or hand-carve the bottle profile into two matching aluminum blocks. Cavity surface finish: polished to 0.2-0.4 μm Ra for glossy bottle surface; bead-blasted for matte finish. Parting line (where the two mold halves meet) must be flat and continuous within 0.02 mm to prevent flash.

5. **Install pinch-off**: Machine hardened steel insert strips along the bottom edge of each mold half where the parison is pinched and sealed. The pinch-off edge is beveled to a sharp cutting edge (0.1-0.3 mm land width) that cuts and welds the parison bottom in one action. The pinch-off land must be exactly aligned between the two mold halves — misalignment causes uneven welds and leaks.

6. **Install cooling channels**: Embed copper tubing in grooves milled into the mold body (on the outside of the cavity, 10-15 mm from the cavity surface). Solder tubing in place. Connect inlet and outlet fittings for cooling water circulation. Water flow rate: 5-15 liters/minute per mold half. Mold temperature: 10-25°C for fast cycle (PE, PP), 40-60°C for thicker wall parts.

7. **Install guide pins**: Mount two guide pins (12-20 mm hardened steel) on one mold half and matching bushings on the other. The pins ensure the two mold halves align precisely when closing. Alignment tolerance at the parting line: 0.02 mm maximum offset.

8. **Install blow pin channel**: Drill or machine a channel through the top of one mold half for the blow pin. The blow pin enters the parison from above (or below, depending on design) and seals against the parison wall with a tapered seat. Air enters through the blow pin bore to inflate the parison.

### Mold Clamping System

9. **Fabricate platens**: Cut two steel plates for mold mounting platens (300-600 mm square, 30-50 mm thick). Mill faces flat within 0.05 mm. Mount one platen rigidly to the machine frame (fixed platen). Mount the other on linear guides (moving platen). Drill mounting holes to accept mold bolt patterns.

10. **Install clamp cylinder**: Mount hydraulic cylinder on the frame behind the moving platen. Connect cylinder rod to the moving platen. Clamp force must exceed the blow pressure × projected part area: for a 0.1 m² bottle at 0.8 MPa blow pressure, minimum clamp force = 80 kN (~8 tonnes). Size the cylinder at 1.5× this value: 120 kN.

11. **Install blow pin actuator**: Mount a pneumatic or hydraulic cylinder to push the blow pin into the parison after mold closing, and retract it before mold opening. Stroke: 50-150 mm. The blow pin must seal against the parison with enough force to prevent air leakage during inflation.

### Air System

12. **Connect air supply**: Connect a regulated compressed air supply to the blow pin via a solenoid valve. Install a pressure regulator (0-2.0 MPa range) and a pressure gauge. Blow pressure for PE bottles: 0.3-0.8 MPa. For PET stretch-blow: 1.0-1.5 MPa.

13. **Install blow timer**: Set an adjustable timer (or PLC-controlled timer) that controls: (a) mold close → (b) blow pin insert → (c) air valve open (inflation) → (d) cooling dwell → (e) exhaust → (f) blow pin retract → (g) mold open. Typical cycle: 5-30 seconds total.

## Calibration and Verification

1. **Parison wall thickness uniformity**: Extrude a parison into open air (no mold). Measure wall thickness at four points around the circumference with a micrometer, at 100 mm intervals along the length. Circumferential variation must be <±10%. Longitudinal variation (die swell) is expected — the mandrel adjustment compensates during production.

2. **Mold alignment check**: Close the empty mold on a sheet of carbon paper between the parting line surfaces. Open and inspect — the imprint must show uniform contact along the entire parting line. Gaps indicate misalignment — adjust guide pins or shim mold mounting.

3. **Pinch-off test**: Close the mold on an extruded parison (no blow air). Open and inspect the pinch weld at the bottom. A good pinch-off produces a clean cut with a uniform weld bead. A ragged or leaking pinch indicates misalignment or dull pinch-off edges.

4. **Leak test (blown part)**: Fill the blown container with water to the rated volume. Apply internal air pressure at 1.5× the intended service pressure. Inspect for leaks at the pinch-off weld, parting line, and neck finish. Zero leaks acceptable.

5. **Volume and dimension check**: Fill the blown container with water and weigh to determine actual volume. Compare to design volume — tolerance: ±3%. Measure OD and height at critical points with calipers: ±1.0 mm for typical bottles.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Container volume range | 10 mL to 250 L (machine-dependent) |
| Blow pressure | 0.2-1.5 MPa (polymer and method dependent) |
| Clamp force | 5-50 tons (typical for bottles) |
| Cycle time | 5-30 seconds (part size dependent) |
| Production rate | 100-700 bottles/hour per station |
| Mold temperature | 10-25°C (fast cycle) or 40-60°C (thick walls) |
| Parison wall thickness | 1-5 mm (at die exit; thins during blowing) |
| Finished wall thickness | 0.3-3.0 mm (varies across part by location and blow ratio) |
| Mold service life | 500,000-5,000,000+ cycles (aluminum) or 1,000,000+ (steel) |
| Duty cycle | Continuous — 24 hours/day operation |

## Strengths

- Economical for hollow parts — blow molds cost $3,000-30,000 vs. $10,000-100,000+ for injection molds
- No core needed — the parison IS the core; air pressure forms the inside surface
- Fast cycle for thin-wall bottles — 5-10 seconds for 500 mL PE bottles
- Mold can be aluminum or even wood for low-pressure, short-run products — much cheaper than steel injection molds

## Weaknesses

- Limited to hollow parts with uniform wall thickness — cannot mold solid features, threads (except in neck area), or precision internal geometry
- Wall thickness varies across the part — thin at corners and deep draws, thick at flat areas — harder to control than injection molding
- Flash at pinch-off must be trimmed — adds a secondary operation (trimming press or manual cutting)
- Part strength is lower than injection-molded equivalents — no molecular orientation control (except in stretch-blow PET)

## Variations and Alternatives

- **Extrusion blow molding vs. injection blow molding**: Extrusion blow molding is simpler and cheaper to set up. Injection blow molding produces bottles with tighter tolerances, better neck finish, and biaxial molecular orientation (PET only). Build extrusion blow molding first; add injection blow molding when PET bottle quality is required.
- **Rotational molding alternative**: For large tanks (100+ liters), rotational molding produces uniform-wall hollow parts with lower tooling cost but much longer cycle times (10-30 minutes). Requires an oven and a rotating mold mechanism, not a blow molding machine.
- **Wooden molds**: For prototyping or very short runs (<100 parts), a split mold carved from hardwood can produce acceptable PE bottles at low pressure (0.2-0.4 MPa). Limited to <500 cycles before mold degrades.

## Safety

- **Pinch points**: The mold closing action generates 5-50+ tons of force. Keep hands clear of the mold area during closing. Install two-hand controls and safety interlock gates.
- **Compressed air**: Blow air at 0.2-1.5 MPa can cause injuries if a fitting fails or a hose whips. Secure all connections with safety chains. Pressure-test the air system at 1.5× maximum working pressure before first use.
- **Hot parison**: The extruded parison exits at 160-240°C. Contact causes thermal burns. Guard the area between the die head and the mold. Do not manually adjust the parison while the extruder is running — use wooden tools if necessary.
- **Mold handling**: Blow molds (especially steel) weigh 20-100+ kg. Use a hoist for installation and removal. Never lift a mold above waist height without mechanical assistance.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Thin walls at corners | Blow ratio too high; parison not centered | Reduce blow ratio (redesign part); adjust die centering; increase parison wall thickness |
| Flash at parting line | Insufficient clamp force; mold alignment off | Increase clamp force; check guide pins and parting line alignment; clean mold faces |
| Leaking pinch-off | Dull pinch-off edges; misalignment | Sharpen or replace pinch-off inserts; realign mold halves; increase pinch-off land width |
| Uneven wall thickness | Parison sag (gravity thins the bottom) | Use higher melt strength polymer; shorten parison extrusion time; install parison wall thickness programmer (variable die gap) |
| Bottle stuck in mold | Insufficient cooling; vacuum formation | Increase cooling water flow; extend cooling dwell time; install air blow-off to break vacuum between part and mold |

## See Also

- [Extruder](extruder.md) — provides the parison melt for extrusion blow molding
- [Injection Molding Machine](injection-molding-machine.md) — provides preforms for injection blow molding
- [Thermoforming Equipment](thermoforming-equipment.md) — alternative for large hollow or curved parts from sheet
- [Compression Press](compression-press.md) — for solid parts that don't require hollow geometry
- [Thermoplastics Processing](../polymers/thermoplastics.md) — polymer-specific blow molding parameters

[← Back to Machine Tools](index.md)
