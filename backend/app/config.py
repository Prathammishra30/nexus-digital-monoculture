"""NEXUS Backend Configuration Module.

Defines application runtime settings, database connection parameters,
GitHub API configurations, and security policies using Pydantic Settings
with graceful fallback to environment variables.
"""

import os
from functools import lru_cache
from typing import List
from pydantic import Field

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class Settings(BaseSettings):
        """Application settings schema loaded from environment variables via Pydantic Settings."""

        # Application
        app_name: str = "NEXUS - Digital Monoculture & Systemic Risk Observatory"
        app_env: str = Field(default="development", alias="APP_ENV")
        debug: bool = Field(default=True, alias="DEBUG")
        log_level: str = Field(default="INFO", alias="LOG_LEVEL")

        # API Server
        api_host: str = Field(default="0.0.0.0", alias="API_HOST")
        api_port: int = Field(default=8000, alias="API_PORT")
        api_prefix: str = Field(default="/api/v1", alias="API_PREFIX")
        cors_origins: List[str] = Field(
            default=["http://localhost:3000", "http://127.0.0.1:3000"],
            alias="CORS_ORIGINS"
        )

        # GitHub API
        github_token: str = Field(default="", alias="GITHUB_TOKEN")
        github_api_url: str = Field(default="https://api.github.com", alias="GITHUB_API_URL")

        # Neo4j Graph Database
        neo4j_uri: str = Field(default="bolt://localhost:7687", alias="NEO4J_URI")
        neo4j_user: str = Field(default="neo4j", alias="NEO4J_USER")
        neo4j_password: str = Field(default="nexus_secure_password", alias="NEO4J_PASSWORD")
        neo4j_database: str = Field(default="neo4j", alias="NEO4J_DATABASE")

        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            extra="ignore"
        )

except ImportError:
    # Graceful fallback when pydantic-settings is not yet installed
    from pydantic import BaseModel

    class Settings(BaseModel):
        """Fallback application settings schema reading directly from environment variables."""

        # Application
        app_name: str = "NEXUS - Digital Monoculture & Systemic Risk Observatory"
        app_env: str = Field(default_factory=lambda: os.getenv("APP_ENV", "development"))
        debug: bool = Field(default_factory=lambda: os.getenv("DEBUG", "true").lower() == "true")
        log_level: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))

        # API Server
        api_host: str = Field(default_factory=lambda: os.getenv("API_HOST", "0.0.0.0"))
        api_port: int = Field(default_factory=lambda: int(os.getenv("API_PORT", "8000")))
        api_prefix: str = Field(default_factory=lambda: os.getenv("API_PREFIX", "/api/v1"))
        cors_origins: List[str] = Field(
            default=["http://localhost:3000", "http://127.0.0.1:3000"]
        )

        # GitHub API
        github_token: str = Field(default_factory=lambda: os.getenv("GITHUB_TOKEN", ""))
        github_api_url: str = Field(default_factory=lambda: os.getenv("GITHUB_API_URL", "https://api.github.com"))

        # Neo4j Graph Database
        neo4j_uri: str = Field(default_factory=lambda: os.getenv("NEO4J_URI", "bolt://localhost:7687"))
        neo4j_user: str = Field(default_factory=lambda: os.getenv("NEO4J_USER", "neo4j"))
        neo4j_password: str = Field(default_factory=lambda: os.getenv("NEO4J_PASSWORD", "nexus_secure_password"))
        neo4j_database: str = Field(default_factory=lambda: os.getenv("NEO4J_DATABASE", "neo4j"))


@lru_cache()
def get_settings() -> Settings:
    """Return a cached singleton instance of application settings."""
    return Settings()
