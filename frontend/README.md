# NEXUS Frontend - Observability Dashboard

This directory houses the user interface for the NEXUS Digital Monoculture & Systemic Risk Observatory.

## Architecture

The frontend is structured to present macro ecosystem metrics and micro dependency graphs:

- `src/components/`: Reusable UI components (graph visualizers, risk scorecards, metric cards, simulation controls).
- `src/pages/`: Main application routes/views (Ecosystem Overview, Repository Detail, Failure Simulator, Concentration Heatmaps).
- `src/services/`: API client services communicating with the NEXUS FastAPI backend (`/api/v1`).
- `src/hooks/`: React custom hooks for data fetching, graph interactions, and simulation state.
- `src/types/`: TypeScript interface definitions mirroring backend Pydantic models.
- `src/utils/`: Formatting, color palettes, graph math, and calculation helpers.
- `public/`: Static assets, icons, and graph presets.

## Planned Tech Stack
- React / Next.js
- Graph Visualization (e.g., Cytoscape.js, D3.js, or React Flow)
- Charting (e.g., Recharts / Tremor)
- TailwindCSS or Vanilla CSS
