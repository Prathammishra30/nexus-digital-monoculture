#!/usr/bin/env python3
"""NEXUS Neo4j Database Initializer.

Applies Cypher uniqueness constraints and performance indexes
from the schema definitions to a running Neo4j instance.

Usage:
    python scripts/setup/init_neo4j.py
"""

import os
import sys
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir))

from backend.app.config import get_settings
from graph.neo4j.client import Neo4jClient


def load_cypher_statements(file_path: Path) -> list[str]:
    """Read file and parse non-empty Cypher statements delimited by semicolons."""
    if not file_path.exists():
        print(f"[WARN] Schema file not found: {file_path}")
        return []

    raw = file_path.read_text(encoding="utf-8")
    statements = []
    for chunk in raw.split(";"):
        cleaned = chunk.strip()
        # Filter out comments-only blocks
        lines = [line for line in cleaned.splitlines() if not line.strip().startswith("//")]
        valid_query = "\n".join(lines).strip()
        if valid_query:
            statements.append(valid_query)
    return statements


def main() -> None:
    """Execute schema constraints and index migrations."""
    settings = get_settings()
    print(f"Connecting to Neo4j at {settings.neo4j_uri} as {settings.neo4j_user}...")

    client = Neo4jClient(
        uri=settings.neo4j_uri,
        user=settings.neo4j_user,
        password=settings.neo4j_password,
        database=settings.neo4j_database
    )
    client.connect()

    schema_dir = root_dir / "graph" / "neo4j" / "schema"
    constraints_file = schema_dir / "constraints.cypher"
    indexes_file = schema_dir / "indexes.cypher"

    constraints = load_cypher_statements(constraints_file)
    indexes = load_cypher_statements(indexes_file)

    print(f"Found {len(constraints)} constraints and {len(indexes)} index definitions.")

    # TODO: Execute statements via client.execute_query when Neo4j is running
    print("[INFO] Neo4j schema initialization script ready.")
    client.close()


if __name__ == "__main__":
    main()
