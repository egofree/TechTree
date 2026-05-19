# Thermosetting Polymers

> **Node ID**: polymers.thermosets

Process-level reference for thermosetting polymers in the tech tree. Thermosets cross-link irreversibly during cure; they cannot be remelted or reformed. This makes them dimensionally stable, heat-resistant, and chemically durable. Feedstocks come from [Petrochemicals](../chemistry/petroleum-alternatives.md).

## Materials and Processes

### Phenol-Formaldehyde (Bakelite)

First synthetic plastic (commercialized 1909). Phenol + formaldehyde condensation polymerization, two distinct routes:

**Novolac route** — acid catalyst (HCl or oxalic acid), excess phenol. Produces a thermoplastic prepolymer that remains uncured until mixed with hexamethylenetetramine (hexamine) hardener and heated. Two-step process: synthesize resin, then blend with filler and cure.

**Resole route** — base catalyst (NaOH or ammonia), excess formaldehyde. Self-curing prepolymer; continued heating drives cross-linking without added hardener.

- Process conditions: 80–150°C initial condensation reaction; 150–200°C compression molding with fillers (wood flour, mineral fillers, cotton flock)
- Pressure: 15–30 MPa in compression press
- Properties: hard, rigid, excellent electrical insulator, heat-resistant to ~200°C, chemically inert to most solvents
- Applications: electrical insulators, switchgear components, distributor caps, molded fittings, early plastic goods
- Note: novolac resins are also the basis for positive-tone photoresist binders in [Photolithography](../photolithography/resists-masks.md)

### Epoxy Resins

Bisphenol-A + epichlorohydrin yields diglycidyl ether of bisphenol-A (DGEBA), the workhorse epoxy prepolymer. Cured with hardeners in a two-part formulation:

- **Amine hardeners** (DETA, TETA): room temperature to 80°C cure, fast pot life
- **Anhydride hardeners**: 100–150°C cure, better electrical properties, longer pot life

Process conditions vary by application:

- Structural adhesive: mix resin/hardener, apply at room temp, post-cure 60–80°C
- Composite matrix: vacuum bag layup, cure 80–120°C under vacuum
- Potting and encapsulation: pour or transfer mold, cure 80–150°C

Properties: high adhesive strength, excellent chemical resistance, low shrinkage on cure (<2%), good electrical insulation.

Applications: die attach adhesive ([Semiconductor Packaging](../chemistry/packaging-testing.md)), IC encapsulation, composite matrix resin, structural adhesive, PCB substrate bonding, protective coatings.

### Phenolic Laminates (FR-4 / G-10)

Phenolic or epoxy resin impregnated into paper (phenolic grades) or woven glass fabric (epoxy grades), then layered and hot-pressed.

- **G-10**: epoxy-glass laminate, non-flame-retardant grade
- **FR-4**: brominated epoxy-glass laminate with flame retardancy (UL 94 V-0)

Process: stack resin-impregnated fabric sheets (prepreg), press at 150–170°C under 3–7 MPa for 60–90 minutes. Cool under pressure to prevent warpage.

Properties: excellent electrical insulation, dimensional stability, moisture resistance, flame resistance (FR-4), mechanical strength.

Applications: **PCB substrates** (critical dependency for [Photolithography](../photolithography/resists-masks.md) semiconductor path), electrical panels, terminal boards, brake linings, bearing retainers, structural insulating panels.

### Unsaturated Polyester Resin

Propylene glycol + maleic anhydride (unsaturated dibasic acid) + phthalic anhydride (saturated modifier) condensed into a low-molecular-weight polyester prepolymer. Dissolved in styrene monomer (~30–40% by weight) as reactive diluent.

Cure mechanism: free-radical polymerization initiated by MEKP (methyl ethyl ketone peroxide) catalyst, typically with cobalt naphthenate accelerator. Room-temperature cure is standard.

- Process: apply gel coat to mold surface, then hand layup of glass fiber mat + resin, roll out air, cure at ambient temperature (20–30°C, 30–60 min gel, 24 hr full cure)
- Elevated temperature post-cure (60–80°C) improves mechanical properties
- Properties: good strength-to-weight ratio, corrosion resistant, easily molded into complex shapes
- Applications: fiberglass composite matrix (most common resin for hand layup), boat hulls, tanks, panels, corrosion-resistant equipment, structural enclosures

### Polyurethane / Polyurea

Isocyanate chemistry is the foundation. Diisocyanates (TDI: toluene diisocyanate, or MDI: methylene diphenyl diisocyanate) react with:

- **Polyols** → polyurethane (foams, elastomers)
- **Polyamines** → polyurea (fast-cure spray coatings)

Material forms:

- **Flexible foam**: low-density molded cushions, padding, acoustic insulation (TDI + polyether polyol, water as blowing agent, 25–40°C mold)
- **Rigid foam**: structural insulation panels, refrigeration (MDI + polyester polyol, fluorocarbon or hydrocarbon blowing agent, 30–50°C mold)
- **Elastomers**: wheels, belts, bushings, wear pads (cast or injection molded)
- **Spray coatings**: polyurea for fast-cure protective linings (reaction time <10 seconds)

**Complexity warning**: isocyanate production is non-trivial. The industrial route reacts primary amines with phosgene (COCl₂), which itself requires chlorine + carbon monoxide. Non-phosgene routes exist (thermal cleavage of urethane, or carbonylation of nitroaromatics) but are less mature. Isocyanates are also toxic and require careful handling, ventilation, and PPE.

## Key Milestones

Ordered by approximate phase availability:

- ☐ **Chemistry stage**: Bakelite compression molding operational (electrical insulators, molded fittings)
- ☐ **Chemistry stage**: Phenolic resin synthesis (novolac and resole routes)
- ☐ **Chemistry stage**: Urea-formaldehyde molding compounds for housings and fixtures
- ☐ **Chemistry-Vacuum Optics stage**: Unsaturated polyester + fiberglass hand layup (panels, tanks, enclosures)
- ☐ **Vacuum & Optics stage**: Epoxy resin formulation for structural adhesives and composite matrix
- ☐ **Vacuum & Optics stage**: G-10 epoxy-glass laminate production (electrical insulation panels)
- ☐ **Vacuum & Optics stage**: Polyurethane flexible and rigid foam production
- ☐ **Silicon stage**: FR-4 brominated epoxy-glass laminate for PCB substrates
- ☐ **Silicon stage**: Polyurea spray coating capability
- ☐ **Photolithography stage**: Novolac-based photoresist resin for photolithography (same chemistry as Bakelite novolac route)
- ☐ **Photolithography stage**: Epoxy die attach and IC encapsulation materials qualified for fab use

### Safety & Hazards

- **Formaldehyde (IARC Group 1 carcinogen)**: A confirmed human carcinogen used in both phenol-formaldehyde (Bakelite) and urea-formaldehyde resin production. Inhalation of formaldehyde vapor causes nasal and respiratory tract irritation; chronic exposure increases cancer risk. Use in well-ventilated areas with local exhaust. Wear chemical splash goggles and a respirator with formaldehyde cartridge when handling formaldehyde solutions or during resin synthesis. Monitor airborne concentrations — OSHA PEL is 0.75 ppm (8-hour TWA).
- **Phenol (chemical burns, skin absorption)**: Causes severe chemical burns on contact — initially painless because it simultaneously anesthetizes tissue, leading to deeper injury before the victim notices. Absorbed rapidly through intact skin; systemic toxicity targets the liver and kidneys. Wear nitrile or neoprylene gloves (not latex — phenol penetrates latex), chemical splash goggles, and a face shield during phenol handling. In case of skin contact, flush with large amounts of water immediately and seek medical attention — do not rely on pain as an indicator of exposure severity.
- **Epoxy sensitization**: Repeated skin contact with uncured epoxy resin or amine hardeners causes allergic contact dermatitis that becomes permanent once sensitized — even trace future exposure triggers severe rash. Once sensitized, a worker may be unable to continue any epoxy-related work. Wear nitrile gloves, change gloves if contaminated, and minimize all skin contact. Use barrier creams as a supplement, never a substitute for gloves.
- **Ammonia (respiratory irritant)**: Used as a base catalyst in the resole route for phenol-formaldehyde. Ammonia gas is a powerful respiratory and eye irritant — 300 ppm is immediately dangerous to life. Handle concentrated ammonia solutions in ventilated areas. Wear eye protection and a respirator if ventilation is insufficient.

---

*Part of the [Bootciv Tech Tree](../) • [Polymers](./) • [All Domains](../)*
