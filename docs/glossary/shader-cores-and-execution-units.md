# Shader cores and execution units

> **Type**: material | **Tier**: important | **Domains**: vlsi-scaling

Modern GPUs contain hundreds to thousands of identical processing cores (shader processors). Each core executes the same instruction on different data lanes (SIMD — Single Instruction, Multiple Data). Warp/wavefront scheduling groups 32-64 threads. Latency hiding: when one warp stalls on memory, another warp executes on the same core. This is why GPUs tolerate high memory latency — thousands of concurrent threads keep arithmetic units busy.
