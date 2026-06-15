# Nuclear Fuel Cycle

> **Node ID**: energy.nuclear-fission.nuclear-fuel-cycle
> **Domain**: [Energy](./index.md)
> **Dependencies**: [`energy.nuclear-fission`](./nuclear-fission.md), [`mining.extraction`](../mining/extraction.md), [`chemistry`](../chemistry/index.md)
> **Enables**: None
> **Timeline**: Years 30-100+
> **Outputs**: enriched_uranium, reactor_fuel, spent_fuel, reprocessed_uranium
> **Critical**: No — the fuel cycle is a sustained industrial undertaking that depends on a mature fission program. Mining, chemical processing, enrichment, fabrication, and waste disposition each demand their own infrastructure, workforce, and regulatory regime, all of which only make sense after a reactor fleet exists.

## Overview

The nuclear fuel cycle is the chain of industrial processes that takes uranium ore from the ground, prepares it for reactor service, manages the irradiated fuel after discharge, and dispositions the resulting waste streams. The cycle divides into a **front end** (mining, milling, conversion, enrichment, fabrication) that prepares fresh fuel, and a **back end** (cooling, reprocessing, conditioning, disposal) that handles spent fuel. Each step is a chemical and metallurgical operation in its own right, and the cycle as a whole is what makes a reactor more than a one-time experiment: without it, fission is a physics demonstration rather than an energy system.

Natural uranium contains only 0.72% fissile U-235; the remainder is mostly U-238, which does not sustain a thermal chain reaction. Light-water reactors (the dominant design worldwide) require uranium enriched to 3-5% U-235, which means physically separating the two isotopes. Because they differ only in mass by about 1.3%, separation requires many successive tiny enrichment steps, performed on uranium in gaseous form (uranium hexafluoride, UF₆). Once enriched, the uranium is converted back to ceramic uranium dioxide (UO₂), pressed into pellets, sintered, and sealed inside zirconium-alloy tubes to form fuel rods.

After 3-6 years in the reactor core, fuel reaches its discharge burnup (33-60 gigawatt-days per tonne of heavy metal) and is removed to a cooling pond. Spent fuel is intensely radioactive and thermally hot: it must cool for at least 5 years before any further handling. The once-through cycle stops here, with the spent fuel destined for a geological repository. The closed cycle continues: the spent fuel is dissolved in nitric acid and put through the PUREX process (Plutonium-URanium EXtraction), a solvent-extraction operation using tributyl phosphate (TBP) in kerosene that separates the recoverable uranium and plutonium from the fission-product waste. The recovered uranium can be re-enriched and refabricated; the plutonium can be blended into mixed-oxide (MOX) fuel.

This article is the process-level companion to the [Nuclear Fission Power](./nuclear-fission.md) capability and covers the cycle from mining through waste form. Reactor physics, neutronics, and power conversion are addressed in the parent article. Radiological protection practices are covered in [Radiation Safety](../ehs/radiation-safety.md).

## Prerequisites

- [Mining and extraction capability](../mining/extraction.md) — uranium orebody identification, open-pit, underground, or in-situ leach (ISL) recovery
- [Industrial chemistry](../chemistry/index.md) — nitric acid, hydrogen fluoride, fluorine gas, kerosene solvents, tributyl phosphate, hydrogen reduction
- [Pressure-vessel metallurgy](../metals/iron-steel.md) and [zirconium refining](../metals/index.md) — for fuel cladding and process vessels
- [Centrifuge technology](../chemistry/centrifuge.md) — gas centrifuges for enrichment, disc-and-bowl centrifuges for solvent-extraction phases
- [Solvent extraction and distillation](../chemistry/distillation-column.md) — for PUREX separation trains
- [Radiation safety regime](../ehs/radiation-safety.md) — licensed operations, dosimetry, contamination control, emergency response
- [Parent fission capability](./nuclear-fission.md) — the reactor fleet that consumes the fuel

## Bill of Materials

### Front-End Inputs (per 1 tonne of natural uranium feed)

| Input | Quantity | Specification | Source |
|----------|----------|----------------|--------|
| Uranium ore (0.2% U₃O₈) | 850-1200 t run-of-mine | Open-pit, underground, or ISL pregnant liquor | [Mining Extraction](../mining/extraction.md) |
| Sulfuric acid (H₂SO₄) | 10-40 kg per t ore (acid leach) | 93-98% concentrated | [Chemistry / Acids](../chemistry/acids.md) |
| Hydrogen fluoride (HF) | ~150 kg per t U | Anhydrous, 99.9% | [Chemistry / Acids](../chemistry/acids.md) |
| Fluorine gas (F₂) | ~270 kg per t U | Electrolytic, >98% | [Chemistry / Electrolysis](../chemistry/electrolysis.md) |
| Enrichment work | ~110 SWU per kg of 3.5% product | Centrifuge cascade | [Chemistry / Centrifuge](../chemistry/centrifuge.md) |
| Hydrogen (H₂) | ~25 kg per t UO₂ | Reducing atmosphere, >99.95% | [Chemistry / Electrolysis](../chemistry/electrolysis-cell.md) |
| Zirconium alloy tubing | ~30 kg per assembly | Zircaloy-4 or Zirlo, 9.5-10.7 mm OD | [Metals](../metals/index.md) |
| Enrichment SWU per GWe-year | ~100,000-120,000 SWU | 3-4 reloads per year at 45 GWd/t | This cycle |

### Back-End Inputs (per 1 tonne of spent fuel reprocessed)

| Input | Quantity | Specification | Source |
|----------|----------|----------------|--------|
| Nitric acid (HNO₃) | 3-7 t | 7-14 M, purified | [Chemistry / Acids](../chemistry/acids.md) |
| Tributyl phosphate (TBP) | 20-40 kg makeup | 30% v/v in kerosene | [Chemistry / Solvents](../chemistry/solvents.md) |
| Kerosene / n-dodecane diluent | 100-200 kg makeup | Hydrogenated, low aromatic | [Chemistry / Solvents](../chemistry/solvents.md) |
| Hydrazine (N₂H₄) or U(IV) reductant | ~1-3 kg Pu stabilized | Pu(IV) → Pu(III) stripping | [Chemistry](../chemistry/index.md) |
| Borosilicate glass frit | 100-150 kg per t HM | Na₂O-B₂O₃-SiO₂-Al₂O₃ base | [Glass](../glass/index.md) |
| Stainless steel canister | ~1 per 50-80 kg HM | 304L or 316L, ~5 mm wall | [Iron & Steel](../metals/iron-steel.md) |

## Front End

### Uranium Mining

Uranium is recovered by three principal methods. The choice depends on orebody geometry, depth, and groundwater chemistry.

- **Open-pit mining** is used for near-surface orebodies (typical depth <200 m). Strip ratio is moderate; ore grades run 0.05-0.5% U₃O₈. The product is broken rock hauled to a mill.
- **Underground mining** extracts deeper deposits (200-2000 m) via shafts and drifts. Higher ore grade (0.1-1% U₃O₈) offsets higher cost. Ventilation must manage radon gas (Rn-222, daughter of U-238 decay) — a radiological hazard addressed under [Radiation Safety](../ehs/radiation-safety.md).
- **In-situ leach (ISL) recovery** dissolves uranium directly in the orebody by injecting an oxidizing leach solution (acidic or alkaline) through injection wells and pumping the pregnant liquor to surface. ISL dominates roughly half of global production because it avoids the cost and tailings burden of conventional mining. Acid leach uses sulfuric acid with an oxidant (hydrogen peroxide or oxygen); alkaline leach uses sodium bicarbonate/carbonate with oxygen, preferred for carbonate-rich ores that would consume excessive acid.

### Milling and Yellowcake

Mined ore is crushed and ground in a wet circuit, then leached (typically with sulfuric acid plus an oxidant) to dissolve uranium as the uranyl sulfate complex. The pregnant liquor is separated from the solids, purified by ion exchange or solvent extraction, and precipitated as ammonium or sodium diuranate. The precipitate is dewatered, washed, and roasted at 400-800°C to produce **yellowcake** — a powder that is nominally U₃O₈ (triuranium octoxide) but in practice a mixture of uranium oxides. Typical yellowcake assays 75-85% U₃O₈ by weight. Mill tailings, containing the radium-bearing residues and roughly 85% of the original ore radioactivity, are placed in engineered tailings management facilities with liners, covers, and long-term stewardship.

The tailings stream is the principal environmental burden of the front end. Radon (Rn-222) emanation from Ra-226 in the tailings, plus the mobility of trace selenium, molybdenum, and arsenic in acidic seepage, drive the design criteria for tailings facilities: compacted clay or synthetic membrane liners, peripheral groundwater monitoring wells, and an eventual earthen cover designed to limit infiltration and radon release for the institutional control period (typically 200-1000 years). ISL operations avoid the tailings burden entirely but produce contaminated groundwater that must be restored to baseline before license termination — typically by re-circulating treated water through the leached aquifer.

### Conversion to UF₆

Yellowcake is refined and converted to uranium hexafluoride (UF₆), the only uranium compound that is gaseous at moderate temperatures (sublimes at 56.5°C). The standard route reduces U₃O₈ to uranium dioxide (UO₂) with hydrogen, hydrofluorinates UO₂ with anhydrous hydrogen fluoride (HF) to uranium tetrafluoride (UF₄), and finally reacts UF₄ with fluorine gas (F₂) to yield UF₆. Fluorine production is itself a significant industrial activity — it requires electrolysis of molten potassium bifluoride (the same [electrolysis cell](../chemistry/electrolysis.md) technology used elsewhere in chemistry). The product is loaded into standard 48Y transport cylinders as a solid, subliming to gas when metered into an enrichment plant.

### Enrichment

Enrichment increases the U-235 assay from 0.72% (natural) to 3-5% (light-water reactor grade). The two industrially dominant methods are the **gas centrifuge** and, historically, **gaseous diffusion**.

- **Gas centrifuge**: UF₆ gas is fed into a cylindrical rotor spinning at very high speed in a vacuum housing. Centrifugal force pushes the heavier U-238-bearing molecules toward the rotor wall, while the lighter U-235-bearing molecules concentrate near the central axis. A small temperature gradient (a heated cap and cooled bottom) drives an axial countercurrent that enriches the gas at one end and depletes it at the other. The separative work per machine is small, so machines are cascaded — product from one stage becomes feed for the next — until the target assay is reached. The unit of enrichment work is the **separative work unit (SWU)**. Producing 1 kg of 3.5%-assay enriched uranium from natural feed, while discarding a 0.3% tails assay, requires roughly 100-130 SWU of work. Centrifuge cascades are described here at the concept level only; cascade arrangement, rotor dimensions, and stage counts are not detailed.
- **Gaseous diffusion** (largely retired): UF₆ is forced under pressure through a porous membrane (the "barrier"). The lighter molecules diffuse slightly faster, producing a tiny enrichment per stage that must be repeated over a thousand stages. Energy consumption is roughly 10-20× that of centrifuges, which is why diffusion plants have been shut down almost everywhere.
- **Laser enrichment** (under development): Atomic or molecular vapor laser isotope separation (AVLIS, MLIS) selectively excites U-235 atoms or UF₆ molecules, achieving in a single step what cascade methods need many steps to reach. The technology has been demonstrated at pilot scale but is not yet deployed at commercial scale.

The output of enrichment is two streams: the **product** (enriched UF₆) and the **tails** (depleted UF₆, typically 0.2-0.4% U-235). Tails are stored in cylinders as a strategic inventory; they can be re-enriched later if economics shift. The tails assay is a key economic variable — operating to a lower tails assay (e.g., 0.2% rather than 0.3%) extracts more fissile content per tonne of natural feed but requires more SWU work per kg of product. The optimum tails assay is set by the relative cost of natural uranium feed versus enrichment work.

The separative performance of a centrifuge scales as the fourth power of the peripheral rotor velocity and is therefore exquisitely sensitive to materials and manufacturing precision. The rotor material is typically a high-strength aluminum alloy, maraging steel, or carbon-fiber composite; the bearings are magnetic or molecular-drag suspension; the housing is maintained at hard vacuum to minimize aerodynamic drag. These manufacturing demands are why centrifuge production is concentrated in a small number of facilities worldwide.

### Fuel Fabrication

Enriched UF₆ is heated in an autoclave, vaporized, and reduced with hydrogen to UF₄, then with calcium metal (or magnesium) to uranium metal, which is oxidized to uranium dioxide (UO₂) powder. The powder is pressed into cylindrical pellets (typically 8-14 mm diameter, 10-15 mm tall), sintered at 1700-1800°C in a hydrogen atmosphere to 95-97% theoretical density, and ground to a precise diameter with a 30-50 μm diametral gap inside the cladding. Pellets are loaded into zirconium-alloy tubes (Zircaloy-4 or Zirlo), which are evacuated, backfilled with helium at 1-2 MPa, and sealed with end plugs welded by resistance or TIG. The rods are assembled into square fuel assemblies (17×17 for a PWR, with 264 fuel rods and 25 guide thimbles) with spacer grids, top and bottom nozzles, and instrumentation. A 1000-MWe light-water reactor core contains roughly 150-200 fuel assemblies, replaced in thirds on an 18-24 month refueling cycle.

Criticality safety governs every step of fabrication: the slightly-enriched UO₂ is still well below the concentration needed for an uncontrolled chain reaction, but the geometry of processing vessels (limited diameter, safe-by-shape) and the avoidance of moderating materials (water, organics) in favorable configurations are rigorously enforced.

## Back End

### Spent Fuel Composition

A fuel assembly discharged at 45 GWd/t burnup has fissioned about 4-5% of its initial heavy metal atoms. The remaining composition is roughly:

- **~95-96% uranium** — mostly U-238 with about 0.8-1.0% residual U-235 (still slightly enriched relative to natural) and a small fraction of U-236 (a parasitic neutron absorber produced by neutron capture in U-235).
- **~1% plutonium** — almost entirely formed by neutron capture in U-238 followed by two beta decays (U-238 + n → U-239 → Np-239 → Pu-239). The isotopic mix is reactor-grade: roughly 55-65% fissile Pu-239 plus Pu-240, Pu-241, and Pu-242. The Pu-240 content (which emits spontaneous-fission neutrons) makes reactor-grade plutonium unsuitable for weapons use, a distinction preserved by the international safeguards regime.
- **~3-4% fission products** — the split fragments of U-235, U-238, and Pu-239 fission. These are intensely radioactive and include the principal heat emitters Cs-137 and Sr-90, each with cumulative thermal-fission yields around 6% and a 30-year half-life.
- **~0.1-0.5% minor actinides** — Np-237, Am-241, Am-243, Cm-244 — produced by successive neutron captures. These dominate the long-term (1000+ year) radiotoxicity of the spent fuel.

A freshly discharged assembly emits roughly 1-2 MW of decay heat per tonne of heavy metal. This drops to about 10 kW/t after one year of cooling and 1 kW/t after ten years. Spent fuel must therefore be handled underwater or in shielded casks at all times.

### Cooling and Storage

Discharged fuel is moved from the reactor core to an adjacent **spent fuel pool** — a deep pool of borated water that provides radiation shielding (≥3 m of water over the assemblies), decay-heat removal (forced circulation through heat exchangers), and a geometrically favorable subcritical configuration. The minimum cooling time before dry storage or reprocessing is **5 years**, established by the decay-heat and radiation-field curves. After pool cooling, fuel can be transferred to **dry cask storage** — massive steel-and-concrete casks that passively reject decay heat through natural convection. Dry cask storage is the operational default when pool capacity is exhausted.

### Reprocessing: PUREX

The PUREX (Plutonium-URanium EXtraction) process is the dominant reprocessing technology. It is a solvent-extraction operation that exploits differential solubility in an organic phase to separate uranium, plutonium, and fission products. The chemistry is described here at the flowsheet level; full plant design is outside the scope of this article and references the [solvent extraction](../chemistry/solvents.md) and [distillation column](../chemistry/distillation-column.md) infrastructure common to industrial chemistry.

1. **Shearing and dissolution**: Fuel rods are chopped into short sections inside a shielded hot cell; the UO₂ pellets dissolve in 7-10 M nitric acid (HNO₃). Zircaloy cladding hulls (the "zircaloy skeletons") are rinsed, monitored for residual uranium, and routed to hull conditioning for low-level waste disposal. The dissolver solution is filtered and clarified to remove insoluble fission products (noble metals, fuel debris).
2. **Co-decontamination**: The clarified solution is contacted with the PUREX solvent — typically **30% v/v tributyl phosphate (TBP) in kerosene or n-dodecane**. TBP forms extractable complexes with both uranium (as UO₂(NO₃)₂·2TBP) and plutonium (as Pu(NO₃)₄·2TBP, when plutonium is held in the tetravalent Pu(IV) state), while leaving the fission products in the aqueous phase. The contactors are pulsed columns or, more commonly in modern plants, banks of centrifugal contactors ([disc centrifuge](../chemistry/centrifuge.md) derivatives) that achieve high throughput in a compact shielded footprint.
3. **Partitioning**: Plutonium is selectively stripped from the loaded solvent by reducing Pu(IV) to Pu(III), which is not extractable by TBP. The reducing agent historically was U(IV) stabilized with hydrazine; modern plants increasingly use electrolytic reduction directly in the contactor. Uranium remains in the organic phase and is stripped in a subsequent section with dilute nitric acid.
4. **Purification cycles**: Each separated stream — uranium, plutonium, fission-product waste — is routed through additional extraction cycles to reach the required purity specification. The uranium product is typically >99.9% U with <10⁻⁸ Ci of alpha activity per gram (specifications vary by flowsheet). The plutonium product is converted to PuO₂ powder by oxalate precipitation and calcination.

The recovered uranium (the **reprocessed uranium** or "RepU" product stream) retains the residual U-235 enrichment and a small U-236 burden. Re-enrichment must account for U-236's parasitic absorption. The recovered plutonium can be blended with depleted or natural uranium to make **mixed-oxide (MOX) fuel** — typically 5-10% PuO₂ in UO₂ — which can substitute for roughly a third of the fresh fuel loading in a light-water reactor.

### Waste Conditioning

The high-level liquid waste (HLLW) stream from PUREX contains the fission products and minor actinides in nitric acid solution. It is concentrator-evaporated to reduce volume, then **calcined** to a dry powder or directly fed to a **vitrification** melter. Vitrification is the preferred waste form: the waste is incorporated into a borosilicate glass matrix at 1100-1200°C, poured into stainless steel canisters (typical size 430 mm diameter × 1300 mm tall, holding ~400 kg of glass with ~10-15% waste oxide loading), and sealed. A vitrified canister from a 1000-MWe reactor operating for one year corresponds to roughly 1 tonne of glass — a volume reduction of about 5× over direct spent-fuel disposal.

Spent fuel from once-through cycles is itself a candidate waste form for geological disposal, requiring only the assembly to be sealed in a copper, steel, or copper-cast iron canister. Both waste forms target isolation in a stable deep geological formation (e.g., saturated granitic basement, bedded salt, or indurated clay) with engineered barrier systems and long-term institutional controls.

## Quantitative Parameters

| Parameter | Value |
|-----------|-------|
| Natural U-235 abundance | 0.72% (atoms) |
| Reactor-grade enrichment target | 3.0-5.0% U-235 (LWR) |
| Enrichment SWU per kg of 3.5% product (0.3% tails) | 100-130 SWU |
| Reactor fuel burnup (modern LWR) | 33-60 GWd/t HM |
| Spent fuel cooling time before dry storage | ≥5 years (pool) |
| Spent fuel composition: uranium | ~95-96% |
| Spent fuel composition: plutonium | ~1% (reactor-grade) |
| Spent fuel composition: fission products | ~3-4% |
| Spent fuel composition: minor actinides | ~0.1-0.5% |
| Cs-137 cumulative yield (thermal fission of U-235) | ~6.2% |
| Sr-90 cumulative yield (thermal fission of U-235) | ~5.9% |
| Spent fuel decay heat at discharge | 1-2 MW/t HM |
| Spent fuel decay heat at 1 year | ~10 kW/t HM |
| PUREX solvent | 30% TBP in kerosene |
| PUREX dissolver solution | 7-10 M HNO₃ |
| Vitrified waste volume per GWe-year | ~1 tonne glass (~0.3 m³) |
| UO₂ pellet sintering temperature | 1700-1800°C, hydrogen atmosphere |
| LWR fuel assembly geometry | 17×17 rod array (264 fuel rods) |

## Variations

- **Once-through cycle**: Spent fuel is cooled and disposed of directly as a waste form. Simpler industrial flowsheet, no plutonium separation, but consumes more natural uranium per MWh and forecloses the energy content of the recovered fissile material. Current U.S. policy.
- **Closed cycle (PUREX/MOX)**: Spent fuel is reprocessed, plutonium is recycled as MOX (one or two passes in a light-water reactor), and uranium is recovered or stored as RepU. Uranium utilization improves by roughly 20-30%. Operated at commercial scale in France, the U.K., Russia, Japan.
- **Thorium fuel cycle**: Thorium-232 is fertile (not fissile), breeding to fissile U-233 on neutron capture. The cycle produces less long-lived transuranic waste and uses an abundant resource, but requires a fissile driver (enriched uranium or plutonium) to start and has been deployed only at pilot scale. Not covered in detail in this article.
- **MOX fuel**: Mixed-oxide (U,Pu)O₂ fuel substitutes Pu-239 for U-235 as the primary fissile isotope. Typical reloads displace a third of the fresh UO₂ fuel in a participating LWR. Fabrication requires glovebox handling of plutonium dust — the radiological controls and safeguards regime are the dominant cost driver.

## Safety

- **Criticality safety** governs every step where fissile material accumulates. Enrichment cascades, UF₆ handling, UO₂ powder processing, dissolution, and the partitioning sections of PUREX all require favorable geometry (limited diameter vessels, no favorable reflection), administrative controls on mass and concentration, and active neutron monitoring. The objective is subcriticality with margin: k-effective ≤ 0.95 in normal operation, ≤ 0.98 in credible accident sequences.
- **Radiological protection** underpins all back-end operations. PUREX plants operate behind 1-1.5 m of concrete shielding, with all process equipment handled remotely through master-slave manipulators or robotic systems. Worker doses are kept below regulatory limits by the [as low as reasonably achievable (ALARA)](../ehs/radiation-safety.md) discipline: time, distance, shielding, contamination control.
- **Fluorine and HF handling**: The conversion step uses hydrogen fluoride (extremely corrosive, severe respiratory hazard) and elemental fluorine (violently reactive with most materials). Both require dedicated process trains, [ventilation exhaust](../ehs/ventilation-exhaust.md), and emergency scrubbers.
- **Waste isolation**: The end-state of the cycle is a high-level waste form destined for geological isolation. Site selection criteria include: low groundwater flux, stable tectonics, reducing geochemical conditions, and a host rock (granite, clay, salt, or tuff) that has been stable for millions of years. Engineered barrier systems (canister, buffer, backfill) augment the natural barrier.
- **Safeguards**: Reprocessing plants are the principal safeguarded facilities in the fuel cycle — plutonium flows are measured and accounted for under international agreement. Material control and accountancy (MC&A) is a continuous operational practice, not an afterthought.

## Strengths

- Converts ~0.7% natural fissile content to reactor-usable 3-5% — the gateway step for the dominant reactor fleet
- Closed-cycle recovery reduces natural uranium demand by 20-30% and reduces the volume of conditioned waste by roughly 5×
- PUREX is a mature, well-characterized flowsheet that has operated at commercial scale for over 60 years
- Vitrified waste form has demonstrated leach rates orders of magnitude below spent fuel
- Cycle produces the [radioisotope feedstocks](./nuclear-fission.md) for medical and industrial isotopes as a co-product of fission-product separation

## Weaknesses

- Capital intensity of every step is extreme: enrichment plants and reprocessing facilities are multi-billion-dollar investments
- Long licensing timelines (5-15 years for a new facility) reflect the regulatory burden of handling kilogram-to-tonne quantities of fissile material
- Waste isolation remains politically and technically contested: no country has yet commissioned a geological repository for high-level waste at scale, though several programs (Finnish Onkalo, French Cigéo) are advancing
- Proliferation sensitivity of reprocessing: the plutonium product stream is safeguarded, but the existence of separated plutonium in the civil cycle is a recurring policy debate
- Decay-heat burden on the back end: every spent fuel assembly must be actively cooled for years before dry storage or reprocessing

## Quality Control

- **Ore grade**: Drill-core assays define the minable resource. Run-of-mine feed to the mill is monitored by radiometric (gamma) and chemical assays. Target: 0.05-0.5% U₃O₈ (open-pit), 0.1-1% (underground). Below economic cutoff, the material is waste rock.
- **Yellowcake assay**: Performed by X-ray fluorescence or titrimetric (Davies-Gray) method. Typical specification: 75-85% U₃O₈, with limits on impurities (Mo, V, As, halides) that would poison downstream conversion.
- **UF₆ purity**: Verified by infrared spectrometry and mass spectrometry for the conversion-plant product. Limits on HF, freon substitutes, and volatile metal fluorides are enforced because impurities corrode centrifuge internals and shift assay measurements.
- **Enrichment assay**: Product and tails streams are sampled by mass spectrometry (thermal ionization or ICP-MS). Target: 3.0-5.0% U-235 in product, 0.2-0.4% in tails. Tighter tolerances (±0.05%) are achievable with cascade feedback control.
- **Fuel pellet density**: 95-97% of theoretical (10.96 g/cm³ for UO₂). Measured by geometric displacement (Archimedes) on a statistical sample. Below 95%: fission-gas release swells the pellet and stresses the cladding. Above 98%: pellet is brittle and prone to thermal-stress cracking.
- **Pellet microstructure**: Grain size 8-25 μm (sintering control), porosity uniformly distributed. Large pores trap fission gas and reduce swelling.
- **Cladding integrity**: Each finished rod is helium-leak-tested to <10⁻⁹ Pa·m³/s, gamma-scanned for pellet gaps and pellet-stack length, and dimensionally inspected for diameter, bow, and surface scratches.
- **Assembly inspection**: Spacer-grid spring forces, guide-thimble straightness, and nozzle seating are checked on every assembly before release.
- **Spent fuel cooling time**: Each assembly's cooling time is tracked by core-follow software and verified against discharge records. A fuel assembly with less than the minimum cooling time cannot be loaded into a dry cask.
- **PUREX decontamination factors**: Uranium product decontamination factor from fission products must exceed 10⁶; plutonium product DF ≥ 10⁷. Verified by sampling each purification cycle.
- **Vitrified waste quality**: Canister product is non-destructively inspected by gamma scanning (for cesium uniformity), by measurement of the glass pour temperature and viscosity, and by periodic core sampling of a witness canister for durability testing (PCT, MCC-1 leach tests).

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Yellowcake U₃O₈ assay below specification | Incomplete leach, low oxidant, or high impurity load in pregnant liquor | Increase oxidant dosing; tighten ion-exchange or solvent-extraction regeneration; monitor precipitation pH |
| UF₆ cylinder pressure rise during storage | Slow ingress of moisture forming HF and UO₂F₂ | Transfer to vented cylinder; restore process dryness (dry-air purge on connections); reject cylinder if corrosion is advanced |
| Enrichment product assay drift | Cascade feedback control mismatched to feed rate or tails assay | Re-balance cascade (adjust headers, reflux ratios); recalibrate mass-spec sampling; verify no interstage leakage |
| Fuel pellet density outside 95-97% band | Sintering temperature drift, atmosphere contamination, or powder precursor off-spec | Recalibrate furnace temperature; verify hydrogen atmosphere dew point; check powder BET surface area and press forming parameters |
| Cladding tube weld defect | Tungsten inclusion or lack of fusion in end-plug weld | 100% radiographic inspection of welds; reject and rework affected rods; verify welding parameters (current, travel speed, gas flow) |
| Spent fuel assembly bow exceeds limit | Creep under neutron fluence and differential irradiation growth | Measure assembly bow before cask loading; re-can bowed assemblies into guide sleeves or process them early in reprocessing |
| PUREX first-cycle DF drops | TBP degradation from radiolysis or nitration; solvent wash inadequate | Increase solvent wash frequency; monitor solvent viscosity and U/Pu retention; replace solvent if DBP (dibutyl phosphoric acid) buildup exceeds specification |
| Vitrified canister shows cesium hot-spot | Pouring inhomogeneity or glass crystallization during cooling | Reduce pour rate; verify melter temperature uniformity; quarantine affected canister for rework or overpacking |

## Process Description

The nuclear fuel cycle is not a single plant but a chain of facilities, each owned and operated as an independent business with its own workforce and license. The cycle is described here as an integrated flowsheet; in practice, material moves between facilities in standardized transport packages (Type 30B or 48Y cylinders for UF₆, TN or NAC casks for spent fuel, MOX truck casks for finished plutonium-bearing fuel).

1. **Mine the ore** by open-pit, underground, or ISL methods. The product is either run-of-mine rock (conventional) or a uranyl-bearing leachate (ISL), each routed to a mill.
2. **Mill the ore** to yellowcake: crush, grind, leach, ion-exchange or solvent-extraction purify, precipitate, dewater, and roast. The product is U₃O₈ powder in 200-litre drums. Tailings go to an engineered management facility.
3. **Convert yellowcake to UF₆**: reduce U₃O₈ to UO₂ with hydrogen, hydrofluorinate to UF₄ with HF, and fluorinate to UF₆ with F₂. The product is liquefied under pressure into transport cylinders.
4. **Enrich UF₆** in a centrifuge cascade from 0.72% to 3.0-5.0% U-235, producing enriched product and depleted tails in separate cylinders. Tails are held in storage.
5. **Fabricate reactor fuel**: convert enriched UF₆ back to UO₂ powder, press into pellets, sinter at 1700-1800°C in hydrogen, grind to final diameter, load into Zircaloy cladding, seal, leak-test, and assemble into finished fuel assemblies.
6. **Irradiate** the assemblies in the reactor core for 3-6 years, reaching discharge burnup of 33-60 GWd/t HM.
7. **Discharge and cool**: transfer spent assemblies to a spent fuel pool, cool for ≥5 years under borated water with active heat removal.
8. **(Once-through path)**: Transfer cooled assemblies to dry cask storage, awaiting a geological repository. Cycle ends here.
9. **(Closed-cycle path)**: Reprocess the cooled fuel through PUREX — shear, dissolve in nitric acid, co-extract U+Pu into TBP/kerosene, partition plutonium by reduction, strip uranium, purify both streams through additional cycles.
10. **Condition the waste**: Concentrate the fission-product + minor-actinide raffinate, calcine, vitrify into borosilicate glass in stainless steel canisters. Cool the canisters in forced-air vaults for 20-50 years before geological emplacement.
11. **Recycle the products**: Re-enrich the reprocessed uranium (accounting for U-236 burden) and refabricate as UO₂ fuel, or blend recovered plutonium with depleted uranium to make MOX. Both streams return to step 5 or 6.

## Fission Product and Actinide Yields

The radiological character of the back end is set by the fission-product and actinide inventory of the spent fuel. The principal contributors (per tonne of typical LWR spent fuel at 45 GWd/t burnup) are tabulated below. Cumulative yields are for thermal fission of U-235 unless otherwise noted.

| Nuclide | Half-life | Cumulative yield | Principal source | Radiological role |
|---------|----------|------------------|------------------|-------------------|
| Cs-137 | 30.0 yr | ~6.2% | U-235 fission | Dominant decay-heat and gamma source at 1-100 yr |
| Cs-134 | 2.06 yr | — (activation of Cs-133) | Neutron capture | Significant gamma source in first decade |
| Sr-90 | 28.8 yr | ~5.9% | U-235 fission | Bone-seeking beta source; decay-heat contributor |
| Tc-99 | 211 kyr | ~6.1% | U-235 fission | Long-lived mobile groundwater contaminant |
| I-129 | 15.7 Myr | ~0.7% | U-235 fission | Long-lived thyroid dose contributor |
| Pu-239 | 24.1 kyr | bred in U-238 | n capture in U-238 | Recoverable fissile material for MOX |
| Pu-240 | 6.56 kyr | bred in Pu-239 | n capture in Pu-239 | Spontaneous-fission neutron source; safeguards marker |
| Am-241 | 432 yr | decayed from Pu-241 | Pu-241 decay | Dominant long-term alpha and neutron source |
| Np-237 | 2.14 Myr | bred in U-236 | n capture in U-236 | Target material for Pu-238 production in special irradiations |

This inventory is what the back end is designed to manage. Cs-137 and Sr-90 dominate the thermal load for the first 100 years; the actinides dominate the long-term (1000+ year) radiotoxicity. The choice between once-through and reprocessing is, at root, a choice about which inventory goes to the repository as spent fuel and which is partitioned into separate waste forms.

## Scaling Notes

The fuel cycle does not scale down gracefully. A minimum-viable enrichment plant of a few hundred thousand SWU per year, a fuel fabrication facility of a few tens of tonnes per year, and a reprocessing plant of a few hundred tonnes per year are all that a single 1000-MWe reactor requires — but each is a dedicated industrial facility with its own workforce, regulatory regime, and capital base. Small modular reactors (SMRs) and advanced reactor concepts partially relax the enrichment requirement (some designs use natural or lightly-enriched fuel) but do not eliminate the fuel cycle. For a bootstrap context, the implication is that nuclear fission arrives only after a substantial industrial base exists: pressure-vessel metallurgy, zirconium refining, fluorine chemistry, centrifuge manufacturing, and a licensed radiological workforce must all be in place before the cycle can operate at any useful scale.

## References

- [Nuclear Fission Power](./nuclear-fission.md) — parent capability; reactor physics, neutronics, power conversion
- [Mining Extraction](../mining/extraction.md) — uranium mining methods and orebody development
- [Chemistry](../chemistry/index.md) — bulk acids, fluorine, solvents, distillation infrastructure that the fuel cycle depends on
- [Centrifuge](../chemistry/centrifuge.md) — gas centrifuges for enrichment, contactor centrifuges for PUREX
- [Solvents](../chemistry/solvents.md) — TBP/kerosene solvent extraction chemistry
- [Distillation Column](../chemistry/distillation-column.md) — separation train infrastructure
- [Electrolysis](../chemistry/electrolysis.md) — fluorine gas production for conversion to UF₆
- [Radiation Safety](../ehs/radiation-safety.md) — radiological protection regime for back-end operations
- [Waste Management](../ehs/waste-management.md) — tailings, low-level, and intermediate waste disposition
- [Iron & Steel](../metals/iron-steel.md) — pressure-vessel and process equipment metallurgy

---

*Part of the [Bootciv Tech Tree](../index.md) • [Energy](./index.md) • [All Domains](../index.md)*
