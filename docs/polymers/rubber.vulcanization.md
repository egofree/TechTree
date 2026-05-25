# Vulcanization & Hardness Scales

> **Node ID**: polymers.rubber.vulcanization
> **Domain**: Polymers & Composites
> **Dependencies**: None (root capability)
> **Enables**: None (leaf capability)
> **Timeline**: Years 5-50
> **Outputs**: vulcanized_elastomers, cured_seals, molded_rubber_parts

Vulcanization is the irreversible chemical process that converts raw rubber (thermoplastic, sticky, temperature-sensitive) into a durable elastomer with stable mechanical properties across a useful temperature range. The process was discovered by Charles Goodyear in 1839 when he accidentally heated a rubber-sulfur mixture on a stove. This single discovery enabled every application of rubber that matters: tires, seals, gaskets, hoses, belts, and vibration isolators. See [Rubber Production](./rubber.md) for an overview and [Natural Rubber](./natural.md) for raw rubber processing.

### Vulcanization Chemistry

**Sulfur cross-linking mechanism**: Sulfur atoms form covalent bridges (polysulfide chains —Sₓ—, where x = 1–8) between adjacent polymer chains at allylic carbon positions. These bridges create a three-dimensional molecular network that prevents permanent chain slippage under deformation. The cross-linked rubber recovers its original shape after stretching because the network stores elastic energy.

**Cross-link types and properties**:

| Cross-link Type | Sulfur Chain Length | Thermal Stability | Mechanical Strength | Fatigue Resistance |
|---|---|---|---|---|
| Polysulfide (—Sₓ—, x ≥ 3) | Long | Low (breaks >130°C) | High tear strength | Excellent |
| Disulfide (—S₂—) | Medium | Medium | Good | Good |
| Monosulfide (—S—) | Short | High (stable to 160°C) | Lower tear strength | Moderate |
| Carbon-carbon (peroxide) | None | Very high (stable >200°C) | Moderate | Lower |

### Cure Systems

Three main cure system families control the type and density of cross-links:

**Conventional Vulcanization (CV)**:
- Sulfur: 2.0–3.5 phr
- Accelerator: 0.5–1.5 phr (e.g., CBS, TBBS)
- Zinc oxide: 5 phr, stearic acid: 2 phr
- Cross-links: predominantly polysulfide (x = 4–8)
- Properties: excellent fatigue resistance, high tear strength, lower thermal stability
- Applications: tire carcass and sidewalls, vibration isolators, conveyor belts
- Cure conditions: 140–160°C, 10–30 minutes

**Efficient Vulcanization (EV)**:
- Sulfur: 0.4–0.8 phr
- Accelerator: 3.0–5.0 phr (high accelerator-to-sulfur ratio)
- Cross-links: predominantly mono- and disulfide
- Properties: superior thermal stability, lower reversion, lower fatigue resistance
- Applications: engine mounts, seals for elevated temperature service, radiator hoses
- Cure conditions: 150–170°C, 8–20 minutes

**Semi-Efficient Vulcanization (SEV)**:
- Sulfur: 1.0–1.8 phr
- Accelerator: 1.5–3.0 phr
- Cross-links: mix of poly-, di-, and monosulfide
- Properties: balance of CV and EV characteristics
- Applications: general-purpose molded goods, O-rings, gaskets
- Cure conditions: 140–160°C, 10–25 minutes

### Cure Parameters by Rubber Type

| Rubber Type | Cure Agent | Temperature (°C) | Time (min) | Pressure (MPa) | Notes |
|---|---|---|---|---|---|
| Natural Rubber (NR) | Sulfur 2–3 phr | 140–160 | 15–60 | 5–20 | CV system; reversion above optimum |
| SBR | Sulfur 1.5–2.5 phr | 150–170 | 10–30 | 5–20 | Less reversion than NR |
| NBR | Sulfur 1.5–2.0 phr | 150–170 | 10–25 | 5–20 | Metal oxide co-cure possible |
| Neoprene (CR) | ZnO 5 + MgO 4 phr | 150–180 | 5–20 | 5–20 | Metal oxide cure, no sulfur needed |
| EPDM | Sulfur 1–2 phr or peroxide | 160–180 | 8–20 | 5–20 | Peroxide for better heat aging |
| Silicone (VMQ) | Peroxide 0.5–2% | 150–175 | 5–15 | 5–15 | Pt-catalyst for LSR at 100–150°C |
| FKM (Viton) | Bisphenol or peroxide | 170–200 | 5–15 | 7–20 | Post-cure 200–250°C, 4–24 hrs |
| Butyl (IIR) | Sulfur 1.5–2.5 phr | 150–170 | 15–30 | 5–20 | Halobutyl cures faster |

### Vulcanization Equipment

**Compression molding press**:
- Hydraulic press, 10–200 tons clamp force. Platens heated by steam, oil, or electric cartridges.
- Temperature control ±2°C across the platen surface. Steam-heated platens use 3–10 bar steam.
- Operation: load uncured rubber preform into mold cavity, close press, maintain temperature and pressure for the specified cure time, open press, demold part.
- Cycle time: 5–60 minutes depending on part thickness (cure time scales approximately with the square of the thickest section — a 6 mm thick part needs ~4× the cure time of a 3 mm part because heat must penetrate to the center).
- Typical mold: tool steel (P20 or H13), chrome-plated for release. Mold temperature: 150–180°C. Flash groove design controls excess material.

**Transfer molding**:
- Rubber preform placed in a pot above the mold cavity. A plunger forces rubber through a runner system into the closed mold.
- Better dimensional accuracy than compression molding, especially for complex shapes with inserts.
- Runner volume wastes 5–15% of material (scrap).
- Used for: rubber-to-metal bonded parts, complex seals, electrical connectors with embedded contacts.

**Injection molding**:
- Rubber strip fed continuously into a screw injection unit. The screw plasticates (warms and softens) the rubber, then injects it into a closed mold at 50–200 MPa injection pressure.
- Fastest cycle time: 2–10 minutes total (fill time 5–30 seconds + cure time).
- Best dimensional consistency. Lowest flash.
- Requires precise barrel temperature control (60–90°C — warm enough to flow but not so hot as to begin curing before injection, called "scorch safety").
- Used for: high-volume O-rings, shoe soles, automotive bushings, precision seals.

**Autoclave (steam pan) curing**:
- Rubber articles (hoses, belts, extruded profiles) placed in a steam autoclave at 3–10 bar steam pressure (corresponding to 134–180°C).
- Batch process: load, close door, pressurize with steam, cure for specified time, depressurize, unload.
- Cure time depends on steam pressure and article thickness: 30–120 minutes typical.
- Used for: hoses (wrapped on mandrels), conveyor belts (built on flat tables, cured in long autoclaves), extruded weatherstripping.

### Cure Monitoring and Control

**Oscillating Disc Rheometer (ODR) / Moving Die Rheometer (MDR)**:
- The standard instrument for measuring vulcanization behavior. A small rubber sample (5–10 g) is heated to the test temperature (typically 150°C or 160°C) in a sealed die. A disc or die oscillates at small amplitude (±0.5° or ±1°), and the torque required for oscillation is measured continuously.
- **Torque curve interpretation**:
  - Minimum torque (M_L): measures compound viscosity before cure begins — related to processability.
  - Scorch time (t_s2): time for torque to rise 2 dNm above M_L — the "safe processing window" before the compound begins curing. Longer scorch time = more processing safety.
  - Cure time (t_90): time for torque to reach 90% of the total rise (M_H − M_L) — the practical cure time for production.
  - Maximum torque (M_H): related to cross-link density and final modulus.
  - Reversion: if torque decreases after M_H (common with NR at high temperature), the compound is overcuring — cross-links are breaking.

**Practical cure time selection**: Production cure time = t_90 + safety margin (typically +10–20%). For thick parts, add extra time for heat penetration to the center (rule of thumb: add 1 minute per mm of thickness above 3 mm).

### Post-Cure Processing

After demolding, vulcanized rubber parts require:
- **Deflashing**: Remove flash (excess material at mold parting lines) by:
  - Manual trimming (tumbling knives, scissors — labor-intensive)
  - Cryogenic deflashing (liquid nitrogen at −80°C to −120°C embrittles the flash, then tumbled with media — the frozen flash cracks off cleanly from the still-flexible part body)
  - Buffing (abrasive wheel grinding — for precision surfaces)
- **Post-cure oven** (for FKM, silicone, and some peroxide-cured compounds): Heat to 200–250°C for 4–24 hours in a circulating air oven. Drives off volatile byproducts and completes residual cross-linking. Essential for FKM — without post-cure, compression set is unacceptably high (>50% vs. <25% after proper post-cure).

### Hardness Scales

Rubber hardness is measured by the depth of indentation of a standardized indenter under a specified force. Two scales are used for elastomeric materials:

**Shore A (soft to medium elastomers)**:
- Range: 0–100 (practical rubber range: 20–95)
- Indenter: Truncated cone (35° apex, flat tip 0.79 mm diameter)
- Spring force: 0.55–8.05 N
- Typical values:
  - Shore A 20–30: very soft (gel insoles, soft foam grips, erasers)
  - Shore A 40–50: soft rubber (sponge rubber, soft door seals, rubber bands ~A35–A45)
  - Shore A 50–60: medium-soft (automotive weatherstripping, shoe soles ~A50–A65)
  - Shore A 60–70: medium (general-purpose seals, O-rings, tire tread ~A60–A70)
  - Shore A 70–80: medium-hard (industrial O-rings, conveyor belt covers, drive belt teeth)
  - Shore A 80–90: hard rubber (hard bushings, printing rolls, shoe heels)
  - Shore A 90–95: very hard (ebonite range, hard wheel materials)

**Shore D (hard rubber and rigid plastics)**:
- Range: 0–100 (practical rubber range: 30–85)
- Indenter: Sharp cone (30° apex, sharp tip)
- Spring force: 0–44.5 N
- Typical values:
  - Shore D 30–40: hard rubber (ebonite at moderate sulfur loading)
  - Shore D 50–60: very hard rubber (highly filled ebonite, hard cast polyurethane)
  - Shore D 60–75: rigid materials (nylon, HDPE, cast PU rollers)
  - Shore D 75–85: very rigid (polycarbonate, cast PU industrial wheels)

**Approximate overlap between scales**:
- Shore A 95 ≈ Shore D 35
- Shore A 98 ≈ Shore D 45
- Shore A 100 ≈ Shore D 55

**Hardness selection guide for O-rings and seals**:

| Application | Shore A | Reasoning |
|---|---|---|
| Low-pressure static seals | 40–50 | Conforms to irregular surfaces |
| General-purpose O-rings | 70 | Standard (AS568 O-rings default to A70) |
| High-pressure dynamic seals | 80–90 | Resists extrusion into clearance gaps |
| Rotary shaft seals | 70–80 | Balance of sealing force and wear resistance |
| Vibration isolators | 40–60 | Low stiffness for maximum isolation |
| Backup rings | 85–95 | High modulus prevents extrusion |

### Compounding Ingredients Detail

**Reinforcing fillers**:

| Filler | Loading (phr) | Effect on Tensile (MPa) | Effect on Hardness (Shore A) | Primary Use |
|---|---|---|---|---|
| None (gum stock) | 0 | 17–28 (NR) / 1–3 (SBR) | 30–40 | Reference |
| Carbon black N110 | 40–50 | 25–32 | +20–30 | Tire treads (max abrasion resistance) |
| Carbon black N330 | 30–50 | 20–28 | +15–25 | General purpose (tires, belts) |
| Carbon black N660 | 30–50 | 18–25 | +12–20 | Carcass, sidewalls |
| Precipitated silica | 10–30 | 18–24 | +10–15 | Green tires (low rolling resistance) |
| Calcium carbonate | 50–100 | 10–15 | +8–12 | Low-cost extension (non-critical) |
| Clay | 30–80 | 10–18 | +5–10 | Low-cost extension |

**Accelerator systems**:

| Accelerator | Abbreviation | Phr | Cure Rate | Scorch Safety | Cross-links |
|---|---|---|---|---|---|
| Mercaptobenzothiazole | MBT | 0.5–2.0 | Medium | Low | Polysulfide |
| Mercaptobenzothiazole disulfide | MBTS | 0.5–2.0 | Medium-slow | Medium | Polysulfide |
| N-Cyclohexyl-2-benzothiazole sulfenamide | CBS | 0.5–1.5 | Delayed action | High | Polysulfide |
| N-tert-Butyl-2-benzothiazole sulfenamide | TBBS | 0.5–1.5 | Delayed action | High | Polysulfide |
| Tetramethylthiuram disulfide | TMTD | 0.2–0.5 | Ultra-fast | Low | Short (EV-like) |
| Diphenylguanidine | DPG | 0.3–1.0 | Slow (secondary) | High | Polysulfide |

**Antioxidants and antiozonants**:
- TMQ (polymerized 2,2,4-trimethyl-1,2-dihydroquinoline): 1–2 phr. General-purpose antioxidant, prevents oxidative chain scission during service. Inexpensive, widely used in tire compounds.
- 6PPD (N-(1,3-dimethylbutyl)-N'-phenyl-p-phenylenediamine): 1–3 phr. Combined antioxidant and antiozonant. Protects tire sidewalls from ozone cracking — the primary failure mode for outdoor-exposed rubber. Migrates to the rubber surface to react with ozone before it can attack the polymer backbone.
- Wax (paraffin or microcrystalline, 1–2 phr): Blooms to the rubber surface forming a physical barrier against ozone. Effective for static seals but not dynamic applications (flexing breaks the wax film).

### Reversion and Overcure

Natural rubber undergoes "reversion" when overcured — the polysulfide cross-links thermally break, and the main chain undergoes chain scission. This reduces cross-link density, softens the rubber, and degrades mechanical properties. Indicators:
- Decreasing torque on rheometer after peak (the classic "reversion curve")
- Soft, sticky surface on demolded parts
- Reduced tensile strength and increased permanent set
- Darkening of compound color

**Prevention**: Use EV systems (lower sulfur, higher accelerator) for applications requiring extended cure at high temperature. EV systems produce thermally stable mono- and disulfide cross-links that resist reversion. The tradeoff: EV-cured rubber has lower tear strength and fatigue resistance than CV-cured rubber.

Synthetic rubbers (SBR, BR, NBR) are less prone to reversion than NR — their cross-links are more thermally stable. This is one reason SBR is blended with NR in tire compounds: the SBR component provides reversion resistance during high-temperature curing.

### Non-Sulfur Cure Systems

**Peroxide cure** (for silicone, EPDM, and some specialty compounds):
- Dicumyl peroxide (DCP): 1–3 phr. Decomposes at 150–175°C to generate free radicals that create carbon-carbon cross-links between polymer chains.
- Carbon-carbon bonds are more thermally stable than sulfur cross-links (stable above 200°C vs. polysulfide breakdown at 130–150°C).
- No sulfur odor. No nitrosamine concerns.
- Limitation: peroxide-cured compounds cannot be cured in contact with oxygen (air inhibits surface cure — use a mold or nitrogen atmosphere). Peroxide is incompatible with many antioxidants (they scavenge the free radicals needed for cross-linking).

**Metal oxide cure** (for neoprene):
- Zinc oxide (5 phr) + magnesium oxide (4 phr). MgO scavenges HCl released during aging.
- No sulfur needed. Good aging properties.

**Bisphenol cure** (for FKM):
- Bisphenol AF + phosphonium salt accelerator. Requires high-temperature post-cure (200–250°C, 4–24 hours).
- Produces cross-links with excellent chemical and thermal resistance.

### Safety & Hazards

- **Vulcanization burns**: Press platens at 140–180°C and autoclave steam at 3–10 bar cause severe thermal burns and scalds. Steam burns are especially severe due to latent heat of condensation (2260 kJ/kg at 1 atm). Use thermal gloves, face shields, and long sleeves.
- **Nitrosamine formation**: Certain accelerators (TMTD, DTDM, MOR) form N-nitrosamines during vulcanization — confirmed carcinogens. Use nitrosamine-safe alternatives (TBzTD, ZBEC) where possible.
- **Dust explosion risk**: Sulfur powder (MEC ~35 g/m³), carbon black (MEC 50–100 g/m³), and rubber crumb form explosive dust-air mixtures. Ground equipment, use local exhaust ventilation, eliminate ignition sources.
- **Volatile organic compounds (VOCs)**: Vulcanization releases a complex mixture of volatile organic compounds including H₂S, SO₂, mercaptans, and various hydrocarbon fragments. Adequate ventilation is mandatory — typical exhaust rates of 15–20 air changes per hour for curing areas.

---

### Cross-Domain Dependencies

- Sulfur from [Chemistry](../chemistry/acids.md). Carbon black from [Charcoal](../energy/charcoal.md). Zinc oxide from [Metals](../metals/non-ferrous.md). Equipment from [Machine Tools](../machine-tools/joining.md). See [Natural Rubber](./natural.md) for raw material sources and [Synthetic Polymers](./synthetic.md) for synthetic rubber cure systems.

## See Also

- **[Rubber Production](./rubber.md)**: Overview of rubber and elastomers
- **[Natural Rubber](./natural.md)**: Raw rubber extraction and basic vulcanization
- **[Synthetic Polymers](./synthetic.md)**: Synthetic rubber types and their cure systems
- **[Semiconductor Applications](./rubber.semiconductor-apps.md)**: Elastomers in semiconductor equipment

[← Back to Polymers](index.md)
