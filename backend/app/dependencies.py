"""NEXUS FastAPI Dependencies.

Provides shared dependency injection providers for database connections,
service layer instances, and request contexts.
"""

from typing import Generator
from fastapi import Depends
from backend.app.config import Settings, get_settings


def get_app_settings() -> Settings:
    """Inject application settings into route handlers."""
    return get_settings()


# TODO: Implement connection pool management for Neo4j driver
def get_graph_client(settings: Settings = Depends(get_app_settings)):
    """Provide a verified Neo4j driver session/client instance."""
    # TODO: Connect using graph.neo4j.client.Neo4jClient
    yield None


# TODO: Implement dependency injections for service classes once service layer is integrated
def get_repository_service():
    """Dependency provider for RepositoryService."""
    # TODO: Return instantiated RepositoryService(graph_client=...)
    pass


def get_dependency_service():
    """Dependency provider for DependencyService."""
    # TODO: Return instantiated DependencyService(graph_client=...)
    pass


def get_risk_service():
    """Dependency provider for RiskService."""
    # TODO: Return instantiated RiskService(graph_client=...)
    pass
