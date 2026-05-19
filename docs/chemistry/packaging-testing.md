# Semiconductor Packaging & Testing

> **Node ID**: chemistry.packaging-testing
> **Domain**: Chemistry
> **Timeline**: Years 40-70
> **Outputs**: packaged_ics, tested_ics, yield_data

### Cleanroom Consumables

**HEPA/ULPA filter media**:
- **HEPA (High Efficiency Particulate Air)**: Remove 99.97% of particles ≥0.3 μm. Construction: fine fiberglass mat (fiber diameter 0.5-2 μm), folded into accordion pleats (increases surface area 20-50x). Separator: corrugated aluminum or hot-melt bead between pleats. Frame: wood, metal, or plastic. Air velocity through filter: 0.025 m/s. Pressure drop: 250 Pa at rated flow.
- **ULPA (Ultra-Low Penetration Air)**: Remove 99.999% of particles ≥0.12 μm. Even finer glass fibers. Higher pressure drop. Used in most critical zones (lithography bays).
- **Filter production**: Glass fiber production (melt borosilicate glass, attenuate into fine fibers by flame attenuation or rotary spinning). Form mat on moving belt with vacuum forming. Bond with acrylic resin binder (5-10% by weight). Cut, pleat, frame, test (challenge with DOP or PAO aerosol particles, measure penetration with photometer).

**Cleanroom garments**:
- Woven polyester or polyester-blend fabric (lint-free, low particle shedding). Coverall design: full body coverage, elastic cuffs, zip front with flap covering zipper. Hood covering head and neck, integrated face mask or separate. Booties over street shoes, low-particulate soles. Boot cover or change into cleanroom-dedicated shoes.
- **Laundering**: Wash in ultra-pure water (18 MΩ·cm) with non-ionic detergent. Dry in HEPA-filtered dryer. Package in cleanroom-compatible bags. Typical garment life: 40-50 washes before particle shedding exceeds spec.

**Wipers**: Polyester knit (cleanest) or non-woven polypropylene. Sealed edges (laser-cut or ultrasonically sealed) to prevent fiber shedding. Used dry or wetted with IPA for surface cleaning. Tested for particle generation, absorbency, and extractable ions.

**Gloves**: Nitrile rubber (synthetic rubber — acrylonitrile + butadiene copolymer, from Polymers). 0.2-0.3 mm thickness for dexterity. Powder-free (powder contaminates cleanroom). Chlorinated inner surface for easy donning. Tested for pinholes (water-fill test), particle count, extractable ions. Change every 2 hours or when contaminated.

### Semiconductor Packaging

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

**Encapsulation**:
- **Transfer molding** (most common for plastic packages): Place die + wire-bonded lead frame in mold cavity. Inject molding compound (epoxy resin + silica filler 70-80% by weight + catalyst + mold release agent) at 175°C, 6-10 MPa pressure. Cure 2-5 minutes. Mold compound protects die from moisture, mechanical damage, contamination. Silica filler reduces thermal expansion coefficient (match silicon → less stress).
- **Ceramic hermetic packages** (high-reliability): Multi-layer ceramic (alumina) with tungsten metallization traces. Co-fired at 1500-1600°C. Seal lid to package with gold-tin eutectic solder (Au-20Sn, mp 280°C) in dry nitrogen atmosphere. Hermetic (gas-tight) — moisture cannot penetrate. For military, aerospace, high-temperature applications.

**Lead forming and finishing**:
- Trim and form lead frame leads (cut free from frame, bend to required shape — DIP, SOP, QFP lead shapes). Apply solder finish (dip in Sn-Pb or Sn-Ag-Cu solder bath at 230-260°C) for solderability. Mark package top with laser (part number, date code, lot code).

### Testing Infrastructure

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

## Safety Concerns

- **Dopant gases (PH₃, AsH₃, B₂H₆)**: Among the most toxic substances used industrially. Lethal at ppm concentrations. Continuous gas monitoring, automated shutdown, emergency evacuation procedures. Always use diluted cylinders. Never store large quantities. Exhaust gas abatement mandatory.
- **Silane**: Pyrophoric. Can auto-detonate without ignition source. Leak detection, inert gas purge protocols, no confined spaces.
- **Fluorine gas**: Reacts with almost everything. Severe chemical burns. Handle only in nickel/Monel equipment. Full PPE including face shield and HF-rated gloves (F₂ penetration produces HF on contact with moisture).
- **Gas cylinder safety**: Secure all cylinders upright (chain or strap to wall). Valve caps on when not in use. Never drag cylinders. Proper labeling (color-coded + text). Separate incompatible gases (flammables from oxidizers). Ventilated cylinder storage.

---

*Part of the [Bootciv Tech Tree](../) • [Chemistry](./) • [All Domains](../)*
