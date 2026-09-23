"""Basic API Smoke Tests.

Validates application startup, health endpoints, and router registration.
"""

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Verify observatory root endpoint returns 200 and operational status."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "version" in data


def test_health_check():
    """Verify health probe returns status healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_list_repositories_skeleton():
    """Verify repositories endpoint returns empty list placeholder."""
    response = client.get("/api/v1/repositories")
    assert response.status_code == 200
    assert response.json() == []


def test_ecosystem_risk_summary_skeleton():
    """Verify risk endpoint returns base structure."""
    response = client.get("/api/v1/risk/ecosystem")
    assert response.status_code == 200
    data = response.json()
    assert data["overall_risk_score"] == 0.0
