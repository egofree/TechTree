# Libraries & Information Systems

> **Node ID**: knowledge.libraries
> **Domain**: [Knowledge Preservation & Education](./index.md)
> **Dependencies**: [`knowledge.education`](education.md), [`knowledge.writing`](writing.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 10-200+
> **Outputs**: libraries
> **Critical**: Yes — a library is the institutional memory of a civilization; without organized storage and retrieval, accumulated knowledge becomes inaccessible

## Prerequisites

- **Materials**: Paper, ink, binding materials from [Printing](printing.md); shelving lumber (oak, ash) or steel angle-iron; acid-free folders and boxes for archival storage
- **Tools**: [Writing](writing.md) instruments for catalog cards, measuring tools for environmental monitoring (thermometers, hygrometers), basic woodworking tools for shelving
- **Knowledge**: [Writing](writing.md) for documentation and cataloging, [Education](education.md) for trained librarians, classification system design
- **Infrastructure**: Fireproof building (stone or brick walls, minimum 300 mm thick), climate-controlled storage (18-22°C, 40-55% RH), reading room (minimum 6 m × 8 m)

## Bill of Materials

| Material | Quantity per 5,000-volume library | Source | Alternatives |
|----------|----------------------------------|--------|-------------|
| Shelving (oak) | 500-800 linear meters | Forestry + [Machine Tools](../machine-tools/index.md) | Steel angle-iron (heavier, requires welding) |
| Card stock (catalog) | 10,000-15,000 cards | [Printing](printing.md) | Ledger-bound catalog (less flexible) |
| Acid-free folders | 2,000-5,000 | [Chemistry](../chemistry/index.md) (alkaline paper) | Regular folders (acid migration degrades contents) |
| Environmental monitors | 4-8 hygrometers + thermometers | [Measurement](../measurement/index.md) | Hair-tension hygrometer (less precise) |
| Binding repair materials | Japanese tissue, wheat starch paste, linen thread | [Textiles](../textiles/fibers.md), [Agriculture](../agriculture/index.md) | Standard paper patches (less durable) |
| Fire suppression equipment | Sand buckets, water pumps, CO₂ extinguishers | [Chemistry](../chemistry/index.md) | Water buckets only (limited effectiveness) |

## Process Description

### Library Construction

**Building design**:
- **Structural requirements**: Load-bearing masonry walls (stone or brick, minimum 300 mm thick). Reinforced concrete or vaulted ceiling for fire resistance. Iron or steel framing for multi-story stacks. Floor loading: books average ~1 kg each; full shelving runs 200-300 kg per linear meter — design floors for 5-7 kN/m² minimum.
- **Climate control**: Maintain 18-22°C and 45-55% relative humidity. Passive methods: thick walls for thermal mass, earth-sheltered construction (stable ground temperature ~10-15°C), ventilated stack aisles. Active methods: steam-heated radiators for heating, evaporative cooling or compressor-based dehumidifiers for humidity. Install hygrometers (hair-tension or wet-bulb type) and thermometers at multiple points; log readings daily.
- **Lighting**: Natural light via north-facing clerestory windows (diffuse, no direct UV). Oil lamps for early libraries — enclosed glass-body lamps reduce fire risk. Electric lighting: incandescent bulbs, low UV output, positioned to avoid heat buildup near shelves.
- **Fire protection**: No open flames, no combustible finishes on walls or ceilings. Lightning rod (copper strip to ground). Sand buckets and water pumps at each floor. Fire doors (iron-clad wood or solid iron). Stone or tile floors only — no wood in stack areas.

**Strengths**:
- Masonry construction (300 mm stone or brick) provides natural fire resistance and thermal mass — thick walls damp daily temperature fluctuations without powered climate control
- Floor loading design at 5-7 kN/m² accommodates dense book storage — 200-300 kg per linear meter of shelving is supported without structural concern
- Passive climate methods (earth-sheltered construction, thermal mass) work without electricity — viable at the earliest stages of library construction

**Weaknesses**:
- Fireproof construction requires stone or brick — wood-frame buildings (cheaper, faster to build) are unacceptable for library use due to fire risk
- Maintaining 18-22°C and 45-55% RH requires either thick passive-design walls or active climate control systems — both add significant cost
- North-facing clerestory windows for natural light require specific building orientation and taller walls — constrains site selection

### Shelving & Storage

**Shelf design**:
- **Wooden shelving**: Dressed hardwood (oak, ash) boards, 20-25 mm thick, 200-250 mm deep, spans up to 900 mm between uprights. Uprights: 50×75 mm posts with routed dadoes for adjustable shelf placement at 25 mm increments. Back panel prevents items falling behind. Load test each shelf to 50 kg before committing to layout. A well-built oak shelf holds approximately 200 kg of books safely. Coat with linseed oil or wax to prevent moisture absorption — raw wood warps in humid conditions.
- **Steel shelving**: Angle-iron uprights with clip-in shelf brackets. Thinner shelves (1.5 mm sheet steel) hold more weight per unit than wood. Corrosion-resistant paint or galvanized finish. Steel conducts heat faster than wood — avoid placing steel shelves against exterior walls in cold climates (condensation risk on books).
- **Aisle width**: Minimum 900 mm for single-person access, 1200 mm for two-way traffic or cart passage. Main aisles: 1500 mm minimum to accommodate book carts and allow two people to pass comfortably.
- **Compact storage**: For high-density archival storage, use sliding (mobile) shelving on floor rails — halves the aisle space required. Floor must be dead-level (self-leveling compound or precision-shimmed rails) — any slope causes mobile shelving to drift.

**Strengths**:
- Adjustable wooden shelving (dadoes at 25 mm increments) accommodates books of all sizes — the same uprights serve for folio volumes, octavo books, and pamphlet boxes
- Oak shelving holds 200 kg per shelf safely — sufficient for dense book storage without sagging over decades
- Mobile shelving halves the aisle space required, effectively doubling storage capacity in a given floor area

**Weaknesses**:
- Wooden shelving requires periodic maintenance (linseed oil or wax treatment) — raw wood warps in humid conditions
- Steel shelving conducts heat faster than wood — placing steel shelves against exterior walls in cold climates causes condensation on books
- Minimum 900 mm aisle width for access plus 1500 mm for main aisles means only ~50% of floor area is usable shelving space

### Library Classification Systems

**[Dewey Decimal Classification](../glossary/dewey-decimal-classification.md)** (Melvil Dewey, 1876):
- Organizes all knowledge into ten main classes, each subdivided decimally: 000 Computer science/information/general works, 100 Philosophy/psychology, 200 Religion, 300 Social sciences, 400 Language, 500 Pure science, 600 Technology/applied science, 700 Arts/recreation, 800 Literature, 900 History/geography. Subdivision by additional digits: 540 = Chemistry, 546 = Inorganic chemistry, 546.3 = Specific elements. For a bootstrap technical library, classes 500-600 are the most densely populated. The system is simple to implement and well-suited for collections under 100,000 volumes.

**[Library of Congress Classification](../glossary/library-of-congress-classification.md)** (developed 1897-1901):
- Uses alphanumeric notation: single or double letters for main classes (T = Technology, TA = Engineering, TF = Railroad engineering), followed by numbers for subdivision, then a Cutter number (derived from author name) for shelf order. Example: TA405 .C35 = Structural engineering, author with surname starting "Ca". More expressive than Dewey for large, specialized collections — accommodates millions of unique shelf positions. Preferred for research libraries and collections exceeding 100,000 volumes.

**[Purpose-built technical classification](../glossary/purpose-built-technical-classification.md)** (for bootstrap context):
- Top-level divisions: 100 Mathematics, 200 Physics, 300 Chemistry, 400 Materials, 500 Engineering (Mechanical), 600 Engineering (Electrical), 700 Mining & Metallurgy, 800 Manufacturing, 900 Reference (dictionaries, indexes, standards). Subdivide with decimal notation (e.g., 310.5 = Inorganic Chemistry → Electrochemistry).
- Each book receives a class mark (e.g., "510.2 CLA" = Mechanical Engineering, Bearings, author Clarke). Print class mark on spine label and title page.

### Cataloging Practices

**Card catalog**:
- Three card trays per collection: author alphabet, title alphabet, subject index. Each card: 75×125 mm card stock, handwritten or typeset. Fields: author, title, class mark, year, page count, acquisition date, shelf location code.
- **Cross-referencing**: Subject cards list all related class marks. "See also" cards link between subjects (e.g., "Thermodynamics — see also 220 Heat Transfer, 540 Engines"). Maintain a master authority file of approved subject headings to prevent duplication and inconsistency.
- **Accession register**: Bound ledger (or card file) recording every item in acquisition order: accession number, source, date received, cost, class mark, disposition (on shelf / loaned / withdrawn). Running count validates against shelf inventory.
- **Shelflist**: Fourth card file arranged in class mark order — represents the exact physical order of books on shelves. Used for inventory verification (shelf reading): systematically walk the shelves, comparing each book to the shelflist card. Discrepancy = misfiled, missing, or unrecorded item. Conduct full shelf reading annually.

**Descriptive cataloging standards**:
- Record author (last name, first name), full title, edition, place of publication, publisher, year, physical description (pages, illustrations, size), series, subject headings, and notes (translation of, revised edition of, supplements). Standardized format enables any user to identify and locate a specific work from the catalog entry alone. Cross-reference variant forms of author names and titles.

### Archival Storage Conditions

**Temperature and humidity control**:
- **Target range**: Temperature 18-22°C, relative humidity 40-55%. Fluctuation is more damaging than steady-state conditions outside the ideal range — avoid daily swings exceeding ±2°C or ±5% RH. Hygroscopic materials (paper, parchment, leather, glue) expand and contract with humidity changes, causing mechanical stress → cracking, warping, delamination.
- **Monitoring**: Install recording hygrothermographs (drum chart recorders or digital data loggers) at multiple points throughout storage areas — near floor, at shelf height, near ceiling, near exterior walls. Log readings continuously. Review weekly. Investigate any reading outside 16-24°C or 35-60% RH within 48 hours.
- **Passive climate control**: Thick masonry walls (≥400 mm stone or brick) provide thermal mass that damps daily temperature fluctuations. Earth-sheltered or bermed construction leverages stable ground temperature (~10-15°C year-round at 2 m depth). Ventilation: stack effect (low intake vents, high exhaust vents) provides air circulation without powered fans. Dehumidification: calcium chloride or silica gel desiccant trays in enclosed storage areas (regenerate CaCl₂ by heating to 200°C; regenerate silica gel at 120°C for 2 hours).
- **[Active climate control](../glossary/active-climate-control.md)** (when electricity available): Thermostatically controlled heating (electric resistance or steam radiators). Dehumidifier (refrigerant-type — cools air below dew point to condense moisture, then reheats). Humidifier (evaporative pan — needed only in very dry climates or heated winter buildings).

**Light exposure**:
- Ultraviolet light is the primary agent of paper degradation — it breaks cellulose chains (photochemical degradation), causing yellowing, embrittlement, and loss of tensile strength. Keep light exposure below 50 lux (5 foot-candles) for sensitive materials, below 300 lux for general collections. Filter UV from all light sources (UV-absorbing sleeves on fluorescent tubes, UV-filtering glazing on windows). Store most sensitive items (manuscripts, photographs, early printed books) in opaque enclosures — light damage is cumulative and irreversible.

### Preservation Techniques

**Paper and binding care**:
- Store acid-free paper items separately from acidic groundwood paper — acid migrates (accelerated degradation in adjacent materials). Interleave with acid-free buffer sheets (calcium carbonate-impregnated tissue).
- **Leather bindings**: Condition with lanolin-based dressing annually. Keep away from direct light (UV bleaches and cracks leather). **Vellum/parchment**: Maintain above 40% RH — below this, vellum curls and cracks; above 60%, gelatin softens and mold risk rises.
- **Binding repair**: Japanese tissue (kozo fiber) and wheat starch paste for page tears. Re-sew broken signatures with linen thread. Re-back with matching leather or archival cloth. Document all repairs in conservation log.

**[Deacidification](../glossary/deacidification.md)** (for acidic paper, pH below 6):
- Acidic paper (groundwood pulp, alum-rosin sized, produced 1850-1990) self-destructs — the acid catalyzes hydrolysis of cellulose chains, reducing paper strength until it crumbles. Detect with pH indicator pen (chlorophenol red: yellow = acidic pH < 5.5, orange = borderline, blue = neutral/alkaline pH > 6.5).
- **Single-item treatment**: Spray or brush with alkaline buffer solution — magnesium bicarbonate or calcium bicarbonate in water or ethanol. The alkaline reserve neutralizes existing acid and provides ongoing protection. Wei T'o process: non-aqueous deacidification using magnesium methoxide in methanol and fluorocarbon solvent — penetrates paper without wetting or distorting it.
- **Mass deacidification**: For large collections, commercial processes (Bookkeeper, Sabathe) treat hundreds of volumes per day by immersing books in alkaline dispersion. Cost: $10-30 per volume. Requires industrial-scale chemical processing capability.
- **When to deacidify**: Paper with pH below 6 and still flexible (not yet brittle — folding endurance above 20 MIT folds). Brittle paper (below 2 MIT folds) cannot be saved by deacidification — the damage is done. Photograph or microfilm brittle items before they disintegrate.

**Microfilming**:
- **Process**: Photograph pages on 35 mm silver halide film at reduction ratio ~15:1 (one standard microfilm frame holds one page). Develop film (standard black-and-white processing — silver gelatin emulsion). Store master negative in climate-controlled vault (18°C, 30-40% RH). Produce duplicate positive prints for reader use.
- **Capacity**: One 30 m roll of 35 mm microfilm holds approximately 700-1000 pages. A library of 10,000 volumes averaging 200 pages each = 2 million pages = ~2500-3000 rolls of microfilm. Storage: a standard microfilm cabinet drawer holds 30-50 rolls — the entire 10,000-volume library fits in ~60-100 drawers occupying 2-3 m² of floor space.
- **Readers**: Microfilm reader = light source + lens + projection screen. Can be built with early optical manufacturing capability (ground glass lens, incandescent lamp, folding mirror). No electronics required.
- **Longevity**: Silver halide microfilm stored properly lasts 100-500 years. Polyester-base film is more stable than acetate-base (acetate develops "vinegar syndrome" — acetic acid release that destroys the emulsion).

**[Digitization workflow](../glossary/digitization-workflow.md)** (once semiconductor capability exists):
- **Scanning**: Flatbed or planetary scanner (camera mounted above book cradle, face-up capture avoids spine stress). Resolution: minimum 300 dpi for text, 600 dpi for images and maps. Color mode: 24-bit RGB for full reproduction; 8-bit grayscale sufficient for most text.
- **File format**: Master images in TIFF (uncompressed, lossless). Derivative copies in JPEG (lossy, small file) for web access. OCR (optical character recognition) software converts page images to searchable text — accuracy 95-99% for clean printed text, 70-90% for degraded or handwritten materials.
- **Metadata**: Record for each item: title, author, date, page count, scan date, scanner operator, resolution, file format, file size, checksum (MD5 or SHA-256 for integrity verification). Dublin Core metadata standard provides 15 elements for resource description.
- **Storage and backup**: 3-2-1 rule (3 copies, 2 media types, 1 offsite). Format migration every 10-15 years onto current storage technology. Maintain format documentation with every archive.

**Strengths**:
- Deacidification with magnesium bicarbonate extends acidic paper life by 3-5× — a book with 50 years remaining life gains 150-250 years at modest cost
- Microfilming compresses 10,000 volumes (2 million pages) into 60-100 cabinet drawers occupying 2-3 m² — a 1000× space reduction compared to physical books
- Silver halide microfilm on polyester base lasts 100-500 years under proper storage — longer than any digital medium

**Weaknesses**:
- Deacidification only works on paper that is still flexible (pH below 6, folding endurance above 20 MIT folds) — brittle paper cannot be saved
- Microfilm readers require optical manufacturing capability (ground glass lenses, light source) — another dependency for the bootstrap chain
- Digitization at 300-600 DPI produces large files (~50 MB per page uncompressed TIFF) — storage requirements scale quickly for large collections

### Environmental Hazards

**Mold**: Spores activate above 65% RH. Prevention: maintain ventilation (2-4 air changes/hour), use silica gel desiccant canisters in enclosed cases (indicator beads turn from blue to pink when saturated — regenerate at 120°C for 2 hours). If mold appears: isolate affected items, dry thoroughly, brush spores outdoors (wear mask), wipe shelves with 70% ethanol.

**[Insects](../glossary/insects.md)** (silverfish, booklice, beetles): Maintain temperature below 20°C where possible. Cedar lining in storage cabinets repels some insects. Periodic inspection: look for frass (insect droppings), exit holes in wood, feeding damage on paper edges. Freezing treatment: bag item, freeze at -20°C for 72 hours, thaw slowly — kills all life stages without chemicals.

**Disaster recovery**:
- **Water damage**: Freeze wet items within 48 hours to halt mold. Freeze-dry (sublimation under vacuum) or air-dry with fans. Interleave pages with blotting paper, replace as saturated.
- **Fire damage**: Prioritize salvage of unique items. Handle charred material on support boards — do not pick up by edges. Remove soot with dry chemical sponge. Deodorize with activated charcoal in sealed containers.

### Information Retrieval

**Shelf arrangement**: Books shelved by class mark in strict alphanumeric order. Oversize volumes on bottom shelves or separate folio section. Reference section (encyclopedias, dictionaries, standards) shelved near the reading area, not loanable.

**Index and abstract services**:
- Maintain a periodical index: quarterly compilation of new articles by subject, with brief abstracts (2-3 sentences summarizing key findings and methods). Distribute to specialists.
- **Citation index**: Track which works cite which — enables tracing the development of ideas and locating related work across subject boundaries.
- **Controlled vocabulary**: Maintain a standardized list of subject terms (thesaurus) used in indexing. Each concept gets one preferred term (e.g., "iron smelting" not "iron production" or "making iron"). Cross-reference synonyms and related terms. Prevents fragmentation of the literature under variant terminology.

**Physical access systems**:
- **[Closed stacks](../glossary/closed-stacks.md)** (staff retrieves books): Maximum preservation — no public access to shelves, reduced theft risk, controlled environment. Slower access (request → retrieve → read → return). Preferred for rare and archival materials.
- **[Open stacks](../glossary/open-stacks.md)** (browsing): Users access shelves directly. Faster access, encourages discovery. Requires wider aisles, more robust shelving, security measures (exit checks). Preferred for general circulating collections.

**Strengths**:
- Classification systems (Dewey, Library of Congress) provide a proven, systematic arrangement — any user who knows the system can locate any book in any library using the same scheme
- Controlled vocabulary (thesaurus) prevents literature fragmentation — every concept has one preferred term, eliminating confusion from synonyms
- Card catalog with author/title/subject triples provides multiple access paths to the same work — users can find a book by any of three approaches

**Weaknesses**:
- Cataloging is labor-intensive — each item requires 10-30 minutes of professional time for complete descriptive cataloging with subject headings
- Shelf reading (verifying books are in correct order) must be done systematically and annually — misfiled books are effectively lost until the next shelf reading
- Controlled vocabulary requires ongoing maintenance — new technical terms must be added and cross-referenced, or the thesaurus falls behind the literature

### Digital Storage Considerations

Once semiconductor manufacturing is available:
- **[Punched cards](../glossary/punched-cards.md)** (pre-electronic): 80 characters/card, ~150 cards/kg. Robust but extremely low density. Useful as a bridge technology for numerical data.
- **Magnetic tape**: High capacity, 10-30 year reliable lifespan before bit rot demands refresh. Store at 18-22°C, 40-50% RH. Rewind annually to prevent adhesive bleed-through.
- **[Optical media](../glossary/optical-media.md)** (CD-ROM, later DVD): 50-100 year claimed lifespan for gold-reflector discs. Read-only after mastering — immune to accidental overwrite. Requires precise manufacturing tolerances (see Photolithography domain).
- **Migration strategy**: Refresh all digital media every 10-15 years onto current format. Maintain format documentation with every archive. Use open, self-describing formats (plain text ASCII/UTF-8, TIFF for images, CSV for tabular data).

### Library Network & Acquisition

**Interlibrary cooperation**:
- Standardize classification and cataloging across settlements so that any library can locate materials in any other.
- **Loan protocols**: Loan period 30-90 days. Borrowing library responsible for safe transport (waterproof wrapping, rigid container). Track all loans in dispatch register.
- **Duplicate exchange**: Libraries inevitably acquire duplicate copies — exchange surplus for gaps in own collection. Maintain "wants lists" and "duplicates available" lists, circulate quarterly.

**Acquisition priorities for civilization rebuilding**:
1. Survival-critical: Agriculture, medicine, water treatment, shelter construction
2. Industrial bootstrap: Metallurgy, chemistry, energy, machine tools
3. Advanced capability: Electronics, semiconductors, telecommunications
4. Cultural: History, literature, philosophy — preserve but not at the expense of technical works

### Reading Rooms & Physical Layout

**Reading room design**:
- **Dimensions**: Minimum 6 m × 8 m for a small reading room (seats 12-16 readers at individual desks). Larger institutions: reading rooms of 15 m × 20 m or more, accommodating 50+ readers. Ceiling height minimum 3.5 m for natural light penetration and air volume.
- **Seating**: Individual desks (minimum 600 mm × 800 mm work surface) with task lighting (adjustable-angle lamp). Chairs with back support — readers sit for hours. Desk spacing: 1.2 m minimum between desks (elbow room and noise isolation). Sound absorption: cork or fabric wall panels reduce ambient noise in large reading rooms.
- **Reference collection**: Encyclopedias, dictionaries, atlases, standards documents, handbook series shelved along the reading room walls — immediately accessible without going to the stacks. These are the most frequently consulted works and should never be loaned out.
- **Map and drawing storage**: Flat files (plan chests) — wide, shallow drawers (A0 size: 850 mm × 1200 mm, 50 mm deep) for engineering drawings, maps, and architectural plans. Store flat, never rolled (rolling causes cracking and makes retrieval difficult). Label each drawer with content range. Acid-free interleaving tissue between items.

### Library Staffing & Operations

**Staffing requirements**:
- **Librarian**: Trained in classification, cataloging, reference services, and collection management. One librarian per 5,000-10,000 volumes for adequate service levels. The librarian decides acquisition priorities, manages the catalog, trains subordinate staff, and answers research queries.
- **Library assistants**: Shelf-reading (verifying books are in correct order), re-shelving returns, processing new acquisitions (stamping, labeling, pocket insertion for due-date cards), issuing and receiving loans. Ratio: 1-2 assistants per librarian.
- **Conservator**: Book repair, binding maintenance, environmental monitoring, disaster preparedness. A dedicated conservator is justified for collections exceeding 20,000 volumes. For smaller collections, the librarian performs basic repairs (tipping in loose pages, re-attaching detached covers) and contracts major conservation work to specialists.
- ** porter/attendant**: Stack maintenance, climate control monitoring, fire watch, moving heavy materials. Often combined with other duties in small libraries.

**Daily operations**:
- **Opening routine**: Record temperature and humidity readings from all monitoring points. Check for water leaks, mold, pest evidence. Power on lighting. Retrieve any reserved materials from overnight storage.
- **Circulation**: Loan transaction: record borrower name, item title, class mark, loan date, due date in the loan register (bound ledger or card system). Stamp due date on the due-date slip in the book pocket. On return: strike through the loan record, re-shelve. Overdue tracking: review loan register weekly for items past due date. Send reminder notices. After 90 days overdue: declare item lost, begin replacement process.
- **Stack maintenance**: Weekly shelf reading of one section (systematically rotating through the entire collection annually). Straighten shifted books. Remove any items showing mold, insect damage, or water damage for immediate conservation assessment.

### Serial Publications & Periodical Management

**Periodicals in a technical civilization**:
- **Journal structure**: A technical journal publishes research articles, experimental reports, book reviews, and letters at regular intervals (monthly, quarterly, or annually). Each article undergoes peer review — submitted to 1-3 independent experts who evaluate methodology, conclusions, and significance before publication. Peer review is the primary quality filter for technical knowledge.
- **Subscription management**: Maintain a subscription register listing all periodicals received, with subscription date, renewal date, and binding status. Each incoming issue is recorded in the accession register and the periodical index (see Information Retrieval).
- **Binding periodicals**: After a volume year is complete, bind all issues together as a single book. Remove original paper covers, collate issues in order, sew through the fold, bind in cloth or buckram covers with the journal title, volume number, and year stamped on the spine. Bound periodicals are more durable, easier to shelve, and easier to handle than loose issues.
- **Indexing periodicals**: At the end of each volume year, compile a subject and author index for that volume. Bind the index at the front of the bound volume. Additionally, maintain a cumulative index across all volumes of each journal — this enables researchers to locate every article on a given topic published over the journal's entire run.

### Archival Records Management

**Records lifecycle**:
- **Active records**: Documents in regular use — stored in the office or workshop where they are created and consulted. No special preservation measures beyond basic filing (acid-free folders, metal filing cabinets, labeled by subject and date).
- **Semi-active records**: Documents with occasional reference value but not in daily use — transfer to central archive after 1-5 years. Stored in acid-free boxes on shelving. Indexed in the archive catalog. Accessible within 24-48 hours on request.
- **Inactive records**: Documents with permanent historical or legal value — transfer to permanent archive after 10-25 years. Full preservation conditions (climate control, acid-free enclosures). These include: founding documents, property records, major engineering drawings, research notebooks, financial records (for legal accountability periods of 30+ years).
- **Destruction schedule**: Not every document is worth keeping forever. Establish retention schedules: routine correspondence — destroy after 5 years; routine financial records — destroy after 10 years; engineering drawings — retain permanently; research data — retain permanently. Uncontrolled accumulation of records is as much a problem as loss — it buries valuable information in a mass of trivia, making retrieval impossible.

**[Archival organization](../glossary/archival-organization.md)** (original order principle):
- Maintain records in the order created by their originating office — this order carries information about organizational structure and work processes that reorganization destroys. Do not rearrange files by subject (that is the catalog's job, not the shelf arrangement's job). Describe each file unit (folder, box, series) in the finding aid — a structured guide listing: originating office, date range, contents summary, physical extent (number of boxes, linear meters of shelf space), access restrictions.

### Statistical Records & Collection Metrics

**Measuring the library**:
- **Collection size**: Track total volumes, serial subscriptions, map/drawing sheets, microfilm rolls. Annual growth rate (new acquisitions minus withdrawals).
- **Circulation**: Total loans per year, broken down by subject class. Circulation data reveals which subjects are most actively used — guides acquisition priorities. Low-circulation subjects may not need expanded collections.
- **Turnover rate**: Loans ÷ collection size. A healthy circulating collection turns over 0.5-2.0 times per year (each book is borrowed once every 6-24 months on average). Below 0.3 suggests the collection does not meet user needs; above 3.0 suggests the collection is too small for the demand.
- **Fill rate**: Percentage of user requests successfully fulfilled from the collection. Target: 85-95% for a well-developed collection. Below 80% signals gaps requiring acquisition or interlibrary loan.

### Conservation & Book Repair

**[Rebacking](../glossary/rebacking.md)** (restoring a deteriorated spine):
- Remove the old spine material carefully with a thin lifting knife, preserving any spine lettering or decoration. Clean the exposed spine and sewing supports. Reinforce the spine with muslin cloth adhered with pH-neutral PVA (polyvinyl acetate) adhesive, extending the muslin 25-30 mm onto each board to create new hinge material. Reattach the original spine material (if salvageable) over the muslin with PVA, aligning it carefully. Dry under weight (boards and weights or a nipping press) for 24 hours to prevent warping. Rebacking extends the service life of a heavily used binding by 20-50 years.

**Paper repair**:
- **Tears and splits**: Use Japanese tissue (kozo fiber, long-fibered and strong) applied with wheat starch paste (cooked 1:5 starch:water, cooled to thin gel). The tissue bridges the tear with minimal bulk — Japanese tissue can be split to match the thickness of the damaged paper. Feather the edges of the tissue patch to avoid a visible ridge.
- **[Leaf-casting](../glossary/leaf-casting.md)** (for losses — holes and missing areas): Suspend the damaged leaf in a leaf-casting tank filled with paper pulp slurry. Vacuum draws pulp through the hole, depositing fibers that interlock with the original paper edges. The resulting fill matches the thickness and texture of the surrounding paper. Requires specialized equipment but produces nearly invisible repairs.

**[Mass deacidification](../glossary/mass-deacidification.md)** (Wei T'o process):
- Spray or immerse acidic paper items in a solution of magnesium methoxy carbonate in a fluorocarbon or alcohol carrier solvent. The magnesium compound penetrates the paper, neutralizing existing acid and depositing an alkaline reserve (magnesium carbonate) that provides ongoing protection. The treatment raises paper pH to 7.5-9.0 (from acidic pH 4-5), extending paper life by 3-5× — a book with 50 years of remaining life gains 150-250 years. Non-aqueous formulation avoids wetting and distortion of the paper.

### Disaster Recovery Procedures

**Water damage response**:
- Freeze wet items within 48 hours at -20°C to halt mold growth (mold spores germinate above 65% RH, which saturated books reach within 2-3 days). Freezing does not kill mold but stops it from spreading. After freezing, vacuum freeze-dry (sublimation under vacuum at -20°C to -40°C) removes ice as vapor without liquid water passing through the pages — minimizes ink bleeding, paper swelling, and adhesion between pages. Air-drying (fans and interleaved blotting paper) is acceptable for small quantities but causes more physical distortion than freeze-drying.

**Fire damage response**:
- Remove soot with dry cleaning sponges (natural rubber sponges used dry, lifting soot particles without solvents that would drive soot deeper into paper fibers). Work from top to bottom, using light strokes — heavy pressure embeds soot. Follow with ozone treatment for smoke odor: place items in a sealed chamber with an ozone generator (0.5-2.0 ppm ozone concentration) for 24-48 hours. Ozone oxidizes odor compounds but also weakens paper — limit exposure time.

**Priority salvage order**: Manuscripts and unique rare books first (irreplaceable), then reference collections (high use value), then general circulating collection (replaceable by acquisition). Document salvage decisions in the disaster log — record item identifiers, condition assessment, treatment applied, and storage location after recovery.

**Pre-disaster preparedness**: Maintain a prioritized salvage list identifying the most valuable and vulnerable items in the collection, with their shelf locations and handling instructions. Store disaster recovery supplies (freeze-drying equipment contracts, blotting paper rolls, plastic sheeting, fans, portable generators) in an accessible location separate from the library building. Train all staff in the salvage priority order and basic recovery techniques — in the first 48 hours after a disaster, trained responders are more valuable than any equipment.

**Strengths**:
- Freezing wet items within 48 hours halts mold growth — buys time for systematic recovery rather than panicked salvage
- Japanese tissue (kozo fiber) and wheat starch paste repairs are reversible and archival — conservation treatments do not damage the original material
- Pre-disaster preparedness (prioritized salvage list, supplies stored separately) enables rapid, organized response — the first 48 hours determine whether a collection survives

**Weaknesses**:
- Vacuum freeze-drying requires specialized equipment that may not exist in a bootstrap context — air-drying causes more distortion and ink bleeding
- Ozone treatment for smoke odor weakens paper — the treatment itself causes damage, forcing a trade-off between odor removal and paper strength
- Mass deacidification (Wei T'o process) requires industrial-scale chemical processing — unavailable until chemical manufacturing reaches moderate capability

---

### Cross-Domain Dependencies

- Libraries preserve [Writing](../knowledge/writing.md) on [Printing](../knowledge/printing.md)-produced materials. Paper from [Pulp Chemicals](../chemistry/pulp-chemicals.md). Serves [Education](../knowledge/education.md) programs.

## Safety

- **Fire prevention**: Libraries are exceptionally vulnerable to fire. No open flames, smoking, or unattended electrical equipment. Install fire extinguishers (CO₂ or dry chemical) at every exit. Develop and practice evacuation plans. Fire-resistant construction (concrete, masonry) for new library buildings.
- **Mold exposure**: Mold-contaminated materials can cause respiratory illness. Wear N95-equivalent masks and gloves when handling moldy books or documents. Work in ventilated areas. Isolate contaminated materials immediately.
- **Heavy shelving**: Fully loaded library shelving is extremely heavy (100+ kg per meter of shelf). Secure tall shelving units to walls or floor to prevent tipping. Distribute weight evenly across shelves. Never climb shelving — use a step stool or rolling ladder.

## Limitations

- **Physical degradation**: All physical media degrade. Paper yellows and becomes brittle (acid-catalyzed hydrolysis of cellulose). Leather bindings rot. Parchment warps. Even with optimal storage (18-22°C, 40-55% RH, darkness), paper documents have finite lifespans measured in centuries.
- **Access limitations**: Physical libraries require physical presence. Knowledge is only available to those who can travel to the library, read the language, and understand the subject. These barriers limit the reach of stored knowledge.
- **Cataloging complexity**: As collections grow, finding specific information becomes increasingly difficult without systematic cataloging. Classification systems (Dewey, Library of Congress) require training to use effectively. Poorly cataloged collections may as well not exist for practical purposes.

## See Also

- [Writing](writing.md) — writing systems and materials
- [Printing](printing.md) — mass production of books and documents
- [Education](education.md) — literacy and knowledge transfer
- [Chemistry](../chemistry/index.md) — paper production, preservation chemicals

---

*Part of the [Bootciv Tech Tree](../index.md) • [Knowledge Preservation & Education](./index.md) • [All Domains](../index.md)*
