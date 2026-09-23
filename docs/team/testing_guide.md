# Testing Guide

Run the complete Python suite with `python -m pytest -q`, compile with `python -m compileall -q backend nexus_domain ai_engine discovery-engine risk-engine graph`, and run `python scripts/validation/validate_architecture.py`.

For frontend changes run `npm ci` and `npm run build`. API startup is checked by importing `backend.app.main:app` and the backend smoke tests. Contract tests must cover required fields, timestamps, evidence, and confidence states. Never use real provider credentials in tests.
