"""Anthropic adapter boundary. Credentials and SDK wiring are intentionally deferred."""

from .local_provider import LocalProvider


class AnthropicProvider(LocalProvider):
    name = "anthropic"
