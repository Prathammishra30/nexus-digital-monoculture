/**
 * NEXUS Core Type Definitions
 * TypeScript interfaces mirroring backend domain models.
 */

export type LayerType =
  | 'application'
  | 'package'
  | 'api'
  | 'cloud'
  | 'ai_model'
  | 'identity'
  | 'infrastructure'
  | 'data'
  | 'maintainer';

export type EcosystemType = 'npm' | 'pypi' | 'maven' | 'golang' | 'docker' | 'terraform' | 'custom';

export interface RepositorySummary {
  id: string;
  name: string;
  owner: string;
  url: string;
  ecosystem: EcosystemType;
  stars: number;
  dependencyCount: number;
  riskScore: number;
}

export interface ConcentrationMetric {
  layer: LayerType;
  hhiScore: number;
  topEntity: string;
  topEntityShare: number;
  monocultureRiskLevel: 'low' | 'moderate' | 'high' | 'critical';
}

export interface SimulationScenario {
  targetNodeId: string;
  targetNodeType: LayerType;
  cascadingFailures: string[];
  totalAffectedRepositories: number;
  estimatedBlastRadius: number;
}

export type ConfidenceStatus = 'CONFIRMED' | 'PROBABLE' | 'UNCERTAIN' | 'REJECTED';

export interface Evidence {
  source: string;
  artifact: string;
  excerpt?: string;
  line_start?: number;
  line_end?: number;
  extraction_method: string;
}

export interface CanonicalEntity {
  id: string;
  name: string;
  entity_type: string;
  layer: LayerType;
  source: string;
  evidence: Evidence[];
  confidence: number;
  confidence_status: ConfidenceStatus;
  reasoning_metadata: Record<string, unknown>;
  observed_at: string;
  extraction_method: string;
}

export interface GraphRelationship {
  source_id: string;
  relationship_type: string;
  target_id: string;
  evidence: Evidence[];
  confidence: number;
  properties: Record<string, unknown>;
}
