# Explosives & Propellants

> **Node ID**: chemistry.explosives
> **Domain**: [Chemistry](./index.md)
> **Dependencies**: [`chemistry.acids`](acids.md), [`chemistry.alkalis`](alkalis.md), [`energy.charcoal`](../energy/charcoal.md)
> **Enables**: [`mining.black-powder`](../mining/black-powder.md), [`metals.finishing`](../metals/finishing.md)
> **Timeline**: Years 5-30+
> **Outputs**: black_powder, nitrocellulose, dynamite, smokeless_powder
> **Critical**: No — explosives accelerate mining and construction but are not prerequisites for core capabilities


A civilization without explosives can dig with hand tools, but it cannot efficiently extract ore from hard rock, cut roads through mountains, or demolish structures larger than a hut. Mining with chisel and hammer advances inches per day in granite. Quarrying building stone without blasting wastes enormous labor. Tunneling through rock with manual tools takes years for modest distances. Explosives compress that work into seconds.

Explosives provide two distinct effects. *Brisance* (shattering force) pulverizes hard rock into fragments. *Heaving force* (gas expansion) moves the broken material aside and heaves soft strata like coal. Different explosives emphasize one or the other, and choosing the right tool for the job determines whether a blast produces useful fragmentation or wasted energy.

The progression runs from black powder, the simplest explosive made from three common materials, through nitration chemistry that yields nitrocellulose, nitroglycerin, and dynamite, to high explosives like TNT and RDX for military and industrial use. At the industrial scale, ANFO dominates mining worldwide because it is cheap, safe to handle, and effective in large boreholes.

The history of explosives mirrors the history of industrial civilization. Black powder enabled the first large-scale mining operations in medieval Europe and China. Dynamite opened the possibility of major earthmoving projects: the transcontinental railroads, the Suez and Panama canals, the deep-level gold mines of South Africa. TNT and RDX enabled the mechanized warfare of the 20th century. ANFO made modern open-pit mining economically viable. At each stage, the availability of a new explosive reshaped what civilization could build, extract, and destroy.

**Explosive classification**:
- **Low explosives** (deflagrating): Burn at subsonic velocities (400-600 m/s). Produce heaving force from gas expansion. Black powder is the archetype. Used as propellants (firearms, rockets) and as blasting agents in soft rock. Confinement increases burn rate and pressure but does not produce a true detonation wave.
- **High explosives** (detonating): Decompose at supersonic velocities (1,500-9,000 m/s). Produce shattering force (brisance) from a shock wave that fractures hard rock and steel. Nitroglycerin, TNT, and RDX are high explosives. Detonation is triggered by a shock wave from a blasting cap or detonator, not by simple ignition.
- **Blasting agents**: Insensitive mixtures that require a booster charge to initiate. ANFO (ammonium nitrate + fuel oil) is the most common. Safer to handle than high explosives but requires a primer (typically a stick of dynamite or a cast booster) to achieve detonation.

**Explosive properties comparison**:

| Explosive | Type | Det. Velocity (m/s) | Density (g/cm³) | Energy (MJ/kg) | Brisance | Primary Use |
|-----------|------|---------------------|------------------|-----------------|----------|-------------|
| Black powder | Low | 400 | 1.0-1.2 | 2.6-3.0 | Very low | Propellant, soft-rock blasting |
| Nitrocellulose | Low (propellant) | 600-800 | 1.0-1.6 | 3.5-4.0 | Low | Smokeless powder, propellant |
| Nitroglycerin | High | 7,700 | 1.59 | 6.4 | Very high | Dynamite component |
| Dynamite (60% NG) | High | 6,000 | 1.3-1.5 | 4.0-4.5 | High | General blasting |
| TNT | High | 6,900 | 1.65 | 4.6 | Moderate | Military, cast charges |
| RDX | High | 8,750 | 1.82 | 5.5 | Very high | Military, plastic explosive |
| ANFO | Blasting agent | 3,000-4,000 | 0.8 | 3.9 | Low | Mining (cheapest per tonne) |
| Detonation cord | High (PETN core) | 6,500-7,000 | ~1.3 | 5.8 | High | Initiation systems, trenching |

## Articles in this capability

![Ampoule with chemical substance Gelsomine (cropped and edited)](../images/chemistry/chemistry_explosives.jpg)

> *Gelsemine*

> *Image: Choij (talk), Public domain*

- [**Black Powder**](black-powder.md) — Black powder manufacture (KNO₃/charcoal/sulfur): separate pulverization, wheel-mill mixing, corning, and granulation. The first explosive, foundational for mining and firearms.
- [**Nitrocellulose & Smokeless Powders**](nitrocellulose.md) — Nitration of cellulose to guncotton and pyroxylin. Manufacture of single-base and double-base smokeless powders. Foundation of modern propellants and early plastics.
- [**Nitroglycerin & Dynamite**](nitroglycerin-dynamite.md) — Synthesis of nitroglycerin from glycerol and mixed acid, absorbed into diatomaceous earth to produce dynamite cartridges. The workhorse blasting explosive from the 1870s onward.
- [**High Explosives (TNT, RDX, ANFO)**](high-explosives.md) — TNT via three-stage toluene nitration, RDX via Woolwich or Bachmann process, ANFO from ammonium nitrate prills and fuel oil. The mature industrial and military explosive palette.
- [**Detonation & Blasting**](detonation-blasting.md) — Blasting caps and initiating systems, detonation physics, blasting design parameters, vibration and airblast control, explosive selection guide, and safety. The systems needed to use explosives safely and effectively.

## Nitration Chemistry Fundamentals

All modern explosives derive from one fundamental reaction: nitration, the substitution of nitro groups (-NO₂) onto organic molecules. The reagent is always mixed acid — a combination of concentrated nitric acid (HNO₃) and concentrated sulfuric acid (H₂SO₄). Sulfuric acid serves as a dehydrating agent, absorbing the water produced by the nitration reaction and driving it to completion. Without sulfuric acid, the water produced would dilute the nitric acid and stop the reaction.

The general nitration reaction: R-H + HNO₃ → R-NO₂ + H₂O (catalyzed by H₂SO₄). The energy stored in the nitro groups is released during detonation as the N-O bonds break and reform into stable N₂ gas (N≡N triple bond, 941 kJ/mol), releasing enormous energy. This is why nitrogen-containing compounds are the basis of virtually all high explosives: the formation of N₂ gas from nitro groups is one of the most exothermic chemical reactions available.

**Nitration hazards** are constant across all explosive production: the reactions are exothermic (heat-producing), and temperature runaway leads to violent decomposition. Every nitrator vessel requires a cooling jacket, continuous temperature monitoring (±2°C), and an emergency dump valve that discharges the batch into a drowning tank (20× volume of cold water). Operators work behind blast shields. The mixed acid itself causes immediate, deep chemical burns on skin contact.

## Prerequisites & Dependencies

Explosive production requires a chemical industry foundation:

| Prerequisite | Purpose | Scale Required |
|-------------|---------|---------------|
| Sulfur mining | Sulfur for black powder (10% by weight) | 100-500 kg/year for village-scale |
| Charcoal production | Fuel component of black powder (15% by weight) | 500-2,000 kg/year for village-scale |
| Saltpeter (KNO₃) production | Oxidizer for black powder (75% by weight) | Niter beds or mining, 2,000+ kg/year |
| Sulfuric acid (contact process) | Dehydrating agent for all nitration chemistry | 10+ tonnes/year for dynamite production |
| Nitric acid (Ostwald process) | Nitration reagent for all high explosives | 5+ tonnes/year for TNT/dynamite |
| Glycerol | Feedstock for nitroglycerin | Byproduct of soap-making or fat hydrolysis |
| Cellulose (cotton/wood pulp) | Feedstock for nitrocellulose | Readily available |
| Toluene (from petroleum or coal tar) | Feedstock for TNT | Requires petroleum refining or coal tar distillation |
| Ammonia (Haber-Bosch) | Precursor for ammonium nitrate, RDX | Requires nitrogen fixation capability |
| Ice plant or refrigeration | Cooling nitrator vessels (maintain <30°C) | Essential for safe nitration |

**Critical dependency chain**: Black powder requires only sulfur, charcoal, and saltpeter — all available from natural sources. All other explosives require concentrated nitric acid (>90%) and sulfuric acid, which in turn require industrial chemical plants (Ostwald process for HNO₃, contact process for H₂SO₄). The jump from black powder to nitroglycerin/dynamite represents a massive step up in industrial infrastructure.

## Explosive Selection Guide

| Application | Preferred Explosive | Why | Typical Charge |
|-------------|-------------------|-----|---------------|
| Soft rock quarrying (limestone, sandstone) | Black powder or ANFO | Low brisance avoids pulverizing soft stone into fines | 0.5-5 kg per hole |
| Hard rock mining (granite, basalt) | Dynamite (60%) or ANFO with booster | High brisance fractures hard rock | 1-10 kg per hole |
| Coal seam blasting | ANFO | Cheap, safe, adequate heaving force for coal | 5-50 kg per hole |
| Tunnel driving | Dynamite or emulsion | Controllable fragmentation, low toxic fumes | 10-100 kg per round |
| Open pit bench blasting | ANFO (bulk loaded) | Cheapest per tonne, easily automated | 50-500 kg per hole |
| Demolition (building) | Dynamite or RDX-based cutting charges | Precise placement, controlled sequence | Variable |
| Military shells | TNT or Composition B | Melt-cast filling, stable storage, high power | 0.5-50 kg |
| Firearms propellant | Nitrocellulose (smokeless powder) | Clean burning, consistent ballistics | 1-50 g per round |
| Demolition charges (military) | C-4 (RDX + plasticizer) | Moldable, adhesive, waterproof | 0.25-5 kg |
| Fireworks display | Black powder + various metal salts | Reliable, colorful, low brisance | Grams to kilograms |

## Scaling Notes

Explosive production scales from village workshop to industrial complex:

- **Village scale** (10-100 kg/year): Black powder only. Manual grinding, wheel mill mixing, hand corning. Adequate for local mining and quarrying. One skilled operator.
- **Workshop scale** (1-10 tonnes/year): Black powder at scale, plus nitroglycerin/dynamite if mixed acid production is available. Requires dedicated explosive magazines (earth-bermed bunkers), nitrator houses with blast walls, and trained operators. The historical dynamite factory (Nobel's factories, 1870s-1900s) operated at this scale with 20-50 workers.
- **Industrial scale** (1,000+ tonnes/year): TNT, RDX, and ANFO production alongside dynamite. Requires petrochemical feedstocks (toluene for TNT), ammonia synthesis (for RDX precursors and ammonium nitrate), and dedicated chemical plant infrastructure. Modern explosive factories employ hundreds and produce thousands of tonnes annually.

Critical scaling constraints: Nitric acid production (Ostwald process) and sulfuric acid production (contact process) are the prerequisites for all nitration chemistry. Without concentrated nitric acid (>90%) and oleum (fuming sulfuric acid), no high explosives can be made. These acid plants represent the primary industrial investment.

## General Safety & Hazards

- **Blast overpressure**: The human body tolerates ~0.2 bar (20 kPa) overpressure without injury. At 1 bar (100 kPa), eardrums rupture. At 3-5 bar, lung damage occurs. At 10+ bar, death is nearly certain. The minimum safe distance from an open-air blast scales with the cube root of the charge weight. For 1 kg of TNT, lethal radius is roughly 5-10 m; for 100 kg, 25-50 m. Blasting operations must evacuate all personnel beyond a calculated safe distance, typically 200-500 m for quarry blasts.
- **Toxic fume production**: All explosives produce toxic gases. Black powder generates SO₂ (sulfur dioxide, IDLH 100 ppm) and CO (carbon monoxide, IDLH 1,200 ppm). TNT and dynamite produce CO and NOₓ (nitrogen oxides, IDLH 20 ppm for NO₂). Underground blasting requires ventilation of 0.5-1.0 m³/s per kg of explosive before re-entry. The standard wait time after an underground blast is 15-30 minutes with ventilation running, followed by gas testing with a handheld CO detector (acceptable limit <25 ppm).
- **Nitroglycerin headache**: Nitroglycerin is absorbed through skin and by inhalation. Symptoms include severe throbbing headache, flushed face, and lowered blood pressure. Workers handling nitroglycerin dynamite often develop tolerance that disappears after 2-3 days away from exposure, leading to "Monday morning headache" when tolerance must rebuild. Treat with rest in a cool, quiet room; symptoms resolve in 2-6 hours. Aspirin or caffeine may help.
- **Ammonium nitrate detonation hazard**: ANFO is insensitive and safe to handle under normal conditions. However, ammonium nitrate becomes detonable when contaminated with fuel, heated above 210°C, or confined in large quantities. The 1947 Texas City disaster (2,300 tonnes of ammonium nitrate on a cargo ship) killed 581 people. Store ammonium nitrate in small, separated piles (under 2,500 tonnes per pile, 5 m minimum between piles). Keep away from fuels, organic materials, and heat sources. Never store in sealed containers that could build pressure.
- **Electrostatic discharge**: Black powder ignites from static sparks as small as 0.1 mJ. All mixing and handling equipment must be electrically grounded. Workers must wear cotton clothing (synthetic fabrics generate static). Maintain relative humidity above 65% in powder-handling areas. Use conductive flooring and grounding straps on all containers.
- **Misfire protocol**: If a charge fails to detonate, wait at least 30 minutes (electric detonators) or 60 minutes (safety fuse) before approaching. Do not attempt to pull out or drill out the misfired charge. The standard procedure is to place a new primer and charge adjacent to the misfire and re-blast. For underwater misfires, wait 24 hours. Document all misfires.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Black powder burns slowly, weak blast | Moisture contamination (>1% water content degrades performance) | Store in sealed containers with desiccant; dry powder at 40-50°C before use; replace if caked or clumped |
| Black powder fails to ignite | Sulfur content too low or grain size too coarse | Maintain 10% sulfur in mixture; sieve to target grain size (2-4 mm for blasting); ensure ingredients thoroughly mixed |
| Nitroglycerin "freezes" below 13°C | NG solidifies and becomes sensitive to shock | Warm dynamite cartridges gradually to 15-20°C in a heated magazine; never use open flame or direct heat to thaw; frozen NG dynamite is shock-sensitive when dropped |
| ANFO fails to detonate | Fuel oil ratio incorrect (optimal 5.5-6% by weight) or ammonium nitrate prills degraded by moisture | Mix fuel oil into prills at 94:6 ratio by weight and allow 24 hours soaking; store prills dry (<0.5% moisture); use fresh prills within 6 months of manufacture |
| Blast produces excessive fly rock | Burden (distance from charge to free face) too small or charge weight too high for the burden | Reduce charge by 30-50% and increase burden to at least 25x borehole diameter; use stemming (clay or sand fill above charge) at least 0.7x burden length |
| Underground blast produces toxic gas requiring long re-entry delay | Insufficient ventilation or explosive formulation produces excess CO/NOₓ | Ensure ventilation delivers 0.5-1.0 m³/s per kg explosive; use permitted explosives (low NOₓ formulations) underground; test air with CO detector before re-entry (<25 ppm CO) |
| Detonation cord fails to initiate booster | Kink or knot in cord attenuating shock wave | Lay cord in smooth curves with minimum bend radius 10x cord diameter; avoid sharp kinks; splice with knot-and-tape connection, maintaining firm contact |
| Dynamite "sweats" nitroglycerin | Storage temperature above 30°C or cartridges aged beyond shelf life | Store at 10-20°C in ventilated magazine; rotate stock (first in, first out); handle sweating cartridges with rubber gloves; destroy cartridges showing visible NG leakage by controlled burning in small quantities |
| Rock fragmentation too coarse after blast | Spacing between boreholes too wide or burden too large | Reduce spacing to 1.0-1.5x burden distance; reduce burden to 25-35x borehole diameter; use delayed initiation sequence to create free faces for each row |
| Premature detonation during loading | Static discharge igniting detonator or primer | Ground all loading equipment; use anti-static detonators; avoid loading during electrical storms; wear cotton clothing and grounding straps |

## Quality Control

| Check | Method | Acceptance Criteria |
|-------|--------|-------------------|
| Black powder burn rate | 10 g sample in test tube, time the burn | 2-5 seconds for blasting grade (2-4 mm grain) |
| Black powder moisture | Weigh, dry at 50°C, reweigh | <1% water content |
| Nitroglycerin purity | Abel heat test (time to brown fumes at 82.2°C) | >10 minutes for stability grade |
| Dynamite density | Weigh cartridge, measure volume | 1.3-1.5 g/cm³ (varies by grade) |
| TNT melting point | Capillary tube melting point apparatus | 80.0-80.8°C (pure TNT); <79.5°C indicates impurities |
| ANFO fuel oil content | Weigh prills before/after oil addition | 5.5-6.0% fuel oil by weight |
| Detonation velocity | Dautriche method or electronic timing | Within 10% of specification for the explosive type |
| Cartridge dimensions | Caliper measurement | ±2 mm on diameter, ±5 mm on length |
| Blasting cap sensitivity | Standard cap test (No. 6 or No. 8 cap) | Reliable initiation with specified cap strength |

## Historical Context

The history of explosives tracks the industrialization of civilization:

- **Black powder (China, ~850 CE)**: First explosive, discovered by Chinese alchemists seeking elixirs of life. Used for fireworks, then military applications by 1000 CE. Reached Europe by 1250 CE. Remained the only explosive for over 700 years.

- **Nitroglycerin (Sobrero, 1847)**: Discovered by Italian chemist Ascanio Sobrero, who was injured by an explosion and warned against its use. Alfred Nobel tamed it by absorbing NG into diatomaceous earth to create dynamite (1867), making it safe enough for industrial use.

- **Dynamite era (1867-1945)**: Dynamite transformed mining, construction, and warfare. The transcontinental railroads, Suez Canal, and Panama Canal were all built with dynamite. Nobel's fortune from dynamite sales funded the Nobel Prizes.

- **TNT and military explosives (1902-1945)**: TNT replaced picric acid as the standard military explosive. WWII drove development of RDX (cyclonite), which was produced at 2,300 tonnes/week by the end of the war. Composition B (60% RDX, 40% TNT) became the standard military filling.

- **ANFO era (1950s-present)**: Ammonium nitrate + fuel oil became the dominant industrial blasting agent due to extreme low cost (~$0.10-0.30/kg vs. $2-5/kg for dynamite). ANFO accounts for ~80% of all explosives used by volume worldwide.

For a bootstrapping civilization, the progression mirrors this history: black powder first (achievable with charcoal, sulfur, and saltpeter), then nitroglycerin and dynamite (once mixed acid production exists), then TNT and military explosives (once petrochemical feedstocks are available), and finally ANFO for large-scale mining (once ammonia synthesis exists).

## See Also

- **[Black Powder](../mining/black-powder.md)**: Detailed gunpowder production
- **[Mining Extraction](../mining/extraction.md)**: Blasting in underground and surface mines
- **[Wood Gasification](wood-gasification.md)**: Charcoal production for black powder
- **[Petrochemicals](petroleum-alternatives.md)**: Hydrocarbon feedstocks for modern explosives
- **[Nitric Acid](acids.md)**: Ostwald process producing nitric acid for nitration
- **[Ammonia Production](ammonia.md)**: Haber-Bosch process for ammonia, the precursor to ammonium nitrate and hexamine

## Storage & Handling

| Explosive | Storage Temperature | Shelf Life | Compatibility | Special Handling |
|-----------|-------------------|------------|--------------|-----------------|
| Black powder | Dry, <30°C | 10+ years (if dry) | Keep away from acids, chlorates | Ground all containers; humidity >65% in handling areas |
| Nitrocellulose | Cool, dry, <25°C | 5-10 years | Decomposes in heat; test with litmus (blue = stable) | Store in ventilated magazines; decomposing NC emits NO₂ (brown gas) |
| Dynamite (NG-based) | 10-20°C | 6-12 months | Keep away from copper (forms sensitive copper fulminate) | Never freeze; thaw frozen cartridges slowly in heated magazine; rotate stock |
| TNT | <50°C | Indefinite | Inert to most materials | Can be melt-cast at 80-82°C; solid TNT is very insensitive |
| RDX | <40°C | 10+ years (when phlegmatized) | Store as Composition B or C-4 (desensitized) | Pure RDX is too sensitive for storage; always store phlegmatized |
| ANFO | Dry, <30°C | 6 months (prills absorb moisture) | Keep separate from fuels and organic material | Load into boreholes within 24 hours of mixing; do not store mixed ANFO |
| Detonators/caps | Magazine storage, <30°C | 2-5 years | Store separately from explosives (different magazine) | Handle with non-sparking tools; never pull on leg wires |

**Magazine construction**: Explosive magazines must be earth-bermed bunkers with blast-relief walls (wood frame with lightweight roof that blows off in an explosion). Interior temperature maintained below 30°C. Lightning protection required. No steel tools inside (use brass, copper, or wood). Locking system with two-key access. Minimum distance from inhabited buildings: 60+ m for small magazines (1 tonne), 300+ m for large magazines (50+ tonnes), calculated using quantity-distance tables.

## Key Deliverables

- **Tier 1** (Years 5-10): Black powder from charcoal, sulfur, and saltpeter. Adequate for soft-rock mining, quarrying, and basic military applications. Production rate: 100-1,000 kg/year at village scale.
- **Tier 2** (Years 15-20): Nitroglycerin and dynamite. Requires mixed acid production (sulfuric + nitric acid). Enables hard-rock mining at 10-100× the efficiency of black powder. Production rate: 1-10 tonnes/year.
- **Tier 3** (Years 20-30): Nitrocellulose smokeless powder for firearms. TNT for military shells. Requires petrochemical toluene and three-stage nitration. Production rate: 10-100 tonnes/year.
- **Tier 4** (Years 30+): RDX, ANFO, and modern military explosives. Requires ammonia synthesis (Haber-Bosch) and advanced chemical plant infrastructure. ANFO production: 1,000+ tonnes/year for large-scale mining.

## Integration Points

| Technology Domain | Explosive Contribution | Dependency on Explosives |
|-------------------|----------------------|------------------------|
| Mining | Rock fragmentation in hard-rock mining (dynamite, ANFO) | Mining is the primary consumer of explosives |
| Construction | Tunnel driving, road cutting, foundation excavation | Large earthmoving projects require blasting |
| Metallurgy | Quarrying limestone for flux, iron ore extraction | Ore supply depends on mining explosives |
| Military | Propellants (nitrocellulose), shell filling (TNT, RDX), demolition | Military drives high-explosive development |
| Chemistry | Nitration chemistry infrastructure (mixed acid plants) | Acid plants serve many industries beyond explosives |
| Petroleum | Seismic exploration (detonation cord), pipeline construction | Exploration uses small explosive charges |
| Transport | Railroad tunneling, canal construction, road cutting | Major infrastructure enabled by blasting |

**Circular dependency note**: Mining requires explosives, but explosives require mined raw materials (sulfur, saltpeter minerals, metal ores for equipment). Black powder breaks this circle because it requires only sulfur, charcoal, and saltpeter — all obtainable without hard-rock mining (sulfur from volcanic vents, saltpeter from niter beds, charcoal from wood). Once black powder enables hard-rock mining, the mined materials support the chemical industry needed for higher explosives.

**Environmental impact**: Large-scale blasting generates ground vibration, airblast (overpressure wave), fly rock, dust, and nitrate contamination of groundwater from ANFO residues. Modern blasting regulations limit peak particle velocity at nearby structures to 5-50 mm/s depending on structure type. Monitoring with seismographs at the nearest occupied structure is standard practice. ANFO residue contributes to groundwater nitrate contamination — a concern for mining operations near water supplies.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
