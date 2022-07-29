from fastapi import APIRouter, Response

from app.models.schemas.tests import TestInCreate, TestInResponse
from app.models.schemas.user_tests import UserTestInCreate
from app.services.tests import TestService


router = APIRouter()

test_service = TestService()

@router.post(
    "",
    response_model=TestInResponse,
)
def create_test(new_test: TestInCreate):
    
    return test_service.create_test(new_test)

@router.post(
    "/take",
)
def take_test(user_test_in: UserTestInCreate):
    
    return test_service.take_test(user_test_in)

@router.get(
    "/user/{user_id}",
)
def get_user_tests(user_id: str):

    return test_service.get_user_tests(user_id)
