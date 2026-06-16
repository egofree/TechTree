# Radiation Protection

> **Node ID**: human-spaceflight.radiation-protection
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `ehs.radiation-safety`, `energy.nuclear-fission`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: radiation_protection
> **Critical**: Yes

Radiation is the single greatest obstacle to long-duration human spaceflight beyond low Earth orbit. The space radiation environment consists of three distinct sources, each with different energies, particle types, and shielding requirements: the Van Allen belts trapped particle populations, solar particle events (SPE) from coronal mass ejections, and galactic cosmic rays (GCR) from supernovae and active galactic nuclei beyond the heliosphere. Together they deliver a dose that can exceed 300 mSv on a single Mars transit and a lethal spike of several sieverts in hours during an extreme SPE.

This article covers two process areas: [storm shelters](./radiation-protection.storm-shelters.md) — the passive shielding architecture that protects crew during solar storms, and [dosimetry and monitoring](./radiation-protection.dosimetry-monitoring.md) — the suite of active and passive detectors that measure the dose as it accumulates.

## Overview

Radiation shielding in space is fundamentally different from terrestrial nuclear shielding. On Earth, the dominant concern is gamma and neutron radiation from reactor cores, handled with dense materials like lead and concrete. In space, the dominant threat is charged particles — protons and heavy ions — at energies from tens of MeV to beyond 10 GeV per nucleon. Paradoxically, dense shielding can make the problem worse: a high-energy heavy ion (e.g., iron-56 at 1 GeV/n) striking a dense nucleus produces a shower of secondary neutrons and charged fragments that deposit more dose than the primary particle would have. The optimal shielding material is therefore hydrogen-rich, not dense.

### The Three Radiation Sources

| Source | Particle Type | Energy Range | Dose Rate (LEO) | Dose Rate (Mars transit) | Time Structure |
|--------|--------------|-------------|-----------------|-------------------------|----------------|
| Trapped belts | Protons, electrons | 0.1-400 MeV (p), 0.1-10 MeV (e) | 0.5-1.0 mSv/day | 0 (outside belts) | Continuous (in belts) |
| SPE (solar storms) | Protons, alpha | 10-500 MeV | 0-50 mSv/event | 0-1,000+ mSv/event | Spikes, hours to days |
| GCR (galactic cosmic) | Protons, heavy ions | 0.1-10+ GeV/n | 0.3-0.6 mSv/day | 1.0-1.8 mSv/day | Continuous, modulated |

### Dose Comparison

| Scenario | Duration | Total Dose (mSv) | Equivalent (chest CT scans) |
|----------|----------|-----------------|-----------------------------|
| Earth surface background | 6 months | 1-3 | 0.1-0.3 |
| ISS (LEO, 51.6 deg orbit) | 6 months | 50-100 | 15-30 |
| ISS (LEO, equatorial) | 6 months | 30-60 | 10-20 |
| Moon surface (Apollo) | 12 days | 10-12 | 3-4 |
| Mars transit (one-way) | 6 months | 300-500 | 90-150 |
| Mars surface (18 months) | 18 months | 200-400 | 60-120 |
| Extreme SPE (e.g., Carrington-class) | 1-2 days | 1,000-10,000+ | 300-3,000 |

## Storm Shelters

A storm shelter is a compact, heavily shielded volume within the spacecraft where the crew retreats during a major solar particle event. The design principle is simple: pile mass between the crew and the radiation source. The key metric is areal density — grams of shielding material per square centimetre of projected area.

### Shielding Materials Comparison

| Material | Density (g/cm³) | H atom fraction | 5 g/cm² thickness (cm) | SPE attenuation (200 MeV p) | GCR attenuation |
|----------|----------------|----------------|----------------------|---------------------------|-----------------|
| Liquid hydrogen | 0.071 | 100% | 70.4 | Best | Best |
| Water | 1.00 | 67% | 5.0 | Good | Good |
| Polyethylene (CH₂) | 0.93 | 66% | 5.4 | Good | Good |
| Lithium hydride | 0.82 | 50% | 6.1 | Good | Good |
| Aluminium | 2.70 | 0% | 1.9 | Poor (secondaries) | Poor |
| Lead | 11.34 | 0% | 0.4 | Worst (bremsstrahlung) | Worst |

### Areal Density Design Points

| Areal Density (g/cm²) | SPE Dose Reduction | GCR Dose Reduction | Material Required (water) |
|----------------------|-------------------|-------------------|---------------------------|
| 1 | ~ 50% | ~ 5% | 1 cm layer |
| 5 | ~ 90% | ~ 15-20% | 5 cm layer |
| 10 | ~ 98% | ~ 25-30% | 10 cm layer |
| 20 | ~ 99.5% | ~ 35-40% | 20 cm layer |
| 50 | ~ 99.9% | ~ 50-55% | 50 cm layer |

### Storm Shelter Configurations

The mass cost of a dedicated storm shelter is prohibitive if the shielding is carried as dead weight. Instead, the standard approach is configurational shielding: arranging existing consumables (water, food, waste, propellant) around a central refuge volume.

| Configuration | Description | Effective Areal Density | Mass Cost |
|---------------|-------------|------------------------|-----------|
| Water wall | Water tanks lining shelter walls | 10-25 g/cm² | Zero (water is already carried) |
| Food/faecal wall | Vacuum-packed food and waste brickettes | 5-15 g/cm² | Zero (consumables already carried) |
| Polyethylene liner | Dedicated HDPE panels | 5-10 g/cm² | 500-2,000 kg per shelter |
| Propellant surround | LH2/LOX tanks surrounding crew cabin | 20-50 g/cm² | Zero (propellant is already carried) |
| Regolith berm (surface) | Bagged Martian/Lunar regolith over habitat | 50-100+ g/cm² | Labor cost, not launch mass |

### SPE Timeline and Response Protocol

| Phase | Duration | Action | Dose Accumulated |
|-------|----------|--------|-----------------|
| Detection | Minutes | SEP sensor triggers alarm, crew alerted | < 1 mSv |
| Retreat | 15-30 min | Crew enters shelter, secures hatch | 1-5 mSv |
| SPE peak | 4-12 hours | Crew remains in shelter, monitoring | 10-100 mSv (inside) |
| SPE decline | 1-3 days | Crew exits when rate < 1 mSv/hr | Cumulative inside |
| Total (with shelter) | 3-5 days | -- | 20-200 mSv |
| Total (without shelter) | 3-5 days | -- | 1,000-10,000 mSv |

## Dosimetry and Monitoring

Radiation dose in space is measured by a layered system of active and passive detectors. Active detectors provide real-time readout for operational decisions; passive detectors provide the dose-of-record for career tracking.

### Detector Types

| Detector | Type | Measures | Range (LET) | Readout | Use |
|----------|------|----------|-------------|---------|-----|
| OSLiD (optically stimulated luminescence) | Passive | Gamma, charged particle dose | 0.2-10 keV/µm | Post-flight lab read | Personal dose-of-record |
| CR-39 PNTD | Passive | High-LET charge spectroscopy | 10-1,000 keV/µm | Post-flight etch + track analysis | Heavy ion and neutron dose |
| TLD-100 (LiF thermoluminescent) | Passive | Gamma, low-LET dose | 0.2-10 keV/µm | Post-flight heat read | Skin and depth dose |
| TEPC (tissue-equivalent proportional counter) | Active | Lineal energy, dose equivalent | 0.3-1,000 keV/µm | Real-time | Area monitoring, SPE alert |
| REM (radiation environment monitor) | Active | Charged particle flux, spectrum | 0.1-100 MeV | Real-time, 1-sec cadence | External environment |
| Charged Particle Directional Spectrometer | Active | Directional particle flux | 0.1-1,000 MeV | Real-time | Habitat dose mapping |

### Personal Dosimetry Suite

Each crew member wears a personal dosimeter package containing multiple detector elements:

| Element | Material | Purpose | Readout Frequency |
|---------|----------|---------|-------------------|
| OSL badge | Al2O3:C | Photon + charged particle dose-of-record | Weekly read + post-flight |
| CR-39 chip | Allyl diglycol carbonate | Heavy ion and neutron dose | Post-flight |
| TLD chip (deep) | LiF:Mg,Ti | Depth dose at 3 cm tissue depth | Monthly |
| TLD chip (shallow) | LiF:Mg,Ti | Skin dose at 0.007 cm | Monthly |
| Electronic dosimeter | Si PIN diode | Real-time dose rate alarm | Continuous |

### Area Monitoring Network

| Location on ISS | Detector | Purpose |
|----------------|----------|---------|
| Service Module (Zvezda) | TEPC | Crew sleep area dose |
| US Lab (Destiny) | TEPC + REM | Primary work area dose |
| Node 2 (Harmony) | REM | Docking/habitat area |
| Columbus module | TEPC | ESA lab area |
| Kibo module | REM | JAXA lab area |
| External (on truss) | REM + CPDS | Unshielded environment baseline |

## NASA Radiation Dose Limits

NASA's Permissible Exposure Limits (PELs) are designed to keep the Risk of Exposure-Induced Death (REID) below 3% at 95% confidence. They are age- and gender-dependent because cancer risk varies with both.

| Career Exposure Limit (mSv) | Age 25 | Age 35 | Age 45 | Age 55 |
|-----------------------------|--------|--------|--------|--------|
| Female | 1,000 | 1,750 | 2,500 | 3,000 |
| Male | 1,500 | 2,500 | 3,250 | 4,000 |

### Organ Dose Limits (30-Day)

| Organ | Limit (mGy-Eq) | Rationale |
|-------|---------------|-----------|
| Eye (lens) | 1,000 | Cataract formation threshold |
| Skin | 1,500 | Erythema threshold |
| Bone marrow | 250 | Acute radiation syndrome |
| Heart | 250 | Cardiovascular damage |
| gonads | 250 | Sterility / hereditary risk |

## Key Parameters Summary

| Parameter | Value | Source |
|-----------|-------|--------|
| ISS 6-month dose | 50-100 mSv | ISS dosimetry data |
| Mars transit dose (one-way) | 300-500 mSv | MSL/RAD measurements |
| Mars surface dose (annual) | 130-230 mSv | MSL/RAD surface data |
| Extreme SPE dose (unshielded) | 1,000-10,000 mSv | Aug 1972, Oct 1989 modelling |
| SPE warning time | 10-60 minutes | Coronagraph detection to particle arrival |
| Storm shelter areal density target | 5-10 g/cm² | NASA HRP recommendation |
| Best shield material (per unit mass) | Liquid hydrogen | NCRP Report 98 |
| Best practical shield material | Water / polyethylene | ISS/Mars architecture studies |
| GCR iron-56 flux | ~ 4 particles/m²/s/sr | CRIS/SAMPEX data |
| Career dose limit (35-y male) | 2,500 mSv | NASA STD-3001 |
| OSLiD sensitivity | 10 µSv - 10 Sv | Landauer InLight spec |
| CR-39 LET range | 5-1,000 keV/µm | Track etch methodology |
| TEPC energy range | 0.3-1,000 keV/µm lineal energy | Far West Technology |

## GCR and the Secondary Radiation Problem

Galactic cosmic rays are the most difficult radiation source to shield against. Unlike SPE protons, which stop at 10-20 g/cm² of water, GCR particles — particularly high-charge, high-energy (HZE) ions like iron-56 — penetrate any practical amount of shielding. Worse, when a GCR nucleus strikes a shielding nucleus, it fragments into secondary particles: neutrons, protons, alpha particles, and lighter ions. These secondaries can deposit more dose than the primary would have, especially inside a large shielded volume.

### Primary vs Secondary Dose Inside Shielding

| Shield Areal Density (g/cm²) | Primary GCR Dose (mSv/day) | Secondary Dose (mSv/day) | Total Dose (mSv/day) | Net Effect |
|------------------------------|---------------------------|-------------------------|---------------------|------------|
| 0 (unshielded) | 1.8 | 0.0 | 1.8 | Baseline |
| 5 (water) | 1.5 | 0.4 | 1.9 | +6% (worse) |
| 10 (water) | 1.2 | 0.6 | 1.8 | 0% (neutral) |
| 20 (water) | 0.8 | 0.7 | 1.5 | -17% |
| 50 (water) | 0.4 | 0.6 | 1.0 | -44% |
| 100 (water) | 0.2 | 0.4 | 0.6 | -67% |
| 20 (aluminium) | 0.8 | 1.2 | 2.0 | +11% (worse!) |

### HZE Ion Contribution to Dose

| Ion | Charge (Z) | Flux (% of GCR) | Dose Contribution (%) | LET (keV/µm in water) |
|-----|-----------|-----------------|----------------------|----------------------|
| Protons (H) | 1 | 85 | 20 | 0.2-1.0 |
| Helium (alpha) | 2 | 12 | 10 | 1.0-4.0 |
| Carbon (C) | 6 | 0.4 | 5 | 10-25 |
| Oxygen (O) | 8 | 0.3 | 7 | 15-35 |
| Silicon (Si) | 14 | 0.1 | 10 | 40-80 |
| Iron (Fe) | 26 | 0.03 | 20 | 100-300 |

## Active Shielding Concepts

Electromagnetic and electrostatic active shielding has been proposed as an alternative to passive mass shielding. These concepts generate magnetic or electric fields that deflect charged particles away from the habitable volume.

| Concept | Field Strength | Mass Estimate | Power | TRL | Status |
|---------|---------------|---------------|-------|-----|--------|
| Superconducting magnetic | 5-10 T at coil | 50-200 tonnes | < 1 kW (cryo) | 2-3 | Research |
| Electrostatic spheres | 100 MV/m | 50-100 tonnes | 1-5 kW | 2 | Conceptual |
| Plasma shielding | 10¹²/cm³ plasma | 10-50 tonnes | 10-100 kW | 1-2 | Theoretical |
| Hybrid (mag + passive) | 1-2 T + 20 g/cm² | 30-80 tonnes | < 5 kW | 2-3 | Study phase |

## Mars Mission Dose Budget

A representative Mars conjunction-class mission (900-day round trip with 500-day surface stay) accrues the following dose:

| Mission Phase | Duration | Dose Rate (mSv/day) | Phase Dose (mSv) | Shielding |
|---------------|----------|--------------------|--------------------|-----------|
| Earth-Mars transit | 180 days | 1.5-1.8 | 270-325 | 20 g/cm² water |
| Mars surface stay | 500 days | 0.3-0.6 | 150-300 | Regolith + atmosphere |
| Mars-Earth transit | 180 days | 1.5-1.8 | 270-325 | 20 g/cm² water |
| SPE exposure (expected) | -- | -- | 50-200 | Storm shelter |
| **Total mission** | **860 days** | -- | **740-1,150** | -- |
| Career limit (35-y male) | -- | -- | 2,500 | -- |
| Margin to limit | -- | -- | ~ 30-40% | -- |

## SPE Detection and Warning

Solar particle events are triggered by coronal mass ejections (CMEs) and solar flares. The particles arrive at Earth 20-60 minutes after the electromagnetic (light/radio) signal, providing a window for crew to retreat to shelter.

| Warning Method | Lead Time | Detection Principle | Reliability |
|---------------|----------|---------------------|-------------|
| GOES X-ray flux | 30-60 min | Soft X-ray flare precedes particle arrival | Moderate (50-70% SPE prediction) |
| Coronagraph CME detection | 30-60 min | Stereo/LASCO CME imaging + propagation model | Good (80% prediction) |
| Neutron monitor (ground level enhancement) | 5-15 min | Ground-level neutron flux increase | Real-time SPE confirmation |
| Onboard charged particle detector | 0-5 min | Direct particle flux measurement | Confirmed (no lead time) |

## ALARA in Spaceflight

The ALARA principle (As Low As Reasonably Achievable) is adapted for spaceflight, where zero exposure is impossible and the total mission dose is a design constraint rather than a safety target.

### ALARA Implementation Hierarchy

| Level | Strategy | Example | Dose Reduction |
|-------|----------|---------|----------------|
| 1. Minimise time | Shorten EVA, rotate crew positions | Limit EVA to 6.5 hr (vs 8 hr max) | Proportional to time |
| 2. Maximise distance | Place sleeping quarters away from hull | Centrally located crew quarters | Inverse square (gamma) |
| 3. Use shielding | Configurational mass around crew | Water wall, food cache surround | 50-90% for SPE |
| 4. Operational planning | Schedule high-dose tasks during low-flux periods | EVA during solar minimum | 20-30% GCR reduction |
| 5. Pharmacological | Radioprotective agents (preclinical) | Amifostine, antioxidants | Unproven in space |

### Solar Cycle and Mission Planning

GCR flux varies with the 11-year solar cycle. During solar maximum, the enhanced solar wind suppresses GCR flux by 30-50% — but SPE frequency is highest. During solar minimum, GCR is at peak but SPE risk is lower.

| Solar Phase | GCR Flux | SPE Frequency | SPE Severity | Optimal Mission Type |
|-------------|----------|---------------|-------------|---------------------|
| Solar minimum (2008-2009 type) | Peak (~1.8 mSv/day) | Low (1-2 major/yr) | Moderate | Short transit, long surface |
| Solar maximum (2014-2015 type) | Reduced (~1.0 mSv/day) | High (5-10 major/yr) | Higher | Requires robust storm shelter |
| Declining phase | Moderate (~1.3 mSv/day) | Moderate | Variable | Balanced risk profile |

## Dosimetry Data Processing Pipeline

The passive dosimetry readout pipeline on returned ISS dosimeters involves multiple laboratory steps:

| Step | Procedure | Output | Turnaround |
|------|-----------|--------|------------|
| 1. Inventory and chain-of-custody | Log returned badges against manifest | Verified dosimeter set | 1 day |
| 2. OSL read | Stimulate Al2O3:C with green laser | Raw luminescence decay curve | 2 hours/badge |
| 3. TLD read | Heat LiF chips to 300°C | Glow curve | 1 hour/chip |
| 4. CR-39 etch | 6.25 N NaOH at 70°C for 6 hours | Etched track pits | 8 hours/batch |
| 5. CR-39 microscopy | Automated track counting and sizing | Track density + LET spectrum | 4 hours/detector |
| 6. Dose calculation | Combine OSL + TLD + CR-39 with transport codes | Total effective dose | 2 days |
| 7. Career tracking | Update individual crew dose ledger | Updated REID estimate | 1 week |

## Prerequisites

- [Radiation Safety](../ehs/index.md) — ALARA principles, dose limits, contamination control
- [Nuclear Fission](../energy/index.md) — radiation physics, shielding material characterisation

## See Also

- [Space Medicine](./space-medicine.md) — health effects of radiation exposure and countermeasures
- [ECLSS](./eclss.md) — water tanks used as configurational shielding
- [Space Stations](./space-stations.md) — habitat modules where shielding is integrated
- [EVA](./eva.md) — suit radiation shielding during extravehicular activity
