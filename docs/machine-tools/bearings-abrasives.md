# Bearings, Abrasives & Cutting Tools

> **Node ID**: machine-tools.bearings-abrasives
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 10-25
> **Outputs**: bearings, ball_bearings, abrasives, cutting_tools, taps, dies, hss_tool_bits

### Abrasives & Grinding Media

**Natural abrasives (available immediately)**:
- **Emery**: Natural aluminum oxide (50-80% Al₂O₃) + iron oxide. Found in Greece, Turkey. Grit grades: coarse (24-60), medium (80-120), fine (150-240). For grinding and polishing.
- **Pumice**: Volcanic glass, porous. Fine polishing.
- **Sandstone**: Natural grinding wheels. Dress to shape with iron dresser.
- **Quartz sand**: Ground to powder, sieved. Lapping and grinding compound.
- **Jeweler's rouge** (iron oxide, Fe₂O₃): Fine polishing compound. Heat steel wool or iron filings in open air until red-hot. Grind resulting oxide to fine powder.
- **Tripoli**: Silica-based polishing compound. Fine finish on soft metals.

**Grit grading**: Sieve abrasive through woven wire screens. Screen mesh number = grit number (60 mesh = 60 grit, particles ~250 μm). Stack sieves coarse to fine, shake, weigh fractions.

**Synthetic abrasives (require the Energy stage electric arc furnace)**:
- **Silicon carbide (SiC)** — Acheson process: Silica sand + petroleum coke, heat in electric furnace to 2200-2500°C for 36-48 hours. SiO₂ + 3C → SiC + 2CO. Green to black crystalline mass. Crush, grade. Harder than aluminum oxide, sharp fracture.
- **Aluminum oxide (Al₂O₃)** — Bauxite fused in electric arc furnace at 2000-2200°C. Cool, crush, grade. Tougher than SiC, better for steel grinding.

**Lapping**: Mix graded abrasive (600-1200 grit, ~5-25 μm) with oil or water into slurry. Place slurry between two flat surfaces, rub in figure-8 pattern. Removes ~0.001-0.01 mm per hour. Produces optically flat surfaces. Essential for gauge blocks, valve seats, bearing surfaces.

### Thread Standards & Fastener Production

**Thread profile standard** (choose ONE system and standardize immediately):
- **Metric (ISO)**: 60° thread angle, flat crests and roots. Designated M×pitch (e.g., M8×1.25 = 8 mm major diameter, 1.25 mm pitch). Coarse pitch series is default (M8 coarse = 1.25 mm pitch).
- **Unified (UNC/UNF)**: 60° thread angle, flat crests, rounded roots. Designated by diameter + TPI (e.g., 5/16-18 UNC = 5/16" diameter, 18 threads per inch, coarse series).
- **CRITICAL**: Pick metric OR unified and commit. Mixing thread standards is a disaster for interchangeable parts. All taps, dies, gauges, and screws must match.

**Thread cutting on lathe**:
- **Setup**: Mount workpiece in chuck. Install correct change gears between spindle and leadscrew for desired pitch. Gear ratio = (pitch to cut / leadscrew pitch) × (stud gear teeth / lead gear teeth).
- **Procedure**: Engage half-nut on leadscrew. First pass at 0.1-0.2 mm depth. Disengage half-nut at end of cut, return carriage to start. Re-engage on SAME thread (use thread dial indicator). Increase depth 0.1-0.2 mm per pass. Total depth for 60° thread = 0.614 × pitch. Final pass at full depth with light cut for smooth finish.

**Tap and die production**:
- **Taps** (cut internal threads): Turn HSS rod to diameter, cut 3-4 flutes with mill, thread between flutes on lathe, harden and temper. Three-tap set: taper tap (starts easily), plug tap (general use), bottoming tap (threads to bottom of blind hole).
- **Dies** (cut external threads): Hardened steel plate with threaded hole and 3-4 cutting edges, split by adjustable slot. Die stock holds die and provides leverage.

**Bolt making**: Heat rod end, upset in heading tool to form hex/square head. Turn shank to diameter, cut threads with die. Heat treatment for high-strength bolts: harden at 820°C, quench in oil, temper at 400-500°C (~800 MPa tensile).

### Bearing Design & Production

**Plain (journal) bearings**:
- **Construction**: Cylindrical housing with removable babbitt liner. Babbitt metal: Sn-Sb-Cu alloy (88/8/4 typical) — soft, embeds dirt, conforms to shaft. Pour molten babbitt into shell around mandrel.
- **Clearance**: 0.001-0.002 × shaft diameter (50 mm shaft = 0.05-0.10 mm radial clearance). Too tight → seizure. Too loose → vibration.
- **Load capacity**: Allowable bearing pressure 2-8 MPa for babbitt on steel.

**Rolling element bearings** (precision):
- **Ball bearing**: Inner ring, outer ring (hardened 52100 steel, 1% C, 1.5% Cr), balls, cage (brass or stamped steel). Standard 6200 series (light): e.g., 6205 = 25 mm bore × 52 mm OD × 15 mm width.
- **Ball production**: Cut wire → cold head into rough spheres → grind between grooved ring plates → lap to 1-5 μm variation. Harden 820-860°C, oil quench, temper 150-200°C.
- **Ring production**: Forge from bearing steel → turn → heat treat (58-62 HRC) → grind raceways → super-finish to 0.05 μm Ra.
- **Assembly**: Press balls into cage between races, rivet cage, pack with grease.

### Lubrication & Coolants

- **Tallow and lard**: Grease plain bearings (apply by hand or oil cup). Lard oil as cutting fluid for turning and threading — reduces friction, improves finish.
- **Vegetable oil** (linseed, castor): Cutting fluid for brass and aluminum. Not ideal for steel (polymerizes and gums).
- **Water with soluble oil**: Best for heavy machining (grinding, milling). 20:1 water-to-emulsifiable-oil ratio. Cools AND lubricates.
- **Sulfurized cutting oil**: For heavy turning and gear cutting. Add flowers of sulfur (5-10%) to mineral oil or lard oil. Extreme pressure lubrication.
- See [Lubricants](../chemistry/lubricants.md) for the full production chain.

### Cutting Tool Materials

**Carbon steel tool bits** (first available, basic carbon steel):
- Composition: 0.8-1.3% carbon steel. Harden by heating to 780-820°C and quenching, temper at 200-250°C.
- Cutting speed: 5-10 m/min for steel, 15-30 m/min for cast iron and brass.
- Loses hardness above ~200°C — limited to light cuts and slow speeds.

**High-speed steel (HSS)** (later, needs alloy elements from chemistry):
- Composition: Tungsten (18%), chromium (4%), vanadium (1%), carbon (0.7-0.8%) — classic T1 grade. M2 grade: 6% W, 5% Mo, 4% Cr, 2% V.
- Hardness retained to ~600°C — 3-5x faster cutting than carbon steel.
- Manufacturing: Melt alloy in electric furnace (Energy), cast, forge, heat treat (austenitize at 1250-1300°C, quench in oil, triple temper at 540-570°C).

**Tool grinding**: Grind tool bits on abrasive wheel to correct geometry:
- **Rake angle**: Positive (5-15°) for aluminum/brass, neutral to negative for steel/heavy cuts.
- **Relief/clearance angle**: 6-12° below cutting edge.
- **Nose radius**: 0.5-2 mm for finishing, sharp for roughing.


### Safety & Hazards

- **Abrasives dust inhalation**: Grinding and polishing generates fine dust from both the abrasive and the workpiece. Silica dust from sandstone wheels causes silicosis. Aluminum oxide and silicon carbide dust are respiratory irritants. Wear respirators during dry grinding. Wet grinding preferred.
- **High-speed machinery**: Grinding wheels and machine tools rotate at high speeds (1000-3000 RPM). Loose clothing, long hair, or jewelry can be caught. Guard all rotating parts. Eye protection mandatory — grinding wheels can shatter and eject fragments at high velocity.
- **Cutting tool hazards**: Sharp cutting tools (taps, dies, tool bits) can cause severe lacerations. Handle with care. Use tool holders, not bare hands, when possible. Cut away from body.
- **Hot metal chips**: Machining metal produces hot, sharp chips. Do not handle with bare hands. Clear chips with brush, not hands or compressed air (compressed air blows chips into eyes and skin).

---

*Part of the [Bootciv Tech Tree](../) • [Machine Tools](./) • [All Domains](../)*
