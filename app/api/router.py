from fastapi import APIRouter
from pydantic import BaseModel

from app.api.routes import (
    users as user_api,
    questions as question_api, 
    results as result_api,
    tests as test_api,
    auth as auth_api,
)

class Health(BaseModel):
    status: str = 'OK'

router = APIRouter()

@router.get(
    '/health',
    response_model=Health,
)
def health():
    """
    Check health of the application
    """

    return Health()


router.include_router(
    auth_api.router, 
    tags=["auth"], 
    prefix="/auth"
)

router.include_router(
    user_api.router, 
    tags=["users"], 
    prefix="/users"
)

router.include_router(
    test_api.router, 
    tags=["tests"], 
    prefix="/tests"
)

router.include_router(
    question_api.router, 
    tags=["questions"], 
    prefix="/questions"
)

router.include_router(
    result_api.router, 
    tags=["results"], 
    prefix="/results"
)