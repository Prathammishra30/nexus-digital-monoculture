// ==============================================================================
// NEXUS Neo4j Schema Constraints
// Enforces unique identifiers across the 9 observatory layers
// ==============================================================================

// Layer 1: Application / Repository
CREATE CONSTRAINT unique_repository_id IF NOT EXISTS
FOR (r:Repository) REQUIRE r.id IS UNIQUE;

// Layer 2: Package
CREATE CONSTRAINT unique_package_id IF NOT EXISTS
FOR (p:Package) REQUIRE p.id IS UNIQUE;

// Layer 3: API Service
CREATE CONSTRAINT unique_api_id IF NOT EXISTS
FOR (a:API) REQUIRE a.id IS UNIQUE;

// Layer 4: Cloud Provider
CREATE CONSTRAINT unique_cloud_id IF NOT EXISTS
FOR (c:Cloud) REQUIRE c.id IS UNIQUE;

// Layer 5: AI Model & Foundation
CREATE CONSTRAINT unique_aimodel_id IF NOT EXISTS
FOR (m:AIModel) REQUIRE m.id IS UNIQUE;

// Layer 6: Identity Provider
CREATE CONSTRAINT unique_identity_id IF NOT EXISTS
FOR (i:Identity) REQUIRE i.id IS UNIQUE;

// Layer 7: Infrastructure / Container
CREATE CONSTRAINT unique_infra_id IF NOT EXISTS
FOR (inf:Infrastructure) REQUIRE inf.id IS UNIQUE;

// Layer 8: Managed Data Service
CREATE CONSTRAINT unique_data_id IF NOT EXISTS
FOR (d:DataService) REQUIRE d.id IS UNIQUE;

// Layer 9: Maintainer / Organization
CREATE CONSTRAINT unique_maintainer_id IF NOT EXISTS
FOR (m:Maintainer) REQUIRE m.id IS UNIQUE;
