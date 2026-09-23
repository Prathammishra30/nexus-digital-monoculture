"""NEXUS Herfindahl-Hirschman Index (HHI) Calculator.

Implements structural market concentration calculations for software ecosystems:
HHI = sum(s_i^2) where s_i is the percentage share of entity i.

Standard HHI thresholds:
- HHI < 1500: Unconcentrated (healthy diversity)
- 1500 <= HHI <= 2500: Moderately concentrated
- HHI > 2500: Highly concentrated (systemic monoculture)
"""

from typing import Dict, List, Tuple


class HerfindahlHirschmanCalculator:
    """Calculates Herfindahl-Hirschman Index (HHI) across distribution shares."""

    def calculate_hhi(self, shares: List[float]) -> float:
        """Calculate raw HHI score from percentage market/dependency shares.

        Args:
            shares: List of percentage shares summing to ~100.0 (e.g. [50.0, 30.0, 20.0]).

        Returns:
            float: HHI score ranging between 0 and 10,000.
        """
        # TODO: Implement HHI formula: sum(s ** 2 for s in shares)
        # Rule: Do not implement full risk formulas yet
        return 0.0

    def categorize_concentration(self, hhi_score: float) -> str:
        """Categorize HHI score into standardized regulatory risk tiers.

        Returns:
            str: 'low', 'moderate', or 'high'.
        """
        # TODO: Return concentration classification based on DOJ/FTC benchmarks
        return "low"
