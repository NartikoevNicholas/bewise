from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

from app.conf import settings


class SessionManager:
    def __init__(self) -> None:
        self._engine = create_async_engine(
            settings.POSTGRES.postgres_async_url,
            pool_pre_ping=True,
            future=True
        )

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SessionManager, cls).__new__(cls)
        return cls.instance  # noqa

    def get_session(self) -> async_sessionmaker:
        return async_sessionmaker(self._engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    session_maker = SessionManager().get_session()
    async with session_maker() as session:
        yield session
