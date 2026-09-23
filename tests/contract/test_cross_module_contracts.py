from datetime import datetime, timezone

from nexus_domain import CanonicalEntity, EntityLayer, GraphRelationship


def test_graph_contract_accepts_canonical_entity_relationship():
    entity = CanonicalEntity(
        id="repository:demo",
        name="demo",
        entity_type="repository",
        layer=EntityLayer.APPLICATION,
        source="github",
        confidence=1.0,
        confidence_status="CONFIRMED",
        observed_at=datetime.now(timezone.utc),
    )
    relationship = GraphRelationship(
        source_id=entity.id,
        relationship_type="DEPENDS_ON",
        target_id="package:pypi:fastapi",
    )

    assert entity.layer.value == "application"
    assert relationship.relationship_type == "DEPENDS_ON"
