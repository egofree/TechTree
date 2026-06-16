# Propellant Recycling

> **Node ID**: space-resources.space-recycling.propellant-recycling
> **Parent**: [Space Recycling](./space-recycling.md)
> **Domain**: [Space Resources](./index.md)
> **Dependencies**: *(inherits from parent capability)*
> **Timeline**: Years 80-200+
> **Outputs**: recycled_materials
> **Critical**: No

Recovery of residual propellants and vented gases on orbit, capturing boil-off from cryogenic tanks, reclaiming residual propellant after engine shutdown, and recycling vented cabin and ullage gases to reduce consumable mass loss during long-duration missions.

## Boil-Off Recovery

Cryogenic propellants continuously evaporate because no thermal insulation is perfect. A passive LOX tank (90 K) loses 0.05-0.5%/day; an LH2 tank (20 K) loses 0.1-1.0%/day. Over a 1,000-day Mars transit, unmanaged boil-off would evaporate the entire propellant load.

| Propellant | Boil-off rate (passive) | Recovery method | Energy cost |
|------------|--------------------------|-----------------|-------------|
| LOX (90 K) | 0.05-0.5%/day | Cryocooler recondensation | 5-15 W per kg/day |
| LH2 (20 K) | 0.1-1.0%/day | Cryocooler + para-ortho conversion | 30-100 W per kg/day |

Zero-boil-off (ZBO) systems use active cryocoolers to recondense vented vapour back into the tank, and route cryocooler waste heat to a Stirling generator for partial electricity recovery.

## Residual Propellant Recovery

After engine shutdown, 1-3% of loaded propellant remains trapped in feed lines, manifolds, and ullage. Recovery methods include positive-expulsion bladders, inert gas (helium) purge to a recovery tank, and cold-trap or zeolite vapour capture.

## Vent Gas Reclamation

A station vents a steady stream of gases (cabin leakage, experiment venting, ullage from tank transfers). Reclamation uses selective membrane separation (O2/N2/CO2 by differential permeation), cryogenic distillation (O2 at 90 K, N2 at 77 K, CO2 sublimation at 195 K), and Sabatier reprocessing where recovered CO2 and H2 react over a ruthenium catalyst to produce methane and water — closing both the carbon and hydrogen loops. Methane pyrolysis further splits CH4 into solid carbon (for storage or structural use) and recoverable hydrogen.

[↑ Back to Space Recycling](./space-recycling.md)
