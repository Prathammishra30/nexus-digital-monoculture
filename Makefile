.PHONY: help install test test-backend test-ai test-contract lint format dev-backend docker-up docker-down schema-init validate

PYTHON ?= python

help:
	@echo "NEXUS - Digital Monoculture & Systemic Risk Observatory"
	@echo ""
	@echo "Available commands:"
	@echo "  make install        Install development and runtime dependencies"
	@echo "  make test           Run all pytest test suites (unit, contract, integration)"
	@echo "  make test-backend   Run backend API tests"
	@echo "  make test-ai        Run AI engine tests"
	@echo "  make test-contract  Run cross-module schema contract tests"
	@echo "  make validate       Run architecture and schema validation audit"
	@echo "  make dev-backend    Start local FastAPI development server"
	@echo "  make docker-up      Launch Neo4j, backend, and frontend containers"
	@echo "  make docker-down    Stop Docker containers"
	@echo "  make schema-init    Apply Cypher schema constraints and indexes to Neo4j"

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest tests/unit tests/contract tests/integration backend/tests ai-engine/tests -v

test-backend:
	$(PYTHON) -m pytest backend/tests -v

test-ai:
	$(PYTHON) -m pytest ai-engine/tests -v

test-contract:
	$(PYTHON) -m pytest tests/contract -v

validate:
	$(PYTHON) scripts/validation/validate_architecture.py

dev-backend:
	$(PYTHON) -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload

docker-up:
	docker compose up -d

docker-down:
	docker compose down

schema-init:
	$(PYTHON) scripts/setup/init_neo4j.py
