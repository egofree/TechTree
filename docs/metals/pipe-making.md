# Pipe and Tube Manufacturing

> **Node ID**: metals.pipe-making
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Water Distribution`](distribution.md), [`Gas Handling`](gas-handling.md)
> **Enables**: [`Metal Casting`](casting.md)
> **Timeline**: Years 15-30
> **Outputs**: metal-pipes, steel-tubes, cast-iron-pipes
> **Critical**: No

## Overview

Manufacture of metal pipes and tubes by casting, extrusion, seamless piercing, or welding. Pipes are essential infrastructure for water distribution, gas handling, steam transport, and chemical processing. Each pipe material and process serves different applications: cast iron for water and drainage, seamless steel for high-pressure steam and structural use, welded steel for moderate-pressure fluids, and copper tube for domestic water and heat exchangers.

The choice of pipe-making method depends on the material, diameter, wall thickness, and pressure rating required. Cast iron pipes are made by centrifugal casting, where molten iron is poured into a spinning mold that distributes the metal evenly against the mold wall. Steel pipes are either seamless (pierced from a solid billet and elongated on a rolling mill) or welded (formed from flat strip and seam-welded). Copper tubes are made by extrusion followed by cold drawing.

For bootstrapping purposes, centrifugal cast iron pipe is the simplest starting point. The equipment (a spinning mold and a ladle) is far less complex than a seamless piercing mill. Cast iron pipes serve municipal water distribution, building drainage, and low-pressure gas service. Steel pipe production can follow once the rolling mill infrastructure is established.

Primary outputs: `metal-pipes`, `steel-tubes`, `cast-iron-pipes`.

## Prerequisites

### Materials

- Cast iron (for centrifugal casting of water and drainage pipes)
- Steel billets or strip (for seamless or welded steel pipe)
- Copper billets (for copper tube production)
- Clay (for ceramic pipes used in drainage and chemical service)
- Welding consumables (for welded pipe: ERW electrodes, SAW flux and wire)
- Zinc for galvanizing steel pipe (optional, for corrosion protection)
- Refractory wash coatings for centrifugal casting molds

### Equipment

- [Water Distribution](distribution.md) — material dependency
- [Gas Handling](gas-handling.md) — material dependency
- Centrifugal casting machine with spinning mold (for cast iron pipe)
- Piercing mill (for seamless steel pipe: cross-roll piercer or Mannesmann piercer)
- Pilger mill or plug mill (for elongating the pierced shell)
- Sizing mill and straightening machine
- Roll forming stand and welding unit (for welded pipe: ERW or SAW)
- Extrusion press (for copper tube and non-ferrous pipe)
- Drawing bench with dies and mandrels for copper tube drawing
- Mandrels and dies for drawing and sizing
- Hydrostatic testing equipment
- Cutting and facing equipment (saw, torch, or rotary cutter)
- Crane and handling equipment for heavy pipe

### Knowledge

- Understanding of centrifugal casting: mold rotation speed, pouring temperature, coating the mold with a refractory wash
- Seamless pipe piercing: how the Mannesmann effect creates a cavity in the billet center when rotated between angled rolls
- Pipe rolling: controlling wall thickness and diameter through roll gap, mandrel position, and pass schedule
- Welded pipe forming: strip edge preparation, roll forming geometry, welding parameters (current, voltage, speed)
- Heat treatment of welded pipe: normalizing the weld zone to restore grain structure
- Hydrostatic testing: pressure calculation based on material grade and wall thickness

### Infrastructure

- Furnace for heating billets (for seamless pipe) or melting iron (for centrifugal casting)
- Casting area with mold preparation, coating, and handling
- Rolling mill floor with roll forming stands, mandrel extraction, and sizing
- Welding station with power supply, cooling, and bead control (for welded pipe)
- Hydrostatic test station with high-pressure pump, end seals, and pressure gauges
- Cooling bed or rack for straightening and cooling finished pipe
- Handling and storage area organized by pipe size, schedule, and material grade
- Galvanizing line (if producing galvanized steel pipe): molten zinc kettle at ~450°C, fluxing station, and cooling rack

## Process Description

### Cast Iron Pipe (Centrifugal Casting)

1. Preheat and coat the water-cooled metal mold with a thin refractory wash (silica or zirconia). The coating controls the casting surface finish and protects the mold from thermal shock.
2. Spin the mold to the target rotation speed (typical: 500-1000 RPM depending on pipe diameter). Centrifugal force must be sufficient to hold the molten iron against the mold wall.
3. Pour molten cast iron into the spinning mold through a trough or runner. The metal flows along the mold length, and centrifugal force distributes it evenly against the wall. The pour rate controls wall thickness.
4. Allow the iron to solidify while the mold continues to spin. The centrifugal force drives denser metal outward and lighter slag and gas inclusions inward, where they can be machined off or remain on the inner surface.
5. Stop the mold and extract the pipe. The pipe shrinks slightly on cooling and releases from the mold. Cool on a rack.
6. Machine the socket (bell) end and spigot end to specification. The bell-and-spigot joint is the standard connection method for cast iron water pipe: the spigot end of one pipe slides into the bell (socket) end of the next, sealed with lead, rubber gasket, or cement mortar. Test hydrostatically.

### Seamless Steel Pipe (Piercing and Rolling)

1. Heat a round steel billet to 1200-1280°C in a reheating furnace. The billet must be uniformly heated through its cross-section.
2. Pierce the billet in the Mannesmann piercer. The heated billet is fed between two large, angled rolls that rotate it and force it over a pointed mandrel. The combination of tensile stress at the billet center (the Mannesmann effect) and the mandrel point creates a hollow shell.
3. Elongate the pierced shell on a pilger mill or plug mill. The shell is rolled between dies that reduce the wall thickness and increase the length. The mandrel inside the shell controls the inner diameter.
4. Pass the rough pipe through a sizing mill to bring the outside diameter to specification. Multiple stands of rolls progressively size the pipe.
5. Reheat and pass through a straightening machine if needed. Cold-draw through a die and over a mandrel for closer dimensional tolerance if required.
6. Cut to length, face the ends, test hydrostatically, and inspect.

### Welded Steel Pipe (ERW or SAW)

1. Uncoil flat steel strip and feed into a roll forming line. A series of contoured rolls progressively form the flat strip into a round tube shape.
2. Bring the strip edges together at the welding station. For ERW (Electric Resistance Welding), copper contacts apply high-frequency current to the edges. The current heats the edges to welding temperature, and squeeze rolls force them together. For SAW (Submerged Arc Welding), a continuous wire electrode and granular flux deposit a weld bead along the seam.
3. Remove the internal and external weld bead flash (for ERW) by cutting or scarfing.
4. Normalize the weld zone by induction heating to refine the grain structure disturbed by welding. This step is essential for ERW pipe that will serve in pressure applications. Without normalizing, the weld zone has a different microstructure from the parent metal, creating a weak point.
5. Size and straighten the pipe in a sizing mill. Cut to length and test hydrostatically.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Cast iron pouring temperature | 1300-1400°C | Must be fully liquid; too cold causes misruns |
| Centrifugal mold speed | 500-1000 RPM | Higher speed for larger diameters; must overcome gravity |
| Billet heating temperature (seamless) | 1200-1280°C | Uniform heating required; cold spots cause piercing failure |
| Pilger mill reduction | 60-80% wall reduction | Controls final wall thickness |
| ERW welding frequency | 100-400 kHz | Higher frequency concentrates heat at the strip edges |
| ERW welding speed | 10-60 m/min | Faster for thin-wall, smaller diameter |
| Hydrostatic test pressure | 1.5x to 2x working pressure | Per applicable code; hold for specified time, check for leaks |

Pipe sizes are designated by nominal diameter and schedule (wall thickness). A 6-inch Schedule 40 pipe, for example, has a nominal bore of 150 mm and a wall thickness of approximately 7 mm. The schedule number determines the pressure rating. Heavier schedules (80, 120, 160) have thicker walls and higher pressure ratings. The pipe-making process must control wall thickness to within the specified tolerance for the schedule being produced.

## Safety Considerations

- **Molten metal**: Cast iron pouring in centrifugal casting involves molten metal at 1300-1400°C. Spillage causes severe burns. Moisture in the mold causes violent steam explosions. Preheat molds and keep them dry.
- **Pinch points**: Rolling mills, pilger mills, and roll forming stands have powerful rotating rolls. Clothing, hands, and tools caught in the rolls cause crushing and amputation injuries. Never reach into a running mill.
- **Heavy pipe handling**: Finished pipe is heavy and awkward to handle manually. Use cranes, slings, and pipe hooks. Rolls of pipe in storage yards can crush workers if not blocked and stacked properly.
- **Radiation and sparks from welding**: ERW and SAW produce intense UV radiation, sparks, and spatter. Burns to skin and eyes (arc flash or welder's flash) are hazards.
- **Noise**: Rolling mills and cutting equipment produce high noise levels. Hearing protection is mandatory.

### Personal Protective Equipment

- Safety glasses with side shields at all times
- Face shield and heat-resistant gloves when working near molten iron or hot pipe
- Hearing protection in the rolling mill and cutting areas
- Steel-toe boots with metatarsal protection
- Welding helmet with appropriate shade lens when observing or performing welding operations
- Long sleeves and leather apron when handling freshly cast or freshly welded pipe

### Emergency Procedures

- For molten metal splash: cool the burn under running water for at least 20 minutes. Do not remove adhered metal. Seek medical attention.
- For caught clothing in a mill: hit the emergency stop immediately. Do not reach toward the rolls. Cut the clothing to free the worker if needed.
- For arc flash eye injury: move the affected person away from the welding area, apply cold compresses, and seek medical attention. Do not rub the eyes.
- Keep fire extinguishers at all welding stations and near the casting area.

## Quality Control

### Acceptance Criteria

- **Cast Iron Pipes**: Wall thickness within specified tolerance. Socket and spigot dimensions gauge correctly. No cracks, porosity, or cold shuts visible on inner or outer surface. Hydrostatic test passed at required pressure.
- **Steel Tubes (Seamless)**: Outside diameter, wall thickness, and ovality within tolerance. No internal laps, seams, or cracks. Hydrostatic test passed. Material grade verified (tensile strength, yield strength, elongation).
- **Welded Steel Pipes**: Weld bead smooth and full-penetration. No undercut, porosity, or incomplete fusion. Weld zone normalized. Hydrostatic test passed.

### Testing Methods

- **Hydrostatic testing**: Seal both ends of the pipe, fill with water, pressurize to 1.5-2x the rated working pressure, and hold for a specified time. Watch for pressure drop (leaks) and visual seepage. This is the primary acceptance test for pressure-containing pipe.
- **Wall thickness measurement**: Ultrasonic thickness gauge or mechanical micrometer. Measure at multiple points around the circumference and along the length. Wall thickness must not fall below the minimum specified for the pipe schedule.
- **Diameter and ovality**: Measure outside diameter with a pi tape or caliper at several points. Ovality (difference between maximum and minimum diameter at any cross-section) must be within tolerance.
- **Visual inspection**: Check inner and outer surfaces for cracks, laps, pits, rolled-in scale, and weld defects. Use a borescope or light for internal inspection of small diameter pipe.
- **Weld inspection (for welded pipe)**: Radiographic or ultrasonic examination of the weld seam if required by specification. Check for incomplete fusion, porosity, and slag inclusions.

### Sampling Protocol

- Hydrostatic test every pipe (100% testing is standard for pressure pipe)
- Measure wall thickness on every pipe at multiple points
- Visual inspect 100% of pipes inside and outside
- Destructive testing (tensile, flatten, bend) on sample pipes per heat lot
- Track dimensional data by batch for trend analysis and mill calibration

## Scaling Notes

- **Foundry scale**: Single centrifugal casting machine, manual pouring. Cast iron pipes in limited diameters. Tens to hundreds of pipes per day depending on size. This is the bootstrapping entry point for pipe production.
- **Pipe mill (seamless)**: Piercing mill, pilger mill, sizing mill, straightener, and test station in a line. Requires significant capital equipment and power. Hundreds of tonnes of pipe per month.
- **Pipe mill (welded)**: Uncoiler, roll forming line, welder, sizing, cutting, and testing. More flexible than seamless for different diameters. Can be built incrementally starting with ERW for smaller diameters.

Key scaling challenges: the piercing mill for seamless pipe is a massive, precision machine that requires heavy foundations and significant power. Welded pipe lines are more modular and can be scaled up incrementally. Centrifugal casting is relatively simple to set up but limited to cast iron and non-ferrous metals. Handling and straightening long, heavy pipes requires overhead cranes and adequate floor space.

Copper tube production (extrusion and drawing) is a smaller-scale operation that can coexist with the other pipe-making processes. A hydraulic extrusion press forces a heated copper billet through a die with a mandrel, producing a tube shell. The shell is then cold-drawn through dies and over mandrels to final dimensions, using equipment similar to wire drawing but with internal tooling.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Ovality (out-of-round pipe) | Uneven cooling, worn rolls, incorrect roll gap | Check and adjust roll gap; ensure uniform cooling; replace worn rolls |
| Wall thickness variation | Eccentric mandrel, uneven billet heating, worn tooling | Re-center mandrel; ensure billet is uniformly heated; inspect and replace worn dies |
| Inner surface defects (laps, seams) | Excessive oxidation during piercing, dirty mandrel surface | Control furnace atmosphere; clean mandrel between passes; reduce dwell time at temperature |
| Weld defects (porosity, incomplete fusion) | Insufficient heat, dirty strip edges, wrong welding speed | Increase weld current; clean strip edges; adjust welding speed |
| Cracking during hydro test | Pre-existing crack from casting or rolling defect | Inspect more carefully before testing; improve casting or rolling parameters |
| Pipe not straight | Uneven cooling, worn straightener rolls, bent mandrel | Adjust straightener rolls; cool pipe evenly on a flat bed; inspect mandrel for wear |

## Variations and Alternatives

- **Centrifugal casting**: Best for cast iron water and drainage pipe. Simple equipment, good surface quality. Limited to materials that can be cast.
- **Seamless piercing and rolling**: Best for high-pressure and high-temperature applications. No weld seam to fail. Expensive equipment, limited diameter range per mill setup.
- **ERW (Electric Resistance Welding)**: Best for medium-diameter steel pipe (20-600 mm). Fast, continuous production. Weld quality requires good strip preparation and controlled parameters.
- **SAW (Submerged Arc Welding)**: Best for large-diameter pipe (400-1600 mm). High deposition rate, deep penetration. Typically used for spiral-welded or straight-seam large pipe.
- **Extrusion and drawing**: Best for copper tube and non-ferrous pipe. Produces smooth, close-tolerance tube. Extrusion press is the main capital item.
- **Clay pipe extrusion and firing**: For drainage and chemical service where metal is not needed. Low-tech alternative that requires a clay extruder and kiln rather than metalworking equipment.
- **Copper tube (extrusion and drawing)**: Extrude a copper billet through a die to form a tube shell, then cold-draw through dies and over mandrels to final size. Produces smooth, close-tolerance tube for domestic water, refrigeration, and heat exchangers. Requires an extrusion press and drawing bench.

Pipe ends are prepared according to the joining method. Cast iron pipes use bell-and-spigot joints. Steel pipes may be beveled for welding, threaded for screw fittings, or grooved for mechanical couplings. Copper tubes use soldered, brazed, or press-fit joints. The end preparation step is part of the finishing line and must match the specification for the intended installation method.

## References

- [Metals](metals.md) — parent capability
- [Metals Domain](./index.md) — domain overview and related capabilities
- [Water Distribution](distribution.md) — upstream dependency (material)
- [Gas Handling](gas-handling.md) — upstream dependency (material)
- [Metal Casting](casting.md) — downstream capability

---
*Part of the [Bootciv Tech Tree](../index.md) · [Metals](./index.md) · [All Domains](../index.md)*