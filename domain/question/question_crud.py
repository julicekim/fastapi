# question_crud.py
from sqlalchemy.orm import Session

from models import Question


def get_question_list(db: Session):
    questions = db.query(Question) \
        .order_by(Question.create_date.desc()) \
        .all()

    return questions


def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question
