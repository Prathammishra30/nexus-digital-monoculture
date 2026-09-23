# Graph Engine Guide

**What:** Neo4j connection, schema, indexes, and canonical relationship persistence.

**Input:** `CanonicalEntity` and `GraphRelationship`. **Output:** persisted nodes/edges or explicit adapter errors. The graph layer does not invent entities.

Own `graph/` and Cypher schema files. Do not place risk formulas or API response formatting here. Validate Cypher with Neo4j during integration testing when available; run graph unit tests without a live database using a fake client.
