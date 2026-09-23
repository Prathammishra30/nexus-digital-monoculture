// ==============================================================================
// NEXUS Cypher Query: Dependency Graph Traversal
// Retrieves direct and transitive dependency trees for a given repository
// ==============================================================================

// Direct Dependencies
MATCH (r:Repository {id: $repo_id})-[rel:DEPENDS_ON]->(dep)
RETURN dep.id AS dependency_id,
       dep.name AS name,
       labels(dep) AS labels,
       rel.relationship_kind AS kind,
       rel.version_spec AS version;

// Transitive Dependency Tree (up to depth $max_depth)
MATCH path = (r:Repository {id: $repo_id})-[:DEPENDS_ON*1..5]->(dep)
RETURN dep.id AS dependency_id,
       dep.name AS name,
       length(path) AS depth,
       [n IN nodes(path) | n.name] AS dependency_chain;
