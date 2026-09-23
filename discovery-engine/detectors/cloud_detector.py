"""NEXUS Cloud Detector.

Detects underlying hyperscaler and cloud provider dependencies (AWS, GCP, Azure, Cloudflare)
across infrastructure templates, Docker configurations, and SDK inclusions.
"""

from typing import Dict, Any, List

CLOUD_SDK_SIGNATURES = {
    # AWS
    "boto3": "aws",
    "@aws-sdk/client-s3": "aws",
    "aws-sdk": "aws",
    # GCP
    "google-cloud-storage": "gcp",
    "@google-cloud/storage": "gcp",
    # Azure
    "azure-storage-blob": "azure",
    "@azure/storage-blob": "azure",
    # Cloudflare
    "cloudflare": "cloudflare",
    "wrangler": "cloudflare"
}


class CloudDetector:
    """Detector for hyperscaler and cloud platform lock-in."""

    def detect_from_packages(self, packages: List[str]) -> List[Dict[str, Any]]:
        """Identify cloud providers based on presence of official cloud SDK packages."""
        # TODO: Match SDKs against CLOUD_SDK_SIGNATURES
        return []

    def detect_from_terraform(self, tf_providers: List[str]) -> List[Dict[str, Any]]:
        """Identify cloud providers declared in Terraform configurations."""
        # TODO: Map aws, google, azurerm to canonical cloud provider nodes
        return []

    def detect_from_ci_workflows(self, workflow_content: str) -> List[Dict[str, Any]]:
        """Scan GitHub actions for cloud login steps (e.g. aws-actions/configure-aws-credentials)."""
        # TODO: Parse workflow action steps
        return []
