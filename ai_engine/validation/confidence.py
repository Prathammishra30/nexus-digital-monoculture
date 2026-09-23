"""Confidence scoring is separate from risk scoring."""

from nexus_domain import ConfidenceStatus


class ConfidenceEvaluator:
    def __init__(self, confirmed: float = 0.85, probable: float = 0.70, uncertain: float = 0.50) -> None:
        self.confirmed = confirmed
        self.probable = probable
        self.uncertain = uncertain

    def status(self, score: float, has_evidence: bool, has_conflict: bool = False) -> ConfidenceStatus:
        if score < 0 or score > 1:
            raise ValueError("confidence must be between 0 and 1")
        if not has_evidence or has_conflict or score < self.uncertain:
            return ConfidenceStatus.REJECTED
        if score >= self.confirmed:
            return ConfidenceStatus.CONFIRMED
        if score >= self.probable:
            return ConfidenceStatus.PROBABLE
        return ConfidenceStatus.UNCERTAIN
