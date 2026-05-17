# Phase 4: Energy Revolution — Steam, Electricity & Scale

**Timeline**: Years 15–30
**Goal**: Abundant, controllable power.
**Dependencies**: [Phase 2](phase-02-metallurgy.md) (iron/steel), [Phase 3](phase-03-machine-tools.md) (precision cylinders, machining)

## Objectives

- Produce coke from coal for superior high-temperature processes
- Build steam engines for mechanical power
- Generate electricity via electromagnetic induction
- Create electric arc and submerged arc furnaces for high-temperature work

## Key Technologies

### Coal & Coke

Coke is to coal what charcoal is to wood — the refined, high-energy, low-impurity fuel that enables high-temperature industrial processes.

**Coal mining** (see [SQ 11](../side-quests/sq-11-mining-engineering.md) for full mining detail):
- **Types**: Bituminous coal (most common, good for coking and steam), anthracite (highest carbon, hardest, cleanest burn), lignite (lowest grade, high moisture).
- **Selection for coking**: Bituminous coal with 20-30% volatile matter, low sulfur (<1%), moderate ash (<10%). Not all coal makes good coke — test by heating a small sealed sample and checking if the residue is hard and porous (good coke) vs. powdery (non-coking coal).

**Coke production (beehive oven method)**:
- **Construction**: Dome-shaped brick or stone chamber, ~3-4 m diameter, 2 m tall. Opening at top for charging and ignition, side opening for air control and coke removal.
- **Process**:
  1. Charge 3-6 tonnes of crushed coal (5-15 cm pieces) through top opening.
  2. Ignite coal at top surface (light wood/coal kindling).
  3. The fire burns downward through the coal bed. Volatile gases (coal tar, ammonia, coal gas) burn at the top, providing heat for carbonization below.
  4. Air supply controlled by covering top opening with loose bricks — restrict to maintain carbonization temperature (~900-1100°C) without full combustion.
  5. Duration: 48-72 hours for full carbonization.
  6. Quench: Spray with water (carefully — massive steam eruption). Or seal oven and let cool inertly.
  7. Remove coke through side door with iron rakes.
- **Yield**: ~60-70% by weight from good coking coal.
- **Byproducts**: Coal gas (CO + H₂ + CH₄ — can be captured and burned), coal tar (benzene, toluene, phenol — see [SQ 12](../side-quests/sq-12-petrochemicals.md)), ammonia (dissolved in quench water = ammonia liquor).
- **Coke properties**: Hard, porous, gray. Burns at ~1800-2100°C with forced air (vs. charcoal ~1100°C unforced). Essential for blast furnaces and silicon production.

**Coke production (by-product recovery oven — more advanced)**:
- Horizontal silica brick chamber, 12-15 m long, 0.4-0.5 m wide, 4-6 m tall. Heated externally by burning collected coal gas. Coal charge ~15-20 tonnes. Carbonization time ~16-20 hours.
- All volatile byproducts captured: coal tar, benzol, ammonia, sulfur. Higher quality coke, but requires more construction effort.

### Steam Engines

**Newcomen-style atmospheric engine** (first practical steam engine, ~1712):
- **Principle**: Steam at atmospheric pressure fills cylinder. Cold water injected into cylinder condenses steam → vacuum → atmospheric pressure pushes piston down → work stroke.
- **Critical component**: Cylinder, bored to close tolerance (~0.5 mm clearance over piston). Requires Phase 3 machine tools (Wilkinson boring machine). Cylinder diameter 30-80 cm, stroke 1.5-3 m.
- **Construction**:
  - **Cylinder**: Cast iron, bored true. Brass or lead sealing rings around piston.
  - **Boiler**: Riveted iron plate (wrought iron, 6-12 mm thick). Haystack or wagon boiler shape. Holds ~1000-5000 liters of water at atmospheric pressure (no high-pressure hazard).
  - **Valves**: Hand-operated or later automated (plug rod/valve gear). Steam valve admits steam, injection valve admits cold water, snifting valve releases air.
  - **Pump rod**: Heavy wooden beam connects piston to mine pump chain. Counterweighted on engine side.
- **Performance**: ~5-15 HP. Efficiency ~0.5-1% (extremely wasteful of coal — but it pumped water from mines, which nothing else could do at scale).
- **Cycle**: Steam in (piston rises) → cold water injection (steam condenses, vacuum, piston pulled down) → pump stroke → repeat. 6-12 strokes/minute.

**Watt-style separate condenser engine** (~1769, massive efficiency improvement):
- **Key innovation**: Separate condenser kept cold, while cylinder stays hot. Eliminates the heating/cooling cycle that wasted most of the Newcomen engine's energy.
- **Additional improvements**: Double-acting (steam pushes piston both directions — doubles power from same cylinder), rotative output (sun-and-planet gear or crank converts reciprocating to rotary motion), governor (centrifugal speed regulator), expansive working (cut off steam early, let expansion do remaining work).
- **Construction**: Higher precision required — cylinder needs ~0.1 mm bore accuracy. Better piston sealing (oil-soaked hemp or leather packing).
- **Boiler**: Higher pressure tolerated — 0.5-2 bar gauge. Still low pressure by modern standards. Lancashire or Cornish boiler design (fire tubes through water jacket).
- **Performance**: 10-100+ HP. Efficiency ~3-5% (5x improvement over Newcomen). Enables factory power, not just mine pumping.

**Boiler construction**:
- **Materials**: Wrought iron plates (6-15 mm thick), riveted joints. Later: welded steel.
- **Riveting**: Overlap plates, drill matching holes, drive red-hot iron rivets, hammer flat on both sides. Rivet spacing 3-5 diameters. Test with hydrostatic pressure at 1.5x operating pressure.
- **Safety**: Pressure relief valve (weighted lever type — adjust weight for set pressure). Water level gauge (glass sight glass). Blowdown valve (drain sediment). Fusible plug (lead core melts if water drops too low, dumps steam into firebox and extinguishes fire — last-resort safety).
- **Feed water**: Must be clean. Sediment clogs tubes. Dissolved minerals cause scale (insulates tubes, causes overheating). Blowdown daily. Water treatment (lime softening) when available.

### Electricity Generation

**Voltaic piles / batteries** (first electrical source):
- **Construction**: Stack alternating disks: copper plate → cardboard soaked in brine (or sulfuric acid) → zinc plate → repeat. 10-20 cells produce 10-20V DC at low current.
- **Output**: ~1V per cell, ~50-100 mA. Sufficient for early electroplating experiments, telegraph operation, electrochemistry exploration. Not sufficient for industrial power.
- **Daniell cell** (improved): Copper electrode in CuSO₄ solution, separated by porous pot from zinc electrode in ZnSO₄ or dilute H₂SO₄. 1.1V, more stable voltage, longer life. Standard for telegraph systems.

**Wire drawing** (essential for all electrical work):
- **Starting material**: Cast copper ingot, hot-forged to rod (~10 mm diameter), then cold-drawn.
- **Drawing process**: Pull copper rod through successively smaller hardened steel dies (tungsten carbide or tool steel). Each pass reduces diameter ~20-30%. Anneal between passes (heat to 400-600°C to restore ductility lost from cold work). Repeat until target gauge reached.
- **Common gauges**: 1 mm diameter for winding (≈ 18 AWG), 0.1 mm for fine coils (≈ 38 AWG). Length from 1 kg of copper: ~130 m at 1 mm diameter.
- **Lubrication**: Tallow or soap solution on wire as it enters die. Essential — without it, wire galls and snaps.
- **Insulation**: Dip drawn wire in rubber solution (natural rubber dissolved in naphtha), wrap with cotton thread, or varnish with shellac. Multiple layers for higher voltage. Gutta-percha (natural thermoplastic) for underwater/underground cables.

**Generators** (Faraday principle — rotating coil in magnetic field):
- **First generator (magneto)**: Permanent magnets (lodestones or magnetized steel bars) provide field. Rotating coil (armature) wound on iron core, turned by hand, water wheel, or steam engine. Output: pulsed DC.
- **Winding**: Copper wire, enamel or shellac insulated. Number of turns determines voltage. Wire gauge determines current capacity. Typical early generator: 500-2000 turns of 0.5-1 mm wire on iron core.
- **Commutator**: Split copper ring with brushes (carbon or copper gauze) to convert AC to DC. For AC generators (alternators): slip rings instead.
- **Self-exciting generator** (dynamo): Electromagnets (iron core + coil) replace permanent magnets for stronger field. Uses residual magnetism in iron to bootstrap, then feeds some output current back to field coils → positive feedback → full excitation.
- **Performance targets**: First generators: 100W-1kW. Mature dynamo: 1-50 kW. Efficiency 70-90%.

**Motors** (reverse of generators):
- **DC motor**: Current through armature coils in magnetic field creates torque. Commutator reverses current direction each half-turn for continuous rotation.
- **Series-wound**: Field and armature in series. High starting torque, speed varies with load. Good for traction (trams, trains, starter motors).
- **Shunt-wound**: Field and armature in parallel. More constant speed, lower starting torque. Good for machine tools, fans, pumps.
- **Construction**: Identical mechanical parts to generators — a dynamo run backwards as a motor.

**Transformers** (voltage step-up/step-down):
- **Principle**: Two coils on shared iron core. Alternating current in primary creates changing magnetic flux, inducing voltage in secondary. Turns ratio determines voltage ratio (V₂/V₁ = N₂/N₁).
- **Construction**: Laminated iron core (thin iron sheets, 0.3-0.5 mm, insulated with shellac or paper — prevents eddy current losses). Primary and secondary windings of insulated copper wire.
- **Essential for**: Power distribution (step up voltage for transmission → lower current → less I²R loss in wires, step down at destination).

**Power distribution**:
- **DC system** (Edison): 110V DC. Limited range (~1-2 km) due to voltage drop in wires. Requires many small generators.
- **AC system** (Westinghouse/Tesla): 110-220V AC, stepped up to 1000-10000V for transmission, stepped down at load. Much longer range. Requires alternators and transformers. Eventually wins.
- **Wire sizing**: Copper wire, sized by current capacity. Rule of thumb: 3-5 A per mm² of cross-section for acceptable heating. Example: 10 A load at 110V over 100 m needs ~6 mm² wire (≈ 2.8 mm diameter) to keep voltage drop under 5%.

### Electric Furnaces

**Electric arc furnace (EAF)**:
- **Construction**: Cylindrical steel shell, lined with refractory brick (magnesite or dolomite). Three graphite electrodes (50-200 mm diameter) inserted through roof. Hydraulic or screw mechanism raises/lowers electrodes.
- **Electrode manufacturing**: Mix petroleum coke + coal tar pitch, extrude, bake at 800-1200°C (carbonization). Graphitize at 2500-3000°C (requires existing EAF or resistive heating — bootstrapping challenge). Early electrodes can be amorphous carbon (lower conductivity, but functional).
- **Operation**: Contact electrodes to scrap/material, withdraw to strike arc. Arc temperature ~3000-3500°C. Material heats by radiation and resistance. Charge 1-50 tonnes. Cycle time 30-90 minutes.
- **Power requirements**: 300-600 kWh per tonne of steel. Requires dedicated generator or grid connection. NOT a casual power load.
- **Critical for**: Steelmaking (recycling scrap → quality steel), silicon reduction (Phase 7 — SiO₂ + 2C → Si + 2CO at ~2000°C), calcium carbide production (CaO + 3C → CaC₂ + CO at ~2000°C).

**Submerged arc furnace** (for silicon, ferroalloys):
- Similar to EAF but electrodes submerged in raw material charge. Heat generated by resistance of the charge itself. More efficient for continuous production than batch EAF.

**Resistance heating**:
- **Principle**: Current through resistive element generates heat (P = I²R).
- **Heating elements**: Nichrome (Ni-Cr alloy, resists oxidation to ~1100°C), Kanthal (Fe-Cr-Al, ~1400°C), silicon carbide (SiC, ~1600°C), molybdenum disilicide (MoSi₂, ~1700°C). For early work: iron wire in reducing atmosphere, or graphite rod.
- **Applications**: Furnaces for crystal growth, annealing, heat treatment, laboratory furnaces.

### Internal Combustion Engines

**Otto-cycle piston engines** (the technology that enables mobile power and aviation):
- **Principle**: Intake (fuel-air mix drawn in) → Compression (piston compresses mixture ~8-12:1) → Power (spark ignites, rapid combustion pushes piston down) → Exhaust (burned gases expelled). Four strokes per power cycle.
- **Critical components**:
  - **Cylinder**: Cast iron or steel, bored to 0.02-0.05 mm tolerance. Requires Phase 3 boring capability. Honed to mirror finish.
  - **Piston**: Cast iron or aluminum alloy (Phase 5+). Cast iron piston rings (2-3) provide gas seal against cylinder wall. Ring gap ~0.3-0.5 mm when installed.
  - **Crankshaft**: Forged steel, ground journals. Counterweights for balance. Requires lathe, grinder, and balancing.
  - **Connecting rod**: Forged or machined steel I-beam section. Big end (crank end) with split bearing shells (babbitt metal: tin-antimony-copper alloy, 80/10/10 typical). Small end (piston end) with bronze bushing.
  - **Valves**: Poppet valves (intake and exhaust). Machined from heat-resistant steel. Seat angle 45°. Springs return valves to closed position. Operated by camshaft (gear or chain driven from crankshaft at half crank speed for 4-stroke).
  - **Camshaft**: Cast iron or steel. Cam lobes ground to precise profile controlling valve timing and lift duration.
- **Carburetor**: Venturi — air flows through constriction, creating low pressure that draws fuel through metering jet. Adjustable needle valve controls fuel-air ratio (~12-15:1 by weight for gasoline). Simpler than fuel injection and sufficient for early engines.
- **Ignition**: Magneto (permanent magnet + coil generates high voltage pulse when triggered by cam — self-contained, no battery). Spark plug (steel shell, ceramic insulator, center electrode, ground electrode, ~0.6-0.8 mm gap). Secondary voltage ~10,000-30,000V.
- **Lubrication**: Splash system (rod dips into oil sump, splashes oil onto cylinder walls and bearings) or pressurized (gear pump circulates oil through galleries). Oil: castor oil or mineral oil (see [SQ 10](../side-quests/sq-10-lubricants-oils.md)).
- **Cooling**: Water jacket around cylinder, thermosiphon circulation (hot water rises to radiator, cools, returns) or pump-forced circulation. Finned air cooling for small engines.
- **Power output**: 5-65 HP for 1-4 cylinders, 1000-3000 RPM. Power-to-weight ratio is THE critical metric for aircraft (see [SQ 13](../side-quests/sq-13-aircraft-development.md)).

### Electrolysis Foundations

**Electrolytic cells**:
- **Principle**: Pass DC current through ionic solution or molten salt → chemical decomposition at electrodes. Anode (+) attracts anions (oxidation). Cathode (-) attracts cations (reduction).
- **Power requirements**: DC supply (battery, dynamo, or rectified AC). Voltage 2-5V per cell (depends on reaction). Current 100-10,000+ A for industrial scale.
- **Cell construction**: Tank (lead-lined wood, concrete, or plastic), electrodes (carbon, lead, titanium), electrolyte (aqueous solution or molten salt), bus bars (copper or aluminum connecting electrodes to power supply).
- **Applications**:
  - **Chlor-alkali**: NaCl brine → Cl₂ (anode) + H₂ + NaOH (cathode). Diaphragm or membrane cell. Voltage ~3.5-4V. Current efficiency ~90-95%.
  - **Water electrolysis**: H₂O → H₂ (cathode) + ½O₂ (anode). Electrolyte: 25-30% KOH. Voltage ~1.8-2.2V. Produces ultra-pure gases.
  - **Aluminum** (Hall-Héroult, later): Al₂O₃ dissolved in molten cryolite (Na₃AlF₆) at 950-1000°C. Carbon anodes. Aluminum deposits at carbon-lined cathode. 4-5V, 100,000+ A. ~13-15 kWh/kg Al. Requires enormous power.
  - **Copper refining**: Impure copper anode → pure copper cathode (99.99%) in CuSO₄/H₂SO₄ electrolyte. Voltage ~0.3V. Gold, silver, platinum collect in anode slimes — valuable byproducts.

### Wire Drawing Bootstrap

- **Chicken-and-egg problem**: you need wire for generators, but hardened steel dies for drawing that wire require decent steel, which itself needs powered machinery
- First wire: hammered or swaged copper rod pulled through hand-punched holes in hardened steel plates, iterating through successively smaller die openings
- Lubrication is critical at every pass (tallow or soap solution; see [SQ 10](../side-quests/sq-10-lubricants-oils.md)); without it the wire galls and snaps
- Wire annealing between passes restores ductility lost from cold working
- Insulation (rubber, varnished cloth, gutta-percha) is applied after drawing, not during

### Permanent Magnets

- **Lodestone** (naturally magnetized magnetite) for early compasses and basic magnetic experiments
- **Magnetized iron/steel bars**: Stroke with lodestone or place in Earth's magnetic field yields magnets for early generator field poles and galvanometers. For stronger magnets: place steel bar inside coil, pass DC current (electromagnet method) — steel retains magnetism after current removed.
- **Keeper**: Store magnets with soft iron bar across poles (keeper) to prevent demagnetization over time.
- **Later materials** (Alnico, ferrite) arrive with Phase 5 chemistry and alloy development

### Elastomer Processing

- **Natural rubber vulcanization**: latex from *Hevea brasiliensis* or temperate alternatives (guayule, Russian dandelion) is coagulated, masticated on a two-roll mill, then compounded with sulfur (1.5-3 phr) and zinc oxide as activator
- **Heat curing** at 140-180°C in electric vulcanizing presses or steam autoclaves (3-10 bar) using Phase 4 electric heating and boiler steam; cycle times 5-30 minutes depending on thickness
- **Applications beyond wire insulation**: shaft seals, gaskets, flat belts and V-belts for power transmission, hoses, vibration dampers, and tire construction for wheeled vehicles
- **Synthetic rubbers** (nitrile, neoprene) are Phase 5+ materials requiring petrochemical feedstocks from [SQ 12](../side-quests/sq-12-petrochemicals.md); see [SQ 14](../side-quests/sq-14-polymers-composites.md) for the full elastomer development roadmap

### Advanced Welding (Phase 4+)

**Oxy-acetylene welding and cutting**:
- **Acetylene production**: Calcium carbide (CaC₂, from CaO + 3C at ~2000°C in electric arc furnace) + water → C₂H₂ + Ca(OH)₂. Generate acetylene on demand in gas generator (water dripped onto carbide in closed vessel). NEVER store acetylene under pressure >0.15 MPa — it detonates spontaneously. Store dissolved in acetone in porous-filled cylinder (acetylene cylinders — safe storage at ~1.5 MPa).
- **Oxygen supply**: From air separation (cryogenic distillation — see SQ 06) or from chemical generation (barium oxide process: heat BaO in air → BaO₂, then heat BaO₂ → BaO + ½O₂). Compressed into steel cylinders at 15-20 MPa.
- **Torch construction**: Brass body with two control valves (oxygen and acetylene), mixing chamber, and copper tip (various sizes — tip orifice 0.5-3 mm). Hoses: rubber with fabric reinforcement, color-coded (red = fuel, blue/green = oxygen).
- **Welding procedure**: Open acetylene valve, ignite (sooty flame). Open oxygen valve — flame becomes blue-white inner cone surrounded by pale blue outer envelope. Neutral flame (equal O₂ and C₂H₂): inner cone ~2-5 mm, temperature ~3100°C. Reducing flame (excess acetylene): longer inner cone, carburizing — for brazing and certain metals. Oxidizing flame (excess O₂): shorter, noisier — for brass/copper brazing only. Hold torch at ~45° angle, move steadily along joint. Add filler rod (matching base metal composition, 1.5-3 mm diameter) to leading edge of puddle. Joint types: butt, lap, fillet.
- **Cutting**: Cutting torch has additional oxygen lever. Heat steel to bright red (~900°C) with acetylene flame, then press oxygen lever — pure O₂ jet reacts with hot steel exothermically (iron burns in oxygen). Blow molten slag through cut. Kerf (cut width) 1-3 mm. Cuts steel up to 300+ mm thick. CANNOT cut non-ferrous metals (copper, aluminum — they conduct heat away too fast, don't oxidize exothermically).
- **Applications**: Repair welding, pipe joining, sheet metal fabrication, cutting steel plate, heating for bending/forming. THE primary metal joining method from ~1900 until arc welding dominated ~1940.

**Arc welding (stick/SMAW — Shielded Metal Arc Welding)**:
- **Principle**: Electric arc between consumable electrode (welding rod) and workpiece melts both, creating a weld pool. Electrode coating provides shielding gas and slag to protect molten metal from atmospheric contamination (oxygen and nitrogen cause porosity and embrittlement).
- **Power source**: DC or AC, 50-100 amps, 20-30 volts open circuit. DC: generator or rectified AC (smoother arc, directional — electrode positive = deeper penetration, electrode negative = faster deposition). AC: transformer (simpler, no rectifier needed, but arc less stable).
- **Electrodes**: Mild steel core wire (2.5-5 mm diameter) with flux coating. Flux composition: cellulose (gas shield), rutile (TiO₂ — slag former, arc stabilizer), limestone (CaCO₃ — additional shielding gas when decomposed by heat), iron powder (increases deposition rate), binders (sodium silicate). Coat by dipping wire in wet flux slurry, or extrude flux around wire. Dry/bake at 100-200°C.
- **Procedure**: Clamp workpiece to metal table (ground/return connection). Insert electrode in holder (insulated handle). Strike arc by scraping electrode across work (like a match) then lifting ~2-3 mm. Maintain arc length ~equal to electrode diameter. Move steadily along joint at ~2-5 mm/second. Electrode melts and deposits filler metal. Slag forms on top of weld — chip off with hammer after cooling. Multi-pass for thicker joints.
- **Joint preparation**: Bevel edges of thick plates (>6 mm) to 30-60° with grinder or torch, leaving 1-3 mm root gap. Clean to bare metal (no rust, oil, paint — all cause defects).
- **Safety**: UV radiation from arc causes "welder's flash" (sunburn of cornea — extremely painful, temporary blindness for 24-48 hours). ALWAYS use welding helmet with proper shade lens (#10-14 shade). Leather gloves, long sleeves (UV burns exposed skin). Sparks and spatter — fire hazard, clear combustibles 10+ m away. Ventilation — welding fumes contain metal oxides, especially hazardous with galvanized steel (zinc fume fever). NEVER weld in confined spaces without forced ventilation.
- **Applications**: Structural steel construction, pressure vessels, shipbuilding, pipe welding, machinery repair. Stronger and faster than oxy-acetylene for steel fabrication.

## Enables (Downstream)

| Output | Used By |
|--------|---------|
| Steam power | Phase 5 (chemical plant machinery, pumps, compressors), Phase 7 (silicon furnace) |
| Electricity (DC and AC) | ALL downstream phases — every motor, furnace, electrolysis cell, lamp |
| Arc furnaces | Phase 7 (MG-Si production, electrodes), Phase 5 (specialty steel, carbides) |
| Electrolysis | Phase 5 (chlorine, alkalis, aluminum, magnesium, sodium) |
| Electric motors | Phase 5 (mixers, pumps, blowers), Phase 7 (crystal pullers), Phase 8 (fab equipment) |
| Wire/cables | Phase 4 (distribution), Phase 6 (coils, electromagnets), Phase 8 (interconnects concept) |
| Transformers | Phase 4 (power distribution), Phase 6 (high voltage), Phase 7 (furnace power) |
| ICE | Phase 4 (mobile power), SQ 13 (aircraft propulsion), SQ 3 (vehicles) |
| Coke | Phase 7 (silicon furnace carbon source), Phase 5 (blast furnace fuel) |

## Key Feedback Loop

```
Electricity → powers better machine tools → better generators → more electricity
Electricity → powers arc furnaces → better steel → better machines
Steam → powers factories → more materials → better steam engines
```

## Practical Bottlenecks

- **Cylinder boring precision**: Without accurate boring (Phase 3), steam engines leak and lose efficiency. Piston-cylinder clearance must be <0.5 mm for useful work. Newcomen tolerated more; Watt engines demanded less.
- **Copper wire production**: Drawing long, consistent wire requires good dies (hardened steel or tungsten carbide) and lubrication. A single generator may need 5-20 km of wire.
- **Insulation**: Finding adequate wire insulation materials (natural rubber, varnished cloth, gutta-percha). Each has temperature and voltage limitations. Rubber degrades above ~60°C continuous.
- **Scale**: Moving from laboratory demos (100W) to industrial-scale power generation (10-100+ kW) requires enormous copper, iron, and construction effort.
- **Boiler safety**: Riveted iron boilers at 2-10 bar are explosion hazards. Proper construction, testing, and safety valves are non-negotiable.

## Safety Concerns

- **Boiler explosions** (catastrophic): Even low-pressure (2 bar) boilers contain enormous energy. A 1 m³ steam explosion releases energy equivalent to ~1 kg TNT. NEVER exceed rated pressure. Test with hydrostatic pressure (water, not steam) at 1.5x working pressure before first firing.
- **Electrical shock and electrocution**: DC at 50V+ can be lethal if current passes through chest. AC at lower voltages also dangerous. Insulate all connections. Keep hands dry. Use one-hand rule when working on live circuits.
- **Coal mine hazards** (collapse, gas, flooding): See [SQ 11](../side-quests/sq-11-mining-engineering.md). Fire damp (methane) and choke damp (CO₂) are deadly.
- **Arc furnace UV radiation and high temperatures**: Welder's flash (UV keratitis — painful eye inflammation). Face shield mandatory. Temperature 3000°C+ — everything nearby burns.
- **CO poisoning**: Incomplete combustion in confined spaces. Symptoms: headache, dizziness, nausea → unconsciousness → death. Ventilate all combustion appliances.

## Resource Estimates

| Resource | Amount | Notes |
|----------|--------|-------|
| Coal for coke | 2-5 tonnes/day | Per beehive oven (3-6 tonne charge) |
| Coke for blast furnace | ~0.5-1 tonne coke per tonne iron | Pig iron production |
| Copper for generator | ~50-200 kg per kW | Wire, windings, bus bars |
| Iron for steam engine | 2-10 tonnes | Cast and wrought iron per engine |
| Water for steam | 5-10 kg steam per kWh | Make-up water for boilers |

## Side Quest Dependencies

- **Lubricants & Oils ([SQ 10](../side-quests/sq-10-lubricants-oils.md))** — critical for wire drawing (soap/tallow lubrication) and cylinder lubrication in steam engines. ICE requires specialized oil (castor oil or mineral oil).
- **[SQ 13: Aircraft Development](../side-quests/sq-13-aircraft-development.md)** — ICE provides propulsion; aircraft is the most demanding mobile power application
- **[SQ 14: Polymers & Composites](../side-quests/sq-14-polymers-composites.md)** — elastomer processing (vulcanization, molding) uses Phase 4 electric heating; synthetic rubber requires Phase 5 feedstocks

[← Phase 3](phase-03-machine-tools.md) | [Overview](overview.md) | [Phase 5: Chemistry →](phase-05-chemistry.md)
