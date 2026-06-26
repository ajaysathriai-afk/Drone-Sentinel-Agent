from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base

from app.api.alerts import router as alerts_router
from app.api.incidents import router as incidents_router
from app.api.analyze import router as analyze_router
from app.api.analytics import router as analytics_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router
from app.api import investigator

app = FastAPI(
    title="DroneSentinel Agent API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(
    investigator.router,
    prefix="/investigator",
    tags=["Investigator"]
)

app.include_router(search_router, prefix="/search", tags=["Search"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
app.include_router(incidents_router, prefix="/incidents", tags=["Incidents"])
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
