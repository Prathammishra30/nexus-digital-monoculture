"""NEXUS Neo4j Package.

Manages connection pooling, transactions, schema migrations, and Cypher executions.
"""

from .client import Neo4jClient

__all__ = ["Neo4jClient"]
