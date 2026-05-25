# F3: Link Integrity + Site QA Report

**Date**: 2026-05-24
**Tool**: python3 /tmp/check-links.py + manual verification
**Scope**: All 7,318 .md files under docs/ (221 content + 7,097 glossary)

## Summary

| Metric | Count |
|--------|-------|
| Files scanned | 7,318 |
| Total links found | 6,719 |
| Skipped (external/refs) | 3 |
| Links checked | 6,716 |
| **Broken links** | **45** |
| Orphaned pages | 6 |
| Anchor errors | 0 |

## Broken Links — T15 Expanded Files (6)

These 6 broken links are in See Also sections added during T15 expansion. They reference forward-looking articles not yet written:

| File | Line | Target | Notes |
|------|------|--------|-------|
| `energy/electrode-manufacturing.md` | 218 | `../chemistry/carbon.md` | Carbon materials article not yet created |
| `energy/wind.md` | 213 | `../chemistry/hydrogen.md` | Hydrogen production article not yet created |
| `machine-tools/bearings-abrasives.md` | 212 | `./measurement.md` | Measurement article not yet created |
| `machine-tools/forming.md` | 224 | `../metals/metallurgy.md` | Metallurgy article not yet created |
| `machine-tools/machining.md` | 224 | `./measurement.md` | Same missing measurement.md |
| `transport/telegraph.md` | 222 | `../metals/nonferrous.md` | Nonferrous metals article not yet created |

**Recommendation**: These are valid cross-domain references to planned articles. Either create the target articles or temporarily remove the broken links.

## Broken Links — Pre-Existing (39)

### Missing domain index pages (9 links from 3 domains)

| Domain | Missing Index | References |
|--------|---------------|------------|
| `electronics/` | `index.md` | 6 references from assembly.md, electrical-systems.md, measurement/electrical-instruments.md |
| `chemicals/` | `index.md` | 3 references from acids-bases.md, water-treatment.md |

### Missing content articles (30 links across 15 files)

| Missing File | Referenced From |
|-------------|-----------------|
| `machine-tools/measurement.md` | bearings-abrasives.md, machining.md |
| `machine-tools/power-transmission.md` | leather.md (×2) |
| `machine-tools/cutting-tools.md` | refractory-metals.md (×2) |
| `chemistry/sulfuric-acid.md` | zinc.md (×2) |
| `vlsi-scaling/cleanrooms.md` | wafer-production.md (×2) |
| `semiconductors/index.md` | sem-tech-hydroponics.md |
| `chemistry/nitrates.md` | animal-husbandry.md |
| `chemistry/catalysts.md` | acids-bases.md |
| `glossary/cathodes.md` | sem-tech-electrodialysis.md |
| `chemistry/cvd.md` | assembly.md |
| `materials/ceramics.md` | assembly.md |
| `energy/photovoltaics.md` | electrical-systems.md |
| `machine-tools/cnc.md` | electrical-systems.md |
| `transport/ice.md` | refining.md |
| `chemistry/petrochemicals.md` | refining.md |
| `foundations/roads.md` | refining.md |
| `electronics/vacuum-tubes.md` | advanced-glassblowing.md |
| `chemistry/lab-equipment.md` | advanced-glassblowing.md |
| `energy/solar-thermal.md` | health/water-treatment.md |
| `metals/metallurgy.md` | forming.md |
| `foundations/paper-making.md` | leather.md |
| `foundings/textiles.md` | leather.md (typo: foundings→foundations?) |
| `chemistry/radiation-safety.md` | refractory-metals.md |
| `metals/superalloys.md` | refractory-metals.md |
| `energy/batteries.md` | zinc.md |
| `foundations/navigation.md` | light-aircraft.md |
| `foundations/education.md` | light-aircraft.md |
| `energy/engines.md` | light-aircraft.md |

## Orphaned Pages (6)

Pages with zero incoming links from any other .md file:

| File | Notes |
|------|-------|
| `docs/animals/animal-husbandry.md` | Not linked from animals/index.md or any other page |
| `docs/glass/advanced-glassblowing.md` | Not linked from glass/index.md or any other page |
| `docs/metals/refractory-metals.md` | Not linked from metals/index.md or any other page |
| `docs/silicon/wafering.md` | Not linked from silicon/index.md or any other page |
| `docs/supporting/schema-spec.md` | Supporting/meta file, likely not content-linked |
| `docs/transport/light-aircraft.md` | Not linked from transport/index.md or any other page |

## Glossary Integrity

- 7,097 glossary entry files in `docs/glossary/`
- `data/glossary-raw.json` contains extracted terms
- 1 glossary link broken: `docs/chemistry/sem-tech-electrodialysis.md:22` → `../glossary/cathodes.md` (file missing)
- No systematic glossary-to-article linking was found — glossary entries appear to be standalone term definitions

## Recommendations

1. **Priority 1 — Create missing domain indexes**: `electronics/index.md` and `chemicals/index.md` (9 broken links)
2. **Priority 2 — Create high-reference-count articles**: `measurement.md` (4 refs), `sulfuric-acid.md` (2), `power-transmission.md` (2), `cutting-tools.md` (2), `cleanrooms.md` (2)
3. **Priority 3 — Link orphaned pages**: Add the 6 orphaned content pages to their respective domain index.md files
4. **Priority 4 — Fix typo**: `leather.md` links to `foundings/textiles.md` (should be `foundations/textiles.md` or correct path)
5. **Priority 5 — T15 forward references**: Create or remove the 6 forward-reference links added in T15 expansion

## Files NOT Modified

This was a READ-ONLY audit. No files were created, modified, or deleted.
