# Frontend Guide

**What:** observatory views for dashboard, repositories, graph, risk, simulation, temporal analysis, and AI intelligence.

**Input:** typed JSON from `/api/v1`. **Output:** views and user actions. UI code does not calculate authoritative metrics or access Neo4j.

Own `frontend/`. Shared types belong in `frontend/src/types`; transport belongs in `frontend/src/services`; feature behavior belongs under `frontend/src/features/`. Run `npm run build`.
