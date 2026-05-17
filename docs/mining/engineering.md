# Mining Engineering & Extractive Metallurgy

> **Node ID**: `mining`
> **Domain**: [Mining Engineering & Extractive Metallurgy](./)
> **Dependencies**: `foundations`
> **Enables**: `chemistry.acids`, `chemistry.alkalis`, `chemistry.cement`, `energy.coal-coke`, `metallurgy`, `metallurgy.glass-lime`, `silicon.mg-si-production`, `transport`
> **Timeline**: Years 0-50+
> **Outputs**: copper_ore, iron_ore, tin_ore, coal, quartz, sulfur, fluorite, concentrated_ore

## Problem

The tech tree needs copper, iron, tin, coal, sulfur, fluorite, and quartz in industrial quantities. Surface deposits exhaust fast. Going deeper demands engineered mines with ventilation, drainage, hoisting, and structural support. Mining engineering is not optional. It is the gateway to every material the civilization needs.

## Technologies & Systems

### Mining Methods

**Surface mining (open pit)**:
- **Planning**: Strip overburden (soil + useless rock) to expose ore body. Bench height 5-15 m. Bench width = height × slope angle (typically 45-70°). Road access on each bench for haulage.
- **Overburden removal**: Hand shovels and wheelbarrows (Foundations), animal-drawn scrapers (Metallurgy), steam or diesel shovels (Energy+). Ratio: overburden-to-ore should be <3:1 for economic viability.
- **Ore extraction**: Break rock with wedges, fire-setting, or explosives (black powder from the Chemistry stage: KNO₃ + S + C at 75:10:15 ratio). Load into carts by hand. Haul to processing area.
- **Reclamation**: Backfill exhausted pits with overburden. Re-contour and re-vegetate to prevent erosion.

**Placer mining (stream deposits)**:
- **Panning**: Fill shallow pan with gravel, agitate underwater. Heavy minerals settle to bottom. Gold, cassiterite (tin), magnetite (iron) concentrate. One pan processes ~10 kg gravel in 5-10 minutes.
- **Sluice box**: Wooden trough 2-5 m long, 30-50 cm wide, with riffles (cross-bars) on bottom. Gravel shoveled in at head, water carries material through. Heavy particles trap behind riffles. Clean riffles periodically. 50-100x faster than panning.
- **Hydraulic mining** (Energy+): Direct high-pressure water jet at hillside to wash gold-bearing gravel through sluice. Requires significant water supply and pressure (20-50 m head).

**Shaft mining** (underground):
- **Shaft sinking**: Dig vertical shaft, typically 2-3 m × 1.5-2 m (enough for one-way traffic + bucket winding). Line walls with timber (oak or pine, 15-25 cm diameter) or stone/brick for permanent shafts. Shaft compartments: one for winding (ore/people), one for ventilation, one for pumping.
- **Timber framing**: Posts (vertical, 15-25 cm), caps (horizontal across top), and sill pieces (across bottom). Frame every 1.5-2 m along shaft. Secure with wooden wedges. Fill space between timber and rock wall with waste rock (gob) for support.
- **Levels (adits)**: Horizontal tunnels driven from shaft at ore-bearing depths. Typical dimensions 1.5-2 m wide × 2-2.5 m high. Timber-supported with sets (posts + cap + sill). Grade slight upward incline (1-3°) toward shaft for water drainage.
- **Stoping** (ore extraction): Extract ore between levels. Overhand stoping: work upward from level. Underhand: work downward. Shrinkage: leave broken ore in stope as working platform. Cut-and-fill: backfill with waste as you go (better ground control).

**Drift/adit mining** (horizontal entry from hillside):
- Drive horizontal tunnel into hillside at or slightly above valley floor level. Gravity drainage — no pumping needed. Most economical method for hillslope deposits. Minimum 1.5 m wide × 2 m tall. Timber supports every 1-2 m in unstable ground.

### Rock Breaking Techniques

**Hand tools**:
- **Chisel and hammer**: Steel chisel (2-5 cm wide), 2-4 kg hammer. Strike chisel to create groove or hole. Slow but precise. For soft rock (limestone, shale): 0.5-2 m³/shift. Hard rock (granite, quartz): 0.1-0.5 m³/shift.
- **Wedge and feather**: Drill hole (2-3 cm diameter, 10-20 cm deep) with hand drill (steel bar, struck with hammer). Insert two feathers (thin curved shims) and one wedge between them. Strike wedge → splits rock along line of holes. Space holes 15-30 cm apart for controlled break.

**Fire-setting** (ancient technique for hard rock):
- Build hot fire against rock face. Burn 2-4 hours. Rock face reaches 400-600°C. Dash with cold water (or let air cool). Thermal shock cracks rock 5-15 cm deep. Break weakened rock with picks and wedges. Very effective on granite, quartz, hard ores. Consumes enormous wood/charcoal — use sparingly.

**Black powder blasting** (Chemistry+):
- **Composition**: 75% KNO₃ (potassium nitrate), 15% charcoal, 10% sulfur. Grind each component separately (NEVER together), mix by tumbling in cloth bag. KNO₃ from cave deposits, saltpeter beds (nitrate-rich soil + urine/manure + lime, leach and crystallize), or guano.
- **Black powder manufacture**:
  1. Pulverize each ingredient separately to fine powder (~100 mesh).
  2. Mix thoroughly: layer ingredients on cloth, roll/tumble for 30+ minutes.
  3. Moisten slightly with water, press into cakes (corning mill or screw press).
  4. Dry cakes, crush and sieve to desired grain size (coarse = slower burn, more lifting power; fine = faster burn, more shattering).
- **Blasting procedure**: Drill hole (2.5-4 cm diameter, 0.5-2 m deep) with jumper drill (steel bar, 1-3 m long, struck with 4-8 kg hammer). Clean hole with scraper. Fill bottom 1/3 with powder. Insert safety fuse (black powder core in tarred cotton sheath) — cut to length for 30-60 second delay. Tamp remaining hole with clay or damp sand (NOT dry sand — sparks from tamping rod ignite powder). Light fuse, retreat. 1-2 kg powder breaks 2-10 m³ rock depending on placement.
- **Safety**: NO smoking, open flames, or spark-producing tools near powder. Store in dry, cool location away from mine. Use non-sparking tools (copper or bronze) for loading. Multiple shots wired to single fuse for simultaneous blast.

### Ventilation

**Natural ventilation** (single shaft):
- Single shaft with partition (brattice — wooden or canvas wall dividing shaft into upcast and downcast). Warm air (heated by mine lights and geothermal) rises in one side, cool air descends in other. Limited to ~100 m depth. Seasonal — reverses in winter.

**Dual-shaft ventilation**:
- Separate intake shaft (downcast) and exhaust shaft (upcast). Connect at depth by levels. Intake positioned upwind. Exhaust may be heated by furnace at shaft bottom (warm air rises faster → stronger draft). Effective to ~200-300 m depth.

**Mechanical ventilation**:
- **Bellows**: Large forge bellows at shaft entrance force air underground. Intermittent flow, limited volume.
- **Fan ventilation** (Machine Tools+): Centrifugal fan (wooden or iron blades in scroll housing), driven by water wheel or steam engine. 5-50 m³/second airflow. Adjustable louvers control flow. Much more reliable than natural ventilation.
- **Air requirements**: Minimum 0.05 m³/second per underground worker. More if blasting (fumes clearance). Replace total mine air volume every 10-30 minutes.

**Gas detection**:
- **Fire damp (methane, CH₄)**: Flammable at 5-15% concentration. Detected by safety lamp (Davy lamp — flame enclosed in fine wire gauze that cools flame below ignition temperature. If methane present, blue halo appears above flame. If air is unsafe, flame extinguishes). Test at floor level (methane lighter than air, accumulates at roof).
- **Choke damp (CO₂)**: Heavier than air, accumulates at floor. Detected by candle flame (extinguishes at ~8% CO₂ — leave immediately). Or bring small animal (bird in cage — more sensitive to bad air).
- **After-damp (CO)**: After explosion or fire. Invisible, odorless, lethal. Detected by chemical indicator or canary (collapses before humans affected). Evacuate immediately if suspected.
- **Hydrogen sulfide (H₂S)**: Rotten egg smell at low concentration, but paralyzes olfactory nerve at higher concentrations so smell disappears. Lethal at 300+ ppm. Chemical detector or lead acetate paper (turns black in H₂S).

### Water Pumping (critical escalation path)

**Manual methods**:
- **Bailing**: Bucket on windlass (hand-cranked drum). One man lifts ~20 liters per bucket, 10-20 buckets/hour. Emergency only.
- **Chain pump**: Endless chain with attached buckets or disks, running in wooden trough. Lifts water 5-15 m. Powered by hand crank or water wheel. 500-2000 liters/hour.

**Powered drainage**:
- **Buddle/water wheel pump**: Water wheel operates crank → piston pump (cast iron cylinder, leather piston seal). Lift height 15-30 m per stage. Multiple stages for deeper mines. 5,000-20,000 liters/hour per pump.
- **Savery engine** (~1698, first practical steam-powered pump): Boil water → fill chamber with steam → condense with cold water injection → vacuum → atmospheric pressure forces water up suction pipe. Lift: ~6-9 m suction + ~10-15 m pressure head. Efficiency ~0.5%. Simpler than Newcomen but limited lift and very wasteful.
- **Newcomen engine** (~1712, atmospheric engine): Steam in cylinder → condense → vacuum pulls piston down → pump rod lifted on other end of beam. Lift: 30-50+ m (pump at bottom of shaft, engine at surface). Power: 5-15 HP. THE KEY FEEDBACK LOOP — mine drainage drove steam engine development, which enabled all of the Energy stage.

### Hoisting & Transport

**Windlass**: Horizontal drum, hand-cranked. Rope wound on drum. Simple, limited to ~30 m depth, ~100 kg load. One-man operation.

**Whim (horse whim)**: Vertical drum (6-10 m diameter) turned by horse walking in circle. Rope winds on drum, lifts bucket from shaft. Depth 50-100 m. Load 200-500 kg. One horse provides ~3-4 HP.

**Steam winding engine** (Energy+): Horizontal steam engine drives winding drum. Speed 5-15 m/second. Depth 200-500+ m. Load 1-5 tonnes per skip. Guides (wooden or iron rails in shaft) prevent cage rotation. Safety brake (friction brake on drum, held off by steam pressure — loss of pressure = automatic brake application).

**Underground transport**:
- **Wheelbarrows**: 50-100 kg capacity. One man. For short distances.
- **Mine carts on rails**: Iron or wooden wheeled carts (200-500 kg capacity) on wooden or iron rails (wooden rails with iron strapping initially). Pushed by hand or pulled by pit pony. 0.5-1 m gauge. Rails enable 10x easier movement vs dragging.

### Ore Dressing (processing raw rock to concentrated ore)

**Crushing**:
- **Hand crushing**: Strike ore with hammer on stone anvil. Slow but effective for small quantities.
- **Stamp mill** (the Metallurgy-Machine Tools stage transition): Vertical iron-shod wooden stamps (50-200 kg each) lifted by cam on rotating shaft, dropped by gravity. 6-12 stamps in battery. Crush ore to 1-5 mm. Water flows through battery, carries fines away. Powered by water wheel. Capacity: 1-5 tonnes/day.
- **Jaw crusher** (Machine Tools): Two jaw plates (cast iron or manganese steel), one fixed, one oscillating. Ore fed in top, crushed between jaws. Gap adjustable for output size (10-50 mm). Powered by water wheel or steam engine. 5-50 tonnes/day.

**Gravity separation**:
- **Hand sorting**: Pick out visible ore pieces from waste rock on picking belt or table. Labor-intensive but effective for coarse ore.
- **Sluicing**: Wash crushed ore through inclined trough with riffles. Heavy ore minerals settle behind riffles, light gangue washes away. For heavy minerals (gold, cassiterite, wolframite).
- **Buddling**: Circular pit with central rotating arm. Crushed ore mixed with water flows inward. Heavy particles settle near center, light particles at periphery. Continuous process.
- **Panning**: Final concentration. Same technique as placer mining.

**Magnetic separation** (Energy+): Magnetite (Fe₃O₄) is naturally magnetic. Pass crushed ore past electromagnet or permanent magnet — magnetic particles deflect, non-magnetic waste continues straight. Effective for iron ore beneficiation.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Foundations | Surface mining, basic prospecting, charcoal for smelting, hand tools |
| Metallurgy | Shaft mining, timber shoring, hand-powered drainage, fire-setting |
| Machine Tools | Machine-driven pumps, precision shafts, iron rails, jaw crushers |
| Energy | **Newcomen engine for mine drainage** — mines DRIVE steam development |
| Chemistry | Chemical ore processing, flotation, acid leaching, black powder blasting |
| Vacuum & Optics | Ventilation fans, vacuum-assisted processes |
| Silicon | High-purity quartz mining, silicon-grade feedstock |

## Key Deliverables

- Prospected ore bodies with assay data (map of what's where, how rich)
- Engineered mine shafts with timber shoring, ventilation, and drainage
- Water pumping progression from manual → water wheel → steam-powered
- Ore dressing workflow: raw rock → crushing → washing → gravity separation → concentrated ore
- Black powder blasting capability (Chemistry)
- The Newcomen engine, born from mine drainage need, enabling all of the Energy stage

## Safety Concerns

- **Roof falls**: Timber every 1.5-2 m. Sound rock with hammer — hollow ring = loose. Test with bar before working under unsupported roof. Never work alone underground.
- **Gas**: Test with safety lamp before entering any heading, especially after blasting. If lamp goes out — evacuate, ventilate, re-test.
- **Flooding**: Maintain pumps at all times. Backup pump ready. Know escape routes to higher levels.
- **Explosives**: Store separately from mine. No smoking near powder. Use safety fuse (not direct ignition). Clear blast area. Wait for dust to settle before returning. Check for misfires (unexploded holes — extremely dangerous).
- **Hoisting**: Inspect rope daily. Never ride with ore. Safety catches on cages. Test brakes each shift.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
