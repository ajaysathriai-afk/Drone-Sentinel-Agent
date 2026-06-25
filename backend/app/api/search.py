from fastapi import APIRouter
from app.vectorstore.chroma_db import collection

router = APIRouter()

@router.get("/")
def search_incidents(query: str):

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    return results
