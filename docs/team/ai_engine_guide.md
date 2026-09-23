# AI Engine Guide

**What:** provider-neutral semantic interpretation for facts deterministic parsers cannot establish.

**Input:** raw artifacts plus evidence and a task category. **Output:** schema-validated canonical observations with evidence, confidence, status, timestamp, and extraction method.

Own `ai_engine/` runtime interfaces and the `ai-engine/` ownership tree. Do not place API handlers, Neo4j queries, or risk thresholds here. Test with local doubles; provider credentials are optional and environment-only.

Run `python -m pytest ai-engine/tests tests/contract -q` and `python -m compileall -q ai_engine`.
