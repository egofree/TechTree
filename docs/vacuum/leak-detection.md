# Vacuum Leak Detection & Seal Integrity

> **Node ID**: vacuum.leak-detection
> **Domain**: [Vacuum Technology](./index.md)
> **Dependencies**: `vacuum.measurement`, `measurement`, `gas-handling`
> **Enables**: Semiconductor process tools, UHV systems, hermetic packaging
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

## See Also

- **[Vacuum Measurement](./measurement.md)**: Pressure gauges, RGA specifications, gauge calibration
- **[Vacuum Pumps](./pumps.md)**: Pump selection for achieving required base pressure
- **[Vacuum Chambers & Sealing](./chambers.md)**: Chamber design, flange types, O-ring selection
- **[Gas Handling](../gas-handling/index.md)**: Gas delivery systems, cylinder regulators, tubing
- **[Measurement](../measurement/index.md)**: General measurement and instrumentation principles

[← Back to Vacuum](index.md)
