# question_crud.py
from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question, User
from sqlalchemy.orm import Session


def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    _questions = db.query(Question) \
        .order_by(Question.create_date.desc())

    total = _questions.count()

    questions = _questions.offset(skip).limit(limit).all()

    return total, questions


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question


def create_question(db: Session,
                    question_create: QuestionCreate,
                    user: User):
    question = Question(
        subject=question_create.subject,
        content=question_create.content,
        create_date=datetime.now(),
        user=user
    )

    db.add(question)
    db.commit()
