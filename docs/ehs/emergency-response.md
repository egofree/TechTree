# Emergency Response

> **Node ID**: ehs.emergency-response
> **Domain**: [Environmental Health & Safety](./index.md)
> **Dependencies**: [`ehs.chemical-safety`](chemical-safety.md), [`ehs.ppe`](ppe.md)
> **Timeline**: Years 30-70
> **Outputs**: emergency_procedures, spill_response, evacuation_plans, first_aid_protocols, emergency_equipment

## Problem

Semiconductor manufacturing presents unique emergency scenarios: pyrophoric gas leaks that ignite spontaneously, toxic hydride gas releases at concentrations measured in parts per billion, hydrofluoric acid exposures that cause systemic poisoning through skin absorption, and mixed-chemical fires producing toxic combustion products. Standard industrial emergency response is insufficient — a firefighter applying water to a silane fire could spread the burning gas; a first responder entering an arsine release without SCBA becomes a victim within minutes. This document defines emergency response procedures specific to semiconductor chemical hazards.

## Emergency Equipment Placement

### Eyewash Stations

**Type**: Plumbed (preferred) or self-contained (gravity-fed, portable). Not handheld squeeze bottles (insufficient volume and flow).

**Specifications**:
- Flow rate: 0.4 L/min minimum per nozzle (two nozzles for both eyes simultaneously)
- Water temperature: Tepid (15-35°C). Heated water supply or tempered blending valve required in cold climates. Cold water causes hypothermic shock during the required 15-minute flush; hot water scalds damaged tissue.
- Activation: Hands-free (foot pedal or push handle that stays on — no hold-open required). Must activate in one second or less.
- Duration: Must deliver flush for minimum 15 minutes continuous without requiring user to hold the valve open.
- Water quality: Potable water. No cross-connection to process water or ultrapure water systems. Weekly activation test (run 3 minutes minimum to flush stagnant water from lines, verify flow, check temperature).

**Placement requirements**:
- Within 10 seconds travel distance from any chemical hazard (approximately 8 meters unobstructed path)
- On the same level as the hazard (no stairs, doors, or obstacles between the worker and the station)
- Clearly marked with illuminated sign (green eyewash symbol, visible in power failure)
- Unobstructed access at all times — no storage, equipment, or carts blocking the path
- Weekly inspection log posted at the station

### Emergency Deluge Showers

**Specifications**:
- Flow rate: 75 L/min minimum (20 GPM) at 210 kPa (30 psi) minimum supply pressure
- Pattern: Full body deluge, 50 cm diameter minimum spray pattern at 60 cm above standing surface
- Activation: Pull rod or chain (overhead) that stays on until intentionally shut off
- Water temperature: Tepid (15-35°C)
- Duration: Minimum 15 minutes continuous flow
- Drainage: Floor drain with capacity to handle 75 L/min flow. Drain routed to chemical waste collection (not general sanitary sewer — contaminated water from emergency showers contains whatever chemical the worker was exposed to)

**Placement requirements**:
- Within 10 seconds travel distance from any chemical hazard
- Co-located with eyewash station (combination units preferred)
- Not within electrical hazard areas unless GFCI-protected
- Clearly marked, illuminated sign, unobstructed access
- Annual flow test (verify 75 L/min flow rate and spray pattern)

### Spill Kits

**Location**: At every chemical storage area, chemical dispensing station, and gas cylinder storage area.

**Contents by chemical type**:

**Acid spill kit**:
- Neutralizing absorbent: Sodium bicarbonate (NaHCO₃) or calcium carbonate (CaCO₃) granules — neutralizes acids with visible fizzing (provides visual confirmation of neutralization)
- Absorbent pads and pillows (polypropylene, acid-resistant)
- Chemical-resistant gloves (neoprene, 0.5 mm)
- Chemical splash goggles
- Polyethylene scoop and disposal bags (thick gauge, labeled for acid waste)
- pH test paper (0-14 range) to verify neutralization to pH 6-8 before disposal

**HF-specific spill kit** (separate from general acid kit):
- Calcium carbonate (CaCO₃) or lime (CaO) absorbent — converts HF to insoluble CaF₂
- NEVER use sodium bicarbonate for HF — the reaction is too slow and produces sodium fluoride (water-soluble and toxic)
- Dedicated neoprene gloves (0.8 mm)
- Full-face shield
- Calcium gluconate gel (2.5%) — multiple tubes
- HF warning signs and barrier tape
- Disposal: all HF spill cleanup material disposed as hazardous fluoride waste

**Solvent spill kit**:
- Hydrophobic absorbent (activated carbon or treated polypropylene — absorbs organics, repels water)
- Non-sparking tools (brass or plastic scoop — no steel, no sparks)
- Chemical-resistant gloves (nitrile)
- Chemical splash goggles
- Ventilation fan or explosion-proof blower for vapor control
- Disposal bags labeled for solvent waste
- NO ignition sources — solvents are flammable; clear area of all potential ignition sources before cleanup

**Hydride gas leak kit** (at gas cabinet locations):
- SCBA (45-minute, pre-checked and ready)
- Chemical suit (barrier laminate)
- Gas-specific emergency response card
- Emergency shutoff valve locations posted
- Two-way radio (intrinsically safe rated)
- Caustic scrubber solution (20% NaOH) for emergency neutralization of AsH₃/PH₃

## Chemical Exposure First Aid

### Hydrofluoric Acid Exposure

**Skin contact** (most common HF emergency):
1. Immediately remove all contaminated clothing while flushing with water. Do not waste time — seconds matter.
2. Flush affected area with copious running water for minimum 15 minutes. If calcium gluconate gel is immediately available, 5 minutes of flushing is acceptable before gel application.
3. Apply calcium gluconate gel (2.5%) generously to the entire affected area. Massage in continuously and deeply — fluoride ions penetrate tissue rapidly and must be neutralized at depth.
4. Reapply gel every 15 minutes during transport to medical facility. Do not let the gel dry out.
5. If pain persists after gel application, inject calcium gluconate solution (5%) subcutaneously beneath the affected area (medical procedure — requires trained provider).
6. For exposures >1% body surface area with concentrated HF (>50%), anticipate systemic hypocalcemia. Monitor cardiac rhythm. Administer IV calcium gluconate (1 g in 100 mL D5W, slow push). Transport to hospital immediately.
7. All HF exposures require medical evaluation, even if initial pain is minimal. Delayed onset of deep tissue necrosis is characteristic of dilute HF.

**Eye exposure**:
1. Flush at eyewash station for minimum 30 minutes — continuous flow, holding eyelids open.
2. Apply calcium gluconate eye drops (1%) after initial flushing if available.
3. Do not apply calcium gluconate gel to the eye — use liquid drops only.
4. Transport to ophthalmologist immediately. HF eye exposures can cause corneal perforation and permanent vision loss.

**Inhalation**:
1. Move victim to fresh air immediately. Call emergency response.
2. Administer 100% oxygen by non-rebreather mask if available.
3. Monitor for pulmonary edema (delayed onset, 12-24 hours). Symptoms: progressive shortness of breath, cough, pink frothy sputum.
4. Nebulized calcium gluconate (2.5% solution) may be administered for symptomatic relief (reduces pulmonary fluoride absorption).

### Silane Exposure / Silane Fire

**Gas leak (no fire)**:
1. Evacuate area immediately — silane can auto-ignite at any moment if concentration exceeds 1.4% in air.
2. Activate emergency shutoff valves (remotely operated from outside the gas cabinet area).
3. Do NOT attempt to stop a silane leak by hand — if it ignites during your approach, you will be in the flash zone.
4. Emergency response team with SCBA investigates from upwind, monitors gas concentration.
5. If concentration is below LEL and declining (natural ventilation), allow to dissipate with continuous monitoring.
6. If concentration is above LEL or rising, evacuate the building.

**Silane fire**:
1. Primary response: Shut off the gas supply at the source. A silane fire will self-extinguish when the fuel supply stops.
2. Do NOT extinguish a silane flame while gas is still flowing — the unburned gas accumulates and can cause a much larger explosion.
3. If gas cannot be shut off, protect surrounding equipment with water spray (cooling only — do not aim water at the flame). Allow the gas to burn off.
4. Silane fires produce SiO₂ fume (white smoke) — respiratory hazard. Wear respiratory protection during response.
5. Never use CO₂ extinguishers on silane fires — the cold CO₂ stream can cause silane to condense and pool, creating an explosion risk when it vaporizes.

### Arsine / Phosphine Exposure

**Inhalation (primary route of exposure for gases)**:
1. Move victim to fresh air immediately. Rescuer must wear SCBA — arsine at 0.5 ppm is dangerous, and IDLH is 3 ppm (arsine) or 50 ppm (phosphine). You cannot smell either gas reliably.
2. Administer 100% oxygen by non-rebreather mask.
3. For arsine: Monitor for hemolytic anemia (onset delayed 2-24 hours). Dark or red urine (hemoglobinuria) indicates active hemolysis. Blood transfusion may be required for severe hemolysis. Dimercaprol (British Anti-Lewisite, BAL) chelation therapy for confirmed arsenic poisoning.
4. For phosphine: Monitor for pulmonary edema and cardiac effects. No specific antidote — treatment is supportive (oxygen, cardiac monitoring, pulmonary care).
5. Hospital transport mandatory for any confirmed or suspected arsine exposure. Hospital must be notified of arsine exposure to prepare for potential massive hemolysis (blood typing, cross-matching, renal dialysis capability).

**Gas leak response**:
1. Evacuate area immediately. Activate emergency shutoff.
2. Emergency response team in full SCBA and chemical suits investigates from upwind.
3. Continuous monitoring with portable gas detector (electrochemical, arsine-specific).
4. If gas is confined to gas cabinet with exhaust operational: allow cabinet exhaust and scrubber system to capture the release. Verify scrubber operation. Monitor exhaust stack for breakthrough.
5. If gas has escaped to fab area: Full building evacuation. Fire department hazmat response.

### General Acid/Base Exposure

**Skin contact**:
- Acids: Flush 15+ minutes with water. Remove contaminated clothing immediately. Do not attempt neutralization on skin (the neutralization reaction is exothermic and causes additional thermal burns).
- Bases (alkalis): Flush 15+ minutes minimum — alkali burns are more damaging than acid burns because alkalis saponify cell membranes and penetrate deeper. Extended flushing (30+ minutes) recommended for concentrated NaOH or KOH exposure.
- Phenol: Flush with water AND use polyethylene glycol (PEG 300 or 400) or 70% isopropanol to dissolve phenol from skin — water alone is insufficient because phenol is poorly water-soluble. Phenol absorbs rapidly through skin and causes systemic toxicity (seizures, cardiac arrhythmia).

**Eye contact**: Flush at eyewash station 15-30 minutes. Hold eyelids open. Alkali burns require longer flushing than acid burns. All chemical eye exposures require ophthalmological evaluation.

## Evacuation Procedures

### Alarm System

Semiconductor fabs use a multi-tier alarm system:

**Tier 1 — Alert alarm** (strobe only, or distinctive tone):
- Condition: Gas detection at low alarm threshold, or equipment malfunction
- Action: Stop work. Assess the situation. Prepare for potential evacuation. Stand by for instructions.

**Tier 2 — Evacuation alarm** (audible + visual, distinctive evacuation tone):
- Condition: Gas detection at high alarm threshold, confirmed toxic release, fire, or explosion
- Action: Evacuate immediately via designated routes. Do not stop to collect personal items. Close doors behind you (contains the release). Proceed to assembly point.

**Tier 3 — Shelter-in-place** (different tone):
- Condition: External hazard (chemical release from adjacent facility, severe weather) making outdoor evacuation more dangerous than staying inside
- Action: Move to designated interior shelter areas. Seal doors and windows. Shut down outside air intake if possible.

### Evacuation Routes

- Minimum two independent exit paths from any location in the fab (no dead-end corridors longer than 6 meters)
- Exit routes do not pass through gas cylinder storage, chemical storage, or utility corridors with gas piping
- Emergency lighting (battery backup, minimum 90 minutes) illuminates exit paths during power failure
- Photoluminescent (glow-in-the-dark) directional markers on floor and at low level (smoke rises, visibility at floor level may be better)
- Exit doors open outward, equipped with panic hardware (push bar), not locked from inside during occupancy

### Assembly Points

- Located upwind and upgrade from the building, minimum 100 meters from gas cylinder storage and chemical loading areas
- Multiple assembly points for large facilities, preventing all personnel from gathering at a single location
- Personnel accountability: Head count against daily access roster. Missing persons reported to emergency response team immediately
- Wind socks visible at assembly points to determine wind direction (inform evacuees which direction is downwind — stay upwind)

## Emergency Response Organization

### Response Team Roles

**First responder** (nearest qualified person):
- Assess the situation from a safe distance
- Activate alarm if not already triggered
- Call emergency response team
- Provide first aid within capability (do not enter the hazard zone without proper PPE)

**Emergency response team** (trained, equipped, on-call):
- Minimum 6 members on duty during operating hours
- All trained in SCBA use, chemical spill response, and first aid
- Access to emergency PPE kits pre-positioned throughout the facility
- Gas-specific response cards for each gas used in the facility (properties, hazards, PPE, containment, first aid)

**Incident commander**:
- Single designated decision-maker during emergency
- Responsible for evacuation decisions, emergency shutdown authorization, coordination with external responders
- Communications: Radio channel dedicated to emergency operations

### Drill Requirements

| Drill Type | Frequency | Duration | Participants |
|------------|-----------|----------|-------------|
| Evacuation drill | Quarterly | 15-30 min | All building occupants |
| Chemical spill response | Semi-annually | 30-60 min | Emergency response team |
| Gas leak response | Annually | 60-90 min | Emergency response team + management |
| Full-scale exercise (multi-agency) | Annually | 2-4 hours | All internal responders + fire department + hospital |
| Tabletop exercise (scenario-based) | Quarterly | 60 min | Emergency response team + management |

## Emergency Equipment Maintenance

### Inspection Schedule

| Equipment | Inspection | Frequency | Standard |
|-----------|-----------|-----------|----------|
| Eyewash stations | Flow test (3 min), temperature, signage | Weekly | ANSI Z358.1 |
| Deluge showers | Flow test, spray pattern, temperature | Annually (weekly visual) | ANSI Z358.1 |
| SCBA units | Cylinder pressure, facepiece seal, regulator function | Monthly (after each use) | NFPA 1852 |
| Spill kits | Contents inventory, expiration dates | Monthly | Facility-specific |
| Fire extinguishers | Pressure gauge, seal, condition | Monthly | NFPA 10 |
| Gas detection alarms | Sensor calibration, alarm setpoints, strobe/horn | Quarterly (monthly bump test) | Manufacturer spec |
| Emergency lighting | Functional test (90 sec minimum) | Monthly | NFPA 101 |
| First aid kits | Contents inventory, expiration dates | Monthly | ANSI Z308.1 |

## See Also

- [Chemical Safety & Toxicology](chemical-safety.md) — Chemical hazard data for emergency planning
- [Ventilation & Exhaust Systems](ventilation-exhaust.md) — Emergency exhaust and scrubber systems
- [Personal Protective Equipment](ppe.md) — Emergency PPE requirements and kits
- [Waste Management](waste-management.md) — Disposal of contaminated spill cleanup materials
- [Occupational Health](../health/occupational-health.md) — General emergency first aid procedures

---

*Part of the [Bootciv Tech Tree](../index.md) · [EHS](./index.md) · [All Domains](../index.md)*
