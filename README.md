# deployment_fun
Small project to test some deployment things, mostly CI/CD

## Struktur

- `backend/` – FastAPI, ein Endpunkt: `GET /api/hello`
- `frontend/` – Vue 3 + Vite, ein Button, der das Backend aufruft

## Lokal starten

**Backend** (Port 8000):

```bash
cd backend
poetry install                              # inkl. Dev-Dependencies
poetry run uvicorn app.main:app --reload
poetry run pytest                           # Tests
```

**Frontend** (Port 5173):

```bash
cd frontend
npm install
npm run dev     # Dev-Server
npm run build   # Statischer Build nach dist/
```

## Konfiguration

| Variable        | Wo       | Default                 | Zweck                                        |
|-----------------|----------|-------------------------|----------------------------------------------|
| `CORS_ORIGINS`  | Backend  | `http://localhost:5173` | Erlaubte Frontend-Origins (komma-getrennt)   |
| `VITE_API_URL`  | Frontend | `http://localhost:8000` | Backend-URL, wird **zur Build-Zeit** eingebaut |
