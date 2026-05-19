# Blast Furnace & Cast Iron Production

> **Node ID**: metals.iron-steel.blast-furnace
> **Domain**: [Metallurgy](./)
> **Dependencies**: `metals.iron-steel`
> **Enables**: `metals.casting`, `machine-tools.casting`
> **Timeline**: Years 10-20
> **Outputs**: pig_iron, gray_cast_iron, white_cast_iron, malleable_iron, sand_castings

### Blast Furnace Operation

The blast furnace is the key advancement from bloomery smelting. Where a bloomery reduces iron ore below its melting point (producing solid bloom that must be consolidated), the blast furnace achieves temperatures high enough to fully melt the iron, producing liquid pig iron that can be cast directly. This is the critical transition from wrought iron to cast iron production.

**Construction**:
- **Shell**: Cylindrical shaft of stone or brick, typically 6-10 m tall, widening from throat (top, ~2 m diameter) to bosh (widest part, ~4 m diameter), then narrowing to the hearth (bottom, ~1.5 m diameter). The bosh angle (the outward slope of the walls) is critical — typically 20-25° from vertical — to allow the solid charge to descend as it shrinks during melting.
- **Tuyeres**: Water-cooled copper or cast iron nozzles near the bottom of the bosh, connected to blowing engine (bellows or, later, steam-driven blower). Deliver preheated air blast into the furnace. Multiple tuyeres (4-8) evenly spaced around circumference for uniform blast distribution.
- **Hearth**: Below the tuyeres, lined with refractory clay or carbon blocks. Collects molten iron and slag. Tap hole at one side near the bottom for iron, slag notch slightly above for slag removal (slag floats on denser molten iron).
- **Charging apparatus**: Double bell or skip hoist at top to charge raw materials while sealing against gas escape.

**Raw materials**:
- **Iron ore**: Hematite (Fe₂O₃) preferred for its high iron content (~70%). Magnetite (Fe₃O₄, ~72%) acceptable but requires higher reduction temperatures. Crushed to 2-5 cm pieces.
- **Fuel**: Charcoal (historical) or coke (from coal, later). 400-800 kg per tonne of iron produced. Modern coke rate: ~400 kg/t.
- **Flux**: Limestone (CaCO₃) or dolomite. 200-400 kg per tonne of iron. Combines with silica and alumina in gangue to form slag (calcium silicate), which is fluid enough to drain from the furnace.
- **Charge ratio**: Roughly 2 tonnes ore, 1 tonne coke, 0.5 tonne limestone per tonne of pig iron produced.

**Operation**:
1. Light fuel bed at the bottom with kindling. Build up a column of alternating layers of coke, ore, and limestone.
2. Start blast. Air enters through tuyeres, combustion of coke produces heat (1500-2000°C in combustion zone) and CO (reducing gas). The CO rises through the charge column, reducing iron oxide stepwise: Fe₂O₃ → Fe₃O₄ → FeO → Fe.
3. Temperature zones from bottom to top: Combustion zone (~2000°C) → active reduction zone (~1200-1500°C) → indirect reduction zone (~800-1200°C) → preheat zone (~200-800°C).
4. Molten iron drips to the hearth. Slag (lighter, ~2.5-3.5 t/m³ vs ~7.0 t/m³ for iron) floats on top.
5. Tap iron every 2-4 hours by opening tap hole with iron bar. Molten iron flows into sand-bed channel (runner) and then into ladles. Each cast yields 1-5 tonnes.
6. Tap slag separately through the slag notch above the iron tap hole. Slag can be granulated with water for cement additive, or air-cooled for road aggregate.

**Production rates**: A small charcoal blast furnace (5-6 m shaft height) produces 0.5-2 tonnes of pig iron per day. A larger furnace (10+ m) with coke fuel and steam-powered blast produces 10-50 tonnes per day. Continuous operation — once lit, a blast furnace runs for years between relinings (campaign life 5-10 years). Stopping and restarting is extremely difficult.

### Pig Iron

**Composition**: ~3.5-4.5% C, ~1-3% Si, ~0.5-1.5% Mn, ~0.02-0.1% S, ~0.05-0.3% P. The high carbon content is the defining characteristic — it lowers the melting point from pure iron's 1538°C to ~1150-1200°C, which is why the blast furnace can produce fully liquid metal while a bloomery cannot.

**Properties**: Very hard and brittle. Cannot be forged or rolled — cracks under hammer. Excellent fluidity when molten — fills complex molds. Used primarily as an intermediate product, remelted in cupola furnaces for casting, or refined to steel.

### Cupola Furnace

The cupola is the foundry workhorse for remelting pig iron and scrap into cast iron castings. Simpler and cheaper than a blast furnace — it melts existing iron rather than reducing ore.

- **Construction**: Cylindrical steel shell (1-3 m diameter, 3-6 m tall), lined with refractory brick. Charging door at mid-height. Tuyeres near bottom connected to blower. Tap hole and slag hole at base.
- **Operation**: Layer coke bed and iron charge (pig iron + scrap cast iron, often with steel scrap for composition adjustment) alternately through the charging door. Ignite coke bed, start blast. Metal melts and drips through the coke bed into the well at the bottom. Open tap hole to pour iron into ladles.
- **Capacity**: 1-30 tonnes/hour depending on size. Intermittent operation — can be started and stopped as needed. This makes the cupola ideal for batch foundry work, unlike the continuous blast furnace.

### Cast Iron Types

- **Gray cast iron**: Carbon present as graphite flakes in a pearlite/ferrite matrix. Graphite gives characteristic gray fracture surface. Excellent machinability (graphite breaks chips), superior vibration damping (ideal for machine tool bases), good thermal conductivity. Tensile strength 150-400 MPa. Casts easily — good fluidity, minimal shrinkage (~1%). Used for: machine frames, engine blocks, cookware, pipes.
- **White cast iron**: Carbon present as cementite (Fe₃C) rather than graphite. Very hard (HV 400-600), extremely brittle. Produced by rapid cooling (chilling against metal mold) or by low silicon content. Used for wear surfaces (crusher jaws, mill liners) and as precursor to malleable iron.
- **Malleable iron**: Produced by annealing white iron castings at 850-950°C for 40-80 hours. Cementite decomposes into irregular graphite nodules (temper carbon). The nodules eliminate stress concentrations → improved ductility and impact resistance vs. gray iron. Elongation 2-10% (vs. <1% for gray iron). Used for pipe fittings, brackets, agricultural hardware, gear cases.

### Sand Casting

The primary molding method for cast iron. Sand molds are cheap, reusable, and can produce shapes impossible to forge.

1. **Pattern making**: Carve wooden pattern of the desired part, oversized by ~1% to compensate for shrinkage during cooling. Include draft angles (~1-3°) on vertical surfaces so pattern can be withdrawn from sand.
2. **Molding**: Pack molding sand (silica sand + 5-10% clay binder + 3-5% water) around pattern in a two-part flask (cope = top half, drag = bottom half). Ram sand firmly around pattern — loose sand causes mold collapse when metal is poured.
3. **Pattern withdrawal**: Separate cope from drag, remove pattern. Cavity remains in sand. Touch up any damaged edges with trowel.
4. **Gating system**: Cut sprue (vertical pouring channel) and runner (horizontal channel) into cope. Cut risers (reservoirs that feed molten metal to compensate for shrinkage). For internal cavities: place baked sand cores (held in position by core prints — recesses in the mold that locate the core).
5. **Closing**: Replace cope on drag, clamp or weigh down to prevent buoyant forces from lifting cope when molten metal enters the mold.
6. **Pouring**: Preheat ladle to prevent premature solidification. Pour molten iron smoothly into sprue. Pour rate critical — too slow → premature solidification; too fast → turbulence and sand erosion (causes sand inclusions in casting).
7. **Cooling**: Wait 30 minutes to several hours depending on section thickness. Thicker sections cool slower. Shake out (break sand mold away) when casting is below ~400°C.
8. **Finishing**: Cut off sprue, risers, and gates with abrasive saw or chisel. Grind flash (thin metal where cope and drag meet). Inspect for defects: porosity (gas holes), shrinkage cavities, sand inclusions, cold shuts (incomplete fusion).

### Safety & Hazards

- **Molten metal contact**: Pig iron and cast iron melt at 1150-1250°C. Splash from tapping or pouring causes catastrophic burns — molten iron retains enough heat to ignite clothing and burn through leather. Full protective equipment: face shield, leather apron, leggings, aluminized coat, spats over boots. Never stand directly in front of tap hole when opening. Keep pouring area dry — water on floor turns to steam explosively on contact with molten metal.
- **Carbon monoxide**: Blast furnace produces large volumes of CO in the off-gas (20-30% CO). CO is colorless, odorless, lethal. Ensure furnace area is open-air or well-ventilated. Monitor with CO detectors if working indoors. Historical blast furnaces had open tops and natural draft; modern enclosed tops require gas handling systems.
- **Tuyere blowback**: If tuyeres become blocked and pressure builds, removing a blockage can cause a blowback of hot gas and particles. Stand to one side when clearing tuyeres. Wear face shield and heavy gloves.
- **Sand dust (silica)**: Molding sand contains fine silica. Chronic inhalation causes silicosis (progressive, irreversible lung disease). Wet sand during mixing to minimize airborne dust. Use local exhaust ventilation at sand mixing and shakeout stations. Wear respirators during mold making and shakeout operations.
- **Heavy lifting**: Ladles of molten iron are extremely heavy. A 100 kg ladle of iron weighs ~200 kg including the ladle itself. Use proper mechanical lifting equipment (overhead crane, jib crane) for all ladle work. Never carry a full ladle manually.

---

*Part of the [Bootciv Tech Tree](../) • [Metals](./) • [All Domains](../)*
