"""NEXUS Risk Engine Package.

Performs quantitative systemic risk evaluation across the software supply chain:
- Herfindahl-Hirschman Index (HHI) concentration calculations
- Normalized Monoculture Indexes across 9 layers
- Maintainer bus-factor and human concentration risk
- Downstream blast radius computation
- Cascading failure simulations & diversification recommendations
- Temporal monoculture velocity tracking
"""

from .risk_pipeline import RiskPipeline

__all__ = ["RiskPipeline"]
