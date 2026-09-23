"""Provider-neutral structured model contract."""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseModel(ABC):
    """A model capable of returning structured output for a task."""

    name: str

    @abstractmethod
    async def generate(self, prompt: str, *, schema: type[Any], metadata: Dict[str, Any] | None = None) -> Any:
        """Generate output validated by the caller against ``schema``."""
        raise NotImplementedError
