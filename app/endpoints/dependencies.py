from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio.session import AsyncSession

from app.pkg.postgres import get_session


Session = Annotated[AsyncSession, Depends(get_session)]
