# Steam Power

> **Node ID**: `energy.steam-power`
> **Domain**: [Energy](./)
> **Dependencies**: `machine-tools`, `metallurgy.iron-steel`, `metallurgy.metalworking`
> **Timeline**: Years 15-25
> **Outputs**: steam_engines, boilers, rotary_power

### Steam Engines

**Newcomen-style atmospheric engine** (first practical steam engine, ~1712):
- **Principle**: Steam at atmospheric pressure fills cylinder. Cold water injected into cylinder condenses steam → vacuum → atmospheric pressure pushes piston down → work stroke.
- **Critical component**: Cylinder, bored to close tolerance (~0.5 mm clearance over piston). Requires the Machine Tools stage (Wilkinson boring machine). Cylinder diameter 30-80 cm, stroke 1.5-3 m.
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

### Compound Engines

Single-expansion engines waste most of the steam's energy — exhaust steam still carries significant pressure. Compound engines extract work in stages:
- **Double-expansion**: High-pressure cylinder receives boiler steam, exhausts into a larger low-pressure cylinder. The larger cylinder captures remaining energy at lower pressure. ~30% efficiency gain over single-expansion.
- **Triple-expansion**: Three cylinders of increasing diameter (HP → IP → LP). The final LP cylinder may be 3-4x the diameter of the HP cylinder. Typical efficiency ~8-12%. Standard for marine engines from ~1880 onward.
- **Why it works**: Steam expands as pressure drops. Each successive cylinder has larger volume to accommodate the expanded steam while maintaining useful piston force.

### High-Pressure Engines

- **Operating pressure**: 5-15 bar (vs. 0.5-2 bar for early Watt engines). Requires better boilers, stronger cylinders, and reliable safety valves.
- **Benefits**: Smaller cylinder for same power, higher efficiency (~10-15%), lighter weight (enables locomotives and steam vehicles).
- **Challenges**: Boiler explosions are catastrophic. Requires rigorous riveting/welding, pressure testing at 1.5x operating pressure, fusible plugs, and reliable safety valves.

### Boilers

**Fire-tube boilers** (Cochran, Lancashire, Cornish):
- Hot combustion gases pass through tubes surrounded by water. Large water volume = slow response but stores energy well. Maximum pressure ~10-15 bar (shell contains pressure — larger shell = thicker plate required).
- **Lancashire boiler**: Two fire tubes through cylindrical shell. 6-9 m long, 2-2.5 m diameter. Steam production ~5000-10000 kg/hour. Thick steel shell (15-25 mm plate).
- **Locomotive boiler**: Horizontal fire-tube with firebox at one end. High steaming rate for weight. Forced draft from exhaust steam blast pipe. Pressure 10-15 bar.

**Water-tube boilers** (Babcock & Wilcox, Stirling):
- Water flows through tubes, combustion gases flow around them. Smaller water volume = faster response, higher pressure capability (20-100+ bar). Tubes are small diameter = thinner walls = safer at high pressure.
- **Advantage**: If a tube fails, only that small volume flashes to steam — not the entire boiler contents. Inherently safer than fire-tube at high pressure.
- **Use case**: Power generation (high-pressure, superheated steam for turbines).

**Boiler construction**:
- **Materials**: Wrought iron plates (6-15 mm thick), riveted joints. Later: welded steel.
- **Riveting**: Overlap plates, drill matching holes, drive red-hot iron rivets, hammer flat on both sides. Rivet spacing 3-5 diameters. Test with hydrostatic pressure at 1.5x operating pressure.
- **Safety**: Pressure relief valve (weighted lever type — adjust weight for set pressure). Water level gauge (glass sight glass). Blowdown valve (drain sediment). Fusible plug (lead core melts if water drops too low, dumps steam into firebox and extinguishes fire — last-resort safety).
- **Feed water**: Must be clean. Sediment clogs tubes. Dissolved minerals cause scale (insulates tubes, causes overheating). Blowdown daily. Water treatment (lime softening) when available.

### Steam Turbines

Steam turbines replace reciprocating engines for power generation — no pistons, no crankshaft, just continuous rotary motion from expanding steam:
- **Impulse turbine (De Laval)**: Steam expands through nozzles, high-velocity jet impinges on bucket-shaped blades. All pressure drop occurs in nozzles; blades rotate from impulse force only. Simple, single-stage, very high speed (10,000-30,000 RPM). Requires large reduction gearing for practical output speeds.
- **Reaction turbine (Parsons)**: Steam expands through both stationary guide blades (nozzles) AND rotating blades. Blades act as moving nozzles — pressure drops across both fixed and moving rows. Multiple stages extract energy gradually. Runs at lower speed (1,500-3,600 RPM) — direct drive to generator possible.
- **Impulse-reaction combination**: Modern practice uses impulse stages at the HP end (where pressure is highest, partial admission is efficient) and reaction stages in the LP stages (where steam volume is large, full admission is practical).
- **Performance**: 50-500+ MW. Efficiency 30-40% (with superheat and condenser). Far exceeds reciprocating engines for electrical generation.

### Governors & Speed Control

- **Centrifugal flyball governor** (Watt): Two rotating balls on hinged arms spin with engine output shaft. As speed increases, balls swing outward (centrifugal force), arms raise a sleeve that closes the steam throttle valve slightly. As speed decreases, balls drop, valve opens. Proportional control — simple, reliable, self-contained.
- **Hartnell governor**: Spring-loaded version with smaller physical size. Spring preload adjusts speed setting. More precise than gravity-based flyball, suitable for higher speeds.
- **Cutoff control**: Adjusting the point in the stroke where steam admission stops (cutoff) controls both speed and efficiency. Early cutoff = less steam used = more efficient but less power. Late cutoff = more power but wasteful.

### Valve Gear

Valve gear controls the timing of steam admission and exhaust to the cylinder. It determines engine efficiency, reversibility, and power output:
- **Stephenson valve gear**: Two eccentrics per cylinder (one for forward, one for reverse), linked by a removable radius rod. Simple, robust, good for locomotives. Heavy — two eccentrics per valve.
- **Walschaerts valve gear**: Single eccentric combined with a return crank. Lighter than Stephenson, externally mounted (accessible for maintenance). Standard on most locomotives worldwide.
- **Corliss valve gear**: Rotary valves (instead of slide valves) at each corner of the cylinder — separate admission and exhaust valves. Quick-opening, quick-closing action minimizes throttling losses. Allows independent cutoff adjustment for each end of the cylinder. Used on large stationary engines for maximum efficiency (~15-20% improvement over slide valve engines).

### Cross-References

- **Boiler fuel**: [coal.md](coal.md), [fuels.md](fuels.md)
- **Metalworking for boilers**: [metalworking.md](../machine-tools/forming.md)
- **Electricity generation**: [electricity.md](electricity.md)
- **Mining pumps** (original application): [extraction.md](../mining/extraction.md)

---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
