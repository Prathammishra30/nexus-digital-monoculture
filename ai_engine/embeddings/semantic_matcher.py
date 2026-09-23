"""Semantic matching boundary; algorithms are supplied by an embedding provider."""

from .embedding_provider import EmbeddingProvider


class SemanticMatcher:
    def __init__(self, provider: EmbeddingProvider) -> None:
        self.provider = provider
