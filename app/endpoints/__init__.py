from .api.v1.problems import router as problem_router


routers = [
    problem_router
]


__all__ = [
    'routers'
]
