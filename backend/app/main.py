"""NEXUS Core Application Entrypoint.

Initializes FastAPI application instance, configures CORS middleware,
registers API route blueprints, and provides server lifecycle events.
"""

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import get_settings
from backend.api.router import api_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager to handle startup and shutdown routines."""
    # Startup: Connect to graph database and initialize caches
    # TODO: Verify Neo4j connectivity via graph.neo4j.client.Neo4jClient
    yield
    # Shutdown: Cleanly close connection pools
    # TODO: Close Neo4j driver sessions


app = FastAPI(
    title=settings.app_name,
    description="Observatory measuring digital monoculture and systemic fragility across software ecosystems.",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure Cross-Origin Resource Sharing (CORS)
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Register aggregated API routes under configured prefix (default: /api/v1)
app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/", tags=["Health"])
async def root():
    """Observatory root endpoint."""
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "status": "operational",
        "docs": "/docs",
        "api_prefix": settings.api_prefix
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for container probes."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": settings.app_env
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
