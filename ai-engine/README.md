# AI Engine

The AI engine is a provider-neutral semantic transformation layer. The executable import package is `ai_engine` because Python package names cannot contain hyphens; this directory is the requested ownership tree and contains compatibility/documentation shims.

Flow: raw artifact -> deterministic extraction -> task-routed model -> typed output -> schema/evidence/consistency validation -> confidence status -> canonical domain object.

No API key is required for tests. Provider credentials must come from environment configuration and must never be logged or committed.
