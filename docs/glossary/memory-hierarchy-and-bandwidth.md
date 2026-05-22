# Memory hierarchy and bandwidth

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

GPU performance is often memory-bound, not compute-bound. GDDR (Graphics DDR) provides 300-1000+ GB/s bandwidth through wide interfaces (256-512 bit bus, 16-32 memory chips). HBM (High Bandwidth Memory) stacks DRAM dies vertically on silicon interposer with 1024-4096 signal traces — bandwidth exceeds 1 TB/s in a fraction of the board area. Cache hierarchy: L1 (per core, 16-128 KB), L2 (shared, 1-8 MB), L3/system cache (optional, 16-64 MB). Cache coherency between cores is optional — many GPU ...
