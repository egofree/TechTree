# RF Front-Ends

> **Node ID**: `space-ground-ops.ground-stations.rf-front-ends`
> **Domain**: [Space Ground Ops](./index.md)
> **Parent**: [Ground Stations](./ground-stations.md)
> **Dependencies**: [`space-ground-ops.ground-stations`](./ground-stations.md)
> **Outputs**: rf_front_ends
> **Timeline**: Years 50+

## Overview

The subsystem between the feed horn and the digital back end. It sets the system noise
temperature and therefore, almost single-handedly, the link budget.

## Low-Noise Amplifiers

The first amplifier after the feed is a **cryogenic LNA** cooled to **20–50 K** by a
closed-cycle helium or Stirling cryocooler. Receiver noise temperature is then in the same
range; system noise temperature T_sys (adding sky noise, feed loss, receiver) is typically
**30–80 K** at X-band under clear sky, rising toward 100 K at low elevation.

Every kelvin of T_sys reduction is as valuable as added antenna area and far cheaper — hence
the cryogenic LNA is the most fiercely engineered component in a deep-space receiver.

## Downconversion and IF

After amplification the RF is mixed down to an intermediate frequency (a few hundred MHz to a
few GHz). The IF is carried on coax or analogue optical fibre to a signal-processing centre
that may be hundreds of metres or kilometres from the antenna. Digitisation happens at or
near the IF; modern digital back ends sample the IF and do filtering, channelisation, and
decoding in FPGA / ASIC (software-defined radio).

## See Also

- [Ground Stations](./ground-stations.md) — parent capability
- [Antenna Systems](./ground-stations.antenna-systems.md) — the dish that feeds the LNA
