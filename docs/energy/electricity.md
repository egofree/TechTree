# Electricity Generation & Distribution

> **Node ID**: energy.electricity
> **Also covers**: `chemistry.electrolysis`, `machine-tools.joining`
> **Domain**: [Energy](./)
> **Dependencies**: `chemistry`, `machine-tools`, `metals.iron-steel`, `chemistry.petroleum-alternatives`
> **Enables**: `energy.electric-furnaces`, `chemistry.electrolysis`, `machine-tools.joining`, `silicon.mg-si-production`, `chemistry.air-separation`, `chemistry.dopant-etch-gases`, `chemistry.hydrogen-silane`
> **Timeline**: Years 15-30
> **Outputs**: generators, motors, transformers, wire_cables, electricity, insulated_wire, electric_arc_furnaces, resistance_heaters, eaf_steel, internal_combustion_engines, ...

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
- **Critical for**: Steelmaking (recycling scrap → quality steel), silicon reduction (the Silicon stage — SiO₂ + 2C → Si + 2CO at ~2000°C), calcium carbide production (CaO + 3C → CaC₂ + CO at ~2000°C).

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
  - **Cylinder**: Cast iron or steel, bored to 0.02-0.05 mm tolerance. Requires the Machine Tools stage boring capability. Honed to mirror finish.
  - **Piston**: Cast iron or aluminum alloy (from metallurgy). Cast iron piston rings (2-3) provide gas seal against cylinder wall. Ring gap ~0.3-0.5 mm when installed.
  - **Crankshaft**: Forged steel, ground journals. Counterweights for balance. Requires lathe, grinder, and balancing.
  - **Connecting rod**: Forged or machined steel I-beam section. Big end (crank end) with split bearing shells (babbitt metal: tin-antimony-copper alloy, 80/10/10 typical). Small end (piston end) with bronze bushing.
  - **Valves**: Poppet valves (intake and exhaust). Machined from heat-resistant steel. Seat angle 45°. Springs return valves to closed position. Operated by camshaft (gear or chain driven from crankshaft at half crank speed for 4-stroke).
  - **Camshaft**: Cast iron or steel. Cam lobes ground to precise profile controlling valve timing and lift duration.
- **Carburetor**: Venturi — air flows through constriction, creating low pressure that draws fuel through metering jet. Adjustable needle valve controls fuel-air ratio (~12-15:1 by weight for gasoline). Simpler than fuel injection and sufficient for early engines.
- **Ignition**: Magneto (permanent magnet + coil generates high voltage pulse when triggered by cam — self-contained, no battery). Spark plug (steel shell, ceramic insulator, center electrode, ground electrode, ~0.6-0.8 mm gap). Secondary voltage ~10,000-30,000V.
- **Lubrication**: Splash system (rod dips into oil sump, splashes oil onto cylinder walls and bearings) or pressurized (gear pump circulates oil through galleries). Oil: castor oil or mineral oil (see [Lubricants](../chemistry/lubricants.md)).
- **Cooling**: Water jacket around cylinder, thermosiphon circulation (hot water rises to radiator, cools, returns) or pump-forced circulation. Finned air cooling for small engines.
- **Power output**: 5-65 HP for 1-4 cylinders, 1000-3000 RPM. Power-to-weight ratio is THE critical metric for aircraft (see [Aircraft](../transport/aviation.md)).

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
- Lubrication is critical at every pass (tallow or soap solution; see [Lubricants](../chemistry/lubricants.md)); without it the wire galls and snaps
- Wire annealing between passes restores ductility lost from cold working
- Insulation (rubber, varnished cloth, gutta-percha) is applied after drawing, not during

### Electrical Engineering Reference

**Copper wire gauge table** (practical reference for all electrical work):
| Diameter (mm) | Cross-section (mm²) | Resistance (Ω/km) | Max current (A) | Typical use |
|---------------|---------------------|--------------------|-----------------|-------------|
| 0.1 | 0.008 | 2,200 | 0.05 | Fine coils, instruments |
| 0.2 | 0.031 | 560 | 0.15 | Meter movements |
| 0.5 | 0.20 | 88 | 1.0 | Small transformers |
| 1.0 | 0.79 | 22 | 5 | Motor windings, generator coils |
| 1.5 | 1.8 | 12 | 10 | Lighting circuits |
| 2.0 | 3.1 | 7.0 | 15 | Power outlets |
| 2.5 | 4.9 | 4.5 | 20 | Branch circuits |
| 4.0 | 12.6 | 1.7 | 40 | Sub-main feeds |
| 6.0 | 28.3 | 0.77 | 70 | Main distribution |
| 10.0 | 78.5 | 0.28 | 130 | Service entrance, bus bars |

- Max current assumes 3-5 A/mm² for enclosed wiring (derate for bundling or high ambient temperature). Open air or short runs can carry more.
- Voltage drop: ΔV = I × R = I × (ρ × L / A), where ρ = 0.0175 Ω·mm²/m for copper, L = length (m), A = cross-section (mm²). Keep voltage drop under 3-5% for efficient operation.
 - Example: 10 A load, 100 m run, 110V supply, max 5% drop (5.5V): Wire resistance = 5.5V / 10A = 0.55Ω. R per conductor = 0.275Ω for 100m = 2.75 Ω/km. From table: ~2.0 mm diameter wire (1.8 mm² cross-section, 12 Ω/km × 0.1 km = 1.2 Ω per conductor... need 2 conductors → 2.4 Ω total, voltage drop = 24V. Too much. Need 6 mm wire: 0.77 Ω/km × 0.1 km = 0.077 Ω per conductor → 0.154 Ω total → 1.54V drop = 1.4%. OK.)

**Motor and generator sizing**:
- **Motor power**: Mechanical power P = T × ω (torque × angular velocity). At 1500 RPM (157 rad/s), 1 Nm torque = 157W. A 1 kW motor at 1500 RPM delivers ~6.4 Nm.
- **Motor current**: I = P / (V × η × PF), where η = efficiency (0.7-0.9), PF = power factor (1.0 for DC, 0.7-0.85 for AC induction motors). Example: 1 kW motor at 220V AC, η=0.8, PF=0.8: I = 1000/(220 × 0.8 × 0.8) = 7.1A.
- **Generator sizing**: Must match peak load + 20% margin. If total connected load = 5 kW with 60% diversity factor (not all running simultaneously), generator needs 5 × 0.6 × 1.2 = 3.6 kW minimum. Round up to nearest available size.

**Fuse and circuit breaker selection**:
- **Fuse**: Short piece of wire or strip that melts at a known current, breaking the circuit. Lead-tin alloy for low-current fuses (1-15A), copper or silver for higher currents. Enclose in ceramic or glass tube with filler (sand) to quench arc when fuse blows. Rating: fuse should carry 100% rated current indefinitely, blow within 1 hour at 135% rated current, blow quickly at 200%+ rated current.
- **Fuse sizing**: Fuse rating ≥ full-load current of device, but ≤ ampacity of wiring. Example: motor drawing 7A on 2.5 mm² wire (20A capacity) → use 10A fuse. The fuse protects the WIRE, not the device.
- **Circuit breaker**: Bimetallic strip heated by current bends and trips latch, opening contacts. Resettable. More convenient than fuses. Calibrate by adjusting strip tension.

**Battery sizing** (lead-acid, see Energy Storage):
- **Capacity**: C = P × t / V, where P = load (W), t = backup time (hours), V = system voltage. Example: 500W load, 4-hour backup, 48V system: C = 500 × 4 / 48 = 41.7 Ah. Add 50% margin for depth-of- discharge limit: 62.5 Ah bank.
- **Charging current**: C/10 rate (capacity ÷ 10 hours) for maximum battery life. For 62.5 Ah bank: charge at ~6.25A, 48V = 300W charger needed. Charge time: ~12-14 hours from fully discharged.

### Permanent Magnets

- **Lodestone** (naturally magnetized magnetite) for early compasses and basic magnetic experiments
- **Magnetized iron/steel bars**: Stroke with lodestone or place in Earth's magnetic field yields magnets for early generator field poles and galvanometers. For stronger magnets: place steel bar inside coil, pass DC current (electromagnet method) — steel retains magnetism after current removed.
- **Keeper**: Store magnets with soft iron bar across poles (keeper) to prevent demagnetization over time.
 - **Later materials** (Alnico, ferrite) arrive with Chemistry stage alloy development

### Elastomer Processing

- **Natural rubber vulcanization**: latex from *Hevea brasiliensis* or temperate alternatives (guayule, Russian dandelion) is coagulated, masticated on a two-roll mill, then compounded with sulfur (1.5-3 phr) and zinc oxide as activator
- **Heat curing** at 140-180°C in electric vulcanizing presses or steam autoclaves (3-10 bar) using the Energy stage electric heating and boiler steam; cycle times 5-30 minutes depending on thickness
- **Applications beyond wire insulation**: shaft seals, gaskets, flat belts and V-belts for power transmission, hoses, vibration dampers, and tire construction for wheeled vehicles
- **Synthetic rubbers** (nitrile, neoprene) require petrochemical feedstocks from [Petrochemicals](../chemistry/petroleum-alternatives.md); see [Polymers](../polymers/index.md) for the full elastomer development roadmap

### Advanced Welding

**Oxy-acetylene welding and cutting**:
- **Acetylene production**: Calcium carbide (CaC₂, from CaO + 3C at ~2000°C in electric arc furnace) + water → C₂H₂ + Ca(OH)₂. Generate acetylene on demand in gas generator (water dripped onto carbide in closed vessel). NEVER store acetylene under pressure >0.15 MPa — it detonates spontaneously. Store dissolved in acetone in porous-filled cylinder (acetylene cylinders — safe storage at ~1.5 MPa).
- **Oxygen supply**: From air separation (cryogenic distillation — see Air Separation) or from chemical generation (barium oxide process: heat BaO in air → BaO₂, then heat BaO₂ → BaO + ½O₂). Compressed into steel cylinders at 15-20 MPa.
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

### Safety & Hazards

- **Electrocution**: Electrical current through the body causes death at surprisingly low levels — 100 mA across the chest can cause ventricular fibrillation. Even "low" voltages (50V+) can be lethal under wet conditions. ALWAYS de-energize circuits before working on them (lock-out/tag-out). Use insulated tools. One-hand rule when working near live circuits (keep one hand in pocket — prevents current across chest).
- **Arc flash**: Short circuits can produce arcs reaching 20,000°C. Arc blast pressure can throw a person across a room. Arc-rated face shield and flame-resistant clothing for any work on energized panels. Minimum approach distances based on voltage level.
- **High voltage**: Transformers and distribution systems operate at thousands of volts. Treat all high-voltage equipment as energized until proven otherwise. Grounding sticks for discharge before approach. Warning signs and barriers. Only qualified personnel near HV equipment.
- **Fire risk**: Electrical faults (short circuits, overloaded wiring, poor connections) are a leading cause of industrial fires. Proper fusing and circuit breakers on all circuits. No overloaded outlets. Inspect wiring for damage regularly.
- **Generator mechanical hazards**: Generators have rotating shafts and belts. Guard all moving parts. Entanglement hazard — no loose clothing near running generators.

---

*Part of the [Bootciv Tech Tree](../) • [Energy](./) • [All Domains](../)*
