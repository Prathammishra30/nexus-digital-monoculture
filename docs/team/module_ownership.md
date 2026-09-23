# Module Ownership

## Tech Lead
Owns `ARCHITECTURE.md`, `docs/architecture/`, `nexus_domain/`, `pyproject.toml`, and cross-module contract reviews. Tests: `tests/contract/`.

## Backend Developer
Owns `backend/` and `graph/`. Inputs are validated API requests or canonical domain objects; outputs are API responses or graph persistence results. Must not edit provider adapters or frontend feature logic.

## Frontend Developer
Owns `frontend/`. Inputs are backend JSON contracts; outputs are user-facing feature components. Must not calculate risk or query Neo4j.

## AI Developer
Owns `ai-engine/`, `ai_engine/`, and `discovery-engine/`. Inputs are raw artifacts and deterministic evidence; outputs are validated canonical observations. Must not bypass `nexus_domain/` validation.
