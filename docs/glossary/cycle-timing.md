# Cycle timing

> **Type**: material | **Tier**: important | **Domains**: computing

0.5-5 μs full read-write cycle. Read is destructive (flips the core to "0"), so every read must be followed by a rewrite of the original value. Non-destructive read variants exist but add complexity.
