# Pipe Fabrication

> **Node ID**: water.pipe-fabrication
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`ceramics.pottery`](../ceramics/index.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.sewage`](sewage.md), [`gas-handling.piping-systems`](../gas-handling/piping-systems.md)
> **Timeline**: Years 5-25
> **Outputs**: pipe, tube, fittings
> **Critical**: Yes — sealed pressurized pipe is the enabling technology for water distribution, sewage conveyance, gas transport, steam power, and hydraulic systems

## Overview

![Wester Pipe Fabrication - geograph.org.uk - 2461896](../images/water/water_pipe-fabrication.jpg)

> *Image: Peter Moore, CC BY-SA 2.0*

Pipe and tube are hollow cylinders that convey fluids under pressure or by gravity. They are the enabling technology for [water distribution](distribution.md), [sewage collection](sewage.md), [gas handling](../gas-handling/piping-systems.md), steam power, hydraulic systems, and chemical process piping. Without sealed pressurized pipe, every fluid must be moved in containers — a severe bottleneck that limits settlement size to what can be carried by hand or gravity channels.

The distinction: pipe is sized by nominal bore (approximate inside diameter) with standardized wall thickness schedules, while tube is sized by exact outside diameter with wall thickness specified directly. Pipe is joined by threaded fittings, flanges, or welding. Tube is joined by compression fittings, flared fittings, or brazing.

Pipe fabrication covers four primary material families and their jointing methods:

- **Cast iron pipe**: Molten iron poured into rotating molds (centrifugal casting) or static sand molds. The standard for municipal water and sewage distribution for over 150 years. Pressure rating: 10-40 bar depending on wall thickness class. Service life: 50-100+ years. Jointed with rubber gasket push-on joints or mechanical joint bolts.
- **Steel pipe**: Seamless (drawn from a billet) or welded (rolled from flat plate and seam-welded). Higher pressure capability than cast iron. Used for steam, gas, high-pressure water, and structural applications. Pressure rating: 20-100+ bar depending on wall schedule. Jointed by welding, threading, or bolted flanges.
- **Clay (terracotta) pipe**: Extruded clay fired in a kiln. Low pressure (0.5-2 bar) but excellent chemical resistance and long service life (50+ years). The standard for gravity-flow sewage systems since Roman times. Jointed with rubber gasket or cement mortar.
- **Copper tube**: Seamless copper drawn from billets. Used for domestic water supply, heating, and refrigeration. Pressure rating: 10-50 bar depending on wall type. Jointed by soldering (sweating) or compression fittings.

Jointing methods must match the pipe material and pressure class: cast iron uses bell-and-spigot rubber gaskets; steel uses welding, threading, or flanges; clay uses bell-and-spigot with rubber gasket; copper uses soldering or compression fittings; PVC uses solvent cement or rubber ring joints.

## Prerequisites

- [Iron and steel](../metals/iron-steel.md) for casting and forming pipe bodies
- [Machine tools](../machine-tools/machining.md) — lathe for threading, rollers for forming
- [Welding equipment](../machine-tools/welding-equipment.md) for steel pipe seam welding and joint fabrication
- [Ceramics](../ceramics/index.md) — kiln firing for clay pipe
- [Rubber](../polymers/rubber.md) for gasket manufacture
- [Copper smelting](../metals/index.md) for copper tube production
- [Polymers](../polymers/index.md) for PVC pipe extrusion

## Bill of Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Pig iron or scrap iron (cast pipe) | 50-200 kg/m | Gray iron (Fe + 3-4% C + 1-3% Si), for centrifugal casting | [Iron & Steel](../metals/iron-steel.md) | Ductile iron (Mg-treated, higher strength) |
| Steel plate or billet (steel pipe) | 20-100 kg/m | A36 or A53 (welded), 1020 or 4130 (seamless) | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (304/316) for corrosive service |
| Clay (terracotta pipe) | 15-40 kg/m | Fireclay or stoneware clay, fired to 1000-1200°C | [Ceramics](../ceramics/index.md) | Concrete pipe (larger diameters) |
| Copper billet (copper tube) | 5-20 kg/m | C12200 (DHP copper), deoxidized, for drawing | [Metals](../metals/index.md) | Stainless steel tube (higher pressure) |
| Rubber gaskets | 1 per joint | SBR or neoprene, molded to pipe bell profile | [Rubber](../polymers/rubber.md) | Lead-caulked joints (historical, not for potable water) |
| Welding consumables | 1-5 kg/joint | E6010/E7018 electrodes for shielded metal arc welding | [Welding](../machine-tools/welding-equipment.md) | Oxy-acetylene welding (thinner wall) |
| Cutting oil and threading tools | As needed | High-speed steel dies for NPT threading | [Machine Tools](../machine-tools/index.md) | — |
| Cement mortar (lining) | 5-20 kg/m | 1:1 to 1:2 cement:sand mix, spun inside pipe | [Chemistry: Cement](../chemistry/cement.md) | Epoxy lining (higher performance, higher cost) |
| Galvanizing zinc | 2-5 kg/m | Hot-dip at 450-460°C, 300-600 g/m² coating weight | [Metals](../metals/index.md) | Paint, bitumen wrap (exterior only) |
| Solder (copper joints) | 0.05-0.2 kg/joint | 95/5 tin-antimony (lead-free) or 60/40 tin-lead | [Metals](../metals/index.md) | Brazing alloy (higher strength, higher temperature) |
| PVC solvent cement | 0.05-0.1 L/joint | PVC resin dissolved in tetrahydrofuran/cyclohexanone | [Polymers](../polymers/index.md) | Rubber ring push-on joints (larger PVC) |

## Process Description

### Cast Iron Pipe (Centrifugal Casting)

**Principle**: Molten iron poured into a horizontally spinning mold is distributed evenly by centrifugal force, producing a dense, defect-free cylindrical casting with a smooth internal surface. Centrifugal pressure forces trapped gas and slag to the inner surface where it can be machined away.

**Prerequisites**: [Cast iron melting furnace](../metals/iron-steel.md), water-cooled steel mold, rotating drive mechanism, [annealing furnace](../metals/iron-steel.md).

**Materials**: Pig iron or scrap (50-200 kg/m), refractory mold coating, machining tools for end preparation.

**Construction**:

1. **Prepare the mold**: Line a water-cooled steel cylinder (the mold) with a thin layer of refractory coating (silica-based spray) to prevent the casting from bonding to the mold. The mold length determines the pipe length (typically 3-6 m per section).
2. **Spin and pour**: Mount the mold horizontally on roller supports. Spin the mold to 300-600 RPM. Pour molten iron (1350-1400°C) into the rotating mold through a trough. Centrifugal force distributes the iron evenly along the mold wall, producing a dense, defect-free casting with a smooth internal surface. The water-cooled mold solidifies the iron in 1-3 minutes.
3. **Extract and anneal**: Stop the mold rotation. Extract the solidified pipe from the mold using a pulling mechanism. Anneal the pipe at 800-900°C for 30-60 minutes to relieve casting stresses and achieve the target hardness (180-240 HB for gray iron).
4. **Machine the ends**: Cut the pipe to exact length (±3 mm). For bell-and-spigot joints, machine one end to form the spigot (plain end that inserts into the bell) and the other end to form the bell (enlarged socket). The bell internal diameter is 3-6 mm larger than the spigot outside diameter to accept the rubber gasket. For flanged joints, machine bolt holes in flange rings cast integral with the pipe ends.
5. **Test**: Hydrostatically test each pipe section at 1.5× rated working pressure for 10 seconds minimum. No leaks, weeps, or visible defects.

**Expected performance**: Diameter range: 50-1200 mm. Pressure rating: 10-40 bar. Service life: 50-100+ years. Joint types: bell-spigot rubber gasket, flanged.

### Steel Pipe (Welded Seam)

**Principle**: Flat steel plate is progressively rolled into a cylinder and the longitudinal seam is welded using submerged arc welding (SAW). The weld provides a continuous pressure-tight joint.

**Prerequisites**: [Steel plate](../metals/iron-steel.md), [forming rollers](../machine-tools/index.md), [submerged arc welding equipment](../machine-tools/welding-equipment.md), [expanding mandrel](../machine-tools/index.md).

**Materials**: Steel plate (20-100 kg/m), welding wire, granular flux.

**Construction**:

6. **Form the plate**: Cut steel plate to the required width (plate width = π × pipe OD, approximately). Roll the plate through a series of forming rollers that progressively bend it into a cylindrical shape. The plate edges meet at a longitudinal seam. For spiral-welded pipe, the plate is fed at an angle to form a helical seam.
7. **Weld the seam**: Weld the longitudinal seam from both inside and outside using submerged arc welding (SAW). SAW feeds a continuous wire electrode under a blanket of granular flux. The arc melts the wire, flux, and base metal, creating a deep-penetration weld. Weld speed: 0.5-2.0 m/min. Inspect the seam with ultrasonic testing or radiography.
8. **Expand and round**: Pass the welded pipe through an expanding mandrel (mechanical or hydraulic) to achieve the exact specified outside diameter and roundness (ovality <1% of OD). The expansion process also tests the weld integrity — defective welds crack under the expansion force.
9. **Galvanize (optional)**: For corrosion protection, hot-dip galvanize the pipe by immersing it in molten zinc at 450-460°C. Zinc coating weight: 300-600 g/m² (both sides). Galvanizing adds 20-50 years of corrosion protection in non-aggressive soils and water.

### Steel Pipe (Seamless, Drawn from Billet)

**Principle**: A solid steel billet is heated and pierced to form a hollow tube shell, then rolled and drawn to final dimensions. No welded seam — the pipe is one continuous piece of steel.

**Prerequisites**: [Steel billets](../metals/iron-steel.md), piercing mill (Mannesmann process), plug mill or mandrel mill, [cold-drawing equipment](../machine-tools/index.md).

**Materials**: Steel billets (100-300 mm diameter), lubricants for cold drawing.

**Construction**:

10. **Pierce the billet**: Heat a solid steel billet (100-300 mm diameter) to 1200-1250°C. Push the billet over a mandrel between two oblique rotating rollers that force the billet to deform and pierce, creating a hollow tube shell (the Mannesmann process).
11. **Reduce and size**: Pass the hollow shell through a series of rolling stands (plug mill or mandrel mill) that reduce the wall thickness and outside diameter to the target dimensions. The final pass achieves wall thickness tolerance of ±10-12.5%.
12. **Cold-draw (optional)**: For tighter tolerances and better surface finish, pull the tube through a die with a mandrel inside (drawn over mandrel, DOM). Each cold-drawing pass reduces the OD by 2-5 mm and improves tolerance to ±0.5% of wall thickness. Cold drawing work-hardens the steel — anneal between passes if additional drawing is needed.

### Clay (Terracotta) Pipe

**Principle**: Fireclay or stoneware clay is extruded into pipe shapes and fired in a kiln to vitrification temperature (1000-1200°C), where the clay partially melts and fuses into a hard, chemically inert ceramic.

**Prerequisites**: [Clay preparation equipment](../ceramics/index.md), extrusion press, drying room, [kiln](../ceramics/index.md).

**Materials**: Fireclay or stoneware clay (15-40 kg/m), grog (pre-fired crushed clay, 20-30%), water.

**Construction**:

13. **Prepare the clay**: Mix fireclay or stoneware clay with water to a plastic consistency (15-20% moisture). Add grog (pre-fired crushed clay) at 20-30% to control shrinkage and improve thermal shock resistance during firing. De-air the clay in a vacuum pug mill to remove trapped air bubbles that would create weaknesses.
14. **Extrude the pipe shape**: Force the prepared clay through an extrusion die that forms the pipe cross-section (cylinder with bell end). The extrusion produces a continuous column that is cut to length (typically 0.6-1.0 m sections for standard vitrified clay pipe). The bell is formed by a special die section that enlarges one end.
15. **Dry**: Air-dry the extruded pipes for 3-7 days to reduce moisture below 3%. Rapid drying causes cracking. Controlled drying in a heated room (30-40°C) speeds the process.
16. **Fire in a kiln**: Load the dried pipes into a kiln. Fire to 1000-1200°C over 12-24 hours (ramp rate 50-100°C/hour to avoid thermal shock). Hold at peak temperature for 2-4 hours (vitrification — the clay partially melts and fuses into a ceramic). Cool over 12-24 hours. The fired pipe is hard, chemically inert, and impervious to water.
17. **Apply glaze (optional)**: A salt glaze (sodium chloride thrown into the kiln at peak temperature) or slip glaze (clay slip applied before firing) seals the surface and reduces friction. Vitrified clay pipe is the standard for sewage — chemically resistant to all common sewage constituents including sulfides, acids, and alkalis.

### Steel Pipe — Threaded Joints

**Principle**: Tapered pipe threads (NPT — National Pipe Thread Tapered, taper 1:16) create a mechanical seal by thread deformation as the fitting tightens. The thread engagement increases diameter interference, compressing the threads together. Thread sealant (PTFE tape or pipe dope) fills the spiral leak path between threads.

**Prerequisites**: [Steel pipe](../metals/iron-steel.md), pipe threading dies, pipe vise, PTFE tape or pipe sealant.

**Materials**: Steel pipe sections, threaded fittings (elbows, tees, couplings), PTFE tape or pipe thread sealant.

**Construction**:

18. **Cut the pipe**: Cut steel pipe to length with a pipe cutter (rotating cutting wheel) or abrasive saw. Deburr the cut end inside and out — burrs create turbulence and restrict flow.
19. **Thread the end**: Clamp the pipe in a vise. Run a pipe threading die (manual ratcheting or powered) onto the end. The die cuts NPT threads — taper of 1:16. Thread length: approximately 5-7 threads for 25 mm (1 inch) pipe. Apply cutting oil during threading to prevent galling and produce clean threads.
20. **Seal and assemble**: Apply PTFE tape (2-3 wraps clockwise around the male threads, wrapping in the direction of tightening) or pipe thread sealant (linseed oil-based paste with fillers). Thread the fitting onto the pipe by hand, then tighten 1-2 turns past hand-tight with a pipe wrench. Do not overtighten — tapered threads can split the fitting or gall the threads.

### Steel Pipe — Flanged Joints

**Principle**: Two flat-faced flanges bolt together with a compressible gasket between them. The bolt force compresses the gasket into the serrated flange face, creating a pressure-tight seal. Flanged joints allow disassembly for maintenance.

**Prerequisites**: [Steel pipe](../metals/iron-steel.md), [welding equipment](../machine-tools/welding-equipment.md) for attaching flanges, gasket material, torque wrench.

**Materials**: Weld-neck or slip-on flanges (4-24 bolts per flange depending on size), flat gaskets (rubber for water, fiber for moderate temperature, spiral-wound metal for high temperature), bolts and nuts.

**Construction**:

21. **Prepare flanges**: Weld slip-on or weld-neck flanges to each pipe end. Weld-neck flanges provide better stress distribution for high-pressure service. Face the flange sealing surface flat and smooth (serrated finish for gasket grip — 0.8 μm Ra concentric grooves).
22. **Install gasket and bolts**: Place a flat gasket (rubber, fiber, or spiral-wound metal) between the flange faces. Insert bolts (typically 4-24 bolts per flange depending on size and pressure class). Tighten in a cross-pattern sequence to the specified torque. Do not tighten sequentially around the circle — this warps the flange and causes leaks.
23. **Torque verification**: After initial tightening, re-torque all bolts in the same cross-pattern to compensate for gasket creep. For critical services (steam, toxic fluids), verify bolt tension with a torque wrench or ultrasonic bolt gauge.

### Copper Tube — Soldered (Sweat) Joints

**Principle**: A capillary joint where molten solder is drawn into the annular gap between the tube outside diameter and the fitting inside diameter by capillary action. The solder alloy bonds to both surfaces, creating a pressure-tight seal. Soldering temperature: 200-260°C (well below the copper melting point of 1085°C).

**Prerequisites**: [Copper tube](../metals/index.md), copper fittings (elbows, tees, couplings), solder (95/5 tin-antimony or 60/40 tin-lead), flux, propane torch.

**Materials**: Copper tube (Type L or Type M), wrought copper fittings, solder wire (1.5-3 mm diameter), flux paste (petroleum-based with zinc chloride or rosin-based), emery cloth or wire brush.

**Construction**:

24. **Cut and prepare the tube**: Cut copper tube to length with a tube cutter (rotating cutting wheel that produces a clean, square cut). Remove internal burr with a deburring tool. Clean the outside of the tube end with emery cloth or a wire brush until bright metal is exposed (minimum 20 mm cleaning length for standard joints). Clean the inside of the fitting socket the same way.
25. **Apply flux**: Brush a thin, even coat of flux paste onto the cleaned tube end and the inside of the fitting socket. Flux removes the oxide layer that forms on heated copper and allows the solder to wet the surface. Without flux, solder balls up and refuses to flow.
26. **Assemble and heat**: Push the tube fully into the fitting socket. Twist slightly to spread the flux evenly. Heat the joint with a propane torch, moving the flame around the fitting (not the tube). The fitting mass is greater, so it takes longer to heat. Touch the solder wire to the joint where the tube enters the fitting — when the joint is hot enough, the solder melts and is drawn into the annular gap by capillary action. Feed solder until a continuous ring of solder appears at the mouth of the fitting. Do not apply solder directly to the flame.
27. **Cool and clean**: Allow the joint to cool naturally. Do not quench with water — thermal shock can crack the solder joint. Wipe away excess flux with a damp rag while the joint is still warm (flux residue is corrosive to copper over time).

### PVC Pipe — Solvent Cement Joints

**Principle**: PVC solvent cement partially dissolves the pipe and fitting surfaces, creating a welded joint as the solvent evaporates. The cement contains PVC resin dissolved in a strong solvent (tetrahydrofuran or cyclohexanone). When applied to both surfaces, it softens the PVC, and when the surfaces are pressed together, the dissolved layers intermix and fuse into a continuous plastic weld as the solvent evaporates.

**Prerequisites**: [PVC pipe and fittings](../polymers/index.md), PVC solvent cement, primer, joining tools.

**Materials**: PVC pipe (PN10-PN16 rated), PVC fittings (socket type), PVC primer (clear or purple, contains methyl ethyl ketone or tetrahydrofuran), PVC solvent cement (gray or clear), clean rag.

**Construction**:

28. **Cut and prepare**: Cut PVC pipe square with a fine-tooth saw or pipe cutter. Deburr the inside and outside of the cut. Dry-fit the pipe into the fitting socket — the pipe should enter 1/2 to 2/3 of the socket depth by hand. If it bottoms out without resistance, the fit is too loose.
29. **Prime both surfaces**: Apply PVC primer to the outside of the pipe end (to the depth of the fitting socket) and to the inside of the fitting socket. Primer removes the glossy surface and softens the PVC for cement adhesion. Allow primer to evaporate (15-30 seconds).
30. **Apply cement and join**: Apply a full, even coat of PVC solvent cement to the outside of the pipe end and a medium coat to the inside of the fitting socket. Immediately push the pipe into the fitting socket with a quarter-turn twist to spread the cement evenly. Hold the joint together for 30 seconds (the cement tries to push the pipe back out as the solvent softens the PVC). Wipe away excess cement with a rag.
31. **Cure**: Do not disturb the joint for 15 minutes minimum. Full pressure-rated cure time: 24 hours at 20°C, longer at lower temperatures. Do not test with pressure for at least 2 hours after assembly.

## Quantitative Parameters

| Parameter | Cast Iron | Steel (Welded) | Steel (Seamless) | Clay (Terracotta) | Copper (Type L) | PVC (PN10) |
|-----------|-----------|----------------|-------------------|-------------------|----------------|------------|
| Diameter range | 50-1200 mm | 15-3000 mm | 6-600 mm | 75-1200 mm | 6-150 mm | 15-600 mm |
| Pressure rating | 10-40 bar | 20-100+ bar | 20-200+ bar | 0.5-2 bar | 10-50 bar | 6-16 bar |
| Wall thickness tolerance | ±15% | ±10% | ±0.5-12.5% | ±10% | ±5% | ±10% |
| Service life (buried, potable) | 50-100+ years | 30-80 years | 50-100 years | 50-100+ years | 50+ years | 50+ years |
| Joint types | Bell-spigot, flanged | Welded, threaded, flanged | Welded, compression | Bell-spigot | Soldered, compression | Solvent cement, rubber ring |
| Chemical resistance | Good (with lining) | Poor without lining | Poor without lining | Excellent | Good | Good |
| Impact resistance | Brittle | Ductile | Ductile | Brittle | Ductile | Brittle (cold) |
| Max temperature (continuous) | N/A (not a limitation) | 400°C+ | 400°C+ | N/A | 200°C (solder limit) | 60°C |

### Friction Loss Reference: Head Loss per 100 m of Pipe at 10 L/s

| Pipe Material | 50 mm | 80 mm | 100 mm | 150 mm | 200 mm |
|--------------|-------|-------|--------|--------|--------|
| Steel, new (C=140) | — | 19 m | 6.5 m | 1.5 m | 0.5 m |
| Cast iron, new (C=130) | — | 23 m | 7.8 m | 1.8 m | 0.6 m |
| Cast iron, 20 years (C=100) | — | 36 m | 12 m | 2.8 m | 1.0 m |
| PVC (C=150) | — | 15 m | 5.2 m | 1.2 m | 0.4 m |
| Copper (C=140) | — | 19 m | 6.5 m | — | — |

Head loss calculated using Hazen-Williams formula: h_f = 10.67 × Q^1.852 / (C^1.852 × D^4.87), where h_f is head loss in meters, Q is flow in m³/s, C is Hazen-Williams coefficient, D is pipe inside diameter in meters. As pipes age and accumulate tuberculation (rust nodules), the C value drops — a 20-year-old cast iron pipe has C=100, nearly doubling the friction loss compared to new pipe.

## Scaling Notes

- **Household** (15-50 mm pipe): Copper (soldered) or PVC (solvent cement), installed by hand with wrenches. A 25 mm pipe delivers 1-3 L/s at 2-4 bar — adequate for a single dwelling. No heavy equipment needed.
- **Village distribution** (50-200 mm pipe): Cast iron or PVC push-on joints, installed in trenches with manual labor. A 100 mm cast iron pipe at 4 bar delivers 10-30 L/s — serves 200-500 people. Excavation by hand or small backhoe.
- **Municipal trunk main** (200-1200 mm pipe): Large-diameter cast iron, steel, or concrete pipe. Requires cranes or excavators for handling (sections weigh 200-2000 kg). Welded steel for high pressure, concrete for gravity sewer. A 600 mm pipe at 6 bar delivers 200-500 L/s.
- **Chemical process piping** (15-150 mm): Stainless steel (304/316) with welded or flanged joints. Wall thickness determined by design pressure per piping code. Every weld must be inspected (visual + ultrasonic or radiographic for critical services). Smaller diameters, higher pressures, tighter tolerances.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Threaded joint leaks | Insufficient PTFE tape; damaged threads; overtightened (cracked fitting) | Remove fitting, clean threads, reapply 3 wraps PTFE tape clockwise. Inspect threads for damage (cross-threading, galling). Replace cracked fitting. |
| Welded seam leak (steel) | Porosity or incomplete fusion in the weld | Grind out the defective weld area. Re-weld with proper technique (correct amperage, electrode type, and travel speed). Inspect with ultrasonic testing. |
| Cast iron pipe cracked in handling | Impact during unloading or lowering into trench | Discard cracked sections — do not attempt to repair cast iron under pressure. Use fabric slings and careful lowering. |
| Clay pipe joint offset | Bell and spigot misaligned during assembly; trench not graded properly | Cut and relay the section with proper alignment. Grade trench bottom to uniform slope before laying pipe. |
| Internal corrosion (steel) | Unlined steel in contact with corrosive water; oxygen in system | Apply cement mortar lining (spin-application inside the pipe). Add corrosion inhibitor to the water. Replace severely corroded sections. |
| PVC joint failure | Insufficient cement; pipe not fully inserted; joint disturbed before cure | Cut out the failed joint. Re-cut and re-join with fresh cement. Hold joint for 30 seconds after assembly. Wait 24 hours before pressurizing. |
| Copper solder joint leak | Inadequate cleaning; insufficient flux; joint overheated (burned flux) | Drain the line. Heat the joint and add fresh flux and solder. If the fitting is damaged, cut it out and replace. Clean both surfaces to bright metal before re-soldering. |
| Galvanized coating flaking | Zinc layer consumed after 20-50 years in aggressive soil; mechanical damage during installation | Apply external wrap (polyethylene sleeve or bitumen coating). Replace severely corroded sections with new galvanized or lined pipe. |

## Safety

- **Pipe handling**: Cast iron and clay pipes weighing 50-200+ kg per section require mechanical lifting (hoist, excavator, or pipe tongs). Never lift pipe with a chain through the bore — it can slip. Use fabric slings rated for the load. Tag lines on both ends control swing during lifting.
- **Cutting and welding**: Steel pipe cutting produces sparks and hot metal. Welding produces UV radiation, fumes, and fire risk. Wear welding hood (shade 10-14), leather gloves, and fire-resistant leathers. Clear combustible material within 10 m of welding operations. Fire watch for 30 minutes after welding stops. Ensure adequate ventilation in confined spaces.
- **Pressure testing**: Test pressure is 1.5× working pressure — a significant stored energy hazard. Never stand in line with a flange or fitting while pressurizing. Inspect from a safe distance. Release pressure before tightening any joint.
- **Trench safety**: Buried pipe installation requires trenching. Trenches deeper than 1.5 m must be shored (timber or hydraulic shoring) before workers enter. Fatal trench collapses occur in sand, silt, and wet soil. Slope trench walls to 1:1 (45°) or shallower in unstable ground.
- **Molten metal**: Cast iron pipe casting involves molten iron at 1350-1400°C. Pouring requires full PPE (face shield, leather apron, heat-resistant gloves, foundry boots). Never pour into a wet or damp mold — trapped moisture causes violent spatter.
- **Soldering fumes**: Lead-based solder produces toxic fumes. Use lead-free solder (95/5 tin-antimony) for potable water systems. When using leaded solder for non-potable applications, ventilate the work area and avoid breathing fumes directly.
- **PVC solvent cement**: Contains tetrahydrofuran and cyclohexanone — volatile organic compounds that cause dizziness and respiratory irritation at high concentrations. Use in well-ventilated areas. Wear nitrile gloves (solvent penetrates latex). Do not smoke — the solvents are flammable.

## Quality Control

- **Dimensional inspection**: Measure OD, wall thickness (ultrasonic gauge), and length of each pipe section. For steel pipe: OD tolerance ±1%, wall thickness tolerance ±12.5%. For cast iron: OD tolerance ±2%, wall thickness tolerance ±15%. Sections outside tolerance are rejected or downrated.
- **Weld inspection**: Inspect all seam welds on steel pipe by ultrasonic testing or radiography. Look for porosity, incomplete fusion, undercut, and cracks. Acceptance criteria per API 5L or equivalent: no cracks, porosity <3 mm, incomplete fusion <10% of wall thickness. Defective welds are ground out and re-welded.
- **Hydrostatic re-test on installed joints**: After field welding or joining, pressure-test each pipeline segment at 1.5× design pressure for 2 hours. Walk the line looking for leaks at every joint and fitting.
- **Coating and lining inspection**: For buried steel pipe, verify the external coating (coal tar enamel, polyethylene, or fusion-bonded epoxy) has no holidays (pinholes) using a holiday detector (spark test at 5-15 kV). For cement-mortar-lined pipe, verify lining thickness (3-6 mm) and cure time (28 days for full strength).
- **Copper solder joint verification**: After assembly and cooling, inspect each joint. A proper solder joint shows a continuous fillet of solder around the entire joint circumference. Gaps, voids, or dull gray solder indicate poor joints. Pressure test at 1.5× working pressure before concealing joints in walls.

## Variations and Alternatives

### Concrete Pressure Pipe

Reinforced or prestressed concrete pipe for large-diameter, moderate-pressure applications. Used for municipal water transmission mains (300-3600 mm diameter, 2-20 bar). Construction: steel cylinder with inner and outer concrete layers, helically wrapped with prestressing wire, coated with mortar. Service life: 75-100+ years. Excellent corrosion resistance due to the alkaline concrete encasement of the steel.

**Prerequisites**: [Cement](../chemistry/cement.md), [steel reinforcement](../metals/iron-steel.md), prestressing wire, concrete mixing and curing infrastructure.

**Strengths**: Very long service life. Excellent corrosion resistance. Handles large diameters economically. High structural stiffness resists earth loads.

**Weaknesses**: Very heavy — requires cranes for every installation. Not suitable for pressures above 20 bar. Susceptible to hydrogen sulfide attack in sewer applications (acid degrades concrete).

### PVC (Polyvinyl Chloride) Pipe

Extruded plastic pipe for low-to-moderate pressure water distribution and drainage. Available from 15-600 mm diameter, pressure rated PN6 to PN16 (6-16 bar). Lightweight, corrosion-proof, and easily joined by solvent cement or rubber ring joints. Requires [chlor-alkali chemistry](../chemistry/electrolysis.md) and [polymer extrusion](../polymers/index.md) capability.

**Prerequisites**: PVC resin, plasticizers, extrusion equipment, [chlorine chemistry](../chemistry/electrolysis.md).

**Strengths**: Zero corrosion. Very lightweight — easy to transport and install by hand. Smooth interior surface (low friction loss, C=150 in Hazen-Williams). Low cost per meter.

**Weaknesses**: Temperature-limited (maximum 60°C for continuous service). Brittle in cold weather (below 0°C). UV degradation if stored above ground in sunlight for extended periods. Cannot be used for hot water or steam.

### Copper Tube

Seamless copper tube for domestic water supply, heating, and refrigeration. Available from 6-150 mm outside diameter in three wall types: Type K (thick, underground), Type L (medium, interior), Type M (thin, low-pressure). Joined by soldering (sweat joints) or compression fittings. Requires [copper smelting](../metals/index.md).

**Prerequisites**: [Copper metallurgy](../metals/index.md), [soldering capability](../machine-tools/welding-equipment.md).

**Strengths**: Naturally antimicrobial — biofilm formation is inhibited. Easy to form and join with simple tools (propane torch, flux, solder). Long service life (50+ years). Recyclable. Handles temperatures up to 200°C.

**Weaknesses**: Expensive per meter compared to steel or plastic. Limited diameter range — not available above 150 mm. Susceptible to corrosion in acidic or aggressive water (pH <6.5). Theft risk due to scrap value.

## References

- [Water Distribution](distribution.md) — pipe network design and installation
- [Water Valves](water-valves.md) — isolation and control valves for pipe systems
- [Sewage Collection](sewage.md) — clay and concrete pipe for gravity sewer networks
- [Piping Systems](../gas-handling/piping-systems.md) — gas service piping and high-pressure design
- [Ceramics](../ceramics/index.md) — clay pipe firing and glazing
- [Iron & Steel](../metals/iron-steel.md) — raw materials for metal pipe production
- [Welding Equipment](../machine-tools/welding-equipment.md) — steel pipe welding processes
- [Polymers](../polymers/index.md) — PVC pipe materials and solvent cement

---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
