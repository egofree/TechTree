# Crew Training

> **Node ID**: human-spaceflight.crew-training
> **Domain**: [Human Spaceflight](./index.md)
> **Dependencies**: `computing`, `aerospace.aviation`
> **Enables**: *(populated in integration wave)*
> **Timeline**: Years 60+
> **Outputs**: trained_crew
> **Critical**: No

A trained crew is the most complex and most expensive component of any human spaceflight programme. An ISS expedition crew member requires two to three years of training before launch, logging over 2,000 hours in simulators, 300+ hours in the Neutral Buoyancy Laboratory pool, and months in analog environments. The training infrastructure — motion-base simulators, VR laboratories, underwater mockup facilities, and isolation habitats — represents an investment comparable to the flight hardware itself, and must be sustained continuously because the next crew is always in the pipeline.

This article covers three process areas: [simulators](./crew-training.simulators.md) — motion-base and VR systems for spacecraft procedures, [neutral buoyancy](./crew-training.neutral-buoyancy.md) — the NBL pool and EVA training methodology, and [analog environments](./crew-training.analog-environments.md) — ground-based isolation and mission simulation campaigns.

## Overview

The objective of crew training is to ensure that every crew member can execute every assigned task — nominal and contingency — under the conditions they will encounter in flight: high-g launch, microgravity adaptation, time pressure, sleep deprivation, and equipment failure. The training programme is built around the principle of graduated fidelity: start with classroom theory, progress through part-task trainers, advance to full-fidelity integrated simulators, and culminate in analog environment campaigns.

### Training Timeline (ISS Expedition Crew)

| Phase | Duration (Months) | Focus | Hours/Week | Location |
|-------|-------------------|-------|------------|----------|
| Basic training | 0-6 | Spaceflight fundamentals, physical conditioning | 40-50 | JSC Star City / ESA EAC |
| International training | 6-12 | ISS systems (US, Russian, Japanese, ESA segments) | 45-50 | Multi-site |
| Role-specific training | 12-18 | Assigned role: commander, flight engineer, scientist | 50-55 | JSC + partner sites |
| Simulations and exams | 18-24 | Integrated sims, emergency drills, certification exams | 55-60 | JSC Star City |
| Final preparation | 24-30 | Crew quarantine, final sims, medical checks | 40-45 | Baikonur / KSC |
| **Total** | **24-30** | -- | -- | -- |

### Hour Breakdown by Training Type

| Training Type | Total Hours (30-month flow) | Percentage |
|---------------|---------------------------|------------|
| Spacecraft systems (classroom + part-task) | 500-600 | 20-25% |
| Full-fidelity simulator | 400-500 | 15-20% |
| EVA / NBL training | 250-350 | 10-15% |
| Robotics (SSRMS, ERA operations) | 150-200 | 5-8% |
| Russian language (non-Russian crew) | 300-400 | 12-15% |
| Physical fitness | 200-300 | 8-10% |
| Science payload training | 200-400 | 8-15% |
| Analog / isolation campaigns | 100-200 | 4-8% |
| Medical and survival | 80-120 | 3-5% |
| **Total** | **2,500-3,000** | 100% |

## Simulators

Spacecraft simulators span a fidelity spectrum from software-only part-task trainers to full-motion cockpit replicas with hydraulic hexapod platforms. The Space Mission Simulator (SMS) complex at JSC and the equivalent facilities at Star City are the primary training venues.

### Simulator Fidelity Tiers

| Tier | Description | Motion | Visual | Examples | Cost Range |
|------|-------------|--------|--------|----------|------------|
| Part-task trainer | Single system, desktop or mockup panel | None | 2D screen | Soyuz docking display trainer | $50K-500K |
| Fixed-base cockpit | Full cockpit panel, no motion | None | Multi-screen | Crew Dragon cockpit trainer | $1-5M |
| Motion-base cockpit | Full cockpit + 6-DOF hexapod | 6-DOF hydraulic | Dome projection | Shuttle MBS | $5-20M |
| Full mission simulator | Integrated cockpit + ground ops + failure injection | 6-DOF + vibration | 360 dome | SMS complex | $20-100M |
| VR immersive | Headset + hand tracking + haptics | None (visual only) | VR HMD | NASA Apache VR EVA trainer | $10K-100K |

### Motion-Base Platform Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Degrees of freedom | 6 (surge, sway, heave, roll, pitch, yaw) | Hexapod configuration |
| Maximum payload | 5,000-15,000 kg | Cockuit + crew + equipment |
| Peak acceleration | +/- 1.5 g per axis | Launch and entry simulation |
| Sustained acceleration | +/- 0.5 g | Vibration and buffet |
| Position resolution | 0.1 mm | Fine cueing |
| Latency | < 25 ms | Motion cueing algorithm |
| Stroke length | 300-600 mm per actuator | Determines max heave |
| Actuator type | Hydraulic or electric screw jack | Hydraulic for large payloads |

### Spacecraft Trainer Inventory

| Trainer | Vehicle | Location | Motion | Crew Size | Status |
|---------|---------|----------|--------|-----------|--------|
| Crew Dragon Cockpit Trainer | Dragon 2 | SpaceX Hawthorne | Fixed | 4-7 | Active |
| Starliner Trainer | CST-100 | JSC Building 5 | Fixed + partial | 4-7 | Active |
| Soyuz TMA Simulator | Soyuz MS | Star City | Fixed | 3 | Active |
| Orion Cockpit Trainer | Orion MPCV | JSC Building 5 | Motion-base | 4 | Development |
| ISS US Lab Trainer | ISS Destiny | JSC Building 5 | Fixed | varies | Active |
| SSRMS Robotics Trainer | ISS Canadarm2 | JSC Building 5 | Fixed + VR | 1-2 | Active |
| Commercial Crew Transport Trainers | Dragon/Starliner | Multiple | Mixed | 4-7 | Active |

### VR Training Applications

| Application | Headset | Purpose | Training Hours |
|-------------|---------|---------|----------------|
| EVA pre-briefing | HTC Vive Pro / Varjo XR-3 | Walkthrough of EVA worksite and procedures | 2-4 hr/EVA |
| ISS configuration familiarisation | Oculus Quest 2 | Module interior layout and equipment location | 10-20 hr |
| Robotics operations | Varjo XR-3 + hand tracking | SSRMS capture and berthing practice | 20-40 hr |
| Emergency egress | HTC Vive Pro | Fire, depress, ammonia leak response | 8-16 hr |
| Lunar surface ops | Varjo XR-3 | Artemis EVA site reconnaissance and traverse planning | 10-30 hr |

## Neutral Buoyancy

The Neutral Buoyancy Laboratory (NBL) at NASA's Sonny Carter Training Facility is the gold standard for EVA training. A suited astronaut in the NBL pool experiences a close approximation of weightlessness — buoyancy is tuned to neutral, and the suit mass is balanced so that the net force on the body is nearly zero.

### NBL Pool Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Length | 71.6 m (235 ft) | Rectangular |
| Width | 41.1 m (135 ft) | Rectangular |
| Depth | 12.3 m (40 ft) | Uniform depth |
| Volume | 23.5 million gallons (62.2M litres) | Indoor heated pool |
| Temperature | 28-32°C (82-90°F) | Controlled for suit cooling loop efficiency |
| Filtration turnover | 4 hours full exchange | Particle filtration + chlorination |

### NBL Mockup Inventory

| Mockup | Description | Mass (kg) | Purpose |
|--------|-------------|-----------|---------|
| ISS US Lab (Destiny) | Full-scale exterior, working ORU interfaces | 12,000 | EVA worksite training |
| ISS Node 2 (Harmony) | Full-scale exterior, docking port access | 6,000 | Node installation EVA |
| ISS Truss segments | S0, S1, P1, S3/S4, P3/P4 truss sections | 4,000-8,000 | Truss assembly EVA |
| SSRMS (Canadarm2) | Sub-scale functional replica | 3,000 | Robotics + EVA coordination |
| Solar Alpha Rotary Joint | Full-scale functional model | 2,000 | SARJ repair training |
| Orion crew module | Full-scale exterior | 8,000 | Artemis EVA worksite |
| Hubble Space Telescope | Full-scale exterior (retired) | 11,000 | HST servicing missions (historical) |

### NBL Training Session Protocol

| Phase | Duration | Activity | Personnel |
|-------|----------|----------|-----------|
| Suit don and checkout | 1.0 hr | IV-style donning, pressure checks | 3-4 suit techs |
| Pre-dive brief | 0.5 hr | Timeline review, comm check | Full team |
| Underwater session | 6.0 hr | EVA task rehearsal at 1:1 time fidelity | 4 divers, 1 test director, 2 comms |
| Post-dive debrief | 0.5 hr | Timeline compliance, task completion | Full team |
| Suit doff and medical | 1.0 hr | Suit removal, post-dive medical check | 3-4 suit techs + flight surgeon |
| **Total session** | **9.0 hr** | -- | **12-15 support staff** |

### Suit Configurations for NBL

| Suit | Type | Pressure (nominal) | Pressure (training) | Mass (kg) |
|------|------|-------------------|--------------------|----|
| EMU (Extravehicular Mobility Unit) | Current NASA EVA suit | 4.3 psi (29.6 kPa) | 4.0-4.3 psi | 127 |
| xEMU (Exploration EVA) | Next-gen Artemis suit | 4.3 psi (29.6 kPa) | 4.3 psi | ~ 80 (planned) |
| Orlan-M (Russian) | Current Roscosmos EVA suit | 4.0 psi (27.6 kPa) | 3.9-4.0 psi | 110 |

## Analog Environments

Analog environments are ground-based facilities that simulate one or more aspects of a long-duration space mission: isolation, confinement, communication delay, limited resources, psychological stress, and harsh external conditions. They are the only ethical way to study crew psychology and team dynamics over mission durations that cannot be achieved on the ISS.

### Major Analog Facilities

| Facility | Operator | Location | Duration Range | Crew Size | Focus |
|----------|----------|----------|---------------|-----------|-------|
| HERA (Human Exploration Research Analog) | NASA | JSC Houston | 14-45 days | 4 | Isolation, psychology, communication delay |
| NEEMO (NASA Extreme Environment Mission Ops) | NASA | Aquarius Reef Base, Florida Keys | 7-14 days | 4-6 | Underwater EVA, saturation diving analog |
| SIRIUS (Scientific International Research In Unique terrestrial Station) | IBMP/NEK | Moscow, Russia | 17 days - 8 months | 4-6 | Lunar mission simulation, isolation |
| Haughton-Mars Project (HMP) | SETI / Mars Institute | Devon Island, Canadian Arctic | 2-12 weeks | 4-12 | Polar desert geology, Mars surface ops |
| Concordia | ESA/IPEV/PNRA | Dome C, Antarctica | 9-12 months | 9-13 | Winter-over isolation, extreme environment |
| HI-SEAS (Hawaii Space Exploration Analog) | University of Hawaii | Mauna Loa, Hawaii | 4-12 months | 6 | Mars surface habitat simulation |
| MARS500 | ESA/IBMP | IBMP Moscow | 105-520 days | 6 | Mars transit isolation (completed 2011) |
| Antarctica stations (multiple) | Various | Various | 6-14 months | 10-200 | Winter-over psychology, medical isolation |

### HERA Facility Specifications

| Parameter | Value |
|-----------|-------|
| Total volume | 636 ft³ (18.0 m³) across 3 floors |
| Floors | 3 (loft, main deck, lower deck) |
| Crew size | 4 |
| Mission duration | 14, 30, 45 days |
| Communication delay | 0-5 minutes each way (simulated) |
| External view | None (light-tight) |
| Exercise equipment | Cycle ergometer, resistive bands |

### SIRIUS Programme Phases

| Phase | Duration | Crew | Launch Date | Simulated Scenario |
|-------|----------|------|-------------|-------------------|
| SIRIUS-17 | 17 days | 4 | Nov 2017 | Lunar orbital sortie |
| SIRIUS-19 | 4 months | 6 | Mar 2019 | Lunar orbital + surface stay |
| SIRIUS-21 | 8 months | 6 | Nov 2021 | Lunar surface mission with EVAs |
| SIRIUS-23 (planned) | 12 months | 4-6 | 2023+ | Full Mars transit analog |

### Analog Environment Psychological Data

| Metric | Baseline | HERA 45-day | NEEMO 14-day | SIRIUS 4-month | MARS500 520-day |
|--------|----------|-------------|-------------|----------------|-----------------|
| Crew cohesion (post-mission survey) | 8.5/10 | 7.5-8.0 | 7.8-8.2 | 6.5-7.5 | 4.5-6.0 |
| Sleep efficiency decline | 0% | 5-10% | 3-5% | 10-15% | 15-25% |
| Cognitive reaction time slowing | 0% | 3-5% | 2-4% | 8-12% | 15-20% |
| Depression inventory elevation | -- | +2-3 points | +1-2 | +3-5 | +5-8 |
| Post-mission recovery time | -- | 1-2 weeks | 3-5 days | 2-4 weeks | 3-6 months |

## Certification and Examination

Before assignment to a flight, each crew member must pass a series of certification exams and evaluations:

| Certification | Format | Duration | Pass Threshold | Retake Policy |
|---------------|--------|----------|----------------|---------------|
| ISS systems exam | Written + oral | 4-6 hr total | 80% | One retake, then reassignment |
| Emergency procedures eval | Simulated scenario | 2-4 hr | No critical errors | Immediate retraining |
| EVA certification | NBL evaluation | 6 hr underwater | All tasks completed | Retraining + re-eval |
| Robotics proficiency | Part-task + integrated | 3-4 hr | 85% | Retraining required |
| Survival training (water/land) | Field exercise | 1-2 days | Pass/fail | Mandatory pass |
| Medical certification | Flight surgeon review | 2 hr | Class I medical | Waiver process |

## Key Parameters Summary

| Parameter | Value | Source |
|-----------|-------|--------|
| ISS crew training duration | 24-30 months | NASA ISS Training Plan |
| Total training hours (ISS crew) | 2,500-3,000 | JSC training data |
| NBL pool volume | 23.5 million gallons (62.2M litres) | NASA Sonny Carter Facility |
| NBL pool dimensions | 71.6 x 41.1 x 12.3 m | NASA NBL spec |
| NBL session duration (underwater) | 6 hours | NBL standard ops |
| NBL support team per session | 12-15 personnel | NBL operations |
| EMU suit mass (NBL config) | 127 kg | NASA EMU spec |
| Motion-base hexapod payload | 5,000-15,000 kg | Stewart platform spec |
| VR headset resolution (Varjo XR-3) | 2,800 x 2,800 per eye | Varjo product spec |
| HERA habitat volume | 18.0 m³ | NASA HERA spec |
| MARS500 mission duration | 520 days | IBMP/ESA final report |
| Mars transit analog comm delay | Up to 20 minutes each way | Speed of light Earth-Mars |
| Training programme annual cost | ~ $100-150M/year | NASA budget estimates |
| Crew certification pass rate | ~ 85-90% first attempt | JSC training records |

## Survival Training

Before flight assignment, all crew members complete survival training for contingency landings. The landing site of a crewed spacecraft cannot be guaranteed — a ballistic reentry or off-nominal descent can place the crew in ocean, desert, tundra, or forest for hours to days before recovery.

### Survival Training Environments

| Environment | Location | Duration | Skills Trained | Spacecraft Scenario |
|-------------|----------|----------|---------------|---------------------|
| Water egress | Black Sea / JSC pool | 1-2 days | Suit flotation, raft deployment, helo hoist | Soyuz water landing, Dragon splashdown |
| Winter survival | Russian taiga / Alaska | 2-3 days | Shelter, fire, signalling, food/water | Soyuz winter landing contingency |
| Desert survival | Nevada / Kazakh steppe | 1-2 days | Shade shelter, water conservation, signalling | Off-nominal dry landing |
| Tropical survival | Florida Everglades | 1-2 days | Insect/injury management, water procurement | Equatorial landing contingency |

### Survival Kit Contents

| Category | Items | Mass (kg) |
|----------|-------|-----------|
| Water and food | 2 L water, 6 x 500 kcal rations, water purification tablets | 3.5 |
| Shelter and fire | Emergency blanket, matches, fire starter, saw knife | 1.2 |
| Signalling | Strobe light, smoke flares, signal mirror, dye marker | 0.8 |
| Medical | First aid kit, trauma bandage, analgesics | 1.0 |
| Tools | Multi-tool, para cord, machete | 1.5 |
| Communications | Emergency beacon (406 MHz), VHF radio | 1.0 |
| **Total** | -- | **9.0** |

## Language and Cross-Cultural Training

ISS crew members from partner agencies must train at each other's facilities and operate in each other's modules. Language proficiency and cultural awareness are mission-critical skills.

### Language Training Requirements

| Crew Nationality | Required Languages | Target Proficiency | Training Hours |
|-----------------|-------------------|-------------------|----------------|
| NASA (US) | Russian | ILR Level 3 (Professional) | 300-500 |
| Roscosmos (Russia) | English | ILR Level 3 (Professional) | 300-500 |
| ESA (Europe) | English + Russian | ILR Level 3 both | 500-800 |
| JAXA (Japan) | English + Russian | ILR Level 3 both | 500-800 |
| CSA (Canada) | English + Russian (basic) | ILR Level 2-3 | 200-400 |

## Prerequisites

- [Computing](../computing/index.md) — simulation software, VR rendering, data processing
- [Aviation](../aerospace/index.md) — flight simulator heritage, crew resource management

## See Also

- [Space Medicine](./space-medicine.md) — crew selection standards and medical monitoring
- [Space Suits](./space-suits.md) — EMU suits used in NBL training
- [EVA](./eva.md) — procedures rehearsed in neutral buoyancy
- [Space Stations](./space-stations.md) — mockup modules in the NBL
- [Crewed Spacecraft](./crewed-spacecraft.md) — simulator cockpit fidelity

- [Space Medicine](./space-medicine.md) — crew selection standards and medical monitoring
- [Space Suits](./space-suits.md) — EMU suits used in NBL training
- [EVA](./eva.md) — procedures rehearsed in neutral buoyancy
- [Space Stations](./space-stations.md) — mockup modules in the NBL
- [Crewed Spacecraft](./crewed-spacecraft.md) — simulator cockpit fidelity
