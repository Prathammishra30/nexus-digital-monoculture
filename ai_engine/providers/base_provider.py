"""Provider adapter interface."""

from abc import ABC, abstractmethod
from typing import Any

from ai_engine.models.base_model import BaseModel


class ModelProvider(ABC):
    name: str

    @abstractmethod
    def create_model(self, model_name: str) -> BaseModel:
        raise NotImplementedError

    async def healthcheck(self) -> dict[str, Any]:
        return {"provider": self.name, "available": True}
