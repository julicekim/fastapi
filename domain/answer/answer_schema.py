# answer_schema.py
import datetime

from pydantic import BaseModel, validator


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

    class Config:
        orm_mode = True
