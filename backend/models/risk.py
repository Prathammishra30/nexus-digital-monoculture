"""NEXUS Risk Domain Models.

Defines schemas for systemic risk analytics, HHI concentration indexes,
blast radius calculations, and cascading failure simulations.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from backend.models.dependency import LayerType


class RiskLevel(str, Enum):
    """Normalized categorical risk tier."""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class ConcentrationMetric(BaseModel):
    """Concentration assessment for a specific architectural layer."""
    layer: LayerType
    hhi_score: float = Field(..., ge=0.0, le=10000.0, description="Herfindahl-Hirschman Index (0-10000)")
    monoculture_index: float = Field(..., ge=0.0, le=1.0, description="Normalized monoculture index (0-1)")
    risk_level: RiskLevel
    top_dominant_entity: str = Field(..., description="Entity with highest market/dependency share")
    top_entity_share_percentage: float = Field(..., ge=0.0, le=100.0)


class BlastRadiusResult(BaseModel):
    """Downstream impact estimation if a specific node fails."""
    target_node_id: str
    target_node_name: str
    target_layer: LayerType
    directly_affected_repositories: int = Field(default=0)
    transitive_affected_repositories: int = Field(default=0)
    total_impacted_services: int = Field(default=0)
    critical_path_vulnerability: bool = Field(default=False)
    affected_repo_ids: List[str] = Field(default_factory=list)


class RiskScoreSummary(BaseModel):
    """Aggregate risk scorecard for a repository or entire observatory ecosystem."""
    overall_risk_score: float = Field(..., ge=0.0, le=100.0)
    risk_level: RiskLevel
    concentration_breakdown: List[ConcentrationMetric] = Field(default_factory=list)
    top_vulnerable_dependencies: List[str] = Field(default_factory=list)
    single_points_of_failure_count: int = Field(default=0)


class SimulationRequest(BaseModel):
    """Payload to initiate a what-if failure simulation."""
    target_node_ids: List[str] = Field(..., description="Node IDs to simulate outage/compromise for")
    include_transitive: bool = Field(default=True)
    depth_limit: int = Field(default=5)


class SimulationResult(BaseModel):
    """Results of a what-if failure propagation simulation."""
    simulation_id: str
    nodes_disabled: List[str]
    total_ecosystem_disruption_percentage: float = Field(..., ge=0.0, le=100.0)
    cascading_failures: List[Dict[str, Any]] = Field(default_factory=list)
    recommended_diversifications: List[str] = Field(default_factory=list)

    # TODO: Add temporal propagation velocity metrics
