"""Task-based model routing with configuration-driven selection."""

from enum import Enum

from .base_model import BaseModel
from .model_config import ModelConfig


class TaskCategory(str, Enum):
    CLASSIFICATION = "classification"
    EXTRACTION = "extraction"
    SEMANTIC_ANALYSIS = "semantic_analysis"
    ARCHITECTURE_ANALYSIS = "architecture_analysis"
    SUMMARIZATION = "summarization"
    EMBEDDING = "embedding"
    GRAPH_REASONING = "graph_reasoning"


class ModelRouter:
    def __init__(self, routes: dict[TaskCategory, ModelConfig] | None = None) -> None:
        self._routes = routes or {}
        self._models: dict[str, BaseModel] = {}

    def register_model(self, name: str, model: BaseModel) -> None:
        self._models[name] = model

    def select(self, task: TaskCategory) -> BaseModel:
        config = self._routes.get(task)
        if config is None:
            raise LookupError(f"No model route configured for task '{task.value}'")
        try:
            return self._models[config.model_name]
        except KeyError as error:
            raise LookupError(f"Model '{config.model_name}' is not registered") from error
