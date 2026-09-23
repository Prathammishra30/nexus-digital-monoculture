# NEXUS Research: Systemic Risk & Monoculture Metrics

This document outlines the theoretical frameworks and metrics evaluated by NEXUS.

## 1. Herfindahl-Hirschman Index (HHI)

The Herfindahl-Hirschman Index measures concentration within an individual layer:

$$\text{HHI} = \sum_{i=1}^{N} s_i^2$$

where $s_i$ is the percentage market or adoption share of entity $i$.
- **HHI < 1500**: Unconcentrated / Resilient Diversity
- **1500 <= HHI <= 2500**: Moderate Monoculture
- **HHI > 2500**: Severe Monoculture / High Systemic Risk

## 2. Monoculture Index ($M$)

Normalized composite score $[0.0, 1.0]$ integrating Simpson's index of diversity and Shannon entropy:

$$M = 1 - \sum p_i^2$$

## 3. Blast Radius & Common Roots

Blast radius measures the downstream reachable subgraph in the reverse dependency graph when a given node $v$ experiences failure:

$$\text{BlastRadius}(v) = |\{ r \in \text{Repositories} \mid r \rightsquigarrow v \}|$$

## 4. Maintainer Bus Factor

Calculates the minimum maintainer subset whose departure causes project stall (Pareto commit distribution $>80\%$).

## 5. Monoculture Velocity ($V_m$)

The first derivative of concentration metrics over time to evaluate whether ecosystems are rapidly converging onto single points of failure.
