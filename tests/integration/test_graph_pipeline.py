"""Integration Tests Placeholder for Graph and Risk Pipeline.

Validates integrated pipeline interactions without requiring a live Neo4j instance.
"""

import sys
from pathlib import Path
import pytest

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir / "discovery-engine"))
sys.path.insert(0, str(root_dir / "risk-engine"))
sys.path.insert(0, str(root_dir / "graph"))
sys.path.insert(0, str(root_dir))

from pipeline import DiscoveryPipeline
from risk_pipeline import RiskPipeline


@pytest.mark.asyncio
async def test_discovery_pipeline_initialization():
    """Verify discovery pipeline initializes and runs stub workflow."""
    pipeline = DiscoveryPipeline()
    report = await pipeline.run(repo_url="https://github.com/example/repo", branch="main")
    assert report["status"] == "completed"
    assert report["manifests_parsed"] == 0


@pytest.mark.asyncio
async def test_risk_pipeline_initialization():
    """Verify risk pipeline initializes and executes baseline evaluation."""
    pipeline = RiskPipeline()
    report = await pipeline.execute_full_risk_assessment()
    assert report["status"] == "completed"
    assert report["layers_evaluated"] == 9
