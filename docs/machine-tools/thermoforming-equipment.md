# Thermoforming Equipment

> **Node ID**: machine-tools.thermoforming-equipment
> **Domain**: [Machine Tools](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`energy.index`](../energy/index.md), [`energy.electric-motor`](../energy/electric-motor.md)
> **Enables**: [`polymers.thermoplastics`](../polymers/thermoplastics.md), [`chemistry.packaging-testing`](../chemistry/packaging-testing.md)
> **Timeline**: Years 15-22
> **Outputs**: formed_trays, containers, panels, signs, boat_hulls, enclosures
> **Critical**: No — injection molding and compression molding can produce most thermoformed shapes, but thermoforming has much lower tooling cost and handles large parts impractical to injection-mold

## Overview

Thermoforming heats a flat thermoplastic sheet to its softening temperature (just above Tg for amorphous polymers, just above melting point for semi-crystalline), then stretches it over or into a mold using vacuum, compressed air, or mechanical force. The sheet cools against the mold surface, retaining the molded shape. The process is limited to thin-wall, open-top shapes (trays, containers, panels, housings) but offers the lowest tooling cost of any plastic forming method: wooden molds cost $10-100, aluminum production molds cost $500-5,000.

Two main methods exist: **vacuum forming** (atmospheric pressure at 0.1 MPa pushes softened sheet onto mold through vacuum holes) and **pressure forming** (compressed air at 0.3-0.7 MPa above the sheet plus vacuum below, producing sharper detail and deeper draws). A plug assist pre-stretches the sheet before vacuum/pressure application for more uniform wall thickness on deep-draw parts.

Thermoforming handles parts up to 3 m × 6 m or larger (boat hulls, signs, panels) that are impossible to injection-mold. It starts from extruded sheet produced by the [extruder](extruder.md). For smaller, complex parts with tight tolerances, [injection molding](injection-molding-machine.md) is the better choice. For hollow closed containers, [blow molding](blow-molding-equipment.md) is required.

The forming force is limited to atmospheric pressure (0.1 MPa for vacuum forming) or the supply pressure (0.3-0.7 MPa for pressure forming). This is orders of magnitude lower than injection molding pressures (50-200 MPa). The low pressure enables the use of inexpensive molds — hardwood, cast aluminum, or epoxy — rather than the hardened tool steel molds required for injection molding. A hardwood mold for a thermoformed tray costs days of carpentry work; an equivalent injection mold costs weeks of precision machining.

Material utilization in thermoforming is inherently lower than injection molding. The sheet area outside the part (the "web" between formed parts) is trimmed and discarded or reground. Typical material utilization is 60-80% of the sheet area. This waste is the primary economic disadvantage of thermoforming versus injection molding, which wastes only the runner system (15-30%). However, the lower mold cost and faster time-to-production make thermoforming the preferred method for large parts and short-to-medium production runs.

Thermoforming requires thermoplastic sheet — most commonly HIPS (high-impact polystyrene), ABS, HDPE, or PVC. The sheet must be produced by the [extruder](extruder.md) in the correct thickness (0.2-12 mm) and cut to size before forming. Sheet quality directly affects part quality: variations in sheet thickness >±5% produce uneven wall thickness in the formed part.

## Prerequisites

- [Steel plate and sheet](../metals/iron-steel.md) — for frame, clamp, and pressure box
- [Vacuum pump](../energy/index.md) — capable of 0.8-0.95 bar negative pressure
- [Compressed air supply](../energy/index.md) — 0.3-0.7 MPa for pressure forming
- [Electric heating elements](../energy/electric-furnaces.md) — infrared heaters or oven elements
- [Temperature controller](../electronics/electrical-systems.md) — for heater regulation
- [Thermoplastic sheet](../polymers/thermoplastics.md) — produced by the extruder

## Bill of Materials

### Heating System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Infrared heaters (quartz or ceramic) | 4-12 | 500-2000 W each, 220 V, with reflectors | [Electric Furnaces](../energy/electric-furnaces.md) | Cal-rod elements in reflector housing |
| Heater mounting frame | 1 | Steel angle or channel, sized to sheet + 100 mm margin | [Iron & Steel](../metals/iron-steel.md) | Aluminum extrusion (lighter, less rigid) |
| Thermocouple or pyrometer | 1 | Type K, 0-300°C, or non-contact IR pyrometer | [Measurement](../measurement/precision-metrology.md) | Surface thermometer (slower) |

### Forming Table and Clamp Frame

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Steel plate (vacuum platen) | 1 | 10-15 mm thick, machined flat, sized to max sheet | [Iron & Steel](../metals/iron-steel.md) | Cast aluminum platen |
| Steel angle (clamp frame) | 4-8 m | 40-50 mm angle, 3-5 mm thick | [Iron & Steel](../metals/iron-steel.md) | Aluminum angle (flexes under clamp force) |
| Clamp mechanism | 4-8 | Toggle clamps or pneumatic cylinders, 500-2000 N each | [Machine Tools](./index.md) | C-clamps (slow, manual) |
| Vacuum seal gasket | 4-8 m | Silicone rubber cord, 6-10 mm diameter | [Elastomers](../polymers/rubber.md) | Foam weatherstrip (short life) |

### Vacuum System

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Vacuum pump | 1 | Rotary vane or piston, 5-25 m³/hour, to 0.1 mbar | [Energy Systems](../energy/index.md) | Venturi vacuum generator |
| Vacuum receiver tank | 1 | 20-100 L, rated to full vacuum, with drain | [Reactor Vessel](../chemistry/reactor-vessel.md) | Direct pump connection (slower response) |
| Vacuum gauge | 1 | 0 to -1.0 bar | [Measurement](../measurement/precision-metrology.md) | Needed for vacuum verification |
| Solenoid valve | 1 | 2-way NC, 12-24 VDC | [Energy Systems](../energy/index.md) | Manual ball valve (slower cycle) |
| Vacuum hose | 2-5 m | Reinforced rubber, 25-40 mm ID, full vacuum rated | [Elastomers](../polymers/rubber.md) | PVC tubing (collapses under vacuum) |

### Mold

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Wood (prototype) | Variable | Hardwood (maple, birch), sealed with shellac or epoxy | [Wood](../foundations/tools-basic.md) | Cast plaster (fragile) |
| Aluminum (production) | Variable | 6061-T6, machined or cast to part profile | [Non-Ferrous Metals](../metals/non-ferrous.md) | Epoxy cast (intermediate durability) |

## Process Description

### Heating System

1. **Build heater mounting frame**: Weld a rectangular frame from steel angle (40 × 40 × 3 mm) sized to maximum sheet + 100 mm margin each side. For a 600 × 600 mm forming area: ~800 × 800 mm frame. Mount on pivoting hinges so it swings over the forming table for heating and away for mold access.
2. **Install infrared heaters**: Mount quartz infrared heaters across the frame at 80-120 mm spacing. Wire in parallel circuits with individual switches or PID controller. Heater density: 2-5 W/cm² of sheet area. Position 100-200 mm above sheet surface (adjustable).
3. **Install temperature monitoring**: Mount a non-contact IR pyrometer aimed at the sheet surface, or install a surface thermocouple. Sheet temperature is the primary process variable — overheating degrades polymer, underheating prevents forming.

**Calibration**: Heat a scrap PS sheet for the standard cycle. Observe uniformity of sag — uniform sag indicates even heating. Localized premature sag indicates a hot spot.

**Expected performance**: Heating time: 15-120 seconds (thickness dependent). Temperature range: 80-200°C.

### Clamp Frame and Vacuum Platen

4. **Build clamp frame**: Weld two rectangular frames from steel angle, sized to sandwich the sheet at its edges. Lower frame bolts to vacuum platen; upper frame clamps down on sheet. Frame width: 25-40 mm contact area per side.
5. **Install vacuum seal groove**: Mill a groove (6-8 mm wide × 4-6 mm deep) in the lower clamp frame face. Press silicone rubber gasket cord into the groove.
6. **Install clamp mechanisms**: Mount toggle clamps at 100-200 mm intervals along the perimeter. Each provides 500-2000 N clamping force. Clamps must seal gasket evenly — uneven clamping causes vacuum leaks at corners.
7. **Prepare vacuum platen**: Mill surface flat within 0.1 mm. Drill a grid of vacuum distribution holes (3-5 mm) at 30-50 mm spacing connecting to a vacuum plenum below. Connect plenum to vacuum pump via solenoid valve and hose.
8. **Install vacuum pump and receiver**: Mount pump near the forming table. Connect pump inlet to receiver tank (20-100 L). Connect tank to vacuum platen via solenoid valve. The receiver provides instant vacuum when the valve opens.

**Calibration**: Close clamp frame on scrap plastic (no mold). Open vacuum valve. Gauge must reach -0.80 to -0.95 bar within 2-3 seconds. Slow vacuum response produces poor forming — the sheet cools before full draw.

**Expected performance**: Vacuum level: -0.80 to -0.95 bar. Response time: <3 seconds. Clamp force: 500-2000 N per clamp.

### Mold Preparation

9. **Drill vacuum holes in mold**: For wooden molds: drill 0.5-1.0 mm holes at 15-30 mm spacing in deep areas and 30-50 mm on flats. Holes connect cavity surface to vacuum plenum below. Countersink slightly on cavity side to prevent snagging.
10. **Mount mold on platen**: Place mold on vacuum platen, aligned with distribution holes. Seal mold base to platen with gasket or silicone caulk. Secure with clamps or bolts.

**Calibration**: Close empty mold on carbon paper at parting line — imprint must show uniform contact. Test a vacuum-only pull: verify the sheet contacts all mold surfaces.

**Expected performance**: Vacuum hole diameter: 0.5-1.0 mm. Hole spacing: 15-50 mm depending on draw depth.

### Pressure Forming (Optional Upgrade)

11. **Build pressure box**: Weld a box from 5-10 mm steel plate sized to fit over the clamp frame. Install air inlet with solenoid valve and pressure regulator. Install silicone gasket on box rim. Pressure-test to 1.05 MPa before first use.

**Calibration**: Verify box seals against clamp frame with no air leakage at 0.7 MPa. Install pressure relief valve set to 0.8 MPa.

**Expected performance**: Forming pressure: 0.3-0.7 MPa. Detail reproduction: approaches injection molding quality.

## Quantitative Parameters

### Machine Specifications

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
| Wall thickness variation | ±20-40% (draw-dependent) |
| Production rate | 10-60 parts/hour (manual) |

### Forming Temperatures by Polymer

| Polymer | Glass Transition / Melting Point | Forming Temperature | Notes |
|---------|----------------------------------|---------------------|-------|
| PS (polystyrene) | Tg ~100°C | 110-130°C | Most forgiving material for testing |
| HDPE | Tm ~130°C | 135-155°C | High shrinkage on cooling |
| LDPE | Tm ~110°C | 110-130°C | Good draw, low stiffness |
| PP (polypropylene) | Tm ~165°C | 155-175°C | Narrow forming temperature range |
| PVC (rigid) | Tg ~80°C | 80-100°C | Forms at low temperature; HCl release if overheated |
| ABS | Tg ~105°C | 130-160°C | Good detail reproduction |
| PET (amorphous) | Tg ~75°C | 95-120°C | Must be dried before forming |

### Vacuum System Performance Requirements

| Sheet Size | Minimum Pump Capacity | Receiver Tank | Vacuum Level | Response Time |
|-----------|----------------------|---------------|-------------|---------------|
| 300 × 300 mm | 5 m³/hour | 20 L | -0.80 bar | <2 s |
| 600 × 600 mm | 15 m³/hour | 50 L | -0.85 bar | <3 s |
| 1000 × 1000 mm | 30 m³/hour | 100 L | -0.90 bar | <3 s |
| 1500 × 3000 mm | 60+ m³/hour | 200+ L | -0.90 bar | <4 s |

## Scaling Notes

- A benchtop vacuum former (300 × 300 mm sheet) built from a steel frame, shop vacuum, and ceramic heaters handles prototype and small-batch production. Build this first.
- Scale to 600 × 600 mm for production trays, containers, and enclosures. Requires a dedicated vacuum pump and larger heater array.
- Large-format thermoformers (1500 × 3000 mm) handle boat hulls, vehicle body panels, and architectural signage. These require 20+ kW of heating power and a large vacuum system.
- Twin-sheet forming produces hollow structural parts (panels, ducts) by forming two sheets simultaneously between two molds and fusing at edges. Requires synchronized clamp frames.
- Rotary thermoforming machines (4-8 stations on a carousel) increase throughput to 200+ parts/hour for high-volume packaging production.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Incomplete forming (sheet doesn't contact mold) | Sheet too cold; insufficient vacuum | Increase heating time/temperature; verify vacuum reaches -0.80 bar; check gasket and mold seal for leaks |
| Excessive thinning at corners | Draw ratio too high; sheet too thin for depth | Add plug assist; increase sheet thickness; reduce draw depth |
| Webbing (wrinkles between features) | Too much material; sheet overheated | Reduce heating temperature; add plug assist; increase feature spacing in mold |
| Vacuum hole marks visible on part | Holes too large; sheet too hot | Reduce hole diameter to 0.5 mm; lower forming temperature 5-10°C; use grooves on cosmetic surfaces |
| Sheet tears during forming | Sheet too cold; draw too deep; material too thin | Increase forming temperature; reduce draw ratio; increase sheet thickness |
| Blistering or bubbles | Moisture in sheet (PET, nylon) | Pre-dry sheet at 80°C for 2-4 hours; store hygroscopic materials in sealed containers |
| Incomplete mold detail | Insufficient vacuum or pressure; sheet too cold | Verify vacuum -0.80 bar within 2 s; increase pressure to 0.5-0.7 MPa; raise temperature 5-10°C |
| Part warps after removal | Uneven cooling; residual stress | Increase cooling time; use fixture to constrain shape; ensure uniform mold temperature |
| Sheet sticks to mold | Insufficient draft angle; mold too hot | Increase mold draft to 2-3° minimum; cool mold to 20-30°C; apply mold release spray (silicone-based) |
| Corner thinning exceeds 60% of original | Draw ratio too high; insufficient pre-stretch | Reduce draw depth; add plug assist; increase sheet thickness; use higher-temperature forming for better material flow |

## Safety

- **Hot sheet burns**: Heated thermoplastic sheets at 100-160°C cause thermal burns on contact. The sheet looks the same hot or cold — always verify temperature before touching. Use heat-resistant gloves (rated to 200°C) when handling heated sheets. Molten polymer sticks to skin — cool under running water for 15+ minutes.
- **Heater radiation**: Infrared heaters produce intense radiant heat. Do not look directly at energized quartz heaters (corneal damage risk). Guard the heater frame to prevent accidental contact.
- **Vacuum implosion**: The vacuum platen and receiver tank experience external atmospheric pressure when evacuated. All vessels must be rated for full vacuum. Inspect for dents, cracks, or corrosion. A cracked receiver tank implodes violently.
- **Pressure box** (if equipped): Contains compressed air at 0.3-0.7 MPa. Pressure-test to 1.05 MPa before first use. Install relief valve at 0.8 MPa. Never open the box while pressurized.
- **Pinch points**: Clamp frame and toggle clamps create pinch hazards. Keep hands clear during clamping.

## Quality Control

1. **Wall thickness measurement**: Cut a formed part at the thinnest point (usually a corner). Measure with calipers. Minimum wall thickness: ≥60% of original sheet for shallow draws, ≥30% for deep draws.
2. **Dimensional check**: Measure critical dimensions with calipers. Tolerance: ±1.0 mm (vacuum-formed), ±0.5 mm (pressure-formed).
3. **Visual inspection**: Check every part for blisters, incomplete forming, webbing, and surface blemishes. Reject parts with visible vacuum hole marks on cosmetic surfaces.
4. **Drop test** (for containers): Drop a formed tray from 1 m onto concrete. No cracking or splitting acceptable.
5. **Material utilization**: Track the ratio of formed part area to total sheet area (including clamp waste). Typical utilization: 60-80%. Regrind and re-extrude trim waste for sheet production. Waste above 30% indicates poor nesting layout on the sheet.

## Variations and Alternatives

- **Vacuum forming vs. pressure forming**: Vacuum forming is simpler and adequate for shallow-draw parts. Pressure forming adds compressed air for deeper draws and sharper detail. Build vacuum forming first; add pressure box when part requirements demand it.
- **Plug assist**: A shaped plug (wood, aluminum, or high-temperature foam) pre-stretches the heated sheet into the mold before vacuum is applied. Improves wall thickness uniformity dramatically on deep-draw parts. Plug is heated to 60-80°C to prevent chilling the sheet.
- **Drape forming (male mold)**: Sheet is draped over a raised mold (male) rather than sucked into a cavity (female). Male molds produce best surface finish on the inside; female molds on the outside.
- **Twin-sheet forming**: Two heated sheets formed simultaneously between two molds and fused at edges. Produces hollow structural parts. Requires synchronized clamp frames.
- **Injection molding** ([injection-molding-machine.md](injection-molding-machine.md)): Higher precision for small complex parts. Higher tooling cost. Cannot match thermoforming for large parts.
- **Blow molding** ([blow-molding-equipment.md](blow-molding-equipment.md)): For hollow closed containers (bottles). Thermoforming cannot produce closed hollow shapes.
- Sheet pre-drying: Hygroscopic polymers (PET, nylon, ABS, polycarbonate) absorb moisture from air. When heated rapidly in the thermoformer, trapped moisture expands as steam, producing blisters and surface defects. Pre-dry PET sheet at 80°C for 2-4 hours, nylon at 80°C for 4-6 hours. Non-hygroscopic polymers (HDPE, PP, PS) do not require pre-drying.
- Trim waste management: Thermoforming generates 20-40% trim waste (the sheet area between formed parts). Regrind trim in a [granulator](extruder.md) and re-extrude into new sheet. Regrind content above 25% can affect sheet quality — blend with virgin material. Sharp granulator knives are essential — dull knives produce long strings that jam the extruder feed.
- Mold draft angle: Vertical sidewalls on a thermoformed part must have 1-3° draft (taper) per side to allow part ejection. Zero-draft vertical walls require splitting the mold (increased complexity). Male molds need less draft than female molds because the part shrinks away from the mold surface during cooling.

## References

- [Extruder](extruder.md) — produces the thermoplastic sheet used as thermoforming input
- [Injection Molding Machine](injection-molding-machine.md) — higher-precision alternative for smaller, complex parts
- [Blow Molding Equipment](blow-molding-equipment.md) — for hollow parts (bottles, containers)
- [Compression Press](compression-press.md) — for thermoset parts that cannot be thermoformed
- [Thermoplastics](../polymers/thermoplastics.md) — polymer-specific thermoforming temperatures and parameters
- [Energy Systems](../energy/index.md) — vacuum pump and compressed air system design
- Heating time scales with sheet thickness²: a 6 mm sheet takes 4× longer to heat than 3 mm.

---
*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](./index.md) • [All Domains](../index.md)*

