"""Orchestration boundary for discovery -> transform -> validate -> persist."""

from abc import ABC, abstractmethod
from typing import Any


class OrchestrationAgent(ABC):
    @abstractmethod
    async def run(self, request: Any) -> Any:
        raise NotImplementedError
