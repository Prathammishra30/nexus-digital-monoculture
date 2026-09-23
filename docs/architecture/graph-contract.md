# Graph Contract

Neo4j labels represent the nine layers: `Repository`, `Package`, `API`, `Cloud`, `AIModel`, `Identity`, `Infrastructure`, `DataService`, and `Maintainer`.

Canonical relationships are `DEPENDS_ON`, `HOSTED_ON`, `CALLS`, `AUTHENTICATES_WITH`, `USES_MODEL`, `STORES_DATA_IN`, `BUILT_WITH`, and `MAINTAINED_BY`. Every persisted node has a stable `id`; relationships may carry evidence, confidence, version, and kind properties.

Only validated canonical objects may cross into graph persistence.
