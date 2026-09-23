"""NEXUS Repository Domain Models.

Defines schemas for ingested software repositories, their metadata,
and discovery state within the observatory.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, HttpUrl


class EcosystemType(str, Enum):
    """Supported package management ecosystems."""
    NPM = "npm"
    PYPI = "pypi"
    MAVEN = "maven"
    GOLANG = "golang"
    DOCKER = "docker"
    TERRAFORM = "terraform"
    MULTI = "multi"
    UNKNOWN = "unknown"


class RepositoryBase(BaseModel):
    """Base representation of a software repository."""
    name: str = Field(..., description="Repository full name, e.g., 'owner/repo'")
    url: str = Field(..., description="Remote git repository URL")
    description: Optional[str] = Field(default=None, description="Repository description")
    primary_language: Optional[str] = Field(default=None, description="Primary detected programming language")
    ecosystem: EcosystemType = Field(default=EcosystemType.UNKNOWN, description="Primary packaging ecosystem")


class RepositoryCreate(RepositoryBase):
    """Payload to trigger analysis on a new repository."""
    branch: Optional[str] = Field(default="main", description="Target branch to scan")
    depth: int = Field(default=2, ge=1, le=10, description="Transitive dependency scanning depth")


class RepositoryMetadata(BaseModel):
    """Supplementary GitHub metadata for risk weighting."""
    stars: int = Field(default=0)
    forks: int = Field(default=0)
    open_issues: int = Field(default=0)
    watchers: int = Field(default=0)
    is_fork: bool = Field(default=False)
    created_at: Optional[datetime] = None
    last_pushed_at: Optional[datetime] = None


class RepositoryResponse(RepositoryBase):
    """API response model for an analyzed repository."""
    id: str = Field(..., description="Internal unique entity ID")
    scanned_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    dependency_count: int = Field(default=0, description="Total direct + transitive dependencies detected")
    systemic_risk_score: Optional[float] = Field(default=None, ge=0.0, le=100.0, description="Composite risk index")
    metadata: Optional[RepositoryMetadata] = None

    # TODO: Add relationship summaries (direct providers, high-risk maintainers)
