"""Canonical, provider-neutral NEXUS data contracts.

These models are the boundary between deterministic discovery, AI transformation,
graph persistence, risk analytics, the API, and the frontend. They describe
observations; they do not assert that a confidence state is a risk ranking.
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class EntityLayer(str, Enum):
    APPLICATION = "application"
    PACKAGE = "package"
    API = "api"
    CLOUD = "cloud"
    AI_MODEL = "ai_model"
    IDENTITY = "identity"
    INFRASTRUCTURE = "infrastructure"
    DATA = "data"
    MAINTAINER = "maintainer"


class ConfidenceStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    PROBABLE = "PROBABLE"
    UNCERTAIN = "UNCERTAIN"
    REJECTED = "REJECTED"


class Evidence(BaseModel):
    """A source reference that grounds an observation."""

    source: str = Field(..., description="Repository, API, or dataset source")
    artifact: str = Field(..., description="Relative path, URL, or artifact identifier")
    excerpt: Optional[str] = None
    line_start: Optional[int] = Field(default=None, ge=1)
    line_end: Optional[int] = Field(default=None, ge=1)
    extraction_method: str = "deterministic"


class CanonicalEntity(BaseModel):
    """A validated observation that is safe to persist in the graph."""

    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    entity_type: str = Field(..., min_length=1)
    layer: EntityLayer
    source: str = Field(..., min_length=1)
    evidence: List[Evidence] = Field(default_factory=list)
    confidence: float = Field(..., ge=0.0, le=1.0)
    confidence_status: ConfidenceStatus
    reasoning_metadata: Dict[str, Any] = Field(default_factory=dict)
    observed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    extraction_method: str = "deterministic"

    @field_validator("observed_at")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None:
            raise ValueError("observed_at must include timezone information")
        return value


class GraphRelationship(BaseModel):
    """A typed edge between two canonical entities."""

    source_id: str = Field(..., min_length=1)
    relationship_type: str = Field(..., min_length=1)
    target_id: str = Field(..., min_length=1)
    evidence: List[Evidence] = Field(default_factory=list)
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    properties: Dict[str, Any] = Field(default_factory=dict)


class SnapshotMetadata(BaseModel):
    """Time-indexed metadata shared by repository, dependency, provider, maintainer, and risk snapshots."""

    snapshot_id: str = Field(..., min_length=1)
    subject_id: str = Field(..., min_length=1)
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    schema_version: str = "1.0"
    source: str = "nexus"
