# NEXUS API Endpoints Reference

The NEXUS API is served via FastAPI with an interactive Swagger UI at `/docs`.

## Base URLs
- Local Development: `http://localhost:8000/api/v1`
- OpenAPI Specification: `http://localhost:8000/openapi.json`

## Endpoints Summary

### Repositories (`/repositories`)
- `POST /repositories/analyze`: Enqueue a repository for dependency scanning.
- `GET /repositories`: List paginated indexed repositories.
- `GET /repositories/{repo_id}`: Retrieve detailed repository scan results and risk scores.

### Dependencies (`/dependencies`)
- `GET /dependencies`: Query discovered nodes filtered by layer or search string.
- `GET /dependencies/{dep_id}`: Node details, version resolution, and license.
- `GET /dependencies/{dep_id}/dependents`: List all upstream repositories depending on this node.

### Risk & Concentration (`/risk`)
- `GET /risk/ecosystem`: Global macroscopic concentration and risk scorecards.
- `GET /risk/concentration`: HHI and Monoculture Index for a specific layer.
- `GET /risk/repository/{repo_id}`: Individual repository risk assessment.

### Simulation (`/simulation`)
- `POST /simulation/simulate-failure`: Simulate cascading failure caused by target node outages.
- `GET /simulation/blast-radius/{node_id}`: Downstream blast radius analysis.
- `POST /simulation/diversify`: Generate diversification recommendations to mitigate monoculture risk.
