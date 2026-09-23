// ==============================================================================
// NEXUS Cypher Query: Common Root Discovery
// Identifies hidden shared root dependencies across seemingly independent repositories
// ==============================================================================

MATCH (r1:Repository)-[:DEPENDS_ON*1..5]->(root)
MATCH (r2:Repository)-[:DEPENDS_ON*1..5]->(root)
WHERE r1 <> r2 AND (labels(root) IN [['Package'], ['Cloud'], ['API'], ['Identity'], ['AIModel']])
WITH root, count(DISTINCT r1) + 1 AS dependent_count, collect(DISTINCT r1.name) AS repos
ORDER BY dependent_count DESC
RETURN root.id AS common_root_id,
       root.name AS root_name,
       labels(root) AS layer,
       dependent_count,
       repos[0..10] AS sample_dependent_repos
LIMIT 50;
