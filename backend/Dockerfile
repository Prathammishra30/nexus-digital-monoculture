# Backend Dockerfile for NEXUS
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if required
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source modules
COPY backend /app/backend
COPY discovery-engine /app/discovery-engine
COPY ai-engine /app/ai-engine
COPY risk-engine /app/risk-engine
COPY graph /app/graph

ENV PYTHONPATH="/app:/app/backend:/app/discovery-engine:/app/ai-engine:/app/risk-engine:/app/graph"

EXPOSE 8000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]