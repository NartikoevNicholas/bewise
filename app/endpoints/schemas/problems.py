import datetime

from pydantic import (
    ConfigDict,
    BaseModel,
    Field
)


class CreateProblemRequest(BaseModel):
    questions_num: int = Field(1, ge=0)


class ProblemDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    problem_question: str
    problem_answer: str
    created_at: datetime.datetime
