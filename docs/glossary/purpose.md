# Purpose

> **Type**: noun | **Tier**: foundational | **Domains**: all

A one-sentence statement of what a procedure produces, followed by scope (applicable materials, size ranges, limitations), safety requirements (required PPE, specific hazards), materials list (raw materials with specifications), step-by-step instructions, and acceptance/rejection criteria for the finished product.

## Context in the Tech Tree

Purpose — the reason a process, tool, or material exists — provides the organizing principle for technical documentation throughout the tech tree. Every capability article in the knowledge base is structured to answer "what does this produce and why does it matter?" In [Casting](../machine-tools/casting.md), the purpose is to produce complex metal shapes from reusable molds. In [Pharmacology](../health/pharmacology.md), the purpose is to produce standardized therapeutic preparations from raw plant or chemical materials. Understanding purpose drives design decisions: a tool designed for precision work looks very different from one designed for heavy stock removal.

## Technical Details

In technical documentation, the purpose statement serves as a contract between the author and the reader — it tells the reader whether the document is relevant to their problem before they invest time reading further. A well-written purpose statement specifies what is produced, from what inputs, and to what quality standard.

The purpose structure also organizes the dependency chain: each capability's purpose defines its outputs, which become inputs (materials or tools) for downstream capabilities. Iron smelting produces wrought iron and steel (purpose), which are inputs for machine tools, which are inputs for precision manufacturing, which is required for semiconductor equipment. The tech tree is essentially a chain of purposes, each enabling the next.

For safety documentation, purpose also means identifying why specific precautions exist. "Wear leather gloves" is a rule; "molten metal at 700°C causes instant deep burns on contact" is the purpose that makes the rule memorable and encourages compliance even when supervision is absent.

## Related Terms

- [Procedure](./procedure.md) — the steps that fulfill a purpose
- [Requirements](./requirements.md) — specifications that define whether purpose is achieved
- [Products](./products.md) — the tangible outputs that realize the purpose

## Appears In

- [Casting](../machine-tools/casting.md)
- [Pharmacology](../health/pharmacology.md)
- [Iron & Steel Production](../metals/iron-steel.md)
