from app.database import engine
from app.models import Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.alerts import router as alerts_router
from app.api.incidents import router as incidents_router
from app.api.analyze import router as analyze_router
from app.api.analytics import router as analytics_router
from app.api.search import router as search_router
from app.api.chat import (
    router as chat_router
)
app = FastAPI(
    title="DroneSentinel Agent API",
    version="1.0.0"
)

Base.metadata.create_all(
    bind=engine
)

app.include_router(
    search_router,
    prefix="/search",
    tags=["Search"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "DroneSentinel Agent API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(
    alerts_router,
    prefix="/alerts",
    tags=["Alerts"]
)

app.include_router(
    incidents_router,
    prefix="/incidents",
    tags=["Incidents"]
)

app.include_router(
    analyze_router,
    prefix="/analyze",
    tags=["Analyze"]
)

app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)
