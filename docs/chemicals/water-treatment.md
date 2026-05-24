# Industrial Water Treatment

> **Node ID**: chemicals.water-treatment
> **Domain**: Chemicals
> **Timeline**: Years 10-30
> **Outputs**: deionized_water, purified_water, ultrapure_water

## Overview

Water purification for industrial use ranges from simple settling and sand filtration (potable grade) through distillation and ion exchange (deionized) to reverse osmosis and ultrafiltration (ultrapure, 18 MΩ·cm). High-purity water is essential for acid dilution, electroplating baths, glass working, and especially semiconductor fabrication where contaminants at ppb levels can destroy yields.

## Purification Hierarchy

Water purification is a staged process, each stage removing a specific class of contaminants. No single method removes everything — the stages must be applied in sequence:

**Stage 1: Coagulation and settling** (removes suspended solids >1 μm):
- Add coagulant (alum Al₂(SO₄)₃ at 10-50 mg/L, or ferric chloride FeCl₃ at 5-30 mg/L) to raw water. Rapid mix (300-500 RPM for 1-3 minutes), then slow mix (20-40 RPM for 15-30 minutes) to form floc.
- Floc (gelatinous aluminum or iron hydroxide) entraps suspended particles, bacteria, and colloids. Settle in clarifier basin (surface loading 1-2 m/hour, detention time 2-4 hours). Removes 90-95% of turbidity.
- Sludge from clarifier bottom: 0.5-2% solids, withdrawn continuously or intermittently. Dewater in drying beds (7-14 days) or mechanical filter press.

**Stage 2: Sand filtration** (removes particles 10-50 μm):
- Downflow through graded sand bed (0.6-1.0 m deep, effective sand size 0.4-0.8 mm, uniformity coefficient 1.3-1.7) at filtration rate 5-10 m/hour.
- Backwash when head loss exceeds 1.5-2.0 m (typically every 24-48 hours): reverse flow at 30-50 m/hour for 5-10 minutes expands bed and flushes accumulated solids.
- Twin alternating filters provide continuous operation. Product: <1 NTU turbidity, <5 ppm suspended solids.

**Stage 3: Activated carbon filtration** (removes organic compounds, chlorine, taste/odor):
- Granular activated carbon (GAC) bed, 1.0-2.0 m depth, EBCT (empty bed contact time) 10-20 minutes. Removes chlorine (critical pretreatment for RO membranes — free chlorine destroys polyamide membranes), organic compounds (reduces TOC to <1 ppm), and disinfection byproduct precursors.
- Carbon capacity: 5-20% of carbon weight in adsorbed organics. Replace or regenerate (thermal reactivation at 800-1000°C in steam) when breakthrough occurs (typically 6-18 months depending on influent quality).

**Stage 4: Ion exchange** (removes dissolved ions — produces deionized water):
- Cation exchange bed: strong acid cation resin (sulfonated polystyrene, H⁺ form) removes all cations (Ca²⁺, Mg²⁺, Na⁺, K⁺, Fe²⁺/³⁺) and replaces with H⁺. Effluent pH drops to 2-3.
- Anion exchange bed: strong base anion resin (quaternary ammonium, OH⁻ form) removes all anions (Cl⁻, SO₄²⁻, HCO₃⁻, SiO₃²⁻) and replaces with OH⁻. H⁺ + OH⁻ → H₂O.
- Mixed bed (cation + anion resin in single vessel) polishes to 10-18 MΩ·cm resistivity. Silica target: <10 ppb as SiO₂.
- Regeneration: cation resin with 4-8% HCl (100-150 g/L resin), anion resin with 4-8% NaOH (50-100 g/L resin). Regeneration waste is acidic or alkaline — neutralize before discharge.
- Throughput: 1 m³ resin treats 500-2,000 m³ water before regeneration, depending on influent TDS. Typical service flow rate: 10-40 bed volumes/hour.

**Stage 5: Membrane processes** (removes dissolved ions and organics at molecular level):

*Reverse osmosis (RO)*: Forces water through a semipermeable membrane (polyamide thin-film composite, 0.1-1.0 nm pore size) at 10-70 bar pressure. Rejects 95-99% of dissolved ions, 99%+ organics, and 99.9%+ bacteria and particles. Energy: 3-8 kWh/m³ product water. Recovery: 50-80% (remainder is concentrate/brine). Single-pass RO produces 5-20 μS/cm water; double-pass (RO permeate through a second RO stage) achieves <1 μS/cm.

*Nanofiltration (NF)*: Similar to RO but at lower pressure (5-20 bar) with larger pores (1-5 nm). Rejects 80-95% divalent ions (Ca²⁺, Mg²⁺, SO₄²⁻) but only 20-50% monovalent ions (Na⁺, Cl⁻). Useful for water softening before RO.

*Ultrafiltration (UF)*: Pore size 2-100 nm, pressure 1-5 bar. Removes colloids, bacteria (99.9999%), viruses (99.99%), and high-molecular-weight organics. Does not remove dissolved ions. Used as RO pretreatment.

*Microfiltration (MF)*: Pore size 100-1000 nm, pressure 0.5-2 bar. Removes suspended solids, large bacteria, and algae. Equivalent to absolute filtration at 0.1-1.0 μm.

**Stage 6: Polishing** (for ultrapure water, 18.2 MΩ·cm):

*Electrodeionization (EDI)*: Continuous ion exchange combining ion exchange resin with an electric field. Ions migrate into concentrate compartments and are continuously removed — no chemical regeneration needed. Product: 15-18 MΩ·cm. Feed must be RO-quality (<20 μS/cm). Power: 0.2-0.5 kWh/m³.

*UV oxidation*: 185 nm UV lamp breaks down trace organic compounds (TOC reduction to <5 ppb). 254 nm UV provides disinfection (99.9% bacteria kill at 30-40 mJ/cm² dose). Lamp output degrades over 8,000-12,000 hours of operation.

*Membrane degasification*: Hollow fiber membrane contactors remove dissolved CO₂ and O₂ to <1 ppb. Critical for semiconductor-grade water where dissolved gases interfere with wafer processing.

*Final filtration*: 0.05-0.2 μm membrane filter (polyethersulfone or nylon) removes any particles shed by upstream equipment. Absolute-rated — captures 99.9999% at rated pore size.

## Ultrapure Water for Semiconductor Fabrication

Semiconductor manufacturing is the most demanding water purity application. The target specifications for 18.2 MΩ·cm ultrapure water (UPW):

| Parameter | Target | Typical Semiconductor Spec |
|-----------|--------|---------------------------|
| Resistivity | 18.2 MΩ·cm at 25°C | 18.0-18.2 MΩ·cm |
| TOC (total organic carbon) | <1 ppb | <5 ppb |
| Bacteria | <1 CFU/100 mL | <1 CFU/100 mL |
| Particles ≥0.05 μm | <100/mL | <500/mL |
| Dissolved O₂ | <10 ppb | <50 ppb |
| Silica (SiO₂) | <1 ppb | <3 ppb |
| Metals (each) | <0.1 ppb | <1 ppb |
| Anions (each) | <0.1 ppb | <1 ppb |

A modern 300 mm wafer fab producing 50,000 wafers/month consumes 5,000-10,000 m³/day of UPW — roughly 100-200 L per wafer for rinsing between process steps. UPW production cost: $4-10/m³ (vs. $0.50-1.00/m³ for potable water). The UPW system is typically 15-20% of total fab capital cost.

## Distillation for High-Purity Water

**Simple distillation**: Boil water, condense vapor. Removes all non-volatile impurities (minerals, heavy metals, bacteria). Does not remove volatile impurities (ammonia, chlorine, VOCs). Energy: 620 kWh/m³ (latent heat of vaporization 2,260 kJ/kg). Product: 1-5 μS/cm.

**Multiple-effect distillation**: Vapor from first effect (boiler) heats second effect at lower pressure, and so on through 4-12 effects. Energy consumption drops to 100-200 kWh/m³ with 6 effects. Each effect operates at progressively lower pressure/temperature (first effect: 120°C, 200 kPa; last effect: 60°C, 20 kPa). Product: <1 μS/cm, pyrogen-free (suitable for pharmaceutical injection water — WFI, water for injection).

**Vapor compression distillation**: Mechanically compress vapor to raise condensation temperature, providing heat source for evaporation. Energy: 60-120 kWh/m³. Single-effect or double-effect designs. Product quality equivalent to multiple-effect.

## Water Treatment for Specific Industries

**Boiler feed water** (power generation, steam systems):
- Dissolved oxygen corrodes steel boiler tubes at high temperature — must be reduced to <7 ppb (mechanical deaeration at 102-105°C plus chemical scavenger: sodium sulfite Na₂SO₃ at 3-5× stoichiometric, or hydrazine N₂H₄ at 50-100 ppb residual).
- Total dissolved solids (TDS) limited to 50-3,500 ppm depending on boiler pressure (low-pressure heating boilers tolerate 3,500 ppm; high-pressure utility boilers require <0.5 ppm).
- Silica limit: 0.02-0.5 ppm depending on pressure (silica deposits on turbine blades as glassy scale at >600°C).
- pH maintained at 9.0-10.0 (ammonia or morpholine addition) to minimize steel corrosion.
- Blowdown (controlled discharge of concentrated boiler water) at 5-10% of feed rate to prevent TDS accumulation.

**Cooling water treatment**:
- Circulating cooling water at 25-40°C promotes biological growth (algae, bacteria, slime). Dose biocide (chlorine gas at 0.5-1.0 ppm free residual, or sodium hypochlorite at 1-3 ppm continuous feed).
- Scale inhibition: add phosphonate (HEDP at 5-10 ppm) or polyacrylate (5-15 ppm) to prevent CaCO₃ and CaSO₄ precipitation.
- Corrosion inhibition: sodium nitrite (500-1000 ppm) or molybdate (50-100 ppm) in closed-loop systems. Chromate (now restricted for environmental reasons) was historically used at 200-500 ppm.
- Cycles of concentration: 3-7× (blow down when TDS reaches 3-7× makeup water TDS).

**Electroplating rinse water**:
- Drag-out from plating baths contaminates rinse water with heavy metals (Cr, Ni, Cu, Zn, Cd, cyanide). Must treat before discharge.
- Recovery: ion exchange recovers metals from dilute rinse water; electrowinning plates recovered metal from ion exchange regenerant.
- Cyanide destruction: alkaline chlorination (NaOCl + CN⁻ → CNO⁻ at pH >10, then CNO⁻ → CO₂ + N₂ at pH 7-8). Chromium reduction: Cr⁶⁺ + FeSO₄ → Cr³⁺ at pH 2-3, then precipitate Cr(OH)₃ with NaOH at pH 8-9.

## Reverse Osmosis System Design

A complete RO system for producing deionized-quality water from municipal or well feed consists of multiple subsystems:

**Pretreatment train**: Multimedia filter (anthracite + sand + garnet layers, removes particles >10 μm) → antiscalant injection (sodium hexametaphosphate at 2-5 ppm prevents CaSO₄ and CaCO₃ scaling) → cartridge filter (5 μm absolute, protects RO pump and membranes) → dechlorination (sodium bisulfite NaHSO₃ at 2-3× stoichiometric, or activated carbon bed — free chlorine destroys polyamide RO membranes).

**High-pressure pump**: Multistage centrifugal pump delivers 10-70 bar (150-1000 psi) at flow rates of 1-500 m³/hour. Stainless steel (316L) construction. Motor: 5-500 kW depending on system size. Energy recovery devices (turbochargers or pressure exchangers) on the concentrate stream recover 30-50% of pumping energy in seawater systems.

**Membrane elements**: Spiral-wound polyamide thin-film composite (TFC) on polysulfone support, 8-inch diameter × 40-inch length. Each element: 37-440 m² active membrane area. Salt rejection: 99.0-99.8%. Permeate flow: 20-50 L/m²/day depending on feed salinity and pressure. Arrange 6-7 elements in series per pressure vessel; multiple vessels in parallel form a single stage. Two-stage arrangement (concentrate from first stage feeds second stage) achieves 75% recovery.

**Post-treatment**: Permeate at 5-20 μS/cm → mixed-bed ion exchange polisher → UV sterilizer → 0.2 μm final filter → storage tank with nitrogen blanket (prevents CO₂ absorption from air, which would lower resistivity).

## Desalination

**Seawater reverse osmosis (SWRO)**: Seawater at 35,000 ppm TDS requires 55-70 bar pressure. Energy consumption: 3-5 kWh/m³ product water (with energy recovery; without, 6-8 kWh/m³). Recovery: 35-50%. Boron rejection is challenging — polyamide membranes reject only 70-90% of boron (present as boric acid H₃BO₃, which is uncharged at seawater pH). Second-pass RO at pH 10 (where boron is ionized) achieves >95% boron rejection.

**Brackish water RO (BWRO)**: Feed at 1,000-10,000 ppm TDS. Pressure: 10-25 bar. Energy: 0.5-2.5 kWh/m³. Recovery: 65-85%. Suitable for inland brackish aquifers. Concentrate disposal: deep well injection, evaporation ponds, or zero-liquid-discharge (ZLD) crystallizer.

**Multi-stage flash distillation (MSF)**: Flash evaporation of seawater through a series of chambers at progressively lower pressure. 20-30 stages. Top brine temperature: 110-120°C. Energy: 10-15 kWh/m³ thermal + 3-4 kWh/m³ electrical. GOR (gain output ratio): 8-12 kg distillate per kg steam. Historically dominant in Middle East where energy is cheap. Product: <10 ppm TDS.

## Deaeration and Gas Removal

**Mechanical deaeration** (spray/tray type): Feed water sprayed into a steam-heated deaerator at 102-105°C. Dissolved gases (O₂, CO₂) have reduced solubility at elevated temperature and are stripped out by countercurrent steam flow. Removes O₂ to <7 ppb and CO₂ to <5 ppm. Essential for boiler feed water — dissolved O₂ at 1 ppm corrodes carbon steel at 0.5-1.0 mm/year in boiler tubes at 200-300°C.

**Vacuum deaeration**: Water sprayed into a vessel under vacuum (5-10 kPa absolute). Dissolved gases flash out. Removes O₂ to <50 ppb without heating. Used when thermal deaeration is impractical (e.g., cold water systems).

**Membrane degasification**: Hydrophobic hollow fiber membranes (polypropylene, 0.05 μm pore) allow dissolved gases to pass but block liquid water. Sweep gas (N₂) or vacuum on the shell side strips O₂ and CO₂ from water. Achieves <1 ppb O₂ and <1 ppb CO₂. Used in semiconductor UPW systems and power plant condensate polishing.

## Zero Liquid Discharge (ZLD)

For facilities that cannot discharge any wastewater (e.g., in arid regions or where regulations prohibit brine discharge), ZLD systems recover all water as purified product and produce solid waste only.

**Process**: Pretreated wastewater → RO (to 50,000 ppm concentrate) → brine concentrator (falling-film evaporator, produces 100,000+ ppm concentrate) → crystallizer (forced-circulation evaporator at 100-120°C, precipitates salts) → centrifuge or filter press separates solids. Recovered distillate returns to process. Solid salts (NaCl, CaSO₄, mixed salts) landfilled.

**Energy**: 25-50 kWh/m³ for complete ZLD. Capital cost: 5-10× conventional wastewater treatment. Operated only where absolutely required — recovery of valuable dissolved materials (e.g., lithium from brine) can offset costs.

## Water Quality Testing

**Conductivity/resistivity**: Inverse relationship — conductivity (μS/cm) = 1/resistivity (MΩ·cm). Pure water at 25°C: 0.055 μS/cm = 18.2 MΩ·cm. Theoretical minimum conductivity due to self-ionization (H₂O ⇌ H⁺ + OH⁻, Kw = 10⁻¹⁴ at 25°C). Temperature compensation: conductivity increases ~2% per °C.

**pH measurement**: Glass electrode + reference electrode. Calibrate with pH 4.01, 7.00, and 10.01 buffer solutions before each measurement. Accuracy: ±0.01 pH units for laboratory-grade meters. Industrial online monitors: ±0.1 pH.

**Total dissolved solids (TDS)**: Estimated from conductivity: TDS (ppm) ≈ 0.5-0.7 × conductivity (μS/cm). Direct measurement: evaporate filtered sample, weigh residue.

**Total organic carbon (TOC)**: Oxidize organic carbon to CO₂ (UV/persulfate oxidation or high-temperature combustion at 680-800°C), measure CO₂ by NDIR. Range: 4 ppb to 50,000 ppm. Semiconductor-grade: <5 ppb target.

**Particle counting**: Laser light scattering. Count and size particles in real time. Ranges: 0.05-100 μm. Semiconductor UPW: <100 particles/mL ≥0.05 μm.

## Ion Exchange Resin Production

Strong acid cation resin: Polystyrene crosslinked with divinylbenzene (DVB, 8% crosslinking is standard), then sulfonated (H₂SO₄ + 1,2-dichloroethane solvent at 80-100°C for 4-8 hours). Capacity: 1.8-2.0 eq/L (equivalents per liter of resin). Service flow: 10-40 bed volumes/hour. Pressure drop: 0.1-0.5 bar/m bed depth.

Strong base anion resin: Polystyrene-DVB (same base), then chloromethylated (CH₂O + HCl in chloromethyl methyl ether — carcinogenic, handle with extreme care), then aminated with trimethylamine (TMA) at 25-35°C for 6-12 hours. Type I (TMA): highest silica removal, lower capacity. Type II (dimethylethanolamine): higher capacity, less effective on silica.

Resin lifespan: 3-7 years in normal service. Failure modes: fouling (iron, organics), oxidation (free chlorine attacks polymer backbone — limit to <0.1 ppm Cl₂), thermal degradation (anion resins degrade above 40°C), and osmotic shock from rapid concentration changes.

## Wastewater Treatment Basics

Industrial water treatment includes treating used water before discharge. The standard treatment chain applies to process wastewater from chemical plants, metal finishing, and semiconductor fabrication:

**pH adjustment**: Neutralize acidic or alkaline waste streams to pH 6-9 before any further treatment. Use H₂SO₄ for alkaline waste, NaOH or Ca(OH)₂ for acidic waste. Automatic pH control: pH probe → controller → dosing pump. Response time: 1-5 minutes for well-mixed tanks.

**Chemical precipitation**: Add coagulant (FeCl₃ at 50-200 ppm or Al₂(SO₄)₃ at 50-150 ppm) to aggregate colloidal metals and suspended solids. Adjust pH to optimal precipitation range for target metals: Cr³⁺ at pH 7-8, Cu²⁺ at pH 8-10, Zn²⁺ at pH 9-10. Flocculant (polyacrylamide at 0.5-2.0 ppm) increases floc size for faster settling.

**Heavy metal removal**: Adjust pH to precipitate metals as hydroxides. For hexavalent chromium (Cr⁶⁺), reduce to Cr³⁺ first (NaHSO₃ or FeSO₄ at pH 2-3, then raise pH to 8-9). For cyanide, destroy by alkaline chlorination before metals removal. Residual dissolved metals: 0.5-5 ppm after precipitation, polished to <0.1 ppm by ion exchange or sulfide precipitation (Na₂S at stoichiometric + 10% excess).

**Biological treatment**: For organic waste streams (BOD 100-10,000 ppm), aerobic biological treatment (activated sludge: 2-6 hour aeration at 1.5-3.0 kg O₂/kg BOD, MLSS 2,000-5,000 mg/L) reduces BOD by 90-95%. Anaerobic treatment for high-strength waste (COD >5,000 ppm) produces biogas (0.3-0.5 m³ CH₄ per kg COD removed) and requires 10-30 day hydraulic retention time.

## Storage and Distribution of Purified Water

**Deionized water storage**: Closed tanks with nitrogen or CO₂ blanket to prevent atmospheric CO₂ absorption (CO₂ dissolves to form H₂CO₃, lowering resistivity from 18 MΩ·cm to <1 MΩ·cm within hours). Tank material: 316L stainless steel (electropolished) or virgin polyethylene. No dead legs (stagnant zones promote bacterial growth). Recirculate continuously at 1-3 m/s velocity through UV and 0.2 μm filters to maintain purity during storage.

**Piping**: PVDF (polyvinylidene fluoride) or 316L stainless steel (electropolished, orbital-welded joints). No threaded connections (leak points and bacterial traps). Slope piping 1% toward drain points. All valve bodies and seals compatible with UPW (EPDM or PTFE seals; no lubricants). Distribution loop: continuous recirculation from storage tank through process tools and back.

**Microbial control**: UV (254 nm) at 30-40 mJ/cm² in recirculation loop. Ozone (O₃ at 0.01-0.1 ppm, generated by corona discharge on O₂ feed) provides continuous disinfection without leaving chemical residue (O₃ decomposes to O₂ in minutes). Hot water sanitization (80°C for 2-4 hours) of entire distribution system on a quarterly basis eliminates biofilm.

## Water Treatment Chemicals

**Coagulants and flocculants**: Alum (Al₂(SO₄)₃·14H₂O) at 10-100 mg/L is the most common coagulant. Ferric chloride (FeCl₃) at 5-50 mg/L works better in cold water. PAC (polyaluminum chloride) at 5-30 mg/L produces less sludge. Flocculant aids: polyacrylamide (anionic for mineral suspensions, cationic for organic waste) at 0.5-2.0 mg/L. Dose optimization by jar test (6 beakers at varying doses, mix 1 min fast + 15 min slow, settle 30 min, measure supernatant turbidity).

**Disinfectants**: Chlorine gas (Cl₂ at 1-5 mg/L, contact time 30 min at pH 7-8, CT value >15 mg·min/L for 99.9% Giardia inactivation). Sodium hypochlorite (NaOCl at 5-15% solution, dosed at 1-5 mg/L as Cl₂ equivalent). Ozone (O₃ at 0.5-2.0 mg/L, contact time 4-10 min, no residual — must follow with chlorine for distribution system protection). UV (254 nm at 30-40 mJ/cm², no chemical residual, no DBPs). Chlorine dioxide (ClO₂ at 0.5-1.5 mg/L, effective at pH 4-10, fewer disinfection byproducts than Cl₂).

**Antiscalants**: Sodium hexametaphosphate (SHMP, 2-5 mg/L) or polyphosphonate (1-3 mg/L) prevents CaCO₃ and CaSO₄ scale in RO and cooling systems. Dose based on scaling potential calculated from feed water analysis (Langelier Saturation Index, Ryznar Index).

**Corrosion inhibitors**: Orthophosphate (H₃PO₄ or Na₃PO₄ at 1-3 mg/L as PO₄) forms protective FePO₄ film on steel pipe interiors. Silicate (Na₂SiO₃ at 10-20 mg/L as SiO₂) for lead and copper corrosion control in drinking water. Zinc orthophosphate (1-3 mg/L) combines film-forming with cathodic inhibition.

## Cross-Domain Links

- **[Water Treatment (Health)](../health/water-treatment.md)**: potable water production, chlorination, boiling, and basic sanitation
- **[Electrolysis](../chemistry/electrolysis.md)**: chlor-alkali process producing chlorine for water disinfection
- **[Basic Semiconductor Devices](../silicon/basic-devices.md)**: UPW requirements for wafer processing
- **[Wafer Production](../silicon/wafer-production.md)**: CMP slurries and rinsing demand for ultrapure water
- **[Vacuum Systems](../vlsi-scaling/vacuum-systems.md)**: sealed water-cooled systems and deionized coolant
- **[Glass Fibers](../glass/fibers.md)**: high-purity water for optical fiber preform processing

---

*Part of the [Chemicals Domain](index.md) • [All Domains](../index.md)*

[← Back to Chemicals](index.md)
