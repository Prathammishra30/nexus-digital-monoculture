"""NEXUS Provider Domain Models.

Defines schemas for upstream infrastructure, cloud, API, and AI model providers
that introduce systemic common-mode failure risks.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ProviderType(str, Enum):
    """Classification of external platform providers."""
    CLOUD = "cloud"              # e.g., AWS, GCP, Azure
    AI = "ai_foundation"        # e.g., OpenAI, Anthropic, Cohere
    IDENTITY = "identity"        # e.g., Auth0, Okta, Firebase Auth
    API = "saas_api"            # e.g., Stripe, Twilio, Sendgrid
    CDN = "cdn_network"         # e.g., Cloudflare, Fastly, Akamai
    DATABASE = "managed_data"   # e.g., Snowflake, Pinecone, MongoDB Atlas


class ProviderNode(BaseModel):
    """Graph representation of an external service/infrastructure provider."""
    id: str = Field(..., description="Unique provider ID, e.g., 'provider:aws'")
    name: str = Field(..., description="Human-readable provider name, e.g., 'Amazon Web Services'")
    provider_type: ProviderType = Field(..., description="Category of provider")
    market_share_estimate: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Global market share indicator for concentration models"
    )
    regions_detected: List[str] = Field(default_factory=list, description="Target regions configured")
    is_monopolistic: bool = Field(default=False, description="Flagged if provider exceeds HHI concentration threshold")
    metadata: Dict[str, Any] = Field(default_factory=dict)

    # TODO: Add dynamic outage and incident status tracking fields
