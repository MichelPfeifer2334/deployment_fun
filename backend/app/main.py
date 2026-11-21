import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="deployment_fun")

# Comma-separated list of allowed frontend origins, e.g. "https://my-frontend.com"
origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins if o.strip()],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/hello")
def hello():
    return {
        "message": "Hello from the backend!",
        "time": datetime.now(timezone.utc).isoformat(),
    }
