# Branching And Security

Branches are `main`, `backend`, `frontend`, `ai-engine`, `discovery-engine`, and `integration`. `main` stays stable; use pull requests, no force push, and no destructive history rewrites. Shared contracts require tech-lead review.

Copy `.env.example` to `.env` locally. Secrets belong in environment variables or GitHub Actions secrets. Log identifiers and statuses, never tokens, prompts containing secrets, or provider responses with credentials.
