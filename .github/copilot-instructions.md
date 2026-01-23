# Copilot instructions for blood-donation-system

This file gives focused, actionable guidance to AI coding agents working in this repository.

1) Big picture
- Backend: FastAPI app in `backend/app` serving a small REST API (routes under `backend/app/routes`).
- Frontend: Vite + React app in `blood-donation-frontend/src` (entry: `App.jsx`, small `Login.jsx`).
- Data: MongoDB accessed via `backend/app/database.py` using `MONGO_URI` env var; collection `donors`.
- Auth: Simple JWT auth in `backend/app/auth.py`. `POST /login` issues a token; protected endpoints use `Depends(verify_token)`.

2) Key integration points and workflows
- Run backend locally (dev): from `backend/` run `uvicorn app.main:app --reload --host 0.0.0.0 --port 8080`.
- Run frontend locally: `cd blood-donation-frontend && npm install && npm run dev` (Vite default port 5173).
- Docker: `backend/Dockerfile` builds the backend; `docker-compose.yml` defines `backend` service and reads `.env` for `MONGO_URI`.
- Environment: `MONGO_URI` must be set (the code raises if missing). Docker-compose maps port `8080`.

3) Request/response and auth details agents should follow
- `POST /login` (implemented in `backend/app/auth.py`) returns a JWT in `access_token`. The secret is hardcoded (`SECRET_KEY = "abcdabcd"`) — treat as test-only.
- Protected routes: attach header `Authorization: Bearer <token>` when calling `/donors` endpoints. The frontend stores the token in `localStorage` under key `token`.
- Donor records are plain JSON stored to the `donors` collection. Filtering supports `blood_group` and `city` query params (see `backend/app/routes/donors.py`).

4) Project-specific conventions and patterns
- Small, flat FastAPI router modules: each file in `backend/app/routes` registers endpoints via `APIRouter` and is included in `app.main`.
- DB objects: when returning Mongo documents, `_id` is converted to string manually in `donors.py`.
- Frontend currently posts login to a deployed URL (`https://blood-donation-system-c82d.onrender.com/login`) inside `Login.jsx` — update to local backend (`http://localhost:8080/login`) when developing locally.
 - Frontend currently posts login to a deployed URL (`https://blood-donation-system-c82d.onrender.com/login`) inside `Login.jsx` — update to local backend (`http://localhost:8080/login`) when developing locally.
 - Use the `RENDER_URL` env var (set to `https://blood-donation-system-c82d.onrender.com`) when deploying; backend `main.py` will include it in allowed CORS origins.
- `blood-donation-frontend/src/donors.jsx` is empty — expect incomplete frontend work here.

5) Files to inspect when making changes
- `backend/app/main.py`, `backend/app/auth.py`, `backend/app/database.py`, `backend/app/routes/donors.py`.
- `backend/Dockerfile`, `docker-compose.yml`, `backend/requirements.txt`.
- `blood-donation-frontend/src/Login.jsx`, `App.jsx`, and `donors.jsx`.

6) Example calls (exact syntax agents can use)
- Login (curl):
  curl -s -X POST http://localhost:8080/login | jq
- Get donors (curl):
  curl -H "Authorization: Bearer <token>" http://localhost:8080/donors

7) Safety / scope notes for AI agents
- The JWT secret is hardcoded for demo purposes; do not assume production-grade security. Keep fixes minimal and clearly explain security changes.
- No tests or CI are present — run local servers to validate behavior.

If any section is unclear or you want more examples (e.g., attaching auth headers from React or a minimal `.env` example), tell me which part to expand.
