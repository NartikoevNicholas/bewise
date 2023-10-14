from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declarative_base
)

from sqlalchemy.dialects.postgresql import TIMESTAMP


Base = declarative_base()


class Problem(Base):
    __tablename__ = 'problem'

    id: Mapped[int] = mapped_column(primary_key=True)
    problem_question: Mapped[str]
    problem_answer: Mapped[str]
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True))
