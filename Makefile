SHELL := /bin/bash
.SHELLFLAGS := -ec

.PHONY: all validate diagrams d2-diagrams build validate-site clean help

help: ## Show this help message
	@echo "bootciv tech-tree-bootstrap — available targets:"
	@echo ""
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

all: validate diagrams build validate-site ## Run full pipeline: validate → diagrams → build → validate-site

validate: ## Validate data integrity (16 checks)
	bash scripts/validate.sh

diagrams: ## Generate Mermaid diagrams from data
	bash scripts/generate-diagrams.sh

d2-diagrams: ## Generate D2 diagrams from data
	bash scripts/generate-d2-diagrams.sh

build: ## Build offline-first static site
	bash scripts/build-site.sh

validate-site: ## Validate built site (10 checks)
	bash scripts/validate-site.sh

clean: ## Remove generated site/ and rendered diagrams
	rm -rf site/
	rm -rf diagrams/rendered/
