"""NEXUS Repository API Routes.

Handles registration, scanning triggers, and metadata queries for tracked software repositories.
"""

from typing import List
from fastapi import APIRouter, HTTPException, Query, status
from backend.models.repository import RepositoryCreate, RepositoryResponse

router = APIRouter(prefix="/repositories", tags=["Repositories"])


@router.post(
    "/analyze",
    response_model=RepositoryResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Enqueue repository for discovery & dependency scanning"
)
async def analyze_repository(payload: RepositoryCreate) -> RepositoryResponse:
    """Trigger the discovery pipeline for a remote git repository.

    - **name**: GitHub repo name (e.g. 'facebook/react')
    - **url**: Clone or API URL
    - **depth**: Transitive scanning depth
    """
    # TODO: Connect to backend.services.repository_service.RepositoryService.register_and_scan
    repo_id = f"repo:{payload.name.replace('/', '_')}"
    return RepositoryResponse(
        id=repo_id,
        name=payload.name,
        url=payload.url,
        description=payload.description,
        primary_language=payload.primary_language,
        ecosystem=payload.ecosystem,
        dependency_count=0,
        systemic_risk_score=None
    )


@router.get(
    "",
    response_model=List[RepositoryResponse],
    summary="List all tracked repositories"
)
async def list_repositories(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100)
) -> List[RepositoryResponse]:
    """Retrieve paginated list of all repositories indexed in the observatory."""
    # TODO: Connect to repository_service.list_repositories
    return []


@router.get(
    "/{repo_id}",
    response_model=RepositoryResponse,
    summary="Get repository profile by ID"
)
async def get_repository(repo_id: str) -> RepositoryResponse:
    """Retrieve detailed scan results, risk score, and metadata for a repository."""
    # TODO: Connect to repository_service.get_repository_by_id
    raise HTTPException(status_code=404, detail=f"Repository '{repo_id}' not found")
