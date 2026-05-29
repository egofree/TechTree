# Specialty Metals for Semiconductor Interconnects & Barrier Layers

> **Node ID**: metals.specialty-semiconductor
> **Domain**: [Metals](./index.md)
> **Dependencies**: `chemistry`, [`gas-handling.vacuum`](../gas-handling/vacuum.md), `metals`, [`metals.refractory-specialty`](refractory-specialty.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 40-80
> **Outputs**: TiN hard masks, Ti diffusion barriers, W contact plugs, Mo gate electrodes, Cu damascene interconnects, Mo/Cu heat sinks


Four metals — titanium (Ti), tungsten (W), molybdenum (Mo), and copper (Cu) — form the structural and electrical backbone of every GPU interconnect stack. Titanium nitride (TiN) serves as the hard mask for dual damascene patterning and as a secondary diffusion barrier. Tungsten fills contact vias and through-silicon vias (TSVs) by CVD from WF₆. Molybdenum provides gate electrodes at advanced nodes where poly-Si resistance is prohibitive, and Mo/Cu heat sinks extract waste heat from multi-hundred-watt GPU dies. Copper, deposited by electroplating into damascene trenches, carries 10-50 km of wiring per metal layer across 10-15 layers in a modern GPU. Without these four metals, interconnect resistance and RC delay would render any sub-100 nm chip non-functional.

Extraction of bulk Ti (Kroll process) and bulk W/Mo (powder metallurgy, hydrogen reduction) are covered in [Non-Ferrous Metals](non-ferrous.md) and [Refractory Metals](refractory-metals.md). This document covers the semiconductor-grade processing and thin-film applications that place them on the GPU critical path.


## Properties Relevant to Semiconductor Use

| Property | Value | Significance |
|----------|-------|--------------|
| Atomic number | 22 | Light transition metal |
| Melting point | 1668°C | Thermally stable through BEOL |
| Density | 4.51 g/cm³ | Lightweight — useful for aerospace too |
| Resistivity (α-Ti) | 42-55 μΩ·cm | Higher than Cu but acceptable for barriers |
| TiN resistivity | 20-250 μΩ·cm (depending on stoichiometry) | Hard mask and ARC layer |
| TiO₂ dielectric constant | 80-100 (rutile) | High-k dielectric candidate |
| TiO₂ bandgap | 3.0-3.2 eV | Transparent to visible light |
| CTE | 8.6 × 10⁻⁶/°C | Closer to Si than most metals |

## Kroll Process (Bulk Titanium — Summary)

Bulk titanium production via the Kroll process is detailed in [Non-Ferrous Metals](non-ferrous.md). Key semiconductor-relevant points:

1. **Chlorination**: TiO₂ + 2Cl₂ + C → TiCl₄ + CO₂ at 800-1000°C. TiCl₄ is a volatile liquid (bp 136°C) purified by fractional distillation to 99.9%+ purity.
2. **Magnesium reduction**: TiCl₄ + 2Mg → Ti + 2MgCl₂ at 800-850°C under argon atmosphere. Produces porous "titanium sponge."
3. **Sponge crushing and melting**: Crush sponge, press into electrodes, vacuum arc remelt (VAR) 2-3 times to produce ingots. Purity: 99.5-99.7% Ti (Grade 1-4).

**Semiconductor-grade Ti**: For sputtering targets, further purification by electron beam melting (EBM) under high vacuum (<10⁻³ Pa) achieves 99.95-99.99% Ti. Key impurity limits: O <300 ppm, Fe <50 ppm, C <50 ppm. Interstitial oxygen increases resistivity and embrittles the metal — must be minimized.

## TiN Hard Mask (PVD)

**Purpose**: In dual damascene Cu patterning, the dielectric stack (SiO₂/Si₃N₄ or low-k material) must be etched with precise feature profiles. A hard mask layer of TiN (100-200 nm) provides etch selectivity >10:1 over SiO₂ in fluorocarbon plasmas (CF₄, C₄F₈), whereas photoresist alone provides only ~2:1 selectivity. Without TiN hard masks, deep dielectric trenches cannot be patterned without excessive resist erosion.

**Deposition — reactive DC magnetron sputtering**: Sputter a Ti target in Ar/N₂ atmosphere. Process: Ar flow 10-30 sccm, N₂ flow 2-10 sccm, pressure 2-8 mTorr, DC power 3-15 kW, substrate temperature 200-400°C. The N₂ partial pressure controls TiN stoichiometry: under-stoichiometric TiNₓ (x < 1.0) is metallic gold, stoichiometric TiN₁.₀ is golden-yellow, over-stoichiometric TiNₓ (x > 1.0) is brown and insulating. For hard mask use, stoichiometric or slightly over-stoichiometric TiN is preferred (harder, better etch selectivity). Deposition rate: 5-20 nm/min. Film stress: compressive, 0.5-3 GPa (controllable by bias voltage).

**Film properties**: Hardness 18-22 GPa (Vickers), elastic modulus 400-500 GPa, density 5.2-5.4 g/cm³. Optical: golden color, reflectivity 60-80% in visible range — acts as anti-reflective coating (ARC) for photolithography at specific thicknesses (quarter-wave at exposure wavelength). For 193 nm ArF lithography, 25-35 nm TiN provides optimal ARC performance, reducing standing wave effects in photoresist.

**Etch selectivity**: TiN etches in Cl₂/BCl₃ plasma at 30-80 nm/min, vs. SiO₂ at 200-500 nm/min in CF₄/C₄F₈ plasma. During dielectric etch, the TiN hard mask erodes <10% while the dielectric is fully cleared. After dielectric etch, the TiN hard mask is stripped in wet H₂O₂/H₂SO₄ (piranha) or dry Cl₂ plasma.

## Ti/TiN Diffusion Barrier (Alternative to TaN/Ta)

TiN serves as a diffusion barrier for aluminum interconnects (250 nm node and above) and as an adhesion/barrier layer for tungsten plug fill. While TaN/Ta has replaced TiN as the primary Cu barrier (see [Refractory & Specialty Metals](refractory-specialty.md)), Ti/TiN remains critical for:

1. **W plug barrier**: 5-20 nm TiN lines contact via sidewalls before W CVD fill. TiN prevents WF₆ from reacting with the underlying Si or silicide, which would form volatile silicon fluorides (SiF₄) and cause "via poisoning."
2. **Al interconnect barrier**: In older nodes (>250 nm) using Al metallization, TiN (50-100 nm) prevents Al-Si interdiffusion and Al spiking into junctions.
3. **Adhesion promoter**: Ti (5-10 nm) under TiN improves adhesion to SiO₂ and low-k dielectrics. The Ti reacts with surface oxide to form Ti-O bonds.

**TiN barrier performance**: Time-to-failure in BTS test at 350°C, 1 MV/cm: TiN (10 nm) fails in <10 minutes for Cu barrier application (vs. TaN at >60 minutes). This is why TaN replaced TiN for Cu damascene — Cu diffuses through grain boundaries in polycrystalline TiN at temperatures >250°C. However, for W barrier applications where the filled metal has low diffusivity, TiN is perfectly adequate.

## TiO₂ High-k Dielectric

**Properties**: TiO₂ in rutile phase has dielectric constant ε_r = 80-100 (one of the highest simple binary oxides). Thin films deposited by ALD (TiCl₄ + H₂O at 150-300°C) or MOCVD (TTIP — titanium tetraisopropoxide, Ti(OiPr)₄ + O₂ at 250-450°C) achieve ε_r = 40-80 for amorphous/nanocrystalline films.

**DRAM capacitor application**: TiO₂ and its doped variants (TiO₂:Al, TiO₂:La) are leading candidates for MIM (metal-insulator-metal) capacitors in DRAM cells at <20 nm technology nodes. Equivalent oxide thickness (EOT) targets: <0.5 nm with leakage <10⁻⁷ A/cm² at 1V. The high ε_r allows physically thicker films (reducing leakage) while maintaining small EOT.

**Challenge**: TiO₂ crystallizes at relatively low temperatures (>400°C for rutile), and crystalline TiO₂ has higher leakage than amorphous films. Doping with Al₂O₃ or SiO₂ suppresses crystallization to >700°C, maintaining amorphous structure through BEOL thermal budgets.


## Properties Relevant to Semiconductor Use

| Property | Value | Significance |
|----------|-------|--------------|
| Melting point | 3422°C | Highest melting point metal |
| Resistivity | 5.6 μΩ·cm | Higher than Cu (1.68) or Al (2.65) but acceptable for short plugs |
| Stress (CVD W on Si) | Tensile, 0.5-1.5 GPa | Must manage to avoid wafer warpage |
| Density | 19.25 g/cm³ | Very dense |
| Thermal conductivity | 173 W/(m·K) | Good thermal conductor |
| CTE | 4.5 × 10⁻⁶/°C | Close match to Si (4.1) |
| WF₆ boiling point | 17°C | Gas at room temperature — ideal for CVD |

## WF₆ — Tungsten Hexafluoride

**Production**: WF₆ is the universal tungsten CVD precursor. Produced by direct fluorination of tungsten metal powder: W + 3F₂ → WF₆ at 250-350°C. F₂ gas is generated by electrolysis of KF·2HF (see [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md)). WF₆ is a colorless gas (bp 17°C, mp -0.5°C) stored as a liquefied compressed gas in nickel or Monel cylinders. Purity: 99.99% WF₆ with impurity limits: SiF₄ <10 ppm, HF <50 ppm, MoF₆ <10 ppm, UF₆ <1 ppm (uranium contamination from ore). WF₆ is extremely corrosive and reacts violently with moisture: WF₆ + 3H₂O → WO₃ + 6HF. All piping, valves, and regulators must be nickel, Monel, or PTFE-lined stainless steel.

**Supply**: Global WF₆ production: ~25,000-30,000 tonnes/year. Price: $30-60/kg. Major producers: Linde, Air Products, Air Liquide, Central Glass (Japan). Semiconductor-grade WF₆ represents ~40% of demand by value but <10% by volume (remaining demand is for WC-Co hardfacing and CVD coating of cutting tools).

## W CVD Plug Fill (Blanket + Etchback)

**Process flow for contact via fill**:

1. **Via etch**: Pattern and etch contact vias (0.1-0.5 μm diameter, AR 3-8) through inter-layer dielectric (ILD) to expose source/drain or gate silicide contacts.

2. **Barrier/liner deposition**: Deposit 5-15 nm TiN by PVD or ALD as the via liner. The TiN prevents WF₆ from attacking the underlying silicide (see TiN barrier above). For sub-45 nm nodes, ALD TiN (TiCl₄ + NH₃ at 300-400°C) provides conformal coverage in high-AR vias where PVD cannot reach.

3. **Nucleation layer — SiH₄ reduction**: Before bulk W fill, deposit a thin (20-50 nm) nucleation layer by silane reduction: WF₆ + 2SiH₄ → W + 2SiF₄ + 4H₂ at 300-350°C, 0.5-5 Torr. This produces a smooth, continuous W film that serves as a seed for the bulk fill. Without the nucleation layer, the subsequent H₂ reduction deposits rough, non-continuous W that encloses voids.

4. **Bulk fill — H₂ reduction**: WF₆ + 3H₂ → W + 6HF at 350-450°C, 10-100 Torr. Hydrogen reduces WF₆ on the growing W surface. Deposition rate: 0.5-2.0 μm/min (fast — one of the highest CVD deposition rates in semiconductor manufacturing). The reaction is highly exothermic and self-limiting: heat from the reaction increases local deposition rate, which is controlled by WF₆ mass transport. Film properties: resistivity 7-12 μΩ·cm (bulk W is 5.6), density 15-17 g/cm³ (bulk 19.25 — CVD W contains 1-3 at.% fluorine trapped in grain boundaries, increasing resistivity). Grain size: 0.1-1.0 μm columnar.

5. **Blanket W overfill**: The W deposits on all surfaces uniformly (conformal), completely filling the vias and continuing to grow over the field region. Total blanket W thickness: 0.5-2.0 μm.

6. **Etchback — W CMP**: Remove blanket W by chemical mechanical planarization (CMP). W CMP slurry: potassium ferricyanide K₃Fe(CN)₆ (0.5-5% wt) as oxidizer (W + K₃Fe(CN)₆ → WO₃ + K₄Fe(CN)₆, then mechanical abrasion of WO₃ by alumina abrasive, 50-200 nm particles, 1-3% wt), pH 8-11. Polish rate: 200-500 nm/min. Selectivity W:TiN:SiO₂ = 20:1:∞ (TiN acts as CMP stopping layer). Endpoint: polish stops on TiN barrier, leaving W only in the vias. Dishing: <30 nm for 0.2 μm contacts.

**Alternative: W etchback by RIE**: Before CMP was available, blanket W was removed by reactive ion etching in SF₆/Cl₂ plasma. RIE etchback produces more dishing and is less planar — CMP is the modern standard.

## W Fill for Through-Silicon Vias (TSVs)

**3D packaging**: In advanced GPU packaging (HBM — high bandwidth memory), multiple DRAM die are stacked vertically and interconnected by TSVs — vertical metal columns passing through the silicon substrate. TSVs are 5-10 μm diameter, 50-150 μm deep (AR 10-30), filled with tungsten or copper.

**W TSV fill**: For TSVs with AR >10, even CVD W has difficulty filling without voids. Process modifications: (1) Pulse-pressure CVD: alternate between 10 Torr (deposition) and 0.1 Torr (evacuation of HF byproduct) to prevent gas-phase nucleation and ensure bottom-up fill. (2) Subatmospheric CVD (SACVD): operate at 50-200 Torr with higher WF₆ flow to enhance mass transport into deep features. W TSV resistance: 0.05-0.5 Ω per via (5 μm diameter, 50 μm deep). Cu TSVs have lower resistance (0.01-0.1 Ω) but require more complex barrier/seed/electroplating processes.

**TSV keep-out zone**: Due to CTE mismatch between W (4.5 ppm/°C) and Si (4.1 ppm/°C), thermal cycling induces mechanical stress in the silicon surrounding the TSV. This stress affects carrier mobility in nearby transistors. Keep-out zone: 5-20 μm from TSV edge where no transistor should be placed. W TSVs have a smaller keep-out zone than Cu TSVs because W's CTE is closer to Si than Cu's CTE (16.5 ppm/°C).

## W Film Stress Management

CVD W films are inherently tensile (0.5-1.5 GPa), which causes wafer bowing and can crack fragile low-k dielectrics. Stress reduction techniques:

1. **Stress-relieved W**: Alternate H₂ reduction with SiH₄ reduction steps. SiH₄-derived W is compressive (-0.5 to -1.0 GPa), offsetting the tensile stress. Net stress: ±0.2 GPa (near-zero).
2. **Low-stress W**: Deposit at lower temperature (300°C vs. 450°C) with higher SiH₄/WF₆ ratio. Produces W-Si alloy (1-5 at.% Si) with compressive stress.
3. **Post-deposition anneal**: Rapid thermal anneal at 600-800°C in N₂/H₂ for 30-60s. Recrystallization and grain growth reduce tensile stress by 30-50%.


## Properties Relevant to Semiconductor Use

| Property | Value | Significance |
|----------|-------|--------------|
| Melting point | 2623°C | Refractory — stable through processing |
| Resistivity | 5.3 μΩ·cm | Low — comparable to W |
| CTE | 4.8 × 10⁻⁶/°C | Close match to Si (4.1) — excellent for bonding |
| Thermal conductivity | 138 W/(m·K) | Good thermal spreader |
| Work function | 4.6-4.9 eV | Tuneable — suitable for gate electrodes |
| Density | 10.22 g/cm³ | Moderate |

## Mo Sputtering Target Manufacturing

Bulk Mo production from molybdenite ore (MoS₂) is covered in [Refractory Metals](refractory-metals.md). For semiconductor applications, the critical step is producing high-purity sputtering targets:

**Purification to semiconductor grade**: Mo powder (99.5-99.9% from standard reduction) is further purified by: (1) Electron beam melting under high vacuum (<10⁻³ Pa) at 2800-3200°C — volatile impurities (Fe, Cu, Ni, K, Na) evaporate. Multiple melt passes (2-4) achieve 99.95-99.99% Mo. (2) Zone refining for ultra-high purity (5N-6N, 99.999-99.9999%) — a molten zone passes along a Mo rod, sweeping impurities to one end.

**Target fabrication**: Forge purified Mo ingot at 1000-1200°C, cross-roll to slab (6-25 mm thick), anneal at 1100-1300°C for recrystallization. Machine to target dimensions: 300 mm × 300 mm × 6-12 mm for 300 mm wafer tools, or cylindrical 380 mm diameter × 12 mm. Grain size: 50-150 μm equiaxed. Surface roughness: Ra <0.4 μm. Bond to Cu backing plate (OFHC copper, 25-40 mm thick) by diffusion bonding or brazing (Cu-Ag eutectic at 779°C).

**Target purity requirements**: For gate electrode applications at sub-10 nm nodes: Mo >99.97%, Fe <10 ppm, Ni <5 ppm, Cu <5 ppm, O <50 ppm, N <30 ppm, C <30 ppm, K <1 ppm, U/Th <1 ppb each (alpha particle emitters cause soft errors in SRAM). Radioactive impurity control is the most challenging specification — U and Th are present in Mo ore at 1-10 ppm and must be reduced to ppb levels.

## Mo Gate Electrodes for Advanced Nodes

**Why Mo replaces poly-Si at sub-22 nm**: Traditional polysilicon gate electrodes have sheet resistance of 10-100 Ω/sq at gate lengths >100 nm. Below 22 nm gate length, the poly-Si line width shrinks to ~20 nm and the gate electrode resistance exceeds 500 Ω/sq — prohibitive for high-frequency operation. Metal gate electrodes (Mo, TiN, TaN, or work-function-tuned alloys) provide sheet resistance <5 Ω/sq.

**Work function engineering**: The gate electrode's work function must match the threshold voltage requirement. NMOS requires work function ~4.1-4.3 eV, PMOS requires ~4.9-5.1 eV. Pure Mo (Φ = 4.6-4.9 eV) is close to PMOS range. For NMOS, Mo is alloyed with Ta or nitrogen-doped to lower work function: MoNₓ (x = 0.1-0.3) achieves Φ = 4.2-4.4 eV.

**Gate-last (replacement gate) process**: In the gate-last approach (used by Intel, TSMC at sub-22 nm): (1) Build transistor with sacrificial poly-Si gate and high-k dielectric (HfO₂). (2) Complete source/drain formation and ILD deposition. (3) CMP back to expose the sacrificial gate. (4) Remove poly-Si by wet etch (TMAH or H₂O₂-based). (5) Deposit work-function-tuned Mo (or Mo alloy) by ALD or CVD to fill the gate cavity. (6) CMP to remove excess metal.

**Mo ALD**: MoCl₅ + H₂ at 400-500°C, or Mo(CO)₆ at 150-250°C. ALD Mo achieves conformal fill in high-AR gate cavities (AR 5-15) with resistivity 15-30 μΩ·cm (higher than bulk Mo due to carbon and chlorine contamination, but acceptable for short gate lengths). Film thickness: 5-30 nm.

## Mo Heat Sinks and Thermal Management

**GPU thermal challenge**: A high-end GPU die (800 mm², 300-450 W) generates heat flux of 40-60 W/cm². The thermal interface between die and heat spreader must conduct this heat with minimal temperature drop. Mo and Mo-Cu composites provide this function.

**Mo heat spreader**: Pure Mo (thermal conductivity 138 W/m·K, CTE 4.8 ppm/°C) is used as a heat spreader base that closely matches the CTE of silicon (4.1 ppm/°C). Unlike copper (CTE 16.5 ppm/°C), Mo does not induce excessive thermal stress on the die during thermal cycling (-40°C to +125°C). Mo heat spreaders: 25-100 mm × 25-100 mm × 1-5 mm, lapped to <1 μm flatness, nickel-gold plated for solderability.

**Mo-Cu composite (infiltrated)**: Mo-Cu composites combine Mo's low CTE with Cu's high thermal conductivity. Manufacturing: press Mo powder to 40-60% density, sinter at 1400-1600°C, infiltrate with molten Cu at 1150-1300°C in H₂ atmosphere. Common grades: Mo-15Cu (CTE 7.0 ppm/°C, k = 155 W/m·K), Mo-30Cu (CTE 8.5 ppm/°C, k = 185 W/m·K). The CTE can be precisely tuned by adjusting the Mo/Cu ratio to match GaAs (6.9 ppm/°C) or alumina (7.2 ppm/°C) substrates.

**Comparison with Cu-Mo-Cu cladding**: Tri-layer Cu/Mo/Cu laminate (Cu outer, Mo core) provides in-plane thermal conductivity >200 W/m·K with through-thickness CTE of 5-7 ppm/°C. Used for RF power amplifier substrates and lid assemblies for flip-chip BGA packages.


## Properties Relevant to Semiconductor Use

| Property | Value | Significance |
|----------|-------|--------------|
| Resistivity (bulk) | 1.68 μΩ·cm | Lowest of all non-precious metals |
| Resistivity (damascene) | 2.0-2.5 μΩ·cm | Higher due to surface/grain boundary scattering |
| Melting point | 1085°C | Lower than W/Mo but adequate for BEOL |
| Thermal conductivity | 401 W/(m·K) | Highest of all metals except Ag |
| CTE | 16.5 × 10⁻⁶/°C | Mismatch with Si — requires barrier |
| Electromigration activation energy | 0.7-1.0 eV | Higher than Al (0.5-0.6 eV) — better EM life |
| Cu diffusivity in SiO₂ | ~10⁻¹⁴ cm²/s at 400°C | Rapid — absolutely requires barrier |

Bulk copper extraction and electrolytic refining are covered in [Copper & Bronze Production](copper-bronze.md). Semiconductor-grade copper for electroplating is discussed below.

## Dual Damascene Process

The dual damascene process is the defining interconnect technology for sub-250 nm ICs. It simultaneously forms trenches (for wire routing) and vias (for vertical connections between layers) in a single metal fill step, avoiding the via misalignment problem of subtractive Al etching.

**Process flow (single damascene layer)**:

1. **Dielectric deposition**: Deposit inter-metal dielectric (IMD) stack — SiO₂ (k=3.9), FSG (fluorosilicate glass, k=3.5), or low-k carbon-doped oxide (k=2.5-3.0) by PECVD at 300-400°C. Total thickness: 0.3-1.0 μm per layer.

2. **Etch stop and hard mask**: Deposit Si₃N₄ etch stop (20-50 nm) and TiN hard mask (50-150 nm) by PVD.

3. **Via-first dual damascene lithography**: (a) Pattern via holes using 193 nm ArF lithography. (b) Etch vias through the upper portion of the IMD, stopping on Si₃N₄ etch stop. (c) Apply second lithography pattern for trenches. (d) Etch trenches through the remaining IMD. (e) Remove Si₃N₄ etch stop at via bottom by H₃PO₄ wet etch or CHF₃ plasma.

4. **Barrier/liner deposition**: Deposit TaN/Ta barrier (2-10 nm) by iPVD (see [Refractory & Specialty Metals](refractory-specialty.md)). The barrier lines both trench bottoms/sidewalls and via sidewalls.

5. **Cu seed layer**: Deposit 50-200 nm Cu seed layer by PVD (ionized sputtering). The seed must be continuous through the entire trench and via — any breaks cause voids during electroplating. Step coverage in high-AR features is the critical limitation. At sub-22 nm nodes, the combined barrier + seed consumes 40-60% of the trench width, leaving insufficient cross-section for Cu fill — this drives research into Ru/Cu direct-plating and Co fill.

6. **Cu electroplating (ECP)**: Fill trenches and vias by electroplating from CuSO₄/H₂SO₄ electrolyte. See detailed process below.

7. **Cu CMP**: Remove overburden Cu and barrier by CMP. See detailed process below.

8. **Capping layer**: Deposit Si₃N₄ or SiC(N) cap (30-50 nm) by PECVD to seal Cu surface and prevent oxidation. Optional: CoWP or CuMn self-forming barrier capping layer for electromigration improvement.

**Repeat** for each metal layer. A modern GPU has 10-15 metal layers, each requiring the full dual damascene cycle.

## Cu Electroplating (Electrochemical Deposition)

**Plating bath chemistry**:

| Component | Concentration | Function |
|-----------|---------------|----------|
| CuSO₄·5H₂O | 40-100 g/L (0.16-0.4 M) | Cu²⁺ source |
| H₂SO₄ | 50-100 g/L (0.5-1.0 M) | Conductivity, pH control |
| HCl | 50-100 ppm Cl⁻ | Brightener activator, anode corrosion |
| PEG (polyethylene glycol) | 100-500 ppm | Suppresses plating at surface, promotes bottom-up fill |
| SPS (bis-(3-sulfopropyl) disulfide) | 1-10 ppm | Accelerator — adsorbs on Cu surface, enhances plating in recessed features |
| Janus Green B or Leveler | 0.1-5 ppm | Leveler — suppresses bump formation at feature openings |

**Bottom-up fill mechanism (superconformal plating)**: The key to void-free fill of high-AR trenches (AR 3-10) is the interplay of accelerator (SPS) and suppressor (PEG). Initially, PEG-Cl⁻ forms a suppressing film on all Cu surfaces, reducing plating rate. As plating proceeds from the bottom of the trench, the trench bottom surface area shrinks while the accelerator (SPS) concentrates — the accelerator/surface-area ratio increases at the bottom, locally accelerating plating. This positive feedback produces "bottom-up" or "superconformal" fill where the trench fills from the bottom up faster than the field region, eliminating voids. Plating conditions: DC current 5-30 mA/cm², temperature 20-30°C, agitation by eddy flow or cathode rotation at 10-50 rpm.

**Plating equipment**: Fountain-type plating cell (cup plater) with Cu phosphorous anode (Cu + 0.03-0.06% P — the phosphorus prevents anode sludge formation). Anode-cathode gap: 20-50 mm. Cell current: 5-50 A for 300 mm wafers. Wafer rotation: 10-50 rpm. Filtration: 0.02 μm absolute filter for bath purity. Plating uniformity: ±3-5% across 300 mm wafer.

**Post-plating anneal**: After plating, anneal at 200-300°C for 30-60 minutes in N₂/H₂. This recrystallizes the as-plated Cu (fine-grained, ~50 nm) to large grains (0.5-5 μm) that reduce resistivity from 2.5-3.0 μΩ·cm (as-plated) to 1.8-2.2 μΩ·cm (annealed). The large grain structure also improves electromigration resistance by reducing grain boundary diffusion paths.

## Cu CMP (Chemical Mechanical Planarization)

**Purpose**: Remove Cu overburden (0.5-2.0 μm thick) and barrier (TaN/Ta, 2-10 nm) to leave Cu only in trenches and vias, with a flat surface for the next layer.

**Three-step Cu CMP**:

| Step | Purpose | Slurry | Rate | Selectivity |
|------|---------|--------|------|-------------|
| Bulk Cu removal | Remove 80-90% of overburden | Alumina abrasive (50-200 nm, 2-5% wt), glycine (1-3% wt), H₂O₂ (1-5% wt), pH 4-5 | 300-800 nm/min | Cu:dielectric >50:1 |
| Cu clearing | Clear remaining Cu to barrier | Colloidal silica (30-80 nm, 1-3% wt), glycine, H₂O₂, pH 4-5 | 50-100 nm/min | Cu:barrier >20:1 |
| Barrier removal | Remove TaN/Ta and TiN | Colloidal silica (30-80 nm), H₂O₂, benzotriazole (BTA, 0.01-0.1%), pH 8-10 | 10-30 nm/min | Barrier:dielectric >5:1 |

**Defect challenges**: Cu dishing (recess of Cu below dielectric surface) and dielectric erosion (thinning of dielectric between dense lines) are the primary yield limiters. Dishing targets: <30 nm for 0.25 μm lines, <10 nm for 10 μm pads. Erosion targets: <30 nm for 50% metal density areas. Controlled by slurry selectivity, downforce (1-4 psi), and pad conditioning.

**Post-CMP clean**: Brush scrubber with dilute citric acid (0.5-2% wt) at pH 3-5 to remove slurry particles and organic residues, followed by megasonic DI water rinse at 50-80°C. Defect target: <50 adders per 300 mm wafer at >0.12 μm particle size.

## Electromigration and Reliability

**Failure mechanism**: Cu atoms migrate along grain boundaries and interfaces under the "electron wind" of high current density (10⁶-10⁷ A/cm²). This creates voids at the upstream (cathode) end and hillocks at the downstream (anode) end. Void growth eventually severs the interconnect — open circuit failure.

**Mean time to failure (MTTF)**: Described by Black's equation: MTTF = A × (J⁻ⁿ) × exp(Ea/kT), where J = current density, n = 1-2 (current density exponent), Ea = activation energy (0.7-1.0 eV for Cu), kT = thermal energy. Typical GPU interconnect reliability: MTTF >10 years at 105°C junction temperature with 2× design current density.

**Electromigration improvement**: (1) Cu alloying: add 0.1-1.0 at.% Al, Mn, or Ti to Cu — these solutes segregate to grain boundaries, reducing Cu diffusivity. (2) CoWP or CuMn self-forming barrier capping layer (5-20 nm by electroless plating) on top of Cu lines — caps grain boundary diffusion paths at the Cu surface. (3) Larger grain size through optimized annealing — fewer grain boundaries means fewer diffusion paths.


## Global Production and Prices

| Metal | Annual Production | Price Range | Critical Semiconductor Use |
|-------|------------------|-------------|---------------------------|
| Titanium | 6-7 million tonnes Ti sponge | $8-15/kg sponge | TiN hard masks, Ti barriers (~0.01% of Ti demand) |
| Tungsten (as WF₆) | 25,000-30,000 t WF₆ | $30-60/kg WF₆ | W contact plugs, TSV fill (~40% of WF₆ demand by value) |
| Molybdenum | 280,000-300,000 t Mo | $10-40/kg Mo | Mo gate electrodes, heat sinks (<1% of Mo demand) |
| Copper | 22-25 million tonnes Cu | $7-10/kg Cu | Cu damascene interconnects (~2% of Cu demand) |

## Critical Supply Risks

**Tungsten**: China controls 80%+ of mine production and >90% of WF₆ manufacturing capacity. A single Chinese export restriction could halt global W CVD plug fill within 6-12 months. Mitigation: recycle W from CMP slurry (economic at >5% recovery), develop Mo or Co as alternative plug fill materials.

**Molybdenum**: Semiconductor-grade Mo targets require U/Th <1 ppb — this specification eliminates most standard Mo production. Only 3-5 suppliers worldwide produce semiconductor-grade Mo sputtering targets (Plansee SE, Toshiba Materials, H.C. Starck). Lead time: 6-12 months for target orders.

**Copper**: Semiconductor-grade Cu sulfate and electroplating additives are available from multiple suppliers. Cu supply risk is low — copper is one of the most widely produced metals. However, ultra-pure Cu seed layer targets (5N-6N, 99.999-99.9999%) are specialty items from fewer suppliers.

**Titanium**: Ti sputtering targets for TiN hard mask production face similar purity challenges as Mo. Semiconductor-grade Ti targets are produced by the same 3-5 specialty suppliers as Mo targets.

## Safety and Hazards

**WF₆ exposure**: Tungsten hexafluoride reacts with atmospheric moisture to produce HF: WF₆ + 3H₂O → WO₃ + 6HF. HF burns penetrate skin and decalcify bone — even small exposures require immediate calcium gluconate gel treatment (see [Mineral Acids](../chemistry/acids.md)). All WF₆ handling must be in ventilated gas cabinets with HF monitors, automatic shutoff valves, and emergency scrubbers.

**Cu CMP slurry**: Cu²⁺ ions are toxic to aquatic life (LC₅₀ <0.1 mg/L for Daphnia magna). Spent Cu CMP slurry is classified as hazardous waste. Treatment: ion exchange or electrowinning to recover Cu (economic at >0.5% Cu in slurry), followed by precipitation of remaining metals as hydroxides before discharge.

**Mo and Ti powders**: Fine metal powders (<10 μm) are pyrophoric — they can ignite spontaneously in air. Handle under inert atmosphere. Use wet methods for powder handling. Fire risk is mitigated by keeping powders in sealed containers under argon.

**TiCl₄**: Titanium tetrachloride (feedstock for TiO₂ and TiN ALD precursors) is a fuming liquid that reacts violently with water: TiCl₄ + 2H₂O → TiO₂ + 4HCl. The HCl fume cloud from a TiCl₄ spill is immediately dangerous to life. Full acid gas respiratory protection required.

## GPU Critical Path Integration

These four metals converge at specific points in GPU fabrication:

**Front-end-of-line (FEOL)**: Mo gate electrodes replace poly-Si at sub-22 nm nodes, enabling the metal-gate/high-k stack that achieves the threshold voltages and drive currents necessary for GHz-range GPU operation. Without Mo (or equivalent metal gate), poly-Si depletion and high resistance limit clock frequency.

**Middle-of-line (MOL)**: W contact plugs connect transistor source/drain terminals to the first metal layer. A single voided W contact kills the transistor. At sub-10 nm nodes, W plug resistance is a significant contributor to RC delay — the W plug resistance (10-50 Ω per contact) can exceed the transistor channel resistance.

**Back-end-of-line (BEOL)**: TiN hard masks enable dual damascene patterning of the dielectric stack. Cu electroplating fills trenches and vias. Cu CMP planarizes each layer. TaN/Ta barriers prevent Cu poisoning. The complete BEOL stack of 10-15 Cu damarcene layers carries all signals and power across the GPU die.

**Packaging/thermal**: Mo heat spreaders and Mo-Cu composites extract heat from the GPU die. W TSVs enable 3D stacking of HBM memory on the GPU interposer. Cu pillar bumps provide the die-to-substrate connection in flip-chip packages.



## See Also

- [Refractory & Specialty Metals](refractory-specialty.md) — tungsten, molybdenum, and tantalum
- [Core Fab Processes](../photolithography/fab-processes.md) — semiconductor fabrication
- [Gas Handling Vacuum](../gas-handling/vacuum.md) — vacuum deposition systems
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — interconnect and barrier deposition
- [Refractory Metals](refractory-metals.md) — high-melting-point metals for tooling
- [Aluminum](aluminum.md) — aluminum interconnects and metallization

[← Back to Metals](index.md)
