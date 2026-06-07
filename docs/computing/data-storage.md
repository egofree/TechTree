# Data Storage

> **Node ID**: computing.data-storage
> **Domain**: [Computing](./index.md)
> **Dependencies**: [`computing`](./index.md), [`polymers.thermoplastics`](../polymers/thermoplastics.md)
> **Enables**: None (leaf capability)
> **Timeline**: Years 35-50
> **Outputs**: persistent_storage, removable_media, solid_state_memory
> **Critical**: No — computing enhances capability but is not strictly required for survival


Computing requires persistent, reliable data storage. Programs, datasets, operating systems, and intermediate results must survive power cycles. Storage technology spans a vast range: from punch cards (the earliest automated data media) through magnetic recording (the backbone of mass storage for seven decades) to solid-state flash memory (the modern standard). Each technology trades off capacity, speed, cost, longevity, and manufacturing complexity. Understanding these tradeoffs is essential for choosing the right storage at each stage of the bootstrapping process.

## Prerequisites

- [Computing fundamentals](./index.md) — digital logic, binary encoding, and basic computer architecture
- [Paper production](../chemistry/pulp-chemicals.md) — for punch cards and paper tape (earliest storage media)
- [Polymer film](../polymers/thermoplastics.md) — polyester/Mylar substrate for magnetic tape and floppy disks
- [Iron and steel](../metals/iron-steel.md) — magnetic recording heads, spindle shafts, actuator arms
- [Magnetic materials](../metals/index.md) — iron oxide particles and cobalt alloys for recording media
- [Precision machining](../machine-tools/index.md) — sub-micron tolerances for disk spindles and head assemblies
- [Semiconductor fabrication](./electronic.md) — required for EPROM, EEPROM, and flash memory
- [Laser technology](../optics/index.md) — CD, DVD, and Blu-ray optical storage

## Bootstrapping Progression

Storage technology appears in a predictable sequence as manufacturing capability matures. Each stage builds on the materials and precision developed in the previous one:

1. **[Paper-based](../glossary/paper-based.md)** (years 1-15): Punch cards and paper tape require only paper production, simple stamping mechanisms, and basic mechanical readers. Data density is abysmal (960 bits per card, ~50 KB per tape roll), but the technology is accessible at the earliest stages of industrialization.

2. **[Magnetic tape](../glossary/magnetic-tape.md)** (years 15-25): Requires polyester film substrate, iron oxide particles, binder chemistry, and precision coating. Cassette-based storage at 300-2400 baud is achievable with moderate electronics. Reel-to-reel at higher density demands better head gap control and tape transport mechanics.

3. **[Magnetic disk](../glossary/magnetic-disk.md)** (years 25-40): Demands precision machining for spindle bearings (runout <0.5 μm), cleanroom assembly, aerodynamic head design, and servo positioning systems. The engineering leap from tape to disk is substantial.

4. **[Solid-state](../glossary/solid-state.md)** (years 40+): Requires semiconductor fabrication. EPROM and EEPROM are achievable with modest process capability (2-3 μm feature sizes). NAND flash at competitive densities needs sub-100nm lithography.

This progression means early computing systems will rely heavily on magnetic tape for mass storage, with paper tape for bootstrapping and program input.

## Punch Cards

Herman Hollerith's 1890 tabulating system used punched paper cards to record and process census data. The standard card measures 7 3/8 × 3 1/4 inches (187 × 83 mm), with 80 columns and 12 rows. Each column encodes one character via punched holes in specific row combinations. A fully punched card holds 80 characters, roughly 960 bits of information.

Card readers detect holes mechanically (early pin-sensing) or photoelectrically (light beam through holes). Reading speed: 100-2000 cards per minute depending on era and mechanism. Card punches operate at 50-300 cards per minute. IBM's 80-column format dominated from 1928 through the 1970s. Earlier formats (45 columns, 90 columns) existed but lost out.

For bootstrapping, punch cards are the simplest entry point into automated data processing. They require only paper, a punching mechanism, and a reading mechanism. No magnets, no semiconductors, no vacuum systems.

## Paper Tape

Narrow strips of paper (typically 17.5 mm, 22 mm, or 25.4 mm wide) with punched holes encoding data across 5 to 8 channels (rows). Five-channel tape encodes Baudot code (32 characters, later ITA2 with shift for 58 characters). Eight-channel tape encodes full ASCII (256 characters). Data density: roughly 10 characters per inch (400 characters per foot). A 1000-foot roll holds about 400,000 characters.

Teletype readers feed tape at 10-60 characters per second. High-speed optical readers reach 1000 characters per second. Paper tape served as program and data storage for early computers (1950s-1970s) and as numerical control (NC) input for machine tools.

Paper tape is easier to produce than punch cards (no special card stock) but harder to edit. Splicing blocks with tape and hand punches was the standard correction method. For bootstrapping, paper tape pairs naturally with teleprinters for low-speed program and data I/O.

## Magnetic Storage Principles

Magnetic recording exploits the hysteresis loop of ferromagnetic materials. Apply a magnetic field to a small region of the medium: the region's magnetization aligns with the field and retains that orientation after the field is removed (remanence). The coercivity of the medium determines how strong an external field is needed to change the magnetization, governing both writeability and stability.

Writing: a current through the write head generates a localized magnetic field that magnetizes a tiny spot on the moving medium. Reading: the magnetized spot induces a voltage in the read head as it passes (Faraday's law). Modern read heads use magnetoresistive (MR) or giant magnetoresistive (GMR) sensors rather than inductive coils, achieving much higher sensitivity.

Recording density depends on head gap width, flying height (head-to-medium spacing), and minimum coercivity of the medium. Areal density has increased from 2 kb/in² (1956 RAMAC) to over 1 Tb/in² in modern drives.

## Magnetic Drum

An early random-access storage device. A rotating cylinder (12-30 inches diameter, 6-24 inches long) coated with magnetic oxide. Read/write heads mounted along the axis, one per track. No head movement needed: each track has its own fixed head. Capacity: 1-10 MB depending on drum size and track density. Rotation speeds: 1200-3600 RPM, giving average access times of 8-25 ms (half rotation).

The IBM 650 computer (1954) used a magnetic drum as its primary memory, holding 1000-4000 words. Drums were faster than tape but far more expensive per bit. They faded once magnetic disk technology matured, but the fixed-head-per-track concept survives in modern drum-buffer designs for video and communications.


## IBM 350 RAMAC (1956)

The first commercial hard disk drive. Stored 5 million characters (5 MB) on 50 spinning platters, each 24 inches in diameter. Two independent read/write heads accessed data with average seek time of ~600 ms. Weight: over one ton. The RAMAC proved the concept that disks could provide fast random access to large datasets.

## Hard Disk Architecture

Modern hard disks use the same principles at vastly smaller scale:

- **Platters**: Aluminum or glass disks coated with a thin magnetic layer (cobalt alloy, 10-20 nm thick). Multiple platters stack on a single spindle. Rotation: 5400-15000 RPM.
- **Tracks**: Concentric circles of recorded data on each surface. Track pitch: 0.1-0.5 μm (100,000-500,000 tracks per inch).
- **Sectors**: Each track divided into sectors (typically 512 bytes or 4 KB). Sector formatting includes address marks, data field, error correction code (ECC).
- **Read/write heads**: One per surface. Heads fly on an air bearing 5-10 nm above the platter surface (closer than a fingerprint ridge). A head crash (contact with the platter) destroys data and the head. The slider aerodynamics that maintain this flying height are a precision engineering achievement.
- **Actuator**: A voice-coil motor swings the head arm across the platter radius. Seek time: 3-5 ms average for modern drives.

## Encoding Schemes

Early drives used simple FM (frequency modulation) encoding: a clock bit precedes every data bit, doubling the required flux transitions. MFM (modified frequency modulation) eliminates the clock bit when the previous and current data bits are both zero, roughly doubling the effective density. RLL (run-length limited) encoding, specifically RLL 2,7, packs 1.5× more data than MFM by constraining the minimum and maximum run lengths of identical bits. Modern drives use PRML (partial response, maximum likelihood) and EPRML (extended PRML) signal processing, which sample the analog readback waveform at intervals and use Viterbi detection to determine the most likely bit sequence, achieving much higher areal densities than peak-detection methods.

## Capacity Progression

| Year | Drive | Capacity | Platters | Areal Density |
|------|-------|----------|----------|---------------|
| 1956 | IBM 350 | 5 MB | 50 × 24" | 2 kb/in² |
| 1980 | Seagate ST-506 | 5 MB | 4 × 5.25" | ~8 Mb/in² |
| 1991 | IBM 0663 | 1 GB | 8 × 3.5" | ~60 Mb/in² |
| 2020 | Typical HDD | 10-20 TB | 6-8 × 3.5" | ~1 Tb/in² |


## Reel-to-Reel

Half-inch wide magnetic tape on 10.5-inch reels, typically 2400 feet long. Data recorded in 9 tracks (8 data bits + 1 parity). Recording density progressed: 800 bpi (NRZI), 1600 bpi (PE), 6250 bpi (GCR). A 2400-foot reel at 6250 bpi stores approximately 180 MB. Tape drive speeds: 75-200 inches per second. Start/stop time: 1-5 ms. Sequential access only, making tape best for backup, archival, and batch processing.

## Cassette Tape

Compact audio cassettes adapted for data storage. The Kansas City standard (1975) used audio frequency shift keying: 1200 Hz for 0, 2400 Hz for 1, at 300 baud. A 60-minute cassette held ~60-600 KB depending on encoding and tape quality. The Coleco Adam and various home computers used cassette storage as the cheapest option. For bootstrapping, audio cassette storage is achievable with minimal electronics: a tape recorder, a tone decoder, and a UART.

## Cartridge Tape

Modern tape cartridges (LTO, IBM 3592) store 6-18 TB per cartridge on half-inch tape with 8000+ tracks. Servo tracks guide the head precisely. Linear tape-open (LTO-9) stores 18 TB native (45 TB compressed) on a single cartridge. Transfer rate: 400 MB/s. Used exclusively for backup and archival in data centers.


## Inch (1971)

IBM's first floppy: a flexible Mylar disk 8 inches in diameter in a protective sleeve. Single-sided, single-density: 80 KB. Double-sided, double-density: 1.2 MB. Rotation: 360 RPM. Transfer rate: 250 kbps. The floppy introduced inexpensive, transportable data storage to computing.

## Inch (1976)

Shugart Associates shrunk the format. Single-sided 160 KB, double-sided 360 KB, high-density 1.2 MB. The flexible sleeve was genuinely floppy (hence the name). Widely used for software distribution through the 1980s.

## Inch (1982)

Sony's rigid-shell format became the standard. Double-density: 720 KB. High-density (HD): 1.44 MB (the most widely recognized capacity). The rigid plastic shell with sliding metal shutter protected the disk far better than the flexible 5.25-inch sleeve. Rotation: 300 RPM. Track density: 135 tpi. The 1.44 MB floppy persisted as a boot and transfer medium well into the 2000s.


## Compact Disc (CD)

Originally developed for audio (1982, Sony/Philips), adapted for data (CD-ROM, 1985). A 120 mm polycarbonate disc with data encoded as pits molded into the surface, read by a 780 nm infrared semiconductor laser. Pit length varies from 0.83 to 3.05 μm. Track pitch: 1.6 μm (spiral track, ~22,188 revolutions). Capacity: 650-700 MB (Mode 1). Data rate: 150 KB/s at 1× speed, up to 7.2 MB/s at 48×.

Recordable CD (CD-R) uses a dye layer that absorbs laser energy and becomes opaque, mimicking a pit. Writable once. CD-RW uses a phase-change alloy that switches between amorphous (low reflectivity) and crystalline (high reflectivity) states, allowing rewriting (~1000 cycles).

## DVD and Blu-ray

DVD (1995): 650 nm red laser, 0.74 μm track pitch, 4.7 GB single-layer. Blu-ray (2006): 405 nm blue-violet laser, 0.32 μm track pitch, 25 GB single-layer, 128 GB quad-layer. Optical storage trades access time (100-200 ms seek) for high capacity, low media cost, and longevity (50+ year claimed archival life for properly stored discs).


## ROM and EPROM

Mask ROM: programmed during fabrication, unchangeable. PROM: one-time programmable by blowing nichrome fuses. EPROM (Erasable Programmable ROM, 1971): uses floating-gate MOSFETs. A high voltage (12-25V) injects charge onto the floating gate through Fowler-Nordheim tunneling or hot-carrier injection. Erased by exposing the chip to UV light through a quartz window for 15-20 minutes. The UV photons give trapped electrons enough energy to escape. EPROMs are recognizable by the distinctive quartz window on the package. Typical endurance: 100-1000 erase cycles.

## EEPROM

Electrically Erasable Programmable ROM. Each byte can be individually erased and reprogrammed electrically, no UV needed. Byte-level erasure is convenient but makes the cell larger than EPROM (two transistors per cell vs one). Endurance: 10,000-100,000 cycles. Slower write than read (1-10 ms per byte). Used for small configuration stores (BIOS settings, calibration data).

## Flash Memory

Flash is a type of EEPROM that erases in blocks (not byte-by-byte), enabling smaller cells and higher density. Two architectures:

- **NOR flash**: Random access to any word (byte-level reads). Fast read (50-100 ns). Slow erase and write (block-level, seconds). Used for firmware storage and execute-in-place (XIP). Cell: one floating-gate transistor per bit.
- **NAND flash**: Page-level reads (page = 2-16 KB). Faster erase and write than NOR. Much higher density (smaller cells, no random-access decoding overhead). Used for mass storage (SSDs, USB drives, memory cards). A 3D NAND chip stacks 100+ layers vertically, achieving 1 Tb per die.

**Endurance**: SLC (single-level cell, 1 bit/cell): 50,000-100,000 write cycles. MLC (2 bits/cell): 3,000-10,000 cycles. TLC (3 bits/cell): 1,000-3,000 cycles. QLC (4 bits/cell): 100-1,000 cycles. Wear leveling (distributing writes across all blocks) extends usable life. Error correction (BCH or LDPC codes) handles bit errors that increase with wear.

**Floating-gate physics**: A control gate sits above the floating gate, separated by an insulating oxide layer (8-10 nm). Programming: a high voltage (15-20V) on the control gate creates a strong electric field. Electrons tunnel through the thin oxide onto the floating gate (Fowler-Nordheim tunneling). The trapped charge shifts the transistor's threshold voltage, changing its read current. Erasing reverses the process, removing charge from the floating gate.

## Integration Points

| Phase | Storage Technology | Role |
|-------|-------------------|------|
| Early automation | Punch cards, paper tape | Data input for tabulating machines and NC machine tools |
| Early computing | Magnetic drum, magnetic tape | Primary memory and mass storage |
| Industrial computing | Hard disk, floppy disk | Operating system storage, program loading, data exchange |
| Semiconductor fab | EPROM/EEPROM | Firmware for process controllers, calibration data |
| Full computing | Flash memory (NOR/NAND) | Boot firmware, solid-state mass storage |

## Bootstrapping Sequence

The progression of storage technology follows manufacturing capability. At the lowest level, punch cards and paper tape require only paper, punching tools, and mechanical readers. A wooden or metal template guides hole positions; a spring-loaded punch mechanism drives a pin through the card. Readers use either mechanical pin sensing (a pin drops through a hole, closing a contact) or photoelectric sensing (a lamp on one side, a photocell on the other).

Magnetic tape storage requires magnetizable coating (iron oxide particles in a binder), a stable substrate (polyester film for tape, later Mylar for floppy disks), and precision read/write heads. The earliest recording used acicular gamma ferric oxide (γ-Fe₂O₃) particles, 0.5-1.0 μm long, dispersed in a lacquer binder and coated onto the substrate. Particle orientation (aligned by a magnetic field during coating) determines signal-to-noise ratio. Coercivity of γ-Fe₂O₃: 250-400 Oe, suitable for recording densities up to several thousand bits per inch.

Hard disk manufacturing demands sub-micron mechanical precision: platter surface smoothness below 0.25 nm Ra (atomic-scale flatness), head gimbal assemblies with aerodynamic slider designs, and cleanroom assembly (Class 10 or better). These requirements make hard disks a late-stage technology in the bootstrapping sequence, well after precision machining and cleanroom capability are established.

### Punch Card Mechanism Construction

**Punch mechanism**: Mount 12 spring-loaded steel pins (2 mm diameter, 20 mm length) in a brass guide plate (80 × 15 × 5 mm, holes drilled at standard column spacing 3.175 mm). Each pin rides in its guide hole with 0.05 mm clearance. A cam bar or key lever presses the pin through the card (187.3 × 83.3 mm, 0.18 mm thick card stock). Return springs (0.5 mm music wire, 8 mm coil diameter) retract pins between strokes.

**Reading mechanism — pin-sensing**: 12 spring-loaded contact pins (1.5 mm diameter) on a reader head press against the card. Where a hole exists, the pin passes through and contacts a brass roller underneath, closing a circuit. Each contact pin connects to a relay coil (one per row). Card advances via a feed roller (rubber-coated, 10 mm diameter) driven by a solenoid or hand crank through a Geneva mechanism (12-position, one column per step).

**Reading mechanism — photoelectric**: Mount 12 photodiodes (or CdS photocells) on one side of the card path and a 12 V incandescent lamp on the other. Light passes through punched holes. Each photodiode drives a transistor switch (2N2222 or equivalent): base connected through photodiode, collector through relay coil, emitter to ground. Sensing threshold: adjust base resistor so <1 kΩ photocell resistance = logic "1" (hole present).

### Paper Tape Mechanism Construction

**Punch**: Same principle as card punch but using a continuous tape (17.5 mm, 25.4 mm, or 22.3 mm width depending on 5/6/8 channel format). Punch die block has 5-8 holes (1.83 mm diameter for standard tape) plus one smaller sprocket feed hole (1.22 mm diameter, offset from data channels). Tape advance: sprocket wheel (2.54 mm pitch teeth) driven by solenoid pawl ratchet — one tooth per character punched.

**Reader**: Spring-loaded contact pins (1.5 mm) sense holes in moving tape. Tape feed: same sprocket wheel driven by a second solenoid or hand crank. Reading speed (hand-cranked): 10-20 characters/second. Motor-driven: 50-300 characters/second depending on relay response time.

## Storage Hierarchy Summary

| Level | Technology | Access Time | Capacity | Cost/GB |
|-------|-----------|-------------|----------|---------|
| Register | Flip-flops | 0.5 ns | ~1 KB | Very high |
| SRAM | 6T cells | 1-10 ns | 1-64 MB | High |
| DRAM | 1T1C cells | 30-70 ns | 4-128 GB | Medium |
| SSD (NAND) | Flash | 50-150 μs | 256 GB-8 TB | Low |
| HDD | Magnetic disk | 5-10 ms | 1-20 TB | Very low |
| Tape | Magnetic tape | 10-60 s | 6-18 TB | Lowest |

Each layer is roughly 10-100× slower but 10-100× cheaper per bit than the layer above it. Caching (keeping frequently accessed data in faster storage) bridges the speed gaps.

## Key Deliverables

- Punch card and paper tape systems for initial data processing
- Magnetic tape (cassette-based) for low-technology mass storage
- Floppy disk drives for portable data exchange
- Hard disk drives for primary mass storage
- EPROM/EEPROM for firmware and configuration
- Flash memory (NOR and NAND) for solid-state storage
- Understanding of the full storage hierarchy for system design

## Safety & Hazards

- **Magnetic media damage**: External magnetic fields erase or corrupt magnetic storage. A degaussing coil at 5,000 Oe reliably erases a hard disk platter. Static magnetic fields above 50 Oe can corrupt data on tape. Common sources of damaging fields: unshielded speakers (100-500 Oe at the cone magnet surface), degaussing coils, MRI machines (10,000-30,000 Gauss), and even strong refrigerator magnets (50-100 Oe at contact). Keep tapes and disks at least 30 cm from any permanent magnet. Store floppy disks and tapes in steel cabinets for magnetic shielding.
- **Head crashes**: A hard disk head flying 5-10 nm above the platter makes physical contact catastrophic. The kinetic energy of a 10 mg slider at 15 m/s (typical linear velocity at the outer track) is 1.1 mJ, concentrated in a contact area of 0.01 mm². This produces a pressure exceeding 100 MPa, gouging the magnetic coating. Mechanical shock (dropping a running drive from just 2 cm onto a hard surface, a 30 G impulse) causes head crashes that destroy data and the head. Operating shock tolerance: 5-70 G for 2 ms (drive-specific). Non-operating shock tolerance: 200-350 G for 2 ms. Modern drives park heads on a ramp when powered down, but operating drives are fragile. Mount drives with shock-absorbing grommets.
- **Laser safety**: CD/DVD/Blu-ray drives contain Class 1 laser systems (safe under normal operation because the enclosure prevents direct beam access). The internal lasers are Class 3B: CD at 780 nm (infrared, 5 mW), DVD at 650 nm (red, 5-10 mW), Blu-ray at 405 nm (blue-violet, 5-15 mW). A 5 mW laser at 405 nm directed into the eye concentrates on the retina at >100 W/cm², causing permanent retinal burns in <0.1 seconds. Never operate a drive with the enclosure removed. Service manuals require laser safety glasses matched to the specific wavelength (optical density 3+ at 405 nm for Blu-ray, at 650 nm for DVD).
- **Dust and contamination**: Hard disk assemblies are built in Class 100 cleanrooms (≤100 particles ≥0.5 μm per cubic foot). A single smoke particle (0.5 μm) is 50× larger than the 5-10 nm head flying height. A human hair (50-100 μm diameter) is 5,000-10,000× larger. Opening a hard disk outside a clean environment contaminates the platter surface and guarantees a head crash within minutes of operation. Floppy disk shutters exist for the same reason. Cigarette smoke near floppy drives causes read errors as tar deposits accumulate on heads.
- **Tape handling**: Magnetic tape stretches under tension, causing data errors. Reel-to-reel tapes must be stored at 18-24°C and 30-50% relative humidity. High humidity (>60% RH) causes binder hydrolysis (sticky-shed syndrome): the tape binder absorbs moisture and becomes gummy, sticking to the read head and shedding oxide at rates up to 10 μg per pass. Bake affected tapes at 50°C for 8-24 hours in a convection oven to temporarily drive out moisture and restore playability. This treatment works for 1-2 months before re-baking is needed. Never touch the recording surface of any magnetic media: skin oils (sebum) contaminate the head-tape interface, increasing the head gap and degrading signal amplitude.
- **Data integrity**: All storage media degrade over time. Magnetic media lose signal amplitude from print-through (magnetization from adjacent tape layers bleeding through, adding pre-echo and post-echo at -30 to -50 dB) and thermal demagnetization at 0.5-2% signal loss per decade. Optical discs suffer from disc rot (delamination of the reflective aluminum layer when the lacquer protective coating fails, allowing oxidation). Flash memory loses charge from floating gates over time: typical data retention is 10-20 years at 25°C, but only 1-3 years at 85°C (JEDEC standard requires 1 year at 85°C for consumer-grade NAND). Regular data migration (copying to fresh media every 3-5 years for magnetic tape, every 5-10 years for optical discs) is the only reliable archival strategy.
- **Electrical hazards in storage devices**: Hard disk drive PCBs have switching voltage regulators generating 5 V and 12 V supplies from SATA or ATX power. The spindle motor driver can deliver 2 A at 12 V (24 W). A shorted PCB component can reach 150°C, causing burns and potential fire. Never handle drive electronics while powered. The 12 V supply from an ATX PSU can deliver 20+ A, enough to melt wire and start fires if shorted.

## Storage Media Specifications by Era

| Year | Technology | Capacity | Access Time | Transfer Rate | Media Cost | Drive Cost |
|------|-----------|----------|-------------|---------------|-----------|-----------|
| 1890 | Punch card (80-col) | 80 chars (960 bits) | 100-2000 cards/min | 13-33 chars/s | $0.002/card | $2,000-15,000 |
| 1945 | Paper tape (8-channel) | 400 KB per 1000 ft roll | 10-1000 chars/s | 0.01-8 KB/s | $5/roll | $500-3,000 |
| 1952 | Magnetic tape (7-track) | 2.3 MB per reel | Sequential (seconds) | 15 KB/s | $25/reel | $30,000 |
| 1956 | Hard disk (IBM 350) | 5 MB | 600 ms avg | 8.8 KB/s | — | $35,000/yr lease |
| 1965 | Magnetic drum | 1-10 MB | 8-25 ms | 100-500 KB/s | — | $20,000-100,000 |
| 1971 | 8-inch floppy | 80 KB | 360 ms rotation | 250 kbps | $5 | $500 |
| 1978 | 5.25-inch floppy | 360 KB (DS/DD) | 200 ms rotation | 250 kbps | $2 | $400 |
| 1982 | 3.5-inch floppy | 1.44 MB (HD) | 200 ms rotation | 500 kbps | $0.50 | $200 |
| 1982 | CD-ROM | 650-700 MB | 100-400 ms seek | 150 KB/s (1×) | $1-5 | $500 |
| 1991 | Hard disk (3.5-inch) | 40-200 MB | 12-15 ms | 2-5 MB/s | — | $300-600 |
| 1995 | DVD | 4.7 GB | 100-200 ms seek | 1.3 MB/s (1×) | $1-3 | $300 |
| 2000 | Hard disk (3.5-inch) | 20-80 GB | 8-9 ms | 30-66 MB/s | — | $100-200 |
| 2006 | Blu-ray | 25 GB (SL) | 100-200 ms seek | 4.5 MB/s (1×) | $5-10 | $400 |
| 2020 | HDD (3.5-inch) | 10-20 TB | 5-8 ms | 150-250 MB/s | $15-25/TB | $50-300 |
| 2020 | NVMe SSD | 1-8 TB | 20-100 μs | 3-7 GB/s | $100-200/TB | $100-600 |

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Magnetic tape won't read | Binder degradation (sticky-shed), oxide shedding, misalignment | Bake at 50°C for 8-24 hours; clean heads with isopropyl alcohol; check tape tension |
| Hard disk click of death | Head crash or failing actuator | Immediately power down; no field repair possible. Restore from backup |
| Floppy disk read errors | Magnetic degradation, dust, oxide loss | Clean drive heads; try another drive; copy recoverable files immediately |
| Garbled data on tape | Print-through from long storage in spooled state | Retension tape (full forward + rewind); no cure for severe print-through |
| Flash memory write failures | Wear-out — exceeded endurance cycles | Replace media; check wear-leveling stats; restore from backup |
| CD/DVD read errors | Disc rot, scratches, dye degradation | Clean disc surface; try slower read speed; resurface if commercially available |
| EPROM data loss | UV exposure erased floating-gate charge through window | Cover quartz window with opaque label; reprogram if device supports it |
| Data corruption after power loss | Write in progress when power failed | Use journaling filesystem; check ECC/crc; restore from last known good backup |

## See Also

- [Electromechanical Computing](electromechanical.md) — relay and early computing hardware that used punch cards and paper tape
- [Electronic Computing](electronic.md) — semiconductor-based computing requiring firmware storage
- [Semiconductor Applications](../electronics/index.md) — flash and solid-state memory fabrication
- [Thermoplastics](../polymers/thermoplastics.md) — polyester and Mylar substrates for magnetic media
- [Magnetism](../metals/index.md) — magnetic recording principles and materials
- [Precision Instruments](../optics/precision-instruments.md) — sub-micron machining for disk assemblies
- [Telecom / Radio](../telecom/radio.md) — data transmission that drove storage demand
- [Optics / Lasers](../optics/index.md) — optical disc read/write technology

---
*Part of the [Bootciv Tech Tree](../index.md) • [Computing](./index.md) • [All Domains](../index.md)*

---
*Part of the [Bootciv Tech Tree](../index.md) • [Computing & Automation](./index.md) • [All Domains](../index.md)*
