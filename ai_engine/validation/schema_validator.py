"""Schema validation boundary for model responses."""

from typing import Any

from pydantic import BaseModel


class SchemaValidator:
    def validate(self, payload: Any, schema: type[BaseModel]) -> BaseModel:
        if isinstance(payload, schema):
            return payload
        return schema.model_validate(payload)
