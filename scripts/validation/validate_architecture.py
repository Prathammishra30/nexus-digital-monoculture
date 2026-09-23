"""Fast, dependency-light architecture guardrail for CI."""

import sys
from importlib import import_module
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
REQUIRED = (
    "backend",
    "discovery-engine",
    "ai-engine",
    "ai_engine",
    "risk-engine",
    "graph",
    "nexus_domain",
    "frontend/src/features",
    "docs/team",
)


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing architecture paths:", ", ".join(missing))
        return 1
    for module in ("nexus_domain", "ai_engine", "backend.app.main"):
        import_module(module)
    print("Architecture validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
