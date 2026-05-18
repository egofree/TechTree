# Metal Casting

> **Node ID**: machine-tools.casting
> **Domain**: Machine Tools Bootstrap
> **Timeline**: Years 10-15
> **Outputs**: cast_iron_parts, cast_aluminum_parts, sand_molds

### Charcoal Foundry (Scale-up from the Metallurgy stage)

The foundry is step zero. Every machine tool starts as a sand-cast iron or aluminum casting.

**Crucible furnace for aluminum**:
- **Crucible**: Steel pipe with welded bottom, or fired clay-graphite crucible. 5-15 kg capacity for startup.
- **Fuel**: Charcoal + forced air (electric blower or hand-cranked fan). Temperature needed: ~660°C (aluminum melts at 660°C, need ~750°C for fluidity).
- **Melting time**: 20-40 minutes for 5 kg charge. Skim dross (aluminum oxide skin) before pouring.
- **Aluminum sourcing**: Scrap aluminum (post-collapse salvage), or bauxite smelting (the Chemistry stage (Hall-Héroult — much harder). For bootstrap purposes, scrap or salvage is assumed available.

**Crucible furnace for cast iron** (for machine beds and heavy parts):
- **Temperature needed**: ~1200-1400°C (cast iron melts ~1150-1250°C depending on carbon content). Requires significant forced air and good insulation.
- **Charge**: Pig iron, scrap iron, or iron bloom + 2-4% carbon (coke/charcoal). Add limestone flux (CaCO₃) to form slag.
- **Crucible**: Clay-graphite (withstands higher temps). Silicon carbide crucible if available.
- **Pouring**: Preheat molds to 200-400°C. Pour steadily, keep sprue full to prevent shrinkage defects.

**Sand molding (green sand)**:
- **Sand**: Fine silica sand (60-120 mesh, 90-95% SiO₂). River sand works if clean and fine.
- **Binder**: Bentonite clay (8-12% by weight). If not available naturally, use any clay that provides bond strength.
- **Water**: 3-6% by weight. Too much = steam explosions, gas porosity. Too little = sand crumbles, won't hold shape.
- **Mixing**: Mull (knead) sand thoroughly — muller is a heavy wheel that grinds clay onto sand grains. Can be done by foot-treading for small batches. Test: squeeze sand in hand — should form a coherent cylinder that doesn't crumble, but breaks cleanly when snapped.
- **Mold boxes (flasks)**: Two-part wooden frames (cope = top, drag = bottom). Sizes: 20×20 cm to 60×60 cm for startup work.
- **Pattern making**: Carve wooden patterns ~1-2% oversize (shrinkage allowance — cast iron shrinks ~1%, aluminum ~1.3%). Add draft angles (1-3°) on vertical surfaces so pattern releases from sand. Include cores for internal passages (sand shapes held in place during pour).
- **Molding process**: Place pattern in drag, ram sand around it (firm but not rock-hard — use peen end of rammer near pattern, flat end elsewhere). Flip drag, place cope on top, ram sand. Cut sprue (pouring channel) and risers (vent/feeding channels). Separate flasks, remove pattern carefully, close mold, pour.

### Investment Casting (Lost-Wax)

For parts requiring finer detail and smoother surfaces than green sand can provide. Investment casting produces near-net-shape parts with minimal machining — critical for complex geometries like turbine blades, valve bodies, and instrument components.

**Wax pattern making**:
- **Injection dies**: Carve or machine aluminum dies. Inject molten wax (paraffin-microcrystalline blend, melts at 60-80°C) at 0.1-0.3 MPa. For simple shapes, hand-carve patterns directly from wax blocks.
- **Pattern assembly (tree construction)**: Attach individual patterns to a central wax sprue using a heated spatula. Typical tree: 5-50 patterns depending on part size. Gate connections must be ~3-6 mm thick to feed metal without freezing off.
- **Runner/gate design**: Bottom-gating minimizes turbulence. Gates should enter the thickest casting section. Total gate cross-sectional area ≥ sprue area to ensure complete fill.

**Ceramic shell building**:
1. **Prime coat**: Dip pattern tree in fine slurry (colloidal silica binder + zircon flour, 200-325 mesh). Drain excess, stucco with fine zircon sand (80-120 mesh). Dry 2-4 hours at 40-60% relative humidity.
2. **Backup coats**: 3-5 additional coats with coarser slurry (colloidal silica + molochite flour). Stucco with progressively coarser grain (30-80 mesh). Each coat dries 2-4 hours. Total shell: 6-12 mm thick (5-7 coats).
3. **Dewaxing**: Heat shell to 100-200°C in oven or autoclave. Wax melts and drains through sprue opening. Collect and reuse wax. Flash-fire alternative: heat rapidly to 800-900°C (wax burns out, produces smoke — requires ventilation).
4. **Burnout**: Heat to 800-1000°C, hold 1-2 hours. Removes all residual wax and organics, sinters ceramic shell to full strength.
5. **Pouring**: While shell is still hot (600-900°C), pour molten metal. Preheated shell prevents premature freezing and thermal shock cracking. Pour steadily, keep sprue full.
6. **Shell removal and finishing**: Once cooled, break ceramic shell with hammer or vibratory knock-off. Cut parts from tree with abrasive wheel. Grind gate stubs flush. Sandblast or machine critical surfaces as needed.

### Quality Control and Defect Analysis

Casting defects are the primary yield loss in foundry work. Identifying and correcting them is essential.

**Common defects**:
- **Gas porosity**: Round, scattered bubbles from dissolved gas (hydrogen in aluminum, nitrogen in iron) or moisture in sand/mold. Fix: degas aluminum melts with chlorine or nitrogen purge, dry molds thoroughly, control sand moisture to 3-6%.
- **Shrinkage porosity**: Irregular angular voids in thick sections where metal contracts without adequate feed metal. Fix: increase riser volume, use chills (metal inserts) to direct solidification toward risers, ensure continuous feed path.
- **Cold shuts and misruns**: Metal freezes before mold fills completely. Cold shut = visible seam where two metal streams meet without fusing. Misrun = missing sections. Fix: increase pouring temperature 20-50°C, widen gates, reduce pour distance, preheat molds.
- **Inclusions**: Sand grains, slag, or dross trapped in the casting body. Fix: skim dross before pouring, use ceramic foam filters in gating system, control sand compaction to prevent mold erosion.
- **Cracking**: Hot tears during solidification (differential shrinkage against rigid mold) or cold cracks from residual stress after cooling. Fix: increase fillet radii at corners, design uniform wall thickness, improve mold collapsibility.

**Inspection methods**: Visual check every casting for surface defects and short pours. Dimensional verification against pattern with calipers and gauges. X-ray radiography for critical castings (machine tool beds, pressure-containing parts) — requires [Electricity](../energy/electricity.md) infrastructure.

### Safety

Foundry work involves the highest temperatures in the machine shop. Safety discipline is non-negotiable.

- **Molten metal hazards**: Cast iron at 1300-1400°C and steel at 1500-1600°C cause catastrophic burns on contact. Steel flows like water and adheres to skin. Aluminum at 700-750°C is less dramatic but equally dangerous — it can wet and stick to clothing.
- **Protective equipment**: Full face shield (not just safety glasses), leather foundry apron, heat-resistant gloves, steel-toed foundry boots with metatarsal guards, long sleeves with no exposed skin. Preheat and inspect all tools (ladles, skimmers, tongs) that will contact molten metal — cold tools cause splatter.
- **Ventilation**: Metal fumes (zinc oxide from brass, manganese from steel, aluminum oxide) cause metal fume fever and long-term respiratory damage. Charcoal furnaces produce carbon monoxide. Work outdoors or with forced ventilation. P100 respirator for enclosed foundries.
- **Moisture explosions**: The most lethal foundry hazard. Any moisture — damp sand, wet molds, condensation on tools, concrete floor — in contact with molten metal produces a steam explosion that launches metal in all directions. Preheat molds to 200-400°C before pouring. Preheat ladles and crucibles. NEVER pour on concrete — use dry sand bed or metal drip tray.

### Cross-References

- [Iron & Steel](../metals/iron-steel.md) — bloom smelting, crucible steel, heat treatment of cast parts
- [Forming](./forming.md) — forging, rolling, and wire drawing of cast ingots
- [Iterative Bootstrap](./iterative-bootstrap.md) — building machine tools from castings

---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*

