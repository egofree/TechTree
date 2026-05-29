# Crude Oil Extraction

> **Node ID**: petroleum.extraction
> **Domain**: [Petroleum Extraction & Refining](./index.md)
> **Dependencies**: `petroleum`
> **Enables**: `petroleum.extraction.cable-tool`, `petroleum.extraction.rotary`, [`petroleum.refining`](refining.md)
> **Timeline**: Years 10-35
> **Outputs**: crude_oil, natural_gas_liquids, associated_gas
> **Critical**: No — petroleum provides the highest-value feedstock but coal tar and fermentation alternatives exist for some products

## Why Extraction Matters

Crude oil is the highest energy-density liquid fuel readily available in nature (~42 MJ/kg) and the primary feedstock for the modern organic chemicals industry. Before petroleum, organic chemistry depended on coal tar (low yield, ~3-5% per tonne of coal) and fermentation (limited to ethanol, acetone, and a few other products). Petroleum provides orders of magnitude more aromatic and olefinic feedstock per unit effort. Without extraction capability, a civilization is limited to surface seeps — typically 5-50 liters/day — insufficient for industrial-scale fuel or chemical production.

The extraction progression follows a clear technological ladder: surface collection → cable-tool drilling → rotary drilling → enhanced recovery. Each step requires the tools and materials from the previous industrial stage.

## Surface Collection & Seeps

### Natural Oil Seeps

Oil reaches the surface in many geological settings where an impermeable cap rock has been breached by erosion, faulting, or unconformity. Ancient civilizations from Mesopotamia to the Caspian collected petroleum from seeps for waterproofing, medicinal use, and lamp fuel.

**Collection methods**:
- **Hand-skimming**: Oil pooling on water surfaces in natural depressions. Skim with ladles or absorbent cloth. Yield: 5-50 liters/day per active seep.
- **Hand-dug wells**: Excavate 1-5 m deep pits where oil accumulates in porous sand or limestone. Line with stone or timber. Oil seeps in faster than from surface pools. Yield: 50-200 liters/day from a productive seep well.
- **Spring collection**: Where oil flows with water, dig a collecting pool. Oil floats on water (density ~0.82-0.95 g/cm³ vs. water at 1.0 g/cm³). Skim with ladles or overflow weirs that separate the lighter oil layer. This method powered the earliest commercial petroleum operations in Pennsylvania (1850s).

**Limitations**: Surface seeps represent only ~0.01-0.1% of total subsurface petroleum. Most oil is trapped in reservoirs beneath impermeable cap rock. To access this oil, you must drill.

**Quality**: Seep oil is typically weathered — lighter fractions (gasoline-range) have evaporated, leaving heavier, more viscous oil. Still suitable for distillation into kerosene, diesel, and fuel oil but yields less light fractions than fresh reservoir oil.

### Oil Sands and Heavy Oil

Where oil has migrated to the surface and degraded extensively (bacteria consume light fractions, leaving heavy residuum), the result is oil sands (tar sands) — a mixture of bitumen (~10-12% by weight), sand (~80-85%), and water (~4-5%). The Athabasca deposits in Canada and Orinoco belt in Venezuela represent enormous reserves.

**Surface mining**: Strip-mine oil sand deposits within 75 m of surface. Mine with power shovels and trucks. Crush and mix with hot water (50-80°C) and NaOH (0.1-0.5% as pH modifier) in a separation vessel. Bitumen attaches to air bubbles and floats as froth (Clark Hot Water Extraction Process). Froth diluted with naphtha and centrifuged to remove residual sand and water. Bitumen yield: ~90% recovery from mined ore. Energy cost: ~700-900 MJ per barrel of synthetic crude (high — energy return on investment ~3-5:1 vs. ~10-20:1 for conventional drilling).

**In-situ methods**: For deeper oil sands, steam-assisted gravity drainage (SAGD) injects steam through a horizontal well, reducing bitumen viscosity from ~10⁶ cP to ~10 cP at 200-250°C. Mobilized bitumen drains to a lower parallel production well and is pumped to surface. Requires ~2.5-3.5 barrels of steam per barrel of oil recovered.

## Cable-Tool (Percussion) Drilling

### Principle

A heavy steel bit (chisel or club shape, 50-200 kg) is repeatedly lifted and dropped onto the rock at the bottom of the borehole. Each impact crushes a few millimeters of rock. Debris (cuttings) is periodically bailed out with a sand pump (a valved tube lowered on a separate cable). The technique is ancient — Chinese brine wells reached 1,000+ m depth using bamboo cables and cast iron bits by the 1800s.

### Rig Components

| Component | Description | Material |
|-----------|-------------|----------|
| Derrick | 10-25 m wooden or steel tower supporting cables and pulleys | Timber or steel |
| Walking beam | Rocking beam 4-8 m long, pivoted at center. One end suspends drill tools, other end connects to power source | Wood with iron bands or steel |
| Drill cable | Wire rope or manila rope (modern: 2-3 cm steel wire rope) | Steel wire rope |
| Drill stem | Heavy wall steel bar 3-10 m long, screwed to bit. Provides weight and rigidity | Steel |
| Drill bit | Chisel or cross-shape, 10-25 cm width. Hardened steel face | Forged steel |
| Sand pump | Valved tube on separate cable. Lowered to bottom, pushed into cuttings slurry, valve admits mixture, raised to surface | Steel with leather valve |
| Casing | Iron or steel pipe 10-15 cm diameter. Driven into hole as drilling progresses to prevent collapse and exclude groundwater | Iron or steel |
| Power source | Steam engine (5-20 HP) or horse/ox walking in circle (1-3 HP). Engine dramatically increases drilling speed | — |

### Drilling Procedure

1. **Site preparation**: Level ground, erect derrick, install walking beam and power source. Dig starter hole 1-2 m deep, set conductor pipe (large diameter pipe to guide initial drilling).
2. **Spudding**: Lower drill bit on cable. Walking beam lifts bit 0.5-1.5 m and drops it on each stroke. Stroke rate: 20-60 strokes/minute. Drill at vertical — use plumb bob to check every 10 m.
3. **Cutting removal**: Every 0.5-1.5 m of depth, withdraw drill tools. Lower sand pump to collect crushed rock mixed with water. Bail to surface. Repeat.
4. **Casing**: Drive iron casing into hole as drilling progresses. Casing prevents hole collapse in soft formations and isolates groundwater from the borehole. Casing joints: threaded and coupled, or welded. Seal with hemp packing and lead wool at each joint.
5. **Well completion**: When oil-bearing formation is reached (recognized by oil show in bailer samples, gas pressure at wellhead, or drilling rate increase in porous rock), set production casing. Perforate casing at the production zone (shoot perforations with explosive bullets or mechanical perforator). Install wellhead (pipe fittings controlling flow from the well).
6. **Production**: If reservoir pressure is sufficient (artesian flow), oil flows to surface unassisted. If not, install a downhole pump (sucker rod pump driven by walking beam at surface — the iconic "pumpjack" motion).

### Performance

| Parameter | Value |
|-----------|-------|
| Depth range | 50-2,000 m (practical limit ~1,500 m) |
| Penetration rate | 3-10 m/day in soft rock, 0.5-2 m/day in hard rock |
| Borehole diameter | 10-25 cm |
| Casing requirement | Continuous in soft formations; intermittent in competent rock |
| Major limitation | Cannot handle soft, unconsolidated formations (hole collapses before casing can be set) |

### Historical Context

Colonel Edwin Drake's 1859 well at Titusville, Pennsylvania reached 21 m using cable-tool drilling and struck oil at ~1,000 liters/day — the first commercial oil well. By 1900, cable-tool rigs had drilled thousands of wells to depths of 500-1,500 m across Pennsylvania, Ohio, Texas, and Romania. The technique remained dominant until rotary drilling surpassed it in the 1920s-1930s.

## Rotary Drilling

### Principle

A rotating drill bit grinds rock at the bottom of the borehole. Continuous circulation of drilling fluid (mud) carries cuttings to the surface, cools the bit, and maintains hydrostatic pressure against formation fluids. Rotary drilling is faster, reaches deeper, and handles all formation types — it replaced cable-tool for virtually all drilling above 500 m depth.

### Rig Components

| Component | Description |
|-----------|-------------|
| Rotary table | Circular table in rig floor, turned by power source. Inserts into table grip and rotate the kelly (the topmost square or hexagonal section of drill string that slides through the table) |
| Drawworks | Hoisting drum and brake system for raising and lowering drill string. Wire rope from crown block (top of derrick) to traveling block (above drill string). |
| Mud pumps | Triplex piston pumps, 5-20 MPa operating pressure, 1,000-3,000 L/min flow rate. Circulate drilling mud down the drill string, out the bit nozzles, and back up the annulus (space between drill pipe and borehole wall). |
| Drill string | Seamless steel tubes (drill pipe), 5-10 m per joint, screwed together. Inside diameter 50-100 mm. Transmits rotation and carries mud to the bit. Total length equals well depth. |
| Drill bits | Tri-cone roller bits (three rotating cones with hardened steel or tungsten carbide teeth) or fixed-cutter PDC (polycrystalline diamond compact) bits. Bit diameter: 15-60 cm depending on hole section. |
| Blowout preventer (BOP) | Stack of hydraulic rams installed below the rig floor at the wellhead. In an emergency (well kicks — formation fluid enters the borehole uncontrollably), the BOP seals the well to prevent uncontrolled flow (blowout). Rams can close around pipe (pipe rams), close completely (blind rams), or shear pipe and seal (shear rams). |
| Mud system | Mud tanks, shale shaker (vibrating screen removes cuttings from returning mud), desander and desilter (hydrocyclones remove fine particles), mud mixer (bentonite, barite, chemicals blended into water base). |

### Drilling Mud

Drilling mud serves four critical functions simultaneously:

1. **Cuttings transport**: Mud velocity in the annulus carries rock chips to surface. Minimum annular velocity: 0.3-0.6 m/s. Mud viscosity (measured by Marsh funnel, target: 40-60 seconds per quart) ensures cuttings are suspended when circulation stops.
2. **Hydrostatic pressure control**: Column of mud in the borehole exerts pressure on the formation. Mud weight must exceed formation pore pressure to prevent influx of formation fluids (oil, gas, water). Typical mud weight: 1.05-2.0 g/cm³. Barite (BaSO₄, density 4.5 g/cm³) added as weighting agent.
3. **Bit cooling and lubrication**: Mud flows through bit nozzles at 30-80 m/s, cooling cutting surfaces and removing heat from friction.
4. **Wellbore stability**: Mud pressure supports the borehole wall. Filter cake (thin layer of clay particles deposited on the formation face) prevents mud loss into permeable formations and stabilizes the wall.

**Water-based mud (WBM)**: Water + bentonite clay (4-8% by weight provides viscosity and filtration control) + barite (as needed for density) + NaOH (pH 9.5-10.5 for clay stability) + lignite or lignosulfonate (thinner — controls excessive viscosity). The standard mud for most drilling. Simple, inexpensive, environmentally benign.

**Oil-based mud (OBM)**: Diesel or mineral oil continuous phase + water emulsion (10-30%) + emulsifiers + organophilic clay + barite. Superior wellbore stability in water-sensitive shales (clays that swell on water contact, causing hole collapse). Better lubrication for directional drilling. Higher cost, environmental concerns with disposal.

### Drilling Procedure

1. **Spudding**: Set conductor pipe (large diameter, 30-50 cm, driven or drilled to 10-50 m). Install BOP stack. Rig up mud circulation system.
2. **Drilling surface hole**: Drill large diameter hole (25-45 cm) to below fresh water aquifers (~100-500 m). Run and cement surface casing. Cement pumped down casing, returns to surface in annulus — isolates aquifers.
3. **Drilling intermediate hole**: Reduce bit size (20-35 cm). Drill to the cap rock above the target reservoir (~1,000-3,000 m). Run and cement intermediate casing. Monitor mud weight carefully — formation pressure generally increases with depth.
4. **Drilling production hole**: Final hole section (15-25 cm) drilled through the reservoir. Here, balanced drilling is critical: mud weight must exceed pore pressure but stay below fracture pressure. If mud weight is too low, formation fluid enters the well (kick). If too high, mud fractures the formation and is lost (lost circulation).
5. **Well logging**: Before completing, lower instruments on wireline to measure formation properties: spontaneous potential (identifies permeable zones), resistivity (identifies hydrocarbon vs. water-bearing zones), gamma ray (identifies clay/shale vs. clean sand/carbonate), density porosity, and sonic travel time. These logs determine which zones to produce.
6. **Completion**: Run production casing (10-15 cm) through the reservoir. Cement. Perforate at the target zone using shaped-charge perforating guns lowered on wireline (explosive charges create 1-3 cm diameter holes through casing and cement into the formation, connecting reservoir to wellbore). Install tubing (production conduit inside casing) and wellhead (Christmas tree — valve assembly controlling production flow).

### Directional and Horizontal Drilling

Modern drilling rarely stays vertical. Directional drilling uses a bent sub (angled connector near the bit) or rotary steerable system (downhole motor that pushes the bit in a controlled direction) to navigate the drill string along a planned trajectory. Horizontal wells extend 500-3,000 m laterally through the reservoir, exposing far more reservoir rock to the wellbore than a vertical well (which intersects only the reservoir thickness, typically 5-50 m).

**Advantages of horizontal wells**: 3-10× higher productivity than vertical wells in the same reservoir. Enables drilling under obstacles (lakes, cities, environmentally sensitive areas from a surface location outside the boundary). Essential for tight (low-permeability) formations where the well must contact as much rock surface as possible.

**Measurement while drilling (MWD)**: Sensors near the bit transmit directional data (inclination, azimuth) to surface via pressure pulses in the mud column. The driller adjusts trajectory in real-time based on this feedback.

### Performance

| Parameter | Value |
|-----------|-------|
| Depth range | 100-12,000+ m (typical: 1,000-5,000 m) |
| Penetration rate | 10-100 m/day (formation-dependent) |
| Hole diameter | 15-60 cm (reduces with depth as casing is set) |
| Rig crew | 5-8 persons per shift, 2-3 shifts |
| Rig power | 500-3,000 HP (diesel or electric) |

## Well Production

### Natural Flow (Artesian)

If reservoir pressure exceeds the hydrostatic head of the oil column in the wellbore, oil flows to the surface unassisted. The driving force is reservoir pressure from compressed gas, water influx, or rock compaction. Flow rate depends on reservoir permeability, pressure differential, and oil viscosity.

**Productivity index**: Barrels per day per psi of pressure drawdown (difference between reservoir pressure and wellbore pressure). Typical range: 0.1-50 bbl/day/psi. High-permeability reservoirs have higher indices.

**Decline curve**: All wells decline over time as reservoir pressure depletes. Initial production rate may be 100-10,000 bbl/day; after 5-10 years, typical decline to 10-30% of initial rate. The exponential decline curve (q = qᵢ × e^(-Dt), where D is the decline rate) approximates most well behavior.

### Artificial Lift

When reservoir pressure is insufficient for natural flow, artificial lift methods bring oil to the surface:

**Sucker rod pump (beam pump)**:
- The most common lift method worldwide. Walking beam at surface drives a connected string of steel rods (sucker rods, 16-25 mm diameter) running to the bottom of the well. Rods connect to a downhole pump: a cylinder with ball-and-seat check valves. On the upstroke, the traveling valve closes, lifting the oil column above it; the standing valve opens, admitting fluid from the reservoir. On the downstroke, the traveling valve opens, fluid passes through, and the standing valve closes.
- Depth limit: ~2,500 m (limited by rod weight and buckling). Pump rate: 10-500 bbl/day.
- Surface unit: pumpjack (the iconic horse-head shaped beam seen in oil fields).

**Strengths**:
- Simple, well-understood mechanical system with over a century of field experience
- Low capital cost relative to other artificial lift methods
- Easily inspected and maintained at surface (no downhole electronics)
- Handles viscous crude and moderate sand production without damage
- Can be powered by electric motor, natural gas engine, or even the produced gas itself
- Visual indicator of well status from pumpjack stroke pattern

**Weaknesses**:
- Depth limited to ~2,500 m — rod weight and buckling prevent deeper installation
- Sucker rods subject to fatigue failure, corrosion, and rod-on-tubing wear
- Not suitable for deviated or horizontal wells (rod friction against tubing)
- Low flow rates compared to ESP (max ~500 bbl/day vs. 30,000 bbl/day)
- Moving parts downhole require periodic workover (pull tubing and rods for repair)
- Paraffin and scale buildup on rods increases friction and risk of rod failure

**Gas lift**:
- Inject compressed natural gas through the casing-tubing annulus. Gas enters the tubing through gas lift valves (pressure-operated) at depth. Gas mixes with oil, reducing the fluid density (aerating the column). The reduced hydrostatic head allows reservoir pressure to push the lighter column to surface.
- Advantages: handles sand and deviated wells better than sucker rod pumps. No downhole moving parts to fail. Depth limit: 3,000+ m.
- Requirement: source of compressed gas (typically produced associated gas from the same or nearby wells).

**Strengths**:
- No downhole moving parts — eliminates mechanical failures that plague rod pumps and ESPs
- Handles sand-laden and abrasive fluids without equipment damage
- Works in highly deviated and horizontal wells where rod pumps cannot operate
- Deepest artificial lift method (3,000+ m depth capability)
- Adjustable gas injection rate tunes lift capacity to changing reservoir conditions
- Can be installed in same tubing as production, reducing completion complexity

**Weaknesses**:
- Requires reliable source of compressed gas — not feasible for isolated wells without gas production
- Gas compression at surface consumes significant energy (compressor stations needed)
- Less efficient than mechanical pumping — energy wasted compressing gas that also expands in the well
- Difficult to optimize injection gas volume — over-injection wastes gas, under-injection fails to lift
- Cannot lift very heavy (low API gravity) crude oils effectively
- Mandrel and gas lift valve installation requires specialized wireline work

**Electrical submersible pump (ESP)**:
- Multi-stage centrifugal pump driven by an electric motor, both submerged in the well fluid at the bottom of the well. Power supplied via cable from surface. High production rates: 200-30,000 bbl/day.
- Disadvantages: expensive, sensitive to gas locking and abrasives (sand), motor failure requires pulling the entire tubing string. Best for high-volume, clean-fluid wells.

**Strengths**:
- Highest production rates of any artificial lift method (200-30,000 bbl/day)
- Compact downhole footprint — multi-stage centrifugal pump fits inside standard tubing
- Efficient electrical operation — lower energy cost per barrel than gas lift for high-rate wells
- Minimal surface footprint — only power cable and small control panel visible
- Can handle large fluid volumes in waterflood and high-water-cut production
- Adjustable speed with variable frequency drive (VFD) matches output to reservoir deliverability

**Weaknesses**:
- Very sensitive to free gas — gas locking shuts down the pump if gas fraction exceeds 10-15% at pump intake
- Sand and abrasives destroy pump stages rapidly — unsuitable for unconsolidated sand formations
- Motor failure requires pulling entire tubing string — expensive workover ($50,000-200,000+)
- Electrical cable to motor is vulnerable to mechanical damage during installation and corrosion over time
- High capital cost ($50,000-250,000 per unit) compared to sucker rod pumps
- Limited tolerance for high temperature — motor insulation degrades above 120-150°C

## Enhanced Oil Recovery (EOR)

Primary recovery (natural and artificial lift) typically recovers only 15-30% of the original oil in place (OOIP). EOR methods target the remaining 70-85%.

### Waterflooding (Secondary Recovery)

Inject water into injection wells to maintain reservoir pressure and physically sweep oil toward production wells. The most widely applied EOR method — used in virtually all major fields after primary depletion.

**Process**: Convert some wells to injectors, continue producing from others. Water injected at 5-20 MPa displaces oil through the reservoir rock. Recovery: typically adds 10-20% of OOIP, for total primary + secondary recovery of 25-45%.

**Breakthrough**: Injected water eventually reaches production wells (water breakthrough), and produced fluid becomes increasingly water-cut. A mature waterflood may produce 95% water and 5% oil — still economic if oil price justifies the operating cost of handling large water volumes.

### Thermal Methods (Heavy Oil and Bitumen)

**Cyclic steam stimulation (CSS)**: Inject steam into a single well for days-weeks. Shut in for soak period (days, allowing heat to diffuse into the reservoir and reduce oil viscosity from ~10⁴-10⁶ cP to ~10-100 cP). Then produce back from the same well. Repeat cycles. Recovery: 15-25% of OOIP. Used extensively in California heavy oil and Venezuelan Orinoco belt.

**Steam flooding**: Continuous steam injection into dedicated injection wells, with oil driven to separate production wells. Recovery: 40-60% of OOIP in suitable reservoirs. Requires ~2-4 barrels of steam (as cold water equivalent) per barrel of oil recovered. Steam generation is the major energy cost — typically burns produced heavy oil or natural gas in boilers.

### Chemical and Miscible Methods (Tertiary Recovery)

**CO₂ flooding**: Inject CO₂ (compressed to supercritical or liquid state) into the reservoir. CO₂ dissolves in crude oil, swelling its volume and reducing viscosity. Also achieves miscible displacement — CO₂ and oil become a single phase, eliminating capillary forces that trap oil in pore spaces. Recovery: 10-20% additional OOIP. Requires a CO₂ source (natural CO₂ deposits, power plant flue gas capture, or ammonia plant byproduct). Widely used in the Permian Basin (West Texas).

**Polymer flooding**: Add water-soluble polymer (polyacrylamide, 250-1,500 ppm) to injection water. Increases water viscosity, improving the sweep efficiency (less water bypassing oil through high-permeability channels). Recovery: 5-15% additional OOIP over waterflooding alone.

## Safety & Environmental Concerns

### Blowout Prevention

A blowout — uncontrolled flow of oil and gas from the well — is the most catastrophic drilling accident. Prevention requires:

- **Mud weight monitoring**: Continuously measure mud weight in and out. Any decrease in return mud weight indicates gas influx (gas reduces mud density). Immediately increase mud weight.
- **Kick detection**: Pit volume increase (formation fluid entering wellbore displaces mud into surface tanks), flow rate increase at return line, drilling break (sudden penetration rate increase indicating porous, potentially pressurized zone).
- **BOP operation**: Close BOP rams immediately on detecting a kick. Kill the well by pumping heavy mud through the choke line (controlled flow path through the BOP) to overbalance formation pressure.
- **Well control training**: All drilling crews must be trained in well control procedures. Simulated kick exercises regularly.

### Environmental Protection

- **Casing and cement**: Proper casing and cementing isolates freshwater aquifers from hydrocarbon-bearing zones. Cement bond logs verify isolation quality.
- **Drilling waste management**: Drill cuttings and used mud must be contained, treated (solid separation, chemical neutralization), and disposed of properly. OBM cuttings require special handling due to oil content.
- **Spill prevention**: Secondary containment (berms, lined pits) around all tanks and production equipment. Spill response equipment (absorbent materials, containment booms) on site.
- **Produced water**: Water co-produced with oil (typically 3-10 barrels of water per barrel of oil in mature fields) must be treated before disposal or reinjection. Contains dissolved hydrocarbons, salts, and heavy metals. Reinjection into the producing formation is the preferred disposal method (also helps maintain reservoir pressure).

## Cross-References

- **Mining**: Drilling technology builds on mining's borehole expertise — [Mining](../mining/extraction.md)
- **Metals**: Steel for casing, drill pipe, and rig components — [Iron & Steel](../metals/iron-steel.md)
- **Steam power**: Powers early drilling rigs and modern EOR steam generation — [Steam Power](../energy/steam-power.md)
- **Refining**: Extraction provides the crude oil feedstock — [Petroleum Refining](refining.md)
- **Chemistry alternatives**: Coal tar and fermentation as petroleum-independent paths — [Petroleum & Alternative Chemistry](../chemistry/petroleum-alternatives.md)

---

*Part of the [Bootciv Tech Tree](../index.md) • [Petroleum Extraction & Refining](./index.md) • [All Domains](../index.md)*
