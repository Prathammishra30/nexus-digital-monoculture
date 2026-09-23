// ==============================================================================
// NEXUS Neo4j Performance Indexes
// Optimizes lookups, traversal speed, and concentration aggregations
// ==============================================================================

// Fast name and ecosystem lookups
CREATE INDEX idx_repository_name IF NOT EXISTS
FOR (r:Repository) ON (r.name);

CREATE INDEX idx_package_name_eco IF NOT EXISTS
FOR (p:Package) ON (p.name, p.ecosystem);

CREATE INDEX idx_provider_name IF NOT EXISTS
FOR (c:Cloud) ON (c.name);

CREATE INDEX idx_api_provider IF NOT EXISTS
FOR (a:API) ON (a.name);

CREATE INDEX idx_aimodel_name IF NOT EXISTS
FOR (m:AIModel) ON (m.name);

CREATE INDEX idx_maintainer_login IF NOT EXISTS
FOR (m:Maintainer) ON (m.login);

// Relationship index on dependency edges for traversal performance
CREATE INDEX idx_rel_depends_on IF NOT EXISTS
FOR ()-[r:DEPENDS_ON]-() ON (r.relationship_kind);
