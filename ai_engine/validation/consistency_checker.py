"""Deterministic conflict detection hook."""

from typing import Iterable


class ConsistencyChecker:
    def has_conflict(self, claims: Iterable[str], deterministic_tokens: Iterable[str]) -> bool:
        known = {token.casefold() for token in deterministic_tokens}
        return any(claim.casefold() not in known for claim in claims)
