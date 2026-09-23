# Development Workflow

1. Pull `main`, create a focused branch, and identify the owning module.
2. Read the module guide and contract before editing.
3. Add or update a focused test first when behavior changes.
4. Run `python -m pytest -q`, frontend build when frontend files change, and architecture validation.
5. Open a pull request with contract changes called out explicitly.
6. A reviewer checks imports, ownership boundaries, secrets, and rollback behavior before merge.

Use adapters and interfaces for external systems. Keep algorithms in their engine, not in API handlers.
