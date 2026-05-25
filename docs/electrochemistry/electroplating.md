# Electroplating

> **Node ID**: electrochemistry.electroplating
> **Domain**: [Electrochemistry & Plating](./index.md)
> **Dependencies**: [`chemistry.acids`](../chemistry/acids.md)
> **Enables**: `electrochemistry.electroplating.copper-damascene`
> **Timeline**: Years 30-70
> **Outputs**: copper_interconnects, plated_nickel, plated_gold, plated_tin, copper_filled_vias

### Overview

Electroplating deposits metal from solution onto a conductive substrate by reducing metal cations at the cathode using externally applied current. While the fundamental principle is shared with electrorefining (see [Electrolysis](../chemistry/electrolysis.md)), semiconductor electroplating demands far greater precision: feature sizes from 25 nm to 10 μm, aspect ratios up to 10:1, and film uniformity of ±5% across 300 mm wafers. The copper damascene process — where electroplated copper fills etched trenches and vias in the dielectric — has been the dominant interconnect technology since its introduction by IBM in 1997, replacing physical vapor deposition (PVD) aluminum at the 250 nm node and below.

For bootstrapping semiconductor manufacturing, electroplating is the only practical method to fill high-aspect-ratio features with copper. PVD and CVD cannot achieve conformal coverage in deep, narrow trenches — the mean free path of sputtered atoms and the sticking coefficient of CVD precursors both work against complete fill. Electroplating achieves bottom-up fill through additive-controlled suppression and acceleration of deposition kinetics, enabling void-free copper in features smaller than 50 nm.

### Copper Damascene Electroplating

The copper damascene process is the cornerstone of modern semiconductor interconnect fabrication. It replaces the earlier aluminum subtractive etch process with an additive (damascene) approach where copper is electroplated into patterned dielectric trenches and then planarized by CMP.

**Acid sulfate bath composition**:
- **Copper sulfate** (CuSO₄·5H₂O): 40-100 g/L (provides Cu²⁺ ions, equivalent to 10-25 g/L Cu). Higher copper concentration enables faster plating but increases bath viscosity and reduces throwing power.
- **Sulfuric acid** (H₂SO₄): 50-100 g/L. Increases bath conductivity (reduces cell voltage from ~2V to ~0.5V at 10 mA/cm²), prevents CuSO₄ precipitation, and maintains low pH (<1) to suppress hydrogen evolution.
- **Chloride ions** (HCl added): 50-100 ppm Cl⁻. Chloride acts as a brightener and leveler catalyst — it complexes with the accelerator (SPS) at the copper surface and promotes uniform, fine-grained deposition. Too much chloride causes pitting; too little causes rough, nodular deposits.
- **Accelerator** (bis-(3-sulfopropyl) disulfide, SPS or MPS): 0.5-10 ppm. Adsorbs on copper surface and catalyzes Cu²⁺ reduction, accelerating deposition at the bottom of features (bottom-up fill mechanism). The accelerator concentration in the feature bottom increases relative to the field because convection is restricted in deep features — the suppressor (PEG) dominates at the field surface while the accelerator dominates at the feature bottom.
- **Suppressor** (polyethylene glycol, PEG, MW 3000-8000): 100-500 ppm. Forms a resistive film on the copper surface (PEG + Cl⁻ + Cu⁺ complex), suppressing plating rate. The suppressor diffusion into features is limited by its large molecular size, allowing the accelerator to dominate in deep features. This differential suppression is the fundamental mechanism of bottom-up (superconformal) fill.
- **Leveler** (Janus Green B, diazine black, or proprietary amines): 0.1-5 ppm. Adsorbs preferentially at high-current-density regions (corners, edges, features near the wafer edge) to suppress overplating and improve across-wafer uniformity. The leveler is consumed (incorporated into the deposit) during plating, so its concentration must be monitored.

**Operating conditions**:
- **Bath temperature**: 20-25°C (tight control ±1°C). Higher temperature increases diffusion rate but reduces suppressor effectiveness, degrading bottom-up fill. Lower temperature increases bath viscosity, reducing transport into high-aspect-ratio features.
- **Current density**: 5-40 mA/cm² (DC) for field plating. Via/trench fill uses lower initial current density (5-10 mA/cm²) during the critical fill phase, then higher current density (20-40 mA/cm²) for bulk copper overburden.
- **Cell voltage**: 0.3-1.5V depending on current density and bath conductivity.
- **Wafer rotation**: 10-100 rpm during plating to control diffusion layer thickness and across-wafer uniformity.
- **Anode**: Phosphorus-containing copper anode (0.03-0.08% P). The phosphorus forms a black film (Cu₃P) on the anode surface that prevents copper particle generation and ensures uniform anode dissolution. Anode-to-cathode area ratio: 2:1 to 3:1.

**Pulse reverse plating**:
- **Forward pulse**: 5-30 mA/cm² for 1-100 ms. Copper deposits during the forward pulse.
- **Reverse pulse**: 5-30 mA/cm² for 0.1-10 ms. Copper dissolves preferentially from high-current-density features (edges, corners) during the reverse pulse, improving uniformity.
- **Duty cycle**: Forward/reverse ratio typically 10:1 to 50:1. The average current density equals the desired deposition rate.
- **Advantages over DC**: Improved via fill (15-30% faster bottom-up fill), reduced overburden (less copper to remove by CMP), finer grain structure, and reduced impurity incorporation. Pulse reverse is essential for features below 100 nm.

**Via and trench fill mechanism**:
1. **Seed layer**: PVD copper seed (50-150 nm) is deposited on the barrier layer (TaN/Ta, 5-20 nm) before electroplating. The seed must be continuous — any breaks cause voids. For features below 50 nm, the PVD seed becomes discontinuous; ALD or CVD copper seed alternatives are under development.
2. **Initial nucleation**: The first 50-200 nm of electroplated copper nucleates on the seed layer. Additive concentrations are critical during this phase — too much suppressor causes "terminal" voids (plating stops before fill completes), too little suppressor causes seams down the center.
3. **Bottom-up fill**: The accelerator (SPS) preferentially adsorbs at the feature bottom where the suppressor (PEG) concentration is lowest (limited diffusion into the feature). This causes faster plating at the bottom than at the opening, resulting in a V-shaped fill front that advances upward. Fill time: 10-60 seconds depending on feature depth and aspect ratio.
4. **Overburden**: After the feature is filled, copper continues to build on the wafer surface (overburden). Overburden thickness: 0.5-5 μm, removed by CMP. Excessive overburden increases CMP time and cost.

### Nickel Electroplating

Nickel plating serves as a diffusion barrier and adhesion layer in semiconductor packaging and PCB fabrication.

**Watts bath** (general purpose):
- NiSO₄·6H₂O: 250-350 g/L
- NiCl₂·6H₂O: 40-60 g/L (improves anode dissolution and conductivity)
- H₃BO₃: 30-45 g/L (pH buffer, prevents cathode pH rise and Ni(OH)₂ precipitation)
- Temperature: 50-65°C, pH 3.5-4.5, current density 20-50 mA/cm²
- Cathode current efficiency: ~95% (5% of current goes to H₂ evolution)

**Sulfamate bath** (low-stress, for electroforming):
- Ni(NH₂SO₃)₂: 300-450 g/L
- NiCl₂·6H₂O: 5-15 g/L
- H₃BO₃: 30-45 g/L
- Temperature: 50-60°C, pH 3.5-4.5, current density 20-100 mA/cm²
- Internal stress: 20-50 MPa tensile (vs. 150-250 MPa for Watts bath). The low stress enables thick deposits (up to several mm) without cracking or delamination.
- Applications: Electroformed stampers for CD/DVD/Blu-ray mastering, micro-molds for embossing, precision metal bellows, and rocket engine thrust chamber liners.

### Gold Electroplating

Gold plating provides wire-bondable, corrosion-resistant, low-contact-resistance surfaces for semiconductor die bonding and connector contacts.

**Acid gold bath** (hard gold, for contacts and connectors):
- KAu(CN)₂ (potassium gold cyanide): 4-12 g/L (as Au)
- Citric acid / citrate buffer: pH 3.5-5.0
- Cobalt or nickel additive: 0.1-0.5 g/L (increases hardness from ~60 HK pure gold to 60-90 HK hard gold)
- Temperature: 30-50°C, current density 1-10 mA/cm²
- Deposition rate: ~7 mg/A·min. Gold efficiency: 90-98%.
- Hardness: 60-90 HK (Knoop). Pure soft gold (no Co/Ni additive): ~60 HK.

**ENIG integration**: Gold plating for PCB pads uses a different approach — immersion gold over electroless nickel (see [Electrochemical Surface Processes](electrochemical-processes.md)). The immersion gold process is self-limiting (0.03-0.08 μm thick) because gold displaces nickel from the surface; when all exposed nickel is covered, the reaction stops.

### Tin Electroplating

Tin plating provides solderable surfaces for electronic assembly and component leads.

**Acid stannous sulfate bath**:
- SnSO₄: 20-60 g/L (as Sn)
- H₂SO₄: 50-150 g/L
- Organic additives (phenolsulfonic acid, brighteners): proprietary
- Temperature: 20-30°C, current density 10-50 mA/cm²
- Cathode efficiency: ~90-95%
- Deposit: matte or bright tin, 1-15 μm thickness

**Tin whisker mitigation**: Pure tin develops conductive crystalline filaments (whiskers) over time — a reliability risk in lead-free electronics. Mitigation: post-plating annealing at 150°C for 1 hour (recrystallizes the tin, relieving internal compressive stress that drives whisker growth), or alloying with 2-3% bismuth. Tin-lead (Sn-Pb) plating does not whisker but is banned by RoHS for most applications.

### Process Control & Metrology

**Thickness control** (Faraday's law):
- Mass deposited: m = (I × t × M) / (n × F)
- Where I = current (A), t = time (s), M = molar mass (g/mol), n = electrons per ion, F = 96,485 C/mol
- For copper: m = (I × t × 63.55) / (2 × 96485) = 3.294 × 10⁻⁴ g/C
- Thickness = m / (ρ × A), where ρ = density (8.96 g/cm³ for Cu), A = area
- At 10 mA/cm² for 60 seconds: thickness = (0.01 × 60 × 63.55) / (2 × 96485 × 8.96) = 2.2 μm/cm² × 60s = ~0.22 μm on 1 cm²

**In-situ monitoring**:
- Coulometric integration: integrates current over time to calculate total charge passed (Q = ∫I dt), then applies Faraday's law to predict thickness. Accuracy ±2-5%.
- X-ray fluorescence (XRF): non-destructive thickness measurement. Measures characteristic X-ray emission from plated metal. Accuracy ±1-3% for 0.1-50 μm range.
- Sheet resistance (four-point probe): relates to thickness via ρ = R × t × (w/l). Useful for thin films on insulating substrates.

**Bath analysis and maintenance**:
- Hull cell testing: standardized 267 mL test cell that produces a range of current densities on a single test panel (5-50 mA/cm² across 10 cm length). Used to diagnose bath health, additive balance, and contamination.
- CVS (cyclic voltammetric stripping): measures organic additive concentrations by plating/stripping copper on a rotating disk electrode. The charge required to strip the plated copper is proportional to the effective accelerator/suppressor ratio. Essential for production bath control.
- ICP-OES (inductively coupled plasma optical emission spectroscopy): measures dissolved metal and impurity concentrations in the bath. Critical for monitoring anode dissolution rate and contaminant buildup.

### Copper Damascene in Semiconductor Fabrication

The copper damascene process is integrated into the semiconductor fab flow after photolithography and etch of the dielectric (SiO₂ or low-k material). Each metal layer follows this sequence:

1. **Dielectric deposition**: Deposit 500-1000 nm of SiO₂ or low-k dielectric by CVD or spin-on glass.
2. **Lithography + etch**: Pattern trenches (horizontal wires) and vias (vertical connections) using photolithography and reactive ion etching (RIE). Dual damascene patterns both trenches and vias in a single etch sequence.
3. **Barrier deposition**: Deposit TaN/Ta barrier layer (5-20 nm) by PVD (sputtering) or ALD. The barrier prevents copper from diffusing into the dielectric (copper is a fast diffuser in SiO₂ and creates deep-level traps in silicon that destroy transistor performance). Barrier uniformity is critical — even a 1 nm gap in the barrier causes fatal device failure.
4. **Seed deposition**: Deposit copper seed layer (50-150 nm) by PVD. The seed must be continuous and conformal to provide electrical contact for electroplating. For features below 50 nm, PVD seed coverage becomes marginal — ALD copper seed or direct electroless copper on the barrier are alternatives under development.
5. **Electroplating**: Fill trenches and vias with copper using the acid sulfate + additive bath described above. Bottom-up fill is essential — any voids trapped in the feature cause reliability failures (electromigration-induced open circuits).
6. **CMP planarization**: Remove excess copper and barrier material by chemical mechanical planarization (CMP). Copper CMP uses a colloidal silica slurry with an oxidizer (H₂O₂ or KIO₃) and a corrosion inhibitor (BTA, benzotriazole). The slurry selectively removes copper while the barrier layer acts as an etch stop. After CMP, the copper in trenches and vias is flush with the dielectric surface, and the barrier layer is removed from the field regions.
7. **Cap layer**: Deposit a thin Si₃N₄ or SiC cap layer (30-50 nm) by PECVD to protect the copper surface from oxidation and serve as the etch stop for the next via level.

**Technology node scaling**: At each technology node, the interconnect dimensions shrink, requiring tighter process control:
- 250 nm node (1997): 1.0 μm pitch, 0.6 μm via, 6-8 metal layers
- 130 nm node (2001): 0.35 μm pitch, 0.2 μm via, 8-10 metal layers
- 65 nm node (2005): 0.2 μm pitch, 0.1 μm via, 10-12 metal layers
- 14 nm node (2014): 0.05 μm pitch, 0.025 μm via, 13-15 metal layers
- 5 nm node (2020): 0.03 μm pitch, 0.015 μm via, 14-17 metal layers

At smaller nodes, the barrier and seed layers consume an increasing fraction of the via cross-section, reducing the conductive copper area. This drives the development of thinner barriers (2-3 nm by ALD) and thinner seeds (20-30 nm by CVD or electroless methods).

### Plating Cell Design

**Wafer plating cell** (for semiconductor damascene copper):
- **Vertical cup cell**: The wafer (cathode) is held face-down by a seal ring that exposes only the front surface to the electrolyte. A copper anode sits below. The cell volume is small (2-5 liters) to minimize bath inventory and additive consumption. The seal ring must not damage the wafer edge — vacuum chuck or elastomer O-ring seal.
- **Flow dynamics**: Electrolyte flows upward from the anode toward the wafer at 1-5 L/min, sweeping away hydrogen bubbles and maintaining uniform concentration. Wafer rotation (10-100 rpm) combined with flow creates a uniform diffusion boundary layer across the 300 mm wafer diameter. Edge-to-center uniformity depends on flow rate, rotation speed, and current density — typically ±3-5% across the wafer.
- **Current delivery**: The wafer makes electrical contact through spring-loaded contacts around the periphery (the "ring contacts"). Contact resistance must be low and uniform — any contact with higher resistance causes a local voltage drop and thin plating. Typical contact design: 60-120 beryllium-copper fingers, each carrying 0.5-2 A.
- **Anode basket**: Titanium anode basket filled with copper anode balls (25 mm diameter, phosphorus-doped). The basket provides large anode area for uniform current distribution. As anode balls dissolve, fresh balls are added to maintain the basket fill level.

**Rack plating** (for discrete components):
- Parts are held on titanium or phosphor-bronze racks with individual contacts. Rack design is critical — contacts must hold parts securely, provide good electrical contact, and not shield any surface from the plating bath. Complex parts may need auxiliary anodes (small internal anodes placed inside cavities) to plate recessed areas.
- Barrel plating: Small parts (fasteners, contacts) tumbled in a rotating perforated barrel immersed in the plating bath. The barrel rotation provides electrical contact through the tumbling action. Current density is lower and less uniform than rack plating, but throughput is high and labor is minimal.

### Wastewater Treatment

**Heavy metal removal**:
- Rinse water from copper, nickel, and tin plating contains dissolved metals at 10-500 mg/L (well above discharge limits of 0.5-2 mg/L). Treatment: adjust pH to 9-11 with NaOH → metal hydroxide precipitation (Cu(OH)₂, Ni(OH)₂, Sn(OH)₂) → flocculate with polymer → settle in clarifier → filter sludge → dewater in filter press → dispose as hazardous waste.
- Ion exchange recovery: Chelating resin (iminodiacetic acid type) removes Cu²⁺ and Ni²⁺ from dilute rinse water (1-50 mg/L) with >99% efficiency. When resin is saturated, regenerate with acid (H₂SO₄) to produce concentrated metal sulfate solution, which can be returned to the plating bath (closing the metal loop) or electrowon for metal recovery.

**Cyanide destruction**:
- Alkaline chlorination: Add sodium hypochlorite (NaOCl) to cyanide-containing waste at pH 10-11. First stage: CN⁻ + OCl⁻ → OCN⁻ (cyanate, much less toxic). Second stage: OCN⁻ + 2OCl⁻ + H₂O → CO₂ + N₂ + 2Cl⁻ + 2OH⁻ (complete oxidation). Monitor oxidation-reduction potential (ORP) to confirm complete destruction. Cyanide concentration in treated effluent must be <0.2 mg/L (EPA standard).

### Defect Analysis

**Common electroplating defects and remedies**:
- **Pitting**: Small holes (1-50 μm) in the deposit caused by hydrogen bubbles adhering to the cathode surface. Remedy: increase agitation, add pit-blocking agents (wetting agents), reduce current density.
- **Burning**: Rough, powdery, dark deposits at high-current-density areas (edges, corners, tips). Caused by excessive current density depleting metal ions at the cathode surface. Remedy: reduce current density, improve agitation, use shields or auxiliary cathodes to redistribute current.
- **Voiding in damascene fill**: A cavity within the plated feature caused by plating closing over the feature opening before the bottom is filled. Visible by cross-section SEM. Remedy: optimize accelerator/suppressor ratio, use pulse reverse plating, verify seed layer continuity.
- **Poor adhesion**: Deposit peels or blisters from the substrate. Caused by contaminated surface (oil, oxide), insufficient strike plating, or wrong pre-treatment sequence. Remedy: improve cleaning, add strike layer, verify surface activation.
- **Nodules**: Bumpy, rough projections on the deposit surface. Caused by particulate contamination (anode sludge, airborne particles) in the bath that act as nucleation sites. Remedy: continuous bath filtration (1-5 μm cartridge filters), anode bags (polypropylene fabric), clean room environment for semiconductor plating.

### Plating Bath Chemistry Management

**Copper damascene bath aging and replenishment**:
- The plating bath is a living chemical system that evolves continuously during operation. Copper is consumed from the bath by deposition onto wafers and replenished by dissolution of the copper anode. In theory, the copper concentration remains constant (deposition = anode dissolution). In practice, the anode efficiency slightly exceeds the cathode efficiency (because some cathode current goes to H₂ evolution), causing copper concentration to slowly increase. Monitor Cu²⁺ by titration or atomic absorption weekly.
- Organic additives (accelerator, suppressor, leveler) are consumed at different rates. The accelerator (SPS) is consumed by incorporation into the deposit and by oxidative decomposition at the anode. The suppressor (PEG) is consumed by adsorption and mechanical entrapment. The leveler is consumed by incorporation. Additive replenishment is based on ampere-hours of plating (tracked by coulometric integration). Typical replenishment: 0.5-2 mL of each additive concentrate per ampere-hour of plating current.
- Contamination control: Particulate contamination is the primary cause of yield loss in damascene plating. The bath is continuously filtered through 0.1-0.2 μm membrane filters. Anode bags (woven polypropylene) contain anode sludge particles. Bath piping is electropolished 316L stainless steel or PVDF to prevent particle generation. The plating cell is housed in a Class 100-1000 clean room environment.

**Bath impurity limits for semiconductor-grade copper plating**:
- Iron (Fe): <1 ppm (causes rough deposits)
- Nickel (Ni): <1 ppm
- Zinc (Zn): <0.5 ppm
- Chromium (Cr): <0.1 ppm
- Chloride (Cl⁻): 50-100 ppm (controlled parameter, not impurity)
- Organic carbon (TOC): <100 ppm (excess organics cause voids and poor fill)

### Environmental Regulations

**Restriction of Hazardous Substances (RoHS)**:
- Lead (Pb): Banned in plating at >0.1% by weight. Historically used in tin-lead (Sn-Pb) solder plating; replaced by pure tin, tin-silver, or tin-bismuth alloys.
- Hexavalent chromium (Cr⁶⁺): Banned at >0.1%. Present in chromate conversion coatings over plated zinc. Replaced by trivalent chromium (Cr³⁺) passivates.
- Cadmium (Cd): Banned at >0.01%. Historically used for aerospace fastener plating; replaced by zinc-nickel alloy (12-15% Ni).

**REACH and wastewater regulations**:
- Per- and polyfluoroalkyl substances (PFAS): Some plating bath formulations contain PFAS-based surfactants and mist suppressants. Under regulatory scrutiny — replacements under development.
- Metal discharge limits: EPA Clean Water Act limits for electroplating wastewater discharge: Cu <0.5 mg/L, Ni <0.5 mg/L, Cr <0.5 mg/L, Cd <0.05 mg/L, Pb <0.1 mg/L, CN⁻ <0.2 mg/L. Achieved by chemical precipitation + ion exchange + activated carbon treatment.

### See Also

- **[Anodizing](anodizing.md)**: Electrochemical oxide growth on aluminum and titanium
- **[Electrochemical Surface Processes](electrochemical-processes.md)**: Electropolishing, electroforming, and electroless plating
- **[Electrolysis](../chemistry/electrolysis.md)**: Fundamental electrochemistry, copper electrorefining, Faraday's law
- **[Metal Finishing](../metals/finishing.md)**: General electroplating for industrial applications
- **[VLSI Scaling](../vlsi-scaling/advanced-processes.md)**: Copper damascene integration in semiconductor fabrication

---

*Part of the [Bootciv Tech Tree](../index.md) • [Electrochemistry & Plating](./index.md) • [All Domains](../index.md)*

