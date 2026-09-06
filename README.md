# neural-agent-os — Autonomous Multi-Agent Operating Platform
Flagship project (ATLAS FORGE cycle). LLM routing: default free models. Built in-house.

## Endpoints
GET /health — defensive-active (score verified >=82)
GET /agent — real agent turn (no placeholder)
GET /docs — OpenAPI

## Architecture
Next.js + Three.js (frontend) + FastAPI (orchestration) + PostgreSQL + Redis + Vector DB.

## Security
Defensive only. Rate limits. Security headers. No secrets. Audit log persistent.

## Requirements
Real functionality. No boilerplate. Score floor >=80.

## License
Public. Proprietary build.
