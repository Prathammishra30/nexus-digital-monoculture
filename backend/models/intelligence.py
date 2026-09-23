"""NEXUS Intelligence Domain Models.

Defines schemas for AI-assisted semantic extraction, confidence evaluation,
grounding evidence, and task routing requests.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from backend.models.dependency import LayerType


class ConfidenceStatus(str, Enum):
    """Categorical confidence classification for AI-derived observations.

    These are data-confidence classifications, NOT risk rankings.
    """
    CONFIRMED = "CONFIRMED"    # Confidence >= 0.85 with verified code/config evidence
    PROBABLE = "PROBABLE"      # Confidence 0.70 - 0.84 with strong heuristic signals
    UNCERTAIN = "UNCERTAIN"    # Confidence 0.50 - 0.69 requiring human confirmation
    REJECTED = "REJECTED"      # Confidence < 0.50 or conflicting deterministic evidence


class EvidenceItem(BaseModel):
    """Grounding proof tying an AI inference to concrete repository tokens or files."""
    file_path: str = Field(..., description="Relative file path where signal was detected")
    line_number: Optional[int] = Field(default=None, description="Line number in source file")
    matched_token: str = Field(..., description="Exact string, import statement, or configuration key")
    context_snippet: Optional[str] = Field(default=None, description="Surrounding code context")


class InferredEntity(BaseModel):
    """An implicit or explicit dependency entity derived via semantic transformation."""
    id: str = Field(..., description="Canonical entity ID (e.g. 'provider:aws' or 'api:stripe')")
    name: str = Field(..., description="Canonical entity name")
    layer: LayerType = Field(..., description="Target architectural layer")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Quantitative confidence [0.0 - 1.0]")
    confidence_status: ConfidenceStatus = Field(..., description="Qualitative confidence rating")
    evidence: List[EvidenceItem] = Field(default_factory=list, description="Grounding evidence references")
    reasoning: Optional[str] = Field(default=None, description="Model explanation / chain of reasoning")
    extracted_by: str = Field(default="deterministic", description="Extraction method or model ID")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TransformationRequest(BaseModel):
    """Payload to trigger semantic transformation on raw repository artifacts."""
    repository_id: str
    manifest_paths: List[str] = Field(default_factory=list)
    include_source_inspection: bool = Field(default=False)
    min_confidence_threshold: float = Field(default=0.70, ge=0.0, le=1.0)
    preferred_model_provider: Optional[str] = Field(default=None, description="e.g. 'openai', 'anthropic', 'local'")


class TransformationResponse(BaseModel):
    """Result of semantic interpretation, showing newly discovered implicit entities."""
    repository_id: str
    inferred_entities: List[InferredEntity] = Field(default_factory=list)
    total_discovered: int = Field(default=0)
    confirmed_count: int = Field(default=0)
    probable_count: int = Field(default=0)
    uncertain_count: int = Field(default=0)
    rejected_count: int = Field(default=0)
    model_used: str = Field(default="heuristic")
    execution_time_ms: float = Field(default=0.0)


class IntelligenceSummary(BaseModel):
    """Observatory-wide intelligence and hallucination control metrics."""
    total_inferences: int = Field(default=0)
    confidence_breakdown: Dict[ConfidenceStatus, int] = Field(default_factory=dict)
    average_confidence: float = Field(default=0.0)
    active_model_providers: List[str] = Field(default_factory=list)
