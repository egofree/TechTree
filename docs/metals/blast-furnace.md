# Blast Furnace & Cast Iron Production

> **Node ID**: metals.iron-steel.blast-furnace
> **Domain**: [Metallurgy](./index.md)
> **Dependencies**: [`ceramics.kilns`](../ceramics/kilns.md), [`energy.fuels.coke`](../energy/coke.md), [`metals.iron-steel`](iron-steel.md)
> **Enables**: [`metals.steelmaking`](steelmaking.md)
> **Timeline**: Years 10-20
> **Outputs**: pig_iron, gray_cast_iron, white_cast_iron, malleable_iron, sand_castings

### Blast Furnace Operation

The blast furnace is the key advancement from bloomery smelting. Where a bloomery reduces iron ore below its melting point (producing solid bloom that must be consolidated), the blast furnace achieves temperatures high enough to fully melt the iron, producing liquid pig iron that can be cast directly. This is the critical transition from wrought iron to cast iron production.

**Construction**:
- **Shell**: Cylindrical shaft of stone or brick, typically 6-10 m tall, widening from throat (top, ~2 m diameter) to bosh (widest part, ~4 m diameter), then narrowing to the hearth (bottom, ~1.5 m diameter). The bosh angle (the outward slope of the walls) is critical — typically 20-25° from vertical — to allow the solid charge to descend as it shrinks during melting.
- **Tuyeres**: Water-cooled copper or cast iron nozzles near the bottom of the bosh, connected to a blowing engine (bellows or, later, steam-driven blower). Deliver preheated air blast into the furnace. Multiple tuyeres (4-8) evenly spaced around circumference for uniform blast distribution.
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

### Hot Blast Stoves

Preheating the blast air is the single most impactful energy efficiency improvement for blast furnace operation. The Cowper stove (invented by Edward Alfred Cowper, 1857) is a regenerative heat exchanger that captures heat from blast furnace gas and transfers it to the incoming blast air.

**Principle**: Refractory checker bricks are heated by burning blast furnace gas. When the bricks are hot, the gas flame is shut off and cold blast air is blown through the bricks in the reverse direction, picking up stored heat. This cyclic (regenerative) approach achieves blast temperatures of 1000-1250°C in modern installations.

**Construction**:
- Cylindrical steel shell (~6-10 m diameter, 25-40 m tall), lined with insulating brick internally. The interior is divided into a combustion chamber (one side) and a checker brick chamber (the remainder).
- **Checker bricks**: Silicon carbide or high-alumina bricks with rectangular gas passages (typically 30-60 mm flue width). Bricks are stacked in a regular grid pattern to maximize surface area while maintaining open flow channels. A large stove contains 500-1,000 tonnes of checker brickwork.
- **Dome**: The top of the stove is domed to distribute combustion gases evenly across the checker chamber.

**[Operating cycle](../glossary/operating-cycle.md)** (each stove alternates between two phases):
1. **[On-gas (heating) phase](../glossary/on-gas-heating-phase.md)** (20-45 minutes): Blast furnace gas (cleaned) is burned with combustion air in the combustion chamber. Hot combustion products (~1200-1400°C) pass downward through the checker bricks, heating them. Exhaust exits through the flue at the bottom at ~200-400°C.
2. **[On-blast (blowing) phase](../glossary/on-blast-blowing-phase.md)** (20-45 minutes): Cold blast air from the blower enters at the bottom of the checker chamber and flows upward through the now-hot bricks, absorbing stored heat. The heated air exits through the dome and is directed to the blast furnace tuyeres at 1000-1250°C.

**Stove arrangement**: A blast furnace has 3-4 stoves. With 3 stoves, typically two are on-gas (heating) while one is on-blast (supplying hot air), then they rotate. With 4 stoves, the sequencing can overlap more smoothly, providing more consistent blast temperature. Valving is critical — large butterfly or gate valves (1-2 m diameter) switch each stove between gas and blast duties.

**Fuel savings**: Preheating blast air to 1000-1250°C saves 20-30% of the coke that would otherwise be needed to achieve the same hearth temperature. This is because the blast air carries significant sensible heat into the combustion zone — roughly 25-35% of the total heat input to the furnace comes from the hot blast. Without stoves, coke consumption roughly doubles.

### Blast Furnace Gas Utilization

The gas exiting the top of the blast furnace (top gas, also called blast furnace gas or BFG) is a valuable fuel byproduct. Capturing and using this gas is essential for the energy economics of an integrated ironworks.

**[Top gas composition](../glossary/top-gas-composition.md)** (typical by volume):
- 20-30% CO (carbon monoxide — the combustible component)
- 1-5% H₂ (hydrogen — also combustible)
- 18-24% CO₂ (carbon dioxide — inert diluent)
- 48-55% N₂ (nitrogen — inert, from the blast air)
- Trace CH₄

**Calorific value**: 3-4 MJ/Nm³ (compared to ~38 MJ/Nm³ for natural gas). This is low-grade fuel — the high nitrogen and CO₂ content dilute the combustible CO and H₂. Despite the low heating value, the enormous volume produced (2,000-4,000 Nm³ per tonne of pig iron) makes BFG a significant energy resource.

**Gas cleaning**: Raw top gas contains 10-40 g/Nm³ of dust (fine ore particles, coke fines, soot). Before the gas can be burned, it must be cleaned:
1. **[Dust catcher](../glossary/dust-catcher.md)** (primary): Large cyclonic vessel where the gas velocity drops and coarse dust settles out by gravity and centrifugal force. Removes ~60-80% of the dust. The collected dust (flue dust) contains 30-50% iron and can be recycled to the sinter plant.
2. **[Venturi scrubber](../glossary/venturi-scrubber.md)** (secondary): Gas is accelerated through a constriction where water is injected. Fine particles are captured by water droplets. Removes ~95% of remaining dust. Gas exits at <0.05 g/Nm³ dust content. The water becomes acidic (dissolved CO₂ and traces of HCl, H₂S) and requires treatment before discharge.
3. **[Electrostatic precipitator (ESP)](../glossary/electrostatic-precipitator-esp.md)** (optional tertiary): For the cleanest gas, an ESP charges dust particles electrically and collects them on oppositely charged plates. Achieves <0.01 g/Nm³. Required if gas is used in gas turbines.

**Utilization**:
- **Hot blast stove fuel**: The primary consumer of BFG — the stoves burn it to heat checker bricks as described above. This creates a closed energy loop: the furnace produces gas, which is used to preheat the blast air for the same furnace.
- **Steam raising**: BFG is burned in boilers to generate steam for blast engine drives, turbo-blowers, or electricity generation. The low calorific value requires specially designed burners with stable flame holders.
- **Electricity generation**: In modern integrated steelworks, BFG fuels gas turbines or steam turbines for on-site power generation. A large blast furnace (producing 10,000 tonnes/day pig iron) generates enough BFG to produce 50-100 MW of electricity — covering much of the steelworks' internal power demand.
- **Sinter plant fuel**: BFG can supplement or replace coke breeze in the sintering ignition hood.

**Gas holder**: A large gasholder (50,000-200,000 Nm³ capacity) buffers the variable production rate of BFG against the variable demand of its consumers. Without buffering, mismatches between furnace gas production and stove/boiler demand would require flaring (wasting the gas).

### Slag Processing and Utilization

Blast furnace slag is the non-metallic byproduct formed when limestone flux reacts with silica and alumina gangue from the iron ore. A blast furnace produces 250-400 kg of slag per tonne of pig iron — roughly 0.25-0.4 tonnes of slag for every tonne of iron. This is a massive material flow that must be managed, and processed slag has significant commercial value.

**[Slag composition](../glossary/slag-composition.md)** (typical): 30-45% CaO, 30-40% SiO₂, 5-15% Al₂O₃, 1-10% MgO, with minor amounts of FeO, MnO, and sulfur (as CaS). The CaO/SiO₂ ratio (basicity) is typically 1.0-1.3.

**Processing routes**:

1. **Air-cooled slag**: Molten slag is directed into shallow pits and allowed to cool and solidify slowly in air. The resulting rock-like mass is crushed and screened to produce aggregate (20-75 mm) for road base, railroad ballast, and concrete aggregate. Air-cooled slag aggregate is denser (~2.5 t/m³) and more angular than natural gravel, providing excellent interlock in road construction. It is free of organic matter and has good frost resistance.

2. **Granulated blast furnace slag (GBFS)**: Molten slag is directed through a water jet into a granulation tank. The rapid quenching with high-pressure water shatters the slag into sand-sized particles (0-5 mm) of predominantly glassy (amorphous) structure. The quenching prevents crystallization — the resulting glassy granules have latent hydraulic properties (they react with water and calcium hydroxide to form cementitious compounds). Granulated slag is ground to a fine powder (~400-500 m²/kg Blaine fineness) to produce **ground granulated blast furnace slag (GGBFS)**, which is used as a partial replacement for Portland cement (typically 30-70% substitution). GGBFS concrete has improved long-term strength, reduced heat of hydration, and greater resistance to sulfate attack and alkali-silica reaction. Water granulation requires 8-10 m³ of water per tonne of slag — most of which is recycled.

3. **Pelletized slag (expanded slag)**: Molten slag is treated with a limited amount of water on a rotating drum, producing partially expanded pellets that are then cooled in air. The resulting lightweight aggregate (bulk density 0.7-1.1 t/m³) is used in lightweight concrete blocks and structural concrete where weight reduction is desired. The pelletizing process uses less water than granulation and produces a product that requires no crushing.

4. **Slag wool**: Molten slag can be fiberized by spinning or steam jetting to produce mineral wool (rock wool / slag wool) insulation. The fibers (3-10 μm diameter, 20-100 mm long) are collected on a conveyor, bonded with phenolic resin, and formed into batts, boards, or loose-fill insulation. Slag wool insulation is non-combustible, provides both thermal and acoustic insulation, and is widely used in building construction and industrial insulation. This is one of the oldest value-added uses of blast furnace slag, dating to the 1840s.

### Modern Blast Furnace Operation

Modern blast furnaces have evolved far beyond the charcoal-fired shafts of the early industrial era. Today's large blast furnaces are computer-controlled, continuously monitored, and optimized for fuel efficiency, production rate, and campaign life.

**Pulverized Coal Injection (PCI)**: The most significant modern fuel efficiency improvement. Pulverized coal (particle size <75 μm, 80% passing 75 μm) is injected through the tuyeres using a carrier gas (nitrogen or compressed air). PCI replaces 30-50% of the coke in the furnace burden, dramatically reducing coke consumption. Injection rates of 150-250 kg coal per tonne of hot metal are standard; the best plants achieve 200-250 kg/t with coke rates of 250-300 kg/t (compared to 500+ kg/t without injection). The injected coal undergoes combustion and gasification in the raceway (the cavity in front of each tuyere), producing CO and H₂ that participate in ore reduction. High-volatile bituminous coals are preferred for their ease of grinding and good combustion characteristics.

**Burden distribution control**: The way raw materials are charged to the top of the furnace critically affects gas flow, reduction efficiency, and smooth operation. Modern furnaces use either:
- **Bell-less top (Paul Wurth type)**: A rotating chute in the furnace throat distributes materials in programmed patterns (rings, spirals, sectors). The chute angle and rotation speed are computer-controlled, allowing precise layering of ore and coke. This is the dominant system on furnaces built after 1970.
- **[Double-bell system](../glossary/double-bell-system.md)** (older): An inner bell and outer bell seal the furnace during charging. The charge is dumped from skips into the receiving hopper, the inner bell opens to drop material onto the distributing bell, then the distributing bell opens to drop the charge into the furnace. Less precise than bell-less top but mechanically simpler.

The key control objective is maintaining a **[central gas flow](../glossary/central-gas-flow.md)** — a slightly more open column of material in the center of the furnace that allows gas to channel upward, while maintaining sufficient ore at the walls to protect the refractory lining from excessive heat. Burden distribution is adjusted continuously based on temperature probes above the burden surface and shaft temperature profiles.

**Process control and instrumentation**:
- **Top gas analysis**: Continuous measurement of CO, CO₂, H₂, and N₂ in the top gas. The CO/CO₂ ratio indicates reduction efficiency. Rising CO₂% means better gas utilization.
- **Shaft temperature probes**: Multiple thermocouples at different heights and radial positions in the furnace shaft. Abnormal temperatures indicate channeling (gas finding preferential paths), hanging (material sticking to walls), or slipping (sudden material drops).
- **Tuyere cameras**: Water-cooled cameras inserted through the tuyeres provide visual observation of the raceway — the combustion zone in front of each tuyere. Operators can see coal injection combustion, tuyere condition, and raceway cavity size.
- **Hearth liquid level**: Measured by electrical resistance probes or radioactive tracers. Critical for safe tapping — if liquid iron rises too high, it can contact and damage the tuyeres.
- **Wall temperature and heat flux**: Thermocouples embedded in the furnace lining monitor refractory wear. Increasing wall temperatures at specific locations indicate lining thinning and approaching end-of-campaign.

**Campaign life**: Modern blast furnace campaigns (the period between major relinings) last 10-20 years. A campaign ends when the refractory lining in the hearth or bosh has worn to the point where it must be replaced to avoid a breakoff (catastrophic shell failure due to molten metal contact). Campaign life depends on cooling system effectiveness, lining quality (carbon blocks, ceramic cups), and operating practice (avoiding thermal cycling). A relining requires 3-6 months of downtime and costs $100-300 million for a large furnace. During the campaign, minor repairs (tuyere replacement, gunning of worn lining sections) are performed during brief maintenance stops.

### Sintering and Pelletizing

Iron ore as mined is rarely suitable for direct charging to a blast furnace. The ore must be agglomerated into larger, stronger, and more uniform pieces that maintain permeability in the furnace shaft and have consistent composition. Two processes dominate: sintering and pelletizing.

**Sintering**:
- A continuous process that partially fuses fine iron ore particles into a porous, clinker-like mass (sinter), which is then crushed and screened to produce 5-40 mm charge material.
- **Process**: A moving strand (traveling grate) — a continuous conveyor of pallets with grate bars — carries a bed of raw material (~400-600 mm deep) under an ignition hood. The ignition hood (fueled by blast furnace gas or natural gas) ignites the top of the bed. A suction fan draws air downward through the bed, and a combustion front propagates downward through the material as a self-sustaining wave.
- **Feed mix**: Fine iron ore (0-8 mm), coke breeze (3-5% of mix as fuel), limestone and dolomite (flux), return fines (undersize sinter recycled to the feed), and sometimes steelmaking dust and sludge (recycling iron-bearing wastes).
- **Temperature**: The combustion front reaches 1250-1350°C — hot enough to partially melt the ore particles at their contact points, fusing them together. Below the combustion front, the material cools as suction air passes through.
- **Product**: Sinter with 45-60% porosity, providing good reducibility in the blast furnace. Typical Fe content: 55-60% (after accounting for flux and fuel additions). The sinter is crushed, screened (undersize returns to the feed), and the 5-40 mm fraction is charged to the blast furnace.
- **Capacity**: A single sinter strand produces 200-1,000 tonnes/hour. Most integrated steelworks have 1-3 sinter machines.
- **Environmental concern**: Sinter plants are a major source of dust, SO₂, NOx, and dioxin emissions. Modern plants use electrostatic precipitators, baghouses, and flue gas desulfurization to control emissions.

**Pelletizing**:
- Produces uniform, spherical pellets (9-16 mm diameter) from very fine iron ore concentrate (<0.15 mm, typically from taconite or magnetite beneficiation).
- **Process steps**:
  1. **Grinding**: Ore is ground in ball mills to ~80% passing 45 μm — fine enough that each pellet contains millions of particles pressed into close contact.
  2. **Balling**: The ground concentrate is mixed with ~0.5-1.0% bentonite clay (as binder) and 8-10% moisture, then fed to rotating drum or disc pelletizers. The rotation causes the moist particles to roll and grow into spherical green pellets (9-16 mm).
  3. **Induration (firing)**: Green pellets are too weak for blast furnace use. They must be fired at high temperature to develop permanent bonding between particles. Three furnace types are used:
     - **Straight-grate (traveling grate)**: Pellets travel on a moving grate through drying, preheating, firing (1250-1350°C), and cooling zones. Suction fans pull hot gases through the pellet bed. Most common for hematite pellets.
     - **Grate-kiln**: Pellets are first dried and preheated on a traveling grate, then transferred to a rotary kiln for firing at 1250-1350°C. The kiln provides uniform heating and good temperature control. Widely used for both hematite and magnetite pellets.
     - **Shaft furnace**: Pellets descend through a vertical shaft countercurrent to hot gases. The oldest pelletizing furnace, now mostly replaced by larger-capacity grate and grate-kiln systems.
  4. **Cooling**: Fired pellets are cooled by forced air to below 150°C before storage and transport.
- **Product**: Uniform, hard, spherical pellets with 65%+ Fe content (higher than sinter because pellets are made from beneficiated concentrate with less gangue). Pellets have excellent permeability in the blast furnace due to their uniform size and shape, and their high iron content reduces slag volume and coke consumption.
- **Comparison with sinter**: Sintering handles coarser fines and is cheaper per tonne. Pelletizing produces higher-grade feed and is better suited to low-grade ores that require fine grinding and beneficiation. Many blast furnaces operate on a blend of sinter, pellets, and lump ore.

### Direct Reduced Iron (DRI)

Direct reduction is an alternative to the blast furnace that produces solid iron (sponge iron) without melting the ore. DRI is an important supplementary ironmaking route and a potential stepping stone in the bootstrap sequence — it requires lower capital investment and lower operating temperatures than a blast furnace, though it cannot match blast furnace scale.

**Principle**: Iron ore (in lump or pellet form) is reduced to metallic iron at 800-1050°C by a reducing gas (CO + H₂) or solid carbon (coal). The temperature is well below iron's melting point (1538°C), so the product is a porous solid — sponge iron — that retains the physical shape of the original ore lump or pellet but has been chemically converted from iron oxide to metallic iron.

**Product characteristics**: DRI typically contains 90-95% total Fe (of which 80-95% is metallic iron, the remainder is unreduced FeO). It also contains 1-4% carbon (from the reducing gas) and the gangue minerals from the original ore. DRI is highly porous (~50-70% porosity) and has a large surface area — making it ideal as feedstock for electric arc furnaces (EAF), where it melts readily and dilutes residuals in scrap-based charges.

**[MIDREX process](../glossary/midrex-process.md)** (dominant, ~60% of global DRI):
- Uses natural gas as the reducing agent feedstock. Natural gas is reformed (partially oxidized with CO₂ or H₂O from the process) to produce a reducing gas mixture of ~55-65% H₂ and 25-35% CO.
- The reducing gas is fed to a vertical shaft furnace at ~800-950°C. Iron oxide pellets or lump ore descends by gravity through the shaft countercurrent to the rising reducing gas.
- **[Reduction zone](../glossary/reduction-zone.md)** (upper shaft): Fe₂O₃ + H₂/CO → Fe + H₂O/CO₂. The gas progressively reduces the ore as it ascends.
- **[Transition zone](../glossary/transition-zone.md)** (middle): A cooling gas can be introduced to control product temperature and carburization.
- **[Discharge zone](../glossary/discharge-zone.md)** (bottom): DRI is continuously discharged. It can be hot-charged directly to an EAF (hot DRI at ~600-700°C, saving ~100 kWh/t of EAF electricity) or cooled and stored for later use.
- **Capacity**: Single MIDREX modules range from 500,000 to 2,500,000 tonnes DRI per year.

**HYL / Energiron process**:
- Similar shaft furnace concept but operates at higher pressure (4-6 bar vs. ~1 bar for MIDREX). The higher pressure increases reduction kinetics and allows a more compact furnace.
- Natural gas is reformed in an external reformer or used directly (auto-reforming within the shaft).
- Produces DRI with higher carbon content (up to 4-5% C) compared to MIDREX (~1-3% C). Higher carbon acts as a fuel in the EAF, reducing electricity consumption.
- The HYL process can also produce hot briquetted iron (HBI) — DRI that has been compacted at ~700°C into briquettes (~100 × 50 × 30 mm) using a roller press. HBI is much less reactive than loose DRI (lower surface area), making it safer and easier to transport and store.

**[Rotary kiln DRI](../glossary/rotary-kiln-dri.md)** (coal-based, used in India):
- Uses non-coking coal as both the reductant and the fuel. Iron ore and coal are fed into a slowly rotating inclined kiln (3-5 rpm, 2-5° inclination).
- Air is injected along the kiln length to burn the volatile matter and partially combust the coal, providing heat. The coal char provides the reducing agent (C + CO₂ → 2CO; CO reduces the ore).
- Operating temperature: 950-1050°C. Must be carefully controlled below the sticking temperature (~1050-1100°C) where iron particles begin to fuse together and form rings on the kiln wall.
- Product: 80-90% metallized sponge iron with significant gangue content (since no melting occurs to separate gangue). Suitable for EAF or induction furnace melting.
- Smaller scale (30,000-150,000 tonnes/year per kiln) but does not require natural gas — an advantage in regions with abundant coal and limited gas infrastructure.

**DRI safety**: Fresh DRI is pyrophoric — the high surface area of porous metallic iron reacts exothermically with oxygen and moisture. Loose DRI can self-heat, ignite, and even explode if exposed to water after significant oxidation (the hydrogen produced is explosive). Mitigation: passivate with controlled air exposure before storage, store under inert atmosphere, convert to HBI for transport, or hot-charge directly to EAF.

**Bootstrap relevance**: A small DRI shaft furnace or rotary kiln is technically achievable at a smaller scale and lower capital cost than a blast furnace. It does not require coke (coal-based rotary kiln) or high-temperature refractory (no molten iron contact). However, DRI production rates per unit are much lower than blast furnaces, and the gangue remains in the product (requiring slag-forming fluxes in the subsequent melting step). For a bootstrap civilization, DRI may serve as an intermediate step between bloomery iron and full blast furnace ironmaking.

### Safety & Hazards

- **Molten metal contact**: Pig iron and cast iron melt at 1150-1250°C. Splash from tapping or pouring causes catastrophic burns — molten iron retains enough heat to ignite clothing and burn through leather. Full protective equipment: face shield, leather apron, leggings, aluminized coat, spats over boots. Never stand directly in front of tap hole when opening. Keep pouring area dry — water on floor turns to steam explosively on contact with molten metal.
- **Carbon monoxide**: Blast furnace produces large volumes of CO in the off-gas (20-30% CO). CO is colorless, odorless, lethal. Ensure furnace area is open-air or well-ventilated. Monitor with CO detectors if working indoors. Historical blast furnaces had open tops and natural draft; modern enclosed tops require gas handling systems.
- **Tuyere blowback**: If tuyeres become blocked and pressure builds, removing a blockage can cause a blowback of hot gas and particles. Stand to one side when clearing tuyeres. Wear face shield and heavy gloves.
- **Sand dust (silica)**: Molding sand contains fine silica. Chronic inhalation causes silicosis (progressive, irreversible lung disease). Wet sand during mixing to minimize airborne dust. Use local exhaust ventilation at sand mixing and shakeout stations. Wear respirators during mold making and shakeout operations.
- **Heavy lifting**: Ladles of molten iron are extremely heavy. A 100 kg ladle of iron weighs ~200 kg including the ladle itself. Use proper mechanical lifting equipment (overhead crane, jib crane) for all ladle work. Never carry a full ladle manually.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Metals](./index.md) • [All Domains](../index.md)*
