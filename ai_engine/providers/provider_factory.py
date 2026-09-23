"""Provider construction boundary. Vendor SDKs belong behind this factory."""

from .base_provider import ModelProvider


class ProviderFactory:
    def __init__(self, providers: dict[str, ModelProvider] | None = None) -> None:
        self._providers = providers or {}

    def register(self, provider: ModelProvider) -> None:
        self._providers[provider.name] = provider

    def get(self, name: str) -> ModelProvider:
        return self._providers[name]
