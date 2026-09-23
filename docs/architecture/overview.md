# NEXUS Architecture Overview

The **NEXUS Digital Monoculture & Systemic Risk Observatory** models the modern software supply chain as a heterogeneous graph spanning nine interdependent layers.

## The 9 Core Layers

1. **Application**: The consumer codebase or user-facing service (e.g. GitHub repos).
2. **Package**: Direct and transitive open source packages (NPM, PyPI, Maven, Go modules).
3. **API**: Third-party SaaS services integrated via client SDKs or HTTP (Stripe, Twilio, SendGrid).
4. **Cloud**: Hyperscaler infrastructure and region-level hosting (AWS, GCP, Azure, Cloudflare).
5. **AI Model**: Centralized foundation models, embeddings, and vector databases (OpenAI, Anthropic, HuggingFace).
6. **Identity**: Authentication and authorization providers (Auth0, Okta, Firebase Auth, Cognito).
7. **Infrastructure**: Container base images and deployment orchestration (Docker, Kubernetes, Terraform).
8. **Data**: Upstream managed databases, warehouses, and storage services.
9. **Human/Maintainer**: Individual committers and maintainers creating bus-factor vulnerabilities.

## Core Pipeline Workflow

```
GitHub Repository
   │
   ▼
Discovery Engine (Fetch manifests & configs)
   │
   ▼
Parsers (NPM, Python, Java, Go, Docker, Terraform)
   │
   ▼
Detectors (Cloud, API, AI Model, Identity)
   │
   ▼
Transformers (Canonical Nodes & Relationships)
   │
   ▼
Neo4j Graph Database
   │
   ▼
Risk Engine (HHI, Monoculture Index, Blast Radius, Cascading Simulations)
   │
   ▼
FastAPI Backend (/api/v1)
   │
   ▼
Frontend Observability Dashboard
```
