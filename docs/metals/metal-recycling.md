# Metal Scrap Recycling

> **Node ID**: metals.metal-recycling
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`Iron & Steel Production`](iron-steel.md), [`Steelmaking`](steelmaking.md), [`Mining Extraction`](../mining/extraction.md), [`Energy`](../energy/index.md)
> **Enables**: [`Metals`](./index.md), [`Construction`](../construction/index.md), [`Electronics`](../electronics/index.md)
> **Timeline**: Years 15-50+
> **Outputs**: recycled_steel, recycled_copper, recycled_aluminum, secondary_metal_feedstock
> **Critical**: No — reduces primary ore demand but does not unlock new capabilities

Metal scrap recycling converts end-of-life metal products, manufacturing offcuts, and demolition debris back into usable metal feedstock through sorting, preparation, and remelting. Unlike primary metal production from ore, recycling requires 5–95% less energy depending on the metal: recycled aluminum uses 5% of primary energy, recycled steel uses 25–35%, and recycled copper uses 15–20%.

Recycling does not replace primary metal production — it supplements it. In a bootstrapping civilization, scrap recycling becomes significant once enough metal has been produced and discarded to create viable collection streams. This typically begins 20–30 years after iron production starts, when the first generation of tools, structures, and machines reaches end-of-life.

The capability spans four metal groups with different recycling economics: ferrous scrap (iron and steel, highest volume), aluminum scrap (highest energy savings), copper scrap (highest value), and specialty metals (titanium, nickel alloys, precious metals). Each group has distinct sorting requirements, contamination tolerances, and remelting processes.

This document covers the recovery side: collecting, sorting, preparing, and remelting scrap. It does not cover waste disposal of non-recyclable residues — see [Waste Management](../ehs/waste-management.md) for that.

## Prerequisites

- [Iron & Steel Production](iron-steel.md) — primary iron smelting and steelmaking processes
- [Steelmaking](steelmaking.md) — EAF and BOF steelmaking details
- [Mining Extraction](../mining/extraction.md) — ore extraction (the upstream process recycling reduces)
- [Energy](../energy/engine.md) — power supply for electric furnaces

## Materials

| Material | Specification | Source |
|----------|--------------|--------|
| Metal scrap | Sorted by alloy family; ferrous, Al, Cu, mixed | Collection from demolition, manufacturing offcuts, end-of-life products |
| Flux (limestone, fluorspar) | 2–5% of charge weight | [Mining](../mining/processing.md) |
| Refractories | Furnace linings rated for target temperature | [Refractories](../chemistry/refractories.md) |
| Fuel or electricity | 300–700 kWh/tonne for EAF steel; 5–20 kWh/kg for Al remelt | [Energy](../energy/engine.md) |

## Tools & Equipment

| Equipment | Purpose | Source |
|-----------|---------|--------|
| Magnetic separator | Ferrous/non-ferrous separation | [Mining Processing](../mining/processing.md) |
| Shredder or shear | Size reduction of bulky scrap | [Machine Tools](../machine-tools/index.md) |
| Electric arc furnace or cupola | Remelting steel scrap | [Steelmaking](steelmaking.md) |
| Crucible furnace or reverberatory furnace | Non-ferrous remelting | [Copper & Bronze](copper-bronze.md) |
| Spectrometer or spark tester | Alloy identification | [Measurement](../measurement/index.md) |

## Knowledge

- Ability to distinguish metal families by visual inspection, spark testing, magnetic response, and weight
- Understanding of alloy contamination: a single piece of leaded steel in a stainless steel heat ruins the entire batch
- Furnace operation and temperature control for the target metal group


## BOM: Steel Scrap Recycling via EAF (per tonne of recycled steel)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Steel scrap (sorted) | 1,050–1,100 kg | Collection streams | Direct reduced iron (DRI) supplement at 10–30% |
| Lime (CaO) | 30–50 kg | [Lime Production](../ceramics/lime.md) | Limestone (requires more heat) |
| Carbon (coal/coke) | 5–15 kg | [Energy Fuels](../energy/index.md) | Electrode carbon |
| Electrodes (graphite) | 2–5 kg | [Chemistry](../chemistry/index.md) | Søderberg electrodes (self-baking) |
| Electricity | 350–500 kWh | [Power Generation](../energy/index.md) | No alternative for EAF |
| Oxygen | 10–25 m³ | [Air Separation](../chemistry/air-separation.md) | Air lancing (less efficient) |

## BOM: Aluminum Scrap Recycling (per tonne of recycled aluminum)

| Material | Quantity | Source | Alternatives |
|----------|----------|--------|-------------|
| Aluminum scrap (sorted) | 1,050–1,100 kg | Collection, manufacturing offcuts | Primary aluminum (energy cost 50× higher) |
| Salt flux (NaCl/KCl) | 10–30 kg | [Alkalis](../chemistry/alkalis.md) | Cryolite (if available) |
| Chlorine gas | 0.5–2.0 kg | [Electrolysis](../chemistry/electrolysis.md) | Nitrogen degassing (less effective) |
| Natural gas or electricity | 5–20 kWh | [Energy](../energy/engine.md) | Oil firing |
| Nitrogen or argon cover gas | 1–5 m³ | [Air Separation](../chemistry/air-separation.md) | SO₂ cover gas (toxic) |


## Ferrous Scrap Recycling (EAF Route)

1. **Collect and sort scrap.** Receive scrap from demolition sites, manufacturing offcuts, and end-of-life products. Sort into categories: heavy melting steel (HMS), plate and structural, shredded scrap, turnings, and baled tin plate. Remove obvious contaminants: rubber, plastic, concrete, non-ferrous metals.

2. **Shred and prepare.** Feed bulky scrap through a shredder reducing pieces to fist-sized fragments (50–150 mm). Pass shredded material through a magnetic separator to recover ferrous fragments from non-metallic waste. Density separation removes light contaminants (plastic, wood, fabric).

3. **Charge the EAF.** Load 50–100 tonnes of prepared scrap into the electric arc furnace using a charging basket. Add 3–5% lime flux on top of the charge. Lower graphite electrodes.

4. **Melt under arc.** Strike the arc at low power for 2–3 minutes (bore-in phase) to establish a molten pool. Ramp to full power (40–80 MW) and melt the charge over 30–45 minutes. Add oxygen lancing to assist melting and decarburize the bath. Target tap temperature: 1620–1650°C.

5. **Refine in ladle.** Transfer molten steel to a ladle furnace. Add ferro-alloys to hit target chemistry (Mn, Si, C). Desulfurize with CaO/CaC₂ if needed. Stir with argon or nitrogen to homogenize. Hold 10–20 minutes.

6. **Cast.** Continuous cast into billets, slabs, or blooms; or pour into ingot molds. Yield: 88–94% of input scrap weight becomes usable steel product.

## Aluminum Scrap Recycling

1. **Sort by alloy.** Separate cast alloys (Al-Si) from wrought alloys (1xxx, 3xxx, 5xxx, 6xxx series). Remove iron attachments, plastic coatings, and other metals. Test uncertain pieces with a portable spectrometer.

2. **Pre-clean and decoat.** Delacquered painted/scrap (beverage cans, coated sheet) in a rotary kiln at 400–500°C to burn off organic coatings. Remove 3–8% weight loss as volatiles.

3. **Charge side-well furnace.** Load scrap into the side-well or charging well of a reverberatory furnace. Add salt flux (NaCl:KCl 70:30) at 1–3% of charge weight to cover the melt surface and prevent oxidation.

4. **Melt at 680–750°C.** Submerge scrap below the molten metal surface using a mechanical stirrer or manual pushing. Avoid excessive turbulence that generates dross (aluminum oxide). Melt rate: 2–5 tonnes/hour for a 20-tonne furnace.

5. **Degas and flux.** Inject chlorine or chlorine-nitrogen mixture (0.1–0.3 kg Cl₂/tonne Al) through a rotary degasser to remove dissolved hydrogen and suspended oxides. Skim dross (5–10% of charge weight).

6. **Cast.** Cast into ingots, sows, or billets. Yield: 85–95% depending on scrap cleanliness.

## Copper Scrap Recycling

1. **Sort and grade.** Classify copper scrap: No. 1 copper (clean, >99% Cu, bare bright wire), No. 2 copper (≥94% Cu, some oxidation/solder), light copper (88–92% Cu), and refinery brass (mixed Cu-Zn). Separate by visual inspection, file testing, and density.

2. **Shred and densify.** Shred wire and cable to liberate copper from insulation. Air-table separation or dense media separation removes insulation and other metals. Bales of thin scrap are compacted for easier furnace charging.

3. **Fire refine.** Charge anode furnace or reverberatory furnace with sorted copper scrap. Melt at 1150–1200°C under a reducing atmosphere. Oxidize impurities by air injection, then poling with green wood (reduces Cu₂O back to Cu). Cast into anodes for electrolytic refining, or directly into shapes if purity is adequate.

4. **Electrolytic refine (if required).** For semiconductor-grade or electrical-grade copper, dissolve anodes in CuSO₄/H₂SO₄ electrolyte and plate onto starter cathodes at 200–300 A/m². See [Copper & Bronze](copper-bronze.md).


## Energy Requirements by Metal

| Metal | Primary Energy (from ore) | Recycling Energy | Energy Savings | CO₂ Reduction |
|-------|--------------------------|-------------------|----------------|---------------|
| Steel | 20–25 GJ/tonne (BF-BOF) | 6–9 GJ/tonne (EAF) | 60–75% | 55–70% |
| Aluminum | 170–200 GJ/tonne (Hall-Héroult) | 8–15 GJ/tonne (remelt) | 92–95% | 90–95% |
| Copper | 30–50 GJ/tonne (mining + smelting) | 6–10 GJ/tonne (remelt) | 75–85% | 65–80% |
| Zinc | 35–45 GJ/tonne | 10–15 GJ/tonne | 65–75% | 60–70% |
| Lead | 25–35 GJ/tonne | 5–10 GJ/tonne | 70–85% | 65–80% |

## Steel Scrap Categories and Yields

| Scrap Grade | Description | Typical Analysis | EAF Yield |
|-------------|-------------|-----------------|-----------|
| HMS 1 | Heavy melting steel, >6mm thick, clean | Fe >98%, low residual | 92–96% |
| HMS 2 | Heavy melting, includes galvanized | Fe >96%, Zn coating | 88–92% |
| Shredded | Fragmentized auto scrap | Fe 95–97%, mixed residuals | 88–93% |
| Turnings | Machine shop chips and borings | Fe 90–95%, oil contamination | 80–88% |
| Baled tin plate | Compacted food cans | Fe 93–96%, Sn 0.3–0.5% | 85–90% |

## Aluminum Scrap Recycling Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Melt temperature | 680–750°C | Well below primary smelting (960°C cell temp) |
| Salt flux ratio | 1–3% of charge weight | NaCl:KCl 70:30 eutectic |
| Dross generation | 5–10% of charge | Aluminum oxide + entrained metal |
| Hydrogen solubility | 0.2–0.5 mL/100g Al at melt temp | Must be reduced to <0.1 mL/100g for casting |
| Chlorine treatment | 0.1–0.3 kg Cl₂/tonne Al | Removes H₂ and Mg; environmental controls required |
| Casting yield | 85–95% | Depends on scrap cleanliness and alloy type |

## Scaling Notes

**Minimum viable scale**: A single crucible furnace remelting 50–200 kg of copper or aluminum scrap per batch requires no infrastructure beyond basic furnace tools. This is the bootstrap entry point — any settlement with metal production capability can recycle.

**Small industrial scale** (1–10 tonnes/day): A small EAF (5–15 tonnes capacity) or cupola furnace can process local steel scrap. Requires 3-phase electrical supply of 5–15 MW or coke supply for cupola operation. Sorting is manual.

**Full industrial scale** (100–1000+ tonnes/day): Modern EAF mini-mills process 500,000–2,000,000 tonnes/year of steel scrap. Automated shredding, magnetic separation, eddy-current separation, and X-ray fluorescence sorting replace manual sorting. Shredder motors: 2,000–10,000 HP.

**Scale breakpoints**: The critical threshold is not technology but **scrap availability**. A community that has produced <1,000 tonnes of steel has insufficient scrap stream to justify a dedicated recycling furnace. Below this threshold, scrap is a supplement to the primary furnace charge (10–30% of total charge weight) rather than the primary feedstock.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| High residual elements (Cu, Sn, Cr) in recycled steel | Contaminated scrap input — mixed grades or non-ferrous contamination | Tighten incoming scrap sorting; dilute with primary iron (DRI or pig iron) to reduce residuals below specification |
| Excessive dross in aluminum remelting | Over-stirring, high melt temperature, thin scrap (high surface area) | Reduce melt temp to 700°C; submerge scrap gently; use salt flux cover; avoid turbulence |
| Porosity in cast recycled aluminum | Dissolved hydrogen >0.1 mL/100g Al | Degas with Cl₂/N₂ mixture; ensure scrap is dry and oil-free before charging |
| Low yield in copper recycling (heavy oxidation) | Excessive air exposure during melting, high superheat | Use charcoal cover on melt; reduce superheat to minimum; work quickly |
| Explosive eruptions during charging | Wet or oily scrap in hot furnace — steam explosions | Pre-dry all scrap; never charge wet material into molten metal; use closed-door charging |
| Off-grade chemistry in recycled steel | Unidentified alloy scrap in charge (e.g., stainless in carbon steel charge) | Pre-sort using spark testing or handheld XRF; maintain segregation of alloy families |
| Contaminated melt (wrong alloy elements) | Mixed scrap not properly sorted | Use spark testing or XRF for incoming sorting; keep alloy families separated; charge only known scrap |
| Low recovery yield (excessive dross) | Oxidation during melting or high contamination | Use protective flux cover; minimize melt time; pre-clean scrap of oil, paint, and coatings |
| Copper contamination in steel scrap | Copper wire mixed in ferrous scrap (copper ennobles steel, causes hot shortness) | Remove all copper wire and motors before charging; use hand-picking or eddy current separation |
| Aluminum melt hydrogen porosity | Moisture on scrap or in furnace atmosphere | Pre-dry scrap; use chlorine or argon degassing; keep melt covered with flux |
| Lead contamination in copper scrap | Solder or bearings mixed in copper charge | Sort out soldered joints and bearings; test melt for Pb content; dilute with clean copper |
| Explosive eruption during charging | Closed containers or wet scrap in molten metal | Puncture all containers before charging; pre-dry scrap; never charge wet material into molten bath |

## Safety

**Steam explosions** are the primary lethal hazard in scrap remelting. Moisture trapped in closed containers, hollow sections, or oil-soaked scrap vaporizes instantly on contact with molten metal (>1500°C for steel, >660°C for aluminum). The resulting steam expansion ratio is 1700:1, producing explosive ejection of molten metal. Prevention: shred all closed containers before charging; pre-heat scrap to >200°C to drive off moisture; never charge sealed containers.

**Zinc fume fever** occurs when galvanized steel scrap is remelted without adequate ventilation. Zinc boils at 907°C — well below steel melting temperature. Inhaled zinc oxide fumes cause flu-like symptoms (chills, fever, muscle aches) 4–8 hours after exposure. Prevention: remove galvanized coatings before melting, or provide local exhaust ventilation with 0.5 m/s capture velocity at the furnace lip. PPE: supplied-air respirator if ventilation is inadequate.

**Magnetic separation hazards**: Powerful permanent magnets and electromagnets used for scrap sorting can crush hands between ferrous pieces. Pinch points on shredder infeed conveyors require guarding. Lock-out/tag-out mandatory for all maintenance.

**Lead exposure**: Lead-acid batteries and leaded solder in mixed scrap produce lead fume and dust. Blood lead monitoring required for workers with regular exposure. PPE: half-face respirator with P100 filters, disposable coveralls, hand washing before eating.


## Steel Scrap Incoming Inspection

| Test | Method | Acceptance Criteria |
|------|--------|-------------------|
| Radiation check | Portal monitor (gamma) | <0.1 μSv/h above background |
| Visible contamination | Visual inspection | <2% non-metallic by weight |
| Radioactive sources | Handheld scintillation probe | No sealed sources detected |
| Heavy metals (Pb, Hg) | Visual check for batteries, switches | None detected |
| Closed containers | Visual + shake test | All hollow sections opened or shredded |

## Recycled Metal Chemistry Verification

| Metal | Key Elements | Method | Typical Spec |
|-------|-------------|--------|-------------|
| Recycled steel | C, Mn, Si, S, P, Cu, Sn, Cr, Ni | OES spectrometer or lab analysis | C ±0.02%, residuals per grade spec |
| Recycled aluminum | Si, Fe, Cu, Mn, Mg, Zn | OES or XRF | Per alloy designation (e.g., 6061, 356) |
| Recycled copper | Cu, Ag, As, Sb, Bi, Pb, O | OES or titration | Cu ≥99.90% for No. 1, ≥99.75% for No. 2 |

## Field Tests (No Lab Required)

- **Spark testing**: Grind steel on an abrasive wheel. Carbon steel sparks are straight with moderate forking. Cast iron sparks are dense with short bursts. Stainless steel produces few sparks (red/orange).
- **Magnetic test**: Ferrous metals are magnetic; austenitic stainless (300-series) is weakly magnetic or non-magnetic; aluminum, copper, brass, and lead are non-magnetic.
- **Density test**: Weigh a piece and measure volume by water displacement. Aluminum ≈2.7 g/cm³, steel ≈7.8, copper ≈8.9, lead ≈11.3.


## Steel Recycling Routes Compared

| Route | Furnace | Scrap Input | Energy Source | Throughput | Capital Cost |
|-------|---------|-------------|---------------|------------|-------------|
| EAF mini-mill | Electric arc | 80–100% scrap | Electricity | 50–200 tonnes/heat | High |
| Cupola | Vertical shaft | 40–70% scrap + pig iron | Coke | 5–30 tonnes/hour | Medium |
| BOF supplement | Basic oxygen | 15–30% scrap with hot metal | Oxygen + heat | 200–350 tonnes/heat | Very high |
| Induction furnace | Coreless induction | 100% scrap | Electricity | 1–30 tonnes/heat | Low–Medium |

## Aluminum Recycling Compared

| Route | Furnace | Scrap Type | Yield | Notes |
|-------|---------|------------|-------|-------|
| Side-well reverberatory | Open-flame | Mixed, sorted | 85–92% | Most common industrial method |
| Crucible remelt | Gas or electric | Clean, known alloy | 90–95% | Small scale, low capital |
| Rotary furnace | Salt-fluxed | Dirty, mixed, dross | 75–88% | Handles high-contamination scrap |

## Historical Context

Bronze Age metalworkers recycled bronze routinely — broken tools and weapons were simply remelted and recast. This was not "recycling" as a concept but the default behavior: metal was too valuable to discard. The modern concept of industrial scrap recycling emerged with the Bessemer and open-hearth processes in the 1860s, when steelmakers began purchasing scrap as a supplementary charge material. The EAF mini-mill revolution (1960s–present) made scrap the primary feedstock for steel production.

## See Also

- [Iron & Steel Production](iron-steel.md) — primary iron smelting and steelmaking processes
- [Steelmaking](steelmaking.md) — EAF and BOF modern steelmaking details
- [Aluminum Production](aluminum.md) — primary aluminum smelting (the process recycling avoids)
- [Copper & Bronze](copper-bronze.md) — primary copper smelting and electrolytic refining
- [Mining Extraction](../mining/extraction.md) — ore extraction (the upstream process recycling reduces)
- [Energy](../energy/engine.md) — power supply for electric furnaces
- [Waste Management](../ehs/waste-management.md) — disposal of non-recyclable residues
- [Chemical Recovery](../chemistry/chemical-recovery.md) — solvent and acid recovery from metal processing
- [Tailings Reprocessing](../mining/tailings-reprocessing.md) — recovering residual metals from mine tailings

[← Back to Metals](index.md)
