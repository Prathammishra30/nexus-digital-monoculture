"""Local provider adapter placeholder; no network call is made by the foundation."""

from ai_engine.models.base_model import BaseModel
from .base_provider import ModelProvider


class LocalProvider(ModelProvider):
    name = "local"

    def __init__(self, model_factory: dict[str, BaseModel] | None = None) -> None:
        self._models = model_factory or {}

    def create_model(self, model_name: str) -> BaseModel:
        return self._models[model_name]
