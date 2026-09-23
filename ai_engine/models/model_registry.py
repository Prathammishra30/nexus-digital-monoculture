"""Small registry for injectable models and test doubles."""

from .base_model import BaseModel


class ModelRegistry:
    def __init__(self) -> None:
        self._models: dict[str, BaseModel] = {}

    def register(self, model: BaseModel) -> None:
        self._models[model.name] = model

    def get(self, name: str) -> BaseModel:
        return self._models[name]
