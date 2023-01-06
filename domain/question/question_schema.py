# question_schema.py
import datetime

from pydantic import BaseModel
from domain.answer.answer_schema import Answer


class Question(BaseModel):
    """
    Question schema
    """
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        orm_mode = True
