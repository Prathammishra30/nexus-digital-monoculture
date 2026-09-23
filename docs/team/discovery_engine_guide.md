# Discovery Engine Guide

**What:** GitHub ingestion and deterministic parsing of manifests, infrastructure, APIs, identity, cloud, and model signals.

**Input:** repository URL/ref and fetched artifacts. **Output:** raw dependency representations and evidence references. AI interpretation is downstream.

Own `discovery-engine/`; do not write graph persistence or frontend code. Add parser fixtures under `tests/fixtures/` and unit tests under `tests/unit/`.

Run `python -m compileall -q discovery-engine` and the focused parser tests.
