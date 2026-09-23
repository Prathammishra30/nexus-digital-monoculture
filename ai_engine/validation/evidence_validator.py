"""Evidence grounding checks."""

from nexus_domain import Evidence


class EvidenceValidator:
    def validate(self, evidence: list[Evidence]) -> bool:
        return bool(evidence) and all(item.source and item.artifact for item in evidence)
