"""NEXUS Maintainer Domain Models.

Defines schemas for open-source maintainers, committers, and organizations
representing human concentration and bus-factor vulnerabilities.
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class MaintainerRiskProfile(BaseModel):
    """Evaluation of maintainer bus factor and sustainment risk."""
    bus_factor: int = Field(default=1, description="Number of maintainers responsible for >=80% of commits")
    is_single_maintainer: bool = Field(default=True, description="Indicates single point of human failure")
    active_maintainer_count: int = Field(default=1)
    last_commit_days_ago: Optional[int] = Field(default=None, description="Recency of maintainer activity")
    burnout_risk_score: Optional[float] = Field(default=None, ge=0.0, le=100.0, description="Risk indicator of maintainer abandonware")


class MaintainerNode(BaseModel):
    """Graph representation of an individual or organization maintainer."""
    id: str = Field(..., description="Unique maintainer ID (e.g. 'github:maintainer_login')")
    login: str = Field(..., description="VCS handle or organization name")
    is_organization: bool = Field(default=False)
    email: Optional[str] = Field(default=None)
    packages_maintained: List[str] = Field(default_factory=list, description="IDs of critical packages maintained")
    risk_profile: Optional[MaintainerRiskProfile] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    # TODO: Add corporate affiliation detection (e.g. Google, Meta, Microsoft maintainer affiliation)
