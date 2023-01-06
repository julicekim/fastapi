# answer_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)


@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):
    # create answer
    question = question_crud.get_question(db, question_id)

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question {question_id} not found",
        )
    answer_crud.create_answer(db,
                              question=question,
                              answer_create=_answer_create)
