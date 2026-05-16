# Contributing

## How to Contribute

### Content

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-addition`)
3. Make your changes
4. Ensure Mermaid diagrams are valid (use [mermaid.live](https://mermaid.live))
5. Submit a pull request

### What We're Looking For

- **Corrections**: Technical inaccuracies, missing dependencies, wrong ordering
- **Detail**: Deeper dives into specific processes (e.g., crystal growth methods, purification techniques)
- **Side Quests**: New parallel tracks that support the main tech tree
- **Resources**: References to books, papers, historical accounts, or practical guides
- **Diagrams**: Improved or new Mermaid diagrams

### File Conventions

- Phase docs go in `docs/core-tech-tree/phase-XX-name.md`
- Side quest docs go in `docs/side-quests/sq-XX-name.md`
- Mermaid source files use `.mmd` extension in `diagrams/mermaid/`
- Structured data goes in `data/` as JSON or YAML
- Keep diagrams and text in sync — update both when changing content

### Style

- Use clear, direct prose — avoid jargon where possible
- Include dependency chains and prerequisite references
- Note practical bottlenecks and safety concerns
- Use relative links between documents
