# NEXUS — Digital Monoculture & Systemic Risk Observatory
## Production Architecture Specification

NEXUS models, analyzes, and visualizes hidden dependency concentration and systemic/common-mode failure risks across modern software ecosystems.

---

## 1. The 9 Core Layers

NEXUS classifies all entities into nine distinct ontological layers:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Application Layer       (User Repositories, Services)    │
│ 2. Package Layer           (NPM, PyPI, Maven, Go Modules)   │
│ 3. API Layer               (Stripe, Twilio, SendGrid)       │
│ 4. Cloud Layer             (AWS, GCP, Azure, Cloudflare)    │
│ 5. AI Model Layer          (OpenAI, Anthropic, HuggingFace) │
│ 6. Identity Layer          (Auth0, Okta, Firebase Auth)     │
│ 7. Infrastructure Layer    (Docker base images, Terraform)  │
│ 8. Data Layer              (Managed DBs, Warehouses)        │
│ 9. Human / Maintainer Layer(Committers, Bus Factor)         │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Core End-to-End Pipeline

```
GitHub Repository
       │
       ▼
[Discovery Engine] ──────────► Deterministic Parsers (NPM, PyPI, Go, Maven, Docker, TF)
       │                       └► Explicit Evidence (Dependencies, Manifests, Keys)
       ▼
Raw Dependency Representation
       │
       ▼
[AI Engine] ─────────────────► Model Router (Task-based routing: OpenAI / Anthropic / Local)
       │                       └► Semantic Interpretation (Implicit APIs, SDKs, Cloud)
       ▼
Structured AI Output
       │
       ▼
[Validation & Confidence] ───► Schema Validation + Grounding Check against deterministic tokens
                               └► Status: CONFIRMED | PROBABLE | UNCERTAIN | REJECTED
       │
       ▼
Canonical NEXUS Objects
       │
       ▼
[Neo4j Graph Database] ──────► 9-Layer Nodes + Relationships (DEPENDS_ON, RELIES_ON, etc.)
       │
       ▼
[Risk Engine] ───────────────► HHI, Monoculture Index, Bus Factor, Blast Radius, Simulation
       │
       ▼
[FastAPI Backend] ───────────► REST API (`/api/v1`)
       │
       ▼
[Frontend Observatory] ──────► React / Next.js Visualization & What-If Simulation
```

---

## 3. Core Architectural Principles

1. **Not a Generic Chatbot**:
   AI is used strictly as an intelligence and semantic transformation engine to interpret implicit dependencies that cannot be extracted deterministically.
2. **Deterministic Primacy**:
   Explicit facts (e.g. `express@4.18.2` in `package.json`) are extracted with 100% deterministic code. AI is called only to classify, disambiguate, or infer complex multi-layer signals.
3. **Rigorous Hallucination Control**:
   Every AI output passes through `ai-engine/validation/` to ensure:
   - Schema adherence (Pydantic).
   - Evidence grounding (must link to file path and line/token evidence).
   - Confidence scoring:
     - `CONFIRMED` ($\ge 0.85$ + verified evidence)
     - `PROBABLE` ($0.70 - 0.84$)
     - `UNCERTAIN` ($0.50 - 0.69$)
     - `REJECTED` ($< 0.50$ or missing evidence)
4. **Multi-Model Provider Independence**:
   No hardcoded vendor SDKs in business logic. The `ModelRouter` selects the appropriate provider (`OpenAI`, `Anthropic`, `Local`) based on the task category (`CLASSIFICATION`, `EXTRACTION`, `SEMANTIC_ANALYSIS`, `ARCHITECTURE_ANALYSIS`, `EMBEDDING`, `GRAPH_REASONING`).
5. **Snapshot & Temporal Analysis**:
   The graph and risk engine support versioned snapshotting to measure **Monoculture Velocity** ($V_m = \frac{d(\text{HHI})}{dt}$).

---

## 4. Graph Ontology (Neo4j)

### Node Labels
- `:Repository`: Ingested software application.
- `:Package`: Open-source software library.
- `:API`: Third-party SaaS service endpoint.
- `:Cloud`: Cloud hyperscaler or hosting platform.
- `:AIModel`: Foundation model, embedding API, or vector database.
- `:Identity`: IAM or authentication service.
- `:Infrastructure`: Container image, Kubernetes cluster, or IaC resource.
- `:DataService`: Managed data warehouse, cache, or database.
- `:Maintainer`: Individual contributor or organization.

### Edge Types
- `(:Repository)-[:DEPENDS_ON {version, kind}]->(:Package)`
- `(:Repository|:Package)-[:CALLS]->(:API)`
- `(:Repository|:Infrastructure)-[:HOSTED_ON]->(:Cloud)`
- `(:Repository)-[:AUTHENTICATES_WITH]->(:Identity)`
- `(:Repository)-[:USES_MODEL]->(:AIModel)`
- `(:Repository)-[:STORES_DATA_IN]->(:DataService)`
- `(:Repository)-[:BUILT_WITH]->(:Infrastructure)`
- `(:Package)-[:MAINTAINED_BY]->(:Maintainer)`

---

## 5. Security & Isolation

- All API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `NEO4J_PASSWORD`) are configured via `.env` and loaded securely through `backend/app/config.py` and `ai-engine/models/model_config.py`.
- No raw secrets are output in logs (`backend/app/logging.py` sanitizes sensitive fields).
- External model API calls implement timeout and rate-limit backoffs.
