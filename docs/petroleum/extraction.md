# Crude Oil Extraction

> **Node ID**: petroleum.extraction
> **Domain**: [Petroleum Extraction & Refining](./index.md)
> **Dependencies**: `petroleum`
> **Enables**: [`petroleum.extraction.cable-tool`](./cable-tool.md),
> [`petroleum.extraction.rotary`](./rotary.md),
> [`petroleum.refining`](./refining.md)
> **Timeline**: Years 10-35
> **Outputs**: crude_oil, natural_gas_liquids, associated_gas
> **Critical**: No — petroleum provides the highest-value feedstock but coal tar and fermentation alternatives exist for some products

## Prerequisites

Petroleum extraction requires specific industrial capabilities:

- [Mining engineering](../mining/index.md) — drilling equipment, geological survey, and earth-moving
- [Iron and steel production](../metals/iron-steel.md) — drill pipe, casing, wellheads, and pumping equipment
- [Machine tools](../machine-tools/index.md) — precision-machined drill bits, pumps, and valves
- [Chemistry](../chemistry/index.md) — drilling mud formulation, cement for well completion

## Safety

Petroleum extraction presents severe hazards:

- **Hydrogen sulfide (H₂S)**: Present in "sour" crude oil and natural gas. Lethal at 100 ppm (0.01%) — causes respiratory paralysis. Detectable by rotten-egg odor at low concentration, but olfactory fatigue masks the smell at dangerous levels. Always use H₂S monitors in production areas. Escape respirators must be available at all well sites.
- **Blowout risk**: Uncontrolled release of pressurized oil and gas from a well. Blowout preventers (BOPs) rated to 5,000-15,000 psi are mandatory on all drilling rigs. A blowout can produce a fireball exceeding 50 m diameter if ignition occurs.
- **Benzene exposure**: Crude oil contains 0.1-3.0% benzene, a confirmed human carcinogen (leukemia). Limit skin contact and inhalation. Use closed sampling systems. Benzene TLV: 0.5 ppm (8-hour TWA).
- **Flash fire and explosion**: Hydrocarbon vapors (C₁-C₅) are flammable at 1-10% concentration in air. All electrical equipment in production areas must be explosion-proof (Class I, Division 1 or 2 rated). No open flames or spark-producing tools near wellheads.
- **Confined space entry**: Storage tanks, separators, and well cellars can contain oxygen-deficient atmospheres or toxic gases. Test atmosphere before entry, use supplied-air respirators, and maintain a standby rescue team.

## Why Extraction Matters

Crude oil is the highest energy-density liquid fuel readily available in nature (~42 MJ/kg) and the primary feedstock for the modern organic chemicals industry. Before petroleum, organic chemistry depended on coal tar (low yield, ~3-5% per tonne of coal) and fermentation (limited to ethanol, acetone, and a few other products). Petroleum provides orders of magnitude more aromatic and olefinic feedstock per unit effort. Without extraction capability, a civilization is limited to surface seeps — typically 5-50 liters/day — insufficient for industrial-scale fuel or chemical production.

The extraction progression follows a clear technological ladder: surface collection → cable-tool drilling → rotary drilling → enhanced recovery. Each step requires the tools and materials from the previous industrial stage.

## Natural Oil Seeps

Oil reaches the surface in many geological settings where an impermeable cap rock has been breached by erosion, faulting, or unconformity. Ancient civilizations from Mesopotamia to the Caspian collected petroleum from seeps for waterproofing, medicinal use, and lamp fuel.

**Collection methods**:
- **Hand-skimming**: Oil pooling on water surfaces in natural depressions. Skim with ladles or absorbent cloth. Yield: 5-50 liters/day per active seep.
- **Hand-dug wells**: Excavate 1-5 m deep pits where oil accumulates in porous sand or limestone. Line with stone or timber. Oil seeps in faster than from surface pools. Yield: 50-200 liters/day from a productive seep well.
- **Spring collection**: Where oil flows with water, dig a collecting pool. Oil floats on water (density ~0.82-0.95 g/cm³ vs. water at 1.0 g/cm³). Skim with ladles or overflow weirs that separate the lighter oil layer. This method powered the earliest commercial petroleum operations in Pennsylvania (1850s).

**Limitations**: Surface seeps represent only ~0.01-0.1% of total subsurface petroleum. Most oil is trapped in reservoirs beneath impermeable cap rock. To access this oil, you must drill.

**Quality**: Seep oil is typically weathered — lighter fractions (gasoline-range) have evaporated, leaving heavier, more viscous oil. Still suitable for distillation into kerosene, diesel, and fuel oil but yields less light fractions than fresh reservoir oil.

## Oil Sands and Heavy Oil

Where oil has migrated to the surface and degraded extensively (bacteria consume light fractions, leaving heavy residuum), the result is oil sands (tar sands) — a mixture of bitumen (~10-12% by weight), sand (~80-85%), and water (~4-5%). The Athabasca deposits in Canada and Orinoco belt in Venezuela represent enormous reserves.

**Surface mining**: Strip-mine oil sand deposits within 75 m of surface. Mine with power shovels and trucks. Crush and mix with hot water (50-80°C) and NaOH (0.1-0.5% as pH modifier) in a separation vessel. Bitumen attaches to air bubbles and floats as froth (Clark Hot Water Extraction Process). Froth diluted with naphtha and centrifuged to remove residual sand and water. Bitumen yield: ~90% recovery from mined ore. Energy cost: ~700-900 MJ per barrel of synthetic crude (high — energy return on investment ~3-5:1 vs. ~10-20:1 for conventional drilling).

**In-situ methods**: For deeper oil sands, steam-assisted gravity drainage (SAGD) injects steam through a horizontal well, reducing bitumen viscosity from ~10⁶ cP to ~10 cP at 200-250°C. Mobilized bitumen drains to a lower parallel production well and is pumped to surface. Requires ~2.5-3.5 barrels of steam per barrel of oil recovered.

## Cable-Tool Drilling

Cable-tool drilling uses a heavy chisel-shaped bit repeatedly lifted and dropped onto the rock, crushing a few millimeters per stroke. Cuttings are periodically bailed with a sand pump. Depth range 50-1,500 m, penetration rate 0.5-10 m/day. The technique requires minimal infrastructure — a wooden derrick, walking beam, steel cable, and a steam engine or animal power — making it the first drilling method suitable for bootstrapping subsurface petroleum access. Colonel Drake's 1859 well at Titusville used this method. For detailed rig components, step-by-step drilling procedure, bit selection, formation-specific behavior, and troubleshooting, see the dedicated article: **[Cable-Tool Drilling](cable-tool.md)**.

## Rotary Drilling

Rotary drilling uses a rotating bit with continuous drilling-mud circulation to cut rock, remove cuttings, cool the bit, and maintain hydrostatic pressure against formation fluids. Depth range 100-5,000+ m, penetration rate 10-100 m/day — dramatically faster and deeper than cable-tool. Rotary drilling handles all formation types and enables directional and horizontal wells (500-3,000 m lateral reach, 3-10× higher productivity than vertical wells). It replaced cable-tool for virtually all drilling above 500 m after the Spindletop discovery in 1901. The method requires steel drill pipe, mud pumps, blowout preventers, and substantial industrial infrastructure. For detailed rig components, mud engineering, step-by-step drilling and completion procedure, casing programs, directional drilling, and troubleshooting, see the dedicated article: **[Rotary Drilling](rotary.md)**.

## Natural Flow (Artesian)

If reservoir pressure exceeds the hydrostatic head of the oil column in the wellbore, oil flows to the surface unassisted. The driving force is reservoir pressure from compressed gas, water influx, or rock compaction. Flow rate depends on reservoir permeability, pressure differential, and oil viscosity.

**Productivity index**: Barrels per day per psi of pressure drawdown (difference between reservoir pressure and wellbore pressure). Typical range: 0.1-50 bbl/day/psi. High-permeability reservoirs have higher indices.

**Decline curve**: All wells decline over time as reservoir pressure depletes. Initial production rate may be 100-10,000 bbl/day; after 5-10 years, typical decline to 10-30% of initial rate. The exponential decline curve (q = qᵢ × e^(-Dt), where D is the decline rate) approximates most well behavior.

## Artificial Lift

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

| Recovery Method | Typical Recovery (% OOIP) | Incremental Over Primary | Key Cost Driver |
|---|---|---|---|
| Primary (natural flow + artificial lift) | 15-30% | — | Pump/maintenance energy |
| Waterflooding (secondary) | 25-45% | +10-20% | Water handling, injection pumps |
| Polymer flooding | 35-55% | +5-15% | Polymer cost ($2-5/kg HPAM) |
| Steam flooding / SAGD | 40-60% | +15-30% | Steam generation (natural gas) |
| CO2 miscible flooding | 35-55% | +8-16% | CO2 source and compression |
| In-situ combustion | 30-50% | +10-25% | Air compression (20-40 MW) |

## Waterflooding (Secondary Recovery)

Inject water into injection wells to maintain reservoir pressure and physically sweep oil toward production wells. The most widely applied EOR method — used in virtually all major fields after primary depletion.

**Process**: Convert some wells to injectors, continue producing from others. Water injected at 5-20 MPa displaces oil through the reservoir rock. Recovery: typically adds 10-20% of OOIP, for total primary + secondary recovery of 25-45%.

**Breakthrough**: Injected water eventually reaches production wells (water breakthrough), and produced fluid becomes increasingly water-cut. A mature waterflood may produce 95% water and 5% oil — still economic if oil price justifies the operating cost of handling large water volumes.

## Thermal Methods (Heavy Oil and Bitumen)

**Cyclic steam stimulation (CSS)**: Inject steam into a single well for days-weeks. Shut in for soak period (days, allowing heat to diffuse into the reservoir and reduce oil viscosity from ~10⁴-10⁶ cP to ~10-100 cP). Then produce back from the same well. Repeat cycles. Recovery: 15-25% of OOIP. Used extensively in California heavy oil and Venezuelan Orinoco belt.

**Steam flooding**: Continuous steam injection into dedicated injection wells, with oil driven to separate production wells. Recovery: 40-60% of OOIP in suitable reservoirs. Requires ~2-4 barrels of steam (as cold water equivalent) per barrel of oil recovered. Steam generation is the major energy cost — typically burns produced heavy oil or natural gas in boilers.

## Chemical and Miscible Methods (Tertiary Recovery)

**CO₂ flooding**: Inject CO₂ (compressed to supercritical or liquid state) into the reservoir. CO₂ dissolves in crude oil, swelling its volume and reducing viscosity. Also achieves miscible displacement — CO₂ and oil become a single phase, eliminating capillary forces that trap oil in pore spaces. Recovery: 10-20% additional OOIP. Requires a CO₂ source (natural CO₂ deposits, power plant flue gas capture, or ammonia plant byproduct). Widely used in the Permian Basin (West Texas).

**Polymer flooding**: Add water-soluble polymer (polyacrylamide, 250-1,500 ppm) to injection water. Increases water viscosity, improving the sweep efficiency (less water bypassing oil through high-permeability channels). Recovery: 5-15% additional OOIP over waterflooding alone.

## Environmental Protection

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

## See Also

- [Cable-Tool Drilling](cable-tool.md) — percussion drilling procedure and equipment
- [Rotary Drilling](rotary.md) — rotary drilling procedure, mud engineering, and well control
- [Petroleum Refining](refining.md) — crude oil distillation and cracking
- [Petrochemicals](petrochemicals.md) — chemical feedstocks from oil
- [Drilling](../mining/drilling.md) — rotary and cable-tool drilling methods
- [Mining Extraction](../mining/extraction.md) — resource extraction principles
- [Fuels](../energy/fuels.md) — combustion fuels from petroleum
- [Distillation](../chemistry/distillation.md) — separation processes

---
*Part of the [Bootciv Tech Tree](../index.md) • [Petroleum Extraction & Refining](./index.md) • [All Domains](../index.md)*
