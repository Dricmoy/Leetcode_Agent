# Leetcode_Agent

```
    LeetCodeAgent/
    ├─ backend/
    │   ├─ app.py               # main FastAPI App
    │   ├─ models.py            # DB connection
    │   ├─ schemas.py           # SQLAlchemy models
    │   ├─ database.py          # Pydantic Schemas
    │   ├─ api/
    │   │    ├─ submissions.py  # submission endpoints
    │   │    ├─ problems.py     # problem endpoints
    │   │    └─ coach.py        # AI coaching endpoints
    │   └─ github_sync.py       # Github auto-save logic
    ├─ frontend/
    │   ├─ package.json
    │   ├─ vite.config.ts
    │   └─ src/
    │        ├─ App.tsx
    │        ├─ main.tsx
    │        ├─ pages/
    │        ├─ components/
    │        └─ services/api.ts
    ├─ docker-compose.yml
    └─ tampermonkey/
        └─ auto_coach.user.js

```