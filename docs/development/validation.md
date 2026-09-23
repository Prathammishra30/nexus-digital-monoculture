# Validation Commands

From the repository root:

```text
python -m compileall -q backend nexus_domain ai_engine discovery-engine risk-engine graph
python -m pytest -q
python scripts/validation/validate_architecture.py
```

From `frontend/`:

```text
npm ci
npm run build
```

Docker Compose syntax can be checked with `docker compose config` when Docker is installed. A live Neo4j instance is required only for graph integration tests, not unit or contract tests.
