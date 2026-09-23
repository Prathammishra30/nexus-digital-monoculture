"""NEXUS Risk API Routes.

Exposes systemic risk scores, Herfindahl-Hirschman Index (HHI) concentration metrics,
monoculture ratings, and single-points-of-failure analytics.
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from backend.models.risk import RiskScoreSummary, ConcentrationMetric, RiskLevel
from backend.models.dependency import LayerType

router = APIRouter(prefix="/risk", tags=["Risk & Concentration"])


@router.get(
    "/ecosystem",
    response_model=RiskScoreSummary,
    summary="Get macroscopic ecosystem risk scorecard"
)
async def get_ecosystem_risk() -> RiskScoreSummary:
    """Retrieve global concentration and systemic fragility indices across all monitored software."""
    # TODO: Connect to backend.services.risk_service.RiskService.get_ecosystem_risk_summary
    return RiskScoreSummary(
        overall_risk_score=0.0,
        risk_level=RiskLevel.LOW,
        concentration_breakdown=[],
        top_vulnerable_dependencies=[],
        single_points_of_failure_count=0
    )


@router.get(
    "/concentration",
    response_model=ConcentrationMetric,
    summary="Get concentration and HHI metrics for a specific layer"
)
async def get_layer_concentration(
    layer: LayerType = Query(..., description="Target architectural layer to analyze")
) -> ConcentrationMetric:
    """Retrieve market and dependency concentration metrics (HHI & Monoculture Index) for a layer."""
    # TODO: Connect to risk_service.get_layer_concentration
    return ConcentrationMetric(
        layer=layer,
        hhi_score=0.0,
        monoculture_index=0.0,
        risk_level=RiskLevel.LOW,
        top_dominant_entity="none",
        top_entity_share_percentage=0.0
    )


@router.get(
    "/repository/{repo_id}",
    response_model=RiskScoreSummary,
    summary="Get risk scorecard for a single repository"
)
async def get_repository_risk(repo_id: str) -> RiskScoreSummary:
    """Evaluate specific dependency risks, maintainer bus factor, and blast radius for a given repo."""
    # TODO: Connect to risk_service for repository-specific risk aggregation
    raise HTTPException(status_code=404, detail=f"Risk profile for repository '{repo_id}' not found")
