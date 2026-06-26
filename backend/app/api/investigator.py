from fastapi import APIRouter

from pydantic import BaseModel

from app.investigator.router import investigate_question

router = APIRouter()


class Question(BaseModel):

    question: str


@router.post("/")
def ask(q: Question):

    answer = investigate_question(
        q.question
    )

    return {
        "answer": answer
    }
