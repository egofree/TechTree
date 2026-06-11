# Semiconductor Packaging & Testing

> **Node ID**: electronics.packaging-testing
> **Domain**: [Electronics](./index.md)
> **Dependencies**: [`machine-tools.machining`](../machine-tools/machining.md), [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`polymers.thermosets`](../polymers/thermosets.md)
> **Enables**: [`electronics.electrical-systems`](./electrical-systems.md)
> **Timeline**: Years 40-70
> **Outputs**: packaged_ics, tested_ics, yield_data
> **Critical**: Yes — semiconductor packaging protects the die from physical damage, moisture, and contamination. Without packaging, fabricated integrated circuits cannot be used in any electronic system.

Semiconductor packaging and testing transforms bare silicon die into reliable, handled integrated circuits ready for assembly onto circuit boards. After wafer fabrication produces functioning die, they must be singulated, attached to a substrate, electrically connected (wire bonding), encapsulated for protection, and tested at multiple stages to ensure functionality and long-term reliability. Packaging determines the IC's physical form factor, thermal performance, and environmental protection; testing verifies that every device meets its electrical, mechanical, and lifetime specifications.

The packaging and testing stage is often the bottleneck for semiconductor production — while a modern fab produces thousands of wafers per month, the test floor must probe every die individually, package the good ones, and burn-in test each packaged part. Test cost can represent 5-10% of total die cost for complex devices, and yield at wafer sort directly determines fab economics.

## Cleanroom Consumables

**HEPA/ULPA filter media**:
- **HEPA (High Efficiency Particulate Air)**: Remove 99.97% of particles ≥0.3 μm. Construction: fine fiberglass mat (fiber diameter 0.5-2 μm), folded into accordion pleats (increases surface area 20-50x). Separator: corrugated aluminum or hot-melt bead between pleats. Frame: wood, metal, or plastic. Air velocity through filter: 0.025 m/s. Pressure drop: 250 Pa at rated flow.
- **ULPA (Ultra-Low Penetration Air)**: Remove 99.999% of particles ≥0.12 μm. Even finer glass fibers. Higher pressure drop. Used in most critical zones (lithography bays).
- **Filter production**: Glass fiber production (melt borosilicate glass, attenuate into fine fibers by flame attenuation or rotary spinning). Form mat on moving belt with vacuum forming. Bond with acrylic resin binder (5-10% by weight). Cut, pleat, frame, test (challenge with DOP or PAO aerosol particles, measure penetration with photometer).

**Cleanroom garments**:
- Woven polyester or polyester-blend fabric (lint-free, low particle shedding). Coverall design: full body coverage, elastic cuffs, zip front with flap covering zipper. Hood covering head and neck, integrated face mask or separate. Booties over street shoes, low-particulate soles. Boot cover or change into cleanroom-dedicated shoes.
- **Laundering**: Wash in ultra-pure water (18 MΩ·cm) with non-ionic detergent. Dry in HEPA-filtered dryer. Package in cleanroom-compatible bags. Typical garment life: 40-50 washes before particle shedding exceeds spec.

**Wipers**: Polyester knit (cleanest) or non-woven polypropylene. Sealed edges (laser-cut or ultrasonically sealed) to prevent fiber shedding. Used dry or wetted with IPA for surface cleaning. Tested for particle generation, absorbency, and extractable ions.

**Gloves**: Nitrile rubber (synthetic rubber — acrylonitrile + butadiene copolymer, from Polymers). 0.2-0.3 mm thickness for dexterity. Powder-free (powder contaminates cleanroom). Chlorinated inner surface for easy donning. Tested for pinholes (water-fill test), particle count, extractable ions. Change every 2 hours or when contaminated.

## Semiconductor Packaging

**Die preparation**:
- **Wafer backgrinding**: Grind back of completed wafer from ~725 μm to 200-350 μm (thinner die fit in thinner packages, better heat dissipation). Diamond-grit grinding wheel, water coolant. Multi-step: coarse grind (30 μm grit, ~600 μm/min removal) → fine grind (5 μm grit, ~100 μm/min) → polish (1 μm grit). Stress relief etch (brief HF dip to remove grinding damage).
- **Wafer mounting**: Adhere wafer to adhesive film (PVC or polyolefin with UV-release adhesive) on metal ring frame. Film holds wafer during dicing.
- **Die singulation (dicing)**: Diamond-impregnated blade (25-50 μm kerf) on high-speed spindle (20,000-40,000 RPM). Cut along scribe streets (pre-defined blank areas between die). Water coolant with surfactant. Feed rate 5-20 mm/second. Produce individual die ~5-20 mm on a side.

**Die attach**:
- **Eutectic bonding**: Au-Si eutectic (97.1% Au, 2.9% Si, mp 363°C). Place die on gold-plated package substrate. Heat to 400-425°C. Gold reacts with silicon die backside → liquid eutectic → bonds on cooling. Very reliable, high thermal conductivity.
- **Epoxy attachment** (more common, lower temperature): Silver-filled epoxy (80% Ag flakes by weight in epoxy resin — provides electrical and thermal conductivity). Dispense epoxy on substrate. Place die (pick-and-place tool — vacuum pickup needle, automated XY positioning). Cure at 150-175°C for 1-2 hours. Epoxy: bisphenol-A + hardener (amine or anhydride), loaded with silver flake 5-20 μm particle size.

**Wire bonding**:
- **Gold ball bonding**: 25 μm (1 mil) diameter gold wire. Form ball on wire tip by electric spark (flame-off). Bond ball to die pad by thermosonic bonding — apply heat (200-250°C), ultrasonic energy (60-120 kHz, 0.5-2 W), and force (0.3-0.8 N) simultaneously. Gold deforms and bonds to aluminum pad. Loop wire to lead frame pad. Bond second end by crescent (wedge) bond. Break wire, repeat. 10-20 bonds/second. Wire length 2-5 mm, loop height 0.2-0.5 mm.
- **Aluminum wedge bonding**: 25-50 μm Al wire. Ultrasonic energy only (room temperature). Wedge tool presses wire against pad. Lower cost but slower. Used for power devices (thicker wire carries more current).
- **Wire drawing for bonding wire**: Draw gold wire through successively smaller diamond dies. Start with 2 mm rod → draw through 20+ dies to 25 μm. Anneal between passes (heat to 500-600°C to restore ductility). Final tensile strength ~200-300 MPa, elongation 2-5%.

**Strengths**: Gold ball bonding is fast (10-20 bonds/second) and reliable — industry standard for 50+ years; thermosonic bonding works at moderate temperature (200-250°C) protecting the die; wire drawing from 2 mm to 25 μm uses standard metalworking techniques; aluminum wedge bonding is cheaper and avoids gold cost.

**Weaknesses**: Gold wire is expensive ($50-80/g); bond pad damage from ultrasonic energy can cause latent failures; wire sweep during molding (flowing epoxy displaces wires) limits loop height and wire length; 25 μm wire is fragile — requires cleanroom handling; bond placement accuracy must be ±5 μm for fine-pitch pads.

**Encapsulation**:
- **Transfer molding** (most common for plastic packages): Place die + wire-bonded lead frame in mold cavity. Inject molding compound (epoxy resin + silica filler 70-80% by weight + catalyst + mold release agent) at 175°C, 6-10 MPa pressure. Cure 2-5 minutes. Mold compound protects die from moisture, mechanical damage, contamination. Silica filler reduces thermal expansion coefficient (match silicon → less stress).
- **Ceramic hermetic packages** (high-reliability): Multi-layer ceramic (alumina) with tungsten metallization traces. Co-fired at 1500-1600°C. Seal lid to package with gold-tin eutectic solder (Au-20Sn, mp 280°C) in dry nitrogen atmosphere. Hermetic (gas-tight) — moisture cannot penetrate. For military, aerospace, high-temperature applications.

**Lead forming and finishing**:
- Trim and form lead frame leads (cut free from frame, bend to required shape — DIP, SOP, QFP lead shapes). Apply solder finish (dip in Sn-Pb or Sn-Ag-Cu solder bath at 230-260°C) for solderability. Mark package top with laser (part number, date code, lot code).

## Testing Infrastructure

**Wafer probing** (test before packaging):
- **Probe card**: Printed circuit board or ceramic substrate with precisely positioned probe needles (tungsten-rhenium or beryllium-copper, tip diameter 12-25 μm). Needles aligned to bond pad pattern. 50-500+ needles per card for complex ICs.
- **Probing station**: Precision XY stage positions wafer under probe card. Camera system for alignment. Z-axis actuator brings probe card into contact — needles scratch through oxide on aluminum pads. Contact resistance <1 Ω.
- **Tests**: DC parametric (Vt, Idsat, Ileakage, breakdown voltage) on test structures (PCMs — process control monitors, placed in scribe streets). Functional test on complete circuits. Speed/bin sort (test at multiple frequencies, bin by maximum operating speed).
- **Yield**: Map pass/fail across wafer → yield map. Typical early fab yields: 10-50%. Mature fab: 80-95%. Track yield by defect type, location, pattern → feedback to process engineering.

**Packaged part testing**:
- **Automated test equipment (ATE)**: Test head with socket for device under test (DUT). Pattern generator applies digital stimuli. Comparator checks outputs. Tests at speed (apply clock, verify timing margins). Temperature testing (hot/cold chuck, -55°C to +125°C for automotive/military grade).
- **Burn-in**: Subject devices to elevated temperature (125-150°C) and voltage (1.2-1.5× rated) for 24-168 hours. Accelerates early-life failures (infant mortality). Devices that survive burn-in have much lower field failure rate.
- **Final test**: Verify all specifications (speed, power, functionality at temperature extremes, I/O levels). Mark passing devices. Package, label, ship.

## Integration Points

| Phase | Contribution |
|-------|-------------|
| Chemistry | Bulk gas production (Cl₂, H₂, O₂, N₂), purification infrastructure |
| Vacuum & Optics | Vacuum technology for gas handling and distillation |
| Silicon | Gas supply for CZ growth (argon), CVD precursors (SiH₄, SiHCl₃) |
| Photolithography | Complete gas/consumable supply chain for fab, packaging, testing |
| Polymers | Epoxy encapsulation, fiberglass filters, nitrile gloves, cleanroom garment materials |

## Key Deliverables

- High-purity argon (99.999%+), nitrogen, hydrogen production via air separation and electrolysis
- Silane production with full pyrophoric safety infrastructure
- Dopant gas supply (PH₃, AsH₃, B₂H₆) with exhaust abatement and monitoring
- Etch gas production (CF₄, SF₆, Cl₂, F₂)
- Gas distribution system (electropolished SS tubing, MFCs, valves)
- HEPA/ULPA filter production
- Cleanroom consumable supply chain (garments, wipers, gloves)
- Die packaging line (dice, attach, wire bond, encapsulate, form leads)
- Wafer probing and parametric test capability
- Burn-in and final test infrastructure

## Cleanroom Consumables — Detailed Specifications

**Wipers**: Ultra-low lint wipers made from polyester (knitted, sealed-edge) for ISO Class 1-4 environments, or nonwoven polyester-cellulose blend for ISO Class 5-7. Critical parameters: particles released (ASTM E2090, <50 particles ≥0.5 µm per cm² for Class 10 wipers), non-volatile residue (NVR <1 mg per m²), ionic extractables (<1 ppm Na⁺, K⁺, Cl⁻). Pre-wetted wipers (with IPA/DI water blend) reduce particle generation during wiping. Cost: $0.50-3.00 per wiper.

**Gloves**: Natural rubber latex causes allergic reactions (protein sensitization) — largely replaced by nitrile (acrylonitrile-butadiene copolymer) in cleanrooms. Nitrile gloves: powder-free, chlorinated inner surface for donning. Thickness: 0.08-0.15 mm (thinner = better dexterity, thicker = better chemical resistance). Critical: ionic extractables, particle shedding, ESD properties (surface resistivity 10⁸-10¹¹ Ω/square for ESD-safe gloves). Change frequency: every 30 minutes to 2 hours depending on protocol. Typical cleanroom uses 20-40 pairs of gloves per operator per shift.

**Chemicals and solvents**: Ultra-pure grades for semiconductor use — "semiconductor grade" or "electronic grade" with specifications tighter than ACS reagent grade. Isopropanol (IPA): <1 ppb each metallic impurity (Fe, Cu, Na, K). Particle specification: <100 particles/mL ≥0.5 µm. Hydrogen peroxide (H₂O₂, 30%): <10 ppb total metallic impurities. Ammonium hydroxide (NH₄OH, 29%): similar metallic specs. These three plus DI water form the "RCA clean" solutions: SC-1 (NH₄OH:H₂O₂:H₂O = 1:1:5) for organic/particle removal; SC-2 (HCl:H₂O₂:H₂O = 1:1:6) for metallic contamination removal.

## Wafer Probing and Test

**Probe cards**: Interface between automated test equipment (ATE) and the wafer — an array of fine needles (tungsten-rhenium or cantilever-style) that make electrical contact to bond pads (50-100 µm aluminum pads) on each die. Modern probe cards use MEMS technology for fine-pitch probing (<50 µm pad pitch). Contact resistance must be <1 Ω per probe. Probe marks on pads must be small enough not to interfere with subsequent wire bonding — typically <25 µm diameter mark. Probe cards are the most expensive consumable in wafer test ($5,000-50,000 each, lifetime 100,000-1,000,000 touchdowns).

**Test flow**: (1) **Wafer sort** (probe test): Test every die on the wafer while still on the full wafer. Marks failed dies with ink dot (or electronic map). Determines yield — critical metric for fab economics. Typical test time: 1-10 seconds per die. Tests: DC parametrics (leakage, threshold voltage, breakdown voltage), basic functional test, sometimes at-speed test for critical paths. (2) **Packaged part test**: After packaging, full functional test at speed, AC timing, thermal testing (hot/cold). (3) **Burn-in**: Stress testing at elevated temperature (125-150°C) and voltage (1.2-1.5× nominal) for 24-168 hours to weed out infant mortality failures. Devices that pass burn-in have much lower field failure rate.

**Automated test equipment (ATE)**: Tester applies test patterns (input stimuli) and measures output responses. Timing accuracy: ±50-100 ps for high-speed digital. Parametric measurement units (PMUs) force voltage/measure current (or force current/measure voltage) with picoamp resolution. Test programs generated from design simulation vectors — "design for test" (DFT) structures like scan chains and built-in self-test (BIST) embedded in the chip during design enable comprehensive testing with reasonable test time.

## Reliability Testing

**Accelerated life testing**: Devices stressed beyond normal operating conditions to predict lifetime. Arrhenius model: failure rate doubles for every 10°C temperature increase. Typical acceleration: operating at 125°C for 1000 hours ≈ equivalent to 10+ years at 55°C use temperature.

**Key reliability tests**: (1) **Temperature cycling**: -65°C to +150°C, 500-1000 cycles. Detects: die attach voids, wire bond degradation, solder joint fatigue, package cracking. (2) **High temperature operating life (HTOL)**: 125°C at nominal voltage, 1000 hours. Detects: gate oxide breakdown, electromigration, hot carrier degradation. (3) **Temperature-humidity-bias (THB)**: 85°C/85%RH with applied bias, 1000 hours (the "85/85" test). Detects: corrosion, ionic contamination, moisture ingress. (4) **Electrostatic discharge (ESD)**: Human body model (HBM, 2000V), charged device model (CDM, 500V). (5) **Pressure cooker (PCT)**: 121°C, 100%RH, 2 atm, 96-168 hours — accelerated version of THB. (6) **Mechanical**: vibration (5-2000 Hz), shock (1500g, 0.5 ms), constant acceleration (30,000g).

**Failure analysis techniques**: (1) **Optical microscopy** and **SEM** for visual inspection. (2) **Acoustic microscopy** (C-SAM) for delamination and void detection — non-destructive. (3) **Decapsulation**: acid (fuming HNO₃ or H₂SO₄) or laser to remove package molding compound and expose die for analysis. (4) **FIB (focused ion beam)**: cross-section specific features for SEM inspection, or cut circuit traces for circuit edit. (5) **EMMI (emission microscopy)**: detects photon emission from defective transistors (hot carrier luminescence, avalanche breakdown). (6) **OBIRCH (optical beam induced resistance change)**: laser scanning detects thermal response changes — localizes shorts and leakage paths.

## Reliability Standards

**JEDEC** standards define test methods and acceptance criteria: JESD22 (test methods), JESD47 (stress-test-driven qualification), JESD74 (early life failure rate). **AEC-Q100** for automotive electronics: more stringent than JEDEC — temperature range -40 to +150°C (Grade 0), zero defects philosophy, additional tests (electromigration, soft error rate). **MIL-STD-883** for military/space: even more stringent — radiation testing (total ionizing dose, single event effects), outgassing testing (ASTM E595, <1% total mass loss, <0.1% collected volatile condensable materials for spacecraft materials).

## Safety Concerns

- **Dopant gases (PH₃, AsH₃, B₂H₆)**: Among the most toxic substances used industrially. Lethal at ppm concentrations. Continuous gas monitoring, automated shutdown, emergency evacuation procedures. Always use diluted cylinders. Never store large quantities. Exhaust gas abatement mandatory.
- **Silane**: Pyrophoric. Can auto-detonate without ignition source. Leak detection, inert gas purge protocols, no confined spaces.
- **Fluorine gas**: Reacts with almost everything. Severe chemical burns. Handle only in nickel/Monel equipment. Full PPE including face shield and HF-rated gloves (F₂ penetration produces HF on contact with moisture).
- **Gas cylinder safety**: Secure all cylinders upright (chain or strap to wall). Valve caps on when not in use. Never drag cylinders. Proper labeling (color-coded + text). Separate incompatible gases (flammables from oxidizers). Ventilated cylinder storage.

## IC Package Types

**Plastic packages**: Over 95% of ICs use plastic (epoxy molding compound) packages. DIP (dual in-line package): 8-40 leads, 2.54 mm lead pitch, through-hole mounting. SOP (small outline package): 8-28 leads, 1.27 mm pitch, surface mount. QFP (quad flat package): 44-240 leads on all four sides, 0.5-0.8 mm pitch. QFN (quad flat no-lead): compact, leads on all four sides but flush with package body, 0.4-0.65 mm pitch. BGA (ball grid array): solder balls on the package bottom, 0.5-1.27 mm pitch, 100-2000+ connections. Higher pin count devices require finer pitch and area array configurations.

**Hermetic packages**: Ceramic or metal packages that are sealed against gas and moisture ingress. Used for high-reliability applications: military (MIL-STD-883), aerospace, medical implants, and high-temperature environments. CERDIP (ceramic dual in-line): ceramic body with glass-sealed ceramic lid. CQFP (ceramic quad flat pack): ceramic body with Kovar leads brazed to the side walls. Metal can packages (TO-5, TO-8): metal body with glass-sealed leads, welded or soldered lid. Hermeticity verified by fine leak test (helium mass spectrometry, leak rate <1×10⁻⁸ atm·cc/sec) and gross leak test (fluorocarbon bubble test).

**Die attach materials**: For plastic packages, silver-filled epoxy (80% Ag by weight, cured at 175°C for 1 hour) provides thermal conductivity 1.5-5.0 W/m·K and electrical conductivity to the lead frame. For high-power devices, eutectic Au-Si attach (mp 363°C) provides superior thermal conductivity (50+ W/m·K through the gold layer). For ceramic hermetic packages, gold-gold thermocompression bonding or silver-glass paste (fired at 350-400°C) provides reliable die attach with excellent thermal performance.

## Semiconductor Test Economics

**Test cost per die**: Wafer sort (probe test): $0.01-0.10 per die depending on complexity. Package test: $0.05-0.50 per die. Burn-in: $0.10-1.00 per die (depends on duration, 24-168 hours). For a complex SoC (system-on-chip), total test cost can be 5-10% of the die cost. Test cost increases with pin count, test speed, and test time. Design-for-test (DFT) structures embedded in the chip reduce test cost by enabling fast structural testing (scan chains test all flip-flops in a serial shift pattern) rather than slow functional testing.

**Yield learning curve**: New semiconductor products start at 10-30% yield and improve to 80-95% over 12-24 months through systematic defect reduction. Each 1% yield improvement on a 300 mm wafer producing 500 die at $50/die represents $250,000 annual revenue increase. This economic incentive drives aggressive yield improvement programs: failure analysis of every failed die, root cause identification, and process or design modification. The Pareto principle applies: 80% of yield loss comes from 20% of defect types, allowing focused improvement efforts.

## Semiconductor Grade Chemical Specifications

**Ultra-pure water (UPW)**: Used for all wafer rinsing steps. Resistivity: 18.2 MΩ·cm at 25°C (theoretical maximum for pure water). TOC (total organic carbon): <1 ppb. Particles: <1000 particles/L ≥0.05 μm. Dissolved oxygen: <10 ppb (oxygen in rinse water causes native oxide growth on silicon). Bacteria: <1 CFU/100 mL. Metals: <0.1 ppb each for Fe, Cu, Ni, Zn. UPW production: municipal water → multimedia filter → softener → activated carbon → RO (reverse osmosis) → EDI (electrodeionization) → UV sterilization → mixed bed ion exchange → 0.05 μm ultrafiltration → distribution loop (continuous recirculation at 1-3 m/s to prevent bacterial growth).

## Limitations

- **Test coverage gap**: No test can prove a device is defect-free — tests can only detect specific failure modes. Design-for-test (DFT) structures improve coverage but cannot exercise every transistor in a complex SoC. Typical stuck-at fault coverage: 95-99%. Untested defects escape to the field.
- **Burn-in trade-off**: Longer burn-in catches more infant mortality failures but reduces yield and increases cost. The optimal burn-in duration balances field failure cost against test cost — for consumer electronics, shorter burn-in (24-48 hours) is economically justified; for automotive or medical, longer burn-in (168+ hours) despite lower throughput.
- **Package parasitics**: Wire bonds add 0.5-2.5 nH inductance and 0.02-0.05 pF capacitance per bond — limiting high-speed signal integrity. Flip-chip bonding (solder bumps directly on die, no wires) reduces parasitics by 10× but requires underfill and more complex substrate design.
- **Thermal management limits**: Plastic encapsulation (epoxy molding compound) has thermal conductivity of only 0.6-1.0 W/m·K — poor compared to metals. High-power devices (>5 W) require thermal vias, copper heat spreaders, or exposed die pads to conduct heat out of the package. Thermal resistance (θJA) is often the binding constraint on maximum power dissipation.
- **Moisture sensitivity**: Plastic packages absorb moisture (MSL — moisture sensitivity level). During solder reflow, absorbed moisture rapidly expands, causing "popcorn cracking" of the package. MSL-rated parts must be baked dry and used within a specified floor life after opening the moisture-barrier bag.
- **Probe card wear**: Tungsten-rhenium probe needles degrade after 100,000-500,000 touchdowns, increasing contact resistance and causing false test failures. Probe card replacement is a significant recurring cost ($5,000-50,000 per card).

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Wire bond lifting (non-stick on pad) | Pad contamination or incorrect bond parameters | Clean pad with plasma descum; verify ultrasonic power and force; check capillary wear |
| Die attach voids (X-ray shows gaps) | Insufficient epoxy or trapped air during dispensing | Optimize epoxy dispense pattern; add vacuum step during cure; verify epoxy viscosity |
| Package cracking after solder reflow | Moisture absorption (popcorn cracking) | Bake parts per MSL rating before reflow; track floor life after bag opening; use dry pack |
| High contact resistance at probe | Probe tip contamination or insufficient overtravel | Clean probe tips; increase overtravel (10-25 μm typical); replace worn probes |
| Burn-in failures exceeding 2% | Infant mortality from fab defect density | Review wafer sort yield; tighten wafer sort limits; investigate failure modes with FA |
| Delamination between die and molding compound | Poor adhesion from contaminated die surface | Apply silane adhesion promoter; verify die attach cure; check for moisture before molding |

## See Also

- [Dopant and Etch Gases](../chemistry/dopant-etch-gases.md) — gas supply for etching and doping during wafer fabrication
- [Hydrogen and Silane](../chemistry/hydrogen-silane.md) — feedstock gases for CVD silicon deposition
- [Vacuum Systems](../gas-handling/vacuum.md) — vacuum technology for deposition and etch processes
- [Solvents](../chemistry/solvents.md) — ultra-pure solvents for wafer cleaning (RCA clean)
- [Thermoplastics](../polymers/thermoplastics.md) — polymer materials for packaging and cleanroom consumables
- [Thermosets](../polymers/thermosets.md) — epoxy molding compounds for IC encapsulation
- [Fab Processes](../photolithography/fab-processes.md) — the wafer fabrication processes that precede packaging
- [Analytical Verification](../ultra-pure/analytical-verification.md) — contamination analysis methods
- [Electronics Assembly](assembly.md) — PCB assembly and system-level integration of packaged ICs

---

*Part of the [Bootciv Tech Tree](../../index.md) • [Electronics](./index.md) • [All Domains](../../index.md)*
