# Charcoal Production

> **Node ID**: energy.fuels.charcoal
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.fuels`](fuels.md), `foundations`
> **Enables**: [`ceramics.pottery.kiln-firing`](../ceramics/kiln-firing.md), [`chemistry.explosives`](../chemistry/explosives.md)
> **Timeline**: Years 0-10
> **Outputs**: charcoal, char_cloth, wood_tar, wood_vinegar
> **Critical**: Yes — charcoal is the primary fuel for all early iron smelting; no charcoal means no iron before coke

Charcoal is the primary fuel for all metallurgy until coke arrives in the industrial stage. Every kg of iron requires roughly 1-2 kg of charcoal. It is produced by heating wood in the absence of sufficient oxygen to drive off water and volatile compounds, leaving nearly pure carbon. The process — pyrolysis — is simple in principle but demands careful control of temperature and airflow to convert wood to charcoal without burning it to ash.

Charcoal has several advantages over raw wood as a metallurgical fuel: roughly double the energy density per unit mass (~29 MJ/kg vs ~16-18 MJ/kg for seasoned wood), burns hotter and cleaner (less smoke and tarry residue), and is nearly pure carbon (no moisture to generate steam that would oxidize iron during smelting).


## Species Selection

Hardwood produces denser, hotter charcoal. Softwood produces lighter, faster-burning charcoal:

| Wood Type | Charcoal Quality | Density (kg/m³) | Best Use |
|-----------|-----------------|-----------------|----------|
| Oak | Excellent | 250-300 | Iron smelting, forging |
| Hickory | Excellent | 280-320 | Iron smelting |
| Maple | Very good | 240-280 | Forging, brass smelting |
| Beech | Very good | 230-270 | General metallurgy |
| Ash | Good | 220-260 | Forging |
| Pine | Fair | 150-200 | Cooking, domestic heating |
| Spruce | Fair | 130-180 | Domestic heating |

**General rule**: The densest hardwoods available make the best metallurgical charcoal. In tropical regions, mangrove, eucalyptus, and dense tropical hardwoods serve well. Avoid resinous softwoods (pine, spruce) for metallurgy — the resin creates tarry smoke that contaminates metal.

## Preparation

- **Cut to uniform lengths**: ~30-60 cm for pit/mound kilns, 15-30 cm for simple kilns. Uniform pieces carbonize evenly.
- **Split to 5-10 cm diameter**: Thick pieces may leave uncarbonized cores. Thin pieces are easier to stack and carbonize evenly. Use wedge and maul for splitting.
- **Season 2-6 months**: Green wood produces more smoke, less charcoal, and requires more energy to drive off moisture. Air-dry under cover to ~20% moisture content. Do not over-season to the point of decay (rotted wood produces weak, crumbly charcoal).
- **Stack by size**: Thickest pieces in the center of the burn (hottest zone), thinner pieces outside.
- **Volume planning**: A typical iron smelting bloomery requires 15-25 kg charcoal per run. A mound kiln produces 100-500 kg per burn. Plan charcoal production capacity to match projected metal output.

## Earth-Covered Pit Method (Simplest)

**Strengths**:
- No permanent construction needed — a hole in the ground with earth cover
- Minimal tools required — shovel, hatchet, and matches
- Can be done anywhere with hardwood trees

**Weaknesses**:
- Low yield (20-30% by weight) — most energy lost as volatiles
- No byproduct recovery — tar, vinegar, and gas are wasted
- Difficult to control — temperature regulation depends on air vent management by eye and experience
- One-time use — pit is destroyed when opened to extract charcoal

The earliest and simplest method.

The oldest and simplest method — requires no permanent construction.

- **Site selection**: Level ground, away from structures, downwind. Clay soil preferred (better seal). Clear vegetation in a 3-5 m radius to prevent fire spread.
- **Pit construction**: Dig shallow pit 60-100 cm deep, 1-2 m diameter, sloping sides. Or use flat ground with earth mound (above-ground method).
- **Stacking**: Stand wood vertically in tight formation around central firing pole (5 cm diameter dry stick). Thickest pieces in center, thinner pieces outside. Leave air channels between pieces. Stack ~50-200 kg per burn.
- **Firing**: Remove central pole, drop burning tinder into the hole. Wood ignites from center outward.
- **Controlled burn (CRITICAL)**: Cover partially with earth/leaves/sod once well lit. Leave small vent holes. The goal is *partial* combustion — enough heat to drive off water and volatiles (pyrolysis) but not so much that the wood burns to ash.
  - **Smoke progression**: White (steam, 100-200°C) → yellow-brown (tar and organic vapors, 200-400°C) → thin blue (nearly done, 400-600°C). When blue smoke diminishes significantly, seal all vents.
- **Timing**: 12-48 hours depending on size. Small pits: ~12-24 hours. Large mound kilns: 24-48+ hours.
- **Cooling**: Seal all vents with earth. Let cool 24-48 hours. Opening too early causes reignition and loss of the entire burn.
- **Yield**: ~20-35% by weight (softwood less, hardwood more). ~100 kg wood → ~25 kg charcoal.
- **Quality indicators**: Good charcoal rings when struck, is lightweight, black throughout with retained wood grain structure. Brittle, easily crushed = underburned. White ash = overburned.

## Simple Kiln Method (Higher Yield, Reusable)

**Strengths**:
- Reusable — a well-built brick or stone kiln lasts hundreds of cycles
- Higher yield (30-40%) than pit method due to better temperature control
- Predictable results — fixed kiln geometry allows repeatable firing schedules

**Weaknesses**:
- Requires brick or stone construction — more upfront effort than pit method
- Still no byproduct recovery — volatiles escape through the chimney
- Batch process — each cycle takes 8-24 hours of firing plus 12-24 hours of cooling

## Mound Kiln (Collier's Method)

The traditional method used by professional charcoal burners (colliers) for centuries. Produces large quantities of high-quality charcoal. Two approaches are described below:

**Cylindrical kiln (permanent structure)** — significantly improves yield and consistency:

- **Construction**: Cylindrical stone or clay structure (~1 m tall, ~80 cm diameter) with grate at bottom and opening at top. Walls 10-15 cm thick. Firebrick lining for durability. Iron or stone grate with 2-3 cm gaps for air flow.
- **Loading**: Pack wood tightly from bottom to top through the top opening. Close the top with an iron sheet or stone slab once loaded (leave a small vent).
- **Ignition**: Ignite from bottom through the grate using kindling. The fire spreads upward through the wood charge.
- **Air control**: Adjust air intake with a door or sliding damper at the base. More air = faster burn but more complete combustion (less yield). Less air = slower, more efficient carbonization.
- **[Cover top](../glossary/cover-top.md)** with iron sheet or stone slab when smoking properly.
- **Yield**: ~30-40% by weight. Can be reused hundreds of times. More consistent quality than pit method.
- **Cycle time**: 8-24 hours for firing, 12-24 hours cooling.

**Earth-covered mound (traditional collier's method)** — scalable to very large volumes:

- **Construction**: Build a hemispherical mound of stacked wood, 2-4 m diameter at the base, 1-2 m tall. Central chimney (tripod of stout sticks, 10 cm gap). Wood stacked vertically against the chimney, leaning inward. Largest pieces at center, smallest at edges.
- **Covering**: Cover the entire mound with a layer of leaves/straw (to prevent earth from falling into gaps between wood), then a thick layer of earth/sod (10-20 cm). Pack firmly. Leave 3-4 vent holes around the base and the central chimney open.
- **Firing**: Drop burning embers into the central chimney. The fire spreads outward from the center.
- **Control**: This is the skilled part. The collier watches smoke color and adjusts vent holes — opening some, closing others — to maintain uniform carbonization throughout the mound. Takes 2-5 days for a large mound. Requires near-constant attention (colliers slept beside their mounds in temporary shelters).
- **Yield**: 25-35% by weight. 1-5 tonnes of charcoal per mound depending on size.
- **Advantage**: Scalable to very large volumes. Traditional method used throughout pre-industrial Europe and Asia for iron production. A single large mound can fuel a bloomery for weeks.

## Retort Method (Highest Quality & Yield)

**Strengths**:
- Highest yield (35-45%) and most consistent quality of all methods
- Full byproduct recovery — tar, wood vinegar (acetic acid), and wood gas captured
- Temperature is controllable — produces uniform charcoal with predictable properties
- Retort vessel is reusable indefinitely

**Weaknesses**:
- Requires a sealed metal vessel (steel or cast iron) — more complex construction
- External heat source needed to drive pyrolysis — consumes fuel to make fuel
- Higher capital cost — retort vessel, condenser, and gas collection system

- **Construction**: Sealed iron or clay chamber with a flue pipe leading to a separate combustion chamber. Wood charge goes in the retort; pyrolysis gases exit through flue and are burned to heat the retort externally.
- **Process**: Heat retort to 400-600°C. Pyrolysis gases (CO, H₂, CH₄, wood vinegar) are routed to a burner that heats the retort — the process becomes self-sustaining once started. No combustion air touches the charcoal.
- **Advantages**: Higher yield (~35-45%), consistent quality, recoverable byproducts (wood tar, methanol, acetic acid from condensed vapors). The recovered gases provide the heat, so less wood is wasted as fuel.
- **Complexity**: Requires metalworking for sealed chamber and piping. Not the first method available, but worth building once iron working is established.
- **Throughput**: Batch operation. 50-500 kg per batch depending on retort size. Cycle time: 6-12 hours heating, 6-12 hours cooling.

## Charcoal Briquetting

Fine charcoal (fines, dust) from production and handling is too small for direct use in furnaces — it falls through grate bars and blocks airflow. Briquetting recovers this otherwise wasted material (typically 15-25% of total production):

- **Binder**: Mix charcoal fines with 5-15% binder by weight. Binders: clay (cheapest, reduces energy density), starch paste (good, requires flour), molasses (excellent, requires sugar processing), or coal tar pitch (strongest, requires coke ovens).
- **Forming**: Press mixture at 100-200 bar in a mold (cylinder or pillow shape). Mechanical or hydraulic press. Higher pressure = denser, harder briquette.
- **Drying**: Air-dry for 2-7 days, or warm oven at 60-80°C for 4-8 hours. Moisture must drop below 5% for proper burning.
- **Result**: Uniform fuel pieces that burn more consistently than lump charcoal. Popular for domestic cooking and smithing.
- **Energy density**: Briquettes with clay binder ~20-23 MJ/kg; with starch/molasses binder ~25-28 MJ/kg (closer to lump charcoal at 29 MJ/kg).

## Char Cloth Production

Char cloth is a key material for fire-starting — a swatch of cotton or linen fabric that has been pyrolyzed (charred) in a near-airless container. It catches a spark from flint-and-steel or friction methods instantly and glows like an ember, allowing a tinder bundle to be ignited reliably.

- **Method**: Place small squares of natural fiber cloth (cotton, linen — no synthetics) in a sealed metal tin with a small vent hole. Heat the tin in a fire or on coals until smoke stops emerging from the vent. Cool before opening (opening hot introduces oxygen → cloth ignites and burns to ash).
- **Result**: Black, soft cloth that catches the faintest spark. Store in airtight container (char cloth absorbs moisture and degrades in humid air).

## Byproduct Recovery

Charcoal production generates valuable byproducts, especially from retort operations:

- **Wood tar**: Condensed from pyrolysis gases at 100-200°C. Contains creosote, phenols, and other organic compounds. Uses: wood preservative (creosote for fence posts and railway sleepers), waterproofing, rope preservation, medical antiseptic.
- **Wood vinegar (pyroligneous acid)**: Condensed from gases at 20-100°C. Contains acetic acid (5-10%), methanol (2-3%), acetone, and other organics. Uses: food preservative (smoking), agricultural pesticide and growth stimulant, acetic acid source for chemistry.
- **Wood gas**: Non-condensible fraction (CO, H₂, CH₄). Combustible. Can be burned to heat the retort or piped to furnaces. Approximate composition: 20-30% CO, 10-20% H₂, 2-5% CH₄, balance CO₂ and N₂.

## Quality Grading

| Grade | Fixed Carbon | Volatile Matter | Ash | Primary Use |
|-------|-------------|-----------------|-----|-------------|
| Barbecue / domestic | ~60% | ~30% | <5% | Cooking, casual heating |
| Industrial | ~75-80% | ~15-20% | <5% | Forging, brass/copper smelting |
| Metallurgical | ~85-90% | <10% | <3% | Iron smelting, steelmaking |

Higher fixed carbon = hotter, cleaner burn. Metallurgical grade requires hardwood feedstock and careful pyrolysis control (complete volatile elimination at 500-600°C with adequate soak time).

**Quality tests**:
- **Ring test**: Strike two pieces together. Metallurgical-grade charcoal produces a clear, bell-like ring. Dull thud = underburned (high volatiles).
- **Fracture**: Break a piece. Clean, conchoidal fracture with visible wood grain = good. Crumbly = underburned. Powdery = overburned.
- **Density**: Hardwood charcoal ~250-350 kg/m³ bulk density. Higher density = harder charcoal = better for blast furnace use.
- **Spark test**: Hit a piece with a hammer. Dense metallurgical charcoal throws bright sparks. Dull, crumbly charcoal throws few or no sparks.

## Charcoal in Metallurgy

The critical application that drives charcoal production at scale:

- **Iron smelting**: Bloomery and early blast furnaces consume 1-2 kg charcoal per kg of iron produced. A modest bloomery producing 10 kg iron per run needs 15-20 kg charcoal — one moderate mound kiln's output. A large blast furnace consumes 5-10 tonnes of charcoal per day.
- **Copper and bronze**: Less demanding — charcoal provides the heat and a reducing atmosphere. ~0.5-1 kg charcoal per kg of copper.
- **Forging**: Smithing hearths consume charcoal continuously. A blacksmith's forge burns 2-5 kg/hour.
- **Carbon source**: In steelmaking, charcoal provides both heat and carbon (carburizer). The carbon from charcoal dissolves into iron to create steel (~0.5-1.5% C). The carburization effect is critical — without it, iron remains soft and cannot be hardened.
- **Reducing atmosphere**: Charcoal combustion produces CO, which reduces metal oxides: Fe₂O₃ + 3CO → 2Fe + 3CO₂. This is the fundamental chemical reaction of iron smelting.

## Production Scale Estimates

| Operation | Charcoal Demand | Wood Required | Kilns Needed |
|-----------|----------------|---------------|-------------|
| Single blacksmith forge | 10-20 kg/day | 40-80 kg/day | 1 small pit kiln every 2-3 days |
| Bloomery (10 kg iron/run) | 15-25 kg/run | 60-100 kg/run | 1 mound kiln per 5-10 runs |
| Small blast furnace (1 tonne iron/day) | 1-2 tonnes/day | 4-8 tonnes/day | 2-4 large mound kilns operating continuously |
| Village heating/cooking | 5-15 kg/household/day | 20-60 kg/day | 1 kiln per 5-10 households |

These figures illustrate why charcoal production was one of the largest industrial activities in pre-modern economies. Entire forests were managed as coppice woodland specifically for charcoal production — trees harvested on 15-25 year cycles, regrown from stumps.

## Charcoal Gasification (Producer Gas)

Charcoal can be gasified to produce a combustible gas suitable for engines and furnaces. Unlike wood gasification, charcoal gasification produces a cleaner gas with minimal tars:

- **Process**: Blow limited air through a hot bed of charcoal in a gasifier (vertical shaft furnace, 0.5-2 m diameter). The partial combustion produces CO: 2C + O₂ → 2CO (exothermic, maintains bed temperature at 800-1100°C). Adding steam to the air blast increases H₂ yield via the water-gas reaction: C + H₂O → CO + H₂ (endothermic — requires alternating air and steam blasts).
- **Producer gas composition**: ~28-32% CO, ~8-15% H₂, ~1-3% CH₄, ~55-60% N₂ (nitrogen from air dilutes the gas). Calorific value: ~4.5-6 MJ/m³. Lower than coal gas (~18 MJ/m³) but sufficient for furnace firing and internal combustion engines.
- **Engine use**: Charcoal producer gas can fuel modified gasoline engines at 40-60% of gasoline power output. Requires gas scrubber (cyclone + sawdust filter) to remove particulates and cooling to ~30°C before engine intake. Widely used during WWII petroleum shortages.
- **Advantage over wood gasification**: Charcoal contains virtually no tars — gas cleanup is minimal. Wood gasification produces heavy tars that foul engine valves and require extensive scrubbing systems.

## Grading by Application

Different metallurgical processes require different charcoal grades, optimized for particle size, density, and burn characteristics:

| Application | Preferred Grade | Size Range | Why |
|-------------|----------------|------------|-----|
| Iron bloomery smelting | Metallurgical, lump | 20-80 mm | Large pieces maintain permeability in the shaft, allowing gas flow |
| Blast furnace | Metallurgical, dense | 25-75 mm | Must support burden weight; high CSR (Coke Strength after Reaction) analog — dense hardwood charcoal preferred |
| Copper/bronze smelting | Industrial | 15-50 mm | Lower temperature requirement allows softer charcoal |
| Forging (blacksmith) | Industrial, lump | 15-40 mm | Consistent size for even bed temperature; forge hearth consumes 2-5 kg/hour |
| Cooking/domestic | Barbecue grade or briquettes | 20-60 mm | Lower grade acceptable; briquettes burn more uniformly |
- **Screening**: After production, pass charcoal through mesh screens to sort by size. Oversize (>80 mm) is broken with wooden mallets. Undersize (<10 mm) goes to briquetting. This grading step is essential for blast furnace and bloomery operation — a charge of mixed sizes results in uneven gas flow and inconsistent reduction.

## Storage & Safety

- **Spontaneous combustion**: Fresh charcoal can self-heat from adsorption of moisture and oxygen. Cool completely before storing. Store in dry, ventilated area — not airtight containers. Fresh charcoal should age 24-48 hours before bulk storage. Monitor internal temperature of large piles — if temperature rises above 60°C, spread the pile to cool.
- **Moisture absorption**: Charcoal is hygroscopic. Absorbs 5-15% moisture from humid air, reducing effective energy density. Cover piles with tarp, store off ground on pallets or stone platform.
- **Dust explosion**: Charcoal dust in enclosed spaces at concentrations >20-60 g/m³ can detonate with an ignition source. Ventilate grinding and handling areas. Avoid spark sources near fine charcoal. Ground equipment to prevent static discharge.
- **Carbon monoxide**: Charcoal burning produces CO, especially during the pyrolysis phase. Perform all kiln operations outdoors or in well-ventilated spaces. Never operate a kiln indoors. CO is odorless and lethal at 0.1% concentration.
- **Burns**: Kiln and charcoal handling involves hot surfaces and hot coals. Wear leather gloves and long sleeves during kiln tending and charcoal extraction.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Charcoal mostly ash (over-burned) | Too much air entering kiln | Seal air leaks; reduce draft openings; monitor earth kiln for cracks |
| Charcoal still brown/black wood (under-carbonized) | Temperature too low or time insufficient | Extend burn time; verify earth kiln steam has stopped (signals completion); ensure proper kiln loading density |
| Low charcoal yield (<15% by weight) | Hardwood too small or over-burned | Use larger billets (10-15 cm diameter); reduce peak temperature; switch to denser hardwood species |
| Excessive smoke during burn | Wet wood or incomplete sealing | Season wood 6+ months before charring; seal kiln thoroughly; pre-dry wood if necessary |
| Charcoal fines (too much dust) | Mechanical damage during handling or soft wood species | Use harder wood species; handle charcoal gently; screen and sell fines separately (briquette feedstock) |
| Kiln won't sustain burn | Green (wet) wood or insufficient kindling | Use dry kindling to start; ensure initial charge is well-dried; build fire from center outward |

## Charcoal Gasification for Vehicle Fuel

During petroleum shortages, charcoal gasification provides a practical alternative fuel for internal combustion engines. Charcoal producer gas powered an estimated 700,000 vehicles in Europe during WWII, particularly in Sweden, France, and Germany, where gasoline was strictly rationed or unavailable.

**Gas composition**: Charcoal gasified with limited air produces producer gas with the following approximate composition by volume: CO 20-25%, H₂ 10-15%, CH₄ 2-4%, CO₂ 8-12%, N₂ 50-55%. Calorific value: 4-6 MJ/m³, roughly one-third the energy density of natural gas (35 MJ/m³) and far below gasoline vapor. This low energy density is the fundamental limitation: engine power output drops to 40-60% of gasoline rating when running on producer gas.

**Gasifier design (Imbert-type downdraft)**: Cylindrical steel vessel, 30-60 cm diameter, with a firebrick-lined combustion hearth at the bottom of the reduction zone. Charcoal is loaded from the top (hopper with airtight lid). Air enters through nozzles at the hearth throat (5-10 tuyeres, 10-20 mm diameter). Gas flows downward through the charcoal bed, exiting at the bottom through a grate. The downdraft configuration passes the gas through the hottest combustion zone, cracking tars — critical for engine fuel quality (tar in gas fouls engine valves and piston rings within hours). Typical fuel consumption: 1 kg charcoal produces approximately 2.5 m³ of producer gas.

**Vehicle integration**: Gasifier mounted on a trailer behind the car or on a platform over the hood/bumper. Gas passes through a cyclone separator (removes ash and soot), a cooling tube (finned pipe, reduces gas from 400°C to ~30°C — cooler gas is denser, improving volumetric efficiency), and a cloth or sawdust filter (final particulate removal). The carburetor is replaced or bypassed with a gas-air mixer. Engine starting: gasoline for cold starts, switch to producer gas once the gasifier is hot (10-15 minute warm-up period).

**Range and performance**: A typical 1940s passenger car (1.5-2.0 L engine) consumed 10-15 kg of charcoal per 100 km, giving a practical range of 30-50 km per 10 kg charcoal load. Top speed reduced by 30-40% compared to gasoline. Hill climbing was noticeably sluggish due to reduced power output. Charcoal quality mattered: metallurgical grade (>85% fixed carbon) produced cleaner gas with fewer tars and better engine performance.

## See Also

- [Coal](coal.md) and [Coke](coke.md) — later fuel progression beyond charcoal
- [Fuels](fuels.md) — comparative fuel properties table
- [Iron & Steel](../metals/iron-steel.md) — primary consumer of metallurgical charcoal
- [Kilns](../ceramics/kilns.md) — kiln construction for charcoal burning
- [Plants & Forestry](../plants/index.md) — wood supply as feedstock
- [Explosives](../chemistry/explosives.md) — charcoal as black powder component
- [Wood Gasification](../chemistry/wood-gasification.md) — producer gas from wood

[← Back to Energy](index.md)
