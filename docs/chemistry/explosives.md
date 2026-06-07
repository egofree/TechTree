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

- [**Black Powder**](black-powder.md) — Black powder manufacture (KNO₃/charcoal/sulfur): separate pulverization, wheel-mill mixing, corning, and granulation. The first explosive, foundational for mining and firearms.
- [**Nitrocellulose & Smokeless Powders**](nitrocellulose.md) — Nitration of cellulose to guncotton and pyroxylin. Manufacture of single-base and double-base smokeless powders. Foundation of modern propellants and early plastics.
- [**Nitroglycerin & Dynamite**](nitroglycerin-dynamite.md) — Synthesis of nitroglycerin from glycerol and mixed acid, absorbed into diatomaceous earth to produce dynamite cartridges. The workhorse blasting explosive from the 1870s onward.
- [**High Explosives (TNT, RDX, ANFO)**](high-explosives.md) — TNT via three-stage toluene nitration, RDX via Woolwich or Bachmann process, ANFO from ammonium nitrate prills and fuel oil. The mature industrial and military explosive palette.
- [**Detonation & Blasting**](detonation-blasting.md) — Blasting caps and initiating systems, detonation physics, blasting design parameters, vibration and airblast control, explosive selection guide, and safety. The systems needed to use explosives safely and effectively.


## Safety & Hazards

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

## See Also

- **[Black Powder](../mining/black-powder.md)**: Detailed gunpowder production
- **[Mining Extraction](../mining/extraction.md)**: Blasting in underground and surface mines
- **[Wood Gasification](wood-gasification.md)**: Charcoal production for black powder
- **[Petrochemicals](petroleum-alternatives.md)**: Hydrocarbon feedstocks for modern explosives
- **[Nitric Acid](acids.md)**: Ostwald process producing nitric acid for nitration
- **[Ammonia Production](ammonia.md)**: Haber-Bosch process for ammonia, the precursor to ammonium nitrate and hexamine

---

*Part of the [Bootciv Tech Tree](../index.md) • [Chemistry](./index.md) • [All Domains](../index.md)*
