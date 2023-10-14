from typing import Optional

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.pkg.postgres import Problem
from app.endpoints.schemas import ProblemDto


class CRUDProblem:

    @staticmethod
    async def insert(session: AsyncSession, data: ProblemDto) -> Optional[ProblemDto]:
        async with session as conn:
            response = await conn.execute(
                insert(Problem)
                .values(**data.model_dump())
                .on_conflict_do_nothing()
                .returning(Problem)
            )
            result = response.scalar_one_or_none()
            await conn.commit()

        return ProblemDto.model_validate(result) if result else None
