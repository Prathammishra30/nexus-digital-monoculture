"""Unit Tests for Risk Calculators.

Verifies instantiation and basic interface contracts of concentration and risk calculators.
"""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir / "risk-engine"))
sys.path.insert(0, str(root_dir))

from concentration.hhi import HerfindahlHirschmanCalculator
from concentration.monoculture_index import MonocultureIndexCalculator
from maintainer.maintainer_risk import MaintainerRiskCalculator
from blast_radius.calculator import BlastRadiusCalculator
from simulation.failure_simulator import FailureSimulator
from simulation.diversification import DiversificationRecommender
from temporal.monoculture_velocity import MonocultureVelocityCalculator


def test_risk_calculator_instantiations():
    """Verify all risk calculator classes can be instantiated."""
    hhi = HerfindahlHirschmanCalculator()
    mono = MonocultureIndexCalculator()
    maintainer = MaintainerRiskCalculator()
    blast = BlastRadiusCalculator()
    sim = FailureSimulator()
    div = DiversificationRecommender()
    vel = MonocultureVelocityCalculator()

    assert hhi is not None
    assert mono is not None
    assert maintainer is not None
    assert blast is not None
    assert sim is not None
    assert div is not None
    assert vel is not None


def test_hhi_base_contract():
    """Verify HHI calculator default return conforms to contract."""
    hhi = HerfindahlHirschmanCalculator()
    score = hhi.calculate_hhi([50.0, 50.0])
    assert isinstance(score, float)
