"""NEXUS Maintainer Risk Subpackage.

Quantifies human-layer fragility, maintainer bus factor, project abandonment likelihood,
and single-maintainer critical dependency vulnerabilities.
"""

from .maintainer_risk import MaintainerRiskCalculator

__all__ = ["MaintainerRiskCalculator"]
