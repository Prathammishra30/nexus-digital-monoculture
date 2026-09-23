# API Contracts

FastAPI routes live under `/api/v1`. Route handlers validate requests and call services; services coordinate engines.

- Repositories: register and list repository scan subjects.
- Dependencies: expose canonical dependency relationships.
- Risk: expose engine-produced concentration and risk observations.
- Simulation: accept what-if requests and return typed results.
- Intelligence: accept transformation requests and expose evidence/confidence summaries.

Use Pydantic models in `backend/models/`. Add a contract test under `tests/contract/` for every cross-module shape.
