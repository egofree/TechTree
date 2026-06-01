# Ion Implantation

> **Node ID**: photolithography.ion-implantation
> **Parent**: [Core Fab Processes](fab-processes.md)
> **Domain**: [Photolithography & IC Fabrication](./index.md)
> **Dependencies**: [`gas-handling`](../gas-handling/index.md), [`energy.electricity`](../energy/electricity.md), [`vacuum`](../vacuum/index.md)
> **Timeline**: Years 50-80
> **Outputs**: ion_implantation, doped_regions, doping_profiles
> **Critical**: No — enables precision doping but thermal diffusion provides a functional baseline

Ion implantation is the primary doping method for modern integrated circuit fabrication, replacing thermal diffusion with independent control of dose and junction depth. A particle accelerator chain ionizes dopant atoms, selects a single species by mass, accelerates the ions to a controlled energy, and scans the beam uniformly across the wafer surface.

## Equipment Chain

### Ion Source

The ion source produces positively charged dopant ions from gas or solid feed materials:

- **BF₃ (boron trifluoride)**: Primary source for p-type doping (boron). Gas fed into the ionization chamber at controlled flow rates. Electron bombardment or RF plasma ionizes the gas, producing B⁺ and BF₂⁺ ions. BF₂⁺ is often preferred for shallow implants because the heavier molecular ion has lower penetration depth at the same acceleration voltage.
- **AsH₃ (arsine)**: Primary source for n-type doping (arsenic). Extremely toxic (IDLH 3 ppm). Produces As⁺ ions for deep, abrupt junction profiles. Arsenic's high mass (75 amu) produces shallower profiles than phosphorus at the same energy.
- **PH₃ (phosphine)**: Alternative n-type dopant source. Also extremely toxic (IDLH 50 ppm). Produces P⁺ ions. Lighter than arsenenic (31 amu) → deeper penetration at the same energy.
- **Solid sources**: Antimony (Sb) and indium (In) can be vaporized from heated crucibles for specialized implants (e.g., Sb for buried layers, In for p-type with minimal channeling due to high mass).

Ionization methods:
- **Electron bombardment**: Heated filament emits electrons (10-100 eV) into the source chamber. Electrons collide with gas molecules, stripping electrons to create positive ions. Current: 1-10 A electron current. Gas pressure in source: 10⁻³ to 10⁻² Torr.
- **RF plasma ionization**: 13.56 MHz RF coil excites the source gas into a plasma. Higher ionization efficiency than electron bombardment, especially for heavy species. Used in high-current implanters.

### Mass Analyzer (Magnetic Sector)

The mass analyzer separates the mixed ion beam into individual species by mass-to-charge ratio (m/q):

- **Magnetic sector**: 90° or 120° bending magnet. Ions pass through a uniform magnetic field B. The Lorentz force bends the ion trajectory with radius r = mv/(qB), where m = ion mass, v = velocity, q = charge. At fixed B and acceleration voltage, only ions with the desired m/q pass through the exit slit.
- **Resolution**: m/Δm > 100 required to separate adjacent species (e.g., ¹¹B⁺ from ¹²C⁺, or ⁷⁵As⁺ from ⁷⁴Ge⁺). Higher resolution means better species purity but lower beam current (narrower slit).
- **Species selection**: The operator sets the magnetic field to transmit the desired dopant (B⁺, BF₂⁺, P⁺, As⁺). Molecular ions (BF₂⁺ at 49 amu) are separated from atomic ions (B⁺ at 11 amu) by adjusting B.

### Acceleration Column

Electrostatic acceleration determines implant depth by controlling ion energy:

- **High-current implanters**: 10-100 keV acceleration. Used for source/drain implants (high dose, 10¹⁵-10¹⁶ cm⁻²), threshold adjust (10¹¹-10¹² cm⁻²), and well formation. Beam current: 1-25 mA. Throughput: 10-30 wafers/hour for 300 mm.
- **Medium-current implanters**: 10-500 keV. Versatile tools for most implant steps. Beam current: 0.1-5 mA.
- **High-energy implanters**: 200 keV to several MeV. Used for buried layers (retrograde wells, buried channels), deep well formation, and silicon-on-insulator (SIMOX) where oxygen is implanted at MeV energies to form a buried oxide layer. Beam current: 0.01-1 mA.

**Energy vs. depth relationship** (LSS theory — Lindhard, Scharff, Schiøtt):
- Projected range Rp ≈ k · E^1.5 for amorphous targets, where k depends on ion and target masses.
- Boron (light, 11 amu) at 100 keV: Rp ≈ 300 nm in silicon. At 30 keV: Rp ≈ 100 nm.
- Arsenic (heavy, 75 amu) at 100 keV: Rp ≈ 60 nm. At 30 keV: Rp ≈ 20 nm.
- Heavier ions stop shallower at the same energy because they lose more energy per unit distance through nuclear stopping (elastic collisions with silicon lattice atoms).

### Beam Scanning and End Station

- **Electrostatic scanning**: Two pairs of deflection plates raster the beam in X and Y across the wafer. Scan frequency: 100-1000 Hz. Uniformity target: ±1% dose across 300 mm wafer.
- **Mechanical scanning**: Wafer mounted on a spinning disk (1000-2000 rpm) that also translates linearly. The beam is stationary; the wafer moves through it. Preferred for high-current implanters where electrostatic deflection cannot handle the beam power.
- **Faraday cup**: Measures beam current for dose calculation. Dose Q = ∫I·dt/(q·A), where I = beam current, q = electronic charge, A = scan area. Accuracy: ±0.5%.
- **Wafer cooling**: Ion beam deposits 0.1-10 W/cm² of heat. Wafer temperature must stay below 100°C to prevent photoresist reticulation. Cooled platen (water-cooled or glycol-cooled) with gas-backed thermal contact (helium at 5-20 Torr between wafer and platen for thermal conduction).

## Process Parameters

### Dose and Energy Ranges

| Application | Dose (cm⁻²) | Energy (keV) | Species | Notes |
|-------------|-------------|-------------|---------|-------|
| Threshold adjust | 10¹¹ - 10¹² | 10 - 50 | B⁺, P⁺ | Fine-tunes Vth by adjusting surface concentration |
| Channel stop | 10¹³ - 10¹⁴ | 50 - 150 | B⁺ | Prevents inversion under field oxide |
| Well formation | 10¹³ - 10¹⁴ | 100 - 1000 | B⁺, P⁺ | Defines NMOS/PMOS tub regions |
| Source/drain extension | 10¹⁴ - 10¹⁵ | 5 - 30 | As⁺, BF₂⁺ | Ultra-shallow junctions (<30 nm) |
| Source/drain (deep) | 10¹⁵ - 10¹⁶ | 30 - 100 | As⁺, P⁺, BF₂⁺ | Low-resistance contact regions |
| Buried layer | 10¹³ - 10¹⁴ | 500 - 5000 | P⁺, O⁺ | MeV implant for retrograde wells or SIMOX |

### Channeling Prevention

Crystalline silicon has open channels along major crystal directions. Ions entering these channels travel much deeper than predicted by LSS theory (which assumes amorphous targets), creating unwanted "channeling tails" in the dopant profile:

- **Tilt**: Wafer tilted 7° off the beam axis so ions encounter lattice atoms rather than open channels. Standard tilt angle for <100> silicon wafers.
- **Twist**: Wafer rotated about its normal axis (typically 0°, 22°, or 45°) to further reduce planar channeling. Combined tilt/twist provides effective channeling suppression.
- **Screen oxide**: Grow 10-30 nm SiO₂ before implant. Ions scatter through the amorphous oxide layer, randomizing their entry angle into the crystal. Also prevents sputtered metal contamination from reaching the silicon surface.

## Annealing and Dopant Activation

Ion implantation amorphizes the silicon crystal lattice (displaces silicon atoms from their lattice sites). Annealing is required to:

1. **Restore crystallinity**: Repair implant damage by recrystallizing the amorphized layer (solid-phase epitaxial regrowth).
2. **Activate dopants**: Move dopant atoms from interstitial sites (electrically inactive) to substitutional lattice sites (electrically active).

### Annealing Methods

- **Furnace anneal**: 900-1050°C for 30-60 minutes in N₂ ambient. Simple but causes significant dopant diffusion (redistributes the carefully controlled profile by 100-300 nm). Adequate for large-geometry processes (>1 μm) where junction depth tolerances are loose.
- **Rapid thermal anneal (RTA)**: Ramp to 1000-1100°C in seconds using halogen lamp arrays, hold 10-30 seconds, cool rapidly. Minimizes dopant redistribution to <10 nm. Preferred for sub-micron processes. Requires precise temperature control (±2°C) and uniformity (±3°C across wafer).
- **Spike anneal**: Ramp to peak temperature (~1050-1080°C) in ~1 second, immediately cool. Total time above 900°C: <5 seconds. Limits dopant diffusion to <2 nm. Essential for ultra-shallow junctions at 65 nm node and below.
- **Laser anneal** (advanced): Pulsed excimer laser (308 nm XeCl or 248 nm KrF) melts the top 20-200 nm of silicon in 20-50 ns. Liquid-phase epitaxy regrows a perfect crystal with all dopants activated at well above solid solubility. Research/early production for sub-22 nm nodes.

### Anneal trade-offs

Higher temperature → more complete dopant activation but more diffusion. The annealing strategy is a balance between activating enough dopants to achieve the target sheet resistance while keeping dopant redistribution within the junction depth budget. Modern processes use multiple low-temperature anneals (e.g., spike anneal at 1050°C) rather than a single high-temperature furnace soak.

## Dose Measurement and Uniformity

- **Faraday cup measurement**: The ion beam current is integrated over time to compute total dose: Dose = ∫I dt / (q × A). Four-point probe sheet resistance mapping (pre- and post-anneal) verifies dose uniformity across the wafer.
- **Uniformity specification**: ±1% dose uniformity across 300 mm wafer (measured by 49-point or 121-point sheet resistance contour map). Non-uniformity causes threshold voltage variation across the die.
- **Thermaprobe / optical dosimetry**: In-situ measurement of implant dose using the refractive index change in silicon caused by lattice damage. Provides real-time dose monitoring without waiting for anneal and four-point probe.

## Integration with the Planar Process

Ion implantation fits into the IC fabrication flow as a replacement for thermal diffusion doping. In a typical NMOS transistor flow:

1. **Well implant**: MeV boron implant defines the p-well (for NMOS transistors) or n-well (for PMOS transistors).
2. **Threshold adjust**: Low-dose implant through the gate oxide to set threshold voltage precisely.
3. **Source/drain extension**: Low-energy, low-dose implant to form shallow extension regions under the gate spacer.
4. **Deep source/drain**: Higher energy, high-dose implant after spacer formation to form the main source/drain contact regions.

Each implant step uses a different photoresist mask to define which regions receive the dopant. The polysilicon gate electrode acts as a self-aligned mask for the source/drain implant — dopants only reach the silicon on either side of the gate, ensuring perfect alignment between gate and source/drain edges.

## Hazards & Safety

- **Dopant gases (AsH₃, PH₃, BF₃)**: Arsine and phosphine are immediately dangerous to life at ppm concentrations. AsH₃ IDLH: 3 ppm. PH₃ IDLH: 50 ppm. Both cause hemolytic anemia (destroy red blood cells) and pulmonary edema. Use in enclosed gas cabinets with continuous toxic gas monitoring (electrochemical sensors), automatic shut-off valves, and exhaust gas scrubbing (caustic wet scrubber or thermal destruct). Emergency protocol: evacuate immediately, use self-contained breathing apparatus (SCBA). BF₃ is corrosive and reacts with moisture to form HF and boric acid.
- **High voltage**: Acceleration columns operate at 10 keV to several MeV. Lethal electrical hazard. Interlocked enclosures, grounding sticks, and lockout/tagout procedures mandatory. X-ray production at voltages above 30 keV requires lead shielding and radiation monitoring.
- **Ionizing radiation**: Bremsstrahlung X-rays produced when high-energy ions strike beam line components. Shielding (lead or steel) around the acceleration column and beam line. Dosimetry monitoring for operators. Radiation area postings at MeV-class implanters.

## See Also

- [Core Fab Processes](fab-processes.md) — baseline fabrication including thermal diffusion doping
- [Advanced Processes](../vlsi-scaling/advanced-processes.md) — ion implantation for sub-250 nm nodes
- [Gas Handling](../gas-handling/index.md) — dopant gas delivery and exhaust systems
- [Vacuum Technology](../vacuum/index.md) — high-vacuum beam line systems
- [Electricity Generation & Distribution](../energy/electricity.md) — high-voltage power supplies

[← Back to Photolithography](index.md)
