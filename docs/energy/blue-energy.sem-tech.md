# SEM Tech Blue Energy: Salinity-Gradient Power Generation

> **Node ID**: `energy.blue-energy.sem-tech`
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`chemistry.electrodialysis`](../chemistry/electrodialysis.md),
> [`chemistry.electrolysis.sem-tech`](../chemistry/sem-tech.md),
> [`energy.blue-energy`](./blue-energy.md)
> **Enables**: None
> **Outputs**: electrical_power
> **Timeline**: Years 5-30
> **Critical**: No

## Overview

Blue energy — also called salinity-gradient power (SGP) or osmotic power — harvests the free energy released when freshwater mixes with seawater. Wherever a river meets the sea, nature performs a spontaneous dilution that releases approximately 2.5 MJ of free energy per cubic metre of freshwater entering the ocean. Convert that to electricity and you have a continuous, weather-independent renewable source positioned at the exact coastal locations where population and industry concentrate.

Two conversion technologies dominate. **Pressure Retarded Osmosis (PRO)** uses a semipermeable membrane: freshwater crosses by osmosis into pressurised saltwater, diluting it and increasing the volume of the pressurised stream. The extra volume drives a turbine. **Reverse Electrodialysis (RED)** uses ion-exchange membranes arranged in a stack: alternating cells of river water and seawater create a chemical potential difference that drives ions through selective membranes, generating direct electrical current without any turbine or moving parts.

The "SEM Tech" qualifier in this capability node signals that both technologies depend on high-performance membrane manufacturing — semipermeable thin-film composite membranes for PRO, and cation/anion-exchange membranes for RED. These are the same membrane families used in [electrodialysis](../chemistry/electrodialysis.md) and [fuel cells](./fuel-cell.md), making blue energy a late-arrival beneficiary of membrane manufacturing maturity rather than a bootstrappable early technology.

The theoretical energy of mixing is 2.5 MJ/m³ (0.7 kWh/m³) for river water meeting standard seawater (35 g/L NaCl). Practical systems capture 30-50% of this — yielding 0.2-0.35 kWh/m³ in pilot deployments. A river with flow 100 m³/s and an efficient plant could theoretically produce 70-250 MW, but the global exploitable potential is estimated at 1,600-2,000 TWh/year. Statkraft's PRO pilot (Norway, 2009-2013) and the Afsluitdijk RED pilot (Netherlands, 2014) demonstrated the technology at kW scale; commercial viability awaits cheaper, more durable membranes.

## Prerequisites

### Materials

- [Ion-exchange membranes](../chemistry/electrodialysis.md) — alternating cation-exchange (CEM) and anion-exchange (AEM) membranes for RED stacks. Perfluorinated polymer (similar to Nafion) is standard; target properties: 95-99% permselectivity, 1-5 Ω·cm² area resistance, 100-200 μm thickness.
- [Semipermeable membranes](../chemistry/electrodialysis.md) — thin-film composite (TFC) for PRO: polyamide active layer on polysulphone support, 0.5-1.5 nm pore size, 5-15 L/m²/h/bar water permeability.
- Electrode materials — carbon-based or metal-oxide electrodes for RED (redox couple in electrode rinse solution, typically FeCl₂/FeCl₃ or NaCl with chlorine evolution)
- [Steel](../metals/iron-steel.md) — pressure housings for PRO, stack frames for RED
- [Copper](../metals/copper-refining.md) — electrode current collectors and bus bars
- River water pretreatment — filtration media (sand, cartridge filters, ultrafiltration membranes) to remove suspended solids that would foul membranes

### Tools and Equipment

- [Electrodialysis](../chemistry/electrodialysis.md) — membrane stack fabrication and testing capability
- [Electrolysis (SEM Tech)](../chemistry/sem-tech.md) — advanced membrane electrode assembly manufacturing
- Pressure exchanger or turbine — for PRO energy recovery (Pelton wheel or rotary pressure exchanger, 80-95% efficiency)
- DC power conditioning — inverters to convert RED DC output to grid AC
- Water intake and outfall structures — screened intake, mixing discharge channel
- Membrane testing rig — permeability, permselectivity, and fouling resistance measurement

### Knowledge

- Osmosis and osmotic pressure: the chemical potential difference between fresh and salt water creates a pressure. For seawater (35 g/L NaCl), osmotic pressure π = iMRT ≈ 27 bar (2.7 MPa). PRO operates with the saltwater side at 50-80% of osmotic pressure (13-22 bar).
- Nernst equation for RED voltage: each fresh/salt cell pair generates E = (RT/zF) × ln(a_salt / a_fresh) ≈ 0.12-0.17 V per cell pair at 25°C. A practical stack with 50-200 cell pairs generates 6-34 V DC.
- Membrane fouling: river water contains organic matter, colloids, and biofilm precursors that accumulate on membrane surfaces, reducing flux (PRO) or increasing resistance (RED) by 20-50% over weeks to months. Pretreatment and periodic cleaning are essential.
- Permselectivity: real membranes are not perfectly selective. Co-ion leakage reduces voltage and current efficiency. Target: >95% permselectivity for both CEM and AEM.

### Infrastructure

- **Coastal or estuarine site** — proximity to both a freshwater source (river, lake discharge) and seawater (ocean, sea). The two water streams must be available at sufficient flow rates.
- **Intake and pretreatment** — river water must be screened (1-5 mm bar screen), filtered (sand filter + 5-20 μm cartridge), and optionally ultrafiltered to protect membranes from fouling. Seawater requires similar treatment plus biological control (chlorination, UV).
- **Power conditioning** — RED produces DC at 6-50 V; requires DC-DC boost and DC-AC inverter for grid connection. PRO produces hydraulic power converted to electricity via turbine-generator.
- **Discharge management** — the brackish outflow mixes with ambient seawater; discharge location must avoid estuarine ecosystem disruption.

## Bill of Materials

### RED Pilot Plant (5 kW net output)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|--------------|
| Cation-exchange membranes (CEM) | 50-100 m² (100-200 sheets, 0.5 × 0.5 m) | [Electrodialysis](../chemistry/electrodialysis.md) — perfluorinated polymer casting | Hydrocarbon-based CEM (cheaper, shorter life) |
| Anion-exchange membranes (AEM) | 50-100 m² (matching CEM count) | [Electrodialysis](../chemistry/electrodialysis.md) — perfluorinated polymer casting | Hydrocarbon-based AEM (cheaper, less stable) |
| Spacer gaskets (silicone or EPDM) | 200-400 sheets, 0.2-0.5 mm | [Polymers](../polymers/index.md) | PVC (cheaper, less compliant) |
| Electrodes (Ti/Pt-coated or graphite) | 2 pieces, 0.25 m² each | [Metals](../metals/index.md) | Stainless steel (lower performance) |
| Electrode rinse solution (FeCl₂/FeCl₃ in NaCl) | 200-500 L | [Chemistry](../chemistry/index.md) | NaCl alone (lower current density) |
| Steel frame (stack housing) | 1 unit, 100-200 kg | [Iron and steel](../metals/iron-steel.md) | Stainless steel 316L (seawater resistant) |
| Copper bus bars and cabling | 10-20 kg | [Copper refining](../metals/copper-refining.md) | Aluminium bus (larger cross-section) |
| DC-AC inverter (5 kW, 48 V DC input) | 1 unit | [Electronics](../electronics/index.md) | — |

### PRO Pilot Plant (5 kW net output)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|--------------|
| Semipermeable TFC membranes | 2,000-5,000 m² (spiral-wound modules) | [Electrodialysis](../chemistry/electrodialysis.md) / RO membrane manufacturing | Cellulose acetate (lower flux, biodegradable) |
| Pressure vessel housing (steel) | 10-20 modules, rated 25-30 bar | [Iron and steel](../metals/iron-steel.md) | Fibreglass (corrosion resistant, lower pressure rating) |
| Pelton turbine + generator (5 kW) | 1 set | [Water turbines](./water-turbines.md) | Francis turbine (less efficient at low flow) |
| Pressure exchanger (isobaric type) | 1 unit, 90-95% energy recovery | [Precision machining](../machine-tools/machining.md) | Turbocharger-type (slightly lower recovery) |
| High-pressure piping (316L SS, 25 mm NB) | 50-100 m | [Iron and steel](../metals/iron-steel.md) | — (steel essential at these pressures) |

## Process Description

### Reverse Electrodialysis (RED)

1. **Pretreat water**: Screen river water to <50 μm and seawater to <50 μm. Dose with biocide (NaOCl, residual 0.5-1.0 mg/L) to control biofouling. Dechlorinate before membrane contact if using chlorine-sensitive membranes.
2. **Feed the stack**: Pump river water (LOW salinity, 0.5-1 g/L) and seawater (HIGH salinity, 30-35 g/L) into alternating cells in the membrane stack. Flow rate: 1-3 cm/s superficial velocity through spacers.
3. **Ion transport generates current**: Sodium ions (Na⁺) migrate from seawater cells through CEM toward the cathode. Chloride ions (Cl⁻) migrate through AEM toward the anode. The electrode rinse solution (Fe²⁺/Fe³⁺ redox couple or water electrolysis reactions) completes the circuit at the electrodes.
4. **Collect power**: The stack generates DC at 6-50 V (depending on cell pair count) and 10-200 A (depending on membrane area and salinity gradient). Feed to DC-DC converter and inverter for grid AC.
5. **Manage brine discharge**: The exit streams are partially equilibrated brackish water. Discharge to the estuary at the river-sea interface where natural mixing occurs.
6. **Clean-in-place (CIP)**: Every 2-8 weeks, flush with biocide, acid (0.5-1% HCl), or EDTA solution to remove biofilm, scale, and organic fouling. Monitor pressure drop and resistance trends to schedule cleaning.

### Pressure Retarded Osmosis (PRO)

1. **Pretreat both streams** as for RED — particulate removal to protect membrane surfaces.
2. **Pressurise seawater**: Pump seawater to 13-22 bar (50-80% of osmotic pressure) using a high-pressure pump. Energy recovery from the depressurised brine is via pressure exchanger (isobaric type, 90-95% efficient).
3. **Osmotic dilution**: River water flows on the low-pressure side of the semipermeable membrane. Water crosses by osmosis into the pressurised seawater, diluting it and increasing its volume by 20-40%.
4. **Turbine generation**: The excess pressurised water (inflow volume minus original seawater volume) splits to a Pelton turbine driving a generator. Net power: P = Q_dil × ΔP × η_turbine, where Q_dil is the dilution flow and ΔP is the operating pressure.
5. **Discharge**: Depressurise the brackish outflow through the pressure exchanger (recovering energy), then discharge to the estuary.

## Quantitative Parameters

| Parameter | RED | PRO | Notes |
|-----------|-----|-----|-------|
| Theoretical energy (mixing) | 0.7 kWh/m³ river | 0.7 kWh/m³ river | For 35 g/L seawater at 25°C |
| Practical efficiency | 30-40% | 35-50% | Membrane and conversion losses |
| Net energy yield | 0.2-0.3 kWh/m³ | 0.25-0.35 kWh/m³ | After pumping and pretreatment |
| Power density | 0.5-2.0 W/m² membrane | 2-5 W/m² membrane | Target: >5 W/m² for commercial viability |
| Operating pressure | 0.1-0.5 bar (hydraulic only) | 13-22 bar | PRO requires high-pressure rated equipment |
| Stack voltage | 6-50 V DC (50-200 cell pairs) | N/A | RED direct DC output |
| Current density | 10-40 A/m² | N/A | Limited by membrane resistance |
| Membrane life | 5-10 years | 7-10 years | Fouling is the primary degradation mode |
| System life | 20-30 years | 20-30 years | Membranes replaced; structures last longer |
| Capacity factor | 90-95% | 90-95% | Continuous — not weather-dependent |
| Water pretreatment energy | 0.02-0.10 kWh/m³ | 0.03-0.15 kWh/m³ | Pumping and filtration parasitic load |
| Capital cost (pilot) | $5-15/W installed | $5-20/W installed | Target: <$2/W for commercial |

### Global Resource Estimate

| Location | Theoretical potential | Exploitable (practical) | Status |
|----------|----------------------|------------------------|--------|
| Global (all estuaries) | ~1,650 TWh/year | 600-2,000 TWh/year | Theoretical studies |
| Norway (Statkraft PRO site) | ~12 TWh/year | 6 TWh/year | Pilot 2009-2013, decommissioned |
| Netherlands (Afsluitdijk RED) | ~3 TWh/year | 1-2 TWh/year | Pilot 2014, ongoing |
| Rhine estuary (Netherlands) | ~5 TWh/year | 2-3 TWh/year | Feasibility studied |
| Mississippi (USA) | ~100 TWh/year | 20-50 TWh/year | Not deployed |

## Scaling Notes

- **Bench scale** (<1 W): Single cell pair in a laboratory acrylic stack. Membrane area 10-100 cm². Demonstrates the voltage per cell pair and validates membrane permselectivity. Total membrane area <0.1 m².
- **Pilot scale** (1-50 kW): 50-200 cell pairs with 0.25-1.0 m² membrane per cell. Validates water pretreatment requirements, fouling rates, and net energy balance (output minus pumping power). This is where membrane durability data is generated.
- **Commercial scale** (1-200 MW): Thousands of membrane modules in parallel. Requires a large river-sea interface, extensive pretreatment (ultrafiltration plant), and significant civil works for intake and outfall. The membrane area alone for a 1 MW RED plant exceeds 500,000 m².

Key scaling challenges: **membrane cost dominates** — at $50-200/m², membranes represent 50-70% of capital cost. A 1 MW RED plant needs 500,000-1,000,000 m² of membrane ($25-200M just for membranes). Membrane durability (5-10 year replacement cycle) is the dominant operating cost after the initial capital. Pretreatment water quality is non-negotiable — river water with high turbidity or organic load makes fouling uncontrollable. PRO's high-pressure equipment (pumps, vessels, piping rated for 25+ bar) adds significant capital cost that RED avoids.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Stack voltage decline (>10% from baseline) | Membrane fouling (biofilm, organic, or scaling), increased co-ion leakage from membrane degradation | Perform CIP cleaning (acid, biocide, EDTA); if voltage does not recover, test individual membrane sheets for permselectivity and resistance; replace membranes with <80% original performance |
| High stack pressure drop (>0.5 bar) | Spacer clogging from particulate fouling, biological growth blocking flow channels | Backflush the stack; increase pretreatment filtration; inspect spacers for biofilm; if severe, disassemble and manually clean membranes |
| Low current density (<10 A/m²) | High membrane resistance (degradation or drying), low salinity gradient (diluted seawater or salty river), poor electrode contact | Measure individual membrane resistance; check salinity of both feed streams (target: seawater >30 g/L, river <1 g/L); inspect electrode connections and rinse solution concentration |
| Electrode corrosion | Reverse polarity without redox buffer, chloride attack on stainless electrodes | Use Ti/Pt-coated or mixed metal oxide electrodes; maintain electrode rinse solution Fe²⁺/Fe³⁺ concentration; avoid polarity reversal |
| PRO membrane rupture | Pressure surge exceeding membrane rating, mechanical stress from module loading | Install pressure relief valves and dampeners; ramp pressure slowly at startup (<1 bar/s); replace damaged modules |
| PRO low dilution flow (<20% volume increase) | Membrane fouling reducing water flux, membrane compaction (creep), excessive operating pressure | Clean membranes; verify operating pressure is 50-80% of osmotic pressure (not higher); check for membrane compaction after extended operation — replace modules after 7-10 years |
| Biofouling (biofilm on membrane surface) | River water organic content, warm water temperature, insufficient biocide dosing | Optimise pretreatment (increase chlorination to 0.5-1 mg/L residual, dechlorinate before membrane); increase CIP frequency in summer; consider ultrafiltration pretreatment |

## Safety

- **High pressure (PRO only)**: Operating pressure 13-22 bar. A ruptured pipe or vessel at these pressures releases stored energy violently. All high-pressure equipment must be rated with 3× safety factor, fitted with pressure relief valves, and enclosed in blast shields during commissioning. Never open a pressurised PRO module — depressurise fully first.
- **Electrical (RED)**: Stack voltage 6-50 V DC at 10-200 A. Contact with electrolyte-carrying channels can deliver a shock. Insulate all bus bars and terminals; ground the stack frame; use insulated tools when adjusting electrodes.
- **Biocide handling**: Sodium hypochlorite (NaOCl) for antifouling is a strong oxidiser. 12-15% solution causes eye and skin burns. Store away from acids (releases toxic Cl₂ gas on contact). Wear chemical splash goggles and nitrile gloves when dosing.
- **Electrode rinse solution (FeCl₂/FeCl₃)**: Iron chloride solutions are corrosive and stain surfaces. pH 2-3 in use. Wear chemical-resistant gloves and eye protection.
- **Drowning risk**: Intake structures on rivers and coasts have powerful suction at the intake screens. Install physical guards. Never enter the water near an operating intake.

## Quality Control

### Acceptance Criteria

- **Membrane permselectivity**: >95% for both CEM and AEM at 0.1/0.5 M NaCl gradient. Test: measure membrane potential and compare to Nernst theoretical.
- **Membrane area resistance**: <5 Ω·cm² for CEM, <10 Ω·cm² for AEM in 0.5 M NaCl at 25°C.
- **PRO membrane water permeability**: >5 L/m²/h/bar (A-factor). Salt rejection >95%.
- **Stack net power density**: >1.0 W/m² membrane for RED (target >2.0 W/m² for commercial).
- **Pretreated water quality**: Turbidity <1 NTU, SDI (silt density index) <3 for membrane feed.
- **System net energy balance**: Gross electrical output minus pumping and pretreatment energy must be positive over a 24-hour period.

### Testing Methods

- **Membrane characterisation**: Permselectivity by membrane potential measurement (calomel reference electrodes, salt bridges); area resistance by electrochemical impedance spectroscopy (EIS) in a 4-electrode cell.
- **Stack performance**: Measure open-circuit voltage, short-circuit current, and maximum power point (I-V curve sweep) with variable load resistance.
- **Fouling monitoring**: Track pressure drop across stack, membrane resistance (via periodic EIS or conductivity probe), and net power output daily. Plot trends; alert if degradation rate exceeds 1%/week.
- **Water quality**: Turbidity meter (daily), SDI test (weekly), total organic carbon (monthly), and microbiological count (monthly).

### Sampling Protocol

- Continuous: stack voltage, current, temperature, flow rates, pressures
- Daily: net energy output, pumping energy, feed water salinity
- Weekly: membrane resistance spot-checks, pressure drop trends
- Monthly: full I-V curve, water quality panel, visual inspection of intake screens

## Variations and Alternatives

### Technology Comparison

| Criterion | RED | PRO |
|-----------|-----|-----|
| Output form | Direct DC electricity | Hydraulic → turbine → AC electricity |
| Moving parts | Pumps only | Pumps, pressure exchanger, turbine |
| Membrane type | Ion-exchange (CEM + AEM) | Semipermeable (TFC) |
| Operating pressure | Low (<0.5 bar) | High (13-22 bar) |
| Power density | 0.5-2.0 W/m² | 2-5 W/m² |
| Maturity | Pilot | Pilot |
| Capital cost | Membrane-dominated | Membrane + pressure equipment |
| Scalability | Modular (add cell pairs) | Modular (add membrane modules) |
| Fouling sensitivity | High (thin spacers clog) | Moderate (wider feed channels) |

### Alternative Salinity-Gradient Technologies

- **Capacitive Mixing (CAPMIX)**: Uses porous carbon electrodes in alternating contact with fresh and salt water. Voltage changes with salinity; energy extracted by charging in high-salinity and discharging in low-salinity. Lower power density (<0.5 W/m²) but no membranes. Research stage.
- **Reverse Osmosis (energy consumer, not producer)**: RO desalination consumes 3-5 kWh/m³ to separate fresh from salt water. Blue energy is the reverse process, recovering up to 0.7 kWh/m³ when they mix back. Co-locating RO plants with blue energy outflows can partially offset desalination energy.

### Complementary Coastal Energy

Blue energy is continuous and weather-independent, complementing intermittent coastal renewables: [tidal](./water-turbines.md), [wind](./wind.md), and [solar](./photovoltaics.md). The continuous baseload nature (90-95% capacity factor) makes it valuable for grid stability where intermittent sources dominate.

## References

- [Electrodialysis](../chemistry/electrodialysis.md) — membrane manufacturing capability underlying both RED and PRO
- [Electrolysis (SEM Tech)](../chemistry/sem-tech.md) — advanced membrane and electrode assembly technology
- [Blue energy overview](./blue-energy.md) — parent capability for osmotic power generation
- [Fuel cell](./fuel-cell.md) — shares membrane electrode assembly technology with RED stacks
- [Water turbines](./water-turbines.md) — Pelton turbine for PRO energy conversion
- [Redox flow battery](./redox-flow-battery.md) — similar electrochemical stack architecture with ion-exchange membranes
- [Electrical systems](../electronics/electrical-systems.md) — DC-AC power conversion for grid interconnection

---
*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
