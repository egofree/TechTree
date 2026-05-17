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

**Boiler construction**:
- **Materials**: Wrought iron plates (6-15 mm thick), riveted joints. Later: welded steel.
- **Riveting**: Overlap plates, drill matching holes, drive red-hot iron rivets, hammer flat on both sides. Rivet spacing 3-5 diameters. Test with hydrostatic pressure at 1.5x operating pressure.
- **Safety**: Pressure relief valve (weighted lever type — adjust weight for set pressure). Water level gauge (glass sight glass). Blowdown valve (drain sediment). Fusible plug (lead core melts if water drops too low, dumps steam into firebox and extinguishes fire — last-resort safety).
- **Feed water**: Must be clean. Sediment clogs tubes. Dissolved minerals cause scale (insulates tubes, causes overheating). Blowdown daily. Water treatment (lime softening) when available.
---

*Part of the [Bootciv Tech Tree](../) • [All Domains](../)*
