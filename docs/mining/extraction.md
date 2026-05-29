# Mining Extraction

> **Node ID**: mining.extraction
> **Domain**: [Mining](./index.md)
> **Dependencies**: [`animals.draft-power`](../animals/draft-power.md), [`foundations.tools-basic`](../foundations/tools-basic.md), [`mining.prospecting`](prospecting.md)
> **Enables**: [`mining.extraction.black-powder`](black-powder.md), [`mining.processing`](processing.md), [`transport`](../transport/index.md)
> **Timeline**: Years 0-20
> **Outputs**: raw_ore
> **Critical**: No

### Mining Methods

**Surface mining (open pit)**:
- **Planning**: Strip overburden (soil + useless rock) to expose ore body. Bench height 5-15 m. Bench width = height × slope angle (typically 45-70°). Road access on each bench for haulage.
- **Overburden removal**: Hand shovels and wheelbarrows (Foundations), animal-drawn scrapers (Metallurgy), steam or diesel shovels. Ratio: overburden-to-ore should be <3:1 for economic viability.
- **Ore extraction**: Break rock with wedges, fire-setting, or explosives (black powder from the Chemistry stage: KNO₃ + S + C at 75:10:15 ratio). Load into carts by hand. Haul to processing area.
- **Reclamation**: Backfill exhausted pits with overburden. Re-contour and re-vegetate to prevent erosion.

**Placer mining (stream deposits)**:
- **Panning**: Fill shallow pan with gravel, agitate underwater. Heavy minerals settle to bottom. Gold, cassiterite (tin), magnetite (iron) concentrate. One pan processes ~10 kg gravel in 5-10 minutes.
- **Sluice box**: Wooden trough 2-5 m long, 30-50 cm wide, with riffles (cross-bars) on bottom. Gravel shoveled in at head, water carries material through. Heavy particles trap behind riffles. Clean riffles periodically. 50-100x faster than panning.
- **Hydraulic mining**: Direct high-pressure water jet at hillside to wash gold-bearing gravel through sluice. Requires significant water supply and pressure (20-50 m head).

**[Shaft mining](../glossary/shaft-mining.md)** (underground):
- **Shaft sinking**: Dig vertical shaft, typically 2-3 m × 1.5-2 m (enough for one-way traffic + bucket winding). Line walls with timber (oak or pine, 15-25 cm diameter) or stone/brick for permanent shafts. Shaft compartments: one for winding (ore/people), one for ventilation, one for pumping.
- **Timber framing**: Posts (vertical, 15-25 cm), caps (horizontal across top), and sill pieces (across bottom). Frame every 1.5-2 m along shaft. Secure with wooden wedges. Fill space between timber and rock wall with waste rock (gob) for support.
- **Levels (adits)**: Horizontal tunnels driven from shaft at ore-bearing depths. Typical dimensions 1.5-2 m wide × 2-2.5 m high. Timber-supported with sets (posts + cap + sill). Grade slight upward incline (1-3°) toward shaft for water drainage.
- **[Stoping](../glossary/stoping.md)** (ore extraction): Extract ore between levels. Overhand stoping: work upward from level. Underhand: work downward. Shrinkage: leave broken ore in stope as working platform. Cut-and-fill: backfill with waste as you go (better ground control).

**Drift/adit mining** (horizontal entry from hillside):
- Drive horizontal tunnel into hillside at or slightly above valley floor level. Gravity drainage — no pumping needed. Most economical method for hillslope deposits. Minimum 1.5 m wide × 2 m tall. Timber supports every 1-2 m in unstable ground.

### Rock Breaking Techniques

**Hand tools**:
- **Chisel and hammer**: Steel chisel (2-5 cm wide), 2-4 kg hammer. Strike chisel to create groove or hole. Slow but precise. For soft rock (limestone, shale): 0.5-2 m³/shift. Hard rock (granite, quartz): 0.1-0.5 m³/shift.
- **Wedge and feather**: Drill hole (2-3 cm diameter, 10-20 cm deep) with hand drill (steel bar, struck with hammer). Insert two feathers (thin curved shims) and one wedge between them. Strike wedge → splits rock along line of holes. Space holes 15-30 cm apart for controlled break.

**[Fire-setting](../glossary/fire-setting.md)** (ancient technique for hard rock):
- Build hot fire against rock face. Burn 2-4 hours. Rock face reaches 400-600°C. Dash with cold water (or let air cool). Thermal shock cracks rock 5-15 cm deep. Break weakened rock with picks and wedges. Very effective on granite, quartz, hard ores. Consumes enormous wood/charcoal — use sparingly.

**Black powder blasting**:
- **Composition**: 75% KNO₃ (potassium nitrate), 15% charcoal, 10% sulfur. Grind each component separately (NEVER together), mix by tumbling in cloth bag. KNO₃ from cave deposits, saltpeter beds (nitrate-rich soil + urine/manure + lime, leach and crystallize), or guano.
- **Black powder manufacture**:
  1. Pulverize each ingredient separately to fine powder (~100 mesh).
  2. Mix thoroughly: layer ingredients on cloth, roll/tumble for 30+ minutes.
  3. Moisten slightly with water, press into cakes (corning mill or screw press).
  4. Dry cakes, crush and sieve to desired grain size (coarse = slower burn, more lifting power; fine = faster burn, more shattering).
- **Blasting procedure**: Drill hole (2.5-4 cm diameter, 0.5-2 m deep) with jumper drill (steel bar, 1-3 m long, struck with 4-8 kg hammer). Clean hole with scraper. Fill bottom 1/3 with powder. Insert safety fuse (black powder core in tarred cotton sheath) — cut to length for 30-60 second delay. Tamp remaining hole with clay or damp sand (NOT dry sand — sparks from tamping rod ignite powder). Light fuse, retreat. 1-2 kg powder breaks 2-10 m³ rock depending on placement.
- **Safety**: NO smoking, open flames, or spark-producing tools near powder. Store in dry, cool location away from mine. Use non-sparking tools (copper or bronze) for loading. Multiple shots wired to single fuse for simultaneous blast.

### Ventilation

**[Natural ventilation](../glossary/natural-ventilation.md)** (single shaft):
- Single shaft with partition (brattice — wooden or canvas wall dividing shaft into upcast and downcast). Warm air (heated by mine lights and geothermal) rises in one side, cool air descends in other. Limited to ~100 m depth. Seasonal — reverses in winter.

**Dual-shaft ventilation**:
- Separate intake shaft (downcast) and exhaust shaft (upcast). Connect at depth by levels. Intake positioned upwind. Exhaust may be heated by furnace at shaft bottom (warm air rises faster → stronger draft). Effective to ~200-300 m depth.

**Mechanical ventilation**:
- **Bellows**: Large forge bellows at shaft entrance force air underground. Intermittent flow, limited volume.
- **Fan ventilation**: Centrifugal fan (wooden or iron blades in scroll housing), driven by water wheel or steam engine. 5-50 m³/second airflow. Adjustable louvers control flow. Much more reliable than natural ventilation.
- **Air requirements**: Minimum 0.05 m³/second per underground worker. More if blasting (fumes clearance). Replace total mine air volume every 10-30 minutes.

**Gas detection**:
- **Fire damp (methane, CH₄)**: Flammable at 5-15% concentration. Detected by safety lamp (Davy lamp — flame enclosed in fine wire gauze that cools flame below ignition temperature. If methane present, blue halo appears above flame. If air is unsafe, flame extinguishes). Test at roof level (methane lighter than air, accumulates at roof).
- **Choke damp (CO₂)**: Heavier than air, accumulates at floor. Detected by candle flame (extinguishes at ~8% CO₂ — leave immediately). Or bring small animal (bird in cage — more sensitive to bad air).
- **After-damp (CO)**: After explosion or fire. Invisible, odorless, lethal. Detected by chemical indicator or canary (collapses before humans affected). Evacuate immediately if suspected.
- **Hydrogen sulfide (H₂S)**: Rotten egg smell at low concentration, but paralyzes olfactory nerve at higher concentrations so smell disappears. Lethal at 300+ ppm. Chemical detector or lead acetate paper (turns black in H₂S).

### Water Pumping (critical escalation path)

**Manual methods**:
- **Bailing**: Bucket on windlass (hand-cranked drum). One man lifts ~20 liters per bucket, 10-20 buckets/hour. Emergency only.
- **Chain pump**: Endless chain with attached buckets or disks, running in wooden trough. Lifts water 5-15 m. Powered by hand crank or water wheel. 500-2000 liters/hour.

**Powered drainage**:
- **Buddle/water wheel pump**: Water wheel operates crank → piston pump (cast iron cylinder, leather piston seal). Lift height 15-30 m per stage. Multiple stages for deeper mines. 5,000-20,000 liters/hour per pump.
- **[Savery engine](../glossary/savery-engine.md)** (~1698, first practical steam-powered pump): Boil water → fill chamber with steam → condense with cold water injection → vacuum → atmospheric pressure forces water up suction pipe. Lift: ~6-9 m suction + ~10-15 m pressure head. Efficiency ~0.5%. Simpler than Newcomen but limited lift and very wasteful.
- **[Newcomen engine](../glossary/newcomen-engine.md)** (~1712, atmospheric engine): Steam in cylinder → condense → vacuum pulls piston down → pump rod lifted on other end of beam. Lift: 30-50+ m (pump at bottom of shaft, engine at surface). Power: 5-15 HP. THE KEY FEEDBACK LOOP — mine drainage drove steam engine development, which enabled all of the Energy stage.

### Hoisting & Transport

**Windlass**: Horizontal drum, hand-cranked. Rope wound on drum. Simple, limited to ~30 m depth, ~100 kg load. One-man operation.

**Whim (horse whim)**: Vertical drum (6-10 m diameter) turned by horse walking in circle. Rope winds on drum, lifts bucket from shaft. Depth 50-100 m. Load 200-500 kg. One horse provides ~3-4 HP.

**Steam winding engine**: Horizontal steam engine drives winding drum. Speed 5-15 m/second. Depth 200-500+ m. Load 1-5 tonnes per skip. Guides (wooden or iron rails in shaft) prevent cage rotation. Safety brake (friction brake on drum, held off by steam pressure — loss of pressure = automatic brake application).

**Underground transport**:
- **Wheelbarrows**: 50-100 kg capacity. One man. For short distances.
- **Mine carts on rails**: Iron or wooden wheeled carts (200-500 kg capacity) on wooden or iron rails (wooden rails with iron strapping initially). Pushed by hand or pulled by pit pony. 0.5-1 m gauge. Rails enable 10x easier movement vs dragging.

### Mine Safety & Operations

**Ground control**:
- **Rock bolting**: Steel rod (2-3 m long, 20-25 mm diameter) inserted into drilled hole, anchored mechanically (expanding shell) or with cement grout. Supplements timber support in hard rock. Plate washer on exposed end distributes load.
- **Roof inspection**: Sound the roof with a bar — solid rock rings, loose rock thuds. Scale (knock down) loose rock before working. Torch inspection for cracks, water seepage, joint separation. Daily checks at working faces.
- **Cribbing**: Square timber frames stacked like a pyramid to support voids and stabilize large openings. Used at shaft stations, junctions, and wide chambers.

**Operational practices**:
- **Scaling**: After each blast, bar down loose rock from roof and walls before crew re-enters. The single most important safety practice underground.
 - **Water control**: Grade all tunnels 1-3° toward shaft for gravity drainage. Sumps at shaft bottom. Pump capacity must exceed maximum inflow rate. Monitor water levels in worked-out areas — sudden inrush is a major hazard.

### Underground Mining Methods

**Room and pillar**: Used for flat-lying, relatively uniform deposits (salt, potash, coal, limestone).
- Mine rooms 6-8 m wide, separated by pillars of unmined ore 6-8 m square. Room height matches the ore body thickness (typically 2-4 m).
- Recovery: 50-60% of the ore (the pillars remain in place to support the roof). In some operations, pillars are extracted ("retreated") on the way out, but this risks roof collapse and is only done with careful planning.
- Equipment: continuous miners (rotating drum on tracked machine) in modern operations, or drill-and-blast in bootstrap scenarios. Roof bolting required in every room for safety.
- Ventilation: air flows through the rooms in a systematic pattern (intake on one side, exhaust on the other). Large room-and-pillar mines can extend over several square kilometers.

**Shrinkage stoping**: Used for steeply dipping, narrow veins (gold, silver, copper).
- Mine the ore in horizontal slices 2-3 m thick, working upward from the bottom level. Each blast breaks ore downward, where it accumulates in the stope. The broken ore provides a working platform for the miners and supports the stope walls.
- Draw off ~40% of the broken ore after each blast (the ore expands 40-50% when broken, so the stope fills up if no ore is drawn). After the stope is fully mined, draw the remaining broken ore from draw points at the bottom.
- Recovery: 70-85%. Dilution from wall rock sloughing can be significant in wide stopes. Best suited for veins 1-3 m wide with competent wall rock.
- Access: raise (vertical or inclined passage) from the level below provides access to the stope floor. Miners work standing on the broken ore surface, drilling upward into the ore above their heads.

**Cut and fill**: Used for irregular ore bodies, steeply dipping deposits with weak walls, or where surface subsidence must be minimized.
- Mine a 2-3 m horizontal slice of ore from the stope floor. Remove the broken ore. Backfill the void with waste rock, mill tailings, or a cemented fill mixture. The fill provides a solid working floor for the next slice and supports the stope walls.
- Repeat upward, slice by slice. Each cycle: drill → blast → muck (remove ore) → fill.
- Recovery: 85-95% (very high because the fill supports the walls and allows complete ore extraction). Selective mining is possible — uneven ore body boundaries can be followed precisely.
- Cemented fill (mill tailings + Portland cement, 3-6% cement by weight) creates a strong, self-supporting mass that allows adjacent stopes to be mined without wall collapse. Uncemented fill (waste rock) is cheaper but provides less support.

**[Longwall mining](../glossary/longwall-mining.md)** (coal): The most productive underground coal method.
- A 150-250 m long coal face is mined by a shearer (rotating drum on an armored face conveyor) that cuts the coal in a single pass. Hydraulic shields (steel canopies supported by hydraulic legs) support the roof directly behind the shearer. As the shearer advances, the shields advance with it, and the roof behind the shields collapses into the void (goaf).
- Recovery: 80-90% of the coal seam, far higher than room and pillar.
- Production: 2,000-5,000 tonnes per day from a single face. Requires continuous conveyor belt transport along the face and in the gate roads.
- Subsidence: the surface above a longwall panel subsides predictably (1-2 m for a 2 m seam at moderate depth). Plan surface use accordingly.

### Surface Mining Detail

**Open pit design**:
- Bench height: 10-15 m for large operations (matches the reach of large excavators). Smaller operations use 5-10 m benches.
- Haul road gradient: <10% (6°). Loaded trucks climb slowly; steeper grades increase fuel consumption, tire wear, and cycle time dramatically. Road width: 3-4× the width of the largest haul truck for two-way traffic.
- Overall pit slope: 35-55° depending on rock strength and geologic structure. Steeper slopes reduce the amount of waste rock that must be removed but increase the risk of slope failure. Install slope monitoring (prisms surveyed by total station, or crack meters on tension cracks) for pits deeper than 100 m.
- Stripping ratio: the ratio of waste rock to ore. Economic limit varies by commodity: iron ore mines operate at 1:1 to 3:1, copper mines at 2:1 to 5:1, gold mines may tolerate 5:1 to 10:1 for high-grade ore.

### Timber Support Systems

**Square set timbering**: Used for wide, irregular stopes in weak ground. Build a framework of timber sets (posts + cap + sill) in a 1.5-2 m grid, stacking each level on the one below. Each set is a rectangular frame: two vertical posts (15-20 cm diameter, 1.5-2 m tall) capped by a horizontal cap (15-20 cm diameter). Fill the space between the timber and the rock walls with waste rock. Provides positive support for the entire stope roof. Timber-intensive — a large stope may consume thousands of cubic meters of lumber. Use only where ground conditions demand it.

**Stulls**: Horizontal timber beams wedged between the two walls of a narrow stope or drift. Used for localized wall support in narrow openings. Stull diameter: 15-25 cm depending on span. Wedge each end firmly into a hitch (notch cut into the rock wall) to prevent slippage.

**Shaft timbering**: Line shafts with timber frames at 1.5-2 m intervals. Each frame consists of two vertical posts, two horizontal caps, and sometimes sills at the base. The compartment dividers (brattice) are horizontal planks separating the winding, ventilation, and pumping compartments. For permanent shafts in stable ground, brick or stone lining replaces timber (longer lifespan, fire-resistant). In wet ground, use concrete lining with waterproofing.

### Shaft Sinking

**Hand-drill and blast method**: The bootstrap approach to sinking a shaft.
1. At the bottom of the shaft, drill 6-12 holes (25-35 mm diameter, 0.8-1.5 m deep) in a pattern (V-cut or burn cut) using a hand jumper drill (steel bar struck with a sledgehammer). Two-man team: one holds and rotates the drill, one swings the hammer.
2. Load holes with black powder and safety fuse. Stem with clay. Retract all equipment. Fire the round.
3. After the blast, wait 15-30 minutes for fumes to clear (longer in deep shafts with poor ventilation). Muck (remove) the broken rock by shoveling into a bucket, which is hoisted to surface by windlass or whim.
4. Install timber framing at the new depth. Repeat.
5. Progress: 0.5-2 m per day in hard rock, 2-5 m in soft rock, depending on crew size, shaft dimensions, and ground conditions.
6. Water: as the shaft deepens, water inflow increases. Install a chain pump or bucket bailing system at the shaft bottom. Grade the shaft bottom slightly to direct water to a sump.

**Lining**: As the shaft deepens past the weathered surface rock and into solid ground, install permanent lining. Brick lining: lay courses of firebrick or common brick with Portland cement mortar, starting from the bottom and working upward. The lining provides a smooth surface for airflow (reduces ventilation resistance) and prevents loose rock from falling into the shaft. In wet ground, install a concrete lining (150-300 mm thick) with waterproofing admixture to keep the shaft dry.

---

### Mine Planning and Development

**Exploration sampling** before mining determines ore location, grade, and extent:
- **Trench sampling**: Dig trenches across the ore body at regular intervals. Sample the exposed rock at 1-2 m intervals. Analyze each sample for metal content. This establishes the surface trace of the ore body and the lateral variation in grade.
- **Channel sampling**: Cut a narrow channel (10 cm wide, 2-3 cm deep) across the ore face with a chisel. Collect all cuttings as a single sample representing that section. Channel spacing: 2-5 m along strike.
- **Diamond drilling**: Core drilling with a diamond-tipped bit produces a cylindrical rock core (25-50 mm diameter) from depth. The core is logged (geologically described) and split for assay. Drill spacing: 50-200 m between holes for initial resource estimation. The core provides the most reliable subsurface information available.

**Development sequence** for an underground mine:
1. **Decline or shaft**: Access from surface to the ore body. A decline (inclined tunnel, 15-20% grade) allows rubber-tired equipment access. A vertical shaft is cheaper per vertical meter but requires winding equipment for all transport.
2. **Level development**: Drive horizontal tunnels (drifts) along the ore body at regular vertical intervals (40-80 m between levels). These provide access for drilling, blasting, mucking (ore removal), and ventilation.
3. **Raise development**: Drive vertical or inclined openings between levels for ventilation, ore passes (gravity chutes), and emergency escape routes. Raises are the most dangerous development heading — miners work underneath unsupported rock.
4. **Stope preparation**: Once levels and raises are established, the stope (the production opening where ore is extracted) can be prepared and production blasting begins.

### Ground Control Methods

**Rock bolting**: The primary method for stabilizing rock in modern mines. A steel bolt (2-3 m long, 20-25 mm diameter) is inserted into a drill hole and anchored:
- **Mechanical anchor**: An expanding shell at the bolt tip grips the rock when the bolt is rotated. Fast to install, but the anchor can slip in weak rock.
- **Resin-grouted**: Polyester resin cartridges are inserted into the hole before the bolt. Spinning the bolt mixes the resin, which sets in 30-60 seconds. Provides full-length anchorage along the bolt. Most common method in modern mining.
- **Cable bolting**: Steel cables (15-25 mm diameter, 4-10 m long) grouted into deep holes for reinforcing large spans (intersection support, stope hanging walls). Higher capacity than rock bolts.

**Shotcrete**: Spray concrete (wet-mix or dry-mix) onto the rock surface immediately after excavation. Provides immediate support and seals the rock from air and moisture (which weaken some rock types). Typical thickness: 50-100 mm. Often reinforced with steel fiber or welded wire mesh. Shotcrete allows mining in ground that would otherwise require heavy timber support.

**Backfill**: Fill mined-out stopes with waste material to provide wall support and allow extraction of adjacent ore:
- **Hydraulic fill**: Mill tailings mixed with water (70-80% solids) pumped into the stope. Water drains out through a filter wall, leaving a solid fill mass. Add Portland cement (3-5% by weight) to create a strong, self-supporting fill (cemented paste fill).
- **Rock fill**: Waste rock dropped into the stope from the level above. Cheaper than hydraulic fill but provides less support. Used where cemented fill is not required.

### Mine Drainage Systems

Water management is often the limiting factor in mine depth and production capacity:

**Gravity drainage**: The simplest and most energy-efficient method. Drive adits (horizontal tunnels) from the nearest valley at a slight upward grade (1-3°) to intercept the mine workings. Water flows out by gravity. Effective for hillside mines where the valley floor is below the workings. Many historical mines were drained this way — the adit serves double duty as both drain and access.

**Sump pumping**: At the lowest point of the mine (the shaft bottom), excavate a sump (collection basin, 2-3 m deep, lined with concrete or brick). Install a pump intake in the sump. The sump provides buffer capacity — if pump flow exceeds inflow, the sump fills; if inflow exceeds pumping, the sump provides warning time before flooding. Sump capacity should hold at least 2-4 hours of normal water inflow to allow time for pump maintenance without flooding.

**Pump types for mine drainage**:
- **[Piston pump](../glossary/piston-pump.md)** (Cornish pump): Cast iron cylinder with leather-packed piston, driven by a surface steam engine through flat rod linkages (rod runs down the shaft). Lift capacity: 50-200 m per stage. Multiple stages for deeper mines. Flow rate: 500-5,000 liters/minute. The Cornish pumping engine was the technology that enabled deep mining in Cornwall and elsewhere from the 18th century onward.
- **Centrifugal pump**: Electrically driven (requires electrical infrastructure). Multi-stage designs lift water 100-500+ m. Flow rates up to 10,000 liters/minute. More efficient than piston pumps but requires reliable electric power. Modern standard for mine dewatering.
- **Air-lift pump**: Inject compressed air into the bottom of a water-filled pipe. The air-water mixture is less dense than the surrounding water column, so it rises by buoyancy. Simple, no moving parts underground (compressor is at surface). Lift: 20-50 m per stage. Efficiency: 20-40%. Useful for sumps where installing a mechanical pump is impractical.

### Mine Communications

Communication between surface and underground is essential for safety and operations:

- **Bell signals**: The oldest method. A system of bell codes (bell pulls on a wire rope running down the shaft) between the banksman (surface) and the onsetter (underground shaft station). Standard signals: 1 bell = stop, 2 bells = lower, 3 bells = raise, 4 bells = men riding (slow and careful), emergency = continuous ringing. Still used as backup in modern mines.
- **Voice pipe**: A steel or brass pipe (25-50 mm diameter) running from surface to underground stations. Sound travels through the pipe with surprising clarity over 100-200 m. Requires no power. Limited to one conversation at a time and one pipe per station.
- **[Electrical telephone](../glossary/electrical-telephone.md)** (requires electrical infrastructure): Magneto telephones (hand-cranked ring generator) connected by cable. The standard method in 20th-century mines. Explosion-proof housings required in gassy mines. Cables vulnerable to damage from blasting and rock falls — run through protected conduits.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Mining](./index.md) • [All Domains](../index.md)*
