# Article QA Checklist

> **Purpose**: Companion document to [`content-template.md`](content-template.md). Use this checklist to verify that an expanded capability article meets the workshop-manual standard. Every item here maps to a requirement defined in the content template.
> **Scope**: Content quality only. Data integrity (DAG, edge types, node ID format, tag vocabularies, taxonomy, glossary) is handled by `validate.sh`. Do not duplicate those checks here.
> **Audience**: QA agents and human reviewers evaluating expanded articles.

---

## How to Use This Checklist

1. Open the article under review and the [`content-template.md`](content-template.md) side by side.
2. Determine the article's **format variant** (Physical-Process, Conceptual/Organizational, Biological/Agricultural, or Informational/Knowledge) by reading the Overview section.
3. Work through the **Mandatory for ALL Articles** section first. Every item must pass.
4. Then work through the **format-specific** requirements for the identified variant.
5. Tally results using the **Scoring Rubric** at the end.

---

## Mandatory for ALL Articles

These 13 items apply to every expanded capability file, regardless of format variant.

### M1. Blockquote metadata header present and complete

**Requirement**: The file opens with a blockquote metadata block containing all seven fields: Node ID, Domain, Dependencies, Enables, Timeline, Outputs, Critical.

**How to verify**:
- Look at the first blockquote in the file (lines starting with `>`).
- Confirm each field is present: `> **Node ID**:`, `> **Domain**:`, `> **Dependencies**:`, `> **Enables**:`, `> **Timeline**:`, `> **Outputs**:`, `> **Critical**:`.
- Confirm no YAML frontmatter exists (no `---` delimited block at the top with `key: value` pairs).
- Confirm the Domain field links to the domain index (e.g., `[Domain Name](./index.md)`).

**Pass**: All seven fields present, blockquote format, no YAML frontmatter.
**Fail**: Missing field(s), YAML frontmatter present, or wrong format.

### M2. Dependencies and Enables fields contain relative Markdown links

**Requirement**: Both the Dependencies and Enables fields in the metadata header list other capabilities as relative Markdown links, not bare text.

**How to verify**:
- Check the `> **Dependencies**:` line. Every capability listed should be wrapped in a Markdown link: `[`name`](../path/to/file.md)`.
- Check the `> **Enables**:` line the same way.
- If either field says "None" or is empty, that is acceptable (some leaf or root nodes have no dependencies/enables).

**Pass**: Every listed capability in both fields is a Markdown link, or the field is legitimately empty.
**Fail**: Bare capability names without links (e.g., `charcoal production` instead of `[charcoal production](../energy/charcoal.md)`).

### M3. All prerequisite and BOM items are linked to tech tree articles

**Requirement**: Every item listed in Prerequisites (Section 2) and Bill of Materials (Section 3) that refers to another capability or material source in the tech tree must be a working relative Markdown link.

**How to verify**:
- Scan the Prerequisites section. Each material, tool, or infrastructure item that corresponds to a tech tree node should be linked: `[Iron production](../metals/iron-steel.md)`.
- Scan the BOM table. The Source column should contain links to capability docs.
- A few items may genuinely not have their own capability doc (e.g., "water" or "manual labor"). Those are acceptable as bare text. But if a named process, material, or technology appears unlinked, it fails.

**Pass**: Every referenceable tech tree item is linked.
**Fail**: Named capabilities or material sources appear as bare text that should be links.

### M4. At least 200 lines of content

**Requirement**: The article body (excluding the blockquote metadata header and the footer navigation link) is at least 200 lines.

**How to verify**:
- Count total file lines.
- Subtract the metadata blockquote lines (typically 6-8 lines).
- Subtract the footer section (typically 2-3 lines: the `---` separator and the navigation line).
- The remaining body must be 200 lines or more.

**Pass**: Body is 200+ lines.
**Fail**: Body is under 200 lines.

### M5. At least one quantitative table with real numbers and units

**Requirement**: The article contains at least one table with measured values and their units (temperatures, pressures, yields, ratios, speeds, tolerances, or comparable operating data).

**How to verify**:
- Scan for Markdown pipe tables (`| header | header |`).
- Confirm at least one table contains numerical values with units (e.g., `400-600°C`, `11-13 MWh`, `20-35%`, `10-15 mm`).
- Tables with only qualitative labels (e.g., "Good", "Variable") in every cell do not count, unless at least some cells have numbers with units.

**Pass**: At least one table has real numerical data with units.
**Fail**: No tables, or all tables contain only text/qualitative values with no numbers and units.

### M6. Cross-references to at least two other capability docs

**Requirement**: The article body (not just the metadata header) links to at least two other capability docs in the project using relative Markdown links.

**How to verify**:
- Search the article body (below the metadata header, above the footer) for relative Markdown links of the form `[text](../some-path/file.md)`.
- Count distinct capability doc links. Links to `index.md` files count. Links to the same file multiple times count as one.
- The count must be at least 2.

**Pass**: Two or more distinct internal capability links in the body.
**Fail**: Fewer than 2 internal links in the body.

### M7. Safety section with specific hazards

**Requirement**: The Safety section (Section 8) names specific hazards with concrete details: named chemicals, temperatures, voltages, concentrations, or mechanical dangers. It does not contain only generic warnings like "be careful" or "use proper safety equipment."

**How to verify**:
- Locate the `## Safety` section.
- Confirm it names at least one specific hazard (e.g., "CO is colorless, odorless, lethal at 0.1% in air for 1 hour" rather than "toxic gases may be present").
- Confirm PPE recommendations specify ratings or standards (e.g., "N95 or better respirator" rather than "wear a mask").
- If the process genuinely has minimal hazards, a brief statement explaining why is acceptable.

**Pass**: Named hazards with specific details (substance, temperature, voltage, concentration, etc.).
**Fail**: Only generic safety advice with no specifics tied to the actual process.

### M8. Each Process Description subsection has Strengths (2+ items)

**Requirement**: Every subsection within Process Description (Section 4) that covers a distinct method, type, or variant includes a Strengths list with at least 2 bullet items.

**How to verify**:
- Identify all subsections (### headings) under `## 4. Process Description`.
- For each subsection, look for a "Strengths" or "Advantages" section.
- Count the bullet items. Must be 2 or more.
- If Process Description has no subsections (single method), the section as a whole must still list Strengths.

**Pass**: Every subsection has Strengths with 2+ items.
**Fail**: Any subsection missing Strengths, or Strengths with fewer than 2 items.

### M9. Each Process Description subsection has Weaknesses (2+ items)

**Requirement**: Every subsection within Process Description (Section 4) that covers a distinct method, type, or variant includes a Weaknesses list with at least 2 bullet items.

**How to verify**:
- Same procedure as M8, but looking for "Weaknesses" or "Limitations."
- Must be 2 or more bullet items per subsection.

**Pass**: Every subsection has Weaknesses with 2+ items.
**Fail**: Any subsection missing Weaknesses, or Weaknesses with fewer than 2 items.

### M10. Sub-sections are self-contained

**Requirement**: No subsection within Process Description uses phrases like "same as above," "same as Type N," "see previous section for calibration," or similar cross-references to other subsections. Each subsection must stand alone as a complete reference.

**How to verify**:
- Read each subsection under `## 4. Process Description`.
- Search for phrases: "same as," "see above," "see previous," "as described in," "identical to," "similar to [Type/Method]" when used to avoid repeating content.
- Each subsection must contain its own prerequisites list, materials list, procedure steps, calibration/verification, and performance specs (where applicable per format variant).
- Cross-references to shared prerequisite docs via links are fine. The prohibition is on referencing content *within the same article* in lieu of repeating it.

**Pass**: Every subsection is self-contained with no internal cross-references.
**Fail**: Any subsection defers to another subsection for essential information.

### M11. No AI-slop patterns

**Requirement**: The article avoids AI-generated writing patterns. Specifically absent:
- Vague qualifiers without specifics: "important," "crucial," "it should be noted," "it is important to note that," "generally speaking," "in most cases"
- Generic filler paragraphs that can be removed without losing information
- Unitless numbers where a unit is expected
- Marketing language or promotional tone
- Phrases like "delve," "leverage," "utilize" (when "use" works), "in order to" (when "to" works), "facilitate" (when "help" or "enable" works)

**How to verify**:
- Search for the phrases listed above.
- Flag any paragraph that restates the obvious without adding information.
- Check that every number in a quantitative context has a unit.
- Verify the tone is direct and specific, like a workshop manual, not a product brochure.

**Pass**: No AI-slop patterns detected.
**Fail**: AI-slop patterns present. Note the specific instances in the review.

### M12. Footer navigation link present

**Requirement**: The file ends with the standard footer navigation link in this exact format:
```
---
*Part of the [Bootciv Tech Tree](../index.md) • [Domain Name](./index.md) • [All Domains](../index.md)*
```

**How to verify**:
- Scroll to the last lines of the file.
- Confirm a `---` separator followed by a line starting with `*Part of the`.
- Confirm the three links are present: `../index.md`, `./index.md`, `../index.md`.
- The domain name in the middle link should match the article's domain.

**Pass**: Footer present with correct format and links.
**Fail**: Footer missing, malformed, or using wrong format.

### M13. All internal links resolve

**Requirement**: Every relative Markdown link in the article (`[text](../path/to/file.md)`) points to a file that actually exists on disk.

**How to verify**:
- Extract all relative link targets from the article.
- For each target, check whether the file exists at the resolved path (relative to the article's directory).
- Anchor links (e.g., `#section-name`) appended to file paths are acceptable; verify the file exists and ignore the anchor portion.

**Pass**: All internal links point to existing files.
**Fail**: Any link target does not exist. List the broken links in the review.

---

## Format-Specific Requirements

After completing the mandatory checklist, apply the requirements for the article's format variant. The variant is determined by the subject matter:

- **Physical-Process**: Building, operating, or maintaining a physical process or device. Default variant.
- **Conceptual/Organizational**: Frameworks, decision criteria, organizational systems.
- **Biological/Agricultural**: Living organisms, cultivation, species-specific processes.
- **Informational/Knowledge**: Reproducing, preserving, or transmitting information.

If unsure, use Physical-Process. Some articles span multiple variants. In that case, apply the dominant variant's requirements and note any gaps from the secondary variant.

### Physical-Process (Workshop Manual)

| # | Requirement | How to verify |
|---|-------------|---------------|
 | P1 | **Numbered construction steps** with dimensions and tolerances | Look under `## 4. Process Description`. Each method subsection should have a numbered list (1. 2. 3.) of steps. Steps should include measurable specs: "Cut rod to 200 mm length, ±2 mm tolerance." |
 | P2 | **Calibration or verification procedure** | Each method subsection describes how to test that the built item or process works correctly. Should be numbered steps with reference standards or expected readings. |
 | P3 | **Expected accuracy or performance** stated with units | Each method subsection states quantitative performance: "Expected accuracy: ±2°C between 0-100°C." Not just "accurate" or "good performance." |
 | P4 | **Materials list with specifications** | Each method subsection lists materials with grades, purity, dimensions, or other specs: "Copper wire, 0.5 mm diameter, >99.5% purity." Not just "copper wire." |

### Conceptual/Organizational

| # | Requirement | How to verify |
|---|-------------|---------------|
 | C1 | **Decision criteria or framework** clearly stated | The article defines explicit criteria for making choices: "Use Method A when X < 50 units/day; use Method B when X > 50 units/day." Not just descriptions of methods without guidance on when to pick each. |
 | C2 | **Implementation steps** (not construction steps) | Process Description contains actionable steps for putting the framework or system into practice. These are organizational actions, not physical building steps. |
 | C3 | **Trade-offs table or comparison** | A table or structured comparison that weighs alternatives against each other on key metrics: cost, complexity, speed, scalability, etc. |

### Biological/Agricultural

| # | Requirement | How to verify |
|---|-------------|---------------|
 | B1 | **Species-specific data** with yield, timing, and conditions | Tables or structured data for specific species: yield per hectare, growing season length, temperature range, soil pH requirements. Not just "this crop grows well in warm climates." |
 | B2 | **Cultivation or management procedure** with seasonal calendar | Step-by-step procedure covering the full growth cycle: planting, maintenance, harvest, post-harvest. Includes timing (weeks/months), not just generic steps. |
 | B3 | **Scale estimates** per unit area or per animal | Quantitative estimates of output at known scales: "1 hectare produces 3-5 tonnes grain under rain-fed conditions." Not just "scales well." |

### Informational/Knowledge

| # | Requirement | How to verify |
|---|-------------|---------------|
 | I1 | **Reproduction or copying procedure** | Step-by-step instructions for how to reproduce or copy the information: carving, printing, photographing, digitizing, etc. |
 | I2 | **Material requirements for the medium** | Specifications for the physical medium: paper quality, ink composition, storage container material, etc. With quantities and specs where applicable. |
 | I3 | **Preservation and storage methods** | How to preserve the information-bearing artifact over time: environmental conditions, handling procedures, expected lifespan. |
 | I4 | **Quality metrics for output** | Measurable quality criteria: legibility, error rate per 1000 characters, resolution in dpi, durability in years under stated conditions. |

---

## Scoring Rubric

### PASS

All 13 mandatory items (M1-M13) pass, AND all format-specific items for the identified variant pass.

The article meets the workshop-manual standard defined in [`content-template.md`](content-template.md). No changes required.

### CONDITIONAL

1-2 mandatory items fail, OR 1 format-specific item fails, AND no critical item fails.

Critical items: M3 (linking), M7 (safety), M11 (no AI-slop), M13 (link resolution).

The article is close to the standard. List the specific failures in the review with instructions for remediation. A follow-up pass is needed but the article does not need a full rewrite.

### FAIL

3 or more mandatory items fail, OR any critical item fails (M3, M7, M11, M13), OR 2+ format-specific items fail.

The article does not meet the standard. Provide a detailed review listing all failures with remediation guidance. The article requires substantial revision before it can pass QA.

---

## Verification Checklist Template

Copy this template into your review. Mark each item.

```
Article: [filename]
Format variant: [Physical-Process / Conceptual / Biological / Informational]
Date: [YYYY-MM-DD]

## Mandatory Items

- [ ] M1: Metadata header complete (7 fields, blockquote format)
- [ ] M2: Dependencies/Enables contain Markdown links
- [ ] M3: All prerequisite/BOM items linked
- [ ] M4: 200+ lines of body content
- [ ] M5: Quantitative table with numbers and units
- [ ] M6: 2+ cross-references to capability docs in body
- [ ] M7: Safety section with specific hazards
- [ ] M8: Each subsection has Strengths (2+)
- [ ] M9: Each subsection has Weaknesses (2+)
- [ ] M10: Sub-sections self-contained (no "same as above")
- [ ] M11: No AI-slop patterns
- [ ] M12: Footer navigation link present
- [ ] M13: All internal links resolve

## Format-Specific Items

[Physical-Process]
- [ ] P1: Numbered construction steps with dimensions/tolerances
- [ ] P2: Calibration/verification procedure
- [ ] P3: Expected accuracy/performance with units
- [ ] P4: Materials list with specifications

[Conceptual/Organizational]
- [ ] C1: Decision criteria or framework stated
- [ ] C2: Implementation steps (not construction)
- [ ] C3: Trade-offs table or comparison

[Biological/Agricultural]
- [ ] B1: Species-specific data (yield, timing, conditions)
- [ ] B2: Cultivation procedure with seasonal calendar
- [ ] B3: Scale estimates per unit area or per animal

[Informational/Knowledge]
- [ ] I1: Reproduction/copying procedure
- [ ] I2: Material requirements for the medium
- [ ] I3: Preservation/storage methods
- [ ] I4: Quality metrics for output

## Result

Score: [PASS / CONDITIONAL / FAIL]
Notes: [any details on failures or conditional items]
```

---

*Part of the [Bootciv Tech Tree](../index.md) • [Supporting Docs](./) • [All Domains](../index.md)*
