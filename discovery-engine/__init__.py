"""NEXUS Discovery Engine Package.

Responsible for cloning/fetching code repositories from GitHub, parsing
manifest and lock files across multiple package ecosystems, detecting
third-party cloud, API, and AI model providers, and transforming discoveries
into canonical graph representations.
"""

from .pipeline import DiscoveryPipeline

__all__ = ["DiscoveryPipeline"]
