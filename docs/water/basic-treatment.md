# Basic Water Treatment

> **Node**: `water.basic-treatment`
> **Parent**: [Water](index.md)
> **Timeline**: Years 5-25
> **Outputs**: potable_water, filtered_water

Purifying raw water for safe human consumption. Waterborne diseases
(cholera, typhoid, dysentery, giardiasis) are among the greatest
killers in all pre-industrial civilizations. Simple treatment methods
dramatically reduce disease burden and are achievable with minimal
technology.

## The Treatment Spectrum

Water treatment operates on a spectrum from coarse to fine:

1. **Settling** — remove large particles by gravity
2. **Filtration** — remove smaller particles and microorganisms
3. **Disinfection** — kill or inactivate remaining pathogens

Each stage is valuable on its own; the combination provides safe
drinking water.

## Settling and Clarification

The simplest treatment: let water sit still so particles sink.

- **Plain sedimentation**: Fill a tank or basin, wait 2-4 hours. Removes
  particles larger than 10-20 microns (sand, silt, some bacteria).
- **Upflow clarifiers**: Water flows upward through a settling zone.
  Continuous operation with sludge removal from the bottom.
- **Pre-sedimentation basins**: Large basins (4-12 hour residence time)
  placed before filtration. Reduce filter loading by 50-90%.

## Slow Sand Filtration

The most important low-technology water treatment method. Developed in
Scotland in 1804, slow sand filtration produces safe drinking water with
no chemicals and minimal maintenance.

### Design Parameters

- **Filter bed depth**: 0.6-1.5 meters of fine sand
- **Sand effective size**: 0.15-0.35 mm
- **Sand uniformity coefficient**: 1.5-3.0
- **Flow rate**: 0.1-0.4 meters per hour (hydraulic loading)
- **Area required**: roughly 1 m² per 50-200 people served

### Biological Layer (Schmutzdecke)

The critical active component forms on top of the sand bed over 1-4
weeks of operation:

- A biological community of bacteria, protozoa, and algae develops
- This layer traps and digests pathogens and organic matter
- Removes 95-99.9% of bacteria, 99-99.99% of viruses, and nearly all
  protozoan parasites
- **Never let the filter dry out** — the biological layer dies

### Construction

- **Tank**: Concrete, ferrocement, stone, or brick with waterproof
  lining. Open top, covered to prevent algae growth.
- **Gravel underdrain**: 15-30 cm graded gravel layer supports sand and
  allows filtered water collection. Perforated drainage pipes at bottom.
- **Sand filling**: Place sand in 15 cm layers, wash each layer to
  remove fines. Top level should be 5-10 cm above the sand surface for
  water depth.
- **Inlet and outlet**: Simple overflow weirs. Maintain 5-10 cm water
  above sand surface at all times.

### Maintenance

- When flow rate drops below design minimum: drain water, scrape 1-2 cm
  of sand from the top, refill and restart. The biological layer
  re-establishes in 1-3 days.
- Scraped sand can be washed and stockpiled for eventual bed
  replacement.
- Full bed replacement needed every 5-10 years.

## Rapid Sand Filtration (Later Development)

Higher flow rates requiring chemical coagulation as pretreatment.

- Flow rate: 5-15 m/hour (50× faster than slow sand)
- Requires aluminum sulfate (alum) or ferric chloride coagulant
- Backwash with air and water to clean filter bed
- Removes turbidity effectively but less biological removal than slow
  sand
- Depends on chemistry capability for coagulant production

## Boiling

The oldest and most universal disinfection method.

- **Effectiveness**: 99.9999% pathogen kill if water reaches a rolling
  boil. Kills bacteria, viruses, and protozoan cysts.
- **Time**: Boil for 1 minute at sea level; 3 minutes above 2,000
  meters elevation (lower boiling point at altitude).
- **Fuel cost**: Boiling 1 liter of water requires roughly 0.1-0.3 kg
  of wood fuel. Significant fuel burden at household scale.
- **Limitation**: Does not remove chemical contaminants, turbidity, or
  heavy metals. Recontamination is a risk if boiled water is stored in
  dirty containers.

## Solar Disinfection (SODIS)

UV radiation and thermal energy from sunlight inactivate pathogens.

- **Method**: Fill clear PET or glass bottles with water, expose to full
  sun for 6+ hours (or 2 days if cloudy).
- **Mechanism**: UV-A radiation damages pathogen DNA; thermal effects
  synergize above 45°C.
- **Limitations**: Requires clear bottles. Turbid water (>30 NTU) must
  be pre-filtered. Ineffective on very cloudy days.
- **Advantage**: Zero fuel cost, minimal technology.

## Chlorination

The most widely used disinfection method worldwide since the early 1900s.

- **Chlorine sources**: Calcium hypochlorite (bleaching powder), sodium
  hypochlorite (liquid bleach), or chlorine gas (industrial).
- **Dosage**: 1-5 mg/L free chlorine. Target 0.5 mg/L residual after
  30 minutes contact time.
- **Contact time**: Minimum 30 minutes at pH <8. Higher pH requires
  longer contact or higher dose.
- **Production**: Electrolysis of brine produces chlorine gas and sodium
  hypochlorite. Requires electricity and salt.
- **Safety**: Chlorine gas is toxic (IDLH 10 ppm). Handle with
  ventilation and gas masks. Sodium hypochlorite solution degrades over
  time; store cool and dark.

## Simple Household Filters

Between boiling nothing and building a slow sand filter, several
intermediate methods exist:

- **Ceramic candle filters**: Porous ceramic elements (pore size 0.5-5
  microns) remove bacteria. Silver-impregnated ceramic provides
  additional antimicrobial action. Flow rate: 1-4 L/hour.
- **Cloth filtration**: Folded cotton cloth removes larger pathogens
  (guinea worm, some bacteria). 4-8 layers of sarif cloth reduce
  cholera bacteria by 50-99%.
- **Charcoal filtration**: Granular activated charcoal removes taste,
  odor, and some organic chemicals. Does NOT reliably remove pathogens.

## Water Quality Testing

Simple field tests verify treatment effectiveness:

- **Turbidity tube**: Measure water clarity. Treated water should be
  <5 NTU (appear clear).
- **Chlorine residual test**: Colorimetric DPD test kit. Verify 0.2-0.5
  mg/L free chlorine residual.
- **Hydrogen sulfide test**: Simple presence/absence test for fecal
  contamination. Water turns black if contaminated.

## Dependencies

- [Water Procurement](procurement.md) — raw water must be collected
  before treatment
- [Ceramics](../ceramics/index.md) — ceramic filter elements, tanks
- [Chemistry](../chemistry/index.md) — chlorination chemicals,
  coagulants for rapid filtration

## Enables

- [Desalination](sem-tech-water-treatment.md) — treatment knowledge
  underpins advanced purification
- [Health: Sanitation](../health/sanitation.md) — clean water is
  fundamental to sanitation

[↑ Back to Water Infrastructure](index.md)
