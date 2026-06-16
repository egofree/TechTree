# Supersonic Aerodynamics

> **Node ID**: `aerospace.supersonic-flight.supersonic-aerodynamics`
> **Domain**: [Aerospace](./index.md)
> **Parent**: [Supersonic & Hypersonic Flight](./supersonic-flight.md)
> **Dependencies**: [`aerospace.supersonic-flight`](supersonic-flight.md)
> **Outputs**: area_ruled_airframe, supersonic_wing
> **Timeline**: Years 30-80
> **Critical**: No

## Overview

Supersonic aerodynamics is the body of compressible-flow theory and design practice that lets an airframe fly efficiently above Mach 1. Three problems dominate. First, **wave drag** — the energy radiated away by the shock waves attached to every change in the aircraft's cross-section — must be minimized by *area ruling*, the deliberate shaping of the fuselage so its total cross-sectional area varies smoothly from nose to tail. Second, the **supersonic airfoil** must be thin (3–5% thickness-to-chord ratio), sharp-edged, and nearly flat, generating lift through small angle of attack rather than camber — the biconvex, double-wedge, and ogive-delta sections. Third, the **lift-to-drag ratio** collapses from subsonic values of 18 to supersonic values of 7–8, multiplying fuel burn.

This process produces the airframe shapes — area-ruled fuselages, thin delta or trapezoidal wings, sharp inlets — that the other three supersonic-flight processes build upon. See the parent [Supersonic & Hypersonic Flight](./supersonic-flight.md) article for the full Mach-regime table, the Concorde / SR-71 / X-15 reference specifications, and the worked area-rule example.

## Key Techniques

- **Whitcomb area rule** (1952) — pinch the fuselage at the wing root so total cross-section stays smooth.
- **Sears-Haack body** — theoretical minimum-drag shape; the design target.
- **Biconvex / double-wedge airfoils** — 3–5% thickness, sharp leading edges.
- **Supersonic leading-edge sweep** — sweep angle > Mach angle (μ = arcsin(1/M)) gives a subsonic leading edge, dramatically reducing drag.
- **Natural laminar flow (NLF)** — favorable pressure gradients keep the boundary layer laminar over 30–60% chord.

## Prerequisites

- **[Aviation](./aviation.md)** — subsonic aerodynamics, wind-tunnel practice, airframe manufacturing base inherited from piston-era flight.
- **[Supersonic & Hypersonic Flight](./supersonic-flight.md)** — parent capability.
- Compressible-flow mathematics (isentropic, Rayleigh, Fanno, normal/oblique shock relations) — *analytical foundation*.

---

*Part of the [Bootciv Tech Tree](../index.md) • [Aerospace](./index.md)*
