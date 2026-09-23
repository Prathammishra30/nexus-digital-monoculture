# NEXUS Developer Contributing & Branching Guidelines

Welcome to the NEXUS project. These guidelines ensure our distributed team can develop in parallel without breaking cross-module contracts or stepping on each other's code.

---

## 1. Branch Strategy

The repository uses strict branch isolation mapped to development roles:

| Branch Name | Primary Owner | Scope of Work |
| :--- | :--- | :--- |
| `main` | **Tech Lead** | Production-stable codebase. Direct commits prohibited. |
| `backend` | **Backend Developer** | `backend/`, `graph/`, Neo4j client & queries, REST API routes. |
| `frontend` | **Frontend Developer** | `frontend/`, UI features, state hooks, graph visualization. |
| `ai-engine` | **AI Developer** | `ai-engine/`, model router, providers, prompts, validation. |
| `discovery-engine` | **AI / Backend Developer** | `discovery-engine/`, parsers, detectors, GitHub fetcher. |
| `integration` | **Tech Lead** | Staging branch for cross-module testing before merging to `main`. |

### Branch Rules
1. **Never commit directly to `main`**.
2. **Never force-push (`git push -f`)** to shared branches.
3. Feature branches should branch off their respective module branch (e.g. `feature/npm-lockfile` off `discovery-engine`).
4. Merges into `main` occur strictly via Pull Requests passing all automated CI tests and approved by the Tech Lead.

---

## 2. Cross-Module Contract Changes

The following schema files define system-wide contracts:
- `backend/models/*.py`
- `ai-engine/schemas/*.py`
- `graph/neo4j/schema/*.cypher`
- `frontend/src/types/index.ts`

> [!WARNING]
> Changing any contract file requires explicit review from the Tech Lead and affected module owners before merging.

---

## 3. Pre-Commit Checklist

Before opening a Pull Request:
1. Ensure all code compiles cleanly:
   ```bash
   python -m compileall backend discovery-engine ai-engine risk-engine graph tests scripts
   ```
2. Run the test suite:
   ```bash
   python -m pytest tests/unit tests/contract tests/integration backend/tests ai-engine/tests -v
   ```
3. Run the architecture validator:
   ```bash
   python scripts/validation/validate_architecture.py
   ```
4. Verify no environment variables or API keys were committed (`git status` and `git diff`).
