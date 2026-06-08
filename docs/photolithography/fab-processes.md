# Core Fab Processes

> **Node ID**: photolithography.fab-processes
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`chemistry.dopant-etch-gases`](../chemistry/dopant-etch-gases.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md), [`metals.aluminum-semiconductor-grade`](../metals/index.md), [`vacuum.pumps`](../vacuum/pumps.md)
> **Enables**: [`chemistry.packaging-testing`](../chemistry/packaging-testing.md), [`computing.electronic`](../computing/electronic.md), [`glass.photomask-substrates`](../glass/photomask-substrates.md), [`metals.specialty-semiconductor`](../metals/specialty-semiconductor.md), [`vlsi-scaling.advanced-processes`](../vlsi-scaling/advanced-processes.md), [`vlsi-scaling.continuous-scaling`](../vlsi-scaling/continuous-scaling.md), [`vlsi-scaling.eda-design`](../vlsi-scaling/eda-design.md)
> **Timeline**: Years 40-70
> **Outputs**: fab_processes, early_ics, msi, patterned_oxide, doped_regions, metal_interconnects
> **Critical**: Yes — core IC fabrication processes are the foundation of all semiconductor manufacturing

## Core Fab Processes

![Moore evermore in Computer History — Happy 50th Birthday to the Law! (16318918399)](../images/photolithography/photolithography_fab-processes.jpg)

> *My article is on p.36 of the &lt;a href="http://s3data.computerhistory.org/core/core-2015.pdf" rel="noreferrer nofollow"&gt;Computer History Museum Core&lt;/a&gt;. Moore's Law is both a prediction and an abstraction The popular perception of Moore’s Law is that computer chips are compounding in their complexity at near constant per unit cost. This is one of the many abstractions of Moore’s Law, and it relates to the compounding of transistor density in two dimensions. Others relate to speed (the signals have less distance to travel) or computational power (speed x density). Unless you work for a chip company and focus on fab-yield optimization, you do not care about transistor counts. Integrated circuit customers do not buy transistors. Consumers of technology purchase computational speed and data storage density. When recast in these terms, Moore’s Law is no longer a transistor-centric metric, and this abstraction allows for longer-term analysis. What Moore observed in the belly of the early IC industry was a derivative metric, a refracted signal, from a longer-term trend, a trend that begs various philosophical questions and predicts mind-bending futures. Humanity’s compounding capacity to compute. Ray Kurzweil’s abstraction of Moore’s Law shows computational power on a logarithmic scale, and finds a double exponential curve that holds over 110 years! A straight line would represent a geometrically compounding curve of progress. [see graph in first comment below] Through five paradigm shifts – such as electro-mechanical calculators and vacuum tube computers – the computational power that $1000 buys has doubled every two years. For the past 30 years, it has been doubling every year. Each dot is the frontier of computational price performance of the day. One machine was used in the 1890 Census; one cracked the Nazi Enigma cipher in World War II; one predicted Eisenhower’s win in the 1956 Presidential election. Many of them can be seen in the Computer History Museum. Each dot represents a human drama. Prior to Moore’s first paper in 1965, none of them even knew they were on a predictive curve. Each dot represents an attempt to build the best computer with the tools of the day. Of course, we use these computers to make better design software and manufacturing control algorithms. And so the progress continues. Notice that the pace of innovation is exogenous to the economy. The Great Depression and the World Wars and various recessions do not introduce a meaningful change in the long-term trajectory of Moore’s Law. Certainly, the adoption rates, revenue, profits and economic fates of the computer companies behind the various dots on the graph may go though wild oscillations, but the long-term trend emerges nevertheless. Any one technology, such as the CMOS transistor, follows an elongated S-shaped curve of slow progress during initial development, upward progress during a rapid adoption phase, and then slower growth from market saturation over time. But a more generalized capability, such as computation, storage, or bandwidth, tends to follow a pure exponential – bridging across a variety of technologies and their cascade of S-curves. In the modern era of accelerating change in the tech industry, it is hard to find even five-year trends with any predictive value, let alone trends that span the centuries. I would go further and assert that this is the most important graph ever conceived. Why is this the most important graph in human history? A large and growing set of industries depends on continued exponential cost declines in computational power and storage density. Moore’s Law drives electronics, communications and computers and has become a primary driver in drug discovery, biotech and bioinformatics, medical imaging and diagnostics. As Moore’s Law crosses critical thresholds, a formerly lab science of trial and error experimentation becomes a simulation science, and the pace of progress accelerates dramatically, creating opportunities for new entrants in new industries. Boeing used to rely on the wind tunnels to test novel aircraft design performance. Ever since CFD modeling became powerful enough, design moves to the rapid pace of iterative simulations, and the nearby wind tunnels of NASA Ames lie fallow. The engineer can iterate at a rapid rate while simply sitting at their desk. Every industry on our planet is going to become an information business. Consider agriculture. If you ask a farmer in 20 years’ time about how they compete, it will depend on how they use information, from satellite imagery driving robotic field optimization to the code in their seeds. It will have nothing to do with workmanship or labor. That will eventually percolate through every industry as IT innervates the economy. Non-linear shifts in the marketplace are also essential for entrepreneurship and meaningful change. Technology’s exponential pace of progress has been the primary juggernaut of perpetual market disruption, spawning wave after wave of opportunities for new companies. Without disruption, entrepreneurs would not exist. Moore’s Law is not just exogenous to the economy; it is why we have economic growth and an accelerating pace of progress. At DFJ, we see that in the growing diversity and global impact of the entrepreneurial ideas that we see each year. The industries impacted by the current wave of tech entrepreneurs are more diverse, and an order of magnitude larger than those of the 90’s — from automobiles and aerospace to energy and chemicals. At the cutting edge of computational capture is biology; we are actively reengineering the information systems of biology and creating synthetic microbes whose DNA is manufactured from bare computer code and an organic chemistry printer. But what to build? So far, we largely copy large tracts of code from nature. But the question spans across all the complex systems that we might wish to build, from cities to designer microbes, to computer intelligence. Reengineering engineering As these systems transcend human comprehension, we will shift from traditional engineering to evolutionary algorithms and iterative learning algorithms like deep learning and machine learning. As we design for evolvability, the locus of learning shifts from the artifacts themselves to the process that created them. There is no mathematical shortcut for the decomposition of a neural network or genetic program, no way to "reverse evolve" with the ease that we can reverse engineer the artifacts of purposeful design. The beauty of compounding iterative algorithms (evolution, fractals, organic growth, art) derives from their irreducibility. And it empowers us to design complex systems that exceed human understanding. Why does progress perpetually accelerate? All new technologies are combinations of technologies that already exist. Innovation does not occur in a vacuum; it is a combination of ideas from before. In any academic field, the advances today are built on a large edifice of history. . This is why major innovations tend to be 'ripe' and tend to be discovered at the nearly the same time by multiple people. The compounding of ideas is the foundation of progress, something that was not so evident to the casual observer before the age of science. Science tuned the process parameters for innovation, and became the best method for a culture to learn. From this conceptual base, come the origin of economic growth and accelerating technological change, as the combinatorial explosion of possible idea pairings grows exponentially as new ideas come into the mix (on the order of 2^n of possible groupings per Reed’s Law). It explains the innovative power of urbanization and networked globalization. And it explains why interdisciplinary ideas are so powerfully disruptive; it is like the differential immunity of epidemiology, whereby islands of cognitive isolation (e.g., academic disciplines) are vulnerable to disruptive memes hopping across, much like South America was to smallpox from Cortés and the Conquistadors. If disruption is what you seek, cognitive island-hopping is good place to start, mining the interstices between academic disciplines. It is the combinatorial explosion of possible innovation-pairings that creates economic growth, and it’s about to go into overdrive. In recent years, we have begun to see the global innovation effects of a new factor: the internet. People can exchange ideas like never before Long ago, people were not communicating across continents; ideas were partitioned, and so the success of nations and regions pivoted on their own innovations. Richard Dawkins states that in biology it is genes which really matter, and we as people are just vessels for the conveyance of genes. It’s the same with ideas or “memes”. We are the vessels that hold and communicate ideas, and now that pool of ideas percolates on a global basis more rapidly than ever before. In the next 6 years, three billion minds will come online for the first time to join this global conversation (via inexpensive smart phones in the developing world). This rapid influx of three billion people to the global economy is unprecedented in human history, and so to, will the pace of idea-pairings and progress. We live in interesting times, at the cusp of the frontiers of the unknown and breathtaking advances. But, it should always feel that way, engendering a perpetual sense of future shock.*

> *Image: Steve Jurvetson from Los Altos, USA, CC BY 2.0*

### Thermal Oxidation

Thermal oxidation grows SiO₂ directly on the silicon wafer surface by exposing it to oxygen or steam at 900-1200°C. Unlike deposited oxides (from CVD), thermally grown oxide has the highest electrical quality because it forms a continuous, dense Si-O network directly from the silicon lattice — making it the only viable choice for gate dielectrics where even a single defect can destroy a transistor. Two variants cover the full thickness range: dry oxidation (Si + O₂ → SiO₂, slow but highest quality) for gate oxides, and wet oxidation (Si + 2H₂O → SiO₂, ~5-10× faster) for thick field and masking oxides.

**[Deal-Grove oxidation model](../glossary/deal-grove-oxidation-model.md)** (predicts oxide thickness as a function of time and temperature):
- Linear-parabolic rate equation: x² + Ax = B(t + τ), where x = oxide thickness, t = time, A and B are temperature-dependent rate constants, τ is the time offset accounting for initial oxide.
- **[Linear regime](../glossary/linear-regime.md)** (thin oxide, surface-reaction limited): x ≈ (B/A)·t. B/A is the linear rate constant.
- **[Parabolic regime](../glossary/parabolic-regime.md)** (thick oxide, diffusion limited): x ≈ √(B·t). B is the parabolic rate constant.
- **Typical growth rates at 1000°C**:
  - Dry O₂: ~2 nm/min (linear regime), slows dramatically in parabolic regime. 100 nm gate oxide takes ~2 hours. Dense, high-quality oxide (breakdown >10 MV/cm).
  - Wet O₂ (steam): ~10 nm/min. 500 nm field oxide takes ~1 hour. Contains more OH bonds, slightly lower quality, but acceptable for masking and insulation.
- **Furnace design**: Horizontal or vertical quartz tube furnace, 3-zone resistive heating (±1°C uniformity over 150 mm zone). O₂ or H₂O (bubbler at 95-98°C) flows through tube at 1-10 L/min. Boat holds 25-200 wafers. Push/pull rate <5 cm/min to avoid thermal stress (warp). The 3-zone control is critical — a ±1°C non-uniformity across the wafer produces measurable gate oxide thickness variation, which directly translates to threshold voltage spread across the die.

**Oxide uses and target thicknesses**:
- Gate oxide: 5-100 nm (dry O₂, highest quality — breakdown field >10 MV/cm, defect density <0.1 cm⁻²)
- Field oxide (isolation): 300-1000 nm (wet O₂ — thicker oxide prevents parasitic channel formation under interconnects)
- Masking oxide (for ion implant or diffusion): 50-200 nm (dry or wet — must be thick enough to stop the implanted species or block dopant diffusion)
- Passivation: 500-1000 nm ([CVD](cvd.md) SiO₂ or SiNₓ — not thermal, because the wafer already has metal interconnects that cannot survive >660°C)

**Why thermal oxidation matters for integration**: Thermal oxidation is unique among fab processes because it consumes the silicon substrate to grow the oxide. This means the oxide-silicon interface is atomically clean and continuous — no pinholes, no adhesion failures. However, it also means the oxide grows into the wafer as well as above it (~44% of the oxide thickness is below the original silicon surface). This must be accounted for in layout design: after growing a 500 nm field oxide, the silicon surface under the oxide is ~220 nm below the active area surface, creating topography that later CMP steps must planarize.

### Etching

Etching removes material selectively through the photoresist mask to transfer the printed pattern into the underlying film. Two broad categories serve different needs:

- **Wet etching**: Liquid chemicals (HF for SiO₂, KOH/TMAH for Si, H₃PO₄ for Si₃N₄, phosphoric-acid blends for Al). Isotropic for most materials (undercuts the mask), inexpensive, and high-throughput for large features (>3 μm). See [Wet Etch Processes](#wet-etch-processes) below for detailed etch rates and selectivities.
- **Dry/plasma etching**: [Plasma etching (RIE & DRIE)](plasma-etching.md) uses reactive ion plasmas to achieve anisotropic (vertical) profiles essential for sub-micron features. The dedicated [Plasma Etching](plasma-etching.md) article covers RIE reactor design, etch gas chemistries (fluorocarbon for dielectrics, chlorine for metals, SF₆ for silicon), selectivity optimization, and the Bosch DRIE process for high-aspect-ratio structures.

**Quick-reference etch rates** (typical values):
| Material | Etchant | Rate | Selectivity vs. photoresist | Notes |
|---|---|---|---|---|
| SiO₂ | Buffered HF (BHF 7:1) | 70-100 nm/min | ~5:1 (SiO₂:PR) | Isotropic, controlled etch |
| SiO₂ | Concentrated HF (49%) | 1-2 μm/min | ~1:1 | Fast, aggressive — hard to control |
| Si | KOH (30%, 80°C) | ~1.1 μm/min (100) | ~50:1 (Si:SiO₂) | Anisotropic — stops on {111} planes |
| Si | TMAH (25%, 80°C) | ~0.6 μm/min | ~20:1 (Si:SiO₂) | CMOS-compatible (no alkali metals) |
| Si₃N₄ | H₃PO₄ (85%, 155°C) | ~5-10 nm/min | ~10:1 (Si₃N₄:SiO₂) | Hot phosphoric acid — reflux system needed |
| Al | H₃PO₄:CH₃COOH:HNO₃ (16:3:1, 50°C) | ~0.5-1.0 μm/min | ~5:1 (Al:PR) | Standard Al wet etch |
| Poly-Si | CF₄/O₂ plasma (RIE) | ~50-100 nm/min | ~5:1 (poly-Si:SiO₂) | Anisotropic with sidewall passivation |
| Si | SF₆ or CF₄ plasma (RIE) | ~100-500 nm/min | Variable | Selectivity depends on chemistry and bias |

### Deposition

Thin film deposition adds material layers to the wafer surface — gate electrodes, interlayer dielectrics, passivation, and metal interconnects. Three deposition mechanisms serve different roles in the process flow:

- **[Chemical Vapor Deposition (CVD)](cvd.md)**: Gas-phase precursors react or decompose at the wafer surface to form solid films. CVD produces highly conformal coatings that cover steps, fill trenches, and coat complex geometries uniformly. The three main variants — APCVD (atmospheric, simple but poor step coverage), LPCVD (low-pressure, highest quality, used for gate poly-Si and Si₃N₄ diffusion barriers), and PECVD (plasma-enhanced, low-temperature for films on metallized wafers) — are covered in detail in the [CVD article](cvd.md), along with tungsten CVD for contact/via plug fill and gas handling requirements.

- **[Physical Vapor Deposition (PVD)](pvd.md)**: Sputtering and evaporation physically transport atoms from a source target to the substrate without chemical reaction. Sputtering (Ar⁺ ion bombardment of the target) provides moderate step coverage and is the workhorse for aluminum interconnects and Ti/TiN barrier layers. Evaporation (thermal or e-beam) offers higher purity but poor step coverage due to line-of-sight deposition. The [PVD article](pvd.md) covers sputtering modes (DC, RF, magnetron), evaporation processes, vacuum requirements, target materials, and thin film monitoring (QCM).

- **Epitaxy**: Growing a single-crystal layer on a single-crystal substrate (used for buried layers and advanced device structures, beyond the scope of early fab).

### Doping

Doping introduces electrically active impurities into the silicon lattice to create n-type (electron-rich) and p-type (hole-rich) regions — the source, drain, well, and channel regions of transistors.

- **Thermal diffusion** (simpler, earlier): Expose the wafer to a dopant source at high temperature (900-1050°C). n-type: phosphorus (POCl₃ gas, or solid P₂O₅). p-type: boron (BBr₃ gas, or solid B₂O₃). Dopant atoms diffuse into silicon from the surface, with junction depth controlled by temperature and time. Diffusion is isotropic (dopants spread laterally under the mask edge) and the surface concentration is fixed by the solid solubility limit. Adequate for large-geometry processes (>3 μm).

- **[Ion implantation](ion-implantation.md)** (more precise, later): A particle accelerator fires dopant ions into the wafer at controlled energies (10 keV to several MeV), independently specifying dose (atoms/cm²) and junction depth (via ion energy). Ion implantation replaced thermal diffusion for all modern processes because it provides precise dose control (±1%), self-aligned doping (the poly-Si gate masks the channel), and selectable dopant species (B⁺, BF₂⁺, P⁺, As⁺). The [Ion Implantation article](ion-implantation.md) covers the full equipment chain (ion source, mass analyzer, acceleration column, beam scanning), process parameters (dose, energy, channeling prevention), and annealing methods (furnace, RTA, spike, laser) required to activate the implanted dopants and repair crystal damage.

### Metallization

Metallization creates the conductive interconnects that wire transistors together into circuits. In the planar process, metal is deposited as a blanket film, then patterned by photolithography and etching to form the interconnect lines. Aluminum (or Al-Cu/Al-Si alloys) is the standard first-generation interconnect metal, with copper replacing it for advanced nodes due to lower resistivity (1.7 vs. 2.7 μΩ·cm).

**Single-level metallization** (first ICs): Deposit 0.5-1.5 μm aluminum by [sputtering (PVD)](pvd.md) or evaporation. Pattern by wet etch (H₃PO₄:CH₃COOH:HNO₃ at 40-50°C) or dry etch (Cl₂/BCl₃ plasma — see [Plasma Etching](plasma-etching.md)). The metal makes contact to source, drain, and gate through contact holes etched in the interlayer dielectric. A forming gas anneal (400-450°C, N₂/H₂ 90/10, 30 min) improves Al-Si contact resistance and passivates dangling bonds at the Si-SiO₂ interface.

**Multi-level metallization** (advanced ICs): Modern ICs require 4-15+ metal layers to route signals and power across the chip. Each additional metal layer requires: deposit interlayer dielectric ([CVD](cvd.md) SiO₂) → planarize by [CMP](cmp.md) → etch via holes → fill vias (tungsten CVD or copper electroplate) → deposit and pattern next metal layer. The transition from single-level to multi-level metallization is gated by planarization — without CMP, topography accumulates with each layer until photolithography fails at the depth-of-focus limit.

**Metal alloy considerations**: Pure aluminum suffers from electromigration (metal atoms migrate under high current density, eventually causing open circuits) and junction spiking (Al dissolves Si at contacts, shorting through shallow junctions). Al-Cu 0.5% alloy suppresses electromigration by factor of 10-50×. Al-Si 1% saturates the aluminum with silicon to prevent further dissolution from the substrate. Both alloys are sputtered from alloy targets — see [PVD](pvd.md) for process details.

## Process Metrology
Every process step must be measured. "If you can't measure it, you can't control it."

- **[Ellipsometry](../glossary/ellipsometry.md)** (film thickness): Monochromatic or spectroscopic light (632.8 nm HeNe laser, or broad spectrum 250-1000 nm) reflects off the thin film surface at a known angle (70-75°). Measures change in polarization (Ψ, Δ) upon reflection. Fits to optical model (Cauchy or Sellmeier dispersion) to extract film thickness and refractive index. Accuracy: ±0.5 nm for oxides, ±2 nm for thicker films. Measures: SiO₂, SiNₓ, photoresist, poly-Si, metals (with appropriate model). Non-destructive, fast (~1 sec per site). Maps wafer uniformity (49-point or 121-point contour map).
- **[Four-point probe](../glossary/four-point-probe.md)** (sheet resistance): Four collinear tungsten probes (1 mm spacing) contact the wafer surface. Outer two probes pass constant current I (1 μA-100 mA), inner two measure voltage V. Sheet resistance Rs = (π/ln 2)·(V/I) ≈ 4.532·(V/I) Ω/sq. Measures doped layers (diffused or implanted), metal films, poly-Si. Corrects for wafer diameter with geometric correction factors. Accuracy ±1%. For metal film thickness: t = ρ/Rs where ρ is bulk resistivity.
- **[Dektak / profilometer](../glossary/dektak-profilometer.md)** (step height): Diamond-tipped stylus (12.5-50 μm radius, 1-15 mg force) scans across a step in the film surface (e.g., where resist or oxide was etched away). Measures vertical displacement with sub-nm resolution (typically ±1-5 nm over 1 μm step range). Used for: etch depth verification, film thickness (after patterning a step), planarization uniformity. Trade-off: higher stylus force = better surface contact but risks scratching soft films (photoresist, aluminum). Also measures surface roughness (Ra, Rq).
- **Optical microscope inspection**: Brightfield and darkfield illumination. Detects pattern defects (missing features, bridges, particles), alignment errors, etch completeness. Magnification 50×-1000×. Essential for yield troubleshooting. Operators visually inspect sample wafers from each lot.
- **Particle counting**: Laser scattering particle counters measure airborne particles (in cleanroom monitoring) or on wafer surfaces (bare wafer or patterned wafer inspection). Defect density (particles/cm² per process step) directly predicts yield: Yield = (1 - D·A)ⁿ where D = defect density, A = die area, n = process steps.

## Planar Process & Integration

The planar process is the fundamental IC manufacturing method: sequential layers of patterned oxide, doped regions, and metal are built up on a flat silicon surface. Each layer requires its own photolithographic mask, and the order of operations is critical — later steps must not damage or alter the results of earlier steps. This is why thermal budget management, contamination control, and process sequencing are the core engineering challenges of IC fabrication.

**Complexity progression**:
- **Start simple**: Single-layer metal, large features (10+ μm), few mask layers (5-7 masks)
- **Progress to**: Multiple metal layers, smaller features, more mask layers (10-30+ masks)
- **Early targets**: Simple logic gates, flip-flops, small counters (SSI → MSI → LSI)

**Example: NMOS transistor fabrication flow** (7 mask layers):

This flow illustrates how all unit processes — oxidation, photolithography, etching, deposition, doping, metallization — interlock in a specific sequence. Each step's output becomes the next step's input, and process quality at every stage compounds into final yield.

1. **Starting wafer**: p-type <100> Si, 5-20 Ω·cm, cleaned (RCA-1: NH₄OH/H₂O₂/H₂O at 75-80°C to remove organics; RCA-2: HCl/H₂O₂/H₂O at 75-80°C to remove metals; final HF dip to strip native oxide).
2. **Mask 1 — Active area**: Grow 500 nm SiO₂ (wet oxidation, 1000°C, ~2 hours). Spin photoresist. Expose through Mask 1 (active areas = where transistors will be). Develop. Etch SiO₂ in buffered HF (BHF: NH₄F:HF 7:1, ~700 nm/min). Strip resist. Result: oxide islands defining transistor regions in thick field oxide.
3. **Mask 2 — Gate oxidation**: Grow 50-100 nm gate oxide (dry oxidation, 900-1000°C, 30-60 min — thin, high-quality oxide). This is the MOST CRITICAL step — gate oxide quality determines transistor performance. Target: breakdown voltage >8 MV/cm. Any contamination (particles, metallic impurities) in the gate oxide creates a permanent defect. The furnace must be dedicated to gate oxidation only.
4. **Mask 3 — Polysilicon gate**: Deposit 300-500 nm poly-Si by [LPCVD](cvd.md) (SiH₄ at 620°C, ~10 nm/min). Dope n+ (POCl₃ diffusion or [ion implant](ion-implantation.md)). Spin resist, expose Mask 3, develop, dry etch poly-Si (CF₄/O₂ plasma — see [Plasma Etching](plasma-etching.md)). Strip resist. Result: polysilicon gate electrodes, self-aligned to source/drain.
5. **Source/drain implant**: [Ion implant](ion-implantation.md) phosphorus (dose 10¹⁵/cm², 50-100 keV) or POCl₃ pre-deposition + drive-in (900°C, 30 min). Polysilicon gate acts as self-aligned mask — source/drain automatically aligned to gate edges. This self-alignment is the key advantage of the silicon-gate process over the older metal-gate process, where gate-source/drain alignment required conservative mask overlaps that wasted area and added parasitic capacitance.
6. **Mask 4 — Contact holes**: Deposit 500 nm SiO₂ by [CVD](cvd.md). Spin resist, expose Mask 4 (contact openings over source, drain, gate). Etch oxide in BHF. Strip resist. The contact holes must be etched cleanly to the silicon surface — any residual oxide adds contact resistance.
7. **Mask 5 — Metal**: Deposit 1 μm aluminum by [sputtering (PVD)](pvd.md) or evaporation. Spin resist, expose Mask 5 (interconnect pattern). Wet etch Al (H₃PO₄:CH₃COOH:HNO₃ at 40-50°C, ~1 μm/min). Strip resist. The metal layer wires all transistors together into the circuit.
8. **Mask 6 — Passivation**: Deposit 1 μm SiO₂ or SiNₓ by [PECVD](cvd.md). Expose Mask 6 (bond pad openings). Etch. Strip resist. Passivation protects the circuit from moisture, ions (Na⁺), and mechanical damage.
9. **Alloy/anneal**: 400-450°C in forming gas (N₂/H₂ 90/10) for 30 min. Hydrogen passivates dangling bonds at the Si-SiO₂ interface (reducing interface trap density), and the anneal improves Al-Si contact by forming a thin alloyed region.
10. **Test, dice, package, wire bond**: See [Packaging & Testing](../chemistry/packaging-testing.md).

**Why the order matters**: The process sequence is constrained by temperature — high-temperature steps (>800°C) must come before low-temperature steps. Once the aluminum interconnects are deposited (step 7), no process above 660°C (Al melting point) can be performed. This is why gate oxidation (step 3) cannot be moved later, and why [PECVD](cvd.md) (200-400°C) is used for passivation (step 8) instead of LPCVD (550-900°C).

**Yield expectations**: First IC runs will have <1% yield. Iteration is essential. Defect density, contamination control, and process uniformity all improve with practice. A mature process might achieve 50-90% yield on simple circuits. Yield follows the Poisson model: Yield = (1 - D·A)ⁿ, where D = defect density (defects/cm² per layer), A = die area, n = number of process layers. Reducing defect density by a factor of 10 (through cleanroom discipline, process optimization, and contamination control) can increase yield from near-zero to economically viable.

## Hazards & Safety

- **Hydrofluoric acid (HF)** — CRITICAL: HF at 5-49 % concentration causes severe, deep-tissue burns that may not be immediately painful — pain onset can be delayed hours while fluoride ions destroy bone and tissue. **Always have calcium gluconate gel (2.5 %) immediately available at every HF station.** Apply to any skin contact immediately, then seek emergency medical care. Wear heavy-duty acid gloves (Neoprene or thick nitrile), face shield, acid apron, and work only in a fume hood. HF burns can be fatal at body surface area exposures as small as 2-5 %.
- **POCl₃ doping**: Phosphorus oxychloride reacts violently with moisture to produce phosphoric acid and HCl gas (corrosive, toxic). Use in enclosed, gas-cabinet-fed furnace tubes with toxic-gas monitoring (HCl detector). Exhaust gas scrubbers (caustic wet scrubber) mandatory. Leak protocol: evacuate area, wear self-contained breathing apparatus (SCBA).
- **Forming gas (N₂/H₂ 90/10)**: The forming gas mixture contains 10 % hydrogen — above the lower explosive limit (LEL = 4 % in air). While the nitrogen diluent raises the minimum ignition energy, leaks in confined spaces can create an explosive H₂/air mixture (4-75 % in air). Use hydrogen gas detectors in furnace areas; ensure ventilation rates prevent accumulation. Never use forming gas near ignition sources.
- **Furnace temperatures (800-1200 °C)**: Severe burn hazard. Use heat-resistant gloves (Kevlar, rated to 1000 °C) and face shield when loading/unloading wafer boats. Quartz furnace tubes are fragile when hot — avoid thermal shock (push/pull boats slowly, <5 cm/min). Allow furnaces to cool below 200 °C before maintenance.
- **Plasma/RIE gases**: SF₆ (GWP 23,900× CO₂), CF₄ (GWP 6,630× CO₂), and NF₃ (GWP 17,200× CO₂) are potent greenhouse gases. Install point-of-use abatement (burn boxes or plasma destruct units, >99 % destruction efficiency) on all exhaust lines. NF₃ and CF₄ also produce toxic byproducts (HF, COF₂) in plasma — downstream scrubbing required.

## Wet Etch Processes

Wet etching uses liquid chemicals to dissolve materials isotropically. It is simple, low-cost, and high-throughput, making it the workhorse for large-geometry (>3 μm) processes. For sub-micron features requiring anisotropic profiles, see [Plasma Etching](plasma-etching.md).

**Silicon dioxide etching**:
- **Buffered HF (BHF)**: NH₄F:HF 7:1 mixture. Etch rate 70-100 nm/min for thermal SiO₂. The ammonium fluoride buffers the HF concentration, maintaining a stable etch rate over time. Selectivity to photoresist ~5:1. Selectivity to silicon >100:1 (HF does not attack crystalline silicon). Temperature: room temperature (20-25°C). Used for: contact hole opens, gate oxide removal, general oxide patterning.
- **Dilute HF (DHF)**: HF:H₂O at 1:10 to 1:100. Etch rate 20-30 nm/min for 1:10 dilution. Used for: thin oxide stripping, native oxide removal, pre-deposition cleaning. Lower attack rate on photoresist than BHF.
- **Vapor HF**: HF vapor etches SiO₂ without liquid contact. Useful for stiction-sensitive MEMS structures and for etching under suspended structures where liquid cannot penetrate.

**Silicon nitride etching**:
- **Hot phosphoric acid**: H₃PO₄ at 155-180°C in a reflux system (condenser returns evaporated acid). Etch rate: 5-10 nm/min for Si₃N₄. Selectivity to SiO₂: 10:1 (phosphoric attacks nitride much faster than oxide). Selectivity to silicon: >50:1. The high temperature requires a reflux condenser to prevent acid evaporation and maintain constant concentration. Silicon nitride is used as a hard mask and as a selective etch stop because it resists most silicon and oxide etchants.

**Silicon anisotropic wet etching**:
- **KOH (potassium hydroxide)**: 30-45% KOH in water at 70-85°C. Etch rate for Si <100>: ~1.1 μm/min (at 30%, 80°C). Etch rate ratio <100>:<111> ≈ 100:1. The {111} crystal planes etch ~100× slower than {100} planes, producing precise V-grooves, pyramidal pits, and thin membranes bounded by {111} sidewalls. Alignment of mask features to the <110> flat is critical: a 1° misalignment produces significant undercut.
- **TMAH (tetramethylammonium hydroxide)**: 5-25% in water at 70-90°C. Etch rate ~0.6 μm/min at 25%, 80°C. CMOS-compatible (TMAH is an organic base — no alkali metal contamination). Selectivity to SiO₂: ~20:1 (lower than KOH's ~50:1). Smoother sidewalls than KOH but slower etch rate.

## Planarization

### Chemical-Mechanical Planarization (CMP)

CMP produces atomically flat surfaces by pressing the wafer face-down against a rotating pad with abrasive slurry, combining chemical dissolution with mechanical abrasion. CMP is the enabling technology for multi-level interconnect — without planarization, each deposited layer follows the topography of the layer beneath, accumulating steps that exceed the photolithography depth of focus. The [CMP article](cmp.md) covers the Preston equation governing removal rate, oxide/tungsten/copper CMP processes, pad materials and conditioning, endpoint detection, post-CMP cleaning, and defect control (dishing, erosion, scratches).

**Key CMP concepts for process integration**:
- Oxide CMP planarizes the interlayer dielectric before via patterning, ensuring a flat surface for the next photolithography step. Removal rate: 100-300 nm/min with colloidal silica slurry at pH 10-11.
- Tungsten CMP removes excess W after plug fill, leaving only tungsten plugs in the contact/via holes. Selectivity W:SiO₂ >10:1 ensures the surrounding oxide is preserved.
- Copper CMP (with BTA corrosion inhibitor and glycine complexing agent) enables the dual-damascene interconnect process used for advanced nodes. Two-step process: bulk removal at 300-500 nm/min, then buff step at 50-100 nm/min to minimize dishing.

### Tungsten Plug Process

Contact holes and vias between metal layers must be filled with a conductive material. Aluminum sputtering cannot fill high-aspect-ratio holes (it bridges the top, leaving voids). The tungsten plug process solves this:

1. **Barrier/adhesion layer**: Deposit 20-50 nm TiN by [sputtering (PVD)](pvd.md) or CVD. TiN prevents WF₆ from reacting with the underlying SiO₂ or silicon.
2. **Tungsten CVD fill**: WF₆ + 3H₂ → W + 6HF at 300-400°C (see [CVD](cvd.md) for full tungsten CVD details). Tungsten nucleates from the bottom and sidewalls, filling void-free. Deposition rate: 50-200 nm/min.
3. **CMP etchback**: Excess tungsten removed by [CMP](cmp.md) (Fe(NO₃)₃ or H₂O₂-based slurry with Al₂O₃ abrasive). Selectivity W:SiO₂ >10:1.

## Process Integration

Process integration is the engineering discipline of ordering 50-100+ individual steps (oxidation, deposition, lithography, etch, implant, anneal, CMP, clean) into a manufacturable sequence where each step is compatible with all previous steps and does not compromise the final device. The process flow is the recipe for building an IC — every transistor, interconnect, and isolation structure is defined by the sequence, parameters, and mask layers used.

### Front-End-of-Line (FEOL) vs. Back-End-of-Line (BEOL)

The process flow divides naturally into two thermal regimes:

**FEOL** (transistor formation): All high-temperature steps (>800°C) must occur here, before any metal is deposited. FEOL creates the transistors: isolation regions (LOCOS or shallow trench), gate oxide, polysilicon gates, source/drain implants, and spacer formation. The thermal budget is consumed during FEOL — total exposure above 900°C must be limited to 2-3 hours after source/drain implant to prevent excessive dopant diffusion that would widen junctions beyond specification.

**BEOL** (interconnect formation): All steps after the first metal deposition are constrained to <450°C (the forming gas anneal temperature) to avoid melting aluminum interconnects (660°C) or degrading metal-semiconductor contacts. BEOL creates the wiring hierarchy: contact fill, Metal 1, interlayer dielectric, via fill, Metal 2, and so on up to 15+ metal layers in advanced nodes. [PECVD](cvd.md) at 200-400°C deposits dielectrics; [PVD](pvd.md) at <300°C deposits metals; [CMP](cmp.md) planarizes between layers.

### Two-Level Metal CMOS Process Sequence

This sequence illustrates how FEOL and BEOL unit processes interlock for a CMOS IC with two metal layers. Each numbered step may require sub-steps (clean, coat, expose, develop, etch, strip, measure) — a full process flow for even a simple IC contains 80-150 individual operations.

1. **Starting wafer**: p-type or n-type <100> Si, 5-20 Ω·cm, RCA clean
2. **Isolation**: LOCOS (grow pad oxide → deposit Si₃N₄ by [LPCVD](cvd.md) → pattern → wet oxidize exposed silicon → strip nitride) or shallow trench isolation (etch trenches → fill with [CVD](cvd.md) SiO₂ → [CMP](cmp.md) planarize)
3. **Well formation**: [Ion implant](ion-implantation.md) n-well and p-well regions (B⁺ for p-well, P⁺ for n-well, MeV energies for deep wells), followed by high-temperature drive-in anneal (1000-1050°C, 4-8 hours)
4. **Gate oxidation**: Grow 5-20 nm gate oxide (dry O₂ at 900-1000°C). Most critical dielectric in the process — requires dedicated clean furnace, ultra-pure O₂, and pre-oxidation RCA clean.
5. **Polysilicon gate**: Deposit 200-400 nm poly-Si by [LPCVD](cvd.md) (SiH₄ at 620°C). Dope n+ and p+ (POCl₃/BBr₃ diffusion or [ion implant](ion-implantation.md)). Pattern gate electrodes by [plasma etching](plasma-etching.md) (HBr/Cl₂/O₂ chemistry for high selectivity to thin gate oxide — selectivity >30:1 required to avoid punching through the gate oxide during etch).
6. **Source/drain implant**: Self-aligned implant using polysilicon gate as mask. NMOS: As⁺ or P⁺ at 30-100 keV, dose 10¹⁵-10¹⁶/cm². PMOS: BF₂⁺ at 30-80 keV. Sidewall spacers (SiO₂ or Si₃N₄ deposited by [LPCVD](cvd.md) and etched back by [RIE](plasma-etching.md)) offset the deep source/drain from the gate edge for the extension implant.
7. **Source/drain anneal**: Rapid thermal anneal (RTA) at 1000-1050°C for 10-30 seconds to activate dopants and repair implant damage while minimizing diffusion.
8. **Contact silicide** (optional): Deposit Ti by [sputtering (PVD)](pvd.md), react with silicon at 600-700°C to form TiSi₂ on source/drain/gate surfaces, strip unreacted Ti from oxide. Reduces contact resistance by 10-50×.
9. **Interlayer dielectric (ILD-1)**: Deposit 500-1000 nm SiO₂ by [PECVD](cvd.md) (SiH₄ + N₂O at 350°C). [CMP](cmp.md) planarize to <50 nm topography variation.
10. **Contact holes**: Pattern and etch contact openings to source, drain, and gate. Etch in [RIE](plasma-etching.md) (CHF₃/CF₄ chemistry) with endpoint detection to stop on silicon. Deposit TiN barrier (20-50 nm by [PVD](pvd.md)) → fill with tungsten [CVD](cvd.md) (WF₆ + H₂ at 350°C) → [CMP](cmp.md) etchback to leave W plugs.
11. **Metal 1**: Deposit 0.5-1.0 μm Al-Cu (0.5%) by [sputtering (PVD)](pvd.md). Pattern and etch (Cl₂/BCl₃ [plasma etch](plasma-etching.md) or wet etch for large features).
12. **Interlayer dielectric (ILD-2)**: Deposit SiO₂ by [PECVD](cvd.md). [CMP](cmp.md) planarize.
13. **Via holes**: Pattern, etch, and fill with TiN/W plug (same as step 10).
14. **Metal 2**: Deposit and pattern Al-Cu interconnect layer.
15. **Passivation**: Deposit 1 μm SiNₓ by [PECVD](cvd.md) (SiH₄ + NH₃ + N₂ at 350°C). Pattern bond pad openings.
16. **Alloy/anneal**: 400-450°C, forming gas (N₂/H₂ 90/10), 30 min.
17. **Test, dice, package, wire bond**: See [Packaging & Testing](../chemistry/packaging-testing.md).

### Thermal Budget Management

Total thermal exposure after source/drain implant must be limited to prevent excessive dopant diffusion. Each high-temperature step (>800°C) widens the junctions. A typical thermal budget allows no more than 2-3 hours cumulative exposure above 900°C after implant. This constraint drives the adoption of low-temperature processes ([PECVD](cvd.md) at <400°C, [sputtering](pvd.md) at <300°C, [ion implant](ion-implantation.md) RTA with <30 sec above 1000°C) for all BEOL steps.

**Thermal budget calculation**: At 1000°C, boron diffuses approximately 100 nm in 1 hour in silicon. If the source/drain junction is targeted at 200 nm depth, more than 2 hours at 1000°C would broaden the junction to ~400 nm — potentially shorting the source to the drain in short-channel devices. This is why RTA (seconds at peak temperature) replaced furnace anneals (hours at peak temperature) for advanced processes, and why all BEOL steps are restricted to <450°C.

### Process Step Count and Yield

A single-level metal NMOS process requires ~80-100 individual operations (including cleans, measurements, and inspections). A two-level metal CMOS process expands to 120-150 operations. Each operation has a finite defect rate. If each step introduces an average of 0.5 defects/cm² and the die area is 0.5 cm², then for 100 process steps: Yield = (1 - 0.5 × 0.5)¹⁰⁰ = (0.75)¹⁰⁰ ≈ 3 × 10⁻¹³ — essentially zero. Reducing per-step defect density to 0.01/cm² raises yield to (1 - 0.005)¹⁰⁰ ≈ 60%. This exponential sensitivity to defect density is why cleanrooms, process control, and contamination discipline are non-negotiable for semiconductor manufacturing.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Gate oxide breakdown voltage below 8 MV/cm — leakage current too high | Wet oxidation used instead of dry O₂; furnace temperature non-uniformity exceeds ±1°C; contamination from quartz tube or gas supply | Use dry O₂ oxidation at 900-1000°C for gate oxide (5-100 nm); verify 3-zone furnace uniformity at ±1°C; clean quartz tube; use ultra-high-purity O₂ (99.999%+) with point-of-use particle filtration |
| Wet etch undercut exceeds 20% of feature width — pattern fidelity lost | BHF etch rate 70-100 nm/min too aggressive for thin oxide; over-etching due to timing inaccuracy; no etch stop layer | Switch to dilute HF (1:10 to 1:100) for 20-30 nm/min rate; use timed etch with test wafer calibration; deposit Si₃Nₓ etch stop layer beneath SiO₂ where undercut must be prevented |
| LPCVD poly-Si film non-uniform — ±10% thickness variation across batch | Gas flow distribution uneven in horizontal tube; wafers at tube ends receive different precursor concentration than center | Switch to vertical LPCVD furnace for better uniformity; verify SiH₄ flow at 620°C with uniform gas injection; use deposition rate of ~10 nm/min with ±2-5% target; rotate wafer positions between runs |
| Source/drain implant misaligned to gate edges — threshold voltage spread across wafer | Polysilicon gate not used as self-aligned mask; implant performed before gate definition or without proper tilt | Ensure source/drain implant occurs after poly-Si gate patterning (step 6 in NMOS flow); implant at 50-100 keV through mask defined by poly-Si gate edge; verify no resist lifting during implant |
| Aluminum interconnect electromigration at 400-450°C forming gas anneal | Aluminum sputtered without Cu alloy (Al-Cu 0.5%); current density exceeds electromigration limit in narrow lines; operating temperature too high | Sputter Al-Cu 0.5% alloy target instead of pure Al; widen narrow metal lines to reduce current density; keep forming gas anneal at 400-450°C (not higher); verify anneal time is 30 min in N₂/H₂ 90/10 |
| Tungsten plug voids in contact holes — open circuit at contact resistance measurement | WF₆ + 3H₂ → W + 6HF CVD reaction not nucleating properly; TiN barrier (20-50 nm) too thin or non-conformal causing adhesion failure | Increase TiN barrier thickness toward 50 nm; optimize WF₆/H₂ ratio at 300-400°C and 1-10 Torr for bottom-up fill; verify cold-wall CVD reactor temperature uniformity; check contact hole aspect ratio is within tool capability |
| CMP oxide removal rate drops below 100 nm/min — endpoint detection fails | Slurry silica particles (20-100 nm) agglomerated; polishing pad worn beyond useful life; downforce below 2 psi | Replace slurry batch — check for agglomeration and pH (target 10-11 with KOH); condition polishing pad; verify downforce at 2-5 psi; clean post-CMP with PVA brush and dilute 0.5% HF rinse to <50 particle adders ≥0.16 μm |
| Contact resistance exceeds 50 Ω per tungsten contact | Native oxide on silicon at contact hole bottom not removed before TiN/W deposition; insufficient Al-Si alloying during forming gas anneal | Add dilute HF (1:50) dip immediately before contact metal deposition to strip native oxide; verify forming gas anneal at 400-450°C for 30 min improves Al-Si contact; check contact hole etch cleared oxide completely (BHF over-etch time verification) |
| RCA clean leaves particle contamination >50 per wafer | DI water quality below 18.2 MΩ·cm; SC-1 (NH₄OH/H₂O₂/H₂O) solution depleted; wafer drying method injects particles | Verify DI water resistivity at 18.2 MΩ·cm with 0.05 μm filtration; mix fresh SC-1 solution (NH₄OH:H₂O₂:H₂O at 1:1:5, 75-80°C, 10-15 min); use Marangoni (IPA vapor) drying instead of N₂ blow-dry to reduce particle deposition |
| PECVD SiNₓ film hydrogen content exceeds 30 at% — passivation reliability fails | Deposition temperature too low (<300°C); SiH₄:NH₃ ratio too rich in hydrogen; RF power insufficient for complete precursor dissociation | Increase substrate temperature to 300-400°C; reduce NH₃ flow relative to SiH₄; increase RF power at 13.56 MHz toward 600 W for better film density; for applications requiring <15 at% H, consider LPCVD Si₃N₄ at 750-850°C instead |

## See Also

- [Chemical Vapor Deposition (CVD)](cvd.md) — CVD processes: LPCVD, PECVD, APCVD, tungsten CVD
- [Physical Vapor Deposition (PVD)](pvd.md) — sputtering and evaporation for metallization
- [Ion Implantation](ion-implantation.md) — precision doping equipment and process
- [Plasma Etching (RIE & DRIE)](plasma-etching.md) — dry etch processes and chemistries
- [Chemical-Mechanical Planarization (CMP)](cmp.md) — planarization for multi-level interconnect
- [Dopant & Etch Gases](../chemistry/dopant-etch-gases.md) — process gas chemistry
- [Gas Handling Vacuum](../gas-handling/vacuum.md) — vacuum systems for fab tools
- [Vacuum Pumps](../vacuum/pumps.md) — pump technology for semiconductor tools
- [Resists & Masks](resists-masks.md) — photoresist and mask technology
- [Cleanrooms](cleanrooms.md) — contamination-controlled environments
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — advanced node processing
- [EDA Design](../vlsi-scaling/eda-design.md) — VLSI design to fabrication

---
*Part of the [Bootciv Tech Tree](../index.md) • [Photolithography & IC Fabrication](./index.md) • [All Domains](../index.md)*
