# Vacuum Systems

> **Node ID**: vlsi-scaling.vacuum-systems
> **Domain**: [VLSI Scaling & Advanced Semiconductor](./index.md)
> **Dependencies**: [`gas-handling.vacuum`](../gas-handling/vacuum.md), [`metals.steel`](../metals/index.md), [`measurement.precision-metrology`](../measurement/precision-metrology.md)
> **Enables**: [`photolithography.fab-processes`](../photolithography/fab-processes.md), [`vlsi-scaling.advanced-processes`](advanced-processes.md), [`vlsi-scaling.advanced-lithography`](advanced-lithography.md)
> **Timeline**: Years 30-50
> **Outputs**: vacuum_pumps, vacuum_chambers, vacuum_gauges
> **Critical**: Yes — vacuum is required for sputtering, evaporation, ion implantation, and e-beam lithography


Vacuum systems — pumps, chambers, gauges, and seals — provide the low-pressure environments essential for sputtering, evaporation, CVD, ion implantation, and electron-beam lithography. The progression runs from mechanical roughing pumps (rotary vane, ~10⁻³ Torr) through diffusion pumps (~10⁻⁶ Torr) to turbomolecular pumps (~10⁻⁹ Torr) and cryopumps (~10⁻¹⁰ Torr). Leak detection (helium mass spectrometry) and outgassing control are ongoing challenges. For basic vacuum concepts and simple pump designs, see [Gas Handling & Vacuum](../gas-handling/vacuum.md).

## Vacuum Requirements by Process

Each semiconductor process has specific pressure requirements determined by the physics of the process — mean free path, gas-phase reactions, contamination thresholds, and beam scattering.

| Process | Operating Pressure | Key Requirement | Pump Type |
|---------|-------------------|-----------------|-----------|
| Sputtering (PVD) | 1-50 mTorr | Controlled Ar pressure for plasma | Turbo + dry rough |
| Evaporation (PVD) | 10⁻⁶ to 10⁻⁵ Torr | Long mean free path (>10 m) | Diffusion or turbo |
| LPCVD | 100-1000 mTorr | Controlled gas flow, uniformity | Rotary vane + throttle |
| PECVD | 0.5-10 Torr | Plasma at controlled pressure | Rotary vane + throttle |
| Ion implantation | 10⁻⁶ to 10⁻⁴ Torr | Beam transport without scattering | Turbo + cryo |
| E-beam lithography | 10⁻⁷ to 10⁻⁵ Torr | Electron beam focus, no scattering | Ion pump + turbo |
| EUV lithography | 10⁻⁷ to 10⁻⁵ Torr | EUV photon transmission (>10 m MFP) | Turbo + cryo |
| ALD | 10⁻³ to 10 Torr (pulsed) | Precise dose/evacuate cycling | Turbo + dry rough |
| SEM/TEM inspection | 10⁻⁷ to 10⁻⁵ Torr | Electron beam focus | Ion pump + turbo |
| Metal etch (RIE) | 1-100 mTorr | Controlled plasma chemistry | Turbo + dry rough |

**Mean free path (MFP)**: The average distance a molecule travels between collisions. MFP ≈ 5/P cm (with P in Torr). At 10⁻⁶ Torr, MFP ≈ 50 m — molecules travel across the chamber without gas-phase collisions. At 1 mTorr, MFP ≈ 5 cm — sufficient for sputtering but too short for e-beam or ion beam work.

**Strengths**:
- Table clearly maps each process to its required pressure, pump type, and physical rationale (MFP, beam scattering) — provides direct equipment selection guidance
- MFP formula (≈ 5/P cm) enables quick back-of-envelope validation of vacuum requirements for any new process

**Weaknesses**:
- ALD pulsed operation (10⁻³ to 10 Torr) requires rapid pressure cycling that stresses pump systems — not captured in the steady-state pressure table
- Actual process pressures depend on gas flow geometry and chamber design — table values are starting points, not guarantees

## Rotary Vane Pumps (Roughing Pumps)

The workhorse of vacuum technology — every high-vacuum system starts with a roughing pump to bring the chamber from atmospheric pressure (~760 Torr) down to ~10⁻² to 10⁻³ Torr, where a high-vacuum pump can take over.

**Construction and operation**:
- Eccentric rotor with spring-loaded vanes (2-3 vanes) rotating inside a cylindrical stator. As the rotor turns, each vane sweeps a crescent-shaped volume of gas from inlet to outlet. Sealed by thin oil film on vane tips and stator wall.
- **Single-stage**: Ultimate pressure ~10⁻² Torr. Pumping speed: 1-300 L/s (5-600 m³/hr typical for semiconductor tools). Motor: 0.5-15 kW depending on size.
- **Two-stage**: Two pump chambers in series. Ultimate pressure ~10⁻³ Torr. Required as backing pump for diffusion and turbomolecular pumps where lower backing pressure improves high-vacuum performance.
- **Oil seal**: Hydrocarbon vacuum oil lubricates vanes, seals clearances (vane-to-stator gap ~10-25 μm), and provides corrosion protection. Oil temperature: 60-80°C during operation (frictional heating). Oil changes: every 3-6 months or 2000-5000 operating hours. Oil degradation products (cracked hydrocarbons, acidic byproducts from corrosive process gases) contaminate the pump and reduce ultimate vacuum.

**Gas ballast**: A valve admits a controlled amount of air into the compression stage to prevent condensation of vapors (water, solvents) in the pump oil. With ballast open, ultimate vacuum degrades by ~10× but the pump handles condensable loads without oil contamination. Essential for pumping down chambers that have been vented to humid air (water vapor is the dominant outgassing species).

**Oil-free (dry) roughing pumps**: Semiconductor fabs increasingly require oil-free roughing pumps to eliminate hydrocarbon backstreaming contamination. Types:
- **Scroll pump**: Interleaving spiral scrolls — one fixed, one orbiting — trap and compress gas pockets. Ultimate vacuum ~10⁻² Torr. Speed: 5-60 L/s. No oil in the gas path. PTFE tip seals wear over time (12-24 month replacement interval). Preferred for clean semiconductor processes.
- **Screw pump**: Two intermeshing helical rotors. Handles higher gas loads and particulates than scroll. Ultimate vacuum ~10⁻² to 10⁻³ Torr. Speed: 20-200 L/s. More robust for corrosive processes (RIE exhaust, CVD byproducts) with appropriate rotor coatings (Ni, Teflon).
- **Diaphragm pump**: Flexible diaphragm driven by eccentric cam. Ultimate vacuum ~1-10 Torr. Speed: 0.5-5 L/s. Used for very small systems or as backing for molecular drag pumps. Completely oil-free with PTFE diaphragms.

**Strengths**:
- Rotary vane pumps achieve 10⁻²-10⁻³ Torr with 1-300 L/s speed — reliable, well-understood workhorse for every roughing application
- Dry scroll pumps eliminate hydrocarbon backstreaming entirely — PTFE tip seals provide clean pumping for semiconductor processes

**Weaknesses**:
- Oil-sealed rotary vane pumps produce hydrocarbon vapor that backstreams into the chamber — unacceptable for clean semiconductor front-end processes
- Dry pump PTFE tip seals wear out every 12-24 months — scheduled replacement required to maintain vacuum performance

## Turbomolecular Pumps

The primary high-vacuum pump for semiconductor processing. Turbomolecular pumps (turbo pumps) use high-speed rotating blades to impart momentum to gas molecules, preferentially directing them toward the exhaust.

**Principle of operation**: Rotor blades (angled like axial compressor blades) spinning at 24,000-90,000 RPM (typically 40,000-60,000 RPM for 200-300 mm pumps). Blade tip speed: 150-350 m/s — comparable to thermal velocity of gas molecules (~500 m/s for N₂ at 300K, ~1300 m/s for H₂). When blade tip speed approaches molecular thermal velocity, the blades effectively "push" molecules toward the exhaust. Each blade stage provides a compression ratio of ~2-10×; a pump with 20-40 blade stages achieves compression ratios of 10⁸-10¹² for N₂.

**Compression ratio by gas species**:
| Gas | Compression Ratio | Note |
|-----|------------------|------|
| H₂ | 10²-10⁴ | Light gases poorly pumped |
| He | 10³-10⁶ | Light gases poorly pumped |
| H₂O | 10⁶-10⁸ | Moderate |
| N₂ | 10⁸-10¹¹ | Well pumped |
| Ar | 10⁹-10¹¹ | Well pumped |
| Hydrocarbons | 10¹⁰-10¹² | Very well pumped |

Hydrogen and helium are the achilles heel of turbo pumps — their high thermal velocity (low molecular mass) makes them difficult to redirect with the rotor blades. H₂ accumulation in the chamber limits ultimate vacuum in many systems. For ultra-high vacuum (UHV, <10⁻⁹ Torr), supplementary pumping (ion pump, cryopump, or titanium sublimation pump) is needed for H₂ and He.

**Pumping speed**: 50-5000 L/s (typical for semiconductor tools: 300-2000 L/s for 200-300 mm wafer chambers). Speed is nearly constant from 10⁻³ to 10⁻⁹ Torr (molecular flow regime).

**Backing pump requirement**: Turbo pumps cannot exhaust to atmosphere — they require a backing (roughing) pump to maintain the foreline pressure below 0.1-1.0 Torr. Typical combination: turbo pump + dry scroll backing pump. The backing pump must handle the turbo's exhaust throughput: Q = S × P, where S is pumping speed and P is inlet pressure. At 10⁻⁶ Torr with 1000 L/s speed: Q = 10⁻³ Torr·L/s — easily handled by a 10 L/s scroll pump.

**Magnetic bearing turbos**: Advanced turbo pumps replace mechanical ball bearings with active magnetic bearings (5-axis electromagnetic levitation of the rotor). Advantages: zero friction, no lubricant contamination, 50,000+ hour maintenance interval (vs. 12,000-24,000 hours for grease-packed ceramic bearings), vibration <0.01 μm. Essential for e-beam lithography and SEM where mechanical vibration blurs the beam. Premium cost: 2-3× conventional bearing turbo pumps.

**Strengths**:
- Compression ratio of 10⁸-10¹² for N₂ with 20-40 blade stages — reaches 10⁻⁹ Torr from a 10⁻³ Torr backing pressure
- Magnetic bearing turbos provide vibration <0.01 μm and 50,000+ hour maintenance interval — essential for e-beam lithography

**Weaknesses**:
- H₂ compression ratio only 10²-10⁴ — hydrogen accumulates in the chamber and limits ultimate vacuum without supplementary pumping
- Blade tip speed of 150-350 m/s with 24,000-90,000 RPM — catastrophic failure mode if bearings seize or foreign object enters

## Diffusion Pumps

The oldest high-vacuum pump type (invented 1915), still used in some evaporation and legacy CVD systems. Simpler and cheaper than turbo pumps for large chambers but more prone to oil backstreaming contamination.

**Principle**: Electric heater (1-5 kW) boils silicone or hydrocarbon vacuum oil in the base of the pump. Oil vapor rises through a chimney and exits through angled jet nozzles at supersonic velocity (~200-300 m/s). The vapor jets collide with gas molecules and impart downward momentum, compressing the gas toward the exhaust. Oil vapor condenses on the cooled pump walls (~20-40°C water cooling) and returns to the boiler by gravity.

**Performance**: Pumping speed: 100-50,000 L/s (very large pumps available). Ultimate vacuum: ~10⁻⁶ to 10⁻⁸ Torr (limited by oil vapor pressure). Compression ratio: ~10⁶-10⁸ for N₂. Backing pressure: must maintain <0.5 Torr in the foreline or oil vapor backstreams into the chamber.

**Oil backstreaming**: The fundamental contamination risk. Oil vapor that escapes the jet nozzles and travels upward into the chamber condenses on the wafer and chamber walls, contaminating the process. Mitigation: cold cap (refrigerated baffle above the top jet), chevron baffles (maze-like geometry that intercepts oil vapor), and liquid-nitrogen cold traps (77 K surface that condenses oil vapor with near-100% efficiency). With proper trapping, backstreaming can be reduced to <10⁻¹⁰ g/(cm²·min), but zero contamination is never achievable with diffusion pumps.

**Advantages vs. turbo pumps**: Lower cost ($2,000-10,000 vs. $10,000-50,000 for equivalent speed), no moving parts (extremely reliable), handles high gas loads without damage, very high pumping speeds available for large chambers. Disadvantage: oil contamination risk makes them unsuitable for ultra-clean processes (semiconductor front-end processing, EUV).

**Strengths**:
- No moving parts — extremely reliable with essentially unlimited service life, unlike turbo pumps with bearing wear
- Pumping speeds of 100-50,000 L/s at 2-5× lower cost than equivalent turbo pumps — economical for large chambers

**Weaknesses**:
- Oil backstreaming contamination is never fully eliminable — cold caps and baffles reduce but cannot zero the risk
- Not suitable for ultra-clean semiconductor front-end processes or EUV — hydrocarbon contamination degrades film and resist quality

## Cryopumps

Cryopumps condense and adsorb gases on surfaces cooled to cryogenic temperatures (10-80 K). They provide very high pumping speeds for all gases including H₂ and He (with appropriate cryosorbent materials) and are completely oil-free.

**Two-stage cold head**:
- **First stage** (60-80 K): Cools a radiation shield and inlet baffle. Condenses water vapor, CO₂, and most hydrocarbons (vapor pressure <10⁻¹⁰ Torr at 70 K). Handles ~80% of the total gas load.
- **Second stage** (10-20 K): Cools the main cryopanel. Condenses N₂, O₂, Ar (vapor pressure <10⁻¹⁰ Torr at 15 K). Porous charcoal or molecular sieve adsorbs H₂, He, and Ne (which do not condense at 15 K — their vapor pressures exceed 1 Torr even at 10 K).
- Cooling power: 2-10 W at 20 K (second stage), 30-100 W at 80 K (first stage). Achieved by closed-cycle helium refrigeration (Gifford-McMahon or pulse tube cycle). Compressor input power: 2-10 kW.

**Pumping speed**: 500-15,000 L/s for N₂, 1500-30,000 L/s for H₂O (very high because water freezes as ice on the 80 K baffle). Ultimate vacuum: ~10⁻⁹ to 10⁻¹⁰ Torr (limited by H₂ and He saturation of the cryosorbent).

**Regeneration**: Cryopanels accumulate frozen gases until saturated (capacity: 10⁴-10⁶ Torr·L depending on size). The pump must be periodically regenerated: isolate from chamber, warm to room temperature, pump out released gases with a roughing pump, then re-cool. Regeneration cycle: 1-4 hours (warm-up + pump-out + re-cool). Typical interval: daily to weekly depending on gas load. During regeneration, the process chamber is unavailable — a scheduling consideration for production fabs.

**Advantages**: Highest pumping speed per unit cost for large systems, captures all gases (no exhaust to abate), completely clean (no oil). Ideal for sputtering systems and batch evaporators. Disadvantage: finite capacity requiring regeneration, not suitable for continuous high-throughput gas flow (LPCVD, PECVD).

**Strengths**:
- Completely oil-free with pumping speeds of 500-15,000 L/s (N₂) — highest speed per dollar for large systems
- Charcoal cryosorbent captures H₂ and He at 10-20 K, addressing the light-gas gap in turbo pump performance

**Weaknesses**:
- Finite gas capacity (10⁴-10⁶ Torr·L) requires periodic regeneration (1-4 hours) — chamber unavailable during cycle
- Not suitable for continuous gas-flow processes (LPCVD, PECVD) — cryopanels saturate rapidly under steady gas load

## Ion Pumps

Ion pumps (sputter ion pumps, SIP) use energetic ions to bury gas molecules in a titanium cathode. They have no moving parts and achieve the lowest ultimate pressures available (~10⁻¹¹ Torr).

**Principle**: Penning cell geometry — stainless steel anode cylinder at +3-7 kV, titanium cathode plates at ground, immersed in a 0.1-0.3 T magnetic field from external permanent magnets. Electrons spiral along magnetic field lines, ionizing gas molecules in the anode cylinder. Positive ions accelerate into the titanium cathode, sputtering titanium atoms that deposit on the anode and bury gas molecules (ion burial). Chemically active gases (N₂, O₂, H₂, CO, CO₂) also react with freshly sputtered titanium (gettering).

**Performance**: Pumping speed: 1-500 L/s (typically 20-100 L/s for semiconductor applications). Ultimate vacuum: <10⁻¹¹ Torr (limited only by the very low outgassing rate of the all-metal, bakeable construction). Operating pressure range: 10⁻⁴ to 10⁻¹¹ Torr. At higher pressures (>10⁻⁴ Torr), excessive ion current overheats the cathode.

**Starting requirement**: Ion pumps must be started at low pressure (<10⁻³ Torr) to avoid arcing. A turbo or diffusion pump roughs the chamber first, then the ion pump takes over. Once started, the ion pump maintains vacuum indefinitely with no backing pump — it traps gas internally rather than exhausting it.

**Applications**: E-beam lithography columns, electron microscopes, surface analysis equipment (XPS, AES), and ultra-high vacuum research systems. Ideal where absolute cleanliness and zero vibration are required (no moving parts, no fluids). Not suitable for high-throughput process tools (sputtering, CVD) due to limited pumping speed and inability to handle large gas loads.

**Strengths**:
- Achieves <10⁻¹¹ Torr with zero vibration and no moving parts — ideal for e-beam lithography and electron microscopes
- Traps gas internally with no backing pump required — once started, maintains vacuum indefinitely

**Weaknesses**:
- Pumping speed limited to 1-500 L/s — inadequate for high-throughput process tools (sputtering, CVD)
- Must be started at <10⁻³ Torr to avoid arcing — requires separate roughing pump for initial pump-down

## Vacuum Gauges and Pressure Measurement

Different pressure ranges require different measurement technologies. No single gauge covers the full range from atmosphere to 10⁻¹¹ Torr.

**Gauge types by range**:
| Gauge | Range (Torr) | Principle | Accuracy |
|-------|-------------|-----------|----------|
| Mechanical (diaphragm) | 760 to 10⁻¹ | Mechanical deflection | ±0.5-1% |
| Pirani/thermocouple | 760 to 10⁻³ | Thermal conductivity of gas | ±10-20% (gas-dependent) |
| Convectron (enhanced Pirani) | 760 to 10⁻⁴ | Thermal convection + conduction | ±10-15% (gas-dependent) |
| Capacitance manometer | 760 to 10⁻⁴ | Capacitance change from diaphragm deflection | ±0.1-0.5% (gas-independent) |
| Cold cathode (Penning) | 10⁻³ to 10⁻⁹ | Ion current from gas discharge | ±30-50% (gas-dependent) |
| Hot cathode ion (Bayard-Alpert) | 10⁻³ to 10⁻¹¹ | Electron ionization current | ±10-20% (gas-dependent) |

**Capacitance manometer**: The most accurate gauge for process pressure control. A thin metal diaphragm (stainless steel or Inconel, 10-50 μm thick) separates a reference vacuum from the measured pressure. Diaphragm deflection changes the capacitance between the diaphragm and a fixed electrode. Resolution: 10⁻⁵ of full scale (e.g., 10⁻⁴ Torr on a 10 Torr full-scale gauge). Gas-independent (mechanical measurement, not thermal or ionization). Temperature-controlled to 40-50°C to prevent drift from ambient temperature changes. Cost: $1,000-5,000 per gauge head; $5,000-20,000 per gauge controller.

**Hot cathode ionization gauge (Bayard-Alpert)**: The standard for high and ultra-high vacuum measurement. Heated tungsten or thoriated iridium filament emits electrons (emission current 1-10 mA) accelerated to +150 V grid. Electrons ionize gas molecules; ions collected on a thin wire cathode at -30 to 0 V. Ion current is proportional to gas density (pressure): I_ion = S × P × I_emission, where S is the gauge sensitivity factor (~10-25 Torr⁻¹ for N₂). Lower limit: ~10⁻¹¹ Torr (X-ray limit — soft X-rays from electron bombardment of the grid produce photoelectrons from the collector, creating a false current that mimics ~10⁻¹¹ Torr pressure).

**Gauge calibration**: Ion gauges and Pirani gauges have gas-dependent sensitivity. Their calibration is typically for N₂. For other gases, correction factors: He ×0.18, H₂ ×0.46, Ar ×1.29, CO₂ ×1.42. Capacitance manometers are gas-independent and require no correction. Annual calibration against a transfer standard (spinning rotor gauge or calibrated capacitance manometer) maintains traceability to national standards.

**Strengths**:
- Capacitance manometer provides ±0.1-0.5% accuracy gas-independently — the gold standard for process pressure control in semiconductor tools
- Bayard-Alpert ion gauge covers 10⁻³ to 10⁻¹¹ Torr — five-decade range with a single instrument

**Weaknesses**:
- Pirani/thermocouple gauges have ±10-20% accuracy and are gas-dependent — require correction factors for non-N₂ atmospheres
- Ion gauge X-ray limit at ~10⁻¹¹ Torr produces false current — cannot measure below this floor without extractor gauge designs

## Chamber Design and Materials

Vacuum chamber design determines ultimate pressure, outgassing rate, and process uniformity. The chamber must maintain structural integrity under atmospheric pressure (14.7 psi = 101 kPa external load on every surface) while minimizing internal surface area and outgassing.

**Materials**:
- **Stainless steel (304 or 316L)**: The standard for semiconductor vacuum chambers. Low outgassing rate after bakeout: ~10⁻¹² Torr·L/(s·cm²). Yield strength: 205 MPa (304), 290 MPa (316L). Minimum wall thickness for 300 mm diameter cylindrical chamber at atmosphere: ~3-5 mm (with 2-3× safety factor). Surface finish: electropolished to Ra <0.4 μm (smooth surface traps less gas and is easier to clean).
- **Aluminum (6061-T6)**: Lower outgassing than stainless after appropriate treatment, lighter weight (2.7 vs. 8.0 g/cm³), better thermal conductivity (167 vs. 16 W/(m·K) — useful for temperature-controlled chambers). Lower strength (276 MPa yield) requires thicker walls or external reinforcement. Anodized surface for corrosion resistance. Used for large process chambers (sputtering, PVD) where weight and thermal uniformity matter.
- **Water cooling**: Stainless steel tubing (6-12 mm OD) welded to chamber exterior or internal channels machined into chamber walls. Flow: 2-10 L/min at 2-4 bar. Removes 0.5-5 kW of process heat (plasma, sputtering, substrate heating) to maintain chamber temperature <60°C.

**Seals and flanges**:
- **Elastomer seals (Viton, Buna-N)**: O-ring in a groove, compressed between flanges. Simple, reusable (100+ cycles). Leak rate: ~10⁻⁸ to 10⁻⁹ Torr·L/s. Temperature limit: 200°C (Viton), 120°C (Buna-N). O-ring groove design: cross-section compression 15-25% for seal. Outgassing from Viton: ~10⁻⁸ Torr·L/(s·cm²) of seal surface — acceptable for high vacuum but not UHV. Helium permeation rate through Viton: ~10⁻⁹ Torr·L/(s·cm) of seal length — limits ultimate vacuum in UHV systems.
- **Metal seals (ConFlat, CF)**: Flat copper gasket (Oxygen-free high-conductivity copper, OFHC) compressed between knife-edge flanges. Leak rate: <10⁻¹² Torr·L/s. Bakeable to 450°C. Single-use gasket (replaced every disassembly). Required for UHV systems (<10⁻⁹ Torr). Knife-edge profile: 70° included angle, ~0.1 mm tip radius — cuts into copper to form a gas-tight seal. Bolt torque: 15-25 N·m per bolt (typically 6-24 bolts per flange depending on size).
- **CF flange sizes**: DN16 (16 mm bore, 6 bolts) through DN350 (350 mm bore, 24 bolts). Larger flanges require thicker gaskets and more bolts for uniform compression. For semiconductor tools, common sizes: DN40, DN63, DN100, DN160, DN200.

**Strengths**:
- CF copper gasket seals achieve <10⁻¹² Torr·L/s leak rate and 450°C bakeout — gold standard for UHV systems
- Electropolished 316L stainless steel achieves 10⁻¹² Torr·L/(s·cm²) outgassing after bakeout — enables 10⁻¹⁰ Torr base pressures

**Weaknesses**:
- CF gaskets are single-use (replaced every disassembly) — frequent maintenance access increases consumable cost
- Viton O-rings outgas at 10⁻⁸ Torr·L/(s·cm²) and permeate helium — limits elastomer-sealed systems to ~10⁻⁸ Torr

## Outgassing and Bakeout

Every surface inside a vacuum chamber releases adsorbed gas molecules — primarily water vapor (H₂O) from atmospheric exposure, plus N₂, O₂, CO₂, and hydrocarbons. This outgassing is the dominant gas load in most vacuum systems below 10⁻³ Torr.

**Outgassing rates** (Torr·L/(s·cm²)):
| Material | Untreated | After 24 hr at 20°C pump | After 24 hr bake at 150°C | After 24 hr bake at 300°C |
|----------|-----------|-------------------------|--------------------------|--------------------------|
| Stainless steel | 10⁻⁷ to 10⁻⁶ | 10⁻⁹ | 10⁻¹⁰ | 10⁻¹² |
| Aluminum | 10⁻⁷ to 10⁻⁶ | 10⁻⁹ | 10⁻¹¹ | 10⁻¹² |
| Viton O-ring | 10⁻⁶ | 10⁻⁷ | 10⁻⁸ (200°C max) | N/A |
| PTFE | 10⁻⁶ | 10⁻⁸ | 10⁻⁹ | 10⁻¹⁰ |

**Bakeout procedure**: Heat chamber walls to 150-300°C (typically with externally mounted heater tapes or blankets) while continuously pumping. Water vapor desorbs rapidly above 100°C. Duration: 12-48 hours depending on target vacuum and chamber history. Temperature uniformity: ±10-20°C — cold spots retain water and extend bakeout. After bakeout, cool to operating temperature while continuing to pump. The improvement in ultimate vacuum after proper bakeout is typically 10-100×.

**In-situ plasma cleaning**: RF or microwave plasma (Ar, O₂, or Ar/O₂ mixture at 10-100 mTorr) bombards chamber walls, desorbing and chemically removing adsorbed contaminants. More effective than thermal bakeout alone for removing organic films and polymer deposits from CVD/RIE processes. Typical recipe: 500 W RF power, 50 mTorr Ar/O₂, 30-60 min. Used as routine chamber conditioning between process runs in production fabs.

**Strengths**:
- 150-300°C bakeout for 12-48 hours improves ultimate vacuum by 10-100× — the single most effective vacuum conditioning step
- In-situ Ar/O₂ plasma cleaning removes organic films that thermal bakeout cannot — essential for CVD/RIE chamber maintenance

**Weaknesses**:
- Bakeout duration of 12-48 hours makes chamber unavailable for production — scheduling impact on fab throughput
- Temperature uniformity of ±10-20°C means cold spots retain water — incomplete bakeout if heating blankets have gaps

## Leak Detection

Even a tiny leak (10⁻⁶ Torr·L/s) can prevent a system from reaching its target vacuum or introduce atmospheric contaminants (O₂, H₂O) that poison the process.

**Helium mass spectrometer leak detector (MSLD)**: The gold standard for leak detection. Helium (He) is sprayed on the exterior of the vacuum system while a mass spectrometer tuned to mass 4 (He⁺) monitors the chamber interior. Helium is ideal: low molecular weight (rapid diffusion through leaks), inert (no chemical reactions), rare in atmosphere (5.2 ppm — low background), and easily distinguished by mass spectrometry.

**Detection sensitivity**: 10⁻⁶ to 10⁻¹² Torr·L/s (depending on configuration). In "direct flow" mode (MSLD connected to chamber via a valve): sensitivity ~10⁻¹⁰ Torr·L/s. In "reverse flow" mode (MSLD on the roughing pump foreline): sensitivity ~10⁻⁷ Torr·L/s but can test at higher chamber pressures.

**Leak hunting procedure**:
1. Evacuate chamber to low pressure with turbomolecular pump.
2. Connect MSLD to chamber (or foreline).
3. Spray helium in small amounts at suspected leak locations: flange seals, weld seams, feedthrough connectors, valve packing, viewports, electrical feedthroughs. Work from top to bottom (helium rises).
4. Observe MSLD readout for He signal increase. Response time: 1-10 seconds (depends on chamber volume and pumping speed).
5. Mark any leak locations. Typical leak sources: scratched O-rings (replace O-ring, clean flange faces), cracked welds (re-weld or patch), porous casting (seal with vacuum epoxy as temporary fix).

**Acceptable leak rates by application**:
- Sputtering system: <10⁻⁶ Torr·L/s (water and O₂ contamination tolerated at 10⁻⁶ Torr process pressure)
- LPCVD reactor: <10⁻⁷ Torr·L/s (O₂ contamination affects film quality)
- Ion implantation: <10⁻⁸ Torr·L/s (O₂ and N₂ scatter the ion beam)
- E-beam lithography: <10⁻⁹ Torr·L/s (contamination deposits on electron optics)
- UHV surface analysis: <10⁻¹⁰ Torr·L/s (any atmospheric gas contaminates surface under study)

**Strengths**:
- Helium MSLD achieves 10⁻¹² Torr·L/s sensitivity — detects leaks smaller than any process requirement
- Helium tracer gas is inert, rare in atmosphere (5.2 ppm), and mass-4 distinguishable — zero false positives

**Weaknesses**:
- Leak hunting is sequential (spray-and-wait) — locating a single leak in a complex tool with 50+ seals takes 1-4 hours
- MSLD equipment costs $20,000-80,000 — dedicated instrument required, not shareable with other measurement tasks

## Vacuum Feedthroughs

Every vacuum chamber requires electrical, mechanical, and optical connections that penetrate the chamber wall without compromising the vacuum seal.

**Electrical feedthroughs**:
- **Low voltage / high current**: Copper or nickel conductors brazed into ceramic (alumina, Al₂O₃) insulators, mounted in CF flanges. Current rating: 10-200 A per pin. Voltage isolation: 1-5 kV. Used for heater power, motor drives, and high-current plasma electrodes.
- **High voltage**: Stainless steel conductors in ceramic insulators, longer creepage paths (>20 mm for 10 kV rating). Voltage rating: 5-60 kV. Used for ion implantation acceleration voltage and e-beam column supplies. Vacuum side must have smooth, polished surfaces to prevent field emission (which causes arcing and vacuum degradation).
- **Thermocouple feedthroughs**: Chromel/alumel (type K) or Pt/Pt-Rh (type B) wires brazed into ceramic. Allows temperature measurement inside the chamber. 2-8 thermocouple channels per feedthrough.
- **Coaxial and RF feedthroughs**: 50 Ω coaxial (SMA, BNC, N-type connectors) for signal transmission. RF power feedthroughs (matched impedance) for plasma generation at 13.56 MHz or 2.45 GHz. Power handling: 100 W to 10 kW depending on connector and cable size.

**Mechanical feedthroughs**:
- **Rotary motion**: Magnetic coupling (internal magnet driven by external rotating magnet, separated by vacuum wall — zero leak, 0-1000 RPM, torque limited to 0.1-5 N·m). Ferrofluidic seal (ferrofluid held in place by permanent magnets around the shaft — near-zero leak, up to 10,000 RPM, higher torque, but ferrofluid has finite vapor pressure limiting ultimate vacuum to ~10⁻⁸ Torr). Bellows-sealed (welded metal bellows transfers rotary or linear motion — zero leak, limited travel, heavy duty).
- **Linear motion**: Bellows-sealed pushrods (1-100 mm travel). Rack-and-pinion or lead screw mechanisms for wafer transfer between load lock and process chamber. Position repeatability: ±0.1-1.0 mm.

**Viewports**: Fused silica or sapphire windows in CF flanges for optical access (pyrometry, laser interferometry, visual inspection). Window thickness: 3-10 mm depending on diameter. Anti-reflection coating on both surfaces reduces reflection from ~7% to <1% per surface at the wavelength of interest. Borosilicate glass viewports for lower-cost applications (visible range only, not UV-transmitting).

**Strengths**:
- Ceramic-to-metal brazed electrical feedthroughs provide 1-5 kV isolation and 10-200 A current — hermetic seal with zero leak
- Magnetic coupling rotary feedthroughs transfer motion through the vacuum wall with zero leak — no seals to wear

**Weaknesses**:
- Ferrofluidic seal feedthroughs have finite vapor pressure (~10⁻⁸ Torr) — limits use in UHV systems
- Viewports under vacuum experience ~10,400 N force on 300 mm diameter — scratched glass can implode violently

## Pump System Integration for Semiconductor Tools

A typical semiconductor process tool (sputtering system, etch chamber, or implanter) uses a multi-stage pumping system combining roughing and high-vacuum pumps.

**Example: 300 mm sputter deposition system**:
- **Chamber**: 400 mm diameter × 300 mm tall stainless steel cylinder, electropolished, water-cooled. Volume ~40 L. Internal surface area ~5000 cm².
- **High-vacuum pump**: Turbomolecular pump, 1000 L/s (N₂), magnetic bearing. Mounted directly on chamber base via CF200 flange.
- **Backing pump**: Dry scroll pump, 15 L/s, connected to turbo exhaust via 25 mm NW flex hose.
- **Roughing line**: Separate 25 mm NW line from chamber to scroll pump, with pneumatic gate valve. Used for initial pump-down and vent cycles.
- **Base pressure**: <5×10⁻⁸ Torr after 24-hour bake at 150°C (dominated by H₂O outgassing from chamber walls and H₂ from turbo pump exhaust back-diffusion).
- **Pump-down time**: Atmosphere to 10⁻³ Torr (roughing): ~5-8 min. 10⁻³ to 10⁻⁶ Torr (turbo takes over): ~15-30 min. 10⁻⁶ to 5×10⁻⁸ Torr (outgassing-limited): ~8-24 hours. Total to base: ~24 hours with bakeout.
- **Process pressure control**: During sputtering, Ar gas flows at 10-50 sccm. Throttle valve (angled butterfly or gate valve with variable conductance) between chamber and turbo maintains constant process pressure (2-10 mTorr). Pressure feedback from capacitance manometer to throttle valve controller: response time <1 second, stability ±0.5% of setpoint.

**Load lock design**: To avoid venting the main process chamber for every wafer exchange, a load lock (small antechamber, ~2-5 L volume) is cycled between atmosphere and high vacuum independently. Pump-down: roughing pump brings load lock to 10⁻³ Torr in ~30-60 seconds. Then gate valve to main chamber opens for wafer transfer by a robot arm. This preserves the main chamber vacuum and reduces total cycle time from hours to minutes per wafer.

**Strengths**:
- Load lock preserves main chamber vacuum during wafer exchange — reduces cycle time from hours to minutes per wafer
- Throttle valve + capacitance manometer feedback maintains process pressure at ±0.5% setpoint with <1 second response

**Weaknesses**:
- Full pump-down to 5×10⁻⁸ Torr base pressure requires 24 hours with bakeout — unscheduled vent events cost a full day of production
- Multi-stage pumping system (roughing + turbo + backing) has 3+ potential failure points — any single pump failure stops the tool

## Hazards & Safety

- **Implosion hazard**: Vacuum chambers experience 14.7 psi (101 kPa) external pressure differential. A 300 mm diameter viewport experiences ~10,400 N (~2400 lbf) of force at atmosphere. Cracked or scratched glass viewports can shatter inward violently. Inspect all viewports before each pump-down — replace any with scratches >0.1 mm deep or star cracks. Safety glasses required near evacuated chambers. Polycarbonate shields over viewports provide secondary containment.
- **Cryogenic burns**: Cryopump cold surfaces at 10-20 K cause immediate frostbite on contact. Second-stage surfaces are not accessible during normal operation, but during regeneration the cold head is exposed. Cryo-rated gloves (loose-fitting for quick removal) and face shield during cryopump maintenance. Liquid nitrogen cold traps at 77 K also present burn hazard.
- **Electrical hazards**: Ion pump power supplies operate at 3-7 kV. Turbo pump magnetic bearing controllers at 100-300 V. Capacitor banks in ion pump controllers store charge. Lock-out/tag-out and grounding procedures before any maintenance on pump electronics.
- **Compressed gases**: Pump exhaust may contain toxic process gases (SF₆ decomposition products, metal-organic ALD precursors, HF from etch processes). Point-of-use abatement on all exhaust lines. Exhaust ventilation to gas scrubber or burn box. Never discharge vacuum pump exhaust directly into laboratory air.
- **Noise**: Turbomolecular pumps produce 50-65 dB at 1 m distance (high-pitch whine from rotor blades). Acceptable for continuous exposure but hearing protection recommended for extended time in pump rooms. Dry scroll pumps produce 55-70 dB with characteristic pulsing tone.


## See Also

- [Gas Handling Vacuum](../gas-handling/vacuum.md) — vacuum fundamentals and roughing pumps
- [Precision Metrology](../measurement/precision-metrology.md) — vacuum gauge calibration
- [Metals Index](../metals/index.md) — stainless steel for vacuum chambers
- [Core Fab Processes](../photolithography/fab-processes.md) — fab vacuum requirements
- [Advanced Processes](advanced-processes.md) — high-vacuum deposition and etch
- [Lithography](lithography.md) — vacuum for lithography tools

[← Back to VLSI Scaling](index.md)
