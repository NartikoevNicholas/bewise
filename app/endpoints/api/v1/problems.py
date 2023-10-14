from typing import List

from fastapi import APIRouter

from app.endpoints.utils.problems_utils import get_problems
from app.endpoints.dependencies import Session
from app.endpoints.schemas import (
    CreateProblemRequest,
    ProblemDto
)


router = APIRouter(
    prefix='/problem'
)


@router.post(
    path='/create'
)
async def problems_create(session: Session, data: CreateProblemRequest) -> List[ProblemDto]:
    try:
        problems = await get_problems(session, data.questions_num)
        return problems
    except Exception:
        await session.rollback()
        raise
