// ==============================================================================
// NEXUS Cypher Query: Blast Radius Quantification
// Traverses reverse dependency edges to compute impacted downstream repositories
// ==============================================================================

MATCH path = (repo:Repository)-[:DEPENDS_ON*1..6]->(target {id: $target_node_id})
WITH target,
     count(DISTINCT repo) AS total_affected_repos,
     collect(DISTINCT repo.name) AS affected_repo_names,
     min(length(path)) AS shortest_distance
RETURN target.id AS failed_node_id,
       target.name AS failed_node_name,
       labels(target) AS layer,
       total_affected_repos,
       shortest_distance,
       affected_repo_names[0..20] AS sample_impacted_repos;
