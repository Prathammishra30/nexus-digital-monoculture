"""NEXUS Simulation API Routes.

Provides what-if failure scenario simulations, blast radius estimations,
and structural diversification recommendations.
"""

from fastapi import APIRouter, HTTPException, Query, status
from backend.models.risk import (
    SimulationRequest,
    SimulationResult,
    BlastRadiusResult,
    RiskLevel
)
from backend.models.dependency import LayerType

router = APIRouter(prefix="/simulation", tags=["Simulation & Blast Radius"])


@router.post(
    "/simulate-failure",
    response_model=SimulationResult,
    summary="Simulate cascading failure from one or more node outages"
)
async def simulate_failure(payload: SimulationRequest) -> SimulationResult:
    """Simulate what-if catastrophic failure or supply chain compromise of target dependencies or providers."""
    # TODO: Connect to backend.services.risk_service.RiskService.run_failure_simulation
    return SimulationResult(
        simulation_id="sim_preview",
        nodes_disabled=payload.target_node_ids,
        total_ecosystem_disruption_percentage=0.0,
        cascading_failures=[],
        recommended_diversifications=[]
    )


@router.get(
    "/blast-radius/{node_id}",
    response_model=BlastRadiusResult,
    summary="Calculate blast radius for a given dependency or provider"
)
async def get_blast_radius(node_id: str) -> BlastRadiusResult:
    """Measure the downstream dependency reachability and affected repository count if node fails."""
    # TODO: Connect to risk_service.calculate_node_blast_radius
    return BlastRadiusResult(
        target_node_id=node_id,
        target_node_name=node_id,
        target_layer=LayerType.PACKAGE,
        directly_affected_repositories=0,
        transitive_affected_repositories=0,
        total_impacted_services=0,
        critical_path_vulnerability=False,
        affected_repo_ids=[]
    )


@router.post(
    "/diversify",
    summary="Generate diversification proposals to reduce systemic risk"
)
async def recommend_diversification(
    repo_id: str = Query(..., description="Target repository ID to optimize")
):
    """Suggest alternative providers or packages to reduce single-point-of-failure concentration."""
    # TODO: Connect to risk-engine/simulation/diversification.py
    return {
        "repository_id": repo_id,
        "recommendations": []
    }
