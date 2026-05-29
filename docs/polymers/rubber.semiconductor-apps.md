# Elastomers in Semiconductor Equipment

> **Node ID**: polymers.rubber.semiconductor-apps
> **Domain**: Polymers & Composites
> **Dependencies**: [`polymers.rubber`](rubber.md), [`polymers.synthetic`](synthetic.md), [`polymers.rubber.vulcanization`](rubber.vulcanization.md), [`chemistry.acids`](../chemistry/acids.md)
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`gas-handling.vacuum`](../gas-handling/vacuum.md)
> **Timeline**: Years 40-200+
> **Outputs**: semiconductor_seals, chemical_resistant_linings, cleanroom_elastomers
> **Critical**: No — essential for semiconductor manufacturing but not required for basic civilization infrastructure


Semiconductor fabrication equipment demands elastomeric seals, gaskets, O-rings, and liners that withstand aggressive chemicals (HF, H₂SO₄, HNO₃, H₃PO₄, organic solvents), elevated temperatures, vacuum integrity, and ultra-clean conditions where a single particle or trace contaminant can destroy a wafer. Material selection is critical — the wrong elastomer in a wet bench can leach metal ions into the process stream, killing device yield. Standard rubber (NR, NBR) degrades rapidly in oxidizing acids and most semiconductor process chemicals; only fluorinated elastomers (FKM, FFKM) and certain specialty grades (EPDM for UPW) survive.

## Prerequisites

- [Rubber production](rubber.md) — basic elastomer processing and molding
- [Synthetic polymers](synthetic.md) — FKM, EPDM, silicone, and fluoropolymer synthesis
- [Vulcanization](rubber.vulcanization.md) — cross-linking for heat and chemical resistance
- [Acid production](../chemistry/acids.md) — HF, H₂SO₄, HNO₃ for wet process chemistry
- [Vacuum technology](../gas-handling/vacuum.md) — vacuum seal requirements and outgassing
- [Fluorine chemistry](../chemistry/index.md) — required for FKM and FFKM synthesis

## Chemical Resistance Properties Table

Comparison of elastomer resistance to chemicals encountered in semiconductor fabrication. Ratings: **A** = Excellent (<10% volume swell, suitable for continuous service), **B** = Good (10–30% swell, acceptable for intermittent use), **C** = Fair (30–60% swell, limited service life), **D** = Poor (>60% swell or chemical attack, not recommended), **F** = Fails (rapid degradation).

| Chemical | NR | NBR | CR (Neoprene) | EPDM | Silicone (VMQ) | FKM (Viton) | PTFE |
|---|---|---|---|---|---|---|---|
| **Sulfuric acid (10%)** | B | B | A | A | B | A | A |
| **Sulfuric acid (conc.)** | F | F | D | B | D | A | A |
| **Hydrofluoric acid (49%)** | F | B | C | B | C | A | A |
| **Nitric acid (10%)** | D | C | B | A | C | A | A |
| **Nitric acid (conc.)** | F | F | F | D | F | B | A |
| **Hydrochloric acid (10%)** | D | B | B | A | B | A | A |
| **HCl (conc.)** | F | D | C | B | C | A | A |
| **Phosphoric acid (85%)** | D | B | B | A | B | A | A |
| **Sodium hydroxide (50%)** | B | B | B | A | B | C | A |
| **KOH (45%)** | B | B | B | A | B | C | A |
| **Acetone** | D | D | D | A | D | F | A |
| **Isopropanol (IPA)** | B | B | B | A | B | A | A |
| **Toluene** | F | C | D | F | D | A | A |
| **Xylene** | F | C | D | F | D | A | A |
| **NMP (N-methylpyrrolidone)** | F | D | D | A | D | F | A |
| **Ethanol** | B | B | B | A | B | A | A |
| **DI Water (80°C)** | A | A | A | A | A | A | A |
| **Ozone (5 ppb)** | F | C | A | A | A | A | A |
| **Steam (120°C)** | C | C | C | A | B | A | A |
| **Silicon oil** | C | B | B | C | C | A | A |

**PTFE note**: PTFE (Teflon) is included as a reference — it is chemically inert to virtually all process chemicals but is not an elastomer (it cold-flows under load, cannot function as a compression seal without backup). Used as a liner material rather than a sealing material.

## O-Ring Selection for Semiconductor Wet Process Equipment

**Wet benches** (etching, cleaning, stripping stations that use concentrated acids and solvents):

1. **Standard acid service** (H₂SO₄, H₃PO₄, HCl, HF mixtures at 20–80°C):
   - Primary: FKM (Viton) — rated to 200°C, resistant to all common acids except hot concentrated HNO₃ and ketones (acetone, MEK). Use peroxide-cured FKM for best compression set (<20% after 70 hrs at 200°C). O-ring hardness: Shore A 75.
   - Economy alternative: EPDM — excellent acid and alkali resistance at lower cost than FKM, but swells severely in hydrocarbon solvents. Use EPDM for acid-only wet benches (no solvent exposure). O-ring hardness: Shore A 70.
   - Not acceptable: NBR (degrades in oxidizing acids), NR (degrades in nearly all semiconductor chemicals), silicone (swells in many solvents, low mechanical strength).

2. **Solvent service** (acetone, NMP, toluene, xylene for photoresist stripping):
   - Primary: FKM (Viton) for most solvents — but FKM fails in ketones (acetone, MEK) and esters.
   - For acetone/NMP service: EPDM is the best elastomeric choice (A-rating for both). However, EPDM is not suitable for simultaneous solvent + acid exposure.
   - PTFE-encapsulated O-rings (PTFE outer shell with FKM or silicone core) provide chemical inertness of PTFE with elastic recovery of the elastomer core — used where no single elastomer is adequate.

3. **Ultra-pure water (UPW) service** (18 MΩ·cm deionized water at 20–80°C):
   - EPDM is the standard for UPW distribution systems — it does not leach extractables at detectable levels when properly formulated. Use peroxide-cured, metal oxide-free EPDM to minimize ion extraction.
   - Silicone is also acceptable for UPW but has higher extractable levels than EPDM.
   - O-ring hardness: Shore A 70. Extractable specification: <50 ppb total organic carbon (TOC) after 72-hour浸泡 test per SEMI F57.

**Vacuum service** (load locks, transfer chambers, deposition systems):

- O-rings for vacuum: FKM (Viton) is standard for rough to high vacuum (10⁻³ to 10⁻⁸ Torr). Low outgassing rate: 1.5 × 10⁻⁹ Torr·L/(s·cm²) after 24-hour bake at 150°C. Shore A 75.
- For ultra-high vacuum (UHV, <10⁻⁹ Torr): metal seals (copper, indium, or ConFlat knife-edge copper gaskets) replace elastomers entirely — all elastomers outgas too much for UHV.
- Silicone O-rings have higher outgassing than FKM (10⁻⁸ vs. 10⁻⁹ Torr·L/(s·cm²)) and are used only in non-critical vacuum applications.
- Pre-baking vacuum O-rings at 150°C for 4–24 hours under vacuum removes adsorbed water and volatile compounds, reducing outgassing by 10–100×.

## FKM Grades for Semiconductor Service

**Standard FKM (Viton A)**: Copolymer of VDF + HFP. 66% fluorine. General-purpose chemical resistance. Service -20 to +200°C.

**Intermediate fluorine FKM (Viton B)**: Terpolymer of VDF + HFP + TFE. 68% fluorine. Better resistance to acids, fuels, and steam than Viton A. Standard for semiconductor wet benches.

**High-fluorine FKM (Viton F)**: Terpolymer with higher TFE content. 70% fluorine. Best chemical resistance, especially to concentrated acids and aggressive solvents. Service -20 to +230°C. Higher cost (3–5× standard FKM).

**Perfluoroelastomer (FFKM, Kalrez, Chemraz)**: Fully fluorinated polymer (like PTFE but cross-linked). Fluorine content >70%. Chemical resistance approaching PTFE — resistant to virtually all process chemicals including hot concentrated HNO₃, amines, and ketones that destroy FKM. Service -20 to +327°C (short-term). Cost: 100–500× standard FKM. Used only for the most critical seals in semiconductor equipment where no other elastomer survives — specifically: plasma etch chamber seals, CVD reactor door seals, and hot concentrated HNO₃ handling.

| Property | FKM (Viton B) | FFKM (Kalrez) | PTFE (reference) |
|---|---|---|---|
| Fluorine content | 68% | >70% | 76% |
| Service temp (max) | 200°C | 327°C | 260°C |
| Tensile strength | 10–20 MPa | 15–25 MPa | 20–35 MPa |
| Compression set (70h, 200°C) | 15–30% | 15–25% | N/A (cold flows) |
| HF (49%) resistance | A | A | A |
| HNO₃ (conc.) resistance | B | A | A |
| Acetone resistance | F | A | A |
| Cost multiplier vs. NR | 20–50× | 100–500× | 10–30× |
| Outgassing (Torr·L/s/cm²) | 1.5 × 10⁻⁹ | 5 × 10⁻¹⁰ | N/A |

## Cleanroom-Compatible Elastomer Requirements

Elastomers used in semiconductor cleanrooms (ISO Class 4–6) must meet stringent cleanliness requirements:

**Particle generation**: O-rings and seals must not shed particles during operation. Low-extraction formulations minimize surface contamination. Pre-cleaned O-rings (washed in ultra-pure water and packaged in cleanroom-compatible bags) are available from specialty suppliers. Particle specification: <100 particles ≥0.1 μm per O-ring (SEMI E49).

**Extractable limits**: Elastomers in contact with process fluids or UPW must not leach organic or ionic contaminants:
- Total organic carbon (TOC) extractables: <50 ppb (SEMI F57 for UPW contact)
- Metal ion extractables (Na, K, Ca, Mg, Fe, Cu, Zn): <1 ppb each (SEMI F57)
- Anion extractables (Cl⁻, F⁻, SO₄²⁻, NO₃⁻): <1 ppb each

**Material certification**: Elastomers for semiconductor use require lot-traceable certification of:
- Material composition (no prohibited additives — certain accelerators, plasticizers, and antioxidants are banned due to metal contamination risk)
- Extractable testing results per SEMI F57
- Particle count per SEMI E49
- Outgassing rate per SEMI E42

## Chemical-Resistant Linings

Semiconductor wet benches and chemical distribution systems use elastomeric and fluoropolymer linings to protect structural materials from chemical attack:

**PTFE-lined pipes and fittings**: PTFE liner (1.5–3.0 mm thick) inside carbon steel or stainless steel pipe. PTFE provides universal chemical resistance. Lining process: paste-extrude PTFE onto a mandrel, sinter at 380°C, then insert into the metal pipe and flare the ends. Temperature limit: 260°C. Pressure limit: 10–15 bar (PTFE cold-flows under sustained pressure above 10 bar at elevated temperature — the metal outer pipe provides restraint).

**PVDF (polyvinylidene fluoride) lined pipe**: Lower cost alternative to PTFE for less aggressive chemical service (resists acids and halogens but not as universally inert as PTFE). Service to 140°C. Used for: UPW distribution, dilute acid distribution, drain lines.

**FKM-lined components**: FKM sheet lining (3–6 mm) bonded to metal substrates with adhesive for chemical pump seals, valve bodies, and tank linings. Service to 200°C. Used for: wet bench process tanks, pump casings handling concentrated acids.

## Vibration Isolation Pads

Semiconductor fabrication equipment (steppers, scanners, electron microscopes, precision measurement tools) requires vibration isolation to sub-micron levels:

**Natural rubber isolation pads**: Effective for frequencies above 5–10 Hz. Dynamic stiffness 1.2–1.8× static stiffness (damping factor). Load capacity 0.5–5 MPa depending on hardness (Shore A 40–60 for isolation, A70–80 for high-load mounts). Rubber pads are the simplest and most cost-effective isolator for heavy equipment.

**Silicone isolation mounts**: Service range -60 to +200°C. Used where temperature excursions exceed natural rubber capability. Lower damping than NR (less energy dissipation per cycle).

**Active vibration isolation**: Pneumatic air springs with servo-controlled pressure provide isolation below 1 Hz — required for lithography steppers and scanning electron microscopes. Air supply at 3–7 bar, response time <10 ms. The elastomeric air bag provides the spring element; a piezoelectric or electromagnetic actuator provides active damping.

## Hose and Tubing for Chemical Distribution

**PTFE-lined hoses**: PTFE inner tube (1.5–2.0 mm) with stainless steel braid reinforcement. Chemical resistance: universal. Pressure rating: 10–20 bar at 20°C. Bend radius: 10× hose diameter (stiffer than rubber hoses). Used for: concentrated acid distribution in semiconductor fabs.

**FKM hoses**: Solid FKM rubber tube with textile or wire reinforcement. Chemical resistance: excellent for acids, bases, and most solvents. More flexible than PTFE-lined hoses. Temperature range: -20 to +200°C. Used for: acid and solvent distribution where flexibility is needed.

**EPDM hoses**: Standard for UPW distribution and dilute chemical transfer. Low extractable levels when properly compounded. Temperature range: -50 to +150°C. Cost: 3–5× less than FKM hoses.

## Material Selection Decision Tree

1. **Is the seal for vacuum service?**
   - Yes → Go to 2
   - No → Go to 3
2. **Vacuum level?**
   - Rough (>10⁻³ Torr) → FKM (Viton), standard grade
   - High (10⁻³–10⁻⁸ Torr) → FKM, pre-baked 24h at 150°C
   - Ultra-high (<10⁻⁹ Torr) → Metal seals (copper ConFlat), not elastomer
3. **What fluid does the seal contact?**
   - Acids only (H₂SO₄, HF, HCl, H₃PO₄) → FKM or EPDM
   - Solvents only (acetone, NMP, IPA) → EPDM (not FKM for ketones)
   - Mixed acids + solvents → FFKM (Kalrez) or PTFE-encapsulated
   - UPW → EPDM (peroxide-cured, low-extractable grade)
   - Steam/hot water → EPDM (best steam resistance)
4. **Temperature requirement?**
   - <100°C → All elastomers acceptable
   - 100–150°C → FKM, EPDM, or silicone
   - 150–200°C → FKM or silicone
   - >200°C → FFKM (Kalrez) or metal seals
5. **Cleanliness requirement?**
   - General industrial → Standard FKM or EPDM
   - Cleanroom (ISO 6) → Low-extractable grade FKM, pre-cleaned
   - Critical wet bench → FFKM (Kalrez) or PTFE-lined, certified to SEMI F57

## Bill of Materials

| Material | Grade | Application | Notes |
|---|---|---|---|
| FKM (Viton B) | 68% fluorine, terpolymer | O-rings, wet bench seals, vacuum seals | Standard for acid and vacuum service |
| FFKM (Kalrez/Chemraz) | >70% fluorine, perfluorinated | Plasma etch seals, hot HNO₃ service | 100-500× cost of FKM; use only where required |
| EPDM (peroxide-cured) | Metal oxide-free, low-extractable | UPW distribution, dilute acid, steam lines | Not resistant to hydrocarbon solvents |
| PTFE (Teflon) | Paste-extruded liner, 1.5-3.0 mm | Pipe and hose linings | Not an elastomer — cold-flows under load |
| PTFE-encapsulated O-rings | PTFE shell + FKM core | Mixed chemical service | PTFE chemical resistance + elastomer recovery |
| Silicone (VMQ) | Shore A 50-70 | Non-critical vacuum, low-temperature service | Higher outgassing than FKM |
| PVDF lining | 2-3 mm sheet | UPW and dilute acid pipe lining | Lower cost than PTFE, 140°C max |
| NR isolation pads | Shore A 40-60 | Vibration isolation for equipment | Effective above 5-10 Hz |

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| O-ring swelling in service | Chemical incompatibility — elastomer absorbing solvent | Check chemical against resistance table; upgrade to FKM or FFKM |
| Seal hardening and cracking | Thermal aging or oxidation at elevated temperature | Replace with higher-temperature grade (FKM→FFKM); check operating temp |
| Vacuum leak at O-ring seal | Compression set — seal lost elastic recovery after prolonged compression | Replace O-ring. Use lower compression-set grade (peroxide-cured FKM <20%) |
| Particle contamination in process fluid | Elastomer shedding particles or improper cleaning | Use pre-cleaned, low-extraction grade O-rings (SEMI E49 certified) |
| Wafer contamination (metal ions) | Elastomer leaching extractables into UPW or process stream | Switch to metal oxide-free, peroxide-cured EPDM; verify SEMI F57 compliance |
| O-ring extrusion under pressure | Pressure exceeds seal capability or gland design is wrong | Add anti-extrusion backup ring; reduce gland clearance; use harder durometer |
| PTFE liner cold-flow failure | Sustained pressure >10 bar at elevated temperature | Add metal reinforcement; reduce operating pressure; consider PVDF alternative |
| FKM failure in acetone/NMP service | FKM is incompatible with ketones and esters (F-rating) | Switch to EPDM (A-rated for acetone/NMP) or PTFE-encapsulated |


## See Also

- [Rubber Production](rubber.md) — overview of rubber and elastomer manufacturing
- [Vulcanization](rubber.vulcanization.md) — cross-linking parameters and hardness scales
- [Synthetic Polymers](synthetic.md) — FKM, EPDM, silicone, and fluoropolymer synthesis
- [Gutta-Percha](gutta-percha.md) — natural polymer cable insulation
- [Acids](../chemistry/acids.md) — HF, H₂SO₄, HNO₃ production for wet processes
- [Gas Handling / Vacuum](../gas-handling/vacuum.md) — vacuum seal requirements and outgassing
- [Cleanrooms](../photolithography/cleanrooms.md) — cleanroom classification and standards
- [Fab Processes](../photolithography/fab-processes.md) — semiconductor manufacturing overview

[← Back to Polymers](index.md)
