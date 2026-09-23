"""Typed transformer contract."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class Transformer(ABC, Generic[TInput, TOutput]):
    input_schema: type[TInput]
    output_schema: type[TOutput]

    @abstractmethod
    async def transform(self, payload: TInput) -> TOutput:
        """Transform evidence without bypassing validation."""
        raise NotImplementedError
