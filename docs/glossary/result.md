# Result

> **Type**: noun | **Tier**: foundational | **Domains**: chemistry, measurement, quality

The measured outcome of a process, test, or transformation. Results are the feedback mechanism that closes the loop between intention and reality — without measuring results, there is no way to know whether a process is working correctly, whether materials meet specification, or whether a change improved or degraded output quality.

## Context in the Tech Tree

In [Quality Control & Testing](../chemistry/packaging-testing.md), test results determine whether a product is fit for use — tensile strength results confirm a steel batch meets specification, chemical analysis results verify alloy composition, hardness test results validate heat treatment. In every production process, the result (yield, purity, strength, dimensions) is the metric against which process parameters are optimized.

In [Quality Control & Testing](../chemistry/packaging-testing.md), test results from each wafer (yield, speed bin, defect map) determine which chips are usable and at what performance tier. The result of the entire semiconductor manufacturing chain — from silicon purification through lithography through packaging — is expressed as the final test result: working chips per wafer.

## Technical Details

A result is only as meaningful as the measurement that produced it. Key principles:

- **Repeatability**: The same measurement on the same sample should give the same result. If results vary, either the process is unstable or the measurement method is inadequate.
- **Accuracy vs. precision**: A result can be precisely wrong (consistently measuring the wrong value) or imprecisely correct (scattered around the true value). Good results require both accuracy (correct on average) and precision (consistent).
- **Significant figures**: A result should not express more precision than the measurement supports. Reporting "99.73% pure" when the analytical method has ±0.5% accuracy misleads the user into false confidence.
- **Interpretation**: Raw results require interpretation in context. A hardness reading of 45 HRC means different things for a file (too soft), a structural beam (appropriate), and a cutting tool (far too soft).

In bootstrapping, results from simple tests (spark test for carbon content, bend test for ductility, fracture appearance for grain size) provide the first feedback loops. As measurement capability improves, results become more quantitative and the feedback loops tighten, enabling tighter process control and more consistent product quality.

## Related Terms

- [Testing](./testing.md) — the process of obtaining results through controlled measurement
- [Source](./source.md) — source materials determine the range of achievable results
- [Accuracy](./accuracy.md) — the correctness of a result relative to the true value
- [Yield](./yield.md) — production yield as a result of the manufacturing process

## Appears In

- [Quality Control & Testing](../chemistry/packaging-testing.md)
- [Precision Metrology](../measurement/precision-metrology.md)
