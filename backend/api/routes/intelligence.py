"""AI intelligence API contracts and confidence observability."""

from fastapi import APIRouter

from backend.models.intelligence import (
    IntelligenceSummary,
    TransformationRequest,
    TransformationResponse,
)
from backend.services.intelligence_service import IntelligenceService

router = APIRouter(prefix="/intelligence", tags=["AI Intelligence"])
_service = IntelligenceService()


@router.post("/transform", response_model=TransformationResponse, status_code=202)
async def transform_repository(request: TransformationRequest) -> TransformationResponse:
    """Queue a provider-neutral semantic transformation for a repository."""
    return await _service.transform(request)


@router.get("/summary", response_model=IntelligenceSummary)
async def get_intelligence_summary() -> IntelligenceSummary:
    """Return confidence and provider metrics for the observatory."""
    return await _service.summary()
