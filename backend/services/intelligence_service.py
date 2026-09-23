"""Application service boundary for AI-assisted transformations."""

from backend.models.intelligence import (
    IntelligenceSummary,
    TransformationRequest,
    TransformationResponse,
)


class IntelligenceService:
    """Coordinates AI adapters; it does not contain provider-specific logic."""

    async def transform(self, request: TransformationRequest) -> TransformationResponse:
        return TransformationResponse(repository_id=request.repository_id)

    async def summary(self) -> IntelligenceSummary:
        return IntelligenceSummary()
