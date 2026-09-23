#!/usr/bin/env python3
"""NEXUS Sample Data Seeder.

Populates a local Neo4j database with a small representative multi-layer
software graph (repositories, packages, cloud providers, APIs, AI models,
and maintainers) for development and frontend testing.

Usage:
    python scripts/data/seed_sample_data.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir))

from backend.app.config import get_settings
from graph.neo4j.client import Neo4jClient


def main() -> None:
    """Seed sample graph data."""
    settings = get_settings()
    print(f"[INFO] Seeding sample data to {settings.neo4j_uri}...")

    # TODO: Execute sample graph seed Cypher statements:
    # 1. Create Repository: (:Repository {id: 'repo:example_app', name: 'example/app'})
    # 2. Create Package: (:Package {id: 'pkg:npm:express', name: 'express', ecosystem: 'npm'})
    # 3. Create Cloud: (:Cloud {id: 'provider:aws', name: 'AWS'})
    # 4. Create API: (:API {id: 'api:stripe', name: 'Stripe'})
    # 5. Create AIModel: (:AIModel {id: 'ai:openai:gpt-4o', name: 'OpenAI GPT-4o'})
    # 6. Create Maintainer: (:Maintainer {id: 'user:dougwilson', login: 'dougwilson'})
    # 7. Create DEPENDS_ON, RELIES_ON_PROVIDER, and MAINTAINED_BY edges

    print("[INFO] Sample seeder script skeleton ready.")


if __name__ == "__main__":
    main()
