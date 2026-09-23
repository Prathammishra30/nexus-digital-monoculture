"""Graph persistence agent interface."""

from abc import ABC, abstractmethod

from nexus_domain import CanonicalEntity, GraphRelationship


class GraphAgent(ABC):
    @abstractmethod
    async def persist(self, entities: list[CanonicalEntity], relationships: list[GraphRelationship]) -> None:
        raise NotImplementedError
