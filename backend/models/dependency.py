"""NEXUS Dependency Domain Models.

Defines schemas for dependency nodes, edge classifications, and layer categorization
across the 9 NEXUS architectural layers.
"""

from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class LayerType(str, Enum):
    """The 9 NEXUS observatory classification layers."""
    APPLICATION = "application"
    PACKAGE = "package"
    API = "api"
    CLOUD = "cloud"
    AI_MODEL = "ai_model"
    IDENTITY = "identity"
    INFRASTRUCTURE = "infrastructure"
    DATA = "data"
    MAINTAINER = "maintainer"


class DependencyType(str, Enum):
    """Relationship nature between consumer and dependency."""
    DIRECT = "direct"
    TRANSITIVE = "transitive"
    PEER = "peer"
    DEV = "dev"
    RUNTIME = "runtime"
    INFRASTRUCTURE = "infrastructure"


class DependencyBase(BaseModel):
    """Basic specification of an external dependency."""
    name: str = Field(..., description="Canonical name of package, service, or resource")
    version_spec: Optional[str] = Field(default=None, description="Declared version requirement or constraint")
    layer: LayerType = Field(default=LayerType.PACKAGE, description="Architectural layer classification")


class DependencyNode(DependencyBase):
    """Graph node representation of a discovered dependency."""
    id: str = Field(..., description="Unique graph node identifier (e.g. 'npm:lodash')")
    resolved_version: Optional[str] = Field(default=None, description="Exact locked version if discovered")
    ecosystem: Optional[str] = Field(default=None, description="Source ecosystem, e.g. npm, pypi")
    license: Optional[str] = Field(default=None, description="SPDX identifier if available")
    is_critical_path: bool = Field(default=False, description="Flag for single-point-of-failure path")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Arbitrary vendor/package metadata")

    # TODO: Add methods for calculating individual node centrality and degree
