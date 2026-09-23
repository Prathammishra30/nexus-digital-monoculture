# Domain Contracts

`nexus_domain/contracts.py` is the cross-module source of truth.

`CanonicalEntity` requires `id`, `name`, `entity_type`, `layer`, `source`, `confidence`, `confidence_status`, and timezone-aware `observed_at`; evidence and reasoning metadata are optional collections. `Evidence` requires source and artifact. `GraphRelationship` requires source ID, relationship type, and target ID. `SnapshotMetadata` provides stable time-series identity.

Confidence values describe observation quality: `CONFIRMED`, `PROBABLE`, `UNCERTAIN`, or `REJECTED`. They do not rank systemic risk. New consumers should import these models instead of creating parallel enums.
