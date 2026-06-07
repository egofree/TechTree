# Salt / Halite Production

> **Node ID**: mining.salt
> **Domain**: [Mining](./index.md)
> **Dependencies**: [`Food Processing`](../food-processing/index.md), [`Electrolysis`](../chemistry/electrolysis.md)
> **Enables**: [`Energy`](../energy/index.md)
> **Timeline**: Years 1-10
> **Outputs**: salt, brine, rock-salt
> **Critical**: No

## Overview

Extraction of halite (rock salt) and brine from underground deposits, salt pans, and seawater evaporation. Salt is essential for food preservation, chlor-alkali electrolysis (chlorine and caustic soda), and as a chemical feedstock. Enables the foundational inorganic chemistry of the industrial revolution.

This technology is characteristic of the Stone Age era of industrial development. It builds on earlier foundational techniques while enabling more precise and controlled manufacturing outcomes.

Primary outputs: `salt`, `brine`, `rock-salt`. These materials or products serve as inputs for downstream manufacturing and processing steps.

Salt is one of the few minerals that humans consume directly in large quantities. Beyond its role as a flavoring agent, salt preserves meat and fish by drawing out moisture and inhibiting bacterial growth — without refrigeration, salting is the primary long-term food preservation method. Industrially, salt feeds the chlor-alkali process (electrolysis of brine to produce chlorine gas and sodium hydroxide), which underpins bleaching, disinfection, and much of the chemical industry. Salt also serves as a raw material for soda ash (sodium carbonate) production via the Solvay process.

Historically, salt was so economically important that it served as currency (the word "salary" derives from the Roman practice of paying soldiers in salt). Control of salt production and trade was a major source of political power.

## Prerequisites

### Materials

- **Seawater or brine** — the primary raw material for evaporation methods. Seawater contains ~3.5% dissolved salts (predominantly NaCl). Brine springs may be much more concentrated.
- **Fuel (for boiling methods)** — wood, coal, or peat for heating brine pans. Fuel consumption is substantial — boiling off 1,000 liters of brine to recover ~260 kg of salt requires burning roughly equivalent energy in fuel.
- **Clay or stone** — for lining evaporation ponds and constructing boiling pans. Clay-lined ponds prevent brine from seeping into the ground.

### Equipment

- **Evaporation ponds**: Shallow, clay-lined basins with controlled inlet and outlet channels. Series of ponds at increasing salinity (concentrators leading to crystallizers). Gravity flow between ponds where possible.
- **Boiling pans**: Large flat iron or ceramic pans over fire hearths. Iron pans conduct heat better and last longer; ceramic pans are available at lower technology levels.
- **Rakes and hoes**: Wooden or iron tools for harvesting crystallized salt from pond bottoms.
- **Hydrometer**: Glass or sealed reed float for measuring brine density (specific gravity).
- **Storage**: Covered, dry storage for finished salt. Salt absorbs moisture from humid air. Wooden bins or sealed clay containers.
- [Food Processing](../food-processing/index.md) — material dependency
- [Electrolysis](../chemistry/electrolysis.md) — material dependency

### Downstream Applications

Salt produced by these methods serves three primary purposes in a bootstrap civilization:

1. **Food preservation**: Salting meat and fish at 10-20% concentration prevents bacterial growth for months. The most energy-efficient food preservation method available at any technology level.
2. **Chemical feedstock**: Electrolysis of brine produces chlorine gas (bleaching, disinfection, water treatment) and sodium hydroxide (soap making, paper pulping, chemical manufacturing). The chlor-alkali process is the gateway to industrial inorganic chemistry.
3. **Iodization**: Adding potassium iodide at 20-40 mg per kg of salt prevents iodine deficiency disorders (goiter, cretinism) — the simplest public health intervention available. Requires only trace amounts of KI and basic mixing equipment.

### Knowledge

- Understanding of brine concentration and saturation behavior — how salt precipitates at different concentration levels
- Familiarity with pond management for solar evaporation — flow rates, pond depth, and crystallizer timing
- Ability to assess salt purity by taste, appearance, and simple dissolution testing
- Safety training for underground mining operations (where applicable) and brine boiling hazards
- Understanding of seasonal effects on evaporation rates and production planning

### Infrastructure

- **Evaporation pond system** (solar method): Series of shallow clay-lined ponds with intake channels from the sea or brine source, interconnected by gravity-flow channels, and a final crystallizer pond for harvesting. Land requirement: hectares for production-scale output.
- **Boiling house** (boiling method): Building with fire hearths and ventilation flues for brine evaporation. Fuel storage area. Drainage for spent brine.
- **Mine infrastructure** (rock salt): Shaft access, ventilation, haulage, and groundwater pumping. Similar to conventional mining operations.
- **Dry storage**: Covered warehouse with raised floor. Salt must be kept dry from production through to end use.

## Deposit Grades and Geology

Salt deposits occur in three main geological settings, each with different NaCl grades and extraction requirements:

| Deposit Type | NaCl Grade | Depth | Typical Thickness | Extraction Method |
|-------------|-----------|-------|-------------------|-------------------|
| Marine evaporite beds | 90-98% | 100-1,500 m | 5-400 m | Room-and-pillar mining or solution mining |
| Salt domes (diapirs) | 95-99% | 100-5,000 m | 100-2,000 m diameter | Solution mining or Frasch-type |
| Sabkha / salt flats | 80-95% | Surface to 5 m | 0.5-3 m | Surface scraping, solar evaporation |
| Seawater | 3.5% (2.7% NaCl) | Surface | N/A | Solar evaporation ponds |
| Brine springs | 5-26% NaCl | Surface seeps | N/A | Boiling or solar evaporation |

Bedded salt deposits form when ancient seas evaporated in restricted basins, leaving layered sequences of halite (NaCl), anhydrite (CaSO₄), and potash minerals. Salt domes form when buried salt layers, being less dense than overlying rock, flow upward in cylindrical plugs. These domes often cap oil and gas reservoirs, making them geologically significant beyond salt production.

**Impurities by deposit type**: Bedded salt contains interbedded anhydrite layers (2-15% of sequence thickness), clay seams (1-5%), and occasionally potash salts (sylvite KCl, carnallite KMgCl₃·6H₂O). Salt domes are purer but may contain entrained anhydrite cap rock at the top. Seawater-derived salt contains MgCl₂ (~0.5%), MgSO₄ (~0.3%), CaSO₄ (~0.1%), and KCl (~0.1%) as co-crystallizing impurities that affect taste and hygroscopic behavior.

## Process Description

Salt extraction varies dramatically by deposit type and geography. The three principal methods — seawater evaporation, solution mining, and rock salt mining — each suit different geological settings and technology levels.

### Step-by-Step Procedure

1. Survey the site to confirm presence and concentration of the target material. Document geological conditions. Coastal sites for solar evaporation; inland salt flats or brine springs for pan evaporation; geological survey for underground deposits.
2. Prepare the extraction site: clear vegetation, establish drainage, set up equipment. Install safety barriers for underground operations.
3. Begin extraction using the method appropriate to deposit type and depth:
   - **Solar evaporation (coastal)**: Draw seawater into a series of shallow, interconnected ponds. Pond depth: 15-30 cm in concentrators, 10-20 cm in crystallizers. As water evaporates under sun and wind, salt concentration increases through successive ponds: seawater at 3.5% → concentrator ponds reach 15-20% → pre-crystallizer at 25% → crystallizer at 26-28% saturation. In the final crystallizer pond, salt crystals precipitate and settle to the clay-lined bottom at a rate of roughly 25-50 mm of crystal per month. Harvest by raking crystals to the edge and draining remaining brine. Requires warm, dry climate with consistent wind, ideally >2,000 mm/year evaporation exceeding rainfall. Cycle time: 3-6 months from intake to harvest in tropical climates, longer in temperate regions. Multiple ponds allow continuous production: a 10-pond system with staggered start dates produces salt every 2-3 weeks.
   - **Solution mining (brine wells)**: Drill or dig a borehole into a salt deposit (typically 100-500 m deep for bedded deposits). Casing diameter: 150-300 mm. Inject water down a central pipe; dissolved brine (26% NaCl) returns up the annular space between the pipe and borehole wall. A single well produces 20-100 m³/hour of saturated brine. Boil the brine in iron or ceramic pans (2-4 m diameter, 15-25 cm depth) over a fire to evaporate the water, leaving crystalline salt. Fuel consumption: approximately 4-5 tonnes of wood per tonne of salt produced, or 1.5-2 tonnes of coal per tonne. Vacuum evaporation (higher technology) reduces fuel consumption to 0.3-0.5 tonnes steam per tonne of salt. This method accesses deep salt beds without excavating solid rock.
   - **Rock salt mining**: When salt deposits form solid underground layers (bedded deposits or salt domes), mine the solid rock salt directly using room-and-pillar techniques (see Underground Mining section below). The mined salt typically grades 90-98% NaCl. Crush the mined rock salt and purify by dissolving and re-crystallizing if higher purity is needed. Alternatively, use the rock salt directly for road de-icing and industrial applications where purity is less critical.
4. Process extracted material through crushing, washing, or re-crystallization to concentrate the product and remove impurities.
5. Transport processed material to storage. Record yield and quality for each batch.
6. Rehabilitate the site as operations progress — backfill, regrade, revegetate.

### Extraction Methods Comparison

| Method | Deposit Type | Energy Required | Purity | Climate Dependency |
|--------|-------------|----------------|--------|-------------------|
| Solar evaporation | Seawater | Sunlight only | Moderate (95-98%) | High — needs sun and wind |
| Solution mining + boiling | Underground salt bed | High (fuel for boiling) | High (99%+) | None |
| Rock salt mining | Solid salt deposit | Moderate (drilling, hauling) | Low to moderate (90-98%) | None |
| Salt pan evaporation (inland) | Brine springs | Sunlight + some fuel | Moderate (95-98%) | Moderate |

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Seawater salinity | ~3.5% (35 g/L) | Varies by location; higher in arid coastal regions (Red Sea ~4.0%) |
| Brine saturation | ~26% NaCl by weight (360 g/L) | Point at which crystallization begins |
| Solar evaporation rate | 5-12 mm/day in arid tropics | Hot, dry, windy conditions optimal; negligible in humid climates |
| Boiling pan temperature | 100-106°C (brine boiling point elevated by dissolved salt) | Fuel-intensive; wood or coal consumption high |
| Crystal size | 1-10 mm (slow), 0.1-1 mm (rapid boiling) | Slow evaporation = larger, purer crystals; rapid boiling = fine grains |
| Salt recovery from seawater | ~25 kg/m³ of seawater | Theoretical maximum; actual yield 20-23 kg/m³ with losses |
| Solution mining brine flow | 20-100 m³/hour per well | Depends on deposit permeability and water injection pressure |

## Underground Rock Salt Mining

Rock salt mining uses room-and-pillar methods. Salt is relatively soft (Mohs hardness 2-2.5) and can be cut with continuous mining machines or broken by drilling and blasting. The plasticity of salt under geological pressure requires wider pillars than hard-rock mining to prevent creep closure.

### Shaft and Tunnel Dimensions

| Parameter | Small Mine (<50,000 t/year) | Medium Mine (50,000-500,000 t/year) | Large Mine (>500,000 t/year) |
|-----------|:--------------------------:|:-----------------------------------:|:---------------------------:|
| Shaft diameter | 3-4 m (single) | 4-6 m (single or dual) | 6-8 m (dual shafts) |
| Shaft depth | 50-200 m | 100-500 m | 200-1,000+ m |
| Room width | 8-12 m | 12-20 m | 15-25 m |
| Room height | 3-5 m | 4-8 m | 5-10 m |
| Pillar width | 8-15 m | 15-25 m | 20-30 m |
| Pillar extraction ratio | 50-60% | 55-65% | 60-70% |
| Main entry dimensions | 4×4 m | 5×5 m | 6×6 m |
| Haulage roadway width | 3-4 m | 4-5 m | 5-6 m |

Pillar width must be at least equal to room width in salt mines because salt creeps under load. A pillar that is too narrow will deform plastically over months to years, narrowing the room and eventually collapsing. The extraction ratio (percentage of salt removed) is conservative compared to hard-rock mining: typically 55-65% compared to 70-80% in limestone or metal mines.

### Ventilation Calculations

Underground salt mines require mechanical ventilation to dilute dust, remove diesel equipment exhaust, and provide breathable air. Salt dust is not toxic but irritates respiratory passages at concentrations above 5 mg/m³.

**Airflow calculation**: Total airflow (m³/s) = Σ (equipment diesel power × 0.04 m³/s per kW) + (personnel × 0.1 m³/s per person) + (blasting fume clearance × additional volume).

Example for a medium mine with two 100 kW diesel trucks, 20 workers, and periodic blasting:

- Diesel equipment: 2 × 100 kW × 0.04 = 8.0 m³/s
- Personnel: 20 × 0.1 = 2.0 m³/s
- Blasting clearance: 5.0 m³/s (purge volume)
- **Total required airflow: ~15 m³/s** (900 m³/min)

Fan selection: a 15 m³/s system with 500 Pa static pressure requires approximately 10 kW fan power. Use a single main fan at the shaft head with a backup. Air flows down the intake shaft, through the working faces, and up the return shaft. In a single-shaft mine, a divider wall (brattice) splits the shaft into intake and return halves.

**Ventilation ducting**: Flexible ducting (600-1,000 mm diameter, fabric-reinforced) carries air from the main shaft to individual working faces. Maximum duct run: 200-300 m per fan. Beyond this distance, auxiliary fans boost airflow.

### Roof Support

Salt is self-supporting over short spans (up to 10-12 m) at moderate depth (<300 m) because its plastic behavior allows stress redistribution. At greater depth or wider spans, systematic roof support is required:

| Roof Condition | Support Type | Spacing | Bolt Length | Bolt Diameter |
|---------------|-------------|---------|-------------|---------------|
| Sound salt, depth <200 m | None or spot bolts | As needed | 1.5-2.0 m | 20 mm |
| Sound salt, depth 200-500 m | Pattern bolts | 1.2-1.5 m grid | 2.0-2.5 m | 22 mm |
| Fractured roof or clay seams | Pattern bolts + mesh | 1.0-1.2 m grid | 2.0-3.0 m | 22-25 mm |
| Wide intersections (>15 m) | Cable bolts | 1.5-2.0 m grid | 4.0-6.0 m | 15.2 mm strand |
| Long-term stable openings | Shotcrete (50-100 mm) + bolts | Combined | As above | As above |

Roof bolts in salt mines use resin-anchored or mechanical-point anchors. The bolt must extend past the immediate roof layer into competent salt above. In layered deposits with clay or anhydrite partings, bolt length must cross at least one competent layer above the nearest parting. Bolt tension: 50-80 kN for 22 mm diameter bars. Torque to achieve this: 200-300 Nm with a standard nut.

Monitoring: install convergence pins (reference points) at 30-50 m intervals along entries. Measure distance between floor and roof pins weekly. Convergence rate should be <1 mm/day in stable openings. Rates exceeding 3 mm/day indicate pillar overload and require immediate room closure or pillar widening.

## Safety Considerations

This process involves specific hazards requiring trained personnel and protective measures:

- **Cave-ins**: Underground rock salt mining shares all the structural hazards of conventional mining. Salt is relatively plastic under geological pressure — rooms may close over time. Maintain generous pillar dimensions.
- **Salt dust inhalation**: Rock salt mining and crushing produce fine salt dust. Prolonged inhalation irritates respiratory passages. Mechanical ventilation required for underground operations.
- **Brine flooding**: Underground salt is soluble. Water intrusion into a salt mine dissolves the walls and floor, potentially causing rapid flooding. Monitor for water ingress constantly.
- **Thermal burns**: Brine boiling operations involve open fires and hot concentrated brine. Salt splatter at high temperature causes severe burns.
- **Sun exposure and heat**: Solar evaporation ponds are typically in hot, arid climates. Workers face heat exhaustion and severe sun exposure during pond maintenance and salt harvesting.

### Gas Detection and Monitoring (Underground Mines)

Underground salt mines are not typically gassy (salt deposits do not contain methane like coal), but diesel equipment exhaust and blasting fumes create respiratory hazards:

- **Diesel particulate**: Continuous diesel equipment operation raises particulate levels. Monitor with a personal aerosol sampler. Limit: <1 mg/m³ (8-hour TWA). Control with exhaust scrubbers on diesel equipment and adequate ventilation.
- **Carbon monoxide**: Produced by diesel engines and blasting. CO is odorless; use chemical indicator tubes or electronic CO sensors. Alarm threshold: 30 ppm (8-hour TWA), evacuate at 100 ppm. A battery-powered CO sensor at each working face costs little and saves lives.
- **Nitrogen oxides (NOₓ)**: Produced by diesel engines and blasting. Causes lung irritation and pulmonary edema at high concentrations. Detection: indicator tubes change color in NOₓ presence. Limit: 5 ppm (NO₂, 8-hour TWA). If the air smells sharp or irritates the throat after a blast, NOₓ levels are too high. Wait 30 minutes after blasting before re-entering the face, with ventilation running.
- **Oxygen deficiency**: In poorly ventilated dead-end headings, oxygen can drop below 19.5%. This happens silently. A flame safety lamp (Davvy lamp) or electronic O₂ sensor detects low oxygen. If the flame dims or extinguishes, evacuate immediately.
- **Hydrogen sulfide (H₂S)**: Occasionally encountered near sulfur-bearing salt deposits. Rotten egg smell at low concentration; deadens sense of smell at higher concentrations. Use chemical indicator tubes. Alarm threshold: 10 ppm. Evacuate at 50 ppm.

**Monitoring protocol**: Check air quality at each working face at the start of each shift and after blasting. Record readings. Train all workers to recognize the signs of poor air: headaches, dizziness, shortness of breath, or unusual tiredness. Any worker feeling these symptoms should move to fresh air immediately and report to the shift supervisor.

### Personal Protective Equipment

- Safety glasses or face shield — brine splatter at boiling temperature causes eye damage
- Heat-resistant gloves for handling hot brine pans and boiled salt
- Respiratory protection for salt dust during crushing and handling operations
- Hearing protection in underground mining operations
- Steel-toe boots for mine operations and heavy equipment handling
- Sun hat and long sleeves for solar pond workers — prolonged exposure to sun reflected off white salt surfaces intensifies UV exposure

### Emergency Procedures

- Maintain first aid kit with burn treatment for brine boiling operations. Hot concentrated brine causes deep burns that are worse than hot water due to the salt content.
- Know locations of emergency shutoffs for brine pumps and mine water pumps.
- Establish evacuation routes and assembly points. Underground salt mines must have clear exit routes marked.
- Train all personnel on flood response for underground mines. Water ingress is the primary life-threatening hazard in salt mining — salt dissolves, so flooding can be rapid and catastrophic.
- For solar pond operations, have shade structures and water available for workers experiencing heat exhaustion.

## Quality Control

### Acceptance Criteria

- **Salt (food grade)**: White to off-white color, free of visible impurities (sand, clay, organic matter). Taste is purely salty with no bitter aftertaste (bitterness indicates magnesium or calcium salts). Moisture content low enough that salt flows freely.
- **Brine**: Clear, saturated solution (~26% NaCl). Specific gravity measured with a hydrometer. Free of suspended solids.
- **Rock Salt**: Minimum 90% NaCl content. Contaminating minerals (gypsum, anhydrite, clay) acceptable for industrial use but not for food.

### Testing Methods

- **Purity test**: Dissolve a weighed sample in water. Filter to remove insoluble impurities (weigh the residue). Evaporate the filtered solution and weigh the recovered salt. Purity = recovered salt / original sample × 100%.
- **Taste test**: Quick field method — food-grade salt should taste purely salty. Bitterness indicates magnesium salts; astringency indicates calcium.
- **Hydrometer reading**: Measure brine specific gravity to determine saturation level. Saturated brine at room temperature has a specific gravity of approximately 1.20.
- **Visual inspection**: Color, crystal size, and presence of foreign material. Pure salt is white; discoloration indicates impurities.

### Sampling Protocol

- Inspect first-article output against full specification. For food-grade salt, check color, taste, and moisture.
- Sample subsequent production at defined intervals. Test purity by dissolution method on a representative sample from each batch.
- Record all measurements for trend analysis. Track salt purity and moisture content over time.
- Reject and investigate any out-of-specification results. Contaminated salt may contain harmful minerals or organic matter.
- For underground mining, also track roof conditions and pillar stability in active areas on a regular schedule.

## Scaling Notes

Transitioning from bench-scale to production involves these considerations:

- **Bench scale (individual/family)**: Small salt pan or beach boiling. Sufficient for local food preservation needs. Output measured in kilograms per week.
- **Pilot scale (community)**: Series of interconnected solar evaporation ponds, or a brine well with multiple boiling pans. Multiple workers. Output measured in tonnes per season.
- **Production scale (industrial)**: Large coastal salt works covering hectares; deep solution mines with mechanical brine pumps and industrial-scale evaporation. Output measured in thousands of tonnes per year. Feeds chemical industry (chlor-alkali plants) in addition to food preservation.

Key scaling challenges: fuel supply for brine boiling (solar evaporation avoids this constraint but is climate-limited), land area for evaporation ponds, and transportation logistics from remote salt deposits to population centers.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Solar pond yield below expected 20-25 kg/m³ of seawater | Inlet brine too dilute or pond too deep | Measure inlet salinity with hydrometer (target >3%); reduce pond depth to 15-20 cm in crystallizer; check for freshwater intrusion in intake channel |
| Salt crystals too small for easy harvesting | Crystallizer pond too shallow or evaporation too rapid | Increase crystallizer depth to 20-25 cm; harvest less frequently to allow crystal growth; reduce brine agitation |
| Brine well flow rate dropping | Cavern filling with insoluble residue or borehole partially blocked | Reverse flush with fresh water; increase injection pressure by 0.5-1.0 MPa; drill a second borehole into the same deposit from a different angle |
| Boiling pan salt has bitter taste | MgCl₂ and MgSO₄ co-crystallizing from insufficiently concentrated brine | Pre-concentrate brine to >24% before boiling; add small amount of lime (CaO) to precipitate magnesium as Mg(OH)₂ before final crystallization |
| Rock salt mine room closing (walls creeping inward) | Pillars too narrow for depth and stress | Stop extraction in affected area; widen pillars by reducing room width; install additional roof bolts; if convergence >3 mm/day, abandon room and backfill |
| Salt discoloration (brown, red, gray) | Iron oxide, clay, or organic contamination from deposit | Crush and wash salt in clean water; dissolve and re-crystallize for food grade; check for clay seams in the mining face that are being extracted along with salt |
| Mine ventilation inadequate (dusty air, diesel fume buildup) | Fan undersized or ducting leaks | Measure airflow at working face (target >0.5 m/s velocity); check duct joints for tears; calculate required airflow from equipment power and personnel count; upgrade fan if below target |
| Underground water ingress increasing | Salt dissolution by freshwater from aquifer or surface | Install or upgrade sump pumps immediately; grout water-bearing fractures with cement; if inflow >50 L/min, evacuate and assess whether the water source can be diverted or the area must be sealed |
| Salt caking in storage | High ambient humidity (>75% RH) | Improve storage ventilation; add desiccant bags (quicklime) to storage containers; seal containers between withdrawals; consider adding anti-caking agent (0.1-0.5% magnesium carbonate or sodium ferrocyanide for food grade) |
| Solar pond green color, algae growth | Nutrient-rich seawater with slow evaporation | Increase salinity in concentrator ponds above 15% (kills most algae); skim algae from surface; check for agricultural runoff contaminating intake water |

## Variations and Alternatives

- **Solar evaporation (coastal ponds)**: Lowest energy input, highest climate dependency. Works best in arid coastal regions with consistent sun and wind. The dominant method in suitable climates — Mediterranean, tropical coasts, salt lakes.
- **Brine boiling (inland)**: Works anywhere brine springs or salt deposits are accessible. Fuel-intensive but climate-independent. The traditional method in Northern Europe where solar evaporation is impractical.
- **Rock salt mining**: Accesses deep solid deposits. Requires conventional mining capability (shafts, ventilation, haulage). Produces salt that may need re-crystallization for food-grade purity. Useful for industrial-scale supply.
- **Salt from salt lakes**: Natural saline lakes (Dead Sea, Great Salt Lake) produce salt by simple evaporation. Harvesting is straightforward but may require purification to remove undesirable co-precipitated minerals.

## References

- [Mining Engineering & Extractive Metallurgy](index.md) — parent capability
- [Mining Domain](./index.md) — domain overview and related capabilities
- [Food Processing](../food-processing/index.md) — upstream dependency (material)
- [Electrolysis](../chemistry/electrolysis.md) — upstream dependency (material)
- [Energy](../energy/index.md) — downstream capability

Salt production connects to [Food Processing](../food-processing/index.md) through food preservation (salting, curing), to [Chemistry](../chemistry/index.md) through the chlor-alkali electrolysis process and soda ash production, and to [Health](../health/index.md) through iodization programs that prevent goiter and cretinism.

The availability of salt often determines the viability of a settlement. Inland communities without access to salt deposits must trade for it — historically, salt trade routes were among the first long-distance commercial networks. A community that can produce surplus salt has a trade good with universal demand.


### Material Handling

Proper handling of input materials and products is essential for consistent results:

- Store finished salt in covered, dry containers. Salt is hygroscopic — it absorbs atmospheric moisture and clumps or dissolves in high humidity. Sealed wooden kegs or clay jars with tight lids.
- Use FIFO (first-in, first-out) inventory management. Older salt may have absorbed moisture and caked.
- Label all containers with source, date produced, and grade (food or industrial).
- Inspect salt before use — reject any that shows discoloration, contamination, or excessive moisture.
- Segregate waste streams: bittern (the concentrated residual brine after salt crystallization) contains magnesium and potassium salts that can be processed separately or used for other applications.
- Protect stored salt from rain and flooding. A flooded salt store is a total loss.

---

*Part of the [Bootciv Tech Tree](../index.md) · [Mining](./index.md) · [All Domains](../index.md)*
