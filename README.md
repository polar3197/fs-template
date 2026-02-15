# fs-template

Minimal full-stack template with FastAPI, React (Vite), PostgreSQL, and nginx using Docker Compose.

## Stack
- FastAPI backend: `src/api`
- React frontend: `src/ui`
- PostgreSQL 16
- nginx reverse proxy

## Prerequisites
- Docker
- Docker Compose

## Environment
Set these in `.env`:
- `PG_USER`
- `PG_PASSWORD`
- `PG_NAME`
- `PG_HOST`
- `PG_PORT`

## Run
```bash
docker compose up --build
```

Open:
- App: `http://localhost`
- API health: `http://localhost/api/`

Stop:
```bash
docker compose down
```
