from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from nexus_domain import CanonicalEntity, ConfidenceStatus, EntityLayer, Evidence


def test_canonical_entity_requires_grounded_shape():
    entity = CanonicalEntity(
        id="package:pypi:fastapi",
        name="fastapi",
        entity_type="package",
        layer=EntityLayer.PACKAGE,
        source="repository:demo",
        evidence=[Evidence(source="repository:demo", artifact="requirements.txt", excerpt="fastapi")],
        confidence=0.92,
        confidence_status=ConfidenceStatus.CONFIRMED,
        observed_at=datetime.now(timezone.utc),
    )

    assert entity.model_dump(mode="json")["layer"] == "package"
    assert entity.evidence[0].extraction_method == "deterministic"


def test_canonical_entity_rejects_naive_timestamps():
    with pytest.raises(ValidationError):
        CanonicalEntity(
            id="package:pypi:fastapi",
            name="fastapi",
            entity_type="package",
            layer=EntityLayer.PACKAGE,
            source="repository:demo",
            confidence=0.9,
            confidence_status=ConfidenceStatus.PROBABLE,
            observed_at=datetime(2026, 1, 1),
        )
