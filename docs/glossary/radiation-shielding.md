# Radiation Shielding

> **Type**: application | **Tier**: specialized | **Domains**: metals

Tungsten's density (19.25 g/cm³, comparable to gold and uranium) makes it effective for X-ray and gamma shielding — used as collimators in medical imaging and radiotherapy. Preferred over lead (11.3 g/cm³) where space is constrained because a thinner tungsten layer provides equivalent attenuation.

## Context in the Tech Tree

Radiation shielding is a specialized application of dense materials, documented within [Tungsten & Refractory Metals](../metals/refractory-metals.md). While not a primary bootstrapping concern, radiation shielding becomes relevant once X-ray tubes, radiotherapy equipment, or nuclear processes are developed. The shielding requirement also applies to [Advanced Ceramics](../ceramics/advanced-ceramics.md) and glass formulations used in radiation environments.

## Technical Details

Radiation shielding works by absorbing ionizing radiation through three mechanisms: photoelectric effect (dominant for low-energy X-rays, proportional to Z⁴⁻⁵), Compton scattering (dominant for mid-energy gamma rays, proportional to electron density), and pair production (dominant above 1.022 MeV, proportional to Z²). For all three mechanisms, higher atomic number (Z) and higher density improve shielding effectiveness.

Tungsten (Z=74, density 19.25 g/cm³) is significantly more effective per unit thickness than lead (Z=82, density 11.3 g/cm³) despite lead's higher atomic number, because tungsten's density advantage more than compensates. A tungsten shield needs roughly 60% of the thickness of an equivalent lead shield, making tungsten preferred in space-constrained applications like medical collimators, where thin shielding jaws define the X-ray beam geometry.

Lead remains the dominant shielding material for large-area applications (protective aprons, room shielding walls) because it is vastly cheaper and easier to fabricate than tungsten. Lead sheets can be cut, bent, and formed with hand tools; tungsten requires powder metallurgy (sintering at 2000-2200°C) or swaging to form useful shapes.

Concrete (density ~2.3 g/cm³) is used for room-scale shielding — a 1.5-2 m concrete wall provides adequate shielding for diagnostic X-ray rooms. Barite concrete (with barium sulfate aggregate, density ~3.5 g/cm³) reduces the required thickness.

## Related Terms

- [Properties](./properties.md) — density and atomic number as shielding-relevant properties
- [Products](./products.md) — shielding as a product form of dense metals
- [Requirements](./requirements.md) — shielding thickness specifications

## Appears In

- [Tungsten & Refractory Metals](../metals/refractory-metals.md)
- [Advanced Ceramics](../ceramics/advanced-ceramics.md)
