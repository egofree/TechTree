# Isotope Production

> **Node ID**: energy.nuclear-fission.isotope-production
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.nuclear-fission`](./nuclear-fission.md),
> [`ehs.radiation-safety`](../ehs/radiation-safety.md),
> [`chemistry`](../chemistry/index.md)
> **Enables**: Radioisotope power systems (RTGs, radioisotope heater units), medical and industrial irradiators, sterilization sources
> **Timeline**: Years 30-100+
> **Outputs**: pu238_oxide, sr90_source, am241_source, co60_source, cs137_source
> **Critical**: No — not on the minimum-viable path. Isotope production presupposes an operating reactor fleet, hot-cell infrastructure with metre-scale biological shielding, and a licensed radiation safety program, all of which arrive late in the tech tree.

## Overview

Isotope production is the supply chain that turns reactor neutrons into usable heat sources. A target nuclide — Np-237, Co-59, or a fission product recovered from spent fuel — is placed in a reactor's neutron flux, transmuted into a radioactive product, then chemically separated and purified in heavily shielded hot cells. The output is a sealed source of a specific radioisotope, calibrated for half-life, decay mode, and specific power (W/g). No isotope production, no radioisotope power: every RTG, every radioisotope heater unit, and every nuclear battery begins here.

The defining feature of this process is not the chemistry — solvent extraction and ion exchange are mature, well-understood unit operations — but the radiation environment in which the chemistry must be performed. Freshly discharged irradiated targets emit kilowatts of decay heat and dose rates of thousands of Sv/h. All handling, dissolution, separation, and packaging happens behind concrete walls a metre or more thick, using mechanical master-slave manipulators and filtered ventilation. Alpha emitters (Pu-238, Am-241) add a contamination hazard that demands glovebox containment with inert atmospheres. The process is slow (irradiation cycles of months, cool-down periods of months to years, batch separations of weeks) and capital-intensive, but the product — a self-heating ceramic that runs for decades with no maintenance — is unmatched for deep-space and unattended power applications.

This process sits one level below [Nuclear Fission Power](./nuclear-fission.md) because it cannot exist without an operating reactor producing useful neutron flux. Every piece of equipment downstream of the reactor face — the hot cells, the gloveboxes, the solvent-extraction columns, the source-encapsulation welders — is dedicated infrastructure that must be built, licensed, and staffed before a single gram of product is delivered.

## Fuel Isotope Comparison

The choice of isotope fixes the half-life, power density, shielding burden, and supply route of any radioisotope power system. The table below covers the five isotopes produced by this process.

| Isotope | Half-life | Specific Power | Decay Mode | Fuel Form | Shielding | Availability |
|---------|-----------|----------------|------------|-----------|-----------|--------------|
| **Pu-238** | 87.7 yr | 0.57 W/g | α | PuO₂ ceramic | Minimal (α stopped by cladding) | DOE ORNL/INL (restarted 2015, ~1.5 kg/yr target) |
| **Sr-90** | 28.8 yr | 0.46 W/g (as SrTiO₃) | β⁻ | SrTiO₃ titanate | Heavy (Pb for bremsstrahlung) | Fission product, ~5.9% yield, PUREX recovery |
| **Am-241** | 432 yr | 0.115 W/g | α, γ (59.5 keV) | Am₂O₃ oxide | Moderate (Pb/Ta for 60 keV γ) | UK NNL / ESA program, from aged civil Pu |
| **Co-60** | 5.27 yr | 17.4 W/g | β⁻, γ (1.17, 1.33 MeV) | Co metal pellets | Extreme (Pb, ≥50 mm + remote handling) | Reactor-produced (Co-59(n,γ)) |
| **Cs-137** | 30.17 yr | ~0.42 W/g | β⁻, γ (662 keV from Ba-137m) | CsCl pellet or pollucite | Heavy (Pb for 662 keV γ) | Fission product (~6.2% yield), waste-management context |

**Selection logic**:

- **Pu-238** dominates space and remote applications because its pure alpha decay needs almost no shielding — a Pu-238 RTG can sit next to sensitive electronics. The drawback is supply scarcity: only the United States produces significant quantities, and world inventory is measured in tens of kilograms.
- **Sr-90** and **Cs-137** are cheap (fission products) but their beta and gamma emissions force heavy shielding that cancels much of the cost advantage for compact systems. They make sense for large, stationary sources or marine beacons where mass is less constrained.
- **Am-241** trades lower power density for a 432-year half-life, attractive for ultra-long-life sources where refuelling is impossible. ESA and UK NNL are establishing a non-US supply.
- **Co-60**'s enormous specific power (17.4 W/g) is irrelevant to RTGs because its gamma emissions require shielding so thick that no net mass is saved — it is produced for medical sterilization and industrial radiography, not power.

### Materials Inventory (Reference Pu-238 Campaign, ~1 kg/yr)

| Material | Quantity | Source |
|----------|----------|--------|
| Neptunium-237 oxide (NpO₂ feedstock) | ~2.5 kg Np recycled + ~0.3 kg make-up | [Chemistry](../chemistry/index.md) |
| Aluminium powder (target matrix) | ~10 kg per campaign | [Metals](../metals/index.md) |
| Stainless-steel cladding (304L/316L tubing) | ~50 m of 10-15 mm OD tubing | [Iron & Steel](../metals/iron-steel.md) |
| Nitric acid (HNO₃, 12 M dissolver) | ~2,000 L per campaign | [Chemistry](../chemistry/acids-bases.md) |
| Tributyl phosphate (TBP, 30% in kerosene) | ~500 L solvent inventory | [Chemistry](../chemistry/solvents.md) |
| Hydroxylamine nitrate (Pu reductant) | ~50 kg | [Chemistry](../chemistry/index.md) |
| Iridium (GPHS liner material) | ~1 kg per GPHS module set | [Metals](../metals/index.md) |
| Graphite / carbon-carbon (aeroshell) | ~5 kg per GPHS module set | [Ceramics](../ceramics/index.md) |
| Heavy concrete (hot-cell walls) | ~400 m³ per cell, 3,500-4,200 kg/m³ | [Construction](../construction/index.md) |
| Lead-glass shielding windows | 2-4 windows per cell, 0.8-1.2 m thick | [Glass](../glass/index.md) |

## Pu-238 Production Pathway

Plutonium-238 is the workhorse isotope for space power. The United States produced roughly 300 kg at the Savannah River Site between 1960 and 1988, when the K-reactor shutdown ended domestic supply. Production restarted at Oak Ridge National Laboratory (ORNL) in 2015, with a Department of Energy target of 1.5 kg/yr to sustain NASA deep-space missions (New Horizons, Curiosity, Perseverance, Dragonfly, and future outer-planet probes). The pathway is the Np-237(n,γ) route.

**Historical context**: From 1960 to 1988 the Savannah River Site's K-reactor produced Pu-238 using the same Np-237(n,γ) route at much larger scale — Savannah River delivered roughly 300 kg over 28 years, peaking at over 10 kg/yr in support of the Apollo, Viking, Voyager, Galileo, and Cassini missions. When K-reactor shut down in 1988, the US lost its production capacity and drew on a ~35 kg inventory for the next 27 years. ORNL demonstrated a new process flow in 2015 with a 50 g batch and scaled to the 400 g-level by 2019; the 1.5 kg/yr sustained rate requires HFIR at ORNL plus the ATR at INL running multiple target campaigns in parallel. Russia produced Pu-238 independently for its own space program; limited quantities have been sold to NASA in the past.

### Step 1 — Target Fabrication

Neptunium-237 (recovered historically from reprocessed spent fuel, stored as NpO₂) is blended with aluminium powder and pressed into pellets. The pellets are loaded into stainless-steel cladding tubes — typically double-encapsulated to contain the Np and any fission gases — and seal-welded under inert atmosphere. The target is designed for neutron transparency (the Al matrix reduces self-shielding) and for survival through multi-cycle irradiation without swelling or breach.

Target design details for specific reactors are export-controlled; this description covers only the unclassified process flow. No classified target geometries, weapons-grade separation techniques, or Pu-239/Pu-238 isotopic-enrichment details are described here.

**Materials**:

- [Neptunium-237 oxide](../chemistry/index.md) (NpO₂, stored under inert atmosphere, typically >95% ²³⁷Np)
- [Aluminium powder](../metals/index.md) (high-purity Al, -100 mesh, matrix material)
- [Stainless steel tubing](../metals/iron-steel.md) (304L/316L, double-encapsulated cladding)
- [Helium cover gas](../chemistry/air-separation.md) (5N purity, backfill to 0.1-0.3 MPa for thermal bonding)

### Step 2 — Reactor Irradiation

Targets are loaded into high-flux positions in the High Flux Isotope Reactor (HFIR) at ORNL or the Advanced Test Reactor (ATR) at Idaho National Laboratory. The neutron capture sequence is:

```
Np-237 + n  →  Np-238   (σ_γ ≈ 169 barns thermal)
Np-238      →  Pu-238 + β⁻   (t½ = 2.117 days)
```

Thermal flux in HFIR's flux trap reaches 2.5 × 10¹⁵ n/cm²·s — among the highest steady-state fluxes in the world. Each irradiation cycle runs roughly 2-3 reactor cycles (about 50-85 days), converting 10-15% of the Np-237 inventory per cycle. Targets are typically re-irradiated through several cycles to build up Pu-238 inventory and burn down residual Np-237. Some Pu-238 absorbs a second neutron to form higher plutonium isotopes, so the product is "heat-source grade" (~80-85% Pu-238 by alpha activity), a distinct isotopic vector from any weapons application — the process is optimised solely for alpha-decay heat.

**Calibration / Verification**:

1. **Flux wires**: Co-Al or Ni flux monitors loaded with each target are extracted post-irradiation and gamma-counted to verify the delivered thermal fluence against the neutronics calculation (target: ±5% agreement).
2. **Non-destructive assay**: Gamma scanning of the irradiated target through the canal wall confirms Pu-238 build-up via the 766 keV line; result is compared to the ORIGEN depletion prediction.
3. **Target integrity**: Visual and sipping tests in the reactor pool confirm no cladding breach (target: no detectable Np or fission-product activity in the canal water).

### Step 3 — Cool-down

After the final irradiation, targets are held in the reactor pool or a water-filled canal for 6-18 months. This lets short-lived activation and fission products (Zr-95, Nb-95, Ru-106, the rare-earth fraction) decay, reducing dose and decay heat before hot-cell processing. A freshly discharged target can emit several kW of decay heat; after a year of cool-down, the dominant activity is the Np/Pu pair itself plus long-lived fission products (Cs-137, Sr-90) carried as impurities.

### Step 4 — Chemical Separation (REDC Hot Cells)

Cooled targets are transferred to the Radiochemical Engineering Development Center (REDC) at ORNL — a hot-cell complex with concrete walls 1.2-1.8 m thick, lead-glass viewing windows 0.8-1.2 m thick, and mechanical master-slave manipulators. The chemical flow is a modified neptunium/uranium extraction based on PUREX chemistry:

1. **Declad and dissolve**: The stainless-steel cladding is mechanically breached or chemically dissolved; the Np/Pu/Al matrix is dissolved in concentrated nitric acid (HNO₃, 8-13 M) with a catalytic fluoride or mercuric catalyst to accelerate Al dissolution.
2. **Solvent extraction**: The dissolver solution is contacted with tributyl phosphate (TBP, 30 vol%) in a kerosene-type diluent — the PUREX solvent. Np and Pu extract into the organic phase; fission products and the Al matrix stay in the aqueous raffinate.
3. **Np/Pu partition**: Plutonium is selectively stripped from the loaded organic phase by reduction to Pu(III) with a reductant such as hydroxylamine nitrate or ferrous sulfamate, leaving Np(IV) in the organic phase for separate recovery and recycle to the next irradiation campaign.
4. **Purification**: The Pu product stream undergoes additional extraction cycles (typically 2-3) and anion-exchange polishing to remove trace Am-241 (grown in from Pu-241 decay) and other alpha/gamma emitters, meeting the <0.5% non-Pu-238 alpha specification for heat-source grade.
5. **Conversion to oxide**: The purified Pu nitrate solution is precipitated as Pu(III) or Pu(IV) oxalate, filtered, calcined in air or hydrogen to PuO₂ powder (typically 80-90% ²³⁸Pu), pressed into pellets, and sintered at 1,500-1,600 °C into the ceramic fuel form.

The recovered Np-237 is recycled into new targets, closing the feedstock loop. Typical end-to-end recovery is 90-95% for Pu and 85-90% for recyclable Np. A single target, irradiated through 3-5 cycles, yields 50-150 g of heat-source-grade Pu-238.

## Sr-90 Production

Strontium-90 is a fission product (cumulative yield ~5.9% per U-235 thermal fission) recovered from reprocessed spent reactor fuel. After cooling, the PUREX aqueous raffinate — the high-level liquid waste stream that contains the fission-product inventory — is routed to a fission-product recovery line. Sr is separated by solvent extraction with bis(2-ethylhexyl) phosphoric acid (HDEHP), by crown-ether-based extraction, or by precipitation as strontium nitrate. The product is converted to strontium titanate (SrTiO₃), a refractory ceramic (melting point 1,910 °C) chosen for its insolubility and chemical stability in accident scenarios.

Sr-90 RTGs powered the Soviet Beta-M series — roughly 1 W(e) per source, deployed at thousands of unattended lighthouses and beacons along the Arctic coast from the 1970s onward. Several of these sources have since been recovered under international cleanup programs. Zeno Power and other commercial ventures are modernizing Sr-90 RTG designs for terrestrial and marine applications, taking advantage of the large existing Sr-90 inventory in stored spent fuel: a single commercial reprocessing campaign can yield kilograms.

**Calibration / Verification**:

1. Gamma spectroscopy confirms Sr-90 (via the Y-90 daughter in secular equilibrium) and bounds the Cs-137 and other gamma impurities to <0.1%.
2. Thermal output of the sealed source is measured in a Bunsen-type calorimeter — agreement with the calculated 0.46 W/g specific power confirms isotopic purity and mass.
3. Strontium carrier chemical purity is verified by ICP-MS: trace Sr-89 (t½ = 50.5 d) decays away during cool-down and must be below the 0.01% specification for long-lived service.
4. SrTiO₃ ceramic density measured by Archimedes method: target ≥95% theoretical (4.7 g/cm³) to ensure mechanical integrity and leach resistance.

## Am-241 Production

Americium-241 is the decay daughter of Pu-241 (t½ = 14.3 yr): aged plutonium stocks accumulate Am-241 at roughly 0.5%/yr of the Pu-241 content. The UK National Nuclear Laboratory (NNL) at Sellafield has demonstrated Am-241 extraction from civil plutonium stocks for the European Space Agency's radioisotope power program. Separation uses a variant of the TRUEX flow — solvent extraction with octyl(phenyl)-N,N-diisobutylcarbamoylmethylphosphine oxide (CMPO) in TBP/kerosene — to co-extract the trivalent actinides, followed by selective stripping and anion-exchange polishing to separate Am from the lanthanides and residual Pu.

The product is precipitated as Am oxalate and calcined to Am₂O₃ for pellet pressing. ESA's program targets 10-50 g/yr initially, scaling toward the multi-hundred-gram quantities needed for a European deep-space RTG. Am-241's attraction is its 432-year half-life: a source decays only ~0.16%/yr, so power output is effectively constant over any mission lifetime. Its drawbacks are lower specific power (0.115 W/g — about a fifth of Pu-238) and a 59.5 keV gamma from the Np-237 daughter, which forces a few millimetres of tantalum or lead shielding around the source.

**Calibration / Verification**:

1. Alpha spectroscopy confirms Am-241 identity (5.486 MeV principal alpha line) and bounds Pu contamination to <0.1% by alpha activity.
2. The 59.5 keV gamma emission is measured by HPGe detector and compared to the known specific gamma constant (1.3 × 10⁻⁵ mSv·m²/(MBq·h)) to verify mass.
3. Am₂O₃ pellet density measured by Archimedes method: target ≥90% theoretical (11.7 g/cm³); pellets are sintered under argon to avoid oxidation-state changes.

## Co-60 Production

Cobalt-60 is made by neutron activation of stable Co-59. Cobalt-59 slugs (high-purity metal, typically 1-5 mm diameter pellets) are loaded into adjuster-rod positions or dedicated irradiation channels in a CANDU, RBMK, or research reactor. The capture reaction is Co-59(n,γ)Co-60 (σ_γ = 37.2 barns thermal). Co-60 decays by β⁻ emission to Ni-60, releasing a 1.17 MeV and a 1.33 MeV gamma pair per decay — the two lines that make Co-60 the workhorse of industrial radiography and medical-product sterilization.

Specific activity is set by the neutron fluence and irradiation time: typical research-reactor cycles reach 50-200 Ci/g after 1-3 years of irradiation. The 17.4 W/g specific power (thermal) is the highest of any practical isotope, but the gamma emissions require extreme shielding — 50 mm of lead for a curie-scale source — so Co-60 is not used for RTGs. Its inclusion here reflects that the same irradiation, hot-cell, and source-encapsulation infrastructure serves both the power-isotope and the irradiation-source applications.

## Cs-137 Recovery

Cesium-137 (fission yield ~6.2%) is recovered from spent fuel alongside Sr-90. CsCl pellets were historically used in medical brachytherapy and in soil-moisture and densitometry gauges; its 30.17-year half-life and 662 keV gamma (from the Ba-137m daughter) made it a common sterilization and brachytherapy source. Cs-137 is primarily a waste-management concern in the context of this tech tree — it is produced as part of the fission-product separation train and either sealed in sources or vitrified in high-level waste glass. Recovery chemistry uses phosphotungstic acid, calix-crown extractants, or ammonium phosphomolybdate; the product is sealed as a CsCl pellet or incorporated into a pollucite glass-ceramic waste form.

## Target Fabrication (General)

Target fabrication is a precision ceramic-and-metallurgy operation performed in gloveboxes (for alpha-emitting target materials like Np-237 or Am-241) or standard dry rooms (for stable targets like Co-59). The general flow:

1. **Blend**: Target oxide (NpO₂, Co₃O₄, etc.) is mixed with a matrix powder (Al, Mg, or graphite for neutron transparency) in a ball mill to a homogeneous 10-30 wt% target loading.
2. **Press**: The blend is cold-pressed into green pellets at 100-400 MPa, typically 5-15 mm diameter, density 60-80% theoretical.
3. **Encapsulate**: Pellets are loaded into cladding tubes (stainless steel 304L/316L, Zircaloy, or aluminium alloy 6061) with a getter or cover gas, seal-welded under helium or argon, and helium-leak tested to <10⁻⁹ Pa·m³/s.
4. **Certify**: Each target is weighed, dimensionally inspected, radiographed, and helium leak-tested before reactor insertion. Documentation traces each target's composition and mass to the subsequent product assay.

## Irradiation Management

Reactor position determines flux and spectrum. Positions in or near the core's flux trap see 10¹⁴-10¹⁵ n/cm²·s thermal; peripheral locations see 10¹²-10¹³ n/cm²·s with a harder spectrum. The irradiation plan is a trade-off between conversion rate (favouring high flux) and target survival (favouring lower flux to limit swelling and gas generation). Typical campaigns run 2-3 cycles of 2-3 months each, with 10-15% conversion of the target nuclide per cycle. In-core dosimetry (cobalt-aluminium or niobium flux wires) is loaded with each target to verify delivered fluence, and the target is re-inserted or withdrawn based on the measured burn-up.

## Chemical Separation (PUREX)

Solvent extraction is the workhorse separation chemistry. The canonical PUREX process — tributyl phosphate (TBP, 30 vol%) in a kerosene-type diluent — selectively extracts tetravalent and hexavalent actinides (U(VI), Pu(IV), Np(IV)) from nitric acid dissolver solution into the organic phase, leaving the fission products (Cs, Sr, lanthanides, transition metals) in the aqueous raffinate. For isotope production, the same chemistry is adapted:

- **Pu-238 line**: Np and Pu co-extract; Pu is reduced to Pu(III) and stripped; Np is recovered for recycle.
- **Sr-90 line**: Loaded on a separate extraction (HDEHP or crown ether) from the PUREX raffinate.
- **Cs-137 line**: Extracted with phosphotungstic acid, calix-crown, or ammonium phosphomolybdate from the fission-product stream.
- **Am-241 line**: TRUEX solvent (CMPO/TBP) co-extracts actinides(III) and lanthanides; a subsequent anion-exchange or Cyanex-301 step separates Am from lanthanides.

Solvent extraction uses pulse columns or mixer-settlers — each "stage" equilibrates the two liquid phases and separates them by gravity. A typical line has 8-16 stages of extraction, 6-10 stages of scrubbing, and 6-10 stages of stripping. The equipment is miniaturized for isotope production (columns 30-100 mm diameter, versus 300-800 mm for commercial reprocessing) because throughput is grams-to-kilograms, not tonnes of heavy metal per day.

## Hot Cell Operations

Hot cells are the defining infrastructure of isotope production. A production cell is a heavily shielded enclosure — typically 6 m × 4 m × 4 m — with:

- **Biological shielding**: 1.0-1.8 m of heavy concrete (magnetite or barite aggregate, density 3,500-4,200 kg/m³) on all sides. Lead or steel inserts thicken local streaming patches.
- **Viewing windows**: 0.8-1.2 m thick oil-filled zinc-bromide or lead-glass laminates, providing a clear view through the equivalent of 1 m of concrete.
- **Remote manipulators**: Mechanical master-slave arms (e.g., CRL Model 8 or SB24-4a) pass through the wall via ball-and-socket thimbles, transmitting the operator's hand motion with 3-6 kg payload capacity at the remote end.
- **Ventilation**: Once-through air, negative pressure (-125 to -500 Pa relative to ambient), HEPA and charcoal filtration on the exhaust. Airflow cascades from clean to contaminated zones; the cell exhaust passes through two stages of HEPA (99.97% at 0.3 µm) and activated charcoal for iodine before stack release. Typical cell ventilation rate: 10-20 air changes per hour.
- **Material handling**: Shielded cask transfer ports (coffins) for moving material in/out; pneumatic or hydraulic sample rabbit systems for small items.

Cell operations are batch-oriented. A target is received, decladded, dissolved, processed through solvent-extraction columns or ion-exchange beds, and the product is precipitated, calcined, and packaged — all by remote manipulation behind the shielding, with the operator watching through the window or on shielded closed-circuit cameras. Routine maintenance (replacing manipulator boots, changing filters, decontaminating the cell floor) is done by personnel in protective suits during scheduled outages when the cell inventory is minimised.

## Gloveboxes for Alpha Emitters

Plutonium-238 and americium-241 are alpha emitters: the decay itself is easy to stop (a sheet of paper blocks alpha particles), but the contamination hazard is severe — inhaled or ingested alpha activity is among the most radiotoxic burdens known. Glovebox containment is therefore mandatory for all dry handling of Pu and Am product.

A glovebox is a welded stainless-steel or polypropylene enclosure, typically 2-3 m long, operated under slight negative pressure (-50 to -250 Pa) with an inert nitrogen or argon atmosphere (O₂ < 1000 ppm, H₂O < 100 ppm) to prevent pyrophoric ignition of fine PuO₂ powder. Operators reach into the box through long elastomer gloves sealed into ports in the front face. Every transfer in or out passes through a bag-out port — a gas-tight sleeve that is heat-sealed, cut, and re-sealed around each item — to maintain containment. Continuous air monitors (CAMs) sample the box atmosphere and the workroom for airborne alpha activity; an alarm at 8 DAC (derived air concentration) triggers evacuation and investigation.

## Source Encapsulation and Quality Assurance

Finished isotope product is sealed into a welded capsule for service. The general-purpose heat source (GPHS) used in US space RTGs is a multi-layer assembly: the PuO₂ pellet sits in an iridium liner (chosen for strength and compatibility at 1,200 °C), which is welded shut inside a graphite impact shell, which is in turn enclosed in a carbon-bonded carbon-fibre aeroshell — the assembly survives atmospheric re-entry and surface impact without releasing Pu. Iridium is uniquely qualified: it retains strength to 1,200 °C and does not embrittle under alpha bombardment.

For non-space sources (Sr-90, Cs-137, Co-60), double-encapsulated stainless-steel capsules, helium leak-tested to <10⁻⁹ Pa·m³/s and hydrostatically proof-tested, are the standard. Each source is non-destructively assayed (mass, isotopic composition, thermal output) and documented with a certificate that traces the material from target irradiation through final encapsulation.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| HFIR peak thermal flux | 2.5 × 10¹⁵ n/cm²·s |
| Np-237 thermal capture cross-section | 169 barns |
| Np-238 half-life | 2.117 days |
| Pu-238 half-life | 87.7 yr |
| Pu-238 specific power | 0.57 W/g (metal) |
| Pu-238 DOE production target | ~1.5 kg/yr |
| Pu-238 heat-source grade isotopic purity | ≥ 82% ²³⁸Pu |
| Savannah River historical production | ~300 kg over 28 yr (1960-1988) |
| Sr-90 fission yield (U-235 thermal) | ~5.9% |
| Sr-90 half-life | 28.8 yr |
| Sr-90 specific power (as SrTiO₃) | ~0.46 W/g |
| Am-241 half-life | 432 yr |
| Am-241 specific power | 0.115 W/g |
| Cs-137 fission yield | ~6.2% |
| Cs-137 half-life | 30.17 yr |
| Co-59 thermal capture cross-section | 37.2 barns |
| Co-60 half-life | 5.27 yr |
| Co-60 specific power | 17.4 W/g |
| Hot-cell concrete wall thickness | 1.0-1.8 m heavy aggregate |
| Hot-cell viewing window thickness | 0.8-1.2 m |
| Hot-cell ventilation | 10-20 air changes/hr, HEPA + charcoal |
| Glovebox atmosphere | N₂ or Ar, O₂ < 1000 ppm |
| Typical irradiation conversion per cycle | 10-15% |
| Typical Np/Pu recovery efficiency | 90-95% (Pu), 85-90% (Np recycle) |
| Source capsule helium leak-test limit | <10⁻⁹ Pa·m³/s |

## Expected Performance

A mature isotope-production program delivers product on multi-year cadences set by reactor availability, irradiation physics, and cool-down requirements — not by market demand:

- **Pu-238 sustained output**: 1.5 kg/yr requires 3-5 concurrent target campaigns in HFIR and ATR, each running 2-3 irradiation cycles. End-to-end latency from target fabrication to sealed GPHS module is 4-6 years (irradiation: 1-2 yr; cool-down: 1-1.5 yr; chemical processing and oxide conversion: 0.5-1 yr; encapsulation and QA: 0.5-1 yr).
- **Sr-90 recovery**: Kilogram-scale batches recovered from each reprocessing campaign; a single commercial reprocessing plant's annual raffinate stream contains tens of kilograms of Sr-90.
- **Am-241 output**: UK NNL / ESA program targets 10-50 g/yr initially, scaling to several hundred grams as the process matures. Latency is dominated by the decades of Pu-241 decay required to build up Am-241 inventory in aged civil plutonium.
- **Co-60 output**: Single CANDU adjuster rod load yields 10-50 MCi of Co-60 per annual cycle; the world supply of Co-60 is set by the number of reactors allocated to isotope production vs. power generation.
- **Hot-cell utilization**: A single REDC-class cell processes 2-4 Pu-238 campaigns per year; throughput is limited by decontamination and maintenance outages between batches, not by chemistry cycle time.

## Safety

Isotope production concentrates every hazard of the nuclear fuel cycle into one facility:

- **Criticality**: Dissolved fissile material (residual Pu in Np targets, U in spent fuel) can, in principle, form a critical mass in a process vessel. Criticality safety relies on geometrically favorable vessel shapes (slab or annular tanks, always subcritical by geometry), batch-size limits, neutron-poison controls (gadolinium or boron dissolved in process solutions), and double-contingency analysis (at least two independent, unlikely failures required for criticality).
- **Contamination**: Alpha contamination from Pu/Am is the dominant radiological risk. Containment (gloveboxes, cell pressure cascades, HEPA filtration), continuous air monitoring, and strict personnel protective measures (positive-pressure suits for cell-entry maintenance, routine whole-body counting) are the controls.
- **Decay heat**: A freshly processed batch of Pu-238 generates hundreds of watts of heat per kilogram. Process solutions and product containers must be cooled or sized to prevent boiling; sealed sources are qualified to dissipate decay heat without thermal runaway.
- **External dose**: Gamma dose from Co-60, Cs-137, and fission-product impurities is managed by the hot-cell shielding, distance, and time (ALARA). Worker dose is tracked by thermoluminescent dosimeter and electronic dosimeter; occupational dose limits are typically 20 mSv/yr (ICRP) or 50 mSv/yr (US 10 CFR 20).
- **Waste management**: The aqueous raffinate from solvent extraction contains the bulk of the fission products and is high-level liquid waste. It is denitrated, vitrified in a borosilicate glass matrix, cast into stainless-steel canisters, and stored for geologic disposal. Solid wastes (contaminated equipment, used solvent) are compacted, incinerated, or cemented as low-level or intermediate-level waste.
- **Regulatory oversight**: Production facilities operate under national nuclear-regulator licenses (US NRC, UK ONR, etc.), with environmental impact statements, probabilistic safety assessments, and International Atomic Energy Agency safeguards for any fissile material inventory.

### Troubleshooting

| Symptom | Likely Cause | Corrective Action |
|---------|--------------|-------------------|
| Low Pu-238 conversion per cycle | Lower-than-design thermal flux or spectral hardening | Verify flux-wire fluence; reposition target closer to core or add a moderator sleeve |
| High Am-241 in Pu product | Long cool-down letting Pu-241 decay to Am-241 | Shorten cool-down or add an extra anion-exchange polishing pass |
| Target cladding breach in pool | Weld defect or corrosion under irradiation | Isolate target in a failed-fuel can; perform sipping survey; reject or re-encapsulate |
| High gamma dose at cell window | Cs-137 or Co-60 breakthrough in extraction | Verify scrub-stage efficiency; add hold-back agent; re-run second extraction cycle |
| Glovebox O₂ alarm | Glove puncture or bag-out seal failure | Stop work; isolate box; replace glove or re-seal port before resuming |
| CAM alpha alarm in workroom | Contamination release from glovebox | Evacuate personnel; survey and decontaminate; root-cause before restart |

## Strengths and Weaknesses

**Strengths**:

- Produces the only long-lived, high-reliability heat source capable of operating in deep space, polar regions, and ocean floors without sunlight or fuel logistics — a Pu-238 RTG has operated for 45+ years (Voyager).
- Alpha-emitting isotopes (Pu-238, Am-241) require minimal radiation shielding, allowing compact source geometries and direct integration with thermoelectric converters.
- The Np-237 feedstock is recyclable: unconverted neptunium is recovered in PUREX and fed back into new targets, so the bulk of the heavy-metal inventory is not consumed but "worked" over many campaigns.
- Co-production of medical and industrial isotopes (Co-60, Cs-137, Sr-90) on the same hot-cell infrastructure amortises the capital cost across multiple product lines.
- The PUREX / solvent-extraction chemistry is mature, well-modelled, and operates at room temperature and atmospheric pressure — no extreme process conditions beyond the radiation field.

**Weaknesses**:

- Capital cost is extreme: a single production-scale hot-cell line costs hundreds of millions of dollars, takes a decade to license and build, and requires a dedicated reactor with high-flux irradiation positions.
- Throughput is fundamentally limited by reactor neutron flux and target survival — the US has struggled to sustain even 1.5 kg/yr of Pu-238 despite a decade of investment.
- Every step from irradiation to encapsulation generates high-level radioactive waste (fission-product raffinate, contaminated equipment, used solvent) that requires vitrification and geologic disposal.
- Pu-238 and Am-241 are extreme radiological hazards if released — even gram quantities of dispersed alpha contamination drive expensive cleanup and pose uptake risks to workers.
- The process depends on a single element (Np-237 feedstock) whose world inventory is finite and tied to past reprocessing campaigns; no significant new Np-237 is being created outside specialized irradiation.
- Proliferation sensitivity surrounds any plutonium-bearing process, requiring IAEA safeguards, physical protection, and classification that raise cost and limit international collaboration.

## See Also

- **[Nuclear Fission Power](./nuclear-fission.md)** — Reactor infrastructure and neutron flux that this process depends on
- **[Radioisotope Power](./radioisotope-power.md)** — Consumer of this supply chain: RTGs, heater units, and other decay-heat power systems
- **[Radiation Safety](../ehs/radiation-safety.md)** — Shielding design, dosimetry, contamination control, and ALARA practice that govern all hot-cell and glovebox operations
- **[Chemistry](../chemistry/index.md)** — Nitric acid, solvent extraction, ion exchange, and the chemical reagent supply chain
- **[Energy Domain](./index.md)** — Other energy conversion processes

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
