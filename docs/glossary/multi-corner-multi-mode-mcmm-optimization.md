# Multi-corner multi-mode (MCMM) optimization

> **Type**: noun | **Tier**: important | **Domains**: vlsi-scaling

Modern designs must meet timing at multiple operating conditions simultaneously: fast process corner at low temperature (hold checks), slow process corner at high temperature (setup checks), multiple supply voltage modes (nominal, low-power), and multiple clock configurations. Each combination is a "scenario." The optimizer must find a single netlist that passes all scenarios — a change that helps one scenario may hurt another. MCMM optimization is computationally expensive but necessary for ...
