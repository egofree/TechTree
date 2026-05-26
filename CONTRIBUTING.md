# Contributing

## How to Contribute

### Content

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-addition`)
3. Make your changes
4. Run validation: `bash scripts/validate.sh` (must pass all 17 checks)
5. Submit a pull request

### What We're Looking For

- **Corrections**: Technical inaccuracies, missing dependencies, wrong ordering
- **Detail**: Deeper dives into specific processes (e.g., crystal growth methods, purification techniques)
- **Side Quests**: New parallel tracks that support the main tech tree
- **Resources**: References to books, papers, historical accounts, or practical guides
- **Diagrams**: Improved or new Mermaid diagrams

### File Conventions

- Domain content lives in `docs/{domain}/` (one directory per domain, lowercase, hyphenated)
- Each domain has an `index.md` and individual capability `.md` files
- Structured data goes in `data/` as JSON (`nodes.json`, `edges.json`) or YAML (`checklist.yaml`)
- Mermaid diagrams in `diagrams/mermaid/` are auto-generated. Never edit them by hand.
- After changing data files, regenerate diagrams: `bash scripts/generate-diagrams.sh`
- Keep diagrams and text in sync. Update both data and prose when changing content

### Style

- Use clear, direct prose, avoiding jargon where possible
- Include dependency chains and prerequisite references
- Note practical bottlenecks and safety concerns
- Use relative links between documents
