SHELL := /bin/bash
.SHELLFLAGS := -ec

.PHONY: all validate diagrams d2-diagrams build validate-site test clean help wikidata-search wikidata-apply wikidata-enrich

help: ## Show this help message
	@echo "bootciv tech-tree-bootstrap — available targets:"
	@echo ""
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

all: validate diagrams build validate-site ## Run full pipeline: validate → diagrams → build → validate-site

validate: ## Validate data integrity (16 checks)
	python3 scripts/validate.py

diagrams: ## Generate Mermaid diagrams from data
	python3 scripts/generate-diagrams.py --format mermaid

d2-diagrams: ## Generate D2 diagrams from data
	python3 scripts/generate-diagrams.py --format d2

build: ## Build offline-first static site
	bash scripts/build-site.sh

validate-site: ## Validate built site (10 checks)
	bash scripts/validate-site.sh

test: ## Run conformance test suite
	bash scripts/run_conformance_tests.sh

clean: ## Remove generated site/ and rendered diagrams
	rm -rf site/
	rm -rf diagrams/rendered/

wikidata-search: ## Search Wikidata for entity Q-IDs, output scored TSV
	cd scripts && python3 wikidata-crawler.py search --output ../data/wikidata-matches.tsv

wikidata-apply: ## Apply approved Q-IDs from reviewed TSV to entity files
	cd scripts && python3 wikidata-crawler.py apply ../data/wikidata-matches-reviewed.tsv

wikidata-enrich: ## Build multilingual enrichment cache from Wikidata
	cd scripts && python3 wikidata-crawler.py enrich
