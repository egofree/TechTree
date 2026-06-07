# Rare Earth and Specialty Elements

> **Node ID**: metals.rare-earths
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Electronics`](electronics.md), [`Photolithography & IC Fabrication`](photolithography.md)
> **Enables**: [`Mining Engineering & Extractive Metallurgy`](mining.md)
> **Timeline**: Years 30-50
> **Outputs**: gallium, indium, germanium, neodymium, rare-earth-oxides
> **Critical**: No

## Overview

Extraction and separation of rare earth elements (REE) and specialty metals from mineral ores through acid leaching, solvent extraction, and ion exchange. The target elements include the fifteen lanthanides plus scandium and yttrium, along with specialty metals like gallium, indium, and germanium. These elements are essential for permanent magnets (neodymium, dysprosium), phosphors (europium, terbium, yttrium), laser materials (neodymium, erbium), battery electrodes (lanthanum, cerium), semiconductors (gallium), transparent conductors (indium), and fiber optics (germanium).

The central challenge in rare earth processing is separation. The lanthanide elements have nearly identical ionic radii that decrease gradually from lanthanum to lutetium (the lanthanide contraction). Their chemistry is so similar that separating adjacent lanthanides requires hundreds of sequential extraction stages. A full separation plant processing bastnasite or monazite ore into individual rare earth oxides may run 50 to 100 stages of counter-current solvent extraction.

Primary outputs: `gallium`, `indium`, `germanium`, `neodymium`, `rare-earth-oxides`.

## Prerequisites

### Materials

- REE-bearing ore concentrate (bastnasite, monazite, xenotime, or ion-adsorption clay)
- Hydrochloric acid or sulfuric acid for leaching
- Organophosphorus extractants (D2EHPA, PC-88A, or Cyanex 272) diluted in kerosene
- Oxalic acid or ammonium bicarbonate for precipitation
- Kerosene or other diluent for the organic phase
- Hydrogen peroxide and other oxidizing/reducing agents for selective valence control (cerium oxidation, europium reduction)
- Ion exchange resins for final purification stages

### Equipment

- [Electronics](electronics.md) — material dependency
- [Photolithography & IC Fabrication](photolithography.md) — material dependency
- Crushing and grinding circuit (jaw crusher, ball mill) for ore comminution
- Gravity and magnetic separation equipment (for pre-concentration of REE minerals)
- Leaching tanks (steel or rubber-lined, with agitation and heating)
- Counter-current solvent extraction cascade: mixer-settlers or pulsed columns (50-100 stages for full separation)
- Precipitation tanks with agitation, heating, and pH control
- Calcination furnace (rotary kiln or muffle furnace) for converting precipitates to oxides
- Ion exchange columns for high-purity final polishing
- Analytical equipment: XRF, ICP-OES, or ICP-MS for trace impurity measurement
- Fume scrubbers and off-gas treatment for acid vapor and radioactive dust

### Knowledge

- REE mineralogy and ore types: bastnasite (light REE carbonate-fluoride), monazite (light REE phosphate with thorium), xenotime (heavy REE phosphate), ion-adsorption clays (easily leached, heavy REE enriched)
- Acid leaching chemistry: hydrochloric acid leaching of bastnasite, sulfuric acid baking followed by water leaching, caustic cracking of monazite
- Solvent extraction fundamentals: distribution coefficients, separation factors, pH control for selectivity, counter-current cascade design
- Valence control for selective separation: cerium (oxidize Ce³⁺ to Ce⁴⁺ for early removal), europium (reduce Eu³⁺ to Eu²⁺ for separation from other REE)
- Precipitation chemistry: oxalate precipitation, double sulfate precipitation, hydroxide precipitation
- Radioactive material handling: thorium and uranium management in monazite processing

### Infrastructure

- Ore receiving, storage, and comminution area with dust collection
- Acid leaching area with ventilation, acid-resistant flooring, and drainage
- Solvent extraction cascade: long rows of mixer-settlers with piping for organic and aqueous phases, pH adjustment stations between stage groups
- Precipitation, filtration, and calcination area
- Analytical laboratory with ICP-OES or ICP-MS capability for trace impurity measurement down to ppm and sub-ppm levels
- Radioactive waste storage and handling facility (for monazite processing, thorium-bearing waste requires licensed disposal)
- Fume scrubbing and off-gas treatment for acid vapors and solvent vapors
- Water treatment and recycling system (the process uses large volumes of water)
- Rare earth metal reduction furnaces (for converting oxides to metals: electrolytic cells for light REE, reduction furnaces for heavy REE)

## Process Description

### Step-by-Step Procedure

1. Mine and crush the REE-bearing ore. Grind to a particle size that liberates the REE minerals (typically below 75 microns).
2. Concentrate the REE minerals by gravity separation, magnetic separation, or flotation. The goal is to upgrade the ore from a few percent total REE to a concentrate suitable for leaching (30-70% REO depending on the mineral).
3. Leach the concentrate. For bastnasite: digest with concentrated hydrochloric acid at elevated temperature. The REE dissolve as chlorides; insoluble residue (barite, fluorite, silica) is filtered off. For monazite: either hot concentrated sulfuric acid leaching or caustic cracking with NaOH followed by acid dissolution of the REE hydroxides.
4. Remove impurities from the leach solution. Adjust pH to precipitate thorium (from monazite), iron, and other non-REE impurities. Filter. The clarified solution contains mixed REE in acid solution.
5. Begin the solvent extraction cascade. The aqueous REE solution enters a long series of mixer-settlers. In each stage, the aqueous solution is mixed with an organic phase containing the extractant (e.g., PC-88A in kerosene). REE ions partition between the aqueous and organic phases according to their distribution coefficients, which vary with pH. By controlling pH precisely at each stage and running the cascade counter-current, individual REE are separated step by step.
6. Use valence control for certain elements. Oxidize cerium to Ce⁴⁺ (which extracts differently from the trivalent REE) for early removal. Reduce europium to Eu²⁺ (which does not extract with the trivalent REE) for selective separation.
7. Collect the separated REE-bearing aqueous streams from the cascade. Precipitate each individual REE as an oxalate or double salt by adding oxalic acid or ammonium bicarbonate.
8. Filter the precipitate and calcine at 800-1000°C to convert to the rare earth oxide (REO). The calcination temperature and time affect the oxide properties (particle size, surface area).
9. For the highest purity requirements (electronics grade), pass the solution through ion exchange columns as a final polishing step before precipitation.

10. Convert selected rare earth oxides to metals by molten salt electrolysis (for light REE like Nd, La, Ce) or by metallothermic reduction with calcium or lanthanum (for heavy REE). The metal production step is separate from the oxide separation plant and requires different equipment.

### Solvent Extraction Detail

The solvent extraction cascade is the heart of a REE separation plant. A typical cascade for separating all the light REE from bastnasite might use 60-80 mixer-settler stages divided into several groups. Each group separates one or two adjacent REE from the rest.

In a mixer-settler stage, the aqueous (REE in acid solution) and organic (extractant in kerosene) phases are pumped into a mixing chamber where they are agitated together. REE ions transfer from the aqueous phase into the organic phase according to the distribution coefficient, which depends on the specific REE, the extractant, the pH, and the temperature. The mixture flows into a settling chamber where the two phases separate by gravity. The heavier aqueous phase settles to the bottom, and the lighter organic phase floats on top.

In a counter-current cascade, fresh aqueous feed enters one end of the cascade and fresh organic solvent enters the other end. They flow in opposite directions through the series of stages. The separation factor between adjacent lanthanides for typical extractants is small (1.2-2.5), so many stages are needed. pH is adjusted at several points along the cascade to tune the selectivity for the group of REE being separated in that section.

### Process Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| Leaching temperature (HCl) | 60-90°C | Higher temperature increases dissolution rate |
| Leaching acid concentration | 4-6 M HCl (bastnasite) | Concentrated acid needed for complete dissolution |
| Extraction pH | 1.0-5.0 (varies by stage group) | pH control is the primary tool for selectivity between adjacent REE |
| O/A (organic/aqueous) ratio | 0.5-3.0 | Controls loading of REE in the organic phase |
| Number of extraction stages | 50-100 (total cascade) | More stages give sharper separation between adjacent REE |
| Mixer residence time | 2-5 minutes per stage | Adequate mixing for phase equilibrium |
| Settler area | Sized for phase disengagement | Prevents organic entrainment in aqueous raffinate |
| Precipitation pH (oxalate) | 1.5-2.5 | Oxalic acid dose must be controlled to avoid co-precipitation of impurities |
| Calcination temperature | 800-1000°C | Converts oxalate to oxide; higher temperature gives denser oxide |
| REE metal reduction temperature | 1000-1100°C (molten salt electrolysis) | For Nd, La, Ce, Pr. Higher temperatures needed for heavy REE |
| Nd electrolysis current density | 3-10 A/cm² | Typical for NdF₃-LiF molten salt electrolysis |

The total process from ore to separated individual REO takes days to weeks, with the solvent extraction cascade operating continuously. The cascade cannot be easily stopped and restarted without losing separation performance, so continuous operation and steady feed supply are essential.

## Safety Considerations

- **Acid burns**: Hydrochloric acid and sulfuric acid at the concentrations used for leaching cause severe chemical burns. Full acid handling PPE is mandatory in the leaching area.
- **Radioactive materials**: Monazite ore contains thorium (0.1-0.6% ThO₂) and uranium. Thorium and its decay products (radon gas, radium) are radioactive. Handling monazite requires radiation monitoring, controlled areas, respiratory protection for dust, and licensed disposal of radioactive waste. Bastnasite processing has lower radioactive hazard.
- **Solvent vapors**: Kerosene diluent and organophosphorus extractants produce vapors that can cause headaches, dizziness, and long-term health effects with chronic exposure. Ventilation in the solvent extraction area must be adequate.
- **Heavy metal toxicity**: REE compounds are moderately toxic if ingested or inhaled as dust. Cerium and lanthanum oxides are respiratory irritants. Avoid generating dust during precipitation, filtration, and calcination operations.
- **Hydrogen gas**: Acid leaching of REE ores can generate hydrogen gas from the reaction with metallic impurities. Adequate ventilation prevents accumulation.

### Personal Protective Equipment

- Acid-resistant gloves (nitrile or neoprene), rubber apron, face shield, and rubber boots in the leaching area
- Respiratory protection (dust mask minimum, supplied air for monazite processing) when handling dry ore, precipitates, or calcined oxides
- Safety glasses with side shields at all times in the plant
- Radiation dosimeter badge when working with monazite or other thorium-bearing materials
- Chemical-resistant gloves when handling extractants and organic solvents

### Emergency Procedures

- For acid contact: flush with water for at least 15 minutes. Remove contaminated clothing. Seek medical attention.
- For solvent exposure: move to fresh air. If breathing is difficult, seek medical attention.
- For radioactive material spill (monazite): evacuate the area, contain the spill, and follow the facility radiation emergency plan. Do not attempt cleanup without proper training and monitoring equipment.
- For hydrogen buildup: evacuate the leaching area, ventilate, and eliminate ignition sources before investigating.

## Quality Control

### Acceptance Criteria

- **Individual REO (rare earth oxide)**: Purity >99.9% for most applications. Electronics and phosphor grades may require >99.99% or >99.999%. Trace impurity limits for specific elements depend on the application.
- **Neodymium oxide (Nd₂O₃)**: Minimum 99.9% for magnet production. Praseodymium and cerium are the most difficult adjacent elements to separate from neodymium.
- **Gallium**: Typically recovered as a byproduct of aluminum or zinc processing, not from REE ores. Requires separate purification (fractional crystallization or electrolysis) to reach semiconductor grade (>99.9999%).
- **Indium**: Recovered from zinc smelter residues. Requires >99.99% for ITO (indium tin oxide) sputtering targets.
- **Germanium**: Recovered from zinc smelter residues or coal fly ash. Requires >99.999% for fiber optics and infrared optics.

### Testing Methods

- **ICP-OES or ICP-MS**: The primary analytical tool for measuring individual REE concentrations and trace impurities in both process streams and final products. Can measure down to sub-ppm levels. Essential for monitoring the solvent extraction cascade and certifying product purity.
- **XRF (X-ray fluorescence)**: Used for rapid ore grade analysis and process stream monitoring. Less sensitive than ICP but faster and non-destructive.
- **Loss on ignition (LOI)**: Measures the residual carbonate or hydroxide content in calcined oxide. High LOI indicates incomplete calcination.
- **Particle size analysis**: The oxide particle size affects downstream processing (magnet powder, phosphor synthesis). Measured by laser diffraction or sedimentation.
- **Radiation survey**: Mandatory for monazite processing areas. Monitor thorium and radium levels in process streams, waste, and workplace air.

### Sampling Protocol

- Sample the solvent extraction cascade aqueous and organic streams at regular intervals (every 4-8 hours) to monitor separation performance
- Analyze each REO product batch for purity by ICP-MS before certification
- Monitor thorium and uranium levels in process streams and waste when processing monazite
- Track extractant concentration and degradation in the organic phase weekly
- Sample and analyze leach residue for REE recovery efficiency

## Scaling Notes

- **Bench scale**: Beaker leaching of ore concentrate in a fume hood. Separatory funnel solvent extraction with a few stages. Produces grams of mixed or partially separated REO. Useful for ore characterization and extractant screening.
- **Pilot scale**: Small leaching tank. 10-20 mixer-settler stages. Produces kilograms of separated REO. Validates cascade design and pH control strategy before building a full plant.
- **Production scale**: Full leaching circuit. 50-100 mixer-settler stages in a cascade. Continuous operation. Produces tonnes of individual REO per year. The cascade alone may span hundreds of meters of equipment.

Key scaling challenges: the solvent extraction cascade is the dominant cost and complexity element. More stages mean better separation but more equipment, more floor space, and more organic solvent inventory. The extractant (PC-88A, D2EHPA, etc.) is expensive and degrades over time. Precise pH control at every stage group is essential; small pH deviations shift distribution coefficients and degrade separation performance. Processing monazite adds radioactive waste management costs that can dominate the economics of a small-scale operation.

The extraction chemicals themselves present logistical challenges. Organophosphorus extractants like D2EHPA and PC-88A are specialty chemicals that must be synthesized or sourced. At bootstrap scale, producing these extractants may be as difficult as building the separation plant itself. This is one reason why rare earth processing appears late in the technology timeline.

Neodymium metal production is worth special attention because of its use in NdFeB permanent magnets. The oxide (Nd₂O₃) is reduced to metal by molten salt electrolysis in a NdF₃-LiF bath at ~1050°C. The neodymium metal collects as a liquid pool at the bottom of the electrolytic cell and is periodically tapped. The metal is reactive and must be handled under inert atmosphere to prevent oxidation.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Poor separation between adjacent REE | pH drift in the extraction cascade; degraded extractant | Check and adjust pH at each stage group; assay extractant and replace if degraded |
| Emulsion formation in mixer-settlers | Fine solids entrainment; extractant degradation products | Filter feed solutions; replace degraded extractant; reduce agitation intensity |
| Low REE recovery from leaching | Incomplete dissolution; incorrect acid strength or temperature | Increase acid concentration, temperature, or leaching time; grind ore finer |
| Impurity co-extraction (Fe, Al, Th) | pH too high in early extraction stages | Lower pH in the scrub section; add impurity scrubbing stages |
| Crmudge (third phase formation) | High REE loading in organic phase; wrong O/A ratio | Reduce organic loading; adjust O/A ratio; add modifier (TBP or decanol) to organic phase |
| Incomplete calcination | Temperature too low or residence time too short | Raise calcination temperature; increase kiln residence time |
| Radioactive dust in monazite area | Inadequate dust collection during dry handling | Improve dust collection; use wet handling methods; increase respiratory protection |

## Variations and Alternatives

- **Monazite processing**: Higher thorium content means higher radioactive hazard but monazite is abundant in heavy mineral sand deposits. Caustic cracking (NaOH fusion) followed by acid dissolution is the standard route.
- **Bastnasite processing**: Lower radioactivity (no significant thorium). Hydrochloric acid leaching is straightforward. The Mountain Pass and Bayan Obo deposits are bastnasite-type.
- **Ion-adsorption clays (South China type)**: These weathered granitic clays contain REE adsorbed on clay mineral surfaces. They are easily leached with dilute ammonium sulfate solution at ambient temperature, avoiding the aggressive acid leaching needed for hard rock ores. However, they are geographically limited.
- **Ion exchange chromatography**: Used for the final purification of individual REE to very high purity (>99.999%). Slow and batch-mode, but achieves separations that solvent extraction cannot. Uses chelating resins with alpha-hydroxyisobutyric acid or similar eluents.
- **Byproduct recovery of gallium and indium**: These are not extracted from REE ores. Gallium comes from aluminum production (bauxite processing). Indium comes from zinc smelter residues. Germanium comes from zinc residues or coal fly ash. Each requires its own extraction and purification process.

### Material Handling

Store REE oxides in sealed, labeled containers to prevent moisture absorption and cross-contamination between different REE products. Keep acid and solvent inventories in dedicated chemical storage areas with secondary containment. Monazite ore and thorium-bearing intermediates require controlled storage with radiation monitoring and restricted access. Waste streams (acidic raffinate, spent solvent, radioactive tailings) must be segregated and managed according to their hazard classification.

## References

- [Metals](metals.md) — parent capability
- [Metals Domain](./index.md) — domain overview and related capabilities
- [Electronics](electronics.md) — upstream dependency (material)
- [Photolithography & IC Fabrication](photolithography.md) — upstream dependency (material)
- [Mining Engineering & Extractive Metallurgy](mining.md) — downstream capability

---
*Part of the [Bootciv Tech Tree](../index.md) · [Metals](./index.md) · [All Domains](../index.md)*