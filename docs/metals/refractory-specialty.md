# Refractory & Specialty Metals for Semiconductor Manufacturing

> **Node ID**: metals.refractory-specialty
> **Domain**: [Metals](./index.md)
> **Dependencies**: [`chemistry`](../chemistry/index.md), [`metals`](./index.md), [`metals.refractory-metals`](refractory-metals.md)
> **Enables**: [`metals.specialty-semiconductor`](specialty-semiconductor.md)
> **Timeline**: Years 35-70
> **Outputs**: tantalum sputtering targets, TaN/Ta diffusion barriers, cobalt silicide contacts, Co CMP slurries, ITO sputtering targets, InGaAs wafers, indium bump bonds
> **Critical**: No — essential for advanced semiconductor nodes but not required for basic civilization infrastructure

### Problem

Modern GPU manufacturing requires three specialty metals that no other materials can replace. Tantalum forms the copper diffusion barrier (TaN/Ta liner) that prevents Cu from poisoning silicon devices — without it, copper interconnects kill transistors within hours. Cobalt silicide (CoSi₂) provides the lowest-resistance self-aligned contacts at sub-7 nm nodes, and cobalt-based CMP slurries planarize copper interconnects. Indium tin oxide (ITO) is the dominant transparent conductor for displays and touchscreens, while InGaAs enables high-speed photonics for optical interconnects. You can pattern features lithographically but cannot build functional contacts, barriers, or optical interfaces without these three metals.

### Prerequisites

- [Refractory metals](refractory-metals.md) — tantalum extraction from coltan ore (HF dissolution + MIBK solvent extraction)
- [Chemistry](../chemistry/index.md) — HF, HNO₃, and solvent extraction for ore processing
- [Non-ferrous metals](non-ferrous.md) — cobalt and indium smelting and refining
- [Semiconductor fabrication](../photolithography/fab-processes.md) — sputtering, CMP, and thin-film processes
- [Vacuum technology](../gas-handling/vacuum.md) — sputtering deposition systems

## Overview

Three specialty metals — tantalum (Ta), cobalt (Co), and indium (In) — occupy critical positions on the semiconductor manufacturing path that no other materials can fill. Tantalum forms the copper diffusion barrier (TaN/Ta liner) that prevents Cu from poisoning silicon devices. Cobalt silicide (CoSi₂) provides the lowest-resistance self-aligned contacts at sub-7 nm nodes, and cobalt-based CMP slurries planarize copper interconnects. Indium tin oxide (ITO) is the dominant transparent conductor for displays and touchscreens, while InGaAs enables high-speed photonics for optical interconnects. Without these three metals, modern GPU manufacturing stops at the lithography stage — you can pattern features but cannot build functional contacts, barriers, or optical interfaces.

Extraction of tantalum from coltan ore (HF dissolution + MIBK solvent extraction) is covered in [Refractory Metals](refractory-metals.md). This document focuses on the semiconductor-grade processing and thin-film applications that justify their position on the GPU critical path.

## Tantalum (Ta) — Copper Diffusion Barrier

### Properties Relevant to Semiconductor Use

| Property | Value | Significance |
|----------|-------|--------------|
| Atomic number | 73 | Heavy atom — dense barrier to Cu diffusion |
| Melting point | 3017°C | Thermally stable through BEOL processing (400-450°C) |
| Resistivity (α-Ta) | 15-25 μΩ·cm | Acceptable RC delay contribution |
| Resistivity (β-Ta) | 180-220 μΩ·cm | Unwanted tetragonal phase — must suppress |
| TaN resistivity | 130-250 μΩ·cm | Barrier layer, higher ρ acceptable |
| Cu diffusivity in Ta | <10⁻²⁰ cm²/s at 400°C | 10⁶× lower than in SiO₂ — effective barrier |
| Adhesion to Cu | Strong (metallic bonding) | Enables reliable Cu fill |
| Adhesion to SiO₂ | Strong (Ta₂O₅ interlayer) | Good dielectric interface |

**Phase control is critical**: Tantalum deposits in two crystallographic phases. α-Ta (bcc, stable) has low resistivity (15-25 μΩ·cm) and is ductile. β-Ta (tetragonal, metastable) has high resistivity (180-220 μΩ·cm) and is brittle. Sputtering conditions (substrate temperature, bias voltage, nitrogen partial pressure, seed layer) determine which phase forms. For barrier applications, pure α-Ta or TaN (which is always cubic NaCl structure) is required.

### Sputtering Target Manufacturing

**Target production pipeline**: Tantalum powder (see [Refractory Metals](refractory-metals.md) for extraction) → electron beam melting or vacuum arc melting into ingot → forging at 800-1000°C → rolling to slab → machining to target geometry → surface finishing → bonding to copper backing plate.

**Electron beam melting (EBM)**: Melt tantalum in a water-cooled copper crucible under high vacuum (<10⁻³ Pa) using a focused electron beam (30-60 keV, 5-30 kW). Multiple melt passes (2-4) improve homogeneity and reduce impurities. Ingot size: 100-300 mm diameter × 500-2000 mm length. Purity: 99.95-99.99% Ta. Key impurity limits for semiconductor-grade: O <50 ppm, N <30 ppm, C <20 ppm, Fe <10 ppm, Nb <100 ppm. Interstitial oxygen and nitrogen embrittle tantalum and increase resistivity — must be minimized.

**Forging and rolling**: Heat ingot to 800-1000°C in argon or vacuum. Upset forge to break cast structure. Roll to target thickness (6-25 mm). Anneal at 1100-1200°C in vacuum for stress relief and recrystallization. Target grain size: 30-100 μm (equiaxed, random texture preferred for uniform sputtering rate). Final dimensions: typically 300 mm × 300 mm × 6-12 mm for 300 mm wafer tools, or cylindrical 380 mm diameter × 12 mm for rotating magnetron cathodes.

**Target-backing plate bonding**: Diffusion-bond or explosively-clad the tantalum target to an oxygen-free copper (OFC) backing plate (25-40 mm thick). The copper provides thermal conductivity to remove sputtering heat (3-20 kW at the target surface). Bond integrity: shear strength >50 MPa, >95% bonded area (ultrasonic C-scan verification). Indium-based solder bonding (In-3Ag, mp 143°C) is also used for thinner targets — the low melting point avoids thermal stress on the target.

### TaN/Ta Barrier Deposition (PVD)

**Copper damascene barrier**: In modern interconnect technology (130 nm node and below), copper replaces aluminum for interconnects due to lower resistivity (1.68 μΩ·cm vs. 2.65 μΩ·cm). But Cu diffuses rapidly through SiO₂ and other dielectrics, creating deep-level traps that destroy transistor function. A barrier/liner layer of TaN/Ta (2-10 nm thick) between the copper and the dielectric prevents this diffusion.

**Ionized PVD (iPVD) process**: Deposit TaN/Ta in a magnetron sputtering system with RF coil ionization. Process conditions: Ar pressure 0.5-5.0 mTorr, target power 5-30 kW DC, substrate bias -50 to -200V RF, nitrogen flow 0-20% of total gas for TaN. Step 1: Deposit 1-3 nm TaN (reactive sputter in Ar/N₂) — the nitrogen-stabilized cubic phase provides the primary diffusion barrier. Step 2: Deposit 2-8 nm Ta (pure Ar sputter, nitrogen off) — the metallic Ta layer improves adhesion between TaN and the subsequently deposited Cu seed layer. Step coverage: iPVD achieves 15-40% bottom coverage in high-aspect-ratio (AR 4-8) trenches and vias, compared to 5-15% for conventional PVD. This is the fundamental limitation driving the transition to ALD TaN for sub-22 nm features.

**ALD TaN**: For advanced nodes (sub-22 nm), PVD cannot provide conformal coverage in features with AR >5. ALD TaN uses alternating pulses of TBTDET (tert-butylimidotris(diethylamido)tantalum, Ta(NC(CH₃)₃)(NEt₂)₃) and plasma nitrogen at 250-350°C. Growth rate: 0.5-0.7 Å/cycle. Film properties: resistivity 150-300 μΩ·cm (slightly higher than PVD TaN), density >14 g/cm³, Cu barrier performance equivalent to PVD TaN. Conformality: >95% step coverage in AR 20:1 features.

### Barrier Performance Metrics

**Figure of merit**: Time-to-failure in bias-temperature-stress (BTS) test. Apply 1-2 MV/cm electric field at 250-350°C for 30-120 minutes. Monitor leakage current through the dielectric. Failure criterion: leakage increase >2 orders of magnitude (Cu has penetrated to Si). TaN/Ta barrier (5 nm): passes BTS at 350°C for >60 minutes. For comparison: TiN barrier (5 nm) fails at 300°C in <10 minutes. TaN is 10-100× more effective than TiN as a Cu diffusion barrier.

**Minimum barrier thickness**: Theoretically, 0.5-1.0 nm of continuous TaN blocks Cu diffusion. Practically, 2-3 nm is the minimum for reliable coverage over trench bottom corners and via sidewall roughness. At sub-7 nm nodes, the barrier/liner consumes 20-30% of the via cross-section, dramatically increasing via resistance — this is the primary driver for cobalt contact and ruthium liner research.

## Cobalt (Co) — Silicide Contacts and CMP

### Properties

| Property | Value |
|----------|-------|
| Atomic number | 27 |
| Melting point | 1495°C |
| Boiling point | 2927°C |
| Density | 8.90 g/cm³ |
| Crystal structure | HCP (α-Co, <417°C), FCC (β-Co, >417°C) |
| Electrical resistivity | 6.2 μΩ·cm |
| CoSi₂ resistivity | 14-18 μΩ·cm |
| CoSi₂ Schottky barrier height (n-Si) | 0.64-0.66 eV |
| Magnetic | Ferromagnetic (Curie temp 1121°C) |

### Ores and Extraction

**Cobaltite** (CoAsS) and **skutterudite** (CoAs₃) are the primary cobalt minerals. Cobalt is overwhelmingly produced as a byproduct — 55% from copper mining (DRC Congo, Zambia), 35% from nickel mining (Russia, Australia, Canada), 10% from primary cobalt operations (Morocco). Global production: ~190,000-230,000 tonnes Co per year.

**Extraction from copper-cobalt ores (DRC)**: Mine sulfide/oxide ore (1-4% Cu, 0.1-1.0% Co). Roast sulfide ore at 600-700°C to convert sulfides to sulfates and oxides. Leach roasted calcine in sulfuric acid (pH 1.5-2.0) at 60-80°C. Remove copper by solvent extraction (LIX reagents). Recover cobalt from raffinate by: (1) Solvent extraction with Cyanex 272 (bis(2,4,4-trimethylpentyl)phosphinic acid) at pH 5.0-6.0 — highly selective for Co over Ni, Ca, Mg. (2) Stripping with H₂SO₄ to produce pure CoSO₄ solution. (3) Electrowinning: Co²⁺ + 2e⁻ → Co at 55-65°C, 200-400 A/m², cell voltage 2.5-3.5 V. Deposit on stainless steel cathodes. Product: 99.8-99.9% Co cathode. Energy: 3.5-4.5 kWh/kg Co.

**Purification to semiconductor grade**: Semiconductor-grade cobalt requires 99.99%+ purity with stringent limits on Fe (<5 ppm), Ni (<10 ppm), Cu (<2 ppm), and magnetic impurities. Additional purification by zone refining or electrolytic refining in chloride bath (CoCl₂ + HCl at pH 2-3). Target: 4N-5N purity for sputtering targets and CoSi₂ formation.

### Cobalt Silicide (CoSi₂) Self-Aligned Contacts

**Why CoSi₂ replaced TiSi₂**: At the 130 nm node, titanium silicide (TiSi₂, C54 phase, 13-18 μΩ·cm) was the standard contact material. Below 130 nm, TiSi₂ fails to nucleate the low-resistance C54 phase on narrow (≤0.2 μm) polysilicon lines — the C49 (high-ρ, 60-80 μΩ·cm) to C54 phase transformation is geometry-dependent and suppressed in narrow lines. Cobalt silicide (CoSi₂) has no such geometry dependence, forms uniformly on features down to 30 nm, and achieves low resistivity (14-18 μΩ·cm) in a single anneal.

**Self-aligned silicide (salicide) process**: (1) Clean exposed silicon/poly-Si surfaces with dilute HF (1-2% HF, 30-60s) to remove native oxide. (2) Deposit cobalt film by PVD sputtering: 5-20 nm Co at room temperature, base pressure <5×10⁻⁷ Pa, Ar pressure 2-5 mTorr. (3) First rapid thermal anneal (RTA1) at 500-550°C for 30-60 seconds in N₂ ambient. Cobalt reacts with Si to form CoSi (cubic, ρ ≈ 150 μΩ·cm) on exposed Si surfaces. Co does NOT react with SiO₂ or Si₃N₄ — the reaction is self-aligned to exposed silicon. (4) Selective etch: immerse in HCl:H₂O₂:H₂O (3:1:10) at 35-45°C for 5-15 minutes. This removes unreacted Co on dielectric surfaces while leaving CoSi on silicon untouched. (5) Second rapid thermal anneal (RTA2) at 700-800°C for 30-60 seconds in N₂. CoSi transforms to CoSi₂ (cubic CaF₂ structure, ρ = 14-18 μΩ·cm). Final CoSi₂ thickness: 3.5-4.0× the initial Co thickness (10 nm Co → ~35-40 nm CoSi₂). Sheet resistance on poly-Si lines: 2-8 Ω/sq depending on linewidth.

**Contact resistance**: CoSi₂/Si specific contact resistivity: ρc = 10⁻⁷ to 10⁻⁸ Ω·cm² on n⁺-Si (doped >10²⁰ cm⁻³). At sub-7 nm nodes, the contact via area shrinks to 500-2000 nm², making contact resistance a significant contributor to transistor RC delay. Pre-silicide implantation (junction activation before Co deposition) and epitaxial raised source/drain structures reduce ρc below 10⁻⁸ Ω·cm².

**Thermal stability**: CoSi₂ is stable to 900-950°C — compatible with all backend-of-line (BEOL) thermal budgets (maximum 400-450°C for Cu damascene). No agglomeration or morphological degradation through multiple thermal cycles.

### Cobalt CMP (Chemical Mechanical Planarization)

**Why cobalt replaced copper for contact polish**: At sub-14 nm nodes, the contact plug transitions from tungsten (W) to cobalt (Co). Co has lower resistivity than W (6.2 vs. 5.6 μΩ·cm — comparable, but Co fills smaller features better by CVD) and provides a direct Co-to-CoSi₂ contact interface without an adhesion layer. After electroplating Co into contact vias, the overburden must be removed by CMP without dishing or erosion.

**Co CMP slurry chemistry**: Unlike Cu CMP (which uses glycine + H₂O₂ + alumina abrasive), Co CMP is complicated by cobalt's high chemical reactivity and low pitting corrosion resistance in acidic media. Modern Co CMP slurries use: (1) Oxidizer: H₂O₂ (0.5-3.0% wt) or potassium persulfate (K₂S₂O₈, 0.1-1.0% wt). (2) Complexing agent: glycine (0.5-2.0% wt) or citric acid — forms soluble Co²⁺ complexes. (3) Corrosion inhibitor: 1,2,4-triazole (0.01-0.5% wt) or benzotriazole (BTA) — adsorbs on Co surface forming a passivation layer that protects recessed areas while allowing protruding areas to be abraded. (4) Abrasive: colloidal silica (SiO₂, 20-80 nm particles, 1-5% wt) or alumina (Al₂O₃, 50-200 nm, 0.5-3% wt). Slurry pH: 8.5-10.5 (alkaline regime — Co forms protective Co(OH)₂ film that prevents pitting). Polish rate: 50-200 nm/min. Selectivity Co:dielectric >20:1.

**Two-step CMP for Co**: Step 1 (bulk removal): fast polish with high-abrasive slurry, removes 80-90% of Co overburden. Step 2 (fine polish): low-downforce polish with inhibitor-rich slurry, clears remaining Co while minimizing dishing (<10 nm) and dielectric erosion (<5 nm). Endpoint detection: optical (interferometric) or motor current (friction change when Co clears to expose dielectric).

**Defect control**: Co CMP scratches are a critical yield limiter at sub-10 nm nodes. Scratches in the Co contact surface propagate through subsequent dielectric layers, causing interlayer shorts. Slurry filtration (0.1-0.2 μm absolute filters), in-situ pad conditioning with diamond disk (100-200 grit, 5-10 N downforce), and post-CMP cleaning (brush scrubber with dilute citric acid + megasonic DI water) reduce scratch density to <0.01 scratches/cm².

## Indium (In) — Transparent Conductors and Photonics

### Properties

| Property | Value |
|----------|-------|
| Atomic number | 49 |
| Melting point | 156.6°C — melts in boiling water |
| Boiling point | 2072°C |
| Density | 7.31 g/cm³ |
| Crystal structure | Tetragonal (body-centered) |
| Electrical resistivity | 8.4 μΩ·cm |
| Thermal conductivity | 82 W/(m·K) |
| Mohs hardness | 1.2 — softer than fingernail |
| CTE | 32.1 × 10⁻⁶/°C |

### Production and Supply

**Source**: Indium is one of the rarest stable elements (crustal abundance ~0.05 ppm). It is never mined as a primary product — it is recovered exclusively as a byproduct of zinc smelting. Sphalerite (ZnS) contains 10-300 ppm In; the indium substitutes for zinc in the crystal lattice. Global production: ~900-1,200 tonnes In per year.

**Recovery from zinc smelting**: In the roast-leach-electrowin zinc process (see [Non-Ferrous Metals](non-ferrous.md)), indium reports to the jarosite/goethite iron precipitation residue or to the copper cementation residue. Recovery: (1) Acid leach the residue with H₂SO₄ at 80-90°C — indium dissolves as In₂(SO₄)₃. (2) Solvent extraction with di-(2-ethylhexyl)phosphoric acid (D2EHPA) in kerosene at pH 2.0-3.0. In³⁺ extracts selectively over Zn²⁺, Cu²⁺, and Cd²⁺ at this pH. (3) Strip loaded organic with 4-6M HCl to produce InCl₃ solution. (4) Replace aluminum or zinc plates in InCl₃ solution — indium cementation (In³⁺ + 3/2 Al → In + 3/2 Al³⁺). Or (4b) Electrowin from In₂(SO₄)₃ or InCl₃ electrolyte at 50-60°C, 50-100 A/m². Product: 99.99% In (4N). (5) Further purification by vacuum distillation or zone refining to 5N-6N (99.999-99.9999%) for semiconductor applications.

**Supply constraint**: Indium supply is fundamentally limited by zinc production — you cannot produce more indium without producing more zinc. At ~1,000 tonnes/year, indium is 0.001% of zinc production by mass. Price: $200-400/kg for 4N grade, $500-1,000/kg for 5N-6N semiconductor grade. This makes indium one of the most expensive bulk semiconductor materials, and a significant supply-chain risk for display manufacturing.

### ITO (Indium Tin Oxide) — Transparent Conductor

**Composition and properties**: ITO is a solid solution of In₂O₃ doped with SnO₂ (typically 90% In₂O₃ + 10% SnO₂ by weight, or ~10% Sn doping on In sites). The tin dopant donates free electrons to the conduction band, creating an n-type degenerate semiconductor with metallic conductivity. Key properties: resistivity 1-5 × 10⁻⁴ Ω·cm, visible light transmission >85% (for 100-200 nm film), bandgap 3.5-4.3 eV (absorbs UV, transmits visible). No other transparent conductor matches ITO's combination of low resistivity and high optical transmission.

**ITO sputtering target manufacturing**: (1) Blend In₂O₃ powder (5N-6N purity, 1-5 μm) with SnO₂ powder (5N, 0.5-2 μm) at 90:10 weight ratio. (2) Press in isostatic press at 100-200 MPa into cylindrical or planar billets. (3) Sinter in oxygen atmosphere at 1400-1600°C for 10-30 hours — oxygen atmosphere is critical to maintain correct stoichiometry and achieve >95% theoretical density (6.8-7.1 g/cm³). (4) Machine to target dimensions (320-380 mm diameter for display production, 150-300 mm for semiconductor). Target uniformity: density variation <1% across target to ensure consistent sputtering rate.

**DC magnetron sputtering**: Deposit ITO on glass, PET, or other substrates at room temperature to 350°C. Process: Ar + 0.5-5% O₂ at 2-8 mTorr, DC power density 1-10 W/cm², target-to-substrate distance 50-120 mm. Deposition rate: 2-15 nm/min. Film thickness: 100-200 nm for display electrodes, 20-50 nm for touch sensors. Oxygen flow must be precisely controlled: too little O₂ → dark, absorbing film (oxygen vacancies create color centers); too much O₂ → insulating film (fully oxidized, no free carriers). Optimum: slight oxygen deficiency (In₂O₃₋ₓ, x = 0.01-0.05) for maximum carrier concentration (10²⁰-10²¹ cm⁻³) and minimum resistivity.

**Post-deposition annealing**: For room-temperature-deposited ITO on flexible substrates (PET), post-anneal at 150-200°C in vacuum or forming gas (N₂ + 5% H₂) for 30-60 minutes to improve crystallinity and reduce resistivity by 30-50%. Vacuum-annealed ITO on PET achieves 3-8 × 10⁻⁴ Ω·cm — adequate for touch sensors but not for high-efficiency solar cells.

**Applications**: (1) LCD/LED display electrodes: ITO on glass for transparent pixel electrodes — every pixel in every display requires ITO. (2) Touch sensors: ITO on PET film for capacitive touch panels (smartphones, tablets). (3) Thin-film solar cells: ITO transparent front contact on CIGS (CuInGaSe₂) and perovskite solar cells. (4) EMI shielding: ITO-coated windows and enclosures for electromagnetic interference attenuation at >10 dB from 30 MHz to 1 GHz while maintaining optical transparency.

### InGaAs (Indium Gallium Arsenide) — High-Speed Photonics

**Material system**: InₓGa₁₋ₓAs is a III-V compound semiconductor alloy lattice-matched to InP (indium phosphide) substrates at x = 0.53 (In₀.₅₃Ga₀.₄₇As). The bandgap of lattice-matched InGaAs is 0.74 eV — ideal for detecting 1.3-1.55 μm wavelength photons used in fiber optic telecommunications. Electron mobility: 10,000-12,000 cm²/V·s (6-8× higher than silicon), enabling ultra-fast transistors (fT >300 GHz).

**InP substrate production**: Grow InP single crystals by liquid-encapsulated Czochralski (LEC) or vertical gradient freeze (VGF). Melt InP polycrystal at 1062°C under boron trioxide (B₂O₃) encapsulant (prevents phosphorus loss). Pull at 5-15 mm/hr. Wafer diameter: 100-150 mm (InP wafers are smaller and 5-10× more expensive than Si wafers). Dislocation density: <5,000 cm⁻² for device-grade substrates. Semi-insulating InP (Fe-doped, ρ >10⁷ Ω·cm) for RF applications.

**MBE and MOCVD growth of InGaAs**: Epitaxial InGaAs layers grown by molecular beam epitaxy (MBE) or metal-organic chemical vapor deposition (MOCVD). MBE: elemental In, Ga, and As sources evaporated in ultra-high vacuum (<10⁻⁸ Pa), growth rate 0.5-2.0 μm/hr, monolayer-level thickness control. MOCVD: trimethylindium (TMIn), trimethylgallium (TMGa), and arsine (AsH₃) in H₂ carrier gas at 550-650°C, 50-100 Torr. InGaAs/InP heterostructures: In₀.₅₃Ga₀.₄₇As channel (0.74 eV) with In₀.₅₂Al₀.₄₈As barrier (1.45 eV) on InP substrate — the lattice-matched III-V system for high-electron-mobility transistors (HEMTs) and heterojunction bipolar transistors (HBTs).

**Photodetector applications**: InGaAs photodiodes are the only practical detectors for 1.3-1.55 μm fiber optic wavelengths (Si and Ge have bandgaps too large for 1.55 μm). PIN photodiodes: InGaAs absorbing layer (1-5 μm thick) between p-InP and n-InP layers. Dark current: <1 nA at -2V. Responsivity: 0.8-1.0 A/W at 1.55 μm. Bandwidth: 10-40 GHz for telecommunications receivers. Avalanche photodiodes (APDs) achieve internal gain of 10-30× for improved receiver sensitivity.

### Indium Bump Bonding for Flip-Chip

**Flip-chip interconnect**: In advanced GPU packaging, the die is flipped face-down onto the organic substrate and connected through an array of solder bumps (5,000-50,000 bumps per die). The bump metallurgy is critical: it must provide reliable electrical and thermal connection, withstand thermal cycling (-40°C to +125°C), and be reworkable.

**Indium-based bump alloys**: (1) In-3Ag (mp 143°C): low melting point enables bonding below 200°C — critical for organic substrates that degrade above 230°C. Excellent thermal fatigue resistance (In's high ductility accommodates CTE mismatch between Si die and organic substrate). (2) In-48Sn (mp 118°C): even lower melting point for temperature-sensitive components. (3) Pure indium bumps: softest metal bump material, highest ductility, compliant under thermal stress. Used for cryogenic applications (superconducting detector arrays) where conventional solders become brittle.

**Bump fabrication — electroplating**: (1) Pattern photoresist on die bump pads (25-100 μm openings). (2) Seed layer: sputter Ti/Cu (50/200 nm) as plating base. (3) Electroplate indium or In-Ag alloy from InCl₃ or In₂(SO₄)₃ bath at 20-30°C, 10-30 mA/cm². Add AgNO₃ to bath for In-3Ag alloy. (4) Strip photoresist. (5) Etch seed layer. Bump height: 20-80 μm. Bump diameter: 25-100 μm. (6) Reflow at 170-200°C in forming gas to form spherical bump shape (surface tension). Coplanarity: ±3 μm across all bumps on die.

**Thermal compression bonding**: For fine-pitch bumps (<40 μm pitch), reflow is insufficient for alignment. Thermal compression bonding: align die to substrate (±1 μm placement accuracy), apply 30-80 MPa pressure at 180-220°C for 5-30 seconds in N₂ atmosphere. The indium bump deforms plastically and metallurgically bonds to the substrate pad (Au or Cu-OSP finish). Bond strength: >20 g/bump. Resistance per bump: 5-20 mΩ.

**Thermal interface material (TIM)**: Indium foil (0.1-1.0 mm) is used as a thermal interface between the GPU die and the heat spreader. Indium's high thermal conductivity (82 W/m·K) and extreme softness (conforms to surface roughness) provide thermal resistance of 0.05-0.15 °C·cm²/W — among the lowest of any TIM. Pure indium melts at 156.6°C, so TIM operating temperature must stay below 125°C. Ga-In eutectic alloys (Ga-In-Sn, liquid at room temperature) are used as liquid metal TIMs for extreme performance.

## Supply Chain and Critical Dependencies

### Global Production and Prices

| Metal | Annual Production | Price Range | Primary Source |
|-------|------------------|-------------|----------------|
| Tantalum | 1,800-2,200 t Ta | $150-400/kg | DRC (35%), Rwanda, Brazil |
| Cobalt | 190,000-230,000 t Co | $25-45/kg | DRC (70%), Russia, Australia |
| Indium | 900-1,200 t In | $200-1,000/kg | China (40%), South Korea, Japan |

### Critical Supply Risks

**Tantalum**: Conflict mineral (DRC). Semiconductor-grade tantalum targets represent <5% of tantalum consumption by volume but >20% by value. Semiconductor fabs maintain 6-12 months of tantalum target inventory as buffer against supply disruptions. Recycling of spent sputtering targets recovers 95%+ of tantalum.

**Cobalt**: Extreme geographic concentration (DRC produces 70% of mined cobalt). Ethical sourcing concerns (artisanal mining, child labor). Cobalt for semiconductor use (CoSi₂, CMP) is <1% of total cobalt demand — automotive batteries consume 60%+. Price volatility: spiked from $25/kg to $95/kg in 2018 due to EV battery demand, collapsed to $25/kg in 2020.

**Indium**: Fundamentally supply-limited by zinc production. ITO for displays consumes 70-80% of indium production. A single large LCD fab (Generation 10.5, glass size 2940 × 3370 mm) can consume 50-100 tonnes of indium per year. ITO recycling from display manufacturing scrap recovers 70-80% of indium. Alternative transparent conductors (silver nanowire, graphene, AZO — aluminum zinc oxide) have been researched for 20+ years but none match ITO performance.

### Recycling and Recovery

**Spent sputtering targets**: Tantalum and ITO targets are used until 50-70% eroded. The remaining material is sent to specialty recyclers who dissolve in HF (Ta) or H₂SO₄ (ITO), recover Ta or In by solvent extraction, and return purified material to target manufacturers. Recovery: >95% for Ta, 85-90% for In. Recycling loop: target → use → reclaim → purify → new target. Cycle time: 3-6 months.

**CMP slurry cobalt recovery**: Co CMP waste slurry contains 0.1-1.0% Co by weight. Ion exchange or cementation recovers cobalt from the spent slurry. Recovery is economically marginal (Co value ~$0.01-0.05/L of spent slurry) but environmentally mandated in most jurisdictions.

## Safety and Hazards

**Cobalt dust and fume**: Cobalt and cobalt compounds are classified as IARC Group 2B (possibly carcinogenic) and Group 2A (probably carcinogenic for cobalt metal with tungsten carbide). Hard metal lung disease (giant cell interstitial pneumonitis) is associated with Co + WC exposure in cemented carbide manufacturing (see [Refractory Metals](refractory-metals.md)). For semiconductor fab workers, Co CMP slurry handling presents the primary exposure route — engineering controls (enclosed slurry delivery, local exhaust ventilation, PPE) keep airborne Co below 0.02 mg/m³ (ACGIH TLV).

**Indium compounds**: Indium tin oxide (ITO) is classified as a suspected lung carcinogen based on animal studies. ITO sputtering targets and ITO dust generated during target handling present inhalation hazards. ITO nanoparticles (<100 nm) are more toxic than larger particles — they cause pulmonary inflammation and alveolar proteinosis in animal models at doses >20 mg/kg. Controls: handle ITO targets and powders in ventilated enclosures, use wet cleaning methods, avoid generating airborne particles.

**Tantalum**: Tantalum metal and Ta₂O₅ are generally considered biocompatible and low-toxicity (hence use in surgical implants). Tantalum powder (<10 μm) is flammable — fine metal powders can form explosive dust-air mixtures. Handle under inert atmosphere, avoid ignition sources. Tantalum target manufacturing involves HF for surface etching — follow standard HF safety protocols (see [Mineral Acids](../chemistry/acids.md)).

**Indium bump bonding**: Indium melts at 156.6°C — well below most solder processing temperatures. Indium vapor pressure is negligible at typical bonding temperatures (<250°C), so inhalation exposure during bonding is minimal. Thermal compression bonding equipment operates at high force (kN range) — mechanical safety interlocks required.

## GPU Critical Path Integration

The three metals in this document converge at specific points in GPU fabrication:

**Front-end-of-line (FEOL)**: CoSi₂ self-aligned contacts form on source/drain and gate regions after transistor definition (see [Core Fab Processes](../photolithography/fab-processes.md)). At sub-7 nm nodes, the contact resistance of CoSi₂ directly limits transistor switching speed and hence GPU clock frequency.

**Middle-of-line (MOL)**: Cobalt CMP planarizes contact plugs that connect FEOL transistors to BEOL interconnects. Any defect in Co CMP (scratches, dishing, erosion) creates an open or short circuit — a single CMP scratch can kill an entire GPU die containing billions of transistors.

**Back-end-of-line (BEOL)**: TaN/Ta diffusion barriers line every copper interconnect trench and via — a modern GPU has 10-15 metal layers with 10-50 km of copper wiring per layer, all requiring TaN/Ta barrier. Without the barrier, copper poisons the transistors within hours at operating temperature.

**Packaging**: Indium bump bonds connect the GPU die to the organic substrate in flip-chip packages. A high-end GPU may have 5,000-10,000 bumps, each carrying 0.1-1.0 A of current. Indium's ductility accommodates the CTE mismatch between silicon (4.1 ppm/°C) and organic substrate (12-17 ppm/°C) through thousands of thermal cycles.

**Photonics**: InGaAs photodetectors are emerging as the receiver technology for optical interconnects between GPU chips in data center AI training clusters. As copper interconnects reach bandwidth-distance limits (~100 GB/s per lane at ~1 m), optical links using InGaAs receivers at 1.55 μm wavelength extend reach to 100+ m at >400 GB/s.

### Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| β-Ta phase (high resistivity) in barrier | Insufficient substrate heating or contamination during sputtering | Increase substrate temperature to 300-400°C; improve base vacuum; add Ti adhesion layer |
| TaN barrier pinholes | Poor sputtering uniformity or particulate contamination | Optimize sputter deposition rate; clean chamber; use point-of-use filtration on process gases |
| CoSi₂ high contact resistance | Insufficient cobalt thickness or wrong rapid thermal anneal profile | Ensure 10-20 nm Co film; optimize RTP (500-700°C first step, 800-850°C second step) |
| Co CMP scratching | Slurry abrasive size too large or pad conditioning inadequate | Use colloidal silica slurry (<50 nm); maintain pad conditioning regime; filter slurry at point of use |
| ITO sputtering target cracking | Thermal stress from high-power DC sputtering | Use pulsed DC power; ramp power gradually; ensure target cooling water flow |
| Indium bump non-wetting | Oxide on bonding surface or insufficient bonding force/temperature | Clean with dilute HCl; increase bonding force; verify temperature profile (200-250°C) |
| High Cu diffusion through barrier | TaN too thin (<2 nm) or phase not stoichiometric | Increase barrier thickness to 3-5 nm; verify N₂:Ar ratio during reactive sputtering |

### See Also

- [Refractory Metals](refractory-metals.md) — tantalum, tungsten, molybdenum extraction and processing
- [Specialty Semiconductor Metals](specialty-semiconductor.md) — downstream semiconductor metal applications
- [Non-Ferrous Metals](non-ferrous.md) — copper, nickel, cobalt, and indium refining
- [Core Fab Processes](../photolithography/fab-processes.md) — semiconductor manufacturing workflow
- [Photolithography](../photolithography/index.md) — patterning processes that these metals serve
- [Chemistry / Acids](../chemistry/acids.md) — HF and HNO₃ for ore processing
- [Gas Handling / Vacuum](../gas-handling/vacuum.md) — sputtering deposition systems
- [Glass / Photomask Substrates](../glass/photomask-substrates.md) — ITO-coated transparent substrates

[← Back to Metals](index.md)
