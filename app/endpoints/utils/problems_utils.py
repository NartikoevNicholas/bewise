import json

from typing import List

from aiohttp import ClientSession

from sqlalchemy.ext.asyncio import AsyncSession

from app.endpoints.crud import CRUDProblem
from app.endpoints.schemas import ProblemDto


async def get_problems(session: AsyncSession, count: int) -> List[ProblemDto]:
    res = []

    while count > len(res):
        async with ClientSession() as client:
            response = await client.get(f'https://jservice.io/api/random?count={count}')
            problems = json.loads(await response.text())

        for problem in problems:
            data = ProblemDto(
                id=problem['id'],
                problem_question=problem['question'],
                problem_answer=problem['answer'],
                created_at=problem['created_at']
            )

            result = await CRUDProblem.insert(session, data)

            if result:
                res.append(result)
                count -= 1

    return res
