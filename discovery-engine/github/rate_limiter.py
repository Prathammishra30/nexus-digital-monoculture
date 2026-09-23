"""Simple async rate-limit gate for GitHub API adapters."""

import asyncio
from datetime import datetime, timezone


class RateLimiter:
    def __init__(self, minimum_interval_seconds: float = 0.0) -> None:
        self.minimum_interval_seconds = max(0.0, minimum_interval_seconds)
        self._last_request: datetime | None = None

    async def wait(self) -> None:
        if self._last_request is not None:
            elapsed = (datetime.now(timezone.utc) - self._last_request).total_seconds()
            delay = self.minimum_interval_seconds - elapsed
            if delay > 0:
                await asyncio.sleep(delay)
        self._last_request = datetime.now(timezone.utc)
