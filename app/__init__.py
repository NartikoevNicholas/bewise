from fastapi import FastAPI

from app.conf import settings
from app.endpoints import routers


def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL
    )

    for router in routers:
        app.include_router(router)

    return app


__all__ = [
    'get_application'
]
