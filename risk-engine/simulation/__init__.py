"""NEXUS Failure Simulation & Diversification Subpackage.

Simulates cascading failures across interconnected dependency networks
and calculates diversification recommendations to reduce monoculture vulnerability.
"""

from .failure_simulator import FailureSimulator
from .diversification import DiversificationRecommender

__all__ = ["FailureSimulator", "DiversificationRecommender"]
