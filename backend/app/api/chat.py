from fastapi import APIRouter

from app.agents.investigator import (
    investigate
)

router = APIRouter()


@router.post("/")
def chat(payload: dict):

    query = payload["query"]

    response = investigate(
        query
    )

    return {
        "answer": response
    }
