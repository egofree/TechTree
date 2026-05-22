# Primary Metal Forming

> **Node ID**: metals.forming
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`metals.steelmaking`](steelmaking.md), [`metals.aluminum`](aluminum.md), [`machine-tools`](../machine-tools/index.md)
> **Timeline**: Years 15-30
> **Outputs**: steel slab, plate, sheet, bar, structural shapes, aluminum profiles, forgings

### Overview

Primary metal forming transforms molten or freshly cast metal into the stock shapes that feed all downstream manufacturing — slab, plate, bar, rod, structural sections, extrusions, and forgings. These processes operate at or near the smelter or mill, handling metal at temperatures where yield strength is 60-80% below room-temperature values. This page covers **bulk forming at the mill**: continuous casting, hot rolling, extrusion, wire rod rolling, production forging, and structural section rolling.

Secondary operations — cold rolling to final gauge, stamping, deep drawing, wire drawing from rod, and sheet metal forming — are covered in [Machine Tools Forming](../machine-tools/forming.md).

### Process Flow

Liquid steel from the [steelmaking](./steelmaking.md) ladle or aluminum from [smelting](./aluminum.md) enters primary forming through one of two routes:

1. **[Ingot casting](../glossary/ingot-casting.md)** → reheat → hot working (forging, rolling). Traditional route, still used for specialty steels and large forgings.
2. **[Continuous casting](../glossary/continuous-casting.md)** → direct hot rolling. The dominant modern route — 95%+ of world steel production. Eliminates ingot-to-bloom conversion steps, improving yield by 8-12%.

The choice between routes depends on product mix and capital availability. Integrated steelworks producing commodity shapes (strip, structural sections, rail) use continuous casting exclusively. Specialty steelmakers producing small batches of high-alloy or tool steel may still use ingot routes because the ladle sizes are too small for economic continuous casting.

**Energy intensity**: Hot rolling consumes 1.5-2.5 GJ per ton of finished steel (primarily for reheating). This is 5-8% of the total energy used in steelmaking from iron ore. Continuous casting with hot charging (transfer slabs to the reheat furnace while still at 600-800°C from the caster) reduces reheating fuel consumption by 30-50%.

### Continuous Casting

Continuous casting solidifies liquid metal into semi-finished shapes (slab, bloom, billet) in a single continuous operation, replacing the older ingot-teeming → soaking-pit → blooming-mill sequence.

**Machine configuration**:
- **Vertical mold**: Copper mold (internally water-cooled at 5-15 m³/hr) oscillates vertically at 60-200 cycles/min with 2-8 mm stroke. Oscillation prevents sticking by breaking the friction bond between solidifying shell and mold wall. Mold length 700-1100 mm for slabs, 600-900 mm for billets.
- **Curved-mold (bow-type)**: Most common configuration. Mold is curved (~1.5-2.5 m radius of curvature). Strand bends from vertical to horizontal through a guided arc, allowing a lower machine height (6-12 m vs 25-40 m for vertical). Splitting the mold into curved segments simplifies maintenance.

**Mold powder (flux)**: Fed continuously onto the meniscus (liquid steel surface inside mold). Functions: (a) thermal insulation preventing premature solidification at meniscus, (b) lubrication between shell and mold — melts at steel temperature to form a 0.1-0.3 mm liquid film, (c) inclusion absorption — captures alumina and oxide inclusions floating to the surface. Powder consumption: 0.3-0.6 kg/m of cast strand. Powder viscosity at casting temperature: 1-5 poise. Too viscous → inadequate lubrication → sticker breakouts. Too fluid → excessive consumption and meniscus instability.

**Secondary cooling zone**: Below the mold, the thin solidified shell (8-15 mm at mold exit) is further cooled by water sprays and air-mist nozzles. Spray density tapers from 1.5-2.5 L/kg of steel at the top to 0.3-0.8 L/kg lower down. Air-mist nozzles (water atomized with compressed air) provide more uniform cooling than pure water sprays, reducing thermal gradients that cause transverse cracks. Cooling rate controls solidification structure — too fast causes transverse cracks and internal stresses, too slow allows centerline segregation (carbon and alloy enrichment in the last liquid to solidify, creating a brittle band at the center). Metallurgical length (full solidification): 15-30 m depending on section size and casting speed.

**Casting speeds**:
| Section | Dimensions | Speed (m/min) | Notes |
|---------|-----------|---------------|-------|
| Slab | 150-300 × 800-2200 mm | 0.8-2.5 | Thinner slabs cast faster |
| Bloom | 200-400 mm square | 0.5-1.5 | Feed for structural mills |
| Billet | 100-200 mm square | 1.5-4.0 | Feed for bar and rod mills |
| Thin slab (CSP) | 50-80 × 900-1600 mm | 3.0-6.0 | Directly into hot rolling — no reheat |

**Breakout prevention**: A breakout — liquid steel escaping the thin shell — is the most dangerous continuous casting failure. Causes include unstable mold level (±3 mm tolerance), insufficient mold powder, and excessive casting speed. Detection systems measure mold heat transfer (thermocouples embedded in copper mold at 25-50 mm spacing). A sudden temperature spike at any thermocouple indicates a thinning shell and triggers automatic speed reduction.

**Thin-slab casting (Compact Strip Production — CSP)**: Casts 50-80 mm slab directly into an in-line tunnel furnace (holding at 1100°C), then into a 5-6 stand hot strip mill. Eliminates the conventional slab reheating step entirely. Capital cost 40-50% lower than conventional thick-slab route. Product: hot-rolled coil down to 1.0 mm thickness.

### Hot Rolling

Hot rolling deforms metal above its recrystallization temperature (typically 1100-1250°C for steel), producing plate, strip, and coil. The metal recrystallizes continuously during deformation, preventing work hardening.

**Walking beam reheat furnace**: Slabs (150-300 mm thick) enter the furnace at ambient temperature and soak 2-4 hours to reach 1200-1300°C throughout. Walking beams lift and advance slabs incrementally (one beam-width step per cycle) through preheating, heating, and soaking zones. Furnace fuel: coke oven gas, natural gas, or heavy fuel oil. Thermal efficiency: 40-55%. Slab support on water-cooled skid pipes leaves "skid marks" (slightly cooler bands) — minimized by skid insulation and alternating shift patterns. Scale formation: 1-2% of slab weight lost as oxide scale — removed by high-pressure water descaling (15-25 MPa) at furnace exit. Descaling is critical because rolled-in scale creates surface defects that persist through cold rolling and finishing.

**[Roughing mill](../glossary/roughing-mill.md)** (reversing): A single high-capacity stand (or 2-stand tandem) that reduces slab from 200-300 mm to 30-50 mm in 3-7 reversing passes. Roll force: 20,000-40,000 kN. Roll torque: 1,000-3,000 kN·m. Work rolls 1000-1350 mm diameter, driven by 5,000-10,000 kW motors through pinion gears and spindles. Slab passes back and forth, with roll gap adjusted between passes (screw-down mechanism, 0.1 mm positioning accuracy). Edger rolls control width to ±2-5 mm. Transfer bar (the roughed slab) exits at 1050-1150°C. Crop shear at roughing mill exit removes the deformed head and tail of the transfer bar before it enters the finishing mill.

**[Finishing mill](../glossary/finishing-mill.md)** (tandem): 5-7 stands in series, each reducing thickness 20-40%. Strip enters at 30-50 mm, exits at 1.0-12.7 mm. Speed accelerates through the mill — stand 1 at 1-2 m/s, stand 7 at 10-20 m/s. Inter-stand tension is controlled by loopers (dancer rolls that maintain ~5-20 kN tension). Roll cooling: 3,000-6,000 L/min water per stand. Strip temperature at exit: 850-950°C.

**Runout table cooling**: Strip travels over a 60-120 m table with top and bottom water sprays (laminar flow headers). Cooling rate determines microstructure: 10-30°C/s for ferrite-pearlite (structural grades), 50-100°C/s for bainite/martensite (high-strength grades). Accelerated cooling (ACL) enables triple the yield strength of the same chemistry compared to air cooling.

**Coiling**: Strip is coiled at 550-750°C on downcoilers (mandrel diameter 760 mm). Coil weight: 15-35 tons. Coil outer diameter: 1.5-2.1 m. Coils are the feedstock for downstream cold rolling (see [Machine Tools Forming](../machine-tools/forming.md)).

**[Plate mill](../glossary/plate-mill.md)** (separate from strip mill): Produces plate 5-150 mm thick, 1500-5200 mm wide, up to 40 m long. Single-stand reversing mill with 4000-5500 mm work rolls. Roll force: 40,000-100,000 kN — the highest forces in any rolling application. Target applications: ship hull plate, pressure vessels, bridge girders, armored plate. Controlled rolling (CR) holds temperature at specific ranges (850-900°C finish) to refine grain structure without subsequent heat treatment. After rolling, plates are leveled on a multi-roll straightener (9-21 rolls) and ultrasonically tested for internal defects.

**Roll wear and maintenance**: Work rolls in the finishing mill wear rapidly — a set of work rolls lasts 2,000-5,000 tons of steel before requiring regrinding. Rolls are removed, ground to restore concentricity and surface finish, and reinstalled at progressively wider gauge positions. Total roll life: 30,000-100,000 tons before the roll diameter is too small for further use. Backup rolls (forged steel, 1250-1600 mm diameter) last 10-20× longer than work rolls.

### Extrusion

Extrusion forces heated metal through a die to produce profiles of constant cross-section — rods, tubes, and complex shapes impossible or impractical by rolling.

**[Hot extrusion — aluminum](../glossary/hot-extrusion-aluminum.md)** (the dominant application):
- Billet preheated to 450-500°C (aluminum does not require as high a temperature as steel).
- Container heated to 400-450°C to prevent billet chilling.
- Ram pressure: 10-40 MPa on billet face (depending on alloy and reduction ratio).
- Extrusion ratio (container area / die area): 10:1 to 100:1. Higher ratios produce finer grain structure but require greater force.
- Exit speed: 5-50 m/min. Profile exits at 500-550°C (heated by deformation energy).
- Die types: flat die for solid profiles; porthole/bridge die for hollow profiles (metal flows around a mandrel core, welding under pressure). Porthole dies produce seamless-appearing but weld-seam tubes — 4 weld seams typical.
- Alloy range: 6060/6063 (architectural — easy to extrude), 6082 (structural), 7075 (aerospace — difficult, higher pressure).
- Press sizes: 1,000-12,000 tons. Container diameter 100-500 mm.

**[Steel extrusion](../glossary/steel-extrusion.md)** (less common, specialized):
- Steel requires 1100-1250°C and 50-150 MPa — far more force than aluminum.
- Glass lubrication (A SEA process): glass powder placed on billet surface melts during preheating to form a viscous lubricating film. The glass also acts as a thermal barrier between hot billet and cooler tooling.
- Used for stainless steel tubing and special profiles where rolling cannot achieve the shape.

**[Tube extrusion](../glossary/tube-extrusion.md)** (with mandrel):
- A pierced billet is extruded over a mandrel to produce seamless tube. Wall thickness controlled by mandrel-to-die gap. Tube diameter 30-350 mm, wall 3-40 mm.
- Seamless tube is structurally superior to welded tube — no weld seam under pressure. Used for boiler tubing, hydraulic cylinders, and high-pressure applications.

**Profile complexity**: Aluminum extrusion can produce shapes with 0.9 mm minimum wall thickness, ±0.15 mm tolerance on dimensions up to 300 mm. Complex hollow profiles with multiple chambers (window frames, heat sinks) are routine. This capability is why aluminum dominates architectural and thermal-management applications.

**Extrusion defects and quality**:
- **Back-end defect**: Inclusions from billet center concentrate in the last 10-15% of the extrusion — this "butt" is discarded.
- **Surface tearing**: Caused by excessive exit temperature (>550°C for 6xxx alloys) or too-high speed. Controlled by reducing ram speed or preheat temperature.
- **Coarse grain ring**: Over-aging in the extrusion can produce a peripheral coarse grain layer (1-3 mm deep) with poor mechanical properties. Controlled by exit temperature and quench delay time.

### Wire Rod Rolling

Wire rod rolling converts billets (100-150 mm square) into coiled rod of 5-25 mm diameter at high speed. This rod is the feedstock for wire drawing (see [Machine Tools Forming](../machine-tools/forming.md)).

**Mill configuration**: 10-25 stands in a continuous line (no reversing). Roughing group (4-6 stands, horizontal-vertical alternation) → intermediate group (4-8 stands) → finishing block (4-10 stands in a compact housing). Stands are increasingly smaller and faster.

**Speed and reduction**:
- Entry speed (stand 1): 0.1-0.5 m/s
- Exit speed (finishing block): 50-120 m/s (modern high-speed mills)
- Total reduction: billet 130 mm → rod 5.5 mm = 550:1 area reduction
- Reduction per pass: 20-30% (roughing), 15-25% (finishing)

**Temperature management**: Billet enters at 1050-1150°C. Deformation heating compensates for radiation losses. Finishing temperature: 850-1000°C. Controlled cooling on the conveyor after the last stand: Stelmor line — rod lays in overlapping loops on a moving conveyor while fans blow air at 0.5-3.0 m/s. Cooling rate controls microstructure: slow cooling for coarse pearlite (high ductility for drawing), faster cooling for fine pearlite or bainite (higher strength).

**Coiling**: Rod is coiled into 1.0-2.5 ton coils at 1.0-1.5 m diameter. Coil weight limited by handling. Rod is subsequently pickled (10-20% HCl at 60-80°C to remove iron oxide scale) and sometimes skin-passed (light 1-2% cold reduction to improve surface finish and straightness) before being shipped to wire drawing plants.

**Tolerances**: ±0.15 mm on 5.5 mm rod (±2.7%). Ovality ≤ 0.3 mm. These tolerances matter because wire drawing dies require consistent input diameter.

### Forging at Scale

Production forging produces high-integrity components with directional grain flow aligned to the part geometry — a metallurgical advantage over casting or machining from billet.

**Open-die forging (hydraulic press)**:
- Press capacity: 1,000-10,000+ tons. Larger presses (15,000-20,000 t) exist for aerospace forgings.
- Workpiece heated to 1100-1250°C (steel). Manipulated by a 1-10 ton manipulator arm that rotates and positions the piece between flat or V-shaped dies.
- Operations: upsetting (reducing height, increasing diameter), drawing out (elongating, reducing cross-section), punching (piercing holes), cogging (drawing out a bloom into a bar with repeated narrow passes).
- Products: shafts (10-500 mm diameter, up to 15 m long), pressure vessel shells, turbine rotor forgings. Grain flow follows the external contour — critical for fatigue resistance in rotating machinery.
- Reduction: typically 3:1 to 5:1 area reduction from ingot to ensure internal soundness (closing porosity from casting).

**Closed-die forging (impression die)**:
- Two dies contain the negative cavity of the finished shape. Heated preform (blank) is compressed in one or more blows. Flash (excess material) flows into the gutter around the die cavity and is trimmed in a separate press.
- Preform design is critical — the blank must distribute metal to fill the cavity without creating laps (metal folding back on itself) or forging defects. Typically requires 2-4 operations: preform → blocker → finisher → trim.
- Die materials: H13 hot-work tool steel (5% Cr, 1.5% Mo, 1% V) hardened to HRC 44-52. For aluminum extrusion, die steel H11 or H13 is standard. Dies are nitrided (surface hardness ~1100 HV) to resist abrasive oxide wear. Die life: 5,000-50,000 parts for forging dies depending on complexity, material forged, and preform accuracy. Aluminum extrusion dies: 20-100 tons throughput per die set. Die cost is the dominant economic factor — a set of forging dies for a connecting rod costs $10,000-50,000.
- Press or hammer: Mechanical presses (1,000-8,000 tons) for high-volume parts. Screw presses for precision work. Hammers (1-20 ton ram weight) for large or complex forgings.

**Ring rolling**:
- A donut-shaped preform (pierced and upset billet) is placed between a driven main roll and a mandrel roll. The gap narrows as the ring rotates, reducing wall thickness and increasing diameter simultaneously. An axial roll pair controls ring height.
- Products: bearing races, turbine rings, pressure vessel flanges, gear blanks. Ring diameters 100 mm to 8 m. Wall thickness 10-500 mm.
- Advantage over machining from billet: grain flow follows the ring circumference (circumferential grain orientation), maximizing fatigue strength. Material utilization 75-90% vs 30-50% for machining from solid.
- Ring rolling mill capacities: radial force 500-5,000 kN. Main roll diameter 400-1400 mm. Mandrel diameter 80-500 mm (consumable — replaced frequently due to wear and thermal fatigue).

### Section and Structural Rolling

Structural rolling produces the shaped cross-sections that are the skeleton of construction and infrastructure: I-beams, H-beams, channels, angles, tees, and rails.

**[Universal mill](../glossary/universal-mill.md)** (for H-beams and wide-flange sections):
- Four rolls: two horizontal (reduce web thickness) and two vertical (reduce flange thickness). The rolls act simultaneously, allowing independent control of web and flange dimensions.
- H-beam sizes: depth 100-1100 mm, flange width 50-450 mm, web thickness 4-20 mm. Lengths 6-24 m standard.
- Tolerances: depth ±2-4 mm, flange width ±2-3 mm, web thickness ±0.5-1.0 mm. Out-of-square on flanges ≤ 1% of flange width.

**Channel and angle rolling**:
- Channels: rolled in a 2-high stand with shaped rolls. Sizes C100-C400 (depth 100-400 mm). Web and flange dimensions set by roll pass profile.
- Angles (L-shapes): equal-leg (50×50 to 250×250 mm) and unequal-leg. Rolled in 2-3 passes through progressively tighter passes. Radius at root: 4-12 mm (important for stress concentration).
- Both products used for bracing, connections, secondary framing.

**Rail production**:
- Rail steel: pearlitic microstructure (0.6-0.8% C). Head-hardened grades achieve 300-380 HB (Brinell) on the running surface through controlled cooling.
- Profile: asymmetric T-shape optimized for wear resistance (wide head) and flexural stiffness (thick web, broad flat foot). Standard rail weights: 60 kg/m and 75 kg/m for heavy-haul service.
- Rolling: universal mill with 3-5 passes. Length: 25-100 m (longer rails reduce joint count). After rolling, rails are straightened by roller straighteners (7-9 roll pairs) to achieve ≤ 0.5 mm/m straightness.
- Heat treatment (head hardening): rail exits the mill at ~900°C and the head is selectively cooled by water sprays or induction heating followed by compressed-air quench, producing a 10-15 mm deep hardened layer on the running surface while the web and foot remain ductile.

**[Bar rolling](../glossary/bar-rolling.md)** (round, square, hexagonal, flat):
- Billets 100-150 mm square → 10-50 mm rounds in 10-18 passes through a continuous bar mill.
- Two types: horizontal-vertical stands (alternate orientation) or no-twist mills (angled stands that turn the bar without requiring twist). No-twist mills are standard for high-speed production — they eliminate the twist defects that occur when bar is rotated 90° between stands.
- Products: reinforcing bar (rebar 10-50 mm, ribbed for concrete bond), round bar for machining and forging stock, square bar, hex bar for fastener heading.
- Speed: 5-20 m/s at the last stand. Bar is sheared to length (3-12 m) by flying shears synchronized to bar speed, or coiled (10-50 mm diameter, 2-4 ton coils) on garret coilers for bar too thin for economical straight-length handling.

**Dimensional tolerances on rolled products**:
| Product | Dimension | Tolerance |
|---------|-----------|-----------|
| Hot-rolled strip | Thickness 1.0-12.7 mm | ±0.05-0.15 mm |
| Plate | Thickness 5-150 mm | ±0.3-1.5 mm |
| Round bar | Diameter 10-50 mm | ±0.3-0.8 mm |
| Rebar | Diameter 10-50 mm | ±0.5 mm (under nominal) |
| H-beam | Depth 100-1100 mm | ±2-4 mm |

### Material Considerations

**Hot shortness**: Steel containing >0.03% sulfur becomes "hot short" — cracks during hot working because FeS forms a low-melting eutectic (988°C) that coats grain boundaries. Manganese is added (Mn:S ratio ≥ 4:1) to form MnS inclusions (melting point 1610°C) instead. This is why all structural steel specifications require minimum manganese content.

**Scale loss**: Steel oxidizes rapidly at rolling temperatures. Total scale loss from reheat furnace through hot rolling: 1.5-3% of original weight. Scale is recovered and recycled to the sinter plant in integrated steelworks. Oxide scale on the finished product is removed by pickling (HCl or H₂SO₄) before cold rolling.

**Recrystallization control**: The temperature at which the last hot rolling pass occurs determines the grain size. Finishing just above the recrystallization temperature (Ar₃ for steel, ~850°C for low-carbon) produces fine, uniform grains. Controlled rolling exploits this by holding the workpiece at specific temperatures between passes (delayed rolling or interpass cooling). Thermomechanical controlled processing (TMCP) combines controlled rolling with accelerated cooling to produce high-strength low-alloy (HSLA) steels with yield strengths of 350-700 MPa — without the cost of expensive alloying additions or subsequent heat treatment.

**Aluminum forming temperatures**: Aluminum alloys are hot-worked at 350-500°C — much lower than steel. The oxide film (Al₂O₃, melting point 2072°C) does not flake off like steel scale but forms a tenacious, protective skin that is harder than the underlying metal. This means aluminum forming tools must be harder and more wear-resistant than might be expected for such a soft base metal.

### Cross-References

- [Steelmaking](./steelmaking.md) — liquid steel that feeds continuous casting
- [Aluminum](./aluminum.md) — primary aluminum for extrusion billets
- [Machine Tools Forming](../machine-tools/forming.md) — secondary operations: cold rolling, stamping, deep drawing, wire drawing, sheet metal forming
- [Iron & Steel](./iron-steel.md) — alloy properties, heat treatment, and metallurgy
- [Construction Materials](../construction/index.md) — structural steel consumption

### Safety & Hazards

- **Molten metal contact**: Continuous casting and forging handle metal at 1100-1300°C. Enclosed operating stations with thermal shielding. Infrared temperature monitoring with automatic shutdown on anomalies. PPE: aluminized heat-resistant clothing, face shields, safety boots with metatarsal guards.
- **Mechanical energy**: Rolling mills develop 5,000-40,000 kN roll force. Pinch points between work rolls, between stock and roll table, and at shears are the leading cause of amputations in steel mills. Light curtains, safety mats, and two-hand controls are mandatory at operator stations.
- **Scale and debris**: High-pressure descaling (15-25 MPa water) throws hot scale fragments. Enclosed descaling boxes with armored viewing windows. Eye protection required in all hot mill areas.
- **Noise**: Rod mills at 100+ m/s exit speed produce 100-110 dB at the laying head. Hearing protection mandatory. Control rooms are acoustically isolated.
- **Breakout**: Continuous casting breakout releases 10-50 tons of liquid steel. Emergency spray systems (100+ L/s water capacity) cool and contain the spill. Evacuation triggers are automatic on breakout detection.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
