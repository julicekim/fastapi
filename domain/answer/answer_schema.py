# answer_schema.py
import datetime
from typing import Optional

from pydantic import BaseModel, validator
from domain.user.user_schema import User


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('content is empty')
        return v


class Answer(BaseModel):
    id: str
    content: str
    create_date: datetime.datetime
    user: Optional[User]
    question_id: int
    modify_date: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class AnswerUpdate(AnswerCreate):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int
