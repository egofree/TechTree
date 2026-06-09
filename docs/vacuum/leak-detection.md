# Vacuum Leak Detection & Seal Integrity

> **Node ID**: vacuum.leak-detection
> **Domain**: [Vacuum Technology](./index.md)
> **Dependencies**: [`vacuum.measurement`](./measurement.md), [`measurement`](../measurement/index.md), [`gas-handling`](../gas-handling/index.md)
> **Enables**: Semiconductor process tools, UHV systems, hermetic packaging
> **Critical**: No — leak detection improves vacuum system reliability but systems can operate at degraded performance without formal leak testing
> **Timeline**: Years 25-40
> **Outputs**: leak_detection_services, hermetic_seals, leak_rate_quantification

## Overview

Leak detection is the discipline of finding, quantifying, and eliminating pathways through which gas enters a vacuum system. While [vacuum measurement](./measurement.md) quantifies pressure, leak detection answers the question "where is the gas coming from?" — a distinct capability essential for building and maintaining any vacuum system that must hold pressure below ~10⁻⁶ Torr.

Every vacuum system leaks. The question is whether the leak rate is small enough for the application. A semiconductor sputtering system needs leak rates below 10⁻⁸ atm·cc/s to prevent film contamination. A UHV surface science chamber needs below 10⁻¹⁰ atm·cc/s. Leak detection provides the methods to verify these limits and locate leaks when they exceed acceptable thresholds.

## Helium Mass Spectrometer Leak Detection

### Operating Principle

The helium leak detector is a dedicated magnetic-sector or quadrupole mass spectrometer tuned exclusively to mass 4 (He). It connects to the vacuum system and continuously monitors the helium partial pressure. Because helium is present in air at only ~5 ppm, any significant increase in He signal indicates gas entering from outside through a leak.

**Why helium?**
- Small atomic radius (0.31 nm) — penetrates the smallest leaks that other gases cannot pass through
- Chemically inert — no reaction with surfaces or process materials
- Low mass — fast diffusion through leaks, rapid response time
- Low atmospheric background — 5 ppm means excellent signal-to-noise ratio
- Non-toxic, non-condensable, readily available

### Vacuum Mode (Spray Probe) — Primary Method

1. Connect the leak detector to the vacuum system at a port near the suspected leak region, or on the roughing line via a branching tee.
2. The system is under vacuum, pumped by the leak detector's internal turbomolecular pump (typically 30-60 L/s).
3. Spray a fine jet of helium from a regulated cylinder with a fine nozzle, systematically working around all joints, welds, flanges, O-rings, and feedthroughs.
4. When the helium spray passes over a leak, He enters the vacuum system through the hole and reaches the mass spectrometer within seconds. Response time depends on internal volume and pumping speed: small chambers respond in <1 second; large systems may take 10-30 seconds.
5. Mark the leak location. Continue searching — systems often have multiple leaks.
6. After repair, re-test to verify the fix and check for new leaks introduced during repair.

**Sensitivity**: Down to 10⁻¹² atm·cc/s (a leak so small it would take ~30 years to pass 1 cc of gas at STP).

### Sniffer Mode (Pressurized System)

For large systems that cannot be evacuated, or for testing welded vessels before vacuum service:

1. Pressurize the system internally with helium (or He/N₂ mixture) to 1-2 bar above atmospheric.
2. Use a sniffer probe connected to the leak detector to scan exterior surfaces.
3. Helium escaping through leaks is drawn into the probe and detected.
4. **Sensitivity**: ~10⁻⁷ atm·cc/s — much less sensitive than vacuum mode, but useful when evacuation is impractical.

### Best Practices

- **Spray from top down**: Helium is lighter than air and rises. Starting at the top prevents rising helium from a lower spray from triggering a false positive at a higher location.
- **Bag technique**: When testing a specific joint or flange, enclose it in a plastic bag, inject helium into the bag, and wait. This technique catches very small leaks that a transient spray might miss because the helium has time to permeate through the leak pathway.
- **Manage background helium**: After extensive leak testing, the room's ambient He concentration rises above 5 ppm, increasing detector background noise. Ventilate the room between sessions. Allow 15-30 minutes for background to drop.
- **Calibrated leak standards**: Every helium leak detector should be verified daily with a calibrated leak — a small artifact containing a known leak rate (typically a permeation leak through a thin glass or quartz membrane). This verifies the instrument's sensitivity and response time. Calibrated leaks are traceable to national standards (NIST).

## Pressure Rise Testing

The simplest and most accessible leak test requires no specialized equipment beyond a vacuum gauge:

1. Pump the system to its base pressure.
2. Isolate the system from all pumps — close all valves between the chamber and the pumps.
3. Monitor pressure rise over time using a [vacuum measurement](./measurement.md) gauge (CDG or Pirani).
4. Plot pressure vs. time on a linear scale. The curve has two components:
   - **Outgassing**: Initially rapid, follows ~1/t decay. Dominates at short times (<1 hour). This is gas desorbing from internal surfaces, not a leak.
   - **Real leak**: Constant pressure rise rate (linear with time). Dominates at long times (>1 hour) after outgassing has decreased to a small fraction of the leak rate.
5. The steady-state leak rate is: **Q_leak = V × (dP/dt)**, where V is system volume and dP/dt is the linear slope of the pressure rise.

**Acceptable leak rates by application**:

| System Type | Maximum Acceptable Leak Rate |
|---|---|
| Rough vacuum (760 – 10⁻³ Torr) | <10⁻³ Pa·L/s |
| High vacuum (10⁻³ – 10⁻⁷ Torr) | <10⁻⁶ Pa·L/s |
| UHV (below 10⁻⁷ Torr) | <10⁻⁹ Pa·L/s |

**Interpreting the curve**:
- If the pressure rise is entirely concave (decreasing slope), the system has outgassing but no significant leak — it needs cleaning and/or baking.
- If the pressure rise becomes linear after 1-2 hours, there is a real leak.
- If the pressure rises rapidly and linearly from the start, the leak is large — start with bubble testing or visual inspection.

## Residual Gas Analysis (RGA) for Leak Diagnosis

The RGA (see [vacuum measurement](./measurement.md) for detailed RGA specifications) is indispensable for distinguishing leaks from outgassing:

| RGA Signature | Diagnosis | Action |
|---|---|---|
| Mass 28 (N₂) + 32 (O₂) in ~4:1 ratio | Real air leak | Helium leak detection to locate |
| Mass 18 (H₂O) dominant | Water outgassing | Bake the chamber |
| Mass 4 (He) increasing during spray | Confirmed leak at spray location | Mark and repair |
| Masses 28 + 32 present, no He response to spray | Virtual leak (trapped internal volume) | Find and vent the trapped volume |
| Mass 2 (H₂) dominant in baked UHV | Stainless steel outgassing | Extended bake at higher temperature |

**Leak hunting with RGA**: Use the RGA to monitor mass 4 while spraying helium externally — same principle as a dedicated leak detector but using existing instrumentation. Sensitivity is lower (~10⁻¹⁰ atm·cc/s with electron multiplier) than a dedicated helium leak detector, but adequate for many applications.

## Bubble Testing (Gross Leaks)

The simplest leak detection method, requiring only pressurized gas and soap solution:

1. Pressurize the system to 1-2 bar above atmospheric with dry N₂.
2. Apply commercial leak detection fluid (Snoop) or dilute dish soap solution to all joints, welds, and fittings.
3. Watch for bubble formation. Each bubble indicates gas escaping through a leak.
4. **Sensitivity**: ~10⁻⁴ atm·cc/s — orders of magnitude less sensitive than helium detection, but useful for:
   - Initial screening before helium testing
   - Systems that cannot be evacuated
   - Finding large leaks that would overwhelm a sensitive helium detector

## Ultrasonic Leak Detection

Pressurize the system and scan with an ultrasonic detector (headphones + directional microphone tuned to ~40 kHz). Gas flowing through a leak creates ultrasonic turbulence. Sensitivity: ~10⁻³ atm·cc/s. Useful for preliminary screening of large systems before helium testing, especially in noisy industrial environments where the directional microphone helps isolate the leak sound.

## Vacuum Brazing and Welding for Seal Integrity

Achieving hermetic seals requires joining techniques that produce leak-tight joints:

### Vacuum Brazing

- **Process**: A brazing filler metal (typically copper, gold-copper, or nickel-based alloys) is placed between the joint surfaces. The assembly is heated in a vacuum furnace to a temperature above the filler's melting point (copper: 1083°C, gold: 1064°C). The molten filler wets the base metal surfaces and flows into the joint by capillary action. On cooling, the filler solidifies, creating a hermetic seal.
- **Vacuum atmosphere prevents oxidation** of both base metal and filler, producing clean, strong joints without flux residue.
- **Applications**: Ceramic-to-metal seals (for electrical feedthroughs), stainless steel vacuum chamber assemblies, copper heat exchanger joints.
- **Requirements**: Vacuum furnace capable of 10⁻⁵ Torr or better at brazing temperature. See [vacuum pumps](./pumps.md) and [vacuum measurement](./measurement.md).

### TIG (GTAW) Welding for Vacuum Chambers

- **Tungsten inert gas welding** is the standard joining method for stainless steel vacuum chambers.
- **Full-penetration welds** are required — any unfused root is a virtual leak (trapped volume that slowly outgasses into the chamber).
- **Interior weld surfaces** must be smooth and continuous. Rough weld beads trap contaminants and create outgassing sites. If the weld is on the vacuum side, it must be ground smooth and passivated.
- **Weld sequence**: For complex chamber assemblies, weld in a sequence that minimizes distortion. Use tack welds to hold the assembly, then complete the welds in alternating positions to balance heat input.
- **Material**: 304L or 316L stainless steel (low carbon content prevents sensitization and intergranular corrosion at weld heat-affected zones).

### Electron Beam Welding

- Performed in vacuum (~10⁻⁴ Torr) — inherently produces clean, contamination-free welds.
- Narrow, deep penetration with minimal heat-affected zone — ideal for precision vacuum components.
- Requires electron beam welding machine (see [machine tools](../machine-tools/index.md)).

### Seal Design Principles

1. **Minimize the total length of seals**: Every seal is a potential leak. Use welded construction wherever possible; reserve demountable seals (O-rings, CF flanges) for ports that must be opened regularly.
2. **All-metal seals for UHV**: CF (ConFlat) flanges with copper gaskets achieve leak rates below 10⁻¹² atm·cc/s. Viton O-rings (KF flanges) are adequate for high vacuum (10⁻⁶ atm·cc/s) but permeate helium and water vapor, making them unsuitable for UHV.
3. **Avoid trapped volumes**: Design joints so there are no internal crevices or unfused regions that could trap gas. Trapped volumes create "virtual leaks" — they slowly release gas into the chamber but cannot be found by helium leak detection because the gas is already inside.
4. **Validate every seal**: After assembly, perform a pressure rise test followed by helium leak detection. Document the measured leak rate for each chamber.

## Leak Rate Specifications for Common Applications

| Application | Required Leak Rate (atm·cc/s) | Test Method |
|---|---|---|
| Industrial vacuum furnace | <10⁻⁵ | Pressure rise, bubble test |
| Sputtering system | <10⁻⁸ | Helium leak detector (vacuum mode) |
| Electron beam lithography | <10⁻⁹ | Helium leak detector (vacuum mode) |
| Surface science UHV chamber | <10⁻¹⁰ | Helium leak detector + RGA monitoring |
| Hermetic IC package | <10⁻⁸ | Helium bombing + accumulation |
| Cryogenic vessel | <10⁻⁷ | Helium sniffer mode |

## Leak Detection Pump Specifications

Helium mass spectrometer leak detectors contain an integrated vacuum pumping system. Understanding the pump specs helps predict response time and sensitivity for different system volumes.

| Pump Parameter | Typical Value | Impact on Leak Detection |
|---|---|---|
| Internal turbo pump speed | 30-60 L/s (small units), 200-300 L/s (large units) | Higher speed = faster helium transport to detector = shorter response time |
| Roughing pump speed | 1-5 m³/h (internal rotary vane) | Determines initial pump-down time before testing begins |
| Ultimate pressure (internal) | <10⁻⁷ mbar (<10⁻⁷ Torr) | Lower base pressure = lower helium background = better sensitivity |
| Minimum detectable leak rate (vacuum mode) | 10⁻¹² atm·cc/s | Sets the floor for the smallest leak you can find |
| Minimum detectable leak rate (sniffer mode) | 10⁻⁷ atm·cc/s | Orders of magnitude less sensitive due to atmospheric helium background |
| Response time (1 L volume) | <1 second | Small volumes respond almost instantly |
| Response time (100 L volume) | 5-30 seconds | Large chambers need patience between spray and signal |
| Response time (1000+ L volume) | 30-180 seconds | Very large systems may need minutes; use bag technique for patience |

**Converting between common vacuum units**:

| Measurement | mbar | Torr (mm Hg) | Pa | atm |
|---|---|---|---|---|
| Atmospheric pressure | 1013 | 760 | 101,325 | 1 |
| Rough vacuum | 1 - 10⁻³ | 0.75 - 7.5×10⁻⁴ | 100 - 0.1 | 10⁻³ - 10⁻⁶ |
| High vacuum | 10⁻³ - 10⁻⁷ | 7.5×10⁻⁴ - 7.5×10⁻⁸ | 0.1 - 10⁻⁵ | 10⁻⁶ - 10⁻¹⁰ |
| Ultra-high vacuum | <10⁻⁷ | <7.5×10⁻⁸ | <10⁻⁵ | <10⁻¹⁰ |

Leak rates are commonly expressed in atm·cc/s (the volume of gas at standard atmosphere passing through the leak per second). Alternative units: mbar·L/s (multiply atm·cc/s by 1.013 to convert) or Pa·m³/s (multiply atm·cc/s by 0.1013).

## Common Leak Locations and Diagnostic Approach

**Where leaks occur** (ranked by frequency):

1. **Flange connections** — scratched O-ring sealing surfaces, misaligned flanges, uneven bolt tightening, degraded O-rings. Start here.
2. **Welded joints** — porosity, incomplete penetration, cracks from thermal cycling or corrosion. Check all welds, especially repair welds.
3. **Valve stem seals** — worn packing glands allow gas to enter along the valve stem shaft. Test with the valve in both open and closed positions.
4. **Viewports** — glass-to-metal seal failures from thermal shock or mechanical stress. Tap the viewport gently with a non-metallic tool while monitoring for pressure changes.
5. **Electrical feedthroughs** — ceramic-to-metal seal cracks from thermal cycling. These are subtle and often require the bag technique to isolate.
6. **Flexible hose connections** — cracked or hardened O-rings, loose clamps, hose pinholes. Flex the hose gently during helium spray.

**Systematic leak checking procedure**:

1. Start with a pressure rise test to confirm whether a real leak exists (vs. outgassing).
2. If a leak is confirmed, use RGA to identify the gas composition (air leak vs. specific contaminant).
3. Divide large systems into sections using gate valves. Isolate each section and pressure-rise test independently. This narrows the search area before helium spraying.
4. Spray helium from top to bottom, working around each joint, weld, and fitting with a fine nozzle held 3-5 mm from the surface.
5. Move the spray slowly (2-5 cm/s) and pause at each joint for at least 2× the expected response time.
6. Mark each checked location with a wax pencil. This prevents re-checking the same spot and ensures complete coverage.
7. When a leak is found, mark it and continue searching. Systems often have multiple leaks, and fixing one may reveal others that were previously masked.
8. After repair, re-test the entire system. Repair work (welding, tightening, replacing gaskets) can introduce new leaks.

**Virtual leaks vs. real leaks**:

| Characteristic | Real Leak | Virtual Leak |
|---|---|---|
| Gas source | Outside atmosphere entering through a hole | Trapped internal volume slowly releasing gas |
| Helium response | Positive when sprayed with He | No response to external He spray |
| RGA signature | N₂ + O₂ in 4:1 ratio; He when sprayed | N₂ + O₂ present, no He response to spray |
| Pressure vs. time (isolated) | Linear increase (constant rate) | 1/t decay (decreasing rate, eventually plateaus) |
| Fix | Locate and seal the physical opening | Vent the trapped volume or redesign the joint |

## Safety & Hazards

- **Pressurized gas hazards**: Helium cylinders store gas at 150-200 bar. Secure cylinders against tipping with chains or straps. Use pressure regulators rated for the cylinder pressure. Never transport uncapped cylinders. When pressurizing systems for sniffer-mode testing, never exceed the vessel's rated pressure. Most vacuum chambers are not designed for significant positive pressure.
- **Helium asphyxiation risk**: Helium is inert but displaces oxygen in enclosed spaces. Large helium releases in unventilated rooms can reduce O₂ below 19.5% (the alarm threshold). This is a particular risk during extended leak testing sessions where multiple helium cylinders are used. Ensure adequate ventilation. If using bag techniques on large flanges, vent excess helium outdoors rather than into the room.
- **Mass spectrometer filament hazard**: The leak detector's mass spectrometer contains a hot filament (similar to an ionization gauge). Never open the leak detector while powered. The filament operates in vacuum and will burn out instantly if exposed to atmospheric pressure while hot.
- **Calibrated leak handling**: Permeation-type calibrated leaks contain a thin glass or quartz membrane that is fragile. Dropping a calibrated leak destroys it. Capillary-type leaks can clog with dust or condensate. Store calibrated leaks in sealed containers and handle with care. Calibrated leaks are traceable to national standards and have a certified uncertainty, typically ±10-20%. Recalibrate annually.
- **Vacuum implosion**: Components under vacuum (viewports, glass bell jars, thin-walled vessels) can implode. Wear safety glasses when working near vacuum systems. Never use a glass bell jar with chips, scratches, or star cracks.
- **Electrical safety**: Helium leak detectors operate at 120-240 VAC and contain high-voltage components for the mass spectrometer (ion acceleration voltages of 100-500 V). Ground the instrument properly. Disconnect power before servicing internal components.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---|---|---|
| Leak detector cannot reach operating vacuum | Internal pump oil contaminated, or test volume too large for internal pump | Change internal rotary vane pump oil; connect an external roughing pump to assist with initial pump-down of large volumes |
| Background helium reading too high for sensitive detection | Room contaminated with helium from previous testing; ambient He above 5 ppm | Ventilate room for 15-30 minutes; check internal He background before starting; move leak testing to a well-ventilated area |
| False positive readings when spraying lower joints | Helium from a lower spray rising past an unrelated upper joint (He is lighter than air) | Always spray from top down; use a plastic bag to isolate the joint being tested from rising helium |
| Response time too long on large system | Internal turbo pump speed insufficient for system volume; long conductance paths delay helium transport | Use bag technique for patience; add an external turbopump connected near the suspected region; spray closer to the detector connection point |
| No response to helium despite confirmed pressure rise | Virtual leak, not a real leak; or helium spray not reaching the actual leak path | Check RGA for atmospheric gas without He response (virtual leak); try sniffer mode on pressurized system; check for internal trapped volumes |
| Calibrated leak reads outside certified range | Calibrated leak damaged or clogged; leak detector sensitivity drifted | Inspect calibrated leak for physical damage; clean capillary leaks with solvent; recalibrate leak detector against a second calibrated standard |
| Leak detector filament burns out frequently | Operating at pressures above 10⁻³ Torr; oil backstreaming coating the filament | Verify internal pump reaches adequate vacuum before activating filament; install a foreline trap to prevent oil backstreaming; replace with yttria-coated iridium filament |

## See Also

- **[Vacuum Measurement](./measurement.md)**: Pressure gauges, RGA specifications, gauge calibration
- **[Vacuum Pumps](./pumps.md)**: Pump selection for achieving required base pressure
- **[Vacuum Chambers & Sealing](./chambers.md)**: Chamber design, flange types, O-ring selection
- **[Gas Handling](../gas-handling/index.md)**: Gas delivery systems, cylinder regulators, tubing
- **[Measurement](../measurement/index.md)**: General measurement and instrumentation principles

---

*Part of the [Bootciv Tech Tree](../index.md) • [Vacuum Technology](./index.md) • [All Domains](../index.md)*
