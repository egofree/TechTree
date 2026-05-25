# Drilling

> **Node ID**: mining.drilling
> **Domain**: [Mining](./index.md)
> **Dependencies**: [`energy.steam-power`](../energy/steam-power.md), [`machine-tools.machining`](../machine-tools/machining.md), `mining`
> **Enables**: None (leaf capability)
> **Timeline**: Years 12-20
> **Outputs**: blast_holes, core_samples, exploration_data

### Hand Steel Drilling

Before pneumatic or hydraulic drills, miners broke rock with hand steel. A steel drill (also called a jumper) is a hardened chisel-pointed rod, driven into rock by hammer blows. One person rotates the drill slightly between strikes to prevent binding and distribute the cutting edge across the rock face.

**[Single jack drilling](../glossary/single-jack-drilling.md)** (one person, one hammer):
- One hand holds and rotates the drill steel, the other swings a 2-3 kg hammer. The drill steel is typically 600-1200 mm long, 19-25 mm diameter, with a forged chisel point at the working end and a slightly widened head (to prevent mushrooming over the holder's hand).
- Advance rate: 0.3-0.5 m/hour in granite. A full shift yields 2-3 m of hole in hard rock, more in softer rock like limestone (4-6 m/day). The rate drops as hole depth increases because deeper holes are harder to clean and the longer steel flexes more under each blow.
- Water is poured into the hole periodically to make a slurry that floats out rock dust and keeps the bit cutting clean. Dry drilling in silica-bearing rock generates respirable quartz dust, the direct cause of silicosis.
- The striker's accuracy matters. Missed strikes deform the drill steel head into a "mushroom" that can send sharp spalls flying. Eye protection is essential. Experienced strikers develop a rhythm of one blow per 1-2 seconds with consistent force.

**[Double jack drilling](../glossary/double-jack-drilling.md)** (two people, one sledge):
- One person holds and rotates the drill steel. A second swings a 4-6 kg sledge hammer. Advance rate roughly doubles to 4-6 m/day in hard rock.
- The holder faces away from the striker and times rotation to the striker's rhythm. Trust and communication are critical. The holder signals readiness by tapping the drill against the rock face between strikes. Mis-timed strikes can injure the holder's hands.
- For deep holes, drill steels are used in sets of increasing length (300 mm, 600 mm, 900 mm, 1200 mm). Short steels start the hole, longer steels extend it. Each successive steel has a slightly wider diameter to prevent binding in the tapered hole.

### Drill Steel and Bit Design

**[Carbon steel bits](../glossary/carbon-steel-bits.md)** (standard for hand drilling and early machine drilling):
- High-carbon steel (0.6-0.8% carbon), forged to shape and hardened by quenching in water or oil from 800-820°C. Tempered at 300-400°C to reduce brittleness while maintaining edge hardness (Rockwell C 50-58).
- Sharp chisel edge dulls quickly in hard rock. Needs re-forging every 0.5-1 m of drilling in granite. In soft rock (coal, shale), a single bit may drill 3-5 m before resharpening.
- Re-sharpening: heat to bright red (850-900°C), re-forge the chisel edge on anvil, re-harden and temper. A mine drill sharpener services dozens of bits per shift at a small forge set up near the working face.

**[Tungsten carbide insert bits](../glossary/tungsten-carbide-insert-bits.md)** (for hard rock and pneumatic drills):
- Small tungsten carbide inserts (WC-Co alloy, 6-10% cobalt binder) brazed into a steel body. The carbide cutting edge retains hardness at temperatures where steel softens (above 600°C), which matters in dry or deep drilling where the bit heats up.
- Insert shapes: chisel (two cutting edges, for hand drilling and jackhammers), cross (four edges, for machine drilling in hard rock), button (hemispherical carbide buttons, for rotary-percussive drilling in very hard rock).
- Service life: 30-100 m of drilling per set of inserts before re-grinding or replacement, compared to 2-5 m for carbon steel in the same rock. The higher upfront cost of carbide is repaid many times over in reduced downtime and labor.
- Brazing the inserts: the steel bit body is heated, a copper-silver-zinc brazing alloy (melting point 650-700°C) flows between the carbide insert and the steel, and the assembly is cooled. The braze joint must be thin (0.05-0.15 mm) and void-free to transfer impact energy efficiently from the steel body to the carbide cutting edge. A poorly brazed insert chips or falls out under the first few hammer blows.

**Bit maintenance and regrinding**:
- Tungsten carbide bits dull gradually. The cutting edges round over, reducing penetration rate. Regrinding with a diamond-impregnated grinding wheel restores the sharp edge. A typical bit is reground 3-5 times before the insert is worn too short to hold in the steel body.
- Regrinding schedule: every 30-50 m in hard rock (granite), every 80-120 m in medium rock (limestone). Delaying regrinding reduces penetration rate by 30-50% and increases the risk of bit seizure in the hole.

### Pneumatic Drills

Compressed air powers the percussive mechanism that replaces hand hammering. The drill piston oscillates inside a cylinder, striking the drill steel shank on each forward stroke.

**Jackhammer (hand-held percussion drill)**:
- Weight: 15-30 kg. Requires compressed air at 500-700 kPa (5-7 bar), consuming 2-4 m³/min of free air. A single compressor (50-100 kW) can supply 3-6 jackhammers simultaneously through a manifold and hose network.
- Bore diameter: 25-40 mm typical for blast holes. Depth: 2-4 m practical maximum for hand-held work. Beyond 4 m, the drill steel whip and weight make accurate control difficult.
- Piston delivers 1500-2500 blows per minute at 5-7 bar. The drill steel rotates a few degrees between blows (independent rotation mechanism: rifle bar or fluted piston). Rotation speed: 50-150 RPM.
- Water flush through hollow drill steel suppresses dust and clears cuttings. Minimum water flow: 4-8 liters per minute. Dry drilling generates respirable silica dust.
- The operator pushes against an air-leg (pneumatic cylinder) that supports the drill weight and provides feed force. Air-leg extended length 1.2-1.8 m, providing 500-1500 N thrust at 5 bar.

**[Drifter drill](../glossary/drifter-drill.md)** (mounted on a boom or carriage):
- Larger piston (60-100 mm bore), heavier frame, higher feed force. Cannot be hand-held. Mounted on a drill jumbo (underground) or crawl carriage (surface).
- Air consumption: 8-15 m³/min. Drills holes 38-64 mm diameter, 3-5 m deep. Feed force: 500-3000 N, adjustable via pneumatic chain or screw feed.
- Drill jumbo: a mobile platform with 1-3 hydraulic or pneumatic booms, each carrying a drifter drill. One operator can drill an entire heading round from a single position. A 2-boom jumbo drills 30-50 holes (3 m deep each) in 2-3 hours, replacing a crew of 4-6 men with hand-held jackhammers.

### Core Drilling (Prospecting)

Core drilling extracts a cylindrical sample of rock for geological analysis. Unlike percussion drilling (which pulverizes rock), core drilling preserves the rock structure for visual inspection, assay, and geotechnical testing.

**Diamond core drilling**:
- A hollow drill bit set with industrial diamonds (or synthetic diamond) rotates against the rock face, cutting an annular ring. The intact core passes up into a core barrel inside the drill string. The bit face contains 4-12 carats of diamond per inch of bit diameter, set in a tungsten carbide or bronze matrix.
- Core sizes (standard): AQ (27 mm core, 48 mm hole), BQ (36.5 mm core, 60 mm hole), NQ (47.6 mm core, 76 mm hole), HQ (63.5 mm core, 96 mm hole), PQ (85 mm core, 123 mm hole). Larger core gives better samples but costs more per meter in diamonds, fuel, and time.
- Rotation speed: 300-1200 RPM depending on bit diameter and rock hardness. Smaller bits spin faster. Weight on bit: 100-500 kg depending on bit diameter. Too much weight fractures the core; too little produces slow penetration.
- Penetration rate: 2-10 m/hour in medium-hard rock (granite), 10-25 m/hour in soft rock (shale). Bit life: 20-100 m per bit depending on rock abrasiveness and bit quality.
- Water circulation: 10-30 liters/min pumps water down the inside of the drill string, returns between the drill rod and borehole wall, carrying rock cuttings to surface while cooling the bit. In cold climates, the return water must be heated to prevent freezing in the drill rods.

**Wireline system**:
- The core barrel is retrieved by lowering a wire cable with a locking spear (overshot) through the inside of the drill string. The spear latches onto the core barrel head and pulls the full barrel to surface.
- Eliminates the need to pull the entire drill string (hundreds of meters of rods) each time the core barrel fills (every 1.5-3 m). A wireline round trip takes 5-15 minutes at 200 m depth vs. 1-2 hours for rod tripping.
- The empty inner barrel is lowered back down on the wireline, landing in the outer barrel to continue drilling. Only the inner barrel and core are handled between runs.
- Wireline cable: galvanized steel wire rope, 4-6 mm diameter, with a breaking strength of 10-20 kN. The cable is spooled on a winch drum (typically 500-2000 m capacity) driven by a hydraulic motor. Winch speed: 0-3 m/s, adjustable for safe landing of the overshot onto the core barrel.

**Core handling**:
- Retrieved core is extruded from the inner barrel into a split-core box (wooden or plastic tray with 5 rows of 1 m slots, holding 5 m of core per box). The core is washed, photographed, logged (geologist records rock type, mineralization, structure, and orientation), then sampled (split lengthwise with a diamond saw; one half is sent to the assay laboratory, the other half is archived).
- Core recovery (the percentage of the drilled interval actually recovered as core) is a key quality metric. Recovery below 85% indicates broken or lost core, usually caused by fractured ground, insufficient water circulation, or excessive weight on bit. Recovery below 50% means the drilling data is unreliable for resource estimation.

### Blast Hole Drilling

Blast holes are drilled in a pattern (grid) across the rock face, loaded with explosive, and fired to break the rock into manageable fragments. The drilling pattern is the most important variable in blast design: hole depth, spacing, burden (distance to the free face), and angle all affect fragmentation size, throw distance, and vibration.

**[Jackhammer blast holes](../glossary/jackhammer-blast-holes.md)** (small-scale underground):
- Diameter: 32-40 mm. Depth: 1.5-3.0 m. Spacing: 0.4-0.8 m between holes in hard rock, wider in softer rock.
- Pattern: parallel holes (burn cut) or angled holes (V-cut, fan cut). A typical round in a 3×3 m heading requires 30-50 holes. The burn cut pattern uses closely-spaced parallel holes in the center, loaded lightly or left empty, to create a free face for the surrounding holes to break toward.
- Specific charge (explosive per cubic meter of rock): 1.0-2.5 kg/m³ for hard rock. Lower values produce larger fragments (easier to handle but may need secondary breaking); higher values produce finer fragmentation but more vibration and fly rock.
- Drilling time: 1-3 hours for a full round, depending on rock hardness and number of drills working simultaneously.

**[Long-hole drilling](../glossary/long-hole-drilling.md)** (mechanized underground):
- Hydraulic or pneumatic long-hole drill on a boom mount. Diameter: 50-100 mm. Depth: 10-30 m. Used for bench mining, sub-level caving, and large stope blasting.
- Larger diameter allows bulk emulsion or ANFO charging. A single long-hole round may contain 500-5000 kg of explosive, breaking 1000-10,000 tonnes of rock.

### Drilling Fluid Circulation

Drilling fluid (mud or water) serves four functions: cools the bit, removes cuttings, supports borehole walls against collapse, and lubricates the drill string to reduce friction. Without fluid, the bit overheats and the cuttings pack the hole, seizing the drill string.

**[Water flush](../glossary/water-flush.md)** (simple, for short holes):
- Clean water pumped at 10-30 liters/min through hollow drill steel. Works for shallow blast holes and diamond drilling in competent (solid) rock. No additives needed.

**[Drilling mud](../glossary/drilling-mud.md)** (for deep or unstable holes):
- Bentonite clay (sodium montmorillonite) mixed with water to specific density (1.05-1.20 g/cm³). The mud forms a filter cake on the borehole wall, preventing collapse in loose or fractured ground. Bentonite swells 10-15 times its dry volume when hydrated, creating a viscous, thixotropic fluid (thin when stirred, gels when standing).
- Mud properties: viscosity 30-40 seconds (Marsh funnel), yield point 5-15 Pa, fluid loss < 10 ml in 30 minutes. These properties are measured on-site with simple instruments. Viscosity too high: pump works too hard, penetration drops. Viscosity too low: cuttings settle, hole collapses.
- Mud circulation system: mud pump (positive displacement, triplex piston pump, 50-200 kW) pushes mud down the drill string at 5-20 MPa pressure. Mud returns through the annulus, carrying cuttings to surface. At surface, mud flows through settling tanks (2-4 m³, allowing coarse cuttings to settle), then shale shakers (vibrating screens, 0.5-2 mm mesh) that remove fine cuttings before the mud returns to the suction tank for re-circulation.

**[Foam drilling](../glossary/foam-drilling.md)** (alternative for dry holes):
- In areas where water is scarce or the formation swells when wet (some clays expand dramatically on contact with water), foam replaces liquid mud. A surfactant (foaming agent, 0.5-2% solution) is injected into the compressed air stream. The resulting stiff foam carries cuttings to the surface and provides borehole support.
- Foam drilling uses less water (10-30 liters/min vs. 100+ liters/min for mud drilling) and does not swell water-sensitive formations. But foam stability is temperature-sensitive, and the method does not work in heavily water-producing formations where groundwater washes out the foam.

### Borehole Surveying

Deviated boreholes waste drilling effort and produce misleading geological data. Holes deviate because the drill string bends under its own weight and the bit deflects off harder rock layers.

**[Acid etch survey](../glossary/acid-etch-survey.md)** (simplest method):
- A glass bottle half-filled with hydrofluoric acid (HF) is lowered into the borehole on a wire and left for 20-30 minutes. HF etches the glass at the acid-air interface, marking the horizontal plane. The etch line angle from the bottle's axis gives borehole inclination.
- Inexpensive, no electronics required. Only measures inclination, not azimuth (direction). HF is extremely hazardous (causes deep tissue burns, bone decalcification). Must be handled in thick polyethylene containers with calcium gluconate gel available as first aid.

**Magnetic survey instruments**:
- A compass and plumb-bob in a sealed brass pressure barrel record azimuth and inclination on photographic film. Lowered on wireline, triggered by a timer or motion switch. Single-shot (one reading per trip) or multi-shot (readings every 3-10 m as the instrument is lowered or raised).
- Accuracy: ±0.5° inclination, ±1° azimuth (away from steel drill rods or other magnetic interference). Readings must be taken with the instrument at least 3-5 m from any steel casing for reliable azimuth.

### Compressed Air Supply

Pneumatic drills require a reliable supply of compressed air at 500-700 kPa. The air supply infrastructure is a significant part of the overall drilling system.

**Compressor types**:
- Reciprocating compressor: piston-driven, single or multi-stage. A 2-stage compressor compresses air to 700 kPa in two steps with intercooling between stages (reduces work and discharge temperature). First stage compresses to ~250 kPa, intercooler drops temperature, second stage reaches 700 kPa. Input power: 50-100 kW per drill served. Driven by electric motor, diesel engine, or steam engine.
- Rotary screw compressor: two intermeshing helical rotors compress air continuously. Quieter, more compact than reciprocating. Oil-injected type is most common (oil seals rotor clearances and cools the air). Requires oil separator filter before air reaches the drills.

**Air distribution**:
- Main line: 75-150 mm steel pipe from compressor to the working area. Branch lines: 25-50 mm rubber hose to individual drills. Total hose length should not exceed 100-150 m per drill, or pressure drop reduces drill performance below acceptable levels.
- Moisture: compressed air contains water vapor that condenses as the air cools in the distribution lines. Water in the drill causes rust and washes away lubrication. Moisture separators (cyclone or coalescing filters) installed at low points in the line, with drain valves opened daily.
- Receiver tank: a pressure vessel (0.5-5 m³) installed between compressor and distribution line. Dampens pressure pulsations from reciprocating compressors, stores compressed air for short peak demands (starting multiple drills simultaneously), and provides a settling volume where water and oil droplets separate from the air stream.

**Lubrication of pneumatic drills**:
- Pneumatic drill pistons and cylinders require continuous lubrication. An inline lubricator (a small reservoir of light machine oil, 100-200 ml, installed in the air hose near the drill) meters oil into the air stream at 2-5 drops per minute. The oil mist coats the cylinder walls and piston rings as the air passes through.
- Without lubrication, the piston seizes in the cylinder within 30-60 minutes of operation. Excessive oil causes the drill to "diesel" (oil ignites from compression heat), producing erratic firing and carbon deposits.

### Safety

Drilling is one of the most hazardous activities in mining. The combination of high-energy impacts, rotating steel, dust, noise, and pressurized fluid creates multiple injury pathways that must be managed simultaneously.

- **Silica dust**: The primary health hazard. Rock drilling generates respirable crystalline silica (< 10 μm particles). Silicosis is irreversible and fatal. Wet drilling suppresses 90-95% of dust. Respirators (P100 filtration) required for any dry drilling or dust cleanup. Exposure limit: 0.025 mg/m³ (OSHA) for respirable crystalline silica as an 8-hour time-weighted average.
- **Noise**: Pneumatic drills produce 110-120 dB. Hearing damage begins at 85 dB over 8 hours (the permissible exposure limit in most jurisdictions). At 110 dB, the permissible exposure without hearing protection is less than 2 minutes. Ear protection (foam plugs: 25-30 dB reduction, or earmuffs: 25-35 dB reduction) is mandatory and reduces exposure to safe levels.
- **High-pressure air**: Compressed air at 5-7 bar can inject through skin causing air embolism (gas bubbles in the bloodstream, potentially fatal if they reach the brain or heart). Never point air hoses at people. Whip checks (safety cables) on all hose connections to prevent whipping if a coupling fails under pressure.
- **Drill steel failure**: Fatigue-fractured drill steel can fly out of the hole. The steel whip can cause severe lacerations or broken bones. Stand clear of rotating steel during operation. Never use bent, cracked, or mushroomed steel. Inspect steel before each shift for cracks near the shank end (the highest-stress area).
- **Entanglement**: Loose clothing, long hair, or jewelry caught in rotating drill steel pulls the wearer into the machinery with devastating speed. Wear close-fitting clothing, secure long hair under a cap, and remove rings and bracelets before operating drills.

### Rock Properties and Drillability

Rock drillability determines bit selection, penetration rate, and cost per meter. The key properties are compressive strength, abrasiveness, and joint/fracture density.

**[Compressive strength](../glossary/compressive-strength.md)** (uniaxial):
- Soft rock (coal, shale, evaporites): 10-50 MPa. Easy to drill with carbon steel bits at 0.5-1.0 m/hour (hand steel) or 10-30 m/hour (pneumatic).
- Medium rock (sandstone, limestone): 50-150 MPa. Requires tungsten carbide bits. Penetration rates roughly half those in soft rock.
- Hard rock (granite, basalt, gneiss): 150-300 MPa. Requires tungsten carbide or button bits at maximum feed pressure. Penetration rates 30-50% of soft rock rates.

**[Abrasiveness](../glossary/abrasiveness.md)** (determines bit wear):
- Measured by the Cerchar Abrasivity Index (CAI): a steel needle dragged across a rock surface under 70 N load, examined under a microscope for wear. CAI 0.5-1.0 = low abrasiveness (limestone, marble). CAI 2.0-4.0 = high (granite, quartzite). CAI > 4.0 = extreme (flint, chert).
- High abrasiveness requires carbide button bits (not chisel bits), generous water flush, and frequent bit changes. Bit cost per meter can be 5-10× higher in abrasive rock than in non-abrasive rock of similar strength.

### Historical Progression

The arc from hand steel to pneumatic drilling took about a century:

1. **Pre-1850**: Hand steel only. Single jack for soft rock, double jack for hard. Rates of 2-6 m/day. Miners relied on plug-and-feather splitting or black powder in hand-drilled holes.
2. **1850-1870**: Early pneumatic drills appear (Cowan, Schumann, Sommeiller). Heavy, unreliable, but proved the concept of compressed-air-powered percussion. Compressed air generated by steam-driven compressors. Sommeiller used pneumatic drills to bore the Mont Cenis tunnel through the Alps (1857-1870).
3. **1870-1900**: Pneumatic drill refinement. Ingersoll Rock Drill (1871), Leyner drill (1897, first with hollow drill steel for water flush). Rates climbed to 30-80 m/day with mechanized drills. Hand steel persisted in narrow veins and small mines where jackhammers could not fit.
4. **1900-1950**: Tungsten carbide bits adopted widely (post-WWII, originally developed in Germany by Krupp). Diamond core drilling standard for exploration. Hydraulic drills begin supplementing pneumatic.
5. **Post-1950**: Hydraulic drills dominate new installations (higher efficiency: 40-50% vs. 15-20% energy efficiency for pneumatic, lower noise: 95-105 dB vs. 110-120 dB, no compressed air infrastructure). Down-the-hole (DTH) hammers for large-diameter surface blast holes. Top hammer drills for underground development. Modern hydraulic drills achieve 100-200 m/day in hard rock with a single operator.

### Down-the-Hole (DTH) Drilling

DTH drilling places the percussive hammer directly behind the drill bit at the bottom of the borehole, rather than at the surface transmitting blows through the drill string. This eliminates energy loss through the drill string (which can be 50-70% of input energy at depths over 30 m with top-hole hammers).

**DTH hammer operation**:
- A pneumatic or hydraulic hammer mechanism sits directly above the bit inside the borehole. Compressed air or hydraulic fluid powers the piston, which strikes the bit shank directly. The drill string above the hammer serves only to rotate the assembly and supply power (air or fluid).
- Air consumption: 10-25 m³/min at 7-25 bar (higher pressure than jackhammers). Hole diameter: 75-200 mm. Depth capability: 50-300+ m. Used primarily in surface mining and quarrying for large-diameter blast holes.
- The exhaust air from the pneumatic hammer exits through the bit, providing excellent hole cleaning (cuttings are blown back up the annulus at high velocity). This self-cleaning action is a significant advantage over top-hole hammer drilling in deep holes.

### Rotary Drilling

Unlike percussive drilling (which chips rock by impact), rotary drilling grinds rock by pressing a rotating bit against the formation under high load. Rotary drills are used for large-diameter holes in surface mining and oil/gas wells.

**[Tricone roller bit](../glossary/tricone-roller-bit.md)** (standard for large blast holes):
- Three conical rollers, each studded with tungsten carbide buttons, rotate on bearings as the bit turns. The buttons crush and shear the rock under the combined effect of rotation and downward pressure (weight on bit: 5-30 tonnes depending on hole diameter and rock hardness).
- Hole diameter: 150-380 mm. Rotation speed: 60-120 RPM. Penetration rate: 10-40 m/hour in medium-hard rock (much faster than percussive drilling in large diameters).
- Air or mud circulation clears cuttings. Air is preferred for blast holes (faster, no mud disposal); mud is required for deep or unstable holes.

### Drill Steel Maintenance

**Sharpening**: Grind chisel bits to the correct included angle for the rock type: 90-110° for hard rock (granite, quartzite — narrower angle penetrates but dulls faster), 110-130° for soft rock (limestone, shale — wider angle resists wear). Use a pedestal grinder with a silicon carbide or aluminum oxide wheel (46-60 grit). Cool the bit frequently in water to prevent overheating (above 250°C the tempered steel loses hardness). A properly sharpened bit has a straight, even cutting edge with no rounding or chipping.

**Rehardening after multiple sharpenings**: After 3-5 resharpenings, the bit nose shortens and the cutting edge reaches into softer (unhardened) steel. Rehardening restores full hardness: heat the bit nose to 780-820°C (cherry red color in dim light) in a forge or with an oxy-propane torch. Hold at temperature for 2-3 minutes to through-heat the working end. Quench immediately in oil (preferred for drill steel — less cracking than water quench) or water. Temper immediately after quenching at 200-250°C for 30-60 minutes to relieve brittleness while maintaining Rockwell C 55-60 hardness. Do not skip tempering — untempered martensite is glass-brittle and shatters under the first hammer blow.

**Drill steel service life**: In hard rock (granite, compressive strength 150-300 MPa), a carbon steel bit drills 30-60 m of hole before resharpening is needed. In soft rock (shale, limestone, 10-50 MPa), a single bit may drill 100-200 m. Tungsten carbide insert bits outlast carbon steel by 10-20×: 300-1000 m in hard rock before regrinding. Total drill steel life (including resharpening cycles): carbon steel shanks last 200-500 m of total drilling before the shank end mushrooms or the steel fatigues; high-quality alloy steel shanks last 500-1500 m.

### Key Deliverables

- Hand steel drilling capability (survival fallback, no infrastructure required)
- Pneumatic jackhammer and air-leg drilling (primary underground method)
- Diamond core drilling for geological exploration with wireline retrieval
- Blast hole drilling patterns for underground and surface mining
- Drilling fluid circulation systems (water, mud, and foam)
- Borehole surveying methods (acid etch and magnetic)
- Compressed air supply infrastructure (compressors, receivers, distribution)
- DTH and rotary drilling for surface mining applications

### Cross-References

- **Compressed air supply**: [steam power](../energy/steam-power.md)
- **Explosives for blast holes**: [Black Powder](black-powder.md)
- **Drill steel material**: [iron and steel](../metals/iron-steel.md)
- **Machine tools for bit sharpening**: [machine tools](../machine-tools/index.md)
- **Mine ventilation (dust control)**: [ventilation](ventilation.md)

---

*Part of the [Bootciv Tech Tree](../index.md) · [Mining](./index.md) · [All Domains](../index.md)*

[← Back to Mining](index.md)
