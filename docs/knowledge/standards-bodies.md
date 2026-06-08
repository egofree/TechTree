# Standards Bodies

> **Node ID**: knowledge.standards-bodies
> **Domain**: [Knowledge Preservation & Education](./index.md)
> **Dependencies**: [`knowledge.writing`](writing.md), [`knowledge.printing`](printing.md), [`knowledge.technical-drawing`](technical-drawing.md), [`measurement`](../measurement/index.md)
> **Enables**: [`knowledge.information-durability`](information-durability.md)
> **Timeline**: Years 10-200+
> **Outputs**: technical_standards, measurement_standards, quality_standards, interoperability_specifications
> **Critical**: Yes — without agreed standards, every workshop produces incompatible parts, measurement systems diverge, and inter-settlement trade in manufactured goods collapses


Standards bodies are the organizational mechanisms by which a civilization agrees on common specifications: screw thread profiles, material grades, electrical voltages, paper sizes, drawing conventions, and measurement units. The need emerges as soon as two workshops must produce interchangeable parts, or two settlements must trade goods with agreed-upon quality. Standards prevent the fragmentation of effort that occurs when each practitioner invents their own system.

This capability covers the *process* of creating, maintaining, and enforcing standards — the organizational and knowledge infrastructure, not the specific content of any particular standard. The content (thread profiles, material specifications, electrical codes) belongs to the relevant technical domains. What belongs here is the machinery of consensus, documentation, revision, and compliance that makes standards work. This includes concrete organizational templates and worked examples sufficient for a community to establish its own standards body from scratch.

## How to Establish a Standards Body

![Bans Off Our Bodies NYC (42278)](../images/knowledge/knowledge_standards-bodies.jpg)

> *Bans Off Our Bodies NYC*

> *Image: Rhododendrites, CC BY-SA 4.0*

A standards body is a standing organization with a defined charter, membership rules, and procedures. It does not require a large bureaucracy — a bootstrap settlement can start with a part-time committee of 3-5 people managing 10-20 critical standards. The key is having defined procedures so that standards are produced by a repeatable process rather than ad hoc.

### Step 1: Identify the Need

The catalyst is always a concrete failure that has an economic cost:

- **Interchangeability failure**: Two workshops produce bolts that do not fit each other's nuts. A machine built with parts from one workshop cannot be repaired with parts from another.
- **Measurement disagreement**: Two settlements measure the same steel bar and get different hardness values because they use different test methods or different reference standards.
- **Material uncertainty**: "Mild steel" from one foundry has different properties than "mild steel" from another, causing unpredictable performance in structural applications.
- **Safety incident**: A pressure vessel fails because the manufacturer used a wall thickness that no one had standardized a minimum for.

Document the failure in specific terms: what broke, what it cost, what would have prevented it. This problem statement becomes the justification for the standards body and the first project in its charter.

### Step 2: Convene a Founding Committee

Gather the people who have direct stakes in the problem. A founding committee needs:

- **Producers**: At least 2 representatives from different workshops or foundries. Without producer buy-in, standards are ignored.
- **Users**: At least 1 representative from the community that consumes the products being standardized. Users catch requirements that producers would not think to include.
- **A technical authority**: 1 person recognized as having the deepest expertise in the domain. This person drafts the initial technical content.
- **A secretary**: 1 person responsible for documenting meetings, distributing drafts, and maintaining records. This can be a part-time role but must be a named individual, not a shared responsibility.

**Founding committee size**: 5-9 members. Fewer than 5 and the committee lacks perspective diversity. More than 9 and decision-making slows unacceptably.

**Who to exclude**: People who do not practice in the domain. Theoretical knowledge is valuable for review but the drafting committee must consist of people who will use the standard daily. At least 50% of the committee must be active practitioners.

### Step 3: Write a Charter

The charter is a single document (1-2 pages) that establishes:

```
CHARTER TEMPLATE

1. NAME: [Settlement/Region] Standards Body for [Domain]
   Example: "Valley Standards Committee for Mechanical Interchangeability"

2. PURPOSE: [One sentence stating what standards this body will produce]
   Example: "To develop and maintain specifications for screw threads,
   material grades, and dimensional tolerances that enable interchangeable
   parts between workshops in the valley."

3. SCOPE: [List of standard categories the body will cover]
   Example: "Screw thread profiles and gauges; steel grade definitions;
   dimensioning and tolerancing conventions for engineering drawings."

4. MEMBERSHIP: [Who may participate, how members are selected, terms]
   Example: "Any workshop or settlement that manufactures or uses products
   within the scope may send one representative. Members serve 3-year
   terms, renewable once. The technical authority is appointed by consensus
   of the founding committee."

5. DECISION PROCESS: [How standards are approved — see Voting Procedures below]
   Example: "Standards are approved when no member raises a sustained
   technical objection after a minimum 3-month comment period. Objections
   must cite specific technical deficiencies. Majority vote is used only
   to break deadlocks after two rounds of technical discussion."

6. REVISION CYCLE: [How often standards are reviewed]
   Example: "Every published standard is reviewed at minimum every 5 years.
   Emergency revisions may be issued at any time by unanimous consent of
   the committee."

7. PUBLICATION: [How standards are distributed]
   Example: "Standards are published as numbered, printed documents.
   One copy is deposited in each settlement library and one in each
   participating workshop."

8. FUNDING: [How the body's costs are covered]
   Example: "Costs are shared equally among participating workshops.
   Initial costs: paper, printing, reference artifacts. Estimated annual
   budget: [amount]."
```

### Step 4: Establish Committee Structure

A standards body with more than one active standard project needs a lightweight committee structure:

**Plenary (all members)**: Meets quarterly. Reviews all standards activity, approves final standards, sets priorities for the next quarter. Quorum: 60% of members.

**Working groups (per standard)**: 3-7 members each. One working group per active standard project. The working group drafts, revises, and tests the standard. Reports to the plenary at each quarterly meeting. Dissolved when the standard is published and maintenance responsibility is assigned.

**Technical review panel**: 3 senior practitioners (not members of the working group that drafted the standard). Reviews the final draft for technical correctness, clarity, and absence of ambiguity before the plenary votes on publication. This separation ensures that no standard is approved by the same people who wrote it.

**Secretary**: Maintains the standards registry (numbered list of all published standards with revision dates), distributes meeting notices, records minutes, manages document archives. This is the one role that must be filled by a named individual at all times — if the secretary leaves, a replacement must be appointed before any other business proceeds.

### Step 5: Begin Operations

1. **Adopt the charter**: Founding committee signs the charter. This act establishes the body's authority — not legal authority (which requires governance infrastructure), but technical authority derived from the expertise of its members.
2. **Numbering system**: Establish a standard numbering system. Format: `[body acronym]-[sequence number]`. Example: VSC-001 (Valley Standards Committee, standard 1). Reserve blocks: 001-099 for measurement standards, 100-199 for material standards, 200-299 for interoperability standards, 300-399 for process standards, 400-499 for safety standards.
3. **Assign the first project**: The problem statement from Step 1 defines the first standard. Assign it to a working group.
4. **Set a schedule**: The working group reports progress monthly. The plenary reviews the draft at the next quarterly meeting. Target: first published standard within 18 months of founding.

## Committee Meeting Formats

### Monthly Working Group Meeting

**Purpose**: Draft and revise a specific standard.
**Duration**: 2-4 hours.
**Attendees**: Working group members (3-7) plus secretary.
**Agenda**:

1. Review action items from previous meeting (10 min)
2. Technical presentation on the section being drafted (30 min)
3. Discussion and revision of draft text (60-120 min)
4. Identify open questions requiring research or testing (30 min)
5. Assign action items with deadlines (10 min)

**Output**: Annotated draft with tracked changes, action item list.

### Quarterly Plenary Meeting

**Purpose**: Review all working group progress, approve or reject standards for publication.
**Duration**: Half day (4-6 hours).
**Attendees**: All members, plus invited observers from affected industries.
**Agenda**:

1. Secretary reads minutes of previous plenary — corrections accepted (15 min)
2. Each working group presents progress report (20 min per group)
3. Technical review panel reports on any standards under review (20 min per standard)
4. Discussion and vote on any standards ready for approval (30 min per standard)
5. New business: proposals for new standards, revision requests, complaints (30 min)
6. Schedule and priorities for next quarter (15 min)

**Output**: Published minutes with voting record, updated standards registry, revised priorities.

### Annual Review Meeting

**Purpose**: Evaluate the body's performance, revise the charter if needed, elect officers.
**Duration**: Full day.
**Attendees**: All members.
**Agenda**:

1. Secretary's annual report: standards published, revised, withdrawn; costs incurred (30 min)
2. Technical review panel assessment: quality of standards produced, common deficiencies found (30 min)
3. Member feedback: each member reports on how standards are being used in practice (60 min)
4. Charter amendments (if any) — requires 75% approval (30 min)
5. Election of secretary and technical review panel for next year (30 min)
6. Priority setting: which domains need new standards next year (60 min)

## Voting Procedures

Standards bodies must make decisions. The decision-making process determines whether standards are technically sound or politically compromised.

### Consensus Process (Primary Method)

A standard is approved when all significant technical objections have been resolved. This is not unanimity — a member who has no technical argument and simply dislikes the standard does not have a blocking objection.

**Procedure**:

1. Working group publishes draft standard and circulates to all members.
2. Comment period: minimum 3 months. Any member may submit written comments citing specific sections and specific technical objections.
3. Working group responds to every comment in writing: accepted (with revision), rejected (with technical justification), or deferred (with reason).
4. If all comments are resolved, the draft goes to the technical review panel.
5. If unresolved comments remain, the working group revises the draft and re-circulates for a second comment period (minimum 1 month).
6. After two rounds, any remaining unresolved objections are escalated to the plenary for a binding decision.

### Escalation Vote (Deadlock Resolution)

When consensus fails after two comment rounds, the plenary votes. This is the exception, not the norm — a standard that requires a vote is usually one that has not been adequately refined.

**Voting rules**:
- Quorum: 60% of members present or represented by written proxy.
- Approval threshold: 75% of votes cast (not 75% of total membership — absent members do not block).
- Voting method: Written ballot (not show of hands) to prevent social pressure.
- The secretary records each member's vote in the minutes. Anonymous voting is not permitted — standards are technical documents and members must stand behind their positions.

### Objection Adjudication

A valid objection must meet all three criteria:

1. **Technical**: The objection cites a specific technical deficiency in the draft (e.g., "Section 4.2 specifies a carbon content range of 0.15-0.25% but the validation data in Annex B shows that 0.25% produces brittle welds at temperatures below -10°C"). Personal preference is not a valid objection.
2. **Constructive**: The objector proposes a specific alternative (e.g., "Revise to 0.15-0.20% and add a note about low-temperature welding limitations").
3. **Material**: The objection affects the standard's technical adequacy, not its formatting, wording preferences, or administrative details.

The technical review panel judges whether an objection meets these criteria. Objections that fail any criterion are recorded but do not block consensus.

## Prerequisites

- **Materials**: Paper and printing for standard documents ([Printing](printing.md))
- **Tools**: [Technical Drawing](technical-drawing.md) instruments for illustrating standard specifications, [Measurement](../measurement/precision-metrology.md) instruments for reference standards
- **Knowledge**: [Writing](writing.md) for unambiguous specification language, engineering knowledge in the domain to be standardized
- **Infrastructure**: Meeting facilities, document storage and distribution system, testing facilities for validating compliance

## Bill of Materials

| Material/Resource | Quantity per Standard | Source | Alternatives |
|-------------------|----------------------|--------|-------------|
| Printed standard documents | 50-500 copies per standard | [Printing](printing.md) | Hand-copied (10× cost, 100× slower) |
| Reference measurement artifacts | 1-3 master sets per standard type | [Measurement](../measurement/precision-metrology.md) | No substitute — must be manufactured to specified accuracy |
| Test specimens for validation | 10-100 per validation round | Relevant domain (metals, ceramics, etc.) | Reduced sample size (lower statistical confidence) |
| Meeting facilities | Shared across all standards activities | [Construction](../construction/index.md) | Correspondence-based process (slower, 5-10× timeline) |


## Standards Development Lifecycle

1. **Need identification**: A practitioner or organization identifies a problem caused by lack of standardization — parts don't fit, measurements don't agree, materials perform unpredictably. Document the specific failure and its economic cost.
2. **Working group formation**: Convene 5-15 domain experts representing different stakeholders (producers, users, testers). Diversity of perspective prevents standards that serve only one interest.
3. **Draft specification**: Working group produces a draft document specifying the standard: definitions, requirements, test methods, acceptance criteria, marking requirements.
4. **Consensus review**: Circulate draft to all affected parties for comment. Minimum comment period: 3-6 months. Resolve objections through technical argument, not voting — the goal is technical correctness, not majority rule.
5. **Testing and validation**: Produce test specimens and distribute to participating workshops. Verify that the specification is achievable in practice and produces the intended result.
6. **Publication and adoption**: Publish the approved standard as a numbered document. Set an adoption timeline: voluntary for 1-2 years, then mandatory for government procurement and safety-critical applications.
7. **Revision cycle**: Review every 5-10 years. Incorporate lessons learned, new technology, and changed circumstances. Maintain backward compatibility where possible.

## Worked Examples

These examples show the full lifecycle of a standard from need identification through publication, using domains relevant to the tech tree.

### Example 1: Length Measurement Standard (VSC-001)

**Need**: Three machine shops in the valley produce parts for each other but their rulers disagree by 0.5 mm over 300 mm. Assembled machines have loose joints and misaligned bores.

**Working group**: 2 machinists, 1 instrument maker, 1 surveyor, 1 secretary (5 members).

**Draft development** (9 months):

1. Define the unit: "The valley meter is the distance between two fine lines engraved on the bar of alloy steel held at the Standards Office, at the temperature of melting ice." Physical realization, not a theoretical definition — the bar *is* the meter.
2. Define temperature correction: All length measurements reference 20°C. Provide a thermal expansion correction table for steel (11.5 × 10⁻⁶ per °C). A 300 mm steel bar measured at 30°C is actually 300.035 mm — this matters for precision fits.
3. Define calibration hierarchy:
   - **Primary standard**: The master meter bar. Stored in a temperature-controlled room. Used only to calibrate secondary standards.
   - **Secondary standards**: 5 working meter bars, calibrated against the primary. Distributed to each participating workshop.
   - **Working standards**: Rulers, calipers, and gauges in daily use. Calibrated against secondary standards every 6 months.
4. Define calibration procedure: Comparison by comparator (a mechanical device that detects displacement between two bars to ±0.001 mm). Record: date, temperature, deviation from primary, adjustment made.
5. Define verification: Every instrument used for trade or interchange must carry a calibration stamp showing the date of last verification. Instruments without stamps are not acceptable for specifying parts in standard dimensions.

**Comment period** (4 months): One machinist objects that the 20°C reference temperature is impractical because workshops operate at 15-35°C. Resolution: add a simplified correction chart (lookup table by temperature) as an annex, so practitioners can adjust readings without calculation.

**Testing** (3 months): Distribute 3 test bars of known length (measured against the primary standard) to each workshop. Each workshop measures the bars using their own instruments and the prescribed procedure. Results agree within ±0.05 mm — the standard is achievable.

**Publication**: VSC-001, "Linear Measurement Standard," Revision A, dated [year]. 50 copies printed. One deposited in each workshop, one in the settlement library, one in the Standards Office archive.

**Annual cost**: Paper and printing for 50 copies (minimal). Manufacture and maintenance of 6 reference bars (one-time, then recalibration labor). Secretary labor: approximately 1 day per month.

### Example 2: Steel Grade Standard (VSC-101)

**Need**: A bridge built with steel from Foundry A collapsed under load that steel from Foundry B would have survived. Investigation reveals that "mild steel" from Foundry A contains 0.35% carbon (too brittle for structural use) while Foundry B's contains 0.20%.

**Working group**: 2 foundry operators, 1 structural engineer, 1 blacksmith, 1 testing laboratory technician (5 members).

**Draft development** (14 months):

1. Define steel grades by carbon content and mechanical properties:

   | Grade | Carbon (% range) | Yield Strength (min) | Use |
   |-------|-------------------|---------------------|-----|
   | S-1 (structural mild) | 0.10-0.20 | 200 MPa | Buildings, bridges, ships |
   | S-2 (medium) | 0.20-0.40 | 300 MPa | Machine frames, gears |
   | S-3 (high carbon) | 0.40-0.70 | 400 MPa | Springs, cutting tools, rails |
   | S-4 (tool steel) | 0.70-1.20 | 500+ MPa (hardened) | Cutting tools, dies |

2. Define test methods: Tensile test (specimen geometry, loading rate, measurement of yield point and ultimate strength). Carbon content by mass: qualitative spark test (for field sorting) and quantitative combustion analysis (for certification).
3. Define marking: Each batch of steel from a certified foundry must be stamped with the grade designation (S-1, S-2, etc.), the foundry mark, and the batch number. The stamp is applied to both ends of each bar.
4. Define batch testing: One specimen per 50 bars in a batch. If the specimen fails, the entire batch is rejected and re-tested bar-by-bar.

**Comment period** (5 months): Foundry A objects that the required tensile testing is too expensive (they do not have a testing machine). Resolution: allow spark testing as a preliminary sorting method, but require tensile testing for any steel used in structural applications. The settlement funds one shared testing machine at the Standards Office.

**Testing** (6 months): Each foundry produces 3 batches of each grade. The testing laboratory independently verifies composition and properties. 2 batches fail (one has carbon content outside the specified range, one has low yield strength due to inadequate forging). The standard catches real quality problems — it works.

**Publication**: VSC-101, "Steel Grade Classification," Revision A. 30 copies.

### Example 3: Screw Thread Standard (VSC-201)

**Need**: A machine assembled from parts made by three different workshops has 14 bolted joints. 6 of them leak or loosen because the bolt and nut threads do not mate properly. Each workshop cuts threads with a different profile and pitch.

**Working group**: 2 machinists (from different workshops), 1 tool maker, 1 mechanical designer, 1 secretary (5 members).

**Draft development** (12 months):

1. Adopt a single thread profile: 60° triangular (metric), based on the argument that the 60° form is easier to cut accurately than the Whitworth 55° form with its radiused roots and crests. Specify flat crests and flat roots (simpler to manufacture than rounded).
2. Define the pitch series: For each nominal diameter, specify exactly one coarse pitch (for general use) and one fine pitch (for adjustable and thin-wall applications).

   | Nominal Diameter (mm) | Coarse Pitch (mm) | Fine Pitch (mm) |
   |----------------------|-------------------|-----------------|
   | 6 | 1.0 | 0.75 |
   | 8 | 1.25 | 1.0 |
   | 10 | 1.5 | 1.25 |
   | 12 | 1.75 | 1.25 |
   | 16 | 2.0 | 1.5 |
   | 20 | 2.5 | 1.5 |
   | 24 | 3.0 | 2.0 |

3. Define tolerance classes: Medium (general purpose) and Close (precision fits). Specify the pitch diameter tolerance for each class in terms of nominal diameter and pitch (formula, not lookup table — so it extends to any diameter).
4. Define gauging: Go/no-go thread gauges for each size. The "go" gauge must thread fully into the nut and over the bolt. The "no-go" gauge must not enter more than 2 turns. Gauge specifications are part of the standard.
5. Define marking: Thread size stamped on bolt head and nut face (e.g., "M10×1.5" for metric 10 mm diameter, 1.5 mm pitch).

**Comment period** (3 months): One machinist objects to the 60° profile because they have 55° Whitworth tooling already. Resolution: the economic argument (interchangeability across all workshops) outweighs the sunk cost of one workshop's tooling. The tool maker in the working group agrees to produce 60° threading tools at cost for the transition.

**Testing** (4 months): Produce go/no-go gauges from the specification. Distribute to all workshops. Each workshop cuts threads in 3 sizes (M10, M16, M20) and tests with gauges. Results: 95% pass rate on first attempt. The 5% failures trace to lathe alignment issues, not the standard itself.

**Publication**: VSC-201, "Metric Screw Threads," Revision A. 60 copies (every workshop gets 2: one for the floor, one for the office).

**Enforcement**: Within 1 year, all government procurement specifies VSC-201 threads. Within 3 years, non-standard threads are refused by all trading partners. The transition cost (replacing tooling) is estimated at 2 weeks of downtime per workshop — far less than the ongoing cost of incompatibility.

## Revision Management

A published standard is not permanent. Technology changes, new materials appear, and practical experience reveals deficiencies. Every standard needs a revision management system.

### Version Control

- **Numbering**: VSC-001 Rev A, Rev B, Rev C, etc. Never reuse a revision letter — if Rev B is withdrawn, the next revision is Rev C, not a reissued Rev B.
- **Change marking**: In the printed document, mark changed paragraphs with a vertical line in the margin. This lets readers find what changed without re-reading the entire standard.
- **Change summary**: The first page of each revision lists every change: "Rev B: Section 4.2 carbon range narrowed from 0.15-0.30% to 0.15-0.25% (low-temperature brittleness). Annex C added (thermal correction chart)."
- **Supersession notice**: When a new revision is published, distribute a supersession notice to all known holders of the previous revision. The notice states: "VSC-001 Rev A is superseded by VSC-001 Rev B dated [date]. Rev A copies should be destroyed or clearly marked 'SUPERSEDED.' Contact the Standards Office for a replacement copy."

### Scheduled Review

Every 5 years, each published standard comes up for review. The review process:

1. **Secretary's notice**: 6 months before the review date, the secretary notifies the plenary that the standard is due.
2. **User survey**: The secretary sends a one-page questionnaire to all known users: "Have you encountered any problems with this standard? Any sections that are unclear, incorrect, or missing? Any new technology that the standard should address?"
3. **Technical review panel assessment**: One panel member reads the standard cover-to-cover and writes a 1-page assessment: still adequate, needs minor revision, needs major revision, or should be withdrawn.
4. **Plenary decision**: Based on the survey and assessment, the plenary votes to reaffirm (no changes, extend for another 5 years), revise (assign to a working group), or withdraw (standard is obsolete or superseded by another).

### Emergency Revision Procedure

When a safety incident or widespread practical failure reveals an urgent deficiency:

1. Any member may petition the secretary for an emergency revision, citing the specific failure and the standard section involved.
2. The technical review panel assesses the petition within 1 week. If they confirm the deficiency is urgent and safety-related, they authorize an emergency revision.
3. The relevant working group (or a hastily convened substitute if the original has been dissolved) produces a revision within 1 month.
4. The revised standard is circulated for a 2-week comment period (shortened from the normal 3 months — the urgency justifies the expedited timeline).
5. If no unresolved objections remain, the plenary chair approves publication without waiting for a quarterly meeting.
6. Emergency revisions are clearly labeled: "VSC-401 Rev B (Emergency — Pressure Vessel Wall Thickness Correction)."

### Standard Withdrawal

A standard may be withdrawn when:
- It has been superseded by a newer standard that fully covers the same scope.
- The technology it covers is no longer used (e.g., a standard for wooden water pipes after the community transitions to iron).
- It has been found fundamentally flawed and a replacement is in development.

Withdrawal procedure: The plenary votes to withdraw. The secretary publishes a withdrawal notice stating the reason, the effective date (typically 6 months in the future to allow users to transition), and any replacement standard. After the effective date, the withdrawn standard is removed from the active registry and copies in libraries are marked "WITHDRAWN — not to be used for new work."

## Critical Standard Categories

**Measurement standards**: Define units, reference artifacts, calibration chains, and measurement procedures. Without these, no two instruments read the same value. Examples: meter standard, kilogram prototype, thermocouple reference tables, thread gauge specifications.

**Material standards**: Define composition ranges, mechanical properties, and testing methods for materials. Without these, "mild steel" means something different in every foundry. Examples: steel grade specifications (yield strength, carbon content), concrete strength classes, paper grammage ranges.

**Interoperability standards**: Define interfaces so that parts from different sources work together. Without these, every manufacturer's bolts fit only their own nuts. Examples: screw thread profiles, flange dimensions, electrical connector pinouts, pipe fitting sizes.

**Process standards**: Define procedures for critical operations. Without these, every practitioner develops their own method, and quality varies unpredictably. Examples: welding procedure specifications, heat treatment protocols, inspection sampling plans.

**Safety standards**: Define minimum safety requirements for products and processes. Without these, the cost of accidents is borne by the user rather than prevented at the design stage. Examples: pressure vessel codes, electrical installation codes, machine guarding requirements.


## Standard Development Timeline

| Phase | Duration | Participants | Deliverable |
|-------|----------|-------------|-------------|
| Need identification and proposal | 1-3 months | 1-3 proponents | Problem statement, scope document |
| Working group formation | 1-2 months | 5-15 experts | Charter, membership, schedule |
| Draft development | 6-18 months | 5-15 experts + support staff | Draft standard document |
| Public review and comment | 3-6 months | All affected parties | Comment resolution log |
| Testing and validation | 3-12 months | 3-10 test laboratories | Validation report |
| Publication | 1-2 months | Editorial staff | Published standard document |
| **Total (typical)** | **15-43 months** | | |

## Standards Categories and Estimated Counts

| Category | Examples | Bootstrap Priority | Estimated Count by Year 50 |
|----------|---------|-------------------|---------------------------|
| Measurement units and calibration | Length, mass, time, temperature | Critical (Year 1-5) | 20-30 |
| Screw threads and fasteners | Metric thread profiles, bolt grades | Critical (Year 10-15) | 15-25 |
| Material grades | Steel, copper, aluminum, ceramics | Critical (Year 10-20) | 30-50 |
| Engineering drawing conventions | Projection, dimensioning, tolerancing | High (Year 5-10) | 5-10 |
| Electrical systems | Voltages, frequencies, wire gauges | High (Year 20-30) | 20-30 |
| Process specifications | Welding, heat treatment, coating | High (Year 15-25) | 20-40 |
| Safety codes | Pressure vessels, electrical, structural | High (Year 20-30) | 15-25 |
| Quality management | Inspection, sampling, SPC | Medium (Year 20-30) | 10-15 |

## Consensus Process Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Minimum working group size | 5 experts | Prevents dominance by single viewpoint |
| Maximum working group size | 15 experts | Beyond this, decision-making becomes too slow |
| Minimum comment period | 3 months | Allows thorough review by busy practitioners |
| Consensus threshold | No sustained opposition | Not majority vote — all significant objections must be resolved |
| Revision cycle | 5-10 years | Frequent enough to stay current, infrequent enough for stability |
| Publication format | Printed document, numbered revision | Enables traceability and reference in contracts |

## Scaling Notes

- **Minimum viable standards body**: 3-5 part-time members managing 10-20 core standards. This is sufficient to cover measurement units, screw threads, basic material grades, and drawing conventions — the standards without which inter-workshop collaboration is impossible.
- **Standards proliferation**: By Year 50, expect 150-250 active standards across all categories. Each standard requires periodic revision (5-10 year cycle), creating ongoing workload proportional to the number of active standards.
- **Enforcement mechanisms**: Without enforcement, standards are voluntary suggestions. Enforcement pathways: (1) government procurement requires compliance, (2) liability for non-compliance in safety-critical applications, (3) quality marks/certification that customers demand. The lightest effective enforcement is preferred — over-regulation stifles innovation.
- **International alignment**: If multiple settlements exist, align standards early. Divergent standards (e.g., different thread profiles) create permanent trade barriers that are expensive to retrofit. Establish inter-settlement standardization agreements before divergence becomes entrenched.

## Troubleshooting

| Problem | Probable Cause | Solution |
|---------|---------------|----------|
| Standards ignored by practitioners | Too complex, not available in workshop, or no enforcement | Simplify to minimum necessary; distribute pocket references; link compliance to procurement |
| Standards outdated | No revision mechanism or revision process stalled | Set mandatory review dates; assign revision responsibility to specific individuals |
| Standards too prescriptive | Over-specification by theoreticians without practical experience | Require working group to include at least 50% active practitioners |
| Standards conflict | Different committees standardize overlapping domains without coordination | Central registry of all standards; cross-reference check during development |
| Standards process too slow | Consensus process deadlocked by competing interests | Time-box discussion periods; escalate unresolved issues to a senior technical authority for binding decision |
| Non-compliant products in market | No testing or certification infrastructure | Build reference testing laboratory; require certification marks for safety-critical products |
| Parts from two workshops don't fit together | Different workshops using different (or no) thread/material standards | Distribute current standard documents; send inspector to verify compliance; manufacture go/no-go gauges for verification |
| Standard documents contradictory | Overlapping standards from different bodies or outdated revision | Cross-reference review committee; mark superseded standards as obsolete; publish consolidated revision |
| Practitioners ignoring standards | Standards unknown, unavailable, or impractical | Audit workshop practices; distribute quick-reference cards; revise standard if genuinely impractical |
| Standards lagging behind technology | Revision cycle too slow or no process for proposing changes | Create formal amendment proposal process; fast-track urgent revisions; set maximum 5-year review cycle |
| Measurement disputes between settlements | Reference standards not calibrated to same master | Establish primary reference standards at central body; issue calibrated secondary standards to settlements; periodic recalibration schedule |
| Standard documents deteriorating | Poor archival storage or insufficient copies | Print on alkaline paper; distribute copies to multiple libraries; see [Information Durability](information-durability.md) |

## Safety

- **Standards as safety infrastructure**: Many safety standards exist because people died from their absence. Pressure vessel codes, electrical codes, structural engineering standards each have body counts behind them. Treat safety standards as non-negotiable minimums, not optional guidelines.
- **Liability framework**: Establish that non-compliance with safety standards creates liability for the producer. This creates market incentive for compliance without requiring a large enforcement bureaucracy.
- **Incident investigation**: When accidents occur, investigate whether the relevant standard was followed, and whether the standard itself was adequate. Root cause analysis may reveal a gap in the standard that needs to be addressed in the next revision.

## Quality Control

- **Compliance testing**: For each material and product standard, define a test method that can be performed by any qualified laboratory. The test method is part of the standard document. Inter-laboratory round-robin testing (same specimen tested by multiple labs) verifies that test results are reproducible across facilities.
- **Reference artifacts**: Physical standards (gauge blocks, thread gauges, surface roughness comparators) provide tangible references that complement written specifications. Distribute reference artifacts to all testing facilities and calibrate them against master references annually.
- **Standard document quality**: Every standard document must be reviewed for clarity, completeness, and absence of ambiguity by at least two reviewers before publication. Ambiguous standards cause more harm than no standard at all.
- **Inter-laboratory comparison**: Periodically distribute identical test specimens to all testing facilities that certify compliance with a given standard. Compare results across facilities. If any facility's results deviate by more than 10% from the median, investigate their testing procedure and equipment calibration. This round-robin testing catches systematic errors in individual laboratories before they cause widespread compliance failures.
- **Appeals process**: When a standard is challenged as technically incorrect or unreasonably burdensome, provide a formal appeals mechanism. The appellant presents technical evidence; the standards body responds with technical counter-evidence. A senior technical panel (not the original working group) renders a binding decision. This process prevents standards from becoming fossilized errors.


## De Facto Standards (Market-Driven)

When one manufacturer's design dominates the market, it becomes a de facto standard regardless of any formal process. Example: the QWERTY keyboard layout. Fast to emerge, but may not be technically optimal. Acceptable as a transitional measure while formal standards are developed.

## Regulatory Standards (Government-Imposed)

Government mandates compliance with specific standards, typically for safety. Effective enforcement but risks political capture (standards written to favor incumbents). Best for safety-critical domains where market forces alone are insufficient.

## Industry Consortium Standards

A group of producers in the same industry agrees on common specifications. Faster than government standards, but may exclude smaller producers from the process. Requires anti-monopoly safeguards.

## Bootstrapping Priority Order

The first standards to develop, in order of criticality:

1. **Length standard** (Year 1-5): A physical reference bar and a defined unit of length. Without this, no two measuring instruments agree.
2. **Mass standard** (Year 1-5): A physical reference weight and defined unit of mass.
3. **Screw thread standard** (Year 10-15): Thread profile, pitch, and tolerance classes. Enables interchangeable fasteners — the single most impactful interoperability standard.
4. **Material grade standards** (Year 10-20): Steel grades by composition and mechanical properties. "Mild steel" must mean the same thing in every foundry.
5. **Drawing convention standard** (Year 5-10): Projection method, dimensioning style, line types, title block format. Enables inter-workshop drawing exchange.
6. **Electrical standards** (Year 20-30): Voltage levels, frequency, wire gauge, connector pinouts. Required once electrification begins.
7. **Safety codes** (Year 20-30): Pressure vessel codes, structural loading, electrical installation safety. Required before complex infrastructure.

## Standards Document Structure

Every published standard document follows a consistent structure for readability and reference:

1. **Identification**: Standard number, title, revision letter, date of publication, issuing body.
2. **Scope**: What the standard covers and what it does not cover. Defines the boundaries clearly.
3. **Normative references**: Other standards that are referenced and required for application of this standard.
4. **Definitions**: Technical terms used in the standard, defined precisely. Ambiguous terms are the enemy of clear standards.
5. **Requirements**: The actual specifications — dimensional limits, composition ranges, performance criteria. Organized by topic or test method.
6. **Test methods**: How to verify compliance with each requirement. Must be reproducible — any qualified tester following the method should get the same result.
7. **Marking and labeling**: How compliant products are identified. What information must appear on the product or its packaging.
8. **Annexes**: Supplementary information (informative, not normative) — examples, calculation methods, rationale for specific requirements.

## Historical Precedent: Whitworth Thread Standard

Joseph Whitworth's 1841 proposal for a unified screw thread standard (55° thread angle, constant pitch-to-diameter ratio) illustrates the bootstrap value of standards. Before Whitworth, every British workshop used its own thread profiles — bolts from one factory would not fit nuts from another. Whitworth's standard was adopted voluntarily by major manufacturers because it reduced costs (no need to stock multiple thread-cutting tools) and enabled inter-company trade. Within 20 years, the Whitworth thread became the de facto British standard, later formalized as BS 84. The lesson: the economic value of interoperability drives voluntary adoption when the standard is technically sound.

## Metric System as Foundation Standard

The metric system (SI units) is the single most impactful standard for a bootstrap civilization. Define the meter, kilogram, second, kelvin, ampere, and mole as the base units. Derive all other units from these (Newton = kg·m/s², Joule = N·m, Watt = J/s, Pascal = N/m²). The decimal structure (prefixes: milli-, centi-, kilo-, mega-) eliminates conversion arithmetic that plagues imperial systems. Adopt SI exclusively — do not maintain dual systems, as conversion errors between systems are a persistent source of engineering mistakes.

## Bootstrapping Approach

In a bootstrap context, the standards body starts with the minimum set that enables inter-workshop collaboration and expands as the civilization's technological complexity grows. Priority order: measurement units → screw threads → material grades → drawing conventions → electrical standards → safety codes.

## Standards Compliance Marking

Products that comply with a standard should carry a compliance mark — a symbol, stamp, or label indicating the standard number and certifying body. Compliance marks enable purchasers to verify quality without testing every item themselves. The mark must be difficult to forge (use a registered die stamp or watermarked paper for certificates). Unauthorized use of the compliance mark is treated as fraud.

## Standards Discovery and Access

A standard that practitioners cannot find or read is useless. Ensure every published standard is:
- Cataloged in a central registry with subject index, standard number, and revision date.
- Available in physical copy at every major workshop and library.
- Summarized in a quick-reference card (single sheet, both sides) for the most commonly referenced standards (thread sizes, material grades, drawing conventions).
- Taught as part of [Education Pathways](education-pathways.md) so practitioners know standards exist and how to look them up.

## See Also

- [Writing & Record-Keeping](writing.md) — the documentation foundation for standards
- [Printing & Book Production](printing.md) — distribution of standard documents
- [Technical Drawing](technical-drawing.md) — drawing conventions are a key early standard
- [Measurement](../measurement/precision-metrology.md) — measurement standards are the most fundamental category
- [Education Pathways](education-pathways.md) — teaching standards to new practitioners
- [Information Durability](information-durability.md) — preserving standards documents across generations
- [Quality Control](../quality-control/index.md) — the quality management systems that standards enable

---

*Part of the [Bootciv Tech Tree](../index.md) • [Knowledge Preservation & Education](./index.md) • [All Domains](../index.md)*
