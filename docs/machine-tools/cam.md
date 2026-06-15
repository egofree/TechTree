# Computer-Aided Manufacturing (CAM)

> **Node ID**: machine-tools.cam
> **Domain**: [Machine Tools](index.md)
> **Dependencies**: [`machine-tools.edm-cnc`](edm-cnc.md),
> [`computing.electronic`](../computing/electronic.md)
> **Enables**: None
> **Timeline**: Years 30-50
> **Outputs**: cam-toolpaths
> **Critical**: No — CAM accelerates and de-risks CNC machining, but a skilled programmer can hand-write G-code for simple parts; CAM becomes essential only for complex 3D contours, high part counts, and adaptive toolpaths.

Computer-Aided Manufacturing (CAM) is the **software layer that converts a digital part design into machine-executable motion**. Where [EDM & CNC](edm-cnc.md) describes the *physical* machine — servo drives, ball screws, encoders, and the G-code *language* that commands them — CAM describes the *software pipeline* that **generates** that G-code from geometry. A CAM system takes a CAD model, applies cutting-tool geometry and machining strategy, computes a collision-free toolpath, and emits a stream of coordinate and feed commands that the CNC controller executes.

This article covers the CAD→CAM→G-code→CNC pipeline, toolpath strategy selection, post-processing, and a worked pocket-milling example. It does **not** re-cover machine hardware, G-code syntax, or servo control — those belong to [EDM & CNC](edm-cnc.md). The boundary is clean: CAM owns *toolpath generation*, edm-cnc owns *toolpath execution*.

## The CAD→CAM→G-code→CNC Pipeline

Manufacturing a part from a digital model passes through four distinct stages. Each stage has its own representation of the part and its own failure modes:

```
   ┌────────────┐     ┌────────────┐     ┌──────────────┐     ┌────────────┐
   │  CAD       │     │  CAM       │     │  POST-       │     │  CNC       │
   │  design    │────▶│  toolpath  │────▶│  PROCESSOR   │────▶│  machine   │
   │            │     │  strategy  │     │  (G-code     │     │  (execute) │
   │ geometry:  │     │ + tools +  │     │   dialect)   │     │            │
   │ solids,    │     │ feeds +    │     │              │     │  servo /   │
   │ surfaces,  │     │ speeds  →  │     │  generic →   │     │  stepper   │
   │ 2D drawings│     │ CL data    │     │  machine     │     │  axes      │
   └────────────┘     └────────────┘     │  G-code      │     └────────────┘
        │                   │            └──────────────┘           │
        │                   │                 │                     │
   .step / .iges       tool library     .nc / .tap / .g            chips
   .stl / .dxf         stock model      .ngc / .cnc            (metal removed)
   dimensions +        stepover,        M03 S10000              finished part
   tolerances          feed, DOC        G01 X.. F..
```

### Stage 1 — CAD (Design)

The part is defined as geometry in a CAD (Computer-Aided Design) system. The CAM system is agnostic to which CAD package produced the model — it consumes a neutral exchange format:

- **STEP (.step/.stp)** — ISO 10303, the preferred format. Preserves solid B-rep (boundary representation), so CAM can reliably detect faces, edges, and fillets. Nearly lossless.
- **IGES (.iges/.igs)** — older surface/wireframe format. Still common but prone to surface-trimming errors; surfaces may stitch incorrectly, leaving gaps that break toolpath generation.
- **STL (.stl)** — triangulated mesh (the same format used for 3D printing). CAM sees only triangles, not analytic surfaces, so it cannot detect a true cylinder vs. a 72-faceted approximation. Acceptable for roughing and organic shapes; avoid for precision finishing where surface finish matters.
- **DXF/DWG (.dxf/.dwg)** — 2D drawings. Used for 2D profiling, drilling, and engraving where no 3D model exists.

**Critical CAD responsibilities**: the model must fully define the finished part, including stock-to-leave allowances (extra material for finishing), and must be dimensionally correct to the tolerance the part requires. CAM cannot fix an inaccurate model — it will faithfully machine the wrong shape.

### Stage 2 — CAM (Toolpath Generation)

The CAM system reads the geometry plus a **process setup** and computes the toolpath. The process setup defines everything the toolpath needs:

1. **Stock model** — the raw block dimensions (or cast/forged preform) the machine starts from.
2. **Tool library** — each tool's diameter, flute length, corner radius (ball vs flat vs bull nose), and shank/collar geometry for collision checking.
3. **Work coordinate system (WCS)** — where part origin sits on the machine (G54-G59).
4. **Machining strategy** — the algorithm used to sweep the tool across the stock (contour, parallel, adaptive, etc. — see below).
5. **Cutting parameters** — feeds, speeds, depth of cut, stepover (see parameter table below).

The output of this stage is **CL data (Cutter Location data)** — a machine-independent list of tool tip positions and orientations: "move to X10 Y10 Z5 rapid, plunge to Z-2 at feed 50, cut to X40 at feed 200…". CL data is generic; it contains no G-codes or M-codes yet.

### Stage 3 — Post-Processor (G-code Generation)

CL data cannot run on a machine. A **post-processor** ("post") translates the generic CL data into the specific G-code dialect a given controller understands. A Fanuc, a Siemens SINUMERIK, a Haas, a LinuxCNC, and a Heidenhain all read different dialects — the same pocket requires a different `.nc` file on each.

The post handles:

- **Modal state management** — emitting G20/G21 (inch/mm), G90/G91 (abs/inc), G17/18/19 (plane) once at the top, not on every line.
- **Canned cycles** — converting "drill these 10 holes" into G81/G83 cycles, or expanding them into G00/G01 moves for controllers lacking the cycle.
- **Arc output** — G02/G03 with I/J/K (arc center offsets) vs R (radius) format. Some controllers reject R for arcs >180°.
- **Tool changes** — M06 T.. with length compensation G43 H.., or a manual tool-change stop for machines without an ATC (automatic tool changer).
- **Feed mode** — F as mm/min (G94) vs mm/rev (G95).
- **Spindle** — M03/M04, S-word in RPM (G97) vs surface speed (G96 constant surface speed, common on lathes).
- **Machine-specific safety** — coolant M08/M09, chip-breaking retracts, optional stops M01, and controller-specific line numbers.

A misconfigured post is the single most common cause of crashes: if the post emits R-format arcs to a controller that misreads them, or omits G43 tool-length compensation, the tool plunges to the wrong height.

### Stage 4 — CNC (Execution)

The machine's controller reads the G-code line by line, plans the trajectory (look-ahead buffering to blend moves without stopping), and commands the servo/stepper drives. This stage — the physical machine, drives, feedback, and the controller's interpreter — is the subject of [EDM & CNC](edm-cnc.md).

## Toolpath Strategy Selection

Choosing the right machining strategy is the core CAM skill. The wrong strategy wastes hours, breaks tools, or leaves a poor finish. Strategy depends on the geometry (2D vs 3D), the feature (pocket, profile, surface, hole), and the material.

### 2D vs 3D Toolpaths

**2D toolpaths** operate on a constant Z (or a flat plane). The tool moves in XY while Z is fixed per pass. Used for profiles, pockets, drilling, and engraving — anything cut from sheet or machined in horizontal layers. Fast to compute and execute; the bulk of job-shop work.

**3D toolpaths** drive the tool along curved surfaces where Z varies continuously with XY. Used for molds, impellers, turbine blades, and any organic or sculptured geometry. Computationally heavier; requires surface or solid model input.

### 2D Strategy Families

```
   CONTOUR / PROFILE          POCKET (offset)         DRILL (canned cycle)
   ┌───────────────┐          ┌───────────────┐       ○   ○   ○
   │               │          │ ╭───────────╮ │       │   │   │
   │   ──────▶     │          │ │ ╭───────╮ │ │       ▼   ▼   ▼
   │   (open or    │          │ │ │ ───▶  │ │ │      (G81 peck / G83
   │    closed)    │          │ │ ╰───────╯ │ │       deep-hole)
   │               │          │ ╰───────────╯ │
   └───────────────┘          └───────────────┘
   tool follows an           spiral/offset inward,
   open or closed curve      removes all material
   (edge finish, part-off)   inside a boundary
```

- **Contour / Profile** — tool follows a single open or closed curve at a given depth. Used for outside profiles, part-off, chamfers, and engraving. Often run as a **multi-pass** (roughing passes leaving stock, then a single spring/finish pass at full depth).
- **Pocket** — removes all material inside a closed boundary. Two sub-strategies:
  - **Offset (spiral-in)** — tool spirals from the boundary inward. Leaves a uniform stepover, good finish on walls, but corners can trap chips.
  - **Roughing + finishing** — a roughing pass (offset or zig-zag) removes bulk at a coarse stepover; a separate finish pass traces the wall at full depth for dimensional accuracy.
- **Face** — flattens the top of stock with overlapping parallel passes. The first operation on most parts.
- **Drill** — canned cycles (G81 drill, G83 deep-hole peck, G73 chip-breaking peck) at point locations.

### 3D Strategy Families

- **Parallel** — raster sweeps across the model in one direction (typically X), stepping over in Y by the stepover amount. Simple, predictable, but leaves scallops on steep walls and a visible "stripe" pattern. Fast to compute.
- **3D Contour / Waterline** — slices the model at constant Z and machines each contour. Excellent on steep walls; poor on shallow slopes (large stepover there).
- **Radial / Spiral** — tool spirals out from a center point. Smooth on radially-symmetric parts (lenses, domes).
- **Pencil / Corner finishing** — drives the tool only along the model's concave corners where a previous larger tool could not reach. Cleans up fillet radii.
- **Project** — projects a 2D curve (text, logo) onto a 3D surface. Used for engraving on curved parts.

### Adaptive Clearing (Trochoidal Roughing)

The most important modern roughing strategy. Instead of cutting a full-width slot (100% radial engagement, which overloads the tool and traps heat), adaptive clearing uses a **small radial engagement (5-15% of diameter)** with a **large axial depth of cut (full flute length)** and **trochoidal tool motion** — the tool circles forward in small loops, peeling a thin chip each pass:

```
   CONVENTIONAL SLOT (100% radial)        ADAPTIVE / TROCHOIDAL (10-15% radial)
   ┌──────────────────────────────┐       ┌──────────────────────────────┐
   │  ████████████████████████████│       │  ◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌     │
   │  ████████████████████████████│       │    ◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌◌       │
   │  tool fully buried:          │       │  tool peels thin chips,      │
   │  - chip packs flutes         │       │  air-cools between cuts,      │
   │  - heat builds, tool fails   │       │  - 3-5× faster material rem. │
   │  - limited to shallow DOC     │       │  - full-flute-depth DOC OK   │
   └──────────────────────────────┘       └──────────────────────────────┘
```

Adaptive clearing's payoff: **3-5× higher material removal rate** than conventional roughing in hard materials, with longer tool life, because the chip is thin and uniform (chip-thinning effect) and the tool spends part of each loop in air, shedding heat. It demands a rigid machine and a controller with fast look-ahead (the trochoidal path has thousands of tiny moves), but on a capable CNC it is the default roughing strategy for aluminum, steel, and titanium.

### Climb vs Conventional Milling

For every peripheral cut, the tool can rotate **with** or **against** the feed direction:

```
   CLIMB (down) milling              CONVENTIONAL (up) milling
   spindle CW, feed →                spindle CW, feed →

        ◐ tool                           ◐ tool
       ╱│ ╲                             ╱│ ╲
      ╱ │  ╲   chip starts MAX,        ╱ │  ╲  chip starts at ZERO,
   ─▶│  │  │◀─ tapers to exit          │  │  │  builds to MAX at exit
     ╰──┴──┴                           ╰──┴──┴
   workpiece                          workpiece
   ─────────────────                  ─────────────────
   • tooth meets work at full         • tooth rubs at entry
     chip thickness — clean cut         (zero chip), work-hardens
   • heat carried away in chip          surface, then digs in
   • pushes work INTO vise /            • lifts work / pulls backlash
     table (stable)                       into leadscrew (backlash
   • BETTER finish, LONGER tool          → chatter on non-preloaded
     life                                  machines)
   • REQUIRES backlash-free              • SAFER on old manual /
     ball screws (CNC standard)            sloppy machines
```

**Rule of thumb**: use **climb milling on CNC machines** (which have backlash-free preloaded ball screws — see [EDM & CNC](edm-cnc.md)). Use **conventional milling on manual or backlashed machines** and on hard castings/case-hardened surfaces (to avoid digging the tooth into a hard crust at full chip). CAM defaults to climb for CNC; confirm this in the strategy settings.

## Post-Processing in Depth

The post-processor is configured per **controller family + machine configuration**. Common pairings:

| Controller | Typical G-code flavor | Arc format | Notes |
|------------|----------------------|------------|-------|
| Fanuc | Modal, G94 mm/min | I/J/K preferred | Industry standard, many clones |
| Haas (Fanuc-derived) | Modal, G94 | R or I/J/K | Conversational-friendly, common in US |
| Siemens SINUMERIK | Rich cycles (@-codes, ShopMill) | I/J/K | Strong conversational layer |
| Heidenhain | Plain-text "conversational" (KL/FF) | via Q-params | Not G-code at all; post is mandatory |
| LinuxCNC / EMC2 | RS274/NGC | R or I/J/K | Open source; G-code readable |
| Mach3 | RS274 | R or I/J/K | Hobby/industrial hybrid |

A typical post-generated program header:

```
%
O0001 (POCKET_DEMO)
(CAM: machine-tools.cam  POST: fanuc-3axis-mm)
(T1 = 6MM FLAT ENDMILL  D6.0  L25.0)
G21 G90 G17 G40 G49 G80
G54 G00 X0 Y0
G43 H01 Z25. M03 S8000
M08
...
M09 M05
G00 Z50.
M30
%
```

The `%` and `O0001` (program number), the `G43 H01` (apply tool 1 length offset), and the `M03 S8000` (spindle CW, 8000 RPM) are all post decisions — none of them exist in the CL data. **Always dry-run a new post on the machine** with the tool retracted (Z+50) before cutting stock.

## Worked Example — Pocket Milling Toolpath

**Goal**: machine a 40 × 40 mm square pocket, 5 mm deep, in 6061-T6 aluminum, from a 50 × 50 × 10 mm blank. Finished wall tolerance ±0.1 mm, floor flatness 0.05 mm, surface finish 1.6 μm Ra.

**Tool**: 6 mm, 3-flute carbide flat endmill, 25 mm flute length, TiAlN coating.

### Parameter selection (from the table below)

- **Spindle speed (S)**: for 6 mm carbide in aluminum, surface speed Vc ≈ 300 m/min → S = 1000·Vc/(π·D) = 1000·300/(π·6) ≈ **15,900 RPM**. If the machine tops out at 10,000 RPM, use S = 10,000 (Vc drops to ~190 m/min — still acceptable in aluminum).
- **Feed per tooth (fz)**: 0.05 mm/tooth for a 6 mm carbide endmill in aluminum.
- **Feed rate (F)**: F = fz · z · S = 0.05 · 3 · 10,000 = **1,500 mm/min**.
- **Axial depth of cut (DOC, ap)**: for a full-slot roughing pass, ap ≤ 1×D = 6 mm. We need 5 mm total → **two Z-passes**: rough at Z-2.5 and Z-5 (DOC 2.5 mm, ~0.4×D — conservative for slotting).
- **Radial stepover (ae)**: for offset pocket roughing, 50% of D = 3 mm. For the finish wall pass, ae = 0.2 mm (spring pass).
- **Stock to leave on walls**: 0.3 mm for the finishing pass. On floor: 0.2 mm.

### Toolpath plan

```
   Z=0 (top of stock)
   ┌─────────────────────────────────────┐  50 mm stock
   │   ╭─────────────────────────────╮   │
   │   │  offset spiral, stepover 3  │   │
   │   │  mm, climb, leave 0.3 wall  │   │  40 mm pocket
   │   │  ↶  ↶  ↶  ↶  ↶  ↶  ↶  ↶    │   │
   │   │                              │   │
   │   ╰─────────────────────────────╯   │
   └─────────────────────────────────────┘

   Z-layers:  Z-2.5 (rough pass 1, DOC 2.5)
              Z-5.0 (rough pass 2, DOC 2.5)
              Z-5.0 (finish floor, full width, F down)
              Z-5.0 (finish walls, 0.2 spring pass, climb)
```

### Generated G-code (excerpt, Fanuc-mm post)

```
(CAM-GENERATED: pocket_demo  POST: fanuc-3axis-mm)
(T01 = 6MM 3FL CARBIDE ENDMILL)
G21 G90 G17 G40 G49 G80
G54 G00 X5. Y5.            (start at pocket corner + lead-in)
G43 H01 Z5. M03 S10000
M08
(--- ROUGH PASS 1: Z-2.5 ---)
G01 Z-2.5 F150             (plunge at feed, 150 mm/min)
G01 X35. F1500             (climb: CCW around the pocket)
G01 Y35.
G01 X5.
G01 Y5.
G01 X8. Y8.                (offset in by stepover)
G01 X32.
...                        (repeat spiraling inward)
(--- PLUNGE TO Z-5 ---)
G01 Z-5. F150
(--- ROUGH PASS 2 at Z-5, same XY path ---)
...
(--- FINISH WALLS: spring pass, 0.2 stock left, climb ---)
G01 X4.8 Y4.8 F1000
G01 X35.2
G01 Y35.2
G01 X4.8
G01 Y4.8
(--- RETRACT ---)
G00 Z5.
M09 M05
G00 Z50.
M30
```

### Expected result and verification

- **Material removed**: ~40 × 40 × 5 = 8,000 mm³ of aluminum.
- **Cycle time** (rough estimate): two roughing passes at ~1,500 mm/min feed over ~140 mm of travel each ≈ 0.1 min/pass + finish pass ≈ 0.1 min + rapid/positioning overhead ≈ **1-2 minutes total** for this small pocket.
- **Verification**: measure pocket width (target 40.0 ±0.1 mm), depth (5.0 ±0.05 mm), and corner radius (should equal tool radius = 3 mm — sharp internal corners are impossible with a round endmill; they need a smaller tool or EDM, see [EDM & CNC](edm-cnc.md)). Floor finish with a 0.2 mm spring pass should meet 1.6 μm Ra.

## Cutting Parameters by Material

These are starting values for **carbide tooling** on a rigid CNC with flood coolant where noted. Always verify against tool-manufacturer datasheets and the specific machine's rigidity. Values are for endmills 3-12 mm diameter.

| Material | Vc (m/min) | fz (mm/tooth) | DOC ap (×D) | Stepover ae (×D) | Coolant | Notes |
|----------|-----------|---------------|-------------|------------------|---------|-------|
| Aluminum 6061-T6 | 250-500 | 0.04-0.10 | 0.5-1.0 (slot) | 0.5-0.75 | Flood or air | Easy to machine; watch for chip welding at low speed |
| Aluminum 7075-T6 | 150-300 | 0.03-0.08 | 0.3-0.8 | 0.4-0.6 | Flood | Harder alloy; lower fz |
| Mild steel (1018) | 80-150 | 0.02-0.06 | 0.3-0.5 | 0.3-0.5 | Flood | Workable; prefer climb milling |
| Tool steel (A2/D2, annealed) | 60-100 | 0.02-0.05 | 0.2-0.4 | 0.2-0.4 | Flood | Slow; TiAlN-coated carbide |
| Tool steel (hardened 50-60 HRC) | 50-90 | 0.01-0.04 | 0.1-0.3 | 0.1-0.3 | Air mist | Hard milling; rigid machine essential |
| Stainless 304 | 50-100 | 0.02-0.05 | 0.2-0.4 | 0.2-0.4 | Flood (high pressure) | Work-hardens — never rub; keep cutting or retract |
| Stainless 17-4 PH (H900) | 50-90 | 0.015-0.04 | 0.15-0.3 | 0.15-0.3 | Flood | Tough, abrasive |
| Brass / bronze | 150-300 | 0.03-0.08 | 0.5-1.0 | 0.5-0.75 | Air or dry | Soft; reduce feed to avoid grabbing |
| Copper | 100-200 | 0.03-0.07 | 0.3-0.6 | 0.3-0.5 | Flood | Gummy; sharp edges, high positive rake |
| Titanium Ti-6Al-4V | 30-60 | 0.02-0.04 | 0.1-0.3 | 0.1-0.3 | Flood (high pressure) | Low Vc, sharp tools, rigid setup; poor thermal conductivity |
| Cast iron (gray) | 80-150 | 0.03-0.07 | 0.5-1.0 | 0.5-0.75 | Air (dry) | Abrasive dust; no flood (rusts chips) |

**Formulas** (for any diameter D in mm, flute count z, surface speed Vc in m/min):

- Spindle speed: **S (RPM) = 1000 × Vc / (π × D)**
- Feed rate: **F (mm/min) = fz × z × S**
- Metal removal rate (slotting): **MRR (mm³/min) = ap × ae × F** = ap × D × F for a full slot

Example for the 6 mm endmill in aluminum above: S = 1000×300/(π×6) ≈ 15,900 RPM; F = 0.05×3×15,900 ≈ 2,385 mm/min; MRR at 2.5 mm DOC, full 6 mm width = 2.5 × 6 × 2,385 ≈ 35,800 mm³/min — the theoretical rate the rigid-machine/adaptive regime can approach.

## Integration with CNC

CAM's output is meaningless without a machine to run it. The handoff points:

1. **Work coordinate system (WCS)** — CAM assumes part origin at a known point (e.g., top-left corner of stock). The operator must **touch off** the tool to set G54 X/Y/Z zero on the physical machine to match, else every coordinate is offset. This is the #1 source of crashes after post errors.
2. **Tool table** — CAM's tool numbers (T01, T02…) must match the machine's tool carousel, with correct length and diameter offsets (H and D registers). A mismatched H offset plunges to the wrong Z.
3. **Stock size and fixturing** — CAM assumes the stock is the declared size and is held rigidly. A vise that lets the part shift 0.1 mm ruins a ±0.05 mm tolerance.
4. **Machine limits** — the post must know the machine's rapid rate, max RPM, axis travel, and whether 4th/5th axes exist. A 3-axis post on a 5-axis machine simply ignores the rotary axes.

For the machine side — servo/stepper drives, ball screws, encoders, controllers, and G-code execution semantics — see [EDM & CNC](edm-cnc.md). For conventional (manual) machining operations that CAM often programs, see [Machining](machining.md).

## Simulation and Verification

Before running G-code on stock, verify it:

- **Backplot** — the CAM system replays its own toolpath over the stock model, showing material removal. Catches missing regions and obvious gouges, but only validates the CL data, not the posted G-code.
- **Machine simulation** — a separate tool reads the **posted G-code** and animates it against a model of the actual machine (spindle, table, clamps). Catches post errors, rapid crashes into clamps, and axis over-travel. Essential for 4/5-axis and tight-fixturing jobs.
- **Single-block dry run** — on the machine, run the program one block at a time with the tool retracted (Z+50 offset or dry-run mode) and feed override at 0-25%. Slow but definitive.

A crash at full rapid (e.g., G00 into a vise) can destroy a spindle in milliseconds. Simulate first.

## CAM in the Bootstrap Context

In a civilization-rebuilding scenario, CAM arrives after [CNC](edm-cnc.md) hardware exists and [electronic computing](../computing/electronic.md) is mature enough to run the toolpath math (CAM systems are computationally heavy — generating a 3D adaptive toolpath over a complex mold can take minutes to hours even on modern hardware). Before CAM, parts are programmed by hand-writing G-code (viable for 2D profiles and drilling) or by manual machining. CAM's value compounds with part complexity: a 2D bracket is only marginally faster via CAM, but a 3D contoured injection mold is effectively impossible without it. CAM also captures and reuses process knowledge — feeds, speeds, and proven strategies become reusable tool-library entries rather than per-part re-derivation.

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Tool gouges part surface on first run | WCS origin not touched off correctly, or H (length) offset wrong | Re-zero G54 XYZ; verify H01 matches tool 1 actual length; dry-run with Z+50 offset |
| Poor surface finish (visible scallops/stripes) on 3D surface | Stepover too large for the surface curvature and tool radius | Reduce stepover to ≤0.1 mm for finishing (ball mill) or switch to 3D-contour strategy on steep walls |
| Tool breaks in aluminum slot | Chip welding from too-low speed / poor chip evacuation | Increase Vc (faster spindle); add air blast or flood; use fewer flutes (2-flute) for aluminum; switch to adaptive (low ae) |
| Gouge or dwell mark at path transitions | CAM "retract between passes" off — tool drags across part at feed | Enable "lead in/out" arcs and "retract Z between regions" in the strategy |
| Post emits R-arc that errors on controller | Arc >180° with R-format — some controllers reject it | Configure post to use I/J/K absolute or incremental arc centers |
| Cycle time much longer than estimated | Tool spending time in air (retracts too high) or rapids disabled | Lower safe Z retract; confirm G00 (not G01) for positioning; enable high-speed mode |
| Adaptive toolpath alarms "tool over engagement" | Radial engagement set > allowed % for the tool | Lower ae% in strategy; verify stock model matches actual stock (oversize stock → deeper cut than planned) |
| Corner radius larger than drawing | Tool corner radius not set in tool library (defaults to sharp) | Set tool corner radius; for sharp internal corners use smaller tool or [EDM](edm-cnc.md) |

## Safety

- **Always simulate posted G-code before running on stock** — backplot + machine simulation catch the great majority of crashes.
- **Single-block dry-run** any new program on the machine with feed override low and tool retracted.
- **Keep the enclosure door closed** during automatic operation — CNC makes unpredictable rapid moves. Safety interlocks exist for a reason.
- **Coolant and chips** — high-pressure coolant and flying chips are hazardous. Eye protection required even through enclosure windows (which can shatter from a thrown tool fragment).
- **Tool retention** — verify tools are fully seated in the holder and the holder is locked in the spindle before M03. An unseated tool drops under centrifugal load.
- See [EDM & CNC](edm-cnc.md) for machine-side safety (servo/stepper hazards, rotating spindle, electrical).

## See Also

- [EDM, CNC & Precision Grinding](edm-cnc.md) — the machine that executes CAM toolpaths: servo drives, ball screws, encoders, G-code language and execution.
- [Machining](machining.md) — conventional turning, milling, drilling, and grinding (the operations CAM programs).
- [Bearings, Abrasives & Cutting Tools](bearings-abrasives.md) — cutting tool materials (HSS, carbide) and geometry that CAM's tool library models.
- [Electronic Computing](../computing/electronic.md) — the stored-program computers that run CAM software.
- [Computer Architecture](../computing/computer-architecture.md) — the processor/memory systems underlying CAM workstations.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Machine Tools](index.md)*
