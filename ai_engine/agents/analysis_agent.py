"""Analysis agent interface."""

from abc import ABC, abstractmethod
from typing import Any


class AnalysisAgent(ABC):
    @abstractmethod
    async def analyze(self, subject: Any) -> Any:
        raise NotImplementedError
