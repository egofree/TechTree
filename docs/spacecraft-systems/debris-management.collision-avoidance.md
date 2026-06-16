# Collision Avoidance

> **Node ID**: spacecraft-systems.debris-management.collision-avoidance
> **Domain**: [Spacecraft Systems](./index.md)
> **Dependencies**: [`spacecraft-systems.debris-management`](./debris-management.md)
> **Enables**: None
> **Timeline**: Years 40-200+
> **Outputs**: conjunction_reports
> **Critical**: No

Collision avoidance is the process of predicting close approaches between operational spacecraft and catalogue debris, computing the probability of collision (Pc), and planning Collision Avoidance Maneuvers (CAMs) when Pc exceeds the operator's threshold (typically 1×10⁻⁴). The mean LEO impact velocity is 10 km/s — a 1 cm fragment at this speed carries enough energy to disable or destroy a satellite. See [Debris Management](./debris-management.md) for the full conjunction assessment workflow.

## Overview

The SSN screens all operational spacecraft against the catalogue daily, issuing Conjunction Data Messages (CDMs) for any approach within a 10 km warning volume. Each CDM is refined with higher-fidelity propagation, and the Pc is computed using the Alfano method — integrating the combined position uncertainty over the collision cross-section. When Pc exceeds threshold, a CAM is planned 24–48 hours before Time of Closest Approach.

## Key Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Pc action threshold | 1×10⁻⁴ (NASA) | Varies by operator |
| Typical CAM delta-v | 0.01–0.5 m/s | In-track burn |
| CAM timing | TCA−12 to TCA−6 hr | Last feasible execution |
| CAM effectiveness | 1–3 orders of Pc | Shifts along-track 1–10 km |
| False alarm rate | 80–95% | Resolves on covariance refinement |

## Prerequisites

- Conjunction screening processing ([computing](../computing/))
- Tracking data for covariance refinement ([measurement](../measurement/))
- Radar infrastructure for catalogue maintenance ([electronics](../electronics/))

## See Also

- [Debris Management](./debris-management.md) — parent capability
- [Debris Tracking](./debris-management.debris-tracking.md) — provides catalogue data
- [Post-Mission Disposal](./debris-management.post-mission-disposal.md) — reduces conjunction load

---

*Part of the [Bootciv Tech Tree](../index.md) • [Spacecraft Systems](./index.md)*
