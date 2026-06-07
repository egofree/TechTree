# Desalination

> **Node ID**: water.desalination
> **Domain**: [Water](./index.md)
> **Dependencies**: [`chemistry.electrodialysis`](../chemistry/sem-tech-electrodialysis.md)
> **Enables**: [`energy.electricity`](../energy/electricity.md)
> **Timeline**: Years 25-45
> **Outputs**: fresh_water, brine
> **Critical**: No — essential only in water-scarce coastal or brackish regions; most civilizations can develop without it initially


Removing dissolved salts from seawater (35,000 mg/L TDS) or brackish water (1,000-10,000 mg/L TDS) to produce fresh water suitable for agriculture, industry, and human consumption. Desalination becomes necessary when freshwater sources are insufficient — arid coastal regions, island communities, and drought-prone areas. Global desalination capacity exceeds 100 million m³/day, with reverse osmosis accounting for roughly 70% of installed capacity.

Desalination methods fall into three families:

1. **Thermal distillation** — phase-change methods that boil and recondense water (MSF, MED)
2. **Membrane separation** — pressure- or voltage-driven filtration through semipermeable membranes (RO, electrodialysis)
3. **Emerging/hybrid** — forward osmosis, membrane distillation, solar stills

This capability covers the three dominant methods: multi-stage flash distillation, reverse osmosis, and electrodialysis. Pretreatment and post-treatment are critical for all methods.


## Materials
- [Seawater or brackish water](procurement.md) as feed
- Semipermeable membranes (polyamide thin-film composite for RO, ion-exchange for electrodialysis) — from [Polymers](../polymers/index.md)
- Stainless steel or titanium alloy for heat exchangers and high-pressure components — from [Metals](../metals/index.md)
- Concrete for intake structures and holding basins — from [Chemistry: Cement](../chemistry/cement.md)
- Antiscalant chemicals (polyphosphates, polyacrylates) — from [Chemistry](../chemistry/index.md)
- Cleaning chemicals (citric acid, sodium hydroxide) for membrane maintenance

## Tools
- High-pressure pumps (55-70 bar for seawater RO)
- Pressure recovery devices (energy recovery turbines or isobaric exchangers)
- Heat exchangers (for thermal methods)
- Turbidity and conductivity meters for monitoring
- Membrane integrity testing equipment

## Knowledge
- Osmotic pressure and solution chemistry
- Membrane fouling mechanisms and control strategies
- Corrosion management in high-salinity environments
- Energy recovery thermodynamics

## Infrastructure
- Reliable [electricity supply](../energy/electricity.md) — desalination is energy-intensive
- Seawater intake and brine outfall structures
- Pretreatment and post-treatment process trains
- Control systems for continuous operation

## Bill of Materials

| Material | Quantity per 1,000 m³/day plant | Source | Alternatives |
|----------|--------------------------------|--------|-------------|
| RO membrane elements (8-inch) | 150-300 elements | [Polymers](../polymers/index.md) | None — specialized product |
| High-pressure pump | 2-4 units | [Machine Tools](../machine-tools/index.md), [Metals](../metals/index.md) | — |
| Energy recovery device | 1-2 units | [Machine Tools](../machine-tools/index.md) | Hydraulic turbocharger |
| Stainless steel piping (316L) | 500-2,000 m | [Metals](../metals/index.md) | Duplex stainless, titanium |
| Concrete (intake/outfall) | 50-200 m³ | [Chemistry: Cement](../chemistry/cement.md) | — |
| Antiscalant | 2-10 L/day | [Chemistry](../chemistry/index.md) | Acid dosing (sulfuric acid) |


## Reverse Osmosis (RO)

The dominant desalination technology worldwide. Pressure forces water through a semipermeable membrane that rejects dissolved salts and contaminants. Developed for practical desalination in the 1960s-1970s, RO now accounts for approximately 70% of global desalination capacity.

**Prerequisites**: [Polymer capability](../polymers/index.md) for membrane production, [high-pressure pumps](../machine-tools/index.md), [electricity](../energy/electricity.md).

**How it works**: A high-pressure pump pressurizes pretreated feedwater to 55-70 bar for seawater (15-25 bar for brackish water), exceeding the osmotic pressure of the feed. Water molecules pass through the semipermeable membrane while dissolved salts are rejected. The product water (permeate) typically contains less than 500 mg/L TDS. The concentrated reject stream (brine) is discharged.

**Key components**:
- Polyamide thin-film composite (TFC) membranes in spiral-wound configuration
- High-pressure pump (multistage centrifugal or positive displacement)
- Energy recovery device (isobaric exchanger or hydraulic turbocharger)
- Cartridge filters (5 micron) as final pretreatment guard

**Energy requirements**: 3-5 kWh/m³ for modern seawater RO with energy recovery. Without energy recovery: 7-10 kWh/m³. Brackish water RO: 1-2.5 kWh/m³ due to lower pressure requirements.

**Expected performance**:
- Salt rejection: 99.2-99.8%
- Product water TDS: 200-500 mg/L (from 35,000 mg/L seawater)
- Recovery rate: 35-50% for seawater, 65-85% for brackish water
- Membrane lifespan: 3-7 years with proper pretreatment and cleaning

**Strengths**:
- Lowest energy consumption of any seawater desalination method
- Modular — plants can be scaled incrementally
- Compact footprint compared to thermal methods
- Well-established technology with 50+ years of operational data

**Weaknesses**:
- Membranes are sensitive to fouling (biological, scaling, particulate)
- Requires extensive pretreatment (media filtration, antiscalant dosing, cartridge filtration)
- Membrane replacement is a significant operating cost ($200-400 per element every 3-7 years)
- Limited recovery rate for seawater (35-50%) — large brine volume

## Multi-Stage Flash Distillation (MSF)

The original industrial-scale desalination method. Seawater is heated and then introduced into a series of chambers (stages) at progressively lower pressures, causing the water to flash-boil (rapidly vaporize). The steam is condensed on heat exchanger tubes to produce fresh water.

**Prerequisites**: [Steam power](../energy/steam-power.md) or large heat source, large-scale heat exchangers, [electricity](../energy/electricity.md) for pumping.

**How it works**: Seawater is heated to 90-120°C in a brine heater using steam. The heated brine enters the first flash stage, which is maintained at a pressure below the saturation pressure of the brine. The sudden pressure drop causes a fraction of the brine to flash into steam. The steam condenses on tubes carrying incoming cold feedwater, simultaneously preheating the feed and producing distillate. This repeats across 15-25 stages.

**Key components**:
- Brine heater (shell-and-tube heat exchanger)
- Flash chambers (15-25 stages) with condenser tube bundles
- Large seawater circulation pumps
- Venting system for non-condensable gases
- Degasifier for dissolved oxygen and CO₂ removal

**Energy requirements**: 50-100 kWh/m³ thermal energy + 3-5 kWh/m³ electrical energy. MSF is the most energy-intensive commercial desalination method. The high thermal demand makes it economical only where waste heat or cheap steam is available.

**Expected performance**:
- Product water TDS: <25 mg/L (extremely pure)
- Recovery rate: 10-15% (very low — large brine volume)
- Plant availability: 90-95% (robust, tolerant of variable feed quality)
- Top brine temperature: 90-120°C

**Strengths**:
- Extremely pure product water (<25 mg/L TDS)
- Robust — tolerant of variable feedwater quality and high temperatures
- Long plant life (25-30+ years)
- Can use low-grade waste heat, improving overall thermal efficiency when co-located with power plants

**Weaknesses**:
- Highest energy consumption of any commercial desalination method
- Very large physical footprint
- Low recovery rate (10-15%)
- High capital cost due to large heat exchanger surface area
- Corrosion in hot brine environment requires exotic materials (titanium, high-grade stainless)

## Electrodialysis (ED)

An electrically driven membrane process that uses ion-selective membranes to remove dissolved salts. Unlike RO, which pushes water through a membrane, ED pulls ions out of the water using an electric field. See [Chemistry: Electrodialysis](../chemistry/sem-tech-electrodialysis.md) for the underlying membrane and electrochemistry principles.

**Prerequisites**: [Electrodialysis capability](../chemistry/sem-tech-electrodialysis.md) for ion-exchange membranes, [electricity](../energy/electricity.md), [basic water treatment](basic-treatment.md) for pretreatment.

**How it works**: Pairs of cation-exchange and anion-exchange membranes are stacked in alternating sequence between two electrodes. When a voltage is applied, cations migrate toward the cathode and anions toward the anode. The ion-selective membranes create alternating compartments of diluted (desalted) and concentrated (brine) water.

**Energy requirements**: 0.5-3 kWh/m³ for brackish water (1,000-5,000 mg/L TDS). Energy consumption scales linearly with the amount of salt removed, making ED efficient for low-salinity feeds but impractical for seawater (would require 15-25 kWh/m³).

**Expected performance**:
- Best suited for brackish water (1,000-5,000 mg/L TDS)
- Salt removal: 50-94% per pass (configurable)
- Recovery rate: 80-95% (higher than RO for brackish water)
- Membrane lifespan: 5-10 years

**Strengths**:
- Higher recovery rate than RO for brackish water (80-95%)
- Lower operating pressure — less mechanical stress on equipment
- Energy scales with salt removed — very efficient for low-salinity feeds
- Membranes are more tolerant of chlorine than RO membranes

**Weaknesses**:
- Not economical for seawater desalination (energy scales linearly with salinity)
- Does not remove non-ionic contaminants (silica, boron, pathogens)
- Membrane scaling and fouling require periodic cleaning and reversal (EDR variant)
- Higher capital cost per unit capacity than RO for seawater applications

## Method Comparison

| Parameter | RO | MSF (Thermal) | Electrodialysis |
|-----------|----|---------------|-----------------|
| **Feedwater** | Seawater or brackish | Seawater | Brackish water |
| **Energy (kWh/m³)** | 3-5 (seawater), 1-2.5 (brackish) | 50-100 thermal + 3-5 electrical | 0.5-3 (brackish) |
| **Product TDS (mg/L)** | 200-500 | <25 | 100-500 |
| **Recovery rate** | 35-50% (SW), 65-85% (BW) | 10-15% | 80-95% |
| **Membrane lifespan** | 3-7 years | N/A (heat exchangers) | 5-10 years |
| **Pretreatment needs** | High | Low-Medium | Medium |
| **Best for** | Large-scale seawater | Waste-heat available | Brackish water |

Reverse osmosis is the default choice for new seawater desalination installations due to its lower energy consumption. MSF remains in use where waste heat is abundant (co-located with power plants in the Middle East). Electrodialysis is the preferred method for brackish water desalination where high recovery rates are important.

## Pretreatment

All desalination methods require feedwater pretreatment to protect membranes or heat exchangers.

**Common pretreatment steps**:
1. **Coarse screening** — bar screens (5-10 mm) remove debris, seaweed, and marine organisms from intake water
2. **Chlorination** — sodium hypochlorite dosing (0.5-2 mg/L residual) controls biological growth. Must be dechlorinated before RO membranes (sodium bisulfite dosing to <0.1 mg/L residual) — polyamide membranes are destroyed by chlorine
3. **Media filtration** — dual-media (anthracite + sand) or multi-media filters remove suspended solids to <0.5 NTU SDI <3 for RO
4. **Antiscalant dosing** — polyphosphate or polyacrylate dosing (2-5 mg/L) prevents calcium carbonate, calcium sulfate, and silica scaling on membranes
5. **Cartridge filtration** — 5-micron pleated cartridges as final guard before RO membranes
6. **pH adjustment** — sulfuric acid dosing to pH 6.5-7.0 reduces scaling tendency and improves membrane performance

For thermal methods, pretreatment is simpler: anti-foaming agents, scale inhibitors (polyphosphates at 2-5 mg/L), and degasification to remove oxygen and CO₂.

## Post-Treatment

Desalinated water is corrosive and mineral-deficient. Post-treatment is required before distribution.

1. **Remineralization** — lime (calcium hydroxide) or limestone contactors add calcium and alkalinity. Target: 80-120 mg/L as CaCO₃ hardness, 50-80 mg/L alkalinity. Without remineralization, the water will dissolve concrete pipes and metal fixtures.
2. **pH adjustment** — soda ash (sodium carbonate) or CO₂ dosing to stabilize pH at 7.5-8.0
3. **Disinfection** — chlorination (0.2-0.5 mg/L residual) for distribution system protection, following the same principles as [basic water treatment](basic-treatment.md)
4. **Fluoridation** — optional, for dental health (0.7-1.2 mg/L as F⁻)

## Brine Management

All desalination methods produce concentrated brine. For seawater RO at 40% recovery, the brine is approximately 60,000 mg/L TDS. For MSF at 12% recovery, the brine is approximately 40,000 mg/L TDS.

**Disposal options**:
- **Surface water discharge** — most common for coastal plants. Requires diffusers for rapid mixing. Monitor salinity at discharge boundary (target <1,000 mg/L above ambient within 100 m of outfall)
- **Subsurface injection** — deep well injection into saline aquifers. Used for inland brackish water plants
- **Evaporation ponds** — solar evaporation in arid climates. Requires large land area (1-3 m² per m³/day brine)
- **Zero liquid discharge (ZLD)** — thermal crystallizer produces solid salt for disposal or sale. Energy-intensive: adds 15-25 kWh/m³ to overall consumption

## Scaling Notes

- **Community scale** (500-5,000 people, 100-1,000 m³/day): Brackish water RO or electrodialysis if brackish source available. Seawater RO at small scale has higher unit cost. Energy requirement: 300-5,000 kWh/day.
- **Municipal scale** (50,000+ people, 10,000+ m³/day): Seawater RO is the standard. Energy recovery devices are essential for economic operation. Typical plant: 100,000 m³/day at 3.5-4.5 kWh/m³.
- **Industrial scale**: Dedicated RO or ED units sized for specific water quality needs. Power plants and refineries often co-locate MSF with waste heat streams.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| RO membrane salt rejection dropping below 97% | Membrane degradation from chlorine exposure, compaction, or hydrolysis | Check dechlorination system (target <0.1 mg/L chlorine). Replace degraded elements. Verify pH within 6.5-7.5 operating range. |
| RO permeate flow declining >15% from baseline | Membrane fouling (biological, scaling, or particulate) | Clean membranes per manufacturer protocol: low-pH cleaning (citric acid, pH 2-3) for scaling; high-pH cleaning (NaOH, pH 11-12) for biological fouling. Check pretreatment performance. |
| High-pressure pump cavitation | Insufficient feed pressure, clogged intake screens, air in suction line | Clean intake screens. Check suction pressure gauge (maintain >2 bar). Vent air from pump casing. |
| MSF distillate conductivity rising | Tube leak in condenser bundle, non-condensable gas buildup | Isolate and plug leaking tubes. Check venting system operation. Monitor brine level in flash chambers. |
| ED stack resistance increasing | Membrane scaling or fouling, spacer channel blockage | Clean-in-place with acid (HCl, 2-5%) for scaling, base (NaOH, 1-2%) for organic fouling. Check electrode condition. |
| Product water corrosive (blue-green staining, pipe leaks) | Insufficient remineralization — water dissolving copper pipes | Increase lime dosing. Target Langelier Saturation Index (LSI) of -0.5 to +0.5. Check alkalinity >50 mg/L as CaCO₃. |

## Safety

- **High-pressure systems**: RO operates at 55-70 bar (800-1,000 psi). High-pressure piping failure can cause whip-lash injuries and water jet cuts. Pressure relief valves, burst discs, and regular inspection of high-pressure fittings are mandatory. Never open a pressure vessel without verifying zero pressure on gauges.
- **Chemical handling**: Antiscalants, acids (sulfuric, citric), and bases (sodium hydroxide) require PPE — chemical goggles, gloves, and aprons. Sulfuric acid dosing systems must have secondary containment.
- **Brine discharge**: Hypersaline discharge harms marine ecosystems. Discharge monitoring must confirm salinity within regulatory limits. Brine may also contain pretreatment chemicals (antiscalants, cleaning agents).
- **Electrical safety**: ED stacks operate at 100-600 V DC. RO and MSF plants have large motor control centers. Lockout/tagout procedures for all maintenance.

## Quality Control

- **Conductivity monitoring**: Continuous online conductivity meters on permeate/product water. Alarm at >500 µS/cm for drinking water. Calibrate weekly with standard solutions (1,413 µS/cm at 25°C).
- **SDI (Silt Density Index)**: Measure feedwater quality before RO. SDI <3 required for reliable operation. SDI >5 indicates inadequate pretreatment.
- **Membrane integrity testing**: Vacuum decay test or conductivity profiling every 6 months. Identifies individual degraded elements.
- **Pressure drop monitoring**: Track feed-to-concentrate pressure drop across each stage. Increasing pressure drop indicates fouling.
- **Brine salinity**: Monitor concentrate TDS to verify recovery rate is within design parameters. Excessive concentration increases scaling risk.

## See Also

- [Basic Water Treatment](basic-treatment.md) — pretreatment foundation and disinfection methods
- [SEM Tech Water Treatment](sem-tech-water-treatment.md) — advanced membrane and purification technologies
- [Chemistry: Electrodialysis](../chemistry/sem-tech-electrodialysis.md) — ion-exchange membrane principles
- [Polymers](../polymers/index.md) — membrane materials and production
- [Energy: Electricity](../energy/electricity.md) — power supply for desalination
- [Water Distribution](distribution.md) — post-desalination water delivery


---
*Part of the [Bootciv Tech Tree](../index.md) • [Water](./index.md) • [All Domains](../index.md)*
