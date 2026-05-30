# Magnetic Tape

> **Type**: noun | **Tier**: critical | **Domains**: computing, knowledge

A data storage medium consisting of magnetizable particles (iron oxide or chromium dioxide) bonded to a flexible substrate (polyester film, earlier paper or acetate). Early magnetic tape systems recorded data on paper or plastic tape coated with iron oxide particles, achieving densities of 100-500 bits per inch. Magnetic tape was the backbone of mass data storage from the 1950s through the 1990s and remains in use for archival backup due to low cost per gigabyte.

## Context in the Tech Tree

Magnetic tape occupies a critical position in the computing domain's storage progression. It bridges the gap between paper-based storage (punch cards, paper tape) and magnetic disk storage. For a bootstrapping civilization, magnetic tape provides the first high-capacity, rewritable storage medium — essential for program storage, data logging, and system bootstrapping once basic electronics become available.

The technology requires polyester film substrate (from the polymers domain), iron oxide particles (from chemistry), binder chemistry, and precision coating application. Cassette-based storage at 300-2400 baud is achievable with moderate electronics, while reel-to-reel systems at higher density demand better head gap control and tape transport mechanics.

## Technical Details

Magnetic recording exploits the hysteresis loop of ferromagnetic materials. A current through the write head generates a localized magnetic field that magnetizes a tiny region of the moving tape. Reading uses the magnetized region to induce voltage in a read head via Faraday's law. Recording density depends on head gap width, tape-to-head contact, and particle coercivity.

Tape storage is sequential — data must be accessed in order, unlike the random access of magnetic disks. This makes tape slower for interactive use but highly efficient for streaming large datasets, backups, and archives. Modern tape cartridges (LTO-9) store 18 TB native per cartridge, with data rates of 400 MB/s. The medium's removable nature enables physical data transport and air-gapped archival storage.

## Related Terms

- [Measurement](./measurement.md) — magnetic recording heads require precise manufacturing
- [Materials](./materials.md) — substrate and magnetic particle materials
- [Manufacturing](./manufacture.md) — tape coating is a precision manufacturing process

## Appears In

- [Data Storage](../computing/data-storage.md)
- [Electronic Computing](../computing/electronic.md)
- [Libraries](../knowledge/libraries.md)
