# RAS and error correction

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

Large SRAM arrays and register files are vulnerable to soft errors (cosmic ray neutrons, alpha particles from packaging materials). ECC (error-correcting code) memory protects SRAM — single-error correction, double-error detection (SECDED). Parity checking on register files and caches. Hardware scrubbers periodically read and correct accumulated single-bit errors before they become double-bit failures. For compute results, algorithms use redundancy (checksums, residue checking) to detect comp...
