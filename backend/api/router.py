"""NEXUS API Root Router.

Aggregates modular route handlers for repositories, dependencies, risk analytics,
and simulation endpoints.
"""

from fastapi import APIRouter
from backend.api.routes import repositories, dependencies, risk, simulation, intelligence

api_router = APIRouter()

api_router.include_router(repositories.router)
api_router.include_router(dependencies.router)
api_router.include_router(risk.router)
api_router.include_router(simulation.router)
api_router.include_router(intelligence.router)
