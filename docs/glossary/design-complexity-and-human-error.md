# Design complexity and human error

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

A billion-transistor GPU design requires 100-500 engineer-years of effort. Human errors in HDL code, constraint specification, or floorplanning cause first-silicon failures (respins cost $5-20M per attempt). Methodology enforcement (lint checks, CDC/RDC analysis for clock domain crossings, power intent verification with UPF) catches classes of errors automatically. The trend toward higher abstraction (high-level synthesis from C/C++, system-level design in SystemC) reduces human error by redu...
