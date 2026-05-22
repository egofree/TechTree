# Scan chains

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Replace every flip-flop with a scan flip-flop (adds a multiplexer and scan input). In normal mode, flip-flops operate normally. In scan mode, all flip-flops are chained into a long shift register. Test patterns are shifted in serially, one clock cycle applied, and results shifted out. Converts sequential testing (2^N states) into combinational testing (N patterns). Typical industrial designs have 100-10,000 scan chains operating in parallel to reduce test time.
