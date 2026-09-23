# Frontend Feature Boundaries

Each feature owns UI composition and hooks for one workflow. Shared API types remain in `src/types`; transport remains in `src/services`; feature code must not import backend internals.

Required feature folders: `dashboard`, `repositories`, `dependency-graph`, `risk`, `simulation`, `temporal-analysis`, and `ai-intelligence`.
