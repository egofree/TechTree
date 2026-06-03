# Thermoforming Equipment

> **Node ID**: machine-tools.thermoforming-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.pneumatics`](../energy/pneumatics.md), [`energy.electric-motors`](../energy/electric-motors.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`chemistry.packaging-testing`](../chemistry/packaging-testing.md)
> **Timeline**: Years 15-22
> **Outputs**: formed_trays, containers, panels, signs, boat_hulls, enclosures
> **Critical**: No — injection molding and compression molding can produce most thermoformed shapes, but thermoforming has much lower tooling cost and handles large parts that are impractical to injection-mold

## Principle

Thermoforming heats a flat thermoplastic sheet to its softening temperature (just above Tg for amorphous polymers, just above melting point for semi-crystalline), then stretches it over or into a mold using vacuum, compressed air, or mechanical force. The sheet cools against the mold surface, retaining the molded shape. The process is limited to thin-wall, open-top shapes (trays, containers, panels, housings) but offers the lowest tooling cost of any plastic forming method.

Two main methods exist:

**Vacuum forming**: The heated sheet is clamped over a mold. A vacuum pump draws air through small holes (0.5-1.0 mm) drilled in the mold surface. Atmospheric pressure (0.1 MPa) pushes the softened sheet onto the mold. Simple, low cost, suitable for shallow-draw parts. Draw ratio (depth / smallest plan dimension) limited to approximately 0.5:1 without assist.

**Pressure forming**: Compressed air (0.3-0.7 MPa) is applied above the sheet while vacuum is applied below. The higher forming pressure produces sharper detail and allows deeper draws (up to 1.5:1 with plug assist). Requires a sealed pressure box above the sheet. Pressure forming approaches injection molding in surface detail for a fraction of the tooling cost.

A plug assist (a shaped mechanical pusher) pre-stretches the sheet into the mold cavity before vacuum or pressure is applied. Plug assist distributes material more evenly across deep draws, preventing excessive thinning at corners.

## Prerequisites

- [Steel plate and sheet](../metals/iron-steel.md) — for frame, clamp, and pressure box
- [Vacuum pump](../energy/pneumatics.md) — capable of 0.8-0.95 bar negative pressure
- [Compressed air supply](../energy/pneumatics.md) — 0.3-0.7 MPa for pressure forming
- [Electric heating elements](../energy/electric-furnaces.md) — infrared heaters or oven elements
- [Temperature controller](../electronics/electrical-systems.md) — for heater regulation

## Materials

### Heating System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Infrared heaters (quartz or ceramic) | 4-12 | 500-2000 W each, 220 V, with reflectors | [Electric Furnaces](../energy/electric-furnaces.md) | Cal-rod elements in a reflector housing (slower, less uniform) |
| Heater mounting frame | 1 | Steel angle or channel, sized to sheet area + 100 mm margin | [Iron & Steel](../metals/iron-steel.md) | Aluminum extrusion frame (lighter, less rigid) |
| Thermocouple or pyrometer | 1 | Type K, 0-300°C, or non-contact IR pyrometer | [Measurement](../measurement/precision.md) | Surface thermometer (slower response) |

### Forming Table and Clamp Frame

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (vacuum platen) | 1 | 10-15 mm thick, machined flat, sized to max sheet dimension | [Iron & Steel](../metals/iron-steel.md) | Cast aluminum platen (lighter, less rigid) |
| Steel angle (clamp frame) | 4-8 m | 40-50 mm angle, 3-5 mm thick | [Iron & Steel](../metals/iron-steel.md) | Aluminum angle (lighter, flexes under clamp force) |
| Clamp mechanism | 4-8 | Toggle clamps or pneumatic cylinders, 500-2000 N each | [Machine Tools](./index.md) | C-clamps (slow, manual) |
| Vacuum seal gasket | 4-8 m | Silicone rubber cord, 6-10 mm diameter | [Elastomers](../polymers/rubber.md) | Foam weatherstrip (short life, poor seal) |

### Vacuum System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Vacuum pump | 1 | Rotary vane or piston, 5-25 m³/hour, to 0.1 mbar | [Pneumatics](../energy/pneumatics.md) | Venturi vacuum generator (uses compressed air, lower vacuum) |
| Vacuum receiver tank | 1 | 20-100 L, rated to full vacuum, with drain | [Pressure Vessels](../chemistry/pressure-vessels.md) | Direct pump connection (slower vacuum response) |
| Vacuum gauge | 1 | 0 to -1.0 bar | [Measurement](../measurement/precision.md) | None — needed to verify vacuum level |
| Solenoid valve | 1 | 2-way normally closed, 12-24 VDC, sized to vacuum line | [Pneumatics](../energy/pneumatics.md) | Manual ball valve (slower cycle, operator must open/close) |
| Vacuum hose | 2-5 m | Reinforced rubber, 25-40 mm ID, rated to full vacuum | [Elastomers](../polymers/rubber.md) | PVC tubing (collapses under vacuum) |

### Mold

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Wood (prototype molds) | Variable | Hardwood (maple, birch), sealed with shellac or epoxy | [Wood](../foundations/tools-basic.md) | Cast plaster (fragile, limited cycles) |
| Aluminum (production molds) | Variable | 6061-T6, machined or cast to part profile | [Nonferrous Metals](../metals/nonferrous.md) | Epoxy cast (intermediate durability) |
| Vacuum holes | 50-200 | 0.5-1.0 mm diameter, drilled through mold into vacuum plenum | — | Grooves (0.5 mm wide) at mold surface (easier to make, visible marks on part) |

### Pressure Forming (Optional)

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (pressure box lid) | 1 | 5-10 mm thick, with gasket seal, sized to clamp frame | [Iron & Steel](../metals/iron-steel.md) | Aluminum plate (lighter, flexes at high pressure) |
| Air inlet valve | 1 | Solenoid or manual, rated to 0.7 MPa | [Pneumatics](../energy/pneumatics.md) | — |
| Pressure regulator | 1 | 0-0.7 MPa output | [Pneumatics](../energy/pneumatics.md) | — |

## Construction Steps

### Heating System

1. **Build heater mounting frame**: Weld a rectangular frame from steel angle (40 × 40 × 3 mm) sized to the maximum sheet dimension plus 100 mm margin on each side. For a 600 × 600 mm forming area, the heater frame is approximately 800 × 800 mm. Mount the frame on pivoting hinges at the back so it can swing over the forming table for heating and swing away for mold access.

2. **Install infrared heaters**: Mount quartz infrared heaters (tubular, 500-2000 W each) across the frame at 80-120 mm spacing. Wire heaters in parallel circuits with individual switches or a single PID controller. Heater density: 2-5 W/cm² of sheet area for adequate heating rate. Position heaters 100-200 mm above the sheet surface (adjustable height for different sheet thicknesses).

3. **Install temperature monitoring**: Mount a non-contact IR pyrometer aimed at the sheet surface, or install a surface thermocouple that contacts the sheet during heating. Connect to a display or controller. Sheet temperature is the primary process variable — overheating degrades polymer, underheating prevents forming.

### Clamp Frame

4. **Build clamp frame**: Weld two rectangular frames from steel angle, sized to sandwich the thermoplastic sheet at its edges. The lower frame bolts to the vacuum platen; the upper frame clamps down on the sheet. Frame width: 25-40 mm contact area on each side of the sheet.

5. **Install vacuum seal groove**: Mill a groove (6-8 mm wide × 4-6 mm deep) in the lower clamp frame face. Press a silicone rubber gasket cord into the groove — this seal prevents vacuum leakage at the clamp edges.

6. **Install clamp mechanisms**: Mount toggle clamps at 100-200 mm intervals along the clamp frame perimeter. Each clamp provides 500-2000 N clamping force. The clamps must seal the gasket evenly around the full perimeter — uneven clamping causes vacuum leaks at the corners.

### Vacuum Platen and System

7. **Prepare vacuum platen**: Mill the vacuum platen surface flat within 0.1 mm. Drill a grid of vacuum distribution holes (3-5 mm diameter) through the platen at 30-50 mm spacing. These holes connect the mold surface to a vacuum chamber (plenum) below the platen. Connect the plenum to the vacuum pump via a hose fitting.

8. **Install vacuum pump and receiver**: Mount the vacuum pump near the forming table. Connect pump inlet to the vacuum receiver tank (20-100 L). Connect tank outlet to the vacuum platen via a solenoid valve and hose. The receiver tank provides instant vacuum when the valve opens — the pump alone has insufficient flow for rapid forming.

9. **Wire vacuum valve**: Connect the solenoid vacuum valve to a control circuit. For manual operation: a push-button or foot-switch opens the valve. For automatic cycling: the valve opens after a timed heating period. Include a vacuum gauge in the line between valve and platen for process monitoring.

### Mold Preparation

10. **Drill vacuum holes in mold**: For a wooden mold: drill 0.5-1.0 mm holes through the mold at 15-30 mm spacing in the deepest areas (corners, draw surfaces) and 30-50 mm spacing on flat areas. The holes connect the mold cavity surface to the vacuum plenum below. For tight-tolerance parts: use 0.5 mm holes to minimize visible marks on the formed part. Countersink holes slightly on the cavity side to prevent snagging the sheet.

11. **Mount mold on platen**: Place the mold on the vacuum platen, aligned with the vacuum distribution holes. Seal the mold base to the platen with a gasket or silicone caulk to prevent vacuum bypass around the mold edges. Secure with clamps or bolts.

### Pressure Forming (Optional Upgrade)

12. **Build pressure box**: Weld a box from 5-10 mm steel plate, sized to fit over the clamp frame and seal against it. The box encloses the space above the heated sheet. Install an air inlet with a solenoid valve and pressure regulator. Install a silicone gasket on the box rim to seal against the clamp frame. The box must withstand 0.7 MPa internal pressure — weld seams must be full-penetration and pressure-tested to 1.05 MPa.

## Calibration and Verification

1. **Vacuum system test**: Close the clamp frame on a flat sheet of scrap plastic (no mold). Open the vacuum valve. Verify the vacuum gauge reaches -0.80 to -0.95 bar within 2-3 seconds. If vacuum is insufficient: check gasket seal, hose connections, and pump oil level. A slow vacuum response produces poor forming — the sheet cools before full draw.

2. **Heating uniformity test**: Place a sheet of thermoplastic (PS recommended for visibility) in the clamp frame. Heat for the standard cycle time. Observe the sheet surface: uniform sag indicates even heating. Localized premature sag or discoloration indicates a hot spot — adjust heater spacing or power.

3. **Forming test — shallow draw**: Heat a 1 mm PS sheet to 110-120°C (just above Tg of ~100°C). Vacuum form over a simple rectangular mold (draw ratio 0.3:1). Inspect for: complete forming (sheet contacts all mold surfaces), uniform wall thickness (no excessive thinning at corners), visible vacuum hole marks (if marks are unacceptable, reduce hole size to 0.5 mm).

4. **Pressure forming test** (if equipped): Heat sheet to forming temperature. Apply vacuum below and 0.3 MPa air pressure above simultaneously. Compare surface detail to vacuum-only test — pressure forming should reproduce sharper mold detail.

## Expected Performance

| Parameter | Value |
|-----------|-------|
| Maximum sheet size | 300 × 300 mm to 1500 × 3000 mm (machine-dependent) |
| Sheet thickness range | 0.2-12 mm |
| Heating time | 15-120 seconds (thickness and material dependent) |
| Forming cycle time | 1-5 minutes (heat + form + cool + unload) |
| Draw ratio (vacuum only) | Up to 0.5:1 |
| Draw ratio (with plug assist) | Up to 1.0:1 |
| Draw ratio (pressure forming) | Up to 1.5:1 |
| Forming vacuum level | -0.80 to -0.95 bar |
| Forming pressure (pressure forming) | 0.3-0.7 MPa |
| Forming temperature (PS) | 110-130°C |
| Forming temperature (PE) | 110-130°C |
| Forming temperature (PVC) | 80-100°C |
| Forming temperature (ABS) | 130-160°C |
| Wall thickness variation | ±20-40% (draw-dependent; corners thin most) |
| Mold cost (wood) | $10-100 |
| Mold cost (aluminum) | $500-5,000 |
| Production rate | 10-60 parts/hour (manual) |

## Strengths

- Lowest tooling cost — wooden molds cost $10-100; aluminum production molds cost $500-5,000 (vs. $10,000-100,000+ for injection molds)
- Handles very large parts — thermoforming can produce parts up to 3 m × 6 m or larger (boat hulls, signs, panels) that are impossible to injection-mold
- Fast prototyping — a new mold can be carved from wood in hours and tested the same day
- Low machine cost — a basic vacuum former can be built for a fraction of an injection molder's cost
- Easy material changeover — switch sheet material by changing the roll or stack; no screw purge needed

## Weaknesses

- Limited to open-top, thin-wall shapes — cannot form closed containers, undercuts, or parts with re-entrant angles
- Wall thickness variation — corners and deep draws thin excessively (up to 70% thinning at corners of deep draws); process is less precise than injection molding
- Sheet material cost — thermoforming starts from extruded sheet, which adds an extrusion step and cost vs. direct pellet-to-part injection molding
- Trim waste — 10-30% of the sheet becomes scrap (trim between parts); scrap can be reground and re-extruded
- Slow cycle for thick sheets — heating time scales with sheet thickness²; a 6 mm sheet takes 4× longer to heat than a 3 mm sheet

## Variations and Alternatives

- **Vacuum forming vs. pressure forming**: Vacuum forming is simpler (no pressure box) and adequate for shallow-draw parts with modest detail. Pressure forming adds compressed air above the sheet for deeper draws, sharper detail, and better material distribution. Build vacuum forming first; add the pressure box when part requirements demand it.
- **Plug assist**: A shaped plug (wood, aluminum, or high-temperature foam) mounted on a pneumatic cylinder pre-stretches the heated sheet into the mold before vacuum is applied. Plug assist dramatically improves wall thickness uniformity on deep-draw parts. The plug is typically heated to 60-80°C to prevent chilling the sheet on contact.
- **Drape forming (male mold)**: The sheet is draped over a raised mold (male) rather than sucked into a cavity (female). Male molds produce parts with the best surface finish on the inside (mold-contact side). Female molds produce best finish on the outside.
- **Twin-sheet forming**: Two heated sheets are simultaneously formed between two molds and fused together at the edges. Produces hollow structural parts (panels, ducts). Requires synchronized clamp frames and precise timing.

## Safety

- **Hot sheet burns**: Heated thermoplastic sheets at 100-160°C cause thermal burns on contact. The sheet looks the same hot or cold — always verify temperature before touching. Use heat-resistant gloves when handling heated sheets.
- **Heater radiation**: Infrared heaters produce intense radiant heat. Do not look directly at energized quartz heaters (eye damage risk). Guard the heater frame to prevent accidental contact.
- **Vacuum implosion**: The vacuum platen and receiver tank experience external atmospheric pressure when evacuated. Ensure all vessels are rated for full vacuum. Inspect for dents, cracks, or corrosion that could cause implosion.
- **Pressure box** (if equipped): The pressure box contains compressed air at 0.3-0.7 MPa. Pressure-test the box to 1.05 MPa before first use. Install a pressure relief valve set to 0.8 MPa. Never open the box while pressurized.
- **Pinch points**: The clamp frame and toggle clamps create pinch points. Keep hands clear when closing clamps.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Incomplete forming (sheet doesn't contact mold) | Sheet too cold; insufficient vacuum | Increase heating time or temperature; verify vacuum level reaches -0.80 bar; check for vacuum leaks at gasket and mold seal |
| Excessive thinning at corners | Draw ratio too high; sheet too thin for draw depth | Add plug assist to pre-distribute material; increase initial sheet thickness; reduce draw depth by redesigning part |
| Webbing (wrinkles between formed features) | Too much material for the draw; sheet overheated | Reduce heating temperature; add plug assist; increase distance between adjacent deep features in mold design |
| Vacuum hole marks visible on part | Vacuum holes too large; sheet too hot | Reduce hole diameter to 0.5 mm; reduce forming temperature 5-10°C; use vacuum grooves instead of holes on cosmetic surfaces |
| Sheet tears during forming | Sheet too cold; draw too deep; material too thin | Increase forming temperature; reduce draw ratio; increase sheet thickness; check material for contamination or degradation |
| Blistering or bubbles in sheet | Moisture in sheet (especially PET, nylon) | Pre-dry sheet at 80°C for 2-4 hours before forming; store hygroscopic materials in sealed containers |

## See Also

- [Extruder](extruder.md) — produces the thermoplastic sheet used as thermoforming input
- [Injection Molding Machine](injection-molding-machine.md) — higher-precision alternative for smaller, complex parts
- [Blow Molding Equipment](blow-molding-equipment.md) — for hollow parts (bottles, containers)
- [Compression Press](compression-press.md) — for thermoset parts that cannot be thermoformed
- [Thermoplastics](../polymers/thermoplastics.md) — polymer-specific thermoforming temperatures and parameters
- [Pneumatics](../energy/pneumatics.md) — vacuum pump and compressed air system design

[← Back to Machine Tools](index.md)
