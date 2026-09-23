# Risk Engine Guide

**What:** concentration, maintainer signals, blast radius, simulation, and temporal calculations.

**Input:** canonical domain/graph projections and snapshots. **Output:** typed metrics and scenarios. Risk scores must never be used as confidence statuses.

Own `risk-engine/`; do not import FastAPI or frontend modules. Keep research assumptions documented and configurable. Test formulas with small deterministic fixtures.
