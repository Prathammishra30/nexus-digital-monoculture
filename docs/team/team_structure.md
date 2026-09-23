# Team Structure

NEXUS has four implementation owners and one integration rule: shared contracts are reviewed by the tech lead before merge.

- Tech lead: architecture, research boundaries, cross-module contracts, integration, and risk composition.
- Backend developer: `backend/`, `graph/`, Neo4j adapters, API orchestration.
- Frontend developer: `frontend/`, typed API consumption, feature views.
- AI developer: `ai-engine/`, `ai_engine/`, `discovery-engine/`, evidence-grounded transformation.

The `tests/` directory is shared and changes with the owning module. No owner changes another owner\'s algorithms without review.
