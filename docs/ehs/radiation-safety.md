# Radiation Safety

> **Node ID**: ehs.radiation-safety
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: [`ehs.chemical-safety`](chemical-safety.md), [`health.occupational-health`](../health/occupational-health.md), [`chemistry`](../chemistry/index.md)
> **Enables**: [`measurement`](../measurement/index.md), [`health.diagnostics`](../health/diagnostics.md)
> **Timeline**: Years 30-100+
> **Outputs**: radiation_protection, shielding_design, dosimetry, contamination_control
> **Critical**: No — radiation safety becomes essential only when X-ray, nuclear, or semiconductor ion implantation equipment is in use

## Overview

Radiation safety covers ionizing radiation fundamentals, shielding design, dose monitoring, and contamination control. In a bootstrap civilization, radiation exposure arises from four sources: medical X-rays (diagnostic imaging), industrial radiography (weld inspection), naturally occurring radioactive materials (uranium, thorium, radon), and semiconductor manufacturing (ion implantation uses radioactive dopant sources). Understanding radiation safety is essential before any of these capabilities are deployed — radiation injuries are invisible, cumulative, and often manifest years after exposure.

The fundamental principle: ALARA — As Low As Reasonably Achievable. No level of ionizing radiation is considered completely safe. All exposure must be justified by benefit and minimized by shielding, distance, and time management. The three pillars of radiation protection: time (minimize time near source), distance (increase distance — dose falls with the square of distance), and shielding (interpose absorbing material between source and person).

## Prerequisites

### Materials

- Shielding materials: lead sheet (0.5-3 mm for X-ray), concrete (15-30 cm for general shielding), steel plate, barium sulfate (for painted shielding)
- Dosimetry materials: photographic film (film badge dosimeter), thermoluminescent crystals (TLD — LiF:Mg,Ti), or optically stimulated luminescence (OSL) badges (requires electronics)
- Warning signs: trefoil radiation symbol, posted at access points
- Survey instruments: Geiger-Müller counter, ionization chamber, or scintillation detector (requires [electronics](../electronics/assembly.md))
- Decontamination supplies: absorbent paper, detergent, chelating agents (EDTA, DTPA) for radioactive metal contamination

### Tools and Equipment

- Radiation survey meter: Geiger-Müller (GM) counter for contamination surveys, ionization chamber for exposure rate measurement
- Personal dosimeters: film badge, TLD, or electronic personal dosimeter (EPD)
- Shielding test equipment: lead thickness gauge, concrete density verification
- Calibration sources: known-activity check sources (Cs-137, Co-60, or Am-241) for instrument calibration

### Knowledge

- Radiation physics: alpha, beta, gamma, X-ray, neutron radiation characteristics
- Units: gray (Gy) for absorbed dose, sievert (Sv) for equivalent dose, becquerel (Bq) for activity, coulomb/kg (C/kg) for exposure
- Biological effects: deterministic (threshold dose, severity increases with dose) vs. stochastic (probability increases with dose, no threshold)
- Shielding calculations: half-value layer (HVL), tenth-value layer (TVL), buildup factors

### Infrastructure

- Shielded enclosure for radiation sources (lead-lined room or concrete bunker)
- Restricted access area with posted warning signs
- Dosimetry processing laboratory (if film badges or TLDs used)
- Radioactive waste storage: shielded, labeled, segregated by half-life

## Bill of Materials

| Material | Quantity per Shielded Room | Source | Alternatives |
|----------|---------------------------|--------|-------------|
| Lead sheet (2 mm) | 50-200 kg | [Metals](../metals/index.md) — lead smelting | Concrete (15 cm ≈ 1.5 mm Pb for diagnostic X-ray), steel plate (3× thickness of lead), barium sulfate plaster |
| Concrete (2.3 g/cm³ density) | 5-30 m³ | [Cement](../chemistry/cement.md) + aggregate | Barytes concrete (3.5 g/cm³ — 40% less thickness needed) |
| Film badge dosimeters | 1 per worker per month | [Photography](../knowledge/printing.md) — silver halide film | Electronic dosimeter (requires electronics, reusable) |
| Geiger-Müller counter | 1 per radiation area | [Electronics](../electronics/index.md) + Geiger tube | Ionization chamber (simpler electronics, no GM tube needed) |
| Warning signs (trefoil) | Per access point | Printed or painted | Hand-drawn trefoil with "RADIATION" label |

## Process Description

### Shielding Design for X-Ray Room

**Strengths**:
- Concrete shielding is widely available, inexpensive, and provides structural walls simultaneously
- Lead sheet shielding is extremely space-efficient (1.6 mm Pb equivalent to 15 cm concrete for 100 kVp X-ray)
- Calculation methods are well-standardized (NCRP Report 147, IAEA Safety Series)

**Weaknesses**:
- Shielding gaps at joints, door frames, and penetrations (electrical conduit, HVAC) are common failure points — require detailed construction oversight
- Lead is toxic and requires protected handling during installation and future demolition
- Retrofitting inadequate shielding is extremely expensive (room may need to be rebuilt)

1. **Determine workload**: Estimate weekly X-ray workload in mA-minutes per week. Example: 50 patients/week × 2 exposures each × 100 mA × 0.1 s = 1,000 mA-min/week.
2. **Calculate primary barrier thickness**: Determine distance from X-ray source to occupied area. Use inverse square law: dose at distance d = dose at 1 m / d². Calculate required barrier transmission factor to meet dose limit (0.02 mSv/week for controlled areas, 0.02 mSv/week for uncontrolled).
3. **Calculate secondary barrier**: Account for scattered radiation (0.1% of primary beam at 90° at 1 m) and leakage radiation (<1 mGy/hr at 1 m for diagnostic units). Secondary barriers are typically thinner than primary barriers.
4. **Select shielding material and thickness**: Use HVL data to determine required thickness. For lead: each HVL reduces dose by 50%. For diagnostic X-ray (100 kVp): HVL = 0.24 mm Pb. Required transmission 0.01 (1%) needs 6.6 HVLs = 1.6 mm Pb.
5. **Verify with survey meter**: After construction, measure actual dose rates outside barriers with calibrated survey meter. All points must be below regulatory limits. Document measurements.

### Personal Dosimetry Program

**Strengths**:
- Film badges and TLDs require no electronics — can be deployed at any technology level
- Provides permanent, legal-quality dose record for regulatory compliance
- Cumulative tracking catches chronic low-level overexposure that acute symptoms would miss

**Weaknesses**:
- Monthly/quarterly readout delay means acute overexposures are discovered after the fact
- Film badges are sensitive to heat, moisture, and light — improper storage causes false readings
- Does not provide real-time dose rate information (worker cannot self-monitor during a procedure)

1. **Issue dosimeters**: Each occupationally exposed worker receives a personal dosimeter worn at chest or waist level (collar if lead apron worn — to estimate unshielded dose). Dosimeter worn during all working hours in radiation areas.
2. **Collect and read**: Collect dosimeters monthly (film badge) or quarterly (TLD). Process through dosimetry laboratory. Record cumulative dose for each worker.
3. **Investigate overexposures**: Any dosimeter reading >10% of annual limit triggers investigation. Determine cause (unusual workload, shielding failure, improper technique). Implement corrective action.
4. **Maintain lifetime records**: Cumulative dose records maintained for each worker's entire career plus 30 years. Many radiation effects (cancer) have long latency periods.

### Contamination Control

**Strengths**:
- GM counter provides immediate feedback on decontamination effectiveness — no laboratory analysis needed
- Most surface contamination can be removed with soap, water, and chelating agents — no exotic materials required

**Weaknesses**:
- Porous surfaces (concrete, wood) can absorb contamination permanently — may require surface removal or replacement
- Internal contamination (inhalation, ingestion) cannot be removed by surface decontamination — requires medical intervention

1. **Survey work area**: Before beginning work with unsealed radioactive materials, survey the area with GM counter to establish background. After work, survey all surfaces, equipment, and personnel.
2. **Contain spills**: If radioactive material spills, alert personnel, isolate area, and don PPE. Cover spill with absorbent material. Work from outside inward to prevent spread. Place contaminated materials in labeled waste container.
3. **Decontaminate surfaces**: Wash with detergent and water. For stubborn contamination, use chelating agents (0.1 M EDTA solution for radioactive metals) or mild acid (1% citric acid). Monitor with GM counter after each wash cycle. Continue until count rate is at background level.
4. **Personnel decontamination**: For skin contamination, wash gently with soap and water. Do not abrade skin (drives contamination deeper). For hair contamination, shampoo repeatedly. If internal contamination suspected (inhalation, ingestion), collect urine samples for bioassay.

## Quantitative Parameters

### Radiation Dose Limits

| Category | Whole Body (mSv/yr) | Lens of Eye (mSv/yr) | Skin (mSv/yr) | Extremities (mSv/yr) | Embryo/Fetus (mSv/gestation) |
|----------|--------------------|--------------------|---------------|---------------------|---------------------------|
| Occupational (adult) | 20 (averaged over 5 yr, max 50 in single yr) | 20 (averaged over 5 yr) | 500 | 500 | 1 (declared pregnancy) |
| Occupational (minor, 16-18 yr) | 6 | 15 | 150 | 150 | — |
| General public | 1 | 15 | 50 | — | — |
| Emergency (lifesaving) | 500 (single event, voluntary) | — | — | — | — |

### Half-Value Layers for Common Shielding Materials

| Material | Density (g/cm³) | 100 kVp X-ray HVL | 200 kVp X-ray HVL | Co-60 (1.17/1.33 MeV) γ HVL |
|----------|----------------|--------------------|--------------------|-----------------------------|
| Lead | 11.35 | 0.24 mm | 0.48 mm | 12.5 mm |
| Steel/iron | 7.87 | 1.5 mm | 2.5 mm | 21 mm |
| Concrete | 2.30 | 15 mm | 30 mm | 62 mm |
| Water | 1.00 | 38 mm | 60 mm | 180 mm |
| Glass (barium) | 3.50 | 5 mm | 10 mm | — |
| Barytes concrete | 3.50 | 8 mm | 15 mm | 40 mm |
| Aluminum | 2.70 | 20 mm | 35 mm | — |

### Tenth-Value Layers (TVL) — Co-60 Gamma

| Material | TVL (mm) | Practical Thickness for Shielding |
|----------|----------|----------------------------------|
| Lead | 41 | 50 mm for therapy rooms |
| Steel | 70 | 80 mm for industrial radiography |
| Concrete | 200 | 250 mm for Co-60, 150 mm for Cs-137 |

### Radiation Characteristics by Type

| Radiation | Mass | Charge | Range in Air | Range in Tissue | Stopped By | Relative Hazard |
|-----------|------|--------|-------------|----------------|-----------|----------------|
| Alpha (α) | 4 amu | +2 | 3-7 cm | 40-80 μm | Sheet of paper, outer skin | Internal hazard only (ingestion, inhalation); external: stopped by skin |
| Beta (β) | 0 amu | -1 | 0.5-3 m | 1-5 mm | 3-5 mm plastic or glass | Skin burns, eye damage; bremsstrahlung X-rays if stopped in lead (use plastic first) |
| Gamma (γ) | 0 | 0 | Hundreds of meters | Passes through | Dense materials (Pb, concrete); exponential attenuation | External whole-body hazard; penetrates deeply |
| X-ray | 0 | 0 | Tens of meters | Passes through | Dense materials (Pb, concrete) | Same as gamma; lower energy = more easily shielded |
| Neutron (n) | 1 amu | 0 | Tens of meters | Passes through | Hydrogenous materials (water, polyethylene, concrete) | Highly penetrating; causes secondary gamma; most damaging per unit dose |

### Common Radionuclides

| Nuclide | Half-Life | Emission | Energy (MeV) | Primary Use | HVL (Pb) |
|---------|-----------|----------|-------------|-------------|----------|
| Cs-137 | 30.1 yr | Beta, Gamma | 0.662 | Calibration source, industrial radiography | 6.5 mm |
| Co-60 | 5.27 yr | Beta, Gamma | 1.173, 1.332 | Industrial radiography, sterilization | 12.5 mm |
| Am-241 | 432 yr | Alpha, Gamma | 0.060 | Smoke detectors, calibration | 0.12 mm |
| I-131 | 8.02 days | Beta, Gamma | 0.364 (γ) | Medical diagnosis/treatment (thyroid) | 2.4 mm |
| Ra-226 | 1,600 yr | Alpha, Gamma | 0.186 (γ) | Historical luminous paint, radon source | 12 mm |
| Rn-222 | 3.82 days | Alpha | 5.49 | Radon gas (uranium decay product) | N/A (gas) |
| Sr-90 / Y-90 | 28.8 yr / 64 hr | Beta | 0.546 / 2.28 | Radioisotope thermoelectric generators (RTG) | Plastic 5 mm |
| Pu-239 | 24,100 yr | Alpha | 5.15 | Nuclear fuel, weapons | Paper (external hazard only if inhaled/ingested) |

### Biological Effects by Dose

| Dose (Sv) | Acute Whole-Body Effect | Onset | Prognosis |
|-----------|------------------------|-------|-----------|
| 0-0.25 | No detectable clinical effects | — | No immediate illness; increased long-term cancer risk |
| 0.25-1.0 | Transient minor blood count changes | Hours-days | Full recovery expected; no acute symptoms in most people |
| 1.0-3.0 | Mild to moderate acute radiation syndrome (ARS): nausea, vomiting, fatigue, reduced blood counts | 2-6 hr | Most survive with supportive care; 5-50% mortality without treatment |
| 3.0-6.0 | Severe ARS: hair loss, hemorrhage, infection, severe blood count depression | 1-4 hr | 50-90% mortality without intensive medical care |
| 6.0-10.0 | Very severe ARS: cardiovascular and CNS involvement | 10-60 min | >95% mortality; survival rare even with best care |
| >10.0 | Acute CNS syndrome: convulsions, coma | Minutes | 100% mortality within days |

## Scaling Notes

- **Basic awareness**: Training for workers near radiation sources. Know the trefoil symbol, stay out of posted areas, report suspected exposures. Zero equipment needed. Appropriate for community with no radiation sources.
- **X-ray room safety**: Shielded room, personal dosimetry, calibrated survey meter, posted warning signs. Serves a medical facility performing diagnostic X-rays. One radiation safety officer. Shielding: 1.5-2 mm Pb equivalent walls, lead-lined door, lead glass window.
- **Industrial radiography safety**: Transport container (lead or depleted uranium shielding, 50-100 kg), collimated source, remote handling tools (1-2 m tongs), exclusion area (30+ m radius during exposure), radiation survey meter. Higher energy sources (Co-60, Ir-192) require substantially more shielding.
- **Semiconductor ion implantation safety**: Beryllium window shielding, interlocked enclosure, toxic gas handling for dopant hydrides (AsH₃, PH₃ — see [chemical-safety](chemical-safety.md)), source change procedures. Requires integration with fab safety systems.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Survey meter reads high in "safe" area | Shielding gap, inadequate thickness, leakage through joints | Survey walls systematically to locate gap; add shielding; seal joints with lead wool or overlapping lead sheet |
| Dosimeter reading unexpectedly high | Improper wear position, left near source when worker absent, badge damage | Investigate work history; compare with co-worker readings; issue replacement dosimeter |
| High background readings | Natural radon, contaminated equipment, cosmic ray increase at altitude | Measure radon separately; decontaminate equipment; compare with historical background data |
| GM counter saturates (reads zero in high field) | Pulse rate exceeds counter dead time, instrument overload | Reduce source distance or use lower-sensitivity instrument (ionization chamber); never assume "zero" means "no radiation" |
| Radioactive spill not cleaning up | Contamination chemically bound to surface, porous material absorption | Use appropriate decontamination agent (chelator for metals, acid for alkaline contaminants); replace porous surfaces if necessary |

## Safety

> **WARNING**: Ionizing radiation is invisible, odorless, and tasteless. You cannot sense it. Damage is cumulative and often irreversible. Radiation safety rules are written in blood — every limit exists because someone was injured.

- **Time, distance, shielding**: The three controls. Reduce time near the source. Maximize distance (dose rate ∝ 1/d²). Interpose shielding. Example: doubling distance from source reduces dose by 75%. Spending half the time reduces dose by 50%. Both together reduce dose by 87.5%.
- **Pregnancy and radiation**: The developing embryo/fetus is extremely radiation-sensitive, especially during organogenesis (weeks 3-12). Declared pregnant workers must not exceed 1 mSv to the fetus during the entire gestation period. Lead aprons (0.5 mm Pb) reduce fetal dose by 50-75% for diagnostic X-ray energies.
- **Radon**: Naturally occurring radioactive gas from uranium decay in soil and rock. Second leading cause of lung cancer after smoking. Accumulates in basements and enclosed ground-level spaces. Action level: 148 Bq/m³ (4 pCi/L). Mitigation: sub-slab ventilation, increased air exchange, sealing foundation cracks.
- **Contamination vs. irradiation**: External irradiation (standing near a source) does not make a person radioactive. The person received a dose but is not contaminated. Contamination (radioactive material on skin or clothing, or inside the body) means the person is continuously being irradiated. Decontamination removes the source of ongoing exposure.
- **Bremsstrahlung production**: Stopping high-energy beta particles with lead produces bremsstrahlung X-rays. Always shield beta emitters with plastic first (stops betas without producing X-rays), then add lead if needed for any secondary X-rays produced.

## Quality Control

- **Survey meter calibration**: Calibrate annually (or after repair) using a traceable reference source. Verify response at two points on each scale. Accuracy must be within ±20% of true value. Perform daily check with a check source before use — meter must read within ±10% of expected check source value.
- **Dosimetry accuracy**: Film badge and TLD systems must be accredited (or self-calibrated against a known standard). Overall accuracy: ±30% at 95% confidence interval for photon doses above 0.2 mSv. Below 0.2 mSv, results are reported as "minimum detectable level" (MDL).
- **Shielding integrity**: Survey new installations with calibrated meter before first use. Re-survey annually or after any modification. Document all survey results with: date, instrument serial number, calibration due date, locations measured, readings, and investigator name.
- **Leak testing sealed sources**: Wipe-test sealed radioactive sources (e.g., calibration check sources) quarterly with filter paper. Count wipe with GM counter or liquid scintillation counter. Activity on wipe must be <185 Bq (5 nCi). If above limit, source is leaking — remove from use, isolate, and decontaminate.
- **Record keeping**: Lifetime dose records for each occupationally exposed worker. Exposure records retained for duration of employment + 30 years. Survey records for each radiation area maintained indefinitely.

## Variations and Alternatives

### Shielding Materials Comparison

| Material | Cost | Availability | Best Application | Limitation |
|----------|------|-------------|-----------------|------------|
| Lead | High | Requires smelting | X-ray rooms, thin shields | Toxic (Pb), heavy, soft |
| Steel | Medium | Widely available | Structural shielding, radiography | 3× thickness of lead needed |
| Concrete | Low | Widely available | Room walls, bunkers | Thick (15-30 cm), heavy, fixed |
| Barytes concrete | Medium | Barite mining needed | When space is limited | 40% thinner than ordinary concrete |
| Water | Very low | Everywhere | Temporary shielding, storage pools | No structural strength, evaporates |
| Tungsten | Very high | Specialized mining | Compact shields, collimators | Expensive, difficult to machine |

### Detection Methods by Radiation Type

| Detector | Detects | Energy Range | Sensitivity | Response Time | Cost |
|----------|---------|-------------|-------------|--------------|------|
| Geiger-Müller tube | β, γ, X-ray | >30 keV | High (individual particles) | 0.1-1 ms | Low |
| Ionization chamber | γ, X-ray | >10 keV | Moderate | ms | Medium |
| Scintillation (NaI) | γ, X-ray | >30 keV | Very high | μs | High |
| Film badge | β, γ, X-ray | >20 keV | Low (cumulative) | Weeks (processing) | Low |
| TLD (LiF) | β, γ, X-ray, neutron | >10 keV | Moderate | Weeks (processing) | Medium |
| Semiconductor (HPGe) | γ | >40 keV | Highest | μs | Very high |

## References

- [Chemical Safety](chemical-safety.md) — semiconductor process gas safety (arsine, phosphine) used in ion implantation
- [Emergency Response](emergency-response.md) — radiation emergency procedures, contamination events
- [PPE](ppe.md) — lead aprons for medical radiation protection
- [Occupational Health](../health/occupational-health.md) — dose limits, medical surveillance for radiation workers
- [Diagnostics](../health/diagnostics.md) — X-ray imaging safety requirements
- [Measurement](../measurement/index.md) — radiation detection instruments, calibration
- [Electronics](../electronics/index.md) — Geiger-Müller tubes, scintillation detectors, dosimetry electronics
- [Metals](../metals/index.md) — lead production for shielding

---

*Part of the [Bootciv Tech Tree](../index.md) • [EHS](./index.md) • [All Domains](../index.md)*
