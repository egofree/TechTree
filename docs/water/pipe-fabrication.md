# Pipe Fabrication

> **Node ID**: water.pipe-fabrication
> **Domain**: [Water](./index.md)
> **Dependencies**: [`metals.iron-steel`](../metals/iron-steel.md), [`ceramics.pottery`](../ceramics/index.md), [`machine-tools.machining`](../machine-tools/machining.md)
> **Enables**: [`water.distribution`](distribution.md), [`water.sewage`](sewage.md), [`gas-handling.piping-systems`](../gas-handling/piping-systems.md)
> **Timeline**: Years 5-25
> **Outputs**: pipe, tube, fittings
> **Critical**: Yes — sealed pressurized pipe is the enabling technology for water distribution, sewage conveyance, gas transport, steam power, and hydraulic systems

## Principle

Pipe and tube are hollow cylinders that convey fluids under pressure or by gravity. The distinction: pipe is sized by nominal bore (approximate inside diameter) with standardized wall thickness schedules, while tube is sized by exact outside diameter with wall thickness specified directly. Pipe is joined by threaded fittings, flanges, or welding. Tube is joined by compression fittings, flared fittings, or brazing.

Pipe fabrication covers three primary material families and their construction methods:

- **Cast iron pipe**: Molten iron poured into rotating molds (centrifugal casting) or static sand molds. The standard for municipal water and sewage distribution for over 150 years. Pressure rating: 10-40 bar depending on wall thickness class. Service life: 50-100+ years.
- **Steel pipe**: Seamless (drawn from a billet) or welded (rolled from flat plate and seam-welded). Higher pressure capability than cast iron. Used for steam, gas, high-pressure water, and structural applications. Pressure rating: 20-100+ bar depending on wall schedule.
- **Clay (terracotta) pipe**: Extruded clay fired in a kiln. Low pressure (0.5-2 bar) but excellent chemical resistance and long service life (50+ years). The standard for gravity-flow sewage systems since Roman times.

Jointing methods must match the pipe material and pressure class. Cast iron: lead-caulked joints (historical), rubber gasket push-on joints (modern), or mechanical joint bolts. Steel: threaded (Schedule 40 and below, up to ~20 bar), welded (all pressures), or bolted flanges (for disassembly). Clay: bell-and-spigot with rubber gasket or cement mortar.

## Materials

| Material | Quantity | Specifications | Source | Alternatives |
|----------|----------|----------------|--------|-------------|
| Pig iron or scrap iron (cast pipe) | 50-200 kg/m | Gray iron (Fe + 3-4% C + 1-3% Si), for centrifugal casting | [Iron & Steel](../metals/iron-steel.md) | Ductile iron (Mg-treated, higher strength) |
| Steel plate or billet (steel pipe) | 20-100 kg/m | A36 or A53 (welded), 1020 or 4130 (seamless) | [Iron & Steel](../metals/iron-steel.md) | Stainless steel (304/316) for corrosive service |
| Clay (terracotta pipe) | 15-40 kg/m | Fireclay or stoneware clay, fired to 1000-1200°C | [Ceramics](../ceramics/index.md) | Concrete pipe (larger diameters) |
| Rubber gaskets | 1 per joint | SBR or neoprene, molded to pipe bell profile | [Elastomers](../polymers/elastomers.md) | Lead-caulked joints (historical, not for potable water) |
| Welding consumables | 1-5 kg/joint | E6010/E7018 electrodes for shielded metal arc welding | [Joining](../machine-tools/welding.md) | Oxy-acetylene welding (thinner wall) |
| Cutting oil and threading tools | As needed | High-speed steel dies for NPT threading | [Machine Tools](../machine-tools/index.md) | — |

## Construction Steps

### Cast Iron Pipe (Centrifugal Casting)

1. **Prepare the mold**: Line a water-cooled steel cylinder (the mold) with a thin layer of refractory coating (silica-based spray) to prevent the casting from bonding to the mold. The mold length determines the pipe length (typically 3-6 m per section).
2. **Spin and pour**: Mount the mold horizontally on roller supports. Spin the mold to 300-600 RPM. Pour molten iron (1350-1400°C) into the rotating mold through a trough. Centrifugal force distributes the iron evenly along the mold wall, producing a dense, defect-free casting with a smooth internal surface. The water-cooled mold solidifies the iron in 1-3 minutes.
3. **Extract and anneal**: Stop the mold rotation. Extract the solidified pipe from the mold using a pulling mechanism. Anneal the pipe at 800-900°C for 30-60 minutes to relieve casting stresses and achieve the target hardness (180-240 HB for gray iron).
4. **Machine the ends**: Cut the pipe to exact length (±3 mm). For bell-and-spigot joints, machine one end to form the spigot (plain end that inserts into the bell) and the other end to form the bell (enlarged socket). The bell internal diameter is 3-6 mm larger than the spigot outside diameter to accept the rubber gasket. For flanged joints, machine bolt holes in flange rings cast integral with the pipe ends.
5. **Test**: Hydrostatically test each pipe section at 1.5× rated working pressure for 10 seconds minimum. No leaks, weeps, or visible defects.

### Steel Pipe (Welded Seam)

6. **Form the plate**: Cut steel plate to the required width (plate width = π × pipe OD, approximately). Roll the plate through a series of forming rollers that progressively bend it into a cylindrical shape. The plate edges meet at a longitudinal seam. For spiral-welded pipe, the plate is fed at an angle to form a helical seam.
7. **Weld the seam**: Weld the longitudinal seam from both inside and outside using submerged arc welding (SAW). SAW feeds a continuous wire electrode under a blanket of granular flux. The arc melts the wire, flux, and base metal, creating a deep-penetration weld. Weld speed: 0.5-2.0 m/min. Inspect the seam with ultrasonic testing or radiography.
8. **Expand and round**: Pass the welded pipe through an expanding mandrel (mechanical or hydraulic) to achieve the exact specified outside diameter and roundness (ovality <1% of OD). The expansion process also tests the weld integrity — defective welds crack under the expansion force.
9. **Galvanize (optional)**: For corrosion protection, hot-dip galvanize the pipe by immersing it in molten zinc at 450-460°C. Zinc coating weight: 300-600 g/m² (both sides). Galvanizing adds 20-50 years of corrosion protection in non-aggressive soils and water.

### Steel Pipe (Seamless, Drawn from Billet)

10. **Pierce the billet**: Heat a solid steel billet (100-300 mm diameter) to 1200-1250°C. Push the billet over a mandrel between two oblique rotating rollers that force the billet to deform and pierce, creating a hollow tube shell (the Mannesmann process).
11. **Reduce and size**: Pass the hollow shell through a series of rolling stands (plug mill or mandrel mill) that reduce the wall thickness and outside diameter to the target dimensions. The final pass achieves wall thickness tolerance of ±10-12.5%.
12. **Cold-draw (optional)**: For tighter tolerances and better surface finish, pull the tube through a die with a mandrel inside (drawn over mandrel, DOM). Each cold-drawing pass reduces the OD by 2-5 mm and improves tolerance to ±0.5% of wall thickness. Cold drawing work-hardens the steel — anneal between passes if additional drawing is needed.

### Clay (Terracotta) Pipe

13. **Prepare the clay**: Mix fireclay or stoneware clay with water to a plastic consistency (15-20% moisture). Add grog (pre-fired crushed clay) at 20-30% to control shrinkage and improve thermal shock resistance during firing. De-air the clay in a vacuum pug mill to remove trapped air bubbles that would create weaknesses.
14. **Extrude the pipe shape**: Force the prepared clay through an extrusion die that forms the pipe cross-section (cylinder with bell end). The extrusion produces a continuous column that is cut to length (typically 0.6-1.0 m sections for standard vitrified clay pipe). The bell is formed by a special die section that enlarges one end.
15. **Dry**: Air-dry the extruded pipes for 3-7 days to reduce moisture below 3%. Rapid drying causes cracking. Controlled drying in a heated room (30-40°C) speeds the process.
16. **Fire in a kiln**: Load the dried pipes into a kiln. Fire to 1000-1200°C over 12-24 hours (ramp rate 50-100°C/hour to avoid thermal shock). Hold at peak temperature for 2-4 hours (vitrification — the clay partially melts and fuses into a ceramic). Cool over 12-24 hours. The fired pipe is hard, chemically inert, and impervious to water.
17. **Apply glaze (optional)**: A salt glaze (sodium chloride thrown into the kiln at peak temperature) or slip glaze (clay slip applied before firing) seals the surface and reduces friction. Vitrified clay pipe is the standard for sewage — chemically resistant to all common sewage constituents including sulfides, acids, and alkalis.

### Threaded Joints (Steel Pipe)

18. **Cut the pipe**: Cut steel pipe to length with a pipe cutter (rotating cutting wheel) or abrasive saw. Deburr the cut end inside and out — burrs create turbulence and restrict flow.
19. **Thread the end**: Clamp the pipe in a vise. Run a pipe threading die (manual ratcheting or powered) onto the end. The die cuts NPT (National Pipe Thread Tapered) threads — taper of 1:16. Thread length: approximately 5-7 threads for 25 mm (1 inch) pipe. Cut threads are tapered; the seal forms by thread deformation as the fitting tightens.
20. **Seal and assemble**: Apply PTFE tape (2-3 wraps clockwise around the male threads) or pipe thread sealant (linseed oil-based paste with fillers). Thread the fitting onto the pipe by hand, then tighten 1-2 turns past hand-tight with a pipe wrench. Do not overtighten — tapered threads can split the fitting or gall the threads.

## Expected Performance

| Parameter | Cast Iron | Steel (Welded) | Steel (Seamless) | Clay (Terracotta) |
|-----------|-----------|----------------|-------------------|-------------------|
| Diameter range | 50-1200 mm | 15-3000 mm | 6-600 mm | 75-1200 mm |
| Pressure rating | 10-40 bar | 20-100+ bar | 20-200+ bar | 0.5-2 bar (gravity only) |
| Wall thickness tolerance | ±15% | ±10% | ±0.5-12.5% | ±10% |
| Service life (buried, potable water) | 50-100+ years | 30-80 years (with lining) | 50-100 years (with lining) | 50-100+ years |
| Joint types | Bell-spigot, flanged | Welded, threaded, flanged | Welded, compression, flared | Bell-spigot |
| Chemical resistance | Good (with cement lining) | Poor without lining | Poor without lining | Excellent (vitrified) |
| Impact resistance | Brittle — fractures under impact | Ductile — bends before breaking | Ductile — bends before breaking | Brittle — fractures under impact |

## Calibration and Verification

1. **Hydrostatic test**: Pressurize each pipe section (or completed pipeline segment) to 1.5× the design working pressure. Hold for a minimum of 2 hours. Walk the line inspecting for leaks, weeps, or pressure drop. Acceptable pressure drop: <0.1 bar over the test period.
2. **Dimensional verification**: Measure OD, wall thickness (ultrasonic gauge), and length of each section. Verify ovality (difference between max and min OD) is within specification (<1% of nominal OD for steel, <2% for cast iron).
3. **Joint pull-out test**: For push-on gasket joints, verify that the pipe is fully inserted into the bell (check the insertion mark on the spigot). Pull-out force for a properly seated gasket joint: 2-10 kN depending on size. Insufficient insertion causes joint separation under pressure or thermal expansion.

## Strengths

- Cast iron pipe provides the longest service life for buried water mains — 100+ years in many installations
- Steel pipe handles the highest pressures and is weldable into continuous runs — the standard for steam, gas, and high-pressure hydraulics
- Seamless steel pipe has no welded seam — the weakest point eliminated, making it suitable for the highest pressure applications
- Clay pipe is chemically inert and resistant to all sewage constituents — never corrodes, never degrades

## Weaknesses

- Cast iron pipe is brittle — impacts during handling and installation cause cracking. Do not drop. Do not backfill with large rocks.
- Steel pipe corrodes without protection — requires lining (cement mortar, epoxy) for potable water and coating (asphalt, polyethylene wrap) for buried exterior. Unlined steel in aggressive water lasts 10-20 years.
- Clay pipe is limited to gravity flow (low pressure) — not suitable for pressurized water supply
- Threaded joints leak if undertightened or if PTFE tape is applied incorrectly. Welded joints require skilled welders and inspection.

## Safety

- **Pipe handling**: Cast iron and clay pipes weighing 50-200+ kg per section require mechanical lifting (hoist, excavator, or pipe tongs). Never lift pipe with a chain through the bore — it can slip. Use fabric slings rated for the load.
- **Cutting and welding**: Steel pipe cutting produces sparks and hot metal. Welding produces UV radiation, fumes, and fire risk. Wear welding hood, gloves, and leathers. Clear combustible material within 10 m of welding operations. Fire watch for 30 minutes after welding stops.
- **Pressure testing**: Test pressure is 1.5× working pressure — a significant stored energy hazard. Never stand in line with a flange or fitting while pressurizing. Inspect from a safe distance. Release pressure before tightening any joint.
- **Trench safety**: Buried pipe installation requires trenching. Trenches deeper than 1.5 m must be shored before workers enter.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Threaded joint leaks | Insufficient PTFE tape; damaged threads; overtightened (cracked fitting) | Remove fitting, clean threads, reapply 3 wraps PTFE tape clockwise. Inspect threads for damage (cross-threading, galling). Replace cracked fitting. |
| Welded seam leak (steel) | Porosity or incomplete fusion in the weld | Grind out the defective weld area. Re-weld with proper technique (correct amperage, electrode type, and travel speed). Inspect with ultrasonic testing. |
| Cast iron pipe cracked in handling | Impact during unloading or lowering into trench | Discard cracked sections — do not attempt to repair cast iron under pressure. Use fabric slings and careful lowering. |
| Clay pipe joint offset | Bell and spigot misaligned during assembly; trench not graded properly | Cut and relay the section with proper alignment. Grade trench bottom to uniform slope before laying pipe. |
| Internal corrosion (steel) | Unlined steel in contact with corrosive water; oxygen in system | Apply cement mortar lining (spin-application inside the pipe). Add corrosion inhibitor to the water. Replace severely corroded sections. |

## See Also

- [Water Distribution](distribution.md) — pipe network design and installation
- [Water Valves](water-valves.md) — isolation and control valves for pipe systems
- [Sewage Collection](sewage.md) — clay and concrete pipe for gravity sewer networks
- [Piping Systems](../gas-handling/piping-systems.md) — gas service piping and high-pressure design
- [Ceramics](../ceramics/index.md) — clay pipe firing and glazing
- [Iron & Steel](../metals/iron-steel.md) — raw materials for metal pipe production

[← Back to Water](index.md)
