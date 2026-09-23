"""Configuration values for model routing; credentials stay in environment variables."""

from pydantic import BaseModel, Field


class ModelConfig(BaseModel):
    provider: str = "local"
    model_name: str = "local-default"
    timeout_seconds: float = Field(default=30.0, gt=0)
    max_retries: int = Field(default=2, ge=0, le=5)
    confidence_threshold: float = Field(default=0.75, ge=0.0, le=1.0)
