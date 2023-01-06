# question_schema.py
import datetime

from pydantic import BaseModel, validator
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


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_emtpy(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용 되지 않습니다.")
        return v


class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []