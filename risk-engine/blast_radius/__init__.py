"""NEXUS Blast Radius Subpackage.

Quantifies the downstream systemic damage caused if a specific package, API,
cloud region, or maintainer experiences an outage, vulnerability, or compromise.
"""

from .calculator import BlastRadiusCalculator

__all__ = ["BlastRadiusCalculator"]
