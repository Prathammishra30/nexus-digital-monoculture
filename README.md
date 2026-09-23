# NEXUS

## Digital Monoculture & Systemic Risk Observatory

NEXUS analyzes hidden dependency concentration across modern software ecosystems and identifies common points of failure across applications, packages, APIs, cloud providers, AI models, infrastructure, and maintainers.

### Core Question

> How independent is the digital ecosystem really?

### Core Pipeline

GitHub Repositories
→ Dependency Discovery
→ Transformation
→ Dependency Graph
→ Concentration Analysis
→ Failure Simulation
→ Risk Visualization

### Key Areas

- Dependency Concentration
- Common-Mode Failure
- Cloud & API Dependency
- AI Model Dependency
- Maintainer Concentration
- Temporal Risk / Monoculture Velocity
- Blast Radius Analysis

### Tech Stack

- Python
- FastAPI
- Neo4j
- React / Next.js
- Docker
- GitHub API

---

## The 9 Core Layers

1. **Application Layer**: User-facing services and analyzed GitHub codebases.
2. **Package Layer**: Direct and transitive open source packages (NPM, PyPI, Maven, Go).
3. **API Layer**: Third-party external SaaS APIs (Stripe, Twilio, SendGrid, Datadog).
4. **Cloud Layer**: Hyperscalers and hosting infrastructure (AWS, GCP, Azure, Cloudflare).
5. **AI Model Layer**: Foundation models, embedding providers, and vector databases (OpenAI, Anthropic, Hugging Face).
6. **Identity Layer**: Centralized authentication and IAM services (Auth0, Okta, Firebase Auth, Cognito).
7. **Infrastructure Layer**: Container base images and deployment orchestration (Docker, Kubernetes, Terraform).
8. **Data Layer**: Managed storage, cloud databases, and data warehouse platforms.
9. **Human / Maintainer Layer**: Critical open-source maintainers, committers, and bus-factor exposure.

---

## Directory Architecture

```
nexus-digital-monoculture/
│
├── backend/                  # FastAPI Application & Domain Services
│   ├── app/                  # Configuration, server setup, dependency injection
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   └── main.py
│   ├── api/                  # API routers and versioned endpoints
│   │   ├── routes/           # Domain-specific route controllers
│   │   │   ├── repositories.py
│   │   │   ├── dependencies.py
│   │   │   ├── risk.py
│   │   │   └── simulation.py
│   │   └── router.py
│   ├── models/               # Pydantic domain models across 9 layers
│   │   ├── repository.py
│   │   ├── dependency.py
│   │   ├── provider.py
│   │   ├── maintainer.py
│   │   └── risk.py
│   ├── services/             # Core business logic orchestrators
│   │   ├── repository_service.py
│   │   ├── dependency_service.py
│   │   ├── graph_service.py
│   │   └── risk_service.py
│   └── tests/                # Backend API smoke tests
│
├── discovery-engine/         # Discovery & Ingestion Engine
│   ├── github/               # GitHub API client & manifest fetcher
│   │   ├── client.py
│   │   └── repository_fetcher.py
│   ├── parsers/              # Multi-ecosystem manifest & lockfile parsers
│   │   ├── npm_parser.py
│   │   ├── python_parser.py
│   │   ├── java_parser.py
│   │   ├── go_parser.py
│   │   ├── docker_parser.py
│   │   └── terraform_parser.py
│   ├── transformers/         # Canonical entity normalizers
│   │   ├── dependency_transformer.py
│   │   ├── provider_transformer.py
│   │   └── maintainer_transformer.py
│   ├── detectors/            # Hidden external dependency detectors
│   │   ├── api_detector.py
│   │   ├── cloud_detector.py
│   │   ├── ai_model_detector.py
│   │   └── identity_detector.py
│   └── pipeline.py           # Discovery orchestration pipeline
│
├── risk-engine/              # Systemic Risk & Resilience Analytics
│   ├── concentration/        # Market & dependency concentration (HHI)
│   │   ├── hhi.py
│   │   └── monoculture_index.py
│   ├── maintainer/           # Human bus-factor & sustainment risk
│   │   └── maintainer_risk.py
│   ├── blast_radius/         # Reverse reachability & impact calculation
│   │   └── calculator.py
│   ├── simulation/           # Cascading failure simulator & diversification
│   │   ├── failure_simulator.py
│   │   └── diversification.py
│   ├── temporal/             # Rate of monoculture convergence over time
│   │   └── monoculture_velocity.py
│   └── risk_pipeline.py      # Risk assessment orchestration pipeline
│
├── graph/                    # Graph Persistence Layer (Neo4j)
│   └── neo4j/
│       ├── schema/           # Cypher constraints and performance indexes
│       │   ├── constraints.cypher
│       │   └── indexes.cypher
│       ├── queries/          # Reusable analytics Cypher queries
│       │   ├── dependencies.cypher
│       │   ├── common_roots.cypher
│       │   └── blast_radius.cypher
│       └── client.py         # Neo4j driver connection pool & query runner
│
├── frontend/                 # Observability Dashboard (React / Next.js)
│   ├── src/
│   │   ├── components/       # Graph visualizers, scorecards, metric cards
│   │   ├── pages/            # Views (Ecosystem, Repo Detail, Simulation)
│   │   ├── services/         # API client bindings to backend
│   │   ├── hooks/            # Custom state and query hooks
│   │   ├── types/            # TypeScript schemas mirroring backend models
│   │   └── utils/            # Graph rendering and math utilities
│   ├── public/               # Static assets and icons
│   └── README.md
│
├── datasets/                 # Repository dumps, processed graphs & sample manifests
│   ├── raw/
│   ├── processed/
│   └── samples/
│
├── docs/                     # Documentation
│   ├── architecture/         # Layer architecture & design specifications
│   ├── research/             # Mathematical formulations (HHI, Entropy, Velocity)
│   └── api/                  # REST API endpoint reference
│
├── tests/                    # Global Test Suites
│   ├── unit/                 # Unit tests for parsers & risk algorithms
│   ├── integration/          # Multi-module pipeline tests
│   └── fixtures/             # Reusable manifest fixtures
│
├── scripts/                  # Operations & Maintenance Scripts
│   ├── setup/                # Database initialization (Neo4j schema)
│   └── data/                 # Sample graph data seeder
│
├── .env.example              # Environment variables template
├── docker-compose.yml        # Orchestration for Backend, Neo4j, and Frontend
├── requirements.txt          # Python runtime dependencies
└── pyproject.toml            # Python packaging and tool configuration
```

---

## Module Ownership & Developer Division of Labor

The project is structured into clear, independently assignable ownership areas:

| Module Area | Directory Path | Core Focus & Responsibilities | Key Files Ready to Own |
| :--- | :--- | :--- | :--- |
| **Backend & API** | `backend/` | REST API routes, Pydantic schemas, dependency injection, and service orchestrators. | `backend/app/main.py`, `backend/api/routes/*.py`, `backend/services/*.py` |
| **Discovery Engine** | `discovery-engine/` | GitHub manifest retrieval, multi-language package parsing, provider & identity detection. | `discovery-engine/parsers/*.py`, `discovery-engine/detectors/*.py`, `discovery-engine/pipeline.py` |
| **Risk Engine** | `risk-engine/` | Quantitative models: HHI, monoculture index, blast radius, maintainer bus factor, and failure simulation. | `risk-engine/concentration/*.py`, `risk-engine/blast_radius/calculator.py`, `risk-engine/simulation/*.py` |
| **Graph Database** | `graph/` | Neo4j client connection management, schema constraints, performance indexes, and analytical Cypher queries. | `graph/neo4j/client.py`, `graph/neo4j/schema/*.cypher`, `graph/neo4j/queries/*.cypher` |
| **Frontend Dashboard** | `frontend/` | Next.js / React dashboard, interactive dependency graphs, risk scorecards, and simulation controls. | `frontend/src/services/api.ts`, `frontend/src/types/index.ts`, `frontend/src/pages/` |
| **Data & Operations** | `datasets/`, `scripts/` | Benchmark manifests, test fixtures, database initialization scripts, and data seeders. | `scripts/setup/init_neo4j.py`, `scripts/data/seed_sample_data.py` |

---

## Quickstart & Local Setup

### 1. Environment Configuration

```bash
cp .env.example .env
```

### 2. Python Virtual Environment

```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 3. Running Backend Locally

```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```
Interactive API documentation will be accessible at `http://localhost:8000/docs`.

### 4. Running via Docker Compose

```bash
docker compose up -d neo4j
python scripts/setup/init_neo4j.py
docker compose up --build
```

