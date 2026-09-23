"""NEXUS API Detector.

Detects third-party SaaS API dependencies (e.g., Stripe, Twilio, SendGrid, Datadog)
by inspecting package dependencies, environment variable conventions, and SDK imports.
"""

from typing import Dict, Any, List

KNOWN_API_SIGNATURES = {
    "stripe": {"provider": "Stripe", "layer": "api", "category": "payments"},
    "twilio": {"provider": "Twilio", "layer": "api", "category": "telecom"},
    "@sendgrid/mail": {"provider": "SendGrid", "layer": "api", "category": "email"},
    "sendgrid": {"provider": "SendGrid", "layer": "api", "category": "email"},
    "datadog": {"provider": "Datadog", "layer": "api", "category": "observability"},
    "@sentry/node": {"provider": "Sentry", "layer": "api", "category": "monitoring"},
    "sentry-sdk": {"provider": "Sentry", "layer": "api", "category": "monitoring"}
}


class APIDetector:
    """Detector for SaaS API service dependencies."""

    def detect_from_packages(self, package_names: List[str]) -> List[Dict[str, Any]]:
        """Identify external API services based on client SDK packages in use.

        Args:
            package_names: List of declared package names.

        Returns:
            List[Dict[str, Any]]: Detected API providers and service roles.
        """
        # TODO: Match package_names against KNOWN_API_SIGNATURES database
        return []

    def detect_from_environment_keys(self, env_keys: List[str]) -> List[Dict[str, Any]]:
        """Identify API services by recognizing API key variable names (e.g. STRIPE_API_KEY)."""
        # TODO: Match pattern prefixes (STRIPE_*, TWILIO_*, SENDGRID_*)
        return []
