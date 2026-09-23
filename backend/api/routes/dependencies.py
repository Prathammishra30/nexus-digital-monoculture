"""NEXUS Dependency API Routes.

Exposes dependency graph inspection, cross-layer dependency search,
and upstream dependent lookups.
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.models.dependency import DependencyNode, LayerType

router = APIRouter(prefix="/dependencies", tags=["Dependencies"])


@router.get(
    "",
    response_model=List[DependencyNode],
    summary="Search dependencies across the 9 observatory layers"
)
async def list_dependencies(
    layer: Optional[LayerType] = Query(default=None, description="Filter by architectural layer"),
    query: Optional[str] = Query(default=None, description="Search term for dependency name"),
    limit: int = Query(default=50, ge=1, le=200)
) -> List[DependencyNode]:
    """Search for packages, APIs, cloud resources, and maintainers in the observatory graph."""
    # TODO: Connect to backend.services.dependency_service.DependencyService
    return []


@router.get(
    "/{dep_id}",
    response_model=DependencyNode,
    summary="Get details for a specific dependency node"
)
async def get_dependency(dep_id: str) -> DependencyNode:
    """Retrieve full dependency attributes, layer categorization, and license information."""
    # TODO: Connect to dependency_service.get_dependency_details
    raise HTTPException(status_code=404, detail=f"Dependency node '{dep_id}' not found")


@router.get(
    "/{dep_id}/dependents",
    response_model=List[str],
    summary="Get all upstream repositories depending on this node"
)
async def get_dependents(
    dep_id: str,
    limit: int = Query(default=100, ge=1, le=500)
) -> List[str]:
    """Find all repositories directly or transitively reliant on this package/provider."""
    # TODO: Connect to dependency_service.find_dependents
    return []
