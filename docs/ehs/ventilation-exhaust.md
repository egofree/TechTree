# Ventilation & Exhaust Systems

> **Node ID**: ehs.ventilation-exhaust
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 30-70
> **Outputs**: lev_systems, gas_cabinets, abatement_systems, scrubbers, exhaust_monitoring

## Problem

Semiconductor fabrication releases toxic, pyrophoric, and corrosive gases and vapors that must be captured at the source and rendered safe before discharge to atmosphere. General dilution ventilation is entirely inadequate — a 1 ppm silane leak in a fab ballroom would require 25,000 room air changes per hour to dilute below the TLV. Local exhaust ventilation (LEV), gas cabinets with dedicated exhaust, and point-of-use abatement systems are the primary engineering controls for semiconductor chemical hazards. This document covers the design, operation, and maintenance of ventilation and exhaust systems specific to semiconductor manufacturing.

## Local Exhaust Ventilation (LEV)

### Principles

LEV captures airborne contaminants at or near their point of generation, before they enter the worker's breathing zone. The system consists of five components: hood (capture point), ductwork (transport), air cleaner (filtration/scrubbing), fan (motive force), and stack (discharge).

**Capture velocity** requirements for semiconductor operations:

| Contaminant Type | Example | Minimum Capture Velocity | Typical Application |
|-----------------|---------|------------------------|-------------------|
| Gases/vapors, released with low velocity | Solvent evaporation, wafer cleaning | 0.25-0.5 m/s | Chemical bench enclosure |
| Gases/vapors, moderate release | Acid bench, wet processing | 0.5-1.0 m/s | Fume hood, wet bench |
| Actively generated gases/vapors | Etching, dispensing | 1.0-2.5 m/s | Enclosed hood with extraction |
| High-velocity discharge | Pressurized gas leak scenario | 2.5-10 m/s | Emergency exhaust, gas cabinet |

### Fume Hoods

**Chemical fume hood** (standard laboratory hood):
- Face velocity: 0.4-0.6 m/s at design sash opening (typically 45-50 cm height)
- Bypass-type hood maintains face velocity as sash is lowered (air bypasses through a slot above the sash)
- Baffle at rear with slots at bottom, middle, and top — adjustable to optimize capture for gases lighter or heavier than air
- Exhaust volume: 500-1,200 CFM (850-2,000 m³/h) at full sash opening
- Construction: Fiberglass-reinforced plastic (FRP) or epoxy-coated steel for acid resistance. Type 316L stainless steel for HF service (no glass components in HF hoods)
- Sash material: Laminated safety glass, 6 mm minimum thickness. For HF: polycarbonate sash (HF etches glass)
- Performance verification: Smoke test at sash opening (visible smoke captured, not escaping). Face velocity measured at a 6-point grid across the sash opening — all points within ±10% of design velocity

**Walk-in hood** (for large process tools):
- Floor-level opening with full-height sash
- Face velocity: 0.4-0.5 m/s across entire opening
- Volume: 2,000-5,000 CFM (3,400-8,500 m³/h)
- Requires balanced exhaust across the vertical face to prevent dead zones

### Wet Bench Exhaust

Semiconductor wet processing benches (acid etching, cleaning, rinsing) generate acid fumes (HF, HNO₃, H₂SO₄, HCl) and solvent vapors:

- Enclosed wet bench with extraction slots along both sides of the process tank
- Extraction rate: 150-250 CFM per linear foot of bench (900-1,500 m³/h per meter)
- Exhaust duct material: Polypropylene (PP) for general acids. PVDF (polyvinylidene fluoride) for HF service. FRP for mixed acid/solvent service. Never use PVC for HF (permeation over time)
- Drain trap: Wet seal (P-trap) prevents sewer gases from back-flowing into the bench
- Exhaust monitoring: Continuous flow sensor in exhaust duct — alarm if flow drops below 80% of design (indicates blockage or fan failure)

## Gas Cabinet Exhaust

### Gas Cabinet Design

Gas cabinets house high-pressure cylinders of toxic and pyrophoric gases used in semiconductor manufacturing. The cabinet provides primary containment with dedicated exhaust:

**Construction requirements**:
- 12-gauge (2.7 mm) steel or 11-gauge stainless steel construction
- Self-closing, locking door with viewing window (laminated safety glass or polycarbonate)
- Fire-rated construction: minimum 1-hour fire rating for pyrophoric gas cabinets
- Continuous exhaust ventilation: minimum 200 CFM (340 m³/h) per cabinet; 250-400 CFM typical
- Exhaust connection: Hard-piped to dedicated toxic gas exhaust system (never to general fab exhaust)
- Negative pressure maintained inside cabinet relative to surrounding area
- Seismic restraints: Cylinder secured with chains or brackets rated for seismic zone loads
- Automatic fire suppression: Internal sprinkler head (for pyrophoric gases) connected to building fire suppression system

**Gas detection within cabinet**:
- Continuous gas sensor monitoring in the cabinet exhaust stream
- Detection thresholds: Low alarm at 50% of TLV, high alarm at TLV, critical alarm at 2× TLV
- Alarm actions: Low alarm = visual/audible notification. High alarm = automatic cylinder valve closure + visual/audible alarm. Critical alarm = automatic cylinder valve closure + evacuation alarm + emergency response notification

**Valve manifold box (VMB)**:
- Houses distribution valves and regulators for delivering process gases from cylinder to tool
- Same construction and exhaust requirements as gas cabinet
- Typically serves 2-4 process tools from a single gas source
- Purge capability: Inert gas (N₂) purge for cylinder change and maintenance

### Exhaust Duct Systems

**Duct classification** by service:

| Duct System | Service | Material | Velocity |
|-------------|---------|----------|----------|
| Acid exhaust | HF, HNO₃, H₂SO₄, HCl fumes | PVDF, FRP (vinyl ester), PP | 8-12 m/s |
| Solvent exhaust | Isopropanol, acetone, NMP, PGMEA | Galvanized steel, FRP | 8-12 m/s |
| Toxic gas exhaust | AsH₃, PH₃, SiH₄, Cl₂, BCl₃ | 316L SS, fluoropolymer-lined | 10-15 m/s |
| General exhaust | Heat, humidity, minor contaminants | Galvanized steel | 6-10 m/s |
| Ammonia exhaust | NH₃ from CVD processes | 316L SS, FRP | 8-12 m/s |

**Duct design principles**:
- Transport velocity sufficient to prevent condensation and settling: 8-15 m/s for semiconductor applications
- Round ducts preferred (better flow, less condensation accumulation)
- Slope ducts toward collection points (minimum 1° slope) for liquid drainage
- No dead legs or low points where condensate can accumulate (corrosion and blockage risk)
- Flexible connections at tool exhaust ports with approved chemical-resistant flex ducts
- Fire dampers NOT installed in toxic gas exhaust (prevents gas buildup in case of fire)

## Abatement Systems

### Point-of-Use (POU) Abatement

POU abatement treats exhaust at or near the process tool before it enters the central exhaust system. This is the primary control for highly toxic and pyrophoric gases:

**Thermal oxidizer / burner box**:
- Burns pyrophoric gases (SiH₄, PH₃) and flammable organics in a combustion chamber at 800-1,200°C
- Typical design: Natural gas or hydrogen-fired burner with combustion air supply
- Destruction removal efficiency (DRE): >99% for silane, >99% for phosphine
- Effluent treatment: Hot combustion gases pass through water scrubber or wet electrostatic precipitator to remove acid gases (HF, HCl, P₂O₅) formed during combustion
- Monitoring: Temperature sensor at combustion chamber (must maintain >800°C for effective destruction). Flame detector confirms burner operation. Backup electric ignition for automatic restart

**Plasma abatement**:
- Uses RF or microwave plasma to dissociate perfluorocarbons (PFCs: CF₄, C₂F₆, C₃F₈, C₄F₈) and NF₃
- Reaction: CF₄ + O₂ (in plasma) → CO₂ + 2F₂ → CO₂ + 2HF (after water scrubbing)
- DRE: 90-97% for CF₄, >99% for C₂F₆ and higher PFCs
- Advantage: Operates at lower temperature than thermal abatement, lower energy consumption for PFC destruction
- Typically installed at etch tool exhaust

**Wet scrubber (packed bed)**:
- Counter-current packed tower: Exhaust gas flows upward through packed bed (polypropylene or ceramic packing), scrubbing liquid flows downward
- Scrubbing liquor: Caustic solution (NaOH 5-15%) for acid gases (HF, HCl, Cl₂, HBr). Oxidizing solution (NaOCl or KMnO₄) for hydride gases (AsH₃, PH₃). Water for soluble gases (NH₃)
- Removal efficiency: >99% for acid gases at proper liquor concentration and flow rate
- Typical operating parameters: Liquid-to-gas ratio 5-15 L/m³, packing depth 1.5-3.0 m, gas velocity 1-2 m/s (superficial)
- Blowdown: Continuous or periodic discharge of spent scrubbing solution. Must be treated as chemical waste (see [Waste Management](waste-management.md))

**Dry scrubber (adsorbent)**:
- Granular adsorbent media in a disposable cartridge: activated carbon (organics), impregnated alumina (acid gases), specialized media for hydrides
- Advantage: No liquid waste stream. Simple change-out when media exhausted.
- Disadvantage: Limited capacity. Media disposal as hazardous waste. Not suitable for high-concentration streams.
- Application: Backup scrubbing, low-flow tool exhaust, gas cabinet exhaust polishing

### Centralized Scrubbing Systems

Large fabs use centralized scrubbing systems that serve multiple tools through a common exhaust header:

**Central acid scrubber**:
- Serves all acid exhaust from wet benches, etch tools, and cleaning stations
- Typically a multi-stage scrubber: first stage with water wash (recovers most acid), second stage with NaOH solution (polishing to achieve >99.9% removal)
- Capacity: 10,000-50,000 CFM (17,000-85,000 m³/h) typical for a medium fab
- Materials of construction: FRP (vinyl ester resin) shell, PP packing, PVC or FRP ductwork
- Monitoring: Continuous pH monitoring of scrubbing liquor (maintain pH 8-10 in caustic stage). Makeup NaOH addition controlled by pH. Effluent pH logging for environmental compliance.

**Central toxic gas scrubber**:
- Serves toxic gas exhaust from gas cabinets, VMBs, and process tool exhaust
- Multi-stage: Thermal oxidation stage (burns pyrophorics) → quench (cools gas) → caustic scrubber (removes acid gases) → oxidizing scrubber (removes hydrides) → HEPA filter (removes particulates)
- Automatic bypass to emergency scrubber if primary system fails (ensures continuous treatment)
- Instrumentation: Gas analyzer at inlet and outlet for compliance monitoring (DRE verification). Automatic shutoff of gas supply to tools if scrubber goes offline

## Cleanroom Air Management

### Makeup Air Handling

Semiconductor cleanrooms require massive air handling capacity to maintain cleanliness (ISO Class 1-5) and temperature/humidity control:

- Air changes per hour: 500-750 for ISO Class 1 (most stringent), 40-60 for ISO Class 7-8 (sub-fab areas)
- Makeup air (fresh outdoor air): Minimum 5% of total supply air volume, or 15-25 CFM per occupant, whichever is greater. Higher makeup rates required when exhaust volume is high
- Pressurization: Cleanroom maintained at +12.5 to +25 Pa (0.05-0.10 inches water gauge) positive pressure relative to surrounding areas. Air locks at all entrances. Pressure gradient cascades from cleanest (highest pressure) to less clean areas
- Temperature: 21-23°C ±0.5°C (tight tolerance for process control)
- Relative humidity: 40-45% ±3% (prevents static discharge and controls hygroscopic film growth)

### Exhaust Air Energy Recovery

The high exhaust volumes in semiconductor fabs represent significant energy loss. Recovery systems capture waste heat:

- Run-around coil system: Exhaust air heats a glycol solution in a coil; the glycol circulates to a coil in the makeup air stream, preheating incoming air
- Heat pipe system: Sealed pipes with refrigerant transfer heat from exhaust to supply air with no cross-contamination
- Energy recovery effectiveness: 50-70% of sensible heat recovered
- Cannot use enthalpy wheels (rotating heat exchangers) for toxic or corrosive exhaust streams due to cross-contamination risk

## Ventilation System Maintenance

### Inspection and Testing

**Periodic testing requirements**:

| System Component | Test | Frequency |
|-----------------|------|-----------|
| Fume hood face velocity | Anemometer measurement at 6-point grid | Annually (minimum); after any modification |
| LEV capture check | Smoke tube test at process point | Semi-annually |
| Gas cabinet exhaust flow | Flow measurement at exhaust connection | Quarterly |
| Scrubber efficiency | Inlet/outlet gas analysis | Monthly (continuous for hydride scrubbers) |
| Duct integrity | Visual inspection of joints, supports, condensation | Semi-annually |
| Fan performance | Static pressure, flow rate, vibration analysis | Quarterly |
| Emergency exhaust system | Functional test (automatic damper actuation, fan start) | Monthly |

**Common failure modes**:
- Duct corrosion (acid condensate at cold spots): Inspect duct interiors annually; replace corroded sections immediately
- Packing fouling in scrubbers (scale, biological growth): Clean or replace packing annually; maintain biocide in recirculating scrubber liquor
- Fan belt wear: Inspect monthly, replace per manufacturer schedule or when cracking visible
- Damper actuator failure (corrosion, mechanical binding): Test quarterly, lubricate annually
- Condensate trap blockage: Inspect quarterly; install level sensors on critical traps

## See Also

- [Chemical Safety & Toxicology](chemical-safety.md) — TLV limits and hazard classifications for ventilated chemicals
- [Emergency Response](emergency-response.md) — Gas leak response procedures
- [Waste Management](waste-management.md) — Scrubber blowdown and spent media disposal
- [Gas Handling](../gas-handling/index.md) — Gas distribution systems, cylinder handling
- [Occupational Health](../health/occupational-health.md) — General LEV design and exposure monitoring

---

*Part of the [Bootciv Tech Tree](../index.md) · [EHS](./index.md) · [All Domains](../index.md)*
