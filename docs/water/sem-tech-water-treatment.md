# SEM Tech Water Treatment: Membrane Desalination and Purification

> **Node ID**: water.desalination
> **Domain**: Water
> **Timeline**: Years 20-35
> **Outputs**: fresh_water, brine
> **Tags**: materials=[polymers], era=industrial

The low-cost ion exchange membranes developed by SEM Tech (see [SEM Tech Membranes](../chemistry/sem-tech.md)) make electrodialysis (ED) desalination practical at a fraction of the cost of conventional membrane processes. While reverse osmosis dominates large-scale seawater desalination today, ED excels at brackish water treatment (1,000–10,000 mg/L TDS) where it consumes significantly less energy. The SEM Tech membrane — manufactured from pulverized water softener resin beads in a PVC/CPVC binder at under $1 per square foot — removes the single largest cost barrier to deploying ED in bootstrap and small-scale water treatment scenarios.

For the underlying electrodialysis principles and membrane science, see [SEM Tech Electrodialysis](../chemistry/sem-tech-electrodialysis.md).

## Overview

Water desalination and purification are essential capabilities for any settlement, regardless of scale. Brackish groundwater — containing 1,000–10,000 mg/L of total dissolved solids (TDS) — is the most common impaired water source worldwide. Conventional approaches (reverse osmosis, multi-stage flash distillation) require either high-pressure pumping systems or large thermal energy inputs, both of which demand industrial infrastructure.

Electrodialysis using SEM Tech membranes offers an alternative path: moderate-voltage DC power drives ion transport through inexpensive membranes, producing fresh water without high-pressure equipment or exotic materials. The process is modular, scales linearly, and can be powered directly from solar panels or wind turbines without inverters (DC operation).

**Speculative status**: SEM Tech ED desalination has not yet been demonstrated. The membranes have been validated for chlor-alkali electrolysis at TRL 5, but complete ED desalination stacks using SEM Tech membranes remain untested. Performance estimates below are drawn from conventional ED practice and projected SEM Tech membrane properties.

## Membrane Water Treatment Technologies

Several membrane-based water treatment technologies exist, each suited to different feed conditions:

**Electrodialysis (ED)**: Ions are transported through ion exchange membranes under an applied electric field. Removes dissolved salts and charged contaminants. Best suited for brackish water (1,000–10,000 mg/L TDS). Operates at low pressure with moderate DC voltage.

**Reverse osmosis (RO)**: High pressure (15–80 bar) forces water through a semipermeable membrane that blocks dissolved salts. Effective across all salinity ranges, including seawater (35,000+ mg/L TDS). Requires high-pressure pumps, energy recovery devices, and robust membrane housings.

**Nanofiltration (NF)**: A membrane process intermediate between RO and ultrafiltration. Removes divalent ions (Ca²⁺, Mg²⁺, SO₄²⁻) and organic molecules while passing monovalent ions. Used for water softening and organic removal.

**Ultrafiltration/Microfiltration (UF/MF)**: Removes suspended solids, bacteria, and large molecules. Does not remove dissolved salts. Used as pre-treatment for ED or RO.

For bootstrap scenarios, ED with SEM Tech membranes is the most accessible option because it avoids the high-pressure infrastructure of RO and the specialized membrane chemistry of NF.

## SEM Tech ED Desalination

The SEM Tech ED desalination process uses alternating cation and anion exchange membranes — both manufactured from the same low-cost resin-bead process described in [SEM Tech](../chemistry/sem-tech.md) — arranged in a multi-cell stack between two electrodes:

1. **Feed water** (brackish water) enters the diluate channels
2. **DC voltage** is applied across the electrode pair
3. **Cations** (Na⁺, Ca²⁺, Mg²⁺) migrate through cation exchange membranes toward the cathode
4. **Anions** (Cl⁻, SO₄²⁻, HCO₃⁻) migrate through anion exchange membranes toward the anode
5. **Diluate channels** progressively lose ions → fresh water product
6. **Concentrate channels** accumulate ions → brine waste stream

The process produces two output streams: fresh water (typically <500 mg/L TDS) and concentrated brine (20,000–80,000 mg/L TDS depending on recovery rate and feed concentration).

**Key advantage**: No high-pressure pumps are required. The driving force is electrical, not hydraulic. A simple DC power supply or direct solar panel connection suffices. Stack pressure is limited to the hydraulic pressure needed to circulate water through the thin channels (typically 0.5–3 bar).

## Comparison with Reverse Osmosis

| Parameter | ED (SEM Tech) | Reverse Osmosis |
|-----------|--------------|-----------------|
| **Optimal feed TDS** | 1,000–10,000 mg/L | 1,000–45,000+ mg/L |
| **Energy (brackish)** | 0.5–3.0 kWh/m³ | 1.5–4.0 kWh/m³ |
| **Energy (seawater)** | Not economical | 3.0–5.0 kWh/m³ |
| **Operating pressure** | 0.5–3 bar (flow only) | 15–80 bar |
| **Membrane cost** | <$1/sq ft (SEM Tech) | $30–100/sq ft |
| **Water recovery** | 75–90% | 50–85% |
| **Removes non-ionic?** | No | Yes |
| **Pre-treatment needed** | Suspended solids removal | Extensive (scaling control) |
| **Power type** | DC (direct solar possible) | AC (high-pressure pumps) |
| **Scaling sensitivity** | Moderate (EDR mitigates) | High (membrane fouling) |

ED wins decisively for brackish water (1,000–10,000 mg/L TDS): lower energy, lower pressure, lower membrane cost, higher water recovery. RO wins for seawater (>35,000 mg/L TDS) where resistive losses in ED stacks become prohibitive.

## Multi-Stage ED Configuration

For high-purity product water (<100 mg/L TDS from brackish feed), a multi-stage ED system is used:

**Stage 1 — Roughing**: Removes 60–80% of feed TDS. Large cell pairs (1.0–1.5mm spacers), moderate current density (20–40 mA/cm²). Handles the bulk of ion removal efficiently.

**Stage 2 — Polishing**: Further reduces TDS to target levels. Tighter spacers (0.5–0.75mm), lower current density (10–20 mA/cm²) to manage concentration polarization at low ionic strength. May use monovalent-selective membranes if hardness removal is critical.

**Stage 3 (optional) — Trimming**: Final ion removal for high-purity applications (industrial process water). Very low current density, long residence time.

Between stages, the partially desalted water may be recirculated to achieve target quality. A single-pass multi-stage system processes water continuously; a batch recirculation system processes a fixed volume until target TDS is reached.

**Electrodialysis Reversal (EDR)**: Periodically reversing electrode polarity (every 15–30 minutes) flips diluate and concentrate channels, which:
- Dissolves scale deposits on membrane surfaces
- Extends membrane lifetime without chemical cleaning
- Simplifies pre-treatment requirements
- Adds control system complexity but reduces operating cost

## Operating Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Feed TDS range** | 1,000–10,000 mg/L | Brackish water sweet spot |
| **Voltage per cell pair** | 0.5–1.5V | Below water splitting threshold |
| **[Current density](../glossary/current-density.html)** | 10–50 mA/cm² | Higher for concentrated feeds |
| **Stack voltage** | 50–600V DC | Depends on cell pair count |
| **[Energy consumption](../glossary/energy-consumption.html)** | 0.5–3.0 kWh/m³ | Brackish water range |
| **Water recovery** | 75–90% | Balance recovery vs. brine concentration |
| **Cell pair count** | 50–600 | More pairs = higher single-pass removal |
| **Flow velocity** | 5–15 cm/s | Through spacer channels |
| **[Operating temperature](../glossary/operating-temperature.html)** | 15–45°C | Higher temperature lowers resistance |
| **Membrane lifetime** | 1–5 years | Projected for SEM Tech in ED service |
| **Product TDS** | <500 mg/L | Drinking water standard: <1,000 mg/L |

Energy consumption scales roughly linearly with the amount of salt removed. Desalting from 5,000 to 500 mg/L TDS requires approximately 1.0–2.0 kWh/m³ with conventional ED membranes. SEM Tech membrane resistance in ED configuration is uncharacterized but expected to be comparable to conventional heterogeneous membranes based on similar composition.

## Applications

**Drinking water**: Primary application. Brackish groundwater (the most common impaired source) is ideal for ED. Product water meets WHO drinking water standards (<1,000 mg/L TDS, typically <500 mg/L). Modular units can serve communities from 100 to 100,000 people.

**Industrial process water**: Many industrial processes require low-TDS water (boiler feed, cooling tower makeup, chemical processing). ED provides this from brackish sources without RO infrastructure.

**Agricultural irrigation**: Moderately saline water (up to 3,000 mg/L TDS) is acceptable for many crops. ED can partially desalinate highly brackish water to irrigation-suitable levels, consuming less energy than full drinking water treatment. See [SEM Tech Hydroponics](../agriculture/sem-tech-hydroponics.md) for water reuse in controlled growing environments.

**Brine management**: The concentrate stream from ED is a managed brine that must be disposed of responsibly. Options include: evaporation ponds (arid climates), deep well injection (geologically suitable sites), further concentration for salt recovery, or dilution with wastewater effluent.

**Mine water treatment**: Acid mine drainage and process water from mining operations contain dissolved metals and salts. SEM Tech ED can recover fresh water while concentrating the contaminants for treatment. This synergizes with SEM Tech mineral extraction capabilities (see [SEM Tech](../chemistry/sem-tech.md)).

## Safety

- **Brine handling**: Concentrated brine (up to 80,000 mg/L TDS) is corrosive and harmful to vegetation and aquatic life. Containment structures must be chemically resistant (HDPE, PVC). Never discharge untreated brine to surface water or groundwater.
- **Electrical safety**: ED stacks operate at 50–600V DC. Proper grounding, insulation, and lockout/tagout procedures are mandatory during maintenance. Current leakage through failed seals can cause localized electrolysis and gas generation.
- **Hydrogen gas**: Minor hydrogen evolution at the cathode during operation. Ensure ventilation in enclosed installations. Hydrogen accumulation above 4% concentration in air is explosive.
- **Chemical exposure**: Cleaning solutions (acid for scale removal, alkali for organic fouling) require standard chemical handling PPE — goggles, gloves, aprons.
- **Product water quality**: ED removes only dissolved ions. Suspended solids, microorganisms, and organic contaminants pass through unaffected. Post-treatment (disinfection, filtration) is required for drinking water applications.

## Limitations

**Not demonstrated**: SEM Tech ED desalination is speculative. Membranes are validated for chlor-alkali electrolysis (TRL 5) but have not been tested in multi-cell ED stacks for water treatment. Key unknowns: membrane resistance in thin-channel ED geometry, matched cation-anion pair performance, fouling behavior with natural water matrices, and long-term durability in continuous desalination service.

**Not suitable for seawater**: ED becomes uneconomical above approximately 10,000 mg/L TDS due to increasing resistive losses. Seawater desalination (35,000+ mg/L) requires reverse osmosis or thermal processes.

**No non-ionic contaminant removal**: ED transports only charged species. Dissolved organics, silica, microorganisms, and suspended solids are not removed. Pre-treatment (filtration) and post-treatment (disinfection) are essential for potable water.

**Brine disposal**: Every cubic meter of fresh water produced generates 0.1–0.25 m³ of concentrated brine. Inland brine disposal is a significant logistical challenge. Evaporation ponds require large land areas; deep well injection requires suitable geology.

**Divalent ion scaling**: Calcium and magnesium can precipitate as carbonates or hydroxides on membrane surfaces, reducing performance. Electrodialysis reversal (EDR) mitigates this but adds complexity. Pre-treatment to remove hardness may be necessary for high-hardness feeds.

## See Also

- [SEM Tech](../chemistry/sem-tech.md) — ion exchange membrane manufacturing
- [SEM Tech Electrodialysis](../chemistry/sem-tech-electrodialysis.md) — ED principles and process variants
- [SEM Tech Hydroponics](../agriculture/sem-tech-hydroponics.md) — water reuse in controlled growing systems

---

*Part of the [Bootciv Tech Tree](../index.md) | [Water](./index.md) | [All Domains](../index.md)*
